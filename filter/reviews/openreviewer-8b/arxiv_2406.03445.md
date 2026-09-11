# Review

## Summary
This paper investigates the mechanisms by which pre-trained LLMs perform integer addition. The authors demonstrate that LLMs leverage Fourier features to compute sums, with different components of the model utilizing these features in distinct ways: MLP layers primarily handle magnitude approximation using low-frequency features, while attention layers handle modular addition using high-frequency features. The paper also shows that pre-training is essential for learning these Fourier features, as models trained from scratch only use low-frequency features and perform less accurately. The authors provide evidence for the presence of Fourier features in the token embeddings of pre-trained models and show that introducing pre-trained token embeddings to a randomly initialized model significantly improves its performance. Overall, the paper provides insights into the mechanisms underlying the mathematical reasoning capabilities of LLMs and highlights the importance of pre-training in equipping models with the necessary features for algorithmic tasks.

## Soundness
3

## Presentation
3

## Contribution
2

## Strengths
- The paper is well-written and easy to follow. 
- The paper provides a mechanistic understanding of how LLMs compute integer addition, highlighting the distinct roles of MLP and attention layers and the use of Fourier features. 
- The paper demonstrates that pre-training is crucial for learning the Fourier features necessary for accurate addition, providing insights into the importance of pre-training for algorithmic tasks.

## Weaknesses
- The paper focuses solely on the addition operation, which is not a strong evidence to support the claim that pre-trained LLMs use Fourier features to compute arithmetic. The authors should extend their analysis to other mathematical operations such as subtraction, multiplication, and division to provide a more comprehensive understanding of the mechanisms underlying the mathematical reasoning capabilities of LLMs.
- The paper should include a more detailed analysis of the token embeddings of pre-trained models to better understand the Fourier features present in these embeddings. The authors should provide a more in-depth examination of the clustering properties of the token embeddings and how they relate to the addition operation.
- The paper should provide a more detailed explanation of the filtering process used to isolate the Fourier features in the model's representations. The authors should include a mathematical formulation of the filtering process and provide a more detailed analysis of the impact of filtering on the model's performance.

## Questions
- Can the authors provide more evidence to support the claim that pre-trained LLMs use Fourier features to compute arithmetic operations other than addition, such as subtraction, multiplication, and division?
- Can the authors provide a more detailed analysis of the token embeddings of pre-trained models, including a more in-depth examination of the clustering properties and their relationship to the addition operation?
- Can the authors provide a more detailed explanation of the filtering process used to isolate the Fourier features, including a mathematical formulation and a more detailed analysis of the impact of filtering on the model's performance?

## Flag For Ethics Review
No ethics review needed.

## Details Of Ethics Concerns


## Rating
6

## Confidence
4