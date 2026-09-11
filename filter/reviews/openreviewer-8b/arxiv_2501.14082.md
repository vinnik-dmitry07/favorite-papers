# Review

## Summary
This paper proposes a method for communication between LLMs by grafting the activation of the last token of LLM A into LLM B. The authors show that this method is more efficient than natural language communication and achieves better performance on some tasks.

## Soundness
3

## Presentation
2

## Contribution
3

## Strengths
1. The proposed method is simple and efficient.
2. The authors conduct extensive experiments to show the effectiveness of the proposed method.

## Weaknesses
1. The presentation of the method is not clear. See the questions below.
2. The method assumes that the activation of the last token encodes the entire belief of the model, which is not well justified.

## Questions
1. What is the definition of the function $f$? In the method section, $f$ is a function from $\mathbb{R}^{d_A + d_B} \to \mathbb{R}^{d_B}$. However, in the compute analysis section, $f$ becomes a function from $\mathbb{R}^{d_A} \to \mathbb{R}^{d_B}$.
2. Why is the last token activation a good representation of the model's belief? It is known that the last token activation is mainly used for the next token prediction. It is also known that the intermediate layer activation contains more information than the last token activation. Why is grafting the last token activation good enough?
3. What is the difference between the proposed method and the method in [1]? In [1], the author grafts the activation of a token at a specific position into the target LLM. Is the difference only that in your method, you graft the last token activation and use a fixed $f$?

[1] Collaborative Decoding with Language Model Patches. Roshan S. Shen et al.

## Flag For Ethics Review
No ethics review needed.

## Details Of Ethics Concerns


## Rating
6

## Confidence
4