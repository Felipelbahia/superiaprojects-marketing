---
name: copy-roteiro-mais-falado
description: Transforma um roteiro de vídeo em uma versão mais falada e natural, removendo a linguagem de texto escrito e aumentando a sensação de proximidade. Use quando o usuário mencionar "roteiro de vídeo", "gravação", "mais falado", "soa natural", "parece que está falando", "está muito escrito/formal demais".
---

# Revisão para tornar o roteiro de vídeo mais falado

> Traduzido para português em 2026-10-28 (E6): a versão anterior estava 100% em chinês (frontmatter e corpo), sem nenhum gatilho em português, o que a tornava inacessível neste hub (regra 2.9 do CLAUDE.md). Função mantida; exemplos adaptados de chinês para português.

## Quando usar esta skill
Use esta técnica quando o usuário pedir algo como:
- Revisar um "roteiro de vídeo" ou "roteiro de gravação"
- Tornar o texto "mais falado", "mais natural", "como se estivesse conversando"
- Disser que o roteiro está "muito escrito", "formal demais", "sem naturalidade"
- Quiser um roteiro "melhor para gravar", "que saia mais fácil na fala"
- Precisar de mais "proximidade" e de uma linguagem "do dia a dia"

## Objetivo central
Transformar um roteiro formal e escrito em uma fala natural e fluida, para que o vídeo soe como uma conversa real e não como uma leitura, aumentando a proximidade com quem assiste e a experiência de visualização.

## Processo de execução

### Primeira passada: trocar vocabulário de texto escrito (nível P0)
**Objetivo:** remover as expressões claramente escritas, não faladas.

**Trocas principais:**
1. **Verbos**
   - ❌ "realizar" → ✅ "fazer"
   - ❌ "implementar" → ✅ "colocar em prática", "fazer"
   - ❌ "disponibilizar" → ✅ "dar", "oferecer para vocês"
   - ❌ "ocasionar" → ✅ "causar", "por isso"
   - ❌ "deparar-se com" → ✅ "encontrar", "topar com"

2. **Conectivos**
   - ❌ "portanto" → ✅ "então", "por isso"
   - ❌ "entretanto" → ✅ "mas", "só que"
   - ❌ "ademais" → ✅ "e também", "além disso" (evitar quando sonar de IA — ver [ai-slop-detector](ai-slop-detector.md))
   - ❌ "em suma" → ✅ "resumindo", "no fim das contas"

3. **Substantivos**
   - ❌ "o referido produto" → ✅ "esse produto", "ele"
   - ❌ "este método" → ✅ "esse jeito", "essa forma"
   - ❌ "o usuário" → ✅ "vocês", "a gente"

### Segunda passada: ajustar a estrutura da frase (nível P1)
**Objetivo:** deixar a frase mais parecida com fala.

**Ajustes:**
1. **Combinar frases longas e curtas**
   - Evitar frases compostas longas demais
   - Usar mais frases curtas
   - Manter o ritmo natural de quem fala

2. **Inversão e omissão**
   - Usar construções de ênfase ("é isso que...")
   - Omitir sujeito ou objeto quando ficar natural
   - Usar intercalações para soar mais espontâneo

3. **Interjeições e marcadores de fala**
   - Usar "né", "então", "olha", "sabe" quando couber
   - Adicionar exclamações como "nossa", "que demais", "hum"
   - Usar "aliás", "na real", "sinceramente"

### Terceira passada: reforçar a sensação de diálogo (nível P2)
**Objetivo:** aumentar a interação e a sensação de conversa real.

**Elementos de interação:**
1. **Perguntas retóricas**
   - "Adivinha como foi o resultado?"
   - "Vocês já passaram por isso?"
   - "Parece simples, né?"

2. **Perguntas-resposta**
   - "Isso é difícil? Na verdade não é nada difícil."
   - "Você entendeu? Acho que já pegou o jeito."

3. **Chamar o público diretamente**
   - "Gente", "pessoal", "galera"
   - "Quero contar uma coisa para vocês..."
   - "Vocês precisam lembrar disso..."

### Quarta passada: adicionar cor emocional (ajuste fino)
**Objetivo:** aumentar a expressão de emoção e a marca pessoal.

**Elementos emocionais:**
1. **Palavras de emoção**
   - "isso é muito bom mesmo", "super útil"
   - "que incrível", "não acredito"
   - "fiquei meio decepcionado", "foi surpreendente"

2. **Fala em primeira pessoa**
   - "eu acho que", "na minha opinião", "para ser sincero"
   - "a minha experiência pessoal é..."
   - "o que mais me marcou foi..."

3. **Metáforas e personificação**
   - Usar comparações do dia a dia
   - Dar características humanas a conceitos abstratos
   - Tornar o abstrato mais concreto

## Exemplos de transformação

### Exemplo 1: apresentação de produto
**Original (escrito, formal):**
```
Este produto utiliza tecnologia avançada de inteligência artificial e oferece
soluções eficientes para o usuário. O produto possui as seguintes características:
operação simples, funcionalidade robusta e desempenho estável. O usuário pode
realizar funções complexas por meio de operações simples.
```

**Depois (falado):**
```
O produto que eu vou apresentar hoje me surpreendeu de verdade!
Ele usa a tecnologia de IA mais avançada que existe, mas é super simples de usar.
Sabe o que é mais incrível? Funções complicadas, você resolve com alguns cliques!
Simples de operar, poderoso e ainda estável — é praticamente um show de resultado!
```

### Exemplo 2: tutorial
**Original (escrito, formal):**
```
Primeiramente, é necessário realizar a preparação. Em seguida, executar as etapas
conforme indicado. Por fim, validar o resultado obtido. Este método é aplicável
à maioria dos cenários.
```

**Depois (falado):**
```
Bom, vamos começar!
Primeiro passo: a gente se prepara um pouco, isso é importante.
Depois, segue comigo passo a passo, é bem simples.
No final, a gente vê como ficou o resultado. Esse método funciona pra quase tudo!
```

### Exemplo 3: compartilhar uma opinião
**Original (escrito, formal):**
```
De acordo com minhas observações, esse fenômeno é recorrente. Considero que
resolver esse problema exige esforço em várias frentes. Portanto, devemos adotar
uma estratégia mais proativa.
```

**Depois (falado):**
```
Sinceramente, reparei que esse problema é mais comum do que parece.
Acho que para resolver isso não basta uma pessoa só fazer força.
Então, a gente precisa mudar de abordagem e ser mais proativo.
```

## Recomendações por tipo de vídeo

### 1. Vídeo educativo/divulgação de conhecimento
**Foco na fala:**
- Usar mais perguntas e interação
- Adicionar comparações do dia a dia
- Manter o profissionalismo somando proximidade

### 2. Vídeo de relato pessoal
**Foco na fala:**
- Reforçar sentimento e experiência pessoal
- Usar mais marcadores de fala e exclamações
- Aumentar o diálogo direto com quem assiste

### 3. Vídeo de tutorial/demonstração
**Foco na fala:**
- Deixar os passos bem claros
- Adicionar linguagem de incentivo e orientação
- Manter o ritmo leve

### 4. Vídeo de review/avaliação de produto
**Foco na fala:**
- Destacar a experiência real de uso
- Adicionar comparação e avaliação
- Manter objetividade ao mesmo tempo que expressa opinião

## Critérios de qualidade

### Fluência
- [ ] Lê-se sem travar
- [ ] O ritmo da fala é natural
- [ ] Sem frases longas e difíceis
- [ ] Variedade de estrutura de frase

### Naturalidade
- [ ] Parece conversa real
- [ ] Sem marcas de texto escrito
- [ ] Marcadores de fala usados com bom senso
- [ ] Expressão emocional genuína

### Proximidade
- [ ] Tem sensação de interação
- [ ] Tem toque pessoal
- [ ] Fácil de o público se identificar
- [ ] Fala com calor humano

## Cuidados especiais

### 1. Manter o sentido original
- Garantir que a informação central não se perca
- Dados e fatos importantes continuam precisos
- A relação lógica entre as ideias continua clara

### 2. Evitar exagerar na informalidade
- Não usar expressões descuidadas demais
- Manter um mínimo de norma da língua
- Evitar gírias de internet fora de contexto

### 3. Considerar o contexto de gravação
- Levar em conta o estilo geral do vídeo
- Adaptar ao nível de aceitação do público-alvo
- Manter a consistência do estilo pessoal de quem fala
