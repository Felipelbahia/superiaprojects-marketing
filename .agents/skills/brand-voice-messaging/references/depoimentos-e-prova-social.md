# Governança de Depoimentos e Prova Social com Consentimento por Canal

**Versão:** 1.0.0  
**Módulo:** `brand-voice-messaging`  
**Crédito de Origem:** Conceitos de prova social estruturada e consentimento granular adaptados a partir de `promovaweb/inboundfy` (licença AGPL-3.0), redigidos com estrutura e regras autorais exclusivas do ecossistema Super IA Projects `0 Mkt`.

---

## 1. Princípio da Autenticidade e Conformidade Jurídica

A prova social é um dos pilares mais persuasivos do marketing de conversão. No entanto, o uso amador ou desregulado de depoimentos acarreta graves riscos:
- **Risco Ético e Reputacional:** Citações embelezadas, resumidas de forma descontextualizada ou inventadas pela IA (slop) destroem a confiança da marca.
- **Risco Jurídico e Regulatório (LGPD / Defesa do Consumidor):** O cliente que autorizou um depoimento institucional no site não autorizou necessariamente o uso da sua foto e nome em campanhas pagas agressivas no Instagram ou em anúncios no Google.

O ecossistema `0 Mkt` exige que todo depoimento seja tratado como um **ativo de dados governado**, contendo aspas literais e uma **matriz de consentimento explícito por canal de distribuição**.

---

## 2. Estrutura Canônica do Registro de Depoimento

Cada registro de depoimento mantido em `_brands/<marca>/depoimentos.md` deve conter obrigatoriamente os seguintes campos:

```markdown
### [DEP-001] Nome do Autor — Empresa / Contexto
- **Identificador Único:** `DEP-001`
- **Autor:** Nome Completo
- **Cargo / Papel Real:** Função profissional exata no momento do relato
- **Organização / Empresa:** Nome da empresa ou instituição do autor
- **Segmento / Setor:** ex.: Fintech, SaaS B2B, Varejo, Consultoria
- **Tipo de Relação:** [Cliente Ativo | Ex-cliente | Aluno | Parceiro Estratégico]
- **Data do Registro:** AAAA-MM-DD
- **Origem / Evidência:** Link da gravação, transcrição de call, e-mail de feedback ou print autenticado
- **Retrato / Foto Oficial:** [URL da imagem aprovada ou "Sem retrato autorizado"]
- **Fala Literal (Aspas Exatas — ipsis litteris):**
  > "[Inserir o texto EXATO do cliente, sem correções gramaticais que alterem o sentido e sem adjetivações inseridas pela IA]"
- **Destaque Curto (Hook / Frase de Impacto):**
  "[1 frase extraída diretamente do relato para uso em chamadas]"

#### Matriz de Consentimento e Permissão por Canal
| Canal de Distribuição | Autorizado? | Condições Específicas / Restrições |
|---|:---:|---|
| **Website / Landing Page** | Sim | Permitido com foto e cargo completo na seção de depoimentos |
| **LinkedIn Orgânico** | Sim | Permitido citar o perfil @ do autor em post institucional |
| **Instagram / Redes Visuais** | Sim | Permitido em carrossel ou card estático |
| **Email Marketing / Newsletter** | Sim | Permitido em campanhas de nutrição e onboarding |
| **Mídia Paga (Meta / Google Ads)** | **NÃO** | **Proibido veicular em anúncios pagos patrocinados** |
| **Materiais de Vendas / Propostas (PDF)** | Sim | Permitido no deck institucional comercial |
```

---

## 3. Regras Mandatórias para Redatores e Agentes de IA

1. **Proibição Total de Fabriação ou Embelezamento:**  
   É terminantemente proibido inventar depoimentos ("persona fictícia elogiando o serviço") ou alterar as palavras do autor para deixá-lo "mais poético" ou "mais vendedor". O texto deve ser 100% literal.
2. **Respeito Estrito à Matriz de Canais:**  
   Antes de inserir um depoimento em uma copy de anúncio pago (`ads-copy-de-anuncio`), página (`copy-landing-page`) ou e-mail (`email-copy`), o agente deve consultar a matriz do depoimento. Se o canal estiver marcado como `NÃO`, a utilização é sumariamente bloqueada.
3. **Anonimização Protetiva:**  
   Se o autor solicitou anonimato ou se não houver consentimento para exibição pública de nome/foto, o depoimento só pode ser veiculado sob a forma anonimizada homologada (ex.: *"Diretor de Operações de uma empresa de logística com mais de 500 colaboradores"*), mantendo a fidelidade das métricas citadas.
4. **Validade e Revogação:**  
   Se um cliente revogar o consentimento ou rescindir o contrato com termo de descontinuidade, o status em `depoimentos.md` muda para `REVOGADO` e nenhuma nova peça pode utilizá-lo.

