# Catálogo de etapas

Cada etapa: **Entrada** (o que ler), **Coleta** (chat, documento ou misto), **Saída** (arquivo na raiz da marca), **Aprovação** (critério que o usuário e eu conferimos antes de avançar).

Formatos de pergunta: ver `question-formats.md`. Marcas de proveniência: ver `SKILL.md`, regra 4.

## 0. Intake

- **Entrada:** pasta `_brands/<marca>/` inteira, se existir. Se o projeto já tem contexto de produto (ficha do projeto em `0 Padrões/projetos/` ou o documento de contexto de `revenue-gtm-e-posicionamento`, referência `product-marketing-context.md`), ler antes de perguntar para não repetir pergunta ao usuário.
- **Coleta:** chat, 5 perguntas.
  1. Nome e uma frase do que é (produto, serviço, pessoa, mídia).
  2. Modo: **nova** (nada existe), **estender** (há arquivos a respeitar) ou **refazer** (usuário quer recomeçar; vira `-v2`, nunca apaga).
  3. Profundidade: **curta** (cerca de 10 min por etapa, poucas perguntas e referências) ou **longa** (workshop, com perguntas abertas e referências). Pode mudar por etapa. **A profundidade não corta entregável:** todos os arquivos e seções existem nas duas; o que falta de base entra como "informação insuficiente" (`brandbook-e-ativos.md`, seção 2).
  4. Usos prioritários dos quatro: conteúdo, previsão de demanda, monitoramento de mídia, audiovisual. Define o peso da etapa 8.
  5. Restrições: o que já está decidido e não se mexe (nome, cores, logo, jurídico).
  6. ~~Escopo do brandbook~~ (removido em 2026-10-27): o brandbook tem sempre a estrutura completa e a etapa 7c é sempre feita (`brandbook-e-ativos.md`, seção 2).
  **Abertura de cada etapa, em qualquer profundidade `[usuário, 2026-10-27]`:** perguntar "quer responder as perguntas desta etapa, ou prefere que eu proponha e você aprova?", com recomendação. Se o usuário pedir "a partir de agora, proponha você", valer para as próximas etapas. O que o modelo propôs vai `[derivado]` e entra em lacunas. Registrar perguntas e respostas (ou a decisão de propor) em `_respostas/respostas-do-usuario/`.
  7. **Mapa de destinos do projeto** (`docs/mapa-de-destinos.md`, skill `geral-arquitetura-de-projeto`): se o projeto é próprio e não tem mapa, propor e criar com o usuário antes da etapa 1; se a marca é hospedada no 0 Mkt, registrar "modo 0 Mkt".
- **Saída:** `00-intake.md` com resumo, modo, profundidade, usos, restrições e a tabela de estado das etapas.
- **Aprovação:** usuário confirma o resumo. Em modo estender, listar o que foi lido e o que está fino.

## 0B. Naming (`brand-naming` - Opcional se nome indefinido)

- **Entrada:** `00-intake.md` (restrições, mercados e categoria).
- **Coleta:** Protocolo dos 6 Portais (Briefing, 5 Tipologias, Filtro Fonético, Filtro Jurídico, Filtro AEO para IA e Filtro Narrativo).
- **Saída:** `00b-naming.md` com os nomes finalistas validados, aprovação jurídica e teste de colisão semântica.
- **Aprovação:** usuário escolhe o nome final baseado nos relatórios de teste fonético e AEO.

## 1-2. Essência e Posicionamento (`brand-essence`)

- **Entrada:** `00-intake.md`, `primal-branding.md`.
- **Coleta:** misto. Escalas e A/B no chat; abertas de essência em documento.
- **Saída:** `01-essencia.md` (propósito, crenças, inimigo, história de criação, os 7 ativos) e `02-posicionamento.md` (categoria, alternativas, diferencial, arquétipo, frase de posicionamento).
- **Aprovação:** frase de posicionamento testada contra "quem não é para nós" e contra o concorrente mais próximo.

## 3. Público (`brand-audience`)

- **Entrada:** 01 e 02, `personas.md` existente.
- **Coleta:** misto. Perfil e jornada no chat; histórias reais ("a última vez que...") em documento.
- **Saída:** `personas.md` (nova versão `-vN` se já existir): 2 a 4 personas com contexto, dor, o que tentam hoje, gatilho de compra, objeção, onde consomem mídia, vocabulário próprio.
- **Aprovação:** cada persona tem pelo menos uma situação real concreta, não só demografia.

## 4. Voz e mensagem (`brand-voice-messaging`)

- **Entrada:** 01, 02, personas, `brand-voice.md` e `content-pillars.md` existentes.
- **Coleta:** chat, com escalas e A/B; reação a frases-exemplo.
- **Saída:** `brand-voice.md` (traços, escalas, exemplos certo/errado, "O que NÃO comunicar", vocabulário permitido e proibido), `content-pillars.md` (3 a 5 pilares com ângulo, formato e prova) e, **sempre, em qualquer profundidade**, `mensagens.md` (casa de mensagens: promessa, proposições, provas, mensagem por persona; com "informação insuficiente" onde faltar base; ver `../brand-voice-messaging/references/casa-de-mensagens.md`).
- **Aprovação:** cada traço de voz tem uma frase certa e uma errada; cada pilar liga a uma dor de persona.
- **Portão de desejo (opcional, profundidade longa):** auditar 5 frases-exemplo e as proposições de `mensagens.md` com a lente de texto do Sexy Canvas e o teste de apelo (`desejo.md`).

## 5. Desejo (`revenue-sexy-canvas` como consultor)

- **Entrada:** 01, 02, personas, voz.
- **Coleta:** chat, conduzida pelo protocolo consultivo da skill `revenue-sexy-canvas` (aconselha, não entrega peça): visão dos 14 do negócio, auditoria do que a marca já entrega **com evidência**, peso do público por persona (baixo, médio, alto) e três apostas. Procedimento completo, escala e teste de apelo em `desejo.md`.
- **Saída:** `05-desejo.md` com mapa de forças e lacunas, e 3 apostas de eletrificação.
- **Aprovação:** cada aposta tem item do canvas, tag de proveniência e ligação com um pilar.

## 6. Direção visual (`brand-visual-direction`)

- **Entrada:** 01, 02, voz, `style-guide.md` existente.
- **Coleta:** misto. Reação a referências (5 a 8 estilos) no chat; anexos opcionais (logo, prints, imagens-modelo).
- **Saída:** `06-direcao-visual.md`: sensação em 3 palavras, "não deve parecer", paleta preliminar, tipografia preliminar, fotografia/ilustração, movimento, referências com o porquê de cada.
- **Amostra visual:** ao propor cor, fonte ou estilo, gerar `_respostas/amostras-visuais-vN.html` para o usuário ver (regra 8 de `brand-visual-direction`). Mesmo no modo curto, DEVE conter a primeira quebra de página do site (Hero completo) e perguntar se o usuário quer opinar sobre cores e sobre a logo.
- **Versão em HTML:** ao fechar, gerar `06-direcao-visual.html` ao lado do `.md` (regra 11 da `SKILL.md` e regra 9 de `brand-visual-direction`).
- **Aprovação:** usuário aprova o moodboard descrito antes de qualquer código.
- **Portão de desejo (opcional, profundidade longa):** auditar a direção em palavras com a lente visual do Sexy Canvas; evidência indireta, grau máximo 3 (`desejo.md`). **Perguntar antes se o usuário quer fazer** (regra 10 da `SKILL.md`), com objetivo e aviso de que é opcional.

## 7. Design system (`brand-design-system`)

- **Entrada:** 06 e `style-guide.md`. Se o style-guide define paleta e fontes, eles vencem e o sistema os estende.
- **Coleta:** poucas perguntas (máximo 3, só se algo importante estiver ambíguo).
- **Saída:** `design-system/index.html` (site único autocontido, temas claro e escuro, componentes, telas, exports de tokens), `design-system/DESIGN.md` e `design-system/visual-style.md` (passo 7b: estilo portátil derivado dos tokens, para gerar imagem, carrossel e vídeo). Detalhe da especificação: prompt original registrado em `.agent/plans/Brand Builder [PLAN].md` e skill `brand-visual-style`.
- **Aprovação:** valores do site, do CSS e do DESIGN.md idênticos; contraste dos pares texto/fundo conferido nos dois temas.

## 7c. Identidade e ativos (sempre, em qualquer profundidade)

Regras de **uso** da identidade, que o design system (etapa 7) não cobre: logo, cor para impressão, tipografia, imagem, aplicações e governança. Guia completo em `references/identidade-e-ativos/` (começar por `00-indice.md`).

- **Quando entra:** sempre, em qualquer profundidade (decisão do usuário, 2026-10-27); em marca que já tem logo mas nenhuma regra de uso; entrega de arquivos a gráfica ou agência; peças fora da marca circulando.
- **Entrada:** `06-direcao-visual.md`, `design-system/tokens.json` e `DESIGN.md` aprovados, `style-guide.md` (vence em conflito), logo e arquivos que o usuário já tem.
- **Coleta:** chat, um capítulo por rodada (logo, cor, tipografia, imagem, aplicações, governança). Valores de tela vêm do `tokens.json`; **CMYK e Pantone nunca saem de fórmula**: ficam "a definir" com responsável.
- **Saída:** `identidade-e-ativos.md` na raiz da marca (nome proposto), com uma seção por capítulo e as lacunas declaradas. Inventário de ativos, quando pedido, conforme `brandbook-e-ativos.md`.
- **Aprovação:** item 16 de `qa-rubric.md`.

## 8. Ativação

Traduz a marca para os quatro usos. O peso de cada um vem do Intake.

| Uso | Arquivo em `ativacao/` | Conteúdo |
|---|---|---|
| Conteúdo | `conteudo.md` | pilares x formatos x canais, séries recorrentes, o que nunca publicar |
| Previsão de demanda | `demanda.md` | sazonalidade e gatilhos do negócio, eventos que movem a categoria, hipóteses de pico e vale, indicadores a acompanhar |
| Monitoramento de mídia | `monitoramento.md` | nome e variações de grafia, porta-vozes, concorrentes, termos da categoria, termos de risco e de crise, consultas de busca prontas, o que conta como menção positiva, neutra e negativa |
| Audiovisual | `audiovisual.md` | voz de locução, ritmo de edição, trilha e identidade sonora, regras de enquadramento, abertura e fechamento padrão, legenda e tipografia em vídeo |

- **Aprovação:** cada arquivo cita de qual etapa anterior vem cada regra (rastreabilidade) e traz ao menos um exemplo aplicado.
- **Portão de desejo (opcional, profundidade longa):** auditar os arquivos de `ativacao/` com a lente do uso (texto, visual ou produto) e o teste de apelo (`desejo.md`).

## 9. Brandbook + QA

- **Saída:** `brandbook.md`: índice que consolida e **referencia** os arquivos das etapas (não duplica texto), mais `Known Gaps` e as decisões em aberto. Profundidade (curta ou longa; mesma estrutura) , perguntas de configuração e gestão de ativos: `brandbook-e-ativos.md`.
- **Navegação, versões e lacunas:** `versoes.json` (qual versão vale), HTML gêmeo gerado por `scripts/brand_html.py`, seção "Lacunas reunidas" no `brandbook.md` e revisão de nomes e lugares (`brandbook-e-ativos.md`, seção 10; regras 13 e 14 do `SKILL.md`).
- **Registro de fontes de números:** a ativação de conteúdo, demanda e imprensa só cita número com fonte registrada. Procurar o registro no projeto; **projeto novo**: criar vazio e explicar como preencher; **projeto existente**: pedir as informações para montá-lo e explicar como atualizar (`registro-de-fontes.md`).
- **Agentes de revisão da marca (opcional, perguntar antes):** criar `brand-voice-guardian-<Marca>` e `brand-identity-guardian-<Marca>` no projeto da marca, personalizados na criação com os arquivos aprovados (procedimento, modelo e teste em `agentes-de-revisao.md`). Recomendado quando a produção é feita por agentes de IA.
- **QA:** rubrica de `qa-rubric.md`. Nota abaixo de 10 em qualquer item volta à etapa responsável. Depois de 3 voltas sem fechar, parar e perguntar ao usuário.
- Ao final, propor ao usuário (sem fazer) a linha no `style-guide.md` apontando para o `DESIGN.md` e para o `brandbook.md`.
- **Checar o que carrega a marca pelo nome.** Em marca com projeto próprio, o `CLAUDE.md` e os arquivos gêmeos (`GEMINI.md`, `AGENTS.md`, `.cursorrules`, `.claude/`, `.agent/rules/`) costumam mandar ler `brand-voice.md`, `personas.md` etc. Se a marca foi reconstruída em arquivos `-v2`, uma IA seguirá carregando a versão antiga. Propor (sem fazer) apontar as regras para a v2, mantendo a paridade entre os gêmeos (conferir com `cmp`).
- **Fichas do projeto.** Conferir se o público descrito em `0 Padrões/projetos/<Projeto>.md` bate com o público aprovado; propor correção.
- **Registrar o uso** na ficha do 0 Mkt (o que a skill aprendeu), com autorização.
- **Depois do brandbook:** conferir peças novas contra a marca com o agente `brand-voice-guardian`; as regras de uso do logo, cor para impressão, tipografia, imagem, aplicações e governança estão em `references/identidade-e-ativos/00-indice.md`.
- **Contrato para quem consome a marca (agentes e outras skills)** (em marca feita antes deste contrato, acrescentar a seção na próxima revisão do brandbook, em nova versão `-vN`): o `brandbook.md` lista, em uma seção "Arquivos para ler", os arquivos da marca na ordem de uso: `brand-voice.md`, `personas.md`, `content-pillars.md`, `style-guide.md`, e quando existirem `01-essencia.md`, `02-posicionamento.md`, `mensagens.md`, `05-desejo.md`, `06-direcao-visual.md`, `design-system/DESIGN.md`, `design-system/visual-style.md`, `identidade-e-ativos.md` e `ativacao/*`.

## Reaproveitar por referência (sem copiar conteúdo)

`brand-naming`, `brand-identidade-sonora`, `revenue-sexy-canvas` (com as referências `sexy-canvas-texto`, `sexy-canvas-visual` e `sexy-canvas-produto`), `brand-visual-style`, `site-tailwind-design-system`, `site-diretrizes-web-codigo`, `execution-loop`, `project-defines`, `brainstorming`. Fora do projeto, o `skill-resolver` acha qualquer outra (`design-system-patterns`, `visual-design-foundations` em 0 Padrões). As subskills `brand-essence` e `brand-voice-messaging` agora carregam em suas pastas `references/` os guias consolidados de estratégia de marca, extração reversa de voz e psicologia de comunicação.
