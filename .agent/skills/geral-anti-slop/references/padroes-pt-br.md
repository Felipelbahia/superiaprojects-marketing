# Padrões de IA em Português do Brasil e Formato de Auditoria

Catálogo sistemático dos 9 padrões de escrita automatizada em língua portuguesa, regras de interpretação contextual, modelo de relatório de auditoria e casos de regressão controlados. Complementa a skill `geral-anti-slop`.

> **Origem conceitual:** Padrões de detecção de vícios automatizados, matriz de auditoria por trecho e protocolo de regressão adaptados livremente a partir da arquitetura de `promovaweb/inboundfy`. Redação autoral e alinhada às diretrizes do hub `0 Mkt`.

---

## 1. As 9 Categorias de Padrões de IA em Português do Brasil

Quando modelos de linguagem geram texto em português, manifestam vícios recorrentes de vocabulário, sintaxe e estrutura retórica. A identificação desses padrões permite apontar o problema com precisão cirúrgica:

### 1. Aberturas Clichês e Aquecimento de Garganta (*Throat-Clearing*)
- **Manifestação:** Frases introdutórias ocas que gastam a atenção do leitor antes de tocar no assunto principal.
- **Expressões típicas:** *"No cenário atual de..."*, *"Em um mundo cada vez mais digital e dinâmico..."*, *"Nos dias de hoje..."*, *"É indiscutível que..."*, *"No ecossistema corporativo contemporâneo..."*.
- **Correção:** Eliminar o preâmbulo por inteiro e abrir o parágrafo diretamente no fato, no sujeito ou na decisão operacional.

### 2. Fórmulas de Contraste Direto e Decalques Sintáticos
- **Manifestação:** Estrutura binária em que o modelo nega uma ideia óbvia para afirmar outra como revelação transcendental, espelhando a fórmula do inglês *"This isn't about X—it's about Y"*.
- **Expressões típicas:** *"Não é apenas sobre [X] — é sobre [Y]"*, *"Longe de ser apenas uma ferramenta, trata-se de..."*, *"Em vez de focar em [A], a verdadeira virada de chave está em [B]"*.
- **Correção:** Excluir a negação retórica e formular uma proposição afirmativa direta com foco no mecanismo de funcionamento.

### 3. Elogio Vazio, Jargão Promocional (*Puffery*) e Adjetivação Inflada
- **Manifestação:** Superlativos e adjetivos abstratos usados para inflar a relevância de um processo comum sem apresentar dados concretos.
- **Expressões típicas:** *"desempenha um papel crucial/vital/fundamental"*, *"verdadeiro divisor de águas"*, *"solução revolucionária"*, *"experiência transformadora"*, *"robusto"*, *"pioneiro"*, *"inovador"*, *"arquitetura de ponta"*.
- **Correção:** Substituir adjetivos grandiloquentes por dados empíricos, números de operação ou descrição factual do que a ferramenta executa.

### 4. Conectores e Transições Muletas
- **Manifestação:** Conjunções e locuções inseridas de forma protocolar no início de períodos para simular coesão onde não há ligação causal verdadeira.
- **Expressões típicas:** *"Além disso,"*, *"Ademais,"*, *"Outrossim,"*, *"Portanto,"* (quando usado sem premissa lógica real), *"Dito isso,"*, *"Vale destacar que,"*, *"É importante ressaltar que,"*, *"Por outro lado,"*.
- **Correção:** Variar as transições, fundir períodos correlatos ou retirar a locução, iniciando a oração diretamente pelo sujeito.

### 5. Trincas de Adjetivos e Paralelismo Forçado (*Rule of Three*)
- **Manifestação:** Agrupamento compulsivo de três substantivos ou adjetivos para encerrar frases com cadência oratória previsível.
- **Expressões típicas:** *"uma solução rápida, eficiente e segura"*, *"trazendo clareza, previsibilidade e escalabilidade"*, *"otimizar, acelerar e transformar a operação"*.
- **Correção:** Manter apenas a característica que possui respaldo factual comprovado ou descrever o processo em ação.

### 6. Perguntas Retóricas Simétricas com Auto-Resposta Imediata
- **Manifestação:** O autor cria subtítulos ou frases interrogativas artificiais apenas para respondê-las na linha seguinte, simulando um diálogo socrático falso.
- **Expressões típicas:** *"Mas como garantir esse resultado? O segredo está em..."*, *"O que isso significa na prática? Significa que..."*, *"Por que isso é tão importante? Porque..."*.
- **Correção:** Converter a pergunta e a resposta em um único parágrafo declarativo ou em um subtítulo substantivo que anuncie o tema da seção.

### 7. Fragmentação Dramática e Microparágrafos Isolados
- **Manifestação:** Frases de efeito curtas isoladas em linhas próprias, simulando suspense ou profundidade emocional desproporcional ao tema técnico.
- **Expressões típicas:** Linhas soltas como *"Simples assim."*, *"Ponto final."*, *"E foi exatamente isso que aconteceu."*, parágrafos sucessivos de uma única frase curta.
- **Correção:** Agrupar causa, ação e consequência em parágrafos coesos, dosando a cadência rítmica sem afetação teatral.

### 8. Conclusões e Resumos Redundantes
- **Manifestação:** Parágrafos finais que apenas repetem o que já foi exposto, sem acrescentar diretriz ou desdobramento prático.
- **Expressões típicas:** *"Em suma, fica evidente que..."*, *"Em conclusão..."*, *"Em última análise..."*, *"Diante de tudo o que foi exposto, resta claro que..."*.
- **Correção:** Substituir o fechamento redundante por um próximo passo operacional, um critério de monitoramento ou uma recomendação técnica.

### 9. Vícios Sintáticos e Decalques de Tradução em Português
- **Manifestação:** Estruturas artificiais herdadas da sintaxe inglesa ou do jargão de redação de IA.
- **Expressões típicas:**
  - Omissão telegráfica de artigos: *"Atrito nasce quando critério não tem evidência"* em vez de *"O atrito surge quando um critério..."*.
  - Gerundismo de causalidade vaga: *"...implicando em atraso"*, *"...culminando em prejuízo"*, *"...proporcionando uma melhora"*.
  - Nominalizações burocráticas pesadas: *"foi efetuada a realização do deploy"* em vez de *"a equipe fez o deploy"*.
- **Correção:** Restaurar a sintaxe natural da língua portuguesa com artigos definidos/indefinidos, orações desenvolvidas na voz ativa e verbos plenos.

---

## 2. A Regra Central de Interpretação: Agrupamento e Muleta

A aplicação rígida e descontextualizada deste catálogo gera sobre-edição e destrói textos humanos legítimos. Por isso, a seguinte regra de governança é mandatória para qualquer revisor ou subagente:

```
Uma ocorrência isolada de um termo legítimo NÃO configura vício de escrita.
O slop se caracteriza pela CONCENTRAÇÃO de padrões, pela AUSÊNCIA de fatos concretos
e pelo uso de termos como MULETA de encerramento ou preenchimento de espaço.
```

### Critérios de distinção:
- **Uso legítimo:** *"Portanto, se o log marcar erro 500, reinicie a fila."* (Dedução lógica direta em runbook operacional).
- **Uso como slop:** *"Portanto, automatizar processos é fundamental para o sucesso corporativo."* (Fechamento genérico e vazio).
- **Uso legítimo:** *"Webhook do Asaas"* / *"Worker de processamento"* (Termos técnicos indispensáveis).
- **Uso como slop:** *"Pipeline de sinergias holísticas"* (Jargão oco para mascarar falta de conteúdo).

---

## 3. Modelo de Relatório de Auditoria por Trecho (5 Colunas)

Quando acionada no modo de auditoria ou durante os marcos de revisão do projeto, a skill `geral-anti-slop` emite o parecer no formato estruturado abaixo:

### Cabeçalho Obrigatório
```markdown
# Auditoria Anti-Slop: [Nome da Peça ou Arquivo]

- **Marco de Revisão:** [brief | rascunho | final]
- **Ciclo:** [1, 2, ...]
- **Modo:** Auditoria de Conformidade
- **Arquivo Analisado:** [Caminho relativo]
- **Veredito Geral:** [APROVADO | AJUSTES NECESSÁRIOS | REPROVADO]
```

### Tabela de Achados (5 Colunas)
| Local e Trecho Auditado | Categoria do Padrão | Regra / Justificativa | Diagnóstico e Efeito no Leitor | Ação Recomendada |
|---|---|---|---|---|
| `§ 1, l. 4`: *"No cenário atual de transformação..."* | 1. Abertura Clichê | Cortar aberturas de aquecimento | Afasta o leitor com preâmbulo vazio | Eliminar e abrir direto na ação do sistema |
| `§ 2, l. 8`: *"não é apenas sobre X — é sobre Y"* | 2. Contraste Direto | Eliminar fórmula binária artificial | Soa como pregação didática de IA | Reescrever com proposição afirmativa direta |
| `§ 3, l. 14`: *"...identificou que haviam três gargalos..."* | Norma Culta (Gramática) | `Haver` no sentido de existir é impessoal | Erro gramatical grave compromete autoridade | Substituir por `"havia três gargalos"` |

### Critérios do *Hard Gate*
- **`APROVADO`:** Zero ocorrências das 9 categorias e zero desvios de norma culta. O texto pode seguir para aprovação e publicação imediatamente.
- **`AJUSTES NECESSÁRIOS`:** Presença de até 3 desvios menores que podem ser resolvidos pontualmente sem alterar a estrutura da tese central.
- **`REPROVADO`:** Ocorrência de múltiplos vícios combinados, abertura clichê com promessa sem mecanismo, ausência generalizada de dados reais ou erros de concordância/regência graves. Exige reescrita substantiva da seção afetada antes de nova submissão.

---

## 4. Casos de Regressão em Português do Brasil

Para calibrar detectores e validar subagentes revisores, estes quatro casos representam a suíte padrão de teste de regressão:

### Caso 1: Peça Reprovada de Propósito
```markdown
### Por que o suporte moderno falha tanto?
A resposta é simples: falta de visão estratégica.

No cenário dinâmico de hoje, o atendimento ao cliente desempenha um papel crucial no sucesso das empresas. Além disso, o software de chamados não é apenas sobre responder tickets — é sobre construir um ecossistema integrado, rápido e acolhedor. A equipe de atendimento ao cliente, implementou melhorias onde haviam gargalos, implicando em otimização operacional. Em suma, essa abordagem inovadora é um divisor de águas que transforma a retenção em escala.
```

### Caso 2: Relatório de Auditoria por Trecho (Referência de Saída)
```markdown
# Auditoria Anti-Slop: Caso 1 (Suporte Moderno)

- **Marco de Revisão:** rascunho
- **Ciclo:** 1
- **Modo:** Auditoria de Conformidade
- **Veredito Geral:** REPROVADO

| Local e Trecho Auditado | Categoria do Padrão | Regra / Justificativa | Diagnóstico e Efeito no Leitor | Ação Recomendada |
|---|---|---|---|---|
| `Título e § 1`: *"### Por que o suporte...? / A resposta é simples..."* | 6. Pergunta Retórica Simétrica | Eliminar auto-resposta artificial em H3 | Estrutura robótica previsível | Transformar em seção declarativa com o tema real |
| `§ 2, l. 1`: *"No cenário dinâmico de hoje..."* | 1. Abertura Clichê | Eliminar preâmbulos vazios | Desperdiça o início do texto com clichê temporal | Cortar e iniciar com o sujeito ou dado empírico |
| `§ 2, l. 2`: *"desempenha um papel crucial"* | 3. Elogio Vazio / Puffery | Afirmação sem mecanismo ou prova | Elogio genérico que não informa nada | Apresentar métrica real de atendimento ou cortar |
| `§ 2, l. 3`: *"não é apenas sobre X — é sobre Y"* | 2. Contraste Direto | Banir fórmula binária artificial de IA | Decalque direto do inglês que irrita o leitor | Declarar diretamente a função real do software |
| `§ 2, l. 4`: *"integrado, rápido e acolhedor"* | 5. Trinca de Adjetivos | Evitar paralelismo compulsivo de 3 adjetivos | Soa como slogan publicitário genérico | Citar a funcionalidade específica testada |
| `§ 2, l. 5`: *"A equipe [...], implementou"* | Norma Culta (Pontuação) | Proibida a inserção de vírgula entre sujeito e predicado | Erro gramatical evidente de pontuação | Remover a vírgula após `cliente` |
| `§ 2, l. 5`: *"onde haviam gargalos"* | Norma Culta (Gramática) | `Onde` para local físico; `haver` impessoal no singular | Duplo desvio: pronome indevido e erro de concordância | Trocar por `"em que havia gargalos"` |
| `§ 2, l. 6`: *"implicando em otimização"* | Norma Culta (Regência) | `Implicar` no sentido de causar é transitivo direto | Regência indevida com preposição `em` | Corrigir para `"implicando otimização"` ou oração direta |
| `§ 2, l. 6`: *"Em suma, essa abordagem inovadora..."* | 8. Conclusão Redundante + Puffery | Não fechar com resumo repetitivo nem autopromoção | Termina sem instrução prática | Encerrar com o resultado apurado ou próximo passo |
```

### Caso 3: Peça Corrigida (Aprovada)
```markdown
Na última segunda-feira, a equipe de suporte identificou que havia 84 chamados represados há mais de duas horas no balcão de notas fiscais. O atraso acontecia porque o formulário de abertura não exigia a chave de acesso do documento, forçando o atendente a pedir o número por mensagem. Atualizamos os campos obrigatórios no portal e o tempo médio de primeira resposta caiu de 45 para 12 minutos ao longo da semana.
```

### Caso 4: Peça Limpa contra Falso Positivo (Calibração)
```markdown
Na terça-feira (14/05), o webhook do Asaas devolveu erro 502 por 18 minutos logo após o lote das 9h. A primeira tentativa de reprocessar a fila inteira de uma vez travou o worker porque o banco abriu 400 conexões simultâneas. Limitamos o lote para 25 boletos por segundo no `queue.py`. Portanto, se o painel marcar mais de 30 boletos pendentes por 5 minutos, cheque a fila `billing_retry` antes de reiniciar o serviço.
```
- **Veredito:** `APROVADO`
- **Justificativa de calibração:**
  - O conector *"Portanto"* não é resumo vazio: introduz uma regra imperativa de contingência baseada nas premissas fáticas demonstradas no parágrafo.
  - Termos técnicos em inglês (*webhook*, *worker*, *queue.py*, *billing_retry*) são indispensáveis e legítimos.
  - Números, prazos e códigos são concretos e verificáveis. Zero alterações necessárias.
