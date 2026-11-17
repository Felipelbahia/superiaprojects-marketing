# SEO e GEO vindos do 0 Padrões (2026-11-17), analisados um a um

Cópias fiéis do que existia no 0 Padrões (os originais foram removidos de lá). Estes arquivos **não são agentes ativos**: `sync_entrypoints.py` só lê `.agent/agents/*.md` do primeiro nível.
O agente de SEO ativo é `seo-otimizacao-de-busca`, que usa as skills `seo-*` do hub.

| Original | Decisão | Onde está o conteúdo útil |
|---|---|---|
| `seo-cannibalization-detector` | Adicionado | `seo-on-page/references/canibalizacao-de-palavras-chave.md` (o hub só citava o tema de passagem) |
| `seo-snippet-hunter` | Juntado | `seo-conteudo/references/featured-snippets-e-paa.md` (só havia a regra "resposta primeiro") |
| `seo-fundamentals` (SKILL.md) | Arquivado | Resumo de princípios guardado em `principios-seo.md` (nesta pasta). Título/descrição, Core Web Vitals e E-E-A-T já estão em `seo-on-page`, `seo-tecnico/references/seo-fundamentals.md` e `seo-tecnico/references/seo-audit-framework.md`. O script virou `seo-tecnico/scripts/seo_checker.py` |
| `seo-meta-optimizer` | Arquivado | `seo-on-page/references/meta-tag-formulas.md` e `meta-tags-optimizer.md` |
| `seo-structure-architect` | Arquivado | `seo-on-page` (headings, `link-architecture-patterns.md`) e `seo-schema-markup` |
| `seo-content-planner` | Arquivado | `seo-palavras-chave/references/topic-cluster-templates.md`, `seo-conteudo/references/seo-content-brief.md` |
| `seo-content-writer` | Arquivado | `seo-conteudo` (`write-content.md`). Densidade de 0,5–1,5% e "nível escolar 8–10" conflitam com a voz de marca e o anti-slop |
| `seo-content-refresher` | Arquivado | `seo-on-page/references/content-refresher.md` e `content-decay-signals.md` |
| `seo-content-auditor` | Arquivado | `seo-on-page/references/content-quality-auditor.md` e o scorecard de 100 pontos |
| `seo-authority-builder` | Arquivado | `seo-geo/references/core-eeat-benchmark.md`, `seo-autoridade-e-backlinks` |
| `seo-keyword-strategist` | Arquivado | Baseado em densidade-alvo de palavra-chave, prática que o Google não usa; pesquisa e intenção ficam em `seo-palavras-chave` |
| `geo-fundamentals` (SKILL.md) | Arquivado | `seo-geo` (12 referências e checklist de prontidão), `seo-tecnico/references/robots-txt-reference.md` (rastreadores de IA). A tabela de "pesos de recuperação" (~40%, ~20%...) não tem fonte e não foi aproveitada |
| `geo-fundamentals/scripts/geo_checker.py` | Adaptado | `seo-geo/scripts/geo_checker.py` (presença por arquivo, sem nota em %, sem frases em inglês) |
| `seo-specialist` | Arquivado | `seo-geo` (SEO × GEO) e `seo-tecnico`; dependia de `clean-code` e `geo-fundamentals`, que não existem aqui |
