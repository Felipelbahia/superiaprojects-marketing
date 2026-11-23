# Passo 7b: exportar o `visual-style.md`

Depois de o design system estar aprovado, **derivar** dele um `visual-style.md`: um arquivo portátil, em YAML mais Markdown, que qualquer IA lê para gerar imagem, carrossel, slide ou vídeo no estilo da marca. É a saída do mesmo conteúdo em outro formato; nada é decidido de novo aqui.

> O design system (`tokens.json`, `DESIGN.md`, `index.html`) serve à tela e ao código. O `visual-style.md` serve ao **prompt**: o campo `style_prompt_full` é, no formato, "o mais importante". Quem gera imagem ou carrossel depois (`social-direcao-de-arte-ia`, `audiovisual-imagem-flux-prompts`, `brand-visual-style` no modo Aplicar) cola esse bloco, em vez de redescobrir o estilo.

**Origem (E5, 2026-10-20):** o formato é da skill `brand-visual-style` (arquivo `references/spec.md` dentro dela); o mapa de campos a partir do `tokens.json`, a forma de escrever o `style_prompt_full` e a verificação de paridade de hex são adaptações `[derivado]` ao design system do `brand-builder`.

**Formato:** especificação em `../../brand-visual-style/references/spec.md`; modelos em `../../brand-visual-style/references/templates/` (mínimo e completo); exemplos em `../../brand-visual-style/references/gallery/`. Ler o `spec.md` antes de escrever.

## Entradas
`design-system/tokens.json` e `DESIGN.md` aprovados; `06-direcao-visual.md` (sensação em 3 palavras, "não deve parecer", imagem, movimento); `style-guide.md` da marca (vence em conflito).

## Mapa: de onde vem cada campo

| Campo do `visual-style.md` | Vem de |
|---|---|
| `name`, `version` | Nome da marca + "Design system" e versão `1.0` |
| `style_prompt_short` | 1 a 2 frases, da sensação em 3 palavras e do caráter (`06-direcao-visual.md`) |
| `style_prompt_full` | **Parágrafo único** com hex reais, nomes de fonte, estrutura de layout, padrão de movimento e humor. Escrever a partir dos tokens, não de memória (ver abaixo) |
| `colors.primary` (mínimo 2) | `primary`, `bg`, `text` do `tokens.json`, cada um com `name`, `hex` e `role`. A variante forte do azul de ação (`primary-strong`, `-text`), quando existe para texto e botões, entra com o papel de texto |
| `colors.accent`, `colors.neutral` | `accent` e cores de estado que a marca usa como assinatura (ex.: alerta); `surface`, `border`, `text-muted` |
| `typography.display`, `.body`, `.caption`, `.rules` | Escala tipográfica do `tokens.json` e regras de `decisoes.md` (seção 2) |
| `layout.grid`, `.alignment`, `.aspect_ratio`, `.notes` | Espaço, forma e densidade (`decisoes.md`, seções 3 e 4); proporção principal dos canais |
| `motion.transitions`, `.animation_style`, `.pacing` | `animation_style` e `pacing` vêm das durações e curvas do `tokens.json` e da seção "Movimento" de `06-direcao-visual.md`. Os **tipos** de transição só entram se a direção visual os cita; do contrário, deixar `transitions` vazio (não inventar) |
| `mood.keywords` | Sensação em 3 palavras |
| `mood.avoid` | "Não deve parecer" e as proibições do design system (sem emoji; sem gradiente, salvo se o `style-guide.md` usa) |
| `assets.*` | Só **URLs**, nunca arquivo embutido; deixar vazio se a marca não tem URL pública |
| `## Connectors`, `## Design Principles`, `## Extraction Notes` | Notas curtas: como colar no gerador; princípios do `DESIGN.md`; "derivado de `tokens.json` versão X em AAAA-MM-DD" |

## Como escrever o `style_prompt_full`

1. Uma frase de caráter (a sensação), em seguida os **hex reais** da paleta com o papel de cada um.
2. Fonte(s) pelo nome, e a regra de uso (títulos x corpo).
3. Layout: grade, respiro, alinhamento, proporção.
4. Movimento: velocidade e tipo de transição (ou "estático").
5. O que **nunca** aparece (de `mood.avoid`).
6. Um tema: o modo claro é o padrão do prompt; se o modo escuro for usado em peças, descrever a variação em uma frase com os hex escuros.
Evitar adjetivo vago ("moderno", "clean"); preferir contraste concreto com o "não deve parecer" (regra do `brand-visual-direction`).

## Regras
1. **Derivado, não digitado de novo:** todo hex do `visual-style.md` existe no `tokens.json`.
2. Sem emoji. Sem gradiente, exceto se o `style-guide.md` já o usa.
3. Nome e versão: `visual-style.md` em `_brands/<marca>/design-system/`; versão nova = `visual-style-v2.md`, sem editar a anterior no lugar.
4. Nada de dependência externa nem chave; assets só por URL.
5. Fonte da marca que o gerador não conhece: o prompt traz a **descrição** da fonte (humanista, geométrica, serifada) além do nome.
6. Texto do arquivo passa pelo `/geral-anti-slop`.

## Verificação (paridade com o `tokens.json`)

Sem criar arquivo no projeto, comparar os hex:

```bash
cd _brands/<marca>/design-system
# hex do visual-style que NÃO estão nos tokens: a saída deve ser vazia
comm -23 <(grep -oE '#[0-9A-Fa-f]{6}' visual-style.md | tr 'a-f' 'A-F' | sort -u) \
         <(grep -oE '#[0-9A-Fa-f]{6}' tokens.json | tr 'a-f' 'A-F' | sort -u)
```

Conferir também que o parágrafo de `style_prompt_full` cita as mesmas fontes do `DESIGN.md`. Resultado vai para `_respostas/` junto da verificação do design system (`verificacao.md`). Abaixo de 10 volta ao passo 7b.

## Uso depois do arquivo pronto
- **Imagem, carrossel e slide:** `social-direcao-de-arte-ia` (injeção do estilo no prompt), `audiovisual-imagem-flux-prompts` (cor por hex), `brand-visual-style` modo Aplicar.
- **Vídeo:** produção no projeto *Edição de Vídeo com IA*; o `style_prompt_full` e `motion.*` são o insumo.
- **Guia de identidade:** o capítulo de imagem (`../../brand-builder/references/identidade-e-ativos/04-imagem.md`) usa o arquivo como bloco de estilo fixo para imagem gerada por IA.
