#!/usr/bin/env bash
# Drop KEYS from jsonl/reviews for MODELS and rescore only them.
#   KEYS='arxiv:2303.07103,doi:10.1073/pnas.1611835114' \
#   MODELS='cyclereviewer-8b deepreviewer-14b' ./_rescore_eight.sh
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

DEFAULT_KEYS='openreview:BZ5a1r-kVsf,openreview:OpC-9aBBVJe,openreview:XyGJJ4FPoX,openreview:hcQfTsVnBo,openreview:klU4737opt,openreview:pOoKI3ouv1,openreview:ry_WPG-A-,openreview:wUU-7XTL5XO'
export KEYS="${KEYS:-$DEFAULT_KEYS}"
export MODELS="${MODELS:-cyclereviewer-8b deepreviewer-7b-fast sea-e openreviewer-8b}"

python3 - <<'PY'
import json
import os
from pathlib import Path
keys = {k.strip() for k in os.environ['KEYS'].split(',') if k.strip()}
models = os.environ['MODELS'].split()
root = Path('/workspace/filter')
for name in models:
    path = root / f'scores_{name}.jsonl'
    if not path.exists():
        continue
    rows = [json.loads(l) for l in path.read_text(encoding='utf-8').splitlines() if l.strip()]
    kept = [r for r in rows if r.get('key') not in keys]
    path.write_text(''.join(json.dumps(r, ensure_ascii=False) + '\n' for r in kept), encoding='utf-8')
    rd = root / 'reviews' / name
    dropped = 0
    if rd.exists():
        for key in keys:
            md = rd / (key.replace(':', '_').replace('/', '_') + '.md')
            if md.exists():
                md.unlink()
                dropped += 1
    print(f'{name}: kept {len(kept)}/{len(rows)} dropped_reviews={dropped}', flush=True)
PY

for model in $MODELS; do
  echo "======== $(date -Is) rescore ${model} ========"
  pkill -9 -f 'VLLM::EngineCore' 2>/dev/null || true
  extra=()
  if [[ "$model" == deepreviewer-* ]]; then
    extra+=(--max-paper-chars 48000)
  fi
  python -u score_reviewers.py --model "$model" --only-keys "$KEYS" "${extra[@]}"
done
echo "======== $(date -Is) rescore done ========"
