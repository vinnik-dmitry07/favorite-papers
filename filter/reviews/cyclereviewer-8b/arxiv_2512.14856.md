## Reviewer

### Summary

This paper introduces T5Gemma 2, a lightweight encoder-decoder model that is capable of multimodal and long-context capabilities. The paper extends the T5Gemma family of models by adapting a pretrained decoder-only model into an encoder-decoder model, using the UL2 objective. The paper also proposes two methods to improve efficiency: tied word embeddings and merged attention. The experiments demonstrate the generality of the adaptation strategy across architectures and modalities and the strength of the encoder-decoder architecture on long-context modeling. The paper also releases the pretrained models to the community for future research.

### Soundness

2 fair

### Presentation

2 fair

### Contribution

2 fair

### Strengths

- The paper introduces T5Gemma 2, a lightweight encoder-decoder model that is capable of multimodal and long-context capabilities.
- The paper proposes two methods to improve efficiency: tied word embeddings and merged attention.
- The experiments demonstrate the generality of the adaptation strategy across architectures and modalities and the strength of the encoder-decoder architecture on long-context modeling.
- The paper also releases the pretrained models to the community for future research.

### Weaknesses

- The paper does not provide a detailed comparison with other existing models in the field, making it difficult to assess its novelty and significance.
- The paper does not provide a detailed discussion of the limitations of the proposed methods and potential future research directions.
- The paper does not provide a detailed discussion of the ethical considerations related to the use of large language models.

### Questions

- How does T5Gemma 2 compare to other existing models in the field in terms of performance and efficiency?
- What are the limitations of the proposed methods and what are the potential future research directions?
- What are the ethical considerations related to the use of large language models?

### Flag For Ethics Review

No ethics review needed.

### Rating

3: reject, not good enough

### Confidence

3: You are fairly confident in your assessment. It is possible that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work. Math/other details were not carefully checked.

**********

## Reviewer

### Summary

This paper introduces T5Gemma 2, a lightweight encoder-decoder model that is capable of multimodal and long-context capabilities. The paper extends the T5Gemma family of models by adapting a pretrained decoder-only model into an encoder-decoder model, using the UL2 objective. The paper also proposes two methods to improve efficiency: tied word embeddings and merged attention. The experiments demonstrate the generality of the adaptation strategy across architectures and modalities and the strength of the encoder-decoder architecture on long-context modeling. The paper also releases the pretrained models to the community for future research.

### Soundness

2 fair

### Presentation

3 good

### Contribution

2 fair

### Strengths

1. The paper is well written and easy to follow.

2. The proposed T5Gemma 2 is capable of multimodal and long-context capabilities.

3. The paper releases the pretrained models to the community for future research.

### Weaknesses

1. The novelty of the proposed method is limited. The proposed T5Gemma 2 is an extension of T5Gemma. The proposed method is also similar to other works, such as GPT-4-32k, which also uses the UL2 objective and the same vision encoder. 

2. The experimental results are not convincing. The proposed T5Gemma 2 only shows comparable performance to Gemma 3 on some benchmarks.

### Questions

1. What are the advantages of T5Gemma 2 over Gemma 3?

2. Can the proposed method be applied to other decoder-only models, such as GPT-4-32k?

### Flag For Ethics Review

No ethics review needed.

### Rating

5: marginally below the acceptance threshold

### Confidence

4: You are confident in your assessment, but not absolutely certain. It is unlikely, but not impossible, that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work.

**********

## Reviewer

### Summary

This paper introduces T5Gemma 2, an encoder-decoder model that is capable of multimodal and long-context capabilities. The paper extends the T5Gemma family of models by adapting a pretrained decoder-only model into an encoder-decoder model, using the UL2 objective. The paper also proposes two methods to improve efficiency: tied word embeddings and merged attention. The experiments demonstrate the generality of the adaptation strategy across architectures and modalities and the strength of the encoder-decoder architecture on long-context modeling. The paper also releases the pretrained models to the community for future research.

### Soundness

2 fair

### Presentation

3 good

### Contribution

2 fair

### Strengths

The paper is well written and easy to follow. The proposed T5Gemma 2 is capable of multimodal and long-context capabilities.

### Weaknesses

The novelty of the proposed method is limited. The proposed T5Gemma 2 is an extension of T5Gemma. The proposed method is also similar to other works, such as GPT-4-32k, which also uses the UL2 objective and the same vision encoder. 

The experimental results are not convincing. The proposed T5Gemma 2 only shows comparable performance to Gemma 3 on some benchmarks.

### Questions

What are the advantages of T5Gemma 2 over Gemma 3?

Can the proposed method be applied to other decoder-only models, such as GPT-4-32k?

### Flag For Ethics Review

No ethics review needed.

### Rating

5: marginally below the acceptance threshold

### Confidence

3: You are fairly confident in your assessment. It is possible that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work. Math/other details were not carefully checked.

**********

## Reviewer

### Summary

This paper introduces T5Gemma 2, a new family of lightweight open encoder-decoder models, featuring strong multilingual, multimodal and long-context capabilities. T5Gemma 2 follows the adaptation recipe (via UL2) in T5Gemma – adapting a pretrained decoder-only model into an encoder-decoder model, and extends it from text-only regime to multimodal based on the Gemma 3 models. The authors propose two methods to improve the efficiency: tied word embedding that shares all embeddings across encoder and decoder, and merged attention that unifies decoder self- and cross-attention into a single joint module. Experiments demonstrate the generality of the adaptation strategy over architectures and modalities as well as the unique strength of the encoder-decoder architecture on long context modeling. Similar to T5Gemma, T5Gemma 2 yields comparable or better pretraining performance and significantly improved post-training performance than its Gemma 3 counterpart. The authors release the pretrained models (270M-270M, 1B-1B and 4B-4B) to the community for future research.

### Soundness

3 good

### Presentation

3 good

### Contribution

2 fair

### Strengths

1. The paper is well-written and easy to follow.
2. The authors propose two methods to improve the efficiency: tied word embedding that shares all embeddings across encoder and decoder, and merged attention that unifies decoder self- and cross-attention into a single joint module.
3. The authors release the pretrained models (270M-270M, 1B-1B and 4B-4B) to the community for future research.

### Weaknesses

1. The novelty of the proposed method is limited. The proposed T5Gemma 2 is an extension of T5Gemma. The proposed method is also similar to other works, such as GPT-4-32k, which also uses the UL2 objective and the same vision encoder. 
2. The experimental results are not convincing. The proposed T5Gemma 2 only shows comparable performance to Gemma 3 on some benchmarks.

### Questions

1. What are the advantages of T5Gemma 2 over Gemma 3?
2. Can the proposed method be applied to other decoder-only models, such as GPT-4-32k?

### Flag For Ethics Review

No ethics review needed.

### Rating

5: marginally below the acceptance threshold

### Confidence

4: You are confident in your assessment, but not absolutely certain. It is unlikely, but not impossible, that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work.

**********

## Meta Review

The paper introduces T5Gemma 2, a lightweight encoder-decoder model that is capable of multimodal and long-context capabilities. The paper extends the T5Gemma family of models by adapting a pretrained decoder-only model into an encoder-decoder model, using the UL2 objective. The paper also proposes two methods to improve efficiency: tied word embeddings and merged attention. The experiments demonstrate the generality of the adaptation strategy across architectures and modalities and the strength of the encoder-decoder architecture on long-context modeling. The paper also releases the pretrained models to the community for future research.

### justification_for_why_not_higher_score

The novelty of the proposed method is limited. The proposed T5Gemma 2 is an extension of T5Gemma. The proposed method is also similar to other works, such as GPT-4-32k, which also uses the UL2 objective and the same vision encoder. The experimental results are not convincing. The proposed T5Gemma 2 only shows comparable performance to Gemma 3 on some benchmarks.

### justification_for_why_not_lower_score

N/A

**********

**********

### justification_for_why_not_higher_score

The novelty of the proposed method is limited. The proposed T5Gemma 2 is an extension of T5Gemma. The proposed method is also similar to other works, such as GPT-4-32k, which also uses the UL2 objective and the same vision encoder. The experimental results are not convincing. The proposed T5Gemma 2 only shows comparable performance to Gemma 3 on some benchmarks.

### justification_for_why_not_lower_score

N/A

**********

**********

## Paper Decision

Reject (not selected for publication in ICLR 2024)

**********

<!-- Added "not selected for publication in ICLR 2024" to the end of the decision. -->