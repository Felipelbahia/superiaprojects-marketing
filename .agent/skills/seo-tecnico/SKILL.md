---
# Source: https://github.com/clawdb
# Repository: https://github.com/Felipelbahia/superiaprojects-marketing
# Status: Customizada / Modificada localmente por Felipe Bahia
name: seo-tecnico
description: "Use when performing technical SEO audits, diagnosing crawling or indexing issues, auditing Core Web Vitals (LCP, INP, CLS), configuring robots.txt (including AI crawlers like GPTBot), validating XML sitemaps, fixing HTTP status codes, or diagnosing site speed drops. Do NOT use for backlinks or link building (use seo-autoridade-e-backlinks)."
author: aaron-he-zhu & Antigravity Kit & Felipe Bahia (Futuro Mercado)
license: MIT
metadata:
  author: aaron-he-zhu & Antigravity Kit & Felipe Bahia (Futuro Mercado)
  version: 1.0.0
complements: seo-on-page, seo-schema-markup, seo-conteudo
---
# Technical SEO Checker

> Comprehensive technical audit framework covering crawlability, indexability, Core Web Vitals, server response codes, XML sitemaps, robots.txt directives, and modern AI crawler governance.

## When to Use This Skill

Activate this skill when:
- **Auditing a website before or after launch/migration**
- **Diagnosing sudden organic traffic or indexation drops**
- **Troubleshooting crawl budget issues** on large sites (1,000+ pages)
- **Configuring or debugging robots.txt** (including AI search bots: GPTBot, CCBot, PerplexityBot)
- **Validating XML sitemaps** and index structures
- **Analyzing Core Web Vitals (CWV)**: Largest Contentful Paint (LCP), Interaction to Next Paint (INP), and Cumulative Layout Shift (CLS)
- **Resolving redirect chains, loops, and 4xx/5xx HTTP status codes**

---

## Technical SEO Audit Architecture

```
[1. Crawlability & Bots] ──> [2. HTTP Status & Redirects] ──> [3. Indexation & Canonicals]
            │                                                                │
            ▼                                                                ▼
   [6. Mobile & Security] <── [5. Sitemaps & Architecture] <── [4. Core Web Vitals & Speed]
```

---

## Core Technical Domains

### 1. Crawlability & Robots.txt Governance

Search engines and AI bots must access URLs without obstruction:

- **Robots.txt Location**: Must be hosted at the exact domain root (`https://example.com/robots.txt`).
- **Syntax Rules**:
  - `User-agent: *`: Applies to all bots unless a specific block overrides it.
  - `Disallow: /admin/`: Blocks crawling of private directories.
  - `Sitemap: https://example.com/sitemap.xml`: Points crawlers directly to the primary sitemap index.
- **AI Crawler Directives (Modern 2026 Standards)**:
  - **GPTBot / ChatGPT-User**: OpenAI crawlers for search and training.
  - **PerplexityBot**: Perplexity real-time search indexing.
  - **ClaudeBot / Anthropic-AI**: Anthropic retrieval and web agents.
  - **Google-Extended**: Used specifically for Gemini training (does not affect standard Google Search).

*Consult [references/robots-txt-reference.md](references/robots-txt-reference.md) for complete user-agent tables and copy-ready configs.*

---

### 2. HTTP Status Codes & Redirect Chains

Improper status codes waste crawl budget and dilute PageRank:

| Code | Meaning | SEO Impact & Correct Action |
|------|---------|-----------------------------|
| **200 OK** | Page successfully delivered | Normal state for indexable pages |
| **301 Moved Permanently** | Permanent redirection | Passes ~99% PageRank. Use for URL changes, migrations |
| **302 Found (Temporary)** | Temporary redirection | Does not pass full authority; avoid for permanent migrations |
| **304 Not Modified** | Cached version valid | Saves bandwidth and crawl budget |
| **404 Not Found** | URL does not exist | Custom 404 page required; monitor in Search Console |
| **410 Gone** | Permanently deleted | Best practice for deleted pages you want purged from index |
| **500 / 503 Server Error** | Internal error / unavailable | Critical issue; if prolonged, search engines de-index URLs |

**Redirect Chain Rule**: Avoid chains (`A -> B -> C`). Redirect directly from source to destination (`A -> C`). Chains beyond 2 hops increase latency and risk bot abandonment.

*Consult [references/http-status-codes.md](references/http-status-codes.md).*

---

### 3. Indexability & Canonicalization

Being crawlable does not guarantee proper indexation:

1. **Meta Robots Tag**:
   - `<meta name="robots" content="index, follow">`: Standard indexable page.
   - `<meta name="robots" content="noindex, follow">`: Exclude page from search while allowing link equity to pass.
2. **Canonical Tags (`rel="canonical"`)**:
   - Prevent duplicate content across parameter URLs, sorting variations, and HTTP/HTTPS mirrors.
   - Every indexable page must contain a self-referencing canonical tag:
     `<link rel="canonical" href="https://example.com/canonical-url/">`

---

### 4. Core Web Vitals (CWV) & Performance Benchmarks

Google's page experience signals directly impact mobile search rankings:

| Metric | Target (Good) | What It Measures | Primary Optimization Lever |
|--------|---------------|------------------|-----------------------------|
| **LCP (Largest Contentful Paint)** | ≤ 2.5s | Loading performance (main hero/image) | Image compression (AVIF/WebP), fetchpriority="high", CDN |
| **INP (Interaction to Next Paint)** | ≤ 200ms | Responsiveness to user clicks/taps | Minimizing main-thread JavaScript, yielding with setTimeout |
| **CLS (Cumulative Layout Shift)** | ≤ 0.1 | Visual stability during page load | Explicit width/height on images and video, reserving ad space |


---

### 5. XML Sitemaps Architecture

A clean XML sitemap speeds up discovery of new and updated content:

- **Format**: Valid XML according to `sitemaps.org` protocol.
- **Size Limits**: Maximum 50,000 URLs or 50MB uncompressed per sitemap file (use a `<sitemapindex>` for larger sites).
- **Inclusion Rules**: Include **only 200 OK, canonical, indexable** URLs. Never include noindexed, redirected, or 404 URLs.
- **`<lastmod>` Accuracy**: Always set `<lastmod>` to the exact timestamp of meaningful content updates.


---

## Technical Audit Checklist

Run through this diagnostic checklist on every technical inspection:

```markdown
### Technical SEO Health Checklist

1. CRAWL & ACCESS:
   □ robots.txt is accessible and syntax is error-free
   □ Critical pages are not blocked by Disallow directives
   □ AI search crawlers (PerplexityBot, GPTBot) explicitly configured
   □ Server response time (TTFB) is under 600ms globally

2. REDIRECTS & STATUS CODES:
   □ No redirect chains (>1 hop) or redirect loops
   □ HTTP properly redirects to HTTPS (301)
   □ Non-www properly redirects to www (or vice-versa)
   □ Zero broken internal links (404 errors)

3. INDEXING & CANONICALS:
   □ Self-referencing canonical tag present on all indexable pages
   □ No conflicting signals (e.g. page has canonical AND noindex)
   □ Parameter URLs properly canonicalized to clean URL
   □ XML sitemap submitted in Google Search Console and Bing Webmaster

4. PERFORMANCE & EXPERIENCE:
   □ LCP ≤ 2.5s, INP ≤ 200ms, CLS ≤ 0.1
   □ Hero images use fetchpriority="high" and modern formats (WebP/AVIF)
   □ CSS/JS minified and critical CSS inlined
   □ Mobile viewport properly configured (<meta name="viewport" content="width=device-width, initial-scale=1">)
```

---

## Reference Materials

The following in-depth technical guides are bundled in the `references/` directory:

- **[http-status-codes.md](references/http-status-codes.md)** — Exhaustive guide to HTTP status codes, redirect loops, and server error resolution.
- **[robots-txt-reference.md](references/robots-txt-reference.md)** — Syntax specifications, bot user-agents, and AI crawler governance rules.
- **[check-technical.md](references/check-technical.md)** — Rapid technical inspection workflow and server validation steps.

---

## Related Skills

- **`seo-on-page`** — On-page content elements, internal link structures, and content freshness.
- **`seo-schema-markup`** — JSON-LD structured data and rich snippet deployment.
- **`seo-conteudo`** — Search-optimized writing and topical cluster development.
- **`seo-geo`** — Optimization for AI answer engines and Perplexity visibility.

## Referências adicionais

- [dataforseo-api.md](references/dataforseo-api.md) — API DataForSEO para SERP, palavras-chave, backlinks e análise on-page (requer a API).
- [entity-signal-checklist.md](references/entity-signal-checklist.md) — Checklist de sinais de entidade por prioridade e método de verificação, para auditoria sistemática.
- [google-search-console.md](references/google-search-console.md) — Uso do Google Search Console para monitorar desempenho e indexação.
- [seo-audit-checklist.md](references/seo-audit-checklist.md) — Framework de auditoria de SEO em formato de checklist.
- [seo-audit-framework.md](references/seo-audit-framework.md) — Como auditar e diagnosticar problemas de SEO ("por que não ranqueio", SEO técnico, on-page).
- [seo-connectors.md](references/seo-connectors.md) — Categorias de ferramentas e conectores, em placeholders por categoria.
- [original-reference.md](references/original-reference.md) — Guia original completo desta skill (780 linhas), de antes da condensação do `SKILL.md`.

## Para onde foram os outros assuntos

- **Backlinks e link building:** skill [seo-autoridade-e-backlinks](../seo-autoridade-e-backlinks/SKILL.md).
- **Acompanhamento de posições:** [seo-relatorio-de-desempenho](../seo-relatorio-de-desempenho/SKILL.md).
- **Verificador de links quebrados, gerador de sitemap e auditoria Lighthouse por script:** arquivados em `.agent/skills/_arquivo/mescladas/r8-seo/` (dependiam de um programa que não existe aqui).
- **[seo-fundamentals.md](references/seo-fundamentals.md)** — Auditoria de SEO completa (técnica, on-page e E-E-A-T) com nota de saúde por categoria; veio da skill `seo-conteudo`.
