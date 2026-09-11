## Reviewer

### Summary

This paper studies the scaling law of RL for LLMs. The authors conduct a large-scale systematic study to analyze the effects of different design choices on the asymptotic performance and compute efficiency. The authors observe that details such as loss aggregation, normalization, curriculum, and off-policy algorithm primarily modulate compute efficiency without materially shifting the asymptote. Based on these insights, the authors propose a best-practice recipe, ScaleRL, and demonstrate its effectiveness by successfully scaling and predicting validation performance on a single RL run scaled up to 100,000 GPU-hours.

### Soundness

3 good

### Presentation

3 good

### Contribution

3 good

### Strengths

1. The paper is well-written and easy to follow.
2. The authors conduct a large-scale systematic study to analyze the effects of different design choices on the asymptotic performance and compute efficiency.
3. The authors propose a best-practice recipe, ScaleRL, and demonstrate its effectiveness by successfully scaling and predicting validation performance on a single RL run scaled up to 100,000 GPU-hours.

### Weaknesses

1. The authors only study the scaling law of RL for LLMs, but do not discuss the scaling law of RL for other tasks, such as robotics and game playing.
2. The authors do not provide a theoretical analysis of the scaling law of RL for LLMs.
3. The authors do not discuss the limitations of the proposed method.

### Questions

1. Can you provide a theoretical analysis of the scaling law of RL for LLMs?
2. Can you discuss the limitations of the proposed method?
3. Can you provide more details about the experimental setup, such as the hardware and software used?

### Flag For Ethics Review

No ethics review needed.

### Rating

6: marginally above the acceptance threshold

### Confidence

3: You are fairly confident in your assessment. It is possible that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work. Math/other details were not carefully checked.

**********

## Reviewer

### Summary

This paper proposes a framework for analyzing and predicting RL scaling in LLMs. The authors fit sigmoidal compute-performance curves for RL training and ablate a wide range of common design choices to analyze their effects on asymptotic performance and compute efficiency. They observe that not all recipes yield similar asymptotic performance, and details such as loss aggregation, normalization, curriculum, and off-policy algorithm primarily modulate compute efficiency without materially shifting the asymptote. The authors propose a best-practice recipe, ScaleRL, and demonstrate its effectiveness by successfully scaling and predicting validation performance on a single RL run scaled up to 100,000 GPU-hours.

### Soundness

3 good

### Presentation

3 good

### Contribution

3 good

### Strengths

1. The paper is well-written and easy to follow.
2. The authors conduct a large-scale systematic study to analyze the effects of different design choices on the asymptotic performance and compute efficiency.
3. The authors propose a best-practice recipe, ScaleRL, and demonstrate its effectiveness by successfully scaling and predicting validation performance on a single RL run scaled up to 100,000 GPU-hours.

### Weaknesses

1. The authors only study the scaling law of RL for LLMs, but do not discuss the scaling law of RL for other tasks, such as robotics and game playing.
2. The authors do not provide a theoretical analysis of the scaling law of RL for LLMs.
3. The authors do not discuss the limitations of the proposed method.

### Questions

1. Can you provide a theoretical analysis of the scaling law of RL for LLMs?
2. Can you discuss the limitations of the proposed method?
3. Can you provide more details about the experimental setup, such as the hardware and software used?

### Flag For Ethics Review

No ethics review needed.

### Rating

6: marginally above the acceptance threshold

### Confidence

3: You are fairly confident in your assessment. It is possible that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work. Math/other details were not carefully checked.

**********

## Reviewer

### Summary

This paper proposes a framework for analyzing and predicting RL scaling in LLMs. The authors fit sigmoidal compute-performance curves for RL training and ablate a wide range of common design choices to analyze their effects on asymptotic performance and compute efficiency. They observe that not all recipes yield similar asymptotic performance, and details such as loss aggregation, normalization, curriculum, and off-policy algorithm primarily modulate compute efficiency without materially shifting the asymptote. The authors propose a best-practice recipe, ScaleRL, and demonstrate its effectiveness by successfully scaling and predicting validation performance on a single RL run scaled up to 100,000 GPU-hours.

### Soundness

3 good

### Presentation

3 good

### Contribution

3 good

### Strengths

1. The paper is well-written and easy to follow.
2. The authors conduct a large-scale systematic study to analyze the effects of different design choices on the asymptotic performance and compute efficiency.
3. The authors propose a best-practice recipe, ScaleRL, and demonstrate its effectiveness by successfully scaling and predicting validation performance on a single RL run scaled up to 100,000 GPU-hours.

### Weaknesses

1. The authors only study the scaling law of RL for LLMs, but do not discuss the scaling law of RL for other tasks, such as robotics and game playing.
2. The authors do not provide a theoretical analysis of the scaling law of RL for LLMs.
3. The authors do not discuss the limitations of the proposed method.

### Questions

1. Can you provide a theoretical analysis of the scaling law of RL for LLMs?
2. Can you discuss the limitations of the proposed method?
3. Can you provide more details about the experimental setup, such as the hardware and software used?

### Flag For Ethics Review

No ethics review needed.

### Rating

6: marginally above the acceptance threshold

### Confidence

3: You are fairly confident in your assessment. It is possible that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work. Math/other details were not carefully checked.

**********

## Reviewer

### Summary

The paper presents a large-scale study of RL scaling in LLMs. The authors fit sigmoidal compute-performance curves for RL training and ablate a wide range of common design choices to analyze their effects on asymptotic performance and compute efficiency. They observe that not all recipes yield similar asymptotic performance, and details such as loss aggregation, normalization, curriculum, and off-policy algorithm primarily modulate compute efficiency without materially shifting the asymptote. The authors propose a best-practice recipe, ScaleRL, and demonstrate its effectiveness by successfully scaling and predicting validation performance on a single RL run scaled up to 100,000 GPU-hours.

### Soundness

3 good

### Presentation

3 good

### Contribution

3 good

### Strengths

1. The paper is well-written and easy to follow.
2. The authors conduct a large-scale systematic study to analyze the effects of different design choices on the asymptotic performance and compute efficiency.
3. The authors propose a best-practice recipe, ScaleRL, and demonstrate its effectiveness by successfully scaling and predicting validation performance on a single RL run scaled up to 100,000 GPU-hours.

### Weaknesses

1. The authors only study the scaling law of RL for LLMs, but do not discuss the scaling law of RL for other tasks, such as robotics and game playing.
2. The authors do not provide a theoretical analysis of the scaling law of RL for LLMs.
3. The authors do not discuss the limitations of the proposed method.

### Questions

1. Can you provide a theoretical analysis of the scaling law of RL for LLMs?
2. Can you discuss the limitations of the proposed method?
3. Can you provide more details about the experimental setup, such as the hardware and software used?

### Flag For Ethics Review

No ethics review needed.

### Rating

6: marginally above the acceptance threshold

### Confidence

3: You are fairly confident in your assessment. It is possible that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work. Math/other details were not carefully checked.

**********

## Meta Review

This paper presents a large-scale study of RL scaling in LLMs. The authors fit sigmoidal compute-performance curves for RL training and ablate a wide range of common design choices to analyze their effects on asymptotic performance and compute efficiency. They observe that not all recipes yield similar asymptotic performance, and details such as loss aggregation, normalization, curriculum, and off-policy algorithm primarily modulate compute efficiency without materially shifting the asymptote. The authors propose a best-practice recipe, ScaleRL, and demonstrate its effectiveness by successfully scaling and predicting validation performance on a single RL run scaled up to 100,000 GPU-hours.

### justification_for_why_not_higher_score

This paper is a good contribution to the community. However, the paper is not a breakthrough.

### justification_for_why_not_lower_score

This paper is a good contribution to the community. However, the paper is not a breakthrough.

**********

## Paper Decision

Accept (poster)