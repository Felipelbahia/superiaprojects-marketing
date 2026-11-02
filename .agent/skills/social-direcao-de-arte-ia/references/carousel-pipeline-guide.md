# Guia Operacional — Esteira de Renderização de Carrosséis via Modelos de Imagem de IA

> Este guia detalha a esteira técnica completa para transformar o plano textual de `social-carrossel` e os prompts de `social-direcao-de-arte-ia` em lâminas visuais geradas por IA, com consistência estética absoluta e zero alucinações tipográficas.

---

## 🚀 Visão Geral da Linha de Montagem

A criação de um carrossel via modelos de imagem no `0 Mkt` segue uma esteira sequencial e disciplinada de 6 etapas:

```
[ 1. PLANO DE COPY ] ──> [ 2. INJEÇÃO DE BRAND ] ──> [ 3. VARIAÇÃO DO HOOK (3x) ]
   (social-carrossel)           (style-guide.md)             (escolha do vencedor)
                                                                 │
[ 6. AUDITORIA FINAL ] <── [ 5. LÂMINAS ANCORADAS ] <── [ 4. SLIDE ÂNCORA (Slide 2) ]
  (Checklist 7 pts)          (Refs nos Slides 3 a N)        (Travamento da referência)
```

---

## 🛠️ Opções de Ferramentas de Renderização

### Opção A: ChatGPT com GPT Image 2 (Recomendada para Início Rápido)
O modelo GPT Image 2 da OpenAI oferece a maior taxa nativa de acerto tipográfico em língua portuguesa e compreende imagens de referência anexadas diretamente na conversa.
- **Como Operar:**
  1. Copie o prompt gerado pelo `social-direcao-de-arte-ia` para o Slide 1 (Hook).
  2. Cole no chat do ChatGPT e gere as 3 variantes divergentes.
  3. Para o Slide 2, gere as 3 opções de layout. Ao escolher a vencedora, baixe a imagem para seu computador.
  4. Para as lâminas seguintes (Slides 3 em diante), anexe o arquivo do Slide 2 na mensagem do ChatGPT junto com o prompt da lâmina atual contendo o bloco `[CONSISTENCY]`.
  5. O modelo reproduzirá o fundo, proporções, fontes e margens exatas do Slide 2.

### Opção B: Midjourney v6+
O Midjourney se destaca pelo acabamento estético sofisticado e texturas ricas.
- **Como Operar:**
  - Adicione o parâmetro de proporção: `--ar 4:5`.
  - Use o Style Reference (`--sref <URL_DA_ANCORA>`) para transferir a paleta e estilo do Slide 2 para os slides seguintes.
  - Ajuste a intensidade do estilo com `--sw 100` a `200` para manter fidelidade estrita.
  - Para textos exatos, coloque as palavras entre aspas duplas e mantenha o número total de caracteres baixo.

### Opção C: Família FLUX (BFL FLUX.1 via fal.ai, Replicate ou API)
Para pipelines automatizados no terminal, a família FLUX (especialmente FLUX.1 [dev] e [pro]) oferece excelente renderização tipográfica e controle programático.
- **Como Operar:**
  - Conecte com a skill `.agent/skills/audiovisual-imagem-flux-prompts/SKILL.md`.
  - Utilize o modo Image-to-Image (I2I) ou fluxos de multi-referência, alimentando o Slide Âncora como imagem base para renderizar as lâminas subsequentes com `denoising_strength` calibrado entre 0.35 e 0.50.

---

## 🎯 Protocolo de Execução do Workflow do Slide Âncora

### Passo 1: O Teste Triplo do Hook (Slide 1)
O Slide 1 é o responsável por 90% do sucesso do carrossel no feed. Nunca gere apenas uma opção:
1. Gere os 3 prompts divergentes fornecidos pelo `social-direcao-de-arte-ia` (Layout minimalista centrado, Layout com card anotado, Layout com elemento de contraste visual forte).
2. Coloque as 3 imagens lado a lado na tela.
3. Pergunte-se honestamente: *"Se eu estivesse passando rapidamente pelo feed, qual dessas 3 imagens me forçaria a parar o polegar?"*
4. Se nenhuma te parar, itere o prompt simplificando o título ou aumentando o contraste.

### Passo 2: O Slide Âncora (Slide 2)
1. O Slide 2 entrega a primeira recompensa prática (zero introdução).
2. Gere 3 opções de diagramação (Cards horizontais, Diagrama de fluxo com setas, Caixa de destaque).
3. Selecione a opção com melhor respiro e legibilidade.
4. **TRAVE O SLIDE:** Salve essa imagem como `ancora-visual.png`. Ela define a identidade de todo o resto do carrossel.

### Passo 3: Produção dos Slides de Conteúdo (Slides 3 a 5)
1. Para cada lâmina de valor, anexe `ancora-visual.png` na ferramenta.
2. Utilize o prompt específico com o comando:
   ```
   [CONSISTENCY] match the attached reference image's layout, typography, color palette, and spacing exactly; replace only the text strings and diagram content.
   ```
3. O modelo mantém a consistência gráfica sem que você precise redefinir cores ou fontes a cada etapa.

### Passo 4: O Slide de Salvamento (Save-Bait — Slide 5 ou 6)
1. Esta lâmina consolida o aprendizado (Checklist, Matriz ou Cheatsheet de Ação).
2. A diagramação deve ser mais rica em densidade visual (caixas de seleção, tabela comparativa com colunas Sim/Não, fluxograma decisório).
3. Mantém a paleta e margens da âncora, mas foca em ser o "resumo para guardar e consultar amanhã".

### Passo 5: O CTA de Impacto (Lâmina Final)
1. Gere 3 opções de chamada à ação.
2. Destaque uma única palavra-chave (ex: *"Comente AUDITORIA"*).
3. Utilize elemento de mock-up da entrega ou caixa de comentário nativa de rede social para indicar visualmente a ação esperada.

---

## 🚨 Guia de Diagnóstico e Correção (Troubleshooting)

| Sintoma Observado | Causa Provável | Correção Imediata no Prompt |
|---|---|---|
| **Palavra com grafia errada ou letra duplicada** | Excesso de palavras na lâmina confundindo a atenção do modelo. | Reduza o texto do corpo para menos de 15 palavras. Se persistir, remova o texto do corpo e deixe apenas o Título gigante + diagrama visual. |
| **Cores ou fontes mudaram do Slide 2 para o Slide 3** | O modelo não recebeu ou ignorou a imagem de referência anexada. | Reanexe o Slide Âncora e adicione no topo do prompt: `STRICT REFERENCE MATCH: Do not change typography, background texture, or palette from the attached reference. Modify only the inner diagram and text.` |
| **Layout abarrotado, elementos encostando nas bordas** | Prompt sem especificação clara de margens e respiro. | Adicione no bloco `[LAYOUT]`: `Ultra-generous 10% outer padding on all sides. Negative white space is prioritized. Keep every element centered with ample breathing room.` |
| **Mais de uma cor competindo por atenção** | Falta de restrição no bloco negativo. | Adicione no bloco `[NEGATIVE]`: `no colorful accents, no multi-color elements, strictly monochromatic background with exactly ONE accent color for icons/badges.` |
| **Visual com cara de "arte de banco de imagens" ou 3D genérico** | Descrição visual abstrata ou uso de adjetivos genéricos ("modern", "futuristic"). | Substitua por termos concretos: `minimal flat UI wireframe, editorial 2D vector typography, high contrast crisp lines, monochrome schematic drawing.` |
