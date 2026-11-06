---
name: site-construcao-de-landing-page
description: "Constrói uma landing page de conversão de ponta a ponta para uma marca de _brands/: brief, estrutura, copy (com filtro anti-slop), design a partir dos tokens da marca, código (só com autorização explícita), teste no navegador e revisão de conversão. Gatilhos: \"crie a landing page\", \"monte a página de captura\", \"construa a LP\", \"página de vendas pronta\". Para só o texto use /landing-page; para site com várias páginas use /build-site."
argument-hint: "[marca] [oferta] [público]"
---

# Build Landing Page

Procedimento com **portões de aprovação**. Cada passo só começa depois do ok do usuário no passo anterior. Orquestra skills que já existem; não cria conhecimento novo.

## Antes de tudo

- **Marca (regra 1.1):** se o pedido não disser a marca (`pr-pulse`, `plus-pr`, `experimentacao`), **pare e pergunte**. Leia `_brands/<marca>/`: `brand-voice.md`, `personas.md`, `content-pillars.md`, `style-guide.md`. Se existir `_brands/<marca>/design-system/tokens.json` (ver [brand-design-system](../skills/brand-design-system/SKILL.md)), ele é a fonte de cor, fonte e espaço.
- **Complexidade (Socratic Gate, seção 3.2 do `CLAUDE.md`):** confirme marca, persona, canal (a LP recebe tráfego de onde?), objetivo e CTA, pilar de conteúdo. Salve o plano em `.agent/plans/` antes de produzir texto.
- **Agentes:** [site-construcao-web](../agents/site-construcao-web.md) conduz; chama `copy-redacao-publicitaria`, `site-otimizacao-de-conversao` e `seo-otimizacao-de-busca` quando o passo pedir.

## Passos

| # | Passo | O que fazer | Skill | Portão |
|---|---|---|---|---|
| 1 | **Brief** | Meta única da página, público e nível de consciência, origem do tráfego (e o texto do anúncio ou e-mail que traz a pessoa), oferta, prova disponível (depoimentos, números reais), objeções, preço, garantia. Modelo no fim de [landing-page-copy.md](../skills/copy-landing-page/references/landing-page-copy.md) | [persona-icp](../skills/persona-icp/SKILL.md) | Usuário aprova o brief |
| 2 | **Estrutura** | Landing de uma página: escolher o framework (PAS, AIDA, BAB ou grade de recursos, ver [write-landing.md](../skills/copy-landing-page/references/write-landing.md)) e a ordem das seções. Se o pedido é mais que uma página, **pare e use [build-site](build-site.md)** | [copy-landing-page](../skills/copy-landing-page/SKILL.md) | Usuário aprova a ordem |
| 3 | **Copy** | Título (3 opções), subtítulo, seções, FAQ, CTA e microcopy, na voz da marca; **sem número ou depoimento inventado** (marcar "exemplo" se ainda não há prova real). Passar pelo [geral-anti-slop](../skills/geral-anti-slop/SKILL.md) (regra 1.3). Cuidados de LGPD: texto de consentimento do formulário e link de privacidade ([geral-conformidade-lgpd](../skills/geral-conformidade-lgpd/SKILL.md)) | [copy-landing-page](../skills/copy-landing-page/SKILL.md) | Usuário aprova a copy |
| 4 | **Design** | Hierarquia, cor, tipografia, espaço e componentes a partir dos tokens da marca; checklist de acessibilidade e celular (alvo de toque 48 px, contraste 4,5:1) | [site-interface-de-conversao](../skills/site-interface-de-conversao/SKILL.md) | Usuário aprova o wireframe em texto |
| 5 | **PORTÃO DA REGRA 1.5** | Pergunte literalmente: **"Posso gerar o código desta página?"** Também pergunte o formato: **(a)** um `index.html` único e autocontido (padrão: abre sem instalar nada) ou **(b)** componente para um projeto existente (Next.js, Astro). **Sem o "sim" explícito, o workflow termina aqui**, entregando copy + wireframe em texto | — | **Autorização explícita** |
| 6 | **Código** | Antes, conferir a versão de Tailwind e de React/Astro no `package.json` e no Context7 (regra 2.8). HTML semântico, um só `<h1>`, `alt` nas imagens, rótulos no formulário, meta title e description, marcação de FAQ se houver. Valores do CSS vindos de `tokens.json`; sem rastreamento nem fonte externa sem decisão do usuário. Guias: [site-tailwind-design-system](../skills/site-tailwind-design-system/SKILL.md), [tailwind-patterns](../skills/site-tailwind-design-system/references/tailwind-patterns.md), [write-landing.md](../skills/copy-landing-page/references/write-landing.md) | [site-tailwind-design-system](../skills/site-tailwind-design-system/SKILL.md) | Usuário vê o resultado |
| 7 | **Teste no navegador** | Com o MCP `chrome-devtools` (carregar com ToolSearch): abrir o arquivo (`file://`), capturar tela cheia, **375 px** e **1440 px** (`resize_page`), `list_console_messages` (sem erro), `lighthouse_audit`, conferir `scrollWidth <= clientWidth` e a medida dos alvos de toque. Guardar as capturas ao lado da página | — | Evidência de comando |
| 8 | **Revisão de conversão** | Auditoria com nota ([homepage-audit](../skills/site-cro/references/homepage-audit.md); se a página vem de anúncio, [landing-page-audit](../skills/site-cro/references/landing-page-audit.md)) pelo agente `site-otimizacao-de-conversao`. Corrigir o que for nota baixa e repetir o passo 7 | [site-cro](../skills/site-cro/SKILL.md) | Nota ≥ 8 ou usuário aceita o resto |
| 9 | **Entrega** | Relatório curto: o que foi feito, o que foi verificado **com evidência** e o que **não** foi (ex.: Safari iOS, leitor de tela, envio real do formulário, desempenho em rede lenta). Publicar (Vercel) **só se o usuário pedir** | — | — |

## Onde salvar

Seguir a regra de resolução de destino da skill `geral-arquitetura-de-projeto`: `content/<marca>/landing-pages/AAAA-MM-DD - Nome da Demanda/` no 0 Mkt (regra 1.4 do `CLAUDE.md`); `conteudos/landing-pages/AAAA-MM-DD - Nome da Demanda/` em projeto próprio. Dentro da pasta: `briefing.md`, `copy-opcao-1.md` (e `copy-opcao-2.md` se houver), `index.html` (ou os arquivos do componente), `capturas/` e `relatorio.md`. Nome da demanda com espaços, capitalizado.

## Limites

- Não mexe em site de produção nem publica sem pedido.
- Não conecta formulário a serviço real (CRM, e-mail) sem o usuário fornecer e autorizar a integração.
- Não inventa prova social, número ou garantia: marca o que é exemplo.
- Para alterar uma página que já existe, rode antes [site-auditoria-de-interface](../skills/site-auditoria-de-interface/SKILL.md).
