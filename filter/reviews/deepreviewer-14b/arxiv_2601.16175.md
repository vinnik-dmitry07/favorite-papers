Of course. I will use Fast Mode for quick thinking. As a professional reviewer, I will directly output a detailed evaluation of this paper. Let me think - Fast Mode means I will directly output a Summary, followed by scores for Soundness, Presentation and Contribution, then provide analysis of Strengths, Weaknesses, Suggestions, and Questions. Finally, I will output the Rating, Confidence and Decision:

\boxed_review{
## Summary:

This paper introduces Test-Time Training to Discover (TTT-Discover), a novel approach that leverages reinforcement learning to train large language models (LLMs) at test time for scientific discovery. Unlike traditional test-time adaptation methods that focus on improving generalization, TTT-Discover aims to find a single, high-reward solution to a given problem. The method combines an entropic objective, which favors actions leading to high rewards, with a PUCT-inspired state reuse strategy that balances exploitation of promising states with exploration of new ones. The authors demonstrate the effectiveness of TTT-Discover across a diverse range of challenging scientific domains, including mathematics, GPU kernel engineering, algorithm design, and single-cell RNA-seq analysis. In each of these domains, TTT-Discover achieves state-of-the-art results, often outperforming both human experts and existing AI methods. The paper also includes a thorough ablation study that validates the importance of the proposed entropic objective and PUCT reuse strategy. Overall, TTT-Discover represents a significant advancement in the field of AI-driven scientific discovery, offering a practical and effective method for solving complex, reward-driven problems.


## Soundness:

3.25


## Presentation:

3.25


## Contribution:

3.25


## Strengths:

I find the paper to be a compelling and well-executed contribution to the field of AI-driven scientific discovery. The core idea of using reinforcement learning at test time to discover novel solutions is both innovative and well-motivated. The authors effectively address the unique challenges of this setting, where the goal is to find a single, high-reward solution rather than to generalize across a distribution of problems. The proposed entropic objective and PUCT-inspired state reuse strategy are well-suited to this task, and the paper provides a clear and thorough explanation of these components. The empirical evaluation is another strong aspect of the paper. The authors demonstrate the effectiveness of TTT-Discover across a diverse set of scientific domains, including mathematics, GPU kernel engineering, algorithm design, and single-cell RNA-seq analysis. In each domain, TTT-Discover achieves state-of-the-art results, often outperforming both human experts and existing AI methods. The ablation study is particularly valuable, as it provides empirical evidence for the importance of the proposed entropic objective and PUCT reuse strategy. The paper is also well-written and easy to follow, with clear explanations of the methods and results. The inclusion of detailed experimental setups and hyperparameter settings in the appendix enhances the reproducibility of the work. Overall, I believe that TTT-Discover is a significant and well-supported contribution to the field, and I am impressed by the thoroughness and clarity of the paper.


## Weaknesses:

While I find the paper to be a strong contribution, there are several verified limitations that I believe should be addressed. First, the paper lacks a detailed analysis of the computational efficiency of the discovered algorithms, particularly in the context of GPU kernel engineering. For instance, in the TriMul and MLA-Decode experiments, the paper reports the runtime of the best kernels found but does not provide a breakdown of the computational complexity or memory access patterns of these kernels. This is a significant gap, as understanding the efficiency of the generated code is crucial for practical applications. The paper mentions that the discovered TriMul kernels fuse operations and convert inputs to FP16 for cuBLAS/rocBLAS, but it does not delve into the specific efficiency gains or limitations of these approaches. Similarly, for the MLA-Decode kernels, the paper notes the use of `torch.compile()` but does not analyze the resulting assembly code or memory access patterns. This lack of detailed analysis makes it difficult to assess the practical value of the discovered kernels beyond their runtime performance. I am confident in this weakness based on the absence of such analyses in the experimental sections and the appendix, and the implications are substantial, as the efficiency of the generated code is a critical factor in real-world deployment. (Confidence: High)

Second, the paper does not provide a detailed analysis of the exploration-exploitation trade-off in the context of the discovered algorithms. While the paper mentions that the discovered algorithms often start from human-designed initial states and improve upon them, it does not quantify the extent to which the method explores the search space beyond these initial states. For example, in the TriMul and ahc039 experiments, the paper states that the discovered kernels and algorithms build upon existing solutions, but it does not provide metrics such as the average edit distance between the discovered solutions and the initial states, or the distribution of the types of modifications made to the initial solutions. This makes it challenging to understand the true novelty of the discovered solutions and the balance between exploration and exploitation. I am confident in this weakness based on the lack of such metrics and the focus on iterative improvement in the experimental results. (Confidence: High)

Third, the paper does not provide a detailed analysis of the sensitivity of the discovered algorithms to the hyperparameters of the TTT-Discover method. The paper mentions the hyperparameters used but does not explore how changes in these parameters affect the final solutions. For example, the paper does not analyze the impact of varying the learning rate, the number of training steps, or the batch size on the discovered algorithms. This is a significant gap, as the robustness of the method to hyperparameter changes is crucial for its practical applicability. I am confident in this weakness based on the lack of such sensitivity analyses in the experimental sections and the appendix. (Confidence: High)

Fourth, the paper does not provide a detailed analysis of the types of code modifications made by the discovered algorithms. While the paper includes high-level descriptions of the strategies used, such as the simulated annealing and beam search techniques in the ahc058 experiment, it does not provide a systematic categorization of the code edits. For example, the paper does not quantify the frequency of different types of edits, such as the addition or removal of code blocks, changes in loop structures, or modifications to function calls. This makes it difficult to understand the specific ways in which the discovered algorithms improve upon the initial solutions and the nature of the learned optimization strategies. I am confident in this weakness based on the absence of such a detailed analysis in the experimental sections and the appendix. (Confidence: High)

Finally, the paper does not provide a detailed analysis of the limitations of the proposed method. While the paper mentions that TTT-Discover did not achieve a new state-of-the-art in the second autocorrelation inequality and circle packing problems, it does not delve into the reasons for these failures. For example, the paper does not analyze the specific characteristics of these problems that make them challenging for TTT-Discover, such as the size of the search space or the sparsity of the reward signal. Additionally, the paper does not discuss the computational cost of the method and its scalability to larger and more complex problems. I am confident in this weakness based on the lack of such a detailed discussion in the paper and the implications for understanding the method's limitations and potential areas for improvement. (Confidence: High)


## Suggestions:

To address the identified weaknesses, I recommend several concrete and actionable improvements. First, the authors should conduct a detailed analysis of the computational efficiency of the discovered GPU kernels. This should include a breakdown of the computational complexity, memory access patterns, and the specific hardware features utilized by the kernels. For the TriMul kernels, the authors should provide an analysis of the fused operations and the use of FP16 conversions, including any limitations or inefficiencies. For the MLA-Decode kernels, a comparison of the assembly code generated by `torch.compile()` with manually optimized assembly code would be valuable. This analysis should be included in the experimental sections and the appendix to provide a more comprehensive understanding of the practical value of the discovered kernels. (Confidence: High)

Second, the authors should provide a more detailed analysis of the exploration-exploitation trade-off in the discovered algorithms. This could involve quantifying the extent to which the method explores the search space beyond the initial states. For example, the authors could calculate the average edit distance between the discovered solutions and the initial states, and provide a distribution of the types of modifications made to the initial solutions. This would help to understand the true novelty of the discovered solutions and the balance between exploration and exploitation. The authors should also include this analysis in the experimental sections and the appendix. (Confidence: High)

Third, the authors should conduct a sensitivity analysis of the discovered algorithms to the hyperparameters of the TTT-Discover method. This should include varying the learning rate, the number of training steps, and the batch size, and analyzing how these changes affect the final solutions. The authors should also discuss the computational cost of the method and its scalability to larger and more complex problems. This analysis would provide valuable insights into the robustness of the method and its practical applicability. The authors should include this analysis in the experimental sections and the appendix. (Confidence: High)

Fourth, the authors should provide a detailed analysis of the types of code modifications made by the discovered algorithms. This could involve categorizing the code edits into different types, such as the addition or removal of code blocks, changes in loop structures, or modifications to function calls. The authors should then quantify the frequency of each type of edit and discuss how these changes contribute to the improved performance of the algorithms. For example, in the ahc058 experiment, the authors should provide a more detailed explanation of the specific techniques used, such as the simulated annealing and beam search, and how these techniques are implemented in the discovered code. This analysis should be included in the experimental sections and the appendix to provide a more comprehensive understanding of the learned optimization strategies. (Confidence: High)

Finally, the authors should provide a more detailed discussion of the limitations of the proposed method. This should include an analysis of the specific characteristics of the problems where TTT-Discover did not achieve a new state-of-the-art, such as the size of the search space or the sparsity of the reward signal. The authors should also discuss the computational cost of the method and its scalability to larger and more complex problems. This would help to identify potential areas for improvement and to understand the practical limitations of the method. The authors should include this discussion in the paper, possibly in a dedicated section on limitations. (Confidence: High)


## Questions:

I have several questions that I believe would help to clarify and strengthen the paper. First, I am curious about the specific types of code modifications made by the discovered algorithms. Could the authors provide a detailed categorization and frequency analysis of the code edits, such as the addition or removal of code blocks, changes in loop structures, or modifications to function calls? This would help to understand the specific ways in which the discovered algorithms improve upon the initial solutions and the nature of the learned optimization strategies. (Confidence: High)

Second, I would like to know more about the exploration-exploitation trade-off in the discovered algorithms. Could the authors quantify the extent to which the method explores the search space beyond the initial states? For example, could they provide the average edit distance between the discovered solutions and the initial states, and a distribution of the types of modifications made to the initial solutions? This would help to understand the true novelty of the discovered solutions and the balance between exploration and exploitation. (Confidence: High)

Third, I am interested in the sensitivity of the discovered algorithms to the hyperparameters of the TTT-Discover method. Could the authors provide a detailed analysis of how changes in hyperparameters, such as the learning rate, the number of training steps, and the batch size, affect the final solutions? This would help to assess the robustness of the method and its practical applicability. (Confidence: High)

Fourth, I would like to understand the computational efficiency of the discovered GPU kernels in more detail. Could the authors provide a breakdown of the computational complexity, memory access patterns, and the specific hardware features utilized by the kernels? For the TriMul kernels, could they analyze the fused operations and the use of FP16 conversions, including any limitations or inefficiencies? For the MLA-Decode kernels, could they compare the assembly code generated by `torch.compile()` with manually optimized assembly code? This would provide a more comprehensive understanding of the practical value of the discovered kernels. (Confidence: High)

Finally, I am curious about the limitations of the proposed method. Could the authors provide a detailed analysis of the specific characteristics of the problems where TTT-Discover did not achieve a new state-of-the-art, such as the size of the search space or the sparsity of the reward signal? Additionally, could they discuss the computational cost of the method and its scalability to larger and more complex problems? This would help to identify potential areas for improvement and to understand the practical limitations of the method. (Confidence: High)


## Rating:

8.0


## Confidence:

3.5


## Decision:

Accept
}