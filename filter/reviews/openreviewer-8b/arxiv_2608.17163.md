# Review

## Summary
This paper introduces Q-Learning with World Models (QWM), a framework that enhances Q-learning by integrating world models for test-time action selection. QWM leverages a learned world model to predict state changes and improve action choices during both online rollouts and evaluations. By using future predictions to score actions without relying on imagined rollouts, QWM avoids compounding model bias and achieves higher sample efficiency. Experiments on Robomimic and LIBERO benchmarks show that QWM outperforms both model-free and model-based RL methods, demonstrating its effectiveness in complex robotic tasks.

## Soundness
3

## Presentation
3

## Contribution
3

## Strengths
1. The paper is clearly written and easy to follow.
2. The proposed method is novel, which leverages the world model to improve the action selection of Q-learning.
3. The experiments are comprehensive, including both state-based and visual observation settings, and the results show that QWM outperforms both model-free and model-based RL methods.

## Weaknesses
1. The proposed method introduces additional computational overhead at test time, which may be a concern for real-world applications.
2. The proposed method relies on a well-performed world model, which is not always easy to obtain.
3. The proposed method is only evaluated on two simulation environments, which may not be sufficient.

## Questions
1. How does the computational overhead of QWM compare to the baselines during training and evaluation? Does it introduce significant overhead during training or evaluation?
2. How does the performance of QWM change if the world model is not well-performed? Does it still have some robustness when the world model makes prediction errors?
3. Can the authors provide more results on other simulation environments to show the generalization of the proposed method?

## Flag For Ethics Review
No ethics review needed.

## Details Of Ethics Concerns


## Rating
6

## Confidence
4