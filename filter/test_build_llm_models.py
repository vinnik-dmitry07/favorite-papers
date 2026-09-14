'''Anti-regression tests for the LLM inventory builder.'''

from __future__ import annotations

import json
import sys
import tempfile
import unittest
from pathlib import Path

FILTER_DIR = Path(__file__).resolve().parent
sys.path.insert(0, str(FILTER_DIR))

import build_llm_models as blm


def _paper(key='arxiv:2501.00001', title='Demo', section='Post-training'):
    return {'key': key, 'line_title': title, 'section': section}


def _norm(raw, paper=None):
    return blm.normalize_row(raw, paper or _paper())


class SizeInferenceTest(unittest.TestCase):
    def test_api_mini_is_not_5m(self):
        row = _norm({
            'model': 'GPT-5 mini',
            'sizes': ['5M'],
            'start_point': 'api',
            'role': 'judge/reward',
        })
        self.assertEqual(row['sizes'], [])

    def test_gpt_4_1_mini_is_not_4_1m(self):
        row = _norm({
            'model': 'GPT-4.1 mini',
            'sizes': ['4.1M'],
            'start_point': 'api',
        })
        self.assertEqual(row['sizes'], [])

    def test_qwen_max_is_not_3_7m(self):
        row = _norm({
            'model': 'Qwen 3.7 Max',
            'sizes': ['3.7M'],
            'start_point': 'api',
        })
        self.assertEqual(row['sizes'], [])

    def test_explicit_billions_kept(self):
        row = _norm({
            'model': 'Qwen2.5-7B-Instruct',
            'sizes': [],
            'start_point': 'instruct',
        })
        self.assertEqual(row['sizes'], ['7B'])

    def test_gpt2_keeps_124m(self):
        row = _norm({
            'model': 'GPT-2',
            'sizes': ['124M'],
            'start_point': 'base',
        })
        self.assertEqual(row['sizes'], ['124M'])


class FamilyGenerationTest(unittest.TestCase):
    def test_gpt_oss_is_own_family(self):
        row = _norm({
            'model': 'GPT-OSS-120B',
            'family': 'GPT',
            'generation': 'OSS',
            'sizes': ['120B'],
            'start_point': 'unknown',
        })
        self.assertEqual(row['family'], 'GPT-OSS')
        self.assertEqual(row['generation'], '')
        self.assertEqual(row['sizes'], ['120B'])

    def test_distill_qwen_unifies_variant(self):
        row = _norm({
            'model': 'DeepSeek-R1-Distill-Qwen-7B',
            'family': 'DeepSeek',
            'generation': 'R1',
            'variant': 'Qwen',
            'start_point': 'reasoning-distilled',
        })
        self.assertEqual(row['variant'], 'Distill-Qwen')
        self.assertEqual(row['generation'], 'R1')

    def test_llada_2_0_not_collapsed(self):
        row = _norm({
            'model': 'LLaDA-2.0-mini',
            'family': 'LLaDA',
            'generation': '2.0',
            'start_point': 'instruct',
        })
        self.assertEqual(row['generation'], '2.0')

    def test_llada_8b_generation_is_not_8(self):
        row = _norm({
            'model': 'LLaDA-8B',
            'family': 'LLaDA',
            'generation': '8',
            'start_point': 'base',
        })
        self.assertEqual(row['generation'], '')
        self.assertEqual(row['sizes'], ['8B'])

    def test_tulu_umlaut_aliases(self):
        self.assertEqual(blm.norm_family('Tülu'), 'Tulu')
        self.assertEqual(blm.norm_family('Tulu'), 'Tulu')

    def test_gpto_is_not_gpt_oss(self):
        self.assertEqual(blm.norm_family('GPTo'), 'GPTo')


class ListNormalizerTest(unittest.TestCase):
    def test_train_data_skips_bench_aliases(self):
        row = _norm({
            'model': 'Qwen2.5-7B',
            'start_point': 'instruct',
            'train_data': ['gsm-8k', 'MATH-500'],
            'eval_ood': ['gsm-8k', 'AIME-2025', 'MMLU Pro', 'Olympiad Bench'],
        })
        self.assertEqual(row['train_data'], ['gsm-8k', 'MATH-500'])
        self.assertEqual(row['eval_ood'], [
            'GSM8K', 'AIME 2025', 'MMLU-Pro', 'OlympiadBench',
        ])

    def test_empty_ood_clears_basis(self):
        row = _norm({
            'model': 'GPT-5',
            'start_point': 'api',
            'eval_ood': [],
            'ood_basis': 'inferred',
        })
        self.assertEqual(row['ood_basis'], '')


class ExtractKeyTest(unittest.TestCase):
    def test_doi_stem_maps_via_safe_key(self):
        key = 'doi:10.1038/s41586-023-06924-6'
        papers = [_paper(key=key)]
        path = Path(blm.safe_key(key) + '.json')
        resolved = blm.resolve_extract_key(path, [{}], blm.papers_safe_map(papers), {
            key: papers[0],
        })
        self.assertEqual(resolved, key)
        self.assertNotIn(':', path.stem)

    def test_stem_replace_would_break_doi(self):
        stem = 'doi_10.1038_s41586-023-06924-6'
        self.assertEqual(stem.replace('_', ':', 1), 'doi:10.1038_s41586-023-06924-6')


class RenderTest(unittest.TestCase):
    def test_notes_and_empty_url(self):
        papers = [_paper()]
        rows = [_norm({
            'model': 'Qwen3-8B',
            'start_point': 'instruct',
            'role': 'trained',
            'eval_id': ['MATH-500'],
            'eval_ood': ['MATH-500', 'AIME 2024'],
            'notes': 'uses MATH-500 as ID',
        })]
        markdown = blm.render_md(rows, papers, [], [
            {'title': 'Verbalizable Representations', 'section': 'Alignment', 'urls': []},
        ])
        self.assertIn('uses MATH-500 as ID', markdown)
        paper_row = next(
            line for line in markdown.splitlines()
            if line.startswith('| [Demo]')
        )
        self.assertIn('| AIME 2024 |', paper_row)
        self.assertNotIn('MATH-500, AIME', paper_row)
        self.assertIn('- Verbalizable Representations — Alignment', markdown)
        self.assertNotIn('[]()', markdown)

    def test_md_link_truncates_before_escape(self):
        text = blm.md_link('A|B' * 20, 'https://example.com', limit=3)
        self.assertEqual(text, '[A\\|B](https://example.com)')


class WriteGuardTest(unittest.TestCase):
    def test_refuse_shrink(self):
        self.assertTrue(blm.refuse_shrink(10, 3, force=False))
        self.assertFalse(blm.refuse_shrink(10, 3, force=True))
        self.assertFalse(blm.refuse_shrink(10, 10, force=False))

    def test_missing_extract_does_not_wipe(self):
        with tempfile.TemporaryDirectory() as tmp:
            tmp_path = Path(tmp)
            jsonl = tmp_path / 'llm_models.jsonl'
            jsonl.write_text('{"key": "keep"}\n', encoding='utf-8')
            md_path = tmp_path / 'llm_models.md'
            md_path.write_text('keep\n', encoding='utf-8')
            meta = tmp_path / 'meta.json'
            meta.write_text('{}\n', encoding='utf-8')
            old = blm.JSONL_PATH, blm.MD_PATH, blm.META_PATH
            blm.JSONL_PATH, blm.MD_PATH, blm.META_PATH = jsonl, md_path, meta
            try:
                code = blm.main(['--extract-dir', str(tmp_path / 'missing')])
            finally:
                blm.JSONL_PATH, blm.MD_PATH, blm.META_PATH = old
            self.assertEqual(code, 1)
            self.assertEqual(jsonl.read_text(encoding='utf-8'), '{"key": "keep"}\n')
            self.assertEqual(md_path.read_text(encoding='utf-8'), 'keep\n')

    def test_empty_extract_does_not_wipe(self):
        with tempfile.TemporaryDirectory() as tmp:
            tmp_path = Path(tmp)
            extract = tmp_path / 'extracts'
            extract.mkdir()
            jsonl = tmp_path / 'llm_models.jsonl'
            jsonl.write_text('{"key": "keep"}\n', encoding='utf-8')
            old = blm.JSONL_PATH, blm.MD_PATH, blm.META_PATH
            blm.JSONL_PATH = jsonl
            blm.MD_PATH = tmp_path / 'llm_models.md'
            blm.META_PATH = tmp_path / 'meta.json'
            try:
                code = blm.main(['--extract-dir', str(extract)])
            finally:
                blm.JSONL_PATH, blm.MD_PATH, blm.META_PATH = old
            self.assertEqual(code, 1)
            self.assertEqual(jsonl.read_text(encoding='utf-8'), '{"key": "keep"}\n')

    def test_missing_keys_do_not_write(self):
        with tempfile.TemporaryDirectory() as tmp:
            tmp_path = Path(tmp)
            extract = tmp_path / 'extracts'
            extract.mkdir()
            (extract / 'candidates.json').write_text(
                json.dumps([{'key': 'arxiv:9999.99999'}]),
                encoding='utf-8',
            )
            (extract / 'arxiv_1111.11111.json').write_text(
                json.dumps([{
                    'key': 'arxiv:1111.11111',
                    'model': 'Qwen3-4B',
                    'start_point': 'base',
                }]),
                encoding='utf-8',
            )
            jsonl = tmp_path / 'llm_models.jsonl'
            jsonl.write_text('{"key": "keep"}\n', encoding='utf-8')
            old = blm.JSONL_PATH, blm.MD_PATH, blm.META_PATH
            blm.JSONL_PATH = jsonl
            blm.MD_PATH = tmp_path / 'out.md'
            blm.META_PATH = tmp_path / 'meta.json'
            try:
                code = blm.main(['--extract-dir', str(extract)])
            finally:
                blm.JSONL_PATH, blm.MD_PATH, blm.META_PATH = old
            self.assertEqual(code, 1)
            self.assertEqual(jsonl.read_text(encoding='utf-8'), '{"key": "keep"}\n')
            self.assertFalse((tmp_path / 'out.md').exists())


class MetaSlimTest(unittest.TestCase):
    def test_drops_absolute_path(self):
        rec = blm.slim_meta_record({
            'key': 'arxiv:2501.00001',
            'title': 'Demo',
            'section': 'RL',
            'path': r'd:\Projects\key-papers\filter\fulltext\arxiv_2501.00001.md',
            'rel_path': 'filter/fulltext/arxiv_2501.00001.md',
            'n_tokens': 12,
        })
        self.assertNotIn('path', rec)
        self.assertEqual(rec['rel_path'], 'filter/fulltext/arxiv_2501.00001.md')


if __name__ == '__main__':
    unittest.main()
