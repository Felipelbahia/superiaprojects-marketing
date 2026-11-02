---
name: brand-audience
description: "Use para definir ou refazer personas, segmentos, jobs to be done, objeções e hábitos de mídia de uma marca (etapa 3 do brand-builder). Gatilhos: \"persona da marca\", \"público da marca\", \"personas finas\". NÃO use para ICP, pontuação de aderência e JTBD de produto em geral (use persona-icp) nem para validar ideia com entrevistas (use persona-descoberta-de-clientes)."
license: MIT
metadata:
  author: Antigravity Multi-IA Hub & Felipe Bahia (Futuro Mercado)
  version: 1.0.0
---

# Brand Audience

## Overview

Etapa 3 do `brand-builder`. Produz `personas.md` com pessoas reais em situação real, não só demografia. O arquivo precisa servir a quatro usos: pauta de conteúdo, previsão de demanda (quem compra quando e por quê), monitoramento de mídia (onde e como falam) e audiovisual (quem aparece e como se fala com essa pessoa).

**Princípio central: persona sem cena concreta é estereótipo. Toda persona nasce de uma situação vivida.**

## Antes de começar

1. `01-essencia.md` e `02-posicionamento.md` aprovados, ou lacunas declaradas.
2. Ler o `personas.md` existente. Ele só é base **se descreve o mesmo público que o Intake e a essência**. Se o público mudou ou diverge (ex.: personas de gestor corporativo para um produto de vendedores autônomos), descartar como base, avisar o usuário e partir do zero; o arquivo antigo fica preservado e a nova versão é `-v2`.
3. Ler `../brand-builder/question-formats.md`.

## Fluxo

| Passo | O que faz | Referência |
|---|---|---|
| 1 | Levantar segmentos candidatos a partir do posicionamento e propor 2 a 4 para o usuário escolher | `references/roteiro-persona.md`, rodada 1 |
| 2 | Situação real por segmento ("a última vez que...") | rodada 2 |
| 3 | Dor, tentativa atual, gatilho, objeção | rodada 3 |
| 4 | Mídia, vocabulário e sinais de demanda | rodada 4 |
| 5 | Anti-persona e prioridade | rodada 5 |
| 6 | Redigir, rodar `/geral-anti-slop`, mostrar, aprovar | |

Curta: passos 1, 2, 3 e 5 com 1 a 2 personas. Longa: todos, 3 a 4 personas, com pedido de dados reais (comentários, DMs, tickets, entrevistas) quando o usuário tiver.

## Regras

0. **Segmento antes de persona.** O primeiro passo é decidir QUEM são as pessoas em termos de profissão, situação e tamanho de rotina (ex.: corretor de imóveis, representante comercial, prestador autônomo), com exemplos concretos. Perguntar de forma aberta, não só ofertar segmentos prontos: o usuário conhece o público melhor que a skill. Persona genérica de "gestor" ou "dono de pequena empresa" como padrão é erro.
1. **Nada inventado como fato.** Dados de mercado, tamanhos e porcentagens só entram com fonte do usuário ou busca confirmada. O resto é `[derivado]` ou hipótese rotulada.
2. **Cena por persona:** pelo menos uma situação real concreta, com data aproximada, lugar e o que a pessoa fez.
3. **Estágio de consciência** de cada persona sobre o problema (não sabe, sabe o problema, sabe soluções, compara marcas, pronto para comprar). Modelo clássico de Eugene Schwartz, `[externo]`, usado como lente.
4. **Vocabulário na boca do público:** termos exatos que a persona usa para descrever a dor, sem tradução para jargão da marca. Alimenta a voz e o monitoramento.
5. **Sinais de demanda:** o que faz essa persona procurar a solução em certos momentos (evento, estação, prazo, notícia). Alimenta `ativacao/demanda.md`.
6. **Onde fala e onde ouve:** canais, comunidades, veículos e formatos. Alimenta `ativacao/monitoramento.md`.
7. **Anti-persona** obrigatória: quem a marca não quer atrair e o motivo.
8. Não usar nome, foto ou história de pessoa real identificável. Personas são compostas.

## Saída: `personas.md`

```
# Personas - <Marca>
Estado: rascunho | aprovado em AAAA-MM-DD
## Prioridade (ordem e porquê)
## Persona 1: nome fictício, papel
Contexto / Cena real / Dor (nas palavras dela) / O que tenta hoje /
Gatilho de busca / Objeção / Estágio de consciência /
Onde fala e onde ouve / Vocabulário / O que a faria confiar / Sinais de demanda
## Persona 2 ...
## Anti-persona
## Lacunas e hipóteses a validar
```

## Erros comuns

| Erro | Correção |
|---|---|
| Persona por idade, cidade e renda | Pedir a cena e a dor em palavras dela |
| Quatro personas iguais com nomes diferentes | Cada persona deve exigir uma pauta diferente; se não, fundir |
| Inventar estatística para dar peso | Sem fonte, rotular como hipótese |
| Persona que só elogia a marca | Incluir objeção real e motivo de abandono |
| Esquecer sinais de demanda e mídia | Sem eles a etapa 8 fica sem base |
