# Review

## Summary
This paper proposes a human preference reward model for text-to-image generation, which is trained with 137k human preference pairs. The proposed reward model can serve as a better alternative to CLIPScore and FID. Furthermore, the paper proposes a reward feedback learning method to finetune the diffusion models with the proposed reward model.

## Soundness
3

## Presentation
3

## Contribution
3

## Strengths
1. The paper is well-written and easy to follow.
2. The paper proposes a large-scale human preference dataset for text-to-image generation, which can be very useful for future research.
3. The proposed reward model outperforms CLIPScore and FID in terms of human preference alignment.
4. The proposed reward feedback learning method can improve the generation quality of the diffusion model.

## Weaknesses
1. The paper does not provide the test set performance of ImageReward in terms of the agreement with human preference. It is unclear how well the model generalizes to unseen prompts.
2. The paper does not provide the human agreement on the 1000 generated images per model in Table 1. It is unclear if the human annotation is consistent enough to support the evaluation.
3. The paper does not provide the human agreement on the 1000 generated images per model for the experiment in Table 4. It is unclear if the human annotation is consistent enough to support the evaluation.
4. The paper does not provide the human preference results for the baselines in Table 4. It is unclear if the improvement is due to the better reward model or the better generation model.

## Questions
1. How well does ImageReward generalize to unseen prompts?
2. How consistent are the human annotations?
3. How well does the reward model perform on the test set in terms of human preference?
4. How do the baseline methods perform in terms of human preference?
5. How well does the improved model perform on the test set in terms of human preference?

## Flag For Ethics Review
No ethics review needed.

## Details Of Ethics Concerns


## Rating
6

## Confidence
4