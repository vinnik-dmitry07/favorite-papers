# Review

## Summary
The paper proposes a method for training representations that are aware of their own capacity, and can adaptively use different parts of the representation for different downstream tasks. The method works by learning a set of linear probing heads of different sizes, and training them all jointly. At test time, the first few dimensions can be used for coarse filtering, and the full representation can be used for final prediction. The method is shown to be effective for image classification and retrieval tasks.

## Soundness
3

## Presentation
3

## Contribution
2

## Strengths
- The paper is well written and easy to follow.
- The method is simple and easy to implement.
- The method achieves good empirical results for classification and retrieval tasks.

## Weaknesses
- The main weakness of the paper is the novelty. The idea of learning representations that are aware of their own capacity is not new. For example, see [1] and [2]. The method of learning a set of linear heads of different sizes is also explored in [3]. The paper should compare to these methods and highlight what is the main difference and advantage of the proposed method.
- The method is only evaluated on ResNet50. It would be interesting to see if the method also works for other architectures, such as Transformers.
- The method is only evaluated on image classification and retrieval tasks. It would be interesting to see if the method also works for other modalities, such as language.
- The method is only evaluated on image classification and retrieval tasks. It would be interesting to see if the method also works for other tasks, such as image generation.

[1] Learning to Represent Data as a Set of Features with Dynamic Sparsity. NeurIPS 2020.

[2] Learning Sparse Representations via Meta-Learning. ICML 2021.

[3] Learning to Represent Data as a Set of Features with Dynamic Sparsity. NeurIPS 2020.

## Questions
- How does the method compare to other methods that learn representations that are aware of their own capacity?
- Does the method work for other architectures, such as Transformers?
- Does the method work for other modalities, such as language?
- Does the method work for other tasks, such as image generation?

## Flag For Ethics Review
No ethics review needed.

## Details Of Ethics Concerns


## Rating
6

## Confidence
4