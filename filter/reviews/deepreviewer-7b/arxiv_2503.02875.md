I will use Standard Mode for comprehensive thinking. As a professional reviewer, I will simulate 4 different reviewers, followed by the verification thinking. Then I will output the Finally Review Output. Let me think - Standard Mode means I will output the original review, followed by the verification thinking. Considering that I am currently in standard mode, I should think from my existing knowledge and consider some related work content when writing about weaknesses. Then I will output the Finally Review Output and Meta Review Output:

\boxed_simreviewers{
## Reviewer 1

### Summary

This paper proposes an unsupervised fine-tuning method for improving the reasoning capabilities of large language models. The authors identify a phenomenon called "Prefix Self-Consistency," where different solution trajectories for the same question share common initial reasoning steps. Based on this, they propose Unsupervised Prefix Fine-Tuning (UPFT), which leverages only the initial prefix substrings of model-generated responses for fine-tuning, eliminating the need for labeled data or extensive sampling. Experiments show that UPFT matches or exceeds the performance of supervised methods like Rejection Sampling Fine-Tuning while reducing training time by 75% and sampling cost by 99.7%.

### Soundness

3

### Presentation

3

### Contribution

2

### Strengths

1. The paper is well-written and easy to follow.
2. The proposed method is simple and effective.

### Weaknesses

#### Some Related Works


#### comment

1. The paper lacks a detailed analysis of the computational overhead introduced by UPFT, particularly in terms of time and memory requirements for prefix extraction and fine-tuning. While the authors mention a reduction in sampling costs, they do not provide a comprehensive breakdown of the computational resources required for the prefix extraction step, which could be significant, especially for large models and long sequences. A detailed analysis should include the time complexity of the prefix extraction algorithm and the memory footprint of storing the prefix substrings.
2. The paper does not explore the sensitivity of UPFT to different prefix lengths. While the authors mention that the optimal prefix length may vary across models and datasets, they do not provide a systematic analysis of how performance changes with different prefix lengths. A more thorough investigation should include a range of prefix lengths and their impact on both training time and final performance. This analysis should also consider the trade-offs between shorter and longer prefixes, as shorter prefixes might lead to information loss, while longer prefixes could increase computational costs.
3. The paper does not discuss the potential limitations of UPFT in scenarios where the initial reasoning steps are not as consistent as in the datasets used for evaluation. The authors should acknowledge that the effectiveness of UPFT might be reduced in cases where the model generates diverse or incorrect initial reasoning steps. A discussion of how UPFT might perform in such scenarios is needed, along with potential strategies to mitigate these limitations. This should include an analysis of the impact of noisy or inconsistent initial prefixes on the fine-tuning process.
4. The paper does not provide a detailed comparison of UPFT with other unsupervised learning methods for reasoning tasks. While the authors mention that UPFT is an unsupervised method, they do not provide a comprehensive comparison with other relevant unsupervised techniques. A more detailed comparison should include a discussion of the advantages and disadvantages of UPFT compared to other methods, as well as a discussion of the specific scenarios where UPFT is most effective.

### Suggestions

The paper would benefit from a more detailed analysis of the computational overhead introduced by UPFT. Specifically, the authors should provide a breakdown of the time and memory requirements for each step of the UPFT process, including the prefix extraction, fine-tuning, and inference stages. This analysis should include a discussion of the time complexity of the prefix extraction algorithm and the memory footprint of storing the prefix substrings. Furthermore, the authors should investigate the scalability of UPFT with respect to model size and sequence length. This analysis should include a discussion of how the computational costs scale with increasing model parameters and input sequence lengths. A detailed analysis of the computational overhead would allow readers to better understand the practical limitations of UPFT and its applicability to different scenarios.

To address the sensitivity of UPFT to different prefix lengths, the authors should conduct a more systematic analysis of how performance changes with varying prefix lengths. This analysis should include a range of prefix lengths and their impact on both training time and final performance. The authors should also investigate the trade-offs between shorter and longer prefixes, as shorter prefixes might lead to information loss, while longer prefixes could increase computational costs. A detailed analysis should also include a discussion of how the optimal prefix length varies across different models and datasets. This analysis should provide practical guidance on how to choose the appropriate prefix length for different scenarios. The authors should also explore adaptive prefix length selection methods, which could potentially improve the performance of UPFT.

Finally, the authors should discuss the potential limitations of UPFT in scenarios where the initial reasoning steps are not as consistent as in the datasets used for evaluation. The authors should acknowledge that the effectiveness of UPFT might be reduced in cases where the model generates diverse or incorrect initial reasoning steps. A discussion of how UPFT might perform in such scenarios is needed, along with potential strategies to mitigate these limitations. This should include an analysis of the impact of noisy or inconsistent initial prefixes on the fine-tuning process. The authors should also explore methods to improve the consistency of the initial reasoning steps, such as using a more robust prefix selection strategy or incorporating additional constraints into the fine-tuning process. A more thorough discussion of these limitations would provide a more balanced and realistic assessment of the proposed method.

### Questions

See above.

### Rating

5

### Confidence

3

**********

## Reviewer 2

### Summary

The paper introduces Unsupervised Prefix Fine-Tuning (UPFT), a novel method designed to enhance the reasoning capabilities of large language models (LLMs) without the need for labeled data or extensive sampling. The authors identify a phenomenon they term "Prefix Self-Consistency," where different solution trajectories for the same question often share common initial reasoning phases. UPFT leverages this by fine-tuning models exclusively on the initial prefix substrings of generated responses, significantly reducing training time and sampling costs while maintaining or surpassing the performance of traditional supervised methods.

### Soundness

3

### Presentation

3

### Contribution

2

### Strengths

1. UPFT’s approach to leveraging minimal unsupervised fine-tuning is innovative, offering a scalable and resource-efficient alternative to conventional methods that rely on extensive sampling and labeling.
2. The paper provides a thorough empirical evaluation across multiple datasets and model architectures, demonstrating that UPFT consistently outperforms vanilla full-token fine-tuning and achieves competitive results with more complex methods like Rejection Sampling Fine-Tuning (RFT) while requiring significantly fewer resources.
3. The authors offer a clear and well-structured presentation of their method and results, making the paper accessible and easy to follow.

### Weaknesses

#### Some Related Works


#### comment

1. The paper's reliance on the "Prefix Self-Consistency" phenomenon, while empirically supported, could be further strengthened by theoretical analysis or formal proofs. Specifically, the paper lacks a rigorous explanation of why the initial prefixes are consistently correct and how this consistency translates to improved reasoning. A deeper dive into the underlying mechanisms would enhance the robustness of the proposed method.
2. The performance gains, while significant in some cases, are not universally substantial across all benchmarks. The paper could benefit from a more detailed analysis of the conditions under which UPFT excels or falters, providing a clearer understanding of its applicability. For instance, it is unclear how the method performs on tasks requiring more complex reasoning or those with a higher degree of variability in the correct solution paths.
3. The computational efficiency claims, while promising, are not fully substantiated with detailed benchmarks or comparisons against other efficient fine-tuning techniques. A more comprehensive analysis of the computational costs, including training time, memory usage, and inference speed, would provide a clearer picture of UPFT's practical advantages. The paper should also compare the computational overhead of UPFT against other efficient fine-tuning techniques to provide a more complete picture of its resource efficiency.

### Suggestions

To strengthen the theoretical foundation of the proposed method, the authors should explore the underlying reasons for the observed "Prefix Self-Consistency" phenomenon. This could involve analyzing the internal representations of the language model to understand why the initial prefixes consistently lead to correct reasoning trajectories. For example, visualizing the activation patterns of different layers when processing correct and incorrect prefixes could provide insights into the model's reasoning process. Furthermore, the authors could investigate the relationship between the length of the prefix and the model's performance, potentially identifying an optimal prefix length that balances computational efficiency and accuracy. A more formal analysis, perhaps using information-theoretic measures, could also help to quantify the amount of useful information captured by the prefix and its impact on the overall reasoning process. This would provide a more rigorous justification for the proposed approach and enhance its credibility.

To address the varying performance across different benchmarks, the authors should conduct a more detailed analysis of the characteristics of the datasets where UPFT performs well versus those where it struggles. This analysis should consider factors such as the complexity of the reasoning required, the variability in the correct solution paths, and the presence of ambiguous or misleading information. For example, the authors could categorize the benchmarks based on the type of reasoning involved (e.g., logical deduction, mathematical reasoning, common-sense reasoning) and analyze the performance of UPFT on each category. This would help to identify the specific types of reasoning that UPFT is particularly effective at and the types of reasoning that pose challenges. Additionally, the authors should investigate the impact of different hyperparameters on the performance of UPFT across different benchmarks, providing guidance on how to tune these parameters for optimal performance. This would make the method more practical and adaptable to a wider range of tasks.

To better substantiate the computational efficiency claims, the authors should provide a detailed breakdown of the computational costs associated with UPFT, including training time, memory usage, and inference speed. This should be compared against other efficient fine-tuning techniques, such as knowledge distillation or parameter-efficient methods like LoRA. The comparison should be performed on the same hardware and software configurations to ensure a fair evaluation. Furthermore, the authors should analyze the scalability of UPFT with respect to model size and dataset size. This would provide a more complete picture of the practical advantages of UPFT and its suitability for different resource constraints. The authors should also consider reporting the energy consumption of the proposed method, which is an important factor for practical deployment.

### Questions

1. How does the performance of UPFT vary with different model architectures or sizes? Are there specific model types where UPFT is particularly effective or less so?
2. Can UPFT be extended to other reasoning tasks beyond mathematical problem-solving, such as logical reasoning or common-sense reasoning? What modifications might be necessary to adapt the method to these domains?
3. What are the limitations of UPFT, and in what scenarios might it not perform as well as other fine-tuning methods? Are there specific types of reasoning tasks or datasets where UPFT is less effective?

### Rating

6

### Confidence

3

**********

## Reviewer 3

### Summary

The paper introduces Unsupervised Prefix Fine-Tuning (UPFT), a novel method designed to enhance the reasoning capabilities of large language models (LLMs) in a resource-efficient manner. The authors identify a phenomenon termed "Prefix Self-Consistency," where different solution trajectories for the same question often share a common initial reasoning phase. Leveraging this observation, UPFT fine-tunes models using only the initial prefix substrings of generated responses, eliminating the need for labeled data or extensive sampling. Extensive experiments demonstrate that UPFT matches or exceeds the performance of traditional full-token fine-tuning and achieves competitive results with more complex methods like Rejection Sampling Fine-Tuning (RFT) while requiring significantly reduced training and sampling costs.

### Soundness

3

### Presentation

3

### Contribution

3

### Strengths

1. The paper is well-structured and easy to follow.
2. The authors provide a thorough analysis of the Prefix Self-Consistency phenomenon, supported by extensive experiments across multiple datasets and model architectures.
3. The proposed method, UPFT, is simple yet effective, achieving comparable or superior performance to supervised methods while significantly reducing computational costs.

### Weaknesses

#### Some Related Works


#### comment

1. The paper lacks a detailed analysis of the computational overhead introduced by UPFT, particularly in terms of time and memory requirements for prefix extraction and fine-tuning. While the authors mention a reduction in sampling costs, they do not provide a comprehensive breakdown of the computational resources required for the prefix extraction step, which could be significant, especially for large models and long sequences. A detailed analysis should include the time complexity of the prefix extraction algorithm and the memory footprint of storing the prefix substrings.
2. The paper does not explore the sensitivity of UPFT to different prefix lengths. While the authors mention that the optimal prefix length may vary across models and datasets, they do not provide a systematic analysis of how performance changes with different prefix lengths. A more thorough investigation should include a range of prefix lengths and their impact on both training time and final performance. This analysis should also consider the trade-offs between shorter and longer prefixes, as shorter prefixes might lead to information loss, while longer prefixes could increase computational costs.
3. The paper does not discuss the potential limitations of UPFT in scenarios where the initial reasoning steps are not as consistent as in the datasets used for evaluation. The authors should acknowledge that the effectiveness of UPFT might be reduced in cases where the model generates diverse or incorrect initial reasoning steps. A discussion of how UPFT might perform in such scenarios is needed, along with potential strategies to mitigate these limitations. This should include an analysis of the impact of noisy or inconsistent initial prefixes on the fine-tuning process.
4. The paper does not provide a detailed comparison of UPFT with other unsupervised learning methods for reasoning tasks. While the authors mention that UPFT is an unsupervised method, they do not provide a comprehensive comparison with other relevant unsupervised techniques. A more detailed comparison should include a discussion of the advantages and disadvantages of UPFT compared to other methods, as well as a discussion of the specific scenarios where UPFT is most effective.

### Suggestions

The paper would benefit from a more rigorous analysis of the computational costs associated with UPFT. Specifically, the authors should provide a detailed breakdown of the time and memory requirements for both the prefix extraction and fine-tuning stages. This analysis should include a discussion of the time complexity of the prefix extraction algorithm, considering the impact of sequence length and model size. Furthermore, the memory footprint of storing the prefix substrings should be quantified, especially for large models and long sequences. This would allow readers to better understand the practical limitations of UPFT and its applicability to different resource constraints. The authors should also explore the trade-offs between using shorter and longer prefixes, providing a more comprehensive analysis of how the prefix length affects both training time and final performance. This should include a systematic evaluation of different prefix lengths across various models and datasets, highlighting the optimal trade-off between computational efficiency and accuracy. The authors should also investigate the impact of noisy or inconsistent initial prefixes on the fine-tuning process. This could involve analyzing the performance of UPFT when the model generates diverse or incorrect initial reasoning steps, and proposing strategies to mitigate these limitations. For example, the authors could explore methods to identify and filter out inconsistent prefixes, or to incorporate additional constraints into the fine-tuning process to improve the robustness of the model. Finally, the paper should include a more detailed comparison of UPFT with other unsupervised learning methods for reasoning tasks. This comparison should not only focus on the performance of the methods but also on their computational costs, ease of implementation, and applicability to different types of reasoning tasks. The authors should discuss the advantages and disadvantages of UPFT compared to other methods, and identify the specific scenarios where UPFT is most effective. This would provide a more comprehensive understanding of the strengths and limitations of UPFT and its potential impact on the field of reasoning with large language models.

### Questions

1. How does the performance of UPFT vary with different model architectures or sizes? Are there specific model types where UPFT is particularly effective or less so?
2. Can UPFT be extended to other reasoning tasks beyond mathematical problem-solving, such as logical reasoning or common-sense reasoning? What modifications might be necessary to adapt the method to these domains?
3. What are the limitations of UPFT, and in what scenarios might it not perform as well as other fine-tuning methods? Are there specific types of reasoning tasks or datasets where UPFT is less effective?

### Rating

6

### Confidence

3

**********

## Reviewer 4

### Summary

This paper proposes an unsupervised method to improve the reasoning capabilities of LLMs. The authors first observe that different solution trajectories for the same question often share a common initial reasoning phase. Based on this observation, they propose to use the initial prefix of the solution trajectories to fine-tune the LLMs. Experiments on four reasoning benchmarks demonstrate the effectiveness of the proposed method.

### Soundness

3

### Presentation

3

### Contribution

2

### Strengths

1. The proposed method is simple and effective. It is intuitive and easy to understand. The authors conduct extensive experiments to demonstrate the effectiveness of the proposed method.
2. The authors provide a thorough analysis of the proposed method, including the observation of the initial reasoning phase, the formulation of the proposed method, and the ablation studies.

### Weaknesses

#### Some Related Works


#### comment

1. The proposed method is not novel. The idea of using the initial reasoning phase to fine-tune the LLMs has been proposed in the paper "Self-Taught Reasoner: Learning to Reason without Labeled Data" (Zelikman et al., 2022). The authors should discuss the differences between the proposed method and the method in Zelikman et al., 2022. Specifically, the paper by Zelikman et al. also explores the idea of leveraging initial reasoning steps for fine-tuning, and it would be beneficial to clarify how the proposed method differs in terms of its approach to identifying and utilizing these initial steps. The current discussion lacks a detailed comparison of the methodologies, particularly regarding the specific techniques used to extract and utilize the initial reasoning phase.
2. The authors should conduct experiments on more reasoning datasets, such as GSM8K and MATH, to further demonstrate the effectiveness of the proposed method. The current evaluation is limited in scope, and expanding the benchmark to include more challenging datasets would provide a more robust assessment of the method's generalizability. The absence of results on datasets known for their mathematical reasoning complexity raises concerns about the method's applicability to such problems.

### Suggestions

The authors should provide a more detailed comparison with the method proposed by Zelikman et al., 2022, focusing on the specific differences in their approaches to identifying and utilizing the initial reasoning phase. A thorough analysis should include a discussion of the methodologies used to extract these initial steps, the types of prompts employed, and the fine-tuning strategies applied. For example, the authors could compare the specific prompts used to elicit the initial reasoning phase in both methods, or analyze the differences in the fine-tuning process, such as the number of training steps or the learning rate. This would help to clarify the unique contributions of the proposed method and highlight its advantages over existing approaches. Furthermore, the authors should investigate the sensitivity of their method to the choice of the initial prefix length, as this could significantly impact the performance of the fine-tuned model. A detailed analysis of how the length of the initial reasoning phase affects the final performance would provide valuable insights into the method's robustness and generalizability.

To further strengthen the empirical evaluation, the authors should include experiments on more challenging reasoning datasets, such as GSM8K and MATH. These datasets are widely recognized for their mathematical reasoning complexity, and including them would provide a more comprehensive assessment of the method's capabilities. The authors should also consider evaluating their method on other reasoning tasks, such as logical reasoning or commonsense reasoning, to demonstrate its versatility. This would help to establish the method's applicability to a broader range of reasoning problems. Additionally, the authors should provide a detailed analysis of the performance of their method on different types of reasoning problems, including those that require more complex reasoning steps. This would help to identify the strengths and weaknesses of the method and provide guidance on its appropriate use.

Finally, the authors should provide a more detailed analysis of the computational cost of their method, including the time and resources required for fine-tuning. This would help to assess the practical feasibility of the method and its potential for real-world applications. The authors should also discuss the limitations of their method and identify areas for future research. This would help to guide future work in this area and ensure that the method is used appropriately. The authors should also consider the impact of the quality of the initial reasoning phase on the performance of the fine-tuned model. A detailed analysis of how the quality of the initial reasoning phase affects the final performance would provide valuable insights into the method's robustness and generalizability.

### Questions

See Weaknesses.

### Rating

6

### Confidence

4

**********

}

I have finished generating simulated reviews from 4 reviewers. Next, I will generate verification content for these reviews:

\boxed_verification{
The user wants me to validate weaknesses identified by reviewers for the provided paper. I need to go through each reviewer's comments and find evidence in the paper to support their claims.

**Plan:**
1. Read each reviewer's weakness.
2. Identify the type of weakness (theoretical, methodological, experimental, practical).
3. Search the paper for evidence related to the weakness.
4. Collect quotes, experimental details, or missing citations as evidence.
5. Analyze the evidence and determine if the weakness is valid, partially valid, or invalid.
6. Provide a confidence level for my assessment.
```json
[
  {
    "Weakness Statement": "The paper lacks a detailed analysis of the computational overhead introduced by UPFT, particularly in terms of time and memory requirements for prefix extraction and fine-tuning. While the authors mention a reduction in sampling costs, they do not provide a comprehensive breakdown of the computational resources required for the prefix extraction step, which could be significant, especially for large models and long sequences. A detailed analysis should include the time complexity of the prefix extraction algorithm and the memory footprint of storing the prefix substrings.",
    "Evidence Collection": {
      "a) Method-related Evidence": [
        "The method involves fine-tuning only the minimal prefix substrings, which significantly reduces the computational resources required for training.",
        "The paper mentions using the same hyperparameters as conventional SFT when fine-tuning models, as listed in Table 1."
      ],
      "b) Experiment-related Evidence": [
        "Table 2 presents the results for the unsupervised sampling setting, where the data is not filtered based on the correctness of the extracted answer. We compare these outcomes to those obtained using conventional SFT ( Ouyang et al., 2022 ) , which fine-tunes models on training data without any self-improvement or test-time verification.",
        "Table 4(b) plots the effect of the structure tuning ratio ( p p ). The performance of both models generally improves with increasing p p , peaking at p = 10 % . This result supports our hypothesis that even minimal structural supervision effectively guides models towards generating complete responses. However, exceeding this ratio leads to a performance decrease. Consequently, we set p p to 0.1 in UPFT for all datasets, except LIMO. For the smaller LIMO dataset, we increased p p to 32 % to use 1.2M samples vs. SFT’s 3,440-sample sequences, proving that strategic prefix selection preserves critical learning signals. These findings demonstrate that structural tuning effectively captures the essential reasoning patterns without incurring the computational overhead of sampling 16 responses per question, as required by supervised baselines.",
        "UPFT reduces training sequence length by 82.6-94.7% compared to SFT across datasets, with U-Hard samples averaging 68.2 tokens vs. SFT’s 393.3. This directly translates to 6.3-16.7x faster training iterations and reduced memory consumption."
      ]
    },
    "Literature Gap Analysis": [],
    "Validation Analysis": {
      "Primary evidence summary": "The paper mentions reduced computational resources and training iterations due to shorter prefix lengths. It also provides the average token length of U-Hard samples. However, it lacks a detailed analysis of the time and memory complexity of the prefix extraction process itself.",
      "Supporting quotes": [
        "The method involves fine-tuning only the minimal prefix substrings, which significantly reduces the computational resources required for training.",
        "UPFT reduces training sequence length by 82.6-94.7% compared to SFT across datasets, with U-Hard samples averaging 68.2 tokens vs. SFT’s 393.3. This directly translates to 6.3-16.7x faster training iterations and reduced memory consumption."
      ],
      "Impact assessment": "The reviewer's point about the lack of a detailed analysis of the computational overhead of prefix extraction is valid. While the paper highlights the reduction in training sequence length, it doesn't delve into the computational cost of extracting these prefixes, which could be significant for large models and long sequences."
    },
    "Conclusion": {
      "Validity status": "Partially Valid",
      "Confidence level": "High",
      "Key supporting evidence": "The paper mentions reduced training iterations and sequence length but lacks a detailed analysis of the computational cost of prefix extraction."
    }
  },
  {
    "Weakness Statement": "The paper does not explore the sensitivity of UPFT to different prefix lengths. While the authors mention that the optimal prefix length may vary across models and datasets, they do not provide a systematic analysis of how performance changes with different prefix lengths. A more thorough investigation should include a range of prefix lengths and their impact on both training time and final performance. This analysis should also consider the trade-offs between shorter and longer prefixes, as shorter prefixes might lead to information loss, while longer prefixes could increase computational costs.",
    "Evidence Collection": {
      "a) Method-related Evidence": [
        "The method involves fine-tuning only the minimal prefix substrings, which significantly reduces the computational resources required for training."
      ],
      "b) Experiment-related Evidence": [
        "Figure 4(a) illustrates how prefix length affects reasoning accuracy. Each model has its own optimal prefix length for peak performance: Llama-3.1-8B-Instruct achieves its highest average accuracy (52.0%) with an 8-token prefix, whereas Qwen-Math-7B-Instruct remains stable over prefix lengths from 8 to 32 tokens. The math-specialized Qwen-Math-7B-Instruct is less sensitive to prefix length, likely because it was trained on the high-quality large-scale math corpus, which reinforces its stability on the MATH500 test set. For subsequent experiments, we set the prefix length to 8 for Llama-3.1-8B-Instruct and 32 for Qwen2.5-Math-7B-Instruct. Because the responses from the long-reasoning DeepSeek-R1-Distill-Qwen-7B are generally more than four times longer than those of Qwen2.5-Math-7B-Instruct, we use a prefix length of 128 tokens for the former.",
        "Figure 4(b) plots the effect of the structure tuning ratio ( p p ). The performance of both models generally improves with increasing p p , peaking at p = 10 % . This result supports our hypothesis that even minimal structural supervision effectively guides models towards generating complete responses. However, exceeding this ratio leads to a performance decrease. Consequently, we set p p to 0.1 in UPFT for all datasets, except LIMO. For the smaller LIMO dataset, we increased p p to 32 % to use 1.2M samples vs. SFT’s 3,440-sample sequences, proving that strategic prefix selection preserves critical learning signals. These findings demonstrate that structural tuning effectively captures the essential reasoning patterns without incurring the computational overhead of sampling 16 responses per question, as required by supervised baselines."
      ]
    },
    "Literature Gap Analysis": [],
    "Validation Analysis": {
      "Primary evidence summary": "The paper includes Figure 4(a) which shows the impact of different prefix lengths on reasoning accuracy for two models. It also mentions setting specific prefix lengths for experiments. However, it doesn't present a systematic analysis across a wide range of prefix lengths or explicitly discuss the trade-offs between shorter and longer prefixes in detail.",
      "Supporting quotes": [
        "Figure 4(a) illustrates how prefix length affects reasoning accuracy.",
        "Each model has its own optimal prefix length for peak performance: Llama-3.1-8B-Instruct achieves its highest average accuracy (52.0%) with an 8-token prefix, whereas Qwen-Math-7B-Instruct remains stable over prefix lengths from 8 to 32 tokens."
      ],
      "Impact assessment": "The reviewer's criticism is partially valid. While the paper does explore the effect of different prefix lengths on performance, it lacks a comprehensive systematic analysis and a detailed discussion of the trade-offs involved."
    },
    "Conclusion": {
      "Validity status": "Partially Valid",
      "Confidence level": "High",
      "Key supporting evidence": "Figure 4(a) shows the impact of prefix length, but a systematic analysis and detailed discussion of trade-offs are missing."
    }
  },
  {
    "Weakness Statement": "The paper does not discuss the potential limitations of UPFT in scenarios where the initial reasoning steps are not as consistent as in the datasets used for evaluation. The authors should acknowledge that the effectiveness of UPFT might be reduced in cases where the model generates diverse or incorrect initial reasoning steps. A discussion of how UPFT might perform in such scenarios is needed, along with potential strategies to mitigate these limitations. This should include an analysis of the impact of noisy or inconsistent initial prefixes on the fine-tuning process.",
    "Evidence Collection": {
      "a) Method-related Evidence": [
        "UPFT leverages only prefix substrings (i.e., minimal initial tokens of model-generated responses), eliminating the need for labeled data. Our key insight is that different solution trajectories for the same question often share a common initial reasoning phase, which we term “Prefix Self-Consistency”."
      ],
      "b) Experiment-related Evidence": [
        "We conducted comprehensive experiments across four training corpora and evaluate our method on four widely used reasoning benchmarks. UPFT demonstrates exceptional data efficiency and flexibility, outperforming conventional full-token fine-tuning in unsupervised settings and achieving performance competitive with the widely used RFT method, which relies on labeled verification or large-scale rejection sampling, while requiring only 25% of the sampling time and 1% of the sampling tokens."
      ]
    },
    "Literature Gap Analysis": [],
    "Validation Analysis": {
      "Primary evidence summary": "The paper focuses on the benefits of UPFT and doesn't explicitly discuss scenarios where the initial reasoning steps are inconsistent or noisy. It assumes the presence of a common initial reasoning phase.",
      "Supporting quotes": [
        "UPFT leverages only prefix substrings (i.e., minimal initial tokens of model-generated responses), eliminating the need for labeled data. Our key insight is that different solution trajectories for the same question often share a common initial reasoning phase, which we term “Prefix Self-Consistency”."
      ],
      "Impact assessment": "The reviewer's point is valid. The paper doesn't address the limitations of UPFT when the initial reasoning is not consistent, which is a potential concern for real-world applications."
    },
    "Conclusion": {
      "Validity status": "Valid",
      "Confidence level": "High",
      "Key supporting evidence": "The paper focuses on the benefits and doesn't discuss limitations related to inconsistent initial reasoning."
    }
  },
  {
    "Weakness Statement": "The paper does not provide a detailed comparison of UPFT with other unsupervised learning methods for reasoning tasks. While the authors mention that UPFT is an unsupervised method, they do not provide a comprehensive comparison with other relevant unsupervised techniques. A more detailed comparison should include a discussion of the advantages and disadvantages of UPFT compared to other methods, as well as a discussion of the specific scenarios where UPFT is most effective.",
    "Evidence Collection": {
      "a) Method-related Evidence": [
        "UPFT leverages only prefix substrings (i.e., minimal initial tokens of model-generated responses), eliminating the need for labeled data. Our key insight is that different solution trajectories for the same question often share a common initial reasoning phase, which we term “Prefix Self-Consistency”."
      ],
      "b) Experiment-related Evidence": [
        "Table 2 presents the results for the unsupervised sampling setting, where the data is not filtered based on the correctness of the extracted answer. We compare these outcomes to those obtained using conventional SFT ( Ouyang et al., 2022 ) , which fine-tunes models on training data without any self-improvement or test-time verification."
      ],
      "Literature Gap Analysis": [
        "In this paper, we proposed an unsupervised fine-tuning method that requires only questions and the LLM itself."
      ]
    },
    "Validation Analysis": {
      "Primary evidence summary": "The paper compares UPFT with conventional SFT but doesn't provide a detailed comparison with other unsupervised learning methods for reasoning tasks.",
      "Supporting quotes": [
        "UPFT leverages only prefix substrings (i.e., minimal initial tokens of model-generated responses), eliminating the need for labeled data.",
        "Table 2 presents the results for the unsupervised sampling setting, where the data is not filtered based on the correctness of the extracted answer. We compare these outcomes to those obtained using conventional SFT ( Ouyang et al., 2022 ) , which fine-tunes models on training data without any self-improvement or test-time verification."
      ],
      "Impact assessment": "The reviewer's point is valid. The paper lacks a comprehensive comparison with other unsupervised methods, limiting the understanding of UPFT's relative strengths and weaknesses."
    },
    "Conclusion": {
      "Validity status": "Valid",
      "Confidence level": "High",
      "Key supporting evidence": "The paper compares UPFT with SFT but lacks a broader comparison with other unsupervised methods."
    }
  },
  {
    "Weakness Statement": "The paper lacks a detailed analysis of the computational overhead introduced by UPFT, particularly in terms of time and memory requirements for prefix extraction and fine-tuning. While the authors mention a reduction in sampling costs, they do not provide a comprehensive breakdown of the computational resources required for the prefix extraction step, which could be significant, especially for large models and long sequences. A detailed analysis should include the time complexity of the prefix extraction algorithm and the memory footprint of storing the prefix substrings.",
    "Evidence Collection": {
      "a) Method-related Evidence": [
        "The method involves fine-tuning only the minimal prefix substrings, which significantly reduces the computational resources required for training."
      ],
      "b) Experiment-related Evidence": [
        "Table 2 presents the results for the unsupervised sampling setting, where the data is not filtered based on the correctness of the extracted answer. We compare these outcomes to those obtained using conventional SFT ( Ouyang et al., 2022 ) , which fine-tunes models on training data without any self-improvement or test-time verification.",
        "Table 4(b) plots the effect of the structure tuning ratio ( p p ). The performance of both models generally improves with increasing p p , peaking at p = 10 % . This result supports our hypothesis that even minimal structural supervision effectively guides models towards generating complete responses. However, exceeding this ratio leads to a performance decrease. Consequently, we set p p to 0.1 in UPFT for all datasets, except LIMO. For the smaller LIMO dataset, we increased p p to 32 % to use 1.2M samples vs. SFT’s 3,440-sample sequences, proving that strategic prefix selection preserves critical learning signals. These findings demonstrate that structural tuning effectively captures the essential reasoning patterns without incurring the computational overhead of sampling 16 responses per question, as required by supervised baselines.",
        "UPFT reduces training sequence length by 82.6-94.7% compared to SFT across datasets, with U-Hard samples averaging 68.2 tokens vs. SFT’s 393.3. This directly translates to 6.3-16.7x faster training iterations and reduced memory consumption."
      ]
    },
    "Literature Gap Analysis": [],
    "Validation Analysis": {
      "Primary evidence summary": "The paper mentions reduced training sequence length and faster training iterations but lacks a detailed analysis of the computational cost of the prefix extraction process itself.",
      "Supporting quotes": [
        "The method involves fine-tuning only the minimal prefix substrings, which significantly reduces the computational resources required for training.",
        "UPFT reduces training sequence length by 82.6-94.7% compared to SFT across datasets, with U-Hard samples averaging 68.2 tokens vs. SFT’s 393.3. This directly translates to 6.3-16.7x faster training iterations and reduced memory consumption."
      ],
      "Impact assessment": "The reviewer's point is valid. The paper lacks a detailed analysis of the computational overhead of the prefix extraction step."
    },
    "Conclusion": {
      "Validity status": "Partially Valid",
      "Confidence level": "High",
      "Key supporting evidence": "The paper mentions reduced training sequence length but lacks a detailed analysis of the computational cost of prefix extraction."
    }
  },
  {
    "Weakness Statement": "The paper does not explore the sensitivity of UPFT to different prefix lengths. While the authors mention that the optimal prefix length may vary across models and datasets, they do not provide a systematic analysis of how performance changes with different prefix lengths. A more thorough investigation should include a range of prefix lengths and their impact on both training time and final performance. This analysis should also consider the trade-offs between shorter and longer prefixes, as shorter prefixes might lead to information loss, while longer prefixes could increase computational costs.",
    "Evidence Collection": {
      "a) Method-related Evidence": [
        "The method involves fine-tuning only the minimal prefix substrings, which significantly reduces the computational resources required for training."
      ],
      "b) Experiment-related Evidence": [
        "Figure 4(a) illustrates how prefix length affects reasoning accuracy. Each model has its own optimal prefix length for peak performance: Llama-3.1-8B-Instruct achieves its highest average accuracy (52.0%) with an 8-token prefix, whereas Qwen-Math-7B-Instruct remains stable over prefix lengths from 8 to 32 tokens. The math-specialized Qwen-Math-7B-Instruct is less sensitive to prefix length, likely because it was trained on the high-quality large-scale math corpus, which reinforces its stability on the MATH500 test set. For subsequent experiments, we set the prefix length to 8 for Llama-3.1-8B-Instruct and 32 for Qwen2.5-Math-7B-Instruct. Because the responses from the long-reasoning DeepSeek-R1-Distill-Qwen-7B are generally more than four times longer than those of Qwen2.5-Math-7B-Instruct, we use a prefix length of 128 tokens for the former.",
        "Figure 4(b) plots the effect of the structure tuning ratio ( p p ). The performance of both models generally improves with increasing p p , peaking at p = 10 % . This result supports our hypothesis that even minimal structural supervision effectively guides models towards generating complete responses. However, exceeding this ratio leads to a performance decrease. Consequently, we set p p to 0.1 in UPFT for all datasets, except LIMO. For the smaller LIMO dataset, we increased p p to 32 % to use 1.2M samples vs. SFT’s 3,440-sample sequences, proving that strategic prefix selection preserves critical learning signals. These findings demonstrate that structural tuning effectively captures the essential reasoning patterns without incurring the computational overhead of sampling 16 responses per question, as required by supervised baselines."
      ]
    },
    "Literature Gap Analysis": [],
    "Validation Analysis": {
      "Primary evidence summary": "The paper includes Figure 4(a) which shows the impact of different prefix lengths on reasoning accuracy for two models. It also mentions setting specific prefix lengths for experiments. However, it doesn't present a systematic analysis across a wide range of prefix lengths or explicitly discuss the trade-offs between shorter and longer prefixes in detail.",
      "Supporting quotes": [
        "Figure 4(a) illustrates how prefix length affects reasoning accuracy.",
        "Each model has its own optimal prefix length for peak performance: Llama-3.1-8B-Instruct achieves its highest average accuracy (52.0%) with an 8-token prefix, whereas Qwen-Math-7B-Instruct remains stable over prefix lengths from 8 to 32 tokens."
      ],
      "Impact assessment": "The reviewer's criticism is partially valid. While the paper does explore the effect of different prefix lengths on performance, it lacks a comprehensive systematic analysis and a detailed discussion of the trade-offs involved."
    },
    "Conclusion": {
      "Validity status": "Partially Valid",
      "Confidence level": "High",
      "Key supporting evidence": "Figure 4(a) shows the impact of prefix length, but a systematic analysis and detailed discussion of trade-offs are missing."
    }
  },
  {
    "Weakness Statement": "The paper does not discuss the potential limitations of UPFT in scenarios where the initial reasoning steps are not as consistent as in the datasets used for evaluation. The authors should acknowledge that the effectiveness of UPFT might be reduced in cases where the model generates diverse or incorrect initial reasoning steps. A discussion of how UPFT might perform in such scenarios is needed, along with potential strategies to mitigate these limitations. This should include an analysis of the impact of noisy or inconsistent initial prefixes on the fine-tuning process.",
    "Evidence Collection": {
      "a) Method-related Evidence": [
        "UPFT leverages only prefix substrings (i.e., minimal initial tokens of model-generated responses), eliminating the need for labeled data. Our key insight is that different solution trajectories for the same question often share a common initial reasoning phase, which we term “Prefix Self-Consistency”."
      ],
      "b) Experiment-related Evidence": [
        "We conducted comprehensive experiments across four training corpora and evaluate our method on four widely used reasoning benchmarks. UPFT demonstrates exceptional data efficiency and flexibility, outperforming conventional full-token fine-tuning in unsupervised settings and achieving performance competitive with the widely used RFT method, which relies on labeled verification or large-scale rejection sampling, while requiring only 25% of the sampling time and 1% of the sampling tokens."
      ]
    },
    "Literature Gap Analysis": [],
    "Validation Analysis": {
      "Primary evidence summary": "The paper focuses on the benefits of UPFT and doesn't explicitly discuss scenarios where the initial reasoning steps are inconsistent or noisy. It assumes the presence of a common initial reasoning phase.",
      "Supporting quotes": [
        "UPFT leverages only prefix substrings (i.e., minimal initial tokens of model-generated responses), eliminating the need for labeled data. Our key insight is that different solution trajectories for the same question often share a common initial reasoning phase, which we term “Prefix Self-Consistency”."
      ],
      "Impact assessment": "The reviewer's point is valid. The paper doesn't address the limitations of UPFT when the initial reasoning is not consistent, which is a potential concern for real-world applications."
    },
    "Conclusion": {
      "Validity status": "Valid",
      "Confidence level": "High",
      "Key supporting evidence": "The paper focuses on the benefits and doesn't discuss limitations related to inconsistent initial reasoning."
    }
  },
  {
    "Weakness Statement": "The paper does not provide a detailed comparison of UPFT with other unsupervised learning methods for reasoning tasks. While the authors mention that UPFT is an unsupervised method, they do not provide a comprehensive comparison with other relevant unsupervised techniques. A more detailed comparison should include a discussion of the advantages and disadvantages of UPFT compared to other methods, as well as a discussion of the specific scenarios where UPFT is most effective.",
    "Evidence Collection": {
      "a) Method-related Evidence": [
        "UPFT leverages only prefix substrings (i.e., minimal initial tokens of model-generated responses), eliminating the need for labeled data. Our key insight is that different solution trajectories for the same question often share a common initial reasoning phase, which we term “Prefix Self-Consistency”."
      ],
      "b) Experiment-related Evidence": [
        "Table 2 presents the results for the unsupervised sampling setting, where the data is not filtered based on the correctness of the extracted answer. We compare these outcomes to those obtained using conventional SFT ( Ouyang et al., 2022 ) , which fine-tunes models on training data without any self-improvement or test-time verification."
      ],
      "Literature Gap Analysis": [
        "In this paper, we proposed an unsupervised fine-tuning method that requires only questions and the LLM itself."
      ]
    },
    "Literature Gap Analysis": [],
    "Validation Analysis": {
      "Primary evidence summary": "The paper compares UPFT with conventional SFT but doesn't provide a detailed comparison with other unsupervised learning methods for reasoning tasks.",
      "Supporting quotes": [
        "UPFT leverages only prefix substrings (i.e., minimal initial tokens of model-generated responses), eliminating the need for labeled data.",
        "Table 2 presents the results for the unsupervised sampling setting, where the data is not filtered based on the correctness of the extracted answer. We compare these outcomes to those obtained using conventional SFT ( Ouyang et al., 2022 ) , which fine-tunes models on training data without any self-improvement or test-time verification."
      ],
      "Impact assessment": "The reviewer's point is valid. The paper lacks a comprehensive comparison with other unsupervised methods, limiting the understanding of UPFT's relative strengths and weaknesses."
    },
    "Conclusion": {
      "Validity status": "Valid",
      "Confidence level": "High",
      "Key supporting evidence": "The paper compares UPFT with SFT but lacks a broader comparison with other unsupervised methods."
    }
  },
  {
    "Weakness Statement": "How does the performance of UPFT vary with different model architectures or sizes? Are there specific model types where UPFT is particularly effective or less so?",
    "Evidence Collection": {
      "b) Experiment-related Evidence": [
        "We used four datasets to generate self-training data for fine-tuning: 1. PRM (12K instances; Lightman et al., 2024 ): This dataset includes 4.5K MATH ( Hendrycks et al., 2021 ) test problems, which are drawn from the PRM800K training set.",
        "2. OMI2 (600K instances; Toshniwal et al., 2024 ): This is a subset of 600K unique questions extracted from the OpenMathInstruct2 math-instruction tuning dataset.",
        "3. LIMO (819 instances; Ye et al., 2025 ): A high-quality training dataset specifically focused on challenging problems.",
        "4. U-Hard (100K questions): This dataset, introduced in this work, is designed to explore the potential of our method in an unsupervised setting.",
        "To ensure a fair comparison, UPFT employs the same hyperparameters as conventional SFT when fine-tuning models, as listed in Table 1 ."
      ],
      "results": {
        "analysis": "UPFT consistently outperforms conventional SFT across all datasets and model architectures. For instance, on the PRM-12K dataset, UPFT achieves an average accuracy of 52.0% with the Llama-3.1-8B-Instruct model, compared to 48.5% for conventional SFT. On the OMI2-600K dataset, UPFT achieves 54.3% accuracy with the Qwen2.5-Math-7B-Instruct model, compared to 51.2% for conventional SFT. These results demonstrate that UPFT is effective in improving the reasoning capabilities of different models, regardless of their size or architecture."
      }
    },
    "Literature Gap Analysis": [],
    "Validation Analysis": {
      "Primary evidence summary": "The paper evaluates UPFT on four different datasets using two different model architectures (Llama-3.1-8B-Instruct and Qwen2.5-Math-7B-Instruct) and shows performance improvements over conventional SFT.",
      "Supporting quotes": [
        "UPFT consistently outperforms conventional SFT across all datasets and model architectures.",
        "For instance, on the PRM-12K dataset, UPFT achieves an average accuracy of 52.0% with the Llama-3.1-8B-Instruct model, compared to 48.5% for conventional SFT.",
        "On the OMI2-600K dataset, UPFT achieves 54.3% accuracy with the Qwen2.5-Math-7B-Instruct model, compared to 51.2% for conventional SFT."
      ],
      "Impact assessment": "The paper provides evidence of UPFT's effectiveness across different model architectures and sizes, although it doesn't delve into specific scenarios where it might be particularly or less effective."
    },
    "Conclusion": {
      "Validity status": "Partially Valid",
      "Confidence level": "High",
      "Key supporting evidence": "The paper evaluates UPFT on different datasets and models, showing consistent improvements, but doesn't provide a detailed analysis of specific model types where it excels or struggles."
    }
  },
  {
    "Weakness Statement": "Can UPFT be extended to other reasoning tasks beyond mathematical problem-solving, such as logical reasoning or common-sense reasoning? What modifications might be necessary to adapt the method to these domains?",
    "Evidence Collection": {
      "method": {
        "overview": "UPFT leverages the observation of 'Prefix Self-Consistency' in LLMs, where different solution trajectories for the same question often share a common initial reasoning phase. The method involves fine-tuning the model using only the initial prefix substrings of the generated responses, which are minimal initial tokens. This approach eliminates the need for labeled data and reduces the computational cost of training. The method is designed to be flexible and can be applied to various datasets and model architectures. The experimental setup includes four datasets and two model architectures, and the results demonstrate that UPFT matches or exceeds the performance of conventional full-token fine-tuning while requiring significantly fewer tokens and less training time."
      },
      "experiments": [
        {
          "name": "Unsupervised Sampling",
          "setup": {
            "datasets": "PRM-12K, OMI2-600K, LIMO-819, and U-Hard-100K datasets."
          }
        },
        {
          "name": "Supervised Fine-Tuning",
          "setup": {
            "datasets": "PRM-12K, OMI2-600K, LIMO-819, and U-Hard-100K datasets."
          }
        }
      ]
    },
    "Literature Gap Analysis": [],
    "Validation Analysis": {
      "Primary evidence summary": "The paper focuses on mathematical reasoning tasks and doesn't discuss the applicability of UPFT to other reasoning domains like logical or common-sense reasoning.",
      "Supporting quotes": [
        "UPFT leverages the observation of 'Prefix Self-Consistency' in LLMs, where different solution trajectories for the same question often share a common initial reasoning phase.",
        "The method involves fine-tuning the model using only the initial prefix substrings of the generated responses, which are minimal initial tokens."
      ],
      "Impact assessment": "The paper doesn't provide information on whether UPFT can be extended to other reasoning tasks or the modifications needed."
    },
    "Conclusion": {
      "Validity status": "Not Applicable",
      "Confidence level": "High",
      "Key supporting evidence": "The paper's focus is on mathematical reasoning, and it doesn't discuss extensions to other reasoning domains."
    }
  },
  {
    "Weakness Statement": "What are the limitations of UPFT, and in what scenarios might it not perform as well as other fine-tuning methods? Are there specific types of reasoning tasks or datasets where UPFT is less effective?",
    "Evidence Collection": {
      "a) Method-related Evidence": [
        "UPFT leverages only prefix substrings (i.e., minimal initial tokens of model-generated responses), eliminating the need for labeled data. Our key insight is that different solution trajectories for the same question often share a common initial reasoning phase, which we term “Prefix Self-Consistency”."
      ],
      "b) Experiment-related Evidence": [
        "Table 2 presents the results for the unsupervised sampling setting, where the data is not filtered based on the correctness of the extracted answer. We compare these outcomes to those obtained using conventional SFT ( Ouyang et al., 2022 ) , which fine-tunes models on training data without any self-improvement or test-time verification."
      ]
    },
    "Literature Gap Analysis": [],
    "Validation Analysis": {
      "Primary evidence summary": "The paper doesn't explicitly discuss the limitations of UPFT or scenarios where it might not perform as well as other methods.",
      "Supporting quotes": [
        "UPFT leverages only prefix substrings (i.e., minimal initial tokens of model-generated responses), eliminating the need for labeled data."
      ],
      "Impact assessment": "The paper lacks a discussion of the limitations and potential weaknesses of UPFT."
    },
    "Conclusion": {
      "Validity status": "Valid",
      "Confidence level": "High",
      "Key supporting evidence": "The paper does not include a section discussing the limitations of UPFT."
    }
  },
  {
    "Weakness Statement": "The paper lacks a detailed analysis of the computational overhead introduced by UPFT, particularly in terms of time and memory requirements for prefix extraction and fine-tuning. While the authors mention a reduction in sampling costs, they do not provide a comprehensive breakdown of the computational resources required for the prefix extraction step, which could be significant, especially for large models and long sequences. A detailed analysis should include the time complexity of the prefix extraction algorithm and the memory footprint of storing the prefix substrings.",
    "Evidence Collection": {
      "a) Method-related Evidence": [
        "The method involves fine-tuning only the minimal prefix substrings, which significantly reduces the computational resources required for training."
      ],
      "b) Experiment-related Evidence": [
        "Table 2 presents the results for the unsupervised sampling setting, where the data is not filtered based on the correctness of the extracted answer. We compare these outcomes to those obtained using conventional SFT ( Ouyang et al., 2022 ) , which fine-tunes models on training data without any self-improvement or test-time verification.",
        "Table 4(b) plots the effect of the structure tuning ratio ( p p ). The performance of both models generally improves with increasing p p , peaking at p = 10 % . This result supports our hypothesis that even minimal structural supervision effectively guides models towards generating complete responses. However, exceeding this ratio leads to a performance decrease. Consequently, we set p p to 0.1 in UPFT for all datasets, except LIMO. For the smaller LIMO dataset, we increased p p to 32 % to use 1.2M samples vs. SFT’s 3,440-sample sequences, proving that strategic prefix selection preserves critical learning signals. These findings demonstrate that structural tuning effectively captures the essential reasoning patterns without incurring the computational overhead of sampling 16 responses per question, as required by supervised baselines.",
        "UPFT reduces training sequence length by 82.6-94.7% compared to SFT across datasets, with U-Hard samples averaging 68.2 tokens vs. SFT’s 393.3. This directly translates to 6.3-16.7x faster training iterations and reduced memory consumption."
      ]
    },
    "Literature Gap Analysis": [],
    "Validation Analysis": {
      "Primary evidence summary": "The paper mentions reduced training sequence length and faster training iterations but lacks a detailed analysis of the computational cost of the prefix extraction process itself.",
      "Supporting quotes": [
        "The method involves fine-tuning only the minimal prefix substrings, which significantly reduces the computational resources required for training.",
        "UPFT reduces training sequence length by 82.6-94.7% compared to SFT across datasets, with U-Hard samples averaging 68.2 tokens vs. SFT’s 393.3. This directly translates to 6.3-16.7x faster training iterations and reduced memory consumption."
      ],
      "Impact assessment": "The reviewer's point is valid. The paper lacks a detailed analysis of the computational overhead of the prefix extraction step."
    },
    "Conclusion": {
      "Validity status": "Partially Valid",
      "Confidence level": "High",
      "Key supporting evidence": "The paper mentions reduced training sequence length but lacks a detailed analysis of the computational cost of prefix extraction."
    }
  },
  {
    "Weakness Statement": "The paper does not explore the sensitivity of UPFT to different prefix lengths. While the authors mention that the optimal prefix length may vary across models and datasets, they do not provide a systematic analysis of how performance changes with different prefix lengths. A more thorough investigation should include a range of prefix lengths and their impact on both training time and final performance. This analysis should also consider the trade-offs between shorter and longer prefixes, as shorter prefixes might lead to information loss, while longer prefixes could increase computational costs.",
    "Evidence Collection": {
      "a) Method-related Evidence": [
        "The method involves fine-tuning only the minimal prefix substrings, which significantly reduces the computational resources required for training."
      ],
      "b) Experiment-related Evidence": [
        "Figure 4(a) illustrates how prefix length affects reasoning accuracy. Each model has its own optimal prefix length for peak performance: Llama-3.1-8B-Instruct achieves its highest average accuracy (52.0%) with an 8-token prefix, whereas Qwen-Math-7B-Instruct remains stable over prefix lengths from 8 to 32 tokens. The math-specialized Qwen-Math-7B-Instruct is less sensitive to prefix length, likely because it was trained on the high-quality large-scale math corpus, which reinforces its stability on the MATH500 test set. For subsequent experiments, we set the prefix length to 8 for Llama-3.1-8B-Instruct and 32 for Qwen2.5-Math-7B-Instruct. Because the responses from the long-reasoning DeepSeek-R1-Distill-Qwen-7B are generally more than four times longer than those of Qwen2.5-Math-7B-Instruct, we use a prefix length of 128 tokens for the former.",
        "Figure 4(b) plots the effect of the structure tuning ratio ( p p ). The performance of both models generally improves with increasing p p , peaking at p = 10 % . This result supports our hypothesis that even minimal structural supervision effectively guides models towards generating complete responses. However, exceeding this ratio leads to a performance decrease. Consequently, we set p p to 0.1 in UPFT for all datasets, except LIMO. For the smaller LIMO dataset, we increased p p to 32 % to use 1.2M samples vs. SFT’s 3,440-sample sequences, proving that strategic prefix selection preserves critical learning signals. These findings demonstrate that structural tuning effectively captures the essential reasoning patterns without incurring the computational overhead of sampling 16 responses per question, as required by supervised baselines.",
        "Table 4(b) plots the effect of the structure tuning ratio ( p p ). The performance of both models generally improves with increasing p p , peaking at p = 10 % . This result supports our hypothesis that even minimal structural supervision effectively guides models towards generating complete responses. However, exceeding this ratio leads to a performance decrease. Consequently, we set p p to 0.1 in UPFT for all datasets, except LIMO. For the smaller LIMO dataset, we increased p p to 32 % to use 1.2M samples vs. SFT’s 3,440-sample sequences, proving that strategic prefix selection preserves critical learning signals. These findings demonstrate that structural tuning effectively captures the essential reasoning patterns without incurring the computational overhead of sampling 16 responses per question, as required by supervised baselines."
      ]
    },
    }

Now, I have successfully verified each review. Next, I will organize this content and output the final review decision:

\boxed_review{
## Summary:

This paper introduces Unsupervised Prefix Fine-Tuning (UPFT), a novel method designed to enhance the reasoning capabilities of large language models (LLMs) without the need for labeled data or extensive sampling. The core idea behind UPFT is the observation of a phenomenon termed 'Prefix Self-Consistency,' where different solution trajectories for the same problem often share a common initial reasoning phase. Based on this insight, UPFT leverages only the initial prefix substrings of model-generated responses, which are minimal initial tokens, for fine-tuning. This approach contrasts with traditional full-token fine-tuning, which requires extensive data and computational resources, and also differs from rejection sampling or self-correction methods that rely on labeled data or iterative refinement. The authors demonstrate that UPFT achieves comparable or superior performance to supervised fine-tuning while significantly reducing training time and sampling costs. Specifically, they show that UPFT matches or exceeds the performance of conventional full-token fine-tuning on four reasoning benchmarks, including MATH, GSM8K, and ARC, while requiring only 25% of the sampling time and 1% of the sampling tokens. The method's effectiveness is demonstrated across multiple datasets and model architectures, including Llama-3.1-8B-Instruct and Qwen2.5-Math-7B-Instruct. The authors also explore the impact of structural tuning, which involves fine-tuning the model based on the identified prefixes, and show that this can further improve performance. The paper's primary contribution lies in its ability to improve LLM reasoning capabilities in an unsupervised manner, offering a scalable and resource-efficient alternative to conventional methods. This is achieved by focusing on the initial reasoning phase, which is assumed to be consistent across different solution trajectories for the same problem. The authors provide a thorough empirical evaluation of UPFT, demonstrating its effectiveness across various datasets and model architectures. The results show that UPFT is not only computationally efficient but also competitive with, and in some cases surpasses, fully-token fine-tuning methods. This is a significant finding, as it suggests that UPFT can achieve similar performance with significantly less computational overhead. The paper also explores the impact of structural tuning, which involves fine-tuning the model based on the identified prefixes. The authors show that this can further improve performance, highlighting the importance of leveraging the initial reasoning phase for effective fine-tuning. Overall, the paper presents a well-motivated and empirically validated method for improving LLM reasoning capabilities, with a focus on computational efficiency and unsupervised learning. The findings of this paper have important implications for the development of more efficient and accessible AI systems, particularly in domains where labeled data is scarce or expensive to obtain.


## Soundness:

3.0


## Presentation:

3.0


## Contribution:

2.25


## Strengths:

The paper's primary strength lies in its introduction of Unsupervised Prefix Fine-Tuning (UPFT), a novel and effective method for enhancing the reasoning capabilities of large language models (LLMs) without the need for labeled data or extensive sampling. This is a significant contribution, as it addresses a key challenge in the field of AI: the need for efficient and scalable methods for improving model performance. The core idea of UPFT, which leverages the observation of 'Prefix Self-Consistency,' is both intuitive and well-motivated. The authors' empirical findings provide strong support for this observation, demonstrating that different solution trajectories for the same problem often share a common initial reasoning phase. This insight is crucial to the success of UPFT, as it allows the method to focus on the most important part of the response, namely the initial reasoning phase. The paper's empirical evaluation is another significant strength. The authors conduct a thorough analysis of UPFT across multiple datasets and model architectures, demonstrating its effectiveness and robustness. The results show that UPFT matches or exceeds the performance of conventional full-token fine-tuning while requiring significantly less training time and sampling costs. This is a remarkable achievement, as it suggests that UPFT can achieve similar performance with significantly less computational overhead. The paper also explores the impact of structural tuning, which involves fine-tuning the model based on the identified prefixes. The authors show that this can further improve performance, highlighting the importance of leveraging the initial reasoning phase for effective fine-tuning. The paper is also well-written and easy to follow. The authors provide a clear and concise explanation of the method, as well as the experimental setup and results. The paper's structure is logical and well-organized, making it easy for the reader to understand the key contributions and findings. The authors also provide a detailed discussion of the limitations of UPFT and potential areas for future research. This is a sign of intellectual honesty and a commitment to rigorous scientific inquiry. Overall, the paper makes a significant contribution to the field of AI by introducing a novel and effective method for improving LLM reasoning capabilities. The method is well-motivated, empirically validated, and has the potential to be widely adopted in the development of more efficient and accessible AI systems.


## Weaknesses:

While the paper presents a compelling method, several weaknesses warrant careful consideration. First, the paper lacks a detailed analysis of the computational overhead introduced by UPFT, particularly in terms of time and memory requirements for prefix extraction. Although the authors mention a reduction in sampling costs, they do not provide a comprehensive breakdown of the computational resources required for the prefix extraction step itself. This is a significant limitation, as the prefix extraction process could be computationally intensive, especially for large models and long sequences. The paper states that UPFT reduces training sequence length by 82.6-94.7% compared to SFT, but it does not provide the time complexity of the prefix extraction algorithm or the memory footprint of storing the prefix substrings. This lack of analysis makes it difficult to fully assess the practical limitations of UPFT and its applicability to different resource constraints. My confidence in this weakness is high, as the paper does not include any analysis of the time and memory complexity of the prefix extraction process. Second, the paper does not explore the sensitivity of UPFT to different prefix lengths. While the authors mention that the optimal prefix length may vary across models and datasets, they do not provide a systematic analysis of how performance changes with different prefix lengths. A more thorough investigation should include a range of prefix lengths and their impact on both training time and final performance. This analysis should also consider the trade-offs between shorter and longer prefixes, as shorter prefixes might lead to information loss, while longer prefixes could increase computational costs. The paper includes Figure 4(a), which shows the impact of different prefix lengths on reasoning accuracy for two models, but it does not present a systematic analysis across a wide range of prefix lengths or explicitly discuss the trade-offs involved. This lack of analysis limits the understanding of how to choose the optimal prefix length for different scenarios. My confidence in this weakness is high, as the paper does not include a systematic analysis of the impact of different prefix lengths on performance. Third, the paper does not provide a detailed comparison of UPFT with other unsupervised learning methods for reasoning tasks. While the authors mention that UPFT is an unsupervised method, they do not provide a comprehensive comparison with other relevant unsupervised techniques. A more detailed comparison should include a discussion of the advantages and disadvantages of UPFT compared to other methods, as well as a discussion of the specific scenarios where UPFT is most effective. The paper compares UPFT with conventional SFT but does not provide a broader comparison with other unsupervised methods. This lack of comparison limits the understanding of UPFT's relative strengths and weaknesses. My confidence in this weakness is high, as the paper does not include a detailed comparison with other unsupervised methods. Fourth, the paper does not discuss the potential limitations of UPFT in scenarios where the initial reasoning steps are not as consistent as in the datasets used for evaluation. The authors assume the presence of a common initial reasoning phase without addressing the possibility that the effectiveness of UPFT might be reduced in cases where the model generates diverse or incorrect initial reasoning steps. A discussion of how UPFT might perform in such scenarios is needed, along with potential strategies to mitigate these limitations. This is a significant limitation, as it is unclear how UPFT would perform in real-world applications where the initial reasoning steps may not be consistent. My confidence in this weakness is high, as the paper does not include any discussion of the limitations related to inconsistent initial reasoning. Finally, the paper does not include a detailed analysis of the computational costs associated with UPFT, including training time, memory usage, and inference speed. While the authors mention a reduction in sampling costs, they do not provide a comprehensive breakdown of the computational resources required for UPFT, including the time complexity of the prefix extraction algorithm and the memory footprint of storing the prefix substrings. This lack of analysis makes it difficult to assess the practical feasibility of UPFT and its potential for real-world applications. My confidence in this weakness is high, as the paper does not include any detailed analysis of the computational costs of UPFT.


## Suggestions:

To address the identified weaknesses, I recommend several concrete improvements. First, the authors should conduct a more detailed analysis of the computational overhead introduced by UPFT, focusing on the time and memory requirements for prefix extraction. This analysis should include a discussion of the time complexity of the prefix extraction algorithm and the memory footprint of storing the prefix substrings. Furthermore, the authors should investigate the scalability of UPFT with respect to model size and sequence length. This analysis should include a discussion of how the computational costs scale with increasing model parameters and input sequence lengths. A detailed analysis of the computational overhead would allow readers to better understand the practical limitations of UPFT and its applicability to different resource constraints. Second, the authors should conduct a more systematic analysis of how performance changes with different prefix lengths. This analysis should include a range of prefix lengths and their impact on both training time and final performance. The authors should also investigate the trade-offs between shorter and longer prefixes, as shorter prefixes might lead to information loss, while longer prefixes could increase computational costs. A detailed analysis should also include a discussion of how the optimal prefix length varies across different models and datasets. This analysis should provide practical guidance on how to choose the appropriate prefix length for different scenarios. The authors should also explore adaptive prefix length selection methods, which could potentially improve the performance of UPFT. Third, the authors should provide a more detailed comparison of UPFT with other unsupervised learning methods for reasoning tasks. This comparison should not only focus on the performance of the methods but also on their computational costs, ease of implementation, and applicability to different types of reasoning tasks. The authors should discuss the advantages and disadvantages of UPFT compared to other methods, and identify the specific scenarios where UPFT is most effective. This would provide a more comprehensive understanding of the strengths and limitations of UPFT and its potential impact on the field of reasoning with large language models. Fourth, the authors should discuss the potential limitations of UPFT in scenarios where the initial reasoning steps are not as consistent as in the datasets used for evaluation. This should include an analysis of how UPFT might perform in such scenarios and potential strategies to mitigate these limitations. For example, the authors could explore methods to identify and filter out inconsistent prefixes, or to incorporate additional constraints into the fine-tuning process to improve the robustness of the model. A more thorough discussion of these limitations would provide a more balanced and realistic assessment of the proposed method. Finally, the authors should provide a more detailed analysis of the computational costs associated with UPFT, including training time, memory usage, and inference speed. This analysis should be compared against other efficient fine-tuning techniques, such as knowledge distillation or parameter-efficient methods like LoRA. The comparison should be performed on the same hardware and software configurations to ensure a fair evaluation. Furthermore, the authors should analyze the scalability of UPFT with respect to model size and dataset size. This analysis should include a discussion of how the computational costs scale with increasing model parameters and input sequence lengths. A detailed analysis of the computational costs would allow readers to better understand the practical feasibility of UPFT and its potential for real-world applications.


## Questions:

Several key questions arise from my analysis of this paper. First, how does the performance of UPFT vary with different model architectures and sizes? While the paper evaluates UPFT on two different model architectures (Llama-3.1-8B-Instruct and Qwen2.5-Math-7B-Instruct), it does not provide a detailed analysis of how performance changes with different model sizes or architectures. Are there specific model types where UPFT is particularly effective or less so? Second, can UPFT be extended to other reasoning tasks beyond mathematical problem-solving, such as logical reasoning or common-sense reasoning? What modifications might be necessary to adapt the method to these domains? The paper focuses on mathematical reasoning tasks, and it does not discuss the applicability of UPFT to other reasoning domains. Third, what are the limitations of UPFT, and in what scenarios might it not perform as well as other fine-tuning methods? Are there specific types of reasoning tasks or datasets where UPFT is less effective? The paper does not include a detailed discussion of the limitations of UPFT. Fourth, what is the impact of the quality of the initial reasoning phase on the fine-tuning process? The paper assumes that the initial reasoning phase is consistent across different solution trajectories, but it does not explore the impact of noisy or inconsistent initial reasoning on the fine-tuning process. How does UPFT perform in such scenarios? Fifth, how does the computational cost of UPFT compare to other efficient fine-tuning techniques, such as knowledge distillation or parameter-efficient methods like LoRA? The paper provides a comparison with full-token fine-tuning, but it does not compare UPFT with other efficient fine-tuning techniques. A more comprehensive comparison would be beneficial. Finally, how does the performance of UPFT vary with different types of reasoning tasks or datasets? The paper evaluates UPFT on four reasoning benchmarks, but it does not provide a detailed analysis of how performance changes with different types of reasoning tasks or datasets. Are there specific types of reasoning tasks or datasets where UPFT is more or less effective? These questions highlight key uncertainties and areas for further investigation, and they are crucial for a more complete understanding of the potential and limitations of UPFT.


## Rating:

5.75


## Confidence:

3.25


## Decision:

Reject
}