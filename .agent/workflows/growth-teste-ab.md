---
name: growth-teste-ab
description: Gera o plano de um teste A/B de marketing (hipótese, variantes, critério estatístico e cronograma mínimo). Use quando for testar um elemento de e-mail, landing page, anúncio ou site.
allowed-tools: Read, Write, Edit, Bash
---

# Plano de Teste A/B

> Workflow estruturado para planejar um teste A/B de marketing, no padrão do Hub Super IA Projects - Marketing `0 Mkt`.

---

## 1. O que este workflow faz

Monta o plano de um teste A/B: hipótese, variantes, cálculo de rigor estatístico, checklist de execução e análise. Verifica:

1. A marca, o canal (e-mail, landing page, anúncio, site) e o elemento a testar.
2. Testes anteriores já registrados, se houver, para não repetir aprendizado.
3. O nível de rigor estatístico necessário para a decisão.

---

## 2. Como executar

```
/growth-teste-ab
```
Ou com parâmetros contextuais:
```
/growth-teste-ab --marca plus-pr --canal landing-page --elemento headline
```

Se faltar a marca, perguntar antes de seguir (regra 1.1 do `CLAUDE.md`).

---

## 3. Instruções de execução passo a passo

### Fase 1: Desenvolvimento da hipótese
- [ ] Definir o problema
- [ ] Criar a hipótese: "Se mudarmos [X], então [métrica Y] vai [aumentar/diminuir] porque [razão Z]"
- [ ] Definir o resultado esperado

### Fase 2: Desenho do teste

| Variante | Descrição |
|---|---|
| A (controle) | [atual] |
| B (teste) | [mudança] |

- [ ] Calcular o tamanho de amostra necessário
- [ ] Definir a duração mínima do teste

### Fase 3: Setup de execução
- [ ] Configurar o rastreamento
- [ ] Configurar a divisão de tráfego
- [ ] QA das duas variantes

### Fase 4: Análise e implementação
- [ ] Verificar significância estatística
- [ ] Documentar os aprendizados
- [ ] Implementar a variante vencedora

---

## Testes comuns por canal

**E-mail**

| Elemento | Ideias de teste |
|---|---|
| Linha de assunto | Tamanho, personalização, emoji, urgência |
| Preview text | Ganchos diferentes, CTAs |
| Nome do remetente | Empresa vs. pessoa |
| Horário de envio | Dia da semana, horário |
| Botão de CTA | Cor, texto, posição |

**Landing page**

| Elemento | Ideias de teste |
|---|---|
| Headline | Benefício vs. feature, pergunta vs. afirmação |
| Imagem principal | Pessoas vs. produto, vídeo vs. imagem |
| Botão de CTA | Cor, tamanho, texto, posição |
| Tamanho do formulário | Campos obrigatórios, single-step vs. multi-step |
| Prova social | Depoimentos, logos, números |

**Anúncio**

| Elemento | Ideias de teste |
|---|---|
| Headline | Propostas de valor diferentes |
| Descrição | Features vs. benefícios |
| Imagem/vídeo | Visuais diferentes |
| CTA | Verbos de ação diferentes |

---

## Priorização de testes (framework ICE)

| Ideia de teste | Impacto (1-10) | Confiança (1-10) | Facilidade (1-10) | Score ICE |
|---|---|---|---|---|
| | | | | |

**Score ICE = (Impacto + Confiança + Facilidade) / 3**

---

## Regras de teste

**Fazer:**
- Testar uma variável por vez
- Rodar até atingir significância estatística
- Documentar tudo
- Ter hipótese clara
- Definir métricas antes de começar

**Não fazer:**
- Não parar o teste antes da hora
- Não espiar os dados e decidir no meio do caminho
- Não testar várias coisas ao mesmo tempo
- Não ignorar dados por segmento
- Não esquecer de implementar o vencedor

**Duração mínima recomendada:**
- E-mail: 24-48h (envio completo)
- Landing page: 2-4 semanas
- Anúncios: 1-2 semanas no mínimo
- Site: 2+ semanas

---

## Delegação de agentes

| Tarefa | Agente | Gatilho |
|---|---|---|
| Criação de hipótese | `conteudo-brainstorm` | Ideação de teste |
| Variantes de copy | `copy-redacao-publicitaria` | Teste de conteúdo |
| Análise de resultado | `revenue-pesquisa-de-mercado` | Revisão de resultado |
| Recomendações | `revenue-planejamento-de-campanha` | Próximos passos |

---

## Onde salvar

Seguir o mapa de destinos do projeto (`docs/mapa-de-destinos.md`; skill `geral-arquitetura-de-projeto`). Sem mapa, grave no padrão direto, sem marca no caminho: `estrategia/campanhas/AAAA-MM-DD - Teste AB [Elemento]/plano-de-teste.md` (o mapa do 0 Mkt, multi-marca, usa `content/<marca>/estrategia/campanhas/AAAA-MM-DD - Teste AB [Elemento]/plano-de-teste.md`).
