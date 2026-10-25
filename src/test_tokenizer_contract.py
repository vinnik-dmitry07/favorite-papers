'''Pinned HF tokenizer regression IDs and identity invalidation, no model loads.'''

from copy import deepcopy
import json
from pathlib import Path
import sys

import pytest

sys.path.insert(0, str(Path(__file__).resolve().parent))
from build_agent_index import (  # noqa: E402
    BuildError, WordPieceTokenizer, build_signature, embedding_signature,
    load_embed,
)


def test_pinned_hf_special_tokens_and_normalization():
    config = load_embed()
    fixture = json.loads((Path(__file__).resolve().parents[1]
                          / 'worker/fixtures/tokenizer_added_tokens.json').read_text())
    assert fixture['model_revision'] == config['tokenizer']['revision']
    assert fixture['added_tokens'] == config['tokenizer']['added_tokens']
    tokenizer = WordPieceTokenizer(config)
    for case in fixture['cases']:
        assert tokenizer.token_ids(case['template'], case['text']) == case['ids'], case['name']


@pytest.mark.parametrize('key,value', [
    ('algorithm_version', 3), ('do_lower_case', False),
    ('strip_accents', False), ('tokenize_chinese_chars', False),
    ('max_input_chars_per_word', 99), ('revision', 'different-revision'),
    ('added_tokens', []),
])
def test_tokenizer_changes_invalidate_build_and_embedding_identities(key, value):
    original = load_embed()
    changed = deepcopy(original)
    changed['tokenizer'][key] = value
    assert build_signature(original) != build_signature(changed)
    assert embedding_signature(original) != embedding_signature(changed)


def test_old_algorithm_and_unsupported_added_token_behavior_fail_closed():
    config = load_embed()
    config['tokenizer']['algorithm_version'] = 1
    with pytest.raises(BuildError, match='algorithm version'):
        WordPieceTokenizer(config)
    config['tokenizer']['algorithm_version'] = 2
    config['tokenizer']['added_tokens'][0]['normalized'] = True
    with pytest.raises(BuildError, match='added-token semantics'):
        WordPieceTokenizer(config)
