# Ordem Estrita de Precedência de Fontes e Trava contra Resolução Silenciosa

**Versão:** 1.0.0  
**Módulo:** `brand-voice-messaging`  
**Crédito de Origem:** Conceitos de hierarquia de dados e resolução transparente de conflitos adaptados a partir de `promovaweb/inboundfy` (licença AGPL-3.0), redigidos com estrutura e regras autorais exclusivas do ecossistema Super IA Projects `0 Mkt`.

---

## 1. O Problema da Resolução Silenciosa pela IA

Em fluxos editoriais automatizados, é frequente que diferentes fontes de informação tragam versões divergentes sobre o mesmo fato:
- Um briefing recente de campanha afirma que o desconto de lançamento é de 25%;
- O documento de preços da marca registra 20%;
- Um post antigo publicado no blog menciona 30%.

Diante de discrepâncias como essa, modelos de linguagem sem governança tendem a cometer um erro crítico: **escolhem uma das fontes por probabilidade estatística ou fazem uma média, "resolvendo" o conflito em silêncio.** O resultado é a veiculação de informações imprecisas, promessas comerciais falsas e quebra de conformidade.

---

## 2. A Hierarquia de Precedência em 5 Níveis

Quando duas ou mais fontes divergirem, os agentes de IA e operadores do ecossistema `0 Mkt` devem aplicar compulsoriamente a seguinte ordem decrescente de autoridade:

```
┌────────────────────────────────────────────────────────────────────────┐
│  NÍVEL 1: Orientação Direta e Recente do Usuário (Decisão na Sessão)    │
├────────────────────────────────────────────────────────────────────────┤
│  NÍVEL 2: Registro Oficial Primário da Marca (_brands/<marca>/)        │
├────────────────────────────────────────────────────────────────────────┤
│  NÍVEL 3: Diretrizes Técnicas do Canal e Requisitos do Briefing        │
├────────────────────────────────────────────────────────────────────────┤
│  NÍVEL 4: Fontes Externas Primárias com Prova Documentada (Link/Data)   │
├────────────────────────────────────────────────────────────────────────┤
│  NÍVEL 5: Hipótese de Trabalho (Explicitamente Marcada [a confirmar])  │
└────────────────────────────────────────────────────────────────────────┘
```

### Detalhamento dos Níveis
1. **Nível 1 — Orientação Direta do Usuário:**  
   Instrução fornecida explicitamente pelo proprietário do projeto no chat ou sessão atual. Vence qualquer arquivo ou histórico prévio, pois reflete a decisão humana soberana em tempo real.
2. **Nível 2 — Registro Oficial Primário da Marca:**  
   Documentos validados da pasta `_brands/<marca>/` (`brand-voice.md`, `personas.md`, `content-pillars.md`, `glossario.md`, `depoimentos.md`) e acervos formais de dados e métricas (`acervo_dados_metricas.md` sob `brand-builder`).
3. **Nível 3 — Diretrizes Operacionais do Canal e Briefing da Demanda:**  
   Regras específicas pactuadas na pauta, sprint ou especificação da peça (tamanho de caracteres, formato de mídia, público-alvo imediato).
4. **Nível 4 — Fontes Externas Primárias com Prova:**  
   Bases oficiais de terceiros, relatórios de mercado, estatísticas governamentais ou documentações de plataformas auditadas com link direto, autoria e data de acesso documentadas.
5. **Nível 5 — Hipótese de Trabalho:**  
   Suposições ou premissas lógicas formuladas pela equipe que ainda não foram chanceladas; devem ser mantidas obrigatoriamente entre colchetes como `[a confirmar]`.

---

## 3. A Regra de Ouro: Proibição de Correção Silenciosa e Trava de Processo

1. **Trava Mandatória por Conflito:**  
   Se duas fontes de mesmo nível (ex.: dois documentos oficiais divergindo entre si) ou fontes de níveis adjacentes apresentarem dados materiais antagônicos (ex.: preços, datas, promessas de produto, métricas de resultado), **o processo trava imediatamente**.
2. **Proibição de Arbitragem Autônoma pela IA:**  
   O agente está estritamente proibido de:
   - Escolher um número sem avisar;
   - Fazer média aritmética ou interpolação;
   - Suavizar a divergência com generalizações vagas ("preço competitivo", "resultados rápidos").
3. **Protocolo de Alerta Transparente:**  
   O agente deve parar e emitir um relatório objetivo de conflito para o usuário:
   ```markdown
   ⚠️ CONFLITO FÁTICO DETECTADO — OPERAÇÃO PAUSADA
   - Afirmação em Conflito: [Tema, ex.: Preço do Plano Pro]
   - Fonte A (Nível X): [Caminho do arquivo ou citação com linha] -> Registra R$ 197/mês
   - Fonte B (Nível Y): [Caminho do arquivo ou citação com linha] -> Registra R$ 247/mês
   -> Ação Requerida: Usuário deve arbitrar qual valor prevalece antes de prosseguir.
   ```
4. **Governança de Correção (Artefato vs. Contexto):**  
   - Ao identificar uma divergência em peça já publicada ou em revisão, **corrige-se o artefato (a peça)** e não o contexto da marca, a menos que o usuário declare formalmente que a base da marca estava desatualizada.
   - Nenhuma base de marca é modificada em silêncio por dedução a partir de uma pauta isolada.

