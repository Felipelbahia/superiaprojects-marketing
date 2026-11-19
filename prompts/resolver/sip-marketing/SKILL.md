---
name: sip-marketing
description: Use whenever the current task involves marketing, content, copywriting, branding, social media, SEO, paid ads, email, PR, growth, sales enablement or marketing analytics but the active project has no local marketing skills — i.e. any project other than "SIP - Marketing" (0 Mkt) itself. Routes the task to the central marketing knowledge hub instead of improvising from general knowledge. Also use when the user asks "existe algo de marketing pra isso", "tem skill de marketing no hub", "consulta o SIP - Marketing", or names a 0 Mkt skill, agent or workflow explicitly in a project that isn't the hub.
---

# sip-marketing

## Por que isso existe

O projeto `SIP - Marketing` (`<HUB>`) é a referência central de marketing: skills especialistas em `.agent/skills/`, agents em `.agent/agents/` e workflows `/comando` em `.agent/workflows/`. Esse conhecimento só é descoberto automaticamente dentro do próprio hub.

**Esta skill é um redirecionador:** o projeto consumidor instala só ela (um symlink). Ela não ensina marketing; leva até quem ensina. Skills, agents e workflows ficam no hub e são lidos **por caminho absoluto**. Não symlinke nem copie nenhum deles para o projeto.

## Passo 0 — acesso ao caminho

`<HUB>` é a pasta deste hub (repositório "0 Mkt") nesta máquina. Descubra-a assim: variável de ambiente `MARKETING_HUB_PATH`; senão a linha `Hub:` da entrada "SIP - Marketing" em `.agent/SIPS-CONSUMIDOS.md` do projeto; senão pergunte ao usuário e confirme que existe `<HUB>/prompts/resolver/sip-marketing/SKILL.md`. Nunca use o caminho de outra máquina. Leitura fora do diretório de trabalho pode pedir aprovação na primeira vez; use sempre o caminho absoluto entre aspas: `"<HUB>"`.

## Passo 1 — marca e destino ficam no projeto consumidor

As skills do hub foram escritas para o 0 Mkt, que guarda marcas em `_brands/<marca>/` e grava saídas conforme o `docs/mapa-de-destinos.md` **dele**. Num projeto consumidor:

- **Marca:** use os arquivos de marca do próprio projeto (voz, personas, pilares, guia de estilo). Se não houver e o pedido não disser qual marca, pergunte antes de escrever. Não leia `_brands/` do hub como se fosse a marca do projeto.
- **Onde gravar:** siga o `docs/mapa-de-destinos.md` do projeto consumidor; sem ele, use a skill `mapa-de-destinos` (via `sip-geral`). **Nunca grave peça, plano ou rascunho dentro do hub.**
- **Anti-slop:** todo texto entregue passa pela skill `geral-anti-slop` do hub antes de sair.

## Passo 2 — classifique a tarefa

| Tipo de tarefa | O que fazer |
| --- | --- |
| **Consulta pontual** (como escrever X, qual estrutura para Y) | **Modo consulta** (abaixo). |
| **Peça ou campanha grande / multi-arquivo** | **Modo dispatch** (abaixo). |
| **Procedimento com nome** ("tem um /comando pra isso?") | Ache o workflow na vertical e leia `"<HUB>/.agent/workflows/<nome>.md"`. |
| **Não sabe qual vertical** | Leia o workflow `geral-navegador-de-skills` ou o agent `geral-navegador-de-comandos` do hub. |

## Modo consulta (padrão — prefira este)

1. Ache a vertical na tabela do índice abaixo pela coluna "Use quando".
2. Leia só o arquivo dela: `"<HUB>/prompts/resolver/sip-marketing/verticais/<vertical>.md"`. Ali estão as skills, agents e workflows daquela área, cada um com o seu "Use quando". Sem certeza da vertical: `grep -ril "<palavra>" "<HUB>/prompts/resolver/sip-marketing/verticais/"`.
3. Leia só o `SKILL.md` da skill escolhida: `"<HUB>/.agent/skills/<nome>/SKILL.md"`. Abra `references/` dela só se o `SKILL.md` mandar.
4. Aplique inline e avise em uma linha que a resposta veio do hub `SIP - Marketing`, não de conhecimento genérico.

## Modo dispatch (só para construções grandes)

Não existe invocação nativa de agente cross-projeto no Claude Code. Disparar um agent do hub é montar um subagente genérico (`Agent`, `subagent_type: "general-purpose"`) com a persona colada no prompt:

1. Ache o agent na vertical da tarefa (seção Agents do arquivo dela) e leia `"<HUB>/.agent/agents/<nome>.md"` inteiro, mais as skills do frontmatter `skills:`.
2. Chame `Agent` com a persona + a tarefa + o caminho da marca e do mapa de destinos **do projeto consumidor**.
3. Revise o resultado com `geral-anti-slop` antes de entregar.

Agent ou workflow que o projeto não instalou: use-o assim mesmo, pelo caminho absoluto. Só ofereça instalar se o usuário disser que vai usá-lo com frequência; nunca instale por conta própria.

## Índice de verticais

<!-- indice:start dir=verticais (gerado por build_sip_index.py — não edite à mão) -->

Total: 99 skills, 33 agents, 114 workflows.

| Vertical | Use quando | Skills | Agents | Workflows | Arquivo |
| --- | --- | --- | --- | --- | --- |
| `ads` | Campanhas pagas (Google, Meta, multiplataforma), criativos, copy de anúncio, análise de desempenho e extração de anúncios de concorrentes. | 6 | 1 | 2 | `verticais/ads.md` |
| `audiovisual` | Vídeo, roteiro técnico, voz, podcast, apresentações e decks (Slidev, pitch deck), imagens por IA, infográfico, QR code, transcrição e legenda. | 10 | 2 | 13 | `verticais/audiovisual.md` |
| `brand` | Marca: essência, voz, naming, identidade visual e sonora, paleta, design system e direção criativa. | 9 | 2 | 2 | `verticais/brand.md` |
| `conteudo` | Estratégia e produção de conteúdo: briefing, blog, pesquisa, tendências, reaproveitamento, aprovação e pré-publicação. | 7 | 2 | 13 | `verticais/conteudo.md` |
| `copy` | Copy que converte: landing page, VSL, hooks de vídeo curto, roteiros, SaaS e métodos clássicos. | 7 | 1 | 7 | `verticais/copy.md` |
| `data` | Métricas e análise: GA4, funil e coortes, atribuição, UTM, ROI, relatórios e revisão mensal. | 3 | 1 | 9 | `verticais/data.md` |
| `email` | E-mail marketing: copy, newsletter, automação, assunto, modelos e entregabilidade. | 4 | 1 | 3 | `verticais/email.md` |
| `geral` | Apoio transversal: anti-slop, briefing e planejamento, verificação de fatos, priorização, postmortem, diagramas, LGPD e navegador de skills. | 2 | 7 | 13 | `verticais/geral.md` |
| `growth` | Crescimento: aquisição, experimentos e testes A/B, retenção e churn, indicação e afiliados, GTM. | 5 | 4 | 2 | `verticais/growth.md` |
| `persona` | Público: ICP, personas, descoberta e entrevistas com clientes, análise de feedback. | 2 | 1 | 4 | `verticais/persona.md` |
| `pr` | Assessoria de imprensa, relações públicas, press releases e pitches de mídia. | 1 | 1 | 0 | `verticais/pr.md` |
| `produto` | Produto: PRD, requisitos, user stories, roadmap, sprint e especificação de funcionalidade. | 2 | 0 | 8 | `verticais/produto.md` |
| `revenue` | Estratégia de receita: campanhas, lançamento, oferta, preço, posicionamento, inteligência competitiva, psicologia e Sexy Canvas. | 12 | 3 | 10 | `verticais/revenue.md` |
| `seo` | Busca orgânica: palavras-chave, on-page, técnico, schema, GEO, backlinks, SEO programático, app store e relatórios. | 11 | 1 | 7 | `verticais/seo.md` |
| `site` | Sites e landing pages: arquitetura, CRO, interface de conversão, construção, auditoria de interface, React e Tailwind. | 8 | 2 | 4 | `verticais/site.md` |
| `social` | Redes sociais: estratégia, carrossel, LinkedIn, Instagram, YouTube, thumbnails e análise de desempenho. | 5 | 1 | 11 | `verticais/social.md` |
| `vendas` | Vendas B2B: prospecção, cold email, pipeline, metodologias, materiais e personalização em escala. | 5 | 3 | 6 | `verticais/vendas.md` |

<!-- indice:end -->

## Modo contribuição (devolver conhecimento ao hub)

**Exceção primeiro:** se o dono do hub pediu a mudança nesta conversa, edite `.agent/skills/`, `.agent/agents/` ou `.agent/workflows/` do hub direto.

Caso contrário, nunca edite essas pastas a partir de um projeto consumidor: elas são lidas por caminho absoluto por todos os consumidores e uma edição sem curadoria propagaria na hora. Em vez disso:

1. Leia o formato em `"<HUB>/inbox/README.md"`.
2. Crie `"<HUB>/inbox/NNN-<assunto>.md"` (próximo número livre, contando `inbox/arquivo/`) com todas as seções do formato, escrito para quem nunca viu a conversa.
3. Avise o usuário que a contribuição ficou pendente de revisão.

## Atualização

- Última atualização do hub: 2026-11-18 (o dono do hub muda esta data sempre que esta skill, um agent, um workflow ou a estrutura do hub mudar).
- Para atualizar a instalação num projeto (refazer links, escolher entre os agents/workflows novos): cole de novo o prompt `"<HUB>/prompts/instalar-skill-sip-marketing.md"` numa sessão daquele projeto.
- A data em que **cada projeto** instalou ou atualizou fica no `.agent/SIPS-CONSUMIDOS.md` dele. Se for anterior à data acima, ofereça rodar o prompt.

## Se nada bater

Se a tarefa não é de marketing, ou se o projeto atual é o próprio `SIP - Marketing` (0 Mkt), não force o uso desta skill.
