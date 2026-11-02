---
name: seo-on-page
description: "Use when auditing on-page SEO factors, title tags, meta descriptions, headings, internal link architectures, content quality, E-E-A-T signals, content freshness and decay, or diagnosing why a page dropped in search rankings. Do NOT use for backlinks, link building or domain authority (use seo-autoridade-e-backlinks)."
license: MIT
metadata:
  author: aaron-he-zhu & Antigravity Kit & Felipe Bahia (Futuro Mercado)
  version: 1.0.0
complements: seo-conteudo, seo-tecnico, seo-geo
---

# On-Page SEO Auditor

> Comprehensive on-page audit framework for evaluating content quality, title/header optimization, internal linking architectures, E-E-A-T signals, backlink profile health, and content decay diagnosis.

## When to Use This Skill

Activate this skill when:
- **Auditing a published page or post** to uncover why it is underperforming or stuck on page 2
- **Pre-publish QA inspection** for new high-priority content
- **Diagnosing traffic drops** on historical pages (content decay vs algorithmic update vs SERP intent shift)
- **Optimizing internal linking architecture** to route PageRank and topical authority to target money pages
- **Evaluating content depth and E-E-A-T signals** against top-ranking SERP competitors
- **Benchmarking domain authority** and reviewing backlink profile health

---

## On-Page Audit Architecture

```
[1. Meta & Title Tags] ──> [2. Headings & Scannability] ──> [3. Content Quality & E-E-A-T]
           │                                                                    │
           ▼                                                                    ▼
[6. Decay & Refresh] <── [5. Authority & Link Profile] <── [4. Internal Link Structure]
```

---

## Core On-Page Audit Pillars

### 1. Title Tags & Meta Descriptions (CTR Optimization)

The title tag remains the single most influential on-page SEO signal:

- **Title Tag Rules**:
  - Length: 50-60 characters (580 pixels max to prevent truncation in SERPs).
  - Primary keyword placed as close to the beginning as natural.
  - Value proposition or secondary hook included (*"With Templates"*, *"Complete 2026 Guide"*).
  - Brand name appended at the end separated by a pipe (`|`) or dash (`-`).
- **Meta Description Rules**:
  - Length: 130-155 characters (960 pixels max).
  - Summarizes the core answer or benefit; contains target keyword naturally.
  - Includes a clear call-to-action (CTA) encouraging clicks.

---

### 2. Heading Hierarchy & Structural Integrity

Clean heading hierarchies allow both search engine bots and AI chunkers to understand semantic relationships:

- **Single H1 Tag**: Exactly one H1 per page containing the core primary keyword.
- **Strict Hierarchy**: Never skip heading levels (e.g., do not jump from H2 directly to H4).
- **Keyword Placement**: Include primary or secondary keywords in 40-60% of H2 tags naturally.
- **Direct Answer Placement**: The text immediately following each H2 should directly address the heading query in 2-3 concise sentences.

---

### 3. Internal Linking Architecture & Siloing

Internal links pass PageRank, establish topical authority, and prevent orphan pages:

- **Hub-and-Spoke Model**:
  - Pillar page links down to all subtopic spokes.
  - Every subtopic spoke links back up to the pillar page using descriptive anchor text.
  - Lateral links connect related spokes within the same topical cluster.
- **Anchor Text Best Practices**:
  - Use descriptive, keyword-rich phrases (e.g., *"read our complete topic cluster guide"*).
  - Strictly avoid generic anchors (*"click here"*, *"read more"*, *"this article"*).
  - Vary anchor text across internal links to prevent artificial over-optimization patterns.

*Consult [references/internal-linking-optimizer.md](references/internal-linking-optimizer.md) and [references/link-architecture-patterns.md](references/link-architecture-patterns.md).*

---

### 4. Content Freshness & Decay Diagnosis

Pages inevitably lose traffic over time as information ages and competitors publish newer assets. Follow the **Decay Triage Protocol**:

1. **Detection**:
   - Compare last 6 months of Google Search Console clicks against the previous 6 months.
   - Flag pages with >20% decline in clicks or impressions.
2. **Diagnosis**:
   - **Freshness Decay**: Outdated statistics, old screenshots, deprecated tools (Solution: Update dates, refresh numbers, re-verify links).
   - **Intent Shift**: Google now favors video or comparison tables instead of standard guides (Solution: Restructure format to match new SERP intent).
   - **Competitor Superiority**: Newer pages have higher word count, better templates, or proprietary data (Solution: Inject novel information gain).
3. **Execution**:
   - Follow the step-by-step refresh workflow to update without changing the core URL or breaking existing backlinks.

*Consult [references/content-decay-signals.md](references/content-decay-signals.md) and [references/content-refresher.md](references/content-refresher.md).*

---

### 5. Backlink Quality & Authority Signals

Evaluate external link health and domain trust:

- **Backlink Profile Audit**: Identify high-authority referring domains vs low-quality spam networks.
- **Link Quality Vetting**: Assess relevance, editorial placement, dofollow ratio, and anchor text distribution.
- **Outreach & Digital PR**: Use validated outreach models to reclaim broken links or earn citations from resource pages.


---

## 100-Point On-Page Scorecard

Use this standardized evaluation rubric to score any URL:

```markdown
### On-Page SEO Quality Scorecard (100 Points)

1. TITLES & METAS (20 pts):
   [ ] Title contains primary keyword near front (5 pts)
   [ ] Title length is 50-60 chars, compelling CTR hook (5 pts)
   [ ] Meta description is 130-155 chars with actionable CTA (5 pts)
   [ ] Clean, short, hyphenated URL slug containing keyword (5 pts)

2. CONTENT STRUCTURE & READABILITY (25 pts):
   [ ] Exactly one H1 matching target topic (5 pts)
   [ ] Logical H2/H3 hierarchy with keyword variations (5 pts)
   [ ] Direct answer provided within first 100 words (5 pts)
   [ ] Short paragraphs (2-4 sentences max), bullet points, and tables (5 pts)
   [ ] Images have descriptive alt text and explicit dimensions (5 pts)

3. INFORMATION GAIN & E-E-A-T (25 pts):
   [ ] First-hand experience demonstrated (screenshots, data, tests) (10 pts)
   [ ] Author bio with credentials clearly displayed (5 pts)
   [ ] Outbound links to authoritative non-competing primary sources (5 pts)
   [ ] Absence of generic AI clichés and repetitive filler (5 pts)

4. INTERNAL LINKING & INTEGRATION (15 pts):
   [ ] At least 3-5 relevant contextual internal links pointing to spokes/pillar (5 pts)
   [ ] Descriptive anchor text used for all internal links (5 pts)
   [ ] Target page receives internal links from related cluster pages (5 pts)

5. FRESHNESS & TECHNICAL HYGIENE (15 pts):
   [ ] Publication date or "Last updated" date visible (5 pts)
   [ ] Self-referencing canonical tag is correct (5 pts)
   [ ] Zero broken links or redirect chains (5 pts)

TOTAL SCORE: ___ / 100
(≥85 = Excellent, 70-84 = Moderate optimization needed, <70 = Significant overhaul required)
```

*See [references/scoring-rubric.md](references/scoring-rubric.md) and [references/content-quality-auditor.md](references/content-quality-auditor.md).*

---

## Reference Materials

The following in-depth reference guides are bundled in the `references/` directory:

- **[internal-linking-optimizer.md](references/internal-linking-optimizer.md)** — PageRank distribution, anchor text ratio strategies, and contextual link placement.
- **[link-architecture-patterns.md](references/link-architecture-patterns.md)** — Silo frameworks, hub-and-spoke topologies, and topic cluster routing.
- **[content-decay-signals.md](references/content-decay-signals.md)** — Quantitative indicators of content decay, freshness loss, and intent evolution.
- **[content-refresher.md](references/content-refresher.md)** — Step-by-step content update framework to recover lost organic rankings.
- **[content-quality-auditor.md](references/content-quality-auditor.md)** — In-depth E-E-A-T auditing and thin-content remediation protocol.
- **[scoring-rubric.md](references/scoring-rubric.md)** — Detailed 100-point on-page quality rubric with weighted diagnostic dimensions.
- **[audit-page.md](references/audit-page.md)** — Single-page rapid audit command workflow.

---

## Related Skills

- **`seo-conteudo`** — Creation of new search-optimized articles and cluster pages.
- **`seo-tecnico`** — Crawlability, robots.txt, CWV, and status code debugging.
- **`seo-geo`** — Optimization for AI citations and LLM search answer engines.
- **`seo-schema-markup`** — Structured data (Schema.org) for rich snippet qualification.

## Referências adicionais

- [meta-tag-formulas.md](references/meta-tag-formulas.md) — Fórmulas de title tag e modelos de meta description, metodologia de teste A/B, padrões sazonais, benchmarks de CTR e otimização multilíngue.
- [meta-tags-optimizer.md](references/meta-tags-optimizer.md) — Otimização de title tag, meta description e Open Graph para melhorar CTR e a pré-visualização em redes sociais.
- [original-reference.md](references/original-reference.md) — Guia original completo desta skill (770 linhas), de antes da condensação do `SKILL.md`.

## Para onde foram os outros assuntos

- **Backlinks, autoridade de domínio e outreach:** skill [seo-autoridade-e-backlinks](../seo-autoridade-e-backlinks/SKILL.md).
