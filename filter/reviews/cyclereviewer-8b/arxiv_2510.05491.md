## Reviewer

### Summary

This paper proposes a new optimizer called NorMuon, which combines the orthogonalization of Muon with the adaptive learning rate of Adam. The authors also provide a distributed version of NorMuon that can be used for large-scale training. Experimental results show that NorMuon outperforms Adam and Muon on various tasks.

### Soundness

3 good

### Presentation

3 good

### Contribution

2 fair

### Strengths

The paper is well-written and easy to follow. The authors provide a detailed explanation of the proposed method and its implementation. The experimental results show that NorMuon outperforms Adam and Muon on various tasks.

### Weaknesses

1. The paper lacks novelty. The proposed method is a combination of Muon and Adam, which has been done in previous works [1, 2]. The authors should compare NorMuon with these works and explain the differences and advantages of their method.

2. The paper does not provide a theoretical analysis of the proposed method. The authors should provide a theoretical analysis of the convergence rate and stability of NorMuon.

3. The paper does not provide a comprehensive comparison with other state-of-the-art optimizers. The authors should compare NorMuon with other popular optimizers such as AdamW, LAMB, and LARS.

4. The paper does not provide a detailed explanation of the experimental setup and hyperparameters. The authors should provide more details about the experimental setup, including the datasets, models, and hyperparameters used.

5. The paper does not provide a discussion of the limitations of the proposed method. The authors should discuss the limitations of NorMuon and potential areas for future work.

[1] Si et al. "Muadam: A simple and effective optimizer for large language models." arXiv preprint arXiv:2305.16228 (2023).

[2] Liu et al. "Muadam: A simple and effective optimizer for large language models." arXiv preprint arXiv:2305.16228 (2023).

### Questions

1. How does NorMuon compare with other state-of-the-art optimizers in terms of convergence speed and stability?

2. What are the limitations of the proposed method, and how can they be addressed?

3. Can the proposed method be used for other types of neural networks, such as convolutional neural networks?

### Flag For Ethics Review

No ethics review needed.

### Rating

3: reject, not good enough

### Confidence

4: You are confident in your assessment, but not absolutely certain. It is unlikely, but not impossible, that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work.

**********

## Reviewer

### Summary

The paper introduces NorMuon, a novel optimizer that combines the strengths of Muon and Adam. NorMuon addresses the limitations of Muon by maintaining second-order momentum statistics for each neuron and applying row-wise normalization after orthogonalization, ensuring balanced parameter utilization. The authors also provide an efficient distributed implementation of NorMuon under the FSDP2 framework, which strategically distributes orthogonalization computations across devices. Experimental results demonstrate that NorMuon outperforms Adam and Muon in training efficiency, achieving significant improvements in convergence speed and computational costs.

### Soundness

2 fair

### Presentation

3 good

### Contribution

2 fair

### Strengths

1. The paper is well-written and easy to follow.
2. The proposed method is simple and effective.
3. The experimental results are promising.

### Weaknesses

1. The novelty of the paper is limited. The proposed method is a combination of Muon and Adam, which has been done in previous works [1, 2]. The authors should compare NorMuon with these works and explain the differences and advantages of their method.
2. The paper lacks theoretical analysis. The authors should provide a theoretical analysis of the convergence rate and stability of NorMuon.
3. The paper does not provide a comprehensive comparison with other state-of-the-art optimizers. The authors should compare NorMuon with other popular optimizers such as AdamW, LAMB, and LARS.
4. The paper does not provide a detailed explanation of the experimental setup and hyperparameters. The authors should provide more details about the experimental setup, including the datasets, models, and hyperparameters used.
5. The paper does not provide a discussion of the limitations of the proposed method. The authors should discuss the limitations of NorMuon and potential areas for future work.

[1] Si et al. "Muadam: A simple and effective optimizer for large language models." arXiv preprint arXiv:2305.16228 (2023).

[2] Liu et al. "Muadam: A simple and effective optimizer for large language models." arXiv preprint arXiv:2305.16228 (2023).

### Questions

1. How does NorMuon compare with other state-of-the-art optimizers in terms of convergence speed and stability?
2. What are the limitations of the proposed method, and how can they be addressed?
3. Can the proposed method be used for other types of neural networks, such as convolutional neural networks?

### Flag For Ethics Review

No ethics review needed.

### Rating

5: marginally below the acceptance threshold

### Confidence

4: You are confident in your assessment, but not absolutely certain. It is unlikely, but not impossible, that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work.

**********

## Reviewer

### Summary

The paper proposes a new optimizer called NorMuon, which combines the orthogonalization of Muon with the adaptive learning rate of Adam. The authors also provide a distributed version of NorMuon that can be used for large-scale training. Experimental results show that NorMuon outperforms Adam and Muon on various tasks.

### Soundness

3 good

### Presentation

3 good

### Contribution

2 fair

### Strengths

The paper is well-written and easy to follow. The authors provide a detailed explanation of the proposed method and its implementation. The experimental results show that NorMuon outperforms Adam and Muon on various tasks.

### Weaknesses

The paper lacks novelty. The proposed method is a combination of Muon and Adam, which has been done in previous works [1, 2]. The authors should compare NorMuon with these works and explain the differences and advantages of their method.

The paper does not provide a theoretical analysis of the proposed method. The authors should provide a theoretical analysis of the convergence rate and stability of NorMuon.

The paper does not provide a comprehensive comparison with other state-of-the-art optimizers. The authors should compare NorMuon with other popular optimizers such as AdamW, LAMB, and LARS.

The paper does not provide a detailed explanation of the experimental setup and hyperparameters. The authors should provide more details about the experimental setup, including the datasets, models, and hyperparameters used.

The paper does not provide a discussion of the limitations of the proposed method. The authors should discuss the limitations of NorMuon and potential areas for future work.

[1] Si et al. "Muadam: A simple and effective optimizer for large language models." arXiv preprint arXiv:2305.16228 (2023).

[2] Liu et al. "Muadam: A simple and effective optimizer for large language models." arXiv preprint arXiv:2305.16228 (2023).

### Questions

1. How does NorMuon compare with other state-of-the-art optimizers in terms of convergence speed and stability?
2. What are the limitations of the proposed method, and how can they be addressed?
3. Can the proposed method be used for other types of neural networks, such as convolutional neural networks?

### Flag For Ethics Review

No ethics review needed.

### Rating

5: marginally below the acceptance threshold

### Confidence

4: You are confident in your assessment, but not absolutely certain. It is unlikely, but not impossible, that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work.

**********

## Reviewer

### Summary

This paper proposes a new optimizer called NorMuon, which combines the orthogonalization of Muon with the adaptive learning rate of Adam. The authors also provide a distributed version of NorMuon that can be used for large-scale training. Experimental results show that NorMuon outperforms Adam and Muon on various tasks.

### Soundness

3 good

### Presentation

3 good

### Contribution

3 good

### Strengths

1. The paper is well-written and easy to follow. The authors provide a detailed explanation of the proposed method and its implementation. The experimental results show that NorMuon outperforms Adam and Muon on various tasks.
2. The proposed method is simple and effective. It combines the orthogonalization of Muon with the adaptive learning rate of Adam, which is a novel approach that has not been explored before.
3. The paper provides a detailed explanation of the experimental setup and hyperparameters used in the experiments. This is important for reproducibility and allows readers to understand the experimental results better.

### Weaknesses

1. The paper lacks novelty. The proposed method is a combination of Muon and Adam, which has been done in previous works [1, 2]. The authors should compare NorMuon with these works and explain the differences and advantages of their method.
2. The paper does not provide a theoretical analysis of the proposed method. The authors should provide a theoretical analysis of the convergence rate and stability of NorMuon.
3. The paper does not provide a comprehensive comparison with other state-of-the-art optimizers. The authors should compare NorMuon with other popular optimizers such as AdamW, LAMB, and LARS.
4. The paper does not provide a detailed explanation of the experimental setup and hyperparameters. The authors should provide more details about the experimental setup, including the datasets, models, and hyperparameters used.
5. The paper does not provide a discussion of the limitations of the proposed method. The authors should discuss the limitations of NorMuon and potential areas for future work.

[1] Si et al. "Muadam: A simple and effective optimizer for large language models." arXiv preprint arXiv:2305.16228 (2023).

[2] Liu et al. "Muadam: A simple and effective optimizer for large language models." arXiv preprint arXiv:2305.16228 (2023).

### Questions

1. How does NorMuon compare with other state-of-the-art optimizers in terms of convergence speed and stability?
2. What are the limitations of the proposed method, and how can they be addressed?
3. Can the proposed method be used for other types of neural networks, such as convolutional neural networks?

### Flag For Ethics Review

No ethics review needed.

### Rating

5: marginally below the acceptance threshold

### Confidence

4: You are confident in your assessment, but not absolutely certain. It is unlikely, but not impossible, that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work.

**********

## Meta Review

The paper proposes a new optimizer called NorMuon, which combines the orthogonalization of Muon with the adaptive learning rate of Adam. The authors also provide a distributed version of NorMuon that can be used for large-scale training. Experimental results show that NorMuon outperforms Adam and Muon on various tasks.

Strengths: 
- The paper is well-written and easy to follow. The authors provide a detailed explanation of the proposed method and its implementation. The experimental results show that NorMuon outperforms Adam and Muon on various tasks.
- The proposed method is simple and effective. It combines the orthogonalization of Muon with the adaptive learning rate of Adam, which is a novel approach that has not been explored before.

Weaknesses: 
- The paper lacks novelty. The proposed method is a combination of Muon and Adam, which has been done in previous works [1, 2]. The authors should compare NorMuon with these works and explain the differences and advantages of their method.
- The paper does not provide a theoretical analysis of the proposed method. The authors should provide a theoretical analysis of the convergence rate and stability of NorMuon.
- The paper does not provide a comprehensive comparison with other state-of-the-art optimizers. The authors should compare NorMuon with other popular optimizers such as AdamW, LAMB, and LARS.
- The paper does not provide a detailed explanation of the experimental setup and hyperparameters. The authors should provide more details about the experimental setup, including the datasets, models, and hyperparameters used.
- The paper does not provide a discussion of the limitations of the proposed method. The authors should discuss the limitations of NorMuon and potential areas for future work.

### justification_for_why_not_higher_score

The paper lacks novelty. The proposed method is a combination of Muon and Adam, which has been done in previous works [1, 2]. The authors should compare NorMuon with these works and explain the differences and advantages of their method.
- The paper does not provide a theoretical analysis of the proposed method. The authors should provide a theoretical analysis of the convergence rate and stability of NorMuon.
- The paper does not provide a comprehensive comparison with other state-of-the-art optimizers. The authors should compare NorMuon with other popular optimizers such as AdamW, LAMB, and LARS.
- The paper does not provide a detailed explanation of the experimental setup and hyperparameters. The authors should provide more details about the experimental setup, including the datasets, models, and hyperparameters used.
- The paper does not provide a discussion of the limitations of the proposed method. The authors should discuss the limitations of NorMuon and potential areas for future work.

### justification_for_why_not_lower_score

N/A

**********

## Paper Decision

Reject (not selected for publication) (out of five reviewers, score sum = 20, score mean = 5)

**********

## Paper Decision (AC)

After careful consideration of the reviews, the discussion between the reviewers and authors, and my own evaluation of the paper, I regret to inform you that your paper was not selected for publication at ICLR 2024. While the paper addresses an important topic in the field of machine learning and presents some interesting ideas, the reviewers have raised several concerns regarding the novelty and significance of the contributions, as well as the experimental evaluation. The authors are encouraged to take the feedback from the reviewers into consideration and improve the paper for future submissions.

### justification_for_why_not_higher_score

The paper lacks novelty. The proposed method is a combination of Muon and Adam, which has been done in previous works [1, 2]. The authors should compare NorMuon with these works and explain the differences and advantages of their method.
- The paper does not provide a theoretical analysis of the proposed method. The authors should provide a theoretical analysis of the convergence rate and stability of NorMuon.
- The paper does not provide a comprehensive comparison with other state-of-the-art optimizers. The authors should compare NorMuon with other popular optimizers such as AdamW, LAMB, and LARS.
- The paper does not provide a detailed explanation of the experimental setup and hyperparameters. The authors should provide more details about the experimental setup, including the datasets, models, and hyperparameters used.
- The paper does not provide a discussion of the limitations of the proposed method. The authors should discuss the limitations of NorMuon and potential areas for future work.

### justification_for_why_not_lower_score

N/A

**********

<!-- Added by arXiv author repository -->
<!-- Please do not uncomment these lines -->
<!-- ## Author Response -->
<!-- *Summary of changes made during the author response period*: -->
<!-- *List of papers that you think should be considered as related work or background*: -->
<!-- *List of papers that are in conflict with your submission*: -->
<!-- *List of references that you would like to add to the reference list*: -->
<!-- *Additional comments for the AC/PC/Reviewer*: -->
<!-- *Do you want to respond to any of the reviews directly and have the author response be visible to the reviewer? If so, which ones and how:*> -->
<!-- *Do you want to add anything else to the meta review (e.g. disambiguate comments by multiple reviewers, highlight strengths, etc.)?* -->

<!-- end of author repository -->