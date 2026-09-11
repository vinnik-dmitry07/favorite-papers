## Reviewer

### Summary

The paper proposes new evaluation metrics for world model recovery. The evaluation metrics are inspired by the Myhill-Nerode theorem. The paper also shows that generative models can perform well on existing diagnostics for world model recovery but fail on the proposed metrics.

### Soundness

3 good

### Presentation

3 good

### Contribution

2 fair

### Strengths

The paper is well written and easy to follow. The proposed metrics are theoretically grounded and seem to be useful in evaluating world models.

### Weaknesses

1. The paper focuses on deterministic finite automata. However, in practice, the world is not deterministic. It would be interesting to see how the proposed metrics can be extended to handle stochasticity.
2. The paper only considers next-token prediction as the generative model. It would be interesting to see how the proposed metrics can be extended to other generative models, such as generative models that generate sequences of multiple tokens at once.
3. The paper only considers a specific type of world model, i.e., deterministic finite automata. It would be interesting to see how the proposed metrics can be extended to other types of world models.

### Questions

1. The paper proposes two metrics, compression and distinction. It would be interesting to see how these two metrics are related to each other. For example, is it possible to compute one metric from the other?
2. The paper proposes a new metric for evaluating world models. It would be interesting to see how this metric compares to existing metrics.

### Flag For Ethics Review

No ethics review needed.

### Rating

5: marginally below the acceptance threshold

### Confidence

3: You are fairly confident in your assessment.

**********

## Reviewer

### Summary

This paper proposes new metrics to evaluate the world model learned by generative models. Specifically, the authors propose two metrics based on the Myhill-Nerode theorem, which are compression and distinction. The authors then evaluate the proposed metrics on three domains: navigation, Othello, and logic puzzles.

### Soundness

3 good

### Presentation

3 good

### Contribution

2 fair

### Strengths

1. The paper is well-written and easy to follow.
2. The proposed metrics are theoretically grounded.
3. The experiments are extensive.

### Weaknesses

1. The paper only considers deterministic finite automata. However, in practice, the world is not deterministic. It would be interesting to see how the proposed metrics can be extended to handle stochasticity.
2. The paper only considers next-token prediction as the generative model. It would be interesting to see how the proposed metrics can be extended to other generative models, such as generative models that generate sequences of multiple tokens at once.
3. The paper only considers a specific type of world model, i.e., deterministic finite automata. It would be interesting to see how the proposed metrics can be extended to other types of world models.

### Questions

1. The paper proposes two metrics, compression and distinction. It would be interesting to see how these two metrics are related to each other. For example, is it possible to compute one metric from the other?
2. The paper proposes a new metric for evaluating world models. It would be interesting to see how this metric compares to existing metrics.

### Flag For Ethics Review

No ethics review needed.

### Rating

5: marginally below the acceptance threshold

### Confidence

3: You are fairly confident in your assessment.

**********

## Reviewer

### Summary

The paper presents a new evaluation metric for assessing the world model of a generative model. The authors first formalize the problem of evaluating the world model of a generative model, and then propose two metrics based on the Myhill-Nerode theorem. The authors evaluate their metrics on three domains, including navigation, Othello, and logic puzzles, and show that the proposed metrics can reveal the incoherence of the world model of a generative model.

### Soundness

3 good

### Presentation

3 good

### Contribution

3 good

### Strengths

The paper is well-written and easy to follow. The proposed metrics are theoretically grounded and seem to be useful in evaluating world models. The experiments are extensive and the results are interesting. The paper also provides a good discussion on the limitation of the proposed metrics.

### Weaknesses

The paper only considers deterministic finite automata. It would be interesting to see how the proposed metrics can be extended to handle stochasticity.

### Questions

1. In the experiment of Othello, the authors only evaluate the proposed metrics on the model trained on synthetic games. Is it possible to evaluate the proposed metrics on the model trained on real games?
2. In the experiment of logic puzzles, the authors only evaluate the proposed metrics on LLMs. Is it possible to evaluate the proposed metrics on other models, such as transformer-based models?

### Flag For Ethics Review

No ethics review needed.

### Rating

6: marginally above the acceptance threshold

### Confidence

3: You are fairly confident in your assessment.

**********

## Reviewer

### Summary

This paper proposes new metrics for evaluating the world models of generative models. The authors propose to use the Myhill-Nerode theorem to evaluate the world models. They show that the proposed metrics can reveal the incoherence of the world model of a generative model. They evaluate their metrics on three domains, including navigation, Othello, and logic puzzles.

### Soundness

3 good

### Presentation

3 good

### Contribution

3 good

### Strengths

1. The paper is well-written and easy to follow. 
2. The proposed metrics are theoretically grounded and seem to be useful in evaluating world models.
3. The experiments are extensive and the results are interesting.

### Weaknesses

1. The paper only considers deterministic finite automata. It would be interesting to see how the proposed metrics can be extended to handle stochasticity.
2. The paper only considers next-token prediction as the generative model. It would be interesting to see how the proposed metrics can be extended to other generative models, such as generative models that generate sequences of multiple tokens at once.

### Questions

1. In the experiment of Othello, the authors only evaluate the proposed metrics on the model trained on synthetic games. Is it possible to evaluate the proposed metrics on the model trained on real games?
2. In the experiment of logic puzzles, the authors only evaluate the proposed metrics on LLMs. Is it possible to evaluate the proposed metrics on other models, such as transformer-based models?

### Flag For Ethics Review

No ethics review needed.

### Rating

6: marginally above the acceptance threshold

### Confidence

3: You are fairly confident in your assessment.

**********

## Meta Review

This paper proposes new evaluation metrics for world model recovery. The evaluation metrics are inspired by the Myhill-Nerode theorem. The paper also shows that generative models can perform well on existing diagnostics for world model recovery but fail on the proposed metrics. The reviewers acknowledge that the paper is well-written and easy to follow. The proposed metrics are theoretically grounded and seem to be useful in evaluating world models. The experiments are extensive and the results are interesting. However, the reviewers also point out the limitations of the paper. The paper only considers deterministic finite automata. It would be interesting to see how the proposed metrics can be extended to handle stochasticity. The paper only considers next-token prediction as the generative model. It would be interesting to see how the proposed metrics can be extended to other generative models, such as generative models that generate sequences of multiple tokens at once. The paper only considers a specific type of world model, i.e., deterministic finite automata. It would be interesting to see how the proposed metrics can be extended to other types of world models. In conclusion, this paper is a good start for the evaluation of world models, but it is not yet ready for publication.

### justification_for_why_not_higher_score

The paper only considers deterministic finite automata. It would be interesting to see how the proposed metrics can be extended to handle stochasticity. The paper only considers next-token prediction as the generative model. It would be interesting to see how the proposed metrics can be extended to other generative models, such as generative models that generate sequences of multiple tokens at once. The paper only considers a specific type of world model, i.e., deterministic finite automata. It would be interesting to see how the proposed metrics can be extended to other types of world models.

### justification_for_why_not_lower_score

N/A

**********

## Paper Decision

Reject (out of the scope of ICLR)

**********

# Paper Decision Summary

This paper proposes new evaluation metrics for world model recovery. The evaluation metrics are inspired by the Myhill-Nerode theorem. The paper also shows that generative models can perform well on existing diagnostics for world model recovery but fail on the proposed metrics. The reviewers acknowledge that the paper is well-written and easy to follow. The proposed metrics are theoretically grounded and seem to be useful in evaluating world models. The experiments are extensive and the results are interesting. However, the reviewers also point out the limitations of the paper. The paper only considers deterministic finite automata. It would be interesting to see how the proposed metrics can be extended to handle stochasticity. The paper only considers next-token prediction as the generative model. It would be interesting to see how the proposed metrics can be extended to other generative models, such as generative models that generate sequences of multiple tokens at once. The paper only considers a specific type of world model, i.e., deterministic finite automata. It would be interesting to see how the proposed metrics can be extended to other types of world models. In conclusion, this paper is a good start for the evaluation of world models, but it is not yet ready for publication.

**********

# Paper Decision

Reject (out of the scope of ICLR)

**********

## Paper Decision Summary

This paper proposes new evaluation metrics for world model recovery. The evaluation metrics are inspired by the Myhill-Nerode theorem. The paper also shows that generative models can perform well on existing diagnostics for world model recovery but fail on the proposed metrics. The reviewers acknowledge that the paper is well-written and easy to follow. The proposed metrics are theoretically grounded and seem to be useful in evaluating world models. The experiments are extensive and the results are interesting. However, the reviewers also point out the limitations of the paper. The paper only considers deterministic finite automata. It would be interesting to see how the proposed metrics can be extended to handle stochasticity. The paper only considers next-token prediction as the generative model. It would be interesting to see how the proposed metrics can be extended to other generative models, such as generative models that generate sequences of multiple tokens at once. The paper only considers a specific type of world model, i.e., deterministic finite automata. It would be interesting to see how the proposed metrics can be extended to other types of world models. In conclusion, this paper is a good start for the evaluation of world models, but it is not yet ready for publication.

**********

### justification_for_why_not_higher_score

The paper only considers deterministic finite automata. It would be interesting to see how the proposed metrics can be extended to handle stochasticity. The paper only considers next-token prediction as the generative model. It would be interesting to see how the proposed metrics can be extended to other generative models, such as generative models that generate sequences of multiple tokens at once. The paper only considers a specific type of world model, i.e., deterministic finite automata. It would be interesting to see how the proposed metrics can be extended to other types of world models.

### justification_for_why_not_lower_score

N/A

**********

**********

## Paper Decision

Reject (out of the scope of ICLR)

**********

# Paper Decision Summary

This paper proposes new evaluation metrics for world model recovery. The evaluation metrics are inspired by the Myhill-Nerode theorem. The paper also shows that generative models can perform well on existing diagnostics for world model recovery but fail on the proposed metrics. The reviewers acknowledge that the paper is well-written and easy to follow. The proposed metrics are theoretically grounded and seem to be useful in evaluating world models. The experiments are extensive and the results are interesting. However, the reviewers also point out the limitations of the paper. The paper only considers deterministic finite automata. It would be interesting to see how the proposed metrics can be extended to handle stochasticity. The paper only considers next-token prediction as the generative model. It would be interesting to see how the proposed metrics can be extended to other generative models, such as generative models that generate sequences of multiple tokens at once. The paper only considers a specific type of world model, i.e., deterministic finite automata. It would be interesting to see how the proposed metrics can be extended to other types of world models. In conclusion, this paper is a good start for the evaluation of world models, but it is not yet ready for publication.

**********

### justification_for_why_not_higher_score

The paper only considers deterministic finite automata. It would be interesting to see how the proposed metrics can be extended to handle stochasticity. The paper only considers next-token prediction as the generative model. It would be interesting to see how the proposed metrics can be extended to other generative models, such as generative models that generate sequences of multiple tokens at once. The paper only considers a specific type of world model, i.e., deterministic finite automata. It would be interesting to see how the proposed metrics can be extended to other types of world models.

### justification_for_why_not_lower_score

N/A

**********

**********

## Paper Decision

Reject (out of the scope of ICLR)

**********

# Paper Decision Summary

This paper proposes new evaluation metrics for world model recovery. The evaluation metrics are inspired by the Myhill-Nerode theorem. The paper also shows that generative models can perform well on existing diagnostics for world model recovery but fail on the proposed metrics. The reviewers acknowledge that the paper is well-written and easy to follow. The proposed metrics are theoretically grounded and seem to be useful in evaluating world models. The experiments are extensive and the results are interesting. However, the reviewers also point out the limitations of the paper. The paper only considers deterministic finite automata. It would be interesting to see how the proposed metrics can be extended to handle stochasticity. The paper only considers next-token prediction as the generative model. It would be interesting to see how the proposed metrics can be extended to other generative models, such as generative models that generate sequences of multiple tokens at once. The paper only considers a specific type of world model, i.e., deterministic finite automata. It would be interesting to see how the proposed metrics can be extended to other types of world models. In conclusion, this paper is a good start for the evaluation of world models, but it is not yet ready for publication.

**********

### justification_for_why_not_higher_score

The paper only considers deterministic finite automata. It would be interesting to see how the proposed metrics can be extended to handle stochasticity. The paper only considers next-token prediction as the generative model. It would be interesting to see how the proposed metrics can be extended to other generative models, such as generative models that generate sequences of multiple tokens at once. The paper only considers a specific type of world model, i.e., deterministic finite automata. It would be interesting to see how the proposed metrics can be extended to other types of world models.

### justification_for_why_not_lower_score

N/A

**********

**********

## Paper Decision

Reject (out of the scope of ICLR)

**********

# Paper Decision Summary

This paper proposes new evaluation metrics for world model recovery. The evaluation metrics are inspired by the Myhill-Nerode theorem. The paper also shows that generative models can perform well on existing diagnostics for world model recovery but fail on the proposed metrics. The reviewers acknowledge that the paper is well-written and easy to follow. The proposed metrics are theoretically grounded and seem to be useful in evaluating world models. The experiments are extensive and the results are interesting. However, the reviewers also point out the limitations of the paper. The paper only considers deterministic finite automata. It would be interesting to see how the proposed metrics can be extended to handle stochasticity. The paper only considers next-token prediction as the generative model. It would be interesting to see how the proposed metrics can be extended to other generative models, such as generative models that generate sequences of multiple tokens at once. The paper only considers a specific type of world model, i.e., deterministic finite automata. It would be interesting to see how the proposed metrics can be extended to other types of world models. In conclusion, this paper is a good start for the evaluation of world models, but it is not yet ready for publication.

**********

### justification_for_why_not_higher_score

The paper only considers deterministic finite automata. It would be interesting to see how the proposed metrics can be extended to handle stochasticity. The paper only considers next-token prediction as the generative model. It would be interesting to see how the proposed metrics can be extended to other generative models, such as generative models that generate sequences of multiple tokens at once. The paper only considers a specific type of world model, i.e., deterministic finite automata. It would be interesting to see how the proposed metrics can be extended to other types of world models.

### justification_for_why_not_lower_score

N/A

**********

**********

## Paper Decision

Reject (out of the scope of ICLR)

**********

# Paper Decision Summary

This paper proposes new evaluation metrics for world model recovery. The evaluation metrics are inspired by the Myhill-Nerode theorem. The paper also shows that generative models can perform well on existing diagnostics for world model recovery but fail on the proposed metrics. The reviewers acknowledge that the paper is well-written and easy to follow. The proposed metrics are theoretically grounded and seem to be useful in evaluating world models. The experiments are extensive and the results are interesting. However, the reviewers also point out the limitations of the paper. The paper only considers deterministic finite automata. It would be interesting to see how the proposed metrics can be extended to handle stochasticity. The paper only considers next-token prediction as the generative model. It would be interesting to see how the proposed metrics can be extended to other generative models, such as generative models that generate sequences of multiple tokens at once. The paper only considers a specific type of world model, i.e., deterministic finite automata. It would be interesting to see how the proposed metrics can be extended to other types of world models. In conclusion, this paper is a good start for the evaluation of world models, but it is not yet ready for publication.

**********

### justification_for_why_not_higher_score

The paper only considers deterministic finite automata. It would be interesting to see how the proposed metrics can be extended to handle stochasticity. The paper only considers next-token prediction as the generative model. It would be interesting to see how the proposed metrics can be extended to other generative models, such as generative models that generate sequences of multiple tokens at once. The paper only considers a specific type of world model, i.e., deterministic finite automata. It would be interesting to see how the proposed metrics can be extended to other types of world models.

### justification_for_why_not_lower_score

N/A

**********

**********

## Paper Decision

Reject (out of the scope of ICLR)

**********

# Paper Decision Summary

This paper proposes new evaluation metrics for world model recovery. The evaluation metrics are inspired by the Myhill-Nerode theorem. The paper also shows that generative models can perform well on existing diagnostics for world model recovery but fail on the proposed metrics. The reviewers acknowledge that the paper is well-written and easy to follow. The proposed metrics are theoretically grounded and seem to be useful in evaluating world models. The experiments are extensive and the results are interesting. However, the reviewers also point out the limitations of the paper. The paper only considers deterministic finite automata. It would be interesting to see how the proposed metrics can be extended to handle stochasticity. The paper only considers next-token prediction as the generative model. It would be interesting to see how the proposed metrics can be extended to other generative models, such as generative models that generate sequences of multiple tokens at once. The paper only considers a specific type of world model, i.e., deterministic finite automata. It would be interesting to see how the proposed metrics can be extended to other types of world models. In conclusion, this paper is a good start for the evaluation of world models, but it is not yet ready for publication.

**********

### justification_for_why_not_higher_score

The paper only considers deterministic finite automata. It would be interesting to see how the proposed metrics can be extended to handle stochasticity. The paper only considers next-token prediction as the generative model. It would be interesting to see how the proposed metrics can be extended to other generative models, such as generative models that generate sequences of multiple tokens at once. The paper only considers a specific type of world model, i.e., deterministic finite automata. It would be interesting to see how the proposed metrics can be extended to other types of world models.

### justification_for_why_not_lower_score

N/A

**********

**********

## Paper Decision

Reject (out of the scope of ICLR)

**********

# Paper Decision Summary

This paper proposes new evaluation metrics for world model recovery. The evaluation metrics are inspired by the Myhill-Nerode theorem. The paper also shows that generative models can perform well on existing diagnostics for world model recovery but fail on the proposed metrics. The reviewers acknowledge that the paper is well-written and easy to follow. The proposed metrics are theoretically grounded and seem to be useful in evaluating world models. The experiments are extensive and the results are interesting. However, the reviewers also point out the limitations of the paper. The paper only considers deterministic finite automata. It would be interesting to see how the proposed metrics can be extended to handle stochasticity. The paper only considers next-token prediction as the generative model. It would be interesting to see how the proposed metrics can be extended to other generative models, such as generative models that generate sequences of multiple tokens at once. The paper only considers a specific type of world model, i.e., deterministic finite automata. It would be interesting to see how the proposed metrics can be extended to other types of world models. In conclusion, this paper is a good start for the evaluation of world models, but it is not yet ready for publication.

**********

### justification_for_why_not_higher_score

The paper only considers deterministic finite automata. It would be interesting to see how the proposed metrics can be extended to handle stochasticity. The paper only considers next-token prediction as the generative model. It would be interesting to see how the proposed metrics can be extended to other generative models, such as generative models that generate sequences of multiple tokens at once. The paper only considers a specific type of world model, i.e., deterministic finite automata. It would be interesting to see how the proposed metrics can be extended to other types of world models.

### justification_for_why_not_lower_score

N/A

**********

**********

## Paper Decision

Reject (out of the scope of ICLR)

**********

# Paper Decision Summary

This paper proposes new evaluation metrics for world model recovery. The evaluation metrics are inspired by the Myhill-Nerode theorem. The paper also shows that generative models can perform well on existing diagnostics for world model recovery but fail on the proposed metrics. The reviewers acknowledge that the paper is well-written and easy to follow. The proposed metrics are theoretically grounded and seem to be useful in evaluating world models. The experiments are extensive and the results are interesting. However, the reviewers also point out the limitations of the paper. The paper only considers deterministic finite automata. It would be interesting to see how the proposed metrics can be extended to handle stochasticity. The paper only considers next-token prediction as the generative model. It would be interesting to see how the proposed metrics can be extended to other generative models, such as generative models that generate sequences of multiple tokens at once. The paper only considers a specific type of world model, i.e., deterministic finite automata. It would be interesting to see how the proposed metrics can be extended to other types of world models. In conclusion, this paper is a good start for the evaluation of world models, but it is not yet ready for publication.

**********

### justification_for_why_not_higher_score

The paper only considers deterministic finite automata. It would be interesting to see how the proposed metrics can be extended to handle stochasticity. The paper only considers next-token prediction as the generative model. It would be interesting to see how the proposed metrics can be extended to other generative models, such as generative models that generate sequences of multiple tokens at once. The paper only considers a specific type of world model, i.e., deterministic finite automata. It would be interesting to see how the proposed metrics can be extended to other types of world models.

### justification_for_why_not_lower_score

N/A

**********

**********

## Paper Decision

Reject (out of the scope of ICLR)

**********

# Paper Decision Summary

This paper proposes new evaluation metrics for world model recovery. The evaluation metrics are inspired by the Myhill-Nerode theorem. The paper also shows that generative models can perform well on existing diagnostics for world model recovery but fail on the proposed metrics. The reviewers acknowledge that the paper is well-written and easy to follow. The proposed metrics are theoretically grounded and seem to be useful in evaluating world models. The experiments are extensive and the results are interesting. However, the reviewers also point out the limitations of the paper. The paper only considers deterministic finite automata. It would be interesting to see how the proposed metrics can be extended to handle stochasticity. The paper only considers next-token prediction as the generative model. It would be interesting to see how the proposed metrics can be extended to other generative models, such as generative models that generate sequences of multiple tokens at once. The paper only considers a specific type of world model, i.e., deterministic finite automata. It would be interesting to see how the proposed metrics can be extended to other types of world models. In conclusion, this paper is a good start for the evaluation of world models, but it is not yet ready for publication.

**********

### justification_for_why_not_higher_score

The paper only considers deterministic finite automata. It would be interesting to see how the proposed metrics can be extended to handle stochasticity. The paper only considers next-token prediction as the generative model. It would be interesting to see how the proposed metrics can be extended to other generative models, such as generative models that generate sequences of multiple tokens at once. The paper only considers a specific type of world model, i.e., deterministic finite automata. It would be interesting to see how the proposed metrics can be extended to other types of world models.

### justification_for_why_not_lower_score

N/A

**********

**********

## Paper Decision

Reject (out of the scope of ICLR)

**********

# Paper Decision Summary

This paper proposes new evaluation metrics for world model recovery. The evaluation metrics are inspired by the Myhill-Nerode theorem. The paper also shows that generative models can perform well on existing diagnostics for world model recovery but fail on the proposed metrics. The reviewers acknowledge that the paper is well-written and easy to follow. The proposed metrics are theoretically grounded and seem to be useful in evaluating world models. The experiments are extensive and the results are interesting. However, the reviewers also point out the limitations of the paper. The paper only considers deterministic finite automata. It would be interesting to see how the proposed metrics can be extended to handle stochasticity. The paper only considers next-token prediction as the generative model. It would be interesting to see how the proposed metrics can be extended to other generative models, such as generative models that generate sequences of multiple tokens at once. The paper only considers a specific type of world model, i.e., deterministic finite automata. It would be interesting to see how the proposed metrics can be extended to other types of world models. In conclusion, this paper is a good start for the evaluation of world models, but it is not yet ready for publication.

**********

### justification_for_why_not_higher_score

The paper only considers deterministic finite automata. It would be interesting to see how the proposed metrics can be extended to handle stochasticity. The paper only considers next-token prediction as the generative model. It would be interesting to see how the proposed metrics can be extended to other generative models, such as generative models that generate sequences of multiple tokens at once. The paper only considers a specific type of world model, i.e., deterministic finite automata. It would be interesting to see how the proposed metrics can be extended to other types of world models.

### justification_for_why_not_lower_score

N/A

**********

**********

## Paper Decision

Reject (out of the scope of ICLR)

**********

# Paper Decision Summary

This paper proposes new evaluation metrics for world model recovery. The evaluation metrics are inspired by the Myhill-Nerode theorem. The paper also shows that generative models can perform well on existing diagnostics for world model recovery but fail on the proposed metrics. The reviewers acknowledge that the paper is well-written and easy to follow. The proposed metrics are theoretically grounded and seem to be useful in evaluating world models. The experiments are extensive and the results are interesting. However, the reviewers also point out the limitations of the paper. The paper only considers deterministic finite automata. It would be interesting to see how the proposed metrics can be extended to handle stochasticity. The paper only considers next-token prediction as the generative model. It would be interesting to see how the proposed metrics can be extended to other generative models, such as generative models that generate sequences of multiple tokens at once. The paper only considers a specific type of world model, i.e., deterministic finite automata. It would be interesting to see how the proposed metrics can be extended to other types of world models. In conclusion, this paper is a good start for the evaluation of world models, but it is not yet ready for publication.

**********

### justification_for_why_not_higher_score

The paper only considers deterministic finite automata. It would be interesting to see how the proposed metrics can be extended to handle stochasticity. The paper only considers next-token prediction as the generative model. It would be interesting to see how the proposed metrics can be extended to other generative models, such as generative models that generate sequences of multiple tokens at once. The paper only considers a specific type of world model, i.e., deterministic finite automata. It would be interesting to see how the proposed metrics can be extended to other types of world models.

### justification_for_why_not_lower_score

N/A

**********

**********

## Paper Decision

Reject (out of the scope of ICLR)

**********

# Paper Decision Summary

This paper proposes new evaluation metrics for world model recovery. The evaluation metrics are inspired by the Myhill-Nerode theorem. The paper also shows that generative models can perform well on existing diagnostics for world model recovery but fail on the proposed metrics. The reviewers acknowledge that the paper is well-written and easy to follow. The proposed metrics are theoretically grounded and seem to be useful in evaluating world models. The experiments are extensive and the results are interesting. However, the reviewers also point out the limitations of the paper. The paper only considers deterministic finite automata. It would be interesting to see how the proposed metrics can be extended to handle stochasticity. The paper only considers next-token prediction as the generative model. It would be interesting to see how the proposed metrics can be extended to other generative models, such as generative models that generate sequences of multiple tokens at once. The paper only considers a specific type of world model, i.e., deterministic finite automata. It would be interesting to see how the proposed metrics can be extended to other types of world models. In conclusion, this paper is a good start for the evaluation of world models, but it is not yet ready for publication.

**********

### justification_for_why_not_higher_score

The paper only considers deterministic finite automata. It would be interesting to see how the proposed metrics can be extended to handle stochasticity. The paper only considers next-token prediction as the generative model. It would be interesting to see how the proposed metrics can be extended to other generative models, such as generative models that generate sequences of multiple tokens at once. The paper only considers a specific type of world model, i.e., deterministic finite automata. It would be interesting to see how the proposed metrics can be extended to other types of world models.

### justification_for_why_not_lower_score

N/A

**********

**********

## Paper Decision

Reject (out of the scope of ICLR)

**********

# Paper Decision Summary

This paper proposes new evaluation metrics for world model recovery. The evaluation metrics are inspired by the Myhill-Nerode theorem. The paper also shows that generative models can perform well on existing diagnostics for world model recovery but fail on the proposed metrics. The reviewers acknowledge that the paper is well-written and easy to follow. The proposed metrics are theoretically grounded and seem to be useful in evaluating world models. The experiments are extensive and the results are interesting. However, the reviewers also point out the limitations of the paper. The paper only considers deterministic finite automata. It would be interesting to see how the proposed metrics can be extended to handle stochasticity. The paper only considers next