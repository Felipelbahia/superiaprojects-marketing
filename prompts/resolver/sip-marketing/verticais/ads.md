# ads

Campanhas pagas (Google, Meta, multiplataforma), criativos, copy de anúncio, análise de desempenho e extração de anúncios de concorrentes.

> Gerado por build_sip_index.py. Não edite à mão. Skill: `"<HUB>/.agents/skills/<nome>/SKILL.md"`; agent: `"<HUB>/.agents/agents/<nome>.md"`; workflow: `"<HUB>/.agents/workflows/<nome>.md"`.

## Skills (6)

| Skill | Use quando |
| --- | --- |
| `ads-analise-de-desempenho` | O cérebro financeiro e analítico do tráfego pago. Aloca verba entre múltiplos canais (Google, Meta, LinkedIn) baseado em MER/CAC, audita e diagnostica desvios de CPA, caça desperdícios orçamentários (Wasted Spend), implementa regras de corte automático (Auto-Pause), projeta ROAS e gera parâmetros de rastreamento UTM padronizados. Use para decidir onde e quanto investir em mídia paga e para analisar, comparar e vigiar o resultado de Google e Meta juntos (estratégia, diagnóstico, orçamento, pacing e relatório). |
| `ads-copy-de-anuncio` | Use para escrever o texto dos anúncios pagos: títulos e descrições de Google Search (RSA), textos primários curtos e longos de Meta Ads, roteiros de TikTok Ads e anúncios de LinkedIn Ads, com matriz de testes de copy. Gatilhos: "copy de anúncio", "RSA", "texto primário", "variações de anúncio". |
| `ads-criativos` | Use para conceber, roteirizar e validar criativos de mídia paga (vídeo UGC, motion, estáticos), combater fadiga de criativo, analisar anúncios de concorrentes e montar pipelines de anúncio com IA generativa. Gatilhos: "criativo de anúncio", "UGC", "fadiga de criativo", "ad spy". |
| `ads-google` | Use para estruturar e otimizar contas de Google Ads (Search, Performance Max, YouTube, Display): arquitetura temática, mineração de termos de busca, Quality Score, canibalização de palavras-chave, extensões e lances inteligentes. Gatilhos: "Google Ads", "PMax", "termos de busca", "Quality Score", "Smart Bidding". |
| `ads-meta` | Use para estruturar e otimizar contas de Meta Ads (Facebook e Instagram): Advantage+, CBO e ABO, públicos Broad e Lookalike, sobreposição de públicos, retargeting por janela e controle de frequência. Gatilhos: "Meta Ads", "Facebook Ads", "Instagram Ads", "lookalike", "CBO". |
| `ads-multiplataforma` | Use para planejar mídia paga fora do Google e do Meta: LinkedIn Ads para ABM e prospecção B2B de ticket alto, TikTok Ads, Reddit Ads e especificações técnicas por plataforma. Gatilhos: "LinkedIn Ads", "TikTok Ads", "Reddit Ads", "ABM pago". |

## Agents (1)

| Agent | Use quando |
| --- | --- |
| `ads-trafego-pago` | Especialista em gestão de tráfego pago, mídia de performance e aquisição de clientes. Use quando precisar planejar, estruturar, analisar ou otimizar campanhas de anúncios em Google Ads, Meta Ads (Facebook/Instagram), TikTok Ads, LinkedIn Ads ou redes alternativas, com foco em CAC, ROAS e escala rentável.\n\n<example>\nContext: O usuário precisa estruturar uma campanha de lançamento de infoproduto ou SaaS no Meta Ads.\nuser: "Como devo estruturar a campanha de tráfego pago para o lançamento da <marca> no Meta?"\nassistant: "Vou acionar o ads-trafego-pago para desenhar a arquitetura de campanha no Meta Ads com distribuição CBO, públicos Broad e testes de criativos."\n<commentary>\nA demanda exige estratégia avançada de tráfego pago, delegando ao especialista de mídia de performance.\n</commentary>\n</example>\n\n<example>\nContext: O CPA de uma campanha de Google Search subiu e o usuário precisa de um plano de otimização.\nuser: "Nosso custo por lead no Google Ads dobrou esta semana. Pode auditar os termos de busca?"\nassistant: "Acionando o ads-trafego-pago para conduzir uma auditoria de Search Term Mining e Quality Score no Google Ads."\n<commentary>\nDiagnóstico de performance e redução de desperdício em mídia paga.\n</commentary>\n</example> |

## Workflows (2)

| Workflow | Use quando |
| --- | --- |
| `/ads-copy-de-anuncio` | Generate high-converting ad copy for Google Ads, Meta (Facebook/Instagram), LinkedIn, and TikTok. Creates multiple variations with A/B testing in mind. Includes headlines, descriptions, CTAs, and platform-specific formats. Use when creating ads, generating ad variations, or A/B testing ad copy. |
| `/ads-extracao-de-anuncios-concorrentes` | Extracts and analyzes competitors' ads from ad libraries (Facebook, LinkedIn, etc.) to understand what messaging, problems, and creative approaches are working. Helps inspire and improve your own ad campaigns. |

