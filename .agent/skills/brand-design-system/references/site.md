# Site de referência: `index.html`

Um único arquivo, autocontido: CSS e JS inline, sem CDN, sem fonte externa, sem rastreamento. Gerado a partir do `tokens.json`.

## Estrutura

- **Menu lateral escuro** à esquerda, fixo, com âncoras para as 12 seções. Escuro nos dois temas da página. Em celular vira gaveta aberta por botão.
- **Barra superior** com: alternador sol/lua (SVG inline, sem emoji), botão **Download DESIGN.md**, botão **Print spec sheet**.
- **Seções, nesta ordem:** Overview, Principles, Color, Typography, Spacing, Shape, Motion, Components, Patterns, Imagery, Token exports, Voice & tone. Cada uma com `id` igual ao nome em minúsculas e hífen.

## Conteúdo por seção

| Seção | Conteúdo |
|---|---|
| Overview | resumo da marca, sensação, "não deve parecer", tabela de origem das decisões |
| Principles | 4 a 6 princípios visuais, cada um ligado a uma decisão da essência ou da voz |
| Color | amostras por papel nos dois temas; clique copia o hex; tabela de contraste com razão e resultado |
| Typography | escala completa com amostra viva, famílias, regras, pares de fontes |
| Spacing | régua dos degraus com valor e nome |
| Shape | raios, bordas, exemplos de cantos |
| Motion | durações e curvas com demonstração (respeita reduced motion) |
| Components | os 6 grupos, cada um em painéis lado a lado **Light** e **Dark** |
| Patterns | 3 a 4 telas realistas com conteúdo de exemplo rotulado |
| Imagery | estilos travados ou placeholder |
| Token exports | quatro blocos copiáveis: CSS, Tailwind, JSON, JS |
| Voice & tone | resumo de `brand-voice.md` e "O que NÃO comunicar", com ponteiro ao arquivo |

## Painéis independentes de tema

```html
<div class="panel" data-theme="light"> ... </div>
<div class="panel" data-theme="dark"> ... </div>
```

```css
.panel { background: var(--bg); color: var(--text); }
```

Os tokens são definidos por `[data-theme]`, então o painel redefine as variáveis para seus descendentes, sem depender de `<html>`.

## Comportamentos

- **Alternar tema:** muda `data-theme` em `<html>`; guarda a escolha em `localStorage` dentro de `try/catch` (pode falhar em `file://` ou modo privado) e funciona sem isso. Estado inicial por `prefers-color-scheme`.
- **Copiar:** amostras de cor e blocos de código. Usar `navigator.clipboard.writeText` e, se falhar, `document.execCommand('copy')` com um `textarea` temporário. Mostrar confirmação textual curta ("Copiado"), com `aria-live="polite"`.
- **Download DESIGN.md:** embutir o texto em `<script type="text/plain" id="design-md">`, criar `Blob` com `text/markdown`, `URL.createObjectURL`, link `download="DESIGN.md"`. Deve funcionar abrindo o arquivo direto do disco.
- **Print:** botão chama `window.print()`. Em `@media print`: fundo branco, texto escuro, menu e barra ocultos, `break-inside: avoid` em amostras e painéis, URLs de links não impressas, painéis Light e Dark preservam cores (`print-color-adjust: exact`), tamanho de página A4.
- **Celular:** a partir de 360 px, sem rolagem horizontal; painéis lado a lado empilham abaixo de 800 px; alvos de toque de 44 px; tabelas rolam dentro do próprio contêiner.
- **Acessibilidade:** `lang="pt-BR"` quando a marca é brasileira, landmarks (`nav`, `main`), foco visível, botões com `aria-label`, toggle com `aria-pressed`, ordem de tabulação lógica.

## Telas (Patterns)

Cada tela é um bloco com moldura simples (sem imitar marca de terceiros), usando só os componentes e tokens do sistema. Conteúdo em português, marcado discretamente como "Conteúdo de exemplo". Sem logos de terceiros, sem dados pessoais reais, sem números apresentados como resultado real.

## Imagery

Com anexos: por estilo, cartão com a imagem de referência (caminho relativo ou `data:` se pequeno), tabela de regras (luz, ângulo, paleta, tratamento, composição, nunca mostrar) e bloco copiável:

```
Assunto: <uma frase>
Estilo: <bloco fixo do Style 0N, idêntico em todo uso>
```

Sem anexos: cartão placeholder com texto "Sem imagens de referência. Envie exemplos para criar estilos travados."

## Regras finais

- Sem emoji, sem gradiente (exceto o permitido), sem enchimento.
- Os valores do CSS são os do `tokens.json`; nenhuma cor literal fora das variáveis, exceto nos blocos de exemplo de código.
- Tamanho total modesto (alvo abaixo de 300 KB).
