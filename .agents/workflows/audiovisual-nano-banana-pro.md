---
name: audiovisual-nano-banana-pro
description: Generate images using Google's Nano Banana Pro (gemini-3-pro-image-preview). Accepts text prompts and optionally images (for editing/transformation) as INPUT. Returns generated IMAGES as OUTPUT. Use when user asks to create, generate, edit, or draw images, infographics, visualizations, diagrams, charts, or illustrations. Excellent for data-accurate infographics and text rendering.
allowed-tools: Bash(curl:*), Write, Read
---

# Nano Banana Pro Image Generator

Generate images using Google's advanced Nano Banana Pro model (`gemini-3-pro-image-preview`).

> Versão corrigida em 2026-10-28 (E6): a versão anterior mandava rodar um script `generate_image.py` que nunca existiu neste repositório. **Esta versão não usa programa:** o agente chama a API Gemini direto por `curl` e salva a imagem recebida.

## Prerequisites

The user must have `GEMINI_API_KEY` environment variable set with a valid Google AI API key.

## Usage

Call the Gemini `generateContent` REST endpoint directly with the `gemini-3-pro-image-preview` model, passing the prompt (and, for editing, the reference image as inline base64 data). Decode the returned base64 image data and write it to the output path the user asked for.

```bash
curl -s "https://generativelanguage.googleapis.com/v1beta/models/gemini-3-pro-image-preview:generateContent?key=$GEMINI_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{
    "contents": [{
      "parts": [{"text": "<prompt>"}]
    }]
  }' | python3 -c "
import sys, json, base64
data = json.load(sys.stdin)
part = data['candidates'][0]['content']['parts'][0]
img = base64.b64decode(part['inlineData']['data'])
open('<output.png>', 'wb').write(img)
"
```

### Parameters (decididos pelo agente a partir do pedido do usuário, não flags de CLI)

| Parâmetro | Como aplicar |
|---|---|
| Prompt | Texto descrevendo a imagem ou a transformação desejada |
| Saída | Caminho decidido pelo agente a partir do contexto do pedido |
| Edição/referência | Para editar ou usar uma imagem de referência, inclua uma segunda `part` com `inlineData` (`mimeType` + `data` em base64 da imagem de entrada) ao lado do `text` |
| Proporção e resolução | Descreva no próprio prompt (ex.: "formato 9:16, vertical" ou "alta resolução") — o modelo não tem flag separada de aspect-ratio/size na chamada direta à API; ajustar via instrução textual |

### Exemplos de prompt

- Geração básica: `"Um pôr do sol sobre montanhas, foto realista"`
- Infográfico: `"Infográfico mostrando o ciclo da água com etapas rotuladas, formato vertical 9:16"`
- Edição: enviar a imagem original como `inlineData` + prompt `"Adicione um céu de pôr do sol a esta imagem"`
- Transformação de estilo: enviar a imagem + prompt `"Transforme isso em uma pintura em aquarela"`

## Model Capabilities

Nano Banana Pro excels at:
- **Accurate infographics** with real data (uses Google Search grounding)
- **Text rendering** in images
- **Image editing and transformation** from input images
- **Context-aware generation** using reference images for style, composition, or subject
- **Cartographic visualizations** and maps
- **Detailed instruction following**
- **Chain-of-thought reasoning** for complex visual tasks

## Output

A resposta da API vem em `candidates[0].content.parts[]`; a parte com imagem tem `inlineData.data` em base64 — decodifique e salve no caminho pedido. Se não houver imagem na resposta, relate ao usuário o texto de erro devolvido pela API em vez de inventar um resultado.
