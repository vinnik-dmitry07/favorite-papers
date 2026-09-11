# Review

## Summary
This paper proposes a self-supervised learning method called LeJEPA, which is based on Joint-Embedding Predictive Architectures (JEPAs). The authors present a comprehensive theory of JEPAs and introduce a novel training objective called Sketched Isotropic Gaussian Regularization (SIGReg) to constrain embeddings to reach an isotropic Gaussian distribution, which is identified as the optimal distribution that JEPAs’ embeddings should follow to minimize downstream prediction risk. The proposed method, LeJEPA, combines the JEPA predictive loss with SIGReg and has numerous theoretical and practical benefits, including single trade-off hyperparameter, linear time and memory complexity, stability across hyper-parameters, architectures, and domains, and heuristics-free implementation. The empirical validation covers 10+ datasets, 60+ architectures, and various scales and domains. LeJEPA outperforms state-of-the-art methods and establishes in-domain pretraining as a viable option.

## Soundness
3

## Presentation
3

## Contribution
3

## Strengths
1. The paper presents a comprehensive theory of Joint-Embedding Predictive Architectures (JEPAs) and introduces a novel training objective, Sketched Isotropic Gaussian Regularization (SIGReg), which is a significant contribution to the field of self-supervised learning.
2. The proposed method, LeJEPA, has numerous theoretical and practical benefits, including single trade-off hyperparameter, linear time and memory complexity, stability across hyper-parameters, architectures, and domains, and heuristics-free implementation, which makes it a practical and scalable solution.
3. The empirical validation is extensive, covering 10+ datasets, 60+ architectures, and various scales and domains, which demonstrates the robustness and effectiveness of the proposed method.
4. The paper challenges the transfer learning paradigm and demonstrates that principled SSL can unlock effective in-domain pretraining, which is a valuable contribution to the field.

## Weaknesses
1. The paper may lack a detailed comparison with other state-of-the-art self-supervised learning methods, which could help to highlight the advantages and disadvantages of LeJEPA in a more comprehensive manner.
2. The paper may not provide a detailed analysis of the limitations of LeJEPA, which could help to understand the potential drawbacks and challenges of the proposed method.

## Questions
1. Can you provide more details on the comparison with other state-of-the-art self-supervised learning methods, such as DINOv2 and IJEPA? How does LeJEPA perform in terms of accuracy, computational efficiency, and scalability compared to these methods?
2. Can you provide more details on the limitations of LeJEPA? Are there any specific scenarios or datasets where LeJEPA may not perform well? How can these limitations be addressed in future work?

## Flag For Ethics Review
No ethics review needed.

## Details Of Ethics Concerns


## Rating
8

## Confidence
4