# Review

## Summary
This paper investigates how to train a BERT-like model with limited computational resources, i.e., with a single GPU in one day. The authors examine the performance of various model architectures, training techniques, and data processing methods, and find that performance follows scaling laws even in the limited-compute setting. The authors find that the best model achieves performance on par with BERT-base on most of the GLUE tasks except CoLA.

## Soundness
3

## Presentation
3

## Contribution
2

## Strengths
1. The paper is well-written and easy to follow.
2. The authors conduct a comprehensive investigation of various techniques for training a BERT-like model with limited computational resources.
3. The authors provide the code for reproducing their results.

## Weaknesses
1. The authors do not compare their results with existing works on efficient BERT pretraining, such as SqueezeBERT and FastBERT. It is unclear whether the proposed model outperforms existing efficient BERT models.
2. The authors only evaluate the model on the GLUE tasks. The performance of the model on other NLP tasks is unclear.

## Questions
1. Can you compare the proposed model with existing efficient BERT models, such as SqueezeBERT and FastBERT?
2. Can you evaluate the proposed model on other NLP tasks, such as the SuperGLUE benchmarks and the benchmark from the BigBench family?

## Flag For Ethics Review
No ethics review needed.

## Details Of Ethics Concerns


## Rating
6

## Confidence
4