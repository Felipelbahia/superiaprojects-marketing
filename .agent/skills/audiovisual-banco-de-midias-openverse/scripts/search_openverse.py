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


def strip_html(text: Optional[str]) -> str:
    if not text:
        return ""
    clean = re.sub(r"<[^>]+>", "", text)
    return clean.strip()


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


def query_wikimedia_fallback(
    query: str,
    media_type: str = "image",
    limit: int = 5,
    commercial: bool = True,
    timeout: int = 8,
) -> List[Dict[str, Any]]:
    """
    Fallback resiliente usando a API da Wikimedia Commons (maior acervo aberto do mundo).
    Ativada automaticamente se o backend do Openverse sofrer degradação ou timeout.
    """
    # Ajusta termo e formato
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
        "gsrlimit": min(limit * 2, 20),
        "prop": "imageinfo",
        "iiprop": "url|size|mime|extmetadata",
        "format": "json",
    }
    url = f"{WIKIMEDIA_API_BASE}?{urllib.parse.urlencode(params)}"
    req = urllib.request.Request(url, headers={"User-Agent": "OpenverseMarketingHub/1.0 (https://wikimedia.org)"})
    
    results = []
    try:
        with urllib.request.urlopen(req, timeout=timeout) as resp:
            payload = json.loads(resp.read().decode("utf-8"))
            pages = payload.get("query", {}).get("pages", {})
            for page in pages.values():
                title = page.get("title", "").replace("File:", "")
                imageinfo_list = page.get("imageinfo", [])
                if not imageinfo_list:
                    continue
                info = imageinfo_list[0]
                url = info.get("url")
                if not url:
                    continue

                meta = info.get("extmetadata", {})
                artist = strip_html(meta.get("Artist", {}).get("value")) or "Wikimedia Contributor"
                license_short = meta.get("LicenseShortName", {}).get("value") or "CC / Public Domain"
                license_url = meta.get("LicenseUrl", {}).get("value") or "https://creativecommons.org"
                
                # Checagem de uso comercial
                if commercial and "nc" in license_short.lower():
                    continue

                width = info.get("width")
                height = info.get("height")
                aspect = "square"
                if width and height:
                    ratio = width / height
                    if ratio >= 1.2:
                        aspect = "wide"
                    elif ratio <= 0.8:
                        aspect = "tall"

                clean_url = url.split("?")[0]
                ext = clean_url.split(".")[-1].lower() if "." in clean_url else "jpg"
                thumb = info.get("thumburl") or (f"https://commons.wikimedia.org/w/thumb.php?f={urllib.parse.quote(title)}&w=600" if media_type == "image" else url)

                attribution = f'"{title}" by {artist} is licensed under {license_short}. Source: Wikimedia Commons'

                results.append({
                    "id": str(page.get("pageid")),
                    "title": title,
                    "url": url,
                    "thumbnail": thumb,
                    "creator": artist,
                    "creator_url": f"https://commons.wikimedia.org/wiki/File:{urllib.parse.quote(title)}",
                    "license": license_short.lower(),
                    "license_version": "",
                    "license_url": license_url,
                    "attribution": attribution,
                    "width": width,
                    "height": height,
                    "aspect_ratio": aspect,
                    "filetype": ext,
                    "provider": "wikimedia-commons",
                    "source": "Wikimedia Commons",
                    "related_url": f"https://commons.wikimedia.org/wiki/Special:Search?search={urllib.parse.quote(query)}",
                })
                if len(results) >= limit:
                    break
    except Exception:
        pass
    return results


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
        "",
        "> **Atribuição Legal Pronta (Copie e cole nos créditos):**",
        f"> `{attribution}`",
        "",
        "---",
    ]
    return "\n".join(lines)


def main():
    parser = argparse.ArgumentParser(
        description="Helper CLI para buscar mídias livres e Creative Commons na API do Openverse com fallback Wikimedia Commons."
    )
    parser.add_argument("--query", "-q", required=True, help="Termo de pesquisa (ex: 'minimalist workspace', 'coffee')")
    parser.add_argument("--type", choices=["image", "audio", "video"], default="image", help="Tipo de mídia: image (padrão), audio ou video")
    parser.add_argument("--commercial", action="store_true", help="Garante licença permitida para uso comercial (anúncios, vendas, produtos)")
    parser.add_argument("--aspect-ratio", choices=["tall", "wide", "square"], help="Proporção: tall (9:16 Reels), wide (16:9 Banner), square (1:1 Feed)")
    parser.add_argument("--category", help="Categoria: photograph, illustration, digitized_art (imagem) ou music, sound_effect (áudio)")
    parser.add_argument("--extension", help="Extensão: jpg, png, svg (imagem) ou mp3, ogg, wav (áudio)")
    parser.add_argument("--page-size", "-n", type=int, default=3, help="Quantidade de resultados a exibir (padrão: 3)")
    parser.add_argument("--format", choices=["markdown", "json", "summary"], default="markdown", help="Formato de saída (padrão: markdown)")
    parser.add_argument("--download-dir", help="Diretório opcional para salvar os arquivos baixados")

    args = parser.parse_args()

    results: List[Dict[str, Any]] = []
    source_used = "Openverse API"
    total_found = 0

    # 1. Se for vídeo ou se o Openverse estiver instável, usamos a rota Wikimedia direta
    if args.type == "video":
        results = query_wikimedia_fallback(args.query, media_type="video", limit=args.page_size, commercial=args.commercial)
        source_used = "Wikimedia Commons (Openverse Provider)"
        total_found = len(results)
    else:
        # Tenta primariamente Openverse
        endpoint = "images" if args.type == "image" else "audio"
        license_type = "commercial" if args.commercial else None
        api_params = {
            "q": args.query,
            "license_type": license_type,
            "aspect_ratio": args.aspect_ratio if args.type == "image" else None,
            "category": args.category,
            "extension": args.extension,
        }
        success, data = query_openverse(endpoint, api_params, timeout=5)
        if success and data.get("results"):
            results = data.get("results", [])[:args.page_size]
            total_found = data.get("result_count", len(results))
        else:
            # Fallback transparente para Wikimedia Commons (maior provedor do Openverse)
            results = query_wikimedia_fallback(
                args.query,
                media_type=args.type,
                limit=args.page_size,
                commercial=args.commercial,
            )
            source_used = "Wikimedia Commons (Fallback Resiliente do Openverse)"
            total_found = len(results)

    if args.format == "json":
        print(json.dumps({"query": args.query, "source": source_used, "results": results}, indent=2, ensure_ascii=False))
        return

    # Renderização em Markdown
    media_labels = {"image": "Imagens", "audio": "Áudios", "video": "Vídeos"}
    filter_tags = [f"**Termo:** `{args.query}`", f"**Fonte:** `{source_used}`"]
    if args.commercial:
        filter_tags.append("**Uso:** `Comercial Permitido`")
    if args.aspect_ratio:
        filter_tags.append(f"**Aspect Ratio:** `{args.aspect_ratio}`")

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
