# Review

## Summary
This paper proposes a new context engineering method that optimizes context as code. The method uses two agents, one at meta-level to generate a new "skill" (a folder containing various context engineering artifacts such as code, templates, etc.) and one at base-level to execute the generated skill and update the context. The method is evaluated on 5 tasks and shows improvement over previous context engineering methods.

## Soundness
3

## Presentation
3

## Contribution
3

## Strengths
- The method is novel and interesting. It is the first to optimize context as code and the use of two-level agents is also interesting.
- The method is well-motivated and the paper is well-written.
- The method shows improvement over previous methods.

## Weaknesses
- The method requires a more complex setup than previous methods (two agents, one for meta-level and one for base-level) and thus may be harder to use in practice.
- The method is only evaluated on 5 tasks. Evaluating on more tasks would make the results more convincing.

## Questions
- How does the method compare to other methods in terms of computational cost?
- How does the method perform on more tasks?

## Flag For Ethics Review
No ethics review needed.

## Details Of Ethics Concerns


## Rating
6

## Confidence
4