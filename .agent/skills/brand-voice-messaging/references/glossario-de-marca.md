# Glossário de Marca e Diretrizes de Tradução

**Versão:** 1.0.0  
**Módulo:** `brand-voice-messaging`  
**Crédito de Origem:** Conceitos de arquitetura de contexto e integridade terminológica adaptados a partir de `promovaweb/inboundfy` (licença AGPL-3.0), redigidos com estrutura e regras autorais exclusivas do ecossistema Super IA Projects `0 Mkt`.

---

## 1. Visão Geral e Princípio de Integridade Verbal

Uma marca forte constrói autoridade através da consistência estrita de sua linguagem. Variações arbitrárias na grafia de nomes próprios, metodologias internas ou traduções literais desajeitadas de termos técnicos consolidados enfraquecem a percepção de valor e geram ruído editorial.

O **Glossário de Marca** é a referência canônica obrigatória que governa a escrita de cada termo, sigla e conceito no âmbito da marca. Ele atua como um contrato terminológico: nenhum conteúdo é considerado aprovado ou pronto para veiculação enquanto contiver termos pendentes de validação ou grafias vetadas.

---

## 2. Estrutura Padrão do Glossário (Tabela em 4 Colunas)

Cada marca mantida em `_brands/<marca>/` deve conter o arquivo `glossario.md` estruturado segundo a seguinte matriz:

| Expressão Original | Escrita Oficial da Marca | Grafias Vetadas | Categoria & Regra de Tradução | Notas de Aplicação & Contexto |
|---|---|---|---|---|
| *Ex.: growth loops* | **Growth Loops** | *loops de crescimento, loop de growth, looping de crescimento* | **NÃO SE TRADUZ** (Conceito Técnico Consolidado) | Manter em inglês com maiúsculas iniciais quando referenciar o framework metodológico. |
| *Ex.: onboarding* | **onboarding** | *embarque de usuário, integração de cliente, ambientação* | **NÃO SE TRADUZ** (Termo Técnico do Setor) | Minúsculas no corpo do texto. Refere-se à ativação de novo cliente na plataforma. |
| *Ex.: actionable insights* | **insights acionáveis** | *percepções acionáveis, insights de ação* | **SE TRADUZ** (Expressão Descritiva) | Traduzir apenas o adjetivo; manter insight como empréstimo linguístico aceito. |

---

## 3. Matriz Binária: O Que Se Traduz vs. O Que Não Se Traduz

Os redatores e agentes de IA devem obedecer categoricamente à seguinte taxonomia:

### 3.1. Categorias que NUNCA Se Traduzem (Manter no Idioma Original)
1. **Nomes de Marcas, Produtos e Features:**  
   - Marcas próprias, submarcas, produtos do portfólio e nomes de módulos comerciais (ex.: *WaiMonitor, Plinq, PowerBI, Google Ads*).
2. **Termos Técnicos Consolidados de Mercado:**  
   - Expressões para as quais a tradução ao português soaria artificial, desconexa ou não reconhecida pela indústria (ex.: *churn, prompt, framework, benchmark, briefing, copy, landing page, cold email*).
3. **Siglas e Acrônimos Padronizados:**  
   - Métricas e conceitos de gestão e marketing internacionalmente aceitos (ex.: *ICP, CAC, LTV, ROAS, ROI, CTR, CPC, API, SLA, MQL, SQL*).
4. **Metodologias e Frameworks Proprietários:**  
   - Fórmulas, métodos registrados ou pilares cunhados pela própria empresa ou por autores de referência (ex.: *$100M Offers, Primal Branding, Jobs to be Done, Challenger Sale*).
5. **Variáveis Técnicas, Identificadores e Código:**  
   - Nomes de parâmetros, chaves, endpoints, funções ou variáveis de ambiente (ex.: `utm_source`, `payload`, `webhooks`).

### 3.2. Categorias que OBRIGATORIAMENTE Se Traduzem (Adaptação Fluida ao PT-BR)
1. **Adjetivos e Termos Conceituais Genéricos:**  
   - Ex.: em vez de *"seamless integration"*, utilize *"integração fluida"*; em vez de *"game-changer"*, utilize *"ponto de inflexão"* ou *"transformador"*.
2. **Chamadas para Ação (CTAs) em Contextos Não-Técnicos:**  
   - Ex.: em vez de *"Subscribe now"*, utilize *"Assine agora"* ou *"Inscreva-se"*.
3. **Explicações Didáticas de Processos:**  
   - A explicação conceitual de como um recurso funciona deve soar natural em português culto, evitando estrangeirismos preguiçosos onde houver termo nacional exato.

---

## 4. Regras Mandatórias de Operação

1. **Trava de Saída Editorial (Zero Termos Pendentes):**  
   Nenhum artefato textual pode avançar para o estado `aprovado` ou `agendado` contendo anotações do tipo `[termo a confirmar]`, grafias não homologadas no glossário ou divergências de capitalização.
2. **Atualização sob Demanda:**  
   Sempre que um novo produto for batizado, uma metodologia for criada ou surgir uma dúvida de grafia em sprint editorial, o `glossario.md` da marca deve ser atualizado imediatamente antes da publicação da peça.
3. **Prevalência sobre Dicionários Genéricos:**  
   A escrita registrada no `glossario.md` da marca se sobrepõe a qualquer norma externa de dicionários gerais, refletindo a voz oficial da empresa.

