# Etapa 5: Desejo (com o Sexy Canvas)

Detalha a etapa 5 do `brand-builder`. A etapa usa a skill `revenue-sexy-canvas` (Sexy Canvas, André Diamand) **como consultora**: ela dá parecer e encaminhamento sobre os 14 motores emocionais; **nunca entrega a peça**. Quem executa é a skill da etapa de destino. O agente `revenue-parecer-sexy-canvas` pode conduzir o parecer.

**Origem (E5, 2026-10-20):** procedimento escrito para o `brand-builder` a partir do protocolo da skill `revenue-sexy-canvas` (`SKILL.md`, `references/03-protocolo-consultivo.md` e `references/10-erros-do-consultor.md`, dentro da pasta dessa skill). A escala, a regra de evidência e o teste de apelo são do Canvas; o mapa de forças e lacunas, o peso do público por persona e o portão de desejo são adaptações `[derivado]`.

**Princípio:** desejo não se inventa em cima de nada. A marca já tem essência, posicionamento, público e voz aprovados; o Canvas mostra **quais desejos a marca já ativa, quais o público pesa e quais valem apostar**, com evidência.

## Antes de começar
1. `01-essencia.md`, `02-posicionamento.md`, `personas.md` e `brand-voice.md` aprovados (ou lacunas declaradas). Se existir, `mensagens.md` (casa de mensagens).
2. Ler `../revenue-sexy-canvas/SKILL.md` e `../revenue-sexy-canvas/references/03-protocolo-consultivo.md`. Conforme o meio, a referência de texto, visual ou produto (`sexy-canvas-texto.md`, `sexy-canvas-visual.md`, `sexy-canvas-produto.md`). Ler só o necessário.
3. Respeitar o "O que NÃO comunicar" da marca.
4. Ler `question-formats.md`.

## Procedimento

| Passo | O que faz | Atuação do Canvas |
|---|---|---|
| 1 | Confirmar contexto: marca, público, objetivo, canal. Se faltar, perguntar antes de opinar | — |
| 2 | **Visão dos 14 do negócio:** como cada um dos 14 itens se conecta à marca, com encaixe (cabe, cabe com cuidado, não cabe) e uma linha de orientação; fechar com os 3 de maior potencial | **A5** (não precisa de peça) |
| 3 | **O que a marca já entrega:** auditar o material que existe (site, perfil, textos aprovados, descrição do produto) item por item, com grau, polaridade e **evidência**. Sem material, pular e declarar | **A1** |
| 4 | **Peso para o público:** por persona, marcar baixo, médio ou alto para cada item relevante, derivado das dores, gatilhos e objeções aprovadas. É `[derivado]`; o usuário corrige | — |
| 5 | **Mapa de forças e lacunas:** cruzar passo 3 e 4 (ver tabela) | — |
| 6 | **Três apostas:** itens recomendados, ordem de prioridade, onde entram (voz, visual, mensagem, ativação), riscos e dose | **A2** (sugestão, se o passo 3 rodou) ou **A4** (direcionamento, se não havia material para auditar) |
| 7 | **Teste de apelo** em cada aposta (6 perguntas do protocolo) contra a voz e o "O que NÃO comunicar" | Teste de apelo |
| 8 | **Autochecagem** do parecer com `../revenue-sexy-canvas/references/10-erros-do-consultor.md`; texto passa pelo `/ai-slop-detector` | — |
| 9 | **Handoff** (ver abaixo) e aprovação do usuário com o resumo à vista | Handoff |

### Regras da escala (do protocolo do Canvas)
- Grau de **0 (ausente) a 4 (central)**, com polaridade `+` (eletrifica), `−` (eletrificação negativa: frustra, irrita, atrita) ou `±`. A escala e os graus são sempre `[derivado]`; nunca rotular como `[Diamand]` nem `[PES]`.
- **Evidência obrigatória:** o trecho ou elemento observado, não a impressão geral. Sem evidência, o grau máximo é 1.
- **Evidência indireta** (só descrição, briefing ou resumo, e não a peça): o grau máximo é 3, e o parecer diz isso.
- Mínimo de 1 item; ideal 3 ou mais. **Criança interior antes dos pecados.** Segurança é piso, não diferencial; Ganância sozinha não diferencia.
- Comparar datas da peça com a data de hoje e avisar se o texto ficou desatualizado.

### Mapa de forças e lacunas
| Entrega da marca (grau) | Peso para o público | Leitura |
|---|---|---|
| Alto (3 ou 4) | Alto | **Força**: manter e mostrar |
| Baixo (0 a 1) | Alto | **Lacuna**: candidata a aposta |
| Alto | Baixo | **Excesso**: a marca insiste onde o público pesa pouco |
| Baixo | Baixo | Ignorar |

### Teste de apelo (para cada aposta)
Aplicar as 6 perguntas do "Teste de apelo" do protocolo (`../revenue-sexy-canvas/references/03-protocolo-consultivo.md`, seção "Teste de apelo"), que checam ligação com o benefício real, coerência com o tom e o "O que NÃO comunicar", credibilidade para o público, dose, excesso de itens e dependência de algo que a marca não entrega. Qualquer "não" nas perguntas 1 a 3 reduz o veredito. Veredito: **passa**, **passa com cuidado** (dizer qual) ou **barra** (dizer por quê). Aposta barrada volta ao passo 6. As perguntas ficam só no protocolo, para não divergir quando o Canvas for recalibrado.

### Handoff
Para cada aposta aprovada: item do Canvas e grau-alvo; onde entra (voz, mensagem, direção visual, ativação); restrição da marca; **quem executa** (a skill da etapa: `brand-voice-messaging`, `brand-visual-direction`, ou `ativacao.md`) e o que recebe. Se uma aposta contradiz a voz aprovada, o parecer **volta à etapa 4** antes de seguir.

## Saída: `05-desejo.md`

```
# Desejo - <Marca>
Estado: rascunho | aprovado em AAAA-MM-DD
## Contexto (marca, público, objetivo, canal)
## Visão dos 14 do negócio (encaixe e orientação; 3 de maior potencial)
## O que a marca já entrega (tabela: item, grau, polaridade, evidência) | "sem material" se for o caso
## Peso para o público (por persona)
## Mapa de forças e lacunas
## Três apostas (item, motivo, onde entra, risco e dose, tag, pilar ligado)
## Teste de apelo (veredito por aposta)
## Handoff (por aposta: quem executa e o que recebe)
## Lacunas
```

Tags: a escala é `[derivado]`; regras do Canvas citam a fonte (`[Diamand]`, `[PES]`, `[externo]`) como na skill.

**Critério de aprovação (do catálogo):** cada aposta tem item do Canvas, tag de proveniência e ligação com um pilar de conteúdo.

## Portão de desejo nas outras etapas (opcional, profundidade longa)

Ao fechar uma etapa de saída, rodar A1 com a lente certa e o teste de apelo antes da aprovação final. Na profundidade curta, só a etapa 5.

**Perguntar antes, sempre** (regra 10 da `SKILL.md`): o portão não roda nem é pulado sem o usuário decidir. A pergunta diz o **objetivo** ("ver se o que a etapa produziu ativa o desejo certo no público, com evidência"), que é **opcional** e a recomendação (rodar quando a etapa define como a marca será percebida, como 4 e 6; dispensar em ajuste pontual). O resultado ou a dispensa vai para o log da etapa.

| Etapa | O que auditar | Lente | Cuidado |
|---|---|---|---|
| 4 Voz e mensagem | 5 frases-exemplo da voz (uma por canal) e as proposições de `mensagens.md` | Texto (`sexy-canvas-texto.md`) | Frase isolada pode mostrar poucos itens; auditar o conjunto |
| 6 Direção visual | A direção **em palavras** | Visual (`sexy-canvas-visual.md`) | **Evidência indireta: grau máximo 3** |
| 8 Ativação | Os arquivos de `ativacao/` e uma pauta de exemplo | Texto, visual e produto, conforme o uso | — |

## Erros comuns
| Erro | Correção |
|---|---|
| Nota por opinião sem evidência | Grau com trecho observado; sem evidência, máximo 1 |
| Rodar só na etapa 5 e esquecer o teste de apelo | O teste é obrigatório em cada aposta |
| Entregar a peça final | O Canvas aconselha; quem executa é a skill da etapa |
| Aposta que contradiz a voz | Voltar à etapa 4, não forçar |
| Apostar só em pecados | Criança interior primeiro; segurança é piso |
| Tratar a escala como do autor | A escala é `[derivado]` e calibrável (`11-calibracao-v1.md` do Canvas) |
| Aplicar os 14 em marca nova sem material | Rodar só A5 e A4, e declarar que o passo 3 foi pulado |

## O que não fazer
- Não gravar perfil de desejo da marca fora da raiz da marca (`<raiz>/05-desejo.md`; `_brands/<marca>/` no 0 Mkt, `<projeto>/brand/` em projeto próprio).
- Não editar a raiz da marca sem aprovação do usuário (regra do `brand-builder`).
- Não prometer resultado de conversão: o Canvas diagnostica, não prevê.
