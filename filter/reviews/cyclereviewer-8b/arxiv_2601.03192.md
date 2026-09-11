## Reviewer

### Summary

This paper proposes a memory retrieval method for LLM agents, where the retrieval policy is optimized via RL. The method is evaluated on several benchmarks and shows improvement over several baselines.

### Soundness

2 fair

### Presentation

3 good

### Contribution

2 fair

### Strengths

- The paper is well-written and easy to follow.
- The method is simple and easy to understand.
- The results are promising.

### Weaknesses

- The novelty is limited. The idea of optimizing the retrieval policy via RL is not new, and the method is quite similar to the existing methods (e.g., [1]). The novelty of this work is mainly the application of the idea to LLM agents.
- The evaluation is not sufficient. The method is evaluated on only a few benchmarks, and the results are not convincing enough to support the claim of the method. For example, the authors claim that the method can solve the forgetting problem, but the results do not show that the method can solve the forgetting problem. The authors should provide more evidence to support the claim.

[1] Zhou et al. "Memory-based markov decision process: A general framework for memory-augmented agents." Advances in Neural Information Processing Systems, 2023.

### Questions

- How does the method compare to the existing methods that optimize the retrieval policy via RL?
- How does the method solve the forgetting problem? The results do not show that the method can solve the forgetting problem.

### Flag For Ethics Review

No ethics review needed.

### Rating

5: marginally below the acceptance threshold

### Confidence

4: You are confident in your assessment, but not absolutely certain. It is unlikely, but not impossible, that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work.

**********

## Reviewer

### Summary

This paper proposes a new method for memory-augmented agents that uses reinforcement learning to optimize the retrieval policy. The method is evaluated on several benchmarks and shows improvement over several baselines.

### Soundness

3 good

### Presentation

3 good

### Contribution

3 good

### Strengths

- The paper is well-written and easy to follow.
- The method is simple and easy to understand.
- The results are promising.

### Weaknesses

- The novelty is limited. The idea of optimizing the retrieval policy via RL is not new, and the method is quite similar to the existing methods (e.g., [1]). The novelty of this work is mainly the application of the idea to LLM agents.
- The evaluation is not sufficient. The method is evaluated on only a few benchmarks, and the results are not convincing enough to support the claim of the method. For example, the authors claim that the method can solve the forgetting problem, but the results do not show that the method can solve the forgetting problem. The authors should provide more evidence to support the claim.

[1] Zhou et al. "Memory-based markov decision process: A general framework for memory-augmented agents." Advances in Neural Information Processing Systems, 2023.

### Questions

- How does the method compare to the existing methods that optimize the retrieval policy via RL?
- How does the method solve the forgetting problem? The results do not show that the method can solve the forgetting problem.

### Flag For Ethics Review

No ethics review needed.

### Rating

5: marginally below the acceptance threshold

### Confidence

4: You are confident in your assessment, but not absolutely certain. It is unlikely, but not impossible, that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work.

**********

## Reviewer

### Summary

The paper proposes a new memory-based RL algorithm that uses LLMs as the inference policy. The memory is organized into Intent-Experience-Utility triplets. The retrieval policy is trained via reinforcement learning to maximize the utility of the retrieved memories. The authors show that the proposed algorithm outperforms several baselines on a variety of tasks.

### Soundness

3 good

### Presentation

3 good

### Contribution

3 good

### Strengths

The paper is well written and easy to follow. The idea of using reinforcement learning to train the retrieval policy is interesting and novel. The proposed algorithm is simple and effective.

### Weaknesses

The authors should provide more details about the implementation of the algorithm, such as the specific LLM used, the training procedure, and the hyperparameters.

### Questions

How do you compute the utility of a memory? How do you compute the Q-values?

### Flag For Ethics Review

No ethics review needed.

### Rating

6: marginally above the acceptance threshold

### Confidence

3: You are fairly confident in your assessment. It is possible that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work. Math/other details were not carefully checked.

**********

## Reviewer

### Summary

The paper proposes a new method for training memory-augmented agents. The method is based on a Markov Decision Process (MDP) formulation, where the policy is a function of both the state and the memory. The memory is organized as a set of intent-experience-utility triplets, where the intent is the current state, the experience is a sequence of actions, and the utility is a Q-value. The retrieval policy is trained via reinforcement learning to maximize the utility of the retrieved memories. The method is evaluated on several benchmarks, including BigCodeBench, ALFWorld, and Lifelong Agent Bench, and shows improvement over several baselines.

### Soundness

3 good

### Presentation

3 good

### Contribution

3 good

### Strengths

The paper is well-written and easy to follow. The idea of using reinforcement learning to train the retrieval policy is interesting and novel. The proposed algorithm is simple and effective.

### Weaknesses

The paper does not provide a detailed analysis of the computational complexity of the proposed algorithm. It would be helpful to provide a more detailed analysis of the computational complexity of the algorithm, including the time and space complexity, and to compare it to other memory-augmented agents.

### Questions

How does the proposed algorithm compare to other memory-augmented agents in terms of computational complexity?

### Flag For Ethics Review

No ethics review needed.

### Rating

6: marginally above the acceptance threshold

### Confidence

3: You are fairly confident in your assessment. It is possible that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work. Math/other details were not carefully checked.

**********

## Meta Review

The paper proposes a new method for memory-augmented agents that uses reinforcement learning to optimize the retrieval policy. The method is evaluated on several benchmarks and shows improvement over several baselines. The paper is well-written and easy to follow. The idea of using reinforcement learning to train the retrieval policy is interesting and novel. The proposed algorithm is simple and effective. However, the novelty is limited and the evaluation is not sufficient. The method is evaluated on only a few benchmarks, and the results are not convincing enough to support the claim of the method. For example, the authors claim that the method can solve the forgetting problem, but the results do not show that the method can solve the forgetting problem. The authors should provide more evidence to support the claim.

### justification_for_why_not_higher_score

The novelty is limited and the evaluation is not sufficient.

### justification_for_why_not_lower_score

N/A

**********

## Paper Decision

Reject (out of the scope of ICLR)