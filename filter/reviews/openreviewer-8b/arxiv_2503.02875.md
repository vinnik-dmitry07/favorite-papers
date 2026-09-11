# Review

## Summary
This paper introduces Unsupervised Prefix Fine-Tuning (UPFT), a novel method to enhance the reasoning capabilities of large language models (LLMs) without relying on labeled data or computationally expensive sampling. The key insight is that different solution paths for the same problem often share a consistent initial reasoning phase, which the authors term "Prefix Self-Consistency." By fine-tuning only on the initial tokens of these solution paths (the prefix), the method guides the model towards more structured reasoning without the need for extensive data filtering. The authors demonstrate that UPFT matches the performance of supervised methods like Rejection Sampling Fine-Tuning (RFT) while reducing training time by 75% and sampling cost by 99%. The paper also shows that errors in reasoning tend to occur in the later stages, and that prefix-based training preserves the model's structural knowledge. The method is evaluated on four reasoning benchmarks using three different LLM architectures, showing its effectiveness and efficiency across various datasets and models.

## Soundness
3

## Presentation
3

## Contribution
3

## Strengths
1. The paper introduces a novel method, UPFT, that leverages the Prefix Self-Consistency phenomenon to improve LLMs' reasoning capabilities without requiring labeled data or extensive sampling. This approach is innovative in its focus on the initial tokens of solution trajectories, providing a new direction for unsupervised fine-tuning.
2. The paper provides a comprehensive set of experiments across four reasoning benchmarks and three different LLM architectures, demonstrating the robustness and generalizability of the proposed method. The authors compare UPFT with both unsupervised and supervised baselines, showing its competitive performance and efficiency gains. The experiments are well-designed and cover a range of scenarios, including both unsupervised and supervised sampling settings.
3. The paper is well-written and clearly structured, with a logical flow from the introduction to the methodology, experiments, and conclusions. The authors provide detailed explanations of the proposed method and the experimental setup, making it easy for readers to understand the methodology and results. Figures and tables are used effectively to illustrate key points and comparisons.

## Weaknesses
1. The paper could benefit from a more detailed discussion of the limitations of the proposed method. While the authors mention that errors tend to occur in the later stages of reasoning, a deeper exploration of how this might impact real-world applications and potential mitigation strategies would strengthen the paper. Including a section on the limitations and future directions would provide a more balanced perspective.
2. The paper could provide more insight into the interpretability of the learned representations and how the prefix fine-tuning affects the model's reasoning process. A qualitative analysis of the model's behavior or a case study of how UPFT handles a challenging reasoning task would help readers gain a better understanding of the method's inner workings.
3. The paper could benefit from a more detailed comparison with other recent methods in unsupervised learning and self-improvement. While the authors compare with RFT and SFT, including a broader range of baselines would provide a more comprehensive evaluation of the proposed method's effectiveness.

## Questions
1. How does the performance of UPFT vary with different prefix lengths, and are there optimal lengths for different types of reasoning tasks?
2. How does the method handle cases where the initial reasoning phases of different solution paths diverge significantly?
3. Can the authors provide more details on the computational efficiency gains of UPFT, including training time, memory usage, and scalability?
4. How does UPFT compare with other recent methods in unsupervised learning and self-improvement, such as self-rewarding or other prefix-based learning approaches?
5. Are there specific types of reasoning tasks or domains where UPFT is particularly effective or less effective, and what are the authors' hypotheses for these observations?
6. How does the method handle cases where the model generates incorrect prefixes that still lead to correct answers?
7. Can the authors provide more insight into how UPFT affects the model's interpretability and whether it learns more structured or consistent reasoning patterns?

## Flag For Ethics Review
No ethics review needed.

## Details Of Ethics Concerns


## Rating
6

## Confidence
4