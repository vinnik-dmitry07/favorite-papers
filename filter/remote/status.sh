#!/usr/bin/env bash
set -uo pipefail
echo GPU
nvidia-smi --query-gpu=utilization.gpu,memory.used --format=csv,noheader || true
echo PROCS
pgrep -af 'score_|run_all|prefetch' || true
echo SCORES
ls -lh /workspace/filter/scores_*.jsonl 2>/dev/null || true
echo PREFETCH
grep -E '^\[prefetch\]' /workspace/filter/logs/prefetch.log | tail -n 12
echo HF
ls /workspace/.hf_home/hub 2>/dev/null | grep models-- || true
echo LOGS
for f in /workspace/filter/logs/openreviewer-8b.log /workspace/filter/logs/sea-e.log /workspace/filter/logs/deepreviewer-7b.log /workspace/filter/logs/deepreviewer-14b.log /workspace/filter/logs/cyclereviewer-8b.log /workspace/filter/logs/cyclereviewer-70b.log /workspace/filter/logs/run_all.log; do
  [[ -f "$f" ]] || continue
  echo "==== $(basename "$f") ===="
  tr '\r' '\n' < "$f" | grep -E 'cached|batch_size|paper_budget|wrote|FAILED|vLLM|Loading|error|%' | tail -n 8
done
