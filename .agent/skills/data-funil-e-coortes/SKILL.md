---
# Repository: https://github.com/Felipelbahia/superiaprojects-marketing
# Status: Customizada / Modificada localmente por Felipe Bahia
name: data-funil-e-coortes
description: "Use para analisar queda de funil (drop-off), retenção por coortes, ativação de usuários, onboarding e paywall em produtos digitais. Gatilhos: \"drop-off\", \"coorte\", \"ativação\", \"onboarding que não converte\", \"paywall\". NÃO use para tracking e GA4 (use data-web-ga4), atribuição e relatório executivo (use data-atribuicao-e-relatorios) nem para executar teste A/B (use growth-testes-ab)."
author: Antigravity Kit (0 Mkt) & Felipe Bahia (Futuro Mercado)
license: MIT
metadata:
  author: Antigravity Kit (0 Mkt) & Felipe Bahia (Futuro Mercado)
  version: 1.0.0
---
# Funnel & Cohort Analyst - Diretrizes Operacionais

Esta skill orienta o diagnóstico profundo de funis de conversão, análise longitudinal de retenção através de matrizes de coorte, aceleração do Time-to-Value (TTV) no onboarding e otimização de telas de paywall e upgrade em produtos digitais e plataformas SaaS.

---

## 🎯 Quando Usar
- Ao mapear gargalos e quedas de conversão (*drop-offs*) entre etapas de aquisição, cadastro e compra.
- Ao construir e interpretar tabelas de retenção por coortes (semanais ou mensais M0 a M12).
- Ao desenhar fluxos de onboarding com foco em ativação rápida e descoberta do momento "Aha!".
- Ao otimizar telas de paywall, comparativos de planos e mecânicas de upgrade de plano gratuito para pago.
- Ao diagnosticar as causas raiz de churn precoce (dias 1, 7 e 30).

## 🚫 Quando NÃO Usar
- Para testes A/B estatísticos de variantes visuais isoladas (use `growth-testes-ab`).
- Para auditoria de usabilidade e heurística de landing pages externas (use `site-cro`).
- Para atribuição de canais de mídia paga (use `data-atribuicao-e-relatorios`).

---

## 📉 1. Diagnóstico de Queda de Funil (Drop-off Analysis)

### 1.1. Estrutura de Funil Fechado vs. Aberto
- **Funil Fechado (Strict Funnel)**: O usuário deve passar obrigatoriamente por todos os passos na ordem exata $A \to B \to C \to D$. Ideal para checkouts e cadastros multi-step.
- **Funil Aberto (Open Funnel)**: O usuário pode entrar em qualquer etapa intermediária. Ideal para navegação de descoberta e catálogo.

### 1.2. Mapeamento de Fricção e Micro-Conversões
Para cada transição entre etapas, meça a Taxa de Passagem (*Pass-through Rate*):
$$\text{Pass-through Rate} = \frac{\text{Usuários que completaram o Passo } N+1}{\text{Usuários que iniciaram o Passo } N} \times 100$$

```
Etapa 1: Visita Página de Preços  (10.000 usuários) ──[100%]
   ↓ (Drop-off de 65% - Fricção na clareza da proposta de valor)
Etapa 2: Início de Cadastro       ( 3.500 usuários) ──[ 35%]
   ↓ (Drop-off de 20% - Fricção no número de campos)
Etapa 3: Verificação de Email     ( 2.800 usuários) ──[ 28%]
   ↓ (Drop-off de 45% - Barreira de cartão de crédito antecipado)
Etapa 4: Setup Concluído / Trial  ( 1.540 usuários) ──[15.4%]
```

---

## 👥 2. Matriz de Coortes e Análise de Retenção

### 2.1. Interpretação da Curva de Retenção

```
Retenção %
100% ────┐
         │
 40%     └──────── Curva Saudável (Platô / Assíntota Estável)
 15%     ─────────
         \
  0%      \_______ Curva Vazada (Decadência Contínua / Churn Crítico)
         ──────────────────────────────────────────────────
         M0     M1     M2     M3     M4     M5     M6 (Meses)
```

- **Platô Estável (Flat Line)**: Indica que o produto atingiu *Product-Market Fit* para um núcleo de usuários fiéis.
- **Curva Decadente até Zero**: Indica que o valor percebido não se sustenta; foco emergencial em retenção antes de investir mais em aquisição.

### 2.2. Exemplo de Matriz Mensal de Coorte (N-Day Retention)

| Coorte | Tamanho (M0) | M1 | M2 | M3 | M6 | M12 |
|---|---|---|---|---|---|---|
| **Jan 2026** | 1.200 | 48% | 38% | 34% | 31% | 29% |
| **Fev 2026** | 1.450 | 52% | 41% | 36% | 33% | - |
| **Mar 2026** | 1.800 | 55% | 44% | 39% | - | - |

---

## ⚡ 3. Framework de Ativação e Onboarding

### 3.1. A Tríade do Onboarding de Sucesso
1. **Setup Milestone**: A configuração técnica mínima para que o produto funcione (ex: convidar 1 colega, integrar o Slack).
2. **Aha! Moment**: O momento emocional em que o usuário experimenta pela primeira vez o benefício central do produto.
3. **Habit Formation**: O retorno recorrente do usuário (frequência natural de uso: diária, semanal ou mensal).

### 3.2. Estratégias de Aceleração do Time-to-Value (TTV)
- **Progressive Profiling**: Não colete todas as informações de perfil no cadastro; solicite dados contextualmente conforme o usuário explora módulos avançados.
- **Pre-populated Templates**: Nunca apresente telas vazias (*blank slate syndrome*); forneça dados de exemplo ou modelos pré-prontos clicáveis.
- **Checklist Interativo com Barra de Progresso**: Usuários são motivados pelo efeito de completude de tarefas (comece o checklist com 1 item já concluído: "Conta criada").

---

## 💳 4. Otimização de Paywalls e Upgrade Flows

### 4.1. Modelos de Barreira: Soft vs. Hard Paywall vs. Reverse Trial
- **Soft Paywall (Freemium)**: O usuário tem acesso perpétuo a recursos básicos; o paywall surge ao bater em limites de cota ou ao solicitar recursos enterprise.
- **Hard Paywall**: O acesso ao produto é 100% bloqueado até que haja assinatura ou inserção de cartão.
- **Reverse Trial**: O usuário começa com acesso total a todas as funcionalidades Pro por 14 dias sem cartão de crédito; ao fim, faz downgrade suave para o plano gratuito se não assinar.

### 4.2. Heurísticas de Design do Paywall de Alta Conversão
- **Ancoragem de Preço**: Destacar o plano Anual como o "Mais Popular" com cálculo do valor equivalente por mês (ex: "R$ 49/mês faturado anualmente") e badge de economia ("Economize 20%").
- **Tabela Comparativa Concisa**: Limitar a tabela a no máximo 5 a 7 linhas comparativas decisivas; evitar listas exaustivas de 40 itens técnicos.
- **Garantia Visível & Reversibilidade**: "Cancele a qualquer momento com 1 clique" e "Garantia incondicional de 30 dias" reduzem a ansiedade de compromisso financeiro.

### 4.3. Fluxo de Cancelamento Inteligente (Offboarding & Churn Prevention)
Não trate o cancelamento como uma ação binária imediata. Desenvolva um fluxo de retenção humanizado:
1. **Pausa Temporária da Conta**: Oferecer pausa de faturamento por 1 a 3 meses (ideal para clientes sazonais ou sobrecarregados).
2. **Oferta de Downgrade Contextual**: Se a queixa for preço, apresentar um plano "Lite" ou "Starter" com menor cota antes do encerramento.
3. **Pesquisa de Motivo com 1 Clique**: Mapear a causa real (preço, falta de tempo, bugs, falta de suporte) para alimentar o backlog de produto.
4. **Preservação de Dados**: Garantir que as configurações e dados históricos do usuário permanecerão salvos com segurança caso ele decida reativar no futuro.

---

## 📚 5. Biblioteca de Referências Operacionais

Consulte os manuais aprofundados na pasta `references/`:

| Arquivo de Referência | Conteúdo Principal & Uso Prático |
|---|---|
| [`activation-playbook.md`](references/activation-playbook.md) | Playbook de ativação de usuários: métricas de engajamento, gatilhos in-app e definição do Aha! Moment. |
| [`funnel-psychology.md`](references/funnel-psychology.md) | Heurísticas psicológicas que causam fricção ou aceleração ao longo das etapas de decisão. |
| [`onboarding-cro.md`](references/onboarding-cro.md) | Otimização de conversão específica para telas de boas-vindas, tours guiados e formulários de cadastro. |
| [`onboarding-guide.md`](references/onboarding-guide.md) | Guia completo de arquitetura de onboarding para produtos web e mobile. |
| [`onboarding-orchestrator.md`](references/onboarding-orchestrator.md) | Orquestração de canais combinados de onboarding: produto in-app + sequências de emails de ativação. |
| [`paywall-upgrade-cro.md`](references/paywall-upgrade-cro.md) | Princípios de conversão para telas de planos, páginas de checkout e CTAs de upgrade. |
| [`paywall-optimization-guide.md`](references/paywall-optimization-guide.md) | Casos práticos, benchmarks de conversão de paywall por nicho e testes de precificação. |

## Roteiros guiados (vindos do kit AgentKits)

Roteiros que fazem perguntas ao usuário antes de entregar. O texto base é inglês.

- **[funnel.md](references/funnel.md)** — Roteiro guiado para analisar a performance do funil de conversão.

## Referências vindas de outras skills

- **[experiments.md](references/experiments.md)** — Ideias de experimentos de onboarding (veio de `growth-testes-ab`).

## Scripts de cálculo

Programas em Python para funil e coorte (origem: pacote `@clawfu/mcp-skills`, licença MIT; revisados e testados em 2026-10-20 com dados de exemplo). Rode a partir da raiz do projeto, com o ambiente `.venv` (precisa só de `click`):

```bash
.venv/bin/python .agent/skills/data-funil-e-coortes/scripts/funnel_analyzer.py analyze eventos.csv --stages visita,cadastro,ativacao,compra
.venv/bin/python .agent/skills/data-funil-e-coortes/scripts/cohort_analysis.py retention dados.csv --date-col signup --event-col event
```

- `funnel_analyzer.py`: o CSV precisa ter as colunas `user_id` e `stage`; mostra usuários, conversão etapa a etapa e queda.
- `cohort_analysis.py`: o CSV traz uma coluna de data de entrada e outra do evento; agrupa por mês e mostra a retenção por período.
- **Datas:** aceita `aaaa-mm-dd`, `aaaa/mm/dd`, `dd/mm/aaaa` e `mm/dd/aaaa`, nessa ordem de tentativa. Com barras, `05/06/2026` vale 5 de junho. **Alterado em relação ao original**, que lia como 6 de maio (corrigido em 2026-10-20). Datas como `12/25/2026` ainda funcionam, pois 25 não é mês.
