#!/usr/bin/env python3
"""
Competitor Tracker - snapshot a competitor's public page and diff it against
the last snapshot to spot pricing/messaging changes.

Limitation (disclosed, not hidden): this fetches raw HTML over HTTP and
strips tags with a regex, no JS rendering. Pages that build pricing with
client-side JavaScript will not show real content here — check manually.

Usage:
    python competitor_tracker.py snapshot --url https://example.com/pricing --name acme
    python competitor_tracker.py diff --name acme
    python competitor_tracker.py check-all --config competitors.json
"""

import difflib
import json
import re
import sys
import urllib.request
from datetime import datetime, timezone
from pathlib import Path

import click

DEFAULT_DIR = "snapshots"
USER_AGENT = "competitor-tracker/1.0 (+marketing-hub internal tool)"
PRICE_RE = re.compile(r"(?:R\$\s?\d[\d.,]*|\$\s?\d[\d.,]*)")


def fetch_text(url: str) -> str:
    """Fetch a URL and strip it down to plain text (no JS rendering)."""
    req = urllib.request.Request(url, headers={"User-Agent": USER_AGENT})
    with urllib.request.urlopen(req, timeout=20) as resp:
        html = resp.read().decode(resp.headers.get_content_charset() or "utf-8", errors="replace")

    html = re.sub(r"(?is)<(script|style)[^>]*>.*?</\1>", " ", html)
    text = re.sub(r"(?s)<[^>]+>", " ", html)
    text = re.sub(r"&nbsp;", " ", text)
    text = re.sub(r"[ \t]+", " ", text)
    text = "\n".join(line.strip() for line in text.splitlines() if line.strip())
    return text


def snapshot_dir(base_dir: str, name: str) -> Path:
    d = Path(base_dir) / name
    d.mkdir(parents=True, exist_ok=True)
    return d


def latest_snapshots(base_dir: str, name: str, count: int = 2) -> list:
    d = snapshot_dir(base_dir, name)
    files = sorted(d.glob("*.txt"))
    return files[-count:]


def take_snapshot(url: str, name: str, base_dir: str) -> Path:
    text = fetch_text(url)
    ts = datetime.now(timezone.utc).strftime("%Y%m%dT%H%M%SZ")
    out = snapshot_dir(base_dir, name) / f"{ts}.txt"
    out.write_text(text, encoding="utf-8")
    return out


def diff_snapshots(older: Path, newer: Path) -> list:
    old_lines = older.read_text(encoding="utf-8").splitlines()
    new_lines = newer.read_text(encoding="utf-8").splitlines()
    diff = list(difflib.unified_diff(old_lines, new_lines, lineterm="", n=0))
    return [l for l in diff if l.startswith(("+", "-")) and not l.startswith(("+++", "---"))]


def price_changes(changed_lines: list) -> list:
    return [l for l in changed_lines if PRICE_RE.search(l)]


@click.group()
def cli():
    """Competitor page tracker (snapshot + diff, static HTML only)."""
    pass


@cli.command()
@click.option("--url", "-u", required=True, help="Competitor page URL (pricing, changelog, etc.)")
@click.option("--name", "-n", required=True, help="Short id for this competitor, used as folder name")
@click.option("--dir", "-d", "base_dir", default=DEFAULT_DIR, help="Where snapshots are stored")
def snapshot(url: str, name: str, base_dir: str):
    """Fetch URL and save a new timestamped snapshot."""
    out = take_snapshot(url, name, base_dir)
    text = out.read_text(encoding="utf-8")
    prices = sorted(set(PRICE_RE.findall(text)))
    click.echo(f"Snapshot salvo: {out}")
    if prices:
        click.echo(f"Preços encontrados no texto: {', '.join(prices[:20])}")


@cli.command()
@click.option("--name", "-n", required=True, help="Competitor id")
@click.option("--dir", "-d", "base_dir", default=DEFAULT_DIR, help="Where snapshots are stored")
def diff(name: str, base_dir: str):
    """Diff the last 2 snapshots of a competitor."""
    files = latest_snapshots(base_dir, name)
    if len(files) < 2:
        raise click.ClickException(f"Preciso de 2 snapshots de '{name}' para comparar; tenho {len(files)}. Rode 'snapshot' de novo depois de um tempo.")

    older, newer = files[-2], files[-1]
    changed = diff_snapshots(older, newer)
    click.echo(f"Comparando {older.name} -> {newer.name}")
    if not changed:
        click.echo("Sem mudanças de texto detectadas.")
        return

    prices = price_changes(changed)
    if prices:
        click.echo("\n⚠ Mudanças envolvendo preço:")
        for line in prices:
            click.echo(f"  {line}")

    click.echo(f"\nTotal de linhas alteradas: {len(changed)}")
    for line in changed[:40]:
        click.echo(f"  {line}")
    if len(changed) > 40:
        click.echo(f"  ... e mais {len(changed) - 40} linha(s)")


@cli.command("check-all")
@click.option("--config", "-c", required=True, help="JSON file: [{\"name\": ..., \"url\": ...}, ...]")
@click.option("--dir", "-d", "base_dir", default=DEFAULT_DIR, help="Where snapshots are stored")
def check_all(config: str, base_dir: str):
    """Snapshot every competitor in the config file and report who changed."""
    raw = sys.stdin.read() if config == "-" else open(config, encoding="utf-8").read()
    try:
        competitors = json.loads(raw)
    except json.JSONDecodeError as exc:
        raise click.ClickException(f"JSON inválido em '{config}': {exc}")

    any_changed = False
    for entry in competitors:
        name, url = entry["name"], entry["url"]
        had_before = len(latest_snapshots(base_dir, name, count=1)) == 1
        take_snapshot(url, name, base_dir)
        if not had_before:
            click.echo(f"{name}: primeiro snapshot, sem comparação ainda.")
            continue

        files = latest_snapshots(base_dir, name)
        changed = diff_snapshots(files[-2], files[-1])
        if changed:
            any_changed = True
            prices = price_changes(changed)
            flag = " (inclui preço)" if prices else ""
            click.echo(f"{name}: {len(changed)} linha(s) mudaram{flag}")
        else:
            click.echo(f"{name}: sem mudanças")

    if not any_changed:
        click.echo("\nNenhum concorrente mudou desde o último snapshot.")


if __name__ == "__main__":
    cli()
