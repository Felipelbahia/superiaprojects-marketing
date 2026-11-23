---
# Source: https://github.com/clawdb
# Repository: https://github.com/Felipelbahia/superiaprojects-marketing
# Status: Customizada / Modificada localmente por Felipe Bahia
name: conteudo-reaproveitamento
description: "One-to-many content multiplication engine. Transform long-form assets (podcasts, webinars, whitepapers, pillar articles) into high-performing social posts, email newsletters, carousels, and video scripts using semantic content architectures. NÃO use para estratégia e calendário de conteúdo (use conteudo-estrategia) nem para escrever um artigo de blog (use conteudo-post-de-blog)."
author: ClawFu, aaron-he-zhu & Antigravity Kit & Felipe Bahia (Futuro Mercado)
license: MIT
metadata:
  author: ClawFu, aaron-he-zhu & Antigravity Kit & Felipe Bahia (Futuro Mercado)
  version: 1.1.0
complements: seo-conteudo, conteudo-post-de-blog, social-estrategia, geral-anti-slop
---
# Content Repurposer & Multiplication Engine

> Transform single high-effort assets into multi-channel content ecosystems. Use the 1-to-Many Repurposing Pyramid to extract text posts, threads, carousels, newsletters, and video scripts from long-form audio, video, interviews, and cornerstone articles without diluting message quality.

## When to Use This Skill

Use this skill when you need to:

- **Extract omnichannel assets** from a long-form cornerstone piece (podcast, webinar, key speech, or pillar article)
- **Turn raw audio/video transcripts** into structured, publication-ready written articles or case studies
- **Execute the Skyscraper Technique** to audit and outperform top-ranking competitive content
- **Design a semantic content architecture** linking pillar topics with cluster spokes and distribution channels
- **Conduct content gap analyses** to discover unaddressed customer queries and intent blind spots
- **Maintain editorial calendars** and multi-format content generation pipelines

---

## The 1-to-Many Repurposing Pyramid

A single high-conviction core asset generates up to 15+ high-leverage derivative pieces across the funnel:

```
+-----------------------------------------------------------------------------------+
|                            TIER 1: CORNERSTONE ASSET                              |
|           (45-Min Podcast, In-Depth Customer Webinar, or 3,000-Word Whitepaper)   |
+-----------------------------------------------------------------------------------+
                                         │
                 ┌───────────────────────┴───────────────────────┐
                 ▼                                               ▼
+---------------------------------+             +---------------------------------+
|     TIER 2: WRITTEN PILLARS     |             |      TIER 2: VISUAL PILLARS     |
| • Comprehensive SEO Blog Post   |             | • Educational Slide Deck        |
| • Deep-Dive Email Newsletter    |             | • Multi-Slide Carousel Blueprint|
+---------------------------------+             +---------------------------------+
                 │                                               │
                 └───────────────────────┬───────────────────────┘
                                         ▼
+-----------------------------------------------------------------------------------+
|                             TIER 3: MICRO-CONTENT ASSETS                          |
| • 3x LinkedIn Tactical Posts     • 2x X/Twitter Viral Threads                     |
| • 4x Short Video Scripts (Reels) • 5x Quotable Graphic Snippets (Save-Bait)       |
+-----------------------------------------------------------------------------------+
```

*See [references/content-repurposing.md](references/content-repurposing.md) and [references/transcription-to-content.md](references/transcription-to-content.md).*

---

## The Skyscraper Technique Protocol (Brian Dean)

When building cornerstone assets to dominate a topic cluster:

1. **SERP & Authority Reconnaissance**: Identify the current #1-ranking asset for the target topic.
2. **Dimension Upgrades**:
   - **More Comprehensive**: Fill gaps in data, missing workflow steps, or obsolete advice.
   - **More Up-to-Date**: Replace outdated 2-3 year-old studies with current year benchmarks.
   - **Better Designed**: Replace walls of text with custom diagrams, comparison matrices, and clear visual hierarchy.
   - **Higher Information Gain**: Add proprietary case studies, interview quotes, and actionable templates.
3. **Targeted Amplification**: Outreach to publishers, newsletters, and sites citing the inferior predecessor.


---

## Saneamento de Material Bruto (Transcrições e Áudios)

Ao processar material oral bruto (gravações de reuniões, entrevistas, podcasts e vídeos), aplique o protocolo de **[`references/saneamento-de-material-bruto.md`](references/saneamento-de-material-bruto.md)**:

1. **A Regra de Ouro: Limpar Não É Reescrever:** O saneamento limita-se à higienização mecânica da fala (remover "tipo assim", "né", "ééé", falsos inícios e pontuar frases). É terminantemente proibido parafrasear, adotar jargão corporativo estéril ou alterar a linha de raciocínio e os atritos do autor.
2. **Correção Técnica Rastreável:** Corrija grafias fonéticas corrompidas de termos conhecidos (ex.: *"Cubernétis"* -> `Kubernetes`), registrando a intervenção no relatório.
3. **Marcadores de Incerteza:** Nunca invente falas em trechos abafados ou inaudíveis. Use rigorosamente `[inaudível]`, `[trecho incerto: contexto]` ou `[termo técnico a confirmar: termo]`.
4. **Governança de Dados Sensíveis:** Faturamento, nomes de clientes e segredos de negócio recebem a marcação `[dado sensível: requer permissão]` e são alertados no relatório.
5. **Relatório de Saneamento Obrigatório (4 Colunas):** Toda saída saneada inclui tabela de intervenções: `Trecho Original da Transcrição | Trecho Saneado | Tipo de Intervenção | Justificativa Operacional`.
6. **Exemplo Resolvido de Saneamento e Acervo:** Consulte [`references/caso-saneamento-reaproveitamento.md`](references/caso-saneamento-reaproveitamento.md) para ver a transcrição bruta preservada, o relatório em 3 blocos (*corrigido*, *preservado*, *pendências*), a base limpa e o plano de oportunidades com matriz e corte justificado.

---

## Matriz de Reaproveitamento e Fluxo de Base Editorial

A multiplicação 1-para-Muitos é orquestrada pela metodologia de **[`references/matriz-de-reaproveitamento.md`](references/matriz-de-reaproveitamento.md)**:

1. **Matriz de Reaproveitamento Estruturada (8 Colunas):** Cada derivado deve mapear `Canal Ativo`, `Formato e Dimensão`, `Persona-Alvo`, `Dúvida / Dor Específica`, `Ângulo Editorial Nativo`, `Fato / Âncora / Timestamp`, `Permissão de Dados Sensíveis` e `Prioridade Justificada`.
2. **Fluxo "Da Transcrição à Base Editorial" (5 Etapas):**
   - **Etapa 1:** Material Bruto Imutável (`bruto.md`).
   - **Etapa 2:** Saneamento com Relatório de Limpeza (`saneado.md`).
   - **Etapa 3:** Perguntas de Permissão e Validação de Dados Sensíveis.
   - **Etapa 4:** FAQ Rastreável por Linha e Timestamp.
   - **Etapa 5:** Base Editorial separando Fatos Observáveis de Interpretações/Opiniões.

---

## Repurposing Quality Gate (Hard Gate Bloqueante)

Antes de aprovar ou despachar qualquer conjunto de peças derivadas, execute a auditoria de conformidade:

### Hard Gate contra Reaproveitamento Mecânico
```
[ ] DIFERENCIAÇÃO DE ÂNGULO: Cada canal aborda o tema sob um recorte psicológico e editorial próprio.
    -> REPROVADO se o mesmo roteiro linear ou a mesma ordem de tópicos for apenas fatiada entre redes.
[ ] ADAPTAÇÃO NATIVA DE FORMATO: Respeita as dinâmicas de retenção de cada plataforma (visual, debate, vídeo).
[ ] RASTREABILIDADE FACTUAL: Cada afirmação tem âncora e timestamp na transcrição saneada original.
[ ] COERÊNCIA DO CONJUNTO: Zero contradições entre peças de canais distintos e saturação temporal evitada.
[ ] GOVERNANÇA E SIGILO: Dados sensíveis foram formalmente liberados ou convertidos em casos anônimos.
```

---

## Reference Materials

The following in-depth guides are bundled in the `references/` directory:

- **[saneamento-de-material-bruto.md](references/saneamento-de-material-bruto.md)** — Protocolo de higienização de transcrições sem reescrever, marcadores e relatório de 4 colunas.
- **[matriz-de-reaproveitamento.md](references/matriz-de-reaproveitamento.md)** — Matriz 1-para-Muitos estruturada (8 colunas), Hard Gate contra reaproveitamento mecânico e fluxo de 5 etapas da base editorial.
- **[content-repurposing.md](references/content-repurposing.md)** — Core repurposing matrix and multi-format extraction workflows.
- **[transcription-to-content.md](references/transcription-to-content.md)** — Step-by-step transcript cleanup, quoting, and article restructuring.
- **[repurpose.md](references/repurpose.md)** — Tactical asset multiplication blueprints across channels.
- **[generate.md](references/generate.md)** — Batch creation templates and prompt structures.
- **[reverse-engineering.md](references/reverse-engineering.md)** — Dissecting viral posts and high-converting campaigns.

---

## Related Skills

- **`seo-conteudo`** — Comprehensive search-optimized article production and keyword clustering.
- **`conteudo-post-de-blog`** — Personal voice blog post drafting from brain dumps.
- **`social-estrategia`** — Social distribution, algorithm optimization, and post scheduling.
- **`geral-anti-slop`** — Mandatory verification to strip generic synthetic writing.

## Roteiros guiados (vindos do kit AgentKits)

Roteiros que fazem perguntas ao usuário antes de entregar. O texto base é inglês.

- **[editing.md](references/editing.md)** — Roteiro guiado para editar e revisar um texto de marketing existente.
- **[enhance.md](references/enhance.md)** — Roteiro guiado para diagnosticar os problemas de um texto e melhorá-lo.

## Outras referências

- **[google-meta-repurposer.md](references/google-meta-repurposer.md)** — Transforma um conteúdo longo em derivados por plataforma.

## Para onde foram os outros assuntos

- **Estratégia de conteúdo** (pilares, calendário, formatos, distribuição, ideias, lacunas, guia de estilo): skill [conteudo-estrategia](../conteudo-estrategia/SKILL.md).
- **Redação de blog** (`write-blog`, `blog-template`, `content-writing`): [conteudo-post-de-blog](../conteudo-post-de-blog/SKILL.md). **Páginas de concorrentes:** [revenue-inteligencia-competitiva](../revenue-inteligencia-competitiva/SKILL.md). **Skyscraper (link building):** [seo-autoridade-e-backlinks](../seo-autoridade-e-backlinks/SKILL.md).
- **Guia rápido da apresentação educativa:** voltou para [audiovisual-pitch-deck](../audiovisual-pitch-deck/SKILL.md), a que ele pertence.
- **Cheat sheets duplicados:** arquivados em `.agents/skills/_arquivo/mescladas/r12-copy/`.

---

## Version History

| Version | Date | Changes |
|---------|------|---------|
| 1.1.0 | 2026-11-20 | Saneamento fiel sem paráfrase com relatório de 4 colunas (`saneamento-de-material-bruto.md`), matriz 1-para-muitos estruturada com 8 colunas (`matriz-de-reaproveitamento.md`), Hard Gate bloqueante contra reaproveitamento mecânico e fluxo de 5 etapas da base editorial (inbox 2034); crédito conceitual formal a `promovaweb/inboundfy` |
| 1.0.0 | 2026-03-01 | Versão inicial importada do kit AgentKits |
