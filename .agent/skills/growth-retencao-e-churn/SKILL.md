---
# Repository: https://github.com/Felipelbahia/superiaprojects-marketing
# Status: Customizada / Modificada localmente por Felipe Bahia
name: growth-retencao-e-churn
description: "Engineer high-converting retention engines, cancel flows, dynamic save offers, exit surveys, and dunning systems to slash voluntary and involuntary subscription churn. Also covers customer health scoring, churn prediction, expansion (upsell) signals, QBR (revisão trimestral) e renovação de contrato. NÃO use para estágios do contato e lead scoring no CRM (use vendas-crm) nem para atribuição de marketing (use data-atribuicao-e-relatorios)."
author: Antigravity Kit & Felipe Bahia (Futuro Mercado)
license: MIT
metadata:
  author: Antigravity Kit & Felipe Bahia (Futuro Mercado)
  version: 1.0.0
complements: copy-conversao, revenue-preco, revenue-gtm-e-posicionamento, revenue-oferta
---
# Retention & Churn Strategist

> Systematic retention architecture to protect recurring revenue. Diagnoses drop-offs, designs empathetic and high-converting cancellation flows, configures intelligent save offers, and recovers 50-60% of failed payments through automated dunning cadences.

## When to Use This Skill

Use this skill when you need to:

- **Audit and diagnose subscription churn** (separating voluntary cancellations from involuntary payment failures)
- **Design self-serve and high-touch cancellation flows** with multi-step save logic
- **Create dynamic save offers** mapped to specific exit survey reasons (pauses, discounts, plan downgrades, coaching)
- **Implement automated dunning sequences** to recover failed credit card transactions and card expirations
- **Define customer lifecycle stages and health scores** to prevent churn before it reaches the cancellation screen
- **Draft empathetic offboarding and post-cancel win-back communications**

---

## The Dual-Engine Churn Model

Subscription churn stems from two fundamentally different root causes that require isolated playbooks:

```
+-----------------------------------------------------------------------------------------+
| CHURN TYPE         | ROOT CAUSE                         | PRIMARY REMEDIATION ENGINE     |
+--------------------+------------------------------------+--------------------------------+
| Voluntary Churn    | Customer actively clicks to cancel | - Dynamic multi-step cancel flow|
| (50-70% of total)  | (Value gap, price, lack of usage)  | - Contextual save offers & pause|
|                    |                                    | - Actionable exit survey       |
+--------------------+------------------------------------+--------------------------------+
| Involuntary Churn  | Technical payment processing fail  | - Pre-dunning expiration alerts|
| (30-50% of total)  | (Card expired, limit, bank decline)| - Smart retry cadence & updater|
|                    |                                    | - 4-part urgent dunning emails |
+-----------------------------------------------------------------------------------------+
```

*See [references/churn-prevention.md](references/churn-prevention.md).*

---

## 1. Cancel Flow Architecture (Voluntary Churn)

A world-class cancel flow does not trap the user; it seeks to understand friction, re-anchors core value, and presents low-friction alternatives to complete termination.

### 4-Step Self-Serve Flow Pattern

```
[Cancel Trigger] 
       │
       ▼
[Step 1: Contextual Exit Survey] ──► Categorize reason (Price, Bugs, Inactivity, Competitor)
       │
       ▼
[Step 2: Dynamic Save Offer]     ──► Tailored incentive matching the stated reason
       │
       ├── Accept Offer ──────────► [Retention Confirmed + Event Tracked]
       │
       ▼ Decline
[Step 3: Value Loss & Confirm]   ──► Display lost data, team seats, or grandfathered pricing
       │
       ▼
[Step 4: Graceful Offboarding]   ──► Confirm access end date + Zero-friction feedback loop
```

### Save Offer Decision Matrix

| Exit Survey Reason | Tier 1 Save Offer | Tier 2 Fallback Save |
|---|---|---|
| **"Too expensive / Budget"** | 25-50% discount for 2-3 months | Downgrade to lower-tier starter plan |
| **"Not using it enough / Seasonal"** | 1 to 3 months account freeze/pause | Switch to free/dormant tier preserving data |
| **"Missing features / Technical bug"** | Direct 1-on-1 support / VIP roadmap pass | Priority bug escalation + account extension |
| **"Switched to competitor"** | Feature parity walkthrough | Offer price-match or migration assistance |
| **"Finished my project"** | Pause plan until next launch | Archive mode preserving workspaces |

*See [references/cancel-flow-patterns.md](references/cancel-flow-patterns.md).*

---

## 2. Involuntary Churn & Dunning Recovery Cadence

Failed credit card transactions account for up to half of all SaaS churn. Execute this structured 14-day dunning sequence to maximize recovery:

### Pre-Dunning (T-30 to T-7 Days)
- **Card Expiration Alerts:** Trigger automated email and in-app banner 30 days and 7 days prior to card expiration date.
- **Direct Card Update Link:** Send an authenticated, 1-click update link (avoid forcing complex login passwords during payment failure).

### Post-Failure Recovery Schedule

```
Day 0:  Payment fails ──► Smart retry #1 (immediate) + Friendly email notification
Day 2:  Retry #2      ──► In-app persistent banner: "Payment declined — update card"
Day 5:  Retry #3      ──► Email #2: "Urgent: We couldn't process your payment"
Day 7:  Retry #4      ──► Email #3: "Your account is scheduled for deactivation"
Day 10: Final retry   ──► Email #4: Final warning from customer success
Day 14: Grace ends    ──► Account soft-paused (data preserved for win-back)
```

*See [references/dunning-playbook.md](references/dunning-playbook.md).*

---

## 3. Customer Lifecycle & Health Scoring

Intervening only at the cancellation screen is already too late. Track health scores across customer lifecycle milestones:

1. **Onboarding (Days 1–14):** Measure time-to-first-value (Aha! moment). Flag accounts without key setup completions.
2. **Adoption (Days 15–60):** Monitor weekly active frequency and core workflow completions. Trigger proactive outreach on 30% drop in 14-day usage.
3. **Maturity (Days 61+):** Track seat expansion, API usage, and champion stability.
4. **Pre-Churn Warning Indicators:**
   - Sudden drop in weekly logins
   - Removal of team members
   - Exporting large volumes of CSV/data
   - Visits to the billing or cancellation page

*See [references/lifecycle-definitions.md](references/lifecycle-definitions.md).*

---

## Practical Execution Checklist

- [ ] Calculate current net churn vs gross churn (MRR churn vs logo churn)
- [ ] Implement an exit survey with mutually exclusive, actionable cancellation categories
- [ ] Configure dynamic save offers mapped 1:1 to user responses
- [ ] Add an account pause / holiday mode (1 to 3 months) before hard cancel
- [ ] Integrate automated dunning retries (Stripe Smart Retries or custom logic)
- [ ] Build in-app payment failure warning banners
- [ ] Craft a 3-part post-cancel win-back email sequence (Day 15, Day 45, Day 90)

---

## Detailed References

- [references/churn-prevention.md](references/churn-prevention.md) — Comprehensive retention playbooks and benchmarks
- [references/cancel-flow-patterns.md](references/cancel-flow-patterns.md) — UI/UX patterns for B2B, B2C, and mobile cancel flows
- [references/dunning-playbook.md](references/dunning-playbook.md) — Dunning timelines, email templates, and retry configurations
- [references/lifecycle-definitions.md](references/lifecycle-definitions.md) — Customer journey mapping, health scoring, and churn cohort analysis

## Saúde de clientes e expansão

O texto base é inglês.

- [references/account-health.md](references/account-health.md) — Pontuação de saúde da conta com uso do produto, sentimento do suporte e pagamento.
- [references/health-score-monitor.md](references/health-score-monitor.md) — Montar e manter o sistema de pontuação de saúde, com alertas automáticos.
- [references/churn-prediction.md](references/churn-prediction.md) — Identificar clientes em risco por sinais de comportamento e engajamento.
- [references/expansion-signals.md](references/expansion-signals.md) — Achar oportunidades de upsell e cross-sell por padrões de uso.
- [references/qbr-preparation.md](references/qbr-preparation.md) — Preparar a revisão trimestral (QBR) com resumo da conta, métricas de sucesso, desafios e recomendações. Veio de `vendas-pipeline` (2026-10-20).
- [references/renewal-management.md](references/renewal-management.md) — Conduzir a renovação com playbooks por saúde da conta, prazos e mitigação de risco. Veio de `vendas-pipeline` (2026-10-20).
