---
name: growth-experimentos-gtm
description: Biblioteca com 500+ experimentos de Go-to-Market para B2B (growth hacking, growth marketing, sales, PLG, ABM, pricing, retenção, expansão, GEO/AI search, founder-led, AI-native GTM) com hipótese, métrica e benchmark, baseada em autoridades do segmento (Kyle Poyar/Growth Unhinged, Tom Tunguz/Theory Ventures, Reforge, CXL/Speero, Clay, ChartMogul, McKinsey, Gartner, SaaStr, PricingSaaS). Use sempre que o usuário pedir ideias de experimentos B2B, growth experiments, testes A/B, hipóteses para destravar funil B2B, sugestões de outbound, ABM, PLG, SEO, GEO, pricing, sales methodologies, retenção, NRR, expansão, indicação, ou inspiração para conteúdo de growth. Trigger também ao detectar "experimentos", "testes", "ideias de growth", "como aumentar conversão/CAC/NRR/MRR", "playbook", "reduzir churn", "aumentar pipeline", ou pedidos de curadoria de táticas para SaaS, indústria, agro, enterprise, serviço B2B. NÃO use para estratégia geral de growth e métricas (use growth-frameworks), para rodar o teste A/B em si (use growth-testes-ab) nem para experimentos de B2C ou conteúdo de redes sociais.
license: MIT
metadata:
  author: Antigravity Multi-IA Hub & Felipe Bahia (Futuro Mercado)
  version: 1.0.0
---

# GT Growth Lab

Biblioteca curada com **505 experimentos de Go-to-Market para B2B**. Cada experimento é entregue no formato hipótese + métrica + benchmark/fonte para ser executável imediatamente. Estruturada por estágio do funil B2B (Aquisição → Ativação → Receita → Adoção → Retenção → Expansão → Indicação) para encaixar em qualquer framework de revenue ou diagnóstico.

---

## Como navegar a skill

Esta SKILL.md é o índice. Os experimentos completos estão em arquivos separados em `references/`. Carregue apenas o(s) arquivo(s) relevante(s) para a pergunta:

| Estágio | Arquivo | Volume |
|---|---|---|
| **Aquisição** (cold email, ABM, LinkedIn, SEO, GEO, ads, eventos, founder-led, AI-native) | `references/01-aquisicao.md` | ~120 experimentos |
| **Ativação** (onboarding, time-to-value, setup, aha moment, AI-powered) | `references/02-ativacao.md` | ~65 experimentos |
| **Receita** (pricing, sales methodologies, demo, propostas, AI sales) | `references/03-receita.md` | ~90 experimentos |
| **Adoção** (feature adoption, QBR, health score, communities, AI CS) | `references/04-adocao.md` | ~55 experimentos |
| **Retenção** (churn, cancellation flow, renewals, win-back, AI retention) | `references/05-retencao.md` | ~60 experimentos |
| **Expansão** (upsell, cross-sell, multi-seat, multi-product, AI expansion) | `references/06-expansao.md` | ~60 experimentos |
| **Indicação** (referral, partner, G2, advocacy, influencer, AI advocacy) | `references/07-indicacao.md` | ~55 experimentos |
| **Frameworks e benchmarks B2B 2025-2026** | `references/00-frameworks-benchmarks.md` | toolkit |

**Total: ~505 experimentos.**

---

## Quando usar esta skill

Trigger imediato quando o usuário disser ou pedir:
- "Me dá ideias de experimentos para [estágio/métrica]"
- "Como destravar [conversão/CAC/NRR/churn] no funil B2B?"
- "Inspiração para campanha de [outbound/ABM/PLG/SEO]"
- "Benchmark de B2B SaaS / indústria / agro 2025-2026"
- "O que outras empresas estão fazendo em [tema]?"
- Pedidos de curadoria de táticas, planejamento de growth, conteúdo educativo sobre experimentos

Se o pedido for genérico ("me dá experimentos"), pergunte primeiro qual estágio ou qual métrica está travada antes de carregar arquivos. Se já estiver claro, abra direto o arquivo correspondente.

---

## Princípios não-negociáveis

1. **Toda ideia tem hipótese, métrica e benchmark.** Formato padrão: *"Se [mudança], então [resultado] porque [racional], medido por [métrica], benchmark de [valor]."*
2. **Volume de experimentos > qualidade individual.** Programas maduros rodam 5-15 testes/mês. Win rate típico de A/B test em B2B fica em ~25%.
3. **ICE como default, PXL para times maduros.** Detalhes em `references/00-frameworks-benchmarks.md`.
4. **Cases públicos verificáveis primeiro.** Sempre ancorar a ideia em case com dado verificável (Fyxer, Amplitude, HubSpot, Loom, Webflow, Notion, Slack, Reforge, Pinterest, Pipe Drive) ou em benchmark agregado de fonte autoritativa.
5. **Métrica primária deve ser de revenue/pipeline.** Opens, clicks e MQL sozinhos não são métricas primárias — só direcionais.

---

## Como propor experimentos ao usuário

Ao receber um pedido, seguir esta ordem:

1. **Identificar estágio** do funil (Aquisição → Indicação) e métrica travada
2. **Carregar o arquivo de referência** correspondente em `references/`
3. **Selecionar 5-10 experimentos** mais alinhados com:
   - Tamanho de empresa (SMB, mid-market, enterprise)
   - Segmento (SaaS, indústria, agro, serviço, varejo B2B)
   - Maturidade do time (cedo, scaling, escalado)
   - Recurso disponível (low-effort vs heavy build)
4. **Aplicar ICE rápido** para ranquear top 3
5. **Perguntar 1-2 informações para refinar** (ICP, ticket médio, canal atual)

**Não despejar 40 ideias de uma vez.** Trabalhar em batches de 5-10, deixar o usuário escolher direção e aprofundar.

---

## Anti-padrões a evitar

- Otimizar opens/clicks em vez de meetings booked / pipeline / revenue
- Parar teste cedo ("peeking") antes de atingir significância estatística
- Mudar 2+ variáveis sem multivariate
- Lift estatisticamente significativo mas pratico irrelevante (ex: +0.5% sem volume)
- Rodar teste sem tracking de qualidade do lead (volume sem MQL→SQL)
- Copiar tática de B2C para B2B sem ajustar ciclo de venda e buying committee
- Recomendar "double pricing" ou mudanças de preço sem validar com pesquisa qualitativa primeiro

---

## Manutenção

Esta skill deve ser atualizada trimestralmente com:
- Novos posts de Growth Unhinged, Reforge, SaaStr, Theory Ventures, PricingSaaS
- Mudanças em benchmarks (cold email reply rate, NRR, pipeline coverage, ciclo médio)
- Cases públicos verificáveis novos (especialmente AI-native growth)
- Frameworks emergentes (GTM Engineer, growth engineering, AI-native GTM)

Ao adicionar novos experimentos:
- Manter formato hipótese + métrica + benchmark
- Citar fonte específica (não "uma empresa" — citar a empresa)
- Mapear para o estágio correto do funil
- Limite de uma citação direta por fonte (regra de copyright)
