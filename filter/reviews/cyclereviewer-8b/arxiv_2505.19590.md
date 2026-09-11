## Reviewer

### Summary

The paper proposes Intuitor, an RLIF method that uses a model’s own confidence—termed self-certainty —as its sole reward signal. The paper shows that Intuitor matches GRPO’s performance on mathematical benchmarks while achieving better generalization to out-of-domain tasks like code generation, without requiring gold solutions or test cases.

### Soundness

2 fair

### Presentation

3 good

### Contribution

2 fair

### Strengths

1. The paper is well-written and easy to follow.
2. The paper is well-motivated and the problem is well-defined.
3. The proposed method is simple and effective.

### Weaknesses

1. The paper lacks novelty. The proposed method is simple and straightforward. The method is similar to the previous work [1] which uses the self-certainty as the reward signal for RLHF. 
2. The paper lacks theoretical analysis. The paper does not provide any theoretical analysis of the proposed method.
3. The paper lacks ablation study. The paper does not provide any ablation study to show the effectiveness of the proposed method.

[1] Kang, J., Li, Y., Li, Y., Li, Y., Chen, L., & Wang, W. (2023, September). Self-certainty: A new intrinsic reward for language models. In Findings of the Association for Computational Linguistics: ACL 2023 (pp. 1933-1944).

### Questions

1. How does the proposed method compare to the previous work [1] which uses the self-certainty as the reward signal for RLHF?
2. What are the advantages of the proposed method compared to the previous work [1]?
3. How does the proposed method compare to other intrinsic reward methods such as entropy or perplexity?
4. What are the advantages of the proposed method compared to other intrinsic reward methods?
5. How does the proposed method compare to other RL methods such as PPO or TRPO?
6. What are the advantages of the proposed method compared to other RL methods?

### Flag For Ethics Review

No ethics review needed.

### Rating

3: reject, not good enough

### Confidence

3: You are fairly confident in your assessment. It is possible that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work. Math/other details were not carefully checked.

**********

## Reviewer

### Summary

This paper proposes a new method called Intuitor, which uses self-certainty as the reward signal to train language models. The experiments show that Intuitor performs better than GRPO on code generation tasks.

### Soundness

2 fair

### Presentation

3 good

### Contribution

2 fair

### Strengths

1. The paper is well-written and easy to follow.
2. The proposed method is simple and effective.

### Weaknesses

1. The proposed method is a simple application of self-certainty to RLVR, which is not a significant contribution.
2. The experiments are not sufficient to show the effectiveness of the proposed method. For example, the authors should compare the proposed method with other RL methods, such as PPO and TRPO.

### Questions

1. The authors should compare the proposed method with other RL methods, such as PPO and TRPO.
2. The authors should compare the proposed method with other intrinsic reward methods, such as entropy and perplexity.
3. The authors should provide more ablation studies to show the effectiveness of the proposed method.

### Flag For Ethics Review

No ethics review needed.

### Rating

3: reject, not good enough

### Confidence

4: You are confident in your assessment, but not absolutely certain. It is unlikely, but not impossible, that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work.

**********

## Reviewer

### Summary

The paper introduces a new paradigm for training large language models (LLMs) called Reinforcement Learning from Internal Feedback (RLIF). RLIF enables LLMs to improve their reasoning skills by leveraging intrinsic, self-generated signals, without relying on external supervision or labeled data. The paper also proposes Intuitor, an RLIF-based method that utilizes a model's own internal confidence measure, termed self-certainty, as the sole intrinsic reward. The authors demonstrate that Intuitor matches supervised RL performance on in-domain tasks and achieves competitive, sometimes better out-of-domain generalization. They also uncover emergent structured reasoning and enhanced instruction-following capabilities induced by intrinsic rewards.

### Soundness

3 good

### Presentation

3 good

### Contribution

3 good

### Strengths

The paper presents a novel approach to training LLMs, Reinforcement Learning from Internal Feedback (RLIF), which enables LLMs to improve their reasoning skills by leveraging intrinsic, self-generated signals, without relying on external supervision or labeled data. This approach is a significant contribution to the field of LLM training and has the potential to improve the performance of LLMs in various tasks.

The paper also introduces Intuitor, an RLIF-based method that utilizes a model's own internal confidence measure, termed self-certainty, as the sole intrinsic reward. This approach is simple, efficient, and effective, and it eliminates the need for external supervision or handcrafted rewards.

The paper demonstrates that Intuitor matches supervised RL performance on in-domain tasks and achieves competitive, sometimes better out-of-domain generalization. This suggests that RLIF and Intuitor can be used to improve the performance of LLMs in a wide range of tasks, without the need for extensive human annotation or domain-specific supervision.

### Weaknesses

The paper does not provide a detailed explanation of the RLIF paradigm and how it differs from other approaches to training LLMs. While the paper mentions that RLIF uses intrinsic, self-generated signals, it does not provide a clear explanation of what these signals are and how they are generated. Additionally, the paper does not provide a detailed explanation of how RLIF is implemented in the Intuitor method.

The paper does not provide a detailed explanation of the self-certainty metric used in the Intuitor method. While the paper mentions that self-certainty is a measure of a model's internal confidence, it does not provide a clear explanation of how this measure is calculated and why it is useful for training LLMs.

The paper does not provide a detailed explanation of the experimental setup and the results obtained. While the paper mentions that Intuitor matches supervised RL performance on in-domain tasks and achieves competitive, sometimes better out-of-domain generalization, it does not provide a detailed explanation of the specific tasks used in the experiments and the results obtained on these tasks.

### Questions

1. How does RLIF differ from other approaches to training LLMs, such as RLHF and RLVR?
2. What are the intrinsic, self-generated signals used in RLIF, and how are they generated?
3. How is self-certainty calculated, and why is it useful for training LLMs?
4. What are the specific tasks used in the experiments, and what are the results obtained on these tasks?
5. How does Intuitor compare to other methods for training LLMs, such as RLHF and RLVR?

### Flag For Ethics Review

No ethics review needed.

### Rating

5: marginally below the acceptance threshold

### Confidence

3: You are fairly confident in your assessment. It is possible that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work. Math/other details were not carefully checked.

**********

## Reviewer

### Summary

The paper proposes a new method called Intuitor, which uses self-certainty as the reward signal to train language models. The experiments show that Intuitor performs better than GRPO on code generation tasks.

### Soundness

3 good

### Presentation

3 good

### Contribution

2 fair

### Strengths

1. The paper is well-written and easy to follow.
2. The proposed method is simple and effective.
3. The paper provides a detailed analysis of the experimental results.

### Weaknesses

1. The paper lacks novelty. The proposed method is similar to the previous work [1] which uses the self-certainty as the reward signal for RLHF.
2. The paper lacks theoretical analysis. The paper does not provide any theoretical analysis of the proposed method.
3. The paper lacks ablation study. The paper does not provide any ablation study to show the effectiveness of the proposed method.

[1] Kang, J., Li, Y., Li, Y., Li, Y., Chen, L., & Wang, W. (2023, September). Self-certainty: A new intrinsic reward for language models. In Findings of the Association for Computational Linguistics: ACL 2023 (pp. 1933-1944).

### Questions

1. How does the proposed method compare to the previous work [1] which uses the self-certainty as the reward signal for RLHF?
2. What are the advantages of the proposed method compared to the previous work [1]?
3. How does the proposed method compare to other intrinsic reward methods such as entropy or perplexity?
4. What are the advantages of the proposed method compared to other intrinsic reward methods?
5. How does the proposed method compare to other RL methods such as PPO or TRPO?
6. What are the advantages of the proposed method compared to other RL methods?

### Flag For Ethics Review

No ethics review needed.

### Rating

5: marginally below the acceptance threshold

### Confidence

3: You are fairly confident in your assessment. It is possible that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work. Math/other details were not carefully checked.

**********

## Meta Review

This paper introduces Intuitor, a method for training large language models using self-certainty as the reward signal. The paper is well-written and easy to follow. The proposed method is simple and effective. The paper provides a detailed analysis of the experimental results. However, the paper lacks novelty and theoretical analysis. The paper also lacks ablation studies to show the effectiveness of the proposed method. Overall, the paper is not ready for publication at ICLR.

### justification_for_why_not_higher_score

The paper lacks novelty and theoretical analysis. The paper also lacks ablation studies to show the effectiveness of the proposed method.

### justification_for_why_not_lower_score

N/A

**********

## Paper Decision

Reject (not selected for publication for ICLR 2024)