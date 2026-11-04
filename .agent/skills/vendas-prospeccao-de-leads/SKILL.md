---
# Repository: https://github.com/Felipelbahia/superiaprojects-marketing
# Status: Customizada / Modificada localmente por Felipe Bahia
name: vendas-prospeccao-de-leads
description: "Use para encontrar e preparar prospectos B2B antes do contato: achar decisores por cargo, porte e setor, montar lista de leads, enriquecer contatos (e-mail, telefone, tecnologia usada), conferir e-mails antes do envio e monitorar sinais de compra como rodada de investimento, vagas abertas e troca de tecnologia. Gatilhos: \"ache decisores\", \"lista de prospects\", \"pesquisa de leads\", \"enriquecer contatos\", \"sinais de compra\", \"quem está contratando\", \"Apollo\". NÃO use para escrever o e-mail frio ou a cadência (use vendas-cold-email), pontuar e rotear leads ou limpar o CRM (use vendas-crm), nem para qualificar um negócio com MEDDIC ou BANT (use vendas-pipeline)."
author: Antigravity Multi-IA Hub & Felipe Bahia (Futuro Mercado)
license: MIT
metadata:
  author: Antigravity Multi-IA Hub & Felipe Bahia (Futuro Mercado)
  version: 1.0.0
---
# Vendas: prospecção de leads

Guia para a etapa que vem **antes** do e-mail frio: descobrir quem abordar, com que dado e em que momento. Os três arquivos estavam dentro de `vendas-cold-email` (2026-10-20), cuja descrição trata de escrever e sequenciar mensagens e não mencionava busca de leads.

## Como escolher o caminho

| Situação | Abra |
|---|---|
| Quero montar uma lista do zero: fontes de leads, padrões de e-mail, enriquecimento, verificação, ferramentas e limites éticos | [lead-gen-scraper](references/lead-gen-scraper.md) |
| Tenho uma chave da API do Apollo.io e quero buscar decisores e enriquecer empresas por filtros (cargo, porte, setor, região, tecnologia) | [apollo-outreach](references/apollo-outreach.md) |
| Quero saber **quando** abordar: rodada de investimento, vagas abertas, troca de tecnologia, notícia da empresa | [buying-signals-monitoring](references/buying-signals-monitoring.md) |
| Já tenho a lista e o gancho e preciso escrever e-mail e follow-up | skill [vendas-cold-email](../vendas-cold-email/SKILL.md) |

## Passo a passo

1. **Defina o perfil de cliente ideal (ICP):** cargos, porte, setor, região e tecnologia. Se a marca tem personas em `_brands/<marca>/personas.md`, parta delas.
2. **Escolha a fonte.** Sem chave do Apollo, use o guia `lead-gen-scraper` (fontes públicas, diretórios, LinkedIn). Com chave, use `apollo-outreach`. O Apollo exige `APOLLO_API_KEY`; se não houver, avise o usuário e não invente contatos.
3. **Acrescente o momento.** Cruze a lista com sinais de compra para priorizar quem tem motivo para ouvir agora.
4. **Verifique antes de enviar.** Confira os e-mails com um verificador e respeite a seção de conformidade do `lead-gen-scraper`. Para LGPD, consulte [geral-conformidade-lgpd](../geral-conformidade-lgpd/SKILL.md).
5. **Entregue a lista com o gancho de cada grupo** e passe para a `vendas-cold-email` escrever a abordagem.

## Fronteiras

- Texto do e-mail, personalização, follow-up e infraestrutura de envio: [vendas-cold-email](../vendas-cold-email/SKILL.md).
- Pontuação de lead, temperatura, roteamento e higiene de dados: [vendas-crm](../vendas-crm/SKILL.md).
- Qualificação e previsão de negócios: [vendas-pipeline](../vendas-pipeline/SKILL.md).
- Para partir só do seu produto e sugerir empresas-alvo com estratégia de contato, há também o workflow `/vendas-prospeccao-de-leads`.
- Nunca entregue contato inventado. Dado que não veio de fonte ou ferramenta fica marcado como "não encontrado".

## Referências

| Arquivo | O que tem |
|---|---|
| [lead-gen-scraper.md](references/lead-gen-scraper.md) | Fontes de leads, padrões de e-mail, enriquecimento, montagem de lista, verificação, panorama de ferramentas, conformidade e modelos de abordagem. |
| [apollo-outreach.md](references/apollo-outreach.md) | Uso da API do Apollo.io: pré-requisito da chave, chamadas, processo de pesquisa de leads e formato do relatório. Requer `APOLLO_API_KEY`. |
| [buying-signals-monitoring.md](references/buying-signals-monitoring.md) | Sinais de compra (investimento, contratação, tecnologia, notícias), análise de sinais e playbook de abordagem por sinal. Material de terceiros (ClawFu, MIT); direito de uso confirmado pelo usuário. |

> Os guias vieram de kits em inglês e foram só movidos, sem revisão de texto.
