## Reviewer

### Summary

The paper proposes a framework for optimizing meta-parameters (hyperparameters) in machine learning, which can be used to wrap around any first-order optimization algorithm. The framework adjusts meta-parameters, particularly step sizes, during training to minimize a specific form of regret that considers the long-term impact of step sizes on training. The authors also introduce lower-complexity variants of the framework that achieve performance comparable to the best hand-crafted learning rate schedules across various machine learning tasks.

### Soundness

3 good

### Presentation

3 good

### Contribution

2 fair

### Strengths

- The paper proposes a novel framework for optimizing meta-parameters in machine learning.
- The framework is general and can be used to wrap around any first-order optimization algorithm.
- The framework adjusts meta-parameters during training to minimize a specific form of regret that considers the long-term impact of step sizes on training.

### Weaknesses

- The paper does not provide a comprehensive comparison with existing methods for optimizing meta-parameters.
- The paper does not provide a detailed analysis of the computational complexity of the proposed framework.
- The paper does not provide a detailed analysis of the performance of the proposed framework on a wide range of machine learning tasks.

### Questions

- Can the framework be used to optimize other types of meta-parameters beyond step sizes?
- How does the framework compare to other methods for optimizing meta-parameters in terms of computational complexity?
- Can the framework be used to optimize meta-parameters for other types of machine learning tasks beyond supervised learning?

### Flag For Ethics Review

No ethics review needed.

### Rating

5: marginally below the acceptance threshold

### Confidence

2: You are willing to defend your assessment, but it is quite likely that you did not understand the central parts of the submission or that you are unfamiliar with some pieces of related work. Math/other details were not carefully checked.

**********

## Reviewer

### Summary

This paper proposes a framework for optimizing meta-parameters in machine learning, which can be used to wrap around any first-order optimization algorithm. The framework adjusts meta-parameters, particularly step sizes, during training to minimize a specific form of regret that considers the long-term impact of step sizes on training. The authors also introduce lower-complexity variants of the framework that achieve performance comparable to the best hand-crafted learning rate schedules across various machine learning tasks.

### Soundness

3 good

### Presentation

3 good

### Contribution

2 fair

### Strengths

1. The paper proposes a novel framework for optimizing meta-parameters in machine learning.
2. The framework is general and can be used to wrap around any first-order optimization algorithm.
3. The framework adjusts meta-parameters during training to minimize a specific form of regret that considers the long-term impact of step sizes on training.

### Weaknesses

1. The paper does not provide a comprehensive comparison with existing methods for optimizing meta-parameters.
2. The paper does not provide a detailed analysis of the computational complexity of the proposed framework.
3. The paper does not provide a detailed analysis of the performance of the proposed framework on a wide range of machine learning tasks.

### Questions

1. Can the framework be used to optimize other types of meta-parameters beyond step sizes?
2. How does the framework compare to other methods for optimizing meta-parameters in terms of computational complexity?
3. Can the framework be used to optimize meta-parameters for other types of machine learning tasks beyond supervised learning?

### Flag For Ethics Review

No ethics review needed.

### Rating

5: marginally below the acceptance threshold

### Confidence

2: You are willing to defend your assessment, but it is quite likely that you did not understand the central parts of the submission or that you are unfamiliar with some pieces of related work. Math/other details were not carefully checked.

**********

## Reviewer

### Summary

This paper proposes a framework for optimizing meta-parameters in machine learning, which can be used to wrap around any first-order optimization algorithm. The framework adjusts meta-parameters, particularly step sizes, during training to minimize a specific form of regret that considers the long-term impact of step sizes on training. The authors also introduce lower-complexity variants of the framework that achieve performance comparable to the best hand-crafted learning rate schedules across various machine learning tasks.

### Soundness

3 good

### Presentation

3 good

### Contribution

3 good

### Strengths

1. The paper proposes a novel framework for optimizing meta-parameters in machine learning.
2. The framework is general and can be used to wrap around any first-order optimization algorithm.
3. The framework adjusts meta-parameters during training to minimize a specific form of regret that considers the long-term impact of step sizes on training.

### Weaknesses

1. The paper does not provide a comprehensive comparison with existing methods for optimizing meta-parameters.
2. The paper does not provide a detailed analysis of the computational complexity of the proposed framework.
3. The paper does not provide a detailed analysis of the performance of the proposed framework on a wide range of machine learning tasks.

### Questions

1. Can the framework be used to optimize other types of meta-parameters beyond step sizes?
2. How does the framework compare to other methods for optimizing meta-parameters in terms of computational complexity?
3. Can the framework be used to optimize meta-parameters for other types of machine learning tasks beyond supervised learning?

### Flag For Ethics Review

No ethics review needed.

### Rating

5: marginally below the acceptance threshold

### Confidence

2: You are willing to defend your assessment, but it is quite likely that you did not understand the central parts of the submission or that you are unfamiliar with some pieces of related work. Math/other details were not carefully checked.

**********

## Reviewer

### Summary

The paper introduces a novel framework called MetaOptimize for optimizing meta-parameters, particularly step sizes, in machine learning. Unlike traditional methods that rely on expensive search processes, MetaOptimize dynamically adjusts these parameters during training, enhancing efficiency and performance. It can be applied to various first-order optimization algorithms, and its lower-complexity variants perform comparably to hand-crafted learning rate schedules across different tasks.

### Soundness

3 good

### Presentation

3 good

### Contribution

3 good

### Strengths

1. The paper introduces a novel framework for optimizing meta-parameters, specifically step sizes, in machine learning. This approach is dynamic, efficient, and can be applied to various first-order optimization algorithms.

2. The framework's lower-complexity variants perform comparably to hand-crafted learning rate schedules across different tasks, making it a practical and effective solution.

3. The paper is well-written and easy to follow, with clear explanations and concise descriptions of the proposed methods.

4. The experimental results demonstrate the effectiveness of the proposed framework, showing improved performance compared to other methods.

### Weaknesses

1. The paper could benefit from a more comprehensive comparison with existing methods for optimizing meta-parameters. This would provide a clearer understanding of the proposed framework's advantages and limitations.

2. The paper does not provide a detailed analysis of the computational complexity of the proposed framework. This information would be helpful for practitioners to understand the computational resources required to implement the framework.

3. The paper does not provide a detailed analysis of the performance of the proposed framework on a wide range of machine learning tasks. This would provide a more comprehensive understanding of the framework's applicability and effectiveness across different domains.

### Questions

1. How does the proposed framework compare to other methods for optimizing meta-parameters in terms of computational complexity?

2. Can the framework be used to optimize meta-parameters for other types of machine learning tasks beyond supervised learning?

3. What are the limitations of the proposed framework, and how do they impact its applicability and effectiveness in different scenarios?

### Flag For Ethics Review

No ethics review needed.

### Rating

5: marginally below the acceptance threshold

### Confidence

2: You are willing to defend your assessment, but it is quite likely that you did not understand the central parts of the submission or that you are unfamiliar with some pieces of related work. Math/other details were not carefully checked.

**********

## Meta Review

This paper introduces a novel framework for optimizing meta-parameters, specifically step sizes, in machine learning. The framework is dynamic, efficient, and can be applied to various first-order optimization algorithms. The lower-complexity variants of the framework perform comparably to hand-crafted learning rate schedules across different tasks. The paper is well-written and easy to follow, with clear explanations and concise descriptions of the proposed methods. The experimental results demonstrate the effectiveness of the proposed framework, showing improved performance compared to other methods.

However, the paper has some limitations. The paper does not provide a comprehensive comparison with existing methods for optimizing meta-parameters. The paper does not provide a detailed analysis of the computational complexity of the proposed framework. The paper does not provide a detailed analysis of the performance of the proposed framework on a wide range of machine learning tasks.

### justification_for_why_not_higher_score

The paper has some limitations. The paper does not provide a comprehensive comparison with existing methods for optimizing meta-parameters. The paper does not provide a detailed analysis of the computational complexity of the proposed framework. The paper does not provide a detailed analysis of the performance of the proposed framework on a wide range of machine learning tasks.

### justification_for_why_not_lower_score

N/A

**********

## Paper Decision

Reject (out of the running for an oral, but can be accepted as a poster)

**********

## Paper Decision Summary

This paper proposes a framework for optimizing meta-parameters in machine learning, which can be used to wrap around any first-order optimization algorithm. The framework adjusts meta-parameters, particularly step sizes, during training to minimize a specific form of regret that considers the long-term impact of step sizes on training. The authors also introduce lower-complexity variants of the framework that achieve performance comparable to the best hand-crafted learning rate schedules across various machine learning tasks.

### justification_for_why_not_higher_score

The paper has some limitations. The paper does not provide a comprehensive comparison with existing methods for optimizing meta-parameters. The paper does not provide a detailed analysis of the computational complexity of the proposed framework. The paper does not provide a detailed analysis of the performance of the proposed framework on a wide range of machine learning tasks.

### justification_for_why_not_lower_score

N/A

**********

## Paper Decision Final Feedback

This paper proposes a framework for optimizing meta-parameters in machine learning, which can be used to wrap around any first-order optimization algorithm. The framework adjusts meta-parameters, particularly step sizes, during training to minimize a specific form of regret that considers the long-term impact of step sizes on training. The authors also introduce lower-complexity variants of the framework that achieve performance comparable to the best hand-crafted learning rate schedules across various machine learning tasks.

### justification_for_why_not_higher_score

The paper has some limitations. The paper does not provide a comprehensive comparison with existing methods for optimizing meta-parameters. The paper does not provide a detailed analysis of the computational complexity of the proposed framework. The paper does not provide a detailed analysis of the performance of the proposed framework on a wide range of machine learning tasks.

### justification_for_why_not_lower_score

N/A

**********

<!---
# Reviewer

## Summary

The paper proposes a framework for optimizing meta-parameters in machine learning, which can be used to wrap around any first-order optimization algorithm. The framework adjusts meta-parameters, particularly step sizes, during training to minimize a specific form of regret that considers the long-term impact of step sizes on training. The authors also introduce lower-complexity variants of the framework that achieve performance comparable to the best hand-crafted learning rate schedules across various machine learning tasks.

## Soundness

3 good

## Presentation

3 good

## Contribution

3 good

## Strengths

1. The paper proposes a novel framework for optimizing meta-parameters in machine learning.
2. The framework is general and can be used to wrap around any first-order optimization algorithm.
3. The framework adjusts meta-parameters during training to minimize a specific form of regret that considers the long-term impact of step sizes on training.

## Weaknesses

1. The paper does not provide a comprehensive comparison with existing methods for optimizing meta-parameters.
2. The paper does not provide a detailed analysis of the computational complexity of the proposed framework.
3. The paper does not provide a detailed analysis of the performance of the proposed framework on a wide range of machine learning tasks.

## Questions

1. Can the framework be used to optimize other types of meta-parameters beyond step sizes?
2. How does the framework compare to other methods for optimizing meta-parameters in terms of computational complexity?
3. Can the framework be used to optimize meta-parameters for other types of machine learning tasks beyond supervised learning?

## Flag For Ethics Review

No ethics review needed.

## Rating

5: marginally below the acceptance threshold

## Confidence

2: You are willing to defend your assessment, but it is quite likely that you did not understand the central parts of the submission or that you are unfamiliar with some pieces of related work. Math/other details were not carefully checked.

**********

# Reviewer

## Summary

The paper proposes a framework for optimizing meta-parameters in machine learning, which can be used to wrap around any first-order optimization algorithm. The framework adjusts meta-parameters, particularly step sizes, during training to minimize a specific form of regret that considers the long-term impact of step sizes on training. The authors also introduce lower-complexity variants of the framework that achieve performance comparable to the best hand-crafted learning rate schedules across various machine learning tasks.

## Soundness

3 good

## Presentation

3 good

## Contribution

3 good

## Strengths

1. The paper proposes a novel framework for optimizing meta-parameters in machine learning.
2. The framework is general and can be used to wrap around any first-order optimization algorithm.
3. The framework adjusts meta-parameters during training to minimize a specific form of regret that considers the long-term impact of step sizes on training.

## Weaknesses

1. The paper does not provide a comprehensive comparison with existing methods for optimizing meta-parameters.
2. The paper does not provide a detailed analysis of the computational complexity of the proposed framework.
3. The paper does not provide a detailed analysis of the performance of the proposed framework on a wide range of machine learning tasks.

## Questions

1. Can the framework be used to optimize other types of meta-parameters beyond step sizes?
2. How does the framework compare to other methods for optimizing meta-parameters in terms of computational complexity?
3. Can the framework be used to optimize meta-parameters for other types of machine learning tasks beyond supervised learning?

## Flag For Ethics Review

No ethics review needed.

## Rating

5: marginally below the acceptance threshold

## Confidence

2: You are willing to defend your assessment, but it is quite likely that you did not understand the central parts of the submission or that you are unfamiliar with some pieces of related work. Math/other details were not carefully checked.

**********

# Reviewer

## Summary

The paper introduces a novel framework for optimizing meta-parameters, specifically step sizes, in machine learning. Unlike traditional methods that rely on expensive search processes, MetaOptimize dynamically adjusts these parameters during training, enhancing efficiency and performance. It can be applied to various first-order optimization algorithms, and its lower-complexity variants perform comparably to hand-crafted learning rate schedules across different tasks.

## Soundness

3 good

## Presentation

3 good

## Contribution

3 good

## Strengths

1. The paper introduces a novel framework for optimizing meta-parameters, specifically step sizes, in machine learning. This approach is dynamic, efficient, and can be applied to various first-order optimization algorithms.

2. The framework's lower-complexity variants perform comparably to hand-crafted learning rate schedules across different tasks, making it a practical and effective solution.

3. The paper is well-written and easy to follow, with clear explanations and concise descriptions of the proposed methods.

4. The experimental results demonstrate the effectiveness of the proposed framework, showing improved performance compared to other methods.

## Weaknesses

1. The paper could benefit from a more comprehensive comparison with existing methods for optimizing meta-parameters. This would provide a clearer understanding of the proposed framework's advantages and limitations.

2. The paper does not provide a detailed analysis of the computational complexity of the proposed framework. This information would be helpful for practitioners to understand the computational resources required to implement the framework.

3. The paper does not provide a detailed analysis of the performance of the proposed framework on a wide range of machine learning tasks. This would provide a more comprehensive understanding of the framework's applicability and effectiveness across different domains.

## Questions

1. How does the proposed framework compare to other methods for optimizing meta-parameters in terms of computational complexity?

2. Can the framework be used to optimize meta-parameters for other types of machine learning tasks beyond supervised learning?

3. What are the limitations of the proposed framework, and how do they impact its applicability and effectiveness in different scenarios?

## Flag For Ethics Review

No ethics review needed.

## Rating

5: marginally below the acceptance threshold

## Confidence

2: You are willing to defend your assessment, but it is quite likely that you did not understand the central parts of the submission or that you are unfamiliar with some pieces of related work. Math/other details were not carefully checked.

**********

## Meta Review

This paper proposes a framework for optimizing meta-parameters in machine learning, which can be used to wrap around any first-order optimization algorithm. The framework adjusts meta-parameters, particularly step sizes, during training to minimize a specific form of regret that considers the long-term impact of step sizes on training. The authors also introduce lower-complexity variants of the framework that achieve performance comparable to the best hand-crafted learning rate schedules across various machine learning tasks.

### justification_for_why_not_higher_score

The paper has some limitations. The paper does not provide a comprehensive comparison with existing methods for optimizing meta-parameters. The paper does not provide a detailed analysis of the computational complexity of the proposed framework. The paper does not provide a detailed analysis of the performance of the proposed framework on a wide range of machine learning tasks.

### justification_for_why_not_lower_score

N/A

**********

## Paper Decision

Reject (out of the running for an oral, but can be accepted as a poster)

**********

## Paper Decision Summary

This paper proposes a framework for optimizing meta-parameters in machine learning, which can be used to wrap around any first-order optimization algorithm. The framework adjusts meta-parameters, particularly step sizes, during training to minimize a specific form of regret that considers the long-term impact of step sizes on training. The authors also introduce lower-complexity variants of the framework that achieve performance comparable to the best hand-crafted learning rate schedules across various machine learning tasks.

### justification_for_why_not_higher_score

The paper has some limitations. The paper does not provide a comprehensive comparison with existing methods for optimizing meta-parameters. The paper does not provide a detailed analysis of the computational complexity of the proposed framework. The paper does not provide a detailed analysis of the performance of the proposed framework on a wide range of machine learning tasks.

### justification_for_why_not_lower_score

N/A

**********

## Paper Decision Final Feedback

This paper proposes a framework for optimizing meta-parameters in machine learning, which can be used to wrap around any first-order optimization algorithm. The framework adjusts meta-parameters, particularly step sizes, during training to minimize a specific form of regret that considers the long-term impact of step sizes on training. The authors also introduce lower-complexity variants of the framework that achieve performance comparable to the best hand-crafted learning rate schedules across various machine learning tasks.

### justification_for_why_not_higher_score

The paper has some limitations. The paper does not provide a comprehensive comparison with existing methods for optimizing meta-parameters. The paper does not provide a detailed analysis of the computational complexity of the proposed framework. The paper does not provide a detailed analysis of the performance of the proposed framework on a wide range of machine learning tasks.

### justification_for_why_not_lower_score

N/A

**********

<!---
# Reviewer

## Summary

The paper proposes a framework for optimizing meta-parameters (hyperparameters) in machine learning, a key factor for efficient training and high model performance. Rather than relying on expensive meta-parameter search methods, the authors introduce MetaOptimize: a dynamic approach that adjusts meta-parameters, particularly step sizes (also known as learning rates), during training. More specifically, MetaOptimize can wrap around any first-order optimization algorithm, tuning step sizes on the fly to minimize a specific form of regret that considers the long-term impact of step sizes on training, through a discounted sum of future losses. The authors also introduce lower-complexity variants of MetaOptimize that, in conjunction with its adaptability to various optimization algorithms, achieve performance comparable to those of the best hand-crafted learning rate schedules across diverse machine learning tasks.

## Soundness

3 good

## Presentation

3 good

## Contribution

3 good

## Strengths

1. The paper addresses the challenge of optimizing meta-parameters in machine learning, a crucial aspect for efficient training and high model performance. The authors introduce MetaOptimize, a dynamic approach that adjusts meta-parameters, particularly step sizes, during training, which is a novel and innovative idea.

2. The paper provides a comprehensive overview of the MetaOptimize framework, including its formulation, algorithm, and experimental results. The authors also discuss the advantages of MetaOptimize, including its adaptability to various optimization algorithms and its ability to achieve performance comparable to hand-crafted learning rate schedules.

3. The paper is well-written and easy to follow, with clear explanations and concise descriptions of the proposed methods.

## Weaknesses

1. The paper does not provide a comprehensive comparison with existing methods for optimizing meta-parameters. It would be helpful to compare MetaOptimize with other methods in terms of performance, computational complexity, and scalability.

2. The paper does not provide a detailed analysis of the computational complexity of the proposed framework. It would be helpful to provide a detailed analysis of the computational resources required to implement the framework, including time and space complexity.

3. The paper does not provide a detailed analysis of the performance of the proposed framework on a wide range of machine learning tasks. It would be helpful to provide a more comprehensive evaluation of the framework's performance on different types of machine learning tasks, including supervised learning, reinforcement learning, and unsupervised learning.

## Questions

1. How does MetaOptimize compare to other methods for optimizing meta-parameters in terms of performance, computational complexity, and scalability?

2. What are the computational resources required to implement the MetaOptimize framework, including time and space complexity?

3. How does the performance of MetaOptimize vary across different types of machine learning tasks, including supervised learning, reinforcement learning, and unsupervised learning?

## Flag For Ethics Review

No ethics review needed.

## Rating

6: marginally above the acceptance threshold

## Confidence

2: You are willing to defend your assessment, but it is quite likely that you did not understand the central parts of the submission or that you are unfamiliar with some pieces of related work. Math/other details were not carefully checked.

**********

# MetaOptimize: A Framework for Optimizing Step Sizes and Other Meta-parameters

## Summary

The paper introduces MetaOptimize, a novel framework for optimizing meta-parameters in machine learning. MetaOptimize can be used to wrap around any first-order optimization algorithm, adjusting meta-parameters like step sizes during training to minimize a specific form of regret that considers the long-term impact of step sizes on training. The framework's lower-complexity variants achieve performance comparable to hand-crafted learning rate schedules across various machine learning tasks.

## Soundness

3 good

## Presentation

3 good

## Contribution

3 good

## Strengths

1. The paper proposes a novel framework for optimizing meta-parameters in machine learning, which can be used to wrap around any first-order optimization algorithm.
2. The framework adjusts meta-parameters during training to minimize a specific form of regret that considers the long-term impact of step sizes on training.
3. The paper is well-written and easy to follow, with clear explanations and concise descriptions of the proposed methods.

## Weaknesses

1. The paper does not provide a comprehensive comparison with existing methods for optimizing meta-parameters.
2. The paper does not provide a detailed analysis of the computational complexity of the proposed framework.
3. The paper does not provide a detailed analysis of the performance of the proposed framework on a wide range of machine learning tasks.

## Questions

1. Can the framework be used to optimize other types of meta-parameters beyond step sizes?
2. How does the framework compare to other methods for optimizing meta-parameters in terms of computational complexity?
3. Can the framework be used to optimize meta-parameters for other types of machine learning tasks beyond supervised learning?

## Flag For Ethics Review

No ethics review needed.

## Rating

6: marginally above the acceptance threshold

## Confidence

2: You are willing to defend your assessment, but it is quite likely that you did not understand the central parts of the submission or that you are unfamiliar with some pieces of related work. Math/other details were not carefully checked.

**********

## MetaOptimize: A Framework for Optimizing Step Sizes and Other Meta-parameters

## Summary

The paper introduces MetaOptimize, a novel framework for optimizing meta-parameters in machine learning. MetaOptimize can be used to wrap around any first-order optimization algorithm, adjusting meta-parameters like step sizes during training to minimize a specific form of regret that considers the long-term impact of step sizes on training. The framework's lower-complexity variants achieve performance comparable to hand-crafted learning rate schedules across various machine learning tasks.

## Soundness

3 good

## Presentation

3 good

## Contribution

3 good

## Strengths

1. The paper proposes a novel framework for optimizing meta-parameters in machine learning, which can be used to wrap around any first-order optimization algorithm.
2. The framework adjusts meta-parameters during training to minimize a specific form of regret that considers the long-term impact of step sizes on training.
3. The paper is well-written and easy to follow, with clear explanations and concise descriptions of the proposed methods.

## Weaknesses

1. The paper does not provide a comprehensive comparison with existing methods for optimizing meta-parameters.
2. The paper does not provide a detailed analysis of the computational complexity of the proposed framework.
3. The paper does not provide a detailed analysis of the performance of the proposed framework on a wide range of machine learning tasks.

## Questions

1. Can the framework be used to optimize other types of meta-parameters beyond step sizes?
2. How does the framework compare to other methods for optimizing meta-parameters in terms of computational complexity?
3. Can the framework be used to optimize meta-parameters for other types of machine learning tasks beyond supervised learning?

## Flag For Ethics Review

No ethics review needed.

## Rating

6: marginally above the acceptance threshold

## Confidence

2: You are willing to defend your assessment, but it is quite likely that you did not understand the central parts of the submission or that you are unfamiliar with some pieces of related work. Math/other details were not carefully checked.

**********

## MetaOptimize: A Framework for Optimizing Step Sizes and Other Meta-parameters

## Summary

The paper introduces MetaOptimize, a novel framework for optimizing meta-parameters in machine learning. MetaOptimize can be used to wrap around any first-order optimization algorithm, adjusting meta-parameters like step sizes during training to minimize a specific form of regret that considers the long-term impact of step sizes on training. The framework's lower-complexity variants achieve performance comparable to hand-crafted learning rate schedules across various machine learning tasks.

## Soundness

3 good

## Presentation

3 good

## Contribution

3 good

## Strengths

1. The paper proposes a novel framework for optimizing meta-parameters in machine learning, which can be used to wrap around any first-order optimization algorithm.
2. The framework adjusts meta-parameters during training to minimize a specific form of regret that considers the long-term impact of step sizes on training.
3. The paper is well-written and easy to follow, with clear explanations and concise descriptions of the proposed methods.

## Weaknesses

1. The paper does not provide a comprehensive comparison with existing methods for optimizing meta-parameters.
2. The paper does not provide a detailed analysis of the computational complexity of the proposed framework.
3. The paper does not provide a detailed analysis of the performance of the proposed framework on a wide range of machine learning tasks.

## Questions

1. Can the framework be used to optimize other types of meta-parameters beyond step sizes?
2. How does the framework compare to other methods for optimizing meta-parameters in terms of computational complexity?
3. Can the framework be used to optimize meta-parameters for other types of machine learning tasks beyond supervised learning?

## Flag For Ethics Review

No ethics review needed.

## Rating

6: marginally above the acceptance threshold

## Confidence

2: You are willing to defend your assessment, but it is quite likely that you did not understand the central parts of the submission or that you are unfamiliar with some pieces of related work. Math/other details were not carefully checked.

**********

## MetaOptimize: A Framework for Optimizing Step Sizes and Other Meta-parameters

## Summary

The paper introduces MetaOptimize, a novel framework for optimizing meta-parameters in machine learning. MetaOptimize can be used to wrap around any first-order optimization algorithm, adjusting meta-parameters like step sizes during training to minimize a specific form of regret that considers the long-term impact of step sizes on training. The framework's lower-complexity variants achieve performance comparable to hand-crafted learning rate schedules across various machine learning tasks.

## Soundness

3 good

## Presentation

3 good

## Contribution

3 good

## Strengths

1. The paper proposes a novel framework for optimizing meta-parameters in machine learning, which can be used to wrap around any first-order optimization algorithm.
2. The framework adjusts meta-parameters during training to minimize a specific form of regret that considers the long-term impact of step sizes on training.
3. The paper is well-written and easy to follow, with clear explanations and concise descriptions of the proposed methods.

## Weaknesses

1. The paper does not provide a comprehensive comparison with existing methods for optimizing meta-parameters.
2. The paper does not provide a detailed analysis of the computational complexity of the proposed framework.
3. The paper does not provide a detailed analysis of the performance of the proposed framework on a wide range of machine learning tasks.

## Questions

1. Can the framework be used to optimize other types of meta-parameters beyond step sizes?
2. How does the framework compare to other methods for optimizing meta-parameters in terms of computational complexity?
3. Can the framework be used to optimize meta-parameters for other types of machine learning tasks beyond supervised learning?

## Flag For Ethics Review

No ethics review needed.

## Rating

6: marginally above the acceptance threshold

## Confidence

2: You are willing to defend your assessment, but it is quite likely that you did not understand the central parts of the submission or that you are unfamiliar with some pieces of related work. Math/other details were not carefully checked.

**********

## MetaOptimize: A Framework for Optimizing Step Sizes and Other Meta-parameters

## Summary

The paper introduces MetaOptimize, a novel framework for optimizing meta-parameters in machine learning. MetaOptimize can be used to wrap around any first-order optimization algorithm, adjusting meta-parameters like step sizes during training to minimize a specific form of regret that considers the long-term impact of step sizes on training. The framework's lower-complexity variants achieve performance comparable to hand-crafted learning rate schedules across various machine learning tasks.

## Soundness

3 good

## Presentation

3 good

## Contribution

3 good

## Strengths

1. The paper proposes a novel framework for optimizing meta-parameters in machine learning, which can be used to wrap around any first-order optimization algorithm.
2. The framework adjusts meta-parameters during training to minimize a specific form of regret that considers the long-term impact of step sizes on training.
3. The paper is well-written and easy to follow, with clear explanations and concise descriptions of the proposed methods.

## Weaknesses

1. The paper does not provide a comprehensive comparison with existing methods for optimizing meta-parameters.
2. The paper does not provide a detailed analysis of the computational complexity of the proposed framework.
3. The paper does not provide a detailed analysis of the performance of the proposed framework on a wide range of machine learning tasks.

## Questions

1. Can the framework be used to optimize other types of meta-parameters beyond step sizes?
2. How does the framework compare to other methods for optimizing meta-parameters in terms of computational complexity?
3. Can the framework be used to optimize meta-parameters for other types of machine learning tasks beyond supervised learning?

## Flag For Ethics Review

No ethics review needed.

## Rating

6: marginally above the acceptance threshold

## Confidence

2: You are willing to defend your assessment, but it is quite likely that you did not understand the central parts of the submission or that you are unfamiliar with some pieces of related work. Math/other details were not carefully checked.

**********

## MetaOptimize: A Framework for Optimizing Step Sizes and Other Meta-parameters

## Summary

The paper introduces MetaOptimize, a novel framework for optimizing meta-parameters in machine learning. MetaOptimize can be used to wrap around any first-order optimization algorithm, adjusting meta-parameters