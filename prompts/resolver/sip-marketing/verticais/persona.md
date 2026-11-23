# persona

Público: ICP, personas, descoberta e entrevistas com clientes, análise de feedback.

> Gerado por build_sip_index.py. Não edite à mão. Skill: `"<HUB>/.agents/skills/<nome>/SKILL.md"`; agent: `"<HUB>/.agents/agents/<nome>.md"`; workflow: `"<HUB>/.agents/workflows/<nome>.md"`.

## Skills (2)

| Skill | Use quando |
| --- | --- |
| `persona-descoberta-de-clientes` | Use para validar ideia, problema e solução com clientes: Mom Test, entrevista de problema e de solução, Customer Development (Steve Blank), descoberta contínua de produto (Teresa Torres) e pesquisas (surveys). Gatilhos: "validar ideia", "entrevista com clientes", "Mom Test", "descoberta de produto". |
| `persona-icp` | Use para construir personas, perfil de cliente ideal (ICP), mapa de Jobs-to-be-Done, gatilhos de compra, roteiros de voz do cliente, pesquisa de público e pontuação de aderência ao ICP. Gatilhos: "persona", "ICP", "cliente ideal", "JTBD", "segmentar público". |

## Agents (1)

| Agent | Use quando |
| --- | --- |
| `persona-descoberta-interativa` | Interactive customer persona discovery agent. Use when you need to build detailed customer profiles through conversation. Asks strategic questions with smart options, collects answers progressively, and constructs comprehensive buyer personas. Examples: <example>Context: User wants to understand their customer. user: "Help me understand who my ideal customer is" assistant: "I'll use the persona-descoberta-interativa agent to conduct an interactive discovery session and build your customer profile." <commentary>Building personas requires progressive questioning and synthesis.</commentary></example> |

## Workflows (4)

| Workflow | Use quando |
| --- | --- |
| `/persona-analise-de-feedback` | Synthesize user feedback from multiple channels and identify patterns to inform product decisions. Use when analyzing feedback, prioritizing feature requests, conducting NPS surveys, or understanding user sentiment. Covers feedback collection, categorization, prioritization frameworks, and closing the feedback loop. |
| `/persona-criacao-de-persona` | Create detailed user personas based on research and data. Develop realistic representations of target users to guide product decisions and ensure user-centered design. |
| `/persona-entrevistas-de-descoberta` | Use when validating product assumptions before building, discovering unmet user needs, understanding customer problems and workflows, testing concepts or positioning, researching target markets, identifying jobs-to-be-done and hiring triggers, uncovering pain points and workarounds, or when users mention user research, customer interviews, surveys, discovery interviews, validation studies, or voice of customer. |
| `/persona-gerador-de-icp` | Create detailed buyer personas and Ideal Customer Profiles (ICP) for B2B and B2C marketing. Generates comprehensive profiles with demographics, psychographics, pain points, goals, objections, and messaging strategies. Use when defining target audience, creating ICP, or developing customer profiles. |

