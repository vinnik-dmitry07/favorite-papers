# Review

## Summary
This paper investigates the knowledge storage and extraction mechanisms of large language models (LLMs) using a controlled biography dataset. The authors aim to determine whether LLMs extract knowledge through exposure to similar questions during training or by genuinely learning from sources like Wikipedia. They find a strong correlation between the model's ability to extract knowledge and the diversity of the training data. The paper demonstrates that without data augmentation during pre-training, knowledge may be memorized but not extractable, leading to zero accuracy, regardless of subsequent instruction fine-tuning. The authors employ linear probing techniques to understand how knowledge is encoded in the model's hidden states. They show that knowledge augmentation, such as through paraphrasing or sentence shuffling, leads to better knowledge extraction. The paper provides several key recommendations for LLM pre-training in the industry, including rewriting pre-training data using small auxiliary models and incorporating more instruction fine-tuning data into the pre-training stage. The study highlights the importance of data augmentation and provides insights into the mechanisms by which LLMs store and extract knowledge.

## Soundness
3

## Presentation
3

## Contribution
3

## Strengths
1. The paper provides a thorough investigation into the knowledge storage and extraction mechanisms of LLMs, using a controlled biography dataset. The authors conduct a range of experiments to determine whether LLMs extract knowledge through exposure to similar questions during training or by genuinely learning from sources like Wikipedia. The paper also employs linear probing techniques to understand how knowledge is encoded in the model's hidden states, providing valuable insights into the internal mechanisms of LLMs.

2. The paper provides several key recommendations for LLM pre-training in the industry, including rewriting pre-training data using small auxiliary models and incorporating more instruction fine-tuning data into the pre-training stage. These recommendations are based on the findings of the study and have the potential to improve the performance of LLMs in real-world applications.

3. The paper is well-written and easy to follow. The authors present their findings in a clear and concise manner, making it easy for readers to understand the key points of the study. The paper is well-structured, with each section building on the previous one to provide a coherent narrative.

## Weaknesses
1. The paper focuses solely on a biography dataset, which may not fully represent the diversity of knowledge that LLMs are capable of storing and extracting. It would be beneficial to include other types of datasets in future studies to provide a more comprehensive understanding of LLMs' knowledge extraction abilities.

2. The paper does not provide a detailed analysis of the computational resources required for the experiments. This information would be valuable for readers who are interested in replicating the study or applying the findings to their own LLM training and fine-tuning efforts.

3. The paper does not provide a detailed analysis of the potential limitations of the proposed methods and recommendations. It would be beneficial to include a discussion on the potential drawbacks or scenarios where the proposed methods may not be as effective, providing a more balanced view of the findings.

## Questions
1. How do the findings of this study generalize to other types of knowledge beyond biographies? Is it possible to apply the proposed methods and recommendations to other domains, such as scientific knowledge or factual knowledge?

2. What are the potential limitations of the proposed methods and recommendations? Are there scenarios where data augmentation or mixed training may not be effective, or where the linear probing techniques may not provide accurate insights?

3. How do the findings of this study relate to the broader field of knowledge extraction from LLMs? Are there other methods or techniques that could be combined with the proposed approaches to further improve knowledge extraction?

## Flag For Ethics Review
No ethics review needed.

## Details Of Ethics Concerns


## Rating
6

## Confidence
4