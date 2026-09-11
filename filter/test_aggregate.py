'''Anti-regression specification for aggregation invariants.'''

from __future__ import annotations

import sys
import unittest
from pathlib import Path

FILTER_DIR = Path(__file__).resolve().parent
sys.path.insert(0, str(FILTER_DIR))
sys.path.insert(0, str(FILTER_DIR / 'remote'))

from aggregate import (
    MODELS,
    apply_cycle_overlay,
    family_composites,
    posterior,
    recover_unparsed_row,
    reliability_q,
    reliability_weight,
    vote_pm,
)
from build_report import clip_sentence, review_href, usable_weak_text
from parse_review import parse_review
from paths import is_score_row, last_valid_by_key

CYCLE_BODY = '''## Reviewer
### Soundness
3 good
### Presentation
2 fair
### Contribution
4 excellent
### Rating
7: accept, good paper
**********
## Reviewer
### Soundness
1 poor
### Presentation
1 poor
### Contribution
1 poor
no rating here
**********
## Reviewer
### Soundness
2 fair
### Presentation
4 excellent
### Contribution
3 good
### Rating
5: marginally below the acceptance threshold
## Meta Review
### Paper Decision
Reject
'''


def _empty_maps() -> tuple[dict, dict]:
    model_z = {name: {} for name in MODELS}
    model_w = {name: {} for name in MODELS}
    return model_z, model_w


class ReliabilityQTest(unittest.TestCase):
    def test_reliability_q_is_lambda_squared_not_lambda_over_psi(self):
        zs = [1.0, -0.5, 0.2]
        lams = [0.8, 0.4, 0.3]
        rel = reliability_q(zs, lams)
        num_rel = 0.0
        num_gauss = 0.0
        w_present = 0.0
        for z, lam in zip(zs, lams):
            psi = 1.0 - lam * lam
            w_rel = (lam * lam) / psi
            w_gauss = lam / psi
            num_rel += w_rel * z
            num_gauss += w_gauss * z
            w_present += w_rel
        factor = num_gauss / (1.0 + w_present)
        self.assertGreater(abs(rel - factor), 0.05)
        self.assertAlmostEqual(rel, num_rel / (1.0 + w_present))

    def test_reliability_weight_formula(self):
        self.assertAlmostEqual(reliability_weight(0.8), 0.64 / 0.36)


class FamilyValueCoverageTest(unittest.TestCase):
    def test_missing_member_preserves_family_value_but_reduces_coverage(self):
        model_z, model_w = _empty_maps()
        for member in ('dr7b', 'dr7bf', 'dr14b'):
            model_z[member]['full'] = 2.0
            model_w[member]['full'] = 1.0
            model_z[member]['low'] = 0.0
            model_w[member]['low'] = 1.0
        model_z['dr7b']['partial'] = 2.0
        model_z['dr7bf']['partial'] = 2.0
        model_w['dr7b']['partial'] = 1.0
        model_w['dr7bf']['partial'] = 1.0
        family_z, extra = family_composites(model_z, model_w)
        deep_z = family_z['deep']
        deep_cov = extra['family_cov']['deep']
        self.assertAlmostEqual(deep_z['full'], deep_z['partial'])
        self.assertLess(deep_cov['partial'], deep_cov['full'])
        self.assertAlmostEqual(deep_cov['full'], 1.0)

    def test_fully_missing_family_is_absent_from_family_z(self):
        model_z, model_w = _empty_maps()
        model_z['cr8b']['p'] = 1.0
        model_w['cr8b']['p'] = 1.0
        model_z['cr8b']['zero'] = 1.0
        model_w['cr8b']['zero'] = 0.0
        family_z, extra = family_composites(model_z, model_w)
        self.assertNotIn('p', family_z.get('deep', {}))
        self.assertNotIn('zero', family_z.get('cr8b', {}))
        self.assertNotIn('zero', extra['family_cov'].get('cr8b', {}))
        self.assertIn('p', family_z['cr8b'])

    def test_confidence_is_coverage_not_prior(self):
        family_z = {'a': {'p': 1.0}, 'b': {'p': 0.0}}
        family_cov = {'a': {'p': 0.5}, 'b': {'p': 1.0}}
        weights = {'a': 2.0, 'b': 2.0}
        signs = {'a': 1.0, 'b': 1.0}
        q_hat, conf = posterior(
            family_z, family_cov, weights, signs, ['p'], ['a', 'b'],
        )
        self.assertAlmostEqual(q_hat['p'], 2.0 / 5.0)
        self.assertAlmostEqual(conf['p'], 0.75)


class EnrichOverlayTest(unittest.TestCase):
    def test_enrich_none_clears_stale_cycle_fields(self):
        row = {
            'key': 'x',
            'rating': 9.0,
            'soundness': 4.0,
            'presentation': 4.0,
            'contribution': 4.0,
            'error': 'unparsed:ok',
        }
        parsed = {
            'rating': 6.0,
            'decision': 'Reject',
            'soundness': None,
            'presentation': 2.0,
            'contribution': None,
            'weaknesses': 'late',
            'n_valid': 1,
            'expected_n': 4,
        }
        out = apply_cycle_overlay(row, parsed)
        self.assertIsNone(out['soundness'])
        self.assertIsNone(out['contribution'])
        self.assertEqual(out['presentation'], 2.0)
        self.assertEqual(out['rating'], 6.0)

    def test_successful_enrich_clears_error(self):
        row = {'key': 'x', 'error': 'unparsed:ok', 'rating': 3.0}
        parsed = {
            'rating': 7.0,
            'decision': 'Accept',
            'soundness': 3.0,
            'presentation': 3.0,
            'contribution': 3.0,
            'n_valid': 4,
            'expected_n': 4,
        }
        out = apply_cycle_overlay(row, parsed)
        self.assertNotIn('error', out)
        self.assertEqual(out['rating'], 7.0)

    def test_reparsed_full_rating_is_not_salvage(self):
        row = {'key': 'x', 'error': 'unparsed:ok', 'salvage': True}
        parsed = {
            'rating': 6.5,
            'decision': 'Accept',
            'soundness': 3.0,
            'presentation': 2.0,
            'contribution': 3.0,
        }
        recovered, kind = recover_unparsed_row(row, parsed)
        self.assertEqual(kind, 'full')
        self.assertNotIn('salvage', recovered)
        self.assertNotIn('error', recovered)
        over = apply_cycle_overlay(row, parsed)
        self.assertNotIn('salvage', over)


class CycleReviewSetTest(unittest.TestCase):
    def test_cycle_spc_uses_same_rating_valid_set(self):
        parsed = parse_review(CYCLE_BODY, kind='cycle')
        self.assertEqual(parsed['n_valid'], 2)
        self.assertEqual(parsed['expected_n'], 4)
        self.assertAlmostEqual(parsed['rating'], 6.0)
        self.assertAlmostEqual(parsed['soundness'], 2.5)
        self.assertAlmostEqual(parsed['presentation'], 3.0)
        self.assertAlmostEqual(parsed['contribution'], 3.5)
        self.assertEqual(parsed['decision'], 'Reject')


class SalvageVoteTest(unittest.TestCase):
    def test_salvage_spc_has_no_vote_and_no_family_value(self):
        spec = MODELS['dr7b']
        row = {
            'key': 'x',
            'salvage': True,
            'soundness': 3.0,
            'presentation': 2.0,
            'contribution': 3.0,
        }
        self.assertIsNone(vote_pm(row, spec))
        recovered, kind = recover_unparsed_row(
            {'key': 'x', 'error': 'unparsed:ok'},
            {'soundness': 3.0, 'presentation': 2.0, 'contribution': 3.0},
        )
        self.assertEqual(kind, 'salvage')
        self.assertTrue(recovered['salvage'])
        self.assertIsNone(recovered.get('rating'))
        model_z, model_w = _empty_maps()
        model_z['cr8b']['only'] = 1.0
        model_w['cr8b']['only'] = 0.5
        family_z, extra = family_composites(model_z, model_w)
        self.assertNotIn('only', family_z.get('deep', {}))
        self.assertNotIn('only', extra['family_cov'].get('deep', {}))


class WeaknessesSnippetTest(unittest.TestCase):
    def test_drops_deepreviewer_outline(self):
        junk = (
            'Weaknesses, Suggestions, and Questions. Finally, I will output'
        )
        self.assertEqual(usable_weak_text(junk), '')
        long_plan = (
            '. Then I will output the Finally Review Output. Based on the '
            'original template, I should write about motivation, methods, '
            'results, and comparisons. Finally, I will output the metareview '
            'thinking and the finally revised output.'
        )
        self.assertEqual(usable_weak_text(long_plan), '')
        real = (
            'The paper lacks a theoretical analysis of the method and only '
            'evaluates a few tasks.'
        )
        self.assertEqual(usable_weak_text(real), real)


class ClipSentenceTest(unittest.TestCase):
    def test_short_text_unchanged(self):
        text = 'The paper lacks a theoretical analysis of the method.'
        self.assertEqual(clip_sentence(text), text)

    def test_fragment_gets_ellipsis(self):
        text = 'The paper could benefit from more examples and illustrations'
        self.assertEqual(clip_sentence(text), text + '…')

    def test_strips_sea_prefix(self):
        text = '** - The paper lacks a theoretical analysis of the method and only evaluates a few tasks.'
        self.assertEqual(
            clip_sentence(text),
            'The paper lacks a theoretical analysis of the method and only evaluates a few tasks.',
        )

    def test_breaks_at_sentence(self):
        text = (
            'The main weakness is the limited evaluation on toy worlds. '
            'The authors do not compare against recent world models. '
            'A third issue is missing ablations on the action head. '
            'A fourth issue is that the discussion of related work is incomplete. '
        ) * 4
        out = clip_sentence(text)
        body = out[:-1]
        self.assertTrue(out.endswith('.…'))
        self.assertLessEqual(len(body), 400)
        self.assertGreaterEqual(len(body), 120)
        self.assertTrue(text.startswith(body))

    def test_breaks_at_question(self):
        text = (
            'Is the evaluation broad enough to support the claim? '
            'Does the paper compare against recent world models? '
            'Are the ablations complete enough for this setting? '
        ) * 5
        out = clip_sentence(text)
        self.assertTrue(out.endswith('?…'))

    def test_never_ends_mid_word(self):
        text = ' '.join(['weakness'] * 80)
        out = clip_sentence(text, limit=80)
        self.assertTrue(out.endswith('…'))
        last = out[:-1].rstrip().split()[-1]
        self.assertEqual(last, 'weakness')
        self.assertFalse(out[:-1].endswith('weakne'))

    def test_review_href(self):
        self.assertEqual(
            review_href('cyclereviewer-8b', 'arxiv:2608.17163'),
            'reviews/cyclereviewer-8b/arxiv_2608.17163.md#weaknesses',
        )


class LastValidTest(unittest.TestCase):
    def test_reparse_uses_last_valid(self):
        rows = [
            {'key': 'a', 'rating': 6.0},
            {'key': 'a', 'error': 'unparsed:ok'},
            {'key': 'b', 'error': 'no_fulltext'},
            {'key': 'b', 'rating': 4.0},
            {'key': 'c', 'error': 'unparsed:ok'},
        ]
        merged = last_valid_by_key(rows)
        out = {row['key']: row for row in merged}
        self.assertEqual(out['a']['rating'], 6.0)
        self.assertEqual(out['b']['rating'], 4.0)
        scored = {row['key']: row for row in merged if is_score_row(row)}
        self.assertIn('a', scored)
        self.assertIn('b', scored)
        self.assertNotIn('c', scored)


if __name__ == '__main__':
    unittest.main()
