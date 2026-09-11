# Review

## Summary
This paper studies how LLMs solve grade school math problems. The authors train GPT-2 from scratch on a synthetic dataset of grade school math problems and analyze the model's behavior. The authors find that the model can learn to solve problems by generalization rather than memorization, and that the model can learn to generate the shortest solution. The authors also study the model's internal state by probing the model, and find that the model can learn dependencies between variables that are not necessary to answer the question. The authors also find that the model's mistakes can be explained by probing the model's internal state. Finally, the authors find that the depth of the model is more important than the width for solving math problems.

## Soundness
4

## Presentation
4

## Contribution
3

## Strengths
- The paper is well-written and easy to follow.
- The paper studies an important problem, namely understanding how LLMs solve math problems.
- The paper's synthetic dataset is well-designed, and the experiments are well-executed.
- The paper's results are interesting and novel, and provide insight into how LLMs solve math problems.

## Weaknesses
- The paper does not study how the model's performance scales with model size. It would be interesting to see if the results hold for smaller and larger models.
- The paper does not study how the model's performance changes with different amounts of training data. It would be interesting to see if the results hold for different training data sizes.
- The paper does not study how the model's performance changes with different types of problems. For example, does the model make different mistakes on different types of problems?

## Questions
- Do the results hold for other LLMs, such as Llama?
- How does the model's performance scale with model size?
- How does the model's performance change with different amounts of training data?
- How does the model's performance change with different types of problems?

## Flag For Ethics Review
No ethics review needed.

## Details Of Ethics Concerns


## Rating
8

## Confidence
4