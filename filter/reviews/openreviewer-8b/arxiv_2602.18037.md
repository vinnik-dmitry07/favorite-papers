# Review

## Summary
This paper addresses reward hacking in RLHF/RLVR by proposing a novel approach that biases policy updates towards regions where the reward model is more accurate. The authors introduce gradient regularization (GR) as an alternative to the commonly used KL penalty, aiming to maintain reward model accuracy during training. The paper establishes a theoretical connection between reward model accuracy and the flatness of the optimum, using this to motivate the use of GR. Experiments show that GR outperforms KL penalties across various RLHF tasks, enhancing GPT-judged win-rates, avoiding excessive focus on formatting in rule-based rewards, and preventing hacking of the judge in LLM-as-a-Judge tasks.

## Soundness
3

## Presentation
3

## Contribution
3

## Strengths
- The paper is well-written and easy to follow.
- The authors provide a detailed theoretical analysis, establishing a clear connection between gradient regularization and the accuracy of the reward model.
- The experimental results are impressive, demonstrating the effectiveness of GR in improving performance across various tasks.

## Weaknesses
- The authors should consider including a pseudocode algorithm to clearly outline the steps of the proposed method, which would aid in understanding the approach.
- The authors should provide a more detailed discussion on the computational overhead introduced by the gradient norm calculation, especially when using finite-difference estimates. This information would help readers assess the practical feasibility of the method.
- The authors should include a discussion on the limitations of the proposed method. For example, the assumption of a Lipschitz-continuous true reward highly depends on the chosen distance between actions. Additionally, there is a risk that GR may inadvertently lead to reward hacking by favoring flat but incorrect maxima of the proxy reward.

## Questions
- Could the authors provide a pseudocode algorithm for the proposed method to clarify the steps involved?
- Can the authors discuss the computational overhead introduced by the gradient norm calculation in more detail? How does it impact the practical feasibility of the method?
- Could the authors include a discussion of the limitations of the proposed method, particularly regarding the assumptions made and potential scenarios where it may not perform as expected?

## Flag For Ethics Review
No ethics review needed.

## Details Of Ethics Concerns


## Rating
5

## Confidence
4