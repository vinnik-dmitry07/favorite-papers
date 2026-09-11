# Review

## Summary
This paper proposes a new self-supervised learning method for vision transformer. The method combines the MIM (Masked Image Modeling) and DINO (self-distillation). The MIM loss is used for patch tokens and the DINO loss is used for the CLS tokens. The authors show that the proposed method outperforms DINO and BEiT on classification, detection, and segmentation.

## Soundness
3

## Presentation
3

## Contribution
3

## Strengths
1. The proposed method is simple and effective. It combines the DINO and BEiT in a nice way.
2. The proposed method outperforms DINO and BEiT on various tasks.

## Weaknesses
1. The authors claim that the proposed method is BERT-like pre-training for ViTs. However, the proposed method is not exactly the same as BERT pre-training. BERT pre-trains the model on the next token prediction task, which is different from the masked image modeling in this paper. The masked image modeling is more similar to the fill-in-the-blanks task in the language modeling.
2. The authors claim that the proposed method is an online tokenizer. However, it is not clear what is the difference between an online tokenizer and a normal tokenizer. The tokenizer in BEiT can also be learned during the pre-training stage.
3. The authors claim that the proposed method can discover emerging local semantic patterns. However, from Figure 4, it seems that the proposed method does not have better local semantic patterns than DINO.

## Questions
1. What is the difference between an online tokenizer and a normal tokenizer?
2. Why is the masked image modeling more similar to the fill-in-the-blanks task in the language modeling?
3. How does the proposed method discover emerging local semantic patterns?

## Flag For Ethics Review
No ethics review needed.

## Details Of Ethics Concerns


## Rating
6

## Confidence
4