---
# Repository: https://github.com/Felipelbahia/superiaprojects-marketing
# Status: Customizada / Modificada localmente por Felipe Bahia
name: seo-palavras-chave
description: "Use para pesquisar palavras-chave e intenção de busca: levantar termos, agrupar por tema e intenção, montar clusters de tópicos, analisar a página de resultados (SERP) de uma palavra e achar lacunas de conteúdo, com ou sem a extensão Keywords Everywhere. Gatilhos: \"pesquisa de palavras-chave\", \"keyword research\", \"intenção de busca\", \"cluster de tópicos\", \"o que o Google mostra para esta busca\", \"volume e dificuldade\". NÃO use para escrever o artigo (use seo-conteudo), para SEO programático (use seo-programatico), para auditar uma página (use seo-on-page) nem para tendências de conteúdo em redes sociais (use conteudo-tendencias)."
author: Antigravity Multi-IA Hub & Felipe Bahia (Futuro Mercado)
license: MIT
metadata:
  author: Antigravity Multi-IA Hub & Felipe Bahia (Futuro Mercado)
  version: 1.0.0
---
# Pesquisa de Palavras-Chave

Reúne os seis guias de pesquisa de palavras-chave que estavam dentro de `seo-conteudo`. O texto base é inglês.

## Qual guia usar

| Preciso de... | Leia |
|---|---|
| Um começo rápido: levantar termos e priorizar | [keyword-research.md](references/keyword-research.md) |
| Pesquisa avançada: agrupamento, intenção, lacunas de conteúdo | [keyword-research-deep.md](references/keyword-research-deep.md) |
| Classificar a intenção de busca (informacional, comercial, transacional, navegacional) | [keyword-intent-taxonomy.md](references/keyword-intent-taxonomy.md) |
| Ver o que já aparece no Google para uma busca e o que dá para superar | [serp-analyzer.md](references/serp-analyzer.md) |
| Organizar tópicos em pilar e satélites | [topic-cluster-templates.md](references/topic-cluster-templates.md) |
| Usar a extensão Keywords Everywhere (volume, CPC, termos relacionados) | [keywords-everywhere.md](references/keywords-everywhere.md) |

## Como trabalhar

1. Parta da marca e da persona (`_brands/<marca>/`) e do pilar de conteúdo, não de uma lista solta de termos.
2. Classifique a intenção antes de escolher o formato do conteúdo.
3. Entregue a lista priorizada com intenção, tema do cluster e a página que vai atender cada termo.
4. Salve em `content/<marca>/blog/AAAA-MM-DD - Nome da Demanda/briefing.md`.

## Onde isso se conecta

- Escrever o conteúdo a partir do brief: [seo-conteudo](../seo-conteudo/SKILL.md).
- Páginas em escala: [seo-programatico](../seo-programatico/SKILL.md).
- Auditar a página depois de publicada: [seo-on-page](../seo-on-page/SKILL.md).

## Scripts de cálculo

Programa em Python que agrupa palavras-chave e classifica a intenção de busca (origem: pacote `@clawfu/mcp-skills`, licença MIT; revisado e testado em 2026-10-20). Rode a partir da raiz do projeto, com o ambiente `.venv` (precisa só de `click`):

```bash
.venv/bin/python .agent/skills/seo-palavras-chave/scripts/keyword_clusterer.py cluster palavras.csv --n-clusters 10
.venv/bin/python .agent/skills/seo-palavras-chave/scripts/keyword_clusterer.py intent palavras.csv --column keyword
```

- **Intenção em português e inglês.** **Alterado em relação ao original**, que só tinha palavras em inglês (corrigido em 2026-10-20): "melhor ferramenta de email marketing" e "email marketing vale a pena" saem como comercial; "email marketing preço", como transacional.
- **Limite que continua:** a primeira palavra reconhecida decide, na ordem informacional, comercial, transacional e navegacional; "onde baixar app de email" sai como informacional (por causa do "onde"), e termos sem nenhuma palavra de intenção caem em informacional. Trate o resultado como triagem e revise as palavras de maior volume.
