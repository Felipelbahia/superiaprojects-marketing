---
name: audiovisual-pitch-deck
description: Especialista em arquitetura, narrativa, storytelling financeiro e design de apresentações executivas (Pitch Decks para investidores no padrão Y Combinator e decks comerciais de alto impacto).
license: MIT
metadata:
  author: Antigravity Kit (0 Mkt) & Felipe Bahia (Futuro Mercado)
  version: 1.0.0
---

# Pitch Deck Strategist - Diretrizes Operacionais

Esta skill orienta a concepção, estrutura narrativa e redação de apresentações executivas para captação de recursos (*Fundraising Pitch Decks* nos padrões de aceleradoras como Y Combinator, Sequoia e Techstars) e apresentações institucionais/comerciais de vendas complexas em formato slide a slide.

---

## 🎯 Quando Usar
- Ao estruturar uma rodada de captação de investimento (Pre-seed, Seed, Series A/B).
- Ao desenhar um pitch deck conciso de 10 a 12 slides focado em métricas de tração e tese de mercado.
- Ao redigir memoriais executivos (*One-Pagers*) e resumos executivos de 1 página para investidores.
- Ao criar narrativas e decks de vendas para comitês executivos e conselhos de administração.
- Ao estruturar templates de slides para captação e vendas.

## 🚫 Quando NÃO Usar
- Para aula, treinamento, workshop ou webinar (use `audiovisual-apresentacoes-educacionais`).
- Para apresentações escritas em código Slidev/Markdown para desenvolvedores (use `audiovisual-slidev`, que também traz os temas e estilos visuais).
- Para criação e redação de carrosséis de redes sociais (use `social-carrossel`).

---

## 🏛️ 1. A Estrutura Canônica do Pitch Deck (Padrão YC de 10 Slides)

```
Slide 01: Título & One-liner (O que a empresa faz em 1 frase simples e memorável)
Slide 02: O Problema (A dor real, urgente e dolorosa de um mercado específico)
Slide 03: A Solução (Como o produto resolve o problema com 10x mais eficiência)
Slide 04: Por Que Agora? (Gatilhos regulatórios, tecnológicos ou comportamentais)
Slide 05: Tamanho de Mercado (TAM, SAM, SOM fundamentados de baixo para cima)
Slide 06: Tração & Crescimento (Gráfico clássico de "Taco de Hóquei" em receita/uso)
Slide 07: Modelo de Negócios (Preço, margem bruta, LTV, CAC e canais de escala)
Slide 08: Diferencial Competitivo & Moat (Por que seremos difíceis de copiar?)
Slide 09: Equipe Fundadora (Histórico de realizações prévias e fit com o problema)
Slide 10: The Ask / A Rodada (Quanto estamos captando e quais marcos atingiremos)
```

---

## 📈 2. As Regras de Ouro do Storytelling para Investidores

### 2.1. A Lei de Guy Kawasaki (Regra 10/20/30)
- **10 Slides**: O número ideal de slides para reter atenção integral.
- **20 Minutos**: Duração máxima da fala, reservando o resto da reunião para perguntas e respostas.
- **30 Pontos de Fonte**: Tamanho mínimo de fonte para impedir que o fundador encha os slides de parágrafos ilegíveis.

### 2.2. A Equação do TAM (Bottom-Up vs. Top-Down)
Fuja de relatórios genéricos que dizem *"o mercado global de IA é de US$ 1 trilhão e queremos apenas 1%"*. Calcule sempre de baixo para cima (*Bottom-up*):
$$\text{TAM} = \text{Total de Empresas Qualificadas no Mundo} \times \text{Valor Anual do Contrato (ACV)}$$

---

## 🎨 3. Arquitetura de Slide: 1 Ideia por Lâmina

```
┌─────────────────────────────────────────────────────────────┐
│ Título Ativo (A Conclusão do Slide em 1 Frase)              │
│ Ex: "A receita cresceu 4.2x no último trimestre com retenção│
│      de 118% NRR."                                          │
│                                                             │
│ [Elemento Gráfico Central / Prova Visual: Gráfico ou Dado] │
│                                                             │
│ Nota de Rodapé ou Citação de Fonte                         │
└─────────────────────────────────────────────────────────────┘
```
*Evite títulos descritivos passivos como "Tração" ou "Mercado". Use títulos com conclusões ativas que contem a história mesmo se o investidor apenas folhear os slides.*

---

---

## 🎯 5. As 5 Perguntas Mais Críticas de Fundos de VC (e Como Responder)

1. **"Qual é o seu Moat / Fosso Defensivo?"**
   - *Resposta Ruim*: "Nossa tecnologia é melhor e temos IA proprietária."
   - *Resposta Robusta*: "Nossa vantagem competitiva se consolida em network effects de dados: quanto mais clientes usam nossa infraestrutura, mais refinados nossos modelos se tornam, reduzindo nosso custo marginal e elevando o custo de troca (switching cost) para o concorrente."

2. **"Por que os gigantes de mercado não constroem isso amanhã?"**
   - *Resposta Robusta*: "Para os grandes players, este mercado de nicho ainda é muito pequeno para mover o ponteiro financeiro deles, mas para nós representa uma oportunidade de R$ 500M. Além disso, a arquitetura legada deles gera um dilema de inovação que os impede de adotar nossa abordagem sem canibalizar o produto principal."

3. **"Qual é a sua estratégia de Go-To-Market (GTM)?"**
   - *Resposta Robusta*: "Não dependemos apenas de mídia paga. Temos um canal de tração validado com CAC de R$ 380 gerando payback em 4 meses, combinado com um loop de expansão onde cada cliente médio ativa 3 novos assentos nos primeiros 90 dias."

### 5.1. Checklist Pré-Envio do Pitch Deck
- [ ] Exportado em formato PDF limpo e leve ($< 10	ext{MB}$) sem quebras de fontes.
- [ ] Gráficos com eixos claramente rotulados com moedas, períodos e unidades métricas.
- [ ] Ausência de jargões técnicos excessivos incompreensíveis para investidores generalistas.
- [ ] Dados de contato do fundador (Email, WhatsApp e LinkedIn) visíveis na primeira e última lâmina.
- [ ] **Envio Seguro via DocSend**: Sempre envie links com rastreamento por slide (DocSend) em vez de anexos soltos, monitorando o tempo exato de leitura por investidor.
- [ ] **Apêndice Separado (Appendix / FAQ)**: Slides técnicos de arquitetura, contratos e demonstrações de fluxo de caixa alocados após o Slide 10 para consulta exclusiva durante o Q&A.

---

### 5.2. A Regra do Elevator Pitch (30 Segundos)
Apresente a tese antes mesmo de abrir os slides usando a fórmula canônica:
> *"Nós ajudamos [Público-Alvo Específico] a [Resultado Desejado Quantificável] através de [Abordagem Inovadora/Proprietária], eliminando [Maior Ponto de Fricção Atual]."*

### 5.3. Métricas de Captação e Valuation
- **Tamanho da Rodada**: Capital necessário para atingir os próximos 18 a 24 meses de runway.
- **Marcos de Desriscagem**: 3 metas operacionais concretas que destravam a próxima rodada (ex: bater R$ 300k MRR, fechar 5 clientes enterprise, atingir NRR de 125%).

---

## 📚 4. Biblioteca de Referências Operacionais

Acesse os guias técnicos na subpasta [`references/`](references/):

| Arquivo de Referência | Conteúdo Técnico & Casos Práticos |
|---|---|
| [`yc-pitch-deck.md`](references/yc-pitch-deck.md) | O playbook oficial da Y Combinator para construção de decks de Demo Day e rodadas Seed. |
| [`fundraising-narrative.md`](references/fundraising-narrative.md) | Estrutura de storytelling para captação de risco: tese de investimento, escassez e FOMO. |
| [`deck-frameworks.md`](references/deck-frameworks.md) | Comparativo de estruturas de apresentação para vendas corporativas, conselho e investidores. |
| [`one-pager-templates.md`](references/one-pager-templates.md) | Modelos concisos de sumários executivos de 1 página para envio por email a fundos de VC. |
| [`slide-templates.md`](references/slide-templates.md) | Blueprints de slides: lâminas de problema, solução, comparativo competitivo e finanças. |
| [`pptx.md`](references/pptx.md) | Diretrizes e padrões para geração e estilização de arquivos PowerPoint profissionais. |
| [`html2pptx.md`](references/html2pptx.md) | Automação e conversão de páginas HTML/CSS em apresentações editáveis em PPTX. |

## Apresentações de ensino

Os guias de aula, workshop e webinar (carga cognitiva, Mayer, validação de acessibilidade) estão na skill [audiovisual-apresentacoes-educacionais](../audiovisual-apresentacoes-educacionais/SKILL.md). Os modelos de slide daqui ([`slide-templates.md`](references/slide-templates.md)) são usados pelas duas.
