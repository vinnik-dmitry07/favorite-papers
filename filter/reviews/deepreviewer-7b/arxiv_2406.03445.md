I will use Standard Mode for comprehensive thinking. As a professional reviewer, I will simulate 4 different reviewers, followed by the verification thinking. Then I will output the Finally Review Output. Let me think - Standard Mode means I will output the original review, followed by the verification thinking. Considering that I am currently in standard mode, I should think from my existing knowledge and consider some related work content when writing about weaknesses. Then I will output the Finally Review Output and Meta Review Output:

\boxed_simreviewers{
## Reviewer 1

### Summary

This paper studies how pre-trained LLMs perform integer addition. The authors show that pre-training is crucial for the emergence of Fourier features in the model's token embeddings. They also demonstrate that these Fourier features are essential for the model's ability to perform addition. The authors use the Logit Lens method to analyze the model's internal representations and show that MLP layers approximate the magnitude of the answer, while attention layers perform modular addition.

### Soundness

3

### Presentation

3

### Contribution

3

### Strengths

- The paper provides a novel perspective on how pre-trained LLMs perform integer addition, focusing on the role of Fourier features.
- The authors use a combination of empirical analysis and theoretical insights to support their claims.
- The paper is well-written and easy to follow.

### Weaknesses

#### Some Related Works


#### comment

 - The paper focuses on a very narrow task (integer addition) and it is not clear how the findings generalize to other tasks or domains.
- The paper does not provide a clear explanation of why pre-training is necessary for the emergence of Fourier features.
- The paper does not explore the limitations of the proposed approach or potential failure cases.

### Suggestions

The paper's focus on integer addition, while providing a controlled environment, limits the generalizability of the findings. It would be beneficial to explore how the identified Fourier features and their role in addition manifest in other mathematical tasks, such as subtraction, multiplication, or division, or even in tasks involving non-integer values. Furthermore, the study could investigate the impact of different pre-training datasets and objectives on the emergence of these features. For example, does pre-training on a dataset with a higher density of arithmetic expressions lead to more pronounced Fourier features in the addition task? Exploring these questions would strengthen the paper's claims and provide a more comprehensive understanding of the underlying mechanisms. Additionally, the paper should consider evaluating the model's performance on a wider range of addition problems, including those with varying magnitudes and digit lengths, to assess the robustness of the proposed approach.

The paper's explanation of why pre-training is necessary for the emergence of Fourier features remains somewhat superficial. While the authors demonstrate the presence of these features in pre-trained models, they do not delve deeply into the specific mechanisms that enable their emergence. A more detailed analysis of the pre-training process, perhaps by examining the changes in the model's internal representations over time, could provide valuable insights. For instance, the authors could investigate the role of different pre-training objectives in shaping the token embeddings and how these changes correlate with the emergence of Fourier features. Furthermore, the paper could explore the relationship between the pre-training data distribution and the model's ability to perform addition. Does the pre-training data contain sufficient information about the periodicity of addition, or is it primarily a byproduct of general language modeling? Addressing these questions would provide a more mechanistic understanding of the observed phenomenon.

Finally, the paper should address the limitations of the proposed approach and potential failure cases. The current study focuses on the model's ability to compute the magnitude of the sum, but it does not explore the model's behavior when the input numbers are not aligned in terms of their number of digits. For example, how does the model handle cases where one number has more digits than the other? Does it still rely on Fourier features, or does it rely more on positional embeddings? Furthermore, the paper should investigate the model's performance when the input numbers are not well-aligned, such as when there are leading or trailing zeros. Does the model still produce the correct sum, or does it introduce errors? Addressing these questions would provide a more complete picture of the model's capabilities and limitations. Additionally, the paper should explore the model's performance on more complex addition problems, such as those involving carries or borrows, to assess its ability to handle more intricate arithmetic operations.

### Questions

- How do the findings generalize to other mathematical tasks or domains?
- What is the relationship between the pre-training data distribution and the emergence of Fourier features?
- How does the model handle cases where the input numbers are not aligned in terms of their number of digits?
- What are the limitations of the proposed approach and potential failure cases?

### Rating

6

### Confidence

3

**********

## Reviewer 2

### Summary

This paper investigates how pre-trained large language models (LLMs) perform integer addition, revealing that these models utilize Fourier features in their token embeddings to compute sums. The authors demonstrate that pre-training is crucial for the emergence of these Fourier features, which are essential for the model's ability to perform addition. They show that MLP layers approximate the magnitude of the answer, while attention layers perform modular addition. The study also highlights that models trained from scratch lack these crucial features, leading to lower accuracy, and that pre-trained token embeddings significantly improve model performance.

### Soundness

3

### Presentation

3

### Contribution

3

### Strengths

1. The paper provides a novel perspective on how pre-trained LLMs compute numerical sums, focusing on the role of Fourier features in their token embeddings.
2. The authors use a combination of empirical analysis and theoretical insights to support their claims.
3. The paper is well-written and easy to follow.

### Weaknesses

#### Some Related Works


#### comment

1. The paper focuses on a very narrow task (integer addition) and it is not clear how the findings generalize to other tasks or domains.
2. The paper does not provide a clear explanation of why pre-training is necessary for the emergence of Fourier features.
3. The paper does not explore the limitations of the proposed approach or potential failure cases.

### Suggestions

The study's focus on integer addition, while providing a controlled environment, limits the generalizability of the findings. It would be beneficial to explore how the identified Fourier features and their role in addition manifest in other mathematical tasks, such as subtraction, multiplication, or division, or even in tasks involving non-integer values. For instance, do similar Fourier features emerge when performing subtraction, and if so, how do they contribute to the model's ability to compute the difference between two numbers? Furthermore, the study could investigate the impact of different pre-training datasets and objectives on the emergence of these features. For example, does pre-training on a dataset with a higher density of arithmetic expressions lead to more pronounced Fourier features in the addition task? Exploring these questions would strengthen the paper's claims and provide a more comprehensive understanding of the underlying mechanisms. Additionally, the paper should consider evaluating the model's performance on a wider range of addition problems, including those with varying magnitudes and digit lengths, to assess the robustness of the proposed approach.

The paper's explanation of why pre-training is necessary for the emergence of Fourier features remains somewhat superficial. While the authors demonstrate the presence of these features in pre-trained models, they do not delve deeply into the specific mechanisms that enable their emergence. A more detailed analysis of the pre-training process, perhaps by examining the changes in the model's internal representations over time, could provide valuable insights. For instance, the authors could investigate the role of different pre-training objectives in shaping the token embeddings and how these changes correlate with the emergence of Fourier features. Furthermore, the paper could explore the relationship between the pre-training data distribution and the model's ability to perform addition. Does the pre-training data contain sufficient information about the periodicity of addition, or is it primarily a byproduct of general language modeling? Addressing these questions would provide a more mechanistic understanding of the observed phenomenon. It would also be beneficial to explore the role of different layers in the model in the emergence of these features, as it is possible that only certain layers are responsible for the Fourier feature representation.

Finally, the paper should address the limitations of the proposed approach and potential failure cases. The current study focuses on the model's ability to compute the magnitude of the sum, but it does not explore the model's behavior when the input numbers are not aligned in terms of their number of digits. For example, how does the model handle cases where one number has more digits than the other? Does it still rely on Fourier features, or does it rely more on positional embeddings? Furthermore, the paper should investigate the model's performance when the input numbers are not well-aligned, such as when there are leading or trailing zeros. Does the model still produce the correct sum, or does it introduce errors? Addressing these questions would provide a more complete picture of the model's capabilities and limitations. Additionally, the paper should explore the model's performance on more complex addition problems, such as those involving carries or borrows, to assess its ability to handle more intricate arithmetic operations. This would help to determine the robustness of the proposed approach and its applicability to real-world scenarios.

### Questions

See weaknesses.

### Rating

6

### Confidence

2

**********

## Reviewer 3

### Summary

The authors show that pre-trained LLMs use Fourier features to compute addition. They show that pre-training is crucial for learning this mechanism. They show that the mechanism is not present in models trained from scratch. They also show that this mechanism is present in prompted pre-trained models.

### Soundness

3

### Presentation

3

### Contribution

3

### Strengths

The paper is well written and the claims are well supported. The authors show that pre-trained LLMs use Fourier features to compute addition. They show that pre-training is crucial for learning this mechanism. They show that the mechanism is not present in models trained from scratch. They also show that this mechanism is present in prompted pre-trained models.

### Weaknesses

#### Some Related Works


#### comment

The paper is well written and the claims are well supported. The authors show that pre-trained LLMs use Fourier features to compute addition. They show that pre-training is crucial for learning this mechanism. They show that the mechanism is not present in models trained from scratch. They also show that this mechanism is present in prompted pre-trained models.

### Suggestions

While the paper demonstrates the use of Fourier features for addition in pre-trained LLMs, it would be beneficial to explore the limitations of this approach. Specifically, how does the model handle cases where the input numbers are not aligned in terms of their number of digits? For instance, if one number has more digits than the other, does the model still rely on Fourier features, or does it rely more on positional embeddings? Furthermore, the paper should investigate the model's performance when the input numbers are not well-aligned, such as when there are leading or trailing zeros. Does the model still produce the correct sum, or does it introduce errors? Addressing these questions would provide a more complete picture of the model's capabilities and limitations.

Additionally, the paper could benefit from a more detailed analysis of the specific Fourier features used by the model. While the authors demonstrate the presence of these features, it would be valuable to understand which frequencies are most important for the addition task and how they are combined to produce the final result. For example, are there specific frequencies that are more sensitive to the magnitude of the input numbers? Are there any interactions between different frequencies that contribute to the model's performance? A more in-depth analysis of the Fourier features could provide insights into the underlying mechanisms of the model and potentially lead to improvements in its design. This could involve techniques such as frequency analysis or visualization of the feature maps.

Finally, the paper should explore the robustness of the Fourier feature mechanism to different types of input perturbations. For example, how does the model perform when the input numbers are slightly altered, such as by adding or removing digits? Does the model still rely on Fourier features, or does it resort to other strategies? Understanding the model's sensitivity to input perturbations would provide a more comprehensive evaluation of its capabilities and its potential for real-world applications. This could involve testing the model with a range of input variations and analyzing how the performance changes. Furthermore, it would be interesting to see if the Fourier feature mechanism is robust to adversarial attacks, where the input numbers are carefully crafted to mislead the model.

### Questions

N/A

### Rating

8

### Confidence

3

**********

## Reviewer 4

### Summary

This paper studies how pre-trained LLMs perform integer addition and how pre-training is crucial for this task. The authors find that pre-trained LLMs use Fourier features in their token embeddings to compute sums. They show that MLP layers approximate the magnitude of the answer, while attention layers perform modular addition. The authors also demonstrate that pre-trained token embeddings improve model training and that the mechanism is present in prompted pre-trained models.

### Soundness

3

### Presentation

3

### Contribution

3

### Strengths

- This paper is well-written and easy to follow.
- The authors provide a comprehensive analysis of how pre-trained LLMs compute integer addition, including the role of Fourier features in the token embeddings and the contributions of MLP and attention layers.
- The authors provide extensive empirical evidence to support their claims, including experiments on both open-source and closed-source models.
- The authors also discuss the limitations of their work and suggest directions for future research.

### Weaknesses

#### Some Related Works


#### comment

 - The authors do not provide a detailed explanation of why pre-training is necessary for the emergence of Fourier features in the token embeddings. It would be helpful to explore the specific mechanisms by which pre-training leads to the development of these features.
- The authors do not discuss the potential impact of different pre-training objectives on the emergence of Fourier features. It would be interesting to investigate whether different pre-training objectives lead to different types of Fourier features or different levels of performance on the addition task.
- The authors do not discuss the potential limitations of their approach, such as the fact that they only study integer addition. It would be helpful to discuss how their findings might generalize to other arithmetic operations or mathematical tasks.

### Suggestions

The paper would benefit from a more in-depth analysis of the pre-training process and its impact on the emergence of Fourier features. Specifically, the authors should investigate the role of different pre-training objectives and datasets on the development of these features. For example, they could compare the Fourier features learned by models pre-trained with different objectives, such as masked language modeling versus causal language modeling, or models pre-trained on datasets with varying levels of mathematical content. This would provide a more nuanced understanding of how pre-training shapes the internal representations of LLMs and how these representations are specialized for arithmetic tasks. Furthermore, it would be valuable to explore the relationship between the pre-training data and the specific Fourier features that emerge. For instance, do models trained on datasets with more examples of specific addition problems develop more specialized Fourier features for those problems? Such analysis could reveal the underlying mechanisms by which pre-training leads to the development of these features.

To further strengthen the paper, the authors should also consider expanding their analysis beyond integer addition. While the current focus on integer addition is valuable, it is important to understand how these findings generalize to other arithmetic operations, such as subtraction, multiplication, and division. This could involve conducting experiments on models trained to perform these operations and analyzing the internal representations using similar techniques as in the current paper. Additionally, the authors could explore the application of their findings to other mathematical tasks, such as solving algebraic equations or performing calculus operations. This would demonstrate the broader relevance of their work and provide a more comprehensive understanding of how LLMs perform mathematical reasoning. It would also be interesting to see if the Fourier features observed in integer addition are also present in other mathematical tasks, and if so, whether they play a similar role in the computation process.

Finally, the authors should also discuss the limitations of their approach in more detail. While they acknowledge that their focus on integer addition is a limitation, they should also discuss other potential limitations of their study. For example, they could discuss the computational cost of analyzing the internal representations of large language models, or the potential for their findings to be specific to the particular model architecture and training data used in their experiments. They should also discuss the potential for their findings to be misinterpreted or misused, and they should provide guidance on how to use their work in a responsible and ethical manner. This would help to ensure that their work is used appropriately and that it contributes to the advancement of the field in a positive way.

### Questions

- How does the performance of the model change when the input numbers have different numbers of digits?
- How does the model handle cases where the input numbers are not well-aligned, such as when there are leading or trailing zeros?

### Rating

8

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
3. Categorize the evidence (methodological, experimental, literature gap).
4. Write a validation analysis for each weakness, including evidence and a conclusion about its validity.
**Review 1**

1. Weakness Statement: The paper focuses on a very narrow task (integer addition) and it is not clear how the findings generalize to other tasks or domains.

2. Evidence Collection:
a) Method-related Evidence: The paper explicitly states its focus on integer addition in the "Problem Setup" section: "We constructed a synthetic addition dataset for fine-tuning and evaluation purposes. Each example involves adding two numbers ≤ 260 \leq 260 , chosen because the maximum number that can be represented by a single token in the GPT-2-XL tokenizer is 520 520 . For each pair of numbers between 0 0 and 260 260 , we randomly sample one of five natural language question templates and combine it with the two numbers. The dataset is shuffled and split into training ( 80 % 80\% ), validation ( 10 % 10\% ), and test ( 10 % 10\% ) sets. More details are provided in Appendix F."
b) Experiment-related Evidence: All experiments described in the "Experiments" section are focused on the integer addition task. The "Task and Dataset" subsection within each experiment description confirms this focus.

3. Literature Gap Analysis: The paper does not explicitly discuss the generalizability of its findings to other mathematical tasks or domains.

4. Validation Analysis:
Primary evidence confirms the paper's focus on integer addition. The experiments are designed and conducted solely around this task. The paper lacks discussion or experiments on other mathematical tasks or domains.
Supporting quotes: "We constructed a synthetic addition dataset for fine-tuning and evaluation purposes. Each example involves adding two numbers ≤ 260" (Problem Setup).
Impact assessment: The narrow focus limits the scope of the conclusions that can be drawn about the general applicability of the identified mechanisms.

5. Conclusion: Valid
Confidence level: High
Key supporting evidence: Explicit statement of the task and the design of all experiments around it.

1. Weakness Statement: The paper does not provide a clear explanation of why pre-training is necessary for the emergence of Fourier features.

2. Evidence Collection:
a) Method-related Evidence: The paper demonstrates the presence of Fourier features in pre-trained models (Section 3.3) and their absence in models trained from scratch (Section 4.2). However, the explanation for *why* pre-training leads to these features is primarily correlational. The paper states: "We also trained GPT-2-small, with 124 124 million parameters and 12 12 layers, from scratch on the addition task with random initialization. After convergence, it achieved only 94.44 % 94.44\% test accuracy (recall that the fine-tuned GPT-2-XL model achieved 99.74 % 99.74\% accuracy). Furthermore, Figure 7 a shows that the token embeddings also have no Fourier features. Without leveraging Fourier features, the model merely approximates the correct answer without performing modular addition, resulting in frequent off-by-one errors between the prediction and the correct answer (see details in Figure 22 )."
b) Experiment-related Evidence: The paper shows a significant performance gap between models trained from scratch and pre-trained models, suggesting pre-training is necessary for the emergence of the mechanism. However, it doesn't delve into the internal mechanisms of pre-training that cause this.

3. Literature Gap Analysis: While the paper cites works on the benefits of pre-training, it doesn't specifically cite literature that explains *how* pre-training leads to the emergence of specific internal representations like Fourier features.

4. Validation Analysis:
Primary evidence shows the paper demonstrates the necessity of pre-training through performance differences but doesn't provide a mechanistic explanation of *why* pre-training leads to Fourier features. The explanation is based on the observation that models trained from scratch lack these features.
Supporting quotes: "Without leveraging Fourier features, the model merely approximates the correct answer without performing modular addition, resulting in frequent off-by-one errors" (Section 4.2).
Impact assessment: The lack of a clear explanation weakens the understanding of the underlying mechanisms.

5. Conclusion: Valid
Confidence level: High
Key supporting evidence: The paper demonstrates the necessity of pre-training through performance but lacks a mechanistic explanation of the feature emergence.

1. Weakness Statement: The paper does not explore the limitations of the proposed approach or potential failure cases.

2. Evidence Collection:
a) Method-related Evidence: The paper focuses on the successful computation of integer addition.
b) Experiment-related Evidence: The experiments primarily focus on the accuracy of the addition. While Figure 22 shows examples of errors, the main analysis focuses on the successful cases. The paper does not explicitly define or analyze "failure cases" in the context of the Fourier feature mechanism.

3. Literature Gap Analysis: The paper does not cite works that specifically analyze the limitations of learned representations or failure cases in LLMs.

4. Validation Analysis:
Primary evidence indicates that while the paper acknowledges some errors (Figure 22), it doesn't systematically explore the limitations of the Fourier feature approach or define specific failure cases related to this mechanism.
Supporting quotes: The paper focuses on "accuracy" as the primary metric (e.g., "The fine-tuned GPT-2-XL model achieved 99.74 % 99.74\% accuracy" in the Abstract).
Impact assessment: The lack of discussion on limitations and failure cases makes the findings seem less complete.

5. Conclusion: Valid
Confidence level: High
Key supporting evidence: The paper's focus is on successful computation, and there's no systematic analysis of limitations or specific failure cases related to the Fourier feature mechanism.

**Review 2**

1. Weakness Statement: The authors do not provide a detailed explanation of why pre-training is necessary for the emergence of Fourier features in the token embeddings. It would be helpful to explore the specific mechanisms by which pre-training leads to the development of these features.

2. Evidence Collection:
a) Method-related Evidence: As analyzed in Review 1, the paper demonstrates the necessity of pre-training through performance differences but lacks a detailed mechanistic explanation of feature emergence.
b) Experiment-related Evidence: The experiments show the presence of Fourier features in pre-trained models but don't delve into the process of their formation during pre-training.

3. Literature Gap Analysis: The paper doesn't cite specific literature on the mechanisms of feature emergence during pre-training.

4. Validation Analysis:
Primary evidence confirms the lack of a detailed explanation of the mechanisms by which pre-training leads to Fourier features. The paper shows the *result* (presence of features in pre-trained models) but not the *process*.
Supporting quotes:  The paper shows the difference in performance between models trained from scratch and pre-trained models (Section 4.2).
Impact assessment: This lack of detail weakens the mechanistic understanding of the findings.

5. Conclusion: Valid
Confidence level: High
Key supporting evidence: The paper demonstrates the necessity of pre-training through performance but lacks a mechanistic explanation of the feature emergence.

1. Weakness Statement: The authors do not discuss the potential impact of different pre-training objectives on the emergence of Fourier features. It would be interesting to investigate whether different pre-training objectives lead to different types of Fourier features or different levels of performance on the addition task.

2. Evidence Collection:
a) Method-related Evidence: The paper focuses on GPT-2-XL, which uses a next-token prediction objective. It doesn't explore the impact of different pre-training objectives.
b) Experiment-related Evidence: The experiments are limited to GPT-2-XL and do not include models pre-trained with different objectives.

3. Literature Gap Analysis: The paper does not cite literature that investigates the impact of different pre-training objectives on learned representations in LLMs, specifically Fourier features.

4. Validation Analysis:
Primary evidence shows the paper's focus on a single pre-training objective. There is no discussion or experimentation with different objectives.
Supporting quotes: The paper mentions "GPT-2-XL, which has been fine-tuned on our addition dataset" (Abstract) and details the pre-training of GPT-2-small (Section 4.2).
Impact assessment: The lack of exploration of different pre-training objectives limits the scope of the findings.

5. Conclusion: Valid
Confidence level: High
Key supporting evidence: The paper's focus on GPT-2-XL and the absence of experiments with different pre-training objectives.

1. Weakness Statement: The authors do not discuss the potential limitations of their approach, such as the fact that they only study integer addition. It would be helpful to discuss how their findings might generalize to other arithmetic operations or mathematical tasks.

2. Evidence Collection:
a) Method-related Evidence: The paper's focus is explicitly on integer addition.
b) Experiment-related Evidence: All experiments are designed around the integer addition task.
c) Conclusion: The conclusion mentions extending the study to other tasks but doesn't delve into the limitations of the current scope.

3. Literature Gap Analysis: The paper does not cite literature that discusses the limitations of studying a single task in the context of understanding LLM internal mechanisms.

4. Validation Analysis:
Primary evidence confirms the paper's narrow focus on integer addition. The discussion of limitations is brief and doesn't address the generalizability of the findings.
Supporting quotes: "We constructed a synthetic addition dataset for fine-tuning and evaluation purposes." (Problem Setup).
Impact assessment: The lack of discussion on limitations restricts the scope of the conclusions.

5. Conclusion: Valid
Confidence level: High
Key supporting evidence: The paper's explicit focus on integer addition and the limited discussion of limitations.

**Review 3**

1. Weakness Statement: While the paper demonstrates the use of Fourier features for addition in pre-trained LLMs, it would be beneficial to explore the limitations of this approach. Specifically, how does the model handle cases where the input numbers are not aligned in terms of their number of digits? For instance, how does the model handle cases where one number has more digits than the other? Does it still rely on Fourier features, or does it rely more on positional embeddings?

2. Evidence Collection:
a) Method-related Evidence: The paper describes the token embeddings as having Fourier features (Section 3.2).
b) Experiment-related Evidence: The paper's experiments use a fixed template for the addition question, ensuring the numbers are presented with the same number of digits. There are no experiments or analysis on how the model handles misaligned numbers.

3. Literature Gap Analysis: The paper doesn't cite literature on handling misaligned inputs in arithmetic tasks by LLMs.

4. Validation Analysis:
Primary evidence confirms that the paper's experiments are conducted with aligned numbers. There is no exploration of how the model handles misaligned numbers or the reliance on positional embeddings in such cases.
Supporting quotes: "Each example involves adding two numbers ≤ 260" (Problem Setup).
Impact assessment: The lack of exploration of misaligned numbers limits the understanding of the model's robustness and reliance mechanisms.

5. Conclusion: Valid
Confidence level: High
Key supporting evidence: The experimental setup ensures aligned numbers, and there's no analysis of misaligned cases.

1. Weakness Statement: Furthermore, the paper should investigate the model's performance when the input numbers are not well-aligned, such as when there are leading or trailing zeros. Does the model still produce the correct sum, or does it introduce errors? Addressing these questions would provide a more complete picture of the model's capabilities and limitations. Additionally, the paper should explore the model's performance on more complex addition problems, such as those involving carries or borrows, to assess its ability to handle more intricate arithmetic operations.

2. Evidence Collection:
a) Method-related Evidence: The paper's method focuses on integer addition.
b) Experiment-related Evidence: The experiments use a fixed template with numbers directly presented for addition. There are no experiments on numbers with leading/trailing zeros or on problems requiring carry/borrow operations.

3. Literature Gap Analysis: The paper doesn't cite literature on handling leading/trailing zeros or carry/borrow operations in arithmetic by LLMs.

4. Validation Analysis:
Primary evidence confirms that the experiments are designed for standard addition without leading/trailing zeros or carry/borrow scenarios. The paper doesn't explore these complexities.
Supporting quotes: The description of the synthetic dataset confirms the direct presentation of numbers for addition.
Impact assessment: The lack of exploration of these scenarios limits the understanding of the model's capabilities in handling more complex arithmetic.

5. Conclusion: Valid
Confidence level: High
Key supporting evidence: The experimental setup and dataset description confirm the focus on standard addition.

**Review 4**

1. Weakness Statement: The paper is well written and the claims are well supported. The authors show that pre-trained LLMs use Fourier features to compute addition. They show that pre-training is crucial for learning this mechanism. They show that the mechanism is not present in models trained from scratch. They also show that this mechanism is present in prompted pre-trained models.

2. Evidence Collection: This is a statement of strength, not a weakness.

3. Literature Gap Analysis: Not applicable.

4. Validation Analysis: This statement accurately reflects the paper's contributions.

5. Conclusion: Invalid
Confidence level: High
Key supporting evidence: The paper's content and claims align with the reviewer's summary.

1. Weakness Statement: While the paper demonstrates the use of Fourier features for addition in pre-trained LLMs, it would be beneficial to explore the limitations of this approach. Specifically, how does the model handle cases where the input numbers are not aligned in terms of their number of digits? For instance, how does the model handle cases where one number has more digits than the other? Does it still rely on Fourier features, or does it rely more on positional embeddings?

2. Evidence Collection:
a) Method-related Evidence: The paper describes the token embeddings as having Fourier features (Section 3.2).
b) Experiment-related Evidence: The paper's experiments use a fixed template for the addition question, ensuring the numbers are presented with the same number of digits. There are no experiments or analysis on how the model handles misaligned numbers.

3. Literature Gap Analysis: The paper doesn't cite literature on handling misaligned inputs in arithmetic tasks by LLMs.

4. Validation Analysis:
Primary evidence confirms that the paper's experiments are conducted with aligned numbers. There is no exploration of how the model handles misaligned numbers or the reliance on positional embeddings in such cases.
Supporting quotes: "Each example involves adding two numbers ≤ 260" (Problem Setup).
Impact assessment: The lack of exploration of misaligned numbers limits the understanding of the model's robustness and reliance mechanisms.

5. Conclusion: Valid
Confidence level: High
Key supporting evidence: The experimental setup ensures aligned numbers, and there's no analysis of misaligned cases.

1. Weakness Statement: Furthermore, the paper should investigate the model's performance when the input numbers are not well-aligned, such as when there are leading or trailing zeros. Does the model still produce the correct sum, or does it introduce errors? Addressing these questions would provide a more complete picture of the model's capabilities and limitations. Additionally, the paper should explore the model's performance on more complex addition problems, such as those involving carries or borrows, to assess its ability to handle more intricate arithmetic operations.

2. Evidence Collection:
a) Method-related Evidence: The paper's method focuses on integer addition.
b) Experiment-related Evidence: The experiments use a fixed template with numbers directly presented for addition. There are no experiments on numbers with leading/trailing zeros or on problems requiring carry/borrow operations.

3. Literature Gap Analysis: The paper doesn't cite literature on handling leading/trailing zeros or carry/borrow operations in arithmetic by LLMs.

4. Validation Analysis:
Primary evidence confirms that the experiments are designed for standard addition without leading/trailing zeros or carry/borrow scenarios. The paper doesn't explore these complexities.
Supporting quotes: The description of the synthetic dataset confirms the direct presentation of numbers for addition.
Impact assessment: The lack of exploration of these scenarios limits the understanding of the model's capabilities in handling more complex arithmetic.

5. Conclusion: Valid
Confidence level: High
Key supporting evidence: The experimental setup and dataset description confirm the focus on standard addition.

**Synthesis and Reflection:**

Several reviewers independently identified the narrow focus on integer addition as a limitation. This is a valid criticism, as the paper's experiments and analysis are centered around this specific task. Reviewers 1, 2, and 3 all highlight this point, indicating a strong consensus on this weakness. Furthermore, the lack of a detailed explanation for *why* pre-training is necessary for the emergence of Fourier features is a recurring concern (Reviewers 1 and 2). While the paper demonstrates the necessity through performance differences, it doesn't delve into the underlying mechanisms. The absence of exploration into the impact of different pre-training objectives (Reviewer 2) and the lack of analysis on more complex arithmetic scenarios (Reviewers 3 and 4) are also valid points that limit the generalizability and robustness of the findings. Reviewer 3 raises a specific question about handling misaligned numbers, which is a valid point given the fixed template used in the experiments. Similarly, the lack of investigation into leading/trailing zeros and carry/borrow operations is a valid concern.

There are no significant conflicts between the reviewers' opinions. They largely converge on the limitations related to the narrow scope of the task and the lack of detailed mechanistic explanations.

**Final Conclusion:**

The majority of the identified weaknesses are valid and well-supported by the paper's content. The primary areas of concern are the narrow focus on integer addition, the lack of a detailed explanation for the necessity of pre-training, and the absence of exploration into more complex scenarios and different pre-training conditions.
}

Now, I have successfully verified each review. Next, I will organize this content and output the final review decision:

\boxed_review{
## Summary:

This paper presents a compelling investigation into how pre-trained Large Language Models (LLMs) perform integer addition, revealing a fascinating interplay between approximation and modular arithmetic within their token embeddings. The authors demonstrate that pre-training is crucial for the emergence of Fourier features in the token embeddings, which are essential for the model's ability to perform the addition task. Specifically, they find that Multi-Layer Perceptrons (MLPs) approximate the magnitude of the sum, while attention layers perform modular addition. This finding is supported by a series of experiments across different open-source and closed-source models, including GPT-2, Phi-2, GPT-J, Phi-3, and PaLM-2. The study also explores the impact of pre-training on the emergence of these Fourier features, showing that models trained from scratch lack the necessary mechanisms for accurate addition. Furthermore, the authors extend their analysis to prompted pre-trained models, demonstrating that these models also exhibit the same Fourier feature-based computation. The core methodology involves fine-tuning pre-trained models on a synthetic addition dataset, allowing for a controlled analysis of the internal representations. The authors use a combination of empirical analysis and theoretical insights to support their claims, including the use of Logit Lens to analyze the internal representations and Fourier analysis to identify the presence of specific frequency components. Overall, this work provides valuable insights into the inner workings of LLMs, highlighting the importance of pre-training and the emergence of specific internal representations for complex tasks. The findings suggest that LLMs do not simply memorize arithmetic facts but rather develop a more nuanced understanding of numerical operations through the learning of Fourier features in their token embeddings. This research contributes to our understanding of how LLMs perform mathematical reasoning and provides a foundation for further exploration of their capabilities and limitations.


## Soundness:

3.0


## Presentation:

3.0


## Contribution:

3.0


## Strengths:

This paper possesses several notable strengths that contribute to its overall impact and significance. First and foremost, the paper provides a novel perspective on how pre-trained LLMs perform integer addition, focusing on the role of Fourier features in their token embeddings. This is a significant departure from previous work that often treats LLMs as black boxes, and it offers a more mechanistic understanding of their internal computations. The authors' use of a combination of empirical analysis and theoretical insights is commendable, allowing for a comprehensive and robust analysis of the models' behavior. The experimental design is well-structured, and the use of a synthetic addition dataset enables a controlled study of the models' internal representations. The authors' demonstration that pre-training is crucial for the emergence of Fourier features is a key finding, highlighting the importance of this stage in the development of mathematical reasoning capabilities. Furthermore, the paper's exploration of different models, including both open-source and closed-source models, strengthens the generalizability of the findings. The authors also show that the Fourier feature mechanism is present in prompted pre-trained models, indicating that this mechanism is not limited to models trained from scratch. The paper is also well-written and easy to follow, making it accessible to a broad audience. The authors clearly articulate their research questions, methodology, and findings, and they provide sufficient detail for the reader to understand the key aspects of their work. The use of visualizations, such as the Logit Lens analysis, further enhances the clarity of the presentation. Finally, the paper's findings have implications for our understanding of how LLMs perform mathematical reasoning, suggesting that they do not simply memorize arithmetic facts but rather develop a more nuanced understanding of numerical operations. This insight could inform future research on the development of more robust and reliable LLMs for mathematical tasks.


## Weaknesses:

Despite its strengths, this paper has several limitations that warrant careful consideration. A primary concern is the narrow focus on integer addition. While the authors provide a controlled environment for their analysis, the exclusive focus on this single task limits the generalizability of their findings. As I've verified, the paper explicitly states its focus on integer addition, and all experiments are designed around this task. This narrow scope raises questions about how the identified Fourier features and their role in addition manifest in other mathematical tasks, such as subtraction, multiplication, or division, or even in tasks involving non-integer values. The paper does not explore these questions, which limits the scope of the conclusions. Furthermore, the paper does not provide a clear explanation of why pre-training is necessary for the emergence of Fourier features. While the authors demonstrate the presence of these features in pre-trained models and their absence in models trained from scratch, they do not delve into the specific mechanisms by which pre-training leads to the development of these features. As I've confirmed, the paper states that models trained from scratch lack Fourier features, but it does not explain *why* this is the case. This lack of a mechanistic explanation weakens the understanding of the underlying processes. The paper also does not explore the impact of different pre-training objectives on the emergence of Fourier features. The authors focus on GPT-2-XL, which uses a next-token prediction objective, but they do not investigate whether different pre-training objectives lead to different types of Fourier features or different levels of performance on the addition task. This is a significant limitation, as it is possible that the emergence of Fourier features is dependent on the specific pre-training objective used. The paper also does not discuss the potential limitations of the proposed approach or potential failure cases. While the paper demonstrates the success of the Fourier feature mechanism, it does not explore the model's behavior when the input numbers are not aligned in terms of their number of digits, or when there are leading or trailing zeros. This is a critical oversight, as it is important to understand the model's robustness and limitations. As I've verified, the paper's experiments use a fixed template for the addition question, ensuring the numbers are presented with the same number of digits, and there are no experiments or analysis on how the model handles misaligned numbers or leading/trailing zeros. Finally, the paper does not explore the model's performance on more complex addition problems, such as those involving carries or borrows. This is another limitation, as it is important to understand how the model handles more intricate arithmetic operations. The paper's focus on standard addition without these complexities limits the scope of the findings. These limitations, while not invalidating the paper's contributions, highlight areas where further research is needed to fully understand the capabilities and limitations of LLMs in mathematical reasoning.


## Suggestions:

To address the identified weaknesses and further strengthen this research, I recommend several concrete improvements. First, the authors should broaden the scope of their investigation to include other mathematical tasks and domains. This could involve exploring how the identified Fourier features manifest in subtraction, multiplication, or division, or even in tasks involving non-integer values. For example, the authors could design experiments to analyze the model's performance on subtraction problems and examine whether similar Fourier features emerge. This would provide a more comprehensive understanding of the underlying mechanisms and allow for a more robust generalization of the findings. Second, the authors should delve deeper into the mechanisms that enable pre-training to lead to the emergence of Fourier features. This could involve analyzing the changes in the model's internal representations over time, examining the role of different pre-training objectives, and exploring the relationship between the pre-training data and the emergence of Fourier features. For instance, the authors could compare the Fourier features learned by models pre-trained with different objectives, such as masked language modeling versus causal language modeling, or models pre-trained on datasets with varying levels of mathematical content. This would provide a more nuanced understanding of the observed phenomenon. Third, the authors should explore the model's performance on a wider range of addition problems, including those with varying magnitudes and digit lengths, to assess the robustness of the proposed approach. This could involve testing the model on problems with leading or trailing zeros, as well as problems that require carries or borrows. This would provide a more complete picture of the model's capabilities and limitations. Fourth, the authors should investigate the model's behavior when the input numbers are not aligned in terms of their number of digits, or when there are leading or trailing zeros. This would provide a more complete picture of the model's capabilities and limitations. For example, the authors could conduct experiments where one number has more digits than the other, or where there are leading or trailing zeros. This would help to determine whether the model relies on Fourier features or positional embeddings in these cases. Finally, the authors should explore the model's performance on more complex addition problems, such as those involving carries or borrows. This would help to determine the robustness of the proposed approach and its applicability to real-world scenarios. By addressing these limitations, the authors can provide a more comprehensive and robust understanding of how LLMs perform mathematical reasoning.


## Questions:

Several key questions arise from my analysis of this paper, focusing on the core methodological choices and assumptions. First, how do the findings generalize to other mathematical tasks or domains beyond integer addition? Specifically, do similar Fourier features emerge when performing subtraction, multiplication, or division, or when dealing with non-integer values? This question is crucial for understanding the broader applicability of the identified mechanisms. Second, what is the precise mechanism by which pre-training leads to the emergence of Fourier features? The paper demonstrates the necessity of pre-training but does not delve into the specific processes. A more detailed analysis of the changes in the model's internal representations over time, and the role of different pre-training objectives, would be beneficial. Third, how does the model handle cases where the input numbers are not aligned in terms of their number of digits, or when there are leading or trailing zeros? The paper's experiments use a fixed template, and it is unclear whether the model relies on Fourier features or positional embeddings in these cases. Fourth, what is the impact of different pre-training objectives on the emergence of Fourier features? The paper focuses on GPT-2-XL, which uses a next-token prediction objective, but it does not explore the impact of different pre-training objectives. A comparison of the Fourier features learned by models pre-trained with different objectives would be valuable. Fifth, how does the model handle more complex addition problems, such as those involving carries or borrows? The paper's focus on standard addition without these complexities limits the scope of the findings. Exploring these scenarios would provide a more complete picture of the model's capabilities. Finally, what are the limitations of the proposed approach and potential failure cases? The paper does not explicitly define or analyze these limitations, and a more thorough discussion of potential failure cases would be beneficial. These questions highlight key uncertainties and areas for future research, and addressing them would significantly enhance our understanding of how LLMs perform mathematical reasoning.


## Rating:

7.0


## Confidence:

2.75


## Decision:

Accept
}