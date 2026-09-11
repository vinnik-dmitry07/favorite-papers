Of course. I will use Fast Mode for quick thinking. As a professional reviewer, I will directly output a detailed evaluation of this paper. Let me think - Fast Mode means I will directly output a Summary, followed by scores for Soundness, Presentation and Contribution, then provide analysis of Strengths, Weaknesses, Suggestions, and Questions. Finally, I will output the Rating, Confidence and Decision:

\boxed_review{
## Summary:

This paper introduces prefix consistency as a novel reliability signal for enhancing the self-consistency method in large language models (LLMs). The core idea is that correct reasoning traces are more reproducible than incorrect ones. By truncating a chain-of-thought (CoT) sample and regenerating the continuation, the method assigns a reliability score based on how often the original answer is reproduced. This prefix consistency score is then used to reweight the votes in a weighted majority voting (WMV) scheme, termed PC-WMV. The authors demonstrate that PC-WMV outperforms standard self-consistency and other WMV baselines across four reasoning benchmarks and five model scales, achieving significant token savings (up to 21x) while maintaining or improving accuracy. The paper also includes a detailed analysis of the method's performance, including the impact of truncation fraction and the number of regenerations. However, the evaluation is limited to a few reasoning benchmarks and open-source models, and the paper lacks a thorough exploration of the method's sensitivity to hyperparameters and its applicability to other NLP tasks. Despite these limitations, the proposed method offers a promising and computationally efficient approach to improving the reliability of LLM reasoning.


## Soundness:

3.25


## Presentation:

3.0


## Contribution:

2.75


## Strengths:

The paper makes several valuable contributions to the field of LLM reasoning and self-consistency. First, the introduction of prefix consistency as a reliability signal is both simple and effective. The method leverages the observation that correct reasoning traces are more reproducible than incorrect ones, which is a novel insight that can be applied to various LLMs without requiring access to token log-probabilities. This makes the method particularly useful for models where probability access is restricted. Second, the empirical results are compelling. The authors show that PC-WMV outperforms standard self-consistency and other WMV baselines across multiple benchmarks and model scales. The performance gains are significant, especially on more challenging tasks, and the method achieves these improvements with substantial token savings, which is crucial for reducing computational costs. Third, the paper is well-written and easy to follow. The motivation for the method is clearly articulated, and the experimental setup is described in detail, making it straightforward for readers to understand and potentially replicate the results. Finally, the authors provide a comprehensive analysis of the method's performance, including the discrimination gap between correct and incorrect samples, which is a valuable contribution to the understanding of self-consistency in LLMs.


## Weaknesses:

Despite the paper's strengths, several limitations and areas for improvement have been identified. First, the evaluation is limited to a few reasoning benchmarks, specifically FrontierScience-Olympiad, HMMT Feb 2026, AIME 2025, and Brumo 2025. This narrow focus restricts the generalizability of the findings to other NLP tasks, such as sentiment analysis, text summarization, and machine translation. The paper does not explore how prefix consistency might be adapted or applied to these tasks, which are also important for LLM applications. Second, the experiments are conducted exclusively on open-source models, including GPT-OSS-120B, GPT-OSS-20B, Nemotron3-30B, Nemotron2-9B, and Ministral3-14B. While these models are powerful, the lack of evaluation on proprietary models like GPT-4 and Claude-3.5 limits the paper's applicability to a broader range of LLMs. Third, the method's sensitivity to hyperparameters, particularly the truncation fraction $	au$ and the number of regenerations $K$, is not thoroughly explored. The paper fixes $	au$ at 0.75 without providing a detailed analysis of how different values of $	au$ affect performance. Similarly, the impact of varying $K$ is not systematically investigated, which is crucial for understanding the method's robustness and optimal settings. The weighting function used in PC-WMV, $w^{(n)}(c) = c^n$, is also a potential limitation. While the paper shows that different values of $n$ (1, 2, 3) perform differently, the choice of this specific functional form is somewhat arbitrary and may not be optimal for all tasks and models. A more flexible weighting scheme, such as a linear combination of $c$ and other functions of $c$, could potentially improve performance. Additionally, the paper lacks a detailed analysis of the computational overhead associated with the regeneration process. While the authors claim token savings, a breakdown of the time and resources required for truncation and regeneration, compared to other WMV methods, would provide a more complete picture of the method's efficiency. The paper also does not explore the potential for combining prefix consistency with other reliability signals, such as log probabilities or verbalized confidence scores. Such a hybrid approach could leverage the strengths of different signals and potentially lead to further performance improvements. Finally, the paper could benefit from a more thorough discussion of the limitations of prefix consistency. For example, the method's effectiveness might be influenced by the quality of the initial CoT sample, and it is not clear how the method performs in scenarios where the initial sample is of poor quality. The paper should also investigate the potential for bias introduced by the truncation and regeneration process, especially in tasks where the answer is not a simple numerical value.


## Suggestions:

To address the identified limitations and strengthen the paper, several concrete and actionable improvements are recommended. First, the authors should expand the evaluation to include a wider range of NLP tasks beyond mathematical and scientific reasoning. This could involve tasks such as sentiment analysis, text summarization, and machine translation. For each task, the authors should discuss how the prefix consistency signal can be defined and adapted, and provide empirical results to demonstrate its effectiveness. This would significantly enhance the paper's impact and applicability. Second, the authors should conduct experiments on proprietary models like GPT-4 and Claude-3.5 to assess the method's performance on state-of-the-art LLMs. This would provide a more comprehensive understanding of the method's generalizability and robustness. Third, a more detailed analysis of the method's sensitivity to hyperparameters is essential. The authors should explore a range of $	au$ values (e.g., from 0.25 to 0.95) and analyze how the performance changes. This analysis should include a discussion of the trade-offs between reproducibility and the amount of context available for regeneration. Similarly, the impact of varying the number of regenerations $K$ should be investigated, with a focus on the computational cost and performance gains. Fourth, the authors should consider more flexible weighting functions for PC-WMV. For instance, a linear combination of $c$ and $c^2$ could be explored, and the optimal combination could be determined through cross-validation. This would allow the method to adapt to different tasks and models more effectively. Fifth, a detailed computational cost analysis should be included. The authors should provide a breakdown of the time and resources required for the truncation and regeneration processes, and compare these costs to other WMV methods. This would help readers understand the practical implications of using prefix consistency. Sixth, the authors should explore the potential for combining prefix consistency with other reliability signals. For example, a weighted average of prefix consistency and log probabilities could be used, with the weights determined through cross-validation. This hybrid approach could leverage the strengths of different signals and potentially lead to further performance improvements. Finally, the paper should include a more thorough discussion of the limitations of prefix consistency. The authors should investigate how the method's effectiveness is influenced by the quality of the initial CoT sample and explore scenarios where the method might fail. The potential for bias introduced by the truncation and regeneration process should also be examined, especially in tasks where the answer is not a simple numerical value.


## Questions:

1. How does the performance of prefix consistency vary across different types of reasoning tasks, such as logical reasoning, common-sense reasoning, and causal reasoning? Are there specific task characteristics that make prefix consistency more or less effective?
2. What is the impact of the truncation fraction $	au$ on the performance of prefix consistency? How does the method's effectiveness change when $	au$ is varied across a wide range of values, and what is the optimal value of $	au$ for different tasks and models?
3. How does the number of regenerations $K$ affect the performance and computational cost of PC-WMV? Is there a point of diminishing returns, and what is the optimal value of $K$ for different tasks and models?
4. Can the prefix consistency signal be combined with other reliability signals, such as log probabilities or verbalized confidence scores, to create a more robust and effective weighting scheme? How do these hybrid approaches perform compared to PC-WMV alone?
5. How does the quality of the initial CoT sample influence the effectiveness of prefix consistency? Are there scenarios where the method fails due to poor initial samples, and how can these be mitigated?
6. What is the computational overhead of the truncation and regeneration process, and how does it compare to other WMV methods? Are there specific hardware or software optimizations that can reduce this overhead?
7. How does the method perform on simpler tasks where the correct answer is easily reproduced? Is there a threshold of task difficulty below which prefix consistency does not provide a significant advantage?
8. Can the prefix consistency approach be applied to non-reasoning tasks, such as text generation or classification? If so, how would the prefix be defined, and what are the potential benefits and limitations in these contexts?


## Rating:

6.75


## Confidence:

3.5


## Decision:

Accept
}