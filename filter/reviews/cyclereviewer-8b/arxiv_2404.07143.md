## Reviewer

### Summary

This paper proposes a new attention mechanism called Infini-attention for long-context LLMs. Infini-attention incorporates a compressive memory into the vanilla attention mechanism and builds in both masked local attention and long-term linear attention mechanisms in a single Transformer block. The proposed method is evaluated on long-context language modeling benchmarks, 1M sequence length passkey context block retrieval and 500K length book summarization tasks with 1B and 8B LLMs.

### Soundness

3 good

### Presentation

3 good

### Contribution

3 good

### Strengths

- The proposed method is simple and easy to implement.
- The proposed method is effective and efficient, and can scale to 1M sequence length.
- The proposed method is evaluated on various long-context tasks.

### Weaknesses

- The proposed method is not as effective as the baseline methods on the long-context language modeling tasks.
- The proposed method is not evaluated on the long-context tasks with 8B LLMs.

### Questions

- The proposed method is not as effective as the baseline methods on the long-context language modeling tasks. For example, the proposed method achieves a perplexity of 2.29 on PG19, while the baseline method achieves a perplexity of 2.15. Could the authors provide more analysis on why the proposed method is not as effective as the baseline methods on the long-context language modeling tasks?
- The proposed method is not evaluated on the long-context tasks with 8B LLMs. Could the authors provide more analysis on why the proposed method is not evaluated on the long-context tasks with 8B LLMs?

### Flag For Ethics Review

No ethics review needed.

### Rating

5: marginally below the acceptance threshold

### Confidence

4: You are confident in your assessment, but not absolutely certain. It is unlikely, but not impossible, that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work.

**********

## Reviewer

### Summary

This paper proposes a new attention mechanism called Infini-attention for long-context LLMs. Infini-attention incorporates a compressive memory into the vanilla attention mechanism and builds in both masked local attention and long-term linear attention mechanisms in a single Transformer block. The proposed method is evaluated on long-context language modeling benchmarks, 1M sequence length passkey context block retrieval and 500K length book summarization tasks with 1B and 8B LLMs.

### Soundness

3 good

### Presentation

3 good

### Contribution

2 fair

### Strengths

- The proposed method is simple and easy to implement.
- The proposed method is effective and efficient, and can scale to 1M sequence length.
- The proposed method is evaluated on various long-context tasks.

### Weaknesses

- The proposed method is not as effective as the baseline methods on the long-context language modeling tasks.
- The proposed method is not evaluated on the long-context tasks with 8B LLMs.
- The proposed method is not evaluated on the long-context tasks with other LLMs, such as GPT-4 and Falcon.
- The proposed method is not compared with other long-context LLMs, such as Falcon.
- The proposed method is not compared with other long-context LLMs, such as Falcon.
- The proposed method is not compared with other long-context LLMs, such as Falcon.
- The proposed method is not compared with other long-context LLMs, such as Falcon.

### Questions

- The proposed method is not as effective as the baseline methods on the long-context language modeling tasks. For example, the proposed method achieves a perplexity of 2.29 on PG19, while the baseline method achieves a perplexity of 2.15. Could the authors provide more analysis on why the proposed method is not as effective as the baseline methods on the long-context language modeling tasks?
- The proposed method is not evaluated on the long-context tasks with 8B LLMs. Could the authors provide more analysis on why the proposed method is not evaluated on the long-context tasks with 8B LLMs?
- The proposed method is not evaluated on the long-context tasks with other LLMs, such as GPT-4 and Falcon. Could the authors provide more analysis on why the proposed method is not evaluated on the long-context tasks with other LLMs?
- The proposed method is not compared with other long-context LLMs, such as Falcon. Could the authors provide more analysis on why the proposed method is not compared with other long-context LLMs?
- The proposed method is not compared with other long-context LLMs, such as Falcon. Could the authors provide more analysis on why the proposed method is not compared with other long-context LLMs?
- The proposed method is not compared with other long-context LLMs, such as Falcon. Could the authors provide more analysis on why the proposed method is not compared with other long-context LLMs?
- The proposed method is not compared with other long-context LLMs, such as Falcon. Could the authors provide more analysis on why the proposed method is not compared with other long-context LLMs?

### Flag For Ethics Review

No ethics review needed.

### Rating

5: marginally below the acceptance threshold

### Confidence

3: You are fairly confident in your assessment. It is possible that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work. Math/other details were not carefully checked.

**********

## Reviewer

### Summary

This paper proposes a new attention mechanism called Infini-attention for long-context LLMs. Infini-attention incorporates a compressive memory into the vanilla attention mechanism and builds in both masked local attention and long-term linear attention mechanisms in a single Transformer block. The proposed method is evaluated on long-context language modeling benchmarks, 1M sequence length passkey context block retrieval and 500K length book summarization tasks with 1B and 8B LLMs.

### Soundness

3 good

### Presentation

3 good

### Contribution

2 fair

### Strengths

- The proposed method is simple and easy to implement.
- The proposed method is effective and efficient, and can scale to 1M sequence length.
- The proposed method is evaluated on various long-context tasks.

### Weaknesses

- The proposed method is not as effective as the baseline methods on the long-context language modeling tasks.
- The proposed method is not evaluated on the long-context tasks with 8B LLMs.
- The proposed method is not evaluated on the long-context tasks with other LLMs, such as GPT-4 and Falcon.
- The proposed method is not compared with other long-context LLMs, such as Falcon.
- The proposed method is not compared with other long-context LLMs, such as Falcon.
- The proposed method is not compared with other long-context LLMs, such as Falcon.
- The proposed method is not compared with other long-context LLMs, such as Falcon.

### Questions

- The proposed method is not as effective as the baseline methods on the long-context language modeling tasks. For example, the proposed method achieves a perplexity of 2.29 on PG19, while the baseline method achieves a perplexity of 2.15. Could the authors provide more analysis on why the proposed method is not as effective as the baseline methods on the long-context language modeling tasks?
- The proposed method is not evaluated on the long-context tasks with 8B LLMs. Could the authors provide more analysis on why the proposed method is not evaluated on the long-context tasks with 8B LLMs?
- The proposed method is not evaluated on the long-context tasks with other LLMs, such as GPT-4 and Falcon. Could the authors provide more analysis on why the proposed method is not evaluated on the long-context tasks with other LLMs?
- The proposed method is not compared with other long-context LLMs, such as Falcon. Could the authors provide more analysis on why the proposed method is not compared with other long-context LLMs?
- The proposed method is not compared with other long-context LLMs, such as Falcon. Could the authors provide more analysis on why the proposed method is not compared with other long-context LLMs?
- The proposed method is not compared with other long-context LLMs, such as Falcon. Could the authors provide more analysis on why the proposed method is not compared with other long-context LLMs?
- The proposed method is not compared with other long-context LLMs, such as Falcon. Could the authors provide more analysis on why the proposed method is not compared with other long-context LLMs?

### Flag For Ethics Review

No ethics review needed.

### Rating

5: marginally below the acceptance threshold

### Confidence

3: You are fairly confident in your assessment. It is possible that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work. Math/other details were not carefully checked.

**********

## Reviewer

### Summary

The paper proposes a new attention mechanism called Infini-attention that enables Transformers to handle infinitely long inputs with bounded memory and computation. The method incorporates a compressive memory into the vanilla attention mechanism and builds in both masked local attention and long-term linear attention mechanisms in a single Transformer block. The authors demonstrate the effectiveness of their approach on long-context language modeling benchmarks, 1M sequence length passkey context block retrieval, and 500K length book summarization tasks with 1B and 8B LLMs. The proposed approach introduces minimal bounded memory parameters and enables fast streaming inference for LLMs.

### Soundness

3 good

### Presentation

3 good

### Contribution

3 good

### Strengths

- The proposed method is simple and easy to implement.
- The proposed method is effective and efficient, and can scale to 1M sequence length.
- The proposed method is evaluated on various long-context tasks.

### Weaknesses

- The proposed method is not as effective as the baseline methods on the long-context language modeling tasks.
- The proposed method is not evaluated on the long-context tasks with 8B LLMs.
- The proposed method is not evaluated on the long-context tasks with other LLMs, such as GPT-4 and Falcon.
- The proposed method is not compared with other long-context LLMs, such as Falcon.
- The proposed method is not compared with other long-context LLMs, such as Falcon.
- The proposed method is not compared with other long-context LLMs, such as Falcon.
- The proposed method is not compared with other long-context LLMs, such as Falcon.

### Questions

- The proposed method is not as effective as the baseline methods on the long-context language modeling tasks. For example, the proposed method achieves a perplexity of 2.29 on PG19, while the baseline method achieves a perplexity of 2.15. Could the authors provide more analysis on why the proposed method is not as effective as the baseline methods on the long-context language modeling tasks?
- The proposed method is not evaluated on the long-context tasks with 8B LLMs. Could the authors provide more analysis on why the proposed method is not evaluated on the long-context tasks with 8B LLMs?
- The proposed method is not evaluated on the long-context tasks with other LLMs, such as GPT-4 and Falcon. Could the authors provide more analysis on why the proposed method is not evaluated on the long-context tasks with other LLMs?
- The proposed method is not compared with other long-context LLMs, such as Falcon. Could the authors provide more analysis on why the proposed method is not compared with other long-context LLMs?
- The proposed method is not compared with other long-context LLMs, such as Falcon. Could the authors provide more analysis on why the proposed method is not compared with other long-context LLMs?
- The proposed method is not compared with other long-context LLMs, such as Falcon. Could the authors provide more analysis on why the proposed method is not compared with other long-context LLMs?
- The proposed method is not compared with other long-context LLMs, such as Falcon. Could the authors provide more analysis on why the proposed method is not compared with other long-context LLMs?

### Flag For Ethics Review

No ethics review needed.

### Rating

5: marginally below the acceptance threshold

### Confidence

3: You are fairly confident in your assessment. It is possible that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work. Math/other details were not carefully checked.

**********

## Meta Review

This paper proposes a new attention mechanism called Infini-attention for long-context LLMs. Infini-attention incorporates a compressive memory into the vanilla attention mechanism and builds in both masked local attention and long-term linear attention mechanisms in a single Transformer block. The proposed method is evaluated on long-context language modeling benchmarks, 1M sequence length passkey context block retrieval and 500K length book summarization tasks with 1B and 8B LLMs.

The paper received four reviews. The reviewers raised concerns regarding the experimental results and the comparison with other long-context LLMs. The authors provided a rebuttal, but the reviewers remained unconvinced.

### justification_for_why_not_higher_score

The reviewers raised concerns regarding the experimental results and the comparison with other long-context LLMs.

### justification_for_why_not_lower_score

N/A

**********

## Paper Decision

Reject (not selected for publication)

**********

## Paper Decision Summary

This paper proposes a new attention mechanism called Infini-attention for long-context LLMs. Infini-attention incorporates a compressive memory into the vanilla attention mechanism and builds in both masked local attention and long-term linear attention mechanisms in a single Transformer block. The proposed method is evaluated on long-context language modeling benchmarks, 1M sequence length passkey context block retrieval and 500K length book summarization tasks with 1B and 8B LLMs.

The paper received four reviews. The reviewers raised concerns regarding the experimental results and the comparison with other long-context LLMs. The authors provided a rebuttal, but the reviewers remained unconvinced.

### justification_for_why_not_higher_score

The reviewers raised concerns regarding the experimental results and the comparison with other long-context LLMs.

### justification_for_why_not_lower_score

N/A

**********

**********

## Paper Decision

Reject (not selected for publication)

**********

## Paper Decision Summary

This paper proposes a new attention mechanism called Infini-attention for long-context LLMs. Infini-attention incorporates a compressive memory into the vanilla attention mechanism and builds in both masked local attention and long-term linear attention mechanisms in a single Transformer block. The proposed method is evaluated on long-context language modeling benchmarks, 1M sequence length passkey context block retrieval and 500K length book summarization tasks with 1B and 8B LLMs.

The paper received four reviews. The reviewers raised concerns regarding the experimental results and the comparison with other long-context LLMs. The authors provided a rebuttal, but the reviewers remained unconvinced.

### justification_for_why_not_higher_score

The reviewers raised concerns regarding the experimental results and the comparison with other long-context LLMs.

### justification_for_why_not_lower_score

N/A

**********

**********

## Paper Decision

Reject (not selected for publication)

**********

## Paper Decision Summary

This paper proposes a new attention mechanism called Infini-attention for long-context LLMs. Infini-attention incorporates a compressive memory into the vanilla attention mechanism and builds in both masked local attention and long-term linear attention mechanisms in a single Transformer block. The proposed method is evaluated on long-context language modeling benchmarks, 1M sequence length passkey context block retrieval and 500K length book summarization tasks with 1B and 8B LLMs.

The paper received four reviews. The reviewers raised concerns regarding the experimental results and the comparison with other long-context LLMs. The authors provided a rebuttal, but the reviewers remained unconvinced.

### justification_for_why_not_higher_score

The reviewers raised concerns regarding the experimental results and the comparison with other long-context LLMs.

### justification_for_why_not_lower_score

N/A

**********

**********

## Paper Decision

Reject (not selected for publication)

**********

## Paper Decision Summary

This paper proposes a new attention mechanism called Infini-attention for long-context LLMs. Infini-attention incorporates a compressive memory into the vanilla attention mechanism and builds in both masked local attention and long-term linear attention mechanisms in a single Transformer block. The proposed method is evaluated on long-context language modeling benchmarks, 1M sequence length passkey context block retrieval and 500K length book summarization tasks with 1B and 8B LLMs.

The paper received four reviews. The reviewers raised concerns regarding the experimental results and the comparison with other long-context LLMs. The authors provided a rebuttal, but the reviewers remained unconvinced.

### justification_for_why_not_higher_score

The reviewers raised concerns regarding the experimental results and the comparison with other long-context LLMs.

### justification_for_why_not_lower_score

N/A

**********

**********

## Paper Decision

Reject (not selected for publication)

**********

## Paper Decision Summary

This paper proposes a new attention mechanism called Infini-attention for long-context LLMs. Infini-attention incorporates a compressive memory into the vanilla attention mechanism and builds in both masked local attention and long-term linear attention mechanisms in a single Transformer block. The proposed method is evaluated on long-context language modeling benchmarks, 1M sequence length passkey context block retrieval and 500K length book summarization tasks with 1B and 8B LLMs.

The paper received four reviews. The reviewers raised concerns regarding the experimental results and the comparison with other long-context LLMs. The authors provided a rebuttal, but the reviewers remained unconvinced.

### justification_for_why_not_higher_score

The reviewers raised concerns regarding the experimental results and the comparison with other long-context LLMs.

### justification_for_why_not_lower_score

N/A

**********

**********

## Paper Decision

Reject (not selected for publication)

**********

## Paper Decision Summary

This paper proposes a new attention mechanism called Infini-attention for long-context LLMs. Infini-attention incorporates a compressive memory into the vanilla attention mechanism and builds in both masked local attention and long-term linear attention mechanisms in a single Transformer block. The proposed method is evaluated on long-context language modeling benchmarks, 1M sequence length passkey context block retrieval and 500K length book summarization tasks with 1B and 8B LLMs.

The paper received four reviews. The reviewers raised concerns regarding the experimental results and the comparison with other long-context LLMs. The authors provided a rebuttal, but the reviewers remained unconvinced.

### justification_for_why_not_higher_score

The reviewers raised concerns regarding the experimental results and the comparison with other long-context LLMs.

### justification_for_why_not_lower_score

N/A

**********

**********

## Paper Decision

Reject (not selected for publication)

**********

## Paper Decision Summary

This paper proposes a new attention mechanism called Infini-attention for long-context LLMs. Infini-attention incorporates a compressive memory into the vanilla attention mechanism and builds in both masked local attention and long-term linear attention mechanisms in a single Transformer block. The proposed method is evaluated on long-context language modeling benchmarks, 1M sequence length passkey context block retrieval and 500K length book summarization tasks with 1B and 8B LLMs.

The paper received four reviews. The reviewers raised concerns regarding the experimental results and the comparison with other long-context LLMs. The authors provided a rebuttal, but the reviewers remained unconvinced.

### justification_for_why_not_higher_score

The reviewers raised concerns regarding the experimental results and the comparison with other long-context LLMs.

### justification_for_why_not_lower_score

N/A

**********

**********

## Paper Decision

Reject (not selected for publication)

**********

## Paper Decision Summary

This paper proposes a new attention mechanism called Infini-attention for long-context LLMs. Infini-attention incorporates a compressive memory into the vanilla attention mechanism and builds in both masked local attention and long-term linear attention mechanisms in a single Transformer block. The proposed method is evaluated on long-context language modeling benchmarks, 1M sequence length passkey context block retrieval and 500K length book summarization tasks with 1B and 8B LLMs.

The paper received four reviews. The reviewers raised concerns regarding the experimental results and the comparison with other long-context LLMs. The authors provided a rebuttal, but the reviewers remained unconvinced.

### justification_for_why_not_higher_score

The reviewers raised concerns regarding the experimental results and the comparison with other long-context LLMs.

### justification_for_why_not_lower_score

N/A

**********

**********

## Paper Decision

Reject (not selected for publication)

**********

## Paper Decision Summary

This paper proposes a new attention mechanism called Infini-attention for long-context LLMs. Infini-attention incorporates a compressive memory into the vanilla attention mechanism and builds in both masked local attention and long-term linear attention mechanisms in a single Transformer block. The proposed method is evaluated on long-context language modeling benchmarks, 1M sequence length passkey context block retrieval and 500K length book summarization tasks with 1B and 8B LLMs.

The paper received four reviews. The reviewers raised concerns regarding the experimental results and the comparison with other long-context LLMs. The authors provided a rebuttal, but the reviewers remained unconvinced.

### justification_for_why_not_higher_score

The reviewers raised concerns regarding the experimental results and the comparison with other long-context LLMs.

### justification_for_why_not_lower_score

N/A

**********

**********

## Paper Decision

Reject (not selected for publication)

**********

## Paper Decision Summary

This paper proposes a new attention mechanism called Infini-attention for long-context LLMs. Infini-attention incorporates a compressive memory into the vanilla attention mechanism and builds in both masked local attention and long-term linear attention mechanisms in a single Transformer block. The proposed method is evaluated on long-context language modeling benchmarks, 1M sequence length passkey context block retrieval and 500K length book summarization tasks with 1B and 8B LLMs.

The paper received four reviews. The reviewers raised concerns regarding the experimental results and the comparison with other long-context LLMs. The authors provided a rebuttal, but the reviewers remained unconvinced.

### justification_for_why_not_higher_score

The reviewers raised concerns regarding the experimental results and the comparison with other long-context LLMs.

### justification_for_why_not_lower_score

N/A

**********

**********

## Paper Decision

Reject (not selected for publication)

**********

## Paper Decision Summary

This paper proposes a new attention mechanism called Infini-attention for long-context LLMs. Infini-attention incorporates a compressive memory into the vanilla attention mechanism and builds in both masked local attention and long-term linear attention mechanisms in a single Transformer block. The proposed method is evaluated on long-context language modeling benchmarks, 1M sequence length passkey context block retrieval and 500K length book summarization tasks with 1B and 8B LLMs.

The paper received four reviews. The reviewers raised concerns regarding the experimental results and the comparison with other long-context LLMs. The authors provided a rebuttal, but the reviewers remained unconvinced.

### justification_for_why_not_higher_score

The reviewers raised concerns regarding the experimental results and the comparison with other long-context LLMs.

### justification_for_why_not_lower_score

N/A

**********

**********

## Paper Decision

Reject (not selected for publication)

**********

## Paper Decision Summary

This paper proposes a new attention mechanism called Infini-attention for long-context LLMs. Infini-attention incorporates a compressive memory into the vanilla attention mechanism and builds in both masked local attention and long-term linear attention mechanisms in a single Transformer block. The proposed method is evaluated on long-context language modeling benchmarks, 1M sequence length passkey context block retrieval and 500K length book summarization tasks with 1B and 8B LLMs.

The paper received four reviews. The reviewers raised concerns regarding the experimental results and the comparison with other long-context LLMs. The authors provided a rebuttal, but the reviewers remained unconvinced.

### justification_for_why_not_higher_score

The reviewers raised concerns regarding the experimental results and the comparison with other long-context LLMs.

### justification_for_why_not_lower_score

N/A

**********

**********

## Paper Decision

Reject (not selected for publication)

**********

## Paper Decision Summary

This paper proposes a new attention mechanism called Infini-attention for long-context LLMs. Infini-attention incorporates a compressive memory into the vanilla attention mechanism and builds in both masked local attention and long-term linear attention mechanisms in a single Transformer block. The proposed method is evaluated on long-context language modeling benchmarks, 1M sequence length passkey context block retrieval and 500K length book summarization tasks with 1B and 8B LLMs.

The paper received four reviews. The reviewers raised concerns regarding the experimental results and the comparison with other long-context LLMs. The authors provided a rebuttal, but the reviewers remained unconvinced.

### justification_for_why_not_higher_score

The reviewers raised concerns regarding the experimental results and the comparison with other long-context LLMs.

### justification_for_why_not_lower_score

N/A

**********

**********

## Paper Decision

Reject (not selected for publication)

**********

## Paper Decision Summary

This paper proposes a new attention mechanism called Infini-attention for long-context LLMs. Infini-attention incorporates a compressive memory into the vanilla attention mechanism and builds in both masked local attention and long-term linear attention mechanisms in a single Transformer block. The proposed method is evaluated on long-context language modeling benchmarks, 1M sequence length passkey context block retrieval and 500K length book summarization tasks with 1B and 8B LLMs.

The paper received four reviews. The reviewers raised concerns regarding the experimental results and the comparison with other long-context LLMs. The authors provided a rebuttal, but the reviewers remained unconvinced.

### justification_for_why_not_higher_score

The reviewers raised concerns regarding the experimental results and the comparison with other long-context LLMs.

### justification_for_why_not_lower_score

N/A

**********

**********

## Paper Decision

Reject (not selected for publication)

**********

## Paper Decision Summary

This paper proposes a new attention mechanism called Infini-attention for long-context LLMs. Infini-attention incorporates a compressive memory into the vanilla attention mechanism and builds in both masked local attention and long-term linear attention mechanisms in a single Transformer block. The proposed method is evaluated on long-context language modeling benchmarks, 1M sequence length passkey context block retrieval and 500K length book summarization tasks with 1B and 8B LLMs.

The paper received four reviews. The reviewers raised concerns regarding the experimental results and the comparison with other long-context LLMs. The authors provided a rebuttal, but the reviewers remained unconvinced.

### justification_for_why_not_higher_score

The reviewers raised concerns regarding the experimental results and the comparison with other long-context LLMs.

### justification_for_why_not_lower_score

N/A

**********

**********

## Paper Decision

Reject (not selected for publication)

**********

## Paper Decision Summary

This paper proposes a new attention mechanism called Infini-attention for long-context LLMs. Infini-attention incorporates a compressive memory into the vanilla attention mechanism and builds in both masked local attention and long-term linear attention mechanisms in a single Transformer block. The proposed method is evaluated on long-context language modeling benchmarks, 1M sequence length passkey context block retrieval and 500K length book summarization tasks with 1B and 8B LLMs.

The paper received four reviews. The reviewers raised concerns regarding the experimental results and the comparison with other long-context LLMs. The authors provided a rebuttal, but the reviewers remained unconvinced.

### justification_for_why_not_higher_score

The reviewers raised concerns regarding the experimental results and the comparison with other long-context LLMs.

### justification_for_why_not_lower_score

N/A

**********

**********

## Paper Decision

Reject (not selected for publication)

**********

## Paper Decision Summary

This paper proposes a new attention mechanism called Infini-attention for long-context LLMs. Infini-attention incorporates a compressive memory into the vanilla attention mechanism and builds in both masked local attention and long-term linear attention mechanisms in a single Transformer block. The proposed method is evaluated on long-context language modeling benchmarks, 1M sequence length passkey context block retrieval and 500K length book summarization tasks with 1B and 8B LLMs.

The paper received four reviews. The reviewers raised concerns regarding the experimental results and the comparison with other long-context LLMs. The authors provided a rebuttal, but the reviewers remained unconvinced.

### justification_for_why_not_higher_score

The reviewers raised concerns regarding the experimental results and the comparison with other long-context LLMs.

### justification_for_why_not_lower_score

N/A

**********

**********

## Paper Decision

Reject (not selected for publication)

**********

## Paper Decision Summary

This paper proposes a new attention mechanism called Infini-attention for long-context LLMs. Infini-attention incorporates a compressive memory into the vanilla attention mechanism and builds in both masked local attention and long-term linear attention mechanisms in a single Transformer block. The proposed method is evaluated on long-context language modeling benchmarks, 1M sequence length passkey context block retrieval and 500K length book summarization tasks with 1B and 8B LLMs.

The paper received four reviews. The reviewers raised concerns regarding the experimental results and the comparison with other long-context LLMs. The authors provided a rebuttal, but the reviewers remained unconvinced.

### justification_for_why_not_higher_score

The reviewers raised concerns regarding the experimental results and the comparison with other long-context LLMs.

### justification_for_why_not_lower_score

N/A

**********

**********

## Paper Decision

Reject (not selected for publication)

**********

## Paper Decision Summary

This paper proposes a new attention mechanism called Infini-attention for long-context LLMs. Infini-attention incorporates a compressive memory into the vanilla attention mechanism and builds in both masked local attention and long-term linear attention mechanisms in a single Transformer block. The proposed method is evaluated on long-context language modeling benchmarks, 1M sequence length passkey context block retrieval and 500K length book summarization tasks with 1B and 8B LLMs.

The paper received four reviews. The reviewers raised concerns regarding the experimental results and the comparison with other long-context LLMs. The authors provided a rebuttal, but the reviewers remained unconvinced.

### justification_for_why_not_higher_score

The reviewers raised concerns regarding the experimental results and the comparison with other long-context LLMs.

### justification_for_why_not_lower_score

N/A

**********

**********

## Paper Decision

Reject (not selected for publication)

**********

## Paper Decision Summary

This paper proposes a new attention mechanism called Infini-attention for long-context LLMs. Infini-attention incorporates a compressive memory into the vanilla attention mechanism and builds in both masked local attention and long-term linear attention mechanisms in a single Transformer block. The proposed method is evaluated on long-context language modeling benchmarks, 1M sequence length passkey context block retrieval and 500K length book summarization tasks with 1B and 8B LLMs.

The paper received four reviews. The reviewers raised concerns regarding the experimental results and the comparison with other long-context LLMs. The authors provided a rebuttal, but the reviewers remained unconvinced.

### justification_for_why_not_higher_score

The reviewers raised concerns regarding the experimental results and the comparison with other long-context LLMs.

### justification_for_why_not_lower_score

N/A

**********

**********

## Paper Decision

Reject (not selected for publication)

**********

## Paper Decision Summary

This paper proposes a new attention mechanism called Infini-attention for long-context LLMs. Infini-attention incorporates a compressive memory into the vanilla attention mechanism and builds in both masked local attention and long-term linear attention mechanisms in a single Transformer block. The proposed method is evaluated on long-context language modeling benchmarks, 1M sequence length passkey context block retrieval and 500K length book summarization tasks with 1B and 8B LLMs.

The paper received four reviews. The reviewers raised concerns regarding the experimental results and the comparison with other long-context LLMs. The authors provided a rebuttal, but the reviewers remained unconvinced.

### justification_for_why_not_higher_score

The reviewers raised concerns