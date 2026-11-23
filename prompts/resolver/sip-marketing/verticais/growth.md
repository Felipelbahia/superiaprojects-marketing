# growth

Crescimento: aquisição, experimentos e testes A/B, retenção e churn, indicação e afiliados, GTM.

> Gerado por build_sip_index.py. Não edite à mão. Skill: `"<HUB>/.agents/skills/<nome>/SKILL.md"`; agent: `"<HUB>/.agents/agents/<nome>.md"`; workflow: `"<HUB>/.agents/workflows/<nome>.md"`.

## Skills (5)

| Skill | Use quando |
| --- | --- |
| `growth-experimentos-gtm` | Biblioteca com 500+ experimentos de Go-to-Market para B2B (growth hacking, growth marketing, sales, PLG, ABM, pricing, retenção, expansão, GEO/AI search, founder-led, AI-native GTM) com hipótese, métrica e benchmark, baseada em autoridades do segmento (Kyle Poyar/Growth Unhinged, Tom Tunguz/Theory Ventures, Reforge, CXL/Speero, Clay, ChartMogul, McKinsey, Gartner, SaaStr, PricingSaaS). Use sempre que o usuário pedir ideias de experimentos B2B, growth experiments, testes A/B, hipóteses para destravar funil B2B, sugestões de outbound, ABM, PLG, SEO, GEO, pricing, sales methodologies, retenção, NRR, expansão, indicação, ou inspiração para conteúdo de growth. Trigger também ao detectar "experimentos", "testes", "ideias de growth", "como aumentar conversão/CAC/NRR/MRR", "playbook", "reduzir churn", "aumentar pipeline", ou pedidos de curadoria de táticas para SaaS, indústria, agro, enterprise, serviço B2B. |
| `growth-frameworks` | Especialista em estratégia de crescimento: métricas AARRR, growth loops, Product-Led Growth (PLG), Lean Canvas, métricas de startup, geração de demanda e ideias e táticas de marketing. |
| `growth-indicacao-e-afiliados` | Use para desenhar programa de indicação de clientes (recompensa nos dois lados), programa de afiliados e parceiros, modelo de comissão e embaixadores, e para calcular o coeficiente viral (K-factor). Gatilhos: "programa de indicação", "afiliados", "comissão", "embaixadores", "K-factor", "loop viral". |
| `growth-retencao-e-churn` | Engineer high-converting retention engines, cancel flows, dynamic save offers, exit surveys, and dunning systems to slash voluntary and involuntary subscription churn. Also covers customer health scoring, churn prediction, expansion (upsell) signals, QBR (revisão trimestral) e renovação de contrato. |
| `growth-testes-ab` | Use para desenhar a estratégia e a estatística de testes A/B, A/B/n e multivariados: hipóteses, tamanho de amostra, significância e governança do programa de testes. Gatilhos: "teste A/B", "hipótese de teste", "significância", "MVT". |

## Agents (4)

| Agent | Use quando |
| --- | --- |
| `growth-aquisicao-de-usuarios` | Growth hacking and user acquisition specialist. |
| `growth-atracao-de-leads` | Lead generation and top-of-funnel (TOFU) marketing specialist. Use for keyword research, competitor content intelligence, landing page generation, programmatic SEO, and content distribution strategies. Examples: <example>Context: User wants to improve organic search traffic. user: "We need to rank higher for product-related keywords" assistant: "I'll use the growth-atracao-de-leads agent to conduct keyword research and develop an SEO content strategy." <commentary>This requires SEO expertise and content gap analysis, so delegate to the growth-atracao-de-leads.</commentary></example> <example>Context: User needs landing pages for a campaign. user: "Create landing pages for our new product launch" assistant: "Let me deploy the growth-atracao-de-leads agent to generate high-converting landing page copy." <commentary>Landing page generation requires conversion-focused copywriting expertise.</commentary></example> |
| `growth-expansao-de-receita` | Revenue expansion specialist. Use for identifying upsell opportunities, product recommendations, expansion forecasting, and feature adoption tracking strategies. Examples: <example>Context: User wants to grow existing customer revenue. user: "How can we increase revenue from current customers?" assistant: "I'll use the growth-expansao-de-receita agent to identify expansion opportunities and design upsell campaigns." <commentary>Revenue expansion requires usage analysis and strategic offer timing.</commentary></example> <example>Context: User launching new features. user: "Promote our new premium features to existing users" assistant: "Let me deploy the growth-expansao-de-receita agent to create feature adoption campaigns with upgrade paths." <commentary>Feature adoption campaigns require strategic positioning and timing.</commentary></example> |
| `growth-retencao-de-clientes` | Customer retention and engagement specialist. Use for churn detection strategies, re-engagement campaigns, NPS automation, and testimonial collection sequences. Examples: <example>Context: User is seeing customer churn. user: "Our customer retention rate is dropping" assistant: "I'll use the growth-retencao-de-clientes agent to analyze churn patterns and design re-engagement campaigns." <commentary>Retention strategy requires behavioral analysis and lifecycle marketing expertise.</commentary></example> <example>Context: User wants customer feedback. user: "Set up an NPS survey program" assistant: "Let me deploy the growth-retencao-de-clientes agent to design an NPS automation with follow-up sequences." <commentary>NPS programs require strategic timing and response workflows.</commentary></example> |

## Workflows (2)

| Workflow | Use quando |
| --- | --- |
| `/growth-aquisicao-de-demanda` | Multi-channel demand generation, paid media optimization, SEO strategy, and partnership programs for Series A+ startups. Includes CAC calculator, channel playbooks, HubSpot integration, and international expansion tactics. Use when planning demand generation campaigns, optimizing paid media, building SEO strategies, establishing partnerships, or when user mentions demand gen, paid ads, LinkedIn ads, Google ads, CAC, acquisition, lead generation, or pipeline generation. |
| `/growth-teste-ab` | Gera o plano de um teste A/B de marketing (hipótese, variantes, critério estatístico e cronograma mínimo). Use quando for testar um elemento de e-mail, landing page, anúncio ou site. |

