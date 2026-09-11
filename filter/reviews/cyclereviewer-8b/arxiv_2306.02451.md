## Reviewer

### Summary

This paper proposes a method for learning state-action representations from low-level states in reinforcement learning. The proposed method, called SALE, learns state-action embeddings that model the dynamics of the environment in latent space. The authors study the design space of these embeddings and highlight important design considerations. They also integrate SALE with an adaptation of checkpoints for RL into TD3 to form the TD7 algorithm, which significantly outperforms existing continuous control algorithms.

### Soundness

3 good

### Presentation

3 good

### Contribution

2 fair

### Strengths

- The paper is well-written and easy to follow.
- The proposed method is simple and effective.
- The authors perform an extensive empirical evaluation over the design space of the proposed method and highlight important design considerations.

### Weaknesses

- The proposed method is an extension of OFENet, and the main difference is the clipping of the target value function. However, the authors do not provide a theoretical justification for the clipping operation, and it is unclear why this is necessary.
- The authors do not provide a clear explanation of how the state-action representation is used in the RL algorithm. It is unclear how the representation is used to improve the performance of the RL algorithm.
- The authors do not provide a comparison with other state-of-the-art RL algorithms that use state-action representations.
- The authors do not provide a clear explanation of how the proposed method can be applied to other RL algorithms.

### Questions

- Can the authors provide a theoretical justification for the clipping operation?
- Can the authors provide a clear explanation of how the state-action representation is used in the RL algorithm?
- Can the authors provide a comparison with other state-of-the-art RL algorithms that use state-action representations?
- Can the authors provide a clear explanation of how the proposed method can be applied to other RL algorithms?

### Flag For Ethics Review

No ethics review needed.

### Rating

6: marginally above the acceptance threshold

### Confidence

4: You are confident in your assessment, but not absolutely certain. It is unlikely, but not impossible, that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work.

**********

## Reviewer

### Summary

This paper proposes a novel approach for learning embeddings that model the interaction between state and action. The authors introduce three important design considerations when learning a state-action representation online. They also perform an extensive empirical evaluation over the design space to show that their approach is the correct and highest performing set of choices. The authors combine their state-action representation learning method with an adaptation of checkpoints for RL into TD3 to form the TD7 algorithm, which significantly outperforms existing continuous control algorithms.

### Soundness

3 good

### Presentation

3 good

### Contribution

3 good

### Strengths

- The paper is well written and easy to follow. 
- The authors perform an extensive empirical evaluation over the design space to show that their approach is the correct and highest performing set of choices.
- The authors combine their state-action representation learning method with an adaptation of checkpoints for RL into TD3 to form the TD7 algorithm, which significantly outperforms existing continuous control algorithms.

### Weaknesses

- The authors should provide more details on the hyperparameters used in the experiments.
- The authors should provide more details on the architecture of the encoders.

### Questions

Please see the weaknesses above.

### Flag For Ethics Review

No ethics review needed.

### Rating

6: marginally above the acceptance threshold

### Confidence

4: You are confident in your assessment, but not absolutely certain. It is unlikely, but not impossible, that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work.

**********

## Reviewer

### Summary

This paper proposes a method for learning state-action representations from low-level states in reinforcement learning. The proposed method, called SALE, learns state-action embeddings that model the dynamics of the environment in latent space. The authors study the design space of these embeddings and highlight important design considerations. They also integrate SALE and an adaptation of checkpoints for RL into TD3 to form the TD7 algorithm, which significantly outperforms existing continuous control algorithms.

### Soundness

3 good

### Presentation

3 good

### Contribution

3 good

### Strengths

The paper is well-written and easy to follow. The authors provide a thorough empirical evaluation of the design space of the proposed method and highlight important design considerations. The proposed method is simple and effective.

### Weaknesses

The paper does not provide a theoretical justification for the clipping operation. It is unclear why this is necessary and how it affects the performance of the algorithm. The authors do not provide a clear explanation of how the state-action representation is used in the RL algorithm. It is unclear how the representation is used to improve the performance of the RL algorithm.

### Questions

1. The authors should provide a theoretical justification for the clipping operation. It is unclear why this is necessary and how it affects the performance of the algorithm.
2. The authors should provide a clear explanation of how the state-action representation is used in the RL algorithm. It is unclear how the representation is used to improve the performance of the algorithm.
3. The authors should provide a comparison with other state-of-the-art RL algorithms that use state-action representations.

### Flag For Ethics Review

No ethics review needed.

### Rating

6: marginally above the acceptance threshold

### Confidence

4: You are confident in your assessment, but not absolutely certain. It is unlikely, but not impossible, that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work.

**********

## Reviewer

### Summary

The paper presents a method for learning state-action representations in reinforcement learning (RL), which is a relatively under-explored area. The proposed method, called SALE, learns embeddings that capture the interaction between state and action, and it is shown to improve the performance of RL algorithms. The paper also introduces a new algorithm, TD7, which combines SALE with other techniques such as prioritized experience replay and policy checkpoints. The results show that TD7 outperforms existing RL algorithms on benchmark tasks.

### Soundness

3 good

### Presentation

3 good

### Contribution

3 good

### Strengths

The paper is well-written and easy to follow. The proposed method is simple and effective. The paper provides a thorough empirical evaluation of the design space of the proposed method and highlights important design considerations. The results show that the proposed method significantly outperforms existing RL algorithms on benchmark tasks.

### Weaknesses

The paper does not provide a theoretical justification for the clipping operation. It is unclear why this is necessary and how it affects the performance of the algorithm. The authors do not provide a clear explanation of how the state-action representation is used in the RL algorithm. It is unclear how the representation is used to improve the performance of the algorithm. The paper does not provide a comparison with other state-of-the-art RL algorithms that use state-action representations. The paper does not provide a clear explanation of how the proposed method can be applied to other RL algorithms.

### Questions

1. The authors should provide a theoretical justification for the clipping operation. It is unclear why this is necessary and how it affects the performance of the algorithm.
2. The authors should provide a clear explanation of how the state-action representation is used in the RL algorithm. It is unclear how the representation is used to improve the performance of the algorithm.
3. The authors should provide a comparison with other state-of-the-art RL algorithms that use state-action representations.
4. The authors should provide a clear explanation of how the proposed method can be applied to other RL algorithms.

### Flag For Ethics Review

No ethics review needed.

### Rating

6: marginally above the acceptance threshold

### Confidence

3: You are fairly confident in your assessment. It is possible that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work. Math/other details were not carefully checked.

**********

## Meta Review

This paper proposes a method for learning state-action representations from low-level states in reinforcement learning. The proposed method, called SALE, learns state-action embeddings that model the dynamics of the environment in latent space. The authors study the design space of these embeddings and highlight important design considerations. They also integrate SALE and an adaptation of checkpoints for RL into TD3 to form the TD7 algorithm, which significantly outperforms existing continuous control algorithms.

The paper received four reviews, all of which were positive. The reviewers appreciated the simplicity and effectiveness of the proposed method, as well as the thorough empirical evaluation of the design space of the proposed method. The authors provided detailed responses to the reviewers' comments and concerns. The reviewers' comments were addressed, and the authors made significant improvements to the paper.

### justification_for_why_not_higher_score

The paper is a good contribution to the field of reinforcement learning, but it is not a groundbreaking or highly influential work.

### justification_for_why_not_lower_score

The paper is a good contribution to the field of reinforcement learning, and it has the potential to inspire future research in this area.

**********

## Paper Decision

Accept (poster)