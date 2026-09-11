## Reviewer

### Summary

This paper proposes a new method for fine-tuning LLMs based on supervised fine-tuning (SFT), which is called dynamic fine-tuning (DFT). DFT is motivated by the fact that SFT can be viewed as a form of policy gradient with a sparse reward function, which is inversely proportional to the model's probability of expert actions. To rectify this, DFT rescales the SFT objective at each token by its probability, canceling the distortion introduced by inverse-probability weighting. The authors show that DFT outperforms SFT on multiple benchmarks and base models, and achieves competitive results in offline RL settings.

### Soundness

3 good

### Presentation

3 good

### Contribution

2 fair

### Strengths

- The paper is well-written and easy to follow.
- The proposed method is simple and easy to implement.
- The proposed method is effective in improving the generalization of SFT.

### Weaknesses

- The theoretical analysis in Section 3.2 is not very convincing. The authors claim that SFT can be viewed as a form of policy gradient with a sparse reward function, which is inversely proportional to the model's probability of expert actions. However, this is not a new observation. The authors should provide a more rigorous proof of this claim.
- The proposed method is only evaluated on a limited set of benchmarks and models. It is not clear how well the method will generalize to other tasks and models.
- The paper does not discuss the limitations of the proposed method. For example, how does the method perform on tasks that require memorization rather than generalization? How does the method perform when the expert demonstrations are noisy or incomplete?

### Questions

- Can the authors provide a more rigorous proof of the claim that SFT can be viewed as a form of policy gradient with a sparse reward function?
- Can the authors provide more results on different tasks and models?
- Can the authors discuss the limitations of the proposed method?

### Flag For Ethics Review

No ethics review needed.

### Rating

5: marginally below the acceptance threshold

### Confidence

3: You are fairly confident in your assessment. It is possible that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work. Math/other details were not carefully checked.

**********

## Reviewer

### Summary

The paper proposes a new method for fine-tuning LLMs called Dynamic Fine-Tuning (DFT). The main idea is to rescale the SFT objective at each token by its probability, which is claimed to cancel the distortion introduced by inverse-probability weighting. The authors show that DFT outperforms SFT on multiple benchmarks and base models, and achieves competitive results in offline RL settings.

### Soundness

2 fair

### Presentation

3 good

### Contribution

2 fair

### Strengths

1. The paper is well-written and easy to follow.
2. The proposed method is simple and easy to implement.
3. The proposed method is effective in improving the generalization of SFT.

### Weaknesses

1. The theoretical analysis in Section 3.2 is not very convincing. The authors claim that SFT can be viewed as a form of policy gradient with a sparse reward function, which is inversely proportional to the model's probability of expert actions. However, this is not a new observation. The authors should provide a more rigorous proof of this claim.
2. The proposed method is only evaluated on a limited set of benchmarks and models. It is not clear how well the method will generalize to other tasks and models.
3. The paper does not discuss the limitations of the proposed method. For example, how does the method perform on tasks that require memorization rather than generalization? How does the method perform when the expert demonstrations are noisy or incomplete?

### Questions

1. Can the authors provide a more rigorous proof of the claim that SFT can be viewed as a form of policy gradient with a sparse reward function?
2. Can the authors provide more results on different tasks and models?
3. Can the authors discuss the limitations of the proposed method?

### Flag For Ethics Review

No ethics review needed.

### Rating

5: marginally below the acceptance threshold

### Confidence

3: You are fairly confident in your assessment. It is possible that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work. Math/other details were not carefully checked.

**********

## Reviewer

### Summary

This paper presents a simple method to improve the generalization of supervised fine-tuning (SFT) for LLMs. The authors show that SFT can be viewed as a policy gradient with a sparse reward function, which is inversely proportional to the model's probability of expert actions. To improve the generalization of SFT, the authors propose Dynamic Fine-Tuning (DFT), which rescales the SFT objective at each token by its probability. The authors show that DFT outperforms SFT on multiple benchmarks and base models, and achieves competitive results in offline RL settings.

### Soundness

3 good

### Presentation

3 good

### Contribution

3 good

### Strengths

1. The paper is well-written and easy to follow.
2. The proposed method is simple and easy to implement.
3. The proposed method is effective in improving the generalization of SFT.
4. The theoretical analysis in Section 3.2 is interesting and insightful.

### Weaknesses

1. The authors should provide more results on different tasks and models.
2. The authors should discuss the limitations of the proposed method. For example, how does the method perform on tasks that require memorization rather than generalization? How does the method perform when the expert demonstrations are noisy or incomplete?

### Questions

1. Can the authors provide more results on different tasks and models?
2. Can the authors discuss the limitations of the proposed method?

### Flag For Ethics Review

No ethics review needed.

### Rating

6: marginally above the acceptance threshold

### Confidence

3: You are fairly confident in your assessment. It is possible that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work. Math/other details were not carefully checked.

**********

## Reviewer

### Summary

The paper presents a method to improve the generalization of supervised fine-tuning (SFT) for LLMs. The authors show that SFT can be viewed as a policy gradient with a sparse reward function, which is inversely proportional to the model's probability of expert actions. To improve the generalization of SFT, the authors propose Dynamic Fine-Tuning (DFT), which rescales the SFT objective at each token by its probability. The authors show that DFT outperforms SFT on multiple benchmarks and base models, and achieves competitive results in offline RL settings.

### Soundness

3 good

### Presentation

3 good

### Contribution

3 good

### Strengths

1. The paper is well-written and easy to follow.
2. The proposed method is simple and easy to implement.
3. The proposed method is effective in improving the generalization of SFT.
4. The theoretical analysis in Section 3.2 is interesting and insightful.

### Weaknesses

1. The authors should provide more results on different tasks and models.
2. The authors should discuss the limitations of the proposed method. For example, how does the method perform on tasks that require memorization rather than generalization? How does the method perform when the expert demonstrations are noisy or incomplete?

### Questions

1. Can the authors provide more results on different tasks and models?
2. Can the authors discuss the limitations of the proposed method?

### Flag For Ethics Review

No ethics review needed.

### Rating

6: marginally above the acceptance threshold

### Confidence

3: You are fairly confident in your assessment. It is possible that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work. Math/other details were not carefully checked.

**********

## Meta Review

This paper proposes a new method for fine-tuning LLMs based on supervised fine-tuning (SFT), which is called dynamic fine-tuning (DFT). The main idea is to rescale the SFT objective at each token by its probability, which is claimed to cancel the distortion introduced by inverse-probability weighting. The authors show that DFT outperforms SFT on multiple benchmarks and base models, and achieves competitive results in offline RL settings.

The reviewers generally agree that the paper is well-written and easy to follow. The proposed method is simple and easy to implement. The proposed method is effective in improving the generalization of SFT. However, the theoretical analysis in Section 3.2 is not very convincing. The authors should provide a more rigorous proof of this claim. The proposed method is only evaluated on a limited set of benchmarks and models. It is not clear how well the method will generalize to other tasks and models. The paper does not discuss the limitations of the proposed method. For example, how does the method perform on tasks that require memorization rather than generalization? How does the method perform when the expert demonstrations are noisy or incomplete?

### justification_for_why_not_higher_score

The theoretical analysis in Section 3.2 is not very convincing. The authors should provide a more rigorous proof of this claim. The proposed method is only evaluated on a limited set of benchmarks and models. It is not clear how well the method will generalize to other tasks and models. The paper does not discuss the limitations of the proposed method. For example, how does the method perform on tasks that require memorization rather than generalization? How does the method perform when the expert demonstrations are noisy or incomplete?

### justification_for_why_not_lower_score

N/A

**********

## Paper Decision

Reject (out of the scope of ICLR) → Reject (not good enough) (after discussion)

**********

## Paper Decision

Reject (not good enough)

**********

*Abstract*:

This paper presents a method to improve the generalization of supervised fine-tuning (SFT) for LLMs. The authors show that SFT can be viewed as a policy gradient with a sparse reward function, which is inversely proportional to the model's probability of expert actions. To improve the generalization of SFT, the authors propose Dynamic Fine-Tuning (DFT), which rescales the SFT objective at each token by its probability. The authors show that DFT outperforms SFT on multiple benchmarks and base models, and achieves competitive results in offline RL settings.

*Strengths*:

1. The paper is well-written and easy to follow.
2. The proposed method is simple and easy to implement.
3. The proposed method is effective in improving the generalization of SFT.
4. The theoretical analysis in Section 3.2 is interesting and insightful.

*Weaknesses*:

1. The theoretical analysis in Section 3.2 is not very convincing. The authors should provide a more rigorous proof of this claim.
2. The proposed method is only evaluated on a limited set of benchmarks and models. It is not clear how well the method will generalize to other tasks and models.
3. The paper does not discuss the limitations of the proposed method. For example, how does the method perform on tasks that require memorization rather than generalization? How does the method perform when the expert demonstrations are noisy or incomplete?

**********

## Paper Decision

Reject (not good enough)

**********

*Abstract*:

This paper presents a method to improve the generalization of supervised fine-tuning (SFT) for LLMs. The authors show that SFT can be viewed as a policy gradient with a sparse reward function, which is inversely proportional to the model's probability of expert actions. To improve the generalization of SFT, the authors propose Dynamic Fine-Tuning (DFT), which rescales the SFT objective at each token by its probability. The authors show that DFT outperforms SFT on multiple benchmarks and base models, and achieves competitive results in offline RL settings.

*Strengths*:

1. The paper is well-written and easy to follow.
2. The proposed method is simple and easy to implement.
3. The proposed method is effective in improving the generalization of SFT.
4. The theoretical analysis in Section 3.2 is interesting and insightful.

*Weaknesses*:

1. The theoretical analysis in Section 3.2 is not very convincing. The authors should provide a more rigorous proof of this claim.
2. The proposed method is only evaluated on a limited set of benchmarks and models. It is not clear how well the method will generalize to other tasks and models.
3. The paper does not discuss the limitations of the proposed method. For example, how does the method perform on tasks that require memorization rather than generalization? How does the method perform when the expert demonstrations are noisy or incomplete?

**********

### justification_for_why_not_higher_score

The theoretical analysis in Section 3.2 is not very convincing. The authors should provide a more rigorous proof of this claim. The proposed method is only evaluated on a limited set of benchmarks and models. It is not clear how well the method will generalize to other tasks and models. The paper does not discuss the limitations of the proposed method. For example, how does the method perform on tasks that require memorization rather than generalization? How does the method perform when the expert demonstrations are noisy or incomplete?

### justification_for_why_not_lower_score

N/A

**********

## Paper Decision

Reject (not good enough)

**********

**********

## Paper Decision

Reject (not good enough)

**********

**********

## Paper Decision

Reject (not good enough)

**********

**********

## Paper Decision

Reject (not good enough)

**********

## Paper Decision

Reject (not good enough)

**********

## Paper Decision

Reject (not good enough)

**********

## Paper Decision

Reject (not good enough)

**********

## Paper Decision

Reject (not good enough)

**********

## Paper Decision

Reject (not good enough)

**********

## Paper Decision

Reject (not good enough)

**********

## Paper Decision

Reject (not good enough)

**********

## Paper Decision

Reject (not good enough)

**********

## Paper Decision

Reject (not good enough)

**********

## Paper Decision

Reject (not good enough)

**********

## Paper Decision

Reject (not good enough)

**********

## Paper Decision

Reject (not good enough)

**********

## Paper Decision

Reject (not good enough)

**********

## Paper Decision

Reject (not good enough)

**********

## Paper Decision

Reject (not good enough)

**********

## Paper Decision

Reject (not good enough)

**********

## Paper Decision

Reject (not good enough)

**********

## Paper Decision

Reject (not good enough)

**********

## Paper Decision

Reject (not good enough)

**********

## Paper Decision

Reject (not good enough)

**********

## Paper Decision

Reject (not good enough)

**********

## Paper Decision

Reject (not good enough)

**********

## Paper Decision

Reject (not good enough)

**********

## Paper Decision

Reject (not good enough)

**********

## Paper Decision

Reject (not good enough)

**********

## Paper Decision

Reject (not good enough)

**********

## Paper Decision

Reject (not good enough)

**********

## Paper Decision

Reject (not good enough)

**********

## Paper Decision

Reject (not good enough)

**********

## Paper Decision

Reject (not good enough)

**********

## Paper Decision

Reject (not good enough)

**********

## Paper Decision

Reject (not good enough)

**********

## Paper Decision

Reject (not good enough)

**********

## Paper Decision

Reject (not good enough)

**********

## Paper Decision

Reject (not good enough)

**********

## Paper Decision

Reject (not good enough)

**********

## Paper Decision

Reject (not good enough)

**********

## Paper Decision

Reject (not good enough)

**********

## Paper Decision

Reject (not good enough)

**********

## Paper Decision

Reject (not good enough)

**********

## Paper Decision

Reject (not good enough)

**********

## Paper Decision

Reject (not good enough)

**********

## Paper Decision

Reject (not good enough)

**********

## Paper Decision

Reject (not good enough)

**********

## Paper Decision

Reject (not good enough)

**********

## Paper Decision

Reject (not good enough)

**********

## Paper Decision

Reject (not good enough)

**********

## Paper Decision

Reject (not good enough)

**********

## Paper Decision

Reject (not good enough)

**********

## Paper Decision

Reject (not good enough)

**********

## Paper Decision

Reject (not good enough)

**********

## Paper Decision

Reject (not good enough)

**********

## Paper Decision

Reject (not good enough)

**********

## Paper Decision

Reject (not good enough)

**********

## Paper Decision

Reject (not good enough)

**********

## Paper Decision

Reject (not good enough)

**********

## Paper Decision

Reject (not good enough)

**********

## Paper Decision

Reject (not good enough)

**********

## Paper Decision

Reject (not good enough)

**********

## Paper Decision

Reject (not good enough)

**********

## Paper Decision

Reject (not good enough)

**********

## Paper Decision

Reject (not good enough)

**********

## Paper Decision

Reject (not good enough)

**********

## Paper Decision

Reject (not good enough)

**********

## Paper Decision

Reject (not good enough)

**********

## Paper Decision

Reject (not good enough)

**********

## Paper Decision

Reject (not good enough)

**********

## Paper Decision

Reject (not good enough)

**********

## Paper Decision

Reject (not good enough)

**********

## Paper Decision

Reject (not good enough)

**********

## Paper Decision

Reject (not good enough)

**********

## Paper Decision

Reject (not good enough)

**********

## Paper Decision

Reject (not good enough)

**********

## Paper Decision

Reject (not good enough)

**********

## Paper Decision

Reject (not good enough)

**********

## Paper Decision

Reject (not good enough)

**********

## Paper Decision

Reject (not good enough)

**********

## Paper Decision

Reject (not good enough)

**********

## Paper Decision

Reject (not good enough)

**********

## Paper Decision

Reject (not good enough)

**********

## Paper Decision

Reject (not good enough)

**********

## Paper Decision

Reject (not good enough)

**********

## Paper Decision

Reject (not good enough)

**********

## Paper Decision

Reject (not good enough)

**********

## Paper Decision

Reject (not good enough)

**********

## Paper Decision

Reject (not good enough)

**********

## Paper Decision

Reject (not good enough)

**********

## Paper Decision

Reject (not good enough)

**********

## Paper Decision

Reject (not good enough)

**********

## Paper Decision

Reject (not good enough)

**********

## Paper Decision

Reject (not good enough)

**********

## Paper Decision

Reject (not good enough)

**********

## Paper Decision

Reject (not good enough)

**********

## Paper Decision

Reject (not good enough)

**********

## Paper Decision

Reject (not good enough)

**********

## Paper Decision

Reject (not good enough)

**********

## Paper Decision

Reject (not good enough)

**********

## Paper Decision

Reject (not good enough)

**********

## Paper Decision

Reject (not good enough)

**********

## Paper Decision

Reject (not good enough)

**********

## Paper Decision

Reject (not good enough)

**********

## Paper Decision

Reject (not good enough)

**********

## Paper Decision

Reject (not good enough)

**********

## Paper Decision

Reject (not good enough)

**********

## Paper Decision

Reject (not good enough)

**********

## Paper Decision

Reject (not good enough)

**********

## Paper Decision

Reject (not good enough)

**********

## Paper Decision

Reject (not good enough)

**********

## Paper Decision

Reject (not good enough)

**********

## Paper Decision

Reject (not good enough)

**********

## Paper Decision

Reject (not good enough)

**********

## Paper Decision

Reject (not good enough)

**********

## Paper Decision

Reject (not good enough)

**********

## Paper Decision

Reject (not good enough)

**********

## Paper Decision

Reject (not good enough)

**********

## Paper Decision

Reject (not good enough)

**********

## Paper Decision

Reject (not good enough)

**********

## Paper Decision

Reject (not good enough)

**********

## Paper Decision

Reject (not good enough)

**********

## Paper Decision

Reject (not good enough)

**********

## Paper Decision

Reject (not good enough)

**********

## Paper Decision

Reject (not good enough)

**********

## Paper Decision

Reject (not good enough)

**********

## Paper Decision

Reject (not good enough)

**********

## Paper Decision

Reject (not good enough)

**********

## Paper Decision

Reject (not good enough)

**********

## Paper Decision

Reject (not good enough)

**********

## Paper Decision

Reject (not good enough)

**********

## Paper Decision

Reject (not good enough)

**********

## Paper Decision

Reject (not good enough)

**********

## Paper Decision

Reject (not good enough)

**********

## Paper Decision

Reject (not good enough)

**********

## Paper Decision

Reject (not good enough)

**********

## Paper Decision

Reject (not good enough)

**********

## Paper Decision

Reject (not good enough)

**********

## Paper Decision

Reject (not good enough)

**********

## Paper Decision

Reject (not good enough)

**********

## Paper Decision

Reject (not good enough)

**********

## Paper Decision

Reject (not good enough)

**********

## Paper Decision

Reject (not good enough)

**********

## Paper Decision

Reject (not good enough)

**********

## Paper Decision

Reject (not good enough)

**********

## Paper Decision

Reject (not good enough)

**********

## Paper Decision

Reject (not good enough)

**********

## Paper Decision

Reject (not good enough)

**********

## Paper Decision

Reject (not good enough)

**********

## Paper Decision

Reject (not good enough)

**********

## Paper Decision

Reject (not good enough)

**********

## Paper Decision

Reject (not good enough)

**********

## Paper Decision

Reject (not good enough)

**********

## Paper Decision

Reject (not good enough)

**********

## Paper Decision

Reject (not good enough)

**********

## Paper Decision

Reject (not good enough)

**********

## Paper Decision

Reject (not good enough)

**********

## Paper Decision

Reject (not good enough)

**********

## Paper Decision

Reject (not good enough)

**********

## Paper Decision

Reject (not good enough)

**********

## Paper Decision

Reject (not good enough)

**********

## Paper Decision

Reject (not good enough)

**********

## Paper Decision

Reject (not good enough)

**********

## Paper Decision

Reject (not good enough)

**********

## Paper Decision

Reject (not good enough)

**********

## Paper Decision

Reject (not good enough)

**********

## Paper Decision

Reject (not good enough)

**********

## Paper Decision

Reject (not good enough)

**********

## Paper Decision

Reject (not good enough)

**********

## Paper Decision

Reject (not good enough)

**********

## Paper Decision

Reject (not good enough)

**********

## Paper Decision

Reject (not good enough)

**********

## Paper Decision

Reject (not good enough)

**********

## Paper Decision

Reject (not good enough)

**********

## Paper Decision

Reject (not good enough)

**********

## Paper Decision

Reject (not good enough)

**********

## Paper Decision

Reject (not good enough)

**********

## Paper Decision

Reject (not good enough)

**********

## Paper Decision

Reject (not good enough)

**********

## Paper Decision

Reject (not good enough)

**********

## Paper Decision

Reject (not good enough)

**********

## Paper Decision

Reject (not good enough)

**********

## Paper Decision

Reject (not good enough)

**********

## Paper Decision

Reject (not good enough)

**********

## Paper Decision

Reject (not good enough)

**********

## Paper Decision

Reject (not good enough)

**********

## Paper Decision

Reject (not good enough)

**********

## Paper Decision

Reject (not good enough)

**********

## Paper Decision

Reject (not good enough)

**********

## Paper Decision

Reject (not good enough)

**********

## Paper Decision

Reject (not good enough)

**********

## Paper Decision

Reject (not good enough)

**********

## Paper Decision

Reject (not good enough)

**********

## Paper Decision

Reject (not good enough)

**********

## Paper Decision

Reject (not good enough)

**********

## Paper Decision

Reject (not good enough)

**********

## Paper Decision

Reject (not good enough)

**********

## Paper Decision

Reject (not good enough)

**********

## Paper Decision

Reject (not good enough)

**********

## Paper Decision

Reject (not good enough)

**********

## Paper Decision

Reject (not good enough)

**********

## Paper Decision

Reject (not good enough)

**********

## Paper Decision

Reject (not good enough)

**********

## Paper Decision

Reject (not good enough)

**********

## Paper Decision

Reject (not good enough)

**********

## Paper Decision

Reject (not good enough)

**********

## Paper Decision

Reject (not good enough)

**********

## Paper Decision

Reject (not good enough)

**********

## Paper Decision

Reject (not good enough)

**********

## Paper Decision

Reject (not good enough)

**********

## Paper Decision

Reject (not good enough)

**********

## Paper Decision

Reject (not good enough)

**********

## Paper Decision

Reject (not good enough)

**********

## Paper Decision

Reject (not good enough)

**********

## Paper Decision

Reject (not good enough)

**********

## Paper Decision

Reject (not good enough)

**********

## Paper Decision

Reject (not good enough)

**********

## Paper Decision

Reject (not good enough)

**********

## Paper Decision

Reject (not good enough)

**********

## Paper Decision

Reject (not good enough)

**********

## Paper Decision

Reject (not good enough)

**********

## Paper Decision

Reject (not good enough)

**********

## Paper Decision

Reject (not good enough)

**********

## Paper Decision

Reject (not good enough)

**********

## Paper Decision

Reject (not good enough)

**********

## Paper Decision

Reject (not good enough)

**********

## Paper Decision

Reject (not good enough)

**********

## Paper Decision

Reject (not good enough)

**********

## Paper Decision

Reject (not good enough)

**********

## Paper Decision

Reject (not good enough)

**********

## Paper Decision

Reject (not good enough)

**********

## Paper Decision

Reject (not good enough)

**********

## Paper Decision

Reject (not good enough)

**********

## Paper Decision

Reject (not good enough)

**********

## Paper Decision

Reject (not good enough)

**********

## Paper Decision

Reject (not good enough)

**********

## Paper Decision

Reject (not good enough)

**********

## Paper Decision

Reject (not good enough)

**********

## Paper Decision

Reject (not good enough)

**********

## Paper Decision

Reject (not good enough)

**********

## Paper Decision

Reject (not good enough)

**********

## Paper Decision

Reject (not good enough)

**********

## Paper Decision

Reject (not good enough)

**********

## Paper Decision

Reject (not good enough)

**********

## Paper Decision

Reject (not good enough)

**********

## Paper Decision

Reject (not good enough)

**********

## Paper Decision

Reject (not good enough)

**********

## Paper Decision

Reject (not good enough)

**********

## Paper Decision

Reject (not good enough)

**********

## Paper Decision

Reject (not good enough)

**********

## Paper Decision

Reject (not good enough)

**********

## Paper Decision

Reject (not good enough)

**********

## Paper Decision

Reject (not good enough)

**********

## Paper Decision

Reject (not good enough)

**********

## Paper Decision

Reject (not good enough)

**********

## Paper Decision

Reject (not good enough)

**********

## Paper Decision

Reject (not good enough)

**********

## Paper Decision

Reject (not good enough)

**********

## Paper Decision

Reject (not good enough)

**********

## Paper Decision

Reject (not good enough)

**********

## Paper Decision

Reject (not good enough)

**********

## Paper Decision

Reject (not good enough)

**********

## Paper Decision

Reject (not good enough)

**********

## Paper Decision

Reject (not good enough)

**********

## Paper Decision

Reject (not good enough)

**********

## Paper Decision

Reject (not good enough)

**********

## Paper Decision

Reject (not good enough)

**********

## Paper Decision

Reject (not good enough)

**********

## Paper Decision

Reject (not good enough)

**********

## Paper Decision

Reject (not good enough)

**********

## Paper Decision

Reject (not good enough)

**********

## Paper Decision

Reject (not good enough)

**********

## Paper Decision

Reject (not good enough)

**********

## Paper Decision

Reject (not good enough)

**********

## Paper Decision

Reject (not good enough)

**********

## Paper Decision

Reject (not good enough)

**********

## Paper Decision

Reject (not good enough)

**********

## Paper Decision

Reject (not good enough)

**********

## Paper Decision

Reject (not good enough)

**********

## Paper Decision

Reject (not good enough)

**********

## Paper Decision

Reject (not good enough)

**********

## Paper Decision

Reject (not good enough)

**********

## Paper Decision

Reject (not good enough)

**********

## Paper Decision

Reject (not good enough)

**********

## Paper Decision

Reject (not good enough)

**********

## Paper Decision

Reject (not good enough)

**********

## Paper Decision

Reject (not good enough)

**********

## Paper Decision

Reject (not good enough)

**********

## Paper Decision

Reject (not good enough)

**********

## Paper Decision

Reject (not good enough)

**********

## Paper Decision

Reject (not good enough)

**********

## Paper Decision

Reject (not good enough)

**********

## Paper Decision

Reject (not good enough)

**********

## Paper Decision

Reject (not good enough)

**********

## Paper Decision

Reject (not good enough)

**********

## Paper Decision

Reject (not good enough)

**********

## Paper Decision

Reject (not good enough)

**********

## Paper Decision

Reject (not good enough)

**********

## Paper Decision

Reject (not good enough)

**********

## Paper Decision

Reject (not good enough)

**********

## Paper Decision

Reject (not good enough)

**********

## Paper Decision

Reject (not good enough)

**********

## Paper Decision

Reject (not good enough)

**********

## Paper Decision

Reject (not good enough)

**********

## Paper Decision

Reject (not good enough)

**********

## Paper Decision

Reject (not good enough)

**********

## Paper Decision

Reject (not good enough)

**********

## Paper Decision

Reject (not good enough)

**********

## Paper Decision

Reject (not good enough)

**********

## Paper Decision

Reject (not good enough)

**********

## Paper Decision

Reject (not good enough)

**********

## Paper Decision

Reject (not good enough)

**********

## Paper Decision

Reject (not good enough)

**********

## Paper Decision

Reject (not good enough)

**********

## Paper Decision

Reject (not good enough)

**********

## Paper Decision

Reject (not good enough)

**********

## Paper Decision

Reject (not good enough)

**********

## Paper Decision

Reject (not good enough)

**********

## Paper Decision

Reject (not good enough)

**********

## Paper Decision

Reject (not good enough)

**********

## Paper Decision

Reject (not good enough)

**********

## Paper Decision

Reject (not good enough)

**********

## Paper Decision

Reject (not good enough)

**********

## Paper Decision

Reject (not good enough)

**********

## Paper Decision

Reject (not good enough)

**********

## Paper Decision

Reject (not good enough)

**********

## Paper Decision

Reject (not good enough)

**********

## Paper Decision

Reject (not good enough)

**********

## Paper Decision

Reject (not good enough)

**********

## Paper Decision

Reject (not good enough)

**********

## Paper Decision

Reject (not good enough)

**********

## Paper Decision

Reject (not good enough)

**********

## Paper Decision

Reject (not good enough)

**********

## Paper Decision

Reject (not good enough)

**********

## Paper Decision

Reject (not good enough)

**********

## Paper Decision

Reject (not good enough)

**********

## Paper Decision

Reject (not good enough)

**********

## Paper Decision

Reject (not good enough)

**********

## Paper Decision

Reject (not good enough)

**********

## Paper Decision

Reject (not good enough)

**********

## Paper Decision

Reject (not good enough)

**********

## Paper Decision

Reject (not good enough)

**********

## Paper Decision

Reject (not good enough)

**********

## Paper Decision

Reject (not good enough)

**********

## Paper Decision

Reject (not good enough)

**********

## Paper Decision

Reject (not good enough)

**********

## Paper Decision

Reject (not good enough)

**********

## Paper Decision

Reject (not good