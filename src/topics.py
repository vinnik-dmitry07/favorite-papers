'''Primary fields + secondary idea tags for the citation map.

Each paper gets exactly one field (node colour) and at most two idea tags
(filter chips). Fields are the communities that cite each other; ideas are
the mechanisms that migrate across fields.

Assignment order: explicit id override, then section default, then title
heuristics. Ideas: explicit id list, then conservative keyword matches.

Run:  python src/topics.py          # coverage on the catalog
      python src/build_graph.py     # writes tags onto graph.json
'''

from __future__ import annotations

import sys
from collections import Counter
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))

from common import CATALOG, load_json  # noqa: E402

MAX_IDEAS = 2

# Short name, colour, hue family. Families share a hue so ~20 fields stay
# readable; the field shade is what the node uses.
FIELDS: list[tuple[str, str, str]] = [
    ('Deep RL', '#1e3f7a', 'RL'),
    ('RLVR', '#3d7fd6', 'RL'),
    ('Reasoning', '#e8891f', 'Reasoning'),
    ('Latent', '#a4501a', 'Reasoning'),
    ('Architectures', '#7d5cc9', 'Models'),
    ('Diffusion', '#b58fe6', 'Models'),
    ('Inter-model', '#5e1d8c', 'Models'),
    ('Optimizers', '#1b5e20', 'Training'),
    ('Scaling', '#a5d6a7', 'Training'),
    ('Dynamics', '#43a047', 'Training'),
    ('Continual', '#7cb342', 'Training'),
    ('Interp', '#c2408a', 'Understanding'),
    ('Repr', '#e18fc0', 'Understanding'),
    ('Open-ended', '#68d2e2', 'Agents'),
    ('Self-improve', '#1fa89e', 'Agents'),
    ('Harness', '#0b6b66', 'Agents'),
    ('Discovery', '#228eaa', 'Agents'),
    ('Safety', '#d43d3d', 'Mind'),
    ('Consciousness', '#8e1d3c', 'Mind'),
    ('NeuroAI', '#ef8c78', 'Mind'),
    ('SSL', '#b89a14', 'SSL'),
    ('Finance', '#6b5e4e', 'Other'),
    ('Other', '#9aa3ab', 'Other'),
]

FIELD_SET = {name for name, _, _ in FIELDS}
FIELD_COLOR = {name: color for name, color, _ in FIELDS}
FIELD_FAMILY = {name: family for name, _, family in FIELDS}

IDEAS = (
    'self-distill',
    'self-refine',
    'evolution',
    'world models',
    'memory',
    'curriculum',
    'forgetting',
    'priming',
    'prompts',
    'enc-dec',
    'arithmetic',
    'critique',
    'GRPO',
)

SECTION_FIELD = {
    'Reinforcement learning': 'Deep RL',
    'Post-training': 'RLVR',
    'LLMs: architectures, context, training': 'Architectures',
    'Reasoning and the "physics" of language models': 'Reasoning',
    'Data, training, optimization': None,
    'Self-supervised learning and vision': 'SSL',
    'Retrieval, embeddings, benchmarks': 'Other',
    'Agents, open-endedness, AGI': 'Self-improve',
    'Harness': 'Harness',
    'AI safety and consciousness': 'Safety',
    'NeuroAI': 'NeuroAI',
    'Representation alignment': 'Repr',
    'Finance': 'Finance',
    'Books': 'Other',
    'Other': 'Other',
}

# Papers whose contribution is not the section default. Prefer this over
# stretching a keyword rule.
FIELD_BY_ID: dict[str, str] = {
    # RL section that is not Deep RL
    'arxiv:2509.09675': 'RLVR',
    'arxiv:2312.00276': 'Continual',
    # Post-training that is not RLVR
    'arxiv:2608.09888': 'Latent',
    'arxiv:2607.07847': 'Continual',
    'arxiv:2607.05609': 'Continual',
    'arxiv:2606.23740': 'Dynamics',
    'arxiv:2601.20861': 'Continual',
    'arxiv:2601.19897': 'Continual',
    'arxiv:2601.16175': 'Discovery',
    'arxiv:2601.14525': 'Discovery',
    'arxiv:2510.14901': 'Reasoning',
    'arxiv:2506.13585': 'Reasoning',
    'arxiv:2504.16084': 'Reasoning',
    'arxiv:2303.17651': 'Reasoning',
    # Architectures that split out
    'arxiv:2608.11676': 'Inter-model',
    'arxiv:2608.03893': 'Inter-model',
    'arxiv:2608.00146': 'Diffusion',
    'arxiv:2606.06574': 'Latent',
    'arxiv:2605.22863': 'Inter-model',
    'arxiv:2604.08302': 'Diffusion',
    'arxiv:2603.05454': 'Diffusion',
    'arxiv:2602.08676': 'Diffusion',
    'arxiv:2512.24601': 'Latent',
    'arxiv:2512.15745': 'Diffusion',
    'arxiv:2511.09149': 'Inter-model',
    'arxiv:2510.03215': 'Inter-model',
    'arxiv:2507.10524': 'Latent',
    'url:pub.sakana.ai/ctm': 'Latent',
    'arxiv:2502.09992': 'Diffusion',
    'arxiv:2501.14082': 'Inter-model',
    'url:ai.meta.com/research/publications/large-concept-models-language-modeling-in-a-sentence-representation-space': 'Inter-model',
    'arxiv:2405.12250': 'Dynamics',
    'arxiv:2207.02098': 'Dynamics',
    'url:people.idsia.ch/~juergen/most-cited-neural-nets.html': 'Other',
    # Reasoning that is not Reasoning
    'doi:10.1073/pnas.2520095123': 'Consciousness',
    'arxiv:2606.31779': 'Latent',
    'arxiv:2606.25010': 'Dynamics',
    'arxiv:2606.03982': 'Interp',
    'arxiv:2604.11791': 'Latent',
    'arxiv:2602.10416': 'Interp',
    'arxiv:2510.00184': 'Interp',
    'arxiv:2509.25239': 'Latent',
    'arxiv:2509.20317': 'Latent',
    'arxiv:2508.02513': 'Interp',
    'arxiv:2506.10947': 'RLVR',
    'url:safe-lip-9a8.notion.site/incorrect-baseline-evaluations-call-into-question-recent-llm-rl-claims-2012f1fbf0ee8094ab8ded1953c15a37': 'RLVR',
    'arxiv:2505.21493': 'RLVR',
    'arxiv:2505.21444': 'RLVR',
    'arxiv:2505.15134': 'RLVR',
    'arxiv:2505.13763': 'Interp',
    'arxiv:2504.20571': 'RLVR',
    'arxiv:2503.21676': 'Dynamics',
    'arxiv:2502.19981': 'Interp',
    'arxiv:2502.05171': 'Latent',
    'arxiv:2502.00873': 'Interp',
    'arxiv:2412.06769': 'Latent',
    'arxiv:2410.21272': 'Interp',
    'arxiv:2305.13673': 'Dynamics',
    'arxiv:2407.20311': 'Dynamics',
    'arxiv:2309.14316': 'Dynamics',
    'arxiv:2309.14402': 'Dynamics',
    'arxiv:2404.05405': 'Dynamics',
    'arxiv:2407.15017': 'Interp',
    'doi:10.1038/s41586-024-07522-w': 'Consciousness',
    'arxiv:2406.11813': 'Dynamics',
    'arxiv:2406.11741': 'Dynamics',
    'arxiv:2406.03445': 'Interp',
    'arxiv:2405.15071': 'Dynamics',
    'arxiv:2405.14838': 'Latent',
    'doi:10.1038/d41586-024-01413-w': 'Discovery',
    'arxiv:2312.13558': 'Interp',
    'openreview:hcQfTsVnBo': 'Dynamics',
    'arxiv:2309.12288': 'Dynamics',
    'arxiv:2304.15004': 'Dynamics',
    'arxiv:2301.06627': 'Consciousness',
    'arxiv:2301.05217': 'Dynamics',
    'url:ai.googleblog.com/2022/11/characterizing-emergent-phenomena-in.html': 'Dynamics',
    # Data / training (no useful section default)
    'arxiv:2608.05136': 'Optimizers',
    'arxiv:2607.27372': 'Scaling',
    'arxiv:2601.21343': 'Scaling',
    'arxiv:2512.24695': 'Continual',
    'arxiv:2510.05491': 'Optimizers',
    'arxiv:2508.11408': 'RLVR',
    'arxiv:2507.12856': 'RLVR',
    'arxiv:2506.08007': 'RLVR',
    'arxiv:2505.24832': 'Dynamics',
    'arxiv:2410.07041': 'Dynamics',
    'url:iclr.cc/virtual/2025/poster/30565': 'Optimizers',
    'arxiv:2409.03137': 'Optimizers',
    'arxiv:2405.20541': 'Scaling',
    'arxiv:2405.20233': 'Dynamics',
    'arxiv:2405.18392': 'Scaling',
    'url:epochai.org/blog/training-compute-of-frontier-ai-models-grows-by-4-5x-per-year': 'Scaling',
    'arxiv:2405.16684': 'Scaling',
    'arxiv:2405.15682': 'Optimizers',
    'url:educatingsilicon.com/2024/05/09/how-much-llm-training-data-is-there-in-the-limit': 'Scaling',
    'arxiv:2403.05175': 'Continual',
    'arxiv:2402.02342': 'Optimizers',
    'arxiv:2401.17401': 'Continual',
    'arxiv:2312.17742': 'SSL',
    'arxiv:2312.10549': 'Continual',
    'arxiv:2307.06440': 'Scaling',
    'doi:10.1038/s41586-024-07711-7': 'Continual',
    'arxiv:2305.14342': 'Optimizers',
    'arxiv:2302.06675': 'Optimizers',
    'arxiv:2212.14034': 'Scaling',
    'arxiv:2210.10760': 'Scaling',
    'arxiv:2110.09485': 'Dynamics',
    'arxiv:2108.06325': 'Continual',
    'arxiv:2010.01412': 'Optimizers',
    'arxiv:2009.11848': 'Dynamics',
    'arxiv:2009.11243': 'Optimizers',
    'arxiv:2001.08361': 'Scaling',
    'url:openai.com/index/deep-double-descent': 'Dynamics',
    'url:paperswithcode.com/paper/optimizing-millions-of-hyperparameters-by': 'Optimizers',
    'arxiv:1904.00962': 'Optimizers',
    'arxiv:1803.03635': 'Dynamics',
    'openreview:ry_WPG-A-': 'Dynamics',
    'arxiv:1708.07120': 'Optimizers',
    'arxiv:1708.02072': 'Continual',
    'doi:10.1073/pnas.1611835114': 'Continual',
    'arxiv:1506.01186': 'Optimizers',
    # SSL that is not SSL
    'arxiv:2604.09168': 'Latent',
    # Retrieval / benches
    'arxiv:2606.18543': 'Open-ended',
    'arxiv:2410.07095': 'Discovery',
    'arxiv:2402.16822': 'Safety',
    'arxiv:2402.12483': 'Reasoning',
    'arxiv:2311.16452': 'Reasoning',
    'url:selfrag.github.io': 'Harness',
    'arxiv:2309.16797': 'Self-improve',
    'arxiv:2304.08467': 'Architectures',
    'arxiv:2212.14024': 'Harness',
    'arxiv:2206.04615': 'Reasoning',
    'acl:2022.acl-long.360': 'Architectures',
    'arxiv:2101.02235': 'Reasoning',
    # Agents
    'arxiv:2608.23875': 'Open-ended',
    'arxiv:2608.19197': 'Open-ended',
    'arxiv:2602.07755': 'Continual',
    'arxiv:2601.21557': 'Harness',
    'arxiv:2601.03192': 'Harness',
    'arxiv:2512.18746': 'Harness',
    'arxiv:2511.15593': 'Discovery',
    'arxiv:2507.18074': 'Discovery',
    'arxiv:2502.15840': 'Open-ended',
    'arxiv:2408.08435': 'Harness',
    'arxiv:2407.00695': 'Discovery',
    'arxiv:2406.04268': 'Open-ended',
    'arxiv:2402.16823': 'Harness',
    'url:research.google/blog/few-shot-tool-use-doesnt-really-work-yet': 'Harness',
    'openreview:pOoKI3ouv1': 'Deep RL',
    'doi:10.1038/s42256-023-00754-x': 'Open-ended',
    'arxiv:2311.02462': 'Open-ended',
    'arxiv:2311.00344': 'Open-ended',
    'doi:10.1038/s41586-023-06924-6': 'Discovery',
    'url:lilianweng.github.io/posts/2023-06-23-agent': 'Harness',
    'url:minedojo.org': 'Open-ended',
    'arxiv:1905.10985': 'Open-ended',
    'arxiv:1901.01753': 'Open-ended',
    # Harness that is not Harness
    'url:weco.ai/blog/first-evidence-of-recursive-self-improvement': 'Self-improve',
    'arxiv:2604.19341': 'Discovery',
    # Safety / consciousness
    'arxiv:2607.23379': 'Interp',
    'arxiv:2603.19426': 'Interp',
    'url:transformer-circuits.pub/2025/introspection': 'Consciousness',
    'url:anthropic.com/research/tracing-thoughts-language-model': 'Interp',
    'url:transformer-circuits.pub/2025/attribution-graphs/methods.html': 'Interp',
    'url:transformer-circuits.pub/2025/attribution-graphs/biology.html': 'Interp',
    'arxiv:2503.16348': 'Consciousness',
    'url:alignmentforum.org/posts/nffst5mio7bcaqhpa/an-extremely-opinionated-annotated-list-of-my-favourite-1': 'Interp',
    'url:anthropic.com/news/mapping-mind-language-model': 'Interp',
    'arxiv:2309.08600': 'Interp',
    'arxiv:2308.08708': 'Consciousness',
    'arxiv:2303.07103': 'Consciousness',
    # NeuroAI
    'url:herasight-project.webflow.io/technical-paper/cogpgt-1': 'Other',
    'url:cell.com/iscience/fulltext/s2589-0042(25)00289-5': 'Consciousness',
    'url:rlhfbook.com': 'RLVR',
    'arxiv:2201.09746': 'Deep RL',
    'url:neuroevolutionbook.com': 'Deep RL',
}

IDEAS_BY_ID: dict[str, list[str]] = {
    'arxiv:2608.17163': ['world models'],
    'url:diamond-wm.github.io': ['world models'],
    'arxiv:2301.04104': ['world models'],
    'arxiv:1712.06567': ['evolution'],
    'arxiv:2608.13040': ['self-distill'],
    'arxiv:2606.18810': ['GRPO'],
    'arxiv:2606.06021': ['self-distill'],
    'arxiv:2605.22074': ['curriculum'],
    'arxiv:2604.20659': ['GRPO'],
    'arxiv:2604.13016': ['self-distill'],
    'arxiv:2604.02288': ['self-distill', 'GRPO'],
    'arxiv:2603.25562': ['self-distill'],
    'arxiv:2603.24472': ['self-distill'],
    'arxiv:2602.09000': ['GRPO', 'self-refine'],
    'arxiv:2601.20861': ['evolution', 'forgetting'],
    'arxiv:2601.20802': ['self-distill'],
    'arxiv:2601.19897': ['self-distill'],
    'arxiv:2601.18734': ['self-distill'],
    'arxiv:2601.11061': ['critique'],
    'url:cameronrwolfe.substack.com/p/grpo-tricks': ['GRPO'],
    'arxiv:2512.02807': ['GRPO'],
    'arxiv:2511.07317': ['curriculum'],
    'arxiv:2510.13786': [],  # scaling is a field, not stacked here
    'arxiv:2510.00977': ['GRPO'],
    'arxiv:2509.14234': ['self-refine'],
    'arxiv:2507.19457': ['evolution', 'prompts'],
    'arxiv:2507.18071': ['GRPO'],
    'arxiv:2506.06632': ['curriculum'],
    'arxiv:2506.03106': ['GRPO'],
    'arxiv:2505.10978': ['GRPO'],
    'arxiv:2504.13837': ['critique'],
    'arxiv:2503.20783': ['GRPO'],
    'arxiv:2503.02875': ['priming'],
    'arxiv:2503.00735': ['self-refine'],
    'arxiv:2402.13669': ['self-distill'],
    'arxiv:2402.03300': ['GRPO'],
    'arxiv:2303.17651': ['self-refine'],
    'arxiv:2607.02303': ['memory'],
    'arxiv:2512.14856': ['enc-dec'],
    'arxiv:2510.26622': ['enc-dec'],
    'arxiv:2504.06225': ['enc-dec'],
    'arxiv:2412.13663': ['enc-dec'],
    'arxiv:2404.09173': ['memory'],
    'arxiv:2203.08913': ['memory'],
    'arxiv:2605.07654': ['priming'],
    'arxiv:2604.01754': ['critique'],
    'arxiv:2606.03982': ['arithmetic'],
    'arxiv:2602.10416': ['arithmetic'],
    'arxiv:2510.00184': ['arithmetic'],
    'arxiv:2508.02513': ['arithmetic'],
    'arxiv:2506.10947': ['critique'],
    'url:safe-lip-9a8.notion.site/incorrect-baseline-evaluations-call-into-question-recent-llm-rl-claims-2012f1fbf0ee8094ab8ded1953c15a37': ['critique'],
    'arxiv:2505.21444': ['self-refine'],
    'arxiv:2502.19981': ['arithmetic'],
    'arxiv:2502.00873': ['arithmetic'],
    'arxiv:2410.21272': ['arithmetic'],
    'arxiv:2406.03689': ['world models'],
    'arxiv:2406.03445': ['arithmetic'],
    'openreview:wUU-7XTL5XO': ['critique'],
    'arxiv:2601.21343': ['self-refine'],
    'arxiv:2302.06675': ['evolution'],
    'doi:10.1038/s41586-024-07711-7': ['forgetting'],
    'arxiv:2403.05175': ['forgetting'],
    'arxiv:2312.10549': ['forgetting'],
    'arxiv:1708.02072': ['forgetting'],
    'doi:10.1073/pnas.1611835114': ['forgetting'],
    'arxiv:2605.26379': ['world models'],
    'arxiv:2606.18543': ['critique'],
    'arxiv:2410.07095': ['critique'],
    'arxiv:2402.12483': ['critique'],
    'arxiv:2309.16797': ['evolution', 'prompts'],
    'arxiv:2304.08467': ['priming'],
    'arxiv:2212.14024': ['prompts'],
    'arxiv:2206.04615': ['critique'],
    'acl:2022.acl-long.360': ['enc-dec'],
    'arxiv:2101.02235': ['critique'],
    'arxiv:2311.16452': ['prompts'],
    'arxiv:2608.19197': ['curriculum'],
    'arxiv:2605.13821': ['evolution'],
    'arxiv:2603.19461': ['evolution'],
    'arxiv:2602.07755': ['memory'],
    'arxiv:2601.21557': ['prompts'],
    'arxiv:2601.03192': ['memory'],
    'arxiv:2512.18746': ['memory', 'evolution'],
    'url:sakana.ai/shinka-evolve': ['evolution'],
    'arxiv:2508.16204': ['evolution'],
    'arxiv:2507.18074': ['evolution'],
    'arxiv:2505.22954': ['evolution'],
    'arxiv:2502.15840': ['critique'],
    'arxiv:2408.08435': ['evolution'],
    'openreview:pOoKI3ouv1': ['world models'],
    'doi:10.1038/s41586-023-06924-6': ['evolution'],
    'arxiv:1905.10985': ['evolution'],
    'arxiv:1901.01753': ['curriculum', 'evolution'],
    'url:github.com/alexisfox7/rgb-agent': ['memory'],
    'url:schema-harness.github.io': ['world models'],
    'arxiv:2606.01770': ['self-refine'],
    'doi:10.1371/journal.pcbi.1010628': ['forgetting'],
    'doi:10.1038/s41467-021-26568-2': ['evolution'],
    'url:neuroevolutionbook.com': ['evolution'],
}


def haystack(node: dict) -> str:
    return ' '.join(
        str(node.get(key) or '')
        for key in ('label', 'title', 'entry', 'id')
    ).lower()


def ideas_from_text(text: str) -> list[str]:
    found: list[str] = []

    def add(idea: str) -> None:
        if idea not in found:
            found.append(idea)

    if any(tok in text for tok in (
        'grpo', 'gspo', 'gigpo', 'igrpo', 'group relative',
        'group sequence policy',
    )):
        add('GRPO')
    if any(tok in text for tok in (
        'self-distil', 'self distillation', 'self-distillation',
        'on-policy distillation', 'on-policy representation distillation',
        'on-policy self-distillation',
    )):
        add('self-distill')
    if any(tok in text for tok in (
        'self-refine', 'self-feedback', 'iterative refinement',
    )):
        add('self-refine')
    if 'world model' in text:
        add('world models')
    if any(tok in text for tok in (
        'catastrophic forget', 'catastrophic forgetting', 'loss of plasticity',
    )):
        add('forgetting')
    if any(tok in text for tok in (
        'prefix tun', 'prefix consist', 'priming', 'gist token',
        'first few tokens', 'upft',
    )):
        add('priming')
    if 'encoder-decoder' in text or 'encoder decoder' in text:
        add('enc-dec')
    if 'curriculum' in text:
        add('curriculum')
    if any(tok in text for tok in (
        'neuroevolution', 'genetic algorithm', 'evolutionary strateg',
        'darwin gödel', 'darwin godel', 'gödel machine', 'godel machine',
        'funsearch', 'promptbreeder', 'shinkaevolve',
    )):
        add('evolution')
    if any(tok in text for tok in (
        'memrl', 'memevolve', 'episodic memory', 'hippocamp',
        'working memory', 'agent memory',
    )):
        add('memory')
    if any(tok in text for tok in (
        'arithmetic', 'digit by digit', 'trigonometry', 'fourier features',
        'why can\'t transformers learn multiplication',
        'lookahead limitation',
    )):
        add('arithmetic')
    if any(tok in text for tok in (
        'spurious reward', 'incorrect baseline', 'planbench',
        'vending-bench', 'mle-bench', 'ceo-bench', 'big-bench',
        'strategyqa', 'emergent abilities of llms a mirage',
    )):
        add('critique')
    return found


def field_from_text(section: str, text: str) -> str:
    '''Fallback when the section has no single default (training data).'''
    if section == 'Data, training, optimization':
        if any(tok in text for tok in (
            'optimizer', 'adam', 'muon', 'lion', 'sophia', 'lamb',
            'schedule-free', 'ademamix', 'learning rate', 'hyperparameter',
            'sharpness-aware', 'cyclical', 'super-convergence',
        )):
            return 'Optimizers'
        if any(tok in text for tok in (
            'continual', 'forget', 'plasticity', 'ewc',
        )):
            return 'Continual'
        if any(tok in text for tok in (
            'grok', 'descent', 'lottery', 'extrapolat', 'memor',
            'bottleneck',
        )):
            return 'Dynamics'
        return 'Scaling'
    return 'Other'


def assign(node: dict) -> tuple[str, list[str]]:
    node_id = node.get('id') or ''
    section = node.get('section') or ''
    text = haystack(node)

    field = FIELD_BY_ID.get(node_id)
    if field is None:
        field = SECTION_FIELD.get(section)
    if field is None:
        field = field_from_text(section, text)
    if field not in FIELD_SET:
        field = 'Other'

    ideas: list[str] = []
    for idea in IDEAS_BY_ID.get(node_id) or []:
        if idea in IDEAS and idea not in ideas:
            ideas.append(idea)
    if node_id not in IDEAS_BY_ID:
        for idea in ideas_from_text(text):
            if idea not in ideas:
                ideas.append(idea)
            if len(ideas) >= MAX_IDEAS:
                break
    return field, ideas[:MAX_IDEAS]


def apply_topics(nodes: list[dict]) -> None:
    for node in nodes:
        field, ideas = assign(node)
        node['topic'] = field
        node['ideas'] = ideas
        node['tags'] = [field, *ideas]


def taxonomy() -> dict:
    return {
        'fields': [
            {'id': name, 'color': color, 'family': family}
            for name, color, family in FIELDS
        ],
        'ideas': list(IDEAS),
    }


def print_coverage(nodes: list[dict]) -> None:
    fields = Counter(node.get('topic') for node in nodes)
    ideas = Counter(
        idea for node in nodes for idea in (node.get('ideas') or [])
    )
    n = len(nodes)
    tagged = sum(1 for node in nodes if node.get('topic'))
    idea_n = sum(len(node.get('ideas') or []) for node in nodes)
    print(f'topics              {tagged}/{n} papers have a field')
    print(f'ideas/paper         {idea_n / n:.2f} mean, cap {MAX_IDEAS}')
    print('fields')
    for name, _, family in FIELDS:
        print(f'  {fields.get(name, 0):3d}  {name:16s} ({family})')
    extra = [key for key in fields if key not in FIELD_SET]
    for key in extra:
        print(f'  {fields[key]:3d}  {key}  (unknown)')
    print('ideas')
    for idea in IDEAS:
        print(f'  {ideas.get(idea, 0):3d}  {idea}')


def print_mixing(nodes: list[dict], edges: list[tuple]) -> None:
    '''Macro citation mix: same-field rate and the strongest crossings.'''
    field_of = {node['id']: node.get('topic') for node in nodes}
    mix: Counter[tuple[str, str]] = Counter()
    for src, dst, _evidence in edges:
        a, b = field_of.get(src), field_of.get(dst)
        if a and b:
            mix[(a, b)] += 1
    total = sum(mix.values())
    same = sum(n for (a, b), n in mix.items() if a == b)
    if not total:
        print('topic mix            no edges')
        return
    print(f'topic mix            same-field {same / total:.2f} of {total} edges')
    print('  strongest within-field')
    within = [((a, b), n) for (a, b), n in mix.items() if a == b]
    for (a, _b), n in sorted(within, key=lambda item: -item[1])[:8]:
        print(f'    {n:3d}  {a}')
    print('  strongest crossings (idea migration candidates)')
    cross = [((a, b), n) for (a, b), n in mix.items() if a != b]
    for (a, b), n in sorted(cross, key=lambda item: -item[1])[:12]:
        print(f'    {n:3d}  {a:16s} → {b}')


def main() -> None:
    catalog = load_json(CATALOG, [])
    if not catalog:
        raise SystemExit('assets/catalog.json missing - run src/parse_readme.py')
    apply_topics(catalog)
    print_coverage(catalog)
    missing = [
        node['id'] for node in catalog
        if node['id'] not in FIELD_BY_ID
        and SECTION_FIELD.get(node.get('section')) is None
    ]
    if missing:
        print(f'no explicit field    {len(missing)} (section fallback / heuristic)')
        for node_id in missing[:20]:
            print(f'  {node_id}')


if __name__ == '__main__':
    main()
