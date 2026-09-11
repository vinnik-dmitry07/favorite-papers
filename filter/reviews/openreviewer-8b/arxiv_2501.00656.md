# Review

## Summary
This paper introduces OLMo 2, a new generation of open language models. OLMo 2 includes a family of dense autoregressive language models at 7B, 13B, and 32B scales, with fully released artifacts such as model weights, training data, training code, recipes, training logs, and thousands of intermediate checkpoints. The paper describes the modified model architecture and training recipe, focusing on techniques for achieving better training stability and improved per-token efficiency. It introduces a new data mix called Dolmino Mix 1124, which significantly improves model capabilities across various downstream task benchmarks when used in the annealing phase of pretraining. The paper also incorporates best practices from Tulu 3 to develop OLMo 2-Instruct, focusing on permissive data and extending the final-stage reinforcement learning with verifiable rewards (RLVR). The OLMo 2 base models are claimed to sit at the Pareto frontier of performance to training compute, often matching or outperforming open-weight only models like Llama 3.1, Qwen 2.5, and Gemma 2 while using fewer FLOPs. The fully open OLMo 2-Instruct models are said to be competitive with open-weight only models of comparable size and even some proprietary models like GPT-3.5 Turbo and GPT 4o Mini.

## Soundness
3

## Presentation
3

## Contribution
3

## Strengths
1. The paper provides a comprehensive description of the OLMo 2 model, including its architecture, training data, training recipe, and evaluation results. The release of all training code, data, and recipes under permissive licenses promotes transparency and reproducibility in language model research.
2. The paper introduces a new data mix called Dolmino Mix 1124, which is shown to significantly improve model capabilities across various downstream task benchmarks. The incorporation of best practices from Tulu 3 into OLMo 2-Instruct enhances the model's ability to be finetuned to downstream use-cases.
3. The OLMo 2 base models are claimed to sit at the Pareto frontier of performance to training compute, matching or outperforming open-weight only models while using fewer FLOPs. The fully open OLMo 2-Instruct models are competitive with open-weight only models of comparable size and even some proprietary models.

## Weaknesses
1. The paper does not provide a detailed comparison of OLMo 2 with other open language models, making it difficult to assess its relative performance and capabilities. The paper could benefit from a more comprehensive comparison with other state-of-the-art language models, both open-weight and proprietary, to provide a clearer understanding of its strengths and weaknesses.
2. The paper does not provide a detailed analysis of the limitations of OLMo 2 or potential areas for improvement. It would be valuable to discuss any limitations of the model, such as its performance on specific tasks or domains, and suggest potential directions for future research to address these limitations.

## Questions
1. Can you provide more details on the specific techniques used to improve training stability, such as the initialization scheme, architectural changes, and hyperparameter tuning?
2. How does OLMo 2 compare to other state-of-the-art language models in terms of performance on various downstream tasks? Can you provide a more comprehensive comparison with other open-weight and proprietary models?
3. What are the limitations of OLMo 2, and how might they be addressed in future research? It would be helpful to have a more detailed discussion of potential areas for improvement.

## Flag For Ethics Review
No ethics review needed.

## Details Of Ethics Concerns


## Rating
8

## Confidence
4