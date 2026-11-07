---
# Source: https://github.com/clawdb
# Repository: https://github.com/Felipelbahia/superiaprojects-marketing
# Status: Customizada / Modificada localmente por Felipe Bahia
name: revenue-inteligencia-competitiva
description: "Use para inteligência competitiva estratégica: mapa de mercado, teardown de concorrente, battlecard, análise de fosso (moat), pesquisa win/loss e mapa de diferenciação. Gatilhos: \"analisar concorrente\", \"battlecard\", \"win/loss\", \"teardown\", \"diferenciação\". NÃO use para posicionar o próprio produto (use revenue-gtm-e-posicionamento), monitorar preço de concorrente (use o workflow revenue-monitoramento-de-preco-concorrente) nem anúncios de concorrentes (use o workflow ads-extracao-de-anuncios-concorrentes)."
author: ClawFu, aaron-he-zhu & Antigravity Kit & Felipe Bahia (Futuro Mercado)
license: MIT
metadata:
  author: ClawFu, aaron-he-zhu & Antigravity Kit & Felipe Bahia (Futuro Mercado)
  version: 1.0.0
complements: revenue-gtm-e-posicionamento, persona-icp, copy-conversao
---
# Competitive Intelligence & Market Landscaping

> Conduct rigorous competitor teardowns, build actionable sales battlecards, analyze defensible economic moats, and uncover strategic market whitespace to out-position rivals and win contested deals.

## When to Use This Skill

Use this skill when you need to:

- **Conduct a deep competitor teardown** across product, pricing, messaging, and acquisition channels
- **Build competitive sales battlecards** equipping go-to-market teams to win against specific rivals
- **Identify defensible economic moats** (network effects, switching costs, brand, economies of scale)
- **Map market alternatives** and craft high-converting comparison pages ("Us vs Them")
- **Monitor competitor movements** (pricing shifts, feature launches, hiring trends, positioning pivots)
- **Perform win/loss analysis** to diagnose why prospects choose or reject your solution

---

## 4-Tier Competitor Taxonomy

Every comprehensive market landscape segments rivals into four distinct buckets:

```
+-----------------------------------------------------------------------------------+
| TIER               | DEFINITION                        | STRATEGIC FOCUS          |
+--------------------+-----------------------------------+--------------------------+
| 1. Direct          | Solves same problem for same ICP  | Head-to-head battlecards |
| 2. Indirect        | Solves same problem differently   | Value proposition framing|
| 3. Tertiary        | Adjacent tools that could expand  | Partnership or moat watch|
| 4. Status Quo      | Spreadsheets, manual effort, inertia| Cost of inaction agitation|
+-----------------------------------------------------------------------------------+
```

*See [references/competitor-analysis.md](references/competitor-analysis.md) and [references/competitor-alternatives.md](references/competitor-alternatives.md).*

---

## The 5-Dimension Competitor Teardown Protocol

When evaluating a competitor, systematically audit these five vectors:

1. **Positioning & Narrative**:
   - What is their primary claim? Who do they declare as the enemy?
   - What awareness stage does their homepage target?
2. **Pricing & Packaging**:
   - Pricing model (flat-rate, per-seat, usage-based, freemium).
   - What features are gated behind enterprise tiers?
3. **Product & Feature Matrix**:
   - Core capabilities vs table-stakes features vs marketing gimmicks.
   - What are their fatal flaws based on user reviews (G2, Capterra, Trustpilot)?
4. **Distribution & Acquisition**:
   - Organic search footprint (keywords, topic clusters).
   - Paid ad strategy, affiliate networks, and ecosystem integrations.
5. **Customer Sentiment & Churn Drivers**:
   - Top 3 reasons users switch away from them.
   - Common customer service complaints and onboarding friction.

*See [references/competitor-teardown.md](references/competitor-teardown.md) and [references/semrush-research.md](references/semrush-research.md).*

---

## Sales Battlecard Architecture

Equip commercial teams with concise, modular objection-handling cards:

```
+-----------------------------------------------------------------------------------+
| BATTLECARD COMPONENT       | CONTENT FOCUS                                        |
+----------------------------+------------------------------------------------------+
| 1. Quick Dismiss / Landmine| 1 sentence planting doubt on their core architectural flaw|
| 2. Where We Win            | 3 distinct capabilities where our solution dominates |
| 3. Where They Win          | Honest acknowledgment of their strengths + reframe    |
| 4. FUD Defense             | Countering rumors or negative claims they spread     |
| 5. Proof Point             | Specific customer quote who migrated from them to us |
+-----------------------------------------------------------------------------------+
```

*See [references/competitor-intel-brief.md](references/competitor-intel-brief.md).*

---

## Economic Moat Analysis (Hamilton Helmer's 7 Powers)

Evaluate long-term defensibility against commoditization:

- **Network Effects**: Value increases quadratically with user adoption.
- **Switching Costs**: High operational or data friction to migrate away.
- **Scale Economies**: Decreasing marginal costs allowing aggressive pricing.
- **Counter-Positioning**: Business model incumbents cannot copy without cannibalization.
- **Branded Authority**: Deep trust and reputation reducing customer acquisition costs.
- **Cornered Resource**: Exclusive access to proprietary data, patents, or talent.
- **Process Power**: Embedded operational speed and organizational efficiency.

*See [references/competitive-moats.md](references/competitive-moats.md).*

---

## Competitive Review Checklist

```
RESEARCH COMPLETENESS:
□ Pricing page and tier structures verified within the last 30 days
□ G2/Capterra reviews analyzed for recurring 1-star and 2-star patterns
□ SEO footprint and organic keyword share assessed via Semrush data
□ Messaging audited across homepage, ad copies, and sales collateral

STRATEGIC INTEGRITY:
□ Battlecard avoids petty disparagement; focuses on structural trade-offs
□ Unique mechanism and defensible moats clearly distinguished from competitor
□ Clear landmines defined for sales reps to plant early in discovery calls
```

---

## Reference Materials

The following in-depth guides are bundled in the `references/` directory:

- **[competitor-analysis.md](references/competitor-analysis.md)** — Comprehensive market landscape mapping and intelligence gathering.
- **[competitor-teardown.md](references/competitor-teardown.md)** — Step-by-step framework for reverse-engineering rival products and funnels.
- **[competitor-page-teardown.md](references/competitor-page-teardown.md)** — Desmontar a página de um concorrente (proposta de valor, hierarquia de mensagem, nota de 100 pontos). Veio de `ads-criativos`.
- **[competitor-intel-brief.md](references/competitor-intel-brief.md)** — Standardized intelligence brief template for executive and sales teams.
- **[competitor-monitor.md](references/competitor-monitor.md)** — Ongoing competitive tracking, alert triggers, and change detection.
- **[competitive-moats.md](references/competitive-moats.md)** — Strategic defensibility evaluation using the 7 Powers and moat frameworks.
- **[competitor-alternatives.md](references/competitor-alternatives.md)** — High-converting comparison page architecture ("Best Alternatives to X"). Traz também os modelos de seção, os dados centralizados de concorrentes, as páginas-índice e a navegação do rodapé.
- **[semrush-research.md](references/semrush-research.md)** — Organic and paid competitive data extraction workflows.
- **[semrush.md](references/semrush.md)** — Quick reference for competitive search metrics and domain comparison.

---

## Related Skills

- **`revenue-gtm-e-posicionamento`** — Category design, market positioning, and Value Proposition Canvas.
- **`persona-icp`** — Audience research, pain points, and decision criteria.
- **`copy-conversao`** — Writing persuasive comparison pages, battlecards, and sales copy.

## Roteiros guiados (vindos do kit AgentKits)

Roteiros que fazem perguntas ao usuário antes de entregar. O texto base é inglês.

- **[market.md](references/market.md)** — Roteiro guiado de pesquisa de mercado.
- **[trend.md](references/trend.md)** — Roteiro guiado de análise de tendências do setor e do mercado.

## Outras referências

- **[battlecard-template.md](references/battlecard-template.md)** — Modelo de battlecard competitivo.
- **[brand-monitor-api.md](references/brand-monitor-api.md)** — Monitoramento de menções à marca pela API Brand.dev; requer a API.
- **[domain-research.md](references/domain-research.md)** — Pesquisa de dados WHOIS de domínios e listagens em marketplaces; requer a API.
- **[gap-analysis-frameworks.md](references/gap-analysis-frameworks.md)** — Frameworks de análise de lacunas.

## Scripts de cálculo

Dois programas em Python escritos em 2026-11-03 (ver [THIRD_PARTY_NOTICE.md](scripts/THIRD_PARTY_NOTICE.md) — nenhum dos dois tinha origem real, eram citação fantasma em `/revenue-estrategia-pmm`). Rode a partir da raiz do projeto, com o ambiente `.venv` (precisa só de `click`):

```bash
# Snapshot e diff de página de concorrente (preço, mensagem) — complementa o roteiro manual de competitor-monitor.md
.venv/bin/python .agent/skills/revenue-inteligencia-competitiva/scripts/competitor_tracker.py snapshot --url https://concorrente.com/precos --name acme
.venv/bin/python .agent/skills/revenue-inteligencia-competitiva/scripts/competitor_tracker.py diff --name acme
.venv/bin/python .agent/skills/revenue-inteligencia-competitiva/scripts/competitor_tracker.py check-all --config competidores.json

# Win/loss: taxa de vitória por competidor, segmento e faixa de tamanho de negócio, com teste de significância
.venv/bin/python .agent/skills/revenue-inteligencia-competitiva/scripts/win_loss_analyzer.py analyze --file negocios.csv
```

- `competitor_tracker.py` só lê HTML estático via HTTP (sem navegador headless) — página montada por JavaScript no cliente não aparece de verdade; use o roteiro de [competitor-monitor.md](references/competitor-monitor.md) nesse caso.
- `win_loss_analyzer.py` espera um CSV com colunas `deal_id,outcome,reason,competitor,segment,deal_size,close_date` (`outcome` = `won`/`lost`); o teste de significância usa a mesma fórmula de duas proporções do script de [`growth-testes-ab`](../growth-testes-ab/SKILL.md), só marca diferença como significativa com 5 ou mais negócios no grupo.
