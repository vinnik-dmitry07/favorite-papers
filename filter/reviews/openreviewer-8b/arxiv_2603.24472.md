# Review

## Summary
This paper explores the effects of self-distillation on the reasoning capabilities of large language models (LLMs), specifically focusing on mathematical reasoning tasks. The authors find that while self-distillation can reduce response length, it may degrade performance on math tasks by suppressing the model's ability to express uncertainty during reasoning, a phenomenon they term "epistemic verbalization." Through controlled experiments, they demonstrate that providing rich information to the teacher model (e.g., correct solutions) leads to more concise but less uncertain reasoning in the student model, which is effective for in-domain tasks but can hurt out-of-distribution (OOD) performance. The study highlights the importance of optimizing for uncertainty expression in reasoning tasks and suggests that simply reinforcing correct answers may not be sufficient for maintaining robust reasoning abilities in LLMs.

## Soundness
3

## Presentation
3

## Contribution
3

## Strengths
1. The paper provides a thorough empirical analysis of the impact of self-distillation on LLM reasoning, particularly in mathematical tasks. The experiments are well-designed and controlled, with clear results that support the main claims.
2. The findings have important implications for the development of LLMs, especially in the context of mathematical reasoning. The suppression of epistemic verbalization and its effect on OOD performance highlights the need for more robust training strategies that preserve uncertainty awareness.
3. The paper is well-written and clearly presents the methodology, results, and implications of the study. The use of figures and tables enhances the understanding of the findings.

## Weaknesses
1. The study primarily focuses on mathematical reasoning tasks. It would be beneficial to see how these findings extend to other types of reasoning tasks, such as commonsense reasoning or logical reasoning.
2. The paper could provide more insight into the long-term effects of self-distillation, particularly in terms of whether the observed degradations in reasoning performance persist with continued model training or fine-tuning.
3. The authors could explore more sophisticated methods for quantifying uncertainty expression beyond simple token counts of epistemic markers. A more nuanced analysis might provide deeper insights into how uncertainty is being suppressed.

## Questions
1. How do the authors envision the findings of this study influencing the development of future LLMs, particularly in terms of training strategies and architectures?
2. The study focuses on language models that are already proficient in mathematical reasoning. How would the results differ for models with less strong initial capabilities?
3. Have the authors considered the potential cultural or societal implications of suppressing epistemic verbalization in LLMs, particularly in contexts where uncertainty awareness is highly valued?

## Flag For Ethics Review
No ethics review needed.

## Details Of Ethics Concerns


## Rating
6

## Confidence
4