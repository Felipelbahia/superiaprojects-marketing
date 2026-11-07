---
# Repository: https://github.com/Felipelbahia/superiaprojects-marketing
# Status: Customizada / Modificada localmente por Felipe Bahia
name: audiovisual-podcast-e-audio
description: "Use para pós-produção de áudio: edição, mixagem e masterização de podcasts, conformidade ACX de audiobooks, transcrição com Whisper, direção de locução e sound design. Gatilhos: \"masterizar podcast\", \"ACX\", \"audiobook\", \"locução\", \"limpar áudio\". NÃO use para logo sonoro e identidade de áudio da marca (use brand-identidade-sonora), para transcrição com ElevenLabs (use audiovisual-transcricao) nem para SEO de podcast (use seo-podcast)."
author: Antigravity Kit (0 Mkt) & Felipe Bahia (Futuro Mercado)
license: MIT
metadata:
  author: Antigravity Kit (0 Mkt) & Felipe Bahia (Futuro Mercado)
  version: 1.0.0
---
# Podcast & Audio Engineer - Diretrizes Operacionais

Esta skill orienta a engenharia, restauração, mixagem, masterização e automação de áudio para podcasts corporativos, videoaulas, audiobooks e identidades sonoras de marca, estabelecendo padrões técnicos rigorosos de sonoridade (LUFS), clareza vocal e transcrição fonética com IA.

---

## 🎯 Quando Usar
- Na pós-produção e masterização de episódios de podcasts e entrevistas remotas.
- Ao calibrar faixas vocais para atender aos requisitos técnicos de plataformas (Spotify, Apple Podcasts, YouTube, ACX/Audible).
- Ao fazer sonoplastia para vídeos de marca e filmes (sound design). Logo sonoro e sons de aplicativo: veja `brand-identidade-sonora`.
- Ao automatizar processos de corte, remoção de silêncio, normalização e export com Pydub e FFmpeg.
- Ao configurar pipelines de transcrição fonética automática com OpenAI Whisper e geração de legendas `.srt`.
- Ao dirigir locutores humanos (cadência, respiração, ênfase) em narração e audiobook.

## 🚫 Quando NÃO Usar
- Para identidade sonora de marca, logo sonoro e sons de interface (use `brand-identidade-sonora`).
- Para escolher ou gerar voz sintética a partir de texto (o guia vive no projeto de edição de vídeo, `Compartilhado/Edição de Vídeo com IA`).
- Para transcrever pela API paga do ElevenLabs (use `audiovisual-transcricao`).
- Para roteirização e concept de vídeo com IA (a skill `ai-video-creator` foi removida do 0 Mkt e vive no projeto de edição de vídeo (`Compartilhado/Edição de Vídeo com IA`)).
- Para SEO e palavras-chave de transcrições de podcasts (use `seo-podcast`).
- Para animações e renderizações de mídia via código (as skills de vídeo programático foram removidas do 0 Mkt e vivem no projeto de edição de vídeo (`Compartilhado/Edição de Vídeo com IA`)).

---

## 🎚️ 1. Padrões de Masterização e Sonoridade (Loudness Standards)

| Plataforma / Formato | Loudness Alvo (LUFS Integrado) | True Peak Máximo | Noise Floor Máximo |
|---|---|---|---|
| **Podcasts (Spotify, Apple)** | **-16 LUFS** (Estéreo) / **-19 LUFS** (Mono) | **-1.0 dBFS** | $< -55 \text{ dBFS}$ |
| **Audiobooks (Padrão ACX/Audible)** | **-18 a -23 LUFS** (RMS entre -18dB e -23dB) | **-3.0 dBFS** | $< -60 \text{ dBFS}$ |
| **YouTube Vídeo / Web** | **-14 LUFS** | **-1.0 dBFS** | $< -50 \text{ dBFS}$ |
| **Áudio para Mobile / Apps (SFX)** | **-12 a -16 LUFS** | **-0.5 dBFS** | Transparente |

---

## 🎙️ 2. A Cadeia de Processamento Vocal Padrão (Vocal Chain)

```mermaid
graph LR
    A[1. Gravação Bruta] --> B[2. De-Noise / Spectral Repair]
    B --> C[3. High-Pass Filter 80Hz & De-Esser]
    C --> D[4. EQ Cirúrgico: Remoção de Ressonâncias]
    D --> E[5. Compressão: Nivelamento de Dinâmica 3:1]
    E --> F[6. EQ Tonal: Presença e Brilho 3kHz-10kHz]
    F --> G[7. Limiter / True Peak Normalization]
```

---

## 🤖 3. Transcrição Avançada com OpenAI Whisper

### 3.1. Comando de Transcrição Otimizado para Português (CLI)
```bash
whisper input_audio.wav \
  --model large-v3 \
  --language pt \
  --output_format srt \
  --word_timestamps True \
  --temperature 0.0 \
  --initial_prompt "Este episódio aborda estratégias de marketing B2B, métricas SaaS, CAC e LTV da empresa [NOME DA MARCA]."
```
> **Aviso:** o comando `whisper` acima exige o Whisper instalado, e ele não está instalado neste projeto. Em vez dele, o transcritor local que funciona hoje está no projeto Listas (`Pessoal/Listas`): `scripts/transcribe.py` com faster-whisper no `.venv` dele (modelos tiny a medium já em `~/.cache/huggingface`). Uso: `cd "…/Pessoal/Listas" && .venv/bin/python scripts/transcribe.py <arquivo> --model medium --lang pt --out transcricao.txt`. O projeto de edição de vídeo tem o transcritor configurado, mas o `.venv` dele não tem o pacote (cai para o ElevenLabs Scribe, pago).

*Dica:* O uso de `--initial_prompt` ensina o modelo a reconhecer termos específicos do nicho e nomes próprios de marcas, prevenindo alucinações fonéticas.

---

## 🎧 4. Logotipo sonoro e sons de interface

O guia de logo sonoro (estrutura de ataque, assinatura melódica e cauda) e o de sons para apps estão em [brand-identidade-sonora](../brand-identidade-sonora/SKILL.md): [audio-logo-design](../brand-identidade-sonora/references/audio-logo-design.md) e [ux-sound-design](../brand-identidade-sonora/references/ux-sound-design.md).

---

## 🚀 5. Checklist de Qualidade de Masterização (Delivery Gate)

Antes de exportar os arquivos finais para distribuição RSS ou upload em plataformas:

- [ ] **Loudness Integrado Verificado:** Exatamente **-16.0 LUFS** (tolerância $\pm 0.5$ LUFS) para estéreo.
- [ ] **True Peak Limiter:** Limiter de pico real travado em **-1.0 dBTP** sem interações com o teto (zero inter-sample peaks).
- [ ] **Noise Floor Silencioso:** Ruído de fundo ambiental em trechos de silêncio $< -55 \text{ dBFS}$ sem cortes abruptos de noise gate.
- [ ] **Sibilância Controlada:** Picos de frequências agudas e sibilantes (5 kHz a 8 kHz) atenuados com De-Esser dinâmico.
- [ ] **Graves Limpos:** High-pass filter em 80 Hz aplicado em todas as trilhas vocais para eliminar ruídos de manuseio e vibração de mesa.
- [ ] **ID3 Tags & Metadados Embutidos:** Título do episódio, artista/marca, número de temporada/episódio e arte da capa (3000x3000px, RGB) inseridos no MP3.
- [ ] **Export Duplo Padronizado:** Arquivo `.wav` 24-bit/48kHz para arquivo mestre e `.mp3` 192kbps CBR estéreo para streaming.

---

### 5.1. Script de Automação de Normalização (Bash / FFmpeg)
```bash
# Normalização EBU R128 (-16 LUFS) em lote com FFmpeg
for file in *.wav; do
  ffmpeg -i "$file" -af loudnorm=I=-16:TP=-1.0:LRA=11 -ar 48000 -y "${file%.wav}_master.wav"
done
```
- **Taxa de Amostragem Obrigatória**: 48 kHz para vídeos e plataformas web; 44.1 kHz aceitável apenas para distribuição de música tradicional.

---

## 📚 6. Biblioteca de Referências Operacionais

Acesse os guias práticos presentes na subpasta [`references/`](references/):

| Arquivo de Referência | Conteúdo Técnico & Casos Práticos |
|---|---|
| [`audio-editing.md`](references/audio-editing.md) | Playbook de edição de voz, equalização paramétrica, compressão e redução de ruído espectral. |
| [`audiobook-production.md`](references/audiobook-production.md) | Manual de conformidade técnica rigorosa para plataformas ACX, Audible e Apple Books. |
| [`podcast-production.md`](references/podcast-production.md) | Fluxo de produção ponta a ponta: microfonação, gravação remota multicanal e publicação RSS. |
| [`remote-interview.md`](references/remote-interview.md) | Gravação remota com qualidade de estúdio: técnica double-ender e plataformas de gravação dedicadas, para podcast e mídia. |
| [`podcast-interview.md`](references/podcast-interview.md) | Roteiros de condução de entrevistas, pautas dinâmicas e engenharia de som com 2 ou mais participantes. |
| [`whisper-transcription.md`](references/whisper-transcription.md) | Guia completo de uso do Whisper: modelos (tiny a large-v3), prompts de contexto e export srt/vtt. |
| [`pydub-automation.md`](references/pydub-automation.md) | Scripts Python com biblioteca Pydub para automação de normalização e processamento em lote. |
| [`sound-design-film.md`](references/sound-design-film.md) | Princípios de sonoplastia cinematográfica, foley, camadas de ambiência e efeitos diegéticos. |
| [`voiceover-direction.md`](references/voiceover-direction.md) | Roteiros com marcações de respiração, ênfase dramática e ritmo para locutores profissionais. |

## Outras referências

- **[podcast-marketing-distribution.md](references/podcast-marketing-distribution.md)** — Planejar, produzir e divulgar um podcast.

## Fora desta skill

- Logo sonoro e sons de interface: [brand-identidade-sonora](../brand-identidade-sonora/SKILL.md).
- Escolha e localização de voz sintética: guias `voice-design` e `voice-localization` no projeto de edição de vídeo.
- Transcrição: o guia de modelos e legendas é [whisper-transcription.md](references/whisper-transcription.md); os guias de WhisperKit por URL foram arquivados porque mandavam rodar scripts que não existem.
