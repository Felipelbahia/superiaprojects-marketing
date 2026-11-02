---
name: audiovisual-video-para-gif
description: Convert video clips to optimized GIFs with speed control, cropping, text overlays, and file size optimization. Create perfect GIFs for social media, documentation, and presentations.
---

# Video to GIF

Transforma trechos de vídeo em GIFs otimizados para redes sociais, documentação e apresentações, usando `ffmpeg` diretamente via linha de comando — sem script ou classe Python intermediária.

## Verificar instalação

```bash
which ffmpeg || brew install ffmpeg
```

## Conversão básica

```bash
ffmpeg -i video.mp4 -vf "fps=15,scale=480:-1:flags=lanczos" output.gif
```

## Selecionar um trecho (clip)

```bash
# De 5s a 15s (usar -ss antes de -i para corte rápido)
ffmpeg -ss 5 -to 15 -i video.mp4 -vf "fps=15,scale=480:-1:flags=lanczos" output.gif

# Por timestamp
ffmpeg -ss 00:01:30 -to 00:01:45 -i video.mp4 -vf "fps=15,scale=480:-1:flags=lanczos" output.gif
```

## Controle de velocidade

```bash
# 2x mais rápido
ffmpeg -i video.mp4 -vf "fps=15,scale=480:-1,setpts=0.5*PTS" output.gif

# Câmera lenta (metade da velocidade)
ffmpeg -i video.mp4 -vf "fps=15,scale=480:-1,setpts=2.0*PTS" output.gif

# Reverso
ffmpeg -i video.mp4 -vf "fps=15,scale=480:-1,reverse" output.gif
```

## Redimensionar e recortar

```bash
# Redimensionar por largura (mantém proporção)
ffmpeg -i video.mp4 -vf "fps=15,scale=480:-1:flags=lanczos" output.gif

# Recortar uma região (x, y, largura, altura)
ffmpeg -i video.mp4 -vf "crop=400:300:100:50,fps=15,scale=480:-1" output.gif

# Recortar para 16:9 ou quadrado — ajustar crop conforme o vídeo de origem
```

## Texto sobreposto

```bash
ffmpeg -i video.mp4 -vf "fps=15,scale=480:-1,drawtext=text='Hello World':fontcolor=white:fontsize=24:x=(w-text_w)/2:y=h-th-10" output.gif
```

Para texto só numa janela de tempo, usar `enable='between(t,0,3)'` dentro do filtro `drawtext`.

## Otimizar tamanho de arquivo

```bash
# Paleta otimizada (melhor qualidade por tamanho) — processo em duas etapas
ffmpeg -i video.mp4 -vf "fps=15,scale=480:-1:flags=lanczos,palettegen" palette.png
ffmpeg -i video.mp4 -i palette.png -lavfi "fps=15,scale=480:-1:flags=lanczos [x]; [x][1:v] paletteuse" output.gif

# FPS mais baixo = arquivo menor
ffmpeg -i video.mp4 -vf "fps=10,scale=320:-1:flags=lanczos" output.gif
```

Checar o tamanho final com `ls -lh output.gif`; se passar do limite da plataforma, reduzir FPS, largura ou duração e gerar de novo.

## Referência de tamanho por plataforma

| Plataforma | Limite típico | Largura sugerida |
|---|---|---|
| Twitter/X | 15 MB | 480px |
| Discord | 8 MB (sem Nitro) | 320-480px |
| Slack | 5 MB | 320-480px |

## Formatos suportados

- **Entrada:** MP4, MOV, AVI, MKV, WebM (qualquer formato que o `ffmpeg` leia)
- **Saída:** GIF animado; para extrair um frame único como imagem, usar `ffmpeg -i video.mp4 -ss 5.5 -vframes 1 frame.png`

## Limitações

- GIF não tem áudio (é uma limitação do formato, não desta skill).
- GIFs muito longos ou em alta resolução ficam pesados — preferir trechos curtos (até ~10s) para redes sociais.
- Cenas complexas podem mostrar banding de cor (paleta limitada a 256 cores); usar o processo de duas etapas com `palettegen`/`paletteuse` acima para melhor qualidade.
