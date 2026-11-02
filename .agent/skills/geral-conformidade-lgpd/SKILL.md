---
name: geral-conformidade-lgpd
description: "Use para conformidade de marketing digital: LGPD e GDPR, consentimento (Consent Mode v2), formulários de captura, revisão de contratos, NDAs de influenciadores e análise de termos de uso. É triagem para orientar o trabalho de marketing; a decisão jurídica final é de advogado. Gatilhos: \"LGPD\", \"GDPR\", \"consentimento\", \"política de privacidade\", \"NDA\", \"contrato de influenciador\". NÃO use para implementar tags e eventos de rastreamento (use data-web-ga4) nem para regras de e-mail e entregabilidade (use email-entregabilidade)."
license: MIT
metadata:
  author: Antigravity Multi-IA Hub & Felipe Bahia (Futuro Mercado)
  version: 1.0.0
---

# Marketing Compliance, LGPD & GDPR (Antigravity Kit)

> Guia mestre de governança, conformidade regulatória e proteção de dados para operações de tráfego, captura de leads, automação de e-mail e parcerias comerciais no Hub `0 Mkt`.

---

## 1. Visão Geral & Escopo

No ecossistema de marketing digital moderno, o compliance jurídico deixou de ser um obstáculo burocrático para se tornar um diferencial competitivo de confiança, reputação de marca e sustentabilidade técnica. Bloqueios de contas no Meta Ads, penalizações de entregabilidade no Google Workspace/Yahoo e multas sob a **LGPD (Brasil - Lei 13.709/2018)** e o **GDPR (União Europeia - Regulamento 2016/679)** decorrem quase sempre de falhas em pontos de captura e rastreamento.

Esta skill padroniza os protocolos de privacidade e segurança jurídica para:
1. **Consentimento de Cookies & Rastreamento**: Implementação de Consent Mode v2 (Google Ads, GA4) e Meta Pixel.
2. **Captação de Leads & Páginas de Conversão**: Formulários com consentimento granular (unbundled), opt-in duplo e termos de lead magnets.
3. **Comunicações Comerciais & E-mail**: Higienização de bases, opt-out em 1 clique e fundamentação legal (Consentimento vs. Legítimo Interesse).
4. **Contratos & NDAs para Parceiros**: Sigilo pré-lançamento, direitos de imagem e acordos com creators/influenciadores.
5. **Auditoria de Martech & SaaS**: Análise de Termos de Serviço (ToS) e Acordos de Processamento de Dados (DPA).

---

## 2. Bases Legais Aplicadas ao Funil de Marketing

| Etapa do Funil | Atividade de Marketing | Base Legal Típica (LGPD / GDPR) | Requisito Operacional Mandatório |
|---|---|---|---|
| **Topo (Atração)** | Rastreamento por cookies/pixels | Consentimento Explícito (Opt-in) | Banner com recusa tão fácil quanto o aceite; Consent Mode v2 ativo |
| **Meio (Captura)** | Download de Ebook / Inscrição em Webinar | Execução de Contrato / Consentimento | Caixa de aceite desmarcada; link visível para Política de Privacidade |
| **Nutrição (E-mail)** | Envio de newsletters e réguas relacionais | Consentimento / Legítimo Interesse | Link de cancelamento funcional (`Unsubscribe-One-Click`) em todo envio |
| **Fundo (Vendas)** | Prospecção B2B (Cold Outreach Outbound) | Legítimo Interesse (LIA documentado) | Oferta estritamente aderente ao cargo; opção de opt-out imediato |
| **Pós-Venda** | Pesquisa de satisfação (NPS) e upsell | Execução de Contrato / Legítimo Interesse | Comunicação direcionada ao serviço contratado |

---

## 3. Diretrizes de Consent Mode v2 & Rastreamento Web

### 3.1. Os 4 Parâmetros Mandatórios do Google Consent Mode v2
Para preservar a atribuição de conversões e audiências de remarketing no Google Ads e GA4 no EEE e globalmente:
- `ad_storage`: Habilita armazenamento (cookies) para publicidade.
- `analytics_storage`: Habilita armazenamento para métricas de uso do site.
- `ad_user_data`: Autoriza explicitamente o envio de dados do usuário ao Google para publicidade online.
- `ad_personalization`: Controla se o remarketing pode ser habilitado.

### 3.2. Heurística Anti-Bloqueio de Banner de Cookies
- **Proibição de Dark Patterns**: O botão "Rejeitar Todos" deve ter o mesmo peso visual (tamanho, contraste e hierarquia) que "Aceitar Todos".
- **Default State**: Todas as tags não essenciais devem iniciar bloqueadas (`default: denied`) até que o usuário clique em aceitar.
- **Registro do Consentimento**: Salvar timestamp, IP mascarado, versão do termo aceito e categorias autorizadas no LocalStorage ou backend.

---

## 4. Formulários de Captura & Lead Magnets

Todo formulário de landing page ou pop-up deve aderir às seguintes heurísticas de transparência:

```markdown
[ Formulário de Captura ]
Nome: [________________________]
E-mail Corporativo: [__________]

[ ] Quero receber o relatório e concordo em receber comunicações semanais 
    com novidades de mercado da [Marca]. (Opcional se o material for entregue 
    sem necessidade de opt-in adicional).
    
Ao clicar em "Baixar Agora", você declara ter lido e concordado com nossa 
[Política de Privacidade](link) e [Termos de Uso](link).
```

### Regras de Ouro:
1. **Nunca use caixas pré-marcadas (Pre-ticked checkboxes)**: Sob a LGPD e GDPR, o silêncio ou inação não configuram consentimento.
2. **Consentimento Desmembrado (Unbundled)**: A permissão para receber ligações de SDR não pode ser imposta como condição obrigatória para baixar um PDF educativo, a menos que claramente explicitado como material restrito a demonstrações comerciais.
3. **Política de Privacidade Acessível**: O link da política deve estar a 1 clique do botão de submissão do formulário.

---

## 5. Diretrizes de E-mail Marketing & Anti-Spam

### 5.1. Protocolo de Opt-Out e Higiene
- Todo e-mail enviado deve conter no rodapé:
  1. Identificação clara da entidade remetente (Razão Social, CNPJ ou endereço físico).
  2. Motivo pelo qual o destinatário recebeu o contato ("Você recebeu este e-mail porque se cadastrou em...").
  3. Link direto de descadastro em 1 clique (sem exigir login, senha ou preenchimento de questionários longos).
- Processamento de cancelamento: Deve ser instantâneo e não exceder 24 horas úteis.

### 5.2. Prospecção B2B (Cold Outreach) sob Legítimo Interesse
- Não disparar para e-mails pessoais (`@gmail.com`, `@hotmail.com`); utilizar exclusivamente endereços profissionais corporativos.
- Personalização estrita: A mensagem deve demonstrar pertinência imediata com o cargo do decisor.
- Fornecer saída honrosa: A primeira linha do rodapé deve oferecer "Se não tiver interesse em temas de [Área], basta responder 'remover' que não entrarei mais em contato".

---

## 6. Acordos de Confidencialidade (NDAs) & Parcerias com Creators

Antes de compartilhar briefings confidenciais, artes de rebranding, produtos ainda não lançados ou métricas financeiras com terceiros, formalize o instrumento adequado:

| Cenário de Parceria | Tipo de Acordo Recomendado | Cláusulas Críticas a Observar |
|---|---|---|
| **Contratação de Influenciador / Creator** | Contrato de Prestação com NDA Anexo | Exclusividade de nicho, período de embargo de postagem, titularidade de direitos autorais da copy/mídia |
| **Contratação de Agência / Freelancer de Tráfego** | NDA Mútuo + DPA (Proteção de Dados) | Proibição de uso de listas de clientes para campanhas de terceiros; obrigação de deleção pós-contrato |
| **Co-marketing / Parceria de Lançamento** | Acordo de Parceria Operacional | Regras de compartilhamento de base de leads (co-branding); divisão de responsabilidades LGPD |
| **Apresentação a Investidores / M&A** | NDA Unilateral Estrito | Definição restrita de "Informações Confidenciais", prazo de 2 a 5 anos, fórum de resolução |

Consulte o gerador contextual de termos em `references/nda-generator.md` para minutas balanceadas.

---

## 7. Análise de Termos de Uso (ToS) de Ferramentas de IA e Martech

Ao contratar ou plugar novas plataformas de automação, web scraping ou inteligência artificial no stack de marketing:
- **Treinamento de Modelos**: Verifique se a plataforma reserva o direito de treinar LLMs públicos com os prompts, dados de clientes ou briefings submetidos (cláusula "Data Improvement / AI Training").
- **Propriedade Intelectual (IP)**: Garanta que o output gerado pertença 100% à sua empresa e que a ferramenta forneça indenização por infração de terceiros.
- **Localização dos Servidores**: Avalie se a ferramenta transfere dados transfronteiriços sem salvaguardas adequadas (cláusulas padrão contratuais).

Utilize o analisador de risco em `references/terms-analyzer.md` para decodificar contratos complexos de fornecedores de software.

---

## 8. Checklist de Pré-Lançamento de Campanha (Compliance Gate)

Antes de aprovar qualquer landing page, anúncio ou régua de e-mails para veiculação pública, execute o checklist:

- [ ] **Banner de Consentimento**: O Consent Mode v2 está disparando os estados `granted`/`denied` corretamente no Tag Manager?
- [ ] **Formulários de Captura**: As caixas de aceite estão desmarcadas por padrão e o link da política de privacidade está ativo?
- [ ] **Rodapé de E-mail**: O endereço comercial e o link de descadastro imediato constam no template de todos os disparos?
- [ ] **Tráfego Pago**: Os termos do anúncio evitam promessas milagrosas ou afirmações enganosas vedadas pelo Código de Defesa do Consumidor (CDC) e políticas do Google/Meta?
- [ ] **Direitos de Imagem**: Todo material de creators ou modelos possui autorização formal de uso comercial assinada?
- [ ] **Contratos de Ferramentas**: As ferramentas integradas para captura possuem DPA assinado e protegem os dados dos leads?

---

## 9. Acervo de Referências & Documentos Complementares

Para detalhamentos operacionais e minutas contratuais completas, consulte o diretório local `references/`:
- [gdpr-compliance.md](references/gdpr-compliance.md) — Manual aprofundado de requisitos GDPR/LGPD para consentimento, direitos de titulares e registros de processamento.
- [terms-analyzer.md](references/terms-analyzer.md) — Metodologia de auditoria de termos de serviço de plataformas SaaS e martechs.
- [nda-generator.md](references/nda-generator.md) — Framework de geração e balanceamento de acordos de confidencialidade comercial.
- [contract-review.md](references/contract-review.md) — Revisão sistemática de contratos: sinais de risco, cláusulas desfavoráveis e pontos de negociação.

## Referências vindas de outras skills

- **[contract-review.md](references/contract-review.md)** — Checklist de análise de termos de serviço, SLA, multas e cláusulas rescisórias.
