---
# Source: https://github.com/clawdb
# Repository: https://github.com/Felipelbahia/superiaprojects-marketing
# Status: Customizada / Modificada localmente por Felipe Bahia
name: revenue-preco
description: "Use para definir preço e pacotes de SaaS e produto digital: preço por valor, pesquisa de preço (Van Westendorp, MaxDiff), planos Good-Better-Best, freemium vs teste grátis, validação de disposição a pagar, quando subir preço e preço enterprise. Gatilhos: \"quanto cobrar\", \"planos e preços\", \"página de preços\", \"freemium\", \"aumentar preço\". NÃO use para montar oferta, bônus e garantia (use revenue-oferta) nem para rodar teste A/B de preço (use growth-testes-ab)."
author: ClawFu, aaron-he-zhu & Antigravity Kit & Felipe Bahia (Futuro Mercado)
license: MIT
metadata:
  author: ClawFu, aaron-he-zhu & Antigravity Kit & Felipe Bahia (Futuro Mercado)
  version: 1.0.0
complements: revenue-gtm-e-posicionamento, persona-icp, copy-conversao
---
# Pricing Strategist & Monetization Architect

> Architect, validate, and optimize monetization models for SaaS and digital products. Design value-based pricing tiers, determine willingness-to-pay using econometric models (Van Westendorp, Gabor-Granger), select defensible value metrics, and engineer expansion loops that drive Net Revenue Retention (NRR).

## When to Use This Skill

Use this skill when you need to:

- **Design or overhaul SaaS pricing tiers** (Good-Better-Best packaging architecture)
- **Select the optimal value metric** (per-seat, usage-based, tiered volume, or hybrid)
- **Measure customer willingness-to-pay** using the Van Westendorp Price Sensitivity Meter
- **Decide between Freemium, Free Trial, and Reverse Trial** for product-led growth (PLG)
- **Identify feature gating thresholds** (what belongs in self-serve vs enterprise tiers)
- **Plan and communicate price increases** without triggering customer revolt or mass churn

---

## 3 Core Pricing Philosophies

```
+-----------------------------------------------------------------------------------+
| METHODOLOGY         | DEFINITION                      | STRATEGIC VERDICT         |
+---------------------+---------------------------------+---------------------------+
| 1. Cost-Plus        | Unit cost + target profit margin| Obsolete for software     |
| 2. Competitor-Based | Pegged to rival market rates    | Leaves money on the table |
| 3. Value-Based      | Pegged to ROI / customer outcome| Gold standard for SaaS/B2B|
+-----------------------------------------------------------------------------------+
```

Value-based pricing aligns your price with the economic value delivered to the buyer. If your software saves a company $100,000/year in labor or generates $200,000 in new revenue, charging $10,000-$20,000 (10-20% of value created) is an easy commercial ROI justification.

*See [references/pricing-strategy.md](references/pricing-strategy.md) and [references/saas-pricing-guide.md](references/saas-pricing-guide.md).*

---

## The Van Westendorp Price Sensitivity Meter

When surveying prospects to establish acceptable pricing corridors, ask 4 precise questions:

1. **Too Cheap**: *"At what price would this software feel so cheap that you would question its quality and reliability?"*
2. **Bargain**: *"At what price would this feel like a great deal—a bargain you'd purchase immediately?"*
3. **Getting Expensive**: *"At what price would this begin to feel expensive, requiring serious thought before buying?"*
4. **Too Expensive**: *"At what price is this so expensive that you would refuse to consider it, no matter how good it is?"*

```
              POINT OF MARGINAL CHEAPNESS (PMC)    POINT OF MARGINAL EXPENSIVENESS (PME)
                            ▼                                     ▼
[ Too Cheap Line ] ─────────┼─────── [ OPTIMAL PRICE POINT (OPP) ] ───────┼── [ Too Expensive Line ]
                                                 ▲
                                     INDIFFERENCE PRICE POINT (IPP)
```

The intersection of these four cumulative distributions defines the **Acceptable Price Range** and the mathematically **Optimal Price Point (OPP)**.

*See [references/pricing-validation.md](references/pricing-validation.md).*

---

## The "Good-Better-Best" (3-Tier) Packaging Blueprint

```
+-----------------------------------------------------------------------------------+
| TIER               | TARGET ICP            | PURPOSE / PSYCHOLOGY                 |
+--------------------+-----------------------+--------------------------------------+
| 1. Starter (Good)  | Solopreneur / Early   | Low-friction entry; anchors the base |
| 2. Pro (Better)    | Growth Team / Mid-Tier| The Hero Tier (60-70% of target users)|
| 3. Scale (Best)    | Established / Enterprise| High-margin anchor; makes Pro look a deal|
+-----------------------------------------------------------------------------------+
```

### Feature Gating Rules:
- **Table Stakes (All Tiers)**: Core utility required to experience the "Aha!" moment.
- **Value Differentiators (Better/Best)**: Higher limits, automation, advanced reporting, integrations.
- **Enterprise Gates (Best Only)**: SAML/SSO, audit logs, custom role-based access control (RBAC), SLA guarantees, dedicated customer success manager.

*See the "Tier Structure", "Packaging for Personas", "Freemium vs. Free Trial" and "Enterprise Pricing" sections of [references/pricing-strategy.md](references/pricing-strategy.md).*

---

## Value Metric Selection Framework

The value metric is the unit of consumption that drives pricing increases as the customer grows.

A great value metric must satisfy 3 conditions:
1. **Direct Correlation to Value**: As the customer gets more value, consumption naturally increases.
2. **Predictable & Transparent**: The customer can easily budget and understand their bill.
3. **Low Friction to Start**: Doesn't penalize early adoption or onboarding of new team members.

*Examples: Active contacts (Email), Monthly Tracked Users (Analytics), Monitored Endpoints (DevOps), Total Revenue Processed (Fintech).*

---

## Pricing Launch & Validation Checklist

```
MONETIZATION RIGOR:
□ Value metric scales linearly with customer success (no perverse disincentives)
□ Hero tier clearly designated visually (e.g. "Most Popular" badge + higher visual contrast)
□ Annual discount incentive calibrated (typically 15-20% discount or "2 months free")
□ Price tested with Van Westendorp or Gabor-Granger quantitative survey data

TRANSPARENCY & FRICTION:
□ Self-serve checkout enabled for Starter and Pro tiers (no mandatory sales calls)
□ Overage policy clearly defined (grace periods vs hard stops vs automatic tier upgrades)
□ FAQ section tackles the top 3 billing questions (refund policy, upgrades, cancellations)
```

---

## Reference Materials

The following in-depth guides are bundled in the `references/` directory:

- **[pricing-strategy.md](references/pricing-strategy.md)** — Comprehensive SaaS monetization frameworks, packaging, and unit economics.
- **[pricing-validation.md](references/pricing-validation.md)** — Van Westendorp, Gabor-Granger, and conjoint analysis survey methodologies.
- **[saas-pricing-guide.md](references/saas-pricing-guide.md)** — Tactical guide to value metrics, annual billing, and discount governance.
- **[roteiro-guiado-preco.md](references/roteiro-guiado-preco.md)** — Roteiro guiado do kit AgentKits (veio de `revenue-gtm-e-posicionamento`, 2026-10-20): faz perguntas e entrega preço, empacotamento e estratégia de monetização. Texto base em inglês.

---

## Related Skills

- **`revenue-gtm-e-posicionamento`** — Category positioning, value propositions, and market segmentation.
- **`persona-icp`** — Customer budget thresholds and purchasing authority mapping.
- **`copy-conversao`** — Writing high-converting pricing page copy, guarantee policies, and checkout microcopy.

## Onde estão os outros assuntos

- Planos Good-Better-Best, pacotes por persona, freemium vs teste grátis, preço enterprise e métodos de pesquisa de preço (Van Westendorp, MaxDiff) são capítulos de [pricing-strategy.md](references/pricing-strategy.md). Os arquivos soltos `tier-structure` e `pricing-research-methods` repetiam esses capítulos e estão em `_arquivo/mescladas/r17-produto/pricing-strategist/`.
