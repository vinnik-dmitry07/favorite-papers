I will use Standard Mode for comprehensive thinking. As a professional reviewer, I will simulate 4 different reviewers, followed by the verification thinking. Then I will output the Finally Review Output. Let me think - Standard Mode means I will output the original review, followed by the verification thinking. Considering that I am currently in standard mode, I should think from my existing knowledge and consider some related work content when writing about weaknesses. Then I will output the Finally Review Output and Meta Review Output:

\boxed_simreviewers{
## Reviewer 1

### Summary

This paper proposes a novel RL algorithm for training LLM agents in multi-step tasks. GiGPO introduces a two-level structure for estimating relative advantages, allowing for fine-grained, step-level credit assignment without the need for additional model rollouts or memory usage. GiGPO achieves performance gains of more than 12% on challenging tasks such as ALFWorld and WebShop, while maintaining the same GPU memory overhead, identical LLM rollout costs, and no additional time cost.

### Soundness

3

### Presentation

3

### Contribution

3

### Strengths

1. GiGPO introduces a hierarchical structure for advantage estimation, allowing for both macro-level group performance comparison and micro-level group-level credit assignment. This approach captures both global task effectiveness and local step-wise performance feedback, addressing the credit assignment challenge in long-horizon LLM agent training effectively.
2. GiGPO is highly compatible with existing group-based RL algorithms, requiring no additional model rollouts or memory usage. This design ensures that GiGPO can be easily integrated into current RL training frameworks, making it highly practical and efficient.
3. GiGPO achieves significant performance improvements on complex tasks such as ALFWorld and WebShop, with more than 12% increase in success rates over previous methods. This demonstrates the effectiveness of GiGPO in training LLM agents for multi-step tasks.

### Weaknesses

#### Some Related Works


#### comment

1. The paper introduces a hierarchical structure for advantage estimation, but the specific implementation details and the rationale behind the design choices could be further elaborated. For instance, the method for grouping trajectories and the criteria for determining the similarity of states are not fully explained. A more detailed explanation of how the grouping is performed, including the specific algorithms or heuristics used, would be beneficial. Furthermore, the choice of similarity metric for state grouping needs more justification, as different metrics could lead to different groupings and potentially impact performance.
2. While GiGPO is compatible with existing group-based RL algorithms, the paper could benefit from a more in-depth analysis of how GiGPO interacts with different group sizes and task complexities. The current analysis lacks a systematic exploration of how the performance of GiGPO varies with different group sizes, especially in relation to the complexity of the task. It would be valuable to see experiments that systematically vary the group size and analyze its impact on the convergence speed and final performance of the algorithm. Additionally, the paper could explore how GiGPO performs on tasks with varying levels of stochasticity, as this could reveal limitations of the approach.
3. The paper claims that GiGPO maintains the same GPU memory overhead, identical LLM rollout costs, and no additional time cost compared to existing methods. However, a more detailed breakdown of the computational costs and memory usage would be helpful to validate these claims. The current analysis lacks a detailed breakdown of the computational costs and memory usage. It would be beneficial to provide a more granular analysis of the time spent on different parts of the algorithm, such as the grouping of trajectories, the computation of advantages, and the policy updates. Similarly, the memory usage should be broken down to show how much memory is used for different components of the algorithm, such as the model parameters, the trajectory data, and the grouping information. Without this detailed breakdown, it is difficult to fully assess the practical implications of the claims.

### Suggestions

To address the lack of detailed implementation specifics, the authors should include a more thorough description of the trajectory grouping and state similarity methods. This should include a clear explanation of the algorithms used for grouping trajectories, the criteria for determining state similarity, and the specific similarity metric employed. For example, if a k-NN algorithm is used for trajectory grouping, the value of k should be specified, and the distance metric used to compute the distances between trajectories should be clearly stated. Similarly, for state similarity, if a cosine similarity is used, the vector representation of the states should be described. Furthermore, the authors should provide a rationale for their design choices, explaining why they chose a particular grouping method or similarity metric over other alternatives. This would allow other researchers to reproduce the results and build upon the work. The authors could also include a sensitivity analysis to show how the performance of the algorithm varies with different grouping methods and similarity metrics.

To strengthen the analysis of GiGPO's interaction with different group sizes and task complexities, the authors should conduct a more systematic study. This should include experiments that vary the group size and analyze its impact on the convergence speed and final performance of the algorithm. The experiments should be conducted on a range of tasks with varying levels of complexity, including both simpler tasks with fewer steps and more complex tasks with longer horizons. The authors should also analyze the performance of GiGPO on tasks with different levels of stochasticity, as this could reveal limitations of the approach. For example, the authors could introduce different levels of noise in the environment and observe how the performance of GiGPO changes. This would provide a more comprehensive understanding of the strengths and weaknesses of the algorithm and its applicability to different types of tasks. The authors should also consider using a more diverse set of tasks to evaluate the generalizability of the approach.

Finally, to validate the claims about computational efficiency, the authors should provide a detailed breakdown of the computational costs and memory usage. This should include a granular analysis of the time spent on different parts of the algorithm, such as the grouping of trajectories, the computation of advantages, and the policy updates. The authors should also provide a breakdown of the memory usage, showing how much memory is used for different components of the algorithm, such as the model parameters, the trajectory data, and the grouping information. This analysis should be conducted on different hardware configurations to show how the performance of the algorithm scales with different resources. The authors should also compare the computational costs and memory usage of GiGPO with other existing methods to demonstrate its efficiency. This detailed analysis would provide a more complete picture of the practical implications of the claims and allow other researchers to assess the feasibility of using GiGPO in their own work.

### Questions

1. How does the performance of GiGPO vary with different group sizes, especially in tasks with varying levels of complexity? Could you provide more detailed analysis on the impact of group size on the convergence speed and final performance?
2. How does GiGPO handle tasks with different levels of stochasticity? Are there any limitations in the approach when dealing with highly stochastic environments?
3. Could you provide a more detailed breakdown of the computational costs and memory usage of GiGPO compared to other methods? How does GiGPO maintain the same GPU memory overhead and LLM rollout costs?

### Rating

6

### Confidence

4

**********

## Reviewer 2

### Summary

This paper introduces a novel group-based reinforcement learning algorithm, GiGPO, designed to enhance fine-grained credit assignment in LLM agents. GiGPO addresses the challenges of sparse rewards and long-horizon tasks by implementing a two-level structure for estimating relative advantages: (i) episode-level advantages and (ii) step-level advantages. The algorithm constructs macro relative advantages based on groups of complete trajectories and micro relative advantages based on groups of step-level groups. These two levels of advantages are combined to provide a comprehensive credit signal for training LLM agents. GiGPO is compatible with group-based RL algorithms, requiring no additional rollouts or memory usage, and demonstrates significant performance improvements over existing methods in tasks such as ALFWorld and WebShop.

### Soundness

3

### Presentation

3

### Contribution

3

### Strengths

1. GiGPO introduces a novel two-level advantage estimation structure that effectively addresses the credit assignment problem in long-horizon LLM agent training. The combination of macro and micro advantages provides a more granular credit signal, enabling more precise updates and faster convergence.
2. GiGPO is compatible with existing group-based RL algorithms without requiring additional rollouts or memory usage, making it highly efficient and easy to integrate into current frameworks.
3. The paper is well-organized and clearly written, with a logical flow that effectively communicates the motivation, methodology, and results of the proposed algorithm.

### Weaknesses

#### Some Related Works


#### comment

1. The paper lacks a detailed discussion of the limitations of GiGPO, such as its sensitivity to hyperparameter settings and potential challenges in real-world applications. Specifically, the paper does not explore how the weighting between episode-level and step-level advantages affects performance across different tasks. Furthermore, the computational overhead of constructing and managing step-level groups, especially in high-dimensional action spaces, is not thoroughly analyzed. A more detailed discussion of these limitations would provide a more balanced view of the algorithm's capabilities.
2. While the paper demonstrates improved performance on specific tasks, it does not explore the generalizability of GiGPO to a broader range of LLM agent tasks or environments. The experiments are limited to ALFWorld and WebShop, which may not fully represent the diversity of challenges encountered in real-world applications. It is unclear how GiGPO would perform in tasks with different reward structures, action spaces, or levels of stochasticity. A more comprehensive evaluation across diverse tasks would strengthen the paper's claims of general applicability.

### Suggestions

To address the identified weaknesses, the authors should conduct a more thorough analysis of the hyperparameter sensitivity of GiGPO. This should include a systematic exploration of how the weighting between episode-level and step-level advantages impacts performance across different tasks. For instance, the authors could perform a sensitivity analysis by varying the weighting parameter across a range of values and observing the resulting changes in performance on tasks with varying reward sparsity and task complexity. This analysis should be presented with clear visualizations, such as plots showing the performance as a function of the weighting parameter. Furthermore, the authors should investigate the computational cost of constructing and managing step-level groups, especially in high-dimensional action spaces. This could involve profiling the algorithm to identify performance bottlenecks and exploring potential optimizations, such as using more efficient data structures or parallel processing techniques. A detailed analysis of the computational overhead would provide a more complete understanding of the practical limitations of GiGPO.

To improve the generalizability of the results, the authors should evaluate GiGPO on a more diverse set of tasks and environments. This could include tasks with different reward structures, such as sparse rewards or delayed rewards, as well as tasks with different action spaces, such as continuous action spaces or multi-modal action spaces. For example, the authors could evaluate GiGPO on tasks from the DeepMind Control Suite or other benchmark environments commonly used in reinforcement learning research. This would provide a more robust assessment of the algorithm's performance and its ability to generalize to different types of tasks. Additionally, the authors should explore the performance of GiGPO in more complex, real-world scenarios, such as those involving multi-agent interactions or partial observability. This would help to identify potential limitations of the algorithm and guide future research directions.

Finally, the authors should provide a more detailed discussion of the limitations of GiGPO, including potential challenges in real-world applications. This should include a discussion of the assumptions made by the algorithm and the conditions under which these assumptions may not hold. For example, the authors should discuss the potential impact of noisy or incomplete state information on the performance of GiGPO. They should also discuss the potential limitations of the algorithm in scenarios where the reward function is not well-defined or where the task is highly dynamic. A thorough discussion of these limitations would provide a more balanced and realistic assessment of the algorithm's capabilities and would help to guide future research in this area.

### Questions

1. How does the performance of GiGPO vary with different weighting between episode-level and step-level advantages? Are there any guidelines for selecting the optimal weighting for different tasks?
2. What are the potential limitations of GiGPO in real-world applications, particularly in scenarios with high-dimensional action spaces or complex reward structures?

### Rating

6

### Confidence

3

**********

## Reviewer 3

### Summary

The paper introduces GiGPO, a novel group-based reinforcement learning algorithm designed to enhance fine-grained credit assignment for LLM agents in multi-turn tasks. GiGPO addresses the challenges of sparse rewards and long-horizon tasks by implementing a two-level structure for estimating relative advantages: (i) episode-level advantages based on groups of complete trajectories and (ii) step-level advantages based on groups of step-level groups. This hierarchical structure effectively captures both global trajectory effectiveness and local step-wise performance feedback, enabling more precise credit assignment and faster convergence. GiGPO is compatible with existing group-based RL algorithms, requiring no additional rollouts or memory usage, and demonstrates significant performance improvements over prior methods in tasks such as ALFWorld and WebShop, achieving over 12% performance gains while maintaining the same GPU memory overhead, identical LLM rollout costs, and no additional time cost.

### Soundness

3

### Presentation

3

### Contribution

3

### Strengths

1. GiGPO introduces a novel two-level advantage estimation structure that effectively addresses the credit assignment problem in long-horizon LLM agent training. The combination of macro and micro advantages provides a more granular credit signal, enabling more precise updates and faster convergence.

2. GiGPO is compatible with existing group-based RL algorithms, requiring no additional rollouts or memory usage, making it highly efficient and easy to integrate into current frameworks.

3. The paper is well-organized and clearly written, with a logical flow that effectively communicates the motivation, methodology, and results of the proposed algorithm.

### Weaknesses

#### Some Related Works


#### comment

1. The paper lacks a detailed discussion of the limitations of GiGPO, such as its sensitivity to hyperparameter settings and potential challenges in real-world applications. Specifically, the paper does not explore how the weighting between episode-level and step-level advantages affects performance across different tasks. Furthermore, the computational overhead of constructing and managing step-level groups, especially in high-dimensional action spaces, is not thoroughly analyzed. A more detailed discussion of these limitations would provide a more balanced view of the algorithm's capabilities.

2. While the paper demonstrates improved performance on specific tasks, it does not explore the generalizability of GiGPO to a broader range of LLM agent tasks or environments. The experiments are limited to ALFWorld and WebShop, which may not fully represent the diversity of challenges encountered in real-world applications. It is unclear how GiGPO would perform in tasks with different reward structures, action spaces, or levels of stochasticity. A more comprehensive evaluation across diverse tasks would strengthen the paper's claims of general applicability.

### Suggestions

To address the identified weaknesses, the authors should conduct a more thorough analysis of the hyperparameter sensitivity of GiGPO. This should include a systematic exploration of how the weighting between episode-level and step-level advantages impacts performance across different tasks. For instance, the authors could perform a sensitivity analysis by varying the weighting parameter across a range of values and observing the resulting changes in performance on tasks with varying reward sparsity and task complexity. This analysis should be presented with clear visualizations, such as plots showing the performance as a function of the weighting parameter. Furthermore, the authors should investigate the computational cost of constructing and managing step-level groups, especially in high-dimensional action spaces. This could involve profiling the algorithm to identify performance bottlenecks and exploring potential optimizations, such as using more efficient data structures or parallel processing techniques. A detailed analysis of the computational overhead would provide a more complete understanding of the practical limitations of GiGPO.

To improve the generalizability of the results, the authors should evaluate GiGPO on a more diverse set of tasks and environments. This could include tasks with different reward structures, such as sparse rewards or delayed rewards, as well as tasks with different action spaces, such as continuous action spaces or multi-modal action spaces. For example, the authors could evaluate GiGPO on tasks from the DeepMind Control Suite or other benchmark environments commonly used in reinforcement learning research. This would provide a more robust assessment of the algorithm's performance and its ability to generalize to different types of tasks. Additionally, the authors should explore the performance of GiGPO in more complex, real-world scenarios, such as those involving multi-agent interactions or partial observability. This would help to identify potential limitations of the algorithm and guide future research directions.

Finally, the authors should provide a more detailed discussion of the limitations of GiGPO, including potential challenges in real-world applications. This should include a discussion of the assumptions made by the algorithm and the conditions under which these assumptions may not hold. For example, the authors should discuss the potential impact of noisy or incomplete state information on the performance of GiGPO. They should also discuss the potential limitations of the algorithm in scenarios where the reward function is not well-defined or where the task is highly dynamic. A thorough discussion of these limitations would provide a more balanced and realistic assessment of the algorithm's capabilities and would help to guide future research in this area.

### Questions

1. How does the performance of GiGPO vary with different weighting between episode-level and step-level advantages? Are there any guidelines for selecting the optimal weighting for different tasks?

2. What are the potential limitations of GiGPO in real-world applications, particularly in scenarios with high-dimensional action spaces or complex reward structures?

### Rating

8

### Confidence

3

**********

## Reviewer 4

### Summary

This paper proposes a novel group-based RL algorithm called GiGPO that improves credit assignment for LLM agents in multi-turn tasks. The key innovation is a two-level advantage estimation structure that combines macro-level group performance comparison with micro-level step-level credit assignment. GiGPO achieves significant performance gains over prior methods on ALFWorld and WebShop benchmarks while maintaining the same GPU memory overhead, LLM rollout costs, and no additional time cost.

### Soundness

3

### Presentation

3

### Contribution

3

### Strengths

- The two-level advantage structure is novel and well-motivated. It effectively combines global trajectory-level credit assignment with local step-level credit assignment.
- The algorithm is compatible with existing group-based RL methods and requires no additional rollouts or memory.
- The paper provides thorough empirical validation on challenging multi-turn tasks like ALFWorld and WebShop, showing significant performance improvements over strong baselines.
- The ablation studies clearly demonstrate the importance of both the macro and micro advantage components.

### Weaknesses

#### Some Related Works


#### comment

 - The paper could benefit from more discussion of the limitations of the approach. For example, how does GiGPO perform in environments with very long horizons or very sparse rewards? It would be helpful to see experiments on more challenging tasks with these characteristics to better understand the boundaries of the method. Specifically, the paper lacks analysis on how the grouping strategy performs when the number of trajectories per group is varied, and how this impacts the stability and convergence of the algorithm. Furthermore, the paper does not explore the sensitivity of the method to the choice of the similarity metric used for grouping trajectories, which could be a critical factor in its performance.
- The paper does not include a detailed analysis of the computational cost of the algorithm. While the authors claim that GiGPO has the same computational cost as GRPO, a more thorough breakdown of the time and memory requirements would be valuable. For example, the cost of computing the macro and micro advantages, and the overhead of maintaining the grouping structure, should be analyzed separately. It would also be useful to see how the computational cost scales with the number of agents, trajectories, and the length of the episodes. The paper also lacks a discussion of the potential for parallelization and how this could impact the overall runtime of the algorithm.

### Suggestions

The paper would benefit from a more thorough investigation into the limitations of the proposed GiGPO algorithm. Specifically, the authors should explore the performance of GiGPO in environments with very long horizons and very sparse rewards. This could involve testing the algorithm on more challenging tasks that require long-term planning and credit assignment, such as those found in complex multi-agent environments or tasks with delayed rewards. It would also be beneficial to analyze the sensitivity of the algorithm to the number of trajectories per group and the choice of the similarity metric used for grouping. For example, the authors could conduct experiments with varying group sizes and analyze how this affects the stability and convergence of the algorithm. Additionally, they could explore different similarity metrics, such as cosine similarity or Euclidean distance, and compare their performance. This would provide a more comprehensive understanding of the algorithm's robustness and generalizability.

Furthermore, the paper should include a more detailed analysis of the computational cost of the algorithm. This should include a breakdown of the time and memory requirements for computing the macro and micro advantages, as well as the overhead of maintaining the grouping structure. The authors should also analyze how the computational cost scales with the number of agents, trajectories, and the length of the episodes. This analysis should be presented in a way that is easy to understand, perhaps using tables or graphs that show the computational cost as a function of these parameters. It would also be useful to discuss the potential for parallelization and how this could impact the overall runtime of the algorithm. For example, the authors could explore the use of distributed computing techniques to speed up the computation of the macro and micro advantages. This would provide a more complete picture of the algorithm's efficiency and scalability.

Finally, the paper should include a more detailed discussion of the hyperparameter settings used in the experiments. This should include a description of how the hyperparameters were chosen and how they affect the performance of the algorithm. For example, the authors could discuss the impact of the weighting parameter that balances the macro and micro advantages, and how this parameter should be chosen for different tasks. It would also be helpful to include a sensitivity analysis of the hyperparameters, showing how the performance of the algorithm varies with different settings. This would provide a more complete understanding of the algorithm's behavior and help other researchers to use it effectively.

### Questions

- How does GiGPO perform in environments with very long horizons or very sparse rewards? Have you considered testing on more challenging tasks with these characteristics?
- How sensitive is GiGPO to the choice of hyperparameters, particularly the weighting between macro and micro advantages?
- Can you provide more details on the computational cost of the algorithm? How does it scale with the number of agents, trajectories, and episode length?

### Rating

8

### Confidence

4

**********

}

I have finished generating simulated reviews from 4 reviewers. Next, I will generate verification content for these reviews:

\boxed_verification{
The user wants me to validate weaknesses identified by reviewers for the provided paper. I need to go through each reviewer's comments and check if the criticism is valid based on the content of the paper.

For each weakness, I will:
1. **State the weakness.**
2. **Collect evidence from the paper.** This will involve looking for relevant sections in the method and experiments.
3. **Perform a literature gap analysis.** Check if the paper misses any crucial citations or baseline comparisons.
4. **Analyze the evidence.** Summarize the findings and assess the impact of the weakness.
5. **Conclude on the validity of the weakness.**
**Review 1**

1. Weakness Statement:
[The paper lacks a detailed discussion of the limitations of GiGPO, such as its sensitivity to hyperparameter settings and potential challenges in real-world applications. Specifically, the paper does not explore how the weighting between episode-level and step-level advantages affects performance across different tasks. Furthermore, the computational overhead of constructing and managing step-level groups, especially in high-dimensional action spaces, is not thoroughly analyzed. A more detailed discussion of these limitations would provide a more balanced view of the algorithm's capabilities.]

2. Evidence Collection:
a) Method-related Evidence:
   - The paper introduces the weighting coefficient $\omega$ in Section 4.3: "A weighting coefficient that balances episode relative advantage and step relative advantage. A E$\mathrm{A^{S}}$ provides micro credit assignment and fine-grained feedback on the relative quality of individual actions taken from the same state, enabling more precise optimization while avoiding the cost explosion; while A E A provides macro credit assignment and global credit."
   - The ablation study in Section 5.4 explicitly investigates the impact of removing either component: "As illustrated, eliminating either component of the two-level advantage significantly degrades performance. Removing the episode relative advantages (GiGPO w/o std) leads to a substantial drop across all tasks, as the policy no longer receives a stable, trajectory-wide signal to encourage long-range coherence. Similarly, discarding the step relative advantages (GiGPO w/o A S A) results in pronounced declines, particularly on more complex and demanding tasks such as Cool, Pick2, and WebShop, which may require nuanced training feedback at each decision step."
   - The paper mentions the computational budget in Section 5.6: "GiGPO shares the same core architecture as GRPO, including multi-turn rollouts, computation of old and reference probabilities, and clipped policy updates. Both approaches are critic-free and operate with a single actor LLM, thereby resulting in identical GPU memory usage and LLM rollout costs. The primary additions introduced by GiGPO are the step-relative advantage estimation components, as described in Section 4.2 . To evaluate their costs, we train an LLM agent in ALFWorld using Qwen2.5-1.5B-Instruct and record a detailed breakdown of per-iteration training time."
   - Section 5.6 provides a detailed breakdown of the per-iteration training time for different components.

b) Experiment-related Evidence:
   - The ablation study in Figure 4 shows the performance impact of removing each component, implicitly addressing the weighting by showing the effect of removing the entire step-level advantage.
   - Figure 6 provides a detailed breakdown of the computational cost of different components.

3. Literature Gap Analysis:
   - The paper does not explicitly cite works discussing the general limitations of group-based RL or the challenges of real-world applications.

4. Validation Analysis:
   - The reviewer is partially correct. The paper *does* explore the impact of removing the step-level advantage, which is related to the weighting between the two levels. The ablation study in Figure 4 shows the performance impact of removing the step-level advantage entirely. The paper also provides a detailed breakdown of the computational cost in Section 5.6 and Figure 6.
   - However, the paper lacks a dedicated section discussing the sensitivity to the hyperparameter $\omega$ and potential challenges in real-world applications beyond the specific environments tested.

5. Conclusion:
   - Validity status: Partially Valid
   - Confidence level: High
   - Key supporting evidence: Ablation study in Section 5.4, computational cost analysis in Section 5.6 and Figure 6.

1. Weakness Statement:
[While the paper demonstrates improved performance on specific tasks, it does not explore the generalizability of GiGPO to a broader range of LLM agent tasks or environments. The experiments are limited to ALFWorld and WebShop, which may not fully represent the diversity of challenges encountered in real-world applications. It is unclear how GiGPO would perform in tasks with different reward structures, action spaces, or levels of stochasticity. A more comprehensive evaluation across diverse tasks would strengthen the paper's claims of general applicability.]

2. Evidence Collection:
b) Experiment-related Evidence:
   - The paper explicitly states the environments used in the experiments: "We first train the LLM agents on two challenging benchmarks: ALFWorld [ 5 ] and WebShop [ 22 ] ."
   - The paper also includes experiments on a search-augmented QA task (Section 5.2).

3. Literature Gap Analysis:
   - The paper does not explicitly discuss the limitations of the chosen benchmarks in representing the full spectrum of LLM agent tasks.

4. Validation Analysis:
   - The reviewer is partially correct. The paper focuses its primary empirical validation on ALFWorld and WebShop. While it does include experiments on a QA task, the core evaluation is limited to these two environments.
   - The paper does not provide a detailed analysis of how GiGPO would perform on tasks with significantly different characteristics (e.g., different reward structures, action spaces, or levels of stochasticity).

5. Conclusion:
   - Validity status: Partially Valid
   - Confidence level: High
   - Key supporting evidence: Experiment section focusing on ALFWorld and WebShop.

**Review 2**

1. Weakness Statement:
[- The paper could benefit from more discussion of the limitations of the approach. For example, how does GiGPO perform in environments with very long horizons or very sparse rewards? It would be helpful to see experiments on more challenging tasks with these characteristics to better understand the boundaries of the method. Specifically, the paper lacks analysis on how the grouping strategy performs when the number of trajectories per group is varied, and how this impacts the stability and convergence of the algorithm. Furthermore, the paper does not explore the sensitivity of the method to the choice of the similarity metric used for grouping trajectories, which could be a critical factor in its performance.]

2. Evidence Collection:
a) Method-related Evidence:
   - The paper describes the anchor state grouping in Section 4.2: "As all trajectories { 𝝉 1 , … , 𝝉 N } arise from the same task and identical initial conditions, many environment states naturally recur across episodes and even across time steps within a single trajectory. We leverage this redundancy by identifying and grouping identical states across trajectories, thereby dynamically constructing step-level groups."
   - The paper mentions the similarity metric in Section 4.2: "Based on this, we can construct | U | step-level groups (one for each unique anchor state 𝒔 ~ ) which is defined as follows: G S ( 𝒔 ~ ) = { ( 𝒂 t ( i ) , r t ( i ) ) | 𝒔 t ( i ) = 𝒔 ~ , 1 ≤ i ≤ N , 1 ≤ t ≤ T }."
   - The paper does not explicitly analyze the impact of varying the number of trajectories per group or the choice of similarity metric.

b) Experiment-related Evidence:
   - The paper does not include experiments specifically designed to test performance in environments with very long horizons or very sparse rewards.
   - The paper does not include ablation studies on the similarity metric.

3. Literature Gap Analysis:
   - The paper does not cite specific works discussing the limitations of grouping strategies in RL or the sensitivity to similarity metrics.

4. Validation Analysis:
   - The reviewer is correct. The paper lacks a detailed discussion and experimental analysis of the limitations of GiGPO, particularly regarding performance in very long or sparse reward environments, the impact of varying the number of trajectories per group, and the sensitivity to the similarity metric.

5. Conclusion:
   - Validity status: Valid
   - Confidence level: High
   - Key supporting evidence: Lack of discussion and experiments on these specific limitations.

1. Weakness Statement:
[- The paper does not include a detailed analysis of the computational cost of the algorithm. While the authors claim that GiGPO has the same computational cost as GRPO, a more thorough breakdown of the time and memory requirements would be valuable. For example, the cost of computing the macro and micro advantages, and the overhead of maintaining the grouping structure, should be analyzed separately. It would also be useful to see how the computational cost scales with the number of agents, trajectories, and the length of the episodes. The paper also lacks a discussion of the potential for parallelization and how this could impact the overall runtime of the algorithm.]

2. Evidence Collection:
b) Experiment-related Evidence:
   - Section 5.6 provides a "Detailed Breakdown of Per-Iteration Training Time" and Figure 6 shows the time cost of different components.
   - The paper states: "GiGPO shares the same core architecture as GRPO, including multi-turn rollouts, computation of old and reference probabilities, and clipped policy updates. Both approaches are critic-free and operate with a single actor LLM, thereby resulting in identical GPU memory usage and LLM rollout costs. The primary additions introduced by GiGPO are the step-relative advantage estimation components, as described in Section 4.2 . To evaluate their costs, we train an LLM agent in ALFWorld using Qwen2.5-1.5B-Instruct and record a detailed breakdown of per-iteration training time."

3. Literature Gap Analysis:
   - The paper does not cite specific works on analyzing the computational complexity of RL algorithms.

4. Validation Analysis:
   - The reviewer is partially incorrect. The paper *does* provide a detailed breakdown of the per-iteration training time in Section 5.6 and Figure 6, addressing the computational cost to some extent.
   - However, the analysis is presented as a comparison to GRPO and does not delve into a separate analysis of the cost of computing macro and micro advantages or the overhead of maintaining the grouping structure. The scaling of computational cost with the number of agents, trajectories, and episode length is also not explicitly analyzed.

5. Conclusion:
   - Validity status: Partially Valid
   - Confidence level: High
   - Key supporting evidence: Per-iteration training time breakdown in Section 5.6 and Figure 6.

1. Weakness Statement:
[- How does GiGPO perform in environments with very long horizons or very sparse rewards? Have you considered testing on more challenging tasks with these characteristics?]

2. Evidence Collection:
b) Experiment-related Evidence:
   - The paper's experiments are primarily on ALFWorld and WebShop, which are not explicitly described as having very long horizons or very sparse rewards. While WebShop involves multiple steps, it's not necessarily characterized by extremely long horizons compared to some other environments. The reward in WebShop is dense.

3. Literature Gap Analysis:
   - The paper does not cite specific benchmarks known for very long horizons or sparse rewards.

4. Validation Analysis:
   - The reviewer's question highlights a valid gap in the experimental evaluation. The paper does not provide specific evidence on how GiGPO performs in environments with very long horizons or very sparse rewards.

5. Conclusion:
   - Validity status: Valid
   - Confidence level: High
   - Key supporting evidence: Lack of experiments on environments with very long horizons or very sparse rewards.

1. Weakness Statement:
[- How sensitive is GiGPO to the choice of hyperparameters, particularly the weighting between macro and micro advantages?]

2. Evidence Collection:
b) Experiment-related Evidence:
   - The paper includes an ablation study in Section 5.4 that effectively examines the impact of removing the step-level advantage, which is related to the weighting. The results in Figure 4 show a significant performance drop when the step-level advantage is removed.
   - The paper mentions the weighting coefficient $\omega$ in Section 4.3 and uses a specific value of $\omega = 1$ in the experiments.

3. Literature Gap Analysis:
   - The paper does not cite specific works on hyperparameter sensitivity analysis in RL.

4. Validation Analysis:
   - The reviewer is partially incorrect. The ablation study in Section 5.4, by removing the step-level advantage, implicitly explores the sensitivity to the weighting between the two levels. The paper does not explicitly test different values of $\omega$.

5. Conclusion:
   - Validity status: Partially Valid
   - Confidence level: High
   - Key supporting evidence: Ablation study in Section 5.4.

1. Weakness Statement:
[- Can you provide more details on the computational cost of the algorithm? How does it scale with the number of agents, trajectories, and episode length?]

2. Evidence Collection:
b) Experiment-related Evidence:
   - Section 5.6 and Figure 6 provide a detailed breakdown of the per-iteration training time.
   - The paper states: "Both approaches are critic-free and operate with a single actor LLM, thereby resulting in identical GPU memory usage and LLM rollout costs."

3. Literature Gap Analysis:
   - The paper does not cite specific works on analyzing the scaling of computational cost in RL algorithms.

4. Validation Analysis:
   - The reviewer is partially incorrect. The paper provides details on the computational cost and the scaling with the number of agents and trajectories is implicitly addressed by the fact that it uses a single actor LLM and the cost breakdown is per iteration. However, the scaling with episode length is not explicitly analyzed.

5. Conclusion:
   - Validity status: Partially Valid
   - Confidence level: High
   - Key supporting evidence: Per-iteration training time breakdown in Section 5.6 and Figure 6.

**Review 3**

1. Weakness Statement:
[The paper lacks a detailed discussion of the limitations of GiGPO, such as its sensitivity to hyperparameter settings and potential challenges in real-world applications. Specifically, the paper does not explore how the weighting between episode-level and step-level advantages affects performance across different tasks. Furthermore, the computational overhead of constructing and managing step-level groups, especially in high-dimensional action spaces, is not thoroughly analyzed. A more detailed discussion of these limitations would provide a more balanced view of the algorithm's capabilities.]

2. Evidence Collection:
a) Method-related Evidence:
   - The paper introduces the weighting coefficient $\omega$ in Section 4.3.
   - The ablation study in Section 5.4 explores the impact of removing the step-level advantage, which is related to the weighting.

b) Experiment-related Evidence:
   - The ablation study in Section 5.4 shows the performance impact of removing the step-level advantage.
   - Section 5.6 and Figure 6 provide a computational cost analysis.

3. Literature Gap Analysis:
   - The paper does not cite specific works discussing the limitations of hyperparameter sensitivity in RL.

4. Validation Analysis:
   - The reviewer is partially correct. The paper does not explicitly discuss the sensitivity to the hyperparameter $\omega$ or potential challenges in real-world applications beyond the tested environments. The ablation study implicitly addresses the weighting by showing the impact of removing the step-level advantage. The computational cost is analyzed, but not specifically regarding the overhead of step-level group management in high-dimensional action spaces.

5. Conclusion:
   - Validity status: Partially Valid
   - Confidence level: High
   - Key supporting evidence: Ablation study in Section 5.4, computational cost analysis in Section 5.6 and Figure 6.

1. Weakness Statement:
[While the paper demonstrates improved performance on specific tasks, it does not explore the generalizability of GiGPO to a broader range of LLM agent tasks or environments. The experiments are limited to ALFWorld and WebShop, which may not fully represent the diversity of challenges encountered in real-world applications. It is unclear how GiGPO would perform in tasks with different reward structures, action spaces, or levels of stochasticity. A more comprehensive evaluation across diverse tasks would strengthen the paper's claims of general applicability.]

2. Evidence Collection:
b) Experiment-related Evidence:
   - The paper's experiments are primarily on ALFWorld and WebShop.

3. Literature Gap Analysis:
   - The paper does not discuss the limitations of the chosen benchmarks in representing the full spectrum of LLM agent tasks.

4. Validation Analysis:
   - The reviewer is correct. The paper's experimental evaluation is limited to ALFWorld and WebShop, and it does not provide evidence of generalizability to a broader range of tasks or environments with different characteristics.

5. Conclusion:
   - Validity status: Valid
   - Confidence level: High
   - Key supporting evidence: Experiment section focusing on ALFWorld and WebShop.

1. Weakness Statement:
[The paper would benefit from a more thorough analysis of the hyperparameter sensitivity of GiGPO. This should include a systematic exploration of how the weighting between episode-level and step-level advantages impacts performance across different tasks. For instance, the authors could perform a sensitivity analysis by varying the weighting parameter across a range of values and observing the resulting changes in performance on tasks with varying reward sparsity and task complexity. This analysis should be presented with clear visualizations, such as plots showing the performance as a function of the weighting parameter. Furthermore, the authors should investigate the computational cost of constructing and managing step-level groups, especially in high-dimensional action spaces. This could involve profiling the algorithm to identify performance bottlenecks and exploring potential optimizations, such as using more efficient data structures or parallel processing techniques. A detailed analysis of the computational overhead would provide a more complete understanding of the practical limitations of GiGPO.]

2. Evidence Collection:
b) Experiment-related Evidence:
   - The ablation study in Section 5.4 implicitly explores the weighting by removing the step-level advantage.
   - Section 5.6 provides a computational cost analysis.

3. Literature Gap Analysis:
   - The paper does not cite specific works on hyperparameter sensitivity analysis or computational cost analysis in detail.

4. Validation Analysis:
   - The reviewer is partially correct. The paper does not include a systematic sensitivity analysis of the weighting parameter across different tasks. The computational cost is analyzed, but not specifically focusing on the overhead of step-level group management in high-dimensional action spaces.

5. Conclusion:
   - Validity status: Partially Valid
   - Confidence level: High
   - Key supporting evidence: Ablation study in Section 5.4, computational cost analysis in Section 5.6 and Figure 6.

1. Weakness Statement:
[To improve the generalizability of the results, the authors should evaluate GiGPO on a more diverse set of tasks and environments. This could include tasks with different reward structures, such as sparse rewards or delayed rewards, as well as tasks with different action spaces, such as continuous action spaces or multi-modal action spaces. For example, the authors could evaluate GiGPO on tasks from the DeepMind Control Suite or other benchmark environments commonly used in reinforcement learning research. This would provide a more robust assessment of the algorithm's performance and its ability to generalize to different types of tasks. Additionally, the authors should explore the performance of GiGPO in more complex, real-world scenarios, such as those involving multi-agent interactions or partial observability. This would help to identify potential limitations of the algorithm and guide future research directions.]

2. Evidence Collection:
b) Experiment-related Evidence:
   - The paper's experiments are primarily on ALFWorld and WebShop.

3. Literature Gap Analysis:
   - The paper does not discuss the limitations of the chosen benchmarks in representing the full spectrum of LLM agent tasks.

4. Validation Analysis:
   - The reviewer is correct. The paper's experimental evaluation is limited to ALFWorld and WebShop, and it does not provide evidence of generalizability to a broader range of tasks or environments with different characteristics, including continuous or multi-modal action spaces, or more complex real-world scenarios.

5. Conclusion:
   - Validity status: Valid
   - Confidence level: High
   - Key supporting evidence: Experiment section focusing on ALFWorld and WebShop.

1. Weakness Statement:
[Finally, the authors should provide a more detailed discussion of the limitations of GiGPO, including potential challenges in real-world applications. This should include a discussion of the assumptions made by the algorithm and the conditions under which these assumptions may not hold. For example, the authors should discuss the potential impact of noisy or incomplete state information on the performance of GiGPO. They should also discuss the potential limitations of the algorithm in scenarios where the reward function is not well-defined or where the task is highly dynamic. A thorough discussion of these limitations would provide a more balanced and realistic assessment of the algorithm's capabilities and would help to guide future research in this area.]

2. Evidence Collection:
   - The paper does not have a dedicated section discussing the limitations of GiGPO.

3. Literature Gap Analysis:
   - The paper does not cite specific works discussing the limitations of its own approach or the assumptions made.

4. Validation Analysis:
   - The reviewer is correct. The paper lacks a dedicated discussion of the limitations of GiGPO, including potential challenges in real-world applications and the assumptions made by the algorithm.

5. Conclusion:
   - Validity status: Valid
   - Confidence level: High
   - Key supporting evidence: Absence of a dedicated limitations section.

1. Weakness Statement:
[How does the performance of GiGPO vary with different weighting between episode-level and step-level advantages? Are there any guidelines for selecting the optimal weighting for different tasks?]

2. Evidence Collection:
b) Experiment-related Evidence:
   - The ablation study in Section 5.4 implicitly explores this by removing the step-level advantage.

3. Literature Gap Analysis:
   - The paper does not cite specific works on hyperparameter tuning or guidelines for selecting optimal weights.

4. Validation Analysis:
   - The reviewer is partially correct. The paper does not provide a systematic analysis of how performance varies with different weighting values or guidelines for selecting the optimal weighting.

5. Conclusion:
   - Validity status: Partially Valid
   - Confidence level: High
   - Key supporting evidence: Ablation study in Section 5.4.

1. Weakness Statement:
[What are the potential limitations of GiGPO in real-world applications, particularly in scenarios with high-dimensional action spaces or complex reward structures?]

2. Evidence Collection:
   - The paper does not have a dedicated section discussing the limitations of GiGPO.

3. Literature Gap Analysis:
   - The paper does not cite specific works discussing the limitations of its own approach.

4. Validation Analysis:
   - The reviewer is correct. The paper does not explicitly discuss the potential limitations of GiGPO in real-world applications, particularly in scenarios with high-dimensional action spaces or complex reward structures.

5. Conclusion:
   - Validity status: Valid
   - Confidence level: High
   - Key supporting evidence: Absence of a dedicated limitations section.

**Review 4**

1. Weakness Statement:
[The paper introduces a hierarchical structure for advantage estimation, but the specific implementation details and the rationale behind the design choices could be further elaborated. For instance, the method for grouping trajectories and the criteria for determining the similarity of states are not fully explained. A more detailed explanation of how the grouping is performed, including the specific algorithms or heuristics used, would be beneficial. Furthermore, the choice of similarity metric for state grouping needs more justification, as different metrics could lead to different groupings and potentially impact performance.]

2. Evidence Collection:
a) Method-related Evidence:
   - The paper describes the grouping process in Section 4.2: "Based on this, we can construct | U | step-level groups (one for each unique anchor state 𝒔 ~ ) which is defined as follows: G S ( 𝒔 ~ ) = { ( 𝒂 t ( i ) , r t ( i ) ) | 𝒔 t ( i ) = 𝒔 ~ , 1 ≤ i ≤ N , 1 ≤ t ≤ T }."
   - The paper mentions the similarity metric in Section 4.2: "Based on this, we can construct | U | step-level groups (one for each unique anchor state 𝒔 ~ ) which is defined as follows: G S ( 𝒔 ~ ) = { ( 𝒂 t ( i ) , r t ( i ) ) | 𝒔 t ( i ) = 𝒔 ~ , 1 ≤ i ≤ N , 1 ≤ t ≤ T }."
   - The paper states: "In settings where only a binary reward is given, this simplification helps stabilize training in some challenging agent scenarios, potentially affecting the stability of updates. In the context of the LLM agent, where tasks often involve very long horizons, this effect tends to emerge frequently, potentially affecting the stability of updates. As an alternative, we also consider a fixed normalization factor F norm = 1, which yields an unbiased Leave-One-Out estimator [ 16 ] (see Appendix C for details)."

3. Literature Gap Analysis:
   - The paper does not cite specific works on the rationale behind the grouping strategy or the choice of similarity metric.

4. Validation Analysis:
   - The reviewer is partially correct. The paper describes the grouping process and mentions the use of cosine similarity. However, it does not provide a detailed explanation of the specific algorithms or heuristics used for grouping beyond the described method. The rationale behind the choice of cosine similarity and a more in-depth justification are missing.

5. Conclusion:
   - Validity status: Partially Valid
   - Confidence level: High
   - Key supporting evidence: Description of grouping in Section 4.2 and mention of cosine similarity.

1. Weakness Statement:
[While GiGPO is compatible with existing group-based RL algorithms, the paper could benefit from a more in-depth analysis of how GiGPO interacts with different group sizes and task complexities. The current analysis lacks a systematic exploration of how the performance of GiGPO varies with different group sizes, especially in relation to the complexity of the task. It would be valuable to see experiments that systematically vary the group size and analyze its impact on the convergence speed and final performance of the algorithm. Additionally, the paper could explore how GiGPO performs on tasks with varying levels of stochasticity, as this could reveal limitations of the approach.]

2. Evidence Collection:
b) Experiment-related Evidence:
   - The paper does not include experiments that systematically vary the group size or analyze its impact on performance or convergence speed.

3. Literature Gap Analysis:
   - The paper does not cite specific works on the impact of group size in group-based RL.

4. Validation Analysis:
   - The reviewer is correct. The paper lacks a systematic analysis of how GiGPO interacts with different group sizes and how this affects performance and convergence, especially in relation to task complexity. Experiments varying group size are missing.

5. Conclusion:
   - Validity status: Valid
   - Confidence level: High
   - Key supporting evidence: Absence of experiments varying group size.

1. Weakness Statement:
[The paper claims that GiGPO maintains the same GPU memory overhead, identical LLM rollout costs, and no additional time cost compared to existing methods. However, a more detailed breakdown of the computational costs and memory usage would be helpful to validate these claims. The current analysis lacks a detailed breakdown of the time spent on different parts of the algorithm, such as the grouping of trajectories, the computation of advantages, and the policy updates. Similarly, the memory usage should be broken down to show how much memory is used for different components of the algorithm, such as the model parameters, the trajectory data, and the grouping information. Without this detailed breakdown, it is difficult to fully assess the practical implications of the claims.]

2. Evidence Collection:
b) Experiment-related Evidence:
   - Section 5.6 provides a "Detailed Breakdown of Per-Iteration Training Time" and Figure 6 shows the time cost of different components.
   - The paper states: "GiGPO shares the same core architecture as GRPO, including multi-turn rollouts, computation of old and reference probabilities, and clipped policy updates. Both approaches are critic-free and operate with a single actor LLM, thereby resulting in identical GPU memory usage and LLM rollout costs. The primary additions introduced by GiGPO are the step-relative advantage estimation components, as described in Section 4.2 . To evaluate their costs, we train an LLM agent in ALFWorld using Qwen2.5-1.5B-Instruct and record a detailed breakdown of per-iteration training time."

3. Literature Gap Analysis:
   - The paper does not cite specific works on detailed computational cost and memory usage analysis in RL.

4. Validation Analysis:
   - The reviewer is partially incorrect. The paper provides a detailed breakdown of per-iteration training time in Section 5.6 and Figure 6, which supports the claim of no additional time cost compared to GRPO. It also states that both methods have identical GPU memory usage and LLM rollout costs. However, a more detailed breakdown of memory usage for different components is not provided.

5. Conclusion:
   - Validity status: Partially Valid
   - Confidence level: High
   - Key supporting evidence: Per-iteration training time breakdown in Section 5.6 and Figure 6.

1. Weakness Statement:
[Finally, the authors should provide a more detailed breakdown of the computational costs and memory usage of GiGPO compared to other methods. How does GiGPO maintain the same GPU memory overhead and LLM rollout costs?]

2. Evidence Collection:
b) Experiment-related Evidence:
   - Section 5.6 and Figure 6 provide a detailed breakdown of per-iteration training time.
   - The paper states: "Both approaches are critic-free and operate with a single actor LLM, thereby resulting in identical GPU memory usage and LLM rollout costs."

3. Literature Gap Analysis:
   - The paper does not cite specific works on detailed computational cost and memory usage analysis in RL.

4. Validation Analysis:
   - The reviewer is partially incorrect. The paper provides a detailed breakdown of per-iteration training time, which supports the claim of no additional time cost compared to GRPO. It also states that both methods have identical GPU memory usage and LLM rollout costs. However, a more detailed breakdown of memory usage for different components is not provided.

5. Conclusion:
   - Validity status: Partially Valid
   - Confidence level: High
   - Key supporting evidence: Per-iteration training time breakdown in Section 5.6 and Figure 6.

1. Weakness Statement:
[1. How does the performance of GiGPO vary with different group sizes, especially in tasks with varying levels of complexity? Could you provide more detailed analysis on the impact of group size on the convergence speed and final performance?]

2. Evidence Collection:
b) Experiment-related Evidence:
   - The paper does not include experiments that systematically vary the group size or analyze its impact on performance or convergence speed.

3. Literature Gap Analysis:
   - The paper does not cite specific works on the impact of group size in group-based RL.

4. Validation Analysis:
   - The reviewer is correct. The paper lacks a systematic analysis of how GiGPO interacts with different group sizes and how this affects performance and convergence, especially in relation to task complexity.

5. Conclusion:
   - Validity status: Valid
   - Confidence level: High
   - Key supporting evidence: Absence of experiments varying group size.

1. Weakness Statement:
[2. How does GiGPO handle tasks with different levels of stochasticity? Are there any limitations in the approach when dealing with highly stochastic environments?]

2. Evidence Collection:
b) Experiment-related Evidence:
   - The paper does not include experiments that specifically test the performance of GiGPO in tasks with varying levels of stochasticity.

3. Literature Gap Analysis:
   - The paper does not cite specific works on the impact of stochasticity in RL.

4. Validation Analysis:
   - The reviewer is correct. The paper does not provide specific evidence on how GiGPO handles tasks with different levels of stochasticity or its limitations in highly stochastic environments.

5. Conclusion:
   - Validity status: Valid
   - Confidence level: High
   - Key supporting evidence: Absence of experiments testing stochasticity.
}

Now, I have successfully verified each review. Next, I will organize this content and output the final review decision:

\boxed_review{
## Summary:

This paper introduces GiGPO, a novel group-based reinforcement learning algorithm designed to enhance credit assignment for Large Language Model (LLM) agents, particularly in multi-turn tasks. The core innovation of GiGPO lies in its two-level advantage estimation structure, which combines macro-level group performance comparison with micro-level credit assignment based on step-level advantages. This hierarchical approach aims to capture both global task effectiveness and local step-wise performance feedback, addressing the challenges of sparse rewards and long-horizon tasks often encountered in LLM agent training. The algorithm operates by constructing macro relative advantages from groups of complete trajectories and micro relative advantages from groups of step-level groups. These two levels of advantages are then combined to provide a comprehensive credit signal for training LLM agents. The authors demonstrate the effectiveness of GiGPO through empirical evaluations on challenging tasks such as ALFWorld and WebShop, showing significant performance improvements over existing methods. Notably, GiGPO achieves performance gains of more than 12% on these benchmarks while maintaining the same GPU memory overhead, identical LLM rollout costs, and no additional time cost compared to existing group-based RL algorithms. The paper also includes ablation studies that highlight the importance of both macro and micro advantages for achieving optimal performance. The authors emphasize that GiGPO is compatible with existing group-based RL algorithms and requires no additional model rollouts or memory usage, making it a practical and efficient solution for training LLM agents in complex environments. The paper is well-organized and clearly written, providing a logical flow that effectively communicates the motivation, methodology, and results of the proposed algorithm. Overall, GiGPO presents a significant advancement in the field of LLM agent training by offering a more effective and efficient approach to credit assignment in multi-turn tasks.


## Soundness:

3.0


## Presentation:

3.0


## Contribution:

3.0


## Strengths:

I find several aspects of this paper to be particularly strong. The most significant is the innovative two-level advantage estimation structure of GiGPO. This hierarchical approach, which combines macro and micro advantages, effectively addresses the credit assignment problem in long-horizon LLM agent training. The combination of global task effectiveness and local step-wise performance feedback provides a more nuanced and accurate credit signal, leading to more precise updates and faster convergence. This is a clear improvement over existing methods that often rely on either macro or micro-level advantages alone. The empirical results presented in the paper are also compelling. The authors demonstrate significant performance improvements on complex tasks such as ALFWorld and WebShop, with over 12% gains over previous methods. These results are achieved while maintaining the same GPU memory overhead, LLM rollout costs, and no additional time cost, which is a testament to the efficiency of the proposed algorithm. The ablation studies further strengthen the paper by clearly demonstrating the importance of both the macro and micro advantage components. The results show that removing either component leads to a substantial drop in performance, highlighting the necessity of both levels of advantage estimation. The compatibility of GiGPO with existing group-based RL algorithms is another notable strength. This design choice ensures that GiGPO can be easily integrated into current frameworks without requiring significant modifications, making it a practical and versatile tool for researchers and practitioners. The paper is also well-organized and clearly written, with a logical flow that effectively communicates the motivation, methodology, and results of the proposed algorithm. The authors provide a clear explanation of the algorithm, the experimental setup, and the results, making it easy for readers to understand and appreciate the contributions of the paper. Finally, the paper's focus on practical efficiency, with no additional rollouts or memory usage, is a significant advantage, making it a valuable contribution to the field of LLM agent training.


## Weaknesses:

Despite the strengths of this paper, I have identified several weaknesses that warrant further discussion. First, while the paper demonstrates improved performance on specific tasks, it lacks a detailed discussion of the limitations of GiGPO, particularly regarding its sensitivity to hyperparameter settings and potential challenges in real-world applications. Specifically, the paper does not explore how the weighting between episode-level and step-level advantages affects performance across different tasks. Although the ablation study in Section 5.4 implicitly addresses this by showing the performance impact of removing the step-level advantage, it does not systematically explore different values of the weighting parameter, ω, and provide clear visualizations of how performance changes with varying ω. This lack of sensitivity analysis makes it difficult to understand the optimal weighting for different tasks and limits the practical applicability of the algorithm. Furthermore, the paper does not discuss the potential impact of noisy or incomplete state information on the performance of GiGPO. This is a critical consideration for real-world applications, where state information may not always be perfect. The paper also does not discuss the potential limitations of the algorithm in scenarios where the reward function is not well-defined or where the task is highly dynamic. This lack of discussion on limitations is a significant oversight, as it prevents a balanced and realistic assessment of the algorithm's capabilities. My confidence in this weakness is high, as the paper's experimental section focuses on specific tasks and does not include a dedicated analysis of hyperparameter sensitivity or real-world limitations. 

Second, while the paper demonstrates improved performance on specific tasks, it does not explore the generalizability of GiGPO to a broader range of LLM agent tasks or environments. The experiments are primarily conducted on ALFWorld and WebShop, which may not fully represent the diversity of challenges encountered in real-world applications. The paper lacks experiments on tasks with different reward structures, such as sparse rewards or delayed rewards, as well as tasks with different action spaces, such as continuous action spaces or multi-modal action spaces. This limited evaluation scope raises concerns about the robustness and general applicability of the proposed algorithm. The paper also does not explore the performance of GiGPO in more complex, real-world scenarios, such as those involving multi-agent interactions or partial observability. This lack of evaluation on more diverse and complex tasks limits the generalizability of the results. My confidence in this weakness is high, as the paper explicitly states the environments used in the experiments and does not include any results on more diverse tasks. 

Third, the paper lacks a detailed analysis of the computational cost of the algorithm. While the authors claim that GiGPO has the same computational cost as GRPO, a more thorough breakdown of the time and memory requirements would be valuable. The paper provides a detailed breakdown of per-iteration training time in Section 5.6 and Figure 6, but it does not analyze how the computational cost scales with the number of agents, trajectories, and the length of the episodes. This lack of analysis makes it difficult to fully assess the practical implications of the algorithm's computational cost. Furthermore, the paper does not discuss the potential for parallelization and how this could impact the overall runtime of the algorithm. My confidence in this weakness is high, as the paper does not include a detailed analysis of the computational cost beyond the per-iteration breakdown. 

Finally, the paper does not provide a detailed explanation of the specific algorithms or heuristics used for grouping trajectories and the criteria for determining the similarity of states. While the paper describes the grouping process in Section 4.2 and mentions the use of cosine similarity, it does not provide a detailed explanation of the specific algorithms or heuristics used for grouping beyond the described method. The rationale behind the choice of cosine similarity and a more in-depth justification are missing. This lack of detail makes it difficult to reproduce the results and understand the underlying mechanisms of the algorithm. My confidence in this weakness is high, as the paper's description of the grouping process is relatively high-level and lacks specific algorithmic details.


## Suggestions:

To address the identified weaknesses, I recommend several concrete improvements. First, the authors should conduct a more thorough analysis of the hyperparameter sensitivity of GiGPO, particularly the weighting parameter, ω, between episode-level and step-level advantages. This should include a systematic exploration of how performance varies with different values of ω across different tasks. The authors could perform a sensitivity analysis by varying the weighting parameter across a range of values and observing the resulting changes in performance on tasks with varying reward sparsity and task complexity. This analysis should be presented with clear visualizations, such as plots showing the performance as a function of the weighting parameter. Furthermore, the authors should investigate the computational cost of constructing and managing step-level groups, especially in high-dimensional action spaces. This could involve profiling the algorithm to identify performance bottlenecks and exploring potential optimizations, such as using more efficient data structures or parallel processing techniques. A detailed analysis of the computational overhead would provide a more complete understanding of the practical limitations of GiGPO. 

Second, to improve the generalizability of the results, the authors should evaluate GiGPO on a more diverse set of tasks and environments. This could include tasks with different reward structures, such as sparse rewards or delayed rewards, as well as tasks with different action spaces, such as continuous action spaces or multi-modal action spaces. For example, the authors could evaluate GiGPO on tasks from the DeepMind Control Suite or other benchmark environments commonly used in reinforcement learning research. This would provide a more robust assessment of the algorithm's performance and its ability to generalize to different types of tasks. Additionally, the authors should explore the performance of GiGPO in more complex, real-world scenarios, such as those involving multi-agent interactions or partial observability. This would help to identify potential limitations of the algorithm and guide future research directions. 

Third, the authors should provide a more detailed analysis of the computational cost of the algorithm. This should include a breakdown of the time and memory requirements for different components of the algorithm, such as the grouping of trajectories, the computation of advantages, and the policy updates. The authors should also analyze how the computational cost scales with the number of agents, trajectories, and the length of the episodes. This analysis should be presented in a way that is easy to understand, perhaps using tables or graphs that show the computational cost as a function of these parameters. It would also be useful to discuss the potential for parallelization and how this could impact the overall runtime of the algorithm. 

Finally, the authors should provide a more detailed explanation of the specific algorithms or heuristics used for grouping trajectories and the criteria for determining the similarity of states. This should include a clear explanation of the algorithms used for grouping trajectories, the specific similarity metric employed, and the distance metric used to compute the distances between trajectories. The authors should also provide a rationale for the choice of similarity metric and distance metric, explaining why they chose a particular grouping method over other alternatives. This would allow other researchers to reproduce the results and build upon the work. The authors could also include a sensitivity analysis to show how the performance of the algorithm varies with different grouping methods and similarity metrics.


## Questions:

Based on my analysis, I have several questions that I believe are important for further understanding and development of the proposed algorithm. First, how does the performance of GiGPO vary with different weighting between episode-level and step-level advantages? While the ablation study implicitly explores this by removing the step-level advantage, I am curious about the specific impact of varying the weighting parameter, ω, across a range of values. Are there any guidelines for selecting the optimal weighting for different tasks, and how sensitive is the algorithm to this parameter? Second, what are the potential limitations of GiGPO in real-world applications, particularly in scenarios with high-dimensional action spaces or complex reward structures? The paper does not explicitly discuss these limitations, and I would like to understand the authors' perspective on the potential challenges of applying GiGPO in more complex environments. Third, how does the performance of GiGPO vary with different group sizes, especially in relation to the complexity of the task? The paper does not include experiments that systematically vary the group size, and I would like to understand how the algorithm's performance and convergence speed are affected by different group sizes. Are there any optimal group sizes for different types of tasks, and how does the algorithm handle tasks with varying levels of stochasticity? Finally, how does the computational cost of GiGPO scale with the number of agents, trajectories, and the length of the episodes? While the paper provides a per-iteration breakdown of training time, I would like to understand how the computational cost scales with these parameters and whether there are any potential bottlenecks that could limit the scalability of the algorithm. These questions are crucial for a more complete understanding of the algorithm's behavior and its practical applicability.


## Rating:

7.0


## Confidence:

3.5


## Decision:

Accept
}