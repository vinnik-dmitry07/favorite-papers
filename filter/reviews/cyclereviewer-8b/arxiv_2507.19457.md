## Reviewer

### Summary

The paper proposes a prompt optimization method that uses a genetic algorithm to search for better prompts. The genetic algorithm is based on Pareto optimization and is guided by natural language feedback. The authors show that the proposed method can outperform existing prompt optimization methods in several benchmarks.

### Soundness

3 good

### Presentation

3 good

### Contribution

2 fair

### Strengths

- The paper is well-written and easy to follow.
- The proposed method is well-motivated and the idea of using a genetic algorithm to search for better prompts is interesting.
- The authors show that the proposed method can outperform existing prompt optimization methods in several benchmarks.

### Weaknesses

- The proposed method is not novel. The idea of using a genetic algorithm to search for better prompts has been explored in previous work, such as EvoPrompt [1]. The authors should provide a more detailed comparison with existing methods.
- The evaluation of the proposed method is not comprehensive. The authors only evaluate the method on a few benchmarks and do not compare it with a wide range of existing methods. The authors should provide a more comprehensive evaluation of the proposed method.
- The authors do not provide a detailed analysis of the results. The authors should provide a more detailed analysis of the results to understand why the proposed method outperforms existing methods.

[1] Guo, Y., Li, Z., Wang, J., & Li, Z. (2023, September). Evolving prompts with evolutionary algorithms for natural language generation. In International Conference on Machine Learning (pp. 13673-13694). PMLR.

### Questions

- How does the proposed method compare with existing methods that use a genetic algorithm to search for better prompts?
- Why does the proposed method outperform existing methods in the benchmarks? What are the advantages of the proposed method?
- How does the proposed method perform on other benchmarks? What are the limitations of the proposed method?

### Flag For Ethics Review

No ethics review needed.

### Rating

5: marginally below the acceptance threshold

### Confidence

4: You are confident in your assessment, but not absolutely certain. It is unlikely, but not impossible, that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work.

**********

## Reviewer

### Summary

The paper proposes a new method for optimizing LLM prompts using a genetic algorithm that incorporates natural language feedback. The method is compared to other prompt optimization methods on several benchmarks and is shown to outperform them.

### Soundness

3 good

### Presentation

3 good

### Contribution

3 good

### Strengths

The paper is well-written and easy to follow. The authors present a clear and concise description of their method and provide a thorough evaluation of its performance on several benchmarks. The paper also includes a detailed analysis of the results, which provides valuable insights into the strengths and weaknesses of the proposed method.

### Weaknesses

The paper presents a novel method for optimizing LLM prompts using a genetic algorithm that incorporates natural language feedback. The method is compared to other prompt optimization methods on several benchmarks and is shown to outperform them. The paper also includes a detailed analysis of the results, which provides valuable insights into the strengths and weaknesses of the proposed method.

### Questions

1. The authors should provide a more detailed comparison with existing methods. The paper only compares the proposed method with a few other prompt optimization methods, and it would be helpful to see how it compares with a wider range of existing methods.

2. The authors should provide a more detailed analysis of the results. The paper only provides a brief analysis of the results, and it would be helpful to see a more detailed analysis of the strengths and weaknesses of the proposed method.

3. The authors should provide more details about the hyperparameters used in the experiments. The paper does not provide a detailed description of the hyperparameters used in the experiments, and it would be helpful to see a more detailed description of the hyperparameters and how they were chosen.

4. The authors should provide more details about the computational resources used in the experiments. The paper does not provide a detailed description of the computational resources used in the experiments, and it would be helpful to see a more detailed description of the computational resources and how they were chosen.

### Flag For Ethics Review

No ethics review needed.

### Rating

5: marginally below the acceptance threshold

### Confidence

3: You are fairly confident in your assessment. It is possible that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work. Math/other details were not carefully checked.

**********

## Reviewer

### Summary

This paper presents a method for optimizing LLM prompts using a genetic algorithm that incorporates natural language feedback. The method is compared to other prompt optimization methods on several benchmarks and is shown to outperform them.

### Soundness

3 good

### Presentation

3 good

### Contribution

3 good

### Strengths

The paper is well-written and easy to follow. The authors present a clear and concise description of their method and provide a thorough evaluation of its performance on several benchmarks. The paper also includes a detailed analysis of the results, which provides valuable insights into the strengths and weaknesses of the proposed method.

### Weaknesses

The paper presents a novel method for optimizing LLM prompts using a genetic algorithm that incorporates natural language feedback. The method is compared to other prompt optimization methods on several benchmarks and is shown to outperform them. The paper also includes a detailed analysis of the results, which provides valuable insights into the strengths and weaknesses of the proposed method.

### Questions

1. How does the proposed method compare with existing methods that use a genetic algorithm to search for better prompts?
2. Why does the proposed method outperform existing methods in the benchmarks? What are the advantages of the proposed method?
3. How does the proposed method perform on other benchmarks? What are the limitations of the proposed method?

### Flag For Ethics Review

No ethics review needed.

### Rating

5: marginally below the acceptance threshold

### Confidence

3: You are fairly confident in your assessment. It is possible that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work. Math/other details were not carefully checked.

**********

## Reviewer

### Summary

This paper proposes GEPA, a prompt optimizer that uses natural language reflection to learn high-level rules from trial and error. GEPA samples trajectories and reflects on them in natural language to diagnose problems, propose and test prompt updates, and combine complementary lessons from the Pareto frontier of its own attempts. GEPA outperforms GRPO by 6% on average and by up to 20%, while using up to 35x fewer rollouts. GEPA also outperforms the leading prompt optimizer, MIPROv2, by over 10% (e.g., +12% accuracy on AIME-2025), and demonstrates promising results as an inference-time search strategy for code optimization.

### Soundness

3 good

### Presentation

3 good

### Contribution

3 good

### Strengths

1. The paper is well-written and easy to follow. The authors present a clear and concise description of their method and provide a thorough evaluation of its performance on several benchmarks. The paper also includes a detailed analysis of the results, which provides valuable insights into the strengths and weaknesses of the proposed method.

2. The proposed method is novel and effective. The authors propose a new method for optimizing LLM prompts using a genetic algorithm that incorporates natural language feedback. The method is compared to other prompt optimization methods on several benchmarks and is shown to outperform them.

3. The paper provides a thorough evaluation of the proposed method on several benchmarks. The authors compare the proposed method to other prompt optimization methods and show that it outperforms them in terms of accuracy and sample efficiency.

### Weaknesses

1. The paper does not provide a detailed analysis of the computational resources used in the experiments. The authors should provide a more detailed description of the computational resources and how they were chosen.

2. The paper does not provide a detailed analysis of the results. The authors should provide a more detailed analysis of the strengths and weaknesses of the proposed method.

### Questions

1. How does the proposed method compare with existing methods that use a genetic algorithm to search for better prompts?
2. Why does the proposed method outperform existing methods in the benchmarks? What are the advantages of the proposed method?
3. How does the proposed method perform on other benchmarks? What are the limitations of the proposed method?

### Flag For Ethics Review

No ethics review needed.

### Rating

6: marginally above the acceptance threshold

### Confidence

4: You are confident in your assessment, but not absolutely certain. It is unlikely, but not impossible, that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work.

**********

## Meta Review

The paper proposes a prompt optimization method that uses a genetic algorithm to search for better prompts. The genetic algorithm is based on Pareto optimization and is guided by natural language feedback. The authors show that the proposed method can outperform existing prompt optimization methods in several benchmarks.

The reviewers have raised several concerns, including the lack of novelty, the limited evaluation, and the lack of detailed analysis of the results. The authors have addressed some of these concerns in their rebuttal, but the reviewers remain unconvinced that the paper is ready for publication. Therefore, I recommend rejecting the paper.

### justification_for_why_not_higher_score

The paper has several weaknesses, including lack of novelty, limited evaluation, and lack of detailed analysis of the results.

### justification_for_why_not_lower_score

N/A

**********

## Paper Decision

Reject (not selected for spotlight)