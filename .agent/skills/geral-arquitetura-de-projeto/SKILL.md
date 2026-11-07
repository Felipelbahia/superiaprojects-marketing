---
# Repository: https://github.com/Felipelbahia/superiaprojects-marketing
# Status: Nativa do Projeto
name: geral-arquitetura-de-projeto
description: Use when creating or reorganizing a marketing project's folders, when deciding where a piece (brand file, strategy, campaign, post, press pitch, monitoring report, asset, data, plan) must be saved, when the project has more than one brand or product, or when a skill needs the project's destination map before writing a file.
author: Felipe Bahia (Futuro Mercado)
license: MIT
metadata:
  author: Felipe Bahia (Futuro Mercado)
  version: 1.1.0
---
# Arquitetura de projeto de marketing (onde cada coisa mora)

## Visão geral
**Princípio:** o lugar de cada peça é decidido **uma vez, por projeto**, num mapa de destinos que todas as skills leem antes de escrever. Skill nenhuma decide pasta por conta própria nem impõe a estrutura do 0 Mkt a um projeto que já tem a sua. Decisão registrada em `.agent/plans/arquitetura-de-pastas-das-pecas.md` (ADR-001, revisado em 2026-11-07: ver o bloco de revisão no topo do ADR).

**Escopo por pasta:** cada pasta de topo declara no mapa o seu **escopo**: `projeto` (uma só, compartilhada), `marca` ou `produto`. Só a pasta que de fato diverge entre marcas ou produtos ganha subpasta; o que é compartilhado fica na raiz, sem duplicar. Mono-marca é o caso mais comum e não tem subpasta nenhuma.

## Glossário (termos fixos nesta skill e nos mapas)
- **Demanda:** a pasta datada `AAAA-MM-DD - Nome da Demanda/` que reúne os arquivos de uma entrega.
- **Fluxo de aprovação:** o processo pelo qual uma peça é aprovada. Pode ou não usar esteira.
- **Esteira:** as pastas `1_a_aprovar`, `2_aprovado`, `3_publicado`, `4_revisar_ajustar`, quando o projeto escolhe usar fluxo com pastas.
- **Mapa:** `docs/mapa-de-destinos.md` do projeto. **Campanha** (não "campaign") em qualquer caminho novo.

## As áreas da raiz
| Pasta | O que é | Exemplo |
|---|---|---|
| `brand/` | Regras e identidade da marca | voz, personas, pilares, kit visual, regras de monitoramento |
| `estrategia/` | Planejamento: direção geral e campanhas | estratégia geral, calendários, `campanhas/` |
| `imprensa/` | **Assessoria de imprensa** (produção com ciclo próprio): pauta, pitch, release, seleção de jornalistas, controle de envio, clipping | `imprensa/AAAA-MM-DD - Nome/`, `envios.md`, `clipping/` |
| `conteudos/` | **Produção**: o que a marca cria e publica | roteiro, post, newsletter, e-mail, relatório de cliente |
| `inteligencia/` | **Repositório do mercado**: tendências, pesquisas, estudos, materiais de terceiros, monitoramento. Não guarda o que a marca produz | radar, estudos e cases com fonte, relatório de menções |
| `referencias/` | Referências **do projeto** que influenciam todo o conteúdo | rubrica, perfil e voz, formatos, hooks e iscas já adaptados à marca |
| `assets/` | Arte final e imagens, com inventário | |

Skill que produz peça escreve em `conteudos/`, `imprensa/` ou `assets/`, nunca em `inteligencia/`. Skill que coleta ou monitora escreve em `inteligencia/`. Registro do que a marca fez (envio de pitch, publicação) é produção: fica em `imprensa/` ou `conteudos/`. A esteira de aprovação vale para `conteudos/`; a imprensa tem o ciclo próprio do `envios.md`.

**Nomes de pasta sem número**, exceto onde o número indica sequência de verdade (a esteira de aprovação: `1_a_aprovar → 4_revisar_ajustar`).

## Campanha é estratégia com foco e prazo
Uma campanha vive em `estrategia/campanhas/AAAA-MM-DD - Nome da Campanha/` e tem um `campanha.md` com objetivo, prazo, etapas, canais e peças, arquivos conectados e **resultado esperado definido antes de começar** (métrica, fonte, janela, critério de sucesso e de fracasso). Ao encerrar, nasce o `resultado.md` (esperado vs. real). As **peças** da campanha ficam em `conteudos/<tipo>/` e o `campanha.md` aponta para elas; cada peça leva `campanha:` nos metadados. Quem cria é `revenue-campanhas` (workflows `revenue-criacao-de-campanha` e `revenue-checklist-de-lancamento-de-campanha`). **Campanha contínua** (sem data de fim) é permitida: `tipo: continua` no `campanha.md`, sem `fim:`, com revisão periódica no lugar da leitura final. Modelo: `revenue-campanhas/references/modelo-campanha.md` (inclui `resultado.md` e a revisão periódica da campanha contínua).

## Quando usar
- Projeto de marketing novo (conduzir a conversa de criação e escrever o mapa).
- Projeto existente sem mapa (descobrir a convenção e propor o mapa, **sem mover nada**).
- Projeto que passou a ter mais de uma marca ou produto.
- Qualquer skill de marca, estratégia, conteúdo, imprensa ou monitoramento prestes a gravar arquivo.
**Não usar** para arquitetura de software ou de site (ver `site-arquitetura`).

## Assessoria de imprensa
Skill de referência: `pr-assessoria-de-imprensa` (e este mapa).
- **Pauta, pitch, release e seleção de jornalistas** são produção, em `imprensa/AAAA-MM-DD - Nome/`. A **pauta é uma pasta**: `pauta/pauta-principal.md` e um `angulo-<tema>.md` por ângulo; o `pitch/` tem um arquivo por ângulo.
- **Controle de envio** (qual ângulo foi para qual jornalista, quando, e o que voltou): `imprensa/envios.md` (ou `.csv`), com status `enviado → respondeu → publicou → sem retorno` e link para o item do clipping. `lido` é campo opcional (abertura de e-mail é pouco confiável). O envio carrega a demanda e o ângulo (e a marca, em multi-marca); o link do clipping usa o nome do arquivo `AAAA-MM-DD_<veiculo>_<tema>.md`. `jornalistas.md` da demanda é a seleção **planejada**; `envios.md` é o **realizado**. Não existe `inteligencia/2_imprensa_pr/`.
- **Clipping** (matérias em que a marca ou o porta-voz é citado): `imprensa/clipping/`.
- **Jornalista, veículo e a metodologia da base** (validação de e-mail, scraping/RSS) só vivem no Hub `Compartilhado/RSS Feed`, nunca duplicados no projeto; consultar via `motores/jornalistas/consultar_hub.py`.
- **Técnica de redação** (ângulos editoriais, matriz de newsjacking, templates de pitch) é playbook reutilizável: mora **na skill** `pr-assessoria-de-imprensa/references/`, não no projeto. O projeto guarda só o que é dele: identidade do porta-voz em `brand/` e a lista de ângulos permanentes da marca (posicionamento) em `brand/ativacao/`. O `angulo-<tema>.md` da pauta é a aplicação de um ângulo a uma pauta específica e cita de qual ângulo permanente nasceu.
- Painel: seção 7 de `.agent/plans/Reorganizacao de Skills Workflows e Agentes [TASK].md`.

## Onde mora o quê: skill ou documento do projeto
- **No documento do projeto** (`docs/mapa-de-destinos.md`): pastas, escopo de cada uma, nomes de etapa, **fluxo de aprovação e portões por tipo**, nomes de arquivo. Mudou o arranjo? **Altera-se só o documento.**
- **Na skill:** só o princípio, a regra de resolução abaixo, a conversa de criação, e os padrões (`references/`) usados uma vez, na criação do mapa. Skill nenhuma repete pastas ou etapas de um projeto específico.
- **Técnica reutilizável** (playbook de redação, hooks, retenção, formatos genéricos) mora na skill do assunto. **Referência específica do projeto** que influencia todo o conteúdo (rubrica, perfil e voz, formatos adaptados à marca) mora em `referencias/`, na raiz. **Dado e referência do mercado** mora em `inteligencia/`, na raiz, porque alimenta o projeto inteiro. Não existe `conteudos/_base/`; o que seria personalização de uma demanda vai no `briefing.md` da pasta dela.

## Regra de resolução (todas as skills seguem, nesta ordem)
1. **Qual é o modo?** Marca hospedada no 0 Mkt (`_brands/<marca>/`) ou projeto próprio: em ambos, leia o mapa, `docs/mapa-de-destinos.md` (ou na raiz, se não houver `docs/`). O 0 Mkt tem mapa próprio (ver regra 5). Ele traz **o caminho completo de cada tipo de peça, já com os placeholders** (ex.: `conteudos/{tipo}/` em mono-marca, `marcas/{marca}/conteudos/{tipo}/` em multi-marca). Use o caminho do mapa; nunca monte prefixo de marca por conta própria.
2. **Sem mapa, crie o mapa mínimo antes de gravar a primeira peça** (sem bloquear a entrega). (a) O projeto tem convenção visível (`CLAUDE.md`, `STANDARDS.md`, pastas existentes)? O mapa documenta o que já existe, sem mover nada, e a peça vai nessa convenção. (b) Não tem nada? Faça **uma só pergunta**, "há mais de uma marca ou produto?", e crie `docs/mapa-de-destinos.md` pelo modelo, com a árvore padrão (`references/arvore-padrao.md`), **sem marca no caminho** (o padrão é mono-marca) e fluxo de aprovação sem esteira (opção 0). Se o usuário não responder ou disser "tanto faz", assuma mono-marca e registre na seção "Respostas" do mapa que foi suposição. Fora do 0 Mkt, confirme com o usuário antes de criar o arquivo; se ele não puder responder agora, grave no padrão e crie o mapa mínimo mesmo assim. Só adote outra estrutura depois da confirmação dele.
3. **Mono-marca vs. multi-marca/produto**: nunca assuma. Se o mapa não responde, **pergunte** (conversa de criação, abaixo) antes de criar qualquer subpasta de marca ou produto.
4. **Só em projeto novo, sem convenção alguma**: conduzir a conversa de criação, criar a estrutura padrão (modo projeto) e o mapa.
5. **Marca hospedada no 0 Mkt** (modo 0 Mkt): o `docs/mapa-de-destinos.md` do 0 Mkt manda: identidade em `_brands/<marca>/`, output em `content/<marca>/…` (peças em `<tipo>/`, estratégia e campanhas em `estrategia/`, imprensa em `imprensa/`). 0 Mkt é multi-marca por desenho, por isso sempre tem a subpasta `<marca>/`; a regra 1.4 do `CLAUDE.md` do 0 Mkt delega ao mapa.
6. **Nunca gravar no Hub Central** (`Compartilhado/RSS Feed`): ele é fonte de leitura. Dado novo que deve voltar ao Hub passa pelo procedimento do próprio Hub, com confirmação do usuário.
7. **Nunca mover arquivo existente** para encaixar na estrutura; mudança de lugar só com aprovação. Em conflito entre o mapa e uma regra de skill, **vale o mapa** (o mapa não vale sobre o `CLAUDE.md` do projeto, que manda nele; por isso o `CLAUDE.md` deve delegar ao mapa).
8. **Mapa incompleto ou desatualizado:** tipo de peça que não está no mapa → use o tipo mais próximo, grave e avise o usuário para acrescentar a linha (não pare a entrega). Pasta que o mapa cita e não existe → crie só essa pasta. Árvore real diferente do mapa → avise e siga o mapa. Criar pasta de tipo nova fora do mapa só com aviso.

## Conversa de criação (projeto novo ou que passou a ter mais marcas)
Uma pergunta por vez; o usuário guia a construção. Mostrar a árvore resultante de cada opção antes de ele escolher. Os desenhos de cada cenário estão em `references/cenarios-multi-marca.md`; mostrar só o que for relevante.

1. **Há mais de uma marca ou produto?** Não → estrutura simples, sem subpastas (padrão). Sim → pergunta 2.
2. **Como se relacionam?** (A) marcas independentes; (B) uma marca com vários produtos; (C) marcas independentes, cada uma com produtos; (D) produtos com identidade própria sob uma marca-mãe.
3. **Onde as marcas moram?** (cenários A e C; em B e D, perguntar também se algum produto precisa de repositório próprio) Dentro do mesmo projeto, em `marcas/<marca>/`, ou **cada marca em seu próprio repositório**. Apresentar os dois com os prós e contras (tabela em `references/cenarios-multi-marca.md`) e deixar o usuário decidir. Não recomendar por padrão sem ouvir o contexto de equipe.
4. **O que é compartilhado?** Pergunta por pasta (`brand/`, `estrategia/`, `conteudos/`, `inteligencia/`, `assets/`), mostrando a sugestão padrão. Preencher a coluna **Escopo** do mapa com as respostas.
5. **Fluxo de aprovação** (seção abaixo). Em multi-marca, acrescentar: a esteira é por marca ou global?
6. **Escrever o mapa**, dizer ao usuário o que cada linha significa e registrar as respostas nele, para não perguntar de novo.

## Dois modos
| Modo | Quando | Fundações da marca | Peças de conteúdo | Inventário de imagens |
|---|---|---|---|---|
| **0 Mkt** | Marca hospedada no 0 Mkt (`_brands/<marca>/`) | `_brands/<marca>/` | `content/<marca>/<tipo>/AAAA-MM-DD - Nome/` | `_brands/<marca>/ativos/inventario.md` |
| **Projeto** | Marca com projeto próprio (Futuro Mercado, WaiMonitor) | `<projeto>/brand/` (raiz da marca) | `<projeto>/conteudos/` (pastas por tipo e/ou esteira, conforme o mapa) | `<projeto>/assets/inventario.md` |
Projeto novo usa o modo **Projeto**. No modo 0 Mkt, a campanha vive em `content/<marca>/estrategia/campanhas/…` (ver o mapa do 0 Mkt). A árvore completa e as convenções de nome estão em `references/arvore-padrao.md`; o modelo do mapa está em `references/modelo-mapa-de-destinos.md`.

## Quem escreve onde (modo Projeto, mono-marca)
Em multi-marca, use o caminho completo que o mapa traz, com placeholders (por exemplo `marcas/{marca}/conteudos/{tipo}/`); não monte o prefixo por conta própria.

| Família de skill | Escreve em | Lê de |
|---|---|---|
| Marca (`brand-builder` e sub-skills) | `brand/` e `brand/ativacao/`, `brand/logo/`, `brand/modelos/`, `brand/design-system/` | o próprio `brand/` |
| Estratégia e campanha (`revenue-campanhas`, `conteudo-estrategia`) | `estrategia/`, `estrategia/campanhas/AAAA-MM-DD - Nome/` | `brand/`, `inteligencia/` |
| Conteúdo (peças de qualquer tipo) | `conteudos/<tipo>/AAAA-MM-DD - Nome da Demanda/` e/ou a esteira (`1_a_aprovar` …), conforme o mapa | `brand/`, `estrategia/`, `inteligencia/` |
| Imprensa (`pr-assessoria-de-imprensa`): pauta, pitch, release, seleção de jornalistas, controle de envio, clipping | `imprensa/` | `brand/`, Hub `Compartilhado/RSS Feed` (somente leitura) |
| Monitoramento | **regras** em `brand/ativacao/monitoramento.md` (fonte da verdade); **consultas, termos e relatórios** em `inteligencia/monitoramento/` | Hub (somente leitura), `brand/` |
| Dados e estudos | `inteligencia/estudos/` (registro de fontes, banco de cases) | fontes externas |
| Imagens e arte | `assets/` | `brand/logo/`, `brand/modelos/` |

## Referência rápida
| Preciso de | Pasta |
|---|---|
| Fundações, voz, ativação, kit, modelos | `brand/` |
| Estratégia geral, calendário | `estrategia/` |
| Campanha (plano, meta, resultado) | `estrategia/campanhas/AAAA-MM-DD - Nome/` |
| Post, carrossel, roteiro (com aprovação) | `conteudos/` |
| Técnica de redação (hooks, retenção, formatos, newsjacking) | dentro da skill do assunto, nunca no projeto |
| Benchmark de canal (anexo da ativação) | `brand/ativacao/` |
| Pauta (pasta com ângulos), pitch, release e seleção de jornalistas | `imprensa/AAAA-MM-DD - Nome/` |
| Controle de envio de imprensa | `imprensa/envios.md` |
| Clipping | `imprensa/clipping/` |
| Mailing, ficha de jornalista, mapa de veículos, metodologia de e-mail/scraping (**só no Hub**) | `Compartilhado/RSS Feed/bases/jornalistas/`, `bases/veiculos/veiculos.csv` |
| Roteiros de vídeo longo e curto | `conteudos/video/` |
| Blog, LinkedIn, carrossel e post, newsletter, e-mail, apresentação, relatório | `conteudos/blog/`, `linkedin/`, `social/`, `newsletter/`, `email/`, `palestra/`, `apresentacoes/`, `reports/` |
| Consultas de monitoramento, `termos.txt`, relatório de menções | `inteligencia/monitoramento/` |
| Número com fonte, caso do mercado, pesquisa | `inteligencia/estudos/` |
| Tendências | `inteligencia/tendencias/` |
| Imagem e inventário | `assets/` |
| Plano e log de execução | `.agent/plans/` |
| Este mapa | `docs/mapa-de-destinos.md` |

## Criar projeto novo (checklist)
- [ ] Conduzir a **conversa de criação** (marcas e produtos, onde moram, o que é compartilhado)
- [ ] Criar a árvore de `references/arvore-padrao.md` (só as pastas que o projeto usa; as demais nascem quando precisar)
- [ ] Criar `CLAUDE.md` do projeto apontando as skills do 0 Mkt (protocolo de fallback) e manter a paridade `GEMINI.md`, `AGENTS.md` (script de sincronização do 0 Padrões)
- [ ] Criar `STANDARDS.md` com nome de arquivo e metadados de peça (inclui o campo `campanha:`)
- [ ] **Perguntar o fluxo de aprovação** (seção abaixo) antes de escrever o mapa
- [ ] Criar `docs/mapa-de-destinos.md` pelo modelo, com a coluna Escopo, e dizer ao usuário o que cada linha significa
- [ ] Criar o registro de fontes (`registro-de-fontes.md` do `brand-builder`) em `inteligencia/estudos/`
- [ ] **Confirmar com o usuário antes de escrever fora do 0 Mkt**

## Fluxo de aprovação: perguntar sempre, padrão é sem esteira
Ao criar o mapa de um projeto novo (ou ao fechar uma inconsistência num projeto sem mapa), perguntar qual das 4 opções usar. Se o usuário não souber ou pular a pergunta, registrar a opção 0 no mapa e seguir:

| # | Opção | Estrutura | Quando preferir |
|---|---|---|---|
| **0 (padrão)** | Sem esteira | Estado vai no campo `status:` dos metadados, dentro de `conteudos/<tipo>/AAAA-MM-DD - Nome/`. Nenhuma pasta nova. | Uma pessoa só aprovando; poucas peças por vez. **É a resposta se o usuário não disser nada.** |
| **A** | Esteira geral, tudo junto | `conteudos/1_a_aprovar/`, `2_aprovado/`, `3_publicado/`, `4_revisar_ajustar/` com peças de todos os tipos misturadas | Volume baixo e um fluxo só |
| **B** | Esteira, espinha primeiro (tipo dentro) | `conteudos/1_a_aprovar/<tipo>/`, `2_aprovado/<tipo>/` … | Mais de uma pessoa aprovando e querendo ver tudo que está num estágio. Precedente: Futuro Mercado (ADR-002, `.agent/plans/fluxo-de-aprovacao-das-pecas.md`) |
| **C** | Esteira, tipo primeiro (estágio dentro) | `conteudos/<tipo>/1_a_aprovar/`, `conteudos/<tipo>/2_aprovado/` … | Equipes por tipo de conteúdo |

Se a resposta for A, B ou C, registrar a escolha no `docs/mapa-de-destinos.md` (linha "Fluxo de aprovação") para não perguntar de novo. Nomes das pastas da esteira ficam sempre `1_a_aprovar`, `2_aprovado`, `3_publicado`, `4_revisar_ajustar`.

## Projeto existente sem mapa
Ler as pastas e as regras do projeto, montar o mapa com o que existe (incluindo nomes antigos como `inteligencia/1_radar_tendencias/` ou `conteudos/_base/`), apontar **inconsistências** e perguntar. Não mover nada. O mapa documenta o que existe; a migração para a árvore nova é decisão do usuário.

## Erros comuns
| Erro | Correção |
|---|---|
| Gravar pitch, release ou roteiro em `inteligencia/` | `inteligencia/` é do mercado; o que a marca produz vai para `conteudos/` |
| Gravar o controle de envio de imprensa em `inteligencia/` | É registro do que a marca fez: `imprensa/envios.md` |
| Guardar playbook genérico de redação em pasta do projeto | Técnica reutilizável mora na skill do assunto; o que é específico do projeto vai para `referencias/` na raiz |
| Criar `conteudos/_base/` | Pesquisa vai para `inteligencia/estudos/`; estratégia para `estrategia/`; personalização de demanda para o `briefing.md` |
| Gravar campanha em `conteudos/campaigns/` num projeto novo | Campanha é estratégia: `estrategia/campanhas/` |
| Copiar as peças para dentro da pasta da campanha | Peças ficam em `conteudos/`; a campanha aponta para elas |
| Campanha sem resultado esperado, ou com meta escrita depois | Definir métrica, fonte, janela e critérios antes de começar |
| Numerar pasta que não tem sequência (`1_radar…`) | Número só na esteira de aprovação |
| Gravar peça em `content/<marca>/` num projeto que já tem esteira | Ler o mapa; a esteira do projeto vence |
| Criar `_brands/<marca>/` para marca que tem projeto próprio | Usar a raiz da marca do projeto |
| Duplicar a lista de veículos e jornalistas no projeto | Consultar o Hub (leitura) |
| Regra de monitoramento em dois lugares | `brand/ativacao/monitoramento.md` manda; `inteligencia/monitoramento/` deriva dele |
| Mover arquivo antigo "para organizar" | Mapear, nunca mover sem aprovação |
| Criar subpasta de marca/produto sem perguntar | Conduzir a conversa de criação; subpasta só com a resposta do usuário |
| Não gravar porque "não achou o mapa", ou gravar sem criar o mapa | Sem mapa, crie o mapa mínimo (regra 2) e grave; a ausência de mapa não bloqueia a entrega, mas também não fica sem mapa |
