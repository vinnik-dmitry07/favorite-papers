#!/usr/bin/env bash
set -uo pipefail
nohup bash /workspace/filter/remote/run_all.sh sea-e >/workspace/filter/logs/run_all4.log 2>&1 &
sleep 3
pgrep -af 'run_all.sh|score_reviewers.py' || true
tail -n 8 /workspace/filter/logs/run_all4.log || true
