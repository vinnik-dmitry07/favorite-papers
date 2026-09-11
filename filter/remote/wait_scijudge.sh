#!/usr/bin/env bash
set -uo pipefail
for _ in $(seq 1 40); do
  if grep -q 'scijudge: wrote' /workspace/filter/logs/scijudge.log 2>/dev/null; then
    echo SCI_DONE
    break
  fi
  if pgrep -f score_reviewers.py >/dev/null; then
    echo REVIEWERS_STARTED
    break
  fi
  tr '\r' '\n' < /workspace/filter/logs/scijudge.log | grep -E 'scijudge: +[0-9]+%' | tail -n 1
  sleep 15
done
echo ---
echo GPU
nvidia-smi --query-gpu=utilization.gpu,memory.used --format=csv,noheader || true
echo PROCS
pgrep -af 'score_|run_all|prefetch' || true
echo ORLOG
tail -n 30 /workspace/filter/logs/openreviewer-8b.log 2>/dev/null || true
echo PREFETCH
grep -E '^\[prefetch\]' /workspace/filter/logs/prefetch.log | tail -n 10
echo SCI_TAIL
grep -E 'scijudge: wrote|FAILED|cached' /workspace/filter/logs/scijudge.log | tail -n 8
