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
import subprocess
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

# An agent that declares `autonomy` adopted the brain model (skill writing-agents).
AUTONOMY_LEVELS = ("propose", "contexts")
BRAIN_FILES = ("contextos.md", "licoes.md", "decisoes.md")

# Models mapping from Antigravity to Claude Code
MODEL_MAP_ANTIGRAVITY_TO_CLAUDE = {
    "flash_lite": "haiku",
    "flash": "haiku",
    "pro": "sonnet",
}

GENERATED_AGENT_HEADER_PREFIX = "<!-- antigravity-kit:generated"


def convert_agent_for_claude(src_path: Path, target_model: str) -> str:
    text = src_path.read_text(encoding="utf-8")
    converted = re.sub(r"^model:[ \t]*.*$", f"model: {target_model}", text, flags=re.M)
    header = f"<!-- antigravity-kit:generated from ../../.agent/agents/{src_path.name} (model: {target_model}) -->\n"
    return header + converted


def frontmatter(path: Path) -> dict:
    text = path.read_text(encoding="utf-8", errors="ignore")
    m = re.match(r"---\n(.*?)\n---", text, re.S)
    if not m:
        return {}
    return {k.strip(): v.strip().strip("\"'") for k, v in re.findall(r"^([A-Za-z_-]+):[ \t]*(.*)$", m.group(1), re.M)}


def sources(kind_dir: str, kind: str):
    base = AGENT / kind_dir
    if not base.is_dir():
        return []
    if kind == "dir":
        return sorted(p for p in base.iterdir() if p.is_dir() and (p / "SKILL.md").exists())
    return sorted(p for p in base.glob("*.md"))  # top level only: _arquivo/ stays hidden


def brain_errors(name: str, autonomy: str) -> list[str]:
    errors = []
    if autonomy not in AUTONOMY_LEVELS:
        errors.append(f"agent {name} has invalid autonomy {autonomy!r} (use one of: {', '.join(AUTONOMY_LEVELS)})")
    brain = AGENT / "agents" / "agents_brains" / name
    if not brain.is_dir():
        return [*errors, f"agent {name} has no brain: missing .agent/agents/agents_brains/{name}/"]
    errors += [f"agent {name} brain misses {item}" for item in BRAIN_FILES if not (brain / item).is_file()]
    if not (brain / "inbox").is_dir():
        errors.append(f"agent {name} brain misses inbox/")
    return errors


def is_hub_skill_link(link: Path, name: str) -> bool:
    """A skill link that goes straight to the same-named skill in another .agent/ tree (a SIP hub).

    0 Padrões keeps a real stub in .agent/skills/sip-<x> and links .claude/skills/sip-<x> to the hub
    resolver on purpose (projetos/_sips.md, "Exceção: 0 Padrões não usa o padrão duplo").
    """
    if not link.is_symlink() or not link.exists():
        return False
    return any(
        t.name == name and t.parent.name == "skills" and t.parent.parent.name == ".agent" and (t / "SKILL.md").is_file()
        for t in link_targets(link)
    )


def is_gitignored(link: Path) -> bool:
    """True when git ignores this path: a machine-local link (e.g. .claude/skills/sip-*) that a clone never has."""
    try:
        return subprocess.run(["git", "check-ignore", "-q", str(link)], cwd=ROOT, capture_output=True).returncode == 0
    except OSError:
        return False


def link_targets(path: Path) -> list[Path]:
    """The link's own target (one hop, absolute) and its fully resolved path: a hub may itself use symlinks."""
    if not path.is_symlink():
        return [path.resolve()]
    return [Path(os.path.normpath(path.parent / os.readlink(path))), path.resolve()]


def hub_skill_names(agent: Path) -> set[str]:
    """Skills of the hub an agent file really lives in, when the agent is a link from a SIP hub."""
    names = set()
    for t in link_targets(agent):
        agent_dir = t.parent.parent
        if t.parent.name != "agents" or agent_dir.name != ".agent" or agent_dir.resolve() == AGENT.resolve():
            continue
        hub_skills = agent_dir / "skills"
        if hub_skills.is_dir():
            names |= {p.name for p in hub_skills.iterdir() if (p / "SKILL.md").exists()}
    return names


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
        for s in srcs:
            name = s.name
            rel = wanted[name]
            link = target / name

            # Check if this agent needs model conversion for .claude/agents
            is_claude_agent = (kind_dir == "agents" and target_rel == ".claude/agents")
            fm = frontmatter(s) if is_claude_agent else {}
            src_model = fm.get("model", "inherit")
            target_model = MODEL_MAP_ANTIGRAVITY_TO_CLAUDE.get(src_model) if is_claude_agent else None

            if target_model:
                expected_content = convert_agent_for_claude(s, target_model)
                if link.is_symlink():
                    if check_only:
                        problems.append(f"symlink should be converted file for agent with model {src_model}: {target_rel}/{name}")
                        continue
                    link.unlink()

                if link.exists():
                    if not link.is_file():
                        problems.append(f"REAL (not file) in {target_rel}: {name} - resolve by hand")
                        continue
                    current_content = link.read_text(encoding="utf-8", errors="ignore")
                    if not current_content.startswith(GENERATED_AGENT_HEADER_PREFIX):
                        problems.append(f"REAL (not symlink) in {target_rel}: {name} - resolve by hand")
                        continue
                    if current_content != expected_content:
                        if check_only:
                            problems.append(f"out of date generated agent: {target_rel}/{name}")
                            continue
                        link.write_text(expected_content, encoding="utf-8")
                        print(f"  updated converted {target_rel}/{name}")
                    continue
                else:
                    if check_only:
                        problems.append(f"missing generated agent: {target_rel}/{name}")
                        continue
                    link.write_text(expected_content, encoding="utf-8")
                    print(f"  generated converted {target_rel}/{name}")
                    continue

            if link.is_symlink() and os.readlink(link) == rel and link.exists():
                continue
            if kind == "dir" and is_hub_skill_link(link, name):
                continue
            if link.is_symlink() and link.exists():
                problems.append(f"symlink points elsewhere, left untouched: {target_rel}/{name} -> {os.readlink(link)}")
                continue
            if link.exists():
                if is_claude_agent and link.is_file() and not link.is_symlink():
                    first_line = link.read_text(encoding="utf-8", errors="ignore").splitlines()[0] if link.stat().st_size > 0 else ""
                    if first_line.startswith(GENERATED_AGENT_HEADER_PREFIX):
                        if check_only:
                            problems.append(f"generated file should be symlink for inherit model: {target_rel}/{name}")
                            continue
                        link.unlink()
                        link.symlink_to(rel)
                        print(f"  converted back to symlink {target_rel}/{name}")
                        continue
                problems.append(f"REAL (not symlink) in {target_rel}: {name} - resolve by hand")
                continue
            if check_only:
                if not link.is_symlink() and is_gitignored(link):
                    continue  # missing, and the project's .gitignore says this link is machine-local
                problems.append(f"missing/broken symlink: {target_rel}/{name}")
            else:
                if link.is_symlink():
                    link.unlink()
                link.symlink_to(rel)
                print(f"  linked {target_rel}/{name}")
        if target.is_dir():
            for existing in target.iterdir():
                if existing.name in wanted:
                    continue
                if existing.is_symlink():
                    raw = os.readlink(existing)
                    ours = (not os.path.isabs(raw) and raw.startswith("../") and "/.agent/" in raw) and not existing.exists()
                    if not ours:
                        continue  # only dangling links we could have created; absolute/foreign links are never removed
                    if check_only:
                        problems.append(f"orphan symlink: {target_rel}/{existing.name}")
                    else:
                        existing.unlink()
                        print(f"  removed orphan {target_rel}/{existing.name}")
                elif existing.is_file():
                    first_line = existing.read_text(encoding="utf-8", errors="ignore").splitlines()[0] if existing.stat().st_size > 0 else ""
                    if first_line.startswith(GENERATED_AGENT_HEADER_PREFIX):
                        if check_only:
                            problems.append(f"orphan generated agent: {target_rel}/{existing.name}")
                        else:
                            existing.unlink()
                            print(f"  removed orphan generated {target_rel}/{existing.name}")
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
        if "autonomy" in fm:
            errors += brain_errors(a.stem, fm["autonomy"])
        known = skill_names | hub_skill_names(a)
        for ref in re.split(r"[,\s]+", fm.get("skills", "")):
            if ref and ref.split("/")[0] not in known:
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
