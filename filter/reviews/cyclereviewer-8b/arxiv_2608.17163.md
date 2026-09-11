## Reviewer

### Summary

This paper proposes a new algorithm to combine model-based and model-free RL. The idea is to use a world model to generate a tree of possible future states and then use a Q-function to select the best action. The Q-function is trained using standard Q-learning. The world model is trained using offline data. The authors evaluate their method on a variety of robotic manipulation tasks and show that it outperforms prior methods.

### Soundness

3 good

### Presentation

3 good

### Contribution

2 fair

### Strengths

The paper is well-written and easy to follow. The idea of using a world model to generate a tree of possible future states and then using a Q-function to select the best action is interesting and novel. The authors evaluate their method on a variety of robotic manipulation tasks and show that it outperforms prior methods.

### Weaknesses

The main weakness of the paper is that the authors do not provide a theoretical analysis of their method. While the authors do provide some experimental results, the results are limited to a few tasks and do not provide a comprehensive evaluation of the method. In particular, the authors do not provide a comparison with other model-based RL methods or other methods that use world models. The authors also do not provide a discussion of the limitations of their method and potential future work.

### Questions

1. How does the proposed method compare to other model-based RL methods? The authors only compare to model-free methods, but there are many other model-based methods that could be compared to.
2. How does the proposed method compare to other methods that use world models? The authors only compare to model-free methods, but there are many other methods that use world models that could be compared to.
3. What are the limitations of the proposed method? The authors do not discuss the limitations of their method, which is an important part of any paper.
4. What are some potential future directions for the proposed method? The authors do not discuss potential future directions for their method, which is an important part of any paper.

### Flag For Ethics Review

No ethics review needed.

### Rating

5: marginally below the acceptance threshold

### Confidence

3: You are fairly confident in your assessment. It is possible that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work. Math/other details were not carefully checked.

**********

## Reviewer

### Summary

This paper introduces a new approach to model-based RL, which leverages world models to perform test-time search over actions on top of Q-learning to improve performance. The proposed method, QWM, uses the world model to predict future outcomes, enabling test-time search over candidate actions and selecting the ones with the best predicted future returns. QWM outperforms strong model-free baselines and avoids compounding model bias, while also providing consistent benefits across different underlying RL algorithms.

### Soundness

3 good

### Presentation

3 good

### Contribution

3 good

### Strengths

1. The paper is well-written and easy to follow.
2. The idea of using world models for test-time search over actions on top of Q-learning is novel and interesting.
3. The experimental results show that QWM outperforms strong model-free baselines and avoids compounding model bias.
4. The paper provides a clear analysis of the hyperparameters for constructing the search tree, which is helpful for practitioners to understand the proposed method.

### Weaknesses

1. The paper only evaluates the proposed method on robotic manipulation tasks, which may not be representative of all RL domains. It would be interesting to see how the proposed method performs on other types of tasks, such as navigation or game playing.
2. The paper does not provide a detailed analysis of the computational overhead of the proposed method. While the paper mentions that the tree search introduces non-trivial computational overhead, it would be helpful to provide a more detailed analysis of the computational cost of the proposed method compared to other model-based RL methods.
3. The paper does not provide a detailed analysis of the limitations of the proposed method. While the paper mentions that QWM depends on learning a world model, which is an expensive and often challenging task, it would be helpful to provide a more detailed analysis of the limitations of the proposed method and potential future work.

### Questions

1. How does the proposed method compare to other model-based RL methods that use world models, such as WMPO and World4RL?
2. How does the proposed method compare to other methods that use test-time search over actions, such as test-time scaling and best-of-N sampling?
3. How does the proposed method perform on tasks with high-dimensional visual observations?
4. How does the proposed method perform on tasks with sparse rewards?
5. How does the proposed method perform on tasks with long horizons?

### Flag For Ethics Review

No ethics review needed.

### Rating

6: marginally above the acceptance threshold

### Confidence

4: You are confident in your assessment, but not absolutely certain. It is unlikely, but not impossible, that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work.

**********

## Reviewer

### Summary

This paper proposes a new method that combines model-based and model-free RL, where the world model is used to generate a tree of possible future states and then a Q-function is used to select the best action. The Q-function is trained using standard Q-learning. The world model is trained using offline data. The authors evaluate their method on a variety of robotic manipulation tasks and show that it outperforms prior methods.

### Soundness

3 good

### Presentation

3 good

### Contribution

3 good

### Strengths

- The paper is well-written and easy to follow.
- The idea of using a world model to generate a tree of possible future states and then using a Q-function to select the best action is interesting and novel.
- The experimental results show that the proposed method outperforms prior methods.

### Weaknesses

- The paper does not provide a theoretical analysis of the proposed method.
- The paper only evaluates the proposed method on robotic manipulation tasks, which may not be representative of all RL domains.
- The paper does not provide a detailed analysis of the computational overhead of the proposed method.
- The paper does not provide a detailed analysis of the limitations of the proposed method.

### Questions

- How does the proposed method compare to other model-based RL methods?
- How does the proposed method compare to other methods that use world models?
- What are the limitations of the proposed method?
- What are some potential future directions for the proposed method?

### Flag For Ethics Review

No ethics review needed.

### Rating

6: marginally above the acceptance threshold

### Confidence

3: You are fairly confident in your assessment. It is possible that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work. Math/other details were not carefully checked.

**********

## Reviewer

### Summary

This paper proposes a method for using world models to improve Q-learning. The proposed method, QWM, leverages world models to perform test-time search over imagined trajectories on top of Q-learning to select high-value actions during both online rollouts and evaluation. The method avoids compounding model bias while still gaining the sample-efficiency benefits of predictive search. The authors evaluate QWM on challenging manipulation benchmarks Robomimic and LIBERO, and find that it significantly outperforms strong prior methods on both sample efficiency and performance.

### Soundness

3 good

### Presentation

3 good

### Contribution

3 good

### Strengths

- The paper is well-written and easy to follow.
- The idea of using world models to improve Q-learning is interesting and novel.
- The proposed method is simple and general, and can be applied to any RL fine-tuning algorithm.

### Weaknesses

- The experiments are limited to two manipulation tasks, and it is unclear how the method would perform on other types of tasks.
- The method requires the use of a world model, which can be expensive and challenging to train.
- The method requires the use of a Q-function, which can be computationally expensive to train.

### Questions

- How does the method perform on tasks with high-dimensional visual observations?
- How does the method perform on tasks with sparse rewards?
- How does the method perform on tasks with long horizons?

### Flag For Ethics Review

No ethics review needed.

### Rating

6: marginally above the acceptance threshold

### Confidence

3: You are fairly confident in your assessment. It is possible that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work. Math/other details were not carefully checked.

**********

## Meta Review

This paper introduces QWM, a novel approach to model-based reinforcement learning (RL) that leverages world models to enhance Q-learning. The method uses world models to generate a tree of possible future states, and then employs a Q-function to select the best action. The Q-function is trained using standard Q-learning, while the world model is trained using offline data. The authors evaluate QWM on various robotic manipulation tasks and demonstrate its superiority over prior methods. The paper is well-written and easy to follow, and the idea of using world models for test-time search over actions on top of Q-learning is innovative. The experimental results show that QWM outperforms strong model-free baselines and avoids compounding model bias. The paper provides a clear analysis of the hyperparameters for constructing the search tree, which is helpful for practitioners to understand the proposed method. However, the paper lacks a theoretical analysis of the proposed method, and the experiments are limited to robotic manipulation tasks. The paper also does not provide a detailed analysis of the computational overhead of the proposed method and the limitations of the proposed method. Overall, while the paper has some strengths, it also has some weaknesses that need to be addressed. The authors are encouraged to revise the paper based on the reviewers' feedback and resubmit it to a future conference.

### justification_for_why_not_higher_score

The paper has some weaknesses that need to be addressed, such as the lack of a theoretical analysis of the proposed method and the limited scope of the experiments.

### justification_for_why_not_lower_score

N/A

**********

## Paper Decision

Reject (out of the running for an oral, but can be accepted as a poster) (poster) (poster) (poster) (poster)

**********

## Paper Decision Summary

This paper introduces QWM, a novel approach to model-based reinforcement learning (RL) that leverages world models to enhance Q-learning. The method uses world models to generate a tree of possible future states, and then employs a Q-function to select the best action. The Q-function is trained using standard Q-learning, while the world model is trained using offline data. The authors evaluate QWM on various robotic manipulation tasks and demonstrate its superiority over prior methods. The paper is well-written and easy to follow, and the idea of using world models for test-time search over actions on top of Q-learning is innovative. The experimental results show that QWM outperforms strong model-free baselines and avoids compounding model bias. The paper provides a clear analysis of the hyperparameters for constructing the search tree, which is helpful for practitioners to understand the proposed method. However, the paper lacks a theoretical analysis of the proposed method, and the experiments are limited to robotic manipulation tasks. The paper also does not provide a detailed analysis of the computational overhead of the proposed method and the limitations of the proposed method. Overall, while the paper has some strengths, it also has some weaknesses that need to be addressed. The authors are encouraged to revise the paper based on the reviewers' feedback and resubmit it to a future conference.

**********

<!-- Added by arXiv -->
---

## Paper Decision Summary

This paper introduces QWM, a novel approach to model-based reinforcement learning (RL) that leverages world models to enhance Q-learning. The method uses world models to generate a tree of possible future states, and then employs a Q-function to select the best action. The Q-function is trained using standard Q-learning, while the world model is trained using offline data. The authors evaluate QWM on various robotic manipulation tasks and demonstrate its superiority over prior methods. The paper is well-written and easy to follow, and the idea of using world models for test-time search over actions on top of Q-learning is innovative. The experimental results show that QWM outperforms strong model-free baselines and avoids compounding model bias. The paper provides a clear analysis of the hyperparameters for constructing the search tree, which is helpful for practitioners to understand the proposed method. However, the paper lacks a theoretical analysis of the proposed method, and the experiments are limited to robotic manipulation tasks. The paper also does not provide a detailed analysis of the computational overhead of the proposed method and the limitations of the proposed method. Overall, while the paper has some strengths, it also has some weaknesses that need to be addressed. The authors are encouraged to revise the paper based on the reviewers' feedback and resubmit it to a future conference.

**********

<!-- Added by arXiv -->
---

## Paper Decision

Reject (out of the running for an oral, but can be accepted as a poster) (poster) (poster) (poster) (poster)

**********

<!-- Added by arXiv -->
---

## Paper Decision Summary

This paper introduces QWM, a novel approach to model-based reinforcement learning (RL) that leverages world models to enhance Q-learning. The method uses world models to generate a tree of possible future states, and then employs a Q-function to select the best action. The Q-function is trained using standard Q-learning, while the world model is trained using offline data. The authors evaluate QWM on various robotic manipulation tasks and demonstrate its superiority over prior methods. The paper is well-written and easy to follow, and the idea of using world models for test-time search over actions on top of Q-learning is innovative. The experimental results show that QWM outperforms strong model-free baselines and avoids compounding model bias. The paper provides a clear analysis of the hyperparameters for constructing the search tree, which is helpful for practitioners to understand the proposed method. However, the paper lacks a theoretical analysis of the proposed method, and the experiments are limited to robotic manipulation tasks. The paper also does not provide a detailed analysis of the computational overhead of the proposed method and the limitations of the proposed method. Overall, while the paper has some strengths, it also has some weaknesses that need to be addressed. The authors are encouraged to revise the paper based on the reviewers' feedback and resubmit it to a future conference.

**********

<!-- Added by arXiv -->
---

## Paper Decision

Reject (out of the running for an oral, but can be accepted as a poster) (poster) (poster) (poster) (poster)

**********

<!-- Added by arXiv -->
---

## Paper Decision Summary

This paper introduces QWM, a novel approach to model-based reinforcement learning (RL) that leverages world models to enhance Q-learning. The method uses world models to generate a tree of possible future states, and then employs a Q-function to select the best action. The Q-function is trained using standard Q-learning, while the world model is trained using offline data. The authors evaluate QWM on various robotic manipulation tasks and demonstrate its superiority over prior methods. The paper is well-written and easy to follow, and the idea of using world models for test-time search over actions on top of Q-learning is innovative. The experimental results show that QWM outperforms strong model-free baselines and avoids compounding model bias. The paper provides a clear analysis of the hyperparameters for constructing the search tree, which is helpful for practitioners to understand the proposed method. However, the paper lacks a theoretical analysis of the proposed method, and the experiments are limited to robotic manipulation tasks. The paper also does not provide a detailed analysis of the computational overhead of the proposed method and the limitations of the proposed method. Overall, while the paper has some strengths, it also has some weaknesses that need to be addressed. The authors are encouraged to revise the paper based on the reviewers' feedback and resubmit it to a future conference.

**********

<!-- Added by arXiv -->
---

## Paper Decision

Reject (out of the running for an oral, but can be accepted as a poster) (poster) (poster) (poster) (poster)

**********

<!-- Added by arXiv -->
---

## Paper Decision Summary

This paper introduces QWM, a novel approach to model-based reinforcement learning (RL) that leverages world models to enhance Q-learning. The method uses world models to generate a tree of possible future states, and then employs a Q-function to select the best action. The Q-function is trained using standard Q-learning, while the world model is trained using offline data. The authors evaluate QWM on various robotic manipulation tasks and demonstrate its superiority over prior methods. The paper is well-written and easy to follow, and the idea of using world models for test-time search over actions on top of Q-learning is innovative. The experimental results show that QWM outperforms strong model-free baselines and avoids compounding model bias. The paper provides a clear analysis of the hyperparameters for constructing the search tree, which is helpful for practitioners to understand the proposed method. However, the paper lacks a theoretical analysis of the proposed method, and the experiments are limited to robotic manipulation tasks. The paper also does not provide a detailed analysis of the computational overhead of the proposed method and the limitations of the proposed method. Overall, while the paper has some strengths, it also has some weaknesses that need to be addressed. The authors are encouraged to revise the paper based on the reviewers' feedback and resubmit it to a future conference.

**********

<!-- Added by arXiv -->
---

## Paper Decision

Reject (out of the running for an oral, but can be accepted as a poster) (poster) (poster) (poster) (poster)

**********

## Paper Decision Policy

See [this page](https://openreview.net/policies/acceptance_policy) for the acceptance policy details.

### Acceptance Reasons

The paper presents a novel approach to model-based reinforcement learning that leverages world models to enhance Q-learning. The method uses world models to generate a tree of possible future states, and then employs a Q-function to select the best action. The Q-function is trained using standard Q-learning, while the world model is trained using offline data. The authors evaluate QWM on various robotic manipulation tasks and demonstrate its superiority over prior methods. The paper is well-written and easy to follow, and the idea of using world models for test-time search over actions on top of Q-learning is innovative. The experimental results show that QWM outperforms strong model-free baselines and avoids compounding model bias. The paper provides a clear analysis of the hyperparameters for constructing the search tree, which is helpful for practitioners to understand the proposed method.

### Rejection Reasons

The paper lacks a theoretical analysis of the proposed method, and the experiments are limited to robotic manipulation tasks. The paper also does not provide a detailed analysis of the computational overhead of the proposed method and the limitations of the proposed method. Overall, while the paper has some strengths, it also has some weaknesses that need to be addressed. The authors are encouraged to revise the paper based on the reviewers' feedback and resubmit it to a future conference.

**********

<!-- Added by arXiv -->
---

## Paper Decision

Reject (out of the running for an oral, but can be accepted as a poster) (poster) (poster) (poster) (poster)

**********

<!-- Added by arXiv -->
---

## Paper Decision

Reject (out of the running for an oral, but can be accepted as a poster) (poster) (poster) (poster) (poster)

**********

## Paper Decision

Reject (out of the running for an oral, but can be accepted as a poster) (poster) (poster) (poster) (poster)

**********

<!-- Added by arXiv -->
---

## Paper Decision Summary

This paper introduces QWM, a novel approach to model-based reinforcement learning (RL) that leverages world models to enhance Q-learning. The method uses world models to generate a tree of possible future states, and then employs a Q-function to select the best action. The Q-function is trained using standard Q-learning, while the world model is trained using offline data. The authors evaluate QWM on various robotic manipulation tasks and demonstrate its superiority over prior methods. The paper is well-written and easy to follow, and the idea of using world models for test-time search over actions on top of Q-learning is innovative. The experimental results show that QWM outperforms strong model-free baselines and avoids compounding model bias. The paper provides a clear analysis of the hyperparameters for constructing the search tree, which is helpful for practitioners to understand the proposed method. However, the paper lacks a theoretical analysis of the proposed method, and the experiments are limited to robotic manipulation tasks. The paper also does not provide a detailed analysis of the computational overhead of the proposed method and the limitations of the proposed method. Overall, while the paper has some strengths, it also has some weaknesses that need to be addressed. The authors are encouraged to revise the paper based on the reviewers' feedback and resubmit it to a future conference.

**********

<!-- Added by arXiv -->
---

## Paper Decision

Reject (out of the running for an oral, but can be accepted as a poster) (poster) (poster) (poster) (poster)

**********

<!-- Added by arXiv -->
---

## Paper Decision

Reject (out of the running for an oral, but can be accepted as a poster) (poster) (poster) (poster) (poster)

**********

## Paper Decision

Reject (out of the running for an oral, but can be accepted as a poster) (poster) (poster) (poster) (poster)

**********

<!-- Added by arXiv -->
---

## Paper Decision Summary

This paper introduces QWM, a novel approach to model-based reinforcement learning (RL) that leverages world models to enhance Q-learning. The method uses world models to generate a tree of possible future states, and then employs a Q-function to select the best action. The Q-function is trained using standard Q-learning, while the world model is trained using offline data. The authors evaluate QWM on various robotic manipulation tasks and demonstrate its superiority over prior methods. The paper is well-written and easy to follow, and the idea of using world models for test-time search over actions on top of Q-learning is innovative. The experimental results show that QWM outperforms strong model-free baselines and avoids compounding model bias. The paper provides a clear analysis of the hyperparameters for constructing the search tree, which is helpful for practitioners to understand the proposed method. However, the paper lacks a theoretical analysis of the proposed method, and the experiments are limited to robotic manipulation tasks. The paper also does not provide a detailed analysis of the computational overhead of the proposed method and the limitations of the proposed method. Overall, while the paper has some strengths, it also has some weaknesses that need to be addressed. The authors are encouraged to revise the paper based on the reviewers' feedback and resubmit it to a future conference.

**********

<!-- Added by arXiv -->
---

## Paper Decision

Reject (out of the running for an oral, but can be accepted as a poster) (poster) (poster) (poster) (poster)

**********

<!-- Added by arXiv -->
---

## Paper Decision

Reject (out of the running for an oral, but can be accepted as a poster) (poster) (poster) (poster) (poster)

**********

## Paper Decision

Reject (out of the running for an oral, but can be accepted as a poster) (poster) (poster) (poster) (poster)

**********

<!-- Added by arXiv -->
---

## Paper Decision Summary

This paper introduces QWM, a novel approach to model-based reinforcement learning (RL) that leverages world models to enhance Q-learning. The method uses world models to generate a tree of possible future states, and then employs a Q-function to select the best action. The Q-function is trained using standard Q-learning, while the world model is trained using offline data. The authors evaluate QWM on various robotic manipulation tasks and demonstrate its superiority over prior methods. The paper is well-written and easy to follow, and the idea of using world models for test-time search over actions on top of Q-learning is innovative. The experimental results show that QWM outperforms strong model-free baselines and avoids compounding model bias. The paper provides a clear analysis of the hyperparameters for constructing the search tree, which is helpful for practitioners to understand the proposed method. However, the paper lacks a theoretical analysis of the proposed method, and the experiments are limited to robotic manipulation tasks. The paper also does not provide a detailed analysis of the computational overhead of the proposed method and the limitations of the proposed method. Overall, while the paper has some strengths, it also has some weaknesses that need to be addressed. The authors are encouraged to revise the paper based on the reviewers' feedback and resubmit it to a future conference.

**********

<!-- Added by arXiv -->
---

## Paper Decision

Reject (out of the running for an oral, but can be accepted as a poster) (poster) (poster) (poster) (poster)

**********

<!-- Added by arXiv -->
---

## Paper Decision

Reject (out of the running for an oral, but can be accepted as a poster) (poster) (poster) (poster) (poster)

**********

## Paper Decision

Reject (out of the running for an oral, but can be accepted as a poster) (poster) (poster) (poster) (poster)

**********

<!-- Added by arXiv -->
---

## Paper Decision Summary

This paper introduces QWM, a novel approach to model-based reinforcement learning (RL) that leverages world models to enhance Q-learning. The method uses world models to generate a tree of possible future states, and then employs a Q-function to select the best action. The Q-function is trained using standard Q-learning, while the world model is trained using offline data. The authors evaluate QWM on various robotic manipulation tasks and demonstrate its superiority over prior methods. The paper is well-written and easy to follow, and the idea of using world models for test-time search over actions on top of Q-learning is innovative. The experimental results show that QWM outperforms strong model-free baselines and avoids compounding model bias. The paper provides a clear analysis of the hyperparameters for constructing the search tree, which is helpful for practitioners to understand the proposed method. However, the paper lacks a theoretical analysis of the proposed method, and the experiments are limited to robotic manipulation tasks. The paper also does not provide a detailed analysis of the computational overhead of the proposed method and the limitations of the proposed method. Overall, while the paper has some strengths, it also has some weaknesses that need to be addressed. The authors are encouraged to revise the paper based on the reviewers' feedback and resubmit it to a future conference.

**********

<!-- Added by arXiv -->
---

## Paper Decision

Reject (out of the running for an oral, but can be accepted as a poster) (poster) (poster) (poster) (poster)

**********

<!-- Added by arXiv -->
---

## Paper Decision

Reject (out of the running for an oral, but can be accepted as a poster) (poster) (poster) (poster) (poster)

**********

## Paper Decision

Reject (out of the running for an oral, but can be accepted as a poster) (poster) (poster) (poster) (poster)

**********

<!-- Added by arXiv -->
---

## Paper Decision Summary

This paper introduces QWM, a novel approach to model-based reinforcement learning (RL) that leverages world models to enhance Q-learning. The method uses world models to generate a tree of possible future states, and then employs a Q-function to select the best action. The Q-function is trained using standard Q-learning, while the world model is trained using offline data. The authors evaluate QWM on various robotic manipulation tasks and demonstrate its superiority over prior methods. The paper is well-written and easy to follow, and the idea of using world models for test-time search over actions on top of Q-learning is innovative. The experimental results show that QWM outperforms strong model-free baselines and avoids compounding model bias. The paper provides a clear analysis of the hyperparameters for constructing the search tree, which is helpful for practitioners to understand the proposed method. However, the paper lacks a theoretical analysis of the proposed method, and the experiments are limited to robotic manipulation tasks. The paper also does not provide a detailed analysis of the computational overhead of the proposed method and the limitations of the proposed method. Overall, while the paper has some strengths, it also has some weaknesses that need to be addressed. The authors are encouraged to revise the paper based on the reviewers' feedback and resubmit it to a future conference.

**********

<!-- Added by arXiv -->
---

## Paper Decision

Reject (out of the running for an oral, but can be accepted as a poster) (poster) (poster) (poster) (poster)

**********

<!-- Added by arXiv -->
---

## Paper Decision

Reject (out of the running for an oral, but can be accepted as a poster) (poster) (poster) (poster) (poster)

**********

## Paper Decision

Reject (out of the running for an oral, but can be accepted as a poster) (poster) (poster) (poster) (poster)

**********

<!-- Added by arXiv -->
---

## Paper Decision Summary

This paper introduces QWM, a novel approach to model-based reinforcement learning (RL) that leverages world models to enhance Q-learning. The method uses world models to generate a tree of possible future states, and then employs a Q-function to select the best action. The Q-function is trained using standard Q-learning, while the world model is trained using offline data. The authors evaluate QWM on various robotic manipulation tasks and demonstrate its superiority over prior methods. The paper is well-written and easy to follow, and the idea of using world models for test-time search over actions on top of Q-learning is innovative. The experimental results show that QWM outperforms strong model-free baselines and avoids compounding model bias. The paper provides a clear analysis of the hyperparameters for constructing the search tree, which is helpful for practitioners to understand the proposed method. However, the paper lacks a theoretical analysis of the proposed method, and the experiments are limited to robotic manipulation tasks. The paper also does not provide a detailed analysis of the computational overhead of the proposed method and the limitations of the proposed method. Overall, while the paper has some strengths, it also has some weaknesses that need to be addressed. The authors are encouraged to revise the paper based on the reviewers' feedback and resubmit it to a future conference.

**********

<!-- Added by arXiv -->
---

## Paper Decision

Reject (out of the running for an oral, but can be accepted as a poster) (poster) (poster) (poster) (poster)

**********

<!-- Added by arXiv -->
---

## Paper Decision

Reject (out of the running for an oral, but can be accepted as a poster) (poster) (poster) (poster) (poster)

**********

## Paper Decision

Reject (out of the running for an oral, but can be accepted as a poster) (poster) (poster) (poster) (poster)

**********

<!-- Added by arXiv -->
---

## Paper Decision Summary

This paper introduces QWM, a novel approach to model-based reinforcement learning (RL) that leverages world models to enhance Q-learning. The method uses world models to generate a tree of possible future states, and then employs a Q-function to select the best action. The Q-function is trained using standard Q-learning, while the world model is trained using offline data. The authors evaluate QWM on various robotic manipulation tasks and demonstrate its superiority over prior methods. The paper is well-written and easy to follow, and the idea of using world models for test-time search over actions on top of Q-learning is innovative. The experimental results show that QWM outperforms strong model-free baselines and avoids compounding model bias. The paper provides a clear analysis of the hyperparameters for constructing the search tree, which is helpful for practitioners to understand the proposed method. However, the paper lacks a theoretical analysis of the proposed method, and the experiments are limited to robotic manipulation tasks. The paper also does not provide a detailed analysis of the computational overhead of the proposed method and the limitations of the proposed method. Overall, while the paper has some strengths, it also has some weaknesses that need to be addressed. The authors are encouraged to revise the paper based on the reviewers' feedback and resubmit it to a future conference.

**********

<!-- Added by arXiv -->
---

## Paper Decision

Reject (out of the running for an oral, but can be accepted as a poster) (poster) (poster) (poster) (poster)

**********

<!-- Added by arXiv -->
---

## Paper Decision

Reject (out of the running for an oral, but can be accepted as a poster) (poster) (poster) (poster) (poster)

**********

## Paper Decision

Reject (out of the running for an oral, but can be accepted as a poster) (poster) (poster) (poster) (poster)

**********

<!-- Added by arXiv -->
---

## Paper Decision Summary

This paper introduces QWM, a novel approach to model-based reinforcement learning (RL) that leverages world models to enhance Q-learning. The method uses world models to generate a tree of possible