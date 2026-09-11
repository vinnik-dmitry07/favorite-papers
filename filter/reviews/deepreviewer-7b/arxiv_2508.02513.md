I will use Standard Mode for comprehensive thinking. As a professional reviewer, I will simulate 4 different reviewers, followed by the verification thinking. Then I will output the Finally Review Output. Let me think - Standard Mode means I will output the original review, followed by the verification thinking. Considering that I am currently in standard mode, I should think from my existing knowledge and consider some related work content when writing about weaknesses. Then I will output the Finally Review Output and Meta Review Output:

\boxed_simreviewers{
## Reviewer 1

### Summary

This paper investigates how large language models (LLMs) perform arithmetic tasks, specifically focusing on addition and subtraction. The authors propose that LLMs process numbers digit by digit, with distinct circuits handling each digit position (units, tens, hundreds, etc.). They use Fisher Score-based feature selection to identify neurons sensitive to individual digit positions and then validate these findings through targeted interventions. The results show that manipulating the activations of specific digit-position circuits leads to predictable changes in the model's output, supporting the modular, compositional nature of arithmetic processing in LLMs.

### Soundness

3

### Presentation

3

### Contribution

2

### Strengths

- The paper presents a novel approach to understanding how LLMs perform arithmetic by identifying digit-position-specific circuits. This modular view of arithmetic processing in LLMs is a valuable contribution to the field.
- The use of Fisher Score for feature selection and targeted interventions provides strong evidence for the causal role of these digit-position circuits in arithmetic tasks. This rigorous methodology strengthens the paper's claims and offers a robust framework for future research.

### Weaknesses

#### Some Related Works


#### comment

 - The study focuses exclusively on addition and subtraction, which limits the generalizability of the findings to other arithmetic operations such as multiplication and division. It is unclear whether the digit-specific processing observed in these operations would extend to more complex tasks involving carries, borrows, and multi-digit operands. The lack of exploration of more complex operations leaves a gap in understanding the robustness of the proposed digit-specific circuits.
- While the paper identifies digit-specific circuits, it does not delve deeply into the underlying mechanisms that enable these circuits to perform arithmetic operations. A more detailed analysis of how these circuits interact with each other and with other parts of the network could provide a more comprehensive understanding of the arithmetic processing pipeline in LLMs. For example, it is not clear how the identified circuits handle carries or borrows, which are crucial for multi-digit arithmetic.
- The paper's reliance on Fisher Score for identifying relevant neurons is a strong point, but it also raises questions about the robustness of the findings. The Fisher Score, while effective, is a heuristic method, and it is possible that other neurons or combinations of neurons could also be involved in the arithmetic process. A more thorough exploration of alternative methods for identifying relevant neurons could strengthen the paper's claims. Furthermore, the paper does not explore the possibility of overlapping circuits, which could be a more efficient way to perform arithmetic.

### Suggestions

The paper would benefit from a more thorough investigation into the generalizability of the identified digit-specific circuits across different arithmetic operations. While the focus on addition and subtraction is a good starting point, the absence of experiments with multiplication and division leaves a significant gap in the study's conclusions. Future work should explore how these circuits adapt to more complex operations, particularly those involving carries and borrows. For instance, the authors could investigate whether the same digit-specific circuits are involved in both addition and multiplication, or if new circuits are required for these operations. This could involve designing experiments that specifically test the performance of the identified circuits on multiplication and division tasks, and analyzing the results to determine if the same patterns of activation are observed. Furthermore, the study should explore the handling of carries and borrows within these circuits, as these are critical for multi-digit arithmetic. This could involve analyzing the activation patterns of the identified circuits during carry and borrow operations, and comparing them to the patterns observed during addition and subtraction.

To enhance the understanding of the underlying mechanisms of the identified circuits, the authors should conduct a more detailed analysis of the interactions between these circuits and other parts of the network. This could involve techniques such as causal mediation analysis to determine the specific roles of the identified circuits in the arithmetic process. For example, the authors could investigate how the activations of the digit-specific circuits influence the activations of other parts of the network, such as the attention mechanism or the feedforward layers. This would provide a more comprehensive understanding of how the identified circuits contribute to the overall arithmetic processing in LLMs. Additionally, the authors should explore the role of attention mechanisms in the arithmetic process, as these mechanisms could play a crucial role in routing information between different parts of the network. This could involve analyzing the attention weights of the model during arithmetic tasks, and comparing them to the activation patterns of the identified circuits.

Finally, the paper should address the limitations of relying solely on Fisher Score for identifying relevant neurons. While Fisher Score is a useful heuristic, it is not a comprehensive method for identifying all relevant neurons in a neural network. The authors should explore alternative methods for identifying relevant neurons, such as gradient-based attribution methods or other feature selection techniques. This would help to ensure that the identified circuits are not specific to the Fisher Score method, and that the findings are robust across different identification methods. Furthermore, the authors should investigate the possibility of overlapping circuits, which could be a more efficient way to perform arithmetic. This could involve analyzing the activation patterns of different neurons and identifying those that are involved in multiple digit positions. This would provide a more nuanced understanding of the arithmetic processing pipeline in LLMs and could lead to more efficient and effective arithmetic circuits.

### Questions

- How do the identified digit-specific circuits handle carries and borrows in arithmetic operations? Are there any specific mechanisms within these circuits that are responsible for managing these critical arithmetic operations?
- Have you considered testing the generalizability of these circuits on more complex arithmetic operations, such as multiplication and division? If so, what were the results?
- Could you elaborate on the potential overlap between digit-specific circuits? Are there any neurons that are involved in multiple digit positions, or are the circuits strictly separated?

### Rating

5

### Confidence

4

**********

## Reviewer 2

### Summary

This paper investigates how LLMs perform arithmetic tasks by identifying digit-specific arithmetic circuits. The authors use Fisher Score-based feature selection to pinpoint MLP neurons sensitive to individual digit positions (units, tens, hundreds) and validate these findings through targeted interventions. The results demonstrate that these digit-specific circuits are causally involved in arithmetic, with each position handling its own computations independently.

### Soundness

3

### Presentation

3

### Contribution

3

### Strengths

1. The paper presents a novel approach by identifying digit-specific arithmetic circuits, moving beyond the traditional view of LLMs using a bag of heuristics. This modular, compositional view of arithmetic processing in LLMs is a significant contribution.
2. The methodology is robust, combining Fisher Score-based feature selection with targeted interventions to validate the identified circuits. The experiments are well-designed, providing strong evidence for the causal role of these circuits in arithmetic tasks.
3. The paper is well-organized, with clear explanations of the methodology and results. The use of heatmaps and visualizations effectively illustrates the digit-specific nature of the identified circuits.

### Weaknesses

#### Some Related Works


#### comment

1. While the paper focuses on addition and subtraction, it would be beneficial to explore how these circuits generalize to more complex operations like multiplication and division. The current analysis leaves open the question of whether the identified digit-specific circuits are unique to addition and subtraction or if similar circuits exist for other arithmetic operations, particularly those involving carries and borrows, which are more complex than simple digit-wise addition or subtraction. The lack of exploration into these more complex operations limits the scope of the conclusions.
2. The study primarily focuses on MLP layers, which contain the neurons that directly control digit outputs. However, it does not explore the role of attention heads or other residual stream components in the arithmetic process. This is a significant limitation, as attention mechanisms could play a crucial role in how information is processed and combined across digit positions. The paper should investigate whether the identified digit-specific circuits interact with attention mechanisms, or if attention is used in a different way to support the arithmetic process. This could involve analyzing the flow of information between MLP layers and attention heads during arithmetic tasks.
3. The paper uses Fisher Score for feature selection, which is a heuristic method. While effective, it is possible that other neurons or combinations of neurons could also be involved in the arithmetic process. A more thorough exploration of alternative methods for identifying relevant neurons could strengthen the findings. For example, gradient-based attribution methods could be used to identify the most influential neurons for each digit position. This would provide a more comprehensive understanding of the neural mechanisms underlying the arithmetic process.

### Suggestions

To address the limitation of focusing solely on addition and subtraction, future work should extend the analysis to more complex arithmetic operations such as multiplication and division. This would involve not only identifying digit-specific circuits but also analyzing how these circuits interact with each other and with other parts of the network, such as attention mechanisms. For example, in multiplication, the process involves multiple digit-wise multiplications and carries, which are not present in simple addition or subtraction. Therefore, the identified digit-specific circuits might need to be adapted or new circuits might need to be formed to handle these more complex operations. The analysis should also investigate whether the identified circuits are consistent across different arithmetic operations or if they are specific to each operation. This would provide a more comprehensive understanding of the neural mechanisms underlying arithmetic processing in LLMs.

To further investigate the role of attention heads, the authors should conduct experiments to analyze the interaction between MLP layers and attention mechanisms during arithmetic tasks. This could involve techniques such as attention visualization or ablation studies to determine the specific role of attention in the arithmetic process. For instance, the authors could analyze the attention weights between different digit positions during arithmetic operations to see if there are any patterns or dependencies. Furthermore, the authors could investigate whether the attention mechanism is used to combine information from different digit-specific circuits or if it is used in a different way to support the arithmetic process. This would provide a more complete picture of how information is processed and combined across digit positions during arithmetic tasks.

Finally, to strengthen the findings regarding the identification of relevant neurons, the authors should explore alternative methods for feature selection beyond Fisher Score. Gradient-based attribution methods, such as Integrated Gradients or SHAP values, could be used to identify the most influential neurons for each digit position. This would provide a more comprehensive understanding of the neural mechanisms underlying the arithmetic process and could potentially reveal additional insights that are not captured by Fisher Score. Additionally, the authors could investigate the overlap between the neurons identified by different feature selection methods to determine the robustness of their findings. This would provide a more robust and reliable understanding of the neural circuits involved in arithmetic processing.

### Questions

1. Could the authors provide more details on how the Fisher Score was calculated and what criteria were used to select the top neurons? This would help in understanding the robustness of the feature selection process.
2. Have the authors considered the potential impact of different model sizes or architectures on the identified digit-specific circuits? It would be valuable to know if the findings generalize across different LLMs.
3. How do the identified digit-specific circuits interact with each other and with other parts of the network, such as attention heads? Further analysis in this area could provide a more complete understanding of the arithmetic processing pipeline.

### Rating

6

### Confidence

3

**********

## Reviewer 3

### Summary

This paper studies how LLMs perform arithmetic tasks. The authors first identify digit-position-specific circuits by using Fisher Score-based feature selection to identify MLP neurons sensitive to each digit position. Then they conduct targeted interventions on the identified digit-position circuits to verify their causal role in arithmetic tasks.

### Soundness

3

### Presentation

3

### Contribution

3

### Strengths

- The paper is well-written and easy to follow.
- The experiments are well-designed and the results are convincing.
- The findings are novel and interesting.

### Weaknesses

#### Some Related Works


#### comment

 - The experiments are only conducted on simple addition and subtraction tasks. It would be interesting to see if the findings generalize to more complex tasks, such as multiplication and division.
- The paper only considers the MLP layers, which contain the neurons that directly control digit outputs. It would be interesting to see if the findings generalize to other types of layers, such as attention layers.
- The paper only considers the digit position-specific circuits, which contain the neurons that directly control digit outputs. It would be interesting to see if the findings generalize to other types of circuits, such as the circuits that control the carry operation.

### Suggestions

The study's focus on simple addition and subtraction, while providing a clear starting point, limits the generalizability of the findings. Future work should explore more complex arithmetic operations such as multiplication and division. These operations involve carry propagation and more intricate digit interactions, which could reveal whether the identified digit-position-specific circuits are sufficient or if additional circuits are required for more complex tasks. For example, in multiplication, the process involves multiple digit-wise multiplications and the accumulation of partial products with appropriate shifts and carry propagation. It would be valuable to investigate if the same digit-specific circuits are active during these operations, or if new circuits are formed, and how these new circuits interact with the existing ones. Furthermore, the study should consider the impact of different algorithms for these operations, as the internal representations and processing steps might vary significantly.

While the paper focuses on MLP layers, it is crucial to investigate the role of attention mechanisms in arithmetic processing. The attention mechanism is a key component of transformer models, and it is plausible that it plays a significant role in how LLMs perform arithmetic. For instance, attention might be used to align digits across different numbers or to manage carry propagation. Analyzing the attention patterns during arithmetic tasks could provide insights into how information is routed and processed within the network. It would be beneficial to examine the attention weights between different digit positions and how these weights change during the execution of arithmetic operations. This could involve techniques such as attention visualization or ablation studies to understand the specific roles of attention in the arithmetic process. Furthermore, it would be interesting to see if the attention mechanism is consistent across different arithmetic operations or if it varies depending on the task.

Finally, the study should explore the role of circuits beyond the digit-position-specific circuits. While these circuits are important for digit-wise processing, they might not be sufficient for all aspects of arithmetic. For example, the carry operation is a critical part of arithmetic, and it is likely that dedicated circuits are involved in this process. Analyzing the neural activity during carry propagation could reveal the existence of specialized circuits and how they interact with the digit-position-specific circuits. This could involve techniques such as causal mediation analysis to identify the specific pathways through which carry information is processed. It would also be interesting to see if the circuits involved in carry propagation are consistent across different arithmetic operations or if they vary depending on the task. A more comprehensive analysis of the neural circuits involved in arithmetic would provide a more complete understanding of how LLMs perform these tasks.

### Questions

Please see the weaknesses.

### Rating

6

### Confidence

4

**********

## Reviewer 4

### Summary

This paper investigates how large language models (LLMs) perform arithmetic tasks by identifying digit-position-specific circuits. The authors use Fisher Score-based feature selection to pinpoint MLP neurons sensitive to individual digit positions (units, tens, hundreds) and validate these findings through targeted interventions. The results show that manipulating the activations of specific digit-position circuits leads to predictable changes in the model's output, supporting the modular, compositional nature of arithmetic processing in LLMs.

### Soundness

3

### Presentation

3

### Contribution

3

### Strengths

1. The paper presents a novel approach by identifying digit-position-specific circuits, moving beyond the traditional view of LLMs using a bag of heuristics. This modular, compositional view of arithmetic processing in LLMs is a significant contribution.
2. The methodology is robust, combining Fisher Score-based feature selection with targeted interventions to validate the identified circuits. The experiments are well-designed, providing strong evidence for the causal role of these circuits in arithmetic tasks.
3. The paper is well-organized, with clear explanations of the methodology and results. The use of heatmaps and visualizations effectively illustrates the digit-specific nature of the identified circuits.

### Weaknesses

#### Some Related Works


#### comment

1. While the paper focuses on addition and subtraction, it would be beneficial to explore how these circuits generalize to more complex operations like multiplication and division. The current analysis leaves open the question of whether the identified digit-specific circuits are unique to addition and subtraction or if similar circuits exist for other arithmetic operations, particularly those involving carries and borrows, which are more complex than simple digit-wise addition or subtraction. The lack of exploration into these more complex operations limits the scope of the conclusions.
2. The study primarily focuses on MLP layers, which contain the neurons that directly control digit outputs. However, it does not explore the role of attention heads or other residual stream components in the arithmetic process. This is a significant limitation, as attention mechanisms could play a crucial role in how information is processed and combined across digit positions. The paper should investigate whether the identified digit-specific circuits interact with attention mechanisms, or if attention is used in a different way to support the arithmetic process. This could involve analyzing the flow of information between MLP layers and attention heads during arithmetic tasks.
3. The paper uses Fisher Score for feature selection, which is a heuristic method. While effective, it is possible that other neurons or combinations of neurons could also be involved in the arithmetic process. A more thorough exploration of alternative methods for identifying relevant neurons could strengthen the findings. For example, gradient-based attribution methods could be used to identify the most influential neurons for each digit position. This would provide a more comprehensive understanding of the neural mechanisms underlying the arithmetic process.

### Suggestions

To address the limitation of focusing solely on addition and subtraction, future work should extend the analysis to more complex arithmetic operations such as multiplication and division. This would involve not only identifying digit-specific circuits but also analyzing how these circuits interact with each other and with other parts of the network, such as attention mechanisms. For example, in multiplication, the process involves multiple digit-wise multiplications and carries, which are not present in simple addition or subtraction. Therefore, the identified digit-specific circuits might need to be adapted or new circuits might need to be formed to handle these more complex operations. The analysis should also investigate whether the identified circuits are consistent across different arithmetic operations or if they are specific to each operation. This would provide a more comprehensive understanding of the neural mechanisms underlying arithmetic processing in LLMs.

To further investigate the role of attention heads, the authors should conduct experiments to analyze the interaction between MLP layers and attention mechanisms during arithmetic tasks. This could involve techniques such as attention visualization or ablation studies to determine the specific role of attention in the arithmetic process. For instance, the authors could analyze the attention weights between different digit positions during arithmetic operations to see if there are any patterns or dependencies. Furthermore, the authors could investigate whether the attention mechanism is used to combine information from different digit-specific circuits or if it is used in a different way to support the arithmetic process. This would provide a more complete picture of how information is processed and combined across digit positions during arithmetic tasks.

Finally, to strengthen the findings regarding the identification of relevant neurons, the authors should explore alternative methods for feature selection beyond Fisher Score. Gradient-based attribution methods, such as Integrated Gradients or SHAP values, could be used to identify the most influential neurons for each digit position. This would provide a more comprehensive understanding of the neural mechanisms underlying the arithmetic process and could potentially reveal additional insights that are not captured by Fisher Score. Additionally, the authors could investigate the overlap between the neurons identified by different feature selection methods to determine the robustness of their findings. This would provide a more robust and reliable understanding of the neural circuits involved in arithmetic processing.

### Questions

1. How do the identified digit-specific circuits handle carries and borrows in arithmetic operations? Are there any specific mechanisms within these circuits that are responsible for managing these critical arithmetic operations?
2. Have you considered testing the generalizability of these circuits on more complex arithmetic operations, such as multiplication and division? If so, what were the results?
3. Could you elaborate on the potential overlap between digit-specific circuits? Are there any neurons that are involved in multiple digit positions, or are the circuits strictly separated?

### Rating

8

### Confidence

4

**********

}

I have finished generating simulated reviews from 4 reviewers. Next, I will generate verification content for these reviews:

\boxed_verification{
The user wants me to validate weaknesses identified by reviewers in a given paper. I need to go through each reviewer's comments and find evidence in the paper to support their claims.

Plan:
1. Read each reviewer's weakness.
2. Find the corresponding section in the paper.
3. Look for evidence (quotes, experimental details, missing citations, etc.) to support the weakness.
4. If the weakness is about missing information, check if that information is indeed absent.
5. If there are conflicting opinions, address them in the synthesis.
6. Output the validation in the specified format.
**Review 1 Weaknesses:**

1. Weakness Statement:
[While the paper focuses on addition and subtraction, it would be beneficial to explore how these circuits generalize to more complex operations like multiplication and division. The current analysis leaves open the question of whether the identified digit-specific circuits are unique to addition and subtraction or if similar circuits exist for other arithmetic operations, particularly those involving carries and borrows, which are more complex than simple digit-wise addition or subtraction. The lack of exploration into these more complex operations limits the scope of the conclusions.]

2. Evidence Collection:
b) Experiment-related Evidence:
   - The paper explicitly states the focus on addition and subtraction in the "Main Idea" section: "The study focuses on identifying and validating digit-position-specific arithmetic circuits in large language models (LLMs) for simple arithmetic tasks, specifically addition and subtraction."
   - The "Method" section details the data generation for addition and subtraction: "We generate a simple addition dataset D_{add} and subtraction dataset D_{sub} by generating 1000 addition and 1000 subtraction prompts respectively."
   - The "Experiments" section also confirms the focus: "We evaluate four decoder-only transformer models: LLaMA3-8B, LLaMA3-70B, OLMo 2 7B, and Gemma 2 9B." and the datasets used are "addition dataset D_{add} and subtraction dataset D_{sub}".

3. Literature Gap Analysis:
   - The paper does not cite any work that specifically investigates digit-specific circuits for multiplication or division in LLMs.

4. Validation Analysis:
   - The paper clearly states its focus on addition and subtraction.
   - The experimental setup and results are solely based on these two operations.
   - The reviewer correctly points out the limitation of not exploring more complex operations like multiplication and division, which involve carries and borrows.

5. Conclusion:
   - Validity status: Valid
   - Confidence level: High
   - Key supporting evidence: Explicit statement of focus on addition and subtraction, experimental setup and results based on these operations.

1. Weakness Statement:
[The study primarily focuses on MLP layers, which contain the neurons that directly control digit outputs. However, it does not explore the role of attention heads or other residual stream components in the arithmetic process. This is a significant limitation, as attention mechanisms could play a crucial role in how information is processed and combined across digit positions. The paper should investigate whether the identified digit-specific circuits interact with attention mechanisms, or if attention is used in a different way to support the arithmetic process. This could involve techniques such as causal mediation analysis to determine the specific roles of the identified circuits in the arithmetic process. For example, the authors could analyze the attention weights between different digit positions during arithmetic tasks, and comparing them to the activation patterns of the identified circuits.]

2. Evidence Collection:
a) Method-related Evidence:
   - The "Method" section states: "We focus our main analyses on LLaMA3-8B in the main text and report detailed analyses showing similar results for Olmo 2 7B and LLaMA3 70B in Appendices E and F."
   - The "Data for Intervention Experiments" subsection mentions: "We construct two addition datasets D a d d , o p p D_{add, opp} and D a d d , o p p D_{add, op2} where operator o = + \mathrm{o} = { + } \mathrm{o} = { + } and operands A , B , C ∈ { 1 0 0 , … , 9 9 9 } A,B,C\in\{ 100 , \ldots , 999 \} \mathrm{ operands A , B , C \in \{ 100 , \ldots , 999 \} } . To isolate digit-wise computations and prevent interactions between digit positions, we construct all data such that no carry occurs in any digit position."
   - The "Causal Verification via Interventions" subsection describes the intervention process: "We then measure the model’s output distribution over all 8 possible digit-wise combinations of the base and source results (e.g., bbb , sbb , bsb , etc., where e.g. sbb indicates the the hundreths digits correspond to the source result and the other two digits to the base result). If our independent digit-wise circuit hypothesis is correct, a position-specific circuit should shift probability mass only toward the expected variant (e.g. for an intervention on hundreds digits sbb )."
   - The paper does not mention or analyze attention mechanisms or residual stream components.

3. Literature Gap Analysis:
   - The paper does not cite any work that specifically investigates the role of attention heads in arithmetic processing in LLMs.

4. Validation Analysis:
   - The paper's methodology focuses on MLP layers and digit-wise interventions.
   - There is no mention of analyzing attention weights or interactions between MLP layers and attention mechanisms.
   - The reviewer correctly identifies the absence of investigation into attention mechanisms.

5. Conclusion:
   - Validity status: Valid
   - Confidence level: High
   - Key supporting evidence: Focus on MLP layers in the methodology, lack of mention of attention mechanisms in the experimental design.

1. Weakness Statement:
[The paper uses Fisher Score for feature selection, which is a heuristic method. While effective, it is possible that other neurons or combinations of neurons could also be involved in the arithmetic process. A more thorough exploration of alternative methods for identifying relevant neurons could strengthen the findings. For example, gradient-based attribution methods or other feature selection techniques could be used to identify the most influential neurons for each digit position. This would provide a more comprehensive understanding of the neural mechanisms underlying the arithmetic process and could potentially reveal additional insights that are not captured by Fisher Score. Furthermore, the paper does not explore the possibility of overlapping circuits, which could be a more efficient way to perform arithmetic.]

2. Evidence Collection:
a) Method-related Evidence:
   - The "Identifying Digit-Specific Neurons" subsection states: "We employ Fisher Score Duda and Hartvigsen (2012) ; Sun et al. (2021) and validate their causal role via targeted interventions Vig et al. (2020) ; Meng et al. (2023) : For each MLP layer l l in model m m and o ∈ { + , − } \mathrm{o}\in\{+,-\} and A , B , C ∈ { 1 0 0 , … , 9 9 9 } \mathrm { operands A , B , C ∈ \{ 100 , … , 999 \} } . Fisher Scores are a relative metric, therefore choosing a reasonable threshold for circuit membership is a hyperparameter tuning problem. Generally speaking, Fisher scores close to 0 indicate a lack of discriminative power, scores between 0.1 and 1.0 weak to moderate discriminability, and values above 1.0 strong discriminability."
   - The paper does not mention or explore alternative feature selection methods like gradient-based attribution.

3. Literature Gap Analysis:
   - The paper cites the original Fisher Score paper but does not discuss or compare it with other feature selection methods commonly used in interpretability research.

4. Validation Analysis:
   - The paper explicitly states the use of Fisher Score.
   - There is no mention of exploring alternative methods.
   - The reviewer correctly points out the heuristic nature of Fisher Score and the potential for missing other relevant neurons.

5. Conclusion:
   - Validity status: Valid
   - Confidence level: High
   - Key supporting evidence: Explicit mention of Fisher Score as the sole feature selection method.

**Review 2 Weaknesses:**

1. Weakness Statement:
[- The experiments are only conducted on simple addition and subtraction tasks. It would be interesting to see if the findings generalize to more complex tasks, such as multiplication and division.]

2. Evidence Collection:
b) Experiment-related Evidence:
   - As identified in Review 1, the paper explicitly states its focus on addition and subtraction.

3. Literature Gap Analysis:
   - The paper does not cite work exploring more complex arithmetic tasks.

4. Validation Analysis:
   - This is the same point as the first weakness in Review 1, and the validation remains the same.

5. Conclusion:
   - Validity status: Valid
   - Confidence level: High
   - Key supporting evidence: Explicit statement of focus on addition and subtraction.

1. Weakness Statement:
[- The paper only considers the MLP layers, which contain the neurons that directly control digit outputs. It would be interesting to see if the findings generalize to other types of layers, such as attention layers.]

2. Evidence Collection:
a) Method-related Evidence:
   - As identified in Review 1, the methodology focuses on MLP layers.

3. Literature Gap Analysis:
   - The paper does not cite work exploring the role of attention layers in arithmetic.

4. Validation Analysis:
   - This is the same point as the second weakness in Review 1, and the validation remains the same.

5. Conclusion:
   - Validity status: Valid
   - Confidence level: High
   - Key supporting evidence: Focus on MLP layers in the methodology.

1. Weakness Statement:
[- The paper only considers the digit position-specific circuits, which contain the neurons that directly control digit outputs. It would be interesting to see if the findings generalize to other types of circuits, such as the circuits that control the carry operation.]

2. Evidence Collection:
a) Method-related Evidence:
   - The paper's focus is on identifying and validating circuits based on digit position.
   - There is no mention of investigating circuits related to carry operations.

3. Literature Gap Analysis:
   - The paper does not cite work exploring carry operation circuits in LLMs.

4. Validation Analysis:
   - This is a valid point. The paper's scope is limited to digit-specific circuits.
   - The reviewer correctly points out the absence of investigation into circuits related to carry operations.

5. Conclusion:
   - Validity status: Valid
   - Confidence level: High
   - Key supporting evidence: Focus on digit position-specific circuits in the methodology.

**Review 3 Weaknesses:**

1. Weakness Statement:
[The study focuses exclusively on addition and subtraction, which limits the generalizability of the findings to other arithmetic operations such as multiplication and division. It is unclear whether the digit-specific processing observed in these operations would extend to more complex tasks involving carries, borrows, and multi-digit operands. The lack of exploration of more complex operations leaves a gap in understanding the robustness of the proposed digit-specific circuits.]

2. Evidence Collection:
b) Experiment-related Evidence:
   - As previously established, the paper focuses on addition and subtraction.

3. Literature Gap Analysis:
   - No discussion of multiplication/division in the context of digit-specific circuits.

4. Validation Analysis:
   - This is a restatement of the first weakness from Review 1 and 2, and the validation remains consistent.

5. Conclusion:
   - Validity status: Valid
   - Confidence level: High
   - Key supporting evidence: Focus on addition and subtraction.

1. Weakness Statement:
[While the paper identifies digit-specific circuits, it does not delve deeply into the underlying mechanisms that enable these circuits to perform arithmetic operations. A more detailed analysis of how these circuits interact with each other and with other parts of the network could provide a more comprehensive understanding of the arithmetic processing pipeline in LLMs. For example, it is not clear how the identified circuits handle carries or borrows, which are crucial for multi-digit arithmetic.]

2. Evidence Collection:
a) Method-related Evidence:
   - The paper identifies digit-specific circuits and validates their causal role.
   - The "Causal Verification via Interventions" section describes the intervention method but doesn't analyze interactions between circuits.
   - The paper does not explicitly analyze how the circuits handle carries or borrows.

3. Literature Gap Analysis:
   - The paper does not cite work that deeply analyzes the interaction between digit-specific circuits or their handling of carries/borrows.

4. Validation Analysis:
   - The paper focuses on identifying and validating the existence of digit-specific circuits.
   - It does not provide a detailed analysis of their internal interactions or their handling of carries/borrows.

5. Conclusion:
   - Validity status: Valid
   - Confidence level: High
   - Key supporting evidence: Focus on identification and validation, lack of analysis on circuit interactions and carry/borrow handling.

1. Weakness Statement:
[The paper's reliance on Fisher Score for identifying relevant neurons is a strong point, but it also raises questions about the robustness of the findings. The Fisher Score, while effective, is a heuristic method, and it is possible that other neurons or combinations of neurons could also be involved in the arithmetic process. A more thorough exploration of alternative methods for identifying relevant neurons could strengthen the paper's claims. Furthermore, the paper does not explore the possibility of overlapping circuits, which could be a more efficient way to perform arithmetic.]

2. Evidence Collection:
a) Method-related Evidence:
   - As previously established, the paper uses Fisher Score for feature selection.
   - There is no exploration of alternative methods or overlapping circuits.

3. Literature Gap Analysis:
   - No discussion of alternative feature selection methods or circuit overlap.

4. Validation Analysis:
   - This is a restatement of the third weakness from Review 1, and the validation remains consistent.

5. Conclusion:
   - Validity status: Valid
   - Confidence level: High
   - Key supporting evidence: Use of Fisher Score without exploring alternatives or circuit overlap.

**Review 4 Weaknesses:**

1. Weakness Statement:
[While the paper focuses on addition and subtraction, it would be beneficial to explore how these circuits generalize to more complex operations like multiplication and division. The current analysis leaves open the question of whether the identified digit-specific circuits are unique to addition and subtraction or if similar circuits exist for other arithmetic operations, particularly those involving carries and borrows, which are more complex than simple digit-wise addition or subtraction. The lack of exploration into these more complex operations limits the scope of the conclusions.]

2. Evidence Collection:
b) Experiment-related Evidence:
   - As previously established, the paper focuses on addition and subtraction.

3. Literature Gap Analysis:
   - No discussion of multiplication/division in the context of digit-specific circuits.

4. Validation Analysis:
   - This is a restatement of the first weakness from Review 1, 2, and 3, and the validation remains consistent.

5. Conclusion:
   - Validity status: Valid
   - Confidence level: High
   - Key supporting evidence: Focus on addition and subtraction.

1. Weakness Statement:
[The study primarily focuses on MLP layers, which contain the neurons that directly control digit outputs. However, it does not explore the role of attention heads or other residual stream components in the arithmetic process. This is a significant limitation, as attention mechanisms could play a crucial role in how information is processed and combined across digit positions. The paper should investigate whether the identified digit-specific circuits interact with attention mechanisms, or if attention is used in a different way to support the arithmetic process. This could involve techniques such as causal mediation analysis to determine the specific roles of the identified circuits in the arithmetic process. For example, the authors could analyze the attention weights between different digit positions during arithmetic tasks, and comparing them to the activation patterns of the identified circuits.]

2. Evidence Collection:
a) Method-related Evidence:
   - As previously established, the methodology focuses on MLP layers.

3. Literature Gap Analysis:
   - No discussion of attention mechanisms in the context of arithmetic processing.

4. Validation Analysis:
   - This is a restatement of the second weakness from Review 1 and 2, and the validation remains consistent.

5. Conclusion:
   - Validity status: Valid
   - Confidence level: High
   - Key supporting evidence: Focus on MLP layers.

1. Weakness Statement:
[The paper uses Fisher Score for feature selection, which is a heuristic method. While effective, it is possible that other neurons or combinations of neurons could also be involved in the arithmetic process. A more thorough exploration of alternative methods for identifying relevant neurons could strengthen the findings. For example, gradient-based attribution methods or other feature selection techniques could be used to identify the most influential neurons for each digit position. This would provide a more comprehensive understanding of the neural mechanisms underlying the arithmetic process and could potentially reveal additional insights that are not captured by Fisher Score. Furthermore, the paper does not explore the possibility of overlapping circuits, which could be a more efficient way to perform arithmetic.]

2. Evidence Collection:
a) Method-related Evidence:
   - As previously established, the paper uses Fisher Score for feature selection.

3. Literature Gap Analysis:
   - No discussion of alternative feature selection methods or circuit overlap.

4. Validation Analysis:
   - This is a restatement of the third weakness from Review 1, 3, and 4, and the validation remains consistent.

5. Conclusion:
   - Validity status: Valid
   - Confidence level: High
   - Key supporting evidence: Use of Fisher Score without exploring alternatives or circuit overlap.

**Synthesis and Reflection:**

All reviewers raise consistent concerns regarding the limited scope of the study to addition and subtraction, the focus on MLP layers, and the reliance on Fisher Score for feature selection. There are no significant contradictions between the reviewers' opinions; they all converge on the same key limitations. The reviewers provide specific suggestions for improvement, such as extending the analysis to more complex arithmetic operations, investigating the role of attention mechanisms, and exploring alternative feature selection methods. These criticisms are well-supported by the paper's content, which clearly states its focus on addition and subtraction and its methodology centered around MLP layers and Fisher Score. The confidence level in the validity of these criticisms is high, as they are based on direct observations of the paper's content and methodology.

**Final Conclusion:**

The identified weaknesses are valid and well-supported by the paper's content. The reviewers correctly point out the limitations of focusing solely on addition and subtraction, the lack of investigation into attention mechanisms, and the heuristic nature of the feature selection method.
}

Now, I have successfully verified each review. Next, I will organize this content and output the final review decision:

\boxed_review{
## Summary:

This paper presents a compelling investigation into how large language models (LLMs) perform arithmetic tasks, specifically focusing on addition and subtraction. The authors propose a modular, compositional view of arithmetic processing, suggesting that LLMs achieve this through digit-position-specific circuits. To identify these circuits, they employ a Fisher Score-based feature selection method to pinpoint MLP neurons that are sensitive to individual digit positions (units, tens, hundreds, etc.). The core methodology involves generating datasets of addition and subtraction problems with controlled digit positions, followed by targeted interventions on the activations of the identified digit-specific neurons. These interventions involve replacing the neuron activations with those from a source prompt, allowing the authors to observe the causal role of these circuits in arithmetic. The main empirical finding is that manipulating the activations of specific digit-position circuits leads to predictable changes in the model's output, corresponding to the expected digit-wise changes in the result. This provides strong evidence for the existence of digit-specific circuits and their causal role in arithmetic processing. The authors further explore the generalizability of these circuits by analyzing the overlap between digit-specific circuits across different arithmetic problems and model sizes. Overall, this work offers a novel perspective on how LLMs perform arithmetic, moving beyond the traditional view of using a bag of heuristics to a modular, compositional approach. The findings suggest that LLMs may decompose arithmetic tasks into digit-wise computations, processing each digit position independently before combining the results. This modular view is a significant contribution to our understanding of how LLMs handle numerical information and provides a foundation for further research into the arithmetic capabilities of these models. The paper's methodology is rigorous, combining feature selection with targeted interventions to validate the identified circuits. The results are compelling, demonstrating a causal link between digit-specific neuron activations and the model's arithmetic output. This work not only advances our understanding of LLMs but also provides a framework for analyzing other complex tasks within these models. The authors' approach of using Fisher Scores for feature selection and targeted interventions is a robust framework for future research in this area. The study's focus on digit-specific circuits is a valuable contribution to the field, offering a new perspective on how LLMs perform arithmetic tasks. The findings suggest that LLMs may be leveraging a modular, compositional approach, which is a significant step forward in understanding their internal mechanisms.


## Soundness:

3.0


## Presentation:

3.0


## Contribution:

2.75


## Strengths:

This paper presents several notable strengths that contribute to its overall impact and significance. First and foremost, the paper introduces a novel approach by identifying digit-specific arithmetic circuits within LLMs. This modular, compositional view of arithmetic processing is a significant departure from the traditional view of LLMs using a bag of heuristics. This shift in perspective is a valuable contribution to the field, offering a new lens through which to understand how these models perform arithmetic tasks. The methodology is also a key strength of the paper. The authors combine Fisher Score-based feature selection with targeted interventions to validate the identified circuits. The use of Fisher Score allows for the identification of neurons that are sensitive to specific digit positions, while the targeted interventions provide strong evidence for the causal role of these circuits in arithmetic. This rigorous methodology provides a robust framework for future research in this area. The experiments are well-designed and the results are compelling. The authors generate datasets of addition and subtraction problems with controlled digit positions, and then manipulate the activations of the identified digit-specific neurons. The results clearly demonstrate that these interventions have a predictable and causal effect on the model's output, supporting the existence of digit-specific circuits. The paper is also well-organized, with clear explanations of the methodology and results. The use of heatmaps and visualizations effectively illustrates the digit-specific nature of the identified circuits. The paper's findings are novel and interesting, offering a robust framework for future research on arithmetic operations in LLMs. The authors' approach of using Fisher Scores for feature selection and targeted interventions is a robust framework for future research in this area. The study's focus on digit-specific circuits is a valuable contribution to the field, offering a new perspective on how LLMs perform arithmetic tasks. The findings suggest that LLMs may be leveraging a modular, compositional approach, which is a significant step forward in understanding their internal mechanisms. The paper's overall contribution is significant, providing a new understanding of how LLMs perform arithmetic tasks and opening up new avenues for research in this area.


## Weaknesses:

While this paper presents a compelling analysis of digit-specific circuits in LLMs, several limitations warrant careful consideration. First, the study's focus on addition and subtraction, while providing a clear starting point, limits the generalizability of the findings to other arithmetic operations such as multiplication and division. As the authors themselves state, the study focuses on "simple arithmetic tasks, specifically addition and subtraction." This narrow focus leaves open the question of whether the identified digit-specific circuits are unique to these operations or if similar circuits exist for more complex tasks. The absence of experiments with multiplication and division, which involve carries and borrows, is a significant limitation. The lack of exploration into these more complex operations limits the scope of the conclusions and raises questions about the robustness of the proposed digit-specific circuits. This is a high-confidence issue, as the paper explicitly states its focus on addition and subtraction, and the experimental setup and results are solely based on these two operations. Second, the study primarily focuses on MLP layers, which contain the neurons that directly control digit outputs. The paper does not explore the role of attention heads or other residual stream components in the arithmetic process. This is a significant limitation, as attention mechanisms could play a crucial role in how information is processed and combined across digit positions. The paper does not investigate whether the identified digit-specific circuits interact with attention mechanisms, or if attention is used in a different way to support the arithmetic process. The absence of analysis into attention mechanisms limits the understanding of the underlying arithmetic process in LLMs. This is a high-confidence issue, as the paper's methodology focuses on MLP layers and does not include any analysis of attention mechanisms. Third, the paper relies on Fisher Score for feature selection, which is a heuristic method. While effective, it is possible that other neurons or combinations of neurons could also be involved in the arithmetic process. The paper does not explore alternative methods for feature selection, such as gradient-based attribution methods, which could potentially reveal additional insights. The use of Fisher Score without exploring alternatives limits the robustness of the findings. This is a high-confidence issue, as the paper explicitly states the use of Fisher Score as the sole feature selection method and does not include any discussion of alternative methods. Finally, the paper does not explore the possibility of overlapping circuits, which could be a more efficient way to perform arithmetic. The paper focuses on identifying and validating digit-specific circuits but does not analyze whether these circuits are distinct or if there is any overlap between them. This is a high-confidence issue, as the paper's methodology and results are focused on identifying distinct digit-specific circuits without any analysis of potential overlap. These limitations, while not invalidating the paper's findings, highlight areas where further research is needed to fully understand the arithmetic capabilities of LLMs.


## Suggestions:

To address the identified weaknesses and further strengthen this research, I recommend several concrete improvements. First, future work should extend the analysis to more complex arithmetic operations, such as multiplication and division. This would involve not only identifying digit-specific circuits but also analyzing how these circuits interact with each other and with other parts of the network, such as attention mechanisms. For example, in multiplication, the process involves multiple digit-wise multiplications and the accumulation of partial products with appropriate shifts and carry propagation. It would be valuable to investigate if the same digit-specific circuits are active during these operations, or if new circuits are formed, and how these new circuits interact with the existing ones. This would provide a more comprehensive understanding of the neural mechanisms underlying arithmetic processing in LLMs. Second, to further investigate the role of attention heads, the authors should conduct experiments to analyze the interaction between MLP layers and attention mechanisms during arithmetic tasks. This could involve techniques such as attention visualization or ablation studies to determine the specific role of attention in the arithmetic process. For instance, the authors could analyze the attention weights between different digit positions during arithmetic operations to see if there are any patterns or dependencies. Furthermore, the authors could investigate whether the attention mechanism is used to combine information from different digit-specific circuits or if it is used in a different way to support the arithmetic process. This would provide a more complete picture of how information is processed and combined across digit positions during arithmetic tasks. Third, to strengthen the findings regarding the identification of relevant neurons, the authors should explore alternative methods for feature selection beyond Fisher Score. Gradient-based attribution methods, such as Integrated Gradients or SHAP values, could be used to identify the most influential neurons for each digit position. This would provide a more comprehensive understanding of the neural mechanisms underlying the arithmetic process and could potentially reveal additional insights that are not captured by Fisher Score. Additionally, the authors could investigate the overlap between the neurons identified by different feature selection methods to determine the robustness of their findings. This would provide a more robust and reliable understanding of the neural circuits involved in arithmetic processing. Finally, the authors should explore the possibility of overlapping circuits. This could involve analyzing the activation patterns of different neurons and identifying those that are involved in multiple digit positions. This would provide a more nuanced understanding of the arithmetic processing pipeline in LLMs and could lead to more efficient and effective arithmetic circuits. These suggestions are all concrete and actionable, and they directly address the limitations identified in the current study. Implementing these changes would significantly enhance the robustness and generalizability of the findings.


## Questions:

Several key questions arise from my analysis of this paper, focusing on methodological choices and potential extensions of the research. First, how do the identified digit-specific circuits handle carries and borrows in arithmetic operations? The paper focuses on simple addition and subtraction, which do not involve carries or borrows. It would be valuable to understand how these circuits interact with other parts of the network to manage these critical arithmetic operations, particularly in more complex tasks like multiplication and division. Second, have the authors considered testing the generalizability of these circuits on more complex arithmetic operations, such as multiplication and division? If so, what were the results? The current analysis is limited to addition and subtraction, and it is unclear whether the identified digit-specific circuits are consistent across different arithmetic operations. Third, could the authors elaborate on the potential overlap between digit-specific circuits? Are there any neurons that are involved in multiple digit positions, or are the circuits strictly separated? The paper does not explore the possibility of overlapping circuits, and it would be valuable to understand if there is any redundancy or shared functionality between these circuits. Fourth, could the authors provide more details on how the Fisher Score was calculated and what criteria were used to select the top neurons? This would help in understanding the robustness of the feature selection process. Fifth, have the authors considered the potential impact of different model sizes or architectures on the identified digit-specific circuits? It would be valuable to know if the findings generalize across different LLMs. Finally, how do the identified digit-specific circuits interact with each other and with other parts of the network, such as attention mechanisms? Further analysis in this area could provide a more complete understanding of the arithmetic processing pipeline in LLMs. These questions target core methodological choices and seek clarification of critical assumptions, aiming to further refine our understanding of the arithmetic capabilities of LLMs.


## Rating:

6.25


## Confidence:

3.75


## Decision:

Accept
}