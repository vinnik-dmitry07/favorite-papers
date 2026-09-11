#!/usr/bin/env bash
set -uo pipefail
for _ in $(seq 1 90); do
  if [[ -f /workspace/filter/scores_sea-e.jsonl ]]; then
    n=$(wc -l < /workspace/filter/scores_sea-e.jsonl)
    if [[ "$n" -ge 8 ]]; then
      echo ROWS="$n"
      break
    fi
  fi
  echo "wait $(date -Is) gpu=$(nvidia-smi --query-gpu=utilization.gpu,memory.used --format=csv,noheader) rows=$(wc -l < /workspace/filter/scores_sea-e.jsonl 2>/dev/null || echo 0)"
  if grep -q 'Engine core initialization failed' /workspace/filter/logs/sea-e.log && ! pgrep -f 'score_reviewers.py --model sea-e' >/dev/null; then
    echo FAILED_AGAIN
    tail -n 15 /workspace/filter/logs/sea-e.log
    exit 1
  fi
  sleep 15
done
python3 - <<'PY'
import json, collections
from pathlib import Path
p = Path('/workspace/filter/scores_sea-e.jsonl')
if not p.exists():
    print('NO_SCORES')
    raise SystemExit(1)
rows = [json.loads(l) for l in p.read_text().splitlines() if l.strip()]
good = [r for r in rows if not r.get('error')]
errs = collections.Counter((r.get('error') or '')[:40] for r in rows if r.get('error'))
print(f'n={len(rows)} good={len(good)} unparsed={sum(1 for r in rows if str(r.get("error","")).startswith("unparsed"))} errors={dict(errs)}')
if good:
    ratings = [r['rating'] for r in good if r.get('rating') is not None]
    dec = collections.Counter(r.get('decision') for r in good)
    print('ratings_sample', ratings[:20], 'mean', round(sum(ratings)/len(ratings), 2) if ratings else None)
    print('decisions', dict(dec))
    print('first_good', {k: good[0].get(k) for k in ('key','rating','decision','soundness')})
if any(r.get('error') for r in rows):
    print('sample_err_tail', (next(r for r in rows if r.get('error')).get('raw_tail') or '')[-200:].replace('\n',' | '))
PY
grep 'paper_budget=' /workspace/filter/logs/sea-e.log | tail -n 1
pgrep -af 'score_reviewers|run_all.sh' || true
