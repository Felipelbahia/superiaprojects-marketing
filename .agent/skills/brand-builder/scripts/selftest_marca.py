#!/usr/bin/env python3
"""Self-test of the brand file scripts, on a throwaway brand built in a temp folder.

Usage (Python 3.9+; Pillow; Chrome, Chromium or Edge for the render steps, skipped with a notice if missing):
  python3 -B selftest_marca.py          # exit 0 = all checks passed, exit 1 = at least one failed

Covers: brand_html.py (build, check, pdf), brand_logo_assets.py (export, check, render --logo),
brand_webfonts.py (local open-licence file, refused licence, bad header) and the docs/code word lists.
Nothing is written outside the temp folder. Network is never used.
"""
import hashlib
import json
import os
import subprocess
import sys
import tempfile
from pathlib import Path

HERE = Path(__file__).resolve().parent
SKILLS = HERE.parent.parent
WEBFONTS = SKILLS / "brand-design-system" / "scripts" / "brand_webfonts.py"
FAILS = []


def run(*args, env_extra=None):
    return subprocess.run([sys.executable, "-B", *map(str, args)], capture_output=True, text=True, timeout=600,
                          env={**os.environ, **(env_extra or {})})


def check(name, ok, detail=""):
    print(("ok    " if ok else "FALHA ") + name + ((" - " + detail) if detail and not ok else ""))
    if not ok:
        FAILS.append(name)


def sha(p):
    return hashlib.sha256(Path(p).read_bytes()).hexdigest()


def build_brand(root):
    (root / "logo" / "svg").mkdir(parents=True)
    (root / "design-system").mkdir()
    (root / "logo/svg/logo.svg").write_text('<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 400 100"><rect width="100" height="100" rx="20" fill="#1b6ef3"/><rect x="130" y="30" width="250" height="40" fill="#161b20"/></svg>')
    (root / "logo/svg/simbolo.svg").write_text('<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 100 100"><rect width="100" height="100" rx="20" fill="#1b6ef3"/></svg>')
    (root / "design-system/tokens.json").write_text(json.dumps({"typography": {"font-sans": "Inter, system-ui, sans-serif"}}))
    (root / "brandbook.md").write_text("# Brandbook\n\nVeja a [essência](01-essencia.md).\n")
    (root / "01-essencia.md").write_text("# Essência\n\n| a | b |\n|---|---|\n| 1 | 2 |\n")
    (root / "versoes.json").write_text(json.dumps({"marca": "Marca Teste", "entrada_html": "_html/brandbook.html", "itens": [
        {"titulo": "Brandbook", "vigente": "brandbook.md", "historico": [], "estado": "vigente"},
        {"titulo": "Essência", "vigente": "01-essencia.md", "historico": [], "estado": "vigente"}]}))


def main():
    sys.path.insert(0, str(HERE))
    import brand_chrome
    try:
        brand_chrome.find_chrome()
        have_chrome = True
    except brand_chrome.ChromeNotFound:
        have_chrome = False
        print("AVISO: sem Chrome/Chromium/Edge; passos de render e PDF ignorados")
    with tempfile.TemporaryDirectory(prefix="selftest-marca-") as tmp:
        root = Path(tmp) / "marca"
        build_brand(root)
        # html twin
        r = run(HERE / "brand_html.py", "sync", root)
        check("brand_html sync limpo", r.returncode == 0, r.stdout[-200:])
        (root / "design-system/fonts").mkdir(exist_ok=True)
        (root / "design-system/fonts/LICENCAS.md").write_text("# gerado\n")
        check("brand_html check ignora a pasta fonts", run(HERE / "brand_html.py", "check", root).returncode == 0)
        (root / "solto.md").write_text("# solto\n")
        check("brand_html check aponta .md solto", run(HERE / "brand_html.py", "check", root).returncode == 1)
        (root / "solto.md").unlink()
        if have_chrome:
            r = run(HERE / "brand_html.py", "pdf", root)
            pdf = root / "pdf" / "marca-teste-manual.pdf"
            check("pdf gerado, A4, mais de 1 página", r.returncode == 0 and pdf.exists() and pdf.read_bytes().startswith(b"%PDF")
                  and b"594.9" in pdf.read_bytes() and "página" in r.stdout and not r.stdout.split("(")[1].startswith("1 "), (r.stdout + r.stderr)[-300:])
            r = run(HERE / "brand_html.py", "pdf", root, env_extra={"BRAND_CHROME_TIMEOUT": "1"})
            check("pdf com limite de tempo estourado dá mensagem clara e não deixa traceback", r.returncode in (0, 1) and "Traceback" not in r.stderr, r.stderr[-300:])
            check("pdf recusa saída fora da pasta", run(HERE / "brand_html.py", "pdf", root, "--out", Path(tmp) / "fora.pdf").returncode == 2)
        # logo
        before = {p.name: sha(p) for p in (root / "logo/svg").glob("*.svg")}
        if have_chrome:
            from PIL import Image
            r = run(HERE / "brand_logo_assets.py", "export", root)
            png = root / "logo/png/logo-512.png"
            ok = r.returncode == 0 and png.exists()
            check("logo export gera os arquivos", ok, r.stdout[-200:])
            if ok:
                im = Image.open(png).convert("RGBA")
                check("PNG com canto transparente e miolo opaco", im.getpixel((0, 0))[3] == 0 and im.getpixel((60, 50))[3] == 255)
                check("PNG do logo tem 512 de largura", im.size[0] == 512)
                check("favicon.ico tem 16, 32 e 48", {(16, 16), (32, 32), (48, 48)} <= set(Image.open(root / "logo/favicon/favicon.ico").info.get("sizes", ())))
            check("manifesto confere", run(HERE / "brand_logo_assets.py", "check", root).returncode == 0)
            check("reexecução mantém os arquivos", "0 arquivo(s) gerado(s)" in run(HERE / "brand_logo_assets.py", "export", root).stdout)
            mould = root / "ativacao" / "moldes"
            mould.mkdir(parents=True)
            src = SKILLS / "brand-builder/assets/moldes-de-canais/youtube-miniatura.svg"
            (mould / src.name).write_text(src.read_text(encoding="utf-8"), encoding="utf-8")
            r = run(HERE / "brand_logo_assets.py", "render", root, mould / src.name, "--width", "640", "--logo", root / "logo/svg/logo.svg")
            check("render com --logo gera PNG 640x360", r.returncode == 0 and Image.open(mould / "youtube-miniatura-640.png").size == (640, 360), r.stdout[-200:])
            check("render recusa logo fora da pasta", run(HERE / "brand_logo_assets.py", "render", root, mould / src.name, "--width", "640", "--logo", "/etc/hosts").returncode == 2)
        check("mestres do logo intactos", before == {p.name: sha(p) for p in (root / "logo/svg").glob("*.svg")})
        # webfonts
        (root / "fontes").mkdir()
        (root / "fontes/Aberta.woff2").write_bytes(b"wOF2" + b"x" * 200)
        (root / "fontes/Falsa.woff2").write_bytes(b"NAOFONTE")
        good = sha(root / "fontes/Aberta.woff2")
        (root / "design-system/fonts.json").write_text(json.dumps({"familias": [
            {"familia": "Inter", "papel": "sans", "arquivos": [{"peso": "400", "estilo": "normal", "arquivo": "fontes/Aberta.woff2", "licenca": "OFL-1.1", "autoria": "x", "fonte_da_licenca": "x", "sha256": good}]},
            {"familia": "Paga", "papel": "display", "arquivos": [{"peso": "400", "estilo": "normal", "url": "https://example.com/p.woff2", "licenca": "Comercial"}]}]}))
        r = run(WEBFONTS, "build", root)
        css = (root / "design-system/fonts/fonts.css").read_text(encoding="utf-8")
        check("webfonts: licença aberta local vira @font-face com swap", r.returncode == 0 and "font-display: swap" in css and "inter-400-normal.woff2" in css, r.stdout[-200:])
        check("webfonts: pilha de reserva vem do tokens.json sem repetir a família", '--font-sans: "Inter", system-ui, sans-serif' in css)
        check("webfonts: licença paga não é baixada", "NÃO baixei" in r.stdout and "Paga" not in css.split(":root")[0])
        check("webfonts check passa", run(WEBFONTS, "check", root).returncode == 0)
        manifest = json.loads((root / "design-system/fonts.json").read_text())
        manifest["familias"][0]["arquivos"][0]["arquivo"] = "fontes/Falsa.woff2"
        manifest["familias"][0]["arquivos"][0].pop("sha256")
        (root / "design-system/fonts.json").write_text(json.dumps(manifest))
        check("webfonts: cabeçalho falso é recusado", run(WEBFONTS, "build", root).returncode == 1)
    # docs x code word lists
    sys.path.insert(0, str(HERE))
    import brand_logo_assets as L
    doc = (SKILLS / "brand-builder/references/identidade-e-ativos/01-logo.md").read_text(encoding="utf-8")
    missing = [w for w in L.SYMBOL_WORDS + L.REVERSE_WORDS + L.MONO_WORDS if "`%s`" % w not in doc]
    check("01-logo.md cita todas as palavras que o código usa", not missing, ", ".join(missing))
    print("\n%s" % ("TUDO OK" if not FAILS else "%d FALHA(S): %s" % (len(FAILS), "; ".join(FAILS))))
    return 1 if FAILS else 0


if __name__ == "__main__":
    sys.exit(main())
