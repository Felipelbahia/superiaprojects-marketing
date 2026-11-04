---
# Source: https://github.com/clawdb
# Repository: https://github.com/Felipelbahia/superiaprojects-marketing
# Status: Customizada / Modificada localmente por Felipe Bahia
name: seo-geo
description: "Use when optimizing content for Generative Engine Optimization (GEO), AI citations, Perplexity, Google AI Overviews, SearchGPT, Claude, or Gemini; making brand content quotable by LLMs; or establishing entity authority in Knowledge Graphs. Do NOT use for creating new content from scratch with research and expert quotes (use conteudo-pesquisa), for keyword-driven SEO articles (use seo-conteudo) or for structured data markup (use seo-schema-markup)."
author: aaron-he-zhu & Antigravity Kit & Felipe Bahia (Futuro Mercado)
license: MIT
metadata:
  author: aaron-he-zhu & Antigravity Kit & Felipe Bahia (Futuro Mercado)
  version: 1.0.0
complements: seo-conteudo, seo-on-page, seo-schema-markup
---
# GEO Content Optimizer (Generative Engine Optimization)

> Optimize digital content to maximize citations, mentions, and source inclusion across AI search engines and answer engines—including Perplexity AI, Google AI Overviews, OpenAI SearchGPT, Claude, and Gemini.

## When to Use This Skill

Activate this skill when:
- **Optimizing existing pages or articles** to be cited by AI answer engines
- **Engineering quotable snippets** that LLMs can easily parse, extract, and reference
- **Auditing brand visibility** when AI systems fail to mention your company or product
- **Aligning entity authority** with Knowledge Graphs (Google Knowledge Graph, Wikidata)
- **Formatting technical documentation and guides** for Retrieval-Augmented Generation (RAG)
- **Balancing traditional SEO** with conversational AI discovery

---

## The GEO Paradigm vs Traditional SEO

| Dimension | Traditional SEO | Generative Engine Optimization (GEO) |
|-----------|-----------------|--------------------------------------|
| **Goal** | Rank in the top 10 blue links | Be cited as an authoritative source / answer |
| **User Journey** | Query -> Click -> Browse page | Query -> AI synthesis -> Source click-through |
| **Target Engine** | Googlebot (crawling & PageRank) | LLM RAG pipelines (semantic search & retrieval) |
| **Optimization Focus** | Keywords, title tags, backlinks | Semantic entities, statistical clarity, factual density |
| **Success Metric** | Organic rankings & impressions | Citation frequency, sentiment, referral traffic |

---

## Core GEO Mechanics

### 1. The Quotable Information Architecture

AI engines cite pages that provide **clear, verifiable, and unambiguous answers**. Use the **Claim + Anchor + Data** formula:

```markdown
### Quotable Snippet Formula:
[Direct Definition or Claim] + [Methodological Anchor] + [Precise Metric/Data] + [Contextual Scope]

Example:
"Generative Engine Optimization (GEO) increases brand citations in AI answer engines by an average of 34% when content includes structured comparison tables and direct statistical claims, based on a 2025 analysis of 1,200 search queries across Perplexity and Google AI Overviews."
```

### 2. Multi-Platform Ranking Signals

Different AI platforms prioritize distinct retrieval signals:

- **Perplexity AI**: Prioritizes fresh content, primary sources, Reddit/community discussions, clear numeric data, and bulleted takeaways. Highly sensitive to domain authority and fast server response times.
- **Google AI Overviews (SGE)**: Heavily tied to top-ranking organic pages (85%+ of cited sources already rank in the top 10 for the query), high CORE-EEAT scores, and schema markup (FAQPage, Article, Review).
- **SearchGPT / ChatGPT**: Favors natural language answers, structured headings, strong entity recognition (Wikidata/Knowledge Graph), and reputable press citations.
- **Claude / Gemini**: Favors logical depth, absence of marketing hyperbole, neutral tone, and well-reasoned comparative analyses.

*Consult [references/platform-ranking-factors.md](references/platform-ranking-factors.md) and [references/ai-citation-patterns.md](references/ai-citation-patterns.md).*

---

## Step-by-Step GEO Optimization Workflow

```
[1. Entity & Knowledge Graph] ──> [2. Direct Answer Injection] ──> [3. Statistical Anchoring]
             │                                                                   │
             ▼                                                                   ▼
  [6. Validation & Test] <── [5. RAG Formatting & Tables] <── [4. Human Voice / Anti-Slop]
```

### Step 1: Establish Entity Authority & Disambiguation
Ensure AI systems know *who* you are, *what* you do, and *why* you are an authority:
- Use consistent Organization and Person schema with `sameAs` links pointing to official profiles (LinkedIn, Crunchbase, Wikipedia, GitHub).
- Disambiguate brand terms from generic industry words.
- Clearly state your domain category in the first sentence of your About page and homepage.

*See [references/entity-optimizer.md](references/entity-optimizer.md) and [references/knowledge-graph-guide.md](references/knowledge-graph-guide.md).*

### Step 2: Inject Direct Answers (BLUF)
- Place direct answers within the **first 50-70 words** beneath each H2 heading.
- Avoid preamble phrases (*"In this section, we will explore..."* or *"It is important to remember that..."*).
- Formulate H2 headers as natural user questions (*"What is the recommended size for a print QR code?"*).

### Step 3: Embed Statistical & Empirical Anchors
AI systems strongly prefer citing pages with concrete figures:
- Add specific percentages, sample sizes, timelines, or benchmarks.
- Attribute data directly to its source (*"According to Gartner's 2025 CMO Survey..."*).
- Replace vague descriptors (*"very fast"*, *"huge increase"*) with quantifiable measurements (*"reduced latency by 420ms"*, *"38% higher conversion"*).

### Step 4: Human Voice & Burstiness (Anti-Slop Guardrail)
Content generated by AI that sounds synthetic is increasingly filtered or downranked by search retrieval models:
- Maintain high **burstiness**: mix short, punchy sentences (4-6 words) with medium and complex explanatory sentences.
- Strictly eliminate AI cliches: *"testament"*, *"delve"*, *"tapestry"*, *"in conclusion"*, *"crucial"*, *"furthermore"*.
- Write from a first-person perspective (*"we tested"*, *"our team discovered"*).

*Consult [references/ai-writing-detection.md](references/ai-writing-detection.md) and [references/ai-seo.md](references/ai-seo.md).*

### Step 5: Format for RAG Retrieval & Context Windows
LLM retrieval chunkers typically slice documents into 300 to 800-token chunks:
- Keep sub-sections self-contained so that a single chunk contains both the question and the full answer.
- Use markdown comparison tables (LLMs extract tabular data with near-100% precision).
- Use definition lists or bold key-value pairs for technical specifications.

*Consult [references/llm-optimized-content.md](references/llm-optimized-content.md).*

---

## GEO Content Audit Checklist

Use this scorecard before publishing content designed for AI visibility:

```markdown
### GEO Readiness Checklist

1. ENTITY CLARITY:
   □ Brand and product names are explicitly defined in context
   □ Organization/Author sameAs links point to authoritative external profiles
   □ Niche terminology aligns with standard Knowledge Graph definitions

2. DIRECT ANSWER VALUE:
   □ H2 questions are answered immediately in the following 1-2 sentences
   □ High-density summary or TL;DR box placed above the fold
   □ Answer can stand alone if extracted as a single chunk

3. CITATION TRIGGERS:
   □ Contains at least 2 proprietary data points, benchmarks, or case metrics
   □ Source citations are clear, verifiable, and dated
   □ Quotable snippet formula applied to key definitions

4. RAG READABILITY:
   □ Markdown tables used for multi-option comparisons
   □ Bulleted summaries highlight takeaways
   □ Free from generic filler and repetitive AI clichés
```

---

## Guias por pergunta

Os guias estão em [`references/`](references/). O texto base é inglês, exceto onde indicado.

### Entender como a busca por IA escolhe fontes
- [ai-seo.md](references/ai-seo.md) — Da busca por palavra-chave para a otimização generativa: como a busca por IA funciona e o que ela cita mais.
- [platform-ranking-factors.md](references/platform-ranking-factors.md) — Como cada plataforma de IA escolhe as fontes (AI Overviews, ChatGPT, Perplexity, Copilot, Claude).
- [ai-citation-patterns.md](references/ai-citation-patterns.md) — Padrões de citação por plataforma e fatores de probabilidade de ser citado.

### Escrever e formatar para ser citado
- [llm-optimized-content.md](references/llm-optimized-content.md) — Regras de estrutura para janelas de contexto e recuperação por trechos.
- [quotable-content-examples.md](references/quotable-content-examples.md) — Dez tipos de bloco citável (definição, estatística, passo a passo, comparação...).
- [ai-writing-detection.md](references/ai-writing-detection.md) — Marcas de texto de IA e como manter autenticidade humana.

### Autoridade da marca e entidade
- [entity-optimizer.md](references/entity-optimizer.md) — Entidade, Knowledge Graph e desambiguação da marca.
- [knowledge-graph-guide.md](references/knowledge-graph-guide.md) — Como construir e ligar relações semânticas entre entidades.

### Auditar
- [core-eeat-benchmark.md](references/core-eeat-benchmark.md) — Benchmark de qualidade de conteúdo com 80 itens (precisão, confiança, expertise).
- [ai-discoverability-audit-v2.md](references/ai-discoverability-audit-v2.md) — "Signal Audit" em 6 seções, versão 2 de outro autor (Brian Wagner). Direito de uso confirmado pelo usuário.

### Guia original
- [original-reference.md](references/original-reference.md) — Guia original completo desta skill (625 linhas), de antes da condensação do `SKILL.md`.

---

## Related Skills

- **`seo-conteudo`** — Comprehensive search content creation and keyword clustering.
- **`seo-on-page`** — Technical on-page evaluation and content freshness auditing.
- **`seo-schema-markup`** — Structured data (Schema.org) for search engine rich results.
- **`geral-anti-slop`** — Mandatory verification to strip AI clichés and unnatural phrasing.

## Referências vindas de outras skills

- **[query-bank.md](references/query-bank.md)** — Banco de perguntas para testar a visibilidade de uma marca em buscas por IA (veio de `data-web-ga4`).
