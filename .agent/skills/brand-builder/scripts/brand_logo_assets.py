#!/usr/bin/env python3
"""Export a brand's master SVG logos to transparent PNGs, a favicon.ico and a manifest.

Usage (Python 3.9+; Pillow for the .ico; Chrome, Chromium or Edge for rendering):
  python3 brand_logo_assets.py export <brand_root> [--chrome <path>]   # logo/svg/*.svg -> logo/png, logo/favicon, logo/manifest.json
  python3 brand_logo_assets.py check  <brand_root>                      # manifest hashes vs files on disk (exit 1 on problems)
  python3 brand_logo_assets.py render <brand_root> <svg> --width <px> [--logo <svg>] [--out <png>] [--chrome <path>]
                                                                        # one SVG (a channel mould, for example) to a PNG; --logo fills the mould's logo-slot

Layout inside the brand root (the master SVGs are the source of truth and are never written to):
  logo/svg/*.svg          masters, named as the brand manual says (see identidade-e-ativos/01-logo.md)
  logo/png/<name>-<W>.png transparent PNGs (lockups: 512, 1024, 2048 px wide; symbols: square icon sizes)
  logo/favicon/favicon.ico  16, 32 and 48 px, from the symbol master
  logo/manifest.json      role, path, format, size and SHA-256 of every file, plus the source hash

Idea adapted from the Brandfy "ativos-logo" skill (Promovaweb, AGPL-3.0); code written from scratch.
"""
import base64
import hashlib
import json
import os
import re
import struct
import sys
import tempfile
import xml.etree.ElementTree as ET
from pathlib import Path

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import brand_chrome  # noqa: E402

LOCKUP_WIDTHS = (512, 1024, 2048)
ICON_SIZES = (16, 32, 48, 180, 192, 512)
ICO_SIZES = (16, 32, 48)
MIN_CANVAS = 600  # headless Chrome clamps very small windows, so render big and crop
SYMBOL_WORDS = ("simbolo", "símbolo", "symbol", "icone", "ícone", "icon", "avatar", "favicon")
REVERSE_WORDS = ("reverso", "reverse", "light", "dark", "branco", "white", "negativo", "claro", "escuro")
MONO_WORDS = ("mono", "monocrom", "preto", "black", "1cor")


def sha256(path):
    h = hashlib.sha256()
    with open(path, "rb") as f:
        for chunk in iter(lambda: f.read(65536), b""):
            h.update(chunk)
    return h.hexdigest()


def has_word(name, words):
    low = name.lower()
    return any(w in low for w in words)


def read_svg(path):
    """Return (width, height, warnings). Raises ValueError for a file that cannot be exported."""
    try:
        root = ET.parse(path).getroot()
    except ET.ParseError as e:
        raise ValueError("SVG inválido (%s)" % e)
    if not root.tag.endswith("svg"):
        raise ValueError("o arquivo não é um SVG")
    warnings = []
    vb = root.get("viewBox")
    if vb:
        nums = [float(x) for x in re.split(r"[\s,]+", vb.strip()) if x]
        if len(nums) != 4 or nums[2] <= 0 or nums[3] <= 0:
            raise ValueError("viewBox inválido: %s" % vb)
        w, h = nums[2], nums[3]
    else:
        def num(v):
            m = re.match(r"^\s*([\d.]+)", v or "")
            return float(m.group(1)) if m else 0
        w, h = num(root.get("width")), num(root.get("height"))
        if not w or not h:
            raise ValueError("sem viewBox e sem width/height: não dá para calcular a proporção")
        warnings.append("sem viewBox (usei width/height); acrescente o viewBox para escalar sem perda")
    for el in root.iter():
        tag = el.tag.split("}")[-1]
        if tag == "image":
            warnings.append("contém <image> embutida (raster dentro do SVG): o PNG não ficará nítido em tamanho grande")
        if tag == "text":
            warnings.append("contém <text>: a fonte precisa estar instalada na máquina; converta o texto em curvas antes de exportar")
    return w, h, sorted(set(warnings))


def render_png(chrome, svg_path, box_w, box_h, fit):
    """Render the SVG once into a box_w x box_h transparent RGBA image. fit='width' keeps the ratio; fit='contain' centers it."""
    from PIL import Image
    with tempfile.TemporaryDirectory(prefix="brand-logo-") as tmp:
        page = Path(tmp) / "page.html"
        style = ("width:%dpx;height:%dpx;display:block" % (box_w, box_h)) + (";object-fit:contain" if fit == "contain" else "")
        page.write_text('<!doctype html><html><body style="margin:0;background:transparent"><img src="%s" style="%s"></body></html>'
                        % (Path(svg_path).resolve().as_uri(), style), encoding="utf-8")
        shot = Path(tmp) / "shot.png"
        cw, ch = max(box_w, MIN_CANVAS), max(box_h, MIN_CANVAS)
        res = brand_chrome.run_headless(chrome, ["--default-background-color=00000000", "--window-size=%d,%d" % (cw, ch),
                                                 "--screenshot=%s" % shot, brand_chrome.file_url(page)])
        if not shot.exists():
            raise RuntimeError("o navegador não gerou a imagem: %s" % res.stderr.decode("utf-8", "replace")[-300:])
        return Image.open(shot).convert("RGBA").crop((0, 0, box_w, box_h)).copy()


def load_manifest(path):
    if not path.exists():
        return {}
    try:
        data = json.loads(path.read_text(encoding="utf-8"))
        return {e["path"]: e for e in data.get("arquivos", [])}
    except (ValueError, KeyError):
        return {}


def export(root, chrome_path=None):
    root = Path(root).resolve()
    svg_dir = root / "logo" / "svg"
    if not svg_dir.is_dir():
        print("Pasta dos mestres não encontrada: %s (coloque os SVG em logo/svg/)" % svg_dir)
        return 1
    masters = sorted(p for p in svg_dir.glob("*.svg") if p.is_file())
    if not masters:
        print("Nenhum SVG em %s" % svg_dir)
        return 1
    try:
        chrome = brand_chrome.find_chrome(chrome_path)
    except brand_chrome.ChromeNotFound as e:
        print(e)
        return 1
    png_dir, fav_dir = root / "logo" / "png", root / "logo" / "favicon"
    manifest_path = root / "logo" / "manifest.json"
    old = load_manifest(manifest_path)
    entries, problems, made, kept = [], 0, 0, 0
    symbols = []
    for svg in masters:
        name = svg.stem
        try:
            w, h, warns = read_svg(svg)
        except ValueError as e:
            print("ERRO %s: %s" % (svg.name, e))
            problems += 1
            continue
        for wmsg in warns:
            print("AVISO %s: %s" % (svg.name, wmsg))
        src_hash = sha256(svg)
        is_symbol = has_word(name, SYMBOL_WORDS)
        if is_symbol:
            symbols.append(svg)
            targets = [("icone", sz, sz, sz) for sz in ICON_SIZES]
            big_box, fit = (max(ICON_SIZES), max(ICON_SIZES)), "contain"
        else:
            targets = [("logo", wd, wd, round(wd * h / w)) for wd in LOCKUP_WIDTHS]
            big_box, fit = (max(LOCKUP_WIDTHS), round(max(LOCKUP_WIDTHS) * h / w)), "width"
        needed = []
        for role, label, bw, bh in targets:
            rel = "png/%s-%d.png" % (name, label)
            out = root / "logo" / rel
            prev = old.get("logo/" + rel)
            if prev and out.exists() and prev.get("origem_sha256") == src_hash and prev.get("sha256") == sha256(out):
                kept += 1
                entries.append(prev)
            else:
                needed.append((role, rel, out, bw, bh))
        if not needed:
            continue
        try:
            big = render_png(chrome, svg, big_box[0], big_box[1], fit)  # one browser run per master; smaller sizes are derived
        except Exception as e:  # noqa: BLE001 - report and keep going with the other masters
            print("ERRO %s: %s" % (svg.name, e))
            problems += 1
            continue
        from PIL import Image
        for role, rel, out, bw, bh in needed:
            img = big if big.size == (bw, bh) else big.resize((bw, bh), Image.LANCZOS)
            os.makedirs(out.parent, exist_ok=True)
            img.save(out, "PNG")
            made += 1
            entries.append({"funcao": role, "path": "logo/" + rel, "formato": "png", "largura": bw, "altura": bh,
                            "sha256": sha256(out), "origem": "logo/svg/" + svg.name, "origem_sha256": src_hash})
    # favicon from the plain symbol (not the reverse/mono variants)
    plain = [s for s in symbols if not has_word(s.stem, REVERSE_WORDS + MONO_WORDS)]
    if symbols:
        chosen = (plain or symbols)[0]
        if len(plain) != 1:
            print("AVISO favicon: %s símbolo(s) \"colorido\" encontrado(s); usei %s" % (len(plain), chosen.name))
        big = png_dir / ("%s-%d.png" % (chosen.stem, 512))
        fav = fav_dir / "favicon.ico"
        prev = old.get("logo/favicon/favicon.ico")
        if prev and fav.exists() and prev.get("origem_sha256") == sha256(chosen) and prev.get("sha256") == sha256(fav):
            kept += 1
            entries.append(prev)
        elif big.exists():
            from PIL import Image
            os.makedirs(fav_dir, exist_ok=True)
            Image.open(big).convert("RGBA").save(fav, format="ICO", sizes=[(sz, sz) for sz in ICO_SIZES])
            entries.append({"funcao": "favicon", "path": "logo/favicon/favicon.ico", "formato": "ico", "largura": max(ICO_SIZES),
                            "altura": max(ICO_SIZES), "sha256": sha256(fav), "origem": "logo/svg/" + chosen.name,
                            "origem_sha256": sha256(chosen)})
            made += 1
    else:
        print("AVISO favicon: nenhum SVG de símbolo (nome com simbolo/symbol/icone/icon); favicon.ico não gerado")
    # missing variants (warn only: the script never invents a variant)
    names = [m.stem for m in masters]
    if not any(has_word(n, REVERSE_WORDS) for n in names):
        print("AVISO variante ausente: versão reversa (para fundo escuro). Nomeie com reverso, light ou dark.")
    if not any(has_word(n, MONO_WORDS) for n in names):
        print("AVISO variante ausente: versão monocromática. Nomeie com mono, preto ou black.")
    if not any(not has_word(n, SYMBOL_WORDS) for n in names):
        print("AVISO variante ausente: logo completo (só há símbolo).")
    if not symbols:
        print("AVISO variante ausente: símbolo isolado.")
    entries.sort(key=lambda e: e["path"])
    manifest = {"formato": 1, "gerado_por": "brand_logo_assets.py", "arquivos": entries}
    manifest_path.write_text(json.dumps(manifest, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    print("Logo: %d arquivo(s) gerado(s), %d mantido(s) (fonte igual), manifesto em %s" % (made, kept, manifest_path))
    return 1 if problems else 0


def put_logo(svg_text, logo_path):
    """Replace the mould's <g id="logo-slot"> placeholder by the brand logo, scaled to fit the slot box."""
    m = re.search(r'<g id="logo-slot" transform="translate\(([\d.]+) ([\d.]+)\)">(.*?)</g>', svg_text, re.S)
    box = re.search(r'<rect class="slot" width="([\d.]+)" height="([\d.]+)"', m.group(3)) if m else None
    if not m or not box:
        raise ValueError('o molde não tem o grupo logo-slot no formato esperado (<g id="logo-slot" transform="translate(x y)"> com um <rect class="slot">)')
    data = Path(logo_path).read_bytes()
    if len(data) > 2 * 1024 * 1024:
        raise ValueError("o SVG do logo tem mais de 2 MB")
    href = "data:image/svg+xml;base64," + base64.b64encode(data).decode("ascii")
    image = '<image x="%s" y="%s" width="%s" height="%s" preserveAspectRatio="xMinYMid meet" href="%s"/>' % (
        m.group(1), m.group(2), box.group(1), box.group(2), href)
    return svg_text[:m.start()] + image + svg_text[m.end():]


def render_one(root, svg, width, out=None, chrome_path=None, logo=None):
    """Export a single SVG of the brand (a channel mould, for example) to a PNG of the given width."""
    root = Path(root).resolve()
    svg = Path(svg).resolve()
    if not svg.is_file():
        print("SVG não encontrado:", svg)
        return 1
    if not 16 <= width <= 8000:
        print("--width precisa ficar entre 16 e 8000 px")
        return 2
    out = Path(out).resolve() if out else svg.with_name("%s-%d.png" % (svg.stem, width))
    if not inside_root(root, out):
        print("A saída precisa ficar dentro da pasta da marca (%s). Use --out ou copie o SVG para a pasta da marca." % root)
        return 2
    try:
        w, h, warns = read_svg(svg)
    except ValueError as e:
        print("ERRO %s: %s" % (svg.name, e))
        return 1
    for wmsg in warns:
        print("AVISO %s: %s" % (svg.name, wmsg))
    try:
        chrome = brand_chrome.find_chrome(chrome_path)
        if logo:
            logo = Path(logo).resolve()
            if not logo.is_file() or logo.suffix.lower() != ".svg" or not inside_root(root, logo):
                print("--logo precisa ser um .svg que exista dentro da pasta da marca")
                return 2
            with tempfile.TemporaryDirectory(prefix="brand-mould-") as tmp:
                filled = Path(tmp) / svg.name
                filled.write_text(put_logo(svg.read_text(encoding="utf-8"), logo), encoding="utf-8")
                img = render_png(chrome, filled, width, round(width * h / w), "width")
        else:
            img = render_png(chrome, svg, width, round(width * h / w), "width")
    except (brand_chrome.ChromeNotFound, RuntimeError, ValueError) as e:
        print(e)
        return 1
    os.makedirs(out.parent, exist_ok=True)
    img.save(out, "PNG")
    print("PNG gerado: %s (%dx%d)" % (out, img.size[0], img.size[1]))
    return 0


def inside_root(root, path):
    try:
        Path(path).resolve().relative_to(root)
        return True
    except ValueError:
        return False


def png_size(path):
    with open(path, "rb") as f:
        head = f.read(24)
    if head[:8] != b"\x89PNG\r\n\x1a\n":
        return None
    return struct.unpack(">II", head[16:24])


def check(root):
    root = Path(root).resolve()
    manifest_path = root / "logo" / "manifest.json"
    if not manifest_path.exists():
        print("manifest.json não encontrado: rode export antes")
        return 1
    data = json.loads(manifest_path.read_text(encoding="utf-8"))
    problems = 0
    for e in data.get("arquivos", []):
        f = root / e["path"]
        if not f.exists():
            print("FALTA:", e["path"])
            problems += 1
            continue
        if sha256(f) != e["sha256"]:
            print("HASH DIFERENTE:", e["path"])
            problems += 1
        if e["formato"] == "png" and png_size(f) != (e["largura"], e["altura"]):
            print("DIMENSÃO DIFERENTE:", e["path"], png_size(f), "esperado", (e["largura"], e["altura"]))
            problems += 1
        src = root / e["origem"]
        if not src.exists() or sha256(src) != e["origem_sha256"]:
            print("MESTRE MUDOU (rode export de novo):", e["origem"])
            problems += 1
    print("OK: nenhum problema" if not problems else "%d problema(s)" % problems)
    return 1 if problems else 0


def main(argv):
    if len(argv) >= 3 and argv[1] == "export":
        chrome = None
        rest = argv[3:]
        if rest[:1] == ["--chrome"] and len(rest) == 2:
            chrome = rest[1]
        elif rest:
            print(__doc__)
            return 2
        return export(argv[2], chrome)
    if len(argv) >= 5 and argv[1] == "render":
        opts, rest = {"--width": None, "--out": None, "--chrome": None, "--logo": None}, argv[4:]
        while rest:
            if rest[0] in opts and len(rest) >= 2:
                opts[rest[0]] = rest[1]
                rest = rest[2:]
            else:
                print(__doc__)
                return 2
        try:
            width = int(opts["--width"])
        except (TypeError, ValueError):
            print("--width é obrigatório e deve ser um número inteiro")
            return 2
        return render_one(argv[2], argv[3], width, opts["--out"], opts["--chrome"], opts["--logo"])
    if len(argv) == 3 and argv[1] == "check":
        return check(argv[2])
    print(__doc__)
    return 2


if __name__ == "__main__":
    sys.exit(main(sys.argv))
