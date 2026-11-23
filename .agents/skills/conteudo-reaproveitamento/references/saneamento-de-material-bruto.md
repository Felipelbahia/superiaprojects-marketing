# Saneamento de Material Bruto (Transcrições e Áudios)

Guia operacional para higienizar transcrições de entrevistas, podcasts, reuniões e vídeos preservando a integridade da voz original do autor, eliminando ruídos orais sem reescrever o conteúdo e auditando intervenções em relatório padronizado de 4 colunas.

> **Origem conceitual:** Princípios de saneamento de áudio bruto, taxonomia de ruídos de fala e relatório de rastreabilidade adaptados livremente a partir da metodologia de `promovaweb/inboundfy`. Redação autoral e alinhada às diretrizes do hub `0 Mkt`.

---

## 1. A Regra de Ouro: Limpar Não É Reescrever

A função do saneamento de material bruto é puramente higiênica e documental. O saneador atua como um restaurador que limpa a fuligem de uma pintura antiga, jamais como um artista que repinta o quadro.

```
┌────────────────────────────────────────────────────────────────────────┐
│                      A REGRA DE OURO DO SANEAMENTO                     │
│                                                                        │
│   Limpar significa remover as impurezas mecânicas da fala oral.        │
│   Reescrever significa alterar o vocabulário, a ordem ou a tese.      │
│   O saneamento NUNCA reescreve: a voz, as metáforas e o ritmo da      │
│   pessoa que falou permanecem 100% preservados.                        │
└────────────────────────────────────────────────────────────────────────┘
```

---

## 2. Lista Taxativa de Intervenções

Para evitar que o assistente caia em tentação de embelezar ou pasteurizar a fala viva do autor, as intervenções permitidas e proibidas são estritamente delimitadas:

### 2.1. O que PODE ser corrigido (Higienização Permitida)
1. **Ruídos orais e muletas de preenchimento:** Supressão de hesitações e tiques orais que poluem a leitura (*"ééé"*, *"tipo assim"*, *"né"*, *"tá entendendo"*, *"quer dizer"*, *"aí tipo"*).
2. **Falsos inícios e gaguejos:** Remoção de recomeços de frase quando o falante repete palavras antes de engatar o raciocínio (*"a gente... nós começamos a olhar"* -> *"nós começamos a olhar"*).
3. **Pontuação e quebra de parágrafos:** Inserção de pontos finais, vírgulas de respiro e quebras de linha para transformar fluxo falado contínuo em parágrafos legíveis.
4. **Concordâncias orais grotescas:** Ajuste pontual e cirúrgico de deslizes de concordância estritamente orais que firam a compreensão, sem forçar erudição artificial.
5. **Correção de vocabulário técnico e nomes específicos conhecidos:** Ajuste de grafias fonéticas corrompidas por ferramentas de transcrição para a denominação técnica oficial consagrada (ex.: *"Cubernétis"* -> `Kubernetes`, *"Poustgre"* -> `PostgreSQL`, *"Asas"* -> `Asaas`), registrando a correção no relatório.

### 2.2. O que NUNCA pode ser corrigido (Proibições Absolutas)
1. **Nunca trocar palavras informais por jargão rebuscado:** Se o engenheiro disse *"o banco arregou"*, mantenha *"o banco arregou"*; jamais transforme em *"o banco de dados apresentou degradação de performance operacional"*.
2. **Nunca alterar o raciocínio ou a ordem cronológica:** A linha de pensamento do falante deve ser mantida na ordem em que foi exposta.
3. **Nunca suprimir atritos, erros ou opiniões fortes:** Não sanitize fracassos, dúvidas ou críticas relatadas pelo autor. O valor do conteúdo reside na verdade empírica.
4. **Nunca adivinhar trechos inaudíveis ou truncados:** Quando o áudio estiver corrompido ou ininteligível, é terminantemente proibido fabricar palavras para dar nexo sintático à frase. Aplique o marcador de incerteza correspondente.
5. **Nunca ignorar dados confidenciais ou sensíveis:** Se o autor mencionar faturamento sensível, nomes de clientes sigilosos ou métricas internas de parceiros, o trecho não deve ser alterado no material bruto saneado, mas obrigatoriamente sinalizado com marcador de risco de governança para checagem de autorização antes da distribuição.

---

## 3. Marcadores de Incerteza e Governança

Quando a transcrição apresentar lacunas ou riscos, utilize exclusivamente os marcadores estruturados abaixo:

| Marcador | Significado | Ação Operacional |
|---|---|---|
| `[inaudível]` | Trecho de áudio abafado, sobreposto ou com ruído impossível de transcrever com certeza. | Mantém o marcador no texto saneado e lista a dúvida no relatório para o autor confirmar. |
| `[trecho incerto: hipótese]` | Palavra que soa como determinado termo, mas com margem de dúvida audível. | Indica a melhor leitura com interrogação no relatório sem assumir certeza. |
| `[termo técnico a confirmar: termo]` | Jargão interno da empresa ou sigla proprietária não reconhecida publicamente. | Sinaliza para checagem de grafia ou expansão de acrônimo. |
| `[dado sensível: requer permissão]` | Menção nominal a cliente, faturamento, perda financeira ou vazamento de processo interno. | Destaca no relatório de saneamento que o dado não pode ser publicado sem liberação formal. |

---

## 4. Modelo de Relatório de Saneamento de Material Bruto (4 Colunas)

Toda operação de saneamento deve gerar, ao final do texto saneado, o **Relatório de Saneamento de Material Bruto** no formato estruturado abaixo:

### Cabeçalho
```markdown
# Relatório de Saneamento: [Título do Material ou Entrevista]

- **Fonte Original:** [Arquivo bruto ou URL de origem]
- **Data do Saneamento:** [AAAA-MM-DD]
- **Operador / Agente:** [Nome do agente]
- **Resumo de Métricas:**
  - Volume Bruto: [X palavras / caracteres]
  - Volume Saneado: [Y palavras / caracteres] (Redução de ruído: Z%)
  - Termos Técnicos Corrigidos: [N]
  - Trechos Inaudíveis / Dúvidas: [N]
  - Alertas de Dados Sensíveis: [N]
```

### Tabela de Intervenções (4 Colunas Oficiais)
| Trecho Original da Transcrição | Trecho Saneado | Tipo de Intervenção | Justificativa Operacional |
|---|---|---|---|
| *"Então, tipo assim, a gente... nós começamos"* | *"Nós começamos"* | Remoção de ruído oral e falso início | Elimina muleta verbal e falso recomeço preservando o sujeito e a ação. |
| *"o Cubernétis tava matando o pod"* | *"o Kubernetes estava matando o pod"* | Correção de fonética técnica | Restaura o nome técnico oficial consagrado do orquestrador de contêineres. |
| *"cara, [ruído ininteligível]... não deu"* | *"cara, [inaudível]... não deu"* | Aplicação de marcador de incerteza | Impede a alucinação de fala fictícia onde o áudio da gravação foi corrompido. |
| *"faturamento da empresa XPTO caiu 15%"* | *"faturamento da empresa XPTO caiu 15% [dado sensível: requer permissão]"* | Alerta de governança e sigilo | Alerta risco de conformidade: métrica financeira e cliente citados nominalmente. |

---

## 5. Exemplo Prático Completo: Antes, Depois e Relatório

### 5.1. Transcrição Bruta (Entrada)
> *"Então, tipo assim, a gente... nós começamos a olhar a fila do Kafka, né? E aí, tipo, o Cubernétis tava... nós fomos lá e o Cubernétis tava matando o pod toda hora porque o limite de memória tava em 512 mega, sabe? Aí o João falou, cara, [ruído ininteligível]... não deu pra entender direito o que ele disse ali na hora da reunião, mas a gente subiu pra 2 giga e o problema sumiu. Só que o faturamento da empresa XPTO caiu 15% naquele dia por causa do atraso."*

### 5.2. Material Saneado (Saída Fiel)
> *"Nós começamos a olhar a fila do Kafka. O Kubernetes estava matando o pod toda hora porque o limite de memória estava em 512 mega. Aí o João falou, cara, [inaudível], mas nós subimos para 2 giga e o problema sumiu. Só que o faturamento da empresa XPTO caiu 15% [dado sensível: requer permissão] naquele dia por causa do atraso."*

### 5.3. Relatório de Saneamento do Exemplo
| Trecho Original da Transcrição | Trecho Saneado | Tipo de Intervenção | Justificativa Operacional |
|---|---|---|---|
| *"Então, tipo assim, a gente... nós começamos"* | *"Nós começamos"* | Remoção de ruído oral e falso início | Elimina *"Então, tipo assim"* e hesitação inicial *"a gente..."*. |
| *"Kafka, né? E aí, tipo, o Cubernétis tava... nós fomos lá e o Cubernétis tava"* | *"Kafka. O Kubernetes estava"* | Remoção de ruídos e correção técnica | Pontua a frase, remove *"né? E aí, tipo"*, elimina falso início e corrige grafia fonética de *Kubernetes*. |
| *"tava em 512 mega, sabe? Aí o João"* | *"estava em 512 mega. Aí o João"* | Pontuação e corte de muleta | Substitui o interrogativo oral *"sabe?"* por ponto final. |
| *"[ruído ininteligível]... não deu pra entender direito o que ele disse ali na hora da reunião, mas a gente subiu"* | *"[inaudível], mas nós subimos"* | Marcador de incerteza e concisão oral | Preserva o marcador oficial `[inaudível]` sem supor o conselho do João; limpa o comentário sobre a acústica da reunião. |
| *"empresa XPTO caiu 15%"* | *"empresa XPTO caiu 15% [dado sensível: requer permissão]"* | Alerta de governança | Métrica de perda financeira e nome de cliente expostos exigem autorização expressa para uso público. |

