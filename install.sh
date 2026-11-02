#!/usr/bin/env bash
# ==============================================================================
# Super IA Projects - Marketing - One-Line Installer & Setup
# Futuro Mercado - www.futuromercado.com.br
# ==============================================================================

set -e

echo ""
echo "🚀 ==========================================================="
echo "    Super IA Projects - Marketing"
echo "    Extensão Oficial de Growth, Copywriting, SEO e Ads"
echo "    Por Felipe Bahia (Futuro Mercado)"
echo "    www.futuromercado.com.br | @felipelbahia"
echo "=============================================================="
echo ""

# 1. Checar Python
if ! command -v python3 &> /dev/null; then
    echo "❌ Python 3 não foi encontrado. Por favor, instale o Python 3 antes de continuar."
    exit 1
fi

echo "✅ Python 3 detectado."

# 2. Inicializar regras a partir do template se não existirem
if [ ! -f "CLAUDE.md" ]; then
    echo "📋 Criando CLAUDE.md a partir de CLAUDE.example.md..."
    cp CLAUDE.example.md CLAUDE.md
    echo "✅ CLAUDE.md criado com sucesso."
else
    echo "ℹ️  CLAUDE.md já existe, preservando seu arquivo local."
fi

# 3. Sincronizar Entrypoints (Claude Code, Antigravity, Cursor)
echo "🔗 Sincronizando symlinks para Claude Code e Cursor..."
python3 .agent/scripts/sync_entrypoints.py

# 4. Regenerar Catálogo Unificado
echo "📊 Gerando catálogo unificado (Markdown e HTML interativo)..."
python3 .agent/scripts/generate_catalog.py

echo ""
echo "🎉 ==========================================================="
echo "    Tudo pronto! Seu Super IA Projects - Marketing está ativo."
echo ""
echo "    Para explorar as 98 skills, 33 agentes e 114 workflows:"
echo "    👉 Abra o arquivo: .agent/catalog.html no seu navegador."
echo "=============================================================="
echo ""
