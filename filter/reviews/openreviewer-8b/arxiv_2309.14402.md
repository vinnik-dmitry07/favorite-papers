# Review

## Summary
The paper studies the ability of LLMs to manipulate knowledge, such as in comparison and classification tasks. The authors find that LLMs struggle with such tasks, unless they are trained and tested with chain-of-thought (CoT) prompting. They also find that LLMs cannot perform inverse knowledge search, unless the knowledge is presented in reverse order in the training data.

## Soundness
3

## Presentation
3

## Contribution
3

## Strengths
- The paper studies an important topic: the ability of LLMs to manipulate knowledge.
- The paper has interesting findings, such as that LLMs cannot perform inverse knowledge search, unless the knowledge is presented in reverse order in the training data.
- The paper is well-written and easy to follow.

## Weaknesses
- The paper does not have any major weaknesses. It would be good to include more LLMs in the experiments, but the paper is fine without them, since it focuses on the more interesting GPT-2.

## Questions
- In Figure 3, why does the accuracy of "What is the birth year of Anya Briar Forger?" drop when going from $N=100k$ to $N=20k$?
- Why does the accuracy of "What is the birth month of Anya Briar Forger?" increase when going from $N=100k$ to $N=20k$?

## Flag For Ethics Review
No ethics review needed.

## Details Of Ethics Concerns


## Rating
8

## Confidence
4