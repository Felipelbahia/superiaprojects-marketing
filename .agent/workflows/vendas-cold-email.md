---
name: vendas-cold-email
description: Gera sequências de e-mail frio com variações de assunto para teste A/B e timing de follow-up. Aponta para a skill vendas-cold-email.
---

# /cold-email-sequence-generator

Este workflow é só a porta de entrada do comando `/cold-email-sequence-generator`. O conteúdo completo, mantido e atualizado, fica numa fonte única: a skill [vendas-cold-email](../skills/vendas-cold-email/SKILL.md).

## Instruções

1. Leia e siga a skill [vendas-cold-email](../skills/vendas-cold-email/SKILL.md) (caminho: `.agent/skills/vendas-cold-email/SKILL.md`), em especial [cold-outreach-sequence.md](../skills/vendas-cold-email/references/cold-outreach-sequence.md) (fluxo de 7 toques), [subject-lines.md](../skills/vendas-cold-email/references/subject-lines.md) e [sequencias-de-email-frio.md](../skills/vendas-cold-email/references/sequencias-de-email-frio.md) (modelos prontos por vertical: SaaS, agência, parceria).
2. Siga a regra 1.1 do `CLAUDE.md`: confirme a marca antes de escrever.

> Fundido na E6 (2026-10-28): a versão anterior (697 linhas) duplicava quase tudo que já estava na skill `vendas-cold-email`; o único bloco exclusivo (modelos de assunto por vertical) foi movido para [sequencias-de-email-frio.md](../skills/vendas-cold-email/references/sequencias-de-email-frio.md). A versão anterior completa está guardada em `.agent/skills/_arquivo/mescladas/e6-workflows/cold-email-sequence-generator.md`.
