## Reviewer

### Summary

This paper proposes a method to improve RLVR training by breaking down the problem into subproblems. The method is motivated by the observation that RLVR training can be ineffective on hard problems because the reward signal becomes extremely sparse. The paper proposes to break down the problem into subproblems, and then train the model to solve each subproblem. The subproblems are constructed using an external LLM, and the model is trained using a curriculum learning approach. The paper also proposes a method to normalize the rewards at each subproblem position, and to assign the resulting advantages to the corresponding answer spans. The paper provides a theoretical analysis of the method, and evaluates it on seven mathematical reasoning benchmarks.

### Soundness

3 good

### Presentation

3 good

### Contribution

3 good

### Strengths

The paper is well-written and easy to follow. The method is clearly explained and motivated. The theoretical analysis is sound and provides some interesting insights. The empirical results are promising, showing consistent gains over strong RLVR and curriculum-learning baselines.

### Weaknesses

I am not an expert in this area, but I am not sure if the method is novel enough. It seems that the method is a combination of existing ideas, such as curriculum learning and subproblem decomposition. The paper does not provide a clear comparison with other methods, and it is not clear how the proposed method compares to other methods in terms of novelty and effectiveness.

### Questions

- How does the proposed method compare to other methods in terms of novelty and effectiveness?
- How does the method perform on other types of reasoning tasks, such as programming tasks?
- How does the method perform on other types of LLMs, such as GPT-3.5-turbo?

### Flag For Ethics Review

No ethics review needed.

### Rating

6: marginally above the acceptance threshold

### Confidence

2: You are willing to defend your assessment, but it is quite likely that you did not understand the central parts of the submission or that you are unfamiliar with some pieces of related work. Math/other details were not carefully checked.

**********

## Reviewer

### Summary

This paper proposes a new curriculum learning method for RLVR, where the hard problem is broken into a sequence of subproblems of increasing difficulty. The model is trained to solve all subproblems in a single rollout. The reward is normalized at each subproblem position and assigned to the corresponding answer spans. The authors provide theoretical analysis and empirical results on 7 mathematical reasoning benchmarks.

### Soundness

3 good

### Presentation

3 good

### Contribution

3 good

### Strengths

1. The paper is well-written and easy to follow.
2. The proposed method is simple yet effective, and the empirical results are promising.
3. The theoretical analysis is sound and provides some interesting insights.

### Weaknesses

1. The paper does not provide a clear comparison with other methods in terms of novelty and effectiveness.
2. The paper does not provide a clear explanation of how the subproblems are constructed and how the rewards are assigned to each subproblem.

### Questions

1. How does the proposed method compare to other methods in terms of novelty and effectiveness?
2. How are the subproblems constructed and how are the rewards assigned to each subproblem?
3. How does the method perform on other types of reasoning tasks, such as programming tasks?

### Flag For Ethics Review

No ethics review needed.

### Rating

6: marginally above the acceptance threshold

### Confidence

3: You are fairly confident in your assessment. It is possible that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work. Math/other details were not carefully checked.

**********

## Reviewer

### Summary

The paper proposes a new curriculum learning method for RLVR, where the hard problem is broken into a sequence of subproblems of increasing difficulty. The model is trained to solve all subproblems in a single rollout. The reward is normalized at each subproblem position and assigned to the corresponding answer spans. The authors provide theoretical analysis and empirical results on 7 mathematical reasoning benchmarks.

### Soundness

3 good

### Presentation

3 good

### Contribution

3 good

### Strengths

1. The paper is well-written and easy to follow.
2. The proposed method is simple yet effective, and the empirical results are promising.
3. The theoretical analysis is sound and provides some interesting insights.

### Weaknesses

1. The paper does not provide a clear comparison with other methods in terms of novelty and effectiveness.
2. The paper does not provide a clear explanation of how the subproblems are constructed and how the rewards are assigned to each subproblem.

### Questions

1. How does the proposed method compare to other methods in terms of novelty and effectiveness?
2. How are the subproblems constructed and how are the rewards assigned to each subproblem?
3. How does the method perform on other types of reasoning tasks, such as programming tasks?

### Flag For Ethics Review

No ethics review needed.

### Rating

6: marginally above the acceptance threshold

### Confidence

3: You are fairly confident in your assessment. It is possible that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work. Math/other details were not carefully checked.

**********

## Reviewer

### Summary

This paper proposes a method to break down hard problems into a sequence of subproblems and train the model to solve all subproblems in a single rollout. The proposed method is evaluated on seven mathematical reasoning benchmarks, and the results show that the proposed method outperforms several strong baselines.

### Soundness

3 good

### Presentation

3 good

### Contribution

3 good

### Strengths

- The proposed method is simple yet effective, and the empirical results are promising.
- The theoretical analysis is sound and provides some interesting insights.

### Weaknesses

- The paper does not provide a clear comparison with other methods in terms of novelty and effectiveness.
- The paper does not provide a clear explanation of how the subproblems are constructed and how the rewards are assigned to each subproblem.

### Questions

- How does the proposed method compare to other methods in terms of novelty and effectiveness?
- How are the subproblems constructed and how are the rewards assigned to each subproblem?
- How does the method perform on other types of reasoning tasks, such as programming tasks?

### Flag For Ethics Review

No ethics review needed.

### Rating

6: marginally above the acceptance threshold

### Confidence

3: You are fairly confident in your assessment. It is possible that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work. Math/other details were not carefully checked.

**********

## Meta Review

This paper proposes a new curriculum learning method for RLVR, where the hard problem is broken into a sequence of subproblems of increasing difficulty. The model is trained to solve all subproblems in a single rollout. The reward is normalized at each subproblem position and assigned to the corresponding answer spans. The authors provide theoretical analysis and empirical results on 7 mathematical reasoning benchmarks.

The reviewers appreciate the simplicity of the proposed method and the promising empirical results. The theoretical analysis is also appreciated. The main concerns are about the novelty and the clarity of the paper. The authors provided detailed responses to the reviewers' questions and concerns. The authors also provided more details about the subproblem construction and the reward assignment in the appendix. The reviewers are generally positive about the paper and recommend acceptance. The AC agrees with the reviewers that the paper is a good submission to ICML.

### justification_for_why_not_higher_score

The paper is a good submission to ICML, but it is not a breakthrough paper.

### justification_for_why_not_lower_score

The reviewers are generally positive about the paper and recommend acceptance.

**********

## Paper Decision

Accept (poster)