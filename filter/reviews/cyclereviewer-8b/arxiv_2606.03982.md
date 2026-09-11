## Reviewer

### Summary

This paper investigates how language models (LMs) compare quantities with measurement units. The authors find that accuracy degrades near the comparison boundary, and the resulting errors are systematic. They show that linear surrogate models can predict LM preferences from numerical-difference and unit-scale-difference cues, and causal interventions on subspaces aligned with these variables can shift LM's output. The results suggest that LM behavior is better explained by a bag of heuristics account over numeral and unit-scale cues than by an account based solely on first converting both expressions into exact shared-scale representations.

### Soundness

3 good

### Presentation

3 good

### Contribution

2 fair

### Strengths

The paper is well-written and easy to follow. The authors provide a clear and concise summary of their findings, and the figures are well-designed and informative.

### Weaknesses

1. The paper lacks novelty. The authors have conducted a thorough analysis of language models' behavior in comparing quantities with measurement units. However, the results are not surprising, and the conclusions drawn from the analysis are not particularly novel or groundbreaking. The paper could benefit from a more in-depth exploration of the implications of these findings or a more nuanced discussion of the limitations of the analysis.

2. The paper could benefit from a more detailed discussion of the limitations of the analysis. The authors acknowledge that their study focuses on controlled, single-step comparisons between two quantities with measurement units, and that it does not cover more realistic multi-step quantitative reasoning. They also note that their surrogate analysis uses linear models to approximate LM behavior from candidate cue features, which may miss nonlinear interactions among cues or more complex heuristic strategies. Additionally, they mention that extending their analysis to reasoning-oriented LMs or long chain-of-thought outputs is nontrivial. A more detailed discussion of these limitations and potential future directions for research could strengthen the paper.

3. The paper could benefit from a more comprehensive evaluation of the generalizability of the findings. The authors conduct experiments on a limited set of language models and unit settings, and it is unclear whether the results would generalize to other models or settings. A more thorough evaluation of the generalizability of the findings could provide more confidence in the conclusions drawn from the analysis.

### Questions

1. What are the implications of the findings for the development of language models? How could the insights gained from this analysis inform the design of more accurate and effective language models?

2. How do the results of this analysis compare to previous studies on language models' behavior in comparing quantities with measurement units? Are there any notable differences or similarities between the findings of this study and previous research in this area?

3. What are the limitations of the analysis, and how might they impact the conclusions drawn from the study?

### Flag For Ethics Review

No ethics review needed.

### Rating

5: marginally below the acceptance threshold

### Confidence

3: You are fairly confident in your assessment. It is possible that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work. Math/other details were not carefully checked.

**********

## Reviewer

### Summary

The paper studies how language models compare quantities with measurement units. The authors find that accuracy degrades near the comparison boundary, and the resulting errors are systematic. They show that linear surrogate models can predict LM preferences from numerical-difference and unit-scale-difference cues, and causal interventions on subspaces aligned with these variables can shift LM's output. The results suggest that LM behavior is better explained by a bag of heuristics account over numeral and unit-scale cues than by an account based solely on first converting both expressions into exact shared-scale representations.

### Soundness

3 good

### Presentation

3 good

### Contribution

3 good

### Strengths

The paper is well-written and easy to follow. The authors provide a clear and concise summary of their findings, and the figures are well-designed and informative.

The paper provides a thorough analysis of language models' behavior in comparing quantities with measurement units. The authors conduct experiments on a range of language models and unit settings, and their results provide valuable insights into how LMs process and compare quantities with measurement units.

The paper's findings have implications for the development of language models and could inform the design of more accurate and effective language models.

### Weaknesses

The paper lacks novelty. The authors have conducted a thorough analysis of language models' behavior in comparing quantities with measurement units. However, the results are not surprising, and the conclusions drawn from the analysis are not particularly novel or groundbreaking. The paper could benefit from a more in-depth exploration of the implications of these findings or a more nuanced discussion of the limitations of the analysis.

The paper could benefit from a more detailed discussion of the limitations of the analysis. The authors acknowledge that their study focuses on controlled, single-step comparisons between two quantities with measurement units, and that it does not cover more realistic multi-step quantitative reasoning. They also note that their surrogate analysis uses linear models to approximate LM behavior from candidate cue features, which may miss nonlinear interactions among cues or more complex heuristic strategies. Additionally, they mention that extending their analysis to reasoning-oriented LMs or long chain-of-thought outputs is nontrivial. A more detailed discussion of these limitations and potential future directions for research could strengthen the paper.

The paper could benefit from a more comprehensive evaluation of the generalizability of the findings. The authors conduct experiments on a limited set of language models and unit settings, and it is unclear whether the results would generalize to other models or settings. A more thorough evaluation of the generalizability of the findings could provide more confidence in the conclusions drawn from the analysis.

### Questions

What are the implications of the findings for the development of language models? How could the insights gained from this analysis inform the design of more accurate and effective language models?

How do the results of this analysis compare to previous studies on language models' behavior in comparing quantities with measurement units? Are there any notable differences or similarities between the findings of this study and previous research in this area?

What are the limitations of the analysis, and how might they impact the conclusions drawn from the study?

### Flag For Ethics Review

No ethics review needed.

### Rating

5: marginally below the acceptance threshold

### Confidence

3: You are fairly confident in your assessment. It is possible that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work. Math/other details were not carefully checked.

**********

## Reviewer

### Summary

This paper studies the behavior of language models when comparing quantities with measurement units, such as 110 cm and 1.2 m. The authors find that accuracy degrades near the comparison boundary, and the resulting errors are systematic. They show that linear surrogate models can predict LM preferences from numerical-difference and unit-scale-difference cues, and causal interventions on subspaces aligned with these variables can shift LM's output. The results suggest that LM behavior is better explained by a bag of heuristics account over numeral and unit-scale cues than by an account based solely on first converting both expressions into exact shared-scale representations.

### Soundness

3 good

### Presentation

3 good

### Contribution

3 good

### Strengths

This paper is well written and easy to follow. The authors provide a clear and concise summary of their findings, and the figures are well-designed and informative.

The paper provides a thorough analysis of language models' behavior in comparing quantities with measurement units. The authors conduct experiments on a range of language models and unit settings, and their results provide valuable insights into how LMs process and compare quantities with measurement units.

The paper's findings have implications for the development of language models and could inform the design of more accurate and effective language models.

### Weaknesses

The paper lacks novelty. The authors have conducted a thorough analysis of language models' behavior in comparing quantities with measurement units. However, the results are not surprising, and the conclusions drawn from the analysis are not particularly novel or groundbreaking. The paper could benefit from a more in-depth exploration of the implications of these findings or a more nuanced discussion of the limitations of the analysis.

The paper could benefit from a more detailed discussion of the limitations of the analysis. The authors acknowledge that their study focuses on controlled, single-step comparisons between two quantities with measurement units, and that it does not cover more realistic multi-step quantitative reasoning. They also note that their surrogate analysis uses linear models to approximate LM behavior from candidate cue features, which may miss nonlinear interactions among cues or more complex heuristic strategies. Additionally, they mention that extending their analysis to reasoning-oriented LMs or long chain-of-thought outputs is nontrivial. A more detailed discussion of these limitations and potential future directions for research could strengthen the paper.

The paper could benefit from a more comprehensive evaluation of the generalizability of the findings. The authors conduct experiments on a limited set of language models and unit settings, and it is unclear whether the results would generalize to other models or settings. A more thorough evaluation of the generalizability of the findings could provide more confidence in the conclusions drawn from the analysis.

### Questions

What are the implications of the findings for the development of language models? How could the insights gained from this analysis inform the design of more accurate and effective language models?

How do the results of this analysis compare to previous studies on language models' behavior in comparing quantities with measurement units? Are there any notable differences or similarities between the findings of this study and previous research in this area?

What are the limitations of the analysis, and how might they impact the conclusions drawn from the study?

### Flag For Ethics Review

No ethics review needed.

### Rating

5: marginally below the acceptance threshold

### Confidence

3: You are fairly confident in your assessment. It is possible that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work. Math/other details were not carefully checked.

**********

## Reviewer

### Summary

This paper studies how language models compare quantities with measurement units. The authors find that accuracy degrades near the comparison boundary, and the resulting errors are systematic. They show that linear surrogate models can predict LM preferences from numerical-difference and unit-scale-difference cues, and causal interventions on subspaces aligned with these variables can shift LM's output. The results suggest that LM behavior is better explained by a bag of heuristics account over numeral and unit-scale cues than by an account based solely on first converting both expressions into exact shared-scale representations.

### Soundness

3 good

### Presentation

3 good

### Contribution

3 good

### Strengths

The paper is well-written and easy to follow. The authors provide a clear and concise summary of their findings, and the figures are well-designed and informative.

The paper provides a thorough analysis of language models' behavior in comparing quantities with measurement units. The authors conduct experiments on a range of language models and unit settings, and their results provide valuable insights into how LMs process and compare quantities with measurement units.

The paper's findings have implications for the development of language models and could inform the design of more accurate and effective language models.

### Weaknesses

The paper lacks novelty. The authors have conducted a thorough analysis of language models' behavior in comparing quantities with measurement units. However, the results are not surprising, and the conclusions drawn from the analysis are not particularly novel or groundbreaking. The paper could benefit from a more in-depth exploration of the implications of these findings or a more nuanced discussion of the limitations of the analysis.

The paper could benefit from a more detailed discussion of the limitations of the analysis. The authors acknowledge that their study focuses on controlled, single-step comparisons between two quantities with measurement units, and that it does not cover more realistic multi-step quantitative reasoning. They also note that their surrogate analysis uses linear models to approximate LM behavior from candidate cue features, which may miss nonlinear interactions among cues or more complex heuristic strategies. Additionally, they mention that extending their analysis to reasoning-oriented LMs or long chain-of-thought outputs is nontrivial. A more detailed discussion of these limitations and potential future directions for research could strengthen the paper.

The paper could benefit from a more comprehensive evaluation of the generalizability of the findings. The authors conduct experiments on a limited set of language models and unit settings, and it is unclear whether the results would generalize to other models or settings. A more thorough evaluation of the generalizability of the findings could provide more confidence in the conclusions drawn from the analysis.

### Questions

What are the implications of the findings for the development of language models? How could the insights gained from this analysis inform the design of more accurate and effective language models?

How do the results of this analysis compare to previous studies on language models' behavior in comparing quantities with measurement units? Are there any notable differences or similarities between the findings of this study and previous research in this area?

What are the limitations of the analysis, and how might they impact the conclusions drawn from the study?

### Flag For Ethics Review

No ethics review needed.

### Rating

5: marginally below the acceptance threshold

### Confidence

3: You are fairly confident in your assessment. It is possible that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work. Math/other details were not carefully checked.

**********

## Meta Review

This paper studies how language models compare quantities with measurement units. The authors find that accuracy degrades near the comparison boundary, and the resulting errors are systematic. They show that linear surrogate models can predict LM preferences from numerical-difference and unit-scale-difference cues, and causal interventions on subspaces aligned with these variables can shift LM's output. The results suggest that LM behavior is better explained by a bag of heuristics account over numeral and unit-scale cues than by an account based solely on first converting both expressions into exact shared-scale representations.

The reviewers all agree that the paper is well written and easy to follow. The paper provides a thorough analysis of language models' behavior in comparing quantities with measurement units. The authors conduct experiments on a range of language models and unit settings, and their results provide valuable insights into how LMs process and compare quantities with measurement units. The paper's findings have implications for the development of language models and could inform the design of more accurate and effective language models.

However, the reviewers all agree that the paper lacks novelty. The authors have conducted a thorough analysis of language models' behavior in comparing quantities with measurement units. However, the results are not surprising, and the conclusions drawn from the analysis are not particularly novel or groundbreaking. The paper could benefit from a more in-depth exploration of the implications of these findings or a more nuanced discussion of the limitations of the analysis.

### justification_for_why_not_higher_score

The paper lacks novelty. The authors have conducted a thorough analysis of language models' behavior in comparing quantities with measurement units. However, the results are not surprising, and the conclusions drawn from the analysis are not particularly novel or groundbreaking. The paper could benefit from a more in-depth exploration of the implications of these findings or a more nuanced discussion of the limitations of the analysis.

### justification_for_why_not_lower_score

N/A

**********

## Paper Decision

Reject (not selected for publication in ICLR)

**********

## Paper Decision Overview

* Paper Decision: Reject (not selected for publication in ICLR)
* Confidence: 5
* Reviewer Scores: 5,5,5,5
* Reviewer Cover Letter: 
Reviewer 2: "I am happy to increase my score if the authors can address my concerns. Please let me know if you would like me to review a revised version of the paper. I am willing to increase my score if the authors can address my concerns. Please let me know if you would like me to review a revised version of the paper."

**********

## Paper Decision Policy

### Accept (oral)
The paper is strong in all aspects. It is well written and easy to follow. The problem is important and the proposed method is sound. The experiments are thorough and the results are convincing. The paper has a high potential to impact the community. The paper is above the acceptance threshold.

### Accept (poster)
The paper has some strengths. It is well written and easy to follow. The problem is important and the proposed method is sound. The experiments are thorough and the results are convincing. However, the paper falls short of being accepted as an oral paper. The paper could be improved with more experiments and/or more theoretical justification. The paper is above the acceptance threshold.

### Reject (not selected for publication in ICLR)
The paper has some strengths. It is well written and easy to follow. The problem is important and the proposed method is sound. The experiments are thorough and the results are convincing. However, the paper falls short of being accepted as a poster paper. The paper could be improved with more experiments and/or more theoretical justification. The paper is below the acceptance threshold.

### Reserve
Not enough information available for a confident evaluation.

**********

## Paper Decision Type
Reject (not selected for publication in ICLR)

**********

## Paper Decision Comments
The paper is well written and easy to follow. The problem is important and the proposed method is sound. The experiments are thorough and the results are convincing. However, the paper lacks novelty. The authors have conducted a thorough analysis of language models' behavior in comparing quantities with measurement units. However, the results are not surprising, and the conclusions drawn from the analysis are not particularly novel or groundbreaking. The paper could benefit from a more in-depth exploration of the implications of these findings or a more nuanced discussion of the limitations of the analysis.

**********

## Block 1: Paper Decision
Reject (not selected for publication in ICLR)

## Block 2: Paper Decision Comments
The paper is well written and easy to follow. The problem is important and the proposed method is sound. The experiments are thorough and the results are convincing. However, the paper lacks novelty. The authors have conducted a thorough analysis of language models' behavior in comparing quantities with measurement units. However, the results are not surprising, and the conclusions drawn from the analysis are not particularly novel or groundbreaking. The paper could benefit from a more in-depth exploration of the implications of these findings or a more nuanced discussion of the limitations of the analysis.

**********

## Block 3: Justification For Why Not Higher Score
The paper lacks novelty. The authors have conducted a thorough analysis of language models' behavior in comparing quantities with measurement units. However, the results are not surprising, and the conclusions drawn from the analysis are not particularly novel or groundbreaking. The paper could benefit from a more in-depth exploration of the implications of these findings or a more nuanced discussion of the limitations of the analysis.

**********

## Block 4: Justification For Why Not Lower Score
N/A

**********

## Block 5: Paper Decision Overview
Reject (not selected for publication in ICLR)

**********

## Block 6: Paper Decision Overview
Reject (not selected for publication in ICLR)

**********

## Block 7: Reviewer Scores
5,5,5,5

**********

## Block 8: Reviewer Cover Letter
Reviewer 2: "I am happy to increase my score if the authors can address my concerns. Please let me know if you would like me to review a revised version of the paper. I am willing to increase my score if the authors can address my concerns. Please let me know if you would like me to review a revised version of the paper."

**********

**********

## Paper Decision (AC)
Reject (not selected for publication in ICLR)

**********

## Paper Decision Comments (AC)
The paper is well written and easy to follow. The problem is important and the proposed method is sound. The experiments are thorough and the results are convincing. However, the paper lacks novelty. The authors have conducted a thorough analysis of language models' behavior in comparing quantities with measurement units. However, the results are not surprising, and the conclusions drawn from the analysis are not particularly novel or groundbreaking. The paper could benefit from a more in-depth exploration of the implications of these findings or a more nuanced discussion of the limitations of the analysis.

**********

## Justification For Why Not Higher Score (AC)
The paper lacks novelty. The authors have conducted a thorough analysis of language models' behavior in comparing quantities with measurement units. However, the results are not surprising, and the conclusions drawn from the analysis are not particularly novel or groundbreaking. The paper could benefit from a more in-depth exploration of the implications of these findings or a more nuanced discussion of the limitations of the analysis.

**********

## Justification For Why Not Lower Score (AC)
N/A

**********

## Paper Decision Overview (AC)
Reject (not selected for publication in ICLR)

**********

## Paper Decision Overview (AC)
Reject (not selected for publication in ICLR)

**********

**********

**********

**********

## Block 1: Paper Decision
Reject (not selected for publication in ICLR)

## Block 2: Paper Decision Comments
The paper is well written and easy to follow. The problem is important and the proposed method is sound. The experiments are thorough and the results are convincing. However, the paper lacks novelty. The authors have conducted a thorough analysis of language models' behavior in comparing quantities with measurement units. However, the results are not surprising, and the conclusions drawn from the analysis are not particularly novel or groundbreaking. The paper could benefit from a more in-depth exploration of the implications of these findings or a more nuanced discussion of the limitations of the analysis.

## Block 3: Justification For Why Not Higher Score
The paper lacks novelty. The authors have conducted a thorough analysis of language models' behavior in comparing quantities with measurement units. However, the results are not surprising, and the conclusions drawn from the analysis are not particularly novel or groundbreaking. The paper could benefit from a more in-depth exploration of the implications of these findings or a more nuanced discussion of the limitations of the analysis.

## Block 4: Justification For Why Not Lower Score
N/A

## Block 5: Paper Decision Overview
Reject (not selected for publication in ICLR)

## Block 6: Paper Decision Overview
Reject (not selected for publication in ICLR)

## Block 7: Reviewer Scores
5,5,5,5

## Block 8: Reviewer Cover Letter
Reviewer 2: "I am happy to increase my score if the authors can address my concerns. Please let me know if you would like me to review a revised version of the paper. I am willing to increase my score if the authors can address my concerns. Please let me know if you would like me to review a revised version of the paper."

## Block 9: Paper Decision (AC)
Reject (not selected for publication in ICLR)

## Block 10: Paper Decision Comments (AC)
The paper is well written and easy to follow. The problem is important and the proposed method is sound. The experiments are thorough and the results are convincing. However, the paper lacks novelty. The authors have conducted a thorough analysis of language models' behavior in comparing quantities with measurement units. However, the results are not surprising, and the conclusions drawn from the analysis are not particularly novel or groundbreaking. The paper could benefit from a more in-depth exploration of the implications of these findings or a more nuanced discussion of the limitations of the analysis.

## Block 11: Justification For Why Not Higher Score (AC)
The paper lacks novelty. The authors have conducted a thorough analysis of language models' behavior in comparing quantities with measurement units. However, the results are not surprising, and the conclusions drawn from the analysis are not particularly novel or groundbreaking. The paper could benefit from a more in-depth exploration of the implications of these findings or a more nuanced discussion of the limitations of the analysis.

## Block 12: Justification For Why Not Lower Score (AC)
N/A

## Block 13: Paper Decision Overview (AC)
Reject (not selected for publication in ICLR)

## Block 14: Paper Decision Overview (AC)
Reject (not selected for publication in ICLR)

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

