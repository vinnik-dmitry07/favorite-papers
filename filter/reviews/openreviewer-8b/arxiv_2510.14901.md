# Review

## Summary
This paper proposes a training-free sampling algorithm that can improve the reasoning ability of LLMs. The proposed method is motivated by the observation that the distribution of the RLHF-tuned models is simply a sharpened version of the original model distribution. Therefore, the authors propose to sample from the power distribution $p^\alpha$ of the original model $p$ and design an Autoregressive MCMC algorithm to approximate sampling from $p^\alpha$. The authors conduct experiments on MATH500, HumanEval, GPQA, and AlpacaEval 2.0 to demonstrate the effectiveness of the proposed method.

## Soundness
3

## Presentation
3

## Contribution
3

## Strengths
1. The proposed method is training-free, which is a significant advantage over RLHF methods.
2. The authors provide a detailed analysis of the difference between the proposed method and the low-temperature sampling.
3. The authors conduct extensive experiments to demonstrate the effectiveness of the proposed method.

## Weaknesses
1. The authors claim that the distribution of the RLHF-tuned models is simply a sharpened version of the original model distribution. However, this claim is not supported by any reference or experimental evidence.
2. The proposed method is similar to the method proposed in [1], which is not cited in this paper.
3. The authors do not report the standard deviation of the results in Table 1.
4. The authors do not compare the proposed method with other training-free methods such as [2].

[1] Autoregressive Sampling for Diffusion Models. ICML 2024.

[2] Training-Free Prompt Tuning for Large Language Models. ICLR 2023.

## Questions
1. Could you provide experimental evidence for the claim that the distribution of the RLHF-tuned models is simply a sharpened version of the original model distribution?
2. What is the difference between the proposed method and the method in [1]?
3. Could you report the standard deviation of the results in Table 1?
4. Could you compare the proposed method with other training-free methods such as [2]?

## Flag For Ethics Review
No ethics review needed.

## Details Of Ethics Concerns


## Rating
6

## Confidence
4