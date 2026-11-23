# Modelo de campanha: `campanha.md`, `resultado.md` e revisões

Uma campanha é uma estratégia com foco específico e, quando pontual, prazo definido. O `campanha.md` é o centro da pasta: quem o abre entende o que se quer, como, até quando e como saber se deu certo.

## Onde gravar

No caminho de campanha do mapa de destinos do projeto (`docs/mapa-de-destinos.md`; skill `mapa-de-destinos`). Sem mapa, o padrão direto, sem marca no caminho, é `estrategia/campanhas/AAAA-MM-DD - Nome da Campanha/`. O mapa do 0 Mkt, multi-marca, usa `content/<marca>/estrategia/campanhas/…`.

Arquivos da pasta:

- `campanha.md` (obrigatório, criado antes de começar)
- `checklist-lancamento.md` (workflow `revenue-checklist-de-lancamento-de-campanha`)
- `apresentacao.html` (opcional, passo 6 do workflow `revenue-criacao-de-campanha`)
- `resultado.md` (criado ao encerrar)
- `revisoes/` (só em campanha contínua)

As **peças** da campanha ficam em `conteudos/<tipo>/` ou `imprensa/`. O `campanha.md` aponta para elas, e cada peça leva `campanha: <id>` nos metadados.

## Pontual ou contínua

| | Pontual | Contínua |
|---|---|---|
| `tipo:` | `pontual` | `continua` |
| `fim:` | obrigatório | vazio |
| Meta | uma, para a janela inteira | uma por ciclo (mensal, trimestral), em janela rolante |
| Leitura de resultado | `resultado.md` ao fim | `revisoes/AAAA-MM_revisao.md` a cada ciclo; `resultado.md` só se a campanha encerrar |
| Critério de encerramento | a data de fim | escrito no `campanha.md` (seção 6) |

## `campanha.md` (aprovado em 2026-11-07)

```markdown
---
campanha: AAAA-MM-DD - Nome da Campanha   # id estável = nome da pasta; as peças usam o mesmo valor em `campanha:`
tipo: pontual | continua
escopo: <marca ou produto, conforme o mapa; omitir se mono-marca>
status: rascunho | aprovada | em-andamento | encerrada | cancelada
aprovada-em: AAAA-MM-DD
aprovada-por: <nome>
inicio: AAAA-MM-DD
fim: AAAA-MM-DD            # vazio se tipo: continua
revisao: mensal | trimestral   # só se tipo: continua
responsavel: <nome>
estrategia-mae: <link para estrategia/estrategia-geral.md ou o objetivo que ela serve>
---

# <Nome da Campanha>

## 1. Objetivo

Uma frase: o que muda se a campanha funcionar. Foco único e específico.

## 2. Contexto

Por que agora. O que motivou. Máximo 5 linhas.

## 3. Público e oferta

- **Persona:** <link para brand/ ou descrição>
- **O que se promove:** <produto, oferta ou mensagem central>
- **Promessa em uma frase:**
- **Verba:** <valor ou "sem verba">

## 4. Etapas, prazo e marcos

| # | Etapa | O que acontece | Responsável | Data | Status |
|---|---|---|---|---|---|
| 1 | Preparação e aprovação do plano | | | | |
| 2 | Produção das peças | | | | |
| 3 | Aprovação das peças (conforme o fluxo do mapa) | | | | |
| 4 | Lançamento | | | | |
| 5 | Checagem intermediária | | | | |
| 6 | Encerramento e leitura do resultado | | | | |

Em campanha contínua, troque as etapas 5 e 6 por "ciclo" (produção, publicação, revisão) com a cadência da revisão.

## 5. Canais e peças

| Canal | Peça (link) |
|---|---|
| | |

O status de cada peça fica na própria peça; não repetir aqui.

## 6. Resultado esperado (definido e aprovado ANTES de começar)

| Métrica | Linha de base (valor, data e fonte) | Meta | Fonte do dado | Janela de medição (datas) |
|---|---|---|---|---|
| | | | | |

**Linha de base é obrigatória:** sem valor, data e fonte, a meta não significa nada e a campanha continua em `rascunho`.

**Critério de sucesso:** o que precisa acontecer para chamar de "deu certo".

**Critério de fracasso:** o valor abaixo do qual consideramos que não funcionou.

**Faixa intermediária:** o que fazemos se o resultado ficar entre os dois.

**Premissas e riscos:** o que precisa ser verdade para a meta ser alcançável.

**Critério de encerramento (só campanha contínua):** quando a campanha para (ex.: duas revisões seguidas abaixo do critério de fracasso).

## 7. Arquivos conectados

Só o que não está nas seções acima: dados de apoio, `checklist-lancamento.md`, `apresentacao.html`, `resultado.md`.

## 8. Registro de mudanças

| Data | O que mudou | Por quê | Aprovado por |
|---|---|---|---|
```

## `resultado.md` (aprovado em 2026-11-07)

Nasce no encerramento de campanha pontual (ou ao encerrar uma contínua). Compara com a meta **como foi aprovada**, e mostra a meta vigente quando ela mudou, para a leitura ser honesta.

```markdown
---
campanha: AAAA-MM-DD - Nome da Campanha
lido-em: AAAA-MM-DD
lido-por: <nome>
veredito: sucesso | faixa-intermediaria | fracasso
decisao: repetir | ajustar-e-repetir | encerrar
---

# Resultado: <Nome da Campanha>

## Veredito em uma frase

## Esperado vs. real

| Métrica | Meta aprovada | Meta vigente (se mudou) | Real | Fonte do dado real | Diferença | Veredito |
|---|---|---|---|---|---|---|

## Verba

| Previsto | Gasto | Observação |
|---|---|---|

## Desempenho por canal e peça

| Canal | Peça (link) | Resultado | Observação |
|---|---|---|---|

## Limitações da medição

O que não conseguimos medir bem e o que pode ter distorcido o número.

## O que atribuímos à campanha e o que não

Fatores externos: sazonalidade, imprensa espontânea, mudança de preço, concorrência.

## O que funcionou

## O que não funcionou

## Decisão

repetir, ajustar e repetir, ou encerrar, com o motivo.

## Próximas ações

| Ação | Responsável | Prazo |
|---|---|---|

## O que vira regra

Aprendizado que muda como produzimos e onde ele foi registrado (`brand/`, `referencias/`, `inteligencia/estudos/`, `memory.md`).
```

## `revisoes/AAAA-MM_revisao.md` (campanha contínua; aprovado em 2026-11-07)

```markdown
---
campanha: AAAA-MM-DD - Nome da Campanha
ciclo: AAAA-MM
lido-em: AAAA-MM-DD
lido-por: <nome>
---

# Revisão <ciclo>: <Nome da Campanha>

| Métrica | Meta do ciclo | Real | Ciclo anterior | Tendência | Veredito |
|---|---|---|---|---|---|

## O que mudou neste ciclo

## Ajuste decidido

O que muda no próximo ciclo e por quê. Se a meta mudar, registrar também na seção 8 do `campanha.md`.

## Alerta de encerramento

Aplica o critério de encerramento do `campanha.md`? Sim ou não, e quantos ciclos faltam.
```

## Regras de preenchimento

1. **Meta e critérios antes de executar.** Meta escrita depois vira justificativa.
2. **Linha de base com valor, data e fonte.** Sem isso a campanha não sai de `rascunho`.
3. **Mudança depois da aprovação** entra na seção 8, com motivo e aprovador. O `resultado.md` mostra a meta aprovada e a vigente.
4. **Peça como link, não cópia.** Status da peça só na peça.
5. **O texto das peças** passa pelo `/geral-anti-slop`; o `campanha.md` é documento de trabalho, escrito direto e sem enfeite.
