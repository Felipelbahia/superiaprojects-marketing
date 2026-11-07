---
name: data-revisao-mensal
description: Gera a revisão analítica mensal (tráfego, conversão, desempenho de conteúdo e campanhas) com comparação ao mês anterior. Use para consolidar os aprendizados do mês e definir prioridades do próximo.
allowed-tools: Read, Write, Edit, Bash
---

# Revisão Analítica Mensal

> Workflow estruturado para a revisão mensal de analytics, no padrão do Hub Super IA Projects - Marketing `0 Mkt`.

---

## 1. O que este workflow faz

Compila a análise do mês: tráfego por canal, funil de conversão, desempenho de conteúdo e campanhas, principais aprendizados e plano de ação para o mês seguinte. Verifica:

1. A marca e o mês/período a revisar.
2. Os dados disponíveis (Google Analytics, Search Console ou os relatórios já salvos em `content/<marca>/reports/`).
3. O relatório do mês anterior, para a comparação MoM.

---

## 2. Como executar

```
/data-revisao-mensal
```
Ou com parâmetros contextuais:
```
/data-revisao-mensal --marca pr-pulse --mes 2026-10
```

Se faltar a marca, perguntar antes de seguir (regra 1.1 do `CLAUDE.md`).

---

## 3. Instruções de execução passo a passo

### Fase 1: Coleta de dados
- [ ] Exportar os dados de analytics do período
- [ ] Reunir métricas por canal (orgânico, pago, social, e-mail)
- [ ] Reunir dados de conversão e funil
- [ ] Compilar os resultados de campanhas ativas no mês

### Fase 2: Análise

**Análise de tráfego**

| Fonte | Sessões | % do total | MoM | YoY |
|---|---|---|---|---|
| Busca orgânica | | | | |
| Direto | | | | |
| Busca paga | | | | |
| Social | | | | |
| E-mail | | | | |
| **Total** | | | | |

**Análise de conversão**

| Estágio | Volume | Taxa | MoM | Benchmark |
|---|---|---|---|---|
| Visitantes | | - | | |
| Leads | | % | | 3% |
| MQLs | | % | | 20% |
| SQLs | | % | | 30% |
| Clientes | | % | | 25% |

**Scorecard**

| KPI | Meta | Real | Status | Tendência |
|---|---|---|---|---|
| Tráfego | | | 🟢/🟡/🔴 | ↑/↓/→ |
| Leads | | | 🟢/🟡/🔴 | ↑/↓/→ |
| Receita | | | 🟢/🟡/🔴 | ↑/↓/→ |

### Fase 3: Geração de insights
- [ ] Identificar vitórias e desafios do mês
- [ ] Documentar aprendizados
- [ ] Definir prioridades

### Fase 4: Plano de ação
- [ ] Prioridades do próximo mês
- [ ] Recomendações de otimização
- [ ] Necessidades de recurso (tempo, verba, ferramenta)

---

## Delegação de agentes

| Tarefa | Agente | Gatilho |
|---|---|---|
| Compilação de dados | `data-analise-de-desempenho` | Revisão mensal |
| Análise de funil | `vendas-qualificacao-de-leads` | Revisão de conversão |
| Narrativa dos insights | `copy-redacao-publicitaria` | Redação do relatório |
| Recomendações | `revenue-planejamento-de-campanha` | Planejamento estratégico |

---

## Onde salvar

Seguir o mapa de destinos do projeto (`docs/mapa-de-destinos.md`; regra de resolução da skill `geral-arquitetura-de-projeto`), tipo de peça `reports`: `content/<marca>/reports/AAAA-MM-DD - Revisao Mensal [Mes-Ano]/relatorio.md` no 0 Mkt (regra 1.4 do `CLAUDE.md`); `conteudos/reports/AAAA-MM-DD - Revisao Mensal [Mes-Ano]/relatorio.md` em projeto próprio.
