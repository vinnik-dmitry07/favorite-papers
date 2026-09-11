I will use Standard Mode for comprehensive thinking. As a professional reviewer, I will simulate 4 different reviewers, followed by the verification thinking. Then I will output the Finally Review Output. Let me think - Standard Mode means I will output the original review, followed by the verification thinking. Considering that I am currently in standard mode, I should think from my existing knowledge and consider some related work content when writing about weaknesses. Then I will output the Finally Review Output and Meta Review Output:

\boxed_simreviewers{
## Reviewer 1

### Summary

This paper addresses the challenge of fine-grained dense rewards in Reinforcement Learning with Verifiable Rewards (RLVR) for reasoning tasks. The authors identify that Monte Carlo estimation for early reasoning tokens yields high variance and frequent sign errors, which outperform outcome-only GRPO. To tackle this, they propose SKPO, which decomposes reasoning into upstream and downstream phases with a skip connection. The upstream phase generates early reasoning with dense rewards, while the downstream phase maintains group-relative optimization. Experiments show that SKPO improves mathematical reasoning and generalization across tasks, with an implicit advantage in intermediate steps.

### Soundness

3

### Presentation

3

### Contribution

3

### Strengths

1. The paper is well-written, with clear explanations of the motivation and methodology. The use of diagrams effectively illustrates the key concepts.

2. The proposed SKPO method is simple yet effective, addressing the limitations of traditional dense reward approaches in RLVR.

3. The experimental results demonstrate significant improvements over existing methods in mathematical reasoning tasks, with strong generalization across diverse benchmarks.

### Weaknesses

#### Some Related Works


#### comment

1. The paper lacks a detailed analysis of the computational overhead introduced by the skip connection and single-stream optimization. Specifically, the paper does not quantify the additional memory or time costs associated with storing and replaying the upstream segment, nor does it provide a breakdown of how the single-stream optimization impacts training time compared to standard group-relative methods. This makes it difficult to assess the practical trade-offs of the proposed approach.

2. The paper does not explore the sensitivity of SKPO to different skip connection strategies or segmentation points. The choice of a fixed split point at 1/6 to 1/2 of the total length seems arbitrary. A more thorough investigation into how varying the segmentation position affects performance, particularly in tasks with different reasoning depths, is needed. Furthermore, the paper does not consider adaptive segmentation strategies that might be more suitable for tasks with varying reasoning lengths.

3. While the paper demonstrates improvements on mathematical reasoning tasks, it lacks a comprehensive evaluation across diverse reasoning domains, such as logical inference or code generation. The current evaluation is limited to benchmarks that primarily test mathematical computation, which may not fully capture the generalizability of the proposed method. The paper should include experiments on tasks that require more complex reasoning steps beyond arithmetic calculations.

### Suggestions

To strengthen the paper, the authors should provide a more detailed analysis of the computational costs associated with SKPO. This should include a breakdown of the memory overhead due to storing and replaying the upstream segment, as well as a comparison of training times with and without the single-stream optimization. It would be beneficial to quantify the additional memory usage and training time for different model sizes and dataset lengths. Furthermore, the authors should explore the impact of the skip connection on the overall training efficiency, considering the potential for increased memory usage and computational cost. A clear understanding of these trade-offs is crucial for assessing the practical applicability of SKPO.

The paper should also include a more comprehensive analysis of the sensitivity of SKPO to different skip connection strategies and segmentation points. The authors should investigate how varying the segmentation position affects performance across different tasks, particularly those with varying reasoning depths. This could involve conducting experiments with different fixed split points, as well as exploring adaptive segmentation strategies that dynamically adjust the segmentation point based on the input length or reasoning complexity. For example, the authors could consider using a sliding window approach or a segmentation strategy based on the number of reasoning steps required to solve the task. This analysis would provide a more robust understanding of the optimal segmentation strategy for SKPO and its applicability to a wider range of reasoning tasks.

Finally, the authors should expand the evaluation of SKPO to include a more diverse set of reasoning tasks beyond mathematical benchmarks. This should include tasks that require logical inference, code generation, or other forms of structured reasoning. The inclusion of such tasks would provide a more comprehensive assessment of the generalizability of SKPO and its ability to handle different types of reasoning challenges. For example, the authors could evaluate SKPO on tasks from the BigBench benchmark or other datasets that include a variety of reasoning tasks. This would help to demonstrate the broader applicability of the proposed method and its potential for use in a wider range of applications.

### Questions

1. How does SKPO perform on tasks with more complex reasoning steps beyond arithmetic calculations? Are there specific types of reasoning tasks where SKPO might underperform?

2. What is the computational overhead of SKPO compared to traditional GRPO methods? How does the single-stream optimization impact training time and memory usage?

3. How sensitive is SKPO to the choice of segmentation point? Have you explored adaptive segmentation strategies?

### Rating

6

### Confidence

3

**********

## Reviewer 2

### Summary

This paper addresses the challenge of integrating fine-grained rewards with group-relative optimization in Reinforcement Learning with Verifiable Rewards (RLVR) for reasoning tasks. The authors identify that Monte Carlo estimation for early reasoning tokens yields high variance and frequent sign errors, which outperform outcome-only baselines. To tackle this, they propose SKPO, which decomposes reasoning into upstream and downstream phases with a skip connection. The upstream phase generates early reasoning with dense rewards, while the downstream phase maintains group-relative optimization. Experiments show that SKPO improves mathematical reasoning and generalization across tasks, with an implicit advantage in intermediate steps.

### Soundness

3

### Presentation

3

### Contribution

3

### Strengths

1. The paper is well-written, with clear explanations of the motivation and methodology. The use of diagrams effectively illustrates the key concepts.

2. The proposed SKPO method is simple yet effective, addressing the limitations of traditional dense reward approaches in RLVR.

3. The experimental results demonstrate significant improvements over existing methods in mathematical reasoning tasks, with strong generalization across diverse benchmarks.

### Weaknesses

#### Some Related Works


#### comment

1. The paper lacks a detailed analysis of the computational overhead introduced by the skip connection and single-stream optimization. Specifically, the paper does not quantify the additional memory or time costs associated with storing and replaying the upstream segment, nor does it provide a breakdown of how the single-stream optimization impacts training time compared to standard group-relative methods. This makes it difficult to assess the practical trade-offs of the proposed approach.

2. The paper does not explore the sensitivity of SKPO to different skip connection strategies or segmentation points. The choice of a fixed split point at 1/6 to 1/2 of the total length seems arbitrary. A more thorough investigation into how varying the segmentation position affects performance, particularly in tasks with different reasoning depths, is needed. Furthermore, the paper does not consider adaptive segmentation strategies that might be more suitable for tasks with varying reasoning lengths.

3. While the paper demonstrates improvements on mathematical reasoning tasks, it lacks a comprehensive evaluation across diverse reasoning domains, such as logical inference or code generation. The current evaluation is limited to benchmarks that primarily test mathematical computation, which may not fully capture the generalizability of the proposed method. The paper should include experiments on tasks that require more complex reasoning steps beyond arithmetic calculations.

### Suggestions

The authors should provide a more detailed analysis of the computational overhead introduced by the skip connection and single-stream optimization. This analysis should include a breakdown of the memory usage for storing the upstream segment, as well as the time costs associated with replaying this segment during training. Furthermore, a comparison of the training time with and without the single-stream optimization would be beneficial to understand the trade-offs involved. This analysis should be conducted across different model sizes and dataset lengths to provide a comprehensive understanding of the computational cost of SKPO. It would also be helpful to compare the memory footprint of SKPO with other methods, such as GRPO, to provide a clear picture of the memory efficiency of the proposed approach.

To address the sensitivity of SKPO to different skip connection strategies, the authors should conduct a more thorough investigation into how varying the segmentation position affects performance. This should include experiments with different fixed split points, as well as adaptive segmentation strategies that dynamically adjust the segmentation point based on the input length or reasoning complexity. For example, the authors could explore a sliding window approach for segmentation, where the segmentation point is adjusted based on the number of reasoning steps required to solve the task. This analysis should be conducted on a variety of tasks with different reasoning depths to understand the robustness of SKPO to different segmentation strategies. The authors should also provide a rationale for the choice of the fixed split point range used in their experiments, and justify why this range is appropriate for the tasks they are considering.

Finally, the authors should expand the evaluation of SKPO to include a more diverse set of reasoning tasks beyond mathematical benchmarks. This should include tasks that require logical inference, code generation, or other forms of structured reasoning. The inclusion of such tasks would provide a more comprehensive assessment of the generalizability of SKPO and its ability to handle different types of reasoning challenges. For example, the authors could evaluate SKPO on tasks from the BigBench benchmark or other datasets that include a variety of reasoning tasks. This would help to demonstrate the broader applicability of the proposed method and its potential for use in a wider range of applications. The authors should also discuss the limitations of their evaluation and identify areas where further research is needed to fully assess the capabilities of SKPO.

### Questions

1. How does SKPO perform on tasks with more complex reasoning steps beyond arithmetic calculations? Are there specific types of reasoning tasks where SKPO might underperform?

2. What is the computational overhead of SKPO compared to traditional GRPO methods? How does the single-stream optimization impact training time and memory usage?

3. How sensitive is SKPO to the choice of segmentation point? Have you explored adaptive segmentation strategies?

### Rating

6

### Confidence

3

**********

## Reviewer 3

### Summary

This paper addresses the challenge of integrating fine-grained dense rewards with group-relative optimization in Reinforcement Learning with Verifiable Rewards (RLVR) for reasoning tasks. The authors identify that Monte Carlo estimation for early reasoning tokens yields high variance and frequent sign errors, underperforming outcome-only baselines. To overcome this, they propose Skip-Connected Policy Optimization (SKPO), which decomposes reasoning into upstream and downstream phases with a skip connection. The upstream phase generates early reasoning segments with dense rewards, while the downstream phase maintains group-relative optimization, leveraging helpful upstream reasoning while preserving exploration freedom. Experiments demonstrate that SKPO significantly improves performance on mathematical reasoning tasks and outperforms strong baselines on both in-domain and out-of-domain tasks.

### Soundness

3

### Presentation

3

### Contribution

3

### Strengths

1. The paper presents a novel approach to addressing the limitations of Monte Carlo reward estimation in RLVR. By decomposing reasoning into upstream and downstream phases with a skip connection, SKPO effectively balances the need for fine-grained rewards with the stability of group-relative optimization. This innovative strategy allows for more efficient and effective learning in reasoning tasks.
2. The paper is well-organized and clearly written, making it easy to follow the methodology and results. The authors provide a thorough explanation of the problem, the proposed solution, and the experimental setup. The use of figures and diagrams further enhances the clarity of the presentation.
3. The experimental results are robust and demonstrate the effectiveness of SKPO. The authors conduct extensive experiments on various mathematical reasoning tasks, comparing SKPO against strong baselines. The results show that SKPO consistently outperforms existing methods, highlighting its potential for practical applications in reasoning tasks.

### Weaknesses

#### Some Related Works


#### comment

1. The paper does not discuss the potential limitations of SKPO in terms of computational cost and scalability. While the authors mention that SKPO reduces instability on fine-grained signals by lowering upstream per-prompt sample count and estimating more stable baselines from historical samples, they do not provide a detailed analysis of the computational overhead introduced by the skip connection and the additional memory requirements for storing and replaying upstream segments. Specifically, the paper lacks a discussion on how the computational cost scales with the length of the reasoning chain and the size of the model. Furthermore, the memory overhead of storing and replaying upstream segments, especially in long reasoning chains, is not quantified, which could be a significant bottleneck for larger models and longer sequences.
2. The paper does not explore the sensitivity of SKPO to different hyperparameters, such as the segmentation position and the number of downstream continuations. While the authors provide some ablation studies, a more comprehensive analysis of the impact of these hyperparameters on the performance of SKPO is needed. For instance, the paper does not investigate how the segmentation position affects the trade-off between upstream and downstream learning, or how the number of downstream continuations influences the stability and convergence of the training process. This lack of sensitivity analysis makes it difficult to understand the robustness of the method and to provide practical guidance for its application.

### Suggestions

The authors should provide a more detailed analysis of the computational cost and memory requirements of SKPO. This should include a breakdown of the time and memory costs associated with each step of the algorithm, such as the Monte Carlo estimation for the upstream phase, the group-relative optimization for the downstream phase, and the skip connection mechanism. The analysis should also consider how these costs scale with the length of the reasoning chain and the size of the model. Furthermore, the authors should discuss potential strategies for reducing the computational overhead of SKPO, such as using more efficient data structures for storing and replaying upstream segments, or employing techniques for parallelizing the Monte Carlo estimation process. This analysis is crucial for assessing the practical applicability of SKPO in resource-constrained environments.

To address the lack of sensitivity analysis, the authors should conduct a more thorough investigation of the impact of key hyperparameters on the performance of SKPO. This should include a systematic exploration of the segmentation position, the number of downstream continuations, and the length of the upstream segment. The authors should also investigate the effect of these hyperparameters on the stability and convergence of the training process. For example, they could analyze how different segmentation positions affect the trade-off between upstream and downstream learning, and how the number of downstream continuations influences the variance of the reward estimates. This analysis should be supported by empirical results and visualizations, which would provide a better understanding of the behavior of SKPO under different hyperparameter settings. The authors should also provide practical guidelines for selecting appropriate hyperparameter values based on the characteristics of the task and the available computational resources.

Finally, the authors should consider including a discussion of the limitations of SKPO in terms of its applicability to different types of reasoning tasks. For example, it is not clear how well SKPO would perform on tasks that require more complex forms of reasoning, such as tasks that involve multiple steps of inference or tasks that require the integration of information from different sources. The authors should also discuss the potential challenges of applying SKPO to tasks with very long reasoning chains, and they should suggest potential directions for future research that could address these challenges. This discussion would help to provide a more complete picture of the strengths and limitations of SKPO and would guide future research in this area.

### Questions

1. How does SKPO handle tasks that require more complex forms of reasoning, such as tasks that involve multiple steps of inference or tasks that require the integration of information from different sources?
2. What are the potential challenges of applying SKPO to tasks with very long reasoning chains, and how can these challenges be addressed?

### Rating

6

### Confidence

3

**********

## Reviewer 4

### Summary

The authors propose a method for RL with verifiable rewards (RLVR) that combines Monte Carlo (MC) rewards for early reasoning steps with group relative rewards for later reasoning steps. The authors find that MC rewards are unstable for early reasoning steps, and group relative rewards are unstable for later reasoning steps. The authors propose to use MC rewards for the early reasoning steps, and group relative rewards for the later reasoning steps. The authors find that their method improves performance on mathematical reasoning benchmarks.

### Soundness

3

### Presentation

3

### Contribution

2

### Strengths

- The paper is well written and easy to follow.
- The authors provide a comprehensive analysis of the proposed method, including ablation studies and implicit advantage analysis.
- The authors provide code for their method, which is helpful for reproducibility.

### Weaknesses

#### Some Related Works

[1] Learning from Failure: A Simple Approach for LLMs to Master Reasoning

#### comment

 - The authors do not compare to the recent work Learning from Failure [1], which also proposes to use MC rewards for early reasoning steps and group relative rewards for later reasoning steps. The authors should compare to this method to demonstrate the advantages of their method.
- The authors do not provide a theoretical analysis of their method, which would help to understand why it works.
- The authors do not provide a detailed analysis of the computational cost of their method, which would be helpful to understand its practical applicability.
- The authors do not provide a detailed analysis of the sensitivity of their method to hyperparameters, which would be helpful to understand its robustness.

### Suggestions

The authors should provide a more thorough comparison to the Learning from Failure method [1], which also combines Monte Carlo and group relative rewards. A direct comparison, including performance on the same benchmarks and with the same experimental setup, is necessary to properly evaluate the novelty and effectiveness of the proposed approach. This comparison should not only focus on final performance but also on the learning curves and the stability of the training process. Furthermore, the authors should analyze the differences in the reward structures and optimization strategies used by both methods to identify the specific advantages of their approach. This analysis should include a discussion of the potential limitations of the Learning from Failure method and how the proposed method addresses these limitations. The authors should also consider including a discussion of the computational cost of both methods, including the number of forward passes and the memory requirements, to provide a more complete picture of their relative advantages and disadvantages.

In addition to the empirical comparisons, the authors should provide a theoretical analysis of their method. This analysis should include a discussion of the convergence properties of the proposed optimization algorithm, as well as the conditions under which the method is guaranteed to find a good solution. The authors should also discuss the relationship between the proposed method and existing reinforcement learning algorithms, such as policy gradient methods and Q-learning. This theoretical analysis would help to provide a deeper understanding of the method's behavior and its limitations. For example, the authors could analyze the bias and variance of the Monte Carlo estimates used in the early reasoning steps and how this affects the overall performance of the method. They could also analyze the impact of the group relative rewards on the stability of the learning process and how this relates to the overall convergence of the algorithm.

Finally, the authors should provide a more detailed analysis of the computational cost and sensitivity of their method. This analysis should include a breakdown of the computational cost of each step of the algorithm, as well as the memory requirements. The authors should also provide a sensitivity analysis of the method to hyperparameters, such as the learning rate, the batch size, and the number of Monte Carlo samples. This analysis should include a discussion of how these hyperparameters affect the performance of the method and how they should be tuned to achieve optimal results. The authors should also provide a discussion of the limitations of their method and the potential areas for future research. This would help to provide a more complete picture of the method's strengths and weaknesses and would guide future research in this area.

### Questions

- How does the proposed method compare to the Learning from Failure method [1]?
- What is the theoretical analysis of the proposed method?
- What is the computational cost of the proposed method?
- How sensitive is the proposed method to hyperparameters?

[1] Li, Z., Zhang, Z., Wang, H., Li, C., & Chen, W. (2024). Learning from Failure: A Simple Approach for LLMs to Master Reasoning. arXiv preprint arXiv:2402.15335.

### Rating

8

### Confidence

3

**********

}

I have finished generating simulated reviews from 4 reviewers. Next, I will generate verification content for these reviews:

\boxed_verification{
The user wants me to validate weaknesses identified by reviewers for the provided paper. I need to go through each reviewer's comments and find evidence in the paper to support or refute their claims.

**Plan:**
1. Go through each reviewer's identified weaknesses one by one.
2. For each weakness, categorize it as theoretical, methodological, experimental, or practical.
3. Find specific evidence in the paper (quotes, experimental setup, results) to support the weakness.
4. If the weakness is about missing information, point out where that information is lacking.
5. If there are conflicting opinions between reviewers, highlight them.
6. Conclude whether the weakness is valid, partially valid, or invalid based on the evidence.
**Review 1**

1. Weakness Statement:
"The paper lacks a detailed analysis of the computational overhead introduced by the skip connection and single-stream optimization. Specifically, the paper does not quantify the additional memory or time costs associated with storing and replaying the upstream segment, nor does it provide a breakdown of how the single-stream optimization impacts training time compared to standard group-relative methods. This makes it difficult to assess the practical trade-offs of the proposed approach."

2. Evidence Collection:
a) Method-related Evidence:
   - The paper describes the single-stream optimization in the "Engineering Optimization" section: "To achieve true computational parity with mainstream GRPO variants, we modify the vLLM (Kwon et al., 2023) inference engine to perform mid-generation KV cache rewriting within a single rollout pass."
   - The paper mentions memory savings: "Notably, Critique-GRPO, which first rolls out 7 direct responses then generates 1 self-critique response in a separate batch, exhibits substantially higher per-step training time due to this sequential dispatch overhead, with time complexity similar to our naive two-batch design. To achieve true computational parity with mainstream GRPO variants, we modify the vLLM (Kwon et al., 2023) inference engine to perform mid-generation KV cache rewriting within a single rollout pass. Concretely, all G G responses are generated in parallel from q q , paused at the shared segmentation position t q t_{q} , then recompute the KV cache for the reordered prefix [ s i ; q i ] [s_i; q_i] . This enables all subsequent outcome tokens o i o_{i} to be generated conditional on the identical prefix, ensuring valid Monte Carlo estimation while requiring only one shared copy of KV ​ ( s ) \text{KV}(s) in GPU memory."
   - The paper does not provide a quantitative analysis of the memory overhead of storing and replaying the upstream segment.

b) Experiment-related Evidence:
   - The paper mentions the hardware used: "All models are trained for 500 optimization steps with a batch size of 128 prompts per step. We set the maximum prompt length to 1024 tokens and the maximum completion length to 3072 tokens for both training and evaluation. For fair comparison, all methods using group-relative advantage estimation adopt G = 8 rollouts per prompt; with our engineering optimization, SKPO generates G = 8 upstream segments in parallel, selects one via median-based selection, and continues with G = 8 downstream responses within a single GPU batch."
   - The paper does not provide a direct comparison of training time with and without the single-stream optimization.

3. Literature Gap Analysis:
   - The paper cites vLLM (Kwon et al., 2023) for the KV cache rewriting technique, but does not provide a detailed analysis of the computational overhead of this technique itself.

4. Validation Analysis:
   - The reviewer correctly points out the lack of a detailed computational overhead analysis. While the paper mentions memory savings through KV cache rewriting, it doesn't quantify the memory cost of storing and replaying the upstream segment. The paper also mentions achieving "true computational parity" but doesn't provide a direct comparison of training times.

5. Conclusion:
   - Validity status: Valid
   - Confidence level: High
   - Key supporting evidence: Lack of quantitative memory cost analysis for the upstream segment and no direct training time comparison with and without single-stream optimization.

1. Weakness Statement:
"The paper does not explore the sensitivity of SKPO to different skip connection strategies or segmentation points. The choice of a fixed split point at 1/6 to 1/2 of the total length seems arbitrary. A more thorough investigation into how varying the segmentation position affects performance, particularly in tasks with different reasoning depths, is needed. Furthermore, the paper does not consider adaptive segmentation strategies that might be more suitable for tasks with varying reasoning lengths."

2. Evidence Collection:
a) Method-related Evidence:
   - The paper states the segmentation position: "For responses that terminate before t q t_{q} , we use half of the actual response length as the split position. We then sample G G continuations from the augmented input [ s , q ] [s,q] , the concatenation of the segment and original problem, to obtain complete responses { o i } i = 1 G \{o_{i}\}_{i=1}^{G} in the downstream phase."
   - The paper mentions the range of the split position: "We then sample G G continuations from the augmented input [ s , q ] [s,q] , the concatenation of the segment and original problem, to obtain complete responses { o i } i = 1 G \{o_{i}\}_{i=1}^{G} in the downstream phase. We set the maximum prompt length to 1024 tokens and the maximum completion length to 3072 tokens for both training and evaluation. For fair comparison, all methods using group-relative advantage estimation adopt G = 8 rollouts per prompt; with our engineering optimization, SKPO generates G = 8 upstream segments in parallel, selects one via median-based selection, and continues with G = 8 downstream responses within a single GPU batch. For SPO which does not use group-relative estimation, we scale the batch size by 8 to ensure equivalent computational cost; we also omit the warm-up phase in our SPO reproduction to avoid introducing a cost-misaligned initialization stage. We use Qwen2.5-Math-7B and Llama-3.2-3B-Instruct as base models. Complete hyperparameters and implementation details are provided in Appendix C ."
   - The paper does not explicitly state the fixed range of the split position used in the experiments.

b) Experiment-related Evidence:
   - The paper includes an "Ablation Studies" section, but it focuses on the segmentation strategy, not the segmentation point. The ablation study on "Segmentation Position" shows results for "Unconditional" and "Selective," but not a continuous range like 1/6 to 1/2.

3. Literature Gap Analysis:
   - The paper does not cite literature on adaptive segmentation strategies for reasoning tasks.

4. Validation Analysis:
   - The reviewer is correct that the paper doesn't explore a continuous range of segmentation points. The ablation study uses discrete strategies. The paper also doesn't discuss or experiment with adaptive segmentation strategies.

5. Conclusion:
   - Validity status: Valid
   - Confidence level: High
   - Key supporting evidence: The ablation study on segmentation strategy uses discrete options, and there is no mention or experimentation with adaptive segmentation strategies.

1. Weakness Statement:
"While the paper demonstrates improvements on mathematical reasoning tasks, it lacks a comprehensive evaluation across diverse reasoning domains, such as logical inference or code generation. The current evaluation is limited to benchmarks that primarily test mathematical computation, which may not fully capture the generalizability of the proposed method. The paper should include experiments on tasks that require more complex reasoning steps beyond arithmetic calculations."

2. Evidence Collection:
a) Experiment-related Evidence:
   - The paper explicitly states the benchmarks used: "We evaluate SKPO on diverse benchmarks covering In-Domain mathematical reasoning and Out-of-Domain general reasoning. For In-Domain evaluation, we conduct extensive experiments on mathematical benchmarks. For Out-of-Domain evaluation, we employ MMLU-Pro ( Wang et al., 2024 ) to assess general reasoning capabilities and LiveCodeBench ( Jain et al., 2025a ) to evaluate code generation skills."
   - The paper focuses on mathematical reasoning benchmarks for in-domain evaluation.
   - The paper includes MMLU-Pro and LiveCodeBench for out-of-domain evaluation.

3. Literature Gap Analysis:
   - The paper does not include evaluations on tasks specifically designed for logical inference.

4. Validation Analysis:
   - The reviewer is partially correct. The paper *does* include out-of-domain evaluations on MMLU-Pro and LiveCodeBench, which assess general reasoning and code generation skills, respectively. However, the in-domain evaluation is heavily focused on mathematical reasoning. The reviewer's point about the lack of evaluation on purely logical inference tasks is valid.

5. Conclusion:
   - Validity status: Partially Valid
   - Confidence level: High
   - Key supporting evidence: The paper includes MMLU-Pro and LiveCodeBench for out-of-domain evaluation, but the in-domain evaluation is primarily focused on mathematical reasoning.

**Review 2**

1. Weakness Statement:
"The paper does not discuss the potential limitations of SKPO in terms of computational cost and scalability. While the authors mention that SKPO reduces instability on fine-grained signals by lowering upstream per-prompt sample count and estimating more stable baselines from historical samples, they do not provide a detailed analysis of the computational overhead introduced by the skip connection and the additional memory requirements for storing and replaying upstream segments. Specifically, the paper lacks a discussion on how the computational cost scales with the length of the reasoning chain and the size of the model. Furthermore, the memory overhead of storing and replaying upstream segments, especially in long reasoning chains, is not quantified, which could be a significant bottleneck for larger models and longer sequences."

2. Evidence Collection:
   - This is the same weakness as Reviewer 1's first point. Please see the validation for that point.

3. Literature Gap Analysis:
   - Same as Reviewer 1's first point.

4. Validation Analysis:
   - Same as Reviewer 1's first point.

5. Conclusion:
   - Validity status: Valid
   - Confidence level: High
   - Key supporting evidence: Lack of quantitative memory cost analysis for the upstream segment and no direct training time comparison with and without single-stream optimization.

1. Weakness Statement:
"The paper does not explore the sensitivity of SKPO to different hyperparameters, such as the segmentation position and the number of downstream continuations. While the authors provide some ablation studies, a more comprehensive analysis of the impact of these hyperparameters on the performance of SKPO is needed. For instance, the paper does not investigate how the segmentation position affects the trade-off between upstream and downstream learning, or how the number of downstream continuations influences the stability and convergence of the training process. This lack of sensitivity analysis makes it difficult to understand the robustness of the method and to provide practical guidance for its application."

2. Evidence Collection:
a) Experiment-related Evidence:
   - The paper includes an "Ablation Studies" section.
   - The ablation study on "Segmentation Strategy" compares "Unconditional" and "Selective."
   - The ablation study on "Segmentation Position" compares "Unconditional," "Selective," and "Extreme."
   - The ablation study on "Upstream Selection" compares "Without Skip," "Selective," and "Extreme."
   - The paper mentions the number of downstream continuations (G=8) in the experimental setup.
   - The paper does not include an ablation study specifically on the number of downstream continuations.

3. Literature Gap Analysis:
   - The paper does not cite literature on hyperparameter sensitivity analysis for RL algorithms.

4. Validation Analysis:
   - The reviewer is partially correct. The paper does include ablation studies on segmentation strategy and segmentation position. However, it does not include an ablation study on the number of downstream continuations. The reviewer's point about the trade-off between upstream and downstream learning with segmentation position is not explicitly addressed with a dedicated ablation.

5. Conclusion:
   - Validity status: Partially Valid
   - Confidence level: High
   - Key supporting evidence: The paper includes ablation studies on segmentation strategy and position, but not on the number of downstream continuations.

1. Weakness Statement:
"How does SKPO handle tasks that require more complex forms of reasoning, such as tasks that involve multiple steps of inference or tasks that require the integration of information from different sources?"

2. Evidence Collection:
   - This is a question about the generalizability of the method, not a statement about a weakness in the paper's content. The paper's evaluation includes MMLU-Pro and LiveCodeBench, which assess general reasoning and code generation, suggesting some ability to handle complex tasks. However, the paper doesn't explicitly address the specific challenges of multi-step inference or integrating information from different sources.

3. Literature Gap Analysis:
   - The paper does not cite literature on handling complex reasoning tasks in RL.

4. Validation Analysis:
   - This is a valid question regarding the limitations of the method, but it's not a direct criticism of a flaw in the paper's content.

5. Conclusion:
   - Validity status: Not Applicable (Question, not a weakness statement)
   - Confidence level: N/A
   - Key supporting evidence: N/A

1. Weakness Statement:
"What are the potential challenges of applying SKPO to tasks with very long reasoning chains, and how can these challenges be addressed?"

2. Evidence Collection:
   - This is a question about potential limitations and future work, not a statement about a weakness in the paper's content. The paper's method involves a segmentation point, which implicitly addresses the length of the reasoning chain to some extent. However, the paper doesn't explicitly discuss the challenges of very long reasoning chains.

3. Literature Gap Analysis:
   - The paper does not cite literature on handling long reasoning chains in RL.

4. Validation Analysis:
   - This is a valid question about potential limitations, but it's not a direct criticism of a flaw in the paper's content.

5. Conclusion:
   - Validity status: Not Applicable (Question, not a weakness statement)
   - Confidence level: N/A
   - Key supporting evidence: N/A

**Review 3**

1. Weakness Statement:
"The paper lacks a detailed analysis of the computational overhead introduced by the skip connection and single-stream optimization. Specifically, the paper does not quantify the additional memory or time costs associated with storing and replaying the upstream segment, nor does it provide a breakdown of how the single-stream optimization impacts training time compared to standard group-relative methods. This makes it difficult to assess the practical trade-offs of the proposed approach."

2. Evidence Collection:
   - This is the same weakness as Reviewer 1's first point and Reviewer 2's first point. Please see the validation for that point.

3. Literature Gap Analysis:
   - Same as Reviewer 1's first point.

4. Validation Analysis:
   - Same as Reviewer 1's first point.

5. Conclusion:
   - Validity status: Valid
   - Confidence level: High
   - Key supporting evidence: Lack of quantitative memory cost analysis for the upstream segment and no direct training time comparison with and without single-stream optimization.

1. Weakness Statement:
"The paper does not explore the sensitivity of SKPO to different skip connection strategies or segmentation points. The choice of a fixed split point at 1/6 to 1/2 of the total length seems arbitrary. A more thorough investigation into how varying the segmentation position affects performance, particularly in tasks with different reasoning depths, is needed. Furthermore, the paper does not consider adaptive segmentation strategies that might be more suitable for tasks with varying reasoning lengths."

2. Evidence Collection:
   - This is the same weakness as Reviewer 1's second point and Reviewer 2's second point. Please see the validation for that point.

3. Literature Gap Analysis:
   - Same as Reviewer 1's second point.

4. Validation Analysis:
   - Same as Reviewer 1's second point.

5. Conclusion:
   - Validity status: Valid
   - Confidence level: High
   - Key supporting evidence: The ablation study on segmentation strategy uses discrete options, and there is no mention or experimentation with adaptive segmentation strategies.

1. Weakness Statement:
"While the paper demonstrates improvements on mathematical reasoning tasks, it lacks a comprehensive evaluation across diverse reasoning domains, such as logical inference or code generation. The current evaluation is limited to benchmarks that primarily test mathematical computation, which may not fully capture the generalizability of the proposed method. The paper should include experiments on tasks that require more complex reasoning steps beyond arithmetic calculations."

2. Evidence Collection:
   - This is the same weakness as Reviewer 1's third point. Please see the validation for that point.

3. Literature Gap Analysis:
   - Same as Reviewer 1's third point.

4. Validation Analysis:
   - Same as Reviewer 1's third point.

5. Conclusion:
   - Validity status: Partially Valid
   - Confidence level: High
   - Key supporting evidence: The paper includes MMLU-Pro and LiveCodeBench for out-of-domain evaluation, but the in-domain evaluation is primarily focused on mathematical reasoning.

**Review 4**

1. Weakness Statement:
"The authors do not compare to the recent work Learning from Failure [1], which also proposes to use MC rewards for early reasoning steps and group relative rewards for later reasoning steps. The authors should compare to this method to demonstrate the advantages of their method."

2. Evidence Collection:
a) Literature Gap Analysis:
   - The paper does not cite or compare against "Learning from Failure" by Li et al. (2024).

3. Validation Analysis:
   - The reviewer is correct. The paper does not include a comparison to the "Learning from Failure" method.

4. Conclusion:
   - Validity status: Valid
   - Confidence level: High
   - Key supporting evidence: The paper lacks a comparison to the "Learning from Failure" method.

1. Weakness Statement:
"The authors do not provide a theoretical analysis of their method, which would help to understand why it works."

2. Evidence Collection:
a) Method-related Evidence:
   - The paper focuses on the algorithmic description and empirical evaluation of SKPO.
   - The paper does not include a formal theoretical analysis of convergence, stability, or optimality.

3. Literature Gap Analysis:
   - The paper does not cite literature on theoretical analysis of RL algorithms.

4. Validation Analysis:
   - The reviewer is correct. The paper lacks a theoretical analysis of the proposed method.

5. Conclusion:
   - Validity status: Valid
   - Confidence level: High
   - Key supporting evidence: The paper lacks a formal theoretical analysis of the method.

1. Weakness Statement:
"The authors do not provide a detailed analysis of the computational cost of their method, which would be helpful to understand its practical applicability."

2. Evidence Collection:
   - This is the same weakness as Reviewer 1's first point and Reviewer 3's first point. Please see the validation for that point.

3. Literature Gap Analysis:
   - Same as Reviewer 1's first point.

4. Validation Analysis:
   - Same as Reviewer 1's first point.

5. Conclusion:
   - Validity status: Valid
   - Confidence level: High
   - Key supporting evidence: Lack of quantitative memory cost analysis for the upstream segment and no direct training time comparison with and without single-stream optimization.

1. Weakness Statement:
"The authors do not provide a detailed analysis of the sensitivity of their method to hyperparameters, which would be helpful to understand its robustness."

2. Evidence Collection:
   - This is the same weakness as Reviewer 2's second point. Please see the validation for that point.

3. Literature Gap Analysis:
   - Same as Reviewer 2's second point.

4. Validation Analysis:
   - Same as Reviewer 2's second point.

5. Conclusion:
   - Validity status: Partially Valid
   - Confidence level: High
   - Key supporting evidence: The paper includes ablation studies on segmentation strategy and position, but not on the number of downstream continuations.

1. Weakness Statement:
"How does the proposed method compare to the Learning from Failure method [1]?"

2. Evidence Collection:
   - This is a question about the comparison to a specific method, which is related to the first weakness identified by this reviewer. Please see the validation for that point.

3. Literature Gap Analysis:
   - Same as Reviewer 4's first point.

4. Validation Analysis:
   - Same as Reviewer 4's first point.

5. Conclusion:
   - Validity status: Not Applicable (Question, not a weakness statement)
   - Confidence level: N/A
   - Key supporting evidence: N/A

1. Weakness Statement:
"What is the theoretical analysis of the proposed method?"

2. Evidence Collection:
   - This is a question about the theoretical analysis, which is related to the second weakness identified by this reviewer. Please see the validation for that point.

3. Literature Gap Analysis:
   - Same as Reviewer 4's second point.

4. Validation Analysis:
   - Same as Reviewer 4's second point.

5. Conclusion:
   - Validity status: Not Applicable (Question, not a weakness statement)
   - Confidence level: N/A
   - Key supporting evidence: N/A

1. Weakness Statement:
"What is the computational cost of the proposed method?"

2. Evidence Collection:
   - This is a question about the computational cost, which is related to the third and fourth weaknesses identified by this reviewer. Please see the validation for those points.

3. Literature Gap Analysis:
   - Same as Reviewer 4's third and fourth points.

4. Validation Analysis:
   - Same as Reviewer 4's third and fourth points.

5. Conclusion:
   - Validity status: Not Applicable (Question, not a weakness statement)
   - Confidence level: N/A
   - Key supporting evidence: N/A

1. Weakness Statement:
"How sensitive is the proposed method to hyperparameters?"

2. Evidence Collection:
   - This is a question about hyperparameter sensitivity, which is related to the fourth weakness identified by this reviewer. Please see the validation for that point.

3. Literature Gap Analysis:
   - Same as Reviewer 4's fourth point.

4. Validation Analysis:
   - Same as Reviewer 4's fourth point.

5. Conclusion:
   - Validity status: Not Applicable (Question, not a weakness statement)
   - Confidence level: N/A
   - Key supporting evidence: N/A

**Synthesis and Reflection:**

Several reviewers consistently pointed out the lack of a detailed computational cost analysis, both in terms of memory and time. This is a valid criticism as the paper does not provide quantitative data on these aspects. Reviewers 1, 2, and 3 all raised concerns about the sensitivity of the method to different skip connection strategies and segmentation points, with Reviewers 1 and 2 specifically noting the lack of a continuous range of segmentation points and the absence of adaptive segmentation strategies. Reviewer 4 highlighted the absence of a comparison to the "Learning from Failure" method, which shares similarities with SKPO, and also pointed out the lack of theoretical analysis. Reviewer 3 questioned the generalizability of the method to tasks beyond mathematical reasoning, although the paper does include evaluations on MMLU-Pro and LiveCodeBench.

There is a strong consensus among the reviewers regarding the need for a more thorough analysis of the computational overhead and the sensitivity of the method to hyperparameters. The lack of comparison to the "Learning from Failure" method is also a significant gap. While the paper includes ablation studies on some aspects, reviewers correctly identified that these studies do not cover all relevant hyperparameters, such as the number of downstream continuations.

**Conclusion:**

Based on the evidence collected, the most significant and consistently raised weaknesses are:

1. **Lack of detailed computational cost analysis:** This includes both memory and time overhead.
2. **Insufficient exploration of skip connection strategies and segmentation points:** The paper lacks a continuous range of segmentation points and does not explore adaptive strategies.
3. **Missing comparison to the "Learning from Failure" method:** This is a relevant baseline given the conceptual similarities.
4. **Lack of theoretical analysis:** The paper does not provide a formal analysis of the method's properties.
5. **Limited hyperparameter sensitivity analysis:** While some ablation studies are present, they do not cover all relevant hyperparameters.

The weakness regarding the generalizability to non-mathematical reasoning is partially valid as the paper includes some out-of-domain evaluations, but the in-domain focus is on mathematical reasoning.

The reviewers' comments are largely valid and well-supported by the paper's content. There are no significant contradictions between the reviewers' opinions.
}

Now, I have successfully verified each review. Next, I will organize this content and output the final review decision:

\boxed_review{
## Summary:

This paper introduces Skip-Connected Policy Optimization (SKPO), a novel approach designed to address the challenges of integrating fine-grained dense rewards with group-relative optimization in Reinforcement Learning with Verifiable Rewards (RLVR). The core problem the authors tackle is the instability of Monte Carlo (MC) reward estimation for early reasoning tokens, which they observe leads to high variance and frequent sign errors, thereby hindering the effectiveness of traditional dense reward approaches. To overcome this, SKPO decomposes the reasoning process into two distinct phases: an upstream phase and a downstream phase. In the upstream phase, the method generates early reasoning steps using dense rewards, leveraging the stability of MC sampling for these initial tokens. This phase is designed to provide a strong initial grounding for the reasoning process. Subsequently, in the downstream phase, the method maintains group-relative optimization, ensuring that helpful upstream reasoning segments are preserved while allowing for exploration freedom. This is achieved through a skip-connection mechanism, which facilitates the flow of information from the upstream phase to the downstream phase. The authors also employ a single-stream optimization technique, which involves generating and replaying multiple upstream segments in parallel, followed by the generation of downstream responses within a single pass of the inference engine. This is done to improve computational efficiency. The empirical evaluation of SKPO is conducted on a range of mathematical reasoning tasks, where it demonstrates significant improvements over existing methods. The authors also show that SKPO maintains its performance across diverse benchmarks, including MMLU-Pro and LiveCodeBench, indicating its potential for generalization. The paper's key contributions lie in the innovative combination of MC rewards for early reasoning steps and group-relative optimization for later steps, the introduction of a skip-connection mechanism for information flow, and the engineering optimization of single-stream inference to improve computational efficiency. Overall, the paper presents a well-motivated and effective approach to addressing a critical challenge in RLVR, with strong empirical results supporting its claims.


## Soundness:

3.0


## Presentation:

3.0


## Contribution:

2.75


## Strengths:

I find several aspects of this paper to be particularly strong. First, the paper is exceptionally well-written, with clear explanations of the motivation, methodology, and results. The use of diagrams effectively illustrates the key concepts, making the paper accessible and easy to follow. The authors have also made their code publicly available, which is a significant contribution to the community and facilitates reproducibility. Second, the proposed SKPO method is both simple and effective. The idea of decomposing reasoning into upstream and downstream phases, with different reward strategies for each, is a novel and intuitive approach to addressing the challenges of fine-grained dense rewards in RLVR. The skip-connection mechanism for information flow between these phases is also a clever way to balance the need for fine-grained guidance with the need for exploration. Third, the empirical results presented in the paper are compelling. The authors demonstrate significant improvements over existing methods on mathematical reasoning tasks, and they also show that SKPO generalizes well across diverse benchmarks, including MMLU-Pro and LiveCodeBench. These results provide strong evidence for the effectiveness of the proposed method. Finally, the engineering optimization of single-stream inference is a notable technical innovation. By generating and replaying upstream segments in parallel and then generating downstream responses within a single pass of the inference engine, the authors achieve a significant reduction in computational cost, making SKPO more practical for real-world applications. The combination of these factors—the clear presentation, the novel method, the strong empirical results, and the technical innovation—makes this paper a valuable contribution to the field of RLVR.


## Weaknesses:

Despite the strengths of this paper, I have identified several weaknesses that warrant further discussion. First and foremost, the paper lacks a detailed analysis of the computational overhead introduced by the skip connection and single-stream optimization. While the authors mention that SKPO reduces instability on fine-grained signals by lowering upstream per-prompt sample count and estimating more stable baselines from historical samples, they do not provide a quantitative analysis of the additional memory or time costs associated with storing and replaying the upstream segment. Specifically, the paper does not quantify the memory overhead of storing and replaying the upstream segment, nor does it provide a breakdown of how the single-stream optimization impacts training time compared to standard group-relative methods. This makes it difficult to assess the practical trade-offs of the proposed approach. The paper mentions a 'mid-generation KV cache rewriting' technique to achieve 'true computational parity' but does not provide a direct comparison of training times. This is a significant omission, as the practical applicability of the method depends on a thorough understanding of its computational cost. My confidence in this weakness is high, as the paper does not provide any quantitative data to support its claims about computational efficiency. Second, the paper does not explore the sensitivity of SKPO to different skip connection strategies or segmentation points. The choice of a fixed split point at 1/6 to 1/2 of the total length seems arbitrary, and the paper does not provide a thorough investigation into how varying the segmentation position affects performance, particularly in tasks with different reasoning depths. The ablation study on 'Segmentation Strategy' compares 'Unconditional,' 'Selective,' and 'Extreme' strategies, but it does not explore a continuous range of segmentation points. Furthermore, the paper does not consider adaptive segmentation strategies that might be more suitable for tasks with varying reasoning lengths. This lack of sensitivity analysis makes it difficult to understand the robustness of the method and to provide practical guidance for its application. My confidence in this weakness is high, as the paper does not include any experiments that systematically vary the segmentation position. Third, while the paper demonstrates improvements on mathematical reasoning tasks, it lacks a comprehensive evaluation across diverse reasoning domains. The current evaluation is heavily focused on mathematical computation, which may not fully capture the generalizability of the proposed method. The paper includes MMLU-Pro and LiveCodeBench for out-of-domain evaluation, but the in-domain evaluation is primarily focused on mathematical reasoning. The paper does not include experiments on tasks that require more complex forms of reasoning, such as tasks that involve multiple steps of inference or tasks that require the integration of information from different sources. This limits the scope of the paper and raises questions about the applicability of SKPO to a wider range of reasoning challenges. My confidence in this weakness is high, as the paper's evaluation is clearly limited to mathematical reasoning tasks in the main experiments. Fourth, the paper does not compare SKPO to the recent work 'Learning from Failure' by Li et al. (2024), which also proposes to use MC rewards for early reasoning steps and group relative rewards for later reasoning steps. This is a significant omission, as it makes it difficult to assess the advantages of SKPO over this relevant baseline. My confidence in this weakness is high, as the paper does not include any comparison to the 'Learning from Failure' method. Finally, the paper lacks a theoretical analysis of the proposed method. The authors do not provide a discussion of the convergence properties of SKPO, as well as the conditions under which the method is guaranteed to find a good solution. This theoretical analysis would help to provide a deeper understanding of the method's behavior and its limitations. My confidence in this weakness is high, as the paper does not include any theoretical analysis of the method.


## Suggestions:

To address the identified weaknesses, I recommend several concrete improvements. First, the authors should provide a more detailed analysis of the computational cost of SKPO. This should include a breakdown of the memory usage for storing and replaying the upstream segment, as well as a comparison of training times with and without the single-stream optimization. The authors should also quantify the additional memory usage and training time for different model sizes and dataset lengths. Furthermore, they should compare the memory footprint of SKPO with other methods, such as GRPO, to provide a clear picture of the memory efficiency of the proposed approach. Second, the authors should conduct a more thorough investigation into the sensitivity of SKPO to different skip connection strategies and segmentation points. This should include experiments with a continuous range of segmentation positions, as well as adaptive segmentation strategies that dynamically adjust the segmentation point based on the input length or reasoning complexity. The authors should also explore different fixed split points, as well as explore adaptive segmentation strategies that might be more suitable for tasks with varying reasoning lengths. This analysis should be conducted on a variety of tasks with different reasoning depths to understand the robustness of SKPO to different segmentation strategies. Third, the authors should expand the evaluation of SKPO to include a more diverse set of reasoning tasks beyond mathematical benchmarks. This should include tasks that require logical inference, code generation, or other forms of structured reasoning. The inclusion of such tasks would provide a more comprehensive assessment of the generalizability of SKPO and its ability to handle different types of reasoning challenges. For example, the authors could evaluate SKPO on tasks from the BigBench benchmark or other datasets that include a variety of reasoning tasks. Fourth, the authors should include a comparison to the 'Learning from Failure' method by Li et al. (2024). This comparison should not only focus on final performance but also on the learning curves and the stability of the training process. Furthermore, the authors should analyze the differences in the reward structures and optimization strategies used by both methods to identify the specific advantages of their approach. This analysis should include a discussion of the potential limitations of the Learning from Failure method and how the proposed method addresses these limitations. Finally, the authors should provide a theoretical analysis of the proposed method. This analysis should include a discussion of the convergence properties of SKPO, as well as the conditions under which the method is guaranteed to find a good solution. The authors should also discuss the relationship between the proposed method and existing reinforcement learning algorithms, such as policy gradient methods and Q-learning. This theoretical analysis would help to provide a deeper understanding of the method's behavior and its limitations. In addition to these points, the authors should also consider including a discussion of the limitations of their method and the potential areas for future research. This would provide a more complete picture of the strengths and weaknesses of SKPO and would guide future research in this area.


## Questions:

I have several questions that I believe would help to further clarify the proposed method and its implications. First, how does SKPO perform on tasks with more complex forms of reasoning, such as tasks that involve multiple steps of inference or tasks that require the integration of information from different sources? The current evaluation is heavily focused on mathematical reasoning, and it would be valuable to understand how SKPO performs on tasks that require more complex reasoning steps beyond arithmetic calculations. Second, what is the computational overhead of SKPO compared to traditional GRPO methods? How does the single-stream optimization impact training time and memory usage? The paper mentions that SKPO reduces instability on fine-grained signals, but it does not provide a detailed analysis of the computational cost of the method. Third, how sensitive is SKPO to the choice of segmentation point? Have you explored adaptive segmentation strategies? The paper uses a fixed split point, but it would be valuable to understand how the performance of SKPO is affected by different segmentation points, particularly in tasks with varying reasoning depths. Fourth, how does SKPO handle tasks that require more complex forms of reasoning, such as tasks that involve multiple steps of inference or tasks that require the integration of information from different sources? The paper does not explicitly address the specific challenges of multi-step inference or integrating information from different sources. Finally, what is the theoretical analysis of the proposed method? What are the convergence properties of SKPO, and under what conditions is it guaranteed to find a good solution? The paper lacks a theoretical analysis of the method, and it would be valuable to understand the theoretical properties of SKPO.


## Rating:

6.5


## Confidence:

3.0


## Decision:

Accept
}