# Tokens, contraste e exports

## `tokens.json` (fonte única)

```json
{
  "name": "Marca",
  "description": "uma frase",
  "colors": {
    "light": { "bg": "#FFFFFF", "surface": "#F6F6F4", "border": "#D9D9D4",
               "text": "#16181A", "text-muted": "#53575B",
               "primary": "#0F4C81", "on-primary": "#FFFFFF" },
    "dark":  { "bg": "#101214", "surface": "#181B1E", "border": "#2D3236",
               "text": "#ECEEEF", "text-muted": "#A3A9AE",
               "primary": "#7FB2E5", "on-primary": "#0B1A29" }
  },
  "typography": {
    "font-sans": "system-ui, -apple-system, 'Segoe UI', Roboto, sans-serif",
    "font-mono": "ui-monospace, SFMono-Regular, Menlo, monospace",
    "scale": { "display": { "size": "3rem", "line": "1.1", "weight": 700 } }
  },
  "rounded": { "sm": "4px", "md": "8px", "lg": "16px", "full": "9999px" },
  "spacing": { "1": "4px", "2": "8px", "3": "12px", "4": "16px", "6": "24px", "8": "32px" },
  "motion": { "fast": "100ms", "base": "200ms", "slow": "320ms" },
  "components": { "button-primary": { "bg": "primary", "color": "on-primary", "radius": "md" } }
}
```

Exemplos acima são formato, não paleta. Os valores reais vêm das decisões.

Convenções:
- Nomes semânticos (`primary`, não `blue-500`). Escala de neutros pode usar números.
- Hex em 6 dígitos maiúsculos nos artefatos (site e DESIGN.md), para a comparação por texto ser exata. OKLCH pode ser usado só no export Tailwind, derivado do mesmo hex e marcado como tal.
- Todo valor existe no claro e no escuro quando for de cor.

## Contraste (WCAG)

Pares mínimos a conferir **nos dois temas**: `text/bg`, `text/surface`, `text-muted/bg`, `text-muted/surface`, `on-primary/primary`, `primary/bg` (3:1 como componente), `border/bg` (3:1 se for limite de campo), `focus/bg` (3:1), estados de status (`success`, `warning`, `danger`, `info` como texto sobre `bg` e `surface`).

Limiares: 4,5:1 texto normal, 3:1 texto grande (a partir de 24 px, ou 18,66 px em negrito) e componentes de interface.

Cálculo (rodar no scratchpad com `python3 -I -c`, sem criar arquivo no projeto):

```python
def lum(h):
    h = h.lstrip('#'); r,g,b = [int(h[i:i+2],16)/255 for i in (0,2,4)]
    f = lambda c: c/12.92 if c <= 0.03928 else ((c+0.055)/1.055)**2.4
    return 0.2126*f(r)+0.7152*f(g)+0.0722*f(b)
def ratio(a,b):
    la,lb = sorted((lum(a),lum(b)),reverse=True)
    return (la+0.05)/(lb+0.05)
```

Gerar a tabela completa de pares (cada um com razão e aprovado/reprovado) a partir do `tokens.json` e guardar em `_respostas/contraste-design-system.md`. Par reprovado: ajustar o token e refazer; só seguir com tudo aprovado ou com exceção declarada em Known Gaps.

## CSS do site (variáveis)

```css
:root, [data-theme="light"] { --bg: ...; --text: ...; /* um por token claro */ }
[data-theme="dark"]         { --bg: ...; --text: ...; /* um por token escuro */ }
```

O toggle da página muda `data-theme` em `<html>`. Cada painel de componente fixa `data-theme="light"` ou `"dark"` no próprio elemento, com `background: var(--bg)` e `color: var(--text)`, para manter o tema independente do toggle. Usar `@media (prefers-color-scheme: dark)` apenas para o estado inicial, quando não houver escolha salva.

## Exports (todos copiáveis, todos gerados do `tokens.json`)

1. **CSS variables**: o bloco acima.
2. **Tailwind v4** (CSS-first, verificado no Context7): 

```css
@import "tailwindcss";
@custom-variant dark (&:where([data-theme=dark], [data-theme=dark] *));
@theme {
  --color-bg: #FFFFFF;
  --color-primary: #0F4C81;
  --font-sans: system-ui, sans-serif;
  --radius-md: 8px;
  --spacing-4: 16px;
}
```

   Namespaces válidos: `--color-*`, `--font-*`, `--text-*`, `--radius-*`, `--spacing-*`, `--shadow-*`, `--ease-*`. Para o modo escuro, redefinir os `--color-*` sob `[data-theme=dark]` com `@layer base`. Em projeto com Tailwind v3, gerar `tailwind.config.js` com `theme.extend` e `darkMode: ['selector', '[data-theme="dark"]']`; consultar o Context7 antes.
3. **JSON**: o próprio `tokens.json`.
4. **Objeto JS**: `export const theme = { light: {...}, dark: {...}, ... }`.
