#!/usr/bin/env python3
"""
search_openverse.py - Helper CLI para consulta à API pública do Openverse (WordPress.org)
com Fallback Resiliente Automático via Wikimedia Commons Open API.

Repositório Oficial do Openverse: https://github.com/WordPress/openverse
Documentação Técnica: https://docs.openverse.org

Indexa centenas de milhões de mídias sob licenças Creative Commons e Domínio Público.
Zero dependências externas: 100% biblioteca padrão do Python (urllib, json, argparse).
"""

import argparse
import html
import json
import os
import re
import sys
import urllib.error
import urllib.parse
import urllib.request
from typing import Any, Dict, List, Optional, Tuple

OPENVERSE_API_BASE = "https://api.openverse.org/v1"
WIKIMEDIA_API_BASE = "https://commons.wikimedia.org/w/api.php"
USER_AGENT = "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/124.0.0.0 Safari/537.36"
# Wikimedia rejeita User-Agent que imita navegador sem contato; usar identificação honesta.
COMMONS_USER_AGENT = "OpenverseMarketingHub/1.0 (https://wikimedia.org)"
EXT_ALIASES = {"jpeg": "jpg", "oga": "ogg"}


def strip_html(text: Optional[str]) -> str:
    if not text:
        return ""
    clean = re.sub(r"<[^>]+>", "", text)
    return html.unescape(clean).strip()


def _meta_value(meta: Dict[str, Any], key: str) -> str:
    entry = meta.get(key) or {}
    if not isinstance(entry, dict):
        return ""
    return entry.get("value") or ""


def is_non_commercial(license_name: str) -> bool:
    normalized = license_name.lower().replace("-", " ")
    return "nc" in normalized.split() or "noncommercial" in normalized.replace(" ", "")


def compute_aspect(width: Optional[int], height: Optional[int]) -> Optional[str]:
    """Proporção calculada a partir das dimensões; None quando as dimensões são desconhecidas."""
    if not width or not height:
        return None
    ratio = width / height
    if ratio >= 1.2:
        return "wide"
    if ratio <= 0.8:
        return "tall"
    return "square"


def passes_filters(item: Dict[str, Any], aspect_ratio: Optional[str], min_width: Optional[int]) -> bool:
    width = item.get("width")
    if min_width is not None and width is not None and width < min_width:
        return False
    if aspect_ratio and item.get("aspect_ratio") != aspect_ratio:
        return False
    return True


def query_openverse(endpoint: str, params: Dict[str, Any], timeout: int = 5) -> Tuple[bool, Dict[str, Any]]:
    filtered_params = {k: v for k, v in params.items() if v is not None and v != ""}
    qs = urllib.parse.urlencode(filtered_params)
    url = f"{OPENVERSE_API_BASE}/{endpoint}/?{qs}"
    req = urllib.request.Request(url, headers={"User-Agent": USER_AGENT, "Accept": "application/json"})
    try:
        with urllib.request.urlopen(req, timeout=timeout) as resp:
            data = json.loads(resp.read().decode("utf-8"))
            return True, data
    except Exception as e:
        return False, {"error": str(e)}


def commons_page_to_result(
    page: Dict[str, Any],
    media_type: str = "image",
    commercial: bool = True,
    related_term: str = "",
) -> Optional[Dict[str, Any]]:
    """Converte uma página da API do Commons (com imageinfo) no dicionário padrão de resultado."""
    title = (page.get("title") or "").removeprefix("File:")
    imageinfo_list = page.get("imageinfo") or []
    info = imageinfo_list[0] if imageinfo_list else {}
    raw_url = info.get("url")
    if not title or not raw_url:
        return None

    meta = info.get("extmetadata") or {}
    artist = strip_html(_meta_value(meta, "Artist")) or "Wikimedia Contributor"
    license_short = _meta_value(meta, "LicenseShortName") or "CC / Public Domain"
    license_url = _meta_value(meta, "LicenseUrl") or "https://creativecommons.org"

    if commercial and is_non_commercial(license_short):
        return None

    width = info.get("width")
    height = info.get("height")
    # Remove query string (ex.: ?utm_...) da URL do arquivo
    clean_url = raw_url.split("?")[0]
    file_name = clean_url.rsplit("/", 1)[-1]
    ext = file_name.rsplit(".", 1)[-1].lower() if "." in file_name else "jpg"
    thumb = info.get("thumburl") or (
        f"https://commons.wikimedia.org/w/thumb.php?f={urllib.parse.quote(title)}&w=600"
        if media_type == "image"
        else clean_url
    )
    attribution = f'"{title}" by {artist} is licensed under {license_short}. Source: Wikimedia Commons'

    return {
        "id": str(page.get("pageid")),
        "title": title,
        "url": clean_url,
        "thumbnail": thumb,
        "creator": artist,
        "creator_url": f"https://commons.wikimedia.org/wiki/File:{urllib.parse.quote(title)}",
        "license": license_short.lower(),
        "license_version": "",
        "license_url": license_url,
        "attribution": attribution,
        "width": width,
        "height": height,
        "aspect_ratio": compute_aspect(width, height),
        "filetype": ext,
        "provider": "wikimedia-commons",
        "source": "Wikimedia Commons",
        "related_url": f"https://commons.wikimedia.org/wiki/Special:Search?search={urllib.parse.quote(related_term)}",
    }


def query_wikimedia_fallback(
    query: str,
    media_type: str = "image",
    limit: int = 5,
    commercial: bool = True,
    timeout: int = 8,
    aspect_ratio: Optional[str] = None,
    min_width: Optional[int] = None,
) -> List[Dict[str, Any]]:
    """
    Busca no Wikimedia Commons (namespace 6, arquivos de mídia).
    Usada como fallback quando o Openverse falha e diretamente pelo modo --commons.
    A API do Commons não filtra por proporção, então os candidatos são pedidos em
    maior número e filtrados depois por aspect_ratio e min_width.
    """
    filetype_filter = ""
    if media_type == "audio":
        filetype_filter = " filetype:audio"
    elif media_type == "video":
        filetype_filter = " filetype:video"

    full_query = f"{query}{filetype_filter}"
    params = {
        "action": "query",
        "generator": "search",
        "gsrsearch": full_query,
        "gsrnamespace": "6",  # Namespace de Arquivos/Mídia
        "gsrlimit": min(max(limit * 4, 20), 50),
        "prop": "imageinfo",
        "iiprop": "url|size|mime|extmetadata",
        "format": "json",
    }
    url = f"{WIKIMEDIA_API_BASE}?{urllib.parse.urlencode(params)}"
    req = urllib.request.Request(url, headers={"User-Agent": COMMONS_USER_AGENT})

    results: List[Dict[str, Any]] = []
    try:
        with urllib.request.urlopen(req, timeout=timeout) as resp:
            payload = json.loads(resp.read().decode("utf-8"))
            pages = payload.get("query", {}).get("pages", {})
            # Mantém a ordem de relevância devolvida pela busca
            for page in sorted(pages.values(), key=lambda p: p.get("index", 0)):
                item = commons_page_to_result(page, media_type, commercial, related_term=query)
                if item is None or not passes_filters(item, aspect_ratio, min_width):
                    continue
                results.append(item)
                if len(results) >= limit:
                    break
    except Exception as e:
        print(f"aviso: falha na busca no Wikimedia Commons: {e}", file=sys.stderr)
    return results


def fetch_commons_file(
    title: str,
    media_type: str = "image",
    commercial: bool = True,
    aspect_ratio: Optional[str] = None,
    min_width: Optional[int] = None,
    timeout: int = 8,
) -> List[Dict[str, Any]]:
    """Metadados de um arquivo específico do Commons. Aceita o título com ou sem o prefixo 'File:'."""
    name = title.strip()
    if not name.lower().startswith("file:"):
        name = f"File:{name}"
    params = {
        "action": "query",
        "titles": name,
        "prop": "imageinfo",
        "iiprop": "url|size|mime|extmetadata",
        "format": "json",
    }
    url = f"{WIKIMEDIA_API_BASE}?{urllib.parse.urlencode(params)}"
    req = urllib.request.Request(url, headers={"User-Agent": COMMONS_USER_AGENT})
    try:
        with urllib.request.urlopen(req, timeout=timeout) as resp:
            payload = json.loads(resp.read().decode("utf-8"))
    except Exception as e:
        print(f"aviso: falha ao consultar o arquivo no Wikimedia Commons: {e}", file=sys.stderr)
        return []

    results: List[Dict[str, Any]] = []
    pages = payload.get("query", {}).get("pages", {})
    for page in pages.values():
        if "missing" in page or "invalid" in page:
            continue
        item = commons_page_to_result(page, media_type, commercial, related_term=name)
        if item and passes_filters(item, aspect_ratio, min_width):
            results.append(item)
    return results


def detect_real_filetype(head: bytes) -> Optional[str]:
    """Detecta o tipo real do arquivo pelos bytes iniciais (assinatura/magic bytes)."""
    if head.startswith(b"\xff\xd8\xff"):
        return "jpg"
    if head.startswith(b"\x89PNG"):
        return "png"
    if head.startswith(b"GIF8"):
        return "gif"
    if head[:4] == b"RIFF" and head[8:12] == b"WEBP":
        return "webp"
    if head[:4] == b"RIFF" and head[8:12] == b"WAVE":
        return "wav"
    stripped = head.lstrip()
    if stripped[:5].lower() == b"<?xml" or stripped[:4].lower() == b"<svg":
        return "svg"
    if head.startswith(b"ID3") or head[:2] in (b"\xff\xfb", b"\xff\xf3", b"\xff\xf2"):
        return "mp3"
    if head.startswith(b"OggS"):
        return "ogg"
    if head[4:8] == b"ftyp":
        return "mov" if head[8:12] == b"qt  " else "mp4"
    if head.startswith(b"\x1a\x45\xdf\xa3"):
        return "webm"
    return None


def safe_filename(title: str) -> str:
    stem = os.path.splitext(title)[0]
    cleaned = re.sub(r"[^A-Za-z0-9._-]+", "_", stem).strip("._")[:80]
    return cleaned or "arquivo"


def download_results(results: List[Dict[str, Any]], download_dir: str, timeout: int = 30) -> None:
    """Baixa cada resultado para download_dir, com extensão pelo tipo real. Erros vão para stderr."""
    abs_dir = os.path.abspath(download_dir)
    os.makedirs(abs_dir, exist_ok=True)
    for idx, item in enumerate(results, start=1):
        url = item.get("url")
        if not url:
            continue
        title = item.get("title") or f"arquivo-{idx}"
        url_ext = url.split("?")[0].rsplit("/", 1)[-1]
        url_ext = url_ext.rsplit(".", 1)[-1].lower() if "." in url_ext else ""
        url_ext = EXT_ALIASES.get(url_ext, url_ext)
        try:
            req = urllib.request.Request(url, headers={"User-Agent": COMMONS_USER_AGENT})
            with urllib.request.urlopen(req, timeout=timeout) as resp:
                data = resp.read()
        except Exception as e:
            print(f"erro ao baixar '{title}': {e}", file=sys.stderr)
            continue

        real_ext = detect_real_filetype(data[:64])
        if real_ext is None:
            print(f"aviso: {title} sem assinatura conhecida; salvo com a extensão da URL", file=sys.stderr)
            save_ext = url_ext or "bin"
            real_filetype = None
        else:
            save_ext = real_ext
            real_filetype = real_ext
            if url_ext and url_ext != real_ext:
                print(f"aviso: {title} veio como {real_ext}, extensão corrigida", file=sys.stderr)

        path = os.path.join(abs_dir, f"{idx:02d}-{safe_filename(title)}.{save_ext}")
        try:
            with open(path, "wb") as fh:
                fh.write(data)
        except OSError as e:
            print(f"erro ao gravar '{title}': {e}", file=sys.stderr)
            continue
        item["local_path"] = path
        item["real_filetype"] = real_filetype


def _one_line(text: Any) -> str:
    return " ".join(str(text).split())


def local_file_lines(item: Dict[str, Any]) -> List[str]:
    path = item.get("local_path")
    return [f"- **Arquivo local:** {path}"] if path else []


def render_markdown_image(item: Dict[str, Any], index: int) -> str:
    title = item.get("title") or "Sem título"
    url = item.get("url") or "#"
    thumb = item.get("thumbnail") or item.get("url")
    creator = item.get("creator") or "Desconhecido"
    creator_url = item.get("creator_url")
    creator_md = f"[{creator}]({creator_url})" if creator_url else creator
    license_name = (item.get("license") or "N/A").upper()
    license_url = item.get("license_url")
    license_md = f"[{license_name}]({license_url})" if license_url else license_name

    attribution = item.get("attribution") or f'"{title}" by {creator} is licensed under {license_name}'
    width = item.get("width")
    height = item.get("height")
    dimensions = f"{width} × {height} px" if width and height else "Alta resolução"
    filetype = (item.get("filetype") or "IMG").upper()
    provider = item.get("provider") or item.get("source") or "Openverse"
    related_url = item.get("related_url") or ""

    lines = [
        f"### {index}. [{title}]({url})",
        "",
        f"![{title}]({thumb})",
        "",
        f"- **Dimensões:** {dimensions} (`{filetype}`)",
        f"- **Autor:** {creator_md}",
        f"- **Provedor / Fonte:** `{provider}`",
        f"- **Licença:** {license_md}",
        f"- **Arquivo em Alta Resolução:** [Download Original]({url})",
        *local_file_lines(item),
    ]
    if related_url:
        lines.append(f"- **Mídias Semelhantes:** [Buscar Similares]({related_url})")
    lines.extend([
        "",
        "> **Atribuição Legal Pronta (Copie e cole nos créditos):**",
        f"> `{attribution}`",
        "",
        "---",
    ])
    return "\n".join(lines)


def render_markdown_audio(item: Dict[str, Any], index: int) -> str:
    title = item.get("title") or "Faixa de Áudio"
    url = item.get("url") or "#"
    creator = item.get("creator") or "Desconhecido"
    creator_url = item.get("creator_url")
    creator_md = f"[{creator}]({creator_url})" if creator_url else creator
    license_name = (item.get("license") or "N/A").upper()
    license_url = item.get("license_url")
    license_md = f"[{license_name}]({license_url})" if license_url else license_name
    attribution = item.get("attribution") or f'"{title}" by {creator} is licensed under {license_name}'
    filetype = (item.get("filetype") or "AUDIO").upper()
    provider = item.get("provider") or "Openverse"

    lines = [
        f"### {index}. 🎵 [{title}]({url})",
        "",
        f"- **Formato:** `{filetype}` | **Provedor:** `{provider}`",
        f"- **Autor:** {creator_md}",
        f"- **Licença:** {license_md}",
        f"- **Link Direto:** [Ouvir / Baixar Arquivo]({url})",
        *local_file_lines(item),
        "",
        "> **Atribuição Legal Pronta (Copie e cole nos créditos):**",
        f"> `{attribution}`",
        "",
        "---",
    ]
    return "\n".join(lines)


def render_markdown_video(item: Dict[str, Any], index: int) -> str:
    title = item.get("title") or "Vídeo Creative Commons"
    url = item.get("url") or "#"
    creator = item.get("creator") or "Desconhecido"
    creator_url = item.get("creator_url")
    creator_md = f"[{creator}]({creator_url})" if creator_url else creator
    license_name = (item.get("license") or "N/A").upper()
    license_url = item.get("license_url")
    license_md = f"[{license_name}]({license_url})" if license_url else license_name
    attribution = item.get("attribution") or f'"{title}" by {creator} is licensed under {license_name}'
    filetype = (item.get("filetype") or "VIDEO").upper()
    provider = item.get("provider") or "Wikimedia Commons"

    lines = [
        f"### {index}. 🎬 [{title}]({url})",
        "",
        f"- **Formato:** `{filetype}` | **Provedor:** `{provider}`",
        f"- **Autor:** {creator_md}",
        f"- **Licença:** {license_md}",
        f"- **Arquivo de Vídeo Original:** [Baixar / Assistir Vídeo]({url})",
        *local_file_lines(item),
        "",
        "> **Atribuição Legal Pronta (Copie e cole nos créditos):**",
        f"> `{attribution}`",
        "",
        "---",
    ]
    return "\n".join(lines)


def render_summary(results: List[Dict[str, Any]], source: str) -> str:
    """Uma linha por item, precedida de um cabeçalho com a fonte e a contagem."""
    lines = [f"# {source} — {len(results)} resultado(s)"]
    for idx, item in enumerate(results, start=1):
        width = item.get("width")
        height = item.get("height")
        dims = f"{width}x{height}" if width and height else "n/d"
        fields = [
            _one_line(item.get("title") or "Sem título"),
            dims,
            item.get("aspect_ratio") or "n/d",
            item.get("license") or "n/d",
            _one_line(item.get("creator") or "Desconhecido"),
            item.get("url") or "n/d",
        ]
        lines.append(f"{idx}. " + " | ".join(fields))
    return "\n".join(lines)


def main():
    parser = argparse.ArgumentParser(
        description="Helper CLI para buscar mídias livres e Creative Commons na API do Openverse com fallback Wikimedia Commons."
    )
    parser.add_argument("--query", "-q", help="Termo de pesquisa (ex: 'minimalist workspace', 'coffee')")
    parser.add_argument("--type", choices=["image", "audio", "video"], default="image", help="Tipo de mídia: image (padrão), audio ou video")
    parser.add_argument("--commercial", action="store_true", help="Garante licença permitida para uso comercial (anúncios, vendas, produtos)")
    parser.add_argument("--aspect-ratio", choices=["tall", "wide", "square"], help="Proporção: tall (9:16 Reels), wide (16:9 Banner), square (1:1 Feed)")
    parser.add_argument("--category", help="Categoria: photograph, illustration, digitized_art (imagem) ou music, sound_effect (áudio)")
    parser.add_argument("--extension", help="Extensão: jpg, png, svg (imagem) ou mp3, ogg, wav (áudio)")
    parser.add_argument("--page-size", "-n", type=int, default=3, help="Quantidade de resultados a exibir (padrão: 3)")
    parser.add_argument("--min-width", type=int, metavar="N", help="Descarta resultados com largura menor que N px (quando a largura é conhecida)")
    parser.add_argument("--commons", action="store_true", help="Busca direta no Wikimedia Commons, sem consultar o Openverse")
    parser.add_argument("--commons-file", metavar="TITLE", help="Metadados de um arquivo específico do Commons (ex: 'File:Nome.jpg'; o prefixo File: é opcional)")
    parser.add_argument("--format", choices=["markdown", "json", "summary"], default="markdown", help="Formato de saída (padrão: markdown)")
    parser.add_argument("--download-dir", help="Diretório opcional para baixar os arquivos encontrados (extensão pelo tipo real)")

    args = parser.parse_args()

    if not args.query and not args.commons_file:
        parser.error("informe --query/-q ou --commons-file")
    if args.min_width is not None and args.min_width < 0:
        parser.error("--min-width deve ser maior ou igual a 0")
    if args.page_size < 1:
        parser.error("--page-size deve ser maior ou igual a 1")

    aspect = args.aspect_ratio
    if args.type == "audio" and aspect:
        print("aviso: --aspect-ratio não se aplica a áudio; ignorado.", file=sys.stderr)
        aspect = None

    query_label = args.commons_file or args.query
    results: List[Dict[str, Any]] = []
    source_used = "Openverse API"
    total_found = 0

    if args.commons_file:
        results = fetch_commons_file(
            args.commons_file,
            media_type=args.type,
            commercial=args.commercial,
            aspect_ratio=aspect,
            min_width=args.min_width,
        )
        source_used = "Wikimedia Commons (arquivo)"
        total_found = len(results)
    elif args.commons or args.type == "video":
        # Modo direto (--commons) ou vídeo, que sempre usa o Commons
        results = query_wikimedia_fallback(
            args.query,
            media_type=args.type,
            limit=args.page_size,
            commercial=args.commercial,
            aspect_ratio=aspect,
            min_width=args.min_width,
        )
        source_used = "Wikimedia Commons (busca direta)" if args.commons else "Wikimedia Commons (Openverse Provider)"
        total_found = len(results)
    else:
        endpoint = "images" if args.type == "image" else "audio"
        api_params = {
            "q": args.query,
            "license_type": "commercial" if args.commercial else None,
            "aspect_ratio": aspect,
            "category": args.category,
            "extension": args.extension,
            # Anonymous Openverse requests accept at most 20 items per page
            "page_size": 20,
        }
        success, data = query_openverse(endpoint, api_params, timeout=5)
        candidates: List[Dict[str, Any]] = []
        if success and data.get("results"):
            for item in data["results"]:
                # The API already filtered by aspect ratio; keep the requested label
                item["aspect_ratio"] = aspect or compute_aspect(item.get("width"), item.get("height"))
            candidates = [it for it in data["results"] if passes_filters(it, None, args.min_width)]
        if candidates:
            results = candidates[:args.page_size]
            total_found = data.get("result_count", len(results))
            source_used = "Openverse API"
        else:
            print("aviso: Openverse indisponível ou sem resultados; usando Wikimedia Commons.", file=sys.stderr)
            results = query_wikimedia_fallback(
                args.query,
                media_type=args.type,
                limit=args.page_size,
                commercial=args.commercial,
                aspect_ratio=aspect,
                min_width=args.min_width,
            )
            source_used = "Wikimedia Commons (Fallback Resiliente do Openverse)"
            total_found = len(results)

    if args.download_dir and results:
        download_results(results, args.download_dir)

    if args.format == "json":
        payload = {
            "query": query_label,
            "source": source_used,
            "aspect_ratio_requested": aspect,
            "results": results,
        }
        print(json.dumps(payload, indent=2, ensure_ascii=False))
        return

    if args.format == "summary":
        print(render_summary(results, source_used))
        return

    # Renderização em Markdown
    media_labels = {"image": "Imagens", "audio": "Áudios", "video": "Vídeos"}
    filter_tags = [f"**Termo:** `{query_label}`", f"**Fonte:** `{source_used}`"]
    if args.commercial:
        filter_tags.append("**Uso:** `Comercial Permitido`")
    if aspect:
        filter_tags.append(f"**Aspect Ratio:** `{aspect}`")
    if args.min_width:
        filter_tags.append(f"**Largura mínima:** `{args.min_width}px`")

    print(f"## 🌐 Media Search: {media_labels.get(args.type, 'Mídia')}")
    print(f"{' | '.join(filter_tags)}")
    print(f"**Arquivos Encontrados:** {total_found:,} disponíveis (Exibindo {len(results)})\n")

    if not results:
        print("⚠️ Nenhuma mídia encontrada com os filtros selecionados. Tente usar termos em inglês (ex: 'office desk', 'ambient synth').")
        return

    for idx, item in enumerate(results, start=1):
        if args.type == "image":
            print(render_markdown_image(item, idx))
        elif args.type == "audio":
            print(render_markdown_audio(item, idx))
        else:
            print(render_markdown_video(item, idx))


if __name__ == "__main__":
    main()
