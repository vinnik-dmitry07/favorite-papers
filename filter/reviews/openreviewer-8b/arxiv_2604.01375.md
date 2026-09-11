# Review

## Summary
This paper introduces RIFT, a taxonomy for categorizing failures in evaluation rubrics used in assessing language models. RIFT organizes failures into three main categories: reliability, content validity, and consequential validity. The taxonomy was developed through a grounded theory approach by expert annotators who iteratively analyzed 85 rubrics from five diverse sources (including human-authored and synthetic rubrics). The authors also developed automated signals to approximate RIFT labels and achieve good alignment with human annotations (up to F1 score of 0.925).

## Soundness
3

## Presentation
3

## Contribution
3

## Strengths
- The paper addresses an important problem in LLM evaluation: assessing the quality of rubrics themselves rather than just downstream performance. This is a key step for improving the reliability of LLM evaluation pipelines.
- The grounded theory approach to developing the taxonomy is well-suited for this problem. It allows for iterative refinement based on expert insights.
- The taxonomy is comprehensive, covering multiple dimensions of rubric quality. The three main categories are well-defined and reasonably exhaustive.
- The use of multiple data sources (human-authored and synthetic) provides good coverage of different types of rubrics.
- The automated diagnostics show promising results in approximating human annotations. This suggests the taxonomy can be practically applied.

## Weaknesses
- The taxonomy development process is labor-intensive, requiring significant expert time and effort. This limits its applicability to only the most important failure modes.
- The generalizability of the taxonomy is uncertain. The current version may not capture all relevant failure modes, particularly for novel or domain-specific rubrics.
- The automated diagnostics rely on LLMs which may introduce their own biases. This could affect the accuracy of the failure mode identification.
- The taxonomy structure and expert annotations are not publicly available, which limits reproducibility and further research.

## Questions
- How does the complexity of the rubrics (e.g., length, structure) affect the quality of the annotations?
- What are the long-term plans for maintaining and updating the taxonomy? How can it be adapted to new rubric types?
- How does the performance of the automated diagnostics change with different LLMs?
- How do you ensure the quality of the expert annotations? What guidelines or training did they receive?

## Flag For Ethics Review
No ethics review needed.

## Details Of Ethics Concerns


## Rating
6

## Confidence
4