# Destino das saídas da assessoria de imprensa

Regra geral: **o mapa de destinos do projeto manda** (`docs/mapa-de-destinos.md`), inclusive pastas, etapas e fluxo de aprovação; **mudou o arranjo, altera-se só o mapa, não esta skill**. Se o projeto tem mapa, siga-o. **Sem mapa, grave no padrão direto (coluna sem marca no caminho, que é o padrão mono-marca)** e proponha o mapa ao usuário (skill `geral-arquitetura-de-projeto`).

**Princípio:** tudo o que a assessoria produz e registra vai para a produção, em `imprensa/` (pauta, pitch, release, jornalistas, controle de envio, clipping). `inteligencia/` é o repositório do mercado e só recebe monitoramento, estudos e tendências. **Jornalista, veículo e a metodologia da base (validação de e-mail, scraping/RSS) só vivem no Hub `Compartilhado/RSS Feed`, nunca duplicados no projeto** — consultar via `motores/jornalistas/consultar_hub.py`, nunca copiar. **A técnica de redação não mora no projeto: está nesta skill**, em `story-angles.md` (ângulos editoriais), `newsjacking.md` (matriz de newsjacking), `journalist-pitching.md` (abordagem e pitch) e `press-release-templates.md` (templates).

| Saída | Padrão direto (sem marca no caminho) | Mapa do 0 Mkt (multi-marca, marca em `_brands/`) |
|---|---|---|
| Pauta principal (tabela de fatos verificáveis, aderência) | `imprensa/AAAA-MM-DD - <Nome>/pauta/pauta-principal.md` | `content/<marca>/imprensa/AAAA-MM-DD - <Nome>/pauta/pauta-principal.md` |
| Um arquivo por ângulo | `pauta/angulo-<tema>.md` na mesma pasta; cita de qual ângulo permanente da marca nasceu | idem |
| Pitch (um por ângulo) e press release | `pitch/` (um arquivo por ângulo) e `release.md` na mesma pasta | idem |
| Seleção de jornalistas-alvo (planejada) | `jornalistas.md` na mesma pasta (a lista-mestra continua no Hub) | idem |
| **Controle de envio** (qual ângulo foi para qual jornalista, quando e o que voltou) | `imprensa/envios.md` (ou `.csv`): data, demanda, ângulo, jornalista, veículo, status `enviado → respondeu → publicou → sem retorno`, `lido` opcional, link do clipping (em multi-marca, coluna marca) | `content/<marca>/imprensa/envios.md` |
| **Clipping** (matérias em que a marca ou o porta-voz foi citado) | `imprensa/clipping/AAAA-MM-DD_<veiculo>_<tema>.md` | `content/<marca>/imprensa/clipping/` |
| Relatório de menções ou de crise (**só sob pedido**; dado de monitoramento) | `inteligencia/monitoramento/relatorios/AAAA-MM-DD_<tema>.md` | `content/<marca>/inteligencia/monitoramento/relatorios/` |
| Consultas e `termos.txt` de monitoramento | `inteligencia/monitoramento/` (derivam de `brand/ativacao/monitoramento.md`) | `content/<marca>/inteligencia/monitoramento/` |
| Media training e mensagens-âncora do porta-voz | `brand/` | `_brands/<marca>/` |
| Ângulos permanentes da marca (posicionamento) | `brand/ativacao/` | `_brands/<marca>/` |
| Mailing, ficha/perfil de jornalista, mapa de veículos, metodologia de e-mail/scraping (**base — só no Hub**) | `Compartilhado/RSS Feed/bases/jornalistas/`, `bases/veiculos/veiculos.csv`, `.agent/skills/jornalista-extracao/references/` | idem (Hub é único para todos os projetos) |

Os registros transversais (`envios.md` e `clipping/`) ficam **sempre** em `imprensa/`, qualquer que seja o fluxo de aprovação do projeto (com ou sem esteira).

Pautas, releases e envios que já existiam em outros caminhos antes do mapa (por exemplo `inteligencia/2_imprensa_pr/`) são **históricos e não são movidos** sem aprovação do usuário.

## Hub Central (`Compartilhado/RSS Feed`): somente leitura
- **Ler:** `bases/veiculos/veiculos.csv`, `bases/jornalistas/_indice.json` e as fichas, pelo CLI `motores/jornalistas/consultar_hub.py` (ver `cliente-hub-imprensa`).
- **Não copiar** a base para o projeto. A seleção da pauta guarda só nomes e o motivo.
- **Termos de monitoramento:** o `avaliar.py` do Hub aceita `--termos <caminho>`; o `termos.txt` do projeto (caminho do mapa, padrão `inteligencia/monitoramento/termos.txt`) é passado por esse argumento, sem morar no Hub.
- **Dado novo e público que deve voltar ao Hub** (por exemplo, ficha de jornalista): só pelo procedimento do Hub e com confirmação do usuário.

## Conflitos a avisar ao usuário
Se o `CLAUDE.md` do projeto citar `./pautas/`, `./envios/` ou `./historico_imprensa.md` e essas pastas não existirem, usar o mapa e dizer qual é a divergência; não criar a pasta citada só para obedecer ao texto.
