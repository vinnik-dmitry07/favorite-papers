# Review

## Summary
The paper proposes a novel regularization method for self-supervised learning (SSL) named Variance-Invariance-Sketching Regularization (VISReg). VISReg builds on the VICReg method by replacing the covariance term with a sketching objective based on the Sliced Wasserstein Distance (SWD), which aligns the normalized embedding distribution with an isotropic Gaussian prior along random 1D projections. This allows for enforcing the full distributional shape of the embeddings while decoupling scale and shape regularization. The method aims to combine the flexibility and interpretability of VICReg with the distributional rigor of sketching methods, providing robust gradients even under embedding collapse. The authors demonstrate that VISReg outperforms existing SSL methods on low-quality datasets and shows superior out-of-distribution (OOD) generalization capabilities.

## Soundness
3

## Presentation
3

## Contribution
3

## Strengths
1. VISReg addresses the limitations of previous methods by decoupling scale and shape regularization, which is a novel approach in the field of SSL.
2. The paper provides a comprehensive analysis of the hyperparameter landscape of VISReg and related methods, offering valuable insights and guidance for practitioners.
3. The method demonstrates robustness to low-quality datasets and shows superior performance on OOD datasets, which is crucial for real-world applications.

## Weaknesses
1. The paper does not provide a detailed analysis of the computational complexity of VISReg compared to other methods, which could be important for large-scale applications.
2. While the paper shows promising results on various datasets, the experiments are limited to a specific set of benchmarks. A broader evaluation on more diverse datasets would strengthen the claims.
3. The paper could benefit from a more detailed comparison with other state-of-the-art SSL methods, particularly in terms of computational efficiency and scalability.

## Questions
1. Can you provide more insights into the choice of the Sliced Wasserstein Distance for shape regularization? How does it compare with other distance measures in the context of SSL?
2. How does VISReg scale with the size of the dataset and the dimensionality of the embeddings? Are there any practical limitations in terms of computational resources for implementing VISReg?
3. Can you elaborate on the robustness of VISReg to hyperparameter choices? How sensitive is the method to the choice of hyperparameters, and how did you determine the optimal values reported in the paper?

## Flag For Ethics Review
No ethics review needed.

## Details Of Ethics Concerns


## Rating
6

## Confidence
4