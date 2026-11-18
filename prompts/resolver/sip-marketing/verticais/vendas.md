# vendas

Vendas B2B: prospecção, cold email, pipeline, metodologias, materiais e personalização em escala.

> Gerado por build_sip_index.py. Não edite à mão. Skill: `"<HUB>/.agent/skills/<nome>/SKILL.md"`; agent: `"<HUB>/.agent/agents/<nome>.md"`; workflow: `"<HUB>/.agent/workflows/<nome>.md"`.

## Skills (5)

| Skill | Use quando |
| --- | --- |
| `vendas-cold-email` | Especialista em prospecção ativa B2B via cold email e cadências outbound. Domina a personalização em 4 níveis (icebreakers contextuais), estrutura de emails curtos de alto impacto, cadências de follow-up multitoque sem passivo-agressividade, CTAs de baixo atrito e infraestrutura de caixas secundárias. |
| `vendas-materiais-de-venda` | Use para criar os materiais que o time comercial usa para fechar negócio (em inglês, sales enablement): deck de vendas, one-pager, pitch personalizado para um prospecto, script de demonstração por tipo de call, mapa de objeções e respostas, case de sucesso, coleta de depoimentos e resposta a RFP/RFI. Gatilhos: "faça um case", "preciso de um depoimento", "responda esta RFP", "script de demo", "objeções de preço", "one-pager", "pitch para esta empresa". |
| `vendas-metodologias-b2b` | Use para aplicar metodologias de venda consultiva e negociação B2B complexa: Challenger Sale, SPIN Selling, Sandler System e Never Split the Difference. Gatilhos: "SPIN", "Challenger", "Sandler", "negociação difícil", "venda consultiva". |
| `vendas-pipeline` | Especialista em orquestração de pipeline comercial B2B, qualificação rigorosa (MEDDIC e BANT), previsão de receita (Forecasting), gestão de risco de negócios, preparação de reuniões de descoberta, passagem de bastão de Vendas para Sucesso do Cliente e comissionamento de vendas (OTE, aceleradores, cota). |
| `vendas-prospeccao-de-leads` | Use para encontrar e preparar prospectos B2B antes do contato: achar decisores por cargo, porte e setor, montar lista de leads, enriquecer contatos (e-mail, telefone, tecnologia usada), conferir e-mails antes do envio e monitorar sinais de compra como rodada de investimento, vagas abertas e troca de tecnologia. Gatilhos: "ache decisores", "lista de prospects", "pesquisa de leads", "enriquecer contatos", "sinais de compra", "quem está contratando", "Apollo". |

## Agents (3)

| Agent | Use quando |
| --- | --- |
| `vendas-direcao-b2b` | Diretor de vendas B2B, RevOps e conformidade comercial. Use quando precisar estruturar processos de vendas consultivas complexas, implementar metodologias de qualificação (MEDDIC, BANT, SPIN), arquitetar esteiras de outbound, gerenciar riscos de fechamento de negócios e assegurar compliance regulatório (LGPD/GDPR e contratos). <example> Context: O time comercial precisa estruturar um processo de vendas enterprise com múltiplos tomadores de decisão. user: "Como estruturo o funil de vendas complexas da <marca> para fechar contratos anuais acima de R$ 50k?" assistant: "Vou acionar o vendas-direcao-b2b para desenhar a régua de qualificação MEDDIC, mapear o Economic Buyer e arquitetar a cadência de follow-up multicanal." <commentary> Demanda de estratégia e governança de vendas B2B complexas delegada ao diretor comercial. </commentary> </example> <example> Context: O usuário precisa de uma cadência de prospecção fria para diretores de marketing respeitando normas de privacidade. user: "Crie uma cadência de outbound cold email de 4 toques para a <marca> em conformidade com a LGPD." assistant: "Acionando o vendas-direcao-b2b para redigir a cadência com foco em dor de negócio, personalização sem atrito e mecanismo claro de opt-out conforme LGPD." <commentary> Outbound B2B combinado com rigor de conformidade e governança. </commentary> </example> |
| `vendas-habilitacao-comercial` | Sales collateral and enablement specialist. Use for creating personalized pitches, objection handling scripts, social proof matching, and deal acceleration workflows. Examples: <example>Context: User needs sales materials. user: "Create a case study for our enterprise clients" assistant: "I'll use the vendas-habilitacao-comercial agent to develop a compelling case study with ROI data and testimonials." <commentary>Case study creation requires sales messaging and social proof expertise.</commentary></example> <example>Context: User wants to improve sales conversations. user: "Help our sales team handle pricing objections" assistant: "Let me deploy the vendas-habilitacao-comercial agent to create objection handling scripts and competitive battlecards." <commentary>Objection handling requires deep understanding of buyer psychology and competitive positioning.</commentary></example> |
| `vendas-qualificacao-de-leads` | Intent detection and lead scoring specialist. Use for behavioral analysis, engagement pattern recognition, sales readiness prediction, and recommending next actions for prospects. Examples: <example>Context: User wants to improve lead quality. user: "We're getting lots of leads but they're not converting to sales" assistant: "I'll use the vendas-qualificacao-de-leads agent to design a lead scoring model and qualification criteria." <commentary>This requires behavioral analysis and scoring expertise, so delegate to the vendas-qualificacao-de-leads.</commentary></example> <example>Context: User needs to segment their audience. user: "Help me create customer segments for targeted campaigns" assistant: "Let me deploy the vendas-qualificacao-de-leads agent to analyze engagement patterns and create segment definitions." <commentary>Audience segmentation requires deep behavioral analysis.</commentary></example> |

## Workflows (6)

| Workflow | Use quando |
| --- | --- |
| `/vendas-cold-email` | Gera sequências de e-mail frio com variações de assunto para teste A/B e timing de follow-up. Aponta para a skill vendas-cold-email. |
| `/vendas-cold-email-multicanal` | Gera modelos de e-mail frio, mensagens de LinkedIn e follow-ups. Aponta para a skill vendas-cold-email. |
| `/vendas-materiais-de-venda` | Deck, one-pager, pitch, script de demo, objeções, case e resposta a RFP. Aponta para a skill vendas-materiais-de-venda. |
| `/vendas-personalizacao-em-escala` | Generate unique personalized first lines for hundreds of prospects using company news, LinkedIn activity, and mutual connections. Saves 10+ hours of manual research per campaign. Use when you need personalized outreach at volume. |
| `/vendas-pitch-de-patrocinio` | Generate professional sponsorship pitches and media kits for brands. Creates compelling proposals highlighting channel value, audience demographics, and collaboration ideas. Use when seeking sponsorships, responding to brand inquiries, or creating media kits. |
| `/vendas-prospeccao-de-leads` | Sugere empresas-alvo e estratégia de contato. Aponta para a skill vendas-prospeccao-de-leads. |

