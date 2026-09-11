## Reviewer

### Summary

This paper studies the role of token entropy in the context of RLHF for reasoning. The authors first show that only a small fraction of tokens in the CoT have high entropy, and that these high-entropy tokens are crucial for reasoning. They then show that RLVR primarily updates the entropy of these high-entropy tokens, while the entropy of low-entropy tokens remains relatively stable. Finally, they show that training on only the high-entropy tokens can achieve comparable performance to training on all tokens.

### Soundness

3 good

### Presentation

3 good

### Contribution

2 fair

### Strengths

The paper is well-written and easy to follow. The idea of focusing on high-entropy tokens in RLHF is interesting and intuitive.

### Weaknesses

The main weakness of the paper is that the results are not very surprising and do not seem to have a significant impact on the field. The paper is essentially showing that high-entropy tokens are important for reasoning, which is already known. The paper also shows that training on high-entropy tokens can achieve comparable performance to training on all tokens, but this is not surprising since high-entropy tokens are the ones that contribute the most to the model's performance.

### Questions

- The paper mentions that the entropy of low-entropy tokens remains relatively stable during RLVR. However, it would be interesting to see how the entropy of low-entropy tokens changes during RLVR. Do they remain stable throughout the training process, or do they increase/decrease over time?
- The paper mentions that training on high-entropy tokens can achieve comparable performance to training on all tokens. However, it would be interesting to see how the performance of training on low-entropy tokens compares to training on all tokens. Do low-entropy tokens contribute negatively to the model's performance, or do they not contribute much to the model's performance?

### Flag For Ethics Review

No ethics review needed.

### Rating

5: marginally below the acceptance threshold

### Confidence

4: You are confident in your assessment, but not absolutely certain. It is unlikely, but not impossible, that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work.

**********

## Reviewer

### Summary

This paper investigates the relationship between token entropy and the performance of Reinforcement Learning with Verifiable Rewards (RLVR) for reasoning. The authors analyze the entropy patterns in Chain-of-Thought (CoT) reasoning and find that only a small fraction of tokens exhibit high entropy, acting as critical forks guiding the model towards diverse reasoning pathways. They also observe that RLVR primarily adjusts the entropy of high-entropy tokens, while the entropy of low-entropy tokens remains relatively stable. Based on these findings, the authors propose a novel approach that restricts policy gradient updates to the top 20% highest-entropy tokens, achieving performance comparable to or surpassing full-token RLVR training. The paper highlights the significance of high-entropy minority tokens in RLVR and provides insights into optimizing RLVR by leveraging these tokens to improve LLM reasoning capabilities.

### Soundness

3 good

### Presentation

3 good

### Contribution

3 good

### Strengths

1. The paper is well-written and easy to follow.
2. The authors provide a comprehensive analysis of token entropy patterns in CoT reasoning and RLVR training, offering valuable insights into the mechanisms of reasoning in LLMs.
3. The proposed approach of focusing on high-entropy tokens for RLVR training is novel and effective, achieving comparable or better performance compared to full-token RLVR training.
4. The paper highlights the importance of high-entropy minority tokens in RLVR, providing a new perspective on optimizing RLVR for improved LLM reasoning capabilities.

### Weaknesses

1. The paper only focuses on Qwen3 models, which may limit the generalizability of the findings to other LLMs.
2. The paper does not provide a detailed analysis of the impact of entropy on the performance of RLVR, which could be an interesting direction for future research.
3. The paper does not discuss the potential limitations of the proposed approach, such as the potential for overfitting to high-entropy tokens.
4. The paper does not provide a detailed analysis of the computational cost of the proposed approach compared to full-token RLVR training.

### Questions

1. How do you think the findings of this paper can be generalized to other LLMs beyond Qwen3 models?
2. Can you provide a more detailed analysis of the impact of entropy on the performance of RLVR?
3. What are the potential limitations of the proposed approach, and how can they be addressed?
4. Can you provide a detailed analysis of the computational cost of the proposed approach compared to full-token RLVR training?

### Flag For Ethics Review

No ethics review needed.

### Rating

5: marginally below the acceptance threshold

### Confidence

3: You are fairly confident in your assessment. It is possible that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work. Math/other details were not carefully checked.

**********

## Reviewer

### Summary

This paper studies the impact of token entropy in reinforcement learning with verifiable rewards (RLVR). The authors find that the majority of tokens in Chain-of-Thought (CoT) reasoning have low entropy, while a small fraction of tokens have high entropy. These high-entropy tokens act as "forks" in the reasoning process, guiding the model towards diverse reasoning paths. The authors also find that RLVR primarily updates the entropy of high-entropy tokens, while the entropy of low-entropy tokens remains relatively stable. Finally, the authors propose a new approach that restricts policy gradient updates to the top 20% highest-entropy tokens, achieving comparable or better performance compared to full-token RLVR training.

### Soundness

3 good

### Presentation

3 good

### Contribution

3 good

### Strengths

- The paper provides a comprehensive analysis of token entropy patterns in CoT reasoning and RLVR training, offering valuable insights into the mechanisms of reasoning in LLMs.
- The proposed approach of focusing on high-entropy tokens for RLVR training is novel and effective, achieving comparable or better performance compared to full-token RLVR training.
- The paper highlights the importance of high-entropy minority tokens in RLVR, providing a new perspective on optimizing RLVR for improved LLM reasoning capabilities.

### Weaknesses

- The paper only focuses on Qwen3 models, which may limit the generalizability of the findings to other LLMs.
- The paper does not provide a detailed analysis of the impact of entropy on the performance of RLVR, which could be an interesting direction for future research.
- The paper does not discuss the potential limitations of the proposed approach, such as the potential for overfitting to high-entropy tokens.
- The paper does not provide a detailed analysis of the computational cost of the proposed approach compared to full-token RLVR training.

### Questions

- Can the authors provide a more detailed analysis of the impact of entropy on the performance of RLVR?
- Can the authors discuss the potential limitations of the proposed approach and how they can be addressed?
- Can the authors provide a detailed analysis of the computational cost of the proposed approach compared to full-token RLVR training?
- Can the authors provide more details about the experimental setup, including the specific hyperparameters used and the training procedure?

### Flag For Ethics Review

No ethics review needed.

### Rating

5: marginally below the acceptance threshold

### Confidence

3: You are fairly confident in your assessment. It is possible that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work. Math/other details were not carefully checked.

**********

## Reviewer

### Summary

This paper analyzes the role of token entropy in RLVR. The authors first show that high-entropy tokens are more important for reasoning. Then, they show that RLVR primarily updates the entropy of high-entropy tokens. Finally, they show that training on only the high-entropy tokens can achieve comparable performance to training on all tokens.

### Soundness

3 good

### Presentation

3 good

### Contribution

2 fair

### Strengths

1. The paper is well-written and easy to follow.
2. The paper provides interesting insights into the role of token entropy in RLVR.

### Weaknesses

1. The paper is mainly based on the Qwen3 models. It is unclear whether the findings can generalize to other models.
2. The paper only considers the DAPO algorithm. It is unclear whether the findings can generalize to other RL algorithms.
3. The paper does not discuss the limitations of the proposed approach.

### Questions

1. Can the authors provide more details about the experimental setup, including the specific hyperparameters used and the training procedure?
2. Can the authors provide more details about the limitations of the proposed approach?
3. Can the authors provide more details about the generalizability of the findings to other models and RL algorithms?

### Flag For Ethics Review

No ethics review needed.

### Rating

5: marginally below the acceptance threshold

### Confidence

3: You are fairly confident in your assessment. It is possible that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work. Math/other details were not carefully checked.

**********

## Meta Review

The paper investigates the role of token entropy in the context of RLHF for reasoning. The authors first show that only a small fraction of tokens in the CoT have high entropy, and that these high-entropy tokens are crucial for reasoning. They then show that RLVR primarily updates the entropy of these high-entropy tokens, while the entropy of low-entropy tokens remains relatively stable. Finally, they show that training on only the high-entropy tokens can achieve comparable performance to training on all tokens. 

The paper is well-written and easy to follow. The idea of focusing on high-entropy tokens in RLHF is interesting and intuitive. However, the results are not very surprising and do not seem to have a significant impact on the field. The paper is essentially showing that high-entropy tokens are important for reasoning, which is already known. The paper also shows that training on high-entropy tokens can achieve comparable performance to training on all tokens, but this is not surprising since high-entropy tokens are the ones that contribute the most to the model's performance. 

The authors did not provide a response to the reviewers' comments.

### justification_for_why_not_higher_score

The paper is not ready for publication at ICLR.

### justification_for_why_not_lower_score

N/A

**********

## Paper Decision

Reject (not selected for publication for ICLR 2024)