# Verificação

Não declarar "feito" sem executar. Cada item vira nota 10 só com evidência. O que não puder ser verificado é relatado ao usuário, não omitido.

## Ferramentas

- Navegador via `mcp__chrome-devtools__*` (carregar com ToolSearch): `navigate_page` com `file://`, `take_screenshot`, `evaluate_script`, `emulate`/`resize_page`, `list_console_messages`.
- Terminal: `grep`, `python3 -I`.

## Checklist

| # | Item | Como verificar | Evidência |
|---|---|---|---|
| 1 | Abre sem erro | `navigate_page` + `list_console_messages` | console sem erros |
| 2 | Tema claro | screenshot com `data-theme=light` | captura |
| 3 | Tema escuro | clicar o toggle e capturar | captura |
| 4 | Painéis independentes | com a página em escuro, `evaluate_script` lê a cor de fundo computada do painel Light e do Dark | valores diferentes e iguais aos tokens |
| 5 | Download | `evaluate_script` obtém o texto de `#design-md` e compara com o `DESIGN.md` em disco; clique dispara `download="DESIGN.md"` | diff vazio |
| 6 | Copiar | clicar uma amostra e um bloco; ler `navigator.clipboard.readText()` ou o textarea de fallback | texto igual ao hex e ao bloco |
| 7 | Impressão | `emulate` mídia `print` e capturar; checar menu oculto e quebras | captura |
| 8 | Celular | `resize_page` 375x812 e 360x800; `scrollWidth <= clientWidth` | sem rolagem horizontal |
| 9 | Contraste | tabela de `_respostas/contraste-design-system.md` | todos aprovados ou exceção declarada |
| 10 | Paridade de valores | comparar `tokens.json`, front matter do `DESIGN.md` e variáveis do CSS | ver abaixo |
| 11 | Regras | `grep -n -i -E 'gradient' index.html` (vazio, salvo exceção); busca por emoji; seção Imagery coerente com os anexos | saída dos comandos |
| 12 | Voice & tone | texto da seção bate com `brand-voice.md` e cita "O que NÃO comunicar" | trecho citado |

## Paridade de valores (item 10)

Comando-base, rodado no scratchpad:

```bash
python3 -I - <<'E'
import json,re,sys
t=json.load(open("tokens.json"))
css=open("index.html").read(); md=open("DESIGN.md").read()
miss=[]
for mode,vals in t["colors"].items():
    for k,v in vals.items():
        if v.upper() not in css.upper(): miss.append(("css",mode,k,v))
        if v.upper() not in md.upper():  miss.append(("md",mode,k,v))
print(miss or "paridade de cores ok")
E
```

Estender o mesmo laço para `rounded`, `spacing` e `typography`. Qualquer divergência: corrigir na fonte (`tokens.json`), regenerar os dois artefatos e repetir.

## Relato final ao usuário

Listar item por item: verificado (com evidência), parcialmente verificado, não verificado (e por quê). Exemplo de não verificado: impressão real em papel; renderização em Safari iOS; leitores de tela.

## Falhas encontradas no primeiro uso (WaiMonitor, 2026-10-19)

Conferir de propósito, porque aconteceram:

| Falha | Como evitar |
|---|---|
| Textos gerados sem acento, depois corrigidos por dicionário cego: "media" virou "média" e quebrou `@media` do CSS | Escrever os textos já acentuados. Nunca aplicar correção de acento no arquivo inteiro; se precisar, só em texto visível e nunca em CSS, JS ou dados de imagem |
| Passou em contraste no claro e falhou no escuro (botão destrutivo com texto branco, 2,77:1) | Conferir os dois temas e criar token de fundo "forte" separado do token de ícone e texto |
| `.btn` sobrescrevendo `display:none` do botão de menu no desktop | Testar o botão de menu em desktop e celular; usar seletor mais específico |
| Alvos de toque de 22 a 39 px contra a promessa de 44 px | Medir com `evaluate_script` em 375 px antes de afirmar no DESIGN.md |
| Cabeçalho fixo cortando o título da seção ao navegar | `scroll-margin-top` nas seções |
| Teste de cópia travou ao ler `navigator.clipboard.readText()` | Não ler a área de transferência no teste; checar o valor enviado e o aviso, e relatar como parcial |
| Valores do CSS fora do bloco de tokens | `grep` por hex fora do bloco; só a sobrescrita de impressão pode repetir valores |
