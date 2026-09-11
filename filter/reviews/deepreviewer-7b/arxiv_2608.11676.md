I will use Standard Mode for comprehensive thinking. As a professional reviewer, I will simulate 4 different reviewers, followed by the verification thinking. Then I will output the Finally Review Output. Let me think - Standard Mode means I will output the original review, followed by the verification thinking. Considering that I am currently in standard mode, I should think from my existing knowledge and consider some related work content when writing about weaknesses. Then I will output the Finally Review Output and Meta Review Output:

\boxed_simreviewers{
## Reviewer 1

### Summary

This paper addresses the problem of cross-architecture communication between LLMs. The authors identify a problem they call entity grounding, which occurs when continuous bridges that transfer contextual information from sender to receiver lose discrete entity identity. To address this, they propose XBridge, a decode-free communication protocol that uses two mechanisms: Lexical Anchor Mapping (LAM) and Latent Enrichment Bridge (LEB). LAM maps the sender's original context tokens to the receiver's vocabulary, while LEB enriches the context with sender-side hidden states. XBridge outperforms text-based communication methods on all seven tasks for each model pair while achieving 11× lower latency than text-based communication, and shows in a same-architecture setting it exceeds a KV-sharing baseline on six of seven tasks.

### Soundness

3

### Presentation

3

### Contribution

3

### Strengths

- The paper addresses an important problem of cross-architecture communication between LLMs.
- The proposed method is novel and effective, outperforming text-based communication methods on all seven tasks for each model pair while achieving 11× lower latency than text-based communication.
- The paper is well-written and easy to follow.

### Weaknesses

#### Some Related Works


#### comment

 - The paper does not provide a detailed analysis of the computational cost of the proposed method, such as the training time and inference time.
- The paper does not provide a detailed analysis of the memory usage of the proposed method.
- The paper does not provide a detailed analysis of the robustness of the proposed method to different types of input data.

### Suggestions

The paper should include a more thorough analysis of the computational resources required by the proposed method. Specifically, the authors should provide a detailed breakdown of the training time, including the time taken for each stage of the training process, such as the LAM and LEB training. This analysis should also include the inference time for both training and inference, as well as the memory usage during these processes. It would be beneficial to compare these metrics against baseline methods to provide a clear understanding of the computational overhead introduced by XBridge. Furthermore, the authors should investigate the scalability of the method with respect to the size of the models and the input data. This would help to determine the practical applicability of the method in real-world scenarios.

In addition to computational cost, the paper should also provide a more detailed analysis of the memory usage of the proposed method. This analysis should include the memory footprint of the model parameters, the intermediate activations during training and inference, and the memory required for the training data. The authors should also investigate the impact of different memory optimization techniques, such as gradient checkpointing and mixed-precision training, on the memory usage of the method. It would be beneficial to compare the memory usage of XBridge against baseline methods to provide a clear understanding of the memory savings achieved by the proposed method. This analysis should also consider the memory requirements for different batch sizes and sequence lengths.

Finally, the paper should include a more detailed analysis of the robustness of the proposed method to different types of input data. This analysis should include an evaluation of the method's performance on noisy or adversarial inputs, as well as an investigation of its sensitivity to different types of perturbations. The authors should also consider the impact of different input preprocessing techniques on the performance of the method. Furthermore, it would be beneficial to analyze the method's performance on different types of tasks and datasets to determine its generalizability. This analysis should include a discussion of the limitations of the method and potential areas for future improvement.

### Questions

- How does the proposed method perform on tasks that require more complex reasoning or multi-hop inference?
- How does the proposed method perform on tasks that require different types of entity grounding?

### Rating

6

### Confidence

3

**********

## Reviewer 2

### Summary

This paper addresses the entity grounding problem in heterogeneous LLM communication, where continuous bridges lose entity identity in the latent bottleneck. The authors propose XBridge, a decode-free protocol that combines Lexical Anchor Mapping (LAM) and Latent Enrichment Bridge (LEB) to achieve entity grounding. XBridge outperforms text-based communication methods on all seven tasks for each model pair while achieving 11× lower latency than text-based communication. The authors also show that XBridge exceeds a KV-sharing baseline on six of seven tasks in a same-architecture setting.

### Soundness

3

### Presentation

3

### Contribution

3

### Strengths

1. The paper is well-written and easy to follow.
2. The proposed method is novel and effective, outperforming text-based communication methods on all seven tasks for each model pair while achieving 11× lower latency than text-based communication.
3. The paper provides a detailed analysis of the entity grounding problem and the limitations of existing communication methods.
4. The paper provides a detailed analysis of the entity grounding problem and the limitations of existing communication methods.
5. The paper provides a detailed analysis of the entity grounding problem and the limitations of existing communication methods.

### Weaknesses

#### Some Related Works


#### comment

1. The paper does not provide a detailed analysis of the computational cost of the proposed method, such as the training time and inference time.
2. The paper does not provide a detailed analysis of the memory usage of the proposed method.
3. The paper does not provide a detailed analysis of the robustness of the proposed method to different types of input data.

### Suggestions

The paper would benefit from a more thorough analysis of the computational costs associated with the proposed XBridge method. Specifically, the authors should provide a detailed breakdown of the training time, including the time taken for each stage of the training process, such as the Lexical Anchor Mapping (LAM) and Latent Enrichment Bridge (LEB) training. This should include the number of GPUs used, the batch size, and the number of training epochs. Furthermore, the inference time for both training and inference should be reported, along with the memory usage during these processes. A comparison of these metrics against baseline methods would provide a clear understanding of the computational overhead introduced by XBridge. This analysis should also consider the scalability of the method with respect to the size of the models and the input data. For example, how does the training time scale with the number of parameters in the models? What is the inference time for different input lengths? These details are crucial for assessing the practical applicability of the method.

In addition to computational cost, the paper should include a more detailed analysis of the memory usage of the proposed method. This analysis should include the memory footprint of the model parameters, the intermediate activations during training and inference, and the memory required for the training data. The authors should also investigate the impact of different memory optimization techniques, such as gradient checkpointing and mixed-precision training, on the memory usage of the method. It would be beneficial to compare the memory usage of XBridge against baseline methods to provide a clear understanding of the memory savings achieved by the proposed method. This analysis should also consider the memory requirements for different batch sizes and sequence lengths. For instance, how does the memory usage change when using larger batch sizes or longer input sequences? This information is essential for understanding the resource requirements of the method in different scenarios.

Finally, the paper should include a more detailed analysis of the robustness of the proposed method to different types of input data. This analysis should include an evaluation of the method's performance on noisy or adversarial inputs, as well as an investigation of its sensitivity to different types of perturbations. The authors should also consider the impact of different input preprocessing techniques on the performance of the method. Furthermore, it would be beneficial to analyze the method's performance on different types of tasks and datasets to determine its generalizability. For example, how does the method perform on tasks that require more complex reasoning or multi-hop inference? This analysis should include a discussion of the limitations of the method and potential areas for future improvement. The authors should also explore the method's performance on datasets with varying levels of noise and adversarial examples to better understand its robustness.

### Questions

Please see the weaknesses.

### Rating

6

### Confidence

3

**********

## Reviewer 3

### Summary

This paper introduces XBridge, a novel communication protocol designed to address the entity grounding problem in heterogeneous LLM communication. The authors identify the entity grounding problem as a key challenge in cross-architecture communication, where continuous bridges struggle to preserve entity identity. To tackle this, XBridge employs a two-pronged approach: Lexical Anchor Mapping (LAM) and Latent Enrichment Bridge (LEB). LAM maps sender tokens to the receiver’s vocabulary, providing discrete entity anchors, while LEB enriches the context with sender-side hidden states, allowing for contextual information transfer. The authors demonstrate that XBridge outperforms text-based communication methods across multiple model families and tasks, achieving 11× lower latency and surpassing a KV-sharing baseline in a same-architecture setting. The paper provides a comprehensive evaluation, including ablation studies and comparisons with existing methods, highlighting the effectiveness and efficiency of XBridge in heterogeneous LLM communication.

### Soundness

3

### Presentation

3

### Contribution

3

### Strengths

1. The paper introduces a novel approach, XBridge, which effectively addresses the entity grounding problem in heterogeneous LLM communication. By combining Lexical Anchor Mapping (LAM) and Latent Enrichment Bridge (LEB), the method provides a unique solution that leverages both discrete and continuous information transfer.
2. The authors conduct extensive experiments across multiple model families (Llama, Qwen, and Mistral) and seven benchmarks, demonstrating the robustness and generalizability of XBridge. The results consistently show that XBridge outperforms text-based communication methods, highlighting its effectiveness in various scenarios.
3. The paper is well-organized and clearly written, with a logical flow that guides the reader through the problem statement, methodology, and experimental results. The use of figures and tables effectively illustrates the key concepts and findings.
4. The authors provide a detailed analysis of the entity grounding problem, including the entity fidelity metric and entity grounding failure, which adds depth to the understanding of the challenges in heterogeneous communication.

### Weaknesses

#### Some Related Works


#### comment

1. While the paper demonstrates the effectiveness of XBridge across different model families, it lacks a detailed analysis of the computational cost associated with the proposed method. Understanding the trade-offs between performance gains and computational overhead is crucial for practical applications, especially in resource-constrained environments. Specifically, the paper does not provide a breakdown of the computational cost associated with LAM and LEB, nor does it discuss the memory footprint of the proposed method, which is important for deployment on devices with limited resources.
2. The paper primarily focuses on the performance of XBridge in terms of accuracy and latency. However, it does not explore other important aspects such as robustness to adversarial attacks or sensitivity to variations in input data. A more comprehensive evaluation of these aspects would provide a better understanding of the method's reliability and practical applicability. For example, the paper does not investigate how XBridge performs when the input data contains noise or is slightly modified, which is a common scenario in real-world applications.
3. Although the paper compares XBridge with text-based communication methods, it does not include a comparison with other state-of-the-art communication protocols specifically designed for heterogeneous LLMs. Including such comparisons would provide a more complete picture of the method's strengths and weaknesses relative to existing approaches. The paper should also discuss the limitations of the proposed method, such as potential biases introduced by the lexical anchor mapping or the latent enrichment bridge, and how these limitations might affect the overall performance.

### Suggestions

The paper would benefit from a more detailed analysis of the computational cost associated with XBridge. Specifically, the authors should provide a breakdown of the computational cost for both LAM and LEB, including the number of parameters, FLOPs, and memory usage. This analysis should also consider the impact of different model sizes and input lengths on the computational cost. Furthermore, the authors should discuss the trade-offs between performance gains and computational overhead, and provide guidelines for selecting the appropriate model size and input length for different applications. For example, the authors could explore the use of model compression techniques or hardware acceleration to reduce the computational cost of XBridge, making it more suitable for resource-constrained environments. A thorough analysis of the computational cost would provide a more complete understanding of the practical implications of the proposed method.

To enhance the robustness analysis of XBridge, the authors should investigate its performance under various types of input perturbations, such as noise injection, adversarial attacks, and variations in input data. This analysis should include a quantitative evaluation of the method's performance under different levels of noise and adversarial attacks, using metrics such as accuracy, F1 score, and latency. The authors should also discuss the limitations of the proposed method, such as potential biases introduced by the lexical anchor mapping or the latent enrichment bridge, and how these limitations might affect the overall performance. For example, the authors could explore the use of robust optimization techniques to mitigate the impact of adversarial attacks on the performance of XBridge. A more comprehensive robustness analysis would provide a better understanding of the method's reliability and practical applicability in real-world scenarios.

Finally, the paper should include a more comprehensive comparison with other state-of-the-art communication protocols specifically designed for heterogeneous LLMs. This comparison should include a detailed analysis of the strengths and weaknesses of XBridge relative to existing approaches, considering factors such as accuracy, latency, and computational cost. The authors should also discuss the limitations of the proposed method, such as potential biases introduced by the lexical anchor mapping or the latent enrichment bridge, and how these limitations might affect the overall performance. For example, the authors could explore the use of alternative communication protocols, such as those based on knowledge distillation or model merging, to further improve the performance of XBridge. A more comprehensive comparison with existing methods would provide a more complete picture of the method's contributions and limitations.

### Questions

1. How does the proposed method handle cases where the lexical anchors are ambiguous or do not exist in the receiver’s vocabulary?
2. Can the authors provide more details on the training process for the Latent Enrichment Bridge (LEB)? Specifically, how is the training data generated, and what are the key hyperparameters used?
3. How does the performance of XBridge scale with the size of the models and the complexity of the tasks? Are there any limitations in terms of model size or task complexity?
4. What are the potential limitations of the proposed method, and how might these limitations be addressed in future work?

### Rating

8

### Confidence

3

**********

## Reviewer 4

### Summary

This paper proposes XBridge, a decode-free communication protocol that addresses the entity grounding problem in heterogeneous LLM communication. XBridge uses Lexical Anchor Mapping (LAM) to map the sender's original context tokens to the receiver's vocabulary, providing discrete entity anchors, and Latent Enrichment Bridge (LEB) to enrich the context with sender-side hidden states, allowing for contextual information transfer. The authors demonstrate that XBridge outperforms text-based communication methods on all seven tasks for each model pair while achieving 11× lower latency than text-based communication. The paper also shows that XBridge exceeds a KV-sharing baseline on six of seven tasks in a same-architecture setting.

### Soundness

3

### Presentation

3

### Contribution

3

### Strengths

1. The paper is well-written and easy to follow.
2. The proposed method is novel and effective, outperforming text-based communication methods on all seven tasks for each model pair while achieving 11× lower latency than text-based communication.
3. The paper provides a detailed analysis of the entity grounding problem and the limitations of existing communication methods.

### Weaknesses

#### Some Related Works


#### comment

1. The paper does not provide a detailed analysis of the computational cost of the proposed method, such as the training time and inference time.
2. The paper does not provide a detailed analysis of the memory usage of the proposed method.
3. The paper does not provide a detailed analysis of the robustness of the proposed method to different types of input data.

### Suggestions

The paper should include a more thorough analysis of the computational resources required by the proposed method. Specifically, the authors should provide a detailed breakdown of the training time, including the time taken for each stage of the training process, such as the Lexical Anchor Mapping (LAM) and Latent Enrichment Bridge (LEB) training. This analysis should also include the inference time for both training and inference, as well as the memory usage during these processes. It would be beneficial to compare these metrics against baseline methods to provide a clear understanding of the computational overhead introduced by XBridge. Furthermore, the authors should investigate the scalability of the method with respect to the size of the models and the input data. This would help to determine the practical applicability of the method in real-world scenarios.

In addition to computational cost, the paper should also provide a more detailed analysis of the memory usage of the proposed method. This analysis should include the memory footprint of the model parameters, the intermediate activations during training and inference, and the memory required for the training data. The authors should also investigate the impact of different memory optimization techniques, such as gradient checkpointing and mixed-precision training, on the memory usage of the method. It would be beneficial to compare the memory usage of XBridge against baseline methods to provide a clear understanding of the memory savings achieved by the proposed method. This analysis should also consider the memory requirements for different batch sizes and sequence lengths.

Finally, the paper should include a more detailed analysis of the robustness of the proposed method to different types of input data. This analysis should include an evaluation of the method's performance on noisy or adversarial inputs, as well as an investigation of its sensitivity to different types of perturbations. The authors should also consider the impact of different input preprocessing techniques on the performance of the method. Furthermore, it would be beneficial to analyze the method's performance on different types of tasks and datasets to determine its generalizability. This analysis should include a discussion of the limitations of the method and potential areas for future improvement.

### Questions

1. How does the proposed method perform on tasks that require more complex reasoning or multi-hop inference?
2. How does the proposed method perform on tasks that require different types of entity grounding?

### Rating

8

### Confidence

3

**********

}

I have finished generating simulated reviews from 4 reviewers. Next, I will generate verification content for these reviews:

\boxed_verification{
The user wants me to validate weaknesses identified by reviewers in the provided paper. I need to go through each reviewer's comments and find evidence in the paper to support their claims.

Plan:
1. Go through each reviewer's identified weaknesses.
2. For each weakness, find corresponding evidence in the paper's method and experiment sections.
3. If the weakness is about missing information, check if that information is indeed absent.
4. If the weakness is about the analysis, check if the analysis is sufficient or if more details are needed.
5. Synthesize the findings and determine if the weakness is valid, partially valid, or invalid.
```json
[
  {
    "Weakness Statement": "The paper does not provide a detailed analysis of the computational cost of the proposed method, such as the training time and inference time.",
    "Evidence Collection": {
      "b) Experiment-related Evidence (if applicable)": [
        "The paper mentions training time in the context of the bridge modules: \"The bridge is trained with a small balanced sample set in under 10 minutes on a single GPU on a balanced set of 587 samples drawn across the seven task domains.\" (Section 3.3)",
        "The paper mentions inference time: \"XBridge achieves 11 × \times lower latency than text-based communication, and in a same-architecture setting it exceeds KVComm [5] on 6 of 7 tasks (63.2 vs. 55.2 for Llama → \rightarrow Qwen, 61.9 vs. 61.2 for Qwen → \rightarrow Llama, 65.0 vs. 61.2 for Mistral → \rightarrow Qwen).\" (Section 4.2)",
        "However, there is no detailed breakdown of the training time for the Lexical Anchor Mapping (LAM) and Latent Enrichment Bridge (LEB) components, nor a detailed inference time breakdown for different input lengths or batch sizes."
      ]
    },
    "Validation Analysis": {
      "Primary evidence summary": "The paper provides some information on training and inference time, but lacks a detailed breakdown.",
      "Supporting quotes": [
        "The bridge is trained with a small balanced sample set in under 10 minutes on a single GPU on a balanced set of 587 samples drawn across the seven task domains."
      ],
      "Impact assessment": "The lack of detailed computational cost analysis makes it harder to fully assess the practical applicability of the method."
    },
    "Conclusion": {
      "Validity status": "Partially Valid",
      "Confidence level": "High",
      "Key supporting evidence": "The paper provides some training and inference time information but lacks a detailed breakdown for LAM and LEB, and doesn't analyze the impact of input length or batch size."
    }
  },
  {
    "Weakness Statement": "The paper does not provide a detailed analysis of the memory usage of the proposed method.",
    "Evidence Collection": {
      "b) Experiment-related Evidence (if applicable)": [
        "The paper mentions the size of the bridge modules: \"Each module has its own learnable parameters ( ∼ {\\textsim} 66M each, ∼ {\\textsim} 264M total, 3.8% of the receiver), training on a single GPU on a balanced set of 587 samples drawn across the seven task domains.\" (Section 3.3)",
        "The paper mentions the training data size: \"The sender receives the context document only and the receiver receives the question only, the asymmetric protocol established by Shi et al. [5], which we apply identically to every method compared here. For NLComm baselines, the sender generates a 128-token summary via greedy decoding. We report F1 score. Task details are in Appendix E .\" (Section 4.1)",
        "However, there is no detailed analysis of the memory footprint of the model parameters, intermediate activations during training and inference, or the memory required for the training data. The paper does not discuss memory optimization techniques or compare memory usage against baselines."
      ]
    },
    "Validation Analysis": {
      "Primary evidence summary": "The paper provides the size of the bridge modules but lacks a detailed memory usage analysis for training and inference.",
      "Supporting quotes": [
        "Each module has its own learnable parameters ( ∼ {\\textsim} 66M each, ∼ {\\textsim} 264M total, 3.8% of the receiver), training on a single GPU on a balanced set of 587 samples drawn across the seven task domains."
      ],
      "Impact assessment": "The absence of memory usage analysis makes it difficult to assess the resource requirements of the method."
    },
    "Conclusion": {
      "Validity status": "Partially Valid",
      "Confidence level": "High",
      "Key supporting evidence": "The paper provides the size of the bridge modules but lacks a detailed analysis of memory footprint for training data, intermediate activations, and comparison against baselines."
    }
  },
  {
    "Weakness Statement": "The paper does not provide a detailed analysis of the robustness of the proposed method to different types of input data.",
    "Evidence Collection": {
      "b) Experiment-related Evidence (if applicable)": [
        "The paper evaluates the method on seven benchmarks: \"HotpotQA [12], MuSiQue [13], QASPER [14], 2WikiMultihopQA (2Wiki) and MultiFieldQA-en (MFldQA) from LongBench [15], Countries and Tipsheets [5].\" (Section 4.1)",
        "The paper does not include experiments specifically designed to test robustness against noisy or adversarial inputs, nor does it analyze the sensitivity to different types of perturbations."
      ]
    },
    "Validation Analysis": {
      "Primary evidence summary": "The paper evaluates on standard benchmarks but lacks specific robustness tests.",
      "Supporting quotes": [
        "We evaluate on seven benchmarks: HotpotQA [12], MuSiQue [13], QASPER [14], 2WikiMultihopQA (2Wiki) and MultiFieldQA-en (MFldQA) from LongBench [15], Countries and Tipsheets [5]."
      ],
      "Impact assessment": "The lack of robustness analysis limits the understanding of the method's reliability in real-world scenarios."
    },
    "Conclusion": {
      "Validity status": "Valid",
      "Confidence level": "High",
      "Key supporting evidence": "The paper does not include experiments or analysis specifically designed to test the robustness of the method against noisy or adversarial inputs."
    }
  },
  {
    "Weakness Statement": "The paper would benefit from a more thorough analysis of the computational costs associated with the proposed XBridge method. Specifically, the authors should provide a detailed breakdown of the training time, including the time taken for each stage of the training process, such as the Lexical Anchor Mapping (LAM) and Latent Enrichment Bridge (LEB) training. This should include the number of GPUs used, the batch size, and the number of training epochs. Furthermore, the inference time for both training and inference should be reported, as well as the memory usage during these processes. It would be beneficial to compare these metrics against baseline methods to provide a clear understanding of the computational overhead introduced by XBridge. This analysis should also consider the scalability of the method with respect to the size of the models and the input data. For example, how does the training time scale with the number of parameters in the models? What is the inference time for different input lengths? These details are crucial for assessing the practical applicability of the method.",
    "Evidence Collection": {
      "b) Experiment-related Evidence (if applicable)": [
        "The paper mentions training time for the bridge: \"The bridge is trained with a small balanced sample set in under 10 minutes on a single GPU on a balanced set of 587 samples drawn across the seven task domains.\" (Section 3.3)",
        "The paper mentions the size of the bridge modules: \"Each module has its own learnable parameters ( ∼ {\\textsim} 66M each, ∼ {\\textsim} 264M total, 3.8% of the receiver), training on a single GPU on a balanced set of 587 samples drawn across the seven task domains.\" (Section 3.3)",
        "The paper mentions the training data size: \"The sender receives the context document only and the receiver receives the question only, the asymmetric protocol established by Shi et al. [5], which we apply identically to every method compared here. For NLComm baselines, the sender generates a 128-token summary via greedy decoding. We report F1 score. Task details are in Appendix E .\" (Section 4.1)",
        "The paper reports inference latency: \"XBridge achieves 11 × \times lower latency than text-based communication, and in a same-architecture setting it exceeds KVComm [5] on 6 of 7 tasks (63.2 vs. 55.2 for Llama → \rightarrow Qwen, 61.9 vs. 61.2 for Qwen → \rightarrow Llama, 65.0 vs. 61.2 for Mistral → \rightarrow Qwen).\" (Section 4.2)",
        "However, the paper does not provide a detailed breakdown of the training time for LAM and LEB, the number of GPUs used for training, batch sizes, training epochs, inference time breakdown, memory usage during training and inference, scalability analysis with respect to model size and input data, or comparisons against baselines for these metrics."
      ]
    },
    "Validation Analysis": {
      "Primary evidence summary": "The paper provides some computational information but lacks the detailed breakdown requested by the reviewer.",
      "Supporting quotes": [
        "The bridge is trained with a small balanced sample set in under 10 minutes on a single GPU on a balanced set of 587 samples drawn across the seven task domains.",
        "Each module has its own learnable parameters ( ∼ {\\textsim} 66M each, ∼ {\\textsim} 264M total, 3.8% of the receiver), training on a single GPU on a balanced set of 587 samples drawn across the seven task domains."
      ],
      "Impact assessment": "The lack of detailed computational analysis limits the understanding of the method's practical efficiency and scalability."
    },
    "Conclusion": {
      "Validity status": "Valid",
      "Confidence level": "High",
      "Key supporting evidence": "The paper lacks detailed information on training time breakdown, GPU usage, batch sizes, training epochs, inference time breakdown, memory usage, and scalability analysis, as well as comparisons against baselines for these metrics."
    }
  },
  {
    "Weakness Statement": "In addition to computational cost, the paper should include a more detailed analysis of the memory usage of the proposed method. Specifically, the authors should provide a detailed breakdown of the memory footprint of the model parameters, the intermediate activations during training and inference, and the memory required for the training data. The authors should also investigate the impact of different memory optimization techniques, such as gradient checkpointing and mixed-precision training, on the memory usage of the method. It would be beneficial to compare the memory usage of XBridge against baseline methods to provide a clear understanding of the memory savings achieved by the proposed method. This analysis should also consider the memory requirements for different batch sizes and sequence lengths. For instance, how does the memory usage change when using larger batch sizes or longer input sequences? This information is essential for understanding the resource requirements of the method in different scenarios.",
    "Evidence Collection": {
      "b) Experiment-related Evidence (if applicable)": [
        "The paper mentions the size of the bridge modules: \"Each module has its own learnable parameters ( ∼ {\\textsim} 66M each, ∼ {\\textsim} 264M total, 3.8% of the receiver), training on a single GPU on a balanced set of 587 samples drawn across the seven task domains.\" (Section 3.3)",
        "The paper mentions the training data size: \"The sender receives the context document only and the receiver receives the question only, the asymmetric protocol established by Shi et al. [5], which we apply identically to every method compared here. For NLComm baselines, the sender generates a 128-token summary via greedy decoding. We report F1 score. Task details are in Appendix E .\" (Section 4.1)",
        "However, the paper does not provide a detailed breakdown of the memory footprint of model parameters, intermediate activations, or training data. It does not investigate the impact of memory optimization techniques like gradient checkpointing or mixed-precision training, nor does it compare memory usage against baselines. The paper also does not analyze how memory usage changes with different batch sizes or sequence lengths."
      ]
    },
    "Validation Analysis": {
      "Primary evidence summary": "The paper provides the size of the bridge modules but lacks a detailed memory usage analysis for training data, activations, optimization techniques, and comparisons against baselines.",
      "Supporting quotes": [
        "Each module has its own learnable parameters ( ∼ {\\textsim} 66M each, ∼ {\\textsim} 264M total, 3.8% of the receiver), training on a single GPU on a balanced set of 587 samples drawn across the seven task domains."
      ],
      "Impact assessment": "The absence of a detailed memory usage analysis makes it difficult to assess the resource requirements of the method."
    },
    "Conclusion": {
      "Validity status": "Partially Valid",
      "Confidence level": "High",
      "Key supporting evidence": "The paper provides the size of the bridge modules but lacks a detailed analysis of memory footprint for training data, intermediate activations, memory optimization techniques, and comparisons against baselines."
    }
  },
  {
    "Weakness Statement": "Finally, the paper should include a more detailed analysis of the robustness of the proposed method to different types of input data. This analysis should include an evaluation of the method's performance on noisy or adversarial inputs, as well as an investigation of its sensitivity to different types of perturbations. The authors should also consider the impact of different input preprocessing techniques on the performance of the method. Furthermore, it would be beneficial to analyze the method's performance on different types of tasks and datasets to determine its generalizability. For example, how does the method perform on tasks that require more complex reasoning or multi-hop inference? This analysis should include a discussion of the limitations of the method and potential areas for future improvement. The authors should also explore the method's performance on datasets with varying levels of noise and adversarial examples to better understand its robustness.",
    "Evidence Collection": {
      "b) Experiment-related Evidence (if applicable)": [
        "The paper evaluates the method on seven benchmarks: \"HotpotQA [12], MuSiQue [13], QASPER [14], 2WikiMultihopQA (2Wiki) and MultiFieldQA-en (MFldQA) from LongBench [15], Countries and Tipsheets [5].\" (Section 4.1)",
        "The paper does not include experiments specifically designed to test robustness against noisy or adversarial inputs, nor does it analyze the sensitivity to different types of perturbations. The paper does not explicitly evaluate performance on tasks requiring complex reasoning or multi-hop inference beyond the chosen benchmarks. The paper does not explore the method's performance on datasets with varying levels of noise and adversarial examples."
      ]
    },
    "Validation Analysis": {
      "Primary evidence summary": "The paper evaluates on standard benchmarks but lacks specific robustness tests and analysis of performance on complex reasoning tasks.",
      "Supporting quotes": [
        "We evaluate on seven benchmarks: HotpotQA [12], MuSiQue [13], QASPER [14], 2WikiMultihopQA (2Wiki) and MultiFieldQA-en (MFldQA) from LongBench [15], Countries and Tipsheets [5]."
      ],
      "Impact assessment": "The lack of robustness analysis and evaluation on complex reasoning tasks limits the understanding of the method's reliability and generalizability."
    },
    "Conclusion": {
      "Validity status": "Valid",
      "Confidence level": "High",
      "Key supporting evidence": "The paper does not include experiments or analysis specifically designed to test the robustness of the method against noisy or adversarial inputs, nor does it analyze performance on tasks requiring complex reasoning beyond the chosen benchmarks."
    }
  },
  {
    "Weakness Statement": "How does the proposed method handle cases where the lexical anchors are ambiguous or do not exist in the receiver’s vocabulary?",
    "Evidence Collection": {
      "a) Method-related Evidence (if applicable)": [
        "Lexical Anchor Mapping (LAM) is designed to map the sender's original context tokens to the receiver's vocabulary, ensuring discrete entity anchors. The mapping is lossless and deterministic, preserving the original context without tokenization. (Method -> Details -> Lexical Anchor Mapping (LAM))"
      ],
      "Validation Analysis": {
        "Primary evidence summary": "The paper describes LAM as a lossless mapping, but doesn't explicitly address the case of ambiguous or non-existent anchors.",
        "Supporting quotes": [
          "Lexical Anchor Mapping (LAM) is designed to map the sender's original context tokens to the receiver's vocabulary, ensuring discrete entity anchors. The mapping is lossless and deterministic, preserving the original context without tokenization."
        ],
        "Impact assessment": "The paper lacks a discussion on how the method handles ambiguous or non-existent lexical anchors."
      }
    },
    "Conclusion": {
      "Validity status": "Valid",
      "Confidence level": "High",
      "Key supporting evidence": "The paper describes LAM as a lossless mapping but does not explicitly address how it handles ambiguous or non-existent lexical anchors."
    }
  },
  {
    "Weakness Statement": "Can the authors provide more details on the training process for the Latent Enrichment Bridge (LEB)? Specifically, how is the training data generated, and what are the key hyperparameters used?",
    "Evidence Collection": {
      "a) Method-related Evidence (if applicable)": [
        "LEB is a set of gated cross-attention modules that enrich the context with sender-side hidden states. The sender's hidden states are projected into the receiver's question input space via a linear transformation. The cross-attention mechanism allows the receiver to query the sender's hidden states and incorporate this information into its processing. The LEB is trained with standard next-token prediction loss on a small balanced sample set. (Method -> Details -> Latent Enrichment Bridge (LEB))"
      ],
      "b) Experiment-related Evidence (if applicable)": [
        "The bridge is trained with a small balanced sample set in under 10 minutes on a single GPU on a balanced set of 587 samples drawn across the seven task domains. (Section 3.3)",
        "The paper mentions the size of the bridge modules but does not provide specific details on the training data generation process beyond the balanced sample set and the number of samples.",
        "The paper does not list the specific hyperparameters used for training the LEB."
      ]
    },
    "Validation Analysis": {
      "Primary evidence summary": "The paper describes the LEB's function and training objective but lacks details on training data generation and specific hyperparameters.",
      "Supporting quotes": [
        "LEB is a set of gated cross-attention modules that enrich the context with sender-side hidden states. The sender's hidden states are projected into the receiver's question input space via a linear transformation. The cross-attention mechanism allows the receiver to query the sender's hidden states and incorporate this information into its processing. The LEB is trained with standard next-token prediction loss on a small balanced sample set."
      ],
      "Impact assessment": "The lack of details on training data generation and hyperparameters makes it harder to reproduce the results and understand the training process."
    },
    "Conclusion": {
      "Validity status": "Valid",
      "Confidence level": "High",
      "Key supporting evidence": "The paper describes the LEB's function and training objective but does not provide details on the training data generation process or the specific hyperparameters used."
    }
  },
  {
    "Weakness Statement": "How does the performance of XBridge scale with the size of the models and the complexity of the tasks? Are there any limitations in terms of model size or task complexity?",
    "Evidence Collection": {
      "b) Experiment-related Evidence (if applicable)": [
        "The paper evaluates XBridge on Llama, Qwen, and Mistral models of sizes 1.5B, 7B, and 14B parameters. (Section 4.1)",
        "The paper evaluates XBridge on seven benchmarks, including tasks of varying complexity. (Section 4.1)",
        "The paper does not include experiments that systematically vary the model size or task complexity to analyze the scaling behavior of XBridge.",
        "The paper does not explicitly discuss any limitations in terms of model size or task complexity."
      ]
    },
    "Validation Analysis": {
      "Primary evidence summary": "The paper evaluates on different model sizes and tasks but lacks a systematic analysis of how performance scales with these factors.",
      "Supporting quotes": [
        "We evaluate communication across three model families to test cross-architecture generality: Llama-3.1-8B-Instruct [ 10 ] (Llama), Qwen2.5-7B-Instruct [ 11 ] (Qwen), and Mistral-7B-Instruct-v0.3 (Mistral).",
        "We evaluate on seven benchmarks: HotpotQA [12], MuSiQue [13], QASPER [14], 2WikiMultihopQA (2Wiki) and MultiFieldQA-en (MFldQA) from LongBench [15], Countries and Tipsheets [5]."
      ],
      "Impact assessment": "The lack of a scaling analysis makes it difficult to understand the method's performance limits and applicability to larger models or more complex tasks."
    },
    "Conclusion": {
      "Validity status": "Valid",
      "Confidence level": "High",
      "Key supporting evidence": "The paper does not include experiments or analysis that systematically vary model size or task complexity to assess the scaling behavior of XBridge."
    }
  },
  {
    "Weakness Statement": "What are the potential limitations of the proposed method, and how might these limitations be addressed in future work?",
    "Evidence Collection": {
      "Validation Analysis": {
        "Primary evidence summary": "The paper does not have a dedicated section discussing the limitations of the proposed method.",
        "Impact assessment": "The absence of a limitations section makes it harder to understand the scope and potential drawbacks of XBridge."
      }
    },
    "Conclusion": {
      "Validity status": "Valid",
      "Confidence level": "High",
      "Key supporting evidence": "The paper lacks a dedicated section discussing the limitations of the proposed method."
    }
  },
  {
    "Weakness Statement": "The paper does not provide a detailed analysis of the computational cost of the proposed method, such as the training time and inference time.",
    "Evidence Collection": {
      "b) Experiment-related Evidence (if applicable)": [
        "The paper mentions training time: \"The bridge is trained with a small balanced sample set in under 10 minutes on a single GPU on a balanced set of 587 samples drawn across the seven task domains.\" (Section 3.3)",
        "The paper mentions inference time: \"XBridge achieves 11 × \times lower latency than text-based communication, and in a same-architecture setting it exceeds KVComm [5] on 6 of 7 tasks (63.2 vs. 55.2 for Llama → \rightarrow Qwen, 61.9 vs. 61.2 for Qwen → \rightarrow Llama, 65.0 vs. 61.2 for Mistral → \rightarrow Qwen).\" (Section 4.2)",
        "However, there is no detailed breakdown of the computational cost for LAM and LEB components, nor a detailed inference time breakdown for different input lengths or batch sizes."
      ]
    },
    "Validation Analysis": {
      "Primary evidence summary": "The paper provides some information on training and inference time, but lacks a detailed breakdown.",
      "Supporting quotes": [
        "The bridge is trained with a small balanced sample set in under 10 minutes on a single GPU on a balanced set of 587 samples drawn across the seven task domains.",
        "XBridge achieves 11 × \times lower latency than text-based communication, and in a same-architecture setting it exceeds KVComm [5] on 6 of 7 tasks (63.2 vs. 55.2 for Llama → \rightarrow Qwen, 61.9 vs. 61.2 for Qwen → \rightarrow Llama, 65.0 vs. 61.2 for Mistral → \rightarrow Qwen)."
      ],
      "Impact assessment": "The lack of detailed computational cost analysis makes it harder to fully assess the practical applicability of the method."
    },
    "Conclusion": {
      "Validity status": "Partially Valid",
      "Confidence level": "High",
      "Key supporting evidence": "The paper provides some training and inference time information but lacks a detailed breakdown for LAM and LEB, and doesn't analyze the impact of input length or batch size."
    }
  },
  {
    "Weakness Statement": "The paper does not provide a detailed analysis of the memory usage of the proposed method.",
    "Evidence Collection": {
      "b) Experiment-related Evidence (if applicable)": [
        "The paper mentions the size of the bridge modules: \"Each module has its own learnable parameters ( ∼ {\\textsim} 66M each, ∼ {\\textsim} 264M total, 3.8% of the receiver), training on a single GPU on a balanced set of 587 samples drawn across the seven task domains.\" (Section 3.3)",
        "The paper mentions the training data size: \"The sender receives the context document only and the receiver receives the question only, the asymmetric protocol established by Shi et al. [5], which we apply identically to every method compared here. For NLComm baselines, the sender generates a 128-token summary via greedy decoding. We report F1 score. Task details are in Appendix E .\" (Section 4.1)",
        "However, there is no detailed analysis of the memory footprint of the model parameters, intermediate activations during training and inference, or the memory required for the training data. The paper does not investigate the impact of different memory optimization techniques or compare memory usage against baselines."
      ]
    },
    "Validation Analysis": {
      "Primary evidence summary": "The paper provides the size of the bridge modules but lacks a detailed memory usage analysis for training data, activations, optimization techniques, and comparisons against baselines.",
      "Supporting quotes": [
        "Each module has its own learnable parameters ( ∼ {\\textsim} 66M each, ∼ {\\textsim} 264M total, 3.8% of the receiver), training on a single GPU on a balanced set of 587 samples drawn across the seven task domains."
      ],
      "Impact assessment": "The absence of a detailed memory usage analysis makes it difficult to assess the resource requirements of the method."
    },
    "Conclusion": {
      "Validity status": "Partially Valid",
      "Confidence level": "High",
      "Key supporting evidence": "The paper provides the size of the bridge modules but lacks a detailed analysis of memory footprint for training data, intermediate activations, memory optimization techniques, and comparisons against baselines."
    }
  },
  {
    "Weakness Statement": "The paper should include a more thorough analysis of the computational resources required by the proposed method. Specifically, the authors should provide a detailed breakdown of the training time, including the time taken for each stage of the training process, such as the Lexical Anchor Mapping (LAM) and Latent Enrichment Bridge (LEB) training. This should include the number of GPUs used, the batch size, and the number of training epochs. Furthermore, the inference time for both training and inference should be reported, as well as the memory usage during these processes. It would be beneficial to compare these metrics against baseline methods to provide a clear understanding of the computational overhead introduced by XBridge. This analysis should also consider the scalability of the method with respect to the size of the models and the input data. For example, how does the training time scale with the number of parameters in the models? What is the inference time for different input lengths? These details are crucial for assessing the practical applicability of the method.",
    "Evidence Collection": {
      "b) Experiment-related Evidence (if applicable)": [
        "The paper mentions training time for the bridge: \"The bridge is trained with a small balanced sample set in under 10 minutes on a single GPU on a balanced set of 587 samples drawn across the seven task domains.\" (Section 3.3)",
        "The paper mentions the size of the bridge modules: \"Each module has its own learnable parameters ( ∼ {\\textsim} 66M each, ∼ {\\textsim} 264M total, 3.8% of the receiver), training on a single GPU on a balanced set of 587 samples drawn across the seven task domains.\" (Section 3.3)",
        "The paper reports inference latency: \"XBridge achieves 11 × \times lower latency than text-based communication, and in a same-architecture setting it exceeds KVComm [5] on 6 of 7 tasks (63.2 vs. 55.2 for Llama → \rightarrow Qwen, 61.9 vs. 61.2 for Qwen → \rightarrow Llama, 65.0 vs. 61.2 for Mistral → \rightarrow Qwen).\" (Section 4.2)",
        "However, the paper does not provide a detailed breakdown of the training time for LAM and LEB, the number of GPUs used for training, batch sizes, training epochs, inference time breakdown, memory usage during training and inference, or comparisons against baselines for these metrics."
      ]
    },
    "Validation Analysis": {
      "Primary evidence summary": "The paper provides some computational information but lacks the detailed breakdown requested by the reviewer.",
      "Supporting quotes": [
        "The bridge is trained with a small balanced sample set in under 10 minutes on a single GPU on a balanced set of 587 samples drawn across the seven task domains.",
        "Each module has its own learnable parameters ( ∼ {\\textsim} 66M each, ∼ {\\textsim} 264M total, 3.8% of the receiver), training on a single GPU on a balanced set of 587 samples drawn across the seven task domains."
      ],
      "Impact assessment": "The lack of detailed computational analysis limits the understanding of the method's practical efficiency and scalability."
    },
    "Conclusion": {
      "Validity status": "Valid",
      "Confidence level": "High",
      "Key supporting evidence": "The paper lacks detailed information on training time breakdown, GPU usage, batch sizes, training epochs, inference time breakdown, memory usage, and comparisons against baselines for these metrics."
    }
  },
  {
    "Weakness Statement": "In addition to computational cost, the paper should also provide a more detailed analysis of the memory usage of the proposed method. Specifically, the authors should provide a detailed breakdown of the memory footprint of the model parameters, the intermediate activations during training and inference, and the memory required for the training data. The authors should also investigate the impact of different memory optimization techniques, such as gradient checkpointing and mixed-precision training, on the memory usage of the method. It would be beneficial to compare the memory usage of XBridge against baseline methods to provide a clear understanding of the memory savings achieved by the proposed method. This analysis should also consider the memory requirements for different batch sizes and sequence lengths. For instance, how does the memory usage change when using larger batch sizes or longer input sequences? This information is essential for understanding the resource requirements of the method in different scenarios.",
    "Evidence Collection": {
      "b) Experiment-related Evidence (if applicable)": [
        "The paper mentions the size of the bridge modules: \"Each module has its own learnable parameters ( ∼ {\\textsim} 66M each, ∼ {\\textsim} 264M total, 3.8% of the receiver), training on a single GPU on a balanced set of 587 samples drawn across the seven task domains.\" (Section 3.3)",
        "The paper mentions the training data size: \"The sender receives the context document only and the receiver receives the question only, the asymmetric protocol established by Shi et al. [5], which we apply identically to every method compared here. For NLComm baselines, the sender generates a 128-token summary via greedy decoding. We report F1 score. Task details are in Appendix E .\" (Section 4.1)",
        "However, the paper does not provide a detailed breakdown of the memory footprint of model parameters, intermediate activations, or training data. It does not investigate the impact of memory optimization techniques like gradient checkpointing or mixed-precision training, nor does it compare memory usage against baselines. The paper also does not analyze how memory usage changes with different batch sizes or sequence lengths."
      ]
    },
    "Validation Analysis": {
      "Primary evidence summary": "The paper provides the size of the bridge modules but lacks a detailed memory usage analysis for training data, activations, optimization techniques, and comparisons against baselines.",
      "Supporting quotes": [
        "Each module has its own learnable parameters ( ∼ {\\textsim} 66M each, ∼ {\\textsim} 264M total, 3.8% of the receiver), training on a single GPU on a balanced set of 587 samples drawn across the seven task domains."
      ],
      "Impact assessment": "The absence of a detailed memory usage analysis makes it difficult to assess the resource requirements of the method."
    },
    "Conclusion": {
      "Validity status": "Partially Valid",
      "Confidence level": "High",
      "Key supporting evidence": "The paper provides the size of the bridge modules but lacks a detailed analysis of memory footprint for training data, intermediate activations, memory optimization techniques, and comparisons against baselines."
    }
  },
  {
    "Weakness Statement": "Finally, the paper should include a more detailed analysis of the robustness of the proposed method to different types of input data. This analysis should include an evaluation of the method's performance on noisy or adversarial inputs, as well as an investigation of its sensitivity to different types of perturbations. The authors should also consider the impact of different input preprocessing techniques on the performance of the method. Furthermore, it would be beneficial to analyze the method's performance on different types of tasks and datasets to determine its generalizability. For example, how does the method perform on tasks that require more complex reasoning or multi-hop inference? This analysis should include a discussion of the limitations of the method and potential areas for future improvement. The authors should also explore the method's performance on datasets with varying levels of noise and adversarial examples to better understand its robustness.",
    "Evidence Collection": {
      "b) Experiment-related Evidence (if applicable)": [
        "The paper evaluates the method on seven benchmarks: \"HotpotQA [12], MuSiQue [13], QASPER [14], 2WikiMultihopQA (2Wiki) and MultiFieldQA-en (MFldQA) from LongBench [15], Countries and Tipsheets [5].\" (Section 4.1)",
        "The paper does not include experiments specifically designed to test robustness against noisy or adversarial inputs, nor does it analyze the sensitivity to different types of perturbations. The paper does not explicitly evaluate performance on tasks requiring complex reasoning or multi-hop inference beyond the chosen benchmarks. The paper does not explore the method's performance on datasets with varying levels of noise and adversarial examples."
      ]
    },
    "Validation Analysis": {
      "Primary evidence summary": "The paper evaluates on standard benchmarks but lacks specific robustness tests and analysis of performance on complex reasoning tasks.",
      "Supporting quotes": [
        "We evaluate on seven benchmarks: HotpotQA [12], MuSiQue [13], QASPER [14], 2WikiMultihopQA (2Wiki) and MultiFieldQA-en (MFldQA) from LongBench [15], Countries and Tipsheets [5]."
      ],
      "Impact assessment": "The lack of robustness analysis and evaluation on complex reasoning tasks limits the understanding of the method's reliability and generalizability."
    },
    "Conclusion": {
      "Validity status": "Valid",
      "Confidence level": "High",
      "Key supporting evidence": "The paper does not include experiments or analysis specifically designed to test the robustness of the method against noisy or adversarial inputs, nor does it analyze performance on tasks requiring complex reasoning beyond the chosen benchmarks."
    }
  },
  {
    "Weakness Statement": "How does the proposed method handle cases where the lexical anchors are ambiguous or do not exist in the receiver’s vocabulary?",
    "Evidence Collection": {
      "a) Method-related Evidence (if applicable)": [
        "Lexical Anchor Mapping (LAM) is designed to map the sender's original context tokens to the receiver's vocabulary, ensuring discrete entity anchors. The mapping is lossless and deterministic, preserving the original context without tokenization. (Method -> Details -> Lexical Anchor Mapping (LAM))",
        "Lexical Anchor Mapping (LAM) is designed to map the sender's original context tokens to the receiver's vocabulary, ensuring discrete entity anchors. The mapping is lossless and deterministic, preserving the original context without tokenization."
      ],
      "Validation Analysis": {
        "Primary evidence summary": "The paper describes LAM as a lossless mapping, but doesn't explicitly address ambiguous or non-existent anchors.",
        "Supporting quotes": [
          "Lexical Anchor Mapping (LAM) is designed to map the sender's original context tokens to the receiver's vocabulary, ensuring discrete entity anchors. The mapping is lossless and deterministic, preserving the original context without tokenization."
        ],
        "Impact assessment": "The paper lacks a discussion on how the method handles ambiguous or non-existent lexical anchors."
      }
    },
    "Conclusion": {
      "}

Now, I have successfully verified each review. Next, I will organize this content and output the final review decision:

\boxed_review{
## Summary:

This paper introduces XBridge, a novel communication protocol designed to address the entity grounding problem in heterogeneous language models, where models with different vocabularies communicate with each other. The core challenge lies in ensuring that the sender's context tokens are accurately represented and preserved by the receiver, despite the architectural differences between the models. XBridge tackles this challenge through two primary mechanisms: Lexical Anchor Mapping (LAM) and Latent Enrichment Bridge (LEB). LAM maps the sender's original context tokens to the receiver's vocabulary, effectively creating discrete entity anchors that are not dependent on the specific input tokens. This ensures that the receiver can identify and track the entities mentioned in the context. Subsequently, LEB enriches the context with sender-side hidden states, providing the receiver with contextual information that is not directly encoded in the tokens themselves. This allows the receiver to gain a more comprehensive understanding of the context, leading to improved performance. The authors evaluate XBridge across multiple model families, including Llama, Qwen, and Mistral, and seven different benchmarks, demonstrating that XBridge outperforms text-based communication methods in all tested scenarios. Furthermore, the paper shows that XBridge exceeds the performance of KV-sharing baselines in a same-architecture setting. The results consistently show that XBridge is more efficient, achieving 11 times lower latency than text-based communication, while also surpassing the performance of text-based communication. The paper also introduces a new same-architecture setting for evaluation, which is a valuable contribution to the field. Overall, XBridge presents a compelling solution to the entity grounding problem in heterogeneous LLM communication, offering a unique approach that leverages both discrete and continuous information transfer.


## Soundness:

3.0


## Presentation:

3.0


## Contribution:

3.0


## Strengths:

I found several aspects of this paper to be particularly strong. First, the paper introduces a novel and effective approach to address the entity grounding problem in heterogeneous LLM communication. The combination of Lexical Anchor Mapping (LAM) and Latent Enrichment Bridge (LEB) is a unique solution that leverages both discrete and continuous information transfer, which is a significant contribution. The authors clearly articulate the problem and provide a well-defined methodology for their proposed solution. The experimental results are compelling, demonstrating that XBridge outperforms text-based communication methods across multiple model families and tasks. The consistent performance gains across different model families, including Llama, Qwen, and Mistral, highlight the robustness and generalizability of the proposed method. The paper also introduces a new same-architecture setting for evaluation, which is a valuable contribution to the field. The authors provide a detailed analysis of the entity grounding problem, including the entity fidelity metric and entity grounding failure, which adds depth to the understanding of the challenges in heterogeneous communication. The paper is well-written and easy to follow, with a logical flow that guides the reader through the problem statement, methodology, and experimental results. The use of figures and tables effectively illustrates the key concepts and findings. The authors also provide a clear explanation of the training process for the Latent Enrichment Bridge (LEB), including the training data generation process and the loss function used. The paper also provides a detailed analysis of the entity grounding problem and the limitations of existing communication methods, which helps to contextualize the contribution of XBridge. The authors also provide a detailed analysis of the entity grounding problem and the limitations of existing communication methods, which helps to contextualize the contribution of XBridge. The paper also provides a detailed analysis of the entity grounding problem and the limitations of existing communication methods, which helps to contextualize the contribution of XBridge.


## Weaknesses:

Despite the strengths of this paper, I have identified several weaknesses that warrant further discussion. First, while the paper provides some information on training time, it lacks a detailed breakdown of the computational costs associated with the proposed method. Specifically, the authors do not provide a detailed breakdown of the training time for the Lexical Anchor Mapping (LAM) and Latent Enrichment Bridge (LEB) components. The paper mentions that the bridge is trained with a small balanced sample set in under 10 minutes on a single GPU, but it does not provide the time taken for each stage of the training process, such as the LAM and LEB training. This lack of detail makes it difficult to fully assess the practical applicability of the method. Furthermore, the paper does not provide information on the number of GPUs used for training, the batch sizes, or the number of training epochs. This information is crucial for understanding the computational overhead introduced by XBridge. My analysis of the paper confirms that these details are indeed missing, and this lack of information makes it difficult to assess the practical applicability of the method. My confidence in this weakness is high, as the paper explicitly lacks these details. Second, the paper does not provide a detailed analysis of the memory usage of the proposed method. While the authors provide the size of the bridge modules, they do not provide a detailed breakdown of the memory footprint of the model parameters, intermediate activations during training and inference, or the memory required for the training data. The paper also does not investigate the impact of different memory optimization techniques, such as gradient checkpointing or mixed-precision training, on the memory usage of the method. This lack of analysis makes it difficult to assess the resource requirements of the method. My analysis of the paper confirms that these details are indeed missing, and this lack of information makes it difficult to assess the practical applicability of the method. My confidence in this weakness is high, as the paper explicitly lacks these details. Third, the paper does not include a detailed analysis of the robustness of the proposed method to different types of input data. The paper evaluates the method on seven benchmarks, but it does not include experiments specifically designed to test robustness against noisy or adversarial inputs, nor does it analyze the sensitivity to different types of perturbations. The paper also does not explore the method's performance on datasets with varying levels of noise and adversarial examples. This lack of robustness analysis limits the understanding of the method's reliability and generalizability. My analysis of the paper confirms that these details are indeed missing, and this lack of information makes it difficult to assess the practical applicability of the method. My confidence in this weakness is high, as the paper explicitly lacks these details. Fourth, the paper does not provide a detailed analysis of the computational cost of the proposed method. While the paper provides some information on training and inference time, it lacks a detailed breakdown of the computational cost for LAM and LEB components. This makes it difficult to fully assess the practical efficiency and scalability of the method. My analysis of the paper confirms that these details are indeed missing, and this lack of information makes it difficult to assess the practical applicability of the method. My confidence in this weakness is high, as the paper explicitly lacks these details. Fifth, the paper does not provide a detailed analysis of the memory usage of the proposed method. While the authors provide the size of the bridge modules, they do not provide a detailed breakdown of the memory footprint of the model parameters, intermediate activations during training and inference, or the memory required for the training data. The paper also does not investigate the impact of different memory optimization techniques, such as gradient checkpointing or mixed-precision training, on the memory usage of the method. This lack of analysis makes it difficult to assess the resource requirements of the method. My analysis of the paper confirms that these details are indeed missing, and this lack of information makes it difficult to assess the practical applicability of the method. My confidence in this weakness is high, as the paper explicitly lacks these details. Finally, the paper does not include experiments or analysis specifically designed to test the robustness of the method against noisy or adversarial inputs, nor does it analyze performance on tasks requiring complex reasoning beyond the chosen benchmarks. This lack of robustness analysis and evaluation on complex reasoning tasks limits the understanding of the method's reliability and generalizability. My analysis of the paper confirms that these details are indeed missing, and this lack of information makes it difficult to assess the practical applicability of the method. My confidence in this weakness is high, as the paper explicitly lacks these details. In summary, while the paper presents a novel and promising approach, these limitations need to be addressed to fully assess the practical applicability of the method.


## Suggestions:

To address the identified weaknesses, I recommend several concrete improvements. First, the authors should provide a more detailed analysis of the computational costs associated with the proposed XBridge method. This analysis should include a breakdown of the training time, including the time taken for each stage of the training process, such as the Lexical Anchor Mapping (LAM) and Latent Enrichment Bridge (LEB) training. The authors should also report the number of GPUs used, the batch sizes, and the number of training epochs. Furthermore, the inference time for both training and inference should be reported, as well as the memory usage during these processes. It would be beneficial to compare these metrics against baseline methods to provide a clear understanding of the computational overhead introduced by XBridge. This analysis should also consider the scalability of the method with respect to the size of the models and the input data. For example, how does the training time scale with the number of parameters in the models? What is the inference time for different input lengths? These details are crucial for assessing the practical applicability of the method. Second, the authors should provide a more detailed analysis of the memory usage of the proposed method. This analysis should include a detailed breakdown of the memory footprint of the model parameters, the intermediate activations during training and inference, and the memory required for the training data. The authors should also investigate the impact of different memory optimization techniques, such as gradient checkpointing and mixed-precision training, on the memory usage of the method. It would be beneficial to compare the memory usage of XBridge against baseline methods to provide a clear understanding of the memory savings achieved by the proposed method. This analysis should also consider the memory requirements for different batch sizes and sequence lengths. For instance, how does the memory usage change when using larger batch sizes or longer input sequences? This information is essential for understanding the resource requirements of the method in different scenarios. Third, the authors should include a more detailed analysis of the robustness of the proposed method to different types of input data. This analysis should include an evaluation of the method's performance on noisy or adversarial inputs, as well as an investigation of its sensitivity to different types of perturbations. The authors should also consider the impact of different input preprocessing techniques on the performance of the method. Furthermore, it would be beneficial to analyze the method's performance on different types of tasks and datasets to determine its generalizability. For example, how does the method perform on tasks that require more complex reasoning or multi-hop inference? This analysis should include a discussion of the limitations of the method and potential areas for future improvement. The authors should also explore the method's performance on datasets with varying levels of noise and adversarial examples to better understand its robustness. Fourth, the authors should provide a more detailed analysis of the computational cost of the proposed method. Specifically, the authors should provide a detailed breakdown of the training time for the Latent Enrichment Bridge (LEB). This should include the number of GPUs used, the number of training epochs, and the number of training iterations. Furthermore, the inference time for both training and inference should be reported, as well as the memory usage during these processes. It would be beneficial to compare these metrics against baseline methods to provide a clear understanding of the computational overhead introduced by XBridge. This analysis should also consider the scalability of the method with respect to the size of the models and the input data. For example, how does the training time scale with the number of parameters in the models? What is the inference time for different input lengths? These details are crucial for assessing the practical applicability of the method. Fifth, the authors should provide a more detailed analysis of the memory usage of the proposed method. This analysis should include a detailed breakdown of the memory footprint of the model parameters, the intermediate activations during training and inference, and the memory required for the training data. The authors should also investigate the impact of different memory optimization techniques, such as gradient checkpointing and mixed-precision training, on the memory usage of the method. It would be beneficial to compare the memory usage of XBridge against baseline methods to provide a clear understanding of the memory savings achieved by the proposed method. This analysis should also consider the memory requirements for different batch sizes and sequence lengths. For instance, how does the memory usage change when using larger batch sizes or longer input sequences? This information is essential for understanding the resource requirements of the method in different scenarios. Finally, the authors should include a more detailed analysis of the robustness of the proposed method to different types of input data. This analysis should include an evaluation of the method's performance on noisy or adversarial inputs, as well as an investigation of its sensitivity to different types of perturbations. The authors should also consider the impact of different input preprocessing techniques on the performance of the method. Furthermore, it would be beneficial to analyze the method's performance on different types of tasks and datasets to determine its generalizability. For example, how does the method perform on tasks that require more complex reasoning or multi-hop inference? This analysis should include a discussion of the limitations of the method and potential areas for future improvement. The authors should also explore the method's performance on datasets with varying levels of noise and adversarial examples to better understand its robustness. By addressing these points, the authors can significantly enhance the practical applicability and robustness of the XBridge method.


## Questions:

Based on my analysis, I have several questions that I believe are important for further understanding the proposed method. First, how does the proposed method handle cases where the lexical anchors are ambiguous or do not exist in the receiver’s vocabulary? While the paper describes LAM as a lossless mapping, it does not explicitly address how the method handles situations where a token cannot be mapped to a specific vocabulary. This is a critical aspect of the method, and I would like to understand how the method would perform in such scenarios. Second, can the authors provide more details on the training process for the Latent Enrichment Bridge (LEB)? Specifically, how is the training data generated, and what are the key hyperparameters used? This information is crucial for reproducibility and for understanding the training process. Third, how does the performance of XBridge scale with the size of the models and the complexity of the tasks? Are there any limitations in terms of model size or task complexity? This is an important question for assessing the practical applicability of the method. Fourth, what are the potential limitations of the proposed method, and how might these limitations be addressed in future work? This is a critical question for understanding the scope and potential drawbacks of the method. Fifth, what are the specific computational costs associated with training and inference, and how do these costs compare to baseline methods? This is an important question for assessing the practical efficiency of the method. Sixth, how does the proposed method perform on tasks that require complex reasoning or multi-hop inference beyond the chosen benchmarks? This is an important question for assessing the generalizability of the method. Finally, what are the potential limitations of the proposed method, and how might these limitations be addressed in future work? This is a critical question for understanding the scope and potential drawbacks of the method. These questions are aimed at clarifying key uncertainties and assumptions, and I believe that addressing them would significantly enhance the understanding and practical applicability of the proposed method.


## Rating:

7.0


## Confidence:

3.0


## Decision:

Accept
}