## Reviewer

### Summary

This paper studies the reliability of activation oracles (AOs) for interpreting internal representations of other models. The paper uses a controlled setup where a subject model is fine-tuned to use a hidden concept (e.g., "leaf") while avoiding direct disclosure. An AO is then trained on the subject's activations and used to recover the hidden concept. The paper finds that the AO trained on the subject's activations (FT-AO) can fail to recover the hidden concept, even when the concept is present in the subject's activations. The paper also shows that the failure is not due to the absence of the concept from the subject's or oracle's representations, but rather due to the AO's readout pathway. The paper concludes that behavioral leakage, representation-level decodability, and AO-verbalizability can come apart, raising reliability concerns for learned interpretability interfaces.

### Soundness

2 fair

### Presentation

3 good

### Contribution

2 fair

### Strengths

- The paper studies an important problem of the reliability of activation oracles for interpreting internal representations of other models.
- The paper uses a controlled setup to study the problem, making it easier to draw conclusions.
- The paper provides several interesting findings, including that FT-AOs can become concept-specific anti-readers, and that the failure is not due to the absence of the concept from the subject's or oracle's representations.

### Weaknesses

- The paper only studies a single model architecture (Qwen3-8B) and a single training setup (Taboo Word Guessing). It would be good to see if the findings generalize to other model architectures and training setups.
- The paper only studies a single hidden concept (e.g., "leaf") per subject model. It would be good to see if the findings generalize to multiple hidden concepts per subject model.
- The paper does not provide any practical implications of the findings. For example, how can the results be used to improve the reliability of activation oracles?

### Questions

- What are the practical implications of the findings?
- How do the findings generalize to other model architectures and training setups?
- How do the findings generalize to multiple hidden concepts per subject model?

### Flag For Ethics Review

No ethics review needed.

### Rating

3: reject, not good enough

### Confidence

3: You are fairly confident in your assessment.

**********

## Reviewer

### Summary

This paper studies the reliability of Activation Oracles (AOs) for interpreting internal representations of other models. The paper uses a controlled setup where a subject model is fine-tuned to use a hidden concept (e.g., "leaf") while avoiding direct disclosure. An AO is then trained on the subject's activations and used to recover the hidden concept. The paper finds that the AO trained on the subject's activations (FT-AO) can fail to recover the hidden concept, even when the concept is present in the subject's activations. The paper also shows that the failure is not due to the absence of the concept from the subject's or oracle's representations, but rather due to the AO's readout pathway. The paper concludes that behavioral leakage, representation-level decodability, and AO-verbalizability can come apart, raising reliability concerns for learned interpretability interfaces.

### Soundness

2 fair

### Presentation

3 good

### Contribution

2 fair

### Strengths

1. The paper studies an important problem of the reliability of activation oracles for interpreting internal representations of other models.
2. The paper uses a controlled setup to study the problem, making it easier to draw conclusions.
3. The paper provides several interesting findings, including that FT-AOs can become concept-specific anti-readers, and that the failure is not due to the absence of the concept from the subject's or oracle's representations.

### Weaknesses

1. The paper only studies a single model architecture (Qwen3-8B) and a single training setup (Taboo Word Guessing). It would be good to see if the findings generalize to other model architectures and training setups.
2. The paper only studies a single hidden concept (e.g., "leaf") per subject model. It would be good to see if the findings generalize to multiple hidden concepts per subject model.
3. The paper does not provide any practical implications of the findings. For example, how can the results be used to improve the reliability of activation oracles?

### Questions

1. What are the practical implications of the findings?
2. How do the findings generalize to other model architectures and training setups?
3. How do the findings generalize to multiple hidden concepts per subject model?

### Flag For Ethics Review

No ethics review needed.

### Rating

5: marginally below the acceptance threshold

### Confidence

3: You are fairly confident in your assessment.

**********

## Reviewer

### Summary

The paper investigates the reliability of Activation Oracles (AOs) in interpreting internal representations of other models. The authors use a controlled setup where a subject model is fine-tuned to use a hidden concept (e.g., "leaf") while avoiding direct disclosure. An AO is then trained on the subject's activations and used to recover the hidden concept. The paper finds that the AO trained on the subject's activations (FT-AO) can fail to recover the hidden concept, even when the concept is present in the subject's activations. The paper also shows that the failure is not due to the absence of the concept from the subject's or oracle's representations, but rather due to the AO's readout pathway. The paper concludes that behavioral leakage, representation-level decodability, and AO-verbalizability can come apart, raising reliability concerns for learned interpretability interfaces.

### Soundness

3 good

### Presentation

3 good

### Contribution

2 fair

### Strengths

1. The paper studies an important problem of the reliability of activation oracles for interpreting internal representations of other models.
2. The paper uses a controlled setup to study the problem, making it easier to draw conclusions.
3. The paper provides several interesting findings, including that FT-AOs can become concept-specific anti-readers, and that the failure is not due to the absence of the concept from the subject's or oracle's representations.

### Weaknesses

1. The paper only studies a single model architecture (Qwen3-8B) and a single training setup (Taboo Word Guessing). It would be good to see if the findings generalize to other model architectures and training setups.
2. The paper only studies a single hidden concept (e.g., "leaf") per subject model. It would be good to see if the findings generalize to multiple hidden concepts per subject model.
3. The paper does not provide any practical implications of the findings. For example, how can the results be used to improve the reliability of activation oracles?

### Questions

1. What are the practical implications of the findings?
2. How do the findings generalize to other model architectures and training setups?
3. How do the findings generalize to multiple hidden concepts per subject model?

### Flag For Ethics Review

No ethics review needed.

### Rating

5: marginally below the acceptance threshold

### Confidence

3: You are fairly confident in your assessment.

**********

## Reviewer

### Summary

This paper investigates the reliability of Activation Oracles (AOs) in interpreting internal representations of other models. The authors use a controlled setup where a subject model is fine-tuned to use a hidden concept (e.g., "leaf") while avoiding direct disclosure. An AO is then trained on the subject's activations and used to recover the hidden concept. The paper finds that the AO trained on the subject's activations (FT-AO) can fail to recover the hidden concept, even when the concept is present in the subject's activations. The paper also shows that the failure is not due to the absence of the concept from the subject's or oracle's representations, but rather due to the AO's readout pathway. The paper concludes that behavioral leakage, representation-level decodability, and AO-verbalizability can come apart, raising reliability concerns for learned interpretability interfaces.

### Soundness

2 fair

### Presentation

3 good

### Contribution

2 fair

### Strengths

1. The paper studies an important problem of the reliability of activation oracles for interpreting internal representations of other models.
2. The paper uses a controlled setup to study the problem, making it easier to draw conclusions.
3. The paper provides several interesting findings, including that FT-AOs can become concept-specific anti-readers, and that the failure is not due to the absence of the concept from the subject's or oracle's representations.

### Weaknesses

1. The paper only studies a single model architecture (Qwen3-8B) and a single training setup (Taboo Word Guessing). It would be good to see if the findings generalize to other model architectures and training setups.
2. The paper only studies a single hidden concept (e.g., "leaf") per subject model. It would be good to see if the findings generalize to multiple hidden concepts per subject model.
3. The paper does not provide any practical implications of the findings. For example, how can the results be used to improve the reliability of activation oracles?

### Questions

1. What are the practical implications of the findings?
2. How do the findings generalize to other model architectures and training setups?
3. How do the findings generalize to multiple hidden concepts per subject model?

### Flag For Ethics Review

No ethics review needed.

### Rating

5: marginally below the acceptance threshold

### Confidence

3: You are fairly confident in your assessment.

**********

## Meta Review

The paper studies the reliability of Activation Oracles (AOs) for interpreting internal representations of other models. The paper uses a controlled setup where a subject model is fine-tuned to use a hidden concept (e.g., "leaf") while avoiding direct disclosure. An AO is then trained on the subject's activations and used to recover the hidden concept. The paper finds that the AO trained on the subject's activations (FT-AO) can fail to recover the hidden concept, even when the concept is present in the subject's activations. The paper also shows that the failure is not due to the absence of the concept from the subject's or oracle's representations, but rather due to the AO's readout pathway. The paper concludes that behavioral leakage, representation-level decodability, and AO-verbalizability can come apart, raising reliability concerns for learned interpretability interfaces.

The paper studies an important problem of the reliability of activation oracles for interpreting internal representations of other models. The paper uses a controlled setup to study the problem, making it easier to draw conclusions. The paper provides several interesting findings, including that FT-AOs can become concept-specific anti-readers, and that the failure is not due to the absence of the concept from the subject's or oracle's representations.

However, the paper only studies a single model architecture (Qwen3-8B) and a single training setup (Taboo Word Guessing). It would be good to see if the findings generalize to other model architectures and training setups. The paper only studies a single hidden concept (e.g., "leaf") per subject model. It would be good to see if the findings generalize to multiple hidden concepts per subject model. The paper does not provide any practical implications of the findings. For example, how can the results be used to improve the reliability of activation oracles?

### justification_for_why_not_higher_score

The paper only studies a single model architecture (Qwen3-8B) and a single training setup (Taboo Word Guessing). It would be good to see if the findings generalize to other model architectures and training setups. The paper only studies a single hidden concept (e.g., "leaf") per subject model. It would be good to see if the findings generalize to multiple hidden concepts per subject model. The paper does not provide any practical implications of the findings. For example, how can the results be used to improve the reliability of activation oracles?

### justification_for_why_not_lower_score

N/A

**********

**********

## Paper Decision

Reject (not selected for publication for this ICLR edition)

**********

## Paper Decision Summary

The paper was not selected for publication for this ICLR edition. The reviewers appreciated the importance of the problem studied, the controlled setup, and the interesting findings. However, they noted that the paper only studies a single model architecture and training setup, and does not provide practical implications of the findings. The authors did not submit a response to the reviews. The paper will be reconsidered for the next ICLR edition.