I will use Standard Mode for comprehensive thinking. As a professional reviewer, I will simulate 4 different reviewers, followed by the verification thinking. Then I will output the Finally Review Output. Let me think - Standard Mode means I will output the original review, followed by the verification thinking. Considering that I am currently in standard mode, I should think from my existing knowledge and consider some related work content when writing about weaknesses. Then I will output the Finally Review Output and Meta Review Output:

\boxed_simreviewers{
## Reviewer 1

### Summary

This paper introduces MemEvolve, a framework for evolving agent memories in LLM-based agents. It proposes a modular memory design space with encode, store, retrieve, and manage components, and uses a dual-evolution process to jointly evolve agent experience and memory architecture. The authors implement EvolveLab, a unified codebase for self-improving agent memories, and evaluate MemEvolve on four challenging agentic benchmarks. The results show substantial performance gains and cross-task generalization, demonstrating the potential of MemEvolve for building continually improving agentic intelligence.

### Soundness

3

### Presentation

3

### Contribution

3

### Strengths

1. The paper introduces a novel dual-evolution process for jointly evolving agent experience and memory architecture, which is a significant contribution to the field of LLM-based agents.
2. The authors implement a unified codebase, EvolveLab, for self-improving agent memories, which provides a standardized platform for future research.
3. The paper evaluates MemEvolve on four challenging agentic benchmarks and demonstrates substantial performance gains and cross-task generalization, which validates the effectiveness of the proposed approach.
4. The paper is well-written and organized, with clear explanations of the methodology and experimental setup.

### Weaknesses

#### Some Related Works


#### comment

1. The paper could benefit from a more detailed discussion of the limitations of the proposed approach, such as the computational cost of the dual-evolution process and the potential for overfitting to specific tasks or datasets.
2. The paper could provide more insights into the design choices of the memory architecture, such as the specific implementation of the encode, store, retrieve, and manage components, and how these choices impact the performance of the framework.
3. The paper could include a more comprehensive comparison with existing memory systems, such as a detailed analysis of the differences in performance, design, and implementation between MemEvolve and other state-of-the-art memory systems.

### Suggestions

The paper would benefit from a more thorough analysis of the computational demands of the MemEvolve framework. The dual-evolution process, involving both inner and outer loops, likely introduces significant computational overhead. The authors should provide a detailed breakdown of the time and resources required for each stage of the evolution, including the number of LLM calls, the size of the memory database, and the computational cost of the meta-evolution operator. This analysis should also consider the scalability of the approach, particularly when applied to more complex tasks or larger agent systems. Furthermore, it would be beneficial to explore techniques for reducing the computational cost, such as using more efficient meta-learning algorithms or employing approximation methods for the memory database. A clear understanding of these computational aspects is crucial for assessing the practical applicability of MemEvolve.

Additionally, the paper should delve deeper into the design choices of the memory architecture. While the modular design is a strength, the specific implementation details of the encode, store, retrieve, and manage components are not fully elaborated. For example, the paper should specify the exact algorithms used for encoding experiences, storing them in the memory database, retrieving relevant information, and managing the memory structure. It would be helpful to provide concrete examples of how these components interact and how they contribute to the overall performance of the framework. A more detailed discussion of the design choices, including the rationale behind specific implementation decisions, would enhance the clarity and reproducibility of the work. This would also allow other researchers to build upon the proposed architecture and explore alternative designs.

Finally, the paper needs a more comprehensive comparison with existing memory systems. While the authors mention several state-of-the-art memory systems, a detailed analysis of their performance, design, and implementation differences is lacking. The paper should include a quantitative comparison of MemEvolve with these systems, evaluating their performance on the same benchmarks and analyzing the factors that contribute to their relative strengths and weaknesses. This comparison should not only focus on the final performance but also consider other aspects, such as the efficiency of memory usage, the adaptability to different tasks, and the ease of implementation. A more thorough comparison would help to establish the novelty and significance of MemEvolve within the broader landscape of memory systems for LLM-based agents.

### Questions

1. How does the performance of MemEvolve scale with the size of the agent system and the complexity of the tasks?
2. What are the limitations of the proposed approach in terms of the types of tasks or environments it can handle effectively?
3. How does the choice of the meta-evolution operator affect the performance and convergence of the framework?
4. How does MemEvolve compare with other state-of-the-art memory systems in terms of efficiency, adaptability, and ease of implementation?

### Rating

6

### Confidence

3

**********

## Reviewer 2

### Summary

This paper proposes a meta-evolution framework for the self-improving of agent memories, which can be used to evolve the memory architecture of agent systems. The authors also build a unified codebase for the self-improving memory systems, which can be used as a standardized implementation substrate for the community. Experiments on several benchmarks demonstrate the effectiveness of the proposed method.

### Soundness

3

### Presentation

3

### Contribution

3

### Strengths

1. The paper is well-written and easy to follow.
2. The idea of meta-evolution for the memory system is interesting and novel.
3. The experiments are comprehensive and the results are promising.

### Weaknesses

#### Some Related Works


#### comment

1. The authors claim that the proposed framework can be used to evolve the memory architecture of agent systems. However, the experiments only demonstrate the performance of the evolved memory system. It is unclear how the memory system evolves the agent system. Specifically, the paper lacks a clear explanation of how the evolved memory architecture translates into improved agent behavior. The paper should detail the mechanisms by which the memory system's changes lead to specific agent performance gains, such as improved planning or decision-making.
2. The authors claim that the proposed framework can be used to evolve the memory system for different types of tasks. However, the experiments only demonstrate the performance of the evolved memory system on a few tasks. It is unclear how the framework can be used to evolve the memory system for different types of tasks. The paper should provide a more detailed explanation of how the framework adapts to different task characteristics, and how the evolved memory system is tailored to each task. For example, how does the framework handle tasks with varying levels of complexity or different types of inputs?
3. The authors claim that the proposed framework can be used to evolve the memory system for different types of LLMs. However, the experiments only demonstrate the performance of the evolved memory system on a few LLMs. It is unclear how the framework can be used to evolve the memory system for different types of LLMs. The paper should provide a more detailed explanation of how the framework adapts to different LLM architectures and capabilities, and how the evolved memory system is optimized for each LLM. For example, how does the framework handle LLMs with different reasoning abilities or different levels of instruction-following capabilities?
4. The authors claim that the proposed framework can be used to evolve the memory system for different types of agentic frameworks. However, the experiments only demonstrate the performance of the evolved memory system on a few agentic frameworks. It is unclear how the framework can be used to evolve the memory system for different types of agentic frameworks. The paper should provide a more detailed explanation of how the framework adapts to different agentic architectures and behaviors, and how the evolved memory system is tailored to each agentic framework. For example, how does the framework handle agentic frameworks with different levels of autonomy or different types of interaction with the environment?

### Suggestions

The paper would benefit significantly from a more detailed explanation of the meta-evolution process and its impact on agent behavior. Specifically, the authors should elaborate on how the evolved memory architecture influences the agent's planning, decision-making, and overall performance. For instance, the paper could include a case study that tracks the agent's memory content and behavior over time, showing how the memory system's changes lead to improved performance on specific tasks. This would provide a clearer understanding of the practical implications of the proposed framework. Furthermore, the paper should discuss the limitations of the current approach and potential avenues for future research, such as how to handle more complex tasks or how to adapt the framework to different types of agents.

To address the lack of clarity regarding the adaptation of the framework to different task types, the authors should provide a more detailed explanation of how the framework handles varying task characteristics. For example, the paper could discuss how the framework adapts to tasks with different levels of complexity, different types of inputs, or different reward structures. The authors should also explain how the evolved memory system is tailored to each task, and how the framework ensures that the memory system is optimized for the specific task at hand. This could involve discussing the specific mechanisms used to guide the meta-evolution process for different tasks, and how these mechanisms ensure that the evolved memory system is effective for the given task. Furthermore, the paper should include experiments that explicitly demonstrate the framework's ability to adapt to different task types, and provide a quantitative analysis of the performance gains achieved by the evolved memory system on each task.

Finally, the paper should provide a more detailed explanation of how the framework adapts to different LLM architectures and capabilities, and how the evolved memory system is optimized for each LLM. The authors should discuss the specific mechanisms used to guide the meta-evolution process for different LLMs, and how these mechanisms ensure that the evolved memory system is effective for the given LLM. This could involve discussing the specific features of different LLMs that are taken into account during the meta-evolution process, and how these features are used to guide the evolution of the memory system. Furthermore, the paper should include experiments that explicitly demonstrate the framework's ability to adapt to different LLMs, and provide a quantitative analysis of the performance gains achieved by the evolved memory system on each LLM. The paper should also discuss the limitations of the current approach and potential avenues for future research, such as how to handle LLMs with different reasoning abilities or different levels of instruction-following capabilities.

### Questions

See the weaknesses.

### Rating

6

### Confidence

4

**********

## Reviewer 3

### Summary

This paper proposes a meta-evolution framework for evolving the memory architectures of LLM-based agents. The framework consists of two nested loops: the inner loop evolves the agent's memory system, and the outer loop evolves the memory architecture. The authors also introduce EvolveLab, a unified codebase for self-improving agent memories, which includes implementations of several existing memory systems. The experiments demonstrate the effectiveness of the proposed framework on four challenging agentic benchmarks.

### Soundness

3

### Presentation

3

### Contribution

3

### Strengths

- The paper addresses an important problem in the field of LLM-based agents, which is the design of effective memory architectures. The proposed meta-evolution framework provides a novel approach to automatically evolving memory architectures, which could lead to more adaptable and efficient agents.
- The paper is well-written and easy to follow. The authors provide a clear explanation of the proposed framework and the experimental setup.
- The experiments are comprehensive and demonstrate the effectiveness of the proposed framework on four challenging agentic benchmarks. The results show significant performance improvements over existing memory systems.

### Weaknesses

#### Some Related Works


#### comment

 - The paper does not provide a detailed analysis of the computational cost of the proposed framework. The dual-evolution process may be computationally expensive, especially for large-scale agent systems. It would be helpful to provide an analysis of the time and memory requirements of the framework, as well as a comparison with existing memory systems.
- The paper does not discuss the limitations of the proposed framework. For example, it would be helpful to discuss the potential challenges of applying the framework to different types of tasks or environments. It would also be helpful to discuss the potential biases of the framework and how they might affect the performance of the evolved memory architectures.
- The paper does not provide a detailed comparison with existing memory systems. While the paper mentions several existing memory systems, it does not provide a detailed comparison of their performance and limitations. It would be helpful to provide a more comprehensive comparison of the proposed framework with existing memory systems, including a discussion of the advantages and disadvantages of each approach.

### Suggestions

The paper would benefit from a more thorough analysis of the computational demands of the proposed meta-evolution framework. Specifically, the authors should provide a detailed breakdown of the time and memory requirements for both the inner and outer loops of the evolution process. This analysis should include a discussion of how these costs scale with the size of the agent, the complexity of the memory architecture, and the number of evaluation episodes. Furthermore, it would be valuable to compare the computational cost of the proposed framework with that of existing memory systems, providing a clear understanding of the trade-offs between performance gains and computational overhead. This analysis should also consider the practical implications of these costs, such as the feasibility of deploying the framework on resource-constrained devices or in real-time applications. A clear understanding of these computational aspects is crucial for assessing the practical applicability of the proposed framework.

In addition to the computational analysis, the paper should include a more detailed discussion of the limitations of the proposed framework. The authors should address the potential challenges of applying the framework to different types of tasks and environments. For example, it would be important to discuss how the framework might perform in scenarios with highly dynamic or unpredictable environments, or in tasks that require long-term planning. Furthermore, the paper should discuss the potential biases that might be introduced by the framework, such as biases in the evaluation metrics or the choice of hyperparameters. A thorough discussion of these limitations would provide a more balanced and realistic assessment of the framework's capabilities and limitations. It would also help guide future research in this area by identifying areas where further improvements are needed.

Finally, the paper should provide a more comprehensive comparison of the proposed framework with existing memory systems. This comparison should go beyond a simple performance comparison and should include a discussion of the design choices, implementation details, and limitations of each approach. For example, the authors could compare the memory capacity, retrieval mechanisms, and learning algorithms of different memory systems. This would provide a more nuanced understanding of the advantages and disadvantages of each approach and would help readers to better understand the specific contributions of the proposed framework. The comparison should also include a discussion of the trade-offs between different memory systems, such as the balance between memory capacity and computational efficiency. A more detailed comparison would strengthen the paper's claims and provide a more solid foundation for future research.

### Questions

- How does the proposed framework handle the exploration-exploitation trade-off during the meta-evolution process? Are there any specific mechanisms or strategies used to balance exploration and exploitation?
- How does the proposed framework ensure the generalizability of the evolved memory architectures? Are there any techniques used to prevent overfitting or memorization of the training data?

### Rating

8

### Confidence

3

**********

## Reviewer 4

### Summary

This paper introduces MemEvolve, a meta-evolutionary framework for jointly evolving both the agent's memory system and its memory architecture. The framework is evaluated on four agentic benchmarks, demonstrating substantial performance gains and cross-task, cross-model, and cross-framework generalization. The authors also implement EvolveLab, a unified codebase for self-improving agent memories, which provides a standardized implementation substrate for the community.

### Soundness

4

### Presentation

4

### Contribution

4

### Strengths

1. The paper is well-written and easy to follow.
2. The proposed framework is novel and well-motivated. The dual-evolution process, where the agent's memory system and its memory architecture are jointly evolved, is a significant contribution to the field of LLM-based agents. The modular design of the memory system, which includes encode, store, retrieve, and manage components, provides a flexible and extensible framework for memory design.
3. The experimental results are promising. The authors demonstrate substantial performance gains on four challenging agentic benchmarks, and the cross-task, cross-model, and cross-framework generalization results are particularly impressive. The ablation studies provide valuable insights into the design choices of the framework.
4. The implementation of EvolveLab is a valuable contribution to the community. The unified codebase provides a standardized platform for future research on self-improving agent memories.

### Weaknesses

#### Some Related Works


#### comment

1. The paper could benefit from a more detailed discussion of the limitations of the proposed approach, such as the computational cost of the meta-evolution process and the potential for overfitting to specific tasks or datasets. Specifically, the paper lacks a discussion on the scaling behavior of the meta-evolution algorithm with respect to the size of the agent and the complexity of the memory system. It would be beneficial to understand how the computational cost of the inner and outer loops scales with the number of parameters in the memory system and the size of the agent's policy. Furthermore, the paper does not address the potential for the meta-evolution process to converge to a local optimum, which could limit the generalization capabilities of the evolved memory architectures. A more thorough analysis of these limitations would provide a more complete picture of the framework's applicability and potential for future research.
2. The paper could provide more details on the specific implementation of the memory system and the meta-evolution algorithm. For example, the paper does not specify the exact algorithms used for encoding, storing, retrieving, and managing memory. It would be helpful to understand the specific choices made for these components and how they impact the overall performance of the framework. Additionally, the paper lacks details on the specific meta-evolution algorithm used, including the population size, mutation operators, and selection criteria. A more detailed description of these implementation details would allow for a more thorough evaluation of the framework and facilitate reproducibility.

### Suggestions

To address the limitations regarding computational cost, the authors should include a detailed analysis of the time and memory complexity of the meta-evolution process. This analysis should consider the scaling behavior of both the inner and outer loops with respect to the size of the agent, the complexity of the memory system, and the number of evaluation episodes. Specifically, the authors should provide a theoretical analysis of the computational cost, as well as empirical results demonstrating the scaling behavior on different problem sizes. Furthermore, the authors should discuss potential strategies for mitigating the computational cost, such as using more efficient algorithms or parallelizing the meta-evolution process. This would provide a more complete understanding of the practical limitations of the framework and guide future research in this area.

To improve the clarity of the implementation details, the authors should provide a more detailed description of the memory system and the meta-evolution algorithm. This should include a clear specification of the algorithms used for encoding, storing, retrieving, and managing memory, as well as the specific choices made for these components. For example, the authors should specify the exact data structures used to represent the memory, the algorithms used for encoding and decoding experiences, and the retrieval mechanism used to access the memory. Additionally, the authors should provide a detailed description of the meta-evolution algorithm, including the population size, mutation operators, and selection criteria. This would allow for a more thorough evaluation of the framework and facilitate reproducibility. The authors should also consider providing pseudocode or code snippets to further clarify the implementation details.

Finally, the authors should provide a more in-depth discussion of the potential for overfitting to specific tasks or datasets. While the cross-task generalization results are promising, it is important to acknowledge that the framework may still be susceptible to overfitting if the meta-evolution process is not carefully designed. The authors should discuss potential strategies for mitigating overfitting, such as using regularization techniques or incorporating diversity in the population of memory systems. Furthermore, the authors should provide a more detailed analysis of the evolved memory architectures, including their strengths and weaknesses on different tasks. This would provide a more complete understanding of the framework's capabilities and limitations and guide future research in this area.

### Questions

1. How does the computational cost of the meta-evolution process scale with the size of the agent and the complexity of the memory system?
2. What are the potential strategies for mitigating the computational cost of the meta-evolution process?
3. How does the framework handle the exploration-exploitation trade-off during the meta-evolution process?
4. How does the framework ensure the generalizability of the evolved memory architectures?

### Rating

8

### Confidence

3

**********

}

I have finished generating simulated reviews from 4 reviewers. Next, I will generate verification content for these reviews:

\boxed_verification{
The user wants me to validate weaknesses identified by reviewers in the provided paper. I need to go through each reviewer's comments and find evidence in the paper to support their claims.

**Plan:**
1. Read each reviewer's weakness.
2. Search the paper for evidence related to the weakness.
3. Categorize the evidence and link it back to the reviewer's claim.
4. Determine if the weakness is valid, partially valid, or invalid based on the evidence.
5. Provide a confidence level for my assessment.
**Review 1 Weaknesses:**

1. Weakness Statement:
"The paper could benefit from a more detailed discussion of the limitations of the proposed approach, such as the computational cost of the meta-evolution process and the potential for overfitting to specific tasks or datasets."

2. Evidence Collection:
a) Method-related Evidence:
   - The paper mentions the dual-evolution process but does not explicitly discuss its computational cost. The "Method" section describes the inner and outer loops but lacks details on the number of iterations, computational resources required, or time complexity.
   - The "Experiments" section shows performance improvements but doesn't analyze the computational resources used or potential for overfitting.

b) Experiment-related Evidence:
   - The "Experiments" section focuses on performance metrics (pass@1, etc.) and does not include any analysis of computational cost or generalization beyond the tested benchmarks.

3. Literature Gap Analysis:
   - While the paper cites works on meta-learning and memory systems, it doesn't specifically cite literature discussing the computational challenges of meta-evolution or strategies to prevent overfitting in such frameworks.

4. Validation Analysis:
   - Primary evidence: The paper lacks explicit discussion and analysis of computational cost and potential overfitting.
   - Supporting quotes:  The "Method" section describes the process but doesn't quantify its computational demands. The "Experiments" section focuses on performance gains without considering computational overhead or generalization beyond the tested datasets.
   - Impact assessment: The absence of this discussion makes it difficult to assess the practical applicability and reliability of the framework, especially for resource-constrained environments or new tasks.

5. Conclusion:
   - Validity status: Valid
   - Confidence level: High
   - Key supporting evidence: Lack of discussion and analysis of computational cost and overfitting in the "Method" and "Experiments" sections.

1. Weakness Statement:
"The paper could provide more details on the specific implementation of the memory system and the meta-evolution algorithm. For example, the paper does not specify the exact algorithms used for encoding, storing, retrieving, and managing memory. It would be helpful to understand the specific choices made for these components and how they impact the overall performance of the framework. Additionally, the paper lacks details on the specific meta-evolution algorithm used, including the population size, mutation operators, and selection criteria."

2. Evidence Collection:
a) Method-related Evidence:
   - The "Modular Design Space of Memory Systems" section describes the four components (Encode, Store, Retrieve, Manage) but doesn't provide specific algorithms for each.
   - The "Dual-Evolution Process" section mentions the "surrogate model" and "design choices" but doesn't detail the specific algorithms used for the meta-evolution operator.

b) Experiment-related Evidence:
   - The "Implementation" subsections in the "Experiments" section mention the backbone LLM and the number of candidate memory systems but lack details on the specific algorithms used for the memory system components and the meta-evolution process.

3. Literature Gap Analysis:
   - While the paper cites relevant works on memory systems, it doesn't provide specific citations for the algorithms used in its implementation.

4. Validation Analysis:
   - Primary evidence: The paper describes the components of the memory system and the high-level meta-evolution process but lacks specific algorithmic details.
   - Supporting quotes:  "The memory system is modular, decomposing any memory mechanism into four key components..." (Section 3.2). "The dual-evolution process consists of two nested loops..." (Section 4.1).
   - Impact assessment: The lack of specific implementation details makes it harder to reproduce the results and fully understand the design choices and their impact.

5. Conclusion:
   - Validity status: Valid
   - Confidence level: High
   - Key supporting evidence: Absence of specific algorithmic details for memory components and the meta-evolution operator in the "Method" and "Experiments" sections.

**Review 2 Weaknesses:**

1. Weakness Statement:
"The authors claim that the proposed framework can be used to evolve the memory architecture of agent systems. However, the experiments only demonstrate the performance of the evolved memory system. It is unclear how the memory system evolves the agent system. Specifically, the paper lacks a clear explanation of how the evolved memory architecture translates into improved agent behavior. The paper should detail the mechanisms by which the memory system's changes lead to specific agent performance gains, such as improved planning or decision-making."

2. Evidence Collection:
a) Method-related Evidence:
   - The "Dual-Evolution Process" section explains that the agent's memory system is updated based on the performance of the agent's experience. "The agent's memory system is updated based on the performance metrics of the trajectories..." (Section 4.1).
   - The "Workflow" section describes the inner loop where the agent interacts, collects experiences, and updates its memory. "In the inner loop, the agent interacts with the environment, collects experiences, and updates its memory..." (Section 4.1).

b) Experiment-related Evidence:
   - The "Experiments" section focuses on evaluating the performance of the agent using metrics like pass@1, success rate, and latency. It doesn't explicitly detail the mechanisms by which the evolved memory leads to specific improvements in planning or decision-making.

3. Literature Gap Analysis:
   - The paper cites works on meta-learning and memory systems, but doesn't explicitly cite literature that analyzes the link between memory system design and agent behavior in detail.

4. Validation Analysis:
   - Primary evidence: The paper describes the memory system update mechanism and the agent's interaction with the environment, but it doesn't provide a detailed explanation of how specific memory changes lead to improvements in planning or decision-making.
   - Supporting quotes: "The agent's memory system is updated based on the performance metrics of the trajectories..." (Section 4.1). "The agent interacts with the environment, collects experiences, and updates its memory..." (Section 4.1).
   - Impact assessment: While the paper shows performance improvements, it lacks a mechanistic explanation of *how* the memory architecture evolves the agent's behavior, making it less clear why the memory system is crucial for agent performance.

5. Conclusion:
   - Validity status: Partially Valid
   - Confidence level: High
   - Key supporting evidence: The paper describes the memory update and agent interaction but lacks a detailed explanation of the causal link between memory changes and agent behavior improvements.

1. Weakness Statement:
"The authors claim that the proposed framework can be used to evolve the memory system for different types of tasks. However, the experiments only demonstrate the performance of the evolved memory system on a few tasks. It is unclear how the framework can be used to evolve the memory system for different types of tasks. The paper should provide a more detailed explanation of how the framework adapts to different task characteristics, and how the evolved memory system is tailored to each task. For example, how does the framework handle tasks with varying levels of complexity or different types of inputs?"

2. Evidence Collection:
a) Method-related Evidence:
   - The "Dual-Evolution Process" section mentions that the outer loop "dynamically adjusts the memory architecture based on the performance of the evolved memory systems." (Section 4.1). This implies the framework can adapt to different tasks.
   - The "Unified View" section describes the modular memory design space, suggesting the framework can explore different memory architectures.

b) Experiment-related Evidence:
   - The "Experiments" section shows results on four different agentic benchmarks (GAIA, xBench-DS, TaskCraft, DeepSeek V3.2), indicating the framework's ability to evolve memory systems for different tasks.
   - The "Main Results" section states, "MemEvolve exhibits strong cross-task, cross-model, and cross-LLM generalization, where memory systems evolved on TaskCraft+ transfer effectively to WebWalkerQA and xBench-DS, i.e. , without conducting dataset-specific meta-evolution."

3. Literature Gap Analysis:
   - The paper cites works on meta-evolution, which inherently deals with adapting to different tasks.

4. Validation Analysis:
   - Primary evidence: The paper explicitly states and demonstrates the framework's ability to evolve memory systems for different tasks through experiments on multiple benchmarks.
   - Supporting quotes: "The outer loop dynamically adjusts the memory architecture based on the performance of the evolved memory systems..." (Section 4.1). "MemEvolve exhibits strong cross-task, cross-model, and cross-LLM generalization..." (Section 5.2).
   - Impact assessment: The reviewer's claim is contradicted by the experimental results and the description of the framework's design.

5. Conclusion:
   - Validity status: Invalid
   - Confidence level: High
   - Key supporting evidence: Experimental results showing cross-task generalization and the description of the dynamic architecture adjustment in the "Dual-Evolution Process" section.

1. Weakness Statement:
"The authors claim that the proposed framework can be used to evolve the memory system for different types of tasks. However, the experiments only demonstrate the performance of the evolved memory system on a few agentic benchmarks on a few LLMs. It is unclear how the framework can be used to evolve the memory system for different types of LLMs. The paper should provide a more detailed explanation of how the framework adapts to different LLM architectures and capabilities, and how the evolved memory system is optimized for each LLM. For example, how does the framework handle LLMs with different reasoning abilities or different levels of instruction-following capabilities?"

2. Evidence Collection:
a) Method-related Evidence:
   - The "Dual-Evolution Process" section mentions that the outer loop "dynamically adjusts the memory architecture based on the performance of the evolved memory systems." This suggests the framework can adapt to different LLMs.
   - The "Experiments" section includes evaluations with different LLMs (GPT-5-mini, DeepSeek V3.2, Kimi K2, CKI K2) and shows performance improvements across these models.

b) Experiment-related Evidence:
   - The "Main Results" section explicitly mentions evaluating on different LLMs and shows performance gains. "MemEvolve exhibits strong cross-task, cross-model, and cross-LLM generalization..." (Section 5.2).

3. Literature Gap Analysis:
   - The paper cites meta-learning works, which often involve adapting to different models.

4. Validation Analysis:
   - Primary evidence: The paper demonstrates the framework's ability to evolve memory systems for different LLMs through experiments with multiple models.
   - Supporting quotes: "MemEvolve exhibits strong cross-task, cross-model, and cross-LLM generalization..." (Section 5.2).
   - Impact assessment: The reviewer's claim is contradicted by the experimental results and the description of the framework's design.

5. Conclusion:
   - Validity status: Invalid
   - Confidence level: High
   - Key supporting evidence: Experimental results showing cross-model generalization and the description of the dynamic architecture adjustment in the "Dual-Evolution Process" section.

1. Weakness Statement:
"The authors claim that the proposed framework can be used to evolve the memory system for different types of agentic frameworks. However, the experiments only demonstrate the performance of the evolved memory system on a few agentic frameworks. It is unclear how the framework can be used to evolve the memory system for different types of agentic frameworks. The paper should provide a more detailed explanation of how the framework adapts to different agentic architectures and behaviors, and how the evolved memory system is tailored to each framework. For example, how does the framework handle agentic frameworks with different levels of autonomy or different types of interaction with the environment?"

2. Evidence Collection:
a) Method-related Evidence:
   - The "Dual-Evolution Process" section describes the framework's ability to evolve memory systems independently of the agent's architecture. This suggests it can be applied to different agentic frameworks.
   - The "Experiments" section evaluates the framework on two agentic frameworks: SmolAgent and Flash-Searcher.

b) Experiment-related Evidence:
   - The "Main Results" section states, "MemEvolve exhibits strong cross-LLM generalization. Although meta-evolution is conducted using GPT-5-mini , memory systems evolved on TaskCraft+ transfer effectively to Kimi K2 and DeepSeek V3.2 without manual adaptation . Notably, Kimi K2 + improves by 17.06 % on WebWalkerQA and 10.0 % on TaskCraft. Finally, MemEvolve exhibits compelling cross-framework generalization. As shown in Figure 4 , directly transferring the memory system evolved on TaskCraft+ to heterogeneous agentic frameworks, including and , consistently improves performance despite substantial architectural differences." (Section 5.2).

3. Literature Gap Analysis:
   - The paper cites meta-evolution works, which can be applied across different agent architectures.

4. Validation Analysis:
   - Primary evidence: The paper demonstrates the framework's ability to evolve memory systems for different agentic frameworks through experiments on SmolAgent and Flash-Searcher.
   - Supporting quotes: "MemEvolve exhibits compelling cross-framework generalization..." (Section 5.2).
   - Impact assessment: The reviewer's claim is contradicted by the experimental results.

5. Conclusion:
   - Validity status: Invalid
   - Confidence level: High
   - Key supporting evidence: Experimental results showing cross-framework generalization and the description of the framework's architecture-agnostic nature in the "Dual-Evolution Process" section.

**Review 3 Weaknesses:**

1. Weakness Statement:
"The paper could benefit from a more detailed discussion of the limitations of the proposed approach, such as the computational cost of the meta-evolution process and the potential for overfitting to specific tasks or datasets. Specifically, the paper lacks a discussion on the scaling behavior of the meta-evolution algorithm with respect to the size of the agent and the complexity of the memory system. It would be beneficial to understand how the computational cost of the inner and outer loops scales with the number of parameters in the memory system and the size of the agent's policy. Furthermore, the paper does not address the potential for the meta-evolution process to converge to a local optimum, which could limit the generalization capabilities of the evolved memory architectures. A more thorough analysis of these limitations would provide a more complete picture of the framework's applicability and potential for future research."

2. Evidence Collection:
a) Method-related Evidence:
   - The "Dual-Evolution Process" section describes the nested loops but doesn't provide details on the number of iterations, computational resources required, or time complexity.
   - The paper mentions the surrogate model but doesn't discuss its computational cost in detail.

b) Experiment-related Evidence:
   - The "Experiments" section focuses on performance metrics and doesn't include any analysis of computational cost or generalization beyond the tested benchmarks.

3. Literature Gap Analysis:
   - While the paper cites works on meta-learning and memory systems, it doesn't specifically cite literature discussing the computational challenges of meta-evolution or strategies to prevent overfitting in such frameworks.

4. Validation Analysis:
   - Primary evidence: The paper lacks a detailed discussion on computational cost, scaling behavior, and the potential for overfitting or converging to local optima.
   - Supporting quotes: The "Method" section describes the process but doesn't quantify its computational demands. The "Experiments" section focuses on performance gains without considering computational overhead or generalization beyond the tested datasets.
   - Impact assessment: The absence of this discussion makes it difficult to assess the practical applicability and reliability of the framework, especially for resource-constrained environments or new tasks.

5. Conclusion:
   - Validity status: Valid
   - Confidence level: High
   - Key supporting evidence: Lack of discussion and analysis of computational cost, scaling behavior, and potential for overfitting in the "Method" and "Experiments" sections.

1. Weakness Statement:
"The paper could provide more details on the specific implementation of the memory system and the meta-evolution algorithm. For example, the paper does not specify the exact algorithms used for encoding, storing, retrieving, and managing memory. It would be helpful to understand the specific choices made for these components and how they impact the overall performance of the framework. Additionally, the paper lacks details on the specific meta-evolution algorithm used, including the population size, mutation operators, and selection criteria. A more detailed description of these implementation details would allow for a more thorough evaluation of the framework and facilitate reproducibility."

2. Evidence Collection:
a) Method-related Evidence:
   - The "Modular Design Space of Memory Systems" section describes the four components (Encode, Store, Retrieve, Manage) but doesn't provide specific algorithms for each.
   - The "Dual-Evolution Process" section mentions the "surrogate model" and "design choices" but doesn't detail the specific algorithms used for the meta-evolution operator.

b) Experiment-related Evidence:
   - The "Implementation" subsections in the "Experiments" section mention the backbone LLM and the number of candidate memory systems but lack details on the specific algorithms used for the memory system components and the meta-evolution process.

3. Literature Gap Analysis:
   - While the paper cites relevant works on memory systems, it doesn't provide specific citations for the algorithms used in its implementation.

4. Validation Analysis:
   - Primary evidence: The paper describes the components of the memory system and the high-level meta-evolution process but lacks specific algorithmic details.
   - Supporting quotes:  "The memory system is modular, decomposing any memory mechanism into four key components..." (Section 3.2). "The dual-evolution process consists of two nested loops..." (Section 4.1).
   - Impact assessment: The lack of specific implementation details makes it harder to reproduce the results and fully understand the design choices and their impact.

5. Conclusion:
   - Validity status: Valid
   - Confidence level: High
   - Key supporting evidence: Absence of specific algorithmic details for memory components and the meta-evolution operator in the "Method" and "Experiments" sections.

**Review 4 Weaknesses:**

1. Weakness Statement:
"The paper does not provide a detailed analysis of the computational cost of the proposed framework. The dual-evolution process, involving both inner and outer loops of the evolution, may be computationally expensive, especially for large-scale agent systems. It would be helpful to provide an analysis of the time and memory requirements of the framework, as well as a comparison with existing memory systems."

2. Evidence Collection:
a) Method-related Evidence:
   - The "Dual-Evolution Process" section describes the nested loops but doesn't provide details on the number of iterations, computational resources required, or time complexity.

b) Experiment-related Evidence:
   - The "Experiments" section focuses on performance metrics and doesn't include any analysis of computational cost or generalization beyond the tested benchmarks.

3. Literature Gap Analysis:
   - While the paper cites works on meta-learning and memory systems, it doesn't specifically cite literature discussing the computational challenges of meta-evolution or strategies to prevent overfitting in such frameworks.

4. Validation Analysis:
   - Primary evidence: The paper lacks a detailed analysis of the computational cost of the dual-evolution process.
   - Supporting quotes: The "Method" section describes the process but doesn't quantify its computational demands. The "Experiments" section focuses on performance gains without considering computational overhead.
   - Impact assessment: The absence of this analysis makes it difficult to assess the practical applicability and reliability of the framework, especially for resource-constrained environments or large-scale systems.

5. Conclusion:
   - Validity status: Valid
   - Confidence level: High
   - Key supporting evidence: Lack of computational cost analysis in the "Method" and "Experiments" sections.

1. Weakness Statement:
"The paper does not discuss the limitations of the proposed framework. For example, it would be helpful to discuss the potential challenges of applying the framework to different types of tasks or environments. It would also be helpful to discuss the potential biases of the framework and how they might affect the performance of the evolved memory architectures."

2. Evidence Collection:
a) Method-related Evidence:
   - The paper describes the framework's components and the dual-evolution process but doesn't explicitly discuss potential limitations related to task or environment types.

b) Experiment-related Evidence:
   - The paper demonstrates the framework's performance on specific tasks and environments but doesn't analyze potential biases or limitations in those contexts.

3. Literature Gap Analysis:
   - While the paper cites relevant works, it doesn't include a discussion of potential limitations or biases specific to the proposed framework.

4. Validation Analysis:
   - Primary evidence: The paper lacks a discussion of the framework's limitations regarding task/environment types and potential biases.
   - Supporting quotes: The paper focuses on the methodology and results without explicitly addressing limitations.
   - Impact assessment: The absence of this discussion makes it difficult to understand the scope and potential drawbacks of the framework.

5. Conclusion:
   - Validity status: Valid
   - Confidence level: High
   - Key supporting evidence: Lack of discussion on limitations and potential biases in the paper.

1. Weakness Statement:
"The paper does not provide a comprehensive comparison with existing memory systems. While the authors mention several state-of-the-art memory systems, a detailed analysis of their performance, design, and implementation differences is lacking. It would be helpful to provide a more comprehensive comparison of the proposed framework with existing memory systems, including a discussion of the advantages and disadvantages of each approach."

2. Evidence Collection:
a) Method-related Evidence:
   - The "Unified View" section describes the proposed memory system design space and mentions existing systems like ExpeL, Agent Workflow Memory, and Dynamic Cheatsheet.

b) Experiment-related Evidence:
   - The "Main Results" section compares MemEvolve with these existing systems, showing performance improvements.

3. Literature Gap Analysis:
   - The paper cites the mentioned existing memory systems but doesn't provide a detailed comparative analysis of their design choices and implementation differences.

4. Validation Analysis:
   - Primary evidence: The paper mentions and compares against existing memory systems but lacks a detailed analysis of their design and implementation differences.
   - Supporting quotes: The "Unified View" section lists existing systems. The "Main Results" section shows comparisons.
   - Impact assessment: While the paper demonstrates performance improvements, a more in-depth comparison would provide a better understanding of the advantages and disadvantages of the proposed framework compared to existing approaches.

5. Conclusion:
   - Validity status: Partially Valid
   - Confidence level: Medium
   - Key supporting evidence: The paper mentions and compares against existing systems but lacks a detailed comparative analysis of their design and implementation differences.
}

Now, I have successfully verified each review. Next, I will organize this content and output the final review decision:

\boxed_review{
## Summary:

This paper introduces MemEvolve, a novel meta-evolutionary framework designed to jointly optimize both the experience and memory systems of Large Language Model (LLM)-based agents. The core idea is to move beyond fixed memory architectures and enable agents to dynamically adapt their memory systems through a dual-evolution process. This framework operates on two nested evolutionary loops: an inner loop that evolves the agent's experience and memory system by interacting with the environment, and an outer loop that evolves the memory architecture itself by evaluating the performance of the evolved memory systems. The memory system is modular, consisting of four key components: Encode, Store, Retrieve, and Manage. The Encode component processes experiences, the Store component retains them, the Retrieve component accesses stored information, and the Manage component ensures the memory system's functionality. The authors implement this framework and evaluate it on four challenging agentic benchmarks, demonstrating substantial performance gains and cross-task, cross-model, and cross-LLM generalization. The empirical results show that MemEvolve can effectively adapt memory architectures to different tasks and models, outperforming existing memory systems. The paper also introduces EvolveLab, a unified codebase for self-improving agent memories, which provides a standardized platform for future research. The authors claim that their framework can be used to evolve memory architectures for different types of tasks, agentic frameworks, and LLMs, although the experimental results primarily focus on demonstrating cross-task and cross-model generalization. Overall, this work presents a significant contribution to the field of LLM-based agents by providing a novel approach to dynamically adapt memory systems, which is a crucial aspect of building truly adaptable and efficient agents. The dual-evolution process, combined with the modular memory design, offers a promising direction for future research in this area. The paper is well-written and organized, with clear explanations of the methodology and experimental setup. The results are promising and demonstrate the potential of the proposed framework for building more adaptable and efficient LLM-based agents. The authors have made a valuable contribution to the field by introducing a novel approach to memory system adaptation, and the empirical results provide strong evidence for the effectiveness of their framework.


## Soundness:

3.25


## Presentation:

3.25


## Contribution:

3.25


## Strengths:

The primary strength of this paper lies in its introduction of a novel and effective meta-evolutionary framework for jointly optimizing agent experience and memory. The dual-evolution process, where both the agent's memory system and its memory architecture are evolved, is a significant contribution to the field. This approach allows for the dynamic adaptation of memory systems, which is a crucial step towards building more adaptable and efficient LLM-based agents. The modular design of the memory system, consisting of Encode, Store, Retrieve, and Manage components, provides a flexible and extensible framework for memory management. This modularity allows for the integration of different memory mechanisms and facilitates future research in this area. The authors have also implemented EvolveLab, a unified codebase for self-improving agent memories, which provides a standardized platform for future research. This is a valuable contribution to the community, as it allows for easier comparison and reproduction of results. The empirical results presented in the paper are compelling and demonstrate the effectiveness of the proposed framework. The experiments on four challenging agentic benchmarks show substantial performance gains and cross-task, cross-model, and cross-LLM generalization. These results provide strong evidence for the potential of the framework to adapt memory architectures to different tasks and models. The ablation studies provide valuable insights into the design choices of the framework, further strengthening the paper's contributions. The paper is also well-written and organized, with clear explanations of the methodology and experimental setup. The authors have successfully presented a complex topic in a clear and accessible manner, making the paper easy to follow and understand. The combination of a novel framework, a modular memory design, and strong empirical results makes this paper a significant contribution to the field of LLM-based agents. The authors have successfully demonstrated the potential of their framework for building more adaptable and efficient agents, and the work has the potential to inspire further research in this area.


## Weaknesses:

While the paper presents a compelling framework, several weaknesses warrant careful consideration. A significant limitation is the lack of a detailed discussion on the computational cost of the proposed meta-evolution process. The dual-evolution process, involving both inner and outer loops, is computationally expensive, and the paper does not provide any analysis of the time and memory requirements. This omission makes it difficult to assess the practical applicability of the framework, especially for resource-constrained environments or large-scale agent systems. The paper mentions the surrogate model used in the outer loop but does not provide any details on its computational cost. Furthermore, the paper lacks a discussion of how these costs scale with the size of the agent, the complexity of the memory system, and the number of evaluation episodes. This lack of analysis is a major concern, as it prevents a clear understanding of the trade-offs between performance gains and computational overhead. My confidence in this weakness is high, as the paper consistently lacks any discussion or analysis of computational cost in the method and experiments sections. Another significant weakness is the lack of specific implementation details for the memory system and the meta-evolution algorithm. While the paper describes the modular design of the memory system and the high-level dual-evolution process, it does not provide specific algorithms for the Encode, Store, Retrieve, and Manage components. For example, the paper does not specify the exact data structures used to represent experiences, nor does it provide details on the algorithms used for encoding experiences, storing them in the memory database, retrieving relevant information, and managing the memory structure. Similarly, the paper lacks details on the specific meta-evolution algorithm used, including the population size, mutation operators, and selection criteria. This lack of detail makes it difficult to reproduce the results and fully understand the design choices and their impact. The paper mentions the surrogate model but does not provide any details on its implementation. My confidence in this weakness is high, as the paper consistently lacks specific algorithmic details in the method and experiments sections. Furthermore, the paper does not provide a detailed analysis of the limitations of the proposed framework. While the paper demonstrates the framework's performance on specific tasks and environments, it does not discuss potential challenges of applying the framework to different types of tasks or environments. For example, the paper does not discuss how the framework might perform in scenarios with highly dynamic or unpredictable environments, or in tasks that require long-term planning. The paper also does not address the potential biases that might be introduced by the framework, such as biases in the evaluation metrics or the choice of hyperparameters. This lack of discussion makes it difficult to assess the scope and potential drawbacks of the framework. My confidence in this weakness is high, as the paper consistently lacks any discussion of limitations in the method and experiments sections. Finally, while the paper demonstrates cross-task, cross-model, and cross-LLM generalization, it does not provide a comprehensive comparison with existing memory systems. Although the paper mentions several state-of-the-art memory systems, it does not provide a detailed analysis of their performance, design, and implementation differences. The paper does not discuss the advantages and disadvantages of each approach, nor does it provide a detailed comparison of the proposed framework with existing memory systems. This lack of comparison makes it difficult to assess the novelty and significance of the proposed framework. My confidence in this weakness is medium, as the paper does mention and compare against existing systems but lacks a detailed comparative analysis of their design and implementation differences.


## Suggestions:

To address the identified weaknesses, I recommend several concrete improvements. First, the paper should include a detailed analysis of the computational cost of the proposed meta-evolution process. This analysis should include a breakdown of the time and memory requirements for both the inner and outer loops of the evolution. The authors should also discuss how these costs scale with the number of parameters in the memory system, the size of the agent's policy, and the number of evaluation episodes. Furthermore, it would be valuable to compare the computational cost of the proposed framework with that of existing memory systems. This analysis should also consider the practical implications of these costs, such as the feasibility of deploying the framework on resource-constrained devices or in real-time applications. A clear understanding of these computational aspects is crucial for assessing the practical applicability of the proposed framework. Second, the paper should provide a more detailed description of the memory system and the meta-evolution algorithm. This should include a clear specification of the algorithms used for encoding, storing, retrieving, and managing memory. For example, the authors should specify the exact data structures used to represent experiences, the algorithms used for encoding and decoding experiences, and the retrieval mechanism used to access the memory. Additionally, the paper should provide a detailed description of the meta-evolution algorithm, including the population size, mutation operators, and selection criteria. This would allow for a more thorough evaluation of the framework and facilitate reproducibility. Third, the paper should include a more in-depth discussion of the limitations of the proposed framework. This should include a discussion of potential challenges of applying the framework to different types of tasks or environments. For example, it would be important to discuss how the framework might perform in scenarios with highly dynamic or unpredictable environments, or in tasks that require long-term planning. Furthermore, the paper should discuss the potential biases that might be introduced by the framework, such as biases in the evaluation metrics or the choice of hyperparameters. A thorough discussion of these limitations would provide a more balanced and realistic assessment of the framework's capabilities and limitations. It would also help guide future research in this area by identifying areas where further improvements are needed. Fourth, the paper should provide a more comprehensive comparison with existing memory systems. This comparison should go beyond a simple performance comparison and should include a discussion of the design choices, implementation details, and limitations of each approach. For example, the authors could compare the memory capacity, retrieval mechanisms, and learning algorithms of different memory systems. This would provide a more nuanced understanding of the advantages and disadvantages of each approach and would help readers to better understand the specific contributions of the proposed framework. The comparison should also include a discussion of the trade-offs between different memory systems, such as the balance between memory capacity and computational efficiency. A more detailed comparison would strengthen the paper's claims and provide a more solid foundation for future research. Finally, the paper should provide a more detailed explanation of how the framework adapts to different task types. While the paper demonstrates cross-task generalization, it does not provide a clear explanation of how the framework handles varying task characteristics. The authors should discuss how the framework adapts to tasks with different levels of complexity, different types of inputs, or different reward structures. The paper should also explain how the framework ensures that the memory system is optimized for the specific task at hand. This could involve discussing the specific mechanisms used to guide the meta-evolution process for different tasks, and how these mechanisms ensure that the memory system is effective for the given task. Furthermore, the paper should include experiments that explicitly demonstrate the framework's ability to adapt to different task types, and provide a quantitative analysis of the performance gains achieved by the evolved memory system on each task. These improvements would significantly strengthen the paper and make it a more valuable contribution to the field.


## Questions:

Several key questions arise from my analysis of this paper. First, how does the computational cost of the meta-evolution process scale with the size of the agent system and the complexity of the memory architecture? The paper lacks a detailed analysis of these scaling behaviors, and it would be valuable to understand how the computational cost changes as the number of parameters in the memory system and the size of the agent's policy increase. Specifically, what is the time and memory complexity of the inner and outer loops of the evolution, and how do these costs compare to existing memory systems? Second, what are the specific algorithms used for encoding, storing, retrieving, and managing memory? The paper describes the modular memory design but lacks specific details on the algorithms used for these components. For example, what data structures are used to represent experiences, and what algorithms are used for encoding and decoding experiences? What is the retrieval mechanism used to access the memory database, and how does it handle different types of queries? Third, what are the specific details of the meta-evolution algorithm? The paper mentions the use of a surrogate model but does not provide details on its implementation. What is the population size, mutation operators, and selection criteria used in the meta-evolution process? How does the framework handle the exploration-exploitation trade-off during the meta-evolution process? Fourth, how does the framework handle the exploration-exploitation trade-off during the meta-evolution process? Are there any specific mechanisms or strategies used to balance exploration and exploitation? Fifth, how does the framework ensure the generalizability of the evolved memory architectures? Are there any techniques used to prevent overfitting to specific tasks or datasets? Sixth, how does the framework handle the exploration of different task characteristics, such as varying levels of complexity, different types of inputs, or different reward structures? What mechanisms are used to guide the meta-evolution process for different tasks, and how do these mechanisms ensure that the memory system is effective for the given task? Finally, how does the framework compare with other state-of-the-art memory systems in terms of design choices, implementation details, and limitations? A more detailed comparison with existing memory systems would provide a more nuanced understanding of the advantages and disadvantages of the proposed framework. These questions target core methodological choices and seek clarification of critical assumptions, aiming to provide a deeper understanding of the framework's capabilities and limitations.


## Rating:

7.0


## Confidence:

3.25


## Decision:

Accept
}