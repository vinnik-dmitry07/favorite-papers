# Review

## Summary
This paper proposes a new method, ConSPO, to address two limitations found in the widely used reinforcement learning with verifiable rewards (RLVR) method, Group Relative Policy Optimization (GRPO). The first limitation is that GRPO optimizes the clipped ratio-based scores rather than the generation likelihood. The second limitation is that GRPO assigns the same coefficient to all positive rollouts in a group and another coefficient to all negative rollouts. To address these issues, ConSPO utilizes a group-wise InfoNCE-style objective and a curriculum-scheduled margin. The experimental results show that ConSPO outperforms other RLVR baselines on seven challenging mathematical reasoning benchmarks.

## Soundness
3

## Presentation
3

## Contribution
3

## Strengths
1. The paper is well-structured and easy to follow.
2. The authors provide a detailed analysis of the limitations of the widely used GRPO method.
3. The proposed method, ConSPO, is well-motivated by the analysis of GRPO.
4. The experimental results show that ConSPO outperforms other RLVR baselines on seven challenging mathematical reasoning benchmarks.

## Weaknesses
1. The paper does not provide a detailed analysis of the computational complexity of ConSPO. It would be helpful to compare the computational requirements of ConSPO with those of the other RLVR methods.
2. The paper does not provide a detailed analysis of the sensitivity of ConSPO to the choice of hyperparameters, such as the target margin and margin warmup ratio. It would be helpful to provide guidelines for selecting these hyperparameters for different models and datasets.
3. The paper does not provide a detailed analysis of the limitations of ConSPO. It would be helpful to discuss any potential drawbacks or scenarios where ConSPO may not perform well.

## Questions
1. How does the computational complexity of ConSPO compare to other RLVR methods?
2. What are the guidelines for selecting the target margin and margin warmup ratio for different models and datasets?
3. What are the limitations of ConSPO, and are there scenarios where it may not perform well?

## Flag For Ethics Review
No ethics review needed.

## Details Of Ethics Concerns


## Rating
6

## Confidence
4