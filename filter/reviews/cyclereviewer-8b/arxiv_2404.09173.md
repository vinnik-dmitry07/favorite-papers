## Reviewer

### Summary

This paper proposes a novel architecture called TransformerFAM, which leverages a feedback loop to enable the network to attend to its own latent representations. This design fosters the emergence of working memory within the Transformer, allowing it to process indefinitely long sequences. TransformerFAM requires no additional weights, enabling seamless integration with pre-trained models. The paper shows that TransformerFAM significantly improves Transformer performance on long-context tasks across various model sizes (1B, 8B, and 24B).

### Soundness

2 fair

### Presentation

2 fair

### Contribution

2 fair

### Strengths

The paper is well-written and easy to follow. The idea of using a feedback loop to enable the network to attend to its own latent representations is novel and interesting.

### Weaknesses

1. The experiments are not convincing. The authors only evaluate the proposed method on a few datasets, and the results are not significantly better than the baselines. The authors should conduct more experiments to demonstrate the effectiveness of the proposed method.

2. The authors should provide more details about the implementation of the proposed method. For example, how to initialize the FAM, how to update it during training, and how to use it during inference.

3. The authors should provide more details about the experimental setup. For example, how to split the data into blocks, how to set the hyperparameters, and how to compare the proposed method with the baselines.

### Questions

See weaknesses.

### Flag For Ethics Review

No ethics review needed.

### Rating

5: marginally below the acceptance threshold

### Confidence

3: You are fairly confident in your assessment. It is possible that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work. Math/other details were not carefully checked.

**********

## Reviewer

### Summary

This paper introduces a novel architecture called TransformerFAM that enables Transformers to process long sequences by leveraging a feedback loop to attend to its own latent representations. The paper demonstrates that TransformerFAM significantly improves Transformer performance on long-context tasks across various model sizes (1B, 8B, and 24B). The paper also shows that TransformerFAM can maintain past information for an indefinite horizon, making it a promising solution for Large Language Models (LLMs) to handle infinitely long input sequences.

### Soundness

2 fair

### Presentation

2 fair

### Contribution

2 fair

### Strengths

The paper introduces a novel architecture, TransformerFAM, that enables Transformers to process long sequences by leveraging a feedback loop to attend to its own latent representations. This is a novel approach that could potentially improve the performance of Transformers on long-context tasks.

The paper demonstrates that TransformerFAM significantly improves Transformer performance on long-context tasks across various model sizes (1B, 8B, and 24B). This is a significant improvement over existing methods and suggests that TransformerFAM could be a promising solution for Large Language Models (LLMs) to handle infinitely long input sequences.

### Weaknesses

The paper does not provide a thorough analysis of the computational complexity of TransformerFAM. While it is mentioned that TransformerFAM has a computational complexity of O(L) and a memory complexity of O(1), where L is the length of the processed tokens, it would be helpful to provide a more detailed analysis of the computational complexity and to compare it with other methods.

The paper does not provide a thorough evaluation of TransformerFAM on a wide range of long-context tasks. While the paper demonstrates that TransformerFAM significantly improves Transformer performance on long-context tasks across various model sizes (1B, 8B, and 24B), it would be helpful to evaluate TransformerFAM on a wider range of tasks to demonstrate its effectiveness.

The paper does not provide a thorough analysis of the limitations of TransformerFAM. While the paper mentions that TransformerFAM requires no additional weights, enabling seamless integration with pre-trained models, it would be helpful to provide a more detailed analysis of the limitations of TransformerFAM and to discuss potential areas for future work.

### Questions

See weaknesses

### Flag For Ethics Review

No ethics review needed.

### Rating

5: marginally below the acceptance threshold

### Confidence

3: You are fairly confident in your assessment. It is possible that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work. Math/other details were not carefully checked.

**********

## Reviewer

### Summary

This paper proposes a novel Transformer architecture called TransformerFAM, which leverages a feedback loop to enable the network to attend to its own latent representations. This design fosters the emergence of working memory within the Transformer, allowing it to process indefinitely long sequences. TransformerFAM requires no additional weights, enabling seamless integration with pre-trained models. The paper shows that TransformerFAM significantly improves Transformer performance on long-context tasks across various model sizes (1B, 8B, and 24B).

### Soundness

2 fair

### Presentation

2 fair

### Contribution

2 fair

### Strengths

1. The idea of using a feedback loop to enable the network to attend to its own latent representations is novel and interesting.
2. The paper is well-written and easy to follow.

### Weaknesses

1. The paper lacks a comprehensive analysis of the computational complexity of TransformerFAM. The authors should provide a more detailed analysis of the computational complexity and compare it with other methods.
2. The paper lacks a thorough evaluation of TransformerFAM on a wide range of long-context tasks. The authors should evaluate TransformerFAM on a wider range of tasks to demonstrate its effectiveness.
3. The paper lacks a thorough analysis of the limitations of TransformerFAM. The authors should provide a more detailed analysis of the limitations of TransformerFAM and discuss potential areas for future work.
4. The paper lacks a clear explanation of how TransformerFAM is trained. The authors should provide a detailed explanation of the training process and how the model is initialized and updated during training.
5. The paper lacks a clear explanation of how TransformerFAM is used during inference. The authors should provide a detailed explanation of how the model is used during inference and how the feedback loop is implemented.

### Questions

1. How does TransformerFAM compare to other methods in terms of computational complexity?
2. How does TransformerFAM perform on a wider range of long-context tasks?
3. What are the limitations of TransformerFAM, and how can they be addressed?
4. How is TransformerFAM trained, and how is it initialized and updated during training?
5. How is TransformerFAM used during inference, and how is the feedback loop implemented?

### Flag For Ethics Review

No ethics review needed.

### Rating

5: marginally below the acceptance threshold

### Confidence

3: You are fairly confident in your assessment. It is possible that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work. Math/other details were not carefully checked.

**********

## Reviewer

### Summary

This paper proposes a novel Transformer architecture called TransformerFAM that leverages a feedback loop to enable the network to attend to its own latent representations. This design fosters the emergence of working memory within the Transformer, allowing it to process indefinitely long sequences. TransformerFAM requires no additional weights, enabling seamless integration with pre-trained models. The paper shows that TransformerFAM significantly improves Transformer performance on long-context tasks across various model sizes (1B, 8B, and 24B). These results showcase the potential to empower Large Language Models (LLMs) to process sequences of unlimited length.

### Soundness

3 good

### Presentation

3 good

### Contribution

2 fair

### Strengths

The paper introduces a novel Transformer architecture called TransformerFAM that leverages a feedback loop to enable the network to attend to its own latent representations. This design fosters the emergence of working memory within the Transformer, allowing it to process indefinitely long sequences. TransformerFAM requires no additional weights, enabling seamless integration with pre-trained models. The paper shows that TransformerFAM significantly improves Transformer performance on long-context tasks across various model sizes (1B, 8B, and 24B). These results showcase the potential to empower Large Language Models (LLMs) to process sequences of unlimited length.

### Weaknesses

1. The authors should provide more details about the implementation of the proposed method. For example, how to initialize the FAM, how to update it during training, and how to use it during inference.

2. The authors should provide more details about the experimental setup. For example, how to split the data into blocks, how to set the hyperparameters, and how to compare the proposed method with the baselines.

3. The authors should provide a more detailed analysis of the computational complexity and compare it with other methods.

### Questions

See above

### Flag For Ethics Review

No ethics review needed.

### Rating

5: marginally below the acceptance threshold

### Confidence

3: You are fairly confident in your assessment. It is possible that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work. Math/other details were not carefully checked.

**********

## Meta Review

This paper proposes a new method for working memory in transformers. The method is based on a feedback loop, which is a common approach in recurrent neural networks. The paper presents some experimental results, which are not very convincing.

### justification_for_why_not_higher_score

The experimental results are not very convincing. The paper presents some experimental results, but they are not very convincing. The paper does not provide a thorough analysis of the computational complexity of the proposed method, and the experiments are not conducted on a wide range of long-context tasks. The paper also lacks a clear explanation of how the proposed method is trained and used during inference.

### justification_for_why_not_lower_score

N/A

**********

## Paper Decision

Reject (out of the scope of ICLR)

**********

## Paper Decision Summary

This paper introduces a novel Transformer architecture called TransformerFAM, which leverages a feedback loop to enable the network to attend to its own latent representations. This design fosters the emergence of working memory within the Transformer, allowing it to process indefinitely long sequences. TransformerFAM requires no additional weights, enabling seamless integration with pre-trained models. The paper shows that TransformerFAM significantly improves Transformer performance on long-context tasks across various model sizes (1B, 8B, and 24B). These results showcase the potential to empower Large Language Models (LLMs) to process sequences of unlimited length.

### justification_for_why_not_higher_score

The experimental results are not very convincing. The paper presents some experimental results, but they are not very convincing. The paper does not provide a thorough analysis of the computational complexity of the proposed method, and the experiments are not conducted on a wide range of long-context tasks. The paper also lacks a clear explanation of how the proposed method is trained and used during inference.

### justification_for_why_not_lower_score

N/A

**********

## Paper Decision Final Feedback

This paper introduces a novel Transformer architecture called TransformerFAM, which leverages a feedback loop to enable the network to attend to its own latent representations. This design fosters the emergence of working memory within the Transformer, allowing it to process indefinitely long sequences. TransformerFAM requires no additional weights, enabling seamless integration with pre-trained models. The paper shows that TransformerFAM significantly improves Transformer performance on long-context tasks across various model sizes (1B, 8B, and 24B). These results showcase the potential to empower Large Language Models (LLMs) to process sequences of unlimited length.

**********

## Paper Decision Final Feedback

Reject (out of the scope of ICLR)

**********

<!-- Added by arXiv -->
<!---->

***

## Qualities desired in a top-tier conference paper

1. Significance: The paper addresses a significant problem or has a substantial impact on the field.
2. Clarity: The paper is well-written, and its ideas are presented clearly and concisely.
3. Originality: The paper presents novel ideas, methods, or findings that have not been previously published.
4. Quality: The paper's technical quality is high, with rigorous experimentation, sound methodology, and thorough evaluation.
5. Presentation: The paper is well-organized, and its structure effectively communicates its content.
6. Reproducibility: The paper provides sufficient details for others to reproduce its results.
7. Code: The paper includes code or provides a clear path for others to obtain the code.
8. Data: The paper includes data or provides a clear path for others to obtain the data.
9. Ethics: The paper considers ethical implications and ensures that its research is conducted responsibly.
10. Broad Impact: The paper's contributions have the potential to impact a broad audience beyond the immediate research community.

***

<!-- End Added by arXiv -->