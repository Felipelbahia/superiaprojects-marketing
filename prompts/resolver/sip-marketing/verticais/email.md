# email

E-mail marketing: copy, newsletter, automação, assunto, modelos e entregabilidade.

> Gerado por build_sip_index.py. Não edite à mão. Skill: `"<HUB>/.agents/skills/<nome>/SKILL.md"`; agent: `"<HUB>/.agents/agents/<nome>.md"`; workflow: `"<HUB>/.agents/workflows/<nome>.md"`.

## Skills (4)

| Skill | Use quando |
| --- | --- |
| `email-automacao` | Arquiteto de jornadas automatizadas de email e automações de ciclo de vida em CRMs (ActiveCampaign, HubSpot, Customer.io). Estrutura Welcome Series em 5 etapas, esteiras de onboarding e ativação de produto SaaS, fluxos de recuperação de carrinho abandonado, automações de reengajamento e Sunset Policy contra contatos inativos. |
| `email-copy` | Use para escrever e-mails de marketing que convertem: linhas de assunto, preheaders, narrativas (Story-Lesson-Offer, Soap Opera, Seinfeld), texto puro versus HTML leve e otimização de CTOR. Gatilhos: "assunto de e-mail", "copy de e-mail", "sequência de e-mails". |
| `email-entregabilidade` | Use para proteger a entregabilidade de e-mail (inbox placement): registros DNS (SPF, DKIM, DMARC, BIMI), aquecimento de domínio de 21 dias, higiene de lista contra spam traps e monitoramento de reputação no Google Postmaster. Gatilhos: "caiu no spam", "SPF DKIM DMARC", "warm-up", "reputação de domínio". |
| `email-newsletter` | Use para transformar a experiência diária do autor em rascunhos de newsletter prontos para publicar, com playbooks editoriais, estratégias de crescimento, curadoria e modelos por setor (Tech, Fintech, RH, Vendas, Operações). Gatilhos: "newsletter", "edição semanal", "crescer newsletter". |

## Agents (1)

| Agent | Use quando |
| --- | --- |
| `email-orquestracao-de-campanhas` | Email campaign orchestration specialist. Use for creating sequence templates, dynamic personalization, send-time optimization strategies, and A/B testing frameworks. Examples: <example>Context: User needs to set up email automation. user: "Create a welcome email sequence for new subscribers" assistant: "I'll use the email-orquestracao-de-campanhas agent to design a welcome sequence with personalization and optimal timing." <commentary>Email sequence design requires expertise in automation and engagement optimization.</commentary></example> <example>Context: User wants to improve email performance. user: "Our email open rates are declining" assistant: "Let me deploy the email-orquestracao-de-campanhas agent to audit your emails and create an A/B testing plan." <commentary>Email optimization requires deep knowledge of deliverability and engagement factors.</commentary></example> |

## Workflows (3)

| Workflow | Use quando |
| --- | --- |
| `/email-modelos` | Generate professional email templates for various business scenarios including sales outreach, customer support, internal communications, follow-ups, and apologies. Creates personalized, tone-appropriate templates with subject lines and formatting. Use when users need to write business emails, cold outreach, or professional communications. |
| `/email-newsletter` | Writing coach that extracts educational content from your daily experiences |
| `/email-otimizacao-de-assunto` | A/B test subject line variations using proven copywriting frameworks. Predict open rates based on historical performance. |

