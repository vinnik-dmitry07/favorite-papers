#!/usr/bin/env bash
set -euo pipefail

ROOT="$(cd "$(dirname "$0")" && pwd)"
export FILTER_DATA="${FILTER_DATA:-/workspace/filter}"
export HF_HOME="${HF_HOME:-/workspace/.hf_home}"
export HUGGINGFACE_HUB_CACHE="${HUGGINGFACE_HUB_CACHE:-$HF_HOME}"
mkdir -p "$FILTER_DATA" "$HF_HOME" "$FILTER_DATA/logs" "$FILTER_DATA/fulltext"
if [[ -f "$FILTER_DATA/fulltext.zip" ]]; then
  unzip -o "$FILTER_DATA/fulltext.zip" -d "$FILTER_DATA/fulltext" >/dev/null
  echo "[setup] unpacked $FILTER_DATA/fulltext.zip"
fi

if [[ -f /venv/main/bin/activate ]]; then
  # shellcheck disable=SC1091
  source /venv/main/bin/activate
fi

echo "[setup] python=$(python --version 2>/dev/null || python3 --version) gpu=$(nvidia-smi --query-gpu=name,memory.total --format=csv,noheader || true)"

# Verified stack on RTX PRO 6000 Blackwell (sm_120), driver 610.43.02:
# vLLM 0.29.0, torch 2.13.0+cu130.
# Required env: VLLM_USE_FLASHINFER_SAMPLER=0 VLLM_ATTENTION_BACKEND=FLASH_ATTN
python -m pip install -U pip
if [[ -f "$ROOT/requirements.lock" && "${USE_LOCK:-0}" == 1 ]]; then
  python -m pip install -r "$ROOT/requirements.lock"
else
  python -m pip install -U \
    'vllm' \
    'ai_researcher' \
    'peft' \
    'bitsandbytes' \
    'tqdm' \
    'huggingface_hub[cli]' \
    'transformers' \
    'accelerate' \
    'numpy'
fi

if [[ -z "${HF_TOKEN:-}" ]]; then
  echo "[setup] WARNING: HF_TOKEN is empty. Gated CycleReviewer/DeepReviewer downloads will fail."
fi

MODELS=(
  ssocean/NAIPv2
  ssocean/NAIP
  OpenMOSS-Team/SciJudge-30B-2605
  maxidl/Llama-OpenReviewer-8B
  ECNU-SEA/SEA-E
  WestlakeNLP/DeepReviewer-7B
  WestlakeNLP/DeepReviewer-14B
  WestlakeNLP/CycleReviewer-ML-Llama-3.1-8B
  WestlakeNLP/CycleReviewer-Llama-3.1-70B
)

HF_BIN=hf
if ! command -v hf >/dev/null 2>&1; then
  HF_BIN=huggingface-cli
fi
for repo in "${MODELS[@]}"; do
  echo "[setup] $HF_BIN download $repo"
  "$HF_BIN" download "$repo" || echo "[setup] download failed for $repo (gated? accept the model license on HF)"
done

echo "[setup] done"
