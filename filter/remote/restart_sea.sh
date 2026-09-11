#!/usr/bin/env bash
set -uo pipefail
FILTER_DATA="${FILTER_DATA:-/workspace/filter}"
cd /workspace/filter/remote
pkill -f '/workspace/filter/remote/run_all.sh' || true
pkill -f 'score_reviewers.py' || true
sleep 3
pkill -9 -f 'score_reviewers.py' || true
sleep 1
if [[ -f "$FILTER_DATA/scores_sea-e.jsonl" ]]; then
  mv -f "$FILTER_DATA/scores_sea-e.jsonl" "$FILTER_DATA/scores_sea-e.bad.jsonl"
fi
if [[ -d "$FILTER_DATA/reviews/sea-e" ]]; then
  rm -rf "$FILTER_DATA/reviews/sea-e.bad"
  mv -f "$FILTER_DATA/reviews/sea-e" "$FILTER_DATA/reviews/sea-e.bad"
fi
rm -f "$FILTER_DATA/scores_deepreviewer-7b.jsonl" "$FILTER_DATA/scores_deepreviewer-14b.jsonl"
rm -rf "$FILTER_DATA/reviews/deepreviewer-7b" "$FILTER_DATA/reviews/deepreviewer-14b"
echo leftover_score_procs
pgrep -af score_reviewers || true
echo starting
nohup bash /workspace/filter/remote/run_all.sh sea-e >"$FILTER_DATA/logs/run_all2.log" 2>&1 &
sleep 2
pgrep -af 'run_all.sh|score_reviewers' || true
echo log
tail -n 15 "$FILTER_DATA/logs/run_all2.log" || true
