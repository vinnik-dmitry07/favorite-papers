## Reviewer

### Summary

The paper introduces a new approach called Self-Refine, which aims to improve the initial outputs of large language models (LLMs) through iterative feedback and refinement. The method uses a single LLM as the generator, refiner, and feedback provider, without the need for additional training or reinforcement learning. The paper evaluates Self-Refine across various tasks, including dialog response generation and mathematical reasoning, and shows that it outperforms the same LLM with conventional one-step generation, with an average improvement of around 20% in task performance. The paper demonstrates that even state-of-the-art LLMs like GPT-4 can be further improved at test time using this simple, standalone approach.

### Soundness

3 good

### Presentation

3 good

### Contribution

3 good

### Strengths

The paper introduces a novel approach called Self-Refine, which allows LLMs to iteratively provide self-feedback and refine their own outputs without additional training or reinforcement learning. This approach is simple, standalone, and effective, as demonstrated by its ability to improve LLMs like GPT-4 across various tasks.

The paper evaluates Self-Refine across a wide range of tasks, including dialog response generation, mathematical reasoning, and code generation, and shows that it outperforms the same LLM with conventional one-step generation. The paper also provides a detailed analysis of the approach, including the impact of feedback quality, the importance of multiple iterations, and the potential for the approach to work with weaker models.

The paper is well-written and easy to follow, with clear explanations of the approach and its evaluation. The paper also provides a detailed analysis of the limitations of the approach, including the need for the base models to have sufficient few-shot modeling or instruction-following abilities.

### Weaknesses

The paper evaluates Self-Refine on a limited number of tasks, and it is not clear how well the approach would perform on other tasks or domains. The paper also does not provide a detailed comparison with other approaches that use feedback and refinement to improve LLM outputs.

The paper does not provide a detailed analysis of the computational cost of Self-Refine, including the time and resources required for each iteration of feedback and refinement. The paper also does not provide a detailed analysis of the potential limitations of the approach, including the potential for the model to get stuck in a loop or to generate low-quality feedback or refinements.

The paper does not provide a detailed analysis of the potential societal impact of Self-Refine, including the potential benefits and risks of using this approach in real-world applications. The paper also does not provide a detailed discussion of the broader implications of this work, including the potential for this approach to be used in other areas of natural language processing or machine learning.

### Questions

1. How does Self-Refine compare to other approaches that use feedback and refinement to improve LLM outputs?

2. How does the computational cost of Self-Refine compare to other approaches that use feedback and refinement to improve LLM outputs?

3. What are the potential limitations of Self-Refine, and how can they be addressed?

4. What are the potential societal implications of Self-Refine, and how can they be addressed?

### Flag For Ethics Review

No ethics review needed.

### Rating

6: marginally above the acceptance threshold

### Confidence

3: You are fairly confident in your assessment. It is possible that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work. Math/other details were not carefully checked.

**********

## Reviewer

### Summary

The paper introduces a simple method to iteratively improve the output of a language model by using it to generate feedback and then use the feedback to refine the output. The method is evaluated on a variety of tasks and shows consistent improvements over the original model.

### Soundness

3 good

### Presentation

3 good

### Contribution

3 good

### Strengths

The paper is well written and easy to follow. The idea is simple and elegant. The results are promising and consistent across different tasks.

### Weaknesses

1. The paper does not provide a detailed analysis of the computational cost of the method, which could be a limitation in practice. 
2. The paper does not provide a detailed analysis of the potential limitations of the method, such as the potential for the model to get stuck in a loop or to generate low-quality feedback or refinements.
3. The paper does not provide a detailed discussion of the broader implications of this work, including the potential for this approach to be used in other areas of natural language processing or machine learning.

### Questions

1. How does the method compare to other methods that use feedback and refinement to improve LLM outputs?
2. How does the computational cost of the method compare to other methods that use feedback and refinement to improve LLM outputs?
3. What are the potential limitations of the method, and how can they be addressed?

### Flag For Ethics Review

No ethics review needed.

### Rating

6: marginally above the acceptance threshold

### Confidence

3: You are fairly confident in your assessment. It is possible that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work. Math/other details were not carefully checked.

**********

## Reviewer

### Summary

This paper proposes a method to improve the output of LLMs through iterative feedback and refinement. The method uses the same LLM to generate feedback and refine its outputs. The authors evaluate their method on 7 generation tasks that span diverse domains, including natural language and source-code generation. The results show that the method outperforms direct generation from strong LLMs like GPT-3.5 and GPT-4 by 5-40% absolute improvement.

### Soundness

3 good

### Presentation

3 good

### Contribution

3 good

### Strengths

- The paper is well-written and easy to follow.
- The proposed method is simple and effective.
- The results are promising and consistent across different tasks.

### Weaknesses

- The method requires the LLM to have sufficient few-shot modeling or instruction-following abilities. This may limit the applicability of the method to weaker models.
- The paper does not provide a detailed analysis of the computational cost of the method, which could be a limitation in practice.
- The paper does not provide a detailed discussion of the broader implications of this work, including the potential for this approach to be used in other areas of natural language processing or machine learning.

### Questions

- How does the method compare to other methods that use feedback and refinement to improve LLM outputs?
- How does the computational cost of the method compare to other methods that use feedback and refinement to improve LLM outputs?
- What are the potential limitations of the method, and how can they be addressed?

### Flag For Ethics Review

No ethics review needed.

### Rating

6: marginally above the acceptance threshold

### Confidence

4: You are confident in your assessment, but not absolutely certain. It is unlikely, but not impossible, that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work.

**********

## Reviewer

### Summary

The paper introduces an iterative self-refinement algorithm that alternates between two generative steps: feedback and refine. This approach leverages a single language model to generate, provide feedback, and refine its outputs, all without the need for additional training or reinforcement learning. The method is evaluated across seven diverse tasks, including dialogue response generation and code generation, and demonstrates significant improvements over direct generation from strong LLMs like GPT-3.5 and GPT-4.

### Soundness

3 good

### Presentation

3 good

### Contribution

3 good

### Strengths

- The paper introduces a novel approach that allows LLMs to iteratively provide self-feedback and refine their own outputs without additional training or reinforcement learning.
- The approach is simple, standalone, and effective, as demonstrated by its ability to improve LLMs like GPT-4 across various tasks.
- The paper provides a detailed analysis of the approach, including the impact of feedback quality, the importance of multiple iterations, and the potential for the approach to work with weaker models.
- The paper evaluates Self-Refine across a wide range of tasks, including dialog response generation, mathematical reasoning, and code generation, and shows that it outperforms the same LLM with conventional one-step generation.

### Weaknesses

- The paper evaluates Self-Refine on a limited number of tasks, and it is not clear how well the approach would perform on other tasks or domains.
- The paper does not provide a detailed comparison with other approaches that use feedback and refinement to improve LLM outputs.
- The paper does not provide a detailed analysis of the computational cost of Self-Refine, including the time and resources required for each iteration of feedback and refinement.
- The paper does not provide a detailed analysis of the potential limitations of the approach, including the potential for the model to get stuck in a loop or to generate low-quality feedback or refinements.
- The paper does not provide a detailed discussion of the broader implications of this work, including the potential for this approach to be used in other areas of natural language processing or machine learning.

### Questions

- How does Self-Refine compare to other approaches that use feedback and refinement to improve LLM outputs?
- How does the computational cost of Self-Refine compare to other approaches that use feedback and refinement to improve LLM outputs?
- What are the potential limitations of Self-Refine, and how can they be addressed?
- What are the potential societal implications of Self-Refine, and how can they be addressed?

### Flag For Ethics Review

No ethics review needed.

### Rating

6: marginally above the acceptance threshold

### Confidence

4: You are confident in your assessment, but not absolutely certain. It is unlikely, but not impossible, that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work.

**********

## Meta Review

This paper introduces a method for iterative refinement of LLM outputs. The method uses the same LLM to generate feedback and refine its outputs. The authors evaluate their method on 7 generation tasks that span diverse domains, including natural language and source-code generation. The results show that the method outperforms direct generation from strong LLMs like GPT-3.5 and GPT-4 by 5-40% absolute improvement.

The paper received four reviews, all of which were positive. The reviewers appreciated the simplicity and effectiveness of the proposed method, as well as its consistent improvements across different tasks. The authors addressed the concerns raised by the reviewers in the rebuttal. The paper is well-written and easy to follow, and the results are promising and consistent across different tasks. The paper also provides a detailed analysis of the approach, including the impact of feedback quality, the importance of multiple iterations, and the potential for the approach to work with weaker models.

### justification_for_why_not_higher_score

The paper does not provide a detailed comparison with other approaches that use feedback and refinement to improve LLM outputs. The paper does not provide a detailed analysis of the computational cost of Self-Refine, including the time and resources required for each iteration of feedback and refinement. The paper does not provide a detailed analysis of the potential limitations of the approach, including the potential for the model to get stuck in a loop or to generate low-quality feedback or refinements.

### justification_for_why_not_lower_score

The paper introduces a novel approach that allows LLMs to iteratively provide self-feedback and refine their own outputs without additional training or reinforcement learning. The approach is simple, standalone, and effective, as demonstrated by its ability to improve LLMs like GPT-4 across various tasks. The paper provides a detailed analysis of the approach, including the impact of feedback quality, the importance of multiple iterations, and the potential for the approach to work with weaker models. The paper evaluates Self-Refine across a wide range of tasks, including dialog response generation, mathematical reasoning, and code generation, and shows that it outperforms the same LLM with conventional one-step generation.

**********

## Paper Decision

Accept (poster)