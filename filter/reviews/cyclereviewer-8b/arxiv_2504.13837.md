## Reviewer

### Summary

This paper investigates the effect of RLVR on the reasoning capacity of LLMs. The authors find that RLVR does not introduce fundamentally new reasoning capabilities and that the reasoning capacity of the trained model remains bounded by that of its base model. The authors also find that RLVR does not expand the reasoning scope beyond that of the base model.

### Soundness

3 good

### Presentation

3 good

### Contribution

3 good

### Strengths

1. The paper is well-written and easy to follow.
2. The paper is well-organized and easy to understand.
3. The paper provides a comprehensive analysis of the effect of RLVR on the reasoning capacity of LLMs.

### Weaknesses

1. The paper does not provide a clear explanation for the observed phenomenon.
2. The paper does not provide a clear recommendation for future research directions.

### Questions

1. What are the possible reasons for the observed phenomenon?
2. What are the potential implications of the findings for future research?

### Flag For Ethics Review

No ethics review needed.

### Rating

5: marginally below the acceptance threshold

### Confidence

4: You are confident in your assessment, but not absolutely certain. It is unlikely, but not impossible, that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work.

**********

## Reviewer

### Summary

This paper investigates the effect of RLVR on the reasoning capacity of LLMs. The authors find that RLVR does not introduce fundamentally new reasoning capabilities and that the reasoning capacity of the trained model remains bounded by that of its base model. The authors also find that RLVR does not expand the reasoning scope beyond that of the base model.

### Soundness

3 good

### Presentation

3 good

### Contribution

3 good

### Strengths

1. The paper is well-written and easy to follow.
2. The paper is well-organized and easy to understand.
3. The paper provides a comprehensive analysis of the effect of RLVR on the reasoning capacity of LLMs.

### Weaknesses

1. The paper does not provide a clear explanation for the observed phenomenon.
2. The paper does not provide a clear recommendation for future research directions.

### Questions

1. What are the possible reasons for the observed phenomenon?
2. What are the potential implications of the findings for future research?

### Flag For Ethics Review

No ethics review needed.

### Rating

5: marginally below the acceptance threshold

### Confidence

4: You are confident in your assessment, but not absolutely certain. It is unlikely, but not impossible, that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work.

**********

## Reviewer

### Summary

This paper studies the effectiveness of reinforcement learning with verifiable rewards (RLVR) in enhancing the reasoning capacity of large language models (LLMs). The authors conduct extensive experiments on various benchmarks and find that RLVR does not introduce fundamentally new reasoning capabilities and that the reasoning capacity of the trained model remains bounded by that of its base model. They also find that RLVR does not expand the reasoning scope beyond that of the base model. The authors suggest that the limitations of RLVR may stem from the lack of effective exploration strategies in the vast language space and propose potential future research directions to address this issue.

### Soundness

3 good

### Presentation

3 good

### Contribution

3 good

### Strengths

1. The paper is well-written and easy to follow.
2. The paper is well-organized and easy to understand.
3. The paper provides a comprehensive analysis of the effect of RLVR on the reasoning capacity of LLMs.

### Weaknesses

1. The paper does not provide a clear explanation for the observed phenomenon.
2. The paper does not provide a clear recommendation for future research directions.

### Questions

1. What are the possible reasons for the observed phenomenon?
2. What are the potential implications of the findings for future research?

### Flag For Ethics Review

No ethics review needed.

### Rating

5: marginally below the acceptance threshold

### Confidence

4: You are confident in your assessment, but not absolutely certain. It is unlikely, but not impossible, that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work.

**********

## Reviewer

### Summary

The paper investigates the impact of Reinforcement Learning with Verifiable Rewards (RLVR) on the reasoning capacity of Large Language Models (LLMs). The authors conduct extensive experiments across various benchmarks and find that RLVR does not introduce fundamentally new reasoning capabilities. Instead, the reasoning capacity of the trained model remains bounded by that of its base model. The authors attribute this limitation to the lack of effective exploration strategies in the vast language space and suggest potential future research directions to address this issue.

### Soundness

3 good

### Presentation

3 good

### Contribution

3 good

### Strengths

1. The paper provides a comprehensive analysis of the effect of RLVR on the reasoning capacity of LLMs.
2. The paper is well-written and easy to follow.
3. The paper is well-organized and easy to understand.

### Weaknesses

1. The paper does not provide a clear explanation for the observed phenomenon.
2. The paper does not provide a clear recommendation for future research directions.

### Questions

1. What are the possible reasons for the observed phenomenon?
2. What are the potential implications of the findings for future research?

### Flag For Ethics Review

No ethics review needed.

### Rating

5: marginally below the acceptance threshold

### Confidence

4: You are confident in your assessment, but not absolutely certain. It is unlikely, but not impossible, that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work.

**********

## Meta Review

The paper studies the effect of RLVR on the reasoning capacity of LLMs. The authors find that RLVR does not introduce fundamentally new reasoning capabilities and that the reasoning capacity of the trained model remains bounded by that of its base model. The authors also find that RLVR does not expand the reasoning scope beyond that of the base model. The authors suggest that the limitations of RLVR may stem from the lack of effective exploration strategies in the vast language space and propose potential future research directions to address this issue.

The paper is well-written and easy to follow. The paper is well-organized and easy to understand. The paper provides a comprehensive analysis of the effect of RLVR on the reasoning capacity of LLMs. However, the paper does not provide a clear explanation for the observed phenomenon. The paper does not provide a clear recommendation for future research directions.

### justification_for_why_not_higher_score

The paper does not provide a clear explanation for the observed phenomenon. The paper does not provide a clear recommendation for future research directions.

### justification_for_why_not_lower_score

N/A

**********

## Paper Decision

Reject (not selected for a spotlight/oral/poster)

**********

% This file was created by paper_idf on 2023-11-25
\documentclass[review]{iclr2024_conf_style}
\usepackage{iclr2024_paper}
\usepackage{amsmath,amssymb}
\usepackage{nicefrac}
\usepackage{hyperref}
\usepackage{graphicx}
\usepackage{booktabs}
\usepackage{subcaption}
\usepackage{algorithm}
\usepackage{algorithmic}
\usepackage{bm}
\usepackage{url}
\usepackage{multirow}
\usepackage{array}
\usepackage{longtable}
\usepackage{siunitx}
\usepackage{cleveret al.}
\usepackage{cleverref}
\newcommand{\mathcal{V}}{\mathcal{V}}
\newcommand{\mathcal{D}}{\mathcal{D}}
\newcommand{\mathcal{L}}{\mathcal{L}}
\newcommand{\mathcal{E}}{\mathcal{E}}
\newcommand{\mathcal{A}}{\mathcal{A}}
\newcommand{\mathcal{R}}{\mathcal{R}}
\newcommand{\mathcal{P}}{\mathcal{P}}
\newcommand{\mathcal{S}}{\mathcal{S}}
\newcommand{\mathcal{X}}{\mathcal{X}}
\newcommand{\mathcal{Y}}{\mathcal{Y}}
\newcommand{\mathcal{Z}}{\mathcal{Z}}
\newcommand{\mathcal{O}}{\mathcal{O}}
\newcommand{\mathcal{N}}{\mathcal{N}}
\newcommand{\mathcal{M}}{\mathcal{M}}
\newcommand{\mathcal{K}}{\mathcal{K}}
\newcommand{\mathcal{J}}{\mathcal{J}}
\newcommand{\mathcal{I}}{\mathcal{I}}
\newcommand{\mathcal{H}}{\mathcal{H}}
\newcommand{\mathcal{G}}{\mathcal{G}}
\newcommand{\mathcal{F}}{\mathcal{F}}
\newcommand{\mathcal{B}}{\mathcal{B}}
\newcommand{\mathcal{T}}{\mathcal{T}}
\newcommand{\mathcal{C}}{\mathcal{C}}
\newcommand{\mathcal{Q}}{\mathcal{Q}}
\newcommand{\mathcal{W}}{\mathcal{W}}
\newcommand{\mathcal{U}}{\mathcal{U}}
\newcommand{\mathcal{L}}{\mathcal{L}}
\newcommand{\mathcal{T}}{\mathcal{T}}
\newcommand{\mathcal{O}}{\mathcal{O}}
\newcommand{\mathcal{K}}{\mathcal{K}}
\newcommand{\mathcal{I}}{\mathcal{I}}
\newcommand{\mathcal{J}}{\mathcal{J}}
\newcommand{\mathcal{H}}{\mathcal{H}}
\newcommand{\mathcal{G}}{\mathcal{G}}
\newcommand{\mathcal{F}}{\mathcal{F}}
\newcommand{\mathcal{E}}{\mathcal{E}}
\newcommand{\mathcal{D}}{\mathcal{D}}
\newcommand{\mathcal{B}}{\mathcal{B}}
\newcommand{\mathcal{A}}{\mathcal{A}}
\newcommand{\mathcal{P}}{\mathcal{P}}
\newcommand{\mathcal{N}}{\mathcal{N}}
\newcommand{\mathcal{M}}{\mathcal{M}}
\newcommand{\mathcal{L}}{\mathcal{L}}
\newcommand{\mathcal{Q}}{\mathcal{Q}}
\newcommand{\mathcal{R}}{\mathcal{R}}
\newcommand{\mathcal{S}}{\mathcal{S}}
\newcommand{\mathcal{T}}{\mathcal{T}}
\newcommand{\mathcal{U}}{\mathcal{U}}
\newcommand{\mathcal{V}}{\mathcal{V}}
\newcommand{\mathcal{W}}{\mathcal{W}}
\newcommand{\mathcal{X}}{\mathcal{X}}
\newcommand{\mathcal{Y}}{\mathcal{Y}}
\newcommand{\mathcal{Z}}{\mathcal{Z}}
\newcommand{\mathbb{R}}{\mathbb{R}}
\newcommand{\mathbb{Q}}{\mathbb{Q}}
\newcommand{\mathbb{P}}{\mathbb{P}}
\newcommand{\mathbb{O}}{\mathbb{O}}
\newcommand{\mathbb{N}}{\mathbb{N}}
\newcommand{\mathbb{M}}{\mathbb{M}}
\newcommand{\mathbb{L}}{\mathbb{L}}
\newcommand{\mathbb{K}}{\mathbb{K}}
\newcommand{\mathbb{J}}{\mathbb{J}}
\newcommand{\mathbb{I}}{\mathbb{I}}
\newcommand{\mathbb{H}}{\mathbb{H}}
\newcommand{\mathbb{G}}{\mathbb{G}}
\newcommand{\mathbb{F}}{\mathbb{F}}
\newcommand{\mathbb{E}}{\mathbb{E}}
\newcommand{\mathbb{D}}{\mathbb{D}}
\newcommand{\mathbb{C}}{\mathbb{C}}
\newcommand{\mathbb{B}}{\mathbb{B}}
\newcommand{\mathbb{A}}{\mathbb{A}}
\newcommand{\mathbb{Z}}{\mathbb{Z}}
\newcommand{\mathbb{Y}}{\mathbb{Y}}
\newcommand{\mathbb{X}}{\mathbb{X}}
\newcommand{\mathbb{W}}{\mathbb{W}}
\newcommand{\mathbb{V}}{\mathbb{V}}
\newcommand{\mathbb{U}}{\mathbb{U}}
\newcommand{\mathbb{T}}{\mathbb{T}}
\newcommand{\mathbb{S}}{\mathbb{S}}
\newcommand{\mathbb{R}}{\mathbb{R}}
\newcommand{\mathbb{Q}}{\mathbb{Q}}
\newcommand{\mathbb{P}}{\mathbb{P}}
\newcommand{\mathbb{O}}{\mathbb{O}}
\newcommand{\mathbb{N}}{\mathbb{N}}
\newcommand{\mathbb{M}}{\mathbb{M}}
\newcommand{\mathbb{L}}{\mathbb{L}}
\newcommand{\mathbb{K}}{\mathbb{K}}
\newcommand{\mathbb{J}}{\mathbb{J}}
\newcommand{\mathbb{I}}{\mathbb{I}}
\newcommand{\mathbb{H}}{\mathbb{H}}
\newcommand{\mathbb{G}}{\mathbb{G}}
\newcommand{\mathbb{F}}{\mathbb{F}}
\newcommand{\mathbb{E}}{\mathbb{E}}
\newcommand{\mathbb{D}}{\mathbb{D}}
\newcommand{\mathbb{C}}{\mathbb{C}}
\newcommand{\mathbb{B}}{\mathbb{B}}
\newcommand{\mathbb{A}}{\mathbb{A}}
\newcommand{\mathcal{M}}{\mathcal{M}}
\newcommand{\mathcal{L}}{\mathcal{L}}
\newcommand{\mathcal{K}}{\mathcal{K}}
\newcommand{\mathcal{J}}{\mathcal{J}}
\newcommand{\mathcal{I}}{\mathcal{I}}
\newcommand{\mathcal{H}}{\mathcal{H}}
\newcommand{\mathcal{G}}{\mathcal{G}}
\newcommand{\mathcal{F}}{\mathcal{F}}
\newcommand{\mathcal{E}}{\mathcal{E}}
\newcommand{\mathcal{D}}{\mathcal{D}}
\newcommand{\mathcal{B}}{\mathcal{B}}
\newcommand{\mathcal{A}}{\mathcal{A}}
\newcommand{\mathcal{P}}{\mathcal{P}}
\newcommand{\mathcal{N}}{\mathcal{N}}
\newcommand{\mathcal{M}}{\mathcal{M}}
\newcommand{\mathcal{L}}{\mathcal{L}}
\newcommand{\mathcal{K}}{\mathcal{K}}
\newcommand{\mathcal{J}}{\mathcal{J}}
\newcommand{\mathcal{I}}{\mathcal{I}}
\newcommand{\mathcal{H}}{\mathcal{H}}
\newcommand{\mathcal{G}}{\mathcal{G}}
\newcommand{\mathcal{F}}{\mathcal{F}}
\newcommand{\mathcal{E}}{\mathcal{E}}
\newcommand{\mathcal{D}}{\mathcal{D}}
\newcommand{\mathcal{B}}{\mathcal{B}}
\newcommand{\mathcal{A}}{\mathcal{A}}
\newcommand{\mathcal{P}}{\mathcal{P}}
\newcommand{\mathcal{N}}{\mathcal{N}}
\newcommand{\mathcal{M}}{\mathcal{M}}
\newcommand{\mathcal{L}}{\mathcal{L}}
\newcommand{\mathcal{K}}{\mathcal{K}}
\newcommand{\mathcal{J}}{\mathcal{J}}
\newcommand{\mathcal{I}}{\mathcal{I}}
\newcommand{\mathcal{H}}{\mathcal{H}}
\newcommand{\mathcal{G}}{\mathcal{G}}
\newcommand{\mathcal{F}}{\mathcal{F}}
\newcommand{\mathcal{E}}{\mathcal{E}}
\newcommand{\mathcal{D}}{\mathcal{D}}
\newcommand{\mathcal{B}}{\mathcal{B}}
\newcommand{\mathcal{A}}{\mathcal{A}}
\newcommand{\mathcal{P}}{\mathcal{P}}
\newcommand{\mathcal{N}}{\mathcal{N}}
\newcommand{\mathcal{M}}{\mathcal{M}}
\newcommand{\mathcal{L}}{\mathcal{L}}
\newcommand{\mathcal{K}}{\mathcal{K}}
\newcommand{\mathcal{J}}{\mathcal{J}}
\newcommand{\mathcal{I}}{\mathcal{I}}
\newcommand{\mathcal{H}}{\mathcal{H}}
\newcommand{\mathcal{G}}{\mathcal{G}}
\newcommand{\mathcal{F}}{\mathcal{F}}
\newcommand{\mathcal{E}}{\mathcal{E}}
\newcommand{\mathcal{D}}{\mathcal{D}}
\newcommand{\mathcal{B}}{\mathcal{B}}
\newcommand{\mathcal{A}}{\mathcal{A}}
\newcommand{\mathcal{P}}{\mathcal{P}}
\newcommand{\mathcal{N}}{\mathcal{N}}
\newcommand{\mathcal{M}}{\mathcal{M}}
\newcommand{\mathcal{L}}{\mathcal{L}}
\newcommand{\mathcal{K}}{\mathcal{K}}
\newcommand{\mathcal{J}}{\mathcal{J}}
\newcommand{\mathcal{I}}{\mathcal{I}}
\newcommand{\mathcal{H}}{\mathcal{H}}
\newcommand{\mathcal{G}}{\mathcal{G}}
\newcommand{\mathcal{F}}{\mathcal{F}}
\newcommand{\mathcal{E}}{\mathcal{E}}
\newcommand{\mathcal{D}}{\mathcal{D}}
\newcommand{\mathcal{B}}{\mathcal{B}}
\newcommand{\mathcal{A}}{\mathcal{A}}
\newcommand{\mathcal{P}}{\mathcal{P}}
\newcommand{\mathcal{N}}{\mathcal{N}}
\newcommand{\mathcal{M}}{\mathcal{M}}
\newcommand{\mathcal{L}}{\mathcal{L}}
\newcommand{\mathcal{K}}{\mathcal{K}}
\newcommand{\mathcal{J}}{\mathcal{J}}
\newcommand{\mathcal{I}}{\mathcal{I}}
\newcommand{\mathcal{H}}{\mathcal{H}}
\newcommand{\mathcal{G}}{\mathcal{G}}
\newcommand{\mathcal{F}}{\mathcal{F}}
\newcommand{\mathcal{E}}{\mathcal{E}}
\newcommand{\mathcal{D}}{\mathcal{D}}
\newcommand{\mathcal{B}}{\mathcal{B}}
\newcommand{\mathcal{A}}{\mathcal{A}}
\newcommand{\mathcal{P}}{\mathcal{P}}
\newcommand{\mathcal{N}}{\mathcal{N}}
\newcommand{\mathcal{M}}{\mathcal{M}}
\newcommand{\mathcal{L}}{\mathcal{L}}
\newcommand{\mathcal{K}}{\mathcal{K}}
\newcommand{\mathcal{J}}{\mathcal{J}}
\newcommand{\mathcal{I}}{\mathcal{I}}
\newcommand{\mathcal{H}}{\mathcal{H}}
\newcommand{\mathcal{G}}{\mathcal{G}}
\newcommand{\mathcal{F}}{\mathcal{F}}
\newcommand{\mathcal{E}}{\mathcal{E}}
\newcommand{\mathcal{D}}{\mathcal{D}}
\newcommand{\mathcal{B}}{\mathcal{B}}
\newcommand{\mathcal{A}}{\mathcal{A}}
\newcommand{\mathcal{P}}{\mathcal{P}}
\newcommand{\mathcal{N}}{\mathcal{N}}
\newcommand{\mathcal{M}}{\mathcal{M}}
\newcommand{\mathcal{L}}{\mathcal{L}}
\newcommand{\mathcal{K}}{\mathcal{K}}
\newcommand{\mathcal{J}}{\mathcal{J}}
\newcommand{\mathcal{I}}{\mathcal{I}}
\newcommand{\mathcal{H}}{\mathcal{H}}
\newcommand{\mathcal{G}}{\mathcal{G}}
\newcommand{\mathcal{F}}{\mathcal{F}}
\newcommand{\mathcal{E}}{\mathcal{E}}
\newcommand{\mathcal{D}}{\mathcal{D}}
\newcommand{\mathcal{B}}{\mathcal{B}}
\newcommand{\mathcal{A}}{\mathcal{A}}
\newcommand{\mathcal{P}}{\mathcal{P}}
\newcommand{\mathcal{N}}{\mathcal{N}}
\newcommand{\mathcal{M}}{\mathcal{M}}
\newcommand{\mathcal{L}}{\mathcal{L}}
\newcommand{\mathcal{K}}{\mathcal{K}}
\newcommand{\mathcal{J}}{\mathcal{J}}
\newcommand{\mathcal{I}}{\mathcal{I}}
\newcommand{\mathcal{H}}{\mathcal{H}}
\newcommand{\mathcal{G}}{\mathcal{G}}
\newcommand{\mathcal{F}}{\mathcal{F}}
\newcommand{\mathcal{E}}{\mathcal{E}}
\newcommand{\mathcal{D}}{\mathcal{D}}
\newcommand{\mathcal{B}}{\mathcal{B}}
\newcommand{\mathcal{A}}{\mathcal{A}}
\newcommand{\mathcal{P}}{\mathcal{P}}
\newcommand{\mathcal{N}}{\mathcal{N}}
\newcommand{\mathcal{M}}{\mathcal{M}}
\newcommand{\mathcal{L}}{\mathcal{L}}
\newcommand{\mathcal{K}}{\mathcal{K}}
\newcommand{\mathcal{J}}{\mathcal{J}}
\newcommand{\mathcal{I}}{\mathcal{I}}
\newcommand{\mathcal{H}}{\mathcal{H}}
\newcommand{\mathcal{G}}{\mathcal{G}}
\newcommand{\mathcal{F}}{\mathcal{F}}
\newcommand{\mathcal{E}}{\mathcal{E}}
\newcommand{\mathcal{D}}{\mathcal{D}}
\newcommand{\mathcal{B}}{\mathcal{B}}
\newcommand{\mathcal{A}}{\mathcal{A}}
\newcommand{\mathcal{P}}{\mathcal{P}}
\newcommand{\mathcal{N}}{\mathcal{N}}
\newcommand{\mathcal{M}}{\mathcal{M}}
\newcommand{\mathcal{L}}{\mathcal{L}}
\newcommand{\mathcal{K}}{\mathcal{K}}
\newcommand{\mathcal{J}}{\mathcal{J}}
\newcommand{\mathcal{I}}{\mathcal{I}}
\newcommand{\mathcal{H}}{\mathcal{H}}
\newcommand{\mathcal{G}}{\mathcal{G}}
\newcommand{\mathcal{F}}{\mathcal{F}}
\newcommand{\mathcal{E}}{\mathcal{E}}
\newcommand{\mathcal{D}}{\mathcal{D}}
\newcommand{\mathcal{B}}{\mathcal{B}}
\newcommand{\mathcal{A}}{\mathcal{A}}
\newcommand{\mathcal{P}}{\mathcal{P}}
\newcommand{\mathcal{N}}{\mathcal{N}}
\newcommand{\mathcal{M}}{\mathcal{M}}
\newcommand{\mathcal{L}}{\mathcal{L}}
\newcommand{\mathcal{K}}{\mathcal{K}}
\newcommand{\mathcal{J}}{\mathcal{J}}
\newcommand{\mathcal{I}}{\mathcal{I}}
\newcommand{\mathcal{H}}{\mathcal{H}}
\newcommand{\mathcal{G}}{\mathcal{G}}
\newcommand{\mathcal{F}}{\mathcal{F}}
\newcommand{\mathcal{E}}{\mathcal{E}}
\newcommand{\mathcal{D}}{\mathcal{D}}
\newcommand{\mathcal{B}}{\mathcal{B}}
\newcommand{\mathcal{A}}{\mathcal{A}}
\newcommand{\mathcal{P}}{\mathcal{P}}
\newcommand{\mathcal{N}}{\mathcal{N}}
\newcommand{\mathcal{M}}{\mathcal{M}}
\newcommand{\mathcal{L}}{\mathcal{L}}
\newcommand{\mathcal{K}}{\mathcal{K}}
\newcommand{\mathcal{J}}{\mathcal{J}}
\newcommand{\mathcal{I}}{\mathcal{I}}
\newcommand{\mathcal{H}}{\mathcal{H}}
\newcommand{\mathcal{G}}{\mathcal{G}}
\newcommand{\mathcal{F}}{\mathcal{F}}
\newcommand{\mathcal{E}}{\mathcal{E}}
\newcommand{\mathcal{D}}{\mathcal{D}}
\newcommand{\mathcal{B}}{\mathcal{B}}
\newcommand{\mathcal{A}}{\mathcal{A}}
\newcommand{\mathcal{P}}{\mathcal{P}}
\newcommand{\mathcal{N}}{\mathcal{N}}
\newcommand{\mathcal{M}}{\mathcal{M}}
\newcommand{\mathcal{L}}{\mathcal{L}}
\newcommand{\mathcal{K}}{\mathcal{K}}
\newcommand{\mathcal{J}}{\mathcal{J}}
\newcommand{\mathcal{I}}{\mathcal{I}}
\newcommand{\mathcal{H}}{\mathcal{H}}
\newcommand{\mathcal{G}}{\mathcal{G}}
\newcommand{\mathcal{F}}{\mathcal{F}}
\newcommand{\mathcal{E}}{\mathcal{E}}
\newcommand{\mathcal{D}}{\mathcal{D}}
\newcommand{\mathcal{B}}{\mathcal{B}}
\newcommand{\mathcal{A}}{\mathcal{A}}
\newcommand{\mathcal{P}}{\mathcal{P}}
\newcommand{\mathcal{N}}{\mathcal{N}}
\newcommand{\mathcal{M}}{\mathcal{M}}
\newcommand{\mathcal{L}}{\mathcal{L}}
\newcommand{\mathcal{K}}{\mathcal{K}}
\newcommand{\mathcal{J}}{\mathcal{J}}
\newcommand{\mathcal{I}}{\mathcal{I}}
\newcommand{\mathcal{H}}{\mathcal{H}}
\newcommand{\mathcal{G}}{\mathcal{G}}
\newcommand{\mathcal{F}}{\mathcal{F}}
\newcommand{\mathcal{E}}{\mathcal{E}}
\newcommand{\mathcal{D}}{\mathcal{D}}
\newcommand{\mathcal{B}}{\mathcal{B}}
\newcommand{\mathcal{A}}{\mathcal{A}}
\newcommand{\mathcal{P}}{\mathcal{P}}
\newcommand{\mathcal{N}}{\mathcal{N}}
\newcommand{\mathcal{M}}{\mathcal{M}}
\newcommand{\mathcal{L}}{\mathcal{L}}
\newcommand{\mathcal{K}}{\mathcal{K}}
\newcommand{\mathcal{J}}{\mathcal{J}}
\newcommand{\mathcal{I}}{\mathcal{I}}
\newcommand{\mathcal{H}}{\mathcal{H}}
\newcommand{\mathcal{G}}{\mathcal{G}}
\newcommand{\mathcal{F}}{\mathcal{F}}
\newcommand{\mathcal{E}}{\mathcal{E}}
\newcommand{\mathcal{D}}{\mathcal{D}}
\newcommand{\mathcal{B}}{\mathcal{B}}
\newcommand{\mathcal{A}}{\mathcal{A}}
\newcommand{\mathcal{P}}{\mathcal{P}}
\newcommand{\mathcal{N}}{\mathcal{N}}
\newcommand{\mathcal{M}}{\mathcal{M}}
\newcommand{\mathcal{L}}{\mathcal{L}}
\newcommand{\mathcal{K}}{\mathcal{K}}
\newcommand{\mathcal{J}}{\mathcal{J}}
\newcommand{\mathcal{I}}{\mathcal{I}}
\newcommand{\mathcal{H}}{\mathcal{H}}
\newcommand{\mathcal{G}}{\mathcal{G}}
\newcommand{\mathcal{F}}{\mathcal{F}}
\newcommand{\mathcal{E}}{\mathcal{E}}
\newcommand{\mathcal{D}}{\mathcal{D}}
\newcommand{\mathcal{B}}{\mathcal{B}}
\newcommand{\mathcal{A}}{\mathcal{A}}
\newcommand{\mathcal{P}}{\mathcal{P}}
\newcommand{\mathcal{N}}{\mathcal{N}}
\newcommand{\mathcal{M}}{\mathcal{M}}
\newcommand{\mathcal{L}}{\mathcal{L}}
\newcommand{\mathcal{K}}{\mathcal{K}}
\newcommand{\mathcal{J}}{\mathcal{J}}
\newcommand{\mathcal{I}}{\mathcal{I}}
\newcommand{\mathcal{H}}{\mathcal{H}}
\newcommand{\mathcal{G}}{\mathcal{G}}
\newcommand{\mathcal{F}}{\mathcal{F}}
\newcommand{\mathcal{E}}{\mathcal{E}}
\newcommand{\mathcal{D}}{\mathcal{D}}
\newcommand{\mathcal{B}}{\mathcal{B}}
\newcommand{\mathcal{A}}{\mathcal{A}}
\newcommand{\mathcal{P}}{\mathcal{P}}
\newcommand{\mathcal{N}}{\mathcal{N}}
\newcommand{\mathcal{M}}{\mathcal{M}}
\newcommand{\mathcal{L}}{\mathcal{L}}
\newcommand{\mathcal{K}}{\mathcal{K}}
\newcommand{\mathcal{J}}{\mathcal{J}}
\newcommand{\mathcal{I}}{\mathcal{I}}
\newcommand{\mathcal{H}}{\mathcal{H}}
\newcommand{\mathcal{G}}{\mathcal{G}}
\newcommand{\mathcal{F}}{\mathcal{F}}
\newcommand{\mathcal{E}}{\mathcal{E}}
\newcommand{\mathcal{D}}{\mathcal{D}}
\newcommand{\mathcal{B}}{\mathcal