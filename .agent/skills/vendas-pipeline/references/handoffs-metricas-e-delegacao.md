# Passagens de bastão, perdas, métricas e delegação a agentes

> **Origem:** absorvido da skill `sales-workflow` em 2026-10-19 (loop "Auditoria e Deduplicação de Skills", cluster C5). A skill original completa está em `.agent/skills/_arquivo/mescladas/sales-workflow/`.
>
> **Quando abrir este arquivo:** (1) definir o pacote e o prazo de passagem de **Vendas para Sucesso do Cliente** depois do fechamento; (2) registrar um negócio perdido com campos padronizados; (3) montar os indicadores de atividade, pipeline e resultado de vendas; (4) saber qual agente do projeto aciona cada tarefa comercial.
>
> **O que NÃO está aqui, de propósito:** as sequências de outreach (estão na `vendas-cold-email`), a estrutura de pitch deck (`audiovisual-pitch-deck`), os scripts de objeção (`objection-mapping.md`, na skill `vendas-materiais-de-venda`), o modelo de battlecard (`revenue-inteligencia-competitiva`), a tabela de temperatura do lead e os sinais de intenção (`lead-scoring.md` e `vendas-crm`), e a passagem de Marketing para Vendas com o prazo de MQL para SQL (`revops.md`). Todos já existem nesses lugares.
>
> **Aviso:** o texto abaixo veio do kit original, em inglês e sem revisão. Os prazos (SLA) e as metas das tabelas são exemplos, não referência validada.

---

## Handoff Protocols

### Sales → Customer Success (Closed Won)

**Trigger:** Contract signed

**Handoff Package:**
- Deal summary + pricing
- Key stakeholders + communication preferences
- Implementation requirements
- Success metrics agreed
- Any promises made during sales

**SLA:** Success contacts within 48 hours

### Lost Deal Analysis

**Required Fields:**
- Primary loss reason (competitor, price, timing, no decision, other)
- Competitor won (if applicable)
- What could we have done differently
- Re-engage date (3/6/12 months)
- Learnings for team

## Sales Metrics & KPIs

### Activity Metrics (Daily/Weekly)
| Metric | Target | Frequency |
|--------|--------|-----------|
| Calls made | 50+/day | Daily |
| Emails sent | 30+/day | Daily |
| Meetings booked | 10+/week | Weekly |
| Proposals sent | 5+/week | Weekly |

### Pipeline Metrics
| Metric | Target | Notes |
|--------|--------|-------|
| Pipeline value | 3x quota | Coverage ratio |
| Stage conversion | Track by stage | Identify bottlenecks |
| Average deal size | Track trend | Upsell opportunities |
| Sales cycle length | Reduce over time | Efficiency |

### Outcome Metrics
| Metric | Calculation | Target |
|--------|-------------|--------|
| Win rate | Closed Won / Total Opps | >25% |
| Revenue closed | Total closed revenue | Quota |
| CAC | Sales cost / New customers | Reduce |
| LTV:CAC ratio | Lifetime value / CAC | >3:1 |

## Agent Delegation

| Task | Agent | Trigger |
|------|-------|---------|
| Lead research | `researcher` | New lead assigned |
| Lead scoring | `lead-qualifier` | New lead or engagement |
| Prospect company analysis | `researcher` | Pre-call prep |
| Lead generation | `attraction-specialist` | Pipeline building |
| Pitch customization | `sales-enabler` | Meeting scheduled |
| Objection scripts | `sales-enabler` | Post-call request |
| Case study matching | `sales-enabler` | Industry/use case match |
| Proposal generation | `copywriter` | Deal at proposal stage |
| Follow-up sequences | `email-wizard` | Post-meeting |
| Lost deal analysis | `researcher` | Deal marked lost |
| Competitive intel | `researcher` | Competitor mentioned |
