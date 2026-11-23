#!/usr/bin/env python3
"""Prepare the web fonts of a brand: fetch open-licence files, write fonts.css and a licence register.

Usage (standard library only, Python 3.9+):
  python3 brand_webfonts.py build <brand_root> [--manifest <file>]   # download/copy fonts, write fonts.css and LICENCAS.md
  python3 brand_webfonts.py check <brand_root> [--manifest <file>]   # files, hashes and css present (exit 1 on problems)

Inputs and outputs (everything stays inside <brand_root>):
  design-system/fonts.json        the manifest the owner approves (format below)
  design-system/tokens.json       optional; its typography.font-sans / font-mono give the fallback stack
  design-system/fonts/*.woff2     the font files
  design-system/fonts/fonts.css   @font-face (font-display: swap) + --font-sans / --font-mono variables
  design-system/fonts/LICENCAS.md family, file, licence, author, where the licence is stated, SHA-256

Manifest:
  {"familias": [{"familia": "Inter", "papel": "sans",            # papel: sans | serif | mono | display
                 "reserva": "system-ui, sans-serif",            # optional; default comes from tokens.json
                 "arquivos": [{"peso": "100 900", "estilo": "normal",
                               "url": "https://.../Inter.woff2" | "arquivo": "path/inside/the/brand/Inter.woff2",
                               "licenca": "OFL-1.1", "autoria": "The Inter Project Authors",
                               "fonte_da_licenca": "https://.../OFL.txt", "sha256": "optional"}]}]}

Rules: only OPEN licences (OFL-1.1, Apache-2.0, UFL-1.0) are downloaded, and only from https. Any other
licence is never downloaded: if the owner already placed the file in the brand folder (arquivo), the css points
to it with a warning; otherwise only the fallback variable is written. A file is data: it is checked by its
magic bytes and size and never executed.

Idea adapted from the Brandfy "tipografia-web" skill (Promovaweb, AGPL-3.0); code written from scratch.
"""
import hashlib
import json
import os
import re
import shutil
import sys
import urllib.request
from pathlib import Path

OPEN_LICENCES = ("OFL-1.1", "Apache-2.0", "UFL-1.0")
MAX_BYTES = 8 * 1024 * 1024
FORMATS = {".woff2": "woff2", ".woff": "woff", ".ttf": "truetype", ".otf": "opentype"}
MAGIC = {".woff2": (b"wOF2",), ".woff": (b"wOFF",), ".ttf": (b"\x00\x01\x00\x00", b"true"), ".otf": (b"OTTO",)}
ROLE_VAR = {"sans": "--font-sans", "serif": "--font-serif", "mono": "--font-mono", "display": "--font-display"}


def sha256_bytes(data):
    return hashlib.sha256(data).hexdigest()


def inside(root, path):
    try:
        Path(path).resolve().relative_to(root)
        return True
    except ValueError:
        return False


def slug(text):
    return re.sub(r"[^a-z0-9]+", "-", text.lower()).strip("-")


def load_manifest(path):
    if not path.exists():
        sys.exit("Manifesto não encontrado: %s (formato no cabeçalho de brand_webfonts.py)" % path)
    try:
        data = json.loads(path.read_text(encoding="utf-8"))
    except ValueError as e:
        sys.exit("Manifesto inválido (%s)" % e)
    if not isinstance(data.get("familias"), list) or not data["familias"]:
        sys.exit('O manifesto precisa de "familias" com pelo menos uma família.')
    return data


def default_fallback(root, role):
    tokens = root / "design-system" / "tokens.json"
    if tokens.exists():
        try:
            typ = json.loads(tokens.read_text(encoding="utf-8")).get("typography", {})
            key = "font-mono" if role == "mono" else "font-sans"
            return typ.get(key, "")
        except ValueError:
            pass
    return "ui-monospace, Menlo, Consolas, monospace" if role == "mono" else "system-ui, -apple-system, 'Segoe UI', Roboto, sans-serif"


def strip_family(stack, family):
    """Drop the brand family from the head of a stack so it is not repeated as its own fallback."""
    parts = [p.strip() for p in stack.split(",") if p.strip()]
    parts = [p for p in parts if p.strip("'\"").lower() != family.lower()]
    return ", ".join(parts)


def fetch(url):
    if not url.startswith("https://"):
        raise ValueError("só https é aceito (recebi %s)" % url.split(":")[0])
    req = urllib.request.Request(url, headers={"User-Agent": "brand-webfonts/1"})
    with urllib.request.urlopen(req, timeout=60) as resp:  # noqa: S310 - https only, checked above
        data = resp.read(MAX_BYTES + 1)
    if len(data) > MAX_BYTES:
        raise ValueError("arquivo maior que %d MB" % (MAX_BYTES // 1024 // 1024))
    return data


def build(root, manifest_path):
    root = Path(root).resolve()
    manifest_path = Path(manifest_path) if manifest_path else root / "design-system" / "fonts.json"
    data = load_manifest(manifest_path)
    out_dir = root / "design-system" / "fonts"
    out_dir.mkdir(parents=True, exist_ok=True)
    faces, variables, licences, warnings, problems = [], {}, [], [], 0
    for fam in data["familias"]:
        name = fam.get("familia")
        role = fam.get("papel", "sans")
        if not name:
            print("ERRO: família sem nome")
            problems += 1
            continue
        usable = 0
        for spec in fam.get("arquivos", []):
            label = "%s %s %s" % (name, spec.get("peso", "400"), spec.get("estilo", "normal"))
            lic = spec.get("licenca", "")
            is_open = lic in OPEN_LICENCES
            ext = Path(spec.get("url", spec.get("arquivo", "")).split("?")[0]).suffix.lower()
            if ext not in FORMATS:
                print("ERRO %s: extensão não aceita (%s). Use woff2, woff, ttf ou otf." % (label, ext or "nenhuma"))
                problems += 1
                continue
            dest = out_dir / ("%s-%s-%s%s" % (slug(name), slug(str(spec.get("peso", "400"))), spec.get("estilo", "normal"), ext))
            expected = spec.get("sha256", "").lower()
            content = None
            if spec.get("arquivo"):
                src = (root / spec["arquivo"]).resolve()
                if not inside(root, src) or not src.is_file():
                    print("ERRO %s: arquivo local fora da pasta da marca ou inexistente (%s)" % (label, spec["arquivo"]))
                    problems += 1
                    continue
                content = src.read_bytes()
                if not is_open:
                    warnings.append("%s: licença %r não é aberta; usei o arquivo que você já tem e não baixei nada. Confira o escopo da licença (web, app, impressão)." % (label, lic or "não informada"))
            elif spec.get("url"):
                if not is_open:
                    warnings.append("%s: licença %r não é aberta; NÃO baixei. Coloque o arquivo licenciado na pasta da marca e use \"arquivo\"." % (label, lic or "não informada"))
                    continue
                if dest.exists() and (not expected or sha256_bytes(dest.read_bytes()) == expected):
                    content = dest.read_bytes()
                else:
                    try:
                        content = fetch(spec["url"])
                    except Exception as e:  # noqa: BLE001 - network, TLS, http errors: report and go on
                        print("ERRO %s: download falhou (%s)" % (label, e))
                        problems += 1
                        continue
            else:
                print("ERRO %s: informe \"url\" ou \"arquivo\"" % label)
                problems += 1
                continue
            if not any(content.startswith(m) for m in MAGIC[ext]):
                print("ERRO %s: o conteúdo não é uma fonte %s (cabeçalho inesperado)" % (label, ext))
                problems += 1
                continue
            digest = sha256_bytes(content)
            if expected and digest != expected:
                print("ERRO %s: SHA-256 diferente do manifesto (recebi %s)" % (label, digest))
                problems += 1
                continue
            if not expected:
                warnings.append("%s: sem sha256 no manifesto; registrei %s. Copie para o manifesto para travar a versão." % (label, digest[:16]))
            if not (dest.exists() and dest.read_bytes() == content):
                dest.write_bytes(content)
            usable += 1
            faces.append('@font-face {\n  font-family: "%s";\n  src: url("%s") format("%s");\n  font-weight: %s;\n  font-style: %s;\n  font-display: swap;\n}'
                         % (name, dest.name, FORMATS[ext], spec.get("peso", "400"), spec.get("estilo", "normal")))
            licences.append((name, dest.name, lic or "não informada", spec.get("autoria", "não informada"),
                             spec.get("fonte_da_licenca", "não informada"), digest))
            if is_open and not spec.get("fonte_da_licenca"):
                warnings.append("%s: licença aberta sem \"fonte_da_licenca\"; anote onde a licença está escrita." % label)
        fallback = strip_family(fam.get("reserva") or default_fallback(root, role), name)
        stack = ('"%s", %s' % (name, fallback)) if usable else fallback
        if not usable:
            warnings.append("%s: nenhum arquivo utilizável; a variável usa só a pilha de reserva." % name)
        variables.setdefault(ROLE_VAR.get(role, "--font-sans"), stack)
    css = "/* Gerado por brand_webfonts.py a partir de design-system/fonts.json. Não edite à mão. */\n"
    css += "\n\n".join(faces) + ("\n\n" if faces else "")
    css += ":root {\n" + "".join("  %s: %s;\n" % (k, v) for k, v in variables.items()) + "}\n"
    (out_dir / "fonts.css").write_text(css, encoding="utf-8")
    lic_md = "# Licenças das fontes\n\n| Família | Arquivo | Licença | Autoria | Onde a licença está escrita | SHA-256 |\n|---|---|---|---|---|---|\n"
    lic_md += "".join("| %s | %s | %s | %s | %s | `%s` |\n" % row for row in licences)
    (out_dir / "LICENCAS.md").write_text(lic_md, encoding="utf-8")
    for w in warnings:
        print("AVISO", w)
    print("Webfonts: %d arquivo(s) de fonte, css em %s" % (len(licences), out_dir / "fonts.css"))
    return 1 if problems else 0


def check(root, manifest_path):
    root = Path(root).resolve()
    out_dir = root / "design-system" / "fonts"
    problems = 0
    if not (out_dir / "fonts.css").exists():
        print("FALTA fonts.css: rode build")
        return 1
    css = (out_dir / "fonts.css").read_text(encoding="utf-8")
    for ref in re.findall(r'url\("([^"]+)"\)', css):
        if not (out_dir / ref).exists():
            print("FALTA o arquivo citado no css:", ref)
            problems += 1
    if "font-display: swap" not in css and "@font-face" in css:
        print("font-display: swap ausente")
        problems += 1
    lic = out_dir / "LICENCAS.md"
    if not lic.exists():
        print("FALTA LICENCAS.md")
        problems += 1
    else:
        text = lic.read_text(encoding="utf-8")
        for fname, digest in re.findall(r"\| ([^|\s]+\.(?:woff2|woff|ttf|otf)) \|.*?`([0-9a-f]{64})`", text):
            f = out_dir / fname
            if not f.exists() or sha256_bytes(f.read_bytes()) != digest:
                print("HASH DIFERENTE ou arquivo ausente:", fname)
                problems += 1
    print("OK: nenhum problema" if not problems else "%d problema(s)" % problems)
    return 1 if problems else 0


def main(argv):
    if len(argv) >= 3 and argv[1] in ("build", "check"):
        manifest = None
        rest = argv[3:]
        if rest[:1] == ["--manifest"] and len(rest) == 2:
            manifest = rest[1]
        elif rest:
            print(__doc__)
            return 2
        return build(argv[2], manifest) if argv[1] == "build" else check(argv[2], manifest)
    print(__doc__)
    return 2


if __name__ == "__main__":
    sys.exit(main(sys.argv))
