"""Gerador do design system de uma marca: le design_tokens.py e produz tokens.json, DESIGN.md e index.html.

Uso (Python 3.9+, sem dependencias):
  DS_BRAND_DIR=<pasta da marca> DS_LOGO_DIR=<pasta com logo.svg e logo-light.svg> \
  DS_VOICE_FILE=brand-voice.md [DS_OUT=<saida>] [DS_DATE=AAAA-MM-DD] \
  python3 -I build_design_system.py

Saida padrao: <DS_BRAND_DIR>/design-system/. Falha se algum par de contraste reprovar.

O QUE E ESPECIFICO DA MARCA (reescrever para outra marca; procure por "BRAND-SPECIFIC"):
  - design_tokens.py inteiro (cores, escalas, componentes, descricao);
  - ORIGEM, a lista de gaps em build_md, os textos de overview_html, principles_html, voice_html;
  - telas de exemplo (screen_*), conteudo dos componentes (c_*), regras de imagery_html.
Escreva todos os textos JA ACENTUADOS. Nao existe correcao automatica de acentos (ela quebrou o CSS uma vez).
Gerado a partir do uso real no WaiMonitor em 2026-10-19; reproduz byte a byte o resultado aprovado
quando chamado com DS_DATE=2026-10-19 e DS_VOICE_FILE=brand-voice-v2.md.
"""
import base64, html, json, re, sys, os
sys.path.insert(0, os.path.dirname(__file__))
from design_tokens import TOKENS as T, contrast_table, ratio

BRAND = os.environ.get("DS_BRAND_DIR")      # pasta da marca (onde fica brand-voice etc.)
OUT = os.environ.get("DS_OUT", BRAND + "/design-system")
PUB = os.environ.get("DS_LOGO_DIR")         # pasta com logo.svg (fundo claro) e logo-light.svg (fundo escuro)
DATE = os.environ.get("DS_DATE") or __import__("datetime").date.today().isoformat()
esc = html.escape



if not BRAND or not PUB:
    sys.exit("Defina DS_BRAND_DIR e DS_LOGO_DIR (ver o cabecalho deste arquivo).")

rows = contrast_table()
assert all(r["ok"] for r in rows), "contraste reprovado"
L, D = T["colors"]["light"], T["colors"]["dark"]
DESCR = T["description"]

# ---------- texto da voz lido do arquivo aprovado ----------
VOICE_FILE = os.environ.get("DS_VOICE_FILE", "brand-voice.md")
voice = open(BRAND + "/" + VOICE_FILE, encoding="utf-8").read()
def section(md, title):
    m = re.search(r"^## " + re.escape(title) + r"\n(.*?)(?=^## |\Z)", md, re.S | re.M)
    return m.group(1).strip() if m else ""
nunca = [re.sub(r"\s*\[[^\]]*\]\s*$", "", l.split(". ", 1)[1]).strip() for l in section(voice, "O que NÃO comunicar").splitlines() if re.match(r"^\d+\. ", l)]
assert len(nunca) >= 5, nunca
tracos = re.findall(r"^### \d+\. (.+)$", section(voice, "Traços"), re.M)
vocab = section(voice, "Vocabulário")

# ---------- CSS de tokens (mesmo texto no site e no export) ----------
def vars_block(mode):
    c = T["colors"][mode]
    lines = ["  --%s: %s;" % (k, v) for k, v in c.items()]
    for k, v in T["elevation"][mode].items():
        lines.append("  --shadow-%s: %s;" % (k, v))
    return "\n".join(lines)

def base_vars():
    lines = ["  --font-sans: %s;" % T["typography"]["font-sans"], "  --font-mono: %s;" % T["typography"]["font-mono"]]
    for k, v in T["rounded"].items(): lines.append("  --radius-%s: %s;" % (k, v))
    for k, v in T["spacing"].items(): lines.append("  --space-%s: %s;" % (k, v))
    for k, v in T["motion"]["duration"].items(): lines.append("  --dur-%s: %s;" % (k, v))
    for k, v in T["motion"]["easing"].items(): lines.append("  --ease-%s: %s;" % (k, v))
    return "\n".join(lines)

CSS_EXPORT = ":root,\n[data-theme=\"light\"] {\n%s\n%s\n}\n\n[data-theme=\"dark\"] {\n%s\n}" % (base_vars(), vars_block("light"), vars_block("dark"))

def tailwind_export():
    cl = "\n".join("  --color-%s: %s;" % (k, v) for k, v in L.items())
    cd = "\n".join("    --color-%s: %s;" % (k, v) for k, v in D.items())
    rad = "\n".join("  --radius-%s: %s;" % (k, v) for k, v in T["rounded"].items())
    sp = "\n".join("  --spacing-s%s: %s;" % (k, v) for k, v in T["spacing"].items())
    ease = "\n".join("  --ease-%s: %s;" % (k, v) for k, v in T["motion"]["easing"].items())
    return ("@import \"tailwindcss\";\n"
            "@custom-variant dark (&:where([data-theme=dark], [data-theme=dark] *));\n\n"
            "@theme {\n  --font-sans: %s;\n  --font-mono: %s;\n%s\n%s\n%s\n%s\n}\n\n"
            "/* Tema escuro: redefine as mesmas variáveis sob o atributo. */\n"
            "@layer base {\n  [data-theme=dark] {\n%s\n  }\n}\n"
            "/* Espaçamento nomeado como s1..s9 (p-s4 = 16px) para não sobrescrever a escala numérica padrão. */"
            % (T["typography"]["font-sans"], T["typography"]["font-mono"], cl, rad, sp, ease, cd))

JSON_EXPORT = json.dumps(T, indent=2, ensure_ascii=False)
JS_EXPORT = "export const theme = " + JSON_EXPORT + ";\n"

# ---------- YAML do front matter ----------
def q(v): return '"%s"' % str(v).replace('"', '\\"')
def ydump(d, ind=0):
    out = []
    for k, v in d.items():
        key = q(k) if re.match(r"^\d", str(k)) else k
        if isinstance(v, dict):
            out.append("  " * ind + "%s:" % key); out += ydump(v, ind + 1)
        else:
            out.append("  " * ind + "%s: %s" % (key, q(v)))
    return out
fm = {"name": T["name"], "description": DESCR, "colors": T["colors"],
      "typography": {"font-sans": T["typography"]["font-sans"], "font-mono": T["typography"]["font-mono"],
                     "scale": T["typography"]["scale"]},
      "rounded": T["rounded"], "spacing": T["spacing"], "components": T["components"]}
FRONT = "---\n" + "\n".join(ydump(fm)) + "\n---\n"

# ---------- DESIGN.md ----------
def mdtable(headers, rws):
    s = "| " + " | ".join(headers) + " |\n|" + "|".join(["---"] * len(headers)) + "|\n"
    return s + "\n".join("| " + " | ".join(str(c) for c in r) + " |" for r in rws) + "\n"

USO = {"bg": "fundo da página", "surface": "cartões e painéis", "surface-alt": "áreas secundárias, cabecalho de tabela",
       "border": "divisores decorativos", "border-strong": "borda de campos e botões secundarios (3:1)",
       "text": "texto principal", "text-muted": "texto de apoio", "primary": "marca: logo, ícones, fundos grandes (não para texto pequeno)",
       "primary-strong": "fundo de botão primário com texto branco", "primary-hover": "hover do botão primário",
       "on-primary": "texto sobre primary-strong", "link": "links e texto azul", "focus": "anel de foco",
       "alert": "marcador do alerta (ponto, borda)", "alert-text": "texto do alerta", "alert-bg": "fundo do alerta",
       "success": "estado de sucesso (cor funcional, não de marca)", "success-text": "texto de sucesso", "success-bg": "fundo de sucesso",
       "danger": "estado de erro (ícone)", "danger-strong": "fundo do botão destrutivo", "danger-text": "texto de erro", "danger-bg": "fundo de erro",
       "info-text": "texto informativo", "info-bg": "fundo informativo",
       "nav-bg": "fundo do menu lateral", "nav-text": "texto do menu", "nav-active": "item ativo do menu", "nav-border": "divisor do menu"}

# BRAND-SPECIFIC: reescrever para outra marca
ORIGEM = [("Azul #137FEC como cor de marca", "existente no app (tailwind.config.js)"),
          ("Inter como fonte", "existente no app"),
          ("Temas claro e escuro", "existente no app"),
          ("Fundo escuro #101922 (unifica #101922 e #101622 do app)", "proposta; ver Known Gaps"),
          ("Variante primary-strong #0E64C4 para texto e botões", "contraste 3,98:1 do azul original; aprovada pelo usuário em 2026-10-19"),
          ("Amarelo/âmbar queimado para alerta", "escolha do usuário; âmbar queimado para evitar tom de guru de vendas"),
          ("Cores de estado (sucesso, erro, info)", "necessidade funcional do Kanban; não são cores de marca"),
          ("Cantos médios (8 px em botões)", "app usa 4 a 24 px; direção visual pede cantos médios"),
          ("Movimento 100 a 240 ms", "escolha do usuário: rápido e seco"),
          ("Sem imagens de pessoas reais ou mensagens reais", "regra de privacidade da essência")]

# BRAND-SPECIFIC: reescrever para outra marca
def build_md():
    s = FRONT + "\n# Design system - %s\n\n" % T["name"]
    s += "## Overview\n\n%s\n\n" % DESCR
    s += "**Sensação:** ágil, confiável, atento. **Não deve parecer:** vigilância ou hacker, software corporativo pesado, guru de vendas agressivo, startup genérica.\n\n"
    s += "Este sistema estende a identidade existente do app (azul, Inter, temas claro e escuro, logo do balao). Nada foi substituído.\n\n"
    s += "### Origem das decisões\n\n" + mdtable(["Decisão", "Origem"], ORIGEM) + "\n"
    s += "Referências: `brand-voice-v2.md` (voz), `06-direção-visual.md` (direção), `style-guide.md` (existente, não alterado), `brandbook.md` (a criar).\n\n"
    s += "## Colors\n\n"
    for mode, c in (("Light", L), ("Dark", D)):
        s += "### %s\n\n" % mode + mdtable(["Token", "Valor", "Uso"], [("`%s`" % k, "`%s`" % v, USO.get(k, "")) for k, v in c.items()]) + "\n"
    s += "### Contraste conferido (WCAG)\n\nTexto normal: mínimo 4,5:1. Componentes e gráficos: mínimo 3:1. Cálculo de luminância relativa sobre os valores acima.\n\n"
    s += mdtable(["Tema", "Tipo", "Par", "Razão", "Mínimo", "Resultado"],
                 [(r["mode"], r["kind"], "%s sobre %s" % (r["fg"], r["bg"]), str(r["ratio"]).replace(".", ","), str(r["min"]).replace(".", ","), "passa" if r["ok"] else "FALHA") for r in rows]) + "\n"
    s += "Valor original do app que reprova: `#137FEC` sobre `#FFFFFF` = 3,98:1 (texto normal exige 4,5:1). Por isso `primary` fica restrito a logo, ícones e fundos grandes.\n\n"
    s += "## Typography\n\nFamília: Inter, com pilha de sistema como alternativa. A fonte **não é embutida** neste sistema; sem Inter instalada, o navegador usa a fonte do sistema.\n\n"
    s += mdtable(["Nível", "Tamanho", "Linha", "Peso"], [(k, v["size"], v["line"], v["weight"]) for k, v in T["typography"]["scale"].items()]) + "\n"
    s += "Regras: comprimento de linha de 60 a 75 caracteres; tracking só em caixa alta; o logo é arquivo, nunca recriado em Inter.\n\n"
    s += "## Layout\n\nEspaçamento em base de 4 px: " + ", ".join("`space-%s` = %s" % (k, v) for k, v in T["spacing"].items()) + ".\n\n"
    s += "Raios: " + ", ".join("`%s` = %s" % (k, v) for k, v in T["rounded"].items()) + ". Botões e campos usam `md`; cartões `lg`; tags `full`.\n\n"
    s += "Grade: conteúdo com largura maxima de 1120 px; menu lateral de 264 px; respiro generoso.\n\n"
    s += "## Elevation\n\nTrês níveis. No tema claro, sombras discretas; no tema escuro, borda em vez de sombra.\n\n"
    s += mdtable(["Nível", "Claro", "Escuro"], [(k, "`%s`" % T["elevation"]["light"][k], "`%s`" % T["elevation"]["dark"][k]) for k in T["elevation"]["light"]]) + "\n"
    s += "Movimento: " + ", ".join("`%s` = %s" % (k, v) for k, v in T["motion"]["duration"].items()) + "; curvas `standard`, `enter`, `exit`. Rápido e seco; respeita `prefers-reduced-motion`.\n\n"
    s += "## Components\n\nGrupos: botões, tags, campos, cartões, dados e navegação, todos mostrados em painel Light e Dark no site.\n\n"
    s += mdtable(["Componente", "Tokens"], [("`%s`" % k, ", ".join("%s: %s" % (a, b) for a, b in v.items())) for k, v in T["components"].items()]) + "\n"
    s += "Estados cobertos: padrão, hover, foco (anel de 2 px em `focus`), desabilitado e erro. O alerta (cartão âmbar) é o único elemento que usa `alert`.\n\n"
    s += "## Imagery\n\n**Sem imagens de referência anexadas.** Os estilos travados (Style 01, Style 02...) não foram criados. Direção aprovada: tela do produto e do celular em destaque; tipografia grande sobre fundo simples. Nunca mostrar nome, foto ou mensagem real de pessoa ou grupo; usar dados fictícios. Nunca: olho, cadeado, código verde, notas de dinheiro em leque.\n\nPara criar estilos travados, anexar imagens-modelo e rodar de novo a etapa 7.\n\n"
    s += "## Responsive Behavior\n\nPontos de quebra: 900 px (menu lateral vira gaveta; painéis Light/Dark empilham) e 560 px (grades de uma coluna). Alvos de toque de pelo menos 44 px. Tabelas rolam dentro do próprio contêiner. Sem rolagem horizontal da página a partir de 360 px.\n\n"
    s += "## Known Gaps\n\n"
    gaps = ["Inter não esta embutida; depende da fonte instalada ou da pilha de sistema.",
            "O app tem dois fundos escuros (`#101922` e `#101622`); este sistema unifica em `#101922`. Não apliquei mudança no app.",
            "`primary-strong` (#0E64C4), alerta âmbar e as cores de estado são novos e precisam de revisão do time de produto antes de entrar no app.",
            "Sem imagens-modelo: nenhum estilo travado de imagem.",
            "O ponto de destaque do ícone e o ping sonoro estão definidos só em texto; não há arquivos.",
            "O export Tailwind v4 usa `@theme` e `@custom-variant` (confirmados na documentação oficial), mas a redefinição de variáveis sob `[data-theme=dark]` não foi testada em um build do Tailwind.",
            "O app usa Tailwind 3.4; para ele, o formato v4 acima não se aplica diretamente.",
            "Landing page e telas reais do app não foram lidas; as telas deste sistema são exemplos.",
            "Impressão em papel, Safari/iOS e leitor de tela não foram verificados."]
    s += "\n".join("- " + g for g in gaps) + "\n"
    return s

DESIGN_MD = build_md()


# ---------- logos ----------
def datauri(path):
    return "data:image/svg+xml;base64," + base64.b64encode(open(path, "rb").read()).decode()
LOGO_BLACK = datauri(PUB + "/logo.svg")        # para fundo claro
LOGO_WHITE = datauri(PUB + "/logo-light.svg")  # para fundo escuro

# ---------- HTML ----------
SECTIONS = [("overview", "Overview", "Visão geral"), ("principles", "Principles", "Princípios"), ("color", "Color", "Cor"),
            ("typography", "Typography", "Tipografia"), ("spacing", "Spacing", "Espaçamento"), ("shape", "Shape", "Forma e elevação"),
            ("motion", "Motion", "Movimento"), ("components", "Components", "Componentes"), ("patterns", "Patterns", "Telas de exemplo"),
            ("imagery", "Imagery", "Imagem"), ("token-exports", "Token exports", "Exportar tokens"), ("voice-tone", "Voice & tone", "Voz e tom")]

def panel(mode, inner, label=None):
    return '<div class="panel" data-theme="%s"><span class="panel-tag">%s</span>%s</div>' % (mode, label or mode.capitalize(), inner)

def pair(inner_fn):
    return '<div class="pair">%s%s</div>' % (panel("light", inner_fn("light")), panel("dark", inner_fn("dark")))

def code(id_, text):
    return '<div class="codeblock"><button class="btn btn-secondary btn-sm copy-btn" data-target="%s" type="button">Copiar</button><pre id="%s"><code>%s</code></pre></div>' % (id_, id_, esc(text))

SW_ORDER = list(L.keys())
def swatches(mode):
    c = T["colors"][mode]
    items = []
    for k in SW_ORDER:
        v = c[k]
        items.append('<button class="swatch" type="button" data-copy="%s" style="--sw:%s" aria-label="Copiar %s %s"><span class="chip" style="background:%s"></span><span class="sw-name">%s</span><span class="sw-hex">%s</span></button>' % (v, v, k, v, v, k, v))
    return '<div class="swatch-grid">%s</div>' % "".join(items)

def contrast_html():
    out = ['<div class="table-wrap"><table class="tbl"><thead><tr><th>Tema</th><th>Tipo</th><th>Par</th><th>Razão</th><th>Mínimo</th><th>Resultado</th></tr></thead><tbody>']
    for r in rows:
        out.append("<tr><td>%s</td><td>%s</td><td>%s sobre %s</td><td>%s:1</td><td>%s:1</td><td>%s</td></tr>" % (r["mode"], r["kind"], r["fg"], r["bg"], str(r["ratio"]).replace(".", ","), str(r["min"]).replace(".", ","), "passa" if r["ok"] else "FALHA"))
    out.append("</tbody></table></div>")
    return "".join(out)

def type_samples():
    out = []
    for k, v in T["typography"]["scale"].items():
        fam = "var(--font-mono)" if k == "code" else "var(--font-sans)"
        out.append('<div class="type-row"><div class="type-meta"><b>%s</b><span>%s / %s / %s</span></div><div class="type-sample" style="font:%s %s/%s %s">Pediram social media no grupo, há 2 min.</div></div>' % (k, v["size"], v["line"], v["weight"], v["weight"], v["size"], v["line"], fam))
    return "".join(out)

def spacing_html():
    return "".join('<div class="sp-row"><span class="sp-name">space-%s</span><span class="sp-val">%s</span><span class="sp-bar" style="width:%s"></span></div>' % (k, v, v) for k, v in T["spacing"].items())

def shape_html():
    rad = "".join('<div class="shape-item"><div class="shape-box" style="border-radius:%s"></div><b>%s</b><span>%s</span></div>' % (v, k, v) for k, v in T["rounded"].items())
    ele = "".join('<div class="shape-item"><div class="shape-box elev" style="box-shadow:var(--shadow-%s)"></div><b>nível %s</b></div>' % (k, k) for k in T["elevation"]["light"])
    return '<h3>Raios</h3><div class="shape-row">%s</div><h3>Elevação</h3><div class="pair">%s%s</div>' % (rad, panel("light", '<div class="shape-row">%s</div>' % ele), panel("dark", '<div class="shape-row">%s</div>' % ele))

def motion_html():
    dur = "".join('<div class="mo-row"><b>%s</b><span>%s</span><div class="mo-track"><div class="mo-dot" style="--d:var(--dur-%s)"></div></div></div>' % (k, v, k) for k, v in T["motion"]["duration"].items())
    ease = "".join("<li><code>%s</code>: <code>%s</code></li>" % (k, v) for k, v in T["motion"]["easing"].items())
    return '<p>Rápido e seco: o alerta acende, não desliza. Sem efeito elástico.</p><button class="btn btn-primary" id="play-motion" type="button">Reproduzir</button><div class="mo-demo" id="mo-demo">%s</div><ul class="plain">%s</ul><p class="muted">Com <code>prefers-reduced-motion</code> ativo, as animações são reduzidas ao mínimo.</p>' % (dur, ease)

# --- componentes ---
def c_buttons(m):
    return ('<div class="row"><button class="btn btn-primary" type="button">Responder agora</button><button class="btn btn-secondary" type="button">Ver grupo</button>'
            '<button class="btn btn-ghost" type="button">Ignorar</button><button class="btn btn-danger" type="button">Remover palavra</button></div>'
            '<div class="row"><button class="btn btn-primary btn-sm" type="button">Pequeno</button><button class="btn btn-primary" type="button" disabled>Desabilitado</button>'
            '<button class="btn btn-secondary btn-icon" type="button" aria-label="Notificações"><svg width="18" height="18" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" aria-hidden="true"><path d="M6 8a6 6 0 1 1 12 0c0 7 3 9 3 9H3s3-2 3-9"/><path d="M10 21h4"/></svg></button></div>')
def c_tags(m):
    return ('<div class="row"><span class="tag tag-neutral">Grupo</span><span class="tag tag-alert"><i class="dot"></i>Pedido novo</span><span class="tag tag-info">Em contato</span>'
            '<span class="tag tag-success">Fechado</span><span class="tag tag-danger">Pausado</span><span class="tag tag-neutral">social media <button class="tag-x" type="button" aria-label="Remover">x</button></span></div>')
def c_inputs(m):
    i = m
    return ('<div class="form"><div class="field"><label for="k-%s">Palavra-chave</label><input id="k-%s" class="input" value="social media" /><small>Avisamos quando aparecer nos seus grupos.</small></div>'
            '<div class="field"><label for="e-%s">Palavra-chave (com erro)</label><input id="e-%s" class="input is-error" value="" aria-invalid="true" /><small class="err">Digite ao menos 3 letras.</small></div>'
            '<div class="field"><label for="s-%s">Grupo</label><select id="s-%s" class="input"><option>Todos os grupos</option><option>Grupo Networking Centro</option></select></div>'
            '<div class="row"><label class="check"><input type="checkbox" checked /> Avisar no celular</label><label class="check"><input type="radio" name="r-%s" checked /> Imediato</label><label class="check"><input type="radio" name="r-%s" /> Resumo</label>'
            '<label class="switch"><input type="checkbox" role="switch" checked /><span class="sw-track"></span><span>Radar ligado</span></label></div></div>') % ((i,) * 8)
# BRAND-SPECIFIC: reescrever para outra marca
def c_cards(m):
    return ('<div class="stack"><div class="card"><h4>Grupo Networking Centro</h4><p class="muted">14 palavras-chave ativas. Último pedido há 2 min.</p></div>'
            '<div class="card alert-card"><div class="alert-top"><i class="dot big"></i><b>Pedido de social media</b><span class="muted-alert">há 2 min</span></div><p>"Alguém indica um bom social media aqui no grupo?"</p><div class="row"><button class="btn btn-primary btn-sm" type="button">Responder agora</button><button class="btn btn-ghost btn-sm" type="button">Ver conversa</button></div></div>'
            '<div class="card stat"><span class="muted">Pedidos vistos hoje</span><strong>12</strong><span class="tag tag-success">exemplo</span></div></div>')
# BRAND-SPECIFIC: reescrever para outra marca
def c_data(m):
    return ('<div class="table-wrap"><table class="tbl"><thead><tr><th>Grupo</th><th>Palavras</th><th>Status</th></tr></thead><tbody>'
            '<tr><td>Networking Centro</td><td>6</td><td><span class="tag tag-success">Ativo</span></td></tr>'
            '<tr><td>Corretores Zona Sul</td><td>9</td><td><span class="tag tag-success">Ativo</span></td></tr>'
            '<tr><td>Bairro Jardim</td><td>3</td><td><span class="tag tag-danger">Pausado</span></td></tr></tbody></table></div>'
            '<div class="empty"><b>Nenhum pedido ainda</b><p class="muted">Quando alguém pedir o que você oferece, aparece aqui.</p></div>')
def c_nav(m):
    return ('<div class="topnav"><span class="topnav-brand">WAI</span><a class="active" href="#components">Painel</a><a href="#components">Kanban</a><a href="#components">Palavras</a><a href="#components">Grupos</a></div>'
            '<div class="tabs" role="tablist"><button class="tab active" role="tab" aria-selected="true" type="button">Novos</button><button class="tab" role="tab" aria-selected="false" type="button">Em contato</button><button class="tab" role="tab" aria-selected="false" type="button">Fechados</button></div>'
            '<div class="crumbs"><a href="#components">Painel</a> / <a href="#components">Grupos</a> / <b>Networking Centro</b></div>'
            '<div class="pager"><button class="btn btn-secondary btn-sm" type="button">Anterior</button><span class="muted">Página 1 de 4</span><button class="btn btn-secondary btn-sm" type="button">Próxima</button></div>')

COMPONENTS = [("Botões", c_buttons), ("Tags", c_tags), ("Campos", c_inputs), ("Cartões", c_cards), ("Dados", c_data), ("Navegação", c_nav)]
def components_html():
    return "".join('<h3>%s</h3>%s' % (n, pair(fn)) for n, fn in COMPONENTS)

# --- telas ---
# BRAND-SPECIFIC: reescrever para outra marca
def screen_dash():
    return ('<div class="scr"><div class="scr-head"><h4>Painel</h4><span class="tag tag-neutral">Conteúdo de exemplo</span></div>'
            '<div class="grid3"><div class="card stat"><span class="muted">Pedidos hoje</span><strong>12</strong></div><div class="card stat"><span class="muted">Respondidos a tempo</span><strong>9</strong></div><div class="card stat"><span class="muted">Grupos no radar</span><strong>14</strong></div></div>'
            '<div class="card alert-card"><div class="alert-top"><i class="dot big"></i><b>Pedido de social media</b><span class="muted-alert">há 2 min</span></div><p>Grupo Networking Centro</p><button class="btn btn-primary btn-sm" type="button">Responder agora</button></div>'
            '<div class="card"><b>Pedido de plano de saúde</b><p class="muted">Grupo Bairro Jardim, há 18 min</p></div></div>')
# BRAND-SPECIFIC: reescrever para outra marca
def screen_kanban():
    def col(t, n, cards):
        return '<div class="kcol"><div class="kcol-h"><b>%s</b><span class="tag tag-neutral">%s</span></div>%s</div>' % (t, n, "".join('<div class="card kcard"><b>%s</b><p class="muted">%s</p></div>' % c for c in cards))
    return ('<div class="scr"><div class="scr-head"><h4>Kanban de oportunidades</h4><span class="tag tag-neutral">Conteúdo de exemplo</span></div><div class="kanban">'
            + col("Novo", 2, [("Social media", "Networking Centro, há 2 min"), ("Seguro auto", "Corretores Zona Sul, há 40 min")])
            + col("Em contato", 1, [("Apartamento 2 quartos", "Bairro Jardim, ontem")])
            + col("Fechado", 1, [("Gestão de redes", "Networking Centro, há 3 dias")]) + '</div></div>')
# BRAND-SPECIFIC: reescrever para outra marca
def screen_keywords():
    return ('<div class="scr"><div class="scr-head"><h4>Palavras-chave</h4><span class="tag tag-neutral">Conteúdo de exemplo</span></div>'
            '<div class="row"><input class="input" id="new-kw" name="new-kw" placeholder="Nova palavra-chave" aria-label="Nova palavra-chave" /><button class="btn btn-primary" type="button">Adicionar</button></div>'
            '<div class="row"><span class="tag tag-neutral">social media</span><span class="tag tag-neutral">gestor de tráfego</span><span class="tag tag-neutral">indica</span></div>'
            '<div class="table-wrap"><table class="tbl"><thead><tr><th>Grupo</th><th>Radar</th></tr></thead><tbody><tr><td>Networking Centro</td><td><label class="switch"><input type="checkbox" role="switch" checked /><span class="sw-track"></span></label></td></tr>'
            '<tr><td>Bairro Jardim</td><td><label class="switch"><input type="checkbox" role="switch" /><span class="sw-track"></span></label></td></tr></tbody></table></div></div>')
# BRAND-SPECIFIC: reescrever para outra marca
def screen_post():
    return ('<div class="post"><span class="post-tag">EXEMPLO DE FORMATO</span><p class="post-big">Pediram social media no grupo.</p><p class="post-big post-sub">Quem viu primeiro respondeu.</p>'
            '<div class="post-foot"><i class="dot big"></i><span>WaiMonitor</span></div></div>')

def patterns_html():
    cap = '<p class="muted">Telas de exemplo com conteúdo fictício. Não é caso real, nem mostra pessoas ou grupos reais.</p>'
    items = [("Painel", screen_dash(), "light"), ("Kanban", screen_kanban(), "dark"), ("Palavras-chave e grupos", screen_keywords(), "light"), ("Cartão de Instagram (4:5)", screen_post(), "dark")]
    return cap + "".join('<h3>%s</h3>%s' % (n, panel(m, s, "Tema " + m)) for n, s, m in items)

# BRAND-SPECIFIC: reescrever para outra marca
def imagery_html():
    rules = [("Estilo principal", "Tela do produto e do celular em destaque (alerta chegando, grupo, pedido)"),
             ("Estilo secundário", "Tipografia grande sobre fundo simples, nas cores da marca"),
             ("Nunca mostrar", "Nome, foto ou mensagem real de pessoa ou grupo; olho, cadeado, código verde, notas de dinheiro em leque"),
             ("Dados nas telas", "Sempre fictícios ou anonimizados"),
             ("Ponto de destaque", "Elemento gráfico âmbar separado do logo; o logo não e alterado")]
    tb = "".join("<tr><td>%s</td><td>%s</td></tr>" % (a, b) for a, b in rules)
    return ('<div class="card placeholder"><b>Sem imagens de referência anexadas</b><p>Os estilos travados (Style 01, Style 02...) ainda não foram criados. Anexe imagens-modelo e rode de novo a etapa 7 para criar um estilo por imagem, com tabela de regras e prompt copiável.</p></div>'
            '<h3>Direção aprovada</h3><div class="table-wrap"><table class="tbl"><thead><tr><th>Regra</th><th>Definição</th></tr></thead><tbody>%s</tbody></table></div>' % tb)

def exports_html():
    return ('<h3>CSS variables</h3>' + code("x-css", CSS_EXPORT) + '<h3>Tailwind v4</h3>' + code("x-tw", tailwind_export())
            + '<h3>JSON</h3>' + code("x-json", JSON_EXPORT) + '<h3>Objeto JS</h3>' + code("x-js", JS_EXPORT))

# BRAND-SPECIFIC: reescrever para outra marca
def voice_html():
    nl = "".join("<li>%s</li>" % esc(x) for x in nunca)
    tr = "".join("<li>%s</li>" % esc(x) for x in tracos)
    return ('<p>A voz não é definida aqui. Este resumo vem de <code>brand-voice-v2.md</code>, o arquivo de referência.</p>'
            '<div class="card"><h4>Colega que avisa na hora</h4><p>Personalidade: Herói (o herói é o cliente) com Sábio de apoio. Humor leve e raro, nunca em alerta ou em assunto de privacidade.</p><h4>Traços</h4><ul class="plain">%s</ul></div>'
            '<h3>O que NÃO comunicar</h3><div class="card alert-card"><ol class="plain">%s</ol></div>'
            '<p class="muted">Fonte: <code>brand-voice-v2.md</code>. Em caso de diferença, vale o arquivo.</p>') % (tr, nl)

# BRAND-SPECIFIC: reescrever para outra marca
def principles_html():
    ps = [("Mostrar só o que importa", "Cada tela tem uma ação principal. Mais recurso não é mais valor.", "crença: simples vence completo"),
          ("Acender no momento certo", "O alerta é o único elemento âmbar. Quando tudo acende, nada acende.", "inimigo: perder negócio por demora"),
          ("Contraste antes de enfeite", "Texto a 4,5:1 e componentes a 3:1, nos dois temas.", "marca: confiável"),
          ("Respeitar o contexto", "Nunca mostrar mensagem, nome ou foto reais. Dados de exemplo são fictícios.", "crença: respeito ao contexto dos grupos"),
          ("Rápido e seco", "Movimento de 100 a 240 ms, sem efeito elástico.", "marca: ágil"),
          ("Marca sem peso", "Respiro, azul vivo e nada de cara de sistema de gestão.", "não deve parecer software corporativo pesado")]
    return '<div class="grid2">%s</div>' % "".join('<div class="card"><h4>%s</h4><p>%s</p><span class="tag tag-neutral">%s</span></div>' % p for p in ps)

# BRAND-SPECIFIC: reescrever para outra marca
def overview_html():
    nop = [("Vigilância ou hacker", "Sem olho, cadeado, código caindo, preto com neon verde."), ("Software corporativo pesado", "Sem tabela cinza densa como cara da marca."),
           ("Guru de vendas agressivo", "Sem vermelho e amarelo saturados, cifrão, contagem regressiva."), ("Startup genérica", "Sem gradiente roxo nem ilustração de gente sem rosto.")]
    og = "".join("<tr><td>%s</td><td>%s</td></tr>" % o for o in ORIGEM)
    return ('<p>%s</p><p><b>Sensação:</b> ágil, confiável, atento.</p>'
            '<div class="pair">%s%s</div>'
            '<h3>Não deve parecer</h3><div class="table-wrap"><table class="tbl"><tbody>%s</tbody></table></div>'
            '<h3>Origem das decisões</h3><div class="table-wrap"><table class="tbl"><thead><tr><th>Decisão</th><th>Origem</th></tr></thead><tbody>%s</tbody></table></div>'
            '<p class="muted">Referências: brand-voice-v2.md, 06-direção-visual.md, style-guide.md (existente, não alterado).</p>') % (
        esc(DESCR), panel("light", '<img class="logo-demo" src="%s" alt="Logo WAI Monitor, versão para fundo claro" />' % LOGO_BLACK), panel("dark", '<img class="logo-demo" src="%s" alt="Logo WAI Monitor, versão para fundo escuro" />' % LOGO_WHITE),
        "".join("<tr><td><b>%s</b></td><td>%s</td></tr>" % o for o in nop), og)

BODIES = {"overview": overview_html(), "principles": principles_html(),
          "color": '<p>Clique em uma amostra para copiar o valor. Cada tema mostra seus próprios valores.</p><h3>Light</h3>%s<h3>Dark</h3>%s<h3>Contraste conferido</h3><p class="muted">56 pares calculados sobre estes valores. Valor original do app que reprova: #137FEC sobre #FFFFFF, 3,98:1. Por isso <code>primary</code> fica para logo, ícones e fundos grandes; texto e botões usam <code>primary-strong</code>.</p>%s' % (swatches("light"), swatches("dark"), contrast_html()),
          "typography": '<p>Inter, com pilha de sistema. A fonte não é embutida: sem Inter instalada, o navegador usa a do sistema.</p>%s' % type_samples(),
          "spacing": '<p>Base de 4 px. Só estes degraus.</p><div class="sp">%s</div>' % spacing_html(),
          "shape": shape_html(), "motion": motion_html(), "components": components_html(), "patterns": patterns_html(),
          "imagery": imagery_html(), "token-exports": exports_html(), "voice-tone": voice_html()}

def nav_html():
    return "".join('<a href="#%s">%s</a>' % (i, n) for i, n, _ in SECTIONS)
def sections_html():
    return "".join('<section id="%s"><h2>%s <small>%s</small></h2>%s</section>' % (i, n, s, BODIES[i]) for i, n, s in SECTIONS)

CSS = r"""
%%TOKENS%%
*{box-sizing:border-box}
html{scroll-behavior:smooth}
body{margin:0;background:var(--bg);color:var(--text);font-family:var(--font-sans);font-size:1rem;line-height:1.55;-webkit-font-smoothing:antialiased}
section{scroll-margin-top:76px}
h1,h2,h3,h4{margin:0 0 var(--space-3);line-height:1.2}
h2{font-size:1.75rem;font-weight:700;padding-top:var(--space-6);display:flex;align-items:baseline;gap:var(--space-3);flex-wrap:wrap}
h2 small{font-size:.875rem;font-weight:500;color:var(--text-muted)}
h3{font-size:1.25rem;font-weight:600;margin-top:var(--space-6)}
h4{font-size:1.0625rem;font-weight:600}
p{margin:0 0 var(--space-3)} a{color:var(--link)}
code,pre{font-family:var(--font-mono);font-size:.875rem}
code{background:var(--surface-alt);padding:1px 6px;border-radius:var(--radius-sm)}
:focus-visible{outline:2px solid var(--focus);outline-offset:2px}
.muted{color:var(--text-muted)} ul.plain,ol.plain{margin:0 0 var(--space-3);padding-left:1.25rem}
.side{position:fixed;inset:0 auto 0 0;width:264px;background:var(--nav-bg);color:var(--nav-text);padding:var(--space-4);overflow:auto;border-right:1px solid var(--nav-border);z-index:30;transition:transform var(--dur-base) var(--ease-standard)}
.side img{width:170px;height:auto;display:block;margin:var(--space-2) 0 var(--space-5)}
.side a{display:flex;align-items:center;min-height:44px;color:var(--nav-text);text-decoration:none;padding:var(--space-2) var(--space-3);border-radius:var(--radius-md);font-size:.9375rem}
.side a:hover,.side a.on{background:var(--nav-border);color:var(--nav-active)}
.side .ver{margin-top:var(--space-5);font-size:.75rem;color:var(--nav-text)}
.main{margin-left:264px}
.topbar{position:sticky;top:0;z-index:20;display:flex;gap:var(--space-2);align-items:center;justify-content:flex-end;padding:var(--space-3) var(--space-5);background:var(--surface);border-bottom:1px solid var(--border)}
.topbar .spacer{flex:1}.topbar .ttl{font-weight:600}
.wrap{max-width:1120px;margin:0 auto;padding:0 var(--space-5) var(--space-9)}
.hero{padding:var(--space-7) 0 var(--space-3)} .hero h1{font-size:3rem;font-weight:800;line-height:1.1}
.btn.menu-btn{display:none}
.btn{display:inline-flex;align-items:center;justify-content:center;gap:var(--space-2);min-height:44px;padding:var(--space-2) var(--space-4);border-radius:var(--radius-md);border:1px solid transparent;font:600 .9375rem/1.2 var(--font-sans);cursor:pointer;transition:background var(--dur-fast) var(--ease-standard),border-color var(--dur-fast) var(--ease-standard)}
.btn-sm{min-height:36px;padding:var(--space-1) var(--space-3);font-size:.875rem}
.btn-icon{padding:var(--space-2);min-width:44px}
.btn-primary{background:var(--primary-strong);color:var(--on-primary)} .btn-primary:hover{background:var(--primary-hover)}
.btn-secondary{background:var(--surface);color:var(--text);border-color:var(--border-strong)} .btn-secondary:hover{background:var(--surface-alt)}
.btn-ghost{background:transparent;color:var(--link)} .btn-ghost:hover{background:var(--surface-alt)}
.btn-danger{background:var(--danger-strong);color:var(--on-primary)}
.btn[disabled]{opacity:.45;cursor:not-allowed}
.tag{display:inline-flex;align-items:center;gap:6px;padding:var(--space-1) var(--space-3);border-radius:var(--radius-full);font:500 .75rem/1.4 var(--font-sans);background:var(--surface-alt);color:var(--text)}
.tag-alert{background:var(--alert-bg);color:var(--alert-text)} .tag-success{background:var(--success-bg);color:var(--success-text)}
.tag-danger{background:var(--danger-bg);color:var(--danger-text)} .tag-info{background:var(--info-bg);color:var(--info-text)}
.tag-x{background:none;border:0;color:inherit;cursor:pointer;font:inherit;min-width:44px;min-height:44px;margin:-14px -14px -14px -8px}
.dot{display:inline-block;width:8px;height:8px;border-radius:50%;background:var(--alert)} .dot.big{width:12px;height:12px}
.row{display:flex;flex-wrap:wrap;gap:var(--space-3);align-items:center;margin-bottom:var(--space-3)}
.stack>*+*{margin-top:var(--space-3)}
.form .field{margin-bottom:var(--space-3)} label{font-weight:600;font-size:.875rem;display:block;margin-bottom:var(--space-1)}
.field small{display:block;color:var(--text-muted);margin-top:var(--space-1)} .field small.err{color:var(--danger-text)}
.input{width:100%;min-height:44px;padding:var(--space-2) var(--space-3);border-radius:var(--radius-md);border:1px solid var(--border-strong);background:var(--surface);color:var(--text);font:inherit}
.input.is-error{border-color:var(--danger);box-shadow:0 0 0 1px var(--danger)}
.check{display:inline-flex;align-items:center;gap:var(--space-2);font-weight:500;margin:0;min-height:44px} .check input{accent-color:var(--primary-strong);width:18px;height:18px}
.switch{display:inline-flex;align-items:center;gap:var(--space-2);font-weight:500;margin:0;cursor:pointer;position:relative;min-height:44px}
.switch input{position:absolute;opacity:0;width:100%;height:100%;left:0;top:0;margin:0;cursor:pointer}
.sw-track{width:44px;height:26px;border-radius:var(--radius-full);background:var(--border-strong);position:relative;transition:background var(--dur-fast) var(--ease-standard)}
.sw-track::after{content:"";position:absolute;top:3px;left:3px;width:20px;height:20px;border-radius:50%;background:var(--surface);transition:transform var(--dur-fast) var(--ease-standard)}
.switch input:checked+.sw-track{background:var(--primary-strong)} .switch input:checked+.sw-track::after{transform:translateX(18px)}
.switch input:focus-visible+.sw-track{outline:2px solid var(--focus);outline-offset:2px}
.card{background:var(--surface);border:1px solid var(--border);border-radius:var(--radius-lg);padding:var(--space-4);box-shadow:var(--shadow-1)}
.card h4{margin-bottom:var(--space-2)}
.alert-card{background:var(--alert-bg);color:var(--alert-text);border-color:var(--alert);border-left:4px solid var(--alert)}
.alert-top{display:flex;align-items:center;gap:var(--space-2);margin-bottom:var(--space-2)} .muted-alert{margin-left:auto;font-size:.8125rem}
.stat{display:flex;flex-direction:column;gap:var(--space-1)} .stat strong{font-size:2.25rem;line-height:1.1}
.placeholder{border-style:dashed}
.table-wrap{overflow-x:auto;border:1px solid var(--border);border-radius:var(--radius-lg);background:var(--surface);margin-bottom:var(--space-3)}
.tbl{width:100%;min-width:520px;border-collapse:collapse;font-size:.875rem} .tbl th,.tbl td{text-align:left;padding:var(--space-2) var(--space-3);border-bottom:1px solid var(--border);vertical-align:top}
.tbl th{background:var(--surface-alt);font-weight:600} .tbl tr:last-child td{border-bottom:0}
.empty{border:1px dashed var(--border-strong);border-radius:var(--radius-lg);padding:var(--space-5);text-align:center}
.topnav{display:flex;gap:var(--space-2);align-items:center;background:var(--nav-bg);padding:var(--space-2) var(--space-3);border-radius:var(--radius-lg);margin-bottom:var(--space-3);flex-wrap:wrap}
.topnav-brand{font-weight:800;color:var(--nav-active);margin-right:var(--space-3)}
.topnav a{color:var(--nav-text);text-decoration:none;padding:var(--space-2) var(--space-3);border-radius:var(--radius-md)} .topnav a.active,.topnav a:hover{background:var(--nav-border);color:var(--nav-active)}
.tabs{display:flex;gap:var(--space-1);border-bottom:1px solid var(--border);margin-bottom:var(--space-3);overflow-x:auto}
.tab{background:none;border:0;border-bottom:2px solid transparent;padding:var(--space-3) var(--space-4);font:600 .9375rem var(--font-sans);color:var(--text-muted);cursor:pointer;min-height:44px}
.tab.active{color:var(--link);border-bottom-color:var(--primary-strong)}
.crumbs{font-size:.875rem;margin-bottom:var(--space-3)} .pager{display:flex;gap:var(--space-3);align-items:center}
.pair{display:grid;grid-template-columns:1fr 1fr;gap:var(--space-4);margin-bottom:var(--space-4)}
.panel{position:relative;background:var(--bg);color:var(--text);border:1px solid var(--border);border-radius:var(--radius-xl);padding:var(--space-5) var(--space-4) var(--space-4);min-width:0}
.panel-tag{position:absolute;top:-11px;left:var(--space-4);background:var(--surface-alt);color:var(--text);border:1px solid var(--border-strong);border-radius:var(--radius-full);padding:0 var(--space-3);font:600 .75rem/20px var(--font-sans);text-transform:uppercase;letter-spacing:.04em}
.logo-demo{max-width:100%;height:auto;width:240px;display:block}
.grid2{display:grid;grid-template-columns:1fr 1fr;gap:var(--space-4)} .grid3{display:grid;grid-template-columns:repeat(3,1fr);gap:var(--space-3);margin-bottom:var(--space-3)}
.swatch-grid{display:grid;grid-template-columns:repeat(auto-fill,minmax(150px,1fr));gap:var(--space-3);margin-bottom:var(--space-4)}
.swatch{display:flex;flex-direction:column;gap:2px;text-align:left;background:var(--surface);color:var(--text);border:1px solid var(--border);border-radius:var(--radius-md);padding:var(--space-2);cursor:pointer;font:inherit;min-height:44px}
.swatch .chip{height:44px;border-radius:var(--radius-sm);border:1px solid var(--border-strong);display:block}
.sw-name{font-weight:600;font-size:.8125rem;margin-top:4px} .sw-hex{font-family:var(--font-mono);font-size:.75rem;color:var(--text-muted)}
.type-row{display:grid;grid-template-columns:200px 1fr;gap:var(--space-4);align-items:center;padding:var(--space-3) 0;border-bottom:1px solid var(--border)}
.type-meta span{display:block;font-size:.75rem;color:var(--text-muted);font-family:var(--font-mono)} .type-sample{min-width:0;overflow-wrap:anywhere}
.sp-row{display:grid;grid-template-columns:90px 60px 1fr;align-items:center;gap:var(--space-3);margin-bottom:var(--space-2);font-family:var(--font-mono);font-size:.8125rem}
.sp-bar{height:16px;background:var(--primary);border-radius:2px;max-width:100%}
.shape-row{display:flex;flex-wrap:wrap;gap:var(--space-5);margin-bottom:var(--space-4)} .shape-item{display:flex;flex-direction:column;gap:4px;font-size:.8125rem;align-items:flex-start}
.shape-box{width:88px;height:64px;background:var(--surface-alt);border:2px solid var(--primary)} .shape-box.elev{border:1px solid var(--border);background:var(--surface)}
.mo-row{display:grid;grid-template-columns:70px 70px 1fr;gap:var(--space-3);align-items:center;margin:var(--space-3) 0}
.mo-track{height:8px;background:var(--surface-alt);border-radius:var(--radius-full);position:relative}
.mo-dot{position:absolute;top:-4px;left:0;width:16px;height:16px;border-radius:50%;background:var(--primary-strong);transition:left var(--d) var(--ease-standard)}
.mo-demo.run .mo-dot{left:calc(100% - 16px)}
.codeblock{position:relative;margin-bottom:var(--space-3)} .codeblock .copy-btn{position:absolute;top:var(--space-2);right:var(--space-2);z-index:2}
.codeblock pre{margin:0;background:var(--surface);border:1px solid var(--border);border-radius:var(--radius-lg);padding:var(--space-4);padding-top:var(--space-6);overflow:auto;max-height:420px;color:var(--text)}
.scr{display:flex;flex-direction:column;gap:var(--space-3)} .scr-head{display:flex;justify-content:space-between;align-items:center;gap:var(--space-3);flex-wrap:wrap}
.kanban{display:grid;grid-template-columns:repeat(3,1fr);gap:var(--space-3)} .kcol{background:var(--surface-alt);border-radius:var(--radius-lg);padding:var(--space-3);display:flex;flex-direction:column;gap:var(--space-2);min-width:0}
.kcol-h{display:flex;justify-content:space-between;align-items:center} .kcard{padding:var(--space-3)} .kcard p{margin:0;font-size:.8125rem}
.post{background:var(--bg);color:var(--text);aspect-ratio:4/5;max-width:420px;border-radius:var(--radius-xl);padding:var(--space-6);display:flex;flex-direction:column;justify-content:center;gap:var(--space-3);border:1px solid var(--border);position:relative}
.post-tag{position:absolute;top:var(--space-4);left:var(--space-6);font:600 .6875rem/1 var(--font-sans);letter-spacing:.06em;color:var(--text-muted)}
.post-big{font-size:2.25rem;font-weight:800;line-height:1.1;margin:0} .post-sub{color:var(--link)}
.post-foot{display:flex;align-items:center;gap:var(--space-2);margin-top:var(--space-5);font-weight:600}
.toast{position:fixed;left:50%;bottom:var(--space-5);transform:translateX(-50%);background:var(--text);color:var(--bg);padding:var(--space-2) var(--space-4);border-radius:var(--radius-full);font-weight:600;opacity:0;pointer-events:none;transition:opacity var(--dur-base) var(--ease-standard);z-index:60}
.toast.show{opacity:1}
.sr{position:absolute;width:1px;height:1px;overflow:hidden;clip:rect(0 0 0 0)}
@media (max-width:900px){
  .side{transform:translateX(-100%)} .side.open{transform:none} .main{margin-left:0} .btn.menu-btn{display:inline-flex}
  .pair,.grid2,.grid3,.kanban{grid-template-columns:1fr} .type-row{grid-template-columns:1fr;gap:var(--space-2)} .hero h1{font-size:2.25rem}
  .topbar{padding:var(--space-2) var(--space-3);flex-wrap:wrap} .wrap{padding:0 var(--space-4) var(--space-8)}
}
@media (max-width:900px),(pointer:coarse){.btn-sm{min-height:44px}}
@media (max-width:560px){ .btn-label-long{display:none} .post-big{font-size:1.75rem} .sp-row{grid-template-columns:70px 50px 1fr} }
@media (prefers-reduced-motion:reduce){*{transition-duration:.01ms!important;animation-duration:.01ms!important;scroll-behavior:auto!important}}
@media print{
  html[data-theme="dark"]{ %%LIGHTVARS%% }
  @page{size:A4;margin:14mm}
  .side,.topbar,.toast,.copy-btn,.btn.menu-btn{display:none!important} .main{margin:0}
  body{background:#fff;color:#000} .wrap{max-width:none;padding:0}
  .panel,.card,.swatch,.table-wrap,.codeblock,.type-row,.post{break-inside:avoid;-webkit-print-color-adjust:exact;print-color-adjust:exact}
  .panel,.swatch .chip,.topnav,.alert-card,.tag,.btn,.sp-bar{-webkit-print-color-adjust:exact;print-color-adjust:exact}
  section{break-before:auto} h2,h3{break-after:avoid}
  .codeblock pre{max-height:none;overflow:visible;white-space:pre-wrap}
}
"""

JS = r"""
(function(){
  var root=document.documentElement, btn=document.getElementById('theme-btn'), toast=document.getElementById('toast');
  function setTheme(t){root.setAttribute('data-theme',t);btn.setAttribute('aria-pressed',t==='dark');btn.setAttribute('aria-label',t==='dark'?'Mudar para tema claro':'Mudar para tema escuro');try{localStorage.setItem('wai-ds-theme',t)}catch(e){}}
  var saved=null;try{saved=localStorage.getItem('wai-ds-theme')}catch(e){}
  var initial=saved||((window.matchMedia&&matchMedia('(prefers-color-scheme: dark)').matches)?'dark':'light');
  setTheme(initial);
  btn.addEventListener('click',function(){setTheme(root.getAttribute('data-theme')==='dark'?'light':'dark')});
  var tt;function say(m){toast.textContent=m;toast.classList.add('show');clearTimeout(tt);tt=setTimeout(function(){toast.classList.remove('show')},1400)}
  function copyText(text){
    if(navigator.clipboard&&navigator.clipboard.writeText){return navigator.clipboard.writeText(text).then(function(){return true},function(){return legacy(text)})}
    return Promise.resolve(legacy(text));
  }
  function legacy(text){try{var ta=document.createElement('textarea');ta.value=text;ta.setAttribute('readonly','');ta.style.position='fixed';ta.style.opacity='0';document.body.appendChild(ta);ta.select();var ok=document.execCommand('copy');document.body.removeChild(ta);return ok}catch(e){return false}}
  window.__lastCopied=null;
  document.addEventListener('click',function(e){
    var s=e.target.closest('[data-copy]');
    if(s){var v=s.getAttribute('data-copy');window.__lastCopied=v;copyText(v).then(function(ok){say(ok?'Copiado: '+v:'Não foi possível copiar')});return}
    var c=e.target.closest('.copy-btn');
    if(c){var el=document.getElementById(c.getAttribute('data-target'));var t=el.textContent;window.__lastCopied=t;copyText(t).then(function(ok){say(ok?'Código copiado':'Não foi possível copiar')})}
  });
  document.getElementById('dl-btn').addEventListener('click',function(){
    var text=document.getElementById('design-md').textContent;
    var blob=new Blob([text],{type:'text/markdown;charset=utf-8'});var url=URL.createObjectURL(blob);
    var a=document.createElement('a');a.href=url;a.download='DESIGN.md';document.body.appendChild(a);a.click();document.body.removeChild(a);setTimeout(function(){URL.revokeObjectURL(url)},1000);say('DESIGN.md baixado');
  });
  document.getElementById('print-btn').addEventListener('click',function(){window.print()});
  var side=document.getElementById('side');
  document.getElementById('menu-btn').addEventListener('click',function(){side.classList.toggle('open')});
  side.addEventListener('click',function(e){if(e.target.tagName==='A')side.classList.remove('open')});
  var pm=document.getElementById('play-motion'),md=document.getElementById('mo-demo');
  if(pm)pm.addEventListener('click',function(){md.classList.remove('run');void md.offsetWidth;md.classList.add('run');setTimeout(function(){md.classList.remove('run')},900)});
  document.querySelectorAll('.tabs').forEach(function(g){g.addEventListener('click',function(e){var t=e.target.closest('.tab');if(!t)return;g.querySelectorAll('.tab').forEach(function(x){x.classList.remove('active');x.setAttribute('aria-selected','false')});t.classList.add('active');t.setAttribute('aria-selected','true')})});
  var links=[].slice.call(side.querySelectorAll('a'));
  if('IntersectionObserver' in window){var io=new IntersectionObserver(function(es){es.forEach(function(en){if(en.isIntersecting){links.forEach(function(l){l.classList.toggle('on',l.getAttribute('href')==='#'+en.target.id)})}})},{rootMargin:'-20% 0px -70% 0px'});document.querySelectorAll('section[id]').forEach(function(s){io.observe(s)})}
})();
"""

def build_html():
    tokens_css = CSS_EXPORT
    lightvars = " ".join("--%s:%s;" % (k, v) for k, v in L.items()) + " " + " ".join("--shadow-%s:%s;" % (k, v) for k, v in T["elevation"]["light"].items())
    css = CSS.replace("%%TOKENS%%", tokens_css).replace("%%LIGHTVARS%%", lightvars)
    page = ('<!doctype html>\n<html lang="pt-BR" data-theme="light">\n<head>\n<meta charset="utf-8">\n<meta name="viewport" content="width=device-width, initial-scale=1">\n'
            '<title>Design System WaiMonitor</title>\n<meta name="description" content="%s">\n<style>%s</style>\n</head>\n<body>\n'
            '<nav class="side" id="side" aria-label="Seções"><img src="%s" alt="WAI Monitor" />%s<div class="ver">Design system v1 - %s</div></nav>\n'
            '<div class="main">\n<header class="topbar"><button class="btn btn-secondary btn-sm menu-btn" id="menu-btn" type="button" aria-label="Abrir menu">Menu</button><span class="ttl">Design system</span><span class="spacer"></span>'
            '<button class="btn btn-secondary btn-sm" id="theme-btn" type="button" aria-pressed="false" aria-label="Mudar para tema escuro"><svg class="ico-sun" width="18" height="18" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" aria-hidden="true"><circle cx="12" cy="12" r="4"/><path d="M12 2v2M12 20v2M4.9 4.9l1.4 1.4M17.7 17.7l1.4 1.4M2 12h2M20 12h2M4.9 19.1l1.4-1.4M17.7 6.3l1.4-1.4"/></svg><svg class="ico-moon" width="18" height="18" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" aria-hidden="true"><path d="M21 12.8A9 9 0 1 1 11.2 3a7 7 0 0 0 9.8 9.8z"/></svg></button>'
            '<button class="btn btn-primary btn-sm" id="dl-btn" type="button">Download DESIGN.md</button><button class="btn btn-secondary btn-sm" id="print-btn" type="button">Print spec sheet</button></header>\n'
            '<main class="wrap"><div class="hero"><h1>WaiMonitor</h1><p class="muted">Design system. Radar de oportunidades para quem vende por indicação.</p></div>\n%s\n</main>\n</div>\n'
            '<div class="toast" id="toast" role="status" aria-live="polite"></div>\n'
            '<script type="text/plain" id="design-md">%s</script>\n<script>%s</script>\n</body>\n</html>\n') % (
        esc(DESCR, quote=True), css, LOGO_WHITE, nav_html(), DATE, sections_html(), DESIGN_MD.replace("</script", "<\\/script"), JS)
    return page

# o icone sol/lua alterna por CSS
EXTRA = "\n.ico-moon{display:none}[data-theme=\"dark\"] #theme-btn .ico-sun{display:none}[data-theme=\"dark\"] #theme-btn .ico-moon{display:inline}\n"

if __name__ == "__main__":
    os.makedirs(OUT, exist_ok=True)
    page = build_html().replace("</style>", EXTRA + "</style>", 1)
    open(OUT + "/index.html", "w", encoding="utf-8").write(page)
    open(OUT + "/DESIGN.md", "w", encoding="utf-8").write(DESIGN_MD)
    open(OUT + "/tokens.json", "w", encoding="utf-8").write(JSON_EXPORT + "\n")
    print("ok", len(page), "bytes html;", len(DESIGN_MD), "bytes md;", len(nunca), "itens em não comunicar")
