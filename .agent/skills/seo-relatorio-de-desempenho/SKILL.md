---
# Source: https://github.com/clawdb
# Repository: https://github.com/Felipelbahia/superiaprojects-marketing
# Status: Customizada / Modificada localmente por Felipe Bahia
name: seo-relatorio-de-desempenho
description: "Comprehensive SEO & GEO performance tracking, executive reporting, anomaly detection, ranking volatility alerts, and KPI analytics across Google, Bing, and generative AI search engines (Perplexity, SearchGPT, Claude, Gemini)."
author: aaron-he-zhu & Antigravity Kit & Felipe Bahia (Futuro Mercado)
license: MIT
metadata:
  author: aaron-he-zhu & Antigravity Kit & Felipe Bahia (Futuro Mercado)
  version: 1.0.0
complements: seo-conteudo, seo-geo, seo-tecnico, seo-on-page
---
# SEO Performance Reporter & Rank Tracker

> Monitor keyword positions across traditional and AI-generated search results, generate executive performance dashboards, track organic KPIs, and detect traffic anomalies and ranking crashes before they impact business revenue.

## When to Use This Skill

Use this skill when you need to:

- **Generate SEO & GEO performance reports** for stakeholders, founders, or clients
- **Track keyword rankings** and monitor SERP position changes over time
- **Measure AI visibility & share of voice** across Perplexity, ChatGPT/SearchGPT, and Google AI Overviews
- **Detect traffic drops and ranking anomalies** using statistical alert thresholds
- **Build executive dashboards** translating search performance into revenue and conversions
- **Analyze SERP feature shifts** (Featured Snippets, People Also Ask, Local Packs)
- **Maintain historical campaign memory** and keyword tracking databases across sprints
- **Investigate algorithm updates** and correlate volatility with site health

---

## Methodology Foundation

**Core Principle**: SEO reporting is not merely a collection of vanity metrics; it is an early-warning system and a strategic narrative that bridges organic technical metrics with commercial business impact.

```
+-----------------------------------------------------------------------------------+
|                        SEO & GEO PERFORMANCE ARCHITECTURE                         |
+-----------------------------------------------------------------------------------+
|  1. INGESTION        Rankings (SERP/AI) + Traffic (GA4/GSC) + Backlinks + Revenue  |
|  2. NORMALIZATION    Weighted Position Scoring + SERP Feature Multipliers         |
|  3. ANOMALY ENGINE   Z-Score Analysis + Threshold Triggering (P0 / P1 / P2)       |
|  4. NARRATIVE LAYER  Executive 1-Pager / Monthly Deep Dive / Weekly Pulse          |
+-----------------------------------------------------------------------------------+
```

### Core Dimensions of Performance Analysis

1. **Rank Position & Volatility**:
   - Traditional Rankings: Absolute position (1-100), average position, top 3 / top 10 distribution.
   - Volatility Index: Measuring day-over-day and week-over-week variance to separate algorithmic noise from true site anomalies.
   - SERP Feature Ownership: Tracking retention of Featured Snippets, Knowledge Panels, and PAA placements.

2. **AI Engine Visibility (GEO Tracking)**:
   - Brand Mention Rate in AI Search (Perplexity, SearchGPT, Claude, Gemini).
   - Citation Share of Voice for core commercial queries.
   - Anchor Source Position (Primary source vs secondary mention).

3. **Traffic & Conversion Attribution**:
   - Non-brand organic clicks and impressions (Google Search Console).
   - Qualified organic sessions and engagement rate (GA4).
   - Goal completion, lead capture, and revenue generated from organic landing pages.

---

## Operational Reporting Cycles

```
+-----------------------------------------------------------------------------------+
| FREQUENCY | FOCUS                    | ARTIFACT PRODUCED    | TARGET AUDIENCE     |
|-----------+--------------------------+----------------------+---------------------|
| Real-Time | Anomaly / Ranking Crash  | Alert Notification   | SEO Lead / Dev Team |
| Weekly    | Tactical Pulse & Shifts  | Keyword Delta Sheet  | Growth / Marketing  |
| Monthly   | Comprehensive Report     | Executive Dashboard  | CMO / VP Marketing  |
| Quarterly | Strategic Review         | GTM / SERP Benchmark | C-Level / Board     |
+-----------------------------------------------------------------------------------+
```

---

## Statistical Alerting & Anomaly Detection Framework

To prevent alert fatigue while catching catastrophic traffic crashes, alerts are governed by three weighted threshold tiers:

### Tier 1: Critical (P0) — Immediate Escalation (<2 Hours)
- **Trigger**: Organic traffic drop >25% over a 3-day rolling window compared to 4-week average.
- **Ranking Trigger**: Top 3 commercial intent keywords dropping >5 positions or off Page 1 entirely.
- **Indexation Trigger**: Sudden loss of >15% of indexed URLs in Google Search Console.
- **Action**: Immediate technical triage (robots.txt, canonical loops, server 5xx errors, accidental noindex tags).

### Tier 2: Warning (P1) — 24-Hour Review
- **Trigger**: Traffic dip of 10-25% on specific content clusters or subdirectories.
- **Ranking Trigger**: Loss of Featured Snippets on high-volume queries to competitors.
- **Backlink Trigger**: Sudden spike in toxic referring domains or loss of high-authority citations.
- **Action**: SERP intent inspection, content freshness audit, competitor update comparison.

### Tier 3: Informational (P2) — Weekly Review
- **Trigger**: Minor fluctuations (±1-3 positions) within Page 1 (positions 4-10).
- **Trigger**: Emergence of new competitors in SERP features or PAA boxes.
- **Action**: Note in weekly tactical pulse; queue for routine content refresher.

*See [references/alert-threshold-guide.md](references/alert-threshold-guide.md) for full statistical models.*

---

## Stakeholder Reporting Structures

### 1. Executive One-Pager (C-Level / Board)
- **Top-Line Summary**: Total organic revenue/pipeline, YoY traffic growth, and overall visibility score.
- **Key Wins**: High-impact keyword captures, AI citation milestones, and major traffic gains.
- **Challenges & Mitigations**: Brief explanation of algorithmic headwinds and countermeasures underway.
- **Strategic Next Steps**: Priority investments for the upcoming sprint.

### 2. Marketing & Growth Dashboard (Monthly)
- **Channel Performance**: Organic search vs paid search vs direct vs referral.
- **Top Performing Hubs**: Best performing topic clusters, traffic share by category.
- **Keyword Movement Matrix**: Keywords entered Top 3, Top 10, or decayed.
- **Conversion Breakdown**: Lead capture rate per cluster, assisted organic conversions.

### 3. SEO Ops & Engineering Backlog (Weekly)
- **Technical Health Score**: Core Web Vitals compliance (LCP, INP, CLS), crawl errors, broken links.
- **Indexation Health**: Coverage report status, canonical discrepancies, orphan pages detected.
- **Action Items**: Prioritized ticket list with developer instructions.

*See [references/report-templates.md](references/report-templates.md) and [references/kpi-definitions.md](references/kpi-definitions.md).*

---

## Standardized Review Checklist

Before delivering an SEO report or resolving an anomaly alert, verify:

```
DATA INTEGRITY:
□ Data date range matches previous reporting cadence (e.g. 28 days vs 28 days YoY)
□ Seasonality and holiday anomalies accounted for in traffic explanations
□ Tracking tags and GA4/GSC properties verified for continuity (no tag drop-off)
□ Internal traffic filtered from analytics data

ANALYSIS RIGOR:
□ Root cause identified for significant drops (Algorithm vs Technical vs Competitor)
□ AI engine citations tracked alongside traditional Google SERP positions
□ Commercial and transactional keyword clusters isolated from informational noise
□ Clear, actionable next steps defined for every highlighted deficit

DELIVERY POLISH:
□ Executive summary leads with revenue/conversions, not just raw impressions
□ Charts include baseline comparisons and clear trendlines
□ Technical jargon translated into business outcomes for leadership
```

---

## Reference Materials

The following operational guides and templates are bundled in the `references/` directory:

- **[rank-tracker.md](references/rank-tracker.md)** — Core rank tracking framework, position change calculation, and SERP monitoring protocol.
- **[alert-manager.md](references/alert-manager.md)** — Anomaly detection engine, escalation rules, and notification dispatch pipelines.
- **[alert-threshold-guide.md](references/alert-threshold-guide.md)** — Mathematical criteria, standard deviations, and sensitivity controls for ranking alerts.
- **[report-templates.md](references/report-templates.md)** — Markdown, slide, and email templates for executive, weekly, and monthly reporting.
- **[kpi-definitions.md](references/kpi-definitions.md)** — Exhaustive dictionary of organic search metrics, calculation formulas, and benchmarks.
- **[serp-feature-taxonomy.md](references/serp-feature-taxonomy.md)** — Tracking methodology for Featured Snippets, Knowledge Panels, SGE/AI Overviews, and Local Packs.

---

## Related Skills

- **`seo-conteudo`** — Plan and create search-optimized content for keywords identified in reports.
- **`seo-geo`** — Optimize brand citations and knowledge graph signals for AI search engines.
- **`seo-tecnico`** — Investigate technical errors and Core Web Vitals regressions flagged by alerts.
- **`seo-on-page`** — Audit pages exhibiting content decay or ranking drops to execute refreshers.
- **`seo-schema-markup`** — Deploy structured data to capture rich snippets identified in SERP reports.

## Referências adicionais

- [original-reference.md](references/original-reference.md) — Guia original completo desta skill (839 linhas), de antes da condensação do `SKILL.md`.
