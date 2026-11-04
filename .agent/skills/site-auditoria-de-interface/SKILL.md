---
# Repository: https://github.com/Felipelbahia/superiaprojects-marketing
# Status: Customizada / Modificada localmente por Felipe Bahia
name: site-auditoria-de-interface
description: "Use ANTES de alterar uma página, seção ou componente que já existe (site, landing page, interface): lê o estado atual, inventaria o que há, checa redundância e só propõe lacunas reais, com prova. Gatilhos: \"melhorar a página\", \"mexer no layout\", \"adicionar uma seção\", \"redesenhar a home\", \"adicionar componente\", quando já existe código ou página publicada. NÃO use para criar uma página do zero (use build-landing-page), para auditar conversão (use site-cro), para desenhar a interface (use site-interface-de-conversao) nem para revisar conformidade de código de UI (use site-diretrizes-web-codigo)."
author: Antigravity Multi-IA Hub & Felipe Bahia (Futuro Mercado)
license: MIT
metadata:
  author: Antigravity Multi-IA Hub & Felipe Bahia (Futuro Mercado)
  version: 1.0.0
---
<!--
Criado por: Madina Gbotoe (https://madinagbotoe.com/)
Projeto original: Claude Code Skills - Professional Development Toolkit
Versão original: 1.0 (28/10/2025) · Licença: MIT · Atribuição obrigatória: manter o nome e o link da autora
GitHub: https://github.com/mgbotoe/claude-code-share/tree/main/claude-code-skills/ui-ux-audit
Adaptação R16b (2026-10-20): texto em português, sem os dados do projeto original, gatilho estreito. Direito de uso confirmado pelo usuário.
-->

# UI/UX Audit

## Para que serve

**Impede implementação redundante e design inchado:** antes de mexer em algo que já existe, audita o estado atual. Nasceu de um incidente real: recomendações de interface foram implementadas **sem ler as páginas**, mostraram o mesmo dado duas vezes, esconderam os CTAs principais e foram revertidas, com horas perdidas.

## Quando roda

Só quando há **algo existente para alterar**: "melhorar a página inicial", "adicionar uma seção", "novo componente no hero", "redesenhar", "mexer no layout". Não roda para criar do zero nem para pedidos de copy ou de marca.

Ordem: **1)** esta auditoria; **2)** apresentar os achados ao usuário; **3)** (opcional) crítica de design com [site-interface-de-conversao](../site-interface-de-conversao/SKILL.md); **4)** implementar só o aprovado, aos poucos. Implementar código exige autorização explícita (regra 1.5 do projeto).

## Processo (ler primeiro, implementar depois)

### Passo 1. Ler o estado atual (inegociável)

Antes de qualquer recomendação, leia: o arquivo da página, os componentes relacionados, os arquivos de dados e de conteúdo, e busque por palavras do recurso proposto. Se o site é uma página publicada sem código acessível, use captura de tela e o conteúdo copiado. Diga **quais arquivos leu**.

### Passo 2. Documentar o que EXISTE, com prova

```markdown
## Estado atual: [página]
### Componentes existentes   (nome, arquivo e linhas, função)
### Dados exibidos           (onde aparece cada número, CTA e seção)
### Características de design (grade, espaço em branco, densidade, estilo)
### Prova                     (trechos de código ou captura)
```

### Passo 3. Checar redundância

- [ ] Esse dado já aparece em outro lugar da página?
- [ ] Já existe algo parecido em outra forma?
- [ ] Duplicaria conteúdo? Poluiria um desenho limpo?
- [ ] A informação aparece mais de uma vez?

**Antipadrões a evitar:** visualização que repete o que os cartões já mostram; cartão grande de assistente quando os CTAs principais já existem no hero; barra de métricas em página de estilo documento; painéis em página propositalmente mínima; adições em volume sem valor claro.

### Passo 4. Identificar lacunas REAIS (não supostas)

Só proponha o que for: funcionalidade ausente (provada pelo código), problema de UX demonstrado, valor claro e específico, que respeite o desenho limpo.

```markdown
### Lacuna 1: [elemento ausente]
- Prova: [o código mostra que não existe]
- Necessidade do usuário: [por quê]
- Valor: [benefício]
- Solução mínima: [o mais simples]
- Sem redundância: [confirmado que não duplica X]
```

### Passo 5. Checar a filosofia do design

Layout simples e escaneável; espaço em branco estratégico; informação mostrada **uma vez**; página de estilo documento continua documento; sem volume sem necessidade. Perguntas: soma valor ou só volume? é a solução mais simples? respeita o desenho existente? sobreviveria à revisão do usuário ou seria revertida?

## Modelo de saída

```markdown
# Auditoria de UI/UX: [página]
## Resumo do estado atual (2 a 3 frases)
## O que já EXISTE (lista, com arquivo e linhas)  + Prova
## Resultado da checagem de redundância (✅ nenhuma / ⚠️ onde duplica)
## Lacunas reais (prioridade 1, 2, ...: prova, impacto, solução mínima, esforço)
## NÃO recomendado (criaria redundância)
## Conformidade com a filosofia do design
## Recomendação e próximos passos (aprovação, crítica opcional, implementação incremental)
```

Um exemplo completo, bom contra ruim, em [resources/exemplo-de-auditoria.md](resources/exemplo-de-auditoria.md).

## Lista de verificação final

- [ ] Li todos os arquivos da página e dos componentes **antes**?
- [ ] Documentei o que existe, não o que presumi?
- [ ] Chequei redundância de forma sistemática?
- [ ] Identifiquei lacunas reais, com prova?
- [ ] A recomendação respeita o desenho limpo e é a mais simples?

Se alguma resposta for não, **pare e reavalie**.

## Onde isso se conecta

- Desenho de interface: [site-interface-de-conversao](../site-interface-de-conversao/SKILL.md). Conversão: [site-cro](../site-cro/SKILL.md). Código de UI: [site-diretrizes-web-codigo](../site-diretrizes-web-codigo/SKILL.md).
- Arquivados em `.agent/skills/_arquivo/mescladas/r16b-design/ui-ux-audit/`: o relato do incidente, o caso de sucesso e os dois exemplos originais (6.474 palavras que contavam a mesma história).
