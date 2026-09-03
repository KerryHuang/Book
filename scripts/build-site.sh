#!/bin/bash
# 建置或預覽 MkDocs 網站。
# 用法：bash scripts/build-site.sh build [site-dir]   → 輸出到 site-dir（預設 ./site）
#       bash scripts/build-site.sh serve              → 本機預覽 http://127.0.0.1:8000
# MkDocs 不允許 docs_dir 等於設定檔所在目錄，所以把 mkdocs.yml 複製到暫存目錄，
# 並把 docs_dir 改成 repo 的絕對路徑後再執行。
set -euo pipefail
ROOT="$(cd "$(dirname "$0")/.." && (pwd -W 2>/dev/null || pwd))"   # Git Bash 用 Windows 路徑，Linux 用一般路徑
MODE="${1:-build}"
SITE_DIR="${2:-$ROOT/site}"
TMP="$(mktemp -d)"
trap 'rm -rf "$TMP"' EXIT

sed "s|^docs_dir: .*|docs_dir: $ROOT|" "$ROOT/mkdocs.yml" > "$TMP/mkdocs.yml"

case "$MODE" in
  build) mkdocs build --strict --config-file "$TMP/mkdocs.yml" --site-dir "$SITE_DIR" ;;
  serve) mkdocs serve --config-file "$TMP/mkdocs.yml" ;;
  *) echo "未知模式：$MODE" >&2; exit 1 ;;
esac
