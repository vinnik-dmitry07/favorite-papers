'''Best-effort SciBERT Accept-Reject scores from the DGC-BERT Drive checkpoint.

    python filter/score_dgcbert.py
'''

from __future__ import annotations

import argparse
import sys
import zipfile
from pathlib import Path

FILTER_DIR = Path(__file__).resolve().parent
sys.path.insert(0, str(FILTER_DIR))

from paths import (  # noqa: E402
    FILTER_DIR as ROOT_FILTER,
    LOGS_DIR,
    append_jsonl,
    is_score_row,
    load_joined,
    read_jsonl,
    scored_keys,
    write_jsonl,
)

DRIVE_ID = '13Inl_ChtY0LBCp9D0wjFW1yFdJPvRMep'
CACHE = ROOT_FILTER / 'cache' / 'dgcbert'
WEIGHTS_ZIP = CACHE / 'dgcbert_state_dicts.zip'
OUT = ROOT_FILTER / 'scores_dgcbert.jsonl'
SCIBERT = 'allenai/scibert_scivocab_uncased'


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser()
    parser.add_argument('--device', default='cuda')
    parser.add_argument('--batch-size', type=int, default=8)
    parser.add_argument('--max-length', type=int, default=256)
    parser.add_argument('--force', action='store_true')
    return parser.parse_args()


def write_na(rows: list[dict], reason: str) -> None:
    existing = [row for row in read_jsonl(OUT) if is_score_row(row)]
    if existing:
        print(f'dgcbert: keep {len(existing)} good rows; skip overwrite ({reason})', flush=True)
        return
    write_jsonl(OUT, [
        {'key': row['key'], 'p_accept': None, 'error': reason}
        for row in rows
    ])
    print(f'dgcbert: N/A ({reason}) -> {OUT}', flush=True)


def download_weights() -> Path | None:
    CACHE.mkdir(parents=True, exist_ok=True)
    if WEIGHTS_ZIP.exists() and WEIGHTS_ZIP.stat().st_size > 1000:
        return WEIGHTS_ZIP
    print('dgcbert: downloading Drive state_dict…', flush=True)
    try:
        import gdown
    except ImportError:
        from subprocess import check_call
        check_call([sys.executable, '-m', 'pip', 'install', 'gdown==5.2.0', '-q'])
        import gdown
    url = f'https://drive.google.com/uc?id={DRIVE_ID}'
    try:
        gdown.download(url, str(WEIGHTS_ZIP), quiet=False)
    except Exception as exc:  # noqa: BLE001
        print(f'dgcbert: gdown failed: {exc}', flush=True)
        return None
    if not WEIGHTS_ZIP.exists() or WEIGHTS_ZIP.stat().st_size < 1000:
        return None
    return WEIGHTS_ZIP


def safe_extract(archive: Path, dest: Path) -> None:
    dest.mkdir(parents=True, exist_ok=True)
    root = dest.resolve()
    with zipfile.ZipFile(archive) as zf:
        for info in zf.infolist():
            name = info.filename.replace('\\', '/')
            if name.startswith('/') or '..' in Path(name).parts:
                continue
            target = (dest / name).resolve()
            if not str(target).startswith(str(root)):
                continue
            zf.extract(info, dest)


def extract_ckpt(archive: Path) -> Path | None:
    dest = CACHE / 'unpacked'
    suffix = archive.suffix.lower()
    if suffix in {'.pt', '.pth', '.bin', '.pkl'}:
        return archive
    if not zipfile.is_zipfile(archive):
        return archive
    safe_extract(archive, dest)
    candidates = []
    for path in dest.rglob('*'):
        if path.suffix.lower() in {'.pt', '.pth', '.bin', '.pkl', '.ckpt'} and path.stat().st_size > 10_000:
            name = path.name.lower()
            score = 0
            if 'scibert' in name:
                score += 2
            if 'aapr' in name or 'peerread' in name:
                score += 1
            candidates.append((score, path.stat().st_size, path))
    if not candidates:
        return None
    candidates.sort(reverse=True)
    return candidates[0][2]


def remap_state(raw: dict) -> dict:
    state = raw
    for key in ('state_dict', 'model', 'model_state_dict'):
        if isinstance(raw, dict) and key in raw and isinstance(raw[key], dict):
            state = raw[key]
            break
    mapped = {}
    for name, tensor in state.items():
        clean = name
        changed = True
        while changed:
            changed = False
            for prefix in ('module.', 'model.'):
                if clean.startswith(prefix):
                    clean = clean[len(prefix):]
                    changed = True
        if clean.startswith('bert_model.'):
            clean = 'bert.' + clean[len('bert_model.'):]
        elif clean.startswith('encoder.'):
            clean = 'bert.' + clean[len('encoder.'):]
        if clean.startswith('fc.'):
            clean = 'classifier.' + clean[3:]
        mapped[clean] = tensor
    return mapped


def load_checkpoint(path: Path):
    import torch
    try:
        return torch.load(path, map_location='cpu', weights_only=True)
    except Exception as exc:  # noqa: BLE001
        raise ValueError(f'refusing unsafe pickle checkpoint: {exc}') from exc


def load_model(ckpt_path: Path, device: str):
    import torch
    from transformers import AutoModelForSequenceClassification, AutoTokenizer

    print(f'dgcbert: loading checkpoint {ckpt_path}', flush=True)
    raw = load_checkpoint(ckpt_path)
    if not isinstance(raw, dict):
        raise ValueError(f'unexpected checkpoint type {type(raw)}')
    mapped = remap_state(raw)
    tokenizer = AutoTokenizer.from_pretrained(SCIBERT)
    model = AutoModelForSequenceClassification.from_pretrained(SCIBERT, num_labels=2)
    missing, unexpected = model.load_state_dict(mapped, strict=False)
    loaded = len(mapped) - len(unexpected)
    print(
        f'dgcbert: loaded {loaded} tensors, missing={len(missing)}, unexpected={len(unexpected)}',
        flush=True,
    )
    if loaded < 50:
        raise ValueError('checkpoint does not match SciBERT classifier')
    if any(name.startswith('classifier.') for name in missing):
        raise ValueError('classifier head missing from checkpoint')
    model.to(device)
    model.eval()
    return model, tokenizer


def accept_prob(logits) -> float:
    import torch
    if logits.numel() == 1:
        return float(torch.sigmoid(logits).item())
    probs = torch.softmax(logits.float(), dim=-1)
    if probs.shape[-1] < 2:
        return float(probs[..., 0].item())
    return float(probs[..., 1].item())


def pick_device(requested: str) -> str:
    import torch
    if requested == 'cpu':
        return 'cpu'
    if torch.cuda.is_available():
        return 'cuda'
    print('dgcbert: CUDA missing, using CPU', flush=True)
    return 'cpu'


def main() -> None:
    args = parse_args()
    LOGS_DIR.mkdir(parents=True, exist_ok=True)
    rows = [row for row in load_joined() if row.get('abstract') or row.get('title')]
    if args.force and OUT.exists():
        OUT.unlink()
    if not args.force and scored_keys(OUT) >= {row['key'] for row in rows}:
        print(f'dgcbert: {OUT} already complete', flush=True)
        return

    archive = download_weights()
    if archive is None:
        write_na(rows, 'drive_download_failed')
        return
    try:
        ckpt = extract_ckpt(archive)
        if ckpt is None:
            write_na(rows, 'no_checkpoint_in_archive')
            return
        device = pick_device(args.device)
        model, tokenizer = load_model(ckpt, device)
    except Exception as exc:  # noqa: BLE001
        print(f'dgcbert: load failed: {exc}', flush=True)
        write_na(rows, f'load_failed: {exc}')
        return

    done = scored_keys(OUT) if not args.force else set()
    pending = [row for row in rows if row['key'] not in done]
    print(f'dgcbert: {len(done)} cached, {len(pending)} to score', flush=True)
    from tqdm import tqdm
    import torch

    for start in tqdm(range(0, len(pending), args.batch_size), desc='dgcbert'):
        batch = pending[start:start + args.batch_size]
        texts = [
            f"{(row.get('title') or '').strip()}. {(row.get('abstract') or '').strip()}"
            for row in batch
        ]
        inputs = tokenizer(
            texts,
            return_tensors='pt',
            padding=True,
            truncation=True,
            max_length=args.max_length,
        )
        inputs = {key: value.to(device) for key, value in inputs.items()}
        with torch.no_grad():
            logits = model(**inputs).logits
        for row, logit in zip(batch, logits):
            p_accept = accept_prob(logit)
            append_jsonl(OUT, {
                'key': row['key'],
                'p_accept': p_accept,
                'decision': 'Accept' if p_accept >= 0.5 else 'Reject',
            })
    print(f'dgcbert: wrote {OUT} ({len(read_jsonl(OUT))} rows)', flush=True)


if __name__ == '__main__':
    main()
