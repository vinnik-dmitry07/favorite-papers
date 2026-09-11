I will use Standard Mode for comprehensive thinking. As a professional reviewer, I will simulate 4 different reviewers, followed by the verification thinking. Then I will output the Finally Review Output. Let me think - Standard Mode means I will output the original review, followed by the verification thinking. Considering that I am currently in standard mode, I should think from my existing knowledge and consider some related work content when writing about weaknesses. Then I will output the Finally Review Output and Meta Review Output:

\boxed_simreviewers{
## Reviewer 1

### Summary

This paper proposes a new fine-tuning method, Self-Distillation Fine-Tuning (SDFT), to address the issue of distribution gap between task datasets and the seed LLM. The proposed method first prompts the seed LM to generate responses that uphold semantic equivalence with the original responses present in the task dataset, resulting in the distilled dataset. Then, SDFT fine-tunes the model using the distilled dataset. Experimental results on the Llama-2-chat model across various benchmarks demonstrate that SDFT effectively mitigates catastrophic forgetting while achieving comparable or superior performance on downstream tasks compared to vanilla fine-tuning.

### Soundness

2

### Presentation

3

### Contribution

2

### Strengths

1. This paper is well-written and easy to follow.
2. The proposed method is simple and straightforward, and the experimental results demonstrate its effectiveness.

### Weaknesses

#### Some Related Works


#### comment

1. The motivation behind the proposed method is not clearly explained. The authors claim that the distribution gap between the task dataset and the seed LLM is the primary underlying cause of catastrophic forgetting, but this claim lacks sufficient justification. The paper does not provide a clear explanation of why the distribution gap is the primary cause, and it does not explore alternative explanations for catastrophic forgetting, such as the model's inability to generalize to new tasks due to overfitting on the training data. The paper should include a more thorough analysis of the underlying causes of catastrophic forgetting to strengthen its motivation.
2. The proposed method is not novel, as it is very similar to the self-distillation approach used in Self-Rewarding Language Models. The paper does not adequately differentiate its approach from existing self-distillation methods, and it does not provide a detailed analysis of the unique aspects of its method. The paper should clearly articulate the novel contributions of its approach and provide a more thorough comparison to existing self-distillation methods.
3. The experiments are insufficient to fully evaluate the effectiveness of the proposed method. The experiments are limited to the Llama-2-chat model, and the paper does not explore the performance of the proposed method on other models. The paper should include experiments on a wider range of models to demonstrate the generalizability of the proposed method. Additionally, the paper does not provide a detailed analysis of the performance of the proposed method on different tasks, and it does not explore the limitations of the proposed method. The paper should include a more thorough analysis of the experimental results to provide a more comprehensive evaluation of the proposed method.

### Suggestions

The paper needs to provide a more robust justification for its core claim that the distribution gap between the task dataset and the seed LLM is the primary cause of catastrophic forgetting. This could involve a more detailed analysis of the feature space of the models before and after fine-tuning, or an investigation of the model's internal representations to understand how the distribution shift affects its performance. Furthermore, the paper should explore alternative explanations for catastrophic forgetting, such as the model's tendency to overfit to the training data, and provide empirical evidence to support its chosen explanation. A more thorough investigation of the underlying causes of catastrophic forgetting would significantly strengthen the motivation for the proposed method.

The paper should also provide a more detailed comparison of the proposed method with existing self-distillation techniques, particularly Self-Rewarding Language Models. This comparison should not only highlight the similarities but also clearly articulate the novel contributions of the proposed method. For example, the paper could analyze the specific mechanisms by which the proposed method achieves self-distillation, and compare these mechanisms to those used in other self-distillation methods. The paper should also provide a more detailed analysis of the unique aspects of its method, such as the use of a distilled dataset, and explain how these aspects contribute to the effectiveness of the proposed method. A more thorough comparison to existing self-distillation methods would help to establish the novelty and significance of the proposed approach.

Finally, the paper needs to significantly expand its experimental evaluation to demonstrate the generalizability and robustness of the proposed method. This should include experiments on a wider range of models, including both smaller and larger models, to assess the scalability of the method. The paper should also include experiments on a more diverse set of tasks, to evaluate the performance of the proposed method on different types of problems. Additionally, the paper should provide a more detailed analysis of the experimental results, including an investigation of the limitations of the proposed method and the conditions under which it performs well or poorly. A more comprehensive experimental evaluation would provide a more robust assessment of the proposed method and its potential impact.

### Questions

1. In line 187, why is the loss function defined as the negative log-likelihood of the target output y^t given the context c^t and the input x^t? Typically, the negative log-likelihood of the target output y^t given the context c^t is used as the loss function.
2. In line 190, what is the meaning of the notation f_{\theta} (y | c^t, x^t)? Is it equivalent to f_{\theta} (y^t | c^t, x^t)?
3. In line 192, why is the loss function defined as the negative log-likelihood of the target output y^t given the context c^t and the input x^t? Typically, the negative log-likelihood of the target output y^t given the context c^t is used as the loss function.
4. In line 203, why is the loss function defined as the negative log-likelihood of the target output y^t given the context c^t and the input x^t? Typically, the negative log-likelihood of the target output y^t given the context c^t is used as the loss function.
5. In line 206, why is the loss function defined as the negative log-likelihood of the target output y^t given the context c^t and the input x^t? Typically, the negative log-likelihood of the target output y^t given the context c^t is used as the loss function.

### Rating

3

### Confidence

4

**********

## Reviewer 2

### Summary

The paper introduces a new fine-tuning method called Self-Distillation Fine-Tuning (SDFT), which addresses the issue of catastrophic forgetting during fine-tuning of large language models (LLMs). The authors hypothesize that the distribution gap between the task dataset and the seed LLM is a primary underlying cause of this forgetting. To mitigate this, SDFT prompts the seed LLM to rewrite original responses into semantically equivalent ones, creating a distilled dataset that maintains the original distribution. This distilled dataset is then used for fine-tuning, reducing the distribution shift and thereby preserving the model's general instruction-following abilities and safety alignment. The authors demonstrate the effectiveness of SDFT through experiments on various benchmarks, showing comparable or superior performance to vanilla fine-tuning while maintaining general capabilities.

### Soundness

2

### Presentation

3

### Contribution

2

### Strengths

- The paper is well-written and easy to follow.
- The proposed method is simple and straightforward.
- The experimental results show that SDFT effectively mitigates catastrophic forgetting and achieves comparable or superior performance on downstream tasks compared to vanilla fine-tuning.

### Weaknesses

#### Some Related Works


#### comment

 - The paper lacks a clear motivation for why the distribution gap between the task dataset and the seed LLM is a primary cause of catastrophic forgetting. The authors should provide more evidence or references to support this claim.
- The paper does not compare SDFT with other methods that address catastrophic forgetting, such as regularization-based approaches or replay-based methods.
- The paper does not provide a detailed analysis of the computational cost of SDFT compared to vanilla fine-tuning. This is important for assessing the practicality of the proposed method.
- The paper does not discuss the limitations of SDFT or potential failure cases. This is important for understanding the scope of applicability of the proposed method.
- The paper does not explore the sensitivity of SDFT to different hyperparameters, such as the size of the distilled dataset or the number of self-distillation iterations.

### Suggestions

The paper should provide a more thorough justification for the claim that the distribution gap between the task dataset and the seed LLM is a primary cause of catastrophic forgetting. While the authors hypothesize this, they do not provide sufficient evidence or cite existing literature that supports this specific claim. It would be beneficial to include a more detailed analysis of how the distribution shift affects the model's parameters and leads to forgetting. For example, the authors could analyze the change in the model's embedding space or attention patterns after fine-tuning on a task with a different distribution than the original training data. This would provide a more concrete understanding of the underlying mechanism and strengthen the motivation for their proposed method. Furthermore, the authors should explore alternative explanations for catastrophic forgetting, such as the model's tendency to overfit to the training data or the limitations of the optimization process itself. By comparing their hypothesis with other potential causes, the authors can provide a more robust and convincing argument for the effectiveness of their approach.

To strengthen the paper, the authors should include a more comprehensive comparison with existing methods for mitigating catastrophic forgetting. Specifically, they should compare SDFT with regularization-based approaches, such as Elastic Weight Consolidation (EWC) or Synaptic Intelligence, and replay-based methods, such as Gradient Episodic Memory (GEM). These methods are widely used in the literature and offer different trade-offs in terms of computational cost, memory requirements, and performance. By comparing SDFT with these methods, the authors can demonstrate the advantages and limitations of their approach and provide a more complete picture of the state-of-the-art in catastrophic forgetting mitigation. The comparison should not only focus on performance metrics but also on other factors such as computational cost, ease of implementation, and sensitivity to hyperparameters. This would allow readers to better understand the practical implications of using SDFT compared to other methods.

Finally, the paper needs a more detailed analysis of the computational cost and sensitivity of SDFT. The authors should provide a breakdown of the computational resources required for each step of the SDFT process, including the self-distillation step and the fine-tuning step. This analysis should include the time and memory requirements for different model sizes and dataset sizes. Furthermore, the authors should investigate the sensitivity of SDFT to different hyperparameters, such as the size of the distilled dataset, the number of self-distillation iterations, and the learning rate. This analysis should include a systematic exploration of the hyperparameter space and a discussion of the optimal settings for different tasks and datasets. This would provide valuable insights into the practical applicability of SDFT and help users to tune the method effectively. Additionally, the authors should discuss the limitations of SDFT, such as its potential sensitivity to the quality of the distilled dataset or the potential for introducing bias during the self-distillation process. This would provide a more balanced and realistic assessment of the proposed method.

### Questions

- How does SDFT compare to other methods that address catastrophic forgetting, such as regularization-based approaches or replay-based methods?
- What is the computational cost of SDFT compared to vanilla fine-tuning?
- What are the limitations of SDFT, and in what scenarios might it fail?
- How sensitive is SDFT to different hyperparameters, such as the size of the distilled dataset or the number of self-distillation iterations?

### Rating

3

### Confidence

4

**********

## Reviewer 3

### Summary

This paper proposes a new fine-tuning method called Self-Distillation Fine-Tuning (SDFT), which aims to address the issue of catastrophic forgetting during fine-tuning. The authors hypothesize that the distribution gap between the task dataset and the seed LLM is the primary underlying cause of catastrophic forgetting. To address this, SDFT prompts the seed LLM to rewrite the original responses into semantically equivalent responses, creating a distilled dataset that maintains the original distribution. This distilled dataset is then used for fine-tuning, reducing the distribution shift and thereby preserving the model's general instruction-following abilities and safety alignment. The authors conduct experiments on various benchmarks to demonstrate the effectiveness of SDFT.

### Soundness

2

### Presentation

3

### Contribution

2

### Strengths

1. The paper is well-written and easy to follow.
2. The proposed method is simple and straightforward.
3. The experimental results show that SDFT effectively mitigates catastrophic forgetting and achieves comparable or superior performance on downstream tasks compared to vanilla fine-tuning.

### Weaknesses

#### Some Related Works


#### comment

1. The motivation behind the proposed method is not clearly explained. The authors claim that the distribution gap between the task dataset and the seed LLM is the primary underlying cause of catastrophic forgetting, but this claim lacks sufficient justification. The paper does not provide a clear explanation of why the distribution gap is the primary cause, and it does not explore alternative explanations for catastrophic forgetting, such as the model's inability to generalize to new tasks due to overfitting on the training data. The paper should include a more thorough analysis of the underlying causes of catastrophic forgetting to strengthen its motivation.
2. The proposed method is not novel, as it is very similar to the self-distillation approach used in Self-Rewarding Language Models. The paper does not adequately differentiate its approach from existing self-distillation methods, and it does not provide a detailed analysis of the unique aspects of its method. The paper should clearly articulate the novel contributions of its approach and provide a more thorough comparison to existing self-distillation methods.
3. The experiments are insufficient to fully evaluate the effectiveness of the proposed method. The experiments are limited to the Llama-2-chat model, and the paper does not explore the performance of the proposed method on other models. The paper should include experiments on a wider range of models to demonstrate the generalizability of the proposed method. Additionally, the paper does not provide a detailed analysis of the performance of the proposed method on different tasks, and it does not explore the limitations of the proposed method. The paper should include a more thorough analysis of the experimental results to provide a more comprehensive evaluation of the proposed method.

### Suggestions

The paper needs to provide a more robust justification for its core claim that the distribution gap between the task dataset and the seed LLM is the primary cause of catastrophic forgetting. This could involve a more detailed analysis of the feature space of the models before and after fine-tuning, or an investigation of the model's internal representations to understand how the distribution shift affects its performance. Furthermore, the paper should explore alternative explanations for catastrophic forgetting, such as the model's tendency to overfit to the training data, and provide empirical evidence to support its chosen explanation. A more thorough investigation of the underlying causes of catastrophic forgetting would significantly strengthen the motivation for the proposed method. The paper should also include a more detailed discussion of the limitations of the proposed method and the conditions under which it might fail.

To address the lack of novelty, the paper should clearly articulate the novel contributions of its approach and provide a more thorough comparison to existing self-distillation methods. This could involve a detailed analysis of the specific mechanisms by which the proposed method achieves self-distillation, and compare these mechanisms to those used in other self-distillation methods. The paper should also highlight the unique aspects of its method and explain how these aspects contribute to its effectiveness. A more detailed comparison to existing self-distillation methods would help to establish the novelty and significance of the proposed approach. The paper should also discuss the potential limitations of the proposed method in comparison to existing self-distillation methods.

Finally, the paper needs to significantly expand its experimental evaluation to demonstrate the generalizability and robustness of the proposed method. This should include experiments on a wider range of models, including both smaller and larger models, to assess the scalability of the method. The paper should also include experiments on a more diverse set of tasks, to evaluate the performance of the proposed method on different types of problems. Additionally, the paper should provide a more detailed analysis of the experimental results, including an investigation of the limitations of the proposed method and the conditions under which it performs well or poorly. A more comprehensive experimental evaluation would provide a more robust assessment of the proposed method and its potential impact.

### Questions

See the weakness.

### Rating

5

### Confidence

4

**********

## Reviewer 4

### Summary

This paper proposes a novel fine-tuning method, Self-Distillation Fine-Tuning (SDFT), to mitigate catastrophic forgetting during fine-tuning of large language models (LLMs). SDFT addresses the issue by using a distilled dataset generated by prompting the seed LLM to rewrite original responses into semantically equivalent ones, thus maintaining the original distribution and reducing the distribution shift during fine-tuning. The method is evaluated on various benchmarks, demonstrating its effectiveness in preserving general instruction-following abilities and safety alignment while achieving comparable or superior performance on downstream tasks compared to vanilla fine-tuning.

### Soundness

3

### Presentation

3

### Contribution

3

### Strengths

- The paper is well-written and easy to follow.
- The motivation behind the proposed method is clearly articulated, and the approach is straightforward and effective.
- The experimental results are comprehensive, covering multiple benchmarks and tasks, which demonstrate the effectiveness of the proposed method.

### Weaknesses

#### Some Related Works


#### comment

 - The paper does not provide a detailed analysis of the computational cost of SDFT compared to vanilla fine-tuning. This is important for assessing the practicality of the proposed method.
- The paper does not discuss the limitations of SDFT or potential failure cases. This is important for understanding the scope of applicability of the proposed method.
- The paper does not explore the sensitivity of SDFT to different hyperparameters, such as the size of the distilled dataset or the number of self-distillation iterations.

### Suggestions

The paper would benefit from a more thorough analysis of the computational overhead introduced by the SDFT method. Specifically, the authors should provide a detailed breakdown of the time and memory costs associated with each step of the SDFT process, including the generation of the distilled dataset and the fine-tuning phase. This analysis should be compared against the computational costs of standard fine-tuning to provide a clear understanding of the trade-offs involved. For example, the authors could report the training time per epoch, the memory footprint of the model and intermediate activations, and the number of parameters involved in the distillation process. Furthermore, it would be beneficial to explore the scalability of SDFT with respect to the size of the seed model and the size of the distilled dataset. This would help to determine the practical applicability of the method to different model sizes and computational resources. 

In addition to the computational cost, the paper should also include a more comprehensive discussion of the limitations of the proposed SDFT method. The authors should explore scenarios where SDFT might fail or underperform, such as tasks that require significant domain adaptation or tasks where the seed model is not well-suited for the target task. For instance, it would be useful to investigate how SDFT performs when the target task requires a significant shift in the model's reasoning or problem-solving strategies compared to the tasks used for distillation. The authors should also consider the impact of the quality of the distilled dataset on the performance of SDFT. If the distilled dataset is not representative of the target task, it could lead to suboptimal performance or even negative transfer. A sensitivity analysis of the distilled dataset generation process would be valuable to understand the robustness of the method. 

Finally, the paper should include a more detailed analysis of the sensitivity of SDFT to its hyperparameters. The authors should investigate how the size of the distilled dataset affects the performance of SDFT, and whether there is an optimal size for the distilled dataset. Similarly, the authors should explore the impact of the number of self-distillation iterations on the performance of SDFT. It would be useful to provide guidelines for selecting these hyperparameters based on the characteristics of the target task and the available computational resources. For example, the authors could perform a grid search over the hyperparameter space and report the performance of SDFT for different hyperparameter settings. This would provide a more complete picture of the practical applicability of the method and help users to effectively tune the method for their specific use cases.

### Questions

- How does the computational cost of SDFT compare to vanilla fine-tuning?
- What are the limitations of SDFT, and in what scenarios might it fail?
- How sensitive is SDFT to different hyperparameters, such as the size of the distilled dataset or the number of self-distillation iterations?

### Rating

6

### Confidence

4

**********

}

I have finished generating simulated reviews from 4 reviewers. Next, I will generate verification content for these reviews:

\boxed_verification{
The user wants me to validate weaknesses identified by reviewers in a given paper. I need to go through each reviewer's comments and check if the criticism is valid based on the content of the paper provided.

For each weakness, I will:
1. **State the weakness** as quoted from the reviewer.
2. **Collect evidence** from the paper to support or refute the weakness. This will involve looking at the method description, experimental setup, results, and related work.
3. **Analyze literature gaps** by checking if the paper misses relevant citations or comparisons.
4. **Provide a validation analysis** summarizing the evidence and its impact.
5. **Conclude** whether the weakness is valid, partially valid, or invalid, and provide a confidence level and key supporting evidence.
```json
[
  {
    "Weakness Statement": "The motivation behind the proposed method is not clearly explained. The authors claim that the distribution gap between the task dataset and the seed LLM is the primary underlying cause of catastrophic forgetting, but this claim lacks sufficient justification. The paper does not provide a clear explanation of why the distribution gap is the primary cause, and it does not explore alternative explanations for catastrophic forgetting, such as the model's inability to generalize to new tasks due to overfitting on the training data. The paper should include a more thorough analysis of the underlying causes of catastrophic forgetting to strengthen its motivation.",
    "Evidence Collection": {
      "a) Method-related Evidence": [
        {
          "quote": "As the distribution of the seed LM converges towards that of the task dataset, it naturally enhances performance on target tasks. However, vanilla fine-tuning is susceptible to catastrophic forgetting in general instruction-following abilities and safety alignment.",
          "section": "Introduction"
        },
        {
          "quote": "The distribution gap between the task dataset and the seed LLM can lead to significant differences in model performance, as evidenced by the degradation of performance on other tasks.",
          "section": "Introduction"
        },
        {
          "quote": "The paper hypothesizes that the distribution gap between the task dataset and the seed LLM is the primary underlying cause of catastrophic forgetting, which is supported by the observation that vanilla fine-tuning on the Open Functions dataset results in a significant decrease in performance on other tasks.",
          "section": "Method -> Overview"
        }
      ],
      "b) Experiment-related Evidence": []
    },
    "Literature Gap Analysis": [],
    "Validation Analysis": {
      "Primary evidence summary": The paper states the hypothesis about the distribution gap as the primary cause of catastrophic forgetting and provides an example with Open Functions. However, it doesn't explicitly cite literature that supports this specific claim or discuss alternative explanations like overfitting.
      "Supporting quotes": [
        "As the distribution of the seed LM converges towards that of the task dataset, it naturally enhances performance on target tasks.",
        "However, vanilla fine-tuning is susceptible to catastrophic forgetting in general instruction-following abilities and safety alignment.",
        "The distribution gap between the task dataset and the seed LLM can lead to significant differences in model performance, as evidenced by the degradation of performance on other tasks."
      ],
      "Impact assessment": The lack of explicit justification and discussion of alternatives weakens the motivation.
    },
    "Conclusion": {
      "Validity status": "Partially Valid",
      "Confidence level": "High",
      "Key supporting evidence": "While the paper states the hypothesis and provides an example, it lacks explicit citations or discussion of alternative explanations for catastrophic forgetting."
    }
  },
  {
    "Weakness Statement": "The proposed method is not novel, as it is very similar to the self-distillation approach used in Self-Rewarding Language Models. The paper does not adequately differentiate its approach from existing self-distillation methods, and it does not provide a detailed analysis of the unique aspects of its method. The paper should clearly articulate the novel contributions of its approach and provide a more thorough comparison to existing self-distillation methods.",
    "Evidence Collection": {
      "a) Method-related Evidence": [
        {
          "quote": "To address this issue, we propose S elf- D istillation F ine- T uning (SDFT), to better align the distribution of the task dataset with that of the seed LM.",
          "section": "Introduction"
        },
        {
          "quote": "As depicted in Figure 2 , the initial step of SDFT involves prompting the seed LM to rewrite the original response y t y^{t}\y^{t} into y ~ \sim \sim f θ ( y ∣ c t , x t , y t ) .",
          "section": "Method -> Workflow"
        },
        {
          "quote": "Next, to ensure the quality of the distilled responses, we employ simple heuristics to evaluate the distilled response. For instance, in math reasoning problems, we extract the final answer from the distilled response y ~ \tilde{y} \tilde{y} and compare it with the one from the original response y t y^{t} y^{t}. Otherwise, we keep the original response.",
          "section": "Method -> Workflow"
        },
        {
          "quote": "Finally, the distilled response is used as a replacement for the original response y t y^{t} y^{t} for fine-tuning, i.e., the loss becomes: L SDFT ( θ ) = − log f θ ( y ~ ′ ∣ c t , x t ) .",
          "section": "Method -> Workflow"
        }
      ],
      "b) Experiment-related Evidence": []
    },
    "Literature Gap Analysis": [
      "Missing citation for Self-Rewarding Language Models or a detailed comparison highlighting the differences."
    ],
    "Validation Analysis": {
      "Primary evidence summary": The paper introduces SDFT as a method to align distributions using self-distillation. While it mentions the use of heuristics for quality, it doesn't explicitly differentiate itself from existing self-distillation techniques like Self-Rewarding Language Models.
      "Supporting quotes": [
        "To address this issue, we propose S elf- D istillation F ine- T uning (SDFT), to better align the distribution of the task dataset with that of the seed LM.",
        "As depicted in Figure 2 , the initial step of SDFT involves prompting the seed LM to rewrite the original response y t y^{t}\y^{t} into y ~ \sim \sim f θ ( y ∣ c t , x t , y t ) ."
      ],
      "Impact assessment": The lack of clear differentiation from existing self-distillation methods weakens the perceived novelty of the approach.
    },
    "Conclusion": {
      "Validity status": "Valid",
      "Confidence level": "High",
      "Key supporting evidence": "The paper describes the method as a form of self-distillation but lacks a detailed comparison to existing methods like Self-Rewarding Language Models to highlight its unique contributions."
    }
  },
  {
    "Weakness Statement": "The experiments are insufficient to fully evaluate the effectiveness of the proposed method. The experiments are limited to the Llama-2-chat model, and the paper does not explore the performance of the proposed method on other models. The paper should include experiments on a wider range of models to demonstrate the generalizability of the proposed method. Additionally, the paper does not provide a detailed analysis of the performance of the proposed method on different tasks, and it does not explore the limitations of the proposed method. The paper should include a more thorough analysis of the experimental results to provide a more comprehensive evaluation of the proposed method.",
    "Evidence Collection": {
      "a) Method-related Evidence": [],
      "b) Experiment-related Evidence": [
        {
          "quote": "We utilize the Llama-2-7b-chat model ( Touvron et al., 2023 ) as the seed LM in most of our experiments, except where explicitly stated otherwise.",
          "section": "Experimental Setup"
        },
        {
          "quote": "To substantiate this claim, we conducted supplementary experiments that included full fine-tuning on Llama-2-7b-chat and LoRA fine-tuning on Llama-2-7b-chat. Additionally, we explored the fine-tuning of the recently unveiled SOTA model, Llama3 Meta AI (2024) on the Open Functions dataset.",
          "section": "Experimental Setup"
        },
        {
          "quote": "Table 5 reveals that in all scenarios, SDFT not only consistently outperforms vanilla fine-tuning in the target task but also reduces forgetting across all other tasks, demonstrating its effectiveness.",
          "section": "Experiments -> SDFT Preserves Alignment -> Results -> Analysis"
        },
        {
          "quote": "In line with the patterns noted in Table 2 , fine-tuning on Alpaca, Dolly and LIMA typically leads to a marked reduction in both safety and helpfulness metrics.",
          "section": "Experiments -> SDFT Preserves Safety Alignment -> Results -> Analysis"
        }
      ]
    },
    "Literature Gap Analysis": [],
    "Validation Analysis": {
      "Primary evidence summary": The paper primarily uses Llama-2-7b-chat as the seed model. While it includes experiments with LoRA and mentions fine-tuning Llama-3 on Open Functions, the main experiments focus on Llama-2. The analysis of performance on different tasks is present but could be more in-depth.
      "Supporting quotes": [
        "We utilize the Llama-2-7b-chat model ( Touvron et al., 2023 ) as the seed LM in most of our experiments, except where explicitly stated otherwise.",
        "Additionally, we explored the fine-tuning of the recently unveiled SOTA model, Llama3 Meta AI (2024) on the Open Functions dataset."
      ],
      "Impact assessment": The limited model diversity in the main experiments and the somewhat brief analysis of task performance support the reviewer's concern.
    },
    "Conclusion": {
      "Validity status": "Partially Valid",
      "Confidence level": "High",
      "Key supporting evidence": "The primary experiments use Llama-2-7b-chat. While Llama-3 is mentioned, the main analysis focuses on Llama-2. The analysis of performance on different tasks is present but could be more detailed."
    }
  },
  {
    "Weakness Statement": "How does the computational cost of SDFT compare to vanilla fine-tuning?",
    "Evidence Collection": {
      "a) Method-related Evidence": [],
      "b) Experiment-related Evidence": []
    },
    "Literature Gap Analysis": [],
    "Validation Analysis": {
      "Primary evidence summary": The paper does not provide a direct comparison of the computational cost between SDFT and vanilla fine-tuning.
      "Supporting quotes": [],
      "Impact assessment": The absence of this comparison makes it difficult to assess the practical trade-offs of using SDFT.
    },
    "Conclusion": {
      "Validity status": "Valid",
      "Confidence level": "High",
      "Key supporting evidence": "The paper lacks a direct comparison of computational costs between SDFT and vanilla fine-tuning."
    }
  },
  {
    "Weakness Statement": "What are the limitations of SDFT, and in what scenarios might it fail?",
    "Evidence Collection": {
      "a) Method-related Evidence": [],
      "b) Experiment-related Evidence": []
    },
    "Literature Gap Analysis": [],
    "Validation Analysis": {
      "Primary evidence summary": The paper does not explicitly discuss the limitations of SDFT or scenarios where it might fail.
      "Supporting quotes": [],
      "Impact assessment": The lack of discussion on limitations leaves a gap in understanding the scope and applicability of SDFT.
    },
    "Conclusion": {
      "Validity status": "Valid",
      "Confidence level": "High",
      "Key supporting evidence": "The paper does not explicitly discuss the limitations of SDFT."
    }
  },
  {
    "Weakness Statement": "How sensitive is SDFT to different hyperparameters, such as the size of the distilled dataset or the number of self-distillation iterations?",
    "Evidence Collection": {
      "a) Method-related Evidence": [
        {
          "quote": "The distillation template is designed to be task-independent, allowing for easy integration into various fine-tuning pipelines.",
          "section": "Method -> Distillation Template"
        }
      ],
      "b) Experiment-related Evidence": [
        {
          "quote": "We utilize the Llama-2-7b-chat model ( Touvron et al., 2023 ) as the seed LM in most of our experiments, except where explicitly stated otherwise.",
          "section": "Experimental Setup"
        },
        {
          "quote": "To substantiate this claim, we conducted supplementary experiments that included full fine-tuning on Llama-2-7b-chat and LoRA fine-tuning on Llama-2-7b-chat. Additionally, we explored the fine-tuning of the recently unveiled SOTA model, Llama3 Meta AI (2024) on the Open Functions dataset.",
          "section": "Experimental Setup"
        }
      ]
    },
    "Literature Gap Analysis": [],
    "Validation Analysis": {
      "Primary evidence summary": The paper mentions the distillation template is task-independent but doesn't provide a detailed sensitivity analysis of hyperparameters like the size of the distilled dataset or the number of self-distillation iterations. The main experiments use a fixed distillation process.
      "Supporting quotes": [
        "The distillation template is designed to be task-independent, allowing for easy integration into various fine-tuning pipelines."
      ],
      "Impact assessment": The lack of hyperparameter sensitivity analysis limits the understanding of SDFT's robustness.
    },
    "Conclusion": {
      "Validity status": "Valid",
      "Confidence level": "High",
      "Key supporting evidence": "The paper does not include a detailed analysis of how SDFT's performance varies with different hyperparameters like the size of the distilled dataset or the number of self-distillation iterations."
    }
  },
  {
    "Weakness Statement": "The motivation behind the proposed method is not clearly explained. The authors claim that the distribution gap between the task dataset and the seed LLM is the primary underlying cause of catastrophic forgetting, but this claim lacks sufficient justification. The paper does not provide a clear explanation of why the distribution gap is the primary cause, and it does not explore alternative explanations for catastrophic forgetting, such as the model's tendency to overfit to the training data. The paper should include a more thorough analysis of the underlying causes of catastrophic forgetting to strengthen its motivation.",
    "Evidence Collection": {
      "a) Method-related Evidence": [
        {
          "quote": "As the distribution of the seed LM converges towards that of the task dataset, it naturally enhances performance on target tasks. However, vanilla fine-tuning is susceptible to catastrophic forgetting in general instruction-following abilities and safety alignment.",
          "section": "Introduction"
        },
        {
          "quote": "The distribution gap between the task dataset and the seed LLM can lead to significant differences in model performance, as evidenced by the degradation of performance on other tasks.",
          "section": "Introduction"
        },
        {
          "quote": "The paper hypothesizes that the distribution gap between the task dataset and the seed LLM is the primary underlying cause of catastrophic forgetting, which is supported by the observation that vanilla fine-tuning on the Open Functions dataset results in a significant decrease in performance on other tasks.",
          "section": "Method -> Overview"
        }
      ],
      "b) Experiment-related Evidence": []
    },
    "Literature Gap Analysis": [],
    "Validation Analysis": {
      "Primary evidence summary": The paper states the hypothesis about the distribution gap and provides an example but lacks explicit citations or a detailed discussion of alternative explanations for catastrophic forgetting.
      "Supporting quotes": [
        "As the distribution of the seed LM converges towards that of the task dataset, it naturally enhances performance on target tasks.",
        "However, vanilla fine-tuning is susceptible to catastrophic forgetting in general instruction-following abilities and safety alignment.",
        "The distribution gap between the task dataset and the seed LLM can lead to significant differences in model performance, as evidenced by the degradation of performance on other tasks."
      ],
      "Impact assessment": The lack of justification weakens the motivation.
    },
    "Conclusion": {
      "Validity status": "Partially Valid",
      "Confidence level": "High",
      "Key supporting evidence": "While the paper states the hypothesis and provides an example, it lacks explicit citations or discussion of alternative explanations for catastrophic forgetting."
    }
  },
  {
    "Weakness Statement": "The proposed method is not novel, as it is very similar to the self-distillation approach used in Self-Rewarding Language Models. The paper does not adequately differentiate its approach from existing self-distillation methods, and it does not provide a detailed analysis of the unique aspects of its method. The paper should clearly articulate the novel contributions of its approach and provide a more thorough comparison to existing self-distillation methods.",
    "Evidence Collection": {
      "a) Method-related Evidence": [
        {
          "quote": "To address this issue, we propose S elf- D istillation F ine- T uning (SDFT), to better align the distribution of the task dataset with that of the seed LM.",
          "section": "Introduction"
        },
        {
          "quote": "As depicted in Figure 2 , the initial step of SDFT involves prompting the seed LM to rewrite the original response y t y^{t}\y^{t} into y ~ \sim \sim f θ ( y ∣ c t , x t , y t ) .",
          "section": "Method -> Workflow"
        },
        {
          "quote": "Next, to ensure the quality of the distilled responses, we employ simple heuristics to evaluate the distilled response. For instance, in math reasoning problems, we extract the final answer from the distilled response y ~ \tilde{y} \tilde{y} and compare it with the one from the original response y t y^{t} y^{t}. Otherwise, we keep the original response.",
          "section": "Method -> Workflow"
        },
        {
          "quote": "Finally, the distilled response is used as a replacement for the original response y t y^{t} y^{t} for fine-tuning, i.e., the loss becomes: L SDFT ( θ ) = − log f θ ( y ~ ′ ∣ c t , x t ) .",
          "section": "Method -> Workflow"
        }
      ],
      "b) Experiment-related Evidence": []
    },
    "Literature Gap Analysis": [
      "Missing citation for Self-Rewarding Language Models or a detailed comparison highlighting the differences."
    ],
    "Validation Analysis": {
      "Primary evidence summary": The paper introduces SDFT as a form of self-distillation but doesn't explicitly differentiate it from existing self-distillation techniques like Self-Rewarding Language Models.
      "Supporting quotes": [
        "To address this issue, we propose S elf- D istillation F ine- T uning (SDFT), to better align the distribution of the task dataset with that of the seed LM.",
        "As depicted in Figure 2 , the initial step of SDFT involves prompting the seed LM to rewrite the original response y t y^{t}\y^{t} into y ~ \sim \sim f θ ( y ∣ c t , x t , y t ) ."
      ],
      "Impact assessment": The lack of clear differentiation from existing self-distillation methods weakens the perceived novelty of the approach.
    },
    "Conclusion": {
      "Validity status": "Valid",
      "Confidence level": "High",
      "Key supporting evidence": "The paper describes the method as a form of self-distillation but lacks a detailed comparison to existing methods like Self-Rewarding Language Models to highlight its unique contributions."
    }
  },
  {
    "Weakness Statement": "The experiments are insufficient to fully evaluate the effectiveness of the proposed method. The experiments are limited to the Llama-2-chat model, and the paper does not explore the performance of the proposed method on other models. The paper should include experiments on a wider range of models to demonstrate the generalizability of the proposed method. Additionally, the paper does not provide a detailed analysis of the performance of the proposed method on different tasks, and it does not explore the limitations of the proposed method. The paper should include a more thorough analysis of the experimental results to provide a more comprehensive evaluation of the proposed method.",
    "Evidence Collection": {
      "a) Method-related Evidence": [],
      "b) Experiment-related Evidence": [
        {
          "quote": "We utilize the Llama-2-7b-chat model ( Touvron et al., 2023 ) as the seed LM in most of our experiments, except where explicitly stated otherwise.",
          "section": "Experimental Setup"
        },
        {
          "quote": "To substantiate this claim, we conducted supplementary experiments that included full fine-tuning on Llama-2-7b-chat and LoRA fine-tuning on Llama-2-7b-chat. Additionally, we explored the fine-tuning of the recently unveiled SOTA model, Llama3 Meta AI (2024) on the Open Functions dataset.",
          "section": "Experimental Setup"
        },
        {
          "quote": "Table 5 reveals that in all scenarios, SDFT not only consistently outperforms vanilla fine-tuning in the target task but also reduces forgetting across all other tasks, demonstrating its effectiveness.",
          "section": "Experiments -> SDFT Preserves Alignment -> Results -> Analysis"
        },
        {
          "quote": "In line with the patterns noted in Table 2 , fine-tuning on Alpaca, Dolly and LIMA typically leads to a marked reduction in both safety and helpfulness metrics.",
          "section": "Experiments -> SDFT Preserves Safety Alignment -> Results -> Analysis"
        }
      ]
    },
    "Literature Gap Analysis": [],
    "Validation Analysis": {
      "Primary evidence summary": The primary experiments use Llama-2-7b-chat. While Llama-3 is mentioned, the main analysis focuses on Llama-2. The analysis of performance on different tasks is present but could be more in-depth.
      "Supporting quotes": [
        "We utilize the Llama-2-7b-chat model ( Touvron et al., 2023 ) as the seed LM in most of our experiments, except where explicitly stated otherwise.",
        "Additionally, we explored the fine-tuning of the recently unveiled SOTA model, Llama3 Meta AI (2024) on the Open Functions dataset."
      ],
      "Impact assessment": The limited model diversity in the main experiments and the somewhat brief analysis of task performance support the reviewer's concern.
    },
    "Conclusion": {
      "Validity status": "Partially Valid",
      "Confidence level": "High",
      "Key supporting evidence": "The primary experiments use Llama-2-7b-chat. While Llama-3 is mentioned, the main analysis focuses on Llama-2. The analysis of performance on different tasks is present but could be more detailed."
    }
  },
  {
    "Weakness Statement": "How does the computational cost of SDFT compare to vanilla fine-tuning?",
    "Evidence Collection": {
      "a) Method-related Evidence": [],
      "b) Experiment-related Evidence": []
    },
    "Literature Gap Analysis": [],
    "Validation Analysis": {
      "Primary evidence summary": The paper does not provide a direct comparison of the computational cost between SDFT and vanilla fine-tuning.
      "Supporting quotes": [],
      "Impact assessment": The absence of this comparison makes it difficult to assess the practical trade-offs of using SDFT.
    },
    "Conclusion": {
      "Validity status": "Valid",
      "Confidence level": "High",
      "Key supporting evidence": "The paper lacks a direct comparison of computational costs between SDFT and vanilla fine-tuning."
    }
  },
  {
    "Weakness Statement": "What are the limitations of SDFT, and in what scenarios might it fail?",
    "Evidence Collection": {
      "a) Method-related Evidence": [],
      "b) Experiment-related Evidence": []
    },
    "Literature Gap Analysis": [],
    "Validation Analysis": {
      "Primary evidence summary": The paper does not explicitly discuss the limitations of SDFT or scenarios where it might fail.
      "Supporting quotes": [],
      "Impact assessment": The lack of discussion on limitations leaves a gap in understanding the scope and applicability of SDFT.
    },
    "Conclusion": {
      "Validity status": "Valid",
      "Confidence level": "High",
      "Key supporting evidence": "The paper does not explicitly discuss the limitations of SDFT."
    }
  },
  {
    "Weakness Statement": "How sensitive is SDFT to different hyperparameters, such as the size of the distilled dataset or the number of self-distillation iterations?",
    "Evidence Collection": {
      "a) Method-related Evidence": [
        {
          "quote": "The distillation template is designed to be task-independent, allowing for easy integration into various fine-tuning pipelines.",
          "section": "Method -> Distillation Template"
        }
      ],
      "b) Experiment-related Evidence": [
        {
          "quote": "We utilize the Llama-2-7b-chat model ( Touvron et al., 2023 ) as the seed LM in most of our experiments, except where explicitly stated otherwise.",
          "section": "Experimental Setup"
        }
      ]
    },
    "Literature Gap Analysis": [],
    "Validation Analysis": {
      "Primary evidence summary": The paper mentions the distillation template is task-independent but doesn't provide a detailed sensitivity analysis of hyperparameters like the size of the distilled dataset or the number of self-distillation iterations. The main experiments use a fixed distillation process.
      "Supporting quotes": [
        "The distillation template is designed to be task-independent, allowing for easy integration into various fine-tuning pipelines."
      ],
      "Impact assessment": The lack of hyperparameter sensitivity analysis limits the understanding of SDFT's robustness.
    },
    "Conclusion": {
      "Validity status": "Valid",
      "Confidence level": "High",
      "Key supporting evidence": "The paper does not include a detailed analysis of how SDFT's performance varies with different hyperparameters like the size of the distilled dataset or the number of self-distillation iterations."
    }
  },
  {
    "Weakness Statement": "The motivation behind the proposed method is not clearly explained. The authors claim that the distribution gap between the task dataset and the seed LLM is the primary underlying cause of catastrophic forgetting, but this claim lacks sufficient justification. It would be beneficial to include a more detailed analysis of how the distribution shift affects the model's parameters and leads to forgetting. For example, the authors could analyze the change in the model's embedding space or attention patterns after fine-tuning on a task with a different distribution than the original training data. This would provide a more concrete understanding of the underlying mechanism and strengthen the motivation for the proposed method. Furthermore, the paper should explore alternative explanations for catastrophic forgetting, such as the model's tendency to overfit to the training data, and provide empirical evidence to support its chosen explanation. A more thorough investigation of the underlying causes of catastrophic forgetting would significantly strengthen the motivation for the proposed method.",
    "Evidence Collection": {
      "a) Method-related Evidence": [
        {
          "quote": "As the distribution of the seed LM converges towards that of the task dataset, it naturally enhances performance on target tasks. However, vanilla fine-tuning is susceptible to catastrophic forgetting in general instruction-following abilities and safety alignment.",
          "section": "Introduction"
        },
        {
          "quote": "The distribution gap between the task dataset and the seed LLM can lead to significant differences in model performance, as evidenced by the degradation of performance on other tasks.",
          "section": "Introduction"
        },
        {
          "quote": "The paper hypothesizes that the distribution gap between the task dataset and the seed LLM is the primary underlying cause of catastrophic forgetting, which is supported by the observation that vanilla fine-tuning on the Open Functions dataset results in a significant decrease in performance on other tasks.",
          "section": "Method -> Overview"
        }
      ],
      "b) Experiment-related Evidence": []
    },
    "Literature Gap Analysis": [],
    "Validation Analysis": {
      "Primary evidence summary": The paper states the hypothesis about the distribution gap and provides an example but lacks explicit citations or a detailed discussion of alternative explanations for catastrophic forgetting. It doesn't include an analysis of parameter changes or embedding space alterations.
      "Supporting quotes": [
        "As the distribution of the seed LM converges towards that of the task dataset, it naturally enhances performance on target tasks.",
        "However, vanilla fine-tuning is susceptible to catastrophic forgetting in general instruction-following abilities and safety alignment.",
        "The distribution gap between the task dataset and the seed LLM can lead to significant differences in model performance, as evidenced by the degradation of performance on other tasks."
      ],
      "Impact assessment": The lack of detailed justification and analysis weakens the motivation.
    },
    "Conclusion": {
      "Validity status": "Partially Valid",
      "Confidence level": "High",
      "Key supporting evidence": "While the paper states the hypothesis and provides an example, it lacks explicit citations or discussion of alternative explanations for catastrophic forgetting. It doesn't include an analysis of parameter changes or embedding space alterations."
    }
  },
  {
    "Weakness Statement": "The proposed method is not novel, as it is very similar to the self-distillation approach used in Self-Rewarding Language Models. The paper does not adequately differentiate its approach from existing self-distillation methods, and it does not provide a detailed analysis of the unique aspects of its method. The paper should clearly articulate the novel contributions of its approach and provide a more thorough comparison to existing self-distillation methods. This comparison should not only highlight the similarities but also clearly articulate the novel contributions of the proposed method. For example, the paper could analyze the specific mechanisms by which the proposed method achieves self-distillation, and compare these mechanisms to those used in other self-distillation methods. The paper should also highlight the unique aspects of its method, such as the use of a distilled dataset, and explain how these aspects contribute to the effectiveness of the proposed method. A more detailed comparison to existing self-distillation methods would help to establish the novelty and significance of the proposed approach. The paper should also discuss the potential limitations of the proposed method in comparison to existing self-distillation methods.",
    "Evidence Collection": {
      "a) Method-related Evidence": [
        {
          "quote": "To address this issue, we propose S elf- D istillation F ine- T uning (SDFT), to better align the distribution of the task dataset with that of the seed LM.",
          "section": "Introduction"
        },
        {
          "quote": "As depicted in Figure 2 , the initial step of SDFT involves prompting the seed LM to rewrite the original response y t y^{t}\y^{t} into y ~ \sim \sim f θ ( y ∣ c t , x t , y t ) .",
          "section": "Method -> Workflow"
        },
        {
          "quote": "Next, to ensure the quality of the distilled responses, we employ simple heuristics to evaluate the distilled response. For instance, in math reasoning problems, we extract the final answer from the distilled response y ~ \tilde{y} \tilde{y} and compare it with the one from the original response y t y^{t} y^{t}. Otherwise, we keep the original response.",
          "section": "Method -> Workflow"
        },
        {
          "quote": "Finally, the distilled response is used as a replacement for the original response y t y^{t} y^{t} for fine-tuning, i.e., the loss becomes: L SDFT ( θ ) = − log f θ ( y ~ ′ ∣ c t , x t ) .",
          "section": "Method -> Workflow"
        }
      ],
      "b) Experiment-related Evidence": []
    },
    "Literature Gap Analysis": [
      "Missing citation for Self-Rewarding Language Models or a detailed comparison highlighting the differences."
    ],
    "Validation Analysis": {
      "Primary evidence summary": The paper introduces SDFT as a form of self-distillation but doesn't explicitly differentiate it from existing self-distillation techniques like Self-Rewarding Language Models.
      "Supporting quotes": [
        "To address this issue, we propose S elf- D istillation F ine- T uning (SDFT), to better align the distribution of the task dataset with that of the seed LM.",
        "As depicted in Figure 2 , the initial step of SDFT involves prompting the seed LM to rewrite the original response y t y^{t}\y^{t} into y ~ \sim \sim f θ ( y ∣ c t , x t , y t ) ."
      ],
      "Impact assessment": The lack of clear differentiation from existing self-distillation methods weakens the perceived novelty of the approach.
    },
    "Conclusion": {
      "Validity status": "Valid",
      "Confidence level": "High",
      "Key supporting evidence": "The paper describes the method as a form of self-distillation but lacks a detailed comparison to existing methods like Self-Rewarding Language Models to highlight its unique contributions."
    }
  },
  {
    "Weakness Statement": "The experiments are insufficient to fully evaluate the effectiveness of the proposed method. The experiments are limited to the Llama-2-chat model, and the paper does not explore the performance of the proposed method on other models. The paper should include experiments on a wider range of models to demonstrate the generalizability of the proposed method. Additionally, the paper does not provide a detailed analysis of the performance of the proposed method on different tasks, and it does not explore the limitations of the proposed method. The paper should include a more thorough analysis of the experimental results to provide a more comprehensive evaluation of the proposed method.",
    "Evidence Collection": {
      "a) Method-related Evidence": [],
      "b) Experiment-related Evidence": [
        {
          "quote": "We utilize the Llama-2-7b-chat model ( Touvron et al., 2023 ) as the seed LM in most of our experiments, except where explicitly stated otherwise.",
          "section": "Experimental Setup"
        },
        {
          "quote": "To substantiate this claim, we conducted supplementary experiments that included full fine-tuning on Llama-2-7b-chat and LoRA fine-tuning on Llama-2-7b-chat. Additionally, we explored the fine-tuning of the recently unveiled SOTA model, Llama3 Meta AI (2024) on the Open Functions dataset.",
          "section": "Experimental Setup"
        },
        {
          "quote": "Table 5 reveals that in all scenarios, SDFT not only consistently outperforms vanilla fine-tuning in the target task but also reduces forgetting across all other tasks, demonstrating its effectiveness.",
          "section": "Experiments -> SDFT Preserves Alignment -> Results -> Analysis"
        },
        {
          "quote": "In line with the patterns noted in Table 2 , fine-tuning on Alpaca, Dolly and LIMA typically leads to a marked reduction in both safety and helpfulness metrics.",
          "section": "Experiments -> SDFT Preserves Safety Alignment -> Results -> Analysis"
        }
      ]
    },
    "Literature Gap Analysis": [],
    "Validation Analysis": {
      "Primary evidence summary": The primary experiments use Llama-2-7b-chat. While Llama-3 is mentioned, the main analysis focuses on Llama-2. The analysis of performance on different tasks is present but could be more in-depth.
      "Supporting quotes": [
        "We utilize the Llama-2-7b-chat model ( Touvron et al., 2023 ) as the seed LM in most of our experiments, except where explicitly stated otherwise.",
        "Additionally, we explored the fine-tuning of the recently unveiled SOTA model, Llama3 Meta AI (2024) on the Open Functions dataset."
      ],
      "Impact assessment": The limited model diversity in the main experiments and the somewhat brief analysis of task performance support the reviewer's concern.
    },
    "Conclusion": {
      "Validity status": "Partially Valid",
      "Confidence level": "High",
      "Key supporting evidence": "The primary experiments use Llama-2-7b-chat. While Llama-3 is mentioned, the main analysis focuses on Llama-2. The analysis of performance on different tasks is present but could be more detailed."
    }
  },
  {
    "Weakness Statement": "How does the computational cost of SDFT compare to vanilla fine-tuning?",
    "Evidence Collection": {
      "a) Method-related Evidence": [],
      "b) Experiment-related Evidence": []
    },
    "Literature Gap Analysis": [],
    "Validation Analysis": {
      "Primary evidence summary": The paper does not provide a direct comparison of the computational cost between SDFT and vanilla fine-tuning.
      "Supporting quotes": [],
      "Impact assessment": The absence of this comparison makes it difficult to assess the practical trade-offs of using SDFT.
    },
    "Conclusion": {
      "Validity status": "Valid",
      "Confidence level": "High",
      "Key supporting evidence": "The paper lacks a direct comparison of computational costs between SDFT and vanilla fine-tuning."
    }
  },
  {
    "Weakness Statement": "What are the limitations of SDFT, and in what scenarios might it fail?",
    "Evidence Collection": {
      "a) Method-related Evidence": [],
      "b) Experiment-related Evidence": []
    },
    "Literature Gap Analysis": [],
    "Validation Analysis": {
      "Primary evidence summary": The paper does not explicitly discuss the limitations of SDFT or scenarios where it might fail.
      "Supporting quotes": [],
      "Impact assessment": The lack of discussion on limitations leaves a gap in understanding the scope and applicability of SDFT.
    },
    "Conclusion": {
      "Validity status": "Valid",
      "Confidence level": "High",
      "Key supporting evidence": "The paper does not explicitly discuss the limitations of SDFT."
    }
  },
  {
    "Weakness Statement": "How sensitive is SDFT to different hyperparameters, such as the size of the distilled dataset or the number of self-distillation iterations?",
    "Evidence Collection": {
      "a) Method-related Evidence": [
        {
          "quote": "The distillation template is designed to be task-independent, allowing for easy integration into various fine-tuning pipelines.",
          "section": "Method -> Distillation Template"
        }
      ],
      "b) Experiment-related Evidence": [
        {
          "quote": "We utilize the Llama-2-7b-chat model ( Touvron et al., 2023 ) as the seed LM in most of our experiments, except where explicitly stated otherwise.",
          "section": "Experimental Setup"
        }
      ]
    },
    "Literature Gap Analysis": [],
    "Validation Analysis": {
      "Primary evidence summary": The paper mentions the distillation template is task-independent but doesn't provide a detailed sensitivity analysis of hyperparameters like the size of the distilled dataset or the number of self-distillation iterations. The main experiments use a fixed distillation process.
      "Supporting quotes": [
        "The distillation template is designed to be task-independent, allowing for easy integration into various fine-tuning pipelines."
      ],
      "Impact assessment": The lack of hyperparameter sensitivity analysis limits the understanding of SDFT's robustness.
    },
    "Conclusion": {
      "Validity status": "Valid",
      "Confidence level": "High",
      "Key supporting evidence": "The paper does not}

Now, I have successfully verified each review. Next, I will organize this content and output the final review decision:

\boxed_review{
## Summary:

This paper introduces Self-Distillation Fine-Tuning (SDFT), a novel approach designed to mitigate catastrophic forgetting during the fine-tuning of large language models (LLMs). The core idea behind SDFT is to address the distribution gap that often exists between a pre-trained (seed) LLM and a task-specific fine-tuning dataset. The authors hypothesize that this distribution gap is a primary contributor to catastrophic forgetting, leading to a degradation of the model's general instruction-following abilities and safety alignment. To tackle this, SDFT prompts the seed LLM to rewrite original responses into semantically equivalent ones that are more representative of the target task. This process aims to create a distilled dataset that maintains the original distribution while better aligning with the fine-tuning objectives. The rewritten responses are then used as a replacement for the original responses during the fine-tuning process, effectively reducing the distribution shift and preserving the model's general capabilities. The authors evaluate SDFT on various benchmarks, including tasks from the Llama-2-chat model, and demonstrate that it achieves comparable or superior performance to vanilla fine-tuning while maintaining general instruction-following abilities and safety alignment. Specifically, the experiments involve fine-tuning the seed LLM on various datasets and then evaluating its performance on both the target task and other tasks to assess the preservation of general capabilities. The results show that SDFT consistently outperforms vanilla fine-tuning in terms of both target task performance and the preservation of general capabilities. The paper also explores the use of SDFT with different base models, including Llama-2-7b-chat and Llama-3, and with different fine-tuning techniques, such as full fine-tuning and LoRA. The authors also investigate the impact of using SDFT on different tasks, such as instruction following, math reasoning, and safety alignment. Overall, the paper presents a simple yet effective method for mitigating catastrophic forgetting during LLM fine-tuning, with promising empirical results. However, as I will discuss in the following sections, there are several limitations and areas for improvement that warrant further investigation.


## Soundness:

2.25


## Presentation:

3.0


## Contribution:

2.25


## Strengths:

The paper's primary strength lies in its clear and straightforward presentation of the proposed method, SDFT. The authors articulate the core idea of using self-distillation to mitigate catastrophic forgetting in a way that is easy to understand. The method itself is remarkably simple, which is a significant advantage in terms of practical applicability. The paper also presents a well-structured experimental evaluation. The authors conduct experiments on a variety of benchmarks and tasks, demonstrating the effectiveness of SDFT across different scenarios. The inclusion of experiments with different base models, such as Llama-2-7b-chat and Llama-3, and different fine-tuning techniques, such as full fine-tuning and LoRA, further strengthens the empirical evaluation. The results consistently show that SDFT achieves comparable or superior performance to vanilla fine-tuning while effectively preserving the model's general instruction-following abilities and safety alignment. This is a significant achievement, as many existing methods struggle to balance task-specific performance with the preservation of general capabilities. The paper also provides a detailed description of the experimental setup, including the datasets used, the evaluation metrics, and the hyperparameter settings. This level of detail allows for reproducibility and further research in this area. Furthermore, the authors explore the impact of SDFT on different tasks, such as instruction following, math reasoning, and safety alignment, which provides a more comprehensive understanding of the method's effectiveness. The use of heuristics to ensure the quality of the distilled responses is also a positive aspect of the method, as it helps to maintain the semantic equivalence between the original and rewritten responses. Finally, the paper's focus on a critical problem in LLM fine-tuning, namely catastrophic forgetting, is commendable. The authors have identified a significant challenge and have proposed a method that shows promise in addressing it. The simplicity of the method, combined with its effectiveness, makes it a valuable contribution to the field.


## Weaknesses:

Despite the strengths of the paper, several weaknesses warrant careful consideration. First, the motivation behind SDFT, specifically the claim that the distribution gap between the task dataset and the seed LLM is the primary cause of catastrophic forgetting, lacks sufficient justification. While the authors provide an example with the Open Functions dataset, they do not cite any specific literature or provide a detailed analysis to support this claim. This lack of evidence weakens the motivation for the proposed method. The paper states that the distribution gap leads to significant differences in model performance, as evidenced by the degradation of performance on other tasks, but it does not explore alternative explanations for catastrophic forgetting, such as the model's tendency to overfit to the training data. This omission is significant because it leaves the reader questioning whether the distribution gap is indeed the primary driver of forgetting or if other factors are at play. The paper also does not include a detailed analysis of the underlying causes of catastrophic forgetting, such as analyzing the change in the model's embedding space or attention patterns after fine-tuning on a task with a different distribution than the original training data. This lack of analysis limits the understanding of the underlying mechanisms and the effectiveness of the proposed approach. My confidence in this weakness is high, as the paper explicitly states the hypothesis about the distribution gap without providing sufficient justification or exploring alternative explanations. Second, the proposed method, SDFT, is not entirely novel. The authors present SDFT as a form of self-distillation, but it is very similar to existing self-distillation methods, particularly Self-Rewarding Language Models. The paper does not adequately differentiate its approach from these existing methods, nor does it provide a detailed analysis of the unique aspects of its method. The paper describes the method as a form of self-distillation but lacks a detailed comparison to existing methods like Self-Rewarding Language Models to highlight its unique contributions. This lack of differentiation weakens the perceived novelty of the approach and raises questions about the significance of the proposed method. My confidence in this weakness is high, as the paper describes the method as a form of self-distillation but lacks a detailed comparison to existing methods like Self-Rewarding Language Models to highlight its unique contributions. Third, the experiments are insufficient to fully evaluate the effectiveness of the proposed method. The experiments are primarily conducted using the Llama-2-7b-chat model, and while the paper mentions fine-tuning Llama-3 on the Open Functions dataset, the main analysis focuses on Llama-2. The paper should include experiments on a wider range of models to demonstrate the generalizability of the proposed method. Additionally, the paper does not provide a detailed analysis of the performance of the proposed method on different tasks, and it does not explore the limitations of the proposed method. The paper should include a more thorough analysis of the experimental results to provide a more comprehensive evaluation of the proposed method. My confidence in this weakness is high, as the primary experiments use Llama-2-7b-chat. While Llama-3 is mentioned, the main analysis focuses on Llama-2. The analysis of performance on different tasks is present but could be more detailed. Fourth, the paper does not provide a direct comparison of the computational cost between SDFT and vanilla fine-tuning. This omission makes it difficult to assess the practical trade-offs of using SDFT, as it is unclear whether the performance gains justify the additional computational cost. My confidence in this weakness is high, as the paper lacks a direct comparison of computational costs between SDFT and vanilla fine-tuning. Fifth, the paper does not explicitly discuss the limitations of SDFT or scenarios where it might fail. This lack of discussion leaves a gap in understanding the scope and applicability of SDFT. My confidence in this weakness is high, as the paper does not explicitly discuss the limitations of SDFT. Finally, the paper does not include a detailed analysis of how SDFT's performance varies with different hyperparameters, such as the size of the distilled dataset or the number of self-distillation iterations. This lack of sensitivity analysis limits the understanding of SDFT's robustness. My confidence in this weakness is high, as the paper does not include a detailed analysis of how SDFT's performance varies with different hyperparameters like the size of the distilled dataset or the number of self-distillation iterations.


## Suggestions:

To address the identified weaknesses, I recommend several concrete improvements. First, the authors should provide a more robust justification for their core claim that the distribution gap between the task dataset and the seed LLM is the primary cause of catastrophic forgetting. This could involve a more detailed analysis of the feature space of the models before and after fine-tuning, or an investigation of the model's internal representations to understand how the distribution shift affects its performance. Furthermore, the authors should explore alternative explanations for catastrophic forgetting, such as the model's tendency to overfit to the training data, and provide empirical evidence to support their chosen explanation. A more thorough investigation of the underlying causes of catastrophic forgetting would significantly strengthen the motivation for the proposed method. Second, the authors should clearly articulate the novel contributions of their approach and provide a more thorough comparison to existing self-distillation methods, particularly Self-Rewarding Language Models. This comparison should not only highlight the similarities but also clearly articulate the unique aspects of the proposed method. The authors should analyze the specific mechanisms by which the proposed method achieves self-distillation and compare these mechanisms to those used in other self-distillation methods. The paper should also highlight the unique aspects of its method, such as the use of a distilled dataset, and explain how these aspects contribute to the effectiveness of the proposed method. A more detailed comparison to existing self-distillation methods would help to establish the novelty and significance of the proposed approach. Third, the authors should significantly expand their experimental evaluation to demonstrate the generalizability and robustness of the proposed method. This should include experiments on a wider range of models, including both smaller and larger models, to assess the scalability of the method. The paper should also include experiments on a more diverse set of tasks, to evaluate the performance of the proposed method on different types of problems. Additionally, the paper should provide a more detailed analysis of the experimental results, including an investigation of the limitations of the proposed method and the conditions under which it performs well or poorly. A more comprehensive experimental evaluation would provide a more robust assessment of the proposed method and its potential impact. Fourth, the authors should provide a detailed comparison of the computational cost of SDFT compared to vanilla fine-tuning. This analysis should include the time and memory requirements for different model sizes and dataset sizes. Furthermore, it would be beneficial to explore the scalability of SDFT with respect to the size of the seed model and the size of the distilled dataset. This would help to determine the practical applicability of the method to different model sizes and computational resources. Fifth, the authors should include a more comprehensive discussion of the limitations of SDFT, including its potential sensitivity to the quality of the distilled dataset or the potential for introducing bias during the self-distillation process. This would provide a more balanced and realistic assessment of the proposed method. Finally, the authors should include a more detailed analysis of the sensitivity of SDFT to its hyperparameters. The authors should investigate how the size of the distilled dataset affects the performance of SDFT, and whether there is an optimal size for the distilled dataset. Similarly, the authors should explore the impact of the number of self-distillation iterations on the performance of SDFT. It would be useful to provide guidelines for selecting these hyperparameters based on the characteristics of the target task and the available computational resources. For example, the authors could perform a grid search over the hyperparameter space and report the performance of SDFT for different hyperparameter settings. This would provide a more complete picture of the practical applicability of the method and help users to effectively tune the method for their specific use cases.


## Questions:

Several key questions arise from my analysis of the paper. First, how does the computational cost of SDFT compare to vanilla fine-tuning? The paper does not provide a direct comparison of the computational cost, and it is unclear whether the performance gains justify the additional computational cost. Second, what are the limitations of SDFT, and in what scenarios might it fail? The paper does not explicitly discuss the limitations of SDFT or scenarios where it might fail, and it would be beneficial to have a more comprehensive understanding of the method's scope and applicability. Third, how sensitive is SDFT to different hyperparameters, such as the size of the distilled dataset or the number of self-distillation iterations? The paper does not include a detailed analysis of how SDFT's performance varies with different hyperparameters, and it would be useful to have guidelines for selecting these hyperparameters based on the characteristics of the target task and the available computational resources. Fourth, how does SDFT compare to other methods that address catastrophic forgetting, such as regularization-based approaches or replay-based methods? The paper does not provide a detailed comparison with these methods, and it would be beneficial to understand the relative strengths and weaknesses of SDFT compared to other approaches. Fifth, what is the impact of the quality of the distilled dataset on the performance of SDFT? The paper does not explicitly address this question, and it would be useful to understand how the quality of the distilled dataset affects the performance of SDFT. Finally, how does the performance of SDFT vary across different types of tasks, such as those used for distillation (e.g., math reasoning, code generation, question-answering)? The paper does not provide a detailed analysis of the performance of SDFT on different types of tasks, and it would be beneficial to understand the method's performance on tasks that are used for distillation.


## Rating:

4.25


## Confidence:

4.0


## Decision:

Reject
}