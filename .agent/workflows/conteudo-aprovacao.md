---
name: conteudo-aprovacao
description: Gera o fluxo de aprovação de uma peça de conteúdo (etapas, responsáveis, SLA, parecer em 5 campos e releitura integral na v2). Use quando uma peça precisar passar por revisão antes de publicar.
allowed-tools: Read, Write, Edit, Bash
---

# Aprovação e Validação de Conteúdo

> Workflow estruturado para governança editorial, auditoria de conformidade, parecer de reprovação em 5 campos e releitura integral de peças de conteúdo no padrão do Hub Super IA Projects - Marketing `0 Mkt`.

---

## 1. O que este workflow faz

Orquestra o fluxo de aprovação e validação técnica de uma peça de conteúdo (post social, artigo de blog, e-mail, carrossel, landing page, roteiro de vídeo etc.), assegurando:
1. **Separação Produtora × Revisora:** Quem produz não decide estratégia; quem valida não corrige a peça. O revisor emite parecer objetivo e devolve para a especialista produtora original executar a edição.
2. **Auditoria com Hard Gate e Parecer em 5 Campos:** Em caso de reprovação ou ajustes, gera relatório estruturado com localização, trecho, regra violada, correção verificável e destinatário da devolução.
3. **Ciclo v1 → Reprovar → v2 com Releitura Integral:** Garante que peças corrigidas (v2) passem por conferência de ponta a ponta (passe literal e passe de sentido), impedindo que correções parciais introduzam novas inconsistências.
4. **Governança de Aprendizado:** Registra correções e preferências do usuário em `_brands/<marca>/aprendizado.md` com escopo delimitado (peça, canal, persona, projeto) e máquina de estados.
5. **Localização e Resolução:** Verifica a pasta da peça via `docs/mapa-de-destinos.md` (`content/<marca>/<tipo>/` no 0 Mkt) e versiona sem sobrescrita (`peça-v1.md`, `peça-v2.md`).

---

## 2. Como executar

```bash
/conteudo-aprovacao
```
Ou com parâmetros contextuais:
```bash
/conteudo-aprovacao --marca <nome-da-marca> --tipo <blog|social|email|landing-page|video>
```

Se a solicitação não especificar a marca, **pare imediatamente e pergunte qual marca deve ser utilizada** (regra 1.1 do `CLAUDE.md`).

---

## 3. Instruções de Execução Passo a Passo

### Fase 1: Rascunho e Autoria (Especialista Produtora)
- [ ] Briefing compreendido, persona definida e objetivo/CTA alinhados;
- [ ] Conteúdo estruturado conforme os padrões nativos do canal;
- [ ] Fatos e dados ancorados com fontes verificadas (sem invenção de números);
- [ ] Passagem obrigatória pelo filtro [geral-anti-slop](.agent/skills/geral-anti-slop/SKILL.md) antes da submissão;
- [ ] Arquivo salvo como versão inicial imutável (ex.: `conteudo-v1.md`).

### Fase 2: Auditoria e Parecer Formal (Agente Revisor)
O revisor designado (ex.: `brand-guardiao-de-voz` para tom e regras de marca, `seo-otimizacao-de-busca` para SEO) audita a peça sem reescrevê-la e emite o parecer com veredito:

```markdown
# Parecer de Revisão: [Nome da Peça]
- **Marca:** [Marca]
- **Canal & Formato:** [Canal]
- **Versão Auditada:** [v1, v2, ...]
- **Revisor:** [Agente revisor]
- **Veredito Geral:** [APROVADO | AJUSTES NECESSÁRIOS | REPROVADO]
- **Destinatário da Devolução:** [Especialista produtora responsável]
```

#### Tabela Oficial de Reprovação (5 Campos)
Quando houver não-conformidade, preencher obrigatoriamente:

| Localização | Trecho Auditado | Regra / Padrão Violado | Correção Verificável | Destinatário da Devolução |
|---|---|---|---|---|
| `§ X, linha Y` | *"trecho literal com problema"* | Documento e item da regra violada | Ação objetiva e mensurável a executar | Especialista produtora (ou brief) |

### Fase 3: Ajustes e Ciclo v2 com Releitura Integral
1. **Execução do Ajuste:** A especialista produtora recebe o parecer e gera a nova versão (ex.: `conteudo-v2.md`).
2. **Protocolo de Dois Passes na v2:**
   - **Passe 1 (Literal):** O revisor confere se o apontamento pontual da v1 foi corrigido conforme a regra (`[RESOLVIDO]`);
   - **Passe 2 (Sentido e Integridade):** O revisor relê a peça inteira do começo ao fim para garantir que a edição local não quebrou a coesão, não alterou a tese central e não introduziu novos desvios.

### Fase 4: Aprovação Final, Governança e Publicação
- [ ] Veredito formal `APROVADO` emitido pelo revisor com indicação estrita da versão exata aprovada (ex.: `versao_aprovada: v1`);
- [ ] **Regra de Invalidação por Edição:** Qualquer alteração textual posterior à aprovação invalida imediatamente o parecer favorável. O arquivo aprovado permanece inalterado e as modificações devem ser salvas em novo arquivo (`conteudo-v2.md`) com `estado: em revisao`, conforme [contrato-de-artefatos-e-estados.md](.agent/skills/conteudo-linha-de-producao/references/contrato-de-artefatos-e-estados.md);
- [ ] Feedbacks e preferências do usuário durante o ciclo registrados em `_brands/<marca>/aprendizado.md` com ID, alcance (`peça`, `canal`, `persona`, `projeto`) e estado (`proposta`, `confirmada`);
- [ ] Regras confirmadas de alcance global promovidas para `brand-voice.md`;
- [ ] Peça liberada para transição para `agendado` ou publicação imediata (`no ar`).

---

## 4. Matriz de SLA e Responsabilidades por Tipo de Conteúdo

| Tipo de Conteúdo | Especialista Produtora | Revisor Técnico / Voz | Aprovação Final | SLA Padrão |
|---|---|---|---|:---:|
| **Artigo de Blog** | `conteudo-post-de-blog` / `conteudo-criacao-multiformato` | `brand-guardiao-de-voz` + `seo-otimizacao-de-busca` | Responsável de Marketing | 3 dias |
| **Post Social / Carrossel** | `social-carrossel` / `social-calendario-e-distribuicao` | `brand-guardiao-de-voz` | Responsável de Social | Mesmo dia |
| **E-mail / Newsletter** | `email-copy` / `email-newsletter` | `brand-guardiao-de-voz` (+ Jurídico se houver claim) | Responsável de CRM/E-mail | 2 dias |
| **Landing Page** | `copy-conversao` / `copy-landing-page` | `brand-guardiao-de-voz` + `seo-otimizacao-de-busca` | Head de Growth / Dono | 5 dias |
| **Roteiro de Vídeo / VSL**| `audiovisual-producao-de-video` / `copy-vsl` | `brand-guardiao-de-voz` | Diretor Audiovisual | 2 dias |

---

## 5. Diretrizes Complementares

- **Referência Canônica:** Consulte [ciclo-de-validacao-de-pecas.md](.agent/skills/brand-voice-messaging/references/ciclo-de-validacao-de-pecas.md) para o guia detalhado dos critérios de Hard Gate, passe duplo de leitura e governança de aprendizado.
- **Moldes de Imagem:** Para peças visuais, audite medidas e margens de segurança conforme `brand-builder/references/identidade-e-ativos/05a-moldes-de-canais.md`.
- **Onde Salvar:** O parecer e o checklist de aprovação acompanham a pasta da demanda na esteira (`content/<marca>/<tipo>/AAAA-MM-DD - Nome da Demanda/`), salvos como `parecer-revisao-v1.md` ou `aprovacao.md`.
