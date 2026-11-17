#!/usr/bin/env python3
"""Mine hooks from a CSV: classify into 11 psychological patterns (pt-BR regex),
detect power words, rank by metric. Standard library only.

Usage:
  mine_hooks.py --selftest
  mine_hooks.py file.csv [--top N] [--out hooks.mined.json]

The JSON output is written next to the input CSV unless --out is given.
"""
import argparse
import csv
import json
import re
import sys
import unicodedata
from collections import Counter
from pathlib import Path

HOOK_COLS = ["hook", "titulo", "title", "caption", "texto", "legenda", "headline", "post"]
METRIC_COLS = ["views", "visualizacoes", "metric", "score", "engajamento", "likes", "alcance"]

PATTERNS = {
    "result-proof": r"\b(eu (fiz|bati|faturei|ganhei|consegui)|como (eu )?(faturei|bati|ganhei|consegui)|faturei|bati \d|resultado)\b|r\$ ?\d|\d+ ?(k|mil|mi|milh[oõ]es)\b.*\b(em|de)\b",
    "time-bound": r"\bem \d+ ?(segundos?|minutos?|horas?|dias?|semanas?)\b|\bem (apenas |s[oó] )?\d+ ?(s|min)\b|\b(r[aá]pido|instantane\w*|imediat\w*)\b",
    "contrarian": r"\b(totalmente|completamente) errado\b|\bpare de\b|\bnunca mais\b|\bmito\b|\bvoc[eê] est[aá] (fazendo|usando)\b.*\berrado\b|\bn[aã]o (faça|fa[cç]a|use)\b",
    "secret-gap": r"\b(ningu[eé]m (te )?(conta|fala|diz|sabe|conhece)|quase ningu[eé]m|segredo|escondido|o que (eles|as ag[eê]ncias|os bancos) n[aã]o)\b",
    "listicle": r"^\W*\d+\s+(erros?|dicas?|passos?|ferramentas?|motivos?|raz[oõ]es|formas?|maneiras?|coisas?|sinais|hacks?|[a-zà-ú]+)\b",
    "how-to": r"^\W*(como|aprenda a|passo a passo)\b|\bcomo (fazer|criar|ganhar|faturar|usar|montar)\b",
    "warning-fear": r"\b(cuidado|alerta|aten[cç][aã]o|perigo|nunca (abra|clique|fa[cç]a|use)|risco|golpe|armadilha|destruindo)\b",
    "newsjack": r"\b(acabou de (sair|lan[cç]ar)|acabou de ser|novo recurso|nova atualiza[cç][aã]o|lan[cç]ou|urgente|[uú]ltima hora)\b",
    "comparison": r"\bvs\.?\b|\bversus\b|\bou\b.*\bqual\b|\bqual (o )?melhor\b|\bdiferen[cç]a (entre|real)\b",
    "question": r"\?|^\W*(por ?que|porque|voc[eê] sabia|ser[aá] que|ser que)\b",
    "curiosity-tease": r"\b(olha o que|veja o que|at[eé] o final|o que aconteceu|voc[eê] n[aã]o vai acreditar|acredite|no final)\b",
}

POWER_WORDS = [
    "grátis", "gratuito", "segredo", "escondido", "comprovado", "imediato", "instantâneo",
    "realmente", "literalmente", "ninguém", "todos", "loucura", "absurdo", "ilegal", "hack",
    "definitivo", "brutal", "exato", "pare", "nunca", "sempre", "pior", "melhor", "quebrado",
    "morto", "destruindo", "gênio", "estúpido", "bizarro", "injusto", "estranho", "proibido",
    "chocante", "verdade", "mentira", "erro", "mais rápido", "mais fácil", "único",
]


def norm(s):
    """Lowercase and strip accents (for header matching)."""
    s = unicodedata.normalize("NFKD", s.strip().lower())
    return "".join(c for c in s if not unicodedata.combining(c))


COMPILED = {k: re.compile(v, re.IGNORECASE) for k, v in PATTERNS.items()}
POWER_RE = {
    w: re.compile(r"(?<!\w)" + re.escape(w) + r"(s|es)?(?!\w)", re.IGNORECASE) for w in POWER_WORDS
}


def parse_number(raw):
    """Parse '100k', '1.5M', '50 mil', 'R$ 50.000', '1.234', '1,5k' into a float. None if not numeric."""
    if raw is None:
        return None
    s = str(raw).strip().lower().replace("r$", "").strip()
    if not s or s in ("na", "n/a", "none", "null", "-"):
        return None
    mult = 1
    m = re.search(r"(milh[oõ]es|milhao|mi|mil|k|m|b)\s*$", s)
    if m:
        suffix = m.group(1)
        mult = {"k": 1e3, "mil": 1e3, "m": 1e6, "mi": 1e6, "milhao": 1e6, "milhões": 1e6, "milhoes": 1e6, "b": 1e9}[suffix]
        s = s[: m.start()].strip()
    s = re.sub(r"[^\d.,]", "", s)
    if not s:
        return None
    if mult == 1:
        # no suffix: dots/commas as thousands separators when they group 3 digits
        if re.fullmatch(r"\d{1,3}([.,]\d{3})+", s):
            s = re.sub(r"[.,]", "", s)
        else:
            s = s.replace(",", ".")
    else:
        s = s.replace(",", ".")
        if s.count(".") > 1:
            s = s.replace(".", "")
    try:
        return float(s) * mult
    except ValueError:
        return None


def classify(text):
    patterns = [k for k, rx in COMPILED.items() if rx.search(text)]
    power = [w for w, rx in POWER_RE.items() if rx.search(text)]
    return patterns, power


def find_col(header, candidates):
    by_norm = {norm(h): h for h in header}
    for c in candidates:
        if norm(c) in by_norm:
            return by_norm[norm(c)]
    return None


def read_rows(path):
    with open(path, newline="", encoding="utf-8-sig") as f:
        sample = f.read(4096)
        f.seek(0)
        try:
            dialect = csv.Sniffer().sniff(sample, delimiters=",;\t")
        except csv.Error:
            dialect = csv.excel
        reader = csv.DictReader(f, dialect=dialect)
        header = reader.fieldnames or []
        hook_col = find_col(header, HOOK_COLS)
        metric_col = find_col(header, METRIC_COLS)
        if not hook_col:
            raise SystemExit(
                f"Coluna de gancho não encontrada. Esperado uma de: {', '.join(HOOK_COLS)}. Cabeçalho: {header}"
            )
        rows = []
        for r in reader:
            text = (r.get(hook_col) or "").strip()
            if not text:
                continue
            rows.append({"hook": text, "metric": parse_number(r.get(metric_col)) if metric_col else None})
        return rows, hook_col, metric_col


def mine(rows):
    out = []
    for r in rows:
        patterns, power = classify(r["hook"])
        out.append({**r, "patterns": patterns, "power_words": power})
    out.sort(key=lambda x: (x["metric"] is None, -(x["metric"] or 0)))
    return out


def summarize(mined):
    pc = Counter(p for m in mined for p in m["patterns"])
    wc = Counter(w for m in mined for w in m["power_words"])
    none = sum(1 for m in mined if not m["patterns"])
    return pc, wc, none


def print_summary(mined, top):
    total = len(mined)
    pc, wc, none = summarize(mined)
    print(f"Ganchos analisados: {total}")
    print("\nPadrões (frequência):")
    for p, n in pc.most_common():
        print(f"  {p:<16} {n:>4}  {'#' * min(n, 40)}")
    if none:
        print(f"  {'(sem padrão)':<16} {none:>4}")
    if wc:
        print("\nPower words:", ", ".join(f"{w} ({n})" for w, n in wc.most_common(10)))
    print(f"\nTop {min(top, total) if top else total} por métrica:")
    for m in mined[: top or total]:
        metric = "-" if m["metric"] is None else f"{m['metric']:,.0f}"
        print(f"  [{metric:>12}] {m['hook'][:90]}  <{', '.join(m['patterns']) or 'sem padrão'}>")


def selftest():
    nums = {"100k": 100000, "1.5M": 1500000, "50 mil": 50000, "R$ 50.000": 50000, "1.234": 1234, "1,5k": 1500, "abc": None, "": None}
    for raw, exp in nums.items():
        got = parse_number(raw)
        assert got == exp, f"parse_number({raw!r}) = {got}, esperado {exp}"
    cases = {
        "Eu bati 100k views em 7 dias usando essa automação": "result-proof",
        "Como auditar um contrato de PR em 45 segundos": "time-bound",
        "Pare de mandar áudio no WhatsApp do seu suporte": "contrarian",
        "O que ninguém te conta sobre o mercado de PR": "secret-gap",
        "3 erros fatais que destroem a segurança da sua empresa": "listicle",
        "Como faturar R$ 50 mil com contratos de assessoria": "how-to",
        "Alerta: nunca abra esse tipo de link no WhatsApp": "warning-fear",
        "Acabou de lançar a nova IA de transcrição": "newsjack",
        "WhatsApp Web vs API Oficial: qual a diferença real?": "comparison",
        "Por que seu cliente não responde mais suas mensagens?": "question",
        "Olha o que aconteceu quando ativei essa função": "curiosity-tease",
    }
    assert set(cases.values()) == set(PATTERNS), "selftest deve cobrir os 11 padrões"
    for text, expected in cases.items():
        patterns, _ = classify(text)
        assert expected in patterns, f"{expected!r} não detectado em {text!r}: {patterns}"
    _, power = classify("O segredo é nunca ignorar esse erro")
    assert {"segredo", "nunca", "erro"} <= set(power), power
    print("selftest ok: parse numérico, 11 padrões e power words")


def main():
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("csv", nargs="?", help="arquivo CSV com ganchos e métricas")
    ap.add_argument("--top", type=int, default=0, help="mostrar só os N melhores por métrica")
    ap.add_argument("--out", help="caminho do JSON (padrão: hooks.mined.json ao lado do CSV)")
    ap.add_argument("--selftest", action="store_true", help="valida parsing e regex")
    a = ap.parse_args()
    if a.selftest:
        selftest()
        return 0
    if not a.csv:
        ap.error("informe o CSV ou use --selftest")
    path = Path(a.csv)
    if not path.is_file():
        print(f"Arquivo não encontrado: {path}", file=sys.stderr)
        return 1
    rows, hook_col, metric_col = read_rows(path)
    mined = mine(rows)
    selected = mined[: a.top] if a.top else mined
    out = Path(a.out) if a.out else path.with_name("hooks.mined.json")
    out.write_text(json.dumps(selected, ensure_ascii=False, indent=2), encoding="utf-8")
    print(f"Colunas: gancho={hook_col!r} métrica={metric_col!r}")
    print_summary(mined, a.top)
    print(f"\nJSON salvo em: {out}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
