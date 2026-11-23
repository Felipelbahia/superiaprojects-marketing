#!/usr/bin/env python3
"""check_local_rules.py - did a rules update keep the project's own rules, whole, and drop the old generic text?

Usage:
  check_local_rules.py <old-rules-file> <new-rules-file> [--adapted adaptadas.md] [--baseline FILE]
  check_local_rules.py --build-baseline OUT <old-rules-file>...

Own rule = a line of the old file that is not generic (generic = in the baseline of old-kit text or in the
current kit modules). Every own rule must be in the new file, whole. A line that appears only cut short, or not
at all, is reported. A line listed in the adapted file (one old snippet per line: rules rewritten on purpose)
is accepted. Old generic text that survives in the new file's `## Local rules` is reported as junk.
The baseline holds the lines that repeat in 2 or more old files (text of the old kit, not of one project).
Exit 0 = ok, 1 = findings, 2 = usage error. Output names lines, never needs secrets.
"""

import argparse
import difflib
import re
import sys
import unicodedata
from collections import Counter
from pathlib import Path

KIT = Path(__file__).resolve().parent.parent
MODULES = KIT / "skills" / "project-initializer" / "modules"
DEFAULT_BASELINE = KIT / "skills" / "project-initializer" / "legacy-generic-lines.txt"
MIN_LEN = 15
MIN_WORDS = 3  # one-word lines (mermaid keywords, bare tokens) are never rules
SIMILAR = 0.9  # a line this close to a generic line is generic too (the old kit text was edited per project)
MIN_FILES = 2
EXEMPT_HEADINGS = {"stack", "project"}  # rebuilt from the project, not carried line by line


def norm(line: str) -> str:
    text = "".join(c for c in line if not unicodedata.category(c).startswith("S"))
    return re.sub(r"\s+", " ", text).strip()


def heading_key(line: str) -> str:
    return norm(line).lower()


def sections(text: str) -> list[tuple[str, list[str]]]:
    """[(heading line or '', content lines)] split at every markdown heading outside code fences."""
    out: list[tuple[str, list[str]]] = []
    head, fence = "", False
    body: list[str] = []
    for raw in text.splitlines():
        if raw.strip().startswith(("```", "~~~")):
            fence = not fence
            continue
        if not fence and re.match(r"#{1,6} ", raw):
            out.append((head, body))
            head, body = raw, []
            continue
        body.append(raw)
    out.append((head, body))
    return out


def shown(line: str) -> str:
    """Printable form: long token-like words are hidden, so a secret inside a rule never reaches the terminal."""
    return re.sub(r"[A-Za-z0-9_+/=-]{20,}", lambda m: "<hidden>" if re.search(r"\d", m.group()) and re.search(r"[A-Za-z]", m.group()) else m.group(), line)


def own_candidates(text: str) -> list[str]:
    """Lines that carry content: long enough, not a table rule or a code fence."""
    out, fence = [], False
    for raw in text.splitlines():
        if raw.strip().startswith(("```", "~~~")):
            fence = not fence
            continue
        n = norm(raw)
        if len(n) < MIN_LEN or len(n.split()) < MIN_WORDS or re.fullmatch(r"[|\-: ]+", n):
            continue
        out.append(n)
    return out


def read(path: Path) -> str:
    return path.read_text(encoding="utf-8") if path.is_file() else ""


def generic_set(baseline: Path) -> set[str]:
    lines = set(read(baseline).splitlines())
    for module in MODULES.glob("*.md"):
        text = read(module)
        lines.update(own_candidates(text))
        lines.update("#" + heading_key(h) for h, _ in sections(text) if h)
    return lines


def is_generic(line: str, generic: set[str], by_len: dict) -> bool:
    if line in generic:
        return True
    n = len(line)
    for size in range(int(n * 0.85), int(n * 1.18) + 1):
        for g in by_len.get(size, ()):
            if difflib.SequenceMatcher(None, line, g, autojunk=False).ratio() >= SIMILAR:
                return True
    return False


def index_by_len(generic: set[str]) -> dict:
    out: dict = {}
    for g in generic:
        if not g.startswith("#"):
            out.setdefault(len(g), []).append(g)
    return out


def local_rules_section(text: str) -> str:
    match = re.search(r"^## Local rules\s*$", text, re.MULTILINE)
    return text[match.end():] if match else text


def review_text(old_text: str) -> str:
    """The old file's own lines (not generic kit text), grouped under their headings, for a human to classify."""
    generic = generic_set(DEFAULT_BASELINE)
    out = []
    for head, body in sections(old_text):
        if re.sub(r"^#+\s*", "", heading_key(head)) in EXEMPT_HEADINGS if head else False:
            continue
        keep = [l for l in body if len(norm(l)) >= MIN_LEN and norm(l) not in generic
                and not re.fullmatch(r"[|\-: ]+", norm(l))]
        if keep:
            out.append((re.sub(r"^#+", "####", head.strip()) + "\n" if head else "") + "\n".join(keep))
    return "\n\n".join(out)


def build_baseline(out: Path, files: list[Path]) -> int:
    seen: Counter = Counter()
    for f in files:
        text = read(f)
        seen.update(set(own_candidates(text)))
        seen.update({"#" + heading_key(h) for h, _ in sections(text) if h})
    lines = sorted(line for line, n in seen.items() if n >= MIN_FILES)
    out.write_text("\n".join(lines) + "\n", encoding="utf-8")
    print(f"baseline: {len(lines)} lines repeated in 2+ of {len(files)} files -> {out}")
    return 0


def findings(old_path: Path, new_path: Path, adapted_path: Path | None = None, baseline: Path = DEFAULT_BASELINE):
    """(cut, missing, junk) lists of lines."""
    generic = generic_set(baseline)
    adapted = {norm(l) for l in read(adapted_path).splitlines()} if adapted_path else set()
    new_text = read(new_path)
    new_lines = set(own_candidates(new_text))

    by_len = index_by_len(generic)
    missing: list[str] = []
    cut: list[str] = []
    for head, body in sections(read(old_path)):
        key = heading_key(head) if head else ""
        title = re.sub(r"^#+\s*", "", key)
        if title in EXEMPT_HEADINGS:
            continue
        for line in dict.fromkeys(own_candidates("\n".join(body))):
            if line in new_lines or any(a and a in line for a in adapted) or is_generic(line, generic, by_len):
                continue
            (cut if any(n != line and line.startswith(n) and len(n) >= MIN_LEN for n in new_lines) else missing).append(line)
    local_text = "\n".join(l for l in local_rules_section(new_text).splitlines() if not l.lstrip().startswith(("#", "|")))
    junk = [l for l in dict.fromkeys(own_candidates(local_text)) if is_generic(l, generic, by_len)]

    return cut, missing, junk


def main() -> int:
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("files", nargs="*")
    ap.add_argument("--adapted")
    ap.add_argument("--baseline", default=str(DEFAULT_BASELINE))
    ap.add_argument("--build-baseline", metavar="OUT")
    args = ap.parse_args()
    if args.build_baseline:
        return build_baseline(Path(args.build_baseline), [Path(f) for f in args.files])
    if len(args.files) != 2:
        ap.print_usage(sys.stderr)
        return 2
    old_path, new_path = Path(args.files[0]), Path(args.files[1])
    if not old_path.is_file() or not new_path.is_file():
        print("old and new files must exist", file=sys.stderr)
        return 2
    cut, missing, junk = findings(old_path, new_path, Path(args.adapted) if args.adapted else None, Path(args.baseline))
    for title, items, hint in (
        ("own rule CUT in the new file (only a shorter start of the line is there)", cut, "restore the whole line"),
        ("own rule MISSING from the new file", missing, "carry it into ## Local rules, or list it in adaptadas.md if rewritten on purpose"),
        ("old generic kit text still in ## Local rules (junk)", junk, "remove it: the kit modules already cover it"),
    ):
        if items:
            print(f"{title}: {len(items)} ({hint})")
            for line in items:
                print(f"  - {shown(line)[:140]}")
    if cut or missing or junk:
        return 1
    print("check_local_rules: ok (every own rule whole, no old generic text)")
    return 0


if __name__ == "__main__":
    sys.exit(main())
