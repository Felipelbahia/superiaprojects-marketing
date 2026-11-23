#!/usr/bin/env python3
"""
assemble_rules.py - Build a project's rules file from the kit's rule modules.

Usage (from the project root):
  python3 <kit>/.agent/scripts/assemble_rules.py --modules core,sip-access,code --title "My Project" [--out CLAUDE.md]
  python3 <kit>/.agent/scripts/assemble_rules.py --list

Modules live in .agent/skills/project-initializer/modules/<name>.md. They are concatenated in a
fixed order (never the order given) and every "## " heading outside code fences is numbered.
Re-running over a file it assembled keeps the project's ## Project, ## Stack and ## Local rules blocks
and moves other hand-written sections into ## Local rules. In ## Project, the first top-level "- Modules:" line
is rewritten with the modules used, in the fixed order; if the line is missing it is not created. Sections of
the kit and the text before the first section are regenerated, and sections of a module left out are removed;
local edits there are not kept and are reported. Code fences (``` or ~~~) are respected; an assembled file with an
unclosed fence is refused (exit 4) and left untouched (an old-model file goes by --replace); a module
with an unclosed fence stops the assembly (exit 2). A file from the old model is refused (exit 3) unless
--replace is given (back it up first). Then run sync_rules.py to copy the result to AGENTS.md
(and to .cursorrules / .claude/CLAUDE.md when they exist).
"""

import argparse
import re
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
from check_local_rules import review_text  # noqa: E402

ORDER = ["core", "sip-access", "code", "interface", "content", "automation"]
DEFAULT_DIR = Path(__file__).resolve().parent.parent / "skills" / "project-initializer" / "modules"
MARKER = "Before acting (mandatory sequence)"
KEPT_TITLES = ("Project", "Stack", "Local rules")


def assemble(names: list[str], title: str, out_name: str, modules_dir: Path) -> str:
    wanted = set(names)
    unknown = wanted - set(ORDER)
    if unknown:
        raise ValueError(f"unknown module(s): {', '.join(sorted(unknown))}. Available: {', '.join(ORDER)}")
    if "core" not in wanted:
        raise ValueError("module 'core' is mandatory")

    lines = []
    for name in (n for n in ORDER if n in wanted):
        module = (modules_dir / f"{name}.md").read_text(encoding="utf-8").rstrip("\n").split("\n")
        opener = fence_scan(module)[1]
        if opener is not None:
            raise ValueError(f"module '{name}' has an unclosed code fence opened at line {opener + 1}")
        lines += module + [""]
    number = 0
    for i, outside in enumerate(fence_states(lines)):
        if outside and lines[i].startswith("## "):
            number += 1
            lines[i] = f"## {number}. {lines[i][3:]}"
    return f"# {out_name} - {title}\n\n" + "\n".join(lines)


FENCE = re.compile(r"^ {0,3}(`{3,}|~{3,})(.*)$")


def fence_scan(lines: list[str]) -> tuple[list[bool], int | None]:
    """CommonMark-style fences (``` or ~~~, closed by the same character, at least as long, with nothing after it).
    Returns, for each line, True when it is outside a fence (fence lines count as inside), and the index of the
    opening line of a fence left unclosed (None when every fence is closed)."""
    states, opener = [], None
    for i, line in enumerate(lines):
        match = FENCE.match(line)
        if opener is None:
            if match and not (match.group(1)[0] == "`" and "`" in match.group(2)):
                opener = i
            states.append(opener is None)
        else:
            mark = FENCE.match(lines[opener]).group(1)
            if match and match.group(1)[0] == mark[0] and len(match.group(1)) >= len(mark) and not match.group(2).strip():
                opener = None
            states.append(False)
    return states, opener


def fence_states(lines: list[str]) -> list[bool]:
    """For each line: True when it is outside a code fence (fence lines count as inside)."""
    return fence_scan(lines)[0]


def unclosed_fence_line(text: str) -> int | None:
    """1-based line of a fence opened and never closed, or None."""
    opener = fence_scan(text.split("\n"))[1]
    return None if opener is None else opener + 1


def section_starts(lines: list[str]) -> list[int]:
    return [i for i, (line, outside) in enumerate(zip(lines, fence_states(lines))) if outside and line.startswith("## ")]


def split_sections(text: str) -> list[list[str]]:
    """Split at "## " lines outside code fences. Each section starts with its heading; the preamble is dropped."""
    lines = text.split("\n")
    starts = section_starts(lines)
    ends = starts[1:] + [len(lines)]
    return [lines[start:end] for start, end in zip(starts, ends)]


def preamble(text: str) -> list[str]:
    """The text before the first "## " section, trailing blank lines trimmed."""
    lines = text.split("\n")
    starts = section_starts(lines)
    return trim(lines[:starts[0]] if starts else lines)


def section_title(heading: str) -> str:
    return re.sub(r"^\d+\.\s+", "", heading[3:]).strip()


def trim(lines: list[str]) -> list[str]:
    while lines and not lines[-1].strip():
        lines = lines[:-1]
    return lines


def demote(lines: list[str]) -> list[str]:
    """Move the headings outside code fences one level down (## Deploy -> ### Deploy)."""
    return [("#" + line) if outside and re.match(r"#+ ", line) else line
            for line, outside in zip(lines, fence_states(lines))]


def normalized(section: list[str]) -> list[str]:
    """A section with its heading reduced to "## Title", trailing blank lines trimmed."""
    return trim([f"## {section_title(section[0])}", *section[1:]])


def module_sections(modules_dir: Path) -> dict[str, tuple[str, list[str]]]:
    """Title -> (module name, normalized text) for every "## " section of the module files present in modules_dir."""
    sections = {}
    for name in ORDER:
        path = modules_dir / f"{name}.md"
        if path.is_file():
            for section in split_sections(path.read_text(encoding="utf-8")):
                sections[section_title(section[0])] = (name, normalized(section))
    return sections


def reassemble(existing: str, fresh: str, used: list[str], modules_dir: Path) -> tuple[str, list[str], list[str], list[str]]:
    """Fresh module text plus the project's own blocks from an assembled file.
    Returns (text, moved titles, replaced: regenerated sections or preamble whose local text was not kept,
    removed: sections of a module left out)."""
    known = module_sections(modules_dir)
    blocks, moved, moved_texts, replaced, removed = {}, [], [], [], []
    if preamble(existing) != preamble(fresh):
        replaced.append("preamble (text before the first section)")
    for section in split_sections(existing):
        title = section_title(section[0])
        if title in known:
            module, text = known[title]
            if module not in used:
                removed.append(title)
            elif normalized(section) != text:
                replaced.append(title)
            continue
        if title in KEPT_TITLES and title not in blocks:
            blocks[title] = "\n".join(trim(section))
        else:
            moved.append(title)
            moved_texts.append("\n".join(trim(demote(section))))

    if "Project" in blocks:
        lines = blocks["Project"].split("\n")
        for i, line in enumerate(lines):
            if line.startswith("- Modules:"):
                lines[i] = f"- Modules: {', '.join(used)}"
                break
        blocks["Project"] = "\n".join(lines)
    if moved_texts:
        blocks["Local rules"] = "\n\n".join([blocks.get("Local rules", "## Local rules"), *moved_texts])

    text = fresh
    for title in KEPT_TITLES:
        if title in blocks:
            text += "\n" + blocks[title] + "\n"
    return text, moved, replaced, removed


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    parser.add_argument("--modules", help="comma-separated module names (core is mandatory)")
    parser.add_argument("--title", default="Project rules")
    parser.add_argument("--out", default="CLAUDE.md")
    parser.add_argument("--modules-dir", type=Path, default=DEFAULT_DIR)
    parser.add_argument("--replace", action="store_true",
                        help="overwrite a rules file that is not assembled from the kit modules, after you backed it up")
    parser.add_argument("--list", action="store_true", help="print the available modules in assembly order")
    args = parser.parse_args()

    if args.list:
        print("\n".join(ORDER))
        return 0
    if not args.modules:
        parser.error("--modules is required (or use --list)")

    names = [n.strip() for n in args.modules.split(",") if n.strip()]
    out = Path(args.out)
    try:
        fresh = assemble(names, args.title, out.name, args.modules_dir)
    except ValueError as err:
        print(f"❌ {err}", file=sys.stderr)
        return 2

    existing = out.read_text(encoding="utf-8") if out.exists() else ""
    moved, replaced, removed = [], [], []
    unclosed = unclosed_fence_line(existing) if MARKER in existing else None
    if unclosed is not None:
        print(f"❌ {out} has an unclosed code fence opened at line {unclosed}. Close it and rerun; nothing was written.",
              file=sys.stderr)
        return 4
    if not existing.strip():
        text = fresh
    elif MARKER in existing:
        used = [n for n in ORDER if n in names]
        text, moved, replaced, removed = reassemble(existing, fresh, used, args.modules_dir)
    elif args.replace:
        text = fresh
        review = review_text(existing)
        if review:
            text = text.rstrip("\n") + "\n\n## Local rules\n\n### A revisar (do arquivo antigo)\n\n" \
                "Classifique: regra do projeto fica inteira (e vai para o corpo de `## Local rules`); texto genérico do kit antigo sai.\n\n" \
                + review + "\n"
            print("⚠️ A revisar: the old file's own text was kept under ## Local rules / A revisar. Classify it, then run check_local_rules.py <backup> <new>.",
                  file=sys.stderr)
    else:
        print(f"❌ {out} is not assembled from the kit modules (old model). Make a backup, then rerun with --replace.",
              file=sys.stderr)
        return 3

    if moved:
        print(f"⚠️ moved to ## Local rules: {', '.join(moved)}", file=sys.stderr)
    if replaced:
        print(f"⚠️ regenerated from the kit, local text not kept (check the diff with your backup): {', '.join(replaced)}",
              file=sys.stderr)
    if removed:
        print(f"⚠️ removed (module not assembled; check the diff with your backup): {', '.join(removed)}",
              file=sys.stderr)
    out.write_text(text, encoding="utf-8")
    used = [n for n in ORDER if n in names]
    print(f"✅ {out} assembled from: {', '.join(used)}. Next: run sync_rules.py")
    return 0


if __name__ == "__main__":
    sys.exit(main())
