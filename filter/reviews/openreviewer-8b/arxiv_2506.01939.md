# Review

## Summary
This paper investigates Reinforcement Learning with Verifiable Rewards (RLVR) for improving the reasoning capabilities of large language models (LLMs). The authors analyze the entropy patterns of tokens in Chain-of-Thought (CoT) reasoning and find that only a small subset of high-entropy "forking" tokens significantly influence reasoning paths. During RLVR training, they observe that these high-entropy tokens remain the main focus of adjustments, while low-entropy tokens show minimal change. By focusing only on these high-entropy tokens during RLVR, they achieve comparable or better performance than full-gradient updates, especially on larger models, highlighting the importance of these tokens for effective reasoning.

## Soundness
3

## Presentation
3

## Contribution
3

## Strengths
- The paper introduces a novel perspective on RLVR by analyzing token entropy patterns, identifying high-entropy "forking" tokens as crucial for reasoning.
- The authors provide a thorough analysis of token entropy in CoT reasoning and how it evolves during RLVR training, offering valuable insights into the mechanisms behind LLM reasoning.
- The proposed approach of focusing only on high-entropy tokens in RLVR leads to performance improvements, especially on larger models, showcasing the potential for more efficient training.
- The paper includes detailed experiments and ablation studies that validate the findings and explore the impact of different entropy thresholds and token ratios.

## Weaknesses
- The experiments are primarily conducted on Qwen models, and the findings might not generalize to other architectures or diverse reasoning tasks.
- The approach relies on manually set entropy thresholds and ratios, which might require tuning for different models and tasks.
- The paper could benefit from more extensive testing on a broader range of reasoning domains beyond mathematics, such as programming or complex reasoning tasks.
- The approach may not be suitable for all RLVR scenarios, and the optimal entropy threshold may vary, requiring additional calibration.

## Questions
- Have you tested the method on other LLM architectures beyond Qwen? If so, how did the results compare?
- How sensitive is the method to the choice of entropy threshold? Is there a way to automatically determine the optimal threshold?
- Can you provide more insights into why focusing on high-entropy tokens seems to improve generalization compared to SFT?
- How do you explain the initial performance drop in Figure 6 when using only forking tokens on Qwen3-8B?
- Have you explored the potential of combining this approach with other RL techniques, such as entropy bonuses or KL penalties?
- How does the method perform on more complex reasoning tasks, such as the ARC AGI benchmark or other non-mathematical reasoning tasks?
- Can you provide more details on the potential impact of longer context lengths on the performance of your approach?

## Flag For Ethics Review
No ethics review needed.

## Details Of Ethics Concerns


## Rating
6

## Confidence
4