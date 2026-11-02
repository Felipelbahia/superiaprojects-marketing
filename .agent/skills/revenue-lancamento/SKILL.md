---
name: revenue-lancamento
description: "Use para planejar o lançamento de qualquer produto, serviço, curso ou funcionalidade: escolher o tipo de lançamento, montar o plano de pré-lançamento, lançamento e pós-lançamento, definir canais próprios, alugados e emprestados (ORB), lançar em fases (interno, alfa, beta, acesso antecipado e geral), usar Product Hunt e lista de espera, ou montar o lançamento como evento (fórmula de Jeff Walker). Gatilhos: \"plano de lançamento\", \"lançar meu curso\", \"lançar produto\", \"abertura de carrinho\", \"lista de espera\", \"Product Hunt\", \"anunciar funcionalidade\". NÃO use para lançar API, SDK ou ferramenta para desenvolvedores, com níveis (tiers) e documentação (use revenue-lancamento-tecnico), para posicionamento, categoria e pré-mortem (use revenue-gtm-e-posicionamento), para campanha multicanal com UTM e calendário (use revenue-campanhas), para oferta, bônus e garantia (use revenue-oferta) nem para o texto de e-mails e páginas de venda (use email-copy e copy-landing-page)."
license: MIT
metadata:
  author: Felipe Bahia (Futuro Mercado)
  version: 1.0.0
---

# Lançamento de Produto

Guia para planejar um lançamento de qualquer tipo de produto. Reúne três enfoques que servem para produto digital, curso, serviço ou funcionalidade nova. Os arquivos vieram do `revenue-lancamento-tecnico` (2026-10-20), onde estavam fora do assunto: aquela skill trata de lançamento técnico (API, SDK, ferramenta para desenvolvedores).

## Como escolher o caminho

| Situação | Abra |
|---|---|
| Quero um roteiro completo: tipo de lançamento, fases antes e depois, Product Hunt, lista de espera, métricas e erros comuns | [launch-playbook-checklist](references/launch-playbook-checklist.md) |
| Quero decidir onde anunciar (canais próprios, alugados e emprestados) e lançar em fases, do interno ao acesso geral | [launch-strategy-framework](references/launch-strategy-framework.md) |
| Vou vender um curso, mentoria ou produto digital e quero transformar o lançamento num evento de uma ou duas semanas, com conteúdo antes da venda | [launch-formula-jeff-walker](references/launch-formula-jeff-walker.md) |
| É um lançamento de API, SDK ou ferramenta para desenvolvedores | skill [revenue-lancamento-tecnico](../revenue-lancamento-tecnico/SKILL.md) |
| Quero um roteiro que me faça perguntas e monte o plano de lançamento ou o anúncio de uma funcionalidade | [roteiro-guiado-lancamento](references/roteiro-guiado-lancamento.md) |
| Falta definir posicionamento, categoria ou riscos antes de lançar | skill [revenue-gtm-e-posicionamento](../revenue-gtm-e-posicionamento/SKILL.md) |

## Passo a passo

1. **Defina o tipo e o tamanho do lançamento.** Funcionalidade para quem já usa, produto novo para o mercado ou relançamento? O playbook traz as categorias e o objetivo de cada uma.
2. **Escolha os canais e as fases.** O `launch-strategy-framework` separa o que é seu (e-mail, site), o que é alugado (redes sociais) e o que é emprestado (parcerias, imprensa), e propõe cinco fases de abertura.
3. **Se for vender um curso ou infoproduto, monte o evento.** A fórmula de Jeff Walker espalha a mensagem de venda numa sequência de conteúdos (a "carta de vendas de lado"), em vez de uma página longa.
4. **Feche com o checklist e as métricas** do playbook, e registre o aprendizado para o próximo lançamento.

## Fronteiras

- O texto de cada e-mail da sequência fica com `email-copy`; a página de venda, com `copy-landing-page`.
- A oferta em si (o que entra, bônus, garantia) fica com `revenue-oferta`.
- Calendário e UTM da campanha ficam com `revenue-campanhas`.
- Se o produto usa uma marca de `_brands/`, leia `brand-voice.md` e `content-pillars.md` antes de escrever qualquer mensagem de lançamento (regra 1.1 do `CLAUDE.md`).

## Referências

| Arquivo | O que tem |
|---|---|
| [launch-playbook-checklist.md](references/launch-playbook-checklist.md) | Tipos de lançamento (por escopo e por canal), pré-lançamento de 4 a 8 semanas, Product Hunt, lançamento de funcionalidade, lista de espera, mensagens, pós-lançamento, métricas e erros comuns. |
| [launch-strategy-framework.md](references/launch-strategy-framework.md) | Filosofia de lançar várias vezes, framework ORB (canais próprios, alugados e emprestados), lançamento em cinco fases, Product Hunt, marketing de produto depois do lançamento e checklist. |
| [launch-formula-jeff-walker.md](references/launch-formula-jeff-walker.md) | Fórmula de lançamento de Jeff Walker: pré-pré-lançamento, sequência de conteúdos de pré-lançamento, abertura de carrinho, gatilhos mentais e tipos de lançamento. Material de terceiros (ClawFu, MIT); direito de uso confirmado pelo usuário. |
| [roteiro-guiado-lancamento.md](references/roteiro-guiado-lancamento.md) | Roteiro guiado do kit AgentKits (veio de `revenue-gtm-e-posicionamento`, 2026-10-20): pergunta escopo e produto, e entrega o plano de lançamento ou de anúncio. Texto base em inglês. |

> O `launch-strategy-framework` tem cabeçalho e seção "Related Skills" do kit original (AgentKits) e cita `email-sequence`, `page-cro`, `marketing-psychology` e `programmatic-seo`. Aqui, use no lugar `email-copy`, `site-cro`, `revenue-psicologia` e `seo-programatico`.
