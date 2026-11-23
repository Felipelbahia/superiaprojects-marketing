# Canibalização de palavras-chave

Duas ou mais páginas do mesmo site disputando a mesma intenção de busca. O buscador alterna entre elas, divide sinais (links, cliques) e às vezes mostra a página errada. Origem: agente `seo-cannibalization-detector` do 0 Padrões, reescrito para o hub (arquivo original em `.agents/agents/_arquivo/seo-0-padroes/`).

## Quando usar

- Antes de publicar um post novo: o assunto já tem página?
- Posição que oscila sem motivo, ou a URL "errada" ranqueando para a consulta.
- Auditoria de um blog com muitos posts sobre o mesmo tema.

## Sobreposição não é sempre problema

Duas páginas com a mesma palavra-chave **e intenções diferentes** convivem bem (ex.: "o que é press release" e "modelo de press release"). O problema é **mesma intenção**: as duas tentam responder à mesma pergunta do mesmo jeito.

## Diagnóstico (nesta ordem)

1. **Mapa palavra-chave → URL.** Liste a palavra-chave principal de cada página. Duas páginas com a mesma principal já são suspeitas.
2. **Dado real, se houver.** No Search Console, filtre por consulta e veja, na aba Páginas, quais URLs recebem impressões para ela. Duas URLs com impressões na mesma consulta confirmam o conflito. **Sem acesso ao Search Console, diga isso no relatório:** a análise passa a ser só de conteúdo e não prova ranking.
3. **Intenção.** Abra a busca e veja o que o buscador mostra (guia, lista, produto, definição). Compare com o que cada página entrega.
4. **Sinais de conflito.**

| Onde | Sinal |
|---|---|
| Título, H1, meta description | Quase iguais ou com a mesma palavra-chave na mesma posição |
| Estrutura | Mesmos H2 na mesma ordem |
| Conteúdo | Mesmos subtemas, mesmo nível de profundidade |
| Links internos | Âncoras idênticas apontando para páginas diferentes |

## Resolução

| Situação | Ação |
|---|---|
| Mesma intenção, uma página claramente mais fraca | **Consolidar**: levar o que presta para a forte, redirecionar a fraca com 301, atualizar links internos |
| Mesma intenção, as duas têm valor | **Diferenciar**: dar a cada uma um ângulo e uma intenção própria (reescrever título, H1, abertura e H2) |
| Intenções na verdade diferentes | Só **ajustar título, meta e âncoras** para deixar a diferença clara |
| Conteúdo quase duplicado que precisa continuar existindo (ex.: versão para impressão) | **Canonical** para a principal. Canonical não resolve páginas de intenção distinta |

Depois da ação: ajustar âncoras dos links internos para a página que deve ranquear, atualizar o sitemap e acompanhar as posições por algumas semanas.

## Formato do relatório

```
Conflito: [palavra-chave]
Páginas: A [URL] (impressões X) | B [URL] (impressões Y)   ← ou "sem dados de posição"
Intenção A / B: ...
Decisão: consolidar | diferenciar | ajustar | canonical
Próximos passos: ...
```

## Prevenção

- Mantenha o mapa palavra-chave → URL junto do calendário editorial; uma principal por página.
- Antes de publicar, consulte o mapa palavra-chave → URL e confira se a palavra-chave principal já tem página. O workflow `conteudo-pre-publicacao` cuida só de categorias, tags e metadados (título, descrição, keyphrase) e não faz essa checagem.
- Clusters com pilar e satélites já separam intenções: ver [topic-cluster-templates](../../seo-palavras-chave/references/topic-cluster-templates.md) e [content-decay-signals](content-decay-signals.md) para o que fazer com post antigo que perdeu posição.
