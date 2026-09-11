## Summary

This paper presents a new optimizer, Lamb, for training large deep neural networks using large batch sizes. The authors provide convergence analysis of Lamb and Lars, and demonstrate the superior performance of Lamb across various tasks, including BERT and ResNet-50 training.

## Soundness

2 fair

## Presentation

1 poor

## Contribution

2 fair

## Strengths

1. The paper is well-written and easy to follow.

2. The authors provide convergence analysis of Lamb and Lars, which is a significant contribution.

3. The authors demonstrate the superior performance of Lamb across various tasks, including BERT and ResNet-50 training.

## Weaknesses

1. The paper is not well-organized. The authors present the convergence analysis of Lamb and Lars in Section 3, but do not provide any experimental results in this section. Instead, the experimental results are presented in Section 4. This makes it difficult to understand the significance of the convergence analysis.

2. The paper lacks a clear motivation for the proposed algorithm. The authors do not explain why Lamb is necessary, or how it differs from existing algorithms.

3. The paper lacks a thorough comparison with existing algorithms. The authors only compare Lamb with Lars and SGD, but do not compare it with other popular optimization algorithms such as Adam and Adagrad.

4. The paper lacks a thorough analysis of the experimental results. The authors only present the results in tables, but do not provide any analysis or discussion of the results.

5. The paper lacks a clear conclusion. The authors do not summarize the main contributions of the paper or provide any recommendations for future work.

## Questions

1. Why is Lamb necessary? How does it differ from existing algorithms?

2. Why is the convergence analysis of Lamb and Lars presented in Section 3, but not in Section 4?

3. Why is Lamb compared only with Lars and SGD, and not with other popular optimization algorithms such as Adam and Adagrad?

4. Why are the experimental results only presented in tables, and not analyzed or discussed?

5. What are the main contributions of the paper? What are the implications of the results?

## Flag For Ethics Review

No ethics review needed.

## Rating

3: reject, not good enough

## Confidence

4: You are confident in your assessment, but not absolutely certain. It is unlikely, but not impossible, that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work.

**********

## Reviewer

## Summary

The paper proposes a new adaptive learning rate method, Lamb, which is a generalization of Lars. The paper provides a theoretical analysis of Lamb and demonstrates its effectiveness in large-scale deep learning tasks.

## Soundness

3 good

## Presentation

3 good

## Contribution

3 good

## Strengths

1. The paper is well-written and easy to follow.
2. The proposed method is simple and intuitive.
3. The theoretical analysis is sound and provides insights into the behavior of Lamb.
4. The experimental results are convincing and demonstrate the effectiveness of Lamb.

## Weaknesses

1. The paper only considers the case where the base algorithm is SGD or Adam. It would be interesting to see how Lamb performs with other base algorithms, such as Adagrad or RMSProp.
2. The paper only considers the case where the base algorithm is SGD or Adam. It would be interesting to see how Lamb performs with other base algorithms, such as Adagrad or RMSProp.
3. The paper does not provide a detailed discussion of the hyperparameters required for Lamb. It would be helpful to provide guidance on how to choose the hyperparameters for different tasks.
4. The paper does not provide a detailed discussion of the computational cost of Lamb. It would be helpful to provide a comparison of the computational cost of Lamb with other adaptive learning rate methods.

## Questions

See above.

## Flag For Ethics Review

No ethics review needed.

## Rating

6: marginally above the acceptance threshold

## Confidence

3: You are fairly confident in your assessment. It is possible that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work. Math/other details were not carefully checked.

**********

## Reviewer

## Summary

This paper proposes a new layerwise adaptive large batch optimization technique called Lamb. The authors provide convergence analysis of Lamb as well as Lars, and demonstrate the superior performance of Lamb across various tasks such as Bert and ResNet-50 training with very little hyperparameter tuning.

## Soundness

3 good

## Presentation

3 good

## Contribution

3 good

## Strengths

- The paper is well-written and easy to follow.
- The proposed method is simple and intuitive.
- The theoretical analysis is sound and provides insights into the behavior of Lamb.
- The experimental results are convincing and demonstrate the effectiveness of Lamb.
- The paper is well-organized and easy to follow.

## Weaknesses

- The paper only considers the case where the base algorithm is SGD or Adam. It would be interesting to see how Lamb performs with other base algorithms, such as Adagrad or RMSProp.
- The paper does not provide a detailed discussion of the hyperparameters required for Lamb. It would be helpful to provide guidance on how to choose the hyperparameters for different tasks.
- The paper does not provide a detailed discussion of the computational cost of Lamb. It would be helpful to provide a comparison of the computational cost of Lamb with other adaptive learning rate methods.

## Questions

- In the experimental results, the authors compare Lamb with Lars and SGD, but not with other popular optimization algorithms such as Adam and Adagrad. It would be interesting to see how Lamb compares with these algorithms.
- The paper does not provide a detailed discussion of the hyperparameters required for Lamb. It would be helpful to provide guidance on how to choose the hyperparameters for different tasks.

## Flag For Ethics Review

No ethics review needed.

## Rating

6: marginally above the acceptance threshold

## Confidence

3: You are fairly confident in your assessment. It is possible that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work. Math/other details were not carefully checked.

**********

## Reviewer

## Summary

The paper proposes a new layerwise adaptive large batch optimization technique called Lamb. The authors provide convergence analysis of Lamb as well as Lars, and demonstrate the superior performance of Lamb across various tasks such as Bert and ResNet-50 training with very little hyperparameter tuning.

## Soundness

3 good

## Presentation

3 good

## Contribution

3 good

## Strengths

1. The paper is well-written and easy to follow.
2. The proposed method is simple and intuitive.
3. The theoretical analysis is sound and provides insights into the behavior of Lamb.
4. The experimental results are convincing and demonstrate the effectiveness of Lamb.
5. The paper is well-organized and easy to follow.

## Weaknesses

1. The paper only considers the case where the base algorithm is SGD or Adam. It would be interesting to see how Lamb performs with other base algorithms, such as Adagrad or RMSProp.
2. The paper does not provide a detailed discussion of the hyperparameters required for Lamb. It would be helpful to provide guidance on how to choose the hyperparameters for different tasks.
3. The paper does not provide a detailed discussion of the computational cost of Lamb. It would be helpful to provide a comparison of the computational cost of Lamb with other adaptive learning rate methods.

## Questions

1. In the experimental results, the authors compare Lamb with Lars and SGD, but not with other popular optimization algorithms such as Adam and Adagrad. It would be interesting to see how Lamb compares with these algorithms.
2. The paper does not provide a detailed discussion of the hyperparameters required for Lamb. It would be helpful to provide guidance on how to choose the hyperparameters for different tasks.

## Flag For Ethics Review

No ethics review needed.

## Rating

6: marginally above the acceptance threshold

## Confidence

3: You are fairly confident in your assessment. It is possible that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work. Math/other details were not carefully checked.

**********

## Meta Review

The paper presents a new optimization algorithm, Lamb, for training large-scale deep learning models. The authors provide theoretical analysis and demonstrate the effectiveness of Lamb in various tasks, including BERT and ResNet-50 training. The reviewers have provided mixed ratings, with some reviewers praising the paper's clarity and simplicity, while others have raised concerns about the lack of comparison with other algorithms and the limited discussion of hyperparameters. The authors have provided a response to the reviewers' concerns, but the paper still lacks a thorough comparison with other algorithms and a detailed discussion of the computational cost of Lamb. Therefore, I recommend rejecting the paper.

### justification_for_why_not_higher_score

The paper lacks a thorough comparison with other algorithms and a detailed discussion of the computational cost of Lamb.

### justification_for_why_not_lower_score

N/A

**********

## Paper Decision

Reject (not selected for publication)