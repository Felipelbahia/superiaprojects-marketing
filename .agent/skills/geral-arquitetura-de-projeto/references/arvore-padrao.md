# Árvore padrão de projeto de marketing (modo Projeto, mono-marca)

**Este é o padrão: uma marca ou produto, sem subpasta de marca no caminho.** Marcas e produtos múltiplos só entram se o usuário disser que sim na conversa de criação (ver `cenarios-multi-marca.md`).

Baseada no projeto Futuro Mercado (Marketing - FM), que a testou, com os ajustes de 2026-11-07. Cada pasta nasce quando o projeto precisa dela.

```text
<projeto>/
├── CLAUDE.md  GEMINI.md  AGENTS.md   # regras do projeto (paridade); apontam as skills do 0 Mkt
├── STANDARDS.md                      # nome de arquivo e metadados de peça (inclui `campanha:`)
├── brand/                            # raiz da marca
│   ├── 00-intake.md … brandbook.md   # fundações (etapas do brand-builder)
│   ├── _respostas/                   # respostas literais do usuário, por rodada
│   ├── ativacao/                     # conteudo.md, monitoramento.md, audiovisual.md, demanda.md, anexos (referências, ângulos próprios da marca)
│   ├── design-system/  logo/  modelos/
│   ├── identidade-e-ativos.md  registro-de-decisoes.md
├── estrategia/                       # PLANEJAMENTO
│   ├── estrategia-geral.md
│   ├── calendarios/
│   └── campanhas/AAAA-MM-DD - Nome da Campanha/   # campanha.md, checklist-lancamento.md, apresentacao.html, resultado.md
├── imprensa/                         # ASSESSORIA DE IMPRENSA (produção com ciclo próprio)
│   ├── AAAA-MM-DD - Nome/            # pauta/ (pauta-principal.md + angulo-<tema>.md), pitch/ (um por ângulo), release.md, jornalistas.md
│   ├── envios.md                     # controle de envio: enviado → respondeu → publicou → sem retorno
│   └── clipping/
├── conteudos/                        # PRODUÇÃO: o que a marca cria e guarda
│   ├── <tipo>/AAAA-MM-DD - Nome da Demanda/   # video, blog, linkedin, social, newsletter, email, palestra/apresentacoes, reports
│   ├── (fluxo de aprovação — perguntar sempre, padrão é NÃO ter esteira; ver skill, seção "Fluxo de aprovação")
│   │     # 0 padrão: sem pasta nova, campo `status:` dentro de <tipo>/AAAA-MM-DD - Nome/
│   │     # A: 1_a_aprovar/ 2_aprovado/ 3_publicado/ 4_revisar_ajustar/ (tudo junto, sem pasta de tipo)
│   │     # B: 1_a_aprovar/<tipo>/ 2_aprovado/<tipo>/ … (espinha primeiro — precedente: Futuro Mercado)
│   │     # C: <tipo>/1_a_aprovar/ <tipo>/2_aprovado/ … (tipo primeiro)
│   └── publicados.md  publicados.json
├── inteligencia/                     # REPOSITÓRIO DO MERCADO (sem números nos nomes)
│   ├── tendencias/
│   ├── estudos/                      # acervo_dados_metricas.md, banco_de_cases.md, registro-de-fontes.md
│   ├── fontes-e-coleta/
│   └── monitoramento/                # consultas.md, termos.txt, relatorios/
├── referencias/                      # referências DO PROJETO que influenciam todo conteúdo (rubrica, perfil e voz, formatos adaptados); técnica genérica fica na skill
├── assets/                           # imagens; inventario.md
├── docs/                             # mapa-de-destinos.md e demais documentos
├── scripts/
├── .agent/{plans,skills,agents,rules}/   # agentes de revisão da marca em .agent/agents/
└── .claude/{skills,agents}/              # links para .agent/
```

Não existem `conteudos/_base/` nem `inteligencia/2_imprensa_pr/`. Técnica de redação mora na skill do assunto. Projetos antigos (Futuro Mercado) que ainda têm esses nomes continuam como estão até o usuário aprovar a migração; o mapa deles documenta o que existe.

## Convenções de nome
- Peça de conteúdo: `AAAA-MM-DD_<canal>_<tema-curto>.md` (metadados no topo, conforme `STANDARDS.md`; `campanha:` quando a peça serve a uma campanha).
- Arquivos de apoio da peça (briefing visual, blueprint, roteiro): ao lado da peça, com o mesmo prefixo: `AAAA-MM-DD_<canal>_<tema-curto>_briefing-visual.md`. Pasta por demanda usa `AAAA-MM-DD - Nome da Demanda` (com espaços e hífen), igual nos dois modos; arquivo de peça solta da esteira usa `AAAA-MM-DD_<canal>_<tema-curto>.md` ou o código do calendário (`D01_LI.md`).
- Peça por tipo: `conteudos/<tipo>/AAAA-MM-DD - Nome da Demanda/` com `briefing.md`, `draft.md` e os arquivos do tipo. Vídeo: `roteiro-longo.md` ou `roteiro-curto.md`.
- Assessoria de imprensa: `imprensa/AAAA-MM-DD - Nome/` com `pauta/` (`pauta-principal.md` + `angulo-<tema>.md`), `pitch/` (um por ângulo), `release.md`, `jornalistas.md`.
- Campanha: `estrategia/campanhas/AAAA-MM-DD - Nome da Campanha/campanha.md`; `resultado.md` nasce no encerramento.
- Imagem: `uso_assunto_AAAA-MM-DD_v1.ext`. Versão nova de documento de marca: arquivo `-vN`, o anterior fica.

## Assessoria de imprensa
Produção em `imprensa/`. **Controle de envio** em `imprensa/envios.md` (colunas: data, demanda, ângulo, jornalista, veículo, status `enviado → respondeu → publicou → sem retorno`, `lido` opcional, link do clipping). **Clipping** em `imprensa/clipping/`. Base de jornalistas e veículos só no Hub `Compartilhado/RSS Feed` (leitura).

## Monitoramento: onde fica cada parte
- **Regras** (grafias, pessoas, termos de risco, classificação, níveis de alerta): `brand/ativacao/monitoramento.md` (**fonte da verdade**).
- **Operação** derivada das regras: `inteligencia/monitoramento/consultas.md` e `termos.txt`. O Hub lê o `termos.txt` pelo argumento `--termos <caminho>` do `avaliar.py` (README do Hub); o arquivo **não** precisa morar dentro do Hub.
- Relatório só quando solicitado: `inteligencia/monitoramento/relatorios/AAAA-MM-DD_<tema>.md`.

## Modo 0 Mkt (marca hospedada no 0 Mkt)
O 0 Mkt tem mapa próprio (`docs/mapa-de-destinos.md`), que a regra 1.4 do `CLAUDE.md` manda seguir. Identidade em `_brands/<marca>/` (e `ativos/inventario.md`); output em `content/<marca>/`: peças em `<tipo>/AAAA-MM-DD - Nome da Demanda/`, estratégia e campanhas em `estrategia/` (`estrategia/campanhas/AAAA-MM-DD - Nome da Campanha/`), imprensa em `imprensa/` (com `envios.md` e `clipping/`). Monitoramento, estudos e tendências: ver o mapa (a confirmar).
