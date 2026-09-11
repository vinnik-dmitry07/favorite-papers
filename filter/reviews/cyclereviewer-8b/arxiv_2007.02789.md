## Summary

This paper addresses two challenges in representational similarity analysis (RSA): 1) the bias introduced by measurement noise in dissimilarity estimates, and 2) the dependency between dissimilarity estimates. The authors derive analytical expressions for the bias and variance of the squared Euclidean and Mahalanobis distances, and propose a new method, the whitened unbiased RDM cosine similarity (WUC), that takes into account the dependency between dissimilarity estimates. The authors also show that WUC is equivalent to the linear Centered Kernel Alignment (CKA) and the RV coefficient. The authors demonstrate the effectiveness of WUC in simulations and real-world data.

## Soundness

2 fair

## Presentation

2 fair

## Contribution

2 fair

## Strengths

- The paper addresses two important challenges in RSA: the bias introduced by measurement noise in dissimilarity estimates and the dependency between dissimilarity estimates.

- The authors derive analytical expressions for the bias and variance of the squared Euclidean and Mahalanobis distances, which provides a theoretical foundation for their method.

- The proposed method, WUC, is shown to be equivalent to the linear Centered Kernel Alignment (CKA) and the RV coefficient, which provides a connection to existing methods.

## Weaknesses

- The paper is not well written and is difficult to follow. The authors should consider revising the paper to make it more accessible to a broader audience.

- The paper only considers the Euclidean and Mahalanobis distances, and it is not clear how the method would generalize to other dissimilarity measures.

- The paper does not provide a thorough evaluation of the method, and it is not clear how it compares to existing methods.

- The paper does not provide a clear discussion of the limitations of the method and potential areas for future work.

## Questions

- What are the limitations of the method? How does it compare to existing methods?

- How does the method generalize to other dissimilarity measures?

- What are the computational costs associated with the method?

- How does the method perform on real-world data?

## Flag For Ethics Review

No ethics review needed.

## Rating

5: marginally below the acceptance threshold

## Confidence

3: You are fairly confident in your assessment. It is possible that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work. Math/other details were not carefully checked.

**********

## Reviewer

## Summary

The authors present a method for comparing representational similarity matrices (RDMs) that takes into account the covariance structure of the data. The method is based on the idea that the RDM elements are correlated with each other and that this correlation structure should be taken into account when comparing RDMs. The authors provide an analytical expression for the covariance matrix of the RDM elements and show that it can be used to whiten the RDMs, leading to a new criterion for RDM similarity. They also show that this new criterion is equivalent to the linear Centered Kernel Alignment (CKA) and the RV coefficient.

## Soundness

3 good

## Presentation

3 good

## Contribution

2 fair

## Strengths

- The paper is well-written and easy to follow.
- The authors provide a detailed derivation of the analytical expression for the covariance matrix of the RDM elements.
- The authors show that the new criterion for RDM similarity is equivalent to the linear Centered Kernel Alignment (CKA) and the RV coefficient.

## Weaknesses

- The paper does not provide any empirical evaluations of the proposed method. The authors only provide a simulation study on synthetic data.
- The paper does not discuss the limitations of the proposed method. For example, it is not clear how the method performs when the data is not normally distributed.
- The paper does not discuss the computational complexity of the proposed method. It is not clear how the method scales with the number of conditions and partitions.
- The paper does not provide any code for implementing the proposed method.

## Questions

- How does the proposed method perform when the data is not normally distributed?
- How does the proposed method scale with the number of conditions and partitions?
- What are the computational costs associated with the proposed method?
- Can you provide code for implementing the proposed method?

## Flag For Ethics Review

No ethics review needed.

## Rating

5: marginally below the acceptance threshold

## Confidence

2: You are willing to defend your assessment, but it is quite likely that you did not understand the central parts of the submission or that you are unfamiliar with some pieces of related work. Math/other details were not carefully checked.

**********

## Reviewer

## Summary

The authors address two challenges in RSA: 1) the bias introduced by measurement noise in dissimilarity estimates, and 2) the dependency between dissimilarity estimates. The authors derive analytical expressions for the bias and variance of the squared Euclidean and Mahalanobis distances, and propose a new method, the whitened unbiased RDM cosine similarity (WUC), that takes into account the dependency between dissimilarity estimates. The authors also show that WUC is equivalent to the linear Centered Kernel Alignment (CKA) and the RV coefficient. The authors demonstrate the effectiveness of WUC in simulations and real-world data.

## Soundness

3 good

## Presentation

3 good

## Contribution

3 good

## Strengths

The authors derive analytical expressions for the bias and variance of the squared Euclidean and Mahalanobis distances, which provides a theoretical foundation for their method.

The proposed method, WUC, is shown to be equivalent to the linear Centered Kernel Alignment (CKA) and the RV coefficient, which provides a connection to existing methods.

The authors demonstrate the effectiveness of WUC in simulations and real-world data.

## Weaknesses

The paper only considers the Euclidean and Mahalanobis distances, and it is not clear how the method would generalize to other dissimilarity measures.

The paper does not provide a thorough evaluation of the method, and it is not clear how it compares to existing methods.

The paper does not provide a clear discussion of the limitations of the method and potential areas for future work.

## Questions

How does the method generalize to other dissimilarity measures?

How does the method compare to existing methods?

What are the limitations of the method?

What are potential areas for future work?

## Flag For Ethics Review

No ethics review needed.

## Rating

6: marginally above the acceptance threshold

## Confidence

3: You are fairly confident in your assessment. It is possible that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work. Math/other details were not carefully checked.

**********

## Reviewer

## Summary

This paper addresses two challenges in Representational Similarity Analysis (RSA): 1) the bias introduced by measurement noise in dissimilarity estimates, and 2) the dependency between dissimilarity estimates. The authors derive analytical expressions for the bias and variance of the squared Euclidean and Mahalanobis distances, and propose a new method, the whitened unbiased RDM cosine similarity (WUC), that takes into account the dependency between dissimilarity estimates. The authors also show that WUC is equivalent to the linear Centered Kernel Alignment (CKA) and the RV coefficient. The authors demonstrate the effectiveness of WUC in simulations and real-world data.

## Soundness

3 good

## Presentation

3 good

## Contribution

3 good

## Strengths

The paper addresses two important challenges in RSA: the bias introduced by measurement noise in dissimilarity estimates and the dependency between dissimilarity estimates.

The authors derive analytical expressions for the bias and variance of the squared Euclidean and Mahalanobis distances, which provides a theoretical foundation for their method.

The proposed method, WUC, is shown to be equivalent to the linear Centered Kernel Alignment (CKA) and the RV coefficient, which provides a connection to existing methods.

The authors demonstrate the effectiveness of WUC in simulations and real-world data.

## Weaknesses

The paper only considers the Euclidean and Mahalanobis distances, and it is not clear how the method would generalize to other dissimilarity measures.

The paper does not provide a thorough evaluation of the method, and it is not clear how it compares to existing methods.

The paper does not provide a clear discussion of the limitations of the method and potential areas for future work.

## Questions

How does the method generalize to other dissimilarity measures?

How does the method compare to existing methods?

What are the limitations of the method?

What are potential areas for future work?

## Flag For Ethics Review

No ethics review needed.

## Rating

6: marginally above the acceptance threshold

## Confidence

3: You are fairly confident in your assessment. It is possible that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work. Math/other details were not carefully checked.

**********

## Meta Review

This paper addresses two challenges in Representational Similarity Analysis (RSA): 1) the bias introduced by measurement noise in dissimilarity estimates, and 2) the dependency between dissimilarity estimates. The authors derive analytical expressions for the bias and variance of the squared Euclidean and Mahalanobis distances, and propose a new method, the whitened unbiased RDM cosine similarity (WUC), that takes into account the dependency between dissimilarity estimates. The authors also show that WUC is equivalent to the linear Centered Kernel Alignment (CKA) and the RV coefficient. The authors demonstrate the effectiveness of WUC in simulations and real-world data.

The paper received 4 reviews. The reviewers generally agreed that the paper addresses two important challenges in RSA, and the authors derive analytical expressions for the bias and variance of the squared Euclidean and Mahalanobis distances, which provides a theoretical foundation for their method. The proposed method, WUC, is shown to be equivalent to the linear Centered Kernel Alignment (CKA) and the RV coefficient, which provides a connection to existing methods. The authors demonstrate the effectiveness of WUC in simulations and real-world data.

However, the reviewers also pointed out that the paper only considers the Euclidean and Mahalanobis distances, and it is not clear how the method would generalize to other dissimilarity measures. The paper does not provide a thorough evaluation of the method, and it is not clear how it compares to existing methods. The paper does not provide a clear discussion of the limitations of the method and potential areas for future work.

Based on the reviews, I recommend that the paper be rejected. The authors are encouraged to address the concerns raised by the reviewers and resubmit the paper to a future conference.

### justification_for_why_not_higher_score

The paper received 4 reviews. The reviewers generally agreed that the paper addresses two important challenges in RSA, and the authors derive analytical expressions for the bias and variance of the squared Euclidean and Mahalanobis distances, which provides a theoretical foundation for their method. The proposed method, WUC, is shown to be equivalent to the linear Centered Kernel Alignment (CKA) and the RV coefficient, which provides a connection to existing methods. The authors demonstrate the effectiveness of WUC in simulations and real-world data.

However, the reviewers also pointed out that the paper only considers the Euclidean and Mahalanobis distances, and it is not clear how the method would generalize to other dissimilarity measures. The paper does not provide a thorough evaluation of the method, and it is not clear how it compares to existing methods. The paper does not provide a clear discussion of the limitations of the method and potential areas for future work.

### justification_for_why_not_lower_score

N/A

**********

## Paper Decision

Reject (poster)