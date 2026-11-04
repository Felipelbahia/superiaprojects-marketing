---
# Repository: https://github.com/Felipelbahia/superiaprojects-marketing
# Status: Nativa do Projeto
name: social-direcao-de-arte-ia
description: "Direção de arte e injeção automática de Design System em prompts de modelos de imagem de IA (ChatGPT/GPT Image 2, FLUX, Midjourney) para carrosséis em proporção 4:5 (1080x1350). Implementa o Workflow do Slide Âncora (geração de 3 variantes do hook e do primeiro slide de valor; travamento do vencedor como imagem de referência anexada para clonar layout, paleta e consistência estética nas lâminas seguintes), checklist de qualidade de 7 pontos e conexão dinâmica com as marcas de _brands/."
author: Felipe Bahia (Futuro Mercado)
license: MIT
metadata:
  author: Felipe Bahia (Futuro Mercado)
  version: 1.0.0
---
# Design Taste — Direção de Arte e Injeção de Design System para Carrosséis via IA

> **Princípio Central:** Modelos de imagem de IA não possuem bom gosto espontâneo. Sem direcionamento explícito, eles misturam tipografias incompatíveis, cores saturadas sem critério e layouts sufocados. O `social-direcao-de-arte-ia` atua como Diretor de Arte: injeta as regras visuais da marca ativa e o Workflow do Slide Âncora diretamente na estrutura de cada prompt.

---

## 🧭 Visão Geral & Modos de Operação

O `social-direcao-de-arte-ia` recebe a estrutura textual gerada por `social-carrossel` e a transforma em prompts de alta fidelidade para modelos generativos de imagem (ChatGPT / GPT Image 2, FLUX, Midjourney).

A skill opera em três modos:

1. **Modo Geração de Prompts (Prompt Mode):** Recebe o plano lâmina a lâmina de `social-carrossel`. Injeta os tokens visuais da marca ativa e gera os prompts em inglês no esqueleto padronizado, estruturando as variantes divergentes de Hook, Slide Âncora e CTA.
2. **Modo Iteração Visual (Iterate Mode):** Você apresenta uma lâmina gerada e o resultado indesejado. A skill diagnostica o problema contra o Checklist de 7 Pontos e reescreve o prompt com cirurgia precisa (eliminação de ruído, respiro de margens, redução de palavras ou aumento da escala tipográfica).
3. **Modo Auditoria Visual (Audit Mode):** Você apresenta as imagens finais renderizadas. A skill audita cada uma das lâminas, reportando conformidade com a âncora, hierarquia de miniatura e integridade tipográfica.

---

## 🎨 Conexão Dinâmica com o Design System da Marca (`_brands/`)

Elimine completamente defaults visuais genéricos. Os parâmetros de design são lidos e injetados diretamente a partir dos arquivos da marca ativa em `_brands/<marca>/`:

- **`style-guide.md`:** Paleta oficial, cor de fundo (light/dark), tipografia de título/corpo e cor de destaque (*accent color*).
- **`brand-voice.md`:** Estética dominante da marca (minimalismo corporativo, dashboard técnico de dados, elegância editorial, etc.).

### Tabela de Tokens Dinâmicos Injetados no Prompt:

| Token de Design | Diretriz Técnica Padrão 0 Mkt | Adaptação Dinâmica por Marca |
|---|---|---|
| **Proporção & Formato** | `4:5 portrait social slide, 1080x1350` | Fixo para Instagram/LinkedIn. Garante ocupação máxima de tela no feed mobile sem cortes indesejados. |
| **Grid & Margens** | Margens generosas (~8% a 10% em todos os lados). Respiro obrigatório. Nenhum elemento encosta na borda. | Respeitado em 100% dos prompts. Espaço em branco é funcionalidade, não desperdício. |
| **Hierarquia Visual** | O TÍTULO é o elemento dominante (3x a 5x maior que o corpo). Legível na miniatura do feed. | Tamanho tipográfico dominante para o título; corpo e diagramas secundários. |
| **Tipografia** | Sem fontes decorativas ou manuscritas. Caixa alta bold no título; sans limpa no corpo. | Definida pelo `style-guide.md` da marca (ex: Inter / SF Pro para tech; Helvetica Neue Condensed para dados). |
| **Paleta de Cores** | Fundo neutro limpo (dark mode profundo ou off-white/paper) + texto em alto contraste. | Extraída do `style-guide.md` da marca ativa. |
| **Cor de Acento (Accent)** | **EXATAMENTE UMA COR DE DESTAQUE**, usada no máximo em 3 lugares (setas, tags, underlines). | Vem do `style-guide.md` da marca (ex.: a cor de destaque definida em `_brands/pr-pulse/style-guide.md`). |
| **Slide Furniture (Mobiliário)** | Identificador de etapa no topo esquerdo (`STEP 01` / `PASSO 01`) e indicador de swipe no topo direito. | Mantido com precisão milimétrica em todas as lâminas para criar sensação de série visual coesa. |

---

## ⚓ O Workflow do Slide Âncora (Visual Anchor Workflow)

O maior erro ao criar carrosséis com IA é enviar prompts isolados para cada slide. O resultado parece uma colagem de posts de autores diferentes. 

O `social-direcao-de-arte-ia` resolve isso em 5 passos metódicos:

```
[ PASSO 1: HOOK ] ──> Gera 3 variantes divergentes de layout ──> Usuário escolhe a vencedora
         │
[ PASSO 2: SLIDE 2 ] ──> Gera 3 variantes divergentes de valor ──> Usuário escolhe a vencedora
         │
         ▼
[ PASSO 3: TRAVAR ÂNCORA ] ──> Slide 2 aprovado vira a ÂNCORA VISUAL (Imagem de Referência)
         │
         ▼
[ PASSO 4: SLIDES SEGUINTES ] ──> Anexa a Âncora como referência + instrução [CONSISTENCY]
         │
[ PASSO 5: CTA FINAL ] ──> Gera 3 variantes divergentes com tratamento de Hook
```

### Regra 1: O Hook recebe 3 Variantes Estruturalmente Divergentes
Para o Slide 1, produza sempre 3 prompts explorando direções visuais e metáforas completamente diferentes (não apenas trocar uma cor de fundo, mas alterar a disposição do título, o tipo de gráfico, o elemento de quebra de padrão). O usuário gera as 3 opções e seleciona a que parar o seu próprio scroll.

### Regra 2: Travar o Slide Âncora no Slide 2
Gere 3 variantes divergentes de layout para o **primeiro slide de valor** (Slide 2). Assim que o usuário aprovar uma imagem, essa imagem é **travada como a Âncora Visual**. Todas as lâminas de valor seguintes utilizarão essa imagem como referência anexada no gerador (GPT Image 2, Midjourney com `--sref`, ou FLUX I2I), com a instrução estrita de clonar o layout, a paleta e o espaçamento, alterando apenas os textos e o diagrama interno.

### Regra 3: CTA com Tratamento de Hook
A lâmina final de conversão recebe o mesmo tratamento do Slide 1: 3 variantes divergentes. Ela mantém a paleta e tipografia da âncora, mas pode romper a composição interna para destacar a caixa de ação e a palavra-chave para envio na DM.

### Regra 4: Instruções de Fidelidade Tipográfica Estrita
Modelos de imagem erram textos longos. Todo prompt deve:
1. Colocar todos os textos entre aspas duplas exatas.
2. Declarar explicitamente: `[TEXT — render exactly, no other words]`.
3. Manter o total de palavras do slide em ≤ 25 palavras.
4. Se o gerador errar uma letra, a correção é **diminuir a quantidade de palavras ou aumentar o tamanho da fonte no prompt**, nunca ficar gerando repetidamente sem mudar o texto.

---

## 🧱 Esqueleto Universal de Prompts (Prompt Template)

> **Nota Crítica de Língua:** O esqueleto e as instruções técnicas do prompt devem ser mantidos em **Inglês**, pois modelos como FLUX, GPT Image 2 e Midjourney possuem taxa de acerto tipográfico e semântico substancialmente superior em língua inglesa. Os textos entre aspas (Title, Body, Labels) são redigidos no idioma final do post (Português PT-BR).

```
[FORMAT] 4:5 portrait social slide, 1080x1350.
[STYLE] {Background: neutral clean/dark UI; Typography: bold condensed sans-serif header, clean geometric sans body; Palette: brand primary background, high-contrast text, single brand accent color used sparingly}.
[LAYOUT] {Generous 8% margins; title sits dominantly at top third; center area features a crisp minimal diagram; bottom area holds clean secondary body lines; top-left features subtle "{STEP 0X}" badge}.
[TEXT — render exactly, no other words]
Title: "{TITULO EM CAIXA ALTA}"
Body: "{Linha 1 do corpo} / {Linha 2 do corpo}"
Labels: "{PASSO 01 ou STEP 01}"
[VISUAL] {Concrete description of the visual diagram: comparison cards, workflow arrows, annotated UI frame, checklist boxes, or save-bait matrix}.
[CONSISTENCY] {Para lâminas ancoradas: "match the attached reference image's layout, typography, color palette, and spacing exactly; replace only the text strings and diagram content."}
[NEGATIVE] no extra text, no misspelled words, no watermarks, no gradients, no 3d glossy render, no stock photo look, no multiple accent colors.
```

---

## 🔍 Checklist de Qualidade Visual (7 Pontos)

Execute este checklist em cada lâmina gerada antes de aprovar a publicação:

1. **Legibilidade de Miniatura:** O título é perfeitamente legível na miniatura do feed do Instagram/LinkedIn?
2. **Fidelidade Tipográfica:** Todas as palavras estão grafadas exatamente como especificadas, sem letras comidas ou duplicadas?
3. **Respiro e Margens:** A margem de ~8% a 10% foi respeitada em todas as bordas? Nenhum elemento gráfico ou texto está colado nas extremidades?
4. **Ponto Focal Único:** A hierarquia visual é absorvida pelo cérebro em menos de 1 segundo?
5. **Disciplina de Cor:** A cor de destaque (*accent color*) foi utilizada em no máximo 3 lugares no slide?
6. **Família da Âncora:** A lâmina pertence visivelmente à mesma família estética e tipográfica do Slide Âncora anexado?
7. **Autonomia da Metáfora:** A metáfora visual faria sentido e entregaria valor prático mesmo se printada isoladamente sem a legenda?

---

## 🛠️ Guia de Integração com Ferramentas

Para detalhes operacionais sobre como plugar este workflow no ChatGPT (GPT Image 2), Midjourney (`--sref`/`--cref`) ou APIs do FLUX, consulte o guia completo em:
[carousel-pipeline-guide.md](references/carousel-pipeline-guide.md).
