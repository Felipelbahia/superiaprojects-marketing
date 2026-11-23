#!/usr/bin/env python3
"""build_sip_index.py - Regenerates the item tables (skills, agents, workflows) inside a SIP hub resolver.

Usage (from the hub root, or pass --hub):
    python3 .agents/scripts/build_sip_index.py [--hub <dir>] [--resolver <nome>] [--check]

    --hub <dir>        hub root (default: current directory)
    --resolver <nome>  resolver folder whose SKILL.md holds the tables: `prompts/resolver/<nome>` (new layout) or
                       `.agents/skills/<nome>` (legacy). Default: the only real sip-* folder; error when zero or several
    --check            write nothing; exit 1 when a table is stale

Regions live in the resolver's SKILL.md, one per kind:
    <!-- skills:start (gerado por .agents/scripts/build_sip_index.py — não edite à mão) -->
    ...generated text...
    <!-- skills:end -->
The start line is kept as written. Options go in it as key=value; `group=prefix` groups the items
by the part of the name before the first "-". Kinds: skills, agents, workflows.

Two-level mode (small resolver): instead of the three regions, one region
    <!-- indice:start dir=verticais (gerado por build_sip_index.py — não edite à mão) -->
    <!-- indice:end -->
holds a summary table (one row per vertical) and the generator writes one file per vertical to
`<resolver>/<dir>/<vertical>.md` with that vertical's skills, agents and workflows. The verticals come from
`<resolver>/verticais.json`:
    {"padrao": "outros",                      # optional: vertical for names no rule matches
     "verticais": [{"nome": "copy", "quando": "one line: when to open it", "match": ["copy-*"]}, ...]}
The first vertical whose `match` (fnmatch on the item name) fits wins. An item that fits none and no `padrao` is an error.

Items: .agents/skills/<name>/SKILL.md, .agents/agents/<name>.md, .agents/workflows/<name>.md (top level only).
Excluded: sip-*, names starting with "_" or ".", README.md, and symlinks that resolve outside the hub.

Exit codes: 0 up to date or rewritten, 1 stale under --check, 2 usage, marker or resolver error.
Standard library only (no PyYAML): reads plain, quoted and block (|, >, >-) descriptions.
"""

import fnmatch
import json
import os
import re
import sys
from pathlib import Path
from typing import Dict, List, NamedTuple, Optional, Tuple

sys.path.insert(0, str(__import__('pathlib').Path(__file__).resolve().parent))
import linkutil  # noqa: E402

KINDS = ("skills", "agents", "workflows")
HEADERS = {"skills": "Skill", "agents": "Agent", "workflows": "Workflow"}
ALLOWED_OPTIONS = {"group": {"prefix"}}
USAGE = "Uso: build_sip_index.py [--hub <dir>] [--resolver <nome>] [--check]"

START_RE = re.compile(r"^<!--\s*(skills|agents|workflows):start\b(.*?)-->\s*$")
END_RE = re.compile(r"^<!--\s*(skills|agents|workflows):end\s*-->\s*$")
OPTION_RE = re.compile(r"(\w+)=(\S+)")
INDEX_START_RE = re.compile(r"^<!--\s*indice:start\b(.*?)-->\s*$")
INDEX_END_RE = re.compile(r"^<!--\s*indice:end\s*-->\s*$")
GENERATED_MARK = "Gerado por build_sip_index.py"
TITLES = {"skills": "Skills", "agents": "Agents", "workflows": "Workflows"}
# Text from "NÃO use" / "Do NOT use" on is the "do not use" part; the table keeps only the trigger part.
NEGATIVE_CUT = re.compile(r"(?:^|\s+)(?:N[ÃA]O use|Do NOT use)\b", re.IGNORECASE)


class UsageError(Exception):
    """A usage, marker or resolver problem: reported on stderr, exit 2."""


class Options(NamedTuple):
    hub: Optional[str]
    resolver: Optional[str]
    check: bool


# ---------- YAML scalar reader (port of Astro's readScalar in lib/frontmatter.mjs) ----------

def read_scalar(fm: str, key: str) -> Optional[str]:
    lines = fm.split("\n")
    key_re = re.escape(key)
    idx = next((i for i, line in enumerate(lines) if re.match(rf"{key_re}\s*:", line)), None)
    if idx is None:
        return None
    rest = re.sub(rf"^{key_re}\s*:\s*", "", lines[idx]).rstrip()
    block = re.match(r"^([>|])([+-]?)\s*$", rest)
    if block:
        body = []
        for line in lines[idx + 1:]:
            if line.strip() == "":
                body.append("")
                continue
            if not line[:1].isspace():
                break
            body.append(line.strip())
        while body and body[-1] == "":
            body.pop()
        text = "\n".join(body) if block.group(1) == "|" else re.sub(r"\s+", " ", " ".join(body))
        return text.strip()
    if rest.startswith('"'):
        m = re.match(r'"((?:[^"\\]|\\.)*)"', rest)
        if not m:
            return None
        return re.sub(r'\\(["\\nt/])', lambda c: {"n": "\n", "t": "\t"}.get(c.group(1), c.group(1)), m.group(1))
    if rest.startswith("'"):
        m = re.match(r"'((?:[^']|'')*)'", rest)
        return m.group(1).replace("''", "'") if m else None
    return re.sub(r"\s+#.*$", "", rest)


def read_frontmatter(path: Path) -> str:
    """Text between the first two '---' lines of the file, or '' when there is no frontmatter."""
    lines = path.read_text(encoding="utf-8").splitlines()
    if not lines or lines[0].rstrip() != "---":
        return ""
    for i in range(1, len(lines)):
        if lines[i].rstrip() == "---":
            return "\n".join(lines[1:i])
    return ""


def parse_description(fm: str) -> str:
    return (read_scalar(fm, "description") or "").strip()


def clean_description(desc: str) -> str:
    desc = desc.replace("&gt;", ">").replace("&lt;", "<").replace("&amp;", "&")
    cut = NEGATIVE_CUT.search(desc)
    if cut:
        desc = desc[:cut.start()]
    desc = re.sub(r"\s+", " ", desc).strip().replace("|", "\\|")
    return desc or "(sem description)"


# ---------- items ----------

def is_listed(name: str) -> bool:
    return not name.startswith(("sip-", "_", "."))


def is_inside(path: Path, hub_real: str) -> bool:
    real = os.path.realpath(path)
    return real == hub_real or real.startswith(hub_real + os.sep)


def list_items(hub: Path, kind: str) -> List[Tuple[str, str]]:
    """(name, cleaned description) for every item of this kind, sorted by name."""
    base = hub / linkutil.adir(hub) / kind
    if not base.is_dir():
        return []
    hub_real = os.path.realpath(hub)
    if kind == "skills":
        entries = [p for p in base.iterdir() if p.is_dir()]
    else:
        entries = [p for p in base.glob("*.md") if p.is_file() and p.name != "README.md"]
    items = []
    for entry in entries:
        name = entry.name if kind == "skills" else entry.stem
        source = entry / "SKILL.md" if kind == "skills" else entry
        if not is_listed(name) or not source.is_file() or not is_inside(source, hub_real):
            continue
        items.append((name, clean_description(parse_description(read_frontmatter(source)))))
    return sorted(items)


# ---------- rendering ----------

def render_body(kind: str, items: List[Tuple[str, str]], group: Optional[str]) -> List[str]:
    """Lines between the start marker and the end marker (both excluded)."""
    if not items:
        return ["", "Nenhum por enquanto.", ""]

    def cell(name: str) -> str:
        return f"`/{name}`" if kind == "workflows" else f"`{name}`"

    header = f"| {HEADERS[kind]} | Use quando |"
    rows = [f"| {cell(name)} | {desc} |" for name, desc in items]
    out = ["", f"Total: {len(items)}.", ""]
    if group == "prefix":
        by_prefix: Dict[str, List[str]] = {}
        for (name, _), row in zip(items, rows):
            by_prefix.setdefault(name.split("-", 1)[0], []).append(row)
        for prefix in sorted(by_prefix):
            out += [f"### {prefix}", "", header, "| --- | --- |", *by_prefix[prefix], ""]
    else:
        out += [header, "| --- | --- |", *rows, ""]
    return out


# ---------- resolver regions ----------

def parse_options(kind: str, text: str) -> Dict[str, str]:
    options = {}
    for key, value in OPTION_RE.findall(text):
        if key not in ALLOWED_OPTIONS:
            raise UsageError(f"opção desconhecida em {kind}:start: {key}")
        if value not in ALLOWED_OPTIONS[key]:
            raise UsageError(f"valor inválido em {kind}:start: {key}={value}")
        options[key] = value
    return options


def find_regions(lines: List[str]) -> Dict[str, Tuple[int, int, Dict[str, str]]]:
    """kind -> (index of start line, index of its end line, options)."""
    starts: Dict[str, Tuple[int, Dict[str, str]]] = {}
    ends: Dict[str, List[int]] = {}
    for i, line in enumerate(lines):
        start = START_RE.match(line)
        if start:
            kind = start.group(1)
            if kind in starts:
                raise UsageError(f"marcador duplicado: {kind}:start")
            starts[kind] = (i, parse_options(kind, start.group(2)))
            continue
        end = END_RE.match(line)
        if end:
            ends.setdefault(end.group(1), []).append(i)
    regions = {}
    for kind, (start_idx, options) in starts.items():
        after = [e for e in ends.get(kind, []) if e > start_idx]
        if not after:
            raise UsageError(f"falta o marcador <!-- {kind}:end --> depois de {kind}:start")
        regions[kind] = (start_idx, after[0], options)
    return regions


def resolver_dir(hub: Path, name: str) -> Path:
    """`<hub>/prompts/resolver/<name>` (new layout) when it exists, else `<hub>/.agents/skills/<name>` (legacy).

    Same rule as linkutil.resolver_dir; kept here so this generator stays a single file with no imports of its own.
    """
    new = hub / "prompts" / "resolver" / name
    return new if new.is_dir() else hub / linkutil.adir(hub) / "skills" / name


def default_resolver(hub: Path) -> str:
    new_base = hub / "prompts" / "resolver"
    base = new_base if new_base.is_dir() else hub / linkutil.adir(hub) / "skills"
    found = sorted(p.name for p in base.glob("sip-*") if p.is_dir() and not p.is_symlink()) if base.is_dir() else []
    if len(found) != 1:
        raise UsageError(f"preciso de exatamente uma pasta sip-* real em {base} (achei {len(found)}); use --resolver <nome>")
    return found[0]


# ---------- two-level mode (verticais) ----------

def find_index_region(lines: List[str]) -> Optional[Tuple[int, int, str]]:
    """(start index, end index, dir) of the `indice` region, or None when the resolver does not use it."""
    start = None
    folder = "verticais"
    for i, line in enumerate(lines):
        m = INDEX_START_RE.match(line)
        if m:
            if start is not None:
                raise UsageError("marcador duplicado: indice:start")
            start = i
            for key, value in OPTION_RE.findall(m.group(1)):
                if key != "dir":
                    raise UsageError(f"opção desconhecida em indice:start: {key}")
                if not re.fullmatch(r"[A-Za-z0-9_-]+", value):
                    raise UsageError(f"valor inválido em indice:start: dir={value}")
                folder = value
            continue
        if start is not None and INDEX_END_RE.match(line):
            return start, i, folder
    if start is not None:
        raise UsageError("falta o marcador <!-- indice:end --> depois de indice:start")
    return None


def load_verticais(resolver_path: Path) -> Tuple[List[dict], Optional[str]]:
    """The verticals of a resolver from its verticais.json, validated."""
    path = resolver_path / "verticais.json"
    if not path.is_file():
        raise UsageError(f"falta {path} (obrigatório quando o resolver usa <!-- indice:start -->)")
    try:
        data = json.loads(path.read_text(encoding="utf-8"))
    except json.JSONDecodeError as err:
        raise UsageError(f"{path} não é JSON válido: {err}")
    verticais = data.get("verticais") if isinstance(data, dict) else None
    if not isinstance(verticais, list) or not verticais:
        raise UsageError(f"{path}: 'verticais' precisa ser uma lista não vazia")
    padrao = data.get("padrao")
    names = set()
    for v in verticais:
        nome = v.get("nome") if isinstance(v, dict) else None
        if not isinstance(nome, str) or not re.fullmatch(r"[a-z0-9][a-z0-9-]*", nome):
            raise UsageError(f"{path}: 'nome' inválido (use a-z, 0-9 e hífen): {nome!r}")
        if nome in names:
            raise UsageError(f"{path}: vertical repetida: {nome}")
        names.add(nome)
        if not str(v.get("quando", "")).strip():
            raise UsageError(f"{path}: a vertical '{nome}' precisa de 'quando' (uma frase de quando abrir)")
        match = v.get("match", [])
        if not isinstance(match, list) or not all(isinstance(m, str) for m in match):
            raise UsageError(f"{path}: 'match' de '{nome}' precisa ser uma lista de padrões")
        if not match and nome != padrao:
            raise UsageError(f"{path}: a vertical '{nome}' não tem 'match' e não é a 'padrao'")
    if padrao is not None and padrao not in names:
        raise UsageError(f"{path}: 'padrao' aponta para uma vertical que não existe: {padrao}")
    return verticais, padrao


def assign(verticais: List[dict], padrao: Optional[str],
           all_items: Dict[str, List[Tuple[str, str]]]) -> Dict[str, Dict[str, List[Tuple[str, str]]]]:
    """vertical name -> kind -> items. First matching vertical wins; the rest goes to `padrao`."""
    out: Dict[str, Dict[str, List[Tuple[str, str]]]] = {v["nome"]: {} for v in verticais}
    lost: List[str] = []
    for kind in KINDS:
        for name, desc in all_items[kind]:
            home = next((v["nome"] for v in verticais if any(fnmatch.fnmatchcase(name, pat) for pat in v.get("match", []))), padrao)
            if home is None:
                lost.append(f"{kind[:-1]} {name}")
                continue
            out[home].setdefault(kind, []).append((name, desc))
    if lost:
        raise UsageError(f"{len(lost)} item(ns) sem vertical (acrescente um 'match' ou uma 'padrao' em verticais.json): "
                         + ", ".join(lost[:10]) + ("…" if len(lost) > 10 else ""))
    return out


def table_lines(kind: str, items: List[Tuple[str, str]]) -> List[str]:
    cell = (lambda n: f"`/{n}`") if kind == "workflows" else (lambda n: f"`{n}`")
    return [f"| {HEADERS[kind]} | Use quando |", "| --- | --- |", *[f"| {cell(n)} | {d} |" for n, d in items]]


def render_vertical(v: dict, by_kind: Dict[str, List[Tuple[str, str]]]) -> str:
    lines = [f"# {v['nome']}", "", str(v["quando"]).strip(), "",
             f"> {GENERATED_MARK}. Não edite à mão. Skill: `\"<HUB>/.agents/skills/<nome>/SKILL.md\"`; "
             f"agent: `\"<HUB>/.agents/agents/<nome>.md\"`; workflow: `\"<HUB>/.agents/workflows/<nome>.md\"`.", ""]
    for kind in KINDS:
        items = by_kind.get(kind, [])
        if items:
            lines += [f"## {TITLES[kind]} ({len(items)})", "", *table_lines(kind, items), ""]
    return "\n".join(lines)


def render_index(verticais: List[dict], grouped: Dict[str, Dict[str, List[Tuple[str, str]]]], folder: str) -> List[str]:
    """Lines of the summary table inside the `indice` region (markers excluded)."""
    used = [v for v in verticais if any(grouped[v["nome"]].get(k) for k in KINDS)]
    totals = {k: sum(len(grouped[v["nome"]].get(k, [])) for v in used) for k in KINDS}
    out = ["", f"Total: {totals['skills']} skills, {totals['agents']} agents, {totals['workflows']} workflows.", "",
           "| Vertical | Use quando | Skills | Agents | Workflows | Arquivo |", "| --- | --- | --- | --- | --- | --- |"]
    for v in used:
        g = grouped[v["nome"]]
        out.append(f"| `{v['nome']}` | {str(v['quando']).strip()} | {len(g.get('skills', []))} | {len(g.get('agents', []))} "
                   f"| {len(g.get('workflows', []))} | `{folder}/{v['nome']}.md` |")
    return out + [""]


def vertical_files(verticais: List[dict], grouped: Dict[str, Dict[str, List[Tuple[str, str]]]]) -> Dict[str, str]:
    """file name -> text, only for verticals that have at least one item."""
    return {f"{v['nome']}.md": render_vertical(v, grouped[v["nome"]]) + "\n"
            for v in verticais if any(grouped[v["nome"]].get(k) for k in KINDS)}


# ---------- CLI ----------

def parse_cli(argv: List[str]) -> Options:
    hub: Optional[str] = None
    resolver: Optional[str] = None
    check = False
    i = 0
    while i < len(argv):
        arg = argv[i]
        if arg == "--check":
            check = True
        elif arg in ("--hub", "--resolver"):
            if i + 1 >= len(argv) or argv[i + 1].startswith("--"):
                raise UsageError(f"faltou o valor de {arg}")
            i += 1
            if arg == "--hub":
                hub = argv[i]
            else:
                resolver = argv[i]
        else:
            raise UsageError(f"argumento desconhecido: {arg}")
        i += 1
    return Options(hub, resolver, check)


def run(argv: List[str]) -> int:
    opts = parse_cli(argv)
    hub = Path(opts.hub) if opts.hub is not None else Path.cwd()
    if opts.resolver is not None and ("/" in opts.resolver or opts.resolver in ("", ".", "..")):
        raise UsageError(f"nome de resolver inválido: {opts.resolver!r}")
    resolver = opts.resolver if opts.resolver is not None else default_resolver(hub)
    skill_md = resolver_dir(hub, resolver) / "SKILL.md"
    if not skill_md.is_file():
        raise UsageError(f"resolver não encontrado: {skill_md}")

    raw = skill_md.read_bytes().decode("utf-8")
    eol = "\r" if "\r\n" in raw else ""
    lines = raw.split("\n")
    regions = find_regions(lines)
    index_region = find_index_region(lines)

    listed = {kind: list_items(hub, kind) for kind in KINDS}
    plan = []  # (start, end, kind, body) in KINDS order, plus the index region
    for kind in KINDS:
        items = listed[kind]
        if kind not in regions:
            if items and index_region is None:
                raise UsageError(f"marcadores ausentes para {kind} em {skill_md}: acrescente "
                                 f"<!-- {kind}:start --> e <!-- {kind}:end -->")
            continue
        start, end, options = regions[kind]
        plan.append((start, end, kind, [line + eol for line in render_body(kind, items, options.get("group"))]))

    files: Dict[str, str] = {}
    index_dir: Optional[Path] = None
    if index_region is not None:
        i_start, i_end, folder = index_region
        verticais, padrao = load_verticais(skill_md.parent)
        grouped = assign(verticais, padrao, listed)
        plan.append((i_start, i_end, "indice", [line + eol for line in render_index(verticais, grouped, folder)]))
        files = vertical_files(verticais, grouped)
        index_dir = skill_md.parent / folder

    changed = [kind for start, end, kind, body in plan
               if [line.rstrip("\r") for line in lines[start + 1:end]] != [line.rstrip("\r") for line in body]]
    stale: List[str] = []
    if index_dir is not None:
        existing = {p.name: p for p in index_dir.glob("*.md")} if index_dir.is_dir() else {}
        changed += [f"{index_dir.name}/{n}" for n, text in files.items()
                    if n not in existing or existing[n].read_text(encoding="utf-8") != text]
        stale = [n for n, p in existing.items() if n not in files and GENERATED_MARK in p.read_text(encoding="utf-8")]
        changed += [f"{index_dir.name}/{n} (sobrou)" for n in stale]
    if not changed:
        print("Sem mudanças.")
        return 0
    if opts.check:
        print(f"Tabelas desatualizadas: {', '.join(changed)} — rode build_sip_index.py", file=sys.stderr)
        return 1

    new_lines = list(lines)
    for start, end, kind, body in sorted(plan, reverse=True):
        new_lines[start + 1:end] = body
    skill_md.write_bytes("\n".join(new_lines).encode("utf-8"))
    if index_dir is not None:
        index_dir.mkdir(parents=True, exist_ok=True)
        for n, text in files.items():
            (index_dir / n).write_text(text, encoding="utf-8")
        for n in stale:
            (index_dir / n).unlink()
    print(f"Regiões atualizadas em {skill_md.relative_to(hub).as_posix()}: {', '.join(changed)}")
    return 0


def main(argv: Optional[List[str]] = None) -> int:
    args = sys.argv[1:] if argv is None else argv
    if any(a in ("-h", "--help") for a in args):
        print(__doc__)
        return 0
    try:
        return run(args)
    except UsageError as err:
        print(f"Erro: {err}", file=sys.stderr)
        print(USAGE, file=sys.stderr)
        return 2
    except (OSError, UnicodeDecodeError) as err:
        print(f"Erro ao ler ou gravar: {err}", file=sys.stderr)
        return 2


if __name__ == "__main__":
    sys.exit(main())
