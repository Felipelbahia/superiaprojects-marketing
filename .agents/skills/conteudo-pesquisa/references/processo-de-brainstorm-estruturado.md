# Processo de Brainstorm Estruturado com Portões de Qualidade

**Versão:** 1.0.0  
**Módulo:** `conteudo-pesquisa` / `conteudo-brainstorm`  
**Crédito de Origem:** Conceitos de processo de ideação com portões e artefatos de tese adaptados a partir de `promovaweb/inboundfy` (licença AGPL-3.0), redigidos com estrutura e regras autorais exclusivas do ecossistema Super IA Projects `0 Mkt`.

---

## 1. Visão Geral e Objetivo

O brainstorm no ecossistema `0 Mkt` não é uma conversa informal sem desfecho: é um **processo governado de 5 portões operacionais** que transforma uma faísca ou ideia bruta em um **artefato validado (`brainstorm.md`)**.

Nenhuma esteira de produção deve iniciar a redação de copy ou roteiro a partir de premissas vagas. O artefato gerado neste processo define a tese inegociável, o recorte de público, as fontes primárias verificadas e as suposições críticas de trabalho.

---

## 2. O Ciclo dos 5 Portões de Ideação

```
[ 1. Triagem & Intenção ] ──> [ 2. Entrevista Mínima ] ──> [ 3. Pesquisa Datada ] ──> [ 4. Síntese Estruturada ] ──> [ 5. Validação ]
                                       │                                                       │                           │
                                (se autossuficiente)                                           │                     (se reprovar)
                                       └───────────────────────────────►                       │                           │
                                                                                               └───────────────(devolução cirúrgica)
```

### Portão 1: Triagem & Intenção Editorial
1. **Preservação Literal da Ideia Original:**  
   O agente deve transcrever a ideia do usuário *ipsis litteris* no topo do artefato, sem filtros ou julgamentos prematuros.
2. **Leitura de Intenção e Formato:**  
   Identificar o objetivo principal (educar, gerar leads, rebater objeção, posicionamento de marca) e o formato prioritário inicial.

### Portão 2: Entrevista Mínima (Filtro de Corte)
1. **Critério de Corte Estrito:**  
   Só formular perguntas ao usuário cuja resposta altere diretamente:
   - A **tese central** defendida;
   - O **recorte de audiência** ou persona;
   - A **veracidade ou viabilidade** fática da proposta.
2. **Regra de Pular a Entrevista:**  
   Se o prompt do usuário ou o briefing fornecido já contiver premissas claras e fontes suficientes, o Portão 2 é compulsoriamente pulado, avançando direto para a pesquisa.

### Portão 3: Pesquisa & Ancoragem Fática Datada
1. **Fontes Externas com Prova:**  
   Levantar no mínimo 2 a 3 fontes críveis (relatórios setoriais, dados oficiais, documentações ou casos reais).
2. **Registro de Rastreabilidade:**  
   Toda fonte citada deve registrar obrigatoriamente a **URL exata** e a **data de acesso** (AAAA-MM-DD), aplicando a ordem de precedência em 5 níveis (orientação do usuário > base da marca > briefing > fontes com prova > hipótese).

### Portão 4: Síntese Estruturada
Neste portão o agente consolida a inteligência no modelo vivo:
1. **A Tríade Editorial:**
   - **Tese:** A afirmação central ou ponto de vista afiado defendido pela peça;
   - **Recorte Específico:** O ângulo exato pelo qual o tema será abordado (o que entra);
   - **Limites de Escopo:** O que fica categoricamente de fora da peça para evitar dispersão.
2. **Tabela de Fatos vs. Hipóteses:**  
   Separação visual entre dados empíricos comprovados e premissas dedutivas que exigem teste.
3. **Matriz de Suposições de Trabalho:**  
   Tabela contendo: `[Suposição | Como Confirmar | Impacto se Errada (Alto/Médio/Baixo)]`.
4. **Mapeamento de Objeções:** As 2-3 resistências mais prováveis do leitor e como contra-argumentar.
5. **Oportunidades de Multiplicação:** Desdobramentos naturais para outros canais (LinkedIn, Blog, Vídeo Curto, E-mail).

### Portão 5: Validação e Regra de Devolução Cirúrgica
1. **Chancela Formal de Aprovação:**  
   O arquivo só transita para `estado: aprovado` quando a tese for clara, as fontes estiverem datadas e as suposições críticas tiverem plano de checagem.
2. **Regra de Devolução Cirúrgica:**  
   Se o revisor ou o usuário reprovar o artefato, o fluxo **não recomeça do zero**:
   - Falha de tese ampla demais → Devolve ao **Portão 4**;
   - Falha de fonte duvidosa ou dado fraco → Devolve ao **Portão 3**;
   - Dúvida sobre público ou premissa de negócio → Devolve ao **Portão 2**.  
   Todo o material válido dos demais portões é preservado intacto.

---

## 3. Destino do Artefato Aprovado

O arquivo `brainstorm.md` gerado deve ser salvo obrigatoriamente na pasta da demanda no mapa de destinos (`docs/mapa-de-destinos.md`), ex.:  
`content/<marca>/<tipo>/AAAA-MM-DD - Nome da Demanda/brainstorm.md`  
(ou em `content/<marca>/estrategia/` quando se tratar de ideação de campanha guarda-chuva).

