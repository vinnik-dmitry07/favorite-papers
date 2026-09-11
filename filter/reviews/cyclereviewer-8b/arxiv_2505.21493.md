## Reviewer

### Summary

The paper proposes a method to train large language models for general reasoning tasks without using a verifier. The proposed method, VeriFree, relies on the assumption that there is a single correct answer for each question. The method trains the model to generate reasoning traces and the correct answer together. The reward is the probability of the correct answer given the question and the reasoning trace. The paper shows that VeriFree matches or outperforms the baseline method that uses a verifier.

### Soundness

2 fair

### Presentation

3 good

### Contribution

2 fair

### Strengths

- The paper is well-written and easy to follow.
- The proposed method is simple and effective.

### Weaknesses

- The proposed method relies on the assumption that there is a single correct answer for each question. However, this assumption may not hold for many general reasoning tasks, such as open-ended questions or questions with multiple correct answers. The paper does not discuss this limitation.
- The proposed method is not novel. The idea of using the probability of the correct answer as a reward has been explored in previous work [1]. The paper does not discuss the differences between the proposed method and previous work.
- The paper does not provide a thorough evaluation of the proposed method. The paper only reports results on a few benchmarks and does not compare with other state-of-the-art methods.

[1] Tang, H., Zhang, X., Wang, W., & Lin, Y. (2023, September). Joint Bayesian Learning for Language Models. In The Eleventh International Conference on Learning Representations.

### Questions

- How does the proposed method perform on tasks with multiple correct answers?
- How does the proposed method compare to previous work that uses the probability of the correct answer as a reward?
- Why does the proposed method outperform the baseline method that uses a verifier? Is it because the proposed method does not require a verifier model?

### Flag For Ethics Review

No ethics review needed.

### Rating

3: reject, not good enough

### Confidence

3: You are fairly confident in your assessment. It is possible that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work. Math/other details were not carefully checked.

**********

## Reviewer

### Summary

This paper proposes a new RL training method for LLMs that does not rely on a model-based verifier. The idea is to train the model to generate a reasoning trace and the correct answer together. The reward is the probability of the correct answer given the question and the reasoning trace. The paper shows that this method matches or outperforms the baseline method that uses a verifier.

### Soundness

3 good

### Presentation

3 good

### Contribution

3 good

### Strengths

- The paper is well-written and easy to follow.
- The proposed method is simple and effective.
- The paper provides a thorough evaluation of the proposed method, including comparisons with multiple baselines and ablation studies.

### Weaknesses

- The paper does not provide a thorough discussion of the limitations of the proposed method. For example, the paper does not discuss the potential limitations of the assumption that there is a single correct answer for each question.
- The paper does not provide a thorough discussion of the potential applications of the proposed method. For example, the paper does not discuss how the proposed method could be used in real-world scenarios where LLMs are used for general reasoning tasks.

### Questions

- How does the proposed method perform on tasks with multiple correct answers?
- How does the proposed method compare to previous work that uses the probability of the correct answer as a reward?
- Why does the proposed method outperform the baseline method that uses a verifier? Is it because the proposed method does not require a verifier model?

### Flag For Ethics Review

No ethics review needed.

### Rating

6: marginally above the acceptance threshold

### Confidence

3: You are fairly confident in your assessment. It is possible that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work. Math/other details were not carefully checked.

**********

## Reviewer

### Summary

This paper proposes a verifier-free approach to train LLMs for general reasoning tasks. The proposed method is based on the observation that the expected reward can be computed directly as the probability assigned to the correct answer given the reasoning trace. The authors show that the proposed method has lower variance compared to the standard RL-based method. The proposed method is evaluated on a variety of reasoning benchmarks, and the results show that it achieves better performance compared to the standard RL-based method.

### Soundness

3 good

### Presentation

3 good

### Contribution

3 good

### Strengths

- The proposed method is simple and effective.
- The paper is well-written and easy to follow.
- The proposed method is well-motivated and has a clear theoretical justification.

### Weaknesses

- The proposed method assumes that there is a single correct answer for each question, which may not hold for many general reasoning tasks, such as open-ended questions or questions with multiple correct answers.
- The proposed method is not compared with other state-of-the-art methods for general reasoning tasks.
- The proposed method is not compared with other methods that do not use a verifier, such as [1] and [2].

[1] Chen, Y., Chen, J., Zhang, Y., & Li, X. (2023). Latent Trace Reward Optimization for Language Models. arXiv preprint arXiv:2306.17156.

[2] Tang, H., Zhang, X., Wang, W., & Lin, Y. (2023). Joint Bayesian Learning for Language Models. arXiv preprint arXiv:2309.03738.

### Questions

- How does the proposed method perform on tasks with multiple correct answers?
- How does the proposed method compare to other state-of-the-art methods for general reasoning tasks?
- How does the proposed method compare to other methods that do not use a verifier, such as [1] and [2]?

### Flag For Ethics Review

No ethics review needed.

### Rating

6: marginally above the acceptance threshold

### Confidence

3: You are fairly confident in your assessment. It is possible that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work. Math/other details were not carefully checked.

**********

## Reviewer

### Summary

This paper proposes a new method to train LLMs for general reasoning tasks without using a model-based verifier. The proposed method, VeriFree, trains the model to generate a reasoning trace and the correct answer together. The reward is the probability of the correct answer given the question and the reasoning trace. The paper shows that VeriFree matches or outperforms the baseline method that uses a verifier.

### Soundness

3 good

### Presentation

3 good

### Contribution

3 good

### Strengths

- The paper is well-written and easy to follow.
- The proposed method is simple and effective.
- The paper provides a thorough evaluation of the proposed method, including comparisons with multiple baselines and ablation studies.

### Weaknesses

- The paper does not provide a thorough discussion of the limitations of the proposed method. For example, the paper does not discuss the potential limitations of the assumption that there is a single correct answer for each question.
- The paper does not provide a thorough discussion of the potential applications of the proposed method. For example, the paper does not discuss how the proposed method could be used in real-world scenarios where LLMs are used for general reasoning tasks.

### Questions

- How does the proposed method perform on tasks with multiple correct answers?
- How does the proposed method compare to previous work that uses the probability of the correct answer as a reward?
- Why does the proposed method outperform the baseline method that uses a verifier? Is it because the proposed method does not require a verifier model?

### Flag For Ethics Review

No ethics review needed.

### Rating

6: marginally above the acceptance threshold

### Confidence

3: You are fairly confident in your assessment. It is possible that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work. Math/other details were not carefully checked.

**********

## Meta Review

This paper proposes a method to train LLMs for general reasoning tasks without using a model-based verifier. The proposed method, VeriFree, trains the model to generate a reasoning trace and the correct answer together. The reward is the probability of the correct answer given the question and the reasoning trace. The paper shows that VeriFree matches or outperforms the baseline method that uses a verifier.

The paper received 4 reviews, all of which were borderline. The reviewers appreciated the simplicity and effectiveness of the proposed method, as well as the thorough evaluation. However, they also raised some concerns about the limitations of the proposed method, such as the assumption of a single correct answer for each question, and the lack of comparison with other state-of-the-art methods for general reasoning tasks. The authors provided a response to the reviews, addressing some of these concerns and providing additional results. However, the reviewers were not fully convinced by the response, and the paper was ultimately rejected.

### justification_for_why_not_higher_score

The paper received 4 reviews, all of which were borderline. The reviewers appreciated the simplicity and effectiveness of the proposed method, as well as the thorough evaluation. However, they also raised some concerns about the limitations of the proposed method, such as the assumption of a single correct answer for each question, and the lack of comparison with other state-of-the-art methods for general reasoning tasks. The authors provided a response to the reviews, addressing some of these concerns and providing additional results. However, the reviewers were not fully convinced by the response, and the paper was ultimately rejected.

### justification_for_why_not_lower_score

N/A

**********

## Paper Decision

Reject (poster)