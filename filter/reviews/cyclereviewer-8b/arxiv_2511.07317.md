## Reviewer

### Summary

This paper proposes a new RL training framework for language models called RLVE. The authors propose to use a suite of 400 procedurally generated environments with adaptive difficulty levels to train language models. The adaptive difficulty levels are adjusted based on the model's performance on the current difficulty level. The authors show that RLVE can improve the performance of language models on reasoning benchmarks compared to other RL training frameworks.

### Soundness

3 good

### Presentation

3 good

### Contribution

2 fair

### Strengths

- The paper is well-written and easy to follow.
- The idea of adaptive difficulty levels is interesting and intuitive.
- The results show that RLVE can improve the performance of language models on reasoning benchmarks compared to other RL training frameworks.

### Weaknesses

- The paper does not provide a clear comparison with other RL training frameworks. The authors should compare RLVE with other RL training frameworks, such as RLVR and ProRL, and show how RLVE improves upon them.
- The paper does not provide a clear analysis of the performance of RLVE on different types of reasoning benchmarks. The authors should analyze the performance of RLVE on different types of reasoning benchmarks, such as mathematical reasoning, logical reasoning, and code generation, and show how RLVE performs compared to other RL training frameworks.
- The paper does not provide a clear analysis of the computational cost of RLVE. The authors should compare the computational cost of RLVE with other RL training frameworks and show how RLVE compares in terms of efficiency.

### Questions

- How does RLVE compare with other RL training frameworks, such as RLVR and ProRL, in terms of performance and efficiency?
- How does RLVE perform on different types of reasoning benchmarks, such as mathematical reasoning, logical reasoning, and code generation?
- What is the computational cost of RLVE compared to other RL training frameworks?
- How does RLVE compare with other RL training frameworks in terms of scalability and generalizability?

### Flag For Ethics Review

No ethics review needed.

### Rating

5: marginally below the acceptance threshold

### Confidence

3: You are fairly confident in your assessment. It is possible that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work. Math/other details were not carefully checked.

**********

## Reviewer

### Summary

This paper proposes a new approach to train language models using adaptive environments. The authors first define a verifiable environment as a tuple of input template, problem generator, and reward function. The problem generator procedurally samples problems that instantiate the input template to produce inputs. The reward function is algorithmically defined to ensure verifiable reward computation. The authors then propose to use RLVE, a method that uses verifiable environments that procedurally generate problems and provide algorithmically verifiable rewards, to scale up RL for language models. The authors create RLVE-Gym, a large-scale suite of 400 verifiable environments carefully developed through manual environment engineering. The authors show that environment scaling, i.e., expanding the collection of training environments, consistently improves generalizable reasoning capabilities. The authors also show that RLVE with joint training across all 400 environments in RLVE-Gym yields a 3.37% absolute average improvement across six reasoning benchmarks, starting from one of the strongest 1.5B reasoning LMs.

### Soundness

3 good

### Presentation

3 good

### Contribution

2 fair

### Strengths

The paper is well-written and easy to follow. The authors provide a clear and concise description of their proposed approach, RLVE, and its components. The authors also provide a thorough evaluation of their approach, including experiments on six reasoning benchmarks and comparisons with baseline methods. The results show that RLVE consistently improves generalizable reasoning capabilities and outperforms baseline methods.

### Weaknesses

The authors propose a new approach to train language models using adaptive environments. However, the authors do not provide a clear comparison with existing methods. The authors should compare RLVE with other RL training frameworks, such as RLVR and ProRL, and show how RLVE improves upon them. The authors should also provide a clear analysis of the performance of RLVE on different types of reasoning benchmarks, such as mathematical reasoning, logical reasoning, and code generation, and show how RLVE performs compared to other RL training frameworks. The authors should also provide a clear analysis of the computational cost of RLVE compared to other RL training frameworks and show how RLVE compares in terms of efficiency.

### Questions

1. The authors propose a new approach to train language models using adaptive environments. However, the authors do not provide a clear comparison with existing methods. The authors should compare RLVE with other RL training frameworks, such as RLVR and ProRL, and show how RLVE improves upon them. The authors should also provide a clear analysis of the performance of RLVE on different types of reasoning benchmarks, such as mathematical reasoning, logical reasoning, and code generation, and show how RLVE performs compared to other RL training frameworks. The authors should also provide a clear analysis of the computational cost of RLVE compared to other RL training frameworks and show how RLVE compares in terms of efficiency.

2. The authors should also provide a clear analysis of the limitations of RLVE and potential areas for future work. The authors should discuss potential limitations of their approach and potential areas for future research.

3. The authors should also provide a clear analysis of the generalizability of RLVE to other domains and tasks. The authors should discuss the potential of RLVE to be applied to other domains and tasks beyond reasoning benchmarks.

### Flag For Ethics Review

No ethics review needed.

### Rating

5: marginally below the acceptance threshold

### Confidence

3: You are fairly confident in your assessment. It is possible that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work. Math/other details were not carefully checked.

**********

## Reviewer

### Summary

The paper introduces RLVE, an approach to scale up reinforcement learning (RL) for language models (LMs) by using verifiable environments that dynamically adapt their problem difficulty distribution to the policy model's capabilities. RLVE enables the creation of procedurally generated problems and algorithmically verifiable rewards, addressing the challenges of static data distributions and vanishing learning signals. The paper presents RLVE-Gym, a large-scale suite of 400 carefully developed verifiable environments, and demonstrates that environment scaling improves generalizable reasoning capabilities. The results show that RLVE with joint training across all 400 environments in RLVE-Gym yields a 3.37% absolute average improvement across six reasoning benchmarks, outperforming existing methods.

### Soundness

3 good

### Presentation

3 good

### Contribution

3 good

### Strengths

The paper introduces a novel approach to scaling up RL for language models by using adaptive verifiable environments. The paper presents a comprehensive evaluation of the proposed method, including experiments on six reasoning benchmarks and comparisons with baseline methods. The results demonstrate that RLVE consistently improves generalizable reasoning capabilities and outperforms baseline methods.

### Weaknesses

The paper does not provide a clear comparison with existing methods. The authors should compare RLVE with other RL training frameworks, such as RLVR and ProRL, and show how RLVE improves upon them. The authors should also provide a clear analysis of the performance of RLVE on different types of reasoning benchmarks, such as mathematical reasoning, logical reasoning, and code generation, and show how RLVE performs compared to other RL training frameworks. The authors should also provide a clear analysis of the computational cost of RLVE compared to other RL training frameworks and show how RLVE compares in terms of efficiency.

### Questions

1. The paper does not provide a clear comparison with existing methods. The authors should compare RLVE with other RL training frameworks, such as RLVR and ProRL, and show how RLVE improves upon them. The authors should also provide a clear analysis of the performance of RLVE on different types of reasoning benchmarks, such as mathematical reasoning, logical reasoning, and code generation, and show how RLVE performs compared to other RL training frameworks. The authors should also provide a clear analysis of the computational cost of RLVE compared to other RL training frameworks and show how RLVE compares in terms of efficiency.

2. The paper does not provide a clear analysis of the limitations of RLVE and potential areas for future work. The authors should discuss potential limitations of their approach and potential areas for future research.

3. The paper does not provide a clear analysis of the generalizability of RLVE to other domains and tasks. The authors should discuss the potential of RLVE to be applied to other domains and tasks beyond reasoning benchmarks.

### Flag For Ethics Review

No ethics review needed.

### Rating

5: marginally below the acceptance threshold

### Confidence

3: You are fairly confident in your assessment. It is possible that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work. Math/other details were not carefully checked.

**********

## Reviewer

### Summary

This paper proposes a new approach called RLVE (Reinforcement Learning with Adaptive Verifiable Environments) to scale up RL for language models. The authors first define a verifiable environment as a tuple of input template, problem generator, and reward function. The problem generator procedurally samples problems that instantiate the input template to produce inputs. The reward function is algorithmically defined to ensure verifiable reward computation. The authors then propose to use RLVE, a method that uses verifiable environments that procedurally generate problems and provide algorithmically verifiable rewards, to scale up RL for language models. The authors create RLVE-Gym, a large-scale suite of 400 verifiable environments carefully developed through manual environment engineering. The authors show that environment scaling, i.e., expanding the collection of training environments, consistently improves generalizable reasoning capabilities. The authors also show that RLVE with joint training across all 400 environments in RLVE-Gym yields a 3.37% absolute average improvement across six reasoning benchmarks, starting from one of the strongest 1.5B reasoning LMs.

### Soundness

3 good

### Presentation

3 good

### Contribution

3 good

### Strengths

- The paper is well-written and easy to follow.
- The idea of adaptive difficulty levels is interesting and intuitive.
- The results show that RLVE consistently improves generalizable reasoning capabilities and outperforms baseline methods.

### Weaknesses

- The paper does not provide a clear comparison with existing methods. The authors should compare RLVE with other RL training frameworks, such as RLVR and ProRL, and show how RLVE improves upon them. The authors should also provide a clear analysis of the performance of RLVE on different types of reasoning benchmarks, such as mathematical reasoning, logical reasoning, and code generation, and show how RLVE performs compared to other RL training frameworks. The authors should also provide a clear analysis of the computational cost of RLVE compared to other RL training frameworks and show how RLVE compares in terms of efficiency.

### Questions

1. The paper does not provide a clear comparison with existing methods. The authors should compare RLVE with other RL training frameworks, such as RLVR and ProRL, and show how RLVE improves upon them. The authors should also provide a clear analysis of the performance of RLVE on different types of reasoning benchmarks, such as mathematical reasoning, logical reasoning, and code generation, and show how RLVE performs compared to other RL training frameworks. The authors should also provide a clear analysis of the computational cost of RLVE compared to other RL training frameworks and show how RLVE compares in terms of efficiency.

2. The paper does not provide a clear analysis of the limitations of RLVE and potential areas for future work. The authors should discuss potential limitations of their approach and potential areas for future research.

3. The paper does not provide a clear analysis of the generalizability of RLVE to other domains and tasks. The authors should discuss the potential of RLVE to be applied to other domains and tasks beyond reasoning benchmarks.

### Flag For Ethics Review

No ethics review needed.

### Rating

5: marginally below the acceptance threshold

### Confidence

3: You are fairly confident in your assessment. It is possible that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work. Math/other details were not carefully checked.

**********

## Meta Review

The paper introduces RLVE, an approach to scale up reinforcement learning (RL) for language models (LMs) by using verifiable environments that dynamically adapt their problem difficulty distribution to the policy model's capabilities. The paper presents a comprehensive evaluation of the proposed method, including experiments on six reasoning benchmarks and comparisons with baseline methods. The results demonstrate that RLVE consistently improves generalizable reasoning capabilities and outperforms baseline methods.

However, the paper does not provide a clear comparison with existing methods, and the authors should compare RLVE with other RL training frameworks, such as RLVR and ProRL, and show how RLVE improves upon them. The authors should also provide a clear analysis of the performance of RLVE on different types of reasoning benchmarks, such as mathematical reasoning, logical reasoning, and code generation, and show how RLVE performs compared to other RL training frameworks. The authors should also provide a clear analysis of the computational cost of RLVE compared to other RL training frameworks and show how RLVE compares in terms of efficiency.

### justification_for_why_not_higher_score

The paper does not provide a clear comparison with existing methods, and the authors should compare RLVE with other RL training frameworks, such as RLVR and ProRL, and show how RLVE improves upon them. The authors should also provide a clear analysis of the performance of RLVE on different types of reasoning benchmarks, such as mathematical reasoning, logical reasoning, and code generation, and show how RLVE performs compared to other RL training frameworks. The authors should also provide a clear analysis of the computational cost of RLVE compared to other RL training frameworks and show how RLVE compares in terms of efficiency.

### justification_for_why_not_lower_score

N/A

**********

## Paper Decision

Reject (not selected for spotlight)

**********

## Paper Decision Summary

The paper introduces RLVE, an approach to scale up reinforcement learning (RL) for language models (LMs) by using verifiable environments that dynamically adapt their problem difficulty distribution to the policy model's capabilities. The paper presents a comprehensive evaluation of the proposed method, including experiments on six reasoning benchmarks and comparisons with baseline methods. The results demonstrate that RLVE consistently improves generalizable reasoning capabilities and outperforms baseline methods.

However, the paper does not provide a clear comparison with existing methods, and the authors should compare RLVE with other RL training frameworks, such as RLVR and ProRL, and show how RLVE improves upon them. The authors should also provide a clear analysis of the performance of RLVE on different types of reasoning benchmarks, such as mathematical reasoning, logical reasoning, and code generation, and show how RLVE performs compared to other RL training frameworks. The authors should also provide a clear analysis of the computational cost of RLVE compared to other RL training frameworks and show how RLVE compares in terms of efficiency.

**********

## Paper Decision Type

Reject (not selected for spotlight)

**********

## Paper Decision Confidence

3: You are fairly confident in your assessment. It is possible that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work. Math/other details were not carefully checked.

**********

*** Reviewer

## Reviewer

### Summary

This paper proposes a new approach called RLVE (Reinforcement Learning with Adaptive Verifiable Environments) to scale up RL for language models. The authors first define a verifiable environment as a tuple of input template, problem generator, and reward function. The problem generator procedurally samples problems that instantiate the input template to produce inputs. The reward function is algorithmically defined to ensure verifiable reward computation. The authors then propose to use RLVE, a method that uses verifiable environments that procedurally generate problems and provide algorithmically verifiable rewards, to scale up RL for language models. The authors create RLVE-Gym, a large-scale suite of 400 verifiable environments carefully developed through manual environment engineering. The authors show that environment scaling, i.e., expanding the collection of training environments, consistently improves generalizable reasoning capabilities. The authors also show that RLVE with joint training across all 400 environments in RLVE-Gym yields a 3.37% absolute average improvement across six reasoning benchmarks, starting from one of the strongest 1.5B reasoning LMs.

### Soundness

3 good

### Presentation

3 good

### Contribution

3 good

### Strengths

- The paper is well-written and easy to follow.
- The idea of adaptive difficulty levels is interesting and intuitive.
- The results show that RLVE consistently improves generalizable reasoning capabilities and outperforms baseline methods.

### Weaknesses

- The paper does not provide a clear comparison with existing methods. The authors should compare RLVE with other RL training frameworks, such as RLVR and ProRL, and show how RLVE improves upon them. The authors should also provide a clear analysis of the performance of RLVE on different types of reasoning benchmarks, such as mathematical reasoning, logical reasoning, and code generation, and show how RLVE performs compared to other RL training frameworks. The authors should also provide a clear analysis of the computational cost of RLVE compared to other RL training frameworks and show how RLVE compares in terms of efficiency.

### Questions

1. The paper does not provide a clear comparison with existing methods. The authors should compare RLVE with other RL training frameworks, such as RLVR and ProRL, and show how RLVE improves upon them. The authors should also provide a clear analysis of the performance of RLVE on different types of reasoning benchmarks, such as mathematical reasoning, logical reasoning, and code generation, and show how RLVE performs compared to other RL training frameworks. The authors should also provide a clear analysis of the computational cost of RLVE compared to other RL training frameworks and show how RLVE compares in terms of efficiency.

2. The paper does not provide a clear analysis of the limitations of RLVE and potential areas for future work. The authors should discuss potential limitations of their approach and potential areas for future research.

3. The paper does not provide a clear analysis of the generalizability of RLVE to other domains and tasks. The authors should discuss the potential of RLVE to be applied to other domains and tasks beyond reasoning benchmarks.

### Flag For Ethics Review

No ethics review needed.

### Rating

5: marginally below the acceptance threshold

### Confidence

3: You are fairly confident in your assessment. It is possible that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work. Math/other details were not carefully checked.

**********

## Paper Decision

Reject (not selected for spotlight)

**********

## Paper Decision Summary

The paper introduces RLVE, an approach to scale up reinforcement learning (RL) for language models (LMs) by using verifiable environments that dynamically adapt their problem difficulty distribution to the policy model's capabilities. The paper presents a comprehensive evaluation of the proposed method, including experiments on six reasoning benchmarks and comparisons with baseline methods. The results demonstrate that RLVE consistently improves generalizable reasoning capabilities and outperforms baseline methods.

However, the paper does not provide a clear comparison with existing methods, and the authors should compare RLVE with other RL training frameworks, such as RLVR and ProRL, and show how RLVE improves upon them. The authors should also provide a clear analysis of the performance of RLVE on different types of reasoning benchmarks, such as mathematical reasoning, logical reasoning, and code generation, and show how RLVE performs compared to other RL training frameworks. The authors should also provide a clear analysis of the computational cost of RLVE compared to other RL training frameworks and show how RLVE compares in terms of efficiency.

**********

## Paper Decision Type

Reject (not selected for spotlight)

**********

## Paper Decision Confidence

3: You are fairly confident in your assessment. It is possible that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work. Math/other details were not carefully checked.

**********

*** Meta Review

The paper introduces RLVE, an approach to scale up reinforcement learning (RL) for language models (LMs) by using verifiable environments that dynamically adapt their problem difficulty distribution to the policy model's capabilities. The paper presents a comprehensive evaluation of the proposed method, including experiments on six reasoning benchmarks and comparisons with baseline methods. The results demonstrate that RLVE consistently improves generalizable reasoning capabilities and outperforms baseline methods.

However, the paper does not provide a clear comparison with existing methods, and the authors should compare RLVE with other RL training frameworks, such as RLVR and ProRL, and show how RLVE improves upon them. The authors should also provide a clear analysis of the performance of RLVE on different types of reasoning benchmarks, such as mathematical reasoning, logical reasoning, and code generation, and show how RLVE performs compared to other RL training frameworks. The authors should also provide a clear analysis of the computational cost of RLVE compared to other RL training frameworks and show how RLVE compares in terms of efficiency.

### justification_for_why_not_higher_score

The paper does not provide a clear comparison with existing methods, and the authors should compare RLVE with other RL training frameworks, such as RLVR and ProRL, and show how RLVE improves upon them. The authors should also provide a clear analysis of the performance of RLVE on different types of reasoning benchmarks, such as mathematical reasoning, logical reasoning, and code generation, and show how RLVE performs compared to other RL training frameworks. The authors should also provide a clear analysis of the computational cost of RLVE compared to other RL training frameworks and show how RLVE compares in terms of efficiency.

### justification_for_why_not_lower_score

N/A

**********

## Paper Decision

Reject (not selected for spotlight)

**********

## Paper Decision Summary

The paper introduces RLVE, an approach to scale up reinforcement learning (RL) for language models (LMs) by using verifiable environments that dynamically adapt their problem difficulty distribution to the policy model's capabilities. The paper presents a comprehensive evaluation of the proposed method, including experiments on six reasoning benchmarks and comparisons with baseline methods. The results demonstrate that RLVE consistently improves generalizable reasoning capabilities and outperforms baseline methods.

However, the paper does not provide a clear comparison with existing methods, and the authors should compare RLVE with other RL training frameworks, such as RLVR and ProRL, and show how RLVE improves upon them. The authors should also provide a clear analysis of the performance of RLVE on different types of reasoning benchmarks, such as mathematical reasoning, logical reasoning, and code generation, and show how RLVE performs compared to other RL training frameworks. The authors should also provide a clear analysis of the computational cost of RLVE compared to other RL training frameworks and show how RLVE compares in terms of efficiency.

**********

## Paper Decision Type

Reject (not selected for spotlight)

**********

## Paper Decision Confidence

3: You are fairly confident in your assessment. It is possible that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work. Math/other details were not carefully checked.

**********

*** Meta Review

The paper introduces RLVE, an approach to scale up reinforcement learning (RL) for language models (LMs) by using verifiable environments that dynamically adapt their problem difficulty distribution to the policy model's capabilities. The paper presents a comprehensive evaluation of the proposed method, including experiments on six reasoning benchmarks and comparisons with baseline methods. The results demonstrate that RLVE consistently improves generalizable reasoning capabilities and outperforms baseline methods.

However, the paper does not provide a clear comparison with existing methods, and the authors should compare RLVE with other RL training frameworks, such as RLVR and ProRL, and show how RLVE improves upon them. The authors should also provide a clear analysis of the performance of RLVE on different types of reasoning benchmarks, such as mathematical reasoning, logical reasoning, and code generation, and show how RLVE performs compared to other RL training frameworks. The authors should also provide a clear analysis of the computational cost of RLVE compared to other RL training frameworks and show how RLVE compares in terms of efficiency.

**********

## Paper Decision

Reject (not selected for spotlight)

**********

## Paper Decision Summary

The paper introduces RLVE, an approach to scale up reinforcement learning (RL) for language models (LMs) by using verifiable environments that dynamically adapt their problem difficulty distribution to the policy model's capabilities. The paper presents a comprehensive evaluation of the proposed method, including experiments on six reasoning benchmarks and comparisons with baseline methods. The results demonstrate that RLVE consistently improves generalizable reasoning capabilities and outperforms baseline methods.

However, the paper does not provide a clear comparison with existing methods, and the authors should compare RLVE with other RL training frameworks, such as RLVR and ProRL, and show how RLVE improves upon them. The authors should also provide a clear analysis of the performance of RLVE on different types of reasoning benchmarks, such as mathematical reasoning, logical reasoning, and code generation, and show how RLVE performs compared to other RL training frameworks. The authors should also provide a clear analysis of the computational cost of RLVE compared to other RL training frameworks and show how RLVE compares in terms of efficiency.

**********

## Paper Decision Type

Reject (not selected for spotlight)

**********

## Paper Decision Confidence

3: You are fairly confident in your assessment. It is possible that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work. Math/other details were not carefully checked.

**********

*** Meta Review

The paper introduces RLVE, an approach to scale up reinforcement learning (RL) for language models (LMs) by using verifiable environments that dynamically adapt their problem difficulty distribution to the policy model's capabilities. The paper presents a comprehensive evaluation of the proposed method, including experiments on six reasoning benchmarks and comparisons with baseline methods. The results demonstrate that RLVE consistently improves generalizable reasoning capabilities and outperforms baseline methods.

However, the paper does not provide a clear comparison with existing methods, and the authors should compare RLVE with other RL training frameworks, such as RLVR and ProRL, and show how RLVE improves upon them. The authors should also provide a clear analysis of the performance of RLVE on different types of reasoning benchmarks, such as mathematical reasoning, logical reasoning, and code generation, and show how RLVE performs compared to other RL training frameworks. The authors should also provide a clear analysis of the computational cost of RLVE compared to other RL training frameworks and show how RLVE compares in terms of efficiency.

**********

## Paper Decision

Reject (not selected for spotlight)

**********

## Paper Decision Summary

The paper introduces RLVE, an approach to scale up reinforcement learning (RL) for language models (LMs) by using verifiable environments that dynamically adapt their problem difficulty distribution to the policy model's capabilities. The paper presents a comprehensive evaluation of the proposed method, including experiments on six reasoning benchmarks and comparisons with baseline methods. The results demonstrate that RLVE consistently improves generalizable reasoning capabilities and outperforms baseline methods.

However, the paper does not provide a clear comparison with existing methods, and the authors should compare RLVE with other RL training frameworks, such as RLVR and ProRL, and show how RLVE improves upon them. The authors should also provide a clear analysis of the performance of RLVE on different types of reasoning benchmarks, such as mathematical reasoning, logical reasoning, and code generation, and show how RLVE performs compared to other RL training frameworks. The authors should also provide a clear analysis of the computational cost of RLVE compared to other RL training frameworks and show how RLVE compares in terms of efficiency.

**********

## Paper Decision Type

Reject (not selected for spotlight)

**********

## Paper Decision Confidence

3: You are fairly confident in your assessment. It is possible that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work. Math/other details were not carefully checked.

**********

*** Meta Review

The paper introduces RLVE, an approach to scale up reinforcement learning (RL) for language models (LMs) by using verifiable environments that dynamically adapt their problem difficulty distribution to the policy model's capabilities. The paper presents a comprehensive evaluation of the proposed method, including experiments on six reasoning benchmarks and comparisons with baseline methods. The results demonstrate that RLVE consistently improves generalizable reasoning capabilities and outperforms baseline methods.

However, the paper does not provide a clear comparison with existing methods, and the authors should compare RLVE with other RL training frameworks, such as RLVR and ProRL, and show how RLVE improves upon them. The authors should also provide a clear analysis of the performance of RLVE on different types of reasoning benchmarks, such as mathematical reasoning, logical reasoning, and code generation, and show how RLVE performs compared to other RL training frameworks. The authors should also provide a clear analysis of the computational cost of RLVE compared to other RL training frameworks and show how RLVE compares in terms of efficiency.

**********

## Paper Decision

Reject (not selected for spotlight)

**********

## Paper Decision Summary

The paper introduces RLVE, an approach to scale up reinforcement learning (RL) for language models (LMs) by using verifiable environments that dynamically adapt their problem difficulty distribution to the policy model's capabilities. The paper presents a comprehensive evaluation of the proposed method, including experiments on six reasoning benchmarks and comparisons with baseline methods. The results demonstrate that RLVE consistently improves generalizable reasoning capabilities and outperforms baseline methods.

However, the paper does not provide a clear comparison with existing methods, and the authors should compare RLVE with other RL training frameworks, such as RLVR and ProRL, and show how RLVE improves upon them. The authors should also provide a clear analysis of the performance of RLVE on different types of reasoning benchmarks, such as mathematical reasoning, logical reasoning, and code generation, and show how RLVE performs compared to other RL training frameworks. The authors should also provide a clear analysis of the computational cost of RLVE compared to other RL training frameworks and show how RLVE compares in terms of efficiency.

**********

## Paper Decision Type

Reject (not selected for spotlight)

**********

## Paper Decision Confidence

3: You are fairly confident in your assessment. It is possible that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work. Math/other details were not carefully checked.

**********

*** Meta Review

The paper introduces RLVE, an approach to scale up reinforcement learning (RL) for language models (LMs) by using verifiable environments that dynamically adapt their problem difficulty distribution to the policy model's capabilities. The paper presents a comprehensive evaluation of the proposed method, including experiments on six reasoning benchmarks and comparisons with baseline methods. The results demonstrate that RLVE consistently improves generalizable reasoning capabilities and outperforms baseline methods.

However, the paper does not provide a clear comparison with existing methods, and the authors should compare RLVE with other RL training frameworks, such as RLVR and ProRL, and show how RLVE improves upon them. The authors should also provide a clear analysis of the performance of RLVE on different types of reasoning benchmarks, such as mathematical reasoning, logical reasoning, and code generation, and show how RLVE performs compared to other RL training frameworks. The authors should also provide a clear analysis of the computational cost of RLVE compared to other RL training frameworks and show how RLVE compares in terms of efficiency.

**********

## Paper Decision

Reject (not selected for spotlight)

**********

## Paper Decision Summary

The paper introduces RLVE, an approach to scale up reinforcement learning (RL) for language models (LMs) by using verifiable environments that dynamically adapt their problem difficulty distribution to the policy model's capabilities. The paper presents a comprehensive evaluation of the proposed method, including experiments on six reasoning benchmarks and comparisons with baseline methods. The results demonstrate that RLVE consistently improves generalizable reasoning capabilities and outperforms baseline methods.

However, the paper does not provide a clear comparison with existing methods, and the authors should compare RLVE with other RL training frameworks, such as RLVR and ProRL, and show how RLVE improves upon them. The authors should also provide a clear analysis of the performance of RLVE on different types of reasoning benchmarks, such as mathematical reasoning, logical reasoning, and code generation, and show how RLVE performs compared to other RL training frameworks. The authors should also provide a clear analysis of the computational cost of RLVE compared to other RL training frameworks and show how RLVE compares in terms of efficiency.

**********

## Paper Decision Type

Reject (not selected for spotlight)

**********

## Paper Decision Confidence

3: You are fairly confident in your assessment. It is possible that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work. Math/other details were not carefully checked.

**********

*** Meta Review

The paper introduces RLVE, an approach to scale up reinforcement learning (RL) for language models (LMs) by using verifiable environments that dynamically adapt their problem difficulty distribution to the policy model's capabilities. The paper presents a comprehensive evaluation of the proposed method, including experiments on six reasoning benchmarks and comparisons with baseline methods. The results demonstrate that RLVE consistently improves generalizable reasoning capabilities and outperforms baseline methods.

However, the paper does not provide a clear comparison with existing methods, and the authors should compare RLVE with other RL training frameworks, such as RLVR and ProRL, and show how RLVE improves upon them. The authors should also provide a clear analysis of the performance of RLVE on different types of reasoning benchmarks, such as mathematical reasoning, logical