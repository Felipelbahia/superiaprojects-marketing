#!/usr/bin/env python3
"""
Win/Loss Analyzer - win rate, reason frequency, and significance of
differences by competitor, segment and deal-size bucket.

Usage:
    python win_loss_analyzer.py analyze --file deals.csv
    python win_loss_analyzer.py analyze --file deals.csv --json

deals.csv columns (header required):
    deal_id,outcome,reason,competitor,segment,deal_size,close_date
    outcome is "won" or "lost". competitor/segment/deal_size/close_date may be blank.
"""

import csv
import json
import math
import sys
from collections import Counter, defaultdict
from statistics import NormalDist

import click


def read_deals(path: str) -> list:
    raw = sys.stdin.read() if path == "-" else open(path, encoding="utf-8").read()
    reader = csv.DictReader(raw.splitlines())
    deals = []
    for row in reader:
        outcome = (row.get("outcome") or "").strip().lower()
        if outcome not in ("won", "lost"):
            continue
        row["outcome"] = outcome
        try:
            row["deal_size"] = float(row["deal_size"]) if row.get("deal_size") else None
        except ValueError:
            row["deal_size"] = None
        deals.append(row)
    if not deals:
        raise click.ClickException("Nenhuma linha com outcome 'won'/'lost' encontrada no CSV.")
    return deals


def win_rate(deals: list) -> tuple:
    won = sum(1 for d in deals if d["outcome"] == "won")
    return won, len(deals), (won / len(deals) if deals else 0.0)


def z_test_vs_baseline(won: int, n: int, baseline_rate: float, baseline_n: int) -> tuple:
    """Two-proportion z-test: does this subgroup's win rate differ from the baseline?
    Returns (z, p_value). Same formula as growth-testes-ab/scripts/ab_test_stats.py."""
    if n == 0 or baseline_n == 0:
        return 0.0, 1.0
    rate = won / n
    p_pool = (rate * n + baseline_rate * baseline_n) / (n + baseline_n)
    se = math.sqrt(p_pool * (1 - p_pool) * (1 / n + 1 / baseline_n)) if 0 < p_pool < 1 else 0
    if se == 0:
        return 0.0, 1.0
    z = (rate - baseline_rate) / se
    p = 2 * (1 - 0.5 * (1 + math.erf(abs(z) / math.sqrt(2))))
    return z, p


def group_win_rates(deals: list, key: str, overall_rate: float, overall_n: int) -> list:
    buckets = defaultdict(list)
    for d in deals:
        val = (d.get(key) or "").strip() or "(sem dado)"
        buckets[val].append(d)

    rows = []
    for val, group in sorted(buckets.items(), key=lambda kv: -len(kv[1])):
        won, n, rate = win_rate(group)
        z, p = z_test_vs_baseline(won, n, overall_rate, overall_n)
        rows.append({"value": val, "won": won, "n": n, "win_rate": rate, "z": z, "p_value": p, "significant": p < 0.05 and n >= 5})
    return rows


def size_buckets(deals: list, overall_rate: float, overall_n: int) -> list:
    sized = [d for d in deals if d["deal_size"] is not None]
    if len(sized) < 6:
        return []
    sizes = sorted(d["deal_size"] for d in sized)
    t1 = sizes[len(sizes) // 3]
    t2 = sizes[2 * len(sizes) // 3]

    def label(size):
        if size <= t1:
            return f"Baixo (≤ {t1:,.0f})"
        if size <= t2:
            return f"Médio ({t1:,.0f}-{t2:,.0f})"
        return f"Alto (> {t2:,.0f})"

    buckets = defaultdict(list)
    for d in sized:
        buckets[label(d["deal_size"])].append(d)

    rows = []
    for val, group in buckets.items():
        won, n, rate = win_rate(group)
        z, p = z_test_vs_baseline(won, n, overall_rate, overall_n)
        rows.append({"value": val, "won": won, "n": n, "win_rate": rate, "z": z, "p_value": p, "significant": p < 0.05 and n >= 5})
    return rows


def reason_frequency(deals: list, outcome: str, top: int = 10) -> list:
    reasons = Counter((d.get("reason") or "(sem motivo)").strip() for d in deals if d["outcome"] == outcome)
    return reasons.most_common(top)


def build_report(deals: list) -> dict:
    won, n, rate = win_rate(deals)
    return {
        "overall": {"won": won, "n": n, "win_rate": rate},
        "by_competitor": group_win_rates(deals, "competitor", rate, n),
        "by_segment": group_win_rates(deals, "segment", rate, n),
        "by_deal_size": size_buckets(deals, rate, n),
        "top_loss_reasons": reason_frequency(deals, "lost"),
        "top_win_reasons": reason_frequency(deals, "won"),
    }


def print_report(report: dict):
    o = report["overall"]
    print("\n" + "=" * 60)
    print("WIN/LOSS ANALYSIS")
    print("=" * 60)
    print(f"\nOverall: {o['won']}/{o['n']} won ({o['win_rate']*100:.1f}%)")

    def print_group(title: str, rows: list):
        if not rows:
            return
        print(f"\n{title}")
        print("-" * 60)
        for r in rows:
            flag = "  ⚠ diferença significativa vs. baseline" if r["significant"] else ""
            print(f"  {r['value']:<28} {r['won']}/{r['n']} ({r['win_rate']*100:.1f}%){flag}")

    print_group("Por competidor", report["by_competitor"])
    print_group("Por segmento", report["by_segment"])
    print_group("Por faixa de tamanho de negócio", report["by_deal_size"])

    def print_reasons(title: str, reasons: list):
        if not reasons:
            return
        print(f"\n{title}")
        print("-" * 60)
        for reason, count in reasons:
            print(f"  {count:>3}x  {reason}")

    print_reasons("Principais motivos de perda", report["top_loss_reasons"])
    print_reasons("Principais motivos de ganho", report["top_win_reasons"])
    print(
        "\nNota: 'diferença significativa' usa teste z de duas proporções contra a taxa geral "
        "(mesma fórmula do growth-testes-ab/scripts/ab_test_stats.py), só marcado quando n ≥ 5 "
        "no grupo — abaixo disso a amostra é pequena demais para confiar no teste."
    )


@click.group()
def cli():
    """Win/Loss Analyzer."""
    pass


@cli.command()
@click.option("--file", "-f", "file_path", required=True, help="CSV file with deals (pass '-' for stdin)")
@click.option("--json", "-j", "as_json", is_flag=True, help="Print machine-readable JSON instead of text")
def analyze(file_path: str, as_json: bool):
    """Analyze a CSV of won/lost deals."""
    deals = read_deals(file_path)
    report = build_report(deals)
    if as_json:
        click.echo(json.dumps(report, ensure_ascii=False, indent=2))
    else:
        print_report(report)


if __name__ == "__main__":
    cli()
