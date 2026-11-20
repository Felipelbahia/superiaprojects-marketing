# conteudo

Estratégia e produção de conteúdo: briefing, blog, pesquisa, tendências, reaproveitamento, aprovação e pré-publicação.

> Gerado por build_sip_index.py. Não edite à mão. Skill: `"<HUB>/.agent/skills/<nome>/SKILL.md"`; agent: `"<HUB>/.agent/agents/<nome>.md"`; workflow: `"<HUB>/.agent/workflows/<nome>.md"`.

## Skills (7)

| Skill | Use quando |
| --- | --- |
| `conteudo-briefing` | Use para montar briefings de conteúdo completos para redatores, com objetivo, público, ângulo, estrutura e critérios de aprovação, em qualquer formato. Gatilhos: "briefing de conteúdo", "brief para redator", "pauta para freela". |
| `conteudo-estrategia` | Use para planejar o conteúdo de uma marca: estratégia e playbook, pilares editoriais, calendário editorial, formatos, distribuição, geração de ideias a partir do posicionamento, análise de lacunas de conteúdo contra concorrentes e guia de estilo. Gatilhos: "teia de conteúdo", "webfluence", "isca digital", "lead magnet", "estratégia de conteúdo", "calendário editorial", "pilares de conteúdo", "ideias de conteúdo", "onde distribuir", "lacuna de conteúdo", "guia de estilo". |
| `conteudo-linha-de-producao` | Use when: orquestrar a linha de produção unificada de conteúdo de alta retenção e conversão para Reels, TikTok, Shorts e Carrosséis; conecta a marca ativa (_brands/), psicologia comportamental (revenue-sexy-canvas), mineração de dados (hook-mining), engenharia reversa (reel-analyzer e viral-carousel), geração de carrosséis via IA (social-carrossel e social-direcao-de-arte-ia), retenção visual (copy-hooks-video-curto), motores de mídia (Remotion, no projeto de edição de vídeo) e filtro anti-slop. |
| `conteudo-pesquisa` | Research-first content creation optimized for both human readers and AI search engines (Claude, ChatGPT, Perplexity, Gemini). Creates authentic, authoritative content that becomes the go-to citation source for AI models answering user questions. Use this skill when: - Creating content that should appear in AI search results (Perplexity, ChatGPT, Claude) - Building topical authority to become THE source AI cites for a topic - Launching a new product and need compelling, citable content - Creating blog posts, articles, social media, or press releases - Need content that references real trends, people, and recent events - Want AI-assisted content that doesn't sound AI-generated - Creating thought leadership content in any industry Triggers: "create content for", "write about", "research and write", "find experts for", "content for launch", "blog post about", "article on", "press release for", "AI search", "show up in AI", "Perplexity", "be cited by AI" This skill is for CREATING content with research. |
| `conteudo-post-de-blog` | Transform brain dumps into polished blog posts in the brand's own voice. Use when the user wants to write a blog post with scattered ideas, talking points, and conclusions that need organization into a cohesive, conversational narrative. |
| `conteudo-reaproveitamento` | One-to-many content multiplication engine. Transform long-form assets (podcasts, webinars, whitepapers, pillar articles) into high-performing social posts, email newsletters, carousels, and video scripts using semantic content architectures. |
| `conteudo-tendencias` | Use para pesquisar tendências de tópicos em Google Trends, Google Analytics, Reddit, LinkedIn, X, Substack, Medium, blogs, podcasts e YouTube e gerar esboços de artigo a partir da intenção de busca. Gatilhos: "o que está em alta", "tendência de conteúdo", "tema do momento", "esboço baseado em dados". |

## Agents (2)

| Agent | Use quando |
| --- | --- |
| `conteudo-brainstorm` | Campaign ideation and creative concept specialist. Use for brainstorming campaign ideas, evaluating marketing approaches, developing messaging angles, and debating creative decisions before execution. Examples: <example>Context: User wants campaign ideas. user: "We need creative concepts for our product launch" assistant: "Let me use the conteudo-brainstorm agent to explore campaign angles and creative concepts for the launch." <commentary>Campaign ideation requires exploring multiple creative approaches, so delegate to the conteudo-brainstorm.</commentary></example> <example>Context: User is choosing between marketing approaches. user: "Should we focus on content marketing or paid ads?" assistant: "I'll engage the conteudo-brainstorm agent to analyze both approaches and recommend the best strategy." <commentary>Strategic decisions require evaluating trade-offs and considering multiple factors.</commentary></example> |
| `conteudo-criacao-multiformato` | Content creation specialist for all marketing content types. |

## Workflows (13)

| Workflow | Use quando |
| --- | --- |
| `/conteudo-aprovacao` | Gera o fluxo de aprovação de uma peça de conteúdo (etapas, responsáveis, SLA, parecer em 5 campos e releitura integral na v2). Use quando uma peça precisar passar por revisão antes de publicar. |
| `/conteudo-briefing` | Generate comprehensive content briefs for writers, ensuring clarity, |
| `/conteudo-briefing-de-seo` | Content brief template and creation methodology for SEO-optimized content. Use when preparing briefs for writers or planning new content pieces. |
| `/conteudo-escrita-colaborativa` | Assists in writing high-quality content by conducting research, adding citations, improving hooks, iterating on outlines, and providing real-time feedback on each section. Transforms your writing process from solo effort to collaborative partnership. |
| `/conteudo-estrategia` | Teia de conteúdo que prepara a venda (conteúdo, VSL, oferta): diagnostica por que há tráfego e não há venda, e onde falta conexão entre os conteúdos. Não é sobre site nem design de página. Use para: oferta enviada direto para tráfego frio, abertura alta sem cliques, VSL assistido sem compra. |
| `/conteudo-kit-de-podcast` | Transform podcast transcripts into comprehensive content marketing suites including blog posts, social media content, newsletters, SEO-optimized articles, and timestamps. Use when user provides podcast transcripts or wants to repurpose podcast content. |
| `/conteudo-pesquisa` | (sem description) |
| `/conteudo-post-de-blog` | Transform brain dumps into polished blog posts in Nick Nisi's voice. |
| `/conteudo-pre-publicacao` | Pre-publish assistant for new blog posts. Use when the user wants to classify a new post with categories and tags, generate SEO metadata (title, description, focus keyphrase), or get intelligent suggestions with rationale. Works with draft content (file path, URL, or text) and suggests from existing taxonomy to maintain balanced distribution. |
| `/conteudo-reaproveitamento` | One-to-many content multiplication engine. Transform long-form assets |
| `/conteudo-sinais-fracos` | Identify EMERGING trends by connecting dots across unrelated sources. Monitor niche communities, academic research, GitHub, patents, funding, regulatory changes. Predict what will trend in 3-6 months based on weak signals. |
| `/conteudo-temas-e-plugins` | Create comprehensive marketing content for themes, plugins, and web products. Generates organized folder structure with product descriptions, feature highlights, social media posts, email campaigns, video scripts, sales materials, and brand assets. Use when creating promotional content, announcements, or sales copy. |
| `/conteudo-tendencias` | Advanced content and topic research skill that analyzes trends across |

