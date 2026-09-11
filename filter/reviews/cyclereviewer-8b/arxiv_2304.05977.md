## Reviewer

### Summary

This paper proposes ImageReward, a human preference reward model for text-to-image generation. It is trained on 137k expert comparisons, and outperforms existing scoring models and metrics in human evaluation. The authors also propose a direct tuning algorithm, Reward Feedback Learning (ReFL), to optimize diffusion models against the ImageReward. The results show that ReFL improves the performance of diffusion models in terms of human preference.

### Soundness

3 good

### Presentation

3 good

### Contribution

3 good

### Strengths

- This paper proposes a novel reward model for text-to-image generation, which is trained on 137k expert comparisons. 
- The proposed reward model outperforms existing scoring models and metrics in human evaluation.
- The authors also propose a direct tuning algorithm, Reward Feedback Learning (ReFL), to optimize diffusion models against the ImageReward.
- The results show that ReFL improves the performance of diffusion models in terms of human preference.

### Weaknesses

- The authors only compared their method with a few existing methods, and it would be better if they could compare with more existing methods in the field. 
- The authors only tested their method on a small set of prompts, and it would be better if they could test their method on a larger set of prompts. 
- The authors only tested their method on a single diffusion model, and it would be better if they could test their method on multiple diffusion models. 
- The authors only tested their method on a single dataset, and it would be better if they could test their method on multiple datasets. 
- The authors only tested their method on a single evaluation metric, and it would be better if they could test their method on multiple evaluation metrics.

### Questions

- How does the ImageReward perform on other text-to-image models such as DALL-E 2 and CogView 2? 
- How does the ImageReward perform on other evaluation metrics such as Inception Score (IS) and Fréchet Inception Distance (FID)? 
- How does the ReFL perform on other text-to-image models such as DALL-E 2 and CogView 2? 
- How does the ReFL perform on other evaluation metrics such as Inception Score (IS) and Fréchet Inception Distance (FID)? 
- How does the ImageReward perform on other datasets such as COCO and LAION? 
- How does the ReFL perform on other datasets such as COCO and LAION? 
- How does the ImageReward perform on other types of prompts such as short text prompts and long text prompts? 
- How does the ReFL perform on other types of prompts such as short text prompts and long text prompts?

### Flag For Ethics Review

No ethics review needed.

### Rating

5: marginally below the acceptance threshold

### Confidence

4: You are confident in your assessment, but not absolutely certain. It is unlikely, but not impossible, that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work.

**********

## Reviewer

### Summary

This paper proposes a novel approach for learning human preference reward model for text-to-image generation. The authors first collect a large-scale dataset of expert comparisons between generated images and then train a reward model based on the collected data. The proposed reward model is evaluated against existing scoring models and metrics, and it outperforms them in human evaluation. The authors also propose a direct tuning algorithm, Reward Feedback Learning (ReFL), to optimize diffusion models against the reward model. The results show that ReFL improves the performance of diffusion models in terms of human preference.

### Soundness

3 good

### Presentation

3 good

### Contribution

3 good

### Strengths

The proposed reward model is trained on a large-scale dataset of expert comparisons, which is more reliable than existing scoring models and metrics. The authors also propose a direct tuning algorithm, Reward Feedback Learning (ReFL), to optimize diffusion models against the reward model, which is more efficient than the generate-and-then-filter paradigm.

### Weaknesses

The authors only compared their method with a few existing methods, and it would be better if they could compare with more existing methods in the field. The authors only tested their method on a small set of prompts, and it would be better if they could test their method on a larger set of prompts. The authors only tested their method on a single diffusion model, and it would be better if they could test their method on multiple diffusion models. The authors only tested their method on a single dataset, and it would be better if they could test their method on multiple datasets. The authors only tested their method on a single evaluation metric, and it would be better if they could test their method on multiple evaluation metrics.

### Questions

Please see the weaknesses above.

### Flag For Ethics Review

No ethics review needed.

### Rating

5: marginally below the acceptance threshold

### Confidence

3: You are fairly confident in your assessment. It is possible that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work. Math/other details were not carefully checked.

**********

## Reviewer

### Summary

The paper proposes a reward model for text-to-image generation, which is trained on a large-scale dataset of expert comparisons. The reward model is evaluated against existing scoring models and metrics, and it outperforms them in human evaluation. The authors also propose a direct tuning algorithm, Reward Feedback Learning (ReFL), to optimize diffusion models against the reward model. The results show that ReFL improves the performance of diffusion models in terms of human preference.

### Soundness

3 good

### Presentation

3 good

### Contribution

3 good

### Strengths

1. The paper proposes a novel approach for learning human preference reward model for text-to-image generation, which is trained on a large-scale dataset of expert comparisons.
2. The proposed reward model is evaluated against existing scoring models and metrics, and it outperforms them in human evaluation.
3. The authors also propose a direct tuning algorithm, Reward Feedback Learning (ReFL), to optimize diffusion models against the reward model, which is more efficient than the generate-and-then-filter paradigm.

### Weaknesses

1. The paper only evaluates the proposed method on a small set of prompts, and it would be better if the authors could test their method on a larger set of prompts.
2. The paper only evaluates the proposed method on a single diffusion model, and it would be better if the authors could test their method on multiple diffusion models.
3. The paper only evaluates the proposed method on a single dataset, and it would be better if the authors could test their method on multiple datasets.
4. The paper only evaluates the proposed method on a single evaluation metric, and it would be better if the authors could test their method on multiple evaluation metrics.

### Questions

1. How does the ImageReward perform on other text-to-image models such as DALL-E 2 and CogView 2?
2. How does the ImageReward perform on other evaluation metrics such as Inception Score (IS) and Fréchet Inception Distance (FID)?
3. How does the ReFL perform on other text-to-image models such as DALL-E 2 and CogView 2?
4. How does the ReFL perform on other evaluation metrics such as Inception Score (IS) and Fréchet Inception Distance (FID)?
5. How does the ImageReward perform on other datasets such as COCO and LAION?
6. How does the ReFL perform on other datasets such as COCO and LAION?
7. How does the ImageReward perform on other types of prompts such as short text prompts and long text prompts?
8. How does the ReFL perform on other types of prompts such as short text prompts and long text prompts?

### Flag For Ethics Review

No ethics review needed.

### Rating

5: marginally below the acceptance threshold

### Confidence

3: You are fairly confident in your assessment. It is possible that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work. Math/other details were not carefully checked.

**********

## Reviewer

### Summary

The paper proposes a reward model for text-to-image generation. The reward model is trained on a large-scale dataset of expert comparisons. The reward model is evaluated against existing scoring models and metrics, and it outperforms them in human evaluation. The authors also propose a direct tuning algorithm, Reward Feedback Learning (ReFL), to optimize diffusion models against the reward model. The results show that ReFL improves the performance of diffusion models in terms of human preference.

### Soundness

3 good

### Presentation

3 good

### Contribution

3 good

### Strengths

1. The paper proposes a novel approach for learning human preference reward model for text-to-image generation, which is trained on a large-scale dataset of expert comparisons.
2. The proposed reward model is evaluated against existing scoring models and metrics, and it outperforms them in human evaluation.
3. The authors also propose a direct tuning algorithm, Reward Feedback Learning (ReFL), to optimize diffusion models against the reward model, which is more efficient than the generate-and-then-filter paradigm.

### Weaknesses

1. The paper only evaluates the proposed method on a small set of prompts, and it would be better if the authors could test their method on a larger set of prompts.
2. The paper only evaluates the proposed method on a single diffusion model, and it would be better if the authors could test their method on multiple diffusion models.
3. The paper only evaluates the proposed method on a single dataset, and it would be better if the authors could test their method on multiple datasets.
4. The paper only evaluates the proposed method on a single evaluation metric, and it would be better if the authors could test their method on multiple evaluation metrics.

### Questions

1. How does the ImageReward perform on other text-to-image models such as DALL-E 2 and CogView 2?
2. How does the ImageReward perform on other evaluation metrics such as Inception Score (IS) and Fréchet Inception Distance (FID)?
3. How does the ReFL perform on other text-to-image models such as DALL-E 2 and CogView 2?
4. How does the ReFL perform on other evaluation metrics such as Inception Score (IS) and Fréchet Inception Distance (FID)?
5. How does the ImageReward perform on other datasets such as COCO and LAION?
6. How does the ReFL perform on other datasets such as COCO and LAION?
7. How does the ImageReward perform on other types of prompts such as short text prompts and long text prompts?
8. How does the ReFL perform on other types of prompts such as short text prompts and long text prompts?

### Flag For Ethics Review

No ethics review needed.

### Rating

5: marginally below the acceptance threshold

### Confidence

3: You are fairly confident in your assessment. It is possible that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work. Math/other details were not carefully checked.

**********

## Meta Review

The paper proposes a reward model for text-to-image generation, which is trained on a large-scale dataset of expert comparisons. The reward model is evaluated against existing scoring models and metrics, and it outperforms them in human evaluation. The authors also propose a direct tuning algorithm, Reward Feedback Learning (ReFL), to optimize diffusion models against the reward model. The results show that ReFL improves the performance of diffusion models in terms of human preference.

The reviewers have raised several concerns regarding the evaluation of the proposed method. The reviewers have pointed out that the proposed method has not been evaluated on a wide range of text-to-image models, datasets, and evaluation metrics. The reviewers have also suggested that the authors should provide more details on the annotation process and the characteristics of the dataset used to train the reward model. Additionally, the reviewers have raised concerns about the robustness of the proposed method to different types of prompts and the generalizability of the results to other domains.

### justification_for_why_not_higher_score

The reviewers have raised several concerns regarding the evaluation of the proposed method. The reviewers have pointed out that the proposed method has not been evaluated on a wide range of text-to-image models, datasets, and evaluation metrics. The reviewers have also suggested that the authors should provide more details on the annotation process and the characteristics of the dataset used to train the reward model. Additionally, the reviewers have raised concerns about the robustness of the proposed method to different types of prompts and the generalizability of the results to other domains.

### justification_for_why_not_lower_score

N/A

**********

## Paper Decision

Reject (not selected for publication)