## Reviewer

### Summary

The paper introduces a new method for training LLM agents, called Group-in-Group Policy Optimization (GiGPO). The method is based on the idea of grouping trajectories and states to improve credit assignment in multi-step decision-making tasks. The authors evaluate GiGPO on two embodied benchmarks (ALFWorld and WebShop) and search-augmented QA tasks, and show that it outperforms prior methods in terms of performance and computational efficiency.

### Soundness

3 good

### Presentation

3 good

### Contribution

3 good

### Strengths

- The paper addresses an important problem in the field of LLM agents, which is credit assignment in multi-step decision-making tasks.
- The proposed method, GiGPO, is novel and effective in improving performance and computational efficiency compared to prior methods.
- The paper is well-written and easy to follow.
- The experiments are thorough and demonstrate the effectiveness of GiGPO on various tasks.

### Weaknesses

- The paper does not provide a theoretical analysis of the proposed method, which could help understand its properties and limitations.
- The paper does not discuss the limitations of the proposed method, such as potential issues with scalability or generalizability to other tasks.
- The paper does not provide a detailed comparison with prior methods, such as a discussion of the trade-offs between performance and computational efficiency.

### Questions

- Can you provide a theoretical analysis of the proposed method, such as its convergence properties or computational complexity?
- Can you discuss the limitations of the proposed method, such as potential issues with scalability or generalizability to other tasks?
- Can you provide a more detailed comparison with prior methods, such as a discussion of the trade-offs between performance and computational efficiency?

### Flag For Ethics Review

No ethics review needed.

### Rating

6: marginally above the acceptance threshold

### Confidence

4: You are confident in your assessment, but not absolutely certain. It is unlikely, but not impossible, that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work.

**********

## Reviewer

### Summary

This paper proposes a new method for training LLM agents. The method is based on the idea of grouping trajectories and states to improve credit assignment in multi-step decision-making tasks. The authors evaluate the method on two embodied benchmarks (ALFWorld and WebShop) and search-augmented QA tasks, and show that it outperforms prior methods in terms of performance and computational efficiency.

### Soundness

3 good

### Presentation

3 good

### Contribution

3 good

### Strengths

The paper is well-written and easy to follow. The proposed method is novel and effective in improving performance and computational efficiency compared to prior methods. The experiments are thorough and demonstrate the effectiveness of the method on various tasks.

### Weaknesses

The paper does not provide a theoretical analysis of the proposed method, which could help understand its properties and limitations. The paper does not discuss the limitations of the proposed method, such as potential issues with scalability or generalizability to other tasks.

### Questions

How does the proposed method compare to other methods in terms of scalability and generalizability to other tasks?

### Flag For Ethics Review

No ethics review needed.

### Rating

6: marginally above the acceptance threshold

### Confidence

3: You are fairly confident in your assessment. It is possible that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work. Math/other details were not carefully checked.

**********

## Reviewer

### Summary

This paper proposes a novel approach for training large language models (LLMs) as agents in reinforcement learning (RL) settings. The main idea is to group trajectories and states to improve credit assignment in multi-step decision-making tasks. The authors evaluate their approach on two embodied benchmarks (ALFWorld and WebShop) and search-augmented QA tasks, and show that it outperforms prior methods in terms of performance and computational efficiency.

### Soundness

3 good

### Presentation

3 good

### Contribution

3 good

### Strengths

- The paper is well-written and easy to follow.
- The proposed method is novel and effective in improving performance and computational efficiency compared to prior methods.
- The experiments are thorough and demonstrate the effectiveness of the method on various tasks.

### Weaknesses

- The paper does not provide a theoretical analysis of the proposed method, which could help understand its properties and limitations.
- The paper does not discuss the limitations of the proposed method, such as potential issues with scalability or generalizability to other tasks.

### Questions

- How does the proposed method compare to other methods in terms of scalability and generalizability to other tasks?

### Flag For Ethics Review

No ethics review needed.

### Rating

6: marginally above the acceptance threshold

### Confidence

3: You are fairly confident in your assessment. It is possible that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work. Math/other details were not carefully checked.

**********

## Reviewer

### Summary

This paper introduces Group-in-Group Policy Optimization (GiGPO), a novel RL algorithm designed to address the challenges of credit assignment in multi-turn LLM agent training. GiGPO achieves fine-grained credit assignment while preserving the benefits of group-based RL, including critic-free optimization, low memory usage, and stable convergence. The algorithm employs a two-level structure for estimating relative advantage, with macro advantages computed at the episode level and micro advantages at the step level through an anchor state grouping mechanism. GiGPO outperforms existing methods on agent benchmarks like ALFWorld and WebShop, and demonstrates superior performance on search-based QA tasks. The algorithm maintains efficiency, with minimal additional time cost and no compromise on GPU memory overhead.

### Soundness

3 good

### Presentation

3 good

### Contribution

3 good

### Strengths

1. The paper is well-written and easy to follow.

2. The proposed method is novel and effective in improving performance and computational efficiency compared to prior methods.

3. The experiments are thorough and demonstrate the effectiveness of the method on various tasks.

### Weaknesses

1. The paper does not provide a theoretical analysis of the proposed method, which could help understand its properties and limitations.

2. The paper does not discuss the limitations of the proposed method, such as potential issues with scalability or generalizability to other tasks.

3. The paper does not provide a detailed comparison with prior methods, such as a discussion of the trade-offs between performance and computational efficiency.

### Questions

1. How does the proposed method compare to other methods in terms of scalability and generalizability to other tasks?

2. Can you provide a theoretical analysis of the proposed method, such as its convergence properties or computational complexity?

3. Can you discuss the limitations of the proposed method, such as potential issues with scalability or generalizability to other tasks?

### Flag For Ethics Review

No ethics review needed.

### Rating

6: marginally above the acceptance threshold

### Confidence

3: You are fairly confident in your assessment. It is possible that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work. Math/other details were not carefully checked.

**********

## Meta Review

This paper introduces a new method for training LLM agents, called Group-in-Group Policy Optimization (GiGPO). The method is based on the idea of grouping trajectories and states to improve credit assignment in multi-step decision-making tasks. The authors evaluate GiGPO on two embodied benchmarks (ALFWorld and WebShop) and search-augmented QA tasks, and show that it outperforms prior methods in terms of performance and computational efficiency.

All reviewers agree that this paper is well-written and easy to follow. The proposed method is novel and effective in improving performance and computational efficiency compared to prior methods. The experiments are thorough and demonstrate the effectiveness of the method on various tasks.

The authors have addressed all the concerns raised by the reviewers. The paper is ready for publication.

### justification_for_why_not_higher_score

N/A

### justification_for_why_not_lower_score

All reviewers agree that this paper is well-written and easy to follow. The proposed method is novel and effective in improving performance and computational efficiency compared to prior methods. The experiments are thorough and demonstrate the effectiveness of the method on various tasks.

**********

## Paper Decision

Accept (poster)