# Política de Segurança — Super IA Projects - Marketing

A segurança de dados de campanhas, proteção contra vazamento de credenciais e integridade das rotinas de marketing são tratadas com máxima seriedade pela [Futuro Mercado](https://www.futuromercado.com.br).

---

## 🛡️ Versões Suportadas

Oferecemos suporte contínuo para a versão ativa na branch `main`:

| Versão | Suportada |
| :--- | :---: |
| `main` (v1.0.0+) | :white_check_mark: |

---

## 🚨 Como Reportar uma Vulnerabilidade ou Vazamento

Se você identificou uma falha de segurança, exposição acidental de credenciais ou brecha em algum dos scripts executáveis:

1. **NÃO crie uma Issue pública no GitHub.**
2. Envie um e-mail com os detalhes para:
   📧 **[felipe@futuromercado.com.br](mailto:felipe@futuromercado.com.br)**
   com o assunto: `[SEGURANÇA] Vulnerabilidade Super IA Projects - Marketing`.
3. Inclua no e-mail:
   - Descrição detalhada do incidente ou vulnerabilidade.
   - Passos para reproduzir o problema.
   - O impacto potencial nos dados ou ambiente do usuário.

### Prazo de Resposta
Confirmamos o recebimento em até **48 horas úteis** com plano de remediação.

---

## 🔒 Diretrizes para Usuários do Hub de Marketing

- **Zero Data Leaks:** Nunca versione dados reais de clientes, relatórios financeiros ou contas de anúncios. Mantenha as pastas `content/`, `clients/` e arquivos `.env*` rigorosamente isolados pelo `.gitignore`.
- **APIs de Mídia e Scraping:** Chaves da OpenAI, Anthropic, Google Gemini, Firecrawl ou Meta Ads devem permanecer exclusivamente no seu arquivo `.env` local.
