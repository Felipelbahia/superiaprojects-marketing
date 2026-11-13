---
name: seo-checklist-semanal
description: Gera o checklist semanal de manutenção e otimização de SEO. Use para organizar as tarefas de SEO da semana por dia (rankings, saúde técnica, conteúdo, link building, concorrência).
allowed-tools: Read, Write, Edit, Bash
---

# Checklist Semanal de SEO

> Workflow estruturado para a manutenção semanal de SEO, no padrão do Hub Super IA Projects - Marketing `0 Mkt`.

---

## 1. O que este workflow faz

Organiza as tarefas de SEO da semana em blocos diários e monta o painel de métricas para acompanhar a evolução. Verifica:
1. A marca e o domínio/site em foco.
2. Ferramentas de SEO disponíveis (Search Console, Ahrefs/Semrush, se configurados via MCP).
3. Resultados da semana anterior, se houver relatório salvo em `content/<marca>/reports/` (0 Mkt) ou `conteudos/reports/` (projeto próprio).

---

## 2. Como executar

```
/seo-checklist-semanal
```
Ou com parâmetros contextuais:
```
/seo-checklist-semanal --marca pr-pulse --site pr-pulse.com
```

Se faltar a marca, perguntar antes de seguir (regra 1.1 do `CLAUDE.md`).

---

## 3. Instruções de execução passo a passo

### Segunda — Rankings e desempenho
- [ ] Revisar Search Console (cliques, impressões, CTR)
- [ ] Tirar snapshot do rastreamento de rankings
- [ ] Analisar tendência de tráfego orgânico

### Terça — Saúde técnica
- [ ] Revisar relatório de cobertura/indexação
- [ ] Checar erros de rastreamento
- [ ] Verificar Core Web Vitals

### Quarta — Otimização de conteúdo
- [ ] Identificar conteúdo com baixo desempenho
- [ ] Otimizar 1-2 páginas (ver workflow `/seo-otimizacao-de-conteudo` e skill `seo-on-page`)
- [ ] Mapear oportunidades de featured snippet

### Quinta — Link building
- [ ] Checar backlinks novos/perdidos
- [ ] Disparar 3-5 e-mails de outreach
- [ ] Atualizar linkagem interna

### Sexta — Concorrência e relatório
- [ ] Checar rankings dos concorrentes (ver workflow `/seo-analise-de-serp`)
- [ ] Pesquisar novas oportunidades de palavra-chave
- [ ] Compilar as métricas da semana

---

## Painel de métricas semanais

| Métrica | Esta semana | Semana anterior | Variação | Meta |
|---|---|---|---|---|
| Sessões orgânicas | | | | |
| Posição média | | | | |
| CTR | | | | |
| Palavras-chave no top 10 | | | | |
| Backlinks novos | | | | |

---

## Delegação de agentes

| Tarefa | Agente | Gatilho |
|---|---|---|
| Pesquisa de palavras-chave | `growth-atracao-de-leads` | Planejamento de conteúdo |
| Auditoria técnica | `seo-otimizacao-de-busca` | Saúde do site |
| Análise de concorrência | `revenue-pesquisa-de-mercado` | Gaps de conteúdo |
| Análise de desempenho | `data-analise-de-desempenho` | Revisão de rankings |

---

## Onde salvar

Seguir o mapa de destinos do projeto (`docs/mapa-de-destinos.md`; regra de resolução da skill `mapa-de-destinos`), tipo de peça `reports`: `content/<marca>/reports/AAAA-MM-DD - Checklist SEO Semanal/checklist.md` no 0 Mkt (regra 1.4 do `CLAUDE.md`); `conteudos/reports/AAAA-MM-DD - Checklist SEO Semanal/checklist.md` em projeto próprio.
