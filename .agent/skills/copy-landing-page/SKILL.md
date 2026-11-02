---
name: copy-landing-page
description: "Design, write, and optimize high-converting landing pages. Section-by-section copywriting architecture (Hero, Problem, Solution, Features/Benefits, Social Proof, Objection Killing, Risk Reversal, FAQ, Final CTA) and CRO diagnostic audits. NÃO use para posicionamento e pesquisa de voz do cliente (use copy-saas), para cartas de venda e persuasão de resposta direta (use copy-conversao), para auditar a conversão de uma página pronta (use site-cro), para desenhar a interface (use site-interface-de-conversao), para isca digital e portão de e-mail (use conteudo-estrategia) nem para roteiro de VSL (use copy-vsl)."
license: MIT
metadata:
  author: ClawFu, aaron-he-zhu & Antigravity Kit & Felipe Bahia (Futuro Mercado)
  version: 1.0.0
complements: copy-conversao, copy-saas, site-cro, geral-anti-slop
---

# Landing Page Copywriter & CRO Architect

> Architect, write, and optimize high-converting landing pages. From attention-grabbing hero sections to frictionless checkout paths, this skill guides section-by-section wireframing, message-to-market matching, and conversion rate optimization (CRO).

## When to Use This Skill

Use this skill when you need to:

- **Write a complete landing page from scratch** (SaaS, lead generation, product sales, or event registration)
- **Optimize an underperforming page** to diagnose conversion friction, bounce rates, and drop-offs
- **Structure hero sections** with clear value propositions, subheadlines, and click triggers
- **Build persuasive social proof sections** using metrics, customer quotes, and case studies
- **Neutralize prospect hesitation** through targeted objection-killing FAQs and risk reversal
- **Audit page conversion health** against standardized CRO rubrics and mobile usability heuristics

---

## The 8-Block Landing Page Architecture

Every high-converting landing page follows a deliberate psychological progression:

```
+-----------------------------------------------------------------------------------+
| 1. HERO SECTION        Headline + Subhead + Primary CTA + Hero Visual + Microproof|
+-----------------------------------------------------------------------------------+
| 2. PROBLEM & AGITATION External frustration + internal pain point + cost of inaction|
+-----------------------------------------------------------------------------------+
| 3. UNIQUE MECHANISM    How the solution works differently (proprietary system)   |
+-----------------------------------------------------------------------------------+
| 4. OUTCOME & BENEFITS  Features translated into emotional and financial results  |
+-----------------------------------------------------------------------------------+
| 5. SOCIAL PROOF STACK  Customer logos + quantifiable metrics + relatable stories  |
+-----------------------------------------------------------------------------------+
| 6. OBJECTION KILLER    Addressing the top 5 doubts before the prospect leaves     |
+-----------------------------------------------------------------------------------+
| 7. RISK REVERSAL       Ironclad guarantee + transparent pricing + bonuses         |
+-----------------------------------------------------------------------------------+
| 8. CLOSING ARGUMENT    Final CTA + summary of transformation + click reassurance |
+-----------------------------------------------------------------------------------+
```

---

## Detailed Section Guidelines

### 1. The Hero Section (Above the Fold)
- **Primary Headline (H1)**: Max 10-12 words. Focuses on the primary transformation or ultimate benefit. Answers: *"What is this and what will it do for me?"*
- **Subheadline**: 1-2 sentences clarifying the target audience, the mechanism, and how it delivers on the H1 promise.
- **Primary CTA**: High-contrast button with value-first copy (e.g. *"Start Free 14-Day Trial"* or *"Get My Free Strategy Audit"*).
- **Click Triggers**: Microcopy immediately adjacent to the button (e.g. *"No credit card required • 2-minute setup"*).
- **Hero Visual**: Product UI mockup, video explainer, or authentic visual proof showing the product in action.

*See [references/landing-page-copy.md](references/landing-page-copy.md) and [references/write-landing.md](references/write-landing.md).*

---

### 2. Social Proof & Authority Stacking
Social proof must be believable, relatable, and specific:
- **Logo Bars**: High-recognition customer or client logos ("Trusted by over 500+ teams").
- **Quantitative Metrics**: Specific numbers rather than generic claims (*"Saved 14.2 hours per week"* beats *"Save time"*).
- **Case Testimonials**: Photo + Full Name + Role/Company + Contextual before/after quote.

---

### 3. Objection Killing & FAQ Architecture
Don't use FAQs for trivial logistics; use them to eliminate the 5 universal purchase blockers:
1. **Time / Complexity**: *"How long does it take to see results?"*
2. **Compatibility**: *"Will this integrate with my existing tech stack?"*
3. **Risk / Cost**: *"What happens if it doesn't work for my specific case?"*
4. **Effort**: *"How much hands-on time does my team need to invest?"*
5. **Alternative Comparison**: *"How is this different from existing solutions X and Y?"*

*See [references/landing-page-optimizer.md](references/landing-page-optimizer.md).*

---

## CRO Health Check & Diagnostic Rubric

```
HERO CLARITY:
□ Value proposition passes the 5-second test (is it immediately obvious what this is?)
□ Headline is benefit-led rather than feature-led
□ Single primary CTA with clear visual hierarchy above the fold

MESSAGE & SCROLL FLOW:
□ Problem is validated before solution is introduced
□ Subheads tell a coherent story when skimmers scroll the page
□ No walls of text (paragraphs limited to 2-3 lines on desktop, 3-4 on mobile)

CONVERSION INTEGRITY:
□ Clear social proof visible within the first two screen scrolls
□ Risk reversal (guarantee, trial, or free sample) clearly articulated
□ Form fields minimized to strictly necessary inputs (each extra field drops conversion ~10%)
□ Checked against geral-anti-slop: zero robotic jargon or empty buzzwords
```


---

## Reference Materials

The following in-depth guides are bundled in the `references/` directory:

- **[landing-page-copy.md](references/landing-page-copy.md)** — Exhaustive landing page copywriting manual covering all 8 blocks.
- **[landing-page-optimizer.md](references/landing-page-optimizer.md)** — Conversion rate optimization, heatmaps, and A/B test hypotheses.
- **[write-landing.md](references/write-landing.md)** — Process, 4 page frameworks, section copy **with Tailwind/React code**, SEO and output format. The only guide that produces code: it needs the explicit-authorization gate (rule 1.5); to deliver the whole page use the workflow [site-construcao-de-landing-page](../../workflows/site-construcao-de-landing-page.md).

---

## Related Skills

- **`copy-conversao`** — Direct response persuasion, headline formulas, and psychological levers.
- **`copy-saas`** — Dedicated SaaS positioning, messaging, and ICP problem-mapping.
- **`site-cro`** — Conversion audit of a finished page (scored, ad × page match, forms, popups).
- **`site-interface-de-conversao`** — Visual design, layout, contrast and accessibility.
- **`geral-anti-slop`** — Mandatory verification to strip generic synthetic copy.

## Para onde foram os outros assuntos

- **Isca digital (lead magnet), portão de e-mail e entrega:** [conteudo-estrategia](../conteudo-estrategia/references/lead-magnet.md).
- Arquivados em `.agent/skills/_arquivo/mescladas/r16b-design/landing-page-copywriter/`: `landing.md` (comando do kit) e o modelo de vigia de LPs `clawdbot-landing-page-health-check.md` (sem ferramenta; se você quiser vigiar LPs, recriar com `/schedule`).
- O checklist de validação da apresentação educativa (`validation.md`) voltou para [audiovisual-pitch-deck](../audiovisual-pitch-deck/SKILL.md), a que ele pertence.
