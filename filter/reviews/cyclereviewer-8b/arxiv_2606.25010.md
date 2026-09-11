## Reviewer

### Summary

The paper studies the emergence of capabilities in transformer models. The authors show that the emergence of capabilities is driven by the learning of task-relevant attention patterns. The authors also show that the difficulty of learning attention patterns depends on context length and pattern sparsity.

### Soundness

3 good

### Presentation

3 good

### Contribution

2 fair

### Strengths

The paper is well-written and easy to follow.

### Weaknesses

The paper does not seem to have any significant contributions. The authors show that the emergence of capabilities is driven by the learning of task-relevant attention patterns. This is not a new finding. The authors also show that the difficulty of learning attention patterns depends on context length and pattern sparsity. This is also not a new finding. The authors also show that scaling the number of attention heads improves learning efficiency on their synthetic tasks, while increasing the head dimension yields diminishing returns past a minimum capacity. This is also not a new finding.

### Questions

I don't have any questions.

### Flag For Ethics Review

No ethics review needed.

### Rating

3: reject, not good enough

### Confidence

4: You are confident in your assessment, but not absolutely certain. It is unlikely, but not impossible, that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work.

**********

## Reviewer

### Summary

This paper investigates the emergence of capabilities in language models, focusing on the role of attention patterns. The authors demonstrate that capabilities arise stochastically throughout training, with larger models acquiring them earlier on average. They also show that the emergence of capabilities corresponds to the learning of task-relevant attention patterns. The paper introduces synthetic linear map and cellular automata datasets to study the difficulty of learning attention patterns, revealing that it depends on context length and pattern sparsity. The study suggests that learning long-context, sparse attention patterns is a key bottleneck for eliciting downstream capabilities in transformer models. The authors propose future research directions to improve model ability to learn sparse attention patterns.

### Soundness

3 good

### Presentation

3 good

### Contribution

3 good

### Strengths

The paper provides a mechanistic insight into emergence, highlighting that downstream capabilities arise abruptly due to the intrinsic difficulty of learning sparse attention patterns in transformer models. The paper also introduces synthetic tasks to study the effects of factors like context length and pattern sparsity on attention pattern learning.

### Weaknesses

The paper's findings are limited to synthetic tasks and may not generalize to more complex natural language tasks. The paper's experiments are conducted on relatively small models, and it is unclear whether the findings would hold for larger models. The paper does not provide a comprehensive comparison with other architectures beyond MLP-Mixer.

### Questions

The paper's findings are limited to synthetic tasks and may not generalize to more complex natural language tasks. The paper's experiments are conducted on relatively small models, and it is unclear whether the findings would hold for larger models. The paper does not provide a comprehensive comparison with other architectures beyond MLP-Mixer.

### Flag For Ethics Review

No ethics review needed.

### Rating

6: marginally above the acceptance threshold

### Confidence

3: You are fairly confident in your assessment. It is possible that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work. Math/other details were not carefully checked.

**********

## Reviewer

### Summary

This paper studies the emergence of capabilities in language models. The authors show that the emergence of capabilities is driven by the learning of task-relevant attention patterns. The authors also show that the difficulty of learning attention patterns depends on context length and pattern sparsity.

### Soundness

3 good

### Presentation

3 good

### Contribution

3 good

### Strengths

The paper is well written and easy to follow. The experiments are extensive and the results are interesting.

### Weaknesses

The experiments are conducted on relatively small models, and it is unclear whether the findings would hold for larger models.

### Questions

1. How does the emergence of capabilities change as the model scale increases? Does it still follow the same pattern as observed in the experiments conducted on smaller models?

2. How does the emergence of capabilities change as the context length increases? Does it still follow the same pattern as observed in the experiments conducted on smaller models?

### Flag For Ethics Review

No ethics review needed.

### Rating

6: marginally above the acceptance threshold

### Confidence

3: You are fairly confident in your assessment. It is possible that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work. Math/other details were not carefully checked.

**********

## Reviewer

### Summary

This paper studies the emergence of capabilities in language models. The authors show that the emergence of capabilities is driven by the learning of task-relevant attention patterns. The authors also show that the difficulty of learning attention patterns depends on context length and pattern sparsity.

### Soundness

3 good

### Presentation

3 good

### Contribution

3 good

### Strengths

This paper is well-written and easy to follow. The experiments are extensive and the results are interesting.

### Weaknesses

The experiments are conducted on relatively small models, and it is unclear whether the findings would hold for larger models.

### Questions

1. How does the emergence of capabilities change as the model scale increases? Does it still follow the same pattern as observed in the experiments conducted on smaller models?

2. How does the emergence of capabilities change as the context length increases? Does it still follow the same pattern as observed in the experiments conducted on smaller models?

### Flag For Ethics Review

No ethics review needed.

### Rating

6: marginally above the acceptance threshold

### Confidence

3: You are fairly confident in your assessment. It is possible that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work. Math/other details were not carefully checked.

**********

## Meta Review

This paper investigates the emergence of capabilities in language models, focusing on the role of attention patterns. The authors demonstrate that capabilities arise stochastically throughout training, with larger models acquiring them earlier on average. They also show that the emergence of capabilities corresponds to the learning of task-relevant attention patterns. The paper introduces synthetic linear map and cellular automata datasets to study the difficulty of learning attention patterns, revealing that it depends on context length and pattern sparsity. The study suggests that learning long-context, sparse attention patterns is a key bottleneck for eliciting downstream capabilities in transformer models. The authors propose future research directions to improve model ability to learn sparse attention patterns.

The reviewers generally agree that the paper is well-written and easy to follow, and the experiments are extensive and the results are interesting. However, the experiments are conducted on relatively small models, and it is unclear whether the findings would hold for larger models. The authors are encouraged to address this limitation in their future work.

### justification_for_why_not_higher_score

The experiments are conducted on relatively small models, and it is unclear whether the findings would hold for larger models.

### justification_for_why_not_lower_score

N/A

**********

## Paper Decision

Reject (not selected for publication for ICLR 2024)