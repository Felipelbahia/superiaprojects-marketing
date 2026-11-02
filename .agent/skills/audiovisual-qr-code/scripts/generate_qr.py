#!/usr/bin/env python3
"""
Generate QR codes with URLs and UTM tracking. Exports PNG and/or SVG with optional captions.
Part of the qr-code-generator skill.
"""

import argparse
import io
import os
import re
import sys
import urllib.parse
import xml.etree.ElementTree as ET

try:
    import segno
except ImportError:
    sys.exit("Error: 'segno' is not installed. Run 'python3 -m pip install segno'.")

try:
    from PIL import Image, ImageDraw, ImageFont
    HAS_PIL = True
except ImportError:
    HAS_PIL = False


def validate_url(url: str) -> str:
    """Validate URL format and warn about non-https or suspicious links."""
    parsed = urllib.parse.urlsplit(url)
    if not parsed.scheme or not parsed.netloc:
        raise ValueError(f"Invalid URL: '{url}'. Must include scheme and domain (e.g. https://example.com).")
    if parsed.scheme.lower() not in ("http", "https"):
        raise ValueError(f"Unsupported URL scheme '{parsed.scheme}'. Only http and https are allowed.")
    if parsed.scheme.lower() == "http":
        print("Warning: HTTP is unencrypted. HTTPS is strongly recommended for QR codes.", file=sys.stderr)
    return url


def append_utm(url: str, utm_params: dict) -> str:
    """Append UTM parameters to URL, preserving existing query parameters."""
    if not utm_params:
        return url
    
    parsed = urllib.parse.urlsplit(url)
    existing_query = urllib.parse.parse_qsl(parsed.query, keep_blank_values=True)
    
    # Filter out empty UTM values
    valid_utm = [(k, v) for k, v in utm_params.items() if v]
    
    # Merge existing queries with new UTMs (new UTMs take precedence)
    existing_dict = dict(existing_query)
    for k, v in valid_utm:
        existing_dict[k] = v
    
    new_query = urllib.parse.urlencode(list(existing_dict.items()))
    new_url = urllib.parse.urlunsplit((parsed.scheme, parsed.netloc, parsed.path, new_query, parsed.fragment))
    return new_url


def add_caption_svg(svg_content: str, label: str = None, show_url: bool = False, url: str = None) -> str:
    """Add text captions under an SVG QR code by expanding the SVG viewBox."""
    # Register namespaces to avoid ns0 prefixes
    ET.register_namespace('', 'http://www.w3.org/2000/svg')
    root = ET.fromstring(svg_content)
    
    viewbox = root.attrib.get('viewBox', '')
    if viewbox:
        vx, vy, vw, vh = [float(x) for x in viewbox.split()]
    else:
        width_str = root.attrib.get('width', '100').replace('px', '').replace('mm', '')
        height_str = root.attrib.get('height', '100').replace('px', '').replace('mm', '')
        vw, vh = float(width_str), float(height_str)
        vx, vy = 0.0, 0.0

    lines = []
    if label:
        lines.append((label, True))
    if show_url and url:
        # Truncate overly long URL for visual caption
        display_url = url if len(url) <= 50 else url[:47] + "..."
        lines.append((display_url, False))
        
    if not lines:
        return svg_content

    # Calculate extra height needed
    extra_height = len(lines) * 22 + 10
    total_h = vh + extra_height
    
    root.attrib['viewBox'] = f"{vx} {vy} {vw} {total_h}"
    root.attrib['height'] = f"{int(total_h)}"
    
    # Add caption container
    curr_y = vh + 16
    for text, is_bold in lines:
        text_el = ET.Element('text', {
            'x': f"{vw / 2:.1f}",
            'y': f"{curr_y:.1f}",
            'text-anchor': 'middle',
            'font-family': 'Helvetica, Arial, sans-serif',
            'font-size': '12' if is_bold else '10',
            'font-weight': 'bold' if is_bold else 'normal',
            'fill': '#1a1a1a'
        })
        text_el.text = text
        root.append(text_el)
        curr_y += 18

    return ET.tostring(root, encoding='unicode')


def add_caption_png(qr_png_bytes: bytes, label: str = None, show_url: bool = False, url: str = None) -> bytes:
    """Add text captions under a PNG QR code using PIL."""
    if not HAS_PIL or (not label and not show_url):
        return qr_png_bytes

    base_img = Image.open(io.BytesIO(qr_png_bytes)).convert("RGBA")
    w, h = base_img.size

    lines = []
    if label:
        lines.append((label, True))
    if show_url and url:
        display_url = url if len(url) <= 55 else url[:52] + "..."
        lines.append((display_url, False))

    if not lines:
        return qr_png_bytes

    # Use default font or truetype
    font_large = ImageFont.load_default()
    font_small = ImageFont.load_default()

    extra_h = len(lines) * 26 + 15
    new_h = h + extra_h
    canvas = Image.new("RGBA", (w, new_h), (255, 255, 255, 255))
    canvas.paste(base_img, (0, 0))

    draw = ImageDraw.Draw(canvas)
    curr_y = h + 6

    for text, is_bold in lines:
        font = font_large if is_bold else font_small
        # calculate text bbox for center alignment
        bbox = draw.textbbox((0, 0), text, font=font)
        text_w = bbox[2] - bbox[0]
        pos_x = max(4, (w - text_w) // 2)
        draw.text((pos_x, curr_y), text, fill=(20, 20, 20, 255), font=font)
        curr_y += 22

    out_buf = io.BytesIO()
    canvas.save(out_buf, format="PNG")
    return out_buf.getvalue()


def generate_qr(
    url: str,
    output_base: str = "qr_code",
    label: str = None,
    show_url: bool = False,
    fmt: str = "both",
    error: str = "M",
    scale: int = 10,
    border: int = 4,
    utm: dict = None,
    size_intent: str = "screen"
) -> dict:
    """Core function to generate QR codes and return metadata."""
    final_url = validate_url(url)
    if utm:
        final_url = append_utm(final_url, utm)

    # Adjust parameters by size intent
    if size_intent == "print":
        scale = max(scale, 20)
        error = "H" if error == "M" else error
    elif size_intent == "sticker":
        scale = max(scale, 15)
        error = "H" if error == "M" else error

    qr = segno.make(final_url, error=error)

    generated_files = []
    out_dir = os.path.dirname(output_base)
    if out_dir:
        os.makedirs(out_dir, exist_ok=True)

    # SVG Export
    if fmt in ("svg", "both"):
        svg_path = f"{output_base}.svg" if not output_base.endswith(".svg") else output_base
        svg_buf = io.BytesIO()
        qr.save(svg_buf, kind="svg", scale=scale, border=border)
        raw_svg = svg_buf.getvalue().decode("utf-8")
        if label or show_url:
            raw_svg = add_caption_svg(raw_svg, label=label, show_url=show_url, url=final_url)
        with open(svg_path, "w", encoding="utf-8") as f:
            f.write(raw_svg)
        generated_files.append(os.path.abspath(svg_path))

    # PNG Export
    if fmt in ("png", "both"):
        png_path = f"{output_base}.png" if not output_base.endswith(".png") else output_base
        png_buf = io.BytesIO()
        qr.save(png_buf, kind="png", scale=scale, border=border)
        raw_png = png_buf.getvalue()
        if label or show_url:
            raw_png = add_caption_png(raw_png, label=label, show_url=show_url, url=final_url)
        with open(png_path, "wb") as f:
            f.write(raw_png)
        generated_files.append(os.path.abspath(png_path))

    return {
        "encoded_url": final_url,
        "files": generated_files,
        "error_level": error.upper(),
        "scale": scale,
        "border": border,
        "size_intent": size_intent
    }


def main():
    parser = argparse.ArgumentParser(description="Generate QR codes with UTM tracking and optional captions.")
    parser.add_argument("url", nargs="?", help="Destination URL")
    parser.add_argument("--url", "-u", dest="flag_url", help="Destination URL (flag option)")
    parser.add_argument("--label", "-l", help="Caption text under the QR code (e.g. 'Scan to register')")
    parser.add_argument("--show-url", action="store_true", help="Display the URL below the QR code")
    parser.add_argument("--output", "-o", default="qr_output", help="Output file path without extension")
    parser.add_argument("--format", "-f", choices=["png", "svg", "both"], default="both", help="Export format")
    parser.add_argument("--error", "-e", choices=["L", "M", "Q", "H", "l", "m", "q", "h"], default="M", help="Error correction level")
    parser.add_argument("--scale", "-s", type=int, default=10, help="Scale factor (module size)")
    parser.add_argument("--border", "-b", type=int, default=4, help="Quiet zone border in modules")
    parser.add_argument("--size-intent", choices=["screen", "print", "sticker"], default="screen", help="Intended display context")
    
    # UTM options
    parser.add_argument("--utm-source", help="UTM source parameter")
    parser.add_argument("--utm-medium", help="UTM medium parameter")
    parser.add_argument("--utm-campaign", help="UTM campaign parameter")
    parser.add_argument("--utm-content", help="UTM content parameter")
    parser.add_argument("--utm-term", help="UTM term parameter")

    args = parser.parse_args()
    target_url = args.url or args.flag_url
    if not target_url:
        parser.error("A target URL is required.")

    utm_dict = {
        "utm_source": args.utm_source,
        "utm_medium": args.utm_medium,
        "utm_campaign": args.utm_campaign,
        "utm_content": args.utm_content,
        "utm_term": args.utm_term,
    }

    try:
        result = generate_qr(
            url=target_url,
            output_base=args.output,
            label=args.label,
            show_url=args.show_url,
            fmt=args.format,
            error=args.error.upper(),
            scale=args.scale,
            border=args.border,
            utm=utm_dict,
            size_intent=args.size_intent
        )
    except Exception as exc:
        sys.exit(f"Generation error: {exc}")

    # Output report
    print("\n=== QR Code Generation Complete ===")
    print(f"Encoded URL: {result['encoded_url']}")
    print("\nFiles generated:")
    for f in result["files"]:
        print(f"  - {f}")
    print("\nRecommendations:")
    print(f"  - Error Correction: Level {result['error_level']} applied.")
    if result['size_intent'] == 'print':
        print("  - For Print: Use the SVG file for infinite vector scaling without pixelation.")
        print("  - Recommended physical print size: Minimum 2 x 2 cm (0.8 x 0.8 in) for close scanning, 5 x 5 cm for flyers.")
    else:
        print("  - For Web/Screen: PNG is lightweight and ready for digital sharing.")
        print("  - For Print Collateral: Prefer the SVG export.")
    print("===================================\n")


if __name__ == "__main__":
    main()
