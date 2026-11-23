"""BRAND-SPECIFIC: valores do design system do WaiMonitor. Para outra marca, copie e edite TOKENS.
Rodar este arquivo sozinho confere contraste (texto 4,5:1, componentes 3:1) e retorna erro se algum par reprovar."""
import json, sys

TOKENS = {
    "name": "WaiMonitor",
    "description": "Radar de oportunidades em grupos de WhatsApp para quem vende por indicação. Sensação: ágil, confiável, atento.",
    "colors": {
        "light": {
            "bg": "#F6F7F8", "surface": "#FFFFFF", "surface-alt": "#EEF1F4",
            "border": "#E2E8F0", "border-strong": "#7A8797",
            "text": "#0F1720", "text-muted": "#4A5565",
            "primary": "#137FEC", "primary-strong": "#0E64C4", "primary-hover": "#0B57B0",
            "on-primary": "#FFFFFF", "link": "#0E64C4", "focus": "#0E64C4",
            "alert": "#C2610C", "alert-text": "#92400E", "alert-bg": "#FFF3DC",
            "success": "#15803D", "success-text": "#166534", "success-bg": "#E6F4EA",
            "danger": "#B91C1C", "danger-strong": "#B91C1C", "danger-text": "#991B1B", "danger-bg": "#FDECEC",
            "info-text": "#0B57B0", "info-bg": "#E6F0FD",
            "nav-bg": "#0B121A", "nav-text": "#C9D3DF", "nav-active": "#FFFFFF", "nav-border": "#1E2A38",
        },
        "dark": {
            "bg": "#101922", "surface": "#1C2630", "surface-alt": "#243040",
            "border": "#232F48", "border-strong": "#6B7B8F",
            "text": "#E8EDF3", "text-muted": "#A3AFBF",
            "primary": "#137FEC", "primary-strong": "#0E64C4", "primary-hover": "#1D6BF5",
            "on-primary": "#FFFFFF", "link": "#6BB3F7", "focus": "#7DBBFA",
            "alert": "#F59E0B", "alert-text": "#FBBF24", "alert-bg": "#33260A",
            "success": "#4ADE80", "success-text": "#4ADE80", "success-bg": "#10281B",
            "danger": "#F87171", "danger-strong": "#B91C1C", "danger-text": "#FCA5A5", "danger-bg": "#351618",
            "info-text": "#6BB3F7", "info-bg": "#12263D",
            "nav-bg": "#0B121A", "nav-text": "#C9D3DF", "nav-active": "#FFFFFF", "nav-border": "#1E2A38",
        },
    },
    "typography": {
        "font-sans": "Inter, system-ui, -apple-system, 'Segoe UI', Roboto, sans-serif",
        "font-mono": "ui-monospace, SFMono-Regular, Menlo, Consolas, monospace",
        "scale": {
            "display": {"size": "3rem", "line": "1.1", "weight": "800"},
            "h1": {"size": "2.25rem", "line": "1.15", "weight": "700"},
            "h2": {"size": "1.75rem", "line": "1.2", "weight": "700"},
            "h3": {"size": "1.375rem", "line": "1.3", "weight": "600"},
            "h4": {"size": "1.125rem", "line": "1.4", "weight": "600"},
            "body": {"size": "1rem", "line": "1.55", "weight": "400"},
            "small": {"size": "0.875rem", "line": "1.5", "weight": "400"},
            "caption": {"size": "0.75rem", "line": "1.4", "weight": "500"},
            "code": {"size": "0.875rem", "line": "1.6", "weight": "400"},
        },
    },
    "rounded": {"sm": "4px", "md": "8px", "lg": "12px", "xl": "16px", "full": "9999px"},
    "spacing": {"1": "4px", "2": "8px", "3": "12px", "4": "16px", "5": "24px", "6": "32px", "7": "48px", "8": "64px", "9": "96px"},
    "elevation": {
        "light": {"1": "0 1px 2px rgba(16,25,34,0.08)", "2": "0 4px 12px rgba(16,25,34,0.10)", "3": "0 12px 32px rgba(16,25,34,0.14)"},
        "dark": {"1": "0 0 0 1px #232F48", "2": "0 0 0 1px #2B3A50", "3": "0 0 0 1px #3A4D68"},
    },
    "motion": {
        "duration": {"fast": "100ms", "base": "160ms", "slow": "240ms"},
        "easing": {"standard": "cubic-bezier(0.2, 0, 0, 1)", "enter": "cubic-bezier(0, 0, 0, 1)", "exit": "cubic-bezier(0.4, 0, 1, 1)"},
    },
    "components": {
        "button-primary": {"bg": "primary-strong", "bg-hover": "primary-hover", "color": "on-primary", "radius": "md", "padding": "2 4"},
        "button-secondary": {"bg": "surface", "border": "border-strong", "color": "text", "radius": "md", "padding": "2 4"},
        "button-ghost": {"bg": "transparent", "color": "link", "radius": "md", "padding": "2 3"},
        "button-danger": {"bg": "danger-strong", "color": "on-primary", "radius": "md", "padding": "2 4"},
        "tag": {"radius": "full", "padding": "1 3", "font": "caption"},
        "input": {"bg": "surface", "border": "border-strong", "color": "text", "radius": "md", "padding": "2 3"},
        "card": {"bg": "surface", "border": "border", "radius": "lg", "padding": "4", "elevation": "1"},
        "alert-card": {"bg": "alert-bg", "color": "alert-text", "marker": "alert", "radius": "lg", "padding": "4"},
        "table": {"bg": "surface", "border": "border", "radius": "lg"},
        "nav": {"bg": "nav-bg", "color": "nav-text", "active": "nav-active", "border": "nav-border"},
    },
}

TEXT_PAIRS = [  # (fg, bg, min)
    ("text", "bg", 4.5), ("text", "surface", 4.5), ("text", "surface-alt", 4.5),
    ("text-muted", "bg", 4.5), ("text-muted", "surface", 4.5), ("text-muted", "surface-alt", 4.5),
    ("on-primary", "primary-strong", 4.5), ("on-primary", "primary-hover", 4.5), ("on-primary", "danger-strong", 4.5),
    ("link", "bg", 4.5), ("link", "surface", 4.5),
    ("alert-text", "alert-bg", 4.5), ("success-text", "success-bg", 4.5),
    ("danger-text", "danger-bg", 4.5), ("info-text", "info-bg", 4.5),
    ("alert-text", "surface", 4.5), ("nav-text", "nav-bg", 4.5), ("nav-active", "nav-bg", 4.5),
]
UI_PAIRS = [  # componentes e graficos, min 3
    ("primary", "bg", 3.0), ("primary", "surface", 3.0), ("border-strong", "bg", 3.0), ("border-strong", "surface", 3.0),
    ("focus", "bg", 3.0), ("focus", "surface", 3.0), ("alert", "bg", 3.0), ("alert", "surface", 3.0),
    ("success", "surface", 3.0), ("danger", "surface", 3.0),
]


def lum(h):
    h = h.lstrip("#")
    r, g, b = [int(h[i:i + 2], 16) / 255 for i in (0, 2, 4)]
    f = lambda c: c / 12.92 if c <= 0.03928 else ((c + 0.055) / 1.055) ** 2.4
    return 0.2126 * f(r) + 0.7152 * f(g) + 0.0722 * f(b)


def ratio(a, b):
    la, lb = sorted((lum(a), lum(b)), reverse=True)
    return round((la + 0.05) / (lb + 0.05), 2)


def contrast_table():
    rows = []
    for mode in ("light", "dark"):
        c = TOKENS["colors"][mode]
        for kind, pairs in (("texto", TEXT_PAIRS), ("componente", UI_PAIRS)):
            for fg, bg, mn in pairs:
                r = ratio(c[fg], c[bg])
                rows.append({"mode": mode, "kind": kind, "fg": fg, "bg": bg, "fg_hex": c[fg], "bg_hex": c[bg],
                             "ratio": r, "min": mn, "ok": r >= mn})
    return rows


if __name__ == "__main__":
    rows = contrast_table()
    bad = [r for r in rows if not r["ok"]]
    for r in bad:
        print("FALHA", r["mode"], r["fg"], r["bg"], r["ratio"], "<", r["min"])
    print(len(rows), "pares,", len(bad), "falhas")
    sys.exit(1 if bad else 0)
