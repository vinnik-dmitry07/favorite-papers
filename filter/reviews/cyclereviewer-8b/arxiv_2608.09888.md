## Reviewer

### Summary

The paper introduces a novel approach to in-context learning that combines it with recurrent latent reasoning. The authors propose a model architecture, BDH-CQ, which uses recurrent memory to update its internal state based on input demonstrations and then performs iterative computation in a high-dimensional latent space to solve a query. The model is evaluated on the ARC-AGI-1 evaluation set and shows improved cost-efficiency compared to previous state-of-the-art models.

### Soundness

3 good

### Presentation

3 good

### Contribution

2 fair

### Strengths

The paper presents a novel approach to in-context learning that combines it with recurrent latent reasoning. The authors provide a detailed description of the model architecture and its training procedure. The evaluation on the ARC-AGI-1 evaluation set shows improved cost-efficiency compared to previous state-of-the-art models.

### Weaknesses

1. The paper lacks a detailed description of the model architecture and its training procedure. The authors only provide a high-level overview of the model and its components, without providing specific details on how it is trained or how the recurrent memory is updated. This makes it difficult to understand the specific design choices and how they contribute to the model's performance.

2. The paper does not provide a detailed analysis of the model's performance on different types of tasks. The evaluation is limited to a single dataset, and the authors do not provide a detailed breakdown of the model's performance on different types of tasks or how it compares to other models on the same dataset. This makes it difficult to understand the model's strengths and weaknesses and how it compares to other models.

3. The paper does not provide a detailed discussion of the limitations of the proposed approach. The authors do not discuss potential limitations or challenges associated with the model architecture or training procedure, or how they plan to address them in future work. This makes it difficult to understand the potential applications and limitations of the proposed approach.

### Questions

1. How does the proposed approach compare to other approaches to in-context learning? The authors should provide a detailed comparison to other approaches and discuss the advantages and disadvantages of their approach.

2. How does the model's performance vary across different types of tasks? The authors should provide a detailed analysis of the model's performance on different types of tasks and how it compares to other models on the same dataset.

3. What are the limitations of the proposed approach? The authors should discuss potential limitations or challenges associated with the model architecture or training procedure and how they plan to address them in future work.

### Flag For Ethics Review

No ethics review needed.

### Rating

5: marginally below the acceptance threshold

### Confidence

2: You are willing to defend your assessment, but it is quite likely that you did not understand the central parts of the submission or that you are unfamiliar with some pieces of related work. Math/other details were not carefully checked.

**********

## Reviewer

### Summary

This paper proposes a new reasoning model, BDH-CQ, which combines in-context learning with recurrent latent reasoning. The model is evaluated on the ARC-AGI-1 evaluation set and achieves a new state-of-the-art cost-accuracy tradeoff. The paper also presents a controlled analysis of the model's behavior, including its ability to learn from demonstrations, apply transformations consistently, and handle complex concepts.

### Soundness

2 fair

### Presentation

2 fair

### Contribution

2 fair

### Strengths

- The paper introduces a novel approach to combining in-context learning with recurrent latent reasoning, which is an interesting and promising direction for future research.
- The paper presents a thorough evaluation of the model's behavior on the ARC-AGI-1 evaluation set, including its ability to learn from demonstrations and apply transformations consistently.
- The paper provides a detailed analysis of the model's performance on different types of tasks, including boundary propagation, copying, ordering, and nesting.

### Weaknesses

- The paper does not provide a clear explanation of how the model's performance is measured and evaluated. It would be helpful to have a more detailed description of the evaluation methodology and metrics used.
- The paper does not provide a clear comparison of the model's performance to other state-of-the-art models on the ARC-AGI-1 evaluation set. It would be helpful to have a more detailed comparison of the model's performance to other models, including their accuracy and cost-efficiency.
- The paper does not provide a clear explanation of how the model's recurrent latent reasoning mechanism works and how it is implemented in the model architecture. It would be helpful to have a more detailed description of the model architecture and how the recurrent latent reasoning mechanism is implemented.
- The paper does not provide a clear explanation of the limitations of the model and how they can be addressed in future work. It would be helpful to have a more detailed discussion of the limitations of the model and potential future directions for research.

### Questions

- How does the model's performance compare to other state-of-the-art models on the ARC-AGI-1 evaluation set?
- How does the model's recurrent latent reasoning mechanism work and how is it implemented in the model architecture?
- What are the limitations of the model and how can they be addressed in future work?

### Flag For Ethics Review

No ethics review needed.

### Rating

5: marginally below the acceptance threshold

### Confidence

2: You are willing to defend your assessment, but it is quite likely that you did not understand the central parts of the submission or that you are unfamiliar with some pieces of related work. Math/other details were not carefully checked.

**********

## Reviewer

### Summary

This paper introduces BDH-CQ, a reasoning model that combines in-context learning with recurrent latent reasoning. The model's recurrent memory is updated by the input demonstrations, and it then solves a query through iterative computation in a high-dimensional latent space. The model is evaluated on the ARC-AGI-1 evaluation set, and it reaches 29.5% pass@2 at a computed inference cost of $0.0007 per task, breaking through the previously reported cost-accuracy Pareto frontier.

### Soundness

2 fair

### Presentation

2 fair

### Contribution

2 fair

### Strengths

1. The paper is well-written and easy to follow.

2. The proposed model achieves state-of-the-art performance on the ARC-AGI-1 evaluation set.

### Weaknesses

1. The paper lacks a detailed description of the model architecture and its training procedure. It is not clear how the model's recurrent memory is updated by the input demonstrations and how the iterative computation in the latent space is performed.

2. The paper only evaluates the model on the ARC-AGI-1 evaluation set, which may not be sufficient to demonstrate the model's generalization ability.

3. The paper does not provide a detailed analysis of the model's performance on different types of tasks. It would be helpful to have a more detailed breakdown of the model's performance on different types of tasks and how it compares to other models on the same dataset.

### Questions

1. Could the authors provide a more detailed description of the model architecture and its training procedure?

2. Could the authors provide more evaluation results on other datasets to demonstrate the model's generalization ability?

3. Could the authors provide a more detailed analysis of the model's performance on different types of tasks?

### Flag For Ethics Review

No ethics review needed.

### Rating

5: marginally below the acceptance threshold

### Confidence

3: You are fairly confident in your assessment. It is possible that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work. Math/other details were not carefully checked.

**********

## Reviewer

### Summary

This paper introduces a new model architecture, BDH-CQ, which combines in-context learning with recurrent latent reasoning. The model is trained on a large dataset of ARC-style tasks and achieves state-of-the-art performance on the ARC-AGI-1 evaluation set. The paper also presents a controlled analysis of the model's behavior on a range of tasks, including boundary propagation, copying, ordering, and nesting.

### Soundness

3 good

### Presentation

3 good

### Contribution

3 good

### Strengths

The paper is well-written and easy to follow. The authors provide a clear description of the model architecture and training procedure, as well as the evaluation methodology and results. The paper also presents a thorough analysis of the model's behavior on a range of tasks, which provides valuable insights into the model's capabilities and limitations.

The paper introduces a new model architecture, BDH-CQ, which combines in-context learning with recurrent latent reasoning. This is an interesting and novel approach that has not been explored in previous work. The paper also presents a thorough evaluation of the model's performance on a range of tasks, which demonstrates its effectiveness.

The paper also presents a controlled analysis of the model's behavior on a range of tasks, including boundary propagation, copying, ordering, and nesting. This analysis provides valuable insights into the model's capabilities and limitations, and helps to understand how the model is able to perform well on certain tasks and struggle on others.

### Weaknesses

The paper only evaluates the model on a single dataset, the ARC-AGI-1 evaluation set. It would be interesting to see how the model performs on other datasets, such as the ARC-AGI-2 evaluation set or other visual reasoning benchmarks.

The paper only presents a single model architecture, BDH-CQ. It would be interesting to see how other model architectures perform on the same tasks and datasets.

The paper only presents a single evaluation metric, pass@2. It would be interesting to see how the model performs on other metrics, such as pass@1 or test-pair accuracy.

### Questions

What is the relationship between the model's performance and the size of the latent space? How does the model's performance change as the size of the latent space increases or decreases?

How does the model's performance change as the number of demonstrations increases or decreases? Does the model require a minimum number of demonstrations to learn a new task?

How does the model's performance change as the complexity of the tasks increases? Does the model struggle with more complex tasks or does it perform equally well on all tasks?

### Flag For Ethics Review

No ethics review needed.

### Rating

6: marginally above the acceptance threshold

### Confidence

3: You are fairly confident in your assessment. It is possible that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work. Math/other details were not carefully checked.

**********

## Meta Review

This paper proposes a novel approach to in-context learning that combines it with recurrent latent reasoning. The model is evaluated on the ARC-AGI-1 evaluation set and shows improved cost-efficiency compared to previous state-of-the-art models. However, the reviewers raised several concerns about the paper, including the lack of clarity in the description of the model architecture and training procedure, the limited evaluation on a single dataset, and the lack of comparison to other state-of-the-art models. The authors provided some clarification and additional results, but the reviewers still have concerns about the paper. The paper is borderline and the AC recommends rejection.

### justification_for_why_not_higher_score

The reviewers raised several concerns about the paper, including the lack of clarity in the description of the model architecture and training procedure, the limited evaluation on a single dataset, and the lack of comparison to other state-of-the-art models.

### justification_for_why_not_lower_score

N/A

**********

## Paper Decision

Reject (not selected for publication)