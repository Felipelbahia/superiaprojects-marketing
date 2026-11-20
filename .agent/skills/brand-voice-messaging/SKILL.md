---
# Repository: https://github.com/Felipelbahia/superiaprojects-marketing
# Status: Customizada / Modificada localmente por Felipe Bahia
name: brand-voice-messaging
description: "Use para definir ou refazer tom de voz, vocabulário, \"o que NÃO comunicar\", mensagens e pilares de conteúdo de uma marca (etapa 4 do brand-builder), ou extrair a voz de textos existentes. Gatilhos: \"tom de voz\", \"brand voice\", \"pilares de conteúdo\", \"o que não comunicar\". NÃO use para escrever a peça (use copy-conversao), planejar calendário e formatos (use conteudo-estrategia) nem limpar texto com cara de IA (use geral-anti-slop)."
author: Antigravity Multi-IA Hub & Felipe Bahia (Futuro Mercado)
license: MIT
metadata:
  author: Antigravity Multi-IA Hub & Felipe Bahia (Futuro Mercado)
  version: 1.2.0
---
# Brand Voice & Messaging

## Overview

Etapa 4 do `brand-builder`. Produz `brand-voice.md`, `content-pillars.md`, `glossario.md` e `depoimentos.md` com **voz testável**: cada traço traz frase certa e frase errada, cada pilar nasce de uma dor real do público e de um ativo da essência, a terminologia segue regras estritas de tradução e a prova social obedece a matriz de consentimento granular.

**Crédito de Origem:** Conceitos de arquitetura de contexto, integridade terminológica e precedência de dados adaptados a partir de `promovaweb/inboundfy` (licença AGPL-3.0), redigidos com estrutura e regras autorais exclusivas do ecossistema Super IA Projects `0 Mkt`.

**Princípio central: voz que não se consegue errar não é voz. Exigir o contraexemplo.**

## Antes de começar

1. `01-essencia.md`, `02-posicionamento.md` e `personas.md` aprovados (ou lacunas declaradas ao usuário).
2. Ler os `brand-voice.md`, `content-pillars.md`, `glossario.md` e `depoimentos.md` existentes. Se existem, base e vence; nova versão é `-v2`.
3. Ler `../brand-builder/question-formats.md`.

## Fluxo

| Passo | O que faz | Referência |
|---|---|---|
| 1 | Pré-preencher a partir do que já foi aprovado e mostrar ao usuário | `references/derivacao.md` |
| 2 | Rodada de escalas (1-5) e A/B | `references/roteiro-voz.md`, rodada 1 |
| 3 | Escalonamento de intensidade com a mesma mensagem | rodada 2 |
| 4 | Reação a frases-exemplo (amo/aceito/evito/nunca) | rodada 3 |
| 5 | Vocabulário, "O que NÃO comunicar" e Glossário de Marca (tabela em 4 colunas com regras de tradução) | `references/glossario-de-marca.md`, rodada 4 |
| 6 | Pilares de conteúdo | `references/pilares.md` |
| 6b | Casa de mensagens: promessa, proposições, provas e mensagem por persona (saída `mensagens.md`) | `references/casa-de-mensagens.md` |
| 6c | **Opcional** (perguntar antes, regra 10): assinatura da marca (slogan), ou a decisão de não ter um; registrada em `mensagens.md` | `references/slogan.md` |
| 6d | Governança de Depoimentos e Prova Social: fala literal e consentimento explícito por canal de distribuição | `references/depoimentos-e-prova-social.md` |
| 7 | Redigir, aplicar precedência em 5 níveis (com trava anti-resolução silenciosa), rodar `/geral-anti-slop`, validar via ciclo formal | `references/ordem-de-precedencia-de-fontes.md`, `references/ciclo-de-validacao-de-pecas.md` |

Profundidade curta: passos 1, 2, 5 e 6, com 2 a 3 rodadas. Longa: todos, mais as frases-exemplo geradas para três canais.

## Regras

1. **Traço sem exemplo não entra.** Cada traço: definição, uma frase certa, uma frase errada, e o que fazer quando em dúvida.
2. **"O que NÃO comunicar"** é obrigatória, com no mínimo 5 itens específicos (afirmações, promessas, temas, formas de ironia, palavras). "Evitar linguagem negativa" não conta. Vem de: credo, não-crente, limites de território e arquétipo.
3. **Vocabulário e Glossário:** lista de termos preferidos, lista de termos banidos e matriz de termos que **não se traduzem** (marcas, siglas, termos técnicos de mercado, metodologias proprietárias) versus termos que **se traduzem**. Nenhuma peça final pode sair com termo marcado como pendente de confirmação.
4. **Escalas registradas** como número, para o monitoramento de consistência e o briefing audiovisual usarem depois.
5. **Voz por contexto:** tabela curta de como a voz varia por canal e momento (vendas, suporte, crise, bastidor), sem trair os traços.
6. Os pilares: 3 a 5, cada um com ângulo, formatos que o sustentam, prova e a dor de persona que atende.
7. **Precedência e Não-Silenciamento:** fontes em conflito obedecem à escala em 5 níveis (Usuário > Marca > Canal/Briefing > Externo com Prova > Hipótese). Conflitos materiais entre fontes travam o fluxo; a IA nunca resolve discrepâncias em silêncio.
8. **Depoimentos Literais e Consentimento:** depoimentos devem reproduzir aspas exatas sem embelezamento da IA e só podem ser veiculados nos canais onde houver autorização explícita registrada na matriz de consentimento.
9. Texto passa pelo `/geral-anti-slop`.

## Saída: `brand-voice.md`

```
# Brand Voice - <Marca>
Estado: rascunho | aprovado em AAAA-MM-DD
## Resumo em 3 palavras e uma frase
## Traços (cada um: definição / certo / errado / em dúvida)
## Escalas (número 1-5 por eixo)
## Voz por contexto
## Vocabulário preferido / vocabulário banido
## O que NÃO comunicar
## Afirmações que exigem confirmação humana
## Restrições específicas por canal e audiência
## Lacunas
```

## Saída: `content-pillars.md`

```
# Pilares - <Marca>
## Pilar 1: nome
Dor atendida / ativo da essência / ângulo / formatos / prova / exemplo de pauta
...
## O que fica fora dos pilares
```

## Saída: `glossario.md`

```
# Glossário Oficial - <Marca>
Tabela de 4 colunas: Expressão Original / Escrita Oficial / Grafias Vetadas / Regra de Tradução & Notas
```

## Saída: `depoimentos.md`

```
# Acervo de Depoimentos - <Marca>
Registros com Fala Literal (aspas exatas) e Matriz de Consentimento por Canal
```

## Modos de Operação

Esta skill opera em dois modos distintos dependendo do estado da marca:

| Modo | Quando usar | Como opera | Referência |
|---|---|---|---|
| **Modo 1: Extract** | A marca/fundador já tem conteúdos que soam exatamente como deseja (posts, e-mails, vídeos) | Analisa 3 a 5 textos reais, detecta padrões de ritmo, pontuação, vocabulário e extrai o perfil | `references/brand-voice-extractor.md` |
| **Modo 2: Build** | Marca nova começando do zero ou que deseja reposicionar intencionalmente o tom | Roteiro guiado por questionário, escalas A/B e testes de intensidade | `references/roteiro-voz.md` e `references/brand-voice-extractor.md` (15 perguntas) |

---

## As 5 Dimensões do Espectro de Tom

Toda voz de marca deve ser calibrada numericamente de 1 a 5 em cinco eixos fundamentais:

```
1. Formal (1) ◄─────────────────────────────────────────► Informal (5)
2. Sério & Solene (1) ◄────────────────────────────────► Bem-humorado & Descontraído (5)
3. Técnico & Acadêmico (1) ◄───────────────────────────► Simples & Acessível (5)
4. Reservado & Analítico (1) ◄─────────────────────────► Expressivo & Acalorado (5)
5. Convencional (1) ◄──────────────────────────────────► Rebelde & Provocador (5)
```

*Ver [references/brand-voice.md](references/brand-voice.md) e [references/voice-tone.md](references/voice-tone.md).*

---

## Erros comuns

| Erro | Correção |
|---|---|
| Traços tipo "autêntico, inovador, próximo" | Exigir certo/errado; sem isso, cortar |
| "Não comunicar" genérico | Exigir 5 itens que um redator poderia violar sem perceber |
| Pilares como temas amplos ("educação") | Pilar = ângulo + dor + prova |
| Traduzir termos técnicos consolidados ou siglas | Seguir estritamente o `glossario.md` da marca |
| Corrigir ou arbitrar conflitos de dados em silêncio | Travar o fluxo e exigir decisão humana via `ordem-de-precedencia-de-fontes.md` |
| Inventar ou polir falas de clientes | Registrar falas literais ipsis litteris e respeitar matriz em `depoimentos.md` |
| Copiar voz de outra marca por afinidade | Reação a referências extrai padrão; não clona |
| Perder a escala numérica | Registrar números: é o que permite checar consistência depois |

---

## Referências Detalhadas

- [references/derivacao.md](references/derivacao.md): derivação de voz a partir de essência e público
- [references/roteiro-voz.md](references/roteiro-voz.md): questionário e rodadas de escalas A/B
- [references/pilares.md](references/pilares.md): metodologia de estruturação de pilares de conteúdo
- [references/glossario-de-marca.md](references/glossario-de-marca.md): diretrizes de glossário em 4 colunas, categorização binária de tradução e trava de termos pendentes
- [references/ordem-de-precedencia-de-fontes.md](references/ordem-de-precedencia-de-fontes.md): hierarquia de precedência em 5 níveis, trava de conflito fático e proibição de resolução silenciosa
- [references/depoimentos-e-prova-social.md](references/depoimentos-e-prova-social.md): acervo estruturado de prova social com falas literais e matriz de consentimento granular por canal
- [references/casa-de-mensagens.md](references/casa-de-mensagens.md): o que a marca diz (promessa, proposições de valor, provas, mensagem por persona), com teste de roteiro de marca e de aderência
- [references/slogan.md](references/slogan.md): assinatura da marca (slogan), opcional: quando recomendar "sem slogan", filtro de corte, oito testes e registro em `mensagens.md`
- [references/brand-voice-extractor.md](references/brand-voice-extractor.md): extrair, construir e auditar voz (guia único, com portões de amostra, validação A/B e auditoria de frase)
- [references/brand-voice.md](references/brand-voice.md): voz preservada ao escrever com IA (rascunho primeiro, 3 perguntas do leitor, marcadores de texto genérico)
- [references/voice-tone.md](references/voice-tone.md): tom por situação e canal, escopos de entrega do guia, playbooks, mensagem por persona e terminologia
- [references/sample-output-brand-voice.md](references/sample-output-brand-voice.md): exemplo de perfil de voz extraído de LinkedIn, e-mail e site
- [references/agentkits-brand-voice-guidelines.md](references/agentkits-brand-voice-guidelines.md): **exemplo preenchido** do guia de voz de outra marca (AgentKits); não é método nem a nossa voz, serve de modelo de formato
- [references/ciclo-de-validacao-de-pecas.md](references/ciclo-de-validacao-de-pecas.md): ciclo formal de validação de peças de conteúdo, parecer de reprovação em 5 campos, releitura integral na v2 e governança de aprendizado com 4 alcances e 4 estados

---

## Version History

| Version | Date | Changes |
|---------|------|---------|
| 1.2.0 | 2026-11-20 | Glossário de marca em 4 colunas (`glossario-de-marca.md`), ordem de precedência de fontes em 5 níveis com trava anti-resolução silenciosa (`ordem-de-precedencia-de-fontes.md`), governança de depoimentos literais com matriz de consentimento por canal (`depoimentos-e-prova-social.md`), templates em `_brands/brand-template/` (`glossario.md`, `depoimentos.md`, seções 5 e 6 em `brand-voice.md`) e proteção estrutural em `_brands/README.md` (inbox 2035 - Leva 1); crédito conceitual a `promovaweb/inboundfy` |
| 1.1.0 | 2026-11-20 | Ciclo formal de validação de peças de conteúdo em `ciclo-de-validacao-de-pecas.md` (parecer de 5 campos, separação produtora x revisora, releitura integral na v2 e governança de aprendizado com alcance/estados no template `_brands/brand-template/aprendizado.md`) (inbox 2037); crédito conceitual a `promovaweb/inboundfy` |
| 1.0.0 | 2026-10-18 | Versão inicial da skill |
