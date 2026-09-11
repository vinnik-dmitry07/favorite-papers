# Review

## Summary
This paper proposes a new way to evaluate whether a language model has learned an implicit world model. The authors propose to use the Myhill-Nerode theorem, which states that two distinct states in a deterministic finite automaton (DFA) can be distinguished by some sequence of input. The authors propose two metrics: (1) sequence compression, which looks at whether the model predicts the same set of sequences to be possible from two states that are the same; and (2) sequence distinction, which looks at whether the model acts as if two sequences are possible from different states. The authors show that these metrics are more sensitive than the existing approach of just looking at the percentage of valid next-tokens.

## Soundness
4

## Presentation
4

## Contribution
3

## Strengths
- The proposed metrics are well-motivated by the Myhill-Nerode theorem and are a natural extension of existing work on evaluating world models.
- The metrics are clearly defined and easy to understand.
- The experiments are thorough and clearly demonstrate the usefulness of the proposed metrics.

## Weaknesses
- The proposed metrics are only applicable to DFAs, which is a relatively simple class of world models.
- The proposed metrics are still quite computationally expensive to calculate, as they require sampling a lot of sequences from the model.

## Questions
- How sensitive are the results to the choice of sampling method and sampling parameters (e.g. temperature, top-k, top-p)?
- How well do the metrics scale to larger models and datasets?

## Flag For Ethics Review
No ethics review needed.

## Details Of Ethics Concerns


## Rating
8

## Confidence
4