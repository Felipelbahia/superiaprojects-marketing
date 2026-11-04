#!/usr/bin/env python3
"""
CAC (Customer Acquisition Cost) Calculator - blended and per-channel CAC.

Usage:
    python calculate_cac.py channel --spend 15000 --customers 10 --name "LinkedIn Ads"
    python calculate_cac.py blended --file channels.json
    python calculate_cac.py blended -   (reads the same JSON from stdin)
    python calculate_cac.py benchmark --channel "Google Search"

channels.json format:
    [
      {"channel": "LinkedIn Ads", "spend": 15000, "customers": 10},
      {"channel": "Google Search", "spend": 12000, "customers": 20}
    ]
"""

import json
import sys

import click

BENCHMARKS = {
    "linkedin ads": (150, 400),
    "google search": (80, 250),
    "seo/organic": (50, 150),
    "partnerships": (100, 300),
}


def calculate_cac(spend: float, customers: int) -> float:
    """Calculate basic CAC. Returns 0.0 when there are no customers (undefined, not infinite)."""
    if customers == 0:
        return 0.0
    return round(spend / customers, 2)


def calculate_channel_cac(channel_data: list) -> dict:
    """Calculate CAC per channel plus the blended CAC across all channels."""
    results = {}
    total_spend = 0.0
    total_customers = 0

    for row in channel_data:
        name = row["channel"]
        spend = row["spend"]
        customers = row["customers"]

        results[name] = {
            "spend": spend,
            "customers": customers,
            "cac": calculate_cac(spend, customers),
        }
        total_spend += spend
        total_customers += customers

    results["blended"] = {
        "total_spend": total_spend,
        "total_customers": total_customers,
        "blended_cac": calculate_cac(total_spend, total_customers),
    }
    return results


def print_results(results: dict):
    print("\n" + "=" * 60)
    print("CAC CALCULATION RESULTS")
    print("=" * 60 + "\n")

    for channel, data in results.items():
        if channel == "blended":
            print("-" * 60)
            print("BLENDED CAC")
            print(f"  Total Spend: ${data['total_spend']:,.2f}")
            print(f"  Total Customers: {data['total_customers']:,}")
            print(f"  Blended CAC: ${data['blended_cac']:,.2f}")
        else:
            print(channel.upper())
            print(f"  Spend: ${data['spend']:,.2f}")
            print(f"  Customers: {data['customers']:,}")
            print(f"  CAC: ${data['cac']:,.2f}\n")


@click.group()
def cli():
    """CAC Calculator."""
    pass


@cli.command()
@click.option("--spend", "-s", required=True, type=float, help="Total spend on this channel")
@click.option("--customers", "-c", required=True, type=int, help="Customers acquired on this channel")
@click.option("--name", "-n", default="Channel", help="Channel name, for the printed label")
def channel(spend: float, customers: int, name: str):
    """Calculate CAC for a single channel."""
    print_results(calculate_channel_cac([{"channel": name, "spend": spend, "customers": customers}]))


@cli.command()
@click.argument("file", required=True)
def blended(file: str):
    """Calculate per-channel and blended CAC from a JSON file (pass '-' for stdin)."""
    raw = sys.stdin.read() if file == "-" else open(file, encoding="utf-8").read()
    try:
        channel_data = json.loads(raw)
    except json.JSONDecodeError as exc:
        raise click.ClickException(f"JSON inválido em '{file}': {exc}")

    if not isinstance(channel_data, list) or not channel_data:
        raise click.ClickException("Esperava uma lista não-vazia de {channel, spend, customers}.")

    print_results(calculate_channel_cac(channel_data))


@cli.command()
@click.option("--channel", "-c", "channel_name", required=True, help="Channel name")
def benchmark(channel_name: str):
    """Print the known B2B SaaS CAC benchmark range (Series A) for a channel, if known."""
    key = channel_name.strip().lower()
    if key not in BENCHMARKS:
        known = ", ".join(sorted(BENCHMARKS))
        raise click.ClickException(f"Sem benchmark para '{channel_name}'. Canais conhecidos: {known}.")
    low, high = BENCHMARKS[key]
    click.echo(f"{channel_name}: ${low}-${high} CAC (B2B SaaS, Series A)")


if __name__ == "__main__":
    cli()
