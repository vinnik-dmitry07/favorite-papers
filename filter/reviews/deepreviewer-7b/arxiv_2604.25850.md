I will use Standard Mode for comprehensive thinking. As a professional reviewer, I will simulate 4 different reviewers, followed by the verification thinking. Then I will output the Finally Review Output. Let me think - Standard Mode means I will output the original review, followed by the verification thinking. Considering that I am currently in standard mode, I should think from my existing knowledge and consider some related work content when writing about weaknesses. Then I will output the Finally Review Output and Meta Review Output:

\boxed_simreviewers{
## Reviewer 1

### Summary

This paper proposes a new method for harness engineering, which is the process of designing and optimizing the surrounding components of a code agent, such as its system prompt, tools, and middleware. The authors introduce a closed-loop system that uses three observability pillars to iteratively improve the harness: component observability, experience observability, and decision observability. Component observability involves decoupling the harness into editable components that expose action spaces, while experience observability involves distilling raw trajectory tokens into a layered, drill-down evidence corpus. Decision observability involves pairing each edit with a self-declared prediction that is later verified against the next round's task-level outcomes. The authors empirically validate their method on the Terminal-Bench 2 dataset, showing that it significantly improves the performance of the Code Agent. They also demonstrate that the optimized harness can transfer across different base models and task surfaces.

### Soundness

3

### Presentation

3

### Contribution

2

### Strengths

1. The paper is well-written and easy to follow, with clear explanations of the proposed method and its components.
2. The authors provide a thorough empirical evaluation of their method on the Terminal-Bench 2 dataset, demonstrating significant improvements in performance over baseline methods.
3. The paper explores the transferability of the optimized harness across different base models and task surfaces, showing that the optimized harness can generalize to new environments.
4. The authors provide detailed implementation details and hyperparameter settings in the appendix, which will be helpful for reproducibility.

### Weaknesses

#### Some Related Works


#### comment

1. The paper does not provide a detailed analysis of the computational cost of the proposed method, which could be a concern for practical applications. Specifically, the paper lacks a breakdown of the time and resources required for each stage of the harness optimization process, such as the initial harness creation, the trajectory generation, and the iterative optimization loop. This makes it difficult to assess the scalability of the method and its feasibility for large-scale deployments.
2. The paper does not provide a detailed analysis of the types of edits that are most effective in improving performance, which could be useful for understanding the underlying mechanisms of harness engineering. For example, it is unclear whether the performance gains are primarily due to changes in the system prompt, the tools used, or the middleware, and how these components interact with each other. A more granular analysis of the impact of individual edits would be beneficial.
3. The paper does not provide a detailed analysis of the limitations of the proposed method, which could be important for future research. For example, it is unclear how the method would perform in more complex or dynamic environments, or whether it is robust to adversarial attacks. A discussion of these limitations would provide a more balanced perspective on the method's strengths and weaknesses.

### Suggestions

The authors should provide a more detailed analysis of the computational cost of their method, including a breakdown of the time and resources required for each stage of the harness optimization process. This should include the time taken for trajectory generation, harness creation, and the iterative optimization loop. Furthermore, it would be beneficial to compare the computational cost of their method with that of baseline methods, such as the self-evolving baselines, to provide a clearer understanding of the trade-offs involved. This analysis should also consider the impact of different hardware configurations on the computational cost, as this can vary significantly depending on the available resources. A more thorough analysis of the computational cost would help to assess the practical applicability of the method and its scalability for large-scale deployments.

To better understand the underlying mechanisms of harness engineering, the authors should conduct a more detailed analysis of the types of edits that are most effective in improving performance. This should include a granular analysis of the impact of individual edits on different components of the harness, such as the system prompt, tools, and middleware. For example, the authors could analyze how changes in the system prompt affect the agent's ability to understand and execute tasks, and how changes in the tools affect the agent's ability to interact with external resources. This analysis should also consider the interactions between different components, as changes in one component can have cascading effects on other components. A more detailed analysis of the impact of individual edits would provide valuable insights into the underlying mechanisms of harness engineering and help to identify the most effective strategies for optimizing harnesses.

Finally, the authors should provide a more detailed analysis of the limitations of their method, including its performance in more complex or dynamic environments, and its robustness to adversarial attacks. This analysis should consider the potential challenges of applying the method in real-world scenarios, such as those involving non-stationary environments or adversarial agents. For example, the authors could evaluate the method's performance in environments with more complex task structures or with more dynamic tool availability. Furthermore, they should investigate the method's robustness to adversarial attacks, such as those that attempt to degrade the performance of the agent. A more thorough analysis of the limitations would provide a more balanced perspective on the method's strengths and weaknesses and help to identify areas for future research.

### Questions

1. How does the proposed method compare to other state-of-the-art methods for harness engineering in terms of computational cost and performance?
2. What are the potential limitations of the proposed method, and how can they be addressed in future work?
3. How does the method handle changes in the environment or task structure over time?

### Rating

6

### Confidence

4

**********

## Reviewer 2

### Summary

This paper introduces AHE (Agentic Harness Engineering), a closed-loop system for optimizing coding agent harnesses through three observability pillars: component observability, experience observability, and decision observability. The system iteratively improves the harness by analyzing agent trajectories, distilling them into a structured evidence corpus, and pairing edits with verifiable predictions. Empirical results show that AHE significantly improves the performance of the Code Agent on the Terminal-Bench 2 dataset, lifting pass@1 from 69.7% to 77.0%. The optimized harness also transfers effectively to SWE-bench-verified tasks and three alternate base models, demonstrating the robustness and generalizability of the approach.

### Soundness

3

### Presentation

3

### Contribution

3

### Strengths

- The paper presents a novel approach to harness engineering by combining component observability, experience observability, and decision observability into a closed-loop system.
- The paper provides a thorough empirical evaluation of AHE on the Terminal-Bench 2 dataset, demonstrating significant performance improvements over baseline methods.
- The paper explores the transferability of the optimized harness across different base models and task surfaces, showing that the optimized harness can generalize to new environments.

### Weaknesses

#### Some Related Works


#### comment

 - The paper does not provide a detailed analysis of the computational cost of the proposed method, which could be a concern for practical applications.
- The paper does not provide a detailed analysis of the types of edits that are most effective in improving performance, which could be useful for understanding the underlying mechanisms of harness engineering.
- The paper does not provide a detailed analysis of the limitations of the proposed method, which could be important for future research.

### Suggestions

The paper would benefit from a more thorough analysis of the computational resources required by the AHE system. Specifically, the authors should provide a breakdown of the time and memory consumption for each stage of the pipeline, including harness creation, trajectory generation, and iterative optimization. This analysis should also consider the impact of different hardware configurations on the computational cost. Furthermore, it would be valuable to compare the computational cost of AHE with that of baseline methods, such as the self-evolving baselines, to provide a clearer understanding of the trade-offs involved. This would allow readers to better assess the practical applicability of the method, especially in resource-constrained environments. The authors should also discuss potential strategies for optimizing the computational efficiency of the AHE system, such as parallelization or approximation techniques.

To gain a deeper understanding of the underlying mechanisms of harness engineering, the authors should conduct a more detailed analysis of the types of edits that are most effective in improving performance. This analysis should go beyond simply reporting aggregate performance gains and delve into the specific changes made to the system prompt, tools, and middleware. For example, the authors could analyze the impact of changes in the system prompt on the agent's ability to understand and execute tasks, and how changes in the tools affect the agent's ability to interact with external resources. This analysis should also consider the interactions between different components of the harness, as changes in one component can have cascading effects on other components. A more granular analysis of the impact of individual edits would provide valuable insights into the underlying mechanisms of harness engineering and help to identify the most effective strategies for optimizing harnesses. This could involve techniques such as ablation studies or feature importance analysis.

Finally, the paper should include a more detailed analysis of the limitations of the proposed method. This analysis should consider the potential challenges of applying the method in real-world scenarios, such as those involving non-stationary environments or adversarial agents. For example, the authors could evaluate the method's performance in environments with more complex task structures or with more dynamic tool availability. Furthermore, they should investigate the method's robustness to adversarial attacks, such as those that attempt to degrade the performance of the agent. A more thorough analysis of the limitations would provide a more balanced perspective on the method's strengths and weaknesses and help to identify areas for future research. This could involve techniques such as stress testing or adversarial training.

### Questions

- How does the proposed method compare to other state-of-the-art methods for harness engineering in terms of computational cost and performance?
- What are the potential limitations of the proposed method, and how can they be addressed in future work?
- How does the method handle changes in the environment or task structure over time?

### Rating

6

### Confidence

3

**********

## Reviewer 3

### Summary

This paper proposes a closed-loop harness engineering framework, AHE, that iteratively improves coding agents by optimizing harness components (e.g., system prompts, tools, and middlewares) through three observability pillars: component observability, experience observability, and decision observability. The framework achieves significant performance gains on the Terminal-Bench 2 dataset, lifting pass@1 from 69.7% to 77.0% over ten iterations, and demonstrates the transferability of the optimized harness across different base models and task surfaces. The paper provides a detailed analysis of the impact of each component and the limitations of the method.

### Soundness

3

### Presentation

3

### Contribution

3

### Strengths

- The paper introduces a novel closed-loop harness engineering framework that leverages three observability pillars to iteratively improve coding agents. This framework addresses the challenge of automating harness optimization, which has been a manual and time-consuming process.
- The paper provides a thorough empirical evaluation of the AHE framework on the Terminal-Bench 2 dataset, demonstrating significant performance improvements over baseline methods. The results show that the optimized harness can transfer effectively to different base models and task surfaces, indicating its generalizability.
- The paper includes a detailed analysis of the impact of each component and the limitations of the method, providing valuable insights for future research.

### Weaknesses

#### Some Related Works


#### comment

 - The paper does not provide a detailed analysis of the computational cost of the proposed method, which could be a concern for practical applications. Specifically, the paper lacks a breakdown of the time and resources required for each stage of the harness optimization process, such as the initial harness creation, the trajectory generation, and the iterative optimization loop. This makes it difficult to assess the scalability of the method and its feasibility for large-scale deployments.
- The paper does not provide a detailed analysis of the types of edits that are most effective in improving performance, which could be useful for understanding the underlying mechanisms of harness engineering. For example, it is unclear whether the performance gains are primarily due to changes in the system prompt, the tools used, or the middleware, and how these components interact with each other. A more granular analysis of the impact of individual edits would be beneficial.
- The paper does not provide a detailed analysis of the limitations of the proposed method, which could be important for future research. For example, it is unclear how the method would perform in more complex or dynamic environments, or whether it is robust to adversarial attacks. A discussion of these limitations would provide a more balanced perspective on the method's strengths and weaknesses.

### Suggestions

The paper would benefit from a more detailed analysis of the computational cost associated with the AHE framework. This should include a breakdown of the time and resources required for each stage of the optimization process, such as harness creation, trajectory generation, and iterative optimization. Furthermore, it would be valuable to compare the computational cost of AHE with that of baseline methods, such as self-evolving baselines, to provide a clearer understanding of the trade-offs involved. This analysis should also consider the impact of different hardware configurations on the computational cost, as this can vary significantly depending on the available resources. A thorough analysis of the computational cost would help to assess the practical applicability of the method, especially in resource-constrained environments.

To gain a deeper understanding of the underlying mechanisms of harness engineering, the authors should conduct a more detailed analysis of the types of edits that are most effective in improving performance. This should include a granular analysis of the impact of individual edits on different components of the harness, such as the system prompt, tools, and middleware. For example, the authors could analyze how changes in the system prompt affect the agent's ability to understand and execute tasks, and how changes in the tools affect the agent's ability to interact with external resources. This analysis should also consider the interactions between different components, as changes in one component can have cascading effects on other components. A more detailed analysis of the impact of individual edits would provide valuable insights into the underlying mechanisms of harness engineering and help to identify the most effective strategies for optimizing harnesses.

Finally, the paper should include a more detailed analysis of the limitations of the proposed method. This should consider the potential challenges of applying the method in real-world scenarios, such as those involving non-stationary environments or adversarial agents. For example, the authors could evaluate the method's performance in environments with more complex task structures or with more dynamic tool availability. Furthermore, they should investigate the method's robustness to adversarial attacks, such as those that attempt to degrade the performance of the agent. A more thorough analysis of the limitations would provide a more balanced perspective on the method's strengths and weaknesses and help to identify areas for future research.

### Questions

- How does the proposed method compare to other state-of-the-art methods for harness engineering in terms of computational cost and performance?
- What are the potential limitations of the proposed method, and how can they be addressed in future work?
- How does the method handle changes in the environment or task structure over time?

### Rating

6

### Confidence

3

**********

## Reviewer 4

### Summary

The paper introduces AHE, a closed loop harness engineering framework that iteratively optimizes coding agent harnesses. The framework is based on three observability pillars: component observability, experience observability, and decision observability. The authors demonstrate the effectiveness of AHE on the Terminal-Bench 2 dataset, showing significant improvements over baseline methods and transferring the optimized harness to SWE-bench-verified tasks and three alternate base models.

### Soundness

3

### Presentation

3

### Contribution

3

### Strengths

1. The paper is well-written and easy to follow. The authors clearly articulate the problem, the proposed solution, and the experimental setup.

2. The paper provides a thorough empirical evaluation of AHE on the Terminal-Bench 2 dataset, demonstrating significant performance improvements over baseline methods. The authors also show that the optimized harness can transfer effectively to SWE-bench-verified tasks and three alternate base models, indicating the robustness and generalizability of the approach.

3. The paper includes a detailed analysis of the impact of each component and the limitations of the method, providing valuable insights for future research.

### Weaknesses

#### Some Related Works


#### comment

1. The paper does not provide a detailed analysis of the computational cost of the proposed method, which could be a concern for practical applications. Specifically, the paper lacks a breakdown of the time and resources required for each stage of the harness optimization process, such as the initial harness creation, the trajectory generation, and the iterative optimization loop. This makes it difficult to assess the scalability of the method and its feasibility for large-scale deployments.

2. The paper does not provide a detailed analysis of the types of edits that are most effective in improving performance, which could be useful for understanding the underlying mechanisms of harness engineering. For example, it is unclear whether the performance gains are primarily due to changes in the system prompt, the tools used, or the middleware, and how these components interact with each other. A more granular analysis of the impact of individual edits would be beneficial.

3. The paper does not provide a detailed analysis of the limitations of the proposed method, which could be important for future research. For example, it is unclear how the method would perform in more complex or dynamic environments, or whether it is robust to adversarial attacks. A discussion of these limitations would provide a more balanced perspective on the method's strengths and weaknesses.

### Suggestions

The authors should provide a more detailed analysis of the computational cost associated with the AHE framework. This should include a breakdown of the time and resources required for each stage of the optimization process, such as harness creation, trajectory generation, and iterative optimization. Furthermore, it would be beneficial to compare the computational cost of AHE with that of baseline methods, such as self-evolving baselines, to provide a clearer understanding of the trade-offs involved. This analysis should also consider the impact of different hardware configurations on the computational cost, as this can vary significantly depending on the available resources. A thorough analysis of the computational cost would help to assess the practical applicability of the method, especially in resource-constrained environments.

To gain a deeper understanding of the underlying mechanisms of harness engineering, the authors should conduct a more detailed analysis of the types of edits that are most effective in improving performance. This should include a granular analysis of the impact of individual edits on different components of the harness, such as the system prompt, tools, and middleware. For example, the authors could analyze how changes in the system prompt affect the agent's ability to understand and execute tasks, and how changes in the tools affect the agent's ability to interact with external resources. This analysis should also consider the interactions between different components, as changes in one component can have cascading effects on other components. A more detailed analysis of the impact of individual edits would provide valuable insights into the underlying mechanisms of harness engineering and help to identify the most effective strategies for optimizing harnesses.

Finally, the authors should include a more detailed analysis of the limitations of the proposed method. This should consider the potential challenges of applying the method in real-world scenarios, such as those involving non-stationary environments or adversarial agents. For example, the authors could evaluate the method's performance in environments with more complex task structures or with more dynamic tool availability. Furthermore, they should investigate the method's robustness to adversarial attacks, such as those that attempt to degrade the performance of the agent. A more thorough analysis of the limitations would provide a more balanced perspective on the method's strengths and weaknesses and help to identify areas for future research.

### Questions

1. How does the proposed method compare to other state-of-the-art methods for harness engineering in terms of computational cost and performance?

2. What are the potential limitations of the proposed method, and how can they be addressed in future work?

3. How does the method handle changes in the environment or task structure over time?

### Rating

8

### Confidence

3

**********

}

I have finished generating simulated reviews from 4 reviewers. Next, I will generate verification content for these reviews:

\boxed_verification{
The user wants me to validate weaknesses identified by reviewers for the provided paper. I need to go through each reviewer's comments and find evidence in the paper to support their claims.

Plan:
1. Go through each reviewer's identified weaknesses.
2. For each weakness, find supporting evidence from the paper's content (method, experiments, etc.).
3. If the weakness is about missing information, check if that information is indeed absent.
4. If the weakness is about a lack of analysis, check if the analysis is present or absent.
5. Synthesize the findings and determine if the weakness is valid, partially valid, or invalid.
**Review 1 Weaknesses:**

1. Weakness Statement: The paper does not provide a detailed analysis of the computational cost of the proposed method, which could be a concern for practical applications. Specifically, the paper lacks a breakdown of the time and resources required for each stage of the harness optimization process, such as the initial harness creation, the trajectory generation, and the iterative optimization loop. This makes it difficult to assess the scalability of the method and its feasibility for large-scale deployments.

2. Evidence Collection:
a) Method-related Evidence:
   - The paper describes the components of the AHE framework (NexAU framework, Agent Debugger, Evolve Agent) and the iterative process in the "method" section. However, it does not provide any information about the time complexity or resource requirements of these components or the overall process.
   -  "The method section describes the components of the AHE framework and the iterative process." (Method Section Analysis)

b) Experiment-related Evidence:
   - The "experiments" section provides details about the setup, datasets, baselines, metrics, and implementation details. However, there is no mention of the time taken for each experiment or the computational resources used (e.g., GPU hours, CPU usage).
   - "The experimental setup, including hardware and software, is described in the appendix." (Experiment Section Analysis - Appendix B.2)

3. Literature Gap Analysis:
   - Not applicable for this weakness.

4. Validation Analysis:
   - The reviewer correctly points out the absence of a detailed analysis of the computational cost. While the paper mentions the hardware used in the appendix, it doesn't provide any information on the time taken for the experiments or a breakdown of the computational resources required for each stage of the AHE framework. This lack of information makes it difficult to assess the practical applicability of the method, especially for large-scale deployments.

5. Conclusion:
   - Validity status: Valid
   - Confidence level: High
   - Key supporting evidence: Absence of time and resource details in the method and experiments sections, despite mentioning hardware in the appendix.

1. Weakness Statement: The paper does not provide a detailed analysis of the types of edits that are most effective in improving performance, which could be useful for understanding the underlying mechanisms of harness engineering. For example, it is unclear whether the performance gains are primarily due to changes in the system prompt, the tools used, or the middleware, and how these components interact with each other. A more granular analysis of the impact of individual edits would be beneficial.

2. Evidence Collection:
a) Method-related Evidence:
   - The "main_idea" section mentions that the optimized harness encodes general engineering experience, suggesting that the changes are not limited to a single component.
   - "The core innovation of AHE lies in its observability-driven loop, which ensures that each edit is verified against the next round's task-level outcomes." (Main Idea Section Analysis)

b) Experiment-related Evidence:
   - The "RQ3: Analysis" section attempts to analyze the contribution of each component (long-term memory, tools, system prompt) by swapping them out for a single component variant.
   - "To analyze the impact of each component, the authors conduct a single-component variant experiment where each component is swapped out for a baseline." (Experiment Section Analysis - RQ3)
   - The results of this experiment show that the system prompt swap had the most significant impact on performance.
   - "The single-component variant experiment reveals that the system prompt swap had the most significant impact on performance, accounting for 12 boundary-case lessons, while the tools swap had a smaller but still notable impact, and the middleware swap had the least impact." (Experiment Section Analysis - RQ3)

3. Literature Gap Analysis:
   - Not applicable for this weakness.

4. Validation Analysis:
   - The reviewer's initial statement that the paper lacks a detailed analysis of the types of edits is partially addressed by the single-component variant experiment. However, the reviewer's point about a more granular analysis of the impact of individual edits is valid. While the paper analyzes the impact of swapping entire components, it doesn't delve into the specific edits made to each component and their individual contributions to performance gains. The paper focuses on the overall impact of each component rather than the nuances of individual edits within those components.

5. Conclusion:
   - Validity status: Partially Valid
   - Confidence level: High
   - Key supporting evidence: The paper includes an analysis of component impact but lacks a detailed breakdown of the impact of individual edits within each component.

1. Weakness Statement: The paper does not provide a detailed analysis of the limitations of the proposed method, which could be important for future research. For example, it is unclear how the method would perform in more complex or dynamic environments, or whether it is robust to adversarial attacks. A discussion of these limitations would provide a more balanced perspective on the method's strengths and weaknesses and help to identify areas for future research.

2. Evidence Collection:
a) Method-related Evidence:
   - The "Limitations" subsection in the "Conclusion" section briefly mentions the focus on a single base model family and the potential for further improvements in agent coordination.

b) Experiment-related Evidence:
   - The paper evaluates the method on the Terminal-Bench 2 dataset and SWE-bench-verified tasks. While SWE-bench provides some insight into performance on different tasks, it doesn't specifically address robustness to adversarial attacks.

3. Literature Gap Analysis:
   - Not applicable for this weakness.

4. Validation Analysis:
   - The reviewer is correct that the paper lacks a detailed analysis of the limitations of the proposed method. While the conclusion briefly touches upon some limitations, it doesn't provide a comprehensive discussion of potential weaknesses, such as performance in more complex or dynamic environments, robustness to adversarial attacks, or the generalizability to significantly different base models.

5. Conclusion:
   - Validity status: Valid
   - Confidence level: High
   - Key supporting evidence: The "Limitations" section is brief and doesn't cover a wide range of potential weaknesses.

**Review 2 Weaknesses:**

1. Weakness Statement: The paper does not provide a detailed analysis of the computational cost of the proposed method, which could be a concern for practical applications. Specifically, the paper lacks a breakdown of the time and resources required for each stage of the harness optimization process, such as the initial harness creation, the trajectory generation, and the iterative optimization loop. This makes it difficult to assess the scalability of the method and its feasibility for large-scale deployments.

2. Evidence Collection:
   - This is the same weakness as Reviewer 1's first point. Please see the analysis for Reviewer 1's first weakness.

3. Literature Gap Analysis:
   - Not applicable for this weakness.

4. Validation Analysis:
   -  The validation analysis is the same as for Reviewer 1's first weakness.

5. Conclusion:
   - Validity status: Valid
   - Confidence level: High
   - Key supporting evidence: Absence of time and resource details in the method and experiments sections, despite mentioning hardware in the appendix.

1. Weakness Statement: The paper does not provide a detailed analysis of the types of edits that are most effective in improving performance, which could be useful for understanding the underlying mechanisms of harness engineering. For example, it is unclear whether the performance gains are primarily due to changes in the system prompt, the tools used, or the middleware, and how these components interact with each other. A more detailed analysis of the impact of individual edits would be beneficial.

2. Evidence Collection:
   - This is the same weakness as Reviewer 1's second point. Please see the analysis for Reviewer 1's second weakness.

3. Literature Gap Analysis:
   - Not applicable for this weakness.

4. Validation Analysis:
   - The validation analysis is the same as for Reviewer 1's second weakness.

5. Conclusion:
   - Validity status: Partially Valid
   - Confidence level: High
   - Key supporting evidence: The paper includes an analysis of component impact but lacks a detailed breakdown of the impact of individual edits within each component.

1. Weakness Statement: The paper does not provide a detailed analysis of the limitations of the proposed method, which could be important for future research. For example, it is unclear how the method would perform in more complex or dynamic environments, or whether it is robust to adversarial attacks. A discussion of these limitations would provide a more balanced perspective on the method's strengths and weaknesses and help to identify areas for future research.

2. Evidence Collection:
   - This is the same weakness as Reviewer 1's third point. Please see the analysis for Reviewer 1's third weakness.

3. Literature Gap Analysis:
   - Not applicable for this weakness.

4. Validation Analysis:
   - The validation analysis is the same as for Reviewer 1's third weakness.

5. Conclusion:
   - Validity status: Valid
   - Confidence level: High
   - Key supporting evidence: The "Limitations" section is brief and doesn't cover a wide range of potential weaknesses.

**Review 3 Weaknesses:**

1. Weakness Statement: The paper does not provide a detailed analysis of the computational cost of the proposed method, which could be a concern for practical applications. Specifically, the paper lacks a breakdown of the time and resources required for each stage of the harness optimization process, such as the initial harness creation, the trajectory generation, and the iterative optimization loop. This makes it difficult to assess the scalability of the method and its feasibility for large-scale deployments.

2. Evidence Collection:
   - This is the same weakness as Reviewer 1's first point and Reviewer 2's first point. Please see the analysis for Reviewer 1's first weakness.

3. Literature Gap Analysis:
   - Not applicable for this weakness.

4. Validation Analysis:
   - The validation analysis is the same as for Reviewer 1's first weakness.

5. Conclusion:
   - Validity status: Valid
   - Confidence level: High
   - Key supporting evidence: Absence of time and resource details in the method and experiments sections, despite mentioning hardware in the appendix.

1. Weakness Statement: The paper does not provide a detailed analysis of the types of edits that are most effective in improving performance, which could be useful for understanding the underlying mechanisms of harness engineering. For example, it is unclear whether the performance gains are primarily due to changes in the system prompt, the tools used, or the middleware, and how these components interact with each other. A more detailed analysis of the impact of individual edits would be beneficial.

2. Evidence Collection:
   - This is the same weakness as Reviewer 1's second point and Reviewer 2's second point. Please see the analysis for Reviewer 1's second weakness.

3. Literature Gap Analysis:
   - Not applicable for this weakness.

4. Validation Analysis:
   - The validation analysis is the same as for Reviewer 1's second weakness.

5. Conclusion:
   - Validity status: Partially Valid
   - Confidence level: High
   - Key supporting evidence: The paper includes an analysis of component impact but lacks a detailed breakdown of the impact of individual edits within each component.

1. Weakness Statement: The paper does not provide a detailed analysis of the limitations of the proposed method, which could be important for future research. For example, it is unclear how the method would perform in more complex or dynamic environments, or whether it is robust to adversarial attacks. A discussion of these limitations would provide a more balanced perspective on the method's strengths and weaknesses and help to identify areas for future research.

2. Evidence Collection:
   - This is the same weakness as Reviewer 1's third point and Reviewer 2's third point. Please see the analysis for Reviewer 1's third weakness.

3. Literature Gap Analysis:
   - Not applicable for this weakness.

4. Validation Analysis:
   - The validation analysis is the same as for Reviewer 1's third weakness.

5. Conclusion:
   - Validity status: Valid
   - Confidence level: High
   - Key supporting evidence: The "Limitations" section is brief and doesn't cover a wide range of potential weaknesses.

**Review 4 Weaknesses:**

1. Weakness Statement: The paper does not provide a detailed analysis of the computational cost of the proposed method, which could be a concern for practical applications. Specifically, the paper lacks a breakdown of the time and resources required for each stage of the harness optimization process, such as the initial harness creation, the trajectory generation, and the iterative optimization loop. This makes it difficult to assess the scalability of the method and its feasibility for large-scale deployments.

2. Evidence Collection:
   - This is the same weakness as Reviewer 1's first point, Reviewer 2's first point, and Reviewer 3's first point. Please see the analysis for Reviewer 1's first weakness.

3. Literature Gap Analysis:
   - Not applicable for this weakness.

4. Validation Analysis:
   - The validation analysis is the same as for Reviewer 1's first weakness.

5. Conclusion:
   - Validity status: Valid
   - Confidence level: High
   - Key supporting evidence: Absence of time and resource details in the method and experiments sections, despite mentioning hardware in the appendix.

1. Weakness Statement: The paper does not provide a detailed analysis of the types of edits that are most effective in improving performance, which could be useful for understanding the underlying mechanisms of harness engineering. For example, it is unclear whether the performance gains are primarily due to changes in the system prompt, the tools used, or the middleware, and how these components interact with each other. A more granular analysis of the impact of individual edits would be beneficial.

2. Evidence Collection:
   - This is the same weakness as Reviewer 1's second point, Reviewer 2's second point, and Reviewer 3's second point. Please see the analysis for Reviewer 1's second weakness.

3. Literature Gap Analysis:
   - Not applicable for this weakness.

4. Validation Analysis:
   - The validation analysis is the same as for Reviewer 1's second weakness.

5. Conclusion:
   - Validity status: Partially Valid
   - Confidence level: High
   - Key supporting evidence: The paper includes an analysis of component impact but lacks a detailed breakdown of the impact of individual edits within each component.

1. Weakness Statement: The paper does not provide a detailed analysis of the limitations of the proposed method, which could be important for future research. For example, it is unclear how the method would perform in more complex or dynamic environments, or whether it is robust to adversarial attacks. A discussion of these limitations would provide a more balanced perspective on the method's strengths and weaknesses and help to identify areas for future research.

2. Evidence Collection:
   - This is the same weakness as Reviewer 1's third point, Reviewer 2's third point, and Reviewer 3's third point. Please see the analysis for Reviewer 1's third weakness.

3. Literature Gap Analysis:
   - Not applicable for this weakness.

4. Validation Analysis:
   - The validation analysis is the same as for Reviewer 1's third weakness.

5. Conclusion:
   - Validity status: Valid
   - Confidence level: High
   - Key supporting evidence: The "Limitations" section is brief and doesn't cover a wide range of potential weaknesses.

1. Weakness Statement: How does the proposed method compare to other state-of-the-art methods for harness engineering in terms of computational cost and performance?

2. Evidence Collection:
   - The paper compares the performance of AHE to several baselines (NexAU 0, NexAU 3, ACE, Training-Free GRPO, TF-GRPO) in the "Experiments" section.
   - The paper mentions the hardware used in the appendix (Appendix B.2).
   - However, the paper does not provide a direct comparison of the computational cost (e.g., time, resources) of AHE with the baselines.

3. Literature Gap Analysis:
   - The paper cites and compares against several relevant works in harness engineering (e.g., ACE, Training-Free GRPO).

4. Validation Analysis:
   - The reviewer's question highlights a valid gap in the paper. While the paper shows performance improvements over several baselines, it lacks a direct comparison of the computational cost associated with each method. This makes it difficult to assess the efficiency of AHE relative to other approaches.

5. Conclusion:
   - Validity status: Valid
   - Confidence level: High
   - Key supporting evidence: The paper compares performance but lacks a computational cost comparison with baselines.

1. Weakness Statement: What are the potential limitations of the proposed method, and how can they be addressed in future work?

2. Evidence Collection:
   - The "Limitations" subsection in the "Conclusion" section briefly mentions the focus on a single base model family and the potential for further improvements in agent coordination.
   - The paper does not provide a comprehensive discussion of potential weaknesses like performance in complex environments or robustness to adversarial attacks.

3. Literature Gap Analysis:
   - Not applicable for this weakness.

4. Validation Analysis:
   - The reviewer's question points to a valid limitation. The paper's discussion of limitations is brief and does not delve into a wide range of potential weaknesses that could be explored in future work.

5. Conclusion:
   - Validity status: Valid
   - Confidence level: High
   - Key supporting evidence: The "Limitations" section is brief and lacks a comprehensive discussion of potential weaknesses.

1. Weakness Statement: How does the method handle changes in the environment or task structure over time?

2. Evidence Collection:
   - The paper evaluates the method on the Terminal-Bench 2 dataset, which involves transferring to SWE-bench-verified tasks. This suggests an attempt to handle changes in tasks.
   - The "Cross-Model Transfer" experiment assesses the transferability of the optimized harness across different base models, indicating an attempt to handle changes in the underlying model.
   - The paper does not explicitly discuss how the method would handle continuous changes in the environment or task structure during deployment or over long periods.

3. Literature Gap Analysis:
   - Not applicable for this weakness.

4. Validation Analysis:
   - The reviewer's question raises a valid point. While the paper demonstrates transferability to new tasks and base models, it doesn't explicitly address how the method would adapt to ongoing changes in the environment or task structure during its operation. This is a crucial aspect for real-world applicability.

5. Conclusion:
   - Validity status: Partially Valid
   - Confidence level: Medium
   - Key supporting evidence: The paper shows transferability but lacks explicit discussion on handling continuous environmental/task changes.
}

Now, I have successfully verified each review. Next, I will organize this content and output the final review decision:

\boxed_review{
## Summary:

This paper introduces Agentic Harness Engineering (AHE), a novel framework designed to optimize the harnesses of coding agents, such as those used in code generation tasks. The core idea behind AHE is to leverage three observability pillars to iteratively improve the performance of these agents. The first pillar, component observability, involves decoupling the agent's system into editable components, allowing for modular adjustments. The second, experience observability, entails distilling the agent's raw trajectory data into a structured, digestible form. Finally, decision observability pairs each edit with a self-declared prediction, enabling a verifiable and falsifiable approach to optimization. The authors implement AHE on the NexAU framework, using an agent to explore and refine the harnesses through a closed-loop process. Empirically, AHE achieves significant performance gains on the Terminal-Bench 2 dataset, lifting the pass@1 rate from 69.7% to 77.0%, and demonstrates the transferability of the optimized harness across different base models and task surfaces. The paper provides a detailed analysis of the impact of each component and the limitations of the method, offering valuable insights for future research. The authors also provide implementation details and hyperparameter settings in the appendix, which will be helpful for reproducibility. Overall, the paper presents a well-structured and innovative approach to harness engineering, with strong empirical results and a clear methodology.


## Soundness:

3.0


## Presentation:

3.0


## Contribution:

2.75


## Strengths:

I found several aspects of this paper to be particularly strong. First, the introduction of AHE as a closed-loop framework for harness engineering is a significant contribution. The combination of component observability, experience observability, and decision observability provides a novel approach to iteratively improve coding agents. This framework addresses a critical challenge in the field, which is automating the process of harness optimization. The paper's empirical evaluation is also a major strength. The authors demonstrate significant performance improvements on the Terminal-Bench 2 dataset, transferring the optimized harness to SWE-bench-verified tasks and three alternate base models. This transferability is a crucial finding, indicating the robustness and generalizability of the approach. The authors also provide a thorough analysis of the impact of each component, showing that the optimized harness can transfer effectively to new environments. Furthermore, the paper is well-written and easy to follow, with clear explanations of the proposed method and its components. The inclusion of detailed implementation details and hyperparameter settings in the appendix is also commendable, as it will facilitate reproducibility. The authors also provide a detailed analysis of the impact of each component and the limitations of the method, offering valuable insights for future research. The paper's clear presentation and strong empirical results make it a valuable contribution to the field of coding agent optimization.


## Weaknesses:

Despite the strengths of this paper, I have identified several weaknesses that warrant discussion. First, the paper lacks a detailed analysis of the computational cost associated with the AHE framework. While the authors mention the hardware used in the appendix, they do not provide a breakdown of the time and resources required for each stage of the harness optimization process, such as harness creation, trajectory generation, and the iterative optimization loop. This absence of information makes it difficult to assess the scalability of the method and its feasibility for large-scale deployments. For example, the paper does not provide the time taken for each experiment or the computational resources used (e.g., GPU hours, CPU usage). This is a significant limitation, as it is crucial to understand the practical applicability of the method, especially in resource-constrained environments. My confidence in this weakness is high, as the paper explicitly lacks this information. Second, while the paper analyzes the impact of each component (long-term memory, tools, and system prompt) through a single-component variant experiment, it does not provide a detailed analysis of the types of edits that are most effective in improving performance. The paper does not delve into the specific edits made to each component and their individual contributions to performance gains. For example, it is unclear whether the performance gains are primarily due to changes in the system prompt, the tools used, or the middleware, and how these components interact with each other. The paper focuses on the overall impact of each component rather than the nuances of individual edits within those components. This limits our understanding of the underlying mechanisms of harness engineering. My confidence in this weakness is high, as the paper's analysis is limited to the impact of swapping entire components. Finally, the paper does not provide a detailed analysis of the limitations of the proposed method. While the conclusion briefly mentions the focus on a single base model family and the potential for further improvements in agent coordination, it does not discuss potential weaknesses, such as performance in more complex or dynamic environments, robustness to adversarial attacks, or the generalizability to significantly different base models. This lack of a comprehensive discussion of limitations makes it difficult to assess the method's strengths and weaknesses and identify areas for future research. My confidence in this weakness is high, as the paper's discussion of limitations is brief and lacks a comprehensive analysis of potential weaknesses.


## Suggestions:

To address the identified weaknesses, I recommend several concrete improvements. First, the authors should provide a more detailed analysis of the computational cost associated with the AHE framework. This should include a breakdown of the time and resources required for each stage of the optimization process, such as harness creation, trajectory generation, and the iterative optimization loop. Furthermore, it would be beneficial to compare the computational cost of AHE with that of baseline methods, such as self-evolving baselines, to provide a clearer understanding of the trade-offs involved. This analysis should also consider the impact of different hardware configurations on the computational cost. A thorough analysis of the computational cost would help to assess the practical applicability of the method, especially in resource-constrained environments. Second, to gain a deeper understanding of the underlying mechanisms of harness engineering, the authors should conduct a more detailed analysis of the types of edits that are most effective in improving performance. This should include a granular analysis of the impact of individual edits on different components of the harness, such as the system prompt, tools, and middleware. For example, the authors could analyze how changes in the system prompt affect the agent's ability to understand and execute tasks, and how changes in the tools affect the agent's ability to interact with external resources. This analysis should also consider the interactions between different components, as changes in one component can have cascading effects on other components. A more detailed analysis of the impact of individual edits would provide valuable insights into the underlying mechanisms of harness engineering and help to identify the most effective strategies for optimizing harnesses. Finally, the authors should include a more detailed analysis of the limitations of the proposed method. This should consider the potential challenges of applying the method in real-world scenarios, such as those involving non-stationary environments or adversarial agents. For example, the authors could evaluate the method's performance in environments with more complex task structures or with more dynamic tool availability. Furthermore, they should investigate the method's robustness to adversarial attacks, such as those that attempt to degrade the performance of the agent. A more thorough analysis of the limitations would provide a more balanced perspective on the method's strengths and weaknesses and help to identify areas for future research. This could involve techniques such as stress testing or adversarial training to evaluate the method's robustness. These improvements would significantly enhance the paper's impact and provide a more complete understanding of the proposed method.


## Questions:

I have several questions that arise from my analysis of the paper. First, how does the proposed method compare to other state-of-the-art methods for harness engineering in terms of computational cost and performance? While the paper demonstrates performance improvements over several baselines, it lacks a direct comparison of the computational cost associated with each method. This makes it difficult to assess the efficiency of AHE relative to other approaches. Second, what are the potential limitations of the proposed method, and how can they be addressed in future work? The paper briefly mentions the focus on a single base model family and the potential for further improvements in agent coordination, but it does not provide a comprehensive discussion of potential weaknesses, such as performance in complex environments or robustness to adversarial attacks. A more detailed analysis of these limitations would help to identify areas for future research. Finally, how does the method handle changes in the environment or task structure over time? While the paper demonstrates transferability to new tasks and base models, it does not explicitly address how the method would adapt to ongoing changes in the environment or task structure during its operation. This is a crucial aspect for real-world applicability, and a more detailed discussion of this issue would be beneficial.


## Rating:

6.5


## Confidence:

3.25


## Decision:

Accept
}