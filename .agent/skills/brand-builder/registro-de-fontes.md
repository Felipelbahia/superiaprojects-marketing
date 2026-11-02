# Registro de fontes de dados (número só com fonte)

**Versão 1.1 (2026-10-23).** Esta é a **referência principal**, vive no 0 Mkt. Projetos têm cópia de uso do registro (o arquivo de dados), nunca uma cópia desta regra. **Quando este arquivo mudar, atualizar os projetos listados em "Projetos que usam" (abaixo)** e subir a versão.

Origem: pedido do usuário no projeto Futuro Mercado (2026-10-23): a skill deve dizer, **em linguagem simples**, o que é o arquivo de registro de dados, avisar quando ele será **criado** (projeto novo) ou **montado a partir do que já existe** (projeto existente), e ensinar como **preencher e atualizar**.

## O que é, em uma frase para o usuário
É uma tabela onde cada número que a marca pode citar em uma peça aparece **uma vez**, com a fonte, a data e o cuidado de uso. Se o número não está lá, não vai para peça. Serve para evitar estatística inventada e para qualquer pessoa (ou agente) conferir de onde veio.

## Dois tipos de dado (decisão do usuário, 2026-10-23)
O registro separa **dado de referência de terceiros** (pesquisa online, relatório de mercado: serve de base, **não é resultado da marca**) de **dado próprio** (resultado real da marca ou de cliente, com permissão). Regras: dado de referência cita-se sempre "segundo <fonte>" e **nunca** como prova, resultado ou prova social da marca; dado próprio só entra com origem e autorização, e fica em tabela ou seção separada. Todo registro novo começa com esta nota no topo, e o usuário é avisado de que os números do registro não são dele.

## Quando entra
Sempre que a marca tiver regra de "número sem fonte não entra" (vem de "O que NÃO comunicar", etapa 4) ou quando o uso A (conteúdo), B (demanda) ou C (imprensa) citar dados.

## Passo 0: procurar antes de criar
No projeto da marca, procurar por arquivos de dados e fontes (nomes como `acervo_dados_metricas`, `registro de dados`, `fontes`, `banco de cases`, `estudos`; pastas de inteligência ou pesquisa). **Se existe, usar como está.** Não criar um segundo registro.

## Projeto novo (nada existe)
1. Avisar o usuário: "este projeto ainda não tem registro de dados; vou criar `acervo_dados_metricas.md` na pasta de pesquisa ou inteligência do projeto (se não houver, na raiz do projeto de conteúdo), vazio, com este modelo".
2. Criar com o modelo abaixo e explicar **como preencher** (um número por linha) e **quando atualizar**.
3. Perguntar se já existem números em uso (site, apresentações, posts) para cadastrar agora; cada um entra com o status que o usuário disser (`verificado`, `autorizado sem fonte` ou `a verificar`), **sem inventar fonte**.

## Projeto existente (já tem conteúdo ou dados)
0. **Nome e local:** usar os que o projeto já tem. Se não há registro, criar `acervo_dados_metricas.md` na pasta de pesquisa ou inteligência do projeto (ou na raiz do projeto de conteúdo, se não houver) e dizer ao usuário onde ficou.
1. Mostrar ao usuário o que foi encontrado e dizer em uma frase como o arquivo é usado.
2. Se não existir registro, **pedir as informações para montá-lo**: números que já aparecem em peças ou no site, onde saíram, quem autorizou. Montar com o modelo, uma linha por número, e marcar `a verificar` o que o usuário não souber de onde veio.
3. Perguntar se quer varrer o conteúdo já publicado em busca de números sem fonte (opcional, nunca alterar peça aprovada sem pedido).
4. Informar **como atualizar** (abaixo).

## Modelo (colunas)
| Tipo (`referência de terceiros` / `dado próprio`) | Métrica ou dado | O que significa (em uma frase) | Fonte primária (nome) | URL | Data da fonte | Amostra ou contexto | Ressalvas e cuidados | Status (`verificado` / `fonte secundária` / `autorizado sem fonte` / `a verificar`) | Onde já foi usado |
|---|---|---|---|---|---|---|---|---|---|

## Como preencher
- Um número por linha, **copiado da fonte**, com a unidade e o recorte (quem, onde, quando).
- Dado de auto-relato de empresa: escrever "segundo a empresa" no campo de ressalvas.
- Estatística que o usuário já usava sem fonte: status `autorizado sem fonte`, com a data da autorização e a tarefa de achar a fonte. Não apresentar como verificado.

## Como atualizar
- Quando entrar peça com número novo, **cadastrar antes de publicar**.
- Revisar o status e a data de fonte na revisão periódica da marca (trimestral, se o projeto tiver esse ritmo); fonte velha ou link quebrado vira `a verificar`.
- Quem confere peça nova (revisor de voz) usa este arquivo para aprovar ou barrar número.

## Ao atualizar este arquivo (propagação)
1. Subir a versão no topo e anotar o que mudou.
2. Para cada projeto da lista abaixo: abrir o registro dele, **ajustar o cabeçalho e as colunas ao modelo novo sem apagar linhas**, anotar a versão do modelo no topo e registrar a mudança no log do projeto.
3. Se um projeto não puder ser atualizado agora, marcar "desatualizado (versão X)" na lista.

## Projetos que usam (atualizar a cada mudança)
| Projeto | Registro | Versão do modelo aplicada |
|---|---|---|
| Futuro Mercado (Marketing - FM) | `inteligencia/3_estudos_embasamento/acervo_dados_metricas.md` | cabeçalho aplicado em 2026-10-23; colunas atuais anteriores ao modelo 1.1 (sem coluna Tipo; todos os itens são referência de terceiros) |
