# Review

## Summary
This paper presents a new optimization algorithm, Lion, which is discovered by program search. The search process is guided by the evolutionary algorithm and funnel selection. The authors conduct extensive experiments to demonstrate the effectiveness of Lion.

## Soundness
3

## Presentation
3

## Contribution
3

## Strengths
1. The experiments are extensive and solid. The authors conduct experiments on various tasks, including image classification, contrastive learning, diffusion model training, and language modeling. The results show that Lion can achieve better performance than AdamW.
2. The authors provide a detailed analysis of Lion, which helps the readers to understand the algorithm better.

## Weaknesses
1. The search cost is still quite large. It takes 3K TPU V2 days to search for the algorithm.
2. The search space is quite limited. Currently, the discovered algorithms are still similar to existing optimization algorithms. It would be better if more novel algorithms can be discovered.

## Questions
1. In the abstract, the authors claim that Lion is more memory-efficient than Adam. Could you provide some numerical results to demonstrate this?
2. In Table 2, the performance of Lion and AdamW is quite close for ResNet-50 on ImageNet. Is it because Lion cannot work well for convolutional neural networks?
3. In Section 4.2, the authors conduct experiments on CLIP. What about GPT? Does Lion work well for large-scale language models?
4. In Section 4.3, the authors conduct experiments on diffusion models. What about some other models for image generation, such as Stable Diffusion?
5. In Section 4.4, the authors conduct experiments on language modeling and fine-tuning. What about some other tasks, such as object detection and segmentation?

## Flag For Ethics Review
No ethics review needed.

## Details Of Ethics Concerns


## Rating
6

## Confidence
4