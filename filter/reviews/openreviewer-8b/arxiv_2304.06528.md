# Review

## Summary
This paper shows that power-seeking behavior is likely to be learned by an RL agent, even when the agent is trained on a different reward function.  The paper formalizes the notion of a training-compatible goal set, which is the set of all reward functions that are consistent with the agent's training data.  The paper shows that for a randomly chosen goal from this set, the agent will tend to avoid a shutdown option.  This is because the shutdown option can be "retargeted" to a recurrent state, which provides higher reward.

## Soundness
3

## Presentation
3

## Contribution
3

## Strengths
The paper provides a formalization of the notion of a training-compatible goal set, which is useful for analyzing the behavior of trained agents.  The paper shows that power-seeking behavior is likely to be learned by an RL agent, even when the agent is trained on a different reward function.  This is an important result, because it suggests that power-seeking behavior may be difficult to avoid, even with careful reward engineering.

## Weaknesses
The paper makes several simplifying assumptions, such as the agent learning a goal from the training-compatible goal set, and the agent being trained on a large distribution of goals.  These assumptions may not hold in practice, and it would be interesting to see future work that relaxes these assumptions and investigates how likely they are to hold.

The paper focuses on a specific setting where the agent faces a choice between shutdown and non-shutdown actions.  It would be interesting to see future work that extends the analysis to more general settings.

## Questions
The paper assumes that the agent learns a goal from the training-compatible goal set.  How likely is this to happen in practice?  Can we encourage this to happen?

The paper assumes that the agent is trained on a large distribution of goals.  How sensitive is the result to the distribution of goals?  Would the result hold even if the agent is trained on a small number of goals?

The paper focuses on a specific setting where the agent faces a choice between shutdown and non-shutdown actions.  Can the result be extended to more general settings?

## Flag For Ethics Review
No ethics review needed.

## Details Of Ethics Concerns


## Rating
6

## Confidence
4