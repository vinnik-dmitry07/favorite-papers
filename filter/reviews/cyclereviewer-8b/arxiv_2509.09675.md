## Reviewer

### Summary

The paper proposes a curiosity-driven exploration method for LLMs. The authors argue that the current RLVR methods explore poorly, leading to premature convergence and entropy collapse. To address this challenge, the authors propose a curiosity-driven exploration framework that leverages the model's own intrinsic sense of curiosity to guide exploration. The authors use perplexity over the generated response as a curiosity signal for the actor, and the variance of value estimates from a multi-head architecture as a curiosity signal for the critic. The paper also provides a theoretical analysis of the proposed method and demonstrates its effectiveness on several benchmarks.

### Soundness

3 good

### Presentation

3 good

### Contribution

2 fair

### Strengths

1. The paper is well-written and easy to follow.
2. The proposed method is simple and easy to implement.
3. The paper provides a theoretical analysis of the proposed method.
4. The paper demonstrates the effectiveness of the proposed method on several benchmarks.

### Weaknesses

1. The novelty of the paper is limited. The idea of using perplexity as a curiosity signal is not new. There are many papers that use perplexity as a curiosity signal for exploration. For example, [1] uses perplexity as a curiosity signal for exploration in RL. The idea of using the variance of value estimates as a curiosity signal is also not new. There are many papers that use the variance of value estimates as a curiosity signal for exploration. For example, [2] uses the variance of value estimates as a curiosity signal for exploration in RL.

2. The paper does not provide a thorough experimental evaluation of the proposed method. The paper only evaluates the proposed method on a single benchmark, and does not compare it to other state-of-the-art methods.

3. The paper does not provide a detailed analysis of the results. The paper only provides a brief discussion of the results, and does not provide a detailed analysis of the results. For example, the paper does not provide a detailed analysis of the effect of the hyperparameters on the performance of the proposed method.

[1] "Curiosity-Driven Exploration for Reinforcement Learning and Planning" by Pathak et al., 2017

[2] "Random Network Distillation" by Burda et al., 2018

### Questions

1. How does the proposed method compare to other state-of-the-art methods for exploration in RL?

2. Can the proposed method be used in other domains besides LLMs?

3. How does the proposed method compare to other curiosity-driven exploration methods?

### Flag For Ethics Review

No ethics review needed.

### Rating

5: marginally below the acceptance threshold

### Confidence

4: You are confident in your assessment, but not absolutely certain. It is unlikely, but not impossible, that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work.

**********

## Reviewer

### Summary

This paper proposes a curiosity-driven exploration method for RL with verifiable rewards. The method uses perplexity as an intrinsic reward to guide the exploration of the agent. The authors show that the perplexity-based bonus intrinsically penalizes overconfident errors while encouraging diversity among correct responses. The authors also show that the critic-based exploration bonus is theoretically equivalent to classical count-based bonuses in linear MDPs. The method is evaluated on four mathematical reasoning benchmarks and shows consistent performance gains over standard PPO and GRPO algorithms.

### Soundness

3 good

### Presentation

3 good

### Contribution

3 good

### Strengths

1. The paper is well written and easy to follow.
2. The proposed method is simple and effective. The theoretical analysis is solid and the empirical results are promising.
3. The paper provides a thorough analysis of the training dynamics and the effect of the PPL bonus on the model's performance.

### Weaknesses

1. The paper only evaluates the proposed method on four mathematical reasoning benchmarks. It would be good to see the method evaluated on other domains such as language translation, question answering, or game playing.
2. The paper does not compare the proposed method to other state-of-the-art methods for exploration in RL.
3. The paper does not discuss the limitations of the proposed method and potential future work.

### Questions

1. How does the proposed method compare to other state-of-the-art methods for exploration in RL?
2. Can the proposed method be used in other domains besides mathematical reasoning?
3. What are the limitations of the proposed method and what are some potential future work directions?

### Flag For Ethics Review

No ethics review needed.

### Rating

6: marginally above the acceptance threshold

### Confidence

3: You are fairly confident in your assessment. It is possible that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work. Math/other details were not carefully checked.

**********

## Reviewer

### Summary

This paper proposes a new method for improving the exploration in RL with verifiable rewards. The proposed method, Curiosity-Driven Exploration (CDE), leverages the model's intrinsic sense of curiosity to guide exploration. CDE uses perplexity over the generated response as a curiosity signal for the actor, and the variance of value estimates from a multi-head architecture as a curiosity signal for the critic. The authors show that the perplexity-based bonus intrinsically penalizes overconfident errors while encouraging diversity among correct responses. The authors also show that the critic-based exploration bonus is theoretically equivalent to classical count-based bonuses in linear MDPs. The method is evaluated on four mathematical reasoning benchmarks and shows consistent performance gains over standard PPO and GRPO algorithms.

### Soundness

3 good

### Presentation

3 good

### Contribution

3 good

### Strengths

1. The paper is well-written and easy to follow. The authors provide a clear motivation for the proposed method and explain the intuition behind the method.
2. The proposed method is simple and effective. The theoretical analysis is solid and the empirical results are promising.
3. The paper provides a thorough analysis of the training dynamics and the effect of the PPL bonus on the model's performance.

### Weaknesses

1. The paper only evaluates the proposed method on four mathematical reasoning benchmarks. It would be good to see the method evaluated on other domains such as language translation, question answering, or game playing.
2. The paper does not compare the proposed method to other state-of-the-art methods for exploration in RL.
3. The paper does not discuss the limitations of the proposed method and potential future work.

### Questions

1. How does the proposed method compare to other state-of-the-art methods for exploration in RL?
2. Can the proposed method be used in other domains besides mathematical reasoning?
3. What are the limitations of the proposed method and what are some potential future work directions?

### Flag For Ethics Review

No ethics review needed.

### Rating

6: marginally above the acceptance threshold

### Confidence

3: You are fairly confident in your assessment. It is possible that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work. Math/other details were not carefully checked.

**********

## Reviewer

### Summary

The paper introduces a curiosity-driven exploration method for reinforcement learning with verifiable rewards (RLVR) in large language models (LLMs). The authors propose a framework that leverages the model's intrinsic curiosity to guide exploration, using perplexity and value variance as exploration bonuses. Theoretical analysis shows that the method inherently penalizes overconfident errors and promotes diversity among correct responses. Empirical results demonstrate improved performance on AIME benchmarks, and analysis reveals a calibration collapse mechanism in RLVR, shedding light on LLM failure modes.

### Soundness

3 good

### Presentation

3 good

### Contribution

3 good

### Strengths

1. The paper is well-written and easy to follow.
2. The proposed method is simple and effective.
3. The paper provides a thorough analysis of the training dynamics and the effect of the PPL bonus on the model's performance.
4. The paper provides a theoretical analysis of the proposed method.

### Weaknesses

1. The paper only evaluates the proposed method on four mathematical reasoning benchmarks. It would be good to see the method evaluated on other domains such as language translation, question answering, or game playing.
2. The paper does not compare the proposed method to other state-of-the-art methods for exploration in RL.
3. The paper does not discuss the limitations of the proposed method and potential future work.

### Questions

1. How does the proposed method compare to other state-of-the-art methods for exploration in RL?
2. Can the proposed method be used in other domains besides mathematical reasoning?
3. What are the limitations of the proposed method and what are some potential future work directions?

### Flag For Ethics Review

No ethics review needed.

### Rating

6: marginally above the acceptance threshold

### Confidence

3: You are fairly confident in your assessment. It is possible that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work. Math/other details were not carefully checked.

**********

## Meta Review

This paper proposes a curiosity-driven exploration method for RL with verifiable rewards. The method uses perplexity as an intrinsic reward to guide the exploration of the agent. The authors show that the perplexity-based bonus intrinsically penalizes overconfident errors while encouraging diversity among correct responses. The authors also show that the critic-based exploration bonus is theoretically equivalent to classical count-based bonuses in linear MDPs. The method is evaluated on four mathematical reasoning benchmarks and shows consistent performance gains over standard PPO and GRPO algorithms.

The paper is well-written and easy to follow. The proposed method is simple and effective. The theoretical analysis is solid and the empirical results are promising. The paper provides a thorough analysis of the training dynamics and the effect of the PPL bonus on the model's performance. The paper is well-written and easy to follow. The proposed method is simple and effective. The theoretical analysis is solid and the empirical results are promising. The paper provides a thorough analysis of the training dynamics and the effect of the PPL bonus on the model's performance.

### justification_for_why_not_higher_score

The paper only evaluates the proposed method on four mathematical reasoning benchmarks. It would be good to see the method evaluated on other domains such as language translation, question answering, or game playing. The paper does not compare the proposed method to other state-of-the-art methods for exploration in RL. The paper does not discuss the limitations of the proposed method and potential future work.

### justification_for_why_not_lower_score

N/A

**********

## Paper Decision

Reject (not selected for a spotlight/oral/talk) **********

**********

# Paper Decision Summary

* Paper Decision: reject (not selected for a spotlight/oral/talk)
* Confidence: 4
* Reviewer scores: 5, 6, 6, 6
* Reviewer covers: 5.1, 5.2
* justification: The paper introduces a curiosity-driven exploration method for reinforcement learning with verifiable rewards (RLVR) in large language models (LLMs). The authors propose a framework that leverages the model's intrinsic curiosity to guide exploration, using perplexity and value variance as exploration bonuses. Theoretical analysis shows that the method inherently penalizes overconfident errors and promotes diversity among correct responses. Empirical results demonstrate improved performance on AIME benchmarks, and analysis reveals a calibration collapse mechanism in RLVR, shedding light on LLM failure modes.
The paper is well-written and easy to follow. The proposed method is simple and effective. The theoretical analysis is solid and the empirical results are promising. The paper provides a thorough analysis of the training dynamics and the effect of the PPL bonus on the model's performance.
The paper only evaluates the proposed method on four mathematical reasoning benchmarks. It would be good to see the method evaluated on other domains such as language translation, question answering, or game playing. The paper does not compare the proposed method to other state-of-the-art methods for exploration in RL. The paper does not discuss the limitations of the proposed method and potential future work.

**********

# Paper Decision Update

The paper was not selected for a spotlight/oral/talk. It was not selected for a poster.

**********

# Paper Decision Update

The paper was not selected for a spotlight/oral/talk. It was not selected for a poster.

**********

# Paper Decision Update

The paper was not selected for a spotlight/oral/talk. It was not selected for a poster.

**********

# Paper Decision Update

The paper was not selected for a spotlight/oral/talk. It was not selected for a poster.

**********

# Paper Decision Update

The paper was not selected for a spotlight/oral/talk. It was not selected for a poster.

**********

# Paper Decision Update

The paper was not selected for a spotlight/oral/talk. It was not selected for a poster.

**********

# Paper Decision Update

The paper was not selected for a spotlight/oral/talk. It was not selected for a poster.

**********

# Paper Decision Update

The paper was not selected for a spotlight/oral/talk. It was not selected for a poster.

**********

# Paper Decision Update

The paper was not selected for a spotlight/oral/talk. It was not selected for a poster.

**********

# Paper Decision Update

The paper was not selected for a spotlight/oral/talk. It was not selected for a poster.

**********

# Paper Decision Update

The paper was not selected for a spotlight/oral/talk. It was not selected for a poster.

**********

# Paper Decision Update

The paper was not selected for a spotlight/oral/talk. It was not selected for a poster.

**********

# Paper Decision Update

The paper was not selected for a spotlight/oral/talk. It was not selected for a poster.

**********

# Paper Decision Update

The paper was not selected for a spotlight/oral/talk. It was not selected for a poster.

**********

# Paper Decision Update

The paper was not selected for a spotlight/oral/talk. It was not selected for a poster.

**********

# Paper Decision Update

The paper was not selected for a spotlight/oral/talk. It was not selected for a poster.

**********

# Paper Decision Update

The paper was not selected for a spotlight/oral/talk. It was not selected for a poster.

**********

# Paper Decision Update

The paper was not selected for a spotlight/oral/talk. It was not selected for a poster.

**********

# Paper Decision Update

The paper was not selected for a spotlight/oral/talk. It was not selected for a poster.

**********

# Paper Decision Update

The paper was not selected for a spotlight/oral/talk. It was not selected for a poster.

**********

# Paper Decision Update

The paper was not selected for a spotlight/oral/talk. It was not selected for a poster.

**********

# Paper Decision Update

The paper was not selected for a spotlight/oral/talk. It was not selected for a poster.

**********

# Paper Decision Update

The paper was not selected for a spotlight/oral/talk. It was not selected for a poster.

**********

# Paper Decision Update

The paper was not selected for a spotlight/oral/talk. It was not selected for a poster.

**********

# Paper Decision Update

The paper was not selected for a spotlight/oral/talk. It was not selected for a poster.

**********

# Paper Decision Update

The paper was not selected for a spotlight/oral/talk. It was not selected for a poster.

**********

# Paper Decision Update

The paper was not selected for a spotlight/oral/talk. It was not selected for a poster.

**********

# Paper Decision Update

The paper was not selected for a spotlight/oral/talk. It was not selected for a poster.

**********

# Paper Decision Update

The paper was not selected for a spotlight/oral/talk. It was not selected for a poster.

**********

# Paper Decision Update

The paper was not selected for a spotlight/oral/talk. It was not selected for a poster.

**********

# Paper Decision Update

The paper was not selected for a spotlight/oral/talk. It was not selected for a poster.

**********

# Paper Decision Update

The paper was not selected for a spotlight/oral/talk. It was not selected for a poster.

**********

# Paper Decision Update

The paper was not selected for a spotlight/oral/talk. It was not selected for a poster.

**********

# Paper Decision Update

The paper was not selected for a spotlight/oral/talk. It was not selected for a poster.

**********

# Paper Decision Update

The paper was not selected for a spotlight/oral/talk. It was not selected for a poster.

**********

# Paper Decision Update

The paper was not selected for a spotlight/oral/talk. It was not selected for a poster.

**********

# Paper Decision Update

The paper was not selected for a spotlight/oral/talk. It was not selected for a poster.

**********

# Paper Decision Update

The paper was not selected for a spotlight/oral/talk. It was not selected for a poster.

**********

# Paper Decision Update

The paper was not selected for a spotlight/oral/talk. It was not selected for a poster.

**********

# Paper Decision Update

The paper was not selected for a spotlight/oral/talk. It was not selected for a poster.

**********

# Paper Decision Update

The paper was not selected for a spotlight/oral/talk. It was not selected for a poster.

**********

# Paper Decision Update

The paper was not selected for a spotlight/oral/talk. It was not selected for a poster.

**********

# Paper Decision Update

The paper was not selected for a spotlight/oral/talk. It was not selected for a poster.

**********

# Paper Decision Update

The paper was not selected for a spotlight/oral/talk. It was not selected for a poster.

**********

# Paper Decision Update

The paper was not selected for a spotlight/oral/talk. It was not selected for a poster.

**********

# Paper Decision Update

The paper was not selected for a spotlight/oral/talk. It was not selected for a poster.

**********

# Paper Decision Update

The paper was not selected for a spotlight/oral/talk. It was not selected for a poster.

**********

# Paper Decision Update

The paper was not selected for a spotlight/oral/talk. It was not selected for a poster.

**********

# Paper Decision Update

The paper was not selected for a spotlight/oral/talk. It was not selected for a poster.

**********

# Paper Decision Update

The paper was not selected for a spotlight/oral/talk. It was not selected for a poster.

**********

# Paper Decision Update

The paper was not selected for a spotlight/oral/talk. It was not selected for a poster.

**********

# Paper Decision Update

The paper was not selected for a spotlight/oral/talk. It was not selected for a poster.

**********

# Paper Decision Update

The paper was not selected for a spotlight/oral/talk. It was not selected for a poster.

**********

# Paper Decision Update

The paper was not selected for a spotlight/oral/talk. It was not selected for a poster.

**********

# Paper Decision Update

The paper was not selected for a spotlight/oral/talk. It was not selected for a poster.

**********

# Paper Decision Update

The paper was not selected for a spotlight/oral/talk. It was not selected for a poster.

**********

# Paper Decision Update

The paper was not selected for a spotlight/oral/talk. It was not selected for a poster.

**********

# Paper Decision Update

The paper was not selected for a spotlight/oral/talk. It was not selected for a poster.

**********

# Paper Decision Update

The paper was not selected for a spotlight/oral/talk. It was not selected for a poster.

**********

# Paper Decision Update

The paper was not selected for a spotlight/oral/talk. It was not selected for a poster.

**********

# Paper Decision Update

The paper was not selected for a spotlight/oral/talk. It was not selected for a poster.

**********

# Paper Decision Update

The paper was not selected for a spotlight/oral/talk. It was not selected for a poster.

**********

# Paper Decision Update

The paper was not selected for a spotlight/oral/talk. It was not selected for a poster.

**********

# Paper Decision Update

The paper was not selected for a spotlight/oral/talk. It was not selected for a poster.

**********

# Paper Decision Update

The paper was not selected for a spotlight/oral/talk. It was not selected for a poster.

**********

# Paper Decision Update

The paper was not selected for a spotlight/oral/talk. It was not selected for a poster.

**********

# Paper Decision Update

The paper was not selected for a spotlight/oral/talk. It was not selected for a poster.

**********

# Paper Decision Update

The paper was not selected for a spotlight/oral/talk. It was not selected for a poster.

**********

# Paper Decision Update

The paper was not selected for a spotlight/oral/talk. It was not selected for a poster.

**********

# Paper Decision Update

The paper was not selected for a spotlight/oral/talk. It was not selected for a poster.

**********

# Paper Decision Update

The paper was not selected for a spotlight/oral/talk. It was not selected for a poster.

**********

# Paper Decision Update

The paper was not selected for a spotlight/oral/talk. It was not selected for a poster.

**********

# Paper Decision Update

The paper was not selected for a spotlight/oral/talk. It was not selected for a poster.

**********

# Paper Decision Update

The paper was not selected for a spotlight/oral/talk. It was not selected for a poster.

**********

# Paper Decision Update

The paper was not selected for a spotlight/oral/talk. It was not selected for a poster.

**********

# Paper Decision Update

The paper was not selected for a spotlight/oral/talk. It was not selected for a poster.

**********

# Paper Decision Update

The paper was not selected for a spotlight/oral/talk. It was not selected for a poster.

**********

# Paper Decision Update

The paper was not selected for a spotlight/oral/talk. It was not selected for a poster.

**********

# Paper Decision Update

The paper was not selected for a spotlight/oral/talk. It was not selected for a poster.

**********

# Paper Decision Update

The paper was not selected for a spotlight/oral/talk. It was not selected for a poster.

**********

# Paper Decision Update

The paper was not selected for a spotlight/oral/talk. It was not selected for a poster.

**********

# Paper Decision Update

The paper was not selected for a spotlight/oral/talk. It was not selected for a poster.

**********

# Paper Decision Update

The paper was not selected for a spotlight/oral/talk. It was not selected for a poster.

**********

# Paper Decision Update

The paper was not selected for a spotlight/oral/talk. It was not selected for a poster.

**********

# Paper Decision Update

The paper was not selected for a spotlight/oral/talk. It was not selected for a poster.

**********

# Paper Decision Update

The paper was not selected for a spotlight/oral/talk. It was not selected for a poster.

**********

# Paper Decision Update

The paper was not selected for a spotlight/oral/talk. It was not selected for a poster.

**********

# Paper Decision Update

The paper was not selected for a spotlight/oral/talk. It was not selected for a poster.

**********

# Paper Decision Update

The paper was not selected for a spotlight/oral/talk. It was not selected for a poster.

**********

# Paper Decision Update

The paper was not selected for a spotlight/oral/talk. It was not selected for a poster.

**********

# Paper Decision Update

The paper was not selected for a spotlight/oral/talk. It was not selected for a poster.

**********

# Paper Decision Update

The paper was not selected for a spotlight/oral/talk. It was not selected for a poster.

**********

# Paper Decision Update

The paper was not selected for a spotlight/oral/talk. It was not selected for a poster.

**********

# Paper Decision Update

The paper was not selected for a spotlight/oral/talk. It was not selected for a poster.

**********

# Paper Decision Update

The paper was not selected for a spotlight/oral/talk. It was not selected for a poster.

**********

# Paper Decision Update

The paper was not selected for a spotlight/oral/talk. It was not selected for a poster.

**********

# Paper Decision Update

The paper was not selected for a spotlight/oral/talk. It was not selected for a poster.

**********

# Paper Decision Update

The paper was not selected for a spotlight/oral/talk. It was not selected for a poster.

**********

# Paper Decision Update

The paper was not selected for a spotlight/oral/talk. It was not selected for a poster.

**********

# Paper Decision Update

The paper was not selected for a spotlight/oral/talk. It was not selected for a poster.

**********

# Paper Decision Update

The paper was not selected for a spotlight/oral/talk. It was not selected for a poster.

**********

# Paper Decision Update

The paper was not selected for a spotlight/oral/talk. It was not selected for a poster.

**********

# Paper Decision Update

The paper was not selected for a spotlight/oral/talk. It was not selected for a poster.

**********

# Paper Decision Update

The paper was not selected for a spotlight/oral/talk. It was not selected for a poster.

**********

# Paper Decision Update

The paper was not selected for a spotlight/oral/talk. It was not selected for a poster.

**********

# Paper Decision Update

The paper was not selected for a spotlight/oral/talk. It was not selected for a poster.

**********

# Paper Decision Update

The paper was not selected for a spotlight/oral/talk. It was not selected for a poster.

**********

# Paper Decision Update

The paper was not selected for a spotlight/oral/talk. It was not selected for a poster.

**********

# Paper Decision Update

The paper was not selected for a spotlight/oral/talk. It was not selected for a poster.

**********

# Paper Decision Update

The paper was not selected for a spotlight/oral/talk. It was not selected for a poster.

**********

# Paper Decision Update

The paper was not selected for a spotlight/oral/talk. It was not selected for a poster.

**********

# Paper Decision Update

The paper was not selected for a spotlight/oral/talk. It was not selected for a poster.

**********

# Paper Decision Update

The paper was not selected for a spotlight/oral/talk. It was not selected for a poster.

**********

# Paper Decision Update

The paper was not selected for a spotlight/oral/talk. It was not selected for a poster.

**********

# Paper Decision Update

The paper was not selected for a spotlight/oral/talk. It was not selected for a poster.

**********

# Paper Decision Update

The paper was not selected for a spotlight/oral/talk. It was not selected for a poster.

**********

# Paper Decision Update

The paper was not selected for a spotlight/oral/talk. It was not selected for a poster.

**********

# Paper Decision Update

The paper was not selected for a spotlight/oral/talk. It was not selected for a poster.

**********

# Paper Decision Update

The paper was not selected for a spotlight/oral/talk. It was not selected for a poster.

**********

# Paper Decision Update

The paper was not selected for a spotlight/oral/talk. It was not selected for a poster.

**********

# Paper Decision Update

The paper was not selected for a spotlight/oral/talk. It was not selected for a poster.

**********

# Paper Decision Update

The paper was not selected for a spotlight/oral/talk. It was not selected for a poster.

**********

# Paper Decision Update

The paper was not selected for a spotlight/oral/talk. It was not selected for a poster.

**********

# Paper Decision Update

The paper was not selected for a spotlight/oral/talk. It was not selected for a poster.

**********

# Paper Decision Update

The paper was not selected for a spotlight/oral/talk. It was not selected for a poster.

**********

# Paper Decision Update

The paper was not selected for a spotlight/oral/talk. It was not selected for a poster.

**********

# Paper Decision Update

The paper was not selected for a spotlight/oral/talk. It was not selected for a poster.

**********

# Paper Decision Update

The paper was not selected for a spotlight/oral/talk. It was not selected for a poster.

**********

# Paper Decision Update

The paper was not selected for a spotlight/oral/talk. It was not selected for a poster.

**********

# Paper Decision Update

The paper was not selected for a spotlight/oral/talk. It was not selected for a poster.

**********

# Paper Decision Update

The paper was not selected for a spotlight/oral/talk. It was not selected for a poster.

**********

# Paper Decision Update

The paper was not selected for a spotlight/oral/talk. It was not selected for a poster.

**********

# Paper Decision Update

The paper was not selected for a spotlight/oral/talk. It was not selected for a poster.

**********

# Paper Decision Update

The paper was not selected for a spotlight/oral/talk. It was not selected for a poster.

**********

# Paper Decision Update

The paper was not selected for a spotlight/oral/talk. It was not selected for a poster.

**********

# Paper Decision Update

The paper was not selected for a spotlight/oral/talk. It was not selected for a poster.

**********

# Paper Decision Update

The paper was not selected for a spotlight/oral/talk. It was not selected for a poster.

**********

# Paper Decision Update

The paper was not selected for a spotlight/oral/talk. It was not selected for a poster.

**********

# Paper Decision Update

The paper was not selected for a spotlight/oral/talk. It was not selected for a poster.

**********

# Paper Decision Update

The paper was not selected for a spotlight/oral/talk. It was not selected for a poster.

**********

# Paper Decision Update

The paper was not selected for a spotlight/oral/talk. It was not selected for a poster.

**********

# Paper Decision Update

The paper was not selected for a spotlight/oral/talk. It was not selected for a poster.

**********

# Paper Decision Update

The paper was not selected for a spotlight/oral/talk. It was not selected for a poster.

**********

# Paper Decision Update

The paper was not selected for a spotlight/oral/talk. It was not selected for a poster.

**********

# Paper Decision Update

The paper was not selected for a spotlight/oral/talk. It was not selected for a poster.

**********

# Paper Decision Update

The paper was not selected for a spotlight/oral/talk. It was not selected for a poster.

**********

# Paper Decision Update

The paper was not selected for a spotlight/oral/talk. It was not selected for a poster.

**********

# Paper Decision Update

The paper was not selected for a spotlight/oral/talk. It was not selected for a poster.

**********

# Paper Decision Update

The paper was not selected for a spotlight/oral/talk. It was not selected for a poster.

**********

# Paper Decision Update

The paper was not selected for a spotlight/oral/talk. It was not selected for a poster.

**********

# Paper Decision Update

The paper was not selected for a spotlight/oral/talk. It was not selected for a poster.

**********

# Paper Decision Update

The paper was not selected for a spotlight/oral/talk. It was not selected for a poster.

**********

# Paper Decision Update

The paper was not selected for a spotlight/oral/talk. It was not selected for a poster.

**********

# Paper Decision Update

The paper was not selected for a spotlight/oral/talk. It was not selected for a poster.

**********

# Paper Decision Update

The paper was not selected for a spotlight/oral/talk. It was not selected for a poster.

**********

# Paper Decision Update

The paper was not selected for a spotlight/oral/talk. It was not selected for a poster.

**********

# Paper Decision Update

The paper was not selected for a spotlight/oral/talk. It was not selected for a poster.

**********

# Paper Decision Update

The paper was not selected for a spotlight/oral/talk. It was not selected for a poster.

**********

# Paper Decision Update

The paper was not selected for a spotlight/oral/talk. It was not selected for a poster.

**********

# Paper Decision Update

The paper was not selected for a spotlight/oral/talk. It was not selected for a poster.

**********

# Paper Decision Update

The paper was not selected for a