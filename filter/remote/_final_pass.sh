#!/usr/bin/env bash
# Retry unparsed keys (seed 1) then noise-floor seed1 files. Not committed.
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

CR8B_RETRY='arxiv:1912.01683,arxiv:2001.08361,arxiv:2309.16797,arxiv:2503.21676,arxiv:2512.13961,arxiv:2601.21557,arxiv:2602.07755,arxiv:2608.19197'
DR14B_RETRY='arxiv:1802.09477,arxiv:2201.00650,arxiv:2302.06675,arxiv:2405.20233,arxiv:2406.03445'
OR8B_RETRY='arxiv:2303.17651,arxiv:2405.08007,doi:10.1101/2023.04.04.535512'
DR7BF_RETRY='acl:2022.emnlp-main.340,acl:2023.acl-demo.51,arxiv:1511.05952,arxiv:1707.06887,arxiv:1712.06567,arxiv:1802.09477,arxiv:2004.12919,arxiv:2005.01643,arxiv:2009.11243,arxiv:2011.14826,arxiv:2108.06325,arxiv:2112.07899,arxiv:2206.04615,arxiv:2206.13353,arxiv:2212.14034,arxiv:2302.00923,arxiv:2302.14045,arxiv:2303.07103,arxiv:2304.01433,arxiv:2304.09355,arxiv:2305.01625,arxiv:2306.13575,arxiv:2307.06440,arxiv:2309.14402,arxiv:2311.16452,arxiv:2401.17401,arxiv:2402.02342,arxiv:2402.12483,arxiv:2402.13669,arxiv:2402.16822,arxiv:2404.05405,arxiv:2404.07143,arxiv:2405.20541,arxiv:2407.00695,arxiv:2411.03820,arxiv:2412.14135,arxiv:2503.00735,arxiv:2505.13763,arxiv:2505.21444,arxiv:2505.22954,arxiv:2506.10947,arxiv:2507.10524,arxiv:2507.18074,arxiv:2510.26622,arxiv:2512.18160,arxiv:2601.03192,arxiv:2601.16175,arxiv:2602.07755,arxiv:2602.10416,arxiv:2602.18037,arxiv:2603.25562,arxiv:2604.01754,arxiv:2606.03982,arxiv:2608.11676,doi:10.1038/d41586-024-01413-w,doi:10.1038/s41566-024-01394-2,doi:10.1038/s41586-024-07522-w,doi:10.1101/2023.04.04.535512,doi:10.1101/2024.02.22.581686,openreview:BZ5a1r-kVsf,openreview:klU4737opt'
DR7B_RETRY='arxiv:1712.06567,arxiv:1802.09477,arxiv:2112.03978,arxiv:2201.00650,arxiv:2206.13353,arxiv:2303.07103,arxiv:2402.03300,arxiv:2405.07987,arxiv:2410.21272,arxiv:2502.05171,arxiv:2506.10947,arxiv:2508.07629,arxiv:2512.24695,doi:10.1038/d41586-024-01413-w,doi:10.1038/s41566-024-01394-2,doi:10.1038/s41586-024-07522-w,doi:10.1073/pnas.1611835114,doi:10.1371/journal.pcbi.1011005,doi:10.21203/rs.3.rs-6688473/v1'
NOISE='arxiv:2503.16348,arxiv:2312.10549,arxiv:2303.07103,acl:2025.acl-long.126,arxiv:2304.09355,arxiv:2512.24695,arxiv:2011.14826,arxiv:2406.04268,arxiv:1710.02298,arxiv:2406.11741,openreview:ry_WPG-A-,arxiv:2210.08340,arxiv:2312.00276,arxiv:2405.15682,arxiv:2602.10416,arxiv:2605.22863,arxiv:1904.00962,arxiv:2301.08243,arxiv:2304.06528,arxiv:2402.12483,arxiv:2507.01098,arxiv:2510.05491,arxiv:2602.08676,arxiv:2606.25010,arxiv:2405.04517,arxiv:2606.06574,arxiv:2112.04035,arxiv:2301.04104,arxiv:2405.07987,arxiv:2503.02875,arxiv:2505.24832,arxiv:2509.09675,arxiv:2512.13961,arxiv:2601.21343,arxiv:2604.09168,arxiv:2607.05609,doi:10.1371/journal.pcbi.1011005,arxiv:2309.15807,arxiv:2301.06627,arxiv:2605.07654,arxiv:2205.13147,arxiv:2405.20541,arxiv:2505.15134,arxiv:2512.18552,arxiv:2604.19341,arxiv:2609.01437,arxiv:2402.03300,arxiv:2408.08435,arxiv:2506.01939,arxiv:2511.09149,arxiv:2607.02303,arxiv:2410.21272'

drop_keys() {
  local model="$1"
  local keys="$2"
  KEYS="$keys" MODELS="$model" python3 - <<'PY'
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
}

run_step() {
  local step="$1"
  shift
  echo "[step] ${step} start $(date -Is)"
  pkill -9 -f 'VLLM::EngineCore' 2>/dev/null || true
  sleep 2
  python -u score_reviewers.py "$@"
  echo "[step] ${step} done $(date -Is)"
}

echo "======== $(date -Is) final_pass start ========"

drop_keys cyclereviewer-8b "$CR8B_RETRY"
run_step cr8b-retry --model cyclereviewer-8b --only-keys "$CR8B_RETRY" --seed 1 --max-tokens 12000
run_step cr8b-seed1 --model cyclereviewer-8b --only-keys "$NOISE" --seed 1 --out-suffix seed1

drop_keys deepreviewer-14b "$DR14B_RETRY"
run_step dr14b-retry --model deepreviewer-14b --only-keys "$DR14B_RETRY" --seed 1 --max-paper-chars 48000
run_step dr14b-seed1 --model deepreviewer-14b --only-keys "$NOISE" --seed 1 --out-suffix seed1 --max-paper-chars 48000

drop_keys openreviewer-8b "$OR8B_RETRY"
run_step or8b-retry --model openreviewer-8b --only-keys "$OR8B_RETRY" --seed 1

drop_keys deepreviewer-7b-fast "$DR7BF_RETRY"
run_step dr7bf-retry --model deepreviewer-7b-fast --only-keys "$DR7BF_RETRY" --seed 1 --max-tokens 24576 --max-paper-chars 48000

drop_keys deepreviewer-7b "$DR7B_RETRY"
run_step dr7b-retry --model deepreviewer-7b --only-keys "$DR7B_RETRY" --seed 1 --max-paper-chars 48000

pkill -9 -f 'VLLM::EngineCore' 2>/dev/null || true
echo "[step] all done $(date -Is)"
echo "======== $(date -Is) final_pass done ========"
