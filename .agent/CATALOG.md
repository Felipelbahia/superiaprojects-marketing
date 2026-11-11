# 0 Mkt — Catálogo Integrado de Marketing, Growth e Vendas

> Catálogo completo de Marketing integrado à base global de Engenharia 0 Padrões

**Total Geral:** `695` recursos | **Skills:** `307` | **Workflows:** `225` | **Agentes:** `163`
**Fontes Integradas:** `0 Mkt` (247) · `0 Padrões` (448)

---

## ⭐ Recursos Fundamentais do Kit (Regra 4b & Metodologia VibeCoding)

Estes recursos regem os processos de desenvolvimento, resolução de skills e governança de qualidade:

| Recurso | Tipo | Origem | Papel / O que faz | Link Direto |
| :--- | :--- | :--- | :--- | :--- |
| **`execution-loop`** | `Skill` | `0 Padrões` | Ciclo Espec → Plan → Execução → QA (nota 0-10) → Debug para builds e mudanças significativas. | [Acessar](#execution-loop) |
| **`skill-resolver`** | `Skill` | `0 Padrões` | Procedimento inteligente de busca e resolução de skills no projeto local, 0 Padrões e 0 Mkt. | [Acessar](#skill-resolver) |
| **`spec-writing`** | `Skill` | `0 Padrões` | Criação de especificação escrita estruturada antes do início do planejamento ou código. | [Acessar](#spec-writing) |
| **`session-handoff`** | `Skill` | `0 Padrões` | Documentação do trabalho da sessão para continuidade fluida em sessões futuras. | [Acessar](#session-handoff) |
| **`writing-skills`** | `Skill` | `0 Padrões` | Criação e edição de qualquer skill aplicando TDD a documentação e symlinks. | [Acessar](#writing-skills) |
| **`clean-code`** | `Skill` | `0 Padrões` | Diretrizes obrigatórias de código limpo, sem over-engineering e com testes. | [Acessar](#clean-code) |
| **`project-initializer`** | `Skill` | `0 Padrões` | Fluxo de 5 fases para inicialização de projetos do zero com paridade dual. | [Acessar](#project-initializer) |
| **`project-defines`** | `Skill` | `0 Padrões` | Governança documental de projetos governados por pasta _projectdefines/. | [Acessar](#project-defines) |

---

## 📌 Sumário de Categorias

- [AI, Data & ML](#ai-data--ml) (`10` recursos)
  - [Engenharia de Prompts & Avaliação de LLMs](#engenharia-de-prompts--avaliação-de-llms) (`4`)
  - [Modelos de IA & Machine Learning](#modelos-de-ia--machine-learning) (`4`)
  - [Pipelines de Dados & Transformação](#pipelines-de-dados--transformação) (`2`)
- [Arquitetura de Software & Engenharia](#arquitetura-de-software--engenharia) (`42` recursos)
  - [Padrões Arquiteturais & Boas Práticas](#padrões-arquiteturais--boas-práticas) (`42`)
- [Backend & APIs](#backend--apis) (`20` recursos)
  - [Design & Integração de APIs (REST / GraphQL)](#design--integração-de-apis-rest--graphql) (`11`)
  - [Node.js, Go & Microsserviços](#nodejs-go--microsserviços) (`2`)
  - [Python & Backends de Alta Performance](#python--backends-de-alta-performance) (`5`)
  - [Serviços de Autenticação & Pagamentos](#serviços-de-autenticação--pagamentos) (`2`)
- [Database & Storage](#database--storage) (`6` recursos)
  - [Bancos Relacionais (PostgreSQL & SQL)](#bancos-relacionais-postgresql--sql) (`3`)
  - [Modelagem & Migrações de Banco](#modelagem--migrações-de-banco) (`3`)
- [DevOps & Cloud Infra](#devops--cloud-infra) (`65` recursos)
  - [Infraestrutura como Código (Terraform / Cloud)](#infraestrutura-como-código-terraform--cloud) (`3`)
  - [Orquestração Kubernetes & Contêineres](#orquestração-kubernetes--contêineres) (`2`)
  - [Pipelines de CI/CD & Deploy Contínuo](#pipelines-de-cicd--deploy-contínuo) (`60`)
- [Frontend & UI/UX](#frontend--uiux) (`212` recursos)
  - [Acessibilidade Web (A11y & WCAG)](#acessibilidade-web-a11y--wcag) (`4`)
  - [Componentes de Interface & Interação](#componentes-de-interface--interação) (`186`)
  - [Design Systems & Estilização Moderna](#design-systems--estilização-moderna) (`10`)
  - [Frameworks Web Modernos (React & Next.js)](#frameworks-web-modernos-react--nextjs) (`12`)
- [Gestão de Produtos e Projetos](#gestão-de-produtos-e-projetos) (`16` recursos)
  - [Conductor & Gestão de Tracks](#conductor--gestão-de-tracks) (`2`)
  - [Estratégia & Especificação de Produto (PRD)](#estratégia--especificação-de-produto-prd) (`3`)
  - [Operações Ágeis & Coordenação de Equipe](#operações-ágeis--coordenação-de-equipe) (`4`)
  - [Planejamento de Projetos & Sprints](#planejamento-de-projetos--sprints) (`7`)
- [Mobile Development](#mobile-development) (`38` recursos)
  - [Arquitetura e Padrões Mobile](#arquitetura-e-padrões-mobile) (`2`)
  - [iOS & Ferramentas Nativas](#ios--ferramentas-nativas) (`36`)
- [Processos de VibeCoding & Metodologia IA](#processos-de-vibecoding--metodologia-ia) (`24` recursos)
  - [Auditoria Anti-Slop & Segurança VibeCoding](#auditoria-anti-slop--segurança-vibecoding) (`1`)
  - [Engenharia de Contexto & Memória](#engenharia-de-contexto--memória) (`3`)
  - [Orquestração de Agentes & Superpoderes](#orquestração-de-agentes--superpoderes) (`11`)
  - [Padrões Fundamentais & Ciclo de Execução](#padrões-fundamentais--ciclo-de-execução) (`6`)
  - [Portão Socrático & Descoberta](#portão-socrático--descoberta) (`2`)
  - [Resolução e Descoberta de Skills](#resolução-e-descoberta-de-skills) (`1`)
- [Segurança & Compliance](#segurança--compliance) (`4` recursos)
  - [Compliance Regulatória & Privacidade](#compliance-regulatória--privacidade) (`1`)
  - [Modelagem de Ameaças & Red Team](#modelagem-de-ameaças--red-team) (`1`)
  - [Varredura SAST & Prevenção de Falhas](#varredura-sast--prevenção-de-falhas) (`2`)
- [Testing & Quality Assurance](#testing--quality-assurance) (`11` recursos)
  - [Automação de Testes E2E & Web](#automação-de-testes-e2e--web) (`1`)
  - [Desenvolvimento Orientado a Testes (TDD)](#desenvolvimento-orientado-a-testes-tdd) (`2`)
  - [Testes Unitários & Integração](#testes-unitários--integração) (`8`)
- [ads (Tráfego Pago (Ads))](#ads-tráfego-pago-ads) (`9` recursos)
  - [Analise De Desempenho](#analise-de-desempenho) (`1`)
  - [Copy De Anuncio](#copy-de-anuncio) (`2`)
  - [Criativos](#criativos) (`1`)
  - [Extracao De Anuncios Concorrentes](#extracao-de-anuncios-concorrentes) (`1`)
  - [Google](#google) (`1`)
  - [Meta](#meta) (`1`)
  - [Multiplataforma](#multiplataforma) (`1`)
  - [Trafego Pago](#trafego-pago) (`1`)
- [audiovisual (Mídia & Audiovisual)](#audiovisual-mídia--audiovisual) (`25` recursos)
  - [Agentes De Voz](#agentes-de-voz) (`1`)
  - [Apresentacoes Educacionais](#apresentacoes-educacionais) (`1`)
  - [Arte Conceitual](#arte-conceitual) (`1`)
  - [Banco De Imagens Pexels](#banco-de-imagens-pexels) (`1`)
  - [Banco De Midias Openverse](#banco-de-midias-openverse) (`1`)
  - [Criacao De Pitch Deck](#criacao-de-pitch-deck) (`1`)
  - [Download De Video](#download-de-video) (`1`)
  - [Estrutura De Apresentacao](#estrutura-de-apresentacao) (`1`)
  - [Imagem Flux Api](#imagem-flux-api) (`1`)
  - [Imagem Flux Prompts](#imagem-flux-prompts) (`1`)
  - [Infografico](#infografico) (`1`)
  - [Melhoria De Slide](#melhoria-de-slide) (`1`)
  - [Nano Banana](#nano-banana) (`1`)
  - [Nano Banana Pro](#nano-banana-pro) (`1`)
  - [Pitch Deck](#pitch-deck) (`1`)
  - [Podcast E Audio](#podcast-e-audio) (`1`)
  - [Producao De Video](#producao-de-video) (`1`)
  - [Qr Code](#qr-code) (`2`)
  - [Slidev](#slidev) (`2`)
  - [Storyline Mckinsey](#storyline-mckinsey) (`1`)
  - [Traducao De Legenda](#traducao-de-legenda) (`1`)
  - [Transcricao](#transcricao) (`1`)
  - [Video Para Gif](#video-para-gif) (`1`)
- [brand (Identidade da Marca)](#brand-identidade-da-marca) (`13` recursos)
  - [Audience](#audience) (`1`)
  - [Builder](#builder) (`1`)
  - [Design System](#design-system) (`1`)
  - [Direcao De Arte](#direcao-de-arte) (`1`)
  - [Essence](#essence) (`1`)
  - [Guardiao De Voz](#guardiao-de-voz) (`1`)
  - [Identidade Sonora](#identidade-sonora) (`1`)
  - [Identidade e Marca](#identidade-e-marca) (`1`)
  - [Naming](#naming) (`1`)
  - [Paleta De Cores](#paleta-de-cores) (`1`)
  - [Visual Direction](#visual-direction) (`1`)
  - [Visual Style](#visual-style) (`1`)
  - [Voice Messaging](#voice-messaging) (`1`)
- [conteudo (Produção de Conteúdo)](#conteudo-produção-de-conteúdo) (`22` recursos)
  - [Aprovacao](#aprovacao) (`1`)
  - [Brainstorm](#brainstorm) (`1`)
  - [Briefing](#briefing) (`2`)
  - [Briefing De Seo](#briefing-de-seo) (`1`)
  - [Criacao Multiformato](#criacao-multiformato) (`1`)
  - [Escrita Colaborativa](#escrita-colaborativa) (`1`)
  - [Estrategia](#estrategia) (`2`)
  - [Kit De Podcast](#kit-de-podcast) (`1`)
  - [Linha De Producao](#linha-de-producao) (`1`)
  - [Pesquisa](#pesquisa) (`2`)
  - [Post De Blog](#post-de-blog) (`2`)
  - [Pre Publicacao](#pre-publicacao) (`1`)
  - [Reaproveitamento](#reaproveitamento) (`2`)
  - [Sinais Fracos](#sinais-fracos) (`1`)
  - [Temas E Plugins](#temas-e-plugins) (`1`)
  - [Tendencias](#tendencias) (`2`)
- [copy (Copywriting & Conversão)](#copy-copywriting--conversão) (`14` recursos)
  - [Avaliacao De Hook](#avaliacao-de-hook) (`1`)
  - [Conversao](#conversao) (`1`)
  - [Hook De Video](#hook-de-video) (`1`)
  - [Hooks Video Curto](#hooks-video-curto) (`1`)
  - [Landing Page](#landing-page) (`2`)
  - [Landing Page Secao A Secao](#landing-page-secao-a-secao) (`1`)
  - [Metodos Classicos](#metodos-classicos) (`1`)
  - [Redacao Publicitaria](#redacao-publicitaria) (`1`)
  - [Roteiro De Video](#roteiro-de-video) (`1`)
  - [Roteiro Mais Falado](#roteiro-mais-falado) (`1`)
  - [Saas](#saas) (`2`)
  - [Vsl](#vsl) (`1`)
- [data (Inteligência de Dados)](#data-inteligência-de-dados) (`13` recursos)
  - [Analise De Desempenho](#analise-de-desempenho) (`1`)
  - [Analise De Funil](#analise-de-funil) (`1`)
  - [Analytics De Produto](#analytics-de-produto) (`1`)
  - [Analytics De Video](#analytics-de-video) (`1`)
  - [Atribuicao E Relatorios](#atribuicao-e-relatorios) (`1`)
  - [Calculo De Roi](#calculo-de-roi) (`1`)
  - [Funil E Coortes](#funil-e-coortes) (`1`)
  - [Gerador De Utm](#gerador-de-utm) (`1`)
  - [Interpretacao De Analytics](#interpretacao-de-analytics) (`1`)
  - [Posthog](#posthog) (`1`)
  - [Relatorio Executivo](#relatorio-executivo) (`1`)
  - [Revisao Mensal](#revisao-mensal) (`1`)
  - [Web Ga4](#web-ga4) (`1`)
- [email (Email Marketing)](#email-email-marketing) (`8` recursos)
  - [Automacao](#automacao) (`1`)
  - [Copy](#copy) (`1`)
  - [Entregabilidade](#entregabilidade) (`1`)
  - [Modelos](#modelos) (`1`)
  - [Newsletter](#newsletter) (`2`)
  - [Orquestracao De Campanhas](#orquestracao-de-campanhas) (`1`)
  - [Otimizacao De Assunto](#otimizacao-de-assunto) (`1`)
- [geral (Geral & Governança)](#geral-geral--governança) (`24` recursos)
  - [Anti Slop](#anti-slop) (`2`)
  - [Arquitetura De Projeto](#arquitetura-de-projeto) (`1`)
  - [Briefing Matinal](#briefing-matinal) (`1`)
  - [Conformidade Lgpd](#conformidade-lgpd) (`1`)
  - [Coordenacao De Campanhas](#coordenacao-de-campanhas) (`1`)
  - [Diagrama Mermaid](#diagrama-mermaid) (`1`)
  - [Execucao Autonoma](#execucao-autonoma) (`1`)
  - [Extracao E Plano De Acao](#extracao-e-plano-de-acao) (`1`)
  - [Gestao De Documentacao](#gestao-de-documentacao) (`1`)
  - [Mapa De Stakeholders](#mapa-de-stakeholders) (`1`)
  - [Navegador De Comandos](#navegador-de-comandos) (`1`)
  - [Navegador De Skills](#navegador-de-skills) (`1`)
  - [Operações e Rotinas](#operações-e-rotinas) (`1`)
  - [Parecer Sexy Canvas](#parecer-sexy-canvas) (`1`)
  - [Persona Fundador Startup](#persona-fundador-startup) (`1`)
  - [Persona Gerente De Marketing](#persona-gerente-de-marketing) (`1`)
  - [Persona Solopreneur](#persona-solopreneur) (`1`)
  - [Planejamento Diario](#planejamento-diario) (`1`)
  - [Postmortem](#postmortem) (`1`)
  - [Priorizacao Esforco Impacto](#priorizacao-esforco-impacto) (`1`)
  - [Revisao Mensal](#revisao-mensal) (`1`)
  - [Revisao Semanal](#revisao-semanal) (`1`)
  - [Verificacao De Fatos](#verificacao-de-fatos) (`1`)
- [growth (Growth Hacking)](#growth-growth-hacking) (`11` recursos)
  - [Aquisicao De Demanda](#aquisicao-de-demanda) (`1`)
  - [Aquisicao De Usuarios](#aquisicao-de-usuarios) (`1`)
  - [Atracao De Leads](#atracao-de-leads) (`1`)
  - [Expansao De Receita](#expansao-de-receita) (`1`)
  - [Experimentos Gtm](#experimentos-gtm) (`1`)
  - [Frameworks](#frameworks) (`1`)
  - [Indicacao E Afiliados](#indicacao-e-afiliados) (`1`)
  - [Retencao De Clientes](#retencao-de-clientes) (`1`)
  - [Retencao E Churn](#retencao-e-churn) (`1`)
  - [Teste Ab](#teste-ab) (`1`)
  - [Testes Ab](#testes-ab) (`1`)
- [persona (Clientes & Persona)](#persona-clientes--persona) (`7` recursos)
  - [Analise De Feedback](#analise-de-feedback) (`1`)
  - [Criacao De Persona](#criacao-de-persona) (`1`)
  - [Descoberta De Clientes](#descoberta-de-clientes) (`1`)
  - [Descoberta Interativa](#descoberta-interativa) (`1`)
  - [Entrevistas De Descoberta](#entrevistas-de-descoberta) (`1`)
  - [Gerador De Icp](#gerador-de-icp) (`1`)
  - [Icp](#icp) (`1`)
- [pr (Relações Públicas (PR))](#pr-relações-públicas-pr) (`2` recursos)
  - [Assessoria De Imprensa](#assessoria-de-imprensa) (`1`)
  - [Relacoes Publicas](#relacoes-publicas) (`1`)
- [produto (Gestão de Produto)](#produto-gestão-de-produto) (`10` recursos)
  - [Agile](#agile) (`2`)
  - [Especificacao De Funcionalidade](#especificacao-de-funcionalidade) (`1`)
  - [Historias De Usuario](#historias-de-usuario) (`1`)
  - [Levantamento De Requisitos](#levantamento-de-requisitos) (`1`)
  - [Planejamento De Sprint](#planejamento-de-sprint) (`1`)
  - [Prd](#prd) (`2`)
  - [Prd Estrategia Gtm](#prd-estrategia-gtm) (`1`)
  - [Roadmap Reverso](#roadmap-reverso) (`1`)
- [revenue (Estratégia de Receita (Revenue))](#revenue-estratégia-de-receita-revenue) (`25` recursos)
  - [Analise Competitiva](#analise-competitiva) (`1`)
  - [Campanhas](#campanhas) (`2`)
  - [Checklist De Lancamento De Campanha](#checklist-de-lancamento-de-campanha) (`1`)
  - [Criacao De Campanha](#criacao-de-campanha) (`1`)
  - [Estrategia Pmm](#estrategia-pmm) (`1`)
  - [Gtm E Posicionamento](#gtm-e-posicionamento) (`1`)
  - [Inteligencia Competitiva](#inteligencia-competitiva) (`1`)
  - [Lancamento](#lancamento) (`1`)
  - [Lancamento Tecnico](#lancamento-tecnico) (`2`)
  - [Modelos Mentais](#modelos-mentais) (`1`)
  - [Monitoramento De Preco Concorrente](#monitoramento-de-preco-concorrente) (`1`)
  - [Oferta](#oferta) (`1`)
  - [Orquestracao De Crm](#orquestracao-de-crm) (`1`)
  - [Orquestracao De Estrategia](#orquestracao-de-estrategia) (`1`)
  - [Pesquisa De Mercado](#pesquisa-de-mercado) (`1`)
  - [Planejamento De Campanha](#planejamento-de-campanha) (`1`)
  - [Plano De Lancamento](#plano-de-lancamento) (`1`)
  - [Preco](#preco) (`2`)
  - [Premortem Previsao](#premortem-previsao) (`2`)
  - [Psicologia](#psicologia) (`1`)
  - [Sexy Canvas](#sexy-canvas) (`1`)
- [seo (SEO & Mecanismos de Busca)](#seo-seo--mecanismos-de-busca) (`19` recursos)
  - [Agrupamento De Palavras Chave](#agrupamento-de-palavras-chave) (`1`)
  - [Analise De Serp](#analise-de-serp) (`1`)
  - [Api De Busca](#api-de-busca) (`1`)
  - [App Store](#app-store) (`1`)
  - [Autoridade E Backlinks](#autoridade-e-backlinks) (`1`)
  - [Checklist Semanal](#checklist-semanal) (`1`)
  - [Conteudo](#conteudo) (`1`)
  - [Geo](#geo) (`1`)
  - [On Page](#on-page) (`1`)
  - [Otimizacao De Busca](#otimizacao-de-busca) (`1`)
  - [Otimizacao De Conteudo](#otimizacao-de-conteudo) (`1`)
  - [Palavras Chave](#palavras-chave) (`1`)
  - [Podcast](#podcast) (`1`)
  - [Programatico](#programatico) (`1`)
  - [Relatorio De Desempenho](#relatorio-de-desempenho) (`1`)
  - [Schema Markup](#schema-markup) (`1`)
  - [Search Console](#search-console) (`1`)
  - [Tecnico](#tecnico) (`1`)
  - [Wordpress](#wordpress) (`1`)
- [site (Sites & Páginas de Conversão)](#site-sites--páginas-de-conversão) (`14` recursos)
  - [Arquitetura](#arquitetura) (`1`)
  - [Auditoria De Interface](#auditoria-de-interface) (`2`)
  - [Construcao De Landing Page](#construcao-de-landing-page) (`1`)
  - [Construcao De Site](#construcao-de-site) (`1`)
  - [Construcao Web](#construcao-web) (`1`)
  - [Cro](#cro) (`1`)
  - [Diretrizes Web Codigo](#diretrizes-web-codigo) (`1`)
  - [Injecao De Cta Astro](#injecao-de-cta-astro) (`1`)
  - [Interface De Conversao](#interface-de-conversao) (`1`)
  - [Otimizacao De Conversao](#otimizacao-de-conversao) (`1`)
  - [React Composicao](#react-composicao) (`1`)
  - [React Desempenho](#react-desempenho) (`1`)
  - [Tailwind Design System](#tailwind-design-system) (`1`)
- [social (Mídias Sociais)](#social-mídias-sociais) (`17` recursos)
  - [Analise De Desempenho](#analise-de-desempenho) (`1`)
  - [Calendario E Distribuicao](#calendario-e-distribuicao) (`1`)
  - [Carrossel](#carrossel) (`1`)
  - [Checklist Diario](#checklist-diario) (`1`)
  - [Conceito De Thumbnail](#conceito-de-thumbnail) (`1`)
  - [Conversao Para Formato Curto](#conversao-para-formato-curto) (`1`)
  - [Direcao De Arte Ia](#direcao-de-arte-ia) (`1`)
  - [Estrategia](#estrategia) (`1`)
  - [Instagram Api](#instagram-api) (`1`)
  - [Leitura De Post Twitter](#leitura-de-post-twitter) (`1`)
  - [Linkedin](#linkedin) (`1`)
  - [Otimizacao De Post Linkedin](#otimizacao-de-post-linkedin) (`1`)
  - [Otimizacao De Titulo De Video](#otimizacao-de-titulo-de-video) (`1`)
  - [Seo De Youtube](#seo-de-youtube) (`1`)
  - [Transcricao De Youtube](#transcricao-de-youtube) (`1`)
  - [Youtube Para Notas](#youtube-para-notas) (`2`)
- [vendas (Vendas B2B & Prospecção)](#vendas-vendas-b2b--prospecção) (`14` recursos)
  - [Cold Email](#cold-email) (`2`)
  - [Cold Email Multicanal](#cold-email-multicanal) (`1`)
  - [Direcao B2B](#direcao-b2b) (`1`)
  - [Habilitacao Comercial](#habilitacao-comercial) (`1`)
  - [Materiais De Venda](#materiais-de-venda) (`2`)
  - [Metodologias B2B](#metodologias-b2b) (`1`)
  - [Personalizacao Em Escala](#personalizacao-em-escala) (`1`)
  - [Pipeline](#pipeline) (`1`)
  - [Pitch De Patrocinio](#pitch-de-patrocinio) (`1`)
  - [Prospeccao De Leads](#prospeccao-de-leads) (`2`)
  - [Qualificacao De Leads](#qualificacao-de-leads) (`1`)

---

## <a id="ai-data--ml"></a>AI, Data & ML

Total de recursos nesta macro-área: `10`

### <a id="engenharia-de-prompts--avaliação-de-llms"></a>Engenharia de Prompts & Avaliação de LLMs

| Recurso | Tipo | Origem | Descrição e Aplicação |
| :--- | :--- | :--- | :--- |
| <a id="llm-evaluation"></a>**`llm-evaluation`** | `Skill` | `0 Padrões` | Implemente estratégias de avaliação abrangentes para aplicações LLM usando métricas automatizadas, feedback humano e benchmarking. Use ao testar o desempenho do LLM, medir a qualidade da aplicação de IA ou estabelecer estruturas de avaliação. |
| <a id="prompt-engineering-patterns"></a>**`prompt-engineering-patterns`** | `Skill` | `0 Padrões` | Domine técnicas avançadas de engenharia imediata para maximizar o desempenho, a confiabilidade e a controlabilidade do LLM na produção. Use ao otimizar prompts, melhorar os resultados do LLM ou projetar modelos de prompt de produção. |
| <a id="prompt-optimize"></a>**`/prompt-optimize`** | `Workflow` | `0 Padrões` | Otimize os prompts de produção com padrões CoT, poucos disparos e IA constitucional |
| <a id="prompt-engineer"></a>**`@prompt-engineer`** | `Agent` | `0 Padrões` | Engenheiro especialista em prompts, especializado em técnicas avançadas de prompts, otimização LLM e design de sistemas de IA. Domina a cadeia de pensamento, a IA constitucional e estratégias imediatas de produção. Use ao criar recursos de IA, melhorar o desempenho do agente ou criar prompts do sistema. |

### <a id="modelos-de-ia--machine-learning"></a>Modelos de IA & Machine Learning

| Recurso | Tipo | Origem | Descrição e Aplicação |
| :--- | :--- | :--- | :--- |
| <a id="ai-assistant"></a>**`/ai-assistant`** | `Workflow` | `0 Padrões` | Crie um aplicativo assistente de IA com NLU, gerenciamento de diálogo e integrações |
| <a id="ai-review"></a>**`/ai-review`** | `Workflow` | `0 Padrões` | Especialista em revisão de código com tecnologia de IA |
| <a id="langchain-agent"></a>**`/langchain-agent`** | `Workflow` | `0 Padrões` | Crie um agente baseado em LangGraph com padrões modernos |
| <a id="ml-engineer"></a>**`@ml-engineer`** | `Agent` | `0 Padrões` | Crie sistemas de ML de produção com PyTorch 2.x, TensorFlow e estruturas de ML modernas. Implementa serviço de modelo, engenharia de recursos, testes A/B e monitoramento. Use PROATIVAMENTE para implantação de modelo de ML, otimização de inferência ou infraestrutura de produção de ML. |

### <a id="pipelines-de-dados--transformação"></a>Pipelines de Dados & Transformação

| Recurso | Tipo | Origem | Descrição e Aplicação |
| :--- | :--- | :--- | :--- |
| <a id="data-quality-frameworks"></a>**`data-quality-frameworks`** | `Skill` | `0 Padrões` | Implemente validação de qualidade de dados com Grandes Esperanças, testes dbt e contratos de dados. Use ao criar pipelines de qualidade de dados, implementar regras de validação ou estabelecer contratos de dados. |
| <a id="spark-optimization"></a>**`spark-optimization`** | `Skill` | `0 Padrões` | Otimize trabalhos do Apache Spark com particionamento, armazenamento em cache, otimização aleatória e ajuste de memória. Use ao melhorar o desempenho do Spark, depurar trabalhos lentos ou dimensionar pipelines de processamento de dados. |

---

## <a id="arquitetura-de-software--engenharia"></a>Arquitetura de Software & Engenharia

Total de recursos nesta macro-área: `42`

### <a id="padrões-arquiteturais--boas-práticas"></a>Padrões Arquiteturais & Boas Práticas

| Recurso | Tipo | Origem | Descrição e Aplicação |
| :--- | :--- | :--- | :--- |
| <a id="code-review-checklist"></a>**`code-review-checklist`** | `Skill` | `0 Padrões` | Diretrizes de revisão de código que abrangem qualidade, segurança e práticas recomendadas do código. |
| <a id="defi-protocol-templates"></a>**`defi-protocol-templates`** | `Skill` | `0 Padrões` | Implemente protocolos DeFi com modelos prontos para produção para sistemas de piquetagem, AMMs, governança e empréstimo. Use ao criar aplicativos financeiros descentralizados ou protocolos de contratos inteligentes. |
| <a id="executing-plans"></a>**`executing-plans`** | `Skill` | `0 Padrões` | Use ao executar um plano de implementação na sessão atual como o próprio implementador — seu parceiro humano escolheu a execução em linha ou nenhuma ferramenta de subagente está disponível |
| <a id="game-development"></a>**`game-development`** | `Skill` | `0 Padrões` | Orquestrador de desenvolvimento de jogos. Rotas para habilidades específicas da plataforma com base nas necessidades do projeto. |
| <a id="geo-fundamentals"></a>**`geo-fundamentals`** | `Skill` | `0 Padrões` | Otimização generativa de mecanismos para mecanismos de busca de IA (ChatGPT, Claude, Perplexity). |
| <a id="go-concurrency-patterns"></a>**`go-concurrency-patterns`** | `Skill` | `0 Padrões` | Simultaneidade Master Go com goroutines, canais, primitivas de sincronização e contexto. Use ao criar aplicativos Go simultâneos, implementar pools de trabalhadores ou depurar condições de corrida. |
| <a id="linkerd-patterns"></a>**`linkerd-patterns`** | `Skill` | `0 Padrões` | Implemente padrões de malha de serviço Linkerd para implantações de malha de serviço leves e focadas em segurança. Use ao configurar o Linkerd, configurar políticas de tráfego ou implementar redes de confiança zero com sobrecarga mínima. |
| <a id="lint-and-validate"></a>**`lint-and-validate`** | `Skill` | `0 Padrões` | Procedimentos automáticos de controle de qualidade, fiapos e análise estática. Use após cada modificação de código para garantir a correção da sintaxe e os padrões do projeto. Gatilhos onKeywords: lint, formato, verificação, validação, tipos, análise estática. |
| <a id="powershell-windows"></a>**`powershell-windows`** | `Skill` | `0 Padrões` | Padrões do Windows do PowerShell. Armadilhas críticas, sintaxe do operador, tratamento de erros. |
| <a id="rust-async-patterns"></a>**`rust-async-patterns`** | `Skill` | `0 Padrões` | Domine a programação assíncrona Rust com Tokio, características assíncronas, tratamento de erros e padrões simultâneos. Use ao criar aplicativos Rust assíncronos, implementar sistemas simultâneos ou depurar código assíncrono. |
| <a id="shellcheck-configuration"></a>**`shellcheck-configuration`** | `Skill` | `0 Padrões` | Domine a configuração e o uso da análise estática do ShellCheck para qualidade de script de shell. Use ao configurar a infraestrutura de linting, corrigir problemas de código ou garantir a portabilidade de scripts. |
| <a id="slo-implementation"></a>**`slo-implementation`** | `Skill` | `0 Padrões` | Defina e implemente Indicadores de Nível de Serviço (SLIs) e Objetivos de Nível de Serviço (SLOs) com orçamentos de erros e alertas. Use ao estabelecer metas de confiabilidade, implementar práticas de SRE ou medir o desempenho do serviço. |
| <a id="code-explain"></a>**`/code-explain`** | `Workflow` | `0 Padrões` | Explicação e análise de código |
| <a id="code-migrate"></a>**`/code-migrate`** | `Workflow` | `0 Padrões` | Assistente de migração de código |
| <a id="config-validate"></a>**`/config-validate`** | `Workflow` | `0 Padrões` | Validação de configuração |
| <a id="cost-optimize"></a>**`/cost-optimize`** | `Workflow` | `0 Padrões` | Otimização de custos na nuvem |
| <a id="create_worktree"></a>**`/create_worktree`** | `Workflow` | `0 Padrões` | --- |
| <a id="debug"></a>**`/debug`** | `Workflow` | `0 Padrões` | Comando de depuração. Ativa o modo DEBUG para investigação sistemática de problemas. |
| <a id="debug-trace"></a>**`/debug-trace`** | `Workflow` | `0 Padrões` | Configuração de depuração e rastreamento |
| <a id="design-new-page"></a>**`/design-new-page`** | `Workflow` | `0 Padrões` | Desenvolvimento de página |
| <a id="doc-generate"></a>**`/doc-generate`** | `Workflow` | `0 Padrões` | Geração Automatizada de Documentação |
| <a id="execute-plan"></a>**`/execute-plan`** | `Workflow` | `0 Padrões` | Execute o plano em lotes com pontos de verificação de revisão |
| <a id="implement_plan"></a>**`/implement_plan`** | `Workflow` | `0 Padrões` | Implementar planos técnicos a partir de pensamentos/compartilhados/planos com verificação |
| <a id="local_review"></a>**`/local_review`** | `Workflow` | `0 Padrões` | Configure a árvore de trabalho para revisar a filial do colega |
| <a id="market-opportunity"></a>**`/market-opportunity`** | `Workflow` | `0 Padrões` | Gere análises abrangentes de oportunidades de mercado com cálculos TAM/SAM/SOM |
| <a id="monitor-setup"></a>**`/monitor-setup`** | `Workflow` | `0 Padrões` | Configuração de monitoramento e observabilidade |
| <a id="multi-agent-optimize"></a>**`/multi-agent-optimize`** | `Workflow` | `0 Padrões` | Kit de ferramentas de otimização multiagente |
| <a id="multi-agent-review"></a>**`/multi-agent-review`** | `Workflow` | `0 Padrões` | Ferramenta de orquestração de revisão de código multiagente |
| <a id="oneshot_plan"></a>**`/oneshot_plan`** | `Workflow` | `0 Padrões` | Executar plano Ralph e implementação para um ticket |
| <a id="refactor-clean"></a>**`/refactor-clean`** | `Workflow` | `0 Padrões` | Refatorar e limpar código |
| <a id="research_codebase"></a>**`/research_codebase`** | `Workflow` | `0 Padrões` | Documente a base de código como está com o diretório de pensamentos para contexto histórico |
| <a id="research_codebase_nt"></a>**`/research_codebase_nt`** | `Workflow` | `0 Padrões` | Documente a base de código como está, sem avaliação ou recomendações |
| <a id="rust-project"></a>**`/rust-project`** | `Workflow` | `0 Padrões` | Andaime de projeto de ferrugem |
| <a id="status"></a>**`/status`** | `Workflow` | `0 Padrões` | Exibir status do projeto, trilhas ativas e próximas ações |
| <a id="tech-debt"></a>**`/tech-debt`** | `Workflow` | `0 Padrões` | Análise e Remediação Técnica de Dívidas |
| <a id="typescript-scaffold"></a>**`/typescript-scaffold`** | `Workflow` | `0 Padrões` | Andaime do projeto TypeScript |
| <a id="write-plan"></a>**`/write-plan`** | `Workflow` | `0 Padrões` | Crie um plano de implementação detalhado com tarefas pequenas |
| <a id="blockchain-developer"></a>**`@blockchain-developer`** | `Agent` | `0 Padrões` | Crie aplicativos Web3 prontos para produção, contratos inteligentes e sistemas descentralizados. Implementa protocolos DeFi, plataformas NFT, DAOs e integrações de blockchain empresarial. Use PROATIVAMENTE para contratos inteligentes, aplicativos Web3, protocolos DeFi ou infraestrutura blockchain. |
| <a id="cpp-pro"></a>**`@cpp-pro`** | `Agent` | `0 Padrões` | Escreva código C++ idiomático com recursos modernos, RAII, ponteiros inteligentes e algoritmos STL. Lida com modelos, semântica de movimentação e otimização de desempenho. Use PROATIVAMENTE para refatoração C++, segurança de memória ou padrões C++ complexos. |
| <a id="php-pro"></a>**`@php-pro`** | `Agent` | `0 Padrões` | Escreva código PHP idiomático com geradores, iteradores, estruturas de dados SPL e recursos OOP modernos. Use PROATIVAMENTE para aplicativos PHP de alto desempenho. |
| <a id="seo-meta-optimizer"></a>**`@seo-meta-optimizer`** | `Agent` | `0 Padrões` | Cria metatítulos, descrições e sugestões de URL otimizados com base em limites de caracteres e práticas recomendadas. Gera metadados atraentes e ricos em palavras-chave. Use PROATIVAMENTE para novos conteúdos. |
| <a id="seo-snippet-hunter"></a>**`@seo-snippet-hunter`** | `Agent` | `0 Padrões` | Formata o conteúdo para ser elegível para snippets em destaque e recursos SERP. Cria blocos de conteúdo otimizados para snippets com base nas práticas recomendadas. Use PROATIVAMENTE para conteúdo baseado em perguntas. |

---

## <a id="backend--apis"></a>Backend & APIs

Total de recursos nesta macro-área: `20`

### <a id="design--integração-de-apis-rest--graphql"></a>Design & Integração de APIs (REST / GraphQL)

| Recurso | Tipo | Origem | Descrição e Aplicação |
| :--- | :--- | :--- | :--- |
| <a id="claude-code-review"></a>**`claude-code-review`** | `Skill` | `0 Padrões` | Use ao configurar, ajustar ou executar o Claude Code Review (revisão gerenciada do GitHub PR, REVIEW.md, @claude review) ou o comando local /code-review, quando as descobertas da revisão são barulhentas, ausentes ou caras, ou ao restringir mesclagens na gravidade da revisão automatizada. Também para revisão de PR automatizada e solicitações de ultrareview. |
| <a id="launch-readiness"></a>**`launch-readiness`** | `Skill` | `0 Padrões` | Use quando um aplicativo ou site construído com IA está prestes a ser publicado ou lançado, ou o usuário solicita uma verificação de pré-lançamento, go-live ou "antes de lançamento" além da segurança do código - capacidade de entrega de e-mail, envio de loja de aplicativos, risco de chatbot, kill switch e limites de gastos, links quebrados, exposição legal e de privacidade. |
| <a id="openapi-spec-generation"></a>**`openapi-spec-generation`** | `Skill` | `0 Padrões` | Gere e mantenha especificações OpenAPI 3.1 a partir de código, especificações de design inicial e padrões de validação. Use ao criar documentação de API, gerar SDKs ou garantir a conformidade do contrato de API. |
| <a id="sip-firecrawl"></a>**`sip-firecrawl`** | `Skill` | `0 Padrões` | Use whenever the current task involves Firecrawl (web scraping, crawling, mapping, search, structured extraction, browser interaction, monitoring, lead gen, SEO audits, etc.) but the active project has no local Firecrawl skills — i.e. any project other than "SIP - Firecrawl" (Firecrawl - local) itself. Routes the task to the central Firecrawl knowledge hub instead of improvising from general knowledge. Also use when the user asks "existe algo de firecrawl pra isso", "tem skill de scraping no hub", "consulta o SIP - Firecrawl", or names Firecrawl explicitly in a project that isn't it. Este stub existe para que IAs que não leem `.claude/skills/` (Google Antigravity/Gemini, Cursor) ainda encontrem este nome via Regra 4 (Fallback Resolution Protocol) — o Claude Code já tem acesso direto via `.claude/skills/sip-firecrawl`. |
| <a id="verification-before-completion"></a>**`verification-before-completion`** | `Skill` | `0 Padrões` | Use quando estiver prestes a declarar que o trabalho foi concluído, corrigido ou aprovado, antes de confirmar ou criar PRs - requer a execução de comandos de verificação e a confirmação da saída antes de fazer qualquer declaração de sucesso; evidência antes de afirmações sempre |
| <a id="api-mock"></a>**`/api-mock`** | `Workflow` | `0 Padrões` | Estrutura de simulação de API |
| <a id="full-stack-feature"></a>**`/full-stack-feature`** | `Workflow` | `0 Padrões` | Orquestre o desenvolvimento de recursos full-stack em camadas de back-end, front-end e infraestrutura com uma abordagem moderna baseada em API |
| <a id="api-documenter"></a>**`@api-documenter`** | `Agent` | `0 Padrões` | Domine a documentação da API com OpenAPI 3.1, ferramentas baseadas em IA e práticas modernas de experiência do desenvolvedor. Crie documentos interativos, gere SDKs e construa portais abrangentes para desenvolvedores. Use PROATIVAMENTE para documentação de API ou criação de portal de desenvolvedor. |
| <a id="backend-security-coder"></a>**`@backend-security-coder`** | `Agent` | `0 Padrões` | Especialista em práticas seguras de codificação de back-end, especializado em validação de entrada, autenticação e segurança de API. Use PROATIVAMENTE para implementações de segurança de back-end ou revisões de código de segurança. |
| <a id="documentation-writer"></a>**`@documentation-writer`** | `Agent` | `0 Padrões` | Especialista em documentação técnica. Use SOMENTE quando o usuário solicitar explicitamente a documentação (README, documentos da API, changelog). NÃO invoque automaticamente durante o desenvolvimento normal. |
| <a id="qa-automation-engineer"></a>**`@qa-automation-engineer`** | `Agent` | `0 Padrões` | Especialista em infraestrutura de automação de testes e testes E2E. Concentra-se em Playwright, Cypress, pipelines de CI e na quebra do sistema. Gatilhos em e2e, teste automatizado, pipeline, dramaturgo, cipreste, regressão. |

### <a id="nodejs-go--microsserviços"></a>Node.js, Go & Microsserviços

| Recurso | Tipo | Origem | Descrição e Aplicação |
| :--- | :--- | :--- | :--- |
| <a id="sip-n8n"></a>**`sip-n8n`** | `Skill` | `0 Padrões` | Use whenever the current task involves n8n (workflows, nodes, expressions, Code nodes, AI Agents in n8n, webhooks, self-hosting, or the n8n REST API) but the active project has no local n8n skills — i.e. any project other than "SIP- N8N" itself. Routes the task to the central n8n knowledge hub instead of improvising from general knowledge. Also use when the user asks "existe algo de n8n pra isso", "tem template pra isso no hub", "consulta o SIP - N8N", or names n8n explicitly in a project that isn't it. Este stub existe para que IAs que não leem `.claude/skills/` (Google Antigravity/Gemini, Cursor) ainda encontrem este nome via Regra 4 (Fallback Resolution Protocol) — o Claude Code já tem acesso direto via `.claude/skills/sip-n8n`. |
| <a id="javascript-pro"></a>**`@javascript-pro`** | `Agent` | `0 Padrões` | Domine JavaScript moderno com ES6+, padrões assíncronos e APIs Node.js. Lida com promessas, loops de eventos e compatibilidade de navegador/nó. Use PROATIVAMENTE para otimização de JavaScript, depuração assíncrona ou padrões JS complexos. |

### <a id="python--backends-de-alta-performance"></a>Python & Backends de Alta Performance

| Recurso | Tipo | Origem | Descrição e Aplicação |
| :--- | :--- | :--- | :--- |
| <a id="async-python-patterns"></a>**`async-python-patterns`** | `Skill` | `0 Padrões` | Domine Python assíncrono, programação simultânea e padrões assíncronos/aguardados para aplicativos de alto desempenho. Use ao criar APIs assíncronas, sistemas simultâneos ou aplicativos vinculados a E/S que exigem operações sem bloqueio. |
| <a id="fastapi-templates"></a>**`fastapi-templates`** | `Skill` | `0 Padrões` | Crie projetos FastAPI prontos para produção com padrões assíncronos, injeção de dependência e tratamento abrangente de erros. Use ao criar novos aplicativos FastAPI ou configurar projetos de API de back-end. |
| <a id="python-performance-optimization"></a>**`python-performance-optimization`** | `Skill` | `0 Padrões` | Crie perfis e otimize o código Python usando cProfile, criadores de perfil de memória e práticas recomendadas de desempenho. Use ao depurar código Python lento, otimizar gargalos ou melhorar o desempenho do aplicativo. |
| <a id="python-testing-patterns"></a>**`python-testing-patterns`** | `Skill` | `0 Padrões` | Implemente estratégias de teste abrangentes com pytest, fixtures, simulação e desenvolvimento orientado a testes. Use ao escrever testes Python, configurar conjuntos de testes ou implementar práticas recomendadas de teste. |
| <a id="python-scaffold"></a>**`/python-scaffold`** | `Workflow` | `0 Padrões` | Andaime do projeto Python |

### <a id="serviços-de-autenticação--pagamentos"></a>Serviços de Autenticação & Pagamentos

| Recurso | Tipo | Origem | Descrição e Aplicação |
| :--- | :--- | :--- | :--- |
| <a id="billing-automation"></a>**`billing-automation`** | `Skill` | `0 Padrões` | Crie sistemas de faturamento automatizados para pagamentos recorrentes, faturamento, ciclo de vida de assinatura e gerenciamento de cobranças. Use ao implementar o faturamento de assinaturas, automatizar o faturamento ou gerenciar sistemas de pagamento recorrentes. |
| <a id="security-auditor"></a>**`@security-auditor`** | `Agent` | `0 Padrões` | Auditor de segurança especializado em DevSecOps, segurança cibernética abrangente e estruturas de conformidade. Domina avaliação de vulnerabilidades, modelagem de ameaças, autenticação segura (OAuth2/OIDC), padrões OWASP, segurança em nuvem e automação de segurança. Lida com integração DevSecOps, conformidade (GDPR/HIPAA/SOC2) e resposta a incidentes. Use PROATIVAMENTE para auditorias de segurança, DevSecOps ou implementação de conformidade. |

---

## <a id="database--storage"></a>Database & Storage

Total de recursos nesta macro-área: `6`

### <a id="bancos-relacionais-postgresql--sql"></a>Bancos Relacionais (PostgreSQL & SQL)

| Recurso | Tipo | Origem | Descrição e Aplicação |
| :--- | :--- | :--- | :--- |
| <a id="postgresql"></a>**`postgresql`** | `Skill` | `0 Padrões` | Projete um esquema específico do PostgreSQL. Abrange práticas recomendadas, tipos de dados, indexação, restrições, padrões de desempenho e recursos avançados |
| <a id="sql-optimization-patterns"></a>**`sql-optimization-patterns`** | `Skill` | `0 Padrões` | Domine a otimização de consultas SQL, estratégias de indexação e análise EXPLAIN para melhorar drasticamente o desempenho do banco de dados e eliminar consultas lentas. Use ao depurar consultas lentas, projetar esquemas de banco de dados ou otimizar o desempenho do aplicativo. |
| <a id="sql-pro"></a>**`@sql-pro`** | `Agent` | `0 Padrões` | Domine SQL moderno com bancos de dados nativos da nuvem, otimização OLTP/OLAP e técnicas avançadas de consulta. Especialista em ajuste de desempenho, modelagem de dados e sistemas analíticos híbridos. Use PROATIVAMENTE para otimização de banco de dados ou análises complexas. |

### <a id="modelagem--migrações-de-banco"></a>Modelagem & Migrações de Banco

| Recurso | Tipo | Origem | Descrição e Aplicação |
| :--- | :--- | :--- | :--- |
| <a id="database-migration"></a>**`database-migration`** | `Skill` | `0 Padrões` | Execute migrações de banco de dados entre ORMs e plataformas com estratégias de tempo de inatividade zero, transformação de dados e procedimentos de reversão. Use ao migrar bancos de dados, alterar esquemas, realizar transformações de dados ou implementar estratégias de implantação com tempo de inatividade zero. |
| <a id="migration-observability"></a>**`/migration-observability`** | `Workflow` | `0 Padrões` | Monitoramento de migração, CDC e infraestrutura de observabilidade |
| <a id="sql-migrations"></a>**`/sql-migrations`** | `Workflow` | `0 Padrões` | Migrações de banco de dados SQL com estratégias de tempo de inatividade zero para PostgreSQL, MySQL, SQL Server |

---

## <a id="devops--cloud-infra"></a>DevOps & Cloud Infra

Total de recursos nesta macro-área: `65`

### <a id="infraestrutura-como-código-terraform--cloud"></a>Infraestrutura como Código (Terraform / Cloud)

| Recurso | Tipo | Origem | Descrição e Aplicação |
| :--- | :--- | :--- | :--- |
| <a id="cost-optimization"></a>**`cost-optimization`** | `Skill` | `0 Padrões` | Otimize os custos da nuvem por meio de redimensionamento de recursos, estratégias de marcação, instâncias reservadas e análise de gastos. Use ao reduzir despesas com nuvem, analisar custos de infraestrutura ou implementar políticas de governança de custos. |
| <a id="prometheus-configuration"></a>**`prometheus-configuration`** | `Skill` | `0 Padrões` | Configure o Prometheus para coleta abrangente de métricas, armazenamento e monitoramento de infraestrutura e aplicativos. Use ao implementar a coleta de métricas, configurar a infraestrutura de monitoramento ou configurar sistemas de alerta. |
| <a id="mlops-engineer"></a>**`@mlops-engineer`** | `Agent` | `0 Padrões` | Crie pipelines de ML abrangentes, rastreamento de experimentos e registros de modelos com MLflow, Kubeflow e ferramentas modernas de MLOps. Implementa treinamento, implantação e monitoramento automatizados em plataformas de nuvem. Use PROATIVAMENTE para infraestrutura de ML, gerenciamento de experimentos ou automação de pipeline. |

### <a id="orquestração-kubernetes--contêineres"></a>Orquestração Kubernetes & Contêineres

| Recurso | Tipo | Origem | Descrição e Aplicação |
| :--- | :--- | :--- | :--- |
| <a id="helm-chart-scaffolding"></a>**`helm-chart-scaffolding`** | `Skill` | `0 Padrões` | Projete, organize e gerencie gráficos Helm para criar modelos e empacotar aplicativos Kubernetes com configurações reutilizáveis. Use ao criar gráficos Helm, empacotar aplicativos Kubernetes ou implementar implantações de modelo. |
| <a id="devops-troubleshooter"></a>**`@devops-troubleshooter`** | `Agent` | `0 Padrões` | Solucionador de problemas especializado em DevOps, especializado em resposta rápida a incidentes, depuração avançada e observabilidade moderna. Domine a análise de log, rastreamento distribuído, depuração do Kubernetes, otimização de desempenho e análise de causa raiz. Lida com interrupções de produção, confiabilidade do sistema e monitoramento preventivo. Use PROATIVAMENTE para depuração, resposta a incidentes ou solução de problemas do sistema. |

### <a id="pipelines-de-cicd--deploy-contínuo"></a>Pipelines de CI/CD & Deploy Contínuo

| Recurso | Tipo | Origem | Descrição e Aplicação |
| :--- | :--- | :--- | :--- |
| <a id="competitive-landscape"></a>**`competitive-landscape`** | `Skill` | `0 Padrões` | Esta habilidade deve ser utilizada quando o usuário solicita “analisar concorrentes”, “avaliar cenário competitivo”, “identificar diferenciação”, “avaliar posicionamento de mercado”, “aplicar as Cinco Forças de Porter” ou solicitar análise de estratégia competitiva. |
| <a id="debugging-strategies"></a>**`debugging-strategies`** | `Skill` | `0 Padrões` | Domine técnicas sistemáticas de depuração, ferramentas de criação de perfil e análise de causa raiz para rastrear bugs com eficiência em qualquer base de código ou pilha de tecnologia. Use ao investigar bugs, problemas de desempenho ou comportamento inesperado. |
| <a id="dependency-upgrade"></a>**`dependency-upgrade`** | `Skill` | `0 Padrões` | Gerencie atualizações de versões de dependências importantes com análise de compatibilidade, implementação gradual e testes abrangentes. Use ao atualizar versões da estrutura, atualizar dependências principais ou gerenciar alterações significativas em bibliotecas. |
| <a id="finishing-a-development-branch"></a>**`finishing-a-development-branch`** | `Skill` | `0 Padrões` | Use quando a implementação for concluída, todos os testes forem aprovados e você precisar decidir como integrar o trabalho |
| <a id="gdpr-data-handling"></a>**`gdpr-data-handling`** | `Skill` | `0 Padrões` | Implemente o tratamento de dados em conformidade com o GDPR com gerenciamento de consentimento, direitos do titular dos dados e privacidade desde o projeto. Use ao criar sistemas que processem dados pessoais da UE, implementando controles de privacidade ou conduzindo análises de conformidade com o GDPR. |
| <a id="github-publisher"></a>**`github-publisher`** | `Skill` | `0 Padrões` | Use quando o usuário solicitar para publicar, fazer upload ou enviar uma pasta local ou projeto para o GitHub pela primeira vez, criar um novo repositório GitHub a partir de código existente ou "subir o projeto pro GitHub" / "criar repositório" - inclusive quando disserem que já está limpo ou que estão com pressa. |
| <a id="grafana-dashboards"></a>**`grafana-dashboards`** | `Skill` | `0 Padrões` | Crie e gerencie painéis de produção do Grafana para visualização em tempo real de métricas de sistemas e aplicativos. Use ao criar painéis de monitoramento, visualizar métricas ou criar interfaces de observabilidade operacional. |
| <a id="incident-runbook-templates"></a>**`incident-runbook-templates`** | `Skill` | `0 Padrões` | Crie runbooks estruturados de resposta a incidentes com procedimentos passo a passo, caminhos de escalonamento e ações de recuperação. Use ao criar runbooks, responder a incidentes ou estabelecer procedimentos de resposta a incidentes. |
| <a id="interaction-design"></a>**`interaction-design`** | `Skill` | `0 Padrões` | Projete e implemente microinterações, design de movimento, transições e padrões de feedback do usuário. Use ao adicionar polimento às interações da IU, implementar estados de carregamento ou criar experiências de usuário agradáveis. |
| <a id="market-sizing-analysis"></a>**`market-sizing-analysis`** | `Skill` | `0 Padrões` | Esta habilidade deve ser usada quando o usuário pede para “calcular TAM”, “determinar SAM”, “estimar SOM”, “dimensionar o mercado”, “calcular oportunidade de mercado”, “qual é o mercado total endereçável”, ou solicitar análise de dimensionamento de mercado para uma startup ou oportunidade de negócio. |
| <a id="memory-safety-patterns"></a>**`memory-safety-patterns`** | `Skill` | `0 Padrões` | Implemente programação segura de memória com RAII, propriedade, ponteiros inteligentes e gerenciamento de recursos em Rust, C++ e C. Use ao escrever códigos de sistemas seguros, gerenciar recursos ou prevenir bugs de memória. |
| <a id="mtls-configuration"></a>**`mtls-configuration`** | `Skill` | `0 Padrões` | Configure o TLS mútuo (mTLS) para comunicação entre serviços de confiança zero. Use ao implementar redes de confiança zero, gerenciamento de certificados ou proteger a comunicação de serviço interno. |
| <a id="on-call-handoff-patterns"></a>**`on-call-handoff-patterns`** | `Skill` | `0 Padrões` | Domine a transferência de turnos de plantão com transferência de contexto, procedimentos de escalonamento e documentação. Use ao fazer a transição de responsabilidades de plantão, documentar resumos de turnos ou melhorar processos de plantão. |
| <a id="opus-haiku"></a>**`opus-haiku`** | `Skill` | `0 Padrões` | Use quando o usuário invoca /opus-haiku ou pede para salvar o uso do plano delegando a escrita do código para um modelo mais barato enquanto o modelo principal planeja e revisa, e na fase de Execução do loop de execução. |
| <a id="ponytail"></a>**`ponytail`** | `Skill` | `0 Padrões` | Lazy senior dev mode: the smallest change that fully solves the task, and a reply a busy human understands in one read. Use on any coding task (writing, fixing, refactoring, reviewing, choosing dependencies) and when the user says "ponytail", "be lazy", "simplest solution", "yagni", or complains about over-engineering or bloat. Levels: lite, full (default), ultra. |
| <a id="receiving-code-review"></a>**`receiving-code-review`** | `Skill` | `0 Padrões` | Use ao receber feedback de revisão de código, antes de implementar sugestões, especialmente se o feedback parecer pouco claro ou tecnicamente questionável - requer rigor técnico e verificação, não acordo performativo ou implementação cega |
| <a id="secrets-management"></a>**`secrets-management`** | `Skill` | `0 Padrões` | Implemente o gerenciamento seguro de segredos para pipelines de CI/CD usando Vault, AWS Secrets Manager ou soluções de plataforma nativa. Use ao lidar com credenciais confidenciais, alternar segredos ou proteger ambientes de CI/CD. |
| <a id="sip-imprensa"></a>**`sip-imprensa`** | `Skill` | `0 Padrões` | Use whenever the current task involves imprensa (jornalistas, veículos, pauta, pitch, assessoria de imprensa, PR) but the active project has no local imprensa skills — i.e. any project other than "SIP - Imprensa & PR" (RSS Feed) itself. Routes the task to the central imprensa knowledge hub instead of improvising from general knowledge. Also use when the user asks "existe algo de imprensa pra isso", "tem skill de jornalista no hub", "consulta o SIP - Imprensa & PR", or names imprensa explicitly in a project that isn't it. Este stub existe para que IAs que não leem `.claude/skills/` (Google Antigravity/Gemini, Cursor) ainda encontrem este nome via Regra 4 (Fallback Resolution Protocol) — o Claude Code já tem acesso direto via `.claude/skills/sip-imprensa`. |
| <a id="sip-trends-previsao-demanda"></a>**`sip-trends-previsao-demanda`** | `Skill` | `0 Padrões` | Use whenever the current task involves demand forecasting, seasonality analysis, or Google Trends data but the active project has no local skills for it — i.e. any project other than "SIP - Trends e Previsão de Demanda (Sazonalidade)" itself. Routes the task to the central knowledge hub instead of improvising from general knowledge. Also use when the user asks "existe algo de sazonalidade/trends pra isso", "tem template pra isso no hub", "consulta o SIP de previsão de demanda", or names Google Trends / sazonalidade explicitly in a project that isn't it. Este stub existe para que IAs que não leem `.claude/skills/` (Google Antigravity/Gemini, Cursor) ainda encontrem este nome via Regra 4 (Fallback Resolution Protocol) — o Claude Code já tem acesso direto via `.claude/skills/sip-trends-previsao-demanda`. |
| <a id="threat-mitigation-mapping"></a>**`threat-mitigation-mapping`** | `Skill` | `0 Padrões` | Mapeie ameaças identificadas para controles e mitigações de segurança apropriados. Use ao priorizar investimentos em segurança, criar planos de correção ou validar a eficácia do controle. |
| <a id="turborepo-caching"></a>**`turborepo-caching`** | `Skill` | `0 Padrões` | Configure o Turborepo para compilações monorepo eficientes com cache local e remoto. Use ao configurar o Turborepo, otimizar pipelines de construção ou implementar cache distribuído. |
| <a id="using-git-worktrees"></a>**`using-git-worktrees`** | `Skill` | `0 Padrões` | Use ao iniciar o trabalho de recurso que precisa de isolamento do espaço de trabalho atual ou antes de executar planos de implementação - garante que exista um espaço de trabalho isolado por meio de ferramentas nativas ou substituto da árvore de trabalho git |
| <a id="web3-testing"></a>**`web3-testing`** | `Skill` | `0 Padrões` | Teste contratos inteligentes de forma abrangente usando Hardhat e Foundry com testes de unidade, testes de integração e bifurcação de rede principal. Use ao testar contratos Solidity, configurar conjuntos de testes de blockchain ou validar protocolos DeFi. |
| <a id="ci_commit"></a>**`/ci_commit`** | `Workflow` | `0 Padrões` | Crie commits git para alterações de sessão com mensagens atômicas claras |
| <a id="deploy"></a>**`/deploy`** | `Workflow` | `0 Padrões` | Comando de implantação para versões de produção. Verificações pré-voo e execução de implantação. |
| <a id="deps-audit"></a>**`/deps-audit`** | `Workflow` | `0 Padrões` | Auditoria de Dependências e Análise de Segurança |
| <a id="deps-upgrade"></a>**`/deps-upgrade`** | `Workflow` | `0 Padrões` | Estratégia de atualização de dependência |
| <a id="enhance"></a>**`/enhance`** | `Workflow` | `0 Padrões` | Adicione ou atualize recursos em aplicativos existentes. Usado para desenvolvimento iterativo. |
| <a id="full-review"></a>**`/full-review`** | `Workflow` | `0 Padrões` | Orquestre revisão de código multidimensional abrangente usando agentes de revisão especializados |
| <a id="incident-response"></a>**`/incident-response`** | `Workflow` | `0 Padrões` | Orquestre a resposta multiagente a incidentes com práticas modernas de SRE para rápida resolução e aprendizado |
| <a id="performance-optimization"></a>**`/performance-optimization`** | `Workflow` | `0 Padrões` | Otimize o desempenho do aplicativo de ponta a ponta usando agentes especializados de desempenho e otimização |
| <a id="pr-enhance"></a>**`/pr-enhance`** | `Workflow` | `0 Padrões` | Aprimoramento de solicitação pull |
| <a id="preview"></a>**`/preview`** | `Workflow` | `0 Padrões` | Visualize o início, a parada e a verificação de status do servidor. Gerenciamento de servidor de desenvolvimento local. |
| <a id="revert"></a>**`/revert`** | `Workflow` | `0 Padrões` | Desfazer com reconhecimento de Git por unidade de trabalho lógica (faixa, fase ou tarefa) |
| <a id="security-dependencies"></a>**`/security-dependencies`** | `Workflow` | `0 Padrões` | Verificação de vulnerabilidade de dependência |
| <a id="security-hardening"></a>**`/security-hardening`** | `Workflow` | `0 Padrões` | Implemente o fortalecimento abrangente da segurança com estratégia de defesa profunda por meio de orquestração multiagente coordenada |
| <a id="arm-cortex-expert"></a>**`@arm-cortex-expert`** | `Agent` | `0 Padrões` | Engenheiro de software embarcado sênior especializado em desenvolvimento de firmware e drivers para microcontroladores ARM Cortex-M (Teensy, STM32, nRF52, SAMD). Décadas de experiência escrevendo código incorporado confiável, otimizado e de fácil manutenção, com profundo conhecimento em barreiras de memória, coerência DMA/cache, E/S orientada por interrupção e drivers periféricos. |
| <a id="c-pro"></a>**`@c-pro`** | `Agent` | `0 Padrões` | Escreva código C eficiente com gerenciamento de memória adequado, aritmética de ponteiro e chamadas de sistema. Lida com sistemas embarcados, módulos de kernel e código de desempenho crítico. Use PROATIVAMENTE para otimização C, problemas de memória ou programação do sistema. |
| <a id="code-archaeologist"></a>**`@code-archaeologist`** | `Agent` | `0 Padrões` | Especialista em código legado, refatoração e compreensão de sistemas não documentados. Use para leitura de código confuso, engenharia reversa e planejamento de modernização. Aciona legado, refatoração, código espaguete, análise de repositório, explicação da base de código. |
| <a id="code-reviewer"></a>**`@code-reviewer`** | `Agent` | `0 Padrões` | Especialista em revisão de código de elite, especializado em análise de código moderna baseada em IA, vulnerabilidades de segurança, otimização de desempenho e confiabilidade de produção. Domina ferramentas de análise estática, verificação de segurança e revisão de configuração com as práticas recomendadas 2024/2025. Use PROATIVAMENTE para garantia de qualidade do código. |
| <a id="conductor-validator"></a>**`@conductor-validator`** | `Agent` | `0 Padrões` | Valida os artefatos do projeto do Conductor quanto à integridade, consistência e correção. Use após a configuração, ao diagnosticar problemas ou antes da implementação para verificar o contexto do projeto. |
| <a id="csharp-pro"></a>**`@csharp-pro`** | `Agent` | `0 Padrões` | Escreva código C# moderno com recursos avançados como registros, correspondência de padrões e assíncrono/espera. Otimiza aplicativos .NET, implementa padrões empresariais e garante testes abrangentes. Use PROATIVAMENTE para refatoração C#, otimização de desempenho ou soluções .NET complexas. |
| <a id="customer-support"></a>**`@customer-support`** | `Agent` | `0 Padrões` | Especialista em suporte ao cliente com inteligência artificial de elite que domina IA conversacional, emissão automatizada de tickets, análise de sentimento e experiências de suporte omnicanal. Integra ferramentas de suporte modernas, plataformas de chatbot e otimização CX com as melhores práticas 2024/2025. Use PROATIVAMENTE para um gerenciamento abrangente da experiência do cliente. |
| <a id="debugger"></a>**`@debugger`** | `Agent` | `0 Padrões` | Especialista em depuração de erros, falhas de teste e comportamento inesperado. Use proativamente ao encontrar qualquer problema. |
| <a id="devops-engineer"></a>**`@devops-engineer`** | `Agent` | `0 Padrões` | Especialista em implantação, gerenciamento de servidores, CI/CD e operações de produção. CRÍTICO - Use para implantação, acesso ao servidor, reversão e alterações de produção. Operações de ALTO RISCO. Aciona em implantação, produção, servidor, pm2, ssh, liberação, reversão, ci/cd. |
| <a id="elixir-pro"></a>**`@elixir-pro`** | `Agent` | `0 Padrões` | Escreva código Elixir idiomático com padrões OTP, árvores de supervisão e Phoenix LiveView. Domina simultaneidade, tolerância a falhas e sistemas distribuídos. Use PROATIVAMENTE para refatoração de Elixir, design de OTP ou otimizações complexas de BEAM. |
| <a id="incident-responder"></a>**`@incident-responder`** | `Agent` | `0 Padrões` | Respondente especializado em incidentes SRE, especializado em resolução rápida de problemas, observabilidade moderna e gerenciamento abrangente de incidentes. Domine o comando de incidentes, análises post-mortem sem culpa, gerenciamento de orçamento de erros e padrões de confiabilidade do sistema. Lida com interrupções críticas, estratégias de comunicação e melhoria contínua. Use IMEDIATAMENTE para incidentes de produção ou práticas de SRE. |
| <a id="legacy-modernizer"></a>**`@legacy-modernizer`** | `Agent` | `0 Padrões` | Refatore bases de código legadas, migre estruturas desatualizadas e implemente uma modernização gradual. Lida com dívidas técnicas, atualizações de dependências e compatibilidade com versões anteriores. Use PROATIVAMENTE para atualizações de sistemas legados, migrações de estruturas ou redução de dívidas técnicas. |
| <a id="penetration-tester"></a>**`@penetration-tester`** | `Agent` | `0 Padrões` | Especialista em segurança ofensiva, testes de penetração, operações de red team e exploração de vulnerabilidades. Use para avaliações de segurança, simulações de ataques e localização de vulnerabilidades exploráveis. Aciona pentest, exploração, ataque, hack, violação, pwn, redteam, ofensivo. |
| <a id="performance-optimizer"></a>**`@performance-optimizer`** | `Agent` | `0 Padrões` | Especialista em otimização de desempenho, criação de perfil, Core Web Vitals e otimização de pacotes. Use para melhorar a velocidade, reduzir o tamanho do pacote e otimizar o desempenho do tempo de execução. Aciona desempenho, otimização, velocidade, lentidão, memória, CPU, benchmark, farol. |
| <a id="posix-shell-pro"></a>**`@posix-shell-pro`** | `Agent` | `0 Padrões` | Especialista em scripts sh POSIX rigorosos para máxima portabilidade em sistemas do tipo Unix. Especializado em scripts de shell executados em qualquer shell compatível com POSIX (dash, ash, sh, bash --posix). |
| <a id="quant-analyst"></a>**`@quant-analyst`** | `Agent` | `0 Padrões` | Crie modelos financeiros, faça backtest de estratégias de negociação e analise dados de mercado. Implementa métricas de risco, otimização de portfólio e arbitragem estatística. Use PROATIVAMENTE para finanças quantitativas, algoritmos de negociação ou análise de risco. |
| <a id="risk-manager"></a>**`@risk-manager`** | `Agent` | `0 Padrões` | Monitore o risco do portfólio, múltiplos R e limites de posição. Cria estratégias de hedge, calcula expectativa e implementa stop-loss. Use PROATIVAMENTE para avaliação de risco, rastreamento de negociações ou proteção de portfólio. |
| <a id="ruby-pro"></a>**`@ruby-pro`** | `Agent` | `0 Padrões` | Escreva código Ruby idiomático com metaprogramação, padrões Rails e otimização de desempenho. Especializado em Ruby on Rails, desenvolvimento de gem e frameworks de teste. Use PROATIVAMENTE para refatoração Ruby, otimização ou recursos Ruby complexos. |
| <a id="seo-cannibalization-detector"></a>**`@seo-cannibalization-detector`** | `Agent` | `0 Padrões` | Analisa várias páginas fornecidas para identificar sobreposição de palavras-chave e possíveis problemas de canibalização. Sugere estratégias de diferenciação. Use PROATIVAMENTE ao revisar conteúdo semelhante. |
| <a id="seo-content-auditor"></a>**`@seo-content-auditor`** | `Agent` | `0 Padrões` | As análises forneceram conteúdo de qualidade, sinais EAT e práticas recomendadas de SEO. Pontua o conteúdo e fornece recomendações de melhoria com base nas diretrizes estabelecidas. Use PROATIVAMENTE para revisão de conteúdo. |
| <a id="seo-content-refresher"></a>**`@seo-content-refresher`** | `Agent` | `0 Padrões` | Identifica elementos desatualizados no conteúdo fornecido e sugere atualizações para mantê-lo atualizado. Encontra estatísticas, datas e exemplos que precisam ser atualizados. Use PROATIVAMENTE para conteúdo mais antigo. |
| <a id="seo-keyword-strategist"></a>**`@seo-keyword-strategist`** | `Agent` | `0 Padrões` | Analisa o uso de palavras-chave no conteúdo fornecido, calcula a densidade, sugere variações semânticas e palavras-chave LSI com base no tópico. Evita otimização excessiva. Use PROATIVAMENTE para otimização de conteúdo. |
| <a id="test-automator"></a>**`@test-automator`** | `Agent` | `0 Padrões` | Domine a automação de testes baseada em IA com estruturas modernas, testes de autocorreção e engenharia de qualidade abrangente. Crie estratégias de teste escalonáveis ​​com integração avançada de CI/CD. Use PROATIVAMENTE para automação de testes ou garantia de qualidade. |
| <a id="test-engineer"></a>**`@test-engineer`** | `Agent` | `0 Padrões` | Especialista em testes, TDD e automação de testes. Use para escrever testes, melhorar a cobertura e depurar falhas de teste. Aciona teste, especificação, cobertura, brincadeira, pytest, dramaturgo, e2e, teste de unidade. |

---

## <a id="frontend--uiux"></a>Frontend & UI/UX

Total de recursos nesta macro-área: `212`

### <a id="acessibilidade-web-a11y--wcag"></a>Acessibilidade Web (A11y & WCAG)

| Recurso | Tipo | Origem | Descrição e Aplicação |
| :--- | :--- | :--- | :--- |
| <a id="accessibility-compliance"></a>**`accessibility-compliance`** | `Skill` | `0 Padrões` | Implemente interfaces compatíveis com WCAG 2.2 com acessibilidade móvel, padrões de design inclusivos e suporte de tecnologia assistiva. Use ao auditar acessibilidade, implementar padrões ARIA, criar leitores de tela ou garantir experiências de usuário inclusivas. |
| <a id="screen-reader-testing"></a>**`screen-reader-testing`** | `Skill` | `0 Padrões` | Teste aplicativos da web com leitores de tela, incluindo VoiceOver, NVDA e JAWS. Use ao validar a compatibilidade do leitor de tela, depurar problemas de acessibilidade ou garantir suporte de tecnologia assistiva. |
| <a id="accessibility-audit"></a>**`/accessibility-audit`** | `Workflow` | `0 Padrões` | Auditar o código da UI para conformidade com as WCAG |
| <a id="accessibility-expert"></a>**`@accessibility-expert`** | `Agent` | `0 Padrões` | Especialista em acessibilidade garantindo conformidade com WCAG, design inclusivo e compatibilidade com tecnologia assistiva. Domina a otimização do leitor de tela, a navegação pelo teclado e todas as metodologias de teste. Use PROATIVAMENTE ao auditar a acessibilidade, corrigir todos os problemas, criar componentes acessíveis ou garantir experiências de usuário inclusivas. |

### <a id="componentes-de-interface--interação"></a>Componentes de Interface & Interação

| Recurso | Tipo | Origem | Descrição e Aplicação |
| :--- | :--- | :--- | :--- |
| <a id="airflow-dag-patterns"></a>**`airflow-dag-patterns`** | `Skill` | `0 Padrões` | Crie DAGs Apache Airflow de produção com práticas recomendadas para operadores, sensores, testes e implantação. Use ao criar pipelines de dados, orquestrar fluxos de trabalho ou agendar trabalhos em lote. |
| <a id="angular-migration"></a>**`angular-migration`** | `Skill` | `0 Padrões` | Migre de AngularJS para Angular usando modo híbrido, reescrita incremental de componentes e atualizações de injeção de dependência. Use ao atualizar aplicativos AngularJS, planejar migrações de estrutura ou modernizar código Angular legado. |
| <a id="api-design-principles"></a>**`api-design-principles`** | `Skill` | `0 Padrões` | Domine os princípios de design de API REST e GraphQL para criar APIs intuitivas, escaláveis ​​e de fácil manutenção que encantam os desenvolvedores. Use ao projetar novas APIs, revisar especificações de API ou estabelecer padrões de design de API. |
| <a id="app-builder"></a>**`app-builder`** | `Skill` | `0 Padrões` | Principal orquestrador de construção de aplicativos. Cria aplicativos full-stack a partir de solicitações de linguagem natural. Determina o tipo de projeto, seleciona a pilha de tecnologia, coordena os agentes. |
| <a id="architecture"></a>**`architecture`** | `Skill` | `0 Padrões` | Estrutura de tomada de decisão arquitetônica. Análise de requisitos, avaliação de trade-off, documentação ADR. Use ao tomar decisões de arquitetura ou analisar o design do sistema. |
| <a id="architecture-decision-records"></a>**`architecture-decision-records`** | `Skill` | `0 Padrões` | Escreva e mantenha registros de decisões de arquitetura (ADRs) seguindo as melhores práticas para documentação de decisões técnicas. Use ao documentar decisões técnicas significativas, revisar escolhas arquitetônicas anteriores ou estabelecer processos de decisão. |
| <a id="architecture-patterns"></a>**`architecture-patterns`** | `Skill` | `0 Padrões` | Implemente padrões comprovados de arquitetura de back-end, incluindo Arquitetura Limpa, Arquitetura Hexagonal e Design Orientado a Domínio. Use ao arquitetar sistemas back-end complexos ou refatorar aplicativos existentes para melhor manutenção. |
| <a id="auth-implementation-patterns"></a>**`auth-implementation-patterns`** | `Skill` | `0 Padrões` | Padrões mestres de autenticação e autorização, incluindo JWT, OAuth2, gerenciamento de sessão e RBAC para criar sistemas de controle de acesso seguros e escaláveis. Use ao implementar sistemas de autenticação, proteger APIs ou depurar problemas de segurança. |
| <a id="backtesting-frameworks"></a>**`backtesting-frameworks`** | `Skill` | `0 Padrões` | Crie sistemas robustos de backtesting para estratégias de negociação com tratamento adequado de viés de antecipação, viés de sobrevivência e custos de transação. Use ao desenvolver algoritmos de negociação, validar estratégias ou construir infraestrutura de backtesting. |
| <a id="bash-linux"></a>**`bash-linux`** | `Skill` | `0 Padrões` | Padrões de terminal Bash/Linux. Comandos críticos, tubulação, tratamento de erros, scripts. Use ao trabalhar em sistemas macOS ou Linux. |
| <a id="bazel-build-optimization"></a>**`bazel-build-optimization`** | `Skill` | `0 Padrões` | Otimize compilações do Bazel para monorepos em grande escala. Use ao configurar o Bazel, implementar execução remota ou otimizar o desempenho de compilação para bases de código empresariais. |
| <a id="binary-analysis-patterns"></a>**`binary-analysis-patterns`** | `Skill` | `0 Padrões` | Domine padrões de análise binária, incluindo desmontagem, descompilação, análise de fluxo de controle e reconhecimento de padrões de código. Use ao analisar executáveis, compreender código compilado ou realizar análises estáticas em binários. |
| <a id="changelog-automation"></a>**`changelog-automation`** | `Skill` | `0 Padrões` | Automatize a geração de changelog a partir de commits, PRs e releases seguindo o formato Keep a Changelog. Use ao configurar fluxos de trabalho de lançamento, gerar notas de lançamento ou padronizar convenções de commit. |
| <a id="code-review-excellence"></a>**`code-review-excellence`** | `Skill` | `0 Padrões` | Domine práticas eficazes de revisão de código para fornecer feedback construtivo, detectar bugs antecipadamente e promover o compartilhamento de conhecimento, mantendo o moral da equipe. Use ao revisar solicitações pull, estabelecer padrões de revisão ou orientar desenvolvedores. |
| <a id="cqrs-implementation"></a>**`cqrs-implementation`** | `Skill` | `0 Padrões` | Implemente a segregação de responsabilidade de consulta de comando para arquiteturas escaláveis. Use ao separar modelos de leitura e gravação, otimizar o desempenho de consultas ou criar sistemas com origem em eventos. |
| <a id="dbt-transformation-patterns"></a>**`dbt-transformation-patterns`** | `Skill` | `0 Padrões` | Domine dbt (ferramenta de construção de dados) para engenharia analítica com organização de modelos, testes, documentação e estratégias incrementais. Use ao construir transformações de dados, criar modelos de dados ou implementar práticas recomendadas de engenharia analítica. |
| <a id="deployment-pipeline-design"></a>**`deployment-pipeline-design`** | `Skill` | `0 Padrões` | Projete pipelines de CI/CD de vários estágios com portas de aprovação, verificações de segurança e orquestração de implantação. Use ao arquitetar fluxos de trabalho de implantação, configurar a entrega contínua ou implementar práticas de GitOps. |
| <a id="deployment-procedures"></a>**`deployment-procedures`** | `Skill` | `0 Padrões` | Princípios de implantação da produção e tomada de decisão. Fluxos de trabalho de implantação seguros, estratégias de reversão e verificação. Ensina a pensar, não a scripts. |
| <a id="distributed-tracing"></a>**`distributed-tracing`** | `Skill` | `0 Padrões` | Implemente rastreamento distribuído com Jaeger e Tempo para rastrear solicitações em microsserviços e identificar gargalos de desempenho. Use ao depurar microsserviços, analisar fluxos de solicitação ou implementar observabilidade para sistemas distribuídos. |
| <a id="dotnet-backend-patterns"></a>**`dotnet-backend-patterns`** | `Skill` | `0 Padrões` | Domine padrões de desenvolvimento de back-end C#/.NET para criar APIs, servidores MCP e aplicativos corporativos robustos. Abrange assíncrono/espera, injeção de dependência, Entity Framework Core, Dapper, configuração, armazenamento em cache e testes com xUnit. Use ao desenvolver back-ends .NET, revisar código C# ou projetar arquiteturas de API. |
| <a id="embedding-strategies"></a>**`embedding-strategies`** | `Skill` | `0 Padrões` | Selecione e otimize modelos de incorporação para pesquisa semântica e aplicativos RAG. Use ao escolher modelos de incorporação, implementar estratégias de agrupamento ou otimizar a qualidade de incorporação para domínios específicos. |
| <a id="employment-contract-templates"></a>**`employment-contract-templates`** | `Skill` | `0 Padrões` | Crie contratos de trabalho, cartas de oferta e documentos de política de RH seguindo as melhores práticas legais. Use ao redigir contratos de trabalho, criar políticas de RH ou padronizar documentação de emprego. |
| <a id="error-handling-patterns"></a>**`error-handling-patterns`** | `Skill` | `0 Padrões` | Domine padrões de tratamento de erros em linguagens, incluindo exceções, tipos de resultados, propagação de erros e degradação elegante para criar aplicativos resilientes. Use ao implementar o tratamento de erros, projetar APIs ou melhorar a confiabilidade do aplicativo. |
| <a id="event-store-design"></a>**`event-store-design`** | `Skill` | `0 Padrões` | Projete e implemente armazenamentos de eventos para sistemas originados de eventos. Use ao construir infraestrutura de fornecimento de eventos, escolher tecnologias de armazenamento de eventos ou implementar padrões de persistência de eventos. |
| <a id="frontend-design"></a>**`frontend-design`** | `Skill` | `0 Padrões` | Design thinking e tomada de decisão para UI web. Use ao projetar componentes, layouts, esquemas de cores, tipografia ou criar interfaces estéticas. Ensina princípios, não valores fixos. |
| <a id="git-advanced-workflows"></a>**`git-advanced-workflows`** | `Skill` | `0 Padrões` | Domine fluxos de trabalho Git avançados, incluindo rebase, seleção seletiva, bissecção, árvores de trabalho e reflog para manter o histórico limpo e se recuperar de qualquer situação. Use ao gerenciar históricos Git complexos, colaborar em ramificações de recursos ou solucionar problemas de repositório. |
| <a id="github-actions-templates"></a>**`github-actions-templates`** | `Skill` | `0 Padrões` | Crie fluxos de trabalho do GitHub Actions prontos para produção para testes, construção e implantação automatizados de aplicativos. Use ao configurar CI/CD com GitHub Actions, automatizar fluxos de trabalho de desenvolvimento ou criar modelos de fluxo de trabalho reutilizáveis. |
| <a id="gitlab-ci-patterns"></a>**`gitlab-ci-patterns`** | `Skill` | `0 Padrões` | Crie pipelines de CI/CD do GitLab com fluxos de trabalho de vários estágios, armazenamento em cache e executores distribuídos para automação escalonável. Use ao implementar CI/CD do GitLab, otimizar o desempenho do pipeline ou configurar testes e implantação automatizados. |
| <a id="gitops-workflow"></a>**`gitops-workflow`** | `Skill` | `0 Padrões` | Implemente fluxos de trabalho GitOps com ArgoCD e Flux para implantações automatizadas e declarativas do Kubernetes com reconciliação contínua. Use ao implementar práticas de GitOps, automatizar implantações de Kubernetes ou configurar o gerenciamento de infraestrutura declarativa. |
| <a id="godot-gdscript-patterns"></a>**`godot-gdscript-patterns`** | `Skill` | `0 Padrões` | Domine os padrões GDScript do Godot 4, incluindo sinais, cenas, máquinas de estado e otimização. Use ao criar jogos Godot, implementar sistemas de jogos ou aprender as práticas recomendadas de GDScript. |
| <a id="hybrid-cloud-networking"></a>**`hybrid-cloud-networking`** | `Skill` | `0 Padrões` | Configure conectividade segura e de alto desempenho entre infraestrutura local e plataformas em nuvem usando VPN e conexões dedicadas. Use ao criar arquiteturas de nuvem híbrida, conectar data centers à nuvem ou implementar redes seguras entre locais. |
| <a id="hybrid-search-implementation"></a>**`hybrid-search-implementation`** | `Skill` | `0 Padrões` | Combine pesquisa vetorial e por palavra-chave para melhor recuperação. Use ao implementar sistemas RAG, construir mecanismos de busca ou quando nenhuma das abordagens por si só fornece recall suficiente. |
| <a id="i18n-localization"></a>**`i18n-localization`** | `Skill` | `0 Padrões` | Padrões de internacionalização e localização. Detectando strings codificadas, gerenciando traduções, arquivos de localidade, suporte RTL. |
| <a id="istio-traffic-management"></a>**`istio-traffic-management`** | `Skill` | `0 Padrões` | Configure o gerenciamento de tráfego do Istio, incluindo roteamento, balanceamento de carga, disjuntores e implantações canário. Use ao implementar políticas de tráfego de malha de serviço, entrega progressiva ou padrões de resiliência. |
| <a id="javascript-testing-patterns"></a>**`javascript-testing-patterns`** | `Skill` | `0 Padrões` | Implemente estratégias de teste abrangentes usando Jest, Vitest e Testing Library para testes de unidade, testes de integração e testes ponta a ponta com simulação, acessórios e desenvolvimento orientado a testes. Use ao escrever testes JavaScript/TypeScript, configurar infraestrutura de teste ou implementar fluxos de trabalho TDD/BDD. |
| <a id="k8s-manifest-generator"></a>**`k8s-manifest-generator`** | `Skill` | `0 Padrões` | Crie manifestos do Kubernetes prontos para produção para implantações, serviços, ConfigMaps e segredos seguindo as práticas recomendadas e os padrões de segurança. Use ao gerar manifestos YAML do Kubernetes, criar recursos K8s ou implementar configurações do Kubernetes de nível de produção. |
| <a id="k8s-security-policies"></a>**`k8s-security-policies`** | `Skill` | `0 Padrões` | Implemente políticas de segurança do Kubernetes, incluindo NetworkPolicy, PodSecurityPolicy e RBAC, para segurança de nível de produção. Use ao proteger clusters Kubernetes, implementar isolamento de rede ou impor padrões de segurança de pod. |
| <a id="landing-page-copy-optimizer"></a>**`landing-page-copy-optimizer`** | `Skill` | `0 Padrões` | Analise e otimize o texto da landing page usando a metodologia de posicionamento de April Dunford. Use quando o usuário quiser avaliar a cópia da página de destino SaaS, melhorar as mensagens com foco na conversão, aplicar uma estrutura de posicionamento (alternativas competitivas, recursos exclusivos, temas de valor, clientes-alvo, categoria de mercado) ou gerar prompts para ferramentas de codificação de vibração (Replit, Lovable). Aciona solicitações como "analisar minha página de destino", "melhorar a cópia do meu site", "ajuda com posicionamento", "otimizar minha página SaaS" ou quando o usuário compartilha o URL de uma página de destino para revisão. |
| <a id="langchain-architecture"></a>**`langchain-architecture`** | `Skill` | `0 Padrões` | Projete aplicativos LLM usando LangChain 1.x e LangGraph para agentes, memória e integração de ferramentas. Use ao construir aplicativos LangChain, implementar agentes de IA ou criar fluxos de trabalho LLM complexos. |
| <a id="mcp-builder"></a>**`mcp-builder`** | `Skill` | `0 Padrões` | Princípios de construção de servidores MCP (Model Context Protocol). Design de ferramentas, padrões de recursos, melhores práticas. |
| <a id="memory-forensics"></a>**`memory-forensics`** | `Skill` | `0 Padrões` | Domine técnicas forenses de memória, incluindo aquisição de memória, análise de processos e extração de artefatos usando Volatilidade e ferramentas relacionadas. Use ao analisar despejos de memória, investigar incidentes ou realizar análises de malware a partir de capturas de RAM. |
| <a id="microservices-patterns"></a>**`microservices-patterns`** | `Skill` | `0 Padrões` | Projete arquiteturas de microsserviços com limites de serviço, comunicação orientada a eventos e padrões de resiliência. Use ao construir sistemas distribuídos, decompor monólitos ou implementar microsserviços. |
| <a id="ml-pipeline-workflow"></a>**`ml-pipeline-workflow`** | `Skill` | `0 Padrões` | Crie pipelines MLOps completos, desde a preparação de dados até o treinamento de modelo, validação e implantação de produção. Use ao criar pipelines de ML, implementar práticas de MLOps ou automatizar treinamento de modelo e fluxos de trabalho de implantação. |
| <a id="mobile-android-design"></a>**`mobile-android-design`** | `Skill` | `0 Padrões` | Domine os padrões Material Design 3 e Jetpack Compose para criar aplicativos Android nativos. Use ao projetar interfaces Android, implementar a IU do Compose ou seguir as diretrizes de Material Design do Google. |
| <a id="mobile-ios-design"></a>**`mobile-ios-design`** | `Skill` | `0 Padrões` | Domine as diretrizes de interface humana do iOS e os padrões SwiftUI para criar aplicativos iOS nativos. Use ao projetar interfaces iOS, implementar visualizações SwiftUI ou garantir que os aplicativos sigam os princípios de design da Apple. |
| <a id="modern-javascript-patterns"></a>**`modern-javascript-patterns`** | `Skill` | `0 Padrões` | Domine os recursos do ES6+, incluindo assíncrono/espera, desestruturação, operadores de propagação, funções de seta, promessas, módulos, iteradores, geradores e padrões de programação funcionais para escrever código JavaScript limpo e eficiente. Use ao refatorar código legado, implementar padrões modernos ou otimizar aplicativos JavaScript. |
| <a id="multi-cloud-architecture"></a>**`multi-cloud-architecture`** | `Skill` | `0 Padrões` | Projete arquiteturas multinuvem usando uma estrutura de decisão para selecionar e integrar serviços em AWS, Azure e GCP. Use ao criar sistemas multinuvem, evitando a dependência de fornecedores ou aproveitando os melhores serviços de vários provedores. |
| <a id="nft-standards"></a>**`nft-standards`** | `Skill` | `0 Padrões` | Implemente padrões NFT (ERC-721, ERC-1155) com tratamento adequado de metadados, estratégias de cunhagem e integração de mercado. Use ao criar contratos NFT, construir mercados NFT ou implementar sistemas de ativos digitais. |
| <a id="nodejs-backend-patterns"></a>**`nodejs-backend-patterns`** | `Skill` | `0 Padrões` | Crie serviços de back-end Node.js prontos para produção com Express/Fastify, implementando padrões de middleware, tratamento de erros, autenticação, integração de banco de dados e práticas recomendadas de design de API. Use ao criar servidores Node.js, APIs REST, back-ends GraphQL ou arquiteturas de microsserviços. |
| <a id="nodejs-best-practices"></a>**`nodejs-best-practices`** | `Skill` | `0 Padrões` | Princípios de desenvolvimento e tomada de decisões do Node.js. Seleção de estrutura, padrões assíncronos, segurança e arquitetura. Ensina a pensar, não a copiar. |
| <a id="nx-workspace-patterns"></a>**`nx-workspace-patterns`** | `Skill` | `0 Padrões` | Configure e otimize espaços de trabalho Nx monorepo. Use ao configurar o Nx, configurar limites do projeto, otimizar o cache de build ou implementar comandos afetados. |
| <a id="paypal-integration"></a>**`paypal-integration`** | `Skill` | `0 Padrões` | Integre o processamento de pagamentos do PayPal com suporte para check-out expresso, assinaturas e gerenciamento de reembolsos. Use ao implementar pagamentos do PayPal, processar transações on-line ou criar fluxos de checkout de comércio eletrônico. |
| <a id="pci-compliance"></a>**`pci-compliance`** | `Skill` | `0 Padrões` | Implemente os requisitos de conformidade do PCI DSS para o manuseio seguro de dados de cartões de pagamento e sistemas de pagamento. Use ao proteger o processamento de pagamentos, alcançar a conformidade com PCI ou implementar medidas de segurança de cartões de pagamento. |
| <a id="projection-patterns"></a>**`projection-patterns`** | `Skill` | `0 Padrões` | Crie modelos de leitura e projeções a partir de fluxos de eventos. Use ao implementar lados de leitura do CQRS, criar visualizações materializadas ou otimizar o desempenho de consultas em sistemas originados por eventos. |
| <a id="protocol-reverse-engineering"></a>**`protocol-reverse-engineering`** | `Skill` | `0 Padrões` | Domine a engenharia reversa de protocolos de rede, incluindo análise de pacotes, dissecação de protocolos e documentação de protocolos personalizados. Use ao analisar o tráfego de rede, compreender protocolos proprietários ou depurar a comunicação de rede. |
| <a id="python-packaging"></a>**`python-packaging`** | `Skill` | `0 Padrões` | Crie pacotes Python distribuíveis com estrutura de projeto adequada, setup.py/pyproject.toml e publicação em PyPI. Use ao empacotar bibliotecas Python, criar ferramentas CLI ou distribuir código Python. |
| <a id="rag-implementation"></a>**`rag-implementation`** | `Skill` | `0 Padrões` | Crie sistemas de geração aumentada de recuperação (RAG) para aplicativos LLM com bancos de dados vetoriais e pesquisa semântica. Use ao implementar IA baseada em conhecimento, construir sistemas de perguntas e respostas de documentos ou integrar LLMs com bases de conhecimento externas. |
| <a id="requesting-code-review"></a>**`requesting-code-review`** | `Skill` | `0 Padrões` | Use ao concluir tarefas, implementar recursos importantes ou antes de mesclar para verificar se o trabalho atende aos requisitos |
| <a id="responsive-design"></a>**`responsive-design`** | `Skill` | `0 Padrões` | Implemente layouts responsivos modernos usando consultas de contêiner, tipografia fluida, grade CSS e estratégias de ponto de interrupção que priorizam dispositivos móveis. Use ao criar interfaces adaptáveis, implementar layouts fluidos ou criar comportamento responsivo em nível de componente. |
| <a id="risk-metrics-calculation"></a>**`risk-metrics-calculation`** | `Skill` | `0 Padrões` | Calcule métricas de risco do portfólio, incluindo VaR, CVaR, Sharpe, Sortino e análise de rebaixamento. Use ao medir o risco do portfólio, implementar limites de risco ou construir sistemas de monitoramento de risco. |
| <a id="saga-orchestration"></a>**`saga-orchestration`** | `Skill` | `0 Padrões` | Implemente padrões de saga para transações distribuídas e fluxos de trabalho agregados cruzados. Use ao coordenar processos de negócios de várias etapas, lidar com transações de compensação ou gerenciar fluxos de trabalho de longa duração. |
| <a id="security-guidance-plugin"></a>**`security-guidance-plugin`** | `Skill` | `0 Padrões` | Use ao ativar, ajustar ou depurar o plug-in de orientação de segurança do Claude Code que analisa as próprias edições de Claude em busca de vulnerabilidades durante uma sessão, ao adicionar regras ou padrões de segurança personalizados ou ao escrever código que usa eval ou exec, desserialização insegura, injeção de DOM bruto ou arquivos de fluxo de trabalho de CI. Também para avisos de segurança durante a edição. |
| <a id="security-requirement-extraction"></a>**`security-requirement-extraction`** | `Skill` | `0 Padrões` | Obtenha requisitos de segurança de modelos de ameaças e contexto de negócios. Use ao traduzir ameaças em requisitos acionáveis, criar histórias de usuários de segurança ou criar casos de teste de segurança. |
| <a id="service-mesh-observability"></a>**`service-mesh-observability`** | `Skill` | `0 Padrões` | Implemente observabilidade abrangente para malhas de serviço, incluindo rastreamento distribuído, métricas e visualização. Use ao configurar o monitoramento de malha, depurar problemas de latência ou implementar SLOs para comunicação de serviço. |
| <a id="similarity-search-patterns"></a>**`similarity-search-patterns`** | `Skill` | `0 Padrões` | Implemente uma pesquisa eficiente de similaridade com bancos de dados vetoriais. Use ao criar pesquisa semântica, implementar consultas de vizinhos mais próximos ou otimizar o desempenho de recuperação. |
| <a id="sip-astro"></a>**`sip-astro`** | `Skill` | `0 Padrões` | Use sempre que a tarefa atual envolver Astro (construir ou migrar um site, escolher um tema, integrações, SEO/GEO, implantação, formulários, análises, i18n, e-commerce, testes, atualizações, auditoria de pré-lançamento), mas o projeto ativo não possui habilidades Astro locais - ou seja, qualquer projeto diferente do próprio "SIP - Astro". Encaminha a tarefa para o centro central de conhecimento Astro em vez de improvisar a partir do conhecimento geral. Use também quando o usuário perguntar "existe algo de astro pra isso", "tem habilidade de astro no hub" ou nomear explicitamente as habilidades do Astro em um projeto que não seja o hub. |
| <a id="sip-marketing"></a>**`sip-marketing`** | `Skill` | `0 Padrões` | Use sempre que a tarefa atual envolver marketing, conteúdo, copywriting, branding, mídia social, SEO, anúncios pagos, e-mail, RP, crescimento, capacitação de vendas ou análise de marketing, mas o projeto ativo não tiver habilidades de marketing local - ou seja, qualquer projeto que não seja o próprio "SIP - Marketing" (0 Mkt). Encaminha a tarefa para o centro central de conhecimento de marketing, em vez de improvisar a partir do conhecimento geral. Use também quando o usuário perguntar "existe algo de marketing pra isso", "tem habilidade de marketing no hub", "consulta o SIP - Marketing", ou nomear explicitamente uma habilidade, agente ou fluxo de trabalho 0 Mkt em um projeto que não é o hub. |
| <a id="startup-financial-modeling"></a>**`startup-financial-modeling`** | `Skill` | `0 Padrões` | Essa habilidade deve ser usada quando o usuário pede para "criar projeções financeiras", "construir um modelo financeiro", "prever receita", "calcular taxa de consumo", "estimar pista", "modelar fluxo de caixa" ou solicitar planejamento financeiro de 3 a 5 anos para uma startup. |
| <a id="stripe-integration"></a>**`stripe-integration`** | `Skill` | `0 Padrões` | Implemente o processamento de pagamentos Stripe para fluxos de pagamento robustos e compatíveis com PCI, incluindo checkout, assinaturas e webhooks. Use ao integrar pagamentos Stripe, criar sistemas de assinatura ou implementar fluxos de checkout seguros. |
| <a id="superiaprojects-criar-sip"></a>**`superiaprojects-criar-sip`** | `Skill` | `0 Padrões` | Use quando o usuário quiser transformar um projeto/repositório em um "SIP" (Super IA Projects) — um repositório central de Skills, Agents, Workflows e Conhecimento de um domínio que outros projetos possam consultar, quase como um agente especializado daquele domínio. Dispara em pedidos como "cria um SIP de marketing", "transforma esse repo num hub de X", "quero um repositório central pra Y como fizemos com o n8n", ou quando o usuário referencia o `SIP - N8N` como modelo a replicar para um novo domínio. Faz o scaffolding da skill resolver (`sip-<dominio>`), do prompt de instalação, do inbox de contribuições e do registro na ficha do projeto — não cria o conhecimento de domínio em si (isso é trabalho de skills/agents específicos, feitos depois). |
| <a id="tdd-workflow"></a>**`tdd-workflow`** | `Skill` | `0 Padrões` | Princípios de fluxo de trabalho de Desenvolvimento Orientado a Testes. Ciclo VERMELHO-VERDE-REFATOR. |
| <a id="team-composition-analysis"></a>**`team-composition-analysis`** | `Skill` | `0 Padrões` | Essa habilidade deve ser usada quando o usuário solicita "planejar estrutura de equipe", "determinar necessidades de contratação", "projetar organograma", "calcular remuneração", "planejar alocação de capital" ou solicitar design organizacional e planejamento de pessoal para uma startup. |
| <a id="temporal-python-testing"></a>**`temporal-python-testing`** | `Skill` | `0 Padrões` | Teste fluxos de trabalho temporais com estratégias pytest, time-skipping e mocking. Abrange testes unitários, testes de integração, testes de repetição e configuração de desenvolvimento local. Use ao implementar testes de fluxo de trabalho temporal ou depurar falhas de teste. |
| <a id="terraform-module-library"></a>**`terraform-module-library`** | `Skill` | `0 Padrões` | Crie módulos Terraform reutilizáveis ​​para infraestrutura AWS, Azure e GCP seguindo as práticas recomendadas de infraestrutura como código. Use ao criar módulos de infraestrutura, padronizar o provisionamento de nuvem ou implementar componentes IaC reutilizáveis. |
| <a id="typescript-advanced-types"></a>**`typescript-advanced-types`** | `Skill` | `0 Padrões` | Domine o sistema de tipos avançado do TypeScript, incluindo genéricos, tipos condicionais, tipos mapeados, literais de modelo e tipos de utilitários para construir aplicativos com segurança de tipo. Use ao implementar lógica de tipo complexo, criar utilitários de tipo reutilizáveis ​​ou garantir segurança de tipo em tempo de compilação em projetos TypeScript. |
| <a id="ui-ux-pro-max"></a>**`ui-ux-pro-max`** | `Skill` | `0 Padrões` | Inteligência de design UI/UX – estilos, paletas de cores, combinações de fontes, diretrizes UX e regras de raciocínio específicas da pilha. Use ao projetar ou revisar interfaces, páginas iniciais, painéis ou sistemas de design. |
| <a id="unity-ecs-patterns"></a>**`unity-ecs-patterns`** | `Skill` | `0 Padrões` | Domine Unity ECS (Entity Component System) com DOTS, Jobs e Burst para desenvolvimento de jogos de alto desempenho. Use ao criar jogos orientados a dados, otimizar o desempenho ou trabalhar com grandes contagens de entidades. |
| <a id="uv-package-manager"></a>**`uv-package-manager`** | `Skill` | `0 Padrões` | Domine o gerenciador de pacotes uv para gerenciamento rápido de dependências do Python, ambientes virtuais e fluxos de trabalho modernos de projetos do Python. Use ao configurar projetos Python, gerenciar dependências ou otimizar fluxos de trabalho de desenvolvimento Python com uv. |
| <a id="vector-index-tuning"></a>**`vector-index-tuning`** | `Skill` | `0 Padrões` | Otimize o desempenho do índice vetorial para latência, recuperação e memória. Use ao ajustar parâmetros HNSW, selecionar estratégias de quantização ou dimensionar infraestrutura de pesquisa vetorial. |
| <a id="workflow-orchestration-patterns"></a>**`workflow-orchestration-patterns`** | `Skill` | `0 Padrões` | Projete fluxos de trabalho duráveis ​​com Temporal para sistemas distribuídos. Abrange fluxo de trabalho versus separação de atividades, padrões de saga, gerenciamento de estado e restrições de determinismo. Use ao criar processos de longa execução, transações distribuídas ou orquestração de microsserviços. |
| <a id="workflow-patterns"></a>**`workflow-patterns`** | `Skill` | `0 Padrões` | Use esta habilidade ao implementar tarefas de acordo com o fluxo de trabalho TDD do Conductor, lidar com pontos de verificação de fase, gerenciar commits git para tarefas ou compreender o protocolo de verificação. |
| <a id="writing-plans"></a>**`writing-plans`** | `Skill` | `0 Padrões` | Use quando você tiver especificações ou requisitos para uma tarefa de várias etapas, antes de tocar no código |
| <a id="c4-architecture"></a>**`/c4-architecture`** | `Workflow` | `0 Padrões` | Fluxo de trabalho de documentação da arquitetura C4 |
| <a id="ci_describe_pr"></a>**`/ci_describe_pr`** | `Workflow` | `0 Padrões` | Gere descrições abrangentes de PR seguindo modelos de repositório |
| <a id="commit"></a>**`/commit`** | `Workflow` | `0 Padrões` | Crie commits git com aprovação do usuário e sem atribuição de Claude |
| <a id="create"></a>**`/create`** | `Workflow` | `0 Padrões` | Crie um novo comando de aplicativo. Aciona a habilidade do App Builder e inicia um diálogo interativo com o usuário. |
| <a id="create-component"></a>**`/create-component`** | `Workflow` | `0 Padrões` | Criação guiada de componentes com padrões adequados |
| <a id="create_plan"></a>**`/create_plan`** | `Workflow` | `0 Padrões` | Crie planos de implementação detalhados por meio de pesquisa e iteração interativas |
| <a id="create_plan_generic"></a>**`/create_plan_generic`** | `Workflow` | `0 Padrões` | Crie planos de implementação detalhados com pesquisa e iteração completas |
| <a id="create_plan_nt"></a>**`/create_plan_nt`** | `Workflow` | `0 Padrões` | Crie planos de implementação com pesquisa completa (sem diretório de pensamentos) |
| <a id="data-pipeline"></a>**`/data-pipeline`** | `Workflow` | `0 Padrões` | Arquitetura de pipeline de dados |
| <a id="describe_pr"></a>**`/describe_pr`** | `Workflow` | `0 Padrões` | Gere descrições abrangentes de PR seguindo modelos de repositório |
| <a id="describe_pr_nt"></a>**`/describe_pr_nt`** | `Workflow` | `0 Padrões` | Gere descrições abrangentes de PR seguindo modelos de repositório |
| <a id="design-new-component"></a>**`/design-new-component`** | `Workflow` | `0 Padrões` | Desenvolvimento de Componentes |
| <a id="design-review"></a>**`/design-review`** | `Workflow` | `0 Padrões` | Revise a UI existente em busca de problemas e melhorias |
| <a id="financial-projections"></a>**`/financial-projections`** | `Workflow` | `0 Padrões` | Crie um modelo financeiro detalhado de 3 a 5 anos com receitas, custos, fluxo de caixa e cenários |
| <a id="git-workflow"></a>**`/git-workflow`** | `Workflow` | `0 Padrões` | Fluxo de trabalho Git completo com orquestração multiagente |
| <a id="implement"></a>**`/implement`** | `Workflow` | `0 Padrões` | Execute tarefas do plano de implementação de uma faixa seguindo o fluxo de trabalho do TDD |
| <a id="improve-agent"></a>**`/improve-agent`** | `Workflow` | `0 Padrões` | Fluxo de trabalho de otimização de desempenho do agente |
| <a id="iterate_plan"></a>**`/iterate_plan`** | `Workflow` | `0 Padrões` | Repita os planos de implementação existentes com pesquisas e atualizações completas |
| <a id="iterate_plan_nt"></a>**`/iterate_plan_nt`** | `Workflow` | `0 Padrões` | Repita os planos de implementação existentes com pesquisas e atualizações completas |
| <a id="legacy-modernize"></a>**`/legacy-modernize`** | `Workflow` | `0 Padrões` | Fluxo de trabalho de modernização de código legado |
| <a id="manage"></a>**`/manage`** | `Workflow` | `0 Padrões` | Gerenciar o ciclo de vida da trilha: arquivar, restaurar, excluir, renomear e limpar |
| <a id="ml-pipeline"></a>**`/ml-pipeline`** | `Workflow` | `0 Padrões` | Pipeline de aprendizado de máquina - orquestração MLOps multiagente |
| <a id="multi-platform"></a>**`/multi-platform`** | `Workflow` | `0 Padrões` | Fluxo de trabalho de desenvolvimento de recursos multiplataforma |
| <a id="oneshot"></a>**`/oneshot`** | `Workflow` | `0 Padrões` | Bilhete de pesquisa e sessão de planejamento de lançamento |
| <a id="plan"></a>**`/plan`** | `Workflow` | `0 Padrões` | Crie um plano de projeto usando o agente planejador de projeto. Sem gravação de código - apenas planeje a geração de arquivos. |
| <a id="research_codebase_generic"></a>**`/research_codebase_generic`** | `Workflow` | `0 Padrões` | Pesquise a base de código de forma abrangente usando subagentes paralelos |
| <a id="setup"></a>**`/setup`** | `Workflow` | `0 Padrões` | Inicialize o projeto com artefatos do Conductor (definição de produto, pilha de tecnologia, fluxo de trabalho, guias de estilo) |
| <a id="slo-implement"></a>**`/slo-implement`** | `Workflow` | `0 Padrões` | Guia de implementação de SLO |
| <a id="tdd-cycle"></a>**`/tdd-cycle`** | `Workflow` | `0 Padrões` | Execute um fluxo de trabalho abrangente de Desenvolvimento Orientado a Testes (TDD) com rigorosa disciplina de refatoração vermelho-verde |
| <a id="tdd-red"></a>**`/tdd-red`** | `Workflow` | `0 Padrões` | Escreva testes de falha abrangentes seguindo os princípios da fase vermelha do TDD. |
| <a id="ui-ux-pro-max"></a>**`/ui-ux-pro-max`** | `Workflow` | `0 Padrões` | Inteligência de design alimentada por IA com mais de 50 estilos, mais de 95 paletas de cores e geração automatizada de sistemas de design |
| <a id="workflow-automate"></a>**`/workflow-automate`** | `Workflow` | `0 Padrões` | Automação de fluxo de trabalho |
| <a id="ai-engineer"></a>**`@ai-engineer`** | `Agent` | `0 Padrões` | Crie aplicativos LLM prontos para produção, sistemas RAG avançados e agentes inteligentes. Implementa pesquisa vetorial, IA multimodal, orquestração de agentes e integrações de IA empresarial. Use PROATIVAMENTE para recursos LLM, chatbots, agentes de IA ou aplicativos com tecnologia de IA. |
| <a id="architect-review"></a>**`@architect-review`** | `Agent` | `0 Padrões` | Arquiteto de software mestre especializado em padrões de arquitetura moderna, arquitetura limpa, microsserviços, sistemas orientados a eventos e DDD. Revisa projetos de sistema e alterações de código quanto à integridade arquitetônica, escalabilidade e capacidade de manutenção. Use PROATIVAMENTE para decisões arquitetônicas. |
| <a id="backend-architect"></a>**`@backend-architect`** | `Agent` | `0 Padrões` | Arquiteto de back-end especializado em design de API escalonável, arquitetura de microsserviços e sistemas distribuídos. Domina APIs REST/GraphQL/gRPC, arquiteturas orientadas a eventos, padrões de malha de serviço e estruturas de back-end modernas. Lida com a definição de limites de serviço, comunicação entre serviços, padrões de resiliência e observabilidade. Use PROATIVAMENTE ao criar novos serviços de back-end ou APIs. |
| <a id="backend-specialist"></a>**`@backend-specialist`** | `Agent` | `0 Padrões` | Arquiteto de back-end especializado para Node.js, Python e sistemas modernos sem servidor/edge. Use para desenvolvimento de API, lógica do lado do servidor, integração de banco de dados e segurança. Gatilhos em back-end, servidor, API, endpoint, banco de dados, autenticação. |
| <a id="c4-code"></a>**`@c4-code`** | `Agent` | `0 Padrões` | Especialista em documentação em nível de código C4. Analisa diretórios de código para criar documentação abrangente em nível de código C4, incluindo assinaturas de funções, argumentos, dependências e estrutura de código. Use ao documentar código no nível C4 mais baixo para diretórios individuais e módulos de código. |
| <a id="c4-component"></a>**`@c4-component`** | `Agent` | `0 Padrões` | Expert C4 Especialista em documentação em nível de componente. Sintetiza a documentação em nível de código C4 em arquitetura em nível de componente, definindo limites, interfaces e relacionamentos de componentes. Cria diagramas de componentes e documentação. Use ao sintetizar documentação em nível de código em componentes lógicos. |
| <a id="c4-container"></a>**`@c4-container`** | `Agent` | `0 Padrões` | Especialista em documentação em nível de contêiner C4. Sintetiza documentação em nível de componente em arquitetura em nível de contêiner, mapeando componentes para unidades de implantação, documentando interfaces de contêiner como APIs e criando diagramas de contêiner. Use ao sintetizar componentes em contêineres de implantação e documentar a arquitetura de implantação do sistema. |
| <a id="c4-context"></a>**`@c4-context`** | `Agent` | `0 Padrões` | Expert C4 Especialista em documentação em nível de contexto. Cria diagramas de contexto do sistema de alto nível, documenta personas, jornadas do usuário, recursos do sistema e dependências externas. Sintetiza a documentação do contêiner e do componente com a documentação do sistema para criar uma arquitetura abrangente em nível de contexto. Use ao criar a documentação de contexto do sistema C4 de mais alto nível. |
| <a id="cloud-architect"></a>**`@cloud-architect`** | `Agent` | `0 Padrões` | Arquiteto de nuvem especializado em design de infraestrutura multinuvem AWS/Azure/GCP, IaC avançado (Terraform/OpenTofu/CDK), otimização de custos de FinOps e padrões arquitetônicos modernos. Domine sem servidor, microsserviços, segurança, conformidade e recuperação de desastres. Use PROATIVAMENTE para arquitetura de nuvem, otimização de custos, planejamento de migração ou estratégias multinuvem. |
| <a id="codebase-analyzer"></a>**`@codebase-analyzer`** | `Agent` | `0 Padrões` | Analisa detalhes de implementação da base de código. Chame o agente analisador de base de código quando precisar encontrar informações detalhadas sobre componentes específicos. Como sempre, quanto mais detalhado for o seu pedido, melhor! :) |
| <a id="codebase-locator"></a>**`@codebase-locator`** | `Agent` | `0 Padrões` | Localiza arquivos, diretórios e componentes relevantes para um recurso ou tarefa. Chame `codebase-locator` com prompt em linguagem humana descrevendo o que você está procurando. Basicamente, uma "ferramenta Super Grep/Glob/LS" - Use-a se desejar usar uma dessas ferramentas mais de uma vez. |
| <a id="codebase-pattern-finder"></a>**`@codebase-pattern-finder`** | `Agent` | `0 Padrões` | codebase-pattern-finder é um subagent_type útil para encontrar implementações semelhantes, exemplos de uso ou padrões existentes que podem ser modelados. Ele lhe dará exemplos de código concretos com base no que você está procurando! É mais ou menos como o localizador de base de código, mas não apenas informa a localização dos arquivos, mas também fornece detalhes do código! |
| <a id="content-marketer"></a>**`@content-marketer`** | `Agent` | `0 Padrões` | Estrategista de marketing de conteúdo de elite especializado em criação de conteúdo com tecnologia de IA, distribuição omnicanal, otimização de SEO e marketing de desempenho baseado em dados. Domina ferramentas de conteúdo modernas, automação de mídia social e otimização de conversão com as práticas recomendadas para 2024/2025. Use PROATIVAMENTE para marketing de conteúdo abrangente. |
| <a id="context-manager"></a>**`@context-manager`** | `Agent` | `0 Padrões` | Especialista em engenharia de contexto Elite AI que domina o gerenciamento de contexto dinâmico, bancos de dados vetoriais, gráficos de conhecimento e sistemas de memória inteligentes. Orquestra o contexto em fluxos de trabalho multiagentes, sistemas de IA empresariais e projetos de longa duração com as práticas recomendadas para 2024/2025. Use PROATIVAMENTE para orquestração complexa de IA. |
| <a id="data-engineer"></a>**`@data-engineer`** | `Agent` | `0 Padrões` | Crie pipelines de dados escalonáveis, data warehouses modernos e arquiteturas de streaming em tempo real. Implementa Apache Spark, dbt, Airflow e plataformas de dados nativas da nuvem. Use PROATIVAMENTE para design de pipeline de dados, infraestrutura analítica ou implementação moderna de pilha de dados. |
| <a id="data-scientist"></a>**`@data-scientist`** | `Agent` | `0 Padrões` | Cientista de dados especialista em análises avançadas, aprendizado de máquina e modelagem estatística. Lida com análise de dados complexos, modelagem preditiva e inteligência de negócios. Use PROATIVAMENTE para tarefas de análise de dados, modelagem de ML, análise estatística e insights baseados em dados. |
| <a id="database-admin"></a>**`@database-admin`** | `Agent` | `0 Padrões` | Administrador de banco de dados especializado em bancos de dados em nuvem modernos, automação e engenharia de confiabilidade. Domina os serviços de banco de dados AWS/Azure/GCP, infraestrutura como código, alta disponibilidade, recuperação de desastres, otimização de desempenho e conformidade. Lida com estratégias multinuvem, bancos de dados de contêineres e otimização de custos. Use PROATIVAMENTE para arquitetura de banco de dados, operações ou engenharia de confiabilidade. |
| <a id="database-architect"></a>**`@database-architect`** | `Agent` | `0 Padrões` | Arquiteto de banco de dados especialista, especializado em design de camada de dados do zero, seleção de tecnologia, modelagem de esquema e arquiteturas de banco de dados escaláveis. Domina a seleção de bancos de dados SQL/NoSQL/TimeSeries, estratégias de normalização, planejamento de migração e design que prioriza o desempenho. Lida com arquiteturas greenfield e rearquitetura de sistemas existentes. Use PROATIVAMENTE para arquitetura de banco de dados, seleção de tecnologia ou decisões de modelagem de dados. |
| <a id="database-optimizer"></a>**`@database-optimizer`** | `Agent` | `0 Padrões` | Otimizador de banco de dados especializado, especializado em ajuste de desempenho moderno, otimização de consultas e arquiteturas escalonáveis. Domina indexação avançada, resolução N+1, cache multicamadas, estratégias de particionamento e otimização de banco de dados em nuvem. Lida com análises de consultas complexas, estratégias de migração e monitoramento de desempenho. Use PROATIVAMENTE para otimização de banco de dados, problemas de desempenho ou desafios de escalabilidade. |
| <a id="deployment-engineer"></a>**`@deployment-engineer`** | `Agent` | `0 Padrões` | Engenheiro de implantação especializado, especializado em pipelines modernos de CI/CD, fluxos de trabalho GitOps e automação avançada de implantação. Domina GitHub Actions, ArgoCD/Flux, entrega progressiva, segurança de contêiner e engenharia de plataforma. Lida com implantações sem tempo de inatividade, verificação de segurança e otimização da experiência do desenvolvedor. Use PROATIVAMENTE para design de CI/CD, implementação de GitOps ou automação de implantação. |
| <a id="django-pro"></a>**`@django-pro`** | `Agent` | `0 Padrões` | Domine Django 5.x com visualizações assíncronas, DRF, Celery e canais Django. Crie aplicativos da Web escalonáveis ​​com arquitetura, testes e implantação adequados. Use PROATIVAMENTE para desenvolvimento Django, otimização ORM ou padrões Django complexos. |
| <a id="docs-architect"></a>**`@docs-architect`** | `Agent` | `0 Padrões` | Cria documentação técnica abrangente a partir de bases de código existentes. Analisa arquitetura, padrões de design e detalhes de implementação para produzir manuais técnicos e e-books extensos. Use PROATIVAMENTE para documentação do sistema, guias de arquitetura ou aprofundamento técnico. |
| <a id="dotnet-architect"></a>**`@dotnet-architect`** | `Agent` | `0 Padrões` | Arquiteto especialista em back-end .NET especializado em C#, ASP.NET Core, Entity Framework, Dapper e padrões de aplicativos corporativos. Domine assíncrono/espera, injeção de dependência, estratégias de cache e otimização de desempenho. Use PROATIVAMENTE para desenvolvimento de API .NET, revisão de código ou decisões de arquitetura. |
| <a id="dx-optimizer"></a>**`@dx-optimizer`** | `Agent` | `0 Padrões` | Especialista em Experiência do Desenvolvedor. Melhora ferramentas, configuração e fluxos de trabalho. Use PROATIVAMENTE ao configurar novos projetos, após feedback da equipe ou quando for observado atrito no desenvolvimento. |
| <a id="error-detective"></a>**`@error-detective`** | `Agent` | `0 Padrões` | Pesquise logs e bases de código em busca de padrões de erro, rastreamentos de pilha e anomalias. Correlaciona erros entre sistemas e identifica as causas raízes. Use PROATIVAMENTE ao depurar problemas, analisar logs ou investigar erros de produção. |
| <a id="event-sourcing-architect"></a>**`@event-sourcing-architect`** | `Agent` | `0 Padrões` | Event sourcing, CQRS e arquitetura orientada a eventos: design de loja de eventos, projeções, sagas, evolução de esquemas. Use para sistemas originados em eventos. |
| <a id="explorer-agent"></a>**`@explorer-agent`** | `Agent` | `0 Padrões` | Descoberta avançada de base de código, análise arquitetural profunda e agente de pesquisa proativo. Os olhos e ouvidos da estrutura. Use para auditorias iniciais, planos de refatoração e tarefas investigativas profundas. |
| <a id="fastapi-pro"></a>**`@fastapi-pro`** | `Agent` | `0 Padrões` | Crie APIs assíncronas de alto desempenho com FastAPI, SQLAlchemy 2.0 e Pydantic V2. Domine microsserviços, WebSockets e padrões assíncronos modernos do Python. Use PROATIVAMENTE para desenvolvimento FastAPI, otimização assíncrona ou arquitetura de API. |
| <a id="firmware-analyst"></a>**`@firmware-analyst`** | `Agent` | `0 Padrões` | Analista especialista em firmware especializado em sistemas embarcados, segurança IoT e engenharia reversa de hardware. Domina a extração, análise e pesquisa de vulnerabilidades de firmware para roteadores, dispositivos IoT, sistemas automotivos e controladores industriais. Use PROATIVAMENTE para auditorias de segurança de firmware, testes de penetração de IoT ou pesquisas de sistemas embarcados. |
| <a id="flutter-expert"></a>**`@flutter-expert`** | `Agent` | `0 Padrões` | Domine o desenvolvimento do Flutter com Dart 3, widgets avançados e implantação multiplataforma. Lida com gerenciamento de estado, animações, testes e otimização de desempenho para plataformas móveis, web, desktop e incorporadas. Use PROATIVAMENTE para arquitetura Flutter, implementação de UI ou recursos de plataforma cruzada. |
| <a id="frontend-security-coder"></a>**`@frontend-security-coder`** | `Agent` | `0 Padrões` | Especialista em práticas seguras de codificação de front-end, especializado em prevenção de XSS, limpeza de saída e padrões de segurança do lado do cliente. Use PROATIVAMENTE para implementações de segurança de front-end ou revisões de código de segurança do lado do cliente. |
| <a id="golang-pro"></a>**`@golang-pro`** | `Agent` | `0 Padrões` | Master Go 1.21+ com padrões modernos, simultaneidade avançada, otimização de desempenho e microsserviços prontos para produção. Especialista no mais recente ecossistema Go, incluindo genéricos, espaços de trabalho e estruturas de ponta. Use PROATIVAMENTE para desenvolvimento Go, design de arquitetura ou otimização de desempenho. |
| <a id="graphql-architect"></a>**`@graphql-architect`** | `Agent` | `0 Padrões` | Domine o GraphQL moderno com federação, otimização de desempenho e segurança empresarial. Crie esquemas escalonáveis, implemente cache avançado e projete sistemas em tempo real. Use PROATIVAMENTE para arquitetura GraphQL ou otimização de desempenho. |
| <a id="haskell-pro"></a>**`@haskell-pro`** | `Agent` | `0 Padrões` | Engenheiro especialista em Haskell especializado em sistemas de tipo avançado, design funcional puro e software de alta confiabilidade. Use PROATIVAMENTE para programação em nível de tipo, simultaneidade e orientação de arquitetura. |
| <a id="hybrid-cloud-architect"></a>**`@hybrid-cloud-architect`** | `Agent` | `0 Padrões` | Arquiteto especialista em nuvem híbrida, especializado em soluções complexas de múltiplas nuvens em AWS/Azure/GCP e nuvens privadas (OpenStack/VMware). Domina a conectividade híbrida, a otimização do posicionamento da carga de trabalho, a computação de ponta e a automação entre nuvens. Lida com estratégias de conformidade, otimização de custos, recuperação de desastres e migração. Use PROATIVAMENTE para arquitetura híbrida, estratégia multinuvem ou integração de infraestrutura complexa. |
| <a id="ios-developer"></a>**`@ios-developer`** | `Agent` | `0 Padrões` | Desenvolva aplicativos iOS nativos com Swift/SwiftUI. Domina iOS 18, SwiftUI, integração UIKit, Core Data, rede e otimização da App Store. Use PROATIVAMENTE para recursos específicos do iOS, otimização da App Store ou desenvolvimento nativo do iOS. |
| <a id="java-pro"></a>**`@java-pro`** | `Agent` | `0 Padrões` | Domine Java 21+ com recursos modernos como threads virtuais, correspondência de padrões e Spring Boot 3.x. Especialista no mais recente ecossistema Java, incluindo GraalVM, Project Loom e padrões nativos da nuvem. Use PROATIVAMENTE para desenvolvimento Java, arquitetura de microsserviços ou otimização de desempenho. |
| <a id="julia-pro"></a>**`@julia-pro`** | `Agent` | `0 Padrões` | Domine Julia 1.10+ com recursos modernos, otimização de desempenho, despacho múltiplo e práticas prontas para produção. Especialista no ecossistema Julia, incluindo gerenciamento de pacotes, computação científica e código numérico de alto desempenho. Use PROATIVAMENTE para desenvolvimento, otimização ou padrões Julia avançados. |
| <a id="kubernetes-architect"></a>**`@kubernetes-architect`** | `Agent` | `0 Padrões` | Arquiteto especialista em Kubernetes especializado em infraestrutura nativa da nuvem, fluxos de trabalho avançados de GitOps (ArgoCD/Flux) e orquestração de contêineres corporativos. Domine EKS/AKS/GKE, service mesh (Istio/Linkerd), entrega progressiva, multilocação e engenharia de plataforma. Lida com segurança, observabilidade, otimização de custos e experiência do desenvolvedor. Use PROATIVAMENTE para arquitetura K8s, implementação de GitOps ou design de plataforma nativa em nuvem. |
| <a id="legal-advisor"></a>**`@legal-advisor`** | `Agent` | `0 Padrões` | Elabore políticas de privacidade, termos de serviço, isenções de responsabilidade e avisos legais. Cria textos, políticas de cookies e acordos de processamento de dados em conformidade com o GDPR. Use PROATIVAMENTE para documentação legal, textos de conformidade ou requisitos regulatórios. |
| <a id="malware-analyst"></a>**`@malware-analyst`** | `Agent` | `0 Padrões` | Analista especialista em malware, especializado em pesquisa defensiva de malware, inteligência de ameaças e resposta a incidentes. Domina a análise de sandbox, a análise comportamental e a identificação de famílias de malware. Lida com análise estática/dinâmica, descompactação e extração de IOC. Use PROATIVAMENTE para triagem de malware, caça a ameaças, resposta a incidentes ou pesquisa de segurança. |
| <a id="mermaid-expert"></a>**`@mermaid-expert`** | `Agent` | `0 Padrões` | Crie diagramas Mermaid para fluxogramas, sequências, ERDs e arquiteturas. Domina a sintaxe para todos os tipos e estilos de diagramas. Use PROATIVAMENTE para documentação visual, diagramas de sistema ou fluxos de processo. |
| <a id="minecraft-bukkit-pro"></a>**`@minecraft-bukkit-pro`** | `Agent` | `0 Padrões` | Domine o desenvolvimento de plugins de servidor Minecraft com APIs Bukkit, Spigot e Paper. Especializado em arquitetura orientada a eventos, sistemas de comando, manipulação mundial, gerenciamento de jogadores e otimização de desempenho. Use PROATIVAMENTE para arquitetura de plugins, mecânica de jogo, recursos do lado do servidor ou compatibilidade entre versões. |
| <a id="monorepo-architect"></a>**`@monorepo-architect`** | `Agent` | `0 Padrões` | Arquitetura Monorepo, construção de sistemas e gerenciamento de dependências em escala (Nx, Turborepo, Bazel, Lerna). Use para configuração do espaço de trabalho e otimização de CI. |
| <a id="network-engineer"></a>**`@network-engineer`** | `Agent` | `0 Padrões` | Engenheiro de rede especializado em redes modernas em nuvem, arquiteturas de segurança e otimização de desempenho. Domina a conectividade multinuvem, malha de serviço, rede de confiança zero, SSL/TLS, balanceamento de carga global e solução de problemas avançada. Lida com otimização de CDN, automação de rede e conformidade. Use PROATIVAMENTE para projeto de rede, problemas de conectividade ou otimização de desempenho. |
| <a id="observability-engineer"></a>**`@observability-engineer`** | `Agent` | `0 Padrões` | Crie sistemas de monitoramento, registro e rastreamento prontos para produção. Implementa estratégias abrangentes de observabilidade, gerenciamento de SLI/SLO e fluxos de trabalho de resposta a incidentes. Use PROATIVAMENTE para monitorar infraestrutura, otimização de desempenho ou confiabilidade de produção. |
| <a id="payment-integration"></a>**`@payment-integration`** | `Agent` | `0 Padrões` | Integre Stripe, PayPal e processadores de pagamento. Lida com fluxos de checkout, assinaturas, webhooks e conformidade com PCI. Use PROATIVAMENTE ao implementar recursos de pagamentos, cobrança ou assinatura. |
| <a id="python-pro"></a>**`@python-pro`** | `Agent` | `0 Padrões` | Domine Python 3.12+ com recursos modernos, programação assíncrona, otimização de desempenho e práticas prontas para produção. Especialista no mais recente ecossistema Python, incluindo uv, ruff, pydantic e FastAPI. Use PROATIVAMENTE para desenvolvimento, otimização ou padrões avançados de Python. |
| <a id="reference-builder"></a>**`@reference-builder`** | `Agent` | `0 Padrões` | Cria referências técnicas exaustivas e documentação de API. Gera listas abrangentes de parâmetros, guias de configuração e materiais de referência pesquisáveis. Use PROATIVAMENTE para documentos de API, referências de configuração ou especificações técnicas completas. |
| <a id="reverse-engineer"></a>**`@reverse-engineer`** | `Agent` | `0 Padrões` | Engenheiro reverso especializado especializado em análise binária, desmontagem, descompilação e análise de software. Domine IDA Pro, Ghidra, radare2, x64dbg e conjuntos de ferramentas RE modernos. Lida com análise executável, inspeção de biblioteca, extração de protocolo e pesquisa de vulnerabilidades. Use PROATIVAMENTE para análise binária, desafios de CTF, pesquisa de segurança ou compreensão de software não documentado. |
| <a id="rust-pro"></a>**`@rust-pro`** | `Agent` | `0 Padrões` | Master Rust 1.75+ com padrões assíncronos modernos, recursos de sistema de tipo avançado e programação de sistemas prontos para produção. Especialista no mais recente ecossistema Rust, incluindo Tokio, axum e caixas de última geração. Use PROATIVAMENTE para desenvolvimento Rust, otimização de desempenho ou programação de sistemas. |
| <a id="scala-pro"></a>**`@scala-pro`** | `Agent` | `0 Padrões` | Domine o desenvolvimento Scala de nível empresarial com programação funcional, sistemas distribuídos e processamento de big data. Especialista em Apache Pekko, Akka, Spark, ZIO/Cats Effect e arquiteturas reativas. Use PROATIVAMENTE para design de sistema Scala, otimização de desempenho ou integração empresarial. |
| <a id="search-specialist"></a>**`@search-specialist`** | `Agent` | `0 Padrões` | Pesquisador especializado na web usando técnicas avançadas de pesquisa e síntese. Domina operadores de pesquisa, filtragem de resultados e verificação de múltiplas fontes. Lida com análises competitivas e verificação de fatos. Use PROATIVAMENTE para pesquisas profundas, coleta de informações ou análise de tendências. |
| <a id="seo-authority-builder"></a>**`@seo-authority-builder`** | `Agent` | `0 Padrões` | Analisa o conteúdo em busca de sinais EAT e sugere melhorias para construir autoridade e confiança. Identifica elementos de credibilidade ausentes. Use PROATIVAMENTE para tópicos YMYL. |
| <a id="seo-content-writer"></a>**`@seo-content-writer`** | `Agent` | `0 Padrões` | Escreve conteúdo otimizado para SEO com base nas palavras-chave fornecidas e resumos de tópicos. Cria conteúdo envolvente e abrangente seguindo as melhores práticas. Use PROATIVAMENTE para tarefas de criação de conteúdo. |
| <a id="seo-specialist"></a>**`@seo-specialist`** | `Agent` | `0 Padrões` | Especialista em SEO e GEO (Generative Engine Optimization). Lida com auditorias de SEO, Core Web Vitals, otimização EAT, visibilidade de pesquisa de IA. Use para melhorias de SEO, otimização de conteúdo ou estratégias de citação de IA. |
| <a id="seo-structure-architect"></a>**`@seo-structure-architect`** | `Agent` | `0 Padrões` | Analisa e otimiza a estrutura do conteúdo, incluindo hierarquia de cabeçalho, sugere marcação de esquema e oportunidades de links internos. Cria organização de conteúdo amigável para pesquisa. Use PROATIVAMENTE para estruturação de conteúdo. |
| <a id="service-mesh-expert"></a>**`@service-mesh-expert`** | `Agent` | `0 Padrões` | Arquitetura de service mesh com Istio e Linkerd: gerenciamento de tráfego, mTLS, observabilidade, entrega progressiva. Use para redes nativas da nuvem. |
| <a id="startup-analyst"></a>**`@startup-analyst`** | `Agent` | `0 Padrões` | Analista de negócios especialista em startups, especializado em dimensionamento de mercado, modelagem financeira, análise competitiva e planejamento estratégico para empresas em estágio inicial. Use PROATIVAMENTE quando o usuário perguntar sobre oportunidade de mercado, TAM/SAM/SOM, projeções financeiras, economia unitária, cenário competitivo, planejamento de equipe, métricas de startup ou estratégia de negócios para pré-semente através de startups da Série A. |
| <a id="tdd-orchestrator"></a>**`@tdd-orchestrator`** | `Agent` | `0 Padrões` | Orquestrador mestre de TDD especializado em disciplina de refatoração vermelho-verde, coordenação de fluxo de trabalho multiagente e práticas abrangentes de desenvolvimento orientado a testes. Aplica as melhores práticas de TDD entre equipes com testes assistidos por IA e estruturas modernas. Use PROATIVAMENTE para implementação e governança de TDD. |
| <a id="temporal-python-pro"></a>**`@temporal-python-pro`** | `Agent` | `0 Padrões` | Domine a orquestração de fluxo de trabalho temporal com Python SDK. Implementa fluxos de trabalho duráveis, padrões de saga e transações distribuídas. Abrange assíncrono/espera, estratégias de teste e implantação de produção. Use PROATIVAMENTE para design de fluxo de trabalho, orquestração de microsserviços ou processos de longa execução. |
| <a id="terraform-specialist"></a>**`@terraform-specialist`** | `Agent` | `0 Padrões` | Especialista em Terraform/OpenTofu que domina automação IaC avançada, gerenciamento de estado e padrões de infraestrutura empresarial. Lida com design de módulo complexo, implantações em várias nuvens, fluxos de trabalho GitOps, política como código e integração CI/CD. Abrange estratégias de migração, práticas recomendadas de segurança e ecossistemas IaC modernos. Use PROATIVAMENTE para IaC avançado, gerenciamento de estado ou automação de infraestrutura. |
| <a id="thoughts-analyzer"></a>**`@thoughts-analyzer`** | `Agent` | `0 Padrões` | O equivalente de pesquisa do analisador de base de código. Use este subagent_type quando quiser se aprofundar em um tópico de pesquisa. Normalmente não é necessário de outra forma. |
| <a id="thoughts-locator"></a>**`@thoughts-locator`** | `Agent` | `0 Padrões` | Descobre documentos relevantes no diretório pensamentos/ (usamos isso para todos os tipos de armazenamento de metadados!). Isso só é realmente relevante/necessário quando você está com vontade de pesquisar e precisa descobrir se temos pensamentos aleatórios escritos que são relevantes para sua tarefa de pesquisa atual. Com base no nome, imagino que você possa adivinhar que este é o equivalente a `pensamentos` de `codebase-locator` |
| <a id="threat-modeling-expert"></a>**`@threat-modeling-expert`** | `Agent` | `0 Padrões` | Modelagem de ameaças e revisão da arquitetura de segurança: STRIDE, PASTA, árvores de ataque, pontuação de risco, design de mitigação. Use antes de criar recursos sensíveis à segurança. |
| <a id="tutorial-engineer"></a>**`@tutorial-engineer`** | `Agent` | `0 Padrões` | Cria tutoriais passo a passo e conteúdo educacional a partir do código. Transforma conceitos complexos em experiências de aprendizagem progressivas com exemplos práticos. Use PROATIVAMENTE para guias de integração, tutoriais de recursos ou explicações de conceitos. |
| <a id="typescript-pro"></a>**`@typescript-pro`** | `Agent` | `0 Padrões` | Domine TypeScript com tipos avançados, genéricos e segurança de tipo estrita. Lida com sistemas de tipos complexos, decoradores e padrões de nível empresarial. Use PROATIVAMENTE para arquitetura TypeScript, otimização de inferência de tipo ou padrões de digitação avançados. |
| <a id="ui-designer"></a>**`@ui-designer`** | `Agent` | `0 Padrões` | Designer de UI especialista especializado em criação de componentes, sistemas de layout e implementação de design visual. Domina padrões de design modernos, layouts responsivos e fluxos de trabalho de design para código. Use PROATIVAMENTE ao construir componentes de UI, projetar layouts, criar maquetes ou implementar designs visuais. |
| <a id="ui-visual-validator"></a>**`@ui-visual-validator`** | `Agent` | `0 Padrões` | Especialista rigoroso em validação visual, especializado em testes de UI, conformidade de sistemas de design e verificação de acessibilidade. Domine a análise de capturas de tela, testes de regressão visual e validação de componentes. Use PROATIVAMENTE para verificar se as modificações da IU atingiram os objetivos pretendidos por meio de uma análise visual abrangente. |
| <a id="unity-developer"></a>**`@unity-developer`** | `Agent` | `0 Padrões` | Crie jogos Unity com scripts C# otimizados, renderização eficiente e gerenciamento adequado de ativos. Domine Unity 6 LTS, pipelines URP/HDRP e implantação de plataforma cruzada. Lida com sistemas de jogo, implementação de UI e otimização de plataforma. Use PROATIVAMENTE para problemas de desempenho do Unity, mecânica de jogo ou versões de plataforma cruzada. |
| <a id="vector-database-engineer"></a>**`@vector-database-engineer`** | `Agent` | `0 Padrões` | Especialista em bancos de dados vetoriais, estratégias de incorporação e implementação de pesquisa semântica. Masters Pinecone, Weaviate, Qdrant, Milvus e pgvector para aplicações RAG, sistemas de recomendação e pesquisa de similaridade. Use PROATIVAMENTE para implementação de pesquisa vetorial, otimização de incorporação ou sistemas de recuperação semântica. |
| <a id="web-search-researcher"></a>**`@web-search-researcher`** | `Agent` | `0 Padrões` | Você deseja informações nas quais não se sente bem treinado (confiante)? Informações modernas e potencialmente detectáveis ​​apenas na web? Use o subagent_type do pesquisador de pesquisa na web hoje para encontrar toda e qualquer resposta para suas perguntas! Ele pesquisará profundamente para descobrir e tentar responder às suas perguntas! Se você não ficar satisfeito imediatamente, poderá receber seu dinheiro de volta! (Na verdade não - mas você pode executar novamente o web-search-researcher com um prompt alterado caso não fique satisfeito na primeira vez) |

### <a id="design-systems--estilização-moderna"></a>Design Systems & Estilização Moderna

| Recurso | Tipo | Origem | Descrição e Aplicação |
| :--- | :--- | :--- | :--- |
| <a id="design-system-patterns"></a>**`design-system-patterns`** | `Skill` | `0 Padrões` | Crie sistemas de design escaláveis ​​com tokens de design, infraestrutura de temas e padrões de arquitetura de componentes. Use ao criar tokens de design, implementar a troca de temas, construir bibliotecas de componentes ou estabelecer bases de sistemas de design. |
| <a id="design-system-prompts"></a>**`design-system-prompts`** | `Skill` | `0 Padrões` | Uma coleção de prompts e fluxos de trabalho para construir um sistema de design completo, componentes e páginas usando shadcn/ui. |
| <a id="tailwind-design-system"></a>**`tailwind-design-system`** | `Skill` | `0 Padrões` | Crie sistemas de design escalonáveis ​​com Tailwind CSS, tokens de design, bibliotecas de componentes e padrões responsivos. Use ao criar bibliotecas de componentes, implementar sistemas de design ou padronizar padrões de UI. |
| <a id="tailwind-patterns"></a>**`tailwind-patterns`** | `Skill` | `0 Padrões` | Princípios do Tailwind CSS v4. Configuração CSS-first, consultas de contêiner, padrões modernos, arquitetura de token de design. |
| <a id="visual-design-foundations"></a>**`visual-design-foundations`** | `Skill` | `0 Padrões` | Aplique tipografia, teoria das cores, sistemas de espaçamento e princípios de iconografia para criar designs visuais coesos. Use ao estabelecer tokens de design, construir guias de estilo ou melhorar a hierarquia e consistência visual. |
| <a id="design-system-foundation"></a>**`/design-system-foundation`** | `Workflow` | `0 Padrões` | Configuração do sistema de projeto |
| <a id="design-system-setup"></a>**`/design-system-setup`** | `Workflow` | `0 Padrões` | Inicialize um sistema de design com tokens |
| <a id="design-system-architect"></a>**`@design-system-architect`** | `Agent` | `0 Padrões` | Arquiteto de sistemas de design especializado em tokens de design, bibliotecas de componentes, infraestrutura de temas e operações de design escaláveis. Domina a arquitetura de tokens, sistemas multimarcas e colaboração no desenvolvimento de design. Use PROATIVAMENTE ao construir sistemas de design, criar arquiteturas de tokens, implementar temas ou estabelecer bibliotecas de componentes. |
| <a id="frontend-specialist"></a>**`@frontend-specialist`** | `Agent` | `0 Padrões` | Arquiteto Frontend Sênior que constrói sistemas React/Next.js sustentáveis ​​com mentalidade de desempenho em primeiro lugar. Use ao trabalhar em componentes de UI, estilo, gerenciamento de estado, design responsivo ou arquitetura de front-end. Aciona palavras-chave como componente, reagir, vue, ui, ux, css, tailwind, responsivo. |
| <a id="ui-ux-designer"></a>**`@ui-ux-designer`** | `Agent` | `0 Padrões` | Crie designs de interface, wireframes e sistemas de design. Domina pesquisas de usuários, padrões de acessibilidade e ferramentas de design modernas. É especializado em tokens de design, bibliotecas de componentes e design inclusivo. Use PROATIVAMENTE para sistemas de design, fluxos de usuários ou otimização de interface. |

### <a id="frameworks-web-modernos-react--nextjs"></a>Frameworks Web Modernos (React & Next.js)

| Recurso | Tipo | Origem | Descrição e Aplicação |
| :--- | :--- | :--- | :--- |
| <a id="mobile-design"></a>**`mobile-design`** | `Skill` | `0 Padrões` | Pensamento de design e tomada de decisões que priorizam dispositivos móveis para aplicativos iOS e Android. Interação por toque, padrões de desempenho, convenções de plataforma. Ensina princípios, não valores fixos. Use ao criar aplicativos móveis React Native, Flutter ou nativos. |
| <a id="nextjs-app-router-patterns"></a>**`nextjs-app-router-patterns`** | `Skill` | `0 Padrões` | Domine o roteador de aplicativos Next.js 14+ com componentes de servidor, streaming, rotas paralelas e busca avançada de dados. Use ao construir aplicativos Next.js, implementar SSR/SSG ou otimizar componentes do React Server. |
| <a id="nextjs-best-practices"></a>**`nextjs-best-practices`** | `Skill` | `0 Padrões` | Princípios do roteador de aplicativos Next.js. Componentes de servidor, busca de dados, padrões de roteamento. |
| <a id="react-modernization"></a>**`react-modernization`** | `Skill` | `0 Padrões` | Atualize aplicativos React para versões mais recentes, migre de componentes de classe para ganchos e adote recursos simultâneos. Use ao modernizar bases de código do React, migrar para React Hooks ou atualizar para as versões mais recentes do React. |
| <a id="react-native-architecture"></a>**`react-native-architecture`** | `Skill` | `0 Padrões` | Crie aplicativos React Native de produção com Expo, navegação, módulos nativos, sincronização offline e padrões de plataforma cruzada. Use ao desenvolver aplicativos móveis, implementar integrações nativas ou arquitetar projetos React Native. |
| <a id="react-native-design"></a>**`react-native-design`** | `Skill` | `0 Padrões` | Domine o estilo React Native, navegação e animações reanimadas para desenvolvimento móvel multiplataforma. Use ao construir aplicativos React Native, implementar padrões de navegação ou criar animações de alto desempenho. |
| <a id="react-patterns"></a>**`react-patterns`** | `Skill` | `0 Padrões` | Padrões e princípios modernos do React. Ganchos, composição, desempenho, práticas recomendadas de TypeScript. |
| <a id="react-state-management"></a>**`react-state-management`** | `Skill` | `0 Padrões` | Domine o gerenciamento moderno de estado React com Redux Toolkit, Zustand, Jotai e React Query. Use ao configurar o estado global, gerenciar o estado do servidor ou escolher entre soluções de gerenciamento de estado. |
| <a id="web-component-design"></a>**`web-component-design`** | `Skill` | `0 Padrões` | Padrões de componentes Master React, Vue e Svelte, incluindo CSS-in-JS, estratégias de composição e arquitetura de componentes reutilizáveis. Use ao criar bibliotecas de componentes de UI, projetar APIs de componentes ou implementar sistemas de design de front-end. |
| <a id="component-scaffold"></a>**`/component-scaffold`** | `Workflow` | `0 Padrões` | Andaime de componente nativo React/React |
| <a id="frontend-developer"></a>**`@frontend-developer`** | `Agent` | `0 Padrões` | Crie componentes React, implemente layouts responsivos e lide com o gerenciamento de estado do lado do cliente. Masters React 19, Next.js 15 e arquitetura de front-end moderna. Otimiza o desempenho e garante acessibilidade. Use PROATIVAMENTE ao criar componentes de UI ou corrigir problemas de front-end. |
| <a id="mobile-developer"></a>**`@mobile-developer`** | `Agent` | `0 Padrões` | Desenvolva aplicativos móveis React Native, Flutter ou nativos com padrões de arquitetura modernos. Domina o desenvolvimento multiplataforma, integrações nativas, sincronização offline e otimização da loja de aplicativos. Use PROATIVAMENTE para recursos móveis, código de plataforma cruzada ou otimização de aplicativos. |

---

## <a id="gestão-de-produtos-e-projetos"></a>Gestão de Produtos e Projetos

Total de recursos nesta macro-área: `16`

### <a id="conductor--gestão-de-tracks"></a>Conductor & Gestão de Tracks

| Recurso | Tipo | Origem | Descrição e Aplicação |
| :--- | :--- | :--- | :--- |
| <a id="track-management"></a>**`track-management`** | `Skill` | `0 Padrões` | Use esta habilidade ao criar, gerenciar ou trabalhar com trilhas do Conductor - as unidades lógicas de trabalho para recursos, bugs e refatoradores. Aplica-se a operações spec.md, plan.md e track lifecycle. |
| <a id="new-track"></a>**`/new-track`** | `Workflow` | `0 Padrões` | Crie um novo caminho com especificações e plano de implementação em fases |

### <a id="estratégia--especificação-de-produto-prd"></a>Estratégia & Especificação de Produto (PRD)

| Recurso | Tipo | Origem | Descrição e Aplicação |
| :--- | :--- | :--- | :--- |
| <a id="data-driven-feature"></a>**`/data-driven-feature`** | `Workflow` | `0 Padrões` | Desenvolvimento de recursos baseado em dados |
| <a id="feature-development"></a>**`/feature-development`** | `Workflow` | `0 Padrões` | Orquestre o desenvolvimento de recursos de ponta a ponta, desde os requisitos até a implantação em produção |
| <a id="product-manager"></a>**`@product-manager`** | `Agent` | `0 Padrões` | Especialista em requisitos de produtos, histórias de usuários e critérios de aceitação. Use para definir recursos, esclarecer ambiguidades e priorizar o trabalho. Aciona requisitos, história do usuário, critérios de aceitação, especificações do produto. |

### <a id="operações-ágeis--coordenação-de-equipe"></a>Operações Ágeis & Coordenação de Equipe

| Recurso | Tipo | Origem | Descrição e Aplicação |
| :--- | :--- | :--- | :--- |
| <a id="issue"></a>**`/issue`** | `Workflow` | `0 Padrões` | Especialista em resolução de problemas do GitHub |
| <a id="linear"></a>**`/linear`** | `Workflow` | `0 Padrões` | Gerencie tickets lineares - crie, atualize, comente e siga padrões de fluxo de trabalho |
| <a id="onboard"></a>**`/onboard`** | `Workflow` | `0 Padrões` | Você é um **especialista em integração e arquiteto de transferência de conhecimento** com profunda experiência em organizações remotas, integração de equipe técnica e metodologias de aprendizagem acelerada. Sua função é garantir uma integração tranquila e abrangente que transforme novos membros da equipe em colaboradores produtivos, preservando ao mesmo tempo o conhecimento institucional. |
| <a id="standup-notes"></a>**`/standup-notes`** | `Workflow` | `0 Padrões` | Gerador de notas standup |

### <a id="planejamento-de-projetos--sprints"></a>Planejamento de Projetos & Sprints

| Recurso | Tipo | Origem | Descrição e Aplicação |
| :--- | :--- | :--- | :--- |
| <a id="postmortem-writing"></a>**`postmortem-writing`** | `Skill` | `0 Padrões` | Escreva postmortems eficazes e isentos de culpa com análise de causa raiz, cronogramas e itens de ação. Use ao conduzir análises de incidentes, redigir documentos post mortem ou melhorar processos de resposta a incidentes. |
| <a id="founder_mode"></a>**`/founder_mode`** | `Workflow` | `0 Padrões` | Crie ticket linear e PR para recursos experimentais após a implementação |
| <a id="ralph_impl"></a>**`/ralph_impl`** | `Workflow` | `0 Padrões` | Implementar pequenos tickets lineares de maior prioridade com configuração de árvore de trabalho |
| <a id="ralph_plan"></a>**`/ralph_plan`** | `Workflow` | `0 Padrões` | Crie um plano de implementação para ticket linear de prioridade mais alta, pronto para especificações |
| <a id="ralph_research"></a>**`/ralph_research`** | `Workflow` | `0 Padrões` | Pesquise ticket linear de maior prioridade que precisa de investigação |
| <a id="product-owner"></a>**`@product-owner`** | `Agent` | `0 Padrões` | Facilitador estratégico conectando necessidades de negócios e execução técnica. Especialista em elicitação de requisitos, gerenciamento de roadmap e priorização de backlog. Aciona requisitos, história do usuário, backlog, MVP, PRD, partes interessadas. |
| <a id="project-planner"></a>**`@project-planner`** | `Agent` | `0 Padrões` | Agente de planejamento de projetos inteligente. Divide as solicitações do usuário em tarefas, planeja a estrutura de arquivos, determina qual agente faz o quê e cria um gráfico de dependências. Use ao iniciar novos projetos ou planejar recursos importantes. |

---

## <a id="mobile-development"></a>Mobile Development

Total de recursos nesta macro-área: `38`

### <a id="arquitetura-e-padrões-mobile"></a>Arquitetura e Padrões Mobile

| Recurso | Tipo | Origem | Descrição e Aplicação |
| :--- | :--- | :--- | :--- |
| <a id="game-developer"></a>**`@game-developer`** | `Agent` | `0 Padrões` | Desenvolvimento de jogos em todas as plataformas (PC, Web, Mobile, VR/AR). Use ao criar jogos com Unity, Godot, Unreal, Phaser, Three.js ou qualquer mecanismo de jogo. Abrange mecânica de jogo, multijogador, otimização, gráficos 2D/3D e padrões de design de jogos. |
| <a id="mobile-security-coder"></a>**`@mobile-security-coder`** | `Agent` | `0 Padrões` | Especialista em práticas seguras de codificação móvel, especializado em validação de entrada, segurança WebView e padrões de segurança específicos para dispositivos móveis. Use PROATIVAMENTE para implementações de segurança móvel ou revisões de códigos de segurança móvel. |

### <a id="ios--ferramentas-nativas"></a>iOS & Ferramentas Nativas

| Recurso | Tipo | Origem | Descrição e Aplicação |
| :--- | :--- | :--- | :--- |
| <a id="anti-reversing-techniques"></a>**`anti-reversing-techniques`** | `Skill` | `0 Padrões` | Compreenda as técnicas anti-reversão, ofuscação e proteção encontradas durante a análise de software. Use ao analisar binários protegidos, ignorar a antidepuração para análises autorizadas ou compreender mecanismos de proteção de software. |
| <a id="api-patterns"></a>**`api-patterns`** | `Skill` | `0 Padrões` | Princípios de design de API e tomada de decisão. Seleção REST vs GraphQL vs tRPC, formatos de resposta, versionamento, paginação. |
| <a id="attack-tree-construction"></a>**`attack-tree-construction`** | `Skill` | `0 Padrões` | Crie árvores de ataque abrangentes para visualizar caminhos de ameaças. Use ao mapear cenários de ataque, identificar lacunas de defesa ou comunicar riscos de segurança às partes interessadas. |
| <a id="bash-defensive-patterns"></a>**`bash-defensive-patterns`** | `Skill` | `0 Padrões` | Domine técnicas defensivas de programação Bash para scripts de nível de produção. Use ao escrever scripts de shell robustos, pipelines de CI/CD ou utilitários de sistema que exigem tolerância a falhas e segurança. |
| <a id="bats-testing-patterns"></a>**`bats-testing-patterns`** | `Skill` | `0 Padrões` | Master Bash Automated Testing System (Bats) para testes abrangentes de script de shell. Use ao escrever testes para scripts de shell, pipelines de CI/CD ou ao exigir desenvolvimento orientado a testes de utilitários de shell. |
| <a id="claude-security-scan"></a>**`claude-security-scan`** | `Skill` | `0 Padrões` | Use ao verificar um repositório, ramificar diff, solicitar pull ou confirmar vulnerabilidades com o plug-in Claude Security (/claude-security), ler relatórios CLAUDE-SECURITY (md, jsonl, SARIF), transformar descobertas em patches revisados ​​ou escolher entre revisão de segurança, verificação profunda, revisão de código e scanners de CI. Também para varredura de vulnerabilidades. |
| <a id="data-storytelling"></a>**`data-storytelling`** | `Skill` | `0 Padrões` | Transforme dados em narrativas atraentes usando visualização, contexto e estrutura persuasiva. Use ao apresentar análises às partes interessadas, criar relatórios de dados ou criar apresentações executivas. |
| <a id="database-design"></a>**`database-design`** | `Skill` | `0 Padrões` | Princípios de design de banco de dados e tomada de decisão. Design de esquema, estratégia de indexação, seleção de ORM, bancos de dados sem servidor. |
| <a id="documentation-templates"></a>**`documentation-templates`** | `Skill` | `0 Padrões` | Modelos de documentação e diretrizes de estrutura. README, documentos de API, comentários de código e documentação amigável para IA. |
| <a id="intelligent-routing"></a>**`intelligent-routing`** | `Skill` | `0 Padrões` | Seleção automática de agentes e roteamento inteligente de tarefas. Analisa as solicitações dos usuários e seleciona automaticamente o(s) melhor(es) agente(s) especializado(s) sem exigir menções explícitas dos usuários. |
| <a id="kpi-dashboard-design"></a>**`kpi-dashboard-design`** | `Skill` | `0 Padrões` | Projete painéis de KPI eficazes com seleção de métricas, melhores práticas de visualização e padrões de monitoramento em tempo real. Use ao criar painéis de negócios, selecionar métricas ou projetar layouts de visualização de dados. |
| <a id="monorepo-management"></a>**`monorepo-management`** | `Skill` | `0 Padrões` | Domine o gerenciamento de monorepo com espaços de trabalho Turborepo, Nx e pnpm para criar repositórios de vários pacotes eficientes e escaláveis ​​com compilações otimizadas e gerenciamento de dependências. Use ao configurar monorepos, otimizar compilações ou gerenciar dependências compartilhadas. |
| <a id="oss-scout"></a>**`oss-scout`** | `Skill` | `0 Padrões` | Use quando um projeto precisar de um recurso que uma biblioteca ou serviço maduro já possa resolver (login, pagamentos, PDF, datas e fusos horários, rich text, arrastar e soltar), antes de instalar ou recomendar qualquer pacote, ou quando solicitado a estudar, comparar ou participar de projetos de código aberto. |
| <a id="performance-profiling"></a>**`performance-profiling`** | `Skill` | `0 Padrões` | Princípios de perfil de desempenho. Técnicas de medição, análise e otimização. |
| <a id="plan-writing"></a>**`plan-writing`** | `Skill` | `0 Padrões` | Planejamento de tarefas estruturado com detalhamentos, dependências e critérios de verificação claros. Use ao implementar recursos, refatorar ou qualquer trabalho de várias etapas. |
| <a id="python-patterns"></a>**`python-patterns`** | `Skill` | `0 Padrões` | Princípios de desenvolvimento Python e tomada de decisão. Seleção de framework, padrões assíncronos, dicas de tipo, estrutura do projeto. Ensina a pensar, não a copiar. |
| <a id="red-team-tactics"></a>**`red-team-tactics`** | `Skill` | `0 Padrões` | Princípios táticos do time vermelho baseados no MITRE ATT&CK. Fases de ataque, evasão de detecção, relatórios. |
| <a id="seo-fundamentals"></a>**`seo-fundamentals`** | `Skill` | `0 Padrões` | Fundamentos de SEO, EAT, Core Web Vitals e princípios de algoritmo do Google. |
| <a id="server-management"></a>**`server-management`** | `Skill` | `0 Padrões` | Princípios de gerenciamento de servidores e tomada de decisões. Gerenciamento de processos, estratégia de monitoramento e decisões de escala. Ensina a pensar, não a comandar. |
| <a id="sip-mautic"></a>**`sip-mautic`** | `Skill` | `0 Padrões` | Use whenever the current task involves Mautic (contatos, segmentos, campanhas, e-mails, formulários) or Mailgun (envio, webhooks, domínios) but the active project has no local Mautic skills — i.e. any project other than "SIP - Mautic" itself. Routes the task to the central Mautic knowledge hub instead of improvising from general knowledge. Also use when the user asks "existe algo de mautic pra isso", "tem template pra isso no hub", "consulta o SIP - Mautic", or names Mautic/Mailgun explicitly in a project that isn't it. Este stub existe para que IAs que não leem `.claude/skills/` (Google Antigravity/Gemini, Cursor) ainda encontrem este nome via Regra 4 (Fallback Resolution Protocol) — o Claude Code já tem acesso direto via `.claude/skills/sip-mautic`. |
| <a id="startup-metrics-framework"></a>**`startup-metrics-framework`** | `Skill` | `0 Padrões` | Essa habilidade deve ser usada quando o usuário pergunta sobre "principais métricas de inicialização", "métricas de SaaS", "CAC e LTV", "economia unitária", "queima múltipla", "regra dos 40", "métricas de mercado" ou solicita orientação sobre rastreamento e otimização de métricas de desempenho de negócios. |
| <a id="supabase"></a>**`supabase`** | `Skill` | `0 Padrões` | Use quando um projeto cria, lê ou escreve um banco de dados Supabase, configura seu .env, escreve migrações ou quando o proprietário trabalha com vários bancos de dados Supabase (cada um com seu próprio login) e não deve misturá-los. |
| <a id="testing-patterns"></a>**`testing-patterns`** | `Skill` | `0 Padrões` | Testando padrões e princípios. Unidade, integração, estratégias de zombaria. |
| <a id="vulnerability-scanner"></a>**`vulnerability-scanner`** | `Skill` | `0 Padrões` | Princípios avançados de análise de vulnerabilidade. OWASP 2025, Segurança da Cadeia de Suprimentos, mapeamento de superfícies de ataque, priorização de riscos. |
| <a id="webapp-testing"></a>**`webapp-testing`** | `Skill` | `0 Padrões` | Princípios de teste de aplicativos da Web. E2E, Playwright, estratégias de auditoria profunda. |
| <a id="business-case"></a>**`/business-case`** | `Workflow` | `0 Padrões` | Gere um documento de caso de negócios abrangente e pronto para o investidor com mercado, solução, finanças e estratégia |
| <a id="orchestrate"></a>**`/orchestrate`** | `Workflow` | `0 Padrões` | Coordene vários agentes para tarefas complexas. Use para análises multiperspectivas, revisões abrangentes ou tarefas que exigem conhecimentos de domínios diferentes. |
| <a id="test-generate"></a>**`/test-generate`** | `Workflow` | `0 Padrões` | Geração automatizada de testes unitários |
| <a id="validate_plan"></a>**`/validate_plan`** | `Workflow` | `0 Padrões` | Valide a implementação em relação ao plano, verifique os critérios de sucesso, identifique problemas |
| <a id="bash-pro"></a>**`@bash-pro`** | `Agent` | `0 Padrões` | Mestre em scripts Bash defensivos para automação de produção, pipelines de CI/CD e utilitários de sistema. Especialista em scripts de shell seguros, portáteis e testáveis. |
| <a id="business-analyst"></a>**`@business-analyst`** | `Agent` | `0 Padrões` | Domine a análise de negócios moderna com análises baseadas em IA, painéis em tempo real e insights baseados em dados. Crie estruturas abrangentes de KPI, modelos preditivos e recomendações estratégicas. Use PROATIVAMENTE para inteligência de negócios ou análise estratégica. |
| <a id="hr-pro"></a>**`@hr-pro`** | `Agent` | `0 Padrões` | Parceiro de RH profissional e ético para contratação, integração/desligamento, PTO e licença, desempenho, políticas de conformidade e relações com funcionários. Pergunte sobre a jurisdição e o contexto da empresa antes de aconselhar; produzir modelos estruturados, mitigados de preconceitos e legais. |
| <a id="orchestrator"></a>**`@orchestrator`** | `Agent` | `0 Padrões` | Coordenação multiagente e orquestração de tarefas. Use quando uma tarefa exigir múltiplas perspectivas, análise paralela ou execução coordenada em diferentes domínios. Invoque esse agente para tarefas complexas que se beneficiam da experiência combinada em segurança, back-end, front-end, testes e DevOps. |
| <a id="performance-engineer"></a>**`@performance-engineer`** | `Agent` | `0 Padrões` | Engenheiro de desempenho especializado em observabilidade moderna, otimização de aplicativos e desempenho escalável de sistemas. Domina OpenTelemetry, rastreamento distribuído, teste de carga, cache multicamadas, Core Web Vitals e monitoramento de desempenho. Lida com otimização ponta a ponta, monitoramento de usuários reais e padrões de escalabilidade. Use PROATIVAMENTE para desafios de otimização de desempenho, observabilidade ou escalabilidade. |
| <a id="sales-automator"></a>**`@sales-automator`** | `Agent` | `0 Padrões` | Elabore e-mails frios, acompanhamentos e modelos de propostas. Cria páginas de preços, estudos de caso e scripts de vendas. Use PROATIVAMENTE para divulgação de vendas ou nutrição de leads. |
| <a id="seo-content-planner"></a>**`@seo-content-planner`** | `Agent` | `0 Padrões` | Cria contornos de conteúdo abrangentes e grupos de tópicos para SEO. Planeja calendários de conteúdo e identifica lacunas de tópicos. Use PROATIVAMENTE para estratégia e planejamento de conteúdo. |

---

## <a id="processos-de-vibecoding--metodologia-ia"></a>Processos de VibeCoding & Metodologia IA

Total de recursos nesta macro-área: `24`

### <a id="auditoria-anti-slop--segurança-vibecoding"></a>Auditoria Anti-Slop & Segurança VibeCoding

| Recurso | Tipo | Origem | Descrição e Aplicação |
| :--- | :--- | :--- | :--- |
| <a id="vibecoding-security-audit"></a>**`vibecoding-security-audit`** | `Skill` | `0 Padrões` | Use quando um aplicativo criado ou editado com IA precisar de um passe de segurança antes do envio - segredos expostos, segurança em nível de linha Supabase, autenticação e sessões, uploads de usuários, uma nova dependência sugerida por uma IA ou IA e rotas com preço de uso que podem custar uma conta. Também para solicitações de "auditoria de segurança" ou "auditoria de segurança vibecoding". |

### <a id="engenharia-de-contexto--memória"></a>Engenharia de Contexto & Memória

| Recurso | Tipo | Origem | Descrição e Aplicação |
| :--- | :--- | :--- | :--- |
| <a id="context-driven-development"></a>**`context-driven-development`** | `Skill` | `0 Padrões` | Use essa habilidade ao trabalhar com a metodologia de desenvolvimento orientada ao contexto do Conductor, gerenciando artefatos de contexto do projeto ou entendendo o relacionamento entre os arquivos product.md, tech-stack.md e workflow.md. |
| <a id="context-restore"></a>**`/context-restore`** | `Workflow` | `0 Padrões` | Restauração de contexto: reidratação avançada de memória semântica |
| <a id="context-save"></a>**`/context-save`** | `Workflow` | `0 Padrões` | Ferramenta de salvamento de contexto: especialista em gerenciamento inteligente de contexto |

### <a id="orquestração-de-agentes--superpoderes"></a>Orquestração de Agentes & Superpoderes

| Recurso | Tipo | Origem | Descrição e Aplicação |
| :--- | :--- | :--- | :--- |
| <a id="behavioral-modes"></a>**`behavioral-modes`** | `Skill` | `0 Padrões` | Modos operacionais de IA (brainstorm, implementar, depurar, revisar, ensinar, enviar, orquestrar). Use para adaptar o comportamento com base no tipo de tarefa. |
| <a id="diagnosing-superpowers"></a>**`diagnosing-superpowers`** | `Skill` | `0 Padrões` | Use quando uma sessão de superpoderes deu errado e seu parceiro humano quiser saber o porquê - trabalho repetido, planos ignorados, tropeços, resultados ruins, uma habilidade que não disparou, "demorou muito", "por que é tão caro", "o que está fazendo" - ou deseja construir um relatório de bug para os mantenedores dos superpoderes, para a sessão atual ou anterior identificada por id ou caminho, em qualquer equipamento. |
| <a id="dispatching-parallel-agents"></a>**`dispatching-parallel-agents`** | `Skill` | `0 Padrões` | Use ao enfrentar mais de 2 tarefas independentes que podem ser trabalhadas sem estado compartilhado ou dependências sequenciais |
| <a id="parallel-agents"></a>**`parallel-agents`** | `Skill` | `0 Padrões` | Padrões de orquestração multiagentes. Use quando diversas tarefas independentes puderem ser executadas com conhecimentos de domínio diferentes ou quando uma análise abrangente exigir diversas perspectivas. |
| <a id="spec-writing"></a>**`spec-writing`** | `Skill` | `0 Padrões` | Use quando um recurso ou mudança precisar de uma especificação escrita – problema, solução, histórias de usuários, decisões – antes do início do planejamento ou implementação, transformando o que já foi discutido em um documento concreto em vez de um entendimento compartilhado implícito. |
| <a id="subagent-driven-development"></a>**`subagent-driven-development`** | `Skill` | `0 Padrões` | Use ao executar planos de implementação com tarefas independentes na sessão atual |
| <a id="using-superpowers"></a>**`using-superpowers`** | `Skill` | `0 Padrões` | Use ao iniciar qualquer conversa - estabelece como encontrar e usar habilidades, exigindo a invocação de habilidades antes de QUALQUER resposta, incluindo esclarecimento de perguntas |
| <a id="error-analysis"></a>**`/error-analysis`** | `Workflow` | `0 Padrões` | Análise e resolução de erros |
| <a id="error-trace"></a>**`/error-trace`** | `Workflow` | `0 Padrões` | Rastreamento e monitoramento de erros |
| <a id="smart-debug"></a>**`/smart-debug`** | `Workflow` | `0 Padrões` | Você é um especialista em depuração assistida por IA com profundo conhecimento de ferramentas modernas de depuração, plataformas de observabilidade e causa raiz automatizada. |
| <a id="smart-fix"></a>**`/smart-fix`** | `Workflow` | `0 Padrões` | Resolução inteligente de problemas com orquestração multiagente |

### <a id="padrões-fundamentais--ciclo-de-execução"></a>Padrões Fundamentais & Ciclo de Execução

| Recurso | Tipo | Origem | Descrição e Aplicação |
| :--- | :--- | :--- | :--- |
| <a id="clean-code"></a>**`clean-code`** | `Skill` | `0 Padrões` | Padrões de codificação pragmáticos – concisos, diretos, sem excesso de engenharia, sem comentários desnecessários |
| <a id="execution-loop"></a>**`execution-loop`** | `Skill` | `0 Padrões` | Use ao iniciar um novo recurso não trivial, construção, refatoração ou mudança significativa que precise de um ciclo de desenvolvimento documentado e com controle de qualidade — também chamado de "Loop de Execução" — antes de escrever o código de implementação. |
| <a id="project-defines"></a>**`project-defines`** | `Skill` | `0 Padrões` | Use quando um novo aplicativo ou sistema deve ser planejado, especificado e construído passo a passo, quando um projeto contém uma pasta _projectdefines/ e algo está prestes a ser construído, alterado ou revisado, ou quando um proprietário que não programa precisa de um caminho de construção seguro e enxuto. |
| <a id="project-initializer"></a>**`project-initializer`** | `Skill` | `0 Padrões` | Use ao iniciar um novo projeto do zero, quando o usuário disser "Quero criar um projeto novo com base na habilidade", ou quando solicitado a inicializar a configuração do projeto greenfield. |
| <a id="session-handoff"></a>**`session-handoff`** | `Skill` | `0 Padrões` | Use ao encerrar uma sessão com trabalho inacabado que outra sessão precisará continuar ou ao iniciar uma sessão que retoma a transferência de outra pessoa (ou do seu próprio passado) — captura o status da tarefa, as decisões, os aprendizados e as próximas etapas sem perder o contexto. |
| <a id="writing-skills"></a>**`writing-skills`** | `Skill` | `0 Padrões` | Use ao criar novas habilidades, editar habilidades existentes ou verificar o funcionamento das habilidades antes da implantação |

### <a id="portão-socrático--descoberta"></a>Portão Socrático & Descoberta

| Recurso | Tipo | Origem | Descrição e Aplicação |
| :--- | :--- | :--- | :--- |
| <a id="brainstorming"></a>**`brainstorming`** | `Skill` | `0 Padrões` | Use quando estiver prestes a criar recursos, construir componentes, adicionar funcionalidades, modificar comportamento ou planejar algo novo, no software ou fora dele, e quando uma solicitação for complexa, vaga ou pouco clara - o Portão Socrático, antes de qualquer uso ou implementação de ferramenta |
| <a id="brainstorm"></a>**`/brainstorm`** | `Workflow` | `0 Padrões` | Você DEVE usar isso antes de qualquer trabalho criativo - criar recursos, construir componentes, adicionar funcionalidades ou modificar comportamento. Explora requisitos e design antes da implementação. |

### <a id="resolução-e-descoberta-de-skills"></a>Resolução e Descoberta de Skills

| Recurso | Tipo | Origem | Descrição e Aplicação |
| :--- | :--- | :--- | :--- |
| <a id="skill-resolver"></a>**`skill-resolver`** | `Skill` | `0 Padrões` | Use whenever a capability seems relevant to the current task but no matching skill appears in the currently loaded skills list — this is common in Antigravity Kit projects (any repo with a .agent/skills/ directory, a .agent/rules/ directory, or a CLAUDE.md/GEMINI.md that references "0 Padrões"), because Claude Code only auto-discovers SKILL.md files under .claude/skills/ and ~/.claude/skills/, never under .agent/skills/. Also use when the user names a skill by name that doesn't show up in the listing, or asks things like "existe skill pra isso", "do we have a skill for X", "check 0 Padrões for a skill". Searches the project's own .agent/skills/ (and .agents/skills/ for older, unmigrated setups), then the global library at 0 Padrões/.agent/skills/, then 0 Mkt/ for marketing, SEO, copywriting or growth topics. |

---

## <a id="segurança--compliance"></a>Segurança & Compliance

Total de recursos nesta macro-área: `4`

### <a id="compliance-regulatória--privacidade"></a>Compliance Regulatória & Privacidade

| Recurso | Tipo | Origem | Descrição e Aplicação |
| :--- | :--- | :--- | :--- |
| <a id="compliance-check"></a>**`/compliance-check`** | `Workflow` | `0 Padrões` | Verificação de conformidade regulatória |

### <a id="modelagem-de-ameaças--red-team"></a>Modelagem de Ameaças & Red Team

| Recurso | Tipo | Origem | Descrição e Aplicação |
| :--- | :--- | :--- | :--- |
| <a id="stride-analysis-patterns"></a>**`stride-analysis-patterns`** | `Skill` | `0 Padrões` | Aplique a metodologia STRIDE para identificar ameaças sistematicamente. Use ao analisar a segurança do sistema, conduzir sessões de modelagem de ameaças ou criar documentação de segurança. |

### <a id="varredura-sast--prevenção-de-falhas"></a>Varredura SAST & Prevenção de Falhas

| Recurso | Tipo | Origem | Descrição e Aplicação |
| :--- | :--- | :--- | :--- |
| <a id="solidity-security"></a>**`solidity-security`** | `Skill` | `0 Padrões` | Domine as práticas recomendadas de segurança de contratos inteligentes para evitar vulnerabilidades comuns e implementar padrões seguros do Solidity. Use ao escrever contratos inteligentes, auditar contratos existentes ou implementar medidas de segurança para aplicações blockchain. |
| <a id="xss-scan"></a>**`/xss-scan`** | `Workflow` | `0 Padrões` | Scanner de vulnerabilidade XSS para código front-end |

---

## <a id="testing--quality-assurance"></a>Testing & Quality Assurance

Total de recursos nesta macro-área: `11`

### <a id="automação-de-testes-e2e--web"></a>Automação de Testes E2E & Web

| Recurso | Tipo | Origem | Descrição e Aplicação |
| :--- | :--- | :--- | :--- |
| <a id="e2e-testing-patterns"></a>**`e2e-testing-patterns`** | `Skill` | `0 Padrões` | Domine os testes ponta a ponta com Playwright e Cypress para criar suítes de testes confiáveis ​​que detectam bugs, melhoram a confiança e permitem implantação rápida. Use ao implementar testes E2E, depurar testes instáveis ​​ou estabelecer padrões de teste. |

### <a id="desenvolvimento-orientado-a-testes-tdd"></a>Desenvolvimento Orientado a Testes (TDD)

| Recurso | Tipo | Origem | Descrição e Aplicação |
| :--- | :--- | :--- | :--- |
| <a id="tdd-green"></a>**`/tdd-green`** | `Workflow` | `0 Padrões` | Implemente código mínimo para fazer testes com falha passarem na fase verde do TDD |
| <a id="tdd-refactor"></a>**`/tdd-refactor`** | `Workflow` | `0 Padrões` | Refatore o código com confiança usando uma rede de segurança de teste abrangente |

### <a id="testes-unitários--integração"></a>Testes Unitários & Integração

| Recurso | Tipo | Origem | Descrição e Aplicação |
| :--- | :--- | :--- | :--- |
| <a id="ponytail-audit"></a>**`ponytail-audit`** | `Skill` | `0 Padrões` | Quality audit of a whole repo: bugs, security holes, what breaks under real load, risky code without tests, slow paths, and what to delete, merge or split. Ranked, each finding explained in plain English. One-shot report, changes nothing. Use for "audit this codebase", "review the whole repo", "find bloat", "what can I delete", /ponytail-audit. |
| <a id="ponytail-review"></a>**`ponytail-review`** | `Skill` | `0 Padrões` | Quality review of a change: is the logic right, is it safe, does it hold under real load, is risky code tested, is it fast enough, and is every line needed. Reads the connected code, not only the diff. Each finding is explained in plain English. Use for "review this", "code review", "review the last commit", "review my PR", "is this over-engineered", /ponytail-review. |
| <a id="sast-configuration"></a>**`sast-configuration`** | `Skill` | `0 Padrões` | Configure ferramentas de teste estático de segurança de aplicativos (SAST) para detecção automatizada de vulnerabilidades no código do aplicativo. Use ao configurar a verificação de segurança, implementar práticas de DevSecOps ou automatizar a detecção de vulnerabilidades de código. |
| <a id="systematic-debugging"></a>**`systematic-debugging`** | `Skill` | `0 Padrões` | Use ao encontrar qualquer bug, falha de teste ou comportamento inesperado, antes de propor correções |
| <a id="test-driven-development"></a>**`test-driven-development`** | `Skill` | `0 Padrões` | Use ao implementar qualquer recurso ou correção de bug, antes de escrever o código de implementação |
| <a id="wcag-audit-patterns"></a>**`wcag-audit-patterns`** | `Skill` | `0 Padrões` | Conduza auditorias de acessibilidade WCAG 2.2 com testes automatizados, verificação manual e orientações de correção. Use ao auditar sites quanto à acessibilidade, corrigir violações das WCAG ou implementar padrões de design acessíveis. |
| <a id="security-sast"></a>**`/security-sast`** | `Workflow` | `0 Padrões` | Teste estático de segurança de aplicativos (SAST) para análise de vulnerabilidade de código em várias linguagens e estruturas |
| <a id="test"></a>**`/test`** | `Workflow` | `0 Padrões` | Geração de teste e comando de execução de teste. Cria e executa testes de código. |

---

## <a id="ads-tráfego-pago-ads"></a>ads (Tráfego Pago (Ads))

Total de recursos nesta macro-área: `9`

### <a id="analise-de-desempenho"></a>Analise De Desempenho

| Recurso | Tipo | Origem | Descrição e Aplicação |
| :--- | :--- | :--- | :--- |
| <a id="ads-analise-de-desempenho"></a>**`ads-analise-de-desempenho`** | `Skill` | `0 Mkt` | O cérebro financeiro e analítico do tráfego pago. Aloca verba entre múltiplos canais (Google, Meta, LinkedIn) baseado em MER/CAC, audita e diagnostica desvios de CPA, caça desperdícios orçamentários (Wasted Spend), implementa regras de corte automático (Auto-Pause), projeta ROAS e gera parâmetros de rastreamento UTM padronizados. Use para decidir onde e quanto investir em mídia paga e para analisar, comparar e vigiar o resultado de Google e Meta juntos (estratégia, diagnóstico, orçamento, pacing e relatório). NÃO use para montar o plano ou o brief de uma campanha (use revenue-campanhas), relatório executivo e modelagem de atribuição para a liderança (use data-atribuicao-e-relatorios), criação de anúncios (use ads-criativos ou ads-copy-de-anuncio) nem configuração de contas (use ads-google ou ads-meta). |

### <a id="copy-de-anuncio"></a>Copy De Anuncio

| Recurso | Tipo | Origem | Descrição e Aplicação |
| :--- | :--- | :--- | :--- |
| <a id="ads-copy-de-anuncio"></a>**`ads-copy-de-anuncio`** | `Skill` | `0 Mkt` | Use para escrever o texto dos anúncios pagos: títulos e descrições de Google Search (RSA), textos primários curtos e longos de Meta Ads, roteiros de TikTok Ads e anúncios de LinkedIn Ads, com matriz de testes de copy. Gatilhos: \"copy de anúncio\", \"RSA\", \"texto primário\", \"variações de anúncio\". NÃO use para conceito e formato do criativo em vídeo ou imagem (use ads-criativos), para decidir verba e analisar resultado (use ads-analise-de-desempenho) nem para configurar a conta (use ads-google ou ads-meta). |
| <a id="ads-copy-de-anuncio"></a>**`/ads-copy-de-anuncio`** | `Workflow` | `0 Mkt` | Gere textos de anúncios de alta conversão para Google Ads, Meta (Facebook/Instagram), LinkedIn e TikTok. Cria múltiplas variações com testes A/B em mente. Inclui títulos, descrições, CTAs e formatos específicos da plataforma. Use ao criar anúncios, gerar variações de anúncios ou testar A/B o texto do anúncio. |

### <a id="criativos"></a>Criativos

| Recurso | Tipo | Origem | Descrição e Aplicação |
| :--- | :--- | :--- | :--- |
| <a id="ads-criativos"></a>**`ads-criativos`** | `Skill` | `0 Mkt` | Use para conceber, roteirizar e validar criativos de mídia paga (vídeo UGC, motion, estáticos), combater fadiga de criativo, analisar anúncios de concorrentes e montar pipelines de anúncio com IA generativa. Gatilhos: \"criativo de anúncio\", \"UGC\", \"fadiga de criativo\", \"ad spy\". NÃO use para escrever o texto do anúncio (use ads-copy-de-anuncio), para alocar verba e diagnosticar CPA (use ads-analise-de-desempenho) nem para configurar contas (use ads-google ou ads-meta). |

### <a id="extracao-de-anuncios-concorrentes"></a>Extracao De Anuncios Concorrentes

| Recurso | Tipo | Origem | Descrição e Aplicação |
| :--- | :--- | :--- | :--- |
| <a id="ads-extracao-de-anuncios-concorrentes"></a>**`/ads-extracao-de-anuncios-concorrentes`** | `Workflow` | `0 Mkt` | Extrai e analisa anúncios de concorrentes de bibliotecas de anúncios (Facebook, LinkedIn, etc.) para entender quais mensagens, problemas e abordagens criativas estão funcionando. Ajuda a inspirar e melhorar suas próprias campanhas publicitárias. |

### <a id="google"></a>Google

| Recurso | Tipo | Origem | Descrição e Aplicação |
| :--- | :--- | :--- | :--- |
| <a id="ads-google"></a>**`ads-google`** | `Skill` | `0 Mkt` | Use para estruturar e otimizar contas de Google Ads (Search, Performance Max, YouTube, Display): arquitetura temática, mineração de termos de busca, Quality Score, canibalização de palavras-chave, extensões e lances inteligentes. Gatilhos: \"Google Ads\", \"PMax\", \"termos de busca\", \"Quality Score\", \"Smart Bidding\". NÃO use para Meta Ads (use ads-meta), LinkedIn, TikTok e Reddit (use ads-multiplataforma), texto do anúncio (use ads-copy-de-anuncio) nem para decidir verba entre canais (use ads-analise-de-desempenho). |

### <a id="meta"></a>Meta

| Recurso | Tipo | Origem | Descrição e Aplicação |
| :--- | :--- | :--- | :--- |
| <a id="ads-meta"></a>**`ads-meta`** | `Skill` | `0 Mkt` | Use para estruturar e otimizar contas de Meta Ads (Facebook e Instagram): Advantage+, CBO e ABO, públicos Broad e Lookalike, sobreposição de públicos, retargeting por janela e controle de frequência. Gatilhos: \"Meta Ads\", \"Facebook Ads\", \"Instagram Ads\", \"lookalike\", \"CBO\". NÃO use para Google Ads (use ads-google), LinkedIn, TikTok e Reddit (use ads-multiplataforma), texto do anúncio (use ads-copy-de-anuncio) nem para decidir verba entre canais (use ads-analise-de-desempenho). |

### <a id="multiplataforma"></a>Multiplataforma

| Recurso | Tipo | Origem | Descrição e Aplicação |
| :--- | :--- | :--- | :--- |
| <a id="ads-multiplataforma"></a>**`ads-multiplataforma`** | `Skill` | `0 Mkt` | Use para planejar mídia paga fora do Google e do Meta: LinkedIn Ads para ABM e prospecção B2B de ticket alto, TikTok Ads, Reddit Ads e especificações técnicas por plataforma. Gatilhos: \"LinkedIn Ads\", \"TikTok Ads\", \"Reddit Ads\", \"ABM pago\". NÃO use para Google Ads (use ads-google), Meta Ads (use ads-meta) nem para alocar verba entre canais (use ads-analise-de-desempenho). |

### <a id="trafego-pago"></a>Trafego Pago

| Recurso | Tipo | Origem | Descrição e Aplicação |
| :--- | :--- | :--- | :--- |
| <a id="ads-trafego-pago"></a>**`@ads-trafego-pago`** | `Agent` | `0 Mkt` | Especialista em gestão de tráfego pago, mídia de performance e aquisição de clientes. Use quando precisar planejar, estruturar, analisar ou otimizar campanhas de anúncios em Google Ads, Meta Ads (Facebook/Instagram), TikTok Ads, LinkedIn Ads ou redes alternativas, com foco em CAC, ROAS e escala rentável.\\n\\n<example>\\nContext: O usuário precisa estruturar uma campanha de lançamento de infoproduto ou SaaS no Meta Ads.\\nuser: \"Como devo estruturar a campanha de tráfego pago para o lançamento da <marca> no Meta?\"\\nassistant: \"Vou acionar o ads-trafego-pago para desenhar a arquitetura de campanha no Meta Ads com distribuição CBO, públicos Broad e testes de criativos.\"\\n<commentary>\\nA demanda exige estratégia avançada de tráfego pago, delegando ao especialista de mídia de performance.\\n</commentary>\\n</example>\\n\\n<example>\\nContext: O CPA de uma campanha de Google Search subiu e o usuário precisa de um plano de otimização.\\nuser: \"Nosso custo por lead no Google Ads dobrou esta semana. Pode auditar os termos de busca?\"\\nassistant: \"Acionando o ads-trafego-pago para conduzir uma auditoria de Search Term Mining e Quality Score no Google Ads.\"\\n<commentary>\\nDiagnóstico de performance e redução de desperdício em mídia paga.\\n</commentary>\\n</example> |

---

## <a id="audiovisual-mídia--audiovisual"></a>audiovisual (Mídia & Audiovisual)

Total de recursos nesta macro-área: `25`

### <a id="agentes-de-voz"></a>Agentes De Voz

| Recurso | Tipo | Origem | Descrição e Aplicação |
| :--- | :--- | :--- | :--- |
| <a id="audiovisual-agentes-de-voz"></a>**`audiovisual-agentes-de-voz`** | `Skill` | `0 Mkt` | Use para criar agentes conversacionais de voz com a plataforma ElevenLabs: SDR de voz para prospecção e qualificação, atendimento ao cliente, bots telefônicos e experiências interativas em tempo real. Gatilhos: \"agente de voz\", \"SDR de voz\", \"bot telefônico\", \"ElevenLabs agents\". NÃO use para transcrever áudio (use audiovisual-transcricao), editar ou masterizar podcast (use audiovisual-podcast-e-audio) nem para cadência de e-mail ou ligação sem voz sintética (use vendas-cold-email). |

### <a id="apresentacoes-educacionais"></a>Apresentacoes Educacionais

| Recurso | Tipo | Origem | Descrição e Aplicação |
| :--- | :--- | :--- | :--- |
| <a id="audiovisual-apresentacoes-educacionais"></a>**`audiovisual-apresentacoes-educacionais`** | `Skill` | `0 Mkt` | Use para planejar, melhorar e validar apresentações de ensino: aula, treinamento, workshop, webinar e palestra, com ciência da aprendizagem (carga cognitiva, 12 princípios de Mayer, 9 eventos de Gagné, design C.R.A.P.) e acessibilidade (WCAG 2.1 AA). Gatilhos: \"slides de aula\", \"apresentação de treinamento\", \"workshop\", \"webinar\", \"slides que ensinam\", \"revisar meus slides\". NÃO use para pitch de investidor ou deck de venda (use audiovisual-pitch-deck), para slides de código em Markdown (use audiovisual-slidev) nem para roteiro de videoaula (use o workflow copy-roteiro-de-video). |

### <a id="arte-conceitual"></a>Arte Conceitual

| Recurso | Tipo | Origem | Descrição e Aplicação |
| :--- | :--- | :--- | :--- |
| <a id="audiovisual-arte-conceitual"></a>**`/audiovisual-arte-conceitual`** | `Workflow` | `0 Mkt` | Crie belas artes visuais em documentos .png e .pdf usando a filosofia de design. Você deve usar essa habilidade quando o usuário solicitar a criação de um pôster, obra de arte, design ou outra peça estática. Crie designs visuais originais, nunca copiando trabalhos de artistas existentes para evitar violações de direitos autorais. |

### <a id="banco-de-imagens-pexels"></a>Banco De Imagens Pexels

| Recurso | Tipo | Origem | Descrição e Aplicação |
| :--- | :--- | :--- | :--- |
| <a id="audiovisual-banco-de-imagens-pexels"></a>**`/audiovisual-banco-de-imagens-pexels`** | `Workflow` | `0 Mkt` | Obtenha imagens e vídeos isentos de royalties da API Pexels para design, espaços reservados ou conteúdo. Suporta pesquisa, conteúdo curado/popular, coleções, múltiplas resoluções e SEMPRE cria arquivos de metadados secundários detalhados. |

### <a id="banco-de-midias-openverse"></a>Banco De Midias Openverse

| Recurso | Tipo | Origem | Descrição e Aplicação |
| :--- | :--- | :--- | :--- |
| <a id="audiovisual-banco-de-midias-openverse"></a>**`audiovisual-banco-de-midias-openverse`** | `Skill` | `0 Mkt` | Use para buscar fotos, ilustrações, vetores, áudios e vídeos livres (domínio público e Creative Commons CC0 e CC-BY) na API do Openverse, com fallback no Wikimedia Commons e atribuição legal pronta. Gatilhos: \"imagem livre\", \"Creative Commons\", \"banco de imagens gratuito\", \"Openverse\". NÃO use para fotos de estoque do Pexels (use o workflow audiovisual-banco-de-imagens-pexels) nem para gerar imagem com IA (use audiovisual-imagem-flux-prompts). |

### <a id="criacao-de-pitch-deck"></a>Criacao De Pitch Deck

| Recurso | Tipo | Origem | Descrição e Aplicação |
| :--- | :--- | :--- | :--- |
| <a id="audiovisual-criacao-de-pitch-deck"></a>**`@audiovisual-criacao-de-pitch-deck`** | `Agent` | `0 Mkt` | Especialista em apresentações executivas, pitch decks de captação de investimento e narrativa de negócios. Use quando precisar estruturar decks para investidores (Venture Capital / Anjos), apresentações comerciais de alto impacto para C-Levels, keynotes institucionais ou slides automatizados via código (Slidev). <example> Context: O fundador precisa preparar o pitch deck para rodada Seed da startup. user: "Preciso montar o pitch deck de captação da <marca> para fundos de VC." assistant: "Vou acionar o audiovisual-criacao-de-pitch-deck para estruturar o deck na narrativa padrão de 10-12 slides (Problema, Solução, Mercado, Tração, Time, Ask) com foco no modelo YC." <commentary> Demanda de fundraising e apresentação executiva para investidores delegada ao audiovisual-criacao-de-pitch-deck. </commentary> </example> <example> Context: O time precisa de uma apresentação comercial técnica em formato Slidev com código interativo. user: "Crie uma apresentação técnica para diretoria da <marca> com slides interativos usando Slidev." assistant: "Acionando o audiovisual-criacao-de-pitch-deck para gerar o arquivo Markdown formatado para renderização Slidev com layout limpo e suporte a componentes." <commentary> Apresentação técnica moderna com ferramenta de slides por código. </commentary> </example> |

### <a id="download-de-video"></a>Download De Video

| Recurso | Tipo | Origem | Descrição e Aplicação |
| :--- | :--- | :--- | :--- |
| <a id="audiovisual-download-de-video"></a>**`/audiovisual-download-de-video`** | `Workflow` | `0 Mkt` | Baixe vídeos do YouTube com opções personalizáveis ​​de qualidade e formato. Use esta habilidade quando o usuário solicitar para baixar, salvar ou capturar vídeos do YouTube. Suporta várias configurações de qualidade (melhor, 1080p, 720p, 480p, 360p), vários formatos (mp4, webm, mkv) e downloads somente de áudio como MP3. |

### <a id="estrutura-de-apresentacao"></a>Estrutura De Apresentacao

| Recurso | Tipo | Origem | Descrição e Aplicação |
| :--- | :--- | :--- | :--- |
| <a id="audiovisual-estrutura-de-apresentacao"></a>**`/audiovisual-estrutura-de-apresentacao`** | `Workflow` | `0 Mkt` | Estruture apresentações atraentes com narrativas claras e sugestões visuais |

### <a id="imagem-flux-api"></a>Imagem Flux Api

| Recurso | Tipo | Origem | Descrição e Aplicação |
| :--- | :--- | :--- | :--- |
| <a id="audiovisual-imagem-flux-api"></a>**`audiovisual-imagem-flux-api`** | `Skill` | `0 Mkt` | Use para integrar a API da BFL (FLUX) em código: endpoints, polling assíncrono, limites de taxa, tratamento de erro, webhooks e endpoints regionais, com exemplos em Python e TypeScript. Gatilhos: \"FLUX API\", \"BFL API\", \"polling FLUX\", \"webhook FLUX\". NÃO use para escrever prompts de imagem (use audiovisual-imagem-flux-prompts). Gera código: só com autorização explícita (regra 1.5 do CLAUDE.md). |

### <a id="imagem-flux-prompts"></a>Imagem Flux Prompts

| Recurso | Tipo | Origem | Descrição e Aplicação |
| :--- | :--- | :--- | :--- |
| <a id="audiovisual-imagem-flux-prompts"></a>**`audiovisual-imagem-flux-prompts`** | `Skill` | `0 Mkt` | Use para escrever prompts para os modelos de imagem FLUX.2 e FLUX.1 (BFL): texto para imagem, imagem para imagem, JSON estruturado, cores em hex, tipografia e edição com várias referências. Gatilhos: \"prompt FLUX\", \"gerar imagem com FLUX\", \"edição multi-referência\". NÃO use para integrar a API em código (use audiovisual-imagem-flux-api) nem para direção de arte e prompts em carrosséis (use social-direcao-de-arte-ia). |

### <a id="infografico"></a>Infografico

| Recurso | Tipo | Origem | Descrição e Aplicação |
| :--- | :--- | :--- | :--- |
| <a id="audiovisual-infografico"></a>**`/audiovisual-infografico`** | `Workflow` | `0 Mkt` | Crie belos infográficos com base no conteúdo do texto fornecido. Use isto quando os usuários solicitarem a criação de infográficos. |

### <a id="melhoria-de-slide"></a>Melhoria De Slide

| Recurso | Tipo | Origem | Descrição e Aplicação |
| :--- | :--- | :--- | :--- |
| <a id="audiovisual-melhoria-de-slide"></a>**`/audiovisual-melhoria-de-slide`** | `Workflow` | `0 Mkt` | Transforme slides com muito texto em narrativas visuais. Sugira melhorias de layout, uso de ícones e visualização de dados. |

### <a id="nano-banana"></a>Nano Banana

| Recurso | Tipo | Origem | Descrição e Aplicação |
| :--- | :--- | :--- | :--- |
| <a id="audiovisual-nano-banana"></a>**`/audiovisual-nano-banana`** | `Workflow` | `0 Mkt` | OBRIGATÓRIO para todas as solicitações de geração de imagens. Gere e edite imagens usando Nano Banana (Gemini CLI). Lida com imagens em destaque do blog, miniaturas do YouTube, ícones, diagramas, padrões, ilustrações, fotos, recursos visuais, gráficos, obras de arte, imagens. Use esta habilidade sempre que o usuário solicitar para criar, gerar, fazer, desenhar, projetar ou editar qualquer imagem ou conteúdo visual. |

### <a id="nano-banana-pro"></a>Nano Banana Pro

| Recurso | Tipo | Origem | Descrição e Aplicação |
| :--- | :--- | :--- | :--- |
| <a id="audiovisual-nano-banana-pro"></a>**`/audiovisual-nano-banana-pro`** | `Workflow` | `0 Mkt` | Gere imagens usando o Nano Banana Pro do Google (gemini-3-pro-image-preview). Aceita prompts de texto e opcionalmente imagens (para edição/transformação) como INPUT. Retorna IMAGENS geradas como SAÍDA. Use quando o usuário solicitar para criar, gerar, editar ou desenhar imagens, infográficos, visualizações, diagramas, gráficos ou ilustrações. Excelente para infográficos com precisão de dados e renderização de texto. |

### <a id="pitch-deck"></a>Pitch Deck

| Recurso | Tipo | Origem | Descrição e Aplicação |
| :--- | :--- | :--- | :--- |
| <a id="audiovisual-pitch-deck"></a>**`audiovisual-pitch-deck`** | `Skill` | `0 Mkt` | Use para montar a narrativa e a estrutura de pitch decks para investidores (padrão Y Combinator) e decks comerciais de alto impacto, com storytelling financeiro e design executivo. Gatilhos: \"pitch deck\", \"deck de investidor\", \"rodada seed\", \"deck comercial\". NÃO use para slides de aula e treinamento (use audiovisual-apresentacoes-educacionais), para slides de código em Markdown (use audiovisual-slidev) nem para melhorar um slide isolado (use o workflow audiovisual-melhoria-de-slide). |

### <a id="podcast-e-audio"></a>Podcast E Audio

| Recurso | Tipo | Origem | Descrição e Aplicação |
| :--- | :--- | :--- | :--- |
| <a id="audiovisual-podcast-e-audio"></a>**`audiovisual-podcast-e-audio`** | `Skill` | `0 Mkt` | Use para pós-produção de áudio: edição, mixagem e masterização de podcasts, conformidade ACX de audiobooks, transcrição com Whisper, direção de locução e sound design. Gatilhos: \"masterizar podcast\", \"ACX\", \"audiobook\", \"locução\", \"limpar áudio\". NÃO use para logo sonoro e identidade de áudio da marca (use brand-identidade-sonora), para transcrição com ElevenLabs (use audiovisual-transcricao) nem para SEO de podcast (use seo-podcast). |

### <a id="producao-de-video"></a>Producao De Video

| Recurso | Tipo | Origem | Descrição e Aplicação |
| :--- | :--- | :--- | :--- |
| <a id="audiovisual-producao-de-video"></a>**`@audiovisual-producao-de-video`** | `Agent` | `0 Mkt` | Produtor audiovisual e diretor criativo especializado em roteirização, engenharia de áudio, ganchos de alta retenção para vídeos curtos (Reels/TikTok/Shorts), VSLs de alta conversão, processamento de mídia e animação com código. Use quando precisar criar roteiros de vídeo, planejar hooks visuais e narrativos, masterizar podcasts ou orquestrar produções de vídeo programático. <example> Context: O usuário precisa de um roteiro dinâmico para Reels com foco em reter o público nos primeiros 3 segundos. user: "Preciso de um roteiro para um vídeo curto no Reels ensinando automação de CRM para a <marca>." assistant: "Vou acionar o audiovisual-producao-de-video para estruturar o roteiro com ganchos visuais e verbais nos primeiros 3 segundos, pattern interrupts e CTA final." <commentary> Demanda de roteirização e retenção para vídeo curto, acionando o produtor audiovisual especializado. </commentary> </example> <example> Context: O usuário quer estruturar uma Video Sales Letter (VSL) de 15 minutos para lançamento de produto. user: "Como estruturar a VSL do novo produto da <marca> com prova social e mecanismo único?" assistant: "Acionando o audiovisual-producao-de-video para construir a estrutura em 5 atos da VSL, integrando o mecanismo único e ritmo narrativo cinematográfico." <commentary> Demanda de direct response audiovisual e narrativa persuasiva de alta conversão. </commentary> </example> |

### <a id="qr-code"></a>Qr Code

| Recurso | Tipo | Origem | Descrição e Aplicação |
| :--- | :--- | :--- | :--- |
| <a id="audiovisual-qr-code"></a>**`audiovisual-qr-code`** | `Skill` | `0 Mkt` | Gere códigos QR com URLs e rastreamento UTM. Exporta PNG/SVG com legendas. Use para códigos únicos, geração de lotes ou campanhas de marketing com parâmetros de rastreamento. |
| <a id="audiovisual-qr-code"></a>**`/audiovisual-qr-code`** | `Workflow` | `0 Mkt` | Gere códigos QR com URLs e rastreamento UTM. Exporta PNG/SVG com legendas. |

### <a id="slidev"></a>Slidev

| Recurso | Tipo | Origem | Descrição e Aplicação |
| :--- | :--- | :--- | :--- |
| <a id="audiovisual-slidev"></a>**`audiovisual-slidev`** | `Skill` | `0 Mkt` | Guia completo para Slidev - uma estrutura de apresentação baseada na web para desenvolvedores. Abrange sintaxe Markdown, layouts, componentes, animações, temas e exportação. Use esta habilidade ao criar ou trabalhar com apresentações para desenvolvedores usando Slidev. |
| <a id="audiovisual-slidev"></a>**`/audiovisual-slidev`** | `Workflow` | `0 Mkt` | Guia completo para Slidev - uma estrutura de apresentação baseada na web para |

### <a id="storyline-mckinsey"></a>Storyline Mckinsey

| Recurso | Tipo | Origem | Descrição e Aplicação |
| :--- | :--- | :--- | :--- |
| <a id="audiovisual-storyline-mckinsey"></a>**`/audiovisual-storyline-mckinsey`** | `Workflow` | `0 Mkt` | Estrutura de enredo no estilo McKinsey para construir apresentações. Use quando os usuários precisarem estruturar apresentações, argumentos de venda ou comunicações estratégicas. Cria um fluxo lógico onde cada enredo se torna um título de slide, progredindo do problema para a solução. |

### <a id="traducao-de-legenda"></a>Traducao De Legenda

| Recurso | Tipo | Origem | Descrição e Aplicação |
| :--- | :--- | :--- | :--- |
| <a id="audiovisual-traducao-de-legenda"></a>**`/audiovisual-traducao-de-legenda`** | `Workflow` | `0 Mkt` | Traduza legendas de vídeo (SRT, VTT, TXT) entre idiomas. Suporta tradução em lote e mantém a sincronização de tempo. Use ao criar legendas multilíngues, expandir para públicos internacionais ou traduzir transcrições de vídeos. |

### <a id="transcricao"></a>Transcricao

| Recurso | Tipo | Origem | Descrição e Aplicação |
| :--- | :--- | :--- | :--- |
| <a id="audiovisual-transcricao"></a>**`audiovisual-transcricao`** | `Skill` | `0 Mkt` | Transcreva áudio para texto usando ElevenLabs Scribe v2. Use ao converter áudio/vídeo em texto, gerar legendas, transcrever reuniões ou processar conteúdo falado. |

### <a id="video-para-gif"></a>Video Para Gif

| Recurso | Tipo | Origem | Descrição e Aplicação |
| :--- | :--- | :--- | :--- |
| <a id="audiovisual-video-para-gif"></a>**`/audiovisual-video-para-gif`** | `Workflow` | `0 Mkt` | Converta videoclipes em GIFs otimizados com controle de velocidade, corte, sobreposições de texto e otimização de tamanho de arquivo. Crie GIFs perfeitos para mídias sociais, documentação e apresentações. |

---

## <a id="brand-identidade-da-marca"></a>brand (Identidade da Marca)

Total de recursos nesta macro-área: `13`

### <a id="audience"></a>Audience

| Recurso | Tipo | Origem | Descrição e Aplicação |
| :--- | :--- | :--- | :--- |
| <a id="brand-audience"></a>**`brand-audience`** | `Skill` | `0 Mkt` | Use para definir ou refazer personas, segmentos, jobs to be done, objeções e hábitos de mídia de uma marca (etapa 3 do brand-builder). Gatilhos: \"persona da marca\", \"público da marca\", \"personas finas\". NÃO use para ICP, pontuação de aderência e JTBD de produto em geral (use persona-icp) nem para validar ideia com entrevistas (use persona-descoberta-de-clientes). |

### <a id="builder"></a>Builder

| Recurso | Tipo | Origem | Descrição e Aplicação |
| :--- | :--- | :--- | :--- |
| <a id="brand-builder"></a>**`brand-builder`** | `Skill` | `0 Mkt` | Use para construir ou aprofundar as fundações de uma marca de _brands/, uma etapa por vez e com aprovação: essência, posicionamento, público, voz, desejo, direção visual, design system, ativação e brandbook. Gatilhos: \"brandbook\", \"marca nova\", \"arquivos de marca finos\", \"posicionamento da marca\". NÃO use para produzir conteúdo da marca (use o fluxo normal com conteudo-estrategia ou copy-conversao), para ajustar um parágrafo, nem para criar só a identidade visual portátil (use brand-visual-style). |

### <a id="design-system"></a>Design System

| Recurso | Tipo | Origem | Descrição e Aplicação |
| :--- | :--- | :--- | :--- |
| <a id="brand-design-system"></a>**`brand-design-system`** | `Skill` | `0 Mkt` | Use para montar o design system da marca como site de referência mais DESIGN.md (paleta com modo escuro, tipografia, espaço, forma, movimento, componentes e tokens), a partir da direção visual aprovada (etapa 7 do brand-builder). Gatilhos: \"design system da marca\", \"DESIGN.md\", \"tokens da marca\". NÃO use para decidir o estilo (use brand-visual-direction) nem para escrever o código de componentes em Tailwind e React (use site-tailwind-design-system). |

### <a id="direcao-de-arte"></a>Direcao De Arte

| Recurso | Tipo | Origem | Descrição e Aplicação |
| :--- | :--- | :--- | :--- |
| <a id="brand-direcao-de-arte"></a>**`@brand-direcao-de-arte`** | `Agent` | `0 Mkt` | Diretor de Arte Sênior e Especialista em Branding com padrão de agência internacional (estilo Apple, Nike, Stripe, Airbnb, Notion). Especialista em neurodesign, hierarquia visual, psicologia das cores, tipografia contemporânea e direção estética para redes sociais, apresentações, landing pages e identidades de marca. Use quando precisar definir conceitos visuais de alto impacto, conceber direção de arte multiformato, gerar prompts de imagem multi-engine (Midjourney, Flux, ChatGPT, SD) ou conduzir auditoria e autocrítica estética intransigente. <example> Context: O usuário precisa de uma direção de arte impactante para a campanha de lançamento de um novo recurso. user: "Preciso criar a direção visual para o lançamento da nova funcionalidade da PR Pulse no Instagram e landing page." assistant: "Vou acionar o brand-direcao-de-arte para conceber o conceito criativo, estruturar 3 caminhos visuais divergentes, definir paleta funcional e tipografia moderna, orquestrando as skills de carrossel e landing page." <commentary> Demanda de concepção estética, direção de arte e consistência visual multiformato. </commentary> </example> <example> Context: O usuário quer prompts de imagem refinados para gerar assets visuais no Midjourney e Flux sem visual clichê de IA. user: "Gere os prompts de imagem para o novo produto da <marca> com estética minimalista e profissional." assistant: "Acionando o brand-direcao-de-arte para aplicar o filtro anti-slop visual, construir a atmosfera e gerar os prompts calibrados para Midjourney, Flux e ChatGPT Image com contraste e respiro profissional." <commentary> Demanda de engenharia estética de prompts de IA generativa com rigor de diretor de arte. </commentary> </example> |

### <a id="essence"></a>Essence

| Recurso | Tipo | Origem | Descrição e Aplicação |
| :--- | :--- | :--- | :--- |
| <a id="brand-essence"></a>**`brand-essence`** | `Skill` | `0 Mkt` | Use para definir ou aprofundar essência, crenças, história de origem, inimigo, posicionamento, categoria e arquétipo de uma marca (etapas 1 e 2 do brand-builder). Gatilhos: \"propósito\", \"posicionamento da marca\", \"Primal Branding\", \"arquétipo\". NÃO use para posicionar produto no mercado com GTM, categoria e proposta de valor de lançamento (use revenue-gtm-e-posicionamento) nem para analisar concorrentes (use revenue-inteligencia-competitiva). |

### <a id="guardiao-de-voz"></a>Guardiao De Voz

| Recurso | Tipo | Origem | Descrição e Aplicação |
| :--- | :--- | :--- | :--- |
| <a id="brand-guardiao-de-voz"></a>**`@brand-guardiao-de-voz`** | `Agent` | `0 Mkt` | Especialista em consistência de marca e validação de voz. Use para garantir que todo o conteúdo de marketing corresponda às diretrizes de voz, tom e estilo da marca. Revisa o conteúdo quanto à consistência das mensagens, qualidade da linguagem e impacto emocional. Exemplos: <exemplo>Contexto: cópia da campanha de e-mail criada pelo usuário. usuário: \"Analise esta campanha de e-mail para verificar a consistência da voz da marca\" assistente: \"Usarei o agente brand-guardiao-de-voz para validar o tom, a mensagem e o alinhamento da marca." <commentary>A validação da voz da marca requer revisão especializada de acordo com as diretrizes.</commentary></example> <example>Contexto: o usuário precisa que a cópia da página de destino seja revisada. usuário: \"Verifique se esta página de destino se parece com a nossa marca\" assistente: \"Deixe-me implantar o agente de guarda-de-voz da marca para analisar a voz, o tom e a consistência das mensagens.\" <commentary>A revisão da consistência da marca garante que todo o conteúdo esteja alinhado com as diretrizes estabelecidas.</commentary></example> |

### <a id="identidade-sonora"></a>Identidade Sonora

| Recurso | Tipo | Origem | Descrição e Aplicação |
| :--- | :--- | :--- | :--- |
| <a id="brand-identidade-sonora"></a>**`brand-identidade-sonora`** | `Skill` | `0 Mkt` | Use para definir a identidade sonora de uma marca: logo sonoro (1 a 3 segundos), estética de voz, moodboard de áudio e diretrizes de trilha, efeitos e silêncio para vídeo, podcast, aplicativo e eventos (etapa 8, uso audiovisual, do brand-builder). Gatilhos: \"logo sonoro\", \"identidade sonora\", \"trilha da marca\", \"sonic branding\". NÃO use para editar, mixar ou masterizar áudio (use audiovisual-podcast-e-audio), para transcrever (use audiovisual-transcricao), para gerar voz sintética ou produzir vídeo (projeto Edição de Vídeo com IA) nem para a identidade visual (use brand-visual-direction e brand-design-system). |

### <a id="identidade-e-marca"></a>Identidade e Marca

| Recurso | Tipo | Origem | Descrição e Aplicação |
| :--- | :--- | :--- | :--- |
| <a id="sip-marketing"></a>**`sip-marketing`** | `Skill` | `0 Mkt` | Use sempre que a tarefa atual envolver marketing, conteúdo, copywriting, branding, mídia social, SEO, anúncios pagos, e-mail, RP, crescimento, capacitação de vendas ou análise de marketing, mas o projeto ativo não tiver habilidades de marketing local - ou seja, qualquer projeto que não seja o próprio "SIP - Marketing" (0 Mkt). Encaminha a tarefa para o centro central de conhecimento de marketing, em vez de improvisar a partir do conhecimento geral. Use também quando o usuário perguntar "existe algo de marketing pra isso", "tem habilidade de marketing no hub", "consulta o SIP - Marketing", ou nomear explicitamente uma habilidade, agente ou fluxo de trabalho 0 Mkt em um projeto que não é o hub. |

### <a id="naming"></a>Naming

| Recurso | Tipo | Origem | Descrição e Aplicação |
| :--- | :--- | :--- | :--- |
| <a id="brand-naming"></a>**`brand-naming`** | `Skill` | `0 Mkt` | Use para criar e validar nomes de marca, produto e empresa pelo protocolo dos 6 portões (briefing, geração, fonético, jurídico, AEO e narrativa). Gatilhos: \"nome da marca\", \"naming\", \"rebranding de nome\", \"nome para a empresa\". NÃO use para reposicionar uma marca que já tem nome (use brand-essence) nem para confirmar registro de marca (o portão jurídico indica a busca; quem confirma é o INPI ou um advogado). |

### <a id="paleta-de-cores"></a>Paleta De Cores

| Recurso | Tipo | Origem | Descrição e Aplicação |
| :--- | :--- | :--- | :--- |
| <a id="brand-paleta-de-cores"></a>**`/brand-paleta-de-cores`** | `Workflow` | `0 Mkt` | Extraia paletas de cores de imagens, sites ou designs. Identifica cores dominantes, gera esquemas complementares e exporta em múltiplos formatos (variáveis ​​HEX, RGB, HSL, Tailwind, CSS). Use quando os usuários precisarem de esquemas de cores de imagens, cores de marcas ou paletas de sistemas de design. |

### <a id="visual-direction"></a>Visual Direction

| Recurso | Tipo | Origem | Descrição e Aplicação |
| :--- | :--- | :--- | :--- |
| <a id="brand-visual-direction"></a>**`brand-visual-direction`** | `Skill` | `0 Mkt` | Use para decidir direção visual, mood, estilo de imagem, intenção de cor e tipografia e visual de vídeo antes do design system (etapa 6 do brand-builder). Gatilhos: \"direção visual\", \"moodboard\", \"como a marca deve parecer\", \"tendências visuais\". NÃO use para gerar tokens e componentes (use brand-design-system), extrair ou aplicar um visual-style.md (use brand-visual-style) nem para conceito de anúncio (use ads-criativos). |

### <a id="visual-style"></a>Visual Style

| Recurso | Tipo | Origem | Descrição e Aplicação |
| :--- | :--- | :--- | :--- |
| <a id="brand-visual-style"></a>**`brand-visual-style`** | `Skill` | `0 Mkt` | Use para criar, extrair e aplicar um sistema visual portátil em um arquivo visual-style.md (cores, tipografia, layout, movimento e humor em um só arquivo que qualquer IA lê): criar do zero, extrair de um site, vídeo ou PDF de marca, aplicar em vídeo (HeyGen), slides HTML, Figma ou paper.design, ou consultar a galeria de estilos prontos (Suíço, Saul Bass, Game Boy etc.). Gatilhos: \"visual style\", \"estilo visual\", \"brand style\", \"style guide\". NÃO use para estratégia de marca, nome ou essência (use brand-builder), para decidir a direção visual da marca (use brand-visual-direction), para tokens e componentes de uma marca de _brands/ (use brand-design-system; o visual-style.md dela é exportado no passo 7b) nem para conceito de anúncio (use ads-criativos). |

### <a id="voice-messaging"></a>Voice Messaging

| Recurso | Tipo | Origem | Descrição e Aplicação |
| :--- | :--- | :--- | :--- |
| <a id="brand-voice-messaging"></a>**`brand-voice-messaging`** | `Skill` | `0 Mkt` | Use para definir ou refazer tom de voz, vocabulário, \"o que NÃO comunicar\", mensagens e pilares de conteúdo de uma marca (etapa 4 do brand-builder), ou extrair a voz de textos existentes. Gatilhos: \"tom de voz\", \"brand voice\", \"pilares de conteúdo\", \"o que não comunicar\". NÃO use para escrever a peça (use copy-conversao), planejar calendário e formatos (use conteudo-estrategia) nem limpar texto com cara de IA (use geral-anti-slop). |

---

## <a id="conteudo-produção-de-conteúdo"></a>conteudo (Produção de Conteúdo)

Total de recursos nesta macro-área: `22`

### <a id="aprovacao"></a>Aprovacao

| Recurso | Tipo | Origem | Descrição e Aplicação |
| :--- | :--- | :--- | :--- |
| <a id="conteudo-aprovacao"></a>**`/conteudo-aprovacao`** | `Workflow` | `0 Mkt` | Gera o fluxo de aprovação de uma peça de conteúdo (etapas, responsáveis, SLA e checklist por estágio). Use quando uma peça precisar passar por revisão antes de publicar. |

### <a id="brainstorm"></a>Brainstorm

| Recurso | Tipo | Origem | Descrição e Aplicação |
| :--- | :--- | :--- | :--- |
| <a id="conteudo-brainstorm"></a>**`@conteudo-brainstorm`** | `Agent` | `0 Mkt` | Especialista em idealização de campanhas e conceito criativo. Use para debater ideias de campanha, avaliar abordagens de marketing, desenvolver ângulos de mensagens e debater decisões criativas antes da execução. Exemplos: <exemplo>Contexto: o usuário deseja ideias de campanha. usuário: \"Precisamos de conceitos criativos para o lançamento de nosso produto\" assistente: \"Deixe-me usar o agente conteudo-brainstorm para explorar ângulos de campanha e conceitos criativos para o lançamento." usuário: \"Devemos nos concentrar em marketing de conteúdo ou anúncios pagos?\" assistente: \"Envolverei o agente de brainstorming para analisar ambas as abordagens e recomendar a melhor estratégia." <commentary>As decisões estratégicas exigem a avaliação de compensações e a consideração de vários fatores.</commentary></example> |

### <a id="briefing"></a>Briefing

| Recurso | Tipo | Origem | Descrição e Aplicação |
| :--- | :--- | :--- | :--- |
| <a id="conteudo-briefing"></a>**`conteudo-briefing`** | `Skill` | `0 Mkt` | Use para montar briefings de conteúdo completos para redatores, com objetivo, público, ângulo, estrutura e critérios de aprovação, em qualquer formato. Gatilhos: \"briefing de conteúdo\", \"brief para redator\", \"pauta para freela\". NÃO use para briefing com foco em SEO e palavras-chave (use o workflow conteudo-briefing-de-seo), para estratégia e calendário (use conteudo-estrategia) nem para escrever o texto (use conteudo-post-de-blog ou copy-conversao). |
| <a id="conteudo-briefing"></a>**`/conteudo-briefing`** | `Workflow` | `0 Mkt` | Gere resumos de conteúdo abrangentes para redatores, garantindo clareza, |

### <a id="briefing-de-seo"></a>Briefing De Seo

| Recurso | Tipo | Origem | Descrição e Aplicação |
| :--- | :--- | :--- | :--- |
| <a id="conteudo-briefing-de-seo"></a>**`/conteudo-briefing-de-seo`** | `Workflow` | `0 Mkt` | Modelo de resumo de conteúdo e metodologia de criação para conteúdo otimizado para SEO. Use ao preparar briefings para redatores ou planejar novos conteúdos. |

### <a id="criacao-multiformato"></a>Criacao Multiformato

| Recurso | Tipo | Origem | Descrição e Aplicação |
| :--- | :--- | :--- | :--- |
| <a id="conteudo-criacao-multiformato"></a>**`@conteudo-criacao-multiformato`** | `Agent` | `0 Mkt` | Especialista em criação de conteúdo para todos os tipos de conteúdo de marketing. |

### <a id="escrita-colaborativa"></a>Escrita Colaborativa

| Recurso | Tipo | Origem | Descrição e Aplicação |
| :--- | :--- | :--- | :--- |
| <a id="conteudo-escrita-colaborativa"></a>**`/conteudo-escrita-colaborativa`** | `Workflow` | `0 Mkt` | Auxilia na redação de conteúdo de alta qualidade conduzindo pesquisas, adicionando citações, melhorando ganchos, iterando esboços e fornecendo feedback em tempo real sobre cada seção. Transforma seu processo de escrita de esforço individual em parceria colaborativa. |

### <a id="estrategia"></a>Estrategia

| Recurso | Tipo | Origem | Descrição e Aplicação |
| :--- | :--- | :--- | :--- |
| <a id="conteudo-estrategia"></a>**`conteudo-estrategia`** | `Skill` | `0 Mkt` | Use para planejar o conteúdo de uma marca: estratégia e playbook, pilares editoriais, calendário editorial, formatos, distribuição, geração de ideias a partir do posicionamento, análise de lacunas de conteúdo contra concorrentes e guia de estilo. Gatilhos: \"teia de conteúdo\", \"webfluence\", \"isca digital\", \"lead magnet\", \"estratégia de conteúdo\", \"calendário editorial\", \"pilares de conteúdo\", \"ideias de conteúdo\", \"onde distribuir\", \"lacuna de conteúdo\", \"guia de estilo\". NÃO use para reaproveitar um conteúdo em vários formatos (use conteudo-reaproveitamento), para pesquisa de palavras-chave (use seo-palavras-chave), para a campanha completa (use revenue-campanhas) nem para tendências de redes (use conteudo-tendencias). |
| <a id="conteudo-estrategia"></a>**`/conteudo-estrategia`** | `Workflow` | `0 Mkt` | Teia de conteúdo que prepara a venda (conteúdo, VSL, oferta): diagnostica por que há tráfego e não há venda, e onde falta conexão entre os conteúdos. Não é sobre site nem design de página. Use para: oferta enviada direto para tráfego frio, abertura alta sem cliques, VSL assistido sem compra. |

### <a id="kit-de-podcast"></a>Kit De Podcast

| Recurso | Tipo | Origem | Descrição e Aplicação |
| :--- | :--- | :--- | :--- |
| <a id="conteudo-kit-de-podcast"></a>**`/conteudo-kit-de-podcast`** | `Workflow` | `0 Mkt` | Transforme transcrições de podcast em pacotes abrangentes de marketing de conteúdo, incluindo postagens de blog, conteúdo de mídia social, boletins informativos, artigos otimizados para SEO e carimbos de data/hora. Use quando o usuário fornecer transcrições de podcast ou quiser redirecionar o conteúdo do podcast. |

### <a id="linha-de-producao"></a>Linha De Producao

| Recurso | Tipo | Origem | Descrição e Aplicação |
| :--- | :--- | :--- | :--- |
| <a id="conteudo-linha-de-producao"></a>**`conteudo-linha-de-producao`** | `Skill` | `0 Mkt` | Use when: orquestrar a linha de produção unificada de conteúdo de alta retenção e conversão para Reels, TikTok, Shorts e Carrosséis; conecta a marca ativa (_brands/), psicologia comportamental (revenue-sexy-canvas), mineração de dados (hook-mining), engenharia reversa (reel-analyzer e viral-carousel), geração de carrosséis via IA (social-carrossel e social-direcao-de-arte-ia), retenção visual (copy-hooks-video-curto), motores de mídia (Remotion, no projeto de edição de vídeo) e filtro anti-slop. |

### <a id="pesquisa"></a>Pesquisa

| Recurso | Tipo | Origem | Descrição e Aplicação |
| :--- | :--- | :--- | :--- |
| <a id="conteudo-pesquisa"></a>**`conteudo-pesquisa`** | `Skill` | `0 Mkt` | Research-first content creation optimized for both human readers and AI search engines (Claude, ChatGPT, Perplexity, Gemini). Creates authentic, authoritative content that becomes the go-to citation source for AI models answering user questions. Use this skill when: - Creating content that should appear in AI search results (Perplexity, ChatGPT, Claude) - Building topical authority to become THE source AI cites for a topic - Launching a new product and need compelling, citable content - Creating blog posts, articles, social media, or press releases - Need content that references real trends, people, and recent events - Want AI-assisted content that doesn't sound AI-generated - Creating thought leadership content in any industry Triggers: "create content for", "write about", "research and write", "find experts for", "content for launch", "blog post about", "article on", "press release for", "AI search", "show up in AI", "Perplexity", "be cited by AI" This skill is for CREATING content with research. NÃO use para otimizar conteúdo já escrito para ser citado por IA (use seo-geo), redigir artigo otimizado para SEO com clusters e palavras-chave (use seo-conteudo) nem relações com a imprensa (use pr-assessoria-de-imprensa). |
| <a id="conteudo-pesquisa"></a>**`/conteudo-pesquisa`** | `Workflow` | `0 Mkt` | Criação de conteúdo que prioriza a pesquisa e é otimizado para leitores humanos e |

### <a id="post-de-blog"></a>Post De Blog

| Recurso | Tipo | Origem | Descrição e Aplicação |
| :--- | :--- | :--- | :--- |
| <a id="conteudo-post-de-blog"></a>**`conteudo-post-de-blog`** | `Skill` | `0 Mkt` | Transforme despejos cerebrais em postagens de blog sofisticadas com a voz da própria marca. Use quando o usuário quiser escrever uma postagem no blog com ideias dispersas, pontos de discussão e conclusões que precisam de organização em uma narrativa coesa e conversacional. |
| <a id="conteudo-post-de-blog"></a>**`/conteudo-post-de-blog`** | `Workflow` | `0 Mkt` | Transforme despejos cerebrais em postagens de blog sofisticadas na voz de Nick Nisi. |

### <a id="pre-publicacao"></a>Pre Publicacao

| Recurso | Tipo | Origem | Descrição e Aplicação |
| :--- | :--- | :--- | :--- |
| <a id="conteudo-pre-publicacao"></a>**`/conteudo-pre-publicacao`** | `Workflow` | `0 Mkt` | Assistente de pré-publicação para novas postagens no blog. Use quando o usuário deseja classificar uma nova postagem com categorias e tags, gerar metadados de SEO (título, descrição, frase-chave de foco) ou obter sugestões inteligentes e fundamentadas. Funciona com rascunho de conteúdo (caminho de arquivo, URL ou texto) e sugere a partir de taxonomia existente para manter uma distribuição equilibrada. |

### <a id="reaproveitamento"></a>Reaproveitamento

| Recurso | Tipo | Origem | Descrição e Aplicação |
| :--- | :--- | :--- | :--- |
| <a id="conteudo-reaproveitamento"></a>**`conteudo-reaproveitamento`** | `Skill` | `0 Mkt` | One-to-many content multiplication engine. Transform long-form assets (podcasts, webinars, whitepapers, pillar articles) into high-performing social posts, email newsletters, carousels, and video scripts using semantic content architectures. NÃO use para estratégia e calendário de conteúdo (use conteudo-estrategia) nem para escrever um artigo de blog (use conteudo-post-de-blog). |
| <a id="conteudo-reaproveitamento"></a>**`/conteudo-reaproveitamento`** | `Workflow` | `0 Mkt` | Mecanismo de multiplicação de conteúdo um para muitos. Transforme ativos de formato longo |

### <a id="sinais-fracos"></a>Sinais Fracos

| Recurso | Tipo | Origem | Descrição e Aplicação |
| :--- | :--- | :--- | :--- |
| <a id="conteudo-sinais-fracos"></a>**`/conteudo-sinais-fracos`** | `Workflow` | `0 Mkt` | Identifique tendências EMERGENTES conectando pontos em fontes não relacionadas. Monitore comunidades de nicho, pesquisas acadêmicas, GitHub, patentes, financiamento, mudanças regulatórias. Preveja qual será a tendência em 3 a 6 meses com base em sinais fracos. |

### <a id="temas-e-plugins"></a>Temas E Plugins

| Recurso | Tipo | Origem | Descrição e Aplicação |
| :--- | :--- | :--- | :--- |
| <a id="conteudo-temas-e-plugins"></a>**`/conteudo-temas-e-plugins`** | `Workflow` | `0 Mkt` | Crie conteúdo de marketing abrangente para temas, plug-ins e produtos da web. Gera uma estrutura de pastas organizada com descrições de produtos, destaques de recursos, postagens em mídias sociais, campanhas por e-mail, scripts de vídeo, materiais de vendas e ativos de marca. Use ao criar conteúdo promocional, anúncios ou textos de vendas. |

### <a id="tendencias"></a>Tendencias

| Recurso | Tipo | Origem | Descrição e Aplicação |
| :--- | :--- | :--- | :--- |
| <a id="conteudo-tendencias"></a>**`conteudo-tendencias`** | `Skill` | `0 Mkt` | Use para pesquisar tendências de tópicos em Google Trends, Google Analytics, Reddit, LinkedIn, X, Substack, Medium, blogs, podcasts e YouTube e gerar esboços de artigo a partir da intenção de busca. Gatilhos: \"o que está em alta\", \"tendência de conteúdo\", \"tema do momento\", \"esboço baseado em dados\". NÃO use para estratégia e calendário editorial (use conteudo-estrategia), sinais fracos de mercado (use o workflow conteudo-sinais-fracos) nem pesquisa de palavras-chave (use seo-palavras-chave). |
| <a id="conteudo-tendencias"></a>**`/conteudo-tendencias`** | `Workflow` | `0 Mkt` | Habilidade avançada de pesquisa de conteúdo e tópico que analisa tendências em |

---

## <a id="copy-copywriting--conversão"></a>copy (Copywriting & Conversão)

Total de recursos nesta macro-área: `14`

### <a id="avaliacao-de-hook"></a>Avaliacao De Hook

| Recurso | Tipo | Origem | Descrição e Aplicação |
| :--- | :--- | :--- | :--- |
| <a id="copy-avaliacao-de-hook"></a>**`/copy-avaliacao-de-hook`** | `Workflow` | `0 Mkt` | Avalia e aprimora ganchos de conteúdo usando a estrutura The Hook Stack™. Use ao pontuar manchetes, refinar ganchos para vídeo/social/boletim informativo ou quando solicitado a "avaliar este gancho", "analisar a pilha de ganchos" ou "pontuar meu título". |

### <a id="conversao"></a>Conversao

| Recurso | Tipo | Origem | Descrição e Aplicação |
| :--- | :--- | :--- | :--- |
| <a id="copy-conversao"></a>**`copy-conversao`** | `Skill` | `0 Mkt` | Enterprise conversion copywriting, direct response methodologies, sales letters, CTA optimization, buyer psychology, and persuasion architecture based on Eugene Schwartz, Dan Kennedy, Gary Halbert, Donald Miller (StoryBrand), and Robert Cialdini. NÃO use para aplicar o método de um livro específico (use copy-metodos-classicos), para posicionamento e pesquisa de voz do cliente de SaaS (use copy-saas), para arquitetura de landing page seção a seção e auditoria de CRO (use copy-landing-page) nem para roteiro de VSL (use copy-vsl). |

### <a id="hook-de-video"></a>Hook De Video

| Recurso | Tipo | Origem | Descrição e Aplicação |
| :--- | :--- | :--- | :--- |
| <a id="copy-hook-de-video"></a>**`/copy-hook-de-video`** | `Workflow` | `0 Mkt` | Gere ganchos que chamam a atenção nos primeiros 3 segundos de vídeos. O gancho determina se os espectadores permanecem ou rolam. Cria múltiplas variações de gancho para testes A/B. Use ao criar aberturas de vídeo, melhorar a retenção ou criar conteúdo de rolagem para YouTube, TikTok ou Reels. |

### <a id="hooks-video-curto"></a>Hooks Video Curto

| Recurso | Tipo | Origem | Descrição e Aplicação |
| :--- | :--- | :--- | :--- |
| <a id="copy-hooks-video-curto"></a>**`copy-hooks-video-curto`** | `Skill` | `0 Mkt` | Use quando: escrever, planejado ou revisar o gancho (primeiros 3 segundos) de um Reel, TikTok ou Short, tanto a fala (segmentação, promessa, loop aberto, quadro mental, nostalgia, 'funciona mesmo que', matriz going-viral de objetivo único e emoção primária high-arousal) quanto o que aparece na tela (frame 0 em movimento, texto grande, funciona no mudo, técnica de payoff postergado); diagnosticar por que um vídeo curto flopou; Implementação conversão comentário -> DM sem link público. Complementa vsl-conrado-framework.md. |

### <a id="landing-page"></a>Landing Page

| Recurso | Tipo | Origem | Descrição e Aplicação |
| :--- | :--- | :--- | :--- |
| <a id="copy-landing-page"></a>**`copy-landing-page`** | `Skill` | `0 Mkt` | Design, write, and optimize high-converting landing pages. Section-by-section copywriting architecture (Hero, Problem, Solution, Features/Benefits, Social Proof, Objection Killing, Risk Reversal, FAQ, Final CTA) and CRO diagnostic audits. NÃO use para posicionamento e pesquisa de voz do cliente (use copy-saas), para cartas de venda e persuasão de resposta direta (use copy-conversao), para auditar a conversão de uma página pronta (use site-cro), para desenhar a interface (use site-interface-de-conversao), para isca digital e portão de e-mail (use conteudo-estrategia) nem para roteiro de VSL (use copy-vsl). |
| <a id="copy-landing-page"></a>**`/copy-landing-page`** | `Workflow` | `0 Mkt` | Cria o texto e a estrutura de uma landing page de conversão (hero, problema, solução, prova, FAQ, CTA final). Para construir a página inteira, com marca, código e teste, use /build-landing-page. |

### <a id="landing-page-secao-a-secao"></a>Landing Page Secao A Secao

| Recurso | Tipo | Origem | Descrição e Aplicação |
| :--- | :--- | :--- | :--- |
| <a id="copy-landing-page-secao-a-secao"></a>**`/copy-landing-page-secao-a-secao`** | `Workflow` | `0 Mkt` | Projete, escreva e otimize landing pages de alta conversão. Seção por seção |

### <a id="metodos-classicos"></a>Metodos Classicos

| Recurso | Tipo | Origem | Descrição e Aplicação |
| :--- | :--- | :--- | :--- |
| <a id="copy-metodos-classicos"></a>**`copy-metodos-classicos`** | `Skill` | `0 Mkt` | Use para aplicar o método de um livro clássico de copywriting, persuasão e marketing a uma peça ou estratégia: Gary Halbert (Boron Letters), David Ogilvy, Eugene Schwartz (5 níveis de consciência), Dan Kennedy, Russell Brunson (Expert Secrets), Heath (Made to Stick), Seth Godin (Permission Marketing e Purple Cow) e StoryBrand. Gatilhos: \"nível de consciência\", \"método Halbert\", \"estilo Ogilvy\", \"StoryBrand\", \"copy de resposta direta\", \"ideia que gruda\". NÃO use para escrever a copy final de conversão com frameworks práticos (use copy-conversao), para landing page (use copy-landing-page), para roteiro de VSL (use copy-vsl) nem para psicologia de consumo (use revenue-psicologia). |

### <a id="redacao-publicitaria"></a>Redacao Publicitaria

| Recurso | Tipo | Origem | Descrição e Aplicação |
| :--- | :--- | :--- | :--- |
| <a id="copy-redacao-publicitaria"></a>**`@copy-redacao-publicitaria`** | `Agent` | `0 Mkt` | Use este agente quando precisar criar textos de alta conversão e voltados para o engajamento para materiais de marketing, postagens em mídias sociais, páginas de destino, campanhas de e-mail, descrições de produtos ou qualquer conteúdo que precise chamar a atenção e impulsionar a ação. Exemplos:\\n\\n<exemplo>\\nContexto: o usuário está lançando um novo recurso de produto e precisa de uma cópia atraente para a seção principal da página de destino.\\nuser: \"Acabamos de adicionar um novo recurso de revisão de código com tecnologia de IA. Você pode escrever um título e um subtítulo principais para a página de destino?\"\\assistente: \"Vou usar a ferramenta Tarefa para iniciar o agente copy-redacao-publicitaria para criar uma cópia principal atraente que interrompa os visitantes e direcione conversões.\"\\n<commentary>\\nO usuário precisa de uma cópia de marketing que converta, então delegue ao agente copy-redacao-publicitaria para criar manchetes que chamem a atenção.\\n</commentary>\\n</example>\\n\\n<example>\\nContexto: o usuário deseja anunciar uma atualização de produto no Twitter/X para maximizar o engajamento.\\nuser: \"Acabamos de enviar GitHub Super IA Projects - Marketingauto-convites para AgentKits. Preciso de um tweet que deixe as pessoas entusiasmadas.\"\\assistente: \"Deixe-me usar o agente copy-redacao-publicitaria para criar um tweet que valha a pena viral, que capte a atenção e estimule o engajamento.\"\\n<commentary>\\nAnúncios em mídia social exigem experiência em redação viral, então use o copy-redacao-publicitaria agente.\\n</commentary>\\n</example>\\n\\n<exemplo>\\nContexto: o usuário está revisando materiais de marketing e o agente identifica proativamente uma cópia fraca.\\nuser: \"Aqui está o rascunho de nossa nova página de preços\"\\nassistente: \"Percebi que o título 'Nossos planos de preços' poderia ser mais atraente. Deixe-me usar o agente copy-redacao-publicitaria para sugerir alternativas que impulsionem conversões.\"\\n<commentary>\\nIdentificar proativamente oportunidades para melhorar o copy e sugerir o uso do agente copy-redacao-publicitaria.\\n</commentary>\\n</example>\\n\\n<example>\\nContexto: O usuário precisa de linhas de assunto de e-mail que aumentem as taxas de abertura.\\nuser: \"Escreva linhas de assunto para nossa campanha de e-mail de lançamento de produto\"\\assistente: \"Estou delegando ao agente copy-redacao-publicitaria para criar linhas de assunto com alta taxa de abertura que eliminam o ruído da caixa de entrada.\"\\n<commentary>\\nO marketing por e-mail requer uma cópia focada na conversão, então use o agente copy-redacao-publicitaria.\\n</commentary>\\n</example> |

### <a id="roteiro-de-video"></a>Roteiro De Video

| Recurso | Tipo | Origem | Descrição e Aplicação |
| :--- | :--- | :--- | :--- |
| <a id="copy-roteiro-de-video"></a>**`/copy-roteiro-de-video`** | `Workflow` | `0 Mkt` | Escreva scripts de vídeo envolventes para YouTube, TikTok e outras plataformas. Cria scripts completos com ganchos, conteúdo principal e CTAs. Suporta vários formatos, incluindo tutoriais, vlogs, análises, explicadores e narrativas. Use ao criar roteiros de vídeo, escrever conteúdo do YouTube ou planejar a estrutura do vídeo. |

### <a id="roteiro-mais-falado"></a>Roteiro Mais Falado

| Recurso | Tipo | Origem | Descrição e Aplicação |
| :--- | :--- | :--- | :--- |
| <a id="copy-roteiro-mais-falado"></a>**`/copy-roteiro-mais-falado`** | `Workflow` | `0 Mkt` | Transforma um roteiro de vídeo em uma versão mais falada e natural, removendo a linguagem de texto escrito e aumentando a sensação de proximidade. Use quando o usuário mencionar "roteiro de vídeo", "gravação", "mais falado", "soa natural", "parece que está falando", "está muito escrito/formal demais". |

### <a id="saas"></a>Saas

| Recurso | Tipo | Origem | Descrição e Aplicação |
| :--- | :--- | :--- | :--- |
| <a id="copy-saas"></a>**`copy-saas`** | `Skill` | `0 Mkt` | Copywriter de SaaS e startups focado em posicionamento, mensagem e pesquisa de voz do cliente (VOC), com um fluxo de 10 fases para criar uma landing page. Use para definir posicionamento e proposta de valor, montar a hierarquia de mensagem, minerar a linguagem do cliente e planejar o processo de uma landing page de SaaS. NÃO use para cartas de venda, CTAs e persuasão de resposta direta (use copy-conversao), para redigir a página seção a seção ou auditar CRO (use copy-landing-page), para roteiro de VSL (use copy-vsl) nem para email (use email-copy). |
| <a id="copy-saas"></a>**`/copy-saas`** | `Workflow` | `0 Mkt` | Redator de SaaS e startups focado em posicionamento, mensagem e pesquisa |

### <a id="vsl"></a>Vsl

| Recurso | Tipo | Origem | Descrição e Aplicação |
| :--- | :--- | :--- | :--- |
| <a id="copy-vsl"></a>**`copy-vsl`** | `Skill` | `0 Mkt` | Use para escrever roteiro de VSL (Video Sales Letter) de resposta direta: estrutura em 8 partes de Conrado Adolpho, tratamento universal de objeções, ritmo slide a slide e textos de retenção na tela. Gatilhos: \"VSL\", \"carta de vendas em vídeo\", \"roteiro de vendas em vídeo\". NÃO use para carta de vendas escrita (use copy-conversao), roteiro de Reels e Shorts (use copy-hooks-video-curto) nem landing page (use copy-landing-page). |

---

## <a id="data-inteligência-de-dados"></a>data (Inteligência de Dados)

Total de recursos nesta macro-área: `13`

### <a id="analise-de-desempenho"></a>Analise De Desempenho

| Recurso | Tipo | Origem | Descrição e Aplicação |
| :--- | :--- | :--- | :--- |
| <a id="data-analise-de-desempenho"></a>**`@data-analise-de-desempenho`** | `Agent` | `0 Mkt` | Especialista em análise de dados de marketing e insights de desempenho. |

### <a id="analise-de-funil"></a>Analise De Funil

| Recurso | Tipo | Origem | Descrição e Aplicação |
| :--- | :--- | :--- | :--- |
| <a id="data-analise-de-funil"></a>**`/data-analise-de-funil`** | `Workflow` | `0 Mkt` | Analise funis de conversão de usuários, calcule taxas de conversão passo a passo, crie visualizações interativas e identifique oportunidades de otimização. Use ao trabalhar com dados de jornada do usuário em várias etapas, análise de conversão ou quando o usuário mencionar funis, taxas de conversão ou análise de fluxo de usuário. |

### <a id="analytics-de-produto"></a>Analytics De Produto

| Recurso | Tipo | Origem | Descrição e Aplicação |
| :--- | :--- | :--- | :--- |
| <a id="data-analytics-de-produto"></a>**`/data-analytics-de-produto`** | `Workflow` | `0 Mkt` | Avalie o que é importante com rastreamento de eventos, funis, coortes e métricas adequados. Use ao configurar análises, recursos de rastreamento ou compreender o comportamento. |

### <a id="analytics-de-video"></a>Analytics De Video

| Recurso | Tipo | Origem | Descrição e Aplicação |
| :--- | :--- | :--- | :--- |
| <a id="data-analytics-de-video"></a>**`/data-analytics-de-video`** | `Workflow` | `0 Mkt` | Interprete dados do YouTube Analytics, TikTok Analytics e desempenho de vídeo. Identifica tendências, explica métricas e fornece recomendações práticas para crescimento. Use ao analisar o desempenho do vídeo, compreender as métricas ou otimizar a estratégia do canal. |

### <a id="atribuicao-e-relatorios"></a>Atribuicao E Relatorios

| Recurso | Tipo | Origem | Descrição e Aplicação |
| :--- | :--- | :--- | :--- |
| <a id="data-atribuicao-e-relatorios"></a>**`data-atribuicao-e-relatorios`** | `Skill` | `0 Mkt` | Especialista em modelagem de atribuição multi-canal, geração de relatórios executivos de marketing, auditoria de saúde de contas e dashboards automatizados para liderança. Use para contar o resultado do marketing em todos os canais. NÃO use para decidir alocação de verba, pausar anúncios ou projetar ROAS de campanha (use ads-analise-de-desempenho), engenharia de tags GTM e dataLayer (use data-web-ga4), coortes e retenção in-app (use data-funil-e-coortes) nem execução de testes A/B (use growth-testes-ab). |

### <a id="calculo-de-roi"></a>Calculo De Roi

| Recurso | Tipo | Origem | Descrição e Aplicação |
| :--- | :--- | :--- | :--- |
| <a id="data-calculo-de-roi"></a>**`/data-calculo-de-roi`** | `Workflow` | `0 Mkt` | Use ao preparar relatórios executivos, avaliar investimentos ou calcular ROI/ponto de equilíbrio/período de retorno. Análise de 30 minutos (87,5% de economia de tempo). Inclui análise de cenário. |

### <a id="funil-e-coortes"></a>Funil E Coortes

| Recurso | Tipo | Origem | Descrição e Aplicação |
| :--- | :--- | :--- | :--- |
| <a id="data-funil-e-coortes"></a>**`data-funil-e-coortes`** | `Skill` | `0 Mkt` | Use para analisar queda de funil (drop-off), retenção por coortes, ativação de usuários, onboarding e paywall em produtos digitais. Gatilhos: \"drop-off\", \"coorte\", \"ativação\", \"onboarding que não converte\", \"paywall\". NÃO use para tracking e GA4 (use data-web-ga4), atribuição e relatório executivo (use data-atribuicao-e-relatorios) nem para executar teste A/B (use growth-testes-ab). |

### <a id="gerador-de-utm"></a>Gerador De Utm

| Recurso | Tipo | Origem | Descrição e Aplicação |
| :--- | :--- | :--- | :--- |
| <a id="data-gerador-de-utm"></a>**`/data-gerador-de-utm`** | `Workflow` | `0 Mkt` | Gere URLs com tags UTM para rastreamento de campanha. Crie links de rastreamento consistentes e organizados para Google Analytics, HubSpot e outras plataformas analíticas. Suporta geração em massa, convenções de nomenclatura e documentação de campanha. Use ao criar links de rastreamento, URLs de campanha ou organizar atribuição de marketing. |

### <a id="interpretacao-de-analytics"></a>Interpretacao De Analytics

| Recurso | Tipo | Origem | Descrição e Aplicação |
| :--- | :--- | :--- | :--- |
| <a id="data-interpretacao-de-analytics"></a>**`/data-interpretacao-de-analytics`** | `Workflow` | `0 Mkt` | Interprete dados GA4 e GSC com benchmarks, indicadores de status e insights acionáveis |

### <a id="posthog"></a>Posthog

| Recurso | Tipo | Origem | Descrição e Aplicação |
| :--- | :--- | :--- | :--- |
| <a id="data-posthog"></a>**`/data-posthog`** | `Workflow` | `0 Mkt` | Análise PostHog, rastreamento de eventos, sinalizadores de recursos, painéis |

### <a id="relatorio-executivo"></a>Relatorio Executivo

| Recurso | Tipo | Origem | Descrição e Aplicação |
| :--- | :--- | :--- | :--- |
| <a id="data-relatorio-executivo"></a>**`/data-relatorio-executivo`** | `Workflow` | `0 Mkt` | Transforme dados brutos de CSVs, Planilhas Google ou bancos de dados em relatórios prontos para executivos com visualizações, principais métricas, análise de tendências e recomendações acionáveis. Cria narrativas baseadas em dados para liderança. Use quando os usuários precisarem transformar planilhas em resumos executivos ou relatórios do conselho. |

### <a id="revisao-mensal"></a>Revisao Mensal

| Recurso | Tipo | Origem | Descrição e Aplicação |
| :--- | :--- | :--- | :--- |
| <a id="data-revisao-mensal"></a>**`/data-revisao-mensal`** | `Workflow` | `0 Mkt` | Gera a revisão analítica mensal (tráfego, conversão, desempenho de conteúdo e campanhas) com comparação ao mês anterior. Use para consolidar os aprendizados do mês e definir prioridades do próximo. |

### <a id="web-ga4"></a>Web Ga4

| Recurso | Tipo | Origem | Descrição e Aplicação |
| :--- | :--- | :--- | :--- |
| <a id="data-web-ga4"></a>**`data-web-ga4`** | `Skill` | `0 Mkt` | Use para arquitetar dados web e implementar tracking: GA4, Google Tag Manager (web e server-side), Consent Mode v2, dataLayer e modelagem de eventos em BigQuery. Gatilhos: \"GA4\", \"GTM\", \"dataLayer\", \"Consent Mode\", \"evento de conversão\". NÃO use para atribuição multi-canal e relatório executivo (use data-atribuicao-e-relatorios), coortes e funil (use data-funil-e-coortes) nem para UTM de campanha (use o workflow data-gerador-de-utm). |

---

## <a id="email-email-marketing"></a>email (Email Marketing)

Total de recursos nesta macro-área: `8`

### <a id="automacao"></a>Automacao

| Recurso | Tipo | Origem | Descrição e Aplicação |
| :--- | :--- | :--- | :--- |
| <a id="email-automacao"></a>**`email-automacao`** | `Skill` | `0 Mkt` | Arquiteto de jornadas automatizadas de email e automações de ciclo de vida em CRMs (ActiveCampaign, HubSpot, Customer.io). Estrutura Welcome Series em 5 etapas, esteiras de onboarding e ativação de produto SaaS, fluxos de recuperação de carrinho abandonado, automações de reengajamento e Sunset Policy contra contatos inativos. NÃO use para estágios do contato, lead scoring e higiene de dados no CRM (use revenue-orquestracao-de-crm), copy de email (use email-copy), entregabilidade e DNS (use email-entregabilidade), prospecção fria (use vendas-cold-email) nem newsletters (use email-newsletter). |

### <a id="copy"></a>Copy

| Recurso | Tipo | Origem | Descrição e Aplicação |
| :--- | :--- | :--- | :--- |
| <a id="email-copy"></a>**`email-copy`** | `Skill` | `0 Mkt` | Use para escrever e-mails de marketing que convertem: linhas de assunto, preheaders, narrativas (Story-Lesson-Offer, Soap Opera, Seinfeld), texto puro versus HTML leve e otimização de CTOR. Gatilhos: \"assunto de e-mail\", \"copy de e-mail\", \"sequência de e-mails\". NÃO use para montar a automação e o fluxo (use email-automacao), para DNS e reputação de envio (use email-entregabilidade), para newsletter editorial (use email-newsletter) nem para cadência de prospecção fria (use vendas-cold-email). |

### <a id="entregabilidade"></a>Entregabilidade

| Recurso | Tipo | Origem | Descrição e Aplicação |
| :--- | :--- | :--- | :--- |
| <a id="email-entregabilidade"></a>**`email-entregabilidade`** | `Skill` | `0 Mkt` | Use para proteger a entregabilidade de e-mail (inbox placement): registros DNS (SPF, DKIM, DMARC, BIMI), aquecimento de domínio de 21 dias, higiene de lista contra spam traps e monitoramento de reputação no Google Postmaster. Gatilhos: \"caiu no spam\", \"SPF DKIM DMARC\", \"warm-up\", \"reputação de domínio\". NÃO use para escrever o e-mail (use email-copy) nem para montar sequências e automações (use email-automacao). |

### <a id="modelos"></a>Modelos

| Recurso | Tipo | Origem | Descrição e Aplicação |
| :--- | :--- | :--- | :--- |
| <a id="email-modelos"></a>**`/email-modelos`** | `Workflow` | `0 Mkt` | Gere modelos de e-mail profissionais para vários cenários de negócios, incluindo divulgação de vendas, suporte ao cliente, comunicações internas, acompanhamentos e desculpas. Cria modelos personalizados e adequados ao tom, com linhas de assunto e formatação. Use quando os usuários precisarem escrever e-mails comerciais, divulgação não solicitada ou comunicações profissionais. |

### <a id="newsletter"></a>Newsletter

| Recurso | Tipo | Origem | Descrição e Aplicação |
| :--- | :--- | :--- | :--- |
| <a id="email-newsletter"></a>**`email-newsletter`** | `Skill` | `0 Mkt` | Use para transformar a experiência diária do autor em rascunhos de newsletter prontos para publicar, com playbooks editoriais, estratégias de crescimento, curadoria e modelos por setor (Tech, Fintech, RH, Vendas, Operações). Gatilhos: \"newsletter\", \"edição semanal\", \"crescer newsletter\". NÃO use para sequências de nutrição e automação (use email-automacao), para copy de e-mail promocional (use email-copy) nem para artigo de blog (use conteudo-post-de-blog). |
| <a id="email-newsletter"></a>**`/email-newsletter`** | `Workflow` | `0 Mkt` | Treinador de redação que extrai conteúdo educacional de suas experiências diárias |

### <a id="orquestracao-de-campanhas"></a>Orquestracao De Campanhas

| Recurso | Tipo | Origem | Descrição e Aplicação |
| :--- | :--- | :--- | :--- |
| <a id="email-orquestracao-de-campanhas"></a>**`@email-orquestracao-de-campanhas`** | `Agent` | `0 Mkt` | Especialista em orquestração de campanhas de e-mail. Use para criar modelos de sequência, personalização dinâmica, estratégias de otimização de tempo de envio e estruturas de teste A/B. Exemplos: <exemplo>Contexto: o usuário precisa configurar a automação de e-mail. usuário: \"Crie uma sequência de e-mail de boas-vindas para novos assinantes\" assistente: \"Usarei o agente email-orquestracao-de-campanhas para criar uma sequência de boas-vindas com personalização e timing ideal.\" <commentary>O design da sequência de e-mail requer experiência em automação e otimização de engajamento.</commentary></example> <example>Contexto: O usuário deseja melhorar o desempenho do e-mail. usuário: \"Nossas taxas de abertura de e-mail estão diminuindo\" assistente: \"Deixe-me implantar o agente email-orquestracao-de-campanhas para auditar seus e-mails e criar um plano de testes A/B.\" <commentary>A otimização de e-mail requer profundo conhecimento da capacidade de entrega e dos fatores de engajamento.</commentary></example> |

### <a id="otimizacao-de-assunto"></a>Otimizacao De Assunto

| Recurso | Tipo | Origem | Descrição e Aplicação |
| :--- | :--- | :--- | :--- |
| <a id="email-otimizacao-de-assunto"></a>**`/email-otimizacao-de-assunto`** | `Workflow` | `0 Mkt` | Teste A/B de variações de linha de assunto usando estruturas de copywriting comprovadas. Preveja taxas de abertura com base no desempenho histórico. |

---

## <a id="geral-geral--governança"></a>geral (Geral & Governança)

Total de recursos nesta macro-área: `24`

### <a id="anti-slop"></a>Anti Slop

| Recurso | Tipo | Origem | Descrição e Aplicação |
| :--- | :--- | :--- | :--- |
| <a id="geral-anti-slop"></a>**`geral-anti-slop`** | `Skill` | `0 Mkt` | Detecta e remove padrões de escrita de IA do texto. Use ao aprimorar rascunhos, limpar conteúdo gerado por IA ou garantir que a escrita pareça autenticamente humana. Invoque com "passar pelo detector de resíduos", "limpar" ou "remover impressões digitais de IA". |
| <a id="geral-anti-slop"></a>**`/geral-anti-slop`** | `Workflow` | `0 Mkt` | Detecta e remove padrões de escrita de IA do texto. Use ao polir |

### <a id="arquitetura-de-projeto"></a>Arquitetura De Projeto

| Recurso | Tipo | Origem | Descrição e Aplicação |
| :--- | :--- | :--- | :--- |
| <a id="geral-arquitetura-de-projeto"></a>**`geral-arquitetura-de-projeto`** | `Skill` | `0 Mkt` | Use ao criar ou reorganizar as pastas de um projeto de marketing, ao decidir onde uma peça (arquivo de marca, estratégia, campanha, post, pitch de imprensa, relatório de monitoramento, ativo, dados, plano) deve ser salva, quando o projeto tiver mais de uma marca ou produto, ou quando uma habilidade precisar do mapa de destino do projeto antes de escrever um arquivo. |

### <a id="briefing-matinal"></a>Briefing Matinal

| Recurso | Tipo | Origem | Descrição e Aplicação |
| :--- | :--- | :--- | :--- |
| <a id="geral-briefing-matinal"></a>**`/geral-briefing-matinal`** | `Workflow` | `0 Mkt` | Gera o briefing matinal consolidado de marketing e prioridades de conteúdo. Use para planejar o dia de trabalho, identificar pautas não publicadas e alinhar entregas prioritárias. |

### <a id="conformidade-lgpd"></a>Conformidade Lgpd

| Recurso | Tipo | Origem | Descrição e Aplicação |
| :--- | :--- | :--- | :--- |
| <a id="geral-conformidade-lgpd"></a>**`geral-conformidade-lgpd`** | `Skill` | `0 Mkt` | Use para conformidade de marketing digital: LGPD e GDPR, consentimento (Consent Mode v2), formulários de captura, revisão de contratos, NDAs de influenciadores e análise de termos de uso. É triagem para orientar o trabalho de marketing; a decisão jurídica final é de advogado. Gatilhos: \"LGPD\", \"GDPR\", \"consentimento\", \"política de privacidade\", \"NDA\", \"contrato de influenciador\". NÃO use para implementar tags e eventos de rastreamento (use data-web-ga4) nem para regras de e-mail e entregabilidade (use email-entregabilidade). |

### <a id="coordenacao-de-campanhas"></a>Coordenacao De Campanhas

| Recurso | Tipo | Origem | Descrição e Aplicação |
| :--- | :--- | :--- | :--- |
| <a id="geral-coordenacao-de-campanhas"></a>**`@geral-coordenacao-de-campanhas`** | `Agent` | `0 Mkt` | Especialista em gestão e coordenação de campanhas. Use para acompanhar o progresso da campanha, coordenar atividades de marketing, gerenciar prazos e fornecer relatórios de status. Exemplos: <exemplo>Contexto: o usuário precisa de supervisão da campanha. usuário: \"Verificar o status da nossa campanha de lançamento de produto\" assistente: \"Utilizarei o agente geral-coordenacao-de-campanhas para revisar o progresso da campanha e fornecer um relatório de status.\" <commentary>A coordenação da campanha requer o acompanhamento de vários fluxos de trabalho e prazos.</commentary></example> <example>Contexto: usuário gerenciando múltiplas campanhas. usuário: \"Dê-me uma visão geral de todas as campanhas de marketing ativas\" assistente: \"Deixe-me usar o agente geral-coordenacao-de-campanhas para consolidar o status da campanha em todas as iniciativas.\" <commentary>O gerenciamento de múltiplas campanhas requer monitoramento e relatórios sistemáticos.</commentary></example> |

### <a id="diagrama-mermaid"></a>Diagrama Mermaid

| Recurso | Tipo | Origem | Descrição e Aplicação |
| :--- | :--- | :--- | :--- |
| <a id="geral-diagrama-mermaid"></a>**`/geral-diagrama-mermaid`** | `Workflow` | `0 Mkt` | Crie diagramas e visualizações usando a sintaxe Mermaid. Use ao gerar fluxogramas, diagramas de sequência, diagramas de classes, diagramas de entidade-relacionamento, gráficos de Gantt ou qualquer documentação visual. Gatilhos no Mermaid, fluxograma, diagrama de sequência, diagrama de classes, diagrama ER, gráfico de Gantt, diagrama, visualização. |

### <a id="execucao-autonoma"></a>Execucao Autonoma

| Recurso | Tipo | Origem | Descrição e Aplicação |
| :--- | :--- | :--- | :--- |
| <a id="geral-execucao-autonoma"></a>**`/geral-execucao-autonoma`** | `Workflow` | `0 Mkt` | Execução autônoma de metas complexas de marketing com ciclo de 5 fases (Meta -> Plano -> Confirmação -> Execução -> Relatório). Você direciona, o agente executável. |

### <a id="extracao-e-plano-de-acao"></a>Extracao E Plano De Acao

| Recurso | Tipo | Origem | Descrição e Aplicação |
| :--- | :--- | :--- | :--- |
| <a id="geral-extracao-e-plano-de-acao"></a>**`/geral-extracao-e-plano-de-acao`** | `Workflow` | `0 Mkt` | Extração de conteúdo unificada e planejamento de ações. Use quando o usuário disser "tapeçaria <URL>", "tecer <URL>", "ajude-me a planejar <URL>", "extrair e planejar <URL>", "tornar este <URL> acionável" ou frases semelhantes indicando que deseja extrair conteúdo e criar um plano de ação. Detecta automaticamente o tipo de conteúdo (vídeo do YouTube, artigo, PDF) e processa de acordo. |

### <a id="gestao-de-documentacao"></a>Gestao De Documentacao

| Recurso | Tipo | Origem | Descrição e Aplicação |
| :--- | :--- | :--- | :--- |
| <a id="geral-gestao-de-documentacao"></a>**`@geral-gestao-de-documentacao`** | `Agent` | `0 Mkt` | Use este agente quando precisar gerenciar documentação de marketing, estabelecer diretrizes de marca, analisar e atualizar documentação existente com base em alterações de campanha, escrever ou atualizar Requisitos de Desenvolvimento de Marketing (MDRs), organizar documentação para produtividade da equipe de marketing ou produzir relatórios resumidos de documentação. Isso inclui tarefas como revisar a estrutura da documentação, garantir que os documentos estejam atualizados com os ativos da campanha, criar nova documentação para as campanhas e manter a consistência em toda a documentação de marketing.\\n\\nExemplos:\\n- <exemplo>\\n Contexto: depois de lançar uma nova campanha, a documentação precisa ser atualizada.\\n usuário: \"Acabamos de lançar a campanha de reconhecimento da marca do quarto trimestre\"\\n assistente: \"Vou usar o agente geral-gestao-de-documentacao para atualizar o documentação para esta campanha\"\\n <commentary>\\n Desde o lançamento da nova campanha, use o agente geral-gestao-de-documentacao para garantir que a documentação seja atualizada adequadamente.\\n </commentary>\\n</example>\\n- <example>\\n Contexto: A documentação de marketing precisa de revisão e organização.\\n usuário: \"Você pode revisar nossa pasta de documentos e ter certeza de que tudo está devidamente organizado?\"\\n assistente: \"Vou iniciar o agente geral-gestao-de-documentacao para analisar e organizar a documentação\"\\n <commentary>\\n O usuário está solicitando revisão e organização da documentação, que é a especialidade do agente geral-gestao-de-documentacao.\\n </commentary>\\n</example>\\n- <example>\\n Contexto: Necessidade de estabelecer documentação de diretrizes de marca.\\n usuário: \"Precisamos documentar a voz de nossa marca e estilo de conteúdo assistente de padrões\"\\n: \"Deixe-me usar o agente geral-gestao-de-documentacao para estabelecer e documentar essas diretrizes da marca\"\\n <commentary>\\n Criar a documentação das diretrizes da marca é uma responsabilidade central do agente geral-gestao-de-documentacao.\\n </commentary>\\n</example> |

### <a id="mapa-de-stakeholders"></a>Mapa De Stakeholders

| Recurso | Tipo | Origem | Descrição e Aplicação |
| :--- | :--- | :--- | :--- |
| <a id="geral-mapa-de-stakeholders"></a>**`/geral-mapa-de-stakeholders`** | `Workflow` | `0 Mkt` | Use ao projetar estrutura organizacional (topologias de equipe, alinhamento da Lei de Conway), mapear as partes interessadas por interesse de poder para iniciativas de mudança, definir contratos de interface de equipe (APIs, SLAs, direitos de decisão, transferências), avaliar a maturidade de capacidade (DORA, CMMC, modelos ágeis de maturidade), planejar reestruturações organizacionais (funcionais para equipes de produto, equipes de plataforma, serviços compartilhados) ou quando o usuário mencionar "design organizacional", "estrutura de equipe", "mapa de partes interessadas", "interfaces de equipe", "maturidade de capacidade", "Lei de Conway" ou "RACI". |

### <a id="navegador-de-comandos"></a>Navegador De Comandos

| Recurso | Tipo | Origem | Descrição e Aplicação |
| :--- | :--- | :--- | :--- |
| <a id="geral-navegador-de-comandos"></a>**`@geral-navegador-de-comandos`** | `Agent` | `0 Mkt` | Assistente de comandos: entende a intenção do usuário e sugere o workflow, skill ou agente certo. Não é preciso memorizar nomes. Examples: <example>Context: User doesn't know which command to use. user: \"Quero escrever um post de blog\" assistant: \"Vou usar o geral-navegador-de-comandos para achar o melhor comando para essa tarefa.\" <commentary>Descoberta de comando exige entender a intenção e casar com o que existe no .agent/.</commentary></example> |

### <a id="navegador-de-skills"></a>Navegador De Skills

| Recurso | Tipo | Origem | Descrição e Aplicação |
| :--- | :--- | :--- | :--- |
| <a id="geral-navegador-de-skills"></a>**`/geral-navegador-de-skills`** | `Workflow` | `0 Mkt` | Guia inteligente para as skills reais do catálogo do hub Super IA Projects - Marketing. Recomenda a skill certa para cada pedido, sugere combinações de skills e ajuda a descobrir capacidades que o usuário talvez não conheça. |

### <a id="operações-e-rotinas"></a>Operações e Rotinas

| Recurso | Tipo | Origem | Descrição e Aplicação |
| :--- | :--- | :--- | :--- |
| <a id="design-direcao-criativa"></a>**`/design-direcao-criativa`** | `Workflow` | `0 Mkt` | Workflow de direção de arte e criação visual em 6 etapas: entendimento, conceito, direção de arte com 3 vias divergentes, paleta funcional, tipografia e layout, com prompts de IA multi-engine e autocrítica (0 a 10). Use para criar conceitos visuais, direções de campanha, identidades ou peças de alto padrão estético. |

### <a id="parecer-sexy-canvas"></a>Parecer Sexy Canvas

| Recurso | Tipo | Origem | Descrição e Aplicação |
| :--- | :--- | :--- | :--- |
| <a id="geral-parecer-sexy-canvas"></a>**`@geral-parecer-sexy-canvas`** | `Agent` | `0 Mkt` | Utilize quando o usuário deseja uma leitura consultiva de um texto, vídeo, imagem, produto ou ideia através do Sexy Canvas (auditar, sugerir, adaptar, direcionar antes de criar, ou uma “visão dos 14”), ou perguntar por que algo não atrai, converte ou engaja. Fornece uma opinião e uma transferência, nunca a peça final. |

### <a id="persona-fundador-startup"></a>Persona Fundador Startup

| Recurso | Tipo | Origem | Descrição e Aplicação |
| :--- | :--- | :--- | :--- |
| <a id="geral-persona-fundador-startup"></a>**`@geral-persona-fundador-startup`** | `Agent` | `0 Mkt` | Revisor da persona do fundador da startup (28 anos, fundador em estágio inicial). Use para revisar conteúdo da perspectiva de um jovem fundador de uma startup. Avalia o conteúdo quanto à velocidade, growth hacking, potencial de viralidade, adequação ao mercado do fundador e execução fragmentada. Exemplos: <exemplo>Contexto: conteúdo de marketing de inicialização criado pelo usuário. usuário: \"Revise isso da perspectiva do fundador de uma startup\" assistente: \"Usarei o agente geral-persona-fundador-startup para avaliar do ponto de vista do fundador: potencial de crescimento, velocidade de lançamento no mercado e restrições de recursos.\" <commentary>A perspectiva do fundador da startup se concentra no crescimento rápido e na execução fragmentada.</commentary></example> |

### <a id="persona-gerente-de-marketing"></a>Persona Gerente De Marketing

| Recurso | Tipo | Origem | Descrição e Aplicação |
| :--- | :--- | :--- | :--- |
| <a id="geral-persona-gerente-de-marketing"></a>**`@geral-persona-gerente-de-marketing`** | `Agent` | `0 Mkt` | Persona revisora (não é um cargo de execução): simula uma gerente de marketing de 38 anos, empresa de porte médio, revendo conteúdo pronto. Use for reviewing content from the perspective of an experienced marketing manager. Evaluates content for team collaboration, scalability, enterprise needs, and practical implementation. Examples: <example>Context: User created B2B marketing content. user: \"Review this from a marketing manager's perspective\" assistant: \"I'll use the geral-persona-gerente-de-marketing agent to evaluate from an experienced manager's viewpoint—team needs, workflow integration, and enterprise considerations.\" <commentary>Manager perspective provides insights on practical implementation and team dynamics.</commentary></example> |

### <a id="persona-solopreneur"></a>Persona Solopreneur

| Recurso | Tipo | Origem | Descrição e Aplicação |
| :--- | :--- | :--- | :--- |
| <a id="geral-persona-solopreneur"></a>**`@geral-persona-solopreneur`** | `Agent` | `0 Mkt` | Revisor de persona Solopreneur (32 anos, freelancer/consultor). Use para revisar o conteúdo da perspectiva de um profissional independente ou proprietário de uma pequena empresa. Avalia o conteúdo quanto à facilidade de autoatendimento, eficiência de tempo, acessibilidade e implementação DIY. Exemplos: <exemplo>Contexto: conteúdo criado pelo usuário para pequenas empresas. usuário: \"Revise isso da perspectiva de um solopreneur\" assistente: \"Usarei o agente geral-persona-solopreneur para avaliar do ponto de vista empresarial de uma pessoa - restrições de tempo, sensibilidade orçamentária e autoimplementação.\" <commentary>A perspectiva do solopreneur destaca preocupações práticas para profissionais independentes.</commentary></example> |

### <a id="planejamento-diario"></a>Planejamento Diario

| Recurso | Tipo | Origem | Descrição e Aplicação |
| :--- | :--- | :--- | :--- |
| <a id="geral-planejamento-diario"></a>**`/geral-planejamento-diario`** | `Workflow` | `0 Mkt` | Gera um diário de planejamento estruturado por blocos de tempo e energia (ritmo circadiano e GTD) para profissionais e líderes de marketing. |

### <a id="postmortem"></a>Postmortem

| Recurso | Tipo | Origem | Descrição e Aplicação |
| :--- | :--- | :--- | :--- |
| <a id="geral-postmortem"></a>**`/geral-postmortem`** | `Workflow` | `0 Mkt` | Use ao analisar falhas, interrupções, incidentes ou resultados negativos, realizar análises post-mortem sem culpa, documentar as causas raízes com 5 porquês ou diagramas de espinha de peixe, identificar ações corretivas com proprietários e cronogramas, aprender com quase acidentes, estabelecer estratégias de prevenção ou quando o usuário mencionar análises post-mortem, revisão de incidentes, análise de falhas, RCA, lições aprendidas ou revisão pós-ação. |

### <a id="priorizacao-esforco-impacto"></a>Priorizacao Esforco Impacto

| Recurso | Tipo | Origem | Descrição e Aplicação |
| :--- | :--- | :--- | :--- |
| <a id="geral-priorizacao-esforco-impacto"></a>**`/geral-priorizacao-esforco-impacto`** | `Workflow` | `0 Mkt` | Use ao classificar pendências, decidir o que fazer primeiro com base no esforço versus impacto (ganhos rápidos versus grandes apostas), priorizar roteiros de recursos, triagem de bugs ou dívida técnica, alocar recursos entre iniciativas, identificar frutos mais fáceis de alcançar, avaliar opções estratégicas com matriz 2x2 ou quando o usuário mencionar priorização, ganhos rápidos, matriz de esforço-impacto, alto impacto e baixo esforço, grandes apostas ou perguntar "o que devemos fazer primeiro?". |

### <a id="revisao-mensal"></a>Revisao Mensal

| Recurso | Tipo | Origem | Descrição e Aplicação |
| :--- | :--- | :--- | :--- |
| <a id="geral-revisao-mensal"></a>**`/geral-revisao-mensal`** | `Workflow` | `0 Mkt` | Gera a revisão mensal de desempenho de marketing e ajuste de estratégia para o mês seguinte. Use para compilar métricas do mês, analisar funil e canais, e planejar o próximo mês. |

### <a id="revisao-semanal"></a>Revisao Semanal

| Recurso | Tipo | Origem | Descrição e Aplicação |
| :--- | :--- | :--- | :--- |
| <a id="geral-revisao-semanal"></a>**`/geral-revisao-semanal`** | `Workflow` | `0 Mkt` | Gera a revisão semanal de marketing e o planejamento da semana seguinte. Use para revisar métricas da semana, status de campanhas e conteúdo, e planejar as prioridades da próxima semana. |

### <a id="verificacao-de-fatos"></a>Verificacao De Fatos

| Recurso | Tipo | Origem | Descrição e Aplicação |
| :--- | :--- | :--- | :--- |
| <a id="geral-verificacao-de-fatos"></a>**`/geral-verificacao-de-fatos`** | `Workflow` | `0 Mkt` | Verifica afirmações factuais em documentos usando pesquisa na web e fontes oficiais e, em seguida, propõe correções com confirmação do usuário. Use quando o usuário solicitar verificação de fatos, verificação de informações, validação de reivindicações, verificação de precisão ou atualização de informações desatualizadas em documentos. Suporta especificações de modelo de IA, documentação técnica, estatísticas e declarações factuais gerais. |

---

## <a id="growth-growth-hacking"></a>growth (Growth Hacking)

Total de recursos nesta macro-área: `11`

### <a id="aquisicao-de-demanda"></a>Aquisicao De Demanda

| Recurso | Tipo | Origem | Descrição e Aplicação |
| :--- | :--- | :--- | :--- |
| <a id="growth-aquisicao-de-demanda"></a>**`/growth-aquisicao-de-demanda`** | `Workflow` | `0 Mkt` | Geração de demanda multicanal, otimização de mídia paga, estratégia de SEO e programas de parceria para startups Série A+. Inclui calculadora CAC, manuais de canal, integração HubSpot e táticas de expansão internacional. Use ao planejar campanhas de geração de demanda, otimizar mídia paga, construir estratégias de SEO, estabelecer parcerias ou quando o usuário mencionar geração de demanda, anúncios pagos, anúncios do LinkedIn, anúncios do Google, CAC, aquisição, geração de leads ou geração de pipeline. |

### <a id="aquisicao-de-usuarios"></a>Aquisicao De Usuarios

| Recurso | Tipo | Origem | Descrição e Aplicação |
| :--- | :--- | :--- | :--- |
| <a id="growth-aquisicao-de-usuarios"></a>**`@growth-aquisicao-de-usuarios`** | `Agent` | `0 Mkt` | Especialista em growth hacking e aquisição de usuários. |

### <a id="atracao-de-leads"></a>Atracao De Leads

| Recurso | Tipo | Origem | Descrição e Aplicação |
| :--- | :--- | :--- | :--- |
| <a id="growth-atracao-de-leads"></a>**`@growth-atracao-de-leads`** | `Agent` | `0 Mkt` | Especialista em geração de leads e marketing no topo do funil (TOFU). Use para pesquisa de palavras-chave, inteligência de conteúdo da concorrência, geração de landing pages, SEO programático e estratégias de distribuição de conteúdo. Exemplos: <exemplo>Contexto: o usuário deseja melhorar o tráfego de pesquisa orgânica. usuário: \"Precisamos ter uma classificação mais elevada para palavras-chave relacionadas ao produto\" assistente: \"Vou usar o agente de atração de crescimento de leads para conduzir pesquisas de palavras-chave e desenvolver uma estratégia de conteúdo de SEO." usuário: \"Criar páginas de destino para o lançamento de nosso novo produto\" assistente: \"Deixe-me implantar o agente de atração de crescimento de leads para gerar uma cópia da página de destino de alta conversão.\" <commentary>A geração de páginas de destino requer experiência em redação com foco na conversão.</commentary></example> |

### <a id="expansao-de-receita"></a>Expansao De Receita

| Recurso | Tipo | Origem | Descrição e Aplicação |
| :--- | :--- | :--- | :--- |
| <a id="growth-expansao-de-receita"></a>**`@growth-expansao-de-receita`** | `Agent` | `0 Mkt` | Especialista em expansão de receita. Use para identificar oportunidades de upsell, recomendações de produtos, previsão de expansão e estratégias de rastreamento de adoção de recursos. Exemplos: <exemplo>Contexto: o usuário deseja aumentar a receita dos clientes existentes. usuário: \"Como podemos aumentar a receita dos clientes atuais?\" assistente: \"Usarei o agente de expansão de crescimento de receita para identificar oportunidades de expansão e criar campanhas de upsell.\" <commentary>A expansão da receita requer análise de uso e timing estratégico de oferta.</commentary></example> <example>Contexto: usuário lançando novos recursos. usuário: \"Promova nossos novos recursos premium para usuários existentes\" assistente: \"Deixe-me implantar o agente de expansão de crescimento para criar campanhas de adoção de recursos com caminhos de atualização.\" <commentary>Campanhas de adoção de recursos exigem posicionamento e timing estratégicos.</commentary></example> |

### <a id="experimentos-gtm"></a>Experimentos Gtm

| Recurso | Tipo | Origem | Descrição e Aplicação |
| :--- | :--- | :--- | :--- |
| <a id="growth-experimentos-gtm"></a>**`growth-experimentos-gtm`** | `Skill` | `0 Mkt` | Biblioteca com 500+ experimentos de Go-to-Market para B2B (growth hacking, growth marketing, sales, PLG, ABM, pricing, retenção, expansão, GEO/AI search, founder-led, AI-native GTM) com hipótese, métrica e benchmark, baseada em autoridades do segmento (Kyle Poyar/Growth Unhinged, Tom Tunguz/Theory Ventures, Reforge, CXL/Speero, Clay, ChartMogul, McKinsey, Gartner, SaaStr, PricingSaaS). Use sempre que o usuário pedir ideias de experimentos B2B, growth experiments, testes A/B, hipóteses para destravar funil B2B, sugestões de outbound, ABM, PLG, SEO, GEO, pricing, sales methodologies, retenção, NRR, expansão, indicação, ou inspiração para conteúdo de growth. Trigger também ao detectar "experimentos", "testes", "ideias de growth", "como aumentar conversão/CAC/NRR/MRR", "playbook", "reduzir churn", "aumentar pipeline", ou pedidos de curadoria de táticas para SaaS, indústria, agro, enterprise, serviço B2B. NÃO use para estratégia geral de growth e métricas (use growth-frameworks), para rodar o teste A/B em si (use growth-testes-ab) nem para experimentos de B2C ou conteúdo de redes sociais. |

### <a id="frameworks"></a>Frameworks

| Recurso | Tipo | Origem | Descrição e Aplicação |
| :--- | :--- | :--- | :--- |
| <a id="growth-frameworks"></a>**`growth-frameworks`** | `Skill` | `0 Mkt` | Especialista em estratégia de crescimento: métricas AARRR, growth loops, Product-Led Growth (PLG), Lean Canvas, métricas de startup, geração de demanda e ideias e táticas de marketing. NÃO use para retenção e saúde de clientes (use growth-retencao-e-churn), crise de reputação (use pr-assessoria-de-imprensa), psicologia do consumidor (use revenue-psicologia) nem decisões e modelos mentais (use revenue-modelos-mentais). |

### <a id="indicacao-e-afiliados"></a>Indicacao E Afiliados

| Recurso | Tipo | Origem | Descrição e Aplicação |
| :--- | :--- | :--- | :--- |
| <a id="growth-indicacao-e-afiliados"></a>**`growth-indicacao-e-afiliados`** | `Skill` | `0 Mkt` | Use para desenhar programa de indicação de clientes (recompensa nos dois lados), programa de afiliados e parceiros, modelo de comissão e embaixadores, e para calcular o coeficiente viral (K-factor). Gatilhos: \"programa de indicação\", \"afiliados\", \"comissão\", \"embaixadores\", \"K-factor\", \"loop viral\". NÃO use para estratégia geral de growth (AARRR, North Star, experimentos ICE: use growth-frameworks), retenção e churn (use growth-retencao-e-churn) nem copy de anúncio (use ads-copy-de-anuncio). |

### <a id="retencao-de-clientes"></a>Retencao De Clientes

| Recurso | Tipo | Origem | Descrição e Aplicação |
| :--- | :--- | :--- | :--- |
| <a id="growth-retencao-de-clientes"></a>**`@growth-retencao-de-clientes`** | `Agent` | `0 Mkt` | Especialista em retenção e engajamento de clientes. Use para estratégias de detecção de rotatividade, campanhas de reengajamento, automação de NPS e sequências de coleta de depoimentos. Exemplos: <exemplo>Contexto: o usuário está vendo uma rotatividade de clientes. usuário: \"Nossa taxa de retenção de clientes está caindo\" assistente: \"Usarei o agente de retenção de crescimento de clientes para analisar padrões de rotatividade e projetar campanhas de reengajamento.\" <commentary>A estratégia de retenção requer análise comportamental e experiência em marketing de ciclo de vida.</commentary></example> <example>Contexto: o usuário deseja feedback do cliente. usuário: \"Configurar um programa de pesquisa NPS\" assistente: \"Deixe-me implantar o agente de retenção de crescimento de clientes para projetar uma automação NPS com sequências de acompanhamento.\" <commentary>Os programas NPS exigem tempo estratégico e fluxos de trabalho de resposta.</commentary></example> |

### <a id="retencao-e-churn"></a>Retencao E Churn

| Recurso | Tipo | Origem | Descrição e Aplicação |
| :--- | :--- | :--- | :--- |
| <a id="growth-retencao-e-churn"></a>**`growth-retencao-e-churn`** | `Skill` | `0 Mkt` | Engineer high-converting retention engines, cancel flows, dynamic save offers, exit surveys, and dunning systems to slash voluntary and involuntary subscription churn. Also covers customer health scoring, churn prediction, expansion (upsell) signals, QBR (revisão trimestral) e renovação de contrato. NÃO use para estágios do contato e lead scoring no CRM (use revenue-orquestracao-de-crm) nem para atribuição de marketing (use data-atribuicao-e-relatorios). |

### <a id="teste-ab"></a>Teste Ab

| Recurso | Tipo | Origem | Descrição e Aplicação |
| :--- | :--- | :--- | :--- |
| <a id="growth-teste-ab"></a>**`/growth-teste-ab`** | `Workflow` | `0 Mkt` | Gera o plano de um teste A/B de marketing (hipótese, variantes, critério estatístico e cronograma mínimo). Use quando for testar um elemento de e-mail, landing page, anúncio ou site. |

### <a id="testes-ab"></a>Testes Ab

| Recurso | Tipo | Origem | Descrição e Aplicação |
| :--- | :--- | :--- | :--- |
| <a id="growth-testes-ab"></a>**`growth-testes-ab`** | `Skill` | `0 Mkt` | Use para desenhar a estratégia e a estatística de testes A/B, A/B/n e multivariados: hipóteses, tamanho de amostra, significância e governança do programa de testes. Gatilhos: \"teste A/B\", \"hipótese de teste\", \"significância\", \"MVT\". NÃO use para executar o passo a passo de um teste pontual (use o workflow growth-teste-ab), para auditar a página (use site-cro) nem para analisar o funil (use data-funil-e-coortes). |

---

## <a id="persona-clientes--persona"></a>persona (Clientes & Persona)

Total de recursos nesta macro-área: `7`

### <a id="analise-de-feedback"></a>Analise De Feedback

| Recurso | Tipo | Origem | Descrição e Aplicação |
| :--- | :--- | :--- | :--- |
| <a id="persona-analise-de-feedback"></a>**`/persona-analise-de-feedback`** | `Workflow` | `0 Mkt` | Sintetize o feedback do usuário de vários canais e identifique padrões para informar decisões sobre produtos. Use ao analisar feedback, priorizar solicitações de recursos, realizar pesquisas de NPS ou compreender o sentimento do usuário. Abrange coleta de feedback, categorização, estruturas de priorização e fechamento do ciclo de feedback. |

### <a id="criacao-de-persona"></a>Criacao De Persona

| Recurso | Tipo | Origem | Descrição e Aplicação |
| :--- | :--- | :--- | :--- |
| <a id="persona-criacao-de-persona"></a>**`/persona-criacao-de-persona`** | `Workflow` | `0 Mkt` | Crie personas de usuário detalhadas com base em pesquisas e dados. Desenvolva representações realistas dos usuários-alvo para orientar as decisões de produtos e garantir um design centrado no usuário. |

### <a id="descoberta-de-clientes"></a>Descoberta De Clientes

| Recurso | Tipo | Origem | Descrição e Aplicação |
| :--- | :--- | :--- | :--- |
| <a id="persona-descoberta-de-clientes"></a>**`persona-descoberta-de-clientes`** | `Skill` | `0 Mkt` | Use para validar ideia, problema e solução com clientes: Mom Test, entrevista de problema e de solução, Customer Development (Steve Blank), descoberta contínua de produto (Teresa Torres) e pesquisas (surveys). Gatilhos: \"validar ideia\", \"entrevista com clientes\", \"Mom Test\", \"descoberta de produto\". NÃO use para definir ICP e personas (use persona-icp), gravar entrevista de podcast (use audiovisual-podcast-e-audio) nem pesquisar preço (use revenue-preco). |

### <a id="descoberta-interativa"></a>Descoberta Interativa

| Recurso | Tipo | Origem | Descrição e Aplicação |
| :--- | :--- | :--- | :--- |
| <a id="persona-descoberta-interativa"></a>**`@persona-descoberta-interativa`** | `Agent` | `0 Mkt` | Agente interativo de descoberta da personalidade do cliente. Use quando precisar criar perfis detalhados de clientes por meio de conversas. Faz perguntas estratégicas com opções inteligentes, coleta respostas progressivamente e constrói buyer personas abrangentes. Exemplos: <exemplo>Contexto: o usuário deseja entender seu cliente. usuário: \"Ajude-me a entender quem é meu cliente ideal\" assistente: \"Usarei o agente persona-descoberta-interativa para conduzir uma sessão interativa de descoberta e construir seu perfil de cliente." <commentary>Construir personas requer questionamento e síntese progressiva.</commentary></example> |

### <a id="entrevistas-de-descoberta"></a>Entrevistas De Descoberta

| Recurso | Tipo | Origem | Descrição e Aplicação |
| :--- | :--- | :--- | :--- |
| <a id="persona-entrevistas-de-descoberta"></a>**`/persona-entrevistas-de-descoberta`** | `Workflow` | `0 Mkt` | Use ao validar suposições do produto antes de construí-lo, descobrir necessidades não atendidas do usuário, entender problemas e fluxos de trabalho do cliente, testar conceitos ou posicionamento, pesquisar mercados-alvo, identificar tarefas a serem realizadas e gatilhos de contratação, descobrir pontos problemáticos e soluções alternativas ou quando os usuários mencionarem pesquisas de usuários, entrevistas com clientes, pesquisas, entrevistas de descoberta, estudos de validação ou voz do cliente. |

### <a id="gerador-de-icp"></a>Gerador De Icp

| Recurso | Tipo | Origem | Descrição e Aplicação |
| :--- | :--- | :--- | :--- |
| <a id="persona-gerador-de-icp"></a>**`/persona-gerador-de-icp`** | `Workflow` | `0 Mkt` | Crie buyer personas detalhadas e perfis de clientes ideais (ICP) para marketing B2B e B2C. Gera perfis abrangentes com dados demográficos, psicográficos, pontos problemáticos, metas, objeções e estratégias de mensagens. Use ao definir o público-alvo, criar ICP ou desenvolver perfis de clientes. |

### <a id="icp"></a>Icp

| Recurso | Tipo | Origem | Descrição e Aplicação |
| :--- | :--- | :--- | :--- |
| <a id="persona-icp"></a>**`persona-icp`** | `Skill` | `0 Mkt` | Use para construir personas, perfil de cliente ideal (ICP), mapa de Jobs-to-be-Done, gatilhos de compra, roteiros de voz do cliente, pesquisa de público e pontuação de aderência ao ICP. Gatilhos: \"persona\", \"ICP\", \"cliente ideal\", \"JTBD\", \"segmentar público\". NÃO use para validar hipótese de produto com entrevistas (use persona-descoberta-de-clientes), analisar saturação de público em anúncios (use ads-analise-de-desempenho) nem montar cadência de prospecção (use vendas-cold-email). |

---

## <a id="pr-relações-públicas-pr"></a>pr (Relações Públicas (PR))

Total de recursos nesta macro-área: `2`

### <a id="assessoria-de-imprensa"></a>Assessoria De Imprensa

| Recurso | Tipo | Origem | Descrição e Aplicação |
| :--- | :--- | :--- | :--- |
| <a id="pr-assessoria-de-imprensa"></a>**`pr-assessoria-de-imprensa`** | `Skill` | `0 Mkt` | Use when planejar estratégias de imprensa, produzir pautas e press releases para veículos de comunicação, redigir pitches individualizados para jornalistas, estruturar Data PR com dados proprietários, conduzir newsjacking reativo de notícias quentes, preparar media training para entrevistas ou emitir notas oficiais e holding statements de gestão de crise, detectar sinais precoces de crise, coordenar a resposta e conduzir a recuperação de reputação. Triggers: \"assessoria de imprensa\", \"press release\", \"pitch para jornalista\", \"falar com repórter\", \"gancho de notícia\", \"disparar para a mídia\", \"divulgação na imprensa\", \"nota oficial\", \"comunicação de crise\", \"media kit\", \"clipping\", \"earned media\". NÃO use para posts de redes sociais (use social-estrategia) nem para backlinks e menções com foco em SEO (use seo-autoridade-e-backlinks). |

### <a id="relacoes-publicas"></a>Relacoes Publicas

| Recurso | Tipo | Origem | Descrição e Aplicação |
| :--- | :--- | :--- | :--- |
| <a id="pr-relacoes-publicas"></a>**`@pr-relacoes-publicas`** | `Agent` | `0 Mkt` | Especialista em Relações Públicas (PR), assessoria de imprensa e gestão de reputação institucional. Use quando precisar redigir press releases de alto interesse jornalístico, construir pitches para a imprensa, montar listas de mídia segmentadas, gerenciar crises de imagem ou articular pautas em veículos de comunicação de massa e nicho. <example> Context: A startup está lançando uma nova funcionalidade com IA e precisa divulgar para portais de negócios e tecnologia. user: "Preciso de um press release anunciando a nova funcionalidade da <marca> para enviar ao Startupi e NeoFeed." assistant: "Vou acionar o pr-relacoes-publicas para redigir o press release com gancho factual e ângulo noticioso, estruturado no padrão de redação jornalística e dados de mercado." <commentary> Demanda de assessoria de imprensa e redação jornalística institucional delegada ao especialista de PR. </commentary> </example> <example> Context: O usuário precisa de um pitch personalizado para apresentar o fundador como fonte para uma matéria de tendências. user: "Como abordo jornalistas do Valor Econômico para sugerir uma pauta sobre monitoramento de marca em tempo real?" assistant: "Acionando o pr-relacoes-publicas para elaborar um email-pitch conciso, com tese provocativa, estatísticas exclusivas e oferta de porta-voz." <commentary> Estratégia de pitching para veículos de alta relevância com foco em autoridade institucional. </commentary> </example> |

---

## <a id="produto-gestão-de-produto"></a>produto (Gestão de Produto)

Total de recursos nesta macro-área: `10`

### <a id="agile"></a>Agile

| Recurso | Tipo | Origem | Descrição e Aplicação |
| :--- | :--- | :--- | :--- |
| <a id="produto-agile"></a>**`produto-agile`** | `Skill` | `0 Mkt` | Use para gestão ágil de produto: Scrum, rituais, backlog e colaboração do time em desenvolvimento iterativo. Gatilhos: \"Scrum\", \"backlog\", \"sprint\", \"cerimônias ágeis\". NÃO use para planejar uma sprint específica (use o workflow produto-planejamento-de-sprint), escrever PRD (use produto-prd) nem histórias de usuário (use o workflow produto-historias-de-usuario). |
| <a id="produto-agile"></a>**`/produto-agile`** | `Workflow` | `0 Mkt` | Gerenciamento ágil de produtos, práticas Scrum e colaboração em equipe para |

### <a id="especificacao-de-funcionalidade"></a>Especificacao De Funcionalidade

| Recurso | Tipo | Origem | Descrição e Aplicação |
| :--- | :--- | :--- | :--- |
| <a id="produto-especificacao-de-funcionalidade"></a>**`/produto-especificacao-de-funcionalidade`** | `Workflow` | `0 Mkt` | Use quando solicitado a criar um novo recurso ou projeto |

### <a id="historias-de-usuario"></a>Historias De Usuario

| Recurso | Tipo | Origem | Descrição e Aplicação |
| :--- | :--- | :--- | :--- |
| <a id="produto-historias-de-usuario"></a>**`/produto-historias-de-usuario`** | `Workflow` | `0 Mkt` | Use quando um agente precisar escrever histórias de usuários para um projeto |

### <a id="levantamento-de-requisitos"></a>Levantamento De Requisitos

| Recurso | Tipo | Origem | Descrição e Aplicação |
| :--- | :--- | :--- | :--- |
| <a id="produto-levantamento-de-requisitos"></a>**`/produto-levantamento-de-requisitos`** | `Workflow` | `0 Mkt` | Levantamento de requisitos principais, redação de histórias de usuários, definição de critérios de aceitação e gerenciamento de escopo. Transforme insights em especificações claras e práticas. |

### <a id="planejamento-de-sprint"></a>Planejamento De Sprint

| Recurso | Tipo | Origem | Descrição e Aplicação |
| :--- | :--- | :--- | :--- |
| <a id="produto-planejamento-de-sprint"></a>**`/produto-planejamento-de-sprint`** | `Workflow` | `0 Mkt` | Planeje e execute sprints eficazes usando metodologias Agile. Defina metas de sprint, estime histórias de usuários, gerencie o backlog de sprint e facilite reuniões diárias para maximizar a produtividade da equipe e agregar valor de forma incremental. |

### <a id="prd"></a>Prd

| Recurso | Tipo | Origem | Descrição e Aplicação |
| :--- | :--- | :--- | :--- |
| <a id="produto-prd"></a>**`produto-prd`** | `Skill` | `0 Mkt` | Use para escrever PRD (documento de requisitos de produto), histórias de usuário, métricas de produto e a etapa v0.9 de go-to-market do PRD. Gatilhos: \"criar um PRD\", \"requisitos do produto\", \"documentar uma funcionalidade\", \"especificação de produto\". NÃO use para plano de lançamento (use revenue-lancamento, ou revenue-lancamento-tecnico se for produto técnico), estratégia de go-to-market e posicionamento (use revenue-gtm-e-posicionamento) nem pesquisa com clientes (use persona-descoberta-de-clientes). |
| <a id="produto-prd"></a>**`/produto-prd`** | `Workflow` | `0 Mkt` | Gere Documentos de Requisitos de Produto (PRDs) abrangentes para o produto |

### <a id="prd-estrategia-gtm"></a>Prd Estrategia Gtm

| Recurso | Tipo | Origem | Descrição e Aplicação |
| :--- | :--- | :--- | :--- |
| <a id="produto-prd-estrategia-gtm"></a>**`/produto-prd-estrategia-gtm`** | `Workflow` | `0 Mkt` | Defina a estratégia de entrada no mercado, incluindo plano de lançamento, mensagens, canais e cronograma durante o PRD v0.9 Go-to-Market. Aciona solicitações para planejar o lançamento, definir a estratégia do GTM ou quando o usuário pergunta "como fazemos o lançamento?", "go-to-market", "plano de lançamento", "estratégia de marketing", "mensagens", "canais de lançamento", "GTM". Produz entradas GTM com componentes do plano de lançamento. |

### <a id="roadmap-reverso"></a>Roadmap Reverso

| Recurso | Tipo | Origem | Descrição e Aplicação |
| :--- | :--- | :--- | :--- |
| <a id="produto-roadmap-reverso"></a>**`/produto-roadmap-reverso`** | `Workflow` | `0 Mkt` | Use ao planejar com prazo fixo ou resultado alvo, trabalhando retroativamente a partir da meta futura até o presente, definindo marcos e dependências, mapeando o caminho crítico, identificando o que deve acontecer e quando, planejando lançamentos de produtos com datas fixas, roteiros estratégicos plurianuais, planejamento de eventos, iniciativas de transformação ou quando o usuário menciona "backcast", "trabalhar retroativamente a partir de", "planejamento reverso", "precisamos lançar até", "a data prevista é" ou "o que precisa acontecer para alcançar". |

---

## <a id="revenue-estratégia-de-receita-revenue"></a>revenue (Estratégia de Receita (Revenue))

Total de recursos nesta macro-área: `25`

### <a id="analise-competitiva"></a>Analise Competitiva

| Recurso | Tipo | Origem | Descrição e Aplicação |
| :--- | :--- | :--- | :--- |
| <a id="revenue-analise-competitiva"></a>**`/revenue-analise-competitiva`** | `Workflow` | `0 Mkt` | Inteligência competitiva, análise de mercado e posicionamento estratégico para diferenciação de produtos. |

### <a id="campanhas"></a>Campanhas

| Recurso | Tipo | Origem | Descrição e Aplicação |
| :--- | :--- | :--- | :--- |
| <a id="revenue-campanhas"></a>**`revenue-campanhas`** | `Skill` | `0 Mkt` | Planejamento integrado de campanhas de marketing digital e roteamento para a skill especialista de cada frente (conteúdo, social, email, SEO, GEO, mídia paga, métricas, lançamento). Gera parâmetros UTM e valida a campanha antes do lançamento. Use para planejar uma campanha que atravessa vários canais, montar o calendário, definir o rastreamento UTM ou destravar uma campanha parada. NÃO use para executar o trabalho de um canal específico (use a skill especialista da tabela de rotas, por exemplo seo-conteudo, social-estrategia, email-copy, ads-analise-de-desempenho ou revenue-gtm-e-posicionamento). |
| <a id="revenue-campanhas"></a>**`/revenue-campanhas`** | `Workflow` | `0 Mkt` | Planejamento integrado de campanhas de marketing digital e roteamento para a skill especialista de cada frente (conteúdo, social, email, SEO, GEO, mídia paga, métricas, lançamento). Gera parâmetros UTM e valida a campanha antes do lançamento. Use para planejar uma campanha que atravessa vários canais, montar o calendário, definir o rastreamento UTM ou destravar uma campanha parada. NÃO use para executar o trabalho de um canal específico (use a skill especialista da tabela de rotas, por exemplo seo-conteudo, social-estrategia, email-copy, ads-analise-de-desempenho ou revenue-gtm-e-posicionamento). |

### <a id="checklist-de-lancamento-de-campanha"></a>Checklist De Lancamento De Campanha

| Recurso | Tipo | Origem | Descrição e Aplicação |
| :--- | :--- | :--- | :--- |
| <a id="revenue-checklist-de-lancamento-de-campanha"></a>**`/revenue-checklist-de-lancamento-de-campanha`** | `Workflow` | `0 Mkt` | Gera o checklist de pré-lançamento de uma campanha, com cronograma T-14 a T+1 e matriz de sign-off. Use antes de colocar uma campanha no ar para garantir que nada ficou de fora. |

### <a id="criacao-de-campanha"></a>Criacao De Campanha

| Recurso | Tipo | Origem | Descrição e Aplicação |
| :--- | :--- | :--- | :--- |
| <a id="revenue-criacao-de-campanha"></a>**`/revenue-criacao-de-campanha`** | `Workflow` | `0 Mkt` | Crie uma campanha de marketing abrangente, da estratégia à execução. |

### <a id="estrategia-pmm"></a>Estrategia Pmm

| Recurso | Tipo | Origem | Descrição e Aplicação |
| :--- | :--- | :--- | :--- |
| <a id="revenue-estrategia-pmm"></a>**`/revenue-estrategia-pmm`** | `Workflow` | `0 Mkt` | Marketing de produto, posicionamento, estratégia GTM e inteligência competitiva. Inclui definição de ICP, metodologia de posicionamento de April Dunford, manuais de lançamento, cartões de batalha competitivos e guias de entrada no mercado internacional. Use ao desenvolver posicionamento, planejar lançamentos de produtos, criar mensagens, analisar concorrentes, entrar em novos mercados, viabilizar vendas ou quando o usuário mencionar marketing de produto, posicionamento, GTM, go-to-market, análise competitiva, entrada no mercado ou capacitação de vendas. |

### <a id="gtm-e-posicionamento"></a>Gtm E Posicionamento

| Recurso | Tipo | Origem | Descrição e Aplicação |
| :--- | :--- | :--- | :--- |
| <a id="revenue-gtm-e-posicionamento"></a>**`revenue-gtm-e-posicionamento`** | `Skill` | `0 Mkt` | Use para estratégia de go-to-market e marketing de produto: posicionamento, Category Design, Value Proposition Canvas, STP (segmentação, alvo e posicionamento), pré-mortem e coordenação de lançamento entre áreas. Gatilhos: \"GTM\", \"posicionar produto\", \"proposta de valor\", \"STP\", \"categoria\". NÃO use para posicionamento e essência da marca (use brand-essence), plano de lançamento detalhado (use revenue-lancamento) nem análise de concorrentes (use revenue-inteligencia-competitiva). |

### <a id="inteligencia-competitiva"></a>Inteligencia Competitiva

| Recurso | Tipo | Origem | Descrição e Aplicação |
| :--- | :--- | :--- | :--- |
| <a id="revenue-inteligencia-competitiva"></a>**`revenue-inteligencia-competitiva`** | `Skill` | `0 Mkt` | Use para inteligência competitiva estratégica: mapa de mercado, teardown de concorrente, battlecard, análise de fosso (moat), pesquisa win/loss e mapa de diferenciação. Gatilhos: \"analisar concorrente\", \"battlecard\", \"win/loss\", \"teardown\", \"diferenciação\". NÃO use para posicionar o próprio produto (use revenue-gtm-e-posicionamento), monitorar preço de concorrente (use o workflow revenue-monitoramento-de-preco-concorrente) nem anúncios de concorrentes (use o workflow ads-extracao-de-anuncios-concorrentes). |

### <a id="lancamento"></a>Lancamento

| Recurso | Tipo | Origem | Descrição e Aplicação |
| :--- | :--- | :--- | :--- |
| <a id="revenue-lancamento"></a>**`revenue-lancamento`** | `Skill` | `0 Mkt` | Use para planejar o lançamento de qualquer produto, serviço, curso ou funcionalidade: escolher o tipo de lançamento, montar o plano de pré-lançamento, lançamento e pós-lançamento, definir canais próprios, alugados e emprestados (ORB), lançar em fases (interno, alfa, beta, acesso antecipado e geral), usar Product Hunt e lista de espera, ou montar o lançamento como evento (fórmula de Jeff Walker). Gatilhos: \"plano de lançamento\", \"lançar meu curso\", \"lançar produto\", \"abertura de carrinho\", \"lista de espera\", \"Product Hunt\", \"anunciar funcionalidade\". NÃO use para lançar API, SDK ou ferramenta para desenvolvedores, com níveis (tiers) e documentação (use revenue-lancamento-tecnico), para posicionamento, categoria e pré-mortem (use revenue-gtm-e-posicionamento), para campanha multicanal com UTM e calendário (use revenue-campanhas), para oferta, bônus e garantia (use revenue-oferta) nem para o texto de e-mails e páginas de venda (use email-copy e copy-landing-page). |

### <a id="lancamento-tecnico"></a>Lancamento Tecnico

| Recurso | Tipo | Origem | Descrição e Aplicação |
| :--- | :--- | :--- | :--- |
| <a id="revenue-lancamento-tecnico"></a>**`revenue-lancamento-tecnico`** | `Skill` | `0 Mkt` | Use para planejar o lançamento de API, SDK, ferramenta para desenvolvedores ou produto técnico: níveis de lançamento (tiers), preparação de desenvolvedores (documentação, exemplos, SDK), mensagens de lançamento e métricas. Gatilhos: \"lançar API\", \"lançamento GA/beta\", \"release técnico\", \"preparar desenvolvedores\". NÃO use para lançar curso, produto digital ou funcionalidade comum (use revenue-lancamento), para posicionamento e estratégia de go-to-market (use revenue-gtm-e-posicionamento), campanha multicanal (use revenue-campanhas) nem PRD (use produto-prd). |
| <a id="revenue-lancamento-tecnico"></a>**`/revenue-lancamento-tecnico`** | `Workflow` | `0 Mkt` | Planejar e executar lançamentos de produtos técnicos para ferramentas de desenvolvedor, APIs, |

### <a id="modelos-mentais"></a>Modelos Mentais

| Recurso | Tipo | Origem | Descrição e Aplicação |
| :--- | :--- | :--- | :--- |
| <a id="revenue-modelos-mentais"></a>**`revenue-modelos-mentais`** | `Skill` | `0 Mkt` | Use quando uma decisão é difícil, cara ou difícil de desfazer e pede raciocínio estruturado: pensamento de segunda ordem, decisões reversíveis ou irreversíveis, minimização do arrependimento, primeiros princípios, inversão, seis chapéus, matriz de Eisenhower, pre-mortem de projeto ou lançamento, técnicas de solução de problemas e conselho de negócio por 9 lentes. Gatilhos: \"devo fazer X\", \"vale a pena\", \"qual o risco\", \"estou travado\", \"priorizar\", \"pivotar\", \"decisão estratégica\". NÃO use para métricas e estratégia de crescimento (use growth-frameworks), psicologia de quem compra (use revenue-psicologia), pre-mortem de uma previsão ou forecast (use revenue-premortem-previsao). |

### <a id="monitoramento-de-preco-concorrente"></a>Monitoramento De Preco Concorrente

| Recurso | Tipo | Origem | Descrição e Aplicação |
| :--- | :--- | :--- | :--- |
| <a id="revenue-monitoramento-de-preco-concorrente"></a>**`/revenue-monitoramento-de-preco-concorrente`** | `Workflow` | `0 Mkt` | Monitore as páginas de preços dos concorrentes e envie alertas quando os preços mudarem. Acompanhe padrões de descontos, ciclos promocionais e mudanças na estratégia de preços. |

### <a id="oferta"></a>Oferta

| Recurso | Tipo | Origem | Descrição e Aplicação |
| :--- | :--- | :--- | :--- |
| <a id="revenue-oferta"></a>**`revenue-oferta`** | `Skill` | `0 Mkt` | Use para montar uma oferta irresistível pelo método de Alex Hormozi (\"$100M Offers\"): equação de valor, empilhamento de bônus, garantia (inversão de risco), escassez, nome pela fórmula M-A-G-I-C, e bibliotecas de headlines, CTAs e objeções. Gatilhos: \"oferta irresistível\", \"Grand Slam Offer\", \"empilhar bônus\", \"garantia\", \"quebrar objeção\". NÃO use para definir preço e pacotes de SaaS (use revenue-preco), copy completa de página (use copy-landing-page) nem roteiro de VSL (use copy-vsl). |

### <a id="orquestracao-de-crm"></a>Orquestracao De Crm

| Recurso | Tipo | Origem | Descrição e Aplicação |
| :--- | :--- | :--- | :--- |
| <a id="revenue-orquestracao-de-crm"></a>**`revenue-orquestracao-de-crm`** | `Skill` | `0 Mkt` | Orquestração de RevOps e CRM em nível de estratégia (não execução de ponta de vendas). Cobre estágios do contato, modelo de lead scoring (demográfico, comportamental e decaimento), temperatura do lead, segmentação, rotina de higiene de dados, pontos de integração entre marketing, CRM e vendas, roteamento de leads, automações de CRM e RevOps. Use para definir como os contatos evoluem, são pontuados e segmentados no CRM. NÃO use para desenhar e implementar as automações de email (use email-automacao), qualificação MEDDIC e BANT e previsão de vendas (use vendas-pipeline), prospecção e cadência de SDR/BDR (use vendas-prospeccao-de-leads), conformidade com LGPD e GDPR (use geral-conformidade-lgpd) nem relatórios de atribuição (use data-atribuicao-e-relatorios). |

### <a id="orquestracao-de-estrategia"></a>Orquestracao De Estrategia

| Recurso | Tipo | Origem | Descrição e Aplicação |
| :--- | :--- | :--- | :--- |
| <a id="revenue-orquestracao-de-estrategia"></a>**`@revenue-orquestracao-de-estrategia`** | `Agent` | `0 Mkt` | Orquestrador geral da estratégia de marketing que coordena todas as atividades de marketing. |

### <a id="pesquisa-de-mercado"></a>Pesquisa De Mercado

| Recurso | Tipo | Origem | Descrição e Aplicação |
| :--- | :--- | :--- | :--- |
| <a id="revenue-pesquisa-de-mercado"></a>**`@revenue-pesquisa-de-mercado`** | `Agent` | `0 Mkt` | Especialista em pesquisa de mercado e análise competitiva. Use para conduzir pesquisas de mercado, analisar concorrentes, coletar insights do público, explorar tendências do setor e encontrar práticas recomendadas de marketing. Exemplos: <exemplo>Contexto: O usuário precisa de inteligência competitiva. usuário: \"Pesquise as estratégias de marketing dos nossos 5 principais concorrentes\" assistente: \"Usarei o agente de pesquisa de receita para conduzir análises competitivas abrangentes, incluindo mensagens, canais e posicionamento.\" <commentary>Isso requer uma pesquisa de mercado aprofundada, então delegue ao agente de pesquisa de receita.</commentary></example> <example>Contexto: o usuário deseja entender seu público. usuário: \"Quais são os pontos problemáticos do nosso mercado-alvo?\" assistente: \"Deixe-me implantar o agente de pesquisa de receita para coletar insights do público e análise dos pontos problemáticos.\" <commentary>A pesquisa de público requer a síntese de múltiplas fontes e a criação de insights acionáveis.</commentary></example> |

### <a id="planejamento-de-campanha"></a>Planejamento De Campanha

| Recurso | Tipo | Origem | Descrição e Aplicação |
| :--- | :--- | :--- | :--- |
| <a id="revenue-planejamento-de-campanha"></a>**`@revenue-planejamento-de-campanha`** | `Agent` | `0 Mkt` | Especialista em planejamento e estratégia de campanhas. Use para criar planos de marketing abrangentes, cronogramas de campanha, alocação de orçamento, calendários de conteúdo e estratégias de mix de canais. Exemplos: <exemplo>Contexto: o usuário precisa de um plano de marketing. usuário: \"Crie um plano de marketing do primeiro trimestre para o lançamento de nosso produto\" assistente: \"Usarei o agente de planejamento de receita para desenvolver um plano de marketing abrangente com cronograma, orçamento e estratégia de canal.\" <commentary>O planejamento da campanha requer uma abordagem estruturada para metas, táticas e recursos.</commentary></example> <example>Contexto: o usuário deseja planejamento de conteúdo. usuário: \"Construa um calendário de conteúdo para os próximos 3 meses\" assistente: \"Deixe-me invocar o agente de planejamento de receita para criar um calendário de conteúdo alinhado com seus objetivos de marketing.\" <commentary>O planejamento de conteúdo requer alinhamento estratégico e coordenação de recursos.</commentary></example> |

### <a id="plano-de-lancamento"></a>Plano De Lancamento

| Recurso | Tipo | Origem | Descrição e Aplicação |
| :--- | :--- | :--- | :--- |
| <a id="revenue-plano-de-lancamento"></a>**`/revenue-plano-de-lancamento`** | `Workflow` | `0 Mkt` | Planeje o lançamento de produtos e a estratégia de entrada no mercado. Use ao lançar produtos, entrar em novos mercados ou planejar campanhas de marketing. Abrange posicionamento, canais, mensagens e execução de lançamento. |

### <a id="preco"></a>Preco

| Recurso | Tipo | Origem | Descrição e Aplicação |
| :--- | :--- | :--- | :--- |
| <a id="revenue-preco"></a>**`revenue-preco`** | `Skill` | `0 Mkt` | Use para definir preço e pacotes de SaaS e produto digital: preço por valor, pesquisa de preço (Van Westendorp, MaxDiff), planos Good-Better-Best, freemium vs teste grátis, validação de disposição a pagar, quando subir preço e preço enterprise. Gatilhos: \"quanto cobrar\", \"planos e preços\", \"página de preços\", \"freemium\", \"aumentar preço\". NÃO use para montar oferta, bônus e garantia (use revenue-oferta) nem para rodar teste A/B de preço (use growth-testes-ab). |
| <a id="revenue-preco"></a>**`/revenue-preco`** | `Workflow` | `0 Mkt` | Estratégia de precificação de produtos digitais e SaaS, precificação baseada em valor, Van Westendorp |

### <a id="premortem-previsao"></a>Premortem Previsao

| Recurso | Tipo | Origem | Descrição e Aplicação |
| :--- | :--- | :--- | :--- |
| <a id="revenue-premortem-previsao"></a>**`revenue-premortem-previsao`** | `Skill` | `0 Mkt` | Use para testar a resistência das previsões, assumindo que elas falharam e trabalhando retroativamente para identificar o motivo. Invoque quando a confiança for alta (>80% ou <20%), necessidade de identificar riscos de cauda e incógnitas desconhecidas ou desejar ampliar intervalos de excesso de confiança. Use quando o usuário mencionar pré-morte, backcasting, o que pode dar errado, teste de estresse ou cisnes negros. |
| <a id="revenue-premortem-previsao"></a>**`/revenue-premortem-previsao`** | `Workflow` | `0 Mkt` | Use para testar a resistência das previsões, assumindo que elas falharam e trabalhando de trás para frente |

### <a id="psicologia"></a>Psicologia

| Recurso | Tipo | Origem | Descrição e Aplicação |
| :--- | :--- | :--- | :--- |
| <a id="revenue-psicologia"></a>**`revenue-psicologia`** | `Skill` | `0 Mkt` | Use para aplicar psicologia do consumidor e economia comportamental a uma peça, oferta ou página: princípios de persuasão de Cialdini, vieses cognitivos (Kahneman e Thaler), modelo de comportamento de BJ Fogg, psicologia de preço, arquitetura de escolha e construção de confiança. Gatilhos: \"psicologia\", \"viés cognitivo\", \"gatilho mental\", \"prova social\", \"escassez\", \"ancoragem\", \"por que as pessoas compram\". NÃO use para auditar uma peça pelos 14 motores emocionais do Sexy Canvas (use revenue-sexy-canvas), para modelos mentais gerais de decisão de negócio (use revenue-modelos-mentais), para escrever a copy pronta (use copy-conversao) nem para auditar a conversão de uma página (use site-cro). |

### <a id="sexy-canvas"></a>Sexy Canvas

| Recurso | Tipo | Origem | Descrição e Aplicação |
| :--- | :--- | :--- | :--- |
| <a id="revenue-sexy-canvas"></a>**`revenue-sexy-canvas`** | `Skill` | `0 Mkt` | Framework mestre de psicologia de consumo e desejos humanos baseado na metodologia Sexy Canvas de André Diamand (7 pecados capitais + 7 elementos da criança interior). Aplica auditoria, adaptação e eletrificação de apelo emocional para produtos, textos de copywriting, criativos visuais e roteiros. Use para: diagnosticar por que uma oferta não engaja ou não converte, amplificar o desejo de compra, enriquecer produtos com dopamina e auditar peças sob a lente dos 14 motores emocionais. NÃO use para escrever a peça final (o Canvas só dá parecer e handoff; use copy-conversao, brand-voice-messaging ou a skill que executa), para psicologia geral de persuasão e vieses (use revenue-psicologia) nem para decisões de negócio (use revenue-modelos-mentais). Dentro do brand-builder, o procedimento da etapa 5 está em brand-builder/desejo.md. |

---

## <a id="seo-seo--mecanismos-de-busca"></a>seo (SEO & Mecanismos de Busca)

Total de recursos nesta macro-área: `19`

### <a id="agrupamento-de-palavras-chave"></a>Agrupamento De Palavras Chave

| Recurso | Tipo | Origem | Descrição e Aplicação |
| :--- | :--- | :--- | :--- |
| <a id="seo-agrupamento-de-palavras-chave"></a>**`/seo-agrupamento-de-palavras-chave`** | `Workflow` | `0 Mkt` | Técnicas para expandir palavras-chave iniciais e agrupamento por tópico e intenção. Use ao criar listas de palavras-chave, planejar calendários de conteúdo ou identificar grupos de tópicos para estratégia de conteúdo de pilares. |

### <a id="analise-de-serp"></a>Analise De Serp

| Recurso | Tipo | Origem | Descrição e Aplicação |
| :--- | :--- | :--- | :--- |
| <a id="seo-analise-de-serp"></a>**`/seo-analise-de-serp`** | `Workflow` | `0 Mkt` | Técnicas de análise SERP para classificação de intenções, identificação de recursos e inteligência competitiva. Use ao analisar resultados de pesquisa para estratégia de conteúdo. |

### <a id="api-de-busca"></a>Api De Busca

| Recurso | Tipo | Origem | Descrição e Aplicação |
| :--- | :--- | :--- | :--- |
| <a id="seo-api-de-busca"></a>**`/seo-api-de-busca`** | `Workflow` | `0 Mkt` | API de resultados do mecanismo de pesquisa SerpApi via curl. Use essa habilidade para raspar Google, Bing, YouTube e outros mecanismos de pesquisa. |

### <a id="app-store"></a>App Store

| Recurso | Tipo | Origem | Descrição e Aplicação |
| :--- | :--- | :--- | :--- |
| <a id="seo-app-store"></a>**`seo-app-store`** | `Skill` | `0 Mkt` | Especialista em App Store Optimization (ASO) para Apple App Store e Google Play Store. Abrange pesquisa de palavras-chave mobile, otimização de metadados visuais e textuais, Custom Product Pages (CPP), testes A/B de ícones e screenshots, conversão de downloads e gestão de avaliações. Use para: ranquear aplicativos nas buscas mobile, otimizar fichas de lojas, estruturar lançamentos de apps e maximizar taxas de instalação orgânica. |

### <a id="autoridade-e-backlinks"></a>Autoridade E Backlinks

| Recurso | Tipo | Origem | Descrição e Aplicação |
| :--- | :--- | :--- | :--- |
| <a id="seo-autoridade-e-backlinks"></a>**`seo-autoridade-e-backlinks`** | `Skill` | `0 Mkt` | Use para analisar e conquistar autoridade de domínio e backlinks: avaliar o perfil de links, identificar links tóxicos, medir a autoridade do domínio (rubrica CITE), montar estratégia de link building e escrever e-mails de outreach e digital PR. Gatilhos: \"backlinks\", \"perfil de links\", \"link building\", \"autoridade de domínio\", \"links tóxicos\", \"outreach para links\". NÃO use para links internos e arquitetura do site (use seo-on-page), para auditoria técnica de rastreio (use seo-tecnico), para assessoria de imprensa e press release (use pr-assessoria-de-imprensa) nem para prospecção comercial por e-mail (use vendas-cold-email). |

### <a id="checklist-semanal"></a>Checklist Semanal

| Recurso | Tipo | Origem | Descrição e Aplicação |
| :--- | :--- | :--- | :--- |
| <a id="seo-checklist-semanal"></a>**`/seo-checklist-semanal`** | `Workflow` | `0 Mkt` | Gera o checklist semanal de manutenção e otimização de SEO. Use para organizar as tarefas de SEO da semana por dia (rankings, saúde técnica, conteúdo, link building, concorrência). |

### <a id="conteudo"></a>Conteudo

| Recurso | Tipo | Origem | Descrição e Aplicação |
| :--- | :--- | :--- | :--- |
| <a id="seo-conteudo"></a>**`seo-conteudo`** | `Skill` | `0 Mkt` | Use ao escrever postagens de blog otimizadas para pesquisa, páginas principais, guias de comparação ou instruções; criação de resumos de SEO; usando as diretrizes EAT do Google. NÃO use para pesquisa de palavras-chave e clusters de tópicos (use seo-palavras-chave) ou SEO programático em escala (use seo-programatico). |

### <a id="geo"></a>Geo

| Recurso | Tipo | Origem | Descrição e Aplicação |
| :--- | :--- | :--- | :--- |
| <a id="seo-geo"></a>**`seo-geo`** | `Skill` | `0 Mkt` | Use ao otimizar conteúdo para Generative Engine Optimization (GEO), citações de IA, Perplexity, Google AI Overviews, SearchGPT, Claude ou Gemini; tornar o conteúdo da marca citável por LLMs; ou estabelecer autoridade de entidade em Knowledge Graphs. NÃO use para criar novo conteúdo do zero com pesquisas e citações de especialistas (use conteudo-pesquisa), para artigos de SEO baseados em palavras-chave (use seo-conteudo) ou para marcação de dados estruturados (use seo-schema-markup). |

### <a id="on-page"></a>On Page

| Recurso | Tipo | Origem | Descrição e Aplicação |
| :--- | :--- | :--- | :--- |
| <a id="seo-on-page"></a>**`seo-on-page`** | `Skill` | `0 Mkt` | Use ao auditar fatores de SEO na página, tags de título, meta descrições, títulos, arquiteturas de links internos, qualidade do conteúdo, sinais EAT, atualização e deterioração do conteúdo ou para diagnosticar por que uma página caiu nas classificações de pesquisa. NÃO use para backlinks, link building ou autoridade de domínio (use seo-autoridade-e-backlinks). |

### <a id="otimizacao-de-busca"></a>Otimizacao De Busca

| Recurso | Tipo | Origem | Descrição e Aplicação |
| :--- | :--- | :--- | :--- |
| <a id="seo-otimizacao-de-busca"></a>**`@seo-otimizacao-de-busca`** | `Agent` | `0 Mkt` | Especialista em otimização de mecanismos de pesquisa. Use para otimizar conteúdo para mecanismos de pesquisa, mantendo a qualidade e a legibilidade. Revisa o conteúdo para otimização de palavras-chave, SEO na página, SEO técnico e potencial de recursos SERP. Exemplos: <exemplo>Contexto: postagem de blog criada pelo usuário. usuário: \"Otimizar esta postagem do blog para SEO\" assistente: \"Usarei o agente seo-otimizacao-de-busca para revisar o uso de palavras-chave, meta tags, estrutura e elementos técnicos.\" <commentary>A otimização de SEO requer conhecimento especializado de algoritmos de pesquisa e práticas recomendadas.</commentary></example> <example>Contexto: O usuário precisa de auditoria de SEO. usuário: \"Por que esta página não é classificada?\" assistente: \"Deixe-me implantar o agente seo-otimizacao-de-busca para analisar problemas de SEO e fornecer recomendações de otimização.\" <commentary>Os diagnósticos de SEO exigem uma análise sistemática de vários fatores de classificação.</commentary></example> |

### <a id="otimizacao-de-conteudo"></a>Otimizacao De Conteudo

| Recurso | Tipo | Origem | Descrição e Aplicação |
| :--- | :--- | :--- | :--- |
| <a id="seo-otimizacao-de-conteudo"></a>**`/seo-otimizacao-de-conteudo`** | `Workflow` | `0 Mkt` | Otimize o conteúdo para mecanismos de pesquisa com análise de palavras-chave, pontuação de legibilidade, meta descrições e comparação de concorrentes. Use isso quando os usuários quiserem melhorar o SEO, otimizar postagens de blog ou analisar conteúdo para desempenho de pesquisa. |

### <a id="palavras-chave"></a>Palavras Chave

| Recurso | Tipo | Origem | Descrição e Aplicação |
| :--- | :--- | :--- | :--- |
| <a id="seo-palavras-chave"></a>**`seo-palavras-chave`** | `Skill` | `0 Mkt` | Use para pesquisar palavras-chave e intenção de busca: levantar termos, agrupar por tema e intenção, montar clusters de tópicos, analisar a página de resultados (SERP) de uma palavra e achar lacunas de conteúdo, com ou sem a extensão Keywords Everywhere. Gatilhos: \"pesquisa de palavras-chave\", \"keyword research\", \"intenção de busca\", \"cluster de tópicos\", \"o que o Google mostra para esta busca\", \"volume e dificuldade\". NÃO use para escrever o artigo (use seo-conteudo), para SEO programático (use seo-programatico), para auditar uma página (use seo-on-page) nem para tendências de conteúdo em redes sociais (use conteudo-tendencias). |

### <a id="podcast"></a>Podcast

| Recurso | Tipo | Origem | Descrição e Aplicação |
| :--- | :--- | :--- | :--- |
| <a id="seo-podcast"></a>**`seo-podcast`** | `Skill` | `0 Mkt` | Otimize o conteúdo do podcast para mecanismos de pesquisa usando transcrições, notas estruturadas do programa e segmentação estratégica por palavras-chave para impulsionar a descoberta orgânica. Use quando: Lançar um novo podcast e planejar a descoberta; Adicionar transcrições a episódios existentes para benefício de SEO; Otimizando notas de show para tráfego de pesquisa; Construir autoridade no tópico por meio de conteúdo de podcast; Aumentando o tráfego orgânico para páginas de destino de podcast |

### <a id="programatico"></a>Programatico

| Recurso | Tipo | Origem | Descrição e Aplicação |
| :--- | :--- | :--- | :--- |
| <a id="seo-programatico"></a>**`seo-programatico`** | `Skill` | `0 Mkt` | Use para criar páginas de SEO em escala a partir de modelos e dados (SEO programático): páginas de comparação, de localidade, de integração, de glossário, diretórios e templates com padrões de título, links internos e schema, sem cair em conteúdo raso. Gatilhos: \"SEO programático\", \"páginas em escala\", \"template de página\", \"centenas de páginas\", \"páginas de cidade ou de categoria\". NÃO use para escrever um artigo único otimizado (use seo-conteudo), para auditar uma página (use seo-on-page) nem para diagnóstico técnico de indexação (use seo-tecnico). |

### <a id="relatorio-de-desempenho"></a>Relatorio De Desempenho

| Recurso | Tipo | Origem | Descrição e Aplicação |
| :--- | :--- | :--- | :--- |
| <a id="seo-relatorio-de-desempenho"></a>**`seo-relatorio-de-desempenho`** | `Skill` | `0 Mkt` | Use para acompanhar e reportar o desempenho de SEO e GEO: relatório executivo, detecção de anomalias, alertas de volatilidade de ranking e KPIs no Google, Bing e buscadores de IA (Perplexity, SearchGPT, Claude, Gemini). Gatilhos: \"relatório de SEO\", \"queda de ranking\", \"tráfego orgânico caiu\", \"KPI de SEO\". NÃO use para dados brutos do Search Console (use o workflow seo-search-console), otimizar para ser citado por IA (use seo-geo) nem relatório de marketing geral (use data-atribuicao-e-relatorios). |

### <a id="schema-markup"></a>Schema Markup

| Recurso | Tipo | Origem | Descrição e Aplicação |
| :--- | :--- | :--- | :--- |
| <a id="seo-schema-markup"></a>**`seo-schema-markup`** | `Skill` | `0 Mkt` | Use quando o usuário solicitar "adicionar marcação de esquema", "gerar dados estruturados", "JSON-LD", "rich snippets", "esquema de perguntas frequentes", "adicionar resultados aprimorados de perguntas frequentes", "Quero avaliações com estrelas no Google", "marcação de produto" ou "esquema de receita". Gera marcação de dados estruturados (Schema.org JSON-LD) para permitir resultados avançados em mecanismos de pesquisa, incluindo trechos de perguntas frequentes, cartões de instruções, listas de produtos, avaliações e muito mais. Para otimização de metatags, consulte otimizador de metatags. Para SEO técnico mais amplo, consulte seo-técnico. |

### <a id="search-console"></a>Search Console

| Recurso | Tipo | Origem | Descrição e Aplicação |
| :--- | :--- | :--- | :--- |
| <a id="seo-search-console"></a>**`/seo-search-console`** | `Workflow` | `0 Mkt` | Assistente de indexação do Google Search Console. Use quando o usuário deseja rastrear o status de indexação da página, comparar o mapa do site com as páginas indexadas do GSC, gerenciar o rastreamento de envios ou mover falsos positivos (páginas indexadas por inspeção de URL, mas ainda não exportadas pelo GSC) para a lista indexada. Mantém dois arquivos de rastreamento (indexed.md, to-index.md) com suporte para priorização. |

### <a id="tecnico"></a>Tecnico

| Recurso | Tipo | Origem | Descrição e Aplicação |
| :--- | :--- | :--- | :--- |
| <a id="seo-tecnico"></a>**`seo-tecnico`** | `Skill` | `0 Mkt` | Use ao realizar auditorias técnicas de SEO, diagnosticar problemas de rastreamento ou indexação, auditar Core Web Vitals (LCP, INP, CLS), configurar robots.txt (incluindo rastreadores de IA como GPTBot), validar mapas de sites XML, corrigir códigos de status HTTP ou diagnosticar quedas de velocidade do site. NÃO use para backlinks ou link building (use seo-autoridade-e-backlinks). |

### <a id="wordpress"></a>Wordpress

| Recurso | Tipo | Origem | Descrição e Aplicação |
| :--- | :--- | :--- | :--- |
| <a id="seo-wordpress"></a>**`/seo-wordpress`** | `Workflow` | `0 Mkt` | Atualização em lote de metadados do Yoast SEO (títulos, descrições, frases-chave de foco) no WordPress via GraphQL. Use quando o usuário deseja atualizar metadados de SEO, otimizar títulos, corrigir meta descrições ou gerenciar campos Yoast SEO em várias postagens. Suporta modo de visualização, rastreamento de progresso e capacidade de retomada. |

---

## <a id="site-sites--páginas-de-conversão"></a>site (Sites & Páginas de Conversão)

Total de recursos nesta macro-área: `14`

### <a id="arquitetura"></a>Arquitetura

| Recurso | Tipo | Origem | Descrição e Aplicação |
| :--- | :--- | :--- | :--- |
| <a id="site-arquitetura"></a>**`site-arquitetura`** | `Skill` | `0 Mkt` | Use para planejar ou reestruturar a estrutura de um site: hierarquia de páginas, mapa do site (sitemap visual), padrão de URLs, menu, rodapé, breadcrumbs, navegação no celular e plano de links internos. Traz modelos prontos por tipo de site (SaaS, blog, e-commerce, documentação, híbrido, negócio local). Gatilhos: \"estrutura do site\", \"mapa do site\", \"arquitetura de informação\", \"menu do site\", \"URLs\", \"breadcrumb\", \"links internos\", \"planejar o site\". NÃO use para sitemap XML e rastreamento (use seo-tecnico), para páginas em escala por template (use seo-programatico), para dados estruturados (use seo-schema-markup), para o design visual das páginas (use site-interface-de-conversao) nem para o texto da página (use copy-landing-page). |

### <a id="auditoria-de-interface"></a>Auditoria De Interface

| Recurso | Tipo | Origem | Descrição e Aplicação |
| :--- | :--- | :--- | :--- |
| <a id="site-auditoria-de-interface"></a>**`site-auditoria-de-interface`** | `Skill` | `0 Mkt` | Use ANTES de alterar uma página, seção ou componente que já existe (site, landing page, interface): lê o estado atual, inventaria o que há, checa redundância e só propõe lacunas reais, com prova. Gatilhos: \"melhorar a página\", \"mexer no layout\", \"adicionar uma seção\", \"redesenhar a home\", \"adicionar componente\", quando já existe código ou página publicada. NÃO use para criar uma página do zero (use o workflow site-construcao-de-landing-page), para auditar conversão (use site-cro), para desenhar a interface (use site-interface-de-conversao) nem para revisar conformidade de código de UI (use site-diretrizes-web-codigo). |
| <a id="site-auditoria-de-interface"></a>**`/site-auditoria-de-interface`** | `Workflow` | `0 Mkt` | Antes de alterar uma página, seção ou componente que já existe: lê o estado atual, inventaria o que há, checa redundância e só propõe lacunas reais, com prova. Não serve para criar página do zero nem para auditar conversão. |

### <a id="construcao-de-landing-page"></a>Construcao De Landing Page

| Recurso | Tipo | Origem | Descrição e Aplicação |
| :--- | :--- | :--- | :--- |
| <a id="site-construcao-de-landing-page"></a>**`/site-construcao-de-landing-page`** | `Workflow` | `0 Mkt` | Constrói uma landing page de conversão de ponta a ponta para uma marca de _brands/: brief, estrutura, copy (com filtro anti-slop), design a partir dos tokens da marca, código (só com autorização explícita), teste no navegador e revisão de conversão. Gatilhos: \"crie a landing page\", \"monte a página de captura\", \"construa a LP\", \"página de vendas pronta\". Para só o texto use /landing-page; para site com várias páginas use /build-site. |

### <a id="construcao-de-site"></a>Construcao De Site

| Recurso | Tipo | Origem | Descrição e Aplicação |
| :--- | :--- | :--- | :--- |
| <a id="site-construcao-de-site"></a>**`/site-construcao-de-site`** | `Workflow` | `0 Mkt` | Constrói um site de várias páginas para uma marca de _brands/: arquitetura (mapa, URLs, menu), design system a partir dos tokens da marca, páginas na ordem de importância (cada uma pelo /build-landing-page), SEO técnico básico e teste no navegador. Gatilhos: \"crie o site\", \"monte o site institucional\", \"site de várias páginas\", \"reestruture o site\". Para uma única página use /build-landing-page. |

### <a id="construcao-web"></a>Construcao Web

| Recurso | Tipo | Origem | Descrição e Aplicação |
| :--- | :--- | :--- | :--- |
| <a id="site-construcao-web"></a>**`@site-construcao-web`** | `Agent` | `0 Mkt` | Construtor de sites e landing pages de conversão para as marcas de _brands/. Use quando o pedido for criar, montar ou reestruturar uma landing page, página de captura ou site de várias páginas: conduz marca, brief, arquitetura, copy, design a partir dos tokens, código (só com autorização explícita), teste no navegador e revisão de conversão, chamando copy-redacao-publicitaria, site-otimizacao-de-conversao e seo-otimizacao-de-busca. Não escreve só o texto (use copy-redacao-publicitaria), não audita página pronta (use site-otimizacao-de-conversao) e não publica sem pedido. Exemplos: <example>Context: usuário quer uma página de captura. user: \"Monte a landing page do e-book da plus-pr\" assistant: \"Vou acionar o site-construcao-web, que segue o workflow site-construcao-de-landing-page com portões de aprovação.\" <commentary>Construção de página de ponta a ponta.</commentary></example> <example>Context: usuário quer o site institucional. user: \"Preciso do site da experimentacao com home, serviços e contato\" assistant: \"Acionando o site-construcao-web com o workflow site-construcao-de-site: primeiro a arquitetura, depois as páginas.\" <commentary>Site de várias páginas.</commentary></example> |

### <a id="cro"></a>Cro

| Recurso | Tipo | Origem | Descrição e Aplicação |
| :--- | :--- | :--- | :--- |
| <a id="site-cro"></a>**`site-cro`** | `Skill` | `0 Mkt` | Use para auditar e otimizar a conversão de uma página que já existe (landing page, home, preços, formulário, popup, cadastro): modelo LIFT, auditoria com nota, casamento anúncio × página, checklist de 15 pontos e ideias de teste. Gatilhos: \"a página não converte\", \"auditoria de CRO\", \"revisar a landing\", \"otimizar formulário\", \"popup de saída\", \"atrito no cadastro\". NÃO use para escrever o texto da página (use copy-landing-page), desenhar a interface (use site-interface-de-conversao), planejar o teste A/B e a estatística (use growth-testes-ab), gatilhos mentais (use revenue-psicologia) nem alterar uma página sem duplicar o que existe (use site-auditoria-de-interface). |

### <a id="diretrizes-web-codigo"></a>Diretrizes Web Codigo

| Recurso | Tipo | Origem | Descrição e Aplicação |
| :--- | :--- | :--- | :--- |
| <a id="site-diretrizes-web-codigo"></a>**`site-diretrizes-web-codigo`** | `Skill` | `0 Mkt` | Use para revisar CÓDIGO de interface contra as Web Interface Guidelines da Vercel (acessibilidade, UX, boas práticas), com saída terse em arquivo:linha. Busca a lista atual online a cada uso: precisa de acesso à internet. Gatilhos: \"revise minha UI\", \"cheque acessibilidade do código\", \"audite o design do site\". NÃO use para auditar a conversão de uma página (use site-cro), desenhar a interface (use site-interface-de-conversao) nem alterar página existente sem duplicar o que há (use site-auditoria-de-interface). |

### <a id="injecao-de-cta-astro"></a>Injecao De Cta Astro

| Recurso | Tipo | Origem | Descrição e Aplicação |
| :--- | :--- | :--- | :--- |
| <a id="site-injecao-de-cta-astro"></a>**`/site-injecao-de-cta-astro`** | `Workflow` | `0 Mkt` | Insere blocos de CTA (newsletter, produto, isca digital) em posts de um site Astro, com posição inteligente, pontuação de relevância feita pelo próprio agente, pré-visualização obrigatória e reversão por git. Sem programas: o agente lê e edita os arquivos de conteúdo do site. Gatilhos: \"adicione CTA nos posts\", \"inserir inscrição na newsletter nos artigos\", \"promova o produto nos posts do blog Astro\". NÃO use para criar o CTA em si (use copy-landing-page e cta-writing de copy-conversao), para escolher onde ele vai na página (use site-cro) nem para sites que não são Astro. |

### <a id="interface-de-conversao"></a>Interface De Conversao

| Recurso | Tipo | Origem | Descrição e Aplicação |
| :--- | :--- | :--- | :--- |
| <a id="site-interface-de-conversao"></a>**`site-interface-de-conversao`** | `Skill` | `0 Mkt` | Use para desenhar a interface de uma página ou site de conversão: hierarquia visual, cor e contraste (60-30-10, WCAG AA), tipografia, espaçamento, componentes, movimento, versão para celular e checklist de acessibilidade. Gatilhos: \"design da landing page\", \"hierarquia visual\", \"paleta e contraste\", \"layout\", \"UI\", \"UX\", \"acessibilidade\". NÃO use para planejar a estrutura do site, URLs e navegação (use site-arquitetura), para auditoria de conversão de uma página pronta (use site-cro), para o texto da página (use copy-landing-page), para identidade visual da marca (use brand-visual-direction e brand-design-system), para código de componentes (use site-tailwind-design-system e site-react-desempenho) nem para alterar uma página existente sem duplicar o que já há (use site-auditoria-de-interface). |

### <a id="otimizacao-de-conversao"></a>Otimizacao De Conversao

| Recurso | Tipo | Origem | Descrição e Aplicação |
| :--- | :--- | :--- | :--- |
| <a id="site-otimizacao-de-conversao"></a>**`@site-otimizacao-de-conversao`** | `Agent` | `0 Mkt` | Especialista em otimização de taxa de conversão. Use para maximizar as taxas de conversão em ativos de marketing, aplicando princípios e psicologia comprovados de CRO. Revisa páginas de destino, texto do e-mail, texto do anúncio e CTAs para eficácia de conversão. Exemplos: <exemplo>Contexto: página inicial criada pelo usuário. usuário: \"Analise esta página de destino para otimização de conversão\" assistente: \"Usarei o agente site-otimizacao-de-conversao para analisar proposta de valor, CTAs e elementos de persuasão.\" <commentary>CRO requer análise especializada de psicologia de conversão e melhores práticas.</commentary></example> <example>Contexto: o usuário precisa de e-mail otimizado. usuário: \"Como posso melhorar as conversões neste e-mail?\" assistente: \"Deixe-me implantar o agente site-otimizacao-de-conversao para revisar o texto, o posicionamento do CTA e os pontos de atrito.\" <commentary>A otimização de conversão de e-mail requer conhecimento especializado em persuasão e psicologia do usuário.</commentary></example> |

### <a id="react-composicao"></a>React Composicao

| Recurso | Tipo | Origem | Descrição e Aplicação |
| :--- | :--- | :--- | :--- |
| <a id="site-react-composicao"></a>**`site-react-composicao`** | `Skill` | `0 Mkt` | Use ao refatorar componentes React com excesso de props booleanas, ao montar bibliotecas de componentes flexíveis ou projetar APIs reutilizáveis (componentes compostos, render props, context providers, mudanças do React 19). NÃO use para desempenho React/Next.js (use site-react-desempenho), tokens e variantes Tailwind (use site-tailwind-design-system), nem para copy ou design de página. Escrever código de aplicação exige autorização explícita (regra 1.5). |

### <a id="react-desempenho"></a>React Desempenho

| Recurso | Tipo | Origem | Descrição e Aplicação |
| :--- | :--- | :--- | :--- |
| <a id="site-react-desempenho"></a>**`site-react-desempenho`** | `Skill` | `0 Mkt` | Use ao escrever, revisar ou refatorar CÓDIGO React e Next.js para desempenho (cascatas de requisições, tamanho do bundle, servidor, re-renderizações, hidratação), com 66 regras da Vercel por prioridade. NÃO use para copy ou design de página (use copy-landing-page e site-interface-de-conversao), para componentes e tokens Tailwind (use site-tailwind-design-system) nem para padrões de composição de componentes (use site-react-composicao). Escrever código de aplicação exige autorização explícita (regra 1.5). |

### <a id="tailwind-design-system"></a>Tailwind Design System

| Recurso | Tipo | Origem | Descrição e Aplicação |
| :--- | :--- | :--- | :--- |
| <a id="site-tailwind-design-system"></a>**`site-tailwind-design-system`** | `Skill` | `0 Mkt` | Use para escrever o CÓDIGO de um design system ou de componentes com Tailwind CSS v4 e React 19: tokens com @theme, variantes com CVA, formulários, grid, animações nativas, modo escuro, migração v3 para v4; inclui trechos de HTML Tailwind para páginas de marketing (references/tailwind-patterns.md). NÃO use para decidir cores, fontes e identidade da marca (use brand-visual-direction e brand-design-system), para princípios visuais de página (use site-interface-de-conversao), para revisar conformidade de UI (use site-diretrizes-web-codigo) nem para desempenho React/Next.js (use site-react-desempenho). |

---

## <a id="social-mídias-sociais"></a>social (Mídias Sociais)

Total de recursos nesta macro-área: `17`

### <a id="analise-de-desempenho"></a>Analise De Desempenho

| Recurso | Tipo | Origem | Descrição e Aplicação |
| :--- | :--- | :--- | :--- |
| <a id="social-analise-de-desempenho"></a>**`/social-analise-de-desempenho`** | `Workflow` | `0 Mkt` | Analisa o desempenho da campanha de mídia social em todas as plataformas com métricas de engajamento, cálculos de ROI e insights de público para decisões de marketing baseadas em dados |

### <a id="calendario-e-distribuicao"></a>Calendario E Distribuicao

| Recurso | Tipo | Origem | Descrição e Aplicação |
| :--- | :--- | :--- | :--- |
| <a id="social-calendario-e-distribuicao"></a>**`@social-calendario-e-distribuicao`** | `Agent` | `0 Mkt` | Estrategista sênior de redes sociais, distribuição orgânica e comunidades. Use quando precisar planejar calendários editoriais, criar carrosséis de alta retenção no Instagram e LinkedIn, estruturar estratégias de crescimento em canais sociais e engajar audiências com conteúdo nativo.\\n\\n<example>\\nContext: O usuário precisa de uma sequência de carrosséis para o LinkedIn para gerar autoridade B2B.\\nuser: \"Preciso de um carrossel educativo para o LinkedIn da <marca> sobre monitoramento de marca.\"\\nassistant: \"Vou acionar o social-calendario-e-distribuicao para estruturar o carrossel lâmina a lâmina, definindo hook de capa, payoff e save-bait com foco em retenção.\"\\n<commentary>\\nDemanda de estratégia de redes sociais e carrossel de autoridade.\\n</commentary>\\n</example>\\n\\n<example>\\nContext: O usuário quer um calendário editorial mensal omnichannel.\\nuser: \"Pode planejar a grade de conteúdo do Instagram e LinkedIn da <marca> para o próximo mês?\"\\nassistant: \"Acionando o social-calendario-e-distribuicao para desenhar o calendário editorial omnichannel alinhado aos pilares de conteúdo da marca.\"\\n<commentary>\\nPlanejamento de distribuição e linhas editoriais em mídias sociais.\\n</commentary>\\n</example> |

### <a id="carrossel"></a>Carrossel

| Recurso | Tipo | Origem | Descrição e Aplicação |
| :--- | :--- | :--- | :--- |
| <a id="social-carrossel"></a>**`social-carrossel`** | `Skill` | `0 Mkt` | Use para planejar e redigir carrosséis de Instagram e LinkedIn lâmina a lâmina, com teto de cerca de 25 palavras por lâmina, gancho forte no slide 1, valor no slide 2 e uma ideia com metáfora visual por lâmina, prontos para renderizar em modelos de imagem de IA. Gatilhos: \"carrossel\", \"lâminas\", \"slides do Instagram\". NÃO use para a direção de arte e prompts de imagem do carrossel (use social-direcao-de-arte-ia), para estratégia social (use social-estrategia) nem para post de LinkedIn em texto (use social-linkedin). |

### <a id="checklist-diario"></a>Checklist Diario

| Recurso | Tipo | Origem | Descrição e Aplicação |
| :--- | :--- | :--- | :--- |
| <a id="social-checklist-diario"></a>**`/social-checklist-diario`** | `Workflow` | `0 Mkt` | Gera o checklist diário de gestão de redes sociais (comunidade, publicação, engajamento e métricas). Use para organizar a rotina diária de social media por bloco de tempo. |

### <a id="conceito-de-thumbnail"></a>Conceito De Thumbnail

| Recurso | Tipo | Origem | Descrição e Aplicação |
| :--- | :--- | :--- | :--- |
| <a id="social-conceito-de-thumbnail"></a>**`/social-conceito-de-thumbnail`** | `Workflow` | `0 Mkt` | Gere conceitos e ideias de miniaturas para YouTube, TikTok e outras plataformas de vídeo. Cria resumos visuais detalhados com sugestões de composição, texto, cores e emoções. Use ao planejar miniaturas, melhorar a CTR ou instruir designers. |

### <a id="conversao-para-formato-curto"></a>Conversao Para Formato Curto

| Recurso | Tipo | Origem | Descrição e Aplicação |
| :--- | :--- | :--- | :--- |
| <a id="social-conversao-para-formato-curto"></a>**`/social-conversao-para-formato-curto`** | `Workflow` | `0 Mkt` | Converta vídeos longos em conteúdo curto para TikTok, YouTube Shorts e Instagram Reels. Identifica momentos virais, cria ganchos e adapta scripts para formato vertical. Use ao adaptar vídeos, criar Shorts a partir de vídeos longos ou planejar conteúdo multiplataforma. |

### <a id="direcao-de-arte-ia"></a>Direcao De Arte Ia

| Recurso | Tipo | Origem | Descrição e Aplicação |
| :--- | :--- | :--- | :--- |
| <a id="social-direcao-de-arte-ia"></a>**`social-direcao-de-arte-ia`** | `Skill` | `0 Mkt` | Use para dirigir a arte de carrosséis 4:5 (1080x1350) gerados por IA: injeção do design system da marca em prompts de ChatGPT/GPT Image, FLUX e Midjourney e fluxo do Slide Âncora (3 variantes do hook e travamento do vencedor como referência). Gatilhos: \"prompt de imagem do carrossel\", \"slide âncora\", \"arte do carrossel com IA\". NÃO use para escrever a copy das lâminas (use social-carrossel), para prompts FLUX avulsos (use audiovisual-imagem-flux-prompts) nem para decidir a direção visual da marca (use brand-visual-direction). |

### <a id="estrategia"></a>Estrategia

| Recurso | Tipo | Origem | Descrição e Aplicação |
| :--- | :--- | :--- | :--- |
| <a id="social-estrategia"></a>**`social-estrategia`** | `Skill` | `0 Mkt` | Omnichannel social media strategy, content planning, platform-native distribution (LinkedIn, X/Twitter, Instagram), algorithmic retention mechanics, social listening, influencer partnerships and Reddit, X and Bluesky playbooks. NÃO use para LinkedIn orgânico (use social-linkedin), anúncios pagos (use ads-multiplataforma, ads-meta ou ads-analise-de-desempenho) nem carrosséis (use social-carrossel). |

### <a id="instagram-api"></a>Instagram Api

| Recurso | Tipo | Origem | Descrição e Aplicação |
| :--- | :--- | :--- | :--- |
| <a id="social-instagram-api"></a>**`/social-instagram-api`** | `Workflow` | `0 Mkt` | Integração da API Instagram Graph via curl. Use esta habilidade para buscar e publicar mídia do Instagram. |

### <a id="leitura-de-post-twitter"></a>Leitura De Post Twitter

| Recurso | Tipo | Origem | Descrição e Aplicação |
| :--- | :--- | :--- | :--- |
| <a id="social-leitura-de-post-twitter"></a>**`/social-leitura-de-post-twitter`** | `Workflow` | `0 Mkt` | Fetch Twitter/X post content by URL using jina.ai API to bypass JavaScript restrictions. Use when Claude needs to retrieve tweet content including author, timestamp, post text, images, and thread replies. Supports individual posts or batch fetching from x.com or twitter.com URLs. |

### <a id="linkedin"></a>Linkedin

| Recurso | Tipo | Origem | Descrição e Aplicação |
| :--- | :--- | :--- | :--- |
| <a id="social-linkedin"></a>**`social-linkedin`** | `Skill` | `0 Mkt` | Use para criar presença e autoridade orgânica no LinkedIn: auditar e reescrever o perfil, escrever posts e carrosséis de alto desempenho, usar fórmulas de post e montar um sistema de conteúdo de liderança de pensamento que gera leads inbound. Gatilhos: \"post de LinkedIn\", \"perfil do LinkedIn\", \"headline\", \"liderança de pensamento\", \"conteúdo para LinkedIn\", \"autoridade no LinkedIn\". NÃO use para anúncios no LinkedIn (use ads-multiplataforma), para estratégia de várias redes ao mesmo tempo (use social-estrategia) nem para prospecção por mensagem direta (use vendas-cold-email). |

### <a id="otimizacao-de-post-linkedin"></a>Otimizacao De Post Linkedin

| Recurso | Tipo | Origem | Descrição e Aplicação |
| :--- | :--- | :--- | :--- |
| <a id="social-otimizacao-de-post-linkedin"></a>**`/social-otimizacao-de-post-linkedin`** | `Workflow` | `0 Mkt` | Estilo narrativo profissional com quebras de linha, estratégia de hashtag e ganchos nas duas primeiras linhas para evitar truncamento |

### <a id="otimizacao-de-titulo-de-video"></a>Otimizacao De Titulo De Video

| Recurso | Tipo | Origem | Descrição e Aplicação |
| :--- | :--- | :--- | :--- |
| <a id="social-otimizacao-de-titulo-de-video"></a>**`/social-otimizacao-de-titulo-de-video`** | `Workflow` | `0 Mkt` | Otimize títulos de vídeo para taxa máxima de cliques (CTR) e SEO do YouTube/TikTok. Gera diversas variações de títulos equilibrando curiosidade, palavras-chave e práticas recomendadas de plataforma. Use ao nomear vídeos, melhorar a CTR ou testar títulos A/B. |

### <a id="seo-de-youtube"></a>Seo De Youtube

| Recurso | Tipo | Origem | Descrição e Aplicação |
| :--- | :--- | :--- | :--- |
| <a id="social-seo-de-youtube"></a>**`/social-seo-de-youtube`** | `Workflow` | `0 Mkt` | Otimize vídeos do YouTube para pesquisa e descoberta. Gera títulos, descrições, tags, hashtags e capítulos otimizados para SEO. Inclui pesquisa de palavras-chave e análise de concorrentes. Use ao publicar vídeos, melhorar a descoberta ou otimizar conteúdo existente. |

### <a id="transcricao-de-youtube"></a>Transcricao De Youtube

| Recurso | Tipo | Origem | Descrição e Aplicação |
| :--- | :--- | :--- | :--- |
| <a id="social-transcricao-de-youtube"></a>**`/social-transcricao-de-youtube`** | `Workflow` | `0 Mkt` | Baixe transcrições de vídeo do YouTube quando o usuário fornecer um URL do YouTube ou solicitar para baixar/obter/buscar uma transcrição do YouTube. Use também quando o usuário deseja transcrever ou obter legendas/legendas de um vídeo do YouTube. |

### <a id="youtube-para-notas"></a>Youtube Para Notas

| Recurso | Tipo | Origem | Descrição e Aplicação |
| :--- | :--- | :--- | :--- |
| <a id="social-youtube-para-notas"></a>**`social-youtube-para-notas`** | `Skill` | `0 Mkt` | Processe vídeos do YouTube em notas resumidas da Obsidian. Use quando receber um URL do YouTube para resumir, extrair insights ou transformar vídeos em notas. Aciona "resumir este vídeo", "processar este YouTube", "sobre o que é este vídeo" ou qualquer URL do YouTube compartilhado para processamento. |
| <a id="social-youtube-para-notas"></a>**`/social-youtube-para-notas`** | `Workflow` | `0 Mkt` | Processe vídeos do YouTube em notas resumidas da Obsidian. Use quando dado |

---

## <a id="vendas-vendas-b2b--prospecção"></a>vendas (Vendas B2B & Prospecção)

Total de recursos nesta macro-área: `14`

### <a id="cold-email"></a>Cold Email

| Recurso | Tipo | Origem | Descrição e Aplicação |
| :--- | :--- | :--- | :--- |
| <a id="vendas-cold-email"></a>**`vendas-cold-email`** | `Skill` | `0 Mkt` | Especialista em prospecção ativa B2B via cold email e cadências outbound. Domina a personalização em 4 níveis (icebreakers contextuais), estrutura de emails curtos de alto impacto, cadências de follow-up multitoque sem passivo-agressividade, CTAs de baixo atrito e infraestrutura de caixas secundárias. NÃO use para encontrar decisores, montar lista de leads, enriquecer contatos ou monitorar sinais de compra (use vendas-prospeccao-de-leads), nem para pontuar e rotear leads no CRM (use revenue-orquestracao-de-crm). |
| <a id="vendas-cold-email"></a>**`/vendas-cold-email`** | `Workflow` | `0 Mkt` | Gera sequências de e-mail frio com variações de assunto para teste A/B e timing de follow-up. Aponta para a skill vendas-cold-email. |

### <a id="cold-email-multicanal"></a>Cold Email Multicanal

| Recurso | Tipo | Origem | Descrição e Aplicação |
| :--- | :--- | :--- | :--- |
| <a id="vendas-cold-email-multicanal"></a>**`/vendas-cold-email-multicanal`** | `Workflow` | `0 Mkt` | Gera modelos de e-mail frio, mensagens de LinkedIn e follow-ups. Aponta para a habilidade vendas-cold-email. |

### <a id="direcao-b2b"></a>Direcao B2B

| Recurso | Tipo | Origem | Descrição e Aplicação |
| :--- | :--- | :--- | :--- |
| <a id="vendas-direcao-b2b"></a>**`@vendas-direcao-b2b`** | `Agent` | `0 Mkt` | Diretor de vendas B2B, RevOps e conformidade comercial. Use quando precisar estruturar processos de vendas consultivas complexas, implementar metodologias de qualificação (MEDDIC, BANT, SPIN), arquitetar esteiras de outbound, gerenciar riscos de fechamento de negócios e assegurar compliance regulatório (LGPD/GDPR e contratos). <example> Context: O time comercial precisa estruturar um processo de vendas enterprise com múltiplos tomadores de decisão. user: "Como estruturo o funil de vendas complexas da <marca> para fechar contratos anuais acima de R$ 50k?" assistant: "Vou acionar o vendas-direcao-b2b para desenhar a régua de qualificação MEDDIC, mapear o Economic Buyer e arquitetar a cadência de follow-up multicanal." <commentary> Demanda de estratégia e governança de vendas B2B complexas delegada ao diretor comercial. </commentary> </example> <example> Context: O usuário precisa de uma cadência de prospecção fria para diretores de marketing respeitando normas de privacidade. user: "Crie uma cadência de outbound cold email de 4 toques para a <marca> em conformidade com a LGPD." assistant: "Acionando o vendas-direcao-b2b para redigir a cadência com foco em dor de negócio, personalização sem atrito e mecanismo claro de opt-out conforme LGPD." <commentary> Outbound B2B combinado com rigor de conformidade e governança. </commentary> </example> |

### <a id="habilitacao-comercial"></a>Habilitacao Comercial

| Recurso | Tipo | Origem | Descrição e Aplicação |
| :--- | :--- | :--- | :--- |
| <a id="vendas-habilitacao-comercial"></a>**`@vendas-habilitacao-comercial`** | `Agent` | `0 Mkt` | Especialista em garantia de vendas e capacitação. Use para criar argumentos de venda personalizados, scripts de tratamento de objeções, correspondência de prova social e fluxos de trabalho de aceleração de negócios. Exemplos: <exemplo>Contexto: O usuário precisa de materiais de vendas. usuário: \"Crie um estudo de caso para nossos clientes corporativos\" assistente: \"Usarei o agente vendas-habilitacao-comercial para desenvolver um estudo de caso atraente com dados de ROI e depoimentos.\" <commentary>A criação de estudo de caso requer mensagens de vendas e experiência em prova social.</commentary></example> <example>Contexto: O usuário deseja melhorar as conversas de vendas. usuário: \"Ajude nossa equipe de vendas a lidar com objeções de preços\" assistente: \"Deixe-me implantar o agente de vendas-habilitacao-comercial para criar scripts de tratamento de objeções e cartões de batalha competitivos.\" <commentary>O tratamento de objeções requer profundo conhecimento da psicologia do comprador e do posicionamento competitivo.</commentary></example> |

### <a id="materiais-de-venda"></a>Materiais De Venda

| Recurso | Tipo | Origem | Descrição e Aplicação |
| :--- | :--- | :--- | :--- |
| <a id="vendas-materiais-de-venda"></a>**`vendas-materiais-de-venda`** | `Skill` | `0 Mkt` | Use para criar os materiais que o time comercial usa para fechar negócio (em inglês, sales enablement): deck de vendas, one-pager, pitch personalizado para um prospecto, script de demonstração por tipo de call, mapa de objeções e respostas, case de sucesso, coleta de depoimentos e resposta a RFP/RFI. Gatilhos: \"faça um case\", \"preciso de um depoimento\", \"responda esta RFP\", \"script de demo\", \"objeções de preço\", \"one-pager\", \"pitch para esta empresa\". NÃO use para qualificar leads, prever receita ou gerir negócios no funil (use vendas-pipeline), técnicas de conversa e negociação (use vendas-metodologias-b2b), deck de investidor (use audiovisual-pitch-deck), battlecard de concorrente (use revenue-inteligencia-competitiva) nem cold email (use vendas-cold-email). |
| <a id="vendas-materiais-de-venda"></a>**`/vendas-materiais-de-venda`** | `Workflow` | `0 Mkt` | Deck, one-pager, pitch, script de demonstração, objeções, case e resposta a RFP. Aponta para a habilidade vendas-materiais-de-venda. |

### <a id="metodologias-b2b"></a>Metodologias B2B

| Recurso | Tipo | Origem | Descrição e Aplicação |
| :--- | :--- | :--- | :--- |
| <a id="vendas-metodologias-b2b"></a>**`vendas-metodologias-b2b`** | `Skill` | `0 Mkt` | Use para aplicar metodologias de venda consultiva e negociação B2B complexa: Challenger Sale, SPIN Selling, Sandler System e Never Split the Difference. Gatilhos: \"SPIN\", \"Challenger\", \"Sandler\", \"negociação difícil\", \"venda consultiva\". NÃO use para gestão de pipeline e previsão (use vendas-pipeline), cadência de prospecção fria (use vendas-cold-email) nem material de venda (use vendas-materiais-de-venda). |

### <a id="personalizacao-em-escala"></a>Personalizacao Em Escala

| Recurso | Tipo | Origem | Descrição e Aplicação |
| :--- | :--- | :--- | :--- |
| <a id="vendas-personalizacao-em-escala"></a>**`/vendas-personalizacao-em-escala`** | `Workflow` | `0 Mkt` | Gere primeiras linhas personalizadas e exclusivas para centenas de clientes em potencial usando notícias da empresa, atividades no LinkedIn e conexões mútuas. Economiza mais de 10 horas de pesquisa manual por campanha. Use quando precisar de divulgação personalizada em grande volume. |

### <a id="pipeline"></a>Pipeline

| Recurso | Tipo | Origem | Descrição e Aplicação |
| :--- | :--- | :--- | :--- |
| <a id="vendas-pipeline"></a>**`vendas-pipeline`** | `Skill` | `0 Mkt` | Especialista em orquestração de pipeline comercial B2B, qualificação rigorosa (MEDDIC e BANT), previsão de receita (Forecasting), gestão de risco de negócios, preparação de reuniões de descoberta, passagem de bastão de Vendas para Sucesso do Cliente e comissionamento de vendas (OTE, aceleradores, cota). NÃO use para materiais de venda como deck, case, depoimento, script de demo, objeções e RFP (use vendas-materiais-de-venda), QBR e renovação de contrato (use growth-retencao-e-churn), pontuação de leads, higiene de CRM e RevOps (use revenue-orquestracao-de-crm), técnicas de conversação e negociação (use vendas-metodologias-b2b), cold email e cadências de prospecção (use vendas-cold-email), automação de email e réguas de nutrição (use email-automacao) nem atribuição de marketing (use data-atribuicao-e-relatorios). |

### <a id="pitch-de-patrocinio"></a>Pitch De Patrocinio

| Recurso | Tipo | Origem | Descrição e Aplicação |
| :--- | :--- | :--- | :--- |
| <a id="vendas-pitch-de-patrocinio"></a>**`/vendas-pitch-de-patrocinio`** | `Workflow` | `0 Mkt` | Gere propostas de patrocínio profissionais e kits de mídia para marcas. Cria propostas atraentes destacando o valor do canal, dados demográficos do público e ideias de colaboração. Use ao buscar patrocínios, responder a dúvidas da marca ou criar kits de mídia. |

### <a id="prospeccao-de-leads"></a>Prospeccao De Leads

| Recurso | Tipo | Origem | Descrição e Aplicação |
| :--- | :--- | :--- | :--- |
| <a id="vendas-prospeccao-de-leads"></a>**`vendas-prospeccao-de-leads`** | `Skill` | `0 Mkt` | Use para encontrar e preparar prospectos B2B antes do contato: achar decisores por cargo, porte e setor, montar lista de leads, enriquecer contatos (e-mail, telefone, tecnologia usada), conferir e-mails antes do envio e monitorar sinais de compra como rodada de investimento, vagas abertas e troca de tecnologia. Gatilhos: \"ache decisores\", \"lista de prospects\", \"pesquisa de leads\", \"enriquecer contatos\", \"sinais de compra\", \"quem está contratando\", \"Apollo\". NÃO use para escrever o e-mail frio ou a cadência (use vendas-cold-email), pontuar e rotear leads ou limpar o CRM (use revenue-orquestracao-de-crm), nem para qualificar um negócio com MEDDIC ou BANT (use vendas-pipeline). |
| <a id="vendas-prospeccao-de-leads"></a>**`/vendas-prospeccao-de-leads`** | `Workflow` | `0 Mkt` | Sugere empresas-alvo e estratégia de contato. Aponta para a skill vendas-prospeccao-de-leads. |

### <a id="qualificacao-de-leads"></a>Qualificacao De Leads

| Recurso | Tipo | Origem | Descrição e Aplicação |
| :--- | :--- | :--- | :--- |
| <a id="vendas-qualificacao-de-leads"></a>**`@vendas-qualificacao-de-leads`** | `Agent` | `0 Mkt` | Especialista em detecção de intenções e pontuação de leads. Use para análise comportamental, reconhecimento de padrões de engajamento, previsão de prontidão para vendas e recomendação de próximas ações para clientes potenciais. Exemplos: <exemplo>Contexto: o usuário deseja melhorar a qualidade do lead. usuário: \"Estamos recebendo muitos leads, mas eles não estão convertendo em vendas\" assistente: \"Vou usar o agente vendas-qualificacao-de-leads para criar um modelo de pontuação de leads e critérios de qualificação.\" <commentary>Isso requer análise comportamental e experiência em pontuação, então delegue para vendas-qualificacao-de-leads.</commentary></example> <example>Contexto: O usuário precisa segmentar seu público. usuário: \"Ajude-me a criar segmentos de clientes para campanhas direcionadas\" assistente: \"Deixe-me implantar o agente de vendas-qualificação-de-leads para analisar padrões de engajamento e criar definições de segmento.\" <commentary>A segmentação de público requer uma análise comportamental profunda.</commentary></example> |

---
