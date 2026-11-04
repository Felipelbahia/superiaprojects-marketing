---
# Repository: https://github.com/Felipelbahia/superiaprojects-marketing
# Status: Customizada / Modificada localmente por Felipe Bahia
name: growth-indicacao-e-afiliados
description: "Use para desenhar programa de indicação de clientes (recompensa nos dois lados), programa de afiliados e parceiros, modelo de comissão e embaixadores, e para calcular o coeficiente viral (K-factor). Gatilhos: \"programa de indicação\", \"afiliados\", \"comissão\", \"embaixadores\", \"K-factor\", \"loop viral\". NÃO use para estratégia geral de growth (AARRR, North Star, experimentos ICE: use growth-frameworks), retenção e churn (use growth-retencao-e-churn) nem copy de anúncio (use ads-copy-de-anuncio)."
author: Antigravity Kit & Felipe Bahia (Futuro Mercado)
license: MIT
metadata:
  author: Antigravity Kit & Felipe Bahia (Futuro Mercado)
  version: 1.0.0
complements: copy-conversao, revenue-gtm-e-posicionamento, revenue-oferta, growth-retencao-e-churn
---
# Referral & Affiliate Growth Architect

> Turn satisfied customers and external distribution partners into primary acquisition channels. Guides the design, launch, and optimization of two-sided referral programs, viral coefficient ($K$-factor) loops, recurring affiliate commission architectures, and partner recruitment funnels.

## When to Use This Skill

Use this skill when you need to:

- **Design two-sided customer referral programs** (Give \$X, Get \$Y / Give feature unlock, Get storage)
- **Calculate and optimize the Viral Coefficient ($K$-factor)** and viral cycle time
- **Structure partner and affiliate commission models** (flat CPA, tiered bounties, or recurring SaaS revenue share)
- **Identify referral trigger moments** (post-purchase, post-value realization, high NPS milestones)
- **Recruit, onboard, and activate affiliates and creator ambassadors**
- **Draft viral share copies, referral landing pages, and partner enablement kits**
- **Establish anti-fraud policies** (self-referral detection, cookie windows, minimum payout thresholds)

---

## The Growth Loop Hierarchy

Referral and affiliate systems compound growth when anchored directly into customer satisfaction:

```
+-----------------------------------------------------------------------------------------+
| PROGRAM TYPE       | PRIMARY ADVOCATES           | INCENTIVE STRUCTURE                  |
+--------------------+-----------------------------+--------------------------------------+
| Two-Sided Referral| Existing active customers   | Double-sided reward (Cash/Credit/VIP)|
| (Word-of-Mouth)    | (High NPS, power users)     | Both referrer and friend get value   |
+--------------------+-----------------------------+--------------------------------------+
| Affiliate Marketing| Content creators, publishers| Performance commission (CPA, CPL,    |
| (Distribution)     | agencies, industry bloggers | 20-40% recurring monthly rev share)  |
+--------------------+-----------------------------+--------------------------------------+
| Ambassador / VIP   | Superfans, community leaders| Exclusive perks, early product access|
| (Brand Loyalty)    | & high-volume affiliates    | higher commission tiers, merch/badge |
+-----------------------------------------------------------------------------------------+
```

*See [references/referral-program.md](references/referral-program.md) and [references/affiliate-marketing.md](references/affiliate-marketing.md).*

---

## 1. Two-Sided Referral Program Architecture

One-sided referrals ("Refer a friend and get \$20") often fail because referrers feel like they are exploiting their peers. **Two-sided rewards** ("Give \$20, Get \$20" or "Give 1 month free, Get 1 month free") make the referrer look generous.

### Optimal Incentive Structure by Business Model

| Business Model | Referral Reward Mechanism | Example |
|---|---|---|
| **B2C Subscription** | Account credits or free service months | "Give 30 days free, get 30 days free" |
| **Product-Led B2B SaaS**| Feature / usage limit expansion (Dropbox model) | "Invite a teammate for +5GB storage or 1,000 AI tokens" |
| **E-Commerce / D2C** | Discount coupons or gift cards | "Give 20% off their first order, get \$25 coupon" |
| **High-Ticket B2B** | Cash bounty or charity donation | "\$500 visa gift card or corporate donation on signed contract" |

### The Viral Loop Formula

$$\text{Viral Factor } (K) = i \times c$$

- **$i$ (Invites sent per customer):** How many referral links or invites an average user sends.
- **$c$ (Conversion rate of invitees):** Percentage of recipients who become active paying users.
- **Goal:** If $K > 1$, every cohort generates more users than itself (exponential viral growth). If $K = 0.2 - 0.5$, it acts as a massive CAC-deflator that accelerates paid acquisition.

*See [references/referral-program-guide.md](references/referral-program-guide.md) and, for viral loop types and the K-factor table, [growth-fundamentos.md](../growth-frameworks/references/growth-fundamentos.md).*

---

## 2. Trigger Moments: When to Ask for Referrals

Asking for a referral at the wrong time (e.g., during payment failure or complex setup) burns goodwill. Trigger the prompt during emotional peaks:

```
[Customer Journey]
   │
   ├── Moment 1: Immediately post-purchase (High dopamine / excitement)
   ├── Moment 2: Immediately post-Aha! moment (First successful project exported)
   ├── Moment 3: In response to high NPS score (Customer rates 9 or 10)
   └── Moment 4: Milestone celebrations ("You just saved 10 hours this month!")
```

---

## 3. Affiliate Program Design & Commission Models

Affiliates are performance-driven partners. Structure offers to attract high-intent publishers while protecting unit economics:

### Commission Models

1. **Recurring SaaS Revenue Share:** 20% to 35% recurring for 12 months or lifetime. Highly attractive to SaaS bloggers and agencies.
2. **One-Time CPA (Cost Per Acquisition):** Fixed bounty paid on first payment (e.g., \$50 to \$250). Ideal for transactional products or e-commerce.
3. **Tiered Performance Incentives:**
   - Standard: 20% (1–10 sales/mo)
   - Silver: 25% (11–25 sales/mo)
   - Gold / VIP: 30%+ with custom landing page co-branding (26+ sales/mo)

### Affiliate Enablement Kit Essentials
- High-converting email swipe copies and social copy angles
- Pre-made banner creatives (GIF, static 1080x1080, 1200x628)
- Feature matrix comparisons against top competitors
- Product demo videos and transparent pricing cheat-sheets

*See [references/affiliate-marketing.md](references/affiliate-marketing.md) and the "Affiliate Program Design" and "Fraud Prevention" sections of [references/referral-program.md](references/referral-program.md).*

---

## Implementation Checklist

- [ ] Select program software (PartnerStack, Rewardful, FirstPromoter, ReferralCandy, Post Affiliate Pro)
- [ ] Calculate maximum allowable CAC and set referral/affiliate payout caps
- [ ] Draft frictionless two-sided copy ("Give X, Get Y")
- [ ] Embed sharing widgets natively into product dashboard, post-checkout, and settings
- [ ] Build a dedicated affiliate signup landing page with clear commission rules
- [ ] Implement fraud prevention: 30-day payout holding window, self-referral IP blocks
- [ ] Prepare an affiliate onboarding email sequence to drive first-sale activation within 14 days

---

## Detailed References

- [references/referral-program.md](references/referral-program.md) — End-to-end referral strategy and mechanics, with real examples (Dropbox, Uber/Lyft, Morning Brew, Notion), affiliate program design (commission, cookie window, recruitment), viral coefficient, fraud prevention and tools
- [references/referral-program-guide.md](references/referral-program-guide.md) — Step-by-step launch roadmap and tactical teardowns
- [references/affiliate-marketing.md](references/affiliate-marketing.md) — Affiliate network types, commission benchmarks, and recruitment
- [growth-fundamentos.md](../growth-frameworks/references/growth-fundamentos.md) (in `growth-frameworks`) — Growth loops, K-factor, ICE prioritization and acquisition channels; the former `growth-hacking` and `growth-strategy` references were merged there (2026-10-20)
