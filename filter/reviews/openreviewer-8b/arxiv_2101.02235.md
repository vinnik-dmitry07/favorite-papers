# Review

## Summary
This paper introduces a new question answering dataset, StrategyQA, that focuses on questions that require multi-hop reasoning and the reasoning steps are implicit rather than explicit. The authors describe the process of collecting the dataset, including how they prompt crowd workers to generate questions, how they verify the quality of the questions and the reasoning steps, and how they match evidence paragraphs to the reasoning steps. They also evaluate several baselines on the dataset and show that the questions in the dataset are challenging for current models.

## Soundness
3

## Presentation
3

## Contribution
3

## Strengths
- The paper is well-written and easy to follow. The authors describe the data collection process in detail, which is important for reproducibility.
- The authors put a lot of effort into verifying the quality of the dataset, including the questions, the reasoning steps, and the evidence paragraphs. They also try to encourage diversity in the questions and the strategies used to answer the questions.
- The dataset covers a wide range of domains and requires a variety of reasoning skills, which is a strength. 
- The baselines the authors evaluate in the paper are reasonable and the results highlight the difficulty of the dataset.

## Weaknesses
- The questions in the dataset are based on Wikipedia articles, which limits the diversity of the questions. Also, since the questions are based on Wikipedia, it might be easier for crowd workers to copy the answers from the Wikipedia articles rather than come up with new questions based on the information in the articles. The authors mention that they filter out questions that have high lexical overlap with the articles, but it is possible that the questions still share semantics with the articles.
- The questions in the dataset are all yes/no questions, which is a limitation. It would be interesting to see questions with more answer formats.
- The dataset is relatively small, with only 2,780 questions. It would be interesting to see a larger dataset.

## Questions
- How do you make sure that the questions are not based on the information in the Wikipedia articles?
- Do you plan to release the list of questions that are filtered out by the solvers?

## Flag For Ethics Review
No ethics review needed.

## Details Of Ethics Concerns


## Rating
6

## Confidence
4