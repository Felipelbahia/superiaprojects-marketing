# Destino das saídas da assessoria de imprensa

Regra geral: **o mapa de destinos do projeto manda** (`docs/mapa-de-destinos.md`), inclusive pastas, etapas e fluxo de aprovação; **mudou o arranjo, altera-se só o mapa, não esta skill**. A tabela abaixo é só o **padrão de partida para projeto novo**. Esta tabela é o padrão quando o mapa segue a árvore padrão da skill `geral-arquitetura-de-projeto`.


**Princípio:** `inteligencia/` é o **repositório do mercado** (tendências, pesquisas, estudos, materiais de terceiros, análises de mercado); **o que a assessoria produz vai para a produção** (`conteudos/`). **Esta organização está em ajuste pelo usuário** (a assessoria é mais complexa); mudanças maiores esperam esse ajuste.

| Saída | Modo Projeto | Modo 0 Mkt (marca em `_brands/`) |
|---|---|---|
| Pauta (tabela de fatos verificáveis, aderência) | `conteudos/imprensa/AAAA-MM-DD - <Nome>/pauta.md` | `content/<marca>/imprensa/AAAA-MM-DD - <Nome>/pauta.md` |
| Pitch e press release | mesma pasta: `pitch.md`, `release.md` | mesma pasta |
| Seleção de jornalistas-alvo da pauta | mesma pasta: `jornalistas.md` (a lista-mestra continua no Hub) | mesma pasta |
| **Clipping** (matérias em que a marca ou o porta-voz foi citado pela imprensa) | `conteudos/imprensa/clipping/AAAA-MM-DD_<veiculo>_<tema>.md` | `content/<marca>/imprensa/clipping/` |
| Histórico de envios e notas de relacionamento (**base atual, em ajuste**) | `inteligencia/2_imprensa_pr/envios/AAAA-MM-DD_<veiculo>_<tema>.md` | `content/<marca>/imprensa/envios/` |
| Relatório de menções ou de crise (**só sob pedido**; dado de monitoramento) | `inteligencia/5_monitoramento/relatorios/AAAA-MM-DD_<tema>.md` | `content/<marca>/monitoramento/` |
| Consultas e `termos.txt` de monitoramento | `inteligencia/5_monitoramento/` (derivam de `brand/ativacao/monitoramento.md`) | `content/<marca>/monitoramento/` |
| Mailing, guias de voz, mapa de veículos, matriz de newsjacking, media training (**base**) | `inteligencia/2_imprensa_pr/` | `content/<marca>/imprensa/base/` |
Pautas e releases que já existiam em `inteligencia/2_imprensa_pr/` antes do mapa são **históricos e não são movidos**.

## Hub Central (`Compartilhado/RSS Feed`): somente leitura
- **Ler:** `bases/veiculos/veiculos.csv`, `bases/jornalistas/_indice.json` e as fichas, pelo CLI `motores/jornalistas/consultar_hub.py` (ver `cliente-hub-imprensa`).
- **Não copiar** a base para o projeto. A seleção da pauta guarda só nomes e o motivo.
- **Termos de monitoramento:** o `avaliar.py` do Hub aceita `--termos <caminho>`; o arquivo do projeto (`inteligencia/5_monitoramento/termos.txt`) é passado por esse argumento, sem morar no Hub.
- **Dado novo e público que deve voltar ao Hub** (por exemplo, ficha de jornalista): só pelo procedimento do Hub e com confirmação do usuário.

## Conflitos a avisar ao usuário
Se o `CLAUDE.md` do projeto citar `./pautas/`, `./envios/` ou `./historico_imprensa.md` e essas pastas não existirem, usar o mapa e dizer qual é a divergência; não criar a pasta citada só para obedecer ao texto.
