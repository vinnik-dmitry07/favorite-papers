'''Anti-regression tests for the OOD gain tables.'''

from __future__ import annotations

import json
import sys
import tempfile
import unittest
from pathlib import Path
from unittest.mock import patch

FILTER_DIR = Path(__file__).resolve().parent
sys.path.insert(0, str(FILTER_DIR))

import build_llm_gains as blg
import build_llm_models as blm
import llm_gains_ood as ood
from llm_reliability import SHAO_MATH500_GT_PP, SHAO_MATH500_RANDOM_PP


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
            _gain(model='Qwen2.5-7B-Instruct', bench='AIME 2025', score=20, base=10),
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
        self.assertIsNotNone(ood.chain_cutoff(
            'Qwen2.5-Math-7B',
            '',
            '',
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


if __name__ == '__main__':
    unittest.main()
