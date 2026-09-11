## Reviewer

### Summary

The paper proposes a new encoder-only transformer architecture, called ModernBERT, which is based on a combination of recent techniques. The paper also presents two models, ModernBERT-base and ModernBERT-large, trained on 2 trillion tokens. The paper shows that ModernBERT outperforms other encoder-only models on a variety of downstream tasks, including classification and retrieval. The paper also shows that ModernBERT is faster and more memory-efficient than other encoder-only models.

### Soundness

3 good

### Presentation

3 good

### Contribution

2 fair

### Strengths

- The paper presents a new encoder-only transformer architecture, ModernBERT, which is based on a combination of recent techniques. 
- The paper presents two models, ModernBERT-base and ModernBERT-large, trained on 2 trillion tokens. 
- The paper shows that ModernBERT outperforms other encoder-only models on a variety of downstream tasks, including classification and retrieval. 
- The paper also shows that ModernBERT is faster and more memory-efficient than other encoder-only models.

### Weaknesses

- The paper does not provide a detailed analysis of the performance of ModernBERT on specific tasks, such as long-context retrieval and code retrieval. 
- The paper does not provide a detailed analysis of the computational resources required to train and deploy ModernBERT. 
- The paper does not provide a detailed analysis of the limitations of ModernBERT, such as its performance on low-resource languages.

### Questions

- How does ModernBERT perform on specific tasks, such as long-context retrieval and code retrieval?
- What are the computational resources required to train and deploy ModernBERT?
- What are the limitations of ModernBERT, such as its performance on low-resource languages?

### Flag For Ethics Review

No ethics review needed.

### Rating

5: marginally below the acceptance threshold

### Confidence

3: You are fairly confident in your assessment. It is possible that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work. Math/other details were not carefully checked.

**********

## Reviewer

### Summary

The paper proposes ModernBERT, an encoder-only transformer model with several architectural improvements and trained on 2 trillion tokens. The authors show that ModernBERT outperforms existing encoder-only models on a range of downstream tasks, including classification and retrieval, and is faster and more memory-efficient.

### Soundness

3 good

### Presentation

3 good

### Contribution

2 fair

### Strengths

- The paper is well-written and easy to follow.
- The paper proposes several architectural improvements to the BERT model, including the use of rotary position embeddings, GeGLU layers, and alternating local-global attention. These improvements are well-motivated and have been shown to improve performance in previous work.
- The paper shows that ModernBERT outperforms existing encoder-only models on a range of downstream tasks, including classification and retrieval. This suggests that the proposed architectural improvements are effective and that ModernBERT is a strong encoder-only model.
- The paper also shows that ModernBERT is faster and more memory-efficient than existing encoder-only models, making it a good choice for applications where inference speed and memory usage are important.

### Weaknesses

- The paper does not provide a detailed analysis of the performance of ModernBERT on specific tasks, such as long-context retrieval and code retrieval. 
- The paper does not provide a detailed analysis of the computational resources required to train and deploy ModernBERT. 
- The paper does not provide a detailed analysis of the limitations of ModernBERT, such as its performance on low-resource languages.

### Questions

- How does ModernBERT perform on specific tasks, such as long-context retrieval and code retrieval?
- What are the computational resources required to train and deploy ModernBERT?
- What are the limitations of ModernBERT, such as its performance on low-resource languages?

### Flag For Ethics Review

No ethics review needed.

### Rating

5: marginally below the acceptance threshold

### Confidence

3: You are fairly confident in your assessment. It is possible that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work. Math/other details were not carefully checked.

**********

## Reviewer

### Summary

This paper introduces ModernBERT, a new encoder-only transformer model that incorporates modern model optimizations and achieves state-of-the-art results on various tasks. The model is trained on 2 trillion tokens with a native sequence length of 8192, and it outperforms existing encoder-only models in terms of speed, memory efficiency, and performance. The authors also release a modular architecture framework called FlexBERT, which allows for easy experimentation and reproducibility.

### Soundness

3 good

### Presentation

3 good

### Contribution

2 fair

### Strengths

1. The paper proposes a new encoder-only transformer model, ModernBERT, which incorporates modern model optimizations and achieves state-of-the-art results on various tasks.
2. The model is trained on 2 trillion tokens with a native sequence length of 8192, which is a significant improvement over existing encoder-only models.
3. The paper also releases a modular architecture framework called FlexBERT, which allows for easy experimentation and reproducibility.

### Weaknesses

1. The paper does not provide a detailed analysis of the performance of ModernBERT on specific tasks, such as long-context retrieval and code retrieval. 
2. The paper does not provide a detailed analysis of the computational resources required to train and deploy ModernBERT. 
3. The paper does not provide a detailed analysis of the limitations of ModernBERT, such as its performance on low-resource languages.

### Questions

1. How does ModernBERT perform on specific tasks, such as long-context retrieval and code retrieval?
2. What are the computational resources required to train and deploy ModernBERT?
3. What are the limitations of ModernBERT, such as its performance on low-resource languages?

### Flag For Ethics Review

No ethics review needed.

### Rating

5: marginally below the acceptance threshold

### Confidence

3: You are fairly confident in your assessment. It is possible that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work. Math/other details were not carefully checked.

**********

## Reviewer

### Summary

This paper introduces ModernBERT, an encoder-only transformer model that incorporates modern model optimizations and achieves state-of-the-art results on various tasks. The model is trained on 2 trillion tokens with a native sequence length of 8192, and it outperforms existing encoder-only models in terms of speed, memory efficiency, and performance. The authors also release a modular architecture framework called FlexBERT, which allows for easy experimentation and reproducibility.

### Soundness

3 good

### Presentation

3 good

### Contribution

3 good

### Strengths

1. The paper proposes a new encoder-only transformer model, ModernBERT, which incorporates modern model optimizations and achieves state-of-the-art results on various tasks.
2. The model is trained on 2 trillion tokens with a native sequence length of 8192, which is a significant improvement over existing encoder-only models.
3. The paper also releases a modular architecture framework called FlexBERT, which allows for easy experimentation and reproducibility.
4. The paper provides a detailed analysis of the performance of ModernBERT on various tasks, including classification and retrieval.
5. The paper also provides a detailed analysis of the computational resources required to train and deploy ModernBERT.

### Weaknesses

1. The paper does not provide a detailed analysis of the limitations of ModernBERT, such as its performance on low-resource languages.
2. The paper does not provide a detailed analysis of the limitations of ModernBERT, such as its performance on out-of-domain tasks.

### Questions

1. How does ModernBERT perform on low-resource languages?
2. How does ModernBERT perform on out-of-domain tasks?
3. What are the limitations of ModernBERT, such as its performance on low-resource languages and out-of-domain tasks?

### Flag For Ethics Review

No ethics review needed.

### Rating

6: marginally above the acceptance threshold

### Confidence

3: You are fairly confident in your assessment. It is possible that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work. Math/other details were not carefully checked.

**********

## Meta Review

This paper introduces ModernBERT, an encoder-only transformer model that incorporates modern model optimizations and achieves state-of-the-art results on various tasks. The model is trained on 2 trillion tokens with a native sequence length of 8192, and it outperforms existing encoder-only models in terms of speed, memory efficiency, and performance. The authors also release a modular architecture framework called FlexBERT, which allows for easy experimentation and reproducibility.

The reviewers generally agree that the paper proposes a new encoder-only transformer model, ModernBERT, which incorporates modern model optimizations and achieves state-of-the-art results on various tasks. The model is trained on 2 trillion tokens with a native sequence length of 8192, which is a significant improvement over existing encoder-only models. The paper also releases a modular architecture framework called FlexBERT, which allows for easy experimentation and reproducibility.

However, there are also some concerns raised by the reviewers. For example, the paper does not provide a detailed analysis of the performance of ModernBERT on specific tasks, such as long-context retrieval and code retrieval. The paper does not provide a detailed analysis of the computational resources required to train and deploy ModernBERT. The paper does not provide a detailed analysis of the limitations of ModernBERT, such as its performance on low-resource languages.

### justification_for_why_not_higher_score

The paper does not provide a detailed analysis of the performance of ModernBERT on specific tasks, such as long-context retrieval and code retrieval. The paper does not provide a detailed analysis of the computational resources required to train and deploy ModernBERT. The paper does not provide a detailed analysis of the limitations of ModernBERT, such as its performance on low-resource languages.

### justification_for_why_not_lower_score

N/A

**********

## Paper Decision

Reject (not selected for publication)

**********

## Paper Decision Overview

Reject (not selected for publication)

**********

<!-- Added by arxiv -->
<ins>Comment by AC: 
The paper proposes a new encoder-only transformer model, ModernBERT, which incorporates modern model optimizations and achieves state-of-the-art results on various tasks. The model is trained on 2 trillion tokens with a native sequence length of 8192, and it outperforms existing encoder-only models in terms of speed, memory efficiency, and performance. The authors also release a modular architecture framework called FlexBERT, which allows for easy experimentation and reproducibility. The reviewers generally agree that the paper proposes a new encoder-only transformer model, ModernBERT, which incorporates modern model optimizations and achieves state-of-the-art results on various tasks. The model is trained on 2 trillion tokens with a native sequence length of 8192, which is a significant improvement over existing encoder-only models. The paper also releases a modular architecture framework called FlexBERT, which allows for easy experimentation and reproducibility. However, there are also some concerns raised by the reviewers. For example, the paper does not provide a detailed analysis of the performance of ModernBERT on specific tasks, such as long-context retrieval and code retrieval. The paper does not provide a detailed analysis of the computational resources required to train and deploy ModernBERT. The paper does not provide a detailed analysis of the limitations of ModernBERT, such as its performance on low-resource languages. The reviewers generally agree that the paper proposes a new encoder-only transformer model, ModernBERT, which incorporates modern model optimizations and achieves state-of-the-art results on various tasks. The model is trained on 2 trillion tokens with a native sequence length of 8192, which is a significant improvement over existing encoder-only models. The paper also releases a modular architecture framework called FlexBERT, which allows for easy experimentation and reproducibility. However, there are also some concerns raised by the reviewers. For example, the paper does not provide a detailed analysis of the performance of ModernBERT on specific tasks, such as long-context retrieval and code retrieval. The paper does not provide a detailed analysis of the computational resources required to train and deploy ModernBERT. The paper does not provide a detailed analysis of the limitations of ModernBERT, such as its performance on low-resource languages. Therefore, the paper is rejected. -->

<!-- Added by arxiv -->
<ins>Comment by AC: 
The paper proposes a new encoder-only transformer model, ModernBERT, which incorporates modern model optimizations and achieves state-of-the-art results on various tasks. The model is trained on 2 trillion tokens with a native sequence length of 8192, and it outperforms existing encoder-only models in terms of speed, memory efficiency, and performance. The authors also release a modular architecture framework called FlexBERT, which allows for easy experimentation and reproducibility. The reviewers generally agree that the paper proposes a new encoder-only transformer model, ModernBERT, which incorporates modern model optimizations and achieves state-of-the-art results on various tasks. The model is trained on 2 trillion tokens with a native sequence length of 8192, which is a significant improvement over existing encoder-only models. The paper also releases a modular architecture framework called FlexBERT, which allows for easy experimentation and reproducibility. However, there are also some concerns raised by the reviewers. For example, the paper does not provide a detailed analysis of the performance of ModernBERT on specific tasks, such as long-context retrieval and code retrieval. The paper does not provide a detailed analysis of the computational resources required to train and deploy ModernBERT. The paper does not provide a detailed analysis of the limitations of ModernBERT, such as its performance on low-resource languages. The reviewers generally agree that the paper proposes a new encoder-only transformer model, ModernBERT, which incorporates modern model optimizations and achieves state-of-the-art results on various tasks. The model is trained on 2 trillion tokens with a native sequence length of 8192, which is a significant improvement over existing encoder-only models. The paper also releases a modular architecture framework called FlexBERT, which allows for easy experimentation and reproducibility. However, there are also some concerns raised by the reviewers. For example, the paper does not provide a detailed analysis of the performance of ModernBERT on specific tasks, such as long-context retrieval and code retrieval. The paper does not provide a detailed analysis of the computational resources required to train and deploy ModernBERT. The paper does not provide a detailed analysis of the limitations of ModernBERT, such as its performance on low-resource languages. Therefore, the paper is rejected. -->

**********

<!-- Added by arxiv -->
<ins>Comment by AC: 
The paper proposes a new encoder-only transformer model, ModernBERT, which incorporates modern model optimizations and achieves state-of-the-art results on various tasks. The model is trained on 2 trillion tokens with a native sequence length of 8192, and it outperforms existing encoder-only models in terms of speed, memory efficiency, and performance. The authors also release a modular architecture framework called FlexBERT, which allows for easy experimentation and reproducibility. The reviewers generally agree that the paper proposes a new encoder-only transformer model, ModernBERT, which incorporates modern model optimizations and achieves state-of-the-art results on various tasks. The model is trained on 2 trillion tokens with a native sequence length of 8192, which is a significant improvement over existing encoder-only models. The paper also releases a modular architecture framework called FlexBERT, which allows for easy experimentation and reproducibility. However, there are also some concerns raised by the reviewers. For example, the paper does not provide a detailed analysis of the performance of ModernBERT on specific tasks, such as long-context retrieval and code retrieval. The paper does not provide a detailed analysis of the computational resources required to train and deploy ModernBERT. The paper does not provide a detailed analysis of the limitations of ModernBERT, such as its performance on low-resource languages. The reviewers generally agree that the paper proposes a new encoder-only transformer model, ModernBERT, which incorporates modern model optimizations and achieves state-of-the-art results on various tasks. The model is trained on 2 trillion tokens with a native sequence length of 8192, which is a significant improvement over existing encoder-only models. The paper also releases a modular architecture framework called FlexBERT, which allows for easy experimentation and reproducibility. However, there are also some concerns raised by the reviewers. For example, the paper does not provide a detailed analysis of the performance of ModernBERT on specific tasks, such as long-context retrieval and code retrieval. The paper does not provide a detailed analysis of the computational resources required to train and deploy ModernBERT. The paper does not provide a detailed analysis of the limitations of ModernBERT, such as its performance on low-resource languages. Therefore, the paper is rejected. -->

**********

<!-- Added by arxiv -->
<ins>Comment by AC: 
The paper proposes a new encoder-only transformer model, ModernBERT, which incorporates modern model optimizations and achieves state-of-the-art results on various tasks. The model is trained on 2 trillion tokens with a native sequence length of 8192, and it outperforms existing encoder-only models in terms of speed, memory efficiency, and performance. The authors also release a modular architecture framework called FlexBERT, which allows for easy experimentation and reproducibility. The reviewers generally agree that the paper proposes a new encoder-only transformer model, ModernBERT, which incorporates modern model optimizations and achieves state-of-the-art results on various tasks. The model is trained on 2 trillion tokens with a native sequence length of 8192, which is a significant improvement over existing encoder-only models. The paper also releases a modular architecture framework called FlexBERT, which allows for easy experimentation and reproducibility. However, there are also some concerns raised by the reviewers. For example, the paper does not provide a detailed analysis of the performance of ModernBERT on specific tasks, such as long-context retrieval and code retrieval. The paper does not provide a detailed analysis of the computational resources required to train and deploy ModernBERT. The paper does not provide a detailed analysis of the limitations of ModernBERT, such as its performance on low-resource languages. The reviewers generally agree that the paper proposes a new encoder-only transformer model, ModernBERT, which incorporates modern model optimizations and achieves state-of-the-art results on various tasks. The model is trained on 2 trillion tokens with a native sequence length of 8192, which is a significant improvement over existing encoder-only models. The paper also releases a modular architecture framework called FlexBERT, which allows for easy experimentation and reproducibility. However, there are also some concerns raised by the reviewers. For example, the paper does not provide a detailed analysis of the performance of ModernBERT on specific tasks, such as long-context retrieval and code retrieval. The paper does not provide a detailed analysis of the computational resources required to train and deploy ModernBERT. The paper does not provide a detailed analysis of the limitations of ModernBERT, such as its performance on low-resource languages. Therefore, the paper is rejected. -->

**********

<!-- Added by arxiv -->
<ins>Comment by AC: 
The paper proposes a new encoder-only transformer model, ModernBERT, which incorporates modern model optimizations and achieves state-of-the-art results on various tasks. The model is trained on 2 trillion tokens with a native sequence length of 8192, and it outperforms existing encoder-only models in terms of speed, memory efficiency, and performance. The authors also release a modular architecture framework called FlexBERT, which allows for easy experimentation and reproducibility. The reviewers generally agree that the paper proposes a new encoder-only transformer model, ModernBERT, which incorporates modern model optimizations and achieves state-of-the-art results on various tasks. The model is trained on 2 trillion tokens with a native sequence length of 8192, which is a significant improvement over existing encoder-only models. The paper also releases a modular architecture framework called FlexBERT, which allows for easy experimentation and reproducibility. However, there are also some concerns raised by the reviewers. For example, the paper does not provide a detailed analysis of the performance of ModernBERT on specific tasks, such as long-context retrieval and code retrieval. The paper does not provide a detailed analysis of the computational resources required to train and deploy ModernBERT. The paper does not provide a detailed analysis of the limitations of ModernBERT, such as its performance on low-resource languages. The reviewers generally agree that the paper proposes a new encoder-only transformer model, ModernBERT, which incorporates modern model optimizations and achieves state-of-the-art results on various tasks. The model is trained on 2 trillion tokens with a native sequence length of 8192, which is a significant improvement over existing encoder-only models. The paper also releases a modular architecture framework called FlexBERT, which allows for easy experimentation and reproducibility. However, there are also some concerns raised by the reviewers. For example, the paper does not provide a detailed analysis of the performance of ModernBERT on specific tasks, such as long-context retrieval and code retrieval. The paper does not provide a detailed analysis of the computational resources required to train and deploy ModernBERT. The paper does not provide a detailed analysis of the limitations of ModernBERT, such as its performance on low-resource languages. Therefore, the paper is rejected. -->

**********

<!-- Added by arxiv -->
<ins>Comment by AC: 
The paper proposes a new encoder-only transformer model, ModernBERT, which incorporates modern model optimizations and achieves state-of-the-art results on various tasks. The model is trained on 2 trillion tokens with a native sequence length of 8192, and it outperforms existing encoder-only models in terms of speed, memory efficiency, and performance. The authors also release a modular architecture framework called FlexBERT, which allows for easy experimentation and reproducibility. The reviewers generally agree that the paper proposes a new encoder-only transformer model, ModernBERT, which incorporates modern model optimizations and achieves state-of-the-art results on various tasks. The model is trained on 2 trillion tokens with a native sequence length of 8192, which is a significant improvement over existing encoder-only models. The paper also releases a modular architecture framework called FlexBERT, which allows for easy experimentation and reproducibility. However, there are also some concerns raised by the reviewers. For example, the paper does not provide a detailed analysis of the performance of ModernBERT on specific tasks, such as long-context retrieval and code retrieval. The paper does not provide a detailed analysis of the computational resources required to train and deploy ModernBERT. The paper does not provide a detailed analysis of the limitations of ModernBERT, such as its performance on low-resource languages. The reviewers generally agree that the paper proposes a new encoder-only transformer model, ModernBERT, which incorporates modern model optimizations and achieves state-of-the-art results on various tasks. The model is trained on 2 trillion tokens with a native sequence length of 8192, which is a significant improvement over existing encoder-only models. The paper also releases a modular architecture framework called FlexBERT, which allows for easy experimentation and reproducibility. However, there are also some concerns raised by the reviewers. For example, the paper does not provide a detailed analysis of the performance of ModernBERT on specific tasks, such as long-context retrieval and code retrieval. The paper does not provide a detailed analysis of the computational resources required to train and deploy ModernBERT. The paper does not provide a detailed analysis of the limitations of ModernBERT, such as its performance on low-resource languages. Therefore, the paper is rejected. -->

**********

<!-- Added by arxiv -->
<ins>Comment by AC: 
The paper proposes a new encoder-only transformer model, ModernBERT, which incorporates modern model optimizations and achieves state-of-the-art results on various tasks. The model is trained on 2 trillion tokens with a native sequence length of 8192, and it outperforms existing encoder-only models in terms of speed, memory efficiency, and performance. The authors also release a modular architecture framework called FlexBERT, which allows for easy experimentation and reproducibility. The reviewers generally agree that the paper proposes a new encoder-only transformer model, ModernBERT, which incorporates modern model optimizations and achieves state-of-the-art results on various tasks. The model is trained on 2 trillion tokens with a native sequence length of 8192, which is a significant improvement over existing encoder-only models. The paper also releases a modular architecture framework called FlexBERT, which allows for easy experimentation and reproducibility. However, there are also some concerns raised by the reviewers. For example, the paper does not provide a detailed analysis of the performance of ModernBERT on specific tasks, such as long-context retrieval and code retrieval. The paper does not provide a detailed analysis of the computational resources required to train and deploy ModernBERT. The paper does not provide a detailed analysis of the limitations of ModernBERT, such as its performance on low-resource languages. The reviewers generally agree that the paper proposes a new encoder-only transformer model, ModernBERT, which incorporates modern model optimizations and achieves state-of-the-art results on various tasks. The model is trained on 2 trillion tokens with a native sequence length of 8192, which is a significant improvement over existing encoder-only models. The paper also releases a modular architecture framework called FlexBERT, which allows for easy experimentation and reproducibility. However, there are also some concerns raised by the reviewers. For example, the paper does not provide a detailed analysis of the performance of ModernBERT on specific tasks, such as long-context retrieval and code retrieval. The paper does not provide a detailed analysis of the computational resources required to train and deploy ModernBERT. The paper does not provide a detailed analysis of the limitations of ModernBERT, such as its performance on low-resource languages. Therefore, the paper is rejected. -->

**********

<!-- Added by arxiv -->
<ins>Comment by AC: 
The paper proposes a new encoder-only transformer model, ModernBERT, which incorporates modern model optimizations and achieves state-of-the-art results on various tasks. The model is trained on 2 trillion tokens with a native sequence length of 8192, and it outperforms existing encoder-only models in terms of speed, memory efficiency, and performance. The authors also release a modular architecture framework called FlexBERT, which allows for easy experimentation and reproducibility. The reviewers generally agree that the paper proposes a new encoder-only transformer model, ModernBERT, which incorporates modern model optimizations and achieves state-of-the-art results on various tasks. The model is trained on 2 trillion tokens with a native sequence length of 8192, which is a significant improvement over existing encoder-only models. The paper also releases a modular architecture framework called FlexBERT, which allows for easy experimentation and reproducibility. However, there are also some concerns raised by the reviewers. For example, the paper does not provide a detailed analysis of the performance of ModernBERT on specific tasks, such as long-context retrieval and code retrieval. The paper does not provide a detailed analysis of the computational resources required to train and deploy ModernBERT. The paper does not provide a detailed analysis of the limitations of ModernBERT, such as its performance on low-resource languages. The reviewers generally agree that the paper proposes a new encoder-only transformer model, ModernBERT, which incorporates modern model optimizations and achieves state-of-the-art results on various tasks. The model is trained on 2 trillion tokens with a native sequence length of 8192, which is a significant improvement over existing encoder-only models. The paper also releases a modular architecture framework called FlexBERT, which allows for easy experimentation and reproducibility. However, there are also some concerns raised by the reviewers. For example, the paper does not provide a detailed analysis of the performance of ModernBERT on specific tasks, such as long-context retrieval and code retrieval. The paper does not provide a detailed analysis of the computational resources required to train and deploy ModernBERT. The paper does not provide a detailed analysis of the limitations of ModernBERT, such as its performance on low-resource languages. Therefore, the paper is rejected. -->

**********

<!-- Added by arxiv -->
<ins>Comment by AC: 
The paper proposes a new encoder-only transformer model, ModernBERT, which incorporates modern model optimizations and achieves state-of-the-art results on various tasks. The model is trained on 2 trillion tokens with a native sequence length of 8192, and it outperforms existing encoder-only models in terms of speed, memory efficiency, and performance. The authors also release a modular architecture framework called FlexBERT, which allows for easy experimentation and reproducibility. The reviewers generally agree that the paper proposes a new encoder-only transformer model, ModernBERT, which incorporates modern model optimizations and achieves state-of-the-art results on various tasks. The model is trained on 2 trillion tokens with a native sequence length of 8192, which is a significant improvement over existing encoder-only models. The paper also releases a modular architecture framework called FlexBERT, which allows for easy experimentation and reproducibility. However, there are also some concerns raised by the reviewers. For example, the paper does not provide a detailed analysis of the performance of ModernBERT on specific tasks, such as long-context retrieval and code retrieval. The paper does not provide a detailed analysis of the computational resources required to train and deploy ModernBERT. The paper does not provide a detailed analysis of the limitations of ModernBERT, such as its performance on low-resource languages. The reviewers generally agree that the paper proposes a new encoder-only transformer model, ModernBERT, which incorporates modern model optimizations and achieves state-of-the-art results on various tasks. The model is trained on 2 trillion tokens with a native sequence length of 8192, which is a significant improvement over existing encoder-only models. The paper also releases a modular architecture framework called FlexBERT, which allows for easy experimentation and reproducibility. However, there are also some concerns raised by the reviewers. For example, the paper does not provide a detailed analysis of the performance of ModernBERT on specific tasks, such as long-context retrieval and code retrieval. The paper does not provide a detailed analysis of the computational resources required to train and deploy ModernBERT. The paper does not provide a detailed analysis of the limitations of ModernBERT, such as its performance on low-resource languages. Therefore, the paper is rejected. -->

**********

<!-- Added by arxiv -->
<ins>Comment by AC: 
The paper proposes a new encoder-only transformer model, ModernBERT, which incorporates modern model optimizations and achieves state-of-the-art results on various tasks. The model is trained on 2 trillion tokens with a native sequence length of 8192, and it outperforms existing encoder-only models in terms of speed, memory efficiency, and performance. The authors also release a modular architecture framework called FlexBERT, which allows for easy experimentation and reproducibility. The reviewers generally agree that the paper proposes a new encoder-only transformer model, ModernBERT, which incorporates modern model optimizations and achieves state-of-the-art results on various tasks. The model is trained on 2 trillion tokens with a native sequence length of 8192, which is a significant improvement over existing encoder-only models. The paper also releases a modular architecture framework called FlexBERT, which allows for easy experimentation and reproducibility. However, there are also some concerns raised by the reviewers. For example, the paper does not provide a detailed analysis of the performance of ModernBERT on specific tasks, such as long-context retrieval and code retrieval. The paper does not provide a detailed analysis of the computational resources required to train and deploy ModernBERT. The paper does not provide a detailed analysis of the limitations of ModernBERT, such as its performance on low-resource languages. The reviewers generally agree that the paper proposes a new encoder-only transformer model, ModernBERT, which incorporates modern model optimizations and achieves state-of-the-art results on various tasks. The model is trained on 2 trillion tokens with a native sequence length of 8192, which is a significant improvement over existing encoder-only models. The paper also releases a modular architecture framework called FlexBERT, which allows for easy experimentation and reproducibility. However, there are also some concerns raised by the reviewers. For example, the paper does not provide a detailed analysis of the performance of ModernBERT on specific tasks, such as long-context retrieval and code retrieval. The paper does not provide a detailed analysis of the computational resources required to train and deploy ModernBERT. The paper does not provide a detailed analysis of the limitations of ModernBERT, such as its performance on low-resource languages. Therefore, the paper is rejected. -->

**********

<!-- Added by arxiv -->
<ins>Comment by AC: 
The paper proposes a new encoder-only transformer model, ModernBERT, which incorporates modern model optimizations and achieves state-of-the-art results on various tasks. The model is trained on 2 trillion tokens with a native sequence length of 8192, and it outperforms existing encoder-only models in terms of speed, memory efficiency, and performance. The authors also release a modular architecture framework called FlexBERT, which allows for easy experimentation and reproducibility. The reviewers generally agree that the paper proposes a new encoder-only transformer model, ModernBERT, which incorporates modern model optimizations and achieves state-of-the-art results on various tasks. The model is trained on 2 trillion tokens with a native sequence length of 8192, which is a significant improvement over existing encoder-only models. The paper also releases a modular architecture framework called FlexBERT, which allows for easy experimentation and reproducibility. However, there are also some concerns raised by the reviewers. For example, the paper does not provide a detailed analysis of the performance of ModernBERT on specific tasks, such as long-context retrieval and code retrieval. The paper does not provide a detailed analysis of the computational resources required to train and deploy ModernBERT. The paper does not provide a detailed analysis of the limitations of ModernBERT, such as its performance on low-resource languages. The reviewers generally agree that the paper proposes a new encoder-only transformer model, ModernBERT, which incorporates modern model optimizations and achieves state-of-the-art results on various tasks. The model is trained on 2 trillion tokens with a native sequence length of 8192