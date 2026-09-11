I will use Standard Mode for comprehensive thinking. As a professional reviewer, I will simulate 4 different reviewers, followed by the verification thinking. Then I will output the Finally Review Output. Let me think - Standard Mode means I will output the original review, followed by the verification thinking. Considering that I am currently in standard mode, I should think from my existing knowledge and consider some related work content when writing about weaknesses. Then I will output the Finally Review Output and Meta Review Output:

\boxed_simreviewers{
## Reviewer 1

### Summary

This paper introduces T5Gemma 2, a new family of lightweight open encoder-decoder models that supports multimodal, long-context capabilities. The authors adapt the Gemma 3 models into an encoder-decoder setup and propose two methods to improve the efficiency: tied word embedding and merged attention. The authors also use positional interpolation methods to extend the context length. T5Gemma 2 demonstrates competitive pretraining performance and improved post-training performance compared to its Gemma 3 counterpart.

### Soundness

2

### Presentation

2

### Contribution

2

### Strengths

- Tied word embedding and merged attention are proposed to improve the efficiency of the encoder-decoder architecture.
- The model demonstrates competitive pretraining performance and improved post-training performance compared to its Gemma 3 counterpart.

### Weaknesses

#### Some Related Works


#### comment

 - The novelty of this paper is limited. The tied word embedding and merged attention are proposed to improve the efficiency of the encoder-decoder architecture. However, these techniques have been widely used in other multimodal LLMs, such as LLaVA and MiniGPT-4. The paper does not sufficiently articulate the specific novel contributions beyond these existing techniques, particularly in the context of encoder-decoder architectures. The application of these techniques to T5Gemma, while potentially beneficial, lacks a clear justification for why these specific methods were chosen over other potential efficiency improvements.
- The paper does not provide a detailed analysis of the performance of the model on different types of tasks, such as text-only, image-only, and multimodal tasks. The evaluation is not granular enough to understand the specific strengths and weaknesses of the proposed model. For example, it is unclear how the model performs on tasks that require complex reasoning or those that are more visually oriented. This lack of detailed analysis makes it difficult to assess the true capabilities of T5Gemma 2.
- The paper does not provide a detailed analysis of the computational cost of the proposed methods. While the paper mentions efficiency improvements, it does not provide concrete metrics such as FLOPs or parameter counts to support these claims. A more thorough analysis of the computational overhead of the proposed methods is needed to fully assess their practical implications.

### Suggestions

The paper would benefit from a more in-depth analysis of the specific contributions of T5Gemma 2, particularly in comparison to existing multimodal models. While the paper mentions the use of tied word embeddings and merged attention, it does not provide a detailed explanation of how these techniques are implemented within the encoder-decoder architecture of T5Gemma 2. A more thorough explanation of the architectural modifications and their impact on performance would be beneficial. Furthermore, the paper should include a more detailed comparison of T5Gemma 2 with other state-of-the-art multimodal models, highlighting the unique aspects of the proposed approach. This comparison should not only focus on overall performance but also on the specific strengths and weaknesses of each model on different types of tasks. For example, a comparison of the model's performance on tasks that require complex reasoning versus those that are more visually oriented would provide valuable insights into the model's capabilities.

To address the lack of detailed performance analysis, the paper should include a more granular evaluation of T5Gemma 2 on a variety of tasks. This evaluation should include not only overall performance metrics but also task-specific analysis. For example, the paper could include a breakdown of performance on text-only tasks, image-only tasks, and multimodal tasks. This would allow for a more detailed understanding of the model's strengths and weaknesses. Furthermore, the paper should include an analysis of the model's performance on tasks that require different types of reasoning, such as logical reasoning, spatial reasoning, and visual reasoning. This would provide a more comprehensive assessment of the model's capabilities. The paper should also include an analysis of the model's performance on tasks that are known to be challenging for multimodal models, such as tasks that require understanding of complex visual scenes or tasks that require reasoning about abstract concepts.

Finally, the paper should include a more detailed analysis of the computational cost of the proposed methods. This analysis should include concrete metrics such as FLOPs, parameter counts, and training time. The paper should also compare the computational cost of T5Gemma 2 with other state-of-the-art multimodal models. This analysis would provide a more complete picture of the practical implications of the proposed approach. The paper should also discuss the trade-offs between performance and computational cost, and provide guidance on how to choose the appropriate model for different applications. This would make the paper more useful for researchers and practitioners who are interested in using T5Gemma 2 for their own work.

### Questions

- How does T5Gemma 2 compare to other state-of-the-art multimodal models in terms of performance and efficiency?
- What are the specific advantages of T5Gemma 2 over other multimodal models, such as LLaVA and MiniGPT-4?

### Rating

5

### Confidence

3

**********

## Reviewer 2

### Summary

This paper proposes T5Gemma 2, a new family of lightweight open encoder-decoder models that supports multimodal, long-context capabilities. The authors adapt the Gemma 3 models into an encoder-decoder setup and propose two methods to improve the efficiency: tied word embedding and merged attention. The authors also use positional interpolation methods to extend the context length. T5Gemma 2 demonstrates competitive pretraining performance and improved post-training performance compared to its Gemma 3 counterpart.

### Soundness

2

### Presentation

3

### Contribution

2

### Strengths

1. The paper is well-written and easy to follow.
2. The authors provide a comprehensive evaluation of T5Gemma 2 on a wide range of benchmarks, including reasoning and factuality, stem and coding, multilingual, multimodal and long-context.

### Weaknesses

#### Some Related Works


#### comment

1. The novelty of this paper is limited. The tied word embedding and merged attention are proposed to improve the efficiency of the encoder-decoder architecture. However, these techniques have been widely used in other multimodal LLMs, such as LLaVA and MiniGPT-4. The paper does not sufficiently articulate the specific novel contributions beyond these existing techniques, particularly in the context of encoder-decoder architectures. The application of these techniques to T5Gemma, while potentially beneficial, lacks a clear justification for why these specific methods were chosen over other potential efficiency improvements.
2. The paper does not provide a detailed analysis of the performance of the model on different types of tasks, such as text-only, image-only, and multimodal tasks. The evaluation is not granular enough to understand the specific strengths and weaknesses of the proposed model. For example, it is unclear how the model performs on tasks that require complex reasoning or those that are more visually oriented. This lack of detailed analysis makes it difficult to assess the true capabilities of T5Gemma 2.
3. The paper does not provide a detailed analysis of the computational cost of the proposed methods. While the paper mentions efficiency improvements, it does not provide concrete metrics such as FLOPs or parameter counts to support these claims. A more thorough analysis of the computational overhead of the proposed methods is needed to fully assess their practical implications.

### Suggestions

The paper would benefit from a more in-depth analysis of the specific contributions of T5Gemma 2, particularly in comparison to existing multimodal models. While the paper mentions the use of tied word embeddings and merged attention, it does not provide a detailed explanation of how these techniques are implemented within the encoder-decoder architecture of T5Gemma 2. A more thorough explanation of the architectural modifications and their impact on performance would be beneficial. Furthermore, the paper should include a more detailed comparison of T5Gemma 2 with other state-of-the-art multimodal models, highlighting the unique aspects of the proposed approach. This comparison should not only focus on overall performance but also on the specific strengths and weaknesses of each model on different types of tasks. For example, a comparison of the model's performance on tasks that require complex reasoning versus those that are more visually oriented would provide valuable insights into the model's capabilities.

To address the lack of detailed performance analysis, the paper should include a more granular evaluation of T5Gemma 2 on a variety of tasks. This evaluation should include not only overall performance metrics but also task-specific analysis. For example, the paper could include a breakdown of performance on text-only tasks, image-only tasks, and multimodal tasks. This would allow for a more detailed understanding of the model's strengths and weaknesses. Furthermore, the paper should include an analysis of the model's performance on tasks that require different types of reasoning, such as logical reasoning, spatial reasoning, and visual reasoning. This would provide a more comprehensive assessment of the model's capabilities. The paper should also include an analysis of the model's performance on tasks that are known to be challenging for multimodal models, such as tasks that require understanding of complex visual scenes or tasks that require reasoning about abstract concepts.

Finally, the paper should include a more detailed analysis of the computational cost of the proposed methods. This analysis should include concrete metrics such as FLOPs, parameter counts, and training time. The paper should also compare the computational cost of T5Gemma 2 with other state-of-the-art multimodal models. This analysis would provide a more complete picture of the practical implications of the proposed approach. The paper should also discuss the trade-offs between performance and computational cost, and provide guidance on how to choose the appropriate model for different applications. This would make the paper more useful for researchers and practitioners who are interested in using T5Gemma 2 for their own work.

### Questions

See the weaknesses.

### Rating

5

### Confidence

3

**********

## Reviewer 3

### Summary

This paper presents T5Gemma 2, a family of encoder-decoder models that support multimodal and long-context capabilities. T5Gemma 2 follows the adaptation recipe from T5Gemma, in which pretrained decoder-only models are adapted into encoder-decoder models. The authors propose two methods to improve the efficiency of the encoder-decoder architecture: tied word embedding and merged attention. The authors also use positional interpolation methods to extend the context length. T5Gemma 2 demonstrates competitive pretraining performance and improved post-training performance compared to its Gemma 3 counterpart.

### Soundness

3

### Presentation

3

### Contribution

2

### Strengths

1. The paper is well-written and easy to follow.
2. The authors provide a comprehensive evaluation of T5Gemma 2 on a wide range of benchmarks, including reasoning and factuality, stem and coding, multilingual, multimodal and long-context.

### Weaknesses

#### Some Related Works


#### comment

1. The novelty of this paper is limited. The tied word embedding and merged attention are proposed to improve the efficiency of the encoder-decoder architecture. However, these techniques have been widely used in other multimodal LLMs, such as LLaVA and MiniGPT-4. The paper does not sufficiently articulate the specific novel contributions beyond these existing techniques, particularly in the context of encoder-decoder architectures. The application of these techniques to T5Gemma, while potentially beneficial, lacks a clear justification for why these specific methods were chosen over other potential efficiency improvements.
2. The paper does not provide a detailed analysis of the performance of the model on different types of tasks, such as text-only, image-only, and multimodal tasks. The evaluation is not granular enough to understand the specific strengths and weaknesses of the proposed model. For example, it is unclear how the model performs on tasks that require complex reasoning or those that are more visually oriented. This lack of detailed analysis makes it difficult to assess the true capabilities of T5Gemma 2.
3. The paper does not provide a detailed analysis of the computational cost of the proposed methods. While the paper mentions efficiency improvements, it does not provide concrete metrics such as FLOPs or parameter counts to support these claims. A more thorough analysis of the computational overhead of the proposed methods is needed to fully assess their practical implications.

### Suggestions

The paper would benefit from a more in-depth analysis of the specific contributions of T5Gemma 2, particularly in comparison to existing multimodal models. While the paper mentions the use of tied word embeddings and merged attention, it does not provide a detailed explanation of how these techniques are implemented within the encoder-decoder architecture of T5Gemma 2. A more thorough explanation of the architectural modifications and their impact on performance would be beneficial. Furthermore, the paper should include a more detailed comparison of T5Gemma 2 with other state-of-the-art multimodal models, highlighting the unique aspects of the proposed approach. This comparison should not only focus on overall performance but also on the specific strengths and weaknesses of each model on different types of tasks. For example, a comparison of the model's performance on tasks that require complex reasoning versus those that are more visually oriented would provide valuable insights into the model's capabilities.

To address the lack of detailed performance analysis, the paper should include a more granular evaluation of T5Gemma 2 on a variety of tasks. This evaluation should include not only overall performance metrics but also task-specific analysis. For example, the paper could include a breakdown of performance on text-only tasks, image-only tasks, and multimodal tasks. This would allow for a more detailed understanding of the model's strengths and weaknesses. Furthermore, the paper should include an analysis of the model's performance on tasks that require different types of reasoning, such as logical reasoning, spatial reasoning, and visual reasoning. This would provide a more comprehensive assessment of the model's capabilities. The paper should also include an analysis of the model's performance on tasks that are known to be challenging for multimodal models, such as tasks that require understanding of complex visual scenes or tasks that require reasoning about abstract concepts.

Finally, the paper should include a more detailed analysis of the computational cost of the proposed methods. This analysis should include concrete metrics such as FLOPs, parameter counts, and training time. The paper should also compare the computational cost of T5Gemma 2 with other state-of-the-art multimodal models. This analysis would provide a more complete picture of the practical implications of the proposed approach. The paper should also discuss the trade-offs between performance and computational cost, and provide guidance on how to choose the appropriate model for different applications. This would make the paper more useful for researchers and practitioners who are interested in using T5Gemma 2 for their own work.

### Questions

Please see the weaknesses.

### Rating

5

### Confidence

3

**********

## Reviewer 4

### Summary

This paper presents T5Gemma 2, a new family of lightweight open encoder-decoder models that support multimodal, long-context capabilities. T5Gemma 2 follows the adaptation recipe from T5Gemma (Zhang et al., 2025b), in which pretrained decoder-only models are adapted into encoder-decoder models. The authors propose two methods to improve the efficiency: tied word embedding and merged attention. The authors also use positional interpolation methods to extend the context length. T5Gemma 2 demonstrates competitive pretraining performance and improved post-training performance than its Gemma 3 counterpart.

### Soundness

3

### Presentation

3

### Contribution

2

### Strengths

1. The paper is well-written and easy to follow.
2. The authors provide a comprehensive evaluation of T5Gemma 2 on a wide range of benchmarks, including reasoning and factuality, stem and coding, multilingual, multimodal and long-context.

### Weaknesses

#### Some Related Works


#### comment

1. The novelty of this paper is limited. The tied word embedding and merged attention are proposed to improve the efficiency of the encoder-decoder architecture. However, these techniques have been widely used in other multimodal LLMs, such as LLaVA and MiniGPT-4. The paper does not sufficiently articulate the specific novel contributions beyond these existing techniques, particularly in the context of encoder-decoder architectures. The application of these techniques to T5Gemma, while potentially beneficial, lacks a clear justification for why these specific methods were chosen over other potential efficiency improvements.
2. The paper does not provide a detailed analysis of the performance of the model on different types of tasks, such as text-only, image-only, and multimodal tasks. The evaluation is not granular enough to understand the specific strengths and weaknesses of the proposed model. For example, it is unclear how the model performs on tasks that require complex reasoning or those that are more visually oriented. This lack of detailed analysis makes it difficult to assess the true capabilities of T5Gemma 2.
3. The paper does not provide a detailed analysis of the computational cost of the proposed methods. While the paper mentions efficiency improvements, it does not provide concrete metrics such as FLOPs or parameter counts to support these claims. A more thorough analysis of the computational overhead of the proposed methods is needed to fully assess their practical implications.

### Suggestions

The paper would benefit from a more in-depth analysis of the specific contributions of T5Gemma 2, particularly in comparison to existing multimodal models. While the paper mentions the use of tied word embeddings and merged attention, it does not provide a detailed explanation of how these techniques are implemented within the encoder-decoder architecture of T5Gemma 2. A more thorough explanation of the architectural modifications and their impact on performance would be beneficial. Furthermore, the paper should include a more detailed comparison of T5Gemma 2 with other state-of-the-art multimodal models, highlighting the unique aspects of the proposed approach. This comparison should not only focus on overall performance but also on the specific strengths and weaknesses of each model on different types of tasks. For example, a comparison of the model's performance on tasks that require complex reasoning versus those that are more visually oriented would provide valuable insights into the model's capabilities.

To address the lack of detailed performance analysis, the paper should include a more granular evaluation of T5Gemma 2 on a variety of tasks. This evaluation should include not only overall performance metrics but also task-specific analysis. For example, the paper could include a breakdown of performance on text-only tasks, image-only tasks, and multimodal tasks. This would allow for a more detailed understanding of the model's strengths and weaknesses. Furthermore, the paper should include an analysis of the model's performance on tasks that require different types of reasoning, such as logical reasoning, spatial reasoning, and visual reasoning. This would provide a more comprehensive assessment of the model's capabilities. The paper should also include an analysis of the model's performance on tasks that are known to be challenging for multimodal models, such as tasks that require understanding of complex visual scenes or tasks that require reasoning about abstract concepts.

Finally, the paper should include a more detailed analysis of the computational cost of the proposed methods. This analysis should include concrete metrics such as FLOPs, parameter counts, and training time. The paper should also compare the computational cost of T5Gemma 2 with other state-of-the-art multimodal models. This analysis would provide a more complete picture of the practical implications of the proposed approach. The paper should also discuss the trade-offs between performance and computational cost, and provide guidance on how to choose the appropriate model for different applications. This would make the paper more useful for researchers and practitioners who are interested in using T5Gemma 2 for their own work.

### Questions

1. What is the specific motivation for choosing tied word embedding and merged attention? How do these techniques specifically benefit the encoder-decoder architecture of T5Gemma 2?
2. How does T5Gemma 2 compare to other multimodal models in terms of performance and efficiency? What are the specific advantages of T5Gemma 2 over these models?
3. What are the specific challenges in adapting the Gemma 3 models into an encoder-decoder setup, and how does T5Gemma 2 address these challenges?

### Rating

5

### Confidence

3

**********

}

I have finished generating simulated reviews from 4 reviewers. Next, I will generate verification content for these reviews:

\boxed_verification{
The user wants me to validate weaknesses identified by reviewers for the T5Gemma 2 paper. I need to go through each reviewer's comments and find evidence in the paper to support or refute their claims.

**Plan:**
1. Go through each reviewer's comments one by one.
2. For each weakness identified by the reviewer, find the relevant section in the paper.
3. Extract evidence (quotes, experimental details, missing citations) from the paper to support the weakness.
4. If the weakness is about missing information, check if that information is indeed absent.
5. If the weakness is about a lack of justification, check if the paper provides any reasoning.
6. Synthesize the findings and conclude whether the weakness is valid, partially valid, or invalid.
**Review 1 Weaknesses:**

1. Weakness Statement:
"The novelty of this paper is limited. The tied word embedding and merged attention are proposed to improve the efficiency of the encoder-decoder architecture. However, these techniques have been widely used in other multimodal LLMs, such as LLaVA and MiniGPT-4. The paper does not sufficiently articulate the specific novel contributions beyond these existing techniques, particularly in the context of encoder-decoder architectures. The application of these techniques to T5Gemma, while potentially beneficial, lacks a clear justification for why these specific methods were chosen over other potential efficiency improvements."

2. Evidence Collection:
a) Method-related Evidence:
   - The paper introduces "tied word embedding" in the "Tied Word Embedding" component description: "Tied word embedding is a technique where all word embeddings across the encoder and decoder are shared. This reduces the number of model parameters, thereby decreasing model size and computational cost."
   - The paper introduces "merged attention" in the "Merged Attention" component description: "Merged attention is a technique that unifies the decoder self-attention and cross-attention into a single joint module. This reduces the number of parameters and computational cost, making the model more efficient."
   - The "Introduction" section mentions the inspiration from UL2: "We further extend the recipe from the text-only realm to multimodal and long-context based on the powerful Gemma 3 models ( Team et al., 2025a ). For vision modeling, T5Gemma 2 reuses the same vision encoder from Gemma 3 and keeps it frozen; vision tokens are always fed to the encoder and all encoder tokens always have full visibility to each other in the self attention. For long-context modeling, we adopt the positional interpolation methods ( Chen et al., 2023 ; Team et al., 2025a ) ."
   - The "Related Work" section does not explicitly discuss the novelty of tied word embeddings or merged attention in the context of encoder-decoder architectures.

3. Literature Gap Analysis:
   - The paper does not cite specific works that introduced tied word embeddings or merged attention in encoder-decoder architectures, particularly in the context of multimodal models.

4. Validation Analysis:
   - The reviewer correctly points out that tied word embeddings and merged attention are not novel concepts in the broader field of deep learning, especially in the context of encoder-decoder models and even multimodal models like LLaVA and MiniGPT-4. The paper focuses on applying these techniques to the specific T5Gemma 2 architecture and demonstrating its effectiveness. However, it doesn't explicitly highlight the novelty of *their* application or the specific challenges they address with these techniques in this context. The justification for choosing these specific methods is primarily based on the general benefit of efficiency, without a detailed comparison to other potential efficiency improvements.

5. Conclusion:
   - Validity status: Valid
   - Confidence level: High
   - Key supporting evidence: The paper describes tied word embedding and merged attention as techniques to improve efficiency without explicitly addressing their novelty in the context of encoder-decoder architectures or comparing them to other efficiency-focused techniques.

1. Weakness Statement:
"The paper does not provide a detailed analysis of the performance of the model on different types of tasks, such as text-only, image-only, and multimodal tasks. The evaluation is not granular enough to understand the specific strengths and weaknesses of the proposed model. For example, it is unclear how the model performs on tasks that require complex reasoning or those that are more visually oriented. This lack of detailed analysis makes it difficult to assess the true capabilities of T5Gemma 2."

2. Evidence Collection:
b) Experiment-related Evidence:
   - The "Experiments" section includes evaluations on "Reasoning and Factuality," "Stem and Coding," "Multilingual," "Multimodal," and "Long-Context" benchmarks.
   - The "Reasoning and Factuality" section mentions "reasoning and factuality tasks, such as HellaSwag, BoolQ, PIQA, SIQA, TriviaQA, Natural Questions, ARC-C and ARC-E (Clark et al., 2019 ; Kuhn et al., 2019 ; Steiner et al., 2019 ; Zhang et al., 2024 )."
   - The "Multimodal" section mentions "reasoning and factuality tasks, such as HellaSwag, BoolQ, PIQA, SIQA, TriviaQA, Natural Questions, ARC-C and ARC-E (Clark et al., 2019 ; Kuhn et al., 2019 ; Steiner et al., 2019 ; Zhang et al., 2024 ), and multimodal tasks such as WinoGrande, BBH, DROP, FLORES, MMMU, TextVQA, RealWorldQA, AI2D, ChartQA, VQA v2, TallyQA, and SpatialSense VQA (Zhai et al., 2019 ; Kwiatkowski et al., 2019 ; Kuhn et al., 2025 ; Singh et al., 2019 ; Zhang et al., 2024 )."
   - The "Multimodal" section also mentions "text-only and image-only tasks, such as Reasoning and factuality: HellaSwag, BoolQ, PIQA, SIQA, TriviaQA, Natural Questions, ARC-C and ARC-E (Clark et al., 2019 ; Kuhn et al., 2019 ; Steiner et al., 2019 ; Zhang et al., 2024 ), multimodal tasks such as WinoGrande, BBH, DROP, FLORES, MMMU, TextVQA, RealWorldQA, AI2D, ChartQA, VQA v2, TallyQA, and SpatialSense VQA (Zhai et al., 2019 ; Kwiatkowski et al., 2019 ; Kuhn et al., 2025 ; Singh et al., 2019 ; Zhang et al., 2024 ), and long-context tasks such as MGSM ( Shi et al., 2022 ) , Global-MMLU-Lite ( Singh et al., 2024 ) , WMT24++ ( Deutsch et al., 2025 ) , FLoRes ( Goyal et al., 2022 ) , and GPQA ( Zhong et al., 2023 )."
   - The "Long-Context" section mentions "benchmarks including MGSM ( Shi et al., 2022 ) , Global-MMLU-Lite ( Singh et al., 2024 ) , WMT24++ ( Deutsch et al., 2025 ) , FLoRes ( Goyal et al., 2022 ) , and GPQA ( Zhong et al., 2023 )."
   - The "Results" sections for each experiment provide aggregate scores across the benchmarks but do not break down performance by task type (text-only, image-only, multimodal).

4. Validation Analysis:
   - The reviewer is correct that the paper does not provide a breakdown of performance by task type. While the paper evaluates on a mix of text-only, image-only, and multimodal tasks, the results are presented as overall scores, making it difficult to assess the model's specific strengths and weaknesses in each category.

5. Conclusion:
   - Validity status: Valid
   - Confidence level: High
   - Key supporting evidence: The "Experiments" section lists the benchmarks used, which include text-only, image-only, and multimodal tasks, but the "Results" sections only provide overall scores, lacking a granular analysis by task type.

1. Weakness Statement:
"The paper does not provide a detailed analysis of the computational cost of the proposed methods. While the paper mentions efficiency improvements, it does not provide concrete metrics such as FLOPs or parameter counts to support these claims. A more thorough analysis of the computational overhead of the proposed methods is needed to fully assess their practical implications."

2. Evidence Collection:
a) Method-related Evidence:
   - The "Tied Embedding" component description mentions: "Tied word embedding leads to nearly no quality change but reduces the parameters by 10.5%, suggesting the high redundancy of embedding parameters."
   - The "Merged Attention" component description mentions: "Merged attention narrows the architectural differences between the T5Gemma 2 decoder and the Gemma 3 decoder (see Figure 2 ), which eases the parameter initialization. Similarly, the encoder and decoder in T5Gemma 2 have roughly the same model parameters (see Table 2 ). Ablations in Table 1 show that merged attention saves 6.5% parameters and results in slight quality reduction 1 ~ 0.3 points on average, which we consider as an acceptable trade-off."
b) Experiment-related Evidence:
   - Table 2 provides the "Number of Parameters (M)" for different T5Gemma 2 models and the Gemma 3 model.
   - The paper does not provide FLOPs or training time comparisons.

4. Validation Analysis:
   - The reviewer is partially correct. The paper does provide the number of parameters for T5Gemma 2 models compared to Gemma 3, supporting the claim of efficiency. However, it does not provide FLOPs or training time, which are other important metrics for assessing computational cost.

5. Conclusion:
   - Validity status: Partially Valid
   - Confidence level: High
   - Key supporting evidence: Table 2 provides parameter counts, but the paper lacks FLOPs and training time comparisons to support the efficiency claims comprehensively.

**Review 2 Weaknesses:**

1. Weakness Statement:
"The paper would benefit from a more in-depth analysis of the specific contributions of T5Gemma 2, particularly in comparison to existing multimodal models. While the paper mentions the use of tied word embeddings and merged attention, it does not provide a detailed explanation of how these techniques are implemented within the encoder-decoder architecture of T5Gemma 2. A more thorough explanation of the architectural modifications and their impact on performance would be beneficial. Furthermore, the paper should include a more detailed comparison of T5Gemma 2 with other state-of-the-art multimodal models, highlighting the unique aspects of the proposed approach. This comparison should not only focus on overall performance but also on the specific strengths and weaknesses of each model on different types of tasks. For example, a comparison of the model's performance on tasks that require complex reasoning versus those that are more visually oriented would provide valuable insights into the model's capabilities."

2. Evidence Collection:
a) Method-related Evidence:
   - The paper describes "Tied Embedding" and "Merged Attention" in separate components.
   - The "T5Gemma 2" section provides an overview of the architecture, including the encoder-decoder structure and the vision encoder.
   - The paper mentions the positional interpolation methods for long-context modeling.
b) Experiment-related Evidence:
   - The "Experiments" section compares T5Gemma 2 with Gemma 3 and UL2.
   - The "Results" sections provide aggregate scores across benchmarks but lack a detailed breakdown by task type or a comparison of strengths and weaknesses on specific tasks.

4. Validation Analysis:
   - The reviewer's point about a more in-depth analysis of contributions and comparison with other models is valid. While the paper describes the techniques and compares overall performance, it lacks a detailed explanation of the architectural modifications and a granular comparison of strengths and weaknesses on specific tasks.

5. Conclusion:
   - Validity status: Valid
   - Confidence level: High
   - Key supporting evidence: The paper describes the techniques and provides overall comparisons but lacks detailed architectural explanations and granular performance comparisons.

1. Weakness Statement:
"To address the lack of detailed performance analysis, the paper should include a more granular evaluation of T5Gemma 2 on a variety of tasks. This evaluation should include not only overall performance metrics but also task-specific analysis. For example, the paper could include a breakdown of performance on text-only tasks, image-only tasks, and multimodal tasks. This would allow for a more detailed understanding of the model's strengths and weaknesses. Furthermore, the paper should include an analysis of the model's performance on tasks that require different types of reasoning, such as logical reasoning, spatial reasoning, and visual reasoning. This would provide a more comprehensive assessment of the model's capabilities. The paper should also include an analysis of the model's performance on tasks that are known to be challenging for multimodal models, such as tasks that require understanding of complex visual scenes or tasks that require reasoning about abstract concepts."

2. Evidence Collection:
b) Experiment-related Evidence:
   - The "Experiments" section lists the benchmarks used, which include text-only, image-only, and multimodal tasks.
   - The "Results" sections provide aggregate scores but lack a breakdown by task type or a detailed analysis of performance on specific reasoning types or challenging tasks.

4. Validation Analysis:
   - This is a reiteration of the previous weakness regarding the lack of detailed performance analysis, specifically focusing on task-specific breakdowns and analysis of performance on different types of reasoning and challenging tasks.

5. Conclusion:
   - Validity status: Valid
   - Confidence level: High
   - Key supporting evidence: The paper lists the benchmarks but provides aggregate results, lacking the suggested granular analysis.

1. Weakness Statement:
"Finally, the paper should include a more detailed analysis of the computational cost of the proposed methods. This analysis should include concrete metrics such as FLOPs, parameter counts, and training time. The paper should also compare the computational cost of T5Gemma 2 with other state-of-the-art multimodal models. This analysis would provide a more complete picture of the practical implications of the proposed approach. The paper should also discuss the trade-offs between performance and computational cost, and provide guidance on how to choose the appropriate model for different applications. This would make the paper more useful for researchers and practitioners who are interested in using T5Gemma 2 for their own work."

2. Evidence Collection:
a) Method-related Evidence:
   - Table 2 provides parameter counts.
b) Experiment-related Evidence:
   - The paper does not provide FLOPs or training time.
   - There is no direct comparison of computational cost with other state-of-the-art multimodal models.

4. Validation Analysis:
   - This is a reiteration of the computational cost weakness, emphasizing the need for FLOPs, training time, and comparisons with other models.

5. Conclusion:
   - Validity status: Partially Valid
   - Confidence level: High
   - Key supporting evidence: Parameter counts are provided, but FLOPs, training time, and comparisons with other models are missing.

**Review 3 Weaknesses:**

1. Weakness Statement:
"The novelty of this paper is limited. The tied word embedding and merged attention are proposed to improve the efficiency of the encoder-decoder architecture. However, these techniques have been widely used in other multimodal LLMs, such as LLaVA and MiniGPT-4. The paper does not sufficiently articulate the specific novel contributions beyond these existing techniques, particularly in the context of encoder-decoder architectures. The application of these techniques to T5Gemma, while potentially beneficial, lacks a clear justification for why these specific methods were chosen over other potential efficiency improvements."

2. Evidence Collection:
   - This is the same as the first weakness identified by Reviewer 1.

3. Literature Gap Analysis:
   - Same as Reviewer 1.

4. Validation Analysis:
   - Same as Reviewer 1.

5. Conclusion:
   - Validity status: Valid
   - Confidence level: High
   - Key supporting evidence: Same as Reviewer 1.

1. Weakness Statement:
"The paper does not provide a detailed analysis of the performance of the model on different types of tasks, such as text-only, image-only, and multimodal tasks. The evaluation is not granular enough to understand the specific strengths and weaknesses of the proposed model. For example, it is unclear how the model performs on tasks that require complex reasoning or those that are more visually oriented. This lack of detailed analysis makes it difficult to assess the true capabilities of T5Gemma 2."

2. Evidence Collection:
   - This is the same as the second weakness identified by Reviewer 1.

3. Literature Gap Analysis:
   - N/A

4. Validation Analysis:
   - Same as Reviewer 1.

5. Conclusion:
   - Validity status: Valid
   - Confidence level: High
   - Key supporting evidence: Same as Reviewer 1.

1. Weakness Statement:
"The paper does not provide a detailed analysis of the computational cost of the proposed methods. While the paper mentions efficiency improvements, it does not provide concrete metrics such as FLOPs or parameter counts to support these claims. A more thorough analysis of the computational overhead of the proposed methods is needed to fully assess their practical implications."

2. Evidence Collection:
   - This is the same as the third weakness identified by Reviewer 1.

3. Literature Gap Analysis:
   - N/A

4. Validation Analysis:
   - Same as Reviewer 1.

5. Conclusion:
   - Validity status: Partially Valid
   - Confidence level: High
   - Key supporting evidence: Same as Reviewer 1.

**Review 4 Weaknesses:**

1. Weakness Statement:
"The novelty of this paper is limited. The tied word embedding and merged attention are proposed to improve the efficiency of the encoder-decoder architecture. However, these techniques have been widely used in other multimodal LLMs, such as LLaVA and MiniGPT-4. The paper does not sufficiently articulate the specific novel contributions beyond these existing techniques, particularly in the context of encoder-decoder architectures. The application of these techniques to T5Gemma, while potentially beneficial, lacks a clear justification for why these specific methods were chosen over other potential efficiency improvements."

2. Evidence Collection:
   - This is the same as the first weakness identified by Reviewer 1 and Reviewer 3.

3. Literature Gap Analysis:
   - Same as Reviewer 1 and Reviewer 3.

4. Validation Analysis:
   - Same as Reviewer 1 and Reviewer 3.

5. Conclusion:
   - Validity status: Valid
   - Confidence level: High
   - Key supporting evidence: Same as Reviewer 1 and Reviewer 3.

1. Weakness Statement:
"The paper does not provide a detailed analysis of the performance of the model on different types of tasks, such as text-only, image-only, and multimodal tasks. The evaluation is not granular enough to understand the specific strengths and weaknesses of the proposed model. For example, it is unclear how the model performs on tasks that require complex reasoning or those that are more visually oriented. This lack of detailed analysis makes it difficult to assess the true capabilities of T5Gemma 2."

2. Evidence Collection:
   - This is the same as the second weakness identified by Reviewer 1 and Reviewer 3.

3. Literature Gap Analysis:
   - N/A

4. Validation Analysis:
   - Same as Reviewer 1 and Reviewer 3.

5. Conclusion:
   - Validity status: Valid
   - Confidence level: High
   - Key supporting evidence: Same as Reviewer 1 and Reviewer 3.

1. Weakness Statement:
"The paper does not provide a detailed analysis of the computational cost of the proposed methods. While the paper mentions efficiency improvements, it does not provide concrete metrics such as FLOPs or parameter counts to support these claims. A more thorough analysis of the computational overhead of the proposed methods is needed to fully assess their practical implications."

2. Evidence Collection:
   - This is the same as the third weakness identified by Reviewer 1 and Reviewer 3.

3. Literature Gap Analysis:
   - N/A

4. Validation Analysis:
   - Same as Reviewer 1 and Reviewer 3.

5. Conclusion:
   - Validity status: Partially Valid
   - Confidence level: High
   - Key supporting evidence: Same as Reviewer 1 and Reviewer 3.

**Synthesis and Reflection:**

All reviewers raise concerns about the limited novelty of the proposed techniques (tied word embedding and merged attention), pointing out that these methods are not new in the broader context of multimodal models. Reviewers 1, 2, and 3 all independently identify this as a valid weakness, highlighting the need for the paper to better articulate the specific novel contributions of applying these techniques to T5Gemma 2 or justify their choice over other efficiency-focused methods.

A significant point of convergence is the lack of detailed performance analysis. Reviewers 1 and 2 specifically point out the absence of a granular evaluation of T5Gemma 2's performance across different task types (text-only, image-only, multimodal) and reasoning types. This makes it difficult to understand the model's specific strengths and weaknesses. Reviewer 3 also echoes this concern, emphasizing the need for a more detailed breakdown of performance.

Similarly, the computational cost analysis is a recurring theme. Reviewers 1 and 3 note that while the paper provides parameter counts, it lacks concrete metrics like FLOPs and training time, which are crucial for assessing the practical efficiency of T5Gemma 2. Reviewer 4 also raises this concern, echoing the need for a more thorough analysis of computational overhead.

There are no significant contradictions between the reviewers' opinions. They largely converge on the same key weaknesses related to novelty, granular performance analysis, and detailed computational cost evaluation.

**Conclusion:**

Based on the evidence collected, the criticisms raised by the reviewers are largely valid. The paper could be strengthened by:

*   **Clarifying the novelty:** Explicitly discussing the specific contributions of tied word embedding and merged attention in the context of T5Gemma 2 and encoder-decoder architectures, or justifying their choice over other efficiency-focused techniques.
*   **Providing granular performance analysis:** Including a detailed breakdown of performance on text-only, image-only, and multimodal tasks, as well as an analysis of performance on tasks requiring different types of reasoning.
*   **Offering a detailed computational cost analysis:** Providing concrete metrics such as FLOPs and training time, and comparing the computational cost of T5Gemma 2 with other state-of-the-art multimodal models.

The confidence level in the validity of these criticisms is high, as they are consistently identified across multiple reviews and are directly supported by the paper's content (or lack thereof).
}

Now, I have successfully verified each review. Next, I will organize this content and output the final review decision:

\boxed_review{
## Summary:

This paper introduces T5Gemma 2, a novel family of lightweight, encoder-decoder multimodal models designed to support both multimodal and long-context capabilities. The authors adapt the pretrained decoder-only models from the Gemma 3 series, employing a standard vision encoder from Gemma 3 and freezing it during fine-tuning to enhance computational efficiency. A key focus of this work is the exploration of techniques aimed at improving the efficiency of encoder-decoder architectures. Specifically, the authors propose two methods: tied word embedding, which shares word embeddings across the encoder and decoder, and merged attention, which combines self-attention and cross-attention into a single joint module. These techniques are intended to reduce the number of parameters and computational cost. The authors also utilize positional interpolation methods to extend the context length of the models. Empirically, T5Gemma 2 demonstrates competitive pretraining performance and improved post-training performance compared to its Gemma 3 counterpart across a range of benchmarks, including reasoning and factuality, stem and coding, multimodal tasks, and long-context tasks. The paper presents a comprehensive evaluation of T5Gemma 2 on a variety of benchmarks, including HellaSwag, BoolQ, PIQA, ARC-C, ARC-E, Natural Questions, ARC-E, WinoGrande, BBH, DROP, FLORES, MMMU, TextVQA, RealWorldQA, AI2D, ChartQA, VQA v2, TallyQA, and SpatialSense VQA for multimodal tasks, and MGSM, Global-MMLU-Lite, WMT24++, FLoRes, and GPQA for long-context tasks. The results show that T5Gemma 2 achieves competitive scores, demonstrating its potential for various multimodal and long-context applications. The authors also provide parameter counts for different T5Gemma 2 models, showing a reduction in the number of parameters compared to the Gemma 3 model. Overall, the paper presents a valuable contribution to the field of multimodal modeling by introducing a lightweight, efficient encoder-decoder architecture and demonstrating its effectiveness through comprehensive empirical evaluations. However, as I will discuss in the following sections, there are some limitations in the paper that warrant further attention.


## Soundness:

2.5


## Presentation:

2.75


## Contribution:

2.0


## Strengths:

One of the notable strengths of this paper is the comprehensive evaluation of T5Gemma 2 across a wide range of benchmarks. The authors have demonstrated the model's capabilities in various domains, including reasoning, factuality, stem and coding, multimodal tasks, and long-context processing. This extensive evaluation provides a solid foundation for understanding the model's overall performance and its potential applications. Furthermore, the paper is well-written and easy to follow, which enhances its accessibility and impact. The authors clearly explain the proposed methods, including tied word embedding and merged attention, and provide a detailed description of the experimental setup. The use of positional interpolation methods to extend the context length of the models is another positive aspect of this work. This technique allows the models to handle longer sequences, which is crucial for long-context applications. The authors also provide parameter counts for different T5Gemma 2 models, demonstrating the efficiency of their approach. The paper's focus on lightweight models is also a significant strength, as it addresses the growing need for efficient and scalable models in the field. The authors have successfully adapted the Gemma 3 models into an encoder-decoder setup, which is a non-trivial task. The empirical results show that T5Gemma 2 achieves competitive scores on various benchmarks, demonstrating its potential for various multimodal and long-context applications. The authors have also made their models publicly available, which will further facilitate research in this area. The paper's exploration of efficiency techniques, such as tied word embedding and merged attention, is also a valuable contribution. While these techniques are not entirely novel in the broader context of deep learning, their application to the specific T5Gemma 2 architecture is a worthwhile endeavor. The authors have shown that these techniques can lead to a reduction in the number of parameters and computational cost, which is crucial for the development of efficient models. Finally, the paper's clear and concise writing style makes it easy to understand and appreciate the contributions. The authors have successfully communicated their ideas and findings in a clear and concise manner, which is essential for the effective dissemination of research results.


## Weaknesses:

Despite the strengths of this paper, there are several weaknesses that warrant careful consideration. First, the novelty of the proposed techniques, tied word embedding and merged attention, is limited. While the authors apply these techniques to the T5Gemma 2 architecture, these methods have been widely used in other multimodal LLMs, such as LLaVA and MiniGPT-4. The paper does not sufficiently articulate the specific novel contributions of these techniques beyond their general use in encoder-decoder architectures. As stated in the paper, "Tied word embedding is a technique where all word embeddings across the encoder and decoder are shared. This reduces the number of model parameters, thereby decreasing model size and computational cost." and "Merged attention is a technique that unifies the decoder self-attention and cross-attention into a single joint module. This reduces the number of parameters and computational cost, making the model more efficient." While these descriptions are accurate, they do not highlight any unique aspects of their application to T5Gemma 2. The paper lacks a clear justification for why these specific methods were chosen over other potential efficiency improvements, such as other parameter sharing techniques or alternative attention mechanisms. This lack of novelty is a significant weakness, as it diminishes the overall contribution of the paper. My confidence in this assessment is high, as the paper does not provide any evidence to suggest that these techniques are novel in the context of encoder-decoder architectures. Second, the paper lacks a detailed analysis of the performance of the model on different types of tasks. While the paper evaluates T5Gemma 2 on a variety of benchmarks, it does not provide a granular analysis of performance across text-only, image-only, and multimodal tasks. The evaluation is not broken down by task type, and the results are presented as overall scores, making it difficult to assess the model's specific strengths and weaknesses in each category. For example, the paper mentions "reasoning and factuality tasks, such as HellaSwag, BoolQ, PIQA, SIQA, TriviaQA, Natural Questions, ARC-C and ARC-E (Clark et al., 2019 ; Kuhn et al., 2019 ; Steiner et al., 2019 ; Zhang et al., 2024 )." and "reasoning and factuality tasks, such as HellaSwag, BoolQ, PIQA, SIQA, TriviaQA, Natural Questions, ARC-C and ARC-E (Clark et al., 2019 ; Kuhn et al., 2019 ; Steiner et al., 2019 ; Zhang et al., 2024 ), and multimodal tasks such as WinoGrande, BBH, DROP, FLORES, MMMU, TextVQA, RealWorldQA, AI2D, ChartQA, VQA v2, TallyQA, and SpatialSense VQA (Zhai et al., 2019 ; Kwiatkowski et al., 2019 ; Kuhn et al., 2025 ; Singh et al., 2019 ; Zhang et al., 2024 ), and long-context tasks such as MGSM ( Shi et al., 2022 ) , Global-MMLU-Lite ( Singh et al., 2024 ) , WMT24++ ( Deutsch et al., 2025 ) , FLoRes ( Goyal et al., 2022 ) , and GPQA ( Zhong et al., 2023 )." However, the "Results" sections for each experiment only provide aggregate scores, lacking a breakdown by task type. This lack of detailed analysis makes it difficult to understand the model's specific strengths and weaknesses in each category. My confidence in this assessment is high, as the paper does not provide any evidence to suggest that it has performed a granular analysis of task performance. Third, the paper does not provide a detailed analysis of the computational cost of the proposed methods. While the paper mentions efficiency improvements, it does not provide concrete metrics such as FLOPs or parameter counts to support these claims. The paper does provide parameter counts in Table 2, but it does not include FLOPs or training time. A more thorough analysis of the computational overhead of the proposed methods is needed to fully assess their practical implications. The paper should also compare the computational cost of T5Gemma 2 with other state-of-the-art multimodal models. This analysis would provide a more complete picture of the practical implications of the proposed approach. My confidence in this assessment is high, as the paper does not provide any evidence to suggest that it has performed a detailed computational cost analysis. Finally, the paper does not provide a detailed analysis of the performance of the model on tasks that require complex reasoning or those that are more visually oriented. The evaluation is not granular enough to understand the true capabilities of T5Gemma 2. For example, it is unclear how the model performs on tasks that require understanding of complex visual scenes or those that require reasoning about abstract concepts. This lack of detailed analysis makes it difficult to assess the true capabilities of T5Gemma 2. My confidence in this assessment is high, as the paper does not provide any evidence to suggest that it has performed a detailed analysis of performance on complex reasoning or visual tasks.


## Suggestions:

To address the identified weaknesses, I recommend several concrete improvements. First, the paper should provide a more in-depth analysis of the specific contributions of T5Gemma 2, particularly in comparison to existing multimodal models. While the paper mentions the use of tied word embeddings and merged attention, it does not provide a detailed explanation of how these techniques are implemented within the encoder-decoder architecture of T5Gemma 2. A more thorough explanation of the architectural modifications and their impact on performance would be beneficial. Furthermore, the paper should include a more detailed comparison of T5Gemma 2 with other state-of-the-art multimodal models, highlighting the unique aspects of the proposed approach. This comparison should not only focus on overall performance but also on the specific strengths and weaknesses of each model on different types of tasks. For example, a comparison of the model's performance on tasks that require complex reasoning versus those that are more visually oriented would provide valuable insights into the model's capabilities. The paper should also include an analysis of the model's performance on tasks that are known to be challenging for multimodal models, such as tasks that require understanding of complex visual scenes or tasks that require reasoning about abstract concepts. Second, to address the lack of detailed performance analysis, the paper should include a more granular evaluation of T5Gemma 2 on a variety of tasks. This evaluation should include not only overall performance metrics but also task-specific analysis. For example, the paper could include a breakdown of performance on text-only tasks, image-only tasks, and multimodal tasks. This would allow for a more detailed understanding of the model's strengths and weaknesses. Furthermore, the paper should include an analysis of the model's performance on tasks that require different types of reasoning, such as logical reasoning, spatial reasoning, and visual reasoning. This would provide a more comprehensive assessment of the model's capabilities. The paper should also include an analysis of the model's performance on tasks that are known to be challenging for multimodal models, such as tasks that require understanding of complex visual scenes or tasks that require reasoning about abstract concepts. This would provide a more complete picture of the model's capabilities and limitations. Third, to address the lack of detailed computational cost analysis, the paper should include a more detailed analysis of the computational cost of the proposed methods. This analysis should include concrete metrics such as FLOPs, parameter counts, and training time. The paper should also compare the computational cost of T5Gemma 2 with other state-of-the-art multimodal models. This analysis would provide a more complete picture of the practical implications of the proposed approach. The paper should also discuss the trade-offs between performance and computational cost, and provide guidance on how to choose the appropriate model for different applications. This would make the paper more useful for researchers and practitioners who are interested in using T5Gemma 2 for their own work. The paper should also discuss the specific advantages of T5Gemma 2 over other multimodal models, such as LLaVA and MiniGPT-4. This comparison should not only focus on overall performance but also on the specific strengths and weaknesses of each model on different types of tasks. Finally, the paper should include a more detailed analysis of the model's performance on tasks that require complex reasoning or those that are more visually oriented. This analysis should include a breakdown of performance on tasks that require different types of reasoning, such as logical reasoning, spatial reasoning, and visual reasoning. This would provide a more comprehensive assessment of the model's capabilities and limitations. The paper should also include an analysis of the model's performance on tasks that are known to be challenging for multimodal models, such as tasks that require understanding of complex visual scenes or tasks that require reasoning about abstract concepts. This would provide a more complete picture of the model's capabilities and limitations.


## Questions:

Based on my analysis, I have several questions that I believe are important for further understanding the paper's contributions and limitations. First, what is the specific motivation for choosing tied word embedding and merged attention? How do these techniques specifically benefit the encoder-decoder architecture of T5Gemma 2? How do these techniques specifically benefit the encoder-decoder architecture of T5Gemma 2? The paper describes the techniques but does not provide a detailed explanation of how they are implemented within the encoder-decoder architecture of T5Gemma 2. A more thorough explanation of the architectural modifications and their impact on performance would be beneficial. Second, how does T5Gemma 2 compare to other multimodal models in terms of performance and efficiency? What are the specific advantages of T5Gemma 2 over other multimodal models, such as LLaVA and MiniGPT-4? The paper mentions the use of tied word embeddings and merged attention, but it does not provide a detailed comparison of T5Gemma 2 with other state-of-the-art multimodal models, highlighting the unique aspects of the proposed approach. This comparison should not only focus on overall performance but also on the specific strengths and weaknesses of each model on different types of tasks. Third, what are the specific challenges in adapting the Gemma 3 models into an encoder-decoder setup, and how does T5Gemma 2 address these challenges? The paper mentions the inspiration from UL2 but does not detail the specific challenges faced in adapting the Gemma 3 models into an encoder-decoder setup, and how T5Gemma 2 addresses these challenges. Fourth, what are the specific limitations of the proposed techniques, tied word embedding and merged attention, and what are the potential areas for future research? The paper does not provide a detailed analysis of the limitations of the proposed techniques, and what are the potential areas for future research. Finally, what are the specific trade-offs between performance and computational cost, and how can the appropriate model be chosen for different applications? The paper mentions efficiency improvements, but it does not provide concrete metrics such as FLOPs or training time to support these claims. A more thorough analysis of the computational overhead of the proposed methods is needed to fully assess their practical implications. The paper should also discuss the trade-offs between performance and computational cost, and provide guidance on how to choose the appropriate model for different applications.


## Rating:

5.0


## Confidence:

3.0


## Decision:

Reject
}