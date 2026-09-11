Of course. I will use Fast Mode for quick thinking. As a professional reviewer, I will directly output a detailed evaluation of this paper. Let me think - Fast Mode means I will directly output a Summary, followed by scores for Soundness, Presentation and Contribution, then provide analysis of Strengths, Weaknesses, Suggestions, and Questions. Finally, I will output the Rating, Confidence and Decision:

\boxed_review{
## Summary:

This paper introduces SC-GRPO, a novel method designed to improve token-level credit assignment in Reinforcement Learning with Verifiable Rewards (RLVR). The core challenge addressed is the inefficient credit allocation in existing methods like GRPO, where uniform credit is assigned regardless of the token's contribution to the final outcome. SC-GRPO tackles this by leveraging the KL divergence between a self-conditioned teacher model, trained on verified trajectories, and the student model. This divergence is used to weight the gradients in GRPO, effectively highlighting tokens that are highly sensitive to the correctness of the trajectory. The method is carefully constructed to avoid the pitfalls of simply averaging over multiple teacher-conditioned models, which could lead to a loss of valuable information. The authors present a clear and well-motivated approach, supported by a thorough theoretical analysis. Empirically, SC-GRPO demonstrates consistent improvements over GRPO and other baselines across a range of tasks, including mathematical reasoning, code generation, and agentic tasks. The paper also includes a detailed ablation study, which provides valuable insights into the importance of the different components of the method. The authors' approach is a significant step forward in addressing the challenges of credit assignment in RLVR, and their work has the potential to impact the development of more efficient and effective language models. The paper is well-written and easy to follow, making it accessible to a broad audience. The authors also provide a comprehensive set of experiments, which further strengthens the validity of their findings. Overall, this paper makes a valuable contribution to the field of RLVR and provides a solid foundation for future research.


## Soundness:

3.0


## Presentation:

3.25


## Contribution:

2.5


## Strengths:

I found several aspects of this paper to be particularly strong. The core idea of using KL divergence to weight token-level gradients is both novel and well-motivated. The authors clearly articulate the limitations of existing methods, such as GRPO, and present a compelling argument for why their approach is necessary. The theoretical analysis, particularly the proof in Appendix A, provides a solid foundation for the method, demonstrating why simply averaging over multiple teacher-conditioned models is insufficient. The paper's clarity is another significant strength. The authors present their method in a very accessible way, making it easy to understand the key concepts and the overall approach. The experimental results are also impressive, showing consistent improvements over GRPO and other baselines across a variety of tasks. The ablation study is particularly valuable, as it provides insights into the importance of the different components of the method. The authors also provide a detailed description of their experimental setup, which allows for reproducibility. The inclusion of a diverse set of benchmarks, covering mathematical reasoning, code generation, and agentic tasks, further strengthens the validity of their findings. The paper's focus on a practical problem, credit assignment in RLVR, and the authors' development of a method that addresses this problem effectively, makes this work highly relevant and impactful. The authors' approach is a significant step forward in addressing the challenges of credit assignment in RLVR, and their work has the potential to impact the development of more efficient and effective language models.


## Weaknesses:

Despite the strengths of this paper, I have identified several weaknesses that warrant careful consideration. First, while the paper introduces a novel method, the core idea of using KL divergence to weight gradients is not entirely new. As noted by one reviewer, the paper does not adequately acknowledge prior work that has explored similar techniques, such as the use of KL divergence for token-level credit assignment in RL. This lack of acknowledgment weakens the claim of novelty and suggests a need for a more thorough literature review. Second, the paper's reliance on verified trajectories as a binary signal is a significant limitation. The method's performance is heavily dependent on the availability of these trajectories, which may not always be feasible in real-world scenarios. The paper does not adequately address the potential for noisy or incomplete verifiers, which could impact the accuracy of the credit assignment. The authors should have explored methods for handling uncertainty in the verification process, such as incorporating confidence scores or using ensemble verifiers. Third, the paper lacks a detailed analysis of the computational overhead of SC-GRPO. While the authors mention that the overhead is relatively small, they do not provide a quantitative analysis of the time and memory requirements. This is a crucial omission, as the computational cost of the method could be a limiting factor in its practical application. The paper should have included a breakdown of the computational cost of each step in the algorithm, as well as a comparison with the computational cost of other methods. Fourth, the paper does not provide a detailed analysis of the sensitivity of SC-GRPO to the choice of hyperparameters. While the authors provide some hyperparameter settings, they do not explore the impact of different values on the performance of the method. This is a significant concern, as the performance of the method may be highly sensitive to the choice of hyperparameters. The paper should have included a sensitivity analysis to demonstrate the robustness of the method. Fifth, the paper does not provide a detailed analysis of the impact of different types of verified trajectories on the performance of SC-GRPO. The method's performance may vary depending on the quality and diversity of the verified trajectories. The paper should have explored the impact of using different types of verified trajectories, such as those generated by different verifiers or those with different levels of correctness. Sixth, the paper does not provide a detailed analysis of the limitations of SC-GRPO. The authors should have discussed the potential challenges of applying the method to more complex tasks or environments. This is a crucial omission, as it limits the understanding of the method's applicability and potential for future research. Finally, the paper does not provide a detailed analysis of the impact of different types of verifiers on the performance of SC-GRPO. The method's performance may vary depending on the quality and reliability of the verifier. The paper should have explored the impact of using different types of verifiers, such as those with different levels of accuracy or those with different types of feedback. These weaknesses, while not invalidating the paper's contributions, highlight areas where further research and analysis are needed.


## Suggestions:

Based on the weaknesses I've identified, I recommend several concrete improvements. First, the authors should conduct a more thorough literature review to acknowledge prior work that has explored similar techniques, particularly those that use KL divergence for token-level credit assignment in RL. This would strengthen the paper's claims of novelty and provide a more complete context for the method. Second, the authors should explore methods for handling uncertainty in the verification process. This could involve incorporating confidence scores or using ensemble verifiers to mitigate the impact of noisy or incomplete verifiers. Third, the authors should provide a detailed analysis of the computational overhead of SC-GRPO, including a breakdown of the time and memory requirements for each step in the algorithm. This would allow for a more accurate assessment of the method's practical applicability. Fourth, the authors should conduct a sensitivity analysis to demonstrate the robustness of the method to different hyperparameter settings. This would provide a better understanding of the method's stability and reliability. Fifth, the authors should explore the impact of different types of verified trajectories on the performance of SC-GRPO. This could involve using different verifiers or varying the level of correctness of the verified trajectories. Sixth, the authors should provide a detailed analysis of the limitations of SC-GRPO, including the potential challenges of applying the method to more complex tasks or environments. This would provide a more complete understanding of the method's applicability and potential for future research. Finally, the authors should explore the impact of different types of verifiers on the performance of SC-GRPO. This could involve using verifiers with different levels of accuracy or different types of feedback. These suggestions, if implemented, would significantly strengthen the paper and provide a more complete understanding of the proposed method.


## Questions:

I have several questions that arise from my analysis of the paper. First, how does the performance of SC-GRPO vary with the quality and diversity of the verified trajectories? Specifically, what is the impact of using verified trajectories generated by different verifiers or with different levels of correctness? Second, what is the computational overhead of SC-GRPO in terms of time and memory requirements, and how does this compare to the computational cost of other methods? Third, how sensitive is SC-GRPO to the choice of hyperparameters, and what is the optimal range of values for these hyperparameters? Fourth, how does the performance of SC-GRPO compare to other methods that use KL divergence for token-level credit assignment in RL? Fifth, what are the potential challenges of applying SC-GRPO to more complex tasks or environments, and how can these challenges be addressed? Sixth, how does the performance of SC-GRPO vary with different types of verifiers, and what are the implications for the robustness of the method? Finally, what are the limitations of using verified trajectories as a binary signal, and how can these limitations be mitigated? These questions target key uncertainties and methodological choices in the paper, and addressing them would provide a more complete understanding of the proposed method.


## Rating:

6.5


## Confidence:

3.75


## Decision:

Accept
}