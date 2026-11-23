# shadcn/ui no design system (obrigatório em qualquer profundidade)

Decisão do usuário, 2026-10-27: o design system de toda marca usa **shadcn/ui** como biblioteca de componentes, tanto na profundidade curta quanto na longa. Fatos abaixo conferidos no Context7 (`/websites/ui_shadcn`) em 2026-10-27; antes de gerar código, consultar de novo a versão adotada (regra 2.8 do hub) e não inventar variante ou token.

## 1. Tokens: nomes do shadcn, valores da marca
O tema do shadcn são variáveis CSS semânticas em `:root` e `.dark`, mapeadas para o Tailwind em `@theme inline` (`--color-primary: var(--primary)` etc.), com `components.json` em `tailwind.cssVariables: true`. O scaffold padrão do shadcn usa OKLCH; a marca pode manter hex no `tokens.json` (fonte única) e declarar o equivalente.
| Token shadcn | Papel | Origem na marca (`tokens.json`) |
|---|---|---|
| `background` / `foreground` | Fundo e texto padrão | fundo e texto principais |
| `card` / `card-foreground` | Superfícies elevadas | superfície |
| `popover` / `popover-foreground` | Menus e sobreposições | superfície |
| `primary` / `primary-foreground` | Ação principal (botão padrão) | cor principal e a letra sobre ela |
| `secondary` / `secondary-foreground` | Ação de menor ênfase | cor secundária |
| `muted` / `muted-foreground` | Apoio, placeholder, texto auxiliar | neutro frio |
| `accent` / `accent-foreground` | Hover, foco e seleção | acento interativo |
| `destructive` | Ação destrutiva, erro | cor de erro |
| `border`, `input`, `ring` | Contorno, campo e foco | borda e foco |
| `chart-1` a `chart-5` | Paleta de gráficos | derivada da paleta |
| `sidebar`, `sidebar-foreground`, `sidebar-primary`, `sidebar-primary-foreground`, `sidebar-accent`, `sidebar-accent-foreground`, `sidebar-border`, `sidebar-ring` | Barra lateral | superfície e acento |
| `radius` | Raio base (os demais derivam: sm, md, lg, xl) | forma da marca |
Regra: **os tokens próprios da marca (ex.: ouro, Brasa) continuam existindo no `tokens.json`; o shadcn recebe o mapeamento**, e o `DESIGN.md` documenta a tabela acima preenchida, claro e escuro. Contraste dos pares (`foreground` sobre `background`, `primary-foreground` sobre `primary` etc.) segue `references/tokens-e-contraste.md`.

## 2. Componentes que o `index.html` mostra (mínimo)
Button (variants default, secondary, outline, ghost, destructive, link; tamanhos e estado desabilitado), Badge, Input, Textarea, Select, Checkbox, Radio Group, Switch, Label e Field, Card, Alert, Tabs, Dialog, Table, Tooltip, Accordion, Navigation Menu, Breadcrumb, Progress, Skeleton, Sonner (toast) e Typography. Os demais (Sidebar, Chart, Calendar, Data Table etc.) entram quando o produto da marca precisar; não inventar componente que não existe na biblioteca.
Cada componente aparece **claro e escuro**, com seus estados (padrão, hover, foco, desabilitado, erro), nomeado como no shadcn, e o HTML é visto num navegador (regra 11 do `brand-builder`).

## 3. O que fica fora (e exige autorização)
Gerar o CSS do tema, o `components.json` e instalar componentes em um projeto de código é código de aplicação: só com autorização explícita. O gerador `scripts/build_design_system.py` **ainda não escreve os tokens com nomes shadcn**; até atualizá-lo (com autorização), o mapeamento da seção 1 entra no `DESIGN.md` e no `index.html` por edição das partes `BRAND-SPECIFIC`.

## 4. Verificação
Conferir no `index.html`: cada token da seção 1 presente nos dois temas, componentes da seção 2 visíveis, console limpo, contraste dos pares. Registrar em `_respostas/qa-e-verificacoes/`.
