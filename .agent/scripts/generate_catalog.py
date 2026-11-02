#!/usr/bin/env python3
"""
generate_catalog.py - Gerador do Catálogo Unificado e Distribuído Multi-Base.

Princípios Arquiteturais:
1. TAXONOMIA SOBERANA POR PROJETO:
   - 0 Mkt: Utiliza suas 17 categorias canônicas oficiais (brand, copy, seo, ads, social, etc.)
   - 0 Padrões: Utiliza categorias técnicas de Engenharia e VibeCoding (Frontend, Backend, DevOps, etc.)
   - Projetos Locais: Prioriza category e subcategory declaradas no frontmatter do projeto
2. GAVETA MODAL INTERATIVA NO HTML:
   - Permite clicar em qualquer skill para abrir suas instruções (SKILL.md) e lista de arquivos de referências/scripts
3. CARREGAMENTO DINÂMICO MULTI-BASE:
   - Carrega via <script src="..."> os dados de cada base (0 Padrões, 0 Mkt e Projeto Local)
4. SANITIZAÇÃO DE ERROS DE SCRIPT:
   - Escapa rigorosamente </script> e tags HTML para nunca quebrar o parser do navegador
"""

import os
import re
import sys
import json
import urllib.request
import urllib.parse
from pathlib import Path
from collections import defaultdict
from concurrent.futures import ThreadPoolExecutor

CWD = Path.cwd().resolve()
GLOBAL_PADROES_DIR = Path(os.environ.get("SUPER_IA_PROJECTS_PATH", "/Users/macbookpro/Documents/IA Projects/_Plataforma/0 Padrões"))
GLOBAL_MKT_DIR = Path(os.environ.get("MARKETING_HUB_PATH", str(CWD)))

SCRIPTS_DIR = Path(__file__).resolve().parent
CACHE_FILE = SCRIPTS_DIR / "translations_cache.json"

# Categorias Oficiais de Marketing (17 categorias canônicas)
MKT_CATEGORIES_INFO = {
    "brand": ("Identidade da Marca", "Essência, público, voz, visual, naming e som"),
    "conteudo": ("Produção de Conteúdo", "Planejamento, pesquisa e criação de conteúdo"),
    "copy": ("Copywriting & Conversão", "Persuasão, landing pages, hooks, VSL e métodos clássicos"),
    "social": ("Mídias Sociais", "LinkedIn, carrossel, YouTube, arte e estratégias orgânicas"),
    "pr": ("Relações Públicas (PR)", "Assessoria de imprensa e reputação corporativa"),
    "seo": ("SEO & Mecanismos de Busca", "Busca orgânica, GEO, Google, ASO e podcasts"),
    "ads": ("Tráfego Pago (Ads)", "Google Ads, Meta Ads, TikTok Ads e criativos de alta conversão"),
    "email": ("Email Marketing", "Automação, newsletters, copy de email e entregabilidade"),
    "vendas": ("Vendas B2B & Prospecção", "Funil comercial, CRM, cold email e materiais de venda"),
    "site": ("Sites & Páginas de Conversão", "Arquitetura, UI, CRO, Tailwind e front-end moderno"),
    "data": ("Inteligência de Dados", "Métricas, atribuição, GA4, coortes e funis de conversão"),
    "growth": ("Growth Hacking", "Frameworks de escala, testes A/B, retenção, churn e indicação"),
    "revenue": ("Estratégia de Receita (Revenue)", "Oferta, precificação, campanhas, lançamentos e modelos mentais"),
    "persona": ("Clientes & Persona", "Pesquisa com clientes, ICP e descoberta de mercado"),
    "produto": ("Gestão de Produto", "Especificação (PRD) e frameworks ágeis para produto"),
    "audiovisual": ("Mídia & Audiovisual", "Áudio, vídeo, apresentações e recursos multimídia"),
    "geral": ("Geral & Governança", "Auditoria anti-slop, conformidade LGPD e utilitários"),
}

# Categorias Técnicas de Engenharia (12 áreas de engenharia)
PADROES_CATEGORIES = [
    "Processos de VibeCoding & Metodologia IA",
    "Gestão de Produtos e Projetos",
    "Frontend & UI/UX",
    "Backend & APIs",
    "Database & Storage",
    "Mobile Development",
    "DevOps & Cloud Infra",
    "AI, Data & ML",
    "Workflows & Automação",
    "Testing & Quality Assurance",
    "Segurança & Compliance",
    "Arquitetura de Software & Engenharia",
]

ESSENTIAL_RESOURCES = [
    ("execution-loop", "Skill", "Super IA Projects", "Ciclo Espec → Plan → Execução → QA (nota 0-10) → Debug para builds e mudanças significativas."),
    ("skill-resolver", "Skill", "Super IA Projects", "Procedimento inteligente de busca e resolução de skills no ecossistema."),
    ("spec-writing", "Skill", "Super IA Projects", "Criação de especificação escrita estruturada antes do início do planejamento ou código."),
    ("session-handoff", "Skill", "Super IA Projects", "Documentação do trabalho da sessão para continuidade fluida em sessões futuras."),
    ("writing-skills", "Skill", "Super IA Projects", "Criação e edição de qualquer skill aplicando TDD a documentação e symlinks."),
    ("clean-code", "Skill", "Super IA Projects", "Diretrizes obrigatórias de código limpo, sem over-engineering e com testes."),
    ("project-initializer", "Skill", "Super IA Projects", "Fluxo de 5 fases para inicialização de projetos do zero com paridade dual."),
    ("project-defines", "Skill", "Super IA Projects", "Governança documental de projetos governados por pasta _projectdefines/."),
]

def load_cache() -> dict:
    if CACHE_FILE.exists():
        try:
            return json.loads(CACHE_FILE.read_text(encoding="utf-8"))
        except Exception:
            return {}
    return {}

def save_cache(cache: dict):
    SCRIPTS_DIR.mkdir(parents=True, exist_ok=True)
    CACHE_FILE.write_text(json.dumps(cache, ensure_ascii=False, indent=2), encoding="utf-8")

def is_portuguese(text: str) -> bool:
    pt_words = {"para", "com", "não", "quando", "este", "esta", "usar", "use", "crie", "como", "está", "estão", "desenvolvimento", "equipe", "recursos", "especialista", "análise", "relatórios", "geração", "estratégia", "padrões", "criação", "produção"}
    lower_words = set(re.findall(r"\b\w+\b", text.lower()))
    return len(lower_words.intersection(pt_words)) >= 2

def translate_to_pt(text: str) -> str:
    if not text or len(text.strip()) == 0:
        return ""
    if is_portuguese(text):
        return text.strip()
    try:
        url = "https://translate.googleapis.com/translate_a/single?client=gtx&sl=en&tl=pt&dt=t&q=" + urllib.parse.quote(text)
        req = urllib.request.Request(url, headers={"User-Agent": "Mozilla/5.0"})
        with urllib.request.urlopen(req, timeout=10) as res:
            data = json.loads(res.read().decode("utf-8"))
            translated = "".join([part[0] for part in data[0] if part[0]])
            return translated.strip()
    except Exception:
        return text

def parse_frontmatter(path: Path) -> dict:
    try:
        text = path.read_text(encoding="utf-8", errors="ignore")
    except Exception:
        return {}
    m = re.match(r"---\n(.*?)\n---", text, re.S)
    if not m:
        return {"_raw": text}
    
    fm_text = m.group(1)
    meta = {}
    
    for line in re.findall(r"^([A-Za-z_-]+):\s*(.*)$", fm_text, re.M):
        k, v = line
        meta[k.strip()] = v.strip().strip("\"'")
        
    m_desc = re.search(r"^description:\s*(?:>\|?|\|)?\s*\n?([^\n]+(?:\n\s+[^\n]+)*)", fm_text, re.M)
    if m_desc and (not meta.get("description") or len(meta.get("description", "")) < 20):
        cleaned_desc = re.sub(r"\s+", " ", m_desc.group(1).strip()).strip("\"'")
        meta["description"] = cleaned_desc
        
    meta["_raw"] = text[m.end():].strip()
    return meta

def extract_description(meta: dict, fallback_name: str) -> str:
    desc = meta.get("description", "")
    if not desc or desc.lower() == fallback_name.lower():
        raw = meta.get("_raw", "")
        lines = [l.strip() for l in raw.split("\n") if l.strip() and not l.strip().startswith("---")]
        for l in lines:
            if not l.startswith("#") and len(l) > 15:
                desc = l.strip(">* -")
                break
            elif l.startswith("#") and not desc:
                desc = l.strip("# ")
    if not desc:
        desc = f"Recurso especializado {fallback_name} para desenvolvimento e automação."
    desc = re.sub(r"\s+", " ", desc).strip()
    return desc

# --- Classificadores Soberanos por Base ---

def classify_0_mkt(name: str, desc: str, kind: str) -> tuple[str, str]:
    """Classifica rigorosamente dentro das 17 categorias canônicas de 0 Mkt."""
    clean_name = name.lower().lstrip("/@")
    
    # 1. Padrão por prefixo explícito em 0 Mkt (<categoria>-<assunto>)
    for cat in MKT_CATEGORIES_INFO.keys():
        if clean_name.startswith(f"{cat}-") or clean_name == cat:
            sub = clean_name.replace(f"{cat}-", "").replace("-", " ").title()
            cat_label = f"{cat} ({MKT_CATEGORIES_INFO[cat][0]})"
            return cat_label, sub if sub else "Fundamentos"

    # 2. Heurística para workflows e agentes de 0 Mkt sem prefixo
    text = f"{name} {desc}".lower()
    if any(k in text for k in ["brand", "posicionamento", "branding"]):
        return f"brand ({MKT_CATEGORIES_INFO['brand'][0]})", "Identidade e Marca"
    if any(k in text for k in ["copy", "vsl", "persuasao", "headline", "hook"]):
        return f"copy ({MKT_CATEGORIES_INFO['copy'][0]})", "Textos e Conversão"
    if any(k in text for k in ["seo", "geo", "palavras-chave", "ranking", "backlink"]):
        return f"seo ({MKT_CATEGORIES_INFO['seo'][0]})", "Otimização para Busca"
    if any(k in text for k in ["ads", "anuncio", "google ads", "meta ads", "criativo"]):
        return f"ads ({MKT_CATEGORIES_INFO['ads'][0]})", "Mídia Paga"
    if any(k in text for k in ["social", "linkedin", "carrossel", "instagram", "youtube"]):
        return f"social ({MKT_CATEGORIES_INFO['social'][0]})", "Redes Sociais"
    if any(k in text for k in ["email", "newsletter", "fluxo"]):
        return f"email ({MKT_CATEGORIES_INFO['email'][0]})", "Fluxos e Automação"
    if any(k in text for k in ["vendas", "prospeccao", "comercial", "pipeline"]):
        return f"vendas ({MKT_CATEGORIES_INFO['vendas'][0]})", "Estratégia Comercial"
    if any(k in text for k in ["growth", "experimento", "a/b", "churn", "retencao"]):
        return f"growth ({MKT_CATEGORIES_INFO['growth'][0]})", "Experimentos e Retenção"
    if any(k in text for k in ["revenue", "preco", "lancamento", "oferta"]):
        return f"revenue ({MKT_CATEGORIES_INFO['revenue'][0]})", "Estratégia de Receita"
    if any(k in text for k in ["persona", "icp", "entrevista"]):
        return f"persona ({MKT_CATEGORIES_INFO['persona'][0]})", "Descoberta de Clientes"
    if any(k in text for k in ["video", "audio", "remotion", "apresentacao"]):
        return f"audiovisual ({MKT_CATEGORIES_INFO['audiovisual'][0]})", "Recursos Multimídia"
    if any(k in text for k in ["data", "ga4", "metricas"]):
        return f"data ({MKT_CATEGORIES_INFO['data'][0]})", "Métricas e Atribuição"

    return f"geral ({MKT_CATEGORIES_INFO['geral'][0]})", "Operações e Rotinas"


def classify_0_padroes(name: str, desc: str, kind: str) -> tuple[str, str]:
    """Classifica rigorosamente dentro das categorias técnicas de 0 Padrões."""
    text = f"{name} {desc}".lower()

    # 1. Processos de VibeCoding & Metodologia IA
    if any(k in name.lower() for k in [
        "execution-loop", "spec-writing", "session-handoff", "writing-skills", "clean-code",
        "skill-resolver", "project-initializer", "project-defines", "brainstorm", "context-save",
        "context-restore", "context-driven", "vibecoding", "subagent-driven", "parallel-agents",
        "dispatching-parallel", "behavioral-modes", "using-superpowers", "diagnosing-superpowers",
        "smart-debug", "smart-fix", "error-analysis", "error-trace", "anti-slop"
    ]):
        if "skill-resolver" in name.lower():
            return "Processos de VibeCoding & Metodologia IA", "Resolução e Descoberta de Skills"
        elif any(k in name.lower() for k in ["execution-loop", "session-handoff", "writing-skills", "clean-code", "project-initializer", "project-defines"]):
            return "Processos de VibeCoding & Metodologia IA", "Padrões Fundamentais & Ciclo de Execução"
        elif any(k in name.lower() for k in ["context-save", "context-restore", "context-driven"]):
            return "Processos de VibeCoding & Metodologia IA", "Engenharia de Contexto & Memória"
        elif "brainstorm" in name.lower():
            return "Processos de VibeCoding & Metodologia IA", "Portão Socrático & Descoberta"
        elif any(k in name.lower() for k in ["anti-slop", "vibecoding-security-audit"]):
            return "Processos de VibeCoding & Metodologia IA", "Auditoria Anti-Slop & Segurança VibeCoding"
        else:
            return "Processos de VibeCoding & Metodologia IA", "Orquestração de Agentes & Superpoderes"

    # 2. Gestão de Produtos e Projetos
    if any(k in text for k in [
        "track-management", "new-track", "sprint", "standup-notes", "product-manager", "project-planner",
        "linear", "jira", "roadmap", "backlog", "agile", "scrum", "feature-development",
        "data-driven-feature", "product-strategist", "postmortem-writing", "onboard", "issue"
    ]):
        if any(k in name.lower() for k in ["track-management", "new-track"]):
            return "Gestão de Produtos e Projetos", "Conductor & Gestão de Tracks"
        elif any(k in name.lower() for k in ["feature-development", "data-driven-feature", "product-manager", "product-strategist"]):
            return "Gestão de Produtos e Projetos", "Estratégia & Especificação de Produto (PRD)"
        elif any(k in name.lower() for k in ["standup-notes", "linear", "issue", "onboard"]):
            return "Gestão de Produtos e Projetos", "Operações Ágeis & Coordenação de Equipe"
        else:
            return "Gestão de Produtos e Projetos", "Planejamento de Projetos & Sprints"

    # 3. Frontend & UI/UX
    if any(k in text for k in ["frontend", "ui", "ux", "css", "tailwind", "react", "nextjs", "vue", "astro", "design-system", "component", "a11y", "accessibility", "html"]):
        if any(k in text for k in ["accessibility", "a11y", "screen-reader", "wcag"]):
            return "Frontend & UI/UX", "Acessibilidade Web (A11y & WCAG)"
        elif any(k in text for k in ["tailwind", "design-system", "tokens", "visual-design"]):
            return "Frontend & UI/UX", "Design Systems & Estilização Moderna"
        elif any(k in text for k in ["react", "nextjs", "app-router", "state-management"]):
            return "Frontend & UI/UX", "Frameworks Web Modernos (React & Next.js)"
        else:
            return "Frontend & UI/UX", "Componentes de Interface & Interação"

    # 4. Mobile Development
    if any(k in text for k in ["mobile", "flutter", "dart", "react-native", "ios", "android", "xcode"]):
        if any(k in text for k in ["flutter", "dart"]):
            return "Mobile Development", "Flutter & Dart Ecossistema"
        elif any(k in text for k in ["react-native"]):
            return "Mobile Development", "React Native & Expo"
        elif any(k in text for k in ["ios", "xcode", "swift"]):
            return "Mobile Development", "iOS & Ferramentas Nativas"
        else:
            return "Mobile Development", "Arquitetura e Padrões Mobile"

    # 5. Database & Storage
    if any(k in text for k in ["database", "postgres", "sql", "supabase", "firebase", "firestore", "schema", "migration"]):
        if any(k in text for k in ["supabase", "firebase", "firestore"]):
            return "Database & Storage", "BaaS & Bancos em Nuvem (Supabase / Firebase)"
        elif any(k in text for k in ["migration", "schema"]):
            return "Database & Storage", "Modelagem & Migrações de Banco"
        else:
            return "Database & Storage", "Bancos Relacionais (PostgreSQL & SQL)"

    # 6. Backend & APIs
    if any(k in text for k in ["backend", "api", "rest", "graphql", "node", "python", "golang", "fastapi", "express", "auth", "stripe", "billing"]):
        if any(k in text for k in ["auth", "stripe", "billing", "payment", "pci"]):
            return "Backend & APIs", "Serviços de Autenticação & Pagamentos"
        elif any(k in text for k in ["fastapi", "python"]):
            return "Backend & APIs", "Python & Backends de Alta Performance"
        elif any(k in text for k in ["node", "express", "microservices"]):
            return "Backend & APIs", "Node.js, Go & Microsserviços"
        else:
            return "Backend & APIs", "Design & Integração de APIs (REST / GraphQL)"

    # 7. AI, Data & ML
    if any(k in text for k in ["ai-", "ml-", "rag-", "embedding", "llm", "vector", "langchain", "prompt", "data-storytelling", "spark", "dbt", "data-quality"]):
        if any(k in text for k in ["rag", "embedding", "vector", "similarity"]):
            return "AI, Data & ML", "RAG & Recuperação Vetorial Avançada"
        elif any(k in text for k in ["llm", "prompt", "eval"]):
            return "AI, Data & ML", "Engenharia de Prompts & Avaliação de LLMs"
        elif any(k in text for k in ["dbt", "spark", "pipeline", "data-quality"]):
            return "AI, Data & ML", "Pipelines de Dados & Transformação"
        else:
            return "AI, Data & ML", "Modelos de IA & Machine Learning"

    # 8. DevOps & Cloud Infra
    if any(k in text for k in ["devops", "k8s", "docker", "terraform", "helm", "cloud", "deploy", "monitoring", "prometheus", "grafana", "gitops", "ci", "github-actions"]):
        if any(k in text for k in ["k8s", "helm", "kubernetes"]):
            return "DevOps & Cloud Infra", "Orquestração Kubernetes & Contêineres"
        elif any(k in text for k in ["terraform", "infra", "cloud"]):
            return "DevOps & Cloud Infra", "Infraestrutura como Código (Terraform / Cloud)"
        elif any(k in text for k in ["ci", "github-actions", "gitlab", "deploy"]):
            return "DevOps & Cloud Infra", "Pipelines de CI/CD & Deploy Contínuo"
        else:
            return "DevOps & Cloud Infra", "Monitoramento, Logs & Confiabilidade (SRE)"

    # 9. Testing & Quality Assurance
    if any(k in text for k in ["test", "tdd", "qa", "playwright", "bats", "e2e"]):
        if "tdd" in text:
            return "Testing & Quality Assurance", "Desenvolvimento Orientado a Testes (TDD)"
        elif any(k in text for k in ["playwright", "e2e", "webapp-testing"]):
            return "Testing & Quality Assurance", "Automação de Testes E2E & Web"
        else:
            return "Testing & Quality Assurance", "Testes Unitários & Integração"

    # 10. Segurança & Compliance
    if any(k in text for k in ["security", "vulnerability", "sast", "audit", "compliance", "gdpr", "lgpd", "stride", "threat", "xss", "secret"]):
        if any(k in text for k in ["gdpr", "lgpd", "compliance", "pci"]):
            return "Segurança & Compliance", "Compliance Regulatória & Privacidade"
        elif any(k in text for k in ["threat", "stride", "attack-tree"]):
            return "Segurança & Compliance", "Modelagem de Ameaças & Red Team"
        else:
            return "Segurança & Compliance", "Varredura SAST & Prevenção de Falhas"

    # 11. Workflows & Automação
    if any(k in text for k in ["n8n", "automation", "workflow", "git-", "changelog", "bash"]):
        if "n8n" in text:
            return "Workflows & Automação", "Automações n8n & Integração de Webhooks"
        elif "git" in text:
            return "Workflows & Automação", "Automação Git & Versionamento"
        else:
            return "Workflows & Automação", "Scripts Utilitários & Tarefas Operacionais"

    # 12. Arquitetura de Software & Engenharia
    return "Arquitetura de Software & Engenharia", "Padrões Arquiteturais & Boas Práticas"


def classify_local_resource(name: str, desc: str, kind: str, meta: dict, project_name: str) -> tuple[str, str]:
    """Prioriza metadados explícitos do projeto local antes de qualquer fallback."""
    # 1. Frontmatter explícito
    if meta.get("category"):
        cat = meta.get("category").strip()
        sub = meta.get("subcategory", "Geral").strip()
        return cat, sub

    # 2. Mapeamento por prefixo do próprio projeto (se seguir padrão com hífen)
    clean_name = name.lower().lstrip("/@")
    if "-" in clean_name:
        parts = clean_name.split("-", 1)
        prefix = parts[0].strip().title()
        subject = parts[1].replace("-", " ").title()
        return f"{prefix} (Local)", subject

    return f"Recursos Próprios ({project_name})", "Funcionalidades Locais"


def scan_agent_dir(agent_dir: Path, source_name: str, cache: dict, project_name: str = "") -> list[dict]:
    items = []
    if not agent_dir.is_dir():
        return items

    # 1. Skills
    skills_dir = agent_dir / "skills"
    if skills_dir.is_dir():
        for skill_dir in sorted(skills_dir.iterdir()):
            if skill_dir.is_dir() and (skill_dir / "SKILL.md").exists():
                name = skill_dir.name
                skill_file = skill_dir / "SKILL.md"
                meta = parse_frontmatter(skill_file)
                desc = extract_description(meta, name)
                
                content = meta.get("_raw", "") or ""
                if not content:
                    try:
                        content = skill_file.read_text(encoding="utf-8", errors="ignore")
                    except Exception:
                        content = ""
                        
                text_exts = {".md", ".txt", ".py", ".sh", ".bash", ".js", ".ts", ".json", ".yaml", ".yml", ".html", ".css", ".sql", ".csv", ".toml", ".ini", ".env"}
                other_files = []
                for p in sorted(skill_dir.glob("**/*")):
                    if p.is_file() and p.name != "SKILL.md" and not p.name.startswith("."):
                        try:
                            rel = str(p.relative_to(skill_dir))
                            f_content = ""
                            if p.suffix.lower() in text_exts or (p.stat().st_size < 50_000):
                                try:
                                    f_content = p.read_text(encoding="utf-8", errors="ignore")[:8000]
                                except Exception:
                                    f_content = ""
                            other_files.append({
                                "name": p.name,
                                "rel_path": rel,
                                "abs_path": str(p.resolve()),
                                "content": f_content
                            })
                        except Exception:
                            pass

                items.append({
                    "name": name,
                    "kind": "Skill",
                    "source": source_name,
                    "desc_en": desc,
                    "path": f".agent/skills/{name}/SKILL.md",
                    "abs_path": str(skill_file.resolve()),
                    "content": content[:12000],
                    "files": other_files,
                    "_meta": meta
                })

    # 2. Workflows
    wf_dir = agent_dir / "workflows"
    if wf_dir.is_dir():
        for wf_file in sorted(wf_dir.glob("*.md")):
            name = wf_file.stem
            meta = parse_frontmatter(wf_file)
            desc = extract_description(meta, name)
            content = meta.get("_raw", "") or ""
            if not content:
                try:
                    content = wf_file.read_text(encoding="utf-8", errors="ignore")
                except Exception:
                    content = ""
                    
            items.append({
                "name": f"/{name}",
                "kind": "Workflow",
                "source": source_name,
                "desc_en": desc,
                "path": f".agent/workflows/{wf_file.name}",
                "abs_path": str(wf_file.resolve()),
                "content": content[:12000],
                "files": [],
                "_meta": meta
            })

    # 3. Agents
    agents_dir = agent_dir / "agents"
    if agents_dir.is_dir():
        for ag_file in sorted(agents_dir.glob("*.md")):
            name = ag_file.stem
            meta = parse_frontmatter(ag_file)
            desc = extract_description(meta, name)
            content = meta.get("_raw", "") or ""
            if not content:
                try:
                    content = ag_file.read_text(encoding="utf-8", errors="ignore")
                except Exception:
                    content = ""

            items.append({
                "name": f"@{name}",
                "kind": "Agent",
                "source": source_name,
                "desc_en": desc,
                "path": f".agent/agents/{ag_file.name}",
                "abs_path": str(ag_file.resolve()),
                "content": content[:12000],
                "files": [],
                "_meta": meta
            })

    # Tradução em lote das descrições para PT-BR
    needed_translations = []
    for it in items:
        en = it["desc_en"]
        if en in cache:
            it["desc"] = cache[en]
        elif is_portuguese(en):
            it["desc"] = en
            cache[en] = en
        else:
            needed_translations.append(it)

    if needed_translations:
        def do_trans(item):
            pt = translate_to_pt(item["desc_en"])
            item["desc"] = pt
            cache[item["desc_en"]] = pt

        with ThreadPoolExecutor(max_workers=10) as ex:
            list(ex.map(do_trans, needed_translations))

    # Classificação Soberana de Acordo com a Fonte
    for it in items:
        if source_name == "0 Mkt":
            cat, subcat = classify_0_mkt(it["name"], it.get("desc", it["desc_en"]), it["kind"])
        elif source_name == "0 Padrões":
            cat, subcat = classify_0_padroes(it["name"], it.get("desc", it["desc_en"]), it["kind"])
        else:
            cat, subcat = classify_local_resource(it["name"], it.get("desc", it["desc_en"]), it["kind"], it.get("_meta", {}), project_name or source_name)
        
        it["category"] = cat
        it["subcategory"] = subcat
        if "_meta" in it:
            del it["_meta"]

    return items


def generate_markdown(items: list[dict], title: str, subtitle: str) -> str:
    grouped = defaultdict(lambda: defaultdict(list))
    for it in items:
        grouped[it["category"]][it["subcategory"]].append(it)

    md = []
    md.append(f"# {title}\n")
    md.append(f"> {subtitle}\n")
    
    skills_count = sum(1 for i in items if i["kind"] == "Skill")
    wf_count = sum(1 for i in items if i["kind"] == "Workflow")
    ag_count = sum(1 for i in items if i["kind"] == "Agent")
    
    sources = sorted(list(set(i["source"] for i in items)))
    source_stats = " · ".join([f"`{s}` ({sum(1 for i in items if i['source'] == s)})" for s in sources])
    
    md.append(f"**Total Geral:** `{len(items)}` recursos | **Skills:** `{skills_count}` | **Workflows:** `{wf_count}` | **Agentes:** `{ag_count}`")
    md.append(f"**Fontes Integradas:** {source_stats}\n")
    md.append("---\n")

    # Recursos Essenciais
    md.append("## ⭐ Recursos Fundamentais do Kit (Regra 4b & Metodologia VibeCoding)\n")
    md.append("Estes recursos regem os processos de desenvolvimento, resolução de skills e governança de qualidade:\n")
    md.append("| Recurso | Tipo | Origem | Papel / O que faz | Link Direto |")
    md.append("| :--- | :--- | :--- | :--- | :--- |")
    for name, k, src_default, desc in ESSENTIAL_RESOURCES:
        m = next((i for i in items if i["name"] == name or i["name"] == f"@{name}" or i["name"] == f"/{name}"), None)
        src = m["source"] if m else src_default
        clean_anchor = name.lower().replace('/', '').replace('@', '')
        md.append(f"| **`{name}`** | `{k}` | `{src}` | {desc} | [Acessar](#{clean_anchor}) |")
    md.append("\n---\n")

    # Sumário de Categorias (dinâmico com base nas categorias realmente existentes)
    md.append("## 📌 Sumário de Categorias\n")
    for cat in sorted(grouped.keys()):
        cat_count = sum(len(items_list) for items_list in grouped[cat].values())
        anchor = re.sub(r"[^\w\- ]", "", cat.lower()).replace(" ", "-")
        md.append(f"- [{cat}](#{anchor}) (`{cat_count}` recursos)")
        for subcat in sorted(grouped[cat].keys()):
            sub_count = len(grouped[cat][subcat])
            sub_anchor = re.sub(r"[^\w\- ]", "", subcat.lower()).replace(" ", "-")
            md.append(f"  - [{subcat}](#{sub_anchor}) (`{sub_count}`)")
    md.append("\n---\n")

    # Tabelas por Categoria e Subcategoria
    for cat in sorted(grouped.keys()):
        cat_count = sum(len(items_list) for items_list in grouped[cat].values())
        anchor = re.sub(r"[^\w\- ]", "", cat.lower()).replace(" ", "-")
        md.append(f"## <a id=\"{anchor}\"></a>{cat}\n")
        md.append(f"Total de recursos nesta macro-área: `{cat_count}`\n")

        for subcat in sorted(grouped[cat].keys()):
            sub_items = grouped[cat][subcat]
            sub_anchor = re.sub(r"[^\w\- ]", "", subcat.lower()).replace(" ", "-")
            md.append(f"### <a id=\"{sub_anchor}\"></a>{subcat}\n")
            md.append("| Recurso | Tipo | Origem | Descrição e Aplicação |")
            md.append("| :--- | :--- | :--- | :--- |")
            for it in sorted(sub_items, key=lambda x: (x["kind"] != "Skill", x["name"])):
                clean_anchor = it["name"].replace("/", "").replace("@", "").lower()
                clean_name = it["name"]
                desc_pt = it.get("desc", it["desc_en"]).replace("|", "\\|")
                md.append(f"| <a id=\"{clean_anchor}\"></a>**`{clean_name}`** | `{it['kind']}` | `{it['source']}` | {desc_pt} |")
            md.append("")
        md.append("---\n")

    return "\n".join(md)


def generate_html_dashboard(items: list[dict], title: str, subtitle: str) -> str:
    # Prepare JSON safe payload com escape estrito de tags HTML
    clean_items = []
    for it in items:
        clean_items.append({
            "name": it["name"],
            "kind": it["kind"],
            "source": it["source"],
            "desc": it.get("desc", it["desc_en"]),
            "category": it["category"],
            "subcategory": it["subcategory"],
            "path": it["path"],
            "abs_path": it.get("abs_path", ""),
            "content": it.get("content", ""),
            "files": it.get("files", [])
        })

    raw_json = json.dumps(clean_items, ensure_ascii=False)
    # CRÍTICO: Sanitização anti-quebra de tag de script no HTML
    safe_json = raw_json.replace("</script>", "<\\/script>").replace("<!--", "<\\!--")
    
    html = f"""<!DOCTYPE html>
<html lang="pt-BR">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>{title}</title>
  <link rel="preconnect" href="https://fonts.googleapis.com">
  <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
  <link href="https://fonts.googleapis.com/css2?family=Plus+Jakarta+Sans:wght@300;400;500;600;700;800&family=JetBrains+Mono:wght@400;500;600&display=swap" rel="stylesheet">
  
  <!-- CSS da Aplicação: 1º Mestre Central (Zero-Sync Runtime), 2º Fallback Local -->
  <link rel="stylesheet" href="file:///Users/macbookpro/Documents/IA Projects/_Plataforma/0 Padrões/.agent/catalog-app.css">
  <link rel="stylesheet" href="./catalog-app.css">
</head>
<body>

  <header>
    <div class="header-top">
      <div class="title-group">
        <h1>🚀 {title}</h1>
        <p>{subtitle}</p>
      </div>
      <div class="header-actions">
        <button class="btn" id="themeToggle" title="Alternar Modo Claro/Escuro">🌓 Tema</button>
        <button class="btn" id="viewToggle" title="Alternar Grid / Tabela">📋 Tabela</button>
      </div>
    </div>
    <div class="controls-row">
      <div class="search-box">
        <span class="search-icon">🔍</span>
        <input type="text" id="searchInput" class="search-input" placeholder="Buscar por nome, tag, categoria ou funcionalidade...">
      </div>
      <div class="filters-group">
        <div class="pill active" data-filter="all">Todas as Fontes</div>
        <div class="pill" data-source="local" id="pillLocal" style="display:none;">Projeto Local</div>
        <div class="pill" data-source="padroes">0 Padrões</div>
        <div class="pill" data-source="mkt">0 Mkt</div>
      </div>
      <div class="filters-group" style="border-left:1px solid var(--border); padding-left:0.75rem;">
        <label class="checkbutton active" id="chkSkill">
          <input type="checkbox" value="Skill" checked>
          <span class="chk-box">✓</span>
          <span>Skills</span>
        </label>
        <label class="checkbutton active" id="chkWf">
          <input type="checkbox" value="Workflow" checked>
          <span class="chk-box">✓</span>
          <span>Workflows</span>
        </label>
        <label class="checkbutton active" id="chkAgent">
          <input type="checkbox" value="Agent" checked>
          <span class="chk-box">✓</span>
          <span>Agentes</span>
        </label>
      </div>
      <div style="display:none;">
        <select id="categorySelect" class="select-dropdown">
          <option value="all">Todas as Categorias</option>
        </select>
      </div>
    </div>

    <!-- Barra de Categorias Expansível (Dropdown / Accordion) -->
    <details class="categories-bar" id="categoriesBar">
      <summary class="categories-bar-header">
        <div class="categories-bar-title">
          <span>🏷️ Categorias por Projeto</span>
          <span class="categories-counter" id="selectedCatsCount">Todas selecionadas</span>
          <span class="categories-toggle-hint">(clique para ver/filtrar)</span>
          <span class="collapsible-chevron">▾</span>
        </div>
        <div class="categories-bulk-actions">
          <button type="button" class="btn-cat-bulk" id="btnSelectAllCats" onclick="event.stopPropagation(); selectAllCategories();" title="Selecionar todas as categorias">✓ Selecionar Todas</button>
          <button type="button" class="btn-cat-bulk" id="btnClearAllCats" onclick="event.stopPropagation(); clearAllCategories();" title="Limpar todas as categorias">✕ Limpar Todas</button>
        </div>
      </summary>
      <div class="categories-rows" id="categoriesRows"></div>
    </details>
  </header>

  <main>
    <div class="stats-bar">
      <span id="resultsCount">Carregando recursos...</span>
      <span id="sourcesActiveInfo" style="font-size:0.75rem;"></span>
    </div>
    <div class="grid-view" id="gridView"></div>
    <div class="table-container" id="tableView">
      <table>
        <thead>
          <tr>
            <th>Recurso</th>
            <th>Tipo</th>
            <th>Origem</th>
            <th>Categoria</th>
            <th>Subcategoria</th>
            <th>O que faz</th>
          </tr>
        </thead>
        <tbody id="tableBody"></tbody>
      </table>
    </div>
  </main>

  <!-- Modal Central de Detalhes -->
  <div class="modal-overlay" id="modalOverlay">
    <div class="modal-card" id="itemModal">
      <div class="modal-header">
        <div class="modal-title-group">
          <h2 id="modalTitle">Nome do Recurso</h2>
          <div class="badges" id="modalBadges"></div>
        </div>
        <button class="modal-close" id="modalClose" title="Fechar (Esc)">&times;</button>
      </div>
      <div class="modal-body">
        <div class="modal-meta-grid">
          <div class="meta-item">
            <div class="meta-label">Categoria</div>
            <div class="meta-val" id="modalCategory">Categoria</div>
          </div>
          <div class="meta-item">
            <div class="meta-label">Subcategoria</div>
            <div class="meta-val" id="modalSubcategory">Subcategoria</div>
          </div>
          <div class="meta-item" style="grid-column: 1 / -1;">
            <div class="meta-label">Caminho do Arquivo</div>
            <div class="meta-val" id="modalPath" style="font-family:'JetBrains Mono',monospace; font-size:0.75rem;"></div>
          </div>
        </div>

        <div class="modal-section">
          <h3>📝 Descrição em Português</h3>
          <p id="modalDesc" style="color:var(--text-muted); font-size:0.875rem; line-height:1.5;"></p>
        </div>

        <div class="modal-actions">
          <button class="btn-action" id="btnCopyPath">📋 Copiar Caminho</button>
          <button class="btn-action" id="btnCopyUsage">⚡ Copiar Invocação</button>
        </div>

        <!-- Dropdown / Collapsible: Referências & Scripts -->
        <details class="modal-collapsible" id="modalFilesDetails" open>
          <summary class="collapsible-header">
            <span class="collapsible-title">📂 Referências & Scripts na Skill (<span id="filesCount">0</span>)</span>
            <span class="collapsible-chevron">▾</span>
          </summary>
          <div class="collapsible-body">
            <ul class="files-list" id="modalFilesList"></ul>
          </div>
        </details>

        <!-- Dropdown / Collapsible: Conteúdo da Skill -->
        <details class="modal-collapsible" id="modalContentDetails" open>
          <summary class="collapsible-header">
            <span class="collapsible-title">📄 Conteúdo / Instruções (<span id="modalContentLabel">SKILL.md</span>)</span>
            <span class="collapsible-chevron">▾</span>
          </summary>
          <div class="collapsible-body">
            <div class="content-box" id="modalContent"></div>
          </div>
        </details>
      </div>
    </div>
  </div>

  <!-- Fallback de Dados Embutidos Sanitizados -->
  <script>
    window.EMBEDDED_CATALOG_DATA = {safe_json};
  </script>

  <!-- Dynamic Loader Scripts (Tentam carregar dados ao vivo das 3 bases) -->
  <script src="file:///Users/macbookpro/Documents/IA Projects/_Plataforma/0 Padrões/.agent/catalog-data.js"></script>
  <script src="file:///Users/macbookpro/Documents/IA Projects/_Plataforma/0 Mkt/.agent/catalog-data.js"></script>
  <script src="./catalog-data.js"></script>

  <!-- JS da Aplicação: 1º Mestre Central (Zero-Sync Runtime), 2º Fallback Local -->
  <script src="file:///Users/macbookpro/Documents/IA Projects/_Plataforma/0 Padrões/.agent/catalog-app.js"></script>
  <script src="./catalog-app.js"></script>
</body>
</html>
"""
    return html


def build_for_target(target_dir: Path, source_name: str, cache: dict, is_primary_global: bool = False):
    agent_dir = target_dir / ".agent"
    if not agent_dir.is_dir():
        print(f"Aviso: Diretório {agent_dir} não encontrado.")
        return

    project_name = target_dir.name
    print(f"\n--- Processando {source_name} em {target_dir} ---")
    local_items = scan_agent_dir(agent_dir, source_name, cache, project_name=project_name)
    print(f"Encontrados {len(local_items)} recursos próprios em {source_name}")

    # Salva catalog-data.js exclusivo desta base
    data_js_path = agent_dir / "catalog-data.js"
    var_name = "CATALOG_PADROES" if "Projects" in source_name or "Padrões" in source_name else ("CATALOG_MKT" if "Marketing" in source_name or "Mkt" in source_name else "CATALOG_LOCAL")
    
    js_payload = {
        "source": source_name,
        "total": len(local_items),
        "items": local_items
    }
    
    raw_js = json.dumps(js_payload, ensure_ascii=False, indent=2)
    safe_js = raw_js.replace("</script>", "<\\/script>").replace("<!--", "<\\!--")
    js_content = f"window.{var_name} = {safe_js};\n"
    data_js_path.write_text(js_content, encoding="utf-8")
    print(f"✅ Gerado catalog-data.js: {data_js_path.relative_to(target_dir)} ({len(local_items)} itens)")

    # Se for uma das bases globais, gera o catálogo consolidado
    combined_items = list(local_items)
    
    if "Projects" in source_name or "Padrões" in source_name:
        if (GLOBAL_MKT_DIR / ".agent").is_dir():
            mkt_items = scan_agent_dir(GLOBAL_MKT_DIR / ".agent", "Super IA Marketing", cache, project_name="Super IA Marketing")
            combined_items.extend(mkt_items)
            title = "Super IA Projects — Catálogo Geral Unificado da Plataforma"
            subtitle = "Índice central de todas as Skills, Workflows e Agentes da Plataforma (Engenharia + Marketing)"
    elif "Marketing" in source_name or "Mkt" in source_name:
        if (GLOBAL_PADROES_DIR / ".agent").is_dir():
            padroes_items = scan_agent_dir(GLOBAL_PADROES_DIR / ".agent", "Super IA Projects", cache, project_name="Super IA Projects")
            combined_items.extend(padroes_items)
            title = "Super IA Projects - Marketing — Catálogo Integrado de Marketing, Growth e Vendas"
            subtitle = "Catálogo completo de Marketing integrado à base global de Engenharia Super IA Projects"
    else:
        if (GLOBAL_PADROES_DIR / ".agent").is_dir():
            padroes_items = scan_agent_dir(GLOBAL_PADROES_DIR / ".agent", "Super IA Projects", cache, project_name="Super IA Projects")
            combined_items.extend(padroes_items)
        if (GLOBAL_MKT_DIR / ".agent").is_dir():
            mkt_items = scan_agent_dir(GLOBAL_MKT_DIR / ".agent", "Super IA Marketing", cache, project_name="Super IA Marketing")
            combined_items.extend(mkt_items)
        title = f"{target_dir.name} — Catálogo Geral de Skills & Recursos"
        subtitle = f"Catálogo local de {target_dir.name} integrado ao ecossistema Super IA Projects"

    # Gera CATALOG.md
    md_content = generate_markdown(combined_items, title, subtitle)
    md_path = agent_dir / "CATALOG.md"
    md_path.write_text(md_content, encoding="utf-8")
    print(f"✅ Gerado CATALOG.md: {md_path.relative_to(target_dir)} ({len(combined_items)} recursos)")

    # Garante fallback local de catalog-app.css e catalog-app.js no projeto alvo
    central_css = GLOBAL_PADROES_DIR / ".agent" / "catalog-app.css"
    central_js = GLOBAL_PADROES_DIR / ".agent" / "catalog-app.js"
    target_css = agent_dir / "catalog-app.css"
    target_js = agent_dir / "catalog-app.js"

    if central_css.is_file() and target_css.resolve() != central_css.resolve():
        target_css.write_text(central_css.read_text(encoding="utf-8"), encoding="utf-8")
        print(f"✅ Sincronizado fallback local: {target_css.relative_to(target_dir)}")

    if central_js.is_file() and target_js.resolve() != central_js.resolve():
        target_js.write_text(central_js.read_text(encoding="utf-8"), encoding="utf-8")
        print(f"✅ Sincronizado fallback local: {target_js.relative_to(target_dir)}")

    # Gera catalog.html
    html_content = generate_html_dashboard(combined_items, title, subtitle)
    html_path = agent_dir / "catalog.html"
    html_path.write_text(html_content, encoding="utf-8")
    print(f"✅ Gerado catalog.html: {html_path.relative_to(target_dir)} ({len(html_content)} bytes)")


def main():
    cache = load_cache()
    
    if CWD == GLOBAL_PADROES_DIR or "--all" in sys.argv:
        build_for_target(GLOBAL_PADROES_DIR, "Super IA Projects", cache, is_primary_global=True)
        if GLOBAL_MKT_DIR.exists():
            build_for_target(GLOBAL_MKT_DIR, "Super IA Marketing", cache, is_primary_global=True)
            idx = GLOBAL_MKT_DIR / ".agent" / "INDEX.md"
            if idx.exists():
                cat_ref = "# Índice de Skills, Workflows e Agentes (Redirecionamento)\n\n> O catálogo consolidado agora vive em [CATALOG.md](CATALOG.md) e no dashboard interativo [catalog.html](catalog.html).\n"
                orig = idx.read_text(encoding="utf-8")
                if "CATALOG.md" not in orig:
                    idx.write_text(cat_ref + "\n" + orig, encoding="utf-8")
                    print("✅ Atualizado INDEX.md com referência ao CATALOG.md")
    elif CWD == GLOBAL_MKT_DIR:
        build_for_target(GLOBAL_MKT_DIR, "Super IA Marketing", cache, is_primary_global=True)
    else:
        build_for_target(CWD, "Projeto Local", cache, is_primary_global=False)

    save_cache(cache)
    print("\n🎉 Processamento concluído com sucesso!")

if __name__ == "__main__":
    main()
