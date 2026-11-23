---
# Repository: https://github.com/Felipelbahia/superiaprojects-marketing
# Status: Customizada / Modificada localmente por Felipe Bahia
name: site-arquitetura
description: "Use para planejar ou reestruturar a estrutura de um site: hierarquia de páginas, mapa do site (sitemap visual), padrão de URLs, menu, rodapé, breadcrumbs, navegação no celular e plano de links internos. Traz modelos prontos por tipo de site (SaaS, blog, e-commerce, documentação, híbrido, negócio local). Gatilhos: \"estrutura do site\", \"mapa do site\", \"arquitetura de informação\", \"menu do site\", \"URLs\", \"breadcrumb\", \"links internos\", \"planejar o site\". NÃO use para sitemap XML e rastreamento (use seo-tecnico), para páginas em escala por template (use seo-programatico), para dados estruturados (use seo-schema-markup), para o design visual das páginas (use site-interface-de-conversao) nem para o texto da página (use copy-landing-page)."
author: Antigravity Multi-IA Hub & Felipe Bahia (Futuro Mercado)
license: MIT
metadata:
  author: Antigravity Multi-IA Hub & Felipe Bahia (Futuro Mercado)
  version: 1.0.0
---
# Arquitetura de Site

Primeiro passo de quem vai criar ou reestruturar um site: decidir **quais páginas existem, como se chamam, onde ficam e como se ligam**, antes de desenhar ou escrever qualquer uma. Os guias são em inglês; a entrega ao usuário sai em português.

## Quando usar

- Criar um site novo (institucional, SaaS, blog, loja, documentação, negócio local).
- Reestruturar um site existente: página enterrada, menu confuso, URLs bagunçadas, links internos fracos.
- Montar o mapa do site antes de [site-construcao-de-site](../../workflows/site-construcao-de-site.md).

## Quando NÃO usar

Ver a descrição. Para uma **landing page única**, o mapa é trivial: vá direto a [site-construcao-de-landing-page](../../workflows/site-construcao-de-landing-page.md).

## Como trabalhar

1. **Marca e contexto** (regra 1.1): ler `_brands/<marca>/` e perguntar o que falta: o que a empresa faz, públicos, 3 metas do site (conversão, tráfego orgânico, educação, suporte), site novo ou reestruturação, URLs a preservar, quantas páginas, quais as 5 mais importantes.
2. **Escolher o tipo de site** e partir do modelo em [site-type-templates.md](references/site-type-templates.md).
3. **Desenhar a hierarquia** (regra dos 3 cliques, plano ou profundo) e o padrão de URLs em [site-architecture.md](references/site-architecture.md).
4. **Definir navegação** (menu, rodapé, barra lateral, breadcrumbs, celular, o que evitar) em [navigation-patterns.md](references/navigation-patterns.md).
5. **Desenhar o plano de links internos** (sem página órfã, âncora descritiva, hub e satélites).
6. **Entregar** as cinco peças do `site-architecture.md`: árvore ASCII, sitemap visual em Mermaid ([modelos](references/mermaid-templates.md)), tabela de URLs, especificação de navegação e plano de links. Salvar seguindo a regra de resolução de destino da skill `mapa-de-destinos` (`content/<marca>/site/AAAA-MM-DD - Nome da Demanda/arquitetura.md` no 0 Mkt; `conteudos/site/AAAA-MM-DD - Nome da Demanda/arquitetura.md` em projeto próprio).

## Guias

| Preciso de... | Leia |
|---|---|
| Método completo: contexto, hierarquia, URLs, links internos, formato de entrega | [site-architecture.md](references/site-architecture.md) |
| Árvore, tabela de URLs e menu prontos para cada tipo de site | [site-type-templates.md](references/site-type-templates.md) |
| Menu, rodapé, barra lateral, breadcrumbs (com marcação), celular, antipadrões, navegação para SEO | [navigation-patterns.md](references/navigation-patterns.md) |
| Diagramas Mermaid de sitemap (zonas de navegação, hub e satélites, antes e depois, cores) | [mermaid-templates.md](references/mermaid-templates.md) |

## Atenção ao caso brasileiro

Os modelos são genéricos e em inglês. Ao aplicar: URLs em português sem acento e com hífen (`/precos`, `/blog/guia-de-seo`); botão de WhatsApp como CTA secundário de negócio local; páginas de política de privacidade e termos (LGPD, ver [geral-conformidade-lgpd](../geral-conformidade-lgpd/SKILL.md)); página de captura sem menu quando a meta é conversão.

## Onde isso se conecta

- Design das páginas: [site-interface-de-conversao](../site-interface-de-conversao/SKILL.md).
- Texto: [copy-landing-page](../copy-landing-page/SKILL.md); conteúdo e clusters: [conteudo-estrategia](../conteudo-estrategia/SKILL.md).
- SEO técnico e dados estruturados: [seo-tecnico](../seo-tecnico/SKILL.md), [seo-schema-markup](../seo-schema-markup/SKILL.md), [seo-programatico](../seo-programatico/SKILL.md).
- Construção: workflows [site-construcao-de-site](../../workflows/site-construcao-de-site.md) e [site-construcao-de-landing-page](../../workflows/site-construcao-de-landing-page.md).
