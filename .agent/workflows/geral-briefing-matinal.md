---
name: geral-briefing-matinal
description: Gera o briefing matinal consolidado de marketing e prioridades de conteúdo. Use para planejar o dia de trabalho, identificar pautas não publicadas e alinhar entregas prioritárias.
allowed-tools: Read, Write, Edit, Bash
---

# Daily Briefing Builder (Marketing Edition)

> Workflow estruturado para geração do briefing diário matinal de marketing, consolidando tarefas prioritárias, pautas de conteúdo pendentes e alertas de calendário.

---

## 1. O que este Workflow faz
Gera um resumo executivo limpo e acionável para o início da jornada de trabalho no Hub Super IA Projects - Marketing`0 Mkt`. Ele verifica:
1. Pautas e conteúdos em elaboração na pasta `content/`.
2. Tarefas e planos em andamento em `.agent/plans/`.
3. Prioridades de campanhas ativas e métricas críticas.
4. Previsão do dia e blocos de tempo para execução focada.

---

## 2. Como Executar

Invoque o comando:
```
/daily-briefing
```
Ou com parâmetros contextuais:
```
/daily-briefing --brand plinq --priority ads
```

---

## 3. Instruções de Execução Passo a Passo

### FASE 1: Coleta & Triagem de Contexto
1. Verificar a data atual do sistema.
2. Identificar a marca em foco (ou varrer as marcas ativas em `_brands/` se for um briefing geral).
3. Verificar a pasta de conteúdo definida pela regra de resolução da skill `mapa-de-destinos` (`content/<marca>/` no 0 Mkt; `conteudos/` em projeto próprio) para identificar:
   - Posts com rascunhos criados nos últimos 7 dias.
   - Entregas programadas ou aprovações pendentes.
4. Verificar `.agent/plans/` para tarefas abertas (`[TASK]`, `[PLAN]`).

### FASE 2: Estruturação do Briefing
Compilar o relatório matinal no seguinte formato padronizado:

```markdown
# ☀️ Briefing Matinal de Marketing — [Data: YYYY-MM-DD]

## 🎯 Top 3 Prioridades do Dia
1. [Tarefa Crítica 1 - ex: Finalizar copy da campanha X de Plinq]
2. [Tarefa Crítica 2 - ex: Auditar métricas de conversão de Waimonitor]
3. [Tarefa Crítica 3 - ex: Revisar e aprovar carrossel de LinkedIn]

---

## 📝 Status de Conteúdo & Pipeline
- **Em Rascunho / Revisão:** [Listar pastas recentes em content/]
- **Pautas Pendentes de Agendamento:** [Listar conteúdos aprovados]
- **Alertas de Campanhas:** [Status de testes A/B ou campanhas de tráfego]

---

## ⚡ Blocos de Energia Recomendados
- **Manhã (09h - 12h - Deep Work):** [Foco criativo / Redação de copy / Estratégia]
- **Tarde (14h - 16h - Operacional):** [Configuração de anúncios / Análise de métricas]
- **Fim de Tarde (16h - 18h - Comunicação):** [Follow-up de leads / Reuniões / Alinhamentos]

---

## 💡 Insight Rápido do Dia
> [Princípio ou insight tático de marketing extraído dos playbooks ativos]
```

### FASE 3: Apresentação & Ação
Apresentar o briefing ao usuário e perguntar:
*"Deseja iniciar pela Prioridade #1 ou quer que eu prepare o plano detalhado no `/plan-my-day`?"*
