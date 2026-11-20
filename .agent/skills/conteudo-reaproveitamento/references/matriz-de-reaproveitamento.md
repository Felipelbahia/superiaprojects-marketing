# Matriz de Reaproveitamento e Fluxo de Base Editorial

Guia operacional para orquestrar a multiplicação de conteúdo (1-para-Muitos) com rastreabilidade semântica, adaptação nativa por canal, governança de dados sensíveis e bloqueio estrito contra reaproveitamento mecânico (Hard Gate).

> **Origem conceitual:** Princípios de matriz de acervo, esteira de multiplicação 1-para-Muitos e fluxo editorial rastreável adaptados livremente a partir da arquitetura de `promovaweb/inboundfy`. Redação autoral e alinhada às diretrizes do hub `0 Mkt`.

---

## 1. A Matriz de Reaproveitamento Estruturada (8 Colunas Obrigatórias)

A multiplicação inteligente de conteúdo rejeita a simples fragmentação mecânica de texto. Cada ativo derivado precisa justificar sua existência respondendo a uma dor real de uma persona específica, ancorando-se em fatos verificáveis da fonte e respeitando o formato e o comportamento de consumo da plataforma de destino.

Toda estratégia de reaproveitamento deve consolidar o inventário de oportunidades na tabela de 8 colunas abaixo:

| # | Coluna da Matriz | Descrição e Finalidade | Exemplo de Aplicação |
|---|---|---|---|
| 1 | **Canal Ativo** | Rede ou meio de distribuição onde o conteúdo será publicado. | `LinkedIn`, `Instagram Carrossel`, `YouTube Shorts`, `Newsletter`, `Blog Técnico` |
| 2 | **Formato e Dimensão** | Especificação técnica do formato e tamanho da entrega. | `Post longo em texto (1.200 carac.)`, `Carrossel 7 lâminas`, `Vídeo vertical 60s`, `Artigo 1.500 palavras` |
| 3 | **Persona-Alvo** | Perfil específico do público que será impactado pela peça. | `Tech Lead / Arquiteto Cloud`, `Fundador / C-Level`, `Engenheiro de Dados Pleno` |
| 4 | **Dúvida / Dor Específica** | A pergunta ou atrito real da persona que o ativo responde diretamente. | *"Como diagnosticar se meu Pod no Kubernetes está morrendo por OOM (Out Of Memory)?"* |
| 5 | **Ângulo Editorial Nativo** | O recorte temático, gancho e enquadramento psicológico adaptado à plataforma. | **LinkedIn:** Decisão técnica sob pressão e gestão de incidentes. **Carrossel:** Checklist visual de sintomas de memória. |
| 6 | **Fato / Âncora / Timestamp** | A evidência factual primária com linha ou minutagem exata na transcrição saneada. | `Transcrição saneada: § 2, l. 4 [04:12 - 05:40]` (Limite de 512MB causava OOMKilled na fila Kafka) |
| 7 | **Permissão de Dados Sensíveis** | Classificação de conformidade jurídica e comercial dos dados expostos. | `Livre (dados técnicos puros)` ou `Requer Autorização / Anonimizar [Nome do cliente e queda percentual de 15%]` |
| 8 | **Prioridade Justificada** | Nível de urgência e valor estratégico (P1, P2, P3) com justificativa de esforço vs. impacto. | `P1 (Alto impacto técnico, resolve dor urgente da persona em momento de contratação)` |

---

## 2. O Hard Gate contra Reaproveitamento Mecânico

Um dos erros mais comuns em esteiras de conteúdo é o reaproveitamento preguiçoso: copiar a mesma narrativa linear, na mesma ordem de tópicos, e transpor para diferentes formatos (ex.: transformar 5 tópicos de um post em 5 slides idênticos de um carrossel e 5 tweets em fio).

```
┌────────────────────────────────────────────────────────────────────────┐
│              PORTÃO DE AUDITORIA: REAPROVEITAMENTO MECÂNICO            │
│                                                                        │
│   A mesma ordem cronológica de tópicos em múltiplos canais é           │
│   considerada REAPROVEITAMENTO MECÂNICO.                               │
│                                                                        │
│   Se o conjunto de peças derivadas apenas fatiar o texto original      │
│   sem criar uma arquitetura narrativa nativa para cada canal, o        │
│   conjunto é sumariamente REPROVADO no portão de qualidade.           │
└────────────────────────────────────────────────────────────────────────┘
```

### 2.1. Critérios Objetivos de Veredito

- **`REPROVADO` (Hard Gate):**
  - O carrossel é apenas a divisão em slides do mesmo texto corrido do LinkedIn;
  - O vídeo curto lê o mesmo parágrafo introdutório sem um gancho nativo de retenção;
  - A newsletter repete exatamente a mesma ordem de argumentos sem contextualização editorial de bastidores;
  - Dados sensíveis não autorizados (nomes de clientes, faturamento, incidentes sigilosos) aparecem em peças públicas.
- **`APROVADO`:**
  - **Diferenciação de Ângulo:** Cada canal explora um corte diferente do material bruto (ex.: LinkedIn aborda a cultura de comunicação em incidentes; Instagram Carrossel foca no diagrama do erro técnico; Blog aprofunda o tutorial de configuração do Kubernetes);
  - **Adaptação de Formato:** A linguagem respeita o ritmo do canal (frases visuais no carrossel, texto de liderança no LinkedIn, roteiro ágil no Reels);
  - **Anonimização Segura:** Dados sob alerta foram devidamente liberados ou convertidos em casos anônimos (`"Um grande cliente de e-commerce"`).

---

## 3. Regras de Coerência e Governança do Conjunto

Além da qualidade individual de cada peça, o conjunto de ativos derivados deve ser auditado em três dimensões estratégicas:

1. **Auditoria contra Contradição Factual entre Canais:** O que é afirmado como fato técnico em um canal não pode ser relativizado ou contradito em outro (ex.: não afirmar no blog que o limite era 1GB e no LinkedIn que era 512MB). A fonte imutável é a transcrição saneada.
2. **Auditoria de Saturação Temporal de Audiência:** A distribuição de peças derivadas do mesmo evento não deve ser descarregada no mesmo dia em todas as redes para o mesmo público. Distribua as publicações ao longo de uma janela de 2 a 3 semanas.
3. **Checagem de Sigilo e Termos de Consentimento:** Nenhuma métrica privada ou logotipo de cliente parceiro entra no pipeline sem a resposta afirmativa formal registrada no campo de permissão.

---

## 4. O Fluxo "Da Transcrição à Base Editorial" (5 Etapas)

Para garantir rastreabilidade completa desde a captura do áudio até a publicação final, todo projeto de reaproveitamento segue as 5 etapas estruturadas:

```
┌────────────────┐     ┌────────────────┐     ┌────────────────┐     ┌────────────────┐     ┌────────────────┐
│    ETAPA 1     │     │    ETAPA 2     │     │    ETAPA 3     │     │    ETAPA 4     │     │    ETAPA 5     │
│ Material Bruto │ ──> │   Saneamento   │ ──> │ Permissões &   │ ──> │ FAQ Rastreável │ ──> │ Base Editorial │
│    Imutável    │     │   e Relatório  │     │ Dados Sigilo   │     │ por Timestamp  │     │ Fatos x Teses  │
└────────────────┘     └────────────────┘     └────────────────┘     └────────────────┘     └────────────────┘
```

### Etapa 1: Material Bruto Imutável (`bruto.md`)
O arquivo de transcrição original é gravado e mantido strictly imutável. Ele serve como lastro legal e factual caso surjam disputas sobre o que foi dito.

### Etapa 2: Saneamento com Relatório de Limpeza (`saneado.md`)
Aplicação do protocolo de [`references/saneamento-de-material-bruto.md`](saneamento-de-material-bruto.md). Limpeza de ruídos orais, correção de grafias fonéticas e geração obrigatória do Relatório de Saneamento de 4 colunas.

### Etapa 3: Perguntas de Permissão e Validação de Dados Sensíveis
Varredura contra menções a:
- Nomes de pessoas físicas, clientes e concorrentes;
- Valores financeiros de receita, faturamento, custos ou multas;
- Prazos contratuais e cláusulas sob acordos de não-divulgação (NDA).
*Ação:* Caso não haja consentimento documentado, converter o dado para formato genérico na Base Editorial.

### Etapa 4: FAQ Rastreável por Linha e Timestamp
Extração das perguntas mais frequentes que a fala responde, apontando a linha e o timestamp da transcrição saneada onde se encontra a evidência.
- *Exemplo:* `"Pergunta: Por que a memória de 512MB travava o Kafka? -> Resposta: § 2, l. 4 [04:15] — O pool de conexões abertas gerava estouro de heap no pod."`

### Etapa 5: Base Editorial com Separação Fato vs. Interpretação
Consolidação do conhecimento em documento estruturado contendo:
- **Tabela de Fatos Observáveis:** Métricas, datas, erros de console, decisões técnicas executadas;
- **Tabela de Interpretações e Opiniões:** Avaliações subjetivas do autor, previsões de mercado e aprendizados pessoais;
- **Menu de Oportunidades Derivadas:** A Matriz de Reaproveitamento de 8 colunas pronta para alimentar redatores e designers.

