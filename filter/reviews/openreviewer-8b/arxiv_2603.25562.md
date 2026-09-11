# Review

## Summary
This paper revisits on-policy distillation (OPD) for LLM post-training from both theoretical and implementation perspectives. Theoretically, the paper explains why token-level OPD is an attractive approximation for long-horizon training: it is biased relative to sequence-level reverse-KL, but avoids future-reward coupling and has substantially better worst-case variance scaling. Empirically, the paper shows that the standard sampled-token implementation can provide brittle supervision because its signal is imbalanced, can remain misleading on student-drifted prefixes, and is sensitive to tokenizer or special-token mismatch. Teacher top-KK local support matching addresses these issues by preserving local token-level updates while replacing one-token supervision with a truncated distribution-level comparison. Across single-task math reasoning and alternating agentic-plus-reasoning training, this simple modification improves optimization stability and downstream performance over sampled-token OPD, while also clarifying where teacher matching remains an imperfect proxy for task success.

## Soundness
3

## Presentation
3

## Contribution
3

## Strengths
1. The paper is well-written and easy to follow.
2. The proposed method is simple and effective.
3. The experiments are comprehensive.

## Weaknesses
1. The experiments are conducted on 7B models, and it would be better to see the performance on larger models.
2. The paper does not discuss the computational cost of the proposed method.

## Questions
1. How does the proposed method perform on larger models?
2. What is the computational cost of the proposed method compared to the baselines?

## Flag For Ethics Review
No ethics review needed.

## Details Of Ethics Concerns


## Rating
6

## Confidence
4