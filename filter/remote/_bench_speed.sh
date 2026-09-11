#!/usr/bin/env bash
set -uo pipefail
ROOT=/workspace/filter/remote
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
cd "$ROOT"

KEYS='arxiv:2608.17163,arxiv:2509.09675,arxiv:2503.14858,arxiv:2501.16142,arxiv:2411.03820,arxiv:2312.13327,arxiv:2312.00276,arxiv:2306.02451'

run_one() {
  local name="$1"
  shift
  local log="${FILTER_DATA}/logs/bench_${name}.log"
  mkdir -p "${FILTER_DATA}/logs"
  echo "======== $(date -Is) bench ${name} start ========" | tee "$log"
  local t0
  t0=$(date +%s)
  python -u score_reviewers.py "$@" 2>&1 | tee -a "$log"
  local t1
  t1=$(date +%s)
  echo "======== $(date -Is) bench ${name} done elapsed_sec=$((t1 - t0)) ========" | tee -a "$log"
}

case "${1:-}" in
  cr8b)
    run_one cyclereviewer-8b --model cyclereviewer-8b --only-keys "$KEYS" --batch-size 8
    ;;
  dr14b)
    run_one deepreviewer-14b --model deepreviewer-14b --deep-mode 'Fast Mode' \
      --max-paper-chars 48000 --only-keys "$KEYS" --batch-size 4
    ;;
  *)
    echo "usage: $0 cr8b|dr14b"
    exit 1
    ;;
esac
