## Reviewer

### Summary

This paper proposes a self-play SWE-RL (SSR) for training superintelligent software agents. SSR requires only access to sandboxed repositories with source code and dependencies, no need for human-labeled issues or test commands. SSR achieves clear self-improvement and consistently outperforms the human-data baseline throughout training.

### Soundness

2 fair

### Presentation

3 good

### Contribution

2 fair

### Strengths

- The idea of self-play SWE-RL (SSR) is novel and interesting.
- The paper is well-written and easy to follow.

### Weaknesses

- The paper lacks a clear explanation of the motivation for the proposed method. What are the benefits of self-play SWE-RL (SSR) compared to existing methods?
- The paper does not provide a detailed explanation of the experimental setup, including the data used, the evaluation metrics, and the baselines used for comparison. More details are needed to understand the experimental design and the results.
- The paper does not provide a clear explanation of the results, including the performance of the proposed method and the comparison with existing methods. More details are needed to understand the results and their implications.

### Questions

Please refer to the Weaknesses section.

### Flag For Ethics Review

No ethics review needed.

### Rating

3: reject, not good enough

### Confidence

4: You are confident in your assessment, but not absolutely certain. It is unlikely, but not impossible, that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work.

**********

## Reviewer

### Summary

This paper proposes Self-play SWE-RL (SSR) for training superintelligent software agents. SSR requires only access to sandboxed repositories with source code and dependencies, no need for human-labeled issues or test commands. SSR achieves clear self-improvement and consistently outperforms the human-data baseline throughout training.

### Soundness

3 good

### Presentation

3 good

### Contribution

2 fair

### Strengths

1. The paper is well-written and easy to follow.
2. The proposed method is novel and interesting.

### Weaknesses

1. The motivation of the paper is not clear. The authors should explain the motivation and the significance of the proposed method.
2. The experimental results are not convincing. The authors should provide more detailed results and analysis to support their claims.
3. The paper lacks a clear explanation of the experimental setup, including the data used, the evaluation metrics, and the baselines used for comparison. More details are needed to understand the experimental design and the results.
4. The paper does not provide a clear explanation of the results, including the performance of the proposed method and the comparison with existing methods. More details are needed to understand the results and their implications.

### Questions

Please refer to the Weaknesses section.

### Flag For Ethics Review

No ethics review needed.

### Rating

5: marginally below the acceptance threshold

### Confidence

4: You are confident in your assessment, but not absolutely certain. It is unlikely, but not impossible, that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work.

**********

## Reviewer

### Summary

This paper presents a method to train a software agent to learn to solve software problems by self-play. The agent is trained to first generate a bug and then to fix the bug. The bug generation and bug fixing are done by the same model, but the model is prompted differently for each task. The bug generation is done by a prompt that instructs the model to remove code files or revert historical changes. The bug fixing is done by a prompt that asks the model to fix the bug. The paper presents results on two benchmarks, SWE-bench Verified and SWE-Bench Pro, showing that the agent can learn to solve more problems over time.

### Soundness

3 good

### Presentation

3 good

### Contribution

2 fair

### Strengths

- The paper presents a novel approach to training software agents to solve problems by self-play.
- The paper shows that the agent can learn to solve more problems over time.
- The paper presents results on two benchmarks, SWE-bench Verified and SWE-Bench Pro.

### Weaknesses

- The paper does not provide a clear description of the benchmarks and the evaluation metrics used.
- The paper does not provide a clear description of the baselines used for comparison.
- The paper does not provide a clear description of the results, including the performance of the proposed method and the comparison with existing methods.
- The paper does not provide a clear explanation of the limitations of the proposed method.

### Questions

- What are the limitations of the proposed method?
- How does the proposed method compare to other methods for training software agents?
- What are the strengths and weaknesses of the proposed method compared to other methods?
- How does the proposed method scale to larger and more complex software systems?
- What are the potential applications of the proposed method?

### Flag For Ethics Review

No ethics review needed.

### Rating

5: marginally below the acceptance threshold

### Confidence

3: You are fairly confident in your assessment. It is possible that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work. Math/other details were not carefully checked.

**********

## Reviewer

### Summary

This paper proposes a method for training a software agent to solve problems by self-play. The agent is trained to first generate a bug and then to fix the bug. The bug generation and bug fixing are done by the same model, but the model is prompted differently for each task. The bug generation is done by a prompt that instructs the model to remove code files or revert historical changes. The bug fixing is done by a prompt that asks the model to fix the bug. The paper presents results on two benchmarks, SWE-bench Verified and SWE-Bench Pro, showing that the agent can learn to solve more problems over time.

### Soundness

3 good

### Presentation

3 good

### Contribution

3 good

### Strengths

- The paper presents a novel approach to training software agents to solve problems by self-play.
- The paper shows that the agent can learn to solve more problems over time.
- The paper presents results on two benchmarks, SWE-bench Verified and SWE-Bench Pro.

### Weaknesses

- The paper does not provide a clear description of the benchmarks and the evaluation metrics used.
- The paper does not provide a clear description of the baselines used for comparison.
- The paper does not provide a clear description of the results, including the performance of the proposed method and the comparison with existing methods.
- The paper does not provide a clear explanation of the limitations of the proposed method.

### Questions

- What are the limitations of the proposed method?
- How does the proposed method compare to other methods for training software agents?
- What are the strengths and weaknesses of the proposed method compared to other methods?
- How does the proposed method scale to larger and more complex software systems?
- What are the potential applications of the proposed method?

### Flag For Ethics Review

No ethics review needed.

### Rating

5: marginally below the acceptance threshold

### Confidence

3: You are fairly confident in your assessment. It is possible that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work. Math/other details were not carefully checked.

**********

## Meta Review

This paper proposes a self-play SWE-RL (SSR) for training superintelligent software agents. SSR requires only access to sandboxed repositories with source code and dependencies, no need for human-labeled issues or test commands. SSR achieves clear self-improvement and consistently outperforms the human-data baseline throughout training.

Strengths: The paper is well-written and easy to follow. The proposed method is novel and interesting.

Weaknesses: The motivation of the paper is not clear. The experimental results are not convincing. The paper lacks a clear explanation of the experimental setup, including the data used, the evaluation metrics, and the baselines used for comparison. More details are needed to understand the experimental design and the results. The paper does not provide a clear explanation of the results, including the performance of the proposed method and the comparison with existing methods. More details are needed to understand the results and their implications.

### justification_for_why_not_higher_score

The motivation of the paper is not clear. The experimental results are not convincing. The paper lacks a clear explanation of the experimental setup, including the data used, the evaluation metrics, and the baselines used for comparison. More details are needed to understand the experimental design and the results. The paper does not provide a clear explanation of the results, including the performance of the proposed method and the comparison with existing methods. More details are needed to understand the results and their implications.

### justification_for_why_not_lower_score

N/A

**********

## Paper Decision

Reject (not selected for publication for ICLR 2024)