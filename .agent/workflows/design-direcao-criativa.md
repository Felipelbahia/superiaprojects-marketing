---
name: design-direcao-criativa
description: "Workflow de direção de arte e criação visual em 6 etapas: entendimento, conceito, direção de arte com 3 vias divergentes, paleta funcional, tipografia e layout, com prompts de IA multi-engine e autocrítica (0 a 10). Use para criar conceitos visuais, direções de campanha, identidades ou peças de alto padrão estético."
---

# Workflow: Direção de Arte & Concepção Criativa

Este workflow conduz a criação de qualquer peça visual pelo método de direção de arte de grandes agências internacionais. Ele garante que nenhuma peça nasça sem intenção conceitual, rigor tipográfico, contraste e autocrítica.

---

## 🧭 Quando Utilizar
- Criação de conceito visual para campanhas de marketing ou lançamentos.
- Direção de arte para carrosséis, key visuals, anúncios ou miniaturas.
- Estruturação de identidade visual ou renovação estética de marca.
- Definição visual para slides de apresentação de alta relevância ou pitch decks.
- Concepção de dobra superior (*above the fold*) e linguagem visual para landing pages.
- Geração de prompts de alta fidelidade para múltiplos motores de imagem de IA (Midjourney, Flux, ChatGPT Image, SD).

---

## 📋 Pré-requisitos & Contexto Inicial
1. **Identificar a Marca Ativa:** Ler obrigatoriamente `_brands/<marca>/style-guide.md` e `_brands/<marca>/brand-voice.md`.
2. **Definir o Formato de Saída:** Rede Social (Instagram/LinkedIn), Apresentação (Slides), Landing Page ou Identidade Geral.

---

## ⚡ As 6 Etapas Obrigatórias

### Etapa 1: Entendimento & Diagnóstico
Responda de forma sintética às 5 perguntas de ouro do Diretor de Arte:
- **Qual é o objetivo principal da peça?** (Ex: reter atenção, educar sobre problema complexo, converter lead).
- **Quem verá isso?** (Persona, contexto mental e plataforma de consumo).
- **Qual emoção deve ser despertada no primeiro segundo?** (Ex: clareza imediata, curiosidade provocativa, solidez executiva).
- **Qual ação clara o usuário deve tomar?** (Salvar post, agendar demo, continuar lendo).
- **Como destacar visualmente essa informação?** (Qual é o elemento dominante único que ancora o olhar).

---

### Etapa 2: Conceito Criativo Central
Crie uma ideia motriz forte que sustente todo o universo visual da peça.
- Não comece por softwares ou ferramentas; defina a **metáfora visual** ou a **linha mestra conceitual** (ex: *"A radiografia do atrito invisível"*, *"O cockpit de dados sem ruído"*, *"O contraste entre o analógico lento e a precisão do código"*).

---

### Etapa 3: Direção de Arte & 3 Vias Criativas Divergentes
Nunca aceite a primeira solução óbvia. Apresente **3 caminhos visuais divergentes** antes de selecionar o melhor:

| Rota Criativa | Atmosfera & Sensação | Referências Estéticas | Tratamento Gráfico |
|---|---|---|---|
| **Rota A: Editorial & Sofisticada** | Elegância, clareza serena, alta autoridade. | Apple, Kinfolk, Notion, revistas de design suíço. | Margens amplas, tipografia geométrica pura, contrastes sutis, respiro extremo. |
| **Rota B: Técnica & Data-Driven** | Precisão milimétrica, controle, inteligência. | Stripe, Linear, dashboards Bloomberg, mapas analíticos. | Grids densos bem modulados, cartões de interface, tags monospaçadas, badges de status. |
| **Rota C: Bold & Dinâmica** | Impacto direto, choque de padrão, urgência inteligente. | Nike, capas de publicações modernas, pôsteres tipográficos. | Títulos em caixa alta dominante, alto contraste (preto/branco + 1 acento saturado), recortes marcantes. |

*Após apresentar as 3 rotas, defina a rota recomendada justificando o porquê com base no objetivo da Etapa 1.*

---

### Etapa 4: Paleta de Cores Funcional
Evite cores genéricas ou aleatórias. Toda cor deve ter uma função prática declarada:

| Papel no Design | Nome / Descrição | HEX | RGB | Função Prática |
|---|---|---|---|---|
| **Fundo Primário** | Neutro dominante | `#FFFFFF` ou `#0D1117` | `(255,255,255)` / `(13,17,23)` | Garante a base limpa e o respiro da peça. |
| **Superfície / Card** | Fundo de apoio | `#F8F9FA` ou `#161B22` | `(248,249,250)` / `(22,27,34)` | Separa blocos de informação com sutileza. |
| **Texto Primário** | Alto contraste | `#111827` ou `#F0F6FC` | `(17,24,39)` / `(240,246,252)` | Garante legibilidade imediata (contraste > 7:1). |
| **Texto Secundário** | Informação de apoio | `#6B7280` ou `#8B949E` | `(107,114,128)` / `(139,148,158)` | Rótulos, metadados e legendas. |
| **Acento Único (Accent)** | Destaque cirúrgico | *Extraído da marca* | *Extraído da marca* | **Usado em no máximo 3 lugares** (CTA, seta ou palavra-chave). |

---

### Etapa 5: Tipografia Moderna & Hierarquia
Defina as famílias tipográficas priorizando fontes contemporâneas e legíveis:
- **Títulos:** Famílias sans limpas e estruturadas (*Inter, Satoshi, Manrope, Plus Jakarta Sans, Outfit, General Sans*).
- **Subtítulos:** Peso médio da mesma família para manter consistência sem introduzir poluição.
- **Corpo de Texto:** Sans geométrica ou humanista de alta legibilidade em telas pequenas (*Inter, DM Sans, Poppins*).
- **Elementos de Código / Dados:** Família monospaçada moderna (*JetBrains Mono, Space Grotesk, Roboto Mono*).

---

### Etapa 6: Layout & Detalhamento por Formato

Conecte a direção conceitual às especificidades do canal escolhido:

#### Se for Post / Carrossel para Instagram/LinkedIn:
- Proporção estrita **4:5 (1080x1350)** para máxima ocupação de tela no feed mobile.
- Estrutura lâmina a lâmina: Hook (Capa) → Problema → Slide Âncora (Slide 2 de valor) → Desdobramentos → CTA de fechamento.
- Aplique as regras da skill [`social-direcao-de-arte-ia`](file:///Users/macbookpro/Documents/IA%20Projects/_Plataforma/0%20Mkt/.agent/skills/social-direcao-de-arte-ia/SKILL.md) (Slide Âncora e margens de 8% a 10%).

#### Se for Apresentação / Slides:
- Proporção **16:9 widescreen**.
- Regra de "1 ideia por slide", composição assimétrica com ponto focal claro e narrativa visual progressiva.
- Delegue o código para [`audiovisual-slidev`](file:///Users/macbookpro/Documents/IA%20Projects/_Plataforma/0%20Mkt/.agent/skills/audiovisual-slidev/SKILL.md).

#### Se for Identidade Visual de Marca:
- Conceito central, arquétipo, universo visual, diretrizes de aplicação em claro e escuro.
- Gere obrigatoriamente a amostra em HTML conforme a skill [`brand-visual-direction`](file:///Users/macbookpro/Documents/IA%20Projects/_Plataforma/0%20Mkt/.agent/skills/brand-visual-direction/SKILL.md).

#### Se for Landing Page / Web:
- Hierarquia da dobra superior (*above the fold*): Headline de valor, sub-headline, prova social e CTA primário de alto contraste.
- Conecte com a skill [`site-interface-de-conversao`](file:///Users/macbookpro/Documents/IA%20Projects/_Plataforma/0%20Mkt/.agent/skills/site-interface-de-conversao/SKILL.md).

---

## 🖼️ Entrega Obrigatória: Prompts Multi-Engine de IA

Para cada peça que demande imagens generativas, entregue os prompts calibrados para os 4 principais motores do mercado:

### 1. Midjourney (v6.1)
```text
/imagine prompt: [Descrição da cena, atmosfera e iluminação em inglês], [paleta de cores exata], [estilo: minimal editorial photography or clean UI graphic], shot on Hasselblad, studio softbox lighting, natural textures, premium design aesthetic, no text, clean composition --ar 4:5 --v 6.1 --style raw
```

### 2. FLUX (Schnell / Dev / Pro)
```text
[Prompt descritivo direto, focado na composição espacial, paleta de cores neutra com acento específico, materiais fotorrealistas ou vetoriais puros, sem elementos clichês de 3D artificial, iluminação difusa direcional, alta fidelidade de detalhes, proporção 4:5 ou 16:9]
```

### 3. ChatGPT Image (DALL-E 3 / GPT Image 2)
```text
A professional high-end graphic design composition featuring [descrição exata]. Minimalist and elegant international agency style, generous negative space, high contrast, clean modern typography reading "[TEXTO EXATO ENTRE ASPAS]". Background is [fundo neutro], with subtle architectural shadows. No clutter, no 3D cartoon slop.
```

### 4. Stable Diffusion (SDXL / Flux Forge)
```text
Prompt: Masterpiece, professional art direction, [descrição do conceito visual], clean studio lighting, sharp focus, 8k resolution, minimalist editorial aesthetic, refined color grading, balanced negative space.
Negative Prompt: oversaturated, ugly, cartoon, 3d render, blurry, distorted, low quality, amateur, watermark, signature, duplicate elements.
```

---

## 🔍 Protocolo de Autocrítica & Laço de Qualidade (0 a 10)

Ao finalizar a proposta visual, o assistente deve obrigatoriamente preencher a tabela de autocrítica:

```markdown
### 📝 Autocrítica do Diretor de Arte
- **Pontos Fortes:** [O que torna este design potente, memorável e funcional]
- **Pontos Fracos:** [Onde o layout pode sofrer risco de interpretação ou perda de foco]
- **Como Poderia Melhorar:** [Qual refinamento extra elevaria ainda mais o nível]
- **Nota Atual (0 a 10):** [Nota atribuída com honestidade técnica]
```

> **Regra de Refinamento Obrigatório:** Se a nota atribuída for **inferior a 10**, o assistente DEVE aplicar imediatamente os ajustes corretivos descritos em "Como Poderia Melhorar" e reescrever a seção até atingir o padrão digno de prêmios internacionais (Awwwards, Behance, Pentawards).
