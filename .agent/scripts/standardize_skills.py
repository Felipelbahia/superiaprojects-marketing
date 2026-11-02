#!/usr/bin/env python3
"""
standardize_skills.py - Padronização canônica de frontmatter para skills do Super IA Projects.

Regras de Autoria e Licença:
1. Todas as skills possuem `license: MIT`.
2. As 9 skills criadas do zero por Felipe Bahia recebem:
   `author: Felipe Bahia (Futuro Mercado)`.
3. As skills de terceiros puras de código (Vercel, Black Forest Labs) mantêm autoria original intacta.
4. Todas as skills de Marketing e Growth que foram adaptadas, traduzidas e enriquecidas
   recebem a coautoria: `[Autor Original] & Felipe Bahia (Futuro Mercado)`.
"""

import re
from pathlib import Path

FELIPE_SOLO = {
    'brand-builder',
    'brand-visual-direction',
    'geral-anti-slop',
    'geral-arquitetura-de-projeto',
    'pr-assessoria-de-imprensa',
    'revenue-lancamento',
    'revenue-sexy-canvas',
    'social-carrossel',
    'social-direcao-de-arte-ia',
}

PURE_VENDORS = {
    'audiovisual-imagem-flux-api',
    'audiovisual-imagem-flux-prompts',
    'site-diretrizes-web-codigo',
    'site-react-composicao',
    'site-react-desempenho',
}

ROOT = Path.cwd()
SKILLS_DIR = ROOT / ".agent" / "skills"


def process_skill(skill_dir: Path):
    skill_file = skill_dir / "SKILL.md"
    if not skill_file.exists():
        return False
    
    content = skill_file.read_text(encoding="utf-8")
    m = re.match(r"^---\n(.*?)\n---\n(.*)$", content, re.DOTALL)
    if not m:
        print(f"⚠️  Sem frontmatter válido: {skill_dir.name}")
        return False

    fm_raw = m.group(1)
    body = m.group(2)

    # Extrair campos
    name_m = re.search(r"^name:\s*(.+)$", fm_raw, re.M)
    name = name_m.group(1).strip() if name_m else skill_dir.name

    desc_m = re.search(r"^description:\s*(.*?)(?=\n[A-Za-z_-]+:|\Z)", fm_raw, re.M | re.S)
    desc = desc_m.group(1).strip() if desc_m else ""

    author_m = re.search(r"author:\s*(.+)$", fm_raw, re.M)
    existing_author = author_m.group(1).strip().strip("\"'") if author_m else "Antigravity Multi-IA Hub"

    vertical_m = re.search(r"vertical:\s*(.+)$", fm_raw, re.M)
    vertical = vertical_m.group(1).strip().strip("\"'") if vertical_m else None

    complements_m = re.search(r"^complements:\s*(.+)$", fm_raw, re.M)
    complements = complements_m.group(1).strip() if complements_m else None

    # Lógica de autoria e coautoria
    if skill_dir.name in PURE_VENDORS:
        final_author = existing_author
    elif skill_dir.name in FELIPE_SOLO:
        final_author = "Felipe Bahia (Futuro Mercado)"
    else:
        clean_author = re.sub(r"\s*&\s*Felipe Bahia.*", "", existing_author).strip()
        final_author = f"{clean_author} & Felipe Bahia (Futuro Mercado)"

    new_fm_lines = [
        "---",
        f"name: {name}",
        f"description: {desc}",
        "license: MIT",
        "metadata:",
        f"  author: {final_author}",
        "  version: 1.0.0",
    ]
    if vertical:
        new_fm_lines.append(f"  vertical: {vertical}")
    if complements:
        new_fm_lines.append(f"complements: {complements}")
    new_fm_lines.append("---\n")

    new_content = "\n".join(new_fm_lines) + body
    skill_file.write_text(new_content, encoding="utf-8")
    return True


def main():
    skills = sorted([p for p in SKILLS_DIR.iterdir() if p.is_dir() and p.name != "_arquivo"])
    count = 0
    for s in skills:
        if process_skill(s):
            count += 1
    print(f"✅ Padronizadas {count} skills com atribuição e coautoria de edição!")


if __name__ == "__main__":
    main()
