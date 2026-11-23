# Contrato de Artefatos e Ciclo de Estados de Peças de Conteúdo
**Versão:** 1.0.0
**Módulo:** `conteudo-linha-de-producao`
**Crédito de Origem:** Conceitos de arquitetura de artefatos e pipeline adaptados a partir de `promovaweb/inboundfy` (licença AGPL-3.0), redigidos com estrutura e regras autorais exclusivas do ecossistema Super IA Projects `0 Mkt`.

---

## 1. Visão Geral e Princípio de Rastreabilidade

Toda peça de conteúdo produzida no ecossistema `0 Mkt` (artigo de blog, post social, carrossel, roteiro audiovisual, e-mail, newsletter ou landing page) é tratada como um **artefato governado**. 

Para garantir reprodutibilidade, conformidade e evitar publicações indevidas, todo arquivo de conteúdo deve conter um **cabeçalho padronizado de metadados** e obedecer a uma **máquina de estados finita** de 6 estágios.

---

## 2. Cabeçalho Padronizado da Peça (Contrato Obrigatório)

O cabeçalho deve ser posicionado no topo do arquivo da peça (em formato de bloco de metadados legível ou frontmatter YAML):

```markdown
---
marca: [slug da marca ativa em _brands/, ex.: plinq, waimonitor, pr-pulse]
canal: [instagram | linkedin | blog | email | youtube | landing-page]
persona: [nome da persona vinculada de _brands/<marca>/personas.md]
origem_briefing: [caminho relativo do briefing ou pauta geradora]
fontes_lidas:
  - [URL, estudo, transcrição ou material primário 1]
  - [URL, estudo, transcrição ou material primário 2]
estado: [rascunho | em revisao | aprovado | agendado | no ar | arquivado]
versao_aprovada: [nenhuma | v1 | v2 ...]
proxima_acao: [ação imediata recomendada, ex.: submeter ao revisor / agendar publicação]
# Campos complementares preenchidos na publicação:
data_publicacao: [AAAA-MM-DD ou vazio]
url_publicada: [link da postagem no ar ou vazio]
---
```

### Detalhamento dos Campos
1. **`marca`**: identificador único da marca hospedada.
2. **`canal`**: plataforma destino da distribuição.
3. **`persona`**: público específico a quem a mensagem se dirige.
4. **`origem_briefing`**: rastreabilidade até o arquivo ou sprint que demandou a peça.
5. **`fontes_lidas`**: âncoras fáticas obrigatórias (proibido inventar dados ou citações sem ancoragem).
6. **`estado`**: estágio atual da peça na máquina de estados.
7. **`versao_aprovada`**: trava de segurança; só preenchida quando um revisor emitir parecer formal favorável.
8. **`proxima_acao`**: direcionamento operacional para o operador ou agente seguinte.
9. **`data_publicacao`** e **`url_publicada`**: registros históricos pós-distribuição.

---

## 3. Máquina de Estados e Ciclo de Vida da Peça

A peça percorre obrigatoriamente um ciclo unidirecional de 6 estados:

```
[ rascunho ] ──> [ em revisao ] ──> [ aprovado ] ──> [ agendado ] ──> [ no ar ] ──> [ arquivado ]
       ▲                │
       └─ (reprovado) ──┘
```

### Transições Permitidas
| Estado Atual | Próximo Estado Permitido | Condição Mandatória |
|---|---|---|
| `rascunho` | `em revisao` | Peça redigida pela especialista produtora e filtrada pelo workflow `/geral-anti-slop`. |
| `em revisao` | `aprovado` | Parecer favorável emitido por revisor independente (`brand-guardiao-de-voz` ou técnico) via `/conteudo-aprovacao`. |
| `em revisao` | `rascunho` | Parecer com veredito `REPROVADO` ou `AJUSTES NECESSÁRIOS` emitido na tabela de 5 campos. Gera ciclo `v2`. |
| `aprovado` | `agendado` | Alocação confirmada na ferramenta de agendamento ou calendário editorial. |
| `agendado` | `no ar` | Publicação efetivamente realizada no canal de distribuição. |
| `no ar` | `arquivado` | Peça descontinuada, substituída por versão mais recente ou ciclo de campanha encerrado. |

> **Trava de Saída:** Peças que atingiram o estado `no ar` **só podem transitar para `arquivado`**. Nunca retornam a rascunho ou revisão.

---

## 4. Regra de Ouro: Invalidação Automática por Edição Posterior

Uma aprovação é vinculada estritamente ao hash textual da versão auditada.

1. **Proibição de Sobrescrita:** É terminantemente proibido sobrescrever ou alterar diretamente o arquivo de uma peça marcada como `aprovado` ou `agendado`.
2. **Invalidação Imediata:** Se qualquer ajuste textual, título ou mídia for solicitado após a aprovação, a aprovação anterior é **automaticamente anulada**.
3. **Criação Obrigatória de Nova Versão:**
   - O arquivo original aprovado (ex.: `copy-opcao-1-v1.md`) permanece intocado no disco e versionado no Git.
   - Cria-se um novo arquivo derivado (ex.: `copy-opcao-1-v2.md`).
   - O cabeçalho de `v2` deve registrar obrigatoriamente:
     - `estado: em revisao`
     - `versao_aprovada: nenhuma`
     - `proxima_acao: submeter v2 ao protocolo de dois passes no /conteudo-aprovacao`
4. **Releitura Integral na v2:** O revisor audita a nova versão em dois passes (passe literal dos apontamentos + passe holístico de integridade), sem herdar aprovações automáticas.

---

## 5. Protocolo de Reentrada e Idempotência Editorial

Em fluxos editoriais com lotes de conteúdo ou sessões longas de execução:

1. **Preservação de Insumos Brutos:**
   - Arquivos de pesquisa, transcrições brutas (`transcricao.txt`), bases mineradas (`shorts.csv`) e briefings nunca são deletados ou limpos durante reentradas.
2. **Idempotência de Peças Aprovadas:**
   - Uma nova execução da esteira para um mesmo tema/campanha verifica os artefatos existentes. Peças com `estado: aprovado`, `agendado` ou `no ar` são preservadas intactas.
3. **Novas Variações e Incrementos:**
   - Caso novas abordagens sejam solicitadas, a esteira deve gerar novos arquivos numerados (`copy-opcao-2.md`, `copy-opcao-3.md`) ou um novo pacote datado no mapa de destinos (`AAAA-MM-DD - Nome/`), evitando colisão de nomes e perda de trabalho já validado.

