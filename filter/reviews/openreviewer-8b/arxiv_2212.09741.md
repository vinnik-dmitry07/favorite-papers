# Review

## Summary
This paper proposes a new method for learning a single embedder that can generate text embeddings tailored to different downstream tasks and domains. The authors first annotate instructions for 330 diverse tasks and train InstructOR on this multitask mixture with a contrastive loss. The proposed method is evaluated on 70 embedding evaluation tasks ranging from classification and information retrieval to semantic textual similarity and text generation evaluation. The experimental results show that the proposed method achieves state-of-the-art performance, with an average improvement of 3.4% compared to the previous best results on the 70 diverse datasets.

## Soundness
3

## Presentation
3

## Contribution
3

## Strengths
1. The authors propose a new method for computing text embeddings given task instructions. The proposed method can generate text embeddings tailored to different downstream tasks and domains without any further training.
2. The authors annotate instructions for 330 diverse tasks and train InstructOR on this multitask mixture with a contrastive loss. The proposed method is evaluated on 70 embedding evaluation tasks ranging from classification and information retrieval to semantic textual similarity and text generation evaluation. The experimental results show that the proposed method achieves state-of-the-art performance, with an average improvement of 3.4% compared to the previous best results on the 70 diverse datasets.
3. The authors also provide analysis and ablations to show the effectiveness of the proposed method.

## Weaknesses
1. The proposed method is similar to the previous work E5: https://arxiv.org/pdf/2205.09818.pdf. The authors should compare the proposed method with E5 and discuss the difference between them.
2. The authors should also compare the proposed method with other text embedding methods such as DPR, Contriever, and Sentence-BERT. The authors can evaluate the performance of these methods on the MTEB benchmark.
3. The authors should provide more details about the training data. The authors should provide the number of training data for each task and domain. The authors should also provide the number of parameters of the proposed method.

## Questions
N/A

## Flag For Ethics Review
No ethics review needed.

## Details Of Ethics Concerns


## Rating
6

## Confidence
4