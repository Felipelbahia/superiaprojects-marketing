---
name: conteudo-aprovacao
description: Gera o fluxo de aprovação de uma peça de conteúdo (etapas, responsáveis, SLA e checklist por estágio). Use quando uma peça precisar passar por revisão antes de publicar.
allowed-tools: Read, Write, Edit, Bash
---

# Aprovação de Conteúdo

> Workflow estruturado para definir e acompanhar o fluxo de aprovação de uma peça de conteúdo, no padrão do Hub Super IA Projects - Marketing `0 Mkt`.

---

## 1. O que este workflow faz

Monta o fluxo de aprovação de uma peça (post, e-mail, landing page, blog etc.): estágios, responsáveis por revisão, SLA por tipo de conteúdo e checklist de cada etapa. Verifica:
1. A marca e o tipo de conteúdo em questão.
2. A pasta da peça, seguindo a regra de resolução da skill `mapa-de-destinos` (`content/<marca>/<tipo>/` no 0 Mkt; `conteudos/<tipo>/` em projeto próprio).
3. Se já existe um fluxo de aprovação padrão registrado no mapa de destinos do projeto (`docs/mapa-de-destinos.md`), reaproveitar; senão, propor o abaixo.

---

## 2. Como executar

```
/conteudo-aprovacao
```
Ou com parâmetros contextuais:
```
/conteudo-aprovacao --marca plus-pr --tipo blog
```

Se faltar a marca, perguntar antes de seguir (regra 1.1 do `CLAUDE.md`).

---

## 3. Instruções de execução passo a passo

### Fase 1: Rascunho
- [ ] Brief entendido e público-alvo definido
- [ ] Mensagens-chave incluídas
- [ ] Palavras-chave de SEO incorporadas (se aplicável)
- [ ] CTA claro
- [ ] Autorrevisão concluída

### Fase 2: Revisão
**Revisor de conteúdo:**
- [ ] Precisão factual
- [ ] Consistência com o tom de voz da marca (`brand-voice.md`)
- [ ] Gramática e ortografia
- [ ] Fluxo lógico

**Revisor de SEO** (quando aplicável):
- [ ] Posicionamento da palavra-chave principal
- [ ] Estrutura de títulos
- [ ] Meta tags otimizadas

### Fase 3: Ajustes
- [ ] Endereçar os pontos obrigatórios ("Must Fix")
- [ ] Considerar as sugestões ("Should Fix")
- [ ] Atualizar a versão do arquivo (ver regra de não sobrescrever versões — salvar como nova versão, não editar a anterior)

### Fase 4: Aprovação e publicação
- [ ] Todo o feedback endereçado
- [ ] Padrões de qualidade atendidos (anti-slop, regra 1.3 do `CLAUDE.md`)
- [ ] Sign-off final
- [ ] Agendado/publicado

---

## Matriz de tipo de conteúdo

| Tipo | Revisores | Aprovação | SLA |
|---|---|---|---|
| Blog | Conteúdo + SEO | Responsável de marketing | 3 dias |
| Post social | Conteúdo | Responsável de social | Mesmo dia |
| E-mail | Conteúdo + Jurídico (se houver claim) | Responsável de e-mail | 2 dias |
| Landing page | Conteúdo + SEO + Jurídico (se houver claim) | Responsável de marketing | 5 dias |

---

## Delegação de agentes

| Tarefa | Agente | Gatilho |
|---|---|---|
| Criação de conteúdo | `copy-redacao-publicitaria` / `conteudo-criacao-multiformato` | Estágio de rascunho |
| Revisão de SEO | `seo-otimizacao-de-busca` | Otimização |
| Revisão de tom de marca | `brand-guardiao-de-voz` | Consistência de voz |
| Polimento final | `copy-redacao-publicitaria` | Ajustes |

---

## Onde salvar

O fluxo de aprovação em si não gera um arquivo novo por padrão — ele acompanha a peça que já está sendo produzida, na pasta definida pela regra de resolução da skill `mapa-de-destinos` (`content/<marca>/<tipo>/AAAA-MM-DD - Nome da Demanda/` no 0 Mkt). Se o usuário pedir um checklist de aprovação como arquivo separado, salvar como `aprovacao.md` dentro dessa mesma pasta.
