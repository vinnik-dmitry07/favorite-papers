# Review

## Summary
This paper proposes a new RL algorithm for LLMs, DAPO, and open-sources a state-of-the-art large-scale RL system. The key techniques introduced in DAPO are 1) Clip-Higher to avoid entropy collapse; 2) Dynamic Sampling to improve training efficiency and stability; 3) Token-Level Policy Gradient Loss to improve long-CoT RL; 4) Overlong Reward Shaping to reduce reward noise and stabilize training. The proposed system achieves 50 points on AIME 2024 using Qwen2.5-32B, outperforming previous state-of-the-art results achieved by DeepSeek-R1-Zero-Qwen-32B (47 points) using 50% training steps.

## Soundness
3

## Presentation
3

## Contribution
3

## Strengths
1. The paper is well-written and easy to follow.
2. The proposed method is simple and effective, and the authors open-source the code and data.
3. The results are impressive, achieving 50 points on AIME 2024 using Qwen2.5-32B.

## Weaknesses
1. The authors do not provide a detailed analysis of the computational resources required for training, such as the number of GPUs and the total training FLOPs.
2. The authors do not provide a detailed analysis of the impact of different hyperparameters, such as the number of samples G, the clipping parameters $\epsilon_{low}$ and $\epsilon_{high}$, and the length $L_{max}$ in Overlong Reward Shaping.

## Questions
1. What is the impact of the number of samples G on the performance of DAPO? Is there an optimal G value?
2. How does the computational cost of DAPO compare to other RL algorithms for LLMs, such as PPO and GRPO? 
3. How does the performance of DAPO scale with the size of the LLM? Does it show better scalability than other RL algorithms for LLMs?

## Flag For Ethics Review
No ethics review needed.

## Details Of Ethics Concerns


## Rating
6

## Confidence
4