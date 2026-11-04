# Brandbook e gestão de ativos

Apoio à etapa 9 do `brand-builder`. Duas coisas que o fluxo precisava e não tinha: **como escolher o tamanho do brandbook** (escopos e perguntas) e **como inventariar, organizar e governar os ativos da marca** (logos, cores, fontes, imagens). Este arquivo diz *como conduzir*; o conteúdo visual detalhado (uso do logo, cor com especificação de impressão, tipografia, imagem, aplicações) mora em `references/identidade-e-ativos/`.

**Origem (copiado e reescrito em português no E5, 2026-10-20; direito de uso confirmado pelo usuário):** comandos `/brand:book` e `/brand:assets` do AgentKits Marketing, que continuam em `revenue-gtm-e-posicionamento/references/book.md` e `assets.md`. Aqui foram adaptados ao fluxo do `brand-builder`: sem perguntas interativas do AgentKits, sem delegação a agentes por comando e com os arquivos de saída no lugar certo (`_brands/<marca>/`).

## Sumário
1. O brandbook do 0 Mkt é um índice
2. Um brandbook só, em qualquer profundidade
3. Perguntas de configuração
4. O que entra em cada escopo, arquivo por arquivo
5. Validação antes de entregar
6. Gestão de ativos: inventariar, organizar, auditar, governar
7. Modelos de saída
8. Quem ajuda em cada tarefa
9. Onde salvar
10. Navegação, versões e lacunas (HTML gêmeo, `versoes.json`, seção de lacunas)

## 1. O brandbook do 0 Mkt é um índice
O `brandbook.md` **referencia** os arquivos das etapas e não copia o texto deles (regra da etapa 9 do `catalog.md`). Então "gerar o brandbook" aqui significa: escolher o escopo, conferir que cada arquivo exigido existe e está aprovado, linkar tudo, registrar `Known Gaps` e as decisões em aberto. O brandbook também lista **quais arquivos da marca uma IA ou um agente deve ler** (para quem consome a marca; ver o contrato na etapa 9).

## 2. Um brandbook só, em qualquer profundidade `[usuário, 2026-10-27]`
**Os materiais são os mesmos em todos os modos.** Não existe mais "Básico, Recomendado ou Completo" como corte de conteúdo: o brandbook e os arquivos das etapas têm sempre a estrutura completa (seção 4). O que muda com a profundidade é a **quantidade de perguntas, de referências e de exemplos**, não a lista de entregáveis.
| Profundidade | O que muda | O que NÃO muda |
|---|---|---|
| **Curta** | Poucas perguntas por etapa, poucas referências, um exemplo por regra; o modelo propõe quando o usuário prefere (tudo `[derivado]`) | Todas as seções, todos os arquivos, lacunas, versões, HTML |
| **Longa** | Workshop: perguntas abertas, referências analisadas, vários exemplos, portões de desejo | idem |
**Informação insuficiente:** seção sem base **nunca é omitida nem inventada**. Entra no arquivo com este bloco:
```
> **Informação insuficiente.** Falta: <o que>. Quem fornece: <usuário | pesquisa | cliente>. Impacto: <o que não dá para decidir ou publicar sem isso>. Estado: pendente.
```
Cada bloco entra também em "Lacunas reunidas" (seção 10.3). **O brandbook de modo curto tem, no mínimo, a estrutura do completo.** Seção com bloco de informação insuficiente conta como entregue, com a lacuna declarada.

## 3. Perguntas de configuração
Fazer em rodadas curtas (ver `question-formats.md`), cada uma com exemplo de resposta.

1. **Profundidade.** "Quer responder as perguntas de cada etapa (profundidade longa) ou prefere respostas curtas e que eu proponha o resto (curta)? A. Longa  B. Curta  C. Misto, por etapa." Exemplo: "B." (A estrutura do brandbook é a mesma nas duas.)
2. **Maturidade da marca.** "A. Marca nova, começando do zero  B. Atualizar uma marca que existe  C. Expandir uma marca consolidada  D. Documentar o que já existe." Define se o `Intake` é modo nova, estender ou refazer.
3. **Foco.** (pode marcar mais de uma) "Identidade visual (logo, cores, fontes) · Voz e tom · Aplicações (digital, impressa, redes) · Regras de uso (pode e não pode)."
4. **Ativos.** "O que você precisa sobre os arquivos da marca? A. Só as especificações (códigos de cor, nomes de fonte)  B. Regras de uso com exemplos  C. Modelos prontos  D. Tudo."
5. **Confirmação.** Mostrar o resumo em tabela (marca, maturidade, foco, ativos, profundidade) e perguntar: "Gero com isto, ou mudamos algo?"

## 4. O que entra no brandbook, arquivo por arquivo (igual em todas as profundidades)
| Seção do brandbook | Arquivo de origem | Sempre |
|---|---|:-:|
| Fundação: propósito, visão, missão, valores, promessa, posicionamento | `01-essencia.md`, `02-posicionamento.md` | sim |
| Público | `personas.md` | sim |
| Voz e tom (atributos, escalas, o que não comunicar) | `brand-voice.md` | sim |
| Mensagens | `mensagens.md` (casa de mensagens) | sim |
| Desejo | `05-desejo.md` | sim |
| Identidade visual: logo, paleta, tipografia, imagem | `06-direcao-visual.md`, `design-system/DESIGN.md`, `references/identidade-e-ativos/` | sim |
| Uso do logo (área de respiro, tamanho mínimo, versões, o que não fazer) | guia de identidade e ativos | sim |
| Aplicações: digital, impressa, redes, apresentações | `ativacao/*`, guia de identidade e ativos | sim |
| Regras de uso (pode e não pode) | todos | sim |
| Biblioteca de ativos + modelos | seção 6 deste arquivo | sim |
| Cartão de referência rápida (uma página) | resumo gerado dos anteriores | sim |
| Narrativa da marca (história de criação) | `01-essencia.md` | sim |
| Arquivos para ler (ordem de uso, para pessoas e agentes) | `versoes.json` | sim |
| Qual versão vale | `versoes.json`, `_html/versoes.html` | sim |
| Design system com componentes shadcn | `design-system/` (ver `brand-design-system/references/shadcn.md`) | sim |
| Lacunas reunidas (inclui cada "informação insuficiente") | seção 10.3 deste arquivo | sim |

## 5. Validação antes de entregar
- [ ] Propósito, visão e missão escritos com clareza (ou lacuna declarada)
- [ ] Especificações de identidade visual completas (cores com código, fontes com nome)
- [ ] Diretrizes de voz incluídas
- [ ] Exemplos de uso incluídos
- [ ] "Pode" e "não pode" claros
- [ ] Todo arquivo linkado existe e está aprovado (ver `qa-rubric.md`)

## 6. Gestão de ativos
Serve quando a marca já tem arquivos (logos, fotos, fontes) espalhados ou quando o brandbook exige a biblioteca (sempre).

### 6.1 Ação
| Ação | O que faz |
|---|---|
| **Inventariar** | Lista o que existe, onde está, em que formato e tamanho |
| **Organizar** | Estrutura e categoriza |
| **Auditar** | Confere qualidade, conformidade com a marca, versão atual e lacunas |
| **Governar** | Cria regras de uso, versionamento, distribuição e atualização |

Perguntar qual ação, e quais **tipos** de ativo: logos (arquivos e variações) · cores (arquivos de paleta) · tipografia (arquivos de fonte e especificação) · imagem (fotos, gráficos, ícones). Perguntar também o **formato de entrega**: lista de inventário (planilha) · estrutura de pastas · guia de uso · pacote completo.

### 6.2 Fluxo
1. **Inventário:** logos (todos os formatos e tamanhos), arquivos de paleta, fontes, fotografia e imagens, modelos e ícones.
2. **Categorização:** por tipo de ativo, por uso, por canal, por formato.
3. **Auditoria de qualidade:** qualidade do arquivo, conformidade com a marca, versão atual, lacunas.
4. **Governança:** diretrizes de uso, controle de versão, forma de distribuição, rotina de atualização.

### 6.3 Profundidade
Mesmos entregáveis em qualquer profundidade (inventário, pastas, convenção de nomes, etiquetas, diretrizes de uso, governança, controle de versão, fluxo de distribuição e calendário de auditoria). Na curta, cada item é mais enxuto; o que faltar entra com "informação insuficiente" (seção 2).

## 7. Modelos de saída
**Brandbook: modelo mínimo de cada seção (o brandbook tem todas as seções, em qualquer profundidade)**
```
## Brandbook: <Marca>
### Fundação
Missão: / Visão: / Valores:
### Identidade visual
Cor principal: <hex> · Cores secundárias: <hex, hex> · Fontes: <nomes>
### Uso do logo
Área de respiro: <regra> · Tamanho mínimo: <regra>
```
As demais seções (voz e tom, aplicações, biblioteca de ativos, modelos, cartão de referência rápida, narrativa) seguem o mesmo padrão, com o bloco de informação insuficiente quando não houver base.

**Inventário de ativos (modelo mínimo)**
```
## Inventário de ativos: <Marca>
### Logos
| Arquivo | Formato | Tamanho | Local |
### Cores
| Nome | Hex | RGB | Uso |
### Tipografia
| Fonte | Peso | Uso |
### Lacunas identificadas
- <ativo que falta>
```
Os mesmos campos valem em qualquer profundidade; acrescenta-se estrutura de pastas, convenção de nomes, etiquetas, diretrizes de uso, governança, versionamento, fluxo de distribuição e calendário de auditoria.

**Validação do inventário:** todos os ativos catalogados com local · formato e tamanho anotados · lacunas identificadas · convenção de nomes consistente · diretrizes de uso claras.

## 8. Quem ajuda em cada tarefa
| Tarefa | Quem | Quando |
|---|---|---|
| Montar o brandbook | `brand-builder` (esta skill) | Tarefa principal |
| Documentar especificações visuais | agente `geral-gestao-de-documentacao` | Documentação de ativos |
| Conferir consistência de voz | agente `brand-guardiao-de-voz` | Depois de pronto, e ao revisar peças novas |
| Organizar ativos | agente `geral-coordenacao-de-campanhas` | Inventário e organização |

## 9. Onde salvar
Tudo na raiz da marca (regra 5 do `SKILL.md`): o brandbook em `_brands/<marca>/brandbook.md`; o inventário, quando pedido, em `_brands/<marca>/ativos/inventario.md` (modo 0 Mkt) ou em `<projeto>/assets/inventario.md` (modo Projeto, conforme o mapa de destinos). Nunca em `content/` (o conteúdo produzido vai lá; a marca não). Em marca com projeto próprio, a raiz é a pasta de marca do projeto, com confirmação do usuário.

## 10. Navegação, versões e lacunas (obrigatório em qualquer profundidade)

**Por quê:** quem lê a marca (pessoa ou agente) precisa abrir o arquivo, saber qual versão vale e ver todas as lacunas num lugar só. Decisão do usuário, Futuro Mercado, 2026-10-23.

### 10.1 `versoes.json` (na raiz da marca)
```
{ "marca": "<Marca>", "entrada_html": "brandbook.html",
  "fontes_google": "<url do CSS das fontes, opcional>",
  "tema": { "fundo": "#...", "texto": "#...", "destaque": "#...", "superficie": "#...", "borda": "#...", "apoio": "#...",
            "fonte_titulo": "...", "fonte_texto": "...", "fonte_mono": "..." },
  "html_autoral": { "06-direcao-visual.md": "06-direcao-visual.html" },
  "ignorar": [],
  "itens": [ { "titulo": "Voz e tom", "vigente": "brand-voice-v3.md",
               "historico": ["brand-voice-v2.md", "brand-voice.md"], "estado": "v3 vigente" } ] }
```
Um item por assunto. `tema` vem do `tokens.json` (mesmos hex). `html_autoral` lista os `.md` que já têm HTML feito à mão (direção visual, identidade e ativos, design system): o script não os sobrescreve e aponta os links para eles. Arquivo fora da pasta da marca entra com `../` (o HTML vai para `_html/_fora/`). Item sem `vigente` é arquivo obsoleto.

### 10.2 HTML gêmeo e script
`python3 scripts/brand_html.py build <raiz da marca>` gera `_html/` com o mesmo caminho de cada `.md` registrado (vigente e histórico; o histórico leva faixa "versão antiga, vale X"), reescreve os links `.md` para `.html` e cria `_html/versoes.html` (qual versão vale). `check` falha (código 1) se faltar HTML, se o `.md` for mais novo que o HTML ou se existir `.md` fora do registro. `gaps` imprime as seções de lacunas dos arquivos vigentes. Não precisa de instalação (Python 3.9+). O brandbook em HTML (cartão de uma página) fica na raiz e liga os arquivos pelo HTML, não pelo `.md`.

### 10.3 Seção única de lacunas
O `brandbook.md` tem uma seção **"Lacunas reunidas"**: uma linha por assunto, com origem (arquivo), lacuna e quem resolve, agrupada por tema (marca, voz, visual, ativação, números e operação). Montar rodando `gaps`, juntando duplicatas e tirando as resolvidas. Atualizar sempre que uma lacuna fechar ou surgir. O QA confere (item 17 da `qa-rubric.md`).

### 10.4 Revisão de nomes e lugares
Antes de fechar a etapa 9, listar a pasta da marca e conferir (1) se **a lógica dos nomes** faz sentido (numeração coerente, sufixo de versão só onde há versão, nenhum nome sem sufixo que seja versão antiga) e (2) se **cada arquivo está onde faz sentido** (apoio, comparações e material bruto fora da raiz). Apresentar a proposta ao usuário; mover arquivo só com aprovação, pois muda links em outros arquivos e nas regras do projeto.

## Depois do brandbook
- Conferir peças novas: `brand-guardiao-de-voz`.
- Mensagens: `references` de `brand-voice-messaging` (`casa-de-mensagens.md`).
- Sites e landing pages com a marca: agente `site-construcao-web`.
