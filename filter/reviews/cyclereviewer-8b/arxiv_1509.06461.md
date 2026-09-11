## Reviewer

### Summary

The paper presents an analysis of the overestimation of the Q-learning algorithm in the context of the DQN algorithm. The authors show that the overestimation can be reduced by introducing a modification to the DQN algorithm, which they refer to as Double DQN. The authors also provide a theoretical analysis of the overestimation and the proposed modification.

### Soundness

2 fair

### Presentation

3 good

### Contribution

2 fair

### Strengths

The paper presents an analysis of the overestimation of the Q-learning algorithm in the context of the DQN algorithm. The authors show that the overestimation can be reduced by introducing a modification to the DQN algorithm, which they refer to as Double DQN. The authors also provide a theoretical analysis of the overestimation and the proposed modification.

### Weaknesses

The paper lacks a comprehensive discussion of the limitations and potential drawbacks of the proposed approach. The authors should provide a more detailed analysis of the computational complexity and scalability of the proposed algorithm, as well as its potential limitations in terms of generalizability and applicability to different types of problems.

### Questions

The paper presents an analysis of the overestimation of the Q-learning algorithm in the context of the DQN algorithm. The authors show that the overestimation can be reduced by introducing a modification to the DQN algorithm, which they refer to as Double DQN. The authors also provide a theoretical analysis of the overestimation and the proposed modification.

### Flag For Ethics Review

No ethics review needed.

### Rating

5: marginally below the acceptance threshold

### Confidence

2: You are willing to defend your assessment, but it is quite likely that you did not understand the central parts of the submission or that you are unfamiliar with some pieces of related work. Math/other details were not carefully checked.

**********

## Reviewer

### Summary

The paper presents an analysis of the overestimation of the Q-learning algorithm in the context of the DQN algorithm. The authors show that the overestimation can be reduced by introducing a modification to the DQN algorithm, which they refer to as Double DQN. The authors also provide a theoretical analysis of the overestimation and the proposed modification.

### Soundness

3 good

### Presentation

3 good

### Contribution

3 good

### Strengths

The paper presents an analysis of the overestimation of the Q-learning algorithm in the context of the DQN algorithm. The authors show that the overestimation can be reduced by introducing a modification to the DQN algorithm, which they refer to as Double DQN. The authors also provide a theoretical analysis of the overestimation and the proposed modification.

### Weaknesses

The paper lacks a comprehensive discussion of the limitations and potential drawbacks of the proposed approach. The authors should provide a more detailed analysis of the computational complexity and scalability of the proposed algorithm, as well as its potential limitations in terms of generalizability and applicability to different types of problems.

### Questions

The paper presents an analysis of the overestimation of the Q-learning algorithm in the context of the DQN algorithm. The authors show that the overestimation can be reduced by introducing a modification to the DQN algorithm, which they refer to as Double DQN. The authors also provide a theoretical analysis of the overestimation and the proposed modification.

### Flag For Ethics Review

No ethics review needed.

### Rating

5: marginally below the acceptance threshold

### Confidence

2: You are willing to defend your assessment, but it is quite likely that you did not understand the central parts of the submission or that you are unfamiliar with some pieces of related work. Math/other details were not carefully checked.

**********

## Reviewer

### Summary

The paper introduces an adaptation of Double Q-learning to the Deep Q-Networks (DQN) algorithm, which is a popular algorithm for deep reinforcement learning. The authors show that the standard DQN algorithm suffers from overestimation of the action values, which can negatively affect the performance of the algorithm. They propose a modification to the DQN algorithm, called Double DQN, which reduces the overestimation of the action values and leads to better performance on several games. The authors also provide a theoretical analysis of the overestimation and the proposed modification.

### Soundness

3 good

### Presentation

3 good

### Contribution

3 good

### Strengths

The paper is well-written and easy to follow. The authors provide a clear explanation of the problem of overestimation in the DQN algorithm and how their proposed solution addresses it. The empirical results are presented clearly and show that the proposed method outperforms the standard DQN algorithm on several games.

### Weaknesses

The paper only evaluates the proposed method on a subset of the Atari games, and it would be interesting to see how the method performs on a wider range of games.

### Questions

How does the proposed method compare to other methods that address the overestimation problem in deep reinforcement learning?

### Flag For Ethics Review

No ethics review needed.

### Rating

6: marginally above the acceptance threshold

### Confidence

2: You are willing to defend your assessment, but it is quite likely that you did not understand the central parts of the submission or that you are unfamiliar with some pieces of related work. Math/other details were not carefully checked.

**********

## Reviewer

### Summary

This paper studies the overestimation problem in Q-learning, which is known to be a problem in the tabular setting. This paper shows that the overestimation problem also exists in the deep RL setting. The authors propose a simple modification to DQN, which is to replace the target in DQN with the one in double Q-learning. The authors show that this modification can reduce the overestimation problem in DQN and improve the performance on the Atari benchmark.

### Soundness

3 good

### Presentation

3 good

### Contribution

3 good

### Strengths

- The paper is well-written and easy to follow.
- The proposed method is simple and intuitive.
- The empirical results are promising.

### Weaknesses

- The authors only compare with DQN. It would be better to compare with other state-of-the-art algorithms, such as C51 (Munos et al., 2016) and Rainbow (Hessel et al., 2018), which also address the overestimation problem.
- The authors only consider the Atari benchmark. It would be better to consider other benchmarks, such as MuJoCo, where the overestimation problem is also a problem.
- The authors only consider the discrete action space. It would be better to consider the continuous action space.

### Questions

- The authors claim that "DQN sometimes substantially overestimates the values of the actions". However, it is not clear how to measure the overestimation. Can the authors provide more analysis on this?

### Flag For Ethics Review

No ethics review needed.

### Rating

6: marginally above the acceptance threshold

### Confidence

3: You are fairly confident in your assessment. It is possible that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work. Math/other details were not carefully checked.

**********

## Meta Review

The paper presents an analysis of the overestimation of the Q-learning algorithm in the context of the DQN algorithm. The authors show that the overestimation can be reduced by introducing a modification to the DQN algorithm, which they refer to as Double DQN. The authors also provide a theoretical analysis of the overestimation and the proposed modification.

The reviewers raised several concerns about the paper, including the lack of a comprehensive discussion of the limitations and potential drawbacks of the proposed approach, the lack of a comparison with other methods that address the overestimation problem in deep reinforcement learning, and the limited evaluation of the proposed method on a subset of the Atari games. The authors provided a rebuttal to the reviewers' concerns, but it did not fully address the concerns raised.

### justification_for_why_not_higher_score

The reviewers raised several concerns about the paper, including the lack of a comprehensive discussion of the limitations and potential drawbacks of the proposed approach, the lack of a comparison with other methods that address the overestimation problem in deep reinforcement learning, and the limited evaluation of the proposed method on a subset of the Atari games. The authors provided a rebuttal to the reviewers' concerns, but it did not fully address the concerns raised.

### justification_for_why_not_lower_score

N/A

**********

## Paper Decision

Reject (not selected for a spotlight/oral/poster)