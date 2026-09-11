## Reviewer

### Summary

This paper introduces a self-supervised learning method for images called I-JEPA, which stands for Image-based Joint-Embedding Predictive Architecture. The authors propose to predict the representations of various target blocks in an image from a single context block. The key idea is to use a masking strategy that samples target blocks with sufficiently large scale (semantic) and uses a sufficiently informative (spatially distributed) context block. The authors show that I-JEPA is highly scalable and can achieve strong downstream performance across a wide range of tasks, from linear classification to object counting and depth prediction. The method is also shown to be efficient, requiring less compute than previous methods. The paper provides a thorough empirical evaluation of I-JEPA, demonstrating its effectiveness and efficiency.

### Soundness

2 fair

### Presentation

3 good

### Contribution

2 fair

### Strengths

- The paper proposes a novel approach to self-supervised learning from images that does not rely on hand-crafted data-augmentations. This is an interesting direction to explore, as it can potentially lead to more generalizable representations.
- The paper provides a thorough empirical evaluation of the proposed method, demonstrating its effectiveness on a wide range of tasks. This provides strong evidence of the method's utility.
- The paper is well-written and easy to follow. The authors provide a clear explanation of the method and its motivation, and the paper is well-organized.

### Weaknesses

- The paper lacks a strong theoretical foundation for the proposed method. While the authors provide some intuition for why the method works, there is no formal analysis or proof of its correctness or optimality. This makes it difficult to understand the underlying principles of the method and its limitations.
- The paper does not provide a clear comparison to existing methods. While the authors compare I-JEPA to some existing methods, the comparison is not comprehensive and does not provide a clear understanding of how I-JEPA compares to other approaches. This makes it difficult to understand the significance of the proposed method.
- The paper does not provide a clear explanation of the limitations of the proposed method. While the authors provide some discussion of the limitations, the paper does not provide a comprehensive analysis of the method's limitations. This makes it difficult to understand the potential applications and limitations of the proposed method.

### Questions

- Can you provide a more detailed explanation of the masking strategy used in I-JEPA? How is the context block and target block selected, and how is the masking strategy implemented?
- Can you provide a more detailed explanation of the loss function used in I-JEPA? How is the loss computed, and what are the specific components of the loss?
- Can you provide a more detailed explanation of the empirical evaluation of I-JEPA? How were the experiments designed, and what are the specific results?
- Can you provide a more detailed explanation of the limitations of I-JEPA? What are the potential limitations of the method, and how can they be addressed?

### Flag For Ethics Review

No ethics review needed.

### Rating

3: reject, not good enough

### Confidence

4: You are confident in your assessment, but not absolutely certain. It is unlikely, but not impossible, that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work.

**********

## Reviewer

### Summary

This paper presents a new self-supervised learning method that does not rely on hand-crafted data-augmentations. The proposed method, I-JEPA, is a non-generative approach that predicts the representations of various target blocks in an image from a single context block. The authors show that I-JEPA is highly scalable and can achieve strong downstream performance across a wide range of tasks, from linear classification to object counting and depth prediction. The method is also shown to be efficient, requiring less compute than previous methods.

### Soundness

2 fair

### Presentation

2 fair

### Contribution

2 fair

### Strengths

- The paper presents a novel approach to self-supervised learning from images that does not rely on hand-crafted data-augmentations.
- The method is shown to be highly scalable and can achieve strong downstream performance across a wide range of tasks.
- The method is efficient, requiring less compute than previous methods.

### Weaknesses

- The paper does not provide a clear explanation of the masking strategy used in I-JEPA. How is the context block and target block selected, and how is the masking strategy implemented?
- The paper does not provide a clear explanation of the loss function used in I-JEPA. How is the loss computed, and what are the specific components of the loss?
- The paper does not provide a clear explanation of the empirical evaluation of I-JEPA. How were the experiments designed, and what are the specific results?

### Questions

- Can you provide a more detailed explanation of the masking strategy used in I-JEPA?
- Can you provide a more detailed explanation of the loss function used in I-JEPA?
- Can you provide a more detailed explanation of the empirical evaluation of I-JEPA?

### Flag For Ethics Review

No ethics review needed.

### Rating

5: marginally below the acceptance threshold

### Confidence

3: You are fairly confident in your assessment. It is possible that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work. Math/other details were not carefully checked.

**********

## Reviewer

### Summary

The paper proposes a novel self-supervised learning method called Image-based Joint-Embedding Predictive Architecture (I-JEPA) that does not rely on hand-crafted data-augmentations. The authors show that I-JEPA is highly scalable and can achieve strong downstream performance across a wide range of tasks, from linear classification to object counting and depth prediction. The method is also shown to be efficient, requiring less compute than previous methods.

### Soundness

2 fair

### Presentation

3 good

### Contribution

2 fair

### Strengths

- The paper presents a novel approach to self-supervised learning from images that does not rely on hand-crafted data-augmentations.
- The method is shown to be highly scalable and can achieve strong downstream performance across a wide range of tasks.
- The method is efficient, requiring less compute than previous methods.

### Weaknesses

- The paper does not provide a clear explanation of the masking strategy used in I-JEPA. How is the context block and target block selected, and how is the masking strategy implemented?
- The paper does not provide a clear explanation of the loss function used in I-JEPA. How is the loss computed, and what are the specific components of the loss?
- The paper does not provide a clear explanation of the empirical evaluation of I-JEPA. How were the experiments designed, and what are the specific results?

### Questions

- Can you provide a more detailed explanation of the masking strategy used in I-JEPA?
- Can you provide a more detailed explanation of the loss function used in I-JEPA?
- Can you provide a more detailed explanation of the empirical evaluation of I-JEPA?

### Flag For Ethics Review

No ethics review needed.

### Rating

5: marginally below the acceptance threshold

### Confidence

3: You are fairly confident in your assessment. It is possible that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work. Math/other details were not carefully checked.

**********

## Reviewer

### Summary

This paper proposes a novel self-supervised learning method, Image-based Joint-Embedding Predictive Architecture (I-JEPA), which does not rely on hand-crafted data-augmentations. The authors show that I-JEPA is highly scalable and can achieve strong downstream performance across a wide range of tasks, from linear classification to object counting and depth prediction. The method is also shown to be efficient, requiring less compute than previous methods.

### Soundness

2 fair

### Presentation

3 good

### Contribution

2 fair

### Strengths

- The paper presents a novel approach to self-supervised learning from images that does not rely on hand-crafted data-augmentations.
- The method is shown to be highly scalable and can achieve strong downstream performance across a wide range of tasks.
- The method is efficient, requiring less compute than previous methods.

### Weaknesses

- The paper does not provide a clear explanation of the masking strategy used in I-JEPA. How is the context block and target block selected, and how is the masking strategy implemented?
- The paper does not provide a clear explanation of the loss function used in I-JEPA. How is the loss computed, and what are the specific components of the loss?
- The paper does not provide a clear explanation of the empirical evaluation of I-JEPA. How were the experiments designed, and what are the specific results?

### Questions

- Can you provide a more detailed explanation of the masking strategy used in I-JEPA?
- Can you provide a more detailed explanation of the loss function used in I-JEPA?
- Can you provide a more detailed explanation of the empirical evaluation of I-JEPA?

### Flag For Ethics Review

No ethics review needed.

### Rating

5: marginally below the acceptance threshold

### Confidence

3: You are fairly confident in your assessment. It is possible that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work. Math/other details were not carefully checked.

**********

## Meta Review

The paper proposes a novel self-supervised learning method called Image-based Joint-Embedding Predictive Architecture (I-JEPA) that does not rely on hand-crafted data-augmentations. The authors show that I-JEPA is highly scalable and can achieve strong downstream performance across a wide range of tasks, from linear classification to object counting and depth prediction. The method is also shown to be efficient, requiring less compute than previous methods.

However, the reviewers have raised several concerns about the paper, including the lack of a strong theoretical foundation, the need for a more comprehensive comparison to existing methods, and the lack of a clear explanation of the limitations of the proposed method. Additionally, the paper does not provide a clear explanation of the masking strategy used in I-JEPA, the loss function used in I-JEPA, and the empirical evaluation of I-JEPA. The authors did not provide any response to these concerns.

### justification_for_why_not_higher_score

The paper does not provide a clear explanation of the masking strategy used in I-JEPA, the loss function used in I-JEPA, and the empirical evaluation of I-JEPA. The authors did not provide any response to these concerns.

### justification_for_why_not_lower_score

N/A

**********

**********

## Paper Decision

Reject (not selected for publication)