#!/usr/bin/env bash
set -uo pipefail
for _ in $(seq 1 180); do
  if ! pgrep -f '/workspace/filter/remote/prefetch.sh' >/dev/null; then
    echo PREFETCH_DONE
    break
  fi
  echo "wait $(date -Is)"
  grep -E '^\[prefetch\]' /workspace/filter/logs/prefetch.log | tail -n 3
  sleep 20
done
echo ---
grep -E '^\[prefetch\]|Access denied|Downloaded|failed' /workspace/filter/logs/prefetch.log | tail -n 30
echo HUB
ls /workspace/.hf_home/hub | grep Westlake || true
bash /workspace/filter/remote/status.sh
