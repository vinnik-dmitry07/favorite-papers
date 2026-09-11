## Reviewer

### Summary

This paper studies the low-rank bias of gradient descent on factored models. The authors show that the low-rank bias of gradient descent is due to its gauge equivariance. The authors then show that the low-rank bias is not present in Adam. The authors also show that the low-rank bias is not present in other adaptive methods such as RMSProp and signSGD. The authors then show that the low-rank bias is present in some non-adaptive methods such as Shampoo and Muon.

### Soundness

3 good

### Presentation

3 good

### Contribution

3 good

### Strengths

The paper is well-written and easy to follow. The authors provide a clear explanation of the low-rank bias of gradient descent and the absence of the low-rank bias in Adam and other adaptive methods. The authors also provide a clear explanation of the low-rank bias in non-adaptive methods such as Shampoo and Muon.

### Weaknesses

The main weakness of the paper is that the authors do not provide a clear explanation of why the low-rank bias is present in some non-adaptive methods such as Shampoo and Muon. The authors only provide a partial explanation of why the low-rank bias is present in these methods.

### Questions

1. Why is the low-rank bias not present in Adam and other adaptive methods? Is it because these methods are not gauge equivariant?
2. Why is the low-rank bias present in Shampoo and Muon? Is it because these methods are gauge equivariant?
3. Can you provide a clear explanation of why the low-rank bias is present in Shampoo and Muon?

### Flag For Ethics Review

No ethics review needed.

### Rating

6: marginally above the acceptance threshold

### Confidence

3: You are fairly confident in your assessment. It is possible that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work. Math/other details were not carefully checked.

**********

## Reviewer

### Summary

This paper studies the implicit bias of various optimizers on factored models. The authors show that the implicit bias of gradient descent on factored models is due to its gauge equivariance. They then show that Adam and other coordinate-wise methods do not have this property, which explains why they do not have the same implicit bias as gradient descent. They also show that shared-scalar preconditioners, such as Muon and Shampoo, do have this property. They then perform experiments on matrix sensing and transformer models to demonstrate the effect of this property on the implicit bias of the optimizers.

### Soundness

3 good

### Presentation

3 good

### Contribution

3 good

### Strengths

- The paper is well-written and easy to follow. The authors provide a clear explanation of the low-rank bias of gradient descent and the absence of the low-rank bias in Adam and other adaptive methods. The authors also provide a clear explanation of the low-rank bias in non-adaptive methods such as Shampoo and Muon.

- The paper provides a clear explanation of the low-rank bias of gradient descent and the absence of the low-rank bias in Adam and other adaptive methods. The authors also provide a clear explanation of the low-rank bias in non-adaptive methods such as Shampoo and Muon.

- The paper provides a clear explanation of the low-rank bias of gradient descent and the absence of the low-rank bias in Adam and other adaptive methods. The authors also provide a clear explanation of the low-rank bias in non-adaptive methods such as Shampoo and Muon.

### Weaknesses

- The paper only considers the low-rank bias of gradient descent on factored models. It would be interesting to see how the results generalize to other implicit biases, such as the implicit bias of gradient descent on overparameterized models.

- The paper only considers the implicit bias of gradient descent on factored models. It would be interesting to see how the results generalize to other optimizers, such as stochastic gradient descent and momentum.

- The paper only considers the implicit bias of gradient descent on factored models. It would be interesting to see how the results generalize to other optimization problems, such as least squares and logistic regression.

- The paper only considers the implicit bias of gradient descent on factored models. It would be interesting to see how the results generalize to other neural network architectures, such as convolutional neural networks and recurrent neural networks.

- The paper only considers the implicit bias of gradient descent on factored models. It would be interesting to see how the results generalize to other tasks, such as image classification and language modeling.

### Questions

- Can the results be generalized to other implicit biases, such as the implicit bias of gradient descent on overparameterized models?

- Can the results be generalized to other optimizers, such as stochastic gradient descent and momentum?

- Can the results be generalized to other optimization problems, such as least squares and logistic regression?

- Can the results be generalized to other neural network architectures, such as convolutional neural networks and recurrent neural networks?

- Can the results be generalized to other tasks, such as image classification and language modeling?

### Flag For Ethics Review

No ethics review needed.

### Rating

6: marginally above the acceptance threshold

### Confidence

3: You are fairly confident in your assessment. It is possible that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work. Math/other details were not carefully checked.

**********

## Reviewer

### Summary

This paper studies the implicit regularization effect of various optimization algorithms on factored models, where the model parameters are represented as the product of two factors $U$ and $V$. The paper shows that gradient descent on factored models is implicitly biased toward low-rank solutions, while Adam and other adaptive methods are not. The paper provides a criterion for determining whether an optimizer preserves or breaks the low-rank inductive bias, and shows that some optimizers such as gradient descent, momentum, and Muon preserve the bias, while others such as Adam and RMSProp do not. The paper also shows that the low-rank bias is not present in Shampoo and other non-adaptive methods. The paper provides a theoretical analysis of the low-rank bias of various optimization algorithms, and demonstrates the effect of the bias on the performance of the algorithms in experiments on matrix sensing and transformer models.

### Soundness

3 good

### Presentation

3 good

### Contribution

3 good

### Strengths

1. The paper provides a clear and concise summary of the main results and contributions.
2. The paper provides a detailed theoretical analysis of the low-rank bias of various optimization algorithms.
3. The paper provides experimental results that demonstrate the effect of the low-rank bias on the performance of the algorithms.

### Weaknesses

1. The paper does not provide a clear explanation of the low-rank bias of gradient descent on factored models.
2. The paper does not provide a clear explanation of the low-rank bias of adaptive methods such as Adam and RMSProp.
3. The paper does not provide a clear explanation of the low-rank bias of non-adaptive methods such as Shampoo and Muon.
4. The paper does not provide a clear explanation of the implications of the low-rank bias for the performance of the algorithms.

### Questions

1. Can you provide a clear explanation of the low-rank bias of gradient descent on factored models?
2. Can you provide a clear explanation of the low-rank bias of adaptive methods such as Adam and RMSProp?
3. Can you provide a clear explanation of the low-rank bias of non-adaptive methods such as Shampoo and Muon?
4. Can you provide a clear explanation of the implications of the low-rank bias for the performance of the algorithms?

### Flag For Ethics Review

No ethics review needed.

### Rating

6: marginally above the acceptance threshold

### Confidence

3: You are fairly confident in your assessment. It is possible that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work. Math/other details were not carefully checked.

**********

## Reviewer

### Summary

The paper studies the implicit bias of various optimization algorithms on factored models. The authors show that the implicit bias of gradient descent on factored models is due to its gauge equivariance. They then show that Adam and other coordinate-wise methods do not have this property, which explains why they do not have the same implicit bias as gradient descent. They also show that shared-scalar preconditioners, such as Muon and Shampoo, do have this property. They then perform experiments on matrix sensing and transformer models to demonstrate the effect of this property on the implicit bias of the optimizers.

### Soundness

3 good

### Presentation

3 good

### Contribution

3 good

### Strengths

1. The paper is well-written and easy to follow. The authors provide a clear explanation of the low-rank bias of gradient descent and the absence of the low-rank bias in Adam and other adaptive methods. The authors also provide a clear explanation of the low-rank bias in non-adaptive methods such as Shampoo and Muon.
2. The paper provides a clear explanation of the low-rank bias of gradient descent and the absence of the low-rank bias in Adam and other adaptive methods. The authors also provide a clear explanation of the low-rank bias in non-adaptive methods such as Shampoo and Muon.
3. The paper provides a clear explanation of the low-rank bias of gradient descent and the absence of the low-rank bias in Adam and other adaptive methods. The authors also provide a clear explanation of the low-rank bias in non-adaptive methods such as Shampoo and Muon.

### Weaknesses

1. The paper only considers the low-rank bias of gradient descent on factored models. It would be interesting to see how the results generalize to other implicit biases, such as the implicit bias of gradient descent on overparameterized models.
2. The paper only considers the implicit bias of gradient descent on factored models. It would be interesting to see how the results generalize to other optimizers, such as stochastic gradient descent and momentum.
3. The paper only considers the implicit bias of gradient descent on factored models. It would be interesting to see how the results generalize to other optimization problems, such as least squares and logistic regression.
4. The paper only considers the implicit bias of gradient descent on factored models. It would be interesting to see how the results generalize to other neural network architectures, such as convolutional neural networks and recurrent neural networks.
5. The paper only considers the implicit bias of gradient descent on factored models. It would be interesting to see how the results generalize to other tasks, such as image classification and language modeling.

### Questions

1. Can the results be generalized to other implicit biases, such as the implicit bias of gradient descent on overparameterized models?
2. Can the results be generalized to other optimizers, such as stochastic gradient descent and momentum?
3. Can the results be generalized to other optimization problems, such as least squares and logistic regression?
4. Can the results be generalized to other neural network architectures, such as convolutional neural networks and recurrent neural networks?
5. Can the results be generalized to other tasks, such as image classification and language modeling?

### Flag For Ethics Review

No ethics review needed.

### Rating

6: marginally above the acceptance threshold

### Confidence

3: You are fairly confident in your assessment. It is possible that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work. Math/other details were not carefully checked.

**********

## Meta Review

This paper studies the implicit bias of various optimization algorithms on factored models. The authors show that the implicit bias of gradient descent on factored models is due to its gauge equivariance. They then show that Adam and other coordinate-wise methods do not have this property, which explains why they do not have the same implicit bias as gradient descent. They also show that shared-scalar preconditioners, such as Muon and Shampoo, do have this property. They then perform experiments on matrix sensing and transformer models to demonstrate the effect of this property on the implicit bias of the optimizers.

The reviewers are in agreement that this paper is well-written and easy to follow. The authors provide a clear explanation of the low-rank bias of gradient descent and the absence of the low-rank bias in Adam and other adaptive methods. The authors also provide a clear explanation of the low-rank bias in non-adaptive methods such as Shampoo and Muon. The paper provides a clear explanation of the low-rank bias of gradient descent and the absence of the low-rank bias in Adam and other adaptive methods. The authors also provide a clear explanation of the low-rank bias in non-adaptive methods such as Shampoo and Muon.

The reviewers also agree that the paper provides a clear explanation of the low-rank bias of gradient descent and the absence of the low-rank bias in Adam and other adaptive methods. The authors also provide a clear explanation of the low-rank bias in non-adaptive methods such as Shampoo and Muon. The paper provides a clear explanation of the low-rank bias of gradient descent and the absence of the low-rank bias in Adam and other adaptive methods. The authors also provide a clear explanation of the low-rank bias in non-adaptive methods such as Shampoo and Muon.

### justification_for_why_not_higher_score

N/A

### justification_for_why_not_lower_score

N/A

**********

## Paper Decision

Accept (poster)