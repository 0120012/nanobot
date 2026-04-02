#!/usr/bin/env bash
set -euo pipefail

# Downloads ggml whisper models to /www/.cache/whisper.cpp by default
# Uses Hugging Face direct downloads (no whisper.cpp repo scripts required).

# Why: 默认落盘到数据盘目录，减少系统盘空间占用风险。
MODELS_DIR="${MODELS_DIR:-/www/.cache/whisper.cpp}"
mkdir -p "$MODELS_DIR"

BASE_URL="https://huggingface.co/ggerganov/whisper.cpp/resolve/main"
PINNED_SHA256_BASE="60ed5bc3dd14eea856493d334349b405782ddcaf0028d4b5df4088345fba2efe"

sha256_file() {
  local file="$1"
  if command -v sha256sum >/dev/null 2>&1; then
    sha256sum "$file" | awk '{print $1}'
    return 0
  fi

  if command -v shasum >/dev/null 2>&1; then
    shasum -a 256 "$file" | awk '{print $1}'
    return 0
  fi

  echo "Missing sha256 tool: need sha256sum or shasum" >&2
  return 1
}

expected_sha256_for_model() {
  local name="$1"
  local key
  key="$(echo "$name" | tr '[:lower:]-' '[:upper:]_')"
  local var="OPENCLAW_WHISPER_SHA256_${key}"
  local from_env
  eval "from_env=\${$var:-}"
  if [ -n "$from_env" ]; then
    echo "$from_env"
    return 0
  fi

  case "$name" in
    base) echo "$PINNED_SHA256_BASE" ;;
    *) echo "" ;;
  esac
}

verify_model_sha256() {
  local name="$1"
  local file="$2"
  local expected
  expected="$(expected_sha256_for_model "$name")"

  # Why: 校验文件完整性，防止下载损坏或供应链污染进入转写链路。
  if [ -z "$expected" ]; then
    echo "[WARN] No SHA256 pinned for model '$name'. Skip verification."
    echo "[WARN] Set OPENCLAW_WHISPER_SHA256_$(echo "$name" | tr '[:lower:]-' '[:upper:]_') to enable strict check."
    return 0
  fi

  local actual
  actual="$(sha256_file "$file")"
  if [ "$actual" != "$expected" ]; then
    echo "[ERR] SHA256 mismatch for $file" >&2
    echo "      expected: $expected" >&2
    echo "      actual:   $actual" >&2
    return 4
  fi

  echo "[OK] SHA256 verified: $file"
}

download() {
  local name="$1"
  local out="$MODELS_DIR/ggml-$name.bin"
  local url="$BASE_URL/ggml-$name.bin?download=true"

  if [ -f "$out" ]; then
    echo "[SKIP] $out exists"
    verify_model_sha256 "$name" "$out"
    return 0
  fi

  echo "[DL] $url -> $out"
  curl -L --fail --retry 3 --retry-delay 2 -o "$out" "$url"
  verify_model_sha256 "$name" "$out"
}

# Choose which models to download.
# - Default: base

MODELS=( )

if [ "$#" -gt 0 ]; then
  MODELS=("$@")
else
  MODELS=(base small)
fi

for m in "${MODELS[@]}"; do
  [ -n "$m" ] || continue
  download "$m"
done

echo "[OK] Models are in: $MODELS_DIR"
