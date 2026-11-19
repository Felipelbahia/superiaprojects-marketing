---
# Repository: https://github.com/Felipelbahia/superiaprojects-marketing
# Status: Nativa do Projeto
name: roteiro-tiktok-60s-noticia
description: Use when escrever o roteiro de um vídeo curto de 60s (TikTok, Reels, Shorts) a partir de uma ou mais matérias jornalísticas, principalmente de tema sensível (violência, crime, saúde, luto), em série com briefing já respondido. Também quando precisar mapear loops abertos e fechados num vídeo curto, ou pontuar o hook de um vídeo de notícia.
author: Felipe Bahia (Futuro Mercado)
license: MIT
metadata:
  author: Felipe Bahia (Futuro Mercado)
  version: 1.0.0
---
# Roteiro TikTok 60s de notícia

## Overview
Compõe em um só fluxo: hook (`copy-hooks-video-curto`), nota do Hook Stack (workflow `copy-avaliacao-de-hook`), comentário de técnica por bloco (`script-roteiro-retencao`, **sem** o briefing socrático dela) e um mapa de loops com guarda de segurança do tema. Princípio: **o dado vem da matéria lida inteira, o suspense vem do dado, nunca da vítima.**

## Quando usar
- Há um briefing da série (formato, tom, quem aparece, CTA) já respondido e um bloco do vídeo com links de matérias.
- NÃO usar: vídeo sem notícia de base, vídeo longo, VSL. NÃO refazer as perguntas do briefing da série; só pergunte o que faltar para o vídeo específico.

## Entradas
1. Bloco do vídeo no `briefing-serie.md` (links, ângulo, registro de tom).
2. Matérias **lidas por completo** (WebFetch). Link fora do ar: avise o dono, use a pauta-bruta e marque `[a confirmar]`.
3. `brand/brand-voice.md`, `brand/personas.md` do projeto.

## Fluxo por vídeo (nesta ordem)
1. **Fatos.** Tabela `fato | fonte (veículo, data, link) | status` com `confirmado` ou `[a confirmar]`. Só entra no roteiro o que está na tabela. Se duas matérias divergem, registre a divergência e use o dado mais conservador.
2. **Ângulo e registro.** Uma frase de ângulo. Registro: `sério` ou `ironia seca`. Ironia só contra sistema, dado ou instituição.
3. **Painel** (uma linha cada): objetivo Going-Viral (`SAVE|SHARE|FOLLOW`) + emoção dominante (uma só), estrutura, 2 técnicas de retenção.
4. **Hook.** 3 variações (fala + tela + o que acontece no mudo), checklist visual de 8 pontos de `copy-hooks-video-curto`, nota do Hook Stack /15 para cada, escolha **uma** e justifique. Nota < 12: reescreva antes de seguir.
5. **Roteiro por blocos com tempo.** Hook 0-3s, Contexto 3-10s, Desenvolvimento 10-45s, Payoff 45-55s, CTA 55-60s (ajuste, mas some 60s). Cada bloco: fala, tela, técnica, emoção.
6. **Mapa de loops.** Tabela `loop | abre em | como abre | fecha em | como fecha`. Regras: máximo 3 loops; o loop do hook fecha só no payoff (45-55s); todos fecham até o início do CTA; loop sobre **dado ou sistema**, nunca sobre detalhe da violência. Loop sem fechamento = reescreva.
7. **Guarda de segurança** (checklist abaixo). Qualquer falha: corrija antes de entregar.
8. **Anti-slop.** Rode `geral-anti-slop` na fala e na tela. Registre que rodou.
9. **Salvar** em `roteiro.md`, formato de `references/template-roteiro.md`, status `rascunho, aguardando aprovação do dono`.

## Tamanho da fala
- 60s ≈ 155 palavras a 155 WPM, frases de 5-10 palavras.
- Gravação espontânea vem 1,3x a 1,6x mais longa que o escrito. Alvo escrito: **110 a 130 palavras faladas**, e conte-as no arquivo.

## Guarda de segurança (tema sensível)
- [ ] Zero humor com vítima ou caso individual. Ironia só contra sistema ou dado.
- [ ] Status do acusado exatamente como a matéria diz: `suspeito`, `preso`, `denunciado`, `condenado`. Suspeito não é culpado; nunca "o assassino" antes de condenação.
- [ ] Vítima sem nome, salvo necessidade e fonte; nunca foto nem apelido. Sem método, arma, local exato ou detalhe gráfico.
- [ ] Autoridade ou pessoa pública: só fato apurado, com nome como a matéria usa, cargo e fonte na tela.
- [ ] Todo número, nome, data e citação tem linha na tabela de fatos. Sem fonte: `[a confirmar]` e fora do texto final.
- [ ] Sem opinião partidária, sem "o governo precisa agir", sem indignação sem dado.
- [ ] Sem CTA de produto. CTA permitido: seguir a série, compartilhar, e (se o briefing permitir) canal de ajuda oficial (Ligue 180).
- [ ] Nada publicado sem o dono aprovar o texto final.

## Erros comuns
| Erro | Correção |
|---|---|
| Escrever a partir do resumo do feed | Ler a matéria inteira; o resumo é dado, não fonte |
| Hook que choca com a cena do crime | Hook com contraste de dados ou de sistema |
| Loop "o que aconteceu depois?" sobre a vítima | Loop sobre o dado: "e o número que ninguém soma é..." |
| Loop prometido no hook que nunca fecha | Rode a tabela de loops antes de salvar |
| Texto de 160+ palavras "porque cabe" | Corte; a fala real alonga |
| Ironia herdada da voz da marca em caso individual | Registro `sério`; ironia só no dado ou no sistema |

## Referências
- `references/template-roteiro.md`: modelo do `roteiro.md`.
- Hub 0 Mkt: `skills/copy-hooks-video-curto`, `workflows/copy-avaliacao-de-hook.md`, `skills/geral-anti-slop`, agent `audiovisual-producao-de-video`.
- Projeto Edição de Vídeo com IA: `skills/script-roteiro-retencao` (técnicas completas em `references/tecnicas-completas.md`).
