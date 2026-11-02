---
name: geral-arquitetura-de-projeto
description: Use when creating or reorganizing a marketing project's folders, when deciding where a piece (brand file, post, press pitch, monitoring report, asset, data, reference, plan) must be saved, or when a skill needs the project's destination map before writing a file.
license: MIT
metadata:
  author: Felipe Bahia (Futuro Mercado)
  version: 1.0.0
---

# Arquitetura de projeto de marketing (onde cada coisa mora)

## Visão geral
**Princípio:** o lugar de cada peça é decidido **uma vez, por projeto**, num mapa de destinos que todas as skills leem antes de escrever. Skill nenhuma decide pasta por conta própria nem impõe a estrutura do 0 Mkt a um projeto que já tem a sua. Decisão registrada em `.agent/plans/arquitetura-de-pastas-das-pecas.md` (ADR-001).

## Princípio de separação `[usuário, 2026-10-23]`
- **Repositório do mercado (`inteligencia/`)** `[usuário, 2026-10-23]`: **tendências, pesquisas, estudos, materiais de terceiros e análises de mercado** (com dados e cases do mercado e as fontes). **Não é onde se guardam os arquivos que a marca produz.** O monitoramento operacional (`5_monitoramento/`) fica ali por ora; **a parte de imprensa está em ajuste pelo usuário** (ver abaixo).
- **Produção (`conteudos/`, `assets/`)**: o que a marca cria e publica: assessoria de imprensa (pauta, pitch, release), roteiros de vídeo longo e curto, texto para blog, LinkedIn, carrosséis e posts, newsletter, e-mail, materiais promocionais, apresentações, relatórios de cliente ou semanais e o que mais o marketing produzir. (**Relatório de monitoramento** é dado do mercado e vai para `inteligencia/5_monitoramento/relatorios/`.) Arte final e imagens em `assets/`.
- **Marca (`brand/`)**: regras e identidade.
Skill que produz peça escreve em **produção**, nunca em `inteligencia/`; skill que coleta ou monitora escreve em `inteligencia/`.

## Quando usar
- Projeto de marketing novo (criar a estrutura e o mapa de destinos).
- Projeto existente sem mapa (descobrir a convenção e propor o mapa, **sem mover nada**).
- Qualquer skill de marca, conteúdo, imprensa ou monitoramento prestes a gravar arquivo.
**Não usar** para arquitetura de software ou de site (ver `site-arquitetura`).

## Assessoria de imprensa: em ajuste (pendência do usuário, 2026-10-23)
A organização de imprensa é mais complexa e **será ajustada depois pelo usuário**; a skill de referência é `pr-assessoria-de-imprensa` (e este mapa). Já decidido: **pauta, pitch, release e seleção de jornalistas** são produção (`conteudos/imprensa/`); **clipping** (matérias em que a marca ou o porta-voz é citado pela imprensa) fica na **pasta de clipping dentro de assessoria de imprensa** (`conteudos/imprensa/clipping/`), e não em `inteligencia/`. A base de imprensa hoje em `inteligencia/2_imprensa_pr/` (mailing, guias, mapa de veículos) **será tratada em outro lugar**; não reorganizar até o ajuste. Painel: seção 7 de `.agent/plans/Reorganizacao de Skills Workflows e Agentes [TASK].md`.

## Onde mora o quê: skill ou documento do projeto `[usuário, 2026-10-23]`
- **No documento do projeto** (`docs/mapa-de-destinos.md`): pastas, nomes de etapa, **fluxo de aprovação e portões por tipo**, nomes de arquivo. Mudou o arranjo? **Altera-se só o documento.**
- **Na skill:** só o princípio, a regra de resolução abaixo, e um **padrão para projeto novo** (`references/`), usado uma vez, na criação do mapa. Skill nenhuma repete pastas ou etapas de um projeto específico.

## Regra de resolução (todas as skills seguem, nesta ordem)
1. **Ler o mapa de destinos do projeto**: `docs/mapa-de-destinos.md` (ou na raiz, se não houver `docs/`).
2. Se não houver mapa: procurar a convenção (`CLAUDE.md`, `STANDARDS.md` e as pastas existentes) e **propor o mapa ao usuário**, com a tabela preenchida pelo que existe; só gravar depois da confirmação.
3. **Só em projeto novo, sem convenção**: criar a estrutura padrão (modo projeto, abaixo) e o mapa.
4. **Marca hospedada no 0 Mkt** (modo 0 Mkt): `_brands/<marca>/` e `content/<marca>/<tipo>/AAAA-MM-DD - Nome da Demanda/`, como o `CLAUDE.md` do 0 Mkt manda.
5. **Nunca gravar no Hub Central** (`Compartilhado/RSS Feed`): ele é fonte de leitura. Dado novo que deve voltar ao Hub passa pelo procedimento do próprio Hub, com confirmação do usuário.
6. **Nunca mover arquivo existente** para encaixar na estrutura; mudança de lugar só com aprovação. Em conflito entre o mapa e uma regra de skill, **vale o mapa**.

## Dois modos
| Modo | Quando | Fundações da marca | Peças de conteúdo | Inventário de imagens |
|---|---|---|---|---|
| **0 Mkt** | Marca hospedada no 0 Mkt (`plus-pr`, `pr-pulse`, `experimentacao`) | `_brands/<marca>/` | `content/<marca>/<tipo>/AAAA-MM-DD - Nome/` | `_brands/<marca>/ativos/inventario.md` |
| **Projeto** | Marca com projeto próprio (Futuro Mercado, WaiMonitor) | `<projeto>/brand/` (raiz da marca) | `<projeto>/conteudos/` (pastas por tipo e/ou esteira, conforme o mapa) | `<projeto>/assets/inventario.md` |
Projeto novo usa o modo **Projeto**. A árvore completa, com a função de cada pasta e as convenções de nome, está em `references/arvore-padrao.md`; o modelo do mapa está em `references/modelo-mapa-de-destinos.md`.

## Quem escreve onde (modo Projeto)
| Família de skill | Escreve em | Lê de |
|---|---|---|
| Marca (`brand-builder` e sub-skills) | `brand/` e `brand/ativacao/`, `brand/logo/`, `brand/modelos/`, `brand/design-system/` | o próprio `brand/` |
| Conteúdo (peças de qualquer tipo) | `conteudos/<tipo>/AAAA-MM-DD - Nome da Demanda/` e/ou a esteira (`1_a_aprovar` …), conforme o mapa | `brand/`, `conteudos/_base/`, `inteligencia/` |
| Imprensa (`pr-assessoria-de-imprensa`): **pauta, pitch, release, seleção de jornalistas** | `conteudos/imprensa/AAAA-MM-DD - Nome/` (produção) | `brand/`, base `inteligencia/2_imprensa_pr/`, Hub (somente leitura) |
| Imprensa: histórico de envios e relacionamento | `inteligencia/2_imprensa_pr/envios/` (registro/base) | |
| Monitoramento | **regras** em `brand/ativacao/monitoramento.md` (fonte da verdade); **consultas, termos e relatórios** em `inteligencia/5_monitoramento/` | Hub (somente leitura), `brand/` |
| Dados e estudos | `inteligencia/3_estudos_embasamento/` (registro de fontes, banco de cases) | fontes externas |
| Imagens e arte | `assets/` | `brand/logo/`, `brand/modelos/` |

## Referência rápida
| Preciso de | Pasta |
|---|---|
| Fundações, voz, ativação, kit, modelos | `brand/` |
| Post, carrossel, roteiro (com aprovação) | `conteudos/` |
| Referência de técnica (hooks, retenção, formatos) | `conteudos/_base/referencias/` |
| Benchmark de canal (anexo da ativação) | `brand/ativacao/` |
| Pauta, pitch, release e seleção de jornalistas (**produção**) | `conteudos/imprensa/` |
| Clipping (matérias em que a marca ou o porta-voz foi citado) | `conteudos/imprensa/clipping/` |
| Mailing, guias de voz, mapa de veículos, histórico de envios (base atual; **em ajuste pelo usuário**) | `inteligencia/2_imprensa_pr/` (não reorganizar até o ajuste) |
| Roteiros de vídeo longo e curto | `conteudos/video/` |
| Blog, LinkedIn, carrossel e post, newsletter, e-mail, promocional, apresentação, relatório | `conteudos/blog/`, `linkedin/` (inclui carrossel de LinkedIn), `social/` (Instagram e demais redes), `newsletter/`, `email/`, `campaigns/`, `palestra/` (palestras), `apresentacoes/` (apresentação comercial), `reports/` (relatório de cliente ou semanal) |
| Consultas de monitoramento, `termos.txt`, relatório de menções | `inteligencia/5_monitoramento/` |
| Número com fonte, caso do mercado | `inteligencia/3_estudos_embasamento/` |
| Tendências | `inteligencia/1_radar_tendencias/` |
| Imagem e inventário | `assets/` |
| Plano e log de execução | `.agent/plans/` |
| Este mapa | `docs/mapa-de-destinos.md` |

## Criar projeto novo (checklist)
- [ ] Criar a árvore de `references/arvore-padrao.md` (só as pastas que o projeto usa; as demais nascem quando precisar)
- [ ] Criar `CLAUDE.md` do projeto apontando as skills do 0 Mkt (protocolo de fallback) e manter a paridade `GEMINI.md`, `AGENTS.md` (script de sincronização do 0 Padrões)
- [ ] Criar `STANDARDS.md` com nome de arquivo e metadados de peça
- [ ] Criar `docs/mapa-de-destinos.md` pelo modelo e dizer ao usuário o que cada linha significa
- [ ] Criar o registro de fontes (`registro-de-fontes.md` do `brand-builder`) em `inteligencia/3_estudos_embasamento/`
- [ ] **Confirmar com o usuário antes de escrever fora do 0 Mkt**

## Projeto existente sem mapa
Ler as pastas e as regras do projeto, montar o mapa com o que existe, apontar **inconsistências** (por exemplo, o `CLAUDE.md` cita uma pasta que não existe) e perguntar. Não mover nada.

## Erros comuns
| Erro | Correção |
|---|---|
| Gravar pitch, release ou roteiro em `inteligencia/` | `inteligencia/` é repositório do mercado; o que a marca produz vai para `conteudos/` |
| Gravar peça em `content/<marca>/` num projeto que já tem esteira | Ler o mapa; a esteira do projeto vence |
| Criar `_brands/<marca>/` para marca que tem projeto próprio | Usar a raiz da marca do projeto |
| Duplicar a lista de veículos e jornalistas no projeto | Consultar o Hub (leitura) |
| Regra de monitoramento em dois lugares | `brand/ativacao/monitoramento.md` manda; `5_monitoramento/` deriva dele |
| Mover arquivo antigo "para organizar" | Mapear, nunca mover sem aprovação |
