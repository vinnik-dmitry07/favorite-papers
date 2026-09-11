# Review

## Summary
This paper proposes a method to reuse the KV cache when swapping models in an LLM family, which can save the prefilling cost. The authors find that the KV cache has a substantial linear structure across matched-KV pairs. Based on this observation, they design a closed-form ridge mapper that operates per head and proceeds in three steps. The evaluation shows that this method can achieve 73–98% of the receiver’s standalone-prefill accuracy on four pairs, while two degrade sharply. The nonlinear MLP recovers the performance on the failed pairs.

## Soundness
3

## Presentation
3

## Contribution
3

## Strengths
1. The paper is well-written and easy to follow.
2. The problem studied in this paper is interesting and practical. 
3. The proposed method is simple and effective. 
4. The experiments are comprehensive and the analysis is insightful.

## Weaknesses
1. The proposed method is limited to the in-family setting, i.e., the source and target models should be from the same model family and share the same KV cache structure. 
2. The proposed method is only evaluated on a few pairs of models. Although the authors have explained that they focus on the in-family setting and the models should share the same KV cache structure, it would be better to include more pairs of models from different families (but with the same KV cache structure) to verify the generalizability of the method.

## Questions
Please refer to the weaknesses.

## Flag For Ethics Review
No ethics review needed.

## Details Of Ethics Concerns


## Rating
6

## Confidence
4