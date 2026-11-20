# 5a. Moldes de canais: arquivos-base para Instagram, LinkedIn, e-mail e YouTube

Complementa o capítulo 5 (aplicações). O capítulo 5 decide **onde** a marca aparece; este diz **como começar** cada peça de canal com um arquivo-base que já respeita tamanho, margem e campos editáveis. Os moldes são neutros (fundo branco, uma cor de destaque, Arial) e só viram da marca depois que recebem as cores, a fonte e o logo aprovados.

*Ideia adaptada da skill `templates-canais` do Brandfy (Promovaweb, AGPL-3.0). Os desenhos, os textos e os limites medidos aqui são próprios; nenhum arquivo foi copiado.*

## 5a.1 O que vem pronto

Seis SVG em `assets/moldes-de-canais/` (na pasta do `brand-builder`):

| Molde | Tamanho do molde | Exportar em | Para quê |
|---|---|---|---|
| `instagram-carrossel-capa.svg` | 1080 × 1350 px (4:5) | 1080 × 1350 | primeira lâmina do carrossel |
| `instagram-carrossel-miolo.svg` | 1080 × 1350 px (4:5) | 1080 × 1350 | lâminas do meio (uma ideia por lâmina) |
| `linkedin-quadrado.svg` | 1200 × 1200 px (1:1) | 1200 × 1200 | imagem de post |
| `email-cabecalho.svg` | 1200 × 400 px | 1200 × 400, exibido a 600 × 200 | cabeçalho de e-mail |
| `youtube-miniatura.svg` | 1280 × 720 px (16:9) | **3840 × 2160** | miniatura de vídeo |
| `youtube-banner.svg` | 2560 × 1440 px (16:9) | 2560 × 1440 | banner do canal |

## 5a.2 Medidas, margens e de onde vêm

Consultado em 2026-11-19. "Oficial" é a página de ajuda da própria plataforma; "terceiros" são guias de mercado, que divergem em detalhes. O que não tem fonte oficial fica `[a confirmar]` até alguém conferir na ajuda da plataforma.

| Canal | Medida | Margem do molde | Fonte e estado |
|---|---|---|---|
| Instagram, carrossel | 1080 × 1350 px, 4:5; todas as lâminas na mesma proporção da primeira | 90 px | **Oficial** para a faixa aceita: a [ajuda de resolução do Instagram](https://help.instagram.com/1631821640426723) mantém a foto original com largura de 320 a 1080 px e proporção de 1,91:1 a 3:4 (1080 de largura com altura de 566 a 1440 px); o 4:5 cai dentro dela. Terceiros ([Linearity](https://www.linearity.io/templates/instagram-size-guide), [HeyOrca](https://heyorca.com/blog/instagram-media-specs-best-practices-2026)) para a escolha de 1080 × 1350 e para a regra de proporção única entre lâminas, que seguem `[a confirmar]`. |
| Instagram, grade do perfil | a grade mostra a miniatura em 3:4; terceiros divergem sobre o que é cortado (topo e base ou laterais) | a guia do molde marca o recorte lateral central de 3:4 (cerca de 34 px de cada lado em 1080 × 1350, conta feita a partir das proporções); a margem de 90 px fica fora dele | Terceiros. A ajuda oficial só diz que a proporção aceita vai até 3:4; como a grade corta, `[a confirmar]` |
| LinkedIn, imagem | Post orgânico: mínimo 552 × 276 px, 1080 px de largura recomendados, proporção de 3:1 a 4:5, 5 MB; o 1200 × 1200 (1:1) cabe na faixa. Anúncio de imagem única: 1200 × 1200, 1200 × 628 e 720 × 900; post de página com link usa 1,91:1 (1200 × 627) | 100 px | **Oficial** nos três casos: post orgânico ([compartilhar fotos](https://www.linkedin.com/help/linkedin/answer/a527229), página marcada como atualizada há 2 anos, conferir se mudou), anúncio ([ajuda de anúncios](https://www.linkedin.com/help/lms/answer/a423644)) e post de página ([ajuda de páginas](https://www.linkedin.com/help/linkedin/answer/a563309)) |
| E-mail, cabeçalho | corpo de 600 px de largura é convenção, não norma; exportar a imagem em 2× (1200 px) para telas de alta densidade; alguns construtores usam outra largura (um deles, 660 px) | metade central de 600 px guarda a mensagem principal | Terceiros ([Mailtrap](https://mailtrap.io/blog/email-template-size/), [Zoho](https://www.zoho.com/zeptomail/articles/email-template-size.html)). Conferir a largura no programa de envio usado. `[a confirmar]` |
| YouTube, banner | recomendado 2560 × 1440 px (16:9); mínimo 2048 × 1152; zona segura **1235 × 338 px no tamanho mínimo** | zona segura de cerca de 1544 × 423 px no molde (conta nossa, proporcional: 1235/2048 × 2560 e 338/1152 × 1440) | **Oficial** ([ajuda do YouTube](https://support.google.com/youtube/answer/10456525)); a conta proporcional não está na ajuda |
| YouTube, miniatura | a ajuda recomenda 3840 × 2160 px para vídeos (2160 × 3840 para Shorts), com no mínimo 640 px de largura; o **1280 × 720 que circula aparece na ajuda do Google Ads como medida da miniatura em anúncios de vídeo**, não na ajuda de miniaturas do YouTube | 64 px (escolha do molde, não da plataforma) | **Oficial** ([ajuda de miniaturas](https://support.google.com/youtube/answer/72431), [especificações de anúncios](https://support.google.com/google-ads/answer/13547298)) |

O molde da miniatura é vetorial em 1280 × 720 (mesma proporção, 16:9); exportar em 3840 × 2160 segue a recomendação oficial.

## 5a.3 Limites de texto (medidos)

Medidos no Chrome, com Arial (negrito nos títulos), em texto corrido em português. Letras largas (`m`, `w`, maiúsculas) reduzem o limite pela metade no pior caso. Com a fonte da marca, **medir de novo**.

| Campo | Caracteres por linha (com 10% de folga) | Pior caso medido (só `m`) |
|---|---|---|
| Carrossel, capa: título (78 px) | 20 | 12 |
| Carrossel, capa: apoio (36 px) | 46 | 30 |
| Carrossel, miolo: título (68 px) | 23 | 14 |
| Carrossel, miolo: corpo (40 px) | 40 | 27 |
| LinkedIn: título (84 px) | 20 | 12 |
| LinkedIn: apoio (40 px) | 43 | 28 |
| E-mail: título (64 px) | 29 | 18 |
| Miniatura: palavra-chave (120 px) | 10 | 6 |
| Miniatura: apoio (48 px) | 26 | 17 |
| Banner: nome ou promessa (110 px) | 23 | 14 |
| Banner: apoio (52 px) | 51 | 33 |

## 5a.4 Como usar

1. **Copiar** o molde para a pasta da marca (por exemplo `ativacao/moldes/`) e trabalhar na cópia. O original da skill não se altera.
2. **Trocar o bloco `<style>`** do topo pelas cores e pela fonte do `design-system/tokens.json` da marca.
3. **Pôr o logo no grupo `logo-slot`** (SVG mestre aprovado, na versão certa para o fundo). Na exportação (passo 6), `--logo` faz isso sozinho: o logo entra escalado dentro da caixa tracejada, sem distorcer. Nunca reconstruir o logo com texto, esticar ou recolorir.
4. **Preencher os campos** `{{...}}`: um `<text>` por linha, respeitando a tabela 5a.3. Cada molde tem uma ideia principal por peça. Se o título usa menos linhas que o molde, apagar as linhas que sobram e subir o texto de apoio para cerca de 90 px abaixo da última linha usada, senão sobra um vazio no meio.
5. **Ver as guias:** tirar `display="none"` do grupo `guides` (margem, zona segura, recorte). **Apagar o grupo antes de exportar.**
6. **Exportar** em PNG com o script do logo, no tamanho da tabela 5a.1:

```bash
# a partir da pasta do brand-builder
python3 scripts/brand_logo_assets.py render <raiz da marca> <raiz da marca>/ativacao/moldes/youtube-miniatura.svg --width 3840 --logo <raiz da marca>/logo/svg/logo.svg
```

   `--logo` e o SVG de saída precisam ficar dentro da pasta da marca. Sem `--logo`, a caixa tracejada "LOGO" aparece na imagem.

   Sem `--out`, o PNG sai ao lado do SVG (que precisa estar dentro da pasta da marca), com o nome `<molde>-<largura>.png` (por exemplo `youtube-miniatura-3840.png`) e com o fundo do molde (retângulo `.bg`, opaco). Para uma peça com fundo transparente, apagar esse retângulo antes.
7. **Conferir no tamanho real de consumo** (feed no celular, caixa de entrada, lista de recomendados): texto pequeno, margem invadida, contraste ruim e logo na versão errada aparecem aí.

## 5a.5 Limites e cuidados

- **Fonte:** o SVG é desenhado como imagem, então a fonte tem de estar **instalada na máquina** que exporta (ou o texto convertido em curvas). Uma webfont do `fonts.css` não é carregada nesse caminho.
- **Fotografia:** usar só imagem autorizada e anotar a origem (capítulo 4). Os campos de imagem dos moldes são só uma caixa tracejada.
- **Contraste:** conferir depois de rasterizar, com os pares aprovados no capítulo 2.
- **Fonte e exportação em pastas diferentes:** guardar o SVG editável e o PNG final separados, para o PNG nunca ser editado no lugar do SVG.
- **Onde fica a peça final:** o molde da marca vive em `ativacao/moldes/`; a **peça pronta** (um post, uma miniatura) vai ao destino do `docs/mapa-de-destinos.md`, nunca à pasta da marca. Projeto sem mapa: parar e propor o mapa ao dono (skill `mapa-de-destinos`), sem inventar pasta; até lá, o PNG fica ao lado do molde e a pendência vai para as lacunas.
- **Testar o molde antes de aprovar:** título curto e longo, sem imagem, foto clara e escura, recorte no celular, outro idioma se a marca usa. Se o molde só fica bonito com o texto e a foto que o autor escolheu, ele ainda não serve para o resto da equipe.

## 5a.6 Saída deste capítulo

Na seção "Aplicações" do `identidade-e-ativos.md`: quais moldes a marca usa, onde estão as cópias, as cores e a fonte aplicadas e a data em que cada medida foi conferida.
