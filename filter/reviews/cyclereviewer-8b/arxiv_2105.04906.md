## Reviewer

### Summary

This paper proposes a new self-supervised learning method based on the principle of preserving the information content of the embeddings. The basic idea is to use a loss function with three terms: Invariance, Variance and Covariance. The proposed method is evaluated on several downstream tasks and compared with other state-of-the-art methods.

### Soundness

2 fair

### Presentation

2 fair

### Contribution

2 fair

### Strengths

- The proposed method is simple and easy to implement.
- The proposed method is evaluated on several downstream tasks and compared with other state-of-the-art methods.

### Weaknesses

- The novelty of the proposed method is limited. The proposed method is based on the principle of preserving the information content of the embeddings. The method is similar to the Barlow Twins method, which also decorrelates the variables of each embedding and prevents an informational collapse in which the variables would vary together or be highly correlated.
- The experiments are not sufficient. The proposed method is only evaluated on several downstream tasks. It is not clear whether the proposed method can be applied to other tasks, such as video recognition.
- The paper is not well written. The organization of the paper is not clear. The figures are not clear. The experiments are not sufficient.

### Questions

- The proposed method is based on the principle of preserving the information content of the embeddings. The method is similar to the Barlow Twins method, which also decorrelates the variables of each embedding and prevents an informational collapse in which the variables would vary together or be highly correlated. What is the difference between the proposed method and the Barlow Twins method?
- The experiments are not sufficient. The proposed method is only evaluated on several downstream tasks. It is not clear whether the proposed method can be applied to other tasks, such as video recognition.
- The paper is not well written. The organization of the paper is not clear. The figures are not clear. The experiments are not sufficient.

### Flag For Ethics Review

No ethics review needed.

### Rating

3: reject, not good enough

### Confidence

3: You are fairly confident in your assessment. It is possible that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work. Math/other details were not carefully checked.

**********

## Reviewer

### Summary

This paper proposes a new self-supervised learning method called VICReg, which uses a loss function with three terms: Invariance, Variance and Covariance. The proposed method is evaluated on several downstream tasks and compared with other state-of-the-art methods.

### Soundness

3 good

### Presentation

3 good

### Contribution

2 fair

### Strengths

- The proposed method is simple and easy to implement.
- The proposed method is evaluated on several downstream tasks and compared with other state-of-the-art methods.

### Weaknesses

- The novelty of the proposed method is limited. The proposed method is based on the principle of preserving the information content of the embeddings. The method is similar to the Barlow Twins method, which also decorrelates the variables of each embedding and prevents an informational collapse in which the variables would vary together or be highly correlated.
- The experiments are not sufficient. The proposed method is only evaluated on several downstream tasks. It is not clear whether the proposed method can be applied to other tasks, such as video recognition.
- The paper is not well written. The organization of the paper is not clear. The figures are not clear. The experiments are not sufficient.

### Questions

- The proposed method is based on the principle of preserving the information content of the embeddings. The method is similar to the Barlow Twins method, which also decorrelates the variables of each embedding and prevents an informational collapse in which the variables would vary together or be highly correlated. What is the difference between the proposed method and the Barlow Twins method?
- The experiments are not sufficient. The proposed method is only evaluated on several downstream tasks. It is not clear whether the proposed method can be applied to other tasks, such as video recognition.
- The paper is not well written. The organization of the paper is not clear. The figures are not clear. The experiments are not sufficient.

### Flag For Ethics Review

No ethics review needed.

### Rating

5: marginally below the acceptance threshold

### Confidence

4: You are confident in your assessment, but not absolutely certain. It is unlikely, but not impossible, that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work.

**********

## Reviewer

### Summary

The authors propose VICReg, a self-supervised learning method that aims to avoid the collapse problem in which the encoders produce constant or non-informative vectors. The method uses two regularization terms applied to both embeddings separately: (1) a term that maintains the variance of each embedding dimension above a threshold, (2) a term that decorrelates each pair of variables. The method is evaluated on several downstream tasks and compared with other state-of-the-art methods.

### Soundness

2 fair

### Presentation

3 good

### Contribution

2 fair

### Strengths

The proposed method is simple and easy to implement. The method does not require techniques such as weight sharing between the branches, batch normalization, feature-wise normalization, output quantization, stop gradient, memory banks, etc. The method achieves results on par with the state of the art on several downstream tasks.

### Weaknesses

The novelty of the proposed method is limited. The method is based on the principle of preserving the information content of the embeddings, which is similar to the Barlow Twins method. The method does not require normalization, but it is not clear if the method can be applied to other tasks, such as video recognition.

### Questions

1. What are the advantages of the proposed method compared to the Barlow Twins method?
2. Can the proposed method be applied to other tasks, such as video recognition?
3. How does the proposed method compare to other self-supervised learning methods in terms of computational cost and memory usage?

### Flag For Ethics Review

No ethics review needed.

### Rating

5: marginally below the acceptance threshold

### Confidence

3: You are fairly confident in your assessment. It is possible that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work. Math/other details were not carefully checked.

**********

## Reviewer

### Summary

This paper proposes a novel method for self-supervised learning called VICReg. The method is based on a joint embedding architecture and uses a loss function with three terms: invariance, variance, and covariance. The authors evaluate the proposed method on several downstream tasks and compare it with other state-of-the-art methods.

### Soundness

3 good

### Presentation

3 good

### Contribution

3 good

### Strengths

- The paper is well-written and easy to follow.
- The proposed method is simple and easy to implement.
- The proposed method is evaluated on several downstream tasks and compared with other state-of-the-art methods.
- The authors provide a detailed analysis of the method and its components.

### Weaknesses

- The novelty of the proposed method is limited. The method is based on the principle of preserving the information content of the embeddings, which is similar to the Barlow Twins method. The method does not require normalization, but it is not clear if the method can be applied to other tasks, such as video recognition.
- The experiments are not sufficient. The proposed method is only evaluated on several downstream tasks. It is not clear whether the proposed method can be applied to other tasks, such as video recognition.
- The paper is not well written. The organization of the paper is not clear. The figures are not clear. The experiments are not sufficient.

### Questions

- The proposed method is based on the principle of preserving the information content of the embeddings. The method is similar to the Barlow Twins method, which also decorrelates the variables of each embedding and prevents an informational collapse in which the variables would vary together or be highly correlated. What is the difference between the proposed method and the Barlow Twins method?
- The experiments are not sufficient. The proposed method is only evaluated on several downstream tasks. It is not clear whether the proposed method can be applied to other tasks, such as video recognition.
- The paper is not well written. The organization of the paper is not clear. The figures are not clear. The experiments are not sufficient.

### Flag For Ethics Review

No ethics review needed.

### Rating

5: marginally below the acceptance threshold

### Confidence

3: You are fairly confident in your assessment. It is possible that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work. Math/other details were not carefully checked.

**********

## Meta Review

The paper introduces VICReg, a self-supervised learning method that avoids the collapse problem in encoders by using two regularization terms: maintaining variance and decorrelating variables. The method does not require weight sharing, batch normalization, or other techniques, achieving results comparable to state-of-the-art methods on several downstream tasks. However, the novelty is limited, and the experiments are not sufficient. The paper is not well written, and the organization is unclear. The figures are not clear, and the experiments are not sufficient.

### justification_for_why_not_higher_score

The novelty of the proposed method is limited, and the experiments are not sufficient. The paper is not well written, and the organization is unclear. The figures are not clear, and the experiments are not sufficient.

### justification_for_why_not_lower_score

N/A

**********

## Paper Decision

Reject (out of the scope of ICLR)