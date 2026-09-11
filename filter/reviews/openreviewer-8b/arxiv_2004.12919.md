# Review

## Summary
The paper proposes a new exploration method for reinforcement learning algorithms. The method is based on explicitly remembering states that were previously visited and exploring from those states. The paper shows that the proposed method solves several hard-exploration tasks in the Atari domain and a robotics domain.

## Soundness
3

## Presentation
3

## Contribution
3

## Strengths
- The paper is well written and easy to follow.
- The proposed method is novel and interesting.
- The experiments show that the proposed method can solve several hard-exploration tasks.

## Weaknesses
- The proposed method relies on the availability of a simulator. While the paper shows that it is possible to implement a version of the algorithm that does not rely on a simulator, it is unclear how well that version of the algorithm would perform.
- The proposed method is only evaluated on a limited number of domains.

## Questions
- How would the version of the algorithm that does not rely on a simulator perform on the robotics domain?
- How would the proposed method perform on other hard-exploration tasks such as Procgen (https://procgen.dev/)?

## Flag For Ethics Review
No ethics review needed.

## Details Of Ethics Concerns


## Rating
8

## Confidence
4