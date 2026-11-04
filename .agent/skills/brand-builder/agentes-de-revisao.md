# Agentes de revisão da marca (criados na etapa 8 ou 9)

Origem: pedido do usuário no projeto Futuro Mercado (2026-10-23): "crie [os agentes de revisão] com o nome da marca, ex.: `brand-guardiao-de-voz-Futuro-Mercado`; a skill que vai criar tem que personalizar na hora da criação".

## O que são
Revisores que conferem peça nova contra o kit **daquela marca**. Existem dois, e um não faz o trabalho do outro:

| Agente | Nome | Revisa | Lê |
|---|---|---|---|
| Voz e conteúdo | `brand-guardiao-de-voz-<Marca>` | Texto: voz, "o que NÃO comunicar", fontes de número, metadados, séries, regras de conteúdo | `brand-voice*.md`, `ativacao/conteudo.md`, pilares, personas, mensagens, posicionamento, `STANDARDS.md` |
| Identidade e kit | `brand-identity-guardian-<Marca>` | Visual e arquivo: cor, fonte, logo, imagem, proporção, contraste, política de imagem e de IA | `identidade-e-ativos.md`, `registro-de-decisoes.md`, `tokens.json`, `visual-style.md`, direção visual, logo e modelos |

Quem cria a peça é outro agente ou o usuário; o revisor **entrega parecer com evidência e não escreve a peça**.

## Quando criar
No fim da etapa 8 (as regras de conteúdo já existem) ou na etapa 9, **perguntando antes ao usuário** (regra 10 da skill): objetivo (conferir peça nova contra o kit antes de aprovar), opcional, recomendação (criar quando a produção é feita por agentes de IA) e custo (um arquivo por agente, mais teste). Pré-requisitos: voz aprovada (etapa 4); para o agente de identidade, também `identidade-e-ativos.md` ou, no mínimo, `tokens.json` e direção visual.

## Nome
`<função>-<Marca>`, com a marca escrita como o usuário escreve e espaços trocados por hífen: `brand-guardiao-de-voz-Futuro-Mercado`, `brand-identity-guardian-Futuro-Mercado`. O campo `name` do arquivo é igual ao nome do arquivo.

## Onde ficam (regra do projeto)
Arquivo em `.agent/agents/<nome>.md` do projeto da marca, com link simbólico em `.claude/agents/<nome>.md` (`ln -s "../../.agent/agents/<nome>.md" ".claude/agents/<nome>.md"`), como o 0 Mkt faz com os agentes. Se o projeto tem registro de agentes ou ficha central, registrar lá. Agente de marca vive **no projeto da marca**, não na pasta global.

## Antes de escrever: ativar `writing-skills` (regra 12 do `SKILL.md`)
Carregar a skill `writing-skills` e seguir o checklist dela para o arquivo do agente: `name` só com letras, números e hífen; **`description` em inglês começando com "Use when..." (padrão do `writing-skills`), em terceira pessoa, só com a condição de uso (nunca resumir o processo), sem exemplos de acionamento, e o frontmatter inteiro até 1024 caracteres** (o corpo do agente fica em português). **O limite de 1024 é referência, não obrigação** `[usuário, 2026-10-23]`: se o conteúdo estourar, decidir entre **reduzir** ou **mover o excesso para uma pasta `references/`** e fazer o agente (ou a skill) guiar o processo por essas referências; visão geral com o princípio; tabela de racionalizações comuns do revisor ("é só um post", "está quase bom"); teste com cenário de pressão antes de entregar (passo 8 abaixo).

## Como personalizar na hora da criação (procedimento)
O agente **referencia os arquivos da marca pelo caminho** (para ficar atualizado) **e** carrega um bloco "Personalização desta marca" **preenchido na criação**, para funcionar mesmo se um arquivo faltar. Passos:
1. **Ler** os arquivos de entrada da tabela acima, por trecho.
2. **Preencher o bloco de personalização** com fatos da marca, cada um copiado de arquivo aprovado (nunca inventado):
   - Voz: nome da marca, descritor, frase da marca (e a diferença entre as duas), traços de voz, itens de "O que NÃO comunicar", regras acrescentadas, séries, canais e frequência, formato dos metadados.
   - Identidade: cores com hex e papéis, versões do logo, respiro e mínimos, fontes e regra por tamanho, política de imagem e de IA, proporções, dados de contato oficiais, o que é provisório, o que o `registro-de-decisoes.md` declara como exceção.
3. **Restringir as ferramentas** (`tools:` no frontmatter): revisor só lê. Voz: `Read, Glob, Grep`. Identidade: `Read, Glob, Grep, Bash` (Bash só para conta, como contraste). Revisor não escreve peça nem arquivo da marca.
4. **Definir o parecer** (formato fixo): veredito (aprovar, ajustar, reprovar), tabela de achados com evidência e regra violada, linhas corrigidas (só as com problema), o que passou, próximo passo, perguntas em aberto.
5. **Declarar limites:** não inventa fato, dado, caso nem medida de plataforma; não cria a peça; lacuna de regra é declarada, não preenchida.
6. **Descrição (frontmatter):** conforme o bloco "Antes de escrever" acima (inglês, "Use when...", sem exemplos), com a marca no nome do agente.
7. **Registrar**: no log da etapa, no `registro-de-decisoes.md` (agente criado, data, versão) e na ficha central do projeto.
8. **Testar** antes de entregar: agente recém-criado **não aparece como tipo de agente na sessão em que foi criado**. Teste, então, com um subagente genérico que receba o texto do arquivo do agente como instrução, em uma peça aprovada e em uma peça com defeito conhecido; se não reprovar o defeito, ajustar. **Teste também uma peça limpa** (só frases aprovadas): se o agente inventar achado ou bloquear por gosto, calibrar (falso positivo). Se não houver peça de teste ou subagente, dizer ao usuário **que não foi testado** e que o teste real exige uma nova sessão.

## Calibração do revisor (aprendida no teste da Futuro Mercado)
Todo agente de revisão leva um bloco "Calibração": bloqueio só com regra escrita citada (arquivo e item); gosto vira observação; marcadores aprovados da marca (por exemplo, dado ilustrativo com "exemplo") e o vocabulário aprovado não são achado; peça limpa recebe APROVAR sem achado inventado; número vindo de fonte de terceiros nunca é apresentado como resultado da marca.

## Manutenção
O agente tem `version` no frontmatter. Quando um arquivo-fonte muda (nova voz, novo kit, exceção nova), **atualizar o bloco de personalização** e subir a versão; o bloco é um retrato do momento da criação, e os arquivos continuam sendo a verdade.

## Modelo de agente de voz (esqueleto; substituir `{{...}}`)
```
---
name: brand-guardiao-de-voz-{{Marca}}
version: "1.0.0"
brand: {{Marca}}
description: "Revisor de voz e conteúdo da marca {{Marca}}. Use antes de uma peça entrar na esteira de aprovação ou quando o usuário pedir para conferir se um texto soa como a {{Marca}}. ... não escreve a peça. Exemplos: <example>...</example>"
model: sonnet
skills: brand-voice-messaging, geral-anti-slop
---
Você é o revisor de voz e de conteúdo da {{Marca}} ({{descritor}}; frase: "{{frase}}"). Você revisa; não escreve a peça.
## Carregar contexto  -> lista de caminhos reais da marca
## Personalização desta marca (gerada na criação)  -> traços, nunca comunicar, regras novas, séries, canais, descritor x frase
## Como revisar  -> metadados, voz, "nunca comunicar", número e prova, série e pilar, gancho e chamada, anti-slop, revisão externa
## Parecer (formato fixo)  ## Limites
```
Os agentes `brand-guardiao-de-voz-Futuro-Mercado` e `brand-identity-guardian-Futuro-Mercado` (em `Projetos/Futuro Mercado/Marketing - FM/.agent/agents/`) são os exemplos prontos; usar como referência de estrutura e de profundidade, nunca copiar o conteúdo de uma marca para outra.
