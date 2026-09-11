# Review

## Summary
This paper investigates whether LLMs can improve themselves by using the voting result of their own answers as a reward signal. The authors find that self-rewarding can improve the reasoning performance of LLMs and the quality of feedback for the next RL iteration. However, they also observe that self-rewarding can cause reward hacking, where models learn to maximize the self-reward, leading to performance collapse.

## Soundness
3

## Presentation
3

## Contribution
3

## Strengths
1. The paper is well-written and easy to follow. The authors provide a clear explanation of the self-rewarding method and the experimental setup.
2. The paper provides a thorough analysis of the performance of self-rewarding, including both the improvement in reasoning performance and the quality of feedback for the next RL iteration. The authors also investigate the potential drawbacks of self-rewarding, such as reward hacking and performance collapse.
3. The paper has some interesting findings. For example, the authors find that self-rewarding can improve the quality of feedback for the next RL iteration, which can drive further model improvement.

## Weaknesses
1. The paper does not provide a detailed analysis of the computational cost of self-rewarding. Self-rewarding requires generating multiple answers to a given question, which can increase the computational cost of training. The authors should provide a comparison of the computational cost of self-rewarding with other training methods, such as SFT and DPO.
2. The paper does not provide a detailed analysis of the impact of the number of generations per prompt on the performance of self-rewarding. The authors should provide an ablation study on the number of generations per prompt to investigate its effect on the performance of self-rewarding.
3. The paper does not provide a detailed analysis of the impact of the self-rewarding method on the diversity of model outputs. The authors should provide an analysis of the diversity of model outputs before and after self-rewarding to investigate whether self-rewarding reduces the diversity of model outputs.
4. The paper does not provide a detailed analysis of the impact of self-rewarding on the model's ability to generalize to new tasks. The authors should provide an analysis of the model's generalization ability before and after self-rewarding to investigate whether self-rewarding improves the model's ability to generalize to new tasks.

## Questions
1. Can you provide a more detailed analysis of the computational cost of self-rewarding compared to other training methods, such as SFT and DPO?
2. Can you provide an ablation study on the number of generations per prompt to investigate its effect on the performance of self-rewarding?
3. Can you provide an analysis of the diversity of model outputs before and after self-rewarding to investigate whether self-rewarding reduces the diversity of model outputs?
4. Can you provide an analysis of the model's generalization ability before and after self-rewarding to investigate whether self-rewarding improves the model's ability to generalize to new tasks?

## Flag For Ethics Review
No ethics review needed.

## Details Of Ethics Concerns


## Rating
6

## Confidence
4