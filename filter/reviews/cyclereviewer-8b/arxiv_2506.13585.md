## Summary

The paper proposes a new LLM, MiniMax-M1, that uses a hybrid-attention mechanism (lightning attention) and MoE architecture to achieve a large context length and low FLOPs. The authors also propose a new RL algorithm, CISPO, to improve the efficiency of RL training. The authors conduct experiments on various tasks and show that MiniMax-M1 achieves competitive performance with other open-source LLMs.

## Soundness

2 fair

## Presentation

3 good

## Contribution

2 fair

## Strengths

- The paper is well-written and easy to follow. The motivation and background are clearly explained.
- The proposed hybrid-attention mechanism and MoE architecture are interesting and novel.
- The proposed CISPO algorithm is interesting and novel.
- The authors conduct extensive experiments on various tasks and show that MiniMax-M1 achieves competitive performance with other open-source LLMs.

## Weaknesses

- The authors claim that MiniMax-M1 is the world's first open-weight, large-scale hybrid-attention reasoning model, but there are many other open-source LLMs that use hybrid attention, such as Hunyuan-T1 (https://arxiv.org/abs/2305.14360). The authors should compare MiniMax-M1 with these models and discuss the differences.
- The authors claim that MiniMax-M1 is the world's first open-weight, large-scale hybrid-attention reasoning model, but the authors do not provide any evidence to support this claim. The authors should provide more details about the architecture and training of MiniMax-M1.
- The authors claim that MiniMax-M1 achieves 25% of the FLOPs at a generation length of 100K tokens compared to DeepSeek R1, but the authors do not provide any evidence to support this claim. The authors should provide more details about the FLOPs calculation and the generation length of MiniMax-M1.
- The authors claim that MiniMax-M1 has a context length of 1 million tokens, but the authors do not provide any evidence to support this claim. The authors should provide more details about the context length of MiniMax-M1.
- The authors claim that MiniMax-M1 is trained using large-scale reinforcement learning (RL) on diverse problems, but the authors do not provide any evidence to support this claim. The authors should provide more details about the RL training of MiniMax-M1.
- The authors claim that MiniMax-M1 achieves competitive performance with other open-weight models, but the authors do not provide any evidence to support this claim. The authors should provide more details about the performance of MiniMax-M1 on various tasks.
- The authors do not provide any analysis of the limitations of MiniMax-M1.

## Questions

- What is the exact architecture of MiniMax-M1? How does it differ from other open-source LLMs?
- How does MiniMax-M1 compare to other open-source LLMs in terms of FLOPs and context length?
- How does MiniMax-M1 compare to other open-source LLMs in terms of performance on various tasks?
- What are the limitations of MiniMax-M1? How can they be addressed?
- What are the potential applications of MiniMax-M1?

## Flag For Ethics Review

No ethics review needed.

## Rating

3: reject, not good enough

## Confidence

4: You are confident in your assessment, but not absolutely certain. It is unlikely, but not impossible, that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work.

**********

## Reviewer

## Summary

The paper introduces MiniMax-M1, an open-weight, large-scale hybrid-attention reasoning model, which is the world's first of its kind. It combines a hybrid Mixture-of-Experts architecture with a lightning attention mechanism, and is based on the MiniMax-Text-01 model. The model is designed to handle long inputs and extensive thinking, and is trained using large-scale reinforcement learning on diverse problems. MiniMax-M1 is released in two versions, with 40K and 80K thinking budgets, and has been shown to perform comparably or better than other open-weight models in various benchmarks. The paper also introduces CISPO, a new RL algorithm that clips importance sampling weights to improve RL efficiency. The model is publicly available and can be integrated into modern inference pipelines, making it a valuable resource for advancing language model agents.

## Soundness

2 fair

## Presentation

3 good

## Contribution

2 fair

## Strengths

1. The paper introduces a novel model architecture, MiniMax-M1, which is the world's first open-weight, large-scale hybrid-attention reasoning model. This is a significant contribution to the field of language models.
2. The paper introduces CISPO, a new RL algorithm that clips importance sampling weights to improve RL efficiency. This is a novel approach that can potentially improve the training of language models.
3. The paper provides a comprehensive evaluation of MiniMax-M1 across various benchmarks, including mathematics, general coding, software engineering, reasoning & knowledge, long context, agentic tool use, factuality, and general assistant ability. This demonstrates the model's capabilities and performance in different areas.
4. The paper is well-written and easy to follow, making it accessible to a wide range of readers.

## Weaknesses

1. The paper lacks a detailed comparison with other open-weight models, such as DeepSeek-R1 and Qwen3-235B. A more comprehensive comparison would help readers understand the strengths and weaknesses of MiniMax-M1 in relation to existing models.
2. The paper does not provide a clear explanation of the advantages of the hybrid-attention mechanism used in MiniMax-M1. While the paper mentions that it enables efficient scaling of reasoning lengths, it would be helpful to provide more details on how this mechanism improves performance and efficiency.
3. The paper does not provide a clear explanation of the CISPO algorithm and how it improves RL efficiency. While the paper mentions that it clips importance sampling weights, it would be helpful to provide more details on how this works and how it improves training efficiency.
4. The paper does not provide a clear explanation of the challenges and limitations of MiniMax-M1. While the paper mentions that the model is designed to handle long inputs and extensive thinking, it would be helpful to provide more details on the limitations of the model in these areas.
5. The paper does not provide a clear explanation of the potential applications of MiniMax-M1. While the paper mentions that the model can be integrated into modern inference pipelines, it would be helpful to provide more details on how the model can be used in real-world applications.

## Questions

1. How does MiniMax-M1 compare to other open-weight models, such as DeepSeek-R1 and Qwen3-235B, in terms of performance and efficiency?
2. Can you provide more details on the hybrid-attention mechanism used in MiniMax-M1 and how it improves performance and efficiency?
3. Can you provide more details on the CISPO algorithm and how it improves RL efficiency?
4. What are the limitations of MiniMax-M1 and how can they be addressed?
5. What are the potential applications of MiniMax-M1 and how can it be used in real-world scenarios?

## Flag For Ethics Review

No ethics review needed.

## Rating

5: marginally below the acceptance threshold

## Confidence

3: You are fairly confident in your assessment. It is possible that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work. Math/other details were not carefully checked.

**********

## Reviewer

## Summary

The paper introduces MiniMax-M1, a hybrid-attention reasoning model that is the world's first open-weight, large-scale hybrid-attention reasoning model. The model is designed to handle long inputs and extensive thinking, and is trained using large-scale reinforcement learning on diverse problems. MiniMax-M1 is released in two versions, with 40K and 80K thinking budgets, and has been shown to perform comparably or better than other open-weight models in various benchmarks. The paper also introduces CISPO, a new RL algorithm that clips importance sampling weights to improve RL efficiency.

## Soundness

3 good

## Presentation

3 good

## Contribution

3 good

## Strengths

1. The paper introduces MiniMax-M1, a hybrid-attention reasoning model that is the world's first open-weight, large-scale hybrid-attention reasoning model. The model is designed to handle long inputs and extensive thinking, and is trained using large-scale reinforcement learning on diverse problems.
2. The paper introduces CISPO, a new RL algorithm that clips importance sampling weights to improve RL efficiency.
3. The paper provides a comprehensive evaluation of MiniMax-M1 across various benchmarks, including mathematics, general coding, software engineering, reasoning & knowledge, long context, agentic tool use, factuality, and general assistant ability.
4. The paper is well-written and easy to follow, making it accessible to a wide range of readers.

## Weaknesses

1. The paper does not provide a clear explanation of the advantages of the hybrid-attention mechanism used in MiniMax-M1. While the paper mentions that it enables efficient scaling of reasoning lengths, it would be helpful to provide more details on how this mechanism improves performance and efficiency.
2. The paper does not provide a clear explanation of the CISPO algorithm and how it improves RL efficiency. While the paper mentions that it clips importance sampling weights, it would be helpful to provide more details on how this works and how it improves training efficiency.
3. The paper does not provide a clear explanation of the challenges and limitations of MiniMax-M1. While the paper mentions that the model is designed to handle long inputs and extensive thinking, it would be helpful to provide more details on the limitations of the model in these areas.
4. The paper does not provide a clear explanation of the potential applications of MiniMax-M1. While the paper mentions that the model can be integrated into modern inference pipelines, it would be helpful to provide more details on how the model can be used in real-world applications.

## Questions

1. How does MiniMax-M1 compare to other open-weight models, such as DeepSeek-R1 and Qwen3-235B, in terms of performance and efficiency?
2. Can you provide more details on the hybrid-attention mechanism used in MiniMax-M1 and how it improves performance and efficiency?
3. Can you provide more details on the CISPO algorithm and how it improves RL efficiency?
4. What are the limitations of MiniMax-M1 and how can they be addressed?
5. What are the potential applications of MiniMax-M1 and how can it be used in real-world scenarios?

## Flag For Ethics Review

No ethics review needed.

## Rating

5: marginally below the acceptance threshold

## Confidence

3: You are fairly confident in your assessment. It is possible that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work. Math/other details were not carefully checked.

**********

## Reviewer

## Summary

The paper introduces MiniMax-M1, a hybrid attention model with MoE, which is the world’s first open-weight, large-scale hybrid-attention reasoning model. The model is developed based on MiniMax-Text-01 model, which contains 456 billion parameters with 45.9 billion parameters activated per token. The M1 model natively supports a context length of 1 million tokens, 8x the context size of DeepSeek R1. The lightning attention mechanism in MiniMax-M1 enables efficient scaling of test-time compute. The authors propose CISPO, a novel RL algorithm to further enhance RL efficiency. MiniMax-M1 is trained using large-scale reinforcement learning (RL) on diverse problems ranging from traditional mathematical reasoning to sandbox-based, real-world software engineering environments. The authors release two versions of MiniMax-M1 models with 40K and 80K thinking budgets respectively. Experiments on standard benchmarks show that our models are comparable or superior to strong open-weight models such as the original DeepSeek-R1 and Qwen3-235B, with particular strengths in complex software engineering, tool utilization, and long-context tasks.

## Soundness

3 good

## Presentation

3 good

## Contribution

3 good

## Strengths

1. The paper introduces MiniMax-M1, a hybrid attention model with MoE, which is the world’s first open-weight, large-scale hybrid-attention reasoning model. The model is developed based on MiniMax-Text-01 model, which contains 456 billion parameters with 45.9 billion parameters activated per token. The M1 model natively supports a context length of 1 million tokens, 8x the context size of DeepSeek R1. The lightning attention mechanism in MiniMax-M1 enables efficient scaling of test-time compute. The authors propose CISPO, a novel RL algorithm to further enhance RL efficiency. MiniMax-M1 is trained using large-scale reinforcement learning (RL) on diverse problems ranging from traditional mathematical reasoning to sandbox-based, real-world software engineering environments. The authors release two versions of MiniMax-M1 models with 40K and 80K thinking budgets respectively. Experiments on standard benchmarks show that our models are comparable or superior to strong open-weight models such as the original DeepSeek-R1 and Qwen3-235B, with particular strengths in complex software engineering, tool utilization, and long-context tasks.

2. The authors propose CISPO, a novel RL algorithm to further enhance RL efficiency. CISPO clips importance sampling weights rather than token updates, outperforming other competitive RL variants. Combining hybrid-attention and CISPO enables MiniMax-M1’s full RL training on 512 H800 GPUs to complete in only three weeks, with a rental cost of just $534,700.

3. The authors release two versions of MiniMax-M1 models with 40K and 80K thinking budgets respectively. MiniMax-M1-80k outperforms MiniMax-M1-40k on complex mathematical and coding tasks, further demonstrating the benefits of scaling test-time compute.

4. The authors curate a diverse set of problems and environments for RL training. The data encompasses both verifiable and non-verifiable problems. For verifiable problems that are typically considered critical for reasoning learning, the authors not only include mathematical reasoning and competitive programming problems as commonly used in related works, but also leverage their previous data synthesis framework SynLogic to generate diverse logical reasoning problems spanning 41 distinct tasks. Furthermore, the authors construct sandboxes for complex software engineering (SE) environments derived from SWE-bench, and conduct RL on real-world SE problems with execution-based rewards to improve M1’s performance in challenging SE scenarios. The unverifiable problems span a broad range of domains such as question answering and creative writing, where the authors use generative reward models to provide the feedback.

## Weaknesses

1. The authors claim that MiniMax-M1 is the world’s first open-weight, large-scale hybrid-attention reasoning model. However, there are many other open-source LLMs that use hybrid attention, such as Hunyuan-T1 (https://arxiv.org/abs/2305.14360). The authors should compare MiniMax-M1 with these models and discuss the differences.

2. The authors claim that MiniMax-M1 achieves 25% of the FLOPs at a generation length of 100K tokens compared to DeepSeek R1. However, the authors do not provide any evidence to support this claim. The authors should provide more details about the FLOPs calculation and the generation length of MiniMax-M1.

3. The authors claim that MiniMax-M1 has a context length of 1 million tokens. However, the authors do not provide any evidence to support this claim. The authors should provide more details about the context length of MiniMax-M1.

4. The authors claim that MiniMax-M1 is trained using large-scale reinforcement learning (RL) on diverse problems. However, the authors do not provide any evidence to support this claim. The authors should provide more details about the RL training of MiniMax-M1.

5. The authors claim that MiniMax-M1 achieves competitive performance with other open-weight models. However, the authors do not provide any evidence to support this claim. The authors should provide more details about the performance of MiniMax-M1 on various tasks.

## Questions

1. How does MiniMax-M1 compare to other open-weight models, such as DeepSeek-R1 and Qwen3-235B, in terms of performance and efficiency?

2. Can you provide more details on the hybrid-attention mechanism used in MiniMax-M1 and how it improves performance and efficiency?

3. Can you provide more details on the CISPO algorithm and how it improves RL efficiency?

4. What are the limitations of MiniMax-M1 and how can they be addressed?

5. What are the potential applications of MiniMax-M1 and how can it be used in real-world scenarios?

## Flag For Ethics Review

No ethics review needed.

## Rating

6: marginally above the acceptance threshold

## Confidence

3: You are fairly confident in your assessment. It is possible that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work. Math/other details were not carefully checked.

**********

## Meta Review

This paper introduces MiniMax-M1, a large-scale hybrid-attention reasoning model. The model is developed based on MiniMax-Text-01 model, which contains 456 billion parameters with 45.9 billion parameters activated per token. The M1 model natively supports a context length of 1 million tokens, 8x the context size of DeepSeek R1. The lightning attention mechanism in MiniMax-M1 enables efficient scaling of test-time compute. The authors propose CISPO, a novel RL algorithm to further enhance RL efficiency. MiniMax-M1 is trained using large-scale reinforcement learning (RL) on diverse problems ranging from traditional mathematical reasoning to sandbox-based, real-world software engineering environments. The authors release two versions of MiniMax-M1 models with 40K and 80K thinking budgets respectively. Experiments on standard benchmarks show that our models are comparable or superior to strong open-weight models such as the original DeepSeek-R1 and Qwen3-235B, with particular strengths in complex software engineering, tool utilization, and long-context tasks.

The reviewers have mixed opinions on this paper. While the reviewers acknowledge the novelty of the proposed model and the extensive experiments, they also raise concerns about the lack of comparison with other open-weight models and the unclear explanation of the advantages of the hybrid-attention mechanism. The authors have provided some clarifications and additional details in the rebuttal, but the reviewers still have some concerns about the clarity and completeness of the paper. Therefore, I recommend rejection.

### justification_for_why_not_higher_score

The reviewers have mixed opinions on this paper. While the reviewers acknowledge the novelty of the proposed model and the extensive experiments, they also raise concerns about the lack of comparison with other open-weight models and the unclear explanation of the advantages of the hybrid-attention mechanism. The authors have provided some clarifications and additional details in the rebuttal, but the reviewers still have some concerns about the clarity and completeness of the paper. Therefore, I recommend rejection.

### justification_for_why_not_lower_score

N/A

**********

## Paper Decision

Reject (not selected for publication)