# GT Growth Lab

**Biblioteca de 505+ experimentos de Go-to-Market para B2B**, pronta para rodar como skill no Claude. Cada experimento traz hipótese, métrica de sucesso e benchmark/fonte. Estruturada nos 7 estágios do funil B2B (Aquisição → Indicação) para encaixar em qualquer framework de revenue ou diagnóstico.

> Criada por **Raphael Lassance** (CEO & Founder do Growth Team) e pelo **Growth Team** — Boutique de Arquitetura de Receita e Growth.

---

## O que está dentro

| Estágio | Experimentos | Cobertura |
|---|---|---|
| **Aquisição** | 120 | Cold email, LinkedIn outbound, ABM, SEO, **GEO/AI search**, paid ads, eventos, lead magnets, partnerships, podcast, comunidade, **founder-led growth**, **AI-native outbound** |
| **Ativação** | 65 | Onboarding flows, time-to-value, multi-seat, lifecycle email, trial mechanics, growth loops, friction reduction, **AI-powered onboarding** |
| **Receita** | 90 | Pricing page/structure, modelos (sub/usage/credit/outcome), discovery, demo, RFP, propostas, **sales methodologies (MEDDPICC, Challenger, SPIN, SPICED, NEAT, Sandler)**, **AI sales** |
| **Adoção** | 55 | Health scoring, QBR, feature adoption, behavior triggers, community, education, CSM playbooks, **AI customer success** |
| **Retenção** | 60 | Renewal mechanics, cancellation flow, dunning, win-back, health monitoring, customer success, **AI retention** |
| **Expansão** | 60 | Cross-sell, upsell, multi-seat, multi-BU, land-and-expand, multi-product platform plays, **AI-driven expansion** |
| **Indicação** | 55 | Referral programs, partner/channel, customer advocacy, case studies, co-marketing, viral loops, **influencer B2B**, **AI advocacy** |

Mais um arquivo de **frameworks de priorização (ICE, RICE, PXL, ICE-R, PIE)** e **benchmarks B2B 2025-2026** (cold email, funil, NRR, CAC, pricing, sales acceleration, AI search).

**Total: 505 experimentos com fonte rastreável.**

---

## Para quem é

Profissionais que tomam decisões de go-to-market em B2B:

- **Founders** de SaaS B2B, indústria, agro, serviço B2B, AI-native
- **Heads/VPs de Marketing, Growth, RevOps**
- **Heads de Vendas / CRO**
- **Customer Success Leaders** (foco em adoção, retenção, expansão)
- **Consultores de growth / GTM**
- **Investidores** que precisam avaliar GTM dos portfolios

Não é para B2C, e-commerce DTC ou times sem alguma maturidade analítica (mínimo: tracking de funil básico).

---

## Fontes

Cada experimento tem fonte rastreável em uma destas autoridades:

- **Newsletters/Blogs:** Growth Unhinged (Kyle Poyar), Theory Ventures (Tom Tunguz), Reforge, CXL/Speero, SaaStr, PricingSaaS, Lenny's Newsletter, Brian Balfour, Aakash Gupta
- **Research:** McKinsey, Gartner, Forrester, ChartMogul, SaaS Capital, OPEXEngine, Recurly, Hunter.io, Backlinko, Bain Capital Ventures
- **Tools/Platforms (com dados reais de uso):** Clay, GrowthBook, Demandbase, Highspot, SiftHub, Demostack, Navattic, Mutiny, Userpilot, Pendo
- **Cases públicos verificáveis:** Fyxer, Amplitude, HubSpot, Loom, Webflow, Notion, Slack, Pipe Drive, Reforge, Pinterest, Snowflake, e mais

---

## Como instalar

### Em claude.ai (Free, Pro, Max, Team, Enterprise)

**Pré-requisito:** Code Execution precisa estar habilitado em `Settings > Capabilities`.

1. Abra `claude.ai` e clique no seu avatar (canto superior direito)
2. Vá em **Settings → Customize → Skills**
3. Clique em **+ Create skill**
4. Faça upload do arquivo **`gt-growth-lab.zip`**
5. A skill aparece na sua lista — toggle ON para ativar

A skill agora dispara automaticamente quando você pedir experimentos, ideias de growth, hipóteses para B2B etc. — não precisa invocar manualmente.

### Em Claude Code

Coloque a pasta `growth-experimentos-gtm/` em uma das duas localizações:

- `~/.claude/skills/growth-experimentos-gtm/` (pessoal, vale para todos os projetos)
- `.claude/skills/growth-experimentos-gtm/` (dentro do repositório do projeto, vale só para ele)

Claude Code descobre e carrega automaticamente.

### Via API

Skills customizadas podem ser usadas via API com o code execution tool. Ver [Skills API Quickstart](https://docs.claude.com).

---

## Como usar

A skill foi escrita para disparar automaticamente. Estes são exemplos de prompts que funcionam bem:

### Pedidos diretos por estágio
- *"Me dá 5 experimentos de aquisição para um SaaS B2B mid-market"*
- *"Quais experimentos rodar para destravar ativação numa indústria com ticket alto?"*
- *"Preciso de ideias de retenção para um agro tech com ciclo anual"*

### Pedidos por métrica travada
- *"Como aumentar minha taxa de free→paid de 1% para 3%?"*
- *"Meu NRR está em 95%. Quais experimentos rodar primeiro?"*
- *"Como reduzir CAC payback de 24m para 18m?"*

### Pedidos por canal
- *"Inspiração para playbook de outbound em 2026"*
- *"Experimentos de ABM Tier 1 para enterprise"*
- *"Ideias de SEO programático para B2B SaaS vertical"*

### Pedidos para diagnóstico
- *"Tenho 200 leads/mês mas só 5 SQLs. Quais experimentos sugere?"*
- *"Estou perdendo 15% dos clientes em 90 dias. O que testar?"*
- *"Quero migrar de pricing per-seat para usage-based. Como testar?"*

### Pedidos para conteúdo
- *"Me dá 3 experimentos de cross-sell para usar em post de LinkedIn"*
- *"Benchmarks de cold email B2B 2026 para citar em apresentação"*

**Dica:** quanto mais contexto sobre seu segmento, ticket médio e métrica travada, melhor o output. Experimentos não são one-size-fits-all.

---

## Estrutura da skill

```
growth-experimentos-gtm/
├── SKILL.md                              ← Roteador / índice (97 linhas)
├── README.md                             ← Este arquivo
└── references/
    ├── 00-frameworks-benchmarks.md       ← ICE, RICE, PXL + benchmarks B2B 2025-2026
    ├── 01-aquisicao.md                   ← 120 experimentos
    ├── 02-ativacao.md                    ← 65 experimentos
    ├── 03-receita.md                     ← 90 experimentos
    ├── 04-adocao.md                      ← 55 experimentos
    ├── 05-retencao.md                    ← 60 experimentos
    ├── 06-expansao.md                    ← 60 experimentos
    └── 07-indicacao.md                   ← 55 experimentos
```

**Progressive disclosure:** Claude carrega só o `SKILL.md` no início (97 linhas) e abre os arquivos de `references/` sob demanda, conforme o estágio que você pediu. Isso mantém a skill rápida mesmo com 505+ experimentos.

---

## Princípios da biblioteca

1. **Toda ideia tem hipótese, métrica e benchmark.** Sem tática solta.
2. **Volume > qualidade individual.** Programas maduros rodam 5-15 testes/mês. Win rate típico em B2B fica em ~25%.
3. **Cases públicos verificáveis primeiro.** Sempre ancorar em fonte rastreável.
4. **Métrica primária deve ser revenue/pipeline.** Opens, clicks e MQL sozinhos não são métricas primárias — só direcionais.
5. **B2B ≠ B2C.** Ciclo de venda mais longo, buying committee, ticket maior. Adaptar antes de copiar.

---

## Disclaimers

- **Não é receita pronta.** Experimento bom em SaaS pode falhar em indústria. Sempre adaptar para seu ICP, ciclo de venda e ticket médio.
- **Nem todo experimento é low-effort.** Alguns exigem build de produto, integração de dados ou time dedicado. Use ICE para priorizar pelo seu contexto.
- **Benchmarks são referências.** Variam por segmento, geografia e maturidade. Use como ponto de partida, não como verdade absoluta.
- **Rodar 1 experimento por vez por canal.** Multivariate só com volume estatístico (5k+ visitas/mês na variante).
- **Statistical significance > "achei que ficou bom".** Nunca parar teste cedo (peeking).

---

## Atualizações

Esta skill é uma versão viva. Atualizada trimestralmente com:

- Novos posts de Growth Unhinged, Reforge, SaaStr, Theory Ventures, PricingSaaS
- Mudanças em benchmarks (cold email reply rate, NRR, pipeline coverage)
- Cases públicos novos (especialmente AI-native growth)
- Frameworks emergentes

---

## Sobre os criadores

**Raphael Lassance** — CEO & Founder do Growth Team

**Growth Team** — Boutique de Arquitetura de Receita e Growth

---



Esta skill é distribuída livremente para uso pessoal e profissional. Você pode:

- ✅ Usar em projetos pessoais e da empresa
- ✅ Compartilhar a skill com seu time
- ✅ Adaptar e estender com seus próprios experimentos
- ✅ Usar os experimentos em apresentações, conteúdo e planejamento

Pedimos apenas que mantenha as fontes citadas quando aplicar os experimentos publicamente — respeito pela autoria das ideias é o que mantém a comunidade B2B saudável.

---

## Suporte

Esta skill é um trabalho de curadoria. Sugestões, correções e novos experimentos validados são bem-vindos. Se rodar um experimento da biblioteca e tiver resultados (positivos ou negativos), compartilhe — ajuda a calibrar os benchmarks.

**Versão:** 1.0
**Data:** Abril 2026
**Total de experimentos:** 505
**Autoria:** Raphael Lassance & Growth Team
