# Featured snippets e "As pessoas também perguntam": como escolher o formato

Guia de decisão. Os **modelos de bloco** (definição, passo a passo, tabela, FAQ) e as faixas de tamanho estão em [content-patterns.md](content-patterns.md); a regra de "resposta primeiro" está em [seo-conteudo/SKILL.md](../SKILL.md) (BLUF); blocos citáveis para respostas de IA estão em [quotable-content-examples](../../seo-geo/references/quotable-content-examples.md). Aqui fica só o que decide **qual** formato usar. Origem: agente `seo-snippet-hunter` do 0 Padrões (original em `.agents/agents/_arquivo/seo-0-padroes/`). Nada garante a exibição: o buscador escolhe.

## Antes de escrever

1. **Veja o que a busca já mostra** para a pergunta (parágrafo, lista ou tabela). Copie o formato, não o texto.
2. **Use a pergunta como título da seção** (H2 ou H3), com as palavras que as pessoas usam.
3. **Responda logo abaixo**, sem preâmbulo.

## Qual formato para qual pergunta

| Tipo de pergunta | Formato | Modelo em content-patterns.md |
|---|---|---|
| "O que é…", "Quem é…" | Parágrafo de definição | Definition Block |
| "Como fazer…", "Passo a passo" | Lista numerada, título antes da lista | Step-by-Step Block |
| "Quais são…", "Tipos de…" | Lista com marcadores | Listicle Block |
| "X ou Y?", "Diferença entre…", preços | Tabela | Comparison Table Block |
| Perguntas relacionadas do mesmo tema | Uma seção curta por pergunta | FAQ (faixa de palavras definida lá) |

## Exemplo

Antes (a definição só chega depois de uma volta):

> Existem muitas definições e, na prática, cada assessoria usa o termo de um jeito, mas de modo geral dá para dizer que um press release é um texto que…

Depois:

```markdown
## O que é um press release?
Press release é um texto curto que uma empresa envia à imprensa para divulgar uma novidade, como um lançamento, uma rodada de investimento ou uma mudança relevante. Ele traz título, lide, corpo, citação do porta-voz e contato de imprensa.
```

## Cuidados

- Use só perguntas que existem de verdade (busca, Search Console, dúvidas reais de clientes). Dado ou número na resposta precisa de fonte; sem fonte, marque `[a confirmar]`.
- O texto continua na voz da marca (`brand-voice.md`) e passa pelo `geral-anti-slop`. Resposta direta não é resposta robótica.
- Não encha a página de blocos de pergunta e resposta só para caçar snippet: um por seção que realmente responde algo.
- Marcação `FAQPage`: [seo-schema-markup](../../seo-schema-markup/SKILL.md). O Google **aposentou o FAQ rich result em 2026-05-07**; a marcação não tem efeito visível lá. Pergunta e resposta em seções curtas continuam valendo como conteúdo. Fonte: [regras de referência](../../seo-on-page/references/regras-de-referencia-google.md).
- Para ser citado por respostas geradas por IA, a lógica é parecida: ver [seo-geo](../../seo-geo/SKILL.md).
