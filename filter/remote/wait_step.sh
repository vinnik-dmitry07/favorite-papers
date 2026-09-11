#!/usr/bin/env bash
# wait_step.sh <name> <min_rows>
set -uo pipefail
name="${1:?}"
need="${2:-8}"
log="/workspace/filter/logs/${name}.log"
scores="/workspace/filter/scores_${name}.jsonl"
for _ in $(seq 1 600); do
  n=0
  [[ -f "$scores" ]] && n=$(wc -l < "$scores")
  gpu=$(nvidia-smi --query-gpu=utilization.gpu,memory.used --format=csv,noheader 2>/dev/null || echo '?')
  echo "wait $name rows=$n gpu=$gpu $(date -Is)"
  if [[ "$n" -ge "$need" ]]; then
    break
  fi
  if ! pgrep -f "score_reviewers.py --model ${name}" >/dev/null && ! pgrep -f '/workspace/filter/remote/run_all.sh' >/dev/null; then
    echo DEAD
    break
  fi
  sleep 30
done
python3 - <<PY
import json, collections, sys
from pathlib import Path
p = Path('$scores')
if not p.exists():
    print('NO_SCORES')
    sys.exit(0)
rows = [json.loads(l) for l in p.read_text().splitlines() if l.strip()]
good = [r for r in rows if not r.get('error')]
errs = collections.Counter((r.get('error') or '')[:50] for r in rows if r.get('error'))
print(f'n={len(rows)} good={len(good)} unparsed={sum(1 for r in rows if str(r.get("error","")).startswith("unparsed"))} errors={dict(errs)}')
if good:
    ratings = [r['rating'] for r in good if r.get('rating') is not None]
    print('mean', round(sum(ratings)/len(ratings), 2) if ratings else None, 'n_ratings', len(ratings))
    print('decisions', dict(collections.Counter(r.get('decision') for r in good)))
    print('rating_minmax', (min(ratings), max(ratings)) if ratings else None)
PY
pgrep -af 'score_reviewers.py|run_all.sh' || true
