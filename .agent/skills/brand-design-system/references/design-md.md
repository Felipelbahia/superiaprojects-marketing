# DESIGN.md: formato

Arquivo exportável. Os valores vêm do `tokens.json`; texto de apoio vem das decisões e dos arquivos da marca.

## Front matter YAML (campos obrigatórios)

```yaml
---
name: Marca
description: uma frase do que é e da sensação visual
colors:
  light:
    bg: "#FFFFFF"
    text: "#16181A"
    # ... todos os tokens
  dark:
    bg: "#101214"
    text: "#ECEEEF"
typography:
  font-sans: "system-ui, -apple-system, 'Segoe UI', Roboto, sans-serif"
  scale:
    display: { size: 3rem, line: 1.1, weight: 700 }
rounded:
  sm: 4px
  md: 8px
spacing:
  "1": 4px
  "2": 8px
components:
  button-primary: { bg: primary, color: on-primary, radius: md }
---
```

Aspas em valores hex e em chaves numéricas, para o YAML não interpretar `#` como comentário nem números como inteiros.

## Seções, nesta ordem

1. **Overview**: o que a marca é, sensação (3 palavras), "não deve parecer", resumo das decisões e **tabela de origem** (decisão, valor, arquivo da marca que a motivou).
2. **Colors**: tabela por papel com claro, escuro e uso. Tabela de contraste dos pares conferidos, com razão e resultado.
3. **Typography**: famílias, escala, regras de uso, o que evitar.
4. **Layout**: grade, espaçamento, breakpoints, largura de leitura.
5. **Elevation**: níveis e como o tema escuro substitui sombra por superfície.
6. **Components**: os seis grupos, estados e tokens que usam.
7. **Imagery**: estilos travados (Style 01...), ou placeholder declarado.
8. **Responsive Behavior**: breakpoints, o que colapsa, alvos de toque (mínimo 44 px), comportamento da navegação lateral em celular.
9. **Known Gaps**: lista honesta do que falta ou diverge (conflitos com o `style-guide.md`, imagens ausentes, fontes sem licença confirmada, o que não foi verificado).

Também incluir, no fim da seção Overview, os ponteiros: `brand-voice.md`, `style-guide.md`, `brandbook.md`. A voz não é reescrita aqui.

## Regras

- Sem emoji, sem gradiente (exceto o permitido), sem enchimento.
- O mesmo texto está embutido no site (aba de download) e o botão salva exatamente esse conteúdo.
- Cada valor do front matter existe com o mesmo valor no CSS do site (conferido mecanicamente em `verificacao.md`).
