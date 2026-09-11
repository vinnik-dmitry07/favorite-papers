## Reviewer

### Summary

The paper introduces a novel reliability signal, prefix consistency, for weighted majority voting (WMV) in large language models (LLMs). The authors observe that correct reasoning traces tend to be more reproducible under regeneration than incorrect ones. They propose to truncate each sample's Chain-of-Thought (CoT) and regenerate the continuation from the prefix, and use the reproduction rate as a reliability signal. The proposed method, prefix-consistency-weighted majority voting (PC-WMV), outperforms existing WMV baselines in terms of AUROC and cost-efficiency across multiple benchmarks and LLMs.

### Soundness

2 fair

### Presentation

2 fair

### Contribution

2 fair

### Strengths

1. The proposed method is simple and easy to understand.
2. The proposed method is effective in improving the performance of LLMs on reasoning tasks.

### Weaknesses

1. The paper lacks sufficient analysis of the proposed method. For example, the paper does not provide any theoretical analysis of the proposed method. The authors only show that the reproduction rate is higher for correct answers than for incorrect answers. However, it is not clear why this is the case or how it leads to the proposed method. It would be helpful to provide a more detailed analysis of the proposed method.
2. The paper does not provide a clear explanation of the empirical results. For example, the paper shows that the proposed method outperforms existing WMV baselines in terms of AUROC and cost-efficiency. However, it is not clear why this is the case. It would be helpful to provide a more detailed analysis of the empirical results.
3. The paper does not provide any ablation studies. For example, the paper does not show the effect of the hyperparameters of the proposed method. It would be helpful to provide an ablation study to show the effect of the hyperparameters.

### Questions

1. Why is the reproduction rate higher for correct answers than for incorrect answers?
2. How does the proposed method compare to other methods that use log-probabilities as a reliability signal?
3. How does the proposed method compare to other methods that use verbalized signals as a reliability signal?

### Flag For Ethics Review

No ethics review needed.

### Rating

5: marginally below the acceptance threshold

### Confidence

2: You are willing to defend your assessment, but it is quite likely that you did not understand the central parts of the submission or that you are unfamiliar with some pieces of related work. Math/other details were not carefully checked.

**********

## Reviewer

### Summary

This paper proposes a new reliability signal for weighted majority voting (WMV) in LLMs. The idea is to truncate the chain-of-thought (CoT) at a certain fraction of the tokens and regenerate the continuation from the prefix. The reproduction rate is then used as a reliability signal to weight the votes. The proposed method, prefix-consistency-weighted majority voting (PC-WMV), outperforms existing WMV baselines in terms of AUROC and cost-efficiency across multiple benchmarks and LLMs.

### Soundness

3 good

### Presentation

3 good

### Contribution

2 fair

### Strengths

1. The proposed method is simple and easy to understand.
2. The proposed method is effective in improving the performance of LLMs on reasoning tasks.
3. The paper is well-written and easy to follow.

### Weaknesses

1. The paper lacks sufficient analysis of the proposed method. For example, the paper does not provide any theoretical analysis of the proposed method. The authors only show that the reproduction rate is higher for correct answers than for incorrect answers. However, it is not clear why this is the case or how it leads to the proposed method. It would be helpful to provide a more detailed analysis of the proposed method.
2. The paper does not provide a clear explanation of the empirical results. For example, the paper shows that the proposed method outperforms existing WMV baselines in terms of AUROC and cost-efficiency. However, it is not clear why this is the case. It would be helpful to provide a more detailed analysis of the empirical results.
3. The paper does not provide any ablation studies. For example, the paper does not show the effect of the hyperparameters of the proposed method. It would be helpful to provide an ablation study to show the effect of the hyperparameters.

### Questions

1. Why is the reproduction rate higher for correct answers than for incorrect answers?
2. How does the proposed method compare to other methods that use log-probabilities as a reliability signal?
3. How does the proposed method compare to other methods that use verbalized signals as a reliability signal?

### Flag For Ethics Review

No ethics review needed.

### Rating

5: marginally below the acceptance threshold

### Confidence

2: You are willing to defend your assessment, but it is quite likely that you did not understand the central parts of the submission or that you are unfamiliar with some pieces of related work. Math/other details were not carefully checked.

**********

## Reviewer

### Summary

The paper proposes a novel reliability signal for weighted majority voting (WMV) in large language models (LLMs). The authors observe that correct reasoning traces tend to be more reproducible under regeneration than incorrect ones. They propose to truncate each sample's Chain-of-Thought (CoT) and regenerate the continuation from the prefix, and use the reproduction rate as a reliability signal. The proposed method, prefix-consistency-weighted majority voting (PC-WMV), outperforms existing WMV baselines in terms of AUROC and cost-efficiency across multiple benchmarks and LLMs.

### Soundness

3 good

### Presentation

3 good

### Contribution

3 good

### Strengths

1. The paper is well-written and easy to follow.
2. The proposed method is simple and easy to understand.
3. The proposed method is effective in improving the performance of LLMs on reasoning tasks.
4. The paper provides a comprehensive evaluation of the proposed method on multiple benchmarks and LLMs.

### Weaknesses

1. The paper lacks sufficient analysis of the proposed method. For example, the paper does not provide any theoretical analysis of the proposed method. The authors only show that the reproduction rate is higher for correct answers than for incorrect answers. However, it is not clear why this is the case or how it leads to the proposed method. It would be helpful to provide a more detailed analysis of the proposed method.
2. The paper does not provide a clear explanation of the empirical results. For example, the paper shows that the proposed method outperforms existing WMV baselines in terms of AUROC and cost-efficiency. However, it is not clear why this is the case. It would be helpful to provide a more detailed analysis of the empirical results.
3. The paper does not provide any ablation studies. For example, the paper does not show the effect of the hyperparameters of the proposed method. It would be helpful to provide an ablation study to show the effect of the hyperparameters.

### Questions

1. Why is the reproduction rate higher for correct answers than for incorrect answers?
2. How does the proposed method compare to other methods that use log-probabilities as a reliability signal?
3. How does the proposed method compare to other methods that use verbalized signals as a reliability signal?

### Flag For Ethics Review

No ethics review needed.

### Rating

5: marginally below the acceptance threshold

### Confidence

2: You are willing to defend your assessment, but it is quite likely that you did not understand the central parts of the submission or that you are unfamiliar with some pieces of related work. Math/other details were not carefully checked.

**********

## Reviewer

### Summary

The paper proposes a new reliability signal for weighted majority voting (WMV) in LLMs, which is based on the observation that correct reasoning traces tend to be more reproducible under regeneration than incorrect ones. The proposed method, prefix-consistency-weighted majority voting (PC-WMV), outperforms existing WMV baselines in terms of AUROC and cost-efficiency across multiple benchmarks and LLMs.

### Soundness

3 good

### Presentation

3 good

### Contribution

3 good

### Strengths

1. The paper is well-written and easy to follow.
2. The proposed method is simple and easy to understand.
3. The proposed method is effective in improving the performance of LLMs on reasoning tasks.
4. The paper provides a comprehensive evaluation of the proposed method on multiple benchmarks and LLMs.

### Weaknesses

1. The paper lacks sufficient analysis of the proposed method. For example, the paper does not provide any theoretical analysis of the proposed method. The authors only show that the reproduction rate is higher for correct answers than for incorrect answers. However, it is not clear why this is the case or how it leads to the proposed method. It would be helpful to provide a more detailed analysis of the proposed method.
2. The paper does not provide a clear explanation of the empirical results. For example, the paper shows that the proposed method outperforms existing WMV baselines in terms of AUROC and cost-efficiency. However, it is not clear why this is the case. It would be helpful to provide a more detailed analysis of the empirical results.
3. The paper does not provide any ablation studies. For example, the paper does not show the effect of the hyperparameters of the proposed method. It would be helpful to provide an ablation study to show the effect of the hyperparameters.

### Questions

1. Why is the reproduction rate higher for correct answers than for incorrect answers?
2. How does the proposed method compare to other methods that use log-probabilities as a reliability signal?
3. How does the proposed method compare to other methods that use verbalized signals as a reliability signal?

### Flag For Ethics Review

No ethics review needed.

### Rating

5: marginally below the acceptance threshold

### Confidence

2: You are willing to defend your assessment, but it is quite likely that you did not understand the central parts of the submission or that you are unfamiliar with some pieces of related work. Math/other details were not carefully checked.

**********

## Meta Review

The paper proposes a new reliability signal for weighted majority voting (WMV) in large language models (LLMs). The authors observe that correct reasoning traces tend to be more reproducible under regeneration than incorrect ones. They propose to truncate each sample's Chain-of-Thought (CoT) and regenerate the continuation from the prefix, and use the reproduction rate as a reliability signal. The proposed method, prefix-consistency-weighted majority voting (PC-WMV), outperforms existing WMV baselines in terms of AUROC and cost-efficiency across multiple benchmarks and LLMs.

The reviewers raised several concerns regarding the paper, including the lack of theoretical analysis, insufficient analysis of the proposed method, and limited explanation of the empirical results. The authors provided some additional results and analysis in the author response, but the reviewers still have concerns about the paper's novelty and significance. The reviewers also suggested that the paper could benefit from a more detailed analysis of the proposed method and a more comprehensive evaluation of the proposed method on multiple benchmarks and LLMs. Overall, the reviewers are not convinced that the paper meets the standards for acceptance.

### justification_for_why_not_higher_score

The reviewers raised several concerns regarding the paper, including the lack of theoretical analysis, insufficient analysis of the proposed method, and limited explanation of the empirical results. The authors provided some additional results and analysis in the author response, but the reviewers still have concerns about the paper's novelty and significance. The reviewers also suggested that the paper could benefit from a more detailed analysis of the proposed method and a more comprehensive evaluation of the proposed method on multiple benchmarks and LLMs. Overall, the reviewers are not convinced that the paper meets the standards for acceptance.

### justification_for_why_not_lower_score

N/A

**********

## Paper Decision

Reject (not selected for publication)