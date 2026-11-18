# seo

Busca orgânica: palavras-chave, on-page, técnico, schema, GEO, backlinks, SEO programático, app store e relatórios.

> Gerado por build_sip_index.py. Não edite à mão. Skill: `"<HUB>/.agent/skills/<nome>/SKILL.md"`; agent: `"<HUB>/.agent/agents/<nome>.md"`; workflow: `"<HUB>/.agent/workflows/<nome>.md"`.

## Skills (11)

| Skill | Use quando |
| --- | --- |
| `seo-app-store` | Especialista em App Store Optimization (ASO) para Apple App Store e Google Play Store. Abrange pesquisa de palavras-chave mobile, otimização de metadados visuais e textuais, Custom Product Pages (CPP), testes A/B de ícones e screenshots, conversão de downloads e gestão de avaliações. Use para: ranquear aplicativos nas buscas mobile, otimizar fichas de lojas, estruturar lançamentos de apps e maximizar taxas de instalação orgânica. |
| `seo-autoridade-e-backlinks` | Use para analisar e conquistar autoridade de domínio e backlinks: avaliar o perfil de links, identificar links tóxicos, medir a autoridade do domínio (rubrica CITE), montar estratégia de link building e escrever e-mails de outreach e digital PR. Gatilhos: "backlinks", "perfil de links", "link building", "autoridade de domínio", "links tóxicos", "outreach para links". |
| `seo-conteudo` | Use when writing search-optimized blog posts, pillar pages, comparison guides, or how-tos; creating SEO briefs; using Google's E-E-A-T guidelines. |
| `seo-geo` | Use when optimizing content for Generative Engine Optimization (GEO), AI citations, Perplexity, Google AI Overviews, SearchGPT, Claude, or Gemini; making brand content quotable by LLMs; or establishing entity authority in Knowledge Graphs; also to run the geo_checker.py sweep (JSON-LD, author, date, H2) over a folder of HTML/JSX/TSX pages before publishing. |
| `seo-on-page` | Use when auditing on-page SEO factors, title tags, meta descriptions, headings, internal link architectures, content quality, E-E-A-T signals, content freshness and decay, or diagnosing why a page dropped in search rankings. |
| `seo-palavras-chave` | Use para pesquisar palavras-chave e intenção de busca: levantar termos, agrupar por tema e intenção, montar clusters de tópicos, analisar a página de resultados (SERP) de uma palavra e achar lacunas de conteúdo, com ou sem a extensão Keywords Everywhere. Gatilhos: "pesquisa de palavras-chave", "keyword research", "intenção de busca", "cluster de tópicos", "o que o Google mostra para esta busca", "volume e dificuldade". |
| `seo-podcast` | Optimize podcast content for search engines using transcripts, structured show notes, and strategic keyword targeting to drive organic discovery. Use when: Launching a new podcast and planning for discoverability; Adding transcripts to existing episodes for SEO benefit; Optimizing show notes for search traffic; Building topical authority through podcast content; Increasing organic traffic to podcast landing pages |
| `seo-programatico` | Use para criar páginas de SEO em escala a partir de modelos e dados (SEO programático): páginas de comparação, de localidade, de integração, de glossário, diretórios e templates com padrões de título, links internos e schema, sem cair em conteúdo raso. Gatilhos: "SEO programático", "páginas em escala", "template de página", "centenas de páginas", "páginas de cidade ou de categoria". |
| `seo-relatorio-de-desempenho` | Use para acompanhar e reportar o desempenho de SEO e GEO: relatório executivo, detecção de anomalias, alertas de volatilidade de ranking e KPIs no Google, Bing e buscadores de IA (Perplexity, SearchGPT, Claude, Gemini). Gatilhos: "relatório de SEO", "queda de ranking", "tráfego orgânico caiu", "KPI de SEO". |
| `seo-schema-markup` | Use when the user asks to "add schema markup", "generate structured data", "JSON-LD", "rich snippets", "FAQ schema", "I want star ratings in Google", "product markup", or "recipe schema". Generates structured data markup (Schema.org JSON-LD) to enable rich results where Google still shows them (Product, Review, Article and others). FAQ and How-To rich results were retired (see seo-on-page/references/regras-de-referencia-google.md). For meta tag optimization, see meta-tags-optimizer. For broader technical SEO, see seo-tecnico. |
| `seo-tecnico` | Use when performing technical SEO audits, diagnosing crawling or indexing issues, auditing Core Web Vitals (LCP, INP, CLS), configuring robots.txt (including AI crawlers like GPTBot), validating XML sitemaps, fixing HTTP status codes, or diagnosing site speed drops; also to run the seo_checker.py sweep (title, meta description, Open Graph, H1, image alt) over a folder of HTML/JSX/TSX pages before publishing a site or landing page. |

## Agents (1)

| Agent | Use quando |
| --- | --- |
| `seo-otimizacao-de-busca` | Search engine optimization expert. Use for optimizing content for search engines while maintaining quality and readability. Reviews content for keyword optimization, on-page SEO, technical SEO, and SERP feature potential. Examples: <example>Context: User created blog post. user: "Optimize this blog post for SEO" assistant: "I'll use the seo-otimizacao-de-busca agent to review keyword usage, meta tags, structure, and technical elements." <commentary>SEO optimization requires expert knowledge of search algorithms and best practices.</commentary></example> <example>Context: User needs SEO audit. user: "Why isn't this page ranking?" assistant: "Let me deploy the seo-otimizacao-de-busca agent to analyze SEO issues and provide optimization recommendations." <commentary>SEO diagnostics require systematic analysis of multiple ranking factors.</commentary></example> |

## Workflows (7)

| Workflow | Use quando |
| --- | --- |
| `/seo-agrupamento-de-palavras-chave` | Techniques for expanding seed keywords and clustering by topic and intent. Use when building keyword lists, planning content calendars, or identifying topic clusters for pillar content strategy. |
| `/seo-analise-de-serp` | SERP analysis techniques for intent classification, feature identification, and competitive intelligence. Use when analyzing search results for content strategy. |
| `/seo-api-de-busca` | SerpApi search engine results API via curl. Use this skill to scrape Google, Bing, YouTube, and other search engines. |
| `/seo-checklist-semanal` | Gera o checklist semanal de manutenção e otimização de SEO. Use para organizar as tarefas de SEO da semana por dia (rankings, saúde técnica, conteúdo, link building, concorrência). |
| `/seo-otimizacao-de-conteudo` | Optimize content for search engines with keyword analysis, readability scoring, meta descriptions, and competitor comparison. Use this when users want to improve SEO, optimize blog posts, or analyze content for search performance. |
| `/seo-search-console` | Google Search Console indexing assistant. Use when the user wants to track page indexing status, compare sitemap against GSC indexed pages, manage submission tracking, or move false positives (pages indexed per URL Inspection but not yet in GSC export) to the indexed list. Maintains two tracking files (indexed.md, to-index.md) with prioritization support. |
| `/seo-wordpress` | Batch update Yoast SEO metadata (titles, descriptions, focus keyphrases) in WordPress via GraphQL. Use when the user wants to update SEO metadata, optimize titles, fix meta descriptions, or manage Yoast SEO fields across multiple posts. Supports preview mode, progress tracking, and resume capability. |

