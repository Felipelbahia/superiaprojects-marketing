#!/usr/bin/env python3
"""
standardize_skills.py - Padronização canônica de frontmatter e governança de vendor para skills do 0 Mkt.

Padrão Aplicado:
---
# Source: <url-upstream> (quando aplicável)
# Repository: https://github.com/Felipelbahia/superiaprojects-marketing
# Status: <Vanilla de Terceiros | Customizada / Modificada localmente por Felipe Bahia | Nativa do Projeto>
name: <nome-da-skill>
description: <descrição>
author: <autor>
license: MIT
metadata:
  author: <autor>
  version: 1.0.0
  vertical: <vertical se houver>
complements: <complements se houver>
---
"""

import os
import re
import subprocess
from pathlib import Path

FELIPE_SOLO = {
    'brand-builder',
    'brand-visual-direction',
    'geral-anti-slop',
    'pr-assessoria-de-imprensa',
    'revenue-lancamento',
    'revenue-sexy-canvas',
    'social-carrossel',
    'social-direcao-de-arte-ia',
}

PURE_VENDORS = {
    'audiovisual-imagem-flux-api': {
        'source': 'https://github.com/fal-ai',
        'status': 'Vanilla de Terceiros',
        'author': 'Black Forest Labs & Fal.ai',
    },
    'audiovisual-imagem-flux-prompts': {
        'source': 'https://github.com/fal-ai',
        'status': 'Customizada / Modificada localmente por Felipe Bahia',
        'author': 'Black Forest Labs / Modificado por Felipe Bahia (Futuro Mercado)',
    },
    'site-diretrizes-web-codigo': {
        'source': 'https://github.com/vercel',
        'status': 'Vanilla de Terceiros',
        'author': 'Vercel Engineering',
    },
    'site-react-composicao': {
        'source': 'https://github.com/vercel',
        'status': 'Vanilla de Terceiros',
        'author': 'Vercel Engineering',
    },
    'site-react-desempenho': {
        'source': 'https://github.com/vercel',
        'status': 'Vanilla de Terceiros',
        'author': 'Vercel Engineering',
    },
}

ROOT = Path.cwd()
SKILLS_DIR = ROOT / ".agent" / "skills"


def get_repo_url() -> str:
    try:
        res = subprocess.run(
            ['git', 'config', '--get', 'remote.origin.url'],
            capture_output=True,
            text=True,
            check=True
        )
        url = res.stdout.strip()
        if url.endswith('.git'):
            url = url[:-4]
        return url
    except Exception:
        return "https://github.com/Felipelbahia/superiaprojects-marketing"


def determine_source(skill_name: str, existing_author: str) -> str:
    if skill_name in PURE_VENDORS:
        return PURE_VENDORS[skill_name]['source']
    
    author_lower = existing_author.lower()
    if 'clawfu' in author_lower or 'aaron-he-zhu' in author_lower:
        return 'https://github.com/clawdb'
    elif 'hormozi' in author_lower:
        return 'https://acquisition.com/books/100m-offers'
    elif 'conrado' in author_lower or 'benson' in author_lower:
        return 'https://8ps.com'
    elif 'claude' in author_lower:
        return 'https://github.com/anthropics/anthropic-quickstarts'
    else:
        return 'https://github.com/Felipelbahia/superiaprojects-marketing'


def process_skill(skill_dir: Path, repo_url: str):
    skill_file = skill_dir / "SKILL.md"
    if not skill_file.exists():
        return False

    content = skill_file.read_text(encoding="utf-8")
    m = re.match(r"^---\s*\n(.*?)\n---\s*\n(.*)$", content, re.DOTALL)
    if not m:
        print(f"⚠️  Sem frontmatter delimitado por ---: {skill_dir.name}")
        return False

    fm_raw = m.group(1)
    body = m.group(2)

    # Extrair name e description
    name_m = re.search(r"^name:\s*(.+)$", fm_raw, re.M)
    name = name_m.group(1).strip() if name_m else skill_dir.name

    desc_m = re.search(r"^description:\s*(.*?)(?=\n[A-Za-z0-9_-]+:|\Z)", fm_raw, re.M | re.S)
    desc = desc_m.group(1).strip() if desc_m else ""

    # Extrair author existente
    author_m = re.search(r"author:\s*(.+)$", fm_raw, re.M)
    existing_author = author_m.group(1).strip().strip("\"'") if author_m else "Antigravity Multi-IA Hub"

    # Extrair campos opcionais
    vertical_m = re.search(r"vertical:\s*(.+)$", fm_raw, re.M)
    vertical = vertical_m.group(1).strip().strip("\"'") if vertical_m else None

    complements_m = re.search(r"^complements:\s*(.+)$", fm_raw, re.M)
    complements = complements_m.group(1).strip() if complements_m else None

    # Determinar status, source e author final
    if skill_dir.name in FELIPE_SOLO:
        status = "Nativa do Projeto"
        source = None
        final_author = "Felipe Bahia (Futuro Mercado)"
    elif skill_dir.name in PURE_VENDORS:
        vendor_info = PURE_VENDORS[skill_dir.name]
        status = vendor_info['status']
        source = vendor_info['source']
        final_author = vendor_info['author']
    else:
        status = "Customizada / Modificada localmente por Felipe Bahia"
        source = determine_source(skill_dir.name, existing_author)
        clean_author = re.sub(r"\s*&\s*Felipe Bahia.*", "", existing_author).strip()
        final_author = f"{clean_author} & Felipe Bahia (Futuro Mercado)"

    # Construir novas linhas de frontmatter
    new_fm_lines = ["---"]
    if source and source != repo_url:
        new_fm_lines.append(f"# Source: {source}")
    new_fm_lines.append(f"# Repository: {repo_url}")
    new_fm_lines.append(f"# Status: {status}")
    new_fm_lines.append(f"name: {name}")
    new_fm_lines.append(f"description: {desc}")
    new_fm_lines.append(f"author: {final_author}")
    new_fm_lines.append("license: MIT")
    new_fm_lines.append("metadata:")
    new_fm_lines.append(f"  author: {final_author}")
    new_fm_lines.append("  version: 1.0.0")
    if vertical:
        new_fm_lines.append(f"  vertical: {vertical}")
    if complements:
        new_fm_lines.append(f"complements: {complements}")
    new_fm_lines.append("---\n")

    new_content = "\n".join(new_fm_lines) + body
    skill_file.write_text(new_content, encoding="utf-8")
    return True


def main():
    repo_url = get_repo_url()
    print(f"🔍 Repositório detectado: {repo_url}")
    
    if not SKILLS_DIR.exists():
        print(f"❌ Diretório {SKILLS_DIR} não encontrado.")
        return

    skills = sorted([p for p in SKILLS_DIR.iterdir() if p.is_dir() and p.name != "_arquivo"])
    count = 0
    for s in skills:
        if process_skill(s, repo_url):
            count += 1
            
    print(f"✅ Sucesso: {count} skills padronizadas com governança de vendor e metadados canônicos!")


if __name__ == "__main__":
    main()
