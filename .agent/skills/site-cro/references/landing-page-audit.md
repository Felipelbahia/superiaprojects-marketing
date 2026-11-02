---
name: landing-page-audit
description: "Auditoria de conversão de uma landing page contra o anúncio que traz o tráfego (Google e Meta): clareza do título, casamento de mensagem entre anúncio e página, CTA, confiança, atrito no celular e no formulário, com plano de ação por impacto. Use ao receber uma captura de tela ou URL da página, quando a conversão cai e as métricas do anúncio (CTR, CPC) não, e antes de lançar campanha."
metadata:
  platform: Google and Meta
  origem: fusão, na R16b (2026-10-20), de 10-google-and-meta-landing-page-audit.md e 39-google-and-meta-landing-page-audit.md (originais em _arquivo/mescladas/r16b-design/cro-page-auditor/)
---

# Auditoria de landing page (anúncio × página)

Análise sistemática de conversão com recomendações priorizadas. Para uma auditoria **com nota por seção** e reescrita de título, use [homepage-audit.md](homepage-audit.md); para o método e as ideias de teste, [page-cro.md](page-cro.md); para uma checagem rápida, o checklist de 15 pontos do `SKILL.md`.

## Quando usar

- A **taxa de conversão caiu e as métricas do anúncio (CTR, CPC) ficaram estáveis:** o problema costuma estar na página.
- **Antes de lançar** uma campanha, para pegar defeitos antes de gastar verba.
- Revisão trimestral das páginas de todas as campanhas ativas.
- Quando você faz teste A/B da página e precisa de hipóteses do que mudar.

## Entradas

O **anúncio** (texto, criativo, oferta) e a **página** (URL ou captura de tela; se for captura parcial, diga o que não deu para avaliar). Se houver, outras páginas da conta que convertem melhor, para comparar.

## Processo

1. **Capturar a página** (URL ou captura; anotar se é só uma parte).
2. **Casamento de mensagem:** o título da página repete o gancho do anúncio? A oferta é a mesma (preço, prazo, "sem cartão")? O CTA entrega a ação que o anúncio prometeu? Promessa que só aparece abaixo da dobra é desconexão.
3. **Acima da dobra:** primeira impressão, clareza, CTA visível.
4. **Mensagem:** estruturas de título, qualidade do texto, foco em benefício.
5. **Sinais de confiança:** prova social e credibilidade.
6. **Matadores de conversão:** atrito e distrações (formulário com campos que não ajudam o topo do funil, como telefone e porte da empresa, é caso clássico).
7. **Priorizar por impacto** e esforço.

## Estruturas de título para testar

| Estrutura | Forma | Exemplo |
|---|---|---|
| **4U** | Urgente + Único + Útil + Ultra-específico | "Dobre suas vendas em 30 dias" |
| **AIDA** | Atenção → Interesse → Desejo → Ação | Padrão ao longo das seções |
| **PAS** | Problema → Agitação → Solução | Começa pela dor, aprofunda, oferece alívio |
| **BAB** | Antes → Depois → Ponte | Mostra a transformação |

## Checklist acima da dobra

- [ ] Título com proposta de valor clara
- [ ] Subtítulo que explica o "como"
- [ ] Imagem ou vídeo que representa o **resultado**, não só o produto
- [ ] Botão principal com contraste, visível sem rolar
- [ ] Um sinal de confiança (logos, nota, depoimento)
- [ ] Navegação mínima (remover links que desviam)

## Onde pôr o CTA

| Local | Função |
|---|---|
| Hero | Conversão principal, mais visível |
| Depois da proposta de valor | Reforça depois de comunicar valor |
| Depois da prova social | Converte depois de construir confiança |
| Depois de recursos e benefícios | Captura depois de educar |
| Cabeçalho ou rodapé fixos | Acesso constante em páginas longas |

## 10 matadores de conversão

| Matador | Correção |
|---|---|
| Carregamento lento | Otimizar imagens, CDN (números de impacto em [element-benchmarks.md](element-benchmarks.md)) |
| Anúncio e página não casam | Igualar título e oferta |
| Proposta de valor confusa | Clarificar o título |
| CTAs concorrentes | Um CTA principal |
| Formulário longo | Reduzir ao essencial |
| Sem sinais de confiança | Acrescentar prova |
| Celular ruim | Layout responsivo; alvo de toque 48 px |
| CTA abaixo da dobra | Subir |
| Poluição visual | Simplificar |
| Texto do CTA fraco | Verbo de ação + valor |

## Modelo de saída

```markdown
## Auditoria de landing page
**Página / anúncio:** ...  **Data:** ...  **Nota geral:** X/100

### Casamento anúncio × página (nota por anúncio e desconexões, com correção)
### Acima da dobra (elemento · presente? · eficácia /10)
### Análise do título (atual · estrutura · problemas · reescrita sugerida)
### Matadores detectados (problema · gravidade 🔴🟡🟢 · impacto · correção)
### Auditoria de CTA (CTA · local · texto · problemas)
### Inventário de sinais de confiança (logos, depoimentos, notas, estudos de caso, selos, garantia)
### Atrito do formulário (quais campos provavelmente causam saída)
### Plano de ação (prioridade · correção · impacto esperado · esforço)
### Celular (responsivo · alvo 48 px · texto legível · carga rápida · formulário)
### Nível de confiança da análise: ALTO / MÉDIO / BAIXO
```

## Regras

- Se a captura for parcial, diga quais seções não deu para avaliar; avaliação de celular pede captura separada.
- Sempre ofereça **reescrita específica**, não só crítica.
- Priorize por impacto × esforço.
- **Nunca afirme ganho exato de conversão:** use faixas e diga que são estimativas.
- Compare com as outras páginas da conta que convertem melhor, quando houver.
