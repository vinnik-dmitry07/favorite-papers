# Review

## Summary
This paper investigates how transformer-based language models, specifically GPT-2, handle complex hierarchical language structures defined by context-free grammars (CFGs). The authors introduce a family of synthetic CFGs that generate hierarchical rules and long sentences with local ambiguities, requiring dynamic programming for parsing. They demonstrate that GPT-2 can effectively learn and reason over these hierarchies, with its hidden states reflecting the structural aspects of the CFGs and its attention patterns resembling dynamic programming algorithms. The paper presents several findings, including the superiority of relative and rotary embeddings over absolute embeddings, the effectiveness of uniform attention, the superior performance of autoregressive models over encoder-only models in deep structure reasoning, and the improved robustness when structural noise is injected into training data.

## Soundness
3

## Presentation
3

## Contribution
3

## Strengths
1. The paper provides a novel and comprehensive study of how transformer models handle complex hierarchical structures, addressing a significant gap in the current understanding of language models.
2. The introduction of synthetic CFGs allows for controlled experiments that reveal the inner workings of GPT-2, providing clear insights into its reasoning mechanisms.
3. The paper offers several significant findings that contribute to the broader understanding of transformer models, including the importance of relative embeddings and the robustness of models trained on perturbed data.

## Weaknesses
1. The paper focuses solely on GPT-2, and it is unclear how well the findings generalize to other transformer models.
2. The synthetic nature of the data may limit the applicability of the findings to real-world language tasks.
3. The paper is dense and may be difficult for readers without a strong background in the subject.

## Questions
1. How do the findings in this paper generalize to other transformer models beyond GPT-2? Have you conducted any preliminary experiments or analyses to explore this?
2. Can you provide more details on the potential real-world applications of your findings? How can the insights gained from this study be applied to improve the performance of language models in natural language processing tasks?
3. The paper is quite dense and technical. Are there any plans to make the content more accessible to readers who may not have a strong background in the subject matter?

## Flag For Ethics Review
No ethics review needed.

## Details Of Ethics Concerns


## Rating
6

## Confidence
4