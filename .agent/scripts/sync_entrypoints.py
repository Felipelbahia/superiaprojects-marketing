#!/usr/bin/env python3
"""
sync_entrypoints.py - Multi-AI discovery sync and validation.

Source of truth is `.agent/` (Google Antigravity reads it natively). Other AIs only
see what is exposed in their own folders, so this script keeps those as SYMLINKS:

    .agent/skills/<n>/        -> .claude/skills/<n>
    .agent/agents/<n>.md      -> .claude/agents/<n>.md      (Claude Code; Cursor also reads it)
    .agent/workflows/<n>.md   -> .claude/commands/<n>.md    (Claude Code slash commands)
                              -> .cursor/commands/<n>.md    (Cursor)

Usage (run from the project root):
    python .agent/scripts/sync_entrypoints.py              # create/repair symlinks, then validate
    python .agent/scripts/sync_entrypoints.py --check      # validate only, exit 1 on errors
    python .agent/scripts/sync_entrypoints.py --write-docs # refresh counts block in ARCHITECTURE.md/README.md

Only symlinks are ever created or removed; a real file or folder in a target is reported, never touched.
"""

import argparse
import os
import re
import sys
from pathlib import Path

ROOT = Path.cwd()
AGENT = ROOT / ".agent"

# (source dir, kind, target dir, relative prefix from target dir back to project root)
LINKS = [
    ("skills", "dir", ".claude/skills"),
    ("agents", "file", ".claude/agents"),
    ("workflows", "file", ".claude/commands"),
    ("workflows", "file", ".cursor/commands"),
]

COUNT_START = "<!-- kit-counts:start -->"
COUNT_END = "<!-- kit-counts:end -->"


def frontmatter(path: Path) -> dict:
    text = path.read_text(encoding="utf-8", errors="ignore")
    m = re.match(r"---\n(.*?)\n---", text, re.S)
    if not m:
        return {}
    return {k.strip(): v.strip().strip("\"'") for k, v in re.findall(r"^([A-Za-z_-]+):\s*(.*)$", m.group(1), re.M)}


def sources(kind_dir: str, kind: str):
    base = AGENT / kind_dir
    if not base.is_dir():
        return []
    if kind == "dir":
        return sorted(p for p in base.iterdir() if p.is_dir() and (p / "SKILL.md").exists())
    return sorted(p for p in base.glob("*.md"))  # top level only: _arquivo/ stays hidden


def sync_links(check_only: bool) -> list[str]:
    problems = []
    for kind_dir, kind, target_rel in LINKS:
        srcs = sources(kind_dir, kind)
        if not srcs:
            continue
        target = ROOT / target_rel
        if not check_only:
            target.mkdir(parents=True, exist_ok=True)
        depth = len(Path(target_rel).parts)
        wanted = {}
        for s in srcs:
            wanted[s.name] = os.path.join(*([".."] * depth), ".agent", kind_dir, s.name)
        for name, rel in wanted.items():
            link = target / name
            if link.is_symlink() and os.readlink(link) == rel and link.exists():
                continue
            if link.is_symlink() and link.exists():
                problems.append(f"symlink points elsewhere, left untouched: {target_rel}/{name} -> {os.readlink(link)}")
                continue
            if link.exists():
                problems.append(f"REAL (not symlink) in {target_rel}: {name} - resolve by hand")
                continue
            if check_only:
                problems.append(f"missing/broken symlink: {target_rel}/{name}")
            else:
                if link.is_symlink():
                    link.unlink()
                link.symlink_to(rel)
                print(f"  linked {target_rel}/{name}")
        if target.is_dir():
            for existing in target.iterdir():
                if not existing.is_symlink() or existing.name in wanted:
                    continue
                raw = os.readlink(existing)
                ours = (not os.path.isabs(raw) and raw.startswith("../") and "/.agent/" in raw) and not existing.exists()
                if not ours:
                    continue  # only dangling links we could have created; absolute/foreign links are never removed
                if check_only:
                    problems.append(f"orphan symlink: {target_rel}/{existing.name}")
                else:
                    existing.unlink()
                    print(f"  removed orphan {target_rel}/{existing.name}")
    return problems


def validate() -> tuple[list[str], dict]:
    errors = []
    skills = sources("skills", "dir")
    skill_names = {p.name for p in skills}
    for s in skills:
        fm = frontmatter(s / "SKILL.md")
        if not fm.get("description"):
            errors.append(f"skill without description: {s.name}")
    agents = sources("agents", "file")
    for a in agents:
        fm = frontmatter(a)
        if fm.get("name") != a.stem:
            errors.append(f"agent name != filename: {a.name} (name: {fm.get('name')!r})")
        if not fm.get("description"):
            errors.append(f"agent without description: {a.name}")
        for ref in re.split(r"[,\s]+", fm.get("skills", "")):
            if ref and ref.split("/")[0] not in skill_names:
                errors.append(f"agent {a.stem} references missing skill: {ref}")
    workflows = sources("workflows", "file")
    for w in workflows:
        if not frontmatter(w).get("description"):
            errors.append(f"workflow without description: {w.name}")
    checklist = AGENT / "scripts" / "checklist.py"
    if checklist.exists():
        for rel in re.findall(r'"(\.agent/skills/[^"]+\.py)"', checklist.read_text(encoding="utf-8")):
            if not (ROOT / rel).exists():
                errors.append(f"checklist.py points to missing script: {rel}")
    scripts = sorted(p for p in AGENT.glob("skills/*/scripts/*") if p.is_file() and p.name != "__pycache__")
    counts = {"agents": len(agents), "skills": len(skills), "workflows": len(workflows), "skill_scripts": len(scripts)}
    return errors, counts


def write_docs(counts: dict) -> None:
    block = (
        f"{COUNT_START}\n"
        f"**{counts['agents']} agents** · **{counts['skills']} skills** · **{counts['workflows']} workflows** · "
        f"**{counts['skill_scripts']} scripts inside skills** "
        f"(generated by `.agent/scripts/sync_entrypoints.py --write-docs`)\n"
        f"{COUNT_END}"
    )
    for doc in (AGENT / "ARCHITECTURE.md", ROOT / "README.md"):
        if not doc.exists():
            continue
        text = doc.read_text(encoding="utf-8")
        if COUNT_START not in text:
            print(f"  skip {doc.relative_to(ROOT)} (no {COUNT_START} marker)")
            continue
        new = re.sub(re.escape(COUNT_START) + r".*?" + re.escape(COUNT_END), lambda _: block, text, flags=re.S)
        if new != text:
            doc.write_text(new, encoding="utf-8")
            print(f"  updated counts in {doc.relative_to(ROOT)}")


def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("--check", action="store_true")
    ap.add_argument("--write-docs", action="store_true")
    ap.add_argument("--catalog", action="store_true", help="Regenerate unified catalog (CATALOG.md and catalog.html)")
    args = ap.parse_args()

    if not AGENT.is_dir():
        print("No .agent/ folder in the current directory.")
        return 1
    problems = sync_links(check_only=args.check)
    errors, counts = validate()
    print(f"agents={counts['agents']} skills={counts['skills']} workflows={counts['workflows']} skill_scripts={counts['skill_scripts']}")
    if args.write_docs:
        write_docs(counts)
    if args.catalog:
        catalog_script = AGENT / "scripts" / "generate_catalog.py"
        if catalog_script.exists():
            print("Regenerating catalog...")
            import subprocess
            subprocess.run([sys.executable, str(catalog_script)], check=False)
    for line in problems + errors:
        print(f"  ERROR: {line}")
    if problems or errors:
        return 1
    print("OK: all AI entrypoints in sync and valid")
    return 0


if __name__ == "__main__":
    sys.exit(main())
