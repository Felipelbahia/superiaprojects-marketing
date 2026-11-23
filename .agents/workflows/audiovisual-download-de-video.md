---
name: audiovisual-download-de-video
description: Download YouTube videos with customizable quality and format options. Use this skill when the user asks to download, save, or grab YouTube videos. Supports various quality settings (best, 1080p, 720p, 480p, 360p), multiple formats (mp4, webm, mkv), and audio-only downloads as MP3.
---

# YouTube Video Downloader

Download YouTube videos with full control over quality and format settings, usando `yt-dlp` diretamente via linha de comando — sem script intermediário.

## Verificar instalação

```bash
which yt-dlp || brew install yt-dlp
```

## Quick Start

A forma mais simples de baixar um vídeo (melhor qualidade disponível, MP4):

```bash
yt-dlp -f "bv*+ba/b" --merge-output-format mp4 -o "%(title)s.%(ext)s" "https://www.youtube.com/watch?v=VIDEO_ID"
```

Por padrão, salva no diretório de trabalho atual (ou no caminho indicado pelo usuário — nunca em `/mnt/user-data/`, que é um caminho de sandbox que não existe neste Mac).

## Opções

### Qualidade

```bash
# 1080p
yt-dlp -f "bv*[height<=1080]+ba/b[height<=1080]" --merge-output-format mp4 -o "%(title)s.%(ext)s" "URL"

# 720p
yt-dlp -f "bv*[height<=720]+ba/b[height<=720]" --merge-output-format mp4 -o "%(title)s.%(ext)s" "URL"
```

### Formato de saída

```bash
# WebM
yt-dlp -f "bv*+ba/b" --merge-output-format webm -o "%(title)s.%(ext)s" "URL"

# Matroska (MKV)
yt-dlp -f "bv*+ba/b" --merge-output-format mkv -o "%(title)s.%(ext)s" "URL"
```

### Só áudio (MP3)

```bash
yt-dlp -x --audio-format mp3 -o "%(title)s.%(ext)s" "URL"
```

### Diretório de saída

```bash
yt-dlp -f "bv*+ba/b" --merge-output-format mp4 -o "/caminho/do/usuario/%(title)s.%(ext)s" "URL"
```

## Exemplos completos

1. Vídeo em 1080p como MP4:
```bash
yt-dlp -f "bv*[height<=1080]+ba/b[height<=1080]" --merge-output-format mp4 -o "%(title)s.%(ext)s" "https://www.youtube.com/watch?v=dQw4w9WgXcQ"
```

2. Só áudio como MP3:
```bash
yt-dlp -x --audio-format mp3 -o "%(title)s.%(ext)s" "https://www.youtube.com/watch?v=dQw4w9WgXcQ"
```

## Observações importantes

- O nome do arquivo é gerado automaticamente a partir do título do vídeo.
- Por padrão, só o vídeo pedido é baixado (playlists inteiras não são baixadas, a menos que o usuário peça explicitamente).
- Vídeos de qualidade mais alta demoram mais e usam mais espaço em disco.
- Se `yt-dlp` não estiver instalado, instalar com `brew install yt-dlp` (ou `pip3 install yt-dlp` em outros sistemas), com autorização do usuário.
