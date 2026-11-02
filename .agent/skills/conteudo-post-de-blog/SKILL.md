---
name: conteudo-post-de-blog
description: Transform brain dumps into polished blog posts in the brand's own voice. Use when the user wants to write a blog post with scattered ideas, talking points, and conclusions that need organization into a cohesive, conversational narrative.
license: MIT
metadata:
  author: Antigravity Multi-IA Hub & Felipe Bahia (Futuro Mercado)
  version: 1.0.0
---

# Blog Writer

Transform unstructured brain dumps into polished blog posts na voz da marca.

> Ajustado em 2026-10-29: a versão anterior pedia para escrever "na voz do Nick Nisi" (um blogueiro de terceiros). A técnica (organizar um brain dump em narrativa, usando o Story Circle) é boa e foi mantida; a voz agora vem de `_brands/<marca>/brand-voice.md` (regra 1.1 do `CLAUDE.md`), não de uma pessoa real. Se a marca não tiver `brand-voice.md` definido, parar e perguntar antes de escrever.

## Process

### 1. Receive the Brain Dump

Accept whatever the user provides:
- Scattered thoughts and ideas
- Technical points to cover
- Code examples or commands
- Conclusions or takeaways
- Links to reference
- Random observations

Don't require organization. The mess is the input.

### 2. Read Voice and Tone

Ler `_brands/<marca>/brand-voice.md` da marca pedida (regra 1.1) — ele define o tom real a seguir. Na ausência de instrução específica ali, usar como base estas características genéricas de blog pessoal/técnico (ajustar sempre ao que o `brand-voice.md` disser primeiro):
- Conversational yet substantive
- Vulnerable and authentic
- Journey-based narrative
- Mix of short and long sentences
- Specific examples and real details
- Self-aware humor

### 3. Check for Story Potential

Read `references/story-circle.md` to understand the narrative framework.

Determine if the content fits a story structure:
- Is there a journey from one understanding to another?
- Can you identify a problem and resolution?
- Does it follow: comfort → disruption → return changed?

Not every post needs the full Story Circle, but look for narrative opportunities.

### 4. Organize Content

Structure the material into sections:

**Common structures:**
- Problem/experience → Journey → Results → Lessons
- Setup → Challenge → Discovery → Application
- Philosophy → How-to → Reflection
- Current state → Past → Learning → Future

Choose the structure that fits the content.

### 5. Write in Nick's Voice

Apply voice characteristics:

**Opening:**
- Hook with current position or recent event
- Set up tension or question
- Be direct and honest

**Body:**
- Vary paragraph length
- Use short paragraphs for emphasis
- Include specific details (tool names, commands, numbers)
- Show vulnerability where appropriate
- Use inline code formatting naturally
- Break up text with headers

**Technical content:**
- Assume reader knowledge but explain when needed
- Show actual commands and examples
- Be honest about limitations
- Use casual tool references

**Tone modulation:**
- Technical sections: clear, instructional
- Personal sections: vulnerable, reflective
- Be conversational throughout

**Ending:**
- Tie back to opening
- Forward-looking perspective
- Actionable advice
- Optimistic or thought-provoking

### 6. Review and Refine

Check the post:

- Does it sound conversational?
- Is there a clear narrative arc?
- Are technical details specific and accurate?
- Does it show vulnerability appropriately?
- Are paragraphs varied in length?
- Is humor self-aware, not forced?
- Does it end with momentum?

Show the post to the user for feedback and iterate.

## Voice Guidelines

### Do:
- Write like talking to a peer over coffee
- Admit uncertainty or being wrong
- Use specific examples with details
- Vary sentence and paragraph length
- Include inline code naturally
- Show the journey, not just the destination
- Use humor sparingly and self-aware
- End with forward momentum

### Don't:
- Use corporate or marketing speak
- Pretend to have all answers
- Be preachy or condescending
- Over-explain basic concepts
- Force humor or emojis
- Hide mistakes or uncertainty
- Write without specific examples

## Example Patterns

### Opening hooks:
```markdown
"AI is going to replace developers."

I must have heard that phrase a hundred times in the last year.
```

```markdown
I've been thinking a lot about how we use AI in our daily work.
```

### Emphasis through structure:
```markdown
Then something clicked.

I watched it use rg to search through codebases, just like I would.
```

### Vulnerability:
```markdown
I won't lie – joining Meta was intimidating.
```

### Technical details:
```markdown
I watched it use `rg` to search through codebases, just like I would. 
It ran `npm test` to verify its changes weren't breaking anything.
```

### Conclusions:
```markdown
You're not being replaced; you're being amplified.
```

## Bundled Resources

### References

- `references/story-circle.md` - Story Circle narrative framework. Check if content fits a story structure.

## Workflow Example

User provides brain dump:
```
thoughts on using cursor vs claude code
- cursor is in IDE, feels familiar
- but claude code is in terminal, my natural environment
- tried cursor first, felt weird leaving vim
- claude code met me where I was
- not about which is better, about workflow fit
- some devs love IDE integration
- I need terminal access
- conclusion: use what fits YOUR workflow
```

Process:
1. Read voice-tone.md
2. Check story-circle.md - yes, there's a journey here
3. Identify structure: Current tools → Trying Cursor → Finding Claude Code → Realization
4. Write opening hook about tool debates
5. Show vulnerability about trying new things
6. Include specific terminal commands naturally
7. Conclude with "meet yourself where you are" message
8. Review for conversational tone and specific details

## Roteiros guiados (vindos do kit AgentKits)

Roteiros que fazem perguntas ao usuário antes de entregar. O texto base é inglês.

- **[blog.md](references/blog.md)** — Roteiro guiado para criar um post de blog otimizado para SEO.

## Referências vindas de outras skills

- **[content-writing.md](references/content-writing.md)** — Core editorial craft, pacing, and scannability rules.
- **[write-blog.md](references/write-blog.md)** — Rapid blog drafting framework and article templates.
- **[blog-template.md](references/blog-template.md)** — Ready-to-use markdown blog layouts.
