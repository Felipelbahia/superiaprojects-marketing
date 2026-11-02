# Decisões de design

A skill decide; o usuário aprova no fim. Cada decisão registra sua origem (`06-direcao-visual.md`, essência ou voz). Marca com `style-guide.md` existente parte dele.

## Ordem

1. Paleta -> 2. Tipografia -> 3. Espaço -> 4. Forma -> 5. Elevação -> 6. Movimento -> 7. Componentes -> 8. Telas -> 9. Imagem.

## 1. Paleta

- Papéis semânticos: `bg`, `surface`, `surface-alt`, `border`, `text`, `text-muted`, `primary`, `on-primary`, `accent`, `on-accent`, `success`, `warning`, `danger`, `info`, `focus`.
- Partir da cor de marca existente (se houver) ou da direção (temperatura, saturação, contraste).
- Escala de neutros com leve tinta da cor dominante.
- **Dark mode:** definir cada papel, não inverter. Fundo escuro nunca preto puro por padrão; reduzir saturação de cores vivas; superfícies em degraus de luminosidade. Todo par é conferido (ver `tokens-e-contraste.md`).
- Cor de marca que falha como texto vira variante `-text` para uso em corpo, mantendo a original para fundos e ícones grandes.
- Gradiente: só se o `style-guide.md` já o usa; então tokenizar como `gradient-*` e registrar.

## 2. Tipografia

- Pilha de sistema por padrão; fonte própria só se existe no `style-guide.md` ou o usuário decidiu (e então com arquivo local ou licença).
- Escala modular com 8 a 9 degraus (display, h1-h4, body, small, caption, code). Linha de 1.4 a 1.6 para corpo, 1.05 a 1.2 para display. Comprimento de linha 60 a 75 caracteres.
- Tracking só em caixa alta e displays grandes.
- Casar com a voz: voz seca e precisa pede peso e espaçamento contidos; voz expressiva tolera contraste de tamanho maior.

## 3. Espaço

- Base de 4 px. Degraus: 4, 8, 12, 16, 24, 32, 48, 64, 96. Nomear (`space-1`...) e usar só estes.
- Densidade vem da escala visual (arejado x denso) da etapa 6.

## 4. Forma

- Raios: nenhum, pequeno, médio, grande, pílula (`radius-0` a `radius-full`). Escolher um caráter dominante (reto, suave, redondo) e ficar nele.
- Bordas e divisores: 1 px, cor `border`. Ênfase em 2 px.

## 5. Elevação

- Máximo 3 níveis. Sombras discretas no claro; no escuro, preferir diferença de superfície a sombra.
- Se o caráter é plano, elevação vira borda.

## 6. Movimento

- Durações: 100, 200, 320 ms. Curvas: `standard`, `enter`, `exit`.
- O que anima: feedback de interação, entrada de painel. O que não anima: texto de leitura.
- Respeitar `prefers-reduced-motion`.
- Alinhar com a seção "Movimento" da etapa 6 (também usada em vídeo).

## 7. Componentes

Seis grupos obrigatórios, cada um com estados (padrão, hover, foco, ativo, desabilitado, erro quando couber):
- **Botões:** primário, secundário, terciário/texto, destrutivo, ícone, tamanhos.
- **Tags:** neutra, status (sucesso, alerta, erro, info), removível.
- **Inputs:** texto, área, select, checkbox, radio, switch, com rótulo, ajuda e erro.
- **Cards:** básico, com mídia, com ação, estatístico.
- **Dados:** tabela, lista, gráfico simples (barra), indicador numérico, estado vazio.
- **Navegação:** barra superior, abas, breadcrumb, paginação, menu lateral.

## 8. Telas (Patterns)

3 a 4 telas realistas **do produto ou presença da marca**, definidas pelo que a marca é (ver Overview): para produto digital, telas do app; para mídia ou pessoa, página inicial, página de série/episódio, cartão de rede social, abertura de vídeo. Conteúdo de exemplo verossímil em português, rotulado como exemplo.

## 9. Imagem

- Com imagens anexadas: "Style 01", "Style 02"... Cada um com a imagem de referência, tabela de regras (luz, ângulo, paleta, tratamento, composição, o que nunca aparece) e prompt copiável: **uma frase de assunto + bloco de estilo fixo**.
- Sem anexos: placeholder honesto, descrevendo o que falta e o que fazer para preencher. Sem inventar estilos.

## Origem das decisões

Tabela no `DESIGN.md`: decisão, valor, origem (qual arquivo da marca motivou).

## Biblioteca de componentes: shadcn/ui (obrigatória, qualquer profundidade)
Os seis grupos acima (botões, tags, inputs, cards, dados, navegação) são montados com os componentes do shadcn/ui, e os tokens seguem os nomes do shadcn. Lista mínima, mapeamento e o que exige autorização: `shadcn.md`.
