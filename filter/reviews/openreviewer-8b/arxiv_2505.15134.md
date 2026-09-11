# Review

## Summary
This paper proposes to use entropy minimization as a way to improve LLM reasoning. The authors propose three ways to use entropy minimization: fine-tuning with a token-level entropy objective, using entropy as a reward in RL, and using entropy minimization at inference time without any training. The authors find that entropy minimization is able to improve performance on math and coding tasks, sometimes outperforming RL methods that use human-verified labels.

## Soundness
4

## Presentation
4

## Contribution
3

## Strengths
- The paper is well-written and easy to follow. The authors clearly describe the three methods they propose and the results are presented in a clear manner.
- The authors evaluate their methods on a variety of math and coding benchmarks, and show that entropy minimization can be a useful objective for improving reasoning.

## Weaknesses
- The authors only experiment with Qwen-2.5-Math-7B and Eurus-2-7B-SFT. It would be interesting to see if these findings hold for other models, especially larger ones.
- While the authors show that entropy minimization can improve performance on math and coding tasks, it would be interesting to see how it performs on other tasks, such as natural language inference or summarization.

## Questions
- How does the performance of entropy minimization compare to other methods for improving LLM reasoning, such as self-consistency or chain-of-thought?
- How does the performance of entropy minimization scale with model size? Would larger models benefit more from entropy minimization, or are the current results representative of the largest models?

## Flag For Ethics Review
No ethics review needed.

## Details Of Ethics Concerns


## Rating
8

## Confidence
4