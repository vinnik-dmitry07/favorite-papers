I will use Standard Mode for comprehensive thinking. As a professional reviewer, I will simulate 4 different reviewers, followed by the verification thinking. Then I will output the Finally Review Output. Let me think - Standard Mode means I will output the original review, followed by the verification thinking. Considering that I am currently in standard mode, I should think from my existing knowledge and consider some related work content when writing about weaknesses. Then I will output the Finally Review Output and Meta Review Output:

\boxed_simreviewers{
## Reviewer 1

### Summary

This paper studies how language models learn to solve grade-school math problems. They propose a synthetic dataset iGSM, which is similar to GSM8K, but is easier to analyze and generate in large quantities. They then study the model's behavior using probing tasks to understand how the model solves the problems. They also study how the model generalizes to harder problems than it is trained on.

### Soundness

2

### Presentation

3

### Contribution

2

### Strengths

The paper studies an interesting question, and the experimental setup seems reasonable. The paper is also well-written and easy to follow.

### Weaknesses

#### Some Related Works


#### comment

The main weakness of the paper is that the proposed dataset is too similar to GSM8K, which makes it difficult to understand the value of the dataset. The paper does not provide a detailed analysis of the differences between the two datasets, beyond the fact that iGSM is easier to analyze and generate in large quantities. It would be helpful to see a more rigorous comparison of the types of problems, the distribution of operations, and the complexity of the mathematical reasoning required in both datasets. For example, are there specific types of arithmetic operations or problem structures that are more prevalent in iGSM compared to GSM8K? A deeper dive into these aspects would help clarify the unique contributions of the iGSM dataset.

Another weakness is that the paper does not provide a clear picture of the model's behavior. The probing tasks are not well-motivated, and it is not clear how they relate to the actual problem-solving process. The paper should provide a more detailed explanation of why these specific probing tasks were chosen and how they can help us understand the model's reasoning. For instance, what specific cognitive skills are being probed by each task, and how do these tasks relate to the steps involved in solving grade-school math problems? Additionally, the paper does not provide a clear explanation of how the model's behavior is analyzed based on the probing results. It would be helpful to see a more detailed description of the analysis methodology and how the results are interpreted.

### Suggestions

To address the concerns about the similarity between iGSM and GSM8K, the authors should provide a more detailed comparative analysis of the two datasets. This analysis should go beyond a simple comparison of the number of problems and should focus on the specific characteristics of the problems themselves. For example, the authors could analyze the distribution of different types of arithmetic operations (e.g., addition, subtraction, multiplication, division) in both datasets, as well as the complexity of the mathematical reasoning required to solve the problems. They could also analyze the structure of the problems, such as the number of steps involved in the solution process and the types of intermediate calculations that are needed. This analysis could be presented in the form of tables or graphs that clearly show the differences between the two datasets. Furthermore, the authors should provide a clear explanation of why iGSM is a more suitable dataset for studying the reasoning abilities of language models compared to GSM8K. This explanation should focus on the specific features of iGSM that make it easier to analyze and generate in large quantities, as well as the specific advantages it offers for studying the model's reasoning process.

To improve the clarity of the model's behavior, the authors should provide a more detailed motivation for the probing tasks and explain how they relate to the actual problem-solving process. The authors should clearly state the specific cognitive skills that each probing task is designed to measure and explain how these skills are relevant to the steps involved in solving grade-school math problems. For example, if a probing task is designed to measure the model's ability to identify the relevant variables in a problem, the authors should explain why this is an important skill for problem-solving and how it relates to the actual solution process. The authors should also provide a more detailed description of the analysis methodology used to interpret the results of the probing tasks. This description should include a clear explanation of how the results are analyzed and how the conclusions are drawn. The authors should also provide examples of how the probing tasks are used to understand the model's behavior in specific problem-solving scenarios. This would help to make the analysis more concrete and easier to understand.

Finally, the authors should provide a more detailed discussion of the limitations of their approach and suggest directions for future research. This discussion should include a clear explanation of the assumptions that are made in the study and the potential impact of these assumptions on the results. The authors should also discuss the potential limitations of the probing tasks and the extent to which these tasks can capture the full range of the model's reasoning abilities. Furthermore, the authors should suggest specific directions for future research that could address the limitations of the current study and provide a more comprehensive understanding of how language models learn to solve grade-school math problems. This could include exploring the use of more diverse datasets, developing more sophisticated probing tasks, and investigating the impact of different training strategies on the model's reasoning abilities.

### Questions

1. How does the proposed dataset differ from GSM8K? If there are no significant differences, then why is iGSM a better dataset for studying the reasoning abilities of language models?

2. What are the probing tasks motivated by? How do they relate to the actual problem-solving process?

### Rating

5

### Confidence

4

**********

## Reviewer 2

### Summary

The paper proposes a synthetic dataset, iGSM, for studying how language models solve grade-school math problems. The dataset is designed to be free from data contamination and to have a large number of diverse problems. The authors use the dataset to train a GPT-2 model and conduct various experiments to understand the model's reasoning process, generalization ability, and error analysis.

### Soundness

3

### Presentation

3

### Contribution

3

### Strengths

1. The paper is well-written and easy to follow.
2. The proposed dataset, iGSM, is a valuable contribution to the field of mathematical reasoning in language models. The dataset is designed to be free from data contamination and to have a large number of diverse problems.
3. The authors conduct various experiments to understand the model's reasoning process, generalization ability, and error analysis. The findings provide valuable insights into how language models solve grade-school math problems.

### Weaknesses

#### Some Related Works


#### comment

1. The paper focuses on a specific type of math problem, namely grade-school math. It would be interesting to see how the findings generalize to other types of math problems, such as algebra or calculus. The current scope limits the broader applicability of the conclusions, as the reasoning processes involved in solving different mathematical domains may vary significantly. For instance, algebraic manipulation requires understanding of variables and equations, while calculus involves limits, derivatives, and integrals, all of which are not addressed in this study.
2. The paper only considers a single model architecture, GPT-2. It would be interesting to see how the findings generalize to other model architectures, such as LLaMA or T5. The conclusions may not hold for other model architectures, as different architectures may have different inductive biases and training procedures that affect their ability to learn and generalize mathematical reasoning. For example, models with different attention mechanisms or layer normalization techniques might exhibit different behaviors when presented with mathematical problems.
3. The paper does not provide a clear definition of what constitutes a "reasoning skill" in the context of math problem solving. The authors use terms like "level-1" and "level-2" reasoning skills, but it is not clear what these terms mean in a precise way. This lack of clarity makes it difficult to interpret the results and compare them with other studies. A more rigorous definition of reasoning skills is needed to ensure the reproducibility and comparability of the findings.

### Suggestions

To address the limitation of focusing solely on grade-school math, the authors should consider expanding their analysis to include more complex mathematical domains, such as algebra or calculus. This would involve creating new synthetic datasets that cover a wider range of mathematical concepts and problem types. For example, the dataset could include problems involving solving linear equations, quadratic equations, or basic calculus problems like finding derivatives or integrals. By doing so, the authors could gain a better understanding of how language models generalize their reasoning abilities across different mathematical domains. Furthermore, this would increase the practical relevance of their findings, as mathematical reasoning is a crucial skill in many real-world applications.

To address the limitation of using only the GPT-2 architecture, the authors should investigate how their findings generalize to other model architectures, such as LLaMA or T5. This would involve training and evaluating these models on the same synthetic datasets and analyzing their performance in terms of reasoning accuracy, generalization ability, and error patterns. By comparing the results across different architectures, the authors could identify the key factors that influence a model's ability to learn and generalize mathematical reasoning. For example, they could investigate whether models with different attention mechanisms or layer normalization techniques exhibit different behaviors when presented with mathematical problems. This would provide valuable insights into the design of more effective models for mathematical reasoning.

Finally, to address the lack of a clear definition of "reasoning skills," the authors should provide a more rigorous and precise definition of these terms. They could start by identifying the specific cognitive processes involved in solving mathematical problems, such as symbolic manipulation, logical deduction, and pattern recognition. Then, they could define "reasoning skills" in terms of these cognitive processes, perhaps by categorizing them into different levels of complexity. For example, they could define "level-1" reasoning skills as those that involve simple arithmetic operations, while "level-2" reasoning skills involve more complex operations, such as solving equations or manipulating algebraic expressions. By providing a clear and precise definition of reasoning skills, the authors could make their results more interpretable and comparable with other studies.

### Questions

1. How do the findings of this paper generalize to other types of math problems, such as algebra or calculus?
2. How do the findings of this paper generalize to other model architectures, such as LLaMA or T5?
3. What is the precise definition of a "reasoning skill" in the context of math problem solving?

### Rating

6

### Confidence

4

**********

## Reviewer 3

### Summary

The paper proposes a new dataset for mathematical reasoning, iGSM, and uses it to study the reasoning abilities of language models. The dataset is synthetic and designed to be free of data contamination. The authors use the dataset to train a GPT-2 model and conduct various experiments to understand the model's reasoning process, generalization ability, and error analysis. The findings reveal that language models can learn math skills aligned with human cognitive processes and even acquire new reasoning skills beyond what is needed for learning the pretraining data.

### Soundness

3

### Presentation

3

### Contribution

3

### Strengths

- The paper addresses an important and timely question about the reasoning abilities of language models, particularly in the context of mathematical problem-solving.
- The proposed dataset, iGSM, is a valuable contribution to the field, as it is designed to be free from data contamination and allows for controlled experimentation.
- The paper provides a comprehensive analysis of the model's reasoning process, including its generalization ability and error analysis. The findings are insightful and shed light on the capabilities and limitations of language models in mathematical reasoning.

### Weaknesses

#### Some Related Works


#### comment

 - The paper primarily focuses on the GPT-2 architecture, and it would be beneficial to see how the findings generalize to other model architectures, such as LLaMA or T5. The conclusions may not hold for other model architectures, as different architectures may have different inductive biases and training procedures that affect their ability to learn and generalize mathematical reasoning.
- The paper does not provide a clear definition of what constitutes a "reasoning skill" in the context of math problem solving. The authors use terms like "level-1" and "level-2" reasoning skills, but it is not clear what these terms mean in a precise way. This lack of clarity makes it difficult to interpret the results and compare them with other studies. A more rigorous definition of reasoning skills is needed to ensure the reproducibility and comparability of the findings.

### Suggestions

The authors should consider expanding their analysis to include a wider range of model architectures to assess the generalizability of their findings. Specifically, they could explore models like LLaMA or T5, which have different architectural designs and training methodologies. This would involve training these models on the proposed iGSM dataset and evaluating their performance on a held-out set of mathematical reasoning problems. By comparing the results across different architectures, the authors could identify the key factors that influence a model's ability to learn and generalize mathematical reasoning. For example, they could investigate whether models with different attention mechanisms or layer normalization techniques exhibit different behaviors when presented with mathematical problems. This would provide a more comprehensive understanding of the capabilities and limitations of language models in this domain.

Furthermore, the authors need to provide a more rigorous and precise definition of "reasoning skills" in the context of mathematical problem-solving. The current use of terms like "level-1" and "level-2" reasoning skills is insufficient for a clear understanding of the model's reasoning process. They should define these skills in terms of specific cognitive processes, such as symbolic manipulation, logical deduction, and pattern recognition. For instance, they could categorize reasoning skills based on the complexity of the operations involved, ranging from simple arithmetic to more complex algebraic manipulations. This would allow for a more systematic analysis of the model's reasoning abilities and facilitate comparisons with other studies. The authors could also consider using a more formal framework for defining reasoning skills, such as those based on computational models of reasoning.

Finally, the authors should provide a more detailed analysis of the model's error patterns. While they mention that the model makes errors due to backward reasoning, they should provide a more in-depth analysis of the types of errors made and the circumstances under which these errors occur. For example, they could categorize errors based on the type of mathematical operation involved or the complexity of the problem. They could also investigate whether the model's errors are related to specific aspects of the model's architecture or training process. This would provide valuable insights into the model's limitations and suggest directions for future research. Additionally, the authors should explore the relationship between the model's reasoning depth and its performance on different types of mathematical problems. This could involve analyzing the model's behavior on problems with varying levels of complexity and identifying the factors that contribute to its success or failure.

### Questions

- How do the findings of this paper generalize to other types of math problems, such as algebra or calculus?
- How do the findings of this paper generalize to other model architectures, such as LLaMA or T5?
- What is the precise definition of a "reasoning skill" in the context of math problem solving?

### Rating

8

### Confidence

3

**********

## Reviewer 4

### Summary

This paper introduces a synthetic dataset, iGSM, to study how language models learn to solve grade-school math problems. The dataset is designed to be free from data contamination and allows for controlled experimentation. The authors train a GPT-2 model on iGSM and conduct various experiments to understand the model's reasoning process, generalization ability, and error analysis. The findings reveal that language models can learn math skills aligned with human cognitive processes and even acquire new reasoning skills beyond what is needed for learning the pretraining data.

### Soundness

3

### Presentation

3

### Contribution

3

### Strengths

- The paper addresses an important and timely question about the reasoning abilities of language models, particularly in the context of mathematical problem-solving.
- The proposed dataset, iGSM, is a valuable contribution to the field, as it is designed to be free from data contamination and allows for controlled experimentation.
- The paper provides a comprehensive analysis of the model's reasoning process, including its generalization ability and error analysis. The findings are insightful and shed light on the capabilities and limitations of language models in mathematical reasoning.

### Weaknesses

#### Some Related Works


#### comment

 - The paper primarily focuses on the GPT-2 architecture, and it would be beneficial to see how the findings generalize to other model architectures, such as LLaMA or T5. The conclusions may not hold for other model architectures, as different architectures may have different inductive biases and training procedures that affect their ability to learn and generalize mathematical reasoning.
- The paper does not provide a clear definition of what constitutes a "reasoning skill" in the context of math problem solving. The authors use terms like "level-1" and "level-2" reasoning skills, but it is not clear what these terms mean in a precise way. This lack of clarity makes it difficult to interpret the results and compare them with other studies. A more rigorous definition of reasoning skills is needed to ensure the reproducibility and comparability of the findings.

### Suggestions

The authors should consider expanding their analysis to include a wider range of model architectures to assess the generalizability of their findings. Specifically, they could explore models like LLaMA or T5, which have different architectural designs and training methodologies. This would involve training these models on the proposed iGSM dataset and evaluating their performance on a held-out set of mathematical reasoning problems. By comparing the results across different architectures, the authors could identify the key factors that influence a model's ability to learn and generalize mathematical reasoning. For example, they could investigate whether models with different attention mechanisms or layer normalization techniques exhibit different behaviors when presented with mathematical problems. This would provide a more comprehensive understanding of the capabilities and limitations of language models in this domain.

Furthermore, the authors need to provide a more rigorous and precise definition of "reasoning skills" in the context of mathematical problem-solving. The current use of terms like "level-1" and "level-2" reasoning skills is insufficient for a clear understanding of the model's reasoning process. They should define these skills in terms of specific cognitive processes, such as symbolic manipulation, logical deduction, and pattern recognition. For instance, they could categorize reasoning skills based on the complexity of the operations involved, ranging from simple arithmetic to more complex algebraic manipulations. This would allow for a more systematic analysis of the model's reasoning abilities and facilitate comparisons with other studies. The authors could also consider using a more formal framework for defining reasoning skills, such as those based on computational models of reasoning.

Finally, the authors should provide a more detailed analysis of the model's error patterns. While they mention that the model makes errors due to backward reasoning, they should provide a more in-depth analysis of the types of errors made and the circumstances under which these errors occur. For example, they could categorize errors based on the type of mathematical operation involved or the complexity of the problem. They could also investigate whether the model's errors are related to specific aspects of the model's architecture or training process. This would provide valuable insights into the model's limitations and suggest directions for future research. Additionally, the authors should explore the relationship between the model's reasoning depth and its performance on different types of mathematical problems. This could involve analyzing the model's behavior on problems with varying levels of complexity and identifying the factors that contribute to its success or failure.

### Questions

- How do the findings of this paper generalize to other types of math problems, such as algebra or calculus?
- How do the findings of this paper generalize to other model architectures, such as LLaMA or T5?
- What is the precise definition of a "reasoning skill" in the context of math problem solving?

### Rating

8

### Confidence

3

**********

}

I have finished generating simulated reviews from 4 reviewers. Next, I will generate verification content for these reviews:

\boxed_verification{
The user wants me to validate weaknesses identified by reviewers in a given paper. I need to go through each reviewer's comments and check if the criticism is valid based on the content of the paper provided.

Here's my plan:
1. **Iterate through each reviewer's comments.**
2. **For each comment identified as a weakness:**
   - **Locate the specific claim in the reviewer's text.**
   - **Search the paper for evidence related to this claim.** This might involve looking at the method description, experimental setup, results, or related work.
   - **Determine if the reviewer's claim is supported by the paper or if there's a misunderstanding.**
   - **Provide specific quotes and section references from the paper to support my validation.**
3. **Categorize the type of weakness (methodological, experimental, etc.).**
4. **Synthesize the findings and provide a conclusion for each weakness.**
**Review 1 Weaknesses:**

1. Weakness Statement:
"The paper primarily focuses on the GPT-2 architecture, and it would be beneficial to see how the findings generalize to other model architectures, such as LLaMA or T5. The conclusions may not hold for other model architectures, as different architectures may have different inductive biases and training procedures that affect their ability to learn and generalize mathematical reasoning."

2. Evidence Collection:
a) Method-related Evidence:
   - "We use the GPT2 architecture [ 18 ] but replace its absolute positional embedding with rotary embedding [ 20 , 7 ] , yet still referring to it as GPT2 for brevity." (Section 2.4)
   - "We are currently bounded by resources to repeat all experiments in this paper with other architectures that have minor differences from GPT2-rotary for knowledge tasks [ 4 ] ." (Section 2.4)

3. Literature Gap Analysis:
   - The paper cites GPT2 [18] and mentions rotary embeddings [20, 7]. It also cites [4] which is likely the paper "Scaling laws for autoregressive generative modeling" by Brown et al.

4. Validation Analysis:
   - Primary evidence confirms the paper's focus on GPT2.
   - The authors explicitly state the limitation of not testing other architectures due to resource constraints.
   - The reviewer's concern about generalizability is valid given the single architecture used.

5. Conclusion:
   - Validity status: Valid
   - Confidence level: High
   - Key supporting evidence: Explicit statement about using GPT2 and the reason for not testing other architectures.

1. Weakness Statement:
"The paper does not provide a clear definition of what constitutes a "reasoning skill" in the context of math problem solving. The authors use terms like "level-1" and "level-2" reasoning skills, but it is not clear what these terms mean in a precise way. This lack of clarity makes it difficult to interpret the results and compare them with other studies. A more rigorous definition of reasoning skills is needed to ensure the reproducibility and comparability of the findings."

2. Evidence Collection:
a) Method-related Evidence:
   - "We use synthetic sentences to reduce the difficulty arising from Common Sense , like “a candle burned for 12 hours at 1 inch per hour” (implying the candle is reducing in length)." (Section 2.1) - This describes the data generation process but not the reasoning skills.
   - "We emphasize that: • The solution only contain parameters necessary towards calculating the final query parameter." (Section 2.4) - This describes the solution format, not reasoning skills.
   - "We also removed the difficulty from pure arithmetic: we only consider integers and arithmetic mod 23 23 to avoid errors from computation involving large numbers." (Section 2.4) - This describes the dataset filtering, not reasoning skills.
   - "We use iGSM op ≤ o p , ip ≤ i p \textsf{iGSM}^{\textsf{op}\leq op,\textsf{ip}\leq ip} to denote the data generated with constraint op ≤ o p \textsf{op}\leq op . 9 9 9 9 We choose op non-uniformly; for instance, we let op = min ⁡ { t 0 , t 1 } \textsf{op}=\min\{t_0,t_1\} for two random draws t 0 , t 1 ∈ [ o p ] t_{0},t_{1}\in[op] ." (Section 2.3) - This describes the data generation constraints, not reasoning skills.
   - "We use two parameters to control data’s difficulty: ip is the number of instance parameters, and op is the number of solution operations; the data’s difficulty is an increasing function over them. We call our dataset iGSM op = 15 \textsf{iGSM}^{\textsf{op}\leq 15} still has at least 7 7 billion solution templates to denote the data generated with constraint op ≤ 15 = def iGSM op ≤ 15 , ip ≤ 20 \textsf{iGSM}^{\textsf{op}=15,\textsf{ip}\leq 20} ." (Section 2.3) - This describes the difficulty control, not reasoning skills.
   - "We use the GPT-2 architecture [ 18 ] but replace its absolute positional embedding with rotary embedding [ 20 , 7 ] , yet still referring to it as GPT2 for brevity." (Section 2.4) - This describes the model architecture, not reasoning skills.
   - "We are currently bounded by resources to repeat all experiments in this paper with other architectures that have minor differences from GPT2-rotary for knowledge tasks [ 4 ] ." (Section 2.4) - This acknowledges the limitation.
   - "Result 7 (Figure 9). Language model depth is crucial, likely due to the complexity of its hidden (mental) reasoning processes. A t t -step mental reasoning, such as mentally computing nece ss t e p ( A ) \texttt{nece\_step}(A) for parameters A A that are a distance t t from the query, may require deeper models for larger t t , assuming all other hyperparameters remain constant." (Section 6) - This discusses the impact of model depth, which is related to reasoning, but not a defined "reasoning skill".

3. Literature Gap Analysis:
   - The paper cites relevant works on reasoning in language models.

4. Validation Analysis:
   - The reviewer is correct that the paper doesn't provide a formal definition of "reasoning skill."
   - The terms "level-1" and "level-2" are used in the context of probing tasks (Section 4.1), but not as a standalone definition of reasoning skills.
   - The paper focuses on analyzing the model's behavior through probing tasks rather than defining fundamental reasoning skills.

5. Conclusion:
   - Validity status: Valid
   - Confidence level: High
   - Key supporting evidence: Absence of a dedicated definition of "reasoning skill" and the use of the term primarily in the context of probing tasks.

**Review 2 Weaknesses:**

1. Weakness Statement:
"The main weakness of the paper is that the proposed dataset is too similar to GSM8K, which makes it difficult to understand the value of the dataset. The paper does not provide a detailed analysis of the differences between the two datasets, beyond the fact that iGSM is easier to analyze and generate in large quantities. It would be helpful to see a more rigorous comparison of the types of problems, the distribution of operations, and the complexity of the mathematical reasoning required in both datasets. For example, are there specific types of arithmetic operations or problem structures that are more prevalent in iGSM compared to GSM8K? A deeper dive into these aspects would help clarify the unique contributions of the iGSM dataset."

2. Evidence Collection:
a) Method-related Evidence:
   - "Motivated by this, we build a GSM8K-like math dataset through a synthetic generation pipeline that captures the dependencies of parameters." (Section 2.1) - This explicitly states the inspiration from GSM8K.
   - "We use synthetic sentences to reduce the difficulty arising from Common Sense , like “a candle burned for 12 hours at 1 inch per hour” (implying the candle is reducing in length)." (Section 2.1) - This describes a specific aspect of the dataset generation that differs from standard math problems.
   - "We emphasize that: • The solution only contain parameters necessary towards calculating the final query parameter." (Section 2.4) - This is a key difference from GSM8K.
   - "We also removed the difficulty from pure arithmetic: we only consider integers and arithmetic mod 23 23 to avoid errors from computation involving large numbers." (Section 2.4) - This is a filtering step not explicitly mentioned for GSM8K.
   - "We use iGSM op ≤ o p , ip ≤ i p \textsf{iGSM}^{\textsf{op}\leq op,\textsf{ip}\leq ip} to denote the data generated with constraint op ≤ o p \textsf{op}\leq op . 9 9 9 9 We choose op non-uniformly; for instance, we let op = min ⁡ { t 0 , t 1 } \textsf{op}=\min\{t_0,t_1\} for two random draws t 0 , t 1 ∈ [ o p ] t_{0},t_{1}\in[op] ." (Section 2.3) - This describes a constraint on the number of operations, which is not explicitly mentioned for GSM8K.
   - "We use two parameters to control data’s difficulty: ip is the number of instance parameters, and op is the number of solution operations; the data’s difficulty is an increasing function over them. We call our dataset iGSM op = 15 \textsf{iGSM}^{\textsf{op}\leq 15} still has at least 7 7 billion solution templates to denote the data generated with constraint op ≤ 15 = def iGSM op ≤ 15 , ip ≤ 20 \textsf{iGSM}^{\textsf{op}=15,\textsf{ip}\leq 20} ." (Section 2.3) - This describes a difficulty control mechanism, potentially different from GSM8K.
   - "We use the GPT-2 architecture [ 18 ] but replace its absolute positional embedding with rotary embedding [ 20 , 7 ] , yet still referring to it as GPT2 for brevity." (Section 2.4) - This describes a model choice, not a dataset difference.
   - "We are currently bounded by resources to repeat all experiments in this paper with other architectures that have minor differences from GPT2-rotary for knowledge tasks [ 4 ] ." (Section 2.4) - This acknowledges the limitation.
   - "Result 1: Data Generation. After sufficient pre-training, we give the model a problem from the test set (without solution) and let it continue to generate (allegedly a solution followed by an answer). Because we have restricted ourselves to a fixed solution format, language models can learn the format easily, allowing us to write a solution parser to check if the solution is fully correct. 1. We perform OOD evaluation such as on op ≥ 28 \textsf{op}\geq 28 while providing only op ≤ 21 \textsf{op}\leq 21 training samples." (Section 3) - This describes a test-time generation capability, which could be a difference.
   - "We train with data whose hash value of solution template (see Footnote 11 ) is < 17 ( mod 23 ) <17\pmod{23} , and test with those ≥ 17 \geq 17 . This ensures no template-level overlap between training and testing ." (Section 3) - This describes a data split strategy, potentially different from GSM8K.

4. Validation Analysis:
   - The paper explicitly states the inspiration from GSM8K but also details several differences in the dataset generation process, including the synthetic sentence structure, the constraint on the number of operations, and the mod 23 arithmetic. The OOD evaluation setup is also a differentiating factor. While the paper doesn't provide a direct, side-by-side comparison table, it does describe these differences.

5. Conclusion:
   - Validity status: Partially Valid
   - Confidence level: Medium
   - Key supporting evidence: The paper acknowledges inspiration from GSM8K but also details several methodological differences in the data generation process. However, a direct, detailed comparison table would strengthen the argument.

1. Weakness Statement:
"Another weakness is that the paper does not provide a clear picture of the model's behavior. The probing tasks are not well-motivated, and it is not clear how they relate to the actual problem-solving process. The paper should provide a more detailed explanation of why these specific probing tasks were chosen and how they can help us understand the model's reasoning. For instance, what specific cognitive skills are being probed by each task, and how do these tasks relate to the steps involved in solving grade-school math problems? Additionally, the paper does not provide a clear explanation of how the model's behavior is analyzed based on the probing results. It would be helpful to see a more detailed description of the analysis methodology and how the results are interpreted."

2. Evidence Collection:
a) Method-related Evidence:
   - "To understand how the model learns to solve math problems, we propose studying the following probing tasks, which align closely with human problem-solving strategies: • nece ( A ) \texttt{nece}(A) : if parameter A A is necessary for computing the final query parameter." (Section 4.1) - This states the motivation for the probing task.
   - "dece ( A , B ) \texttt{dece}(A,B) : if parameter A A (recursively) depends on parameter B B given the problem statement." (Section 4.1) - This describes the dependence probing task.
   - "known ( A ) \texttt{known}(A) : if parameter A A has already been computed." (Section 4.1) - This describes the known parameter probing task.
   - "value ( A ) \texttt{value}(A) : the value of parameter A A (a number between 0-22, or 23 if known A ) \texttt{value}(A) \texttt{value}(A) ." (Section 4.1) - This describes the value prediction task.
   - "can_next ( A ) \texttt{can\_next}(A) \texttt{can\_next}(A) : if A A can be computed in the next solution sentence (namely, its predecessors have all been calculated)." (Section 4.1) - This describes the next solution sentence prediction task.
   - "nece_next ( A ) \texttt{nece\_next}(A) \texttt{nece\_next}(A) : if parameter A A satisfies both can\_next ( A ) \texttt{can\_next}(A) and nece ( A ) \texttt{nece}(A) ." (Section 4.1) - This describes the combined probing task.
   - "dece_next ( A ) \texttt{dece\_next}(A) \texttt{dece\_next}(A) : if parameter A A satisfies both can\_next ( A ) \texttt{can\_next}(A) and dece ( A ) \texttt{dece}(A) ." (Section 4.1) - This describes the combined probing task.
   - "The probing tasks are designed to align closely with human problem-solving strategies: nece(A) checks if parameter A is necessary for the final answer, dece(A, B) checks if B depends on A, known(A) indicates if A has been computed, value(A) predicts the value of A, can_next(A) checks if A can be computed next, and nece_next(A) and dece_next(A) combine these checks to understand the model's internal reasoning." (Section 4.1) - This provides a summary of the probing tasks and their relation to human reasoning.
   - "The probing tasks are designed to align closely with human problem-solving strategies: nece(A) checks if parameter A is necessary for the final answer, dece(A, B) checks if B depends on A, known(A) indicates if A has been computed, value(A) predicts the value of A, can_next(A) checks if A can be computed next, and nece_next(A) and dece_next(A) combine these checks to understand the model's internal reasoning." (Section 4.1) - This reiterates the motivation.
   - "We compute the V-probing accuracies on a language model pretrained from iGSM and compare them with the V-probing accuracies on a randomly initialized transformer model. If the former accuracies are significantly higher, we conclude that the probing signals must have (or be very close to having) come from the pretrained weights, rather than the (lightweight) finetuning stage." (Section 4.1) - This describes the analysis methodology.
   - "We compute the V-probing accuracies on a language model pretrained from iGSM and compare them with the V-probing accuracies on a randomly initialized transformer model. If the former accuracies are significantly higher, we conclude that the probing signals must have (or be very close to having) come from the pretrained weights, rather than the (lightweight) finetuning stage." (Section 4.1) - This reiterates the analysis methodology.

4. Validation Analysis:
   - The paper explicitly states the motivation for the probing tasks and how they relate to human reasoning.
   - The analysis methodology is described as comparing the probing accuracies of a model pretrained on iGSM with a randomly initialized model.
   - The interpretation of the results is that higher probing accuracies in the pretrained model suggest that the probing signals come from the pretrained weights.

5. Conclusion:
   - Validity status: Partially Valid
   - Confidence level: Medium
   - Key supporting evidence: The paper explains the motivation and analysis methodology for the probing tasks. However, a more detailed explanation of *why* these specific combinations of probes are chosen and how they uniquely reveal the model's reasoning process could be beneficial.

**Review 3 Weaknesses:**

1. Weakness Statement:
"The paper primarily focuses on the GPT-2 architecture, and it would be beneficial to see how the findings generalize to other model architectures, such as LLaMA or T5. The conclusions may not hold for other model architectures, as different architectures may have different inductive biases and training procedures that affect their ability to learn and generalize mathematical reasoning."

2. Evidence Collection:
   - This is the same weakness identified by Reviewer 1. Please see the validation for that weakness.

3. Literature Gap Analysis:
   - Same as Reviewer 1.

4. Validation Analysis:
   - Same as Reviewer 1.

5. Conclusion:
   - Validity status: Valid
   - Confidence level: High
   - Key supporting evidence: Explicit statement about using GPT2 and the reason for not testing other architectures.

1. Weakness Statement:
"The paper does not provide a clear definition of what constitutes a "reasoning skill" in the context of math problem solving. The authors use terms like "level-1" and "level-2" reasoning skills, but it is not clear what these terms mean in a precise way. This lack of clarity makes it difficult to interpret the results and compare them with other studies. A more rigorous definition of reasoning skills is needed to ensure the reproducibility and comparability of the findings."

2. Evidence Collection:
   - This is the same weakness identified by Reviewer 1. Please see the validation for that weakness.

3. Literature Gap Analysis:
   - Same as Reviewer 1.

4. Validation Analysis:
   - Same as Reviewer 1.

5. Conclusion:
   - Validity status: Valid
   - Confidence level: High
   - Key supporting evidence: Absence of a dedicated definition of "reasoning skill" and the use of the term primarily in the context of probing tasks.

**Review 4 Weaknesses:**

1. Weakness Statement:
"The paper focuses on a specific type of math problem, namely grade-school math. It would be interesting to see how the findings generalize to other types of math problems, such as algebra or calculus. The current scope limits the broader applicability of the conclusions, as the reasoning processes involved in solving different mathematical domains may vary significantly. For instance, algebraic manipulation requires understanding of variables and equations, while calculus involves limits, derivatives, and integrals, all of which are not addressed in this study."

2. Evidence Collection:
a) Method-related Evidence:
   - "Motivated by this, we build a GSM8K-like math dataset through a synthetic generation pipeline that captures the dependencies of parameters." (Section 2.1) - This explicitly states the focus on grade-school math.
   - "We use synthetic sentences to reduce the difficulty arising from Common Sense , like “a candle burned for 12 hours at 1 inch per hour” (implying the candle is reducing in length)." (Section 2.1) - This describes the type of grade-school math problems.
   - "We are currently bounded by resources to repeat all experiments in this paper with other architectures that have minor differences from GPT2-rotary for knowledge tasks [ 4 ] ." (Section 2.4) - This acknowledges the limitation to grade-school math.

3. Literature Gap Analysis:
   - The paper cites works on reasoning in language models but doesn't explicitly discuss the differences in reasoning required for different mathematical domains.

4. Validation Analysis:
   - The paper's focus is clearly on grade-school math, as evidenced by the dataset generation process and the examples provided.
   - The authors acknowledge the limitation to this specific type of math problem.

5. Conclusion:
   - Validity status: Valid
   - Confidence level: High
   - Key supporting evidence: Explicit statement of focusing on grade-school math and the examples of the problems generated.

1. Weakness Statement:
"The paper only considers a single model architecture, GPT-2. It would be interesting to see how the findings generalize to other model architectures, such as LLaMA or T5. The conclusions may not hold for other model architectures, as different architectures may have different inductive biases and training procedures that affect their ability to learn and generalize mathematical reasoning."

2. Evidence Collection:
   - This is the same weakness identified by Reviewer 1 and Reviewer 3. Please see the validation for that weakness.

3. Literature Gap Analysis:
   - Same as Reviewer 1.

4. Validation Analysis:
   - Same as Reviewer 1.

5. Conclusion:
   - Validity status: Valid
   - Confidence level: High
   - Key supporting evidence: Explicit statement about using GPT2 and the reason for not testing other architectures.

1. Weakness Statement:
"The paper does not provide a clear definition of what constitutes a "reasoning skill" in the context of math problem solving. The authors use terms like "level-1" and "level-2" reasoning skills, but it is not clear what these terms mean in a precise way. This lack of clarity makes it difficult to interpret the results and compare them with other studies. A more rigorous definition of reasoning skills is needed to ensure the reproducibility and comparability of the findings."

2. Evidence Collection:
   - This is the same weakness identified by Reviewer 1 and Reviewer 3. Please see the validation for that weakness.

3. Literature Gap Analysis:
   - Same as Reviewer 1.

4. Validation Analysis:
   - Same as Reviewer 1.

5. Conclusion:
   - Validity status: Valid
   - Confidence level: High
   - Key supporting evidence: Absence of a dedicated definition of "reasoning skill" and the use of the term primarily in the context of probing tasks.

1. Weakness Statement:
"How do the findings of this paper generalize to other types of math problems, such as algebra or calculus?"

2. Evidence Collection:
   - This is a question prompting for generalization, which is addressed by the paper's focus on grade-school math. The paper doesn't provide experimental evidence for other types of math problems.

3. Literature Gap Analysis:
   - The paper doesn't cite work that directly compares reasoning skills across different mathematical domains.

4. Validation Analysis:
   - The paper's scope is limited to grade-school math, and it doesn't provide evidence for generalization to other types.

5. Conclusion:
   - Validity status: Valid (as a question highlighting a limitation)
   - Confidence level: High
   - Key supporting evidence: The paper's explicit focus on grade-school math.

1. Weakness Statement:
"How do the findings of this paper generalize to other model architectures, such as LLaMA or T5?"

2. Evidence Collection:
   - This is a question prompting for generalization, which is addressed by the paper's focus on GPT-2. The paper doesn't provide experimental evidence for other architectures.

3. Literature Gap Analysis:
   - The paper doesn't cite work that directly compares reasoning capabilities across different model architectures for mathematical tasks.

4. Validation Analysis:
   - The paper's scope is limited to GPT-2, and it doesn't provide evidence for generalization to other architectures.

5. Conclusion:
   - Validity status: Valid (as a question highlighting a limitation)
   - Confidence level: High
   - Key supporting evidence: The paper's explicit focus on GPT-2.

1. Weakness Statement:
"What is the precise definition of a "reasoning skill" in the context of math problem solving?"

2. Evidence Collection:
   - This is a question prompting for a definition, which is not provided in the paper. The paper uses terms like "level-1" and "level-2" reasoning skills without a formal definition.

3. Literature Gap Analysis:
   - The paper doesn't cite work that provides a standard definition of "reasoning skill" in the context of math problem solving.

4. Validation Analysis:
   - The paper lacks a clear definition of "reasoning skill."

5. Conclusion:
   - Validity status: Valid (as a question highlighting a lack of definition)
   - Confidence level: High
   - Key supporting evidence: Absence of a dedicated definition of "reasoning skill."

**Synthesis and Reflection:**

Several reviewers consistently raised concerns about the lack of a clear definition of "reasoning skill" and the limited generalizability of the findings due to the focus on GPT-2 and grade-school math. There's a consensus that while the paper presents a valuable dataset and initial experiments, further work is needed to address these limitations.

Reviewer 1 and Reviewer 2 both highlighted the similarity between the proposed dataset (iGSM) and GSM8K, questioning the added value without a detailed comparative analysis. While the paper mentions the inspiration from GSM8K, it doesn't provide a side-by-side comparison table or a deep dive into the specific differences in problem structure, operation types, and complexity.

Reviewer 4 directly asked about the generalizability of the findings to other math domains and model architectures, echoing the concerns of Reviewer 1 and Reviewer 3. The paper acknowledges these limitations but doesn't offer experimental evidence to address them.

There are no direct contradictions between the reviewers' opinions. The weaknesses identified are largely complementary, focusing on different aspects of the paper's limitations.

**Conclusion:**

Based on the evidence collected, the majority of the weaknesses identified by the reviewers are **valid**. The paper could be significantly strengthened by:

*   Providing a rigorous and precise definition of "reasoning skill" in the context of mathematical problem solving.
*   Expanding the analysis to include other model architectures (e.g., LLaMA, T5) to assess the generalizability of the findings.
*   Providing a detailed comparative analysis of the iGSM dataset with GSM8K, highlighting the specific differences in problem structure, operation types, and complexity.
*   Including experiments on other types of math problems (e.g., algebra, calculus) to broaden the scope and impact of the research.
*   Providing a more detailed motivation and explanation for the choice of probing tasks and their relevance to the model's reasoning process.
*   Including a more comprehensive discussion of the limitations of the study and suggesting directions for future research.
}

Now, I have successfully verified each review. Next, I will organize this content and output the final review decision:

\boxed_review{
## Summary:

This paper introduces a novel synthetic dataset, iGSM, designed to investigate the mathematical reasoning capabilities of large language models (LLMs). The authors' primary motivation stems from the limitations of existing datasets like GSM8K, which, despite being widely used, may suffer from data contamination or lack sufficient diversity in problem-solving scenarios. To address these concerns, iGSM is constructed using a carefully crafted, synthetic generation pipeline that allows for controlled experimentation and the elimination of potential data contamination. The dataset is designed to encompass a range of grade-school math problems, focusing on arithmetic operations and logical dependencies between parameters. The core methodology involves training a GPT-2 model on the iGSM dataset and then employing a series of probing tasks to analyze the model's internal reasoning processes. These probing tasks are designed to align with human problem-solving strategies, specifically targeting the model's ability to identify necessary and sufficient parameters, understand logical dependencies, and predict parameter values. The authors conduct a series of experiments, including out-of-distribution (OOD) evaluations and error analysis, to understand the model's generalization ability and error patterns. The main empirical findings reveal that the GPT-2 model, when trained on iGSM, can learn certain mathematical skills and even acquire new reasoning skills beyond what is explicitly present in the training data. The authors also demonstrate that the model's reasoning process can be probed using the designed tasks, providing insights into how the model solves math problems. The paper concludes by highlighting the potential of iGSM as a valuable resource for studying the reasoning abilities of LLMs and suggesting future research directions, such as exploring different model architectures and investigating the emergence of more complex reasoning skills. Overall, this work makes a significant contribution by providing a controlled environment for studying mathematical reasoning in LLMs and offering a novel dataset that addresses some of the limitations of existing resources.


## Soundness:

2.75


## Presentation:

3.0


## Contribution:

2.75


## Strengths:

I find several aspects of this paper to be particularly strong. First, the introduction of the iGSM dataset is a significant contribution. The authors have successfully created a synthetic dataset that allows for controlled experimentation and the elimination of data contamination, which is a critical issue with datasets like GSM8K. The dataset's design, which includes a focus on grade-school math problems with a clear structure and logical dependencies, provides a valuable resource for studying the reasoning abilities of LLMs. The authors' decision to use a synthetic generation pipeline also allows for the systematic manipulation of problem parameters, which is a significant advantage over real-world datasets. Second, the use of probing tasks to analyze the model's reasoning process is a novel and insightful approach. The authors have designed these tasks to align with human problem-solving strategies, specifically targeting the model's ability to identify necessary and sufficient parameters, understand logical dependencies, and predict parameter values. This approach allows for a more fine-grained analysis of the model's internal reasoning processes than simply evaluating its final answer. The authors' choice of probing tasks, such as 'nece', 'dece', 'known', 'value', 'can_next', and 'nece_next', provides a comprehensive view of the model's reasoning abilities. Finally, the paper's experimental setup is well-designed and executed. The authors have conducted a series of experiments, including OOD evaluations and error analysis, to understand the model's generalization ability and error patterns. The inclusion of a random baseline for the probing tasks is also a valuable addition, as it helps to establish the significance of the model's performance. The authors' analysis of the model's error patterns, particularly the observation that the model makes errors due to backward reasoning, provides valuable insights into the model's limitations. The paper's clear and concise writing style also contributes to its overall strength, making it easy to follow the authors' arguments and understand their findings. The authors have also provided a detailed description of their methodology, which allows for reproducibility and further research in this area.


## Weaknesses:

Despite the strengths of this paper, I have identified several weaknesses that warrant careful consideration. First, the paper lacks a clear and rigorous definition of what constitutes a 'reasoning skill' in the context of mathematical problem-solving. While the authors use terms like 'level-1' and 'level-2' reasoning skills, these terms are not defined precisely, making it difficult to interpret the results and compare them with other studies. For example, the paper does not specify what cognitive processes are involved in these skills, such as symbolic manipulation, logical deduction, or pattern recognition. This lack of clarity makes it challenging to understand the model's reasoning process and to draw meaningful conclusions about its capabilities. This is a significant limitation, as it hinders the reproducibility and comparability of the findings. Second, the paper primarily focuses on the GPT-2 architecture, and it would be beneficial to see how the findings generalize to other model architectures, such as LLaMA or T5. The conclusions may not hold for other model architectures, as different architectures may have different inductive biases and training procedures that affect their ability to learn and generalize mathematical reasoning. The authors acknowledge this limitation, stating that they are bounded by resources to repeat all experiments with other architectures. However, this limitation significantly restricts the scope of the paper's findings and raises questions about the generalizability of the results. Third, the paper does not provide a clear and detailed comparison between the proposed iGSM dataset and the existing GSM8K dataset. While the authors state that iGSM is designed to be free from data contamination and allows for controlled experimentation, they do not provide a side-by-side comparison of the types of problems, the distribution of operations, and the complexity of the mathematical reasoning required in both datasets. The paper mentions that iGSM is easier to analyze and generate in large quantities, but it does not provide a concrete analysis of the differences between the two datasets. This lack of a detailed comparison makes it difficult to assess the unique contributions of the iGSM dataset and to understand why it is a more suitable resource for studying the reasoning abilities of LLMs. Fourth, the paper's focus on grade-school math limits the broader applicability of the conclusions. The reasoning processes involved in solving different mathematical domains may vary significantly, and the findings may not generalize to other types of math problems, such as algebra or calculus. The authors acknowledge this limitation, but they do not provide any experimental evidence to support their claims. This limitation significantly restricts the scope of the paper's findings and raises questions about the generalizability of the results. Finally, while the paper introduces the probing tasks, it does not provide a detailed motivation for why these specific tasks were chosen and how they relate to the actual problem-solving process. The authors state that the probing tasks are designed to align closely with human problem-solving strategies, but they do not provide a clear explanation of the specific cognitive skills that are being probed by each task. This lack of clarity makes it difficult to interpret the results and to compare them with other studies. The paper also does not provide a detailed analysis of the model's error patterns, which would be helpful in understanding the model's limitations and suggesting directions for future research. These weaknesses, while not invalidating the paper's contributions, do highlight areas where further research is needed to strengthen the findings and to broaden the scope of the study.


## Suggestions:

To address the identified weaknesses, I recommend several concrete improvements. First, the authors should provide a more rigorous and precise definition of 'reasoning skill' in the context of mathematical problem-solving. They should start by identifying the specific cognitive processes involved in solving mathematical problems, such as symbolic manipulation, logical deduction, and pattern recognition. Then, they should define 'reasoning skills' in terms of these cognitive processes, perhaps by categorizing them into different levels of complexity. For example, they could define 'level-1' reasoning skills as those that involve simple arithmetic operations, while 'level-2' reasoning skills involve more complex operations, such as solving equations or manipulating algebraic expressions. This would allow for a more systematic analysis of the model's reasoning abilities and facilitate comparisons with other studies. Second, the authors should expand their analysis to include a wider range of model architectures to assess the generalizability of their findings. Specifically, they could explore models like LLaMA or T5, which have different architectural designs and training methodologies. This would involve training and evaluating these models on the same synthetic datasets and analyzing their performance in terms of reasoning accuracy, generalization ability, and error patterns. By comparing the results across different architectures, the authors could identify the key factors that influence a model's ability to learn and generalize mathematical reasoning. For example, they could investigate whether models with different attention mechanisms or layer normalization techniques exhibit different behaviors when presented with mathematical problems. This would provide a more comprehensive understanding of the capabilities and limitations of language models in this domain. Third, the authors need to provide a more detailed comparative analysis of the iGSM dataset and GSM8K. This analysis should go beyond a simple comparison of the number of problems and should focus on the specific characteristics of the problems themselves. For example, the authors could analyze the distribution of different types of arithmetic operations (e.g., addition, subtraction, multiplication, division) in both datasets, as well as the complexity of the mathematical reasoning required to solve the problems. They could also analyze the structure of the problems, such as the number of steps involved in the solution process and the types of intermediate calculations that are needed. This analysis could be presented in the form of tables or graphs that clearly show the differences between the two datasets. Furthermore, the authors should provide a clear explanation of why iGSM is a more suitable dataset for studying the reasoning abilities of language models compared to GSM8K. This explanation should focus on the specific features of iGSM that make it easier to analyze and generate in large quantities, as well as the specific advantages it offers for studying the model's reasoning process. Fourth, the authors should expand their analysis to include other types of math problems, such as algebra or calculus. This would involve creating new synthetic datasets that cover a wider range of mathematical concepts and problem types. By doing so, the authors could gain a better understanding of how language models generalize their reasoning abilities across different mathematical domains. Furthermore, this would increase the practical relevance of their findings, as mathematical reasoning is a crucial skill in many real-world applications. Finally, the authors should provide a more detailed motivation for the probing tasks and explain how they relate to the actual problem-solving process. They should clearly state the specific cognitive skills that each probing task is designed to measure and explain how these skills are relevant to the steps involved in solving grade-school math problems. For example, they could explain why the 'nece' task is designed to measure the model's ability to identify the relevant variables in a problem, and why the 'dece' task is designed to measure the model's ability to understand the logical dependencies between variables. The authors should also provide a more detailed analysis of the model's error patterns, including the types of mathematical operations or problem structures that are more prone to errors and the circumstances under which these errors occur. This would provide valuable insights into the model's limitations and suggest directions for future research.


## Questions:

Based on my analysis, I have several questions that I believe are crucial for a deeper understanding of the paper's findings. First, how do the findings of this paper generalize to other types of math problems, such as algebra or calculus? The current study focuses on grade-school math, but it is unclear whether the same reasoning skills are relevant to more complex mathematical domains. Second, how do the findings of this paper generalize to other model architectures, such as LLaMA or T5? The paper primarily focuses on GPT-2, and it is important to understand whether the conclusions hold for other architectures with different inductive biases and training procedures. Third, what is the precise definition of a 'reasoning skill' in the context of math problem solving? The paper uses terms like 'level-1' and 'level-2' reasoning skills without a formal definition, which makes it difficult to interpret the results and compare them with other studies. Fourth, what are the probing tasks motivated by? How do they relate to the actual problem-solving process? The paper states that the probing tasks are designed to align with human problem-solving strategies, but it does not provide a clear explanation of the specific cognitive skills that are being probed by each task. Finally, what is the precise definition of a 'reasoning skill' in the context of math problem solving? The paper uses terms like 'level-1' and 'level-2' reasoning skills, but it does not provide a clear definition of these terms in a precise way. This lack of clarity makes it difficult to interpret the results and compare them with other studies. These questions are crucial for understanding the limitations of the study and for guiding future research in this area.


## Rating:

6.75


## Confidence:

3.5


## Decision:

Reject
}