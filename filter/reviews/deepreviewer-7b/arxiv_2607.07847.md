I will use Standard Mode for comprehensive thinking. As a professional reviewer, I will simulate 4 different reviewers, followed by the verification thinking. Then I will output the Finally Review Output. Let me think - Standard Mode means I will output the original review, followed by the verification thinking. Considering that I am currently in standard mode, I should think from my existing knowledge and consider some related work content when writing about weaknesses. Then I will output the Finally Review Output and Meta Review Output:

\boxed_simreviewers{
## Reviewer 1

### Summary

This paper studies the problem of continual learning in LLMs. The authors categorize the continual learning problem into two axes: space and time. The authors conduct experiments to evaluate different methods on four families of methods: prompt optimization, supervised weight updates, reinforcement learning, and context compression. The authors also introduce a unified framework to compare different methods.

### Soundness

3

### Presentation

2

### Contribution

2

### Strengths

1. The authors provide a unified framework to compare different methods, which is useful for future research.
2. The authors conduct experiments on different settings, including domain adaptation, agentic tasks, financial analysis, and temporally-dependent knowledge updates.

### Weaknesses

#### Some Related Works


#### comment

1. The authors should provide more details about the baselines, such as how to apply the baselines on the agentic task. The authors should also include more baselines, such as simple prompt-based baselines like CoT and Tree of Thoughts.
2. The authors should include more baselines on the financial analysis task, such as prompt-based baselines like CoT and Tree of Thoughts, and RL-based baselines like PPO.
3. The authors should include more baselines on the temporal drift task, such as prompt-based baselines like CoT and Tree of Thoughts, and RL-based baselines like PPO.
4. The authors should include more baselines on the catastrophic memorizing task, such as prompt-based baselines like CoT and Tree of Thoughts, and RL-based baselines like PPO.
5. The authors should include more baselines on the selective fact change task, such as prompt-based baselines like CoT and Tree of Thoughts, and RL-based baselines like PPO.
6. The authors should include more baselines on the noisy temporal drift task, such as prompt-based baselines like CoT and Tree of Thoughts, and RL-based baselines like PPO.
7. The authors should include more baselines on the agentic task, such as prompt-based baselines like CoT and Tree of Thoughts, and RL-based baselines like PPO.

### Suggestions

The paper would significantly benefit from a more thorough exploration of baseline methods across all experimental settings. Specifically, the inclusion of Chain-of-Thought (CoT) and Tree-of-Thoughts (ToT) prompting strategies as baselines is crucial, given their demonstrated effectiveness in complex reasoning tasks. These methods, which involve generating intermediate reasoning steps, could provide a strong point of comparison for the proposed approach. Furthermore, for tasks where reward signals are available, Reinforcement Learning (RL) methods such as Proximal Policy Optimization (PPO) should be considered. PPO is a well-established algorithm for continuous control and has shown impressive results in various domains, making it a relevant baseline for tasks where the goal is to maximize a cumulative reward. The absence of these baselines makes it difficult to assess the true novelty and effectiveness of the proposed methods.

In addition to CoT, ToT, and PPO, the authors should also consider including simpler prompt-based methods as baselines. For instance, a basic prompt-based approach that concatenates all the training data as a prefix to the input could serve as a useful reference point. This would help to isolate the impact of the proposed methods from the simple benefits of providing more context to the model. Furthermore, for the catastrophic memorizing task, it would be beneficial to include more recent and relevant baselines, such as those that explicitly address catastrophic forgetting. This would provide a more comprehensive evaluation of the proposed approach in the context of this specific problem. The current set of baselines is insufficient to fully contextualize the performance of the proposed methods.

Finally, the authors should provide more details on how the baselines are applied to the agentic task. The current description is vague and lacks sufficient detail to allow for reproducibility. For example, it is unclear how the prompts are constructed and how the model is prompted to generate the required actions. Providing a more detailed description of the prompt engineering process, including the specific prompts used and the rationale behind their design, would greatly enhance the clarity and reproducibility of the results. Furthermore, the authors should consider including more baselines on the temporal drift task, such as prompt-based baselines like CoT and Tree of Thoughts, and RL-based baselines like PPO. This would provide a more comprehensive evaluation of the proposed approach in the context of this specific problem.

### Questions

See the weaknesses.

### Rating

3

### Confidence

3

**********

## Reviewer 2

### Summary

This paper studies continual learning in LLMs. The authors categorize the continual learning problem into two axes: space (domain shift) and time (temporal drift). The authors conduct experiments to evaluate different methods on four families of methods: prompt optimization, supervised weight updates, reinforcement learning, and context compression. The authors also introduce a unified framework to compare different methods.

### Soundness

3

### Presentation

3

### Contribution

2

### Strengths

- The paper is well-written and easy to follow.
- The paper provides a unified framework to compare different methods for continual learning in LLMs.
- The paper evaluates different methods on multiple benchmarks and tasks.

### Weaknesses

#### Some Related Works


#### comment

 - The paper does not provide a clear definition of what constitutes a 'continual learning' setting for LLMs. The authors do not specify the assumptions about the data distribution, the task distribution, or the model capacity. This lack of clarity makes it difficult to assess the validity of the experimental results.
- The paper does not provide a clear explanation of how the proposed framework addresses the challenges of continual learning in LLMs. The authors do not discuss the limitations of existing methods for continual learning in LLMs, nor do they explain how their framework overcomes these limitations.
- The paper does not provide a clear evaluation protocol for the proposed framework. The authors do not specify how the different methods are compared, nor do they provide a clear metric for evaluating the performance of the methods.
- The paper does not provide a clear discussion of the limitations of the proposed framework. The authors do not discuss the assumptions made by the framework, nor do they discuss the potential biases in the experimental results.

### Suggestions

The paper needs to provide a more rigorous definition of the continual learning setting for LLMs. This should include a clear specification of the data distribution, the task distribution, and the model capacity. For example, are the tasks assumed to be independent and identically distributed (i.i.d.) or are they allowed to have some degree of correlation? What is the capacity of the model relative to the complexity of the tasks? These details are crucial for understanding the scope and limitations of the proposed framework. Without a clear definition, it is difficult to assess the validity of the experimental results and to compare the proposed framework with existing approaches.

Furthermore, the paper should provide a more detailed explanation of how the proposed framework addresses the challenges of continual learning in LLMs. This should include a discussion of the limitations of existing methods, such as catastrophic forgetting, and how the proposed framework overcomes these limitations. For example, how does the framework handle the trade-off between plasticity and stability? Does it use any specific techniques to mitigate catastrophic forgetting? The paper should also discuss the computational complexity of the proposed framework and its scalability to large-scale continual learning problems. A clear explanation of these aspects is essential for understanding the practical applicability of the proposed framework.

Finally, the paper should provide a clear evaluation protocol for the proposed framework. This should include a detailed description of how the different methods are compared, including the specific metrics used to evaluate their performance. For example, are the metrics task-specific or model-specific? How are the metrics aggregated across different tasks and models? The paper should also discuss the statistical significance of the results and provide a clear interpretation of the findings. Without a clear evaluation protocol, it is difficult to assess the validity of the experimental results and to compare the performance of different methods. The paper should also discuss the limitations of the evaluation protocol and potential biases in the experimental results.

### Questions

- What is the definition of 'continual learning' in the context of LLMs?
- What are the assumptions about the data distribution, task distribution, and model capacity?
- How does the proposed framework address the challenges of continual learning in LLMs?
- What is the evaluation protocol for the proposed framework?

### Rating

5

### Confidence

3

**********

## Reviewer 3

### Summary

This paper studies the problem of continual learning in LLMs. The authors categorize the continual learning problem into two axes: space (domain shift) and time (temporal drift). The authors conduct experiments to evaluate different methods on four families of methods: prompt optimization, supervised weight updates, reinforcement learning, and context compression. The authors also introduce a unified framework to compare different methods.

### Soundness

3

### Presentation

3

### Contribution

2

### Strengths

1. The paper is well-written and easy to follow.
2. The paper provides a unified framework to compare different methods for continual learning in LLMs.
3. The paper evaluates different methods on multiple benchmarks and tasks.

### Weaknesses

#### Some Related Works


#### comment

1. The paper does not provide a clear definition of what constitutes a 'continual learning' setting for LLMs. The authors do not specify the assumptions about the data distribution, the task distribution, or the model capacity. This lack of clarity makes it difficult to assess the validity of the experimental results.
2. The paper does not provide a clear explanation of how the proposed framework addresses the challenges of continual learning in LLMs. The authors do not discuss the limitations of existing methods for continual learning in LLMs, nor do they explain how their framework overcomes these limitations.
3. The paper does not provide a clear evaluation protocol for the proposed framework. The authors do not specify how the different methods are compared, nor do they provide a clear metric for evaluating the performance of the methods.
4. The paper does not provide a clear discussion of the limitations of the proposed framework. The authors do not discuss the assumptions made by the framework, nor do they discuss the potential biases in the experimental results.

### Suggestions

The paper would benefit significantly from a more rigorous definition of the continual learning setting within the context of Large Language Models (LLMs). Currently, the paper lacks specific details regarding the data distribution, task distribution, and model capacity. For instance, are the tasks assumed to be independent and identically distributed (i.i.d.) or are they allowed to have some degree of correlation? What is the capacity of the model relative to the complexity of the tasks? These details are crucial for understanding the scope and limitations of the proposed framework. Without a clear definition, it is difficult to assess the validity of the experimental results and to compare the proposed framework with existing approaches. The authors should explicitly state these assumptions and justify their choices. Furthermore, the paper should clarify how the proposed framework handles the trade-off between plasticity and stability, which is a fundamental challenge in continual learning.

To strengthen the paper, the authors should provide a more detailed explanation of how their framework addresses the challenges of continual learning in LLMs. The paper should discuss the limitations of existing methods for continual learning in LLMs, such as catastrophic forgetting, and how the proposed framework overcomes these limitations. For example, does the framework employ any specific techniques to mitigate catastrophic forgetting? Does it use any form of regularization or replay to maintain performance on previous tasks? The authors should also discuss the computational complexity of the proposed framework and its scalability to large-scale continual learning problems. A clear explanation of these aspects is essential for understanding the practical applicability of the proposed framework. The paper should also discuss the potential biases in the experimental results and how these biases might affect the conclusions.

Finally, the paper needs a clear evaluation protocol for the proposed framework. The authors should specify how the different methods are compared, including the specific metrics used to evaluate their performance. For example, are the metrics task-specific or model-specific? How are the metrics aggregated across different tasks and models? The paper should also discuss the statistical significance of the results and provide a clear interpretation of the findings. Without a clear evaluation protocol, it is difficult to assess the validity of the experimental results and to compare the performance of different methods. The authors should also discuss the limitations of the evaluation protocol and potential biases in the experimental results. A more rigorous evaluation protocol would greatly enhance the credibility of the paper.

### Questions

Please see the weakness part.

### Rating

5

### Confidence

3

**********

## Reviewer 4

### Summary

This paper studies the problem of continual learning in LLMs. The authors categorize the continual learning problem into two axes: space (domain shift) and time (temporal drift). The authors conduct experiments to evaluate different methods on four families of methods: prompt optimization, supervised weight updates, reinforcement learning, and context compression. The authors also introduce a unified framework to compare different methods.

### Soundness

3

### Presentation

3

### Contribution

3

### Strengths

1. The paper is well-written and easy to follow.
2. The paper provides a unified framework to compare different methods for continual learning in LLMs.
3. The paper evaluates different methods on multiple benchmarks and tasks.

### Weaknesses

#### Some Related Works


#### comment

1. The paper does not provide a clear definition of what constitutes a 'continual learning' setting for LLMs. The authors do not specify the assumptions about the data distribution, the task distribution, or the model capacity. This lack of clarity makes it difficult to assess the validity of the experimental results.
2. The paper does not provide a clear explanation of how the proposed framework addresses the challenges of continual learning in LLMs. The authors do not discuss the limitations of existing methods for continual learning in LLMs, nor do they explain how their framework overcomes these limitations.
3. The paper does not provide a clear evaluation protocol for the proposed framework. The authors do not specify how the different methods are compared, nor do they provide a clear metric for evaluating the performance of the methods.
4. The paper does not provide a clear discussion of the limitations of the proposed framework. The authors do not discuss the assumptions made by the framework, nor do they discuss the potential biases in the experimental results.

### Suggestions

The paper would benefit significantly from a more rigorous definition of the continual learning setting within the context of Large Language Models (LLMs). Currently, the paper lacks specific details regarding the data distribution, task distribution, and model capacity. For instance, are the tasks assumed to be independent and identically distributed (i.i.d.) or are they allowed to have some degree of correlation? What is the capacity of the model relative to the complexity of the tasks? These details are crucial for understanding the scope and limitations of the proposed framework. Without a clear definition, it is difficult to assess the validity of the experimental results and to compare the proposed framework with existing approaches. The authors should explicitly state these assumptions and justify their choices. Furthermore, the paper should clarify how the proposed framework handles the trade-off between plasticity and stability, which is a fundamental challenge in continual learning.

To strengthen the paper, the authors should provide a more detailed explanation of how their framework addresses the challenges of continual learning in LLMs. The paper should discuss the limitations of existing methods for continual learning in LLMs, such as catastrophic forgetting, and how the proposed framework overcomes these limitations. For example, does the framework employ any specific techniques to mitigate catastrophic forgetting? Does it use any form of regularization or replay to maintain performance on previous tasks? The authors should also discuss the computational complexity of the proposed framework and its scalability to large-scale continual learning problems. A clear explanation of these aspects is essential for understanding the practical applicability of the proposed framework. The paper should also discuss the potential biases in the experimental results and how these biases might affect the conclusions.

Finally, the paper needs a clear evaluation protocol for the proposed framework. The authors should specify how the different methods are compared, including the specific metrics used to evaluate their performance. For example, are the metrics task-specific or model-specific? How are the metrics aggregated across different tasks and models? The paper should also discuss the statistical significance of the results and provide a clear interpretation of the findings. Without a clear evaluation protocol, it is difficult to assess the validity of the experimental results and to compare the performance of different methods. The authors should also discuss the limitations of the evaluation protocol and potential biases in the experimental results. A more rigorous evaluation protocol would greatly enhance the credibility of the paper.

### Questions

Please see the weakness part.

### Rating

6

### Confidence

3

**********

}

I have finished generating simulated reviews from 4 reviewers. Next, I will generate verification content for these reviews:

\boxed_verification{
The reviewer has identified several weaknesses related to the lack of clarity in defining continual learning for LLMs, the absence of a clear explanation of how the framework addresses continual learning challenges, the lack of a clear evaluation protocol, and the absence of a discussion on the framework's limitations. I need to go through each of these points and see if they are supported by the content of the paper.

**Weakness 1: Lack of clear definition of continual learning for LLMs.**
- Check the introduction and method sections for explicit definitions.
- Look for discussions on assumptions about data/task/model.

**Weakness 2: Lack of explanation of how the framework addresses continual learning challenges.**
- Review the method section for how each method addresses the identified challenges (plasticity/stability, catastrophic forgetting).
- Look for discussions on limitations of existing methods and how the framework overcomes them.

**Weakness 3: Lack of a clear evaluation protocol.**
- Examine the experiment section for details on how methods are compared and metrics are used.
- Check if statistical significance or clear interpretation of results is discussed.

**Weakness 4: Lack of discussion on limitations of the framework.**
- Search for explicit statements about assumptions and potential biases.
- Check if the discussion section or elsewhere mentions limitations.

**Plan:**
1. Go to the "Introduction" and "Method" sections to check for explicit definitions of continual learning for LLMs.
2. Go to the "Method" section to see how each method addresses the challenges.
3. Go to the "Experiments" section to find details on the evaluation protocol.
4. Search the paper for any explicit statements about limitations.
**Reviewer 1 Weakness Analysis**

1. Weakness Statement:
"The paper does not provide a clear definition of what constitutes a 'continual learning' setting for LLMs. The authors do not specify the assumptions about the data distribution, the task distribution, or the model capacity. This lack of clarity makes it difficult to assess the validity of the experimental results."

2. Evidence Collection:
a) Method-related Evidence:
- The introduction mentions "continual learning as the problem of increasing competence as the world changes" and "continual learning is fundamentally about increasing competence as the world changes." (Introduction, Paragraph 1)
- The paper categorizes continual learning into "space, where the model encounters new domains, and time, where the underlying data drifts under a fixed task." (Introduction, Paragraph 2)
- The paper uses the Qwen3-8B model as the primary model for evaluation. (Method, Workflow)
- The experimental setups explicitly define the tasks and datasets used for each experiment (e.g., ToolUse, FinQA, SciKE-Bio for Domain Adaptation; 2025-11-20, 2025-12-01, 2026-01-01 for Agentic Task; ToolUse, FinQA, SciKE-Bio for Financial Analysis; 2022-11-20, 2022-12-01, 2023-01-01 for Noisy Temporal Drift; WebArena-Infinity with agentic tasks for Agentic Task).

b) Experiment-related Evidence:
- The "Domain Adaptation" experiment uses three unrelated tasks.
- The "Agentic Task" uses a sequence of agentic tasks.
- The "Financial Analysis" experiment uses three distinct financial datasets.
- The "Noisy Temporal Drift" experiment uses a sequence of Wikipedia snapshots.
- The "Domain Adaptation" experiment uses a fixed model (Qwen3-8B).
- The "Noisy Temporal Drift" experiment uses a fixed model (Qwen3-8B).
- The "Agentic Task" uses a fixed model (Qwen3-8B).
- The "Financial Analysis" experiment uses a fixed model (Qwen3-8B).

3. Literature Gap Analysis:
- The paper does not explicitly cite foundational CL papers to define its specific notion of CL for LLMs.

4. Validation Analysis:
- The reviewer is correct that the paper lacks a formal, explicit definition of "continual learning" within the context of LLMs. While the paper describes the problem and its axes (space and time), it doesn't provide a concise definition that distinguishes it from standard machine learning. The assumptions about data distribution are implicit (e.g., in-domain for domain adaptation, out-of-distribution for agentic tasks), but these are not explicitly stated. The task distribution is also implicitly defined by the chosen tasks. The model capacity is fixed for the experiments, which is a limitation acknowledged in the discussion. The paper relies on the reader's understanding of CL concepts and adapts them to LLMs.

5. Conclusion:
- Validity status: Valid
- Confidence level: High
- Key supporting evidence: Lack of explicit definition in the introduction or method sections, implicit assumptions about data/task distribution and model capacity.

1. Weakness Statement:
"The paper does not provide a clear explanation of how the proposed framework addresses the challenges of continual learning in LLMs. The authors do not discuss the limitations of existing methods for continual learning in LLMs, nor do they explain how their framework overcomes these limitations."

2. Evidence Collection:
a) Method-related Evidence:
- The "Unified Framework" section describes the evaluation protocol where each method is applied to different stages of the sequential tasks. (Method, Unified Framework)
- The "Prompt Optimization" subsection describes the limitations of prompt optimization in terms of catastrophic forgetting and the need for task-specific updates.
- The "Supervised Weight Updates" subsection mentions the limitations of weight updates in adapting to new tasks.
- The "Reinforcement Learning" subsection discusses the limitations of RL in terms of noisy rewards and stability-anchored methods.
- The "Context Compression" subsection highlights the limitations of context compression in accumulating new information.
- The "Discussion" section states: "Overall, our results suggest that continual learning is not a single capability: different patterns of environmental change require fundamentally different update behaviors. We hope that understanding where each method succeeds and fails will guide the design of more capable continual learning systems."

3. Literature Gap Analysis:
- The paper cites relevant works for each method but doesn't explicitly frame the limitations of *existing CL methods* in LLMs as a central problem it aims to solve.

4. Validation Analysis:
- The reviewer is partially correct. The paper *does* discuss the limitations of the individual methods it evaluates within the unified framework. For example, it explains why prompt optimization struggles with catastrophic forgetting and why weight updates might not adapt well to new tasks. The "Discussion" section also touches upon the idea that different CL methods are suited for different types of environmental changes. However, the paper doesn't explicitly state that the *framework itself* directly addresses the limitations of existing CL methods in LLMs. The framework's strength lies in providing a unified way to *evaluate* different methods, highlighting their strengths and weaknesses in the specific CL setting for LLMs.

5. Conclusion:
- Validity status: Partially Valid
- Confidence level: High
- Key supporting evidence: The paper discusses limitations of individual methods, but doesn't explicitly frame the framework as a solution to the limitations of existing CL methods.

1. Weakness Statement:
"The paper does not provide a clear evaluation protocol for the proposed framework. The authors do not specify how the different methods are compared, nor do they provide a clear metric for evaluating the performance of the methods."

2. Evidence Collection:
a) Method-related Evidence:
- The "Unified Framework" section describes the evaluation protocol: "After each stage we evaluate on every stage’s eval set, producing R i , j = acc ⁡ ( θ i , T j eval ) , i ∈ { 0 , … , K } , j ∈ { 1 , … , K } , with row 0 0 the base model before any update. Further details on task design choices can be found in Appendix A.2 ." (Method, Unified Framework)
- The "Experiments" section details the specific metrics used for each experiment (accuracy, F1 score, BLEU score, Rouge score, accuracy).

3. Literature Gap Analysis:
- The paper clearly states the metrics used for each experiment.

4. Validation Analysis:
- The reviewer is incorrect. The paper provides a clear evaluation protocol in the "Unified Framework" section, outlining how performance is measured across different stages and tasks. The "Experiments" section further specifies the metrics used for each specific experiment.

5. Conclusion:
- Validity status: Invalid
- Confidence level: High
- Key supporting evidence: Explicit description of the evaluation protocol in the "Unified Framework" section and specific metrics in the "Experiments" section.

1. Weakness Statement:
"The paper does not provide a clear discussion of the limitations of the proposed framework. The authors do not discuss the assumptions made by the framework, nor do they discuss the potential biases in the experimental results."

2. Evidence Collection:
a) Method-related Evidence:
- The "Discussion" section mentions limitations of the framework: "To draw unified conclusions, we use a single model (Qwen3-8B)..." and "In addition, our benchmark suite captures only a subset of realistic environmental change: domain shifts, agentic sequences, noisy temporal drift, and discrete factual updates."

b) Experiment-related Evidence:
- The paper uses specific benchmark datasets for each experiment.
- The paper uses a single model for all experiments.

3. Literature Gap Analysis:
- The paper doesn't explicitly discuss potential biases in the experimental results beyond the limitations of the benchmark suite.

4. Validation Analysis:
- The reviewer is partially correct. The paper *does* discuss the limitations of the framework and the benchmark suite in the "Discussion" section. It acknowledges the use of a single model and the limited scope of the benchmark. However, it does not explicitly discuss potential biases in the experimental results beyond these limitations.

5. Conclusion:
- Validity status: Partially Valid
- Confidence level: High
- Key supporting evidence: The "Discussion" section addresses some limitations, but lacks a broader discussion of potential biases in the experimental results.

**Reviewer 1 Question Analysis**

1. Question Statement:
"- What is the definition of 'continual learning' in the context of LLMs?"

2. Evidence Collection:
- As analyzed in the first weakness, the paper lacks a formal definition.

3. Validation Analysis:
- The question highlights a valid point about the lack of a clear definition.

4. Conclusion:
- Validity status: Valid (as a point for clarification)
- Confidence level: High

1. Question Statement:
"- What are the assumptions about the data distribution, task distribution, and model capacity?"

2. Evidence Collection:
- As analyzed in the first weakness, the assumptions are implicit rather than explicitly stated.

3. Validation Analysis:
- The question points to a valid area where the paper could be more explicit.

4. Conclusion:
- Validity status: Valid (as a point for clarification)
- Confidence level: High

1. Question Statement:
"- How does the proposed framework address the challenges of continual learning in LLMs?"

2. Evidence Collection:
- As analyzed in the second weakness, the paper discusses the limitations of individual methods but doesn't explicitly frame the framework as a solution to these limitations.

3. Validation Analysis:
- The question highlights a partially valid point. The framework's strength lies in evaluating methods, but it doesn't inherently solve the challenges.

4. Conclusion:
- Validity status: Partially Valid (as a point for clarification)
- Confidence level: High

1. Question Statement:
"- What is the evaluation protocol for the proposed framework?"

2. Evidence Collection:
- As analyzed in the third weakness, the paper provides a clear evaluation protocol.

3. Validation Analysis:
- The question points to an invalid point, as the paper does provide an evaluation protocol.

4. Conclusion:
- Validity status: Invalid (as a point for clarification)
- Confidence level: High

**Synthesis and Reflection**

The reviewer raises several valid points regarding the paper's clarity and completeness. The most significant weakness is the lack of a formal definition of "continual learning" for LLMs, which makes it difficult to understand the scope and validity of the experimental results. While the paper does discuss the limitations of individual methods and provides an evaluation protocol, it doesn't explicitly frame the proposed framework as a direct solution to the identified limitations of existing CL methods in LLMs. The discussion section does address some limitations of the framework and the benchmark, but a broader discussion of potential biases in the experimental results is missing. The reviewer's claim about the absence of a clear evaluation protocol is incorrect, as the paper provides a detailed description of the evaluation process. Overall, the reviewer's criticisms are well-substantiated by the paper's content, highlighting areas where the paper could be significantly improved in terms of clarity and explicitness.

**Final Conclusion on Reviewer 1's Validity:**

- Definition of Continual Learning: Valid
- Explanation of Framework's Addressing Challenges: Partially Valid
- Evaluation Protocol: Invalid
- Discussion of Limitations: Partially Valid
}

Now, I have successfully verified each review. Next, I will organize this content and output the final review decision:

\boxed_review{
## Summary:

This paper explores the problem of continual learning in Large Language Models (LLMs) by categorizing it into two primary axes: 'space,' which refers to domain shifts, and 'time,' which encompasses temporal changes in the data distribution. The authors introduce a unified framework designed to compare various continual learning methods across these dimensions. The study evaluates four families of methods: prompt optimization, supervised weight updates, reinforcement learning, and context compression. The authors conduct experiments on multiple benchmarks and tasks, including domain adaptation, agentic tasks, financial analysis, and temporally-dependent knowledge updates. The core idea is to assess how well different methods can adapt to changes in the data distribution over time, specifically focusing on the trade-offs between plasticity and stability. The paper's main contribution lies in its systematic approach to evaluating continual learning methods in LLMs, providing a framework for future research in this area. The experiments reveal that different methods are better suited to different types of environmental changes, suggesting that a one-size-fits-all approach to continual learning is unlikely to be effective. The authors find that prompt-based methods tend to perform well in scenarios with domain shifts, while weight update methods are more effective in scenarios with temporal drift. Reinforcement learning methods are shown to be sensitive to noisy rewards, and context compression methods struggle to accumulate new information effectively. Overall, the paper provides valuable insights into the strengths and weaknesses of different continual learning methods for LLMs, highlighting the importance of considering the specific nature of the data distribution when selecting an appropriate method. The paper's findings suggest that the challenge of continual learning in LLMs is multifaceted, requiring a nuanced approach that takes into account the specific characteristics of the task and the data.


## Soundness:

3.0


## Presentation:

2.75


## Contribution:

2.25


## Strengths:

I found several aspects of this paper to be particularly strong. First, the paper's systematic approach to evaluating continual learning methods in LLMs is a significant contribution. The authors have successfully created a unified framework that allows for a fair comparison of different methods across various tasks and settings. This framework is a valuable tool for the community and will likely facilitate further research in this area. The paper's categorization of continual learning into 'space' and 'time' axes is also a useful way to frame the problem, providing a clear lens through which to analyze the performance of different methods. The authors' choice of benchmarks and tasks is commendable, as they cover a range of realistic scenarios, including domain adaptation, agentic tasks, financial analysis, and temporally-dependent knowledge updates. This broad range of tasks allows for a more comprehensive evaluation of the methods and provides a more robust assessment of their strengths and weaknesses. Furthermore, the paper's analysis of the results is insightful, highlighting the trade-offs between plasticity and stability and suggesting that different methods are better suited to different types of environmental changes. The authors' discussion of the limitations of each method is also valuable, as it provides a more nuanced understanding of the challenges involved in continual learning for LLMs. Finally, the paper is well-written and easy to follow, making it accessible to a wide audience. The clear presentation of the methods, experiments, and results contributes to the overall strength of the paper.


## Weaknesses:

Despite its strengths, I have identified several weaknesses in this paper that warrant careful consideration. The most significant issue is the lack of a clear and explicit definition of 'continual learning' within the context of LLMs. While the paper describes the problem and its axes, it does not provide a concise definition that distinguishes it from standard machine learning. This lack of clarity makes it difficult to assess the validity of the experimental results and to compare the proposed framework with existing approaches. The paper implicitly assumes a specific notion of continual learning, but this assumption is not explicitly stated or justified. For example, the paper does not specify the assumptions about the data distribution, the task distribution, or the model capacity. These assumptions are crucial for understanding the scope and limitations of the proposed framework. The paper uses a fixed model (Qwen3-8B) for all experiments, which is a limitation acknowledged in the discussion, but the lack of explicit assumptions about the data and task distributions is a significant oversight. This lack of clarity makes it difficult to understand the scope and limitations of the proposed framework. My confidence in this weakness is high, as it is directly observable from the lack of explicit definitions and assumptions in the paper. 

Another weakness lies in the paper's explanation of how the proposed framework addresses the challenges of continual learning in LLMs. While the paper does discuss the limitations of the individual methods it evaluates, it does not explicitly state that the framework itself directly addresses the limitations of existing CL methods in LLMs. The framework's strength lies in providing a unified way to *evaluate* different methods, highlighting their strengths and weaknesses in the specific CL setting for LLMs. However, the paper does not explicitly state that the framework itself directly addresses the limitations of existing CL methods in LLMs. The framework's strength lies in providing a unified way to *evaluate* different methods, highlighting their strengths and weaknesses in the specific CL setting for LLMs. While the paper does discuss the limitations of individual methods, it does not explicitly frame the framework as a solution to these limitations. This lack of clarity makes it difficult to understand the paper's contribution to the field. My confidence in this weakness is high, as the paper does not explicitly state that the framework addresses the limitations of existing CL methods. 

Finally, while the paper does provide an evaluation protocol in the 'Unified Framework' section, it does not explicitly discuss potential biases in the experimental results beyond the limitations of the benchmark suite. The paper acknowledges the use of a single model and the limited scope of the benchmark, but it does not delve into the potential biases introduced by the specific datasets and tasks chosen for evaluation. This lack of discussion is a significant oversight, as it is crucial to understand the limitations of the experimental results and to avoid drawing overly broad conclusions. My confidence in this weakness is high, as the paper does not explicitly discuss potential biases in the experimental results beyond the limitations of the benchmark suite. While the paper does provide an evaluation protocol, the reviewer's claim about the absence of a clear evaluation protocol is incorrect, as the paper provides a detailed description of the evaluation process. This was a misunderstanding on the reviewer's part.


## Suggestions:

To address the identified weaknesses, I recommend several concrete improvements. First, the paper needs to provide a more rigorous definition of 'continual learning' within the context of LLMs. This definition should include explicit assumptions about the data distribution, the task distribution, and the model capacity. For example, the authors should specify whether the tasks are assumed to be independent and identically distributed (i.i.d.) or are allowed to have some degree of correlation. What is the capacity of the model relative to the complexity of the tasks? These details are crucial for understanding the scope and limitations of the proposed framework. Without a clear definition, it is difficult to assess the validity of the experimental results and to compare the proposed framework with existing approaches. The authors should explicitly state these assumptions and justify their choices. This would significantly improve the clarity and rigor of the paper. 

Second, the paper should provide a more detailed explanation of how the proposed framework addresses the challenges of continual learning in LLMs. The paper should discuss the limitations of existing methods for continual learning in LLMs, such as catastrophic forgetting, and how the proposed framework overcomes these limitations. For example, does the framework employ any specific techniques to mitigate catastrophic forgetting? Does it use any form of regularization or replay to maintain performance on previous tasks? The authors should also discuss the computational complexity of the proposed framework and its scalability to large-scale continual learning problems. A clear explanation of these aspects is essential for understanding the practical applicability of the proposed framework. The paper should also discuss the potential biases in the experimental results and how these biases might affect the conclusions. This would provide a more comprehensive understanding of the paper's contribution to the field. 

Finally, the paper should include a more thorough discussion of the limitations of the proposed framework. The authors should discuss the assumptions made by the framework, and the potential biases in the experimental results. The paper should also discuss the potential for future research to address these limitations. For example, the authors could explore the use of more advanced continual learning techniques, such as meta-learning or reinforcement learning, to improve the performance of the framework. The authors should also consider the impact of different model architectures and training procedures on the performance of the framework. A more comprehensive discussion of the limitations would help to guide future research in this area. By addressing these points, the paper would be significantly strengthened and would provide a more valuable contribution to the field of continual learning in LLMs.


## Questions:

I have several questions that arise from my analysis of the paper. First, what is the precise definition of 'continual learning' in the context of LLMs? The paper does not provide a clear definition, and this lack of clarity makes it difficult to assess the validity of the experimental results. What are the specific assumptions about the data distribution, task distribution, and model capacity? These assumptions are crucial for understanding the scope and limitations of the proposed framework. Second, how does the proposed framework address the challenges of continual learning in LLMs? The paper discusses the limitations of individual methods, but it does not explicitly state that the framework itself directly addresses these limitations. Does the framework employ any specific techniques to mitigate catastrophic forgetting or to adapt to new tasks? What are the computational complexity and scalability of the proposed framework? Third, what are the potential biases in the experimental results? The paper acknowledges the use of a single model and the limited scope of the benchmark, but it does not delve into the potential biases introduced by the specific datasets and tasks chosen for evaluation. How might these biases affect the conclusions of the paper? Finally, what are the limitations of the proposed framework? The paper acknowledges the use of a single model and the limited scope of the benchmark, but it does not provide a comprehensive discussion of the limitations of the framework itself. What are the potential for future research to address these limitations? These questions are crucial for understanding the paper's contribution to the field and for guiding future research in this area.


## Rating:

4.75


## Confidence:

3.0


## Decision:

Reject
}