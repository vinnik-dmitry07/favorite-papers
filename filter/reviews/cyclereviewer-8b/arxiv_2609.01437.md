## Reviewer

### Summary

This paper introduces a new benchmark for evaluating the ability of LLMs to develop their own agent harness. The benchmark consists of two stages: creation and evolution. In the creation stage, the LLM starts from a minimal seed and a small number of cases, then builds a complete execution system. In the evolution stage, the LLM starts from its own created harness and iteratively revises it using downstream execution feedback, with the goal of improving benchmark performance. The authors evaluate each constructed harness on capability (task success on held-out benchmarks) and efficiency (execution-token cost). The results show that generated harnesses remain substantially behind mature human-engineered references on code and search and research tasks, but match or exceed the selected references on writing and machine-learning experimentation tasks, with large variation in execution cost. The evolution stage produces some performance gains, but they are unstable and transfer only partially to held-out tasks.

### Soundness

3 good

### Presentation

3 good

### Contribution

2 fair

### Strengths

1. The paper is well-written and easy to follow.

2. The paper is well-motivated. The problem of LLMs developing their own agent harness is an important one, and this paper provides a new benchmark for evaluating this ability.

3. The paper provides a comprehensive evaluation of the LLMs' ability to develop their own agent harness, including both creation and evolution stages.

### Weaknesses

1. The paper lacks novelty. The idea of evaluating the ability of LLMs to develop their own agent harness is not new, and there have been several previous works on this topic. For example, the Meta-Agent Challenge (Lu et al., 2023) directly evaluates the development ability of LLMs. The paper does not clearly explain why the proposed benchmark is better than these previous works.

2. The paper lacks sufficient experiments. The paper only evaluates six LLMs on four domains and five downstream benchmarks, which is not enough to show the effectiveness of the proposed benchmark. The paper should evaluate more LLMs and benchmarks to demonstrate the effectiveness of the proposed benchmark.

3. The paper lacks sufficient analysis. The paper only provides some basic statistics of the results, but does not provide any in-depth analysis of the results. For example, the paper does not analyze the reasons why the generated harnesses perform better on writing and machine-learning experimentation tasks than on code and search and research tasks. The paper should provide more analysis of the results to help understand the reasons behind the results.

### Questions

1. Why is the proposed benchmark better than the previous works on evaluating the ability of LLMs to develop their own agent harness?

2. Why are the generated harnesses better on writing and machine-learning experimentation tasks than on code and search and research tasks?

3. What are the reasons behind the unstable performance gains in the evolution stage?

### Flag For Ethics Review

No ethics review needed.

### Rating

5: marginally below the acceptance threshold

### Confidence

4: You are confident in your assessment, but not absolutely certain. It is unlikely, but not impossible, that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work.

**********

## Reviewer

### Summary

This paper proposes a new benchmark for evaluating LLMs' ability to create and evolve their own agent harness. The benchmark consists of two stages: creation and evolution. In the creation stage, the LLM starts from a minimal seed and a small number of cases, then builds a complete execution system. In the evolution stage, the LLM starts from its own created harness and iteratively revises it using downstream execution feedback, with the goal of improving benchmark performance. The results show that generated harnesses remain substantially behind mature human-engineered references on code and search and research tasks, but match or exceed the selected references on writing and machine-learning experimentation tasks, with large variation in execution cost. The evolution stage produces some performance gains, but they are unstable and transfer only partially to held-out tasks.

### Soundness

3 good

### Presentation

3 good

### Contribution

3 good

### Strengths

The paper is well written and easy to follow. The motivation is clear and the paper is well-motivated. The paper provides a comprehensive evaluation of the LLMs' ability to develop their own agent harness, including both creation and evolution stages. The paper also provides a new benchmark for evaluating this ability, which can be useful for future research in this area.

### Weaknesses

The paper only evaluates six LLMs on four domains and five downstream benchmarks, which is not enough to show the effectiveness of the proposed benchmark. The paper should evaluate more LLMs and benchmarks to demonstrate the effectiveness of the proposed benchmark. The paper should also provide more analysis of the results to help understand the reasons behind the results.

### Questions

1. Why is the proposed benchmark better than the previous works on evaluating the ability of LLMs to develop their own agent harness?
2. Why are the generated harnesses better on writing and machine-learning experimentation tasks than on code and search and research tasks?
3. What are the reasons behind the unstable performance gains in the evolution stage?

### Flag For Ethics Review

No ethics review needed.

### Rating

5: marginally below the acceptance threshold

### Confidence

3: You are fairly confident in your assessment. It is possible that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work. Math/other details were not carefully checked.

**********

## Reviewer

### Summary

This paper presents a new benchmark for evaluating the ability of LLMs to develop their own agent harness. The benchmark consists of two stages: creation and evolution. In the creation stage, the LLM starts from a minimal seed and a small number of cases, then builds a complete execution system. In the evolution stage, the LLM starts from its own created harness and iteratively revises it using downstream execution feedback, with the goal of improving benchmark performance. The results show that generated harnesses remain substantially behind mature human-engineered references on code and search and research tasks, but match or exceed the selected references on writing and machine-learning experimentation tasks, with large variation in execution cost. The evolution stage produces some performance gains, but they are unstable and transfer only partially to held-out tasks.

### Soundness

3 good

### Presentation

3 good

### Contribution

3 good

### Strengths

This paper is well-written and easy to follow. The paper is well-motivated and the problem of LLMs developing their own agent harness is an important one. The paper provides a comprehensive evaluation of the LLMs' ability to develop their own agent harness, including both creation and evolution stages. The paper also provides a new benchmark for evaluating this ability, which can be useful for future research in this area.

### Weaknesses

The paper only evaluates six LLMs on four domains and five downstream benchmarks, which is not enough to show the effectiveness of the proposed benchmark. The paper should evaluate more LLMs and benchmarks to demonstrate the effectiveness of the proposed benchmark. The paper should also provide more analysis of the results to help understand the reasons behind the results.

### Questions

1. Why is the proposed benchmark better than the previous works on evaluating the ability of LLMs to develop their own agent harness?
2. Why are the generated harnesses better on writing and machine-learning experimentation tasks than on code and search and research tasks?
3. What are the reasons behind the unstable performance gains in the evolution stage?

### Flag For Ethics Review

No ethics review needed.

### Rating

5: marginally below the acceptance threshold

### Confidence

3: You are fairly confident in your assessment. It is possible that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work. Math/other details were not carefully checked.

**********

## Reviewer

### Summary

This paper introduces a benchmark called HarnessDev that evaluates the ability of LLMs to create and evolve their own agent harness. The benchmark consists of two stages: creation and evolution. In the creation stage, the LLM starts from a minimal seed and a small number of cases, then builds a complete execution system. In the evolution stage, the LLM starts from its own created harness and iteratively revises it using downstream execution feedback, with the goal of improving benchmark performance. The results show that generated harnesses remain substantially behind mature human-engineered references on code and search and research tasks, but match or exceed the selected references on writing and machine-learning experimentation tasks, with large variation in execution cost. The evolution stage produces some performance gains, but they are unstable and transfer only partially to held-out tasks.

### Soundness

3 good

### Presentation

3 good

### Contribution

3 good

### Strengths

The paper is well-written and easy to follow. The paper is well-motivated and the problem of LLMs developing their own agent harness is an important one. The paper provides a comprehensive evaluation of the LLMs' ability to develop their own agent harness, including both creation and evolution stages. The paper also provides a new benchmark for evaluating this ability, which can be useful for future research in this area.

### Weaknesses

The paper only evaluates six LLMs on four domains and five downstream benchmarks, which is not enough to show the effectiveness of the proposed benchmark. The paper should evaluate more LLMs and benchmarks to demonstrate the effectiveness of the proposed benchmark. The paper should also provide more analysis of the results to help understand the reasons behind the results.

### Questions

1. Why is the proposed benchmark better than the previous works on evaluating the ability of LLMs to develop their own agent harness?
2. Why are the generated harnesses better on writing and machine-learning experimentation tasks than on code and search and research tasks?
3. What are the reasons behind the unstable performance gains in the evolution stage?

### Flag For Ethics Review

No ethics review needed.

### Rating

5: marginally below the acceptance threshold

### Confidence

3: You are fairly confident in your assessment. It is possible that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work. Math/other details were not carefully checked.

**********

## Meta Review

The paper presents a benchmark for evaluating LLMs' ability to create and evolve their own agent harness. The benchmark consists of two stages: creation and evolution. In the creation stage, the LLM starts from a minimal seed and a small number of cases, then builds a complete execution system. In the evolution stage, the LLM starts from its own created harness and iteratively revises it using downstream execution feedback, with the goal of improving benchmark performance. The results show that generated harnesses remain substantially behind mature human-engineered references on code and search and research tasks, but match or exceed the selected references on writing and machine-learning experimentation tasks, with large variation in execution cost. The evolution stage produces some performance gains, but they are unstable and transfer only partially to held-out tasks.

Strengths: The paper is well-written and easy to follow. The paper is well-motivated and the problem of LLMs developing their own agent harness is an important one. The paper provides a comprehensive evaluation of the LLMs' ability to develop their own agent harness, including both creation and evolution stages. The paper also provides a new benchmark for evaluating this ability, which can be useful for future research in this area.

Weaknesses: The paper only evaluates six LLMs on four domains and five downstream benchmarks, which is not enough to show the effectiveness of the proposed benchmark. The paper should evaluate more LLMs and benchmarks to demonstrate the effectiveness of the proposed benchmark. The paper should also provide more analysis of the results to help understand the reasons behind the results.

### justification_for_why_not_higher_score

The paper only evaluates six LLMs on four domains and five downstream benchmarks, which is not enough to show the effectiveness of the proposed benchmark. The paper should evaluate more LLMs and benchmarks to demonstrate the effectiveness of the proposed benchmark. The paper should also provide more analysis of the results to help understand the reasons behind the results.

### justification_for_why_not_lower_score

N/A

**********

## Paper Decision

Reject (not selected for publication at ICLR 2024)

**********

## Paper Decision Summary

The paper introduces HarnessDev, a benchmark for evaluating the ability of LLMs to create and evolve their own agent harness. The benchmark consists of two stages: creation and evolution. In the creation stage, the LLM starts from a minimal seed and a small number of cases, then builds a complete execution system. In the evolution stage, the LLM starts from its own created harness and iteratively revises it using downstream execution feedback, with the goal of improving benchmark performance. The results show that generated harnesses remain substantially behind mature human-engineered references on code and search and research tasks, but match or exceed the selected references on writing and machine-learning experimentation tasks, with large variation in execution cost. The evolution stage produces some performance gains, but they are unstable and transfer only partially to held-out tasks.

Strengths: The paper is well-written and easy to follow. The paper is well-motivated and the problem of LLMs developing their own agent harness is an important one. The paper provides a comprehensive evaluation of the LLMs' ability to develop their own agent harness, including both creation and evolution stages. The paper also provides a new benchmark for evaluating this ability, which can be useful for future research in this area.

Weaknesses: The paper only evaluates six LLMs on four domains and five downstream benchmarks, which is not enough to show the effectiveness of the proposed benchmark. The paper should evaluate more LLMs and benchmarks to demonstrate the effectiveness of the proposed benchmark. The paper should also provide more analysis of the results to help understand the reasons behind the results.

**********

## Paper Decision

Reject (not selected for publication at ICLR 2024)

**********

<!--====================

## Paper Decision Summary

The paper introduces HarnessDev, a benchmark for evaluating the ability of LLMs to create and evolve their own agent harness. The benchmark consists of two stages: creation and evolution. In the creation stage, the LLM starts from a minimal seed and a small number of cases, then builds a complete execution system. In the evolution stage, the LLM starts from its own created harness and iteratively revises it using downstream execution feedback, with the goal of improving benchmark performance. The results show that generated harnesses remain substantially behind mature human-engineered references on code and search and research tasks, but match or exceed the selected references on writing and machine-learning experimentation tasks, with large variation in execution cost. The evolution stage produces some performance gains, but they are unstable and transfer only partially to held-out tasks.

Strengths: The paper is well-written and easy to follow. The paper is well-motivated and the problem of LLMs developing their own agent harness is an important one. The paper provides a comprehensive evaluation of the LLMs' ability to develop their own agent harness, including both creation and evolution stages. The paper also provides a new benchmark for evaluating this ability, which can be useful for future research in this area.

Weaknesses: The paper only evaluates six LLMs on four domains and five downstream benchmarks, which is not enough to show the effectiveness of the proposed benchmark. The paper should evaluate more LLMs and benchmarks to demonstrate the effectiveness of the proposed benchmark. The paper should also provide more analysis of the results to help understand the reasons behind the results.

====================-->
**********

<!--====================

## Paper Decision Summary

This paper introduces a benchmark called HarnessDev that evaluates the ability of LLMs to create and evolve their own agent harness. The benchmark consists of two stages: creation and evolution. In the creation stage, the LLM starts from a minimal seed and a small number of cases, then builds a complete execution system. In the evolution stage, the LLM starts from its own created harness and iteratively revises it using downstream execution feedback, with the goal of improving benchmark performance. The results show that generated harnesses remain substantially behind mature human-engineered references on code and search and research tasks, but match or exceed the selected references on writing and machine-learning experimentation tasks, with large variation in execution cost. The evolution stage produces some performance gains, but they are unstable and transfer only partially to held-out tasks.

Strengths: The paper is well-written and easy to follow. The paper is well-motivated and the problem of LLMs developing their own agent harness is an important one. The paper provides a comprehensive evaluation of the LLMs' ability to develop their own agent harness, including both creation and evolution stages. The paper also provides a new benchmark for evaluating this ability, which can be useful for future research in this area.

Weaknesses: The paper only evaluates six LLMs on four domains and five downstream benchmarks, which is not enough to show the effectiveness of the proposed benchmark. The paper should evaluate more LLMs and benchmarks to demonstrate the effectiveness of the proposed benchmark. The paper should also provide more analysis of the results to help understand the reasons behind the results.

====================-->
**********

<!--====================

## Paper Decision Summary

The paper presents a benchmark called HarnessDev that evaluates the ability of LLMs to create and evolve their own agent harness. The benchmark consists of two stages: creation and evolution. In the creation stage, the LLM starts from a minimal seed and a small number of cases, then builds a complete execution system. In the evolution stage, the LLM starts from its own created harness and iteratively revises it using downstream execution feedback, with the goal of improving benchmark performance. The results show that generated harnesses remain substantially behind mature human-engineered references on code and search and research tasks, but match or exceed the selected references on writing and machine-learning experimentation tasks, with large variation in execution cost. The evolution stage produces some performance gains, but they are unstable and transfer only partially to held-out tasks.

Strengths: The paper is well-written and easy to follow. The paper is well-motivated and the problem of LLMs developing their own agent harness is an important one. The paper provides a comprehensive evaluation of the LLMs' ability to develop their own agent harness, including both creation and evolution stages. The paper also provides a new benchmark for evaluating this ability, which can be useful for future research in this area.

Weaknesses: The paper only evaluates six LLMs on four domains and five downstream benchmarks, which is not enough to show the effectiveness of the proposed benchmark. The paper should evaluate more LLMs and benchmarks to demonstrate the effectiveness of the proposed benchmark. The paper should also provide more analysis of the results to help understand the reasons behind the results.

====================-->
**********

<!--====================

## Paper Decision Summary

This paper introduces a benchmark called HarnessDev that evaluates the ability of LLMs to create and evolve their own agent harness. The benchmark consists of two stages: creation and evolution. In the creation stage, the LLM starts from a minimal seed and a small number of cases, then builds a complete execution system. In the evolution stage, the LLM starts from its own created harness and iteratively revises it using downstream execution feedback, with the goal of improving benchmark performance. The results show that generated harnesses remain substantially behind mature human-engineered references on code and search and research tasks, but match or exceed the selected references on writing and machine-learning experimentation tasks, with large variation in execution cost. The evolution stage produces some performance gains, but they are unstable and transfer only partially to held-out tasks.

Strengths: The paper is well-written and easy to follow. The paper is well-motivated and the problem of LLMs developing their own agent harness is an important one. The paper provides a comprehensive evaluation of the LLMs' ability to develop their own agent harness, including both creation and evolution stages. The paper also provides a new benchmark for evaluating this ability, which can be useful for future research in this area.

Weaknesses: The paper only evaluates six LLMs on four domains and five downstream benchmarks, which is not enough to show the effectiveness of the proposed benchmark. The paper should evaluate more LLMs and benchmarks to demonstrate the effectiveness of the proposed benchmark. The paper should also provide more analysis of the results to help understand the reasons behind the results.

====================-->
**********

<!--====================

## Paper Decision Summary

This paper introduces a benchmark called HarnessDev that evaluates the ability of LLMs to create and evolve their own agent harness. The benchmark consists of two stages: creation and evolution. In the creation stage, the LLM starts from a minimal seed and a small number of cases, then builds a complete execution system. In the evolution stage, the LLM starts from its own created harness and iteratively revises it using downstream execution feedback, with the goal of improving benchmark performance. The results show that generated harnesses remain substantially behind mature human-engineered references on code and search and research tasks, but match or exceed the selected references on writing and machine-learning experimentation tasks, with large variation in execution cost. The evolution stage produces some performance gains, but they are unstable and transfer only partially to held-out tasks.

Strengths: The paper is well-written and easy to follow. The paper is well-motivated and the problem of LLMs developing their own agent harness is an important one. The paper provides a comprehensive evaluation of the LLMs' ability to develop their own agent harness, including both creation and evolution stages. The paper also provides a new benchmark for evaluating this ability, which can be useful for future research in this area.

Weaknesses: The paper only evaluates six LLMs on four domains and five downstream benchmarks, which is not enough to show the effectiveness of the proposed benchmark. The paper should evaluate more LLMs and benchmarks to demonstrate the effectiveness of the proposed benchmark. The paper should also provide more analysis of the results to help understand the reasons behind the results.

====================-->
**********

<!--====================

## Paper Decision Summary

The paper introduces HarnessDev, a benchmark for evaluating the ability of LLMs to create and evolve their own agent harness. The benchmark consists of two stages: creation and evolution. In the creation stage, the LLM starts from a minimal seed and a small number of cases, then builds a complete execution system. In the evolution stage, the LLM starts from its own created harness and iteratively revises it using downstream execution feedback, with the goal of improving benchmark performance. The results show that generated harnesses remain substantially behind mature human-engineered references on code and search and research tasks, but match or exceed the selected references on writing and machine-learning experimentation tasks, with large variation in execution cost. The evolution stage produces some performance gains, but they are unstable and transfer only partially to held-out tasks.

Strengths: The paper is well-written and easy to follow. The paper is well-motivated and the problem of LLMs developing their own agent harness is an important one. The paper provides a comprehensive evaluation of the LLMs' ability to develop their own agent harness, including both creation and evolution stages. The paper also provides a new benchmark for evaluating this ability, which can be useful for future research in this area.

Weaknesses: The paper only evaluates six LLMs on four domains and five downstream benchmarks, which is not enough to show the effectiveness of the proposed benchmark. The paper should evaluate more LLMs and benchmarks to demonstrate the effectiveness of the proposed benchmark. The paper should also provide more analysis of the results to help understand the reasons behind the results.

====================-->
**********

<!--====================

## Paper Decision Summary

This paper introduces a benchmark called HarnessDev that evaluates the ability of LLMs to create and evolve their own agent harness. The benchmark consists of two stages: creation and evolution. In the creation stage, the LLM starts from a minimal seed and a small number of cases, then builds a complete execution system. In the evolution stage, the LLM starts from its own created harness and iteratively revises it using downstream execution feedback, with the goal of improving benchmark performance. The results show that generated harnesses remain substantially behind mature human-engineered references on code and search and research tasks, but match or exceed the selected references on writing and machine-learning experimentation tasks, with large variation in execution cost. The evolution stage produces some performance gains, but they are unstable and transfer only partially to held-out tasks.

Strengths: The paper is well-written and easy to follow. The paper is well-motivated and the problem of LLMs developing their own agent harness is an important one. The paper provides a comprehensive evaluation of the LLMs' ability to develop their own agent harness, including both creation and evolution stages. The paper also provides a new benchmark for evaluating this ability, which can be useful for future research in this area.

Weaknesses: The paper only evaluates six LLMs on four domains and five downstream benchmarks, which is not enough to show the effectiveness of the proposed benchmark. The paper should evaluate more LLMs and benchmarks to demonstrate the effectiveness of the proposed benchmark. The paper should also provide more analysis of the results to help understand the reasons behind the results.

====================-->
**********

<!--====================

## Paper Decision Summary

The paper presents a benchmark called HarnessDev that evaluates the ability of LLMs to create and evolve their own agent harness. The benchmark consists of two stages: creation and evolution. In the creation stage, the LLM starts from a minimal seed and a small number of cases, then builds a complete execution system. In the evolution stage, the LLM starts from its own created harness and iteratively revises it using downstream execution feedback, with the goal of improving benchmark performance. The results show that generated harnesses remain substantially behind mature human-engineered references on code and search and research tasks, but match or exceed the selected references on writing and machine-learning experimentation tasks, with large variation in execution cost. The evolution stage produces some performance gains, but they are unstable and transfer only partially to held-out tasks.

Strengths: The paper is well-written and easy to follow. The paper is well-motivated and the problem of LLMs developing their own agent harness is an important one. The paper provides a comprehensive evaluation of the LLMs' ability to develop their own agent harness, including both creation and evolution stages. The paper also provides a new benchmark for evaluating this ability, which can be useful for future research in this area.

Weaknesses: The paper only evaluates six LLMs on four domains and five downstream benchmarks, which is not enough to show the effectiveness of the proposed benchmark. The paper should evaluate more LLMs and benchmarks to demonstrate the effectiveness of the proposed benchmark. The paper should also provide more analysis of the results to help understand the reasons behind the results.

====================-->
**********

<!--====================

## Paper Decision Summary

This paper introduces a benchmark called HarnessDev that evaluates the ability of LLMs to create and evolve their own agent harness. The benchmark consists of two stages: creation and evolution. In the creation stage, the LLM starts from a minimal seed and a small number of cases, then builds a complete execution system. In the evolution stage, the LLM starts from its own created harness and iteratively revises it using downstream execution feedback, with the goal of improving benchmark performance. The results show that generated harnesses remain substantially behind mature human-engineered references on code and search and research tasks, but match or exceed the selected references on writing and machine-learning experimentation tasks, with large variation in execution cost. The evolution stage produces some performance gains, but they are unstable and transfer only partially to held-out tasks.

Strengths: The paper is well-written and easy to follow. The paper is well-motivated and the problem of LLMs developing their own agent harness is an important one. The paper provides a comprehensive evaluation of the LLMs' ability to develop their own agent harness, including both creation and evolution stages. The paper also provides a new benchmark for evaluating this ability, which can be useful for future research in this area.

Weaknesses: The paper only evaluates six LLMs on four domains and five downstream benchmarks, which is not enough to show the effectiveness of the proposed benchmark. The paper should evaluate more LLMs and benchmarks to demonstrate the effectiveness of the proposed benchmark. The paper should also provide more analysis of the results to help understand the reasons behind the results.

====================-->
**********

<!--====================

## Paper Decision Summary

This paper introduces a benchmark called HarnessDev that evaluates the ability of LLMs to create and evolve their own agent harness. The benchmark consists of two stages: creation and evolution. In the creation stage, the LLM starts from a minimal seed and a small number of cases, then builds a complete execution system. In the evolution stage, the LLM starts from its own created harness and iteratively revises it using downstream execution feedback, with the goal of improving benchmark performance. The results show that generated harnesses remain substantially behind mature human-engineered references on code and search and research tasks, but match or exceed the selected references on writing and machine-learning experimentation tasks, with large variation in execution cost. The evolution stage produces some performance gains, but they are unstable and transfer only partially to held-out tasks.

Strengths: The paper is well-written and easy to follow. The paper is well-motivated and the problem of LLMs developing their own agent harness is an important one. The paper provides a comprehensive evaluation of the LLMs' ability to develop their own agent harness, including both creation and evolution stages. The paper also provides a new benchmark for evaluating this ability, which can be useful for future research in this area.

Weaknesses: The paper only evaluates six LLMs on four domains and five downstream benchmarks, which is not enough to show the effectiveness of the proposed benchmark. The paper should evaluate more LLMs and benchmarks to demonstrate the effectiveness of the proposed benchmark. The paper should also provide more analysis of the results to help understand the reasons behind the results.

====================-->
**********

<!--====================

## Paper Decision Summary

The paper introduces HarnessDev, a benchmark for evaluating the ability of LLMs to create and evolve their own agent harness. The benchmark consists of two stages: creation and evolution. In the creation stage, the LLM starts from a minimal seed and a small number of cases, then builds a complete execution system. In the evolution stage, the LLM starts from its own created harness and iteratively revises it using downstream execution feedback, with the goal of improving benchmark performance. The results show that generated harnesses remain substantially behind mature human-engineered references on code and search and research tasks, but match or exceed the selected references on writing and machine-learning experimentation tasks, with large variation in execution cost. The evolution stage produces some performance gains, but they are unstable and transfer only partially to held-out tasks.

Strengths: The paper is well-written and easy to follow. The paper is well-motivated and the problem of LLMs developing their own agent harness is an important one. The paper provides a comprehensive evaluation of the LLMs' ability to develop their own agent harness, including both creation and evolution stages. The paper also provides a new benchmark for evaluating this ability, which can be useful for future research in this area.

Weaknesses: The paper only evaluates six LLMs on four domains and five downstream benchmarks, which is not enough to show the effectiveness of the proposed benchmark. The paper should evaluate more LLMs and benchmarks to demonstrate the effectiveness of the proposed benchmark. The paper should also provide more analysis of the results to help understand the reasons behind the results.

====================-->
**********

<!--====================

## Paper Decision Summary

This paper introduces a benchmark called HarnessDev that evaluates the ability of LLMs to create and evolve their own agent harness. The benchmark consists of two stages: creation and evolution. In the creation stage, the LLM starts from a minimal seed and a small number of cases, then builds a complete execution system. In the evolution stage, the LLM starts from its own created harness and iteratively revises it using downstream execution feedback, with the goal of improving benchmark performance. The results show that generated harnesses remain substantially behind mature human-engineered references on code and search and research tasks, but match or exceed the selected references on writing and machine-learning experimentation tasks, with large variation in execution cost. The evolution stage produces some performance gains, but they are unstable and transfer only partially to held-out tasks.

Strengths: The paper is well-written and easy to follow. The paper is well-motivated and the problem of LLMs developing their own agent harness is an important one. The paper provides a comprehensive evaluation of the LLMs' ability to develop their own agent harness, including both creation and evolution stages. The paper also provides a new benchmark for evaluating this ability, which can be useful for future research in this area.

Weaknesses: The paper only evaluates six LLMs on four domains and five downstream benchmarks, which is not enough to show the effectiveness of the proposed benchmark. The paper should evaluate more LLMs and benchmarks to demonstrate the effectiveness of the proposed benchmark. The paper should also provide more analysis of the results to help understand the reasons behind the results.

====================-->
**********

<!--====================

## Paper Decision Summary

The paper presents a benchmark called HarnessDev that evaluates the ability of LLMs to create and evolve their own agent harness. The benchmark consists of two stages: creation and evolution. In the creation stage, the LLM starts from a minimal seed and a small number of cases, then builds a complete execution system. In the evolution stage, the LLM starts from its own created harness and iteratively revises it using downstream execution feedback, with the goal of improving benchmark performance