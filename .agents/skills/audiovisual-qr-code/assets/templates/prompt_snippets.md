# Prompt snippets

## Single QR (PNG + SVG)
Use the `audiovisual-qr-code` skill. Generate a QR for:
URL: https://example.com
Caption label: Scan to visit
Show URL under code: no
Formats: png, svg
Error correction: H

## QR with UTM tracking
Use the `audiovisual-qr-code` skill.
URL: https://example.com/pricing
UTM:
- source: linkedin
- medium: qr
- campaign: jan_2026_launch
Caption: Scan for pricing
Formats: svg

## Batch
Use the `audiovisual-qr-code` skill.
Here’s a CSV with id,url,label. Generate SVGs for print with error correction H.
