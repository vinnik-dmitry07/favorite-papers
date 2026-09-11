I will use Standard Mode for comprehensive thinking. As a professional reviewer, I will simulate 4 different reviewers, followed by the verification thinking. Then I will output the Finally Review Output. Let me think - Standard Mode means I will output the original review, followed by the verification thinking. Considering that I am currently in standard mode, I should think from my existing knowledge and consider some related work content when writing about weaknesses. Then I will output the Finally Review Output and Meta Review Output:

\boxed_simreviewers{
## Reviewer 1

### Summary

This paper investigates how language models (LMs) compare quantities with measurement units, such as 110 cm and 1.2 m. The authors find that LMs struggle near the comparison boundary, where small changes in value determine the correct answer. Through surrogate analysis, they show that LMs rely on numerical and unit-scale cues rather than exact shared-scale conversions. Causal interventions confirm that these cues influence LM decisions. The study provides a controlled case study of how LMs combine numerical and symbolic measurement units, highlighting limitations in their unit handling.

### Soundness

3

### Presentation

3

### Contribution

3

### Strengths

- The paper addresses a novel and important problem in the field of language models, specifically focusing on how they compare quantities with measurement units. This is a critical area of research as it impacts the reliability and accuracy of LMs in real-world applications.
- The authors conduct a thorough analysis, employing surrogate models and causal interventions to understand the internal mechanisms of LMs. This multi-faceted approach strengthens the validity of their findings.
- The paper is well-structured and clearly written, making it accessible to both experts and non-experts in the field. The use of figures and tables effectively communicates the key results and insights.

### Weaknesses

#### Some Related Works


#### comment

 - The study focuses on controlled, single-step comparisons, which may not fully capture the complexities of real-world scenarios involving multiple units or more intricate calculations. This limitation could affect the generalizability of the findings.
- The reliance on linear models for surrogate analysis might oversimplify the underlying mechanisms of LMs, potentially missing more complex interactions between cues. The use of ridge regression, while interpretable, may not fully capture the non-linear relationships that could be present in the LM's internal representations.
- The paper could benefit from a more detailed discussion of the limitations of the proposed approach and potential avenues for future research. For example, the current study does not explore how the model handles comparisons involving more complex units or quantities, such as those involving prefixes (e.g., kilometer vs. meter) or non-standard units. Furthermore, the study does not investigate the model's performance when the units are not explicitly stated but are implied by the context.

### Suggestions

The authors should consider expanding their analysis to include more complex scenarios, such as comparisons involving multiple units or quantities with prefixes. This would provide a more comprehensive understanding of the model's capabilities and limitations. For instance, the study could investigate how the model compares 1.5 km and 1500 m, or 2.5 kg and 2500 g. Additionally, the authors could explore the model's performance when units are not explicitly stated but are implied by the context, such as comparing "a kilometer away" and "1000 meters away". This would require the model to infer the units and perform the comparison, which would be a more challenging task. Furthermore, the authors should consider using non-linear models for surrogate analysis to capture more complex interactions between cues. While linear models are interpretable, they may not fully represent the underlying mechanisms of LMs. Techniques such as neural networks or kernel methods could be used to model the relationships between the input features and the model's output. This would provide a more accurate representation of the model's internal workings and potentially uncover more nuanced patterns in the data. 

To address the limitations of the current study, the authors should provide a more detailed discussion of the potential avenues for future research. This could include exploring the model's performance on more complex units and quantities, investigating the model's ability to handle implicit units, and using non-linear models for surrogate analysis. The authors could also consider investigating the model's performance on tasks that require more complex reasoning, such as comparing quantities that involve multiple steps or require the use of arithmetic operations. This would provide a more comprehensive understanding of the model's capabilities and limitations and would help to guide future research in this area. Additionally, the authors should consider exploring the model's performance on different types of language models, such as transformer-based models or recurrent neural networks. This would provide a more comprehensive understanding of the model's capabilities and limitations and would help to identify the factors that contribute to its performance.

Finally, the authors should consider exploring the model's performance on tasks that require more complex reasoning, such as comparing quantities that involve multiple steps or require the use of arithmetic operations. This would provide a more comprehensive understanding of the model's capabilities and limitations and would help to guide future research in this area. For example, the model could be tested on tasks that require it to compare quantities that involve multiple units or quantities that require the use of arithmetic operations to determine the correct answer. This would provide a more challenging task and would help to identify the limitations of the model's unit handling capabilities. The authors should also consider exploring the model's performance on tasks that require it to handle implicit units, such as comparing "a kilometer away" and "1000 meters away". This would require the model to infer the units and perform the comparison, which would be a more challenging task.

### Questions

- How does the model handle comparisons involving more complex units or quantities, such as those with prefixes (e.g., kilometer vs. meter) or non-standard units?
- Could the authors elaborate on the choice of linear models for surrogate analysis? Are there any specific reasons for not using non-linear models?
- How does the model perform when units are not explicitly stated but are implied by the context?

### Rating

6

### Confidence

4

**********

## Reviewer 2

### Summary

This paper investigates how language models (LMs) compare quantities with measurement units, such as 110 cm and 1.2 m. The authors find that LMs struggle near the comparison boundary, where small changes in value determine the correct answer. Through surrogate analysis, they show that LMs rely on numerical and unit-scale cues rather than exact shared-scale conversions. Causal interventions confirm that these cues influence LM decisions. The study provides a controlled case study of how LMs combine numerical and symbolic measurement units, highlighting limitations in their unit handling.

### Soundness

3

### Presentation

3

### Contribution

3

### Strengths

- The paper addresses a novel and important problem in the field of language models, specifically focusing on how they compare quantities with measurement units. This is a critical area of research as it impacts the reliability and accuracy of LMs in real-world applications.
- The authors conduct a thorough analysis, employing surrogate models and causal interventions to understand the internal mechanisms of LMs. This multi-faceted approach strengthens the validity of their findings.
- The paper is well-structured and clearly written, making it accessible to both experts and non-experts in the field. The use of figures and tables effectively communicates the key results and insights.

### Weaknesses

#### Some Related Works


#### comment

 - The study focuses on controlled, single-step comparisons, which may not fully capture the complexities of real-world scenarios involving multiple units or more intricate calculations. This limitation could affect the generalizability of the findings.
- The reliance on linear models for surrogate analysis might oversimplify the underlying mechanisms of LMs, potentially missing more complex interactions between cues. The use of ridge regression, while interpretable, may not fully capture the non-linear relationships that could be present in the LM's internal representations.
- The paper could benefit from a more detailed discussion of the limitations of the proposed approach and potential avenues for future research. For example, the current study does not explore how the model handles comparisons involving more complex units or quantities, such as those involving prefixes (e.g., kilometer vs. meter) or non-standard units. Furthermore, the study does not investigate the model's performance when the units are not explicitly stated but are implied by the context.

### Suggestions

The authors should consider expanding their analysis to include more complex scenarios, such as comparisons involving multiple units or quantities with prefixes. This would provide a more comprehensive understanding of the model's capabilities and limitations. For instance, the study could investigate how the model compares 1.5 km and 1500 m, or 2.5 kg and 2500 g. Additionally, the authors should explore the model's performance when units are not explicitly stated but are implied by the context, such as comparing "a kilometer away" and "1000 meters away". This would require the model to infer the units and perform the comparison, which would be a more challenging task. Furthermore, the authors should consider using non-linear models for surrogate analysis to capture more complex interactions between cues. While linear models are interpretable, they may not fully represent the underlying mechanisms of LMs. Techniques such as neural networks or kernel methods could be used to model the relationships between the input features and the model's output. This would provide a more accurate representation of the model's internal workings and potentially uncover more nuanced patterns in the data.

To address the limitations of the current study, the authors should provide a more detailed discussion of the potential avenues for future research. This could include exploring the model's performance on more complex units and quantities, investigating the model's ability to handle implicit units, and using non-linear models for surrogate analysis. The authors could also consider investigating the model's performance on tasks that require more complex reasoning, such as comparing quantities that involve multiple steps or require the use of arithmetic operations. This would provide a more comprehensive understanding of the model's capabilities and limitations and would help to guide future research in this area. Additionally, the authors should consider exploring the model's performance on different types of language models, such as transformer-based models or recurrent neural networks. This would provide a more comprehensive understanding of the model's capabilities and limitations and would help to identify the factors that contribute to its performance.

Finally, the authors should consider a more in-depth analysis of the types of errors made by the language models. For example, are the errors primarily due to incorrect unit conversions, or are they due to a lack of understanding of the numerical values? A more detailed error analysis could provide valuable insights into the limitations of the language models and could help to guide the development of more robust and reliable models. The authors could also explore the use of techniques such as attention visualization to understand which parts of the input the model is focusing on when making its comparisons. This could help to identify potential biases or limitations in the model's reasoning process.

### Questions

- How does the model handle comparisons involving more complex units or quantities, such as those with prefixes (e.g., kilometer vs. meter) or non-standard units?
- Could the authors elaborate on the choice of linear models for surrogate analysis? Are there any specific reasons for not using non-linear models?
- How does the model perform when units are not explicitly stated but are implied by the context?

### Rating

6

### Confidence

3

**********

## Reviewer 3

### Summary

This paper studies how language models (LMs) compare quantities with measurement units. The authors find that LMs struggle near the comparison boundary, where small changes in value determine the correct answer. They use surrogate analysis and causal interventions to show that LMs rely on numerical and unit-scale cues rather than exact shared-scale conversions. The study provides a controlled case study of how LMs combine numerical and symbolic measurement units, highlighting limitations in their unit handling.

### Soundness

3

### Presentation

3

### Contribution

2

### Strengths

1. This paper is well-written and easy to follow.
2. The authors conduct extensive experiments to analyze how language models compare quantities with measurement units. They use surrogate models and causal interventions to understand the internal mechanisms of LMs.
3. The authors provide a detailed analysis of the limitations of language models in handling measurement units and suggest potential avenues for future research.

### Weaknesses

#### Some Related Works


#### comment

1. The study focuses on controlled, single-step comparisons, which may not fully capture the complexities of real-world scenarios involving multiple units or more intricate calculations. This limitation could affect the generalizability of the findings.
2. The reliance on linear models for surrogate analysis might oversimplify the underlying mechanisms of LMs, potentially missing more complex interactions between cues. The use of ridge regression, while interpretable, may not fully capture the non-linear relationships that could be present in the LM's internal representations.
3. The paper could benefit from a more detailed discussion of the limitations of the proposed approach and potential avenues for future research. For example, the current study does not explore how the model handles comparisons involving more complex units or quantities, such as those involving prefixes (e.g., kilometer vs. meter) or non-standard units. Furthermore, the study does not investigate the model's performance when the units are not explicitly stated but are implied by the context.

### Suggestions

The authors should consider expanding their analysis to include more complex scenarios, such as comparisons involving multiple units or quantities with prefixes. This would provide a more comprehensive understanding of the model's capabilities and limitations. For instance, the study could investigate how the model compares 1.5 km and 1500 m, or 2.5 kg and 2500 g. Additionally, the authors should explore the model's performance when units are not explicitly stated but are implied by the context, such as comparing "a kilometer away" and "1000 meters away". This would require the model to infer the units and perform the comparison, which would be a more challenging task. Furthermore, the authors should consider using non-linear models for surrogate analysis to capture more complex interactions between cues. While linear models are interpretable, they may not fully represent the underlying mechanisms of LMs. Techniques such as neural networks or kernel methods could be used to model the relationships between the input features and the model's output. This would provide a more accurate representation of the model's internal workings and potentially uncover more nuanced patterns in the data.

To address the limitations of the current study, the authors should provide a more detailed discussion of the potential avenues for future research. This could include exploring the model's performance on more complex units and quantities, investigating the model's ability to handle implicit units, and using non-linear models for surrogate analysis. The authors could also consider investigating the model's performance on tasks that require more complex reasoning, such as comparing quantities that involve multiple steps or require the use of arithmetic operations. This would provide a more comprehensive understanding of the model's capabilities and limitations and would help to guide future research in this area. Additionally, the authors should consider exploring the model's performance on different types of language models, such as transformer-based models or recurrent neural networks. This would provide a more comprehensive understanding of the model's capabilities and limitations and would help to identify the factors that contribute to its performance.

Finally, the authors should consider a more in-depth analysis of the types of errors made by the language models. For example, are the errors primarily due to incorrect unit conversions, or are they due to a lack of understanding of the numerical values? A more detailed error analysis could provide valuable insights into the limitations of the language models and could help to guide the development of more robust and reliable models. The authors could also explore the use of techniques such as attention visualization to understand which parts of the input the model is focusing on when making its comparisons. This could help to identify potential biases or limitations in the model's reasoning process.

### Questions

1. How does the model handle comparisons involving more complex units or quantities, such as those with prefixes (e.g., kilometer vs. meter) or non-standard units?
2. Could the authors elaborate on the choice of linear models for surrogate analysis? Are there any specific reasons for not using non-linear models?
3. How does the model perform when units are not explicitly stated but are implied by the context?

### Rating

6

### Confidence

3

**********

## Reviewer 4

### Summary

This paper investigates how language models (LMs) compare quantities with measurement units, such as 110 cm and 1.2 m. The authors find that LMs struggle near the comparison boundary, where small changes in value determine the correct answer. Through surrogate analysis, they show that LMs rely on numerical and unit-scale cues rather than exact shared-scale conversions. Causal interventions confirm that these cues influence LM decisions. The study provides a controlled case study of how LMs combine numerical and symbolic measurement units, highlighting limitations in their unit handling.

### Soundness

3

### Presentation

3

### Contribution

3

### Strengths

1. The paper addresses a novel and important problem in the field of language models, specifically focusing on how they compare quantities with measurement units. This is a critical area of research as it impacts the reliability and accuracy of LMs in real-world applications.
2. The authors conduct a thorough analysis, employing surrogate models and causal interventions to understand the internal mechanisms of LMs. This multi-faceted approach strengthens the validity of their findings.
3. The paper is well-structured and clearly written, making it accessible to both experts and non-experts in the field. The use of figures and tables effectively communicates the key results and insights.

### Weaknesses

#### Some Related Works


#### comment

1. The study focuses on controlled, single-step comparisons, which may not fully capture the complexities of real-world scenarios involving multiple units or more intricate calculations. This limitation could affect the generalizability of the findings.
2. The reliance on linear models for surrogate analysis might oversimplify the underlying mechanisms of LMs, potentially missing more complex interactions between cues. The use of ridge regression, while interpretable, may not fully capture the non-linear relationships that could be present in the LM's internal representations.
3. The paper could benefit from a more detailed discussion of the limitations of the proposed approach and potential avenues for future research. For example, the current study does not explore how the model handles comparisons involving more complex units or quantities, such as those involving prefixes (e.g., kilometer vs. meter) or non-standard units. Furthermore, the study does not investigate the model's performance when the units are not explicitly stated but are implied by the context.

### Suggestions

The authors should consider expanding their analysis to include more complex scenarios, such as comparisons involving multiple units or quantities with prefixes. This would provide a more comprehensive understanding of the model's capabilities and limitations. For instance, the study could investigate how the model compares 1.5 km and 1500 m, or 2.5 kg and 2500 g. Additionally, the authors should explore the model's performance when units are not explicitly stated but are implied by the context, such as comparing "a kilometer away" and "1000 meters away". This would require the model to infer the units and perform the comparison, which would be a more challenging task. Furthermore, the authors should consider using non-linear models for surrogate analysis to capture more complex interactions between cues. While linear models are interpretable, they may not fully represent the underlying mechanisms of LMs. Techniques such as neural networks or kernel methods could be used to model the relationships between the input features and the model's output. This would provide a more accurate representation of the model's internal workings and potentially uncover more nuanced patterns in the data.

To address the limitations of the current study, the authors should provide a more detailed discussion of the potential avenues for future research. This could include exploring the model's performance on more complex units and quantities, investigating the model's ability to handle implicit units, and using non-linear models for surrogate analysis. The authors could also consider investigating the model's performance on tasks that require more complex reasoning, such as comparing quantities that involve multiple steps or require the use of arithmetic operations. This would provide a more comprehensive understanding of the model's capabilities and limitations and would help to guide future research in this area. Additionally, the authors should consider exploring the model's performance on different types of language models, such as transformer-based models or recurrent neural networks. This would provide a more comprehensive understanding of the model's capabilities and limitations and would help to identify the factors that contribute to its performance.

Finally, the authors should consider a more in-depth analysis of the types of errors made by the language models. For example, are the errors primarily due to incorrect unit conversions, or are they due to a lack of understanding of the numerical values? A more detailed error analysis could provide valuable insights into the limitations of the language models and could help to guide the development of more robust and reliable models. The authors could also explore the use of techniques such as attention visualization to understand which parts of the input the model is focusing on when making its comparisons. This could help to identify potential biases or limitations in the model's reasoning process.

### Questions

1. How does the model handle comparisons involving more complex units or quantities, such as those with prefixes (e.g., kilometer vs. meter) or non-standard units?
2. Could the authors elaborate on the choice of linear models for surrogate analysis? Are there any specific reasons for not using non-linear models?
3. How does the model perform when units are not explicitly stated but are implied by the context?

### Rating

8

### Confidence

3

**********

}

I have finished generating simulated reviews from 4 reviewers. Next, I will generate verification content for these reviews:

\boxed_verification{
The user wants me to validate weaknesses identified by reviewers for the provided paper. I need to go through each reviewer's comments and find evidence within the paper to support their claims.

**Plan:**
1. Go through each reviewer's comments one by one.
2. For each weakness identified by the reviewer, locate the relevant section in the paper.
3. Extract evidence (quotes, experimental setup details, missing citations, etc.) to support the reviewer's claim.
4. If the weakness is valid, summarize the evidence. If not, explain why the reviewer's claim is incorrect based on the paper's content.
5. Pay attention to conflicting opinions between reviewers.
**Review 1 Weaknesses:**

1. Weakness Statement:
"The study focuses on controlled, single-step comparisons, which may not fully capture the complexities of real-world scenarios involving multiple units or more intricate calculations. This limitation could affect the generalizability of the findings."

2. Evidence Collection:
b) Experiment-related Evidence:
   - The paper explicitly states the focus on "controlled setting" in the "Task Formulation" section: "For each comparison q1 = r1 u1 and q2 = r2 u2, the correct answer can be determined by the log-scale difference between the two quantities after accounting for unit scale: Q​ M​ ( q1 , q2 ) \displaystyle QM(q_1, q_2) = log ⁡ ( r 1 ) − log ⁡ ( r 2 ) + log ⁡ ( s D ( u 1 ) ) − log ⁡ ( s D ( u 2 ) )."
   - The "Overall Experimental Setup" section mentions the use of "five unit settings, each defined by a physical dimension D and a set of mutually comparable measurement units U D U_{D} UD, as shown in Table 1." This indicates a focus on pairwise comparisons.
   - The "Behavioral Observation: LMs Become Less Accurate Near the Boundary" experiment uses "5,000 comparison examples per unit setting" for each of the five unit settings. This confirms the controlled, single-step nature of the comparisons.

3. Literature Gap Analysis:
   - The paper does not explicitly discuss the limitations of focusing on single-step comparisons or how the findings might generalize to more complex scenarios.

4. Validation Analysis:
   - The paper's methodology is clearly designed for controlled, single-step comparisons. The reviewer's point about the limitations of this approach for real-world scenarios is a valid observation based on the defined experimental setup.

5. Conclusion:
   - Validity status: Valid
   - Confidence level: High
   - Key supporting evidence: The paper's description of the task formulation and experimental setup confirms the focus on controlled, single-step comparisons.

1. Weakness Statement:
"The reliance on linear models for surrogate analysis might oversimplify the underlying mechanisms of LMs, potentially missing more complex interactions between cues. The use of ridge regression, while interpretable, may not fully capture the non-linear relationships that could be present in the LM's internal representations."

2. Evidence Collection:
a) Method-related Evidence:
   - The "Surrogate Analysis: Number and Unit Differences Best Predict LM Behavior" section states: "We use surrogate models to test which candidate quantities and cues explain the LM’s comparison behavior. For each comparison example, we instantiate a prompt Prompt ⁡ ( q 1 , q 2 ) \mathrm{Prompt}(q_{1},q_{2}) Prompt(q1,q2) , such as “Which is larger, ? The answer is”. We then compare the LM’s average log-probability of generating the two candidate answer strings, namely the left quantity a q 1 a_{q_1} aq1​ and the right quantity a q 2 a_{q_2} aq2​ , as continuations of this prompt: m LM ​ ( q 1 , q 2 ) \displaystyle m_{\mathrm{LM}}(q_1, q_2) mLM(q1,q2) = ℓ ¯ θ ​ ( a q 1 ∣ Prompt ⁡ ( q 1 , q 2 ) ) \displaystyle=\bar{\ell}_{\theta}(a_{q_{1}}\mid\mathrm{Prompt}(q_{1},q_{2})) mLM​(aq1​∣Prompt(q1​,q2​)) (10) To evaluate each surrogate model with two metrics, Δ ​ R 2 \Delta R^{2} \DeltaR2 and R partial 2 R^{2}_{\mathrm{partial}} Rpartial2​ ."
   - The paper then describes the candidate variables for the surrogate models, including "NumLogDiff = log r1 − log r2" and "UnitLogDiff = log sD(u1) − log sD(u2)". These are linear transformations of the input features.
   - The paper mentions using "ridge regression surrogate model to predict m LM ​ ( q 1 , q 2 ) m_{\mathrm{LM}}(q_1, q_2) mLM(q1,q2)". Ridge regression is a linear model.

3. Literature Gap Analysis:
   - The paper does not explicitly justify the choice of linear models over non-linear models or discuss the potential limitations of this choice.

4. Validation Analysis:
   - The reviewer correctly points out that the surrogate models used are based on linear transformations of the input features and employ ridge regression, a linear model. This could potentially oversimplify the complex internal workings of the LMs.

5. Conclusion:
   - Validity status: Valid
   - Confidence level: High
   - Key supporting evidence: The description of the surrogate models and the use of ridge regression confirm the reliance on linear models.

1. Weakness Statement:
"The paper could benefit from a more detailed discussion of the limitations of the proposed approach and potential avenues for future research. For example, the current study does not explore how the model handles comparisons involving more complex units or quantities, such as those involving prefixes (e.g., kilometer vs. meter) or non-standard units. Furthermore, the study does not investigate the model's performance when the units are not explicitly stated but are implied by the context."

2. Evidence Collection:
- The "Limitations" section of the paper explicitly acknowledges some limitations: "First, our study focuses on controlled, single-step comparisons between two quantities with measurement units. This design allows us to analyze LM behavior in a controlled setting, but it does not cover more realistic multi-step quantitative reasoning, where unit conversion may be combined with retrieval, arithmetic, or reasoning over longer textual contexts. Extending the analysis to such settings is an important direction for future work."
- The paper's "Task Formulation" section defines the measurement units as "numerical value r ∈ [ r min , r max ] 10 − 3 ≤ r < 10 4 10^{-3}\leq r<10^{4} 10−3≤r<104  and unit u ∈ U D U_{D} U D , a chosen set of mutually comparable measurement units for that dimension. A quantity with a measurement unit is specified by a numerical value r ∈ [ r min , r max ] ⊂ ℝ > 0 r\in[r_{\min},r_{\max}]\subset\mathbb{R}_{>0} r∈[rmin​,rmax​]⊂R>0> 0  and a unit u ∈ U D u\in U_{D} u∈UD, and is written as r ​ u ru ru ."
- The paper does not explicitly discuss the handling of units with prefixes or non-standard units.

3. Literature Gap Analysis:
   - While the paper mentions the limitations of the controlled setting, it doesn't delve into the specific challenges of handling complex units or implicit units in future work.

4. Validation Analysis:
   - The reviewer's point about the lack of exploration of more complex units and implicit units is valid. The paper's focus is on a controlled setting with specific, defined units.

5. Conclusion:
   - Validity status: Valid
   - Confidence level: High
   - Key supporting evidence: The "Limitations" section and the definition of measurement units in the "Task Formulation" section support the reviewer's claim.

**Review 2 Weaknesses:**

1. Weakness Statement:
"The study focuses on controlled, single-step comparisons, which may not fully capture the complexities of real-world scenarios involving multiple units or more intricate calculations. This limitation could affect the generalizability of the findings."

2. Evidence Collection:
   - This is the same weakness as Reviewer 1's first point. Please see the analysis for Reviewer 1's first weakness.

3. Literature Gap Analysis:
   - Same as Reviewer 1's first point.

4. Validation Analysis:
   - Same as Reviewer 1's first point.

5. Conclusion:
   - Validity status: Valid
   - Confidence level: High
   - Key supporting evidence: Same as Reviewer 1's first point.

1. Weakness Statement:
"The reliance on linear models for surrogate analysis might oversimplify the underlying mechanisms of LMs, potentially missing more complex interactions between cues. The use of ridge regression, while interpretable, may not fully capture the non-linear relationships that could be present in the LM's internal representations."

2. Evidence Collection:
   - This is the same weakness as Reviewer 1's second point. Please see the analysis for Reviewer 1's second weakness.

3. Literature Gap Analysis:
   - Same as Reviewer 1's second point.

4. Validation Analysis:
   - Same as Reviewer 1's second point.

5. Conclusion:
   - Validity status: Valid
   - Confidence level: High
   - Key supporting evidence: Same as Reviewer 1's second point.

1. Weakness Statement:
"The paper could benefit from a more detailed discussion of the limitations of the proposed approach and potential avenues for future research. For example, the current study does not explore how the model handles comparisons involving more complex units or quantities, such as those with prefixes (e.g., kilometer vs. meter) or non-standard units. Furthermore, the study does not investigate the model's performance when units are not explicitly stated but are implied by the context."

2. Evidence Collection:
   - This is the same weakness as Reviewer 1's third point. Please see the analysis for Reviewer 1's third point.

3. Literature Gap Analysis:
   - Same as Reviewer 1's third point.

4. Validation Analysis:
   - Same as Reviewer 1's third point.

5. Conclusion:
   - Validity status: Valid
   - Confidence level: High
   - Key supporting evidence: Same as Reviewer 1's third point.

**Review 3 Weaknesses:**

1. Weakness Statement:
"The study focuses on controlled, single-step comparisons, which may not fully capture the complexities of real-world scenarios involving multiple units or more intricate calculations. This limitation could affect the generalizability of the findings."

2. Evidence Collection:
   - This is the same weakness as Reviewer 1's first point and Reviewer 2's first point. Please see the analysis for Reviewer 1's first point.

3. Literature Gap Analysis:
   - Same as Reviewer 1's first point.

4. Validation Analysis:
   - Same as Reviewer 1's first point.

5. Conclusion:
   - Validity status: Valid
   - Confidence level: High
   - Key supporting evidence: Same as Reviewer 1's first point.

1. Weakness Statement:
"The reliance on linear models for surrogate analysis might oversimplify the underlying mechanisms of LMs, potentially missing more complex interactions between cues. The use of ridge regression, while interpretable, may not fully capture the non-linear relationships that could be present in the LM's internal representations."

2. Evidence Collection:
   - This is the same weakness as Reviewer 1's second point and Reviewer 2's second point. Please see the analysis for Reviewer 1's second point.

3. Literature Gap Analysis:
   - Same as Reviewer 1's second point.

4. Validation Analysis:
   - Same as Reviewer 1's second point.

5. Conclusion:
   - Validity status: Valid
   - Confidence level: High
   - Key supporting evidence: Same as Reviewer 1's second point.

1. Weakness Statement:
"The paper could benefit from a more detailed discussion of the limitations of the proposed approach and potential avenues for future research. For example, the current study does not explore how the model handles comparisons involving more complex units or quantities, such as those with prefixes (e.g., kilometer vs. meter) or non-standard units. Furthermore, the study does not investigate the model's performance when units are not explicitly stated but are implied by the context."

2. Evidence Collection:
   - This is the same weakness as Reviewer 1's third point and Reviewer 2's third point. Please see the analysis for Reviewer 1's third point.

3. Literature Gap Analysis:
   - Same as Reviewer 1's third point.

4. Validation Analysis:
   - Same as Reviewer 1's third point.

5. Conclusion:
   - Validity status: Valid
   - Confidence level: High
   - Key supporting evidence: Same as Reviewer 1's third point.

**Review 4 Weaknesses:**

1. Weakness Statement:
"The study focuses on controlled, single-step comparisons, which may not fully capture the complexities of real-world scenarios involving multiple units or more intricate calculations. This limitation could affect the generalizability of the findings."

2. Evidence Collection:
   - This is the same weakness as Reviewer 1's first point, Reviewer 2's first point, and Reviewer 3's first point. Please see the analysis for Reviewer 1's first point.

3. Literature Gap Analysis:
   - Same as Reviewer 1's first point.

4. Validation Analysis:
   - Same as Reviewer 1's first point.

5. Conclusion:
   - Validity status: Valid
   - Confidence level: High
   - Key supporting evidence: Same as Reviewer 1's first point.

1. Weakness Statement:
"The reliance on linear models for surrogate analysis might oversimplify the underlying mechanisms of LMs, potentially missing more complex interactions between cues. The use of ridge regression, while interpretable, may not fully capture the non-linear relationships that could be present in the LM's internal representations."

2. Evidence Collection:
   - This is the same weakness as Reviewer 1's second point, Reviewer 2's second point, and Reviewer 3's second point. Please see the analysis for Reviewer 1's second point.

3. Literature Gap Analysis:
   - Same as Reviewer 1's second point.

4. Validation Analysis:
   - Same as Reviewer 1's second point.

5. Conclusion:
   - Validity status: Valid
   - Confidence level: High
   - Key supporting evidence: Same as Reviewer 1's second point.

1. Weakness Statement:
"The paper could benefit from a more detailed discussion of the limitations of the proposed approach and potential avenues for future research. For example, the current study does not explore how the model handles comparisons involving more complex units or quantities, such as those with prefixes (e.g., kilometer vs. meter) or non-standard units. Furthermore, the study does not investigate the model's performance when units are not explicitly stated but are implied by the context."

2. Evidence Collection:
   - This is the same weakness as Reviewer 1's third point, Reviewer 2's third point, and Reviewer 3's third point. Please see the analysis for Reviewer 1's third point.

3. Literature Gap Analysis:
   - Same as Reviewer 1's third point.

4. Validation Analysis:
   - Same as Reviewer 1's third point.

5. Conclusion:
   - Validity status: Valid
   - Confidence level: High
   - Key supporting evidence: Same as Reviewer 1's third point.

**Synthesis and Reflection:**

All reviewers have identified similar weaknesses in the paper, primarily concerning the limitations of the controlled, single-step comparison setting and the use of linear models for surrogate analysis. There is a strong consensus among the reviewers regarding these points.

*   **Controlled, Single-Step Comparisons (High Confidence):**  All reviewers explicitly mention this limitation. The paper's methodology, as described in the "Task Formulation" and "Overall Experimental Setup" sections, confirms the focus on pairwise comparisons with explicit unit information. This design choice, while allowing for controlled analysis, inherently limits the generalizability of the findings to more complex, real-world scenarios.
*   **Linear Models for Surrogate Analysis (High Confidence):** Reviewers 1, 2, and 3 all point out the reliance on linear models, specifically ridge regression, for surrogate analysis. The "Surrogate Analysis" section clearly states the use of linear transformations of input features and ridge regression. This choice, while interpretable, might oversimplify the complex, potentially non-linear, interactions within the LMs.
*   **Limited Discussion of Complex Units (High Confidence):** Reviewers 1, 2, and 3 also note the lack of exploration into how the model handles more complex units, such as those with prefixes or non-standard units. The "Task Formulation" section defines the units used in the study, which do not include such complexities. The "Limitations" section acknowledges the focus on controlled settings but doesn't delve into the specific challenges of handling complex units in future work.

There are no significant contradictions between the reviewers' opinions. They are consistently pointing out the same limitations and suggesting similar areas for improvement.

**Conclusion:**

The identified weaknesses are valid and well-supported by the paper's content. The reviewers have accurately pinpointed the limitations of the controlled experimental setup and the use of linear models for surrogate analysis. The paper could be strengthened by acknowledging these limitations more explicitly and suggesting future research directions that address these shortcomings.
}

Now, I have successfully verified each review. Next, I will organize this content and output the final review decision:

\boxed_review{
## Summary:

This paper presents a compelling investigation into how language models (LMs) compare quantities that are associated with measurement units, a task that is fundamental to real-world applications. The authors introduce a novel framework for analyzing this problem, focusing on the interplay between numerical and symbolic measurement unit information. They begin by defining a quantity as a combination of a numerical value and a unit, and then they establish a comparison metric based on the log-scale difference between the quantities, which accounts for both numerical and unit scales. This metric, denoted as QM, forms the basis for their behavioral experiments. The core of the study involves comparing the LMs' performance against this QM metric, using a controlled experimental setup where LMs are presented with pairs of quantities and asked to select the larger one. The authors find that LMs exhibit a bias towards numerical comparisons, struggling near the comparison boundary where small changes in value determine the correct answer. To understand the internal mechanisms driving these biases, they employ surrogate models, which are designed to predict the LM's behavior based on various candidate variables. These variables include numerical and unit differences, as well as other potential cues. The results of the surrogate analysis reveal that numerical and unit-scale differences are the most predictive variables for the LM's decisions, suggesting that the models rely on these cues rather than performing exact shared-scale conversions. Furthermore, the authors conduct causal interventions to demonstrate that these numerical and unit-scale cues directly influence the LM's judgments. These interventions involve manipulating the input quantities and observing the resulting changes in the LM's output. The findings reveal that the numerical and unit-scale differences are indeed the primary factors that drive the LM's behavior. Overall, this paper provides a valuable contribution to our understanding of how LMs process and compare quantities with measurement units. The controlled experimental setup, combined with the use of surrogate models and causal interventions, offers a rigorous approach to analyzing this complex task. The results highlight the limitations of current LMs in handling measurement units and provide insights into the underlying mechanisms that govern their behavior. The study's focus on the interplay between numerical and symbolic information is particularly noteworthy, as it sheds light on the ways in which LMs integrate different types of input. The authors' findings have implications for the development of more robust and reliable LMs, particularly in applications that require accurate comparisons of quantities with units. The paper's emphasis on the importance of understanding the internal workings of LMs makes it a significant contribution to the field.


## Soundness:

3.0


## Presentation:

3.0


## Contribution:

2.75


## Strengths:

This paper demonstrates several notable strengths, making it a valuable contribution to the field of language model research. First, the paper addresses a novel and important problem: how language models compare quantities with measurement units. This is a critical area of research, as it impacts the reliability and accuracy of LMs in real-world applications. The ability to accurately compare quantities is essential for tasks such as measurement, calculation, and decision-making. The authors' focus on this specific problem is a significant strength, as it targets a gap in our current understanding of LMs. Second, the paper's methodology is rigorous and well-structured. The authors employ a controlled experimental setup, which allows them to isolate the factors that influence the LMs' behavior. This is crucial for conducting a systematic analysis of the problem. The use of surrogate models is another strength, as it provides a way to understand the internal mechanisms of LMs. By training these models to predict the LM's behavior, the authors are able to identify the key variables that drive the LMs' decisions. The causal interventions further enhance the analysis by demonstrating that the identified cues directly influence the LM's judgments. This combination of behavioral experiments, surrogate models, and causal interventions provides a comprehensive approach to understanding the problem. Third, the paper is well-written and easy to follow. The authors clearly explain their methodology, results, and implications. The use of figures and tables effectively communicates the key findings. The paper is accessible to both experts and non-experts in the field, which is a significant strength. The authors also provide a detailed description of their experimental setup, which allows for reproducibility. Fourth, the paper's findings are significant and have implications for the development of more robust and reliable LMs. The authors demonstrate that LMs struggle near the comparison boundary, where small changes in value determine the correct answer. This highlights a limitation of current LMs in handling measurement units. The surrogate analysis reveals that numerical and unit-scale differences are the most predictive variables for the LM's decisions. This finding suggests that LMs rely on these cues rather than performing exact shared-scale conversions. The causal interventions further confirm that these numerical and unit-scale cues directly influence the LM's judgments. These findings have important implications for the development of more accurate and reliable LMs, particularly in applications that require accurate comparisons of quantities with units. Finally, the paper's focus on the interplay between numerical and symbolic information is a significant contribution. The authors demonstrate how LMs combine these two types of information to make their comparisons. This is a crucial aspect of understanding how LMs process and reason about quantities. The paper's emphasis on the importance of understanding the internal workings of LMs makes it a significant contribution to the field.


## Weaknesses:

While this paper presents valuable insights into how language models compare quantities with measurement units, there are several weaknesses that warrant careful consideration. First, the study's focus on controlled, single-step comparisons limits the generalizability of the findings. As noted by multiple reviewers, the experimental setup is designed to isolate specific factors, but this design choice may not fully capture the complexities of real-world scenarios involving multiple units or more intricate calculations. The paper explicitly states that the task involves "controlled setting" and uses "five unit settings, each defined by a physical dimension D and a set of mutually comparable measurement units U D" (Section 3.1). This focus on pairwise comparisons, where each comparison involves two quantities with explicit units, does not account for the complexities of situations where multiple units or calculations are involved. This limitation is significant because real-world applications often involve more complex numerical reasoning, and the findings may not directly translate to these scenarios. The reliance on linear models for surrogate analysis is another significant limitation. The authors use ridge regression, a linear model, to predict the LM's behavior (Section 3.2). While linear models are interpretable, they may not fully capture the non-linear relationships that could be present in the LM's internal representations. As the paper states, "we use surrogate models to test which candidate quantities and cues explain the LM’s comparison behavior. For each comparison example, we instantiate a prompt Prompt(q1, q2) ... and then compare the LM’s average log-probability of generating the two candidate answer strings ... as continuations of this prompt" (Section 3.2). This approach, while useful for identifying the most predictive variables, may miss more complex interactions between cues. The use of ridge regression, while interpretable, may not fully capture the non-linear relationships that could be present in the LM's internal representations. This limitation is significant because it may lead to an incomplete understanding of the underlying mechanisms of the LMs. Furthermore, the paper does not provide a detailed discussion of the limitations of the proposed approach and potential avenues for future research. While the "Limitations" section acknowledges the focus on controlled settings, it does not delve into the specific challenges of handling complex units or implicit units in future work. The paper defines the measurement units as "numerical value r ∈ [r_min, r_max] ⊂ ℝ > 0" and "unit u ∈ U D" (Section 3.1), and the examples used in the experiments involve explicit units. The paper does not explore how the model handles comparisons involving more complex units, such as those with prefixes (e.g., kilometer vs. meter) or non-standard units. Additionally, the study does not investigate the model's performance when units are not explicitly stated but are implied by the context. This is a significant limitation because real-world scenarios often involve implicit units or units that are not explicitly stated. The lack of exploration of these aspects limits the generalizability of the findings and raises questions about the robustness of the models in real-world applications. Finally, the paper does not explore how the model handles comparisons involving more complex units or quantities, such as those involving prefixes (e.g., kilometer vs. meter) or non-standard units. The study also does not investigate the model's performance when units are not explicitly stated but are implied by the context. This is a significant limitation because real-world scenarios often involve implicit units or units that are not explicitly stated. The paper's focus on a controlled setting with specific, defined units limits the generalizability of the findings. The paper's methodology is clearly designed for controlled, single-step comparisons, and it does not address the complexities of real-world scenarios involving more complex units or implicit units. This limitation is significant because it raises questions about the robustness of the models in real-world applications.


## Suggestions:

To address the identified weaknesses, I recommend several concrete improvements. First, the authors should expand their analysis to include more complex scenarios, such as comparisons involving multiple units or quantities with prefixes. This would provide a more comprehensive understanding of the model's capabilities and limitations. For instance, the study could investigate how the model compares 1.5 km and 1500 m, or 2.5 kg and 2500 g. This would require the model to infer the units and perform the comparison, which would be a more challenging task. Furthermore, the authors should explore the model's performance when units are not explicitly stated but are implied by the context, such as comparing "a kilometer away" and "1000 meters away". This would require the model to infer the units and perform the comparison, which would be a more challenging task. This would also help to identify potential biases or limitations in the model's reasoning process. Second, the authors should consider using non-linear models for surrogate analysis to capture more complex interactions between cues. While linear models are interpretable, they may not fully represent the underlying mechanisms of LMs. Techniques such as neural networks or kernel methods could be used to model the relationships between the input features and the model's output. This would provide a more accurate representation of the model's internal workings and potentially uncover more nuanced patterns in the data. To address the limitations of the current study, the authors should provide a more detailed discussion of the potential avenues for future research. This could include exploring the model's performance on more complex units and quantities, investigating the model's ability to handle implicit units, and using non-linear models for surrogate analysis. The authors could also consider investigating the model's performance on tasks that require more complex reasoning, such as comparing quantities that involve multiple steps or require the use of arithmetic operations. This would provide a more comprehensive understanding of the model's capabilities and limitations and would help to guide future research in this area. Additionally, the authors should consider exploring the model's performance on different types of language models, such as transformer-based models or recurrent neural networks. This would provide a more comprehensive understanding of the model's capabilities and limitations and would help to identify the factors that contribute to its performance. The authors could also consider investigating the model's performance on tasks that require more complex reasoning, such as comparing quantities that involve multiple steps or require the use of arithmetic operations. This would provide a more comprehensive understanding of the model's capabilities and limitations and would help to guide future research in this area. Finally, the authors should consider a more in-depth analysis of the types of errors made by the language models. For example, are the errors primarily due to incorrect unit conversions, or are they due to a lack of understanding of the numerical values? A more detailed error analysis could provide valuable insights into the limitations of the language models and could help to guide the development of more robust and reliable models. The authors could also explore the use of techniques such as attention visualization to understand which parts of the input the model is focusing on when making its comparisons. This could help to identify potential biases or limitations in the model's reasoning process.


## Questions:

Several key questions arise from my analysis of this paper. First, how does the model handle comparisons involving more complex units or quantities, such as those with prefixes (e.g., kilometer vs. meter) or non-standard units? The paper's focus on controlled settings with specific, defined units leaves this question unanswered. Understanding how the model performs with more complex units is crucial for assessing its real-world applicability. Second, could the authors elaborate on the choice of linear models for surrogate analysis? Are there any specific reasons for not using non-linear models? The use of ridge regression, while interpretable, may not fully capture the non-linear relationships that could be present in the LM's internal representations. Exploring the use of non-linear models could provide a more accurate representation of the model's internal workings. Third, how does the model perform when units are not explicitly stated but are implied by the context? The paper's focus on explicit unit statements leaves this question unanswered. Real-world scenarios often involve implicit units, and understanding how the model handles these situations is crucial for assessing its robustness. Fourth, how does the model's performance vary when units are presented in different ways, such as using prefixes (e.g., kilometer vs. meter) or when the units are not explicitly stated but are implied by the context? This question is related to the previous question about complex units and implicit units. Understanding how the model's performance varies under different conditions is crucial for assessing its robustness. Fifth, how does the model's performance change when units are not explicitly stated but are implied by the context? This question is related to the previous question about implicit units. Understanding how the model's performance changes under different conditions is crucial for assessing its robustness. Finally, how does the model's performance compare when using more complex units or quantities, such as those with prefixes or non-standard units? This question is related to the first question about complex units. Understanding how the model's performance compares under different conditions is crucial for assessing its robustness.


## Rating:

6.5


## Confidence:

3.25


## Decision:

Accept
}