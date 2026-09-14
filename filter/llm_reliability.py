'''Curated reliability labels for the LLM inventory.

Spurious-reward status is a property of a training signal on a checkpoint,
not a property of a family. Empty contamination means these two source
papers did not establish a status for that row.
'''

from __future__ import annotations

CONTAMINATION = (
    '',
    'direct-memorization',
    'spurious-gains',
    'sensitivity',
    'weaker-than-qwen-math',
    'post-rl-saturated',
    'control',
    'untested',
)
REWARD_TYPES = (
    '',
    'ground-truth',
    'spurious-suite',
    'format',
    'entropy',
    'environment',
    'unspecified',
)
SPURIOUS_CONTROLS = (
    '',
    'random+incorrect+format',
    'format+entropy',
    'held-out-envs',
    'none-reported',
)
CKPT_SELECT = (
    '',
    'validation-avg',
    'per-bench-best',
    'mixed-avg-and-per-bench',
    'last',
    'unspecified',
)

SHAO = 'arxiv:2506.10947'
YAN = 'arxiv:2601.11061'
ONESHOT = 'arxiv:2504.20571'
ENTROPY = 'arxiv:2505.15134'
SKPO = 'arxiv:2604.08690'
RLVE = 'arxiv:2511.07317'

PAPER_META = {
    SHAO: {
        'title': 'Spurious Rewards: Rethinking Training Signals in RLVR',
        'section': 'Post-training',
    },
    YAN: {
        'title': 'Spurious Rewards Paradox: How RLVR Activates Memorization Shortcuts',
        'section': 'Post-training',
    },
    ONESHOT: {
        'title': (
            'Reinforcement Learning for Reasoning in Large Language Models '
            'with One Training Example'
        ),
        'section': 'Post-training',
    },
}

# MATH-500 deltas from Shao et al. v2 on Qwen2.5-Math-7B.
SHAO_MATH500_RANDOM_PP = 21.4
SHAO_MATH500_GT_PP = 29.1

MODEL_STATUS = (
    (
        'Qwen2.5-Math-7B',
        'direct-memorization',
        'Large gains under random/incorrect reward; mechanistic evidence of '
        'retrieving memorized answers on the studied sets.',
    ),
    (
        'Qwen2.5-Math-1.5B',
        'spurious-gains',
        'Spurious-reward gains, reward- and benchmark-dependent. The 7B '
        'memorization mechanism is a separate claim.',
    ),
    (
        'Qwen2.5-1.5B / 7B Base',
        'sensitivity',
        'Some uninformative or incorrect signals help; the effect is not '
        'the same for every reward. Not a universal contamination finding.',
    ),
    (
        'Qwen3-8B',
        'weaker-than-qwen-math',
        'Yan et al. see similar memorization marks on the studied checkpoint, '
        'weaker than Qwen2.5-Math-7B.',
    ),
    (
        'Qwen2.5-Math-7B-Instruct / Qwen2.5-7B-Instruct',
        'post-rl-saturated',
        'Appendix J of Shao et al.: further RLVR, even with a correct reward, '
        'adds little. A later post-training regime; a flat curve is not proof '
        'the checkpoint is clean.',
    ),
    (
        'Llama 3.1/3.2 and OLMo 2 in those two papers',
        'control',
        'Spurious rewards usually help much less or hurt. Useful controls; '
        'not a guarantee of no contamination.',
    ),
    (
        'Other Qwen3 sizes, OLMo 3, Llama 4, everything else',
        'untested',
        'These two papers do not establish a status.',
    ),
)

PAPER_READINGS = (
    (
        'One-shot RLVR',
        ONESHOT,
        'High-priority recheck: separate gains from format/entropy controls '
        'and from checkpoint picking. The paper already trains Llama, so it '
        'is not a Qwen-only result. Default tables use the best average on '
        'six benches; Appendix C.1.3 also reports the best score on each '
        'benchmark (an optimistic upper bound).',
    ),
    (
        'Entropy Minimization',
        ENTROPY,
        'Authors already show a much smaller Llama effect and that the result '
        'depends on confidence tracking correctness. Keep those on the '
        'trained rows; API SciCode names are not the finding.',
    ),
    (
        'SKPO',
        SKPO,
        'Stronger transfer check than a second public math set: trains Qwen '
        'and Llama, evaluates MMLU-Pro and LiveCodeBench. That is not a '
        'spurious-reward control.',
    ),
    (
        'RLVE',
        RLVE,
        '50 environments unseen in training and 2,500 generated problems are '
        'a more contentful transfer control than another public math '
        'benchmark. Do not merge those numbers with the DeepMath run.',
    ),
)

SHAO_EVAL_ID = ['MATH-500']
SHAO_EVAL_OOD = ['AMC', 'AIME 2024', 'AIME 2025']
SHAO_TRAIN = ['DeepScaleR']

EXTRA_ROWS = (
    {
        'key': SHAO,
        'model': 'Qwen2.5-Math-7B-Instruct',
        'family': 'Qwen',
        'generation': '2.5',
        'variant': 'Math-Instruct',
        'sizes': ['7B'],
        'start_point': 'instruct',
        'role': 'trained',
        'method': 'GRPO',
        'train_data': list(SHAO_TRAIN),
        'eval_id': list(SHAO_EVAL_ID),
        'eval_ood': list(SHAO_EVAL_OOD),
        'ood_basis': 'inferred',
        'notes': (
            'Appendix J of Shao et al. v2: already post-RLVR. Further RLVR, '
            'including ground-truth reward, adds little. Saturation after '
            'earlier post-training; a flat curve is not proof the checkpoint '
            'is clean.'
        ),
        'checkpoint_origin': 'Qwen2.5-Math-7B-Instruct (prior RLVR)',
        'reward_type': 'spurious-suite',
        'spurious_controls': 'random+incorrect+format',
        'contamination': 'post-rl-saturated',
        'ckpt_select': 'unspecified',
    },
    {
        'key': SHAO,
        'model': 'Qwen2.5-7B-Instruct',
        'family': 'Qwen',
        'generation': '2.5',
        'variant': 'Instruct',
        'sizes': ['7B'],
        'start_point': 'instruct',
        'role': 'trained',
        'method': 'GRPO',
        'train_data': list(SHAO_TRAIN),
        'eval_id': list(SHAO_EVAL_ID),
        'eval_ood': list(SHAO_EVAL_OOD),
        'ood_basis': 'inferred',
        'notes': (
            'Appendix J of Shao et al. v2: same plateau as '
            'Qwen2.5-Math-7B-Instruct under further RLVR, including '
            'ground-truth reward.'
        ),
        'checkpoint_origin': 'Qwen2.5-7B-Instruct (prior post-training)',
        'reward_type': 'spurious-suite',
        'spurious_controls': 'random+incorrect+format',
        'contamination': 'post-rl-saturated',
        'ckpt_select': 'unspecified',
    },
    {
        'key': SHAO,
        'model': 'Llama-3.1-Tulu-3-8B',
        'family': 'Llama',
        'generation': '3.1',
        'variant': 'Tulu-3',
        'sizes': ['8B'],
        'start_point': 'rl-tuned',
        'role': 'trained',
        'method': 'GRPO',
        'train_data': list(SHAO_TRAIN),
        'eval_id': list(SHAO_EVAL_ID),
        'eval_ood': list(SHAO_EVAL_OOD),
        'ood_basis': 'inferred',
        'notes': (
            'Appendix J of Shao et al. v2: unlike the Qwen Instruct pair, '
            'ground-truth RLVR still gives a small MATH gain and limited '
            'AMC/AIME movement. Tracks Llama-3.1-8B more than the saturated '
            'Qwen Instruct checkpoints. Paper spelling Llama-3.1-Tulu-3-8B.'
        ),
        'checkpoint_origin': 'Llama-3.1-Tulu-3-8B (Tulu3 RLVR)',
        'reward_type': 'spurious-suite',
        'spurious_controls': 'random+incorrect+format',
        'contamination': 'control',
        'ckpt_select': 'unspecified',
    },
)

# Split a collapsed size-sweep row into one checkpoint per size.
SIZE_SPLITS = (
    {
        'key': SHAO,
        'model': 'Qwen2.5-Math-7B',
        'keep_model': 'Qwen2.5-Math-7B',
        'keep_sizes': ['7B'],
        'sibling_model': 'Qwen2.5-Math-1.5B',
        'sibling_sizes': ['1.5B'],
        'keep_notes': (
            'Shao et al. v2 main result. MATH-500: random reward +21.4 pp, '
            'ground truth +29.1 pp. Comparing only to the untuned checkpoint '
            'is not enough. Code-reasoning frequency 65% to >90% under '
            'spurious rewards; path analysis on this 7B checkpoint.'
        ),
        'sibling_notes': (
            'Spurious-reward gains on Qwen2.5-Math-1.5B; random reward is '
            'slower and weaker on AMC (+4.9 pp). Do not copy the 7B '
            'memorization mechanism onto this size.'
        ),
        'keep_contamination': 'direct-memorization',
        'sibling_contamination': 'spurious-gains',
    },
    {
        'key': SHAO,
        'model': 'Qwen2.5-7B',
        'keep_model': 'Qwen2.5-7B',
        'keep_sizes': ['7B'],
        'sibling_model': 'Qwen2.5-1.5B',
        'sibling_sizes': ['1.5B'],
        'keep_notes': (
            'General-purpose Qwen2.5-7B (Bad-Code). Some uninformative or '
            'incorrect rewards help; not the same as the Math-7B shortcut.'
        ),
        'sibling_notes': (
            'Qwen2.5-1.5B (No-Code in the paper; prompting still helps). '
            'Sensitivity to weak rewards, not a universal contamination claim.'
        ),
        'keep_contamination': 'sensitivity',
        'sibling_contamination': 'sensitivity',
    },
    {
        'key': ONESHOT,
        'model': 'Qwen2.5-Math-1.5B',
        'keep_model': 'Qwen2.5-Math-1.5B',
        'keep_sizes': ['1.5B'],
        'sibling_model': 'Qwen2.5-Math-7B',
        'sibling_sizes': ['7B'],
        'keep_notes': (
            'Headline 1-shot is π1 on Qwen2.5-Math-1.5B (also π13, 2-shot, '
            '16-shot). Format-reward and entropy-loss-only ablations. PPO '
            'also works (Tab. 4). Default report: best average on 6 benches. '
            'Appendix C.1.3 also lists best-per-benchmark scores.'
        ),
        'sibling_notes': (
            'Qwen2.5-Math-7B 1-shot with π1: +17.8 pp average, 5.9 pp above '
            'the format-reward baseline. Same checkpoint family Shao et al. '
            'show is highly sensitive to spurious rewards. Llama is also '
            'trained in this paper.'
        ),
        'keep_contamination': 'untested',
        'sibling_contamination': 'untested',
    },
)

PATCHES = (
    {
        'key': SHAO,
        'model': 'Qwen2.5-Math-7B',
        'reward_type': 'spurious-suite',
        'spurious_controls': 'random+incorrect+format',
        'contamination': 'direct-memorization',
        'ckpt_select': 'unspecified',
        'checkpoint_origin': 'Qwen2.5-Math-7B (base)',
        'ood_basis': 'inferred',
    },
    {
        'key': SHAO,
        'model': 'Qwen2.5-Math-1.5B',
        'reward_type': 'spurious-suite',
        'spurious_controls': 'random+incorrect+format',
        'contamination': 'spurious-gains',
        'ckpt_select': 'unspecified',
        'checkpoint_origin': 'Qwen2.5-Math-1.5B (base)',
        'ood_basis': 'inferred',
    },
    {
        'key': SHAO,
        'model': 'Qwen2.5-7B',
        'reward_type': 'spurious-suite',
        'spurious_controls': 'random+incorrect+format',
        'contamination': 'sensitivity',
        'ckpt_select': 'unspecified',
        'checkpoint_origin': 'Qwen2.5-7B (base)',
        'ood_basis': 'inferred',
    },
    {
        'key': SHAO,
        'model': 'Qwen2.5-1.5B',
        'reward_type': 'spurious-suite',
        'spurious_controls': 'random+incorrect+format',
        'contamination': 'sensitivity',
        'ckpt_select': 'unspecified',
        'checkpoint_origin': 'Qwen2.5-1.5B (base)',
        'ood_basis': 'inferred',
    },
    {
        'key': SHAO,
        'model': 'Llama3.1-8B',
        'reward_type': 'spurious-suite',
        'spurious_controls': 'random+incorrect+format',
        'contamination': 'control',
        'ckpt_select': 'unspecified',
        'checkpoint_origin': 'Llama-3.1-8B (base)',
    },
    {
        'key': SHAO,
        'model': 'Llama3.1-8B-Instruct',
        'reward_type': 'spurious-suite',
        'spurious_controls': 'random+incorrect+format',
        'contamination': 'control',
        'ckpt_select': 'unspecified',
        'checkpoint_origin': 'Llama-3.1-8B-Instruct',
    },
    {
        'key': SHAO,
        'model': 'Llama3.2-3B',
        'reward_type': 'spurious-suite',
        'spurious_controls': 'random+incorrect+format',
        'contamination': 'control',
        'ckpt_select': 'unspecified',
        'checkpoint_origin': 'Llama-3.2-3B (base)',
    },
    {
        'key': SHAO,
        'model': 'Llama3.2-3B-Instruct',
        'reward_type': 'spurious-suite',
        'spurious_controls': 'random+incorrect+format',
        'contamination': 'control',
        'ckpt_select': 'unspecified',
        'checkpoint_origin': 'Llama-3.2-3B-Instruct',
    },
    {
        'key': SHAO,
        'model': 'OLMo2-7B',
        'reward_type': 'spurious-suite',
        'spurious_controls': 'random+incorrect+format',
        'contamination': 'control',
        'ckpt_select': 'unspecified',
        'checkpoint_origin': 'OLMo2-7B (base)',
    },
    {
        'key': SHAO,
        'model': 'OLMo2-7B-SFT',
        'reward_type': 'spurious-suite',
        'spurious_controls': 'random+incorrect+format',
        'contamination': 'control',
        'ckpt_select': 'unspecified',
        'checkpoint_origin': 'OLMo2-7B-SFT',
    },
    {
        'key': YAN,
        'model': 'Qwen2.5-Math-7B',
        'start_point': 'base',
        'reward_type': 'spurious-suite',
        'spurious_controls': 'random+incorrect+format',
        'contamination': 'direct-memorization',
        'ckpt_select': 'unspecified',
        'checkpoint_origin': 'Qwen2.5-Math-7B (base vs Shao spurious RLVR)',
        'notes': (
            'Original checkpoint vs Shao et al. 2025 spurious RLVR-tuned. '
            'MATH-500 and MinervaMath are the contamination analysis sets; '
            'LiveMathBench is the paper\'s leakage-free control. '
            'wrong→right is the analysis slice, not proof of leakage. '
            'Text-recovery and intervention checks are the evidence; do not '
            'extend that to every improved item or all Qwen models.'
        ),
    },
    {
        'key': YAN,
        'model': 'Qwen2.5-Math-7B',
        'start_point': 'rl-tuned',
        'reward_type': 'spurious-suite',
        'spurious_controls': 'random+incorrect+format',
        'contamination': 'direct-memorization',
        'ckpt_select': 'unspecified',
        'checkpoint_origin': 'Qwen2.5-Math-7B after Shao et al. spurious RLVR',
        'notes': (
            'Shao et al. 2025 spurious RLVR-tuned checkpoint '
            '(incorrect/random/format rewards). Mechanistic probes on this '
            'checkpoint. wrong→right is the analysis slice, not the proof.'
        ),
    },
    {
        'key': YAN,
        'model': 'Qwen3-8B',
        'reward_type': 'spurious-suite',
        'spurious_controls': 'random+incorrect+format',
        'contamination': 'weaker-than-qwen-math',
        'ckpt_select': 'unspecified',
        'checkpoint_origin': 'Qwen3-8B (studied checkpoint)',
        'notes': (
            'Same contamination marks as Qwen2.5-Math-7B on partial-prompt '
            'eval, weaker memory activation in path-patching. Status is for '
            'this checkpoint only. Do not extend to other Qwen3 sizes.'
        ),
    },
    {
        'key': YAN,
        'model': 'Llama-3.1-8B',
        'reward_type': 'spurious-suite',
        'spurious_controls': 'random+incorrect+format',
        'contamination': 'control',
        'ckpt_select': 'unspecified',
        'checkpoint_origin': 'Llama-3.1-8B (base)',
    },
    {
        'key': YAN,
        'model': 'OLMo-2-1124-7B',
        'reward_type': 'spurious-suite',
        'spurious_controls': 'random+incorrect+format',
        'contamination': 'control',
        'ckpt_select': 'unspecified',
        'checkpoint_origin': 'OLMo-2-1124-7B (base)',
    },
    {
        'key': ONESHOT,
        'model': 'Qwen2.5-Math-1.5B',
        'reward_type': 'ground-truth',
        'spurious_controls': 'format+entropy',
        'contamination': 'untested',
        'ckpt_select': 'mixed-avg-and-per-bench',
        'checkpoint_origin': 'Qwen2.5-Math-1.5B (base)',
    },
    {
        'key': ONESHOT,
        'model': 'Qwen2.5-Math-7B',
        'reward_type': 'ground-truth',
        'spurious_controls': 'format+entropy',
        'contamination': 'untested',
        'ckpt_select': 'mixed-avg-and-per-bench',
        'checkpoint_origin': 'Qwen2.5-Math-7B (base)',
    },
    {
        'key': ONESHOT,
        'model': 'Llama-3.2-3B-Instruct',
        'reward_type': 'ground-truth',
        'spurious_controls': 'format+entropy',
        'contamination': 'untested',
        'ckpt_select': 'mixed-avg-and-per-bench',
        'checkpoint_origin': 'Llama-3.2-3B-Instruct',
        'notes_suffix': (
            'Already a non-Qwen trained model in this paper. Smaller '
            'absolute gains; RLVR unstable (App. C.1).'
        ),
    },
    {
        'key': ONESHOT,
        'model': 'Qwen2.5-1.5B',
        'reward_type': 'ground-truth',
        'spurious_controls': 'format+entropy',
        'contamination': 'untested',
        'ckpt_select': 'mixed-avg-and-per-bench',
        'checkpoint_origin': 'Qwen2.5-1.5B (base)',
    },
    {
        'key': ONESHOT,
        'model': 'Qwen2.5-Math-1.5B-Instruct',
        'reward_type': 'ground-truth',
        'spurious_controls': 'format+entropy',
        'contamination': 'untested',
        'ckpt_select': 'mixed-avg-and-per-bench',
        'checkpoint_origin': 'Qwen2.5-Math-1.5B-Instruct',
    },
    {
        'key': ONESHOT,
        'model': 'DeepSeek-R1-Distill-Qwen1.5B',
        'reward_type': 'ground-truth',
        'spurious_controls': 'format+entropy',
        'contamination': 'untested',
        'ckpt_select': 'mixed-avg-and-per-bench',
        'checkpoint_origin': 'DeepSeek-R1-Distill-Qwen-1.5B',
    },
    {
        'key': ENTROPY,
        'model': 'Qwen2.5-Math-7B',
        'method': 'EM-FT / EM-RL',
        'reward_type': 'entropy',
        'spurious_controls': 'none-reported',
        'contamination': 'untested',
        'ckpt_select': 'unspecified',
        'checkpoint_origin': 'Qwen2.5-Math-7B (base)',
        'notes_suffix': (
            'Same Qwen2.5-Math-7B family Shao/Yan flag. No spurious-reward '
            'suite here.'
        ),
    },
    {
        'key': ENTROPY,
        'model': 'Llama-3.1-8B-Instruct',
        'method': 'EM-FT / EM-RL',
        'reward_type': 'entropy',
        'spurious_controls': 'none-reported',
        'contamination': 'untested',
        'ckpt_select': 'unspecified',
        'checkpoint_origin': 'Llama-3.1-8B-Instruct',
        'notes_suffix': (
            'Table 4: EM gains much smaller than on Qwen2.5. Result depends '
            'on confidence tracking correctness.'
        ),
    },
    {
        'key': SKPO,
        'model': 'Qwen2.5-Math-7B',
        'reward_type': 'ground-truth',
        'spurious_controls': 'none-reported',
        'contamination': 'untested',
        'ckpt_select': 'unspecified',
        'checkpoint_origin': 'Qwen2.5-Math-7B (base)',
        'notes_suffix': (
            'Trains Qwen and Llama; MMLU-Pro and LiveCodeBench are the paper '
            'OOD pair. That is transfer, not a spurious-reward control.'
        ),
    },
    {
        'key': SKPO,
        'model': 'Llama-3.2-3B-Instruct',
        'reward_type': 'ground-truth',
        'spurious_controls': 'none-reported',
        'contamination': 'untested',
        'ckpt_select': 'unspecified',
        'checkpoint_origin': 'Llama-3.2-3B-Instruct',
    },
    {
        'key': RLVE,
        'method': 'RLVE (DAPO)',
        'reward_type': 'environment',
        'spurious_controls': 'held-out-envs',
        'contamination': 'untested',
        'ckpt_select': 'unspecified',
        'notes_suffix': (
            'D_ood: 50 environments unseen in training, 2,500 generated '
            'problems. Keep this split from any DeepMath run on the same '
            'checkpoint.'
        ),
    },
    {
        'key': RLVE,
        'method': 'DAPO',
        'model': 'OpenThinker3-1.5B',
        'reward_type': 'ground-truth',
        'spurious_controls': 'none-reported',
        'contamination': 'untested',
        'ckpt_select': 'unspecified',
        'checkpoint_origin': 'OpenThinker3-1.5B on DeepMath-103K',
        'notes_suffix': (
            'DeepMath math RLVR. Do not read RLVE-Gym D_ood as this run\'s OOD.'
        ),
    },
)


def _match(row: dict, spec: dict) -> bool:
    if row.get('key') != spec.get('key'):
        return False
    if spec.get('model') and row.get('model') != spec['model']:
        return False
    if spec.get('method') and row.get('method') != spec['method']:
        return False
    if spec.get('start_point') and row.get('start_point') != spec['start_point']:
        return False
    return True


def _has_model(rows: list[dict], key: str, model: str) -> bool:
    return any(row.get('key') == key and row.get('model') == model for row in rows)


def _split_size_sweeps(rows: list[dict]) -> list[dict]:
    out = []
    for row in rows:
        rule = next(
            (
                item for item in SIZE_SPLITS
                if item['key'] == row.get('key') and item['model'] == row.get('model')
            ),
            None,
        )
        sizes = row.get('sizes') or []
        if rule is None or not (
            set(rule['keep_sizes']) <= set(sizes)
            and set(rule['sibling_sizes']) <= set(sizes)
        ):
            out.append(row)
            continue
        kept = dict(row)
        kept['model'] = rule['keep_model']
        kept['sizes'] = list(rule['keep_sizes'])
        kept['notes'] = rule['keep_notes']
        kept['contamination'] = rule['keep_contamination']
        out.append(kept)
        if not _has_model(rows, rule['key'], rule['sibling_model']) and not _has_model(
            out, rule['key'], rule['sibling_model'],
        ):
            sibling = dict(row)
            sibling['model'] = rule['sibling_model']
            sibling['sizes'] = list(rule['sibling_sizes'])
            sibling['notes'] = rule['sibling_notes']
            sibling['contamination'] = rule['sibling_contamination']
            out.append(sibling)
    return out


def _append_notes(row: dict, suffix: str) -> None:
    suffix = (suffix or '').strip()
    if not suffix:
        return
    notes = (row.get('notes') or '').strip()
    if suffix in notes:
        return
    row['notes'] = f'{notes} {suffix}'.strip() if notes else suffix


def _apply_patches(rows: list[dict]) -> None:
    fields = (
        'checkpoint_origin',
        'reward_type',
        'spurious_controls',
        'contamination',
        'ckpt_select',
        'ood_basis',
    )
    for spec in PATCHES:
        for row in rows:
            if not _match(row, spec):
                continue
            for field in fields:
                value = spec.get(field)
                if value:
                    row[field] = value
            if spec.get('notes'):
                row['notes'] = spec['notes']
            elif spec.get('notes_suffix'):
                _append_notes(row, spec['notes_suffix'])


def _inject_extra_rows(
    rows: list[dict],
    papers_by_key: dict[str, dict],
    normalize_row,
) -> list[dict]:
    existing = {(row.get('key'), row.get('model')) for row in rows}
    added = []
    for raw in EXTRA_ROWS:
        if (raw['key'], raw['model']) in existing:
            continue
        paper = papers_by_key.get(raw['key']) or {
            'key': raw['key'],
            'line_title': PAPER_META.get(raw['key'], {}).get('title') or raw['key'],
            'section': PAPER_META.get(raw['key'], {}).get('section') or '',
        }
        added.append(normalize_row(raw, paper))
        existing.add((raw['key'], raw['model']))
    if added:
        print(f'injected {len(added)} missing Appendix J rows', flush=True)
    return rows + added


def apply_reliability(
    rows: list[dict],
    papers_by_key: dict[str, dict] | None = None,
    normalize_row=None,
) -> list[dict]:
    papers_by_key = papers_by_key or {}
    rows = _split_size_sweeps(rows)
    if normalize_row is not None:
        rows = _inject_extra_rows(rows, papers_by_key, normalize_row)
    _apply_patches(rows)
    return rows
