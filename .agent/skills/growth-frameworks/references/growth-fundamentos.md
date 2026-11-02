# Growth Fundamentals

> Guia de bolso de growth: North Star, funil AARRR com benchmarks, loops virais e K-factor, ativação, retenção, priorização por ICE, experimentos, canais com faixa de CAC e formato de entrega. Fusão de `growth-hacking` e `growth-strategy` (vindos de `growth-indicacao-e-afiliados`, 2026-10-20); os originais estão em `_arquivo/mescladas/r17-produto/referral-affiliate-growth/`. Para a análise profunda de cada tema, veja [aarrr-metrics.md](aarrr-metrics.md), [growth-loops.md](growth-loops.md) e [product-led-growth.md](product-led-growth.md).

---

## 1. North Star Metric

Toda estratégia de growth começa pela métrica que melhor mostra o valor entregue ao cliente.

**Como achar:**
1. Qual ação indica que o usuário está recebendo valor?
2. É mensurável e acionável?
3. Melhorá-la melhora a receita de forma direta?

| Tipo de negócio | North Star de exemplo |
|---|---|
| SaaS (B2B) | Usuários ativos por semana que fazem a ação principal |
| E-commerce | Compras por semana / frequência de compra |
| Marketplace | Transações por semana |
| Mídia / conteúdo | Leitores ativos por dia / tempo total de leitura por mês |
| App de consumo | Razão DAU/MAU |
| Ferramenta para devs | Chamadas de API por mês |

| North Star | Métricas de entrada |
|---|---|
| Usuários ativos | Cadastros, ativação, retenção |
| Receita | Clientes, ARPU, frequência |
| Engajamento | Sessões, ações, tempo de uso |

---

## 2. Funil AARRR e benchmarks

```
Acquisition → Activation → Retention → Revenue → Referral
    │              │            │           │          │
 Como acham?   Veem valor?  Voltam?      Pagam?    Indicam?
```

| Etapa | Métrica | Bom | Ótimo |
|---|---|---|---|
| **Acquisition** | Visitante → cadastro | 2–5% | 8%+ |
| **Activation** | Cadastro → "aha moment" | 20–40% | 50%+ |
| **Retention** | Retenção na semana 1 | 25–40% | 50%+ |
| **Retention** | Retenção no mês 1 | 10–25% | 30%+ |
| **Revenue** | Grátis → pago | 2–5% | 8%+ |
| **Revenue** | Retenção líquida de receita (NRR) | 100–110% | 120%+ |
| **Referral** | Usuários que indicam | 5–10% | 20%+ |

Métrica-chave por etapa: Acquisition = CAC e fontes de tráfego; Activation = taxa de ativação; Retention = churn e DAU/MAU; Revenue = ARPU e LTV; Referral = coeficiente viral.

**Diagnóstico do funil. Regra: conserte da direita para a esquerda (retenção antes de aquisição).**

```
Retenção quebrada  → conserte o produto antes de gastar em aquisição
Ativação baixa     → melhore o onboarding antes de otimizar landing pages
Receita baixa      → conserte preço/pacote antes de criar funcionalidades
```

---

## 3. Growth loops e viralidade

Loops > funis. O funil é linear; o loop se acumula.

| Loop | Fluxo | Métrica-chave |
|---|---|---|
| **Viral** | Usuário tem valor → convida → novo usuário entra → tem valor → convida | Coeficiente viral (K) |
| **Conteúdo** | Usuário cria conteúdo → é indexado/compartilhado → novo visitante acha → cadastra → cria conteúdo | Crescimento do tráfego orgânico |
| **Pago** | Usuário paga → receita financia anúncios → anúncios trazem novo usuário | LTV:CAC (ideal > 3:1) |
| **Vendas** | Usuário começa pequeno → expande assentos/uso → vira defensor → negócio enterprise | NRR |

Exemplos: Dropbox (viral), Pinterest/Quora (conteúdo), SaaS com payback < 12 meses (pago), Slack/Figma/Notion (vendas bottom-up).

### Tipos de loop viral

| Tipo | Exemplo | Potencial de K |
|---|---|---|
| **Inerente** | Convite para colaborar | Alto |
| **Boca a boca** | Produto tão bom que se indica | Médio |
| **Incentivado** | Recompensa por indicação | Alto |
| **Compartilhamento social** | Compartilhar conteúdo | Médio |
| **Embutido** | "Feito com X" | Baixo–médio |

### Coeficiente viral (K-factor)

```
K = i × c
i = convites enviados por usuário
c = taxa de conversão dos convites
```

| K | Resultado |
|---|---|
| K > 1 | Crescimento exponencial |
| 0,5 < K < 1 | Ganho viral relevante, mas não se sustenta sozinho |
| K = 1 | Crescimento linear |
| K < 1 | Crescimento que se esgota |

Estrutura de um programa de indicação (detalhes em [referral-program.md](../../growth-indicacao-e-afiliados/references/referral-program.md)): recompensa para os dois lados, compartilhar com um clique, posição visível dentro do produto, códigos de indicação únicos para rastrear.

---

## 4. Ativação

Levar o usuário ao "aha moment" rápido.

1. **Identifique o aha moment**: qual ação se correlaciona com retenção de longo prazo?
2. **Meça o tempo até o valor** (cadastro → primeiro valor).
3. **Remova atrito**: cada passo desnecessário antes do aha mata a conversão.
4. **Acrescente motivação**: barra de progresso, checklist, vitórias rápidas, dicas (tooltips), personalização.
5. **Use estados vazios com inteligência**: mostre valor antes de o usuário fazer qualquer coisa (dados de exemplo, modelos).

| Exemplo de aha moment | Produto |
|---|---|
| Enviar a primeira mensagem | Slack |
| Criar o primeiro design | Figma |
| Publicar o primeiro site | Vercel |
| Primeiro resultado de busca | Algolia |

| Métrica | Cálculo |
|---|---|
| Taxa de ativação | Usuários que fazem a ação-chave / total de cadastros |
| Tempo até o valor | Tempo entre cadastro e primeiro valor |
| Conclusão de configuração | % que termina o onboarding |

---

## 5. Retenção

**Curvas de retenção.** Boa retenção: a curva achata (o platô é a base retida). Má retenção: a curva chega perto de zero. Análise: trace coortes semanais/mensais, ache onde a curva achata e foque em levar mais gente até esse ponto.

| Janela | Foco |
|---|---|
| Dia 1 (24 h) | Primeira impressão |
| Semana 1 | Formação de hábito, chegar ao aha moment |
| Mês 1 | Valor central, dependência do fluxo de trabalho, integrações |
| Mês 1–3 | Aprofundar o uso, apresentar recursos avançados |
| 90+ dias | Lealdade: comunidade, identidade, custo de troca |

| Tática | Como |
|---|---|
| Sequências de e-mail | Gotejamento (drip) |
| Notificações push | Lembretes na hora certa |
| Mensagens no app | Ajuda contextual |
| Educação de recursos | Mostrar o que não foi usado |
| Recompensas | Gamificação |
| Comunidade | Criar conexões |

**Reduzir churn:** (1) identifique sinais (uso caindo, chamados, pagamento atrasado); (2) segmente quem saiu e pergunte por quê; (3) intervenha cedo com alertas automáticos; (4) campanhas de reconquista com novidades; (5) conserte o produto, porque a maior parte do churn é de produto, não de marketing.

| Métrica | Fórmula |
|---|---|
| Retenção no dia N | Ativos no dia N / cadastros no dia 0 |
| Retenção por coorte | Usuários ainda ativos / usuários da coorte |
| Taxa de churn | Clientes perdidos / total de clientes |
| DAU/MAU | Ativos diários / ativos mensais |

---

## 6. Priorização e experimentos (ICE)

| Fator | Nota 1–10 | Definição |
|---|---|---|
| **Impact** | Quanto move a métrica | 1 = quase nada, 10 = 2x+ |
| **Confidence** | Certeza de que funciona | 1 = palpite, 10 = comprovado |
| **Ease** | Facilidade de implementar e medir | 1 = meses, 10 = horas |

**ICE = (Impact + Confidence + Ease) / 3.** Serve também para priorizar canais.

**Processo:** Ideação (brainstorm + ICE) → Desenho (hipótese, métrica de sucesso) → Construção (MVP) → Medição → Aprendizado (documentar e iterar).

```
Hipótese: Se fizermos [mudança], então [métrica] vai [subir/cair] porque [motivo].
```

**Amostra aproximada por variante (teste A/B):**

| Taxa base | Melhora relativa | Amostra |
|---|---|---|
| 2% | 10% | ~78.000 |
| 2% | 25% | ~12.500 |
| 5% | 10% | ~31.000 |
| 5% | 25% | ~5.000 |

Para calcular com a sua taxa e confirmar significância, use o script de [growth-testes-ab](../../growth-testes-ab/SKILL.md).

**Modelo de experimento:**

```markdown
## Experimento: {Nome}
**Hipótese:** Se {mudança}, então {métrica} vai {melhorar} porque {motivo}.
**Métrica:** {métrica primária}
**ICE:** Impact {}/10, Confidence {}/10, Ease {}/10 = **{média}**
**Desenho:** Controle {estado atual} · Variante {mudança} · Amostra {estimativa} · Duração {dias/semanas}
**Resultado:** Controle {X} vs. Variante {Y} ({+/-Z%}) · Significância {sim/não, p-valor} · Decisão {lançar / iterar / matar}
**Aprendizados:** {o que aprendemos, qualquer que seja o resultado}
```

---

## 7. Canais de aquisição

| Canal | Tipo | Tempo até resultado | Faixa de CAC (US$) | Melhor para |
|---|---|---|---|---|
| SEO / conteúdo | Orgânico | 3–6 meses | 50–200 | Entrada contínua, confiança |
| Busca paga | Pago | Imediato | 20–200 | Compradores com intenção alta |
| Anúncios sociais | Pago | 1–2 semanas | 10–100 | Awareness, remarketing |
| E-mail | Próprio | 1–2 semanas | 1–10 | Nutrição, retenção |
| Parcerias | Alavancagem | 1–3 meses | 10–50 | Co-marketing, transferência de confiança |
| Comunidade | Orgânico | 3–6 meses | 5–20 | Lealdade, boca a boca |
| Product-led | Viral | 1–3 meses | 0–10 | Viral, bottom-up |
| Vendas | Pago | Imediato | 200–2.000 | Enterprise, ticket alto |

Regra prática: domine 1–2 canais antes de abrir outros. As faixas de CAC são referências em dólar de SaaS; confira com os seus números.

---

## 8. Product-Led Growth (resumo)

Princípios: plano grátis generoso, autoatendimento (sem venda), começar pelo usuário individual (bottom-up), viralidade embutida, uso que dispara o upgrade. Metas de referência: grátis → pago 2–5%, tempo até pagar < 30 dias, conversão de PQL 10–20%, receita de expansão > 30% da receita nova. Detalhes em [product-led-growth.md](product-led-growth.md).

---

## 9. Ferramentas e time de growth

| Uso | Ferramentas de exemplo |
|---|---|
| Analytics de produto | Mixpanel, Amplitude, Heap |
| Tráfego web | Google Analytics |
| Pipeline de dados | Segment |
| Testes A/B e flags | Optimizely, LaunchDarkly, Statsig |
| Mensagens e onboarding | Intercom, Customer.io, Appcues |

| Papel | Responsabilidade |
|---|---|
| Growth Lead | Estratégia e priorização |
| Growth PM | Experimentos e roadmap |
| Growth Engineer | Implementação |
| Analista de dados | Insights e medição |
| Growth Marketer | Aquisição e conteúdo |

Cadência: semanal (revisão de experimentos), quinzenal (planejamento de sprint), mensal (mergulho nas métricas), trimestral (revisão de estratégia).

---

## 10. Formato de entrega (estratégia de growth)

```markdown
# Estratégia de Growth: {Produto/Empresa}

## North Star Metric
{Métrica}: {por que essa}

## Análise do funil atual
| Etapa | Atual | Meta | Lacuna |
|---|---|---|---|
| Acquisition | {%} | {%} | {ajuste} |
| Activation | {%} | {%} | {ajuste} |
| Retention | {%} | {%} | {ajuste} |
| Revenue | {%} | {%} | {ajuste} |
| Referral | {%} | {%} | {ajuste} |

## Loop de growth principal
{descrição do loop em que investir}

## Top 5 experimentos (por ICE)
| # | Experimento | Impact | Confidence | Ease | ICE | Etapa AARRR |

## Roteiro de 90 dias
Mês 1: {tema, ações} · Mês 2: {tema, ações} · Mês 3: {tema, ações}
```

**Lembretes:**
- Growth sem retenção é balde furado; conserte a retenção primeiro.
- Métrica sem contexto não diz nada: compare com a sua própria tendência e com benchmarks do setor.
- A maior parte do crescimento vem de pequenas vitórias acumuladas, não de bala de prata.
- O melhor canal é o que os concorrentes ainda não saturaram.
- Converse com quem cancelou: costuma ensinar mais que qualquer painel.
