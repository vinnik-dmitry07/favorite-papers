## Reviewer

### Summary

This paper investigates the use of linear probes to detect strategic deception in language models. The authors train linear probes on two different datasets, one with instructed pairs and one with roleplaying scenarios, and evaluate them on various realistic settings where the model behaves deceptively. They find that the probes can distinguish between honest and deceptive responses with high accuracy but struggle with low false positive rates. The authors conclude that while white-box probes are promising for monitoring systems, they are not yet robust enough to detect deception.

### Soundness

3 good

### Presentation

3 good

### Contribution

2 fair

### Strengths

- The paper is well-written and easy to follow.
- The authors provide a thorough evaluation of their method on various datasets and settings.
- The paper is well-motivated and addresses an important problem.

### Weaknesses

- The paper lacks novelty. The authors use existing datasets and methods for training and evaluating their probes. The only novelty seems to be the use of a new model (LLaMA-3.3-70B-Instruct) and the evaluation on additional datasets. However, this is not enough to justify the novelty of the paper.
- The authors do not provide a thorough analysis of the limitations of their method. While they mention some limitations in the discussion, they do not provide a comprehensive evaluation of the method's weaknesses.
- The paper does not provide a clear conclusion or recommendation for future work. The authors conclude that white-box probes are promising but not yet robust enough for detecting deception. However, they do not provide any guidance on how to improve the method or what future work should focus on.

### Questions

- What are the limitations of the method, and how can they be addressed?
- How can the method be improved to achieve better false positive rates?
- What are the implications of the results for future work in this area?

### Flag For Ethics Review

No ethics review needed.

### Rating

3: reject, not good enough

### Confidence

4: You are confident in your assessment, but not absolutely certain. It is unlikely, but not impossible, that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work.

**********

## Reviewer

### Summary

This paper proposes to use linear probes to detect deception in LLMs. The paper trains a linear probe on a dataset of instructed pairs (from Zou et al.) and a roleplaying dataset, and evaluates it on a variety of datasets where LLMs are known to exhibit deception. The paper finds that the probe can detect deception with high accuracy, but struggles with false positives.

### Soundness

3 good

### Presentation

3 good

### Contribution

2 fair

### Strengths

The paper is well-written and easy to follow. The authors provide a thorough evaluation of their method on various datasets and settings. The paper is well-motivated and addresses an important problem. The use of linear probes to detect deception is an interesting idea, and the authors provide a good justification for their approach.

### Weaknesses

I have several concerns with the paper:

1. The paper does not provide a clear justification for why linear probes are a good approach for detecting deception. The authors mention that they are using linear probes because they are white-box and can be used to monitor model internals, but this is not a good reason to use linear probes. The authors should provide a clear justification for their choice of method.

2. The paper does not provide a clear evaluation of the limitations of their method. The authors mention some limitations in the discussion, but they do not provide a comprehensive evaluation of the method's weaknesses. The authors should provide a more thorough evaluation of the limitations of their method.

3. The paper does not provide a clear conclusion or recommendation for future work. The authors conclude that white-box probes are promising but not yet robust enough for detecting deception. However, they do not provide any guidance on how to improve the method or what future work should focus on. The authors should provide a more thorough discussion of the implications of their results for future work in this area.

### Questions

1. What are the limitations of the method, and how can they be addressed?

2. How can the method be improved to achieve better false positive rates?

3. What are the implications of the results for future work in this area?

### Flag For Ethics Review

No ethics review needed.

### Rating

5: marginally below the acceptance threshold

### Confidence

4: You are confident in your assessment, but not absolutely certain. It is unlikely, but not impossible, that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work.

**********

## Reviewer

### Summary

The paper proposes to use linear probes to detect strategic deception in LLMs. The authors train a linear probe on a dataset of instructed pairs and a roleplaying dataset, and evaluate it on a variety of datasets where LLMs are known to exhibit deception. The paper finds that the probe can detect deception with high accuracy, but struggles with false positives.

### Soundness

3 good

### Presentation

3 good

### Contribution

2 fair

### Strengths

The paper is well-written and easy to follow. The authors provide a thorough evaluation of their method on various datasets and settings. The paper is well-motivated and addresses an important problem. The use of linear probes to detect deception is an interesting idea, and the authors provide a good justification for their approach.

### Weaknesses

1. The paper does not provide a clear justification for why linear probes are a good approach for detecting deception. The authors mention that they are using linear probes because they are white-box and can be used to monitor model internals, but this is not a good reason to use linear probes. The authors should provide a clear justification for their choice of method.

2. The paper does not provide a clear evaluation of the limitations of their method. The authors mention some limitations in the discussion, but they do not provide a comprehensive evaluation of the method's weaknesses. The authors should provide a more thorough evaluation of the limitations of their method.

3. The paper does not provide a clear conclusion or recommendation for future work. The authors conclude that white-box probes are promising but not yet robust enough for detecting deception. However, they do not provide any guidance on how to improve the method or what future work should focus on. The authors should provide a more thorough discussion of the implications of their results for future work in this area.

### Questions

1. What are the limitations of the method, and how can they be addressed?

2. How can the method be improved to achieve better false positive rates?

3. What are the implications of the results for future work in this area?

### Flag For Ethics Review

No ethics review needed.

### Rating

5: marginally below the acceptance threshold

### Confidence

4: You are confident in your assessment, but not absolutely certain. It is unlikely, but not impossible, that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work.

**********

## Reviewer

### Summary

This paper proposes to use linear probes to detect strategic deception in LLMs. The authors train a linear probe on a dataset of instructed pairs and a roleplaying dataset, and evaluate it on a variety of datasets where LLMs are known to exhibit deception. The paper finds that the probe can detect deception with high accuracy, but struggles with false positives.

### Soundness

3 good

### Presentation

3 good

### Contribution

3 good

### Strengths

This paper is well-written and easy to follow. The authors provide a thorough evaluation of their method on various datasets and settings. The paper is well-motivated and addresses an important problem. The use of linear probes to detect deception is an interesting idea, and the authors provide a good justification for their approach. The paper also provides a good discussion of the limitations of their method and potential future work.

### Weaknesses

This paper is well-written and easy to follow. The authors provide a thorough evaluation of their method on various datasets and settings. The paper is well-motivated and addresses an important problem. The use of linear probes to detect deception is an interesting idea, and the authors provide a good justification for their approach. The paper also provides a good discussion of the limitations of their method and potential future work.

### Questions

The paper does not provide a clear justification for why linear probes are a good approach for detecting deception. The authors mention that they are using linear probes because they are white-box and can be used to monitor model internals, but this is not a good reason to use linear probes. The authors should provide a clear justification for their choice of method.

The paper does not provide a clear evaluation of the limitations of their method. The authors mention some limitations in the discussion, but they do not provide a comprehensive evaluation of the method's weaknesses. The authors should provide a more thorough evaluation of the limitations of their method.

The paper does not provide a clear conclusion or recommendation for future work. The authors conclude that white-box probes are promising but not yet robust enough for detecting deception. However, they do not provide any guidance on how to improve the method or what future work should focus on. The authors should provide a more thorough discussion of the implications of their results for future work in this area.

### Flag For Ethics Review

No ethics review needed.

### Rating

5: marginally below the acceptance threshold

### Confidence

3: You are fairly confident in your assessment. It is possible that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work. Math/other details were not carefully checked.

**********

## Meta Review

This paper proposes to use linear probes to detect strategic deception in LLMs. The authors train a linear probe on a dataset of instructed pairs and a roleplaying dataset, and evaluate it on a variety of datasets where LLMs are known to exhibit deception. The paper finds that the probe can detect deception with high accuracy, but struggles with false positives.

The reviewers raised the following concerns:

- The paper lacks novelty. The authors use existing datasets and methods for training and evaluating their probes. The only novelty seems to be the use of a new model (LLaMA-3.3-70B-Instruct) and the evaluation on additional datasets. However, this is not enough to justify the novelty of the paper.
- The authors do not provide a thorough analysis of the limitations of their method. While they mention some limitations in the discussion, they do not provide a comprehensive evaluation of the method's weaknesses.
- The paper does not provide a clear conclusion or recommendation for future work. The authors conclude that white-box probes are promising but not yet robust enough for detecting deception. However, they do not provide any guidance on how to improve the method or what future work should focus on.

### justification_for_why_not_higher_score

The reviewers raised the following concerns:

- The paper lacks novelty. The authors use existing datasets and methods for training and evaluating their probes. The only novelty seems to be the use of a new model (LLaMA-3.3-70B-Instruct) and the evaluation on additional datasets. However, this is not enough to justify the novelty of the paper.
- The authors do not provide a thorough analysis of the limitations of their method. While they mention some limitations in the discussion, they do not provide a comprehensive evaluation of the method's weaknesses.
- The paper does not provide a clear conclusion or recommendation for future work. The authors conclude that white-box probes are promising but not yet robust enough for detecting deception. However, they do not provide any guidance on how to improve the method or what future work should focus on.

### justification_for_why_not_lower_score

N/A

**********

## Paper Decision

Reject (not selected for publication)