---
name: brand-essence
description: "Use para definir ou aprofundar essência, crenças, história de origem, inimigo, posicionamento, categoria e arquétipo de uma marca (etapas 1 e 2 do brand-builder). Gatilhos: \"propósito\", \"posicionamento da marca\", \"Primal Branding\", \"arquétipo\". NÃO use para posicionar produto no mercado com GTM, categoria e proposta de valor de lançamento (use revenue-gtm-e-posicionamento) nem para analisar concorrentes (use revenue-inteligencia-competitiva)."
license: MIT
metadata:
  author: Antigravity Multi-IA Hub & Felipe Bahia (Futuro Mercado)
  version: 1.0.0
---

# Brand Essence

## Overview

Etapas 1 (Essência) e 2 (Posicionamento) do `brand-builder`. Transforma respostas do usuário em dois arquivos: o que a marca é e acredita, e onde ela se posiciona. Base: os sete ativos do Primal Branding (`../brand-builder/primal-branding.md`) mais posicionamento e arquétipo.

**Princípio central: crença sem custo é slogan. Toda crença sai com o que ela proíbe.**

## Antes de começar

1. Marca identificada e `00-intake.md` aprovado (modo e profundidade definidos). Sem isso, voltar ao `brand-builder`.
2. Ler `_brands/<marca>/` inteiro. Em modo estender, tratar o que existe como base e perguntar só o que falta.
3. Ler `../brand-builder/question-formats.md`.

## Fluxo

| Passo | Curta | Longa |
|---|---|---|
| Coleta de essência | `references/questionario-curto.md`, no chat | `references/questionario-longo.md`, gerado como documento em `_respostas/` |
| Síntese | `01-essencia.md` | `01-essencia.md` |
| Coleta de posicionamento | `references/posicionamento.md`, passos 1 a 4 | passos 1 a 7, com reação a referências |
| Síntese | `02-posicionamento.md` | `02-posicionamento.md` |
| Aprovação | uma por arquivo | uma por arquivo |

Perguntar a profundidade só se o Intake não definiu. Sempre mostrar a síntese antes de gravar.

## Regras

1. Cada ativo do Primal Branding vem do usuário (`[usuário]`) ou fica como lacuna. Se eu propuser, marcar `[derivado]` e pedir confirmação.
2. Credo: cada crença com "o que isso nos impede de fazer". Sem custo, devolver a pergunta.
3. Frase de posicionamento só é aprovada depois do teste dos dois filtros: "quem não é para nós" e "o concorrente mais próximo diria o mesmo?". Se diria, refazer.
4. Arquétipo é escolha de direção, não rótulo decorativo: mostrar o que ele muda na voz e no visual antes de aprovar.
5. Marca pessoal: líder e marca coincidem; perguntar o que acontece quando a pessoa sai de cena.
6. Texto final passa pelo `/geral-anti-slop`.
7. Não sobrescrever `01-essencia.md` ou `02-posicionamento.md` existentes; nova versão é `-v2`.

## Saída: `01-essencia.md`

```
# Essência - <Marca>
Estado: rascunho | aprovado em AAAA-MM-DD
## Propósito (uma frase)
## Crenças e o que cada uma proíbe
## Inimigo (o que a marca combate)
## Os 7 ativos
  História de criação / Credo / Ícone / Rituais / Palavras sagradas / Não-crentes / Líder
## Lacunas
```

## Saída: `02-posicionamento.md`

```
# Posicionamento - <Marca>
Estado: rascunho | aprovado em AAAA-MM-DD
## Categoria e alternativas do cliente (inclui "não fazer nada")
## Diferencial e prova
## Arquétipo (principal e secundário) e o que muda na voz e no visual
## Frase de posicionamento
## Quem não é para nós
## Lacunas
```

---

## O Brand Stack

Para garantir consistência do nível estratégico ao operacional, a essência se apoia na hierarquia da marca:

```
┌─────────────────────────────────┐
│         Brand Purpose           │  Por que existimos (Razão além do lucro)
├─────────────────────────────────┤
│         Brand Vision            │  Para onde estamos caminhando
├─────────────────────────────────┤
│         Brand Mission           │  Como chegaremos lá no dia a dia
├─────────────────────────────────┤
│         Brand Values            │  O que acreditamos (com o custo de cada crença)
├─────────────────────────────────┤
│       Brand Positioning         │  Como somos categoricamente diferentes
├─────────────────────────────────┤
│        Brand Personality        │  Como nos comportamos e arquétipos
├─────────────────────────────────┤
│         Brand Voice             │  Como nos comunicamos (Etapa 4)
└─────────────────────────────────┘
```

*Fontes: o Brand Stack vem do guia original `brand-strategy-framework`, que o atribuía a Marty Neumeier; **a atribuição não foi confirmada** em fonte primária (verificação de 2026-10-20), então tratar como estrutura de trabalho `[externo]`, sem citar Neumeier como autor. As 5 perguntas são de April Dunford. Ver também [references/fundamentos-de-marca.md](references/fundamentos-de-marca.md).*

---

## As 5 Perguntas de Posicionamento (April Dunford)

Antes de aprovar a frase final de posicionamento em `02-posicionamento.md`, responda:

1. **Alternativas Competitivas:** O que o cliente usaria ou faria se sua marca não existisse? (Inclui planilhas, processos manuais ou inércia).
2. **Atributos Únicos:** Quais capacidades, recursos ou abordagens só a sua marca tem?
3. **Valor Tangível:** Qual benefício mensurável ou alívio emocional esses atributos geram para o cliente?
4. **Alvo Bem Definido:** Quem é o cliente que mais se importa e se beneficia desesperadamente desse valor?
5. **Contexto de Categoria:** Em qual mercado você joga para que seu valor seja imediatamente óbvio e intuitive?

---

> **Produto e lançamento:** Value Proposition Canvas, STP, Category Design e posicionamento de produto para GTM estão em `revenue-gtm-e-posicionamento`. Esta skill cuida da **marca**; use aquela quando a pergunta for sobre o produto no mercado.

## Erros comuns

| Erro | Correção |
|---|---|
| Aceitar "qualidade, inovação, confiança" como credo | Pedir o custo de cada um e um exemplo de recusa real |
| Posicionamento que serve a qualquer concorrente | Rodar os dois filtros; se falhar, voltar |
| Preencher os 7 ativos para "ficar completo" | Ativo sem resposta é lacuna declarada |
| Escolher arquétipo por gosto | Mostrar efeito na voz e no visual antes |

---

## Referências Detalhadas

- [references/questionario-curto.md](references/questionario-curto.md) — Roteiro de perguntas rápidas de essência
- [references/questionario-longo.md](references/questionario-longo.md) — Workshop profundo com perguntas abertas
- [references/posicionamento.md](references/posicionamento.md) — Roteiro prático de posicionamento e diferenciação
- [references/fundamentos-de-marca.md](references/fundamentos-de-marca.md) — Propósito, visão, missão, valores, promessa, 12 arquétipos, formas de posicionar, arquitetura de marca, patrimônio, boas práticas e erros (fusão de 5 guias, inclui o canvas de posicionamento; consulta para as etapas 1 e 2)

