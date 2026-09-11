# Review

## Summary
This paper proposes a new method, SRPO, which combines GRPO and SDPO. SRPO uses GRPO for correct samples and SDPO for failed samples. The paper identifies that the self-distillation in SDPO can be harmful for already-correct samples and the quality of the self-teacher’s distillation signal degrades as training progresses. The paper shows that SRPO can achieve better performance than GRPO and SDPO on 5 benchmarks.

## Soundness
3

## Presentation
3

## Contribution
2

## Strengths
- The paper is well-written and easy to follow.
- The idea is simple and easy to implement.
- The experiments show that the proposed method can achieve better performance than GRPO and SDPO.

## Weaknesses
- The idea is a bit incremental. It is a simple combination of GRPO and SDPO. The novelty may be limited.
- The experiments are not comprehensive. Why not include the experiments on math benchmarks (e.g., GSM8K, MATH)? These benchmarks are also important to evaluate the reasoning ability of LLMs. The paper only evaluates the model on 5 benchmarks, which may not be sufficient to show the generalization of the proposed method.

## Questions
- Why not include the experiments on math benchmarks (e.g., GSM8K, MATH)?

## Flag For Ethics Review
No ethics review needed.

## Details Of Ethics Concerns


## Rating
5

## Confidence
4