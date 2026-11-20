# Registro de Aprendizado e Governança de Feedback

Este documento registra as preferências, correções e aprendizados manifestados pelo usuário ou revisor durante os ciclos de validação de conteúdo desta marca. O objetivo é evitar a repetição de erros e permitir a evolução contínua da voz da marca sem generalizações precipitadas.

> **Princípio de Governança:** Nenhuma observação pontual de uma peça é promovida para o `brand-voice.md` sem confirmação formal do usuário. Registre a fala literal, determine o alcance e monitore o estado da regra.

---

## 1. Classificação de Escopo e Ciclo de Vida

### 1.1. Os 4 Níveis de Alcance (Escopo)
- **`peça`:** Vale estritamente para o arquivo ou entrega pontual em desenvolvimento. Não afeta outros conteúdos.
- **`canal`:** Vale para todas as publicações do canal especificado (ex.: LinkedIn, Instagram, Blog).
- **`persona`:** Vale para qualquer conteúdo direcionado àquele segmento de público específico.
- **`projeto`:** Vale universalmente para todas as comunicações e canais desta marca.

### 1.2. Os 4 Estados do Feedback
- **`proposta`:** Anotado a partir de comentário do usuário, mas restrito ao teste inicial; aguarda validação.
- **`confirmada`:** O usuário chancelou expressamente que o aprendizado deve ser estendido como padrão de canal ou marca.
- **`aplicada`:** Regra incorporada formalmente no `brand-voice.md`, `style-guide.md` ou `glossario.md` da marca.
- **`arquivada`:** Regra superada por decisão posterior, temporária ou revogada pelo usuário.

---

## 2. Tabela de Registros de Feedback

| ID | Data | Fala Literal do Usuário | Interpretação Técnica da Regra | Alcance | Estado | Validação Seguinte / Destino |
|:---:|:---:|---|---|:---:|:---:|---|
| `FB-001` | `AAAA-MM-DD` | *"Nesse post achei muito longo, corta para 3 linhas"* | Limitar introdução do anúncio específico a 3 períodos curtos. | `peça` | `aplicada` | Restrito ao criativo do post em edição; não aplicar a posts orgânicos. |
| `FB-002` | `AAAA-MM-DD` | *"No LinkedIn nunca use mais de 2 hashtags"* | Restrição técnica de distribuição orgânica no LinkedIn. | `canal` | `confirmada` | Promover para `style-guide.md: Regras por Canal (LinkedIn)`. |
| `FB-003` | `AAAA-MM-DD` | *"Não fale que somos líderes de mercado, soa arrogante"* | Proibição de autopromoção vazia e superlativos não fundamentados. | `projeto` | `aplicada` | Integrado em `brand-voice.md: "O que NÃO comunicar"`. |
| `FB-004` | `AAAA-MM-DD` | *"Para diretores de TI, evite metáforas de cozinha"* | Adequação de repertório e analogias para a Persona Tech Executive. | `persona` | `proposta` | Testar nas próximas 2 peças da Persona antes de confirmar. |

---

## 3. Protocolo de Promoção de Regras

```
┌────────────────────────────────────────────────────────────────────────┐
│                   FLUXO DE PROMOÇÃO DE APRENDIZADO                     │
│                                                                        │
│   Feedback do Usuário ──> Registro como 'proposta' (com alcance)       │
│                                      │                                 │
│                                      ▼                                 │
│                        Confirmação do Usuário?                         │
│                           ├── Sim ──> 'confirmada' ──> 'aplicada' no   │
│                           │                            brand-voice.md  │
│                           └── Não ──> Mantém 'peça' ou 'arquivada'     │
└────────────────────────────────────────────────────────────────────────┘
```

1. **Captura Fiel:** Anote a frase exata entre aspas no campo "Fala Literal", acompanhada da tradução técnica operacional.
2. **Checagem de Escopo:** Em caso de dúvida sobre o alcance, pergunte ao usuário: *"Essa preferência deve valer apenas para esta peça ou deve virar regra fixa para todo o [Canal / Projeto]?"*.
3. **Migração Oficial:** Ao atingir o estado `confirmada` com alcance `canal` ou `projeto`, migre a regra para o arquivo canônico correspondente da marca e marque como `aplicada` na tabela acima.

