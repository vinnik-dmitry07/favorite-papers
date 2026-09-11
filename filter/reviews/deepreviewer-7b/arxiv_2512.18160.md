I will use Standard Mode for comprehensive thinking. As a professional reviewer, I will simulate 4 different reviewers, followed by the verification thinking. Then I will output the Finally Review Output. Let me think - Standard Mode means I will output the original review, followed by the verification thinking. Considering that I am currently in standard mode, I should think from my existing knowledge and consider some related work content when writing about weaknesses. Then I will output the Finally Review Output and Meta Review Output:

\boxed_simreviewers{
## Reviewer 1

### Summary

This paper introduces Propose, Solve, Verify (PSV), a self-play framework for training LLMs to generate code that passes formal verification. The approach alternates between proposing new verification specifications, training the code generation model on verified solutions, and using the verifier to filter out incorrect solutions for subsequent rounds of training. The authors demonstrate that this iterative process leads to significant improvements in pass@1 and pass@10 metrics compared to baselines such as AlphaVerus and iterative rejection fine-tuning (RFT).

### Soundness

3

### Presentation

3

### Contribution

2

### Strengths

1. The paper is well-written and easy to follow, with clear explanations of the methodology and experimental setup.
2. The authors conduct thorough experiments to evaluate the effectiveness of the proposed approach, including ablation studies that demonstrate the importance of key components such as formal verification and difficulty-aware proposal.

### Weaknesses

#### Some Related Works


#### comment

1. The paper focuses on formal verification for code generation, which is a relatively small subset of the broader self-play literature. The approach appears to be a straightforward combination of existing techniques, such as rejection fine-tuning and self-play, and may not be sufficiently novel to justify acceptance. The core idea of using a verifier to filter solutions is not new, and the paper does not sufficiently highlight the unique challenges or insights that arise from applying this to code generation in a self-play setting. The novelty is further diminished by the fact that the method is essentially a loop of proposing, solving, and verifying, which is a common pattern in self-play.
2. The paper lacks a detailed analysis of the computational cost and scalability of the approach, particularly in comparison to other self-play methods. The iterative nature of the training process, involving multiple rounds of proposal, training, and filtering, raises concerns about the practical applicability of the method, especially for large-scale code generation tasks. The paper does not provide sufficient information on the time and resources required for each iteration, making it difficult to assess the feasibility of the approach.
3. The paper does not provide a thorough comparison to other self-play methods for code generation, particularly those that do not rely on formal verification. While the authors compare against AlphaVerus and RFT, a more comprehensive comparison with other self-play techniques would help to better contextualize the contribution of the proposed method. The lack of comparison to methods that use different self-play strategies or reward mechanisms makes it hard to determine the specific advantages of the proposed approach.

### Suggestions

The paper would benefit from a more detailed discussion of the specific challenges and insights that arise from applying self-play to code generation with formal verification. The authors should elaborate on how the formal verification process interacts with the self-play loop, and what unique difficulties this interaction presents. For example, how does the verifier's feedback influence the proposal strategy, and how does the system handle situations where the verifier rejects a large number of proposed specifications? A deeper analysis of these aspects would help to justify the novelty of the approach and highlight its specific contributions to the field. Furthermore, the authors should provide a more detailed explanation of the proposal mechanism, including how it ensures diversity in the proposed specifications and how it adapts to the evolving capabilities of the code generation model.

To address the concerns about computational cost and scalability, the authors should provide a more detailed analysis of the time and resource requirements for each iteration of the training process. This analysis should include a breakdown of the computational cost of each step, such as proposal, solving, and verification. The authors should also discuss how the computational cost scales with the size of the code generation task and the number of iterations. Furthermore, the authors should compare the computational cost of their approach to other self-play methods, providing a clear understanding of the trade-offs between performance and computational resources. This analysis would help to assess the practical applicability of the method and identify potential bottlenecks.

Finally, the paper should include a more comprehensive comparison to other self-play methods for code generation, particularly those that do not rely on formal verification. This comparison should include a discussion of the strengths and weaknesses of each approach, as well as a detailed analysis of the performance differences. The authors should also consider comparing their approach to methods that use different self-play strategies or reward mechanisms. This would help to better contextualize the contribution of the proposed method and identify areas for future research. The comparison should also include an analysis of the diversity of the generated code and the robustness of the approach to different types of code generation tasks.

### Questions

1. How does the proposed approach compare to other self-play methods for code generation, particularly those that do not rely on formal verification?
2. What is the computational cost of the proposed approach, and how does it scale with the size of the code generation task?

### Rating

5

### Confidence

4

**********

## Reviewer 2

### Summary

The paper proposes a self-play algorithm for code generation that leverages formal verification to improve the quality of the generated code. The algorithm iteratively proposes new specifications, trains the code generation model on verified solutions, and uses the verifier to filter out incorrect solutions for subsequent training rounds. The authors demonstrate that this approach outperforms existing methods on verified Rust programming tasks, with performance scaling with the number of generated questions and iterations.

### Soundness

3

### Presentation

3

### Contribution

2

### Strengths

1. The paper introduces a novel self-play algorithm that leverages formal verification to improve code generation. This approach is particularly relevant for safety-critical applications where traditional unit tests are insufficient.

2. The authors provide a thorough evaluation of their algorithm on multiple benchmarks, including Dafny2Verus, MBPP-Verified, and HumanEval-Verified. The results show that the proposed method outperforms existing approaches, such as AlphaVerus and RFT, by a significant margin.

3. The paper is well-written and easy to follow. The authors clearly explain the proposed algorithm and the experimental setup.

### Weaknesses

#### Some Related Works


#### comment

1. The paper does not provide a detailed analysis of the types of errors that the proposed method still makes. It would be helpful to understand the limitations of the approach and the types of code generation tasks that it struggles with.

2. The paper does not compare the proposed method to other self-play algorithms for code generation, such as those that use reinforcement learning or evolutionary algorithms. It would be helpful to understand how the proposed method compares to these approaches in terms of performance and computational cost.

3. The paper does not discuss the potential ethical implications of using formal verification for code generation. For example, it would be helpful to discuss the potential for using this approach to generate code that is less safe or less reliable than code generated by traditional methods.

### Suggestions

The paper would benefit from a more detailed error analysis, specifically focusing on the types of logical errors that the model still makes. For instance, does the model struggle more with certain types of control flow structures, such as nested loops or conditional statements, or does it have difficulty with specific data structures? A breakdown of errors by code length, complexity, and the specific formal verification techniques used would also be valuable. This would help to identify the specific weaknesses of the approach and guide future research. Furthermore, it would be beneficial to analyze the correlation between the formal verification metrics and the actual correctness of the generated code, as this could reveal whether the formal verification is truly capturing the relevant aspects of code quality.

In addition, the paper should include a more comprehensive comparison to other self-play algorithms for code generation. This comparison should not only focus on the final performance metrics but also on the training dynamics, such as the convergence rate and the stability of the training process. It would be useful to compare the proposed method to algorithms that use reinforcement learning, such as policy gradient methods, or evolutionary algorithms, such as genetic programming. This would help to understand the strengths and weaknesses of the proposed approach compared to other self-play techniques. Furthermore, the computational cost of each approach should be compared, as this is an important factor for practical applications. A detailed analysis of the computational resources required for each method would provide a more complete picture of their relative efficiency.

Finally, the paper should address the potential ethical implications of using formal verification for code generation. While formal verification can help to ensure the safety and reliability of code, it is important to consider the potential for misuse. For example, could this approach be used to generate code that is less safe or less reliable than code generated by traditional methods? The paper should also discuss the potential for bias in the formal verification process and how this bias could affect the generated code. A thorough discussion of these ethical considerations would help to ensure that the proposed approach is used responsibly and ethically.

### Questions

1. How does the proposed method handle cases where the formal verification system is incorrect or incomplete?

2. How does the proposed method compare to other self-play algorithms for code generation, such as those that use reinforcement learning or evolutionary algorithms?

3. What are the potential ethical implications of using formal verification for code generation?

### Rating

5

### Confidence

3

**********

## Reviewer 3

### Summary

This paper proposes a self-play framework for solving code generation problems, where the authors use formal verification as the reward signal. The authors train a code generation model and a solver model, which are used in an alternating fashion. The authors show that this method can achieve better performance on verified Rust programming tasks.

### Soundness

3

### Presentation

3

### Contribution

2

### Strengths

1. The paper is well-written and easy to follow.
2. The authors conduct extensive experiments to show the effectiveness of the proposed method.

### Weaknesses

#### Some Related Works


#### comment

1. The authors do not provide a detailed analysis of the computational cost of the proposed method, which makes it difficult to assess its practical applicability. Specifically, the paper lacks a breakdown of the time and resources required for each stage of the self-play loop, including the formal verification process, code generation, and solver training. This makes it challenging to understand the scalability of the approach and compare it with other methods.
2. The authors do not compare their method with other self-play methods for code generation, such as AlphaCode, which makes it difficult to assess the novelty and effectiveness of the proposed method. The paper should include a more comprehensive comparison with existing self-play techniques, including those that do not rely on formal verification, to better contextualize the contributions of this work.

### Suggestions

To address the lack of computational cost analysis, the authors should provide a detailed breakdown of the time and resources required for each stage of their self-play loop. This should include the time taken for code generation, formal verification, and solver training. Furthermore, the authors should analyze how these costs scale with the size of the code generation task and the number of iterations. This analysis should be presented in a clear and concise manner, possibly using tables or graphs to illustrate the computational demands of the proposed method. This would allow readers to better understand the practical applicability of the approach and compare it with other methods more effectively.

To better contextualize the contributions of this work, the authors should include a more comprehensive comparison with existing self-play methods for code generation. This should include methods that do not rely on formal verification, such as AlphaCode, to provide a broader perspective on the state-of-the-art. The comparison should not only focus on the final performance metrics but also on the training dynamics, such as the convergence rate and the stability of the training process. This would help to highlight the specific advantages and disadvantages of the proposed method compared to other approaches. The authors should also discuss the limitations of their method and identify areas for future research.

Finally, the authors should provide a more detailed explanation of the difficulty-aware proposer. While the paper mentions that the proposer is difficulty-aware, it does not fully explain how this is implemented. The authors should provide a more detailed description of the mechanism used to generate problems of varying difficulty levels. This should include a discussion of the specific criteria used to determine the difficulty of a problem and how these criteria are used to guide the proposer. This would help readers to better understand the proposed method and its potential for generating diverse and challenging code generation tasks.

### Questions

1. What is the difficulty-aware proposer? How is it implemented?
2. How does the proposed method compare with other self-play methods for code generation, such as AlphaCode?

### Rating

6

### Confidence

3

**********

## Reviewer 4

### Summary

This paper proposes Propose, Solve, Verify (PSV), a self-play framework where formal verification provides reliable correctness signals. The authors train a code generation model and a solver model that iteratively propose specifications, train the code generation model with verified solutions, and use the solver’s performance to guide the next round of problem proposal. The authors demonstrate that this approach leads to substantial improvements in pass@1 and pass@10 metrics on verified Rust programming tasks, and that performance scales with the number of generated questions and iterations.

### Soundness

3

### Presentation

3

### Contribution

3

### Strengths

- This paper proposes a novel self-play framework that leverages formal verification to improve code generation. The idea is simple yet effective, and the authors demonstrate that it leads to significant performance improvements on verified Rust programming tasks.
- The authors conduct thorough experiments to evaluate the effectiveness of the proposed approach, including ablation studies that demonstrate the importance of formal verification and difficulty-aware proposal.
- The paper is well-written and easy to follow.

### Weaknesses

#### Some Related Works


#### comment

 - The authors do not provide a detailed analysis of the computational cost of the proposed method, which makes it difficult to assess its practical applicability.
- The authors do not compare their method with other self-play methods for code generation, such as AlphaCode, which makes it difficult to assess the novelty and effectiveness of the proposed method.

### Suggestions

The paper would benefit significantly from a more thorough analysis of the computational cost associated with the proposed Propose, Solve, Verify (PSV) framework. Specifically, the authors should provide a breakdown of the time and resources required for each stage of the self-play loop, including the formal verification process, code generation, and solver training. This analysis should include a discussion of how these costs scale with the size of the code generation task and the number of iterations. For example, providing a table showing the time taken for each iteration, the number of formal verification checks performed, and the memory usage would be very helpful. Furthermore, it would be beneficial to compare the computational cost of PSV with other self-play methods, such as AlphaCode, to provide a better understanding of its practical applicability. This comparison should not only focus on the final performance metrics but also on the training dynamics, such as the convergence rate and the stability of the training process. Without this analysis, it is difficult to assess the practical feasibility of the proposed method.

To better contextualize the contributions of this work, the authors should include a more comprehensive comparison with existing self-play methods for code generation. While the paper mentions AlphaCode, a more detailed comparison is needed to highlight the specific advantages and disadvantages of PSV. This comparison should include a discussion of the different self-play strategies used by each method, such as the difficulty-aware proposal mechanism in PSV, and how these strategies impact the final performance. For example, the authors could compare the performance of PSV with AlphaCode on a range of code generation tasks, including those with varying levels of complexity. This would help to demonstrate the specific scenarios where PSV is most effective and to identify areas where further improvements are needed. Furthermore, the authors should discuss the limitations of their method and identify potential areas for future research.

Finally, the authors should provide a more detailed explanation of the difficulty-aware proposer. While the paper mentions that the proposer is difficulty-aware, it does not fully explain how this is implemented. The authors should provide a more detailed description of the mechanism used to generate problems of varying difficulty levels. This should include a discussion of the specific criteria used to determine the difficulty of a problem and how these criteria are used to guide the proposer. For example, the authors could explain how the difficulty of a problem is measured and how this measurement is used to adjust the proposal distribution. This would help readers to better understand the proposed method and its potential for generating diverse and challenging code generation tasks.

### Questions

- What is the difficulty-aware proposer? How is it implemented?

### Rating

6

### Confidence

3

**********

}

I have finished generating simulated reviews from 4 reviewers. Next, I will generate verification content for these reviews:

\boxed_verification{
The user wants me to validate weaknesses identified by reviewers for the provided paper. I need to go through each reviewer's comments and find evidence in the paper to support their claims.

**Plan:**
1. Read each reviewer's weakness.
2. Search the paper for evidence related to the weakness.
3. Categorize the evidence (method, experiment, literature).
4. Write a validation analysis for each weakness.
**Review 1 Weaknesses:**

1. Weakness Statement:
[The paper focuses on formal verification for code generation, which is a relatively small subset of the broader self-play literature. The approach appears to be a straightforward combination of existing techniques, such as rejection fine-tuning and self-play, and may not be sufficiently novel to justify acceptance. The core idea of using a verifier to filter solutions is not new, and the paper does not sufficiently highlight the unique challenges or insights that arise from applying this to code generation in a self-play setting. The novelty is further diminished by the fact that the method is essentially a loop of proposing, solving, and verifying, which is a common pattern in self-play.]

2. Evidence Collection:
a) Method-related Evidence:
   - The paper explicitly states the use of rejection fine-tuning (RFT) as a baseline and mentions it in the method section: "The solver is updated through rejection fine-tuning (RFT) ( Singh et al., 2024 ) , where the base model is fine-tuned only on verified solutions." (Section 3.1)
   - The core loop of "Propose, Solve, Verify" is described in the "method" section (Section 3).
   - The paper acknowledges the use of formal verification in the introduction: "In this setup, a proposer model generates problems for a solver model to train on, and the solver’s capabilities inform the next round of problem proposal." (Introduction) and "We introduce Propose, Solve, Verify ( PSV ), which uses formal verification to unlock a new paradigm for self-play in code generation." (Introduction).

b) Experiment-related Evidence:
   - The paper compares against RFT in the experiments (Section 4).

3. Literature Gap Analysis:
   - The paper cites Singh et al. (2024) for RFT.

4. Validation Analysis:
   - Primary evidence summary: The reviewer correctly points out that the core components (self-play loop, rejection fine-tuning) are not entirely novel. The paper itself acknowledges the use of RFT. The novelty lies in the specific application of formal verification within this self-play framework for code generation.
   - Supporting quotes: "We introduce Propose, Solve, Verify ( PSV ), which uses formal verification to unlock a new paradigm for self-play in code generation." (Introduction) highlights the claim of novelty, but the underlying techniques are acknowledged.
   - Impact assessment: The reviewer's point is valid in that the high-level approach isn't entirely new. The paper could strengthen its novelty claim by more explicitly detailing the specific challenges and insights gained from applying formal verification in this self-play context for code generation.

5. Conclusion:
   - Validity status: Partially Valid
   - Confidence level: High
   - Key supporting evidence: Explicit mention of RFT as a component and the high-level nature of the "Propose, Solve, Verify" loop.

1. Weakness Statement:
[The paper lacks a detailed analysis of the computational cost and scalability of the approach, particularly in comparison to other self-play methods. The iterative nature of the training process, involving multiple rounds of proposal, training, and filtering, raises concerns about the practical applicability of the method, especially for large-scale code generation tasks. The paper does not provide sufficient information on the time and resources required for each iteration, making it difficult to assess the feasibility of the approach.]

2. Evidence Collection:
a) Method-related Evidence:
   - The method section describes the iterative process (Section 3).

b) Experiment-related Evidence:
   - The "Implementation" subsection in the "Experiments" section mentions the hardware used: "We use the Qwen2.5-Coder-3B-Instruct model as our base because it was the strongest open-weight code model at the 3B size. We use SGLang ( Zheng et al., 2024 ) with dp-size=8 and temperature 0.8 for all inference sampling because SGLang has large efficiency gains for inference time sampling and can parallelize over multiple GPUs on the same machine easily." (Section 4).
   - The paper mentions the number of iterations in the analysis of ablation studies (Section 6.3).
   - There is no explicit mention of training time, inference time, or resource usage (e.g., memory) for each iteration or the entire process.

3. Literature Gap Analysis:
   - While the paper compares against RFT, it doesn't provide a direct computational cost comparison.

4. Validation Analysis:
   - Primary evidence summary: The reviewer is correct that the paper lacks a detailed analysis of computational cost. While hardware is mentioned, there's no breakdown of time or resource usage per iteration or overall.
   - Supporting quotes: The method description details the iterative process, highlighting the computational nature of the approach. The experimental setup mentions hardware but not computational cost.
   - Impact assessment: The lack of computational cost analysis makes it difficult to assess the practical applicability and scalability of the proposed method.

5. Conclusion:
   - Validity status: Valid
   - Confidence level: High
   - Key supporting evidence: Absence of explicit computational cost metrics in the experimental section.

1. Weakness Statement:
[The paper does not provide a thorough comparison to other self-play methods for code generation, particularly those that do not rely on formal verification. While the authors compare against AlphaVerus and RFT, a more comprehensive comparison with other self-play techniques would help to better contextualize the contribution of the proposed method. The lack of comparison to methods that use different self-play strategies or reward mechanisms makes it hard to determine the specific advantages of the proposed approach.]

2. Evidence Collection:
a) Experiment-related Evidence:
   - The paper compares against AlphaVerus (No treefinement version) and RFT (Section 4).
   - There is no comparison with other self-play methods for code generation that do not use formal verification.

3. Literature Gap Analysis:
   - The related work section mentions self-play reasoning systems in general (Section 2), but the experimental section doesn't include comparisons with methods outside the formal verification domain.

4. Validation Analysis:
   - Primary evidence summary: The reviewer is correct. The experimental section primarily compares against methods within the formal verification domain.
   - Supporting quotes: The "Baselines" subsection in the "Experiments" section lists only AlphaVerus and RFT.
   - Impact assessment: The lack of comparison with other self-play methods makes it harder to understand the specific advantages of PSV compared to the broader landscape of self-play techniques.

5. Conclusion:
   - Validity status: Valid
   - Confidence level: High
   - Key supporting evidence: The limited set of baselines in the experimental section.

**Review 2 Weaknesses:**

1. Weakness Statement:
[The authors do not provide a detailed analysis of the types of errors that the proposed method still makes. It would be helpful to understand the limitations of the approach and the types of code generation tasks that it struggles with.]

2. Evidence Collection:
a) Experiment-related Evidence:
   - The paper reports pass@k metrics, which indicate the success rate on the top-k generated solutions.
   - The paper does not provide a detailed breakdown of the types of errors made (e.g., logical errors, syntax errors, edge cases not covered by the verifier).

3. Literature Gap Analysis:
   - Not applicable here.

4. Validation Analysis:
   - Primary evidence summary: The reviewer is correct. The paper focuses on overall pass rates but doesn't delve into the specific types of errors.
   - Supporting quotes: The "Metrics" subsection in the "Experiments" section states: "We measure Pass@ k k metric ( Chen et al., 2021 ) : for n n samples and c c verified successes, pass@ k = 1 − ( n − c k ) / ( n k ) k=1-\binom{n-c}{k}/\binom{n}{k} k=1−(n−c choose k)/ (n choose k) . We measure Pass@1, 5, and 10, and run our final evaluation with n = 100 to provide a strong unbiased estimate of the evaluation metrics." This focuses on the number of verified solutions.
   - Impact assessment: Understanding the types of errors would provide valuable insights into the limitations of the approach.

5. Conclusion:
   - Validity status: Valid
   - Confidence level: High
   - Key supporting evidence: The metrics used focus on overall success rate rather than error types.

1. Weakness Statement:
[The paper does not compare the proposed method to other self-play algorithms for code generation, such as those that use reinforcement learning or evolutionary algorithms. It would be helpful to understand how the proposed method compares to these approaches in terms of performance and computational cost.]

2. Evidence Collection:
a) Experiment-related Evidence:
   - The paper compares against AlphaVerus (a treefinement-based method, which can be seen as a form of RL) and RFT (a rejection fine-tuning method, which can be seen as a form of supervised learning).
   - The paper does not explicitly compare against evolutionary algorithms for code generation.

3. Literature Gap Analysis:
   - The related work section mentions self-play reasoning systems in general, but the experimental section doesn't include comparisons with methods outside the formal verification domain.

4. Validation Analysis:
   - Primary evidence summary: The reviewer is partially correct. The paper compares against a method that uses treefinement (related to RL) and rejection fine-tuning (related to supervised learning). However, it doesn't explicitly compare against other self-play algorithms specifically categorized as using reinforcement learning or evolutionary algorithms.
   - Supporting quotes: The "Baselines" subsection lists AlphaVerus and RFT. The descriptions of AlphaVerus and RFT in the "Related Work" section provide some context on their methodologies.
   - Impact assessment: A more explicit comparison against a broader range of self-play methods would provide a more comprehensive understanding of PSV's strengths and weaknesses.

5. Conclusion:
   - Validity status: Partially Valid
   - Confidence level: Medium
   - Key supporting evidence: Comparison against AlphaVerus and RFT, but no explicit comparison against other RL or evolutionary self-play methods.

1. Weakness Statement:
[The paper does not discuss the potential ethical implications of using formal verification for code generation. For example, it would be helpful to discuss the potential for using this approach to generate code that is less safe or less reliable than code generated by traditional methods.]

2. Evidence Collection:
a) Method-related Evidence:
   - The paper focuses on the technical aspects of the method and its performance.

3. Literature Gap Analysis:
   - Not applicable here.

4. Validation Analysis:
   - Primary evidence summary: The reviewer is correct. The paper does not include a discussion of the ethical implications.
   - Supporting quotes: The paper's focus is on the technical contribution and experimental results.
   - Impact assessment: Discussing ethical implications is important for responsible research, especially in safety-critical domains.

5. Conclusion:
   - Validity status: Valid
   - Confidence level: High
   - Key supporting evidence: Absence of any discussion on ethical implications in the paper.

**Review 3 Weaknesses:**

1. Weakness Statement:
[The authors do not provide a detailed analysis of the computational cost of the proposed method, which makes it difficult to assess its practical applicability. Specifically, the paper lacks a breakdown of the time and resources required for each stage of the self-play loop, including the formal verification process, code generation, and solver training. This makes it challenging to understand the scalability of the approach and compare it with other methods.]

2. Evidence Collection:
    - This is the same weakness as identified by Reviewer 1. Please see the analysis for Reviewer 1's first weakness.

3. Literature Gap Analysis:
    - Same as Reviewer 1.

4. Validation Analysis:
    - Same as Reviewer 1.

5. Conclusion:
    - Validity status: Valid
    - Confidence level: High
    - Key supporting evidence: Absence of explicit computational cost metrics in the experimental section.

1. Weakness Statement:
[The authors do not compare their method with other self-play methods for code generation, such as AlphaCode, which makes it difficult to assess the novelty and effectiveness of the proposed method. The paper should include a more comprehensive comparison with existing self-play techniques, including those that do not rely on formal verification, to better contextualize the contributions of this work.]

2. Evidence Collection:
    - This is the same weakness as identified by Reviewer 1 regarding the lack of comparison with other self-play methods. Please see the analysis for Reviewer 1's second weakness.

3. Literature Gap Analysis:
    - Same as Reviewer 1.

4. Validation Analysis:
    - Same as Reviewer 1.

5. Conclusion:
    - Validity status: Valid
    - Confidence level: High
    - Key supporting evidence: The limited set of baselines in the experimental section.

**Review 4 Weaknesses:**

1. Weakness Statement:
[The authors do not provide a detailed analysis of the types of errors that the proposed method still makes. It would be helpful to understand the limitations of the approach and the types of code generation tasks that it struggles with.]

2. Evidence Collection:
    - This is the same weakness as identified by Reviewer 2. Please see the analysis for Reviewer 2's first weakness.

3. Literature Gap Analysis:
    - Same as Reviewer 2.

4. Validation Analysis:
    - Same as Reviewer 2.

5. Conclusion:
    - Validity status: Valid
    - Confidence level: High
    - Key supporting evidence: The metrics used focus on overall success rate rather than error types.

1. Weakness Statement:
[The authors do not compare their method with other self-play algorithms for code generation, such as AlphaCode, which makes it difficult to assess the novelty and effectiveness of the proposed method. The paper should include a more comprehensive comparison with existing self-play techniques for code generation, particularly those that do not rely on formal verification, to better contextualize the contribution of the proposed method.]

2. Evidence Collection:
    - This is the same weakness as identified by Reviewer 2 regarding the lack of comparison with other self-play methods. Please see the analysis for Reviewer 2's second weakness.

3. Literature Gap Analysis:
    - Same as Reviewer 2.

4. Validation Analysis:
    - Same as Reviewer 2.

5. Conclusion:
    - Validity status: Valid
    - Confidence level: High
    - Key supporting evidence: The limited set of baselines in the experimental section.

1. Weakness Statement:
[Finally, the authors should provide a more detailed explanation of the difficulty-aware proposer. While the paper mentions that the proposer is difficulty-aware, it does not fully explain how this is implemented. The authors should provide a more detailed description of the mechanism used to generate problems of varying difficulty levels. This should include a discussion of the specific criteria used to determine the difficulty of a problem and how these criteria are used to guide the proposer. This would help readers to better understand the proposed method and its potential for generating diverse and challenging code generation tasks.]

2. Evidence Collection:
a) Method-related Evidence:
   - The paper describes the difficulty-aware proposer in the "Proposing" subsection of the "method" section: "We categorize problems into one of four classes based on r i , t r i = { Easy , Medium , Hard , and Impossible : difficulty ( x i , t ) = { Easy if ​ r i , t ≥ τ E Medium if ​ τ M ≤ r i , t < τ E Hard if ​ 0 < r i , t < τ M Impossible if ​ r i , t = 0 . We then sample k p ​ problems from D t to use as examples and ask the proposer to output a question at a target difficulty level." (Section 3.1).
   - The paper provides the specific thresholds used for difficulty levels: "We set τ M = 0.2, similar to Dong and Ma (2025) (who used 0.25), and set τ E = 0.8. We set k p ​ = 12 and use uniform input and output targets, meaning that we populate the proposer prompt with 3 problems for each difficulty class, and ask for B / 4 B/4 problems of each difficulty class as the output." (Section 3.1).
   - The paper does not explicitly detail the criteria used to determine the *initial* difficulty of the problems in the dataset or how the proposer uses these criteria to generate new problems of varying difficulty.

3. Literature Gap Analysis:
   - The paper cites Dong and Ma (2025) for the difficulty thresholds.

4. Validation Analysis:
   - Primary evidence summary: The reviewer is correct that the paper explains *how* the proposer is difficulty-aware (by sampling from different difficulty classes and asking for outputs at a target difficulty), but it doesn't fully explain the underlying mechanism for *generating* problems of varying difficulty levels. The paper relies on the initial dataset having problems of different difficulties, which are then used to guide the proposer.
   - Supporting quotes: The description of the difficulty-aware proposer explains the sampling and output target mechanism. The description of the proposer prompt mentions sampling from different difficulty classes.
   - Impact assessment: A clearer explanation of how the proposer learns to generate problems of varying difficulty would improve the understanding of the method.

5. Conclusion:
   - Validity status: Partially Valid
   - Confidence level: Medium
   - Key supporting evidence: The paper explains the sampling mechanism but not the underlying generation process of difficulty levels.
}

Now, I have successfully verified each review. Next, I will organize this content and output the final review decision:

\boxed_review{
## Summary:

This paper introduces Propose, Solve, Verify (PSV), a novel self-play framework for training code generation models, particularly in the context of formal verification. The core idea revolves around iteratively proposing new specifications, training a code generation model on verified solutions, and using the verifier's performance to guide the next round of problem proposal. The authors leverage formal verification as a reliable correctness signal, which is a departure from traditional self-play methods that might rely on less robust evaluation metrics. The proposed method involves three key components: a proposer model that generates code specifications, a solver model that generates code based on these specifications, and a verifier that checks the correctness of the generated code. The training process is iterative, with the verifier's performance used to adjust the difficulty of the proposed specifications. The authors demonstrate the effectiveness of PSV on verified Rust programming tasks, showing significant improvements in pass@1 and pass@10 metrics compared to existing approaches such as AlphaVerus and iterative rejection fine-tuning (RFT). The empirical results highlight the importance of formal verification and difficulty-aware proposal mechanisms in achieving these performance gains. The paper's main contribution lies in its novel application of formal verification within a self-play framework for code generation, which addresses the limitations of traditional methods that often suffer from error propagation and reward hacking. The authors also provide ablation studies that demonstrate the importance of formal verification and difficulty-aware proposal mechanisms. The paper is well-written and easy to follow, making it accessible to a broad audience. However, the paper also has some limitations, particularly in its analysis of computational costs and comparisons to other self-play methods. Despite these limitations, the paper presents a significant contribution to the field of code generation and formal verification, offering a promising approach for training more reliable and robust code generation models.


## Soundness:

3.0


## Presentation:

3.0


## Contribution:

2.25


## Strengths:

I found several aspects of this paper to be particularly strong. First, the introduction of PSV as a self-play framework that leverages formal verification is a novel and significant contribution. The idea of using a verifier to filter out incorrect solutions and guide the proposal of new specifications is a clever approach that addresses the limitations of traditional self-play methods. The authors clearly articulate the motivation for their approach, highlighting the shortcomings of existing methods that rely on less robust evaluation metrics. The paper is also well-written and easy to follow, making it accessible to a broad audience. The authors provide a clear explanation of the proposed method, including the roles of the proposer, solver, and verifier models. The experimental setup is also well-described, and the results are presented in a clear and concise manner. The empirical results are compelling, demonstrating that PSV outperforms existing approaches such as AlphaVerus and RFT on verified Rust programming tasks. The authors also provide ablation studies that demonstrate the importance of formal verification and difficulty-aware proposal mechanisms. These studies provide valuable insights into the inner workings of the proposed method and help to justify the design choices. The paper's focus on formal verification is particularly relevant for safety-critical applications, where reliability is paramount. The authors have successfully demonstrated the potential of using formal verification to train more reliable code generation models. The paper also provides a thorough evaluation of the proposed method, including comparisons to relevant baselines and ablation studies that demonstrate the importance of key components. The authors have also made an effort to address the limitations of their approach, such as the computational cost of formal verification, although this is not fully explored. Overall, I believe that this paper makes a significant contribution to the field of code generation and formal verification, offering a promising approach for training more reliable and robust code generation models.


## Weaknesses:

Despite the strengths of this paper, I have identified several weaknesses that warrant further consideration. First, while the paper introduces a novel self-play framework, the core components of the method, such as rejection fine-tuning (RFT) and the self-play loop, are not entirely new. As the authors themselves acknowledge, the method builds upon existing techniques, and the novelty lies primarily in the application of formal verification within this self-play context for code generation. The paper does not sufficiently highlight the unique challenges and insights that arise from applying formal verification in this specific setting. The core idea of using a verifier to filter solutions is not new, and the paper could strengthen its novelty claim by more explicitly detailing the specific challenges and insights gained from applying formal verification in this self-play context for code generation. The paper also lacks a detailed analysis of the computational cost and scalability of the proposed approach. The iterative nature of the training process, involving multiple rounds of proposal, training, and filtering, raises concerns about the practical applicability of the method, especially for large-scale code generation tasks. The paper does not provide sufficient information on the time and resources required for each iteration, making it difficult to assess the feasibility of the approach. While the hardware used is mentioned, there is no breakdown of time or resource usage per iteration or overall. This lack of computational cost analysis makes it difficult to assess the practical applicability and scalability of the proposed method. Furthermore, the paper does not provide a thorough comparison to other self-play methods for code generation, particularly those that do not rely on formal verification. While the paper compares against AlphaVerus and RFT, a more comprehensive comparison with other self-play techniques would help to better contextualize the contribution of the proposed method. The lack of comparison to methods that use different self-play strategies or reward mechanisms makes it hard to determine the specific advantages of the proposed approach. The paper also does not provide a detailed analysis of the types of errors that the proposed method still makes. It would be helpful to understand the limitations of the approach and the types of code generation tasks that it struggles with. The paper focuses on overall pass rates but doesn't delve into the specific types of errors. Understanding the types of errors would provide valuable insights into the limitations of the approach. The paper also does not discuss the potential ethical implications of using formal verification for code generation. For example, it would be helpful to discuss the potential for using this approach to generate code that is less safe or less reliable than code generated by traditional methods. The paper's focus is on the technical contribution and experimental results, and it does not address the ethical implications. Finally, while the paper mentions that the proposer is difficulty-aware, it does not fully explain how this is implemented. The paper explains *how* the proposer is difficulty-aware (by sampling from different difficulty classes and asking for outputs at a target difficulty), but it doesn't fully explain the underlying mechanism for *generating* problems of varying difficulty levels. The paper relies on the initial dataset having problems of different difficulties, which are then used to guide the proposer. A clearer explanation of how the proposer learns to generate problems of varying difficulty would improve the understanding of the method. These weaknesses, while not invalidating the paper's contributions, do highlight areas where further research and analysis are needed.


## Suggestions:

To address the identified weaknesses, I recommend several concrete improvements. First, the authors should provide a more detailed discussion of the specific challenges and insights that arise from applying formal verification in the self-play context for code generation. This discussion should elaborate on how the formal verification process interacts with the self-play loop, and what unique difficulties this interaction presents. For example, how does the verifier's feedback influence the proposal strategy, and how does the system handle situations where the verifier rejects a large number of proposed specifications? A deeper analysis of these aspects would help to justify the novelty of the approach and highlight its specific contributions to the field. Furthermore, the authors should provide a more detailed explanation of the proposal mechanism, including how it ensures diversity in the proposed specifications and how it adapts to the evolving capabilities of the code generation model. Second, the authors should include a more comprehensive analysis of the time and resource requirements for each stage of the self-play loop. This analysis should include a breakdown of the computational cost of each step, such as proposal, solving, and verification. The authors should also discuss how these costs scale with the size of the code generation task and the number of iterations. Furthermore, it would be beneficial to compare the computational cost of PSV with other self-play methods, providing a clear understanding of the trade-offs between performance and computational resources. This analysis would help to assess the practical applicability of the method and identify potential bottlenecks. Third, the paper should include a more comprehensive comparison to other self-play methods for code generation, particularly those that do not rely on formal verification. This comparison should not only focus on the final performance metrics but also on the training dynamics, such as the convergence rate and the stability of the training process. This would help to highlight the specific advantages and disadvantages of the proposed method compared to other approaches. The authors should also discuss the limitations of their method and identify areas for future research. Fourth, the authors should provide a more detailed error analysis, specifically focusing on the types of logical errors that the model still makes. For instance, does the model struggle more with certain types of control flow structures, such as nested loops or conditional statements, or does it have difficulty with specific data structures? A breakdown of errors by code length, complexity, and the specific formal verification techniques used would also be valuable. This would help to identify the specific weaknesses of the approach and guide future research. Furthermore, it would be beneficial to analyze the correlation between the formal verification metrics and the actual correctness of the generated code, as this could reveal whether the formal verification is truly capturing the relevant aspects of code quality. Fifth, the authors should address the potential ethical implications of using formal verification for code generation. While formal verification can help to ensure the safety and reliability of code, it is important to consider the potential for misuse. For example, could this approach be used to generate code that is less safe or less reliable than code generated by traditional methods? The paper should also discuss the potential for bias in the formal verification process and how this bias could affect the generated code. A thorough discussion of these ethical considerations would help to ensure that the proposed approach is used responsibly and ethically. Finally, the authors should provide a more detailed explanation of the difficulty-aware proposer. While the paper mentions that the proposer is difficulty-aware, it does not fully explain how this is implemented. The authors should provide a more detailed description of the mechanism used to generate problems of varying difficulty levels. This should include a discussion of the specific criteria used to determine the difficulty of a problem and how these criteria are used to guide the proposer. This would help readers to better understand the proposed method and its potential for generating diverse and challenging code generation tasks.


## Questions:

Based on my analysis, I have several questions that I believe would be valuable to address. First, how does the proposed approach compare to other self-play methods for code generation, such as those that use reinforcement learning or evolutionary algorithms, particularly in terms of performance and computational cost? While the paper compares against AlphaVerus and RFT, a more comprehensive comparison would help to better contextualize the contribution of the proposed method. Second, what is the computational cost of the proposed approach, and how does it scale with the size of the code generation task and the number of iterations? A detailed breakdown of the time and resource requirements for each stage of the self-play loop would be very helpful in assessing the practical applicability of the method. Third, what are the specific criteria used to determine the difficulty of a problem, and how does the proposer use these criteria to generate new problems of varying difficulty levels? The paper explains *how* the proposer is difficulty-aware, but it doesn't fully explain the underlying mechanism for *generating* problems of varying difficulty. Fourth, what are the specific types of errors that the proposed method still makes, and what are the limitations of the approach in terms of code generation tasks that it struggles with? A more detailed error analysis would provide valuable insights into the limitations of the approach and guide future research. Finally, what are the potential ethical implications of using formal verification for code generation, and how can these implications be addressed to ensure responsible and ethical use of the proposed approach? A thorough discussion of these ethical considerations would help to ensure that the proposed approach is used responsibly and ethically. Addressing these questions would further strengthen the paper and provide a more comprehensive understanding of the proposed method.


## Rating:

5.5


## Confidence:

3.25


## Decision:

Reject
}