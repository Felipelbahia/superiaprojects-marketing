# Changelog — sexy-canvas

Formato: Adicionado / Alterado / Corrigido / Removido.
Versionamento: `0.1.0` entrega inicial · `0.x.0` mudança de conteúdo · `0.x.y` correção.
Regra: nova versão de documento = novo arquivo `-vN`; as anteriores não são editadas.

## [0.1.3] — 2026-10-20

Origem: padrão de nomenclatura das skills do `0 Mkt` (etapa E4.3).

### Alterado
- A skill passou a se chamar `revenue-sexy-canvas` (antes `sexy-canvas`). Só o nome mudou: pasta, `name:` do `SKILL.md` e as citações em outras skills, agentes e workflows. O conteúdo dos documentos não foi alterado. Os registros anteriores deste changelog mantêm o nome antigo, que era o nome na época.

## [0.1.2] — 2026-10-19

Origem: auditoria de skills do `0 Mkt` (execution-loops/2026_10_19/Auditoria e Deduplicacao de Skills).

### Corrigido
- `sexy-canvas-texto.md`, `sexy-canvas-visual.md` e `sexy-canvas-produto.md`: 7 ponteiros apontavam para `references/sinais.md`, `adaptacoes.md`, `sinais-estatico.md` e `sinais-movimento.md`, que não existem com esses nomes. Passaram a apontar para os arquivos reais (`sexy-canvas-<modulo>-sinais*.md` e `sexy-canvas-<modulo>-adaptacoes.md`). Só os nomes nos links mudaram; o conteúdo dos documentos não foi alterado.

### Alterado
- `SKILL.md`: a tabela de acervo passou a listar também `00`, `04`, `07`, `08`, `09`, `10`, `11` e `12`, que existiam e não eram citados.

## [0.1.1] — 2026-10-15

Origem: teste com agentes independentes (`execution-loops/2026_10_15/Sexy Canvas/05 Debug.md`).

### Alterado
- `03-protocolo-consultivo.md`: polaridade `−` permitida com grau 0 quando a peça causa o atrito do polo negativo; teto de grau 3 quando a evidência é só descrição (briefing, roteiro, lista de funcionalidades); a escala e os graus são sempre `[derivado]` (um parecer havia rotulado a régua como `[PES]`); checagem de datas da peça contra a data de hoje.
- `SKILL.md`: o anti-slop exige abrir e aplicar `.agent/workflows/ai-slop-detector.md` (os agentes de teste só "revisaram de cabeça"); nova regra 10 sobre datas e fatos.
- Agente `sexy-canvas-strategist`: mesmo ajuste do anti-slop.

### Observação
Edição no lugar, porque a skill nasceu na mesma sessão e o histórico fica neste changelog; a calibração continua em arquivos `-vN`.

## [0.1.0] — 2026-10-15

### Adicionado
- Skill-núcleo `sexy-canvas` (consultiva): os 14 itens, teoria, metodologia reconstruída, protocolo A1–A5, regras de aplicação, matriz de combinações, banco de casos, mapa de fontes.
- Lentes externas STEPPS e Hook; autochecagem do consultor a partir dos "7 pecados" de IA, UX, marketing e startups.
- Skills por meio: `sexy-canvas-texto`, `sexy-canvas-visual`, `sexy-canvas-produto`.
- Agente `sexy-canvas-strategist`.
- Régua de calibração v1 (`references/11-calibracao-v1.md`), sem casos.

### Decisões do Brainstorm (execution-loops/2026_10_15/Sexy Canvas)
- Desempate entre fontes: vale a mais detalhada; fontes complementares.
- Atuação sempre consultiva; nunca entrega a peça final.
- Mínimo 1 item, ideal 3+, sem máximo; criança interior antes dos pecados; teste de apelo.
- Sem perfil de marca gravado; predileção da marca é inferida de `_brands/` na hora.
- Sem bloco ético; sem profundidade mínima por item.
- Escala de aderência 0–4 provisória (`[derivado]`).
- Conteúdo em PT-BR.

### Conflitos entre fontes e decisões
- Energia: 14 itens; energia como qualidade transversal e como "conjunto de itens da marca".
- Recompensa: duas modalidades (espontânea e conquistada).
- Lista de Preguiça do Manual (p.6) duplicada da de Ganância: usar a do SEXYBOOK.
- Escassez fica em Segurança, conforme o Manual.
- Detalhes em `references/07-conflitos-entre-fontes.md`.

### Descartado
- Leitura de subliminares sexuais em logos.
- Estatísticas sem fonte e teses político-religiosas do autor.
- Números de alunos e de faturamento como prova.

### Conhecidas
- Metodologia reconstruída a partir de fragmentos: faltam o Módulo 0, o template oficial do canvas e o case Nubank detalhado.
- Aplicações por meio são `[derivado]`, exceto as poucas falas do autor sobre áudio, imagem e cenário.
