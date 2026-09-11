# Review

## Summary
This paper introduces Self-Distillation Fine-Tuning (SDFT), a novel approach to address the challenge of balancing performance and preserving general instruction-following abilities in Large Language Models (LLMs) during fine-tuning for specific tasks. The primary cause identified for the degradation of LLMs' general capabilities during fine-tuning is the distribution gap between task datasets and the LLMs. SDFT mitigates this issue by generating a distilled dataset through the LLM itself to match its original distribution. Experimental results on the Llama-2-chat model across various benchmarks demonstrate that SDFT effectively mitigates catastrophic forgetting while achieving comparable or superior performance on downstream tasks compared to vanilla fine-tuning. Additionally, SDFT shows potential in maintaining the helpfulness and safety alignment of LLMs.

## Soundness
3

## Presentation
3

## Contribution
3

## Strengths
1. The paper introduces a novel approach, Self-Distillation Fine-Tuning (SDFT), which addresses the critical issue of balancing performance and preserving general instruction-following abilities in Large Language Models (LLMs) during fine-tuning for specific tasks. This is a significant contribution to the field of natural language processing.
2. The paper provides a thorough analysis of the problem, identifying the distribution gap between task datasets and LLMs as the primary cause of performance degradation. This analysis is backed by empirical evidence and theoretical reasoning, adding depth to the understanding of the issue.
3. The proposed SDFT method is innovative, utilizing the LLM itself to generate a distilled dataset that bridges the distribution gap. This approach is practical and has the potential for wide adoption in the research community.
4. The experimental results on the Llama-2-chat model across various benchmarks are impressive, showing that SDFT effectively mitigates catastrophic forgetting while achieving comparable or superior performance on downstream tasks compared to vanilla fine-tuning. This demonstrates the effectiveness of the proposed method.
5. The paper discusses the potential of SDFT in maintaining the helpfulness and safety alignment of LLMs, which is crucial for the deployment of LLMs in real-world applications.

## Weaknesses
1. The paper primarily focuses on the Llama-2-chat model and may not have been tested extensively across a variety of LLMs, which could limit the generalizability of the findings.
2. The experiments are based on a limited number of datasets, which may not fully represent the diversity of tasks and data distributions encountered in real-world applications.
3. The paper does not provide a detailed analysis of the computational resources required for implementing SDFT, which could be a barrier to adoption for some researchers or practitioners.

## Questions
1. Have you tested SDFT on other LLMs besides the Llama-2-chat model? If so, how did it perform? If not, what are the potential challenges or limitations you foresee in applying SDFT to other LLMs?
2. Can you provide more details on the computational resources required for implementing SDFT? How does it compare to vanilla fine-tuning in terms of time and memory consumption?
3. How does SDFT perform on more complex tasks or domains, such as legal or medical text processing? Have you considered any specific challenges in these areas?
4. How does SDFT handle extremely large datasets or real-time streaming data? What are the potential limitations or considerations in these scenarios?
5. How does SDFT integrate with other emerging technologies, such as multi-modal LLMs or LLMs for vision tasks? What are the potential challenges or opportunities in these areas?

## Flag For Ethics Review
No ethics review needed.

## Details Of Ethics Concerns


## Rating
8

## Confidence
4