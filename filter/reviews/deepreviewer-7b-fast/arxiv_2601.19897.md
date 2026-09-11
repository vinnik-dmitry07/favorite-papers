Of course. I will use Fast Mode for quick thinking. As a professional reviewer, I will directly output a detailed evaluation of this paper. Let me think - Fast Mode means I will directly output a Summary, followed by scores for Soundness, Presentation and Contribution, then provide analysis of Strengths, Weaknesses, Suggestions, and Questions. Finally, I will output the Rating, Confidence and Decision:

\boxed_review{
## Summary:

This paper introduces Self-Distillation Fine-Tuning (SDFT), a novel approach for continual learning in large language models (LLMs) that leverages in-context learning for on-policy learning. SDFT is designed to address the limitations of traditional supervised fine-tuning (SFT) and reinforcement learning (RL) methods in continual learning. The method involves using a teacher model, which is the base model conditioned on expert demonstrations, to generate training signals for a student model that is conditioned only on the task prompt. The paper demonstrates that SDFT outperforms SFT and DFT in both skill learning and knowledge acquisition tasks, while maintaining higher in-distribution accuracy and lower out-of-distribution errors. The authors also show that SDFT can be used to train reasoning models without explicit reasoning data, and that it can be combined with offline distillation methods to further improve performance. However, the paper's claims about the method's efficiency and its ability to handle complex behavioral shifts are not fully supported by the experimental results, and there are several areas where the methodology and presentation could be improved.


## Soundness:

2.75


## Presentation:

3.0


## Contribution:

2.75


## Strengths:

The paper makes several significant contributions to the field of continual learning in LLMs. Firstly, the introduction of SDFT as a method that uses in-context learning for on-policy learning is a novel and promising approach. The authors provide a clear and well-structured explanation of the method, including the teacher-student framework and the token-level loss function. This method is particularly innovative because it leverages the in-context learning capabilities of LLMs to generate training signals, which is a departure from traditional SFT and RL methods that rely on explicit reward functions or external data. The paper also demonstrates the effectiveness of SDFT in both skill learning and knowledge acquisition tasks, showing that it outperforms SFT and DFT in terms of in-distribution accuracy and reduces catastrophic forgetting. The empirical results are robust and well-supported, with detailed ablation studies and comparisons to relevant baselines. Additionally, the paper's exploration of using SDFT to train reasoning models without explicit reasoning data is a valuable contribution, as it addresses a practical challenge in the deployment of LLMs. The authors also provide a theoretical justification for the method, linking it to the concept of trust-region-regularized RL, which adds depth to the understanding of SDFT's behavior. Overall, the paper's core contributions and empirical findings are strong and well-supported, making it a valuable addition to the literature on continual learning in LLMs.


## Weaknesses:

Despite the paper's strengths, several limitations and concerns are evident. One of the primary concerns is the lack of a detailed analysis of the computational costs associated with SDFT. The paper mentions that SDFT requires approximately 2.5 times the computational cost in FLOPs and roughly 4 times the wall-clock training time compared to SFT, but it does not provide a breakdown of the computational overhead for each step of the process, such as the forward pass for the teacher model, the backward pass for the student model, and the distillation loss calculation. This omission makes it difficult to assess the practical feasibility of SDFT, especially in resource-constrained environments. Furthermore, the paper does not explore the trade-offs between computational cost and performance, which is crucial for understanding the method's scalability and efficiency. Another significant concern is the limited exploration of the method's performance on more complex behavioral shifts. The paper demonstrates SDFT's effectiveness in single-task and multi-task continual learning scenarios, but it does not include experiments that involve more substantial changes in the model's behavior, such as adapting to new domains or styles. This limitation is particularly important because the ability to handle complex behavioral shifts is a key requirement for true continual learning. The paper also lacks a thorough comparison with other state-of-the-art continual learning methods, such as prompt-based learning and parameter isolation techniques. While the paper compares SDFT to SFT, DFT, and Re-invocation, it does not include these other methods, which are relevant and widely used in the field. This omission makes it challenging to fully understand the relative strengths and weaknesses of SDFT. Additionally, the paper's claim that SDFT can be combined with offline distillation methods to further improve performance is not well-supported. The authors show that SDFT outperforms offline distillation, but they do not provide a detailed analysis of how SDFT's on-policy nature contributes to this improvement. This lack of clarity undermines the paper's argument for the unique benefits of SDFT. The paper also does not provide a clear definition of the term 'on-policy' in the context of SDFT, which can lead to confusion. While the term is explained in the introduction, a more explicit definition would enhance the paper's clarity. Moreover, the paper's discussion of the relationship between SDFT and on-policy RL is not sufficiently detailed. The authors acknowledge that SDFT is not an alternative to on-policy RL but highlight the differences in supervision assumptions and computational costs. However, a deeper exploration of these differences and their implications would strengthen the paper's theoretical foundation. The paper also lacks a comprehensive discussion of the limitations of SDFT, particularly in scenarios where the teacher model's output is not sufficiently diverse or informative. This is a critical aspect that needs to be addressed to provide a balanced view of the method's applicability. Finally, the paper's presentation could be improved by including more detailed explanations of the experimental setup and results, as well as a more thorough discussion of the implications of the findings. The inclusion of additional experiments, such as those involving more complex behavioral shifts or comparisons with a broader range of continual learning methods, would also enhance the paper's overall impact.


## Suggestions:

To address the identified limitations, I recommend several concrete and actionable improvements. First, the paper should provide a detailed analysis of the computational costs associated with SDFT. This should include a breakdown of the FLOPs and wall-clock time for each step of the process, such as the forward pass for the teacher model, the backward pass for the student model, and the distillation loss calculation. The authors should also explore the trade-offs between computational cost and performance, which would help readers understand the practical feasibility of the method. Second, the paper should include experiments that specifically test the method's ability to handle complex behavioral shifts. This could involve scenarios where the model needs to adapt to new domains, styles, or tasks that are significantly different from the original training data. By demonstrating SDFT's performance in these challenging settings, the authors can provide a more comprehensive evaluation of its capabilities. Third, the paper should conduct a more thorough comparison with other state-of-the-art continual learning methods, such as prompt-based learning and parameter isolation techniques. This comparison should include both performance metrics and computational costs, allowing readers to better understand the relative strengths and weaknesses of SDFT. Fourth, the authors should provide a more detailed analysis of how SDFT's on-policy nature contributes to its performance gains when combined with offline distillation methods. This could involve ablation studies that isolate the effects of the on-policy learning and the offline distillation components. Fifth, the paper should include a clear definition of the term 'on-policy' in the context of SDFT, which would enhance the paper's clarity and accessibility. Sixth, the authors should explore the potential of combining SDFT with other continual learning techniques, such as replay buffers or regularization methods, to further improve its performance and robustness. This could involve experiments that integrate SDFT with these methods and analyze the resulting performance gains. Seventh, the paper should provide a more in-depth discussion of the limitations of SDFT, particularly in scenarios where the teacher model's output is not sufficiently diverse or informative. This could include experiments that test the method's performance with varying levels of teacher quality and diversity. Finally, the paper should include a more detailed discussion of the implications of the findings, including potential future research directions and practical applications of SDFT. The inclusion of additional experiments and a more thorough analysis of the method's strengths and weaknesses would significantly enhance the paper's overall impact and provide a more balanced view of its contributions.


## Questions:

1. Could the authors provide a detailed breakdown of the computational costs associated with SDFT, including the FLOPs and wall-clock time for each step of the process? This would help readers understand the practical feasibility of the method, especially in resource-constrained environments.
2. How does SDFT perform in scenarios involving more complex behavioral shifts, such as adapting to new domains, styles, or tasks that are significantly different from the original training data? Are there specific types of shifts where SDFT excels or struggles?
3. Could the authors include a comparison of SDFT with other state-of-the-art continual learning methods, such as prompt-based learning and parameter isolation techniques? This would provide a more comprehensive evaluation of the method's relative strengths and weaknesses.
4. How does the on-policy nature of SDFT contribute to its performance gains when combined with offline distillation methods? Could the authors provide ablation studies that isolate the effects of the on-policy learning and the offline distillation components?
5. What is the precise definition of 'on-policy' in the context of SDFT, and how does it differ from the standard definition in reinforcement learning? This would enhance the paper's clarity and accessibility.
6. Could the authors explore the potential of combining SDFT with other continual learning techniques, such as replay buffers or regularization methods? What are the expected performance gains and computational costs of such combinations?
7. How does SDFT handle scenarios where the teacher model's output is not sufficiently diverse or informative? Are there specific types of tasks or datasets where SDFT might struggle, and how can these limitations be addressed?
8. What are the implications of the findings for future research in continual learning? Could the authors discuss potential avenues for extending SDFT to handle more complex tasks or to integrate it with other learning paradigms?


## Rating:

6.25


## Confidence:

3.25


## Decision:

Accept
}