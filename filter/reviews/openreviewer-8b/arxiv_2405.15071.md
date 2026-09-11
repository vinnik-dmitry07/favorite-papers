# Review

## Summary
The paper investigates whether transformers can learn to perform implicit reasoning over parametric knowledge. The paper focuses on two types of reasoning, composition and comparison, and consistently finds that transformers can learn implicit reasoning through a phenomenon called grokking, which involves extended training beyond overfitting. The paper also reveals the different levels of systematic generalization across reasoning types, and conducts mechanistic analysis to understand the internal mechanisms within the model. The paper provides insights into the data and training setup to better induce implicit reasoning and suggests potential improvements to the transformer architecture.

## Soundness
3

## Presentation
3

## Contribution
3

## Strengths
1. The paper investigates an important and interesting question of whether transformers can learn to perform implicit reasoning over parametric knowledge. This is a crucial aspect of intelligence that is still not well understood.
2. The paper provides a mechanistic analysis of the internal mechanisms within the model, which offers valuable insights into how the model learns and generalizes. The analysis of the generalizing circuit and its relation to systematicity is a significant contribution.
3. The paper demonstrates the power of parametric memory for complex reasoning, showcasing its potential for solving challenging tasks that are beyond the capabilities of state-of-the-art language models based on non-parametric memory.

## Weaknesses
1. The paper focuses on two specific reasoning types, composition and comparison. It would be valuable to explore other types of reasoning, such as induction, abduction, and negation.
2. The paper primarily focuses on synthetic datasets. It would be beneficial to evaluate the findings on real-world datasets, such as logical reasoning datasets like LogiQA.
3. The paper could provide more insights into the limitations of non-parametric memory and how it fails on the complex reasoning task. This would help to better understand the advantages of parametric memory in such scenarios.

## Questions
1. Can you provide more insights into how the findings in the paper can be applied to improve the transformer architecture? Are there any potential modifications or enhancements that you suggest?
2. How do you plan to evaluate the findings on real-world datasets, such as logical reasoning datasets like LogiQA? How do you expect the results to be different from the synthetic datasets used in the paper?
3. Can you provide more details on the limitations of non-parametric memory and how it fails on the complex reasoning task? This would help to better understand the advantages of parametric memory in such scenarios.

## Flag For Ethics Review
No ethics review needed.

## Details Of Ethics Concerns


## Rating
5

## Confidence
4