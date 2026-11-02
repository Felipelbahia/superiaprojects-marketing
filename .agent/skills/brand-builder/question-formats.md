# Formatos de pergunta

Misture formatos dentro de uma etapa. Cansaço de questionário é o principal motivo de resposta rasa.

## Regras de rodada

- 3 a 5 perguntas por rodada no chat. Etapa longa pode ter várias rodadas.
- Antes de perguntar, ler os arquivos da marca. Nunca perguntar o que já está escrito; confirmar ("li que X, continua valendo?").
- Toda pergunta de múltipla escolha leva a saída "nenhuma, é isto: ___".
- Fechar cada rodada com síntese em 3 a 5 linhas e pedir correção antes de seguir.
- Marcar a resposta com a tag de proveniência `[usuário]` e guardar a resposta bruta em `_respostas/`.

## 1. Escala (1 a 5)

Para traços de voz, personalidade, posicionamento visual. Sempre um polo contra o outro, nunca "quanto você gosta de X".

```
Sério 1 - 2 - 3 - 4 - 5 Brincalhão
Técnico 1 - 2 - 3 - 4 - 5 Coloquial
Premium 1 - 2 - 3 - 4 - 5 Acessível
Provocador 1 - 2 - 3 - 4 - 5 Acolhedor
```

Tratar 3 como "não sei" e perguntar de que lado pende em um exemplo concreto.

## 2. A ou B forçado

Para destravar quem responde "depende". Dois polos concretos, com marcas ou cenas reais, não adjetivos.

> A conversa é mais ______ ou mais ______?

Depois de 4 a 6 pares, mostrar o padrão que apareceu e pedir confirmação.

## 3. ABCDE

Para escolher entre 4 a 5 caminhos nomeados, cada um com uma linha de efeito prático. Sempre com recomendação marcada.

```
Qual território a marca ocupa?
A. Especialista que simplifica   (autoridade, didática)
B. Rebelde que questiona         (tensão, opinião forte)
C. Parceiro que acompanha        (proximidade, cuidado)
D. Curador que filtra            (gosto, seleção)
E. Nenhum, é isto: ___
Recomendo A porque ...
```

## 4. Escalonamento de intensidade

Para calibrar o quanto: apresentar a mesma mensagem em 3 a 5 intensidades e o usuário aponta a certa.

> 1 neutra, 2 calorosa, 3 bem-humorada, 4 irônica, 5 ácida. Qual é a nossa? Qual é o limite que não passamos?

## 5. Reação a referências

Eu trago 5 a 8 exemplos (marcas, perfis, anúncios, estilos visuais, frases). O usuário reage a cada um: **amo / aceito / evito / nunca**, com uma linha do porquê. Eu extraio o padrão.

Regras: variar propositalmente os exemplos (incluir 2 que eu espero que ele rejeite); só citar marcas e peças que eu realmente conheço; se não tenho certeza de um detalhe, dizer. Quando houver acesso à web, buscar e confirmar antes de citar.

## 6. Completar a frase

Para extrair vocabulário e crenças sem induzir.

> "A maioria das marcas de [categoria] erra quando ..."
> "Nosso cliente vai embora quando ..."
> "Se a marca sumisse amanhã, o que faltaria é ..."

## 7. Situação real

Para personas e voz: "conte a última vez que alguém [fez a compra / reclamou / elogiou]". Pede cena, não opinião.

## 8. Aberta em documento

Só para essência e posicionamento. A skill gera um `.md` em `_respostas/` com as perguntas numeradas e espaço de resposta; o usuário preenche com calma e avisa. Cada pergunta traz um exemplo curto de resposta boa e outro de resposta rasa.

## Qual formato em qual etapa

| Etapa | Principal | Apoio |
|---|---|---|
| Intake | ABCDE | situação real |
| Essência | aberta em documento, completar a frase | A/B |
| Posicionamento | ABCDE, A/B | reação a referências |
| Público | situação real | escala |
| Voz | escala, intensidade | reação a referências, A/B |
| Desejo | escala 1-5 | ABCDE |
| Direção visual | reação a referências | A/B, escala |

## Pergunta de abertura de etapa (obrigatória, qualquer profundidade)
Antes das perguntas da etapa: "Quer responder as perguntas desta etapa, ou prefere que eu proponha e você aprova? Recomendo <A ou B> porque <motivo curto>. A. Eu pergunto (3 a 5 perguntas)  B. Você propõe e eu aprovo  C. Proponha daqui em diante, e eu só aprovo." Exemplo de resposta: "B." Registrar a escolha em `_respostas/respostas-do-usuario/`. Em B e C, tudo o que foi proposto vai `[derivado]`.
