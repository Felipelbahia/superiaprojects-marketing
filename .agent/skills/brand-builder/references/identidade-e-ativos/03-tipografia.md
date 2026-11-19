# 3. Tipografia: famílias, hierarquia, licença e uso

**Fontes:** `visual-identity` (família principal e secundária, hierarquia de exemplo), `brand-guidelines` (família, pilha de reserva, web fonts), `branding-expert` (níveis: display, corpo, interface, mono), `brand-strategy-framework` (diretrizes tipográficas), guia da Anthropic (par Poppins + Lora com reserva Arial + Georgia e regra de aplicação por tamanho). Reescrito e ampliado no E5.

> **Divisão de trabalho com o `brand-design-system`.** A escala tipográfica para **tela** (tamanhos, linha, peso, pilha de sistema) é decidida na etapa 7 e vive no `tokens.json` (`brand-design-system/references/decisoes.md`, seção 2). Este capítulo **não a redigita**. Ele cobre o que o design system não cobre: **licença e arquivos**, **substituição em documentos e e-mail**, **impressão**, **português** e **governança das fontes**.

## 3.1 Papéis tipográficos

| Papel | Uso | Quantas famílias |
|---|---|---|
| **Display / títulos** | Manchetes, capas, destaques; carrega a personalidade | 1 |
| **Corpo** | Parágrafos e leitura longa; prioriza legibilidade | 1 (pode ser a mesma do display) |
| **Interface** | Botões, rótulos, menus | A mesma do corpo, em geral |
| **Mono (código, dados)** | Só se a marca mostra código ou números tabulares | 0 ou 1 |

Regra de economia: **no máximo 2 famílias** (3 só com justificativa). O que dá variedade é peso e tamanho, não mais fontes. No display, limitar a 2 ou 3 pesos; o corpo pode ter mais.

## 3.2 Decidir as famílias

1. **Partir do que existe.** Se o `style-guide.md` ou o logo já definem fonte, ela vence; estender, nunca substituir.
2. **Casar com a voz e o arquétipo** (etapas 2 e 4): voz seca e precisa pede peso e espaçamento contidos; voz expressiva tolera contraste maior de tamanho. Mostrar ao usuário o efeito antes de aprovar.
3. **Origem da fonte** (decidir e registrar):
   - **Pilha de sistema** (padrão do `brand-design-system`): zero licença, carrega rápido, sem dependência externa.
   - **Fonte aberta ou gratuita**: conferir a licença da própria fonte (uso em web, aplicativo, impressão e vídeo pode ter regras diferentes).
   - **Fonte licenciada**: guardar a licença e o escopo (quantos usuários, que mídias, validade).
4. **Registrar a fonte também do logo**, mesmo que só exista como curvas: o time precisa saber qual é para não "refazer de memória".

## 3.3 Hierarquia (modelo de ficha)

Tamanhos e pesos reais vêm do `tokens.json`. Esta tabela é o **formato** de registro no guia, uma linha por nível:

| Nível | Família | Peso | Tamanho (tela) | Linha | Uso |
|---|---|---|---|---|---|
| Display | | | | 1.05 a 1.2 | Capas e manchetes de impacto |
| H1 a H4 | | | | | Títulos e subtítulos |
| Corpo | | | 16 px ou mais | 1.4 a 1.6 | Leitura |
| Pequeno / legenda | | | | | Notas, rodapés |
| Interface | | | | | Botões e rótulos |

Exemplo de formato do guia antigo (`visual-identity`), só para ilustrar: H1 48 px negrito, H2 36 px negrito, corpo 16 px regular. **Não é valor para outras marcas.**

Regras de legibilidade (mesmas do design system, repetidas por serem as que o time mais esquece): comprimento de linha de 60 a 75 caracteres; ajuste de espaçamento entre letras só em caixa alta e em títulos grandes; evitar blocos longos em caixa alta.

## 3.4 Pilha de reserva (fallback)

Fonte própria nunca vai sozinha. Sempre declarar a sequência de reserva:

```
Títulos:  <Fonte da marca>, <reserva parecida>, sans-serif
Corpo:    <Fonte da marca>, <reserva parecida>, serif ou sans-serif
```

O guia da Anthropic é um exemplo de como registrar: títulos em Poppins com reserva Arial; corpo em Lora com reserva Georgia; regra de aplicação "títulos de 24 pt para cima na fonte de títulos; o resto na fonte de corpo"; "se a fonte não estiver instalada, cai na reserva sem quebrar a leitura". A regra de aplicação por tamanho é uma boa prática a copiar.

## 3.5 Licença, arquivos e fontes não instaladas

| Situação | Regra |
|---|---|
| **Site e aplicativo** | Arquivo da fonte servido localmente (ou serviço aprovado); sem dependência externa sem decisão do usuário (regra 9 do `brand-design-system`) |
| **Documentos e apresentações** (Word, Google Docs, PowerPoint, Keynote) | Quem recebe o arquivo pode não ter a fonte. Definir a **fonte substituta aprovada** para esses casos, ou entregar em PDF |
| **E-mail** | Clientes de e-mail ignoram fonte própria; usar pilha de sistema aprovada |
| **Impressão** | Converter texto em curvas ou incorporar a fonte no PDF; confirmar com a gráfica |
| **Vídeo e motion** | Fonte instalada na máquina que renderiza; conferir a licença para uso em vídeo |
| **Equipe e agências** | Dizer onde baixar a fonte aprovada e quem guarda a licença (ver inventário de ativos) |

Registrar tudo no inventário (`../../brandbook-e-ativos.md`, seção 6): arquivo, versão, licença, validade, quem é o dono.

### Arquivos de fonte para web (script)

A escala (tamanho, linha, peso) continua no `tokens.json`. O que faltava era o **arquivo da fonte** e o `@font-face`. Quando a marca decidiu por fonte própria, o `brand-design-system/scripts/brand_webfonts.py` cuida disso a partir de um manifesto `design-system/fonts.json` que o dono aprova:

```bash
# a partir da pasta do brand-builder
python3 ../brand-design-system/scripts/brand_webfonts.py build <raiz da marca>   # baixa ou copia, gera fonts.css e LICENCAS.md
python3 ../brand-design-system/scripts/brand_webfonts.py check <raiz da marca>
```

Exemplo mínimo de `design-system/fonts.json` (uma fonte de licença aberta, baixada por https com a versão fixa na URL):

```json
{"familias": [{"familia": "Inter", "papel": "sans",
  "arquivos": [{"peso": "400", "estilo": "normal",
    "url": "https://cdn.jsdelivr.net/npm/@fontsource/inter@5.0.8/files/inter-latin-400-normal.woff2",
    "licenca": "OFL-1.1", "autoria": "The Inter Project Authors",
    "fonte_da_licenca": "https://github.com/rsms/inter/blob/master/LICENSE.txt"}]}]}
```

Na primeira rodada o script avisa o SHA-256 que registrou; copiar para o campo `sha256` trava a versão. O texto integral da licença (OFL.txt) não é baixado pelo script: guardar à parte e citar o endereço em `fonte_da_licenca`.

- **Cada arquivo traz no manifesto:** família, peso, estilo, `url` (https) ou `arquivo` (dentro da pasta da marca), licença, autoria, onde a licença está escrita e, de preferência, o SHA-256 (sem ele o script registra o hash e avisa).
- **Só licença aberta é baixada:** `OFL-1.1`, `Apache-2.0` e `UFL-1.0`. Qualquer outra (paga, desconhecida) nunca é baixada. Se o dono já colocou o arquivo licenciado na pasta da marca, o css aponta para ele com um aviso para conferir o escopo da licença (web, app, impressão); sem arquivo, só a variável de reserva é escrita.
- **Saída** em `design-system/fonts/`: os arquivos, `fonts.css` (`font-display: swap` e uma variável por papel presente no manifesto: `--font-sans`, `--font-serif`, `--font-mono` ou `--font-display`) e `LICENCAS.md`, que alimenta o inventário. A pilha de reserva vem do campo `reserva` da família; sem ele, do `font-sans` (ou `font-mono`, no papel mono) do `tokens.json`; sem `tokens.json`, de uma pilha de sistema embutida no script. Duas famílias com o mesmo papel: só a primeira define a variável.
- **Cuidados do script:** aceita só `woff2`, `woff`, `ttf` e `otf`, confere o cabeçalho do arquivo, limita o **download** a 8 MB (arquivo local não tem esse limite), só lê arquivo local de dentro da pasta da marca, grava apenas em `design-system/fonts/` e trata o arquivo como dado, nunca como código.
- **Padrão continua sendo a pilha de sistema** (3.2). Rodar o script só depois da decisão do dono e do teste com texto em português (3.6).

*Ideia adaptada da skill `tipografia-web` do Brandfy (Promovaweb, AGPL-3.0); código e texto reescritos aqui.*

## 3.6 Português e acentuação

Marca brasileira: **testar a fonte com texto em português antes de aprovar**. Conferir ç, ã, õ, á, é, í, ó, ú, â, ê, ô, à, ü e as aspas e travessões, em todos os pesos que serão usados. Fonte sem os caracteres cai na reserva no meio da palavra e quebra a marca.

## 3.7 Acessibilidade

- Corpo em tela a partir de 16 px, salvo decisão registrada.
- Contraste do texto: ver `tokens-e-contraste.md` (4,5:1 normal; 3:1 grande).
- Não usar fonte decorativa para texto corrido; reservar para display.
- Respeitar o zoom do usuário (unidades relativas, não tamanhos travados), quando o canal permitir.

## 3.8 Saída deste capítulo

Seção "Tipografia" do `identidade-e-ativos.md`:

```
## Tipografia
Famílias e papéis (3.1) / Origem e licença (3.2) / Hierarquia (3.3, referência ao tokens.json)
Pilha de reserva e regra de aplicação (3.4) / Regras por canal (3.5) / Teste de português (3.6) / Lacunas
```

## Checklist

- [ ] Máximo de 2 famílias, cada uma com papel
- [ ] Fonte do logo registrada
- [ ] Origem e licença de cada fonte anotadas (escopo, validade, dono)
- [ ] Pilha de reserva e regra de aplicação por tamanho
- [ ] Fonte substituta aprovada para documentos e e-mail
- [ ] Teste com acentos em todos os pesos
- [ ] Hierarquia registrada e igual ao `tokens.json`
