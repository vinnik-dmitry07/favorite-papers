# Review

## Summary
This paper proposes Intuitor, a method that utilizes the self-certainty of LLM as the reward signal for reinforcement learning. The authors replace the advantage term in GRPO with self-certainty and demonstrate the effectiveness of this method through experiments on mathematical reasoning and code generation tasks.

## Soundness
3

## Presentation
3

## Contribution
2

## Strengths
1. The paper is well-written and easy to understand.
2. The authors demonstrate the effectiveness of self-certainty as a reward signal through experiments on multiple datasets and models.

## Weaknesses
1. The novelty of the paper is limited. The method proposed by the authors is essentially the same as GRPO, with the only difference being that the advantage term in GRPO is replaced by self-certainty. However, the use of self-certainty as a reward signal has already been proposed in the work [1], and the authors do not cite this previous work.
2. The authors claim that Intuitor can generalize to out-of-domain tasks, but the experiments only demonstrate generalization to code generation tasks from mathematical reasoning tasks. This is not sufficient to substantiate the claim of out-of-domain generalization. Additionally, the authors do not provide any experimental results for the code reasoning task on the GSM8K dataset.
3. The authors do not provide any experimental results on the MMLU dataset.

[1] Self-Rewarding Language Models. arXiv 2024.

## Questions
1. Why is it necessary to use the average KL divergence between the model’s output distribution and a uniform distribution as the measure of self-certainty? Can other metrics, such as entropy, be used instead?
2. In Table 1, why is there no comparison with the results of Intuitor on the MMLU dataset?

## Flag For Ethics Review
No ethics review needed.

## Details Of Ethics Concerns


## Rating
5

## Confidence
4