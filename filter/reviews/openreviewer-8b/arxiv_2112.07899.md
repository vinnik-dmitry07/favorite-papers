# Review

## Summary
This paper proposes a simple and effective method to improve the generalizability of dual encoders for dense retrieval. The authors propose to scale up the size of the dual encoder model while keeping the bottleneck embedding size fixed. The proposed model Generalizable T5-based dense Retrievers (GTR) outperforms existing sparse and dense retrievers on the BEIR dataset. The authors also conduct ablation studies to show that GTR is very data efficient, as it only needs 10% of MS Marco supervised data to achieve the best out-of-domain performance.

## Soundness
3

## Presentation
3

## Contribution
3

## Strengths
1. The paper is well-written and easy to follow.
2. The proposed method is simple and effective. Scaling up the model size is a valid path towards generalizability for dual encoders. 
3. The authors conduct extensive experiments on the BEIR benchmark and the results are promising.
4. The authors also conduct ablation studies to show that GTR is very data efficient.

## Weaknesses
1. The inference speed may be a concern for the proposed GTR model.
2. The proposed GTR model is only evaluated on the BEIR benchmark. It would be better to evaluate the model on more datasets.

## Questions
1. How does the inference speed compare to other baselines?
2. How does the GTR model perform on other datasets besides the BEIR benchmark?

## Flag For Ethics Review
No ethics review needed.

## Details Of Ethics Concerns


## Rating
8

## Confidence
4