# Ciclo de Validação de Peças de Conteúdo e Governança de Aprendizado

Guia operacional para auditoria de conformidade, parecer estruturado de reprovação, releitura integral em ciclos de ajuste e registro de aprendizado de marca no hub `0 Mkt`.

> **Origem conceitual:** Princípios de validação pareada por canal, relatório estruturado de reprovação por trecho, releitura integral de v2 e governança de aprendizado com alcance adaptados livremente a partir da metodologia de `promovaweb/inboundfy`. Redação autoral e alinhada às diretrizes do hub `0 Mkt`.

---

## 1. O Princípio da Separação Produtora × Revisora

A integridade e o rigor da esteira de conteúdo dependem da separação estrita de responsabilidades entre os agentes que operam no ecossistema:

```
┌────────────────────────────────────────────────────────────────────────┐
│                   SEPARAÇÃO PRODUTORA × REVISORA                       │
│                                                                        │
│   1. Quem produz NÃO decide estratégia (obedece ao brief e às regras). │
│   2. Quem valida NÃO corrige a peça (emite parecer e devolve o texto). │
│   3. O revisor aponta o erro e exige a correção; a especialista        │
│      produtora executa o ajuste preservando a voz e o formato nativo.  │
└────────────────────────────────────────────────────────────────────────┘
```

- **Por que o revisor não reescreve a peça?** Quando o revisor tenta "consertar" o texto por conta própria, ele contorna as especialistas dedicadas (`copy-redacao-publicitaria`, `conteudo-criacao-multiformato`), atropela a esteira do `geral-anti-slop` e assume decisões estilísticas unilaterais que mascaram lacunas na fonte ou no processo.
- **Papel do revisor:** Emitir um parecer cirúrgico, objetivo e auditável, apontando a evidência, a regra violada e a ação necessária para que a especialista produtora corrija a entrega.

---

## 2. O Relatório de Reprovação em 5 Campos Oficiais

Quando uma peça de conteúdo não atinge a conformidade integral de voz, fatos, conformidade de canal ou diretrizes de marca, o revisor (ou o workflow `/conteudo-aprovacao`) emite obrigatoriamente a **Tabela de Reprovação de 5 Campos**:

| # | Coluna do Relatório | Definição Operacional | Exemplo Prático |
|---|---|---|---|
| 1 | **Localização** | Parágrafo, linha, slide ou seção exata onde o desvio ocorre. | `§ 2, linha 3` ou `Lâmina 4 (Corpo)` |
| 2 | **Trecho Auditado** | Citação literal do fragmento de texto ou elemento visual com problema. | *"Nossa solução revolucionária alavanca sinergias corporativas..."* |
| 3 | **Regra / Padrão Violado** | Documento normativo, cláusula ou seção da marca infringida. | `brand-voice.md: "O que NÃO comunicar" (Item 3: banir superlativos vazios)` + `padroes-pt-br.md (Cat. 3: Puffery)` |
| 4 | **Correção Verificável** | Instrução clara, objetiva e mensurável do que deve ser feito. | *"Eliminar 'revolucionária' e 'alavanca sinergias'; substituir pelo dado real de economia de tempo registrado no brief."* |
| 5 | **Destinatário da Devolução** | Agente especialista responsável por executar a correção. | `copy-redacao-publicitaria` (redação) ou `brand-estrategia` (se faltar dado no brief) |

### Cabeçalho Obrigatório do Parecer
```markdown
# Parecer de Revisão: [Nome da Peça ou Arquivo]

- **Marca:** [Nome da marca]
- **Canal & Formato:** [ex.: LinkedIn Post / Instagram Carrossel]
- **Versão Auditada:** [v1, v2, ...]
- **Revisor:** [Agente revisor, ex.: brand-guardiao-de-voz]
- **Veredito Geral:** [APROVADO | AJUSTES NECESSÁRIOS | REPROVADO]
- **Destinatário do Retorno:** [Especialista produtora correspondente]
```

---

## 3. Critérios Objetivos do Hard Gate de Aprovação

- **`APROVADO`:** Zero violações do `brand-voice.md`, zero infrações de "O que NÃO comunicar", 100% aderente ao anti-slop, dados com fontes verificáveis e especificações técnicas de canal atendidas. A peça segue para agendamento/publicação.
- **`AJUSTES NECESSÁRIOS`:** Presença de até 2 desvios cosméticos pontuais que não firam a tese, a reputação da marca nem o tom de voz central (ex.: ajuste de uma quebra de linha ou substituição de sinônimo secundário). Não exige novo ciclo formal se o operador validar a troca imediata.
- **`REPROVADO` (Hard Gate):** Qualquer uma das seguintes condições implica reprovação obrigatória:
  1. Uso de termos proibidos expressamente na seção "O que NÃO comunicar" da marca;
  2. Presença de jargões clichês de IA ou padrões condenados de slop;
  3. Menção a números, percentuais ou alegações de resultados sem fonte verificada;
  4. Reaproveitamento mecânico linear da mesma narrativa entre canais sem adaptação de formato;
  5. Imagem fora da proporção oficial do canal ou violando margens de segurança (`05a-moldes-de-canais.md`).

---

## 4. O Ciclo v1 → Reprovar → v2 com Releitura Integral

Quando uma peça é devolvida para ajuste, a especialista produtora gera uma nova versão identificada numericamente (ex.: `post-v1.md` -> `post-v2.md`), preservando o arquivo original sem sobrescrita.

Ao receber a versão corrigida (v2), o revisor é **estritamente proibido** de checar apenas a linha citada no relatório anterior. É mandatória a **releitura integral de ponta a ponta**.

### O Protocolo de Dois Passes na v2
1. **Passe 1 (Passe Literal de Verificação Pontual):**
   - O revisor inspeciona os pontos exatos listados na Tabela de Reprovação da v1;
   - Confere se a especialista produtora executou a correção verificável solicitada de forma satisfatória;
   - Registra o status de cada apontamento: `[RESOLVIDO]` ou `[PENDENTE]`.
2. **Passe 2 (Passe de Sentido e Integridade do Todo):**
   - O revisor relê a peça completa, do início ao fim;
   - Verifica se a alteração pontual gerou incoerência sintática com os parágrafos vizinhos, quebrou a fluidez da leitura, alterou involuntariamente a tese da peça ou introduziu um novo vício de escrita;
   - Garante que a peça corrigida como um todo permanece harmoniosa, coesa e 100% aderente à marca.

---

## 5. Validação de Imagem por Canal

Para peças visuais (estáticos, carrosséis, capas e miniaturas), a auditoria reaproveita as regras oficiais de `brand-builder/references/identidade-e-ativos/05a-moldes-de-canais.md`:

- **Dimensão e Proporção:** Verificar resolução e proporção exata da plataforma (ex.: Instagram Feed retrato `1080x1350` / 4:5; LinkedIn `1080x1080` ou `1200x627`; YouTube Thumbnail `3840x2160` / 16:9);
- **Zona Segura (Safe Zones):** Nenhum texto ou logo pode invadir margens reservadas para botões de interface nativa (coração, comentários, barra de progresso em Reels);
- **Consistência de Identidade:** Uso exclusivo da paleta de cores primária e secundária da marca em seus códigos hexadecimais aprovados, e tipografia condizente com o `style-guide.md`.

---

## 6. Governança de Aprendizado de Marca (`aprendizado.md`)

Feedbacks e correções do usuário durante os ciclos de validação são valiosos, mas representam um risco crítico de governança se forem generalizados sem critério. Uma observação como *"corta para 3 linhas neste post"* pode ser uma exigência pontual daquele criativo, e não uma proibição eterna de posts longos.

Todo feedback de ajuste deve ser registrado no arquivo `_brands/<marca>/aprendizado.md` segundo a matriz de **4 Alcances** e **4 Estados**:

### 6.1. Os 4 Níveis de Alcance (Escopo do Feedback)
1. **`peça`:** Aplica-se exclusivamente ao arquivo em edição (ex.: *"não cite o valor deste contrato nesta peça"*). Não se propaga para outras produções.
2. **`canal`:** Aplica-se a todas as peças daquele canal específico (ex.: *"no LinkedIn da marca, sempre usar quebra de linha dupla entre parágrafos"*).
3. **`persona`:** Aplica-se às mensagens direcionadas àquele segmento (ex.: *"para a Persona Dev, nunca use analogias de futebol"*).
4. **`projeto` / `marca`:** Aplica-se universalmente a toda e qualquer comunicação da marca (ex.: *"nunca usar a palavra 'revolucionário' em nenhum canal"*).

### 6.2. Os 4 Estados do Ciclo de Vida da Regra
1. **`proposta`:** Feedback anotado textualmente a partir de uma fala do usuário, mas ainda restrito à peça inicial ou pendente de validação em outros momentos.
2. **`confirmada`:** Regra chancelada formalmente pelo usuário após pergunta confirmatória explícita (ex.: *"Você quer que essa regra de 3 linhas valha para todos os posts de LinkedIn ou apenas para este?"* -> *"Para todos do LinkedIn"*).
3. **`aplicada`:** Regra promovida formalmente para o `brand-voice.md`, `content-pillars.md` ou `style-guide.md` da marca, passando a integrar as auditorias automáticas.
4. **`arquivada`:** Regra temporária que expirou, foi revogada pelo usuário ou substituída por nova diretriz.

```
┌────────────────────────────────────────────────────────────────────────┐
│                   REGRA DE PROMOÇÃO DE APRENDIZADO                     │
│                                                                        │
│   NENHUM feedback em estado 'proposta' altera o 'brand-voice.md'.      │
│   Apenas regras no estado 'confirmada' com alcance 'canal' ou          │
│   'projeto' são promovidas para a documentação permanente da marca.    │
└────────────────────────────────────────────────────────────────────────┘
```

