#!/usr/bin/env python3
"""
GEO Checker - mechanical sweep of HTML/JSX/TSX pages for AI-citation readiness.

Origin: geo-fundamentals/scripts/geo_checker.py (0 Padroes kit), adapted for the 0 Mkt hub.
Differences from the original: presence checks only (no percentage score), language-neutral
(the old text patterns such as "according to" penalised Portuguese pages), lists every file
with its issues, accepts a file or folder, Python 3.9+ standard library only.

Required (a page fails without them):
    - JSON-LD structured data (<script type="application/ld+json">)
    - author attribution (JSON-LD "author", rel="author", byline/author class)
    - publication or update date (datePublished/dateModified, <time datetime>, article:published)
    - at least two <h2> subheadings (page title heading: see seo-tecnico/scripts/seo_checker.py)
Info only (never fails): FAQ block, lists, tables, Organization/Person/Brand schema.

It does not judge quality, sources or whether numbers are real: that is the GEO checklist in
seo-geo/SKILL.md, applied by a person.

Usage:
    python3 geo_checker.py <folder-or-file> [--limit N]

Exit code: 0 = all pages have the required items, 1 = issues found. Last line is JSON.
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
    "docs", "documentation", ".venv", ".agent", ".claude",
}
SKIP_PATTERNS = [
    "config", "setup", "util", "helper", "hook", "context", "store",
    "service", "api", "lib", "constant", "type", "interface", "mock",
    ".test.", ".spec.", "_test.", "_spec.",
]
PAGE_DIRS = {"pages", "app", "routes", "views", "screens"}
PAGE_NAMES = ["page", "index", "home", "about", "contact", "blog", "post",
              "article", "product", "landing", "layout"]


def is_page_file(path: Path) -> bool:
    # HTML is always a page. SKIP_PATTERNS only apply to JSX/TSX code files.
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
        return [target]
    files = []
    for pattern in ("**/*.html", "**/*.htm", "**/*.jsx", "**/*.tsx"):
        for f in sorted(target.glob(pattern)):
            if any(part in SKIP_DIRS for part in f.relative_to(target).parts[:-1]):
                continue
            if is_page_file(f):
                files.append(f)
    return files


def check_page(path: Path):
    """Return (required_issues, info_notes)."""
    try:
        content = path.read_text(encoding="utf-8", errors="ignore")
    except Exception as exc:
        return [f"Could not read file: {exc}"], []
    low = content.lower()
    issues, info = [], []

    if "application/ld+json" not in low:
        issues.append("No JSON-LD structured data")
    if not (re.search(r"\"author\"\s*:", content) or 'rel="author"' in low or "rel='author'" in low
            or re.search(r"class=[\"'][^\"']*(byline|author)", low)):
        issues.append("No author attribution")
    if not re.search(r"datepublished|datemodified|<time[^>]+datetime=|article:published|article:modified", low):
        issues.append("No publication or update date")
    h2 = len(re.findall(r"<h2[\s>]", content, re.I))
    if h2 < 2:
        issues.append(f"Only {h2} H2 subheading(s): need at least 2")

    if re.search(r"<details|faqpage|\bfaq\b|perguntas frequentes", low):
        info.append("FAQ block found")
    if re.search(r"\"@type\"\s*:\s*\"(organization|person|localbusiness|brand)\"", low):
        info.append("Entity schema (Organization/Person/Brand) found")
    if len(re.findall(r"<(ul|ol)[\s>]", low)) >= 1:
        info.append("List(s) found")
    if "<table" in low:
        info.append("Table(s) found")
    return issues, info


def main() -> int:
    ap = argparse.ArgumentParser(description="GEO readiness presence check for HTML/JSX/TSX pages")
    ap.add_argument("target", nargs="?", default=".")
    ap.add_argument("--limit", type=int, default=200, help="max files to check (default 200)")
    args = ap.parse_args()

    target = Path(args.target).resolve()
    if not target.exists():
        print(f"[!] Not found: {target}")
        return 2
    base = target if target.is_dir() else target.parent

    print("=" * 60)
    print("  GEO CHECKER - AI citation readiness (presence only)")
    print("=" * 60)
    print(f"Target: {target}")
    print(f"Time:   {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")
    print("-" * 60)

    pages = find_pages(target)
    truncated = len(pages) > args.limit
    pages = pages[: args.limit]
    if not pages:
        print("[!] No page files found (looked for .html, .htm, .jsx, .tsx).")
        print(json.dumps({"script": "geo_checker", "files_checked": 0, "passed": True}, indent=2))
        return 0
    if truncated:
        print(f"[!] More than {args.limit} files: only the first {args.limit} were checked.")

    failing = {}
    for f in pages:
        issues, info = check_page(f)
        rel = str(f.relative_to(base))
        status = "FAIL" if issues else "OK  "
        print(f"[{status}] {rel}")
        for i in issues:
            print(f"    * {i}")
        for n in info:
            print(f"    + {n}")
        if issues:
            failing[rel] = issues

    total = sum(len(v) for v in failing.values())
    print()
    print(json.dumps({
        "script": "geo_checker",
        "target": str(target),
        "files_checked": len(pages),
        "files_with_issues": len(failing),
        "issues_found": total,
        "truncated": truncated,
        "passed": total == 0,
    }, indent=2))
    return 0 if total == 0 else 1


if __name__ == "__main__":
    sys.exit(main())
