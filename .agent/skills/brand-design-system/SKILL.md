---
name: brand-design-system
description: "Use para montar o design system da marca como site de referência mais DESIGN.md (paleta com modo escuro, tipografia, espaço, forma, movimento, componentes e tokens), a partir da direção visual aprovada (etapa 7 do brand-builder). Gatilhos: \"design system da marca\", \"DESIGN.md\", \"tokens da marca\". NÃO use para decidir o estilo (use brand-visual-direction) nem para escrever o código de componentes em Tailwind e React (use site-tailwind-design-system)."
license: MIT
metadata:
  author: Antigravity Multi-IA Hub & Felipe Bahia (Futuro Mercado)
  version: 1.0.0
---

# Brand Design System

## Overview

Etapa 7 do `brand-builder`. Gera, a partir da direção visual aprovada e do que a marca já tem, o design system executável: `index.html` (site único de referência, autocontido) e `DESIGN.md` (arquivo exportável), em `_brands/<marca>/design-system/`.

Adapta o prompt externo "Build me a complete design system" (registrado em `.agent/plans/Brand Builder [PLAN].md`) e corrige o ponto fraco dele: aqui as decisões vêm de essência, voz e persona, não de 5 respostas rasas.

**Princípio central: uma única fonte de valores (`tokens.json`). Site, CSS e DESIGN.md são gerados dela, nunca digitados três vezes.**

## Antes de começar

1. `06-direcao-visual.md` **aprovado**. Sem ele, parar e voltar à etapa 6.
2. Ler `_brands/<marca>/style-guide.md`, `brand-voice.md`, `personas.md`, `01-essencia.md`.
3. **Identidade existente vence.** Se o `style-guide.md` define paleta e fontes, eles são a base; estender, nunca substituir. Conflito com as regras abaixo (ex.: "sem gradiente" contra uma marca com gradiente) -> o `style-guide.md` vence e o conflito vai para `Known Gaps` do `DESIGN.md`.
4. Perguntar no máximo 3 coisas, só se algo importante estiver ambíguo. Aceitar anexos: logo, prints, imagens-modelo.
5. Antes de escrever código de Tailwind, consultar o Context7 para a versão realmente adotada. Hoje o repositório adota v4 (`@theme`); em projeto com v3, ver `references/tokens-e-contraste.md`.

## Fluxo

| Passo | O que faz | Referência |
|---|---|---|
| 1 | Decidir paleta, tipografia, espaço, forma, movimento e componentes. **Componentes: sempre shadcn/ui, em qualquer profundidade** | `references/decisoes.md`, `references/shadcn.md` |
| 2 | Escrever `tokens.json` (claro e escuro), com o mapeamento para os tokens do shadcn (`background`, `primary`, `muted`, `ring` etc.) | `references/tokens-e-contraste.md`, `references/shadcn.md` |
| 3 | Conferir contraste de todos os pares texto/fundo nos dois temas | `references/tokens-e-contraste.md` |
| 4 | Gerar `DESIGN.md` a partir de `tokens.json` | `references/design-md.md` |
| 5 | Gerar `index.html` a partir de `tokens.json` | `references/site.md` |
| 6 | Verificar (abrir, temas, download, copiar, impressão, celular, paridade) | `references/verificacao.md` |
| 7b | Exportar `visual-style.md` derivado do `tokens.json` (insumo para gerar imagem, carrossel, slide e vídeo no estilo da marca) | `references/export-visual-style.md` |
| 7 | Mostrar ao usuário, ajustar, aprovar | |

## Regras

1. Sem emoji. Sem gradiente (exceto se o `style-guide.md` da marca usa). Sem texto de enchimento.
2. Texto legível nos dois temas: contraste mínimo de 4,5:1 para texto normal e 3:1 para texto grande e componentes de interface.
3. **Voice & tone não é inventada:** a seção resume e referencia `brand-voice.md`, incluindo "O que NÃO comunicar". Nada de voz nova aqui.
4. Conteúdo de exemplo das telas em português quando a marca é brasileira, verossímil e sem dado real de terceiros. Sem depoimentos nem números fabricados apresentados como reais; rotular como exemplo.
5. **Imagery:** com imagens anexadas, um estilo travado por imagem ("Style 01", "Style 02"...). Sem anexos, a seção é placeholder explícito.
6. Nunca sobrescrever o `style-guide.md`. No fim, propor ao usuário (sem fazer) a linha que aponta para `DESIGN.md`.
7. Nova versão do design system é `design-system-v2/` ou arquivos `-v2`; não editar a versão anterior in place.
8. Código do site é artefato de marca em `_brands/`, não aplicação. Ainda assim, não criar nada fora de `design-system/`.
9. Não incluir segredo, URL de rastreamento ou dependência externa no site: tudo inline, fontes via pilha de sistema ou arquivo local, salvo decisão do usuário.

## Gerador (scripts/)

Autorizado pelo usuário em 2026-10-19. Dois arquivos, Python 3.9+, sem dependências:

- `scripts/design_tokens.py`: **específico da marca** (`TOKENS`). Rodado sozinho, confere contraste e falha se algum par reprovar.
- `scripts/build_design_system.py`: lê os tokens e gera `tokens.json`, `DESIGN.md` e `index.html`. As partes marcadas `BRAND-SPECIFIC` (textos, telas de exemplo, origem das decisões, gaps) devem ser reescritas por marca, já acentuadas.

```bash
DS_BRAND_DIR=<pasta da marca> DS_LOGO_DIR=<pasta com logo.svg e logo-light.svg> \
DS_VOICE_FILE=brand-voice.md python3 -I scripts/build_design_system.py
```

Para outra marca: copiar os dois arquivos para o scratchpad, editar, rodar, verificar (`references/verificacao.md`). O modo de usar em uma marca nova é editar os tokens e os blocos `BRAND-SPECIFIC`, não editar a skill. Reprodutibilidade provada: reproduziu byte a byte o design system do WaiMonitor.

## Saídas

```
_brands/<marca>/design-system/
  tokens.json      fonte única de valores
  DESIGN.md        exportável
  index.html       site de referência, autocontido
  visual-style.md  estilo portátil para prompts (passo 7b, derivado do tokens.json)
```

## Erros comuns

| Erro | Correção |
|---|---|
| Digitar valores nos três lugares | Gerar de `tokens.json`; a paridade vira verificação mecânica |
| Dark mode como inversão automática | Definir cada token escuro com contraste conferido |
| Painéis do componente seguindo o toggle da página | Cada painel fixa o próprio `data-theme` |
| Reinventar a voz na seção Voice & tone | Resumir e referenciar `brand-voice.md` |
| Declarar "verificado" sem abrir a página | Abrir, testar cada item, relatar o que não deu para verificar |
| Fonte web externa que quebra offline | Pilha de sistema ou arquivo local, salvo decisão do usuário |
| Corrigir acento com dicionário no arquivo todo | Escrever já acentuado; correção cega quebra CSS (`@media`) e termos como "social media" |
| Guardar o gerador na pasta da marca | O gerador fica em `scripts/` desta skill; só `index.html`, `DESIGN.md` e `tokens.json` entram na pasta da marca |
