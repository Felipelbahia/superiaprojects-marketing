# 10 — Erros do consultor (os "7 pecados" externos como autocheck)

`[externo]` Quatro textos usam a metáfora dos sete pecados para falar de falhas ao trabalhar: em IA (Thoughtworks), em UX (Nielsen Norman Group, com as virtudes opostas), em marketing (Aaron Hayes) e na construção de startups (Sambeet Parija, que usa os pecados como motores de produto). Aqui eles viram **checagens do próprio parecer**, não conteúdo para o cliente. A conversão é `[derivado]`.

## Autochecagens antes de entregar o parecer

| # | Risco | Como aparece num parecer | Checagem | Origem |
|---|---|---|---|---|
| 1 | **Pensamento terceirizado** | Auditar de cabeça, sem olhar a peça | Cada grau tem evidência literal; sem evidência, grau ≤1 | `[externo · UX: Outsourced thinking]` |
| 2 | **Confiança ingênua** | Afirmar como fato o que é inferência | Toda regra tem tag; `[derivado]` aparece como hipótese | `[externo · UX: Naïve trust]` |
| 3 | **Sabor genérico** | Sugestões que serviriam para qualquer marca | Cada recomendação cita público, marca e objetivo concretos | `[externo · UX: Bland taste]` |
| 4 | **Detalhes perdidos** | Resumir e perder o que importa | O resumo não substitui a tabela dos 14 | `[externo · UX: Lost details]` |
| 5 | **Achar que você é o cliente** | "Eu não clicaria nisso" | Preferências do consultor não entram; vale o público | `[externo · Marketing: Pride]` |
| 6 | **Falar para todo mundo** | Direção que serve para qualquer um | Definir quem é o público e quem fica de fora | `[externo · Marketing: Greed]` |
| 7 | **Copiar o concorrente** | "Faça como a marca X" | Usar a referência para ler itens, não para imitar | `[externo · Marketing: Sloth]` |
| 8 | **Reagir em vez de decidir** | Sugestão apressada após uma ação do concorrente | Voltar ao objetivo e ao público | `[externo · Marketing: Wrath]` |
| 9 | **Moda sem identidade** | Recomendar item/formato que não é da marca | Teste de apelo, perguntas 2 e 3 | `[externo · Marketing: Envy]` |
| 10 | **Encher a mensagem** | Recomendar 8 itens ao mesmo tempo | Itens sem limite, mas cada um precisa passar o teste de apelo e a peça continuar clara | `[externo · Marketing: Gluttony]` |
| 11 | **Apaixonar-se pela ferramenta** | Aplicar o Canvas onde outro problema pesa mais | Perguntar se o problema é produto, preço ou canal antes de itens | `[externo · Marketing: Lust]` |
| 12 | **Uso por vaidade da IA** | Entregar tabela bonita sem ligação ao objetivo | Todo achado liga-se ao objetivo declarado | `[externo · IA: Pride/Lust]` |
| 13 | **Isolar a decisão** | Fechar direção sem ouvir quem executa | Fazer handoff com perguntas abertas | `[externo · UX: Isolated ideation]` |

## Ligação com o anti-slop do projeto
O `CLAUDE.md` exige que todo texto passe pelo `/geral-anti-slop`. Os riscos 2, 3 e 12 são a versão do parecer: frases vagas, listas genéricas, certeza sem prova. Antes de entregar:
1. Rodar o parecer pelo `/geral-anti-slop` (`.agent/workflows/geral-anti-slop.md`).
2. Remover palavras de efeito sem conteúdo; cada frase deve ter dado, trecho ou decisão.

## A lição positiva (startups) `[externo · Parija]`
O texto de startups sugere partir de um impulso humano e construir em torno dele, o que é próximo da lógica do Canvas. É apenas um paralelo: **não** atribuir a Diamand.
