# Prompt: Instalar/Atualizar o acesso ao hub "SIP - Marketing" em outro projeto

Cole isto numa sessão do Claude Code dentro do projeto que precisa consultar o hub central de marketing (SIP - Marketing, pasta `0 Mkt`). O SIP é um **redirecionador**: instala-se **somente o resolver `sip-marketing`**. Skills, agents e workflows ficam no hub e são lidos **por caminho absoluto**. Não são symlinkados nem copiados para o projeto. Criar uma skill, agent ou workflow novo no hub não exige reinstalar nada.

```
Instale/atualize o acesso ao hub central SIP - Marketing (marketing) neste projeto.
Padrão duplo: o resolver ganha um symlink absoluto em .agent/ (pro hub) e um
symlink relativo em .claude/ (pro symlink local em .agent/). Isso dá acesso
tanto ao Claude Code quanto a Google Antigravity/Gemini/Cursor.

REGRA PARA TODO SYMLINK DESTE PROMPT: crie sempre com `ln -sfn <destino> <link>` (nunca
só com `-s`). `-f` recria um link velho/quebrado; `-n` impede que, se <link> já for um
symlink para uma pasta, o novo link seja criado DENTRO dessa pasta (o que poluiria o hub).
Antes de recriar, confira com `readlink` e, se <link> for uma pasta REAL, não toque nela.

PRÉ-VERIFICAÇÃO (faça ANTES de qualquer passo numerado): confira `.agent/skills/sip-marketing`
deste projeto. Se for uma PASTA REAL (não um symlink), PARE AGORA: não execute NENHUM dos
passos abaixo, não crie, mova nem apague nada, e avise o usuário que essa pasta precisa ser
movida ou removida por ele antes de instalar o resolver.

1. Skill resolver (o ÚNICO recurso a instalar):
   - Crie a pasta .agent/skills/ se ela não existir.
   - Crie (ou recrie, se estiver desatualizado/quebrado) o symlink absoluto com `ln -sfn`:
     .agent/skills/sip-marketing -> "/Users/macbookpro/Documents/IA Projects/_Plataforma/0 Mkt/.agent/skills/sip-marketing"
   - Crie a pasta .claude/skills/ se ela não existir.
   - Crie o symlink relativo com `ln -sfn` (pro symlink acima, não direto pro hub):
     .claude/skills/sip-marketing -> ../../.agent/skills/sip-marketing

2. Não instale agents, workflows nem skills especialistas do hub. O hub tem dezenas
   de cada; o resolver manda ler cada um por caminho absoluto.

3. Confirme com `ls -la` os dois symlinks e que o SKILL.md do resolver é legível
   através de cada um. Depois, na raiz
   deste projeto, rode
   `python3 "/Users/macbookpro/Documents/IA Projects/_Plataforma/0 Padrões/.agent/scripts/sync_entrypoints.py" --check`:
   tem de sair com 0. Se acusar erro de link ou skill do hub, pare e relate
   (não apague links para "limpar" o aviso).

4. Ajuste o .gitignore deste projeto (crie a seção se não existir) com estas duas
   linhas (symlinks com path absoluto desta máquina, não portáveis entre clones):
   .agent/skills/sip-marketing
   .claude/skills/sip-marketing

5. Registre esta instalação no hub (bookkeeping, pode escrever direto):
   - Veja o formato em "/Users/macbookpro/Documents/IA Projects/_Plataforma/0 Mkt/instalacoes/README.md".
   - Crie ou atualize "/Users/macbookpro/Documents/IA Projects/_Plataforma/0 Mkt/instalacoes/<nome-deste-projeto>.md"
     com nome e caminho absoluto deste projeto, data de hoje e o recurso instalado
     (resolver `sip-marketing`).

6. Atualize o manifesto local deste projeto, `.agent/SIPS-CONSUMIDOS.md` (crie se não
   existir). Uma entrada por SIP; se já existir uma para este hub, substitua em vez de
   duplicar:
   ## SIP - Marketing (`sip-marketing`)
   - Hub: /Users/macbookpro/Documents/IA Projects/_Plataforma/0 Mkt
   - Instalado/atualizado em: AAAA-MM-DD
   - Skill: sip-marketing (redirecionador; skills, agents e workflows são lidos por caminho absoluto, não instalados)
   - Agents: nenhum (lidos no hub)
   - Workflows: nenhum (lidos no hub)
   - Para atualizar: cole de novo "/Users/macbookpro/Documents/IA Projects/_Plataforma/0 Mkt/prompts/instalar-skill-sip-marketing.md"

7. Se este projeto produz peças de marca e ainda não tem `docs/mapa-de-destinos.md`,
   avise o usuário: as skills do hub gravam conforme o mapa do projeto consumidor
   (ver skill `mapa-de-destinos` no kit). Não crie o mapa sem ele pedir.
```

## Por que o padrão duplo e por que só o resolver

A fonte de verdade fica no hub. O symlink absoluto em `.agent/` aponta direto pro hub; o relativo em `.claude/` aponta pro symlink local em `.agent/`. Claude Code só descobre `.claude/`; Antigravity/Gemini/Cursor só leem `.agent/`. Só o **resolver** precisa ser descoberto por nome no projeto consumidor: ele traz a tabela gerada das skills e manda ler cada skill, agent ou workflow por caminho absoluto. Symlinkar as ~100 skills, ~30 agents e ~110 workflows em cada projeto obrigaria a reinstalar a cada novidade e poluiria o `.gitignore`.

## Via de volta: contribuir com o hub

A skill instalada devolve conhecimento ao hub sem editar arquivos compartilhados: deixa um arquivo em `/Users/macbookpro/Documents/IA Projects/_Plataforma/0 Mkt/inbox/` para revisão manual (formato em `inbox/README.md`).

## Registro e manifesto

Este prompt registra quem instalou em `/Users/macbookpro/Documents/IA Projects/_Plataforma/0 Mkt/instalacoes/` e mantém `.agent/SIPS-CONSUMIDOS.md` no projeto. Assim o hub sabe quem o consome, e o projeto sabe o que consome.
