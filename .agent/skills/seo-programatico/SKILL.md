---
# Repository: https://github.com/Felipelbahia/superiaprojects-marketing
# Status: Customizada / Modificada localmente por Felipe Bahia
name: seo-programatico
description: "Use para criar páginas de SEO em escala a partir de modelos e dados (SEO programático): páginas de comparação, de localidade, de integração, de glossário, diretórios e templates com padrões de título, links internos e schema, sem cair em conteúdo raso. Gatilhos: \"SEO programático\", \"páginas em escala\", \"template de página\", \"centenas de páginas\", \"páginas de cidade ou de categoria\". NÃO use para escrever um artigo único otimizado (use seo-conteudo), para auditar uma página (use seo-on-page) nem para diagnóstico técnico de indexação (use seo-tecnico)."
author: Antigravity Multi-IA Hub & Felipe Bahia (Futuro Mercado)
license: MIT
metadata:
  author: Antigravity Multi-IA Hub & Felipe Bahia (Futuro Mercado)
  version: 1.0.0
---
# SEO Programático

Reúne os três guias de páginas em escala que estavam dentro de `seo-conteudo`. O texto base é inglês, exceto onde indicado.

## Qual guia usar

| Preciso de... | Leia |
|---|---|
| Os princípios e a arquitetura: quais tipos de página, como escolher o padrão e como evitar conteúdo duplicado ou raso | [programmatic-seo.md](references/programmatic-seo.md) |
| Modelos prontos de página: padrões de título, links internos, schema e estrutura (em português) | [programmatic-seo-builder.md](references/programmatic-seo-builder.md) |
| Colocar no ar: mapear o conjunto de dados, gerar, validar e publicar | [pseo-implementation-guide.md](references/pseo-implementation-guide.md) |

## Como trabalhar

1. Defina o padrão de busca (o que as pessoas procuram em escala) e confirme que há dado próprio para cada página; sem dado único, não faça.
2. Escolha o modelo no `programmatic-seo-builder` e valide uma página-piloto antes de gerar o lote.
3. Gere o schema com [seo-schema-markup](../seo-schema-markup/SKILL.md) e confira o rastreio e a indexação com [seo-tecnico](../seo-tecnico/SKILL.md).
4. Texto entregue passa pelo fluxo de `/geral-anti-slop`; salve seguindo a regra de resolução de destino da skill `geral-arquitetura-de-projeto` (pasta do canal, conforme o mapa do projeto ou o padrão sem mapa).

## Onde isso se conecta

- Artigo único e pesquisa de intenção: [seo-conteudo](../seo-conteudo/SKILL.md).
- Auditoria da página gerada: [seo-on-page](../seo-on-page/SKILL.md).
