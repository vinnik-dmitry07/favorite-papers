# Review

## Summary
This paper proposes a self-supervised learning method that pretrains a ViT model with 1B parameters on a large-scale dataset curated from the web, and then distills it into smaller models. The resulting models are shown to outperform OpenCLIP on most image and pixel-level benchmarks.

## Soundness
3

## Presentation
3

## Contribution
3

## Strengths
- The paper is well-written and easy to follow.
- The proposed method is simple and effective. 
- Extensive experiments and ablation studies are conducted to validate the effectiveness of the proposed method.

## Weaknesses
- The paper is more like an engineering work that combines multiple existing techniques to train a better visual backbone. The authors should clearly state the technical contributions of this paper.
- The comparison with weakly-supervised models is unfair. The proposed method uses much more images from the web for pretraining, while CLIP only uses 400M paired images. What if CLIP is pretrained on the same dataset? 
- The paper claims that the proposed method can learn general-purpose features. However, the experiments are mainly conducted on classification benchmarks. More experiments on general visual tasks (e.g., detection, segmentation, etc.) are needed to support this claim.

## Questions
See Weaknesses.

## Flag For Ethics Review
No ethics review needed.

## Details Of Ethics Concerns


## Rating
5

## Confidence
4