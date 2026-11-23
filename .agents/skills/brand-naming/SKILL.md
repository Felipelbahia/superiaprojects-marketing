---
# Source: https://github.com/clawdb
# Repository: https://github.com/Felipelbahia/superiaprojects-marketing
# Status: Customizada / Modificada localmente por Felipe Bahia
name: brand-naming
description: "Use para criar e validar nomes de marca, produto e empresa pelo protocolo dos 6 portões (briefing, geração, fonético, jurídico, AEO e narrativa). Gatilhos: \"nome da marca\", \"naming\", \"rebranding de nome\", \"nome para a empresa\". NÃO use para reposicionar uma marca que já tem nome (use brand-essence) nem para confirmar registro de marca (o portão jurídico indica a busca; quem confirma é o INPI ou um advogado)."
author: ClawFu & Antigravity Kit & Felipe Bahia (Futuro Mercado)
license: MIT
metadata:
  author: ClawFu & Antigravity Kit & Felipe Bahia (Futuro Mercado)
  version: 1.0.0
complements: brand-builder, brand-essence, brand-visual-direction, revenue-gtm-e-posicionamento
---
# Arquiteto de Nomes de Marca (Protocolo dos 6 Portões)

> Em 2026, dar nome a uma marca é engenharia, não palpite criativo. Um bom nome precisa ser lido por máquinas (tokenização eficiente em LLMs e mecanismos de resposta), defensável juridicamente em várias jurisdições, fácil de falar para assistentes de voz e carregado de narrativa.

## Quando usar

Use esta skill para:

- **Criar o nome de uma marca, empresa, produto ou submarca do zero**
- **Executar a etapa 0B (Naming) do `brand-builder`** quando a entidade é nova
- **Trocar um nome existente** por colisão de marca registrada ou expansão internacional
- **Otimizar o nome para descoberta por IA (AEO, Answer Engine Optimization)**, para que ChatGPT, Perplexity e Gemini o reconheçam como entidade distinta
- **Filtrar nomes candidatos** por testes rigorosos de fonética, idiomas, jurídico e narrativa

---

## A arquitetura dos 6 portões

Para sobreviver ao atrito do mercado, todo nome candidato passa por 6 portões eliminatórios, em sequência:

```
[1. BRIEFING] ──► [2. GERAÇÃO] ──► [3. LINGUÍSTICO] ──► [4. JURÍDICO] ──► [5. AEO] ──► [6. NARRATIVA]
  Restrições        5 tipologias      Pronúncia e         Marca e           Força de       Pilares de
  e limites         de exploração     gírias              conflitos         entidade       história
```

*Ver [references/naming-6-gates.md](references/naming-6-gates.md).*

---

## Portão 1: briefing de restrições

Antes de gerar qualquer ideia, fixe os limites que não se negociam:

| Parâmetro | Limite alvo | Motivo |
|---|---|---|
| **Comprimento** | 5 a 8 caracteres, no máximo | Leitura fácil, ícone de app no celular, tokenização limpa |
| **Sílabas** | 1 a 3 | Chamada por assistente de voz, memorização sem esforço |
| **Caracteres** | A a Z, sem hífen | Disponibilidade de domínio, digitação em qualquer teclado |
| **Riscos de fonética** | Sem letras mudas nem encontros difíceis | Evita erro de grafia e falha no reconhecimento de voz |

---

## Portão 2: geração em 5 tipologias

Gere lotes de candidatos por 5 estruturas distintas, em vez de associação livre de palavras:

1. **Analógica (transferência de domínio real):** termos da natureza, da arquitetura ou da mitologia (ex.: Apple, Amazon, Jaguar).
2. **Metafórica (transformação abstrata):** traduz uma dor ou mudança emocional em uma âncora concreta (ex.: Slack, Notion, Stripe).
3. **Neologismo (invenção fonética):** palavra nova com padrão sonoro harmônico (ex.: Kodak, Xerox, Plinq).
4. **Amálgama (fusão estratégica):** duas raízes que mantêm sentido ao se unir (ex.: Instagram, Pinterest).
5. **Vaso vazio (simetria fonética pura):** combinação distintiva de sons, sem bagagem de significado prévio (ex.: Rolex, Vimeo, Skype).

---

## Portão 3: teste fonético e multilíngue

- **Verificação por síntese de voz (TTS):** confira a clareza da pronúncia no Google TTS, no Amazon Polly e no ElevenLabs.
- **Gírias e armadilhas culturais:** procure palavrões, homófonos sensíveis e gírias negativas nos idiomas-alvo (PT, EN, ES, FR).
- **Uso por assistente de voz:** teste o atrito de chamar o nome por voz ("Ei Siri, abra [Nome]").

---

## Portão 4: triagem jurídica e de marca

Varredura eliminatória em 3 fases:

1. **Desqualificação rápida:** busca exata no Google, domínios `.com`, `.com.br`, `.io` e `.ai`, e disponibilidade do usuário nas redes sociais.
2. **Busca em registros:** pesquise as classes de Nice do negócio (ex.: classe 9 para software, 35 para marketing, 42 para SaaS) no INPI (Brasil), no USPTO (EUA) e no EUIPO (Europa).
3. **Avaliação de semelhança:** confira semelhança fonética, visual e conceitual com líderes de mercado.

Esta triagem **indica** a busca; quem confirma o registro é o INPI ou um advogado de propriedade intelectual.

---

## Portão 5: teste de AEO e força de entidade (descoberta por IA)

Garanta que os modelos de IA identifiquem o nome como entidade comercial distinta:

- **Teste de colisão zero:** pergunte a LLMs *"O que é [Nome]?"*. Uma resposta limpa (*"Não tenho informações sobre [Nome]"*) é melhor do que colidir com definições comuns de dicionário.
- **Dificuldade da palavra nos buscadores** (para ler a página de resultados de um termo, ver `seo-palavras-chave`, referência `serp-analyzer.md`): verifique se o nome não está soterrado por uma intenção de busca genérica de altíssimo volume, que enterraria sua presença orgânica.

Depois da escolha e do lançamento, construir a presença como entidade (sinais, Knowledge Graph, Wikidata) é trabalho da skill `seo-geo` (referências `entity-optimizer.md` e `knowledge-graph-guide.md`).

---

## Portão 6: potencial de história

Se a marca tem `01-essencia.md`, usar a história de criação e o credo como matéria-prima dos 5 pilares abaixo.

O nome precisa carregar a ética da empresa em 5 pilares narrativos:

- **História de origem:** o nome tem uma razão autêntica e compartilhável?
- **Âncora de crença:** sustenta naturalmente os valores centrais?
- **Verdade do produto:** sugere a velocidade, a força ou a simplicidade do que o produto entrega?
- **Arco de transformação:** representa a jornada do cliente, da dificuldade ao domínio?
- **Identidade de comunidade:** o cliente usa o nome como distintivo com orgulho (ex.: embaixadores do Notion, Plinqers)?

---

## Critérios de nome e estilos clássicos (complemento)

Vindo do `branding-expert` (arquivado em `_arquivo/mescladas/e5-brand/brand-essence/`). Use como lente extra depois do portão 2.

| Critério | Pergunta |
|---|---|
| Memorável | É fácil de lembrar? |
| Pronunciável | É fácil de falar? |
| Escrevível | É fácil de escrever sem errar? |
| Disponível | Domínio e registro de marca livres? |
| Significativo | As associações são relevantes? |
| Escalável | Continua servindo se a marca crescer? |

| Estilo | Exemplo | Vantagem | Atenção |
|---|---|---|---|
| Descritivo | General Electric | Claro | Fraco em AEO e difícil de registrar (ver portão 5) |
| Abstrato | Xerox | Só seu | Exige mais investimento em significado |
| Acrônimo | IBM | Curto | Pouco memorável sem contexto |
| Metáfora | Amazon | Evocativo | Coberto pela tipologia 2 do portão 2 |
| Nome do fundador | Ford | Pessoal | Depende da pessoa |
| Amálgama | Pinterest | Único | Coberto pela tipologia 4 do portão 2 |

---

## Checklist de verificação

- [ ] Nome com 5 a 8 letras e no máximo 3 sílabas
- [ ] Sem letras mudas nem pronúncia difícil
- [ ] Passou no teste de pronúncia (TTS) em português, inglês e espanhol
- [ ] Nenhum conflito de marca nas classes de Nice do negócio (INPI, USPTO, EUIPO)
- [ ] Domínio principal, ou domínio limpo com modificador, disponível
- [ ] Testado em LLMs quanto a ambiguidade e colisão de significado
- [ ] Razão narrativa aprovada, ligada ao propósito da marca

---

## Referências detalhadas

- [references/naming-6-gates.md](references/naming-6-gates.md): protocolo completo dos 6 portões, modelos de prompt e heurísticas de marca registrada
