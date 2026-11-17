#!/usr/bin/env python3
"""
SEO Checker - mechanical sweep of HTML/JSX/TSX pages.

Origin: seo-fundamentals/scripts/seo_checker.py (0 Padroes kit), adapted for the 0 Mkt hub.

Checks, per page (presence only, it does not judge quality):
    - <title> with text
    - meta description
    - Open Graph tags (property="og:...")
    - exactly one <h1>
    - every <img> has a non-empty alt (an empty alt is fine for decorative images: review it)

Usage:
    python3 seo_checker.py <folder-or-file> [--limit N]

Exit code: 0 = no issues, 1 = issues found. Last line is a JSON summary.
Needs only the Python standard library (3.9+).
"""
import argparse
import json
import re
import sys
from datetime import datetime
from pathlib import Path

try:
    sys.stdout.reconfigure(encoding="utf-8", errors="replace")
except Exception:
    pass

SKIP_DIRS = {
    "node_modules", ".next", "dist", "build", ".git", ".github", "__pycache__",
    ".vscode", ".idea", "coverage", "test", "tests", "__tests__", "spec",
    "docs", "documentation", "examples", ".venv", ".agent", ".claude",
}

# Only for JSX/TSX: files that are code, not pages. HTML files are always pages.
SKIP_PATTERNS = [
    "config", "setup", "util", "helper", "hook", "context", "store",
    "service", "api", "lib", "constant", "type", "interface", "mock",
    ".test.", ".spec.", "_test.", "_spec.",
]
PAGE_DIRS = {"pages", "app", "routes", "views", "screens"}
PAGE_NAMES = ["page", "index", "home", "about", "contact", "blog", "post",
              "article", "product", "landing", "layout"]


def is_page_file(path: Path) -> bool:
    if path.suffix.lower() in (".html", ".htm"):
        return True
    name = path.name.lower()
    if any(s in name for s in SKIP_PATTERNS):
        return False
    if any(p.lower() in PAGE_DIRS for p in path.parts):
        return True
    return any(p in path.stem.lower() for p in PAGE_NAMES)


def find_pages(target: Path):
    if target.is_file():
        return [target], False
    files = []
    for pattern in ("**/*.html", "**/*.htm", "**/*.jsx", "**/*.tsx"):
        for f in sorted(target.glob(pattern)):
            rel_parts = f.relative_to(target).parts[:-1]
            if any(part in SKIP_DIRS for part in rel_parts):
                continue
            if is_page_file(f):
                files.append(f)
    return files, False


def check_page(path: Path) -> list:
    try:
        content = path.read_text(encoding="utf-8", errors="ignore")
    except Exception as exc:
        return [f"Could not read file: {exc}"]
    low = content.lower()
    issues = []
    # Fragments and components without <head>/<Head> are not checked for head tags.
    has_head = "<head" in low or "head>" in low
    if has_head:
        if not (re.search(r"<title[^>]*>\s*[^<\s]", content, re.I) or "<Head>" in content):
            issues.append("Missing <title> tag")
        if not re.search(r"name=[\"']description[\"']", content, re.I):
            issues.append("Missing meta description")
        if not re.search(r"property=[\"']og:", content, re.I):
            issues.append("Missing Open Graph tags")
    h1s = re.findall(r"<h1[\s>]", content, re.I)
    if not h1s:
        issues.append("Missing <h1> tag")
    elif len(h1s) > 1:
        issues.append(f"Multiple H1 tags ({len(h1s)})")
    missing = empty = 0
    for img in re.findall(r"<img\b[^>]*>", content, re.I):
        m = re.search(r"\balt=([\"'])(.*?)\1", img, re.I | re.S)
        if not m:
            missing += 1
        elif not m.group(2).strip():
            empty += 1
    if missing:
        issues.append(f"Image missing alt attribute ({missing})")
    if empty:
        issues.append(f"Image with empty alt ({empty}): ok only if decorative")
    return issues


def main() -> int:
    ap = argparse.ArgumentParser(description="SEO presence check for HTML/JSX/TSX pages")
    ap.add_argument("target", nargs="?", default=".")
    ap.add_argument("--limit", type=int, default=200, help="max files to check (default 200)")
    args = ap.parse_args()

    target = Path(args.target).resolve()
    if not target.exists():
        print(f"[!] Not found: {target}")
        return 2
    base = target if target.is_dir() else target.parent

    print("=" * 60)
    print("  SEO CHECKER")
    print("=" * 60)
    print(f"Target: {target}")
    print(f"Time:   {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")
    print("-" * 60)

    pages, _ = find_pages(target)
    truncated = len(pages) > args.limit
    pages = pages[: args.limit]
    if not pages:
        print("[!] No page files found (looked for .html, .htm, .jsx, .tsx).")
        print(json.dumps({"script": "seo_checker", "files_checked": 0, "passed": True}, indent=2))
        return 0
    if truncated:
        print(f"[!] More than {args.limit} files: only the first {args.limit} were checked.")

    results = {}
    for f in pages:
        found = check_page(f)
        if found:
            results[str(f.relative_to(base))] = found

    print(f"Checked {len(pages)} file(s).\n")
    if results:
        for rel, found in results.items():
            print(f"- {rel}")
            for issue in found:
                print(f"    * {issue}")
    else:
        print("[OK] No SEO issues found.")

    total = sum(len(v) for v in results.values())
    print()
    print(json.dumps({
        "script": "seo_checker",
        "target": str(target),
        "files_checked": len(pages),
        "files_with_issues": len(results),
        "issues_found": total,
        "truncated": truncated,
        "passed": total == 0,
    }, indent=2))
    return 0 if total == 0 else 1


if __name__ == "__main__":
    sys.exit(main())
