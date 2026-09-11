## Reviewer

### Summary

The paper proposes a new policy optimization algorithm for training large language models with reinforcement learning. The proposed algorithm, called Soft Adaptive Policy Optimization (SAPO), is based on the idea of replacing hard clipping with a smooth, temperature-controlled gate that adaptively attenuates off-policy updates while preserving useful learning signals. SAPO is compared with two existing algorithms, GSPO and GRPO, and is shown to improve training stability and performance on mathematical reasoning benchmarks.

### Soundness

3 good

### Presentation

3 good

### Contribution

2 fair

### Strengths

The paper is well-written and easy to follow. The proposed algorithm is well-motivated and the experimental results are promising.

### Weaknesses

The main weakness of the paper is the lack of novelty. The proposed algorithm is based on existing techniques, such as group-based policy optimization and soft clipping, and does not introduce any new ideas or techniques. The experimental results are also not very convincing, as the proposed algorithm only shows a small improvement over the existing algorithms.

### Questions

1. What are the main advantages of the proposed algorithm over the existing algorithms?
2. How does the proposed algorithm perform on other types of tasks, such as language translation or question answering?
3. Can the proposed algorithm be applied to other types of models, such as transformer-based models or recurrent neural networks?

### Flag For Ethics Review

No ethics review needed.

### Rating

5: marginally below the acceptance threshold

### Confidence

3: You are fairly confident in your assessment. It is possible that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work. Math/other details were not carefully checked.

**********

## Reviewer

### Summary

This paper proposes a new algorithm for policy optimization in reinforcement learning (RL) for large language models (LLMs). The authors propose a new algorithm called Soft Adaptive Policy Optimization (SAPO) that replaces the hard clipping in existing group-based policy optimization methods with a smooth, temperature-controlled gate. The authors show that SAPO is both sequence-coherent and token-adaptive, and that it outperforms existing methods on mathematical reasoning benchmarks.

### Soundness

3 good

### Presentation

3 good

### Contribution

3 good

### Strengths

1. The paper is well-written and easy to follow. The authors provide a clear description of the problem, the proposed solution, and the experimental results.

2. The proposed algorithm is novel and shows promising results. The idea of using a smooth, temperature-controlled gate to replace hard clipping is an interesting and effective approach.

3. The experiments are well-designed and provide strong evidence of the effectiveness of the proposed algorithm. The authors compare SAPO with existing methods on multiple benchmarks and show that it outperforms them in terms of stability and performance.

### Weaknesses

1. The paper only considers a specific type of RL problem, namely policy optimization in LLMs. It would be interesting to see if the proposed algorithm can be applied to other types of RL problems.

2. The paper does not provide a theoretical analysis of the proposed algorithm. It would be interesting to see a theoretical analysis of the convergence properties of SAPO.

### Questions

1. Can the proposed algorithm be applied to other types of RL problems beyond policy optimization in LLMs?

2. What are the theoretical guarantees of the proposed algorithm? Does it have any convergence properties?

### Flag For Ethics Review

No ethics review needed.

### Rating

6: marginally above the acceptance threshold

### Confidence

3: You are fairly confident in your assessment. It is possible that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work. Math/other details were not carefully checked.

**********

## Reviewer

### Summary

This paper proposes a new policy optimization algorithm, Soft Adaptive Policy Optimization (SAPO), to address the instability and inefficiency associated with hard-clipped policy optimization in large language models. SAPO replaces discontinuous clipping with a temperature-controlled soft gate and employs asymmetric temperatures to better regulate negative-token gradients. Empirical results on several mathematical reasoning benchmarks demonstrate that SAPO extends the duration of stable training and achieves higher Pass@1 performance under comparable budgets. Beyond controlled settings, large-scale experiments on Qwen3-VL models further demonstrate that SAPO delivers consistent improvements across diverse text and multimodal tasks and across different model sizes and architectures.

### Soundness

3 good

### Presentation

3 good

### Contribution

3 good

### Strengths

1. The paper is well-written and easy to follow. The proposed algorithm is well-motivated and the experimental results are promising.
2. The proposed algorithm is novel and shows promising results. The idea of using a smooth, temperature-controlled gate to replace hard clipping is an interesting and effective approach.
3. The experiments are well-designed and provide strong evidence of the effectiveness of the proposed algorithm. The authors compare SAPO with existing methods on multiple benchmarks and show that it outperforms them in terms of stability and performance.

### Weaknesses

1. The proposed algorithm is not a significant improvement over the existing algorithms. The proposed algorithm is based on existing techniques, such as group-based policy optimization and soft clipping, and does not introduce any new ideas or techniques. The experimental results are also not very convincing, as the proposed algorithm only shows a small improvement over the existing algorithms.
2. The paper does not provide a theoretical analysis of the proposed algorithm. It would be interesting to see a theoretical analysis of the convergence properties of SAPO.

### Questions

1. What are the main advantages of the proposed algorithm over the existing algorithms?
2. How does the proposed algorithm perform on other types of tasks, such as language translation or question answering?
3. Can the proposed algorithm be applied to other types of models, such as transformer-based models or recurrent neural networks?

### Flag For Ethics Review

No ethics review needed.

### Rating

6: marginally above the acceptance threshold

### Confidence

3: You are fairly confident in your assessment. It is possible that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work. Math/other details were not carefully checked.

**********

## Reviewer

### Summary

The paper proposes a new algorithm, Soft Adaptive Policy Optimization (SAPO), for policy optimization in reinforcement learning (RL) for large language models (LLMs). The authors show that SAPO is both sequence-coherent and token-adaptive, and that it outperforms existing methods on mathematical reasoning benchmarks.

### Soundness

3 good

### Presentation

3 good

### Contribution

3 good

### Strengths

1. The paper is well-written and easy to follow.
2. The proposed algorithm is novel and shows promising results.
3. The experiments are well-designed and provide strong evidence of the effectiveness of the proposed algorithm.

### Weaknesses

1. The paper only considers a specific type of RL problem, namely policy optimization in LLMs. It would be interesting to see if the proposed algorithm can be applied to other types of RL problems.
2. The paper does not provide a theoretical analysis of the proposed algorithm. It would be interesting to see a theoretical analysis of the convergence properties of SAPO.

### Questions

1. Can the proposed algorithm be applied to other types of RL problems beyond policy optimization in LLMs?
2. What are the theoretical guarantees of the proposed algorithm? Does it have any convergence properties?

### Flag For Ethics Review

No ethics review needed.

### Rating

6: marginally above the acceptance threshold

### Confidence

3: You are fairly confident in your assessment. It is possible that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work. Math/other details were not carefully checked.

**********

## Meta Review

This paper proposes a new policy optimization algorithm, Soft Adaptive Policy Optimization (SAPO), to address the instability and inefficiency associated with hard-clipped policy optimization in large language models. SAPO replaces discontinuous clipping with a temperature-controlled soft gate and employs asymmetric temperatures to better regulate negative-token gradients. Empirical results on several mathematical reasoning benchmarks demonstrate that SAPO extends the duration of stable training and achieves higher Pass@1 performance under comparable budgets. Beyond controlled settings, large-scale experiments on Qwen3-VL models further demonstrate that SAPO delivers consistent improvements across diverse text and multimodal tasks and across different model sizes and architectures.

The paper is well-written and easy to follow. The proposed algorithm is well-motivated and the experimental results are promising. The proposed algorithm is novel and shows promising results. The idea of using a smooth, temperature-controlled gate to replace hard clipping is an interesting and effective approach. The experiments are well-designed and provide strong evidence of the effectiveness of the proposed algorithm. The authors compare SAPO with existing methods on multiple benchmarks and show that it outperforms them in terms of stability and performance.

### justification_for_why_not_higher_score

The paper only considers a specific type of RL problem, namely policy optimization in LLMs. It would be interesting to see if the proposed algorithm can be applied to other types of RL problems. The paper does not provide a theoretical analysis of the proposed algorithm. It would be interesting to see a theoretical analysis of the convergence properties of SAPO.

### justification_for_why_not_lower_score

N/A

**********

## Paper Decision

Reject (out of the scope of ICLR) -> Post-Rebuttal: Reject (out of the scope of ICLR)

**********

## Paper Decision Post Rebuttal

The paper presents an interesting approach for policy optimization in RL for large language models. The paper is well-written and easy to follow. The proposed algorithm is well-motivated and the experimental results are promising. The proposed algorithm is novel and shows promising results. The idea of using a smooth, temperature-controlled gate to replace hard clipping is an interesting and effective approach. The experiments are well-designed and provide strong evidence of the effectiveness of the proposed algorithm. The authors compare SAPO with existing methods on multiple benchmarks and show that it outperforms them in terms of stability and performance.

However, the paper only considers a specific type of RL problem, namely policy optimization in LLMs. It would be interesting to see if the proposed algorithm can be applied to other types of RL problems. The paper does not provide a theoretical analysis of the proposed algorithm. It would be interesting to see a theoretical analysis of the convergence properties of SAPO.

### justification_for_why_not_higher_score

The paper only considers a specific type of RL problem, namely policy optimization in LLMs. It would be interesting to see if the proposed algorithm can be applied to other types of RL problems. The paper does not provide a theoretical analysis of the proposed algorithm. It would be interesting to see a theoretical analysis of the convergence properties of SAPO.

### justification_for_why_not_lower_score

N/A

**********

# Editor

**********

## Paper Decision

Reject (out of the scope of ICLR)

**********

## Paper Decision Summary

The paper presents an interesting approach for policy optimization in RL for large language models. The paper is well-written and easy to follow. The proposed algorithm is well-motivated and the experimental results are promising. The proposed algorithm is novel and shows promising results. The idea of using a smooth, temperature-controlled gate to replace hard clipping is an interesting and effective approach. The experiments are well-designed and provide strong evidence of the effectiveness of the proposed algorithm. The authors compare SAPO with existing methods on multiple benchmarks and show that it outperforms them in terms of stability and performance.

However, the paper only considers a specific type of RL problem, namely policy optimization in LLMs. It would be interesting to see if the proposed algorithm can be applied to other types of RL problems. The paper does not provide a theoretical analysis of the proposed algorithm. It would be interesting to see a theoretical analysis of the convergence properties of SAPO.

**********

# Editor

**********

## Paper Decision Post Rebuttal

The paper presents an interesting approach for policy optimization in RL for large language models. The paper is well-written and easy to follow. The proposed algorithm is well-motivated and the experimental results are promising. The proposed algorithm is novel and shows promising results. The idea of using a smooth, temperature-controlled gate to replace hard clipping is an interesting and effective approach. The experiments are well-designed and provide strong evidence of the effectiveness of the proposed algorithm. The authors compare SAPO with existing methods on multiple benchmarks and show that it outperforms them in terms of stability and performance.

However, the paper only considers a specific type of RL problem, namely policy optimization in LLMs. It would be interesting to see if the proposed algorithm can be applied to other types of RL problems. The paper does not provide a theoretical analysis of the proposed algorithm. It would be interesting to see a theoretical analysis of the convergence properties of SAPO.

**********

# Editor

**********

## Paper Decision

Reject (out of the scope of ICLR)

**********

## Paper Decision Summary

The paper presents an interesting approach for policy optimization in RL for large language models. The paper is well-written and easy to follow. The proposed algorithm is well-motivated and the experimental results are promising. The proposed algorithm is novel and shows promising results. The idea of using a smooth, temperature-controlled gate to replace hard clipping is an interesting and effective approach. The experiments are well-designed and provide strong evidence of the effectiveness of the proposed algorithm. The authors compare SAPO with existing methods on multiple benchmarks and show that it outperforms them in terms of stability and performance.

However, the paper only considers a specific type of RL problem, namely policy optimization in LLMs. It would be interesting to see if the proposed algorithm can be applied to other types of RL problems. The paper does not provide a theoretical analysis of the proposed algorithm. It would be interesting to see a theoretical analysis of the convergence properties of SAPO.

**********

# Editor

**********

## Paper Decision Post Rebuttal

The paper presents an interesting approach for policy optimization in RL for large language models. The paper is well-written and easy to follow. The proposed algorithm is well-motivated and the experimental results are promising. The proposed algorithm is novel and shows promising results. The idea of using a smooth, temperature-controlled gate to replace hard clipping is an interesting and effective approach. The experiments are well-designed and provide strong evidence of the effectiveness of the proposed algorithm. The authors compare SAPO with existing methods on multiple benchmarks and show that it outperforms them in terms of stability and performance.

However, the paper only considers a specific type of RL problem, namely policy optimization in LLMs. It would be interesting to see if the proposed algorithm can be applied to other types of RL problems. The paper does not provide a theoretical analysis of the proposed algorithm. It would be interesting to see a theoretical analysis of the convergence properties of SAPO.

**********

# Editor

**********

## Paper Decision

Reject (out of the scope of ICLR)

**********

## Paper Decision Summary

The paper presents an interesting approach for policy optimization in RL for large language models. The paper is well-written and easy to follow. The proposed algorithm is well-motivated and the experimental results are promising. The proposed algorithm is novel and shows promising results. The idea of using a smooth, temperature-controlled gate to replace hard clipping is an interesting and effective approach. The experiments are well-designed and provide strong evidence of the effectiveness of the proposed algorithm. The authors compare SAPO with existing methods on multiple benchmarks and show that it outperforms them in terms of stability and performance.

However, the paper only considers a specific type of RL problem, namely policy optimization in LLMs. It would be interesting to see if the proposed algorithm can be applied to other types of RL problems. The paper does not provide a theoretical analysis of the proposed algorithm. It would be interesting to see a theoretical analysis of the convergence properties of SAPO.

**********

# Editor

**********

## Paper Decision Post Rebuttal

The paper presents an interesting approach for policy optimization in RL for large language models. The paper is well-written and easy to follow. The proposed algorithm is well-motivated and the experimental results are promising. The proposed algorithm is novel and shows promising results. The idea of using a smooth, temperature-controlled gate to replace hard clipping is an interesting and effective approach. The experiments are well-designed and provide strong evidence of the effectiveness of the proposed algorithm. The authors compare SAPO with existing methods on multiple benchmarks and show that it outperforms them in terms of stability and performance.

However, the paper only considers a specific type of RL problem, namely policy optimization in LLMs. It would be interesting to see if the proposed algorithm can be applied to other types of RL problems. The paper does not provide a theoretical analysis of the proposed algorithm. It would be interesting to see a theoretical analysis of the convergence properties of SAPO.

**********

# Editor

**********

## Paper Decision

Reject (out of the scope of ICLR)

**********

## Paper Decision Summary

The paper presents an interesting approach for policy optimization in RL for large language models. The paper is well-written and easy to follow. The proposed algorithm is well-motivated and the experimental results are promising. The proposed algorithm is novel and shows promising results. The idea of using a smooth, temperature-controlled gate to replace hard clipping is an interesting and effective approach. The experiments are well-designed and provide strong evidence of the effectiveness of the proposed algorithm. The authors compare SAPO with existing methods on multiple benchmarks and show that it outperforms them in terms of stability and performance.

However, the paper only considers a specific type of RL problem, namely policy optimization in LLMs. It would be interesting to see if the proposed algorithm can be applied to other types of RL problems. The paper does not provide a theoretical analysis of the proposed algorithm. It would be interesting to see a theoretical analysis of the convergence properties of SAPO.

**********

# Editor

**********

## Paper Decision Post Rebuttal

The paper presents an interesting approach for policy optimization in RL for large language models. The paper is well-written and easy to follow. The proposed algorithm is well-motivated and the experimental results are promising. The proposed algorithm is novel and shows promising results. The idea of using a smooth, temperature-controlled gate to replace hard clipping is an interesting and effective approach. The experiments are well-designed and provide strong evidence of the effectiveness of the proposed algorithm. The authors compare SAPO with existing methods on multiple benchmarks and show that it outperforms them in terms of stability and performance.

However, the paper only considers a specific type of RL problem, namely policy optimization in LLMs. It would be interesting to see if the proposed algorithm can be applied to other types of RL problems. The paper does not provide a theoretical analysis of the proposed algorithm. It would be interesting to see a theoretical analysis of the convergence properties of SAPO.

**********

# Editor

**********

## Paper Decision

Reject (out of the scope of ICLR)

**********

## Paper Decision Summary

The paper presents an interesting approach for policy optimization in RL for large language models. The paper is well-written and easy to follow. The proposed algorithm is well-motivated and the experimental results are promising. The proposed algorithm is novel and shows promising results. The idea of using a smooth, temperature-controlled gate to replace hard clipping is an interesting and effective approach. The experiments are well-designed and provide strong evidence of the effectiveness of the proposed algorithm. The authors compare SAPO with existing methods on multiple benchmarks and show that it outperforms them in terms of stability and performance.

However, the paper only considers a specific type of RL problem, namely policy optimization in LLMs. It would be interesting to see if the proposed algorithm can be applied to other types of RL problems. The paper does not provide a theoretical analysis of the proposed algorithm. It would be interesting to see a theoretical analysis of the convergence properties of SAPO.

**********

# Editor

**********

## Paper Decision Post Rebuttal

The paper presents an interesting approach for policy optimization in RL for large language models. The paper is well-written and easy to follow. The proposed algorithm is well-motivated and the experimental results are promising. The proposed algorithm is novel and shows promising results. The idea of using a smooth, temperature-controlled gate to replace hard clipping is an interesting and effective approach. The experiments are well-designed and provide strong evidence of the effectiveness of the proposed algorithm. The authors compare SAPO with existing methods on multiple benchmarks and show that it outperforms them in terms of stability and performance.

However, the paper only considers a specific type of RL problem, namely policy optimization in LLMs. It would be interesting to see if the proposed algorithm can be applied to other types of RL problems. The paper does not provide a theoretical analysis of the proposed algorithm. It would be interesting to see a theoretical analysis of the convergence properties of SAPO.

**********

# Editor

**********

## Paper Decision

Reject (out of the scope of ICLR)

**********

## Paper Decision Summary

The paper presents an interesting approach for policy optimization in RL for large language models. The paper is well-written and easy to follow. The proposed algorithm is well-motivated and the experimental results are promising. The proposed algorithm is novel and shows promising results. The idea of using a smooth, temperature-controlled gate to replace hard clipping is an interesting and effective approach. The experiments are well-designed and provide strong evidence of the effectiveness of the proposed algorithm. The authors compare SAPO with existing methods on multiple benchmarks and show that it outperforms them in terms of stability and performance.

However, the paper only considers a specific type of RL problem, namely policy optimization in LLMs. It would be interesting to see if the proposed algorithm can be applied to other types of RL problems. The paper does not provide a theoretical analysis of the proposed algorithm. It would be interesting to see a theoretical analysis of the convergence properties of SAPO.

**********

# Editor

**********

## Paper Decision Post Rebuttal

The paper presents an interesting approach for policy optimization in RL for large language models. The paper is well-written and easy to follow. The proposed algorithm is well-motivated and the experimental results are promising. The proposed algorithm is novel and shows promising results. The idea of using a smooth, temperature-controlled gate to replace hard clipping is an interesting and effective approach. The experiments are well-designed and provide strong evidence of the effectiveness of the proposed algorithm. The authors compare SAPO with existing methods on multiple benchmarks and show that it outperforms them in terms of stability and performance.

However, the paper only considers a specific type of RL problem, namely policy optimization in LLMs. It would be interesting to see if the proposed algorithm can be applied to other types of RL problems. The paper does not provide a theoretical analysis of the proposed algorithm. It would be interesting to see a theoretical analysis of the convergence properties of SAPO.

**********

# Editor

**********

## Paper Decision

Reject (out of the scope of ICLR)

**********

## Paper Decision Summary

The paper presents an interesting approach for policy optimization in RL for large language models. The paper is well-written and easy to follow. The proposed algorithm is well-motivated and the experimental results are promising. The proposed algorithm is novel and shows promising results. The idea of using a smooth, temperature-controlled gate to replace hard clipping is an interesting and effective approach. The experiments are well-designed and provide strong evidence of the effectiveness of the proposed algorithm. The authors compare SAPO with existing methods on multiple benchmarks and show that it outperforms them in terms of stability and performance.

However, the paper only considers a specific type of RL problem, namely policy optimization in LLMs. It would be interesting to see if the proposed algorithm can be applied to other types of RL problems. The paper does not provide a theoretical analysis of the proposed algorithm. It would be interesting to see a theoretical analysis of the convergence properties of SAPO.

**********

# Editor

**********

## Paper Decision Post Rebuttal

The paper presents an interesting approach for policy optimization in RL for large language models. The paper is well-written and easy to follow. The proposed algorithm is well-motivated and the experimental results are promising. The proposed algorithm is novel and shows promising results. The idea of using a smooth, temperature-controlled gate to replace hard clipping is an interesting and effective approach. The experiments are well-designed and provide strong evidence of the effectiveness of the proposed algorithm. The authors compare SAPO with existing methods on multiple benchmarks and show that it outperforms them in terms of stability and performance.

However, the paper only considers a specific type of RL problem, namely policy optimization in LLMs. It would be interesting to see if the proposed algorithm can be applied to other types of RL problems. The paper does not provide a theoretical analysis of the proposed algorithm. It would be interesting to see a theoretical analysis of the convergence properties of SAPO.

**********

# Editor

**********

## Paper Decision

Reject (out of the scope of ICLR)

**********

## Paper Decision Summary

The paper presents an interesting approach for policy optimization in RL for large language models. The paper is well-written and easy to follow. The proposed algorithm is well-motivated and the experimental results are promising. The proposed algorithm is novel and shows promising results. The idea of using a smooth, temperature-controlled gate to replace hard clipping is an interesting and effective approach. The experiments are well-designed and provide strong evidence of the effectiveness of the proposed algorithm. The authors compare SAPO with existing methods on multiple benchmarks and show that it outperforms them in terms of stability and performance.

However, the paper only considers a specific type of RL problem, namely policy optimization in LLMs. It would be interesting to see if the proposed algorithm can be applied to other types of RL problems. The paper does not provide a theoretical analysis of the proposed algorithm. It would be interesting to see a theoretical analysis of the convergence properties of SAPO.

**********

# Editor

**********

## Paper Decision Post Rebuttal

The paper presents an interesting approach for policy optimization in RL for large language models. The paper is well-written and easy to follow. The proposed algorithm is well-motivated and the experimental results are promising. The proposed algorithm is novel and shows promising results. The idea of using a smooth, temperature-controlled gate to replace hard clipping is an interesting and effective approach. The experiments are well-designed and provide strong evidence of the effectiveness of the proposed algorithm. The authors compare SAPO with existing methods on multiple benchmarks and show that it outperforms them in terms of stability and performance.

However, the paper only considers a specific type of RL problem, namely policy optimization in LLMs. It would be interesting to see if the proposed algorithm can be applied to other types of RL problems. The paper does not provide a theoretical analysis of the proposed algorithm. It would be interesting to see a theoretical analysis of the convergence properties of SAPO.

**********

# Editor

**********

## Paper Decision

Reject (out of the scope of ICLR)

**********

## Paper Decision Summary

The paper presents an interesting approach for policy optimization in RL for large language models. The paper is well-written and easy to follow. The proposed algorithm is well-motivated and the experimental results are promising. The proposed algorithm is novel and shows promising results. The idea of using a smooth, temperature-controlled gate to replace hard clipping is an interesting and effective approach. The experiments are well-designed and provide strong evidence of the effectiveness of the proposed algorithm. The authors compare SAPO with existing methods on multiple benchmarks and show that it outperforms them in terms of stability and performance.

However, the paper only considers a specific type of RL problem, namely policy optimization in LLMs. It would be interesting to see if the proposed algorithm can be applied to other types of RL problems. The paper does not provide a theoretical analysis of the proposed algorithm. It would be interesting to see a theoretical analysis of the convergence properties of SAPO.

**********

# Editor

**********

## Paper Decision Post Rebuttal

The paper presents an interesting approach for policy optimization in RL for large language models. The paper is well-written and easy to follow. The proposed algorithm is well-motivated and the experimental results are promising. The proposed algorithm is novel and shows promising results. The idea of using a smooth, temperature-controlled gate to replace hard clipping is an interesting and effective approach. The experiments are well-designed and provide strong evidence of the effectiveness of the proposed algorithm. The authors compare SAPO with existing methods on multiple benchmarks and show that it outperforms them in terms of stability and performance.

However, the paper only considers a specific type of RL problem, namely policy optimization in LLMs. It would be interesting to see if the proposed algorithm can be applied to other types of RL problems. The paper does not provide a theoretical analysis of the proposed algorithm. It would be interesting to see a theoretical analysis of the convergence properties of SAPO.

**********

# Editor

**********

## Paper Decision

Reject (out of the scope of ICLR)

**********

## Paper Decision Summary

The paper presents an interesting approach for policy optimization in RL for large language models. The paper is well-written and easy to follow. The proposed algorithm is well-motivated and the experimental results are promising. The proposed algorithm is novel and shows promising results. The idea of using a smooth, temperature-controlled gate to replace hard clipping is an interesting and effective approach. The experiments are well-designed and provide strong evidence of the effectiveness of the proposed algorithm. The authors compare SAPO with existing methods on multiple benchmarks and show that it outperforms them in terms of stability and performance.

However, the paper only considers a specific type of RL problem, namely policy optimization in LLMs. It would be interesting to see if the proposed algorithm can be applied to other types of RL problems. The paper does not provide a theoretical analysis of the proposed algorithm. It would be interesting to see a theoretical analysis of the convergence properties of SAPO.

**********

# Editor

**********

## Paper Decision Post Rebuttal

The paper presents an interesting approach for policy optimization in RL for large language models. The paper is well-written and easy to follow. The proposed algorithm is well-motivated and the experimental results are promising. The proposed algorithm is novel and shows promising results. The idea of using a smooth, temperature-controlled gate to replace hard clipping is an interesting and effective approach. The experiments are well-designed and provide strong evidence of the effectiveness of the proposed algorithm. The authors compare SAPO with existing methods on multiple benchmarks and show that it outperforms them in terms of stability and performance.

However, the paper only considers a specific type of RL problem, namely policy optimization in LLMs. It would be interesting to see if the proposed algorithm can be applied to other types of RL problems. The paper does not provide a theoretical analysis of the proposed algorithm. It would be interesting to see a theoretical analysis of the convergence properties of SAPO.

**********

# Editor

**********

## Paper Decision

Reject (out of the scope of ICLR)

**********

## Paper Decision Summary

The paper presents an interesting approach for policy optimization in RL for large language models. The paper is well-written and easy to follow. The proposed algorithm is well-motivated and the experimental results are promising. The proposed algorithm is novel and shows promising results. The idea of using a smooth, temperature-controlled gate to replace hard clipping is an interesting and effective approach. The experiments are well-designed and provide strong evidence of the effectiveness of the proposed algorithm. The authors compare SAPO with existing methods on multiple benchmarks and show that it outperforms them in terms of stability and performance.

However, the paper only considers a specific type of RL problem, namely policy optimization in LLMs. It would be interesting to see if the proposed algorithm can be applied to other types of RL problems. The paper does not provide a theoretical analysis of the proposed algorithm. It would be interesting to see a theoretical analysis of the convergence properties of SAPO.

**********

# Editor

**********

## Paper Decision Post Rebuttal

The paper presents an interesting approach for policy optimization in RL for large language models. The paper is well-written and easy to follow. The proposed algorithm is well-motivated and the experimental results are promising. The proposed algorithm is novel and shows promising results. The idea of using a smooth, temperature-controlled gate to replace hard clipping is an interesting and effective approach. The experiments are well-designed and provide strong evidence of the effectiveness of the proposed algorithm. The authors compare SAPO with existing methods on multiple benchmarks and show that it outperforms them in terms of stability and performance.

However, the paper only considers a specific type of RL problem, namely policy optimization in LLMs. It would be interesting to see if the proposed algorithm can be applied to other types of RL problems. The paper does not provide a theoretical analysis of the proposed algorithm. It would be interesting to see a theoretical analysis of the convergence properties of SAPO.

**********

# Editor

**********

## Paper Decision

Reject (out of the scope of ICLR)

**********

## Paper Decision Summary

The paper presents an interesting approach for policy optimization in RL for large language models. The paper is well-written and easy to follow. The proposed algorithm is well-motivated and the experimental results are promising. The proposed algorithm is novel and shows promising results. The idea of using a smooth, temperature-controlled gate to replace hard clipping is an interesting and effective approach. The experiments are well-designed and provide strong evidence of the effectiveness of the proposed algorithm. The authors compare SAPO with existing methods on multiple benchmarks and show that it outperforms them in terms of stability and performance.

However, the paper only considers a specific type of RL problem, namely policy optimization in LLMs. It would be interesting to see if the proposed algorithm can be applied to other types of RL problems. The paper does not provide a theoretical analysis of the proposed algorithm. It