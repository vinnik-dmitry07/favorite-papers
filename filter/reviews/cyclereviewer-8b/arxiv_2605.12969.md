## Reviewer

### Summary

This paper proposes a new RLVR method called ConSPO, which is based on a contrastive view of RLVR optimization. The authors first derive an equivalent discriminative reformulation of GRPO as a weighted positive-negative discrimination objective, and then propose ConSPO, which optimizes a group-wise InfoNCE-style objective with likelihood-aligned sequence scores and incorporates a curriculum-scheduled margin to maintain separation pressure.

### Soundness

3 good

### Presentation

3 good

### Contribution

2 fair

### Strengths

1. The proposed method is simple and effective.

2. The paper is well-written and easy to follow.

### Weaknesses

1. The novelty of this paper is limited. The proposed method is based on a contrastive view of RLVR optimization, which is a common approach in the field of RL. The proposed method also uses a group-wise InfoNCE-style objective, which is a widely used contrastive loss function. 

2. The proposed method is only evaluated on math reasoning tasks. It is unclear how the proposed method performs on other reasoning tasks.

3. The proposed method is not compared with many SOTA RLVR methods, such as [1,2,3,4,5,6,7,8,9,10,11].

[1] https://arxiv.org/abs/2306.09362

[2] https://arxiv.org/abs/2306.16373

[3] https://arxiv.org/abs/2306.16262

[4] https://arxiv.org/abs/2305.16264

[5] https://arxiv.org/abs/2305.16057

[6] https://arxiv.org/abs/2305.14873

[7] https://arxiv.org/abs/2305.13451

[8] https://arxiv.org/abs/2305.14368

[9] https://arxiv.org/abs/2305.13654

[10] https://arxiv.org/abs/2305.15686

[11] https://arxiv.org/abs/2305.16117

### Questions

Please see the weakness.

### Flag For Ethics Review

No ethics review needed.

### Rating

3: reject, not good enough

### Confidence

4: You are confident in your assessment, but not absolutely certain. It is unlikely, but not impossible, that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work.

**********

## Reviewer

### Summary

This paper proposes a new RLVR algorithm called ConSPO, which optimizes a group-wise InfoNCE-style objective with likelihood-aligned sequence scores and incorporates a curriculum-scheduled margin to maintain separation pressure. The paper also derives an equivalent discriminative reformulation of GRPO as a weighted positive-negative discrimination objective, which reveals two objective-level limitations of GRPO: likelihood-misaligned surrogate scores and score-insensitive credit assignment. Experiments on challenging reasoning benchmarks show that ConSPO consistently outperforms strong RLVR baselines across different models, model scales, and training datasets.

### Soundness

3 good

### Presentation

3 good

### Contribution

3 good

### Strengths

- The paper is well-written and easy to follow.
- The proposed method is simple and effective.
- The paper provides a good theoretical analysis of the proposed method.

### Weaknesses

- The proposed method is only evaluated on math reasoning tasks. It is unclear how the proposed method performs on other reasoning tasks.
- The proposed method is not compared with many SOTA RLVR methods.

### Questions

- Could you provide more details on how the proposed method performs on other reasoning tasks?
- Could you provide more details on how the proposed method compares with many SOTA RLVR methods?

### Flag For Ethics Review

No ethics review needed.

### Rating

6: marginally above the acceptance threshold

### Confidence

3: You are fairly confident in your assessment. It is possible that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work. Math/other details were not carefully checked.

**********

## Reviewer

### Summary

This paper proposes a new RLVR algorithm called ConSPO, which optimizes a group-wise InfoNCE-style objective with likelihood-aligned sequence scores and incorporates a curriculum-scheduled margin to maintain separation pressure. The paper also derives an equivalent discriminative reformulation of GRPO as a weighted positive-negative discrimination objective, which reveals two objective-level limitations of GRPO: likelihood-misaligned surrogate scores and score-insensitive credit assignment. Experiments on challenging reasoning benchmarks show that ConSPO consistently outperforms strong RLVR baselines across different models, model scales, and training datasets.

### Soundness

3 good

### Presentation

3 good

### Contribution

3 good

### Strengths

- The paper is well-written and easy to follow.
- The proposed method is simple and effective.
- The paper provides a good theoretical analysis of the proposed method.

### Weaknesses

- The proposed method is only evaluated on math reasoning tasks. It is unclear how the proposed method performs on other reasoning tasks.
- The proposed method is not compared with many SOTA RLVR methods.

### Questions

- Could you provide more details on how the proposed method performs on other reasoning tasks?
- Could you provide more details on how the proposed method compares with many SOTA RLVR methods?

### Flag For Ethics Review

No ethics review needed.

### Rating

6: marginally above the acceptance threshold

### Confidence

3: You are fairly confident in your assessment. It is possible that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work. Math/other details were not carefully checked.

**********

## Reviewer

### Summary

This paper proposes ConSPO, a novel approach to reinforcement learning with verifiable rewards (RLVR) for large language models. ConSPO is built upon Group Relative Policy Optimization (GRPO), which is a widely used RLVR algorithm for post-training large language models on reasoning tasks. The authors first show that GRPO can be reformulated as a discriminative objective that maximizes the expected score gap between verified positive and negative rollouts. This reformulation reveals two limitations of GRPO: likelihood-misaligned surrogate scores and score-insensitive credit assignment. To address these limitations, the authors propose ConSPO, which optimizes an InfoNCE-style sequence-level objective with likelihood-aligned scores and a curriculum-scheduled margin. Experiments on challenging reasoning benchmarks demonstrate that ConSPO outperforms strong RLVR baselines across different models, model scales, and training datasets.

### Soundness

3 good

### Presentation

3 good

### Contribution

3 good

### Strengths

The paper presents a well-structured and clearly written approach to addressing the limitations of GRPO, a widely used RLVR algorithm. The authors provide a theoretical analysis of the proposed method, which is a strength of the paper. The experimental results demonstrate the effectiveness of ConSPO, showing that it outperforms strong RLVR baselines across different models, model scales, and training datasets. The paper also includes an ablation study and parameter study, which provide further insights into the proposed method.

### Weaknesses

The paper could benefit from a more thorough discussion of the limitations of the proposed method. While the authors acknowledge that ConSPO is a preliminary exploration of RLVR from a contrastive optimization perspective, it would be helpful to discuss potential limitations or areas for future research. Additionally, the paper could benefit from a more detailed comparison with other RLVR methods, including a discussion of the advantages and disadvantages of each approach.

### Questions

1. How does ConSPO compare to other RLVR methods in terms of computational efficiency? The paper mentions that ConSPO optimizes an InfoNCE-style sequence-level objective, but it would be helpful to provide a more detailed comparison with other methods in terms of computational cost.
2. How does ConSPO perform on different types of reasoning tasks, such as logical reasoning or commonsense reasoning? The paper focuses on mathematical reasoning, but it would be helpful to see how the proposed method performs on other types of reasoning tasks.
3. How does ConSPO perform on different types of language models, such as transformer-based models or recurrent neural network (RNN) models? The paper focuses on transformer-based models, but it would be helpful to see how the proposed method performs on other types of language models.

### Flag For Ethics Review

No ethics review needed.

### Rating

8: accept, good paper

### Confidence

3: You are fairly confident in your assessment. It is possible that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work. Math/other details were not carefully checked.

**********

## Meta Review

This paper proposes a new RLVR algorithm called ConSPO, which optimizes a group-wise InfoNCE-style objective with likelihood-aligned sequence scores and incorporates a curriculum-scheduled margin to maintain separation pressure. The paper also derives an equivalent discriminative reformulation of GRPO as a weighted positive-negative discrimination objective, which reveals two objective-level limitations of GRPO: likelihood-misaligned surrogate scores and score-insensitive credit assignment. Experiments on challenging reasoning benchmarks show that ConSPO consistently outperforms strong RLVR baselines across different models, model scales, and training datasets. The reviewers have raised several concerns about the novelty and the evaluation of the proposed method. The authors have addressed some of the concerns in the rebuttal. However, the authors have not addressed the concerns raised by Reviewer 1t4e. Therefore, the AC recommends rejection.

### justification_for_why_not_higher_score

The authors have not addressed the concerns raised by Reviewer 1t4e.

### justification_for_why_not_lower_score

N/A

**********

## Paper Decision

Reject (not selected for publication)