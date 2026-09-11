## Reviewer

### Summary

This paper studies the problem of reward model overoptimization in RLHF. The authors use a synthetic setup with a gold-standard reward model to study the relationship between the gold reward model score and the KL divergence between the initial and optimized policies. The authors find that this relationship follows a different functional form depending on the method of optimization, and that the coefficients of this relationship scale smoothly with the number of reward model parameters. The authors also study the effect on this relationship of the size of the reward model dataset, the number of reward model and policy parameters, and the coefficient of the KL penalty added to the reward in the reinforcement learning setup.

### Soundness

3 good

### Presentation

3 good

### Contribution

2 fair

### Strengths

The paper studies an important problem in RLHF, namely reward model overoptimization. The authors use a synthetic setup to study the relationship between the gold reward model score and the KL divergence between the initial and optimized policies. The authors find that this relationship follows a different functional form depending on the method of optimization, and that the coefficients of this relationship scale smoothly with the number of reward model parameters. The authors also study the effect on this relationship of the size of the reward model dataset, the number of reward model and policy parameters, and the coefficient of the KL penalty added to the reward in the reinforcement learning setup.

### Weaknesses

1. The paper does not provide a clear motivation for why the synthetic setup is a good proxy for real-world RLHF. The authors acknowledge this limitation in the paper, but do not provide any evidence that the synthetic setup is a good approximation of real-world RLHF.
2. The paper does not provide a clear explanation of how the results can be used to improve RLHF. The authors find that the relationship between the gold reward model score and the KL divergence between the initial and optimized policies follows a different functional form depending on the method of optimization, and that the coefficients of this relationship scale smoothly with the number of reward model parameters. However, it is not clear how this information can be used to improve RLHF.
3. The paper does not provide a clear explanation of how the results can be used to improve the design of reward models. The authors find that the size of the reward model dataset, the number of reward model and policy parameters, and the coefficient of the KL penalty added to the reward in the reinforcement learning setup affect the relationship between the gold reward model score and the KL divergence between the initial and optimized policies. However, it is not clear how this information can be used to improve the design of reward models.
4. The paper does not provide a clear explanation of how the results can be used to improve the design of RL algorithms. The authors find that the relationship between the gold reward model score and the KL divergence between the initial and optimized policies follows a different functional form depending on the method of optimization, and that the coefficients of this relationship scale smoothly with the number of reward model parameters. However, it is not clear how this information can be used to improve the design of RL algorithms.

### Questions

1. Can you provide a clear motivation for why the synthetic setup is a good proxy for real-world RLHF? 
2. Can you provide a clear explanation of how the results can be used to improve RLHF? 
3. Can you provide a clear explanation of how the results can be used to improve the design of reward models? 
4. Can you provide a clear explanation of how the results can be used to improve the design of RL algorithms?

### Flag For Ethics Review

No ethics review needed.

### Rating

5: marginally below the acceptance threshold

### Confidence

4: You are confident in your assessment, but not absolutely certain. It is unlikely, but not impossible, that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work.

**********

## Reviewer

### Summary

This paper studies the effect of overoptimization in reinforcement learning from human feedback (RLHF). In particular, it studies the relationship between the gold reward model score and the KL divergence between the initial and optimized policies. The authors find that this relationship follows a different functional form depending on the method of optimization, and that the coefficients of this relationship scale smoothly with the number of reward model parameters. They also study the effect on this relationship of the size of the reward model dataset, the number of reward model and policy parameters, and the coefficient of the KL penalty added to the reward in the reinforcement learning setup.

### Soundness

3 good

### Presentation

3 good

### Contribution

2 fair

### Strengths

- The paper studies an important problem in RLHF, namely reward model overoptimization. The authors use a synthetic setup to study the relationship between the gold reward model score and the KL divergence between the initial and optimized policies. The authors find that this relationship follows a different functional form depending on the method of optimization, and that the coefficients of this relationship scale smoothly with the number of reward model parameters. The authors also study the effect on this relationship of the size of the reward model dataset, the number of reward model and policy parameters, and the coefficient of the KL penalty added to the reward in the reinforcement learning setup.
- The paper is well-written and easy to follow. The authors provide a clear explanation of their methodology and results, and the paper is well-organized and easy to understand.

### Weaknesses

- The paper does not provide a clear explanation of how the results can be used to improve RLHF. The authors find that the relationship between the gold reward model score and the KL divergence between the initial and optimized policies follows a different functional form depending on the method of optimization, and that the coefficients of this relationship scale smoothly with the number of reward model parameters. However, it is not clear how this information can be used to improve RLHF.
- The paper does not provide a clear explanation of how the results can be used to improve the design of reward models. The authors find that the size of the reward model dataset, the number of reward model and policy parameters, and the coefficient of the KL penalty added to the reward in the reinforcement learning setup affect the relationship between the gold reward model score and the KL divergence between the initial and optimized policies. However, it is not clear how this information can be used to improve the design of reward models.
- The paper does not provide a clear explanation of how the results can be used to improve the design of RL algorithms. The authors find that the relationship between the gold reward model score and the KL divergence between the initial and optimized policies follows a different functional form depending on the method of optimization, and that the coefficients of this relationship scale smoothly with the number of reward model parameters. However, it is not clear how this information can be used to improve the design of RL algorithms.

### Questions

- Can you provide a clear motivation for why the synthetic setup is a good proxy for real-world RLHF? 
- Can you provide a clear explanation of how the results can be used to improve RLHF? 
- Can you provide a clear explanation of how the results can be used to improve the design of reward models? 
- Can you provide a clear explanation of how the results can be used to improve the design of RL algorithms?

### Flag For Ethics Review

No ethics review needed.

### Rating

5: marginally below the acceptance threshold

### Confidence

2: You are willing to defend your assessment, but it is quite likely that you did not understand the central parts of the submission or that you are unfamiliar with some pieces of related work. Math/other details were not carefully checked.

**********

## Reviewer

### Summary

The paper studies the phenomenon of overoptimization in RLHF. The authors use a synthetic setup in which a fixed “gold-standard” reward model plays the role of humans, providing labels used to train a proxy reward model. They study how the gold reward model score changes as they optimize against the proxy reward model using either reinforcement learning or best-of-n sampling. They find that this relationship follows a different functional form depending on the method of optimization, and that in both cases its coefficients scale smoothly with the number of reward model parameters. They also study the effect on this relationship of the size of the reward model dataset, the number of reward model and policy parameters, and the coefficient of the KL penalty added to the reward in the reinforcement learning setup.

### Soundness

3 good

### Presentation

3 good

### Contribution

2 fair

### Strengths

The paper studies an important problem in RLHF, namely reward model overoptimization. The authors use a synthetic setup to study the relationship between the gold reward model score and the KL divergence between the initial and optimized policies. The authors find that this relationship follows a different functional form depending on the method of optimization, and that the coefficients of this relationship scale smoothly with the number of reward model parameters. The authors also study the effect on this relationship of the size of the reward model dataset, the number of reward model and policy parameters, and the coefficient of the KL penalty added to the reward in the reinforcement learning setup.

### Weaknesses

The paper does not provide a clear explanation of how the results can be used to improve RLHF. The authors find that the relationship between the gold reward model score and the KL divergence between the initial and optimized policies follows a different functional form depending on the method of optimization, and that the coefficients of this relationship scale smoothly with the number of reward model parameters. However, it is not clear how this information can be used to improve RLHF.

The paper does not provide a clear explanation of how the results can be used to improve the design of reward models. The authors find that the size of the reward model dataset, the number of reward model and policy parameters, and the coefficient of the KL penalty added to the reward in the reinforcement learning setup affect the relationship between the gold reward model score and the KL divergence between the initial and optimized policies. However, it is not clear how this information can be used to improve the design of reward models.

The paper does not provide a clear explanation of how the results can be used to improve the design of RL algorithms. The authors find that the relationship between the gold reward model score and the KL divergence between the initial and optimized policies follows a different functional form depending on the method of optimization, and that the coefficients of this relationship scale smoothly with the number of reward model parameters. However, it is not clear how this information can be used to improve the design of RL algorithms.

### Questions

Can you provide a clear motivation for why the synthetic setup is a good proxy for real-world RLHF? 
Can you provide a clear explanation of how the results can be used to improve RLHF? 
Can you provide a clear explanation of how the results can be used to improve the design of reward models? 
Can you provide a clear explanation of how the results can be used to improve the design of RL algorithms?

### Flag For Ethics Review

No ethics review needed.

### Rating

5: marginally below the acceptance threshold

### Confidence

2: You are willing to defend your assessment, but it is quite likely that you did not understand the central parts of the submission or that you are unfamiliar with some pieces of related work. Math/other details were not carefully checked.

**********

## Reviewer

### Summary

This paper studies the effect of optimizing a reward model on the gold reward model score. The authors use a synthetic setup with a fixed gold reward model and a proxy reward model. They find that the relationship between the gold reward model score and the KL divergence between the initial and optimized policies follows a different functional form depending on the method of optimization. They also study the effect on this relationship of the size of the reward model dataset, the number of reward model and policy parameters, and the coefficient of the KL penalty added to the reward in the reinforcement learning setup.

### Soundness

3 good

### Presentation

3 good

### Contribution

3 good

### Strengths

The paper studies an important problem in RLHF, namely reward model overoptimization. The authors use a synthetic setup to study the relationship between the gold reward model score and the KL divergence between the initial and optimized policies. The authors find that this relationship follows a different functional form depending on the method of optimization, and that the coefficients of this relationship scale smoothly with the number of reward model parameters. The authors also study the effect on this relationship of the size of the reward model dataset, the number of reward model and policy parameters, and the coefficient of the KL penalty added to the reward in the reinforcement learning setup.

### Weaknesses

The paper does not provide a clear explanation of how the results can be used to improve RLHF. The authors find that the relationship between the gold reward model score and the KL divergence between the initial and optimized policies follows a different functional form depending on the method of optimization, and that the coefficients of this relationship scale smoothly with the number of reward model parameters. However, it is not clear how this information can be used to improve RLHF.

The paper does not provide a clear explanation of how the results can be used to improve the design of reward models. The authors find that the size of the reward model dataset, the number of reward model and policy parameters, and the coefficient of the KL penalty added to the reward in the reinforcement learning setup affect the relationship between the gold reward model score and the KL divergence between the initial and optimized policies. However, it is not clear how this information can be used to improve the design of reward models.

The paper does not provide a clear explanation of how the results can be used to improve the design of RL algorithms. The authors find that the relationship between the gold reward model score and the KL divergence between the initial and optimized policies follows a different functional form depending on the method of optimization, and that the coefficients of this relationship scale smoothly with the number of reward model parameters. However, it is not clear how this information can be used to improve the design of RL algorithms.

### Questions

Can you provide a clear motivation for why the synthetic setup is a good proxy for real-world RLHF? 
Can you provide a clear explanation of how the results can be used to improve RLHF? 
Can you provide a clear explanation of how the results can be used to improve the design of reward models? 
Can you provide a clear explanation of how the results can be used to improve the design of RL algorithms?

### Flag For Ethics Review

No ethics review needed.

### Rating

5: marginally below the acceptance threshold

### Confidence

2: You are willing to defend your assessment, but it is quite likely that you did not understand the central parts of the submission or that you are unfamiliar with some pieces of related work. Math/other details were not carefully checked.

**********

## Meta Review

This paper studies the phenomenon of overoptimization in RLHF. The authors use a synthetic setup in which a fixed “gold-standard” reward model plays the role of humans, providing labels used to train a proxy reward model. They study how the gold reward model score changes as they optimize against the proxy reward model using either reinforcement learning or best-of-n sampling. They find that this relationship follows a different functional form depending on the method of optimization, and that in both cases its coefficients scale smoothly with the number of reward model parameters. They also study the effect on this relationship of the size of the reward model dataset, the number of reward model and policy parameters, and the coefficient of the KL penalty added to the reward in the reinforcement learning setup.

The reviewers all agree that this paper studies an important problem in RLHF, namely reward model overoptimization. The authors use a synthetic setup to study the relationship between the gold reward model score and the KL divergence between the initial and optimized policies. The authors find that this relationship follows a different functional form depending on the method of optimization, and that the coefficients of this relationship scale smoothly with the number of reward model parameters. The authors also study the effect on this relationship of the size of the reward model dataset, the number of reward model and policy parameters, and the coefficient of the KL penalty added to the reward in the reinforcement learning setup.

However, the reviewers also raised several concerns. They pointed out that the paper does not provide a clear explanation of how the results can be used to improve RLHF. They also pointed out that the paper does not provide a clear explanation of how the results can be used to improve the design of reward models. Finally, they pointed out that the paper does not provide a clear explanation of how the results can be used to improve the design of RL algorithms.

### justification_for_why_not_higher_score

The reviewers all agree that this paper studies an important problem in RLHF, namely reward model overoptimization. The authors use a synthetic setup to study the relationship between the gold reward model score and the KL divergence between the initial and optimized policies. The authors find that this relationship follows a different functional form depending on the method of optimization, and that the coefficients of this relationship scale smoothly with the number of reward model parameters. The authors also study the effect on this relationship of the size of the reward model dataset, the number of reward model and policy parameters, and the coefficient of the KL penalty added to the reward in the reinforcement learning setup.

However, the reviewers also raised several concerns. They pointed out that the paper does not provide a clear explanation of how the results can be used to improve RLHF. They also pointed out that the paper does not provide a clear explanation of how the results can be used to improve the design of reward models. Finally, they pointed out that the paper does not provide a clear explanation of how the results can be used to improve the design of RL algorithms.

### justification_for_why_not_lower_score

N/A

**********

## Paper Decision

Reject (not selected for a spotlight/oral/poster) **********

**********

# Editor

assistant

## Paper Decision

Reject (not selected for a spotlight/oral/poster)

**********

## Paper Decision Summary

The reviewers all agree that this paper studies an important problem in RLHF, namely reward model overoptimization. The authors use a synthetic setup to study the relationship between the gold reward model score and the KL divergence between the initial and optimized policies. The authors find that this relationship follows a different functional form depending on the method of optimization, and that the coefficients of this relationship scale smoothly with the number of reward model parameters. The authors also study the effect on this relationship of the size of the reward model dataset, the number of reward model and policy parameters, and the coefficient of the KL penalty added to the reward in the reinforcement learning setup.

However, the reviewers also raised several concerns. They pointed out that the paper does not provide a clear explanation of how the results can be used to improve RLHF. They also pointed out that the paper does not provide a clear explanation of how the results can be used to improve the design of reward models. Finally, they pointed out that the paper does not provide a clear explanation of how the results can be used to improve the design of RL algorithms.

**********

## Paper Decision Public Feedback

Dear authors,

Thank you for your submission to ICLR. The reviewers all agree that this paper studies an important problem in RLHF, namely reward model overoptimization. The authors use a synthetic setup to study the relationship between the gold reward model score and the KL divergence between the initial and optimized policies. The authors find that this relationship follows a different functional form depending on the method of optimization, and that the coefficients of this relationship scale smoothly with the number of reward model parameters. The authors also study the effect on this relationship of the size of the reward model dataset, the number of reward model and policy parameters, and the coefficient of the KL penalty added to the reward in the reinforcement learning setup.

However, the reviewers also raised several concerns. They pointed out that the paper does not provide a clear explanation of how the results can be used to improve RLHF. They also pointed out that the paper does not provide a clear explanation of how the results can be used to improve the design of reward models. Finally, they pointed out that the paper does not provide a clear explanation of how the results can be used to improve the design of RL algorithms.

The reviewers all agree that this paper studies an important problem in RLHF, namely reward model overoptimization. The authors use a synthetic setup to study the relationship between the gold reward model score and the KL divergence between the initial and optimized policies. The authors find that this relationship follows a different functional form depending on the method of optimization, and that the coefficients of this relationship scale smoothly with the number of reward model parameters. The authors also study the effect on this relationship of the size of the reward model dataset, the number of reward model and policy parameters, and the coefficient of the KL penalty added to the reward in the reinforcement learning setup.

However, the reviewers also raised several concerns. They pointed out that the paper does not provide a clear explanation of how the results can be used to improve RLHF. They also pointed out that the paper does not provide a clear explanation of how the results can be used to improve the design of reward models. Finally, they pointed out that the paper does not provide a clear explanation of how the results can be used to improve the design of RL algorithms.

I encourage the authors to take the reviewers' comments into consideration and resubmit to a future venue.

Best regards,
ICLR Chair

**********

## Paper Decision Policy

See [this page](https://iclr.cc/Conferences/2024/CallForPapers/policy) for the ICLR 2024 paper decision policy.

**********

**********

# Paper Decision

Reject (not selected for a spotlight/oral/poster)

**********

## Paper Decision Summary

The reviewers all agree that this paper studies an important problem in RLHF, namely reward model overoptimization. The authors use a synthetic setup to study the relationship between the gold reward model score and the KL divergence between the initial and optimized policies. The authors find that this relationship follows a different functional form depending on the method of optimization, and that the coefficients of this relationship scale smoothly with the number of reward model parameters. The authors also study the effect on this relationship of the size of the reward model dataset, the number of reward model and policy parameters, and the coefficient of the KL penalty added to the reward in the reinforcement learning setup.

However, the reviewers also raised several concerns. They pointed out that the paper does not provide a clear explanation of how the results can be used to improve RLHF. They also pointed out that the paper does not provide a clear explanation of how the results can be used to improve the design of reward models. Finally, they pointed out that the paper does not provide a clear explanation of how the results can be used to improve the design of RL algorithms.

**********

## Paper Decision Public Feedback

Dear authors,

Thank you for your submission to ICLR. The reviewers all agree that this paper studies an important problem in RLHF, namely reward model overoptimization. The authors use a synthetic setup to study the relationship between the gold reward model score and the KL divergence between the initial and optimized policies. The authors find that this relationship follows a different functional form depending on the method of optimization, and that the coefficients of this relationship scale smoothly with the number of reward model parameters. The authors also study the effect on this relationship of the size of the reward model dataset, the number of reward model and policy parameters, and the coefficient of the KL penalty added to the reward in the reinforcement learning setup.

However, the reviewers also raised several concerns. They pointed out that the paper does not provide a clear explanation of how the results can be used to improve RLHF. They also pointed out that the paper does not provide a clear explanation of how the results can be used to improve the design of reward models. Finally, they pointed out that the paper does not provide a clear explanation of how the results can be used to improve the design of RL algorithms.

The reviewers all agree that this paper studies an important problem in RLHF, namely reward model overoptimization. The authors use a synthetic setup to study the relationship between the gold reward model score and the KL divergence between the initial and optimized policies. The authors find that this relationship follows a different functional form depending on the method of optimization, and that the coefficients of this relationship scale smoothly with the number of reward model parameters. The authors also study the effect on this relationship of the size of the reward model dataset, the number of reward model and policy parameters, and the coefficient of the KL penalty added to the reward in the reinforcement learning setup.

However, the reviewers also raised several concerns. They pointed out that the paper does not provide a clear explanation of how the results can be used to improve RLHF. They also pointed out that the paper does not provide a clear explanation of how the results can be used to improve the design of reward models. Finally, they pointed out that the paper does not provide a clear explanation of how the results can be used to improve the design of RL algorithms.

I encourage the authors to take the reviewers' comments into consideration and resubmit to a future venue.

Best regards,
ICLR Chair

**********

## Paper Decision Policy

See [this page](https://iclr.cc/Conferences/2024/CallForPapers/policy) for the ICLR 2024 paper decision policy.

**********

**********

# Paper Decision

Reject (not selected for a spotlight/oral/poster)

**********

## Paper Decision Summary

The reviewers all agree that this paper studies an important problem in RLHF, namely reward model overoptimization. The authors use a synthetic setup to study the relationship between the gold reward model score and the KL divergence between the initial and optimized policies. The authors find that this relationship follows a different functional form depending on the method of optimization, and that the coefficients of this relationship scale smoothly with the number of reward model parameters. The authors also study the effect on this relationship of the size of the reward model dataset, the number of reward model and policy parameters, and the coefficient of the KL penalty added to the reward in the reinforcement learning setup.

However, the reviewers also raised several concerns. They pointed out that the paper does not provide a clear explanation of how the results can be used to improve RLHF. They also pointed out that the paper does not provide a clear explanation of how the results can be used to improve the design of reward models. Finally, they pointed out that the paper does not provide a clear explanation of how the results can be used to improve the design of RL algorithms.

**********

## Paper Decision Public Feedback

Dear authors,

Thank you for your submission to ICLR. The reviewers all agree that this paper studies an important problem in RLHF, namely reward model overoptimization. The authors use a synthetic setup to study the relationship between the gold reward model score and the KL divergence between the initial and optimized policies. The authors find that this relationship follows a different functional form depending on the method of optimization, and that the coefficients of this relationship scale smoothly with the number of reward model parameters. The authors also study the effect on this relationship of the size of the reward model dataset, the number of reward model and policy parameters, and the coefficient of the KL penalty added to the reward in the reinforcement learning setup.

However, the reviewers also raised several concerns. They pointed out that the paper does not provide a clear explanation of how the results can be used to improve RLHF. They also pointed out that the paper does not provide a clear explanation of how the results can be used to improve the design of reward models. Finally, they pointed out that the paper does not provide a clear explanation of how the results can be used to improve the design of RL algorithms.

The reviewers all agree that this paper studies an important problem in RLHF, namely reward model overoptimization. The authors use a synthetic setup to study the relationship between the gold reward model score and the KL divergence between the initial and optimized policies. The authors find that this relationship follows a different functional form depending on the method of optimization, and that the coefficients of this relationship scale smoothly with the number of reward model parameters. The authors also study the effect on this relationship of the size of the reward model dataset, the number of reward model and policy parameters, and the coefficient of the KL penalty added to the reward in the reinforcement learning setup.

However, the reviewers also raised several concerns. They pointed out that the paper does not provide a clear explanation of how the results can be used to improve RLHF. They also pointed out that the paper does not provide a clear explanation of how the results can be used to improve the design of reward models. Finally, they pointed out that the paper does not provide a clear explanation of how the results can be used to improve the design of RL algorithms.

I encourage the authors to take the reviewers' comments into consideration and resubmit to a future venue.

Best regards,
ICLR Chair

**********

## Paper Decision Policy

See [this page](https://iclr.cc/Conferences/2024/CallForPapers/policy) for the ICLR 2024 paper decision policy.

**********

**********

# Paper Decision

Reject (not selected for a spotlight/oral/poster)

**********

## Paper Decision Summary

The reviewers all agree that this paper studies an important problem in RLHF, namely reward model overoptimization. The authors use a synthetic setup to study the relationship between the gold reward model score and the KL divergence between the initial and optimized policies. The authors find that this relationship follows a different functional form depending on the method of optimization, and that the coefficients of this relationship scale smoothly with the number of reward model parameters. The authors also study the effect on this relationship of the size of the reward model dataset, the number of reward model and policy parameters, and the coefficient of the KL penalty added to the reward in the reinforcement learning setup.

However, the reviewers also raised several concerns. They pointed out that the paper does not provide a clear explanation of how the results can be used to improve RLHF. They also pointed out that the paper does not provide a clear explanation of how the results can be used to improve the design of reward models. Finally, they pointed out that the paper does not provide a clear explanation of how the results can be used to improve the design of RL algorithms.

**********

## Paper Decision Public Feedback

Dear authors,

Thank you for your submission to ICLR. The reviewers all agree that this paper studies an important problem in RLHF, namely reward model overoptimization. The authors use a synthetic setup to study the relationship between the gold reward model score and the KL divergence between the initial and optimized policies. The authors find that this relationship follows a different functional form depending on the method of optimization, and that the coefficients of this relationship scale smoothly with the number of reward model parameters. The authors also study the effect on this relationship of the size of the reward model dataset, the number of reward model and policy parameters, and the coefficient of the KL penalty added to the reward in the reinforcement learning setup.

However, the reviewers also raised several concerns. They pointed out that the paper does not provide a clear explanation of how the results can be used to improve RLHF. They also pointed out that the paper does not provide a clear explanation of how the results can be used to improve the design of reward models. Finally, they pointed out that the paper does not provide a clear explanation of how the results can be used to improve the design of RL algorithms.

The reviewers all agree that this paper studies an important problem in RLHF, namely reward model overoptimization. The authors use a synthetic setup to study the relationship between the gold reward model score and the KL divergence between the initial and optimized policies. The authors find that this relationship follows a different functional form depending on the method of optimization, and that the coefficients of this relationship scale smoothly with the number of reward model parameters. The authors also study the effect on this relationship of the size of the reward model dataset, the number of reward model and policy parameters, and the coefficient of the KL penalty added to the reward in the reinforcement learning setup.

However, the reviewers also raised several concerns. They pointed out that the paper does not provide a clear explanation of how the results can be used to improve RLHF. They also pointed out that the paper does not provide a clear explanation of how the results can be used to improve the design of reward models. Finally, they pointed out that the paper does not provide a clear explanation of how the results can be used to improve the design of RL algorithms.

I encourage the authors to take the reviewers' comments into consideration and resubmit to a future venue.

Best regards,
ICLR Chair

**********

## Paper Decision Policy

See [this page](https://iclr.cc/Conferences/2024/CallForPapers/policy) for the ICLR 2024 paper decision policy.

**********

**********

# Paper Decision

Reject (not selected for a spotlight/oral/poster)

**********

## Paper Decision Summary

The reviewers all agree that this paper studies an important problem in RLHF, namely reward model overoptimization. The authors use a synthetic setup to study the relationship between the gold reward model score and the KL divergence between the initial and optimized policies. The authors find that this relationship follows a different functional form depending on the method of optimization, and that the coefficients of this relationship scale smoothly with the number of reward model parameters. The authors also study the effect on this relationship of the size of the reward model dataset, the number of reward model and policy parameters, and the coefficient of the KL penalty added to the reward in the reinforcement learning setup.

However, the reviewers also raised several concerns. They pointed out that the paper does not provide a clear explanation of how the results can be used to improve RLHF. They also pointed out that the paper does not provide a clear explanation of how the results can be used to improve the design of reward models. Finally, they pointed out that the paper does not provide a clear explanation of how the results can be used to improve the design of RL algorithms.

**********

## Paper Decision Public Feedback

Dear authors,

Thank