## Reviewer

### Summary

This paper focuses on the Platonic representation hypothesis, which suggests that representations from neural networks are converging to a common statistical model of reality. The authors argue that existing metrics used to measure representational similarity are confounded by network scale, and they introduce a permutation-based null-calibration framework to transform any representational similarity metric into a calibrated score with statistical guarantees. They revisit the Platonic Representation Hypothesis using their calibration framework and find that the apparent convergence reported by global spectral measures largely disappears after calibration, while local neighborhood similarity retains significant agreement across different modalities. The authors propose the Aristotelian Representation Hypothesis, which suggests that representations in neural networks are converging to shared local neighborhood relationships.

### Soundness

3 good

### Presentation

3 good

### Contribution

3 good

### Strengths

1. The paper is well-written and easy to follow.

2. The authors provide a theoretical analysis of the width and depth confounders that affect representational similarity metrics and introduce a null-calibration framework to address these issues.

3. The authors conduct extensive experiments to validate the effectiveness of their calibration framework and provide a nuanced picture of the Platonic Representation Hypothesis.

### Weaknesses

1. The paper could benefit from a more thorough discussion of the limitations of the proposed Aristotelian Representation Hypothesis. While the authors acknowledge that representational similarity has no ground-truth scale, they do not provide a clear explanation of how this limitation affects the validity of their findings.

2. The paper could benefit from a more detailed discussion of the potential implications of the Aristotelian Representation Hypothesis. While the authors propose this hypothesis as a refinement of the Platonic Representation Hypothesis, they do not provide a clear explanation of how this refinement could impact our understanding of neural networks and their representations.

### Questions

1. How does the Aristotelian Representation Hypothesis differ from the Platonic Representation Hypothesis, and what are the implications of this difference for our understanding of neural networks and their representations?

2. How does the proposed null-calibration framework address the limitations of the Aristotelian Representation Hypothesis, and what are the potential implications of this framework for future research in this area?

### Flag For Ethics Review

No ethics review needed.

### Rating

6: marginally above the acceptance threshold

### Confidence

4: You are confident in your assessment, but not absolutely certain. It is unlikely, but not impossible, that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work.

**********

## Reviewer

### Summary

The paper proposes a new method for calibrating representational similarity metrics. The authors argue that the previous metrics are confounded by the model width and depth, and that the calibration is needed to disentangle the signal from the noise. The authors show that the calibration framework works well in the synthetic experiments and then apply it to the Platonic Representation Hypothesis, showing that the global spectral convergence is largely confounded by the width and depth, while the local neighborhood alignment remains significant.

### Soundness

3 good

### Presentation

3 good

### Contribution

2 fair

### Strengths

The paper is well-written and easy to follow. The authors provide a good theoretical analysis of the width and depth confounders that affect representational similarity metrics and introduce a null-calibration framework to address these issues. The authors conduct extensive experiments to validate the effectiveness of their calibration framework and provide a nuanced picture of the Platonic Representation Hypothesis.

### Weaknesses

The paper focuses on the calibration of representational similarity metrics, which is an important problem. However, the novelty of the proposed method seems limited. The authors use a standard permutation-based approach to calibrate the similarity metrics, which has been used in many other works. The authors also use the standard statistical techniques to analyze the width and depth confounders.

### Questions

1. How does the proposed calibration method compare to other calibration methods? For example, the authors could compare their method with the previous calibration methods, such as the ones proposed in [1,2]. 

2. The authors argue that the width and depth confounders affect the representational similarity metrics. However, it is not clear how these confounders affect the downstream tasks. For example, the authors could show how the calibration affects the performance of the downstream tasks, such as the classification accuracy.

3. The authors propose the Aristotelian Representation Hypothesis, which suggests that representations in neural networks are converging to shared local neighborhood relationships. However, it is not clear how this hypothesis can be tested or validated. For example, the authors could provide a more detailed analysis of the local neighborhood alignment and show how it affects the downstream tasks.

[1] Murphy, Brian, et al. "Debiased centered kernel alignment for comparing deep representations." Advances in Neural Information Processing Systems 37 (2024): 25770-25783.

[2] Chun, Soohee, et al. "Debiased centered kernel alignment for comparing deep representations." arXiv preprint arXiv:2305.14382 (2023).

### Flag For Ethics Review

No ethics review needed.

### Rating

6: marginally above the acceptance threshold

### Confidence

3: You are fairly confident in your assessment. It is possible that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work. Math/other details were not carefully checked.

**********

## Reviewer

### Summary

This paper addresses the issue of representational similarity metrics in neural networks, arguing that they are confounded by network scale. To address this, the authors propose a permutation-based null-calibration framework that transforms any representational similarity metric into a calibrated score with statistical guarantees. They revisit the Platonic Representation Hypothesis and find that the apparent convergence reported by global spectral measures largely disappears after calibration, while local neighborhood similarity retains significant agreement across different modalities. The authors propose the Aristotelian Representation Hypothesis, which suggests that representations in neural networks are converging to shared local neighborhood relationships.

### Soundness

3 good

### Presentation

3 good

### Contribution

3 good

### Strengths

1. The paper is well-written and easy to follow.
2. The authors provide a theoretical analysis of the width and depth confounders that affect representational similarity metrics and introduce a null-calibration framework to address these issues.
3. The authors conduct extensive experiments to validate the effectiveness of their calibration framework and provide a nuanced picture of the Platonic Representation Hypothesis.

### Weaknesses

1. The authors could provide more details about the limitations of the Aristotelian Representation Hypothesis. While the authors acknowledge that representational similarity has no ground-truth scale, they do not provide a clear explanation of how this limitation affects the validity of their findings.
2. The authors could provide more details about the potential implications of the Aristotelian Representation Hypothesis. While the authors propose this hypothesis as a refinement of the Platonic Representation Hypothesis, they do not provide a clear explanation of how this refinement could impact our understanding of neural networks and their representations.

### Questions

1. How does the Aristotelian Representation Hypothesis differ from the Platonic Representation Hypothesis, and what are the implications of this difference for our understanding of neural networks and their representations?
2. How does the proposed null-calibration framework address the limitations of the Aristotelian Representation Hypothesis, and what are the potential implications of this framework for future research in this area?

### Flag For Ethics Review

No ethics review needed.

### Rating

6: marginally above the acceptance threshold

### Confidence

3: You are fairly confident in your assessment. It is possible that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work. Math/other details were not carefully checked.

**********

## Reviewer

### Summary

This paper presents a framework to calibrate representational similarity metrics by considering two confounders: width and depth. The authors provide theoretical analysis and empirical results to support their framework.

### Soundness

3 good

### Presentation

3 good

### Contribution

3 good

### Strengths

1. The paper is well-written and easy to follow.
2. The authors provide a theoretical analysis of the width and depth confounders that affect representational similarity metrics and introduce a null-calibration framework to address these issues.
3. The authors conduct extensive experiments to validate the effectiveness of their calibration framework and provide a nuanced picture of the Platonic Representation Hypothesis.

### Weaknesses

1. The authors could provide more details about the limitations of the Aristotelian Representation Hypothesis. While the authors acknowledge that representational similarity has no ground-truth scale, they do not provide a clear explanation of how this limitation affects the validity of their findings.
2. The authors could provide more details about the potential implications of the Aristotelian Representation Hypothesis. While the authors propose this hypothesis as a refinement of the Platonic Representation Hypothesis, they do not provide a clear explanation of how this refinement could impact our understanding of neural networks and their representations.

### Questions

1. How does the Aristotelian Representation Hypothesis differ from the Platonic Representation Hypothesis, and what are the implications of this difference for our understanding of neural networks and their representations?
2. How does the proposed null-calibration framework address the limitations of the Aristotelian Representation Hypothesis, and what are the potential implications of this framework for future research in this area?

### Flag For Ethics Review

No ethics review needed.

### Rating

6: marginally above the acceptance threshold

### Confidence

3: You are fairly confident in your assessment. It is possible that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work. Math/other details were not carefully checked.

**********

## Meta Review

This paper addresses the problem of representational similarity metrics in neural networks, arguing that they are confounded by network scale. To address this, the authors propose a permutation-based null-calibration framework that transforms any representational similarity metric into a calibrated score with statistical guarantees. They revisit the Platonic Representation Hypothesis and find that the apparent convergence reported by global spectral measures largely disappears after calibration, while local neighborhood similarity retains significant agreement across different modalities. The authors propose the Aristotelian Representation Hypothesis, which suggests that representations in neural networks are converging to shared local neighborhood relationships.

The reviewers generally agreed that the paper is well-written and easy to follow, and the authors provided a theoretical analysis of the width and depth confounders that affect representational similarity metrics and introduced a null-calibration framework to address these issues. The authors conducted extensive experiments to validate the effectiveness of their calibration framework and provided a nuanced picture of the Platonic Representation Hypothesis.

The reviewers raised some questions about the limitations of the Aristotelian Representation Hypothesis and the potential implications of this framework for future research in this area. The authors provided additional information and clarifications in their response, which addressed some of the concerns.

### justification_for_why_not_higher_score

The paper focuses on the calibration of representational similarity metrics, which is an important problem. However, the novelty of the proposed method seems limited. The authors use a standard permutation-based approach to calibrate the similarity metrics, which has been used in many other works. The authors also use the standard statistical techniques to analyze the width and depth confounders.

### justification_for_why_not_lower_score

The paper is well-written and easy to follow. The authors provide a theoretical analysis of the width and depth confounders that affect representational similarity metrics and introduce a null-calibration framework to address these issues. The authors conduct extensive experiments to validate the effectiveness of their calibration framework and provide a nuanced picture of the Platonic Representation Hypothesis.

**********

## Paper Decision

Accept (poster)