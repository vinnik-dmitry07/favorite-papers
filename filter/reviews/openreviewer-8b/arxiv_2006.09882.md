# Review

## Summary
The paper proposes a new self-supervised learning method that learns visual representations by contrasting cluster assignments. The method is similar to contrastive learning methods, but does not require computing pairwise comparisons. Instead, it clusters the data and enforces consistency between cluster assignments produced for different augmentations (or “views”) of the same image. The method uses a “swapped” prediction mechanism where it predicts the code of a view from the representation of another view. The method can be trained with large and small batches and can scale to unlimited amounts of data. The paper also proposes a new data augmentation strategy called multi-crop, which uses a mix of views with different resolutions in place of two full-resolution views, without increasing the memory or compute requirements. The method is evaluated on ImageNet and several transfer tasks, and achieves good results.

## Soundness
3

## Presentation
3

## Contribution
3

## Strengths
1. The paper proposes a novel self-supervised learning method that does not require pairwise comparisons, which is different from most existing methods. This method can be trained with large and small batches and can scale to unlimited amounts of data.
2. The paper proposes a new data augmentation strategy called multi-crop, which uses a mix of views with different resolutions in place of two full-resolution views, without increasing the memory or compute requirements. This augmentation strategy can be applied to many self-supervised methods and improves their performance.
3. The method is evaluated on ImageNet and several transfer tasks, and achieves good results, outperforming supervised pretraining on all the considered transfer tasks. This shows the effectiveness of the method.

## Weaknesses
1. The paper does not provide a detailed analysis of the computational complexity of the method, which is an important factor to consider in self-supervised learning. It would be helpful to compare the computational complexity of the method with other methods.
2. The paper does not provide a detailed analysis of the sensitivity of the method to hyperparameters, such as the number of clusters, the entropy regularization parameter, and the number of iterations in the Sinkhorn-Knopp algorithm. It would be helpful to investigate how these hyperparameters affect the performance of the method.
3. The paper does not provide a detailed analysis of the interpretability of the learned representations. It would be helpful to visualize the learned features and clusters, and analyze what the model has learned.

## Questions
1. How does the method compare to other self-supervised learning methods in terms of computational complexity?
2. How sensitive is the method to the choice of hyperparameters, such as the number of clusters, the entropy regularization parameter, and the number of iterations in the Sinkhorn-Knopp algorithm?
3. Can you provide more insights into the interpretability of the learned representations? How do the learned features and clusters relate to the input images?

## Flag For Ethics Review
No ethics review needed.

## Details Of Ethics Concerns


## Rating
5

## Confidence
4