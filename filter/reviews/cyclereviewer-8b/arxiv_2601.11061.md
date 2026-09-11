## Reviewer

### Summary

This paper studies the spurious rewards paradox in RLVR, which is the phenomenon that RLVR can lead to memorization over generalization. The authors investigate the Qwen2.5 model and identify the Anchor-Adapter circuit, which is the middle layers acting as the decisive trigger for retrieving memorized answers and the later layers undergoing weight transformations to accommodate shortcut signals. The authors also provide ablation experiments to validate the necessity and sufficiency of these layer groups for memorization. Finally, the authors demonstrate that scaling specific MLP keys within this circuit allows for bidirectional causal steering, i.e., artificially inflating or suppressing contamination effect.

### Soundness

3 good

### Presentation

3 good

### Contribution

2 fair

### Strengths

- The paper is well-written and easy to follow.
- The authors provide a comprehensive mechanistic analysis of the spurious rewards paradox in RLVR, including Path Patching, Logit Lens, and JSD analysis, and neural differential equations.
- The authors provide a detailed ablation study to validate the necessity and sufficiency of the Anchor and Adapter layers for memorization.
- The authors demonstrate that scaling specific MLP keys within this circuit allows for bidirectional causal steering, i.e., artificially inflating or suppressing contamination effect.

### Weaknesses

- The paper only studies the Qwen2.5 model, which is a specific model architecture. It is unclear whether the findings can be generalized to other model architectures.
- The paper only studies the spurious rewards paradox in RLVR, which is a specific phenomenon. It is unclear whether the findings can be generalized to other phenomena in RLVR.
- The paper does not provide a comprehensive discussion of the limitations of the findings and potential future work.

### Questions

- How do the findings generalize to other model architectures?
- How do the findings generalize to other phenomena in RLVR?
- What are the limitations of the findings?
- What are the potential future directions for this work?

### Flag For Ethics Review

No ethics review needed.

### Rating

6: marginally above the acceptance threshold

### Confidence

4: You are confident in your assessment, but not absolutely certain. It is unlikely, but not impossible, that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work.

**********

## Reviewer

### Summary

This paper presents a mechanistic analysis of how spurious RLVR induces stubborn memorization in the Qwen2.5-Math models. The authors identify the Perplexity Paradox: rising prompt perplexity alongside falling answer perplexity, as a macroscopic fingerprint of this phenomenon, where general language coherence is sacrificed for shortcut learning. Mechanistically, they uncover a fundamental decoupling between function and structure: utilizing Path Patching, Logit Lens, JSD analysis, and Neural Differential Equations (NDEs), they pinpoint Layers 18–20 as the Functional Anchor that causally injects the memorization trigger, while Layers 21+ serve as Structural Adapters that undergo drastic weight reorganization to accommodate this signal. Ablation experiments confirm that these layers encode dataset-specific shortcuts rather than general reasoning improvements, as manipulation selectively degrades contaminated benchmarks while leaving clean benchmarks unaffected. Finally, they demonstrate that scaling specific MLP keys within this circuit allows for bidirectional causal steering, i.e., artificially amplifying or suppressing contamination-driven performance. With a conservative probe gate, the same intervention becomes a selective shortcut audit that suppresses suspicious contaminated gains while preserving behavior on fresh benchmarks. Their findings provide mechanistic grounding for understanding RLVR vulnerabilities and open avenues for targeted mitigation strategies.

### Soundness

3 good

### Presentation

3 good

### Contribution

3 good

### Strengths

The paper is well-written and easy to follow. The authors provide a comprehensive mechanistic analysis of the spurious rewards paradox in RLVR, including Path Patching, Logit Lens, and JSD analysis, and neural differential equations. The authors provide a detailed ablation study to validate the necessity and sufficiency of the Anchor and Adapter layers for memorization. The authors demonstrate that scaling specific MLP keys within this circuit allows for bidirectional causal steering, i.e., artificially inflating or suppressing contamination effect.

### Weaknesses

The paper only studies the Qwen2.5 model, which is a specific model architecture. It is unclear whether the findings can be generalized to other model architectures. The paper only studies the spurious rewards paradox in RLVR, which is a specific phenomenon. It is unclear whether the findings can be generalized to other phenomena in RLVR.

### Questions

1. How do the findings generalize to other model architectures?
2. How do the findings generalize to other phenomena in RLVR?
3. What are the limitations of the findings?
4. What are the potential future directions for this work?

### Flag For Ethics Review

No ethics review needed.

### Rating

6: marginally above the acceptance threshold

### Confidence

3: You are fairly confident in your assessment. It is possible that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work. Math/other details were not carefully checked.

**********

## Reviewer

### Summary

The authors investigate the phenomenon of spurious rewards in RLVR and how it leads to memorization of answers. They identify a specific circuit of layers in Qwen2.5-Math that enables this memorization. They also demonstrate that manipulating the weights of these layers can steer the model's behavior.

### Soundness

3 good

### Presentation

3 good

### Contribution

3 good

### Strengths

The authors identify a specific circuit of layers in Qwen2.5-Math that enables memorization of answers, and demonstrate that manipulating the weights of these layers can steer the model's behavior.

### Weaknesses

The paper focuses on a specific model architecture (Qwen2.5-Math) and a specific phenomenon (spurious rewards in RLVR). It is unclear whether the findings can be generalized to other model architectures and phenomena.

### Questions

How do the findings generalize to other model architectures?
How do the findings generalize to other phenomena in RLVR?

### Flag For Ethics Review

No ethics review needed.

### Rating

6: marginally above the acceptance threshold

### Confidence

3: You are fairly confident in your assessment. It is possible that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work. Math/other details were not carefully checked.

**********

## Reviewer

### Summary

The paper studies the phenomenon of spurious rewards in RLVR, which is the phenomenon that RLVR can lead to memorization over generalization. The authors investigate the Qwen2.5 model and identify the Anchor-Adapter circuit, which is the middle layers acting as the decisive trigger for retrieving memorized answers and the later layers undergoing weight transformations to accommodate shortcut signals. The authors also provide ablation experiments to validate the necessity and sufficiency of these layer groups for memorization. Finally, the authors demonstrate that scaling specific MLP keys within this circuit allows for bidirectional causal steering, i.e., artificially inflating or suppressing contamination effect.

### Soundness

3 good

### Presentation

3 good

### Contribution

3 good

### Strengths

- The paper is well-written and easy to follow.
- The authors provide a comprehensive mechanistic analysis of the spurious rewards paradox in RLVR, including Path Patching, Logit Lens, and JSD analysis, and neural differential equations.
- The authors provide a detailed ablation study to validate the necessity and sufficiency of the Anchor and Adapter layers for memorization.
- The authors demonstrate that scaling specific MLP keys within this circuit allows for bidirectional causal steering, i.e., artificially inflating or suppressing contamination effect.

### Weaknesses

- The paper only studies the Qwen2.5 model, which is a specific model architecture. It is unclear whether the findings can be generalized to other model architectures.
- The paper only studies the spurious rewards paradox in RLVR, which is a specific phenomenon. It is unclear whether the findings can be generalized to other phenomena in RLVR.
- The paper does not provide a comprehensive discussion of the limitations of the findings and potential future work.

### Questions

- How do the findings generalize to other model architectures?
- How do the findings generalize to other phenomena in RLVR?
- What are the limitations of the findings?
- What are the potential future directions for this work?

### Flag For Ethics Review

No ethics review needed.

### Rating

6: marginally above the acceptance threshold

### Confidence

3: You are fairly confident in your assessment. It is possible that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work. Math/other details were not carefully checked.

**********

## Meta Review

The paper provides a mechanistic analysis of how spurious RLVR induces stubborn memorization in the Qwen2.5-Math models. The authors identify the Perplexity Paradox: rising prompt perplexity alongside falling answer perplexity, as a macroscopic fingerprint of this phenomenon, where general language coherence is sacrificed for shortcut learning. Mechanistically, they uncover a fundamental decoupling between function and structure: utilizing Path Patching, Logit Lens, JSD analysis, and Neural Differential Equations (NDEs), they pinpoint Layers 18–20 as the Functional Anchor that causally injects the memorization trigger, while Layers 21+ serve as Structural Adapters that undergo drastic weight reorganization to accommodate this signal. Ablation experiments confirm that these layers encode dataset-specific shortcuts rather than general reasoning improvements, as manipulation selectively degrades contaminated benchmarks while leaving clean benchmarks unaffected. Finally, they demonstrate that scaling specific MLP keys within this circuit allows for bidirectional causal steering, i.e., artificially amplifying or suppressing contamination-driven performance. With a conservative probe gate, the same intervention becomes a selective shortcut audit that suppresses suspicious contaminated gains while preserving behavior on fresh benchmarks. Their findings provide mechanistic grounding for understanding RLVR vulnerabilities and open avenues for targeted mitigation strategies.

The paper received 4 reviews, all of which rated it as marginally above the acceptance threshold. The reviewers appreciated the comprehensive mechanistic analysis and the detailed ablation study. The authors provided additional information in their response, which was appreciated by the reviewers.

### justification_for_why_not_higher_score

The paper only studies the Qwen2.5 model, which is a specific model architecture. It is unclear whether the findings can be generalized to other model architectures. The paper only studies the spurious rewards paradox in RLVR, which is a specific phenomenon. It is unclear whether the findings can be generalized to other phenomena in RLVR.

### justification_for_why_not_lower_score

The paper received 4 reviews, all of which rated it as marginally above the acceptance threshold. The reviewers appreciated the comprehensive mechanistic analysis and the detailed ablation study. The authors provided additional information in their response, which was appreciated by the reviewers.

**********

## Paper Decision

Accept (poster)