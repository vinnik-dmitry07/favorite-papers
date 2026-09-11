## Reviewer

### Summary

This paper proposes a new sampling method for LLMs to improve their reasoning capabilities. The proposed method is based on the idea of sampling from the power distribution, which is a sharpened version of the base model distribution. The paper shows that this method can achieve comparable or even better performance than RL-based methods on various reasoning tasks.

### Soundness

3 good

### Presentation

3 good

### Contribution

3 good

### Strengths

1. The paper is well-written and easy to follow.
2. The proposed method is simple and easy to understand.
3. The experimental results are promising, showing that the proposed method can achieve comparable or even better performance than RL-based methods.

### Weaknesses

1. The paper claims that the proposed method is training-free, but it requires additional inference-time computation. The paper should discuss the trade-off between training time and inference time.
2. The paper only compares the proposed method with GRPO, which is a specific RL-based method. It would be better to compare it with other RL-based methods as well.
3. The paper only evaluates the proposed method on a few reasoning tasks. It would be better to evaluate it on more tasks to show its generalizability.

### Questions

1. How does the proposed method compare with other RL-based methods in terms of training time and inference time?
2. How does the proposed method perform on more reasoning tasks?

### Flag For Ethics Review

No ethics review needed.

### Rating

5: marginally below the acceptance threshold

### Confidence

2: You are willing to defend your assessment, but it is quite likely that you did not understand the central parts of the submission or that you are unfamiliar with some pieces of related work. Math/other details were not carefully checked.

**********

## Reviewer

### Summary

This paper proposes a sampling algorithm for base models that leverages additional compute at inference time, achieving single-shot performance that nearly matches RL-posttraining on in-domain reasoning tasks and can even outperform on out-of-domain reasoning tasks. The algorithm is training-free, dataset-free, and verifier-free, avoiding some of the inherent weaknesses of RL methods. The paper introduces the power distribution as a useful sampling target for reasoning tasks and proposes an approximate sampling algorithm using a Markov chain Monte Carlo (MCMC) algorithm that iteratively resamples token subsequences according to their base model likelihoods. The paper also empirically demonstrates the effectiveness of the algorithm over a range of models and reasoning tasks.

### Soundness

3 good

### Presentation

3 good

### Contribution

3 good

### Strengths

- The paper is well-written and easy to follow.
- The proposed method is simple and easy to understand.
- The experimental results are promising, showing that the proposed method can achieve comparable or even better performance than RL-based methods.

### Weaknesses

- The paper only compares the proposed method with GRPO, which is a specific RL-based method. It would be better to compare it with other RL-based methods as well.
- The paper only evaluates the proposed method on a few reasoning tasks. It would be better to evaluate it on more tasks to show its generalizability.

### Questions

- How does the proposed method compare with other RL-based methods in terms of training time and inference time?
- How does the proposed method perform on more reasoning tasks?
- Can the proposed method be applied to other types of models, such as diffusion models?

### Flag For Ethics Review

No ethics review needed.

### Rating

6: marginally above the acceptance threshold

### Confidence

3: You are fairly confident in your assessment. It is possible that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work. Math/other details were not carefully checked.

**********

## Reviewer

### Summary

This paper proposes a sampling algorithm for base models that leverages additional compute at inference time, achieving single-shot performance that nearly matches RL-posttraining on in-domain reasoning tasks and can even outperform on out-of-domain reasoning tasks. The algorithm is training-free, dataset-free, and verifier-free, avoiding some of the inherent weaknesses of RL methods. The paper introduces the power distribution as a useful sampling target for reasoning tasks and proposes an approximate sampling algorithm using a Markov chain Monte Carlo (MCMC) algorithm that iteratively resamples token subsequences according to their base model likelihoods. The paper also empirically demonstrates the effectiveness of the algorithm over a range of models and reasoning tasks.

### Soundness

3 good

### Presentation

3 good

### Contribution

3 good

### Strengths

- The paper is well-written and easy to follow.
- The proposed method is simple and easy to understand.
- The experimental results are promising, showing that the proposed method can achieve comparable or even better performance than RL-based methods.

### Weaknesses

- The paper only compares the proposed method with GRPO, which is a specific RL-based method. It would be better to compare it with other RL-based methods as well.
- The paper only evaluates the proposed method on a few reasoning tasks. It would be better to evaluate it on more tasks to show its generalizability.

### Questions

- How does the proposed method compare with other RL-based methods in terms of training time and inference time?
- How does the proposed method perform on more reasoning tasks?
- Can the proposed method be applied to other types of models, such as diffusion models?

### Flag For Ethics Review

No ethics review needed.

### Rating

6: marginally above the acceptance threshold

### Confidence

3: You are fairly confident in your assessment. It is possible that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work. Math/other details were not carefully checked.

**********

## Reviewer

### Summary

The paper presents a novel sampling algorithm for base models that leverages additional compute at inference time, achieving single-shot performance that nearly matches RL-posttraining on in-domain reasoning tasks and can even outperform on out-of-domain reasoning tasks. The algorithm is training-free, dataset-free, and verifier-free, avoiding some of the inherent weaknesses of RL methods. The paper introduces the power distribution as a useful sampling target for reasoning tasks and proposes an approximate sampling algorithm using a Markov chain Monte Carlo (MCMC) algorithm that iteratively resamples token subsequences according to their base model likelihoods. The paper also empirically demonstrates the effectiveness of the algorithm over a range of models and reasoning tasks.

### Soundness

3 good

### Presentation

3 good

### Contribution

3 good

### Strengths

- The paper is well-written and easy to follow.
- The proposed method is simple and easy to understand.
- The experimental results are promising, showing that the proposed method can achieve comparable or even better performance than RL-based methods.

### Weaknesses

- The paper only compares the proposed method with GRPO, which is a specific RL-based method. It would be better to compare it with other RL-based methods as well.
- The paper only evaluates the proposed method on a few reasoning tasks. It would be better to evaluate it on more tasks to show its generalizability.

### Questions

- How does the proposed method compare with other RL-based methods in terms of training time and inference time?
- How does the proposed method perform on more reasoning tasks?
- Can the proposed method be applied to other types of models, such as diffusion models?

### Flag For Ethics Review

No ethics review needed.

### Rating

6: marginally above the acceptance threshold

### Confidence

3: You are fairly confident in your assessment. It is possible that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work. Math/other details were not carefully checked.

**********

## Meta Review

This paper proposes a sampling algorithm for base models that leverages additional compute at inference time, achieving single-shot performance that nearly matches RL-posttraining on in-domain reasoning tasks and can even outperform on out-of-domain reasoning tasks. The algorithm is training-free, dataset-free, and verifier-free, avoiding some of the inherent weaknesses of RL methods. The paper introduces the power distribution as a useful sampling target for reasoning tasks and proposes an approximate sampling algorithm using a Markov chain Monte Carlo (MCMC) algorithm that iteratively resamples token subsequences according to their base model likelihoods. The paper also empirically demonstrates the effectiveness of the algorithm over a range of models and reasoning tasks.

The paper received mixed reviews. Some reviewers found the paper interesting and the proposed method promising, while others found it lacking in terms of experimental evaluation. The authors provided additional experimental results to address some of the concerns raised by the reviewers, but it seems that there is still a need for further evaluation and analysis of the proposed method. I encourage the authors to take the feedback from the reviewers into account and consider revising the paper accordingly.

### justification_for_why_not_higher_score

The paper received mixed reviews, and there are concerns about the experimental evaluation.

### justification_for_why_not_lower_score

N/A

**********

## Paper Decision

Reject (out of the running for an oral, but can be accepted as a poster)