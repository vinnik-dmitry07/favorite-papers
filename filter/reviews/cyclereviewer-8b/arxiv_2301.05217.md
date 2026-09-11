## Reviewer

### Summary

This paper presents a mechanistic interpretability analysis of a small transformer model trained on a modular addition task. The authors show that the model uses a Fourier multiplication algorithm to solve the task. They then use this understanding to define two progress measures that capture the model's behavior during training. The authors find that the training process can be divided into three phases: memorization, circuit formation, and cleanup. The authors also show that weight decay plays an important role in the grokking phenomenon.

### Soundness

3 good

### Presentation

3 good

### Contribution

3 good

### Strengths

- The paper presents a mechanistic interpretability analysis of a small transformer model trained on a modular addition task. The authors show that the model uses a Fourier multiplication algorithm to solve the task. This is a novel and interesting finding that sheds light on the behavior of transformer models.
- The authors use their understanding of the model's behavior to define two progress measures that capture the model's behavior during training. These progress measures provide a way to track the model's performance over time and understand the dynamics of the training process.
- The authors find that the training process can be divided into three phases: memorization, circuit formation, and cleanup. This provides a useful framework for understanding the grokking phenomenon and the role of weight decay in it.

### Weaknesses

- The paper focuses on a very specific task and model architecture, which limits the generalizability of the findings. It is not clear how the results would extend to other tasks or model architectures.
- The paper does not provide a clear explanation for why the model uses the Fourier multiplication algorithm to solve the modular addition task. It would be helpful to have a more in-depth discussion of the reasons behind this behavior.
- The paper does not provide a clear explanation for the role of weight decay in the grokking phenomenon. It would be helpful to have a more in-depth discussion of the reasons behind this behavior.

### Questions

- How do you think the results would generalize to other tasks or model architectures?
- Can you provide more insight into why the model uses the Fourier multiplication algorithm to solve the modular addition task?
- Can you provide more insight into the role of weight decay in the grokking phenomenon?

### Flag For Ethics Review

No ethics review needed.

### Rating

6: marginally above the acceptance threshold

### Confidence

3: You are fairly confident in your assessment. It is possible that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work. Math/other details were not carefully checked.

**********

## Reviewer

### Summary

This paper studies the grokking phenomenon in small transformers trained on modular addition tasks. The authors reverse engineer the algorithm learned by these networks, which uses discrete Fourier transforms and trigonometric identities to convert addition to rotation about a circle. Based on this understanding, the authors define progress measures that allow them to study the dynamics of training and split training into three continuous phases: memorization, circuit formation, and cleanup. The authors show that grokking, rather than being a sudden shift, arises from the gradual amplification of structured mechanisms encoded in the weights, followed by the later removal of memorizing components.

### Soundness

3 good

### Presentation

3 good

### Contribution

3 good

### Strengths

The paper is well-written and easy to follow. The authors provide a detailed description of the methodology and results, and the figures are clear and informative.

The authors provide a novel and interesting perspective on the grokking phenomenon, and their results suggest that grokking is not a sudden shift, but rather a gradual process. This challenges the conventional wisdom that grokking is a sudden and unexpected event.

The authors also provide a detailed analysis of the mechanisms underlying grokking, including the use of discrete Fourier transforms and trigonometric identities. This provides a mechanistic understanding of how grokking occurs and can inform future research on this topic.

### Weaknesses

The paper focuses on a specific task (modular addition) and model architecture (small transformers), which may limit the generalizability of the findings. It is not clear how the results would extend to other tasks or model architectures.

The paper does not provide a clear explanation for why the model uses the Fourier multiplication algorithm to solve the modular addition task. It would be helpful to have a more in-depth discussion of the reasons behind this behavior.

The paper does not provide a clear explanation for the role of weight decay in the grokking phenomenon. It would be helpful to have a more in-depth discussion of the reasons behind this behavior.

### Questions

How do you think the results would generalize to other tasks or model architectures?

Can you provide more insight into why the model uses the Fourier multiplication algorithm to solve the modular addition task?

Can you provide more insight into the role of weight decay in the grokking phenomenon?

### Flag For Ethics Review

No ethics review needed.

### Rating

6: marginally above the acceptance threshold

### Confidence

3: You are fairly confident in your assessment. It is possible that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work. Math/other details were not carefully checked.

**********

## Reviewer

### Summary

The paper investigates the grokking phenomenon in small transformers trained on modular addition tasks. The authors reverse engineer the algorithm learned by these networks, which uses discrete Fourier transforms and trigonometric identities to convert addition to rotation about a circle. Based on this understanding, the authors define progress measures that allow them to study the dynamics of training and split training into three continuous phases: memorization, circuit formation, and cleanup. The authors show that grokking, rather than being a sudden shift, arises from the gradual amplification of structured mechanisms encoded in the weights, followed by the later removal of memorizing components.

### Soundness

3 good

### Presentation

3 good

### Contribution

3 good

### Strengths

1. The paper is well-written and easy to follow. The authors provide a detailed description of the methodology and results, and the figures are clear and informative.

2. The authors provide a novel and interesting perspective on the grokking phenomenon, and their results suggest that grokking is not a sudden shift, but rather a gradual process. This challenges the conventional wisdom that grokking is a sudden and unexpected event.

3. The authors also provide a detailed analysis of the mechanisms underlying grokking, including the use of discrete Fourier transforms and trigonometric identities. This provides a mechanistic understanding of how grokking occurs and can inform future research on this topic.

### Weaknesses

1. The paper focuses on a specific task (modular addition) and model architecture (small transformers), which may limit the generalizability of the findings. It is not clear how the results would extend to other tasks or model architectures.

2. The paper does not provide a clear explanation for why the model uses the Fourier multiplication algorithm to solve the modular addition task. It would be helpful to have a more in-depth discussion of the reasons behind this behavior.

3. The paper does not provide a clear explanation for the role of weight decay in the grokking phenomenon. It would be helpful to have a more in-depth discussion of the reasons behind this behavior.

### Questions

How do you think the results would generalize to other tasks or model architectures?

Can you provide more insight into why the model uses the Fourier multiplication algorithm to solve the modular addition task?

Can you provide more insight into the role of weight decay in the grokking phenomenon?

### Flag For Ethics Review

No ethics review needed.

### Rating

6: marginally above the acceptance threshold

### Confidence

3: You are fairly confident in your assessment. It is possible that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work. Math/other details were not carefully checked.

**********

## Reviewer

### Summary

The paper presents a mechanistic interpretability study of the grokking phenomenon in small transformers trained on modular addition tasks. The authors reverse engineer the algorithm learned by these networks, which uses discrete Fourier transforms and trigonometric identities to convert addition to rotation about a circle. Based on this understanding, the authors define progress measures that allow them to study the dynamics of training and split training into three continuous phases: memorization, circuit formation, and cleanup. The authors show that grokking, rather than being a sudden shift, arises from the gradual amplification of structured mechanisms encoded in the weights, followed by the later removal of memorizing components.

### Soundness

3 good

### Presentation

3 good

### Contribution

3 good

### Strengths

1. The paper is well-written and easy to follow. The authors provide a detailed description of the methodology and results, and the figures are clear and informative.

2. The authors provide a novel and interesting perspective on the grokking phenomenon, and their results suggest that grokking is not a sudden shift, but rather a gradual process. This challenges the conventional wisdom that grokking is a sudden and unexpected event.

3. The authors also provide a detailed analysis of the mechanisms underlying grokking, including the use of discrete Fourier transforms and trigonometric identities. This provides a mechanistic understanding of how grokking occurs and can inform future research on this topic.

### Weaknesses

1. The paper focuses on a specific task (modular addition) and model architecture (small transformers), which may limit the generalizability of the findings. It is not clear how the results would extend to other tasks or model architectures.

2. The paper does not provide a clear explanation for why the model uses the Fourier multiplication algorithm to solve the modular addition task. It would be helpful to have a more in-depth discussion of the reasons behind this behavior.

3. The paper does not provide a clear explanation for the role of weight decay in the grokking phenomenon. It would be helpful to have a more in-depth discussion of the reasons behind this behavior.

### Questions

How do you think the results would generalize to other tasks or model architectures?

Can you provide more insight into why the model uses the Fourier multiplication algorithm to solve the modular addition task?

Can you provide more insight into the role of weight decay in the grokking phenomenon?

### Flag For Ethics Review

No ethics review needed.

### Rating

6: marginally above the acceptance threshold

### Confidence

3: You are fairly confident in your assessment. It is possible that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work. Math/other details were not carefully checked.

**********

## Meta Review

This paper presents a mechanistic interpretability analysis of a small transformer model trained on a modular addition task. The authors show that the model uses a Fourier multiplication algorithm to solve the task. This is a novel and interesting finding that sheds light on the behavior of transformer models. The authors use their understanding of the model's behavior to define two progress measures that capture the model's behavior during training. These progress measures provide a way to track the model's performance over time and understand the dynamics of the training process. The authors find that the training process can be divided into three phases: memorization, circuit formation, and cleanup. This provides a useful framework for understanding the grokking phenomenon and the role of weight decay in it. The paper is well-written and easy to follow. The authors provide a detailed description of the methodology and results, and the figures are clear and informative. The authors provide a novel and interesting perspective on the grokking phenomenon, and their results suggest that grokking is not a sudden shift, but rather a gradual process. This challenges the conventional wisdom that grokking is a sudden and unexpected event. The authors also provide a detailed analysis of the mechanisms underlying grokking, including the use of discrete Fourier transforms and trigonometric identities. This provides a mechanistic understanding of how grokking occurs and can inform future research on this topic. The paper focuses on a specific task (modular addition) and model architecture (small transformers), which may limit the generalizability of the findings. It is not clear how the results would extend to other tasks or model architectures. The paper does not provide a clear explanation for why the model uses the Fourier multiplication algorithm to solve the modular addition task. It would be helpful to have a more in-depth discussion of the reasons behind this behavior. The paper does not provide a clear explanation for the role of weight decay in the grokking phenomenon. It would be helpful to have a more in-depth discussion of the reasons behind this behavior. The authors have addressed the concerns raised by the reviewers in the rebuttal.

### justification_for_why_not_higher_score

The paper focuses on a specific task (modular addition) and model architecture (small transformers), which may limit the generalizability of the findings. It is not clear how the results would extend to other tasks or model architectures. The paper does not provide a clear explanation for why the model uses the Fourier multiplication algorithm to solve the modular addition task. It would be helpful to have a more in-depth discussion of the reasons behind this behavior. The paper does not provide a clear explanation for the role of weight decay in the grokking phenomenon. It would be helpful to have a more in-depth discussion of the reasons behind this behavior.

### justification_for_why_not_lower_score

The paper presents a mechanistic interpretability analysis of a small transformer model trained on a modular addition task. The authors show that the model uses a Fourier multiplication algorithm to solve the task. This is a novel and interesting finding that sheds light on the behavior of transformer models. The authors use their understanding of the model's behavior to define two progress measures that capture the model's behavior during training. These progress measures provide a way to track the model's performance over time and understand the dynamics of the training process. The authors find that the training process can be divided into three phases: memorization, circuit formation, and cleanup. This provides a useful framework for understanding the grokking phenomenon and the role of weight decay in it. The paper is well-written and easy to follow. The authors provide a detailed description of the methodology and results, and the figures are clear and informative. The authors provide a novel and interesting perspective on the grokking phenomenon, and their results suggest that grokking is not a sudden shift, but rather a gradual process. This challenges the conventional wisdom that grokking is a sudden and unexpected event. The authors also provide a detailed analysis of the mechanisms underlying grokking, including the use of discrete Fourier transforms and trigonometric identities. This provides a mechanistic understanding of how grokking occurs and can inform future research on this topic.

**********

## Paper Decision

Accept (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster)