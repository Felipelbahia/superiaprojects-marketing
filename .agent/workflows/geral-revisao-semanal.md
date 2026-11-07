---
name: geral-revisao-semanal
description: Gera a revisão semanal de marketing e o planejamento da semana seguinte. Use para revisar métricas da semana, status de campanhas e conteúdo, e planejar as prioridades da próxima semana.
allowed-tools: Read, Write, Edit, Bash
---

# Revisão Semanal de Marketing

> Workflow estruturado para a revisão semanal de desempenho e planejamento, no padrão do Hub Super IA Projects - Marketing`0 Mkt`.

---

## 1. O que este workflow faz

Compila a revisão da semana: métricas de desempenho, status das campanhas ativas, conteúdo publicado e pendente, e prioridades da semana seguinte. Ele verifica:
1. Conteúdo publicado e em rascunho na pasta definida pela regra de resolução da skill `geral-arquitetura-de-projeto` (`content/<marca>/` no 0 Mkt; `conteudos/` em projeto próprio).
2. Tarefas e planos abertos em `.agent/plans/`.
3. Status de campanhas ativas (tráfego pago, testes A/B, lançamentos).

---

## 2. Como executar

```
/geral-revisao-semanal
```
Ou com parâmetros contextuais:
```
/geral-revisao-semanal --brand plus-pr --semana 2026-10-27
```

Se faltar a marca, perguntar antes de seguir (regra 1.1 do `CLAUDE.md`).

---

## 3. Instruções de execução passo a passo

### Fase 1: Coleta de dados
1. Confirmar a marca e a semana a revisar.
2. Reunir métricas de desempenho da semana (tráfego, leads, conversões) — se uma fonte não estiver disponível, marcar "⚠️ sem dado".
3. Listar o status das campanhas ativas e do conteúdo (publicado, em revisão, pendente de aprovação).

### Fase 2: Estruturação da revisão

```markdown
# 📅 Revisão Semanal de Marketing — [Marca] — Semana de [data]

## Métricas de Desempenho
[Tráfego, leads, conversões — com comparação à semana anterior]

## Status das Campanhas
[Campanhas ativas e o que mudou nesta semana]

## Conteúdo da Semana
- **Publicado:** [lista]
- **Em revisão/pendente de aprovação:** [lista]

## Prioridades da Próxima Semana
1. [Prioridade 1]
2. [Prioridade 2]
3. [Prioridade 3]
```

### Fase 3: Apresentação e ação

Apresentar a revisão ao usuário e perguntar se quer já montar o planejamento detalhado da próxima semana (ver `/geral-planejamento-diario` dia a dia, se for o caso).

---

## Onde salvar

Seguir o mapa de destinos do projeto (`docs/mapa-de-destinos.md`; regra de resolução da skill `geral-arquitetura-de-projeto`), tipo de peça `reports`: `content/<marca>/reports/AAAA-MM-DD - Revisao Semanal/relatorio.md` no 0 Mkt (regra 1.4 do `CLAUDE.md`); `conteudos/reports/AAAA-MM-DD - Revisao Semanal/relatorio.md` em projeto próprio.
