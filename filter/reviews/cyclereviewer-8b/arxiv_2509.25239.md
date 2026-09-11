## Summary

This paper studies the expressiveness of two types of reasoning paradigms: chain of thought (CoT) and latent thought. CoT is a method that elicits reasoning in large language models by explicitly generating intermediate tokens, while latent thought operates directly in the continuous latent space. The paper presents a formal analysis showing that latent thought admits more efficient parallel computation than inherently sequential CoT. It also shows that CoT enables approximate counting and sampling through stochastic decoding. The results suggest the tasks for which depth-driven recursion is more suitable, offering practical guidance for choosing between reasoning paradigms.

## Soundness

2 fair

## Presentation

2 fair

## Contribution

2 fair

## Strengths

1. The paper presents a formal analysis of the computational capabilities of chain-of-thought and latent thought reasoning, providing a rigorous comparison of their respective strengths and limitations.
2. The paper shows that latent thought enables efficient parallel computation, while CoT enables randomized approximate counting.
3. The results provide practical guidance for selecting between reasoning paradigms, suggesting that latent reasoning is more suitable for problems that can be solved efficiently, while CoT is more effective for more complex problems.

## Weaknesses

1. The paper focuses on theoretical analysis and lacks empirical validation of the theoretical results. The experimental results are limited to a few simple tasks and do not demonstrate the practical applicability of the theoretical findings.
2. The paper does not discuss the limitations of the theoretical analysis, such as the assumptions made and the potential biases introduced.
3. The paper does not provide a clear comparison with other related work in the field.

## Questions

1. Can you provide more empirical validation of the theoretical results? How do the theoretical findings apply to more complex and realistic tasks?
2. Can you discuss the limitations of the theoretical analysis and how they may impact the practical applicability of the results?
3. Can you provide a clear comparison with other related work in the field?

## Flag For Ethics Review

No ethics review needed.

## Rating

3: reject, not good enough

## Confidence

3: You are fairly confident in your assessment. It is possible that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work. Math/other details were not carefully checked.

**********

## Reviewer

## Summary

This paper presents a formal analysis of the computational capabilities of chain-of-thought and latent thought reasoning. The authors show that latent thought enables efficient parallel computation, while CoT enables randomized approximate counting. The results provide practical guidance for selecting between reasoning paradigms, suggesting that latent reasoning is more suitable for problems that can be solved efficiently, while CoT is more effective for more complex problems.

## Soundness

3 good

## Presentation

3 good

## Contribution

3 good

## Strengths

The paper presents a formal analysis of the computational capabilities of chain-of-thought and latent thought reasoning, providing a rigorous comparison of their respective strengths and limitations. The results provide practical guidance for selecting between reasoning paradigms, suggesting that latent reasoning is more suitable for problems that can be solved efficiently, while CoT is more effective for more complex problems.

## Weaknesses

The paper lacks empirical validation of the theoretical results. The experimental results are limited to a few simple tasks and do not demonstrate the practical applicability of the theoretical findings.

## Questions

Can you provide more empirical validation of the theoretical results? How do the theoretical findings apply to more complex and realistic tasks?

## Flag For Ethics Review

No ethics review needed.

## Rating

5: marginally below the acceptance threshold

## Confidence

3: You are fairly confident in your assessment. It is possible that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work. Math/other details were not carefully checked.

**********

## Reviewer

## Summary

This paper studies the computational power of Chain of Thought (CoT) and Latent Thought (LT) reasoning. It provides a formal analysis of the computational capabilities of CoT and LT, and shows that LT enables efficient parallel computation, while CoT enables randomized approximate counting. The results provide practical guidance for selecting between reasoning paradigms, suggesting that LT is more suitable for problems that can be solved efficiently, while CoT is more effective for more complex problems.

## Soundness

3 good

## Presentation

3 good

## Contribution

3 good

## Strengths

1. The paper provides a formal analysis of the computational capabilities of CoT and LT, providing a rigorous comparison of their respective strengths and limitations.
2. The results provide practical guidance for selecting between reasoning paradigms, suggesting that LT is more suitable for problems that can be solved efficiently, while CoT is more effective for more complex problems.
3. The paper shows that LT enables efficient parallel computation, while CoT enables randomized approximate counting.

## Weaknesses

1. The paper lacks empirical validation of the theoretical results. The experimental results are limited to a few simple tasks and do not demonstrate the practical applicability of the theoretical findings.
2. The paper does not discuss the limitations of the theoretical analysis, such as the assumptions made and the potential biases introduced.
3. The paper does not provide a clear comparison with other related work in the field.

## Questions

1. Can you provide more empirical validation of the theoretical results? How do the theoretical findings apply to more complex and realistic tasks?
2. Can you discuss the limitations of the theoretical analysis and how they may impact the practical applicability of the results?
3. Can you provide a clear comparison with other related work in the field?

## Flag For Ethics Review

No ethics review needed.

## Rating

5: marginally below the acceptance threshold

## Confidence

3: You are fairly confident in your assessment. It is possible that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work. Math/other details were not carefully checked.

**********

## Reviewer

## Summary

This paper studies the computational power of two reasoning paradigms: Chain of Thought (CoT) and Latent Thought (LT). The authors show that LT enables efficient parallel computation, while CoT enables randomized approximate counting. The results provide practical guidance for selecting between reasoning paradigms, suggesting that LT is more suitable for problems that can be solved efficiently, while CoT is more effective for more complex problems.

## Soundness

3 good

## Presentation

3 good

## Contribution

3 good

## Strengths

1. The paper provides a formal analysis of the computational capabilities of CoT and LT, providing a rigorous comparison of their respective strengths and limitations.
2. The results provide practical guidance for selecting between reasoning paradigms, suggesting that LT is more suitable for problems that can be solved efficiently, while CoT is more effective for more complex problems.
3. The paper shows that LT enables efficient parallel computation, while CoT enables randomized approximate counting.

## Weaknesses

1. The paper lacks empirical validation of the theoretical results. The experimental results are limited to a few simple tasks and do not demonstrate the practical applicability of the theoretical findings.
2. The paper does not discuss the limitations of the theoretical analysis, such as the assumptions made and the potential biases introduced.
3. The paper does not provide a clear comparison with other related work in the field.

## Questions

1. Can you provide more empirical validation of the theoretical results? How do the theoretical findings apply to more complex and realistic tasks?
2. Can you discuss the limitations of the theoretical analysis and how they may impact the practical applicability of the results?
3. Can you provide a clear comparison with other related work in the field?

## Flag For Ethics Review

No ethics review needed.

## Rating

5: marginally below the acceptance threshold

## Confidence

3: You are fairly confident in your assessment. It is possible that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work. Math/other details were not carefully checked.

**********

## Meta Review

This paper studies the computational power of two reasoning paradigms: Chain of Thought (CoT) and Latent Thought (LT). The authors show that LT enables efficient parallel computation, while CoT enables randomized approximate counting. The results provide practical guidance for selecting between reasoning paradigms, suggesting that LT is more suitable for problems that can be solved efficiently, while CoT is more effective for more complex problems.

The reviewers found the paper to be well-written and well-motivated, but raised concerns about the lack of empirical validation of the theoretical results, the limited experimental results, and the lack of discussion on the limitations of the theoretical analysis. They also suggested that the paper could benefit from a clearer comparison with other related work in the field.

## justification_for_why_not_higher_score

The paper is borderline, but the reviewers all gave it a score of 5.

## justification_for_why_not_lower_score

N/A

**********

## Paper Decision

Reject (not selected for publication for this venue)