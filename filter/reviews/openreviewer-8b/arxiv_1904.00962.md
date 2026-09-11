# Review

## Summary
This paper proposes a new adaptive learning rate method that can scale the learning rate based on the norm of the parameters and gradients. The authors provide some theoretical analysis for the proposed method. The authors evaluate the proposed method on BERT and ResNet-50 and show that the proposed method can train these models fast with large batch sizes.

## Soundness
2

## Presentation
3

## Contribution
2

## Strengths
1. The proposed method is simple and intuitive. 
2. The authors evaluate the proposed method on two important models, BERT and ResNet-50, and demonstrate that the proposed method can train these models fast with large batch sizes.

## Weaknesses
1. The authors should compare the proposed method with more baselines. For example, the authors should compare the proposed method with the baselines mentioned in the related work section. The authors should also compare the proposed method with the baselines on small batch sizes and small datasets, so that we can see whether the proposed method is effective for different tasks and settings.
2. The authors should provide more ablation studies. For example, the authors should conduct ablation studies on the hyperparameters $\gamma_l$ and $\gamma_u$.

## Questions
1. The authors should compare the proposed method with more baselines.
2. The authors should provide more ablation studies on the hyperparameters $\gamma_l$ and $\gamma_u$.
3. The authors should evaluate the proposed method on small batch sizes and small datasets, so that we can see whether the proposed method is effective for different tasks and settings.

## Flag For Ethics Review
No ethics review needed.

## Details Of Ethics Concerns


## Rating
5

## Confidence
4