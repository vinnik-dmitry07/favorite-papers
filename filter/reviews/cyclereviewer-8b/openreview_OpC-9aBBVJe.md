## Reviewer

### Summary

This paper studies the effect of replay ratio scaling in deep reinforcement learning. The authors propose to scale the replay ratio by resetting the parameters of the agent periodically. This approach is evaluated on the DeepMind Control Suite and Atari 100k benchmarks. The results show that the proposed approach outperforms the baselines.

### Soundness

3 good

### Presentation

3 good

### Contribution

2 fair

### Strengths

The paper is well-written and easy to follow. The authors provide a comprehensive overview of the related work and the problem setup. The results are presented clearly and the ablation studies are informative.

### Weaknesses

The main weakness of the paper is the novelty of the approach. The idea of resetting the parameters periodically has been proposed in previous works (e.g., Nikishin et al., 2022). The authors do not provide a theoretical analysis of the proposed approach. The results are only evaluated on two benchmarks and the baselines are not up-to-date. For example, the authors only compare with REDQ, which was proposed in 2021. There are more recent works that have been proposed since then. The authors also do not provide any ablation studies on the hyperparameters of the proposed approach.

### Questions

- How does the proposed approach compare with other methods that use ensembles or normalization strategies to improve sample efficiency?
- How does the proposed approach compare with other methods that use periodic resets to improve sample efficiency?
- What are the hyperparameters of the proposed approach? How are they tuned?
- What are the limitations of the proposed approach?

### Flag For Ethics Review

No ethics review needed.

### Rating

6: marginally above the acceptance threshold

### Confidence

3: You are fairly confident in your assessment. It is possible that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work. Math/other details were not carefully checked.

**********

## Reviewer

### Summary

This paper investigates the effect of replay ratio scaling in deep reinforcement learning. The authors propose to scale the replay ratio by resetting the parameters of the agent periodically. This approach is evaluated on the DeepMind Control Suite and Atari 100k benchmarks. The results show that the proposed approach outperforms the baselines.

### Soundness

3 good

### Presentation

3 good

### Contribution

2 fair

### Strengths

The paper is well-written and easy to follow. The authors provide a comprehensive overview of the related work and the problem setup. The results are presented clearly and the ablation studies are informative.

### Weaknesses

The main weakness of the paper is the novelty of the approach. The idea of resetting the parameters periodically has been proposed in previous works (e.g., Nikishin et al., 2022). The authors do not provide a theoretical analysis of the proposed approach. The results are only evaluated on two benchmarks and the baselines are not up-to-date. For example, the authors only compare with REDQ, which was proposed in 2021. There are more recent works that have been proposed since then. The authors also do not provide any ablation studies on the hyperparameters of the proposed approach.

### Questions

- How does the proposed approach compare with other methods that use ensembles or normalization strategies to improve sample efficiency?
- How does the proposed approach compare with other methods that use periodic resets to improve sample efficiency?
- What are the hyperparameters of the proposed approach? How are they tuned?
- What are the limitations of the proposed approach?

### Flag For Ethics Review

No ethics review needed.

### Rating

6: marginally above the acceptance threshold

### Confidence

3: You are fairly confident in your assessment. It is possible that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work. Math/other details were not carefully checked.

**********

## Reviewer

### Summary

The paper proposes a method to improve the sample efficiency of deep RL by scaling the replay ratio. The method is based on the observation that the ability of a neural network to learn and generalize decreases over time, and that this can be mitigated by periodically resetting the network parameters. The authors evaluate their method on the DeepMind Control Suite and Atari 100k benchmarks, and show that it outperforms existing methods.

### Soundness

3 good

### Presentation

3 good

### Contribution

3 good

### Strengths

The paper is well-written and easy to follow. The authors provide a comprehensive overview of the related work and the problem setup. The results are presented clearly and the ablation studies are informative.

### Weaknesses

The paper only evaluates the proposed method on two benchmarks, and does not provide a theoretical analysis of the proposed approach. Additionally, the paper does not compare the proposed method with other methods that use periodic resets to improve sample efficiency.

### Questions

- How does the proposed approach compare with other methods that use ensembles or normalization strategies to improve sample efficiency?
- How does the proposed approach compare with other methods that use periodic resets to improve sample efficiency?
- What are the hyperparameters of the proposed approach? How are they tuned?
- What are the limitations of the proposed approach?

### Flag For Ethics Review

No ethics review needed.

### Rating

6: marginally above the acceptance threshold

### Confidence

3: You are fairly confident in your assessment. It is possible that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work. Math/other details were not carefully checked.

**********

## Reviewer

### Summary

The paper investigates the impact of replay ratio scaling in deep reinforcement learning (RL) and proposes a method to scale the replay ratio by periodically resetting the agent's parameters. The method is evaluated on the DeepMind Control Suite and Atari 100k benchmarks, and the results show that the proposed approach outperforms the baselines. The paper also discusses the importance of online interaction in the training process and the trade-offs involved in replay ratio scaling.

### Soundness

3 good

### Presentation

3 good

### Contribution

3 good

### Strengths

- The paper is well-written and easy to follow. The authors provide a comprehensive overview of the related work and the problem setup.
- The results are presented clearly and the ablation studies are informative.
- The paper provides a good discussion on the importance of online interaction in the training process and the trade-offs involved in replay ratio scaling.

### Weaknesses

- The paper only evaluates the proposed method on two benchmarks, and does not provide a theoretical analysis of the proposed approach.
- The paper does not compare the proposed method with other methods that use periodic resets to improve sample efficiency.

### Questions

- How does the proposed approach compare with other methods that use ensembles or normalization strategies to improve sample efficiency?
- How does the proposed approach compare with other methods that use periodic resets to improve sample efficiency?
- What are the hyperparameters of the proposed approach? How are they tuned?
- What are the limitations of the proposed approach?

### Flag For Ethics Review

No ethics review needed.

### Rating

6: marginally above the acceptance threshold

### Confidence

3: You are fairly confident in your assessment. It is possible that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work. Math/other details were not carefully checked.

**********

## Meta Review

The paper studies the effect of replay ratio scaling in deep reinforcement learning. The authors propose to scale the replay ratio by resetting the parameters of the agent periodically. This approach is evaluated on the DeepMind Control Suite and Atari 100k benchmarks. The results show that the proposed approach outperforms the baselines. The paper also discusses the importance of online interaction in the training process and the trade-offs involved in replay ratio scaling.

The reviewers appreciate the paper's well-written presentation and the comprehensive overview of the related work. They also find the results and ablation studies informative. However, the reviewers also raise concerns about the novelty of the approach, the lack of theoretical analysis, and the limited evaluation on two benchmarks. The authors address some of these concerns in their rebuttal, and the reviewers agree that the paper makes a contribution to the field. Therefore, I recommend accepting the paper.

### justification_for_why_not_higher_score

The paper's novelty and evaluation are limited.

### justification_for_why_not_lower_score

The paper makes a contribution to the field.

**********

## Paper Decision

Accept (poster)