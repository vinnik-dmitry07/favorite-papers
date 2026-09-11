# Review

## Summary
This paper proposes a new reasoning paradigm for LLMs called Coconut, which performs reasoning in a continuous latent space. Specifically, the authors train LLMs to predict hidden states instead of actual tokens in the final stages of training. The authors evaluate their method on logical reasoning tasks and math reasoning tasks. On logical reasoning tasks, the proposed method outperforms CoT baselines.

## Soundness
2

## Presentation
3

## Contribution
2

## Strengths
1. The paper is well-written and easy to follow.
2. The proposed method is novel and interesting.
3. The proposed method outperforms CoT baselines on logical reasoning tasks.

## Weaknesses
1. The proposed method underperforms CoT baselines on math reasoning tasks.
2. The proposed method requires multi-stage training and is not training-free like CoT.
3. The proposed method is only evaluated on GPT-2, and it is unclear whether it can be applied to larger LLMs.

## Questions
1. Why does the proposed method underperform the CoT baselines on math reasoning tasks? Is it because the method is not suitable for math reasoning tasks or because the method is not well-trained due to the complexity of the tasks?
2. Is the method applicable to larger LLMs such as LLaMA? If so, what is the performance of the proposed method on LLaMA?
3. Is it possible to make the method training-free like CoT? If not, how much additional training cost does the method incur compared to CoT?

## Flag For Ethics Review
No ethics review needed.

## Details Of Ethics Concerns


## Rating
6

## Confidence
4