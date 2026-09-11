## Reviewer

### Summary

This paper proposes a method to extend the input length of any encoder-decoder transformer model. The method is based on a kNN search over the encoder output, which is used to select the attention keys for the decoder. The method is evaluated on summarization tasks.

### Soundness

3 good

### Presentation

3 good

### Contribution

2 fair

### Strengths

- The proposed method is simple and generic, and can be applied to any encoder-decoder transformer model.
- The method is evaluated on a range of summarization tasks.

### Weaknesses

- The method is only evaluated on summarization tasks. It is unclear how the method will perform on other tasks such as translation.
- The method requires a kNN search over the encoder output, which can be slow. This may limit the applicability of the method to long inputs.
- The method requires a large amount of memory to store the kNN index, which can be a limitation for very long inputs.

### Questions

- How does the method perform on tasks other than summarization?
- How does the method perform when applied to other encoder-decoder models, such as the standard transformer model?
- How does the kNN search affect the inference speed of the method?
- How does the size of the kNN index affect the memory requirements of the method?

### Flag For Ethics Review

No ethics review needed.

### Rating

5: marginally below the acceptance threshold

### Confidence

4: You are confident in your assessment, but not absolutely certain. It is unlikely, but not impossible, that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work.

**********

## Reviewer

### Summary

This paper proposes a method to extend the input length of any encoder-decoder transformer model. The method is based on a kNN search over the encoder output, which is used to select the attention keys for the decoder. The method is evaluated on summarization tasks.

### Soundness

3 good

### Presentation

3 good

### Contribution

3 good

### Strengths

- The proposed method is simple and generic, and can be applied to any encoder-decoder transformer model.
- The method is evaluated on a range of summarization tasks.

### Weaknesses

- The method is only evaluated on summarization tasks. It is unclear how the method will perform on other tasks such as translation.
- The method requires a kNN search over the encoder output, which can be slow. This may limit the applicability of the method to long inputs.
- The method requires a large amount of memory to store the kNN index, which can be a limitation for very long inputs.

### Questions

- How does the method perform on tasks other than summarization?
- How does the method perform when applied to other encoder-decoder models, such as the standard transformer model?
- How does the kNN search affect the inference speed of the method?
- How does the size of the kNN index affect the memory requirements of the method?

### Flag For Ethics Review

No ethics review needed.

### Rating

5: marginally below the acceptance threshold

### Confidence

4: You are confident in your assessment, but not absolutely certain. It is unlikely, but not impossible, that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work.

**********

## Reviewer

### Summary

The paper proposes Unlimiformer, a method that allows a transformer to attend to any token in the input sequence. This is achieved by indexing the hidden states of the encoder and using a kNN search to retrieve the top-k most similar tokens for each decoder layer. The authors evaluate their method on several long document summarization and book summarization benchmarks and show that it can improve the performance of several models such as BART and Longformer.

### Soundness

3 good

### Presentation

3 good

### Contribution

3 good

### Strengths

The paper is well-written and easy to follow. The idea is simple and effective. The evaluation is comprehensive and shows that Unlimiformer can improve the performance of several models on several long document and book summarization benchmarks.

### Weaknesses

The paper would be stronger if the authors could provide more analysis on the attention patterns of the model. For example, what are the most attended tokens in the input sequence? Are they the most relevant tokens for the task? How does this compare to the attention patterns of the original model?

### Questions

1. The authors claim that Unlimiformer can process inputs of unlimited length. However, in the experimental section, the authors only evaluate on inputs up to 500k tokens. How does the method perform on longer inputs?
2. How does the method perform on other tasks such as translation or question answering?
3. The authors use a kNN search to retrieve the top-k most similar tokens for each decoder layer. How does the choice of k affect the performance of the model? What is the optimal value of k for each task and model?
4. The authors use a single index for all decoder layers and heads. How does this affect the performance of the model? Would it be better to use separate indices for each layer and head?
5. The authors use a dot-product similarity metric for the kNN search. How does this compare to other similarity metrics such as cosine similarity?
6. The authors use a GPU index for inputs up to 500k tokens. How does the method perform when the index is offloaded to the CPU memory?
7. The authors use a single GPU for all experiments. How does the method perform when using multiple GPUs?

### Flag For Ethics Review

No ethics review needed.

### Rating

5: marginally below the acceptance threshold

### Confidence

3: You are fairly confident in your assessment. It is possible that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work. Math/other details were not carefully checked.

**********

## Reviewer

### Summary

The paper proposes a method to extend the input length of any encoder-decoder transformer model. The method is based on a kNN search over the encoder output, which is used to select the attention keys for the decoder. The method is evaluated on summarization tasks.

### Soundness

3 good

### Presentation

3 good

### Contribution

3 good

### Strengths

- The proposed method is simple and generic, and can be applied to any encoder-decoder transformer model.
- The method is evaluated on a range of summarization tasks.

### Weaknesses

- The method is only evaluated on summarization tasks. It is unclear how the method will perform on other tasks such as translation.
- The method requires a kNN search over the encoder output, which can be slow. This may limit the applicability of the method to long inputs.
- The method requires a large amount of memory to store the kNN index, which can be a limitation for very long inputs.

### Questions

- How does the method perform on tasks other than summarization?
- How does the method perform when applied to other encoder-decoder models, such as the standard transformer model?
- How does the kNN search affect the inference speed of the method?
- How does the size of the kNN index affect the memory requirements of the method?

### Flag For Ethics Review

No ethics review needed.

### Rating

5: marginally below the acceptance threshold

### Confidence

4: You are confident in your assessment, but not absolutely certain. It is unlikely, but not impossible, that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work.

**********

## Meta Review

This paper proposes Unlimiformer, a method to extend the input length of any encoder-decoder transformer model. The method is based on a kNN search over the encoder output, which is used to select the attention keys for the decoder. The method is evaluated on summarization tasks.

The reviewers raised several concerns about the paper, including the limited evaluation on summarization tasks, the computational cost of the kNN search, and the memory requirements for storing the kNN index. The authors did not provide any rebuttal. Therefore, I recommend rejecting this paper.

### justification_for_why_not_higher_score

The reviewers raised several concerns about the paper, including the limited evaluation on summarization tasks, the computational cost of the kNN search, and the memory requirements for storing the kNN index. The authors did not provide any rebuttal.

### justification_for_why_not_lower_score

N/A

**********

## Paper Decision

Reject (not selected for publication)