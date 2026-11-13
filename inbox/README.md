# Inbox — contribuições de outros projetos

Porta de entrada para qualquer projeto que, usando a skill `sip-marketing`, tenha
aprendido algo sobre marketing e queira devolver ao hub: um insight, um exemplo
novo, ou uma melhoria numa skill existente.

**Ninguém edita `.agent/skills/` (ou pastas de exemplos/workflows) direto a
partir de outro projeto.** O conteúdo cai aqui primeiro e é promovido
manualmente para o lugar certo durante uma revisão do hub. Qualquer skill do hub
é compartilhada por symlink com todos os projetos que a instalaram: um ajuste
sem curadoria quebra todo mundo ao mesmo tempo. Os itens desta pasta ficam fora
do git do hub (só este README é versionado).

Contribuições podem ser sobre skill, agent ou workflow do hub. **Não traga conteúdo de marca de cliente** (voz, personas, dados): só o aprendizado genérico. Os itens podem citar projetos e contextos de clientes; por isso ficam fora do git.

**Itens anteriores a 2026-11-11** usam o formato antigo (`AAAA-MM-DD_<projeto>_<assunto>.md`, seções Tipo/Contexto/Proposta) e continuam válidos; não renomeie. Itens novos seguem o formato abaixo.

## Como contribuir

1. Crie `inbox/NNN-<assunto-curto>.md`, com `NNN` = próximo número livre desta
   pasta (contando `arquivo/`). Duas sessões podem usar o mesmo número ao mesmo
   tempo: tudo bem, o assunto diferencia. Nunca renumere arquivos existentes.
2. Escreva para uma IA que nunca viu a sua conversa: caminhos absolutos,
   frases literais como âncora (números de linha mudam), evidência.
3. Formato:
   ```markdown
   # NNN — <título>
   Status: na inbox · Aberto em: AAAA-MM-DD · Pedido por: <quem> · Projeto de origem: <nome e caminho>

   ## O quê
   ## Como (o que fazer quando for pedido)
   ## Onde (arquivos, skills, pastas do hub)
   ## Por quê (o que depende disto; evidência)
   ## Para quê (critério de sucesso)
   ## Quem (decide / aplica / afetados)
   ## Efeitos e impactos (o que muda, o que acontece se nada for feito)
   ## Exemplos
   ## Gatilho para sair da inbox
   ## Enquanto isso
   ```
4. Não edite nada fora desta pasta.

## Revisão (lado do hub)

Itens da inbox não são analisados até o dono do hub pedir. Ao resolver um item:
mude o `Status` para `feito em AAAA-MM-DD` com o link do que resolveu e **mova o
arquivo para `inbox/arquivo/`**. Nunca apague. Se o item não for aplicado, o mesmo:
`Status: descartado em AAAA-MM-DD` com o motivo, e mova.

Se a mudança tocar uma `description` de skill, rode `python3 .agent/scripts/build_sip_index.py` e `python3 .agent/scripts/generate_catalog.py`.
