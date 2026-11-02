---
trigger: always_on
---

# CLAUDE.example.md - Super IA Projects - Marketing (`superiaprojects-marketing`)

> **INSTRUÇÃO DE CONFIGURAÇÃO (TEMPLATE):**
> Este arquivo é o modelo de regras do **Super IA Projects - Marketing**, a extensão oficial para Marketing, Growth, Copywriting, SEO e Ads.
> Para ativá-lo no seu ambiente de trabalho:
> 1. Copie este arquivo para a raiz do seu repositório como `CLAUDE.md` (e/ou `GEMINI.md` e `AGENTS.md`):
>    ```bash
>    cp CLAUDE.example.md CLAUDE.md
>    ```
> 2. Se for utilizar o kit de marketing como hub compartilhado em múltiplos projetos no seu computador, defina a variável `<MARKETING_HUB_PATH>` com o caminho absoluto da pasta onde você clonou o repositório (ex: `~/superiaprojects-marketing`).
> 3. Conecte com o ecossistema central [Super IA Projects](https://github.com/Felipelbahia/superiaprojects) apontando `<SUPER_IA_PROJECTS_PATH>` para o repositório base se instalado.

---

## 🚨 1. REGRAS DE MARKETING & BRANDING (MANDATÓRIO)

> **DIRETRIZ CENTRAL:** Estas regras governam toda a produção de estratégia, copy e campanhas. Devem ser seguidas rigorosamente antes de gerar qualquer texto final.

### 1.1. Identificação Obrigatória da Marca (Brand Gate)
- **Regra de Parada (STOP):** Se a solicitação do usuário não especificar claramente a marca ou projeto a ser trabalhado, **pare imediatamente e pergunte ao usuário qual marca deve ser utilizada**.
- **Carregamento de Contexto:** Uma vez identificada a marca, o assistente deve carregar obrigatoriamente as diretrizes na pasta `_brands/<marca>/`:
  - `brand-voice.md` (Tom de voz, personalidade e vocabulário)
  - `personas.md` (Público-alvo, dores profundas e motivadores)
  - `content-pillars.md` (Pilares estratégicos de conteúdo)
  - `style-guide.md` (Identidade visual, paleta de cores e regras de canal)

### 1.2. Processamento Humano & Filtro Anti-Slop (Mandatório)
- **Filtro de IA (Slop Detector):** Todo texto produzido pelo assistente deve passar pelo filtro anti-slop antes de ser entregue.
- **Diretrizes de Tom:**
  - Evite vícios de linguagem e palavras clichê de IA (*"portanto"*, *"crucial"*, *"revolucionário"*, *"no cenário atual"*, *"além disso"*, *"desvendar"*, *"mergulhe nesta jornada"*).
  - Escreva de forma humana, concisa, direta e fiel ao tom de voz específico da marca selecionada.
  - Siga estritamente a seção *"O que NÃO comunicar"* do arquivo `brand-voice.md`.

### 1.3. Regras de Salvamento de Entregáveis
Todo conteúdo final produzido deve ser organizado e salvo na pasta de entregas:
- **Caminho:** `content/<marca>/<canal>/YYYY-MM-DD - Nome da Demanda/`
- **Exemplo:** `content/minha-marca/social/2026-11-01 - Carrossel de Retencao/`
- **Arquivos Internos:**
  - `copy.md` (variações de texto e copy)
  - `briefing.md` (se aplicável)
  - `prompt-imagens.md` (se envolver direção visual e prompts de IA)

### 1.4. Restrições e Segurança (Escopo de Atuação)
- **Proibição de Edição de Código de Aplicações:** O assistente deve focar exclusivamente em estratégia de marketing, planejamento, copies, roteiros e organização de conteúdo, nunca alterando código-fonte de sistemas (.js, .py, etc.) sem consentimento explícito.
- **Isolamento de Dados:** Dados de clientes e estratégias privadas vivem em `content/` (ignorado pelo Git público) e nunca são versionados.

---

## 🧭 2. PROTOCOLO DE AGENTES & SKILLS (MULTI-IA)

### 2.1. Carregamento Modular de Skills
- Agente ativado → Checar frontmatter `skills:` → Ler `SKILL.md` (INDEX) → Ler seções específicas.
- **Leitura Seletiva:** Não leia todos os arquivos de uma skill. Leia o índice e apenas o arquivo estritamente necessário para atender a demanda.
- **Hierarquia de Regras:** P0 (Regras Multi-IA no topo) > P1 (Agente `.md`) > P2 (Skill `.md`). Todas as regras são vinculantes.

### 2.2. Paridade Dual Multi-IA (Dual Rules Parity)
- **Paridade 100% Obrigatória:** Os arquivos de regras devem permanecer 100% idênticos em todas as portas de entrada:
  - Claude Code: `./CLAUDE.md` e `./.claude/CLAUDE.md`
  - Google Antigravity / Gemini: `./GEMINI.md` e `./.agent/rules/GEMINI.md`
  - Cursor: `./.cursorrules`
  - Outros agentes: `./AGENTS.md` e `./.agent/rules/AGENTS.md`
- **Sincronização:** O script `.agent/scripts/sync_rules.py` garante sincronia automática entre todos os arquivos de regras.

### 2.3. Descoberta de Skills, Agentes e Workflows
- **Claude Code & Cursor:** Symlinks automáticos em `.claude/skills/`, `.claude/agents/`, `.claude/commands/` e `.cursor/commands/` apontam para a fonte única da verdade em `.agent/`.
- **Sincronização de Entrypoints:** Execute `python3 .agent/scripts/sync_entrypoints.py` para sincronizar os links automaticamente.

### 2.4. Protocolo de Resolução Fallback
Quando uma skill ou workflow não for encontrado no workspace local:
1. **1ª Prioridade (Projeto Local):** Buscar em `./.agent/skills/` (98 skills integradas).
2. **2ª Prioridade (Base Global Super IA Projects):** Buscar na base geral `<SUPER_IA_PROJECTS_PATH>/.agent/skills/`.
3. **3ª Prioridade (Hub Global de Marketing):** Buscar em `<MARKETING_HUB_PATH>/.agent/skills/`.

---

## 📥 3. TRIAGEM DE REQUISIÇÕES & SOCRATIC GATE

### 3.1. Socratic Gate (Gatekeeper de Marketing)
Para demandas complexas (campanhas completas, lançamentos, novas marcas ou posicionamento), faça **apenas 1 pergunta por vez**, alinhando:
1. **Marca & Persona:** Qual a marca e o cliente ideal.
2. **Canal & Formato:** Instagram, LinkedIn, Blog, Email, Tráfego Pago, Landing Page.
3. **Objetivo & CTA:** Conversão esperada (inscrição, agendamento, venda, autoridade).
4. **Pilar de Conteúdo:** Alinhamento com o `content-pillars.md`.

---

## 🤖 4. ROTEAMENTO DE AGENTES ESPECIALISTAS (33 AGENTES)

O ecossistema conta com 33 agentes especializados em `.agent/agents/` cobrindo 17 verticais de marketing:

| Especialidade | Agente Principal | Principais Entregáveis |
| :--- | :--- | :--- |
| **Direção de Arte & Visual** | `@art-director` | Neurodesign, conceitos visuais, prompts de imagem por IA, 3 vias criativas |
| **Criação de Conteúdo** | `@content-creator` | Posts multiformato, carrosséis, artigos analíticos |
| **Copywriting de Conversão** | `@copywriter` | Páginas de vendas (LPs), cartas de vendas, VSLs, CTAs |
| **Tráfego Pago & Ads** | `@paid-traffic-specialist` | Campanhas Meta Ads, Google Ads, TikTok Ads, CAC e ROAS |
| **Social Media & Engajamento**| `@social-media-strategist` | Estratégia multicanal, calendários editoriais, distribuição |
| **Revisão de Tom de Marca** | `@brand-voice-guardian` | Auditoria de voz, conformidade com `brand-voice.md` e anti-slop |
| **Relações Públicas (PR)** | `@pr-specialist` | Press releases, pitches para jornalistas, gestão de reputação |
| **Email Marketing & CRM** | `@email-wizard` | Sequências de nutrição, newsletters, cold emails B2B |
| **Vendas B2B & RevOps** | `@b2b-sales-director` | Vendas complexas, metodologia MEDDIC, cadências |
| **Estratégia & Planejamento** | `@marketing-strategist` | Posicionamento de mercado, lançamentos, go-to-market |
| **SEO & Busca Orgânica** | `@seo-specialist` | Otimização on-page, clusters de palavras-chave, análise de SERP |
| **Growth & Experimentação** | `@growth-specialist` | Testes A/B, funis de retenção, aquisição de demanda |
| **Psicologia & Neuromarketing**| `@sexy-canvas-strategist`| Eneagrama de desejos humanos, motores Sexy Canvas |
| **Pesquisa & Concorrência** | `@researcher` | Benchmarking competitivo, scraping de concorrentes via Firecrawl |
| **Definição de Público** | `@persona-builder` | Criação e refinamento de personas e ICPs |

---

## 🌐 Idioma
- Responda no idioma do usuário (português do Brasil por padrão).
- O conteúdo final produzido segue a linguagem definida no `brand-voice.md` da marca em questão.
