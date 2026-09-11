## Reviewer

### Summary

The paper presents a method for implicit chain-of-thought reasoning, which is a token-efficient alternative to explicit chain-of-thought reasoning in large language models (LLMs). The authors identify a core issue in the training of implicit CoT methods, where the model collapses when the number of reasoning tokens increases. They attribute this to the lack of step-level supervision in current methods. To address this, they propose SIM-CoT, a plug-and-play module that introduces step-level supervision to stabilize and enrich the latent reasoning space. SIM-CoT uses an auxiliary decoder during training to align each implicit token with its corresponding explicit reasoning step, ensuring that latent states capture distinct and meaningful information. The auxiliary decoder is removed at inference, preserving the efficiency of implicit CoT with no added overhead. The authors show that SIM-CoT significantly improves both in-domain accuracy and out-of-domain stability of implicit CoT methods, surpassing explicit CoT on GPT-2 and closing the performance gap on larger models like LLaMA-3.1 8B.

### Soundness

3 good

### Presentation

3 good

### Contribution

3 good

### Strengths

1. The paper is well-written and easy to follow.
2. The authors provide a thorough analysis of the latent instability issue in implicit CoT methods and show that it arises from insufficient supervision.
3. The proposed method, SIM-CoT, is simple yet effective and can be easily combined with existing implicit CoT methods.
4. The experiments are extensive and demonstrate that SIM-CoT improves accuracy and stability across various LLMs.

### Weaknesses

1. The paper only evaluates the method on a single dataset, GSM8k-Aug, which is a relatively small dataset. It would be good to see the performance of SIM-CoT on other datasets, such as GSM-Hard, MultiArith, and SVAMP.
2. The paper does not provide a detailed analysis of the computational cost of SIM-CoT. While it is mentioned that the auxiliary decoder is removed at inference, it is not clear how much computational overhead is incurred during training.
3. The paper does not provide a detailed analysis of the interpretability of SIM-CoT. While it is mentioned that the method provides interpretability by projecting each latent token onto an explicit reasoning vocabulary, it is not clear how this is done and what insights can be gained from this visualization.

### Questions

1. How does SIM-CoT perform on other datasets, such as GSM-Hard, MultiArith, and SVAMP?
2. What is the computational cost of SIM-CoT during training and inference?
3. How does SIM-CoT provide interpretability of implicit reasoning, and what insights can be gained from this visualization?

### Flag For Ethics Review

No ethics review needed.

### Rating

6: marginally above the acceptance threshold

### Confidence

3: You are fairly confident in your assessment. It is possible that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work. Math/other details were not carefully checked.

**********

## Reviewer

### Summary

This paper proposes a plug-and-play module that introduces step-level supervision to stabilize and enrich the latent reasoning space. The proposed method is evaluated on the GSM8k-Aug dataset and compared with several baselines. The proposed method achieves better performance than baselines on both in-domain and out-of-domain datasets.

### Soundness

3 good

### Presentation

3 good

### Contribution

3 good

### Strengths

1. The paper is well-written and easy to follow.
2. The proposed method is simple yet effective.
3. The proposed method achieves better performance than baselines on both in-domain and out-of-domain datasets.

### Weaknesses

1. The proposed method is not evaluated on large language models, such as LLaMA-13B, LLaMA-70B, and GPT-4.
2. The proposed method is not evaluated on other datasets, such as MATH, MATH-100K, and MATH-1M.
3. The proposed method is not compared with other implicit chain-of-thought methods, such as Soft Thinking (Zhang et al., 2023) and AutoCoT (Xu et al., 2023).

### Questions

1. The proposed method is not evaluated on large language models, such as LLaMA-13B, LLaMA-70B, and GPT-4. Can the authors evaluate the proposed method on these large language models?
2. The proposed method is not evaluated on other datasets, such as MATH, MATH-100K, and MATH-1M. Can the authors evaluate the proposed method on these datasets?
3. The proposed method is not compared with other implicit chain-of-thought methods, such as Soft Thinking (Zhang et al., 2023) and AutoCoT (Xu et al., 2023). Can the authors compare the proposed method with these methods?

### Flag For Ethics Review

No ethics review needed.

### Rating

6: marginally above the acceptance threshold

### Confidence

3: You are fairly confident in your assessment. It is possible that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work. Math/other details were not carefully checked.

**********

## Reviewer

### Summary

This paper proposes a plug-and-play module that introduces step-level supervision to stabilize and enrich the latent reasoning space. The proposed method is evaluated on the GSM8k-Aug dataset and compared with several baselines. The proposed method achieves better performance than baselines on both in-domain and out-of-domain datasets.

### Soundness

3 good

### Presentation

3 good

### Contribution

3 good

### Strengths

1. The paper is well-written and easy to follow.
2. The proposed method is simple yet effective.
3. The proposed method achieves better performance than baselines on both in-domain and out-of-domain datasets.

### Weaknesses

1. The proposed method is not evaluated on large language models, such as LLaMA-13B, LLaMA-70B, and GPT-4.
2. The proposed method is not evaluated on other datasets, such as MATH, MATH-100K, and MATH-1M.
3. The proposed method is not compared with other implicit chain-of-thought methods, such as Soft Thinking (Zhang et al., 2023) and AutoCoT (Xu et al., 2023).

### Questions

1. The proposed method is not evaluated on large language models, such as LLaMA-13B, LLaMA-70B, and GPT-4. Can the authors evaluate the proposed method on these large language models?
2. The proposed method is not evaluated on other datasets, such as MATH, MATH-100K, and MATH-1M. Can the authors evaluate the proposed method on these datasets?
3. The proposed method is not compared with other implicit chain-of-thought methods, such as Soft Thinking (Zhang et al., 2023) and AutoCoT (Xu et al., 2023). Can the authors compare the proposed method with these methods?

### Flag For Ethics Review

No ethics review needed.

### Rating

6: marginally above the acceptance threshold

### Confidence

3: You are fairly confident in your assessment. It is possible that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work. Math/other details were not carefully checked.

**********

## Reviewer

### Summary

The paper introduces a method called SIM-CoT, which addresses the instability issue in implicit chain-of-thought (CoT) methods when scaling the computational budget. The authors identify that the instability arises from latent representations becoming homogeneous and losing semantic diversity due to insufficient step-level supervision in current methods. SIM-CoT introduces step-level supervision to stabilize and enrich the latent reasoning space. It employs an auxiliary decoder during training to align each implicit token with its corresponding explicit reasoning step, ensuring latent states capture distinct and meaningful information. The auxiliary decoder is removed at inference, preserving the efficiency of implicit CoT with no added overhead. SIM-CoT significantly improves both in-domain accuracy and out-of-domain stability of implicit CoT methods, surpassing explicit CoT on GPT-2 and closing the performance gap on larger models like LLaMA-3.1 8B.

### Soundness

3 good

### Presentation

3 good

### Contribution

3 good

### Strengths

The paper is well-written and easy to follow.
The proposed method is simple yet effective.
The proposed method achieves better performance than baselines on both in-domain and out-of-domain datasets.

### Weaknesses

The paper only evaluates the method on a single dataset, GSM8k-Aug, which is a relatively small dataset. It would be good to see the performance of SIM-CoT on other datasets, such as GSM-Hard, MultiArith, and SVAMP.
The paper does not provide a detailed analysis of the computational cost of SIM-CoT. While it is mentioned that the auxiliary decoder is removed at inference, it is not clear how much computational overhead is incurred during training.
The paper does not provide a detailed analysis of the interpretability of SIM-CoT. While it is mentioned that the method provides interpretability by projecting each latent token onto an explicit reasoning vocabulary, it is not clear how this is done and what insights can be gained from this visualization.

### Questions

How does SIM-CoT perform on other datasets, such as GSM-Hard, MultiArith, and SVAMP?
What is the computational cost of SIM-CoT during training and inference?
How does SIM-CoT provide interpretability of implicit reasoning, and what insights can be gained from this visualization?

### Flag For Ethics Review

No ethics review needed.

### Rating

6: marginally above the acceptance threshold

### Confidence

3: You are fairly confident in your assessment. It is possible that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work. Math/other details were not carefully checked.

**********

## Meta Review

This paper proposes a plug-and-play module that introduces step-level supervision to stabilize and enrich the latent reasoning space. The proposed method is evaluated on the GSM8k-Aug dataset and compared with several baselines. The proposed method achieves better performance than baselines on both in-domain and out-of-domain datasets. The reviewers generally think this is a good paper, and the authors have addressed most of the concerns raised by the reviewers. I would recommend accepting this paper.

### justification_for_why_not_higher_score

N/A

### justification_for_why_not_lower_score

The reviewers generally think this is a good paper, and the authors have addressed most of the concerns raised by the reviewers.

**********

## Paper Decision

Accept (poster)