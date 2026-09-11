I will use Standard Mode for comprehensive thinking. As a professional reviewer, I will simulate 4 different reviewers, followed by the verification thinking. Then I will output the Finally Review Output. Let me think - Standard Mode means I will output the original review, followed by the verification thinking. Considering that I am currently in standard mode, I should think from my existing knowledge and consider some related work content when writing about weaknesses. Then I will output the Finally Review Output and Meta Review Output:

\boxed_simreviewers{
## Reviewer 1

### Summary

The paper proposes a novel method for improving the accuracy of large language models (LLMs) in reasoning tasks by utilizing a reliability signal called "prefix consistency." This signal measures how often the initial answer to a reasoning task is reproduced when the model is given a partial reasoning (prefix) and regenerates the full reasoning from that point. The authors use this signal to weight the votes of different Chain-of-Thought (CoT) traces, a technique known as Weighted Majority Voting (WMV). The proposed method, called PC-WMV, is tested across various reasoning models and datasets, demonstrating that it outperforms existing WMV baselines in terms of correctness prediction and cost efficiency. The paper also shows that PC-WMV is more effective than adaptive-stopping methods on the most challenging problems, where the correct answer is less likely to be found by chance.

### Soundness

3

### Presentation

3

### Contribution

2

### Strengths

1. The paper introduces a novel and intuitive method for improving the accuracy of LLMs in reasoning tasks by leveraging prefix consistency as a reliability signal for WMV.
2. The paper is well-written and easy to follow, with clear explanations of the proposed method and its advantages over existing approaches.
3. The paper provides a comprehensive evaluation of the proposed method across various reasoning models and datasets, demonstrating its effectiveness and robustness.

### Weaknesses

#### Some Related Works


#### comment

1. The paper does not provide a detailed analysis of the computational cost of the proposed method, especially in comparison to other WMV baselines. This is important for assessing the practicality of the approach in real-world applications.
2. The paper does not explore the limitations of the proposed method, such as cases where prefix consistency may fail to accurately predict the correctness of a reasoning trace. Understanding these limitations is crucial for determining the applicability of the method in different contexts.
3. The paper could benefit from a more thorough comparison with other state-of-the-art methods for improving the accuracy of LLMs in reasoning tasks, such as self-consistency and other forms of test-time augmentation.

### Suggestions

The paper should include a more detailed analysis of the computational overhead associated with the proposed prefix consistency method. While the authors mention the method is efficient, a quantitative comparison of the time and resources required for prefix regeneration and consistency calculation against other WMV baselines would be beneficial. This should include not only the token generation costs but also the computational cost of the regeneration process itself, especially for longer reasoning chains. Furthermore, the analysis should consider the impact of different hyperparameter settings on the computational cost, such as the length of the prefix used for regeneration and the number of regeneration attempts. This would provide a more complete picture of the practical trade-offs involved in using the proposed method.

To address the limitations of the proposed method, the authors should investigate scenarios where prefix consistency might fail to accurately predict the correctness of a reasoning trace. For example, it would be useful to explore cases where the model generates a correct answer but fails to reproduce it during regeneration, or vice versa. This could involve analyzing the types of errors that occur during regeneration and how they relate to the correctness of the initial answer. Additionally, the authors should explore the sensitivity of the method to different hyperparameters, such as the threshold for considering a regeneration as successful. Understanding these limitations is crucial for determining the applicability of the method in different contexts and for identifying potential areas for improvement. The paper should also discuss the potential for combining prefix consistency with other reliability signals to improve the robustness of the method.

Finally, the paper should include a more thorough comparison with other state-of-the-art methods for improving the accuracy of LLMs in reasoning tasks. While the authors compare against some baselines, a more comprehensive comparison with methods such as self-consistency, which is a widely used approach for improving the reliability of LLMs, would be valuable. This comparison should not only focus on the final accuracy but also on other aspects such as computational cost, robustness to different types of reasoning tasks, and sensitivity to hyperparameter settings. The authors should also consider comparing against other test-time augmentation techniques that have been proposed for improving the accuracy of LLMs in reasoning tasks. This would provide a more complete picture of the strengths and weaknesses of the proposed method relative to the current state-of-the-art.

### Questions

1. How does the computational cost of the proposed method compare to other WMV baselines, and how does it scale with the length of the reasoning chain?
2. Are there specific types of reasoning tasks or problems where the proposed method is less effective, and if so, why?
3. How does the proposed method compare to other state-of-the-art methods for improving the accuracy of LLMs in reasoning tasks, such as self-consistency and other forms of test-time augmentation?

### Rating

5

### Confidence

4

**********

## Reviewer 2

### Summary

This paper introduces a novel method to improve the accuracy of reasoning in large language models (LLMs) by leveraging a new reliability signal called "prefix consistency." The authors propose a Weighted Majority Voting (WMV) technique that utilizes this prefix consistency to reweight the votes of different Chain-of-Thought (CoT) traces. The method is tested across five reasoning models and four math and science benchmarks, demonstrating superior correctness prediction and cost efficiency compared to existing WMV baselines. The paper also highlights the effectiveness of PC-WMV on the most challenging problems, where Standard MV often fails.

### Soundness

3

### Presentation

3

### Contribution

2

### Strengths

1. The paper introduces a novel reliability signal, "prefix consistency," which is a unique and innovative approach to improving the accuracy of reasoning in LLMs.
2. The proposed Weighted Majority Voting (WMV) technique is well-motivated and theoretically sound, providing a clear framework for reweighting votes based on prefix consistency.
3. The paper is well-written and easy to follow, with clear explanations of the proposed method and its advantages over existing approaches.
4. The experimental results are comprehensive, covering five reasoning models and four math and science benchmarks, demonstrating the effectiveness of PC-WMV across different settings.

### Weaknesses

#### Some Related Works


#### comment

1. While the paper demonstrates the effectiveness of PC-WMV on math and science benchmarks, it would be beneficial to explore its performance on other types of reasoning tasks, such as commonsense reasoning or logical inference, to assess its generalizability.
2. The paper could benefit from a more detailed analysis of the computational cost associated with generating and evaluating the prefix consistency scores, especially for longer reasoning chains. This would help to understand the practical implications of using PC-WMV in resource-constrained environments.
3. The paper primarily compares PC-WMV with other WMV baselines. It would be valuable to include comparisons with other state-of-the-art methods for improving the accuracy of reasoning in LLMs, such as self-consistency or other forms of test-time augmentation.

### Suggestions

The paper introduces an interesting approach using prefix consistency for reweighting Chain-of-Thought (CoT) traces, but its evaluation is limited to math and science benchmarks. To strengthen the paper, it is crucial to investigate the method's performance on other reasoning tasks, such as commonsense reasoning or logical inference. These tasks often involve different types of reasoning steps and knowledge requirements, and it is important to understand whether the prefix consistency signal remains effective in these contexts. For example, in commonsense reasoning, the reasoning steps might rely on implicit knowledge and common-sense understanding, which are not directly captured by the prefix consistency signal derived from math and science problems. Therefore, it would be beneficial to include experiments on datasets like the Winograd Schema Challenge or similar benchmarks to assess the generalizability of the proposed method. Furthermore, analyzing the types of errors made by the model on these different tasks could provide insights into the limitations of the prefix consistency signal and suggest potential improvements.

Another area that requires further investigation is the computational cost of the proposed method. While the paper mentions the efficiency of the approach, a more detailed analysis of the time and memory requirements for generating and evaluating prefix consistency scores is needed, especially for longer reasoning chains. The computational overhead could become a significant bottleneck in resource-constrained environments or when dealing with very long reasoning sequences. It would be helpful to provide a breakdown of the computational cost associated with each step of the PC-WMV method, including the time taken to generate the prefix, regenerate the full chain, and evaluate the consistency score. Additionally, exploring techniques to optimize the computation of prefix consistency, such as caching intermediate results or using more efficient algorithms, could be beneficial. A thorough analysis of the computational trade-offs would help to understand the practical applicability of the method in different scenarios.

Finally, the paper should include comparisons with other state-of-the-art methods for improving the accuracy of reasoning in LLMs. While the paper compares PC-WMV with other Weighted Majority Voting (WMV) baselines, it would be valuable to include comparisons with methods such as self-consistency or other forms of test-time augmentation. These methods have shown promising results in improving the accuracy of LLMs, and comparing PC-WMV with them would provide a more comprehensive evaluation of its effectiveness. For example, self-consistency involves generating multiple reasoning chains and selecting the answer that is consistent across the majority of them. Comparing PC-WMV with self-consistency would help to understand whether the proposed method offers a significant advantage over existing techniques or if it is complementary to them. Furthermore, exploring the combination of PC-WMV with other techniques could also be a promising direction for future research.

### Questions

1. How does the performance of PC-WMV vary across different types of reasoning tasks, and are there specific scenarios where it excels or struggles?
2. What is the computational cost of generating and evaluating prefix consistency scores, especially for longer reasoning chains, and how does it compare to other WMV baselines?
3. How does PC-WMV compare with other state-of-the-art methods for improving the accuracy of reasoning in LLMs, such as self-consistency or other forms of test-time augmentation?

### Rating

6

### Confidence

4

**********

## Reviewer 3

### Summary

This paper introduces a novel approach to improve the accuracy of LLMs in reasoning tasks by utilizing a reliability signal called "prefix consistency." The authors propose a Weighted Majority Voting (WMV) method that leverages this signal to reweight votes from different Chain-of-Thought (CoT) traces. The paper demonstrates that this method outperforms existing WMV baselines in terms of correctness prediction and cost efficiency across various reasoning models and datasets.

### Soundness

3

### Presentation

3

### Contribution

3

### Strengths

1. The paper introduces a novel reliability signal, "prefix consistency," that effectively measures the reproducibility of correct answers under regeneration, providing a new way to assess the reliability of LLMs in reasoning tasks.

2. The proposed Weighted Majority Voting (WMV) method is theoretically sound and empirically validated, showing significant improvements in correctness prediction and cost efficiency compared to existing WMV baselines.

3. The paper is well-structured and clearly written, making it easy to follow and understand the proposed method and its advantages.

### Weaknesses

#### Some Related Works


#### comment

1. The paper could benefit from a more detailed discussion of the limitations of the proposed method, such as scenarios where prefix consistency may fail to accurately predict the correctness of a reasoning trace. For example, the method's reliance on the regeneration of CoT traces might be computationally expensive for very long or complex reasoning chains, and the paper does not explore the potential for error propagation during this regeneration process. Furthermore, the method's performance might be sensitive to the choice of the prefix fraction, and the paper does not provide a clear guideline on how to select this hyperparameter optimally across different tasks and datasets.

2. While the paper compares the proposed method with several baselines, it could be strengthened by including a broader range of state-of-the-art methods for improving the accuracy of LLMs in reasoning tasks. For instance, the paper does not compare against methods that use self-consistency or other forms of test-time augmentation, which are known to be effective in improving the reliability of LLM outputs. A more comprehensive comparison would provide a better understanding of the relative strengths and weaknesses of the proposed method.

### Suggestions

The authors should provide a more thorough analysis of the scenarios where the prefix consistency signal might fail. Specifically, they should investigate cases where the model generates a correct answer but fails to reproduce it during regeneration, or vice versa. This analysis should include a discussion of the types of reasoning errors that are more likely to be missed by the prefix consistency signal, and how these errors might affect the overall performance of the proposed method. Furthermore, the authors should explore the computational cost of the regeneration process in more detail, and provide guidelines for selecting the optimal prefix fraction for different tasks and datasets. This could involve a sensitivity analysis of the method's performance with respect to the prefix fraction, and a discussion of the trade-offs between computational cost and accuracy.

To strengthen the paper's evaluation, the authors should include a more comprehensive comparison with state-of-the-art methods for improving the accuracy of LLMs in reasoning tasks. This should include methods such as self-consistency, which generates multiple reasoning chains and selects the answer that is consistent across the majority of them. The authors should also consider comparing against other test-time augmentation techniques, such as adversarial examples or data augmentation methods. This would provide a more complete picture of the relative strengths and weaknesses of the proposed method, and help to identify the specific scenarios where it is most effective. The comparison should not only focus on the final accuracy but also on other metrics such as computational cost and robustness to different types of reasoning errors.

Finally, the authors should provide more details on the implementation of the proposed method, including the specific prompts used for regeneration and the criteria for selecting the final answer. This would allow other researchers to reproduce the results and build upon the proposed method. The authors should also discuss the limitations of the proposed method in more detail, and suggest potential directions for future research. This could include exploring alternative reliability signals, or combining the proposed method with other techniques for improving the accuracy of LLMs in reasoning tasks.

### Questions

1. How does the proposed method perform on tasks that require common-sense reasoning or multi-hop inference, where the reasoning steps may not be as clearly defined as in math or science problems?

2. Can the prefix consistency signal be adapted to other types of reasoning tasks, such as natural language inference or planning?

3. How sensitive is the proposed method to the choice of the prefix fraction, and what guidelines can be provided for selecting the optimal value for different tasks and datasets?

### Rating

6

### Confidence

3

**********

## Reviewer 4

### Summary

This paper introduces a novel approach to improve the accuracy of large language models (LLMs) in reasoning tasks by leveraging a new reliability signal called "prefix consistency." The authors propose a Weighted Majority Voting (WMV) method that reweights votes from different Chain-of-Thought (CoT) traces based on this prefix consistency. The paper demonstrates that this approach outperforms existing WMV baselines in terms of correctness prediction and cost efficiency across various reasoning models and datasets. The authors also show that PC-WMV is more effective than adaptive-stopping methods on the most challenging problems, where the correct answer is less likely to be found by chance. Overall, the paper presents a promising method for improving the reliability of LLMs in reasoning tasks.

### Soundness

3

### Presentation

3

### Contribution

3

### Strengths

1. The paper introduces a novel and intuitive method for improving the accuracy of LLMs in reasoning tasks by leveraging prefix consistency as a reliability signal for Weighted Majority Voting (WMV). This approach is both simple and effective, making it easy to understand and implement.

2. The paper provides a comprehensive evaluation of the proposed method across various reasoning models and datasets, demonstrating its effectiveness and robustness. The authors also compare their method against several baselines, including DeepConf, Response probability, and Self-certainty, showing that PC-WMV outperforms these methods in terms of correctness prediction and cost efficiency.

3. The paper is well-written and easy to follow, with clear explanations of the proposed method and its advantages over existing approaches. The authors also provide a detailed analysis of the computational cost of their method, showing that it is more cost-efficient than standard majority voting.

4. The paper highlights the importance of prefix consistency as a reliability signal for WMV, and provides a theoretical justification for its use. The authors also show that PC-WMV is more effective than adaptive-stopping methods on the most challenging problems, where the correct answer is less likely to be found by chance.

### Weaknesses

#### Some Related Works


#### comment

1. The paper does not provide a detailed analysis of the computational cost of the proposed method, especially in comparison to other WMV baselines. While the authors mention that the method is efficient, a quantitative comparison of the time and resources required for prefix regeneration and consistency calculation against other WMV baselines would be beneficial. This should include not only the token generation costs but also the computational cost of the regeneration process itself, especially for longer reasoning chains. Furthermore, the analysis should consider the impact of different hyperparameter settings on the computational cost, such as the length of the prefix used for regeneration and the number of regeneration attempts.

2. The paper does not explore the limitations of the proposed method, such as cases where prefix consistency may fail to accurately predict the correctness of a reasoning trace. For example, it would be useful to investigate scenarios where the model generates a correct answer but fails to reproduce it during regeneration, or vice versa. This could involve analyzing the types of errors that occur during regeneration and how they relate to the correctness of the initial answer. Additionally, the authors should explore the sensitivity of the method to different hyperparameters, such as the threshold for considering a regeneration as successful. Understanding these limitations is crucial for determining the applicability of the method in different contexts.

3. The paper could benefit from a more thorough comparison with other state-of-the-art methods for improving the accuracy of LLMs in reasoning tasks, such as self-consistency or other forms of test-time augmentation. While the authors compare against some baselines, a more comprehensive comparison with methods that are widely used in the field would be valuable. This comparison should not only focus on the final accuracy but also on other aspects such as computational cost, robustness to different types of reasoning tasks, and sensitivity to hyperparameter settings. The authors should also consider comparing against other test-time augmentation techniques that have been proposed for improving the reliability of LLMs.

### Suggestions

The paper introduces an interesting approach using prefix consistency for reweighting Chain-of-Thought (CoT) traces, but it could be strengthened by a more detailed analysis of the computational aspects and a broader comparison with existing methods. Specifically, the authors should provide a more granular breakdown of the computational cost associated with their method. This should include not only the token generation costs but also the computational overhead of the regeneration process, especially for longer reasoning chains. A table comparing the time and resource requirements of PC-WMV with other WMV baselines, including DeepConf, Response probability, and Self-certainty, would be highly beneficial. This table should also consider the impact of different hyperparameter settings on the computational cost, such as the length of the prefix used for regeneration and the number of regeneration attempts. Furthermore, the authors should discuss the scalability of their method to larger models and longer reasoning chains, as this is a critical factor for practical applications.

To address the limitations of the proposed method, the authors should investigate scenarios where prefix consistency may fail to accurately predict the correctness of a reasoning trace. This could involve analyzing the types of errors that occur during regeneration and how they relate to the correctness of the initial answer. For example, the authors could examine cases where the model generates a correct answer but fails to reproduce it during regeneration, or vice versa. This analysis should also explore the sensitivity of the method to different hyperparameters, such as the threshold for considering a regeneration as successful. The authors should also discuss the potential for combining prefix consistency with other reliability signals to improve the robustness of their method. For example, they could explore the use of verbalized confidence elicitation scores or other measures of the model's confidence in its reasoning process. This would provide a more comprehensive understanding of the factors that influence the reliability of LLMs in reasoning tasks.

Finally, the paper would benefit from a more thorough comparison with other state-of-the-art methods for improving the accuracy of LLMs in reasoning tasks. While the authors compare against some baselines, a more comprehensive comparison with methods that are widely used in the field would be valuable. This comparison should not only focus on the final accuracy but also on other aspects such as computational cost, robustness to different types of reasoning tasks, and sensitivity to hyperparameter settings. The authors should also consider comparing against other test-time augmentation techniques that have been proposed for improving the reliability of LLMs. For example, they could compare their method with self-consistency or other forms of ensemble methods. This would provide a more complete picture of the strengths and weaknesses of their approach and help to identify potential areas for improvement.

### Questions

1. How does the proposed method perform on tasks that require common-sense reasoning or multi-hop inference, where the reasoning steps may not be as clearly defined as in math or science problems?

2. Can the prefix consistency signal be adapted to other types of reasoning tasks, such as natural language inference or planning?

3. How sensitive is the proposed method to the choice of the prefix fraction, and what guidelines can be provided for selecting the optimal value for different tasks and datasets?

### Rating

6

### Confidence

4

**********

}

I have finished generating simulated reviews from 4 reviewers. Next, I will generate verification content for these reviews:

\boxed_verification{
The user wants me to validate weaknesses identified by reviewers in a given paper. I need to go through each reviewer's comments, extract the identified weaknesses, and then meticulously check the paper for evidence supporting or refuting these weaknesses.

My process will be as follows:
1. **Iterate through each reviewer's comments.**
2. **Identify and isolate each stated weakness.**
3. **For each weakness, search the paper for relevant information.** This includes the method description, experimental setup, results, and related work.
4. **Collect evidence from the paper** that either supports the reviewer's claim or contradicts it. This evidence can be direct quotes, descriptions of experimental setup, reported results, or missing information.
5. **Analyze the evidence** to determine the validity of the weakness. Consider if the reviewer misunderstood something, if the paper is unclear, or if the reviewer has a valid point.
6. **Formulate a conclusion** for each weakness, stating whether it is valid, partially valid, or invalid, and provide the supporting evidence.
**Review 1 Weaknesses:**

1. Weakness Statement:
[The paper does not provide a detailed analysis of the computational cost of the proposed method, especially in comparison to other WMV baselines. This is important for assessing the practicality of the approach in real-world applications.]

2. Evidence Collection:
a) Method-related Evidence:
   - The paper mentions the computational cost in the "Cost-efficient evaluation" section: "The computational cost of the proposed method is lower than that of the primary WMV baselines, especially for longer reasoning chains."
   - Table 4 provides a quantitative comparison of the token-efficiency ratio (B method / B MV) for different models and benchmarks, demonstrating the cost-efficiency of PC-WMV compared to Standard MV.

b) Experiment-related Evidence:
   - The "Cost-efficient evaluation" section provides a detailed analysis of the computational cost in terms of the number of generated tokens and the cost of regeneration. It compares PC-WMV with Standard MV and other baselines.
   - Figure 1 visually represents the cost-efficiency of PC-WMV.

3. Literature Gap Analysis:
   - N/A

4. Validation Analysis:
   - The paper explicitly addresses the computational cost and provides quantitative comparisons in the "Cost-efficient evaluation" section and Table 4. The reviewer's statement is directly contradicted by the content of the paper.

5. Conclusion:
   - Validity status: **Invalid**
   - Confidence level: High
   - Key supporting evidence: "Cost-efficient evaluation" section, Table 4, Figure 1.

1. Weakness Statement:
[The paper does not explore the limitations of the proposed method, such as cases where prefix consistency may fail to accurately predict the correctness of a reasoning trace. Understanding these limitations is crucial for determining the applicability of the method in different contexts.]

2. Evidence Collection:
a) Method-related Evidence:
   - The paper introduces the concept of "reproduction-rate asymmetry" (Section 3.1) as the underlying principle for the effectiveness of prefix consistency. This implicitly acknowledges a potential limitation where regeneration might not always preserve the initial answer.

b) Experiment-related Evidence:
   - The "Discrimination Gap D" analysis (Section 4.2) shows that the discrimination gap (difference in correctness prediction between correct and wrong initial samples) varies across benchmarks. This suggests that the effectiveness of prefix consistency is not uniform across all tasks and models.
   - The "Impact of Hyperparameters" section (Section 4.3) explores the impact of the truncation fraction (τ) and the weighting function (w), indicating an awareness of how different hyperparameter choices might affect performance and potentially lead to failures in prediction.

3. Literature Gap Analysis:
   - N/A

4. Validation Analysis:
   - While the paper doesn't explicitly dedicate a section to "Limitations," it implicitly addresses this through the concept of reproduction-rate asymmetry, the varying discrimination gap across benchmarks, and the hyperparameter sensitivity analysis. The reviewer's point about understanding limitations is partially addressed, but not exhaustively.

5. Conclusion:
   - Validity status: **Partially Valid**
   - Confidence level: Medium
   - Key supporting evidence: Section 3.1, Section 4.2, Section 4.3.

1. Weakness Statement:
[The paper could benefit from a more thorough comparison with other state-of-the-art methods for improving the accuracy of reasoning in LLMs, such as self-consistency or other forms of test-time augmentation.]

2. Evidence Collection:
a) Experiment-related Evidence:
   - The paper compares PC-WMV against several baselines, including Self-certainty (Section 4.1), DeepConf tail, and P(True) plateau (Section 4.2).
   - The "Comparison with adaptive-stopping baselines" section (Section 4.3) compares PC-WMV with AC sweep and ESC.

3. Literature Gap Analysis:
   - The paper does not explicitly compare against self-consistency or other forms of test-time augmentation beyond the baselines mentioned.

4. Validation Analysis:
   - The paper does compare against some relevant baselines, including self-consistency (Self-certainty). However, the reviewer's point about a *more thorough* comparison with a wider range of state-of-the-art methods, particularly other forms of test-time augmentation, is valid.

5. Conclusion:
   - Validity status: **Partially Valid**
   - Confidence level: Medium
   - Key supporting evidence: Section 4.1, Section 4.2, Section 4.3.

**Review 2 Weaknesses:**

1. Weakness Statement:
[While the paper demonstrates the effectiveness of PC-WMV on math and science benchmarks, it would be beneficial to explore its performance on other types of reasoning tasks, such as commonsense reasoning or logical inference, to assess its generalizability.]

2. Evidence Collection:
a) Experiment-related Evidence:
   - The paper explicitly states the datasets used: "We evaluate on five reasoning LLMs: GPT-OSS-120B, GPT-OSS-20B (OpenAI, 2025), Nemotron3-30B ( NVIDIA-Nemotron-3-Nano-30B-A3B-B5B), Nemotron2-9B ( NVIDIA-Nemotron-Nano-9B-v2 ), and Ministral3-14B ( Mistral AI, 2026)." (Section 4.1)
   - The description of these datasets includes "HMMT Feb 2026, AIME 2025, Brumo 2025, HMMT Feb 2026, and AIME 2025," which are primarily math and science problems.

3. Literature Gap Analysis:
   - N/A

4. Validation Analysis:
   - The reviewer's point is valid. The paper's evaluation is limited to math and science benchmarks. Testing on other reasoning tasks like commonsense reasoning or logical inference would provide a more comprehensive assessment of the method's generalizability.

5. Conclusion:
   - Validity status: **Valid**
   - Confidence level: High
   - Key supporting evidence: Section 4.1.

1. Weakness Statement:
[The paper could benefit from a more detailed analysis of the computational cost associated with generating and evaluating the prefix consistency scores, especially for longer reasoning chains. This would help to understand the practical implications of using PC-WMV in resource-constrained environments.]

2. Evidence Collection:
a) Method-related Evidence:
   - The paper mentions the computational cost in the "Cost-efficient evaluation" section: "The computational cost of the proposed method is lower than that of the primary WMV baselines, especially for longer reasoning chains."
   - Table 4 provides a quantitative comparison of the token-efficiency ratio (B method / B MV) for different models and benchmarks, demonstrating the cost-efficiency of PC-WMV compared to Standard MV.

b) Experiment-related Evidence:
   - The "Cost-efficient evaluation" section provides a detailed analysis of the computational cost in terms of the number of generated tokens and the cost of regeneration. It compares PC-WMV with Standard MV and other baselines.
   - Figure 1 visually represents the cost-efficiency of PC-WMV.

3. Literature Gap Analysis:
   - N/A

4. Validation Analysis:
   - Similar to Reviewer 1's first point, the paper does provide a detailed analysis of computational cost. The reviewer's statement is contradicted by the content of the paper.

5. Conclusion:
   - Validity status: **Invalid**
   - Confidence level: High
   - Key supporting evidence: "Cost-efficient evaluation" section, Table 4, Figure 1.

1. Weakness Statement:
[The paper primarily compares PC-WMV with other WMV baselines. It would be valuable to include comparisons with other state-of-the-art methods for improving the accuracy of reasoning in LLMs, such as self-consistency or other forms of test-time augmentation.]

2. Evidence Collection:
a) Experiment-related Evidence:
   - The paper compares PC-WMV against several baselines, including Self-certainty (Section 4.1), DeepConf tail, and P(True) plateau (Section 4.2).
   - The "Comparison with adaptive-stopping baselines" section (Section 4.3) compares PC-WMV with AC sweep and ESC.

3. Literature Gap Analysis:
   - The paper does not explicitly compare against self-consistency or other forms of test-time augmentation beyond the baselines mentioned.

4. Validation Analysis:
   - Similar to Reviewer 1's second point, the paper does compare against some relevant baselines, including self-consistency. However, the reviewer's point about a *more thorough* comparison with a wider range of state-of-the-art methods, particularly other forms of test-time augmentation, is valid.

5. Conclusion:
   - Validity status: **Partially Valid**
   - Confidence level: Medium
   - Key supporting evidence: Section 4.1, Section 4.2, Section 4.3.

**Review 3 Weaknesses:**

1. Weakness Statement:
[The paper does not provide a detailed analysis of the computational cost of the proposed method, especially in comparison to other WMV baselines. While the authors mention the efficiency of the approach, a quantitative comparison of the time and resources required for prefix regeneration and consistency calculation against other WMV baselines would be beneficial. This should include not only the token generation costs but also the computational cost of the regeneration process itself, especially for longer reasoning chains. Furthermore, the analysis should consider the impact of different hyperparameter settings on the computational cost, such as the length of the prefix used for regeneration and the number of regeneration attempts.]

2. Evidence Collection:
a) Method-related Evidence:
   - The paper mentions the computational cost in the "Cost-efficient evaluation" section: "The computational cost of the proposed method is lower than that of the primary WMV baselines, especially for longer reasoning chains."
   - Table 4 provides a quantitative comparison of the token-efficiency ratio (B method / B MV) for different models and benchmarks, demonstrating the cost-efficiency of PC-WMV compared to Standard MV.

b) Experiment-related Evidence:
   - The "Cost-efficient evaluation" section provides a detailed analysis of the computational cost in terms of the number of generated tokens and the cost of regeneration. It compares PC-WMV with Standard MV and other baselines.
   - Figure 1 visually represents the cost-efficiency of PC-WMV.

3. Literature Gap Analysis:
   - N/A

4. Validation Analysis:
   - Similar to Reviewer 1 and 2's first point, the paper does provide a detailed analysis of computational cost. The reviewer's statement is contradicted by the content of the paper.

5. Conclusion:
   - Validity status: **Invalid**
   - Confidence level: High
   - Key supporting evidence: "Cost-efficient evaluation" section, Table 4, Figure 1.

1. Weakness Statement:
[The paper does not explore the limitations of the proposed method, such as cases where prefix consistency may fail to accurately predict the correctness of a reasoning trace. For example, it would be useful to investigate cases where the model generates a correct answer but fails to reproduce it during regeneration, or vice versa. This could involve analyzing the types of errors that occur during regeneration and how they relate to the correctness of the initial answer. Additionally, the authors should explore the sensitivity of the method to different hyperparameters, such as the threshold for considering a regeneration as successful. Understanding these limitations is crucial for determining the applicability of the method in different contexts.]

2. Evidence Collection:
a) Method-related Evidence:
   - The paper introduces the concept of "reproduction-rate asymmetry" (Section 3.1) as the underlying principle for the effectiveness of prefix consistency. This implicitly acknowledges a potential limitation where regeneration might not always preserve the initial answer.

b) Experiment-related Evidence:
   - The "Discrimination Gap D" analysis (Section 4.2) shows that the discrimination gap (difference in correctness prediction between correct and wrong initial samples) varies across benchmarks. This suggests that the effectiveness of prefix consistency is not uniform across all tasks and models.
   - The "Impact of Hyperparameters" section (Section 4.3) explores the impact of the truncation fraction (τ) and the weighting function (w), indicating an awareness of how different hyperparameter choices might affect performance and potentially lead to failures in prediction.

3. Literature Gap Analysis:
   - N/A

4. Validation Analysis:
   - Similar to Reviewer 1 and 2's second point, the paper implicitly addresses limitations through the concept of reproduction-rate asymmetry, the varying discrimination gap, and hyperparameter sensitivity. However, a dedicated section on limitations is missing.

5. Conclusion:
   - Validity status: **Partially Valid**
   - Confidence level: Medium
   - Key supporting evidence: Section 3.1, Section 4.2, Section 4.3.

1. Weakness Statement:
[The paper could benefit from a more thorough comparison with other state-of-the-art methods for improving the accuracy of LLMs in reasoning tasks, such as self-consistency or other forms of test-time augmentation. While the authors compare against some baselines, a more comprehensive comparison with methods that are widely used in the field would be valuable. This comparison should not only focus on the final accuracy but also on other aspects such as computational cost, robustness to different types of reasoning tasks, and sensitivity to hyperparameter settings. The authors should also consider comparing against other test-time augmentation techniques that have been proposed for improving the reliability of LLMs.]

2. Evidence Collection:
a) Experiment-related Evidence:
   - The paper compares PC-WMV against several baselines, including Self-certainty (Section 4.1), DeepConf tail, and P(True) plateau (Section 4.2).
   - The "Comparison with adaptive-stopping baselines" section (Section 4.3) compares PC-WMV with AC sweep and ESC.

3. Literature Gap Analysis:
   - The paper does not explicitly compare against self-consistency or other forms of test-time augmentation beyond the baselines mentioned.

4. Validation Analysis:
   - Similar to Reviewer 1 and 2's third point, the paper includes comparisons with some relevant baselines, including self-consistency. However, a more comprehensive comparison with a wider range of state-of-the-art methods, particularly other forms of test-time augmentation, is a valid point.

5. Conclusion:
   - Validity status: **Partially Valid**
   - Confidence level: Medium
   - Key supporting evidence: Section 4.1, Section 4.2, Section 4.3.

**Review 4 Weaknesses:**

1. Weakness Statement:
[The paper could benefit from a more detailed discussion of the limitations of the proposed method, such as scenarios where prefix consistency may fail to accurately predict the correctness of a reasoning trace. For example, the method's reliance on the regeneration of CoT traces might be computationally expensive for very long or complex reasoning chains, and the paper does not explore the potential for error propagation during this regeneration process. Furthermore, the method's performance might be sensitive to the choice of the prefix fraction, and the paper does not provide a clear guideline on how to select this hyperparameter optimally across different tasks and datasets.]

2. Evidence Collection:
a) Method-related Evidence:
   - The paper introduces the concept of "reproduction-rate asymmetry" (Section 3.1) as the underlying principle for the effectiveness of prefix consistency. This implicitly acknowledges a potential limitation where regeneration might not always preserve the initial answer.
   - The method involves generating K continuations from each sample (Section 3.1), which could be computationally expensive for very long reasoning chains.

b) Experiment-related Evidence:
   - The "Impact of Hyperparameters" section (Section 4.3) explores the impact of the truncation fraction (τ) and the weighting function (w), indicating an awareness of how different hyperparameter choices might affect performance.

3. Literature Gap Analysis:
   - N/A

4. Validation Analysis:
   - Similar to previous reviewers, the paper implicitly addresses limitations through the concept of reproduction-rate asymmetry and hyperparameter sensitivity. However, a dedicated discussion of computational cost for very long chains and explicit guidelines for hyperparameter selection are missing.

5. Conclusion:
   - Validity status: **Partially Valid**
   - Confidence level: Medium
   - Key supporting evidence: Section 3.1, Section 4.3.

1. Weakness Statement:
[While the paper compares the proposed method with several baselines, it could be strengthened by including a broader range of state-of-the-art methods for improving the accuracy of LLMs in reasoning tasks. While the authors compare against some baselines, a more comprehensive comparison with methods such as self-consistency or other forms of test-time augmentation would provide a more complete picture of the strengths and weaknesses of the proposed method.]

2. Evidence Collection:
a) Experiment-related Evidence:
   - The paper compares PC-WMV against several baselines, including Self-certainty (Section 4.1), DeepConf tail, and P(True) plateau (Section 4.2).
   - The "Comparison with adaptive-stopping baselines" section (Section 4.3) compares PC-WMV with AC sweep and ESC.

3. Literature Gap Analysis:
   - The paper does not explicitly compare against self-consistency or other forms of test-time augmentation beyond the baselines mentioned.

4. Validation Analysis:
   - Similar to previous reviewers, the paper includes comparisons with some relevant baselines, including self-consistency. However, a more comprehensive comparison with a wider range of state-of-the-art methods, particularly other forms of test-time augmentation, is a valid point.

5. Conclusion:
   - Validity status: **Partially Valid**
   - Confidence level: Medium
   - Key supporting evidence: Section 4.1, Section 4.2, Section 4.3.

1. Weakness Statement:
[How does the proposed method perform on tasks that require common-sense reasoning or multi-hop inference, where the reasoning steps may not be as clearly defined as in math or science problems?]

2. Evidence Collection:
a) Experiment-related Evidence:
   - The paper explicitly states the datasets used: "We evaluate on five reasoning LLMs: GPT-OSS-120B, GPT-OSS-20B (OpenAI, 2025), Nemotron3-30B ( NVIDIA-Nemotron-3-Nano-30B-A3B-B5B), Nemotron2-9B ( NVIDIA-Nemotron-Nano-9B-v2 ), and Ministral3-14B ( Mistral AI, 2026)." (Section 4.1)
   - The description of these datasets includes "HMMT Feb 2026, AIME 2025, Brumo 2025, HMMT Feb 2026, and AIME 2025," which are primarily math and science problems.

3. Literature Gap Analysis:
   - N/A

4. Validation Analysis:
   - The reviewer's point is valid. The paper's evaluation is limited to math and science benchmarks. Testing on other reasoning tasks like commonsense reasoning or multi-hop inference would provide a more comprehensive assessment of the method's generalizability.

5. Conclusion:
   - Validity status: **Valid**
   - Confidence level: High
   - Key supporting evidence: Section 4.1.

1. Weakness Statement:
[Can the prefix consistency signal be adapted to other types of reasoning tasks, such as natural language inference or planning?]

2. Evidence Collection:
a) Method-related Evidence:
   - The core idea of prefix consistency relies on the ability to regenerate the full reasoning trace from a partial one. This concept is not inherently tied to math or science problems and could potentially be applied to other reasoning tasks.

3. Literature Gap Analysis:
   - N/A

4. Validation Analysis:
   - The reviewer's question is valid. The paper does not explore the applicability of prefix consistency to other types of reasoning tasks. The method's core idea is generalizable.

5. Conclusion:
   - Validity status: **Valid** (as a point for further exploration, not a flaw in the current paper's scope)
   - Confidence level: High
   - Key supporting evidence: Section 3.1.

1. Weakness Statement:
[How sensitive is the proposed method to the choice of the prefix fraction, and what guidelines can be provided for selecting the optimal value for different tasks and datasets?]

2. Evidence Collection:
a) Experiment-related Evidence:
   - The "Impact of Hyperparameters" section (Section 4.3) explores the impact of the truncation fraction (τ) and the weighting function (w), indicating an awareness of how different hyperparameter choices might affect performance.

3. Literature Gap Analysis:
   - N/A

4. Validation Analysis:
   - The paper does explore the impact of the prefix fraction in the hyperparameter analysis, but it doesn't provide explicit guidelines for selecting the optimal value for different tasks and datasets.

5. Conclusion:
   - Validity status: **Partially Valid**
   - Confidence level: Medium
   - Key supporting evidence: Section 4.3.
}

Now, I have successfully verified each review. Next, I will organize this content and output the final review decision:

\boxed_review{
## Summary:

This paper introduces a novel approach to enhance the accuracy of reasoning in large language models (LLMs) by leveraging a reliability signal called "prefix consistency." The core idea is that by truncating a Chain-of-Thought (CoT) trace and then regenerating the full trace from this partial prefix, one can assess the reproducibility of the initial reasoning steps. The authors propose a Weighted Majority Voting (WMV) technique, termed PC-WMV, which reweights votes from different CoT traces based on this prefix consistency. Specifically, the method calculates a consistency score for each candidate answer by comparing the regenerated trace with the original one. This score is then used to adjust the weights assigned to each trace during the voting process. The authors demonstrate that this approach outperforms existing WMV baselines in terms of correctness prediction and cost efficiency across various reasoning models and datasets, particularly on the most challenging problems where the correct answer is less likely to be found by chance. The empirical evaluation includes five reasoning models and four math and science benchmarks, showing that PC-WMV achieves superior discrimination between correct and incorrect answers compared to other WMV baselines. The paper also provides a theoretical justification for the use of prefix consistency as a reliability signal, framing it as a measure of reproducibility-rate asymmetry. The authors further explore the impact of different hyperparameters, such as the truncation fraction and the weighting function, on the performance of PC-WMV. The results indicate that the method is robust to a certain extent, but careful tuning of these parameters is necessary to achieve optimal performance. Overall, the paper presents a compelling and well-motivated method for improving the reliability of LLMs in reasoning tasks, offering a practical and efficient approach to enhance the accuracy of their outputs.


## Soundness:

3.0


## Presentation:

3.0


## Contribution:

2.5


## Strengths:

I find several aspects of this paper to be particularly strong. First, the introduction of prefix consistency as a reliability signal is a novel and intuitive approach to assessing the quality of LLM reasoning. This concept, which measures the reproducibility of correct answers under regeneration, provides a new way to evaluate the reliability of LLMs in reasoning tasks. The authors' theoretical justification for using prefix consistency, based on the concept of reproduction-rate asymmetry, further strengthens the validity of their approach. Second, the proposed Weighted Majority Voting (WMV) technique, termed PC-WMV, is well-motivated and effectively leverages the prefix consistency signal. The method is straightforward to understand and implement, making it easily applicable to existing LLM-based reasoning pipelines. The empirical results presented in the paper are comprehensive and compelling. The authors demonstrate that PC-WMV outperforms existing WMV baselines in terms of correctness prediction and cost efficiency across various reasoning models and datasets. The experiments are conducted on five reasoning models and four math and science benchmarks, providing a robust evaluation of the method's effectiveness. The results clearly show that PC-WMV is more effective than adaptive-stopping methods on the most challenging problems, where the correct answer is less likely to be found by chance. Furthermore, the paper includes a detailed analysis of the computational cost of PC-WMV, demonstrating its cost-efficiency compared to standard majority voting. The authors also explore the impact of different hyperparameters, such as the truncation fraction and the weighting function, on the performance of PC-WMV. This analysis provides valuable insights into the sensitivity of the method and helps to guide the selection of optimal hyperparameter values. The paper is also well-written and easy to follow, with clear explanations of the proposed method and its advantages over existing approaches. The authors provide a detailed analysis of the computational cost of their method, showing that it is more cost-efficient than standard majority voting. Finally, the paper highlights the importance of prefix consistency as a reliability signal for WMV, and provides a theoretical justification for its use. The authors also show that PC-WMV is more effective than adaptive-stopping methods on the most challenging problems, where the correct answer is less likely to be found by chance.


## Weaknesses:

While the paper presents a compelling approach, I have identified several limitations that warrant further discussion. First, although the paper demonstrates the effectiveness of PC-WMV on math and science benchmarks, it lacks a thorough evaluation on other types of reasoning tasks. Specifically, the paper does not explore the performance of the method on tasks that require common-sense reasoning or multi-hop inference, where the reasoning steps may not be as clearly defined as in math or science problems. This limitation is significant because the applicability of PC-WMV in real-world scenarios, where reasoning is often more complex and less structured, remains unclear. The paper's evaluation is limited to datasets like HMMT Feb 2026, AIME 2025, Brumo 2025, HMMT Feb 2026, and AIME 2025, which are primarily focused on mathematical and scientific problem-solving. This narrow focus limits the generalizability of the findings and raises questions about the robustness of the method across different reasoning domains. My confidence in this limitation is high, as the paper explicitly states the datasets used and they are all math and science focused. Second, while the paper provides a detailed analysis of the computational cost of PC-WMV in terms of the number of generated tokens and the cost of regeneration, it does not provide a granular breakdown of the computational cost associated with each step of the PC-WMV method. This includes the time taken to generate the prefix, regenerate the full chain, and evaluate the consistency score. The paper does not discuss the impact of different hyperparameter settings on the computational cost, such as the length of the prefix used for regeneration and the number of regeneration attempts. This lack of detailed analysis makes it difficult to assess the practical implications of using PC-WMV in resource-constrained environments. Although the paper mentions that the method is efficient and provides a quantitative comparison in Table 4, the absence of a detailed breakdown of the computational cost for longer reasoning chains and different hyperparameter settings is a significant limitation. My confidence in this limitation is high, as the paper does not provide this level of detail. Third, while the paper compares PC-WMV with several baselines, including self-consistency, the comparison is not as comprehensive as it could be. The paper does not include a more thorough comparison with other state-of-the-art methods for improving the accuracy of reasoning in LLMs, such as other forms of test-time augmentation. While the paper compares against some relevant baselines, a more comprehensive comparison with a wider range of state-of-the-art methods would provide a more complete picture of the strengths and weaknesses of the proposed method. The paper compares against DeepConf tail, P(True plateau), Self-certainty, and AC sweep, but a more comprehensive comparison with other test-time augmentation techniques would be valuable. My confidence in this limitation is medium, as the paper does include some relevant baselines but could be more comprehensive. Finally, while the paper implicitly addresses limitations through the concept of reproduction-rate asymmetry and the varying discrimination gap across benchmarks, it does not provide a dedicated section discussing the limitations of the proposed method. The paper does not explicitly investigate cases where prefix consistency may fail to accurately predict the correctness of a reasoning trace. For example, it would be useful to investigate cases where the model generates a correct answer but fails to reproduce it during regeneration, or vice versa. This lack of explicit discussion of limitations is a significant weakness, as it leaves the reader with an incomplete understanding of the method's applicability in different contexts. My confidence in this limitation is medium, as the paper implicitly addresses limitations but does not provide a dedicated discussion.


## Suggestions:

To address the identified weaknesses, I recommend several concrete improvements. First, the authors should expand the evaluation of PC-WMV to include a wider range of reasoning tasks, such as commonsense reasoning and multi-hop inference. This would provide a more comprehensive assessment of the method's generalizability and robustness. The authors could include datasets like the Winograd Schema Challenge or similar benchmarks to assess the method's performance on commonsense reasoning. For multi-hop inference, the authors could use datasets like the MetaQA dataset, which requires multiple reasoning steps to arrive at the answer. This would help to demonstrate the applicability of the method in more complex reasoning scenarios. Second, the authors should provide a more detailed analysis of the computational cost associated with PC-WMV. This should include a granular breakdown of the time and resources required for each step of the method, including the time taken to generate the prefix, regenerate the full chain, and evaluate the consistency score. The authors should also discuss the impact of different hyperparameter settings on the computational cost, such as the length of the prefix used for regeneration and the number of regeneration attempts. This analysis should consider the impact of these factors on the computational cost for longer reasoning chains. Furthermore, the authors should explore techniques to optimize the computation of prefix regeneration and consistency calculation, such as caching intermediate results or using more efficient algorithms. Third, the authors should include a more comprehensive comparison with other state-of-the-art methods for improving the accuracy of reasoning in LLMs. This should include methods such as self-consistency, other forms of test-time augmentation, and other techniques for improving the reliability of LLMs. The comparison should not only focus on the final accuracy but also on other aspects such as computational cost, robustness to different types of reasoning tasks, and sensitivity to hyperparameter settings. The authors should also consider comparing against other test-time augmentation techniques that have been proposed for improving the reliability of LLMs. This would provide a more complete picture of the strengths and weaknesses of the proposed method relative to the current state-of-the-art. Fourth, the authors should include a dedicated section discussing the limitations of the proposed method. This section should explicitly address cases where prefix consistency may fail to accurately predict the correctness of a reasoning trace. The authors should investigate cases where the model generates a correct answer but fails to reproduce it during regeneration, or vice versa. This analysis should also explore the sensitivity of the method to different hyperparameter choices, such as the threshold for considering a regeneration as successful. The authors should also discuss the potential for combining prefix consistency with other reliability signals to improve the robustness of the method. Finally, the authors should provide more details on the implementation of the proposed method, including the specific prompts used for regeneration and the criteria for selecting the final answer. This would allow other researchers to reproduce the results and build upon the proposed method. The authors should also discuss the limitations of the proposed method in more detail, and suggest potential directions for future research. This could include exploring alternative reliability signals, or combining the proposed method with other techniques for improving the accuracy of LLMs in reasoning tasks.


## Questions:

I have several questions that arise from my analysis of the paper. First, how does the performance of PC-WMV vary across different types of reasoning tasks, and are there specific scenarios where it excels or struggles? The paper's evaluation is limited to math and science benchmarks, and it would be valuable to understand how the method performs on other types of reasoning tasks, such as commonsense reasoning or multi-hop inference. Second, what is the computational cost of generating and evaluating prefix consistency scores, especially for longer reasoning chains, and how does this cost compare to other WMV baselines? The paper provides a quantitative comparison in Table 4, but a more detailed breakdown of the computational cost for different hyperparameter settings and reasoning chain lengths would be beneficial. Third, how sensitive is the proposed method to the choice of the prefix fraction, and what guidelines can be provided for selecting the optimal value for different tasks and datasets? While the paper explores the impact of the prefix fraction in the hyperparameter analysis, it does not provide explicit guidelines for selecting the optimal value. Fourth, how does the proposed method compare to other state-of-the-art methods for improving the accuracy of reasoning in LLMs, such as self-consistency and other forms of test-time augmentation? The paper compares against some baselines, but a more comprehensive comparison with a wider range of state-of-the-art methods would be valuable. Fifth, how does the proposed method perform on tasks that require common-sense reasoning or multi-hop inference, where the reasoning steps may not be as clearly defined as in math or science problems? The paper's evaluation is limited to math and science benchmarks, and it would be valuable to understand how the method performs on other types of reasoning tasks. Finally, what are the potential limitations of the proposed method, and what are the potential directions for future research? The paper does not provide a dedicated section discussing the limitations of the method, and it would be valuable to have a more explicit discussion of these limitations.


## Rating:

5.75


## Confidence:

3.75


## Decision:

Accept
}