# Rubrica de QA do brandbook

Mecânica emprestada do `execution-loop`: cada item recebe nota de 0 a 10 com **evidência verificável** (trecho citado, arquivo, comando). 10 = cumprido e provado. Abaixo de 10 = a etapa responsável volta. Nunca nota por impressão.

Gravar o resultado em `<raiz da marca>/_respostas/qa-brandbook.md` (uma versão por rodada, `-v1`, `-v2`).

| # | Item | Critério de 10 | Etapa que corrige |
|---|---|---|---|
| 1 | Completude | Todos os arquivos das etapas aprovadas existem na raiz da marca (`_brands/<marca>/` ou `<projeto>/brand/`) e o `brandbook.md` linka cada um | 9 |
| 2 | Rastreabilidade | Cada afirmação relevante tem tag de proveniência; nenhuma `[derivado]` sem confirmação do usuário | etapa de origem |
| 3 | Coerência | Nenhuma contradição entre essência, posicionamento, voz e visual (conferir pares: credo x "não comunicar", arquétipo x escalas de voz, sensação visual x voz) | 1-6 |
| 4 | Respeito ao existente | Nenhum arquivo anterior sobrescrito; divergências listadas em Known Gaps | 0 |
| 5 | Voz testável | Cada traço tem frase certa e errada; "O que NÃO comunicar" existe e tem pelo menos 5 itens específicos | 4 |
| 6 | Público concreto | Cada persona tem situação real, objeção e vocabulário | 3 |
| 7 | Pilares ligados à dor | Cada pilar aponta uma dor de persona e um ativo da essência | 4 |
| 8 | Visual consistente | Valores do site, do CSS e do DESIGN.md idênticos; contraste dos pares texto/fundo conferido nos dois temas | 7 |
| 9 | Ativação aplicável | Os quatro arquivos de `ativacao/` (ou os escolhidos no Intake) trazem regra, origem e exemplo | 8 |
| 10 | Slop | Textos passaram pelo `/ai-slop-detector`; sem cliché de IA | qualquer |
| 11 | Lacunas honestas | Known Gaps lista o que ficou em aberto e o que não pôde ser verificado | 9 |
| 12 | Aprovação do usuário | Cada etapa tem aprovação registrada no estado de `00-intake.md` | 0 |
| 13 | Desejo com evidência | `05-desejo.md` traz o grau de cada item auditado com trecho observado (sem evidência, máximo 1; evidência indireta, máximo 3), peso do público por persona, 3 apostas com item do Canvas, teste de apelo e handoff; ou declara que a auditoria foi pulada por falta de material | 5 |
| 14 | Mensagens com prova | Se `mensagens.md` existe: promessa, 3 a 5 proposições ligadas a dores de persona, cada uma com prova com origem ou marcada como "promessa a validar"; nenhuma afirmação contra "O que NÃO comunicar" | 4 |
| 15 | Exportação visual | `design-system/visual-style.md` existe (ou a decisão de não gerar está registrada no Intake ou em Known Gaps; vale para marcas feitas antes do passo 7b) e todo hex dele existe no `tokens.json` (comando de paridade em `brand-design-system/references/export-visual-style.md`) | 7 |
| 16 | Identidade e ativos | Se `identidade-e-ativos.md` existe (sempre, em qualquer profundidade): versões do logo com arquivo real; ficha de cor com hex idêntico ao `tokens.json` e CMYK/Pantone preenchidos por fonte confiável ou marcados "a definir" com responsável; tipografia com licença e pilha de reserva; direitos de imagem registrados; tabela de aprovação preenchida ou lacuna declarada | 7c |
| 17 | Navegação e lacunas | `versoes.json` existe e bate com a pasta; `brand_html.py check` sem problema (HTML gêmeo atualizado, nenhum `.md` fora do registro); links do brandbook em HTML levam a HTML; `brandbook.md` tem a seção "Lacunas reunidas" cobrindo as lacunas de cada arquivo vigente (`gaps`); revisão de nomes e lugares feita (`brandbook-e-ativos.md`, seção 10.4) | 9 |
| 18 | Paridade e informação insuficiente | Os mesmos arquivos e seções existem em qualquer profundidade; cada seção sem base traz o bloco "Informação insuficiente" e consta em "Lacunas reunidas"; nenhuma seção omitida; registro de perguntas e respostas (ou de delegação) em `_respostas/respostas-do-usuario/` | 9 |
| 19 | HTML de cor e afins e shadcn | Cada menção de cor, fonte, logo, estilo, looks e componentes tem HTML visto num navegador; o design system mostra componentes shadcn com tokens nomeados como no shadcn (`brand-design-system/references/shadcn.md`) | 7 |

## Regras

- Evidência de visual (item 8) exige abrir o `index.html` de verdade e conferir; se não foi possível, nota máxima 7 e declarar.
- Depois de 3 rodadas sem 10 em tudo, parar e levar as lacunas ao usuário (estreitar escopo, aceitar nota menor, buscar especialista).
- Ao fechar, propor ao usuário (sem fazer) a linha no `style-guide.md` apontando para `DESIGN.md` e `brandbook.md`.
