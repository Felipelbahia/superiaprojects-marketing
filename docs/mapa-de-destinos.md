# Mapa de destinos: 0 Mkt
Estrutura: multi-marca por desenho (cada marca hospedada tem a sua subpasta). Modo: 0 Mkt.
Atualizado em 2026-11-07 (linhas `vendas` e `design` acrescentadas após a auditoria de padrão). Se este mapa divergir de uma regra de skill, **vale este mapa**. Pasta nova, ou tipo de peça que não está aqui, entra aqui antes de ser usada. Regras de resolução, mapa incompleto e conversa de criação: skill `mapa-de-destinos`.

`{marca}` é o nome da pasta em `_brands/`. `{tipo}` é o tipo de peça (blog, linkedin, social, newsletter, email, video, palestra, apresentacoes, reports, vendas, design). Hoje não há marca ativa: `_brands/` só tem o `brand-template/`.

| Tipo de peça | Caminho | Escopo | Nome e metadados | Observação |
|---|---|---|---|---|
| Fundações da marca (voz, personas, pilares, guia de estilo) | `_brands/{marca}/` | marca | `brand-voice.md`, `personas.md`, `content-pillars.md`, `style-guide.md` | somente identidade; nunca output final |
| Inventário de imagens da marca | `_brands/{marca}/ativos/inventario.md` | marca | | |
| Estratégia geral | `content/{marca}/estrategia/estrategia-geral.md` | marca | | |
| Calendários | `content/{marca}/estrategia/calendarios/` | marca | | |
| Campanha (plano, meta, resultado) | `content/{marca}/estrategia/campanhas/AAAA-MM-DD - Nome da Campanha/` | marca | `campanha.md`, `checklist-lancamento.md`, `apresentacao.html`, `resultado.md` | resultado esperado definido antes de começar; as peças ficam em `content/{marca}/{tipo}/`. Campanha contínua é permitida (`tipo: continua`, sem `fim:`) |
| Peça de conteúdo por tipo | `content/{marca}/{tipo}/AAAA-MM-DD - Nome da Demanda/` | marca | `copy-opcao-1.md`, `copy-opcao-2.md`, `briefing.md`, `draft.md`; campo `campanha:` quando serve a uma campanha | |
| Playbook, cadência e material comercial | `content/{marca}/vendas/AAAA-MM-DD - Nome da Demanda/` | marca | `cadencia-outbound.md`, `playbook-discovery.md`, `deal-governance.md` | tipo `vendas` (agente `vendas-direcao-b2b`) |
| Direção de arte e briefing visual | `content/{marca}/design/AAAA-MM-DD - Nome da Demanda/` | marca | `direcao-de-arte.md`, `prompts-ia.md`, `briefing-layout.md` | tipo `design` (agente `brand-direcao-de-arte`); arte final fica em `assets/` |
| Fluxo de aprovação | sem esteira | marca | campo `status:` nos metadados da peça | ver "Respostas" |
| Assessoria de imprensa: pauta (pasta com ângulos), pitch por ângulo, release, jornalistas | `content/{marca}/imprensa/AAAA-MM-DD - Nome/` | marca | `pauta/pauta-principal.md`, `pauta/angulo-<tema>.md`, `pitch/`, `release.md`, `jornalistas.md` | base de jornalistas só no Hub (leitura) |
| Controle de envio de imprensa | `content/{marca}/imprensa/envios.md` | marca | uma linha por envio | status enviado → respondeu → publicou → sem retorno |
| Clipping | `content/{marca}/imprensa/clipping/` | marca | `AAAA-MM-DD_<veiculo>_<tema>.md` | |
| Monitoramento (consultas, termos, relatório) | `content/{marca}/inteligencia/monitoramento/` | marca | | substitui o antigo `content/{marca}/monitoramento/` |
| Estudos, dados, cases, registro de fontes | `content/{marca}/inteligencia/estudos/` | marca | | |
| Tendências | `content/{marca}/inteligencia/tendencias/` | marca | | |
| Planos e log de execução | `.agent/plans/` | projeto | `{Nome da Tarefa} [PLAN].md`, `[TASK].md`, `[WALKTHROUGH].md` | |
| Hub Central | `Compartilhado/RSS Feed` | — | | **somente leitura** |

## Como usar este mapa (toda skill que grava arquivo)
1. Leia esta tabela antes de gravar. Use o **Caminho** da linha do tipo de peça, preenchendo os placeholders. Não monte caminho por conta própria.
2. Tipo de peça que não está aqui: use o tipo mais próximo, grave e avise o usuário para acrescentar a linha.
3. Pasta que o mapa cita e não existe: crie só essa pasta.
4. Nunca mova nem apague arquivo existente para encaixar na estrutura; mudança de lugar só com aprovação.
5. Nunca grave no Hub Central. Em dúvida que este mapa não resolve, consulte a skill `mapa-de-destinos`.

## Respostas da conversa de criação
| Pergunta | Resposta | Data |
|---|---|---|
| Há mais de uma marca ou produto? | sim: cada marca hospedada em `_brands/{marca}/` e `content/{marca}/` (multi-marca por desenho do 0 Mkt) | 2026-11-07 |
| Onde moram as marcas? | mesmo projeto | 2026-11-07 |
| Fluxo de aprovação | opção 0, sem esteira (campo `status:`); registros de imprensa ficam sempre em `content/{marca}/imprensa/` | 2026-11-07 |
| Quem aprova | o dono do hub | 2026-11-07 |

## Inconsistências conhecidas
- A marca fica em `_brands/{marca}/` (identidade) e o output em `content/{marca}/`. Se o usuário preferir `brand/{marca}/`, é uma migração e depende de aprovação.
- `inteligencia` dentro de `content/{marca}/` foi confirmada em 2026-11-07: pelo princípio da skill, `inteligencia/` não guarda peças produzidas, mas aqui o 0 Mkt agrupa tudo por marca em `content/`.
