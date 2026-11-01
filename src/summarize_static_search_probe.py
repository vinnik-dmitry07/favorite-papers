'''Create a compact, reproducible report from a completed probe run.'''

import argparse
import hashlib
import json
from pathlib import Path

from common import ROOT
from run_static_search_probe import summarize


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('report', type=Path)
    parser.add_argument('--output', required=True, type=Path)
    args = parser.parse_args()
    raw = args.report.read_bytes()
    report = json.loads(raw)
    summarize(report)
    patterns = (
        'src/*static_search_probe*.py', 'worker/src/static-search*.ts',
        'worker/src/catalog-search*.ts', 'worker/src/tokenize*.ts',
        'worker/src/service.ts', 'worker/probe-kernel/*.wat',
        'worker/probe-kernel/*.mjs', 'worker/wrangler.probe.toml',
        'worker/package.json', 'worker/package-lock.json',
    )
    paths = sorted(
        {path for pattern in patterns for path in ROOT.glob(pattern)})
    compact = {key: report.get(key) for key in (
        'run_id', 'origin', 'started_ms', 'finished_ms', 'info', 'variants',
        'cases', 'variant_gates', 'functional_gate', 'cpu_gate',
        'runtime_gate',
        'memory_gate', 'isolate_cold_gate', 'retrieval_quality', 'limitations',
    )}
    compact.update(
        raw_report_sha256=hashlib.sha256(raw).hexdigest(),
        source_sha256={str(path.relative_to(ROOT)): hashlib.sha256(
            path.read_bytes()).hexdigest() for path in paths},
        requests={key: {'count': len(report.get(key, [])),
                        'successful': sum(row['success']
                                          for row in report.get(key, []))}
                  for key in ('requests', 'priming_requests', 'diagnostics')},
    )
    args.output.parent.mkdir(parents=True, exist_ok=True)
    args.output.write_text(
        json.dumps(
            compact,
            indent=2) + '\n',
        encoding='utf-8')
    print(args.output)


if __name__ == '__main__':
    main()
