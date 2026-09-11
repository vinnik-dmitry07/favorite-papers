#!/usr/bin/env bash
set -uo pipefail
for _ in $(seq 1 40); do
  if grep -q 'paper_budget=' /workspace/filter/logs/openreviewer-8b.log 2>/dev/null; then
    echo OR_READY
    break
  fi
  if grep -q 'FAILED' /workspace/filter/logs/openreviewer-8b.log 2>/dev/null; then
    echo OR_FAILED
    break
  fi
  if ! pgrep -f 'score_reviewers.py --model openreviewer-8b' >/dev/null; then
    echo OR_EXITED
    break
  fi
  echo "loading $(date -Is) mem=$(nvidia-smi --query-gpu=memory.used --format=csv,noheader)"
  sleep 15
done
bash /workspace/filter/remote/status.sh
