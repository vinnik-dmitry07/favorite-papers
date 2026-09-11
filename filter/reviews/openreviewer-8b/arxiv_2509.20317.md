# Review

## Summary
This paper introduces SIM-CoT, a novel approach to enhance the performance of implicit Chain-of-Thought (CoT) methods in Large Language Models (LLMs). The authors identify a key limitation in existing implicit CoT models: as the number of reasoning tokens increases, the models often become unstable and collapse during training. This instability is attributed to the homogenization of latent representations, which lose semantic diversity due to insufficient step-level supervision. To address this, SIM-CoT incorporates an auxiliary decoder during training that aligns each implicit token with its corresponding explicit reasoning step, thereby enriching the latent reasoning space with step-level detail. This method improves both the in-domain accuracy and out-of-domain stability of implicit CoT approaches, demonstrating significant performance gains across various LLMs, including GPT-2 and LLaMA models.

## Soundness
3

## Presentation
3

## Contribution
3

## Strengths
1. The introduction of step-level supervision through an auxiliary decoder is a novel approach that addresses a critical gap in existing implicit CoT methods, improving both performance and stability.
2. The paper provides a thorough analysis of the latent instability issue in current implicit CoT models, offering clear evidence of how the proposed method resolves this problem.
3. The method is designed to be plug-and-play, easily integrating with existing implicit CoT approaches without additional inference overhead, making it practical for real-world application.
4. Extensive experiments across multiple benchmarks and model types demonstrate the robustness and effectiveness of SIM-CoT, showing consistent improvements over state-of-the-art methods.

## Weaknesses
1. While the method shows promising results on the selected benchmarks, its generalizability to other types of reasoning tasks beyond mathematical problems is not explored.
2. The paper could benefit from a more detailed discussion on the computational cost of training with the auxiliary decoder, especially for very large models.
3. The method assumes a fixed number of reasoning steps (K), which may limit the model's flexibility in adapting to problems with varying complexity.

## Questions
1. How does the performance of SIM-CoT vary with different choices of the number of implicit tokens? Is there an upper limit to the number of tokens that can be used before performance degrades?
2. Have you explored the potential of SIM-CoT for other types of reasoning tasks, such as logical reasoning or commonsense reasoning? What modifications would be necessary?
3. How does the training time and computational cost of SIM-CoT compare to other implicit CoT methods, particularly when scaling to very large models?

## Flag For Ethics Review
No ethics review needed.

## Details Of Ethics Concerns


## Rating
6

## Confidence
4