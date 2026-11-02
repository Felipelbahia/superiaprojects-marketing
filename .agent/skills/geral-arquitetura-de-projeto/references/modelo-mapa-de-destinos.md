# Modelo de `docs/mapa-de-destinos.md`

Copiar para o projeto, preencher com os caminhos reais e datar. Quem lê: todas as skills de marca, conteúdo, imprensa e monitoramento, e os agentes de revisão.

```markdown
# Mapa de destinos: <Projeto>
Atualizado em AAAA-MM-DD. Modo: Projeto. Se este mapa divergir de uma regra de skill, **vale este mapa**.

| Tipo de peça | Pasta | Nome e metadados | Quem escreve | Quem lê | Observação |
|---|---|---|---|---|---|
| Fundações da marca e ativação | brand/ | etapas do brand-builder; versões -vN | brand-builder | todas | |
| Kit visual e modelos | brand/logo/, brand/modelos/ | | | | |
| Peça de conteúdo por tipo (blog, linkedin, social, newsletter, video, ...) | conteudos/<tipo>/ | pasta AAAA-MM-DD - Nome da Demanda/ | skills de conteúdo | | |
| Esteira de aprovação (se o projeto usa) | conteudos/1_a_aprovar → 2_aprovado → 3_publicado; 4_revisar_ajustar | AAAA-MM-DD_<canal>_<tema>.md | | | |
| Assessoria de imprensa (pauta, pitch, release, jornalistas) — **produção** | conteudos/imprensa/ | pasta AAAA-MM-DD - Nome/ | pr-assessoria-de-imprensa | | |
| Histórico de envios (base) | inteligencia/2_imprensa_pr/envios/ | | | | repositório do mercado |
| Monitoramento (consultas, termos, relatório) | inteligencia/5_monitoramento/ | | | | regras em brand/ativacao/monitoramento.md |
| Dados e cases | inteligencia/3_estudos_embasamento/ | | | | |
| Imagens | assets/ (inventario.md) | | | | |
| Hub Central | Compartilhado/RSS Feed | | | **somente leitura** | |

## Inconsistências conhecidas (o que as regras do projeto dizem e a árvore real)
- <ex.: CLAUDE.md cita ./pautas/ mas a pasta real é inteligencia/2_imprensa_pr/pautas/>
```

## Como manter
Princípio: `inteligencia/` é repositório do mercado; peça produzida vai para `conteudos/` ou `assets/`. Revisar o mapa na revisão periódica da marca e sempre que uma pasta nascer ou mudar. Mudança de lugar de arquivo existente exige aprovação do usuário.
