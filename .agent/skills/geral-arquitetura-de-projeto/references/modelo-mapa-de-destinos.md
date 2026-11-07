# Modelo de `docs/mapa-de-destinos.md`

Copiar para o projeto, preencher com os caminhos reais e datar. Quem lê: todas as skills de marca, estratégia, conteúdo, imprensa e monitoramento, e os agentes de revisão. Quem escreve em cada pasta é decidido pela skill do assunto (tabela "Quem escreve onde" da skill `geral-arquitetura-de-projeto`); o mapa não repete isso.

**Como ler a coluna Caminho:** é o caminho completo, relativo à raiz do projeto, já com o prefixo de marca ou produto quando houver. `{tipo}`, `{marca}`, `{produto}` e `AAAA-MM-DD - Nome` são placeholders que a skill preenche. Em mono-marca (o padrão), nenhum caminho leva `{marca}` e a coluna Escopo pode ser removida.

**Onde mora o mapa:** mono-marca → `docs/mapa-de-destinos.md`. Multi-marca no mesmo projeto → um mapa na raiz do projeto. Uma marca por repositório → cada repositório tem o seu mapa e a seção "Respostas" informa onde estão os repositórios irmãos e o que é compartilhado.

```markdown
# Mapa de destinos: <Projeto>
Estrutura: <mono-marca | multi-marca cenário A/B/C/D>. Modo: Projeto.
Atualizado em AAAA-MM-DD. Se este mapa divergir de uma regra de skill, **vale este mapa**. Pasta nova, ou tipo de peça que não está aqui, entra aqui antes de ser usada.

| Tipo de peça | Caminho | Escopo | Nome e metadados | Observação |
|---|---|---|---|---|
| Fundações da marca e ativação | brand/ | projeto | etapas do brand-builder; versões -vN | |
| Kit visual e modelos | brand/logo/, brand/modelos/, brand/design-system/ | projeto | | |
| Estratégia geral | estrategia/estrategia-geral.md | projeto | | |
| Calendários | estrategia/calendarios/ | projeto | | |
| Campanha (plano, meta, resultado) | estrategia/campanhas/AAAA-MM-DD - Nome da Campanha/ | projeto | `campanha.md`, `checklist-lancamento.md`, `apresentacao.html`, `resultado.md` | resultado esperado definido antes de começar; as peças ficam em conteudos/ |
| Peça de conteúdo por tipo (blog, linkedin, social, newsletter, video…) | conteudos/{tipo}/AAAA-MM-DD - Nome da Demanda/ | projeto | `briefing.md`, `draft.md`; campo `campanha:` | |
| Fluxo de aprovação | <ver "Respostas" abaixo> | projeto | | opção 0 usa o campo `status:`; A/B/C usam as pastas da esteira |
| Assessoria de imprensa: pauta (pasta com ângulos), pitch por ângulo, release, jornalistas | imprensa/AAAA-MM-DD - Nome/ | projeto | `pauta/pauta-principal.md`, `pauta/angulo-<tema>.md`, `pitch/`, `release.md`, `jornalistas.md` | |
| Controle de envio de imprensa | imprensa/envios.md | projeto | uma linha por envio | status enviado → respondeu → publicou → sem retorno |
| Clipping | imprensa/clipping/ | projeto | `AAAA-MM-DD_<veiculo>_<tema>.md` | |
| Peças publicadas (registro) | conteudos/publicados.md | projeto | | |
| Monitoramento (consultas, termos, relatório) | inteligencia/monitoramento/ | projeto | | regras em brand/ativacao/monitoramento.md |
| Estudos, dados, cases, registro de fontes | inteligencia/estudos/ | projeto | | |
| Tendências | inteligencia/tendencias/ | projeto | | |
| Fontes e coleta | inteligencia/fontes-e-coleta/ | projeto | | |
| Referências do projeto (rubrica, perfil e voz, formatos adaptados) | referencias/ | projeto | | influenciam todo conteúdo; técnica genérica fica na skill |
| Imagens | assets/ (inventario.md) | projeto | `uso_assunto_AAAA-MM-DD_v1.ext` | |
| Documentos do projeto | docs/ | projeto | | este mapa e demais |
| Planos e log de execução | .agent/plans/ | projeto | | |
| Hub Central | Compartilhado/RSS Feed | — | | **somente leitura** |

## Como usar este mapa (toda skill que grava arquivo)
1. Leia esta tabela antes de gravar. Use o **Caminho** da linha do tipo de peça, preenchendo os placeholders. Não monte caminho por conta própria.
2. Tipo de peça que não está aqui: use o tipo mais próximo, grave e avise o usuário para acrescentar a linha.
3. Pasta que o mapa cita e não existe: crie só essa pasta.
4. Nunca mova nem apague arquivo existente para encaixar na estrutura; mudança de lugar só com aprovação.
5. Nunca grave no Hub Central. Em dúvida que este mapa não resolve, consulte a skill `geral-arquitetura-de-projeto`.

## Respostas da conversa de criação
| Pergunta | Resposta | Data |
|---|---|---|
| Há mais de uma marca ou produto? | <não \| sim: cenário A/B/C/D \| suposição: mono-marca, usuário não respondeu> | |
| Onde moram as marcas? (se multi-marca) | <mesmo projeto em marcas/{marca}/ \| um repositório por marca: caminhos> | |
| O que é compartilhado? (escopo por pasta) | <brand, estrategia, conteudos, inteligencia, assets> | |
| Onde está o compartilhado? (se repositório por marca) | <repositório e caminho> | |
| Fluxo de aprovação | <0 sem esteira \| A geral \| B espinha primeiro \| C tipo primeiro>; em multi-marca, por marca ou global | |
| Quem aprova | <nome ou papel> | |

Se a opção de aprovação for A, B ou C, escrever aqui o caminho resultante de peças, `envios.md`, `clipping/` e `publicados.md`.

## Inconsistências conhecidas (só em projeto existente)
O que as regras do projeto dizem versus a árvore real. Não migrar sem aprovação do usuário.
- <ex.: o CLAUDE.md cita ./pautas/ mas a pasta real é imprensa/pautas/>
```

## Como manter
Princípio: `inteligencia/` é repositório do mercado; peça produzida vai para `conteudos/` ou `assets/`; planejamento vai para `estrategia/`. Revisar o mapa na revisão periódica da marca e sempre que uma pasta nascer ou mudar. Mudança de lugar de arquivo existente exige aprovação do usuário.
