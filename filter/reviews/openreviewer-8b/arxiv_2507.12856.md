# Review

## Summary
This paper introduces a novel approach to supervised fine-tuning (SFT) of large language models (LLMs) by framing it as a form of reinforcement learning (RL). The authors propose a method called importance-weighted supervised fine-tuning (iw-SFT), which modifies SFT by incorporating importance sampling to better align with RL objectives. The paper demonstrates that this modification can lead to improved performance compared to standard SFT, particularly when applied to curated or filtered data. The authors evaluate their approach on tasks such as reasoning (AIME 2024, MATH500) and continuous control (D4RL benchmark), showing competitive results with established RL algorithms.

## Soundness
3

## Presentation
3

## Contribution
3

## Strengths
1. The paper provides a theoretical basis for understanding SFT as a form of RL, which is a novel perspective in the field. By drawing a connection between SFT and RL, the authors offer a new lens through which to view post-training optimization of LLMs.

2. The proposed iw-SFT method is well-motivated and theoretically grounded. The authors provide a clear derivation of how their approach can improve upon standard SFT by tightening the bound on the RL objective.

3. The experimental results demonstrate the effectiveness of the proposed method, particularly in reasoning tasks. The paper reports improvements over standard SFT on the AIME 2024 dataset and achieves competitive performance with established RL algorithms on continuous control tasks.

## Weaknesses
1. The paper does not provide a comprehensive comparison with other recent methods in LLM post-training, such as DPO or other RL-based approaches. A more extensive comparison would help to contextualize the contributions of this work.

2. The experimental evaluation is limited to a relatively small set of tasks. The paper would benefit from a more extensive evaluation across a wider range of tasks to demonstrate the generalizability of the proposed method.

3. The paper does not provide a detailed analysis of the computational requirements of the proposed method compared to standard SFT and other RL approaches. A comparison of computational costs would be valuable for assessing the practicality of the approach.

## Questions
1. How does the proposed method compare to other recent approaches in LLM post-training, such as DPO or other RL-based methods? A more comprehensive comparison would help to better position this work in the context of existing methods.

2. Can the authors provide a more extensive evaluation of the proposed method across a wider range of tasks to demonstrate its generalizability? The current experimental evaluation is limited to a relatively small set of tasks.

3. What are the computational requirements of the proposed method compared to standard SFT and other RL approaches? A comparison of computational costs would be valuable for assessing the practicality of the approach.

## Flag For Ethics Review
No ethics review needed.

## Details Of Ethics Concerns


## Rating
6

## Confidence
4