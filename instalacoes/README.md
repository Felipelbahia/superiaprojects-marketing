# Instalações — quem consome este hub

Registro de todo projeto que instalou acesso a este hub (skill `sip-marketing`) via `prompts/instalar-skill-sip-marketing.md`. Diferente do `inbox/`: isto não é conteúdo pendente de revisão, é bookkeeping. Por isso o prompt de instalação escreve aqui direto, sem curadoria.

**Por que existe:** quando algo muda neste hub (o resolver, uma skill, um agent, um workflow ou a estrutura), esta pasta mostra quais projetos consomem o hub, sem ter que perguntar um por um. Serve também para decidir se vale avisar alguém antes de uma mudança que quebra compatibilidade.

**Fora do git deste hub** (ver `.gitignore`: `instalacoes/*`, menos este README): cada entrada tem caminho absoluto de outro projeto na máquina do dono; não é portável entre máquinas nem é conhecimento que valha versionar.

## Formato de cada arquivo (`<nome-do-projeto>.md`)

```markdown
## Projeto
<nome do projeto>

## Caminho absoluto
<path completo do projeto consumidor>

## Instalado em
AAAA-MM-DD

## Última atualização
AAAA-MM-DD (atualize sempre que o prompt for colado de novo nesse projeto)

## Recursos instalados
- Skill: sip-marketing (redirecionador)
- Agents: nenhum (lidos no hub por caminho absoluto)
- Workflows: nenhum (lidos no hub por caminho absoluto)
```

## Manutenção

Cada vez que o prompt de instalação for colado num projeto (instalação nova ou atualização), o próprio prompt cria ou atualiza o arquivo correspondente aqui. Se um projeto parar de usar o hub, apague o arquivo dele.
