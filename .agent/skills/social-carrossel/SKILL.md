---
name: social-carrossel
description: "Planeja e redige copy lâmina a lâmina para carrosséis de Instagram e LinkedIn otimizados para renderização em modelos de imagem de IA. Aplica teto rígido de ~25 palavras de corpo por lâmina, gancho agressivo no slide 1, entrega de valor imediata no slide 2 (sem enrolação), 1 ideia por lâmina com metáfora visual tangível, slide de salvamento (Save-Bait) com checklist/matriz, frase screenshotable e modo de auditoria com scorecard de 7 regras. Conecta dinamicamente com as marcas de _brands/."
license: MIT
metadata:
  author: Felipe Bahia (Futuro Mercado)
  version: 1.0.0
---

# Carousel Copy — Redação e Estruturação de Carrosséis para Modelos de Imagem de IA

> **Princípio Central:** O copy decide a estrutura e o ritmo do carrossel; o modelo de imagem de IA apenas materializa visualmente o plano. Nunca gere imagens sem antes ter o plano lâmina a lâmina fechado, validado e com teto rigoroso de palavras.

---

## 🧭 Visão Geral & Modos de Operação

O `social-carrossel` resolve o maior gargalo da geração de imagens via IA: **alucinação tipográfica causada por excesso de texto**. Ele estrutura o carrossel em lâminas enxutas (6 a 8 no total), garantindo alta retenção cognitiva e aderência estética absoluta aos modelos generativos (ChatGPT / GPT Image 2, FLUX, Midjourney).

A skill opera em dois modos:

1. **Modo Planejamento (Plan Mode):** Você fornece um tema, dor de cliente, anotações brutas ou concorrente minerado. A skill gera o plano lâmina a lâmina completo com título, corpo, metáfora visual e indicação de Slide de Salvamento.
2. **Modo Auditoria (Audit Mode):** Você fornece um carrossel pronto ou rascunho de copy. A skill audita cada lâmina contra as 7 Regras de Ouro, emite um Scorecard analítico (Passou / Falhou + Ajuste Específico) e devolve a versão blindada reescrita.

---

## 🎯 Conexão Dinâmica com a Marca Ativa (`_brands/`)

Antes de redigir qualquer linha, identifique a marca ativa (`plinq`, `waimonitor`, `pr-pulse`, `plus-pr`, `felipe-bahia`, `experimentacao`):

1. **Regra STOP Mandatória:** Se a marca não foi definida, pergunte imediatamente antes de prosseguir.
2. **Carregamento de Diretrizes (`_brands/<marca>/`):**
   - `brand-voice.md`: Tom de voz, nível de formalidade e termos proibidos ("O que NÃO comunicar").
   - `personas.md`: Dores viscerais, termos do dia a dia e objeções reais da persona.
   - `content-pillars.md`: Alinhamento do tema com os pilares estratégicos da marca.

---

## 📐 Estrutura Obrigatória do Carrossel (6 a 8 Lâminas)

Evite carrosséis com menos de 5 lâminas (percepção de conteúdo raso) ou com mais de 10 lâminas (queda brusca na taxa de conclusão). O padrão ouro é **6 a 8 lâminas**.

```
┌─────────────────────────────────────────────────────────────┐
│ 1. SLIDE 1 (HOOK) — Dor visceral ou choque contraintuitivo  │
├─────────────────────────────────────────────────────────────┤
│ 2. SLIDE 2 (VALOR 1) — Payoff imediato (zero enrolação)     │
├─────────────────────────────────────────────────────────────┤
│ 3. SLIDES 3 a 5 (VALOR 2 a 4) — 1 ideia / passo por lâmina  │
├─────────────────────────────────────────────────────────────┤
│ 4. SLIDE 5 ou 6 (SAVE-BAIT) — O Slide de Salvamento         │
├─────────────────────────────────────────────────────────────┤
│ 5. SLIDE FINAL (CTA) — Conversão na DM com 1 ação única     │
└─────────────────────────────────────────────────────────────┘
```

---

## ⚖️ As 7 Regras de Ouro & Scorecard de Auditoria

### Regra 1: Hook = Dor Direta, Zero Introdução
O Slide 1 encapsula a dor do leitor ou faz uma afirmação de quebra de padrão em no máximo 2 linhas. Nada de subtítulo explicando o que o carrossel vai ensinar ("Neste carrossel você vai aprender...").
- **Checagem:** Cubra todo o carrossel exceto o Slide 1. Um estranho no feed pararia o dedo e arrastaria? Se o gancho precisar de uma segunda frase de apoio para fazer sentido, ele é fraco — reescreva.

### Regra 2: Proibição de Slide de Sumário / "O que Veremos"
Nunca insira um slide de transição ou índice entre o Hook e o primeiro valor. O Slide 2 é a zona crítica de desistência do leitor; ele deve entregar a primeira recompensa prática imediatamente. O encadeamento se revela enquanto a pessoa arrasta (Passo 01, Passo 02...).
- *Exceção Permitida:* Slide de Prova Tangível (print real de métricas, dashboard ou mensagem de cliente) no Slide 2, exclusivamente se a afirmação bombástica do Slide 1 exigir validação imediata para sustentar a credibilidade.
- **Checagem:** O Slide 2 entrega valor prático e aplicável sozinho? Se for apenas uma introdução, apague.

### Regra 3: Uma Única Ideia por Lâmina
Cada lâmina de valor carrega estritamente uma ação, um conceito ou uma lição. Se precisar da conjunção "e" para resumir o que a lâmina ensina, divida em duas ou elimine a menos importante.
- **Checagem:** Resuma cada slide em um único verbo no infinitivo ("Auditar o banco", "Travar a âncora", "Eliminar intermediários"). Se houver dois verbos, são dois slides.

### Regra 4: Limite Rígido de Palavras (~25 Palavras de Corpo)
Modelos de imagem deformam e alucinam blocos densos de texto. O orçamento tipográfico por lâmina é inegociável:
- **Título:** 1 a 5 palavras, em CAIXA ALTA, tipografia dominante.
- **Corpo:** Máximo de 3 linhas curtas, somando no máximo ~25 palavras no total.
- **Detalhes e Dados:** Tudo o que passar desse teto deve ser transferido para o elemento visual (gráfico, cards de antes/depois, fluxograma, tabela), nunca em parágrafos de texto corrido.
- **Checagem:** Conte as palavras do corpo. Passou de 25 palavras? Corte o texto ou transfira os itens para a metáfora visual.

### Regra 5: Toda Lâmina Especifica sua Metáfora Visual
Um carrossel não é um arquivo de texto com fundo colorido. Cada lâmina precisa ter uma metáfora visual descrita em uma linha objetiva (ex: diagrama comparativo, cards de antes/depois, checklist anotado, gráfico de barras limpo, interface simplificada).
- **Checagem:** O elemento visual faria sentido e ensinaria algo se fosse visualizado sem o texto de apoio? Se o visual for apenas "o texto centralizado e estilizado", crie uma representação gráfica concreta.

### Regra 6: Slide de Salvamento (Save-Bait) & Frase Screenshotable
O algoritmo recompensa posts com alto volume de salvamentos (Saves). Para isso, o carrossel deve conter dois elementos mandatários:
1. **O Slide de Salvamento (Eixo 3 de `viral-carousel`):** Inserido na penúltima lâmina de valor (Slide 5 ou 6). Deve apresentar uma síntese ultra-densa e prática (Checklist de Ação, Matriz Comparativa, Tabela Decisória ou Mapa Mental) para que o leitor salve o post para consultar depois.
2. **A Frase Screenshotable:** Pelo menos uma lâmina do carrossel deve conter uma frase tão afiada e concisa que o leitor sinta vontade de tirar print e compartilhar nos stories ou no WhatsApp.
- **Checagem:** Há um slide que atua como ímã de salvamentos para consulta futura? Há uma frase que você postaria sozinha como citação de autoridade?

### Regra 7: CTA com Tratamento de Gancho (1 Ação Única)
A lâmina final de conversão deve receber o mesmo capricho de redação do Slide 1. O leitor acabou de receber alto valor; agora ele quer o próximo passo.
- **Mecânica Direta:** Indique uma única ação clara: comentar uma palavra-chave para receber material exclusivo na DM (ex: *"Comente AUDITORIA para receber o checklist em PDF no seu direct"*).
- **Proibição Estrita:** Nunca dê duas opções na mesma lâmina (ex: "comente X, curta e clique no link da bio"). Mais de uma opção destrói a conversão.
- **Checagem:** Há apenas uma chamada à ação? O texto do CTA é tão enxuto quanto o do Slide 1?

---

## 📋 Formato de Saída (Template Padronizado)

Ao operar no **Modo Planejamento**, utilize rigorosamente o formato abaixo:

```markdown
### 1. Marca & Premissas
- **Marca Ativa:** [Marca de _brands/]
- **Público & Dor:** [Persona e dor central abordada]
- **Objetivo Algorítmico:** SAVE + LEAD
- **Mecânica de CTA:** Comente [PALAVRA-CHAVE] na DM

### 2. Estrutura & Racional
- **Total de Lâminas:** [6 a 8 lâminas]
- **Racional:** [Por que este número e encadeamento foram escolhidos]

### 3. Plano Lâmina a Lâmina

**SLIDE 1 — HOOK (Scroll-Stopper)**
- **TÍTULO:** [1 a 5 palavras em CAIXA ALTA]
- **Corpo:** [Até 2 linhas curtas, max 20 palavras]
- **Visual:** [Descrição concreta da metáfora visual / elemento gráfico]

**SLIDE 2 — VALOR 01 (Payoff Imediato)**
- **TÍTULO:** [1 a 5 palavras em CAIXA ALTA]
- **Corpo:** [Até 3 linhas curtas, max 25 palavras]
- **Visual:** [Descrição do diagrama, card ou elemento]

**SLIDE 3 — VALOR 02 (Passo Prático)**
- **TÍTULO:** [1 a 5 palavras em CAIXA ALTA]
- **Corpo:** [Até 3 linhas curtas, max 25 palavras]
- **Visual:** [Descrição visual]

**SLIDE 4 — VALOR 03 (O Pulo do Gato)**
- **TÍTULO:** [1 a 5 palavras em CAIXA ALTA]
- **Corpo:** [Até 3 linhas curtas, max 25 palavras]
- **Visual:** [Descrição visual]

**SLIDE 5 — SAVE-BAIT (Slide de Salvamento)**
- **TÍTULO:** [1 a 5 palavras em CAIXA ALTA]
- **Corpo:** [Até 3 linhas curtas, max 25 palavras]
- **Visual:** [Matriz, Checklist de Ação ou Tabela Comparativa de consulta rápida]

**SLIDE 6 — CTA (Conversão)**
- **TÍTULO:** [1 a 5 palavras em CAIXA ALTA]
- **Corpo:** [Instrução direta da palavra-chave para DM, max 20 palavras]
- **Visual:** [Card de mock-up do entregável ou caixa de mensagem com a palavra destacada]

### 4. Frase Screenshotable
- **Lâmina:** [Slide X]
- **Frase:** "[A frase de maior impacto do carrossel]"

### 5. Auditoria de Palavras (Word-Count Check)
- Slide 1: X palavras (≤ 20) — OK
- Slide 2: X palavras (≤ 25) — OK
- Slide 3: X palavras (≤ 25) — OK
- Slide 4: X palavras (≤ 25) — OK
- Slide 5: X palavras (≤ 25) — OK
- Slide 6: X palavras (≤ 20) — OK
```

---

## 🔍 Scorecard de Auditoria (Modo Auditoria)

Ao auditar carrosséis existentes, gere o scorecard abaixo antes de apresentar o plano reescrito:

| # | Regra de Ouro | Status | Diagnóstico & Ajuste Específico |
|---|---|---|---|
| **1** | Hook = Dor Direta, Zero Introdução | `PASSOU` / `FALHOU` | [Explicação clara do ajuste se falhou] |
| **2** | Sem Slide de Sumário no Slide 2 | `PASSOU` / `FALHOU` | [Se houver introdução, indicar corte] |
| **3** | Uma Ideia por Lâmina | `PASSOU` / `FALHOU` | [Indicar onde houve acúmulo de ideias] |
| **4** | Teto de ~25 Palavras de Corpo | `PASSOU` / `FALHOU` | [Indicar lâminas que estouraram o teto] |
| **5** | Metáfora Visual Obrigatória | `PASSOU` / `FALHOU` | [Indicar onde falta representação gráfica] |
| **6** | Slide de Salvamento & Screenshotable | `PASSOU` / `FALHOU` | [Indicar ausência de checklist/matriz ou frase marcante] |
| **7** | CTA com Tratamento de Gancho (1 Ação) | `PASSOU` / `FALHOU` | [Garantir uma única ação via DM] |

---

## 🚫 Filtro Anti-Slop Obrigatório

Antes de aprovar qualquer copy:
- Elimine termos clichês de IA: "no cenário atual", "crucial", "revolucionário", "mergulhar", "desvendar", "portanto", "além disso", "como um divisor de águas".
- Escreva com a cadência oral do profissional brasileiro: direto, substantivo, sem adjetivação inflada.
- Respeite as proibições específicas da marca ativa registradas em seu `brand-voice.md`.

---

## 📚 Biblioteca de Referências Operacionais

| Arquivo de Referência | Escopo Técnico |
|---|---|
| [`references/reverse-engineering-viral-carousels.md`](references/reverse-engineering-viral-carousels.md) | Framework de dissecação, engenharia reversa e análise de retenção de carrosséis virais de LinkedIn e Instagram. |
