#!/usr/bin/env bash
set -uo pipefail
pkill -f '/workspace/filter/remote/run_all.sh' || true
pkill -f 'score_reviewers.py' || true
sleep 4
pkill -9 -f 'score_reviewers.py' || true
pkill -9 -f 'VLLM::EngineCore' || true
sleep 2
mv -f /workspace/filter/scores_sea-e.jsonl /workspace/filter/scores_sea-e.bad2.jsonl 2>/dev/null || true
rm -rf /workspace/filter/reviews/sea-e
rm -f /workspace/filter/scores_deepreviewer-7b.jsonl
echo GPU
nvidia-smi --query-gpu=memory.used --format=csv,noheader || true
pgrep -af 'score_reviewers|EngineCore|run_all.sh' || echo clean
