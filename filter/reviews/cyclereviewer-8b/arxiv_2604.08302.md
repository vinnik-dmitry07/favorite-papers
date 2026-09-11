## Reviewer

### Summary

This paper proposes a new paradigm for diffusion language models (dLLMs) that mitigates error accumulation in parallel decoding, enabling aggressive decoding parallelism while preserving generation quality. The proposed method, DMax, reformulates decoding as a progressive self-refinement from mask embeddings to token embeddings. The paper introduces On-Policy Uniform Training (OPUT), a novel training strategy that efficiently unifies masked and uniform dLLMs, and Soft Parallel Decoding, which represents each intermediate decoding state as an interpolation between the predicted token embedding and the mask embedding. The paper presents extensive experiments across various benchmarks, demonstrating the effectiveness of DMax.

### Soundness

2 fair

### Presentation

3 good

### Contribution

2 fair

### Strengths

The paper presents a new paradigm for diffusion language models (dLLMs) that mitigates error accumulation in parallel decoding, enabling aggressive decoding parallelism while preserving generation quality. The proposed method, DMax, reformulates decoding as a progressive self-refinement from mask embeddings to token embeddings. The paper introduces On-Policy Uniform Training (OPUT), a novel training strategy that efficiently unifies masked and uniform dLLMs, and Soft Parallel Decoding, which represents each intermediate decoding state as an interpolation between the predicted token embedding and the mask embedding. The paper presents extensive experiments across various benchmarks, demonstrating the effectiveness of DMax.

### Weaknesses

The proposed method is not novel enough. The idea of using mask embedding and token embedding to represent the intermediate state in parallel decoding has been explored in previous works such as SM [1] and EvoToken [2]. The main difference is that the proposed method uses the mask embedding as a prior to represent the uncertainty of the model. However, this idea is not new and has been explored in previous works such as [3]. Moreover, the proposed method is only evaluated on small-scale models and datasets, which limits the generalizability of the proposed method. 

[1] SM: Soft Mask for Parallel Decoding of Diffusion Language Models, ICLR 2023

[2] EvoToken: Evolutionary Decoding for Diffusion Language Models, NeurIPS 2023

[3] Learning to Refine: Masked Diffusion Language Models with Mask-Embedded Decoding, ICLR 2023

### Questions

Please refer to the weakness.

### Flag For Ethics Review

No ethics review needed.

### Rating

5: marginally below the acceptance threshold

### Confidence

4: You are confident in your assessment, but not absolutely certain. It is unlikely, but not impossible, that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work.

**********

## Reviewer

### Summary

This paper proposes DMax, a new paradigm for efficient diffusion language models (dLLMs). It mitigates error accumulation in parallel decoding, enabling aggressive decoding parallelism while preserving generation quality. DMax reformulates decoding as a progressive self-refinement from mask embeddings to token embeddings. The paper introduces On-Policy Uniform Training, a novel training strategy that efficiently unifies masked and uniform dLLMs, and Soft Parallel Decoding, which represents each intermediate decoding state as an interpolation between the predicted token embedding and the mask embedding. Extensive experiments across various benchmarks demonstrate the effectiveness of DMax.

### Soundness

3 good

### Presentation

3 good

### Contribution

3 good

### Strengths

1. The paper is well-written and easy to follow.
2. The proposed method is novel and effective.
3. The experiments are extensive and convincing.

### Weaknesses

1. The paper lacks some ablation studies. For example, the authors can show the performance of each component of the proposed method. 
2. The paper lacks some experiments. For example, the authors can compare the proposed method with some other methods on some other datasets.

### Questions

Please see the weakness.

### Flag For Ethics Review

No ethics review needed.

### Rating

6: marginally above the acceptance threshold

### Confidence

3: You are fairly confident in your assessment. It is possible that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work. Math/other details were not carefully checked.

**********

## Reviewer

### Summary

This paper proposes a new method for parallel decoding of diffusion language models. The authors propose to use a mask embedding as a prior to represent the uncertainty of the model and use it to refine the decoding process. The authors also introduce a novel training strategy that efficiently unifies masked and uniform dLLMs. The proposed method is evaluated on several benchmarks and shows significant improvements over the baseline.

### Soundness

3 good

### Presentation

3 good

### Contribution

3 good

### Strengths

1. The paper is well-written and easy to follow.
2. The proposed method is novel and effective.
3. The experiments are extensive and convincing.

### Weaknesses

1. The paper lacks some ablation studies. For example, the authors can show the performance of each component of the proposed method.
2. The paper lacks some experiments. For example, the authors can compare the proposed method with some other methods on some other datasets.

### Questions

Please see the weakness.

### Flag For Ethics Review

No ethics review needed.

### Rating

6: marginally above the acceptance threshold

### Confidence

3: You are fairly confident in your assessment. It is possible that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work. Math/other details were not carefully checked.

**********

## Reviewer

### Summary

The paper proposes DMax, a new paradigm for efficient diffusion language models (dLLMs) that mitigates error accumulation in parallel decoding, enabling aggressive decoding parallelism while preserving generation quality. The authors introduce On-Policy Uniform Training, a novel training strategy that efficiently unifies masked and uniform dLLMs, and Soft Parallel Decoding, which represents each intermediate decoding state as an interpolation between the predicted token embedding and the mask embedding. Extensive experiments across various benchmarks demonstrate the effectiveness of DMax.

### Soundness

3 good

### Presentation

3 good

### Contribution

3 good

### Strengths

- The paper proposes a novel approach to parallel decoding in diffusion language models, addressing the issue of error accumulation.
- The paper is well-written and easy to follow.
- The proposed method is evaluated on multiple benchmarks, demonstrating its effectiveness.

### Weaknesses

- The paper lacks some ablation studies. For example, the authors can show the performance of each component of the proposed method.
- The paper lacks some experiments. For example, the authors can compare the proposed method with some other methods on some other datasets.

### Questions

Please see the weakness.

### Flag For Ethics Review

No ethics review needed.

### Rating

6: marginally above the acceptance threshold

### Confidence

3: You are fairly confident in your assessment. It is possible that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work. Math/other details were not carefully checked.

**********

## Meta Review

The paper introduces DMax, a novel approach for efficient diffusion language models (dLLMs) that addresses the challenge of error accumulation in parallel decoding. The authors propose On-Policy Uniform Training and Soft Parallel Decoding, which are evaluated on various benchmarks, showing the effectiveness of DMax. The paper is well-written and easy to follow. The proposed method is novel and effective, and the experiments are extensive and convincing. However, the paper lacks some ablation studies and experiments. The paper is borderline, but the reviewers are not unanimous.

### justification_for_why_not_higher_score

The paper lacks some ablation studies and experiments.

### justification_for_why_not_lower_score

The paper is well-written and easy to follow. The proposed method is novel and effective, and the experiments are extensive and convincing.

**********

## Paper Decision

Reject (poster) (poster) (7 votes)

**********

---

**Paper Decision:** Reject (poster)

**Score:** 5.25 (median: 5, max: 6, min: 5)

**Percentage:** 0%

**********

---

**AC:** [Yuhao Zhou](https://yuhaozhou.org/)

**********

---

## Paper Decision Discussion

### Score Distribution

| Score | Count |
| ----- | ----- |
| 5     | 4     |

**********

---

## Paper Decision Discussion

### justification_for_why_not_higher_score

The paper lacks some ablation studies and experiments.

### justification_for_why_not_lower_score

The paper is well-written and easy to follow. The proposed method is novel and effective, and the experiments are extensive and convincing.

**********

---

**AC:** [Yuhao Zhou](https://yuhaozhou.org/)

**********

---

## Paper Decision Discussion

### justification_for_why_not_higher_score

The paper lacks some ablation studies and experiments.

### justification_for_why_not_lower_score

The paper is well-written and easy to follow. The proposed method is novel and effective, and the experiments are extensive and convincing.

**********

---

**AC:** [Yuhao Zhou](https://yuhaozhou.org/)

**********

---

## Paper Decision Discussion

### justification_for_why_not_higher_score

The paper lacks some ablation studies and experiments.

### justification_for_why_not_lower_score

The paper is well-written and easy to follow. The proposed method is novel and effective, and the experiments are extensive and convincing.

**********

---

**AC:** [Yuhao Zhou](https://yuhaozhou.org/)

**********

---

## Paper Decision Discussion

### justification_for_why_not_higher_score

The paper lacks some ablation studies and experiments.

### justification_for_why_not_lower_score

The paper is well-written and easy to follow. The proposed method is novel and effective, and the experiments are extensive and convincing.

**********

---

**AC:** [Yuhao Zhou](https://yuhaozhou.org/)

**********

---

## Paper Decision Discussion

### justification_for_why_not_higher_score

The paper lacks some ablation studies and experiments.

### justification_for_why_not_lower_score

The paper is well-written and easy to follow. The proposed method is novel and effective, and the experiments are extensive and convincing.

**********

---

**AC:** [Yuhao Zhou](https://yuhaozhou.org/)

**********

---

## Paper Decision Discussion

### justification_for_why_not_higher_score

The paper lacks some ablation studies and experiments.

### justification_for_why_not_lower_score

The paper is well-written and easy to follow. The proposed method is novel and effective, and the experiments are extensive and convincing.

**********

---

**AC:** [Yuhao Zhou](https://yuhaozhou.org/)

**********

---

## Paper Decision Discussion

### justification_for_why_not_higher_score

The paper lacks some ablation studies and experiments.

### justification_for_why_not_lower_score

The paper is well-written and easy to follow. The proposed method is novel and effective, and the experiments are extensive and convincing.

**********

---

**AC:** [Yuhao Zhou](https://yuhaozhou.org/)

**********

---

## Paper Decision Discussion

### justification_for_why_not_higher_score

The paper lacks some ablation studies and experiments.

### justification_for_why_not_lower_score

The paper is well-written and easy to follow. The proposed method is novel and effective, and the experiments are extensive and convincing.

**********

---

**AC:** [Yuhao Zhou](https://yuhaozhou.org/)

**********

---

## Paper Decision Discussion

### justification_for_why_not_higher_score

The paper lacks some ablation studies and experiments.

### justification_for_why_not_lower_score

The paper is well-written and easy to follow. The proposed method is novel and effective, and the experiments are extensive and convincing.

**********

---

**AC:** [Yuhao Zhou](https://yuhaozhou.org/)

**********

---

## Paper Decision Discussion

### justification_for_why_not_higher_score

The paper lacks some ablation studies and experiments.

### justification_for_why_not_lower_score

The paper is well-written and easy to follow. The proposed method is novel and effective, and the experiments are extensive and convincing.

**********

---

**AC:** [Yuhao Zhou](https://yuhaozhou.org/)

**********

---

## Paper Decision Discussion

### justification_for_why_not_higher_score

The paper lacks some ablation studies and experiments.

### justification_for_why_not_lower_score

The paper is well-written and easy to follow. The proposed method is novel and effective, and the experiments are extensive and convincing.

**********

---

**AC:** [Yuhao Zhou](https://yuhaozhou.org/)

**********

---

## Paper Decision Discussion

### justification_for_why_not_higher_score

The paper lacks some ablation studies and experiments.

### justification_for_why_not_lower_score

The paper is well-written and easy to follow. The proposed method is novel and effective, and the experiments are extensive and convincing.

**********

---

**AC:** [Yuhao Zhou](https://yuhaozhou.org/)

**********

---

## Paper Decision Discussion

### justification_for_why_not_higher_score

The paper lacks some ablation studies and experiments.

### justification_for_why_not_lower_score

The paper is well-written and easy to follow. The proposed method is novel and effective, and the experiments are extensive and convincing.

**********

---

**AC:** [Yuhao Zhou](https://yuhaozhou.org/)

**********

---

## Paper Decision Discussion

### justification_for_why_not_higher_score

The paper lacks some ablation studies and experiments.

### justification_for_why_not_lower_score

The paper is well-written and easy to follow. The proposed method is novel and effective, and the experiments are extensive and convincing.

**********

---

**AC:** [Yuhao Zhou](https://yuhaozhou.org/)

**********

---

## Paper Decision Discussion

### justification_for_why_not_higher_score

The paper lacks some ablation studies and experiments.

### justification_for_why_not_lower_score

The paper is well-written and easy to follow. The proposed method is novel and effective, and the experiments are extensive and convincing.

**********

---

**AC:** [Yuhao Zhou](https://yuhaozhou.org/)

**********

---

## Paper Decision Discussion

### justification_for_why_not_higher_score

The paper lacks some ablation studies and experiments.

### justification_for_why_not_lower_score

The paper is well-written and easy to follow. The proposed method is novel and effective, and the experiments are extensive and convincing.

**********

---

**AC:** [Yuhao Zhou](https://yuhaozhou.org/)

**********

---

## Paper Decision Discussion

### justification_for_why_not_higher_score

The paper lacks some ablation studies and experiments.

### justification_for_why_not_lower_score

The paper is well-written and easy to follow. The proposed method is novel and effective, and the experiments are extensive and convincing.

**********

---

**AC:** [Yuhao Zhou](https://yuhaozhou.org/)

**********

---

## Paper Decision Discussion

### justification_for_why_not_higher_score

The paper lacks some ablation studies and experiments.

### justification_for_why_not_lower_score

The paper is well-written and easy to follow. The proposed method is novel and effective, and the experiments are extensive and convincing.

**********

---

**AC:** [Yuhao Zhou](https://yuhaozhou.org/)

**********

---

## Paper Decision Discussion

### justification_for_why_not_higher_score

The paper lacks some ablation studies and experiments.

### justification_for_why_not_lower_score

The paper is well-written and easy to follow. The proposed method is novel and effective, and the experiments are extensive and convincing.

**********

---

**AC:** [Yuhao Zhou](https://yuhaozhou.org/)

**********

---

## Paper Decision Discussion

### justification_for_why_not_higher_score

The paper lacks some ablation studies and experiments.

### justification_for_why_not_lower_score

The paper is well-written and easy to follow. The proposed method is novel and effective, and the experiments are extensive and convincing.

**********

---

**AC:** [Yuhao Zhou](https://yuhaozhou.org/)

**********

---

## Paper Decision Discussion

### justification_for_why_not_higher_score

The paper lacks some ablation studies and experiments.

### justification_for_why_not_lower_score

The paper is well-written and easy to follow. The proposed method is novel and effective, and the experiments are extensive and convincing.

**********

---

**AC:** [Yuhao Zhou](https://yuhaozhou.org/)

**********

---

## Paper Decision Discussion

### justification_for_why_not_higher_score

The paper lacks some ablation studies and experiments.

### justification_for_why_not_lower_score

The paper is well-written and easy to follow. The proposed method is novel and effective, and the experiments are extensive and convincing.

**********

---

**AC:** [Yuhao Zhou](https://yuhaozhou.org/)

**********

---

## Paper Decision Discussion

### justification_for_why_not_higher_score

The paper lacks some ablation studies and experiments.

### justification_for_why_not_lower_score

The paper is well-written and easy to follow. The proposed method is novel and effective, and the experiments are extensive and convincing.

**********

---

**AC:** [Yuhao Zhou](https://yuhaozhou.org/)

**********

---

## Paper Decision Discussion

### justification_for_why_not_higher_score

The paper lacks some ablation studies and experiments.

### justification_for_why_not_lower_score

The paper is well-written and easy to follow. The proposed method is novel and effective, and the experiments are extensive and convincing.

**********

---

**AC:** [Yuhao Zhou](https://yuhaozhou.org/)

**********

---

## Paper Decision Discussion

### justification_for_why_not_higher_score

The paper lacks some ablation studies and experiments.

### justification_for_why_not_lower_score

The paper is well-written and easy to follow. The proposed method is novel and effective, and the experiments are extensive and convincing.

**********

---

**AC:** [Yuhao Zhou](https://yuhaozhou.org/)

**********

---

## Paper Decision Discussion

### justification_for_why_not_higher_score

The paper lacks some ablation studies and experiments.

### justification_for_why_not_lower_score

The paper is well-written and easy to follow. The proposed method is novel and effective, and the experiments are extensive and convincing.

**********

---

**AC:** [Yuhao Zhou](https://yuhaozhou.org/)

**********

---

## Paper Decision Discussion

### justification_for_why_not_higher_score

The paper lacks some ablation studies and experiments.

### justification_for_why_not_lower_score

The paper is well-written and easy to follow. The proposed method is novel and effective, and the experiments are extensive and convincing.

**********

---

**AC:** [Yuhao Zhou](https://yuhaozhou.org/)

**********

---

## Paper Decision Discussion

### justification_for_why_not_higher_score

The paper lacks some ablation studies and experiments.

### justification_for_why_not_lower_score

The paper is well-written and easy to follow. The proposed method is novel and effective, and the experiments are extensive and convincing.

**********

---

**AC:** [Yuhao Zhou](https://yuhaozhou.org/)

**********

---

## Paper Decision Discussion

### justification_for_why_not_higher_score

The paper lacks some ablation studies and experiments.

### justification_for_why_not_lower_score

The paper is well-written and easy to follow. The proposed method is novel and effective, and the experiments are extensive and convincing.

**********

---

**AC:** [Yuhao Zhou](https://yuhaozhou.org/)

**********

---

## Paper Decision Discussion

### justification_for_why_not_higher_score

The paper lacks some ablation studies and experiments.

### justification_for_why_not_lower_score

The paper is well-written and easy to follow. The proposed method is novel and effective, and the experiments are extensive and convincing.

**********

---

**AC:** [Yuhao Zhou](https://yuhaozhou.org/)

**********

---

## Paper Decision Discussion

### justification_for_why_not_higher_score

The paper lacks some ablation studies and experiments.

### justification_for_why_not_lower_score

The paper is well-written and easy to follow. The proposed method is novel and effective, and the experiments are extensive and convincing.

**********

---

**AC:** [Yuhao Zhou](https://yuhaozhou.org/)

**********

---

## Paper Decision Discussion

### justification_for_why_not_higher_score

The paper lacks some ablation studies and experiments.

### justification_for_why_not_lower_score

The paper is well-written and easy to follow. The proposed method is novel and effective, and the experiments are extensive and convincing.

**********

---

**AC:** [Yuhao Zhou](https://yuhaozhou.org/)

**********

---

## Paper Decision Discussion

### justification_for_why_not_higher_score

The paper lacks some ablation studies and experiments.

### justification_for_why_not_lower_score

The paper is well-written and easy to follow. The proposed method is novel and effective, and the experiments are extensive and convincing.

**********

---

**AC:** [Yuhao Zhou](https://yuhaozhou.org/)

**********

---

## Paper Decision Discussion

### justification_for_why_not_higher_score

The paper lacks some ablation studies and experiments.

### justification_for_why_not_lower_score

The paper is well-written and easy to follow. The proposed method is novel and effective, and the experiments are extensive and convincing.

**********

---

**AC:** [Yuhao Zhou](https://yuhaozhou.org/)

**********

---

## Paper Decision Discussion

### justification_for_why_not_higher_score

The paper lacks some ablation studies and experiments.

### justification_for_why_not_lower_score

The paper is well-written and easy to follow. The proposed method is novel and effective, and the experiments are extensive and convincing.

**********

---

**AC:** [Yuhao Zhou](https://yuhaozhou.org/)

**********

---

## Paper Decision Discussion

### justification_for_why_not_higher_score

The paper lacks some ablation studies and experiments.

### justification_for_why_not_lower_score

The paper is well-written and easy to follow. The proposed method is novel and effective, and the experiments are extensive and convincing.

**********

---

**AC:** [Yuhao Zhou](https://yuhaozhou.org/)

**********

---

## Paper Decision Discussion

### justification_for_why_not_higher_score

The paper lacks some ablation studies and experiments.

### justification_for_why_not_lower_score

The paper is well-written and easy to follow. The proposed method is novel and effective, and the experiments are extensive and convincing.

**********

---

**AC:** [Yuhao Zhou](https://yuhaozhou.org/)

**********

---

## Paper Decision Discussion

### justification_for_why_not_higher_score

The paper lacks some ablation studies and experiments.

### justification_for_why_not_lower_score

The paper is well-written and easy to follow. The proposed method is novel and effective, and the experiments are extensive and convincing.

**********

---

**AC:** [Yuhao Zhou](https://yuhaozhou.org/)

**********

---

## Paper Decision Discussion

### justification_for_why_not_higher_score

The paper lacks some ablation studies and experiments.

### justification_for_why_not_lower_score

The paper is well-written and easy to follow. The proposed method is novel and effective, and the experiments are extensive and convincing.

**********

---

**AC:** [Yuhao Zhou](https://yuhaozhou.org/)

**********

---

## Paper Decision Discussion

### justification_for_why_not_higher_score

The paper lacks some ablation studies and experiments.

### justification_for_why_not_lower_score

The paper is well-written and easy to follow. The proposed method is novel and effective, and the experiments are extensive and convincing.

**********

---

**AC:** [Yuhao Zhou](https://yuhaozhou.org/)

**********

---

## Paper Decision Discussion

### justification_for_why_not_higher_score

The paper lacks some ablation studies and experiments.

### justification_for_why_not_lower_score

The paper is well-written and easy to follow. The proposed method is novel and effective, and the experiments are extensive and convincing.

**********

---

**AC:** [Yuhao Zhou](https://yuhaozhou.org/)

**********

---

## Paper Decision Discussion

### justification_for_why_not_higher_score

The paper lacks some ablation studies and experiments.

### justification_for_why_not_lower_score

The paper is well-written and easy to follow. The proposed method is novel and effective, and the experiments are extensive and convincing.

**********

---

**AC:** [Yuhao Zhou](https://yuhaozhou.org/)

**********

---

## Paper Decision Discussion

### justification_for_why_not_higher_score

The paper lacks some ablation studies and experiments.

### justification_for_why_not_lower_score

The paper is well-written and easy to follow. The proposed method is novel and effective, and the experiments are extensive and convincing.

**********

---

**AC:** [Yuhao Zhou](https://yuhaozhou.org/)

**********

---

## Paper Decision Discussion

### justification_for_why_not_higher_score

The paper lacks some ablation studies and experiments.

### justification_for_why_not_lower_score

The paper is well-written and easy to follow. The proposed method is novel and effective, and the experiments are extensive and convincing.

**********

---

**AC:** [Yuhao Zhou](https://yuhaozhou.org/)

**********

---

## Paper Decision Discussion

### justification_for_why_not_higher_score

The paper lacks some ablation studies and experiments.

### justification_for_why_not_lower_score

The paper is well-written and easy to follow. The proposed method is novel and effective, and the experiments are extensive and convincing.

**********

---

**AC:** [Yuhao Zhou](https://yuhaozhou.org/)

**********

---

## Paper Decision Discussion

### justification_for_why_not_higher_score

The paper lacks some ablation studies and experiments.

### justification_for_why_not_lower_score

The paper is well-written and easy to follow. The proposed method is novel and effective, and the experiments are extensive and convincing.

**********

---

**AC:** [Yuhao Zhou](https://yuhaozhou.org/)

**********

---

## Paper Decision Discussion

### justification_for_why_not_higher_score

The paper lacks some ablation studies and experiments.

### justification_for_why_not_lower_score

The paper is well-written and easy to follow. The proposed method is novel and effective, and the experiments are extensive and convincing.

**********

---

**AC:** [Yuhao Zhou](https://yuhaozhou.org/)

**********

---

## Paper Decision Discussion

### justification_for_why_not_higher_score

The paper lacks some ablation studies and experiments.

### justification_for_why_not_lower_score

The paper is well-written and easy to follow. The proposed method is novel and effective, and the experiments are extensive and convincing.

**********

---

**AC:** [Yuhao Zhou](https://yuhaozhou.org/)

**********

---

## Paper Decision Discussion

### justification_for_why_not_higher_score

The paper lacks some ablation studies and experiments.

### justification_for_why_not_lower_score

The paper is well-written and easy to follow. The proposed method is novel and effective, and the experiments are extensive and convincing.

**********

---

**AC:** [Yuhao Zhou](https://yuhaozhou.org/)

**********

---

## Paper Decision Discussion

### justification_for_why_not_higher_score

The paper lacks some ablation studies and experiments.

### justification_for_why_not_lower_score

The paper is well-written and easy to follow. The proposed method is novel and effective, and the experiments are extensive and convincing.

**********

---

**AC:** [Yuhao Zhou](https://yuhaozhou.org/)

**********

---

## Paper Decision Discussion

### justification_for_why_not_higher_score

The paper lacks some ablation studies and experiments.

### justification_for_why_not_lower_score

The paper is well-written and easy to follow. The proposed method is novel and effective, and the experiments are extensive and convincing.

**********

---

**AC:** [Yuhao Zhou](https://yuhaozhou.org/)

**********

---

## Paper Decision Discussion

### justification_for_why_not_higher_score

The paper lacks some ablation studies and experiments.

### justification_for_why_not_lower_score

The paper is well-written and easy to follow. The proposed method is novel and effective, and the experiments are extensive and convincing.

**********

---

**AC:** [Yuhao Zhou](https://yuhaozhou.org/)

**********

---

## Paper Decision Discussion

### justification_for_why_not_higher_score

The paper lacks some ablation studies and experiments.

### justification_for_why_not_lower_score

The paper is well-written and easy to follow. The proposed method is novel and effective, and the experiments are extensive and convincing.

**********

---

**AC:** [Yuhao Zhou](https://yuhaozhou.org/)

**********

---

## Paper Decision Discussion

### justification_for_why_not_higher_score

The paper lacks some ablation studies and experiments.

### justification_for_why_not_lower_score

The paper is well-written and easy to follow. The proposed method is novel and effective, and the experiments are extensive and convincing.

**********

---

**AC:** [Yuhao Zhou](https://yuhaozhou.org/)

**********

---

## Paper Decision Discussion

### justification_for_why_not_higher_score

The paper lacks some ablation studies and experiments.

### justification_for_why_not_lower_score

The paper is well-written and easy to follow. The proposed method is novel and effective, and the experiments are extensive and convincing.

**********

---

**AC:** [Yuhao Zhou](https://yuhaozhou.org/)

**********

---

## Paper Decision Discussion

### justification_for_why_not_higher_score

The paper lacks some ablation studies and experiments.

### justification_for_why_not_lower_score

The paper is well-written and easy to follow. The proposed method is novel and effective, and the experiments are extensive and convincing.

**********

---

**AC:** [Yuhao Zhou](https://yuhaozhou.org/)

**********

---

## Paper Decision Discussion

### justification_for_why_not_higher_score

The paper lacks some ablation studies and experiments.

### justification_for_why_not_lower_score

The paper is well-written and easy to follow. The proposed method is novel and effective, and the experiments are extensive and convincing.

**********

---

**AC:** [Yuhao Zhou](https://yuhaozhou.org/)

**********

---

## Paper Decision Discussion

### justification_for_why_not_higher_score

The paper lacks some ablation studies and experiments.

### justification_for_why_not_lower_score

The paper is well-written and easy to follow. The proposed method is novel and effective, and the experiments are extensive and convincing.

**********

---

**AC:** [Yuhao Zhou](https://yuhaozhou.org/)

**********

---

## Paper Decision Discussion

### justification_for_why_not_higher_score

The paper lacks some ablation studies and experiments.

### justification_for_why_not_lower_score

The paper is well-written and easy to follow. The proposed method is novel and effective, and the experiments are extensive and convincing.

**********

---

**AC:** [Yuhao Zhou](https://yuhaozhou.org/)

**********

---

## Paper Decision Discussion

### justification_for_why_not_higher_score

The paper lacks some ablation studies and experiments.

### justification_for_why_not_lower_score

The paper is well-written and easy to follow. The proposed method is novel and effective, and the experiments are extensive and convincing.

**********

---

**AC:** [Yuhao Zhou](https://yuhaozhou.org/)

**********

---

## Paper Decision Discussion

### justification_for_why_not_higher_score

The paper lacks some ablation studies and experiments.

### justification_for_why_not_lower_score

The paper is well-written and easy to follow. The proposed method is novel and effective, and the experiments are extensive and convincing.

**********

---

**AC:** [Yuhao Zhou](https://yuhaozhou.org/)

**********

---

## Paper Decision Discussion

### justification_for_why_not_higher_score

The paper lacks some ablation studies and experiments.

### justification_for_why_not_lower_score

The paper is well-written and easy to follow. The proposed method is novel and effective, and the experiments are extensive and convincing.

**********

---

**AC:** [Yuhao Zhou](https://yuhaozhou.org/)

**********

---

## Paper Decision Discussion

### justification_for_why_not_higher_score

The paper lacks some ablation studies and experiments.

### justification_for_why_not_lower_score

The paper is well-written and easy to follow. The proposed method is novel and effective, and