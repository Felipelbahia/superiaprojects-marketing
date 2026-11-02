# Árvore padrão de projeto de marketing (modo Projeto)

Baseada no projeto Futuro Mercado (Marketing - FM), que a testou. Cada pasta nasce quando o projeto precisa dela.

```text
<projeto>/
├── CLAUDE.md  GEMINI.md  AGENTS.md   # regras do projeto (paridade); apontam as skills do 0 Mkt
├── STANDARDS.md                      # nome de arquivo e metadados de peça
├── brand/                            # raiz da marca
│   ├── 00-intake.md … brandbook.md   # fundações (etapas do brand-builder)
│   ├── _respostas/                   # respostas literais do usuário, por rodada
│   ├── ativacao/                     # conteudo.md, monitoramento.md, audiovisual.md, demanda.md, anexos (referências)
│   ├── design-system/  logo/  modelos/
│   ├── identidade-e-ativos.md  registro-de-decisoes.md
├── conteudos/                        # PRODUÇÃO: o que a marca cria e guarda
│   ├── <tipo>/AAAA-MM-DD - Nome da Demanda/   # imprensa, video, blog, linkedin, social, newsletter, email, campaigns, palestra/apresentacoes, reports
│   ├── 1_a_aprovar/ 2_aprovado/ 3_publicado/ 4_revisar_ajustar/   # esteira (opcional, conforme o mapa)
│   ├── _base/{estrategia,pesquisa,referencias}/
│   └── publicados.md  publicados.json
├── inteligencia/                     # REPOSITÓRIO DO MERCADO: tendências, pesquisas, estudos, materiais de terceiros, análises de mercado; não é onde se guardam peças produzidas
│   ├── 1_radar_tendencias/
│   ├── 2_imprensa_pr/                # base: mailing, guias de voz, mapa de veículos, envios/ (histórico); Hub só leitura
│   ├── 3_estudos_embasamento/        # acervo_dados_metricas.md, banco_de_cases.md
│   ├── 4_fontes_e_coleta/
│   └── 5_monitoramento/              # consultas.md, termos.txt, relatorios/
├── campanhas/  calendarios/
├── assets/                           # imagens; inventario.md
├── docs/                             # mapa-de-destinos.md e demais documentos
├── scripts/
├── .agent/{plans,skills,agents,rules}/   # agentes de revisão da marca em .agent/agents/
└── .claude/{skills,agents}/              # links para .agent/
```

## Convenções de nome
- Peça de conteúdo: `AAAA-MM-DD_<canal>_<tema-curto>.md` (metadados no topo, conforme `STANDARDS.md`).
- Arquivos de apoio da peça (briefing visual, blueprint, roteiro): ao lado da peça, com o mesmo prefixo: `AAAA-MM-DD_<canal>_<tema-curto>_briefing-visual.md`. Pasta por demanda usa `AAAA-MM-DD - Nome da Demanda` (com espaços e hífen), igual nos dois modos; arquivo de peça solta da esteira usa `AAAA-MM-DD_<canal>_<tema-curto>.md` ou o código do calendário (`D01_LI.md`).
- Peça por tipo (modo 0 Mkt e como o projeto Futuro Mercado já faz): `conteudos/<tipo>/AAAA-MM-DD - Nome da Demanda/` com `briefing.md`, `draft.md` e os arquivos do tipo. Assessoria de imprensa: `conteudos/imprensa/AAAA-MM-DD - Nome/` com `pauta.md`, `pitch.md`, `release.md`, `jornalistas.md`. Vídeo: `roteiro-longo.md` ou `roteiro-curto.md`.
- Histórico de envios à imprensa: `inteligencia/2_imprensa_pr/envios/AAAA-MM-DD_<veiculo>_<tema>.md`.
- Relatório de monitoramento (só sob pedido): `inteligencia/5_monitoramento/relatorios/AAAA-MM-DD_<tema>.md`.
- Imagem: `uso_assunto_AAAA-MM-DD_v1.ext`. Versão nova de documento de marca: arquivo `-vN`, o anterior fica.

## Assessoria de imprensa (em ajuste pelo usuário)
`conteudos/imprensa/AAAA-MM-DD - Nome/` para pauta, pitch, release e jornalistas; **`conteudos/imprensa/clipping/`** para matérias em que a marca ou o porta-voz é citado. A base atual em `inteligencia/2_imprensa_pr/` será tratada em outro lugar quando o usuário ajustar a assessoria; não reorganizar antes.

## Monitoramento: onde fica cada parte
- **Regras** (grafias, pessoas, termos de risco, classificação, níveis de alerta): `brand/ativacao/monitoramento.md` (**fonte da verdade**).
- **Operação** derivada das regras: `inteligencia/5_monitoramento/consultas.md` e `termos.txt`. O Hub lê o `termos.txt` pelo argumento `--termos <caminho>` do `avaliar.py` (README do Hub); o arquivo **não** precisa morar dentro do Hub.
- Relatório só quando solicitado.

## Modo 0 Mkt (marca hospedada no 0 Mkt)
`_brands/<marca>/` com os arquivos da marca (e `ativos/inventario.md`) e `content/<marca>/<tipo>/AAAA-MM-DD - Nome da Demanda/` para peças (regra 1.4 do `CLAUDE.md` do 0 Mkt). Imprensa: `content/<marca>/imprensa/…`; monitoramento (dados): `content/<marca>/monitoramento/…`.
