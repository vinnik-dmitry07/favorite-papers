I will use Standard Mode for comprehensive thinking. As a professional reviewer, I will simulate 4 different reviewers, followed by the verification thinking. Then I will output the Finally Review Output. Let me think - Standard Mode means I will output the original review, followed by the verification thinking. Considering that I am currently in standard mode, I should think from my existing knowledge and consider some related work content when writing about weaknesses. Then I will output the Finally Review Output and Meta Review Output:

\boxed_simreviewers{
## Reviewer 1

### Summary

The paper introduces Meta-Harness, an outer-loop system for optimizing harnesses for large language models (LLMs). It uses an agentic proposer to access a filesystem of prior harnesses, enabling the system to search for effective harnesses across multiple tasks. The system is evaluated on online text classification, math reasoning, and agentic coding, showing improvements over baseline methods.

### Soundness

3

### Presentation

3

### Contribution

3

### Strengths

- The paper introduces a novel approach to harness engineering by using an agentic proposer to search over harness code, allowing for more flexible and effective optimization.
- The system demonstrates significant improvements over baseline methods across multiple tasks, including a 7.7-point increase in online text classification accuracy and a 4.7-point increase in retrieval-augmented math reasoning accuracy.

### Weaknesses

#### Some Related Works


#### comment

 - The paper does not provide a detailed analysis of the computational resources required for the harness search process, which may limit its practical applicability. Specifically, the paper lacks details on the hardware used (e.g., CPU, GPU models, memory), the number of search iterations, and the time taken for each iteration. This information is crucial for assessing the feasibility of the proposed method in resource-constrained environments.
- The paper does not discuss the potential for overfitting to the specific search set, which could impact the generalizability of the discovered harnesses. While the paper mentions using a test set for evaluation, it does not provide a clear methodology for preventing overfitting during the search process, such as using a separate validation set or employing regularization techniques within the search space.
- The paper does not provide a comprehensive comparison with existing methods for harness optimization, making it difficult to assess the relative advantages and disadvantages of the proposed approach. The paper should include a more thorough comparison with other harness optimization techniques, including both manual and automated approaches, to better contextualize the performance of Meta-Harness.

### Suggestions

To address the lack of detail regarding computational resources, the authors should provide a comprehensive breakdown of the hardware specifications used for the experiments, including the CPU, GPU models, and memory. They should also specify the number of search iterations performed, the time taken for each iteration, and the total time required to complete the harness search. This information is essential for other researchers to replicate the experiments and assess the practical applicability of the proposed method. Furthermore, the authors should discuss the scalability of the method with respect to the size of the search space and the number of available resources. For example, they could analyze how the search time scales with the number of prior harnesses stored on the filesystem. This would provide a better understanding of the computational cost associated with the proposed approach and its limitations.

To mitigate the risk of overfitting, the authors should implement a more rigorous validation strategy. This could involve using a separate validation set that is distinct from both the search set and the evaluation set. The validation set could be used to monitor the performance of the discovered harnesses during the search process and to stop the search when the performance on the validation set starts to degrade. This would help to prevent the method from overfitting to the specific search set and ensure that the discovered harnesses generalize well to unseen data. Additionally, the authors should explore techniques such as early stopping or regularization to further improve the generalization performance of the method. The paper should also include a discussion of the potential limitations of the validation strategy and how these limitations could be addressed in future work.

Finally, the authors should provide a more comprehensive comparison with existing methods for harness optimization. This comparison should include both manual and automated approaches, and it should focus on the relative advantages and disadvantages of each method. The authors should also discuss the specific scenarios in which Meta-Harness is expected to outperform existing methods and the scenarios in which it may not be as effective. This would provide a better understanding of the strengths and weaknesses of the proposed approach and its potential impact on the field. The comparison should also include a discussion of the computational cost and the complexity of implementation for each method. This would allow researchers to make informed decisions about which method is most suitable for their specific needs.

### Questions

- How does the computational cost of the harness search process scale with the size of the search space and the number of available resources?
- What measures are in place to prevent overfitting to the specific search set, and how is the generalizability of the discovered harnesses ensured?
- How does the performance of Meta-Harness compare to other state-of-the-art harness optimization methods, and what are the specific scenarios in which it is expected to outperform them?

### Rating

6

### Confidence

3

**********

## Reviewer 2

### Summary

The paper introduces Meta-Harness, an outer-loop system for harness optimization that automates the process of refining harness code for large language models (LLMs). Unlike traditional text optimizers that compress feedback into summaries or templates, Meta-Harness allows a coding agent to inspect and modify harness code, execution traces, and scores from prior attempts. This enables more flexible and effective optimization by leveraging selective diagnostic access to past experiences. The system uses a file system to store prior harnesses and allows the coding agent to modify harnesses based on feedback from prior attempts. Meta-Harness is evaluated on three tasks: online text classification, retrieval-augmented math reasoning, and agentic coding. It demonstrates significant improvements over baseline methods, including a 7.7-point increase in online text classification accuracy and a 4.7-point increase in retrieval-augmented math reasoning accuracy. The paper also highlights the benefits of full access to prior experience compared to methods that rely on compressed feedback.

### Soundness

3

### Presentation

3

### Contribution

3

### Strengths

Originality: The paper introduces a novel approach to harness engineering by automating the optimization process using a coding agent that has selective access to prior experience. This is a significant departure from traditional text optimizers that rely on compressed feedback.

Quality: The paper presents a well-structured and thorough evaluation of Meta-Harness across multiple tasks, including online text classification, retrieval-augmented math reasoning, and agentic coding. The results demonstrate the effectiveness of the proposed approach, with significant improvements over baseline methods.

Clarity: The paper is well-written and easy to follow, with clear explanations of the methodology and experimental setup. The use of figures and tables helps to illustrate the key concepts and results.

Significance: The paper addresses a critical challenge in harness engineering, which is the manual optimization of harness code. By automating this process, Meta-Harness has the potential to significantly improve the performance of LLMs in various applications.

### Weaknesses

#### Some Related Works


#### comment

Limited Comparison with State-of-the-Art Methods: While the paper demonstrates the effectiveness of Meta-Harness, it would be beneficial to compare it with more state-of-the-art methods in harness engineering. This would provide a more comprehensive evaluation of the proposed approach and highlight its strengths and weaknesses relative to existing techniques.

Lack of Analysis of Failure Cases: The paper does not provide a detailed analysis of failure cases, which could provide valuable insights into the limitations of the proposed approach. Understanding the reasons for failures could help to identify areas for improvement and guide future research.

### Suggestions

To strengthen the paper, a more thorough comparison with existing state-of-the-art methods in harness engineering is needed. Specifically, the paper should benchmark Meta-Harness against methods that utilize more sophisticated optimization techniques, such as reinforcement learning or evolutionary algorithms, rather than just simpler text optimization methods. This would provide a more rigorous evaluation of Meta-Harness's performance and highlight its unique advantages. For example, comparing against methods that use policy gradient techniques or genetic algorithms could reveal whether the proposed approach is truly superior or if it is simply more effective than the chosen baselines. Furthermore, the comparison should not only focus on the final performance metrics but also consider the computational cost and resource requirements of each method. This would provide a more complete picture of the trade-offs involved in using Meta-Harness.

In addition to a more comprehensive comparison, the paper should include a detailed analysis of failure cases. This analysis should go beyond simply reporting the number of failures and should delve into the underlying reasons for these failures. For instance, the paper could investigate whether failures are more common in specific types of tasks or with certain types of LLMs. This could involve analyzing the types of errors made by the system, the characteristics of the input data, and the specific harness code that leads to failures. Such an analysis would provide valuable insights into the limitations of Meta-Harness and could guide future research in this area. For example, if failures are more common when using smaller LLMs, this could suggest that the optimization process needs to be adapted for different model sizes. Similarly, if errors are related to specific types of input, this could indicate that the harness code needs to be more robust to such inputs.

Finally, the paper should explore the impact of different design choices on the performance of Meta-Harness. For example, the paper could investigate the effect of the size of the file system used to store prior experiences, the frequency of code modifications, and the specific algorithms used for code generation and optimization. This could involve conducting ablation studies to determine which components of the system are most critical for its performance. Such an analysis would provide a deeper understanding of the inner workings of Meta-Harness and could lead to further improvements in its design. For instance, the paper could explore the impact of different file system access patterns on the efficiency of the optimization process, or the effect of different code generation strategies on the quality of the optimized harness.

### Questions

How does Meta-Harness compare to state-of-the-art methods in harness engineering, particularly those that use more sophisticated optimization techniques?

What are the limitations of Meta-Harness, and in what scenarios does it perform poorly? Could you provide more insights into the failure cases?

Could you provide more details on the computational cost of the proposed approach? How does it scale with the size of the search space and the number of available resources?

### Rating

6

### Confidence

3

**********

## Reviewer 3

### Summary

This paper introduces a new approach to harness engineering, which involves optimizing harnesses for LLMs. The authors propose a system called Meta-Harness, which uses an agentic proposer to search over harness code for LLM applications. The key innovation is allowing the proposer to access a file system of prior harnesses and inspect execution traces, which enables more flexible and effective optimization. The paper evaluates Meta-Harness on three tasks: online text classification, math reasoning, and agentic coding. The results show that Meta-Harness achieves state-of-the-art performance on these tasks, outperforming existing methods by a significant margin.

### Soundness

3

### Presentation

3

### Contribution

3

### Strengths

- The paper introduces a novel approach to harness engineering that has the potential to significantly improve the performance of LLMs in various applications.
- The proposed system, Meta-Harness, is well-designed and effectively leverages selective access to prior experience to enable more flexible and effective optimization.
- The paper provides a thorough evaluation of Meta-Harness across multiple tasks, demonstrating its effectiveness and robustness.
- The paper is well-written and easy to follow, with clear explanations of the methodology and experimental setup.

### Weaknesses

#### Some Related Works


#### comment

 - The paper does not provide a detailed analysis of the computational resources required for the harness search process, which may limit its practical applicability. Specifically, the paper lacks details on the hardware used (e.g., CPU, GPU models, memory), the number of search iterations, and the time taken for each iteration. This information is crucial for assessing the feasibility of the proposed method in resource-constrained environments.
- The paper does not discuss the potential for overfitting to the specific search set, which could impact the generalizability of the discovered harnesses. While the paper mentions using a test set for evaluation, it does not provide a clear methodology for preventing overfitting during the search process, such as using a separate validation set or employing regularization techniques within the search space.
- The paper does not provide a comprehensive comparison with existing methods for harness optimization, making it difficult to assess the relative advantages and disadvantages of the proposed approach. The paper should include a more thorough comparison with other harness optimization techniques, including both manual and automated approaches, to better contextualize the performance of Meta-Harness.

### Suggestions

The paper should provide a more detailed analysis of the computational resources required for the harness search process. This should include specifics on the hardware used (e.g., CPU model, GPU model, memory), the number of search iterations performed, and the time taken for each iteration. This information is essential for other researchers to replicate the experiments and assess the practical applicability of the proposed method. Furthermore, the authors should discuss the scalability of the method with respect to the size of the search space and the number of available resources. For example, how does the search time scale with the number of prior harnesses stored on the filesystem? This would provide a better understanding of the computational cost associated with the proposed approach and its limitations.

To address the potential for overfitting, the authors should implement a more rigorous validation strategy. This could involve using a separate validation set that is distinct from both the search set and the evaluation set. The validation set could be used to monitor the performance of the discovered harnesses during the search process and to stop the search when the performance on the validation set starts to degrade. This would help to prevent the method from overfitting to the specific search set and ensure that the discovered harnesses generalize well to unseen data. Additionally, the authors should explore techniques such as early stopping or regularization to further improve the generalization performance of the method. The paper should also include a discussion of the potential limitations of the validation strategy and how these limitations could be addressed in future work.

Finally, the paper should include a more comprehensive comparison with existing methods for harness optimization. This comparison should include both manual and automated approaches, and it should focus on the relative advantages and disadvantages of each method. The authors should discuss the specific scenarios in which Meta-Harness is expected to outperform existing methods and the scenarios in which it may not be as effective. This would provide a better understanding of the strengths and weaknesses of the proposed approach and its potential impact on the field. The comparison should also include a discussion of the computational cost and the complexity of implementation for each method. This would allow researchers to make informed decisions about which method is most suitable for their specific needs.

### Questions

- How does the performance of Meta-Harness vary with different base models? Are there any specific models where it performs particularly well or poorly?
- How does the size of the prior experience affect the performance of Meta-Harness? Is there a point of diminishing returns?
- What are the limitations of the current approach, and what are the potential directions for future research?

### Rating

6

### Confidence

3

**********

## Reviewer 4

### Summary

The paper presents a novel system for harness optimization, Meta-Harness, which leverages a coding agent to search over harness code for LLM applications. The system uses an agentic proposer that accesses a file system of prior harnesses, enabling selective diagnosis and modification of harness code. The paper evaluates Meta-Harness on three tasks: online text classification, math reasoning, and agentic coding, demonstrating significant improvements over baseline methods.

### Soundness

3

### Presentation

3

### Contribution

3

### Strengths

- The paper introduces a novel approach to harness engineering by automating the optimization process using a coding agent that has selective access to prior experience. This is a significant departure from traditional text optimizers that rely on compressed feedback.
- The paper presents a comprehensive evaluation of Meta-Harness across multiple tasks, including online text classification, retrieval-augmented math reasoning, and agentic coding. The results demonstrate the effectiveness of the proposed approach, with significant improvements over baseline methods.
- The paper is well-written and easy to follow, with clear explanations of the methodology and experimental setup. The use of figures and tables helps to illustrate the key concepts and results.

### Weaknesses

#### Some Related Works


#### comment

 - The paper does not provide a detailed analysis of the computational resources required for the harness search process, which may limit its practical applicability. Specifically, the paper lacks details on the hardware used (e.g., CPU, GPU models, memory), the number of search iterations, and the time taken for each iteration. This information is crucial for assessing the feasibility of the proposed method in resource-constrained environments.
- The paper does not discuss the potential for overfitting to the specific search set, which could impact the generalizability of the discovered harnesses. While the paper mentions using a test set for evaluation, it does not provide a clear methodology for preventing overfitting during the search process, such as using a separate validation set or employing regularization techniques within the search space.
- The paper does not provide a comprehensive comparison with existing methods for harness optimization, making it difficult to assess the relative advantages and disadvantages of the proposed approach. The paper should include a more thorough comparison with other harness optimization techniques, including both manual and automated approaches, to better contextualize the performance of Meta-Harness.

### Suggestions

The paper would benefit from a more thorough analysis of the computational resources required for the harness search process. The authors should provide specific details on the hardware used, including the CPU model, GPU model, memory, and the number of available cores. Furthermore, the paper should include a detailed breakdown of the time taken for each iteration of the search process, as well as the total time required to complete the harness search. This information is crucial for assessing the practical applicability of the proposed method, especially in resource-constrained environments. The authors should also discuss the scalability of the method with respect to the size of the search space and the number of available resources. For example, how does the search time scale with the number of prior harnesses stored on the filesystem? This would provide a better understanding of the computational cost associated with the proposed approach and its limitations.

To address the potential for overfitting, the authors should implement a more rigorous validation strategy. This could involve using a separate validation set that is distinct from both the search set and the evaluation set. The validation set could be used to monitor the performance of the discovered harnesses during the search process and to stop the search when the performance on the validation set starts to degrade. This would help to prevent the method from overfitting to the specific search set and ensure that the discovered harnesses generalize well to unseen data. Additionally, the authors should explore techniques such as early stopping or regularization to further improve the generalization performance of the method. The paper should also include a discussion of the potential limitations of the validation strategy and how these limitations could be addressed in future work.

Finally, the paper should include a more comprehensive comparison with existing methods for harness optimization. This comparison should include both manual and automated approaches, and it should focus on the relative advantages and disadvantages of each method. The authors should discuss the specific scenarios in which Meta-Harness is expected to outperform existing methods and the scenarios in which it may not be as effective. This would provide a better understanding of the strengths and weaknesses of the proposed approach and its potential impact on the field. The comparison should also include a discussion of the computational cost and the complexity of implementation for each method. This would allow researchers to make informed decisions about which method is most suitable for their specific needs.

### Questions

- How does the performance of Meta-Harness vary with different base models? Are there any specific models where it performs particularly well or poorly?
- How does the size of the prior experience affect the performance of Meta-Harness? Is there a point of diminishing returns?
- What are the limitations of the current approach, and what are the potential directions for future research?

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
1. Go through each reviewer's comments one by one.
2. For each comment identified as a weakness, find the corresponding section in the paper.
3. Extract evidence (quotes, experimental details, missing citations) to support the reviewer's claim.
4. If the weakness is about missing information, check if that information is indeed absent.
5. If there are conflicting opinions, note them down.
6. Finally, summarize the findings for each weakness, stating if it's valid, partially valid, or invalid, and provide the supporting evidence.
```json
[
  {
    "Weakness Statement": "The paper does not provide a detailed analysis of the computational resources required for the harness search process, which may limit its practical applicability. Specifically, the paper lacks details on the hardware used (e.g., CPU, GPU models, memory), the number of search iterations, and the time taken for each iteration. This information is crucial for assessing the feasibility of the proposed method in resource-constrained environments.",
    "Evidence Collection": {
      "b) Experiment-related Evidence (if applicable)": [
        "The paper mentions the use of Claude Code for the proposer and Opus-4.6 for the base model but does not specify the hardware used for the experiments.",
        "The paper states the number of candidates evaluated in each iteration (e.g., 40 candidates in the online text classification experiment) but does not provide the total number of iterations or the time taken for each iteration.",
        "There is no discussion on the computational cost or scalability of the method with respect to the size of the search space or the number of available resources."
      ]
    },
    "Literature Gap Analysis": [],
    "Validation Analysis": {
      "Primary evidence summary": "The paper lacks specific details on hardware specifications, the number of search iterations, and the time taken for each iteration.",
      "Supporting quotes": [
        "We use Claude Code [5] with Opus-4.6 . The proposer is guided by a minimal domain-specific skill that describes where to write new harnesses, how to inspect previous harnesses and their execution traces, and what files it can and cannot modify.",
        "In our experiments, a typical run evaluates roughly 60 harnesses over 20 iterations."
      ],
      "Impact assessment": "The absence of these details makes it difficult to assess the practical applicability and scalability of the proposed method."
    },
    "Conclusion": {
      "Validity status": "Valid",
      "Confidence level": "High",
      "Key supporting evidence": "The paper does not provide specific hardware details, the exact number of iterations, or the time taken per iteration."
    }
  },
  {
    "Weakness Statement": "The paper does not discuss the potential for overfitting to the specific search set, which could impact the generalizability of the discovered harnesses. While the paper mentions using a test set for evaluation, it does not provide a clear methodology for preventing overfitting during the search process, such as using a separate validation set or employing regularization techniques within the search space.",
    "Evidence Collection": {
      "b) Experiment-related Evidence (if applicable)": [
        "The paper mentions using a test set for evaluation in the online text classification experiment: \"We evaluate this harness on 200 200 previously unseen IMO-level problems drawn from IMO-AnswerBench, IMO-ProofBench, and ArXivMath [30 ; 6].\"",
        "The paper does not explicitly describe the creation or use of a separate validation set during the search process.",
        "The paper does not discuss any regularization techniques applied to the search process."
      ]
    },
    "Literature Gap Analysis": [],
    "Validation Analysis": {
      "Primary evidence summary": "The paper uses a test set for evaluation but lacks details on a separate validation set for preventing overfitting during the search and any regularization techniques used.",
      "Supporting quotes": [
        "We evaluate this harness on 200 200 previously unseen IMO-level problems drawn from IMO-AnswerBench, IMO-ProofBench, and ArXivMath [30 ; 6]."
      ],
      "Impact assessment": "The lack of a clear methodology for preventing overfitting could lead to the discovered harnesses being overly specialized to the search set and not generalizing well."
    },
    "Conclusion": {
      "Validity status": "Valid",
      "Confidence level": "High",
      "Key supporting evidence": "The paper does not describe the use of a separate validation set or discuss regularization techniques during the search process."
    }
  },
  {
    "Weakness Statement": "The paper does not provide a comprehensive comparison with existing methods for harness optimization, making it difficult to assess the relative advantages and disadvantages of the proposed approach. The paper should include a more thorough comparison with other harness optimization techniques, including both manual and automated approaches, to better contextualize the performance of Meta-Harness.",
    "Evidence Collection": {
      "b) Experiment-related Evidence (if applicable)": [
        "The paper compares Meta-Harness against 'Best-of-N', 'OpenEvolve', 'ACE', and 'MCE' baselines in the online text classification experiment.",
        "The paper compares Meta-Harness against 'No retrieval', 'Dense retrieval using the separate embedding model text-embedding-3-small', 'Random few-shot prompting', and 'BM25 retrieval' in the math reasoning experiment.",
        "The paper compares Meta-Harness against 'Terminus 2', 'Terminus-KIRA', and 'Goose' baselines in the agentic coding experiment.",
        "While the paper includes comparisons with several baselines, it does not explicitly compare against a broader range of 'manual' harness optimization techniques or provide a detailed analysis of the specific advantages and disadvantages of Meta-Harness compared to these methods."
      ]
    },
    "Literature Gap Analysis": [],
    "Validation Analysis": {
      "Primary evidence summary": "The paper compares against several automated baselines but lacks a comprehensive comparison with a wider range of manual harness optimization techniques.",
      "Supporting quotes": [
        "We compare against two main classes of methods. (1) Human-designed strategies : these are hand-crafted harnesses for each domain, representing the current state of the art in context construction. We describe these baselines in the corresponding subsections. (2) Program-search methods: these methods search over executable code for functions, workflows, or agent designs. ... We consider the following points of comparison: • Best-of-N : independent samples from the seed with no search structure; a compute-matched control for whether search matters at all.",
        "We compare against representative methods for optimizing text. For a fair comparison, we use the same proposer configuration ( Opus-4.6 with max reasoning), select candidates solely based on search-set performance, and hold out the test sets until the final evaluation. Since evaluation is the main computational bottleneck, we give each method the same budget of proposal harness evaluations. We consider the following points of comparison: • No retrieval, few-shot prompting, and BM25 retrieval."
      ],
      "Impact assessment": "Without a more comprehensive comparison, it's harder to fully understand the novelty and effectiveness of Meta-Harness relative to the broader landscape of harness optimization."
    },
    "Conclusion": {
      "Validity status": "Partially Valid",
      "Confidence level": "High",
      "Key supporting evidence": "The paper compares against several automated baselines but lacks a broader comparison with manual harness optimization techniques."
    }
  },
  {
    "Weakness Statement": "How does the performance of Meta-Harness vary with different base models? Are there any specific models where it performs particularly well or poorly?",
    "Evidence Collection": {
      "b) Experiment-related Evidence (if applicable)": [
        "The paper mentions using Claude Code with Opus-4.6 as the proposer.",
        "The paper does not present experiments or results using different base models for the proposer."
      ]
    },
    "Literature Gap Analysis": [],
    "Validation Analysis": {
      "Primary evidence summary": "The paper uses Claude Code with Opus-4.6 but does not explore the performance of Meta-Harness with other base models.",
      "Supporting quotes": [
        "We use Claude Code [5] with Opus-4.6 ."
      ],
      "Impact assessment": "The lack of experiments with different base models leaves a gap in understanding the robustness and generalizability of Meta-Harness across different LLM architectures."
    },
    "Conclusion": {
      "Validity status": "Valid",
      "Confidence level": "High",
      "Key supporting evidence": "The paper only reports results using Claude Code with Opus-4.6."
    }
  },
  {
    "Weakness Statement": "How does the size of the prior experience affect the performance of Meta-Harness? Is there a point of diminishing returns?",
    "Evidence Collection": {
      "b) Experiment-related Evidence (if applicable)": [
        "The paper mentions the size of the search set in the online text classification experiment (200 IMO-level problems) and the agentic coding experiment (89-task benchmark).",
        "The paper does not systematically vary the size of the prior experience to analyze its impact on performance."
      ]
    },
    "Literature Gap Analysis": [],
    "Validation Analysis": {
      "Primary evidence summary": "The paper uses a specific size for the prior experience but does not analyze how varying this size affects the performance of Meta-Harness.",
      "Supporting quotes": [
        "We evaluate this harness on 200 200 previously unseen IMO-level problems drawn from IMO-AnswerBench, IMO-ProofBench, and ArXivMath [30 ; 6].",
        "We evaluate the harness on the full benchmark in Table 7 , evaluated on two base models: Claude Opus 4.6 and Claude Haiku 4.5 ."
      ],
      "Impact assessment": "Without analyzing the impact of prior experience size, it's difficult to understand the scalability and efficiency of the search process."
    },
    "Conclusion": {
      "Validity status": "Valid",
      "Confidence level": "High",
      "Key supporting evidence": "The paper does not include experiments systematically varying the size of the prior experience."
    }
  },
  {
    "Weakness Statement": "What are the limitations of the current approach, and what are the potential directions for future research?",
    "Evidence Collection": {
      "b) Experiment-related Evidence (if applicable)": [
        "The paper mentions a limitation in the agentic coding experiment: \"We note that although the resulting harness is specialized to the TerminalBench-2 regime, autonomous completion of difficult long-horizon tasks from a single instruction is a core capability, and the benchmark consists of many tasks that frontier models and heavily engineered harnesses struggle with.\"",
        "The paper does not explicitly dedicate a section to discussing the limitations of Meta-Harness in general or provide a comprehensive overview of potential future research directions beyond the specific experiments conducted."
      ]
    },
    "Literature Gap Analysis": [],
    "Validation Analysis": {
      "Primary evidence summary": "The paper acknowledges a limitation in one specific experiment but lacks a broader discussion of the limitations of the Meta-Harness approach and potential future research directions.",
      "Supporting quotes": [
        "We note that although the resulting harness is specialized to the TerminalBench-2 regime, autonomous completion of difficult long-horizon tasks from a single instruction is a core capability, and the benchmark consists of many tasks that frontier models and heavily engineered harnesses struggle with."
      ],
      "Impact assessment": "The absence of a comprehensive discussion on limitations and future directions makes it harder to understand the scope and potential impact of the work."
    },
    "Conclusion": {
      "Validity status": "Valid",
      "Confidence level": "High",
      "Key supporting evidence": "The paper lacks a dedicated section discussing the general limitations of Meta-Harness and potential future research directions."
    }
  },
  {
    "Weakness Statement": "The paper does not provide a detailed analysis of the computational resources required for the harness search process, which may limit its practical applicability. Specifically, the paper lacks details on the hardware used (e.g., CPU, GPU models, memory), the number of search iterations, and the time taken for each iteration. This information is crucial for assessing the feasibility of the proposed method in resource-constrained environments.",
    "Evidence Collection": {
      "b) Experiment-related Evidence (if applicable)": [
        "The paper mentions the use of Claude Code for the proposer and Opus-4.6 for the base model but does not specify the hardware used for the experiments.",
        "The paper states the number of candidates evaluated in each iteration (e.g., 40 candidates in the online text classification experiment) but does not provide the total number of iterations or the time taken for each iteration.",
        "There is no discussion on the computational cost or scalability of the method with respect to the size of the search space or the number of available resources."
      ]
    },
    "Literature Gap Analysis": [],
    "Validation Analysis": {
      "Primary evidence summary": "The paper lacks specific details on hardware specifications, the number of search iterations, and the time taken for each iteration.",
      "Supporting quotes": [
        "We use Claude Code [5] with Opus-4.6 . The proposer is guided by a minimal domain-specific skill that describes where to write new harnesses, how to inspect previous harnesses and their execution traces, and what files it can and cannot modify.",
        "In our experiments, a typical run evaluates roughly 60 harnesses over 20 iterations."
      ],
      "Impact assessment": "The absence of these details makes it difficult to assess the practical applicability and scalability of the proposed method."
    },
    "Conclusion": {
      "Validity status": "Valid",
      "Confidence level": "High",
      "Key supporting evidence": "The paper does not provide specific hardware details, the exact number of iterations, or the time taken per iteration."
    }
  },
  {
    "Weakness Statement": "The paper does not discuss the potential for overfitting to the specific search set, which could impact the generalizability of the discovered harnesses. While the paper mentions using a test set for evaluation, it does not provide a clear methodology for preventing overfitting during the search process, such as using a separate validation set or employing regularization techniques within the search space.",
    "Evidence Collection": {
      "b) Experiment-related Evidence (if applicable)": [
        "The paper mentions using a test set for evaluation in the online text classification experiment: \"We evaluate this harness on 200 200 previously unseen IMO-level problems drawn from IMO-AnswerBench, IMO-ProofBench, and ArXivMath [30 ; 6].\"",
        "The paper does not explicitly describe the creation or use of a separate validation set during the search process.",
        "The paper does not discuss any regularization techniques applied to the search process."
      ]
    },
    "Literature Gap Analysis": [],
    "Validation Analysis": {
      "Primary evidence summary": "The paper uses a test set for evaluation but lacks details on a separate validation set for preventing overfitting during the search and any regularization techniques used.",
      "Supporting quotes": [
        "We evaluate this harness on 200 200 previously unseen IMO-level problems drawn from IMO-AnswerBench, IMO-ProofBench, and ArXivMath [30 ; 6]."
      ],
      "Impact assessment": "The lack of a clear methodology for preventing overfitting could lead to the discovered harnesses being overly specialized to the search set and not generalizing well."
    },
    "Conclusion": {
      "Validity status": "Valid",
      "Confidence level": "High",
      "Key supporting evidence": "The paper does not describe the use of a separate validation set or discuss regularization techniques during the search process."
    }
  },
  {
    "Weakness Statement": "The paper does not provide a comprehensive comparison with existing methods for harness optimization, making it difficult to assess the relative advantages and disadvantages of the proposed approach. The paper should include a more thorough comparison with other harness optimization techniques, including both manual and automated approaches, to better contextualize the performance of Meta-Harness.",
    "Evidence Collection": {
      "b) Experiment-related Evidence (if applicable)": [
        "The paper compares Meta-Harness against 'Best-of-N', 'OpenEvolve', 'ACE', and 'MCE' baselines in the online text classification experiment.",
        "The paper compares Meta-Harness against 'No retrieval', 'Dense retrieval using the separate embedding model text-embedding-3-small', 'Random few-shot prompting', and 'BM25 retrieval' in the math reasoning experiment.",
        "The paper compares Meta-Harness against 'Terminus 2', 'Terminus-KIRA', and 'Goose' baselines in the agentic coding experiment.",
        "While the paper includes comparisons with several baselines, it does not explicitly compare against a broader range of manual harness optimization techniques or provide a detailed analysis of the specific advantages and disadvantages of Meta-Harness compared to these methods."
      ]
    },
    "Literature Gap Analysis": [],
    "Validation Analysis": {
      "Primary evidence summary": "The paper compares against several automated baselines but lacks a comprehensive comparison with a wider range of manual harness optimization techniques.",
      "Supporting quotes": [
        "We compare against two main classes of methods. (1) Human-designed strategies : these are hand-crafted harnesses for each domain, representing the current state of the art in context construction. We describe these baselines in the corresponding subsections. (2) Program-search methods: these methods search over executable code for functions, workflows, or agent designs. ... We consider the following points of comparison: • Best-of-N : independent samples from the seed with no search structure; a compute-matched control for whether search matters at all.",
        "We compare against representative methods for optimizing text. For a fair comparison, we use the same proposer configuration ( Opus-4.6 with max reasoning), select candidates solely based on search-set performance, and hold out the test sets until the final evaluation. Since evaluation is the main computational bottleneck, we give each method the same budget of proposal harness evaluations. We consider the following points of comparison: • No retrieval, few-shot prompting, and BM25 retrieval."
      ],
      "Impact assessment": "Without a more comprehensive comparison, it's harder to fully understand the novelty and effectiveness of Meta-Harness relative to the broader landscape of harness optimization."
    },
    "Conclusion": {
      "Validity status": "Partially Valid",
      "Confidence level": "High",
      "Key supporting evidence": "The paper compares against several automated baselines but lacks a broader comparison with manual harness optimization techniques."
    }
  },
  {
    "Weakness Statement": "The paper does not provide a detailed analysis of the computational resources required for the harness search process, which may limit its practical applicability. Specifically, the paper lacks details on the hardware used (e.g., CPU, GPU models, memory), the number of search iterations, and the time taken for each iteration. This information is crucial for assessing the feasibility of the proposed method in resource-constrained environments.",
    "Evidence Collection": {
      "b) Experiment-related Evidence (if applicable)": [
        "The paper mentions the use of Claude Code for the proposer and Opus-4.6 for the base model but does not specify the hardware used for the experiments.",
        "The paper states the number of candidates evaluated in each iteration (e.g., 40 candidates in the online text classification experiment) but does not provide the total number of iterations or the time taken for each iteration.",
        "There is no discussion on the computational cost or scalability of the method with respect to the size of the search space or the number of available resources."
      ]
    },
    "Literature Gap Analysis": [],
    "Validation Analysis": {
      "Primary evidence summary": "The paper lacks specific details on hardware specifications, the number of search iterations, and the time taken for each iteration.",
      "Supporting quotes": [
        "We use Claude Code [5] with Opus-4.6 . The proposer is guided by a minimal domain-specific skill that describes where to write new harnesses, how to inspect previous harnesses and their execution traces, and what files it can and cannot modify.",
        "In our experiments, a typical run evaluates roughly 60 harnesses over 20 iterations."
      ],
      "Impact assessment": "The absence of these details makes it difficult to assess the practical applicability and scalability of the proposed method."
    },
    "Conclusion": {
      "Validity status": "Valid",
      "Confidence level": "High",
      "Key supporting evidence": "The paper does not provide specific hardware details, the exact number of iterations, or the time taken per iteration."
    }
  },
  {
    "Weakness Statement": "The paper does not discuss the potential for overfitting to the specific search set, which could impact the generalizability of the discovered harnesses. While the paper mentions using a test set for evaluation, it does not provide a clear methodology for preventing overfitting during the search process, such as using a separate validation set or employing regularization techniques within the search space.",
    "Evidence Collection": {
      "b) Experiment-related Evidence (if applicable)": [
        "The paper mentions using a test set for evaluation in the online text classification experiment: \"We evaluate this harness on 200 200 previously unseen IMO-level problems drawn from IMO-AnswerBench, IMO-ProofBench, and ArXivMath [30 ; 6].\"",
        "The paper does not explicitly describe the creation or use of a separate validation set during the search process.",
        "The paper does not discuss any regularization techniques applied to the search process."
      ]
    },
    "Literature Gap Analysis": [],
    "Validation Analysis": {
      "Primary evidence summary": "The paper uses a test set for evaluation but lacks details on a separate validation set for preventing overfitting during the search and any regularization techniques used.",
      "Supporting quotes": [
        "We evaluate this harness on 200 200 previously unseen IMO-level problems drawn from IMO-AnswerBench, IMO-ProofBench, and ArXivMath [30 ; 6]."
      ],
      "Impact assessment": "The lack of a clear methodology for preventing overfitting could lead to the discovered harnesses being overly specialized to the search set and not generalizing well."
    },
    "Conclusion": {
      "Validity status": "Valid",
      "Confidence level": "High",
      "Key supporting evidence": "The paper does not describe the use of a separate validation set or discuss regularization techniques during the search process."
    }
  },
  {
    "Weakness Statement": "The paper does not provide a comprehensive comparison with existing methods for harness optimization, making it difficult to assess the relative advantages and disadvantages of the proposed approach. The paper should include a more thorough comparison with other harness optimization techniques, including both manual and automated approaches, to better contextualize the performance of Meta-Harness.",
    "Evidence Collection": {
      "b) Experiment-related Evidence (if applicable)": [
        "The paper compares Meta-Harness against 'Best-of-N', 'OpenEvolve', 'ACE', and 'MCE' baselines in the online text classification experiment.",
        "The paper compares Meta-Harness against 'No retrieval', 'Dense retrieval using the separate embedding model text-embedding-3-small', 'Random few-shot prompting', and 'BM25 retrieval' in the math reasoning experiment.",
        "The paper compares Meta-Harness against 'Terminus 2', 'Terminus-KIRA', and 'Goose' baselines in the agentic coding experiment.",
        "While the paper includes comparisons with several baselines, it does not explicitly compare against a broader range of manual harness optimization techniques or provide a detailed analysis of the specific advantages and disadvantages of Meta-Harness compared to these methods."
      ]
    },
    "Literature Gap Analysis": [],
    "Validation Analysis": {
      "Primary evidence summary": "The paper compares against several automated baselines but lacks a comprehensive comparison with a wider range of manual harness optimization techniques.",
      "Supporting quotes": [
        "We compare against two main classes of methods. (1) Human-designed strategies : these are hand-crafted harnesses for each domain, representing the current state of the art in context construction. We describe these baselines in the corresponding subsections. (2) Program-search methods: these methods search over executable code for functions, workflows, or agent designs. ... We consider the following points of comparison: • Best-of-N : independent samples from the seed with no search structure; a compute-matched control for whether search matters at all.",
        "We compare against representative methods for optimizing text. For a fair comparison, we use the same proposer configuration ( Opus-4.6 with max reasoning), select candidates solely based on search-set performance, and hold out the test sets until the final evaluation. Since evaluation is the main computational bottleneck, we give each method the same budget of proposal harness evaluations. We consider the following points of comparison: • No retrieval, few-shot prompting, and BM25 retrieval."
      ],
      "Impact assessment": "Without a more comprehensive comparison, it's harder to fully understand the novelty and effectiveness of Meta-Harness relative to the broader landscape of harness optimization."
    },
    "Conclusion": {
      "Validity status": "Partially Valid",
      "Confidence level": "High",
      "Key supporting evidence": "The paper compares against several automated baselines but lacks a broader comparison with manual harness optimization techniques."
    }
  },
  {
    "Weakness Statement": "How does Meta-Harness compare to state-of-the-art harnesses, particularly those that use more sophisticated optimization techniques?",
    "Evidence Collection": {
      "b) Experiment-related Evidence (if applicable)": [
        "The paper compares Meta-Harness against 'Best-of-N', 'OpenEvolve', 'ACE', and 'MCE' baselines in the online text classification experiment.",
        "The paper compares Meta-Harness against 'No retrieval', 'Dense retrieval using the separate embedding model text-embedding-3-small', 'Random few-shot prompting', and 'BM25 retrieval' in the math reasoning experiment.",
        "The paper compares Meta-Harness against 'Terminus 2', 'Terminus-KIRA', and 'Goose' baselines in the agentic coding experiment.",
        "The paper demonstrates state-of-the-art performance compared to the chosen baselines in each experiment."
      ]
    },
    "Literature Gap Analysis": [],
    "Validation Analysis": {
      "Primary evidence summary": "The paper compares against several baselines, demonstrating superior performance in each experiment. However, it does not explicitly compare against the absolute state-of-the-art harnesses in each domain.",
      "Supporting quotes": [
        "We compare against two main classes of methods. (1) Human-designed strategies : these are hand-crafted harnesses for each domain, representing the current state of the art in context construction. We describe these baselines in the corresponding subsections. (2) Program-search methods: these methods search over executable code for functions, workflows, or agent designs. ... We consider the following points of comparison: • Best-of-N : independent samples from the seed with no search structure; a compute-matched control for whether search matters at all.",
        "We compare against representative methods for optimizing text. For a fair comparison, we use the same proposer configuration ( Opus-4.6 with max reasoning), select candidates solely based on search-set performance, and hold out the test sets until the final evaluation. Since evaluation is the main computational bottleneck, we give each method the same budget of proposal harness evaluations. We consider the following points of comparison: • No retrieval, few-shot prompting, and BM25 retrieval."
      ],
      "Impact assessment": "While the paper shows improvement over the chosen baselines, the question of how it compares to the absolute best harnesses remains unanswered."
    },
    "Conclusion": {
      "Validity status": "Partially Valid",
      "Confidence level": "High",
      "Key supporting evidence": "The paper compares against several baselines but does not explicitly compare against the absolute state-of-the-art harnesses in each domain."
    }
  },
  {
    "Weakness Statement": "What are the limitations of Meta-Harness, and in what scenarios does it perform poorly? Could you provide more insights into the failure cases?",
    "Evidence Collection": {
      "b) Experiment-related Evidence (if applicable)": [
        "The paper mentions a limitation in the agentic coding experiment: \"We note that although the resulting harness is specialized to the TerminalBench-2 regime, autonomous completion of difficult long-horizon tasks from a single instruction is a core capability, and the benchmark consists of many tasks that frontier models and heavily engineered harnesses struggle with.\"",
        "The paper does not provide a detailed analysis of failure cases or scenarios where Meta-Harness performs poorly."
      ]
    },
    "Literature Gap Analysis": [],
    "Validation Analysis": {
      "Primary evidence summary": "The paper acknowledges one limitation but lacks a broader discussion of limitations and failure cases.",
      "Supporting quotes": [
        "We note that although the resulting harness is specialized to the TerminalBench-2 regime, autonomous completion of difficult long-horizon tasks from a single instruction is a core capability, and the benchmark consists of many tasks that frontier models and heavily engineered harnesses struggle with."
      ],
      "Impact assessment": "The absence of a detailed analysis of limitations and failure cases makes it difficult to understand the scope and weaknesses of Meta-Harness."
    },
    "Conclusion": {
      "Validity status": "Valid",
      "Confidence level": "High",
      "Key supporting evidence": "The paper only mentions one limitation and does not provide a detailed analysis of failure cases."
    }
  },
  {
    "Weakness Statement": "How does the performance of Meta-Harness vary with different base models? Are there any specific models where it performs particularly well or poorly?",
    "Evidence Collection": {
      "b) Experiment-related Evidence (if applicable)": [
        "The paper mentions using Claude Code with Opus-4.6 as the proposer.",
        "The paper does not present experiments or results using different base models for the proposer."
      ]
    },
    "Literature Gap Analysis": [],
    "Validation Analysis": {
      "Primary evidence summary": "The paper uses a specific base model but does not explore the performance with different base models.",
      "Supporting quotes": [
        "We use Claude Code [5] with Opus-4.6 ."
      ],
      "Impact assessment": "The lack of experiments with different base models leaves a gap in understanding the robustness and generalizability of Meta-Harness across different LLM architectures."
    },
    "Conclusion": {
      "Validity status": "Valid",
      "Confidence level": "High",
      "Key supporting evidence": "The paper only reports results using Claude Code with Opus-4.6."
    }
  },
  {
    "Weakness Statement": "How does the size of the prior experience affect the performance of Meta-Harness? Is there a point of diminishing returns?",
    "Evidence Collection": {
      "b) Experiment-related Evidence (if applicable)": [
        "The paper mentions the size of the search set in the online text classification experiment (200 IMO-level problems) and the agentic coding experiment (89-task benchmark).",
        "The paper does not systematically vary the size of the prior experience to analyze its impact on performance."
      ]
    },
    "Literature Gap Analysis": [],
    "Validation Analysis": {
      "Primary evidence summary": "The paper uses a specific size for the prior experience but does not analyze how varying this size affects performance.",
      "Supporting quotes": [
        "We evaluate this harness on 200 200 previously unseen IMO-level problems drawn from IMO-AnswerBench, IMO-ProofBench, and ArXivMath [30 ; 6].",
        "We evaluate the harness on the full benchmark in Table 7 , evaluated on two base models: Claude Opus 4.6 and Claude Haiku 4.5 ."
      ],
      "Impact assessment": "Without analyzing the impact of prior experience size, it's difficult to understand the scalability and efficiency of the search process."
    },
    "Conclusion": {
      "Validity status": "Valid",
      "Confidence level": "High",
      "Key supporting evidence": "The paper does not include experiments systematically varying the size of the prior experience."
    }
  },
  {
    "Weakness Statement": "The paper does not provide a detailed analysis of the computational resources required for the harness search process. This may limit its practical applicability. Specifically, the paper lacks details on the hardware used (e.g., CPU, GPU models, memory), the number of search iterations, and the time taken for each iteration. This information is crucial for assessing the feasibility of the proposed method in resource-constrained environments.",
    "Evidence Collection": {
      "b) Experiment-related Evidence (if applicable)": [
        "The paper mentions the use of Claude Code for the proposer and Opus-4.6 for the base model but does not specify the hardware used for the experiments.",
        "The paper states the number of candidates evaluated in each iteration (e.g., 40 candidates in the online text classification experiment) but does not provide the total number of iterations or the time taken for each iteration.",
        "There is no discussion on the computational cost or scalability of the method with respect to the size of the search space or the number of available resources."
      ]
    },
    "Literature Gap Analysis": [],
    "Validation Analysis": {
      "Primary evidence summary": "The paper lacks specific details on hardware specifications, the number of search iterations, and the time taken per iteration.",
      "Supporting quotes": [
        "We use Claude Code [5] with Opus-4.6 . The proposer is guided by a minimal domain-specific skill that describes where to write new harnesses, how to inspect previous harnesses and their execution traces, and what files it can and cannot modify.",
        "In our experiments, a typical run evaluates roughly 60 harnesses over 20 iterations."
      ],
      "Impact assessment": "The absence of these details makes it difficult to assess the practical applicability and scalability of the proposed method."
    },
    "Conclusion": {
      "Validity status": "Valid",
      "Confidence level": "High",
      "Key supporting evidence": "The paper does not provide specific hardware details, the exact number of iterations, or the time taken per iteration."
    }
  },
  {
    "Weakness Statement": "The paper does not discuss the potential for overfitting to the specific search set, which could impact the generalizability of the discovered harnesses. While the paper mentions using a test set for evaluation, it does not provide a clear methodology for preventing overfitting during the search process, such as using a separate validation set or employing regularization techniques within the search space.",
    "Evidence Collection": {
      "b) Experiment-related Evidence (if applicable)": [
        "The paper mentions using a test set for evaluation in the online text classification experiment: \"We evaluate this harness on 200 200 previously unseen IMO-level problems drawn from IMO-AnswerBench, IMO-ProofBench, and ArXivMath [30 ; 6].\"",
        "The paper does not explicitly describe the creation or use of a separate validation set during the search process.",
        "The paper does not discuss any regularization techniques applied to the search process."
      ]
    },
    "Literature Gap Analysis": [],
    "Validation Analysis": {
      "Primary evidence summary": "The paper uses a test set for evaluation but lacks details on a separate validation set for preventing overfitting during the search and any regularization techniques used.",
      "Supporting quotes": [
        "We evaluate this harness on 200 200 previously unseen IMO-level problems drawn from IMO-AnswerBench, IMO-ProofBench, and ArXivMath [30 ; 6]."
      ],
      "Impact assessment": "The lack of a clear methodology for preventing overfitting could lead to the discovered harnesses being overly specialized to the search set and not generalizing well."
    },
    "Conclusion": {
      "Validity status": "Valid",
      "Confidence level": "High",
      "Key supporting evidence": "The paper does not describe the use of a separate validation set or discuss regularization techniques during the search process."
    }
  },
  {
    "Weakness Statement": "The paper does not provide a comprehensive comparison with existing methods for harness optimization, making it difficult to assess the relative advantages and disadvantages of the proposed approach. The paper should include a more thorough comparison with other harness optimization techniques, including both manual and automated approaches, to better contextualize the performance of Meta-Harness.",
    "Evidence Collection": {
      "b) Experiment-related Evidence (if applicable)": [
        "The paper compares Meta-Harness against 'Best-of-N', 'OpenEvolve', 'ACE', and 'MCE' baselines in the online text classification experiment.",
        "The paper compares Meta-Harness against 'No retrieval', 'Dense retrieval using the separate embedding model text-embedding-3-small', 'Random few-shot prompting', and 'BM25 retrieval' in the math reasoning experiment.",
        "The paper compares Meta-Harness against 'Terminus 2', 'Terminus-KIRA', and 'Goose' baselines in the agentic coding experiment.",
        "While the paper includes comparisons with several baselines, it}

Now, I have successfully verified each review. Next, I will organize this content and output the final review decision:

\boxed_review{
## Summary:

This paper introduces Meta-Harness, a novel system designed to automate the optimization of harnesses for large language models (LLMs). The core idea revolves around a 'coding agent' that interacts with a file system containing prior harnesses, their execution traces, and scores from previous attempts. This agent, guided by a specific skill, can inspect existing harnesses, analyze execution logs, and propose modifications to improve their performance. The system employs a file system of prior harnesses, allowing the agent to search over harness code, execution traces, and scores from prior attempts. The agent is guided by a minimal domain-specific skill that describes where to write new harnesses, how to inspect previous harnesses and their execution traces, and what files it can and cannot modify. The paper evaluates Meta-Harness on three tasks: online text classification, mathematical reasoning, and agentic coding. In online text classification, harnesses are evaluated on a held-out test set, while in mathematical reasoning, the harnesses are evaluated on the IMO-ProofBench hard problems. In agentic coding, the harness is evaluated on the agentic coding benchmark. The results demonstrate significant improvements over baseline methods, with a 7.7-point increase in online text classification accuracy and a 4.7-point increase in retrieval-augmented math reasoning accuracy. The paper highlights the potential of Meta-Harness to significantly improve the performance of LLMs in various applications by automating the harness optimization process. The authors emphasize that the ability to selectively access and modify harness code, execution traces, and scores allows for more flexible and effective optimization compared to traditional text optimizers that rely on compressed feedback. The paper is well-written and easy to follow, with clear explanations of the methodology and experimental setup. The use of figures and tables helps to illustrate the key concepts and results. Overall, this paper presents a significant contribution to the field of harness optimization, offering a promising approach to automating and improving the performance of LLMs.


## Soundness:

3.0


## Presentation:

3.0


## Contribution:

3.0


## Strengths:

I find several aspects of this paper to be particularly strong. First, the introduction of Meta-Harness represents a novel approach to harness engineering. Unlike traditional text optimizers that compress feedback into summaries or templates, Meta-Harness allows a coding agent to inspect and modify harness code, execution traces, and scores from prior attempts. This level of access and control over the optimization process is a significant departure from existing methods and represents a substantial technical innovation. The paper clearly articulates the motivation for this approach, highlighting the limitations of existing methods and the potential of Meta-Harness to overcome these limitations. Second, the empirical results presented in the paper are compelling. The authors demonstrate significant improvements over baseline methods across multiple tasks, including online text classification, mathematical reasoning, and agentic coding. The reported gains of 7.7 points in online text classification accuracy and 4.7 points in retrieval-augmented math reasoning accuracy are substantial and provide strong evidence for the effectiveness of the proposed approach. The consistent improvements across different tasks further strengthen the credibility of the results. The paper also provides a detailed description of the experimental setup and the evaluation metrics used, which enhances the reproducibility of the work. The use of figures and tables to illustrate the key concepts and results is also commendable, as it makes the paper more accessible and easier to understand. Finally, the paper is well-written and easy to follow, with clear explanations of the methodology and experimental setup. The authors have done a good job of presenting a complex topic in a clear and concise manner, which makes the paper engaging and accessible to a wider audience. The combination of a novel approach, strong empirical results, and clear writing makes this paper a valuable contribution to the field.


## Weaknesses:

Despite the strengths of this paper, I have identified several weaknesses that warrant further discussion. First, the paper lacks a detailed analysis of the computational resources required for the harness search process. Specifically, the paper does not provide details on the hardware used for the experiments, such as the CPU model, GPU model, or memory. This information is crucial for assessing the feasibility of the proposed method in resource-constrained environments. Furthermore, the paper does not specify the number of search iterations performed, nor does it provide the time taken for each iteration. This lack of information makes it difficult to assess the practical applicability and scalability of the proposed method. For example, the paper mentions using Claude Code with Opus-4.6 but does not specify the hardware used for the experiments. Similarly, the paper states the number of candidates evaluated in each iteration (e.g., 40 candidates in the online text classification experiment) but does not provide the total number of iterations or the time taken per iteration. This absence of details makes it difficult to assess the practical applicability and scalability of the proposed method. My confidence in this weakness is high, as the paper clearly omits these crucial details. Second, the paper does not discuss the potential for overfitting to the specific search set. While the paper mentions using a test set for evaluation, it does not provide a clear methodology for preventing overfitting during the search process, such as using a separate validation set or employing regularization techniques within the search space. The paper uses a test set for evaluation in the online text classification experiment, but it does not describe the creation or use of a separate validation set during the search process. The paper also does not discuss any regularization techniques applied to the search process. This lack of a clear methodology for preventing overfitting could lead to the discovered harnesses being overly specialized to the search set and not generalizing well. My confidence in this weakness is high, as the paper clearly lacks a discussion of these critical aspects. Third, the paper does not provide a comprehensive comparison with existing methods for harness optimization. While the paper includes comparisons with several baselines, it does not explicitly compare against a broader range of manual harness optimization techniques or provide a detailed analysis of the specific advantages and disadvantages of Meta-Harness compared to these methods. The paper compares Meta-Harness against 'Best-of-N', 'OpenEvolve', 'ACE', and 'MCE' baselines in the online text classification experiment, 'No retrieval', 'Dense retrieval using the separate embedding model text-embedding-3-small', 'Random few-shot prompting', and 'BM25 retrieval' in the math reasoning experiment, and 'Terminus 2', 'Terminus-KIRA', and 'Goose' baselines in the agentic coding experiment. While the paper includes comparisons with several baselines, it lacks a comprehensive comparison with a wider range of manual harness optimization techniques. My confidence in this weakness is high, as the paper clearly lacks a broader comparison. Fourth, the paper does not provide a detailed analysis of the impact of the size of the prior experience on the performance of Meta-Harness. The paper uses a specific size for the prior experience but does not systematically vary this size to analyze its impact on performance. The paper mentions the size of the search set in the online text classification experiment (200 IMO-level problems) and the agentic coding experiment (89-task benchmark). The paper does not systematically vary the size of the prior experience to analyze its impact on performance. This lack of analysis makes it difficult to understand the scalability and efficiency of the search process. My confidence in this weakness is high, as the paper clearly lacks this analysis. Finally, the paper does not provide a detailed analysis of the computational cost and scalability of the method with respect to the size of the search space and the number of available resources. This lack of analysis makes it difficult to assess the practical applicability of the proposed method in resource-constrained environments. My confidence in this weakness is high, as the paper clearly lacks this analysis. These weaknesses, while not invalidating the core contributions of the paper, do highlight areas where further research and analysis are needed to fully understand the potential and limitations of Meta-Harness.


## Suggestions:

To address the identified weaknesses, I propose several concrete suggestions. First, the authors should provide a more detailed analysis of the computational resources required for the harness search process. This should include specifics on the hardware used for the experiments, including the CPU model, GPU model, memory, and the number of available cores. Furthermore, the paper should specify the number of search iterations performed, and the time taken for each iteration. This information is essential for other researchers to replicate the experiments and assess the practical applicability of the proposed method. The authors could also discuss the scalability of the method with respect to the size of the search space and the number of available resources. For example, how does the search time scale with the number of prior harnesses stored on the filesystem? This would provide a better understanding of the computational cost associated with the proposed approach and its limitations. Second, to address the potential for overfitting, the authors should implement a more rigorous validation strategy. This could involve using a separate validation set that is distinct from both the search set and the evaluation set. The validation set could be used to monitor the performance of the discovered harnesses during the search process and to stop the search when the performance on the validation set starts to degrade. This would help to prevent the method from overfitting to the specific search set and ensure that the discovered harnesses generalize well to unseen data. Additionally, the authors should explore techniques such as early stopping or regularization to further improve the generalization performance of the method. The paper should also include a discussion of the potential limitations of the validation strategy and how these limitations could be addressed in future work. Third, the authors should include a more comprehensive comparison with existing methods for harness optimization. This comparison should include both manual and automated approaches, and it should focus on the relative advantages and disadvantages of each method. The authors should discuss the specific scenarios in which Meta-Harness is expected to outperform existing methods and the scenarios in which it may not be as effective. This would provide a better understanding of the strengths and weaknesses of the proposed approach and its potential impact on the field. The comparison should also include a discussion of the computational cost and the complexity of implementation for each method. This would allow researchers to make informed decisions about which method is most suitable for their specific needs. Fourth, the authors should conduct a systematic analysis of the impact of the size of the prior experience on the performance of Meta-Harness. This analysis should involve varying the size of the prior experience and evaluating the performance of the discovered harnesses on a held-out test set. This would help to understand the scalability and efficiency of the search process. Finally, the authors should provide a more detailed analysis of the computational cost and scalability of the method with respect to the size of the search space and the number of available resources. This analysis should include a discussion of the time taken for each iteration, the total time required to complete the harness search, and the memory requirements of the method. This would provide a better understanding of the practical applicability of the proposed method in resource-constrained environments. By addressing these suggestions, the authors can significantly strengthen the paper and make it more impactful for the research community.


## Questions:

I have several questions that arise from my analysis of this paper. First, how does the performance of Meta-Harness vary with different base models? The paper mentions using Claude Code with Opus-4.6 as the proposer, but it does not present experiments or results using different base models for the proposer. Are there any specific models where it performs particularly well or poorly? This is important to understand the robustness and generalizability of Meta-Harness across different LLM architectures. Second, how does the size of the prior experience affect the performance of Meta-Harness? The paper mentions the size of the search set in the online text classification experiment (200 IMO-level problems) and the agentic coding experiment (89-task benchmark), but it does not systematically vary the size of the prior experience to analyze its impact on performance. Is there a point of diminishing returns, and how does the search time scale with the number of prior harnesses stored on the filesystem? This is important to understand the scalability and efficiency of the search process. Third, what are the limitations of Meta-Harness, and in what scenarios does it perform poorly? The paper acknowledges one limitation in the agentic coding experiment, but it lacks a broader discussion of limitations and failure cases. Could you provide more insights into the failure cases and scenarios where Meta-Harness performs poorly? This is important to understand the scope and weaknesses of Meta-Harness and to identify areas for future research. Fourth, what are the specific scenarios in which Meta-Harness is expected to outperform existing methods, and what are the specific scenarios in which it may not be as effective? The paper compares Meta-Harness against several baselines, but it does not explicitly compare against the absolute state-of-the-art harnesses in each domain. A more detailed comparison would provide a better understanding of the relative advantages and disadvantages of Meta-Harness. Finally, what are the computational costs of the proposed approach, and how does it scale with respect to the size of the search space and the number of available resources? The paper lacks details on the hardware used for the experiments, the number of search iterations, and the time taken for each iteration. This information is crucial for assessing the feasibility of the proposed method in resource-constrained environments. These questions are important to further understand the capabilities and limitations of Meta-Harness and to guide future research in this area.


## Rating:

6.5


## Confidence:

3.0


## Decision:

Accept
}