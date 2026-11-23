# brand

Marca: essência, voz, naming, identidade visual e sonora, paleta, design system e direção criativa.

> Gerado por build_sip_index.py. Não edite à mão. Skill: `"<HUB>/.agents/skills/<nome>/SKILL.md"`; agent: `"<HUB>/.agents/agents/<nome>.md"`; workflow: `"<HUB>/.agents/workflows/<nome>.md"`.

## Skills (9)

| Skill | Use quando |
| --- | --- |
| `brand-audience` | Use para definir ou refazer personas, segmentos, jobs to be done, objeções e hábitos de mídia de uma marca (etapa 3 do brand-builder). Gatilhos: "persona da marca", "público da marca", "personas finas". |
| `brand-builder` | Use para construir ou aprofundar as fundações de uma marca de _brands/, uma etapa por vez e com aprovação: essência, posicionamento, público, voz, desejo, direção visual, design system, ativação e brandbook. Gatilhos: "brandbook", "marca nova", "arquivos de marca finos", "posicionamento da marca". |
| `brand-design-system` | Use para montar o design system da marca como site de referência mais DESIGN.md (paleta com modo escuro, tipografia, espaço, forma, movimento, componentes e tokens), a partir da direção visual aprovada (etapa 7 do brand-builder). Gatilhos: "design system da marca", "DESIGN.md", "tokens da marca". |
| `brand-essence` | Use para definir ou aprofundar essência, crenças, história de origem, inimigo, posicionamento, categoria e arquétipo de uma marca (etapas 1 e 2 do brand-builder). Gatilhos: "propósito", "posicionamento da marca", "Primal Branding", "arquétipo". |
| `brand-identidade-sonora` | Use para definir a identidade sonora de uma marca: logo sonoro (1 a 3 segundos), estética de voz, moodboard de áudio e diretrizes de trilha, efeitos e silêncio para vídeo, podcast, aplicativo e eventos (etapa 8, uso audiovisual, do brand-builder). Gatilhos: "logo sonoro", "identidade sonora", "trilha da marca", "sonic branding". |
| `brand-naming` | Use para criar e validar nomes de marca, produto e empresa pelo protocolo dos 6 portões (briefing, geração, fonético, jurídico, AEO e narrativa). Gatilhos: "nome da marca", "naming", "rebranding de nome", "nome para a empresa". |
| `brand-visual-direction` | Use para decidir direção visual, mood, estilo de imagem, intenção de cor e tipografia e visual de vídeo antes do design system (etapa 6 do brand-builder). Gatilhos: "direção visual", "moodboard", "como a marca deve parecer", "tendências visuais". |
| `brand-visual-style` | Use para criar, extrair e aplicar um sistema visual portátil em um arquivo visual-style.md (cores, tipografia, layout, movimento e humor em um só arquivo que qualquer IA lê): criar do zero, extrair de um site, vídeo ou PDF de marca, aplicar em vídeo (HeyGen), slides HTML, Figma ou paper.design, ou consultar a galeria de estilos prontos (Suíço, Saul Bass, Game Boy etc.). Gatilhos: "visual style", "estilo visual", "brand style", "style guide". |
| `brand-voice-messaging` | Use para definir ou refazer tom de voz, vocabulário, "o que NÃO comunicar", mensagens e pilares de conteúdo de uma marca (etapa 4 do brand-builder), ou extrair a voz de textos existentes. Gatilhos: "tom de voz", "brand voice", "pilares de conteúdo", "o que não comunicar". |

## Agents (2)

| Agent | Use quando |
| --- | --- |
| `brand-direcao-de-arte` | Diretor de Arte Sênior e Especialista em Branding com padrão de agência internacional (estilo Apple, Nike, Stripe, Airbnb, Notion). Especialista em neurodesign, hierarquia visual, psicologia das cores, tipografia contemporânea e direção estética para redes sociais, apresentações, landing pages e identidades de marca. Use quando precisar definir conceitos visuais de alto impacto, conceber direção de arte multiformato, gerar prompts de imagem multi-engine (Midjourney, Flux, ChatGPT, SD) ou conduzir auditoria e autocrítica estética intransigente. <example> Context: O usuário precisa de uma direção de arte impactante para a campanha de lançamento de um novo recurso. user: "Preciso criar a direção visual para o lançamento da nova funcionalidade da PR Pulse no Instagram e landing page." assistant: "Vou acionar o brand-direcao-de-arte para conceber o conceito criativo, estruturar 3 caminhos visuais divergentes, definir paleta funcional e tipografia moderna, orquestrando as skills de carrossel e landing page." <commentary> Demanda de concepção estética, direção de arte e consistência visual multiformato. </commentary> </example> <example> Context: O usuário quer prompts de imagem refinados para gerar assets visuais no Midjourney e Flux sem visual clichê de IA. user: "Gere os prompts de imagem para o novo produto da <marca> com estética minimalista e profissional." assistant: "Acionando o brand-direcao-de-arte para aplicar o filtro anti-slop visual, construir a atmosfera e gerar os prompts calibrados para Midjourney, Flux e ChatGPT Image com contraste e respiro profissional." <commentary> Demanda de engenharia estética de prompts de IA generativa com rigor de diretor de arte. </commentary> </example> |
| `brand-guardiao-de-voz` | Brand consistency and voice validation specialist. Use for ensuring all marketing content matches brand voice, tone, and style guidelines. Reviews content for messaging consistency, language quality, and emotional impact. Examples: <example>Context: User created email campaign copy. user: "Review this email campaign for brand voice consistency" assistant: "I'll use the brand-guardiao-de-voz agent to validate tone, messaging, and brand alignment." <commentary>Brand voice validation requires expert review against guidelines.</commentary></example> <example>Context: User needs landing page copy reviewed. user: "Check if this landing page sounds like our brand" assistant: "Let me deploy the brand-guardiao-de-voz agent to analyze voice, tone, and messaging consistency." <commentary>Brand consistency review ensures all content aligns with established guidelines.</commentary></example> |

## Workflows (2)

| Workflow | Use quando |
| --- | --- |
| `/brand-paleta-de-cores` | Extract color palettes from images, websites, or designs. Identifies dominant colors, generates complementary schemes, and exports in multiple formats (HEX, RGB, HSL, Tailwind, CSS variables). Use when users need color schemes from images, brand colors, or design system palettes. |
| `/design-direcao-criativa` | Workflow de direção de arte e criação visual em 6 etapas: entendimento, conceito, direção de arte com 3 vias divergentes, paleta funcional, tipografia e layout, com prompts de IA multi-engine e autocrítica (0 a 10). Use para criar conceitos visuais, direções de campanha, identidades ou peças de alto padrão estético. |

