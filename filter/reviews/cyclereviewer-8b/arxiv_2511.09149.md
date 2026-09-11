## Reviewer

### Summary

This paper proposes a method for enabling agents to communicate entirely in latent space. The method is based on the idea of transmitting the last-layer hidden states of an LLM as a representation of its thought for direct communication. The authors demonstrate that their method outperforms both fine-tuned chain-of-thought (CoT) prompting and single-agent baselines in terms of performance and efficiency.

### Soundness

2 fair

### Presentation

3 good

### Contribution

2 fair

### Strengths

- The paper is well-written and easy to follow.
- The proposed method is novel and interesting.
- The experiments are comprehensive and demonstrate the effectiveness of the proposed method.

### Weaknesses

- The proposed method is limited to a two-agent setting. It is unclear how it would scale to more complex multi-agent systems.
- The method assumes access to internal model representations, which may not be available in all scenarios.
- The method is not interpretable and may be difficult to debug or monitor.

### Questions

- How does the method scale to more complex multi-agent systems?
- How does the method perform in scenarios where access to internal model representations is limited?
- How can the method be made more interpretable and easier to debug or monitor?

### Flag For Ethics Review

No ethics review needed.

### Rating

5: marginally below the acceptance threshold

### Confidence

3: You are fairly confident in your assessment. It is possible that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work. Math/other details were not carefully checked.

**********

## Reviewer

### Summary

This paper introduces Interlat, a novel approach to inter-agent communication in latent space, aiming to improve the efficiency and effectiveness of communication between agents. The authors propose a paradigm that leverages the continuous last hidden states of an LLM as a representation of its thought for direct communication. They also introduce a compression process to further compress latent communication via latent space reasoning. The results demonstrate that Interlat outperforms both fine-tuned chain-of-thought (CoT) prompting and single-agent baselines, promoting more exploratory behavior and enabling the utilization of latent information. The paper also highlights the potential of entirely latent space inter-agent communication, offering valuable insights for future research.

### Soundness

3 good

### Presentation

3 good

### Contribution

3 good

### Strengths

1. The paper is well-written and easy to follow.
2. The proposed method is novel and interesting.
3. The experiments are comprehensive and demonstrate the effectiveness of the proposed method.

### Weaknesses

1. The authors claim that the proposed method can outperform CoT in the MATH benchmark, but the results in Table 2 are not significant enough to support this claim. The difference between the proposed method and CoT is not very large, and the results are not statistically significant. 
2. The authors only evaluate the proposed method on two benchmarks, Alfworld and MATH. It would be better to evaluate the proposed method on more benchmarks to demonstrate its effectiveness.
3. The authors do not provide a detailed analysis of the proposed method. For example, how does the proposed method work? What are the advantages and disadvantages of the proposed method compared to CoT?

### Questions

Please refer to the Weaknesses.

### Flag For Ethics Review

No ethics review needed.

### Rating

5: marginally below the acceptance threshold

### Confidence

3: You are fairly confident in your assessment. It is possible that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work. Math/other details were not carefully checked.

**********

## Reviewer

### Summary

This paper proposes a new method for inter-agent communication, called Interlat, which enables agents to communicate entirely in latent space. The authors demonstrate that Interlat outperforms both fine-tuned chain-of-thought (CoT) prompting and single-agent baselines in terms of performance and efficiency. They also show that latent communication can be compressed through latent-space reasoning, forming a compact, task-preserving representation that retains parallel hypotheses while discarding redundant structure. The authors also provide an analysis of the proposed method, including its limitations and potential applications.

### Soundness

3 good

### Presentation

3 good

### Contribution

3 good

### Strengths

1. The paper is well-written and easy to follow.
2. The proposed method is novel and interesting.
3. The experiments are comprehensive and demonstrate the effectiveness of the proposed method.
4. The analysis of the proposed method is thorough and provides valuable insights.

### Weaknesses

1. The authors should provide a more detailed analysis of the limitations of the proposed method, including its potential drawbacks and areas for future improvement.
2. The authors should provide more details on the experimental setup, including the specific models used, the hyperparameters, and the evaluation metrics.
3. The authors should provide a more detailed discussion of the related work, including a comparison of the proposed method with other existing methods.

### Questions

1. How does the proposed method compare to other existing methods for inter-agent communication?
2. What are the potential applications of the proposed method?
3. How does the proposed method handle noisy or incomplete information during communication?

### Flag For Ethics Review

No ethics review needed.

### Rating

6: marginally above the acceptance threshold

### Confidence

3: You are fairly confident in your assessment. It is possible that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work. Math/other details were not carefully checked.

**********

## Reviewer

### Summary

The paper introduces Interlat, a novel approach to inter-agent communication in latent space. The authors demonstrate that Interlat outperforms both fine-tuned chain-of-thought (CoT) prompting and single-agent baselines in terms of performance and efficiency. They also show that latent communication can be compressed through latent-space reasoning, forming a compact, task-preserving representation that retains parallel hypotheses while discarding redundant structure. The paper also provides an analysis of the proposed method, including its limitations and potential applications.

### Soundness

3 good

### Presentation

3 good

### Contribution

3 good

### Strengths

1. The paper is well-written and easy to follow.
2. The proposed method is novel and interesting.
3. The experiments are comprehensive and demonstrate the effectiveness of the proposed method.
4. The analysis of the proposed method is thorough and provides valuable insights.

### Weaknesses

1. The authors should provide a more detailed analysis of the limitations of the proposed method, including its potential drawbacks and areas for future improvement.
2. The authors should provide more details on the experimental setup, including the specific models used, the hyperparameters, and the evaluation metrics.
3. The authors should provide a more detailed discussion of the related work, including a comparison of the proposed method with other existing methods.

### Questions

1. How does the proposed method compare to other existing methods for inter-agent communication?
2. What are the potential applications of the proposed method?
3. How does the proposed method handle noisy or incomplete information during communication?

### Flag For Ethics Review

No ethics review needed.

### Rating

6: marginally above the acceptance threshold

### Confidence

3: You are fairly confident in your assessment. It is possible that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work. Math/other details were not carefully checked.

**********

## Meta Review

This paper introduces Interlat, a novel approach to inter-agent communication in latent space. The authors demonstrate that Interlat outperforms both fine-tuned chain-of-thought (CoT) prompting and single-agent baselines in terms of performance and efficiency. They also show that latent communication can be compressed through latent-space reasoning, forming a compact, task-preserving representation that retains parallel hypotheses while discarding redundant structure. The paper also provides an analysis of the proposed method, including its limitations and potential applications.

The paper is well-written and easy to follow. The proposed method is novel and interesting. The experiments are comprehensive and demonstrate the effectiveness of the proposed method. The analysis of the proposed method is thorough and provides valuable insights.

However, the authors should provide a more detailed analysis of the limitations of the proposed method, including its potential drawbacks and areas for future improvement. The authors should provide more details on the experimental setup, including the specific models used, the hyperparameters, and the evaluation metrics. The authors should provide a more detailed discussion of the related work, including a comparison of the proposed method with other existing methods.

### justification_for_why_not_higher_score

The authors should provide a more detailed analysis of the limitations of the proposed method, including its potential drawbacks and areas for future improvement. The authors should provide more details on the experimental setup, including the specific models used, the hyperparameters, and the evaluation metrics. The authors should provide a more detailed discussion of the related work, including a comparison of the proposed method with other existing methods.

### justification_for_why_not_lower_score

N/A

**********

## Paper Decision

Reject (not selected for publication at ICLR 2024)