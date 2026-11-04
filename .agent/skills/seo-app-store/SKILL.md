---
# Repository: https://github.com/Felipelbahia/superiaprojects-marketing
# Status: Customizada / Modificada localmente por Felipe Bahia
name: seo-app-store
description: "Especialista em App Store Optimization (ASO) para Apple App Store e Google Play Store. Abrange pesquisa de palavras-chave mobile, otimização de metadados visuais e textuais, Custom Product Pages (CPP), testes A/B de ícones e screenshots, conversão de downloads e gestão de avaliações. Use para: ranquear aplicativos nas buscas mobile, otimizar fichas de lojas, estruturar lançamentos de apps e maximizar taxas de instalação orgânica."
author: Antigravity Multi-IA Hub & Felipe Bahia (Futuro Mercado)
license: MIT
metadata:
  author: Antigravity Multi-IA Hub & Felipe Bahia (Futuro Mercado)
  version: 1.0.0
---
# App Store Optimization (ASO) Master

> Arquitetura técnica e estratégica para maximizar a visibilidade orgânica e as taxas de conversão de downloads na Apple App Store (iOS) e Google Play Store (Android).

---

## 🎯 1. Visão Geral & Heurísticas Fundamentais

O App Store Optimization (ASO) é a disciplina contínua de otimização de aplicativos para elevar o ranqueamento orgânico em buscas mobile e a taxa de conversão (CVR) da visualização da página para o download efetivo.

### As Duas Forças do ASO
```
ASO = Visibilidade Orgânica (Search + Browse) × Taxa de Conversão da Ficha (CVR)
```
1. **Visibilidade (Search & Browse/Explore):** Indexação semântica de palavras-chave, relevância algorítmica, presença em tops de categorias e destaques editoriais (Featuring).
2. **Conversão (Page CVR):** Impacto visual de ícones, screenshots persuasivos, vídeos de pré-visualização, clareza da proposta de valor nas primeiras 2 linhas e prova social (ratings & reviews).

---

## 📊 2. Comparativo de Algoritmos: iOS vs. Android

| Dimensão de Metadados | Apple App Store (iOS) | Google Play Store (Android) |
|---|---|---|
| **App Name / Title** | 30 caracteres (Peso algorítmico máximo) | 30 caracteres (Peso algorítmico máximo) |
| **Subtitle / Short Description** | 30 caracteres (Peso algorítmico muito alto) | 80 caracteres (Indexado e visível acima da dobra) |
| **Keyword Field Privado** | 100 caracteres separados por vírgula (Oculto) | Não existe campo oculto dedicado |
| **Long Description** | 4.000 caracteres (**NÃO indexada** para busca!) | 4.000 caracteres (**Altamente indexada**; densidade de 2% a 3%) |
| **Promotional Text** | 170 caracteres (Editável sem nova release) | Não possui campo equivalente direto |
| **Package Name / URL Slug** | Imutável (Definido pelo Apple ID) | `package_name` indexa keywords permanentemente! |
| **Visual First Impression** | Primeiros 3 screenshots em modo retrato | Primeiro screenshot ou vídeo landscape + cards |
| **Segmentação Personalizada** | Custom Product Pages (CPP, até 35 páginas) | Custom Store Listings (CSL, até 50 listagens) |

---

## 🔍 3. Estratégia de Pesquisa e Alocação de Keywords

### Heurística do Campo de Keywords da Apple (100 Chars)
1. **Regra de Ouro da Pontuação:** Separar termos apenas por vírgulas, sem espaços (`finanças,gestão,orçamento,contas`).
2. **Nunca Repetir:** Não repita termos já presentes no App Name ou Subtitle; a Apple combina automaticamente palavras cruzadas.
3. **Sem Plurais Redundantes:** O algoritmo da Apple normalmente reconhece variações singulares/plurais em inglês e espanhol (para o português, priorize a versão com maior volume de busca).
4. **Sem Nomes de Concorrentes Protegidos:** Marcas registradas de terceiros levam a rejeição na App Store Review.

### Matriz de Densidade para Google Play Store
- **Volume Ótimo de Menções:** 4 a 6 repetições da palavra-chave foco ao longo dos 4.000 caracteres da descrição longa.
- **Evitar Keyword Stuffing:** Densidade acima de 3,5% gera penalização algorítmica e rebaixamento de rank.
- **Posicionamento Estratégico:** Inclua as 3 keywords primárias no primeiro parágrafo (primeiras 150 palavras) e no último parágrafo de fechamento.

---

## 🎨 4. Otimização de Conversão Visual (Creative CRO)

Os elementos visuais são responsáveis por mais de 85% da decisão de instalação por impulso:

```
[ Ícone Atraente ] ──> [ 3 Primeiros Screenshots ] ──> [ Vídeo Demo ] ──> [ Nota 4.5+ ]
     (Clique na Busca)           (Compreensão Rápida)       (Engajamento)       (Confiança)
```

### Checklist de Criativos de Alta Conversão
- [ ] **Ícone:** Contraste marcante em fundos claro e escuro (Dark Mode). Elemento visual único e memorável; zero textos microscópicos ilegíveis.
- [ ] **Screenshot 1 (The Hook):** Deve responder à promessa principal do app em menos de 2 segundos com um benefício claro, não apenas um print de interface.
- [ ] **Screenshot 2 & 3 (Core Features):** Demonstração do produto em ação resolvendo os maiores pontos de atrito da persona.
- [ ] **Tipografia dos Banners:** Textos legíveis em telas pequenas (tamanho mínimo equivalente a 36pt), com copy direto e contrastante.
- [ ] **App Preview / Promo Video:** Primeiros 3 segundos dinâmicos com som mudo compreensível (legendas integradas), demonstrando a UI real sem enrolação institucional.

---

## 🎯 5. Sinergia Apple Search Ads (ASA) & ASO Orgânico

A busca paga em lojas mobile retroalimenta diretamente o ranqueamento orgânico:

| Tática de Sinergia ASA $\rightarrow$ ASO | Impacto Esperado | Mecanismo Algorítmico |
|---|---|---|
| **Keyword Discovery via Search Match** | Identificação de novos termos de cauda longa com alta intenção | Termos convertidos em ASA são promovidos para o Title e Keyword Field orgânico. |
| **Download Velocity Acceleration** | Subida rápida no Top Charts de categoria | O algoritmo da Apple prioriza apps com alto volume de instalações recentes por hora. |
| **Alinhamento com Custom Product Pages (CPP)** | Aumento de CVR em até 40% | Anúncios de ASA apontam para CPP com o mesmo screenshot e copy da busca, mantendo coerência visual. |
| **Defesa de Marca (Brand Defense)** | Blindagem contra canibalização de concorrentes | Garante que o tráfego que busca sua marca não seja desviado no topo da SERP da loja. |

---

## 🎪 6. In-App Events (IAE) & Promotional Content

Eventos ao vivo e conteúdos promocionais ocupam cards gigantes nos resultados de busca:

- **Apple In-App Events (IAE):** Cards dedicados de até 30 dias de duração (desafios, lançamentos de temporada, eventos ao vivo). Aparecem nos resultados de busca tanto para usuários novos quanto para quem já tem o app instalado.
- **Google Play Promotional Content (LiveOps):** Banners na aba inicial e na página de detalhes. Apps que utilizam Promotional Content ativamente recebem 2,5x mais chances de destaque editorial (*Featuring*).

---

## 🚀 7. Framework de Testes A/B & Iteração Contínua

Nunca faça alterações de ASO sem medição estatística controlada:

| Ferramenta / Plataforma | Tipo de Teste Recomendado | Métrica de Decisão | Tempo Mínimo de Teste |
|---|---|---|:---:|
| **App Store Connect PPO** | Product Page Optimization (Ícones, Screenshots) | Conversion Rate (Installs / Impressions) | 7 a 14 dias (min. 500 conversões) |
| **Google Play Experiments** | Fichas de teste (Ícone, Descrição, Screenshots) | Retained Installers (D1/D7 Retention) | 14 dias (para cobrir ciclos semanais) |
| **Custom Product Pages (CPP)** | Segmentação por anúncio de Apple Search Ads (ASA) | ROAS & CVR por grupo de palavras-chave | Contínuo |

---

## ⭐ 8. Gestão de Reputação: Ratings & Reviews

A nota média é um fator eliminatório de ranqueamento e de conversão:
- **Barreira Mínima Crítica:** Apps com nota abaixo de 4.0 sofrem perda média de 50% na conversão orgânica; notas abaixo de 3.5 perdem quase 80%.
- **In-App Review Prompt:** Disparar o prompt nativo (`SKStoreReviewController` no iOS) **apenas** no momento de maior satisfação do usuário (ex: após concluir uma tarefa com sucesso ou atingir um marco positivo), NUNCA no primeiro acesso ou no meio de um fluxo crítico.
- **SLA de Resposta de Reviews:** Responder a 100% das avaliações de 1 e 2 estrelas em menos de 48 horas com tom empático, citando que o time técnico investigou e oferecendo canal direto de suporte.

---

## 📈 9. KPIs e Fórmulas de Acompanhamento de ASO

```
1. Organic Multiplier = (Downloads Orgânicos Totais) / (Downloads Pagos de Campanhas)
   → Benchmark saudável: 1.3 a 2.0 (para cada 100 installs pagos, 30 a 100 orgânicos adicionais)

2. Search Impression Share = (Impressões Obtidas nas Keywords Alvo) / (Total de Buscas Estimadas)

3. Page Conversion Rate (CVR) = (Instalações Únicas) / (Visualizações de Página da Ficha)
   → Benchmark: 25% a 35% na App Store; 20% a 30% na Google Play
```

---

## 📚 10. Acervo de Referências Catalogadas

A tabela abaixo lista os guias integrados disponíveis para aprofundamento operacional:

| Arquivo de Referência | Escopo Técnico |
|---|---|
| [`references/original-guide.md`](references/original-guide.md) | Guia completo original de estratégias de indexação de keywords mobile, metadados e ASO. |

---

## 📋 11. Checklist de Auditoria Rápida de ASO

- [ ] O App Name contém o nome da marca + a principal keyword funcional com alto volume de busca?
- [ ] O Subtitle / Short Description complementa sem repetir palavras do título?
- [ ] O campo de keywords do iOS utiliza todas as 100 posições sem espaços extras?
- [ ] A descrição longa do Google Play contém os termos sem ultrapassar 3% de densidade?
- [ ] Os 3 primeiros screenshots mostram a dor principal resolvida com títulos de fácil leitura?
- [ ] A nota média consolidada está acima de 4.3 estrelas nas duas lojas?
- [ ] As Custom Product Pages estão alinhadas com as campanhas de tráfego pago ativo?
- [ ] Há In-App Events ativos programados para os próximos 30 dias?
