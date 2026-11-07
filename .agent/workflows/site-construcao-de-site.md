---
name: site-construcao-de-site
description: "Constrói um site de várias páginas para uma marca de _brands/: arquitetura (mapa, URLs, menu), design system a partir dos tokens da marca, páginas na ordem de importância (cada uma pelo /build-landing-page), SEO técnico básico e teste no navegador. Gatilhos: \"crie o site\", \"monte o site institucional\", \"site de várias páginas\", \"reestruture o site\". Para uma única página use /build-landing-page."
argument-hint: "[marca] [tipo de site] [metas]"
---

# Build Site

Procedimento com **portões de aprovação**, para site de **mais de uma página** (institucional, SaaS, blog, loja, negócio local). Uma página só: use [build-landing-page](build-landing-page.md). O agente que conduz é o [site-construcao-web](../agents/site-construcao-web.md).

## Antes de tudo

- **Marca (regra 1.1):** sem marca clara, **pare e pergunte**; leia `_brands/<marca>/` e `design-system/tokens.json` se existir.
- **Socratic Gate (seção 3.2):** marca e persona, tipo de site, metas (conversão, tráfego orgânico, educação, suporte), páginas que já existem e URLs a preservar, o que já é conhecido de concorrentes e do conteúdo. Plano em `.agent/plans/`.
- **Reestruturando um site existente?** Antes de propor qualquer mudança, rode [site-auditoria-de-interface](../skills/site-auditoria-de-interface/SKILL.md) (ler o estado atual, não duplicar).

## Passos

| # | Passo | O que fazer | Skill | Portão |
|---|---|---|---|---|
| 1 | **Arquitetura** | Hierarquia, URLs, menu, rodapé, breadcrumbs e plano de links internos; entregar as 5 peças (árvore, sitemap em Mermaid, tabela de URLs, navegação, links) | [site-arquitetura](../skills/site-arquitetura/SKILL.md) | Usuário aprova o mapa |
| 2 | **Conteúdo por página** | Lista de páginas com meta, palavra-chave principal e CTA de cada uma; ordem de produção por importância (home, oferta, preço, contato, depois o resto). Clusters e blog: [conteudo-estrategia](../skills/conteudo-estrategia/SKILL.md), [seo-palavras-chave](../skills/seo-palavras-chave/SKILL.md) | [conteudo-estrategia](../skills/conteudo-estrategia/SKILL.md) | Usuário aprova a lista |
| 3 | **Design system** | Se a marca já tem `design-system/`, usar. Se não, **parar e propor** rodar a skill [brand-design-system](../skills/brand-design-system/SKILL.md) (é a etapa 7 do `brand-builder`), antes de desenhar páginas | [brand-design-system](../skills/brand-design-system/SKILL.md) | Tokens aprovados |
| 4 | **Cada página** | Para cada página, em ordem: passos 1 a 4 do [build-landing-page](build-landing-page.md) (brief, estrutura, copy com anti-slop, design). Menu, rodapé e componentes repetidos saem uma vez só | [copy-landing-page](../skills/copy-landing-page/SKILL.md), [site-interface-de-conversao](../skills/site-interface-de-conversao/SKILL.md) | Aprovação por página |
| 5 | **PORTÃO DA REGRA 1.5** | **"Posso gerar o código do site?"** e o formato: projeto novo (Astro ou Next.js), HTML estático ou componentes para um projeto existente. Sem o "sim" explícito, entregar só arquitetura, copy e wireframes em texto | — | **Autorização explícita** |
| 6 | **Código** | Conferir versões no lockfile e no Context7 (regra 2.8). Layout compartilhado, páginas, `<title>` e meta description únicos, canonical, `robots`, `sitemap.xml`, dados estruturados ([seo-schema-markup](../skills/seo-schema-markup/SKILL.md)) e checagem técnica ([seo-tecnico](../skills/seo-tecnico/SKILL.md)). Código React/Next: [site-react-desempenho](../skills/site-react-desempenho/SKILL.md) e [site-react-composicao](../skills/site-react-composicao/SKILL.md) | [site-tailwind-design-system](../skills/site-tailwind-design-system/SKILL.md) | Usuário vê o resultado |
| 7 | **Teste** | Passo 7 do `build-landing-page` em **cada** página (375 e 1440 px, console, Lighthouse) e nos links internos (nenhum 404, nenhuma página órfã) | — | Evidência |
| 8 | **Revisão de conversão** | `site-cro` nas páginas de conversão (home, oferta, preço, contato) | [site-cro](../skills/site-cro/SKILL.md) | Nota ≥ 8 |
| 9 | **Entrega** | Relatório do que foi e do que **não** foi verificado. **Publicar e apontar domínio só se o usuário pedir** (Vercel) | — | — |

## Onde salvar

Seguir o mapa de destinos do projeto (`docs/mapa-de-destinos.md`; regra de resolução da skill `geral-arquitetura-de-projeto`). Esse tipo não tem linha no mapa do 0 Mkt: use o tipo mais próximo e avise (regra 8). Hoje: `content/<marca>/site/AAAA-MM-DD - Nome da Demanda/` no 0 Mkt (regra 1.4 do `CLAUDE.md`); `conteudos/site/AAAA-MM-DD - Nome da Demanda/` em projeto próprio. Dentro da pasta: `arquitetura.md`, `paginas/` (uma pasta por página, como no `build-landing-page`), código, `capturas/` e `relatorio.md`.

## Limites

Não migra nem altera site em produção, não mexe em DNS, não conecta formulários, CRM ou e-mail reais e não inventa prova social sem autorização e dado real.
