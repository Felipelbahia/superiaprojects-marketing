# Extração, construção e auditoria de voz

Guia único para três trabalhos sobre a mesma coisa, a voz: **extrair** a voz de textos que já existem, **construir** uma voz do zero e **auditar** se um texto soa como a marca. Serve à etapa 4 do `brand-builder` (a saída alimenta o `brand-voice.md`) e a qualquer pessoa que precise de um "guia de voz" para treinar uma IA, orientar um redator ou alinhar um time.

> Texto genérico converte pior que texto com voz própria. Não porque as palavras mudam, mas porque o leitor sente que ouve uma pessoa, não um time de marketing. A correção de uma IA que escreve igual a todas não é um prompt melhor: é ensiná-la a comunicar como a marca comunica.

**Origem deste arquivo (fusão feita no E5, 2026-10-20; direito de uso confirmado pelo usuário):** `brand-voice-extractor` e `voice-extractor` (Brian Wagner) e `brand-voice-learner` (ClawFu, baseado em pesquisa de voz do NN/g). Os dois últimos estão arquivados em `.agent/skills/_arquivo/mescladas/e5-brand/`. Cada seção abaixo diz de onde veio.

## Sumário

1. Escolher o modo
2. Portões de contexto
3. Modo Extrair (fases 1 a 7 e modo rápido)
4. O que analisar: dimensões, padrões linguísticos, estrutura
5. Modo Construir (15 perguntas)
6. Modo Auditar (uma frase contra a voz)
7. Formatos de saída (perfil de voz, guia de voz pessoal e guia completo com exemplos)
8. Exemplo completo
9. Régua de qualidade e autocrítica
10. Como isto se liga ao resto

---

## 1. Escolher o modo

> "Existe conteúdo que já soa como você quer soar?" Sim: **Extrair**. Não ou não sei: **Construir**. Já existe uma voz definida e a pergunta é se um texto a respeita: **Auditar**.

| Modo | Quando | Entrada | Saída |
|---|---|---|---|
| **Extrair** | A marca ou a pessoa já tem textos que soam certo (página Sobre, e-mails, posts, transcrições) | 3 a 5 textos de que se orgulha (mínimo) | Perfil de voz |
| **Construir** | Marca nova, conteúdo genérico, ou reposicionamento de tom | Respostas a 15 perguntas | Perfil de voz |
| **Auditar** | Voz já definida, texto novo a conferir | Perfil ou `brand-voice.md` + o texto | Veredito, problemas, reescrita |

Vindo de `brand-voice-extractor` (dois modos) e `brand-voice-learner` (auditoria).

## 2. Portões de contexto

Antes de extrair, reunir (vindo de `voice-extractor`):

- [ ] **Amostras de escrita**: mínimo de 3 amostras ou 500 palavras no total.
- [ ] **Finalidade do guia**: treinar IA? orientar redator (ghostwriter)? alinhar o time?
- [ ] **Zonas de confiança**: assuntos em que a pessoa quer soar mais ou menos autoridade.
- [ ] **Antipadrões conhecidos**: palavras e frases que ela já sabe que quer evitar.

**Prioridade das fontes (da mais autêntica para a menos):**
1. Mensagem casual de Slack ou e-mail (voz crua, sem edição)
2. Transcrição de podcast ou de chamada
3. Posts ou artigos de LinkedIn
4. Texto de site (costuma ser editado, menos autêntico)

**Portão de amostra mínima.** Com menos de 500 palavras, parar e dizer: "Essas amostras são curtas demais para extrair padrões confiáveis. Adicione 2 ou 3 mais; e-mails, mensagens e transcrições funcionam melhor. Quanto mais bagunçado e casual, melhor." Não tentar a extração completa com menos disso; oferecer o modo rápido.

**Para um guia de voz de marca (não de pessoa)**, o ideal é de 10 a 15 peças, de contextos variados e incluindo os melhores exemplos (vindo de `brand-voice-learner`):

| Fonte | Mostra |
|---|---|
| Texto do site | A voz central |
| Posts de blog | A voz estendida |
| Redes sociais | A variação casual |
| Campanhas de e-mail | A comunicação direta |
| Interface do produto | A voz funcional |
| Atendimento ao cliente | A voz empática |

## 3. Modo Extrair

Sete fases (vindo de `voice-extractor`). As fases 6 e 7 são obrigatórias.

### Fase 1: avaliar a qualidade da amostra

1. **Autenticidade:** vêm de contexto editado (site, imprensa) ou cru (Slack, e-mail)? Mais polimento, menos voz autêntica.
2. **Variedade:** cobrem contextos diferentes (profissional, casual, educativo)? Amostra de um contexto só gera guia de uma dimensão só.
3. **Exclusões:** marcar o que NÃO é a voz autêntica: tiques de formatação de plataforma (quebras de linha do LinkedIn, brevidade forçada do Twitter), erros de digitação e autocorreção, frases emprestadas (citações, retweets), escrita formal demais (documento jurídico, comunicado).
4. **Tamanho:** há material para o modo completo ou é caso de modo rápido?

Relatar assim: "Tenho [X amostras / Y palavras]. Qualidade: [alta/média, por quê]. Vou usar o modo [completo/rápido]. Excluindo: [padrões e motivo]."

### Fase 2: energia central

Identificar o modo fundamental de comunicar:

- **Papel:** Professor (explica de forma sistemática), Desafiador (questiona premissas), Líder de torcida (dá confiança e ritmo), Direto ao ponto (corta a enrolação).
- **Energia padrão:** autoridade calma ("É isto que funciona."), entusiasmo alto ("Isto é empolgante, deixa eu mostrar."), confiança contida ("Já vi isso cem vezes.").
- **Temas recorrentes:** os assuntos que aparecem sem ninguém pedir; são aquilo que a pessoa realmente valoriza.

### Fase 3: extração sistemática de frases

Varrer todas as amostras e extrair, **citando o trecho exato**:

- **Transições** (como muda de assunto): "O ponto é o seguinte...", "O que aprendi...", "Deixa eu dizer de outro jeito..."
- **Ênfases** (como crava um ponto): "A realidade é...", "Esta é a parte que a maioria perde...", "O problema de verdade é..."
- **Fechamentos** (como encerra): "É esse o movimento.", "Comece por aí.", "Você consegue."

### Fase 4: mapa das zonas de confiança

| Zona | Descrição | Marcas de linguagem |
|---|---|---|
| Autoridade plena | Assuntos em que é especialista | Sem rodeio, afirmações definitivas, "o que funciona é..." |
| Perspectiva conquistada | Tem experiência, não domínio | "Na minha experiência...", "O que encontrei..." |
| Exploração ativa | Está aprendendo agora | "Estou testando isto...", "O que estou vendo..." |

Ligar as áreas de expertise declaradas a cada zona. Essa calibração separa uma voz real de uma voz de uma dimensão só.

### Fase 5: documentar antipadrões

Extrair o que a pessoa NUNCA diria: palavras que soariam falsas, frases que a fariam se encolher, tons que evita, jargão do setor que detesta. Sempre que der, com evidência: "Você não usou [palavra] em nenhuma de [X] amostras; ela não combina com a sua voz."

### Fase 6: teste de validação (obrigatório)

Com o perfil completo, gerar 2 frases sobre o mesmo assunto:

- **Versão A** (voz extraída): "[frase na voz da pessoa]"
- **Versão B** (voz errada, em contraste): "[mesmo conteúdo, outra voz; mostra o que evitar]"

Perguntar: "A versão A soa como você quando não está pensando demais? O que está estranho?" A validação pega erro de extração antes de o guia entrar em uso.

### Fase 7: autocrítica (obrigatório)

Depois de gerar o guia, conferir:

- [ ] As frases extraídas estão mesmo nas amostras, ou eu as inferi?
- [ ] A lista de antipadrões tem palavras e frases específicas, ou só categorias vagas?
- [ ] As frases do teste mostram diferença real entre dentro e fora da voz?
- [ ] As zonas de confiança nomeiam assuntos, ou são genéricas?
- [ ] Um redator conseguiria usar o guia sem fazer perguntas?

Registrar o que faltar: "A seção de antipadrões tem só 2 itens; não basta para um guia utilizável. Preciso de mais amostras ou de informação direta do usuário."

### Modo rápido (`--quick`)

Para amostra magra (300 a 500 palavras) ou pouco tempo: ler 3 amostras rápido; tirar 10 frases típicas; anotar 3 coisas que a pessoa nunca diria; escrever 1 frase sobre a energia dela. **Saída:** guia mínimo viável.

| | Rápido | Completo |
|---|---|---|
| Frases | cerca de 10 | perfil completo |
| Antipadrões | 3 | com evidência |
| Energia | 1 frase | calibração por zona, frases de teste validadas, exemplos com fonte |

## 4. O que analisar

### Dimensões de voz (vindo de `brand-voice-extractor` e `brand-voice-learner`)

| Dimensão | Espectro |
|---|---|
| Formalidade | Casual ←→ Formal |
| Personalidade | Sério ←→ Brincalhão |
| Franqueza | Indireto ←→ Direto |
| Entusiasmo | Reservado ←→ Entusiasmado |
| Técnico | Simples ←→ Técnico |
| Calor | Distante ←→ Caloroso |
| Ousadia | Reservado ←→ Ousado |
| Intimidade | Distante ←→ Íntimo (eu/você ou nós/eles?) |

Para o `brand-voice.md`, **converter para os 5 eixos 1 a 5** da skill `brand-voice-messaging` e registrar o número; é ele que permite checar consistência depois.

### Padrões a observar

**Tom:** contrações? fragmentos? gíria? humor ou gravidade? afirmações fortes ou ressalvas?
**Vocabulário:** nível de jargão (pesado, traduzido ou leve); palavras e frases típicas; palavras que a pessoa parece evitar; vocabulário do dia a dia ou formal.
**Ritmo:** tamanho médio de frase e de parágrafo; mistura de curto e longo; uso de fragmentos; frequência de listas.
**Estrutura:** como abre (história, pergunta, afirmação forte); como faz a transição entre ideias; como fecha (CTA, resumo, ponto aberto); uso de títulos, formatação e respiro.
**Sinais de personalidade:** autoironia ou confiança? professor ou par? polido ou cru? otimista ou realista?

### Elementos linguísticos (vindo de `brand-voice-learner`)

| Elemento | O que identificar |
|---|---|
| Tamanho da frase | Curta, média, longa |
| Escolha de palavras | Comum, especializada, de marca |
| Contrações | Usa, evita, mistura |
| Voz ativa ou passiva | Preferência |
| Pronomes | Padrão nós/você/eles |
| Pontuação | Exclamações, reticências, travessão |

## 5. Modo Construir

Fazer de 10 a 15 perguntas, em rodadas de 3 a 5 (não despejar tudo de uma vez; ver `../../brand-builder/question-formats.md`). Vindo de `brand-voice-extractor`.

**Identidade (quem você é)**
1. Quais 3 a 5 palavras descrevem sua personalidade?
2. Pelo que você se posiciona? Qual a sua crença central sobre o setor?
3. Qual a sua trajetória? O que moldou o seu jeito de ver as coisas?
4. O que realmente diferencia você de outros no seu espaço?

**Público (com quem você fala)**
5. Com quem você fala? (Específico; não "empreendedores".)
6. Que tom ressoa com essa pessoa? A que ela reage?
7. O que a faria confiar em você? O que a afastaria?

**Posicionamento (como você aparece)**
8. Você é o especialista, o par, o rebelde, o guia ou o de dentro?
9. Onde fica entre acessível e exclusivo?
10. Onde fica entre próximo e autoritário?

**Aspiração (como quer soar)**
11. Cite 2 ou 3 pessoas ou marcas cuja voz você admira. O que, especificamente?
12. Como você NÃO quer soar?
13. Há palavras ou frases típicas que parecem "você"?
14. Há palavras que você odeia ou quer evitar?
15. O que acha de humor, palavrão e opiniões polêmicas?

Dentro do `brand-builder`, as respostas já dadas nas etapas 1 a 3 pré-preenchem várias delas (ver `derivacao.md`); perguntar só o que falta.

## 6. Modo Auditar

Vindo de `brand-voice-learner`. Entrada: a voz definida (perfil, ou `brand-voice.md` da marca) e o texto a conferir.

1. **Veredito:** combina ou não combina.
2. **Problemas encontrados**, em tabela:

| Problema | Trecho | Deveria ser |
|---|---|---|
| Formal demais | "Temos o prazer de informar" | "Boa notícia!" |
| Voz passiva | "foi processado" | "Nós processamos" |
| Fala corporativa | "o resultado desejado" | "o que você queria" |
| Estrutura rígida | Frase longa e completa | Mais curta e direta |

3. **Reescrita:** versão na voz da marca e, se pedir, uma versão ainda mais casual.
4. **O que deu errado:** explicar em uma frase por que soa como resposta automática corporativa (sem contração, voz passiva, frase formal, sem personalidade).

Pedidos de acompanhamento úteis: "reescreva isto na voz da marca", "crie variações por canal", "audite estas amostras quanto à consistência", "acrescente isto ao dicionário de palavras e frases".

## 7. Formatos de saída

### 7.1 Perfil de voz (marca ou pessoa)

Vindo de `brand-voice-extractor`.

```
# Perfil de voz - [Nome]

## Resumo da voz
[2 a 3 frases: como é ENCONTRAR essa voz?]

## Traços centrais de personalidade
- **[Traço]:** [o que significa na prática]
- **[Traço]:** [o que significa na prática]
- **[Traço]:** [o que significa na prática]

## Espectro de tom
| Dimensão | Posição | Notas |
|---|---|---|
| Formal ↔ Casual | | |
| Sério ↔ Brincalhão | | |
| Reservado ↔ Ousado | | |
| Simples ↔ Sofisticado | | |
| Caloroso ↔ Direto | | |

## Vocabulário
USE: [palavras, frases, aberturas típicas]
EVITE: [palavras, fala corporativa, frases com cara de IA]
Nível de jargão: [pesado / leve / traduzido]

## Ritmo e estrutura
Frases / Parágrafos / Aberturas típicas / Formatação

## Exemplos de frase
No tom: [3 exemplos]
Fora do tom: [3 exemplos + por que errado]

## Faça e não faça
FAÇA: [3 a 5 regras]
NÃO FAÇA: [3 a 5 regras]
```

### 7.2 Guia de voz pessoal (mais forte em evidência)

Vindo de `voice-extractor`. Usar quando a voz é de uma pessoa (fundador, porta-voz, ghostwriter).

```
## Guia de voz: [Nome] - [Data]

### Avaliação das amostras
Amostras (quantidade e tipos) / Total de palavras / Qualidade / Modo / Excluído e por quê

### Energia central
Papel / Energia padrão / Temas recorrentes

### Frases típicas
Transições: "[frase]" (fonte: [e-mail/post])
Ênfases: "[frase]" (fonte)
Fechamentos: "[frase]"

### Calibração de confiança
Autoridade plena (sem rodeio): assuntos + "soa assim: [frase]"
Perspectiva conquistada: assuntos + frase
Exploração ativa: assuntos + frase

### Antipadrões (nunca usar)
- [Palavra/frase]: por quê (evidência nas amostras)

### Teste de validação
Soa como você: "[Versão A]"
Não soa como você: "[Versão B]"

### Notas de autocrítica
[Lacunas e o que validar com o usuário]

### Como usar
Para IA: colar o guia no prompt de sistema.
Para ghostwriter: entregar no dia 1; reduz ciclos de revisão.
Para o time: é a referência do que é "na marca".
```

### 7.3 Guia completo com princípios e exemplos

Vindo de `brand-voice-learner`. Estrutura de um guia de marca: (1) resumo da voz, (2) dimensões com nota, (3) 3 a 5 princípios com exemplo certo e errado, (4) padrões linguísticos, (5) faça e não faça, (6) guia de escolha de palavras (em vez de X use Y), (7) frases típicas e quando usar, (8) variação por canal, (9) checklist de publicação.

**Checklist de publicação (modelo):**
- [ ] Você diria isto a um amigo?
- [ ] Há palavras de fala corporativa?
- [ ] Dá para encurtar?
- [ ] O ponto principal está claro?
- [ ] Soa como nós e não como um concorrente?
- [ ] Faria sentido sem contexto?

**Variação por canal (modelo):** site (voz central, a mais polida), blog (mais conversacional, opinião bem-vinda), redes (a mais curta e direta, mais humor), e-mail (amigável e orientado à ação), atendimento (mais calor e paciência, menos atitude).

## 8. Exemplo completo

Vindo de `brand-voice-learner` (adaptado ao português).

**Entrada:** quatro amostras de uma marca de software.
- Site: "Construímos ferramentas que funcionam de verdade. Sem enrolação, sem complicação: só um software que ajuda você a fazer as coisas."
- Blog: "O ponto sobre apps de produtividade é este: a maioria complica a sua vida em vez de facilitar. Achamos isso ao contrário."
- E-mail: "Oi! Seu teste está quase no fim. Antes de ir, queremos ter certeza de que você viu tudo o que o [Produto] faz."
- Social: "Segunda é difícil. O seu software não devia ser. ☕"

**Saída (resumida):**
- **Caráter:** confiante, casual, anti-corporativo. Soa como um amigo esperto e direto, que se irrita com as mesmas coisas que o cliente e não tem medo de chamar conversa fiada pelo nome.
- **Dimensões (1 a 10):** formalidade 3, personalidade brincalhona 7, franqueza 9, entusiasmo 6, técnico 4, calor 7.
- **Princípios:** (1) Diga direto: sem fala corporativa. Certo "Construímos ferramentas que funcionam"; errado "Alavancamos soluções de ponta para otimizar...". (2) Fique do lado deles: aliado contra a frustração. (3) Seja humano: contrações, linguagem casual. (4) Confiante sem arrogância: opinião clara, sem ironizar os outros.
- **Padrões:** frases curtas a médias (8 a 15 palavras), contrações sempre, muito "nós/você", voz ativa, travessão ocasional, emoji raro e relevante.
- **Faça:** contrações; abrir com "O ponto é"; "de verdade" para ênfase; citar frustração compartilhada; parágrafos de 2 a 3 frases; segunda pessoa.
- **Não faça:** "alavancar", "otimizar", "sinergia"; "temos o prazer de anunciar"; voz passiva; ressalvas ("talvez, quem sabe"); frases longas e complexas; exclamação em excesso.
- **Palavras:** em vez de "utilizar", "usar"; "soluções" vira "ferramentas"; "empoderar" vira "ajudar"; "perfeito" ("seamless") vira "fácil"; "de ponta" vira "novo". Mostrar, não dizer "o melhor da categoria".
- **Canais:** site polido mas casual; blog mais exploratório; redes mais curtas e com humor; e-mail amigável com CTA claro; atendimento mais caloroso.

**Auditoria do exemplo:** "Temos o prazer de informar que sua solicitação foi processada e o resultado desejado foi alcançado." Veredito: não combina (formal, passiva, corporativa). Reescrita: "Boa notícia! Cuidamos do seu pedido; está tudo certo." Versão mais casual: "Pronto! Seu pedido passou. Pode seguir."

## 9. Régua de qualidade e autocrítica

Um bom perfil passa neste teste (vindo de `brand-voice-extractor`):

- **Reconhecível:** alguém identificaria o conteúdo como "seu" sem assinatura?
- **Acionável:** um redator (humano ou IA) produziria texto na marca só com este perfil?
- **Diferenciado:** soa diferente dos concorrentes?
- **Autêntico:** parece verdadeiro para quem é?
- **Consistente:** vale para vários formatos (social, e-mail, texto longo)?

Se alguma resposta é não, falta especificidade. Rodar também a autocrítica da fase 7.

**Limites do método** (vindo de `brand-voice-learner`): ele analisa o que existe; não cria a estratégia da marca, não acessa todo o conteúdo e não substitui o julgamento de marca. Quem decide a evolução da voz, a aprovação do guia e as exceções é o usuário.

## 10. Como isto se liga ao resto

- **Salvar onde:** dentro do `brand-builder`, a saída vira o `brand-voice.md` da marca, em `_brands/<marca>/` (nunca em `docs/brand/`). Fora dele, em um arquivo de perfil de voz acessível.
- **Antes de produzir:** rodar a extração primeiro, salvar o perfil e referenciá-lo em toda tarefa de conteúdo.
- **Usar o perfil em:** `copy-conversao` (landing e textos de venda), `conteudo-reaproveitamento` (adaptar para outros canais), `email-copy` e `email-automacao` (sequências), `conteudo-estrategia` (isca digital e pilares).
- **Revisão de consistência depois:** agente `brand-guardiao-de-voz`.
- **Texto com cara de IA:** `geral-anti-slop`.
- **Voz ao escrever com IA** (rascunho primeiro, as 3 perguntas do leitor): `brand-voice.md` desta mesma pasta de referências.
- **Exemplo de resultado:** `sample-output-brand-voice.md`.
