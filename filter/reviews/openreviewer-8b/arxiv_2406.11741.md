# Review

## Summary
This paper studies the phenomenon of transcendence, where a model trained to imitate the conditional probability distribution induced by the data it is trained on, can surpass the performance of the experts generating the data. The authors demonstrate this phenomenon by training an autoregressive transformer to play chess from game transcripts, and show that the trained model can sometimes achieve better performance than all players in the dataset. The authors prove that transcendence can be enabled by low-temperature sampling, and rigorously assess this claim experimentally. Finally, the authors discuss other sources of transcendence, laying the groundwork for future investigation of this phenomenon in a broader setting.

## Soundness
3

## Presentation
3

## Contribution
2

## Strengths
1. The paper is well-written and easy to follow.
2. The paper provides a rigorous theoretical analysis of the conditions under which transcendence is possible, and introduces the concept of low-temperature sampling as a key enabler of this phenomenon.
3. The authors conduct experiments to test their theoretical predictions, and provide evidence for the existence of transcendence in the context of chess.

## Weaknesses
1. The paper focuses narrowly on the specific domain of chess, and it is unclear how well the findings would generalize to other domains.
2. The paper assumes that the experts generating the data are sampled uniformly at random, which may not be the case in many real-world scenarios.
3. The paper does not provide a detailed analysis of the potential limitations or drawbacks of the transcendence phenomenon, such as the potential for overfitting or the potential for the model to learn and reproduce biases present in the data.

## Questions
1. Can you provide more insights into the potential limitations or drawbacks of the transcendence phenomenon?
2. How well do you expect your findings to generalize to other domains beyond chess?
3. Can you provide more details on the experimental setup, such as the specific algorithms used for training and evaluation, the computational resources used, and the amount of data used for training and testing?

## Flag For Ethics Review
No ethics review needed.

## Details Of Ethics Concerns


## Rating
6

## Confidence
4