> [!NOTE]
> **[EXEMPLO RESOLVIDO ILUSTRATIVO — USO COMO REFERÊNCIA DE PROCESSO]**
> Este documento integra o pacote de referências do Item 2042 da inbox. Estrutura de campos, ordem e cabeçalhos canônicos baseados na suíte de validação do `promovaweb/inboundfy` (com adaptação 100% original em PT-BR para o ecossistema Multi-IA do `0 Mkt`).

# Modelo Canônico de Relatório de Validação (Reprovação e Aprovação)

Este documento define o gabarito estrutural obrigatório para laudos de validação em dois passes (literal e de sentido) emitidos pelo validador de conteúdo (`geral-anti-slop` ou agente revisor).

---

## Bloco A: Exemplo de Relatório de Reprovação (Rodada 1)

```markdown
# Relatório de Validação de Conteúdo — Rodada 1

### Cabeçalho de Controle
- **Ativo Analisado:** Post LinkedIn — "Fim de Mês no Consultório e o Fantasma das Glosas"
- **Briefing de Origem:** `content/lumina/briefs/2026-02-01-linkedin-glosas.md`
- **Agente Produtor:** `@conteudo-criacao-multiformato`
- **Agente Validador / Revisor:** `@brand-guardiao-de-voz` (com skill `geral-anti-slop`)
- **Data da Avaliação:** 2026-02-02
- **Veredito Geral:** ❌ **REPROVADO**
- **Ocorrências Remanescentes:** 6 violações detectadas

### Fontes Carregadas e Confrontadas
- [x] `_brands/lumina/brand-voice.md` (Tom de voz e lista de vetos — LIDO)
- [x] `_brands/lumina/glossario.md` (Terminologia TISS e termos em inglês — LIDO)
- [x] Briefing da Demanda (Critérios contáveis e CTA único — LIDO)

---

### Tabela 1: Hard Gate por Categoria (Passe Literal x Passe Semântico)

| Categoria de Checagem | Passe Literal | Passe Semântico | Ocorrências | Status |
|---|---|---|---|---|
| **1. Lista de Vetos (Slop Clichês)** | ❌ FALHOU | — | 3 termos proibidos identificados | REPROVADO |
| **2. Estrutura de Abertura e Fecho** | — | ❌ FALHOU | Abertura professoral genérica e fecho circular | REPROVADO |
| **3. Proibições da Marca (O que NÃO comunicar)** | ❌ FALHOU | — | Prometeu "lucro multiplicado" sem amparo | REPROVADO |
| **4. Fatos, Números e Fontes** | — | ❌ FALHOU | Estatística de 40% citada sem fonte verificável | REPROVADO |
| **5. Termos Técnicos e Grafia** | ❌ FALHOU | — | Grafou "Lumina" sem acento e aportuguesou *dashboard* | REPROVADO |
| **6. CTA Único do Brief** | ✅ PASSOU | ✅ PASSOU | Respeitou chamada única para ler o guia | APROVADO |

---

### Tabela 2: Matriz de Achados Detalhados

| ID | Localização | Evidência (Trecho Exato) | Regra / Fonte Violada | Diagnóstico Técnico | Correção Verificável Exigida |
|---|---|---|---|---|---|
| **#01** | § 1, Linha 2 | *"No cenário atual da medicina..."* | `brand-voice.md`, Seção 3 (Blacklist) | Muleta introdutória clássica de modelo de linguagem. | Deletar a frase genérica e abrir diretamente com a situação real do consultório. |
| **#02** | § 2, Linha 4 | *"uma solução robusta e revolucionária"* | `brand-voice.md`, Seção 3 (Blacklist) | Adjetivos vazios proibidos pela marca. | Substituir por mecanismo técnico concreto (ex: conciliação automática via XML). |
| **#03** | § 2, Linha 6 | *"multiplicar o faturamento líquido da sua clínica"* | `brand-voice.md`, Seção "O que NÃO comunicar" | Promessa de lucro milagroso vedada na marca. | Reformular para foco em redução de perdas por glosas não recuperadas. |
| **#04** | § 3, Linha 1 | *"Mais de 40% dos médicos perdem repasses"* | AGENTS.md, Regra de Fatos Verificáveis | Dado numérico sem fonte atribuída na peça. | Inserir a fonte real ou remover o número, descrevendo o problema sem dado inventado. |
| **#05** | § 3, Linha 3 | *"painel de controle Lumina"* | `glossario.md` da marca fictícia | Grafia errada da marca e tradução indevida de termo técnico. | Corrigir para "*dashboard* da Lúmina Gestão" (com itálico e acento). |
| **#06** | § 4, Linha 2 | *"Portanto, desvendar novas ferramentas é crucial."* | `geral-anti-slop`, Padrões 01 e 04 | Tríplice clichê de IA ("portanto", "desvendar", "crucial"). | Reescrever em português direto sem conectivos artificiais. |

---

### Encaminhamento e Próximo Passo
- **Destino da Devolução:** Retorna ao agente produtor `@conteudo-criacao-multiformato`.
- **Instrução Obrigatória:**
  1. Corrigir individualmente as 6 ocorrências tabuladas acima.
  2. Varrer a peça inteira procurando ocorrências adicionais dos mesmos padrões (não apenas substituir sinônimos nos trechos apontados).
  3. Reenviar o artefato completo acompanhado de nota das alterações para a Rodada 2 de validação.
```

---

## Bloco B: Exemplo de Relatório de Aprovação (Rodada 2)

```markdown
# Relatório de Validação de Conteúdo — Rodada 2 (Final)

### Cabeçalho de Controle
- **Ativo Analisado:** Post LinkedIn — "Fim de Mês no Consultório e o Fantasma das Glosas" (Versão Revisada)
- **Briefing de Origem:** `content/lumina/briefs/2026-02-01-linkedin-glosas.md`
- **Agente Produtor:** `@conteudo-criacao-multiformato`
- **Agente Validador / Revisor:** `@brand-guardiao-de-voz` (com skill `geral-anti-slop`)
- **Data da Avaliação:** 2026-02-02
- **Veredito Geral:** ✅ **APROVADO**
- **Ocorrências Remanescentes:** **ZERO (0)**

---

### Tabela 1: Hard Gate por Categoria — Conferência de Reenvio

| Categoria de Checagem | Status Rodada 1 | Reavaliação Rodada 2 | Ocorrências Atuais | Veredito |
|---|---|---|---|---|
| **1. Lista de Vetos (Slop Clichês)** | ❌ FALHOU | ✅ PASSOU | Zero termos proibidos | APROVADO |
| **2. Estrutura de Abertura e Fecho** | ❌ FALHOU | ✅ PASSOU | Abertura por cena concreta; fecho limpo | APROVADO |
| **3. Proibições da Marca** | ❌ FALHOU | ✅ PASSOU | Foco restrito a tempo e glosas | APROVADO |
| **4. Fatos, Números e Fontes** | ❌ FALHOU | ✅ PASSOU | Dado removido; relato ancorado em processo | APROVADO |
| **5. Termos Técnicos e Grafia** | ❌ FALHOU | ✅ PASSOU | *dashboard* em itálico e Lúmina com acento | APROVADO |
| **6. CTA Único do Brief** | ✅ PASSOU | ✅ PASSOU | Mantido CTA oficial aprovado | APROVADO |

---

### Tabela 2: Conferência Positiva dos Achados Anteriores

- [x] **Achado #01 Sanado:** Abertura genérica removida. A peça agora inicia com: *"Sábado, 17h30. Consultório vazio, mas a mesa da recepção ainda tem 40 guias pendentes..."*.
- [x] **Achado #02 Sanado:** Clichês "robusta e revolucionária" substituídos por descrição funcional: *"cruzamento automático das guias TISS com o extrato bancário"*.
- [x] **Achado #03 Sanado:** Promessa exagerada de lucro removida; mantido o benefício de previsibilidade de caixa.
- [x] **Achado #04 Sanado:** Dado sem fonte retirado; substituído pelo relato do processo de conciliação.
- [x] **Achado #05 Sanado:** Grafia corrigida para "*dashboard* da Lúmina Gestão".
- [x] **Achado #06 Sanado:** "Portanto/desvendar/crucial" eliminados; conclusão em tom sóbrio e profissional.

---

### Liberação e Próximo Passo
- **Status do Artefato:** Liberado para agendamento e publicação no canal LinkedIn Oficial da Lúmina Gestão.
- **Encaminhamento:** Nenhum reparo pendente. Salvar versão final no destino do mapa (`content/lumina/linkedin/2026-02-02 - Glosas de Convenio/copy-final.md`).
```
