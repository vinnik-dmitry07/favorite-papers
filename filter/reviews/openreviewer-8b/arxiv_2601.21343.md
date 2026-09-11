# Review

## Summary
This paper proposes a new pretraining paradigm, self-improving pretraining, which incorporates desirable properties like safety, factuality, and quality into the pretraining stage. This approach uses a post-trained model as a rewriter and a judge to guide the policy model during pretraining. The authors demonstrate significant improvements in factuality, safety, and generation quality over standard pretraining approaches.

## Soundness
3

## Presentation
3

## Contribution
3

## Strengths
1. The paper introduces a novel approach to integrate safety, factuality, and quality into the pretraining phase, addressing a fundamental gap in traditional methods.
2. The use of a post-trained model as both rewriter and judge provides a robust mechanism to steer the policy model towards desirable behaviors from the beginning of training.
3. The authors conduct extensive experiments, showing substantial improvements in factuality, safety, and generation quality over standard pretraining methods.

## Weaknesses
1. The approach is computationally intensive, requiring a strong post-trained model and additional resources for training the rewriter and judge components.
2. The method's reliance on a post-trained model as a rewriter and judge could introduce biases from the original training data used for the post-trained model.
3. The paper does not extensively explore how to balance the rewards between different objectives (e.g., quality vs. safety), which could be crucial for achieving optimal results.

## Questions
1. How does the performance of the rewriter and judge models impact the overall effectiveness of the self-improving pretraining? Have you explored using weaker or stronger models for these roles, and how does this affect the results?
2. How do you balance the rewards between different objectives (e.g., quality vs. safety) in the self-improving pretraining? Could you provide more details on how you determine the weights for these objectives, and how sensitive the model's performance is to these weights?
3. How does the self-improving pretraining compare to other approaches that incorporate safety, factuality, and quality during post-training? Could you provide a more detailed comparison with these methods, including their advantages and disadvantages?
4. How does the self-improving pretraining approach scale with larger models or datasets? Are there any computational or memory limitations you encountered, and how did you address them?

## Flag For Ethics Review
No ethics review needed.

## Details Of Ethics Concerns


## Rating
6

## Confidence
4