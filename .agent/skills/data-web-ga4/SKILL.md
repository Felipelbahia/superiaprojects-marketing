---
# Repository: https://github.com/Felipelbahia/superiaprojects-marketing
# Status: Customizada / Modificada localmente por Felipe Bahia
name: data-web-ga4
description: Especialista em arquitetura de dados web, engenharia de tracking, implementação avançada de GA4, Google Tag Manager (Web e Server-Side), Consent Mode v2 e modelagem de eventos em BigQuery.
author: Antigravity Kit (0 Mkt) & Felipe Bahia (Futuro Mercado)
license: MIT
metadata:
  author: Antigravity Kit (0 Mkt) & Felipe Bahia (Futuro Mercado)
  version: 1.0.0
---
# Web Analytics Architect - Diretrizes Operacionais

Esta skill orienta a concepção, implementação técnica, padronização e governança de arquiteturas de mensuração web, incluindo Google Analytics 4 (GA4), Google Tag Manager (GTM Client-Side e Server-Side), dataLayer, Enhanced Conversions e integração com BigQuery.

---

## 🎯 Quando Usar
- Ao estruturar uma nova propriedade do GA4 ou auditar propriedades existentes.
- Ao projetar taxonomias de eventos, schemas de `dataLayer` e convenções de nomenclatura.
- Ao configurar tags, acionadores e variáveis no Google Tag Manager (Client ou Server-Side).
- Ao implementar Consent Mode v2 e conformidade com LGPD/GDPR.
- Ao criar queries SQL avançadas para export de dados brutos do GA4 no Google BigQuery.
- Ao auditar perda de dados, duplicação de transações ou discrepâncias entre plataformas.

## 🚫 Quando NÃO Usar
- Para testes A/B e significância estatística (use `growth-testes-ab`).
- Para auditoria de UX/UI ou psicologia de conversão de páginas (use `site-cro`).
- Para modelos de atribuição multi-canal e relatórios de marketing executivos (use `data-atribuicao-e-relatorios`).

---

## 🧱 1. Taxonomia de Eventos e Padrão de Nomenclatura (GA4)

### 1.1. Regras Fundamentais de Nomenclatura
- **Formato Estrito**: Nomes de eventos e parâmetros devem utilizar exclusivamente `snake_case` em minúsculas (ex: `lead_form_submitted`, `subscription_tier`).
- **Comprimento Máximo**: Até 40 caracteres para o nome do evento; até 40 caracteres para o nome do parâmetro; até 100 caracteres para valores de strings de parâmetros.
- **Proibição de PII**: Jamais enviar dados pessoais identificáveis (nome, email em texto puro, telefone, CPF) em parâmetros de eventos ou URLs.

### 1.2. Padrão Universal de `dataLayer.push`

```javascript
window.dataLayer = window.dataLayer || [];
window.dataLayer.push({
  event: 'generate_lead',
  lead_type: 'b2b_demo_request',
  lead_source: 'hero_form',
  form_id: 'enterprise_quote_v2',
  user_status: 'anonymous',
  // Enhanced Conversions (Hash SHA-256 pré-computado ou texto normal capturado via variável GTM de 1st party):
  user_data: {
    email: 'user@example.com', // Sanitizado via GTM Enhanced Conversions
    phone_number: '+5511999999999'
  }
});
```

---

## 🛡️ 2. Consent Mode v2 e Privacidade

### 2.1. Estados Padrão Obrigatórios (Antes do Consentimento)
O script de Consent Mode v2 DEVE ser executado antes de qualquer tag do GTM ser carregada no `<head>`:

```html
<script>
  window.dataLayer = window.dataLayer || [];
  function gtag(){dataLayer.push(arguments);}
  gtag('consent', 'default', {
    'ad_storage': 'denied',
    'analytics_storage': 'denied',
    'ad_user_data': 'denied',
    'ad_personalization': 'denied',
    'wait_for_update': 500
  });
</script>
```

---

## 🛒 3. Matriz de Eventos Críticos (E-commerce e B2B SaaS)

| Evento Padrão | Parâmetros Obrigatórios | Disparo / Gatilho |
|---|---|---|
| `view_item` | `currency`, `value`, `items[{item_id, item_name, price}]` | Carregamento da página de produto ou visualização de plano SaaS |
| `begin_checkout` | `currency`, `value`, `coupon`, `items[]` | Primeiro clique em "Assinar" ou início do fluxo de checkout |
| `purchase` | `transaction_id`, `value`, `tax`, `shipping`, `currency`, `items[]` | Página de confirmação de pagamento ou webhook server-side |
| `generate_lead` | `lead_type`, `lead_value`, `form_id`, `channel` | Envio de formulário de contato qualificado ou agendamento de demo |
| `sign_up` | `method` (`google`, `email`, `sso`) | Criação com sucesso de nova conta |
| `login` | `method` | Autenticação bem-sucedida do usuário |

---

## 💻 4. BigQuery SQL: Consultas Essenciais de Auditoria

### 4.1. Taxa de Conversão Diária com Deduplicação de Transações
```sql
SELECT
  PARSE_DATE('%Y%m%d', event_date) AS date,
  COUNT(DISTINCT user_pseudo_id) AS total_users,
  COUNT(DISTINCT CASE WHEN event_name = 'purchase' THEN (SELECT value.string_value FROM UNNEST(event_params) WHERE key = 'transaction_id') END) AS unique_purchases,
  ROUND(
    SAFE_DIVIDE(
      COUNT(DISTINCT CASE WHEN event_name = 'purchase' THEN user_pseudo_id END),
      COUNT(DISTINCT user_pseudo_id)
    ) * 100, 2
  ) AS user_conversion_rate_pct
FROM
  `seu-projeto.analytics_123456789.events_*`
WHERE
  _TABLE_SUFFIX BETWEEN FORMAT_DATE('%Y%m%d', DATE_SUB(CURRENT_DATE(), INTERVAL 30 DAY))
  AND FORMAT_DATE('%Y%m%d', CURRENT_DATE())
GROUP BY
  date
ORDER BY
  date DESC;
```

---

## 🔍 5. Protocolo de Validação e Debugging

1. **GTM Preview Mode (Tag Assistant)**:
   - Validar se a tag dispara no acionador correto sem duplicação (*Fire count = 1*).
   - Verificar variáveis de Event Parameters mapeadas no painel.
2. **GA4 DebugView**:
   - Ativar extensão *Google Analytics Debugger* ou usar `debug_mode: true`.
   - Inspecionar fluxo cronológico de eventos e checar propriedades do usuário (*User Properties*).
3. **Network Tab (Chrome DevTools)**:
   - Filtrar por `collect?v=2` para verificar requisições diretas do GA4.
   - Conferir status code 204 e payloads em POST (`en` = event name, `ep.*` = event parameters).

---

## 📚 6. Biblioteca de Referências Operacionais

Aprofunde-se nos guias especializados na pasta `references/`:

| Arquivo de Referência | Conteúdo Principal & Uso Prático |
|---|---|
| [`ga4-implementation-guide.md`](references/ga4-implementation-guide.md) | Guia completo de ponta a ponta para setup e governança do Google Analytics 4. |
| [`gtm-implementation.md`](references/gtm-implementation.md) | Melhores práticas de contêineres GTM, nomenclatura de tags, triggers e variáveis personalizadas. |
| [`event-library.md`](references/event-library.md) | Dicionário de eventos padrão e recomendados para e-commerce, B2B SaaS e conteúdo. |
| [`analytics-tracking.md`](references/analytics-tracking.md) | Arquitetura de dataLayer e padrões de rastreamento de interações ricas no frontend. |
| [`ga4-implementation.md`](references/ga4-implementation.md) | Manual de migração de Universal Analytics para GA4 e resolução de desvios de métricas. |
| [`adobe-analytics.md`](references/adobe-analytics.md) | Guia comparativo e transição de arquiteturas Adobe Analytics / Launch para ecossistema Google. |

## Outras referências

- **[posthog-analytics.md](references/posthog-analytics.md)** — Guia do PostHog; requer a API.
