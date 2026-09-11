#!/usr/bin/env bash
set -uo pipefail

export HF_HOME="${HF_HOME:-/workspace/.hf_home}"
export HUGGINGFACE_HUB_CACHE="${HUGGINGFACE_HUB_CACHE:-$HF_HOME/hub}"
export FILTER_DATA="${FILTER_DATA:-/workspace/filter}"
LOG="${FILTER_DATA}/logs/prefetch.log"
mkdir -p "$(dirname "$LOG")" "$HF_HOME" "$HUGGINGFACE_HUB_CACHE"

if [[ -f /venv/main/bin/activate ]]; then
  # shellcheck disable=SC1091
  source /venv/main/bin/activate
fi

if [[ $# -gt 0 ]]; then
  MODELS=("$@")
else
  MODELS=(
    maxidl/Llama-OpenReviewer-8B
    ECNU-SEA/SEA-E
    WestlakeNLP/DeepReviewer-7B
    WestlakeNLP/DeepReviewer-14B
    WestlakeNLP/CycleReviewer-ML-Llama-3.1-8B
    WestlakeNLP/CycleReviewer-Llama-3.1-70B
  )
fi

echo "[prefetch] start $(date -Is)" | tee -a "$LOG"
for repo in "${MODELS[@]}"; do
  echo "[prefetch] $(date -Is) $repo" | tee -a "$LOG"
  if ! hf download "$repo" >>"$LOG" 2>&1; then
    echo "[prefetch] failed $repo" | tee -a "$LOG"
  fi
done
echo "[prefetch] done $(date -Is)" | tee -a "$LOG"
