## Reviewer

### Summary

This paper studies the connection between gradient descent and neuroevolution. The authors show that in the limit of small mutation size, neuroevolution is equivalent to gradient descent on the loss function with Gaussian white noise.

### Soundness

3 good

### Presentation

3 good

### Contribution

3 good

### Strengths

The paper is well-written and easy to follow. The authors provide a detailed theoretical analysis of the connection between gradient descent and neuroevolution.

### Weaknesses

The paper is missing some important references. For example, there is a line of work studying the connection between gradient descent and evolutionary algorithms, such as [1,2,3]. The authors should discuss the relationship between their work and these previous works.

[1] Li, Ji, et al. "A second-order gradient method for composition optimization. " Advances in Neural Information Processing Systems 29 (2016): 3498-3506.

[2] Li, Ji, et al. "Evolutionary optimization in function composition space. " Advances in neural information processing systems 30 (2017).

[3] Li, Ji, et al. "Evolutionary optimization in function composition space." Advances in Neural Information Processing Systems 30 (2017).

### Questions

The authors should discuss the relationship between their work and previous works that study the connection between gradient descent and evolutionary algorithms.

### Flag For Ethics Review

No ethics review needed.

### Rating

6: marginally above the acceptance threshold

### Confidence

3: You are fairly confident in your assessment. It is possible that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work. Math/other details were not carefully checked.

**********

## Reviewer

### Summary

The paper establishes a correspondence between gradient descent and neuroevolution, showing that the former is equivalent to the latter in the limit of small mutation size. The authors show that this correspondence can be observed numerically for finite mutations and finite integration steps.

### Soundness

3 good

### Presentation

3 good

### Contribution

3 good

### Strengths

The paper is well-written and easy to follow. The authors provide a detailed theoretical analysis of the connection between gradient descent and neuroevolution, and show that the correspondence can be observed numerically for finite mutations and finite integration steps.

### Weaknesses

The paper only considers a simple form of neuroevolution, where the mutation is a Gaussian random number. It would be interesting to see if the correspondence still holds for more complex forms of neuroevolution, such as those that use non-Gaussian mutations or have a non-uniform mutation rate.

### Questions

See weaknesses.

### Flag For Ethics Review

No ethics review needed.

### Rating

6: marginally above the acceptance threshold

### Confidence

3: You are fairly confident in your assessment. It is possible that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work. Math/other details were not carefully checked.

**********

## Reviewer

### Summary

This paper shows that training a neural network by conditioned stochastic mutation or neuroevolution of its weights is equivalent, in the limit of small mutations, to gradient descent on the loss function in the presence of Gaussian white noise. Averaged over independent realizations of the learning process, neuroevolution is equivalent to gradient descent on the loss function. The paper also shows that this correspondence can be observed for finite mutations, for shallow and deep neural networks.

### Soundness

3 good

### Presentation

3 good

### Contribution

3 good

### Strengths

This paper is well-written and easy to follow. The authors provide a detailed theoretical analysis of the connection between gradient descent and neuroevolution, and show that the correspondence can be observed numerically for finite mutations and finite integration steps.

### Weaknesses

The authors should consider the computational complexity of the neuroevolution algorithm. In particular, the authors should discuss the number of iterations required to achieve convergence and the computational cost of each iteration.

### Questions

The authors should consider the computational complexity of the neuroevolution algorithm. In particular, the authors should discuss the number of iterations required to achieve convergence and the computational cost of each iteration.

### Flag For Ethics Review

No ethics review needed.

### Rating

6: marginally above the acceptance threshold

### Confidence

3: You are fairly confident in your assessment. It is possible that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work. Math/other details were not carefully checked.

**********

## Reviewer

### Summary

The authors show that neuroevolution and gradient descent are equivalent in the limit of small mutation size. They also show that this correspondence can be observed numerically for finite mutations and finite integration steps.

### Soundness

3 good

### Presentation

3 good

### Contribution

3 good

### Strengths

The paper is well-written and easy to follow. The authors provide a detailed theoretical analysis of the connection between gradient descent and neuroevolution, and show that the correspondence can be observed numerically for finite mutations and finite integration steps.

### Weaknesses

The authors should consider the computational complexity of the neuroevolution algorithm. In particular, the authors should discuss the number of iterations required to achieve convergence and the computational cost of each iteration.

### Questions

The authors should consider the computational complexity of the neuroevolution algorithm. In particular, the authors should discuss the number of iterations required to achieve convergence and the computational cost of each iteration.

### Flag For Ethics Review

No ethics review needed.

### Rating

6: marginally above the acceptance threshold

### Confidence

3: You are fairly confident in your assessment. It is possible that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work. Math/other details were not carefully checked.

**********

## Meta Review

This paper establishes a correspondence between gradient descent and neuroevolution. The authors show that the former is equivalent to the latter in the limit of small mutation size. The authors show that this correspondence can be observed numerically for finite mutations and finite integration steps. The paper is well-written and easy to follow. The authors provide a detailed theoretical analysis of the connection between gradient descent and neuroevolution, and show that the correspondence can be observed numerically for finite mutations and finite integration steps. The paper is interesting and important.

### justification_for_why_not_higher_score

The paper is interesting and important.

### justification_for_why_not_lower_score

The paper is interesting and important.

**********

## Paper Decision

Accept (poster)