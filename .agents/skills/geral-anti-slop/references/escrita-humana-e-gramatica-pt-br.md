# Escrita Humana e Gramática em Português do Brasil

Guia prático para estruturar textos com voz autêntica, ancoragem em fatos operacionais e observância rigorosa da norma culta em língua portuguesa. Complementa a skill `geral-anti-slop` e orienta revisores e redatores a construir peças substantivas, eliminando fórmulas artificiais sem cair em frieza burocrática.

> **Origem conceitual:** Conceitos de escrita orientada a fatos e revisão sistemática adaptados livremente a partir da arquitetura editorial de `promovaweb/inboundfy`. Redação autoral e alinhada às diretrizes do hub `0 Mkt`.

---

## 1. Anatomia do Parágrafo Humano (7 Elementos Fundamentais)

Textos gerados por modelos de linguagem tendem a flutuar em abstrações: descrevem "o quê" de modo vago e saltam direto para conclusões grandiosas. O parágrafo humano profissional ancora a narrativa em evidências verificáveis. Um parágrafo sólido não precisa conter todos os sete elementos em sequência linear rígida, mas constrói sua substância a partir deles:

1. **Contexto temporal e espacial definido:** Dia da semana, data, turno, sistema, ambiente ou local físico onde a ação se desenrola (ex.: *"Na manhã de terça-feira (14/05), durante a conciliação do lote das 9h..."*).
2. **Sujeito e agente ativo:** A pessoa, o time ou o componente que tomou a decisão ou sofreu o impacto (ex.: *"A equipe de cobrança..."*, *"O gateway de pagamento..."*).
3. **Fato observável ou incidente inicial:** O que realmente aconteceu, registrado em log, tela ou relato (ex.: *"devolveu status 502 por 18 minutos consecutivos"*).
4. **Fricção, atrito ou falha da primeira tentativa:** O obstáculo real ou o equívoco inicial que exigiu intervenção humana qualificada (ex.: *"A primeira tentativa de rodar o reprocessamento em lote sobrecarregou o pool de conexões com 400 acessos simultâneos"*).
5. **Decisão, ajuste ou mecanismo de correção:** O procedimento concreto adotado para conter ou resolver a fricção (ex.: *"Limitamos a vazão no `queue.py` para 25 disparos por segundo"*).
6. **Resultado aferido ou estado operacional:** O efeito mensurável ou a situação verificada após a mudança (ex.: *"A fila esvaziou em 12 minutos sem novas quedas de conexão"*).
7. **Próxima ação ou implicação lógica direta:** A recomendação prática, o runbook ou a diretriz derivada do ocorrido, sem clichês de resumo (ex.: *"Mantenha o monitoramento ativo e revise o timeout caso a latência supere 800ms"*).

---

## 2. Progressão Narrativa como Incidente Real

A marca registrada do texto artificial é a perfeição sem atrito: apresenta-se um problema hipotético e uma solução milagrosa imediata. Em operações reais, o valor do conteúdo nasce do atrito superado.

- **A falha da primeira tentativa:** Documentar o que não funcionou de início confere credibilidade instantânea. Mostra que o autor domina o terreno e não está repetindo teoria de manual.
- **Ressalvas e limites operacionais:** Assumir o que a solução resolve e o que ela ainda não resolve evita promessas infladas (*puffery*). Se um processo economizou tempo mas gerou retrabalho inicial de conferência, declare a conferência.
- **Não inventar dados ausentes:** Se o autor ou o rascunho de entrada não trouxe métricas concretas (ex.: porcentagens, tempos ou valores), o revisor jamais deve fabricar números fictícios. O procedimento correto é usar marcadores de checagem: `[a confirmar: tempo médio de resposta]` ou orientar o autor a inserir o dado apurado.

---

## 3. Sinais Humanos a Preservar e Regra de Contexto

Um erro comum em revisões automatizadas é a caça cega a palavras. O detector anti-slop não deve transformar o texto em uma cartilha engessada.

### A regra central contra a condenação isolada
> **Nenhuma palavra isolada constitui vício de estilo por si só.** O vício surge do papel sintático desnecessário, da repetição como muleta de ligação ou da ausência de substância factual no entorno.

### O que deve ser preservado:
1. **Termos técnicos legítimos do setor:** Palavras em inglês como *webhook*, *worker*, *deploy*, *pipeline*, *payload*, *churn*, *sprint*, *setup* ou *trade-off* são vocabulário padrão da profissão. Condenar esses termos ou tentar forçar traduções artificiais destrói o tom de autoridade técnica.
2. **Conectores causais legítimos:** A palavra *"Portanto"* é perfeitamente legítima quando fecha uma dedução lógica genuína ou introduz uma regra de ação operacional derivada de premissas demonstradas. Ela só se torna slop quando usada para repetir o que já foi dito ou para fingir profundidade em parágrafos vagos.
3. **Expressões idiomáticas autênticas e cadência oral:** Pausas naturais, períodos de comprimentos variados (frases de 7 palavras alternadas com frases de 22 palavras) e vocabulário espontâneo do mercado brasileiro devem ser protegidos contra a padronização asséptica.
4. **Números reais não redondos:** Horários exatos (`14h18`), percentuais quebrados (`7,3%`), volumes apurados (`142 chamados`) e datas no calendário indicam experiência empírica real.

---

## 4. Ângulo Próprio por Canal

Cada canal exige um enquadramento específico para que a peça não pareça um texto genérico transposto sem cuidado:

| Canal | Propósito Principal | Dinâmica do Parágrafo | O que eliminar imediatamente |
|---|---|---|---|
| **WhatsApp e Mensagens Diretas** | Resposta rápida, alinhamento ou orientação operacional pontual | Frases curtas, diretas ao ponto, sem formalismo burocrático | Fórmulas de saudação corporativa pesada, introduções reflexivas, parágrafos densos |
| **LinkedIn e Redes B2B** | Compartilhamento de aprendizado prático e autoridade técnica | Parágrafos de 2 a 4 frases, foco no atrito superado e no método aplicado | Frases isoladas com quebra de linha após cada ponto (*LinkedIn formatting bro*), aberturas com "Pare tudo o que está fazendo" |
| **Email Transacional e Operacional** | Ação requerida e clareza de instrução | Bloco informativo claro com sujeito e verbo ativos, seguido de instrução de ação | Abstrações sobre "sua jornada", adjetivação sobre "excelência no atendimento" |
| **Artigo de Blog e Base de Conhecimento** | Explicação aprofundada, conceituação e documentação | Parágrafos coesos e estruturados em 7 elementos, com exemplos de código ou processo | Fórmulas de encerramento do tipo "Em resumo, vimos que...", "No cenário dinâmico de hoje" |
| **Runbook e Documentação Interna** | Execução rápida sob pressão operacional | Instruções no modo imperativo ou declarativo direto, com parâmetros explícitos | Narrativas emotivas, justificativas filosóficas, jargões vagos |

---

## 5. Casos Práticos Antes e Depois em Português do Brasil

### Caso 1: B2B SaaS e Infraestrutura
- **Antes (Slop / IA):**  
  > "No ecossistema atual de tecnologia, garantir a alta disponibilidade é crucial para o sucesso de qualquer empresa. Além disso, nossa infraestrutura robusta desempenha um papel fundamental ao orquestrar microsserviços modernos, permitindo uma experiência transformadora e escalável. Portanto, adotar essa arquitetura inovadora representa um verdadeiro divisor de águas na eficiência operacional."
- **Depois (Humano e Específico):**  
  > "Na última sexta-feira (08/11), o pico de requisições no fechamento bancário elevou a latência da API de 120ms para 3,4s. A primeira medida de subir novas instâncias no Kubernetes não resolveu porque o gargalo estava no bloqueio de tabelas do PostgreSQL. Separamos as consultas de leitura da fila de conciliação criando uma réplica dedicada. Com a divisão, a API retornou ao patamar de 110ms mesmo durante as janelas de maior volume."

### Caso 2: Finanças e Cobrança
- **Antes (Slop / IA):**  
  > "É importante ressaltar que a automação dos fluxos de recebimento não é apenas sobre cobrar clientes — é sobre revolucionar a gestão financeira com inteligência e empatia. Ao implementar lembretes proativos e relatórios analíticos, sua operação alcança visibilidade, controle e previsibilidade. Isso garante uma redução drástica do atrito e maximiza o fluxo de caixa."
- **Depois (Humano e Específico):**  
  > "Substituímos o envio manual de boletos em PDF por notificações automáticas via WhatsApp enviadas 2 dias antes do vencimento. No primeiro teste, clientes reclamaram da falta do código de barras digitável no corpo da mensagem. Corrigimos o payload para exibir a linha digitável e a chave Pix antes do link. Em três semanas, o índice de pagamento na data de vencimento subiu de 61% para 74% na base de planos trimestrais."

### Caso 3: Recursos Humanos e Operações Internas
- **Antes (Slop / IA):**  
  > "No contexto de trabalho remoto contemporâneo, alinhar expectativas com a equipe é essencial para promover o engajamento contínuo. Vale destacar que ferramentas colaborativas servem como um alicerce poderoso para criar conexões significativas entre colaboradores. Dessa forma, uma liderança estratégica constrói pontes e potencializa o capital humano em prol dos objetivos organizacionais."
- **Depois (Humano e Específico):**  
  > "Depois de migrar para o modelo remoto, percebemos que o alinhamento diário de 30 minutos consumia tempo útil da engenharia sem destravar bloqueios. Reduzimos a reunião para um formulário assíncrono no Slack com três perguntas: o que foi concluído, o que está travado e quem precisa de ajuda hoje. Os impasses urgentes passaram a ser tratados em chamadas de 10 minutos apenas entre os envolvidos."

### Caso 4: E-commerce e Logística
- **Antes (Slop / IA):**  
  > "Uma logística ágil e eficiente é indispensável para proporcionar uma jornada de compra memorável ao consumidor exigente. Em um mercado hipercompetitivo, atender às expectativas de entrega não é um diferencial, mas sim uma obrigação fundamental. Por isso, investir em rastreamento inteligente fortalece o vínculo de confiança e fideliza sua base de clientes."
- **Depois (Humano e Específico):**  
  > "Durante a campanha de setembro, transportadoras parceiras atrasaram 14% das entregas na região Sul devido a bloqueios rodoviários temporários. Em vez de aguardar o contato de compradores insatisfeitos no suporte, enviamos um aviso preventivo por SMS informando o motivo da retenção e a nova previsão estimada. O volume de chamados de 'onde está meu pedido' caiu pela metade em comparação com o evento anterior."

---

## 6. Checklist de Norma Culta em Língua Portuguesa

A credibilidade do texto desmorona quando o leitor encontra deslizes gramaticais básicos. Este checklist cobre os pontos mais recorrentes em conteúdos técnicos e comerciais no Brasil:

### 6.1. Pontuação e Uso da Vírgula
- [ ] **Separação indevida entre sujeito e verbo:** Nunca coloque vírgula simples entre o núcleo/sintagma do sujeito e seu predicado, independentemente da extensão da frase.
  - *Incorreto:* "A equipe responsável pela integração com o banco, identificou o erro."
  - *Correto:* "A equipe responsável pela integração com o banco identificou o erro."
- [ ] **Separação indevida entre verbo e complemento:** Nunca isole o objeto direto ou indireto com vírgula do seu respectivo verbo.
  - *Incorreto:* "O sistema gerou, um alerta de erro crítico na console."
  - *Correto:* "O sistema gerou um alerta de erro crítico na console."
- [ ] **Adjuntos adverbiais deslocados:** Use vírgula quando a locução adverbial estiver antecipada ou intercalada, sobretudo se tiver mais de três palavras.
  - *Recomendado:* "Na manhã da última terça-feira, a equipe liberou o patch."
- [ ] **Vírgula antes do conector "e":** Obrigatória quando as orações coordenadas possuírem sujeitos gramaticais diferentes; facultativa para conferir ênfase estilística; proibida quando o sujeito for o mesmo e a ação for contínua.
  - *Correto:* "O gateway recusou o token, e a aplicação redirecionou o usuário para o login." (Sujeitos diferentes: *o gateway* / *a aplicação*).

### 6.2. Emprego do Sinal Indicativo de Crase
- [ ] **Proibição antes de verbos:** Nunca use crase diante de formas infinitivas.
  - *Incorreto:* "à partir de", "disposto à colaborar", "valores à receber".
  - *Correto:* "a partir de", "disposto a colaborar", "valores a receber".
- [ ] **Proibição antes de palavras masculinas:**
  - *Incorreto:* "pagamento à prazo", "envio à domicílio".
  - *Correto:* "pagamento a prazo", "envio a domicílio".
- [ ] **Proibição antes de pronomes indefinidos, demonstrativos e de tratamento:**
  - *Incorreto:* "aviso à todos", "solicitação enviada à Vossa Senhoria".
  - *Correto:* "aviso a todos", "solicitação enviada a Vossa Senhoria".
- [ ] **Obrigatoriedade em locuções femininas:** Use crase em locuções prepositivas, conjuntivas e adverbiais com núcleo feminino.
  - *Correto:* "às 14h", "à medida que", "à disposição", "à vista", "à frente de".
- [ ] **Casos facultativos:** Antes de pronomes possessivos femininos no singular seguidos de substantivo (*"enviamos a/à sua equipe"*) e antes de nomes próprios femininos de pessoas (*"notificamos a/à Maria"*).

### 6.3. Concordância Verbal e Nominal
- [ ] **Verbo "haver" impessoal:** No sentido de existir, acontecer ou marcar tempo decorrido, o verbo `haver` não tem sujeito e fica obrigatoriamente na terceira pessoa do singular.
  - *Incorreto:* "Haviam três inconsistências no relatório.", "Devem haver soluções melhores."
  - *Correto:* "Havia três inconsistências no relatório.", "Deve haver soluções melhores." (ou usar o verbo `existir`: *"Existiam três inconsistências"*).
- [ ] **Verbo "fazer" indicando tempo decorrido:** Também é impessoal e não flexiona para o plural.
  - *Incorreto:* "Fazem dois meses que o recurso foi lançado."
  - *Correto:* "Faz dois meses que o recurso foi lançado."
- [ ] **Expressões partitivas seguidas de plural:** Com expressões como *"a maioria de"*, *"a maior parte de"*, *"grande parte dos"*, a concordância é facultativa: pode concordar com o coletivo (singular) ou com o termo partitivo plural.
  - *Correto:* "A maior parte dos clientes aprovou o novo painel." (foco no bloco).
  - *Correto:* "A maior parte dos clientes aprovaram o novo painel." (foco nos indivíduos).
- [ ] **Concordância com porcentagens e valores:**
  - Sem especificador: concorda com o numeral (*"1% confirmou"*, *"18% desistiram"*).
  - Com substantivo especificador: a concordância pode se dar tanto com o numeral quanto com o substantivo (*"1% dos clientes desistiu/desistiram"*).

### 6.4. Regência Verbal Crítica em Redação Técnica e de Negócios
- [ ] **Implicar:** No sentido de acarretar, causar ou ter como consequência direta, é transitivo direto (não rege a preposição `em`).
  - *Incorreto:* "Essa configuração implica em lentidão no processamento."
  - *Correto:* "Essa configuração implica lentidão no processamento." (ou reescrever ativamente: *"Essa configuração atrasa o processamento"*).
- [ ] **Assistir:** No sentido de ver, presenciar ou monitorar ativamente uma ação, rege a preposição `a`. No sentido de dar suporte ou prestar socorro, rege sem preposição.
  - *Uso correto:* "O técnico assistiu ao webinar." / "O monitor assiste à base em tempo real." / "O atendente assiste o cliente com presteza."
  - *Dica técnica:* Em redação de tecnologia, prefira verbos diretos e inequívocos como `monitorar`, `consultar`, `inspecionar` ou `atender`.
- [ ] **Visar:** No sentido de ter como meta ou objetivo, rege a preposição `a`.
  - *Correto:* "A melhoria visa ao aprimoramento do fluxo." / "A melhoria visa otimizar o fluxo." (diante de verbo infinitivo dispensa-se a preposição).
- [ ] **Acessar e Informar:** O verbo `acessar` é transitivo direto (não use "acessar ao painel"). O verbo `informar` rege algo a alguém ou alguém de algo.
  - *Correto:* "Acesse o painel administrativo."
  - *Correto:* "Informamos o cliente sobre a atualização." / "Informamos ao cliente o status do chamado."
- [ ] **Chegar e Ir:** Verbos de movimento regem a preposição `a`, nunca `em`.
  - *Incorreto:* "Chegamos no resultado desejado."
  - *Correto:* "Chegamos ao resultado desejado."

### 6.5. Pronomes Relativos e Conectores
- [ ] **Uso do pronome "onde":** Reservado estritamente para referenciar locais físicos concretos ou espaços geográficos bem determinados.
  - *Incorreto:* "Criamos um fluxo onde o cliente recebe o alerta.", "Apresentamos uma proposta onde todos ganham."
  - *Correto:* "Criamos um fluxo em que o cliente recebe o alerta.", "Apresentamos uma proposta na qual todos ganham."
- [ ] **Colocação pronominal básica:** Nunca inicie períodos com pronome oblíquo átono na norma culta padrão. Palavras de sentido negativo (*não*, *nunca*, *jamais*), pronomes relativos (*que*, *quem*) e conjunções subordinativas atraem a próclise.
  - *Incorreto:* "Me avise quando concluir.", "Não entregou-se o pacote."
  - *Correto:* "Avise-me quando concluir." / "Você pode me avisar quando concluir." / "Não se entregou o pacote."
