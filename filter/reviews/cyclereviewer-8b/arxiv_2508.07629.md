## Reviewer

### Summary

This paper presents Klear-Reasoner, a model with advanced reasoning capabilities. The authors conduct a comprehensive analysis of the reasoning model, including data preparation, long chain-of-thought supervised fine-tuning, and reinforcement learning. They also introduce a new clipping policy optimization technique called GPPO that addresses the limitations of traditional clipping methods. The results show that Klear-Reasoner outperforms existing models on various benchmarks.

### Soundness

3 good

### Presentation

3 good

### Contribution

3 good

### Strengths

- The paper is well-written and easy to follow.
- The authors conduct a thorough analysis of the reasoning model and identify key issues with current clipping mechanisms in RL.
- The proposed GPPO technique is innovative and addresses the limitations of traditional clipping methods.
- The experimental results show that Klear-Reasoner outperforms existing models on various benchmarks.

### Weaknesses

- The paper focuses on a specific problem of clipping in RL, which may limit its generalizability to other areas of research.
- The paper does not provide a detailed comparison with other state-of-the-art models, making it difficult to evaluate the effectiveness of the proposed method.
- The paper does not discuss potential limitations or drawbacks of the proposed method.

### Questions

- How does GPPO compare to other existing methods for addressing the limitations of traditional clipping in RL?
- What are the potential limitations or drawbacks of the proposed method?
- How does the proposed method generalize to other areas of research beyond reasoning and RL?

### Flag For Ethics Review

No ethics review needed.

### Rating

6: marginally above the acceptance threshold

### Confidence

3: You are fairly confident in your assessment. It is possible that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work. Math/other details were not carefully checked.

**********

## Reviewer

### Summary

This paper proposes a new RL training method for reasoning models. The method is based on the observation that the clipping in PPO can suppress the gradient of high-entropy tokens, which are important for exploration. The proposed method, GPPO, preserves the gradient of the high-entropy tokens. The experiments show that the proposed method can improve the performance of reasoning models.

### Soundness

3 good

### Presentation

3 good

### Contribution

2 fair

### Strengths

The paper is well-written and easy to follow. The proposed method is simple and effective.

### Weaknesses

The paper only compares with Clip-Higher, which is a simple baseline. The proposed method is similar to CISPO, which is a concurrent work. The paper should compare with CISPO and discuss the difference.

### Questions

1. Why does the proposed method perform better than CISPO on AIME2024 and LiveCodeBench V5?
2. What is the difference between the proposed method and CISPO?

### Flag For Ethics Review

No ethics review needed.

### Rating

6: marginally above the acceptance threshold

### Confidence

3: You are fairly confident in your assessment. It is possible that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work. Math/other details were not carefully checked.

**********

## Reviewer

### Summary

This paper proposes Klear-Reasoner, a model with advanced reasoning capabilities. The authors conduct a comprehensive analysis of the reasoning model, including data preparation, long chain-of-thought supervised fine-tuning, and reinforcement learning. They also introduce a new clipping policy optimization technique called GPPO that addresses the limitations of traditional clipping methods. The results show that Klear-Reasoner outperforms existing models on various benchmarks.

### Soundness

3 good

### Presentation

3 good

### Contribution

3 good

### Strengths

1. This paper is well-written and easy to follow.
2. The authors conduct a thorough analysis of the reasoning model and identify key issues with current clipping mechanisms in RL.
3. The proposed GPPO technique is innovative and addresses the limitations of traditional clipping methods.
4. The experimental results show that Klear-Reasoner outperforms existing models on various benchmarks.

### Weaknesses

1. The paper focuses on a specific problem of clipping in RL, which may limit its generalizability to other areas of research.
2. The paper does not provide a detailed comparison with other state-of-the-art models, making it difficult to evaluate the effectiveness of the proposed method.
3. The paper does not discuss potential limitations or drawbacks of the proposed method.

### Questions

1. How does GPPO compare to other existing methods for addressing the limitations of traditional clipping in RL?
2. What are the potential limitations or drawbacks of the proposed method?
3. How does the proposed method generalize to other areas of research beyond reasoning and RL?

### Flag For Ethics Review

No ethics review needed.

### Rating

6: marginally above the acceptance threshold

### Confidence

3: You are fairly confident in your assessment. It is possible that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work. Math/other details were not carefully checked.

**********

## Reviewer

### Summary

This paper presents Klear-Reasoner, a model that can perform long reasoning. The paper first investigates the data preparation and long Chain-of-Thought supervised fine-tuning (CoT SFT) and reinforcement learning (RL) for the reasoning model. The authors also propose a new clipping policy optimization method called Gradient-Preserving Clipping Policy Optimization (GPPO) to address the limitations of traditional clipping methods. The results show that Klear-Reasoner outperforms existing models on various benchmarks.

### Soundness

3 good

### Presentation

3 good

### Contribution

3 good

### Strengths

The paper is well-written and easy to follow. The authors conduct a thorough analysis of the reasoning model and identify key issues with current clipping mechanisms in RL. The proposed GPPO technique is innovative and addresses the limitations of traditional clipping methods. The experimental results show that Klear-Reasoner outperforms existing models on various benchmarks.

### Weaknesses

The paper focuses on a specific problem of clipping in RL, which may limit its generalizability to other areas of research. The paper does not provide a detailed comparison with other state-of-the-art models, making it difficult to evaluate the effectiveness of the proposed method. The paper does not discuss potential limitations or drawbacks of the proposed method.

### Questions

How does GPPO compare to other existing methods for addressing the limitations of traditional clipping in RL?

### Flag For Ethics Review

No ethics review needed.

### Rating

6: marginally above the acceptance threshold

### Confidence

3: You are fairly confident in your assessment. It is possible that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work. Math/other details were not carefully checked.

**********

## Meta Review

This paper proposes a new RL training method for reasoning models. The method is based on the observation that the clipping in PPO can suppress the gradient of high-entropy tokens, which are important for exploration. The proposed method, GPPO, preserves the gradient of the high-entropy tokens. The experiments show that the proposed method can improve the performance of reasoning models.

The paper is well-written and easy to follow. The proposed method is simple and effective. However, the paper only compares with Clip-Higher, which is a simple baseline. The proposed method is similar to CISPO, which is a concurrent work. The paper should compare with CISPO and discuss the difference.

### justification_for_why_not_higher_score

The paper only compares with Clip-Higher, which is a simple baseline. The proposed method is similar to CISPO, which is a concurrent work. The paper should compare with CISPO and discuss the difference.

### justification_for_why_not_lower_score

The paper is well-written and easy to follow. The proposed method is simple and effective.

**********

## Paper Decision

Accept (poster) (poster)