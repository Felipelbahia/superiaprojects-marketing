---
name: conteudo-linha-de-producao
description: "Use when: orquestrar a linha de produção unificada de conteúdo de alta retenção e conversão para Reels, TikTok, Shorts e Carrosséis; conecta a marca ativa (_brands/), psicologia comportamental (revenue-sexy-canvas), mineração de dados (hook-mining), engenharia reversa (reel-analyzer e viral-carousel), geração de carrosséis via IA (social-carrossel e social-direcao-de-arte-ia), retenção visual (copy-hooks-video-curto), motores de mídia (Remotion, no projeto de edição de vídeo) e filtro anti-slop."
license: MIT
metadata:
  author: Antigravity Multi-IA Hub & Felipe Bahia (Futuro Mercado)
  version: 1.0.0
---

# Content Factory — Esteira Unificada de Produção de Conteúdo

> **Visão Geral:** O `conteudo-linha-de-producao` é o motor orquestrador do `0 Mkt`. Ele integra todas as skills analíticas, psicológicas e operacionais em uma linha de montagem de 8 etapas, transformando dados brutos de concorrentes e inteligência de marca em peças finais prontas para gravação ou renderização automatizada.

---

## 🏭 A Esteira de Produção em 8 Etapas

```
[ 1. MARCA ATIVA ] ──> [ 2. OBJETIVO & SEXY CANVAS ] ──> [ 3. PESQUISA & MINERAÇÃO ]
                                                                     │
[ 6. RENDERIZAÇÃO ] <── [ 5. ROTEIRO & PAYOFF ] <── [ 4. HOOK 0-3s VISUAL/FALADO ]
         │
         ▼
[ 7. LEGENDA & DM ] ──> [ 8. AUDITORIA ANTI-SLOP ] ──> [ OUTPUT FINAL EM CONTENT/ ]
```

---

### Etapa 1: Identificação e Carregamento da Marca Ativa
- **Regra STOP Mandatória:** Se a marca não estiver especificada na requisição do usuário, PARE imediatamente e pergunte qual marca deve ser ativada (`plinq`, `waimonitor`, `pr-pulse`, `felipe-bahia`, `plus-pr`, `cada-dia-um-absurdo` ou `experimentacao`).
- **Carregamento de Contexto:** Ler obrigatoriamente os 4 arquivos em `_brands/<marca>/`:
  1. `brand-voice.md` (Tom, palavras proibidas e diretrizes de comunicação).
  2. `personas.md` (Dores viscerais, desejos e objeções reais).
  3. `content-pillars.md` (Pilares temáticos e formatos autorizados).
  4. `style-guide.md` (Identidade visual, regras de contraste e formatação).

---

### Etapa 2: Definição do Objetivo Algorítmico & Sexy Canvas
- **Objetivo Going-Viral (Escolha Única):**
  - `SAVE` (Alívio + Medo de Esquecer)
  - `SHARE` (Indignação / Prova de Status)
  - `FOLLOW` (FOMO + Aspiração)
  - `LEAD` (Ganância + Curiosidade Terminal)
- **Mapeamento Sexy Canvas (`.agent/skills/revenue-sexy-canvas/`):**
  - Mapear qual dos 14 itens (7 pecados capitais ou 7 itens da criança interior) será ativado no gancho e na solução.
  - Exemplo: Inveja + Ganância para PR Pulse; Medo + Criança Protegida para Plinq; Preguiça + Segurança para WaiMonitor.

---

### Etapa 3: Pesquisa & Engenharia Reversa Baseada em Dados
Escolha a rota de inteligência conforme a demanda:
- **Rota A — Mineração de Ganchos (`hook-mining`):**
  - Extrair títulos de concorrentes via `yt-dlp` (`yt-dlp --flat-playlist --print "%(title)s,%(view_count)s" <url> > shorts.csv`).
  - Executar `python3 .agent/skills/hook-mining/scripts/mine_hooks.py shorts.csv --top 20`.
  - Selecionar os 3 padrões mais frequentes (ex: `contrarian`, `secret-gap`, `result-proof`) e aplicar o framework de remix trocando as variáveis para a marca ativa.
- **Rota B — Engenharia Reversa de Vídeo (`reel-analyzer`):**
  - Desmontar um vídeo concorrente de alta performance em 5 camadas (Hook, Beats, Pacing, Técnica Visual e Remake Blueprint).
- **Rota C — Engenharia Reversa de Carrossel (`viral-carousel`):**
  - Desmontar um carrossel viral em 4 eixos (Scroll-stopper, Mapeamento de Prova, Slide de Salvamento e Slide Jobs).

---

### Etapa 4: Validação do Hook (0 a 3s)
Passe o gancho formulado pela validação dupla de `copy-hooks-video-curto`:
1. **Checklist Falado (1-3s):**
   - Segmentação imediata nos primeiros 500ms?
   - Promessa de valor ou loop aberto claro?
   - Uma única emoção ativada?
2. **Checklist Visual de 8 Pontos (0-3s):**
   - [ ] 1. Frame 0 já se move.
   - [ ] 2. Frame 0 mostra algo reconhecível (UI, objeto, problema).
   - [ ] 3. Elemento principal ocupa 40%+ da área.
   - [ ] 4. Evento extraordinário acontece antes de 3s.
   - [ ] 5. Promessa entra entre 1,2s e 1,6s palavra por palavra.
   - [ ] 6. Primeira palavra falada em até 0,5s.
   - [ ] 7. Funciona 100% no mudo.
   - [ ] 8. Fala do negócio do espectador (não da IA nem de você).

---

### Etapa 5: Roteiro & Beats com Payoff Postergado (Incentivized Wait)
- **Estruturação da Linha do Tempo (30 a 50 segundos):**
  - `00:00 - 00:03` [Hook & Promessa]: Promessa do segredo / item de maior impacto (ex: "o passo 4").
  - `00:03 - 00:10` [Agitação]: Mostrar a tela do erro ou custo de não resolver.
  - `00:10 - 00:25` [Mecânica / Demonstração]: Passos 1 a 3 com cuts rápidos a cada 2 segundos.
  - `00:25 - 00:35` [Payoff Postergado]: Revelação do item prometido no segundo 0 com ancoragem lenta.
  - `00:35 - 00:42` [CTA na DM]: Instrução para comentar palavra-chave.
- **Contagem Visual:** Incluir marcador na tela (Passo 1 a 4) sustentando a retenção cognitiva.

---

### Etapa 6: Direcionamento de Renderização Audiovisual
Conforme o formato da peça:
- **Vídeo Programático / Motion:** Para codificar o vídeo em React (Remotion), usar o projeto de edição de vídeo (`Compartilhado/Edição de Vídeo com IA`), onde a skill `remotion` vive; para montagem e overlay, usar `media-processing`, que também foi removida para no projeto de edição de vídeo (`Compartilhado/Edição de Vídeo com IA`).
- **Vídeo com Narração / Avatar:** Usar `elevenlabs` e HeyGen, skills removidas do 0 Mkt que vivem no projeto de edição de vídeo (`Compartilhado/Edição de Vídeo com IA`).
- **Carrossel via Modelos de Imagem de IA (Padrão Oficial 0 Mkt):**
  1. *Planejamento & Copy:* Executar `.agent/skills/social-carrossel/SKILL.md` para estruturação de 6 a 8 lâminas com teto de ~25 palavras de corpo, gancho agressivo no Slide 1, entrega de valor imediata no Slide 2 e Slide de Salvamento (Save-Bait) com checklist/matriz no Slide 5 ou 6.
  2. *Direção de Arte & Prompts:* Executar `.agent/skills/social-direcao-de-arte-ia/SKILL.md` para injeção dinâmica de tokens da marca ativa (`_brands/<marca>/style-guide.md`) e aplicação do Workflow do Slide Âncora (3 variantes divergentes no Hook/Slide 2, travamento da referência e propagação de consistência 4:5 para as lâminas seguintes).
  3. *Engenharia Reversa Prévia (Opcional):* Utilizar `.agent/skills/viral-carousel/SKILL.md` caso a peça tenha origem em dissecação analítica de concorrente em 4 eixos cognitivos.

---

### Etapa 7: Legenda & Protocolo de Conversão Comentário → DM
- **Estrutura da Legenda:**
  - *Linha 1:* Palavra-chave em destaque + promessa direta (ex: *"Comente AUDITORIA para receber a planilha completa na sua DM"*).
  - *Corpo:* Resumo dos 3 pontos principais abordados na peça.
  - *Proibição Estrita:* NUNCA inserir link na legenda ou comentários públicos (penalidade algorítmica). Toda entrega ocorre na DM.

---

### Etapa 8: Auditoria Anti-Slop Obrigatória & Salvamento de Output
1. **Passagem pelo `/geral-anti-slop`:**
   - Submeter o roteiro/copy às regras de `.agent/workflows/geral-anti-slop.md`.
   - Eliminar termos proibidos ("portanto", "crucial", "revolucionário", "no cenário atual", "além disso", "desvendar", "mergulhar").
   - Garantir cadência natural de fala brasileira.
2. **Salvamento Padronizado:**
   - Criar diretório: `content/<marca>/<tipo-de-conteudo>/YYYY-MM-DD - Nome da Demanda/`
   - Salvar os arquivos:
     - `roteiro.md` ou `copy-opcao-1.md`
     - `briefing-visual.md`
     - `blueprint-reverso.md` (se originado de concorrente)

---

## 🚀 Como Iniciar uma Demanda no `conteudo-linha-de-producao`

O assistente pode ser acionado diretamente com:
> *"Execute a esteira conteudo-linha-de-producao para a marca [MARCA] no canal [Reels/Shorts/Carrossel] com objetivo de [SAVE/SHARE/FOLLOW/LEAD] a partir do concorrente [URL/CSV/Tópico]."*

Ou selecionando o agente `content-creator` e aplicando o fluxo acima passo a passo.

## Outras referências

- **[content-calendar-template.md](references/content-calendar-template.md)** — Modelo de calendário de conteúdo por campanha ou mês.
- **[product-update-example.md](references/product-update-example.md)** — Exemplo de conteúdo de atualização de produto.
