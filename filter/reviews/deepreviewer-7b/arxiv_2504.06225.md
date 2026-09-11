I will use Standard Mode for comprehensive thinking. As a professional reviewer, I will simulate 4 different reviewers, followed by the verification thinking. Then I will output the Finally Review Output. Let me think - Standard Mode means I will output the original review, followed by the verification thinking. Considering that I am currently in standard mode, I should think from my existing knowledge and consider some related work content when writing about weaknesses. Then I will output the Finally Review Output and Meta Review Output:

\boxed_simreviewers{
## Reviewer 1

### Summary

This paper explores adapting pre-trained decoder-only LLMs to encoder-decoder architectures for improved quality-efficiency trade-offs. The authors propose a method to initialize encoder-decoder models from pre-trained decoder-only models and fine-tune them on specific tasks. They test their approach on the Gemma 2 model series (2B and 9B parameters) and demonstrate that the adapted encoder-decoder models outperform their decoder-only counterparts after instruction tuning. They also find that encoder-decoder models achieve better contextual representations, as evaluated on SuperGLUE.

### Soundness

3

### Presentation

3

### Contribution

2

### Strengths

- The paper addresses an important problem: improving the quality-efficiency trade-off in LLMs by leveraging the strengths of both encoder-decoder and decoder-only architectures.
- The authors provide a thorough analysis of different pre-training objectives (PrefixLM and UL2) and initialization strategies for encoder-decoder models.
- The paper includes extensive experiments across various benchmarks, including pretraining, instruction-tuning, and SuperGLUE, providing a comprehensive evaluation of the proposed approach.

### Weaknesses

#### Some Related Works


#### comment

 - The paper primarily focuses on adapting the Gemma 2 model series, which limits the generalizability of the findings. It would be beneficial to see how the proposed approach performs on other model architectures, such as LLaMA or QWen.
- The paper does not provide a detailed analysis of the computational costs associated with the proposed adaptation method. It would be helpful to understand the training time and resources required for adapting encoder-decoder models compared to training decoder-only models from scratch.
- The paper could benefit from a more in-depth discussion of the limitations of the proposed approach. For example, are there specific types of tasks or model sizes where the adaptation method is less effective?

### Suggestions

The authors should consider expanding their experimental evaluation to include a wider range of model architectures beyond the Gemma 2 series. Specifically, testing the proposed adaptation method on models like LLaMA or QWen would significantly strengthen the generalizability of their findings. This would involve not only replicating the experiments with these models but also analyzing how the adaptation method performs across different model sizes and pre-training datasets. Such an analysis would reveal whether the observed improvements are consistent across diverse architectures or if specific architectural features of Gemma 2 play a crucial role in the adaptation process. Furthermore, it would be beneficial to explore the impact of different pre-training objectives and initialization strategies on these other architectures to determine if the optimal settings vary across models. This would provide a more comprehensive understanding of the proposed method's applicability and limitations.

To address the lack of computational cost analysis, the authors should include a detailed breakdown of the resources required for their adaptation method. This should include not only the training time but also the memory footprint and the number of GPUs used. A comparison with the computational costs of training decoder-only models from scratch would be particularly valuable. This analysis should also consider the impact of different batch sizes and sequence lengths on the training time and resource utilization. Furthermore, the authors should discuss the scalability of their method, i.e., how the computational costs scale with model size and dataset size. This would help potential users of their method to assess its feasibility for their specific use cases. It would also be useful to provide an estimate of the time required to achieve a certain level of performance, which would allow for a more direct comparison with other methods.

Finally, the authors should provide a more thorough discussion of the limitations of their approach. This should include an analysis of the types of tasks or model sizes where the adaptation method is less effective. For example, are there specific tasks that are more challenging for the adapted encoder-decoder models? Are there certain model sizes where the adaptation method does not provide significant improvements? A detailed analysis of these limitations would provide a more balanced view of the proposed method and help guide future research in this area. It would also be beneficial to discuss the potential reasons for these limitations, such as the differences in the architectural inductive biases between encoder-decoder and decoder-only models. This would help to identify areas where further improvements are needed and provide a more complete understanding of the proposed method's strengths and weaknesses.

### Questions

- How does the proposed adaptation method compare to other approaches for improving the quality-efficiency trade-off in LLMs, such as model pruning or quantization?
- What are the potential benefits and challenges of applying the proposed adaptation method to other encoder-decoder architectures, such as BART or T5?

### Rating

6

### Confidence

3

**********

## Reviewer 2

### Summary

This paper explores adapting pretrained decoder-only LLMs to encoder-decoder architectures, aiming to leverage the strengths of both approaches for improved quality-efficiency trade-offs. The authors propose a method to initialize encoder-decoder models from pretrained decoder-only models and fine-tune them on specific tasks. Their experiments, conducted on the Gemma 2 model series (2B and 9B parameters), demonstrate that the adapted encoder-decoder models outperform their decoder-only counterparts after instruction tuning. They also find that encoder-decoder models achieve better contextual representations, as evaluated on SuperGLUE. The study contributes to the understanding of how to effectively combine different LLM architectures and provides insights into the potential benefits of encoder-decoder models for various NLP tasks.

### Soundness

3

### Presentation

3

### Contribution

2

### Strengths

1. The paper is well-structured and clearly written, making it easy to follow the methodology and results.
2. The authors provide a thorough analysis of different pre-training objectives (PrefixLM and UL2) and initialization strategies for encoder-decoder models.
3. The paper includes extensive experiments across various benchmarks, including pretraining, instruction-tuning, and SuperGLUE, providing a comprehensive evaluation of the proposed approach.

### Weaknesses

#### Some Related Works


#### comment

1. The paper primarily focuses on adapting the Gemma 2 model series, which limits the generalizability of the findings. It would be beneficial to see how the proposed approach performs on other model architectures, such as LLaMA or QWen.
2. The paper does not provide a detailed analysis of the computational costs associated with the proposed adaptation method. It would be helpful to understand the training time and resources required for adapting encoder-decoder models compared to training decoder-only models from scratch.
3. The paper could benefit from a more in-depth discussion of the limitations of the proposed approach. For example, are there specific types of tasks or model sizes where the adaptation method is less effective?

### Suggestions

The authors should consider expanding their experimental evaluation to include a wider range of model architectures beyond the Gemma 2 series. Specifically, testing the proposed adaptation method on models like LLaMA or QWen would significantly strengthen the generalizability of their findings. This would involve not only replicating the experiments with these models but also analyzing how the adaptation method performs across different model sizes and pre-training datasets. Such an analysis would reveal whether the observed improvements are consistent across diverse architectures or if specific architectural features of Gemma 2 play a crucial role in the adaptation process. Furthermore, it would be beneficial to explore the impact of different pre-training objectives and initialization strategies on these other architectures to determine if the optimal settings vary across models. This would provide a more comprehensive understanding of the proposed method's applicability and limitations.

To address the lack of computational cost analysis, the authors should include a detailed breakdown of the resources required for their adaptation method. This should include not only the training time but also the memory footprint and the number of GPUs used. A comparison with the computational costs of training decoder-only models from scratch would be particularly valuable. This analysis should also consider the impact of different batch sizes and sequence lengths on the training time and resource utilization. Furthermore, the authors should discuss the scalability of their method, i.e., how the computational costs scale with model size and dataset size. This would help potential users of their method to assess its feasibility for their specific use cases. It would also be useful to provide an estimate of the time required to achieve a certain level of performance, which would allow for a more direct comparison with other methods.

Finally, the authors should provide a more thorough discussion of the limitations of their approach. This should include an analysis of the types of tasks or model sizes where the adaptation method is less effective. For example, are there specific tasks that are more challenging for the adapted encoder-decoder models? Are there certain model sizes where the adaptation method does not provide significant improvements? A detailed analysis of these limitations would provide a more balanced view of the proposed method and help guide future research in this area. It would also be beneficial to discuss the potential reasons for these limitations, such as the differences in the architectural inductive biases between encoder-decoder and decoder-only models. This would help to identify areas where further improvements are needed and provide a more complete understanding of the proposed method's strengths and weaknesses.

### Questions

1. How does the proposed adaptation method compare to other approaches for improving the quality-efficiency trade-off in LLMs, such as model pruning or quantization?
2. What are the potential benefits and challenges of applying the proposed adaptation method to other encoder-decoder architectures, such as BART or T5?

### Rating

6

### Confidence

3

**********

## Reviewer 3

### Summary

This paper explores adapting pretrained decoder-only LLMs to encoder-decoder architectures for improving the quality-efficiency trade-off. The authors propose a method to initialize encoder-decoder models from pretrained decoder-only models and fine-tune them on specific tasks. They conduct experiments on the Gemma 2 model series (2B and 9B parameters) and demonstrate that the adapted encoder-decoder models outperform their decoder-only counterparts after instruction tuning. They also find that encoder-decoder models achieve better contextual representations, as evaluated on SuperGLUE.

### Soundness

3

### Presentation

3

### Contribution

3

### Strengths

1. The paper addresses an important problem: improving the quality-efficiency trade-off in LLMs by leveraging the strengths of both encoder-decoder and decoder-only architectures.
2. The authors provide a thorough analysis of different pre-training objectives (PrefixLM and UL2) and initialization strategies for encoder-decoder models.
3. The paper includes extensive experiments across various benchmarks, including pretraining, instruction-tuning, and SuperGLUE, providing a comprehensive evaluation of the proposed approach.

### Weaknesses

#### Some Related Works


#### comment

1. The paper primarily focuses on adapting the Gemma 2 model series, which limits the generalizability of the findings. It would be beneficial to see how the proposed approach performs on other model architectures, such as LLaMA or QWen.
2. The paper does not provide a detailed analysis of the computational costs associated with the proposed adaptation method. It would be helpful to understand the training time and resources required for adapting encoder-decoder models compared to training decoder-only models from scratch.
3. The paper could benefit from a more in-depth discussion of the limitations of the proposed approach. For example, are there specific types of tasks or model sizes where the adaptation method is less effective?

### Suggestions

The authors should consider expanding their experimental evaluation to include a wider range of model architectures beyond the Gemma 2 series. Specifically, testing the proposed adaptation method on models like LLaMA or QWen would significantly strengthen the generalizability of their findings. This would involve not only replicating the experiments with these models but also analyzing how the adaptation method performs across different model sizes and pre-training datasets. Such an analysis would reveal whether the observed improvements are consistent across diverse architectures or if specific architectural features of Gemma 2 play a crucial role in the adaptation process. Furthermore, it would be beneficial to explore the impact of different pre-training objectives and initialization strategies on these other architectures to determine if the optimal settings vary across models. This would provide a more comprehensive understanding of the proposed method's applicability and limitations.

To address the lack of computational cost analysis, the authors should include a detailed breakdown of the resources required for their adaptation method. This should include not only the training time but also the memory footprint and the number of GPUs used. A comparison with the computational costs of training decoder-only models from scratch would be particularly valuable. This analysis should also consider the impact of different batch sizes and sequence lengths on the training time and resource utilization. Furthermore, the authors should discuss the scalability of their method, i.e., how the computational costs scale with model size and dataset size. This would help potential users of their method to assess its feasibility for their specific use cases. It would also be useful to provide an estimate of the time required to achieve a certain level of performance, which would allow for a more direct comparison with other methods.

Finally, the authors should provide a more thorough discussion of the limitations of their approach. This should include an analysis of the types of tasks or model sizes where the adaptation method is less effective. For example, are there specific tasks that are more challenging for the adapted encoder-decoder models? Are there certain model sizes where the adaptation method does not provide significant improvements? A detailed analysis of these limitations would provide a more balanced view of the proposed method and help guide future research in this area. It would also be beneficial to discuss the potential reasons for these limitations, such as the differences in the architectural inductive biases between encoder-decoder and decoder-only models. This would help to identify areas where further improvements are needed and provide a more complete understanding of the proposed method's strengths and weaknesses.

### Questions

See the weakness.

### Rating

6

### Confidence

3

**********

## Reviewer 4

### Summary

This paper explores adapting pretrained decoder-only LLMs to encoder-decoder, with the goal of leveraging the strengths of both approaches to achieve a more favorable quality-efficiency trade-off. The authors propose a method to initialize the parameters of encoder-decoder models from pretrained decoder-only models and then fine-tune them on specific tasks. The study uses the Gemma 2 model series as the testbed and demonstrates that the adapted encoder-decoder LLMs outperform their decoder-only counterparts after instruction tuning. The authors also find that encoder-decoder LLMs achieve better contextual representations, as evaluated on SuperGLUE. The paper contributes to the understanding of how to effectively combine different LLM architectures and provides insights into the potential benefits of encoder-decoder models for various NLP tasks.

### Soundness

3

### Presentation

3

### Contribution

3

### Strengths

- The paper addresses an important problem: improving the quality-efficiency trade-off in LLMs by leveraging the strengths of both encoder-decoder and decoder-only architectures.
- The authors provide a thorough analysis of different pre-training objectives (PrefixLM and UL2) and initialization strategies for encoder-decoder models.
- The paper includes extensive experiments across various benchmarks, including pretraining, instruction-tuning, and SuperGLUE, providing a comprehensive evaluation of the proposed approach.
- The paper is well-written and organized, making it easy to follow the methodology and results.

### Weaknesses

#### Some Related Works


#### comment

 - The paper primarily focuses on adapting the Gemma 2 model series, which limits the generalizability of the findings. It would be beneficial to see how the proposed approach performs on other model architectures, such as LLaMA or QWen.
- The paper does not provide a detailed analysis of the computational costs associated with the proposed adaptation method. It would be helpful to understand the training time and resources required for adapting encoder-decoder models compared to training decoder-only models from scratch.
- The paper could benefit from a more in-depth discussion of the limitations of the proposed approach. For example, are there specific types of tasks or model sizes where the adaptation method is less effective?

### Suggestions

The authors should consider expanding their experimental evaluation to include a wider range of model architectures beyond the Gemma 2 series. Specifically, testing the proposed adaptation method on models like LLaMA or QWen would significantly strengthen the generalizability of their findings. This would involve not only replicating the experiments with these models but also analyzing how the adaptation method performs across different model sizes and pre-training datasets. Such an analysis would reveal whether the observed improvements are consistent across diverse architectures or if specific architectural features of Gemma 2 play a crucial role in the adaptation process. Furthermore, it would be beneficial to explore the impact of different pre-training objectives and initialization strategies on these other architectures to determine if the optimal settings vary across models. This would provide a more comprehensive understanding of the proposed method's applicability and limitations.

To address the lack of computational cost analysis, the authors should include a detailed breakdown of the resources required for their adaptation method. This should include not only the training time but also the memory footprint and the number of GPUs used. A comparison with the computational costs of training decoder-only models from scratch would be particularly valuable. This analysis should also consider the impact of different batch sizes and sequence lengths on the training time and resource utilization. Furthermore, the authors should discuss the scalability of their method, i.e., how the computational costs scale with model size and dataset size. This would help potential users of their method to assess its feasibility for their specific use cases. It would also be useful to provide an estimate of the time required to achieve a certain level of performance, which would allow for a more direct comparison with other methods.

Finally, the authors should provide a more thorough discussion of the limitations of their approach. This should include an analysis of the types of tasks or model sizes where the adaptation method is less effective. For example, are there specific tasks that are more challenging for the adapted encoder-decoder models? Are there certain model sizes where the adaptation method does not provide significant improvements? A detailed analysis of these limitations would provide a more balanced view of the proposed method and help guide future research in this area. It would also be beneficial to discuss the potential reasons for these limitations, such as the differences in the architectural inductive biases between encoder-decoder and decoder-only models. This would help to identify areas where further improvements are needed and provide a more complete understanding of the proposed method's strengths and weaknesses.

### Questions

- How does the proposed adaptation method compare to other approaches for improving the quality-efficiency trade-off in LLMs, such as model pruning or quantization?
- What are the potential benefits and challenges of applying the proposed adaptation method to other encoder-decoder architectures, such as BART or T5?

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
1. Go through each reviewer's identified weaknesses one by one.
2. For each weakness, find relevant sections in the paper (Method, Experiments, Results, Discussion).
3. Extract specific quotes or details from the paper that support the reviewer's claim.
4. If the weakness is about missing information, confirm that the information is indeed absent.
5. If there are conflicting opinions between reviewers, highlight them.
6. Finally, conclude whether the weakness is valid, partially valid, or invalid based on the evidence found.
**Review 1 Weaknesses:**

1. Weakness Statement: The paper primarily focuses on adapting the Gemma 2 model series, which limits the generalizability of the findings. It would be beneficial to see how the proposed approach performs on other model architectures, such as LLaMA or QWen.

2. Evidence Collection:
b) Experiment-related Evidence:
   - The paper explicitly states in the "Model Setting" section: "We use Gemma 2 (2B and 9B) as the base decoder-only LLM. We also pretrain a series of small models (Small, Base, Large, and XL) following mT5 configurations ( Xue et al., 2021 ) under the Gemma 2 framework, and then adapt them to encoder-decoder LLMs."
   - The "Experiments" section details the setup using Gemma 2 models.

3. Literature Gap Analysis:
   - The paper does not include experiments on other model architectures like LLaMA or QWen.

4. Validation Analysis:
   - The paper's experimental setup is solely based on the Gemma 2 model series. The reviewer correctly points out that this limits the generalizability of the findings to other architectures.

5. Conclusion:
   - Validity status: Valid
   - Confidence level: High
   - Key supporting evidence: The paper explicitly states the use of Gemma 2 models for all experiments.

1. Weakness Statement: The paper does not provide a detailed analysis of the computational costs associated with the proposed adaptation method. It would be helpful to understand the training time and resources required for adapting encoder-decoder models compared to training decoder-only models from scratch.

2. Evidence Collection:
b) Experiment-related Evidence:
   - The "Experiments" section mentions the use of "standard hardware configurations" but does not specify the exact hardware or provide detailed training times or resource utilization.
   - The "Discussion" section mentions "additional pretraining compute" but doesn't provide a detailed comparison of computational costs.

3. Literature Gap Analysis:
   - There is no explicit comparison of training time or resource usage between the proposed adaptation method and training decoder-only models from scratch.

4. Validation Analysis:
   - The paper lacks a detailed analysis of the computational costs. While it mentions pretraining compute, it doesn't provide specific training times, hardware details, or a comparison with training from scratch.

5. Conclusion:
   - Validity status: Valid
   - Confidence level: High
   - Key supporting evidence: The paper lacks specific details on training time, hardware, and a direct comparison of computational costs with training from scratch.

1. Weakness Statement: The paper could benefit from a more in-depth discussion of the limitations of the proposed approach. For example, are there specific types of tasks or model sizes where the adaptation method is less effective?

2. Evidence Collection:
   - The "Discussion" section touches upon some limitations, such as the impact of bidirectional attention and the effectiveness of different pretraining objectives.
   - However, it doesn't provide a comprehensive analysis of specific task types or model sizes where the adaptation method might be less effective.

3. Literature Gap Analysis:
   - The paper doesn't explicitly discuss scenarios where the adaptation method might underperform compared to other approaches or the inherent limitations of the method itself.

4. Validation Analysis:
   - While the paper discusses some limitations, it lacks a dedicated and in-depth analysis of specific task types or model sizes where the proposed adaptation method might be less effective.

5. Conclusion:
   - Validity status: Valid
   - Confidence level: High
   - Key supporting evidence: The "Discussion" section mentions some limitations but lacks a comprehensive analysis of specific task or model size effects.

**Review 2 Weaknesses:**

1. Weakness Statement: The paper primarily focuses on adapting the Gemma 2 model series, which limits the generalizability of the findings. It would be beneficial to see how the proposed approach performs on other model architectures, such as LLaMA or QWen.

2. Evidence Collection:
b) Experiment-related Evidence:
   - The paper explicitly states in the "Model Setting" section: "We use Gemma 2 (2B and 9B) as the base decoder-only LLM. We also pretrain a series of small models (Small, Base, Large, and XL) following mT5 configurations ( Xue et al., 2021 ) under the Gemma 2 framework, and then adapt them to encoder-decoder LLMs."
   - The "Experiments" section details the setup using Gemma 2 models.

3. Literature Gap Analysis:
   - The paper does not include experiments on other model architectures like LLaMA or QWen.

4. Validation Analysis:
   - The paper's experimental setup is solely based on the Gemma 2 model series. The reviewer correctly points out that this limits the generalizability of the findings to other architectures.

5. Conclusion:
   - Validity status: Valid
   - Confidence level: High
   - Key supporting evidence: The paper explicitly states the use of Gemma 2 models for all experiments.

1. Weakness Statement: The paper does not provide a detailed analysis of the computational costs associated with the proposed adaptation method. It would be helpful to understand the training time and resources required for adapting encoder-decoder models compared to training decoder-only models from scratch.

2. Evidence Collection:
b) Experiment-related Evidence:
   - The "Experiments" section mentions the use of "standard hardware configurations" but does not specify the exact hardware or provide detailed training times or resource utilization.
   - The "Discussion" section mentions "additional pretraining compute" but doesn't provide a detailed comparison of computational costs.

3. Literature Gap Analysis:
   - There is no explicit comparison of training time or resource usage between the proposed adaptation method and training decoder-only models from scratch.

4. Validation Analysis:
   - The paper lacks a detailed analysis of the computational costs. While it mentions pretraining compute, it doesn't provide specific training times, hardware details, or a comparison with training from scratch.

5. Conclusion:
   - Validity status: Valid
   - Confidence level: High
   - Key supporting evidence: The paper lacks specific details on training time, hardware, and a direct comparison of computational costs with training from scratch.

1. Weakness Statement: The paper could benefit from a more in-depth discussion of the limitations of the proposed approach. For example, are there specific types of tasks or model sizes where the adaptation method is less effective?

2. Evidence Collection:
   - The "Discussion" section touches upon some limitations, such as the impact of bidirectional attention and the effectiveness of different pretraining objectives.
   - However, it doesn't provide a comprehensive analysis of specific task types or model sizes where the adaptation method might be less effective.

3. Literature Gap Analysis:
   - The paper doesn't explicitly discuss scenarios where the adaptation method might underperform compared to other approaches or the inherent limitations of the method itself.

4. Validation Analysis:
   - While the paper discusses some limitations, it lacks a dedicated and in-depth analysis of specific task types or model sizes where the proposed adaptation method might be less effective.

5. Conclusion:
   - Validity status: Valid
   - Confidence level: High
   - Key supporting evidence: The "Discussion" section mentions some limitations but lacks a comprehensive analysis of specific task or model size effects.

**Review 3 Weaknesses:**

1. Weakness Statement: The paper primarily focuses on adapting the Gemma 2 model series, which limits the generalizability of the findings. It would be beneficial to see how the proposed approach performs on other model architectures, such as LLaMA or QWen.

2. Evidence Collection:
b) Experiment-related Evidence:
   - The paper explicitly states in the "Model Setting" section: "We use Gemma 2 (2B and 9B) as the base decoder-only LLM. We also pretrain a series of small models (Small, Base, Large, and XL) following mT5 configurations ( Xue et al., 2021 ) under the Gemma 2 framework, and then adapt them to encoder-decoder LLMs."
   - The "Experiments" section details the setup using Gemma 2 models.

3. Literature Gap Analysis:
   - The paper does not include experiments on other model architectures like LLaMA or QWen.

4. Validation Analysis:
   - The paper's experimental setup is solely based on the Gemma 2 model series. The reviewer correctly points out that this limits the generalizability of the findings to other architectures.

5. Conclusion:
   - Validity status: Valid
   - Confidence level: High
   - Key supporting evidence: The paper explicitly states the use of Gemma 2 models for all experiments.

1. Weakness Statement: The paper does not provide a detailed analysis of the computational costs associated with the proposed adaptation method. It would be helpful to understand the training time and resources required for adapting encoder-decoder models compared to training decoder-only models from scratch.

2. Evidence Collection:
b) Experiment-related Evidence:
   - The "Experiments" section mentions the use of "standard hardware configurations" but does not specify the exact hardware or provide detailed training times or resource utilization.
   - The "Discussion" section mentions "additional pretraining compute" but doesn't provide a detailed comparison of computational costs.

3. Literature Gap Analysis:
   - There is no explicit comparison of training time or resource usage between the proposed adaptation method and training decoder-only models from scratch.

4. Validation Analysis:
   - The paper lacks a detailed analysis of the computational costs. While it mentions pretraining compute, it doesn't provide specific training times, hardware details, or a comparison with training from scratch.

5. Conclusion:
   - Validity status: Valid
   - Confidence level: High
   - Key supporting evidence: The paper lacks specific details on training time, hardware, and a direct comparison of computational costs with training from scratch.

1. Weakness Statement: The paper could benefit from a more in-depth discussion of the limitations of the proposed approach. For example, are there specific types of tasks or model sizes where the adaptation method is less effective?

2. Evidence Collection:
   - The "Discussion" section touches upon some limitations, such as the impact of bidirectional attention and the effectiveness of different pretraining objectives.
   - However, it doesn't provide a comprehensive analysis of specific task types or model sizes where the adaptation method might be less effective.

3. Literature Gap Analysis:
   - The paper doesn't explicitly discuss scenarios where the adaptation method might underperform compared to other approaches or the inherent limitations of the method itself.

4. Validation Analysis:
   - While the paper discusses some limitations, it lacks a dedicated and in-depth analysis of specific task types or model sizes where the proposed adaptation method might be less effective.

5. Conclusion:
   - Validity status: Valid
   - Confidence level: High
   - Key supporting evidence: The "Discussion" section mentions some limitations but lacks a comprehensive analysis of specific task or model size effects.

**Review 4 Weaknesses:**

1. Weakness Statement: The paper primarily focuses on adapting the Gemma 2 model series, which limits the generalizability of the findings. It would be beneficial to see how the proposed approach performs on other model architectures, such as LLaMA or QWen.

2. Evidence Collection:
b) Experiment-related Evidence:
   - The paper explicitly states in the "Model Setting" section: "We use Gemma 2 (2B and 9B) as the base decoder-only LLM. We also pretrain a series of small models (Small, Base, Large, and XL) following mT5 configurations ( Xue et al., 2021 ) under the Gemma 2 framework, and then adapt them to encoder-decoder LLMs."
   - The "Experiments" section details the setup using Gemma 2 models.

3. Literature Gap Analysis:
   - The paper does not include experiments on other model architectures like LLaMA or QWen.

4. Validation Analysis:
   - The paper's experimental setup is solely based on the Gemma 2 model series. The reviewer correctly points out that this limits the generalizability of the findings to other architectures.

5. Conclusion:
   - Validity status: Valid
   - Confidence level: High
   - Key supporting evidence: The paper explicitly states the use of Gemma 2 models for all experiments.

1. Weakness Statement: The paper does not provide a detailed analysis of the computational costs associated with the proposed adaptation method. It would be helpful to understand the training time and resources required for adapting encoder-decoder models compared to training decoder-only models from scratch.

2. Evidence Collection:
b) Experiment-related Evidence:
   - The "Experiments" section mentions the use of "standard hardware configurations" but does not specify the exact hardware or provide detailed training times or resource utilization.
   - The "Discussion" section mentions "additional pretraining compute" but doesn't provide a detailed comparison of computational costs.

3. Literature Gap Analysis:
   - There is no explicit comparison of training time or resource usage between the proposed adaptation method and training decoder-only models from scratch.

4. Validation Analysis:
   - The paper lacks a detailed analysis of the computational costs. While it mentions pretraining compute, it doesn't provide specific training times, hardware details, or a comparison with training from scratch.

5. Conclusion:
   - Validity status: Valid
   - Confidence level: High
   - Key supporting evidence: The paper lacks specific details on training time, hardware, and a direct comparison of computational costs with training from scratch.

1. Weakness Statement: The paper could benefit from a more in-depth discussion of the limitations of the proposed approach. For example, are there specific types of tasks or model sizes where the adaptation method is less effective?

2. Evidence Collection:
   - The "Discussion" section touches upon some limitations, such as the impact of bidirectional attention and the effectiveness of different pretraining objectives.
   - However, it doesn't provide a comprehensive analysis of specific task types or model sizes where the adaptation method might be less effective.

3. Literature Gap Analysis:
   - The paper doesn't explicitly discuss scenarios where the adaptation method might underperform compared to other approaches or the inherent limitations of the method itself.

4. Validation Analysis:
   - While the paper discusses some limitations, it lacks a dedicated and in-depth analysis of specific task types or model sizes where the proposed adaptation method might be less effective.

5. Conclusion:
   - Validity status: Valid
   - Confidence level: High
   - Key supporting evidence: The "Discussion" section mentions some limitations but lacks a comprehensive analysis of specific task or model size effects.
}

Now, I have successfully verified each review. Next, I will organize this content and output the final review decision:

\boxed_review{
## Summary:

This paper introduces a novel approach to adapting pre-trained decoder-only Large Language Models (LLMs) into encoder-decoder architectures, aiming to leverage the strengths of both types of models. The core idea revolves around initializing the encoder-decoder models with parameters derived from pre-trained decoder-only models, specifically the Gemma 2 series. This initialization is followed by fine-tuning on various tasks, including pre-training, instruction tuning, and the SuperGLUE benchmark. The authors explore two primary pre-training objectives: PrefixLM and UL2, investigating their impact on the performance of the adapted encoder-decoder models. The methodology involves a series of models with varying parameter counts, ranging from 2 billion to 9 billion parameters, allowing for a comprehensive evaluation of the proposed adaptation method across different scales. The main empirical finding is that the adapted encoder-decoder models consistently outperform their decoder-only counterparts after instruction tuning. This suggests that the integration of an encoder, even when initialized from a decoder-only model, leads to improved performance in downstream tasks. Furthermore, the authors demonstrate that encoder-decoder models achieve better contextual representations, as evaluated on the SuperGLUE benchmark, indicating that the bidirectional attention mechanism enhances their ability to understand and process complex textual information. The overall significance of this work lies in its contribution to the understanding of how to effectively combine different LLM architectures. By demonstrating that encoder-decoder models can be successfully adapted from decoder-only models, the paper opens up new avenues for research into hybrid architectures and their potential benefits. The findings suggest that encoder-decoder models, when properly adapted, can offer a more favorable quality-efficiency trade-off compared to traditional decoder-only models, making them more suitable for a wide range of applications. The paper's exploration of different pre-training objectives and initialization strategies also provides valuable insights into the factors that influence the performance of encoder-decoder models. While the study is primarily focused on the Gemma 2 series, the underlying principles and methodologies could potentially be extended to other LLM architectures, further broadening the impact of this research. The authors' work provides a solid foundation for future investigations into the adaptation and optimization of hybrid LLM architectures, paving the way for more efficient and effective natural language processing systems.


## Soundness:

3.0


## Presentation:

3.0


## Contribution:

2.5


## Strengths:

This paper presents several notable strengths that contribute to its overall value and impact. First and foremost, the paper addresses a significant and timely problem: the exploration of encoder-decoder architectures for LLMs. By focusing on the adaptation of pre-trained decoder-only models to encoder-decoder architectures, the authors tackle the challenge of leveraging the strengths of both approaches. This is a crucial area of research, as it seeks to overcome the limitations of traditional decoder-only models and potentially unlock new avenues for improving the quality and efficiency of NLP systems. The paper's methodological approach is another key strength. The authors propose a clear and well-defined method for adapting decoder-only models to encoder-decoder architectures. The use of initialization strategies derived from pre-trained decoder-only models, such as Gemma 2, is a logical and effective way to transfer knowledge from one architecture to another. The exploration of different pre-training objectives, specifically PrefixLM and UL2, is also commendable. By comparing the performance of models trained with these different objectives, the authors provide valuable insights into the factors that influence the effectiveness of encoder-decoder models. The empirical evaluation is comprehensive and well-executed. The authors conduct extensive experiments across various benchmarks, including pre-training, instruction tuning, and SuperGLUE. This thorough evaluation provides a robust assessment of the proposed adaptation method and its impact on model performance. The inclusion of SuperGLUE evaluations is particularly valuable, as it allows for a direct comparison of contextual representation capabilities between encoder-decoder and decoder-only models. The paper's findings are significant and well-supported by the experimental results. The consistent outperformance of adapted encoder-decoder models over their decoder-only counterparts after instruction tuning is a notable achievement. This demonstrates the effectiveness of the proposed adaptation method and its potential to improve the performance of LLMs. Furthermore, the finding that encoder-decoder models achieve better contextual representations, as evaluated on SuperGLUE, provides further evidence of their potential. The paper is also well-written and organized, making it easy to follow the methodology and results. The authors clearly articulate their research questions, describe their approach, and present their findings in a logical and coherent manner. The use of tables and figures effectively illustrates the experimental results and facilitates a better understanding of the paper's contributions. Overall, the paper's strengths lie in its clear problem definition, well-defined methodology, comprehensive empirical evaluation, and significant findings. These strengths make it a valuable contribution to the field of LLM research and provide a solid foundation for future investigations into hybrid architectures.


## Weaknesses:

Despite its strengths, this paper exhibits several notable weaknesses that warrant careful consideration. The most significant limitation, and one that is consistently highlighted across multiple reviews, is the narrow focus on the Gemma 2 model series. As explicitly stated in the "Model Setting" section, the authors exclusively use Gemma 2 models (2B and 9B parameters) as the base decoder-only LLM for all their experiments. This choice limits the generalizability of the findings to other model architectures. It remains unclear whether the observed improvements from adapting to encoder-decoder architectures would hold for other popular LLM families, such as LLaMA or QWen. This lack of diversity in the experimental setup raises concerns about whether the findings are specific to the Gemma 2 architecture or represent a more generalizable phenomenon. The absence of experiments on other architectures makes it difficult to assess the robustness of the proposed adaptation method and its potential applicability across different model types. This is a high-confidence concern, as the paper explicitly states its reliance on Gemma 2, and the lack of alternative models is a clear gap in the experimental design. Another significant weakness is the lack of a detailed analysis of the computational costs associated with the proposed adaptation method. While the "Experiments" section mentions using "standard hardware configurations," it fails to provide specific details about the hardware used, such as the type and number of GPUs, or the memory footprint. Furthermore, the paper does not include a comparison of the training time and resource utilization between the proposed adaptation method and training decoder-only models from scratch. This omission makes it difficult to assess the practical feasibility of the method, especially when considering the computational demands of large-scale LLM training. The absence of a direct comparison of computational costs is a high-confidence concern, as it directly impacts the practicality of the proposed method. The paper also lacks a comprehensive discussion of the limitations of the proposed approach. While the "Discussion" section touches upon some limitations, such as the impact of bidirectional attention and the effectiveness of different pretraining objectives, it does not provide a detailed analysis of specific task types or model sizes where the adaptation method might be less effective. For instance, the paper does not explore whether the adaptation method performs differently on tasks that require specific types of reasoning or understanding. It also does not investigate whether the adaptation method is more or less effective for certain model sizes within the Gemma 2 series. This lack of a thorough analysis of limitations is a high-confidence concern, as it prevents a balanced understanding of the method's strengths and weaknesses. The paper's analysis of the impact of bidirectional attention is also limited. While the "Discussion" section mentions that bidirectional attention contributes to the performance gains, it does not provide a detailed explanation of the underlying mechanisms. The paper does not explore whether the gains are primarily due to the increased context window or other architectural factors. This lack of a deeper analysis of the impact of bidirectional attention is a medium-confidence concern, as it leaves open questions about the specific reasons for the observed performance improvements. Finally, the paper does not provide a detailed analysis of the computational costs associated with the proposed adaptation method. While the "Discussion" section mentions "additional pretraining compute," it does not provide a detailed comparison of computational costs with training from scratch. This omission makes it difficult to assess the practical feasibility of the method, especially when considering the computational demands of large-scale LLM training. The absence of a direct comparison of computational costs is a high-confidence concern, as it directly impacts the practicality of the proposed method. In summary, the paper's limitations stem from its narrow focus on a single model architecture, the lack of detailed computational cost analysis, and the limited discussion of the method's limitations. These weaknesses, while not invalidating the findings, do raise questions about the generalizability and practical applicability of the proposed approach. The confidence level in these identified issues is generally high, as they are based on direct observations of the paper's content and a lack of specific information in the relevant sections.


## Suggestions:

To address the identified weaknesses and further strengthen the paper, I would suggest several concrete and actionable improvements. First and foremost, the authors should significantly expand their experimental evaluation to include a wider range of model architectures beyond the Gemma 2 series. Specifically, testing the proposed adaptation method on models like LLaMA or QWen would substantially enhance the generalizability of the findings. This would involve not only replicating the experiments with these new models but also analyzing how the adaptation method performs across different model sizes and pre-training datasets. Such an analysis would reveal whether the observed improvements are consistent across diverse architectures or if specific architectural features of Gemma 2 play a crucial role in the adaptation process. Furthermore, it would be beneficial to explore the impact of different pre-training objectives and initialization strategies on these other architectures to determine if the optimal settings vary across models. This would provide a more comprehensive understanding of the proposed method's applicability and limitations. Second, the authors should include a detailed breakdown of the resources required for their adaptation method. This should include not only the training time but also the memory footprint and the number of GPUs used. A comparison with the computational costs of training decoder-only models from scratch would be particularly valuable. This analysis should also consider the impact of different batch sizes and sequence lengths on the training time and resource utilization. Furthermore, the authors should discuss the scalability of their method, i.e., how the computational costs scale with model size and dataset size. This would help potential users of their method to assess its feasibility for their specific use cases. It would also be useful to provide an estimate of the time required to achieve a certain level of performance, which would allow for a more direct comparison with other methods. Third, the authors should provide a more thorough discussion of the limitations of their approach. This should include an analysis of the types of tasks or model sizes where the adaptation method is less effective. For example, are there specific tasks that are more challenging for the adapted encoder-decoder models? Are there certain model sizes where the adaptation method does not provide significant improvements? A detailed analysis of these limitations would provide a more balanced view of the proposed method and help guide future research in this area. It would also be beneficial to discuss the potential reasons for these limitations, such as the differences in the architectural inductive biases between encoder-decoder and decoder-only models. This would help to identify areas where further improvements are needed and provide a more complete understanding of the proposed method's strengths and weaknesses. Fourth, the authors should delve deeper into the analysis of the impact of bidirectional attention. This could involve a more detailed investigation of how the increased context window affects the model's ability to capture long-range dependencies and how this relates to the observed performance gains. It would also be beneficial to compare the performance of the adapted encoder-decoder models with decoder-only models of similar size and training data to determine if the gains are primarily due to the increased context window or other architectural factors. Finally, the authors should provide a more detailed comparison of the computational costs of their adaptation method with the costs of training decoder-only models from scratch. This comparison should include a breakdown of the resources required for different stages of the adaptation process, such as pre-training, fine-tuning, and evaluation. This would help potential users of their method to assess its feasibility for their specific use cases. By addressing these points, the authors can significantly strengthen their paper and provide a more comprehensive and robust analysis of their proposed method.


## Questions:

Several key questions arise from my analysis of this paper, primarily focusing on the methodological choices and the scope of the experimental evaluation. First, how does the proposed adaptation method compare to other approaches for improving the quality-efficiency trade-off in LLMs, such as model pruning or quantization? A comparative analysis with these alternative methods would provide valuable context and help to position the proposed approach within the broader landscape of LLM optimization techniques. Specifically, I am interested in understanding the relative advantages and disadvantages of the adaptation method compared to these other techniques in terms of computational cost, performance gains, and ease of implementation. Second, what are the potential benefits and challenges of applying the proposed adaptation method to other encoder-decoder architectures, such as BART or T5? While the paper focuses on variations of the Gemma 2 model, exploring the applicability of the method to other established architectures would further validate its generalizability. This would involve not only replicating the experiments with these new architectures but also analyzing how the adaptation method performs across different pre-training objectives and initialization strategies. I am particularly interested in understanding whether the optimal settings for the adaptation method vary across different architectures and what factors influence these variations. Third, regarding the computational costs, could the authors provide a more detailed breakdown of the resources required for their adaptation method, including the training time, memory footprint, and the number of GPUs used? A comparison with the computational costs of training decoder-only models from scratch would be particularly valuable. This analysis should also consider the impact of different batch sizes and sequence lengths on the training time and resource utilization. Furthermore, I am interested in understanding how the computational costs scale with model size and dataset size. Fourth, concerning the limitations of the proposed approach, are there specific types of tasks or model sizes where the adaptation method is less effective? For example, are there specific tasks that are more challenging for the adapted encoder-decoder models? Are there certain model sizes where the adaptation method does not provide significant improvements? A detailed analysis of these limitations would provide a more balanced view of the proposed method and help to identify areas where further improvements are needed. Finally, regarding the impact of bidirectional attention, what is the underlying mechanism that explains the performance gains observed with encoder-decoder models? Is the improvement primarily due to the increased context window, or are there other architectural factors at play? A deeper analysis of this aspect would provide a more complete understanding of the benefits of the proposed method. These questions are intended to encourage further exploration of the proposed method's strengths, limitations, and potential for broader application.


## Rating:

6.5


## Confidence:

3.0


## Decision:

Accept
}