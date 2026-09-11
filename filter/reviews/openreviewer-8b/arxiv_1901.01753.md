# Review

## Summary
This paper introduces the Paired Open-Ended Trailblazer (POET) algorithm, which generates its own learning challenges and solves them. POET creates diverse and increasingly complex environments and optimizes agents to navigate them. Tested on a 2-D bipedal-walking obstacle course, POET outperforms direct optimization and curriculum-based methods by producing novel solutions and transferring knowledge between environments. The results show that POET's open-ended approach can autonomously generate and solve a wide range of environmental challenges, demonstrating its potential for self-generated curricula and continuous learning improvement.

## Soundness
3

## Presentation
3

## Contribution
3

## Strengths
- The paper is well-written and easy to follow.
- The idea of open-ended learning is interesting and important for the field.

## Weaknesses
- My main concern is the scalability of the proposed method. It seems that the method is only tested in a simple 2-D bipedal-walking obstacle-course domain, which is not convincing enough to show the effectiveness of the proposed method. I would expect the authors to test the proposed method in more complex environments, such as 3-D environments.
- The compared baselines are not strong enough. The authors only compare the proposed method with ES, which is not a strong baseline for the considered task. I would expect the authors to compare the proposed method with more strong baselines, such as PPO and DDPG.
- The proposed method is not novel enough. The proposed method seems to be a simple combination of existing methods.

## Questions
Please refer to the weaknesses.

## Flag For Ethics Review
No ethics review needed.

## Details Of Ethics Concerns


## Rating
5

## Confidence
4