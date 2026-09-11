# Review

## Summary
This paper studies the problem of step-size adaptation in continual learning. The authors first show the limitations of existing step-size adaptation methods, including RMSProp and Adam, which are based on heuristics. They then show that Incremental-Delta-Bar-Delta (IDBD), which optimizes the step-size vector explicitly, can better adapt to the changing landscape in continual learning. The authors also discuss the limitations of IDBD and propose it as a promising research direction to combine the advantages of both approaches.

## Soundness
2

## Presentation
2

## Contribution
2

## Strengths
1. The paper is well-written and easy to follow. The authors provide a clear motivation for the problem and a detailed explanation of the existing methods.
2. The authors provide a thorough analysis of the limitations of existing step-size adaptation methods and the IDBD method.

## Weaknesses
1. The main concern is that the paper does not provide any new methods or insights. It simply shows that IDBD can outperform RMSProp and Adam on two toy problems. However, IDBD is an existing method and is not specifically designed for continual learning. It would be more interesting to see how IDBD can be modified or combined with existing methods to better suit the continual learning setting.
2. The paper only considers two toy problems. It would be more convincing to see how the methods perform on more complex and realistic problems, such as image classification or natural language processing.
3. The paper does not provide any theoretical analysis of the proposed method. It would be more interesting to see how the authors can theoretically justify the effectiveness of IDBD in continual learning.

## Questions
1. Can the authors provide any new methods or insights specifically for continual learning?
2. Can the authors evaluate the methods on more complex and realistic problems?
3. Can the authors provide any theoretical analysis of the proposed method?

## Flag For Ethics Review
No ethics review needed.

## Details Of Ethics Concerns


## Rating
3

## Confidence
4