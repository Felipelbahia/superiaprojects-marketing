---
name: sip-marketing
description: Use whenever the current task involves marketing, content, copywriting, branding, social media, SEO, paid ads, email, PR, growth, sales enablement or marketing analytics but the active project has no local marketing skills — i.e. any project other than "SIP - Marketing" (0 Mkt) itself. Routes the task to the central marketing knowledge hub instead of improvising from general knowledge. Also use when the user asks "existe algo de marketing pra isso", "tem skill de marketing no hub", "consulta o SIP - Marketing", or names a 0 Mkt skill, agent or workflow explicitly in a project that isn't the hub.
---

# sip-marketing

## Por que isso existe

O projeto `SIP - Marketing` (`/Users/macbookpro/Documents/IA Projects/_Plataforma/0 Mkt`) é a referência central de marketing: skills especialistas (lista gerada abaixo), agents de marketing em `.agent/agents/` e workflows `/comando` em `.agent/workflows/`. Esse conhecimento só é descoberto automaticamente dentro do próprio hub.

**Esta skill é um redirecionador:** o projeto consumidor instala só ela (um symlink). Ela não ensina marketing; leva até quem ensina. Skills, agents e workflows ficam no hub e são lidos **por caminho absoluto**. Não symlinke nem copie nenhum deles para o projeto.

## Passo 0 — acesso ao caminho

Leitura de arquivo fora do diretório de trabalho pode pedir aprovação do usuário na primeira vez. Isso é esperado. Sempre use o caminho absoluto entre aspas: `"/Users/macbookpro/Documents/IA Projects/_Plataforma/0 Mkt"`.

## Passo 1 — marca e destino ficam no projeto consumidor

As skills do hub foram escritas para o 0 Mkt, que guarda marcas em `_brands/<marca>/` e grava saídas conforme `docs/mapa-de-destinos.md` **dele**. Num projeto consumidor:

- **Marca:** use os arquivos de marca do próprio projeto (voz, personas, pilares, guia de estilo). Se o projeto não tiver e o pedido não disser qual marca, pergunte antes de escrever. Não leia `_brands/` do hub como se fosse a marca do projeto.
- **Onde gravar:** siga o `docs/mapa-de-destinos.md` do projeto consumidor. Se ele não existir, siga a skill `mapa-de-destinos` (via `sip-geral`) (cria o mapa mínimo). **Nunca grave peça, plano ou rascunho dentro do hub.**
- **Anti-slop:** todo texto entregue passa pela skill `geral-anti-slop` do hub antes de sair.

## Passo 2 — classifique a tarefa

| Tipo de tarefa | O que fazer |
| --- | --- |
| **Consulta pontual** (como escrever X, qual estrutura para Y) | **Modo consulta**: ache a skill na tabela abaixo, leia só o `SKILL.md` dela e aplique inline. |
| **Peça ou campanha grande / multi-arquivo** | **Modo dispatch**: subagente carregado com a persona de um agent do hub. |
| **Procedimento com nome** ("tem um /comando pra isso?") | Leia o workflow correspondente em `.agent/workflows/` do hub e siga. |
| **Não sabe qual skill** | Leia o workflow `geral-navegador-de-skills` ou o agent `geral-navegador-de-comandos` do hub. |

## Modo consulta (padrão — prefira este)

1. Ache a skill na tabela abaixo pela coluna "Use quando".
2. Leia só o `SKILL.md` dela: `"/Users/macbookpro/Documents/IA Projects/_Plataforma/0 Mkt/.agent/skills/<nome>/SKILL.md"`. Abra `references/` da skill só se o `SKILL.md` mandar.
3. Aplique o conteúdo inline. Avise o usuário em uma linha que a resposta veio do hub `SIP - Marketing`, não de conhecimento genérico.

## Modo dispatch (só para construções grandes)

Não existe invocação nativa de agente cross-projeto no Claude Code. Disparar um agent do hub é montar um subagente genérico (`Agent`, `subagent_type: "general-purpose"`) com a persona colada no prompt:

1. Liste `"/Users/macbookpro/Documents/IA Projects/_Plataforma/0 Mkt/.agent/agents/"` e escolha o agent cujo nome bate com a tarefa (ex.: `copy-redacao-publicitaria`, `social-calendario-e-distribuicao`, `pr-relacoes-publicas`).
2. Leia o `.md` inteiro do agent e as skills que ele cita no frontmatter `skills:`.
3. Chame `Agent` com a persona + a tarefa + o caminho da marca e do mapa de destinos **do projeto consumidor**.
4. Revise o resultado com `geral-anti-slop` antes de entregar.

## Agents do hub

Em `"/Users/macbookpro/Documents/IA Projects/_Plataforma/0 Mkt/.agent/agents/"` (um `.md` por agent). Não são instalados no consumidor: leia pelo caminho absoluto.

## Workflows do hub

Em `"/Users/macbookpro/Documents/IA Projects/_Plataforma/0 Mkt/.agent/workflows/"` (um `.md` por `/comando`). Só use um workflow que exista lá; não invente `/comando`. Leia o `.md` e siga o procedimento.

## Skills do hub

Tabela gerada das `description` de cada skill (só a parte "use quando"; o "NÃO use" está no `SKILL.md` de cada uma). Regenerar a partir da raiz do hub: `python3 .agent/scripts/build_sip_index.py`. Não edite à mão.

<!-- skills:start (gerado por .agent/scripts/build_sip_index.py — não edite à mão) -->

Total: 99 skills.

### ads

| Skill | Use quando |
| --- | --- |
| `ads-analise-de-desempenho` | O cérebro financeiro e analítico do tráfego pago. Aloca verba entre múltiplos canais (Google, Meta, LinkedIn) baseado em MER/CAC, audita e diagnostica desvios de CPA, caça desperdícios orçamentários (Wasted Spend), implementa regras de corte automático (Auto-Pause), projeta ROAS e gera parâmetros de rastreamento UTM padronizados. Use para decidir onde e quanto investir em mídia paga e para analisar, comparar e vigiar o resultado de Google e Meta juntos (estratégia, diagnóstico, orçamento, pacing e relatório). |
| `ads-copy-de-anuncio` | Use para escrever o texto dos anúncios pagos: títulos e descrições de Google Search (RSA), textos primários curtos e longos de Meta Ads, roteiros de TikTok Ads e anúncios de LinkedIn Ads, com matriz de testes de copy. Gatilhos: \"copy de anúncio\", \"RSA\", \"texto primário\", \"variações de anúncio\". |
| `ads-criativos` | Use para conceber, roteirizar e validar criativos de mídia paga (vídeo UGC, motion, estáticos), combater fadiga de criativo, analisar anúncios de concorrentes e montar pipelines de anúncio com IA generativa. Gatilhos: \"criativo de anúncio\", \"UGC\", \"fadiga de criativo\", \"ad spy\". |
| `ads-google` | Use para estruturar e otimizar contas de Google Ads (Search, Performance Max, YouTube, Display): arquitetura temática, mineração de termos de busca, Quality Score, canibalização de palavras-chave, extensões e lances inteligentes. Gatilhos: \"Google Ads\", \"PMax\", \"termos de busca\", \"Quality Score\", \"Smart Bidding\". |
| `ads-meta` | Use para estruturar e otimizar contas de Meta Ads (Facebook e Instagram): Advantage+, CBO e ABO, públicos Broad e Lookalike, sobreposição de públicos, retargeting por janela e controle de frequência. Gatilhos: \"Meta Ads\", \"Facebook Ads\", \"Instagram Ads\", \"lookalike\", \"CBO\". |
| `ads-multiplataforma` | Use para planejar mídia paga fora do Google e do Meta: LinkedIn Ads para ABM e prospecção B2B de ticket alto, TikTok Ads, Reddit Ads e especificações técnicas por plataforma. Gatilhos: \"LinkedIn Ads\", \"TikTok Ads\", \"Reddit Ads\", \"ABM pago\". |

### audiovisual

| Skill | Use quando |
| --- | --- |
| `audiovisual-agentes-de-voz` | Use para criar agentes conversacionais de voz com a plataforma ElevenLabs: SDR de voz para prospecção e qualificação, atendimento ao cliente, bots telefônicos e experiências interativas em tempo real. Gatilhos: \"agente de voz\", \"SDR de voz\", \"bot telefônico\", \"ElevenLabs agents\". |
| `audiovisual-apresentacoes-educacionais` | Use para planejar, melhorar e validar apresentações de ensino: aula, treinamento, workshop, webinar e palestra, com ciência da aprendizagem (carga cognitiva, 12 princípios de Mayer, 9 eventos de Gagné, design C.R.A.P.) e acessibilidade (WCAG 2.1 AA). Gatilhos: \"slides de aula\", \"apresentação de treinamento\", \"workshop\", \"webinar\", \"slides que ensinam\", \"revisar meus slides\". |
| `audiovisual-banco-de-midias-openverse` | Use para buscar fotos, ilustrações, vetores, áudios e vídeos livres (domínio público e Creative Commons CC0 e CC-BY) na API do Openverse, com fallback no Wikimedia Commons e atribuição legal pronta. Gatilhos: \"imagem livre\", \"Creative Commons\", \"banco de imagens gratuito\", \"Openverse\". |
| `audiovisual-imagem-flux-api` | Use para integrar a API da BFL (FLUX) em código: endpoints, polling assíncrono, limites de taxa, tratamento de erro, webhooks e endpoints regionais, com exemplos em Python e TypeScript. Gatilhos: \"FLUX API\", \"BFL API\", \"polling FLUX\", \"webhook FLUX\". |
| `audiovisual-imagem-flux-prompts` | Use para escrever prompts para os modelos de imagem FLUX.2 e FLUX.1 (BFL): texto para imagem, imagem para imagem, JSON estruturado, cores em hex, tipografia e edição com várias referências. Gatilhos: \"prompt FLUX\", \"gerar imagem com FLUX\", \"edição multi-referência\". |
| `audiovisual-pitch-deck` | Use para montar a narrativa e a estrutura de pitch decks para investidores (padrão Y Combinator) e decks comerciais de alto impacto, com storytelling financeiro e design executivo. Gatilhos: \"pitch deck\", \"deck de investidor\", \"rodada seed\", \"deck comercial\". |
| `audiovisual-podcast-e-audio` | Use para pós-produção de áudio: edição, mixagem e masterização de podcasts, conformidade ACX de audiobooks, transcrição com Whisper, direção de locução e sound design. Gatilhos: \"masterizar podcast\", \"ACX\", \"audiobook\", \"locução\", \"limpar áudio\". |
| `audiovisual-qr-code` | Generate QR codes with URLs and UTM tracking. Exports PNG/SVG with captions. Use for single codes, batch generation, or marketing campaigns with tracking parameters. |
| `audiovisual-slidev` | Comprehensive guide for Slidev - a web-based presentation framework for developers. Covers Markdown syntax, layouts, components, animations, theming, and exporting. Use this skill when creating or working with developer presentations using Slidev. |
| `audiovisual-transcricao` | Transcribe audio to text using ElevenLabs Scribe v2. Use when converting audio/video to text, generating subtitles, transcribing meetings, or processing spoken content. |

### brand

| Skill | Use quando |
| --- | --- |
| `brand-audience` | Use para definir ou refazer personas, segmentos, jobs to be done, objeções e hábitos de mídia de uma marca (etapa 3 do brand-builder). Gatilhos: \"persona da marca\", \"público da marca\", \"personas finas\". |
| `brand-builder` | Use para construir ou aprofundar as fundações de uma marca de _brands/, uma etapa por vez e com aprovação: essência, posicionamento, público, voz, desejo, direção visual, design system, ativação e brandbook. Gatilhos: \"brandbook\", \"marca nova\", \"arquivos de marca finos\", \"posicionamento da marca\". |
| `brand-design-system` | Use para montar o design system da marca como site de referência mais DESIGN.md (paleta com modo escuro, tipografia, espaço, forma, movimento, componentes e tokens), a partir da direção visual aprovada (etapa 7 do brand-builder). Gatilhos: \"design system da marca\", \"DESIGN.md\", \"tokens da marca\". |
| `brand-essence` | Use para definir ou aprofundar essência, crenças, história de origem, inimigo, posicionamento, categoria e arquétipo de uma marca (etapas 1 e 2 do brand-builder). Gatilhos: \"propósito\", \"posicionamento da marca\", \"Primal Branding\", \"arquétipo\". |
| `brand-identidade-sonora` | Use para definir a identidade sonora de uma marca: logo sonoro (1 a 3 segundos), estética de voz, moodboard de áudio e diretrizes de trilha, efeitos e silêncio para vídeo, podcast, aplicativo e eventos (etapa 8, uso audiovisual, do brand-builder). Gatilhos: \"logo sonoro\", \"identidade sonora\", \"trilha da marca\", \"sonic branding\". |
| `brand-naming` | Use para criar e validar nomes de marca, produto e empresa pelo protocolo dos 6 portões (briefing, geração, fonético, jurídico, AEO e narrativa). Gatilhos: \"nome da marca\", \"naming\", \"rebranding de nome\", \"nome para a empresa\". |
| `brand-visual-direction` | Use para decidir direção visual, mood, estilo de imagem, intenção de cor e tipografia e visual de vídeo antes do design system (etapa 6 do brand-builder). Gatilhos: \"direção visual\", \"moodboard\", \"como a marca deve parecer\", \"tendências visuais\". |
| `brand-visual-style` | Use para criar, extrair e aplicar um sistema visual portátil em um arquivo visual-style.md (cores, tipografia, layout, movimento e humor em um só arquivo que qualquer IA lê): criar do zero, extrair de um site, vídeo ou PDF de marca, aplicar em vídeo (HeyGen), slides HTML, Figma ou paper.design, ou consultar a galeria de estilos prontos (Suíço, Saul Bass, Game Boy etc.). Gatilhos: \"visual style\", \"estilo visual\", \"brand style\", \"style guide\". |
| `brand-voice-messaging` | Use para definir ou refazer tom de voz, vocabulário, \"o que NÃO comunicar\", mensagens e pilares de conteúdo de uma marca (etapa 4 do brand-builder), ou extrair a voz de textos existentes. Gatilhos: \"tom de voz\", \"brand voice\", \"pilares de conteúdo\", \"o que não comunicar\". |

### conteudo

| Skill | Use quando |
| --- | --- |
| `conteudo-briefing` | Use para montar briefings de conteúdo completos para redatores, com objetivo, público, ângulo, estrutura e critérios de aprovação, em qualquer formato. Gatilhos: \"briefing de conteúdo\", \"brief para redator\", \"pauta para freela\". |
| `conteudo-estrategia` | Use para planejar o conteúdo de uma marca: estratégia e playbook, pilares editoriais, calendário editorial, formatos, distribuição, geração de ideias a partir do posicionamento, análise de lacunas de conteúdo contra concorrentes e guia de estilo. Gatilhos: \"teia de conteúdo\", \"webfluence\", \"isca digital\", \"lead magnet\", \"estratégia de conteúdo\", \"calendário editorial\", \"pilares de conteúdo\", \"ideias de conteúdo\", \"onde distribuir\", \"lacuna de conteúdo\", \"guia de estilo\". |
| `conteudo-linha-de-producao` | Use when: orquestrar a linha de produção unificada de conteúdo de alta retenção e conversão para Reels, TikTok, Shorts e Carrosséis; conecta a marca ativa (_brands/), psicologia comportamental (revenue-sexy-canvas), mineração de dados (hook-mining), engenharia reversa (reel-analyzer e viral-carousel), geração de carrosséis via IA (social-carrossel e social-direcao-de-arte-ia), retenção visual (copy-hooks-video-curto), motores de mídia (Remotion, no projeto de edição de vídeo) e filtro anti-slop. |
| `conteudo-pesquisa` | Research-first content creation optimized for both human readers and AI search engines (Claude, ChatGPT, Perplexity, Gemini). Creates authentic, authoritative content that becomes the go-to citation source for AI models answering user questions. Use this skill when: - Creating content that should appear in AI search results (Perplexity, ChatGPT, Claude) - Building topical authority to become THE source AI cites for a topic - Launching a new product and need compelling, citable content - Creating blog posts, articles, social media, or press releases - Need content that references real trends, people, and recent events - Want AI-assisted content that doesn't sound AI-generated - Creating thought leadership content in any industry Triggers: "create content for", "write about", "research and write", "find experts for", "content for launch", "blog post about", "article on", "press release for", "AI search", "show up in AI", "Perplexity", "be cited by AI" This skill is for CREATING content with research. |
| `conteudo-post-de-blog` | Transform brain dumps into polished blog posts in the brand's own voice. Use when the user wants to write a blog post with scattered ideas, talking points, and conclusions that need organization into a cohesive, conversational narrative. |
| `conteudo-reaproveitamento` | One-to-many content multiplication engine. Transform long-form assets (podcasts, webinars, whitepapers, pillar articles) into high-performing social posts, email newsletters, carousels, and video scripts using semantic content architectures. |
| `conteudo-tendencias` | Use para pesquisar tendências de tópicos em Google Trends, Google Analytics, Reddit, LinkedIn, X, Substack, Medium, blogs, podcasts e YouTube e gerar esboços de artigo a partir da intenção de busca. Gatilhos: \"o que está em alta\", \"tendência de conteúdo\", \"tema do momento\", \"esboço baseado em dados\". |

### copy

| Skill | Use quando |
| --- | --- |
| `copy-conversao` | Enterprise conversion copywriting, direct response methodologies, sales letters, CTA optimization, buyer psychology, and persuasion architecture based on Eugene Schwartz, Dan Kennedy, Gary Halbert, Donald Miller (StoryBrand), and Robert Cialdini. |
| `copy-hooks-video-curto` | Use when: escrever, planejar ou revisar o hook (primeiros 3 segundos) de um Reel, TikTok ou Short, tanto a fala (segmentação, promessa, loop aberto, quadro mental, nostalgia, 'funciona mesmo que', matriz going-viral de objetivo único e emoção primária high-arousal) quanto o que aparece na tela (frame 0 em movimento, texto grande, funciona no mudo, técnica de payoff postergado); diagnosticar por que um vídeo curto flopou; implementar conversão comentário -> DM sem link público. Complementa vsl-conrado-framework.md. |
| `copy-landing-page` | Design, write, and optimize high-converting landing pages. Section-by-section copywriting architecture (Hero, Problem, Solution, Features/Benefits, Social Proof, Objection Killing, Risk Reversal, FAQ, Final CTA) and CRO diagnostic audits. |
| `copy-metodos-classicos` | Use para aplicar o método de um livro clássico de copywriting, persuasão e marketing a uma peça ou estratégia: Gary Halbert (Boron Letters), David Ogilvy, Eugene Schwartz (5 níveis de consciência), Dan Kennedy, Russell Brunson (Expert Secrets), Heath (Made to Stick), Seth Godin (Permission Marketing e Purple Cow) e StoryBrand. Gatilhos: \"nível de consciência\", \"método Halbert\", \"estilo Ogilvy\", \"StoryBrand\", \"copy de resposta direta\", \"ideia que gruda\". |
| `copy-saas` | Copywriter de SaaS e startups focado em posicionamento, mensagem e pesquisa de voz do cliente (VOC), com um fluxo de 10 fases para criar uma landing page. Use para definir posicionamento e proposta de valor, montar a hierarquia de mensagem, minerar a linguagem do cliente e planejar o processo de uma landing page de SaaS. |
| `copy-vsl` | Use para escrever roteiro de VSL (Video Sales Letter) de resposta direta: estrutura em 8 partes de Conrado Adolpho, tratamento universal de objeções, ritmo slide a slide e textos de retenção na tela. Gatilhos: \"VSL\", \"carta de vendas em vídeo\", \"roteiro de vendas em vídeo\". |

### data

| Skill | Use quando |
| --- | --- |
| `data-atribuicao-e-relatorios` | Especialista em modelagem de atribuição multi-canal, geração de relatórios executivos de marketing, auditoria de saúde de contas e dashboards automatizados para liderança. Use para contar o resultado do marketing em todos os canais. |
| `data-funil-e-coortes` | Use para analisar queda de funil (drop-off), retenção por coortes, ativação de usuários, onboarding e paywall em produtos digitais. Gatilhos: \"drop-off\", \"coorte\", \"ativação\", \"onboarding que não converte\", \"paywall\". |
| `data-web-ga4` | Use para arquitetar dados web e implementar tracking: GA4, Google Tag Manager (web e server-side), Consent Mode v2, dataLayer e modelagem de eventos em BigQuery. Gatilhos: \"GA4\", \"GTM\", \"dataLayer\", \"Consent Mode\", \"evento de conversão\". |

### email

| Skill | Use quando |
| --- | --- |
| `email-automacao` | Arquiteto de jornadas automatizadas de email e automações de ciclo de vida em CRMs (ActiveCampaign, HubSpot, Customer.io). Estrutura Welcome Series em 5 etapas, esteiras de onboarding e ativação de produto SaaS, fluxos de recuperação de carrinho abandonado, automações de reengajamento e Sunset Policy contra contatos inativos. |
| `email-copy` | Use para escrever e-mails de marketing que convertem: linhas de assunto, preheaders, narrativas (Story-Lesson-Offer, Soap Opera, Seinfeld), texto puro versus HTML leve e otimização de CTOR. Gatilhos: \"assunto de e-mail\", \"copy de e-mail\", \"sequência de e-mails\". |
| `email-entregabilidade` | Use para proteger a entregabilidade de e-mail (inbox placement): registros DNS (SPF, DKIM, DMARC, BIMI), aquecimento de domínio de 21 dias, higiene de lista contra spam traps e monitoramento de reputação no Google Postmaster. Gatilhos: \"caiu no spam\", \"SPF DKIM DMARC\", \"warm-up\", \"reputação de domínio\". |
| `email-newsletter` | Use para transformar a experiência diária do autor em rascunhos de newsletter prontos para publicar, com playbooks editoriais, estratégias de crescimento, curadoria e modelos por setor (Tech, Fintech, RH, Vendas, Operações). Gatilhos: \"newsletter\", \"edição semanal\", \"crescer newsletter\". |

### geral

| Skill | Use quando |
| --- | --- |
| `geral-anti-slop` | Detects and removes AI writing patterns from text. Use when polishing drafts, cleaning AI-generated content, or ensuring writing sounds authentically human. Invoke with "run through slop detector", "clean this up", or "remove AI fingerprints". |
| `geral-conformidade-lgpd` | Use para conformidade de marketing digital: LGPD e GDPR, consentimento (Consent Mode v2), formulários de captura, revisão de contratos, NDAs de influenciadores e análise de termos de uso. É triagem para orientar o trabalho de marketing; a decisão jurídica final é de advogado. Gatilhos: \"LGPD\", \"GDPR\", \"consentimento\", \"política de privacidade\", \"NDA\", \"contrato de influenciador\". |

### growth

| Skill | Use quando |
| --- | --- |
| `growth-experimentos-gtm` | Biblioteca com 500+ experimentos de Go-to-Market para B2B (growth hacking, growth marketing, sales, PLG, ABM, pricing, retenção, expansão, GEO/AI search, founder-led, AI-native GTM) com hipótese, métrica e benchmark, baseada em autoridades do segmento (Kyle Poyar/Growth Unhinged, Tom Tunguz/Theory Ventures, Reforge, CXL/Speero, Clay, ChartMogul, McKinsey, Gartner, SaaStr, PricingSaaS). Use sempre que o usuário pedir ideias de experimentos B2B, growth experiments, testes A/B, hipóteses para destravar funil B2B, sugestões de outbound, ABM, PLG, SEO, GEO, pricing, sales methodologies, retenção, NRR, expansão, indicação, ou inspiração para conteúdo de growth. Trigger também ao detectar "experimentos", "testes", "ideias de growth", "como aumentar conversão/CAC/NRR/MRR", "playbook", "reduzir churn", "aumentar pipeline", ou pedidos de curadoria de táticas para SaaS, indústria, agro, enterprise, serviço B2B. |
| `growth-frameworks` | Especialista em estratégia de crescimento: métricas AARRR, growth loops, Product-Led Growth (PLG), Lean Canvas, métricas de startup, geração de demanda e ideias e táticas de marketing. |
| `growth-indicacao-e-afiliados` | Use para desenhar programa de indicação de clientes (recompensa nos dois lados), programa de afiliados e parceiros, modelo de comissão e embaixadores, e para calcular o coeficiente viral (K-factor). Gatilhos: \"programa de indicação\", \"afiliados\", \"comissão\", \"embaixadores\", \"K-factor\", \"loop viral\". |
| `growth-retencao-e-churn` | Engineer high-converting retention engines, cancel flows, dynamic save offers, exit surveys, and dunning systems to slash voluntary and involuntary subscription churn. Also covers customer health scoring, churn prediction, expansion (upsell) signals, QBR (revisão trimestral) e renovação de contrato. |
| `growth-testes-ab` | Use para desenhar a estratégia e a estatística de testes A/B, A/B/n e multivariados: hipóteses, tamanho de amostra, significância e governança do programa de testes. Gatilhos: \"teste A/B\", \"hipótese de teste\", \"significância\", \"MVT\". |

### persona

| Skill | Use quando |
| --- | --- |
| `persona-descoberta-de-clientes` | Use para validar ideia, problema e solução com clientes: Mom Test, entrevista de problema e de solução, Customer Development (Steve Blank), descoberta contínua de produto (Teresa Torres) e pesquisas (surveys). Gatilhos: \"validar ideia\", \"entrevista com clientes\", \"Mom Test\", \"descoberta de produto\". |
| `persona-icp` | Use para construir personas, perfil de cliente ideal (ICP), mapa de Jobs-to-be-Done, gatilhos de compra, roteiros de voz do cliente, pesquisa de público e pontuação de aderência ao ICP. Gatilhos: \"persona\", \"ICP\", \"cliente ideal\", \"JTBD\", \"segmentar público\". |

### pr

| Skill | Use quando |
| --- | --- |
| `pr-assessoria-de-imprensa` | Use when planejar estratégias de imprensa, produzir pautas e press releases para veículos de comunicação, redigir pitches individualizados para jornalistas, estruturar Data PR com dados proprietários, conduzir newsjacking reativo de notícias quentes, preparar media training para entrevistas ou emitir notas oficiais e holding statements de gestão de crise, detectar sinais precoces de crise, coordenar a resposta e conduzir a recuperação de reputação. Triggers: \"assessoria de imprensa\", \"press release\", \"pitch para jornalista\", \"falar com repórter\", \"gancho de notícia\", \"disparar para a mídia\", \"divulgação na imprensa\", \"nota oficial\", \"comunicação de crise\", \"media kit\", \"clipping\", \"earned media\". |

### produto

| Skill | Use quando |
| --- | --- |
| `produto-agile` | Use para gestão ágil de produto: Scrum, rituais, backlog e colaboração do time em desenvolvimento iterativo. Gatilhos: \"Scrum\", \"backlog\", \"sprint\", \"cerimônias ágeis\". |
| `produto-prd` | Use para escrever PRD (documento de requisitos de produto), histórias de usuário, métricas de produto e a etapa v0.9 de go-to-market do PRD. Gatilhos: \"criar um PRD\", \"requisitos do produto\", \"documentar uma funcionalidade\", \"especificação de produto\". |

### revenue

| Skill | Use quando |
| --- | --- |
| `revenue-campanhas` | Planejamento integrado de campanhas de marketing digital e roteamento para a skill especialista de cada frente (conteúdo, social, email, SEO, GEO, mídia paga, métricas, lançamento). Gera parâmetros UTM e valida a campanha antes do lançamento. Use para planejar uma campanha que atravessa vários canais, montar o calendário, definir o rastreamento UTM ou destravar uma campanha parada. |
| `revenue-gtm-e-posicionamento` | Use para estratégia de go-to-market e marketing de produto: posicionamento, Category Design, Value Proposition Canvas, STP (segmentação, alvo e posicionamento), pré-mortem e coordenação de lançamento entre áreas. Gatilhos: \"GTM\", \"posicionar produto\", \"proposta de valor\", \"STP\", \"categoria\". |
| `revenue-inteligencia-competitiva` | Use para inteligência competitiva estratégica: mapa de mercado, teardown de concorrente, battlecard, análise de fosso (moat), pesquisa win/loss e mapa de diferenciação. Gatilhos: \"analisar concorrente\", \"battlecard\", \"win/loss\", \"teardown\", \"diferenciação\". |
| `revenue-lancamento` | Use para planejar o lançamento de qualquer produto, serviço, curso ou funcionalidade: escolher o tipo de lançamento, montar o plano de pré-lançamento, lançamento e pós-lançamento, definir canais próprios, alugados e emprestados (ORB), lançar em fases (interno, alfa, beta, acesso antecipado e geral), usar Product Hunt e lista de espera, ou montar o lançamento como evento (fórmula de Jeff Walker). Gatilhos: \"plano de lançamento\", \"lançar meu curso\", \"lançar produto\", \"abertura de carrinho\", \"lista de espera\", \"Product Hunt\", \"anunciar funcionalidade\". |
| `revenue-lancamento-tecnico` | Use para planejar o lançamento de API, SDK, ferramenta para desenvolvedores ou produto técnico: níveis de lançamento (tiers), preparação de desenvolvedores (documentação, exemplos, SDK), mensagens de lançamento e métricas. Gatilhos: \"lançar API\", \"lançamento GA/beta\", \"release técnico\", \"preparar desenvolvedores\". |
| `revenue-modelos-mentais` | Use quando uma decisão é difícil, cara ou difícil de desfazer e pede raciocínio estruturado: pensamento de segunda ordem, decisões reversíveis ou irreversíveis, minimização do arrependimento, primeiros princípios, inversão, seis chapéus, matriz de Eisenhower, pre-mortem de projeto ou lançamento, técnicas de solução de problemas e conselho de negócio por 9 lentes. Gatilhos: \"devo fazer X\", \"vale a pena\", \"qual o risco\", \"estou travado\", \"priorizar\", \"pivotar\", \"decisão estratégica\". |
| `revenue-oferta` | Use para montar uma oferta irresistível pelo método de Alex Hormozi (\"$100M Offers\"): equação de valor, empilhamento de bônus, garantia (inversão de risco), escassez, nome pela fórmula M-A-G-I-C, e bibliotecas de headlines, CTAs e objeções. Gatilhos: \"oferta irresistível\", \"Grand Slam Offer\", \"empilhar bônus\", \"garantia\", \"quebrar objeção\". |
| `revenue-orquestracao-de-crm` | Orquestração de RevOps e CRM em nível de estratégia (não execução de ponta de vendas). Cobre estágios do contato, modelo de lead scoring (demográfico, comportamental e decaimento), temperatura do lead, segmentação, rotina de higiene de dados, pontos de integração entre marketing, CRM e vendas, roteamento de leads, automações de CRM e RevOps. Use para definir como os contatos evoluem, são pontuados e segmentados no CRM. |
| `revenue-preco` | Use para definir preço e pacotes de SaaS e produto digital: preço por valor, pesquisa de preço (Van Westendorp, MaxDiff), planos Good-Better-Best, freemium vs teste grátis, validação de disposição a pagar, quando subir preço e preço enterprise. Gatilhos: \"quanto cobrar\", \"planos e preços\", \"página de preços\", \"freemium\", \"aumentar preço\". |
| `revenue-premortem-previsao` | Use to stress-test predictions by assuming they failed and working backward to identify why. Invoke when confidence is high (>80% or <20%), need to identify tail risks and unknown unknowns, or want to widen overconfident intervals. Use when user mentions premortem, backcasting, what could go wrong, stress test, or black swans. |
| `revenue-psicologia` | Use para aplicar psicologia do consumidor e economia comportamental a uma peça, oferta ou página: princípios de persuasão de Cialdini, vieses cognitivos (Kahneman e Thaler), modelo de comportamento de BJ Fogg, psicologia de preço, arquitetura de escolha e construção de confiança. Gatilhos: \"psicologia\", \"viés cognitivo\", \"gatilho mental\", \"prova social\", \"escassez\", \"ancoragem\", \"por que as pessoas compram\". |
| `revenue-sexy-canvas` | Framework mestre de psicologia de consumo e desejos humanos baseado na metodologia Sexy Canvas de André Diamand (7 pecados capitais + 7 elementos da criança interior). Aplica auditoria, adaptação e eletrificação de apelo emocional para produtos, textos de copywriting, criativos visuais e roteiros. Use para: diagnosticar por que uma oferta não engaja ou não converte, amplificar o desejo de compra, enriquecer produtos com dopamina e auditar peças sob a lente dos 14 motores emocionais. |

### seo

| Skill | Use quando |
| --- | --- |
| `seo-app-store` | Especialista em App Store Optimization (ASO) para Apple App Store e Google Play Store. Abrange pesquisa de palavras-chave mobile, otimização de metadados visuais e textuais, Custom Product Pages (CPP), testes A/B de ícones e screenshots, conversão de downloads e gestão de avaliações. Use para: ranquear aplicativos nas buscas mobile, otimizar fichas de lojas, estruturar lançamentos de apps e maximizar taxas de instalação orgânica. |
| `seo-autoridade-e-backlinks` | Use para analisar e conquistar autoridade de domínio e backlinks: avaliar o perfil de links, identificar links tóxicos, medir a autoridade do domínio (rubrica CITE), montar estratégia de link building e escrever e-mails de outreach e digital PR. Gatilhos: \"backlinks\", \"perfil de links\", \"link building\", \"autoridade de domínio\", \"links tóxicos\", \"outreach para links\". |
| `seo-conteudo` | Use when writing search-optimized blog posts, pillar pages, comparison guides, or how-tos; creating SEO briefs; using Google's E-E-A-T guidelines. Do NOT use for keyword research and topic clusters (use seo-palavras-chave) or programmatic SEO at scale (use seo-programatico). |
| `seo-geo` | Use when optimizing content for Generative Engine Optimization (GEO), AI citations, Perplexity, Google AI Overviews, SearchGPT, Claude, or Gemini; making brand content quotable by LLMs; or establishing entity authority in Knowledge Graphs. Do NOT use for creating new content from scratch with research and expert quotes (use conteudo-pesquisa), for keyword-driven SEO articles (use seo-conteudo) or for structured data markup (use seo-schema-markup). |
| `seo-on-page` | Use when auditing on-page SEO factors, title tags, meta descriptions, headings, internal link architectures, content quality, E-E-A-T signals, content freshness and decay, or diagnosing why a page dropped in search rankings. Do NOT use for backlinks, link building or domain authority (use seo-autoridade-e-backlinks). |
| `seo-palavras-chave` | Use para pesquisar palavras-chave e intenção de busca: levantar termos, agrupar por tema e intenção, montar clusters de tópicos, analisar a página de resultados (SERP) de uma palavra e achar lacunas de conteúdo, com ou sem a extensão Keywords Everywhere. Gatilhos: \"pesquisa de palavras-chave\", \"keyword research\", \"intenção de busca\", \"cluster de tópicos\", \"o que o Google mostra para esta busca\", \"volume e dificuldade\". |
| `seo-podcast` | Optimize podcast content for search engines using transcripts, structured show notes, and strategic keyword targeting to drive organic discovery. Use when: Launching a new podcast and planning for discoverability; Adding transcripts to existing episodes for SEO benefit; Optimizing show notes for search traffic; Building topical authority through podcast content; Increasing organic traffic to podcast landing pages |
| `seo-programatico` | Use para criar páginas de SEO em escala a partir de modelos e dados (SEO programático): páginas de comparação, de localidade, de integração, de glossário, diretórios e templates com padrões de título, links internos e schema, sem cair em conteúdo raso. Gatilhos: \"SEO programático\", \"páginas em escala\", \"template de página\", \"centenas de páginas\", \"páginas de cidade ou de categoria\". |
| `seo-relatorio-de-desempenho` | Use para acompanhar e reportar o desempenho de SEO e GEO: relatório executivo, detecção de anomalias, alertas de volatilidade de ranking e KPIs no Google, Bing e buscadores de IA (Perplexity, SearchGPT, Claude, Gemini). Gatilhos: \"relatório de SEO\", \"queda de ranking\", \"tráfego orgânico caiu\", \"KPI de SEO\". |
| `seo-schema-markup` | Use when the user asks to "add schema markup", "generate structured data", "JSON-LD", "rich snippets", "FAQ schema", "add FAQ rich results", "I want star ratings in Google", "product markup", or "recipe schema". Generates structured data markup (Schema.org JSON-LD) to enable rich results in search engines including FAQ snippets, How-To cards, Product listings, Reviews, and more. For meta tag optimization, see meta-tags-optimizer. For broader technical SEO, see seo-tecnico. |
| `seo-tecnico` | Use when performing technical SEO audits, diagnosing crawling or indexing issues, auditing Core Web Vitals (LCP, INP, CLS), configuring robots.txt (including AI crawlers like GPTBot), validating XML sitemaps, fixing HTTP status codes, or diagnosing site speed drops. Do NOT use for backlinks or link building (use seo-autoridade-e-backlinks). |

### sip

| Skill | Use quando |
| --- | --- |
| `sip-geral` | Use when the current task involves general software engineering, architecture, backend, frontend, mobile, database, testing, security, DevOps, AI/ML or development workflows (spec, planning, execution-loop, TDD, debugging) in any project other than "SIP - Geral" (0 Padrões) itself, or when the user asks "existe algo no 0 Padrões pra isso", "tem skill/agent/workflow pra isso no hub geral", "consulta o SIP - Geral", or names a 0 Padrões skill, agent or workflow explicitly in a consumer project. |

### site

| Skill | Use quando |
| --- | --- |
| `site-arquitetura` | Use para planejar ou reestruturar a estrutura de um site: hierarquia de páginas, mapa do site (sitemap visual), padrão de URLs, menu, rodapé, breadcrumbs, navegação no celular e plano de links internos. Traz modelos prontos por tipo de site (SaaS, blog, e-commerce, documentação, híbrido, negócio local). Gatilhos: \"estrutura do site\", \"mapa do site\", \"arquitetura de informação\", \"menu do site\", \"URLs\", \"breadcrumb\", \"links internos\", \"planejar o site\". |
| `site-auditoria-de-interface` | Use ANTES de alterar uma página, seção ou componente que já existe (site, landing page, interface): lê o estado atual, inventaria o que há, checa redundância e só propõe lacunas reais, com prova. Gatilhos: \"melhorar a página\", \"mexer no layout\", \"adicionar uma seção\", \"redesenhar a home\", \"adicionar componente\", quando já existe código ou página publicada. |
| `site-cro` | Use para auditar e otimizar a conversão de uma página que já existe (landing page, home, preços, formulário, popup, cadastro): modelo LIFT, auditoria com nota, casamento anúncio × página, checklist de 15 pontos e ideias de teste. Gatilhos: \"a página não converte\", \"auditoria de CRO\", \"revisar a landing\", \"otimizar formulário\", \"popup de saída\", \"atrito no cadastro\". |
| `site-diretrizes-web-codigo` | Use para revisar CÓDIGO de interface contra as Web Interface Guidelines da Vercel (acessibilidade, UX, boas práticas), com saída terse em arquivo:linha. Busca a lista atual online a cada uso: precisa de acesso à internet. Gatilhos: \"revise minha UI\", \"cheque acessibilidade do código\", \"audite o design do site\". |
| `site-interface-de-conversao` | Use para desenhar a interface de uma página ou site de conversão: hierarquia visual, cor e contraste (60-30-10, WCAG AA), tipografia, espaçamento, componentes, movimento, versão para celular e checklist de acessibilidade. Gatilhos: \"design da landing page\", \"hierarquia visual\", \"paleta e contraste\", \"layout\", \"UI\", \"UX\", \"acessibilidade\". |
| `site-react-composicao` | Use ao refatorar componentes React com excesso de props booleanas, ao montar bibliotecas de componentes flexíveis ou projetar APIs reutilizáveis (componentes compostos, render props, context providers, mudanças do React 19). |
| `site-react-desempenho` | Use ao escrever, revisar ou refatorar CÓDIGO React e Next.js para desempenho (cascatas de requisições, tamanho do bundle, servidor, re-renderizações, hidratação), com 66 regras da Vercel por prioridade. |
| `site-tailwind-design-system` | Use para escrever o CÓDIGO de um design system ou de componentes com Tailwind CSS v4 e React 19: tokens com @theme, variantes com CVA, formulários, grid, animações nativas, modo escuro, migração v3 para v4; inclui trechos de HTML Tailwind para páginas de marketing (references/tailwind-patterns.md). |

### social

| Skill | Use quando |
| --- | --- |
| `social-carrossel` | Use para planejar e redigir carrosséis de Instagram e LinkedIn lâmina a lâmina, com teto de cerca de 25 palavras por lâmina, gancho forte no slide 1, valor no slide 2 e uma ideia com metáfora visual por lâmina, prontos para renderizar em modelos de imagem de IA. Gatilhos: \"carrossel\", \"lâminas\", \"slides do Instagram\". |
| `social-direcao-de-arte-ia` | Use para dirigir a arte de carrosséis 4:5 (1080x1350) gerados por IA: injeção do design system da marca em prompts de ChatGPT/GPT Image, FLUX e Midjourney e fluxo do Slide Âncora (3 variantes do hook e travamento do vencedor como referência). Gatilhos: \"prompt de imagem do carrossel\", \"slide âncora\", \"arte do carrossel com IA\". |
| `social-estrategia` | Omnichannel social media strategy, content planning, platform-native distribution (LinkedIn, X/Twitter, Instagram), algorithmic retention mechanics, social listening, influencer partnerships and Reddit, X and Bluesky playbooks. |
| `social-linkedin` | Use para criar presença e autoridade orgânica no LinkedIn: auditar e reescrever o perfil, escrever posts e carrosséis de alto desempenho, usar fórmulas de post e montar um sistema de conteúdo de liderança de pensamento que gera leads inbound. Gatilhos: \"post de LinkedIn\", \"perfil do LinkedIn\", \"headline\", \"liderança de pensamento\", \"conteúdo para LinkedIn\", \"autoridade no LinkedIn\". |
| `social-youtube-para-notas` | Process YouTube videos into summarized Obsidian notes. Use when given a YouTube URL to summarize, extract insights, or turn videos into notes. Triggers on "summarize this video", "process this YouTube", "what's this video about", or any YouTube URL shared for processing. |

### vendas

| Skill | Use quando |
| --- | --- |
| `vendas-cold-email` | Especialista em prospecção ativa B2B via cold email e cadências outbound. Domina a personalização em 4 níveis (icebreakers contextuais), estrutura de emails curtos de alto impacto, cadências de follow-up multitoque sem passivo-agressividade, CTAs de baixo atrito e infraestrutura de caixas secundárias. |
| `vendas-materiais-de-venda` | Use para criar os materiais que o time comercial usa para fechar negócio (em inglês, sales enablement): deck de vendas, one-pager, pitch personalizado para um prospecto, script de demonstração por tipo de call, mapa de objeções e respostas, case de sucesso, coleta de depoimentos e resposta a RFP/RFI. Gatilhos: \"faça um case\", \"preciso de um depoimento\", \"responda esta RFP\", \"script de demo\", \"objeções de preço\", \"one-pager\", \"pitch para esta empresa\". |
| `vendas-metodologias-b2b` | Use para aplicar metodologias de venda consultiva e negociação B2B complexa: Challenger Sale, SPIN Selling, Sandler System e Never Split the Difference. Gatilhos: \"SPIN\", \"Challenger\", \"Sandler\", \"negociação difícil\", \"venda consultiva\". |
| `vendas-pipeline` | Especialista em orquestração de pipeline comercial B2B, qualificação rigorosa (MEDDIC e BANT), previsão de receita (Forecasting), gestão de risco de negócios, preparação de reuniões de descoberta, passagem de bastão de Vendas para Sucesso do Cliente e comissionamento de vendas (OTE, aceleradores, cota). |
| `vendas-prospeccao-de-leads` | Use para encontrar e preparar prospectos B2B antes do contato: achar decisores por cargo, porte e setor, montar lista de leads, enriquecer contatos (e-mail, telefone, tecnologia usada), conferir e-mails antes do envio e monitorar sinais de compra como rodada de investimento, vagas abertas e troca de tecnologia. Gatilhos: \"ache decisores\", \"lista de prospects\", \"pesquisa de leads\", \"enriquecer contatos\", \"sinais de compra\", \"quem está contratando\", \"Apollo\". |

<!-- skills:end -->

## Modo contribuição (devolver conhecimento ao hub)

**Exceção primeiro — edição direta quando o dono já revisou:** se o próprio usuário dono do hub pediu explicitamente a mudança nesta conversa, edite `.agent/skills/`, `.agent/agents/` ou `.agent/workflows/` do hub direto, sem passar pelo inbox.

Caso contrário, nunca edite essas pastas do hub a partir de um projeto consumidor: elas são lidas por caminho absoluto por todo projeto que consome o hub, e uma edição sem curadoria propagaria na hora. Em vez disso:

1. Leia o formato em `"/Users/macbookpro/Documents/IA Projects/_Plataforma/0 Mkt/inbox/README.md"`.
2. Crie `"/Users/macbookpro/Documents/IA Projects/_Plataforma/0 Mkt/inbox/NNN-<assunto>.md"` (próximo número livre da pasta,
   contando `inbox/arquivo/`) com todas as seções do formato, escrito para quem
   nunca viu a conversa.
3. Avise o usuário que a contribuição ficou pendente de revisão.

## Atualização

- Última atualização do hub: 2026-11-11 (o dono do hub muda esta data sempre
  que esta skill, um agent, um workflow ou a estrutura do hub mudar).
- Para atualizar a instalação num projeto (pegar agents/workflows novos,
  refazer links): cole de novo o prompt
  `"/Users/macbookpro/Documents/IA Projects/_Plataforma/0 Mkt/prompts/instalar-skill-sip-marketing.md"` numa sessão daquele projeto.
- A data em que **cada projeto** instalou ou atualizou fica no
  `.agent/SIPS-CONSUMIDOS.md` dele. Se for anterior à data acima, ofereça
  rodar o prompt.

## Se nada bater

Se a tarefa não é de marketing, ou se o projeto atual é o próprio `SIP - Marketing` (0 Mkt), não force o uso desta skill.
