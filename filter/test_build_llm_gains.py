'''Anti-regression tests for the OOD gain tables.'''

from __future__ import annotations

import json
import sys
import tempfile
import unittest
from datetime import date
from pathlib import Path
from unittest.mock import patch

FILTER_DIR = Path(__file__).resolve().parent
sys.path.insert(0, str(FILTER_DIR))

import build_llm_gains as blg
import build_llm_models as blm
import llm_gains_ood as ood
from llm_reliability import SHAO_MATH500_GT_PP, SHAO_MATH500_RANDOM_PP
from paths import (
    PAPERS_JSONL,
    SCOREABLE_KINDS,
    append_jsonl,
    papers_in_readme_order,
    read_jsonl,
    readme_paper_keys,
    write_jsonl,
)


def _paper(key='arxiv:2501.00001', title='Demo', section='Post-training'):
    return {'key': key, 'line_title': title, 'section': section, 'title': title}


def _gain(**kwargs):
    raw = {
        'key': 'arxiv:2501.00001',
        'code': 'SC-GRPO',
        'method': 'SC-GRPO',
        'model': 'Qwen2.5-Math-7B',
        'bench': 'AIME 2024',
        'metric': 'avg@8',
        'base': 10.0,
        'ref': 20.0,
        'ref_method': 'GRPO',
        'score': 25.0,
        'source': 'Table 1',
        'ood': True,
    }
    raw.update(kwargs)
    return blg.normalize_gain_row(raw)


class DeltaTest(unittest.TestCase):
    def test_format_delta_and_blank(self):
        self.assertEqual(blg.format_delta(70.8, 49.4), f'+{SHAO_MATH500_RANDOM_PP}')
        self.assertEqual(blg.format_delta(78.5, 49.4), f'+{SHAO_MATH500_GT_PP}')
        self.assertEqual(blg.format_delta(48.2, 49.4), '-1.2')
        self.assertEqual(blg.format_delta(None, 49.4), '')
        self.assertEqual(blg.format_delta(70.8, None), '')

    def test_gain_field_when_score_missing(self):
        row = _gain(score=None, base=None, gain=21.4)
        self.assertEqual(blg.format_gain_cell(blg.delta_over_base(row)), '+21.4')

    def test_keeps_sub_percent_aime_scores(self):
        row = _gain(base=0.41, ref=None, score=0.83)
        self.assertAlmostEqual(row['base'], 0.41)
        self.assertAlmostEqual(row['score'], 0.83)
        self.assertEqual(blg.format_delta(row['score'], row['base']), '+0.4')

    def test_mixed_scale_paper_scales_fraction_row(self):
        rows = blg.coerce_pp_rows([
            _gain(base=0.41, ref=None, score=0.83, bench='AIME 2024'),
            _gain(base=49.4, ref=None, score=70.8, bench='MATH-500'),
        ])
        aime = next(row for row in rows if row['bench'] == 'AIME 2024')
        math = next(row for row in rows if row['bench'] == 'MATH-500')
        self.assertAlmostEqual(aime['base'], 41.0)
        self.assertAlmostEqual(aime['score'], 83.0)
        self.assertAlmostEqual(math['base'], 49.4)

    def test_unit_scale_paper_times_100(self):
        rows = blg.rescale_unit_papers([
            _gain(base=0.3, ref=0.2, score=0.6, bench='AIME 2024'),
            _gain(base=0.2, ref=0.15, score=0.5, bench='MATH-500'),
        ])
        self.assertAlmostEqual(rows[0]['base'], 30.0)
        self.assertAlmostEqual(rows[0]['score'], 60.0)
        self.assertAlmostEqual(rows[1]['ref'], 15.0)

    def test_explicit_pp_does_not_scale(self):
        rows = blg.coerce_pp_rows([
            _gain(
                key='arxiv:2509.03646',
                model='Llama-3.1-8B-Instruct',
                bench='AIME 2025',
                code='HICRA',
                method='HICRA',
                base=0.6,
                ref=0.5,
                score=0.8,
                unit='pp',
            ),
        ])
        self.assertAlmostEqual(rows[0]['base'], 0.6)
        self.assertAlmostEqual(rows[0]['score'], 0.8)
        self.assertEqual(blg.format_delta(0.5, 0.6), '-0.1')
        self.assertEqual(blg.format_delta(0.8, 0.6), '+0.2')
        self.assertEqual(blg.format_delta(0.8, 0.5), '+0.3')

    def test_dft_pp_stays_sub_percent(self):
        rows = blg.coerce_pp_rows([
            _gain(
                key='arxiv:2508.05629',
                model='Llama-3.2-3B',
                bench='AIME 2024',
                base=0.41,
                score=0.83,
                unit='pp',
            ),
        ])
        self.assertAlmostEqual(rows[0]['base'], 0.41)
        self.assertAlmostEqual(rows[0]['score'], 0.83)

    def test_unscale_already_multiplied_hicra(self):
        row = _gain(
            key='arxiv:2509.03646',
            model='Llama-3.1-8B-Instruct',
            bench='AIME 2025',
            code='HICRA',
            method='HICRA',
            base=60.0,
            ref=50.0,
            score=80.0,
            unit='pp',
        )
        out = ood.apply_gain_overrides([row])
        hit = next(item for item in out if item['code'] == 'HICRA')
        self.assertAlmostEqual(hit['base'], 0.6)
        self.assertAlmostEqual(hit['ref'], 0.5)
        self.assertAlmostEqual(hit['score'], 0.8)

    def test_renormalize_twice_leaves_hicra(self):
        raw = {
            'key': 'arxiv:2509.03646',
            'code': 'HICRA',
            'method': 'HICRA',
            'model': 'Llama-3.1-8B-Instruct',
            'bench': 'AIME 2025',
            'metric': 'avg@32',
            'base': 60.0,
            'ref': 50.0,
            'score': 80.0,
            'unit': 'pp',
        }
        once = blg.renormalize_rows([raw], [])
        twice = blg.renormalize_rows(once, [])
        first = next(row for row in once if row['code'] == 'HICRA')
        second = next(row for row in twice if row['code'] == 'HICRA')
        self.assertAlmostEqual(first['base'], 0.6)
        self.assertAlmostEqual(first['ref'], 0.5)
        self.assertAlmostEqual(first['score'], 0.8)
        self.assertAlmostEqual(second['base'], first['base'])
        self.assertAlmostEqual(second['ref'], first['ref'])
        self.assertAlmostEqual(second['score'], first['score'])

    def test_qwen_hicra_aime25_stays_thirteen(self):
        row = _gain(
            key='arxiv:2509.03646',
            model='Qwen2.5-7B-Base',
            bench='AIME 2025',
            code='HICRA',
            method='HICRA',
            base=1.7,
            ref=11.4,
            score=14.8,
            unit='pp',
        )
        out = ood.apply_gain_overrides(blg.coerce_pp_rows([row]))
        hit = next(
            item for item in out
            if item['code'] == 'HICRA' and item['model'] == 'Qwen2.5-7B-Base'
        )
        self.assertAlmostEqual(blg.delta_over_base(hit), 13.1)
        self.assertAlmostEqual(blg.delta_over_ref(hit), 3.4)
        classified = blg.attach_ood([hit], [])
        self.assertEqual(classified[0]['ood_basis'], 'unverified')
        markdown = blg.render_md(classified, [_paper(key='arxiv:2509.03646')], [])
        self.assertNotIn('+13.1', markdown)

    def test_pp_mixed_scale_warns(self):
        row = _gain(
            key='arxiv:2509.03646',
            model='Llama-3.1-8B-Instruct',
            bench='AIME 2025',
            base=60.0,
            ref=0.5,
            score=0.8,
            unit='pp',
        )
        with patch('builtins.print') as printed:
            out = blg.coerce_pp_rows([row])
        self.assertAlmostEqual(out[0]['base'], 60.0)
        self.assertAlmostEqual(out[0]['score'], 0.8)
        self.assertTrue(any(
            'mixed-scale' in ' '.join(str(arg) for arg in call.args)
            for call in printed.call_args_list
        ))

    def test_zero_base_is_not_mixed_scale(self):
        row = _gain(base=0.0, ref=None, score=16.7, unit='pp')
        with patch('builtins.print') as printed:
            out = blg.coerce_pp_rows([row])
        self.assertAlmostEqual(out[0]['score'], 16.7)
        self.assertFalse(any(
            'mixed-scale' in ' '.join(str(arg) for arg in call.args)
            for call in printed.call_args_list
        ))

    def test_unscale_skips_lone_gain(self):
        row = {
            'key': 'arxiv:2509.03646',
            'model': 'Llama-3.1-8B-Instruct',
            'bench': 'AIME 2025',
            'base': 0.6,
            'ref': 0.5,
            'score': 0.8,
            'gain': 20.0,
        }
        out = ood.unscale_row(row)
        self.assertAlmostEqual(out['base'], 0.6)
        self.assertAlmostEqual(out['gain'], 20.0)

    def test_unscale_leaves_small_gain(self):
        row = {
            'key': 'arxiv:2509.03646',
            'model': 'Llama-3.1-8B-Instruct',
            'bench': 'AIME 2025',
            'base': 60.0,
            'ref': 50.0,
            'score': 80.0,
            'gain': 0.2,
        }
        out = ood.unscale_row(row)
        self.assertAlmostEqual(out['base'], 0.6)
        self.assertAlmostEqual(out['gain'], 0.2)


class RefMarkerTest(unittest.TestCase):
    def test_vanilla_grpo_has_no_star(self):
        row = _gain(ref_method='GRPO', score=25, ref=20)
        self.assertEqual(blg.grpo_cell(row), '+5.0')
        self.assertFalse(blg.starred_ref(row))

    def test_dapo_star_and_vs_column(self):
        row = _gain(ref_method='DAPO', score=25, ref=20)
        self.assertEqual(blg.grpo_cell(row), '+5.0*')
        self.assertTrue(blg.starred_ref(row))
        paper = _paper()
        markdown = blg.render_md([row], [paper], [])
        self.assertIn('| vs |', markdown)
        self.assertIn('| metric |', markdown)
        self.assertIn('| DAPO |', markdown)
        self.assertIn('+5.0*', markdown)
        self.assertIn('## Gain over the starting checkpoint', markdown)

    def test_skips_self_ref_grpo_row(self):
        grpo = _gain(code='GRPO', method='GRPO', score=20, ref=20, ref_method='GRPO')
        method = _gain(code='SC-GRPO', score=25, ref=20, ref_method='GRPO')
        markdown = blg.render_md([grpo, method], [_paper()], [])
        grpo_section = markdown.split('## Gain over GRPO', 1)[1]
        self.assertNotIn('[GRPO](', grpo_section)
        self.assertIn('[SC-GRPO](', grpo_section)
        self.assertIn('+5.0', grpo_section)
        base_section = markdown.split('## Gain over the starting checkpoint', 1)[1]
        self.assertIn('[GRPO](', base_section.split('## Gain over GRPO', 1)[0])

    def test_drgrpo_matches_dotted_name(self):
        row = _gain(
            code='DrGRPO',
            method='DrGRPO',
            ref_method='Dr. GRPO',
            score=25,
            ref=20,
        )
        self.assertTrue(blg.is_self_ref(row))

    def test_equal_ref_and_score_shows_zero(self):
        row = _gain(
            code='LOPD',
            method='LOPD',
            ref_method='GRPO',
            score=45.8,
            ref=45.8,
        )
        self.assertFalse(blg.is_self_ref(row))
        self.assertEqual(blg.grpo_cell(row), '+0.0')

    def test_r1_grpo_is_not_vanilla_code(self):
        row = _gain(code='GRPO', method='R1-GRPO', score=20, ref=None, ref_method='')
        self.assertEqual(row['code'], 'R1-GRPO')
        self.assertIsNone(blg.ref_rank(row['code'], row['method']))


class GrpoOnlyTableTest(unittest.TestCase):
    def test_ablation_predicate(self):
        self.assertTrue(blg.is_grpo_ablation('GRPO', 'GRPO'))
        self.assertTrue(blg.is_grpo_ablation('GRPO-format', 'GRPO (format reward)'))
        self.assertTrue(blg.is_grpo_ablation('GRPO-random', ''))
        self.assertFalse(blg.is_grpo_ablation('2-GRPO', '2-GRPO'))
        self.assertFalse(blg.is_grpo_ablation('Dr.GRPO', 'Dr.GRPO'))
        self.assertFalse(blg.is_grpo_ablation('1-shot RLVR', '1-shot RLVR'))

    def test_omits_listed_method_codes(self):
        self.assertTrue(blg.is_omitted_method('GRPO-format', ''))
        self.assertTrue(blg.is_omitted_method('GRPO-incorrect', ''))
        self.assertTrue(blg.is_omitted_method('GRPO-majority', ''))
        self.assertTrue(blg.is_omitted_method('GRPO-random', ''))
        self.assertTrue(blg.is_omitted_method('2-GRPO+RS', '2-GRPO+RS'))
        self.assertTrue(blg.is_omitted_method('R1-GRPO', 'R1-GRPO'))
        self.assertFalse(blg.is_omitted_method('GRPO', 'GRPO'))
        self.assertFalse(blg.is_omitted_method('2-GRPO', '2-GRPO'))
        rows = blg.attach_ood([
            _gain(
                key=ood.TWO_GRPO,
                code='2-GRPO+RS',
                method='2-GRPO+RS',
                model='Qwen2.5-Math-7B',
                bench='AIME 2025',
                train_data='MATH',
                base=5.0,
                score=11.67,
            ),
            _gain(
                key=ood.TWO_GRPO,
                code='2-GRPO',
                method='2-GRPO',
                model='Qwen2.5-Math-7B',
                bench='AIME 2025',
                train_data='MATH',
                base=5.0,
                score=12.8,
            ),
            _gain(
                key=ood.SHAO,
                code='GRPO-format',
                method='GRPO (format reward)',
                model='Qwen2.5-Math-7B',
                bench='AIME 2025',
                train_data='DeepScaleR',
                base=6.3,
                score=5.9,
            ),
        ], [])
        markdown = blg.render_md(
            rows,
            [_paper(key=ood.TWO_GRPO), _paper(key=ood.SHAO)],
            [],
        )
        self.assertNotIn('[GRPO-format]', markdown)
        self.assertNotIn('[2-GRPO+RS]', markdown)
        self.assertIn('[2-GRPO](', markdown)

    def test_omits_grpo_reward_ablation_table(self):
        rows = blg.attach_ood([
            _gain(
                key=ood.SHAO,
                code=code,
                method=method,
                model='OLMo-2-1124-7B',
                bench='AIME 2025',
                train_data='DeepScaleR',
                base=0.4,
                score=score,
            )
            for code, method, score in (
                ('GRPO', 'GRPO (ground-truth reward)', 0.4),
                ('GRPO-format', 'GRPO (format reward)', 0.4),
                ('GRPO-random', 'GRPO (random reward)', 0.4),
            )
        ], [])
        markdown = blg.render_md(rows, [_paper(key=ood.SHAO)], [])
        self.assertNotIn('### OLMo-2-1124-7B', markdown)

    def test_keeps_mixed_grpo_and_other_method(self):
        rows = blg.attach_ood([
            _gain(
                key=ood.SHAO,
                code='GRPO',
                method='GRPO (ground-truth reward)',
                model='Qwen2.5-Math-7B',
                bench='AIME 2025',
                train_data='DeepScaleR',
                base=6.3,
                score=13.7,
            ),
            _gain(
                key=ood.ONESHOT,
                code='1-shot RLVR',
                method='1-shot RLVR',
                model='Qwen2.5-Math-7B',
                bench='AIME 2025',
                train_data='DeepScaleR subset',
                base=6.7,
                score=10.8,
            ),
            _gain(
                key=ood.SHAO,
                code='GRPO-format',
                method='GRPO (format reward)',
                model='Qwen2.5-Math-7B',
                bench='AIME 2025',
                train_data='DeepScaleR',
                base=6.3,
                score=5.9,
            ),
        ], [])
        markdown = blg.render_md(
            rows,
            [_paper(key=ood.SHAO), _paper(key=ood.ONESHOT)],
            [],
        )
        self.assertIn('### Other checkpoints', markdown)
        self.assertIn('1-shot RLVR', markdown)
        self.assertIn('Qwen2.5-Math-7B', markdown)


class OodFilterTest(unittest.TestCase):
    def test_math500_id_is_dropped(self):
        models = [
            blm.normalize_row({
                'model': 'Qwen2.5-Math-7B',
                'start_point': 'base',
                'role': 'trained',
                'method': 'SC-GRPO',
                'eval_id': ['MATH-500'],
                'eval_ood': ['AIME 2024'],
            }, _paper()),
        ]
        rows = blg.attach_ood([
            _gain(bench='MATH-500', score=70.8, base=49.4),
            _gain(bench='AIME 2024', score=20, base=10),
        ], models)
        by_bench = {row['bench']: row for row in rows}
        self.assertEqual(by_bench['MATH-500']['ood_basis'], 'id')
        self.assertFalse(by_bench['MATH-500']['ood'])
        self.assertEqual(by_bench['AIME 2024']['ood_basis'], 'rl_stage')
        self.assertFalse(by_bench['AIME 2024']['ood'])
        markdown = blg.render_md(rows, [_paper()], [])
        self.assertNotIn('MATH500', markdown)
        self.assertNotIn('AIME24', markdown.split('## Not applicable', 1)[0])

    def test_math500_ood_when_trained_on_deepscaler(self):
        models = [
            blm.normalize_row({
                'model': 'Qwen2.5-Math-7B',
                'start_point': 'base',
                'role': 'trained',
                'method': 'GRPO',
                'train_data': ['DeepScaleR'],
                'eval_id': ['MATH-500'],
                'eval_ood': ['AMC', 'AIME 2024'],
            }, _paper(key='arxiv:2506.10947')),
        ]
        rows = blg.attach_ood([
            _gain(key='arxiv:2506.10947', bench='MATH-500', score=70.8, base=49.4),
        ], models)
        self.assertFalse(rows[0]['ood'])
        self.assertEqual(rows[0]['ood_basis'], 'id')
        markdown = blg.render_md(rows, [_paper(key='arxiv:2506.10947')], [])
        self.assertNotIn('+21.4', markdown)
        self.assertNotIn('MATH500', markdown)

    def test_math500_intersection_is_id_when_trained_on_math(self):
        models = [
            blm.normalize_row({
                'model': 'Qwen2.5-Math-7B',
                'start_point': 'base',
                'role': 'trained',
                'method': '2-GRPO',
                'train_data': ['MATH'],
                'eval_id': ['MATH-500'],
                'eval_ood': ['MATH-500', 'AIME 2024'],
            }, _paper()),
        ]
        rows = blg.attach_ood([
            _gain(bench='MATH-500', score=70.8, base=49.4),
            _gain(bench='AIME 2024', score=20, base=10),
        ], models)
        by_bench = {row['bench']: row for row in rows}
        self.assertEqual(by_bench['MATH-500']['ood_basis'], 'id')
        self.assertEqual(by_bench['AIME 2024']['ood_basis'], 'rl_stage')
        self.assertFalse(by_bench['MATH-500']['ood'])
        self.assertFalse(by_bench['AIME 2024']['ood'])

    def test_openr1_does_not_force_math500_ood(self):
        models = [
            blm.normalize_row({
                'model': 'Qwen2.5-Math-7B',
                'start_point': 'base',
                'role': 'trained',
                'method': 'GRPO',
                'train_data': ['OpenR1-Math'],
                'eval_id': ['MATH-500'],
                'eval_ood': ['AIME 2024'],
            }, _paper()),
        ]
        rows = blg.attach_ood([
            _gain(bench='MATH-500', score=70.8, base=49.4),
        ], models)
        self.assertFalse(rows[0]['ood'])

    def test_unmatched_model_fails_closed(self):
        models = [
            blm.normalize_row({
                'model': 'Qwen2.5-Math-7B',
                'start_point': 'base',
                'role': 'trained',
                'method': 'GRPO',
                'eval_id': ['MATH-500'],
                'eval_ood': ['AIME 2024'],
            }, _paper()),
        ]
        rows = blg.attach_ood([
            _gain(model='Unknown-9B', bench='MATH-500', score=70, base=40),
            _gain(model='Unknown-9B', bench='AIME 2024', score=20, base=10),
        ], models)
        self.assertFalse(rows[0]['ood'])
        self.assertFalse(rows[1]['ood'])
        self.assertEqual(rows[0]['ood_basis'], 'rl_stage')
        self.assertEqual(rows[1]['ood_basis'], 'rl_stage')

    def test_fuzzy_model_alias_matches(self):
        models = [
            blm.normalize_row({
                'model': 'Qwen2.5-Instruct',
                'start_point': 'instruct',
                'role': 'trained',
                'method': 'GRPO',
                'eval_ood': ['AIME 2025'],
            }, _paper()),
        ]
        rows = blg.attach_ood([
            _gain(
                model='Qwen2.5-7B-Instruct',
                bench='AIME 2025',
                score=20,
                base=10,
                train_data='DeepScaleR',
            ),
        ], models)
        self.assertTrue(rows[0]['ood'])
        self.assertEqual(rows[0]['ood_basis'], 'temporal')

    def test_aime24_never_auto_temporal(self):
        models = [
            blm.normalize_row({
                'model': 'Qwen2.5-Math-7B',
                'start_point': 'base',
                'role': 'trained',
                'method': 'GRPO',
                'eval_ood': ['AIME 2024'],
            }, _paper()),
        ]
        rows = blg.attach_ood([
            _gain(bench='AIME 2024', score=20, base=10),
        ], models)
        self.assertEqual(rows[0]['ood_basis'], 'rl_stage')

    def test_qwen3_aime25_not_temporal(self):
        models = [
            blm.normalize_row({
                'model': 'Qwen3-8B',
                'start_point': 'base',
                'role': 'trained',
                'method': 'GRPO',
                'eval_ood': ['AIME 2025'],
            }, _paper()),
        ]
        rows = blg.attach_ood([
            _gain(model='Qwen3-8B', bench='AIME 2025', score=20, base=10),
        ], models)
        self.assertEqual(rows[0]['ood_basis'], 'unverified')
        self.assertFalse(rows[0]['ood'])

    def test_lcb_version_only_not_temporal(self):
        models = [
            blm.normalize_row({
                'model': 'Qwen2.5-1.5B',
                'start_point': 'base',
                'role': 'trained',
                'method': 'Intuitor',
                'eval_ood': ['LiveCodeBench v6'],
            }, _paper()),
        ]
        rows = blg.attach_ood([
            _gain(
                model='Qwen2.5-1.5B',
                bench='LiveCodeBench v6',
                score=9.9,
                base=0.0,
            ),
        ], models)
        self.assertEqual(rows[0]['ood_basis'], 'unverified')

    def test_amc_unifies_to_2023(self):
        self.assertEqual(_gain(bench='AMC')['bench'], 'AMC 2023')


class RowCapTest(unittest.TestCase):
    def test_splits_over_45_rows(self):
        rows = []
        papers = []
        for i in range(50):
            key = f'arxiv:2501.{i:05d}'
            papers.append(_paper(key=key, title=f'P{i}'))
            rows.append(_gain(
                key=key,
                code=f'M{i:02d}',
                model='Qwen2.5-Math-7B',
                bench='AIME 2024',
                base=10,
                score=20,
            ))
        parts = blg.split_row_groups(blg.order_groups(blg.pivot_groups(rows), papers))
        self.assertGreaterEqual(len(parts), 2)
        self.assertTrue(all(len(chunk) <= 45 for _, chunk in parts))
        markdown = blg.render_md(rows, papers, [])
        self.assertIn('Qwen2.5-Math-7B (a)', markdown)
        self.assertIn('Qwen2.5-Math-7B (b)', markdown)
        self.assertNotIn('Qwen2.5-Math-7B (c)', markdown)

    def test_core_benches_only(self):
        rows = [
            _gain(bench='AIME 2024', score=20, base=10),
            _gain(bench='HumanEval', score=40, base=10, code='SC-GRPO'),
        ]
        markdown = blg.render_md(rows, [_paper()], [])
        self.assertIn('AIME24', markdown)
        self.assertNotIn('HumanEval', markdown)


class CandidateTest(unittest.TestCase):
    def test_drops_from_scratch_only(self):
        paper = _paper(key='arxiv:2407.20311')
        models = [
            blm.normalize_row({
                'model': 'Llama-3.2-3B',
                'start_point': 'base',
                'role': 'trained',
                'method': 'autoregressive pretrain from scratch',
                'eval_ood': ['HellaSwag'],
            }, paper),
        ]
        cands, skipped = blg.iter_candidates(models, {})
        self.assertEqual(cands, [])
        self.assertEqual(skipped[0]['key'], paper['key'])

    def test_keeps_mixed_pretrain_and_rl(self):
        paper = _paper(key='arxiv:2601.21343')
        models = [
            blm.normalize_row({
                'model': 'Qwen3-8B',
                'start_point': 'base',
                'role': 'trained',
                'method': 'DrGRPO (RL mid-training)',
                'eval_ood': ['AIME 2024'],
            }, paper),
            blm.normalize_row({
                'model': 'Qwen3-8B',
                'start_point': 'base',
                'role': 'trained',
                'method': 'continual pre-training (CMS)',
                'eval_ood': ['AIME 2024'],
            }, paper),
        ]
        cands, skipped = blg.iter_candidates(models, {})
        self.assertEqual([item['key'] for item in cands], [paper['key']])
        self.assertEqual(skipped, [])

    def test_continued_pretrain_is_not_from_scratch(self):
        self.assertFalse(blg.is_from_scratch_method('math continued pretrain'))
        self.assertFalse(blg.is_from_scratch_method('continual pre-training (CMS)'))
        self.assertTrue(blg.is_from_scratch_method('autoregressive pretrain from scratch'))
        paper = _paper(key='arxiv:2402.03300')
        models = [
            blm.normalize_row({
                'model': 'DeepSeekMath-7B',
                'start_point': 'base',
                'role': 'trained',
                'method': 'math continued pretrain',
                'eval_ood': ['MATH-500'],
            }, paper),
        ]
        cands, skipped = blg.iter_candidates(models, {})
        self.assertEqual([item['key'] for item in cands], [paper['key']])
        self.assertEqual(skipped, [])


class FillRefTest(unittest.TestCase):
    def test_fills_grpo_from_sibling(self):
        rows = blg.fill_baselines([
            _gain(code='GRPO', method='GRPO', score=20, base=10, ref=None, ref_method=''),
            _gain(code='SC-GRPO', method='SC-GRPO', score=25, base=None, ref=None, ref_method=''),
        ])
        sc = next(row for row in rows if row['code'] == 'SC-GRPO')
        self.assertEqual(sc['base'], 10.0)
        self.assertEqual(sc['ref'], 20.0)
        self.assertEqual(sc['ref_method'], 'GRPO')

    def test_does_not_share_base_across_metrics(self):
        rows = blg.fill_baselines([
            _gain(code='GRPO', method='GRPO', metric='pass@1', score=20, base=10, ref=None, ref_method=''),
            _gain(code='SC-GRPO', method='SC-GRPO', metric='avg@8', score=25, base=None, ref=None, ref_method=''),
        ])
        sc = next(row for row in rows if row['code'] == 'SC-GRPO')
        self.assertIsNone(sc['base'])
        self.assertIsNone(sc['ref'])

    def test_skips_conflicting_bases(self):
        rows = blg.fill_baselines([
            _gain(code='SC-GRPO', method='SC-GRPO', score=25, base=10, ref=None, ref_method=''),
            _gain(code='RIFT', method='RIFT', score=22, base=12, ref=None, ref_method=''),
            _gain(code='SFT', method='SFT', score=18, base=None, ref=None, ref_method=''),
        ])
        sft = next(row for row in rows if row['code'] == 'SFT')
        self.assertIsNone(sft['base'])

    def test_r1_grpo_is_not_shared_ref(self):
        rows = blg.fill_baselines([
            _gain(code='GRPO', method='R1-GRPO', score=20, base=10, ref=None, ref_method=''),
            _gain(code='SC-GRPO', method='SC-GRPO', score=25, base=10, ref=None, ref_method=''),
        ])
        sc = next(row for row in rows if row['code'] == 'SC-GRPO')
        self.assertIsNone(sc['ref'])

    def test_does_not_share_base_across_train_data(self):
        rows = blg.fill_baselines([
            _gain(
                key='arxiv:2605.12969',
                code='GRPO',
                method='GRPO',
                model='DeepSeek-R1-Distill-Qwen-1.5B',
                bench='AIME 2025',
                metric='avg@32',
                source='Table 4 / §5.2',
                train_data='DAPO-Math-17k',
                score=22.7,
                base=20.7,
                ref=None,
                ref_method='',
            ),
            _gain(
                key='arxiv:2605.12969',
                code='ConSPO',
                method='ConSPO',
                model='DeepSeek-R1-Distill-Qwen-1.5B',
                bench='AIME 2025',
                metric='avg@32',
                source='Table 1 / §5.2',
                train_data='DeepScaleR-Preview-Dataset',
                score=26.7,
                base=None,
                ref=None,
                ref_method='',
            ),
        ])
        conspo = next(row for row in rows if row['code'] == 'ConSPO')
        self.assertIsNone(conspo['base'])
        self.assertIsNone(conspo['ref'])


class AliasTest(unittest.TestCase):
    def test_espo_qwen3_is_14b_base(self):
        row = _gain(key='arxiv:2512.00499', model='Qwen3', bench='AIME 2025')
        self.assertEqual(row['model'], 'Qwen3-14B-Base')

    def test_dft_math_is_7b(self):
        row = _gain(key='arxiv:2508.05629', model='Qwen2.5-Math', bench='AIME 2024')
        self.assertEqual(row['model'], 'Qwen2.5-Math-7B')

    def test_midtrain_method_keeps_stages(self):
        row = _gain(
            key='arxiv:2601.21343',
            code='SFT+DrGRPO',
            method='SFT+DrGRPO',
            bench='GSM8K',
        )
        self.assertEqual(row['code'], 'SFT(think) 10k + RLMT 5k + RLPT')

    def test_hicra_llama_is_8b_instruct(self):
        row = _gain(
            key='arxiv:2509.03646',
            model='Llama-3.1-Instruct',
            bench='AIME 2025',
        )
        self.assertEqual(row['model'], 'Llama-3.1-8B-Instruct')


class TeacherChainTest(unittest.TestCase):
    def test_opd_teacher_makes_aime25_unverified(self):
        row = _gain(
            key='arxiv:2606.06021',
            code='OPD-top1',
            method='OPD-top1',
            model='DeepSeek-R1-Distill-Qwen-1.5B',
            bench='AIME 2025',
            score=33.5,
            base=21.9,
            ood=False,
        )
        rows = blg.attach_teacher([row], [])
        self.assertEqual(rows[0]['teacher'], 'JustRL-Deepseek-1.5B')
        rows = blg.attach_ood(rows, [])
        self.assertEqual(rows[0]['ood_basis'], 'unverified')
        self.assertFalse(rows[0]['ood'])

    def test_revisit_opd_teacher_unverified(self):
        row = _gain(
            key='arxiv:2603.25562',
            code='OPD',
            method='sampled-token OPD',
            model='Qwen2.5-7B-Instruct',
            bench='AIME 2025',
            score=16.7,
            base=0.0,
            ood=False,
        )
        rows = blg.attach_ood(blg.attach_teacher([row], []), [])
        self.assertEqual(rows[0]['teacher'], 'OpenThinker3-7B')
        self.assertEqual(rows[0]['ood_basis'], 'unverified')

    def test_chain_cutoff_uses_unknown_teacher(self):
        self.assertIsNone(ood.chain_cutoff(
            'DeepSeek-R1-Distill-Qwen-1.5B',
            'JustRL-Deepseek-1.5B',
            'DAPO-Math-17K',
            'arxiv:2606.06021',
            'OPD-top1',
            'OPD-top1',
        ))
        self.assertIsNone(ood.chain_cutoff(
            'Qwen2.5-Math-7B',
            '',
            '',
            'arxiv:2501.00001',
            'GRPO',
            'GRPO',
        ))
        self.assertIsNotNone(ood.chain_cutoff(
            'Qwen2.5-Math-7B',
            '',
            'DeepScaleR',
            'arxiv:2501.00001',
            'GRPO',
            'GRPO',
        ))


class ConspoDisplayTest(unittest.TestCase):
    def test_aliases_merge_and_label_train_data(self):
        shared = dict(
            key='arxiv:2605.12969',
            model='DeepSeek-R1-Distill-Qwen-1.5B',
            bench='AIME 2025',
            metric='avg@32',
            ckpt_select='best-every-100',
        )
        rows = ood.apply_gain_overrides([
            _gain(
                **shared,
                code='ConSPO',
                method='ConSPO',
                source='Table 1 / §5.2',
                train_data='DeepScaleR-Preview-Dataset',
                base=20.7,
                score=26.7,
                ref=22.9,
                ref_method='GRPO',
            ),
            _gain(
                **shared,
                code='ConSPO',
                method='ConSPO',
                source='Table 4 / §5.2',
                train_data='DAPO-Math-17k',
                base=20.7,
                score=25.8,
                ref=22.7,
                ref_method='GRPO',
            ),
            _gain(
                **shared,
                code='ConSPO-DAPO',
                method='ConSPO (DAPO-Math-17k)',
                source='Table 4 / §5.2',
                train_data='DAPO-Math-17k',
                base=20.7,
                score=25.8,
                ref=22.7,
                ref_method='GRPO',
            ),
            _gain(
                **shared,
                code='GRPO-DAPO',
                method='GRPO (DAPO-Math-17k)',
                source='Table 4 / §5.2',
                train_data='DAPO-Math-17k',
                base=20.7,
                score=22.7,
                ref=22.7,
                ref_method='GRPO',
            ),
            _gain(
                **shared,
                code='GRPO',
                method='GRPO',
                source='Table 4 / §5.2',
                train_data='DAPO-Math-17k',
                base=20.7,
                score=22.7,
                ref=22.7,
                ref_method='GRPO',
            ),
        ])
        rows = blg.dedupe_rows(rows)
        rows = blg.attach_ood(rows, [])
        codes = {
            (row['code'], row.get('train_data') or '')
            for row in rows
            if row['bench'] == 'AIME 2025' and row['model'].endswith('1.5B')
        }
        self.assertIn(('ConSPO', 'DeepScaleR-Preview-Dataset'), codes)
        self.assertIn(('ConSPO', 'DAPO-Math-17k'), codes)
        self.assertNotIn('ConSPO-DAPO', {code for code, _ in codes})
        self.assertNotIn('GRPO-DAPO', {code for code, _ in codes})
        grpo = next(
            row for row in rows
            if row['code'] == 'GRPO'
            and row.get('train_data') == 'DAPO-Math-17k'
            and row['bench'] == 'AIME 2025'
        )
        self.assertTrue(blg.is_self_ref(grpo))
        markdown = blg.render_md(rows, [_paper(key='arxiv:2605.12969')], [])
        self.assertNotIn('ConSPO-DAPO', markdown)
        self.assertNotIn('GRPO-DAPO', markdown)
        self.assertIn('DeepScaleR', markdown)
        self.assertIn('DAPO-Math', markdown)
        grpo_section = markdown.split('## Gain over GRPO', 1)[1]
        self.assertNotIn('[GRPO](', grpo_section.split('## Not applicable', 1)[0])

    def test_two_grpo_dapo_other_paper_kept(self):
        row = _gain(
            key='arxiv:2510.00977',
            code='2-GRPO-DAPO',
            method='2-GRPO-DAPO',
            bench='AIME 2025',
        )
        self.assertEqual(row['code'], '2-GRPO-DAPO')

    def test_dapo_code_not_stolen_by_conspo_method(self):
        row = ood.alias_conspo_code({
            'key': ood.CONSPO,
            'code': 'DAPO',
            'method': 'ConSPO-DAPO',
        })
        self.assertEqual(row['code'], 'DAPO')
        self.assertEqual(row['method'], 'ConSPO-DAPO')


class CkptAndAdmitTest(unittest.TestCase):
    def test_oneshot_validation_avg_gets_dagger(self):
        row = _gain(
            key='arxiv:2504.20571',
            code='1-shot RLVR',
            method='1-shot RLVR (GRPO)',
            model='Qwen2.5-Math-7B',
            bench='AIME 2025',
            metric='avg@8',
            base=6.7,
            score=10.8,
            ckpt_select='unspecified',
        )
        self.assertEqual(row['ckpt_select'], 'validation-avg')
        self.assertTrue(blg.best_ckpt_mark(row))
        markdown = blg.render_md([row], [_paper(key='arxiv:2504.20571')], [])
        self.assertIn('+4.1†', markdown)

    def test_online_dapo_is_temporal(self):
        row = _gain(
            key='arxiv:2606.23740',
            code='DAPO',
            method='Online DAPO',
            model='Qwen3-4B-Instruct-2507',
            bench='AIME26',
            base=16.7,
            ref=20.0,
            ref_method='GRPO',
            score=16.7,
            train_data=(
                'DeepScaleR prompts (on-policy; Table 2 adapters, '
                'same protocol as Online GRPO)'
            ),
            ood=False,
        )
        rows = blg.attach_ood([row], [])
        self.assertEqual(rows[0]['ood_basis'], 'temporal')
        self.assertEqual(blg.format_gain_cell(blg.delta_over_base(rows[0])), '+0.0')
        self.assertEqual(blg.format_gain_cell(blg.delta_over_ref(rows[0])), '-3.3')

    def test_online_dapo_raw_name_is_temporal(self):
        self.assertEqual(
            ood.classify_ood_basis(
                key='arxiv:2606.23740',
                model='Qwen3-4B-Instruct-2507',
                bench='AIME26',
                code='Online DAPO',
                method='Online DAPO',
                train_data='DeepScaleR prompts (on-policy)',
            ),
            'temporal',
        )

    def test_explicit_ckpt_not_overwritten(self):
        self.assertEqual(ood.default_ckpt_select(ood.ONESHOT, 'final'), 'final')
        self.assertEqual(ood.default_ckpt_select(ood.ONESHOT, 'best'), 'best')
        self.assertEqual(
            ood.default_ckpt_select(ood.ONESHOT, 'unspecified'),
            'validation-avg',
        )
        self.assertEqual(
            ood.default_ckpt_select(ood.ONESHOT, ''),
            'validation-avg',
        )


class PivotGroupTest(unittest.TestCase):
    def test_richness_tie_keeps_later_row(self):
        rows = [
            _gain(score=1.0, source='Table 1'),
            _gain(score=2.0, source='Table 2'),
        ]
        groups = blg.pivot_groups(rows)
        self.assertAlmostEqual(groups[0][0]['score'], 2.0)

    def test_source_clash_warns(self):
        rows = [
            _gain(score=1.0, base=0.0, source='Table 1'),
            _gain(score=2.0, base=0.0, source='Table 2'),
        ]
        with patch('builtins.print') as printed:
            blg.pivot_groups(rows)
        self.assertTrue(any(
            'pivot source clash' in ' '.join(str(arg) for arg in call.args)
            for call in printed.call_args_list
        ))


class WriteGuardTest(unittest.TestCase):
    def test_refuse_shrink(self):
        self.assertTrue(blg.refuse_shrink(10, 3, force=False))
        self.assertFalse(blg.refuse_shrink(10, 3, force=True))
        self.assertFalse(blg.refuse_shrink(10, 10, force=False))
        self.assertTrue(blg.refuse_shrink_keys({'a', 'b'}, {'a'}, force=False))
        self.assertFalse(blg.refuse_shrink_keys({'a', 'b'}, {'a'}, force=True))
        self.assertFalse(blg.refuse_shrink_keys({'a'}, {'a', 'b'}, force=False))

    def test_missing_extract_does_not_wipe(self):
        with tempfile.TemporaryDirectory() as tmp:
            tmp_path = Path(tmp)
            jsonl = tmp_path / 'llm_gains.jsonl'
            jsonl.write_text('{"key": "keep"}\n', encoding='utf-8')
            md_path = tmp_path / 'llm_gains.md'
            md_path.write_text('keep\n', encoding='utf-8')
            old = blg.JSONL_PATH, blg.MD_PATH
            blg.JSONL_PATH, blg.MD_PATH = jsonl, md_path
            try:
                code = blg.main(['--extract-dir', str(tmp_path / 'missing')])
            finally:
                blg.JSONL_PATH, blg.MD_PATH = old
            self.assertEqual(code, 1)
            self.assertEqual(jsonl.read_text(encoding='utf-8'), '{"key": "keep"}\n')
            self.assertEqual(md_path.read_text(encoding='utf-8'), 'keep\n')

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
                    'bench': 'AIME 2024',
                    'score': 1,
                }]),
                encoding='utf-8',
            )
            jsonl = tmp_path / 'llm_gains.jsonl'
            jsonl.write_text('{"key": "keep"}\n', encoding='utf-8')
            old = blg.JSONL_PATH, blg.MD_PATH
            blg.JSONL_PATH = jsonl
            blg.MD_PATH = tmp_path / 'out.md'
            try:
                code = blg.main(['--extract-dir', str(extract)])
            finally:
                blg.JSONL_PATH, blg.MD_PATH = old
            self.assertEqual(code, 1)
            self.assertEqual(jsonl.read_text(encoding='utf-8'), '{"key": "keep"}\n')
            self.assertFalse((tmp_path / 'out.md').exists())

    def test_empty_extract_listed_in_candidates_refuses(self):
        with tempfile.TemporaryDirectory() as tmp:
            tmp_path = Path(tmp)
            extract = tmp_path / 'extracts'
            extract.mkdir()
            (extract / 'candidates.json').write_text(
                json.dumps([{'key': 'arxiv:9999.99999'}]),
                encoding='utf-8',
            )
            (extract / 'arxiv_9999.99999.json').write_text('[]\n', encoding='utf-8')
            jsonl = tmp_path / 'llm_gains.jsonl'
            jsonl.write_text('{"key": "keep"}\n', encoding='utf-8')
            old = blg.JSONL_PATH, blg.MD_PATH
            blg.JSONL_PATH = jsonl
            blg.MD_PATH = tmp_path / 'out.md'
            try:
                code = blg.main(['--extract-dir', str(extract)])
            finally:
                blg.JSONL_PATH, blg.MD_PATH = old
            self.assertEqual(code, 1)
            self.assertEqual(jsonl.read_text(encoding='utf-8'), '{"key": "keep"}\n')
            self.assertFalse((tmp_path / 'out.md').exists())

    def test_filename_fills_missing_row_key(self):
        with tempfile.TemporaryDirectory() as tmp:
            extract = Path(tmp)
            (extract / 'arxiv_1111.22222.json').write_text(
                json.dumps([{
                    'model': 'Qwen3-4B',
                    'bench': 'AIME 2024',
                    'score': 1,
                    'base': 0,
                }]),
                encoding='utf-8',
            )
            by_key = blg.load_extracts(extract, {'arxiv:1111.22222'})
            self.assertEqual(list(by_key), ['arxiv:1111.22222'])
            self.assertEqual(by_key['arxiv:1111.22222'][0]['key'], 'arxiv:1111.22222')

    def test_doi_stem_restores_slash_from_known_keys(self):
        key = 'doi:10.1038/s41586-023-06924-6'
        self.assertEqual(blg.key_from_stem('doi_10.1038_s41586-023-06924-6', {key}), key)


class StrictTemporalOodTest(unittest.TestCase):
    def test_empty_train_data_is_unverified(self):
        self.assertFalse(ood.temporal_proof(
            'Qwen2.5-Math-7B', '', '', 'arxiv:2501.00001', 'GRPO', 'GRPO',
        ))
        self.assertEqual(
            ood.classify_ood_basis(
                key='arxiv:2501.00001',
                model='Qwen2.5-Math-7B',
                bench='AIME 2025',
                code='GRPO',
                method='GRPO',
                train_data='',
            ),
            'unverified',
        )

    def test_conspo_dapo_math_dates(self):
        shared = dict(
            key=ood.CONSPO,
            model='DeepSeek-R1-Distill-Qwen-1.5B',
            code='ConSPO',
            method='ConSPO',
            train_data='DAPO-Math-17k',
        )
        self.assertEqual(
            ood.classify_ood_basis(**shared, bench='AIME 2025'),
            'unverified',
        )
        self.assertEqual(
            ood.classify_ood_basis(**shared, bench='HMMT 2025'),
            'unverified',
        )
        self.assertEqual(
            ood.classify_ood_basis(**shared, bench='AIME26'),
            'temporal',
        )

    def test_oneshot_infers_deepscaler_and_stays_temporal(self):
        self.assertEqual(
            ood.infer_train_data({'key': ood.ONESHOT}),
            'DeepScaleR subset',
        )
        row = _gain(
            key=ood.ONESHOT,
            code='1-shot RLVR',
            method='1-shot RLVR (GRPO)',
            model='Qwen2.5-Math-7B',
            bench='AIME 2025',
            metric='avg@8',
            base=6.7,
            score=10.8,
            ckpt_select='unspecified',
        )
        rows = blg.renormalize_rows([row], [])
        hit = next(item for item in rows if item['code'] == '1-shot RLVR')
        self.assertEqual(hit['train_data'], 'DeepScaleR subset')
        self.assertEqual(hit['ood_basis'], 'temporal')
        self.assertTrue(blg.best_ckpt_mark(hit))
        markdown = blg.render_md(rows, [_paper(key=ood.ONESHOT)], [])
        self.assertIn('+4.1†', markdown)

    def test_two_grpo_math_vs_dapo_sub(self):
        math_row = {
            'key': ood.TWO_GRPO,
            'source': 'Table 1 (MATH train)',
        }
        dapo_row = {
            'key': ood.TWO_GRPO,
            'source': 'Table 1 (DAPO-Math-Sub)',
        }
        self.assertEqual(ood.infer_train_data(math_row), 'MATH')
        self.assertEqual(ood.infer_train_data(dapo_row), 'DAPO-Math-sub')
        self.assertEqual(
            ood.classify_ood_basis(
                key=ood.TWO_GRPO,
                model='Qwen2.5-Math-7B',
                bench='AIME 2025',
                code='2-GRPO',
                method='2-GRPO',
                train_data='MATH',
            ),
            'temporal',
        )
        self.assertEqual(
            ood.classify_ood_basis(
                key=ood.TWO_GRPO,
                model='Qwen2.5-Math-7B',
                bench='AIME 2025',
                code='2-GRPO-DAPO',
                method='2-GRPO-DAPO',
                train_data='DAPO-Math-sub',
            ),
            'unverified',
        )

    def test_hicra_aime25_unverified(self):
        self.assertEqual(ood.infer_train_data({'key': ood.HICRA}), '')
        self.assertEqual(
            ood.classify_ood_basis(
                key=ood.HICRA,
                model='Llama-3.1-8B-Instruct',
                bench='AIME 2025',
                code='HICRA',
                method='HICRA',
                train_data='',
            ),
            'unverified',
        )

    def test_sr_grpo_smoltalk2_and_self_distill_unverified(self):
        self.assertEqual(
            ood.classify_ood_basis(
                key='arxiv:2512.02807',
                model='Qwen2.5-1.5B-Instruct',
                bench='AIME 2025',
                code='SR-GRPO',
                method='SR-GRPO',
                train_data='SmolTalk2',
            ),
            'unverified',
        )
        self.assertEqual(ood.infer_train_data({'key': ood.SELF_DISTILL}), 'DAPO-Math-17k')
        self.assertEqual(
            ood.classify_ood_basis(
                key=ood.SELF_DISTILL,
                model='DeepSeek-R1-Distill-Qwen-7B',
                bench='AIME 2025',
                code='SFT',
                method='SFT',
                train_data='DAPO-Math-17k',
            ),
            'unverified',
        )

    def test_weight_geo_online_wipes_teacher_and_is_temporal(self):
        self.assertEqual(
            ood.resolve_teacher(
                ood.WEIGHT_GEO,
                'GRPO',
                'Online GRPO',
                explicit='DeepSeek-V4-Flash',
            ),
            '',
        )
        self.assertEqual(
            ood.resolve_teacher(
                ood.WEIGHT_GEO,
                'GRPO',
                'GRPO',
                explicit='DeepSeek-V4-Flash',
            ),
            'DeepSeek-V4-Flash',
        )
        self.assertEqual(
            ood.resolve_teacher(
                ood.WEIGHT_GEO,
                'DAPO',
                'DAPO',
                explicit='DeepSeek-V4-Flash',
                source='Table 2 (Online DAPO)',
            ),
            '',
        )
        self.assertNotIn(ood.WEIGHT_GEO, ood.REQUIRE_TEACHER)
        self.assertEqual(
            ood.classify_ood_basis(
                key=ood.WEIGHT_GEO,
                model='Qwen3-4B-Instruct-2507',
                bench='AIME26',
                code='GRPO',
                method='Online GRPO',
                train_data='DeepScaleR prompts (on-policy rollouts)',
                teacher='',
            ),
            'temporal',
        )

    def test_every_temporal_row_has_proof(self):
        cases = [
            (
                'DeepSeek-R1-Distill-Qwen-1.5B',
                '',
                'DeepScaleR-Preview-Dataset',
                ood.CONSPO,
                'ConSPO',
                'AIME 2025',
            ),
            (
                'Qwen3-4B-Instruct-2507',
                '',
                'DeepScaleR',
                ood.WEIGHT_GEO,
                'GRPO',
                'AIME26',
            ),
            (
                'Qwen2.5-Math-7B',
                '',
                'DeepScaleR subset',
                ood.ONESHOT,
                '1-shot RLVR',
                'AIME 2025',
            ),
            (
                'Qwen2.5-Math-7B',
                '',
                'DeepScaleR',
                ood.SHAO,
                'GRPO-majority',
                'AIME 2025',
            ),
            (
                'OLMo-2-1124-7B',
                '',
                'DeepScaleR',
                ood.SHAO,
                'GRPO',
                'AIME 2025',
            ),
        ]
        for model, teacher, train, key, code, bench in cases:
            basis = ood.classify_ood_basis(
                key=key,
                model=model,
                bench=bench,
                code=code,
                method=code,
                train_data=train,
                teacher=teacher,
            )
            self.assertEqual(basis, 'temporal')
            self.assertTrue(ood.temporal_proof(
                model, teacher, train, key, code, code,
            ))

    def test_notes_range_does_not_change_counts(self):
        row = _gain(
            key=ood.ONESHOT,
            code='1-shot RLVR',
            method='1-shot RLVR',
            model='Qwen2.5-Math-7B',
            bench='AIME 2025',
            base=6.7,
            score=10.8,
            train_data='DeepScaleR subset',
            ood_basis='temporal',
        )
        markdown = blg.render_md([row], [_paper(key=ood.ONESHOT)], [])
        self.assertIn('−0.4…+4.5', markdown)
        self.assertIn('2506.10947', markdown)
        self.assertIn('2601.11061', markdown)
        self.assertIn('Leakage-free', markdown)
        self.assertIn('Llama-3.1-8B', markdown)
        self.assertIn('OLMo-2-1124-7B', markdown)
        self.assertIn('LiveMathBench', markdown)
        self.assertIn('leakage_free: true', markdown)
        self.assertIn('Figure 3', markdown)
        self.assertIn('id` / `rl_stage', markdown)
        self.assertIn('step 300', markdown)
        self.assertIn('‡', markdown)
        self.assertIn('**1**', markdown.split('## Notes', 1)[0])
        self.assertNotIn('source_precision', markdown)
        self.assertNotIn("'plot'", markdown)

    def test_renormalize_byte_idempotent(self):
        raw = _gain(
            key=ood.ONESHOT,
            code='1-shot RLVR',
            method='1-shot RLVR (GRPO)',
            model='Qwen2.5-Math-7B',
            bench='AIME 2025',
            base=6.7,
            score=10.8,
            source='Table 4',
        )
        papers = [_paper(key=ood.ONESHOT)]
        once = blg.renormalize_rows([raw], [], papers)
        twice = blg.renormalize_rows(once, [], papers)
        with tempfile.TemporaryDirectory() as tmp:
            path = Path(tmp) / 'gains.jsonl'
            write_jsonl(path, once, sort_keys=True)
            first = path.read_bytes()
            write_jsonl(path, twice, sort_keys=True)
            self.assertEqual(first, path.read_bytes())

    def test_math_cutoff_is_token_not_substring(self):
        self.assertEqual(
            ood.dataset_cutoff('MATH'),
            ood.MATH_DATASET_CUTOFF.day,
        )
        self.assertEqual(
            ood.dataset_cutoff('MATH (7,500 step-by-step competition problems)'),
            ood.MATH_DATASET_CUTOFF.day,
        )
        self.assertEqual(
            ood.dataset_cutoff('MATH train'),
            ood.MATH_DATASET_CUTOFF.day,
        )
        self.assertIsNone(ood.dataset_cutoff('OpenR1-Math-220k'))
        self.assertIsNone(ood.dataset_cutoff('OpenThoughts mathematical reasoning'))
        self.assertIsNone(ood.dataset_cutoff('Qwen2.5-Math-7B trajectories'))
        self.assertIsNone(ood.dataset_cutoff('math_verify-only corpus'))
        self.assertIsNone(ood.dataset_cutoff('50 mixed-success math problems'))

    def test_hicra_ignores_single_inventory_train(self):
        models = [
            blm.normalize_row({
                'model': 'Llama-3.1-8B-Instruct',
                'start_point': 'instruct',
                'role': 'trained',
                'method': 'HICRA',
                'train_data': ['DeepScaleR'],
                'eval_ood': ['AIME 2025'],
            }, _paper(key=ood.HICRA)),
        ]
        row = _gain(
            key=ood.HICRA,
            code='HICRA',
            method='HICRA',
            model='Llama-3.1-8B-Instruct',
            bench='AIME 2025',
            train_data='',
            ood=False,
        )
        rows = blg.attach_ood(blg.attach_train_data([row], models), models)
        self.assertEqual(rows[0]['train_data'], '')
        self.assertEqual(rows[0]['ood_basis'], 'unverified')

    def test_conspo_html_table1_cells(self):
        self.assertEqual(
            ood.CONSPO_T1_1P5[('ConSPO', 'AIME 2025')],
            (20.7, 26.7, 22.9),
        )
        self.assertEqual(
            ood.CONSPO_T1_1P5[('SAPO', 'HMMT 2025')],
            (9.7, 12.8, 11.7),
        )

    def test_html_score_beats_gain_only(self):
        rows = ood.apply_gain_overrides([
            _gain(
                key=ood.CONSPO,
                code='ConSPO',
                method='ConSPO',
                model='DeepSeek-R1-Distill-Qwen-7B',
                bench='AIME 2025',
                metric='avg@32',
                source='Table 2 / §5.2',
                train_data='DeepScaleR-Preview-Dataset',
                base=30.3,
                ref=35.9,
                score=None,
                gain=8.8,
                gain_ref=3.2,
            ),
        ])
        rows = blg.dedupe_rows(rows)
        hit = next(
            row for row in rows
            if row['code'] == 'ConSPO'
            and row['model'].endswith('7B')
            and row['bench'] == 'AIME 2025'
        )
        self.assertAlmostEqual(hit['score'], 39.1)
        self.assertAlmostEqual(hit['base'], 30.3)


class ShaoAime25PlotTest(unittest.TestCase):
    def _plot_rows(self):
        rows = [
            row for row in ood.apply_gain_overrides([])
            if row.get('key') == ood.SHAO
            and row.get('source') == ood.SHAO_PLOT_SOURCE
        ]
        return blg.attach_ood(blg.coerce_pp_rows(rows), [])

    def test_injects_fifty_temporal_plot_rows(self):
        rows = self._plot_rows()
        self.assertEqual(len(rows), 50)
        self.assertEqual({row['bench'] for row in rows}, {'AIME 2025'})
        self.assertEqual({row['metric'] for row in rows}, {'avg@8'})
        self.assertEqual({row['train_data'] for row in rows}, {'DeepScaleR'})
        self.assertEqual({row['unit'] for row in rows}, {'pp'})
        self.assertEqual({row['source_precision'] for row in rows}, {'plot'})
        self.assertTrue(all(row['ood_basis'] == 'temporal' for row in rows))
        self.assertEqual(
            sum(1 for row in rows if blg.delta_over_base(row) is not None),
            50,
        )
        self.assertEqual(
            sum(
                1 for row in rows
                if not blg.is_self_ref(row)
                and blg.delta_over_ref(row) is not None
            ),
            40,
        )

    def test_math7b_last_point_not_curve_max(self):
        rows = {row['code']: row for row in self._plot_rows()
                if row['model'] == 'Qwen2.5-Math-7B'}
        self.assertAlmostEqual(rows['GRPO']['base'], 6.3)
        self.assertAlmostEqual(rows['GRPO']['score'], 13.7)
        self.assertAlmostEqual(blg.delta_over_base(rows['GRPO']), 7.4)
        self.assertAlmostEqual(blg.delta_over_base(rows['GRPO-majority']), 4.5)
        self.assertAlmostEqual(blg.delta_over_ref(rows['GRPO-majority']), -3.8)
        self.assertAlmostEqual(blg.delta_over_base(rows['GRPO-incorrect']), 2.8)
        self.assertAlmostEqual(blg.delta_over_ref(rows['GRPO-incorrect']), -6.8)
        self.assertAlmostEqual(blg.delta_over_base(rows['GRPO-format']), -0.4)
        self.assertAlmostEqual(blg.delta_over_ref(rows['GRPO-format']), -8.7)
        self.assertAlmostEqual(blg.delta_over_base(rows['GRPO-random']), 2.4)
        self.assertAlmostEqual(blg.delta_over_ref(rows['GRPO-random']), -5.0)
        self.assertNotAlmostEqual(
            blg.delta_over_base(rows['GRPO-incorrect']), 6.0,
        )

    def test_math15b_vs_gt(self):
        rows = {row['code']: row for row in self._plot_rows()
                if row['model'] == 'Qwen2.5-Math-1.5B'}
        self.assertAlmostEqual(blg.delta_over_base(rows['GRPO']), 1.5)
        self.assertAlmostEqual(blg.delta_over_base(rows['GRPO-majority']), 3.4)
        self.assertAlmostEqual(blg.delta_over_ref(rows['GRPO-majority']), -0.2)
        self.assertAlmostEqual(blg.delta_over_base(rows['GRPO-incorrect']), 0.7)
        self.assertAlmostEqual(blg.delta_over_ref(rows['GRPO-incorrect']), -0.8)
        self.assertAlmostEqual(blg.delta_over_base(rows['GRPO-format']), -0.7)
        self.assertAlmostEqual(blg.delta_over_ref(rows['GRPO-format']), -2.2)
        self.assertAlmostEqual(blg.delta_over_base(rows['GRPO-random']), -0.8)
        self.assertAlmostEqual(blg.delta_over_ref(rows['GRPO-random']), -2.3)

    def test_llama_random_ends_at_287_without_dagger(self):
        hit = next(
            row for row in self._plot_rows()
            if row['model'] == 'Llama-3.2-3B' and row['code'] == 'GRPO-random'
        )
        self.assertEqual(hit['ckpt_select'], ood.SHAO_PLOT_CKPT_287)
        self.assertFalse(blg.best_ckpt_mark(hit))
        self.assertTrue(all(
            not blg.best_ckpt_mark(row) for row in self._plot_rows()
        ))

    def test_majority_alias_and_noisy_cells(self):
        self.assertEqual(
            blg.method_to_code('GRPO (majority vote)', 'GRPO'),
            'GRPO-majority',
        )
        self.assertTrue(blg.is_qualified_grpo_name('GRPO-majority'))
        fmt = next(
            row for row in self._plot_rows()
            if row['model'] == 'Qwen2.5-Math-7B' and row['code'] == 'GRPO-format'
        )
        maj = next(
            row for row in self._plot_rows()
            if row['model'] == 'Qwen2.5-Math-7B'
            and row['code'] == 'GRPO-majority'
        )
        self.assertEqual(blg.base_cell(fmt), '-0.4‡')
        self.assertEqual(blg.base_cell(maj), '+4.5')
        self.assertEqual(blg.grpo_cell(fmt), '-8.7')
        markdown = blg.render_md(
            self._plot_rows(), [_paper(key=ood.SHAO)], [],
        )
        self.assertNotIn('### Qwen2.5-Math-7B', markdown)
        self.assertIn('−0.4…+4.5', markdown)
        table_cells = ''.join(
            line for line in markdown.splitlines()
            if line.startswith('|') and '---' not in line and 'method' not in line
        )
        self.assertNotIn('+6.0', table_cells)
        self.assertNotIn('†', table_cells)
        self.assertNotIn('source_precision', markdown)
        self.assertTrue(blg.is_self_ref(next(
            row for row in self._plot_rows()
            if row['model'] == 'Qwen2.5-Math-7B' and row['code'] == 'GRPO'
        )))

    def test_small_pp_values_stay_pp(self):
        hit = next(
            row for row in self._plot_rows()
            if row['model'] == 'Qwen2.5-1.5B' and row['code'] == 'GRPO'
        )
        self.assertAlmostEqual(hit['base'], 0.4)
        self.assertAlmostEqual(hit['score'], 1.5)
        self.assertEqual(hit['unit'], 'pp')

    def test_skip_if_scored_pair_exists(self):
        existing = {
            'key': ood.SHAO,
            'code': 'GRPO-majority',
            'method': 'GRPO (majority vote)',
            'model': 'Qwen2.5-Math-7B',
            'bench': 'AIME 2025',
            'metric': 'avg@8',
            'base': 5.4,
            'score': 9.9,
            'source': ood.SHAO_PLOT_SOURCE,
            'train_data': 'DeepScaleR',
            'unit': 'pp',
        }
        rows = [
            row for row in ood.apply_gain_overrides([existing])
            if row.get('key') == ood.SHAO
            and row.get('source') == ood.SHAO_PLOT_SOURCE
            and row.get('code') == 'GRPO-majority'
            and row.get('model') == 'Qwen2.5-Math-7B'
        ]
        self.assertEqual(len(rows), 1)
        self.assertAlmostEqual(rows[0]['score'], 9.9)


class CutoffProvenanceTest(unittest.TestCase):
    def test_empty_source_cutoff_is_unverified(self):
        rec = ood.Cutoff(date(2024, 10, 1), '', 'content')
        self.assertIsNone(ood.usable_day(rec))
        with patch.object(ood, 'DATASET_CUTOFFS', (('deepscaler', rec),)):
            self.assertIsNone(ood.dataset_cutoff('DeepScaleR'))
            self.assertEqual(
                ood.classify_ood_basis(
                    key='arxiv:2501.00001',
                    model='Qwen2.5-Math-7B',
                    bench='AIME 2025',
                    train_data='DeepScaleR',
                ),
                'unverified',
            )

    def test_deepscaler_content_bound_admits_aime25(self):
        self.assertEqual(ood.dataset_cutoff('DeepScaleR'), date(2025, 1, 26))
        self.assertEqual(
            ood.classify_ood_basis(
                key=ood.SHAO,
                model='Qwen2.5-Math-7B',
                bench='AIME 2025',
                train_data='DeepScaleR',
            ),
            'temporal',
        )
        release = date(2025, 2, 9)
        self.assertFalse(date(2025, 2, 6) > release)

    def test_sourced_cutoff_dates(self):
        self.assertEqual(
            ood.model_cutoff('Qwen3-4B-Instruct-2507'), date(2025, 8, 6),
        )
        self.assertEqual(ood.model_cutoff('OLMo-2-1124-7B'), date(2024, 11, 26))
        self.assertEqual(ood.bench_date('AIME 2025'), date(2025, 2, 6))
        self.assertEqual(ood.PAPER_HMMT_DATE[ood.CONSPO].day, date(2025, 2, 15))
        self.assertTrue(ood.model_cutoff_rec('Qwen2.5-Math-7B').source)
        self.assertTrue(ood.dataset_cutoff_rec('DeepScaleR').source)
        self.assertTrue(ood.BENCH_DATES['AIME 2025'].source)

    def test_temporal_rows_carry_proof(self):
        rows = blg.renormalize_rows(read_jsonl(blg.JSONL_PATH), [], [])
        temporal = [row for row in rows if row.get('ood_basis') == 'temporal']
        self.assertGreaterEqual(len(temporal), 50)
        for row in temporal:
            self.assertTrue(row['model_cutoff'], row)
            self.assertTrue(row['train_cutoff'], row)
            self.assertTrue(row['benchmark_date'], row)
            src = row['cutoff_source']
            self.assertTrue(src['model'], row)
            self.assertTrue(src['train'], row)
            self.assertTrue(src['bench'], row)
            if row.get('teacher'):
                self.assertTrue(row['teacher_cutoff'], row)
                self.assertTrue(src['teacher'], row)
            else:
                self.assertFalse(row['teacher_cutoff'])
            bench = date.fromisoformat(row['benchmark_date'])
            cuts = [
                date.fromisoformat(row['model_cutoff']),
                date.fromisoformat(row['train_cutoff']),
            ]
            if row['teacher_cutoff']:
                cuts.append(date.fromisoformat(row['teacher_cutoff']))
            self.assertGreater(bench, max(cuts), row)

    def test_readme_paper_keys_are_scoreable(self):
        keys = readme_paper_keys()
        self.assertGreater(len(keys), 50)
        self.assertEqual(len(keys), len(set(keys)))
        for key in keys:
            self.assertIn(key.split(':', 1)[0], SCOREABLE_KINDS)

    def test_readme_paper_keys_match_papers_jsonl(self):
        if not PAPERS_JSONL.exists():
            self.skipTest('papers.jsonl not checked out')
        jsonl_keys = [row['key'] for row in read_jsonl(PAPERS_JSONL)]
        readme_keys = readme_paper_keys()
        shared = [key for key in readme_keys if key in set(jsonl_keys)]
        self.assertEqual(shared, jsonl_keys)

    def test_papers_in_readme_order_fills_section_without_jsonl(self):
        with patch('paths.PAPERS_JSONL', Path('missing-papers.jsonl')):
            papers = papers_in_readme_order()
        self.assertGreater(len(papers), 50)
        self.assertTrue(all(paper.get('section') for paper in papers))

    def test_write_jsonl_lf_only(self):
        with tempfile.TemporaryDirectory() as tmp:
            path = Path(tmp) / 'rows.jsonl'
            write_jsonl(path, [{'a': 1}])
            raw = path.read_bytes()
            self.assertNotIn(b'\r', raw)
            self.assertTrue(raw.endswith(b'\n'))

    def test_append_jsonl_lf_only(self):
        with tempfile.TemporaryDirectory() as tmp:
            path = Path(tmp) / 'rows.jsonl'
            append_jsonl(path, {'a': 1})
            raw = path.read_bytes()
            self.assertNotIn(b'\r', raw)
            self.assertTrue(raw.endswith(b'\n'))


class LeakageFreeTest(unittest.TestCase):
    def test_leakage_free_models_and_benches(self):
        self.assertTrue(ood.leakage_free('Llama-3.2-3B-Instruct', 'MATH-500'))
        self.assertTrue(ood.leakage_free('Llama-3.1-8B-Base', 'AMC 2023'))
        self.assertTrue(ood.leakage_free('OLMo-2-1124-7B-SFT', 'Minerva Math'))
        self.assertFalse(ood.leakage_free('Qwen2.5-Math-7B', 'MATH-500'))
        self.assertFalse(ood.leakage_free('Llama-3-8B', 'MATH-500'))
        self.assertFalse(ood.leakage_free('Llama-3.1-8B', 'OlympiadBench'))
        self.assertFalse(ood.leakage_free('Llama-3.1-8B', 'AIME 2025'))

    def test_attach_ood_sets_flag_without_changing_basis(self):
        rows = blg.attach_ood([
            _gain(
                model='Llama-3.2-3B-Instruct',
                bench='MATH-500',
                train_data='DeepScaleR',
                base=26.4,
                score=52.8,
            ),
        ], [])
        self.assertTrue(rows[0]['leakage_free'])
        self.assertIn('leakage_free', blg.ROW_FIELDS)
        self.assertEqual(rows[0]['ood_basis'], 'rl_stage')
        self.assertFalse(rows[0]['ood'])

    def test_render_md_places_llama_not_qwen(self):
        llama = blg.attach_ood([
            _gain(
                key=ood.CONSPO,
                code='ConSPO',
                method='ConSPO',
                model='Llama-3.2-3B-Instruct',
                bench='MATH-500',
                train_data='DeepScaleR-Preview-Dataset',
                base=26.4,
                score=52.8,
            ),
        ], [])
        qwen = blg.attach_ood([
            _gain(
                bench='MATH-500',
                train_data='MATH',
                base=49.4,
                score=70.8,
            ),
        ], [])
        markdown = blg.render_md(
            llama + qwen,
            [_paper(key=ood.CONSPO, title='ConSPO'), _paper()],
            [],
        )
        leak, rest = markdown.split('## Gain over the starting checkpoint', 1)
        self.assertIn(
            'Leakage-free: gain over the starting checkpoint', leak,
        )
        self.assertIn('MATH500', leak)
        self.assertIn('+26.4', leak)
        temporal = rest.split('## Not applicable', 1)[0]
        self.assertNotIn('MATH500', temporal)
        self.assertNotIn('+21.4', markdown)


if __name__ == '__main__':
    unittest.main()
