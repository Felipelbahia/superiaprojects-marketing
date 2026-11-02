# ⚙️ Guia Completo de Setup — Super IA Projects - Marketing

> **Ecossistema Oficial de Marketing por Felipe Bahia ([Futuro Mercado](https://www.futuromercado.com.br))**  
> Este guia detalha a configuração do ambiente, servidores MCP recomendados e extensões de IDE para operar o hub de marketing autônomo com máxima eficiência.

---

## 🚀 1. Instalação Rápida em 1 Comando

O repositório inclui um script instalador automático que verifica seu ambiente, inicializa as regras e sincroniza os symlinks para todos os agentes:

```bash
git clone https://github.com/Felipelbahia/superiaprojects-marketing.git
cd superiaprojects-marketing
./install.sh
```

O script `./install.sh`:
1. Valida o ambiente **Python 3**.
2. Cria o arquivo de regras `CLAUDE.md` a partir do template agnóstico `CLAUDE.example.md`.
3. Sincroniza e valida os links simbólicos para **Claude Code** (`.claude/`) e **Cursor** (`.cursor/`).
4. Gera o catálogo visual unificado em `catalog.html`.

---

## 🔌 2. Servidores MCP Recomendados para Marketing

O Model Context Protocol (MCP) expande a capacidade dos agentes autônomos com leitura da web, documentação e sincronização em tempo real.

### Os Servidores Selecionados para Marketing

| Servidor MCP | Função Principal | Quando Utilizar |
| :--- | :--- | :--- |
| **`firecrawl`** | Web Scraping & SERP | Inteligência competitiva, análise de concorrentes e mineração de tendências |
| **`notion`** | Gestão de Briefings & Docs | Sincronização de calendários de conteúdo, briefings e entregas no Notion |
| **`context7`** | Documentação Técnica Oficial | Consulta de documentações atualizadas de SDKs, APIs e bibliotecas de mídia |
| **`stitch`** | Prototipagem & UI | Geração de telas, design systems e layouts de Landing Pages de alta conversão |
| **`chrome-devtools`** | Auditoria CRO & Performance | Análise de carregamento (LCP/CWV), responsividade e atrito em páginas de vendas |
| **`supabase`** | Banco de Dados & Analytics | Gestão de leads, métricas de funil e dados de campanhas em Postgres |

---

### Como Ativar os MCPs no seu Ambiente

Utilize o arquivo modelo [`mcp.example.json`](mcp.example.json) fornecido na raiz:

#### Para Claude Code (CLI)
Copie o modelo para as configurações globais do Claude Code:
```bash
cp mcp.example.json ~/.claude/mcp.json
```
*(Preencha sua chave de API do Firecrawl e tokens do Notion no arquivo).*

#### Para Cursor IDE
Copie para as configurações do Cursor ou configure em **Settings > Features > MCP**:
```bash
cp mcp.example.json ~/.cursor/mcp.json
```

#### Para VS Code / Google Antigravity
Copie para a pasta de configurações do seu workspace:
```bash
cp mcp.example.json .vscode/mcp.json
```

---

## 🧩 3. Extensões Recomendadas (VS Code / Antigravity / Cursor)

O arquivo [`.vscode/extensions.json`](.vscode/extensions.json) contém as extensões ideais para produtividade em desenvolvimento e documentação.

### Instalação em Lote via Linha de Comando:

```bash
code --install-extension anthropic.claude-code \
     --install-extension kilocode.kilo-code \
     --install-extension johnpapa.vscode-peacock \
     --install-extension pkief.material-icon-theme \
     --install-extension mechatroner.rainbow-csv \
     --install-extension cweijan.vscode-office \
     --install-extension tomoki1207.pdf \
     --install-extension jasdeepkhalsa.html-md-converter-vscode \
     --install-extension rangav.vscode-thunder-client \
     --install-extension pranaygp.vscode-css-peek \
     --install-extension svelte.svelte-vscode \
     --install-extension ms-python.python \
     --install-extension ms-python.vscode-pylance \
     --install-extension ms-azuretools.vscode-docker
```

---

## 🏷️ 4. Configurando sua Primeira Marca

1. Duplique a pasta de template:
   ```bash
   cp -r _brands/brand-template _brands/minha-marca
   ```
2. Preencha os 4 arquivos em `_brands/minha-marca/`:
   - `brand-voice.md`: Personalidade, tom e termos proibidos (anti-slop).
   - `personas.md`: Dores, objetivos e objeções do seu cliente ideal.
   - `content-pillars.md`: Os 3 a 5 pilares estratégicos de conteúdo.
   - `style-guide.md`: Paleta de cores (Hex), tipografia e direção de arte.
3. Pronto! Seus agentes autônomos agora carregarão automaticamente as diretrizes ao gerar qualquer campanha ou conteúdo.

---

## 🌐 5. Conexão com o Ecossistema Super IA Projects

O **Super IA Projects - Marketing** atua em perfeita simbiose com o repositório central de engenharia [**Super IA Projects (`superiaprojects`)**](https://github.com/Felipelbahia/superiaprojects).

### Setup Recomendado dos Dois Repositórios
Recomendamos clonar ambos os projetos lado a lado no seu ambiente de desenvolvimento:

```bash
# 1. Clone o núcleo de Engenharia e Padrões (220+ skills, scaffolding, QA loop)
git clone https://github.com/Felipelbahia/superiaprojects.git ~/superiaprojects

# 2. Clone a extensão oficial de Marketing e Tração (98 skills, anti-slop, growth)
git clone https://github.com/Felipelbahia/superiaprojects-marketing.git ~/superiaprojects-marketing
```

### Configuração de Resolução Multi-IA
No seu terminal (`~/.zshrc` ou `~/.bashrc`), defina as variáveis de ambiente globais:

```bash
export SUPER_IA_PROJECTS_PATH="$HOME/superiaprojects"
export MARKETING_HUB_PATH="$HOME/superiaprojects-marketing"
```

E no arquivo de regras do seu projeto ativo (`CLAUDE.md` ou `GEMINI.md`), inclua a diretriz de busca hierárquica:

```markdown
### Protocolo de Fallback
1. 1ª Prioridade: `./.agent/skills/` (projeto local)
2. 2ª Prioridade (Engenharia): `~/superiaprojects/.agent/skills/`
3. 3ª Prioridade (Marketing & Growth): `~/superiaprojects-marketing/.agent/skills/`
```

Com essa estrutura, qualquer agente de IA que você abrir em qualquer repositório da sua máquina terá acesso instantâneo a todo o conhecimento técnico e comercial do ecossistema.

---

**Futuro Mercado** — [www.futuromercado.com.br](https://www.futuromercado.com.br) | Contato: [felipe@futuromercado.com.br](mailto:felipe@futuromercado.com.br)
