#!/usr/bin/env python3
"""check_personal_paths.py - fail when a versioned file carries a machine-specific absolute path.

This repo is public: paths like /Users/<name>/..., C:\\Users\\<name>\\... or file:///Users/... break
installs on other machines and leak who built it.

Usage (from the project root):
    python3 .agents/scripts/check_personal_paths.py          # scan every tracked file, exit 1 on hits
    python3 .agents/scripts/check_personal_paths.py --staged # scan only staged files (pre-commit)
"""

import re
import subprocess
import sys
from pathlib import Path

PATTERN = re.compile(r"(?i)(/Users/[A-Za-z0-9._-]+/|[A-Z]:[\\/]+Users[\\/]+[A-Za-z0-9._ -]+[\\/]|/home/(?!tools/)[a-z][a-z0-9._-]*/)")
ALLOWED = re.compile(r"(?i)/Users/(\d+|<[^>]+>|\$USER|Shared|you|username|seu-usuario|\.\.\.)/|/home/(user|username|you)/")
SELF = Path(__file__).name
SKIP_SUFFIXES = {".png", ".jpg", ".jpeg", ".gif", ".webp", ".ico", ".pdf", ".zip", ".woff", ".woff2", ".mp4", ".mp3"}


def tracked(staged: bool) -> list[str]:
    cmd = ["git", "diff", "--cached", "--name-only", "--diff-filter=ACM", "-z"] if staged else ["git", "ls-files", "-z"]
    out = subprocess.run(cmd, capture_output=True, check=True).stdout.decode("utf-8", "replace")
    return [p for p in out.split("\0") if p]


def main() -> int:
    hits = []
    for rel in tracked("--staged" in sys.argv):
        path = Path(rel)
        if path.name == SELF or path.suffix.lower() in SKIP_SUFFIXES or not path.is_file():
            continue
        try:
            text = path.read_text(encoding="utf-8")
        except (UnicodeDecodeError, OSError):
            continue
        for n, line in enumerate(text.splitlines(), 1):
            m = PATTERN.search(line)
            if m and not ALLOWED.search(m.group(0)):
                hits.append(f"{rel}:{n}: {m.group(0)}")
    if hits:
        print("Personal/absolute machine paths found (use <HUB>, relative paths or env vars):", file=sys.stderr)
        print("\n".join(hits[:60]), file=sys.stderr)
        if len(hits) > 60:
            print(f"... and {len(hits) - 60} more", file=sys.stderr)
        return 1
    print("check_personal_paths: ok")
    return 0


if __name__ == "__main__":
    sys.exit(main())
