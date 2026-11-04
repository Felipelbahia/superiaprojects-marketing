---
name: geral-execucao-autonoma
description: Execução autônoma de metas complexas de marketing com ciclo de 5 fases (Meta -> Plano -> Confirmação -> Execução -> Relatório). Você direciona, o agente executa.
allowed-tools: Read, Write, Edit, Bash
---

# 🎯 Go Mode — Autonomous Goal Execution (Marketing Edition)

> Forneça uma meta de marketing de ponta a ponta. O assistente quebra em etapas, aguarda sua confirmação, executa autonomamente e reporta o resultado final.

---

## 1. Fluxo de Trabalho

```
META → PLANO → CONFIRMAÇÃO → EXECUÇÃO → RELATÓRIO
```

---

## 2. Como Executar

Invoque o comando seguido da sua meta:
```
/go-mode "Criar campanha de reengajamento de e-mails para a base fria da Plinq"
```

---

## 3. As 5 Fases Operacionais

### Fase 1: PLAN (Planejamento Detalhado)
Ao receber a meta, o assistente decompõe o objetivo sem executar imediatamente:
1. **Definição de Pronto (Definition of Done)**: Critérios exatos de conclusão e aceitação.
2. **Plano Sequencial de Ação**: Tabela com passos concretos, ferramentas/skills acionadas e estimativas.
3. **Mapeamento de Riscos & Guardrails**:
   - Disparo de comunicações externas (exige confirmação explícita).
   - Alteração em campanhas ativas de mídia paga.
   - Ações irreversíveis de deleção ou migração.

Apresentar a proposta de plano:
```markdown
## 🎯 Meta: [Restatement claro da meta]

### Definição de Pronto
- [ ] Entregável 1 especificado e validado
- [ ] Entregável 2 salvo no caminho correto em content/ ou .agent/plans/

### Plano de Execução
| # | Etapa | Skill / Ferramenta | Risco / Ponto Crítico |
|---|---|---|---|
| 1 | Mapeamento de contexto e personas | persona-descoberta-interativa | Alinhamento com brand-voice |
| 2 | Redação da sequência de e-mails | email-orquestracao-de-campanhas | Filtro anti-slop mandatório |
| 3 | Revisão e salvamento estruturado | file-creator | content/<marca>/email/ |
```

### Fase 2: CONFIRM (Aprovação Humana)
Aguardar a validação do usuário antes de iniciar qualquer ação:
- **"Go"**: Executa todas as etapas conforme planejado.
- **"Go com ajustes"**: Refina as etapas indicadas e inicia.
- **"Apenas etapas 1 e 2"**: Execução parcial.
- **"Cancelar"**: Interrompe o processo.

> **Regra de Ouro:** NUNCA pule a fase de confirmação em tarefas complexas. O usuário é o piloto; a IA é o copiloto.

### Fase 3: EXECUTE (Execução Autônoma)
1. Anunciar cada etapa iniciada: *"Iniciando Etapa 2/4: Redigindo as 3 opções de copy..."*
2. Executar utilizando as skills e diretrizes de marketing cabíveis.
3. Pausar e solicitar aprovação se encontrar ambiguidade crítica de marca ou persona.
4. Aplicar o workflow mandatório `/ai-slop-detector` em todo texto antes de finalizar.

### Fase 4: QA (Controle de Qualidade)
1. Validar se a entrega atende estritamente a "Definição de Pronto".
2. Confirmar se os arquivos foram salvos na pasta padronizada: `content/<marca>/<tipo>/YYYY-MM-DD - Demanda/`.

### Fase 5: REPORT (Relatório de Conclusão)
Apresentar o relatório de fechamento com links clicáveis para os artefatos gerados.
