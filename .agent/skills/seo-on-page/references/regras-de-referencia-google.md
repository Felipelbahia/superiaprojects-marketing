# Regras de referência de SEO: o que o Google diz e o que adotamos

Fonte única dos números que as skills `seo-*` repetem. Quando outra skill citar um tamanho, um limite ou um recurso do Google, o valor é o desta página. Consultado em **2026-11-17** nas páginas oficiais do Google (links abaixo). O que não foi possível confirmar fica marcado `[a confirmar]`.

Como ler a coluna **Status**: **oficial** = o Google afirma; **heurística da casa** = valor que adotamos por prática de mercado, sem regra do Google; **aposentado** = o recurso não existe mais.

## Tamanhos e formatos

| Tema | O que o Google diz | O que adotamos | Status |
|---|---|---|---|
| Título (`<title>`) | "While there's no limit on how long a `<title>` element can be, the title link is truncated in Google Search results as needed, typically to fit the device width." O Google também pode reescrever o título. [title-link](https://developers.google.com/search/docs/appearance/title-link) | Alvo de 50 a 60 caracteres (teto prático de ~60), com a informação principal no começo | heurística da casa |
| Meta description | "There's no limit on how long a meta description can be, but the snippet is truncated in Google Search results as needed, typically to fit the device width." O snippet nasce sobretudo do conteúdo da página. [snippet](https://developers.google.com/search/docs/appearance/snippet) | Alvo de 130 a 155 caracteres, com benefício e chamada para ação | heurística da casa |
| Resposta curta para snippet, "As pessoas também perguntam" e IA | Featured snippet: "You can't" pedir um; "Google does not provide an exact minimum length required to appear as a featured snippet." [featured-snippets](https://developers.google.com/search/docs/appearance/featured-snippets) | Resposta direta de 40 a 60 palavras logo abaixo da pergunta (H2/H3) | heurística da casa |
| Tamanho do texto | "there's no magical word count target, minimum or maximum" [seo-starter-guide](https://developers.google.com/search/docs/fundamentals/seo-starter-guide) | O tamanho vem do que a busca pede, não de um número | oficial |
| Densidade de palavra-chave | Não consta nas páginas consultadas; o guia diz que repetir as mesmas palavras "over and over" cansa o leitor | Sem alvo de densidade. Se a repetição soar forçada ao ler em voz alta, reescreva | oficial (ausência) + heurística |

## Recursos que mudaram

| Recurso | O que o Google diz | O que fazer | Status |
|---|---|---|---|
| FAQ rich result | 08/ago/2023: passa a aparecer "only... for well-known, authoritative government and health websites". 08/mai/2026: "This feature will no longer appear in Google Search starting May 7, 2026." 15/jun/2026: "The FAQ rich result feature is no longer shown in Google Search results", e a documentação foi removida. [blog 2023](https://developers.google.com/search/blog/2023/08/howto-faq-changes), [atualizações](https://developers.google.com/search/updates) | Não prometer FAQ rich result. Pergunta e resposta continuam úteis como conteúdo (leitor, snippet, IA). `FAQPage` é só marcação sem efeito visível no Google; benefício em outros buscadores ou em IA: `[a confirmar]` | aposentado |
| HowTo rich result | 08/ago/2023: só no desktop. Atualização de 14/set/2023 (vale a partir de 13/set): "Google Search no longer shows How-to rich results on desktop, which means this result type is now deprecated." [blog 2023](https://developers.google.com/search/blog/2023/08/howto-faq-changes) | Não prometer HowTo rich result | aposentado |
| Marcação sem uso | "While you can drop this structured data from your site, there's no need to proactively remove it." "Structured data that's not being used does not cause problems for Search" [blog 2023](https://developers.google.com/search/blog/2023/08/howto-faq-changes) | Não precisa remover marcação antiga | oficial |

## Limites técnicos

| Tema | O que o Google diz | Status |
|---|---|---|
| Core Web Vitals "bom" | LCP "within 2.5 seconds"; INP "200 milliseconds or less"; CLS "0.1 or less"; medido no percentil 75 das visitas, em celular e desktop. [web.dev/vitals](https://web.dev/articles/vitals), atualizado em 31/out/2024. FID foi substituído pelo INP e não é mais métrica de Core Web Vitals: usar INP | oficial |
| Sitemap | "limit a single sitemap to 50MB (uncompressed) or 50,000 URLs"; acima disso, vários sitemaps. [build-sitemap](https://developers.google.com/search/docs/crawling-indexing/sitemaps/build-sitemap) | oficial |
| robots.txt | "Google enforces a robots.txt file size limit of 500 kibibytes (KiB)"; o que passa disso é ignorado. [robots_txt](https://developers.google.com/search/docs/crawling-indexing/robots/robots_txt) | oficial |

## Como usar

- Ao escrever ou auditar, cite o valor desta página, não um número de memória. Se precisar de uma regra nova do Google, consulte a página oficial, cite a frase e a data aqui.
- Heurística da casa nunca é apresentada como exigência do Google. Em relatório, diga "referência de exibição" ou "boa prática".
- Estatística de exemplo em modelo de texto (ex.: "70% do tráfego vem do celular") precisa de fonte; sem fonte, marque `[exemplo, sem fonte]`.
- Revisar esta página a cada 6 meses ou quando o Google anunciar mudança em [atualizações da documentação](https://developers.google.com/search/updates).
