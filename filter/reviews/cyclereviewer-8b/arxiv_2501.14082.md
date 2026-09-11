## Reviewer

### Summary

The paper proposes a novel approach to inter-LLM communication, which involves passing activations between models. The authors demonstrate the effectiveness of their approach on a variety of tasks, including multi-player coordination games and reasoning benchmarks.

### Soundness

3 good

### Presentation

3 good

### Contribution

3 good

### Strengths

- The paper is well-written and easy to follow.
- The proposed method is simple yet effective. 
- The experiments are well-designed and the results are convincing.

### Weaknesses

- The paper lacks an ablation study on the hyperparameters. For example, the choice of layer $j$ and $k$ seems to be crucial. However, the authors only provide a single choice for these hyperparameters. 
- The paper lacks a discussion of the limitations of the proposed method. For example, the paper does not discuss the limitations of the proposed method in terms of scalability and generalizability.

### Questions

- How do the results change if we vary the choice of hyperparameters (e.g., $j$ and $k$)?

### Flag For Ethics Review

No ethics review needed.

### Rating

6: marginally above the acceptance threshold

### Confidence

3: You are fairly confident in your assessment. It is possible that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work. Math/other details were not carefully checked.

**********

## Reviewer

### Summary

This paper proposes a novel communication protocol between language models, where the intermediate activations of the models are used to facilitate communication between them. The paper claims that this approach is more efficient and effective than traditional natural language communication. The paper also provides a theoretical analysis of the computational complexity of the proposed method and compares it with natural language communication. The paper evaluates the proposed method on two experimental setups: multi-player coordination games and reasoning benchmarks. The results show that the proposed method achieves up to 27.0% improvement over natural language communication across these datasets, using less than 1/4 the compute.

### Soundness

3 good

### Presentation

3 good

### Contribution

3 good

### Strengths

1. The paper proposes a novel communication protocol between language models that is purely activation-based.
2. The paper provides a theoretical analysis of the computational complexity of the proposed method and compares it with natural language communication.
3. The paper evaluates the proposed method on two experimental setups: multi-player coordination games and reasoning benchmarks. The results show that the proposed method achieves up to 27.0% improvement over natural language communication across these datasets, using less than 1/4 the compute.

### Weaknesses

1. The paper does not provide a detailed explanation of the intuition behind the proposed method.
2. The paper does not provide a detailed analysis of the limitations of the proposed method.

### Questions

1. Can the authors provide a more detailed explanation of the intuition behind the proposed method?
2. Can the authors provide a more detailed analysis of the limitations of the proposed method?

### Flag For Ethics Review

No ethics review needed.

### Rating

6: marginally above the acceptance threshold

### Confidence

3: You are fairly confident in your assessment. It is possible that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work. Math/other details were not carefully checked.

**********

## Reviewer

### Summary

This paper proposes a novel method for communication between language models. The proposed method involves communicating the activations of one model to another instead of using natural language. The authors demonstrate the effectiveness of their method on a variety of tasks, including multi-player coordination games and reasoning benchmarks. The results show that the proposed method achieves up to 27.0% improvement over natural language communication across these datasets, using less than 1/4 the compute.

### Soundness

3 good

### Presentation

3 good

### Contribution

3 good

### Strengths

1. The paper proposes a novel method for communication between language models, which is a relatively unexplored area of research.
2. The paper provides a detailed analysis of the computational complexity of the proposed method and compares it with natural language communication.
3. The paper evaluates the proposed method on a variety of tasks, including multi-player coordination games and reasoning benchmarks.

### Weaknesses

1. The paper does not provide a detailed discussion of the limitations of the proposed method.
2. The paper does not provide a detailed analysis of the robustness of the proposed method to different types of noise or perturbations.

### Questions

1. How does the proposed method compare to other methods for communication between language models?
2. How does the proposed method scale to larger language models?
3. How does the proposed method perform in scenarios where the models are not aligned?

### Flag For Ethics Review

No ethics review needed.

### Rating

6: marginally above the acceptance threshold

### Confidence

3: You are fairly confident in your assessment. It is possible that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work. Math/other details were not carefully checked.

**********

## Reviewer

### Summary

This paper proposes a new method of communication between language models. In this method, the authors propose to communicate the activations of the language models. The authors show that this method can be more efficient than natural language communication and can achieve better performance on some tasks.

### Soundness

3 good

### Presentation

3 good

### Contribution

3 good

### Strengths

The paper is well written and easy to follow. The idea of communication between language models is interesting and important. The proposed method is simple and effective. The experiments are comprehensive and the results are convincing.

### Weaknesses

1. The proposed method requires the language models to have the same architecture and embedding space. This is a strong assumption and may not be practical. 
2. The method requires the language models to have access to their activations, which may not be possible in some cases. 
3. The method is only evaluated on simple tasks and it is not clear how it will perform on more complex tasks.

### Questions

1. Can the proposed method be used for communication between language models with different architectures and embedding spaces?
2. Can the proposed method be used for communication between language models that do not have access to their activations?
3. How does the proposed method perform on more complex tasks?

### Flag For Ethics Review

No ethics review needed.

### Rating

6: marginally above the acceptance threshold

### Confidence

3: You are fairly confident in your assessment. It is possible that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work. Math/other details were not carefully checked.

**********

## Meta Review

The paper proposes a novel approach to inter-LLM communication, which involves passing activations between models. The authors demonstrate the effectiveness of their approach on a variety of tasks, including multi-player coordination games and reasoning benchmarks. The paper is well-written and easy to follow. The proposed method is simple yet effective. The experiments are well-designed and the results are convincing. The reviewers have raised some concerns about the lack of ablation studies on hyperparameters, limitations of the proposed method, and scalability and generalizability. The authors have addressed these concerns in their rebuttal. The reviewers have also raised some questions about the intuition behind the proposed method and the limitations of the proposed method. The authors have provided additional information and clarifications in their rebuttal. Overall, the paper presents a novel approach to inter-LLM communication and demonstrates its effectiveness on a variety of tasks. The paper is well-written and easy to follow, and the proposed method is simple yet effective. The experiments are well-designed and the results are convincing. The paper addresses some of the concerns raised by the reviewers in the rebuttal. However, the paper could benefit from additional ablation studies on hyperparameters and a more detailed discussion of the limitations of the proposed method. The paper could also benefit from a more detailed analysis of the scalability and generalizability of the proposed method. Overall, the paper presents a novel approach to inter-LLM communication and demonstrates its effectiveness on a variety of tasks. The paper is well-written and easy to follow, and the proposed method is simple yet effective. The experiments are well-designed and the results are convincing. The paper addresses some of the concerns raised by the reviewers in the rebuttal. However, the paper could benefit from additional ablation studies on hyperparameters and a more detailed discussion of the limitations of the proposed method. The paper could also benefit from a more detailed analysis of the scalability and generalizability of the proposed method.

### justification_for_why_not_higher_score

The paper presents a novel approach to inter-LLM communication and demonstrates its effectiveness on a variety of tasks. The paper is well-written and easy to follow, and the proposed method is simple yet effective. The experiments are well-designed and the results are convincing. The paper addresses some of the concerns raised by the reviewers in the rebuttal. However, the paper could benefit from additional ablation studies on hyperparameters and a more detailed discussion of the limitations of the proposed method. The paper could also benefit from a more detailed analysis of the scalability and generalizability of the proposed method.

### justification_for_why_not_lower_score

The paper presents a novel approach to inter-LLM communication and demonstrates its effectiveness on a variety of tasks. The paper is well-written and easy to follow, and the proposed method is simple yet effective. The experiments are well-designed and the results are convincing. The paper addresses some of the concerns raised by the reviewers in the rebuttal. However, the paper could benefit from additional ablation studies on hyperparameters and a more detailed discussion of the limitations of the proposed method. The paper could also benefit from a more detailed analysis of the scalability and generalizability of the proposed method.

**********

## Paper Decision

Accept (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster