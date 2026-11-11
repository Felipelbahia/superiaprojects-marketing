#!/usr/bin/env python3
"""
build_sip_index.py - Regenerates the skills table inside the sip-marketing resolver.

Reads the `description` of every .agent/skills/<name>/SKILL.md in this hub and rewrites
only the block between the markers in .agent/skills/sip-marketing/SKILL.md.

Usage (from the hub root):
    python3 .agent/scripts/build_sip_index.py          # rewrite the table
    python3 .agent/scripts/build_sip_index.py --check  # exit 1 if the table is stale

Standard library only (no PyYAML): handles plain, quoted and block (| or >) descriptions.
"""

import re
import sys
from collections import defaultdict
from pathlib import Path

HUB_ROOT = Path(__file__).resolve().parents[2]
SKILLS_DIR = HUB_ROOT / ".agent" / "skills"
RESOLVER = SKILLS_DIR / "sip-marketing" / "SKILL.md"
EXCLUDED = {"sip-marketing"}

START = "<!-- skills:start (gerado por .agent/scripts/build_sip_index.py — não edite à mão) -->"
END = "<!-- skills:end -->"

# Text after this marker is the "do not use" part; the table keeps only the trigger part.
NEGATIVE_SPLIT = re.compile(r"\s+N[ÃA]O use\b", re.IGNORECASE)


def read_frontmatter(path: Path) -> list:
    lines = path.read_text(encoding="utf-8").splitlines()
    if not lines or lines[0].strip() != "---":
        return []
    for i in range(1, len(lines)):
        if lines[i].strip() == "---":
            return lines[1:i]
    return []


def parse_description(fm: list) -> str:
    for i, line in enumerate(fm):
        if not line.startswith("description:"):
            continue
        value = line[len("description:"):].strip()
        if value and value[0] in "|>":
            block = []
            for nxt in fm[i + 1:]:
                if nxt.strip() == "" or nxt.startswith((" ", "\t")):
                    block.append(nxt.strip())
                else:
                    break
            return " ".join(part for part in block if part)
        if len(value) >= 2 and value[0] == value[-1] and value[0] in "\"'":
            value = value[1:-1]
        return value
    return ""


def clean(desc: str) -> str:
    desc = desc.replace("&gt;", ">").replace("&lt;", "<").replace("&amp;", "&")
    desc = NEGATIVE_SPLIT.split(desc, maxsplit=1)[0].strip()
    desc = re.sub(r"\s+", " ", desc).replace("|", "\\|")
    return desc or "(sem description)"


def build_table() -> str:
    groups = defaultdict(list)
    for skill_md in sorted(SKILLS_DIR.glob("*/SKILL.md")):
        name = skill_md.parent.name
        if name in EXCLUDED or name.startswith(("_", ".")):
            continue
        desc = clean(parse_description(read_frontmatter(skill_md)))
        groups[name.split("-", 1)[0]].append((name, desc))

    total = sum(len(v) for v in groups.values())
    out = [START, "", f"Total: {total} skills.", ""]
    for prefix in sorted(groups):
        out += [f"### {prefix}", "", "| Skill | Use quando |", "| --- | --- |"]
        out += [f"| `{name}` | {desc} |" for name, desc in groups[prefix]]
        out.append("")
    out.append(END)
    return "\n".join(out)


def main() -> int:
    content = RESOLVER.read_text(encoding="utf-8")
    pattern = re.compile(re.escape(START) + r".*?" + re.escape(END), re.DOTALL)
    if not pattern.search(content):
        print(f"Markers not found in {RESOLVER}", file=sys.stderr)
        return 2
    updated = pattern.sub(lambda _: build_table(), content, count=1)
    if "--check" in sys.argv:
        if updated != content:
            print("sip-marketing skills table is stale: run build_sip_index.py", file=sys.stderr)
            return 1
        print("sip-marketing skills table is up to date")
        return 0
    if updated != content:
        RESOLVER.write_text(updated, encoding="utf-8")
        print(f"Updated {RESOLVER.relative_to(HUB_ROOT)}")
    else:
        print("No changes")
    return 0


if __name__ == "__main__":
    sys.exit(main())
