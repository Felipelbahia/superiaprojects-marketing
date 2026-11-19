#!/usr/bin/env python3
"""Build HTML twins of a brand's Markdown files, check them, and collect gaps.

Usage (standard library only, Python 3.9+):
  python3 brand_html.py build  <brand_root>   # write <brand_root>/_html/**.html from the registry
  python3 brand_html.py check  <brand_root>   # stale HTML, missing files, unclassified .md (exit 1 on problems)
  python3 brand_html.py gaps   <brand_root>   # print every "Lacunas"/"Known Gaps" section of the registered files
  python3 brand_html.py sync   <brand_root>   # build + check in one step (run after editing any .md; exit 1 on problems)
  python3 brand_html.py pdf    <brand_root> [--chrome <path>] [--out <file>]
                                              # print the current Markdown to one A4 PDF (needs Chrome, Chromium or Edge)

The registry is <brand_root>/versoes.json (see brandbook-e-ativos.md). Markdown stays the
source of truth; the HTML is generated and must never be edited by hand.
"""
import html
import json
import os
import re
import sys
from urllib.parse import quote

HTML_DIR = "_html"
SKIP_DIRS = {"_respostas", HTML_DIR, "logo", "modelos", "audiovisual-looks", "pdf", "png", "favicon", "imagens", "fonts"}


# ---------------------------------------------------------------- inline
def inline(text, resolve):
    """Convert inline Markdown to HTML. `resolve(href)` maps a link target."""
    parts = re.split(r"(`[^`]*`)", text)
    out = []
    for part in parts:
        if part.startswith("`") and part.endswith("`") and len(part) >= 2:
            out.append("<code>%s</code>" % html.escape(part[1:-1]))
            continue
        s = html.escape(part, quote=False)
        s = re.sub(r"\[([^\]]+)\]\(([^)\s]+(?:\s[^)]*)?)\)",
                   lambda m: '<a href="%s">%s</a>' % (html.escape(resolve(m.group(2).strip()), quote=True), m.group(1)), s)
        s = re.sub(r"\*\*(.+?)\*\*", r"<strong>\1</strong>", s)
        s = re.sub(r"(?<![\w*])\*(?!\s)(.+?)(?<!\s)\*(?![\w*])", r"<em>\1</em>", s)
        s = re.sub(r"~~(.+?)~~", r"<del>\1</del>", s)
        out.append(s)
    return "".join(out)


def split_row(line):
    line = line.strip()
    if line.startswith("|"):
        line = line[1:]
    if line.endswith("|") and not line.endswith("\\|"):
        line = line[:-1]
    cells, cur, tick = [], "", False
    i = 0
    while i < len(line):
        c = line[i]
        if c == "`":
            tick = not tick
        if c == "\\" and i + 1 < len(line) and line[i + 1] == "|":
            cur += "|"
            i += 2
            continue
        if c == "|" and not tick:
            cells.append(cur.strip())
            cur = ""
        else:
            cur += c
        i += 1
    cells.append(cur.strip())
    return cells


LIST_RE = re.compile(r"^(\s*)([-*]|\d+[.)])\s+(.*)$")


def render_list(lines, i, resolve):
    """Render a (possibly nested) list starting at lines[i]. Returns (html, next_i)."""
    base = len(LIST_RE.match(lines[i]).group(1))
    ordered = bool(re.match(r"\d", LIST_RE.match(lines[i]).group(2)))
    tag = "ol" if ordered else "ul"
    items = []
    while i < len(lines):
        m = LIST_RE.match(lines[i])
        if m and len(m.group(1)) == base:
            body = [m.group(3)]
            i += 1
            sub = ""
            while i < len(lines):
                n = LIST_RE.match(lines[i])
                if n and len(n.group(1)) > base:
                    sub, i = render_list(lines, i, resolve)
                elif lines[i].strip() and not n and lines[i].startswith(" " * (base + 2)):
                    body.append(lines[i].strip())
                    i += 1
                else:
                    break
            text = " ".join(body)
            box = ""
            tm = re.match(r"\[( |x|X)\]\s+(.*)", text)
            if tm:
                box = "☑ " if tm.group(1).lower() == "x" else "☐ "
                text = tm.group(2)
            items.append("<li>%s%s%s</li>" % (box, inline(text, resolve), sub))
        else:
            break
    return "<%s>%s</%s>" % (tag, "".join(items), tag), i


def convert(md, resolve):
    lines = md.splitlines()
    if lines and lines[0].strip() == "---":
        for k in range(1, len(lines)):
            if lines[k].strip() == "---":
                lines = lines[k + 1:]
                break
    out, i, title = [], 0, ""
    while i < len(lines):
        line = lines[i]
        if not line.strip():
            i += 1
            continue
        if line.startswith("```"):
            code = []
            i += 1
            while i < len(lines) and not lines[i].startswith("```"):
                code.append(lines[i])
                i += 1
            i += 1
            out.append("<pre><code>%s</code></pre>" % html.escape("\n".join(code)))
            continue
        hm = re.match(r"^(#{1,6})\s+(.*)$", line)
        if hm:
            level = len(hm.group(1))
            text = hm.group(2).strip()
            if not title and level == 1:
                title = re.sub(r"[`*]", "", text)
            slug = re.sub(r"[^\w]+", "-", re.sub(r"[`*]", "", text).lower()).strip("-")
            out.append('<h%d id="%s">%s</h%d>' % (level, slug, inline(text, resolve), level))
            i += 1
            continue
        if re.match(r"^\s*([-*_])\s*\1\s*\1[\s\1]*$", line) and not LIST_RE.match(line):
            out.append("<hr>")
            i += 1
            continue
        if line.lstrip().startswith("|") and i + 1 < len(lines) and re.match(r"^\s*\|?[\s:|-]+\|[\s:|-]*$", lines[i + 1]) and "-" in lines[i + 1]:
            head = split_row(line)
            i += 2
            rows = []
            while i < len(lines) and lines[i].lstrip().startswith("|"):
                rows.append(split_row(lines[i]))
                i += 1
            t = "<div class='tw'><table><thead><tr>%s</tr></thead><tbody>" % "".join("<th>%s</th>" % inline(c, resolve) for c in head)
            for r in rows:
                r = (r + [""] * len(head))[:len(head)]
                t += "<tr>%s</tr>" % "".join("<td>%s</td>" % inline(c, resolve) for c in r)
            out.append(t + "</tbody></table></div>")
            continue
        if line.startswith(">"):
            q = []
            while i < len(lines) and lines[i].startswith(">"):
                q.append(lines[i].lstrip(">").strip())
                i += 1
            out.append("<blockquote><p>%s</p></blockquote>" % inline(" ".join(q), resolve))
            continue
        if LIST_RE.match(line):
            block, i = render_list(lines, i, resolve)
            out.append(block)
            continue
        para = [line.strip()]
        i += 1
        while i < len(lines) and lines[i].strip() and not re.match(r"^(#{1,6}\s|```|>|\s*\|)", lines[i]) and not LIST_RE.match(lines[i]):
            para.append(lines[i].strip())
            i += 1
        out.append("<p>%s</p>" % inline(" ".join(para), resolve))
    return "\n".join(out), title


# ---------------------------------------------------------------- registry
def load_registry(root):
    path = os.path.join(root, "versoes.json")
    if not os.path.exists(path):
        sys.exit("versoes.json não encontrado em %s (ver brandbook-e-ativos.md)" % root)
    with open(path, encoding="utf-8") as f:
        return json.load(f)


def entries(reg):
    """Yield (md_path, status, item) with status 'vigente' or 'historico'."""
    for item in reg.get("itens", []):
        if item.get("vigente"):
            yield item["vigente"], "vigente", item
        for h in item.get("historico", []):
            yield h, "historico", item


def html_for(md_rel, reg):
    """Relative path (from the brand root) of the HTML that stands for md_rel."""
    autoral = reg.get("html_autoral", {})
    if md_rel in autoral:
        return autoral[md_rel]
    if md_rel.startswith("../"):  # file outside the brand folder, kept under _html/_fora/
        return "%s/_fora/%s.html" % (HTML_DIR, md_rel.replace("../", "")[:-3])
    return "%s/%s.html" % (HTML_DIR, md_rel[:-3])


CSS = """*{box-sizing:border-box}body{margin:0;background:%(fundo)s;color:%(texto)s;font:16px/1.6 '%(fonte_texto)s',Arial,sans-serif}
main{max-width:980px;margin:0 auto;padding:28px 20px 80px}h1,h2,h3,h4{font-family:'%(fonte_titulo)s',Georgia,serif;line-height:1.2;margin:1.6em 0 .5em}
h1{font-size:2rem;margin-top:.4em}h2{font-size:1.4rem}h3{font-size:1.15rem}p,li{margin:.4em 0}a{color:%(texto)s;text-decoration-color:%(destaque)s;text-decoration-thickness:2px}
code{font:.85em '%(fonte_mono)s','Courier New',monospace;background:%(borda)s;padding:1px 5px;border-radius:3px}pre{background:%(superficie)s;border:1px solid %(borda)s;padding:12px;overflow:auto;border-radius:4px}pre code{background:none;padding:0}
.tw{overflow-x:auto;margin:.8em 0}table{border-collapse:collapse;width:100%%;background:%(superficie)s;font-size:.9rem}th,td{border:1px solid %(borda)s;padding:6px 9px;text-align:left;vertical-align:top}th{background:%(borda)s}
blockquote{margin:.8em 0;padding:4px 14px;border-left:4px solid %(destaque)s;background:%(superficie)s}hr{border:0;border-top:1px solid %(borda)s;margin:2em 0}
.bar{display:flex;gap:12px;flex-wrap:wrap;align-items:center;font:.8rem '%(fonte_mono)s','Courier New',monospace;color:%(apoio)s;margin-bottom:14px}.bar a{color:%(apoio)s}
.tag{border:1px solid %(apoio)s;border-radius:4px;padding:2px 8px;text-transform:uppercase;letter-spacing:.06em}.ok{background:%(destaque)s;color:%(texto)s;border-color:%(destaque)s}
.hist{border-left:4px solid %(apoio)s;background:%(superficie)s;padding:10px 14px;margin:0 0 18px}.gen{font:.75rem '%(fonte_mono)s','Courier New',monospace;color:%(apoio)s;margin-top:40px}"""

THEME_DEFAULT = {"fundo": "#ECE6DF", "texto": "#161B20", "destaque": "#D4A62A", "superficie": "#F7F3EE", "borda": "#CFC5B8",
                 "apoio": "#525C64", "fonte_titulo": "Georgia", "fonte_texto": "Arial", "fonte_mono": "Courier New"}


def page(title, body, reg, status, item, up, brand_name, vigente_href, md_rel):
    theme = dict(THEME_DEFAULT, **reg.get("tema", {}))
    fonts = reg.get("fontes_google", "")
    link = '<link rel="stylesheet" href="%s">' % html.escape(fonts) if fonts else ""
    tag = '<span class="tag ok">vigente</span>' if status == "vigente" else '<span class="tag">histórico</span>'
    banner = ""
    if status == "historico" and not item.get("vigente"):
        banner = '<div class="hist"><strong>Arquivo obsoleto.</strong> %s</div>' % html.escape(item.get("estado", "Não vale; fica só como histórico."))
    elif status == "historico" and vigente_href:
        banner = '<div class="hist"><strong>Versão antiga.</strong> Vale <a href="%s">%s</a>. Este arquivo fica só como histórico.</div>' % (
            html.escape(vigente_href), html.escape(item.get("vigente", "")))
    return """<!doctype html><html lang="pt-BR"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1">
<title>%s</title>%s<style>%s</style></head><body><main>
<div class="bar"><a href="%s">← Brandbook</a>%s<span>%s</span></div>
%s
%s
<p class="gen">Gerado de <code>%s</code> por brand_html.py. Não edite este HTML: edite o .md e gere de novo.</p>
</main></body></html>""" % (html.escape(title), link, CSS % theme, up, tag, html.escape(brand_name), banner, body, html.escape(md_rel))


def build(root):
    reg = load_registry(root)
    root = os.path.abspath(root)
    known = {md: st for md, st, _ in entries(reg)}
    count = 0
    for md_rel, status, item in entries(reg):
        src = os.path.join(root, md_rel)
        if md_rel in reg.get("html_autoral", {}):
            continue
        if not os.path.exists(src):
            print("FALTA:", md_rel)
            continue
        out_rel = html_for(md_rel, reg)
        out_path = os.path.join(root, out_rel)
        os.makedirs(os.path.dirname(out_path), exist_ok=True)
        here = os.path.dirname(out_path)

        def resolve(href, md_rel=md_rel, here=here):
            if re.match(r"^(https?:|mailto:|#)", href):
                return href
            href = href.split(" ")[0]
            target, _, frag = href.partition("#")
            abs_t = os.path.normpath(os.path.join(root, os.path.dirname(md_rel), target))
            rel_t = os.path.relpath(abs_t, root)
            if target.endswith(".md") and rel_t in known or rel_t in reg.get("html_autoral", {}):
                dest = os.path.join(root, html_for(rel_t, reg))
                return quote(os.path.relpath(dest, here)) + ("#" + frag if frag else "")
            if os.path.exists(abs_t):
                if abs_t.startswith(root + os.sep):
                    return quote(os.path.relpath(abs_t, here)) + ("#" + frag if frag else "")
                return "file://" + quote(abs_t)
            return quote(target) + ("#" + frag if frag else "")

        with open(src, encoding="utf-8") as f:
            body, title = convert(f.read(), resolve)
        vig_href = ""
        if status == "historico" and item.get("vigente"):
            vig_href = quote(os.path.relpath(os.path.join(root, html_for(item["vigente"], reg)), here))
        up = quote(os.path.relpath(os.path.join(root, reg.get("entrada_html", "brandbook.html")), here))
        with open(out_path, "w", encoding="utf-8") as f:
            f.write(page(title or md_rel, body, reg, status, item, up, reg.get("marca", ""), vig_href, md_rel))
        count += 1
    # registry page: which version is current
    rows = ""
    for item in reg.get("itens", []):
        v = item.get("vigente", "")
        vh = quote(os.path.relpath(os.path.join(root, html_for(v, reg)), os.path.join(root, HTML_DIR))) if v else ""
        hs = ", ".join(item.get("historico", [])) or "nenhum"
        rows += "<tr><td>%s</td><td><a href=\"%s\">%s</a></td><td>%s</td><td>%s</td></tr>" % (
            html.escape(item.get("titulo", "")), vh, html.escape(v), html.escape(item.get("estado", "")), html.escape(hs))
    body = "<h1>Qual versão vale</h1><p>Uma linha por assunto. Vale a coluna \"Vigente\"; o histórico fica só para consulta. Origem: <code>versoes.json</code>.</p><div class='tw'><table><thead><tr><th>Assunto</th><th>Vigente</th><th>Estado</th><th>Histórico</th></tr></thead><tbody>%s</tbody></table></div>" % rows
    up = quote(os.path.relpath(os.path.join(root, reg.get("entrada_html", "brandbook.html")), os.path.join(root, HTML_DIR)))
    with open(os.path.join(root, HTML_DIR, "versoes.html"), "w", encoding="utf-8") as f:
        f.write(page("Qual versão vale", body, reg, "vigente", {}, up, reg.get("marca", ""), "", "versoes.json"))
    print("HTML gerados: %d (+ versoes.html) em %s" % (count, os.path.join(root, HTML_DIR)))


def check(root):
    reg = load_registry(root)
    root = os.path.abspath(root)
    problems = 0
    registered = set()
    for md_rel, status, item in entries(reg):
        registered.add(md_rel)
        src = os.path.join(root, md_rel)
        if not os.path.exists(src):
            print("FALTA O MD:", md_rel)
            problems += 1
            continue
        out = os.path.join(root, html_for(md_rel, reg))
        if not os.path.exists(out):
            print("SEM HTML:", md_rel)
            problems += 1
        elif os.path.getmtime(out) < os.path.getmtime(src) and md_rel not in reg.get("html_autoral", {}):
            print("HTML DESATUALIZADO (md mais novo):", md_rel)
            problems += 1
        elif md_rel in reg.get("html_autoral", {}) and os.path.getmtime(out) < os.path.getmtime(src):
            print("AVISO (HTML autoral, confira à mão se reflete o md):", md_rel)
    ignore = set(reg.get("ignorar", []))
    for dirpath, dirnames, files in os.walk(root):
        dirnames[:] = [d for d in dirnames if d not in SKIP_DIRS]
        for fn in files:
            if fn.endswith(".md"):
                rel = os.path.relpath(os.path.join(dirpath, fn), root)
                if rel not in registered and rel not in ignore:
                    print("NÃO CLASSIFICADO no versoes.json:", rel)
                    problems += 1
    print("OK: nenhum problema" if not problems else "%d problema(s)" % problems)
    return 1 if problems else 0


def gaps(root):
    reg = load_registry(root)
    root = os.path.abspath(root)
    head = re.compile(r"^#{2,3}\s+(?:\d+\.\s*)?(Lacunas?|Known Gaps|Pendências.*|Limites e lacunas)\b", re.I)
    for md_rel, status, item in entries(reg):
        if status != "vigente":
            continue
        path = os.path.join(root, md_rel)
        if not os.path.exists(path):
            continue
        lines = open(path, encoding="utf-8").read().splitlines()
        i = 0
        while i < len(lines):
            if head.match(lines[i]):
                level = len(lines[i]) - len(lines[i].lstrip("#"))
                block = []
                i += 1
                while i < len(lines) and not (lines[i].startswith("#") and len(lines[i]) - len(lines[i].lstrip("#")) <= level):
                    block.append(lines[i])
                    i += 1
                text = "\n".join(block).strip()
                if text:
                    print("### %s\n%s\n" % (md_rel, text))
            else:
                i += 1


# ---------------------------------------------------------------- PDF
# Idea adapted from the Brandfy "guia-pdf" skill (Promovaweb, AGPL-3.0): the PDF is a print of the
# canonical Markdown, never an independent document. Code and CSS here are written from scratch.
PRINT_CSS = """@page{size:A4;margin:18mm 16mm}
body{font-size:10.5pt;background:#fff}main{max-width:none;padding:0}
.cover{break-after:page;min-height:235mm;display:flex;flex-direction:column;justify-content:center}
.cover h1{font-size:2.6rem;margin:0 0 .3em}.cover p{color:%(apoio)s}
.toc{break-after:page}.toc ul{list-style:none;padding:0}.toc li{margin:.5em 0;font-size:1.05rem}
.doc{break-before:page}
h1,h2,h3,h4{break-after:avoid}table,pre,blockquote,tr{break-inside:avoid}
th,td{overflow-wrap:anywhere}.tw{overflow:visible}pre{white-space:pre-wrap}
a{color:inherit;text-decoration:none;border-bottom:1px solid %(destaque)s}.toc a{border:0}"""


def pdf(root, chrome=None, out=None):
    """Print the current Markdown of the brand (registry order) to one A4 PDF through headless Chrome."""
    sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
    import brand_chrome
    from pathlib import Path
    from datetime import date

    reg = load_registry(root)
    root = os.path.abspath(root)
    docs = []
    for md_rel, status, item in entries(reg):
        if status != "vigente":
            continue
        if os.path.exists(os.path.join(root, md_rel)):
            docs.append((md_rel, item))
        else:
            print("FALTA O MD (fica fora do PDF):", md_rel)
    if not docs:
        print("Nada para imprimir: nenhum arquivo vigente existe em %s" % root)
        return 1
    ids = {md: "s-%d" % n for n, (md, _) in enumerate(docs, 1)}

    def make_resolve(md_rel):
        def resolve(href):
            if re.match(r"^(https?:|mailto:|#)", href):
                return href
            target, _, frag = href.split(" ")[0].partition("#")
            abs_t = os.path.normpath(os.path.join(root, os.path.dirname(md_rel), target))
            rel = os.path.relpath(abs_t, root)
            if rel in ids:
                return "#" + ids[rel]
            if os.path.exists(abs_t):
                return Path(abs_t).as_uri()
            return target
        return resolve

    sections, toc = [], []
    for md_rel, item in docs:
        with open(os.path.join(root, md_rel), encoding="utf-8") as f:
            body, title = convert(f.read(), make_resolve(md_rel))
        sections.append('<section class="doc" id="%s">%s</section>' % (ids[md_rel], body))
        toc.append('<li><a href="#%s">%s</a></li>' % (ids[md_rel], html.escape(item.get("titulo") or title or md_rel)))
    theme = dict(THEME_DEFAULT, **reg.get("tema", {}))
    fonts = reg.get("fontes_google", "")
    link = '<link rel="stylesheet" href="%s">' % html.escape(fonts) if fonts else ""
    brand = reg.get("marca", "") or os.path.basename(root)
    page_html = ('<!doctype html><html lang="pt-BR"><head><meta charset="utf-8"><title>%s</title>%s<style>%s\n%s</style></head><body><main>'
                 '<div class="cover"><h1>%s</h1><p>Manual da marca · %s</p></div>'
                 '<nav class="toc"><h2>Sumário</h2><ul>%s</ul></nav>%s</main></body></html>') % (
        html.escape(brand), link, CSS % theme, PRINT_CSS % theme, html.escape(brand),
        date.today().strftime("%d/%m/%Y"), "".join(toc), "\n".join(sections))
    html_dir = os.path.join(root, HTML_DIR)
    os.makedirs(html_dir, exist_ok=True)
    html_path = os.path.join(html_dir, "manual-para-pdf.html")
    with open(html_path, "w", encoding="utf-8") as f:
        f.write(page_html)

    slug = re.sub(r"[^a-z0-9]+", "-", brand.lower()).strip("-") or "marca"
    out_path = os.path.abspath(out) if out else os.path.join(root, "pdf", "%s-manual.pdf" % slug)
    if not out_path.startswith(root + os.sep):
        print("A saída precisa ficar dentro da pasta da marca (%s)." % root)
        return 2
    os.makedirs(os.path.dirname(out_path), exist_ok=True)
    try:
        browser = brand_chrome.find_chrome(chrome)
    except brand_chrome.ChromeNotFound as e:
        print(e)
        return 1
    if os.path.exists(out_path):
        os.remove(out_path)
    try:
        res = brand_chrome.run_headless(browser, ["--no-pdf-header-footer", "--virtual-time-budget=10000",
                                                  "--print-to-pdf=%s" % out_path, brand_chrome.file_url(html_path)])
    except RuntimeError as e:
        print(e)
        return 1
    if not os.path.exists(out_path) or os.path.getsize(out_path) == 0:
        print("O navegador não gerou o PDF (código %s). Saída: %s" % (res.returncode, res.stderr.decode("utf-8", "replace")[-400:]))
        return 1
    with open(out_path, "rb") as f:
        data = f.read()
    if not data.startswith(b"%PDF"):
        print("O arquivo gerado não é um PDF válido:", out_path)
        return 1
    pages = len(re.findall(rb"/Type\s*/Page(?![s\w])", data))
    print("PDF gerado: %s (%d página(s), %d KB, %d arquivo(s) do registro)" % (out_path, pages, len(data) // 1024, len(docs)))
    autoral = [md for md, _ in docs if md in reg.get("html_autoral", {})]
    if autoral:
        print("AVISO: o PDF imprime o texto destes arquivos, sem a amostra visual do HTML autoral: %s" % ", ".join(autoral))
    return 0


def main(argv):
    if len(argv) >= 3 and argv[1] == "pdf":
        opts = {"--chrome": None, "--out": None}
        rest = argv[3:]
        while rest:
            if rest[0] in opts and len(rest) >= 2:
                opts[rest[0]] = rest[1]
                rest = rest[2:]
            else:
                print(__doc__)
                return 2
        return pdf(argv[2], chrome=opts["--chrome"], out=opts["--out"])
    if len(argv) != 3 or argv[1] not in ("build", "check", "gaps", "sync"):
        print(__doc__)
        return 2
    cmd, root = argv[1], argv[2]
    if cmd == "build":
        build(root)
        return 0
    if cmd == "check":
        return check(root)
    if cmd == "sync":
        build(root)
        return check(root)
    gaps(root)
    return 0


if __name__ == "__main__":
    sys.exit(main(sys.argv))
