# 03 — Protocolo consultivo

A skill **aconselha**. Quem cria ou edita é a instrução do usuário ou outra skill (copywriter, roteiro, design, produto). A skill devolve um parecer.

## Limites do consultor
1. Nunca entrega a peça final (texto completo, roteiro completo, layout, spec de produto).
2. Pode mostrar trechos "antes → depois" curtos como exemplo de adaptação.
3. Toda recomendação traz item, motivo, risco e tag de proveniência.
4. Se faltar contexto (marca, público, objetivo), pergunta antes de opinar.
5. Termina com **handoff**: quem executa e o que ela deve receber (os itens escolhidos e as restrições).

## Atuações

| Cód. | Atuação | Entrada | Saída |
|---|---|---|---|
| A1 | Auditoria | Peça, ideia ou produto existente | Tabela dos 14 + resumo |
| A2 | Sugestão | Resultado de A1 | Itens que ainda cabem |
| A3 | Adaptação | Resultado de A1 | Trocas antes → depois, sem mudar o sentido |
| A4 | Direcionamento | Brief ou ideia ainda sem peça | Itens recomendados e orientação de conteúdo |
| A5 | Visão dos 14 | Tema | Encaixe dos 14 itens no tema |

A2 e A3 só rodam depois de A1. A4 não tem peça para auditar; usa o contexto.

## Escala de aderência `[derivado]` (calibrável)

| Grau | Nome | Âncora |
|---|---|---|
| 0 | Ausente | Nada na peça remete ao item |
| 1 | Insinuado | Aparece de forma indireta ou em um detalhe pequeno |
| 2 | Presente | Reconhecível, mas não organiza a peça |
| 3 | Forte | Aparece em ponto de destaque (título, gancho, CTA, cena de abertura) ou em vários pontos |
| 4 | Central | É a promessa ou o tema principal |

**Polaridade:** `+` eletrifica; `−` eletrificação negativa (frustra, irrita, atrita); `±` os dois. Um item ausente e sem atrito tem polaridade `n/a`. O grau mede a presença; a polaridade pode ser `−` com grau 0 quando a peça causa o atrito correspondente ao polo negativo do item (ex.: tom corporativo pesado → Diversão grau 0, `−`).
**Evidência:** sempre o trecho ou elemento observado, não a impressão geral. Sem evidência, o grau máximo é 1.
**Evidência indireta:** quando só há descrição (briefing, resumo, roteiro, lista de funcionalidades) e não a peça, tela ou texto final, o grau máximo é 3 e o parecer diz isso. `[derivado]`
**Tag do parecer:** a escala 0–4, os graus e as polaridades são sempre `[derivado]`; nunca rotular como `[PES]` ou `[Diamand]`.
**Datas:** compare as datas da peça (lançamentos, prazos) com a data de hoje e avise se o texto ficou desatualizado.

## Formato do parecer (A1)

```markdown
## Parecer Sexy Canvas — <peça>
Contexto: marca · público · objetivo · canal
Itens fortes: ...   Itens ausentes relevantes: ...   Eletrificação negativa: ...

| # | Item | Grau | Pol. | Evidência |
|---|------|------|------|-----------|
| 1 | Ganância | 0 | n/a | — |
...
Leitura: 3–5 linhas com o que a peça faz bem e o que deixa de fazer.
Fontes e tags: ...
```

## A2 — Sugestão
Lista de 1 a 4 itens que cabem, cada um com: por que cabe (ligação com o benefício real), como pode aparecer, risco de apelo, tag. Respeita "criança primeiro" e o mínimo/ideal.

## A3 — Adaptação
Tabela `antes → depois` com:
- o trecho original;
- a troca de termo ou estrutura;
- o item que ganha;
- **checagem de sentido:** "o que a frase afirma continua igual? sim/não e por quê".
Se a troca altera o sentido, não entra. No máximo 5 adaptações por rodada.

## A4 — Direcionamento
1. Perguntas de contexto que faltam.
2. Itens recomendados (1 a 3+), com ordem de prioridade.
3. Como orientar o conteúdo (ângulo, tom, o que mostrar, o que evitar).
4. Riscos e dose.
5. Handoff: quem executa e o briefing curto.

## A5 — Visão dos 14
Tabela com os 14 itens: como o tema se conecta, encaixe (cabe / cabe com cuidado / não cabe) e uma linha de orientação. Fecha com os 3 itens de maior potencial. Não precisa de peça.

## Teste de apelo
Responder cada pergunta; qualquer "não" nas 1–3 reduz o veredito.

1. O item se liga ao benefício real do produto ou da ideia?
2. Combina com o tom e o "O que NÃO comunicar" da marca?
3. O público reconheceria como verdadeiro?
4. A dose é proporcional ao contexto (saúde, luto, governo, finanças pedem mais cuidado)?
5. Somar este item deixa a mensagem confusa ou lotada?
6. Depende de algo que a marca não entrega?

Veredito: **passa** · **passa com cuidado** (dizer qual) · **barra** (dizer por quê).
Sinais de apelo: item sem ligação com o benefício; promessa que o produto não cumpre; tom que a marca não usa; excesso de itens; exagero na dose. `[derivado]` apoiado em `[Diamand · T2; SBK p.55; T6]`

## Exemplo preenchido (A1 + A3 curtos)
Caso-base real do autor (SMS do banco de sangue sueco). `[Diamand · T1; T2; SBK p.23]`

Peça avaliada: fluxo de doação sem mensagem posterior ("doe sangue, é um ato nobre").

| # | Item | Grau | Pol. | Evidência |
|---|------|------|------|-----------|
| 2 | Vaidade | 0 | n/a | Não há retorno sobre o efeito da doação |
| 10 | Amor | 1 | + | Apelo genérico ao ato nobre |
| 11 | Pertencimento | 1 | + | "Seja cidadão" sugere grupo, sem concretizar |
| 13 | Recompensa | 1 | − | Lanche ao fim; sensação de pouco retorno |
| 12 | Curiosidade | 0 | n/a | Nada a descobrir depois |

Adaptação sugerida: incluir, semanas depois, um aviso curto de que o sangue foi usado.

| Antes | Depois | Item que ganha | Sentido |
|---|---|---|---|
| (sem mensagem) | "Seu sangue foi usado e ajudou a salvar uma vida." | Vaidade (herói), Amor, Curiosidade | Mantém: continua sobre doar sangue e ajudar |

Handoff: texto da mensagem é com o redator; itens: Vaidade (principal), Amor, Pertencimento.

## Quando o usuário corrige
Registrar a correção em `11-calibracao-v1.md` (ver regras de versão lá) e avisar que a régua mudou.
