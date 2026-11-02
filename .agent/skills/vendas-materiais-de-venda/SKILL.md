---
name: vendas-materiais-de-venda
description: "Use para criar os materiais que o time comercial usa para fechar negócio (em inglês, sales enablement): deck de vendas, one-pager, pitch personalizado para um prospecto, script de demonstração por tipo de call, mapa de objeções e respostas, case de sucesso, coleta de depoimentos e resposta a RFP/RFI. Gatilhos: \"faça um case\", \"preciso de um depoimento\", \"responda esta RFP\", \"script de demo\", \"objeções de preço\", \"one-pager\", \"pitch para esta empresa\". NÃO use para qualificar leads, prever receita ou gerir negócios no funil (use vendas-pipeline), técnicas de conversa e negociação (use vendas-metodologias-b2b), deck de investidor (use audiovisual-pitch-deck), battlecard de concorrente (use revenue-inteligencia-competitiva) nem cold email (use vendas-cold-email)."
license: MIT
metadata:
  author: Antigravity Multi-IA Hub & Felipe Bahia (Futuro Mercado)
  version: 1.0.0
---

# Vendas: materiais de venda

Em inglês isso se chama *sales enablement*: tudo o que o vendedor leva para a conversa (apresentação, folha resumo, roteiro de demo, respostas para "não", prova de que funciona). Esta skill reúne sete guias que estavam dentro de `vendas-pipeline` (2026-10-20), onde ficavam fora do assunto: aquela skill trata de funil, qualificação e previsão.

## Como escolher o caminho

| Situação | Abra |
|---|---|
| Preciso montar o kit do time: deck, one-pager, leave-behind, playbook por persona | [sales-enablement](references/sales-enablement.md) |
| Vou conversar com uma empresa específica e quero um pitch sob medida (formato, público, nível de detalhe) | [roteiro-guiado-pitch](references/roteiro-guiado-pitch.md) |
| Vou fazer uma demonstração e quero o roteiro cena a cena (descoberta, primeira demo, demo técnica, visão executiva) | [demo-scripts](references/demo-scripts.md) |
| Quero antecipar os "nãos" (preço, concorrente, timing, segurança) e preparar respostas | [objection-mapping](references/objection-mapping.md) |
| Ganhei um cliente e quero transformar o resultado em prova para as próximas vendas | [case-study-builder](references/case-study-builder.md) |
| Preciso coletar depoimentos com números, de forma sistemática | [testimonial-collector](references/testimonial-collector.md) |
| Chegou uma RFP ou RFI e preciso decidir se respondo e como estruturar a resposta | [rfp-response](references/rfp-response.md) |

## Passo a passo

1. **Descubra o momento da venda.** Primeiro contato, demo, proposta ou renovação pedem materiais diferentes. Sem isso, o material sai genérico.
2. **Leia o contexto de produto.** O `sales-enablement` pede o contexto de product marketing antes de começar; se existir um para a marca, use.
3. **Escolha um guia da tabela e siga o roteiro dele.** Cada guia pede dados de entrada (cliente, resultado, objeção). Faltando dado, pergunte; não invente número de resultado.
4. **Marque o que é exemplo.** Prazos, metas e métricas dos guias vieram do kit original em inglês e são ilustrativos.
5. **Passe o texto pelo `/geral-anti-slop`** antes de entregar (regra 1.3 do `CLAUDE.md`).

## Fronteiras

- Qualificação (MEDDIC, BANT), previsão, risco de negócio, passagem para Sucesso do Cliente e comissão ficam com [vendas-pipeline](../vendas-pipeline/SKILL.md).
- Perguntas de descoberta e técnicas de negociação (SPIN, Challenger, Voss) ficam com [vendas-metodologias-b2b](../vendas-metodologias-b2b/SKILL.md). O `objection-mapping` aqui aplica essas técnicas a uma lista de objeções.
- Deck para investidor ou captação: [audiovisual-pitch-deck](../audiovisual-pitch-deck/SKILL.md). Comparação com concorrente e battlecard: [revenue-inteligencia-competitiva](../revenue-inteligencia-competitiva/SKILL.md).
- Texto de página de vendas: [copy-conversao](../copy-conversao/SKILL.md) ou [copy-landing-page](../copy-landing-page/SKILL.md).
- Se o material vai usar uma marca de `_brands/`, leia `brand-voice.md` e respeite "O que NÃO comunicar" (regra 1.1).

## Referências

| Arquivo | O que tem |
|---|---|
| [sales-enablement.md](references/sales-enablement.md) | Deck de vendas, one-pager, documento de objeções, scripts de demo e playbooks por persona e por etapa. |
| [roteiro-guiado-pitch.md](references/roteiro-guiado-pitch.md) | Roteiro guiado do kit AgentKits: pergunta o escopo, o formato e o público, e entrega um pitch personalizado. Texto base em inglês. |
| [demo-scripts.md](references/demo-scripts.md) | Roteiros por tipo de call, com tempo, fala sugerida e o que estabelecer em cada cena. |
| [objection-mapping.md](references/objection-mapping.md) | Mapa de objeções com psicologia de negociação (Chris Voss) e método de vendas. Material de terceiros (ClawFu, MIT). |
| [case-study-builder.md](references/case-study-builder.md) | Case de sucesso em três formatos, a partir de 8 campos de contexto. |
| [testimonial-collector.md](references/testimonial-collector.md) | Coleta, pontuação e formatação de depoimentos. |
| [rfp-response.md](references/rfp-response.md) | Análise de requisitos, decisão de responder ou não, estrutura da proposta e temas de vitória. Material de terceiros (ClawFu, MIT). |

> Os guias vieram de kits em inglês (AgentKits, ClawFu) e foram só movidos, sem revisão de texto. Material de terceiros: direito de uso confirmado pelo usuário.
