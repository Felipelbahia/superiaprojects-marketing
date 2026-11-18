# social

Redes sociais: estratégia, carrossel, LinkedIn, Instagram, YouTube, thumbnails e análise de desempenho.

> Gerado por build_sip_index.py. Não edite à mão. Skill: `"<HUB>/.agent/skills/<nome>/SKILL.md"`; agent: `"<HUB>/.agent/agents/<nome>.md"`; workflow: `"<HUB>/.agent/workflows/<nome>.md"`.

## Skills (5)

| Skill | Use quando |
| --- | --- |
| `social-carrossel` | Use para planejar e redigir carrosséis de Instagram e LinkedIn lâmina a lâmina, com teto de cerca de 25 palavras por lâmina, gancho forte no slide 1, valor no slide 2 e uma ideia com metáfora visual por lâmina, prontos para renderizar em modelos de imagem de IA. Gatilhos: "carrossel", "lâminas", "slides do Instagram". |
| `social-direcao-de-arte-ia` | Use para dirigir a arte de carrosséis 4:5 (1080x1350) gerados por IA: injeção do design system da marca em prompts de ChatGPT/GPT Image, FLUX e Midjourney e fluxo do Slide Âncora (3 variantes do hook e travamento do vencedor como referência). Gatilhos: "prompt de imagem do carrossel", "slide âncora", "arte do carrossel com IA". |
| `social-estrategia` | Omnichannel social media strategy, content planning, platform-native distribution (LinkedIn, X/Twitter, Instagram), algorithmic retention mechanics, social listening, influencer partnerships and Reddit, X and Bluesky playbooks. |
| `social-linkedin` | Use para criar presença e autoridade orgânica no LinkedIn: auditar e reescrever o perfil, escrever posts e carrosséis de alto desempenho, usar fórmulas de post e montar um sistema de conteúdo de liderança de pensamento que gera leads inbound. Gatilhos: "post de LinkedIn", "perfil do LinkedIn", "headline", "liderança de pensamento", "conteúdo para LinkedIn", "autoridade no LinkedIn". |
| `social-youtube-para-notas` | Process YouTube videos into summarized Obsidian notes. Use when given a YouTube URL to summarize, extract insights, or turn videos into notes. Triggers on "summarize this video", "process this YouTube", "what's this video about", or any YouTube URL shared for processing. |

## Agents (1)

| Agent | Use quando |
| --- | --- |
| `social-calendario-e-distribuicao` | Estrategista sênior de redes sociais, distribuição orgânica e comunidades. Use quando precisar planejar calendários editoriais, criar carrosséis de alta retenção no Instagram e LinkedIn, estruturar estratégias de crescimento em canais sociais e engajar audiências com conteúdo nativo.\n\n<example>\nContext: O usuário precisa de uma sequência de carrosséis para o LinkedIn para gerar autoridade B2B.\nuser: "Preciso de um carrossel educativo para o LinkedIn da <marca> sobre monitoramento de marca."\nassistant: "Vou acionar o social-calendario-e-distribuicao para estruturar o carrossel lâmina a lâmina, definindo hook de capa, payoff e save-bait com foco em retenção."\n<commentary>\nDemanda de estratégia de redes sociais e carrossel de autoridade.\n</commentary>\n</example>\n\n<example>\nContext: O usuário quer um calendário editorial mensal omnichannel.\nuser: "Pode planejar a grade de conteúdo do Instagram e LinkedIn da <marca> para o próximo mês?"\nassistant: "Acionando o social-calendario-e-distribuicao para desenhar o calendário editorial omnichannel alinhado aos pilares de conteúdo da marca."\n<commentary>\nPlanejamento de distribuição e linhas editoriais em mídias sociais.\n</commentary>\n</example> |

## Workflows (11)

| Workflow | Use quando |
| --- | --- |
| `/social-analise-de-desempenho` | Analyzes social media campaign performance across platforms with engagement metrics, ROI calculations, and audience insights for data-driven marketing decisions |
| `/social-checklist-diario` | Gera o checklist diário de gestão de redes sociais (comunidade, publicação, engajamento e métricas). Use para organizar a rotina diária de social media por bloco de tempo. |
| `/social-conceito-de-thumbnail` | Generate thumbnail concepts and ideas for YouTube, TikTok, and other video platforms. Creates detailed visual briefs with composition, text, colors, and emotion suggestions. Use when planning thumbnails, improving CTR, or briefing designers. |
| `/social-conversao-para-formato-curto` | Convert long-form videos into short-form content for TikTok, YouTube Shorts, and Instagram Reels. Identifies viral moments, creates hooks, and adapts scripts for vertical format. Use when repurposing videos, creating Shorts from long videos, or planning multi-platform content. |
| `/social-instagram-api` | Instagram Graph API integration via curl. Use this skill to fetch and publish Instagram media. |
| `/social-leitura-de-post-twitter` | Fetch Twitter/X post content by URL using jina.ai API to bypass JavaScript restrictions. Use when Claude needs to retrieve tweet content including author, timestamp, post text, images, and thread replies. Supports individual posts or batch fetching from x.com or twitter.com URLs. |
| `/social-otimizacao-de-post-linkedin` | Professional narrative style with line breaks, hashtag strategy, and hooks in first 2 lines to avoid truncation |
| `/social-otimizacao-de-titulo-de-video` | Optimize video titles for maximum click-through rate (CTR) and YouTube/TikTok SEO. Generates multiple title variations balancing curiosity, keywords, and platform best practices. Use when naming videos, improving CTR, or A/B testing titles. |
| `/social-seo-de-youtube` | Optimize YouTube videos for search and discovery. Generates SEO-optimized titles, descriptions, tags, hashtags, and chapters. Includes keyword research and competitor analysis. Use when publishing videos, improving discoverability, or optimizing existing content. |
| `/social-transcricao-de-youtube` | Download YouTube video transcripts when user provides a YouTube URL or asks to download/get/fetch a transcript from YouTube. Also use when user wants to transcribe or get captions/subtitles from a YouTube video. |
| `/social-youtube-para-notas` | Process YouTube videos into summarized Obsidian notes. Use when given |

