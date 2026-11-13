---
name: social-checklist-diario
description: Gera o checklist diário de gestão de redes sociais (comunidade, publicação, engajamento e métricas). Use para organizar a rotina diária de social media por bloco de tempo.
allowed-tools: Read, Write, Edit, Bash
---

# Checklist Diário de Social Media

> Workflow estruturado para a rotina diária de gestão de redes sociais, no padrão do Hub Super IA Projects - Marketing `0 Mkt`.

---

## 1. O que este workflow faz

Organiza a rotina diária de social media em blocos de tempo (manhã, meio-dia, tarde, fim do dia) e o painel de métricas da semana. Verifica:
1. A marca e as plataformas geridas (Instagram, LinkedIn, TikTok etc.).
2. O calendário editorial e os posts agendados em `content/<marca>/social/` ou `content/<marca>/linkedin/` (0 Mkt).
3. Alertas de menção ou comentário pendente, se houver monitoramento ativo.

---

## 2. Como executar

```
/social-checklist-diario
```
Ou com parâmetros contextuais:
```
/social-checklist-diario --marca experimentacao --plataformas instagram,linkedin
```

Se faltar a marca, perguntar antes de seguir (regra 1.1 do `CLAUDE.md`).

---

## 3. Instruções de execução passo a passo

### Manhã (primeiros 30 min)
**Gestão de comunidade (15 min)**
- [ ] Checar notificações em todas as plataformas
- [ ] Responder comentários das últimas 24h
- [ ] Responder DMs (priorizar leads)
- [ ] Endereçar reclamações, se houver

**Publicação (10 min)**
- [ ] Revisar posts agendados
- [ ] Verificar links e mídia
- [ ] Publicar conteúdo sensível ao tempo

**Monitoramento rápido (5 min)**
- [ ] Checar menções à marca
- [ ] Anotar temas em alta

### Meio-dia (15 min)
- [ ] Responder novos comentários
- [ ] Engajar com 5-10 posts (influenciadores, clientes)
- [ ] Compartilhar conteúdo de terceiros relevante

### Tarde (15 min)
- [ ] Rascunhar os posts de amanhã
- [ ] Agendar conteúdo na ferramenta de scheduling
- [ ] Checagem final de engajamento

### Fim do dia (10 min)
- [ ] Registrar métricas: seguidores, engajamento, DMs
- [ ] Anotar o melhor e o pior conteúdo do dia
- [ ] Verificar o agendamento de amanhã

---

## Metas de tempo de resposta

| Temperatura do lead | Tempo de resposta |
|---|---|
| Lead quente (70-100) | < 5 min |
| Lead morno (50-69) | < 1 hora |
| Reclamação de cliente | < 15 min |
| Comentário geral | < 4 horas |

---

## Painel de métricas semanais

| Métrica | Seg | Ter | Qua | Qui | Sex | Média |
|---|---|---|---|---|---|---|
| Novos seguidores | | | | | | |
| Taxa de engajamento | | | | | | |
| DMs | | | | | | |

---

## Delegação de agentes

| Tarefa | Agente | Gatilho |
|---|---|---|
| Ideias de conteúdo | `conteudo-brainstorm` | Gaps de conteúdo |
| Criação de copy | `copy-redacao-publicitaria` | Rascunho de post |
| Estratégia de engajamento | `social-calendario-e-distribuicao` | Construção de comunidade |
| Revisão de desempenho | `data-analise-de-desempenho` | Métricas diárias |

---

## Onde salvar

Seguir o mapa de destinos do projeto (`docs/mapa-de-destinos.md`; regra de resolução da skill `mapa-de-destinos`), tipo de peça `reports`: `content/<marca>/reports/AAAA-MM-DD - Checklist Social Diario/checklist.md` no 0 Mkt (regra 1.4 do `CLAUDE.md`); `conteudos/reports/AAAA-MM-DD - Checklist Social Diario/checklist.md` em projeto próprio.
