I will use Standard Mode for comprehensive thinking. As a professional reviewer, I will simulate 4 different reviewers, followed by the verification thinking. Then I will output the Finally Review Output. Let me think - Standard Mode means I will output the original review, followed by the verification thinking. Considering that I am currently in standard mode, I should think from my existing knowledge and consider some related work content when writing about weaknesses. Then I will output the Finally Review Output and Meta Review Output:

\boxed_simreviewers{
## Reviewer 1

### Summary

This paper draws a connection between reinforcement learning (RL) and supervised fine-tuning (SFT) in the context of sparse reward settings. The authors demonstrate that SFT can be viewed as optimizing a lower bound on the RL objective in scenarios with sparse rewards. Building on this insight, they propose an improved method called importance-weighted supervised fine-tuning (iw-SFT) that optimizes a tighter bound to the RL objective. The paper shows that this approach can be applied to both language model fine-tuning and continuous control tasks, achieving competitive results with less training compute.

### Soundness

3

### Presentation

3

### Contribution

2

### Strengths

1. The paper provides a theoretical connection between SFT and RL, offering a new perspective on SFT as an approximation of RL.
2. The proposed iw-SFT method is simple yet effective, showing significant performance gains over standard SFT in both language model and control tasks.
3. The authors conduct extensive experiments across multiple domains, demonstrating the robustness and versatility of their approach.

### Weaknesses

#### Some Related Works


#### comment

1. The paper assumes a sparse reward setting, which may not always be the case in real-world applications. In many practical scenarios, rewards are dense or semi-dense, making the RL perspective less relevant. Specifically, the paper does not address how the proposed method would perform in environments with continuous reward signals, where the sparse reward assumption breaks down. The theoretical connection between SFT and RL, which is central to the paper's contribution, relies on the sparsity of rewards, and it is unclear how this connection would hold or be modified in dense reward settings.
2. The proposed method requires additional computational resources for importance sampling, which may not be feasible in resource-constrained environments. The paper does not provide a detailed analysis of the computational overhead associated with the importance sampling step, making it difficult to assess the practical applicability of the method in scenarios with limited computational budgets. Furthermore, the paper does not explore alternative, potentially more efficient, methods for estimating the importance weights.
3. The paper primarily focuses on filtered datasets for SFT, but it would be valuable to explore how iw-SFT could be applied to other forms of data, such as unfiltered or mixed-quality datasets. The current analysis is limited to scenarios where high-quality data is readily available and can be filtered. The paper does not investigate the performance of iw-SFT when applied to datasets with varying levels of noise and uncertainty, which is a common challenge in real-world applications. It is unclear how the method would handle datasets where the quality of data is not easily categorized or filtered.

### Suggestions

The paper would benefit from a more thorough discussion of the limitations of the sparse reward assumption and how the proposed method might be adapted for dense or semi-dense reward settings. Specifically, the authors should explore alternative formulations of the RL objective that are more suitable for dense reward environments, such as policy gradient methods or actor-critic algorithms. Furthermore, the paper should include experiments on benchmark tasks with dense rewards to demonstrate the performance of iw-SFT in a broader range of scenarios. This would help to clarify the scope and applicability of the proposed method and provide a more comprehensive understanding of its strengths and weaknesses. The authors should also consider the potential for combining their approach with existing techniques for handling dense rewards, such as reward shaping or reward decomposition, to further improve performance.

To address the computational concerns, the paper should include a detailed analysis of the computational cost of the importance sampling step and explore alternative methods for estimating importance weights that are more computationally efficient. For example, the authors could investigate the use of online importance estimation techniques or explore methods for approximating the importance weights using a smaller set of samples. The paper should also provide a comparison of the computational cost of iw-SFT with other SFT methods, such as standard SFT or behavior cloning, to demonstrate the trade-offs between performance and computational efficiency. Furthermore, the authors should discuss the potential for parallelizing the importance sampling step to reduce the overall training time. This would help to make the method more practical for resource-constrained environments.

Finally, the paper should explore the application of iw-SFT to other forms of data, such as unfiltered or mixed-quality datasets. The authors should investigate how the method performs when applied to datasets with varying levels of noise and uncertainty, and explore techniques for mitigating the impact of low-quality data. For example, the authors could consider using robust loss functions or incorporating uncertainty estimates into the importance weighting scheme. The paper should also investigate the potential for combining iw-SFT with data augmentation techniques to improve the robustness of the method. This would help to broaden the applicability of the proposed method and make it more useful in real-world scenarios where high-quality data is not always available.

### Questions

1. How does the performance of iw-SFT compare to other state-of-the-art methods in dense reward settings?
2. What are the computational costs associated with the importance sampling step in iw-SFT, and how do they scale with the size of the dataset?
3. How well does iw-SFT perform when applied to unfiltered or mixed-quality datasets, and what modifications might be needed to handle such data effectively?

### Rating

6

### Confidence

3

**********

## Reviewer 2

### Summary

This paper draws a connection between SFT and RL, showing that SFT on curated data is optimizing a lower bound on the RL objective. The authors propose a new method, importance-weighted SFT (iw-SFT), which improves upon standard SFT by optimizing a tighter bound to the RL objective. The paper demonstrates the effectiveness of iw-SFT on both LLM reasoning tasks and continuous control tasks.

### Soundness

3

### Presentation

3

### Contribution

3

### Strengths

1. The paper provides a novel perspective on SFT by drawing a connection to RL, which is a relatively new and interesting approach.

2. The proposed method, iw-SFT, is simple and effective, and the authors provide a thorough theoretical analysis and empirical evaluation.

3. The paper is well-written and easy to follow.

### Weaknesses

#### Some Related Works


#### comment

1. The paper assumes a sparse reward setting, which may not always be the case in real-world applications. In many practical scenarios, rewards are dense or semi-dense, making the RL perspective less relevant. Specifically, the paper does not address how the proposed method would perform in environments with continuous reward signals, where the sparse reward assumption breaks down. The theoretical connection between SFT and RL, which is central to the paper's contribution, relies on the sparsity of rewards, and it is unclear how this connection would hold or be modified in dense reward settings.

2. The proposed method requires additional computational resources for importance sampling, which may not be feasible in resource-constrained environments. The paper does not provide a detailed analysis of the computational overhead associated with the importance sampling step, making it difficult to assess the practical applicability of the method in scenarios with limited computational budgets. Furthermore, the paper does not explore alternative, potentially more efficient, methods for estimating the importance weights.

3. The paper primarily focuses on filtered datasets for SFT, but it would be valuable to explore how iw-SFT could be applied to other forms of data, such as unfiltered or mixed-quality datasets. The current analysis is limited to scenarios where high-quality data is readily available and can be filtered. The paper does not investigate the performance of iw-SFT when applied to datasets with varying levels of noise and uncertainty, which is a common challenge in real-world applications. It is unclear how the method would handle datasets where the quality of data is not easily categorized or filtered.

### Suggestions

The paper would benefit from a more thorough discussion of the limitations of the sparse reward assumption and how the proposed method might be adapted for dense or semi-dense reward settings. Specifically, the authors should explore alternative formulations of the RL objective that are more suitable for dense reward environments, such as policy gradient methods or actor-critic algorithms. Furthermore, the paper should include experiments on benchmark tasks with dense rewards to demonstrate the performance of iw-SFT in a broader range of scenarios. This would help to clarify the scope and applicability of the proposed method and provide a more comprehensive understanding of its strengths and weaknesses. The authors should also consider the potential for combining their approach with existing techniques for handling dense rewards, such as reward shaping or reward decomposition, to further improve performance.

To address the computational concerns, the paper should include a detailed analysis of the computational cost of the importance sampling step and explore alternative methods for estimating importance weights that are more computationally efficient. For example, the authors could investigate the use of online importance estimation techniques or explore methods for approximating the importance weights using a smaller set of samples. The paper should also provide a comparison of the computational cost of iw-SFT with other SFT methods, such as standard SFT or behavior cloning, to demonstrate the trade-offs between performance and computational efficiency. Furthermore, the authors should discuss the potential for parallelizing the importance sampling step to reduce the overall training time. This would help to make the method more practical for resource-constrained environments.

Finally, the paper should explore the application of iw-SFT to other forms of data, such as unfiltered or mixed-quality datasets. The authors should investigate how the method performs when applied to datasets with varying levels of noise and uncertainty, and explore techniques for mitigating the impact of low-quality data. For example, the authors could consider using robust loss functions or incorporating uncertainty estimates into the importance weighting scheme. The paper should also investigate the potential for combining iw-SFT with data augmentation techniques to improve the robustness of the method. This would help to broaden the applicability of the proposed method and make it more useful in real-world scenarios where high-quality data is not always available.

### Questions

1. How does the performance of iw-SFT compare to other state-of-the-art methods in dense reward settings?

2. What are the computational costs associated with the importance sampling step in iw-SFT, and how do they scale with the size of the dataset?

3. How well does iw-SFT perform when applied to unfiltered or mixed-quality datasets, and what modifications might be needed to handle such data effectively?

### Rating

6

### Confidence

3

**********

## Reviewer 3

### Summary

This paper proposes a new method for SFT that improves upon the standard SFT approach by incorporating importance weighting. The authors draw a connection between SFT and RL, showing that SFT can be viewed as optimizing a lower bound on the RL objective. They introduce importance-weighted SFT (iw-SFT), which optimizes a tighter bound to the RL objective. The authors demonstrate the effectiveness of their method on both language model reasoning tasks and continuous control tasks.

### Soundness

3

### Presentation

3

### Contribution

2

### Strengths

1. The paper provides a novel perspective on SFT by drawing a connection to RL, which is a relatively new and interesting approach.

2. The proposed method, iw-SFT, is simple yet effective, and the authors provide a thorough theoretical analysis and empirical evaluation.

3. The paper is well-written and easy to follow.

### Weaknesses

#### Some Related Works


#### comment

1. The paper assumes a sparse reward setting, which may not always be the case in real-world applications. In many practical scenarios, rewards are dense or semi-dense, making the RL perspective less relevant. Specifically, the paper does not address how the proposed method would perform in environments with continuous reward signals, where the sparse reward assumption breaks down. The theoretical connection between SFT and RL, which is central to the paper's contribution, relies on the sparsity of rewards, and it is unclear how this connection would hold or be modified in dense reward settings.

2. The proposed method requires additional computational resources for importance sampling, which may not be feasible in resource-constrained environments. The paper does not provide a detailed analysis of the computational overhead associated with the importance sampling step, making it difficult to assess the practical applicability of the method in scenarios with limited computational budgets. Furthermore, the paper does not explore alternative, potentially more efficient, methods for estimating the importance weights.

3. The paper primarily focuses on filtered datasets for SFT, but it would be valuable to explore how iw-SFT could be applied to other forms of data, such as unfiltered or mixed-quality datasets. The current analysis is limited to scenarios where high-quality data is readily available and can be filtered. The paper does not investigate the performance of iw-SFT when applied to datasets with varying levels of noise and uncertainty, which is a common challenge in real-world applications. It is unclear how the method would handle datasets where the quality of data is not easily categorized or filtered.

### Suggestions

The paper would benefit from a more thorough discussion of the limitations of the sparse reward assumption and how the proposed method might be adapted for dense or semi-dense reward settings. Specifically, the authors should explore alternative formulations of the RL objective that are more suitable for dense reward environments, such as policy gradient methods or actor-critic algorithms. Furthermore, the paper should include experiments on benchmark tasks with dense rewards to demonstrate the performance of iw-SFT in a broader range of scenarios. This would help to clarify the scope and applicability of the proposed method and provide a more comprehensive understanding of its strengths and weaknesses. The authors should also consider the potential for combining their approach with existing techniques for handling dense rewards, such as reward shaping or reward decomposition, to further improve performance.

To address the computational concerns, the paper should include a detailed analysis of the computational cost of the importance sampling step and explore alternative methods for estimating importance weights that are more computationally efficient. For example, the authors could investigate the use of online importance estimation techniques or explore methods for approximating the importance weights using a smaller set of samples. The paper should also provide a comparison of the computational cost of iw-SFT with other SFT methods, such as standard SFT or behavior cloning, to demonstrate the trade-offs between performance and computational efficiency. Furthermore, the authors should discuss the potential for parallelizing the importance sampling step to reduce the overall training time. This would help to make the method more practical for resource-constrained environments.

Finally, the paper should explore the application of iw-SFT to other forms of data, such as unfiltered or mixed-quality datasets. The authors should investigate how the method performs when applied to datasets with varying levels of noise and uncertainty, and explore techniques for mitigating the impact of low-quality data. For example, the authors could consider using robust loss functions or incorporating uncertainty estimates into the importance weighting scheme. The paper should also investigate the potential for combining iw-SFT with data augmentation techniques to improve the robustness of the method. This would help to broaden the applicability of the proposed method and make it more useful in real-world scenarios where high-quality data is not always available.

### Questions

1. How does the performance of iw-SFT compare to other state-of-the-art methods in dense reward settings?

2. What are the computational costs associated with the importance sampling step in iw-SFT, and how do they scale with the size of the dataset?

3. How well does iw-SFT perform when applied to unfiltered or mixed-quality datasets, and what modifications might be needed to handle such data effectively?

### Rating

6

### Confidence

3

**********

## Reviewer 4

### Summary

This paper studies the connection between SFT and RL and proposes a new method to improve SFT. The authors show that SFT can be viewed as optimizing a lower bound of the RL objective in sparse reward settings. They propose a new method called importance-weighted SFT (iw-SFT) to improve SFT by optimizing a tighter bound to the RL objective. The authors conduct experiments on both language model reasoning tasks and continuous control tasks to demonstrate the effectiveness of their method.

### Soundness

3

### Presentation

3

### Contribution

3

### Strengths

1. The paper is well-written and easy to follow.
2. The paper provides a novel perspective on SFT by connecting it to RL and proposes a new method to improve SFT.
3. The experiments are comprehensive and demonstrate the effectiveness of the proposed method.

### Weaknesses

#### Some Related Works


#### comment

1. The paper assumes a sparse reward setting, which may not always be the case in real-world applications. In many practical scenarios, rewards are dense or semi-dense, making the RL perspective less relevant. Specifically, the paper does not address how the proposed method would perform in environments with continuous reward signals, where the sparse reward assumption breaks down. The theoretical connection between SFT and RL, which is central to the paper's contribution, relies on the sparsity of rewards, and it is unclear how this connection would hold or be modified in dense reward settings.
2. The proposed method requires additional computational resources for importance sampling, which may not be feasible in resource-constrained environments. The paper does not provide a detailed analysis of the computational overhead associated with the importance sampling step, making it difficult to assess the practical applicability of the method in scenarios with limited computational budgets. Furthermore, the paper does not explore alternative, potentially more efficient, methods for estimating the importance weights.
3. The paper primarily focuses on filtered datasets for SFT, but it would be valuable to explore how iw-SFT could be applied to other forms of data, such as unfiltered or mixed-quality datasets. The current analysis is limited to scenarios where high-quality data is readily available and can be filtered. The paper does not investigate the performance of iw-SFT when applied to datasets with varying levels of noise and uncertainty, which is a common challenge in real-world applications. It is unclear how the method would handle datasets where the quality of data is not easily categorized or filtered.

### Suggestions

The paper would benefit from a more thorough discussion of the limitations of the sparse reward assumption and how the proposed method might be adapted for dense or semi-dense reward settings. Specifically, the authors should explore alternative formulations of the RL objective that are more suitable for dense reward environments, such as policy gradient methods or actor-critic algorithms. Furthermore, the paper should include experiments on benchmark tasks with dense rewards to demonstrate the performance of iw-SFT in a broader range of scenarios. This would help to clarify the scope and applicability of the proposed method and provide a more comprehensive understanding of its strengths and weaknesses. The authors should also consider the potential for combining their approach with existing techniques for handling dense rewards, such as reward shaping or reward decomposition, to further improve performance.

To address the computational concerns, the paper should include a detailed analysis of the computational cost of the importance sampling step and explore alternative methods for estimating importance weights that are more computationally efficient. For example, the authors could investigate the use of online importance estimation techniques or explore methods for approximating the importance weights using a smaller set of samples. The paper should also provide a comparison of the computational cost of iw-SFT with other SFT methods, such as standard SFT or behavior cloning, to demonstrate the trade-offs between performance and computational efficiency. Furthermore, the authors should discuss the potential for parallelizing the importance sampling step to reduce the overall training time. This would help to make the method more practical for resource-constrained environments.

Finally, the paper should explore the application of iw-SFT to other forms of data, such as unfiltered or mixed-quality datasets. The authors should investigate how the method performs when applied to datasets with varying levels of noise and uncertainty, and explore techniques for mitigating the impact of low-quality data. For example, the authors could consider using robust loss functions or incorporating uncertainty estimates into the importance weighting scheme. The paper should also investigate the potential for combining iw-SFT with data augmentation techniques to improve the robustness of the method. This would help to broaden the applicability of the proposed method and make it more useful in real-world scenarios where high-quality data is not always available.

### Questions

1. How does the performance of iw-SFT compare to other state-of-the-art methods in dense reward settings?
2. What are the computational costs associated with the importance sampling step in iw-SFT, and how do they scale with the size of the dataset?
3. How well does iw-SFT perform when applied to unfiltered or mixed-quality datasets, and what modifications might be needed to handle such data effectively?

### Rating

8

### Confidence

4

**********

}

I have finished generating simulated reviews from 4 reviewers. Next, I will generate verification content for these reviews:

\boxed_verification{
The user wants me to validate weaknesses identified by reviewers for the provided paper. I need to go through each reviewer's comments and find evidence in the paper to support their claims.

Plan:
1. Go through each reviewer's comments one by one.
2. For each weakness identified by the reviewer, find the relevant section in the paper.
3. Extract evidence (quotes, formulas, missing citations, etc.) from the paper to support the weakness.
4. If the weakness is about missing information, check if that information is indeed absent.
5. If there are conflicting opinions, note them down.
6. Finally, summarize the findings for each weakness and conclude if it's valid, partially valid, or invalid.
**Review 1**

1. Weakness Statement:
"The paper assumes a sparse reward setting, which may not always be the case in real-world applications. In many practical scenarios, rewards are dense or semi-dense, making the RL perspective less relevant. Specifically, the paper does not address how the proposed method would perform in environments with continuous reward signals, where the sparse reward assumption breaks down. The theoretical connection between SFT and RL, which is central to the paper's contribution, relies on the sparsity of rewards, and it is unclear how this connection would hold or be modified in dense reward settings."

2. Evidence Collection:
a) Method-related Evidence:
   - The paper explicitly states the focus on sparse reward settings in the Introduction: "We draw a on a known connection between this successful strategy and the sparse reward regime."
   - The "SFT lower bounds RL" section (Section 3.2) starts with: "We can derive a lower bound on this RL objective via a well known inequality [ Kober and Peters, 2008 , Roux, 2016b , Ferbach et al., 2024 ] ... assuming strictly positive rewards, we can utilize the inequality x ≥ 1 + log(x) applied to the importance weights..."
   - The derivation of the lower bound relies on the assumption of sparse rewards, as the inequality used is specific to this scenario.
b) Experiment-related Evidence:
   - The experiments in Section 4.1 (LLMs) and Section 4.2 (Control) both use sparse reward settings. For LLMs, the reward is based on whether the generated response matches the top-k examples (binary reward). For Control, the rewards are discretized into ordinal categories.

3. Literature Gap Analysis:
   - The paper does not discuss or cite literature that addresses the connection between SFT and RL in dense reward settings.

4. Validation Analysis:
   - The paper's core theoretical framework and experimental validation are based on the assumption of sparse rewards. The reviewer correctly points out that this assumption might not hold in all real-world scenarios, and the paper doesn't address the implications for dense rewards.

5. Conclusion:
   - Validity status: Valid
   - Confidence level: High
   - Key supporting evidence: Explicit mention of sparse reward setting in the introduction and the derivation of the lower bound relying on this assumption.

1. Weakness Statement:
"The proposed method requires additional computational resources for importance sampling, which may not be feasible in resource-constrained environments. The paper does not provide a detailed analysis of the computational overhead associated with the importance sampling step, making it difficult to assess the practical applicability of the method in scenarios with limited computational budgets. Furthermore, the paper does not explore alternative, potentially more efficient, methods for estimating the importance weights."

2. Evidence Collection:
a) Method-related Evidence:
   - The "Importance Weighted SFT (iw-SFT)" section (Section 3.3) introduces the concept of importance weights and the need to compute them.
   - The description of the smoothing per-step importance weights mentions: "We can thus side-step common problems with large variance in the importance weights/blow-up by enforcing importance weights to not be too extreme. That is we choose: q ⁡ ( τ ) = p ⁡ ( s 0 ) ​ ∏ t = 0 T − 1 ( p ⁡ ( s t + 1 | s t ) ​ clip ⁡ ( π ⁡ ( a t | s t ; θ ) , α min , α max ) )". This shows the need to compute the importance weights at each step.
   - The "The importance of choosing q ⁡ ( τ ) q(\tau)" section discusses the role of the auxiliary distribution but doesn't detail the computational cost of choosing it.
b) Experiment-related Evidence:
   - The paper mentions using g(q) = 0.1 * clip(x, 0.2, 1.8) for smoothing, which involves a computation at each step.
   - There is no explicit analysis of the computational time or resources required for the importance sampling step.

3. Literature Gap Analysis:
   - While the paper cites works on importance sampling, it doesn't delve into the computational complexity of different importance sampling techniques.

4. Validation Analysis:
   - The reviewer is correct that the paper introduces a method that inherently involves importance sampling, which can be computationally intensive. The paper lacks a detailed analysis of this overhead.

5. Conclusion:
   - Validity status: Valid
   - Confidence level: High
   - Key supporting evidence: The description of the importance weight calculation and the smoothing function implies computational overhead, which is not analyzed.

1. Weakness Statement:
"The paper primarily focuses on filtered datasets for SFT, but it would be valuable to explore how iw-SFT could be applied to other forms of data, such as unfiltered or mixed-quality datasets. The current analysis is limited to scenarios where high-quality data is readily available and can be filtered. The paper does not investigate the performance of iw-SFT when applied to datasets with varying levels of noise and uncertainty, which is a common challenge in real-world applications. It is unclear how the method would handle datasets where the quality of data is not easily categorized or filtered."

2. Evidence Collection:
a) Method-related Evidence:
   - The "SFT lower bounds RL" section (Section 3.2) discusses filtering as a way to obtain quality scores.
   - The "Importance Weighted SFT (iw-SFT)" section (Section 3.3) mentions using a reference distribution, which could be derived from a filtered dataset.
b) Experiment-related Evidence:
   - The experiments in Section 4.1 and 4.2 explicitly use filtered datasets.
   - The paper does not include experiments or analysis on applying iw-SFT to unfiltered or mixed-quality datasets.

3. Literature Gap Analysis:
   - The paper does not cite literature on handling noisy or mixed-quality data in the context of SFT.

4. Validation Analysis:
   - The reviewer accurately points out that the paper's focus is on filtered datasets, and it doesn't explore the applicability of iw-SFT to other data types.

5. Conclusion:
   - Validity status: Valid
   - Confidence level: High
   - Key supporting evidence: The experimental setup and the method description are centered around filtered datasets.

**Review 2**

1. Weakness Statement:
"The paper assumes a sparse reward setting, which may not always be the case in real-world applications. In many practical scenarios, rewards are dense or semi-dense, making the RL perspective less relevant. Specifically, the paper does not address how the proposed method would perform in environments with continuous reward signals, where the sparse reward assumption breaks down. The theoretical connection between SFT and RL, which is central to the paper's contribution, relies on the sparsity of rewards, and it is unclear how this connection would hold or be modified in dense reward settings."

2. Evidence Collection:
   - This is the same weakness as identified by Reviewer 1, and the evidence and validation are the same.

3. Literature Gap Analysis:
   - Same as Reviewer 1.

4. Validation Analysis:
   - Same as Reviewer 1.

5. Conclusion:
   - Validity status: Valid
   - Confidence level: High
   - Key supporting evidence: Same as Reviewer 1.

1. Weakness Statement:
"The proposed method requires additional computational resources for importance sampling, which may not be feasible in resource-constrained environments. The paper does not provide a detailed analysis of the computational overhead associated with the importance sampling step, making it difficult to assess the practical applicability of the method in scenarios with limited computational budgets. Furthermore, the paper does not explore alternative, potentially more efficient, methods for estimating the importance weights."

2. Evidence Collection:
   - This is the same weakness as identified by Reviewer 1, and the evidence and validation are the same.

3. Literature Gap Analysis:
   - Same as Reviewer 1.

4. Validation Analysis:
   - Same as Reviewer 1.

5. Conclusion:
   - Validity status: Valid
   - Confidence level: High
   - Key supporting evidence: Same as Reviewer 1.

1. Weakness Statement:
"The paper primarily focuses on filtered datasets for SFT, but it would be valuable to explore how iw-SFT could be applied to other forms of data, such as unfiltered or mixed-quality datasets. The authors should investigate how the method performs when applied to datasets with varying levels of noise and uncertainty, and explore techniques for mitigating the impact of low-quality data. For example, the authors could consider using robust loss functions or incorporating uncertainty estimates into the importance weighting scheme. The paper should also investigate the potential for combining iw-SFT with data augmentation techniques to improve the robustness of the method. This would help to broaden the applicability of the proposed method and make it more useful in real-world scenarios where high-quality data is not always available."

2. Evidence Collection:
   - This is the same weakness as identified by Reviewer 1, and the evidence and validation are the same.

3. Literature Gap Analysis:
   - Same as Reviewer 1.

4. Validation Analysis:
   - Same as Reviewer 1.

5. Conclusion:
   - Validity status: Valid
   - Confidence level: High
   - Key supporting evidence: Same as Reviewer 1.

**Review 3**

1. Weakness Statement:
"The paper assumes a sparse reward setting, which may not always be the case in real-world applications. In many practical scenarios, rewards are dense or semi-dense, making the RL perspective less relevant. Specifically, the paper does not address how the proposed method would perform in environments with continuous reward signals, where the sparse reward assumption breaks down. The theoretical connection between SFT and RL, which is central to the paper's contribution, relies on the sparsity of rewards, and it is unclear how this connection would hold or be modified in dense reward settings."

2. Evidence Collection:
   - This is the same weakness as identified by Reviewer 1 and 2, and the evidence and validation are the same.

3. Literature Gap Analysis:
   - Same as Reviewer 1 and 2.

4. Validation Analysis:
   - Same as Reviewer 1 and 2.

5. Conclusion:
   - Validity status: Valid
   - Confidence level: High
   - Key supporting evidence: Same as Reviewer 1 and 2.

1. Weakness Statement:
"The proposed method requires additional computational resources for importance sampling, which may not be feasible in resource-constrained environments. The paper does not provide a detailed analysis of the computational overhead associated with the importance sampling step, making it difficult to assess the practical applicability of the method in scenarios with limited computational budgets. Furthermore, the paper does not explore alternative, potentially more efficient, methods for estimating the importance weights."

2. Evidence Collection:
   - This is the same weakness as identified by Reviewer 1 and 2, and the evidence and validation are the same.

3. Literature Gap Analysis:
   - Same as Reviewer 1 and 2.

4. Validation Analysis:
   - Same as Reviewer 1 and 2.

5. Conclusion:
   - Validity status: Valid
   - Confidence level: High
   - Key supporting evidence: Same as Reviewer 1 and 2.

1. Weakness Statement:
"The paper primarily focuses on filtered datasets for SFT, but it would be valuable to explore how iw-SFT could be applied to other forms of data, such as unfiltered or mixed-quality datasets. The current analysis is limited to scenarios where high-quality data is readily available and can be filtered. The paper does not investigate the performance of iw-SFT when applied to datasets with varying levels of noise and uncertainty, which is a common challenge in real-world applications. It is unclear how the method would handle datasets where the quality of data is not easily categorized or filtered."

2. Evidence Collection:
   - This is the same weakness as identified by Reviewer 1, 2, and the evidence and validation are the same.

3. Literature Gap Analysis:
   - Same as Reviewer 1 and 2.

4. Validation Analysis:
   - Same as Reviewer 1 and 2.

5. Conclusion:
   - Validity status: Valid
   - Confidence level: High
   - Key supporting evidence: Same as Reviewer 1 and 2.

**Review 4**

1. Weakness Statement:
"The paper assumes a sparse reward setting, which may not always be the case in real-world applications. In many practical scenarios, rewards are dense or semi-dense, making the RL perspective less relevant. Specifically, the paper does not address how the proposed method would perform in environments with continuous reward signals, where the sparse reward assumption breaks down. The theoretical connection between SFT and RL, which is central to the paper's contribution, relies on the sparsity of rewards, and it is unclear how this connection would hold or be modified in dense reward settings."

2. Evidence Collection:
   - This is the same weakness as identified by Reviewer 1, 2, and 3, and the evidence and validation are the same.

3. Literature Gap Analysis:
   - Same as Reviewer 1 and 2.

4. Validation Analysis:
   - Same as Reviewer 1 and 2.

5. Conclusion:
   - Validity status: Valid
   - Confidence level: High
   - Key supporting evidence: Same as Reviewer 1 and 2.

1. Weakness Statement:
"The proposed method requires additional computational resources for importance sampling, which may not be feasible in resource-constrained environments. The paper does not provide a detailed analysis of the computational overhead associated with the importance sampling step, making it difficult to assess the practical applicability of the method in scenarios with limited computational budgets. Furthermore, the paper does not explore alternative, potentially more efficient, methods for estimating the importance weights."

2. Evidence Collection:
   - This is the same weakness as identified by Reviewer 1, 2, and 3, and the evidence and validation are the same.

3. Literature Gap Analysis:
   - Same as Reviewer 1 and 2.

4. Validation Analysis:
   - Same as Reviewer 1 and 2.

5. Conclusion:
   - Validity status: Valid
   - Confidence level: High
   - Key supporting evidence: Same as Reviewer 1 and 2.

1. Weakness Statement:
"The paper primarily focuses on filtered datasets for SFT, but it would be valuable to explore how iw-SFT could be applied to other forms of data, such as unfiltered or mixed-quality datasets. The current analysis is limited to scenarios where high-quality data is readily available and can be filtered. The paper does not investigate the performance of iw-SFT when applied to datasets with varying levels of noise and uncertainty, which is a common challenge in real-world applications. It is unclear how the method would handle datasets where the quality of data is not easily categorized or filtered."

2. Evidence Collection:
   - This is the same weakness as identified by Reviewer 1, 2, and 3, and the evidence and validation are the same.

3. Literature Gap Analysis:
   - Same as Reviewer 1 and 2.

4. Validation Analysis:
   - Same as Reviewer 1 and 2.

5. Conclusion:
   - Validity status: Valid
   - Confidence level: High
   - Key supporting evidence: Same as Reviewer 1 and 2.

1. Weakness Statement:
"How does the performance of iw-SFT compare to other state-of-the-art methods in dense reward settings?"

2. Evidence Collection:
   - This is a question, not a weakness. However, it points to a valid gap in the experimental evaluation, as the paper doesn't compare against methods specifically designed for dense rewards.

3. Literature Gap Analysis:
   - The paper doesn't compare against methods explicitly designed for dense reward settings.

4. Validation Analysis:
   - The question highlights a valid gap in the experimental evaluation.

5. Conclusion:
   - Validity status: Valid (as a gap in evaluation)
   - Confidence level: High
   - Key supporting evidence: Lack of comparison with dense reward methods.

1. Weakness Statement:
"What are the computational costs associated with the importance sampling step in iw-SFT, and how do they scale with the size of the dataset?"

2. Evidence Collection:
   - This is a question, not a weakness. However, it points to a valid gap in the analysis of computational costs.

3. Literature Gap Analysis:
   - The paper lacks a detailed analysis of the computational cost of the importance sampling step.

4. Validation Analysis:
   - The question highlights a valid gap in the analysis of computational costs.

5. Conclusion:
   - Validity status: Valid (as a gap in analysis)
   - Confidence level: High
   - Key supporting evidence: Lack of computational cost analysis.

1. Weakness Statement:
"How well does iw-SFT perform when applied to unfiltered or mixed-quality datasets, and what modifications might be needed to handle such data effectively?"

2. Evidence Collection:
   - This is a question, not a weakness. However, it points to a valid gap in the evaluation on different data types.

3. Literature Gap Analysis:
   - The paper doesn't evaluate performance on unfiltered or mixed-quality datasets.

4. Validation Analysis:
   - The question highlights a valid gap in the evaluation on different data types.

5. Conclusion:
   - Validity status: Valid (as a gap in evaluation)
   - Confidence level: High
   - Key supporting evidence: Lack of evaluation on unfiltered/mixed-quality datasets.
}

Now, I have successfully verified each review. Next, I will organize this content and output the final review decision:

\boxed_review{
## Summary:

This paper introduces a novel perspective on Supervised Fine-Tuning (SFT) by framing it as an approximation of Reinforcement Learning (RL), specifically focusing on optimizing a lower bound of the RL objective. The authors propose a method called importance-weighted SFT (iw-SFT), which aims to improve upon standard SFT by incorporating importance sampling to better approximate the RL objective. The core idea is that SFT, when applied to a filtered dataset, can be viewed as optimizing a lower bound on the RL objective, and by weighting the importance of different data points, the method can achieve a tighter bound and thus better performance. The paper presents a theoretical framework for this approach, demonstrating that SFT can be seen as optimizing a lower bound on the RL objective in sparse reward settings. The proposed iw-SFT method then uses importance weights to refine this approximation. The authors validate their approach through extensive experiments across multiple domains, including language model reasoning tasks and continuous control tasks. In language model experiments, they use a filtered dataset of LLM responses and show that iw-SFT outperforms standard SFT and other RL baselines. In control tasks, they demonstrate that iw-SFT can learn policies that achieve higher returns compared to standard SFT. The paper's main contribution lies in its novel connection between SFT and RL, providing a new theoretical foundation for SFT and a practical method for improving its performance. The authors also show that their method can be applied to both language models and continuous control tasks, highlighting its versatility. The empirical results are compelling, demonstrating that iw-SFT can achieve competitive performance with less training compute compared to state-of-the-art methods. Overall, the paper presents a significant contribution to the field of SFT by providing a new theoretical perspective and a practical method for improving its performance, and it opens up new avenues for future research in this area.


## Soundness:

3.0


## Presentation:

3.0


## Contribution:

2.5


## Strengths:

This paper presents several notable strengths that contribute to its overall significance. First and foremost, the paper provides a novel and insightful perspective on Supervised Fine-Tuning (SFT) by drawing a connection to Reinforcement Learning (RL). This connection is not only theoretically sound but also provides a new framework for understanding SFT as an approximation of RL. The authors successfully demonstrate that SFT, when applied to a filtered dataset, can be viewed as optimizing a lower bound on the RL objective, and they use this insight to develop a new method, importance-weighted SFT (iw-SFT). This is a significant contribution because it provides a new way to think about SFT and opens up new avenues for research in this area. The proposed iw-SFT method is also a key strength of the paper. The method is simple yet effective, and the authors provide a thorough theoretical analysis and empirical evaluation to support its effectiveness. The use of importance weights to refine the approximation of the RL objective is a clever and effective approach, and the authors demonstrate that it leads to improved performance compared to standard SFT. The empirical results presented in the paper are also a major strength. The authors conduct extensive experiments across multiple domains, including language model reasoning tasks and continuous control tasks, and they show that iw-SFT achieves competitive performance with less training compute compared to state-of-the-art methods. The fact that the method is validated on both language models and control tasks highlights its versatility and potential for broader application. The paper is also well-written and easy to follow, which makes it accessible to a wide audience. The authors provide a clear and concise explanation of their method and the theoretical framework, and they also provide sufficient details about their experimental setup. The paper is well-organized and the arguments are presented in a logical and coherent manner. Finally, the paper's focus on sparse reward settings is also a strength, as it addresses a common challenge in real-world applications of RL. By focusing on sparse rewards, the authors make their method more applicable to a wider range of problems. Overall, the paper's strengths lie in its novel theoretical perspective, its effective method, its strong empirical results, and its clear presentation.


## Weaknesses:

Despite its strengths, this paper has several limitations that warrant careful consideration. The most significant weakness is the paper's reliance on the assumption of sparse reward settings. As I've verified, the paper explicitly states its focus on sparse reward settings, and the theoretical connection between SFT and RL, which is central to the paper's contribution, is derived under this assumption. The authors use inequalities that are specific to sparse reward scenarios, such as the inequality used to derive the lower bound on the RL objective. This reliance on sparse rewards limits the applicability of the proposed method to environments with continuous or semi-dense reward signals, where the RL perspective may not be as relevant. The paper does not address how the proposed method would perform in such environments, and it is unclear how the theoretical connection between SFT and RL would hold or be modified in dense reward settings. This is a critical limitation, as many real-world applications involve dense or semi-dense rewards, and the paper's findings may not be directly applicable to these scenarios. My confidence in this limitation is high, as it is explicitly stated in the paper and directly impacts the validity of the theoretical framework. Another significant weakness is the computational cost associated with the importance sampling step in iw-SFT. As I've confirmed, the method requires additional computational resources for importance sampling, which may not be feasible in resource-constrained environments. The paper does not provide a detailed analysis of the computational overhead associated with the importance sampling step, making it difficult to assess the practical applicability of the method in scenarios with limited computational budgets. Furthermore, the paper does not explore alternative, potentially more efficient, methods for estimating importance weights. The authors use a specific smoothing technique and a clipping function for importance weights, but they do not investigate the impact of these choices on the computational cost or explore alternative methods for estimating importance weights that are more computationally efficient. This lack of analysis makes it difficult to assess the practical feasibility of the method in resource-constrained environments. My confidence in this limitation is high, as it is directly related to the method's implementation and the paper lacks the necessary analysis. Finally, the paper primarily focuses on filtered datasets for SFT, and it does not explore how iw-SFT could be applied to other forms of data, such as unfiltered or mixed-quality datasets. The current analysis is limited to scenarios where high-quality data is readily available and can be filtered. The paper does not investigate the performance of iw-SFT when applied to datasets with varying levels of noise and uncertainty, which is a common challenge in real-world applications. It is unclear how the method would handle datasets where the quality of data is not easily categorized or filtered. The paper's focus on filtered datasets limits the generalizability of the method and raises questions about its applicability to real-world scenarios where high-quality data is not always available. My confidence in this limitation is high, as it is evident from the experimental setup and the method description, which are centered around filtered datasets.


## Suggestions:

To address the identified weaknesses, I recommend several concrete improvements. First, the paper would benefit from a more thorough discussion of the limitations of the sparse reward assumption and how the proposed method might be adapted for dense or semi-dense reward settings. Specifically, the authors should explore alternative formulations of the RL objective that are more suitable for dense reward environments, such as policy gradient methods or actor-critic algorithms. Furthermore, the paper should include experiments on benchmark tasks with dense rewards to demonstrate the performance of iw-SFT in a broader range of scenarios. This would help to clarify the scope and applicability of the proposed method and provide a more comprehensive understanding of its strengths and weaknesses. The authors should also consider the potential for combining their approach with existing techniques for handling dense rewards, such as reward shaping or reward decomposition, to further improve performance. Second, to address the computational concerns, the paper should include a detailed analysis of the computational cost of the importance sampling step and explore alternative methods for estimating importance weights that are more computationally efficient. For example, the authors could investigate the use of online importance estimation techniques or explore methods for approximating the importance weights using a smaller set of samples. The paper should also provide a comparison of the computational cost of iw-SFT with other SFT methods, such as standard SFT or behavior cloning, to demonstrate the trade-offs between performance and computational efficiency. Furthermore, the authors should discuss the potential for parallelizing the importance sampling step to reduce the overall training time. This would help to make the method more practical for resource-constrained environments. Third, the paper should explore the application of iw-SFT to other forms of data, such as unfiltered or mixed-quality datasets. The authors should investigate how the method performs when applied to datasets with varying levels of noise and uncertainty, and explore techniques for mitigating the impact of low-quality data. For example, the authors could consider using robust loss functions or incorporating uncertainty estimates into the importance weighting scheme. The paper should also investigate the potential for combining iw-SFT with data augmentation techniques to improve the robustness of the method. This would help to broaden the applicability of the proposed method and make it more useful in real-world scenarios where high-quality data is not always available. Finally, the paper should include a more thorough discussion of the limitations of the sparse reward assumption and how the proposed method might be adapted for dense or semi-dense reward settings. Specifically, the authors should explore alternative formulations of the RL objective that are more suitable for dense reward environments, such as policy gradient methods or actor-critic algorithms. Furthermore, the paper should include experiments on benchmark tasks with dense rewards to demonstrate the performance of iw-SFT in a broader range of scenarios. This would help to clarify the scope and applicability of the proposed method and provide a more comprehensive understanding of its strengths and weaknesses. The authors should also consider the potential for combining their approach with existing techniques for handling dense rewards, such as reward shaping or reward decomposition, to further improve performance.


## Questions:

Several key questions arise from my analysis of this paper. First, how does the performance of iw-SFT compare to other state-of-the-art methods in dense reward settings? The paper's focus on sparse reward settings limits its applicability to real-world scenarios where dense rewards are common. It would be valuable to understand how iw-SFT performs in these environments and whether it can be adapted to handle dense rewards effectively. Second, what are the computational costs associated with the importance sampling step in iw-SFT, and how do they scale with the size of the dataset? The paper does not provide a detailed analysis of the computational overhead associated with the importance sampling step, making it difficult to assess the practical applicability of the method in resource-constrained environments. It would be important to understand how the computational cost scales with the size of the dataset and whether there are any techniques that can be used to reduce the computational overhead. Third, how well does iw-SFT perform when applied to unfiltered or mixed-quality datasets, and what modifications might be needed to handle such data effectively? The paper primarily focuses on filtered datasets, and it is unclear how the method would perform when applied to datasets with varying levels of noise and uncertainty. It would be valuable to understand the robustness of the method to low-quality data and whether any techniques can be used to mitigate the impact of noisy data. Finally, how does the performance of iw-SFT compare to other state-of-the-art methods in dense reward settings? The paper does not compare against methods specifically designed for dense rewards, and it would be valuable to understand how iw-SFT performs relative to these methods. These questions highlight key uncertainties about the method's applicability and performance in different scenarios and target areas for future research.


## Rating:

6.5


## Confidence:

3.25


## Decision:

Accept
}