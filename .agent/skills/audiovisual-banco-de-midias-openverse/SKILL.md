---
# Source: https://api.openverse.org/v1/ | https://github.com/WordPress/openverse
# Repository: https://github.com/Felipelbahia/superiaprojects-marketing
# Status: Nativa do Projeto
name: audiovisual-banco-de-midias-openverse
description: "Use para buscar fotos, ilustrações, vetores, áudios e vídeos livres (domínio público e Creative Commons CC0 e CC-BY) na API do Openverse, com fallback no Wikimedia Commons e atribuição legal pronta. Gatilhos: \"imagem livre\", \"Creative Commons\", \"banco de imagens gratuito\", \"Openverse\". NÃO use para fotos de estoque do Pexels (use o workflow audiovisual-banco-de-imagens-pexels) nem para gerar imagem com IA (use audiovisual-imagem-flux-prompts)."
author: Felipe Bahia (0 Mkt)
license: MIT
metadata:
  author: Felipe Bahia (0 Mkt)
  version: 1.1.0
  vertical: Audiovisual & Conteúdo
complements: audiovisual-podcast-e-audio, audiovisual-imagem-flux-api, conteudo-pesquisa, ads-criativos, social-carrossel
---

# Banco de Mídias Openverse (Skill & Helper CLI)

A skill **`audiovisual-banco-de-midias-openverse`** permite localizar e extrair imagens em alta resolução, vetores, ilustrações, efeitos sonoros, músicas e vídeos do ecossistema do **Openverse** ([WordPress/openverse](https://github.com/WordPress/openverse)) e seu maior provedor público, a **Wikimedia Commons**, indexando coletivamente centenas de milhões de ativos sob licenças **Creative Commons** e **Domínio Público**.

Conta com um script helper nativo em Python (`search_openverse.py`) com **zero dependências externas** (apenas biblioteca padrão do Python), suporte a proporções visuais (wide, square, tall), conformidade para uso comercial, fallback automático para alta disponibilidade e o texto exato de atribuição legal formatado para copy-paste.

---

## 🎯 Quando Usar

- **Anúncios Pagos & Mídia de Performance (`ads-criativos` / `ads-trafego-pago`)**:
  - Encontrar fotos autênticas, sem cara de banco de imagem artificial ou "IA slop".
  - Garantir licenças 100% liberadas para fins comerciais (`--commercial`).
- **Criativos para Redes Sociais (`social-carrossel` / `social-calendario-e-distribuicao`)**:
  - Formato vertical 9:16 para Reels e Stories (`--aspect-ratio tall`).
  - Formato quadrado 1:1 para Feed do Instagram/LinkedIn (`--aspect-ratio square`).
- **Landing Pages & Banners de Blog (`site-interface-de-conversao` / `conteudo-post-de-blog`)**:
  - Hero banners horizontais 16:9 (`--aspect-ratio wide`).
  - Ilustrações e ícones vetoriais SVG (`--extension svg` ou `--category illustration`).
- **Produção Audiovisual & Podcasts (`audiovisual-producao-de-video` / `audiovisual-podcast-e-audio`)**:
  - Efeitos sonoros e trilhas de fundo para vídeos e podcasts (`--type audio`).
- **Atribuição Legal Rigorosa (Compliance & LGPD)**:
  - Obter instantaneamente o texto oficial de crédito Creative Commons pronto para colar no rodapé de artigos ou descrições de vídeos.

---

## 🚫 Quando NÃO Usar

- **Geração Sintética de Imagens**: Se você precisa gerar imagens do zero via inteligência artificial com prompts fotorrealistas, utilize a skill `audiovisual-imagem-flux-api` ou `audiovisual-imagem-flux-prompts`.
- **Geração de Voz / TTS**: Se você precisa de dublagem ou clonagem de voz, utilize a skill `audiovisual-agentes-de-voz` (ElevenLabs).
- **Vídeos Longos e Renderização**: Para montagem de vídeos programáticos, utilize o projeto de edição de vídeo com Remotion.

---

## ⚡ Guia Rápido de Comandos CLI

O helper reside em `.agent/skills/audiovisual-banco-de-midias-openverse/scripts/search_openverse.py`. Execute a partir da raiz do workspace:

### 1. Imagem para Anúncios (Comercial + Horizontal 16:9)
```bash
python3 .agent/skills/audiovisual-banco-de-midias-openverse/scripts/search_openverse.py --query "coffee shop laptop" --commercial --aspect-ratio wide -n 3
```

### 2. Imagem Vertical para Reels / Stories (9:16)
```bash
python3 .agent/skills/audiovisual-banco-de-midias-openverse/scripts/search_openverse.py --query "urban architecture" --commercial --aspect-ratio tall -n 3
```

### 3. Imagem Quadrada para Feed do Instagram (1:1)
```bash
python3 .agent/skills/audiovisual-banco-de-midias-openverse/scripts/search_openverse.py --query "minimalist desk setup" --aspect-ratio square -n 3
```

### 4. Vetores e Ilustrações SVG (Para Logos, LP e Ícones)
```bash
python3 .agent/skills/audiovisual-banco-de-midias-openverse/scripts/search_openverse.py --query "technology cloud" --category illustration -n 3
```

### 5. Domínio Público Absoluto (CC0 / PDM - Zero Atribuição Necessária)
```bash
python3 .agent/skills/audiovisual-banco-de-midias-openverse/scripts/search_openverse.py --query "vintage botanical" --license cc0 -n 3
```

### 6. Vídeos Livres e Motion Graphics (CC0 / Creative Commons)
```bash
python3 .agent/skills/audiovisual-banco-de-midias-openverse/scripts/search_openverse.py --query "nature drone" --type video -n 2
```

### 7. Efeitos Sonoros ou Trilhas Musicais
```bash
python3 .agent/skills/audiovisual-banco-de-midias-openverse/scripts/search_openverse.py --query "ambient piano" --type audio -n 2
```

### 8. Exportar em JSON (Para Pipelines & Automações)
```bash
python3 .agent/skills/audiovisual-banco-de-midias-openverse/scripts/search_openverse.py --query "startup team" --commercial --format json
```

### 9. Download Automático dos Arquivos Originais em Alta Resolução
```bash
python3 .agent/skills/audiovisual-banco-de-midias-openverse/scripts/search_openverse.py --query "nature sunset" --commercial -n 3 --download-dir "content/downloads/sunset"
```

---

## 📋 Parâmetros e Filtros Disponíveis

| Parâmetro | Valores / Exemplos | Descrição & Caso de Uso |
| :--- | :--- | :--- |
| `--query`, `-q` | `"minimalist workspace"` | **(Obrigatório)** Palavra-chave da busca (recomenda-se inglês para maior volume). |
| `--type` | `image` (padrão), `audio` | Escolhe entre catálogo de imagens ou faixas de áudio. |
| `--commercial` | Flag booleana | Garante apenas mídias liberadas para fins comerciais (elimina licenças Não-Comerciais `NC`). |
| `--modify` | Flag booleana | Garante licenças que permitem modificações/recortes (elimina licenças `ND`). |
| `--license` | `cc0`, `pdm`, `by`, `by-sa`, `by-nc` | Filtra por código estrito de licença Creative Commons. |
| `--aspect-ratio` | `tall`, `wide`, `square` | `tall` (Stories/Reels 9:16), `wide` (Banners/YT 16:9), `square` (Feed 1:1). |
| `--category` | Imagem: `photograph`, `illustration`, `digitized_art`<br>Áudio: `music`, `sound_effect`, `podcast` | Segmenta o estilo visual ou o gênero de áudio desejado. |
| `--extension` | `jpg`, `png`, `svg` (imagem) / `mp3`, `wav`, `ogg` (áudio) | Formato do arquivo (ex: `svg` para ícones vetoriais). |
| `--size` | `small`, `medium`, `large` | Filtra pelo tamanho/resolução da imagem. |
| `--source`, `--provider` | `wikimedia`, `flickr`, `smithsonian`, `rawpixel`, etc. | Filtra acervos de museus e provedores específicos. |
| `--page-size`, `-n` | Inteiro (1 a 50, padrão: 5) | Número de mídias retornadas na consulta. |
| `--format` | `markdown` (padrão), `json`, `summary` | Formato da resposta no terminal/chat. |
| `--download-dir` | Caminho de pasta (ex: `content/...`) | Faz o download dos arquivos em alta resolução para a pasta indicada. |

---

## ⚖️ Conformidade Legal & Licenças Creative Commons

O marketing digital exige rigor na utilização de ativos visuais de terceiros. Veja como interpretar as licenças retornadas:

```mermaid
graph TD
    A[Mídia no Openverse] --> B{Possui 'NC'?}
    B -- Sim --> C[USO APENAS EDITORIAL / NÃO-COMERCIAL]
    C --> C1[Proibido em anúncios pagos, páginas de vendas ou produtos]
    B -- Não --> D{Possui 'CC0' ou 'PDM'?}
    D -- Sim --> E[DOMÍNIO PÚBLICO TOTAL]
    E --> E1[Uso comercial livre, sem exigência legal de crédito]
    D -- Não --> F[USO COMERCIAL COM ATRIBUIÇÃO]
    F --> F1[Copie a atribuição pronta gerada pelo script e inclua nos créditos]
```

### Resumo das Licenças Principais:
1. **CC0 / PDM (Public Domain)**: Liberdade total. Pode usar em vendas, anúncios e embalagens sem necessidade de citar o autor.
2. **CC BY**: Pode usar comercialmente e alterar, desde que cite a autoria com a linha de atribuição oficial.
3. **CC BY-SA**: Pode usar comercialmente, mas obras derivadas devem ser distribuídas sob a mesma licença.
4. **CC BY-NC / CC BY-NC-ND**: **PROIBIDO** para marketing comercial, vendas ou tráfego pago. O script helper bloqueia automaticamente quando você passa a flag `--commercial`.

---

## 🤖 Integração com Agentes de Marketing

Quando um agente do repositório precisar de fotos ou referências visuais para um conteúdo:

1. **`brand-direcao-de-arte`**:
   - Utilize para encontrar referências de iluminação, composições fotográficas autênticas e acervos históricos de museus (Smithsonian, Met, Cleveland Museum).
2. **`ads-trafego-pago`**:
   - Execute sempre com `--commercial` para alimentar criativos de Google Ads e Meta Ads com segurança jurídica.
3. **`social-calendario-e-distribuicao`**:
   - Combine `--aspect-ratio tall` para Stories/Reels e `--aspect-ratio square` para carrosséis de feed.
4. **`conteudo-criacao-multiformato`**:
   - Incorpore o markdown gerado diretamente no arquivo de post, no destino da regra de resolução da skill `geral-arquitetura-de-projeto` (`content/<marca>/<canal>/YYYY-MM-DD - Demanda/` no 0 Mkt; `conteudos/<canal>/YYYY-MM-DD - Demanda/` em projeto próprio), incluindo a imagem e os créditos no rodapé.

---

## 🔧 Arquitetura do Helper (`scripts/search_openverse.py`)

- **Resiliência e Fallback Local**: A API pública do Openverse pode sofrer com latências no backend Elasticsearch ao calcular agregações em 800M+ registros. O script helper implementa timeout inteligente de 8 segundos com **fallback transparente** para filtragem em memória cliente e acionamento da API da Wikimedia Commons (maior provedor do Openverse), garantindo que o agente nunca fique bloqueado.
- **Zero Instalações**: Não requer `pip install requests` nem dependências de terceiros; roda nativamente com `urllib.request` e `json` do Python 3.

---

## 🔗 Referências Oficiais do Projeto & GitHub

- **Repositório Principal no GitHub:** [WordPress/openverse](https://github.com/WordPress/openverse)
- **Django REST API (Backend):** [WordPress/openverse/api](https://github.com/WordPress/openverse/tree/main/api)
- **Frontend de Busca (Nuxt/Vue):** [WordPress/openverse/frontend](https://github.com/WordPress/openverse/tree/main/frontend)
- **Pipelines de Ingestão de Catálogo (Apache Airflow):** [WordPress/openverse/catalog](https://github.com/WordPress/openverse/tree/main/catalog)
- **Documentação Técnica Oficial:** [docs.openverse.org](https://docs.openverse.org)
- **Swagger / OpenAPI Reference:** [api.openverse.org/v1](https://api.openverse.org/v1/)
- **Site Público de Busca:** [openverse.org](https://openverse.org)

