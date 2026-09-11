# Review

## Summary
This paper investigates the limitations of large language models (LLMs) in performing multi-operand addition, revealing a fundamental limitation due to a one-digit lookahead heuristic. The authors demonstrate that while this heuristic works well for two-operand addition, it fails with multiple operands, especially when carries propagate across digits, leading to inaccuracies in the results. The paper presents empirical evidence through probing experiments and shows that this limitation persists across different LLMs, regardless of their tokenization strategy. The study provides insights into why LLMs struggle with complex arithmetic tasks and suggests that enhancing lookahead capabilities may be crucial for improving their mathematical performance.

## Soundness
3

## Presentation
3

## Contribution
3

## Strengths
1. The paper identifies a fundamental limitation in LLMs related to their addition of multiple operands, providing valuable insights into the models' arithmetic capabilities.
2. The authors conduct probing experiments to investigate how LLMs perform two-operand addition, revealing a one-digit lookahead heuristic.
3. The study shows that the identified heuristic also applies to multi-operand addition, explaining the decline in performance as the number of operands increases.
4. The paper demonstrates that the observed limitations persist across different LLMs and tokenization strategies, highlighting a general issue in LLMs.

## Weaknesses
1. The paper focuses solely on addition, and it is unclear if the identified limitation extends to other mathematical operations.
2. The study does not explore whether larger models within the same family exhibit deeper lookahead capabilities, which could potentially improve performance.
3. The authors do not propose or implement methods to overcome the shallow lookahead limitation, which would have strengthened the paper's practical contributions.

## Questions
1. Do you think this limitation is only present in smaller LLMs? Larger LLMs might have better performance in this regard.

## Flag For Ethics Review
No ethics review needed.

## Details Of Ethics Concerns


## Rating
6

## Confidence
4