# Review

## Summary
This paper introduces a novel dynamic inference approach for LLMs, where the inference computation can be customized for each input by selecting and configuring pre-trained layers as needed. The authors first use MCTS to explore the space of layer skipping and layer looping, and find that looping is more effective and most valid programs are quite simple (dominated by short, contiguous segments). Based on these observations, they train a lightweight model to predict the execution program directly, which is then used to guide layer execution at inference time. The authors demonstrate that this approach achieves better accuracy than standard inference and prior dynamic inference methods on a range of mathematical reasoning benchmarks.

## Soundness
3

## Presentation
3

## Contribution
3

## Strengths
1. The idea of treating layers as reusable functions and dynamically composing them into execution programs is novel and interesting. The authors also provide an effective way to implement this idea, which is lightweight and easy to deploy.
2. The paper is well-written and easy to follow. The authors first use MCTS to explore the space of layer skipping and looping, and then use the insights gained to design the program predictor. The experimental results are strong and comprehensive.
3. The proposed method is general and can be applied to various models and tasks. It can also be used in conjunction with other techniques such as COT.

## Weaknesses
1. The paper lacks an analysis of the computational complexity of the proposed method. While the authors claim that their method is lightweight, it would be helpful to provide more concrete details on the computational overhead, such as the number of additional parameters and the inference latency.
2. The paper does not provide a detailed analysis of the failure cases. It would be helpful to understand the limitations of the proposed method and the cases where it may not perform well.
3. The paper does not provide a detailed analysis of the interpretability of the learned execution programs. It would be helpful to understand how the model decides to skip or loop certain layers and how this relates to the difficulty of the input.

## Questions
1. How does the computational complexity of the proposed method compare to the baseline methods? It would be helpful to provide a detailed analysis of the computational overhead, such as the number of additional parameters and the inference latency.
2. Can the proposed method be applied to other tasks beyond mathematical reasoning? It would be helpful to provide some preliminary results or discussion on the applicability of the method to other types of tasks.
3. How does the proposed method interact with other techniques such as COT? It would be helpful to provide some preliminary results or discussion on the compatibility and potential benefits of combining the two approaches.

## Flag For Ethics Review
No ethics review needed.

## Details Of Ethics Concerns


## Rating
6

## Confidence
4