---
name: persona-icp
description: "Use para construir personas, perfil de cliente ideal (ICP), mapa de Jobs-to-be-Done, gatilhos de compra, roteiros de voz do cliente, pesquisa de público e pontuação de aderência ao ICP. Gatilhos: \"persona\", \"ICP\", \"cliente ideal\", \"JTBD\", \"segmentar público\". NÃO use para validar hipótese de produto com entrevistas (use persona-descoberta-de-clientes), analisar saturação de público em anúncios (use ads-analise-de-desempenho) nem montar cadência de prospecção (use vendas-cold-email)."
license: MIT
metadata:
  author: ClawFu, aaron-he-zhu & Antigravity Kit & Felipe Bahia (Futuro Mercado)
  version: 1.0.0
complements: revenue-gtm-e-posicionamento, copy-conversao, discovery-interviews-surveys
---

# Buyer Persona & ICP Architect

> Construct deeply researched, commercially actionable buyer personas and Ideal Customer Profiles (ICPs). Uncover the Jobs-to-be-Done (JTBD), emotional triggers, internal frustrations, and decision criteria that drive purchase velocity.

## When to Use This Skill

Use this skill when you need to:

- **Define a crystal-clear Ideal Customer Profile (ICP)** for B2B or B2C go-to-market motions
- **Construct detailed buyer personas** for founders, product marketing, copywriters, and sales teams
- **Map the Jobs-to-be-Done (JTBD)** across functional, emotional, and social dimensions
- **Conduct Voice-of-Customer (VoC) research** and synthesize user interviews into pain matrices
- **Identify high-intent purchase triggers** (funding events, leadership changes, metric drops, tool deprecations)
- **Scan audience saturation** and calculate realistic addressable market segments

---

## B2B ICP vs Buyer Persona Matrix

A complete customer intelligence model separates the company profile from the human buyer:

```
+-----------------------------------------------------------------------------------+
| DIMENSION           | IDEAL CUSTOMER PROFILE (COMPANY) | BUYER PERSONA (HUMAN)    |
+---------------------+----------------------------------+--------------------------+
| Scope               | Firmographics & Tech Stack       | Psychographics & Fears   |
| Core Questions      | What kind of company buys this?  | Who signs the contract?  |
| Attributes          | Revenue, Team Size, Tech Stack,  | Job Title, KPIs, Pains,  |
|                     | Industry, Growth Rate, Geography | Objections, Career Goals |
| Decision Role       | Target Account Qualification     | Messaging & Copy Angle   |
+-----------------------------------------------------------------------------------+
```

*See [references/buyer-personas.md](references/buyer-personas.md) and [references/persona-generator.md](references/persona-generator.md).*

---

## The Jobs-to-be-Done (JTBD) & 4 Forces Framework

Customers do not buy products; they "hire" products to make progress in their lives:

```
                          PUSH OF PRESENT PAIN
                    (Frustration with current tools)
                                   ▼
             HABIT & INERTIA ──► [DECISION GATE] ◄── PULL OF NEW SOLUTION
             (Fear of change)              ▲         (Promise of better outcome)
                                           │
                                 ANXIETY OF THE NEW
                         (Will it fail? Is it risky?)
```

### The 3 Dimensions of Every Job:
1. **Functional Job**: The core objective task (e.g. *"Generate monthly financial reports automatically"*).
2. **Emotional Job**: Personal peace of mind (e.g. *"Stop feeling terrified that an Excel formula broke"*).
3. **Social Job**: Peer and executive perception (e.g. *"Look like a modern, data-driven VP of Finance to the board"*).

*See [references/persona-generator.md](references/persona-generator.md).*

---

## 10-Question Customer Discovery Script

When conducting 1-on-1 interviews to extract unfiltered voice-of-customer data:

1. *"Take me back to the day you first realized you needed to solve this problem. What happened?"*
2. *"What were you doing before to manage this? What broke or stopped working?"*
3. *"What other solutions or workarounds did you try before finding us?"*
4. *"What was the single most frustrating part about those previous alternatives?"*
5. *"When you were evaluating our solution, what almost stopped you from buying?"*
6. *"How did you justify the cost and effort of switching to your boss or team?"*
7. *"What is the single biggest difference in your daily work now compared to before?"*
8. *"What metric or KPI did this directly impact for your business?"*
9. *"How would you describe what we do to a peer in your industry over coffee?"*
10. *"If you lost access to this tool tomorrow, what would you have to do?"*

*See [references/audience-research.md](references/audience-research.md).*

---

## Persona Actionability Checklist

```
GROUNDED RIGOR:
□ Persona based on real qualitative interviews or customer reviews (not generic guesses)
□ Specific quotes captured in the customer's exact conversational vocabulary (VoC)
□ Pain points quantified (e.g. "wastes 6 hours/week on manual data entry", not "busy")

COMMERCIAL ACTIONABILITY:
□ Primary buying trigger identified (the catalytic event that forces urgent action)
□ Top 3 purchase objections and corresponding counter-arguments documented
□ Specific watering holes mapped (subreddits, podcasts, newsletters, conferences they consume)
□ Negative persona defined (who NOT to target because they churn or create support drag)
```

*See [references/audience-research.md](references/audience-research.md) and [references/segment.md](references/segment.md).*

---

## Reference Materials

The following in-depth guides are bundled in the `references/` directory:

- **[persona-generator.md](references/persona-generator.md)** — Comprehensive persona construction framework and data gathering guide.
- **[buyer-personas.md](references/buyer-personas.md)** — B2B vs B2C persona modeling templates and behavioral categorization.
- **[audience-research.md](references/audience-research.md)** — Qualitative and quantitative customer research methodology.
- **[segment.md](references/segment.md)** — Create or analyze a customer segment (command-style guide).

---

## Related Skills

- **`revenue-gtm-e-posicionamento`** — Value Proposition Canvas and positioning matching the persona.
- **`copy-conversao`** — Crafting targeted sales copy in the persona's authentic voice.
- **`discovery-interviews-surveys`** — Interview guides and qualitative data synthesis.

## Roteiros guiados (vindos do kit AgentKits)

Roteiros que fazem perguntas ao usuário antes de entregar. O texto base é inglês.

- **[segment.md](references/segment.md)** — Roteiro guiado para criar ou analisar um segmento de clientes.

## Outras referências

- **[google-meta-icp-research.md](references/google-meta-icp-research.md)** — Personas B2B detalhadas: dores, objeções, gatilhos de compra e canais, para Google e Meta.

## Referências vindas de outras skills

- **[icp-builder.md](references/icp-builder.md)** — Framework de construção de Perfil de Cliente Ideal em 4 dimensões (Firmeográfica, Tecnológica, Comportamental e Gatilhos).
- **[icp-matching.md](references/icp-matching.md)** — Algoritmo de cruzamento e pontuação para identificar se uma conta possui fit elevado com o produto.
