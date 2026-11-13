# Prompt: Instalar/Atualizar o acesso ao hub "SIP - Marketing" em outro projeto

Cole isto numa sessão do Claude Code dentro do projeto que precisa consultar o
hub central de marketing (SIP - Marketing). Instala sempre o resolver e, dos
agents e workflows do hub, só os que você escolher (o prompt mostra as tabelas e pergunta):

```
Instale/atualize o acesso ao hub central SIP - Marketing (marketing) neste projeto.
O que entra: o resolver sip-marketing sempre; agents e workflows do hub só os que eu
escolher; skills especialistas do hub nunca (o resolver as acha pela tabela e
as lê por caminho absoluto).
Padrão duplo: cada recurso instalado ganha um symlink absoluto em .agent/ (pro
hub) e um symlink relativo em .claude/ (pro symlink local em .agent/) — isso dá
acesso tanto ao Claude Code quanto a Google Antigravity/Gemini/Cursor, que leem
.agent/ direto e não dependem do stub global do 0 Padrões.

REGRA PARA TODO SYMLINK DESTE PROMPT: crie sempre com `ln -sfn <destino> <link>` (nunca
só com `-s`). `-f` recria um link velho/quebrado; `-n` impede que, se <link> já for um
symlink para uma pasta, o novo link seja criado DENTRO dessa pasta (poluiria o hub).
Antes de criar, confira <link> com `test -L` e `readlink`:
- não existe, ou é symlink: pode (re)criar;
- é arquivo ou pasta REAL (não symlink): NÃO rode `ln` (o `-f` apagaria o arquivo).
  Pare só aquele item e me pergunte, caso a caso: (a) renomear o meu arquivo
  (eu digo o novo nome; lembre que o `name:` do frontmatter dele também muda) e
  depois instalar o do hub; (b) substituir: mova o meu arquivo para
  `<link>.bak-AAAA-MM-DD` (nunca apague) e depois instale; (c) pular: não instale.
  Sem resposta = (c). Registre o desfecho na linha "Conflitos" do manifesto
  (passo 10); um item pulado entra em "Vistos no hub" e não em "Agents"/"Workflows",
  e só volta a ser oferecido se eu pedir para mudar a escolha.
REGRA PARA TODA REMOÇÃO DESTE PROMPT: só remova um <link> que seja symlink (`test -L`)
E cujo destino aponte para dentro de "/Users/macbookpro/Documents/IA Projects/_Plataforma/0 Mkt". Leia o destino com `readlink`
SEM `-f` (com `-f`, um link quebrado sai com erro no macOS): link de .agent/ tem o
caminho absoluto do hub; link relativo de .claude/ ou .cursor/ aponta para o link de
.agent/ de mesmo nome, então confira esse. Nunca remova arquivo ou pasta real.

1. Skill resolver (obrigatório):
   - Crie a pasta .agent/skills/ se ela não existir.
   - Crie (ou recrie) o symlink absoluto com `ln -sfn`:
     .agent/skills/sip-marketing -> "/Users/macbookpro/Documents/IA Projects/_Plataforma/0 Mkt/.agent/skills/sip-marketing"
   - Crie a pasta .claude/skills/ se ela não existir.
   - Crie o symlink relativo com `ln -sfn` (pro symlink acima, não direto pro hub):
     .claude/skills/sip-marketing -> ../../.agent/skills/sip-marketing

2. Migração (instalações antigas): remova, seguindo a regra de remoção, todo
   symlink em .agent/skills/ e .claude/skills/ que aponte para uma skill
   especialista do hub (qualquer uma que não seja sip-marketing), e a entrada dele
   no .gitignore. Skills especialistas não são mais instaladas.

3. Escolha de agents e workflows:
   - Leia as tabelas "Agents do hub" e "Workflows do hub" em
     "/Users/macbookpro/Documents/IA Projects/_Plataforma/0 Mkt/.agent/skills/sip-marketing/SKILL.md" (nome + "use quando").
   - Leia a entrada deste hub em .agent/SIPS-CONSUMIDOS.md, se existir:
     "Agents"/"Workflows" (escolhidos) e "Vistos no hub" (oferecidos antes).
   - Primeira instalação (sem entrada): mostre as duas tabelas e pergunte
     "Quais instalar? nenhum / todos / lista de nomes". Sem resposta = nenhum.
   - Instalação antiga sem entrada no manifesto, mas com symlinks deste hub já
     em .agent/agents/, .claude/agents/, .agent/workflows/ ou .claude/commands/:
     mostre as tabelas com esses itens já marcados e pergunte "manter esta
     escolha, mudar, ou nenhum?". Sem resposta = manter (nunca remova sem resposta).
   - Reinstalação: mantenha a escolha anterior sem perguntar de novo. Pergunte
     só sobre os itens das tabelas que NÃO estão em "Vistos no hub" (os novos).
     Sem resposta = os novos ficam de fora. Se eu pedir para mudar a escolha,
     mostre as tabelas inteiras com a escolha atual marcada.
   - Tabelas vazias: pule este passo e os passos 4 e 5 sem erro.

4. Instale só o escolhido (seguindo a regra de symlink acima):
   - Cada agent <nome>: .agent/agents/<nome>.md -> "/Users/macbookpro/Documents/IA Projects/_Plataforma/0 Mkt/.agent/agents/<nome>.md"
     (absoluto) e .claude/agents/<nome>.md -> ../../.agent/agents/<nome>.md (relativo).
   - Cada workflow <nome>: .agent/workflows/<nome>.md -> "/Users/macbookpro/Documents/IA Projects/_Plataforma/0 Mkt/.agent/workflows/<nome>.md"
     (absoluto), e .claude/commands/<nome>.md e .cursor/commands/<nome>.md ->
     ../../.agent/workflows/<nome>.md (relativos).
   - Crie as pastas que faltarem.

5. Remova o que saiu da escolha (seguindo a regra de remoção): symlinks de
   agents/workflows deste hub que não estão mais escolhidos, ou cujo arquivo
   sumiu do hub (link quebrado), e as entradas deles no .gitignore.

6. Confirme com `ls -la` cada symlink criado (os de .agent/ E os de .claude/)
   e que o .md correspondente é legível através de cada um. Depois, na raiz
   deste projeto, rode
   `python3 "/Users/macbookpro/Documents/IA Projects/_Plataforma/0 Padrões/.agent/scripts/sync_entrypoints.py" --check`:
   tem de sair com 0. Se acusar erro de link ou skill do hub, pare e relate
   (não apague links para "limpar" o aviso).
7. Não copie conteúdo de nenhum desses arquivos para este projeto — mantenha
   tudo como symlink, para herdar atualizações futuras do hub automaticamente.
8. Adicione ao .gitignore deste projeto (crie a seção se não existir) uma linha
   por symlink instalado, nunca um curinga do prefixo do domínio:
   .agent/skills/sip-marketing
   .claude/skills/sip-marketing
   (e, para cada agent/workflow instalado no passo 4, os caminhos
   .agent/agents/<nome>.md, .claude/agents/<nome>.md,
   .agent/workflows/<nome>.md, .claude/commands/<nome>.md,
   .cursor/commands/<nome>.md correspondentes)
   — são symlinks com path absoluto desta máquina, não portáveis entre clones.
9. Registre esta instalação no hub (bookkeeping, não é conteúdo de domínio —
   pode escrever direto, sem passar pelo inbox):
   - Veja o formato em "/Users/macbookpro/Documents/IA Projects/_Plataforma/0 Mkt/instalacoes/README.md".
   - Crie ou atualize "/Users/macbookpro/Documents/IA Projects/_Plataforma/0 Mkt/instalacoes/<nome-deste-projeto>.md" com:
     nome e caminho absoluto deste projeto, data de hoje, e os recursos
     instalados (skill sempre; agents/workflows escolhidos, ou "nenhum").
10. Atualize o manifesto local deste projeto, `.agent/SIPS-CONSUMIDOS.md`
   (crie se não existir — contrapartida local do registro do passo 9: lá o
   hub sabe quem consome; aqui o projeto sabe o que consome, sem precisar
   abrir .gitignore ou seguir symlink pra descobrir):
   - Formato de cada entrada (uma por SIP instalado neste projeto):
     ```markdown
     ## SIP - Marketing (`sip-marketing`)
     - Hub: /Users/macbookpro/Documents/IA Projects/_Plataforma/0 Mkt
     - Instalado/atualizado em: AAAA-MM-DD
     - Skill: sip-marketing
     - Agents: <escolhidos, ou "nenhum">
     - Workflows: <escolhidos, ou "nenhum">
     - Vistos no hub: agents <todos os nomes da tabela hoje>; workflows <idem>
     - Conflitos: <"nome: pulado" | "nome: meu arquivo renomeado para <novo>" | "nome: substituído (meu em <link>.bak-AAAA-MM-DD)", ou "nenhum">
     - Para atualizar: cole de novo "/Users/macbookpro/Documents/IA Projects/_Plataforma/0 Mkt/prompts/instalar-skill-sip-marketing.md"
     ```
   - "Vistos no hub" é o que permite, na próxima vez, perguntar só os novos.
   - Se o arquivo já tiver uma entrada pra este hub (de uma instalação
   anterior), substitua-a em vez de duplicar.
```

## Por que o padrão duplo (symlink de symlink) e não um só

A fonte de verdade de cada recurso fica no hub (`/Users/macbookpro/Documents/IA Projects/_Plataforma/0 Mkt/.agent/skills/`,
`.agent/agents/`, `.agent/workflows/`). O symlink absoluto em `.agent/` deste
projeto aponta direto pro hub; o symlink relativo em `.claude/` aponta pro
symlink local em `.agent/`, não direto pro hub. Essa cadeia de dois symlinks
(em vez de um só direto em `.claude/`) existe porque **Claude Code e as
outras IAs leem pastas diferentes**: Claude Code só descobre
`.claude/skills/`/`.claude/agents/`/`.claude/commands/`; Google
Antigravity/Gemini/Cursor só leem `.agent/skills/`/`.agent/agents/`/
`.agent/workflows/` direto (via Regra 4, 1ª prioridade: skills locais do
próprio projeto). Um symlink só em `.claude/` (direto pro hub) atende só o
Claude Code — pra essas outras IAs acharem o recurso neste projeto
específico, ele precisa também existir em `.agent/`. Atualizações futuras no
hub já refletem aqui automaticamente nos dois — exceto se um symlink quebrar
(hub movido ou arquivo renomeado), caso em que basta colar o prompt outra
vez, ou se o hub adicionar um agent/workflow novo depois da instalação, caso
em que rodar o prompt de novo pergunta só sobre os novos (a escolha anterior
fica registrada em `.agent/SIPS-CONSUMIDOS.md`, linha "Vistos no hub").

## Para outras IAs (Google Antigravity / Gemini / Cursor)

Com o padrão duplo acima, essas IAs já encontram o resolver e os
agents/workflows escolhidos **direto neste projeto** (via `.agent/skills/`,
`.agent/agents/`, `.agent/workflows/`), sem depender do stub global do
`0 Padrões` nem da Regra 4 (Fallback Resolution Protocol) — a 1ª prioridade
da Regra 4 já é "skills locais do próprio projeto", que é exatamente o que
os passos 1 e 4 criaram aqui. O que não foi escolhido elas acham pelas
tabelas do resolver e leem por caminho absoluto no hub. O stub global do `0 Padrões` continua existindo como rede de
segurança pra projetos que *não* instalaram (2ª prioridade da Regra 4), mas
quem instalou via este prompt não depende dele.

## Via de volta: contribuir com o hub

A skill instalada também sabe devolver conhecimento ao hub — nunca edita os
arquivos compartilhados direto, só deixa um arquivo em `/Users/macbookpro/Documents/IA Projects/_Plataforma/0 Mkt/inbox/`
para revisão manual. Ver `inbox/README.md` no hub para o formato esperado.

## Registro desta instalação no hub

Este prompt também registra quem instalou, em `/Users/macbookpro/Documents/IA Projects/_Plataforma/0 Mkt/instalacoes/`
(ver `instalacoes/README.md` no hub) — isto não é conteúdo de domínio, é
bookkeeping de quem consome o hub, então pode ser escrito direto, sem passar
pelo inbox. Serve pro dono do hub saber, quando mudar algo, quais projetos
revisar ou avisar — sem esse registro, ele teria que adivinhar ou perguntar
projeto por projeto.

## Manifesto local neste projeto

Este prompt também atualiza `.agent/SIPS-CONSUMIDOS.md` **neste projeto**
(contrapartida local do registro acima: lá o hub sabe quem o consome; aqui
o projeto sabe o que consome). Sem esse manifesto, a única forma de saber
que este projeto depende de um SIP é abrir o `.gitignore` ou seguir cada
symlink manualmente — o manifesto deixa isso visível de cara, num lugar só,
pra qualquer pessoa ou IA que abrir o projeto.
