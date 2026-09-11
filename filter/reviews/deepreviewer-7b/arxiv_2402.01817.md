I will use Standard Mode for comprehensive thinking. As a professional reviewer, I will simulate 4 different reviewers, followed by the verification thinking. Then I will output the Finally Review Output. Let me think - Standard Mode means I will output the original review, followed by the verification thinking. Considering that I am currently in standard mode, I should think from my existing knowledge and consider some related work content when writing about weaknesses. Then I will output the Finally Review Output and Meta Review Output:

\boxed_simreviewers{
## Reviewer 1

### Summary

The paper discusses the limitations of LLMs in planning and reasoning tasks, arguing that LLMs cannot perform planning or self-verification independently. The authors propose the LLM-Modulo Framework, which integrates LLMs with external symbolic components for improved planning and reasoning, emphasizing the LLM's role as an approximate knowledge source and candidate plan generator.

### Soundness

2

### Presentation

2

### Contribution

2

### Strengths

1. The paper is well-structured, with a clear and logical flow that effectively communicates the authors' arguments and the proposed framework.
2. The authors provide a comprehensive review of the literature, clearly identifying the limitations of LLMs in planning and reasoning tasks. This thorough analysis strengthens the foundation for their proposed framework and helps position their work within the broader context of AI research.
3. The LLM-Modulo Framework is a novel approach that addresses the identified limitations of LLMs. By integrating LLMs with external symbolic components, the framework offers a more robust solution for planning and reasoning tasks.

### Weaknesses

#### Some Related Works


#### comment

1. The paper's motivation is not entirely convincing. The authors argue that LLMs cannot perform planning or self-verification independently, yet they do not provide a clear explanation of why this is a problem or how their proposed framework addresses this issue. A more detailed discussion of the limitations of LLMs in planning and reasoning, and how the LLM-Modulo Framework overcomes these limitations, would strengthen the paper's motivation.
2. The paper lacks a detailed analysis of the computational complexity and efficiency of the LLM-Modulo Framework. It would be beneficial to include a discussion of the time and space complexity of the framework, as well as any potential bottlenecks or limitations in its scalability.
3. The paper does not provide a thorough evaluation of the LLM-Modulo Framework. While the authors present case studies, a more comprehensive evaluation, including comparisons with existing planning and reasoning frameworks, would be necessary to demonstrate the effectiveness and advantages of their approach. The evaluation should also consider different types of planning problems and varying levels of complexity to provide a more robust assessment of the framework's performance.

### Suggestions

The paper would benefit significantly from a more detailed explanation of the specific limitations of LLMs in planning and reasoning that the LLM-Modulo Framework aims to address. For instance, the authors could elaborate on how the inherent probabilistic nature of LLMs leads to difficulties in guaranteeing the correctness of generated plans, or how the lack of a strong notion of time in LLMs hinders the ability to handle temporal constraints in planning tasks. Providing concrete examples of planning scenarios where LLMs fail due to these limitations would further strengthen the motivation for the proposed framework. Furthermore, the authors should clearly articulate how the integration of external symbolic components in the LLM-Modulo Framework mitigates these specific issues. For example, they could explain how the symbolic components provide a structured environment for planning and reasoning, ensuring the soundness and completeness of the generated plans, and how they interact with the LLM to guide the planning process. This would help to clarify the novelty and significance of their approach.

To enhance the paper's technical depth, the authors should include a more rigorous analysis of the computational complexity and efficiency of the LLM-Modulo Framework. This analysis should consider the time and space complexity of both the LLM and the external symbolic components, as well as the overhead introduced by the interaction between them. It would be beneficial to discuss how the framework scales with the size and complexity of the planning problem, and to identify any potential bottlenecks or limitations in its scalability. For example, the authors could analyze the number of LLM calls required for different planning problems, and how this number affects the overall computational cost. Additionally, the authors should provide a more detailed discussion of the trade-offs between the expressiveness of the external symbolic components and the computational efficiency of the framework. This would help readers understand the practical implications of using the LLM-Modulo Framework in real-world applications.

Finally, the paper needs a more comprehensive evaluation of the LLM-Modulo Framework. The authors should compare their framework with existing planning and reasoning frameworks, both in terms of performance and computational efficiency. This comparison should include a variety of planning problems with different characteristics, such as different levels of complexity, different types of constraints, and different planning domains. The evaluation should also consider the robustness of the framework to different types of errors and uncertainties, and should provide a detailed analysis of the framework's strengths and weaknesses. For example, the authors could evaluate the framework on benchmark planning problems, and compare its performance with state-of-the-art planning algorithms. This would provide a more objective assessment of the framework's effectiveness and its potential for practical applications.

### Questions

1. How does the LLM-Modulo Framework handle situations where the external symbolic components are not available or are difficult to define?
2. Can the authors provide more details on how the LLM-Modulo Framework ensures the soundness and completeness of the generated plans?
3. What are the limitations of the LLM-Modulo Framework in terms of scalability and computational efficiency?

### Rating

3

### Confidence

4

**********

## Reviewer 2

### Summary

This paper argues that LLMs cannot perform planning or self-verification independently, and proposes a framework called LLM-Modulo Framework to address this issue.

### Soundness

2

### Presentation

2

### Contribution

2

### Strengths

The paper is well-organized and clearly written, making it easy to understand.

### Weaknesses

#### Some Related Works


#### comment

1. The paper's motivation is not entirely convincing. The authors argue that LLMs cannot perform planning or self-verification independently, yet they do not provide a clear explanation of why this is a problem or how their proposed framework addresses this issue. A more detailed discussion of the limitations of LLMs in planning and reasoning, and how the LLM-Modulo Framework overcomes these limitations, would strengthen the paper's motivation.

2. The paper lacks a detailed analysis of the computational complexity and efficiency of the LLM-Modulo Framework. It would be beneficial to include a discussion of the time and space complexity of the framework, as well as any potential bottlenecks or limitations in its scalability.

3. The paper does not provide a thorough evaluation of the LLM-Modulo Framework. While the authors present case studies, a more comprehensive evaluation, including comparisons with existing planning and reasoning frameworks, would be necessary to demonstrate the effectiveness and advantages of their approach. The evaluation should also consider different types of planning problems and varying levels of complexity to provide a more robust assessment of the framework's performance.

### Suggestions

The paper would benefit significantly from a more detailed explanation of the specific limitations of LLMs in planning and reasoning that the LLM-Modulo Framework aims to address. For instance, the authors could elaborate on how the inherent probabilistic nature of LLMs leads to difficulties in guaranteeing the correctness of generated plans, or how the lack of a strong notion of time in LLMs hinders the ability to handle temporal constraints in planning tasks. Providing concrete examples of planning scenarios where LLMs fail due to these limitations would further strengthen the motivation for the proposed framework. Furthermore, the authors should clearly articulate how the integration of external symbolic components in the LLM-Modulo Framework mitigates these specific issues. For example, they could explain how the symbolic components provide a structured environment for planning and reasoning, ensuring the soundness and completeness of the generated plans, and how they interact with the LLM to guide the planning process. This would help to clarify the novelty and significance of their approach.

To enhance the paper's technical depth, the authors should include a more rigorous analysis of the computational complexity and efficiency of the LLM-Modulo Framework. This analysis should consider the time and space complexity of both the LLM and the external symbolic components, as well as the overhead introduced by the interaction between them. It would be beneficial to discuss how the framework scales with the size and complexity of the planning problem, and to identify any potential bottlenecks or limitations in its scalability. For example, the authors could analyze the number of LLM calls required for different planning problems, and how this number affects the overall computational cost. Additionally, the authors should provide a more detailed discussion of the trade-offs between the expressiveness of the external symbolic components and the computational efficiency of the framework. This would help readers understand the practical implications of using the LLM-Modulo Framework in real-world applications.

Finally, the paper needs a more thorough evaluation of the LLM-Modulo Framework. The authors should compare their framework with existing planning and reasoning frameworks, both in terms of performance and computational efficiency. This comparison should include a variety of planning problems with different characteristics, such as different levels of complexity, different types of constraints, and different planning domains. The evaluation should also consider the robustness of the framework to different types of errors and uncertainties, and should provide a detailed analysis of the framework's strengths and weaknesses. For example, the authors could evaluate the framework on benchmark planning problems, and compare its performance with state-of-the-art planning algorithms. This would provide a more objective assessment of the framework's effectiveness and its potential for practical applications.

### Questions

See Weaknesses.

### Rating

3

### Confidence

3

**********

## Reviewer 3

### Summary

The paper proposes a framework called LLM-Modulo Framework, which integrates LLMs with external symbolic components for improved planning and reasoning. The authors argue that LLMs cannot perform planning or self-verification independently and propose the LLM-Modulo Framework to address this issue. The framework consists of a generate-test-critique loop, where the LLM generates candidate plans, and external critics evaluate and refine them. The authors also discuss the limitations of LLMs in planning and reasoning tasks and provide case studies to illustrate the effectiveness of the proposed framework.

### Soundness

3

### Presentation

3

### Contribution

2

### Strengths

1. The paper is well-written and easy to follow.
2. The authors provide a comprehensive review of the literature, clearly identifying the limitations of LLMs in planning and reasoning tasks.
3. The LLM-Modulo Framework is a novel approach that integrates LLMs with external symbolic components for improved planning and reasoning.

### Weaknesses

#### Some Related Works


#### comment

1. The paper's motivation is not entirely convincing. The authors argue that LLMs cannot perform planning or self-verification independently, yet they do not provide a clear explanation of why this is a problem or how their proposed framework addresses this issue. A more detailed discussion of the limitations of LLMs in planning and reasoning, and how the LLM-Modulo Framework overcomes these limitations, would strengthen the paper's motivation.
2. The paper lacks a detailed analysis of the computational complexity and efficiency of the LLM-Modulo Framework. It would be beneficial to include a discussion of the time and space complexity of the framework, as well as any potential bottlenecks or limitations in its scalability.
3. The paper does not provide a thorough evaluation of the LLM-Modulo Framework. While the authors present case studies, a more comprehensive evaluation, including comparisons with existing planning and reasoning frameworks, would be necessary to demonstrate the effectiveness and advantages of their approach. The evaluation should also consider different types of planning problems and varying levels of complexity to provide a more robust assessment of the framework's performance.

### Suggestions

The paper would benefit from a more rigorous justification of the proposed LLM-Modulo Framework. While the authors argue that LLMs cannot perform planning or self-verification independently, they do not adequately explain why this is a significant limitation or how their framework specifically addresses it. A more detailed discussion of the inherent limitations of LLMs in these tasks, perhaps drawing on existing literature on the theoretical boundaries of LLM capabilities, would be valuable. For example, the authors could discuss the challenges of using LLMs for symbolic reasoning, such as their tendency to generate plans that are syntactically correct but semantically flawed, or their difficulty in handling complex temporal constraints. Furthermore, the paper should provide a more concrete explanation of how the external symbolic components interact with the LLM to overcome these limitations. This could involve a detailed description of the types of symbolic representations used, the algorithms employed for verification and refinement, and the specific mechanisms by which the LLM is guided to generate more robust plans. 

To strengthen the paper's technical contribution, the authors should include a more detailed analysis of the computational complexity and efficiency of the LLM-Modulo Framework. This analysis should consider the time and space complexity of both the LLM and the external symbolic components, as well as the overhead introduced by the interaction between them. It would be beneficial to provide a theoretical analysis of the framework's scalability, discussing how its performance is affected by the size and complexity of the planning problems. For example, the authors could analyze the number of LLM calls required for different planning problems, and how this number affects the overall computational cost. Additionally, the paper should include a more thorough evaluation of the LLM-Modulo Framework, comparing its performance with existing planning and reasoning frameworks. This evaluation should include a variety of planning problems with different characteristics, such as different levels of complexity, different types of constraints, and different planning domains. The authors should also consider the robustness of the framework to different types of errors and uncertainties, and provide a detailed analysis of the framework's strengths and weaknesses. 

Finally, the paper should provide a more detailed discussion of the limitations of the LLM-Modulo Framework. While the authors acknowledge that the framework is not a perfect solution, they do not adequately discuss the potential challenges and limitations that may arise in practice. For example, the authors could discuss the sensitivity of the framework to the choice of external symbolic components, the potential for the framework to get stuck in local optima, or the difficulty of debugging and interpreting the generated plans. Furthermore, the paper should discuss the potential ethical implications of using LLMs for planning and reasoning, such as the potential for bias or the risk of misuse. A more thorough discussion of these limitations would help to provide a more balanced and nuanced perspective on the proposed framework.

### Questions

1. How does the LLM-Modulo Framework handle situations where the external symbolic components are not available or are difficult to define?
2. Can the authors provide more details on how the LLM-Modulo Framework ensures the soundness and completeness of the generated plans?
3. What are the limitations of the LLM-Modulo Framework in terms of scalability and computational efficiency?

### Rating

5

### Confidence

3

**********

## Reviewer 4

### Summary

The paper presents a position paper arguing that LLMs cannot be used as standalone planners or reasoners. The authors argue that LLMs are not capable of planning or self-verifying, and that the LLMs can only be used as approximate knowledge sources and candidate plan generators within a framework that integrates them with external symbolic components. The authors propose the LLM-Modulo Framework, which integrates LLMs with external symbolic components for improved planning and reasoning, emphasizing the LLM's role as an approximate knowledge source and candidate plan generator. The paper also discusses the limitations of LLMs in planning and reasoning tasks and provides case studies of adapting the LLM-Modulo Framework to classical planning domains and a recent travel planning benchmark.

### Soundness

3

### Presentation

3

### Contribution

3

### Strengths

- The paper is well-written and easy to follow.
- The authors provide a comprehensive review of the literature, clearly identifying the limitations of LLMs in planning and reasoning tasks.
- The LLM-Modulo Framework is a novel approach that integrates LLMs with external symbolic components for improved planning and reasoning.
- The paper includes case studies of adapting the LLM-Modulo Framework to classical planning domains and a recent travel planning benchmark, demonstrating the practical applicability of the proposed framework.

### Weaknesses

#### Some Related Works


#### comment

 - The paper does not provide a detailed analysis of the computational complexity and efficiency of the LLM-Modulo Framework. It would be beneficial to include a discussion of the time and space complexity of the framework, as well as any potential bottlenecks or limitations in its scalability.
- The paper does not provide a thorough evaluation of the LLM-Modulo Framework. While the authors present case studies, a more comprehensive evaluation, including comparisons with existing planning and reasoning frameworks, would be necessary to demonstrate the effectiveness and advantages of their approach. The evaluation should also consider different types of planning problems and varying levels of complexity to provide a more robust assessment of the framework's performance.

### Suggestions

The paper would benefit from a more rigorous analysis of the computational aspects of the proposed LLM-Modulo Framework. Specifically, the authors should delve into the time and space complexity of the framework, considering both the LLM component and the external symbolic components. This analysis should include a breakdown of the computational cost associated with each stage of the framework, such as the generation of candidate plans, the application of external critics, and the iterative backpropagation process. Furthermore, it would be valuable to explore the potential bottlenecks that might arise in the framework, such as the computational cost of the LLM or the complexity of the symbolic reasoning steps. This analysis should also consider how the framework scales with the size and complexity of the planning problems, providing insights into its practical applicability and limitations. For example, the authors could analyze how the number of LLM calls and the size of the symbolic representations affect the overall runtime and memory usage. Such a detailed analysis would provide a more solid foundation for the practical implementation and deployment of the LLM-Modulo Framework.

To strengthen the evaluation of the LLM-Modulo Framework, the authors should conduct a more comprehensive empirical study. This study should include comparisons with existing planning and reasoning frameworks, using a variety of benchmark problems with different characteristics and complexities. The evaluation should not only focus on the success rate of the framework but also consider other metrics, such as the efficiency of the planning process, the quality of the generated plans, and the robustness of the framework to different types of errors. For instance, the authors could compare the performance of the LLM-Modulo Framework with other state-of-the-art planning algorithms on standard planning benchmarks, such as the International Planning Competition benchmarks. This would provide a more objective assessment of the framework's effectiveness and its advantages over existing approaches. Additionally, the evaluation should explore the framework's performance under different conditions, such as varying the number of LLM calls, the complexity of the symbolic components, and the quality of the initial plan candidates. This would provide a more nuanced understanding of the framework's strengths and weaknesses.

Finally, the paper should address the limitations of the LLM-Modulo Framework more explicitly. While the authors acknowledge that LLMs cannot perform planning or self-verification independently, they should further discuss the potential challenges and limitations that might arise in practice. For example, the authors could explore the sensitivity of the framework to the choice of external symbolic components, the potential for the framework to get stuck in local optima, and the difficulty of debugging and interpreting the generated plans. Furthermore, the authors should discuss the potential ethical implications of using LLMs for planning and reasoning, such as the potential for bias or the risk of misuse. A more thorough discussion of these limitations would provide a more balanced and nuanced perspective on the proposed framework and its potential impact.

### Questions

- How does the LLM-Modulo Framework handle situations where the external symbolic components are not available or are difficult to define?
- Can the authors provide more details on how the LLM-Modulo Framework ensures the soundness and completeness of the generated plans?
- What are the limitations of the LLM-Modulo Framework in terms of scalability and computational efficiency?

### Rating

6

### Confidence

3

**********

}

I have finished generating simulated reviews from 4 reviewers. Next, I will generate verification content for these reviews:

\boxed_verification{
The user wants me to validate weaknesses identified by reviewers in a given paper. I need to go through each reviewer's comments and check if the criticism is valid based on the content of the paper.

Here's my plan:
1. **Parse each reviewer's comments and extract the identified weaknesses.**
2. **For each weakness, find supporting evidence (or lack thereof) in the paper.** This involves looking at the method description, experimental setup, results, and related work sections.
3. **Categorize the weakness** (theoretical, methodological, experimental, practical).
4. **Provide a validation analysis** for each weakness, including evidence and a conclusion on its validity.
**Review 1 Weaknesses:**

1. **Weakness Statement:** The paper's motivation is not entirely convincing. The authors argue that LLMs cannot perform planning or self-verification independently, yet they do not provide a clear explanation of why this is a problem or how their proposed framework addresses this issue. A more detailed discussion of the limitations of LLMs in planning and reasoning, and how the LLM-Modulo Framework overcomes these limitations, would strengthen the paper's motivation.

2. **Evidence Collection:**
    a) Method-related Evidence:
        - The paper states in the Introduction: "In truth, LLMs can be a genuine artificial approximate knowledge source (see Figure 1 ). Even from a pure engineering perspective, a system that takes constant time to produce the next token cannot possibly be doing principled reasoning on its own. The underlying n-gram nature makes them effortlessly intermix what would be considered disparate fields of study (not surprisingly, LLMs are seen to be very good at making/finding analogies!). The challenge is to leverage them without wrongly ascribing to them capabilities they don’t possess."
        - The paper further elaborates in Section 2: "In this section, we will first review literature that calls into question claims about the planning capabilities of LLMs ( Kambhampati et al., 2023c ; Kambhampati, 2024 ) several recent studies confirm that LLMs are not actually able to generate executable plans when they are used in autonomous modes ( Valmeekam et al., 2023c ; Liu et al., 2023 ; Silver et al., 2022 ) . For example, in ( Valmeekam et al., 2023c ; Valmeekam et al., 2023b ) , we evaluate LLMs’ ability to generate correct plans on a suite of planning problem instances based on the kinds of domains employed in the International Planning Competition ( IPC, 1998 ) . To eliminate the subjective aspect of analysis that forms the core part of many earlier efforts to evaluate the reasoning capabilities of LLMs, we leverage models and tools from the automated planning community to automate evaluation. We show that results in the autonomous mode are pretty bleak. On average, only about 12% of the plans that the best LLM (GPT-4) generates are actually executable without errors and goal-reaching. We demonstrate that the performance deteriorates further if the names of the actions and objects in the domain are obfuscated–a change that doesn’t in any way affect the performance of the standard AI planners. This further suggests that LLMs are more likely doing approximate retrieval of plans than actual planning."
        - The paper introduces the LLM-Modulo Framework in Section 3, stating: "While Section 2 questions the claims that LLMs are capable of planning/reasoning by themselves, it is certainly not meant to imply that LLMs don’t have any constructive roles to play in solving planning/reasoning tasks. On the contrary, as discussed in the Introduction, their uncanny ability to generate ideas/potential candidate solutions–albeit with no guarantees about those guesses–can be valuable in the generate-test-critique setups in conjunction with either model-based verifiers or expert humans in the loop. Accordingly, we propose a general ‘‘LLM-Modulo’’ framework 7 7 7 The name LLM-Modulo is inspired by the SAT-Modulo system ( Nieuwenhuis & Oliveras, 2006 ) . . . The LLM-Modulo framework proposed in this position paper tackles this challenge."

3. **Literature Gap Analysis:**
    - The paper cites relevant literature (Kambhampati et al., 2023c; Kambhampati, 2024; Valmeekam et al., 2023c; Liu et al., 2023; Silver et al., 2022) to support its claims about LLMs' limitations in planning and reasoning.

4. **Validation Analysis:**
    - The paper explicitly states the motivation as addressing the over-optimism about LLMs' planning capabilities and proposing a framework to leverage LLMs more effectively. The introduction sets the stage by highlighting the potential of LLMs as knowledge sources and the need for a framework to integrate them with symbolic components. The paper argues that LLMs are better suited for generating candidate plans, which can then be refined by external verifiers, rather than being used as standalone planners. The motivation is present, but it could be strengthened by explicitly stating the negative consequences of using LLMs as autonomous planners.

5. **Conclusion:**
    - Validity status: Partially Valid
    - Confidence level: High
    - Key supporting evidence: The paper clearly states the problem and proposes a solution, but the explanation of the negative implications of LLMs' autonomous capabilities could be more explicit.

1. **Weakness Statement:** The paper lacks a detailed analysis of the computational complexity and efficiency of the LLM-Modulo Framework. It would be beneficial to include a discussion of the time and space complexity of the framework, as well as any potential bottlenecks or limitations in its scalability.

2. **Evidence Collection:**
    a) Method-related Evidence:
        - The paper describes the LLM-Modulo Framework in Section 3, outlining the roles of the LLM, verifiers, and the controller.
        - The workflow is described in Section 3.1.
    b) Experiment-related Evidence:
        - The paper mentions the number of back prompts used in the experiments (e.g., 15 in Section 4).
        - There is no explicit discussion of time complexity, space complexity, or potential bottlenecks.

3. **Literature Gap Analysis:**
    - While the paper cites work on automated planning, it doesn't explicitly discuss the computational complexity of integrating LLMs with symbolic verifiers.

4. **Validation Analysis:**
    - The paper focuses on the conceptual framework and its effectiveness in generating plans. It does not delve into the computational aspects of the framework. The reviewer's point about the lack of analysis of time and space complexity is valid.

5. **Conclusion:**
    - Validity status: Valid
    - Confidence level: High
    - Key supporting evidence: The paper lacks any discussion or analysis of the computational complexity of the proposed framework.

1. **Weakness Statement:** The paper does not provide a thorough evaluation of the LLM-Modulo Framework. While the authors present case studies, a more comprehensive evaluation, including comparisons with existing planning and reasoning frameworks, would be necessary to demonstrate the effectiveness and advantages of their approach. The evaluation should also consider different types of planning problems and varying levels of complexity to provide a more robust assessment of the framework's performance.

2. **Evidence Collection:**
    b) Experiment-related Evidence:
        - The paper presents two case studies: Classical Planning Domains (Section 4) and Travel Planning (Section 4).
        - In the Classical Planning Domains case study, the paper compares the performance of the LLM-Modulo Framework with a baseline (GPT-3.5-Turbo) and shows improvements with back prompting.
        - In the Travel Planning case study, the paper compares the LLM-Modulo Framework with a baseline (GPT-3.5-Turbo) and shows significant improvements.
        - The paper uses specific metrics like "Success Rate" and "Error Rate" in the experimental setup.
        - The paper does not compare against other established planning or reasoning frameworks.

3. **Literature Gap Analysis:**
    - The paper does not include comparisons with existing planning or reasoning frameworks.

4. **Validation Analysis:**
    - The paper does provide some evaluation through case studies and comparisons with a baseline. However, the reviewer's point about the lack of comparison with other established frameworks is valid. The evaluation could be more comprehensive by including a wider range of baselines and different types of planning problems.

5. **Conclusion:**
    - Validity status: Partially Valid
    - Confidence level: High
    - Key supporting evidence: The paper includes case studies and comparisons with a baseline, but lacks comparisons with other established planning or reasoning frameworks.

**Review 2 Weaknesses:**

1. **Weakness Statement:** The paper's motivation is not entirely convincing. The authors argue that LLMs cannot perform planning or self-verification independently, yet they do not provide a clear explanation of why this is a problem or how their proposed framework addresses this issue. A more detailed discussion of the inherent limitations of LLMs in planning and reasoning, and how the LLM-Modulo Framework mitigates these limitations, would strengthen the paper's motivation.

2. **Evidence Collection:** (Same as Review 1, Weakness 1)
    a) Method-related Evidence:
        - The paper states in the Introduction: "In truth, LLMs can be a genuine artificial approximate knowledge source (see Figure 1 ). Even from a pure engineering perspective, a system that takes constant time to produce the next token cannot possibly be doing principled reasoning on its own. The underlying n-gram nature makes them effortlessly intermix what would be considered disparate fields of study (not surprisingly, LLMs are seen to be very good at making/finding analogies!). The challenge is to leverage them without wrongly ascribing to them capabilities they don’t possess."
        - The paper further elaborates in Section 2: "In this section, we will first review literature that calls into question claims about the planning capabilities of LLMs ( Kambhampati et al., 2023c ; Kambhampati, 2024 ) several recent studies confirm that LLMs are not actually able to generate executable plans when they are used in autonomous modes ( Valmeekam et al., 2023c ; Liu et al., 2023 ; Silver et al., 2022 ) . For example, in ( Valmeekam et al., 2023c ; Valmeekam et al., 2023b ) , we evaluate LLMs’ ability to generate correct plans on a suite of planning problem instances based on the kinds of domains employed in the International Planning Competition ( IPC, 1998 ) . To eliminate the subjective aspect of analysis that forms the core part of many earlier efforts to evaluate the reasoning capabilities of LLMs, we leverage models and tools from the automated planning community to automate evaluation. We show that results in the autonomous mode are pretty bleak. On average, only about 12% of the plans that the best LLM (GPT-4) generates are actually executable without errors and goal-reaching. We demonstrate that the performance deteriorates further if the names of the actions and objects in the domain are obfuscated–a change that doesn’t in any way affect the performance of the standard AI planners. This further suggests that LLMs are more likely doing approximate retrieval of plans than actual planning."
        - The paper introduces the LLM-Modulo Framework in Section 3, stating: "While Section 2 questions the claims that LLMs are capable of planning/reasoning by themselves, it is certainly not meant to imply that LLMs don’t have any constructive roles to play in solving planning/reasoning tasks. On the contrary, as discussed in the Introduction, their uncanny ability to generate ideas/potential candidate solutions–albeit with no guarantees about those guesses–can be valuable in the generate-test-critique setups in conjunction with either model-based verifiers or expert humans in the loop. Accordingly, we propose a general ‘‘LLM-Modulo’’ framework 7 7 7 The name LLM-Modulo is inspired by the SAT-Modulo system ( Nieuwenhuis & Oliveras, 2006 ) . . . The LLM-Modulo framework proposed in this position paper tackles this challenge."

3. **Literature Gap Analysis:** (Same as Review 1, Weakness 1)
    a) Method-related Evidence:
        - The paper describes the LLM-Modulo Framework in Section 3, stating: "While Section 2 questions the claims that LLMs are capable of planning/reasoning by themselves, it is certainly not meant to imply that LLMs don’t have any constructive roles to play in solving planning/reasoning tasks. On the contrary, as discussed in the Introduction, their uncanny ability to generate ideas/potential candidate solutions–albeit with no guarantees about those guesses–can be valuable in the generate-test-critique setups in conjunction with either model-based verifiers or expert humans in the loop. Accordingly, we propose a general ‘‘LLM-Modulo’’ framework 7 7 7 The name LLM-Modulo is inspired by the SAT-Modulo system ( Nieuwenhuis & Oliveras, 2006 ) . . . The LLM-Modulo framework proposed in this position paper tackles this challenge."
        - The paper explains how the LLM generates candidate plans and how the symbolic components provide soundness and completeness guarantees.

4. **Validation Analysis:** (Same as Review 1, Weakness 1)
    - The paper clearly states the problem and proposes a solution, but the explanation of the negative implications of LLMs' autonomous capabilities could be more explicit.

5. **Conclusion:**
    - Validity status: Partially Valid
    - Confidence level: High
    - Key supporting evidence: The paper clearly states the problem and proposes a solution, but the explanation of the negative implications of LLMs' autonomous capabilities could be more explicit.

1. **Weakness Statement:** The paper lacks a detailed analysis of the computational complexity and efficiency of the LLM-Modulo Framework. It would be beneficial to include a discussion of the time and space complexity of the framework, as well as any potential bottlenecks or limitations in its scalability.

2. **Evidence Collection:** (Same as Review 1, Weakness 2)
    a) Method-related Evidence:
        - The paper describes the LLM-Modulo Framework in Section 3, outlining the roles of the LLM, verifiers, and the controller.
        - The workflow is described in Section 3.1.
    b) Experiment-related Evidence:
        - The paper mentions the number of back prompts used in the experiments (e.g., 15 in Section 4).
        - There is no explicit discussion of time complexity, space complexity, or potential bottlenecks.

3. **Literature Gap Analysis:**
    - While the paper cites work on automated planning, it doesn't explicitly discuss the computational complexity of integrating LLMs with symbolic verifiers.

4. **Validation Analysis:** (Same as Review 1, Weakness 2)
    - The paper focuses on the conceptual framework and its effectiveness in generating plans. It does not delve into the computational aspects of the framework. The reviewer's point about the lack of analysis of time and space complexity is valid.

5. **Conclusion:**
    - Validity status: Valid
    - Confidence level: High
    - Key supporting evidence: The paper lacks any discussion or analysis of the computational complexity of the proposed framework.

1. **Weakness Statement:** The paper does not provide a thorough evaluation of the LLM-Modulo Framework. While the authors present case studies, a more comprehensive evaluation, including comparisons with existing planning and reasoning frameworks, would be necessary to demonstrate the effectiveness and advantages of their approach. The evaluation should also consider different types of planning problems and varying levels of complexity to provide a more robust assessment of the framework's performance.

2. **Evidence Collection:** (Same as Review 1, Weakness 3)
    b) Experiment-related Evidence:
        - The paper presents two case studies: Classical Planning Domains (Section 4) and Travel Planning (Section 4).
        - In the Classical Planning Domains case study, the paper compares the performance of the LLM-Modulo Framework with a baseline (GPT-3.5-Turbo) and shows improvements with back prompting.
        - In the Travel Planning case study, the paper compares the LLM-Modulo Framework with a baseline (GPT-3.5-Turbo) and shows significant improvements.
        - The paper does not compare against other established planning or reasoning frameworks.

3. **Literature Gap Analysis:**
    - The paper does not include comparisons with existing planning or reasoning frameworks.

4. **Validation Analysis:** (Same as Review 1, Weakness 3)
    - The paper includes case studies and comparisons with a baseline. However, the reviewer's point about the lack of comparison with other established frameworks is valid. The evaluation could be more comprehensive by including a wider range of baselines and different types of planning problems.

5. **Conclusion:**
    - Validity status: Partially Valid
    - Confidence level: High
    - Key supporting evidence: The paper includes case studies and comparisons with a baseline, but lacks comparisons with other established planning or reasoning frameworks.

**Review 3 Weaknesses:**

1. **Weakness Statement:** The paper's motivation is not entirely convincing. The authors argue that LLMs cannot perform planning or self-verification independently, yet they do not provide a clear explanation of why this is a problem or how their proposed framework addresses this issue. A more detailed discussion of the limitations of LLMs in planning and reasoning, and how the LLM-Modulo Framework mitigates these limitations, would strengthen the paper's motivation.

2. **Evidence Collection:** (Same as Review 1, Weakness 1 and Review 2, Weakness 1)
    a) Method-related Evidence:
        - The paper states in the Introduction: "In truth, LLMs can be a genuine artificial approximate knowledge source (see Figure 1 ). Even from a pure engineering perspective, a system that takes constant time to produce the next token cannot possibly be doing principled reasoning on its own. The underlying n-gram nature makes them effortlessly intermix what would be considered disparate fields of study (not surprisingly, LLMs are seen to be very good at making/finding analogies!). The challenge is to leverage them without wrongly ascribing to them capabilities they don’t possess."
        - The paper further elaborates in Section 2: "In this section, we will first review literature that calls into question claims about the planning capabilities of LLMs ( Kambhampati et al., 2023c ; Kambhampati, 2024 ) several recent studies confirm that LLMs are not actually able to generate executable plans when they are used in autonomous modes ( Valmeekam et al., 2023c ; Liu et al., 2023 ; Silver et al., 2022 ) . For example, in ( Valmeekam et al., 2023c ; Valmeekam et al., 2023b ) , we evaluate LLMs’ ability to generate correct plans on a suite of planning problem instances based on the kinds of domains employed in the International Planning Competition ( IPC, 1998 ) . To eliminate the subjective aspect of analysis that forms the core part of many earlier efforts to evaluate the reasoning capabilities of LLMs, we leverage models and tools from the automated planning community to automate evaluation. We show that results in the autonomous mode are pretty bleak. On average, only about 12% of the plans that the best LLM (GPT-4) generates are actually executable without errors and goal-reaching. We demonstrate that the performance deteriorates further if the names of the actions and objects in the domain are obfuscated–a change that doesn’t in any way affect the performance of the standard AI planners. This further suggests that LLMs are more likely doing approximate retrieval of plans than actual planning."
        - The paper introduces the LLM-Modulo Framework in Section 3, stating: "While Section 2 questions the claims that LLMs are capable of planning/reasoning by themselves, it is certainly not meant to imply that LLMs don’t have any constructive roles to play in solving planning/reasoning tasks. On the contrary, as discussed in the Introduction, their uncanny ability to generate ideas/potential candidate solutions–albeit with no guarantees about those guesses–can be valuable in the generate-test-critique setups in conjunction with either model-based verifiers or expert humans in the loop. Accordingly, we propose a general ‘‘LLM-Modulo’’ framework 7 7 7 The name LLM-Modulo is inspired by the SAT-Modulo system ( Nieuwenhuis & Oliveras, 2006 ) . . . The LLM-Modulo framework proposed in this position paper tackles this challenge."

3. **Literature Gap Analysis:** (Same as Review 1, Weakness 1 and Review 2, Weakness 1)
    a) Method-related Evidence:
        - The paper describes the LLM-Modulo Framework in Section 3, stating: "While Section 2 questions the claims that LLMs are capable of planning/reasoning by themselves, it is certainly not meant to imply that LLMs don’t have any constructive roles to play in solving planning/reasoning tasks. On the contrary, as discussed in the Introduction, their uncanny ability to generate ideas/potential candidate solutions–albeit with no guarantees about those guesses–can be valuable in the generate-test-critique setups in conjunction with either model-based verifiers or expert humans in the loop. Accordingly, we propose a general ‘‘LLM-Modulo’’ framework 7 7 7 The name LLM-Modulo is inspired by the SAT-Modulo system ( Nieuwenhuis & Oliveras, 2006 ) . . . The LLM-Modulo framework proposed in this position paper tackles this challenge."
        - The paper explains how the LLM generates candidate plans and how the symbolic components provide soundness and completeness guarantees.

4. **Validation Analysis:** (Same as Review 1, Weakness 1 and Review 2, Weakness 1)
    - The paper clearly states the problem and proposes a solution, but the explanation of the negative implications of LLMs' autonomous capabilities could be more explicit.

5. **Conclusion:**
    - Validity status: Partially Valid
    - Confidence level: High
    - Key supporting evidence: The paper clearly states the problem and proposes a solution, but the explanation of the negative implications of LLMs' autonomous capabilities could be more explicit.

1. **Weakness Statement:** The paper lacks a detailed analysis of the computational complexity and efficiency of the LLM-Modulo Framework. It would be beneficial to include a discussion of the time and space complexity of the framework, as well as any potential bottlenecks or limitations in its scalability.

2. **Evidence Collection:** (Same as Review 1, Weakness 2 and Review 2, Weakness 2)
    a) Method-related Evidence:
        - The paper describes the LLM-Modulo Framework in Section 3, outlining the roles of the LLM, verifiers, and the controller.
        - The workflow is described in Section 3.1.
    b) Experiment-related Evidence:
        - The paper mentions the number of back prompts used in the experiments (e.g., 15 in Section 4).
        - There is no explicit discussion of time complexity, space complexity, or potential bottlenecks.

3. **Literature Gap Analysis:**
    - While the paper cites work on automated planning, it doesn't explicitly discuss the computational complexity of integrating LLMs with symbolic verifiers.

4. **Validation Analysis:** (Same as Review 1, Weakness 2 and Review 2, Weakness 2)
    - The paper focuses on the conceptual framework and its effectiveness in generating plans. It does not delve into the computational aspects of the framework. The reviewer's point about the lack of analysis of time and space complexity is valid.

5. **Conclusion:**
    - Validity status: Valid
    - Confidence level: High
    - Key supporting evidence: The paper lacks any discussion or analysis of the computational complexity of the proposed framework.

1. **Weakness Statement:** The paper does not provide a thorough evaluation of the LLM-Modulo Framework. While the authors present case studies, a more comprehensive evaluation, including comparisons with existing planning and reasoning frameworks, would be necessary to demonstrate the effectiveness and advantages of their approach. The evaluation should also consider different types of planning problems and varying levels of complexity to provide a more robust assessment of the framework's performance.

2. **Evidence Collection:** (Same as Review 1, Weakness 3 and Review 2, Weakness 3)
    b) Experiment-related Evidence:
        - The paper presents two case studies: Classical Planning Domains (Section 4) and Travel Planning (Section 4).
        - In the Classical Planning Domains case study, the paper compares the performance of the LLM-Modulo Framework with a baseline (GPT-3.5-Turbo) and shows improvements with back prompting.
        - In the Travel Planning case study, the paper compares the LLM-Modulo Framework with a baseline (GPT-3.5-Turbo) and shows significant improvements.
        - The paper does not compare against other established planning or reasoning frameworks.

3. **Literature Gap Analysis:**
    - The paper does not include comparisons with existing planning or reasoning frameworks.

4. **Validation Analysis:** (Same as Review 1, Weakness 3 and Review 2, Weakness 3)
    - The paper includes case studies and comparisons with a baseline. However, the reviewer's point about the lack of comparison with other established frameworks is valid. The evaluation could be more comprehensive by including a wider range of baselines and different types of planning problems.

5. **Conclusion:**
    - Validity status: Partially Valid
    - Confidence level: High
    - Key supporting evidence: The paper includes case studies and comparisons with a baseline, but lacks comparisons with other established planning or reasoning frameworks.

**Review 4 Weaknesses:**

1. **Weakness Statement:** The paper's motivation is not entirely convincing. The authors argue that LLMs cannot perform planning or self-verification independently, yet they do not provide a clear explanation of why this is a problem or how their proposed framework addresses this issue. A more detailed discussion of the inherent limitations of LLMs in planning and reasoning, and how the LLM-Modulo Framework mitigates these limitations, would strengthen the paper's motivation.

2. **Evidence Collection:** (Same as Review 1, Weakness 1, Review 2, Weakness 1, and Review 3, Weakness 1)
    a) Method-related Evidence:
        - The paper states in the Introduction: "In truth, LLMs can be a genuine artificial approximate knowledge source (see Figure 1 ). Even from a pure engineering perspective, a system that takes constant time to produce the next token cannot possibly be doing principled reasoning on its own. The underlying n-gram nature makes them effortlessly intermix what would be considered disparate fields of study (not surprisingly, LLMs are seen to be very good at making/finding analogies!). The challenge is to leverage them without wrongly ascribing to them capabilities they don’t possess."
        - The paper further elaborates in Section 2: "In this section, we will first review literature that calls into question claims about the planning capabilities of LLMs ( Kambhampati et al., 2023c ; Kambhampati, 2024 ) several recent studies confirm that LLMs are not actually able to generate executable plans when they are used in autonomous modes ( Valmeekam et al., 2023c ; Liu et al., 2023 ; Silver et al., 2022 ) . For example, in ( Valmeekam et al., 2023c ; Valmeekam et al., 2023b ) , we evaluate LLMs’ ability to generate correct plans on a suite of planning problem instances based on the kinds of domains employed in the International Planning Competition ( IPC, 1998 ) . To eliminate the subjective aspect of analysis that forms the core part of many earlier efforts to evaluate the reasoning capabilities of LLMs, we leverage models and tools from the automated planning community to automate evaluation. We show that results in the autonomous mode are pretty bleak. On average, only about 12% of the plans that the best LLM (GPT-4) generates are actually executable without errors and goal-reaching. We demonstrate that the performance deteriorates further if the names of the actions and objects in the domain are obfuscated–a change that doesn’t in any way affect the performance of the standard AI planners. This further suggests that LLMs are more likely doing approximate retrieval of plans than actual planning."
        - The paper introduces the LLM-Modulo Framework in Section 3, stating: "While Section 2 questions the claims that LLMs are capable of planning/reasoning by themselves, it is certainly not meant to imply that LLMs don’t have any constructive roles to play in solving planning/reasoning tasks. On the contrary, as discussed in the Introduction, their uncanny ability to generate ideas/potential candidate solutions–albeit with no guarantees about those guesses–can be valuable in the generate-test-critique setups in conjunction with either model-based verifiers or expert humans in the loop. Accordingly, we propose a general ‘‘LLM-Modulo’’ framework 7 7 7 The name LLM-Modulo is inspired by the SAT-Modulo system ( Nieuwenhuis & Oliveras, 2006 ) . . . The LLM-Modulo framework proposed in this position paper tackles this challenge."

3. **Literature Gap Analysis:** (Same as Review 1, Weakness 1 and Review 2, Weakness 1)
    a) Method-related Evidence:
        - The paper describes the LLM-Modulo Framework in Section 3, stating: "While Section 2 questions the claims that LLMs are capable of planning/reasoning by themselves, it is certainly not meant to imply that LLMs don’t have any constructive roles to play in solving planning/reasoning tasks. On the contrary, as discussed in the Introduction, their uncanny ability to generate ideas/potential candidate solutions–albeit with no guarantees about those guesses–can be valuable in the generate-test-critique setups in conjunction with either model-based verifiers or expert humans in the loop. Accordingly, we propose a general ‘‘LLM-Modulo’’ framework 7 7 7 The name LLM-Modulo is inspired by the SAT-Modulo system ( Nieuwenhuis & Oliveras, 2006 ) . . . The LLM-Modulo framework proposed in this position paper tackles this challenge."
        - The paper explains how the LLM generates candidate plans and how the symbolic components provide soundness and completeness guarantees.

4. **Validation Analysis:** (Same as Review 1, Weakness 1 and Review 2, Weakness 1 and Review 3, Weakness 1)
    - The paper clearly states the problem and proposes a solution, but the explanation of the negative implications of LLMs' autonomous capabilities could be more explicit.

5. **Conclusion:**
    - Validity status: Partially Valid
    - Confidence level: High
    - Key supporting evidence: The paper clearly states the problem and proposes a solution, but the explanation of the negative implications of LLMs' autonomous capabilities could be more explicit.

1. **Weakness Statement:** The paper lacks a detailed analysis of the computational complexity and efficiency of the LLM-Modulo Framework. It would be beneficial to include a discussion of the time and space complexity of the framework, as well as any potential bottlenecks or limitations in its scalability.

2. **Evidence Collection:** (Same as Review 1, Weakness 2, Review 2, Weakness 2, and Review 3, Weakness 2)
    a) Method-related Evidence:
        - The paper describes the LLM-Modulo Framework in Section 3, outlining the roles of the LLM, verifiers, and the controller.
        - The workflow is described in Section 3.1.
    b) Experiment-related Evidence:
        - The paper mentions the number of back prompts used in the experiments (e.g., 15 in Section 4).
        - There is no explicit discussion of time complexity, space complexity, or potential bottlenecks.

3. **Literature Gap Analysis:**
    - While the paper cites work on automated planning, it doesn't explicitly discuss the computational complexity of integrating LLMs with symbolic verifiers.

4. **Validation Analysis:** (Same as Review 1, Weakness 2, Review 2, Weakness 2, and Review 3, Weakness 2)
    - The paper focuses on the conceptual framework and its effectiveness in generating plans. It does not delve into the computational aspects of the framework. The reviewer's point about the lack of analysis of time and space complexity is valid.

5. **Conclusion:**
    - Validity status: Valid
    - Confidence level: High
    - Key supporting evidence: The paper lacks any discussion or analysis of the computational complexity of the proposed framework.

1. **Weakness Statement:** The paper does not provide a thorough evaluation of the LLM-Modulo Framework. While the authors present case studies, a more comprehensive evaluation, including comparisons with existing planning and reasoning frameworks, would be necessary to demonstrate the effectiveness and advantages of their approach. The evaluation should also consider different types of planning problems and varying levels of complexity to provide a more robust assessment of the framework's performance.

2. **Evidence Collection:** (Same as Review 1, Weakness 3, Review 2, Weakness 3, and Review 3, Weakness 3)
    b) Experiment-related Evidence:
        - The paper presents two case studies: Classical Planning Domains (Section 4) and Travel Planning (Section 4).
        - In the Classical Planning Domains case study, the paper compares the performance of the LLM-Modulo Framework with a baseline (GPT-3.5-Turbo) and shows improvements with back prompting.
        - In the Travel Planning case study, the paper compares the LLM-Modulo Framework with a baseline (GPT-3.5-Turbo) and shows significant improvements.
        - The paper does not compare against other established planning or reasoning frameworks.

3. **Literature Gap Analysis:**
    - The paper does not include comparisons with existing planning or reasoning frameworks.

4. **Validation Analysis:** (Same as Review 1, Weakness 3, Review 2, Weakness 3, and Review 3, Weakness 3)
    - The paper includes case studies and comparisons with a baseline. However, the reviewer's point about the lack of comparison with other established frameworks is valid. The evaluation could be more comprehensive by including a wider range of baselines and different types of planning problems.

5. **Conclusion:**
    - Validity status: Partially Valid
    - Confidence level: High
    - Key supporting evidence: The paper includes case studies and comparisons with a baseline, but lacks comparisons with other established planning or reasoning frameworks.
}

Now, I have successfully verified each review. Next, I will organize this content and output the final review decision:

\boxed_review{
## Summary:

This paper introduces the LLM-Modulo Framework, a novel approach designed to integrate the approximate reasoning capabilities of Large Language Models (LLMs) with the soundness and completeness of traditional symbolic planning methods. The authors argue that LLMs, while adept at generating candidate plans, lack the structured reasoning necessary for reliable planning, especially in complex scenarios. They propose that LLMs can serve as valuable approximate knowledge sources, generating a diverse set of candidate plans, which are then rigorously evaluated and refined by external symbolic components. This framework, termed the LLM-Modulo Framework, consists of an LLM that generates plan candidates, external symbolic components that act as verifiers, and a controller that orchestrates the interaction between the LLM and the symbolic components. The core idea is to leverage the LLM's ability to produce a wide range of potential solutions, while using symbolic components to ensure the soundness and completeness of the generated plans. The authors present case studies in classical planning domains and a recent travel planning benchmark to demonstrate the practical applicability of their framework. In these case studies, the LLM-Modulo Framework is compared against baselines, including standalone LLMs, and shows improvements in performance, particularly when using back prompts to refine the LLM's initial plan candidates. The paper's central claim is that LLMs are not suitable as standalone planners due to their lack of structured reasoning, and that the LLM-Modulo Framework provides a more robust solution by integrating LLMs with external symbolic components. The authors emphasize the potential of this framework to leverage the strengths of both LLMs and symbolic methods, leading to more effective and reliable planning systems. While the paper presents a compelling argument and demonstrates the potential of the LLM-Modulo Framework, it also acknowledges the limitations of LLMs in planning and reasoning, and the need for further research to address these limitations. The paper is well-structured, with a clear introduction, detailed methodology, and comprehensive case studies. The authors provide a thorough review of the literature, clearly identifying the limitations of LLMs in planning and reasoning tasks. The LLM-Modulo Framework is a novel approach that addresses the identified limitations, and the case studies demonstrate its practical applicability. However, the paper lacks a detailed analysis of the computational complexity and efficiency of the framework, and the evaluation could be more comprehensive by including comparisons with existing planning and reasoning frameworks. Overall, the paper makes a significant contribution to the field of AI planning and reasoning, and the LLM-Modulo Framework provides a promising direction for future research.


## Soundness:

2.5


## Presentation:

2.5


## Contribution:

2.25


## Strengths:

The paper's primary strength lies in its clear articulation of the limitations of LLMs in planning and reasoning tasks, and its proposal of a novel framework, the LLM-Modulo Framework, to address these limitations. The authors provide a comprehensive review of the literature, effectively identifying the shortcomings of LLMs in autonomous planning modes, which serves as a strong foundation for their proposed approach. The LLM-Modulo Framework is a novel and well-motivated solution that integrates LLMs with external symbolic components to leverage the strengths of both. The framework's design, which includes an LLM for candidate plan generation and external verifiers for soundness and completeness, is logically sound and well-explained. The paper's structure is also commendable, with a clear and coherent flow that effectively communicates the authors' arguments and contributions. The case studies in classical planning domains and the travel planning benchmark provide concrete examples of the framework's practical applicability and demonstrate its potential to improve planning performance. The authors also show that the LLM-Modulo Framework outperforms standalone LLM baselines, particularly when using back prompts to refine the LLM's initial plan candidates. This empirical evidence supports the authors' claim that LLMs are not suitable as standalone planners and that the LLM-Modulo Framework offers a more robust solution. The paper's focus on leveraging the approximate knowledge sources and candidate plan generation capabilities of LLMs, while using symbolic components to ensure soundness and completeness, is a significant contribution to the field. The authors also acknowledge the limitations of their approach and discuss potential challenges and future directions, which demonstrates a thorough understanding of the problem and a commitment to further research. The paper's clear writing style and well-organized structure make it easy to follow and understand, which enhances its overall impact. The authors have successfully presented a complex topic in a way that is accessible to a broad audience, and their work has the potential to inspire further research in this area.


## Weaknesses:

Despite the strengths of the paper, several weaknesses warrant attention. A primary concern is the lack of a detailed analysis of the computational complexity and efficiency of the LLM-Modulo Framework. While the paper introduces the framework and demonstrates its effectiveness through case studies, it fails to provide a thorough discussion of the time and space complexity of the framework. This omission is significant because the integration of LLMs with symbolic components could introduce substantial computational overhead, and without a detailed analysis, it is difficult to assess the practical applicability of the framework in real-world scenarios. The paper does not analyze how the framework scales with the size and complexity of the planning problems, nor does it identify any potential bottlenecks or limitations in its scalability. This lack of analysis is a significant weakness, as it leaves a critical gap in our understanding of the framework's performance. My confidence in this assessment is high, as the paper's methodology and experimental sections do not include any discussion or analysis of computational complexity. Another significant weakness is the limited evaluation of the LLM-Modulo Framework. While the authors present case studies in classical planning domains and a travel planning benchmark, the evaluation lacks comparisons with existing planning and reasoning frameworks. The paper compares the LLM-Modulo Framework with standalone LLM baselines, such as GPT-3.5-Turbo, but it does not include comparisons with other established planning or reasoning frameworks. This omission makes it difficult to assess the effectiveness and advantages of the LLM-Modulo Framework relative to existing approaches. The evaluation should have included a wider range of baselines and different types of planning problems to provide a more robust assessment of the framework's performance. My confidence in this assessment is high, as the paper's experimental sections clearly show the absence of comparisons with other established frameworks. Furthermore, the paper's motivation, while well-articulated, could be strengthened by providing a more explicit explanation of the negative consequences of LLMs' autonomous capabilities. While the authors argue that LLMs cannot perform planning or self-verification independently, they do not provide a clear explanation of why this is a problem or how their proposed framework addresses this issue. The paper could have provided more concrete examples of planning scenarios where LLMs fail due to these limitations, and how the integration of external symbolic components in the LLM-Modulo Framework mitigates these specific issues. The paper does provide some evidence of LLMs' limitations in Section 2, but the explanation of the negative implications of LLMs' autonomous capabilities could be more explicit. My confidence in this assessment is high, as the paper's introduction and Section 2 do not provide a sufficiently detailed explanation of the negative consequences of LLMs' autonomous capabilities. Finally, the paper's discussion of the LLM-Modulo Framework could be enhanced by a more detailed explanation of the specific limitations of LLMs in planning and reasoning that the framework aims to address. While the authors acknowledge that LLMs cannot perform planning or self-verification independently, they do not fully articulate how the integration of external symbolic components in the LLM-Modulo Framework mitigates these specific issues. For example, the paper could have explained how the symbolic components provide a structured environment for planning and reasoning, ensuring the soundness and completeness of the generated plans, and how they interact with the LLM to guide the planning process. My confidence in this assessment is high, as the paper's introduction and Section 3 do not provide a sufficiently detailed explanation of the specific limitations of LLMs that the framework aims to address.


## Suggestions:

To address the identified weaknesses, I recommend several concrete improvements. First, the paper should include a detailed analysis of the computational complexity and efficiency of the LLM-Modulo Framework. This analysis should consider both the time and space complexity of the framework, as well as any potential bottlenecks or limitations in its scalability. The authors should analyze how the framework scales with the size and complexity of the planning problems, and they should identify any potential computational bottlenecks or limitations in its scalability. This analysis should include a discussion of the number of LLM calls required for different planning problems, and how this number affects the overall computational cost. Furthermore, the authors should provide a more detailed discussion of the trade-offs between the expressiveness of the external symbolic components and the computational efficiency of the framework. This would help readers understand the practical implications of using the LLM-Modulo Framework in real-world applications. Second, the paper should include a more comprehensive evaluation of the LLM-Modulo Framework. This evaluation should include comparisons with existing planning and reasoning frameworks, using a variety of benchmark problems with different characteristics and complexities. The evaluation should not only focus on the success rate of the framework but also consider other metrics, such as the efficiency of the planning process, the quality of the generated plans, and the robustness of the framework to different types of errors. For instance, the authors could compare the performance of the LLM-Modulo Framework with other state-of-the-art planning algorithms on standard planning benchmarks. This would provide a more objective assessment of the framework's effectiveness and its advantages over existing approaches. Additionally, the evaluation should explore the framework's performance under different conditions, such as varying the number of LLM calls, the complexity of the symbolic components, and the quality of the initial plan candidates. This would provide a more nuanced understanding of the framework's strengths and weaknesses. Third, the paper should provide a more explicit explanation of the negative consequences of LLMs' autonomous capabilities and how the LLM-Modulo Framework addresses these limitations. The authors should provide concrete examples of planning scenarios where LLMs fail due to these limitations, and they should explain how the integration of external symbolic components in the LLM-Modulo Framework mitigates these specific issues. For example, the authors could elaborate on how the symbolic components provide a structured environment for planning and reasoning, ensuring the soundness and completeness of the generated plans, and how they interact with the LLM to guide the planning process. This would help to clarify the novelty and significance of their approach. Finally, the paper should provide a more detailed discussion of the specific limitations of LLMs in planning and reasoning that the LLM-Modulo Framework aims to address. The authors should explain how the symbolic components provide a structured environment for planning and reasoning, ensuring the soundness and completeness of the generated plans, and how they interact with the LLM to guide the planning process. This would help readers understand the specific contributions of the framework and its potential impact on the field of AI planning and reasoning.


## Questions:

Several questions arise from my analysis of the paper. First, how does the LLM-Modulo Framework handle situations where the external symbolic components are not available or are difficult to define? The paper assumes the availability of symbolic components, but it does not discuss the robustness of the framework in scenarios where these components are absent or poorly defined. Understanding how the framework behaves in such cases is crucial for assessing its practical applicability. Second, can the authors provide more details on how the LLM-Modulo Framework ensures the soundness and completeness of the generated plans? The paper mentions that the symbolic components provide a structured environment for planning and reasoning, but it does not provide a detailed explanation of the specific mechanisms used to ensure soundness and completeness. A more detailed explanation of these mechanisms would be beneficial for understanding the framework's theoretical underpinnings. Third, what are the limitations of the LLM-Modulo Framework in terms of scalability and computational efficiency? The paper does not provide a detailed analysis of the computational complexity and efficiency of the framework, and it is unclear how the framework would perform on very large or complex planning problems. Understanding the scalability and efficiency limitations of the framework is crucial for assessing its practical applicability. Fourth, how does the LLM-Modulo Framework compare to other state-of-the-art planning and reasoning frameworks in terms of performance and efficiency? The paper compares the framework with standalone LLM baselines, but it does not include comparisons with other established planning or reasoning frameworks. A more comprehensive comparison with existing frameworks would be necessary to demonstrate the effectiveness and advantages of the LLM-Modulo Framework. Finally, what are the potential ethical implications of using the LLM-Modulo Framework, such as the potential for bias or the risk of misuse? The paper does not discuss the ethical implications of using the framework, and it is important to consider these implications when evaluating the framework's potential impact. These questions highlight key uncertainties and areas for further investigation, and addressing them would significantly enhance the paper's overall contribution.


## Rating:

4.25


## Confidence:

3.25


## Decision:

Reject
}