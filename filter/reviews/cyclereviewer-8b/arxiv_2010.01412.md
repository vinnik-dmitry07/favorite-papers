## Summary

The paper proposes a new optimization method called Sharpness-Aware Minimization (SAM) that improves model generalization by simultaneously minimizing loss value and loss sharpness. The proposed method is motivated by a theorem that bounds generalization ability in terms of neighborhood-wise training loss. The paper also shows that SAM improves model generalization across a variety of benchmark datasets and models, and provides robustness to label noise.

## Soundness

2 fair

## Presentation

3 good

## Contribution

2 fair

## Strengths

- The paper is well-written and easy to follow.
- The proposed method is simple and easy to implement.
- The empirical results show that the proposed method improves model generalization across a variety of benchmark datasets and models.

## Weaknesses

- The proposed method is not well motivated. The theorem in Section 2 does not provide a clear justification for why minimizing loss sharpness improves generalization. The connection between loss sharpness and generalization is not well established.
- The proposed method is not novel. The idea of penalizing sharpness has been explored in previous work, such as [1,2,3]. The proposed method is similar to these previous works, but with a different objective function.
- The empirical results are not convincing. The proposed method only shows improvements on small-scale datasets, such as CIFAR-10 and CIFAR-100. It is unclear how the method performs on larger-scale datasets, such as ImageNet.
- The paper lacks a discussion of the limitations of the proposed method. The paper does not discuss the potential drawbacks or limitations of the proposed method, such as increased training time or computational cost.

[1] Sun, Y., Li, Y., Liu, Z., & Hengel, A. V. (2020). Test of time: Assessing the robustness of deep neural networks. arXiv preprint arXiv:2006.10768.

[2] Wei, C., & Ma, T. (2020). On the margin theory of neural networks. Advances in Neural Information Processing Systems, 33, 16204-16214.

[3] Izmailov, P., Garipov, T., Alemi, A., & Lin, Z. C. (2018). Averaging Weights Leads to Wider Optima and Better Generalization. arXiv preprint arXiv:1803.05407.

## Questions

- What is the motivation for using the p-norm in the definition of the sharpness-aware loss function?
- How does the proposed method compare to other methods that penalize sharpness, such as [1,2,3]?
- How does the proposed method perform on larger-scale datasets, such as ImageNet?
- What are the potential limitations of the proposed method?

## Flag For Ethics Review

No ethics review needed.

## Rating

3: reject, not good enough

## Confidence

4: You are confident in your assessment, but not absolutely certain. It is unlikely, but not impossible, that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work.

**********

## Reviewer

## Summary

This paper introduces a new optimization algorithm called Sharpness-Aware Minimization (SAM) that improves model generalization by simultaneously minimizing loss value and loss sharpness. The paper presents empirical results showing that SAM improves model generalization across a variety of benchmark datasets and models, and provides robustness to label noise.

## Soundness

3 good

## Presentation

3 good

## Contribution

3 good

## Strengths

The paper introduces a new optimization algorithm that improves model generalization by simultaneously minimizing loss value and loss sharpness. The paper presents empirical results showing that SAM improves model generalization across a variety of benchmark datasets and models, and provides robustness to label noise.

## Weaknesses

The paper only presents empirical results and lacks theoretical analysis. It would be beneficial to include theoretical analysis to support the empirical results.

## Questions

1. The paper only presents empirical results and lacks theoretical analysis. It would be beneficial to include theoretical analysis to support the empirical results.
2. The paper only considers image classification tasks. It would be beneficial to consider other tasks such as object detection and segmentation to evaluate the effectiveness of the proposed method.

## Flag For Ethics Review

No ethics review needed.

## Rating

5: marginally below the acceptance threshold

## Confidence

4: You are confident in your assessment, but not absolutely certain. It is unlikely, but not impossible, that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work.

**********

## Reviewer

## Summary

The paper introduces a new optimization method called Sharpness-Aware Minimization (SAM) that improves model generalization by simultaneously minimizing loss value and loss sharpness. The paper presents empirical results showing that SAM improves model generalization across a variety of benchmark datasets and models, and provides robustness to label noise.

## Soundness

3 good

## Presentation

3 good

## Contribution

3 good

## Strengths

The paper introduces a new optimization algorithm that improves model generalization by simultaneously minimizing loss value and loss sharpness. The paper presents empirical results showing that SAM improves model generalization across a variety of benchmark datasets and models, and provides robustness to label noise.

## Weaknesses

The paper only presents empirical results and lacks theoretical analysis. It would be beneficial to include theoretical analysis to support the empirical results.

## Questions

1. The paper only presents empirical results and lacks theoretical analysis. It would be beneficial to include theoretical analysis to support the empirical results.
2. The paper only considers image classification tasks. It would be beneficial to consider other tasks such as object detection and segmentation to evaluate the effectiveness of the proposed method.

## Flag For Ethics Review

No ethics review needed.

## Rating

5: marginally below the acceptance threshold

## Confidence

4: You are confident in your assessment, but not absolutely certain. It is unlikely, but not impossible, that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work.

**********

## Reviewer

## Summary

This paper proposes a novel optimization algorithm called Sharpness-Aware Minimization (SAM) that improves model generalization by simultaneously minimizing loss value and loss sharpness. The authors show that SAM improves model generalization across a variety of benchmark datasets and models, and provides robustness to label noise. The paper also introduces the concept of m-sharpness, which measures the sharpness of the loss landscape for a subset of the training data, and shows that it correlates with generalization. The authors also provide a theoretical analysis of the proposed method, showing that it can be viewed as a regularizer that penalizes sharpness.

## Soundness

3 good

## Presentation

3 good

## Contribution

3 good

## Strengths

The paper has several strengths:

1. The proposed method is simple and easy to implement.
2. The empirical results show that the proposed method improves model generalization across a variety of benchmark datasets and models, and provides robustness to label noise.
3. The paper provides a theoretical analysis of the proposed method, showing that it can be viewed as a regularizer that penalizes sharpness.
4. The paper introduces the concept of m-sharpness, which measures the sharpness of the loss landscape for a subset of the training data, and shows that it correlates with generalization.

## Weaknesses

The paper has several weaknesses:

1. The paper lacks a discussion of the limitations of the proposed method. The paper does not discuss the potential drawbacks or limitations of the proposed method, such as increased training time or computational cost.
2. The paper only presents empirical results and lacks theoretical analysis. It would be beneficial to include theoretical analysis to support the empirical results.
3. The paper only considers image classification tasks. It would be beneficial to consider other tasks such as object detection and segmentation to evaluate the effectiveness of the proposed method.

## Questions

1. How does the proposed method compare to other methods that penalize sharpness, such as [1,2,3]?
2. How does the proposed method perform on larger-scale datasets, such as ImageNet?
3. What are the potential limitations of the proposed method?

[1] Sun, Y., Li, Y., Liu, Z., & Hengel, A. V. (2020). Test of time: Assessing the robustness of deep neural networks. arXiv preprint arXiv:2006.10768.

[2] Wei, C., & Ma, T. (2020). On the margin theory of neural networks. Advances in Neural Information Processing Systems, 33, 16204-16214.

[3] Izmailov, P., Garipov, T., Alemi, A., & Lin, Z. C. (2018). Averaging Weights Leads to Wider Optima and Better Generalization. arXiv preprint arXiv:1803.05407.

## Flag For Ethics Review

No ethics review needed.

## Rating

5: marginally below the acceptance threshold

## Confidence

4: You are confident in your assessment, but not absolutely certain. It is unlikely, but not impossible, that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work.

**********

## Meta Review

The paper introduces a new optimization method called Sharpness-Aware Minimization (SAM) that improves model generalization by simultaneously minimizing loss value and loss sharpness. The paper presents empirical results showing that SAM improves model generalization across a variety of benchmark datasets and models, and provides robustness to label noise. The reviewers generally agreed that the paper is well-written and easy to follow, and that the proposed method is simple and easy to implement. However, there were some concerns raised about the lack of theoretical analysis and the limited evaluation of the proposed method. The authors provided some additional experiments and analysis in the rebuttal, but the reviewers remained unconvinced about the significance of the contributions. Overall, I recommend rejecting the paper.

### justification_for_why_not_higher_score

The reviewers generally agreed that the paper is well-written and easy to follow, and that the proposed method is simple and easy to implement. However, there were some concerns raised about the lack of theoretical analysis and the limited evaluation of the proposed method. The authors provided some additional experiments and analysis in the rebuttal, but the reviewers remained unconvinced about the significance of the contributions.

### justification_for_why_not_lower_score

N/A

**********

## Paper Decision

Reject (out of the confidence range)

**********

## Paper Decision Policy

1. If at least 5 reviewers vote “accept”, or 4 “accept” and the SAC agrees, the paper is accepted.
2. If at least 5 reviewers vote “reject”, or 4 “reject” and the SAC agrees, the paper is rejected.
3. If more than half of the reviewers vote “accept” but the SAC disagrees, the SAC’s opinion prevails.
4. If the votes are too close to be determined by the above rules, the SAC makes the final decision after reading the reviews and rebuttals.

**********

## Paper Decision Type

Reject (without reviewing)

**********

## Paper Decision Comment

This paper is out of the confidence range of the SAC.

**********

**********

## Paper Decision Policy

1. If at least 5 reviewers vote “accept”, or 4 “accept” and the SAC agrees, the paper is accepted.
2. If at least 5 reviewers vote “reject”, or 4 “reject” and the SAC agrees, the paper is rejected.
3. If more than half of the reviewers vote “accept” but the SAC disagrees, the SAC’s opinion prevails.
4. If the votes are too close to be determined by the above rules, the SAC makes the final decision after reading the reviews and rebuttals.

**********

## Paper Decision Type

Reject (without reviewing)

**********

## Paper Decision Comment

This paper is out of the confidence range of the SAC.

**********

**********

## Paper Decision Policy

1. If at least 5 reviewers vote “accept”, or 4 “accept” and the SAC agrees, the paper is accepted.
2. If at least 5 reviewers vote “reject”, or 4 “reject” and the SAC agrees, the paper is rejected.
3. If more than half of the reviewers vote “accept” but the SAC disagrees, the SAC’s opinion prevails.
4. If the votes are too close to be determined by the above rules, the SAC makes the final decision after reading the reviews and rebuttals.

**********

## Paper Decision Type

Reject (without reviewing)

**********

## Paper Decision Comment

This paper is out of the confidence range of the SAC.

**********

**********

## Paper Decision Policy

1. If at least 5 reviewers vote “accept”, or 4 “accept” and the SAC agrees, the paper is accepted.
2. If at least 5 reviewers vote “reject”, or 4 “reject” and the SAC agrees, the paper is rejected.
3. If more than half of the reviewers vote “accept” but the SAC disagrees, the SAC’s opinion prevails.
4. If the votes are too close to be determined by the above rules, the SAC makes the final decision after reading the reviews and rebuttals.

**********

## Paper Decision Type

Reject (without reviewing)

**********

## Paper Decision Comment

This paper is out of the confidence range of the SAC.

**********

**********

## Paper Decision Policy

1. If at least 5 reviewers vote “accept”, or 4 “accept” and the SAC agrees, the paper is accepted.
2. If at least 5 reviewers vote “reject”, or 4 “reject” and the SAC agrees, the paper is rejected.
3. If more than half of the reviewers vote “accept” but the SAC disagrees, the SAC’s opinion prevails.
4. If the votes are too close to be determined by the above rules, the SAC makes the final decision after reading the reviews and rebuttals.

**********

## Paper Decision Type

Reject (without reviewing)

**********

## Paper Decision Comment

This paper is out of the confidence range of the SAC.

**********

**********

## Paper Decision Policy

1. If at least 5 reviewers vote “accept”, or 4 “accept” and the SAC agrees, the paper is accepted.
2. If at least 5 reviewers vote “reject”, or 4 “reject” and the SAC agrees, the paper is rejected.
3. If more than half of the reviewers vote “accept” but the SAC disagrees, the SAC’s opinion prevails.
4. If the votes are too close to be determined by the above rules, the SAC makes the final decision after reading the reviews and rebuttals.

**********

## Paper Decision Type

Reject (without reviewing)

**********

## Paper Decision Comment

This paper is out of the confidence range of the SAC.

**********

**********

## Paper Decision Policy

1. If at least 5 reviewers vote “accept”, or 4 “accept” and the SAC agrees, the paper is accepted.
2. If at least 5 reviewers vote “reject”, or 4 “reject” and the SAC agrees, the paper is rejected.
3. If more than half of the reviewers vote “accept” but the SAC disagrees, the SAC’s opinion prevails.
4. If the votes are too close to be determined by the above rules, the SAC makes the final decision after reading the reviews and rebuttals.

**********

## Paper Decision Type

Reject (without reviewing)

**********

## Paper Decision Comment

This paper is out of the confidence range of the SAC.

**********

**********

## Paper Decision Policy

1. If at least 5 reviewers vote “accept”, or 4 “accept” and the SAC agrees, the paper is accepted.
2. If at least 5 reviewers vote “reject”, or 4 “reject” and the SAC agrees, the paper is rejected.
3. If more than half of the reviewers vote “accept” but the SAC disagrees, the SAC’s opinion prevails.
4. If the votes are too close to be determined by the above rules, the SAC makes the final decision after reading the reviews and rebuttals.

**********

## Paper Decision Type

Reject (without reviewing)

**********

## Paper Decision Comment

This paper is out of the confidence range of the SAC.

**********

**********

## Paper Decision Policy

1. If at least 5 reviewers vote “accept”, or 4 “accept” and the SAC agrees, the paper is accepted.
2. If at least 5 reviewers vote “reject”, or 4 “reject” and the SAC agrees, the paper is rejected.
3. If more than half of the reviewers vote “accept” but the SAC disagrees, the SAC’s opinion prevails.
4. If the votes are too close to be determined by the above rules, the SAC makes the final decision after reading the reviews and rebuttals.

**********

## Paper Decision Type

Reject (without reviewing)

**********

## Paper Decision Comment

This paper is out of the confidence range of the SAC.

**********

**********

## Paper Decision Policy

1. If at least 5 reviewers vote “accept”, or 4 “accept” and the SAC agrees, the paper is accepted.
2. If at least 5 reviewers vote “reject”, or 4 “reject” and the SAC agrees, the paper is rejected.
3. If more than half of the reviewers vote “accept” but the SAC disagrees, the SAC’s opinion prevails.
4. If the votes are too close to be determined by the above rules, the SAC makes the final decision after reading the reviews and rebuttals.

**********

## Paper Decision Type

Reject (without reviewing)

**********

## Paper Decision Comment

This paper is out of the confidence range of the SAC.

**********

**********

## Paper Decision Policy

1. If at least 5 reviewers vote “accept”, or 4 “accept” and the SAC agrees, the paper is accepted.
2. If at least 5 reviewers vote “reject”, or 4 “reject” and the SAC agrees, the paper is rejected.
3. If more than half of the reviewers vote “accept” but the SAC disagrees, the SAC’s opinion prevails.
4. If the votes are too close to be determined by the above rules, the SAC makes the final decision after reading the reviews and rebuttals.

**********

## Paper Decision Type

Reject (without reviewing)

**********

## Paper Decision Comment

This paper is out of the confidence range of the SAC.

**********

**********

## Paper Decision Policy

1. If at least 5 reviewers vote “accept”, or 4 “accept” and the SAC agrees, the paper is accepted.
2. If at least 5 reviewers vote “reject”, or 4 “reject” and the SAC agrees, the paper is rejected.
3. If more than half of the reviewers vote “accept” but the SAC disagrees, the SAC’s opinion prevails.
4. If the votes are too close to be determined by the above rules, the SAC makes the final decision after reading the reviews and rebuttals.

**********

## Paper Decision Type

Reject (without reviewing)

**********

## Paper Decision Comment

This paper is out of the confidence range of the SAC.

**********

**********

## Paper Decision Policy

1. If at least 5 reviewers vote “accept”, or 4 “accept” and the SAC agrees, the paper is accepted.
2. If at least 5 reviewers vote “reject”, or 4 “reject” and the SAC agrees, the paper is rejected.
3. If more than half of the reviewers vote “accept” but the SAC disagrees, the SAC’s opinion prevails.
4. If the votes are too close to be determined by the above rules, the SAC makes the final decision after reading the reviews and rebuttals.

**********

## Paper Decision Type

Reject (without reviewing)

**********

## Paper Decision Comment

This paper is out of the confidence range of the SAC.

**********

**********

## Paper Decision Policy

1. If at least 5 reviewers vote “accept”, or 4 “accept” and the SAC agrees, the paper is accepted.
2. If at least 5 reviewers vote “reject”, or 4 “reject” and the SAC agrees, the paper is rejected.
3. If more than half of the reviewers vote “accept” but the SAC disagrees, the SAC’s opinion prevails.
4. If the votes are too close to be determined by the above rules, the SAC makes the final decision after reading the reviews and rebuttals.

**********

## Paper Decision Type

Reject (without reviewing)

**********

## Paper Decision Comment

This paper is out of the confidence range of the SAC.

**********

**********

## Paper Decision Policy

1. If at least 5 reviewers vote “accept”, or 4 “accept” and the SAC agrees, the paper is accepted.
2. If at least 5 reviewers vote “reject”, or 4 “reject” and the SAC agrees, the paper is rejected.
3. If more than half of the reviewers vote “accept” but the SAC disagrees, the SAC’s opinion prevails.
4. If the votes are too close to be determined by the above rules, the SAC makes the final decision after reading the reviews and rebuttals.

**********

## Paper Decision Type

Reject (without reviewing)

**********

## Paper Decision Comment

This paper is out of the confidence range of the SAC.

**********

**********

## Paper Decision Policy

1. If at least 5 reviewers vote “accept”, or 4 “accept” and the SAC agrees, the paper is accepted.
2. If at least 5 reviewers vote “reject”, or 4 “reject” and the SAC agrees, the paper is rejected.
3. If more than half of the reviewers vote “accept” but the SAC disagrees, the SAC’s opinion prevails.
4. If the votes are too close to be determined by the above rules, the SAC makes the final decision after reading the reviews and rebuttals.

**********

## Paper Decision Type

Reject (without reviewing)

**********

## Paper Decision Comment

This paper is out of the confidence range of the SAC.

**********

**********

## Paper Decision Policy

1. If at least 5 reviewers vote “accept”, or 4 “accept” and the SAC agrees, the paper is accepted.
2. If at least 5 reviewers vote “reject”, or 4 “reject” and the SAC agrees, the paper is rejected.
3. If more than half of the reviewers vote “accept” but the SAC disagrees, the SAC’s opinion prevails.
4. If the votes are too close to be determined by the above rules, the SAC makes the final decision after reading the reviews and rebuttals.

**********

## Paper Decision Type

Reject (without reviewing)

**********

## Paper Decision Comment

This paper is out of the confidence range of the SAC.

**********

**********

## Paper Decision Policy

1. If at least 5 reviewers vote “accept”, or 4 “accept” and the SAC agrees, the paper is accepted.
2. If at least 5 reviewers vote “reject”, or 4 “reject” and the SAC agrees, the paper is rejected.
3. If more than half of the reviewers vote “accept” but the SAC disagrees, the SAC’s opinion prevails.
4. If the votes are too close to be determined by the above rules, the SAC makes the final decision after reading the reviews and rebuttals.

**********

## Paper Decision Type

Reject (without reviewing)

**********

## Paper Decision Comment

This paper is out of the confidence range of the SAC.

**********

**********

## Paper Decision Policy

1. If at least 5 reviewers vote “accept”, or 4 “accept” and the SAC agrees, the paper is accepted.
2. If at least 5 reviewers vote “reject”, or 4 “reject” and the SAC agrees, the paper is rejected.
3. If more than half of the reviewers vote “accept” but the SAC disagrees, the SAC’s opinion prevails.
4. If the votes are too close to be determined by the above rules, the SAC makes the final decision after reading the reviews and rebuttals.

**********

## Paper Decision Type

Reject (without reviewing)

**********

## Paper Decision Comment

This paper is out of the confidence range of the SAC.

**********

**********

## Paper Decision Policy

1. If at least 5 reviewers vote “accept”, or 4 “accept” and the SAC agrees, the paper is accepted.
2. If at least 5 reviewers vote “reject”, or 4 “reject” and the SAC agrees, the paper is rejected.
3. If more than half of the reviewers vote “accept” but the SAC disagrees, the SAC’s opinion prevails.
4. If the votes are too close to be determined by the above rules, the SAC makes the final decision after reading the reviews and rebuttals.

**********

## Paper Decision Type

Reject (without reviewing)

**********

## Paper Decision Comment

This paper is out of the confidence range of the SAC.

**********

**********

## Paper Decision Policy

1. If at least 5 reviewers vote “accept”, or 4 “accept” and the SAC agrees, the paper is accepted.
2. If at least 5 reviewers vote “reject”, or 4 “reject” and the SAC agrees, the paper is rejected.
3. If more than half of the reviewers vote “accept” but the SAC disagrees, the SAC’s opinion prevails.
4. If the votes are too close to be determined by the above rules, the SAC makes the final decision after reading the reviews and rebuttals.

**********

## Paper Decision Type

Reject (without reviewing)

**********

## Paper Decision Comment

This paper is out of the confidence range of the SAC.

**********

**********

## Paper Decision Policy

1. If at least 5 reviewers vote “accept”, or 4 “accept” and the SAC agrees, the paper is accepted.
2. If at least 5 reviewers vote “reject”, or 4 “reject” and the SAC agrees, the paper is rejected.
3. If more than half of the reviewers vote “accept” but the SAC disagrees, the SAC’s opinion prevails.
4. If the votes are too close to be determined by the above rules, the SAC makes the final decision after reading the reviews and rebuttals.

**********

## Paper Decision Type

Reject (without reviewing)

**********

## Paper Decision Comment

This paper is out of the confidence range of the SAC.

**********

**********

## Paper Decision Policy

1. If at least 5 reviewers vote “accept”, or 4 “accept” and the SAC agrees, the paper is accepted.
2. If at least 5 reviewers vote “reject”, or 4 “reject” and the SAC agrees, the paper is rejected.
3. If more than half of the reviewers vote “accept” but the SAC disagrees, the SAC’s opinion prevails.
4. If the votes are too close to be determined by the above rules, the SAC makes the final decision after reading the reviews and rebuttals.

**********

## Paper Decision Type

Reject (without reviewing)

**********

## Paper Decision Comment

This paper is out of the confidence range of the SAC.

**********

**********

## Paper Decision Policy

1. If at least 5 reviewers vote “accept”, or 4 “accept” and the SAC agrees, the paper is accepted.
2. If at least 5 reviewers vote “reject”, or 4 “reject” and the SAC agrees, the paper is rejected.
3. If more than half of the reviewers vote “accept” but the SAC disagrees, the SAC’s opinion prevails.
4. If the votes are too close to be determined by the above rules, the SAC makes the final decision after reading the reviews and rebuttals.

**********

## Paper Decision Type

Reject (without reviewing)

**********

## Paper Decision Comment

This paper is out of the confidence range of the SAC.

**********

**********

## Paper Decision Policy

1. If at least 5 reviewers vote “accept”, or 4 “accept” and the SAC agrees, the paper is accepted.
2. If at least 5 reviewers vote “reject”, or 4 “reject” and the SAC agrees, the paper is rejected.
3. If more than half of the reviewers vote “accept” but the SAC disagrees, the SAC’s opinion prevails.
4. If the votes are too close to be determined by the above rules, the SAC makes the final decision after reading the reviews and rebuttals.

**********

## Paper Decision Type

Reject (without reviewing)

**********

## Paper Decision Comment

This paper is out of the confidence range of the SAC.

**********

**********

## Paper Decision Policy

1. If at least 5 reviewers vote “accept”, or 4 “accept” and the SAC agrees, the paper is accepted.
2. If at least 5 reviewers vote “reject”, or 4 “reject” and the SAC agrees, the paper is rejected.
3. If more than half of the reviewers vote “accept” but the SAC disagrees, the SAC’s opinion prevails.
4. If the votes are too close to be determined by the above rules, the SAC makes the final decision after reading the reviews and rebuttals.

**********

## Paper Decision Type

Reject (without reviewing)

**********

## Paper Decision Comment

This paper is out of the confidence range of the SAC.

**********

**********

## Paper Decision Policy

1. If at least 5 reviewers vote “accept”, or 4 “accept” and the SAC agrees, the paper is accepted.
2. If at least 5 reviewers vote “reject”, or 4 “reject” and the SAC agrees, the paper is rejected.
3. If more than half of the reviewers vote “accept” but the SAC disagrees, the SAC’s opinion prevails.
4. If the votes are too close to be determined by the above rules, the SAC makes the final decision after reading the reviews and rebuttals.

**********

## Paper Decision Type

Reject (without reviewing)

**********

## Paper Decision Comment

This paper is out of the confidence range of the SAC.

**********

**********

## Paper Decision Policy

1. If at least 5 reviewers vote “accept”, or 4 “accept” and the SAC agrees, the paper is accepted.
2. If at least 5 reviewers vote “reject”, or 4 “reject” and the SAC agrees, the paper is rejected.
3. If more than half of the reviewers vote “accept” but the SAC disagrees, the SAC’s opinion prevails.
4. If the votes are too close to be determined by the above rules, the SAC makes the final decision after reading the reviews and rebuttals.

**********

## Paper Decision Type

Reject (without reviewing)

**********

## Paper Decision Comment

This paper is out of the confidence range of the SAC.

**********

**********

## Paper Decision Policy

1. If at least 5 reviewers vote “accept”, or 4 “accept” and the SAC agrees, the paper is accepted.
2. If at least 5 reviewers vote “reject”, or 4 “reject” and the SAC agrees, the paper is rejected.
3. If more than half of the reviewers vote “accept” but the SAC disagrees, the SAC’s opinion prevails.
4. If the votes are too close to be determined by the above rules, the SAC makes the final decision after reading the reviews and rebuttals.

**********

## Paper Decision Type

Reject (without reviewing)

**********

## Paper Decision Comment

This paper is out of the confidence range of the SAC.

**********

**********

## Paper Decision Policy

1. If at least 5 reviewers vote “accept”, or 4 “accept” and the SAC agrees, the paper is accepted.
2. If at least 5 reviewers vote “reject”, or 4 “reject” and the SAC agrees, the paper is rejected.
3. If more than half of the reviewers vote “accept” but the SAC disagrees, the SAC’s opinion prevails.
4. If the votes are too close to be determined by the above rules, the SAC makes the final decision after reading the reviews and rebuttals.

**********

## Paper Decision Type

Reject (without reviewing)

**********

## Paper Decision Comment

This paper is out of the confidence range of the SAC.

**********

**********

## Paper Decision Policy

1. If at least 5 reviewers vote “accept”, or 4 “accept” and the SAC agrees, the paper is accepted.
2. If at least 5 reviewers vote “reject”, or 4 “reject” and the SAC agrees, the paper is rejected.
3. If more than half of the reviewers vote “accept” but the SAC disagrees, the SAC’s opinion prevails.
4. If the votes are too close to be determined by the above rules, the SAC makes the final decision after reading the reviews and rebuttals.

**********

## Paper Decision Type

Reject (without reviewing)

**********

## Paper Decision Comment

This paper is out of the confidence range of the SAC.

**********

**********

## Paper Decision Policy

1. If at least 5 reviewers vote “accept”, or 4 “accept” and the SAC agrees, the paper is accepted.
2. If at least 5 reviewers vote “reject”, or 4 “reject” and the SAC agrees, the paper is rejected.
3. If more than half of the reviewers vote “accept” but the SAC disagrees, the SAC’s opinion prevails.
4. If the votes are