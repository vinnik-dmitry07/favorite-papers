#!/usr/bin/env bash
set -uo pipefail

ROOT="$(cd "$(dirname "$0")" && pwd)"
export FILTER_DATA="${FILTER_DATA:-/workspace/filter}"
export HF_HOME="${HF_HOME:-/workspace/.hf_home}"
export HUGGINGFACE_HUB_CACHE="${HUGGINGFACE_HUB_CACHE:-$HF_HOME/hub}"
export PYTHONUNBUFFERED=1
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
mkdir -p "$LOGDIR"
cd "$ROOT"

KEYS='arxiv:2410.04444,arxiv:2308.16117,arxiv:2402.16823,arxiv:1901.01753,arxiv:2312.04927,arxiv:2006.16236,arxiv:2509.14234'
LOG="${LOGDIR}/score_new7.log"

echo "[score_new7] start $(date -Is) keys=$KEYS" | tee -a "$LOG"

run() {
  local name="$1"
  shift
  echo "======== $(date -Is) $name ========" | tee -a "$LOG"
  echo "[step] $name start" | tee -a "$LOG"
  if ! "$PYTHON" -u "$@" 2>&1 | tee -a "$LOGDIR/${name}.log" | tee -a "$LOG"; then
    echo "[score_new7] $name FAILED (continuing)" | tee -a "$LOG"
  fi
  echo "[step] $name done" | tee -a "$LOG"
  pkill -9 -f VLLM::EngineCore >/dev/null 2>&1 || true
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

run naip score_naip.py --model both
run scijudge score_scijudge.py
run openreviewer-8b score_reviewers.py --model openreviewer-8b --only-keys "$KEYS"
run sea-e score_reviewers.py --model sea-e --only-keys "$KEYS"
run cyclereviewer-8b score_reviewers.py --model cyclereviewer-8b --only-keys "$KEYS"
run deepreviewer-7b-fast score_reviewers.py --model deepreviewer-7b-fast --only-keys "$KEYS" --max-paper-chars 48000
run deepreviewer-14b score_reviewers.py --model deepreviewer-14b --only-keys "$KEYS" --max-paper-chars 48000
run deepreviewer-7b score_reviewers.py --model deepreviewer-7b --only-keys "$KEYS" --max-paper-chars 48000

echo "[score_new7] finished $(date -Is)" | tee -a "$LOG"
echo "[step] all done" | tee -a "$LOG"
ls -lh "$FILTER_DATA"/scores_*.jsonl | tee -a "$LOG"
