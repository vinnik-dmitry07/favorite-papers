# Review

## Summary
The paper introduces a new benchmark called BIG-bench, which consists of 204 tasks contributed by 450 authors across 132 institutions. The tasks in BIG-bench are designed to be challenging and diverse, covering topics such as linguistics, childhood development, math, common sense reasoning, biology, physics, social bias, and software development. The authors evaluate the performance of various language models on BIG-bench, including OpenAI's GPT models, Google-internal dense transformer architectures, and Switch-style sparse transformers. The evaluation spans model sizes ranging from millions to hundreds of billions of parameters. Additionally, human expert raters are employed to provide a strong baseline for comparison. The findings of the evaluation include: (1) model performance and calibration both improve with scale, but are still poor in absolute terms compared to human raters; (2) performance is similar across different model classes, with benefits from sparsity; (3) tasks that improve gradually and predictably often involve a large knowledge or memorization component, while tasks that exhibit "breakthrough" behavior at a critical scale often involve multiple steps or components, or brittle metrics; (4) social bias typically increases with scale in settings with ambiguous context, but can be improved with prompting.

## Soundness
3

## Presentation
3

## Contribution
3

## Strengths
1. The paper introduces a new benchmark called BIG-bench, which consists of 204 tasks contributed by 450 authors across 132 institutions. The tasks in BIG-bench are designed to be challenging and diverse, covering topics such as linguistics, childhood development, math, common sense reasoning, biology, physics, social bias, and software development. This benchmark provides a comprehensive and diverse set of tasks for evaluating the capabilities and limitations of language models.

2. The authors evaluate the performance of various language models on BIG-bench, including OpenAI's GPT models, Google-internal dense transformer architectures, and Switch-style sparse transformers. The evaluation spans model sizes ranging from millions to hundreds of billions of parameters. This evaluation provides a thorough comparison of different language models across a wide range of tasks and model sizes.

3. Human expert raters are employed to provide a strong baseline for comparison. This allows for a clear comparison between the performance of language models and human capabilities, providing insights into the strengths and weaknesses of language models in relation to human intelligence.

4. The paper provides detailed analysis of the evaluation results, including insights into the impact of model scale, the similarity of performance across different model classes, and the influence of task design on model performance. This analysis provides valuable insights into the behavior of language models and their limitations.

## Weaknesses
1. The paper does not provide a detailed discussion of the limitations of the BIG-bench benchmark. It would be helpful to have a more comprehensive discussion of the potential limitations and biases of the benchmark, as well as any potential ethical considerations.

2. The paper does not provide a detailed discussion of the potential ethical implications of the findings, such as the potential risks and challenges associated with the development and deployment of language models with enhanced capabilities. It would be helpful to have a more comprehensive discussion of the ethical considerations related to the findings.

3. The paper does not provide a detailed discussion of the potential future directions for research, such as how to further improve language models based on the findings of this study. It would be helpful to have a more comprehensive discussion of the potential future research directions and how the findings of this study can inform and guide future research in this area.

## Questions
1. What are the limitations of the BIG-bench benchmark? How might these limitations affect the evaluation and development of language models?

2. What are the potential ethical implications of the findings? How might the enhanced capabilities of language models pose risks or challenges for society?

3. What are the potential future directions for research based on the findings of this study? How can the findings of this study inform and guide future research in this area?

## Flag For Ethics Review
No ethics review needed.

## Details Of Ethics Concerns


## Rating
6

## Confidence
4