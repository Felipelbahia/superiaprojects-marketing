---
name: geral-planejamento-diario
description: Gera um planejamento diário estruturado por blocos de tempo e energia (ritmo circadiano e GTD) para profissionais e líderes de marketing.
allowed-tools: Read, Write, Edit
---

# Plan My Day (Marketing Productivity Edition)

> Planejamento diário inteligente de tempo e foco, combinando ritmo circadiano, princípios GTD e prioridades táticas de marketing.

---

## 1. O que este Workflow faz
Estrutura uma agenda horária realista e focada para o dia, combinando tarefas de alta carga cognitiva (estratégia, redação de copy, análise de funil) com horários de pico mental, e alocando reuniões e tarefas operacionais nos vales de energia.

---

## 2. Como Executar

```
/plan-my-day
```
Ou com personalização de foco:
```
/plan-my-day --focus "Campanha de Lançamento Plinq" --peak 09-12
```

---

## 3. Princípios Operacionais de Produtividade

1. **Otimização Circadiana**: A capacidade analítica e criativa atinge o ápice ~2-3 horas após acordar.
2. **Ciclos Ultradianos**: Blocos de foco máximo de 90 minutos seguidos de 15 minutos de descanso.
3. **Prevenção da Fadiga de Decisão**: Decisões de investimento de mídia e revisões de copy complexas devem ocorrer antes das 15h.
4. **Regra 1-3-5**:
   - 1 Grande Meta Estratégica do Dia.
   - 3 Tarefas Médias Importantes.
   - 5 Tarefas Rápidas / Administrativas.

---

## 4. Roteiro Passo a Passo

### Passo 1: Triagem de Demandas
Perguntar ou identificar:
- Qual é a **#1 Prioridade Absoluta** (se você só fizesse isso hoje, o dia teria valido a pena)?
- Quais são as entregas secundárias e prazos de clientes/marcas?
- Quais reuniões ou compromissos fixos já estão na agenda?

### Passo 2: Estruturação da Grade Horária
Montar o bloco do dia:

```markdown
# 📅 Plano Diário de Alta Performance — [Data: YYYY-MM-DD]

### 🎯 A Grande Meta do Dia
> **[Meta Principal - ex: Finalizar e revisar a Landing Page de captura da marca X]**

---

### ⏰ Grade Horária Otimizada por Energia

| Horário | Bloco de Energia | Tipo de Atividade | Entrega Esperada |
|---|---|---|---|
| **09:00 - 10:30** | ⚡ Pico Máximo (Deep Work) | Redação / Estratégia | Copy principal ou arquitetura de campanha |
| **10:30 - 10:45** | ☕ Pausa de Recuperação | Desconexão de tela | Caminhada leve, água |
| **10:45 - 12:00** | ⚡ Pico Secundário | Análise / Otimização | Auditoria de métricas e testes A/B |
| **12:00 - 13:30** | 🥗 Almoço & Reset | Descanso | Desconexão mental |
| **13:30 - 15:00** | 🔨 Foco Operacional | Produção & Setup | Configuração de tags, criativos e carrosséis |
| **15:00 - 15:15** | ☕ Pausa de Recuperação | Respiração | Café, pausa rápida |
| **15:15 - 16:30** | 👥 Alinhamentos & Reuniões | Comunicação | 1-on-1s, syncs de time e feedback de clientes |
| **16:30 - 17:30** | 📥 Caixa de Entrada & Admin | Inbox Zero | E-mails, mensagens rápidas, agendamento |
| **17:30 - 18:00** | 🏁 Fechamento & Shutdown | Revisão & Handoff | Checklist de pendências e planejamento de amanhã |

---

### 🛡️ Guardrails do Dia
- [ ] Celular em modo foco durante os blocos da manhã.
- [ ] Não abrir e-mail ou mensagens antes de avançar na Prioridade #1.
- [ ] Validar qualquer copy final pelo `/ai-slop-detector`.
```

### Passo 3: Fechamento Noturno (Evening Shutdown)
Ao final do dia, revisar rapidamente o que foi concluído e salvar anotações de continuidade.
