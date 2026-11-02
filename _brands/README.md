# 🏷️ Estrutura de Marcas (`_brands/`)

Este diretório armazena a identidade de cada marca utilizada pelos agentes autônomos de marketing.
> **Lembrete de Isolamento:** Aqui vive apenas a **identidade** da marca (estratégia, tom e personas). Todo conteúdo produzido pelos agentes deve ser salvo na pasta de entregas: `content/<marca>/<canal>/` (isolada do Git público via `.gitignore`).

---

## 📁 Estrutura de uma Marca

Cada subpasta de marca deve conter os 4 pilares fundamentais:
1. `brand-voice.md`: Tom de voz, personalidade, arquétipos e tabus editoriais ("O que NÃO comunicar").
2. `personas.md`: Mapeamento das personas-alvo, dores profundas, objetivos e canais preferidos.
3. `content-pillars.md`: 3 a 5 pilares estratégicos que sustentam as linhas editoriais.
4. `style-guide.md`: Identidade visual, paleta de cores (Hex), tipografia e direção de arte.

---

## 🚀 Como Adicionar uma Nova Marca

1. Duplique a pasta template:
   ```bash
   cp -r _brands/brand-template _brands/minha-marca
   ```
2. Edite os 4 arquivos em `_brands/minha-marca/` com as informações do seu negócio.
3. (Opcional) A skill `brand-builder` (`.agent/skills/brand-builder/SKILL.md`) conduz uma entrevista socrática para preencher esses arquivos do zero.
