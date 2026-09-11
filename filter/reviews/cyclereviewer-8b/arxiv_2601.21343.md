## Summary

This paper presents two approaches to improve the training of large language models (LLMs). The first approach, "Self-Improving Pretraining," uses a strong, post-trained model to improve earlier stages of training by rewriting pretraining data and judging policy model rollouts. The second approach, "Thinking Mid-training," introduces an intermediate training phase that teaches models to reason on augmented pretraining corpora, bridging the gap between pretraining and post-training. The authors demonstrate that both methods can improve the factuality, safety, and generation quality of pretrained models.

## Soundness

2 fair

## Presentation

2 fair

## Contribution

2 fair

## Strengths

1. The paper proposes a novel approach to improve the training of large language models by introducing an intermediate training phase that teaches models to reason on augmented pretraining corpora. This approach bridges the gap between pretraining and post-training, allowing models to acquire reasoning capabilities earlier in their training pipeline.

2. The paper demonstrates that the proposed approach can improve the factuality, safety, and generation quality of pretrained models. This is a significant contribution, as it addresses some of the limitations of current LLM training methods.

3. The paper is well-structured and easy to follow. The authors provide a clear description of their approach and the results of their experiments.

## Weaknesses

1. The paper lacks a clear comparison with existing methods. The authors should provide a more comprehensive comparison with other approaches to improve the training of LLMs, such as chain-of-thought and reasoning-based pretraining.

2. The paper does not provide a detailed analysis of the limitations of the proposed approach. The authors should discuss the potential limitations of their method and how they plan to address them in future work.

3. The paper does not provide a clear explanation of how the proposed approach can be scaled to larger models. The authors should discuss the scalability of their method and how it can be applied to larger models.

## Questions

1. How does the proposed approach compare to other methods for improving the training of LLMs, such as chain-of-thought and reasoning-based pretraining?

2. What are the limitations of the proposed approach, and how do you plan to address them in future work?

3. How can the proposed approach be scaled to larger models?

## Flag For Ethics Review

No ethics review needed.

## Rating

5: marginally below the acceptance threshold

## Confidence

4: You are confident in your assessment, but not absolutely certain. It is unlikely, but not impossible, that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work.

**********

------------------

## Summary

This paper proposes a new pretraining method that uses a strong, post-trained model to rewrite pretraining data and judge policy model rollouts, incorporating desirable behaviors like safety and factuality earlier in training. The method shows strong gains in quality, safety, factuality, and reasoning.

## Soundness

3 good

## Presentation

3 good

## Contribution

3 good

## Strengths

1. The paper proposes a new approach to pretraining that incorporates desirable behaviors like safety and factuality earlier in training, which is an important problem in the field.
2. The method shows strong gains in quality, safety, factuality, and reasoning, which is a significant contribution to the field.
3. The paper is well-written and easy to follow.

## Weaknesses

1. The paper lacks a detailed discussion of the limitations of the proposed method. While the method shows strong gains in quality, safety, factuality, and reasoning, it is not clear how these gains are achieved or what the limitations of the method are.
2. The paper does not provide a clear comparison with existing methods. While the method shows strong gains in quality, safety, factuality, and reasoning, it is not clear how these gains compare to existing methods.
3. The paper does not provide a clear explanation of how the proposed method can be scaled to larger models. While the method shows strong gains in quality, safety, factuality, and reasoning, it is not clear how these gains can be achieved in larger models.

## Questions

1. How does the proposed method compare to existing methods in terms of quality, safety, factuality, and reasoning?
2. What are the limitations of the proposed method, and how can they be addressed?
3. How can the proposed method be scaled to larger models, and what are the expected gains in quality, safety, factuality, and reasoning?

## Flag For Ethics Review

No ethics review needed.

## Rating

5: marginally below the acceptance threshold

## Confidence

3: You are fairly confident in your assessment. It is possible that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work. Math/other details were not carefully checked.

**********

------------------

## Summary

The paper proposes a new approach to pretraining that incorporates desirable behaviors like safety and factuality earlier in training, using a strong, post-trained model to rewrite pretraining data and judge policy model rollouts. The method shows strong gains in quality, safety, factuality, and reasoning. The paper also introduces an intermediate training phase that teaches models to reason on augmented pretraining corpora, bridging the gap between pretraining and post-training. The method shows strong gains in quality, safety, factuality, and reasoning.

## Soundness

3 good

## Presentation

3 good

## Contribution

3 good

## Strengths

1. The paper proposes a new approach to pretraining that incorporates desirable behaviors like safety and factuality earlier in training, which is an important problem in the field.
2. The method shows strong gains in quality, safety, factuality, and reasoning, which is a significant contribution to the field.
3. The paper is well-written and easy to follow.

## Weaknesses

1. The paper lacks a detailed discussion of the limitations of the proposed method. While the method shows strong gains in quality, safety, factuality, and reasoning, it is not clear how these gains are achieved or what the limitations of the method are.
2. The paper does not provide a clear comparison with existing methods. While the method shows strong gains in quality, safety, factuality, and reasoning, it is not clear how these gains compare to existing methods.
3. The paper does not provide a clear explanation of how the proposed method can be scaled to larger models. While the method shows strong gains in quality, safety, factuality, and reasoning, it is not clear how these gains can be achieved in larger models.

## Questions

1. How does the proposed method compare to existing methods in terms of quality, safety, factuality, and reasoning?
2. What are the limitations of the proposed method, and how can they be addressed?
3. How can the proposed method be scaled to larger models, and what are the expected gains in quality, safety, factuality, and reasoning?

## Flag For Ethics Review

No ethics review needed.

## Rating

5: marginally below the acceptance threshold

## Confidence

3: You are fairly confident in your assessment. It is possible that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work. Math/other details were not carefully checked.

**********

------------------

## Summary

This paper proposes two new approaches to improve the training of LLMs. The first approach, "Self-Improving Pretraining," uses a strong, post-trained model to rewrite pretraining data and judge policy model rollouts. The second approach, "Thinking Mid-training," introduces an intermediate training phase that teaches models to reason on augmented pretraining corpora. The authors demonstrate that both methods can improve the factuality, safety, and generation quality of pretrained models.

## Soundness

3 good

## Presentation

3 good

## Contribution

3 good

## Strengths

The paper proposes a new approach to pretraining that incorporates desirable behaviors like safety and factuality earlier in training, which is an important problem in the field.

## Weaknesses

The paper lacks a detailed discussion of the limitations of the proposed method. While the method shows strong gains in quality, safety, factuality, and reasoning, it is not clear how these gains are achieved or what the limitations of the method are.

## Questions

How does the proposed method compare to existing methods in terms of quality, safety, factuality, and reasoning?

## Flag For Ethics Review

No ethics review needed.

## Rating

5: marginally below the acceptance threshold

## Confidence

3: You are fairly confident in your assessment. It is possible that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work. Math/other details were not carefully checked.

**********

------------------

## Meta Review

This paper presents two approaches to improve the training of large language models (LLMs). The first approach, "Self-Improving Pretraining," uses a strong, post-trained model to rewrite pretraining data and judge policy model rollouts. The second approach, "Thinking Mid-training," introduces an intermediate training phase that teaches models to reason on augmented pretraining corpora, bridging the gap between pretraining and post-training. The authors demonstrate that both methods can improve the factuality, safety, and generation quality of pretrained models. The reviewers have raised concerns about the lack of a detailed discussion of the limitations of the proposed method, the lack of a clear comparison with existing methods, and the lack of a clear explanation of how the proposed method can be scaled to larger models. The authors have provided some clarifications and additional results in their rebuttal, but the reviewers have not been convinced that these concerns have been fully addressed. Therefore, the paper is not recommended for acceptance at this time.

## justification_for_why_not_higher_score

The reviewers have raised concerns about the lack of a detailed discussion of the limitations of the proposed method, the lack of a clear comparison with existing methods, and the lack of a clear explanation of how the proposed method can be scaled to larger models.

## justification_for_why_not_lower_score

N/A

**********

---

## Paper Decision

Reject (not selected for publication)