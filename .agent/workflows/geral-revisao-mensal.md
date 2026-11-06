---
name: geral-revisao-mensal
description: Gera a revisão mensal de desempenho de marketing e ajuste de estratégia para o mês seguinte. Use para compilar métricas do mês, analisar funil e canais, e planejar o próximo mês.
allowed-tools: Read, Write, Edit, Bash
---

# Revisão Mensal de Marketing

> Workflow estruturado para a revisão mensal de desempenho, cobrindo métricas, funil, canais e planejamento do mês seguinte, no padrão do Hub Super IA Projects - Marketing`0 Mkt`.

---

## 1. O que este workflow faz

Compila a revisão mensal de marketing: métricas do mês (com comparação mês a mês e ano a ano), desempenho do funil, análise por canal e metas do próximo mês. Ele verifica:
1. Métricas de campanhas e conteúdo na pasta definida pela regra de resolução da skill `geral-arquitetura-de-projeto` (`content/<marca>/` no 0 Mkt; `conteudos/` em projeto próprio).
2. Dados em `.agent/plans/` sobre tarefas e campanhas do mês.
3. Benchmarks já registrados (se houver) para comparar o desempenho.

---

## 2. Como executar

```
/geral-revisao-mensal
```
Ou com parâmetros contextuais:
```
/geral-revisao-mensal --brand pr-pulse --mes 2026-10
```

Se faltar a marca ou o mês, perguntar antes de seguir (regra 1.1 do `CLAUDE.md`).

---

## 3. Instruções de execução passo a passo

### Fase 1: Coleta de dados
1. Confirmar a marca e o mês a revisar.
2. Reunir as métricas disponíveis do mês (campanhas, funil, canais) — se uma fonte de dados não estiver disponível, marcar como "⚠️ sem dado" em vez de inventar número.
3. Comparar com o mês anterior e, se houver, com o mesmo mês do ano anterior.

### Fase 2: Estruturação da revisão

```markdown
# 📊 Revisão Mensal de Marketing — [Marca] — [Mês/Ano]

## Resultados-Chave
| Métrica | Real | Meta | Vs. mês anterior | Status |
|---|---|---|---|---|
| [métrica] | [valor] | [meta] | [variação] | 🟢/🟡/🔴 |

## Desempenho do Funil
[Taxas de conversão por etapa, qualidade de lead, tendência]

## Desempenho por Canal
[Canais pagos, orgânicos e de e-mail, com o que funcionou e o que não funcionou]

## 3 Principais Vitórias do Mês
1. [Vitória com o impacto medido]

## Metas do Próximo Mês
1. [Meta específica e mensurável]
2. [Meta específica e mensurável]
```

### Fase 3: Apresentação e ação

Apresentar a revisão ao usuário e perguntar quais metas do próximo mês entram no planejamento de campanhas (ver `revenue-campanhas`).

---

## Onde salvar

Seguir a regra de resolução de destino da skill `geral-arquitetura-de-projeto`: `content/<marca>/relatorios/AAAA-MM - Revisao Mensal/relatorio.md` no 0 Mkt (regra 1.4 do `CLAUDE.md`); `conteudos/relatorios/AAAA-MM - Revisao Mensal/relatorio.md` em projeto próprio.
