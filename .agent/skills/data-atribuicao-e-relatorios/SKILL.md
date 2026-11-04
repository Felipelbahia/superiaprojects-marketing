---
# Repository: https://github.com/Felipelbahia/superiaprojects-marketing
# Status: Customizada / Modificada localmente por Felipe Bahia
name: data-atribuicao-e-relatorios
description: Especialista em modelagem de atribuição multi-canal, geração de relatórios executivos de marketing, auditoria de saúde de contas e dashboards automatizados para liderança. Use para contar o resultado do marketing em todos os canais. NÃO use para decidir alocação de verba, pausar anúncios ou projetar ROAS de campanha (use ads-analise-de-desempenho), engenharia de tags GTM e dataLayer (use data-web-ga4), coortes e retenção in-app (use data-funil-e-coortes) nem execução de testes A/B (use growth-testes-ab).
author: Antigravity Kit (0 Mkt) & Felipe Bahia (Futuro Mercado)
license: MIT
metadata:
  author: Antigravity Kit (0 Mkt) & Felipe Bahia (Futuro Mercado)
  version: 1.0.0
---
# Marketing Attribution & Reporter - Diretrizes Operacionais

Esta skill orienta a análise comparativa de modelos de atribuição multi-toque (MTA), consolidação de métricas executivas de marketing (CAC, ROAS, LTV, MER), produção de relatórios narrativos de alta densidade e envio de alertas estruturados de desempenho para Slack e WhatsApp.

---

## 🎯 Quando Usar
- Ao avaliar a contribuição de múltiplos pontos de contato ao longo da jornada do cliente.
- Ao consolidar resultados semanais ou mensais para C-level, investidores ou clientes de agência.
- Ao calcular métricas financeiras de eficiência de aquisição (CAC Blended vs. Pago, Payback, MER).
- Ao estruturar relatórios automatizados no padrão executivo ClawdBot via mensagens instantâneas.
- Ao auditar a saúde de contas e detectar anomalias súbitas de tráfego ou conversão.

## 🚫 Quando NÃO Usar
- Para engenharia técnica de tags GTM ou dataLayer (use `data-web-ga4`).
- Para análise de coortes e retenção in-app (use `data-funil-e-coortes`).
- Para execução e cálculo amostral de testes A/B (use `growth-testes-ab`).

---

## 🧭 1. Comparativo de Modelos de Atribuição

| Modelo de Atribuição | Como Funciona | Quando é Recomendado | Limitações Principais |
|---|---|---|---|
| **Last Interaction (Último Clique)** | 100% do crédito para o último canal antes da conversão. | Ciclos de venda curtíssimos ou compras por impulso. | Ignora canais de topo de funil (Social, Conteúdo, Display). |
| **First Interaction (Primeiro Clique)** | 100% do crédito para o canal que gerou o primeiro contato. | Foco agressivo em awareness e descoberta de marca. | Desconsidera canais de fechamento e nutrição (Email, Retargeting). |
| **Linear** | Crédito dividido igualmente entre todos os pontos de contato. | Jornadas longas com múltiplos pontos de contato equivalentes. | Trata um banner acidental com o mesmo peso de um webinar aprofundado. |
| **Time-Decay (Decaimento Temporal)** | Mais crédito para toques próximos do momento da conversão. | Campanhas promocionais sazonais com prazos curtos (ex: Black Friday). | Subestima a importância do primeiro impacto da marca. |
| **Position-Based (U-Shaped 40-20-40)** | 40% para o primeiro toque, 40% para o toque de conversão, 20% para intermediários. | B2B SaaS e vendas consultivas com jornada estruturada. | Modelo estático que não aprende com padrões reais de conversão. |
| **Data-Driven (Algorítmico / Shapley)** | Algoritmo proprietário (ex: GA4) que analisa caminhos de conversão e não-conversão. | Operações de alto volume (> 1.000 conversões/mês). | Caixa-preta algorítmica; difícil de replicar manualmente em planilhas. |

---

## 📈 2. Métricas Executivas de Eficiência de Marketing

### 2.1. Fórmulas Fundamentais de Performance
- **Blended CAC**:
  $$\text{Blended CAC} = \frac{\text{Investimento Total em Mídia} + \text{Custos de Equipe/Ferramentas}}{\text{Total de Novos Clientes Conquistados (Todos os Canais)}}$$
- **Marketing Efficiency Ratio (MER)**:
  $$\text{MER} = \frac{\text{Receita Total Bruta}}{\text{Investimento Total em Mídia Paga}}$$
- **Razão LTV:CAC**:
  $$\text{LTV:CAC} = \frac{\text{Lifetime Value Médio}}{\text{CAC}}$$
  *(Benchmark de mercado saudável: entre 3:1 e 5:1)*.
- **Payback Period**: Tempo necessário (em meses) para que a margem de contribuição gerada pelo cliente pague o seu custo de aquisição.

### 2.2. Benchmarks de Eficiência por Modelo de Negócio

| Métrica | E-commerce D2C | B2B SaaS Enterprise | Infoprodutos / Lançamentos |
|---|---|---|---|
| **ROAS Mínimo Aceitável** | $\ge 2.5\text{x}$ (primeira compra) | $\ge 1.0\text{x}$ (foco em LTV anual) | $\ge 3.0\text{x}$ a $5.0\text{x}$ |
| **MER Saudável** | $4.0\text{x}$ a $8.0\text{x}$ | $3.0\text{x}$ a $6.0\text{x}$ | $4.0\text{x}$ a $10.0\text{x}$ |
| **Payback Alvo** | $< 30$ dias | 6 a 12 meses | Imediato (D0 a D7) |
| **Razão LTV:CAC** | $\ge 2.5:1$ | $\ge 3.5:1$ | $\ge 4.0:1$ |

---

## 📝 3. Estrutura do Relatório Executivo Semanal

Todo relatório narrativo de alto nível deve evitar o despejo de métricas brutas e focar em 4 blocos concisos:

1. **Executive Summary (Contexto em 3 Linhas)**:
   - Resumo claro: batemos a meta? Qual foi a principal alavanca de crescimento? Qual foi a principal ameaça?
2. **Scorecard de Metas (Realizado vs. Meta)**:
   - Tabela comparativa: Investimento, Leads, MQLs, Clientes, CAC, ROAS e Variação percentual ($\Delta\%$).
3. **Diagnóstico de Causa Raiz**:
   - Por que o desempenho subiu ou caiu? Análise focada em variáveis controláveis (CPA, CTR, taxa de conversão) e externas (concorrência, sazonalidade).
4. **Plano de Ação para a Próxima Semana**:
   - 3 iniciativas prioritárias com dono e data de entrega.

---

## 📱 4. Padrão de Relatórios Rápidos e Alertas de Anomalias

### 4.1. Snapshot ClawdBot (WhatsApp / Slack)
Formatação limpa e de fácil leitura móvel:

```markdown
📊 *RELATÓRIO SEMANAL DE PERFORMANCE - SEMANA 42*
━━━━━━━━━━━━━━━━━━━━━━━━━━
💰 *Investimento Total:* R$ 18.450,00 (+4% vs. sem. anterior)
🎯 *Novos Clientes:* 42 (Meta: 40 | +5% ✅)
📉 *Blended CAC:* R$ 439,28 (-11% vs. sem. anterior 🚀)
💵 *Receita Gerada:* R$ 89.200,00 (ROAS: 4.83x)

🏆 *Top Canais por Eficiência:*
1. Meta Ads (Retargeting): ROAS 6.2x | CAC R$ 280
2. Google Ads (Search Fundo): ROAS 5.1x | CAC R$ 390
3. Email Marketing / Nutrição: 11 vendas diretas

⚠️ *Pontos de Atenção:*
- Aumento de 18% no CPC de Google Search na palavra-chave concorrente.

🚀 *Prioridades da Semana:*
1. Escalar orçamento em 15% nas campanhas vencedoras de Meta Ads.
2. Lançar teste A/B no novo formulário de checkout para conter drop-off mobile.
```

### 4.2. Checklist de Auditoria de Saúde de Contas (Health Audit)
- [ ] **Discrepância Ads vs. GA4**: Diferença entre cliques reportados no Meta/Google e sessões registradas no GA4 não deve ultrapassar 15% (acima disso indica carregamento lento de página ou perda de UTM).
- [ ] **Conversões Órfãs**: Transações registradas no processador de pagamento sem parâmetros de UTM ou `gclid`/`fbclid` associados.
- [ ] **Fadiga de Criativo**: Frequência semanal > 3.5 em públicos frios com aumento simultâneo de CPA > 25%.
- [ ] **Tracking Break Check**: Verificar diariamente se houve dias com conversão zerada ou queda abrupta superior a 50% sem alteração de investimento.

---

## 📚 5. Biblioteca de Referências Operacionais

Consulte os guias especializados na pasta `references/`:

| Arquivo de Referência | Conteúdo Principal & Uso Prático |
|---|---|
| [`attribution-models.md`](references/attribution-models.md) | Detalhamento matemático de modelos de atribuição e trade-offs estratégicos. |
| [`analytics-attribution.md`](references/analytics-attribution.md) | Configuração de modelos de atribuição no GA4, Meta Attribution e Google Ads. |
| [`analytics-marketing.md`](references/analytics-marketing.md) | Framework de mensuração de marketing de performance e métricas de crescimento. |
| [`reporting-templates.md`](references/reporting-templates.md) | Templates executivos em Markdown para relatórios semanais, mensais e trimestrais (QBR). |
| [`dashboards.md`](references/dashboards.md) | Melhores práticas de UI/UX para dashboards executivos em Looker Studio e Metabase. |
| [`clawdbot-weekly-whatsapp-report.md`](references/clawdbot-weekly-whatsapp-report.md) | Padrão otimizado de envio de relatórios curtos com destaques gráficos para WhatsApp. |
| [`clawdbot-account-health-audit.md`](references/clawdbot-account-health-audit.md) | Checklist de auditoria de saúde de contas de anúncios, discrepâncias e segurança. |

## Roteiros guiados (vindos do kit AgentKits)

Roteiros que fazem perguntas ao usuário antes de entregar. O texto base é inglês.

- **[roi.md](references/roi.md)** — Roteiro guiado para calcular o ROI de campanha ou canal.

## Outras referências

- **[attribution-origins.md](references/attribution-origins.md)** — Origem dos modelos e frameworks de atribuição.
- **[marketing-metrics-kpis.md](references/marketing-metrics-kpis.md)** — Métricas e KPIs de marketing.
- **[use-mcp.md](references/use-mcp.md)** — Usar ferramentas de servidores MCP para puxar dados de marketing; requer MCP configurado.
- **[revenue-attribution.md](references/revenue-attribution.md)** — Atribuição de receita entre pontos de contato de marketing e vendas.

## Para onde foram os outros assuntos

- **Guias de Word, PDF e Excel, ferramentas de relatório por script e rastreamento duplicado de GA4:** arquivados em `.agent/skills/_arquivo/mescladas/r11-analytics/`. Para documentos, use as skills globais `docx`, `pdf` e `xlsx`.
