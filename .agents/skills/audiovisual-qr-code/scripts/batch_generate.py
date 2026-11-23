#!/usr/bin/env python3
"""
Batch QR code generator from CSV.
Reads CSV with columns 'id,url,label' (and optional UTM columns).
Part of the qr-code-generator skill.
"""

import argparse
import csv
import os
import sys

# Import generate_qr from the sibling script generate_qr.py
try:
    from generate_qr import generate_qr
except ImportError:
    script_dir = os.path.dirname(os.path.abspath(__file__))
    if script_dir not in sys.path:
        sys.path.insert(0, script_dir)
    from generate_qr import generate_qr


def batch_generate(
    csv_path: str,
    output_dir: str = "batch_qr_output",
    fmt: str = "both",
    error: str = "M",
    scale: int = 10,
    show_url: bool = False,
    size_intent: str = "screen"
):
    if not os.path.isfile(csv_path):
        sys.exit(f"Error: CSV file not found at '{csv_path}'.")

    os.makedirs(output_dir, exist_ok=True)

    success_records = []
    error_records = []

    with open(csv_path, mode="r", encoding="utf-8-sig") as f:
        reader = csv.DictReader(f)
        
        # Verify required headers
        fieldnames = [c.strip().lower() for c in (reader.fieldnames or [])]
        if "id" not in fieldnames or "url" not in fieldnames:
            sys.exit(f"Error: CSV must contain at least 'id' and 'url' columns. Found: {reader.fieldnames}")

        row_num = 1
        for row in reader:
            row_num += 1
            # Normalize keys to lowercase stripped
            norm_row = {k.strip().lower(): (v.strip() if v else "") for k, v in row.items() if k}
            
            item_id = norm_row.get("id")
            url = norm_row.get("url")
            label = norm_row.get("label") or None

            if not item_id or not url:
                error_records.append((row_num, item_id or f"Row {row_num}", "Missing id or url"))
                continue

            # Optional per-row UTM params
            utm = {}
            for param in ["utm_source", "utm_medium", "utm_campaign", "utm_content", "utm_term"]:
                val = norm_row.get(param)
                if val:
                    utm[param] = val

            output_base = os.path.join(output_dir, item_id)

            try:
                result = generate_qr(
                    url=url,
                    output_base=output_base,
                    label=label,
                    show_url=show_url,
                    fmt=fmt,
                    error=error,
                    scale=scale,
                    utm=utm,
                    size_intent=size_intent
                )
                success_records.append((item_id, result["encoded_url"], len(result["files"])))
            except Exception as e:
                error_records.append((row_num, item_id, str(e)))

    print("\n=== Batch QR Generation Summary ===")
    print(f"Total processed: {len(success_records) + len(error_records)}")
    print(f"Successful: {len(success_records)}")
    print(f"Failed: {len(error_records)}")
    print(f"Output directory: {os.path.abspath(output_dir)}")
    
    if success_records:
        print("\nGenerated items:")
        for item_id, final_url, count in success_records:
            print(f"  [{item_id}] -> {final_url} ({count} file(s))")

    if error_records:
        print("\nErrors encountered:")
        for row_n, item_id, err in error_records:
            print(f"  Line {row_n} [{item_id}]: {err}")
    print("====================================\n")


def main():
    parser = argparse.ArgumentParser(description="Batch generate QR codes from a CSV file.")
    parser.add_argument("csv_file", nargs="?", help="Path to CSV file with headers 'id,url,label'")
    parser.add_argument("--csv", "-c", dest="flag_csv", help="Path to CSV file (flag option)")
    parser.add_argument("--output-dir", "-o", default="batch_qr_output", help="Output directory for generated files")
    parser.add_argument("--format", "-f", choices=["png", "svg", "both"], default="both", help="Export format")
    parser.add_argument("--error", "-e", choices=["L", "M", "Q", "H", "l", "m", "q", "h"], default="M", help="Error correction level")
    parser.add_argument("--scale", "-s", type=int, default=10, help="Scale factor")
    parser.add_argument("--show-url", action="store_true", help="Display URL under QR code")
    parser.add_argument("--size-intent", choices=["screen", "print", "sticker"], default="screen", help="Intended display context")

    args = parser.parse_args()
    csv_target = args.csv_file or args.flag_csv
    if not csv_target:
        parser.error("A CSV file path is required.")

    batch_generate(
        csv_path=csv_target,
        output_dir=args.output_dir,
        fmt=args.format,
        error=args.error.upper(),
        scale=args.scale,
        show_url=args.show_url,
        size_intent=args.size_intent
    )


if __name__ == "__main__":
    main()
