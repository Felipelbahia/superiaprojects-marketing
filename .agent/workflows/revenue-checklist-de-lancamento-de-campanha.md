---
name: revenue-checklist-de-lancamento-de-campanha
description: Gera o checklist de pré-lançamento de uma campanha, com cronograma T-14 a T+1 e matriz de sign-off. Use antes de colocar uma campanha no ar para garantir que nada ficou de fora.
allowed-tools: Read, Write, Edit, Bash
---

# Checklist de Lançamento de Campanha

> Workflow estruturado para o checklist de pré-lançamento de campanha, no padrão do Hub Super IA Projects - Marketing `0 Mkt`.

---

## 1. O que este workflow faz

Monta o cronograma de preparação de uma campanha (estratégia, criativo, setup técnico, QA final, lançamento e primeiras 24h) e a matriz de sign-off por área. Verifica:
1. A marca, o nome e a data de lançamento da campanha.
2. O tipo de campanha e os canais envolvidos (e-mail, tráfego pago, landing page, social).
3. O plano de campanha já existente, se houver (ver workflow `revenue-criacao-de-campanha`).

---

## 2. Como executar

```
/revenue-checklist-de-lancamento-de-campanha
```
Ou com parâmetros contextuais:
```
/revenue-checklist-de-lancamento-de-campanha --marca plus-pr --campanha "Lançamento Q1" --data 2026-12-01
```

Se faltar a marca, perguntar antes de seguir (regra 1.1 do `CLAUDE.md`).

---

## 3. Instruções de execução passo a passo

### T-14 dias: Estratégia e planejamento
- [ ] Objetivo da campanha definido (SMART)
- [ ] Público-alvo documentado
- [ ] Mensagens-chave finalizadas
- [ ] Orçamento aprovado e alocado
- [ ] Métricas de sucesso definidas

### T-7 dias: Conteúdo e criativo
- [ ] Landing page no ar e com carregamento rápido
- [ ] Responsividade mobile verificada
- [ ] Formulário funcionando corretamente
- [ ] Copy revisado (filtro anti-slop)
- [ ] Assets visuais prontos

### T-3 dias: Setup técnico
- [ ] Metas de analytics configuradas
- [ ] Rastreamento de conversão instalado (UTMs, pixels)
- [ ] Fluxo de leads para o CRM testado
- [ ] Automação de e-mail pronta
- [ ] Anúncios montados e aprovados

### T-1 dia: QA final
- [ ] Jornada completa do usuário testada
- [ ] Todos os links verificados
- [ ] Testado em múltiplos navegadores/dispositivos
- [ ] Time de vendas alinhado
- [ ] Plano de contingência pronto

### T-0: Dia de lançamento
- [ ] Checagem final dos sistemas
- [ ] Ativação de todas as campanhas
- [ ] Monitoramento de erros
- [ ] Resposta ao engajamento inicial

### T+1: Desempenho inicial
- [ ] Revisão do desempenho da madrugada/primeiro dia
- [ ] Checagem da qualidade dos leads
- [ ] Ajuste de eventuais problemas
- [ ] Otimização com base nos primeiros dados

---

## Matriz de sign-off

| Área | Responsável | Aprovado | Data |
|---|---|---|---|
| Estratégia | | ☐ | |
| Criativo | | ☐ | |
| Copy | | ☐ | |
| Técnico | | ☐ | |
| Jurídico | | ☐ | |
| **Aprovação final** | | ☐ | |

---

## Delegação de agentes

| Tarefa | Agente | Gatilho |
|---|---|---|
| Revisão de copy | `copy-redacao-publicitaria` | QA de conteúdo |
| Otimização de landing page | `site-otimizacao-de-conversao` | Revisão da página |
| Roteamento de leads | `vendas-qualificacao-de-leads` | Setup de CRM |
| Alinhamento com vendas | `vendas-direcao-b2b` | Preparação de handoff |

---

## Onde salvar

Seguir o mapa de destinos do projeto (`docs/mapa-de-destinos.md`; skill `mapa-de-destinos`). Sem mapa, grave no padrão direto, sem marca no caminho: `estrategia/campanhas/AAAA-MM-DD - Nome da Campanha/checklist-lancamento.md` (o mapa do 0 Mkt, multi-marca, usa `content/<marca>/estrategia/campanhas/AAAA-MM-DD - Nome da Campanha/checklist-lancamento.md`).
