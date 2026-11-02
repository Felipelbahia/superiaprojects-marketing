# Guia de Contribuição — Super IA Projects - Marketing

Obrigado pelo seu interesse em contribuir com o **Super IA Projects - Marketing** (`superiaprojects-marketing`), o hub de inteligência autônoma para Marketing, Growth, Copywriting, SEO e Ads mantido pela [Futuro Mercado](https://www.futuromercado.com.br).

---

## 🛠️ Metodologia de Design de Skills de Marketing

Seguimos a metodologia **TDD para Conteúdo e Procedimentos**:

1. **Atômica e Especializada:** Cada skill resolve uma vertical ou canal específico (ex: `ads-meta`, `copy-vsl`, `seo-on-page`). Não crie "mega-skills" genéricas.
2. **Gatilhos Explícitos (YAML Frontmatter):**
   ```yaml
   ---
   name: copy-nova-estrategia
   description: Use when [gatilhos com palavras-chave claras e termos de busca].
   ---
   ```
3. **Filtro Anti-Slop Nativo:** Todo procedimento de geração de texto deve conter salvaguardas explícitas contra linguagem clichê de IA.
4. **Sem Caminhos Absolutos ou Dados Privados:** Nunca inclua `/Users/...` ou nomes de marcas/clientes reais nas skills ou referências. Use referências relativas e placeholders padronizados.

---

## 🚀 Como Criar uma Nova Skill ou Agente

### 1. Criar a pasta da Skill
```bash
mkdir -p .agent/skills/minha-skill/references
```

### 2. Criar o arquivo `SKILL.md`
Escreva a documentação procedural contendo instruções diretas para o agente, ferramentas recomendadas e critérios de avaliação de qualidade.

### 3. Sincronizar Entrypoints Multi-IA
Após adicionar qualquer skill, persona de agente ou comando de workflow:
```bash
python3 .agent/scripts/sync_entrypoints.py
```
Isso criará automaticamente os symlinks necessários para o **Claude Code** (`.claude/skills/`) e para o **Cursor** (`.cursor/commands/`).

---

## 📋 Como Submeter Pull Requests

1. Crie uma branch para a sua feature: `git checkout -b feature/minha-skill-de-mkt`
2. Valide os links e frontmatter: `python3 .agent/scripts/sync_entrypoints.py --check`
3. Envie o PR descrevendo o canal atendido, referências bibliográficas e exemplos práticos de uso.

---

**Futuro Mercado** — [www.futuromercado.com.br](https://www.futuromercado.com.br) | [@felipelbahia](https://instagram.com/felipelbahia)
