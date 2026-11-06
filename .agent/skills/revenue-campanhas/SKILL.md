---
# Source: https://github.com/anthropics/anthropic-quickstarts
# Repository: https://github.com/Felipelbahia/superiaprojects-marketing
# Status: Customizada / Modificada localmente por Felipe Bahia
name: revenue-campanhas
description: >
  Planejamento integrado de campanhas de marketing digital e roteamento para a skill especialista de cada frente (conteúdo, social, email, SEO, GEO, mídia paga, métricas, lançamento). Gera parâmetros UTM e valida a campanha antes do lançamento. Use para planejar uma campanha que atravessa vários canais, montar o calendário, definir o rastreamento UTM ou destravar uma campanha parada. NÃO use para executar o trabalho de um canal específico (use a skill especialista da tabela de rotas, por exemplo seo-conteudo, social-estrategia, email-copy, ads-analise-de-desempenho ou revenue-gtm-e-posicionamento).
author: Claude Skills & Felipe Bahia (Futuro Mercado)
license: MIT
metadata:
  author: Claude Skills & Felipe Bahia (Futuro Mercado)
  version: 1.0.0
---
# Marketing Campaign Execution

Plan, execute, and measure digital marketing campaigns across content, social, email, and analytics.

## Contents

- [Quick Start](#quick-start)
- [Domain Reference Guide](#domain-reference-guide)
- [Rotas por especialidade](#rotas-por-especialidade)
- [Ordem de consulta em pedidos com várias frentes](#ordem-de-consulta-em-pedidos-com-várias-frentes)
- [Campaign Validation Checklist](#campaign-validation-checklist)
- [Desbloqueio de Campanhas (When Stuck Protocol)](#desbloqueio-de-campanhas-when-stuck-protocol)
- [Persona Adaptation](#persona-adaptation)
- [Boundaries](#boundaries)

## Quick Start

### Generate UTM Parameters
```
Source: where traffic originates (google, facebook, newsletter)
Medium: how it arrives (cpc, email, social, organic)
Campaign: initiative name (spring-sale-2025, product-launch)

Format: lowercase, hyphens, no spaces
Input: "Spring Sale 2025" → Output: "spring-sale-2025"
Input: "Q1 Launch Campaign" → Output: "q1-launch-campaign"

Example: ?utm_source=linkedin&utm_medium=social&utm_campaign=q1-launch
```

### Create Email Sequence
1. Welcome (immediate): Set expectations, deliver promised value
2. Value (day 2-3): Best content or quick win
3. Engagement (day 5-7): Encourage reply or action
4. Offer (day 10): Clear CTA with incentive

### Plan Content Calendar
Essential fields: Title, Target keyword, Funnel stage (TOFU/MOFU/BOFU), Format, Owner, Publish date, Distribution channels.

### Check Campaign Performance
Primary metrics by channel:
- Email: Open rate (43% avg), CTR (2% avg), Conversion rate
- Social: Engagement rate, Reach, Click-through
- Paid: ROAS, CPA, CTR
- Content: Traffic, Time on page, Conversions

## Domain Reference Guide

| Need | Reference | When to Load |
|------|-----------|--------------|
| Track campaigns | [utm-tracking.md](references/utm-tracking.md) | UTM formatting, naming conventions, GA4 alignment |
| Measure performance | [analytics-measurement.md](references/analytics-measurement.md) | KPIs, GA4 setup, attribution, ROI calculations |
| Launch products | [gtm-tools.md](references/gtm-tools.md) | GTM frameworks, positioning, tool selection |
| Optimize for search | [seo-optimization.md](references/seo-optimization.md) | Technical SEO, on-page, content SEO, link building, E-E-A-T |
| Optimize for AI | [geo-optimization.md](references/geo-optimization.md) | GEO, LLMO, AEO, AI Overviews, chatbot visibility |
| Sequências prontas de skills | [skill-orchestration-matrix.md](references/skill-orchestration-matrix.md) | 7 fluxos prontos (lançamento, validação de clientes, conteúdo, posicionamento, vendas, decisão, vídeo com IA); o começo do arquivo traz o mapa de nome do passo para arquivo real |

## Rotas por especialidade

Esta skill planeja e coordena a campanha. O trabalho de cada frente é da skill especialista. Pergunte qual é a frente do pedido e abra a skill correspondente; use as referências locais só para a visão geral de UTM, métricas, lançamento, SEO e GEO.

| Quando o pedido é sobre | Skill especialista |
|---|---|
| Estratégia e calendário de conteúdo | [conteudo-linha-de-producao](../conteudo-linha-de-producao/SKILL.md), [conteudo-briefing](../conteudo-briefing/SKILL.md), [conteudo-reaproveitamento](../conteudo-reaproveitamento/SKILL.md) |
| Redes sociais | [social-estrategia](../social-estrategia/SKILL.md), [social-carrossel](../social-carrossel/SKILL.md) |
| Email | [email-copy](../email-copy/SKILL.md), [email-automacao](../email-automacao/SKILL.md), [email-newsletter](../email-newsletter/SKILL.md) |
| Voz, tom e mensagem da marca | [brand-voice-messaging](../brand-voice-messaging/SKILL.md) |
| SEO | [seo-conteudo](../seo-conteudo/SKILL.md), [seo-on-page](../seo-on-page/SKILL.md), [seo-tecnico](../seo-tecnico/SKILL.md) |
| Visibilidade em IA (GEO) | [seo-geo](../seo-geo/SKILL.md) |
| Lançamento e go-to-market | [revenue-gtm-e-posicionamento](../revenue-gtm-e-posicionamento/SKILL.md), [revenue-lancamento](../revenue-lancamento/SKILL.md), [revenue-lancamento-tecnico](../revenue-lancamento-tecnico/SKILL.md) |
| Mídia paga | [ads-analise-de-desempenho](../ads-analise-de-desempenho/SKILL.md), [ads-google](../ads-google/SKILL.md), [ads-meta](../ads-meta/SKILL.md) |
| Métricas e relatório | [data-web-ga4](../data-web-ga4/SKILL.md), [data-atribuicao-e-relatorios](../data-atribuicao-e-relatorios/SKILL.md) |
| Landing page | [copy-landing-page](../copy-landing-page/SKILL.md), [site-cro](../site-cro/SKILL.md) |
| Rastreamento UTM | referência local [utm-tracking.md](references/utm-tracking.md) |
| Visão geral de lançamento (SOSTAC, RACE, AARRR) | referência local [gtm-tools.md](references/gtm-tools.md) |
| Visão geral de SEO | referência local [seo-optimization.md](references/seo-optimization.md) |
| Visão geral de GEO (LLMO, AEO) | referência local [geo-optimization.md](references/geo-optimization.md) |
| KPIs, GA4, atribuição e ROI em visão geral | referência local [analytics-measurement.md](references/analytics-measurement.md) |

Se o pedido for vago ("ajude com marketing"), pergunte qual frente antes de abrir qualquer coisa.

## Ordem de consulta em pedidos com várias frentes

| Tipo de pedido | Comece por | Depois | Apoio |
|---|---|---|---|
| Lançamento de produto | [revenue-gtm-e-posicionamento](../revenue-gtm-e-posicionamento/SKILL.md) | [conteudo-linha-de-producao](../conteudo-linha-de-producao/SKILL.md), [brand-voice-messaging](../brand-voice-messaging/SKILL.md) | [email-copy](../email-copy/SKILL.md), [social-estrategia](../social-estrategia/SKILL.md) |
| Rastreamento de campanha | [utm-tracking.md](references/utm-tracking.md) | [analytics-measurement.md](references/analytics-measurement.md) | — |
| Plano trimestral | [conteudo-linha-de-producao](../conteudo-linha-de-producao/SKILL.md) | [social-estrategia](../social-estrategia/SKILL.md), [email-copy](../email-copy/SKILL.md) | [analytics-measurement.md](references/analytics-measurement.md) |
| Otimização de desempenho | [analytics-measurement.md](references/analytics-measurement.md) | skill do canal | — |
| Voz de marca | [brand-voice-messaging](../brand-voice-messaging/SKILL.md) | — | — |
| Posição nas buscas | [seo-conteudo](../seo-conteudo/SKILL.md) | [seo-on-page](../seo-on-page/SKILL.md), [seo-tecnico](../seo-tecnico/SKILL.md) | [analytics-measurement.md](references/analytics-measurement.md) |
| Visibilidade em IA | [seo-geo](../seo-geo/SKILL.md) | [seo-conteudo](../seo-conteudo/SKILL.md) | [conteudo-linha-de-producao](../conteudo-linha-de-producao/SKILL.md) |
| Estratégia completa | [seo-optimization.md](references/seo-optimization.md) e [geo-optimization.md](references/geo-optimization.md) | skills de conteúdo e social | skills de email e [analytics-measurement.md](references/analytics-measurement.md) |

## Campaign Validation Checklist

Before launching any campaign, verify:

### Strategy
- [ ] Target audience clearly defined
- [ ] Campaign goals documented with baseline metrics
- [ ] Success criteria established (KPIs + targets)
- [ ] Timeline and milestones set

### Tracking
- [ ] UTM parameters validated (lowercase, hyphens, no spaces)
- [ ] GA4 channel alignment confirmed
- [ ] Conversion tracking tested
- [ ] Attribution model selected

### Content
- [ ] Brand voice checklist completed
- [ ] No banned words or unsubstantiated claims
- [ ] Readability score acceptable (60+ Flesch)
- [ ] CTA clear and actionable

### Technical
- [ ] Email sequences tested in preview
- [ ] Links verified working
- [ ] Mobile responsiveness checked
- [ ] Analytics tracking confirmed

---

## ⚡ Desbloqueio de Campanhas (When Stuck Protocol)

Para destravar projetos ou campanhas estagnadas por excesso de opções, reuniões improdutivas ou paralisia por análise:
- [Guia Operacional: When Stuck Protocol](references/when-stuck-protocol.md): Protocolo de 4 passos (Zoom out, Restrição de 1 dia/baixo custo, Pergunta ingênua e Menor teste viável) para decisões imediatas e execução rápida.

---

## Persona Adaptation

**Beginner signals:** Asks "what is," "how do I," "why should I," unfamiliar terminology, requests explanations.
→ Provide concept context before tactics. Explain frameworks. Offer templates.

**Experienced signals:** Uses correct terminology, asks for benchmarks, requests templates, mentions specific tools.
→ Skip fundamentals. Provide benchmarks, templates, advanced tactics directly.

## Boundaries

**Dentro do escopo:**
- Planejamento e coordenação de campanhas entre canais
- Calendário de conteúdo e distribuição
- Geração e governança de parâmetros UTM
- Checklist de validação antes do lançamento
- Roteamento para a skill especialista de cada frente
- Destravar campanhas paradas (When Stuck Protocol)

**Fora do escopo (use a skill indicada):**
- Gestão de anúncios pagos, lances e públicos: [ads-analise-de-desempenho](../ads-analise-de-desempenho/SKILL.md), [ads-google](../ads-google/SKILL.md), [ads-meta](../ads-meta/SKILL.md)
- Implementação de CRM: [revenue-orquestracao-de-crm](../revenue-orquestracao-de-crm/SKILL.md)
- Identidade visual da marca: [brand-visual-direction](../brand-visual-direction/SKILL.md), [brand-design-system](../brand-design-system/SKILL.md)
- Relações com a imprensa: [pr-assessoria-de-imprensa](../pr-assessoria-de-imprensa/SKILL.md)
- Copy que não é de campanha: [copy-conversao](../copy-conversao/SKILL.md)

**Esclareça antes de seguir:**
- "Ajude com marketing" → qual frente?
- "Melhore meus anúncios" → criativo e copy ([ads-criativos](../ads-criativos/SKILL.md), [ads-copy-de-anuncio](../ads-copy-de-anuncio/SKILL.md)) ou gestão da campanha ([ads-analise-de-desempenho](../ads-analise-de-desempenho/SKILL.md))?
- "Configurar analytics" → tags e GA4 ([data-web-ga4](../data-web-ga4/SKILL.md)) ou relatório ([data-atribuicao-e-relatorios](../data-atribuicao-e-relatorios/SKILL.md))?
- "Diretrizes de marca" → voz e mensagem ([brand-voice-messaging](../brand-voice-messaging/SKILL.md)) ou identidade visual ([brand-design-system](../brand-design-system/SKILL.md))?

## Montar a campanha: plano, brief e playbooks

O texto base é inglês.

- **[plan.md](references/plan.md)** — Roteiro guiado do kit AgentKits para criar o plano de uma campanha.
- **[campaign-brief.md](references/campaign-brief.md)** — Modelo de brief de campanha.
- **[campaign-playbooks.md](references/campaign-playbooks.md)** — Modelos testados para executar diferentes tipos de campanha.

## Receitas por canal e formato

Cada receita é a ordem de skills para um tipo de entrega. Antes de qualquer uma, leia a marca em `_brands/<marca>/` (regra 1.1 do projeto) e, no fim, passe o texto por `/geral-anti-slop` e salve seguindo a regra de resolução de destino da skill `geral-arquitetura-de-projeto` (lê o mapa do projeto; sem mapa, `content/<marca>/<canal>/AAAA-MM-DD - Nome da Demanda/` no 0 Mkt ou `conteudos/<canal>/AAAA-MM-DD - Nome da Demanda/` em projeto próprio).

### Receita 1: Carrossel de alta conversão (Instagram e LinkedIn)
1. Marca: `brand-voice.md` e `content-pillars.md`.
2. Psicologia: [revenue-sexy-canvas](../revenue-sexy-canvas/SKILL.md) (motores de Vaidade, Curiosidade e Preguiça).
3. Roteiro lâmina a lâmina: [social-carrossel](../social-carrossel/SKILL.md): capa com gancho em caixa alta (até 20 palavras), pagamento imediato no slide 2 (até 25), "isca de salvamento" (checklist ou matriz) no slide 5 e um único CTA para DM no slide 6.
4. Direção visual: [social-direcao-de-arte-ia](../social-direcao-de-arte-ia/SKILL.md).
5. Salvar na pasta do canal — ver a regra de resolução de destino acima.

### Receita 2: Reels, Shorts e TikTok com retenção
1. Marca.
2. Gancho dos 3 primeiros segundos: [copy-hooks-video-curto](../copy-hooks-video-curto/SKILL.md): 0,0 s elemento em movimento, 0,5 s primeira palavra sem enrolação, 1,2 s quebra de padrão com promessa e pagamento adiado.
3. Engenharia reversa de um reel de referência: [reel-analyzer](../copy-hooks-video-curto/references/reel-analyzer.md).
4. Geração e direção: ai-video-creator *(removido para o projeto de edição de vídeo)*. Montagem em código (Remotion) vive no projeto de edição de vídeo (`Compartilhado/Edição de Vídeo com IA`).
5. Salvar na pasta do canal — ver a regra de resolução de destino acima.

### Receita 3: Landing page de conversão
1. Marca e persona: [persona-icp](../persona-icp/SKILL.md).
2. Copy: [copy-landing-page](../copy-landing-page/SKILL.md).
3. Atrito e conversão: [site-cro](../site-cro/SKILL.md).
4. Design e interface: [site-interface-de-conversao](../site-interface-de-conversao/SKILL.md).
5. Salvar na pasta do canal — ver a regra de resolução de destino acima.

**Para entregar a página pronta** (marca, design a partir dos tokens, código com autorização, teste no navegador e revisão de conversão), use o workflow [site-construcao-de-landing-page](../../workflows/site-construcao-de-landing-page.md), conduzido pelo agente [site-construcao-web](../../agents/site-construcao-web.md); a página é salva no destino da regra de resolução de `geral-arquitetura-de-projeto` (pasta de landing pages). Site de várias páginas: [site-construcao-de-site](../../workflows/site-construcao-de-site.md) e a skill [site-arquitetura](../site-arquitetura/SKILL.md).

### Receita 4: Sequência de nutrição e onboarding (e-mail)
1. Marca.
2. Arquitetura da jornada: [email-automacao](../email-automacao/SKILL.md).
3. Redação: [email-copy](../email-copy/SKILL.md).
4. Validação técnica (SPF, DKIM, DMARC): [email-entregabilidade](../email-entregabilidade/SKILL.md).
5. Salvar na pasta do canal — ver a regra de resolução de destino acima.

### Receita 5: Artigo de busca orgânica (SEO e GEO)
1. Intenção de busca: [keyword-research-deep](../seo-palavras-chave/references/keyword-research-deep.md).
2. Redação: [seo-conteudo](../seo-conteudo/SKILL.md).
3. Schema e GEO: [seo-schema-markup](../seo-schema-markup/SKILL.md) e [seo-geo](../seo-geo/SKILL.md).
4. Auditoria on-page: [seo-on-page](../seo-on-page/SKILL.md).
5. Salvar na pasta do canal — ver a regra de resolução de destino acima.
