---
name: geral-verificacao-de-fatos
description: Verifies factual claims in documents using web search and official sources, applies the 5-level source precedence hierarchy, locks on factual conflicts to prevent silent AI resolution, and proposes corrections with user confirmation. Use when the user asks to fact-check, verify information, validate claims, check accuracy, or resolve conflicting sources in documents.
---

# Fact Checker & Governança de Fatos

Verify factual claims in documents and propose corrections backed by authoritative sources, enforcing strict source precedence and anti-silent resolution locks.

## When to use

Trigger when users request:
- "Fact-check this document"
- "Verify these AI model specifications"
- "Check if this information is still accurate"
- "Update outdated data in this file"
- "Validate the claims in this section"
- "Resolve conflicting information between sources"

## Workflow

Copy this checklist to track progress:

```
Fact-checking Progress:
- [ ] Step 1: Identify factual claims
- [ ] Step 2: Search authoritative sources & verify 5-level precedence
- [ ] Step 3: Compare claims against sources & detect conflicts
- [ ] Step 4: Generate correction report (lock on conflicts)
- [ ] Step 5: Apply corrections with user approval
```

---

## Hierarquia de Precedência em 5 Níveis

Ao checar ou confrontar dados entre múltiplas origens, aplique compulsoriamente a seguinte escala:

1. **Nível 1 (Autoridade Máxima):** Orientação direta e recente do usuário/proprietário;
2. **Nível 2 (Registro Oficial da Marca):** Bases em `_brands/<marca>/` (`brand-voice.md`, `acervo_dados_metricas.md`, `glossario.md`, `depoimentos.md`);
3. **Nível 3 (Diretrizes Operacionais):** Requisitos acordados no briefing, pauta ou sprint da demanda;
4. **Nível 4 (Fontes Externas com Prova):** Estudos, relatórios ou documentações de terceiros com link e data de checagem;
5. **Nível 5 (Hipótese de Trabalho):** Suposições operacionais mantidas sob a tag `[a confirmar]`.

---

## Regra de Ouro: Proibição de Correção Silenciosa (Trava de Processo)

1. **Trava em Conflito Fático:** Se duas fontes de mesmo nível ou níveis equivalentes divergirem em dados materiais (preços, datas, promessas, métricas), a IA está terminantemente proibida de arbitrar, calcular médias ou escolher silenciosamente. O fluxo trava imediatamente para decisão humana.
2. **Correção de Peça vs. Correção de Contexto:** Em peças de conteúdo já geradas ou publicadas, corrige-se o artefato (a peça) e não a base de contexto da marca, a menos que o usuário declare expressamente que a base da marca estava desatualizada.

---

### Step 1: Identify factual claims

Scan the document for verifiable statements:

**Target claim types:**
- Technical specifications (context windows, pricing, features)
- Version numbers and release dates
- Statistical data and metrics
- API capabilities and limitations
- Benchmark scores and performance data

**Skip subjective content:**
- Opinions and recommendations
- Explanatory prose
- Tutorial instructions
- Architectural discussions

### Step 2: Search authoritative sources

For each claim, search official sources obeying the 5-level precedence:

**AI models:**
- Official announcement pages (anthropic.com/news, openai.com/index, blog.google)
- API documentation (platform.claude.com/docs, platform.openai.com/docs)
- Developer guides and release notes

**Technical libraries:**
- Official documentation sites
- GitHub repositories (releases, README)
- Package registries (npm, PyPI, crates.io)

**General claims:**
- Academic papers and research
- Government statistics
- Industry standards bodies

**Search strategy:**
- Use model names + specification (e.g., "Claude Opus 4.5 context window")
- Include current year for recent information
- Verify from multiple sources when possible

### Step 3: Compare claims against sources

Create a comparison table:

| Claim in Document | Source Information | Precedence Level | Status | Authoritative Source |
|---|---|:---:|---|---|
| Claude 3.5 Sonnet: 200K tokens | Claude Sonnet 4.5: 200K tokens | Nível 4 | ❌ Outdated model name | platform.claude.com/docs |
| Plano Pro: R$ 197/mês | Plano Pro: R$ 247/mês | Nível 2 vs 3 | ⚠️ Conflito Fático (Trava) | `_brands/marca/ofertas.md` vs Briefing |

**Status codes:**
- ✅ Accurate - claim matches sources
- ❌ Incorrect - claim contradicts sources
- ⚠️ Outdated - claim was true but superseded
- ❓ Unverifiable - no authoritative source found
- 🛑 Conflito Fático - fontes divergem materialmente; trava de processo obrigatória

### Step 4: Generate correction report

Present findings in structured format:

```markdown
## Fact-Check Report

### Summary
- Total claims checked: X
- Accurate: Y
- Issues found: Z
- Conflitos fáticos (travas): W

### Issues Requiring Correction / Decisions

#### Issue 1: Outdated AI Model Reference
**Location:** Line 77-80 in docs/file.md
**Current claim:** "Claude 3.5 Sonnet: 200K tokens"
**Correction:** "Claude Sonnet 4.5: 200K tokens"
**Source:** https://platform.claude.com/docs/en/build-with-claude/context-windows
**Rationale:** Claude 3.5 Sonnet has been superseded by Claude Sonnet 4.5 (released Sept 2025)

#### Issue 2: Conflito Fático de Preço (Trava Mandatória)
**Location:** Linha 45 da peça
**Fonte A (Nível 2 - Registro Oficial):** R$ 197/mês em `_brands/marca/ofertas.md`
**Fonte B (Nível 3 - Briefing da Campanha):** R$ 247/mês em `briefing.md`
**Ação:** Decisão humana necessária. Nenhuma correção foi aplicada em silêncio.
```

### Step 5: Apply corrections with user approval

**Before making changes:**

1. Show the correction report to the user
2. Wait for explicit approval: "Should I apply these corrections?"
3. Only proceed after confirmation

**After corrections:**

1. Verify all edits were applied successfully
2. Note the correction summary (e.g., "Updated 4 claims in section 2.1")
3. Remind user to commit changes
