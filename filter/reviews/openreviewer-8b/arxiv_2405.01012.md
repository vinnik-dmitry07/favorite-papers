# Review

## Summary
The paper discusses the limitations of using CKA as a metric to compare neural responses from fMRI and MEG with deep neural network representations. The authors show that CKA is sensitive to the ratio of features to samples, and can give high similarity scores to random data. They demonstrate that using a corrected version of CKA addresses these issues, and allows for a better assessment of the similarity between brain and ANN representations.

## Soundness
3

## Presentation
3

## Contribution
2

## Strengths
The paper is well written and easy to follow. The authors do a good job of explaining the limitations of CKA and showing how the corrected version addresses these limitations. The authors provide a thorough evaluation of the corrected CKA, comparing it to other similarity metrics and showing its performance on both synthetic and real-world data. The results are presented clearly and the authors provide a detailed discussion of their implications.

## Weaknesses
The main weakness of the paper is that it does not provide a clear comparison of the performance of the corrected CKA with other state-of-the-art methods for measuring the similarity between brain and ANN representations. The authors mention that other metrics such as CCA, RSA, and cosine similarity have been used for this purpose, but they do not provide a detailed comparison of the performance of these metrics with the corrected CKA. 

Additionally, the authors could have provided more details on the computational complexity of the corrected CKA and how it compares to other metrics. 

Finally, the authors could have provided more details on the statistical analysis of the results, such as p-values and confidence intervals.

## Questions
1. How does the corrected CKA compare to other state-of-the-art methods for measuring the similarity between brain and ANN representations, such as CCA, RSA, and cosine similarity? Please provide a detailed comparison of the performance of these metrics with the corrected CKA.

2. What are the computational advantages and disadvantages of the corrected CKA compared to other metrics? Please provide a detailed comparison of the computational complexity of these metrics.

3. Can you provide more details on the statistical analysis of the results, such as p-values and confidence intervals?

## Flag For Ethics Review
No ethics review needed.

## Details Of Ethics Concerns


## Rating
5

## Confidence
4