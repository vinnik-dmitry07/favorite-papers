#!/usr/bin/env bash
set -uo pipefail

ROOT="$(cd "$(dirname "$0")" && pwd)"
export FILTER_DATA="${FILTER_DATA:-/workspace/filter}"
export HF_HOME="${HF_HOME:-/workspace/.hf_home}"
export HUGGINGFACE_HUB_CACHE="${HUGGINGFACE_HUB_CACHE:-$HF_HOME/hub}"
export PYTHONUNBUFFERED=1
# Blackwell + CUDA 12.8: FlashInfer JIT cannot target sm_120.
export VLLM_USE_FLASHINFER_SAMPLER="${VLLM_USE_FLASHINFER_SAMPLER:-0}"
export VLLM_ATTENTION_BACKEND="${VLLM_ATTENTION_BACKEND:-FLASH_ATTN}"
if [[ -f /venv/main/bin/activate ]]; then
  # shellcheck disable=SC1091
  source /venv/main/bin/activate
fi
if command -v python >/dev/null 2>&1; then
  PYTHON=python
else
  PYTHON=python3
fi
LOGDIR="${FILTER_DATA}/logs"
mkdir -p "$LOGDIR" "$HUGGINGFACE_HUB_CACHE"
cd "$ROOT"

run() {
  local name="$1"
  shift
  echo "======== $(date -Is) $name ========"
  if ! "$PYTHON" -u "$@" 2>&1 | tee -a "$LOGDIR/${name}.log"; then
    echo "[run_all] $name FAILED (continuing)" | tee -a "$LOGDIR/${name}.log"
  fi
  "$PYTHON" - <<'PY'
import gc
try:
    import torch
    gc.collect()
    if torch.cuda.is_available():
        torch.cuda.empty_cache()
        print('cuda cache cleared', flush=True)
except Exception as exc:
    print('cache clear skipped:', exc, flush=True)
PY
}

START="${1:-}"
skip=0
if [[ -n "$START" ]]; then
  skip=1
fi

run_if() {
  local name="$1"
  shift
  if [[ $skip -eq 1 ]]; then
    if [[ "$name" == "$START" ]]; then
      skip=0
    else
      echo "[run_all] skip $name (waiting for $START)"
      return
    fi
  fi
  run "$name" "$@"
}

echo "[run_all] data=$FILTER_DATA python=$PYTHON start=${START:-all}"
run_if naip score_naip.py --model both
run_if scijudge score_scijudge.py
run_if openreviewer-8b score_reviewers.py --model openreviewer-8b
run_if sea-e score_reviewers.py --model sea-e
run_if cyclereviewer-8b score_reviewers.py --model cyclereviewer-8b
run_if deepreviewer-7b-fast score_reviewers.py --model deepreviewer-7b-fast --max-paper-chars 48000
run_if deepreviewer-14b score_reviewers.py --model deepreviewer-14b --max-paper-chars 48000
run_if deepreviewer-7b score_reviewers.py --model deepreviewer-7b --max-paper-chars 48000

echo "[run_all] finished $(date -Is)"
echo "[run_all] scores:"
ls -lh "$FILTER_DATA"/scores_*.jsonl || true
