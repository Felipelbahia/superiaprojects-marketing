---
name: revenue-criacao-de-campanha
description: Create a comprehensive marketing campaign from strategy to execution.
---

# /campaign - Create Marketing Campaign

Follow this workflow to create a marketing campaign.

## Step 1: Campaign Brief

Define the campaign basics:

1. **Goal**: What are we trying to achieve?
   - Awareness
   - Lead generation
   - Sales/conversions
   - Product launch
   - Brand building

2. **Target Audience**: Who are we reaching?
   - Demographics
   - Psychographics
   - Pain points
   - Where they hang out

3. **Budget & Timeline**: Resources and deadlines

4. **Success Metrics**: How will we measure success?

## Step 2: Strategy Development

1. **Positioning**: How do we want to be perceived?
2. **Messaging**: Key messages and value proposition
3. **Channels**: Which channels to use
   - Paid (Google, Meta, LinkedIn)
   - Organic (SEO, social, email)
   - Earned (PR, influencers)
4. **Creative direction**: Visual and copy themes

## Step 3: Content Creation

Create campaign assets:

1. **Landing pages**: Design and copy
2. **Ad creative**: Images, videos, copy
3. **Email sequences**: Nurture flows
4. **Social content**: Platform-specific posts
5. **Blog/SEO content**: Supporting content

## Step 4: Setup & Launch

1. **Tracking**: UTMs, pixels, conversion events
2. **Audience setup**: Targeting configuration
3. **A/B tests**: Variations to test
4. **Launch checklist**: Pre-flight checks
5. **Go live**: Execute launch

## Step 5: Optimize

1. **Monitor**: Daily/weekly check-ins
2. **Analyze**: Performance vs goals
3. **Iterate**: Adjust based on data
4. **Report**: Share learnings

## Registrar a campanha (obrigatório)

Ao aprovar o brief e a estratégia, crie o `campanha.md` pelo modelo `.agent/skills/revenue-campanhas/references/modelo-campanha.md` (pontual ou contínua), no destino do mapa de destinos do projeto. Preencha objetivo, prazo, etapas, canais e **resultado esperado com linha de base, critério de sucesso e de fracasso antes de produzir qualquer peça**. A campanha só sai de `rascunho` com a aprovação do dono. Ao encerrar, crie o `resultado.md` (ou as revisões periódicas, se for contínua).

## Output

- `campanha.md` (objetivo, prazo, etapas, resultado esperado)

- Campaign brief document
- Content calendar
- Creative assets
- Tracking setup
- Results report

## Passo 6: Apresentação em HTML (opcional)

Perguntar ao usuário: **"Quer que eu gere um arquivo de apresentação em HTML para esta campanha?"**

Se sim:

### 6.1 Montar a apresentação em HTML

Usar a skill `site-interface-de-conversao` para criar uma apresentação em um único arquivo HTML, com:
- Tema escuro moderno com gradiente
- Navegação por slide (setas do teclado + clique)
- Barra de progresso
- Suporte a toque/swipe no celular
- CSS tudo embutido no arquivo (sem dependência externa)

Slides de conteúdo: título com nome da campanha, metas e KPIs, público-alvo, mensagens-chave, canais de marketing, cronograma, plano de conteúdo, métricas de sucesso, CTA/próximos passos.

Salvar seguindo o mapa de destinos do projeto (`docs/mapa-de-destinos.md`; skill `geral-arquitetura-de-projeto`). Sem mapa, grave no padrão direto, sem marca no caminho: `estrategia/campanhas/AAAA-MM-DD - Nome da Campanha/apresentacao.html` (o mapa do 0 Mkt, multi-marca, usa `content/<marca>/estrategia/campanhas/AAAA-MM-DD - Nome da Campanha/apresentacao.html`). O plano da campanha é o `campanha.md` (modelo em `.agent/skills/revenue-campanhas/references/modelo-campanha.md`).

### 6.2 Visualizar localmente

Abrir a apresentação no navegador:

```bash
# macOS
open apresentacao.html
```

Publicar na internet só se o usuário pedir explicitamente, e nesse caso usando a infraestrutura de deploy já definida no projeto (não inventar ferramenta de túnel nova).

## Passo 7: Produção automatizada de vídeo (opcional)

Perguntar ao usuário: **"Quer que eu gere um vídeo de anúncio automático para esta campanha (TikTok/Reels/Meta)?"**

Se sim, usar o workflow/skill de produção audiovisual já existente no hub (ver agente `audiovisual-producao-de-video` e as skills `audiovisual-*`), seguindo o padrão de pedido em linguagem natural ("crie um vídeo de 16:9 e outro de 9:16 para esta campanha"), sem inventar ferramentas, pacotes npm ou IDs de composição de outro projeto.
