## Reviewer

### Summary

The paper studies the linearity of transformer decoders. It finds that the embedding transformations between sequential layers in transformer decoders exhibit almost linear properties. The paper also proposes a new regularization approach for pretraining based on the cosine similarity, designed to decrease the layer linearity. The proposed method improves the performance of transformer models on benchmark datasets such as SuperGLUE and TinyStories.

### Soundness

3 good

### Presentation

3 good

### Contribution

2 fair

### Strengths

The paper is well-written and easy to follow. The experiments are comprehensive and the results are promising.

### Weaknesses

The paper focuses on the linearity of transformer decoders, which is a relatively narrow topic. The paper could benefit from a more thorough discussion of related work on sparsity and pruning in transformers. The paper also could benefit from a more in-depth analysis of the limitations of the proposed method.

### Questions

1. What are the limitations of the proposed method? How does it compare to other pruning and distillation techniques in the literature?
2. How does the proposed method perform on larger models?
3. How does the proposed method perform on different types of tasks?

### Flag For Ethics Review

No ethics review needed.

### Rating

6: marginally above the acceptance threshold

### Confidence

4: You are confident in your assessment, but not absolutely certain. It is unlikely, but not impossible, that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work.

**********

## Reviewer

### Summary

This paper presents an in-depth analysis of the linearity properties of transformer decoders, revealing a surprising near-linear behavior in embedding transformations between sequential layers. The paper introduces new pruning and distillation techniques inspired by this observation, demonstrating that transformer models can be refined and optimized without compromising performance. Additionally, a cosine-based regularization approach during pretraining is proposed, enhancing model efficiency and performance on benchmarks like SuperGLUE and TinyStories. The study highlights the relationship between linearity and performance of transformer decoders, offering strategic guidance for future model developments.

### Soundness

3 good

### Presentation

3 good

### Contribution

3 good

### Strengths

1. The paper presents a novel and insightful analysis of the linearity properties of transformer decoders, revealing a surprising near-linear behavior in embedding transformations between sequential layers.
2. The paper introduces new pruning and distillation techniques inspired by this observation, demonstrating that transformer models can be refined and optimized without compromising performance.
3. The study highlights the relationship between linearity and performance of transformer decoders, offering strategic guidance for future model developments.

### Weaknesses

1. The paper could benefit from a more comprehensive discussion of the potential limitations and challenges associated with the proposed methods, particularly in the context of larger and more complex models.
2. The paper could also provide more details on the scalability and generalizability of the proposed methods to different domains and tasks, beyond the specific benchmarks and datasets used in the experiments.

### Questions

1. How do the proposed pruning and distillation techniques compare to existing methods in terms of computational efficiency and scalability?
2. How do the proposed methods perform on larger and more complex models, and what are the potential challenges and limitations in applying these methods to such models?
3. How do the proposed methods generalize to different domains and tasks, beyond the specific benchmarks and datasets used in the experiments?

### Flag For Ethics Review

No ethics review needed.

### Rating

6: marginally above the acceptance threshold

### Confidence

3: You are fairly confident in your assessment. It is possible that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work. Math/other details were not carefully checked.

**********

## Reviewer

### Summary

The paper studies the linearity of the embedding transformation in the transformer decoder. The authors find that the embedding transformation between sequential layers is highly linear. Based on this observation, the authors propose a pruning method that removes the most linear layers and a distillation method that replaces the pruned layers with linear approximations. The authors also propose a regularization term that encourages the embeddings of sequential layers to be similar. The proposed methods are evaluated on several benchmarks, and the results show that the proposed methods can improve the performance of the model.

### Soundness

3 good

### Presentation

3 good

### Contribution

3 good

### Strengths

1. The paper studies the linearity of the embedding transformation in the transformer decoder, which is a novel and interesting problem.
2. The authors propose a pruning method that removes the most linear layers and a distillation method that replaces the pruned layers with linear approximations, which are effective and efficient.
3. The authors also propose a regularization term that encourages the embeddings of sequential layers to be similar, which can improve the performance of the model.

### Weaknesses

1. The paper only studies the linearity of the embedding transformation in the transformer decoder, but not the encoder. It would be interesting to see how the linearity of the encoder is different from the decoder.
2. The paper only evaluates the proposed methods on a few benchmarks, and it would be interesting to see how the proposed methods perform on more benchmarks.
3. The paper only studies the linearity of the embedding transformation in the transformer decoder, but not the linearity of the attention mechanism. It would be interesting to see how the linearity of the attention mechanism is different from the embedding transformation.

### Questions

1. How does the linearity of the encoder compare to the decoder?
2. How does the proposed method perform on more benchmarks?
3. How does the linearity of the attention mechanism compare to the embedding transformation?

### Flag For Ethics Review

No ethics review needed.

### Rating

6: marginally above the acceptance threshold

### Confidence

3: You are fairly confident in your assessment. It is possible that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work. Math/other details were not carefully checked.

**********

## Reviewer

### Summary

The paper studies the linearity of the embedding transformation in the transformer decoder. The authors find that the embedding transformation between sequential layers is highly linear. Based on this observation, the authors propose a pruning method that removes the most linear layers and a distillation method that replaces the pruned layers with linear approximations. The authors also propose a regularization term that encourages the embeddings of sequential layers to be similar. The proposed methods are evaluated on several benchmarks, and the results show that the proposed methods can improve the performance of the model.

### Soundness

3 good

### Presentation

3 good

### Contribution

3 good

### Strengths

1. The paper studies the linearity of the embedding transformation in the transformer decoder, which is a novel and interesting problem.
2. The authors propose a pruning method that removes the most linear layers and a distillation method that replaces the pruned layers with linear approximations, which are effective and efficient.
3. The authors also propose a regularization term that encourages the embeddings of sequential layers to be similar, which can improve the performance of the model.

### Weaknesses

1. The paper only studies the linearity of the embedding transformation in the transformer decoder, but not the encoder. It would be interesting to see how the linearity of the encoder is different from the decoder.
2. The paper only evaluates the proposed methods on a few benchmarks, and it would be interesting to see how the proposed methods perform on more benchmarks.
3. The paper only studies the linearity of the embedding transformation in the transformer decoder, but not the linearity of the attention mechanism. It would be interesting to see how the linearity of the attention mechanism is different from the embedding transformation.

### Questions

1. How does the linearity of the encoder compare to the decoder?
2. How does the proposed method perform on more benchmarks?
3. How does the linearity of the attention mechanism compare to the embedding transformation?

### Flag For Ethics Review

No ethics review needed.

### Rating

6: marginally above the acceptance threshold

### Confidence

3: You are fairly confident in your assessment. It is possible that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work. Math/other details were not carefully checked.

**********

## Meta Review

This paper studies the linearity of the embedding transformation in the transformer decoder. The authors find that the embedding transformation between sequential layers is highly linear. Based on this observation, the authors propose a pruning method that removes the most linear layers and a distillation method that replaces the pruned layers with linear approximations. The authors also propose a regularization term that encourages the embeddings of sequential layers to be similar. The proposed methods are evaluated on several benchmarks, and the results show that the proposed methods can improve the performance of the model.

The reviewers agree that the paper studies an interesting problem and the proposed methods are effective and efficient. However, the reviewers also raise some concerns about the limited evaluation and the generalizability of the proposed methods. The authors address these concerns by providing additional results and clarifications. The reviewers acknowledge the additional results and appreciate the authors' efforts to address their concerns.

### justification_for_why_not_higher_score

The paper studies a specific problem and the proposed methods are only evaluated on a few benchmarks. The generalizability of the proposed methods to larger and more complex models is not well studied.

### justification_for_why_not_lower_score

The paper studies an interesting problem and the proposed methods are effective and efficient. The authors address the reviewers' concerns by providing additional results and clarifications.

**********

## Paper Decision

Accept (poster)