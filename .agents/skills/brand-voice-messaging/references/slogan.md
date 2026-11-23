# Assinatura da marca (slogan)

Passo "6c" da etapa 4 do `brand-builder`, **opcional**. A casa de mensagens (6b) diz o que a marca promete. O slogan é, no máximo, uma frase curta que acompanha o nome e carrega um pedaço dessa promessa. Muitas marcas ficam melhores sem ele.

*Ideia adaptada da skill `slogan` do Brandfy (Promovaweb, AGPL-3.0); texto reescrito para o fluxo do 0 Mkt.*

## Antes de começar

1. **Perguntar se o usuário quer este passo** (regra 10 do `brand-builder`). A pergunta traz: o objetivo ("uma frase curta ao lado do nome, que lembra o que a marca faz ou promete"), que é **opcional**, minha recomendação e o custo (duas rodadas de conversa). Registrar a resposta no log da etapa.
2. **Perguntar se ele quer responder ou delegar** (regra 17). Se delegar, o que eu propus fica `[derivado]` e vai para as lacunas.
3. Ler `mensagens.md` (promessa aprovada e "Limites"), `brand-voice.md` ("O que NÃO comunicar") e o nome. Sem promessa aprovada, **não escrever slogan**: voltar à casa de mensagens.

## Quando recomendar "sem slogan"

Recomendar a ausência, com o motivo escrito, quando:

- o nome já diz a categoria e a promessa;
- a promessa ainda não foi aprovada;
- as opções só ficam de pé com clichê, superlativo ou garantia que a marca não prova;
- o posicionamento deve mudar nos próximos meses (a frase envelheceria rápido).

"Sem slogan" é uma resposta completa. Entra no brandbook como decisão, não como lacuna.

## 1. Escolher a função (uma só)

| Função | A frase serve para | Vida esperada |
|---|---|---|
| Esclarecer a categoria | dizer em palavras simples o que a marca é, quando o nome não diz | longa |
| Condensar a promessa | resumir o nível 1 da casa de mensagens | longa |
| Criar memória | ficar na cabeça por ritmo e imagem, sem mentir | longa |
| Marcar uma campanha | acompanhar uma ação com data | curta: **não é assinatura da marca** |

Frase de campanha não entra como slogan. Vai para o plano da campanha.

## 2. Matéria-prima

Só o que já foi aprovado: promessa (nível 1), a dor da persona, traços de voz, "O que NÃO comunicar" e o nome. Nenhum dado novo. Número ou resultado na frase só com fonte (`registro-de-fontes.md`).

## 3. Gerar

Três ou quatro famílias de ângulo, duas ou três frases em cada:

- o que a pessoa ganha;
- o que a marca recusa fazer;
- a categoria em palavras do dia a dia;
- a ação que a marca facilita.

Poucas palavras. Se a frase precisa de vírgula ou de explicação para fazer sentido, é frase de campanha. Não rimar por obrigação.

## 4. Filtro de corte (antes dos testes)

Cortar toda opção que:

- usa clichê, superlativo ("o melhor", "líder", "número 1") ou garantia sem prova;
- carrega jargão que o público não usa;
- passa no **teste de troca**: trocar o nome pelo de um concorrente e a frase continua verdadeira;
- afirma algo que o "O que NÃO comunicar" proíbe;
- promete mais do que a marca consegue mostrar hoje.

## 5. Testes (cada finalista passa por todos)

| Teste | Como fazer | Passa quando |
|---|---|---|
| Entendimento | Mostrar a frase sem contexto a três pessoas do público e perguntar o que a marca faz | pelo menos duas acertam a categoria |
| Verdade | Ligar a frase à promessa aprovada e a uma prova | existe prova ou "a conseguir" declarado |
| Distinção | Teste de troca (seção 4) | a frase deixa de servir ao concorrente |
| Som | Ler em voz alta e ditar por telefone | quem ouve escreve igual |
| Com o nome | Ler nome mais frase e a frase sozinha | não repete o nome e funciona sem ele |
| Tamanho | Aplicar em avatar, cabeçalho, anúncio e assinatura de e-mail | cabe sem quebrar mal |
| Sentidos indesejados | Procurar duplo sentido, gíria, leitura negativa e, se a marca opera em outro idioma, a tradução | nenhum achado |
| Vida útil | Perguntar se continuará verdadeira em dois anos | sim; senão é frase de campanha |

O número de três pessoas no teste de entendimento é uma proposta de método, não um padrão provado: serve para pegar mal-entendido, não para medir.

## 6. Mostrar e aprovar

Mostrar até três finalistas **e a opção "sem slogan"**, cada uma com o resultado dos testes, minha recomendação e o custo de trocar depois (peças já impressas). Rodar `/geral-anti-slop` no texto antes. O usuário escolhe; nada é aprovado no mesmo turno em que o modelo propôs tudo sem ele ver.

## 7. Registro

Em `mensagens.md`, seção **"Assinatura (slogan)"**:

- versão principal (ou "sem slogan" e o motivo);
- até duas alternativas, só para campanha;
- usos proibidos (por exemplo, não substituir o nome, não aparecer em contexto de crise);
- resultado dos testes;
- histórico das opções descartadas, com o porquê.

Trocar um slogan aprovado exige registrar o motivo e gerar `mensagens-v2.md` (não editar a versão antiga). Se `mensagens.md` ainda não está no `versoes.json`, registrar os dois (v2 vigente, a antiga no histórico) e rodar `brand_html.py sync` para o HTML gêmeo. Peça de marketing que traga slogan usa **a frase registrada aqui**, sem inventar outra na hora.

## Erros comuns

| Erro | Correção |
|---|---|
| Escrever slogan antes da promessa aprovada | Voltar ao passo 6b |
| Oferecer só opções, nunca "sem slogan" | "Sem slogan" entra sempre na lista de decisão |
| Frase bonita que amplia a promessa | Cortar: verdade vence memória |
| Escolher pelo gosto de quem escreveu | Cada finalista passa pelos oito testes, com a tabela à vista |
| Tratar frase de campanha como assinatura | Mover para o plano da campanha |
