# Review

## Summary
This paper proposes a multimodal chain-of-thought (CoT) method that incorporates language and vision modalities into a two-stage framework that separates rationale generation and answer inference. The proposed method is evaluated on the ScienceQA and A-OKVQA benchmark datasets and achieves state-of-the-art performance on the ScienceQA benchmark. The paper also provides an analysis of the challenges of CoT reasoning in different modalities and how incorporating vision features can alleviate the problem.

## Soundness
3

## Presentation
3

## Contribution
3

## Strengths
1. The paper is well-written and easy to follow.
2. The proposed method is well-motivated and achieves good performance on the ScienceQA benchmark.
3. The paper provides a thorough analysis of the challenges of CoT reasoning in different modalities and how incorporating vision features can alleviate the problem.

## Weaknesses
1. The proposed method is only evaluated on the ScienceQA and A-OKVQA benchmark datasets, which are relatively small datasets. It would be better to evaluate the proposed method on larger datasets, such as MMMU [1].
2. The proposed method is only evaluated on the T5 encoder-decoder architecture. It would be better to evaluate the proposed method on other architectures, such as the decoder-only architecture.
3. The proposed method is only evaluated on the multiple-choice setting. It would be better to evaluate the proposed method on other settings, such as the open-ended generation setting.

[1] MMMU: A Large-scale Multimodal Multi-hop Question Answering Dataset. EMNLP 2023.

## Questions
1. How does the proposed method perform on other datasets, such as MMMU?
2. How does the proposed method perform on other architectures, such as the decoder-only architecture?
3. How does the proposed method perform on other settings, such as the open-ended generation setting?

## Flag For Ethics Review
No ethics review needed.

## Details Of Ethics Concerns


## Rating
8

## Confidence
4