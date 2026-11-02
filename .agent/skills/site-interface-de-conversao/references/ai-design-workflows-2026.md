# Interfaces e landing pages com IA (pesquisa, janeiro de 2026)

> Fontes originais: Perplexity Pro (75+ fontes) e Gemini Pro, pesquisa de 2026-01-28. Na R16b ficaram só as partes de **interface e página**. Imagem para 3D, consistência de personagem e Mixamo (assuntos de vídeo e jogo) estão na versão original, em `.agent/skills/_arquivo/mescladas/r16b-design/ui-ux-conversion-designer/ai-design-workflows-2026.original.md`; só vão para o projeto de edição de vídeo com autorização do usuário. Dados de ferramentas envelhecem rápido: conferir antes de recomendar.

## 1. Geração de interface com IA

| Ferramenta | Tecnologia | Qualidade | Integração |
|---|---|---|---|
| **v0.dev** (Vercel) | GPT-4 + shadcn/ui | React pronto para produção | Direto para Next.js |
| **aura.build** | Claude + custom | Componentes de design elevado | Copiar e colar React/HTML |
| **Galileo AI** | Modelo próprio | Mockups de alta fidelidade | Exporta para Figma |
| **Claude Artifacts** | Claude 3+ | Protótipos funcionais | Copiar e colar |
| **Gemini Pro** | Gemini 1.5 | Iteração rápida | Exportação manual |

**aura.build, boas práticas:** descrever o efeito visual desejado (por exemplo "cartão estilo jogo de corrida", "parallax no hover", "inclinação 3D"); citar referências de nível Awwwards; dar destinos e conteúdos concretos para ancorar o design; **salvar os prompts** (o histórico da ferramenta nem sempre persiste).

**v0.dev, boas práticas:** começar com restrições claras ("só shadcn/ui, Tailwind"); entregar os tokens de design (paleta, escala tipográfica) antes; iterar em seções, não regerar a página inteira; exportar cedo para o ambiente local e ajustar lá.

**Fluxo com sistema de design:**

```
Tokens (Figma/JSON) → prompt com restrições → componente gerado → integração e polimento manual → biblioteca de componentes
```

Neste hub os tokens vêm de `_brands/<marca>/design-system/tokens.json` (skill [brand-design-system](../../brand-design-system/SKILL.md)).

**Armadilha:** interface gerada por IA tende ao genérico. Sempre aplicar o refinamento da marca depois.

## 2. "Vibe design"

Termo de Andrej Karpathy (2024, para código), adaptado a design por praticantes como Pieter Levels e Dilum Sanjaya. Princípios: velocidade acima de perfeição; deixar a IA repetir e focar a direção criativa; aceitar os acidentes felizes; empilhar ferramentas, cada uma acrescenta uma camada.

```
1. Esboço ou captura da ideia → 2. v0.dev para a interface inicial → 3. iterar ("deixe mais [adjetivo]") → 4. polir seções à mão → 5. publicar em horas
```

**Quando NÃO usar:** peças críticas de marca com especificação exata; setores regulados (saúde, finanças); sistemas de design que exigem consistência ao pixel.

## 3. Fluxos de ponta a ponta

**Peças de campanha:** briefing → imagem-chave (Midjourney) → variações por formato (DALL-E 3) → adaptação de layout (Canva/Figma) → versões em movimento (Runway) → entrega. Tempo citado: 2 a 4 horas contra 2 a 3 dias.

**Landing page (estilo indie hacker):** v0.dev gera a estrutura → Claude refina copy e interações → Midjourney faz as imagens → Vercel publica. Tempo citado: 30 minutos. **Neste hub o procedimento equivalente, com marca, autorização de código e teste, é o workflow [site-construcao-de-landing-page](../../../workflows/site-construcao-de-landing-page.md).**

## 4. Escolha de ferramenta

| Uso | Principal | Reserva |
|---|---|---|
| Prototipar interface | v0.dev | Galileo AI |
| Componentes de design elevado | aura.build | v0.dev |
| Peça gráfica para campanha | Midjourney v6 | Nano Banana |
| Movimento e vídeo | Runway Gen-3 | Kling |
| Copy e texto de interface | Claude | GPT-4 |

## 5. Referências

[Documentação do v0.dev](https://v0.dev/docs) · YouTube: Theo Browne (t3.gg), Pieter Levels · Comunidades: #vibedesign, #aidesign no X; Discord do Midjourney e da Vercel.
