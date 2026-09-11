'''Score title+abstract with NAIPv2 and NAIP-v1.

    python score_naip.py
    python score_naip.py --model naipv2
    python score_naip.py --model naipv1
'''

from __future__ import annotations

import argparse
import sys
from pathlib import Path

HERE = Path(__file__).resolve().parent
sys.path.insert(0, str(HERE))

from data_paths import (  # noqa: E402
    append_jsonl,
    fill_template,
    load_joined,
    scored_keys,
    scores_path,
)

# NAIPv2 model card / demo_v2 — do not rewrite.
PROMPT_V2 = (
    'Given a research paper, Title: {title}\n'
    'Abstract: {abstract}\n'
    'Evaluate the quality of this paper:'
)
# NAIP-v1 demo_v1.py (the GitHub file interpolates too early; this is the template).
PROMPT_V1 = (
    'Given a certain paper, Title: {title}\n Abstract: {abstract}. \n '
    'Predict its normalized academic impact (between 0 and 1):'
)


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser()
    parser.add_argument('--model', choices=['naipv2', 'naipv1', 'both'], default='both')
    parser.add_argument('--batch-size', type=int, default=8)
    parser.add_argument('--max-length', type=int, default=512)
    parser.add_argument('--device', default='cuda')
    return parser.parse_args()


def load_cls_model(repo: str, eight_bit: bool, peft: bool):
    import torch
    from transformers import AutoTokenizer, BitsAndBytesConfig

    tokenizer = AutoTokenizer.from_pretrained(repo)
    if tokenizer.pad_token is None:
        tokenizer.pad_token = tokenizer.eos_token
    kwargs = {'num_labels': 1, 'device_map': 'auto'}
    if eight_bit:
        kwargs['quantization_config'] = BitsAndBytesConfig(load_in_8bit=True)
    else:
        kwargs['torch_dtype'] = torch.float16
    if peft:
        from peft import AutoPeftModelForSequenceClassification
        model = AutoPeftModelForSequenceClassification.from_pretrained(repo, **kwargs)
    else:
        from transformers import AutoModelForSequenceClassification
        model = AutoModelForSequenceClassification.from_pretrained(repo, **kwargs)
    model.config.pad_token_id = tokenizer.pad_token_id
    model.eval()
    score_names = [
        name for name, _ in model.named_parameters()
        if 'score' in name or 'classifier' in name
    ]
    saved = []
    if peft:
        cfg = getattr(model, 'peft_config', None)
        if isinstance(cfg, dict):
            for adapter in cfg.values():
                saved.extend(list(getattr(adapter, 'modules_to_save', None) or []))
        if saved and not any('score' in name or 'classifier' in name for name in saved):
            print(f'warning: PEFT modules_to_save={saved} has no score head', flush=True)
    if not score_names:
        print('warning: no score/classifier parameters found', flush=True)
    else:
        print(f'loaded score params: {score_names[:8]}', flush=True)
    return model, tokenizer


def score_rows(
    name: str,
    repo: str,
    rows: list[dict],
    args,
    *,
    prompt: str,
    eight_bit: bool,
    peft: bool,
    sigmoid: bool,
) -> None:
    import torch
    from tqdm import tqdm

    out = scores_path(name)
    done = scored_keys(out)
    pending = [
        row for row in rows
        if row['key'] not in done and (row.get('title') or row.get('abstract'))
    ]
    print(f'{name}: {len(done)} cached, {len(pending)} to score', flush=True)
    if not pending:
        return
    model, tokenizer = load_cls_model(repo, eight_bit=eight_bit, peft=peft)
    device = next(model.parameters()).device
    for start in tqdm(range(0, len(pending), args.batch_size), desc=name):
        batch = pending[start:start + args.batch_size]
        prompts = [
            fill_template(
                prompt,
                title=(row.get('title') or '').strip().replace('\n', ' '),
                abstract=(row.get('abstract') or '').strip().replace('\n', ' '),
            )
            for row in batch
        ]
        inputs = tokenizer(
            prompts,
            return_tensors='pt',
            padding=True,
            truncation=True,
            max_length=args.max_length,
        )
        inputs = {key: value.to(device) for key, value in inputs.items()}
        with torch.no_grad():
            logits = model(**inputs).logits.view(-1)
            values = torch.sigmoid(logits) if sigmoid else logits
        for row, score in zip(batch, values.tolist()):
            append_jsonl(out, {
                'key': row['key'],
                'score': float(score),
                'model': name,
            })
    print(f'{name}: wrote {out}', flush=True)


def main() -> None:
    args = parse_args()
    rows = load_joined()
    if args.model in ('naipv2', 'both'):
        score_rows(
            'naipv2', 'ssocean/NAIPv2', rows, args,
            prompt=PROMPT_V2, eight_bit=False, peft=False, sigmoid=False,
        )
    if args.model in ('naipv1', 'both'):
        score_rows(
            'naipv1', 'ssocean/NAIP', rows, args,
            prompt=PROMPT_V1, eight_bit=True, peft=True, sigmoid=True,
        )


if __name__ == '__main__':
    main()
