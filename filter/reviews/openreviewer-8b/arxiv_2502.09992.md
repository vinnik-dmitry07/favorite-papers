# Review

## Summary
This paper presents LLaDA, an 8B parameter diffusion model for language. The model is trained on 2.3T tokens and SFT on 4.5M pairs. The model shows comparable performance to Llama3 8B on a wide range of tasks.

## Soundness
3

## Presentation
3

## Contribution
3

## Strengths
- The paper is well-written and easy to follow.
- The results are strong, with the model showing comparable performance to Llama3 8B.
- The paper is the first to scale diffusion models to 8B parameters and 2.3T tokens, which is a significant achievement.
- The paper includes a detailed analysis of the model's capabilities, including its performance on reversal reasoning tasks, which are known to be challenging for autoregressive models.

## Weaknesses
- The paper does not compare the performance of LLaDA with other diffusion models, such as the one proposed in [1].
- The paper does not provide a detailed analysis of the computational requirements for training and inference of LLaDA. This information would be valuable for researchers interested in replicating the results or extending the work.
- The paper does not provide a detailed analysis of the impact of the forward process on the model's performance. Understanding how the forward process affects the model's ability to capture different aspects of language would be valuable for improving the model and for understanding its limitations.

[1] Austin, Jacob, et al. "A diffusion model for language generation." arXiv preprint arXiv:2205.14217 (2022).

## Questions
- How does the performance of LLaDA compare to other diffusion models, such as the one proposed in [1]?
- What are the computational requirements for training and inference of LLaDA? How does it compare to autoregressive models of similar size?
- How does the forward process affect the model's performance? Which types of language tasks benefit most from the forward process?
- Have you explored the use of classifier-free guidance (CFG) for improving the performance of LLaDA? If so, what were the results?
- Have you explored the use of reinforcement learning (RL) for improving the performance of LLaDA? If so, what were the results?

[1] Austin, Jacob, et al. "A diffusion model for language generation." arXiv preprint arXiv:2205.14217 (2022).

## Flag For Ethics Review
No ethics review needed.

## Details Of Ethics Concerns


## Rating
8

## Confidence
4