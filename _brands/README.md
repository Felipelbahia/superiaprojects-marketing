# 🏷️ Estrutura de Marcas (`_brands/`)

Este diretório armazena a identidade de cada marca utilizada pelos agentes autônomos de marketing.
> **Lembrete de Isolamento:** Aqui vive apenas a **identidade** da marca (estratégia, tom e personas). Todo conteúdo produzido pelos agentes deve ser salvo onde o mapa de destinos manda (`docs/mapa-de-destinos.md`), em `content/<marca>/…` (isolada do Git público via `.gitignore`).

---

## 📁 Estrutura Canônica de uma Marca

Cada subpasta de marca deve conter os pilares fundamentais de governança:
1. `brand-voice.md`: Tom de voz, personalidade, arquétipos, afirmações que exigem confirmação humana, restrições por canal e tabus editoriais ("O que NÃO comunicar").
2. `personas.md`: Mapeamento das personas-alvo, dores profundas, objetivos e canais preferidos.
3. `content-pillars.md`: 3 a 5 pilares estratégicos que sustentam as linhas editoriais.
4. `style-guide.md`: Identidade visual, paleta de cores (Hex), tipografia e direção de arte.
5. `glossario.md`: Escrita oficial da marca, termos proibidos, categorização do que não se traduz (marcas, metodologias, siglas) e trava de saída de termos pendentes.
6. `depoimentos.md`: Acervo governado de prova social contendo aspas literais (*ipsis litteris*) e matriz de consentimento explícito por canal de distribuição.

---

## 🛡️ Regras de Integridade e Proteção Estrutural

1. **Proteção de Cabeçalhos (Proibição de Deleção):**  
   Ao editar ou refinar arquivos de marca existentes, é terminantemente proibido apagar cabeçalhos de seção padronizados (`## 1. Posicionamento`, `## 5. Afirmações...`). Se uma seção ainda não possuir conteúdo definido, mantenha o cabeçalho intacto e anote `[a definir]` ou `[aguardando alinhamento]`.
2. **Princípio da Informação Insuficiente (Anti-Alucinação):**  
   Estendendo a regra de integridade de `mensagens.md`, nenhum arquivo de marca pode ter lacunas preenchidas com dados inventados ou suposições probabilísticas da IA. Dados faltantes (preços, métricas, SLAs, depoimentos) devem ser explicitamente registrados na seção `## Lacunas` ou marcados com `[a confirmar]`.
3. **Imutabilidade em Divergências:**  
   A base de marca representa o registro oficial. Discrepâncias surgidas durante a redação de peças isoladas corrigem a peça e nunca a base de marca em silêncio.

---

## 🚀 Como Adicionar uma Nova Marca

1. Duplique a pasta template:
   ```bash
   cp -r _brands/brand-template _brands/minha-marca
   ```
2. Edite os arquivos em `_brands/minha-marca/` com as informações do seu negócio.
3. (Opcional) A skill `brand-builder` (`.agent/skills/brand-builder/SKILL.md`) conduz uma entrevista socrática para preencher esses arquivos do zero.
