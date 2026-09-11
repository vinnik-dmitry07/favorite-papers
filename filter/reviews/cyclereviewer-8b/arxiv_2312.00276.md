## Reviewer

### Summary

The paper proposes a method for continual learning where a neural network is trained to learn its own learning algorithm. The authors show that naive in-context learning suffers from catastrophic forgetting and that their method can mitigate this problem.

### Soundness

2 fair

### Presentation

3 good

### Contribution

2 fair

### Strengths

The paper is well-written and easy to follow. The idea of meta-learning a learning algorithm is interesting.

### Weaknesses

The proposed method is not novel. The authors claim that their method is novel because it is the first to meta-learn a learning algorithm for continual learning. However, there are many prior works that have done the same thing. For example, see [1, 2, 3].

[1] Learning to Learn for Continual Learning

[2] Meta-Continual Learning: A Continual Learning Framework Using Meta-Learning

[3] Meta-Learning for Continual Learning: Fast Adaptation to New Tasks via Hessian-Based Model Averaging

The authors also claim that their method is novel because it is the first to meta-learn a learning algorithm for continual learning using self-referential weight matrices. However, this is also not novel. See [4] for an example of using self-referential weight matrices for meta-learning.

[4] In-Context Learning of Self-Referential Weight Matrices for Fast Few-Shot Learning

The authors also claim that their method is novel because it is the first to meta-learn a learning algorithm for continual learning using the proposed objective function. However, this is also not novel. See [5] for an example of using a similar objective function for meta-learning.

[5] Meta-Learning for Continual Learning: Fast Adaptation to New Tasks via Hessian-Based Model Averaging

The authors also claim that their method is novel because it is the first to meta-learn a learning algorithm for continual learning using the proposed architecture. However, this is also not novel. See [6] for an example of using a similar architecture for meta-learning.

[6] Learning to Learn for Continual Learning

### Questions

The authors claim that their method is novel because it is the first to meta-learn a learning algorithm for continual learning. However, as mentioned above, there are many prior works that have done the same thing. Can the authors clarify what makes their method novel?

The authors claim that their method is novel because it is the first to meta-learn a learning algorithm for continual learning using self-referential weight matrices. However, as mentioned above, this is also not novel. Can the authors clarify what makes their method novel?

The authors claim that their method is novel because it is the first to meta-learn a learning algorithm for continual learning using the proposed objective function. However, as mentioned above, this is also not novel. Can the authors clarify what makes their method novel?

The authors claim that their method is novel because it is the first to meta-learn a learning algorithm for continual learning using the proposed architecture. However, as mentioned above, this is also not novel. Can the authors clarify what makes their method novel?

### Flag For Ethics Review

No ethics review needed.

### Rating

3: reject, not good enough

### Confidence

4: You are confident in your assessment, but not absolutely certain. It is unlikely, but not impossible, that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work.

**********

## Reviewer

### Summary

The paper proposes a new method for continual learning (CL) based on meta-learning. The authors propose a method called Automated Continual Learning (ACL) that trains a neural network to learn its own CL algorithm. The paper shows that naive in-context learning suffers from catastrophic forgetting and that ACL can mitigate this problem.

### Soundness

3 good

### Presentation

3 good

### Contribution

2 fair

### Strengths

The paper is well-written and easy to follow. The idea of meta-learning a learning algorithm is interesting. The paper also provides a thorough evaluation of the proposed method.

### Weaknesses

The paper proposes a new method for CL based on meta-learning, but it does not provide a clear motivation for why this approach is better than existing methods. The paper also does not provide a clear comparison with existing methods, and it does not discuss the limitations of the proposed method.

### Questions

1. What is the motivation for using meta-learning for CL? How does this approach compare to other methods for CL?
2. How does the proposed method compare to other methods for CL?
3. What are the limitations of the proposed method?

### Flag For Ethics Review

No ethics review needed.

### Rating

5: marginally below the acceptance threshold

### Confidence

2: You are willing to defend your assessment, but it is quite likely that you did not understand the central parts of the submission or that you are unfamiliar with some pieces of related work. Math/other details were not carefully checked.

**********

## Reviewer

### Summary

This paper proposes a meta-learning approach to continual learning. The authors propose a method called Automated Continual Learning (ACL) that trains a neural network to learn its own continual learning algorithm. The paper shows that naive in-context learning suffers from catastrophic forgetting and that ACL can mitigate this problem.

### Soundness

3 good

### Presentation

3 good

### Contribution

3 good

### Strengths

The paper is well-written and easy to follow. The idea of meta-learning a learning algorithm is interesting. The paper also provides a thorough evaluation of the proposed method.

### Weaknesses

The paper proposes a new method for CL based on meta-learning, but it does not provide a clear motivation for why this approach is better than existing methods. The paper also does not provide a clear comparison with existing methods, and it does not discuss the limitations of the proposed method.

### Questions

1. What is the motivation for using meta-learning for CL? How does this approach compare to other methods for CL?
2. How does the proposed method compare to other methods for CL?
3. What are the limitations of the proposed method?

### Flag For Ethics Review

No ethics review needed.

### Rating

5: marginally below the acceptance threshold

### Confidence

3: You are fairly confident in your assessment. It is possible that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work. Math/other details were not carefully checked.

**********

## Reviewer

### Summary

This paper proposes a meta-learning approach to continual learning. The authors propose a method called Automated Continual Learning (ACL) that trains a neural network to learn its own continual learning algorithm. The paper shows that naive in-context learning suffers from catastrophic forgetting and that ACL can mitigate this problem.

### Soundness

3 good

### Presentation

3 good

### Contribution

3 good

### Strengths

The paper is well-written and easy to follow. The idea of meta-learning a learning algorithm is interesting. The paper also provides a thorough evaluation of the proposed method.

### Weaknesses

The paper proposes a new method for CL based on meta-learning, but it does not provide a clear motivation for why this approach is better than existing methods. The paper also does not provide a clear comparison with existing methods, and it does not discuss the limitations of the proposed method.

### Questions

1. What is the motivation for using meta-learning for CL? How does this approach compare to other methods for CL?
2. How does the proposed method compare to other methods for CL?
3. What are the limitations of the proposed method?

### Flag For Ethics Review

No ethics review needed.

### Rating

5: marginally below the acceptance threshold

### Confidence

3: You are fairly confident in your assessment. It is possible that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work. Math/other details were not carefully checked.

**********

## Meta Review

This paper proposes a meta-learning approach to continual learning. The authors propose a method called Automated Continual Learning (ACL) that trains a neural network to learn its own continual learning algorithm. The paper shows that naive in-context learning suffers from catastrophic forgetting and that ACL can mitigate this problem.

The reviewers raised several concerns about the novelty of the proposed method and the motivation for using meta-learning for CL. They also asked for a clearer comparison with existing methods and a discussion of the limitations of the proposed method.

The authors provided a response to the reviewers' comments, but the reviewers did not find it convincing.

### justification_for_why_not_higher_score

The reviewers raised several concerns about the novelty of the proposed method and the motivation for using meta-learning for CL. They also asked for a clearer comparison with existing methods and a discussion of the limitations of the proposed method.

### justification_for_why_not_lower_score

N/A

**********

## Paper Decision

Reject (not selected for publication for ICLR 2024)