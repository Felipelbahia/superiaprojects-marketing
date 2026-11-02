---
name: hook-mining
description: "Use when: minerar ganchos (hooks) de alta performance a partir de dados reais de concorrentes ou da própria marca; classificar ganchos em 11 padrões psicológicos por regex em português; coletar títulos e métricas gratuitamente via yt-dlp e Firecrawl; realizar o remix sintático de ganchos vencedores para marcas de _brands/ sem ferramentas pagas."
metadata:
  source: "Hub 0 Mkt - Inteligência de Conteúdo e Engenharia Reversa"
  version: 1.0.0
---

# Hook Mining — Mineração de Ganchos e Engenharia Reversa Baseada em Dados

> **Princípio Central:** Nunca adivinhe o que chama atenção. Minere o que já foi validado pelo algoritmo e pelo comportamento real das pessoas, isole o padrão psicológico subjacente e faça o remix das variáveis de produto/nicho para a sua marca. Zero dependência de ferramentas pagas.

---

## 🛠️ 1. O Script Local `mine_hooks.py`

A skill é alimentada pelo script Python local localizado em `.agent/skills/hook-mining/scripts/mine_hooks.py`.

### Capacidades do Script:
- **Detecção de Colunas Heterogêneas:** Identifica automaticamente variações de cabeçalhos de ganchos (`hook`, `titulo`, `title`, `caption`, `texto`, `legenda`, `headline`, `post`) e de métricas (`views`, `visualizacoes`, `visualizações`, `metric`, `score`, `engajamento`, `likes`, `alcance`).
- **Parse Numérico Flexível:** Converte valores formatados como `100k`, `1.5M`, `50 mil`, `R$ 50.000` em números reais para ordenação.
- **Classificação em 11 Padrões Psicológicos:** Aplica expressões regulares calibradas especificamente para o português brasileiro.
- **Detecção de Power Words:** Identifica palavras de alta carga emocional e seus plurais.
- **Exportação JSON e Resumo Visual:** Salva os dados enriquecidos em `hooks.mined.json` e imprime um resumo estatístico das forças no terminal.

### Modos de Uso:

```bash
# 1. Executar selftest (validação da lógica de parsing e regex)
python3 .agent/skills/hook-mining/scripts/mine_hooks.py --selftest

# 2. Minerar um CSV completo
python3 .agent/skills/hook-mining/scripts/mine_hooks.py caminho/do/arquivo.csv

# 3. Minerar apenas o Top N de melhor performance
python3 .agent/skills/hook-mining/scripts/mine_hooks.py caminho/do/arquivo.csv --top 30
```

---

## 🆓 2. Táticas de Coleta Gratuitas (Zero Ferramentas Pagas)

Esqueça assinaturas caras de scrapers ou ferramentas como Apify, Sandcastles ou BuzzSumo. O `0 Mkt` utiliza três fontes gratuitas e locais:

### Tática A: YouTube Shorts via `yt-dlp` Local
O `yt-dlp` já está instalado e disponível localmente no ecossistema (a skill `video-download` foi removida do 0 Mkt e vive no projeto de edição de vídeo (`Compartilhado/Edição de Vídeo com IA`)). Ele extrai títulos e contagem de visualizações de qualquer canal público em segundos, sem necessidade de login ou chave de API.

**Comando de Coleta Direta para CSV:**
```bash
yt-dlp --flat-playlist --print "%(title)s,%(view_count)s" "https://www.youtube.com/@CanalConcorrente/shorts" > concorrente_shorts.csv
```

**Preparação do CSV (Inserir Cabeçalho):**
Adicione a primeira linha no CSV para facilitar a leitura automática:
```csv
titulo,visualizacoes
```
Em seguida, execute o minerador:
```bash
python3 .agent/skills/hook-mining/scripts/mine_hooks.py concorrente_shorts.csv --top 25
```

### Tática B: Pesquisa de Dores e Dúvidas no Reddit via Firecrawl MCP
Para minerar ganchos baseados em dúvidas cruéis e dores viscerais do público, utilize as ferramentas de busca do Firecrawl MCP direcionadas a comunidades abertas (Reddit, fóruns, Quora):

**Exemplo de Consulta no Firecrawl:**
- Consultar tópicos mais votados em subreddits relacionados (ex: `site:reddit.com/r/brasil "segurança"`, `site:reddit.com/r/empreendedorismo "whatsapp"`).
- Extrair as perguntas que acumulam mais comentários.
- Transformar as perguntas literais das pessoas em ganchos no padrão `question` ou `secret-gap`.

### Tática C: Ingestão de Relatórios Nativos (Meta Business Suite / YouTube Studio)
Ao auditar ou minerar ganchos das marcas proprietárias em `_brands/`:
1. Acesse o **Meta Business Suite** (para Reels/Instagram) ou o **YouTube Studio** (para Shorts).
2. Exporte a planilha de postagens dos últimos 90 dias em formato `.csv`.
3. Passe a planilha diretamente no `mine_hooks.py`:
   ```bash
   python3 .agent/skills/hook-mining/scripts/mine_hooks.py relatorio_meta.csv --top 20
   ```

---

## 🧠 3. Os 11 Padrões Psicológicos Universais de Ganchos

O script classifica os ganchos nos seguintes 11 pilares comportamentais:

| Padrão | Mecanismo Psicológico | Gatilho / Emoção | Sintaxe Base em Português | Exemplo Real |
| :--- | :--- | :--- | :--- | :--- |
| **`result-proof`** | Prova irrefutável e ancoragem numérica | Ganância / Inveja / Certeza | `[Eu fiz / Como faturei] [Número/Resultado] [em X tempo]` | *"Eu bati 100k views em 7 dias usando essa automação"* |
| **`time-bound`** | Urgência e promessa de velocidade | Preguiça / Alívio | `[Ação/Resultado] em [X segundos/minutos/dias]` | *"Como auditar um contrato de PR em 45 segundos"* |
| **`contrarian`** | Quebra de padrão e destruição de mitos | Curiosidade / Desafio | `Você está usando [Ferramenta/Hábito] totalmente errado` | *"Pare de mandar áudio no WhatsApp do seu suporte"* |
| **`secret-gap`** | Assimetria de informação / Informação restrita | Medo de exclusão / Soberba | `O que ninguém te conta sobre [Tópico/Mercado]` | *"A técnica de vigilância corporativa que quase ninguém conhece"* |
| **`listicle`** | Previsibilidade e facilidade de consumo | Preguiça / Organização | `[Número] [Substantivo] para [Objetivo]` | *"3 erros fatais que destroem a segurança da sua empresa"* |
| **`how-to`** | Tutorial pragmático e direcionamento claro | Esperança / Capacitação | `Como [Ação desejada] [sem complicação]` | *"Como faturar R$ 50 mil com contratos de assessoria"* |
| **`warning-fear`** | Aversão à perda e alerta de risco | Medo / Alívio imediato | `Cuidado: [Ação] está destruindo seu [Ativo]` | *"Alerta: nunca abra esse tipo de link no WhatsApp"* |
| **`newsjack`** | Novidade quente e relevância temporal | Curiosidade / FOMO | `Acabou de sair o novo [Recurso/Atualização]` | *"Acabou de lançar a nova IA de transcrição do WhatsApp"* |
| **`comparison`** | Confronto de alternativas (A vs B) | Discernimento / Certeza | `[Opção A] vs [Opção B]: qual o melhor para [Caso]?` | *"WhatsApp Web vs API Oficial: qual a diferença real?"* |
| **`question`** | Dissonância cognitiva e autorreflexão | Dúvida / Identificação | `Por que [Situação bizarra/comum] acontece?` | *"Por que seu cliente não responde mais suas mensagens?"* |
| **`curiosity-tease`**| Tensão narrativa e loop aberto | Curiosidade pura / Tensão | `Olha isso até o final se você [Condição]` | *"Olha o que aconteceu quando ativei essa função secreta"* |

---

## ⚡ 4. Dicionário de Power Words

Palavras que funcionam como aceleradores de atenção quando inseridas no gancho:
`grátis`, `gratuito`, `segredo`, `escondido`, `comprovado`, `imediato`, `instantâneo`, `realmente`, `literalmente`, `ninguém`, `todos`, `loucura`, `absurdo`, `ilegal`, `hack`, `definitivo`, `brutal`, `exato`, `pare`, `nunca`, `sempre`, `pior`, `melhor`, `quebrado`, `morto`, `destruindo`, `gênio`, `estúpido`, `bizarro`, `injusto`, `estranho`, `proibido`, `chocante`, `verdade`, `mentira`, `erro`, `mais rápido`, `mais fácil`, `único`.

---

## 🔄 5. Framework de Remix de Ganchos (Remixing Architecture)

Após minerar e identificar os ganchos de maior tração, isole o esqueleto psicológico e substitua **apenas as variáveis de nicho e produto** pela marca ativa do repositório:

### Passo a Passo de Remix:
1. **Identificar o Padrão Vencedor:** Analisar o hook original (ex: *"Você está usando o Notion totalmente errado para estudar"* -> `contrarian`).
2. **Extrair o Esqueleto Abstrato:** `Você está usando [FERRAMENTA/PROCESSO] totalmente errado para [OBJETIVO]`.
3. **Mapear para a Marca Ativa:**
   - **Plinq (Segurança Feminina):** *"Você está configurando o compartilhamento de rota do seu celular totalmente errado."*
   - **WaiMonitor (WhatsApp Compliance):** *"Você está usando os grupos de WhatsApp da sua empresa totalmente errado."*
   - **PR Pulse (Agências de PR):** *"Você está medindo o clipping da sua agência totalmente errado."*
   - **Felipe Bahia (Creator / AI):** *"Você está usando prompts do Claude Code totalmente errado no terminal."*

---

## 🔗 6. Integração com o Ecossistema do `0 Mkt`

- **Entrada:** CSVs coletados via `yt-dlp`, Firecrawl ou Meta Business Suite.
- **Processamento:** Classificação via `mine_hooks.py`.
- **Validação de Retenção:** Os ganchos remixados devem ser passados pelo checklist visual de 8 pontos de `copy-hooks-video-curto`.
- **Eletrificação:** Conectar os ganchos aos 14 botões emocionais de `revenue-sexy-canvas`.
- **Filtro Anti-Slop:** Passagem mandatória pelo workflow `/geral-anti-slop` antes da finalização.
