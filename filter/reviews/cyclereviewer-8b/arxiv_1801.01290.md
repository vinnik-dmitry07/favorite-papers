## Reviewer

### Summary

This paper proposes a soft actor-critic algorithm for continuous control tasks. The algorithm is derived from the policy iteration method in the maximum entropy framework, and the theoretical convergence is proved. The algorithm is evaluated on MuJoCo tasks and the humanoid task, and the results show that the proposed algorithm achieves state-of-the-art performance.

### Soundness

3 good

### Presentation

3 good

### Contribution

3 good

### Strengths

- The paper is well-written and easy to follow.
- The algorithm is derived from the policy iteration method in the maximum entropy framework, and the theoretical convergence is proved.
- The algorithm achieves state-of-the-art performance on MuJoCo tasks and the humanoid task.

### Weaknesses

- The proposed algorithm is similar to the soft Q-learning algorithm proposed by Haarnoja et al. (2017). The main difference is that the proposed algorithm uses a separate critic network to estimate the state value function, while the soft Q-learning algorithm does not. The authors should compare the proposed algorithm with the soft Q-learning algorithm more clearly.
- The proposed algorithm uses two Q-function networks to mitigate the positive bias in the policy improvement step. However, the authors do not provide any theoretical analysis or experimental results to support this design choice.
- The proposed algorithm requires the reward function to be bounded. However, this assumption is not realistic in many real-world applications. The authors should discuss how the algorithm can be extended to handle unbounded rewards.

### Questions

See Weaknesses.

### Flag For Ethics Review

No ethics review needed.

### Rating

6: marginally above the acceptance threshold

### Confidence

3: You are fairly confident in your assessment. It is possible that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work. Math/other details were not carefully checked.

**********

## Reviewer

### Summary

This paper presents an off-policy actor-critic algorithm for continuous control tasks. The algorithm is derived from the policy iteration method in the maximum entropy framework, and the theoretical convergence is proved. The algorithm is evaluated on MuJoCo tasks and the humanoid task, and the results show that the proposed algorithm achieves state-of-the-art performance.

### Soundness

3 good

### Presentation

3 good

### Contribution

3 good

### Strengths

- The paper is well-written and easy to follow.
- The algorithm is derived from the policy iteration method in the maximum entropy framework, and the theoretical convergence is proved.
- The algorithm achieves state-of-the-art performance on MuJoCo tasks and the humanoid task.

### Weaknesses

- The proposed algorithm is similar to the soft Q-learning algorithm proposed by Haarnoja et al. (2017). The main difference is that the proposed algorithm uses a separate critic network to estimate the state value function, while the soft Q-learning algorithm does not. The authors should compare the proposed algorithm with the soft Q-learning algorithm more clearly.
- The proposed algorithm uses two Q-function networks to mitigate the positive bias in the policy improvement step. However, the authors do not provide any theoretical analysis or experimental results to support this design choice.
- The proposed algorithm requires the reward function to be bounded. However, this assumption is not realistic in many real-world applications. The authors should discuss how the algorithm can be extended to handle unbounded rewards.

### Questions

See Weaknesses.

### Flag For Ethics Review

No ethics review needed.

### Rating

6: marginally above the acceptance threshold

### Confidence

3: You are fairly confident in your assessment. It is possible that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work. Math/other details were not carefully checked.

**********

## Reviewer

### Summary

This paper introduces a new algorithm for deep reinforcement learning, called Soft Actor-Critic (SAC). The algorithm is based on the maximum entropy framework, which aims to maximize expected reward while also maximizing entropy. This is achieved by combining off-policy updates with a stable stochastic actor-critic formulation. The paper shows that SAC achieves state-of-the-art performance on a range of continuous control benchmark tasks, outperforming prior on-policy and off-policy methods. The paper also demonstrates that SAC is very stable, achieving very similar performance across different random seeds.

### Soundness

3 good

### Presentation

3 good

### Contribution

3 good

### Strengths

- The paper is well-written and easy to follow.
- The algorithm is derived from the policy iteration method in the maximum entropy framework, and the theoretical convergence is proved.
- The algorithm achieves state-of-the-art performance on MuJoCo tasks and the humanoid task.

### Weaknesses

- The algorithm is similar to the soft Q-learning algorithm proposed by Haarnoja et al. (2017). The main difference is that the proposed algorithm uses a separate critic network to estimate the state value function, while the soft Q-learning algorithm does not. The authors should compare the proposed algorithm with the soft Q-learning algorithm more clearly.
- The proposed algorithm uses two Q-function networks to mitigate the positive bias in the policy improvement step. However, the authors do not provide any theoretical analysis or experimental results to support this design choice.
- The proposed algorithm requires the reward function to be bounded. However, this assumption is not realistic in many real-world applications. The authors should discuss how the algorithm can be extended to handle unbounded rewards.

### Questions

See Weaknesses.

### Flag For Ethics Review

No ethics review needed.

### Rating

6: marginally above the acceptance threshold

### Confidence

3: You are fairly confident in your assessment. It is possible that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work. Math/other details were not carefully checked.

**********

## Reviewer

### Summary

This paper introduces a new off-policy actor-critic algorithm for continuous control tasks. The algorithm is derived from the policy iteration method in the maximum entropy framework, and the theoretical convergence is proved. The algorithm achieves state-of-the-art performance on MuJoCo tasks and the humanoid task.

### Soundness

3 good

### Presentation

3 good

### Contribution

3 good

### Strengths

- The paper is well-written and easy to follow.
- The algorithm is derived from the policy iteration method in the maximum entropy framework, and the theoretical convergence is proved.
- The algorithm achieves state-of-the-art performance on MuJoCo tasks and the humanoid task.

### Weaknesses

- The proposed algorithm is similar to the soft Q-learning algorithm proposed by Haarnoja et al. (2017). The main difference is that the proposed algorithm uses a separate critic network to estimate the state value function, while the soft Q-learning algorithm does not. The authors should compare the proposed algorithm with the soft Q-learning algorithm more clearly.
- The proposed algorithm uses two Q-function networks to mitigate the positive bias in the policy improvement step. However, the authors do not provide any theoretical analysis or experimental results to support this design choice.
- The proposed algorithm requires the reward function to be bounded. However, this assumption is not realistic in many real-world applications. The authors should discuss how the algorithm can be extended to handle unbounded rewards.

### Questions

See Weaknesses.

### Flag For Ethics Review

No ethics review needed.

### Rating

6: marginally above the acceptance threshold

### Confidence

3: You are fairly confident in your assessment. It is possible that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work. Math/other details were not carefully checked.

**********

## Meta Review

This paper presents an off-policy actor-critic algorithm for continuous control tasks. The algorithm is derived from the policy iteration method in the maximum entropy framework, and the theoretical convergence is proved. The algorithm is evaluated on MuJoCo tasks and the humanoid task, and the results show that the proposed algorithm achieves state-of-the-art performance. The paper is well-written and easy to follow.

The main concerns raised by the reviewers are:
- The proposed algorithm is similar to the soft Q-learning algorithm proposed by Haarnoja et al. (2017). The main difference is that the proposed algorithm uses a separate critic network to estimate the state value function, while the soft Q-learning algorithm does not. The authors should compare the proposed algorithm with the soft Q-learning algorithm more clearly.
- The proposed algorithm uses two Q-function networks to mitigate the positive bias in the policy improvement step. However, the authors do not provide any theoretical analysis or experimental results to support this design choice.
- The proposed algorithm requires the reward function to be bounded. However, this assumption is not realistic in many real-world applications. The authors should discuss how the algorithm can be extended to handle unbounded rewards.

The authors have addressed the concerns in the rebuttal. The paper is recommended for acceptance.

### justification_for_why_not_higher_score

The paper is a solid contribution to the field of reinforcement learning, but it is not a groundbreaking work.

### justification_for_why_not_lower_score

The paper is a solid contribution to the field of reinforcement learning, and it is a good fit for the ICLR conference.

**********

## Paper Decision

Accept (poster)