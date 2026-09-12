##### Report GitHub Issue

Content selection saved. Describe the issue below:

# Artifacts or Abduction: How Do LLMs Answer Multiple-Choice Questions Without the Question?

###### Abstract

Multiple-choice question answering (MCQA) is often used to evaluate large language models (LLMs). To see if MCQA assesses LLMs as intended, we probe if LLMs can perform MCQA with choices-only prompts, where models must select the correct answer only from the choices. In three MCQA datasets and four LLMs, this prompt bests a majority baseline in 11/12 cases, with up to 0.33 accuracy gain. To help explain this behavior, we conduct an in-depth, black-box analysis on memorization, choice dynamics, and question inference. Our key findings are threefold. First, we find no evidence that the choices-only accuracy stems from memorization alone. Second, priors over individual choices do not fully explain choices-only accuracy, hinting that LLMs use the group dynamics of choices. Third, LLMs have some ability to infer a relevant question from choices, and surprisingly can sometimes even match the original question. Inferring the original question is an impressive reasoning strategy, but it cannot fully explain the high choices-only accuracy of LLMs in MCQA. Thus, while LLMs are not fully incapable of reasoning in MCQA, we still advocate for the use of stronger baselines in MCQA benchmarks, the design of robust MCQA datasets for fair evaluations, and further efforts to explain LLM decision-making. 1 1 1 Our data and code are available at https://github.com/nbalepur/mcqa-artifacts

## 1 Introduction

Multiple-choice question answering (MCQA) has been key for evaluating large language models (LLMs), valued for its ease of scoring and alignment with human testing protocols Robinson and Wingate (2023) . In this task, a model is given a question and list of choices as input, and must select the choice that best answers the question. This process is intended to assess if LLMs comprehend, use relevant pretraining knowledge, and reason via information from both the question and the choices. Since MCQA is meant to evaluate several model abilities, it is often used to rank LLMs in benchmarks such as the Open LLM leaderboard Beeching et al. (2023) and the Holistic Evaluation of Language Models Liang et al. (2023) benchmark.

Given this role of MCQA, it is essential to verify that MCQA accuracy reflects the abilities we intend to measure. While this concern has been studied with prompt sensitivity Zheng et al. (2024) , an unexplored aspect of MCQA-based LLM evaluation is dataset artifacts—patterns or biases in text that models may use as shortcuts, rather than completing the task as intended. Researchers have found that partial-input baselines Poliak et al. (2018) , models trained using just a subset of inputs, can exploit artifacts in parts of the input. Such models include hypothesis -only models in natural language inference Poliak et al. (2018) ; Herlihy and Rudinger (2021) and passage -only models in reading comprehension Shah et al. (2020) ; Kaushik and Lipton (2018) . If LLMs rely on artifacts, our datasets may not only fail to assess the skills they are designed to, but we may also overestimate LLMs and face generalizability issues in deployment Wiegreffe and Marasović (2021) .

Thus, to gauge if MCQA measures LLM abilities as intended, we probe if LLaMA-2 Touvron et al. (2023) , Falcon Penedo et al. (2023) , Phi-2 Abdin et al. (2023) , and Mixtral Jiang et al. (2024) can use artifacts on three benchmarks: ARC Clark et al. (2018) , MMLU Hendrycks et al. (2021) , and HellaSwag Zellers et al. (2019) . To do so, we test a partial-input choices -only model in MCQA, which omits the question and only sees the choices. Concretely, we propose partial-input prompts , a strategy analogous to trainable partial-input models, where only a subset of inputs are used in a prompt.

For our tested LLMs and datasets, we find that in 11/12 cases, choices-only accuracies significantly surpass majority baselines, with a sizeable gain of 0.33 in LLaMA on HellaSwag. Notably, this is achieved with minimal few-shot examples, ranging from 5 on MMLU to 25 on ARC. To give more insights, we design tests to help explain how LLMs obtain high choices-only accuracy and see if this behavior stems from surface-level shortcuts usually associated with artifacts Du et al. (2023) , or if more advanced reasoning is employed. We test three hypotheses, shown in Figure 1 (right).

1) Memorization: One explanation is that the LLM has been trained on the test set and is recalling answers via memorization ( section 4 ). To test this, we create partial-input prompts that give no discriminative information in the choices, and can only be answered if the LLM has already seen the answer (Figure 1 , top ). These prompts never largely best the majority baseline, leading us to test more complex behaviors to explain choices-only accuracy.

2) Choice Dynamics: With no evidence of memorization, we define two properties of choices that could explain the high choices-only accuracy ( section 5 ). First, LLMs may have individual priors on choices, such as favoring choices that contain “always.” Second, LLMs may use the group dynamics of choices, where the models assess a choice based on the other choices, such as favoring an odd-numbered choice if the other choices are even. We refer to these latter behaviors as meta-strategies , where the model reasons over all choices beyond individual priors.

To quantify the impact of individual priors on choices-only accuracy, we prompt the LLM to classify the correctness of each choice in isolation (Figure 1 , middle ). This prompt only sees one choice at a time and thus the LLM can only use its individual priors. In several cases, the individual priors alone cannot explain the high choices-only accuracy, implying that LLMs reason over all choices rather than just using cues from individual choices.

3) Abductive Question Inference: Inspired by work using LLMs to verbalize inferences Hoyle et al. (2023) and given the potential use of meta-strategies, we see if LLMs can reason via the meta-strategy of abductive question inference (AQI) ( section 6 ). We design a two-step prompt where the LLM: 1) abductively infers the missing question from the choices; and 2) answers its own question (Figure 1 , bottom ). We call it abductive QI as we aim to generate the question that best explains the observed choices Peirce (1974) ; Bhagavatula et al. (2020) .

AQI performs similarly to the choices-only prompt, even besting it for 3 LLMs on HellaSwag, and they also exhibit moderate agreement, implying that AQI may be just one of many strategies LLMs use in choices-only settings. We then study the questions generated by LLaMA on ARC. Out of the 43 cases when AQI picks the gold answer and the inferred question is answerable by one of the choices, 42% match the meaning of the original question . Thus, we argue that a successful choices-only prompt does not always mean that the LLM uses surface-level shortcuts linked with artifacts; in some cases, it may recover the missing question.

Our intention is not to discredit MCQA evaluations. Instead, by highlighting the high choices-only accuracy of LLMs and investigating several potential explanations, we aim to give suggestions to enhance transparency and robustness in benchmarking, as well as provide insights into the decision-making of LLMs in partial-input settings. Our contributions can be summarized as follows:

1) We assess choices-only prompts with four LLMs and three MCQA datasets, being the first to show that LLMs can exhibit high partial-input accuracy in few-shot settings and with minimal exemplars. 2) We test several hypotheses to help explain this high choices-only accuracy, such as memorization, choice priors, and abductive question inference. 3) We release a thorough black-box MCQA analysis suite to facilitate transparent LLM evaluations.

## 2 Experimental Setup

### 2.1 MCQA Task Definition

Our MCQA task is based on Robinson and Wingate (2023) , where the model is given: 1) a question q q ; and 2) a set of four choices 𝒞 = { c a , c b , c c , c d } \mathcal{C}=\{c_{a},c_{b},c_{c},c_{d}\} , exactly one of which is correct (i.e. gold choice c g ∈ 𝒞 c_{g}\in\mathcal{C} ). Using these inputs, the LLM must give the letter of the correct option a ∈ { (A) , (B) , (C) , (D) } a\in\{\texttt{(A)},\texttt{(B)},\texttt{(C)},\texttt{(D)}\} .

The standard MCQA prompt is a full prompt , where the LLM uses the question q q and choices 𝒞 \mathcal{C} :

In the prompt box above, and all prompt boxes in this paper, the non-highlighted text represents the input prompt provided to the model, while the highlighted text represents what the model generates (e.g. the letter of the choice in Prompt 2.1 ). All of our prompts are few-shot to guide the LLM outputs, leaving zero-shot artifact exploitation for future work. In the few-shot prompts, each exemplar follows the same format shown in the prompt box. For the exemplars, the highlighted text is replaced with the ground truth (Example in Appendix A.4 ).

### 2.2 Models

Due to the cost of closed-source LLMs, we study four open-source LLMs: LLaMA-2 70B 2 2 2 LLaMA is 8-bit quantized on MMLU to use less memory. Touvron et al. (2023) , Falcon 40B 3 3 3 Falcon is 20-shot on ARC to fit its 2048 token limit. Penedo et al. (2023) , Mixtral 8x7B Jiang et al. (2024) , and Phi-2 (2.7B) Abdin et al. (2023) . Each LLM is run with HuggingFace. We generate with default parameters and set the output length between 5 and 200 tokens.

### 2.3 Datasets

We select three MCQA benchmarks from the Open LLM Leaderboard Beeching et al. (2023) : ARC -Challenge Clark et al. (2018) , MMLU Hendrycks et al. (2021) , and HellaSwag Zellers et al. (2019) , collectively testing factual knowledge, scientific reasoning, and commonsense reasoning. We use the entire evaluation sets, but omit the questions in ARC that do not have four choices to ensure all questions have four choices. We follow the Open LLM Leaderboard to pick few-shot examples and use 25 random training examples for ARC, 10 random training examples for HellaSwag, and the 5 given training examples for each subject in MMLU. While our experiments reflect the prompting setups of present MCQA benchmarks, we believe that future works could extend our analysis with zero-shot prompting Kojima et al. (2022) to limit the influence of priors from the few-shot examples.

### 2.4 Evaluation Protocol

As defined in section 2.1 , the LLM aims to generate the letter of the gold answer choice. This black-box setup allows us to study LLM behavior without accessing LLM internals. However, one drawback is that LLMs may produce invalid outputs (e.g. “(E)” when there are four choices), especially when using atypical prompts like the memorization prompts in Figure 1 (top). In these cases, the LLM may not understand the task even with few-shot examples.

One solution is to mark every invalid output as incorrect, but this unfairly penalizes the LLM when the mistake likely stems from the atypical prompt. Thus, for a fair evaluation, when the LLM gives an invalid output, we treat it as random guessing and assign a score of 0.25. In Appendix A.5 , we show versions of all experiments where invalid outputs are marked as wrong, which do not alter our claims.

## 3 Performing MCQA With No Question

To test if LLMs exploit MCQA artifacts, we design partial-input choices-only prompts ( section 3.1 ), and show that these prompts often largely best majority baselines 4 4 4 A majority class baseline always predicts the most frequent answer choice found in the dataset. ( section 3.2 ). High partial-input accuracies typically imply artifact exploitation via simple shortcuts Du et al. (2023) . However, in § 6 we explore if some of this overperformance can be attributed to the LLM’s ability to infer the original question. In this case, it would be difficult to claim that the model has bypassed the intended MCQA format. Thus, in this section, we establish an initial ceiling for artifact exploitation in the choices-only setting.

### 3.1 Prompt Design

Artifacts can be uncovered via partial-input models Poliak et al. (2018) —trained models that omit parts of the input. To adapt this for LLMs, we propose an analogous method: partial-input prompts . In MCQA, the apt partial-input prompt is a choices-only prompt, where LLMs only use the choices:

We expect Prompt 3.1 to perform near a majority baseline, as ignoring the question should ideally equal random guessing. An accuracy largely above this suggests that the model may use artifacts.

### 3.2 Results

In 11/12 cases, the choices-only prompt surpasses the majority baseline significantly, indicating that LLMs may be using artifacts in MCQA benchmarks (Figure 2 ). Further, larger LLMs tend to have higher choices-only accuracy, implying that more capable LLMs may use artifacts to a higher degree. In Appendix B.1 , we study scaling laws with LLaMA to understand this relation more. Overall, these results serve as an initial ceiling for artifact exploitation in choices-only settings, which we use to motivate our subsequent analyses that help attribute where this accuracy may stem from.

Takeaway: Prior work has found artifacts with trained partial-input models Gururangan et al. (2018) , but we are the first to show that LLMs exhibit high choices-only accuracy in MCQA benchmarks, even in few-shot settings with limited exemplars. For researchers seeking to have LLMs perform MCQA as intended, where both the question and choices are needed, we recommend three approaches: First, along with typical MCQA metrics, choices-only prompts can be reported as stronger alternatives to majority baselines Poliak et al. (2018) . Second, researchers can design datasets with more robust protocols, such as the Winograd pair format Levesque et al. (2011) , to mitigate the potential for artifacts. Third, HellaSwag has the highest choices-only accuracy (0.585 with LLaMA) and it is also the only dataset with human -written gold answers and model -written distractors. Thus, the gold answers may contain stylistic cues distinct from the distractors, which can inform strong discriminators like LLMs in partial-input settings. To avoid introducing such artifacts, we advise researchers to use a consistent approach when generating text data.

## 4 Hypothesis 1: Memorization

Our first hypothesis to explain choices-only accuracy is test set leakage, where the LLM is trained on the test set Zhou et al. (2023) . If this occurred, the LLM could recall the answer via memorization Huang et al. (2022) . To test this, we design prompts only answerable via memorization ( section 4.1 ). We assess these prompts and find that memorization cannot explain choices-only accuracy ( section 4.2 ).

### 4.1 Prompt Design

While it is possible to test memorization via contamination analysis Sainz et al. (2023) , this does not reveal how memorization affects MCQA accuracy. As a simple solution, we create partial-input prompts where the LLM must return the letter a a of the correct choice, but without any discriminative information in the choices. Such prompts are only answerable if the LLM has already been trained on the example, allowing us to quantify how memorization alone impacts choices-only accuracy:

We cannot detect all forms of memorization, as adversarial actors could train an LLM on the test set while shuffling the choice order, bypassing our prompts. However, we assume a non-adversarial setting to test exact memorization and conjecture that if substantial exact memorization had occurred, these prompts would best the majority baseline.

### 4.2 Results

Figure 3 shows no strong evidence that our LLMs memorized the test sets, as the prompts only barely surpass the majority baseline once. While impossible to rule out memorization entirely, we believe that more complex strategies lead to high choices-only accuracy, motivating our ensuing analyses on choice dynamics ( section 5 ) and question inference ( section 6 ).

## 5 Hypothesis 2: Choice Dynamics

With no evidence of memorization in section 4 , we study choice dynamics in MCQA. We define two properties of answer choices that could account for the LLMs’ high accuracy in choices-only prompts:

1) Individual Priors: LLMs may learn strong priors over specific choices from in-context learning or pretraining. For instance, an LLM may believe a priori that “Albert Einstein” is often correct, or subtly that choices containing “not” are often wrong, informing its decision in the choices-only setting.

2) Group Dynamics: LLMs may also ground the evaluation of the correctness of a choice based on its relation to surrounding choices. For example, if an LLM is given a math question with three odd choices and one even choice, the model may reason that the even choice is correct, as it has distinct parity. We define these processes as meta-strategies , where the LLM reasons or makes decisions over a group of choices beyond assessing a single choice, such as inferring the original question ( section 6 ) or eliminating similar options Balepur et al. (2023) .

In this section, we tease apart these two factors of choice dynamics. We first design a prompt format that tasks LLMs with classifying the individual correctness of choices ( section 5.1 ), isolating the effect of individual priors on choices-only accuracy. Next, we develop a scoring system to make these binary classification scores directly comparable to the accuracy of the choices-only prompt ( section 5.2 ). Finally, we assess the relation of individual priors and meta-strategies to choices-only accuracy ( section 5.3 ).

### 5.1 Prompt Design

In a full (Prompt 2.1 ) or choices-only (Prompt 3.1 ) prompt, the LLMs’ accuracy can be explained by both individual priors and group dynamics, since these prompts include all of the choices in 𝒞 \mathcal{C} . To isolate how individual priors alone affect choices-only accuracy, we prompt the LLMs to classify the correctness of each choice c ∈ 𝒞 c\in\mathcal{C} separately. Since these prompts only include a single choice, LLMs cannot use group dynamics. We create two versions of this prompt, when the question q q is present or absent, mirroring the full and choices-only prompts:

Our other few-shot prompts include all choices, using n n MCQA questions as exemplars for an n n -shot prompt, but the above individual prompts must be adapted to manage the increase of 4 ​ n 4n total exemplars (4 choices c c per n n questions). Thus, to keep an n n -shot format, we segment the exemplars such that ⌈ n 2 ⌉ \lceil\frac{n}{2}\rceil classify a random distractor as False and ⌊ n 2 ⌋ \lfloor\frac{n}{2}\rfloor classify the gold answer as True , balancing exposure to both True and False labels.

### 5.2 Converting Individual Scores

To study MCQA when LLMs can use individual priors and group dynamics versus only individual priors, we seek to compare the accuracies of the group full and choices-only prompts (Prompts 2.1 , 3.1 ) against their individual counterparts (Prompts 5.1 , 5.1 ). But the group setting is four-way classification, while the individual setting is binary classification, preventing a direct comparison of the tasks.

Thus, we introduce a function that converts the binary accuracy in the individual setting to a score comparable to the four-way accuracy in the group setting. Based on elimination testing Ben-Simon et al. (1997) , we define s ​ c ​ o ​ r ​ e ​ ( 𝒞 t ​ r ​ u ​ e , c g ) score(\mathcal{C}_{true},c_{g}) , returning the chance the LLM picks the gold choice c g ∈ 𝒞 c_{g}\in\mathcal{C} given the choices 𝒞 t ​ r ​ u ​ e ⊆ 𝒞 \mathcal{C}_{true}\subseteq\mathcal{C} it classifies as True : s ​ c ​ o ​ r ​ e ​ ( 𝒞 t ​ r ​ u ​ e , c g ) = { 0.25 if ​ | 𝒞 t ​ r ​ u ​ e | = 0 0 elif ​ c g ∉ 𝒞 t ​ r ​ u ​ e 1 | 𝒞 t ​ r ​ u ​ e | elif ​ c g ∈ 𝒞 t ​ r ​ u ​ e score(\mathcal{C}_{true},c_{g})=\begin{cases}0.25&\text{if }|\mathcal{C}_{true}|=0\\ 0&\text{elif }c_{g}\notin\mathcal{C}_{true}\\ \frac{1}{|\mathcal{C}_{true}|}&\text{elif }c_{g}\in\mathcal{C}_{true}\end{cases} If the LLM predicts False for all choices (i.e. | 𝒞 t ​ r ​ u ​ e | = 0 |\mathcal{C}_{true}|=0 ), it implies uncertainty and equates to random guessing, giving a score of 0.25. Otherwise, if the LLM does not classify the gold answer c g c_{g} as True (i.e. c g ∉ 𝒞 t ​ r ​ u ​ e c_{g}\notin\mathcal{C}_{true} ), the LLM would not select c g c_{g} when given 𝒞 \mathcal{C} , resulting in a score of 0. Lastly, when c g ∈ 𝒞 t ​ r ​ u ​ e c_{g}\in\mathcal{C}_{true} , the LLM’s ability to pick c g c_{g} is akin to guessing among 𝒞 t ​ r ​ u ​ e \mathcal{C}_{true} , yielding a score of 1 | 𝒞 t ​ r ​ u ​ e | \frac{1}{|\mathcal{C}_{true}|} . With this scoring, we can directly compare the group and individual prompt accuracies.

### 5.3 Results

In Figure 4 , on ARC and MMLU, both the group full prompt and its individual counterpart lead in accuracy, followed by the group choices-only prompt and its individual counterpart. The individual full prompt bests the group choices-only prompt, implying that seeing the question is more helpful than seeing all the choices on these datasets. Further, the individual choices-only prompts underperform the group choices-only prompts. Thus, the LLMs’ individual priors alone do not fully explain the choices-only accuracy, suggesting the use of meta-strategies and group dynamics in choices-only settings.

On HellaSwag, the trend varies by model. For LLaMA, the order mirrors ARC/MMLU, but the group choices-only prompt bests the individual full prompt. Hence, for LLaMA, seeing all choices is more informative than the question, and the LLM may still use meta-strategies. In contrast, for Mixtral and Phi, the individual prompts surpass their group versions. This implies that these LLMs may: 1) mainly use individual priors in the choices-only setting; and 2) struggle with the context present in group prompts, due to the dataset’s longer choices.

Takeaway: Partial-input models are often linked to simple shortcuts Du et al. (2023) , such as using statistical cues in individual choices, but we find that LLMs may reason over groups of choices. To study when meta-strategies can effectively be used by LLMs, future works can try to manually control specific properties of distractors (e.g. parity).

## 6 Hypothesis 3: Question Inference

Given the potential use of meta-strategies ( section 5 ), we see if LLMs can use abductive reasoning—giving the best rationale for an observation Peirce (1974) —in choices-only settings. Inspired by work using LLMs to verbalize inferences Hoyle et al. (2023) , we test this via abductive question inference (AQI) . Below, we design ( section 6.1 ), evaluate ( section 6.2 ), and qualitatively analyze ( section 6.3 ) AQI.

### 6.1 Prompt Design

We implement AQI via the two-step process of: 1) generating a question q g ​ e ​ n q_{gen} using the choices 𝒞 \mathcal{C} ; and 2) asking the LLM to pick the correct answer a a to its own question q g ​ e ​ n q_{gen} . Step 1 uses the prompt:

We extract q g ​ e ​ n q_{gen} from Prompt 6.1 5 5 5 The LLM also outputs “ Answer: a \texttt{Answer:}\;a ” after q g ​ e ​ n q_{gen} . We initially wanted AQI to be 1 step where q g ​ e ​ n q_{gen} acts as a chain-of-thought (i.e. merge steps one and two of AQI), but this 1-step process is less effective (see Appendix B.5 ). to perform step two of AQI, where the LLM answers q g ​ e ​ n q_{gen} :

In Prompt 6.1 , the LLM may ignore q g ​ e ​ n q_{gen} , treating it like the choices-only prompt (Prompt 3.1 ). To test this, we design a baseline where the LLM must answer q r ​ a ​ n ​ d q_{rand} , a randomly sampled question from the test set unrelated to the current choices 𝒞 \mathcal{C} :

If the self-ask prompt outperforms the random question prompt, the generated question q g ​ e ​ n q_{gen} provides more useful information than a random question q r ​ a ​ n ​ d q_{rand} , suggesting that the LLM is using q g ​ e ​ n q_{gen} .

### 6.2 Quantitative Results

AQI always results in an accuracy near the choices-only prompt on ARC and MMLU (Figure 5 ). One hypothesis is that the LLMs ignore the generated question q g ​ e ​ n q_{gen} in the self-ask prompt (Prompt 6.1 ), but in 11/12 cases, using the random question q r ​ a ​ n ​ d q_{rand} underperforms q g ​ e ​ n q_{gen} . Thus, q g ​ e ​ n q_{gen} is of higher average quality 6 6 6 It is also possible for q r ​ a ​ n ​ d q_{rand} to be misleading and q g ​ e ​ n q_{gen} to just be irrelevant/non-misleading. However, our qualitative analysis ( section 6.3 ) reveals that q g ​ e ​ n q_{gen} is often answerable by the choices, and thus we claim that it is higher quality than q r ​ a ​ n ​ d q_{rand} . than q r ​ a ​ n ​ d q_{rand} , meaning our LLMs can extract information from q g ​ e ​ n q_{gen} relevant to answering the question. Further, on HellaSwag for Falcon, Phi, and Mixtral, AQI bests the choices-only prompt. AQI is a reasoning-based strategy and thus, future works can try to reason with other strategies Huang and Chang (2023) to see if LLMs can obtain even higher accuracy in choices-only settings.

Since the choices-only prompt and AQI perform similarly, the choices-only prompt may effectively function as the two-step process of AQI. To test this, we use Cohen’s κ \kappa Cohen (1960) to quantify if the choices-only prompt and AQI answer similar questions correctly and incorrectly. The two strategies exhibit moderate agreement (average κ \kappa of 0.32), much higher than a random baseline near 0 (Table 1 ). Thus, while LLMs may implicitly perform AQI in choices-only prompts, we speculate that they may also employ other strategies jointly, such as reasoning over multiple inferred questions.

### 6.3 Qualitative Analysis

In our qualitative analysis, we study the behavior of AQI grouped into three research questions below. We use ARC, as MMLU has questions requiring expert knowledge, and HellaSwag contains multi-sentence questions that are hard to interpret. We study LLaMA’s outputs, but show other LLMs and examples of inferred questions in Appendix B.6 .

Q1—Why can AQI fail : We study when AQI ends up picking the correct (gold) or incorrect (non-gold) choice, sampling 50 cases of each. The two errors of AQI we examine are: 1) generating a question q g ​ e ​ n q_{gen} that cannot be answered by any choice; and 2) selecting a choice a a that does not answer q g ​ e ​ n q_{gen} . We compute IP (Ans), the proportion where q g ​ e ​ n q_{gen} is answerable by one of the choices, and for each answerable q g ​ e ​ n q_{gen} , if the model correctly answers q g ​ e ​ n q_{gen} ( IP (Corr | Ans)). In Table 2 (left), IP (Ans) and IP (Corr | Ans) are high (over 0.8), even when AQI leads to an incorrect answer. Thus, AQI errors with LLaMA mostly stem from inferring questions related to non-gold choices, rather than generating an unanswerable q g ​ e ​ n q_{gen} or incorrectly answering q g ​ e ​ n q_{gen} .

Q2—Can LLMs infer the original question: For each answerable q g ​ e ​ n q_{gen} studied in Q1, we annotate if it matches the meaning of the original question ( IP (Match | Ans)). When a a is incorrect, q g ​ e ​ n q_{gen} never matches the original question, but remarkably, in 43 cases when q g ​ e ​ n q_{gen} is answerable and a a is correct, it matches the original question 42% of the time (Table 2 , right). None of the matches are identical, leading us to believe that this ability is not due to exact memorization. The high rate of matched questions suggests that LLMs may have the ability to verbalize MCQA inferences via abductive reasoning, motivating future works to study the faithfulness of these rationales Turpin et al. (2023) .

Q3— When is AQI effective: We explore the effectiveness of AQI based on the nature of the inferred question q g ​ e ​ n q_{gen} . We sample 100 AQI cases with LLaMA on ARC and mark each q g ​ e ​ n q_{gen} as: 1) unanswerable; 2) answerable and not matching the original question q q ; or 3) answerable and matching q q . To isolate the efficacy of question inference from LLaMA’s ability to answer questions, we have one “oracle” annotator read each q g ​ e ​ n q_{gen} and mark all correct choices 𝒞 a ​ n ​ s ⊆ 𝒞 \mathcal{C}_{ans}\subseteq\mathcal{C} with access to Google. The annotator can mark multiple options as correct to account for when q g ​ e ​ n q_{gen} is ambiguous. The score of this human/LLM team is 0 if the gold answer is not in 𝒞 a ​ n ​ s \mathcal{C}_{ans} , and 1 | 𝒞 a ​ n ​ s | \frac{1}{|\mathcal{C}_{ans}|} if the gold answer is in 𝒞 a ​ n ​ s \mathcal{C}_{ans} .

Table 3 shows that, as expected, the average human/LLM score is 0 when q g ​ e ​ n q_{gen} is unanswerable and 1 when q g ​ e ​ n q_{gen} matches q q . However, when q g ​ e ​ n q_{gen} is answerable and does not match q q , it obtains a score of 0.293—above random guessing (0.25). Thus, even when LLaMA generates a question distinct from the original, it still often pertains to the gold answer, indicating an ability to infer questions relevant to the gold answer beyond random chance.

Takeaway: In some cases, LLMs can use reasoning to reconstruct the question from the choices. AQI is more impressive than the surface-level shortcuts linked with artifacts Du et al. (2023) , but it cannot fully explain choices-only accuracy, meaning that the rest of the choices-only accuracy could be attributed to artifacts and surface-level shortcuts. Thus, while we support artifact-robust evaluations to test LLMs as intended, we also urge researchers to not fully dismiss successful partial-input models Srikanth and Rudinger (2022) , as such models may still employ impressive, unexpected reasoning.

## 7 Related Work

### 7.1 Dataset Artifacts

Data collection protocols can introduce artifacts exploitable by models Du et al. (2023) . Artifacts stem from many sources, such as biases in crowdworkers Gururangan et al. (2018) ; Geva et al. (2019) ; Parmar et al. (2023) or models in synthetic data Yu et al. (2023) . Model reliance on artifacts poses risks, leading to performance overestimation and generalization issues Wiegreffe and Marasović (2021) .

One approach to uncover artifacts is partial-input models Poliak et al. (2018) , which omit parts of inputs. Such models include hypothesis-only models in NLI Poliak et al. (2018) ; Herlihy and Rudinger (2021) ; Srikanth and Rudinger (2022) , passage-only models in reading comprehension Kaushik and Lipton (2018) ; Shah et al. (2020) , and question-only models in visual QA Goyal et al. (2017) .

Other methods to find artifacts include text perturbations Feng et al. (2019) ; Sugawara et al. (2019) ; Gardner et al. (2020) , adversarial data Jia and Liang (2017) ; Wallace et al. (2019) ; Morris et al. (2020) , and probing experiments Glockner et al. (2018) ; McCoy et al. (2019) . To limit artifacts and reliably assess models, works have used special training objectives Belinkov et al. (2019) ; Mersinias and Valvis (2022) , debiasing procedures Ravichander et al. (2023) , human-AI data collection Liu et al. (2022) , and context altering to flip model decisions Srikanth and Rudinger (2022) ; Elazar et al. (2023) .

Conversely, we show that LLMs can obtain high partial-input MCQA accuracy with few examples.

### 7.2 MCQA Decision Making

We study three facets of MCQA decision making: memorization, choice dynamics, and question inference. Each has been explored in prior works.

Several works quantify memorization via data extraction attacks Carlini et al. (2020) ; Ishihara (2023) ; Sainz et al. (2023) and analyzing models after dataset-specific training Huang et al. (2022) ; Zhou et al. (2023) . In contrast, we design the first partial-input memorization prompts for MCQA.

While many works study how humans make informed or cued MCQA guesses via choice dynamics Royal and Hedgpeth (2015) ; Royal and Stockdale (2017) , we are the first to define similar abilities (i.e. meta-strategies) with LLMs. Other studies assess if LLM pretraining priors can recognize tasks Pan et al. (2023) and sensitivity to option order in MCQA Pezeshkpour and Hruschka (2023) , but neither work focuses on dataset artifacts.

Lastly, prior works explore generating entire MC questions Ch and Saha (2018) , but we are the first to use LLMs to infer the original question from the choices. Other MC strategies have been used with LLMs, such as process of elimination Ma and Du (2023) ; Balepur et al. (2023) , where wrong options are removed, and Maieutic Prompting Jung et al. (2022) , involving reasoning over abductive explanations, but not in relation to artifact exploitation.

## 8 Conclusion

We find that LLMs can perform MCQA without access to the question, a result that can be achieved through few-shot prompting with minimal examples. In pursuing explanations for these results, we release an in-depth black-box evaluation suite, based on our proposed partial-input prompts. As part of our analysis, we show that LLMs still exhibit reasoning abilities in choices-only settings via the meta-strategy of question inference, suggesting that partial-input abilities of LLMs should not be completely attributed to surface-level shortcuts linked to artifacts. Along with software and analysis, we suggest ways to evaluate LLMs on MCQA as intended, where both the question and choices are needed, including: 1) reporting stronger baselines like our proposed choices-only prompt; and 2) designing robust data creation protocols. In light of our findings, we advocate for more critical discussions around LLM evaluation, allowing us to better understand and interpret the model capabilities our benchmarks are truly assessing.

## 9 Limitations

One limitation is that our experiments are conducted in a black-box rather than a white-box manner, motivated by the increasing use of closed-source LLMs. This setup allows our analysis to be applicable to any LLM that can provide generated text outputs through prompting. However, we acknowledge that an analysis of logits from open-source LLMs could offer more insights into aspects like confidence, uncertainty, and calibration in artifact exploitation. We believe these directions would be very interesting extensions of our work.

Our experiments also do not use closed-source models like ChatGPT due to resource constraints. Based on the large number of prompts we study, we need to run inference over each MCQA dataset 16 times. This is a very expensive endeavor, as two of our datasets, MMLU and HellaSwag, both have over 10,000 questions in the test set. However, all of our experiments are designed in a black-box fashion and will be made open-source. Thus, we hope if members of the NLP community with access to more resources are interested, they can replicate our experiments with closed-source LLMs.

Lastly, LLMs are sensitive to prompts Min et al. (2022) and hyperparameters, so it is possible that varied configurations could alter the accuracy in our experiments. Our prompts and hyperparameters were just the first ones we tried, so we believe that LLMs can likely be optimized to obtain even higher choices-only accuracy. Future works can explore these alterations more in-depth and analyze LLM sensitivity in choices-only settings.

## 10 Ethical Considerations

Through few-shot prompting, we discover that LLMs can achieve high choices-only accuracy in prominent MCQA benchmark datasets. However, our goal is not to discount the adoption of these datasets for evaluation and suggest that they are fundamentally flawed, or discredit the performance of LLMs on these datasets and claim that they are incapable of performing MCQA. Instead, we wish to provide more transparency for MCQA benchmarking and LLM decision-making, which we hope will inspire future work on: 1) better understanding LLM decision-making in MCQA; 2) reporting choices-only baselines as a stronger alternative to majority class baselines on MCQA evaluation suites; and 3) designing more resilient benchmarks that limit the influence of artifacts.

## 11 Acknowledgements

We would like to thank members of the CLIP lab at the University of Maryland and external collaborators for their feedback and discussions of this work, including Yu (Hope) Hou, Dayeon (Zoey) Ki, Neha Srikanth, Rupak Sarkar, Shi Feng, and Jordan Boyd-Graber. We are also grateful for our discussions with Hailey Schoelkopf, Stella Biderman, and other members of the EleutherAI community. We also thank the anonymous reviewers for their feedback. This material is based upon work supported by the National Science Foundation Graduate Research Fellowship Program under Grant No. DGE 2236417. Any opinions, findings, and conclusions or recommendations expressed in this material are those of the author(s) and do not necessarily reflect the views of the National Science Foundation.

## References

Abdin et al. (2023) Marah Abdin, Jyoti Aneja, Sebastien Bubeck, Caio César Teodoro Mendes, Weizhu Chen, Allie Del Giorno, Ronen Eldan, Sivakanth Gopi, Suriya Gunasekar, Mojan Javaheripi, Piero Kauffmann, Yin Tat Lee, Yuanzhi Li, Anh Nguyen, Gustavo de Rosa, Olli Saarikivi, Adil Salim, Shital Shah, Michael Santacroce, Harkirat Singh Behl, Adam Taumann Kalai, Xin Wang, Rachel Ward, Philipp Witte, Cyril Zhang, and Yi Zhang. 2023. Phi-2: The surprising power of small language models . Microsoft Research Blog .

Alzahrani et al. (2024) Norah Alzahrani, Hisham Abdullah Alyahya, Yazeed Alnumay, Sultan Alrashed, Shaykhah Alsubaie, Yusef Almushaykeh, Faisal Mirza, Nouf Alotaibi, Nora Altwairesh, Areeb Alowisheq, et al. 2024. When benchmarks are targets: Revealing the sensitivity of large language model leaderboards. arXiv preprint arXiv:2402.01781 .

Balepur et al. (2023) Nishant Balepur, Shramay Palta, and Rachel Rudinger. 2023. It’s not easy being wrong: Evaluating process of elimination reasoning in large language models. arXiv preprint arXiv:2311.07532 .

Beeching et al. (2023) Edward Beeching, Clémentine Fourrier, Nathan Habib, Sheon Han, Nathan Lambert, Nazneen Rajani, Omar Sanseviero, Lewis Tunstall, and Thomas Wolf. 2023. Open llm leaderboard. https://huggingface.co/spaces/HuggingFaceH4/open_llm_leaderboard .

Belinkov et al. (2019) Yonatan Belinkov, Adam Poliak, Stuart Shieber, Benjamin Van Durme, and Alexander Rush. 2019. Don’t take the premise for granted: Mitigating artifacts in natural language inference . In Proceedings of the 57th Annual Meeting of the Association for Computational Linguistics , pages 877–891, Florence, Italy. Association for Computational Linguistics.

Ben-Simon et al. (1997) Anat Ben-Simon, David V Budescu, and Baruch Nevo. 1997. A comparative study of measures of partial knowledge in multiple-choice tests. Applied Psychological Measurement , 21(1):65–88.

Bhagavatula et al. (2020) Chandra Bhagavatula, Ronan Le Bras, Chaitanya Malaviya, Keisuke Sakaguchi, Ari Holtzman, Hannah Rashkin, Doug Downey, Wen tau Yih, and Yejin Choi. 2020. Abductive commonsense reasoning . In International Conference on Learning Representations .

Carlini et al. (2020) Nicholas Carlini, Florian Tramèr, Eric Wallace, Matthew Jagielski, Ariel Herbert-Voss, Katherine Lee, Adam Roberts, Tom B. Brown, Dawn Xiaodong Song, Úlfar Erlingsson, Alina Oprea, and Colin Raffel. 2020. Extracting training data from large language models . In USENIX Security Symposium .

Ch and Saha (2018) Dhawaleswar Rao Ch and Sujan Kumar Saha. 2018. Automatic multiple choice question generation from text: A survey. IEEE Transactions on Learning Technologies , 13(1):14–25.

Clark et al. (2018) Peter Clark, Isaac Cowhey, Oren Etzioni, Tushar Khot, Ashish Sabharwal, Carissa Schoenick, and Oyvind Tafjord. 2018. Think you have solved question answering? try arc, the ai2 reasoning challenge. arXiv preprint arXiv:1803.05457 .

Cohen (1960) Jacob Cohen. 1960. A coefficient of agreement for nominal scales. Educational and psychological measurement , 20(1):37–46.

Du et al. (2023) Mengnan Du, Fengxiang He, Na Zou, Dacheng Tao, and Xia Hu. 2023. Shortcut learning of large language models in natural language understanding. Communications of the ACM , 67(1):110–120.

Elazar et al. (2023) Yanai Elazar, Bhargavi Paranjape, Hao Peng, Sarah Wiegreffe, Khyathi Raghavi, Vivek Srikumar, Sameer Singh, and Noah A Smith. 2023. Measuring and improving attentiveness to partial inputs with counterfactuals. arXiv preprint arXiv:2311.09605 .

Feng et al. (2019) Shi Feng, Eric Wallace, and Jordan Boyd-Graber. 2019. Misleading failures of partial-input baselines . In Proceedings of the 57th Annual Meeting of the Association for Computational Linguistics , pages 5533–5538, Florence, Italy. Association for Computational Linguistics.

Gardner et al. (2020) Matt Gardner, Yoav Artzi, Victoria Basmov, Jonathan Berant, Ben Bogin, Sihao Chen, Pradeep Dasigi, Dheeru Dua, Yanai Elazar, Ananth Gottumukkala, Nitish Gupta, Hannaneh Hajishirzi, Gabriel Ilharco, Daniel Khashabi, Kevin Lin, Jiangming Liu, Nelson F. Liu, Phoebe Mulcaire, Qiang Ning, Sameer Singh, Noah A. Smith, Sanjay Subramanian, Reut Tsarfaty, Eric Wallace, Ally Zhang, and Ben Zhou. 2020. Evaluating models’ local decision boundaries via contrast sets . In Findings of the Association for Computational Linguistics: EMNLP 2020 , pages 1307–1323, Online. Association for Computational Linguistics.

Geva et al. (2019) Mor Geva, Yoav Goldberg, and Jonathan Berant. 2019. Are we modeling the task or the annotator? an investigation of annotator bias in natural language understanding datasets . In Proceedings of the 2019 Conference on Empirical Methods in Natural Language Processing and the 9th International Joint Conference on Natural Language Processing (EMNLP-IJCNLP) , pages 1161–1166, Hong Kong, China. Association for Computational Linguistics.

Glockner et al. (2018) Max Glockner, Vered Shwartz, and Yoav Goldberg. 2018. Breaking NLI systems with sentences that require simple lexical inferences . In Proceedings of the 56th Annual Meeting of the Association for Computational Linguistics (Volume 2: Short Papers) , pages 650–655, Melbourne, Australia. Association for Computational Linguistics.

Goyal et al. (2017) Yash Goyal, Tejas Khot, Douglas Summers-Stay, Dhruv Batra, and Devi Parikh. 2017. Making the v in vqa matter: Elevating the role of image understanding in visual question answering. In Proceedings of the IEEE conference on computer vision and pattern recognition , pages 6904–6913.

Gururangan et al. (2018) Suchin Gururangan, Swabha Swayamdipta, Omer Levy, Roy Schwartz, Samuel Bowman, and Noah A. Smith. 2018. Annotation artifacts in natural language inference data . In Proceedings of the 2018 Conference of the North American Chapter of the Association for Computational Linguistics: Human Language Technologies, Volume 2 (Short Papers) , pages 107–112, New Orleans, Louisiana. Association for Computational Linguistics.

Hendrycks et al. (2021) Dan Hendrycks, Collin Burns, Steven Basart, Andy Zou, Mantas Mazeika, Dawn Song, and Jacob Steinhardt. 2021. Measuring massive multitask language understanding . In International Conference on Learning Representations .

Herlihy and Rudinger (2021) Christine Herlihy and Rachel Rudinger. 2021. MedNLI is not immune: Natural language inference artifacts in the clinical domain . In Proceedings of the 59th Annual Meeting of the Association for Computational Linguistics and the 11th International Joint Conference on Natural Language Processing (Volume 2: Short Papers) , pages 1020–1027, Online. Association for Computational Linguistics.

Hoyle et al. (2023) Alexander Hoyle, Rupak Sarkar, Pranav Goel, and Philip Resnik. 2023. Natural language decompositions of implicit content enable better text representations . In Proceedings of the 2023 Conference on Empirical Methods in Natural Language Processing , pages 13188–13214, Singapore. Association for Computational Linguistics.

Huang and Chang (2023) Jie Huang and Kevin Chen-Chuan Chang. 2023. Towards reasoning in large language models: A survey . In Findings of the Association for Computational Linguistics: ACL 2023 , pages 1049–1065, Toronto, Canada. Association for Computational Linguistics.

Huang et al. (2022) Jie Huang, Hanyin Shao, and Kevin Chen-Chuan Chang. 2022. Are large pre-trained language models leaking your personal information? In Findings of the Association for Computational Linguistics: EMNLP 2022 , pages 2038–2047, Abu Dhabi, United Arab Emirates. Association for Computational Linguistics.

Ishihara (2023) Shotaro Ishihara. 2023. Training data extraction from pre-trained language models: A survey . In Proceedings of the 3rd Workshop on Trustworthy Natural Language Processing (TrustNLP 2023) , pages 260–275, Toronto, Canada. Association for Computational Linguistics.

Jia and Liang (2017) Robin Jia and Percy Liang. 2017. Adversarial examples for evaluating reading comprehension systems . In Proceedings of the 2017 Conference on Empirical Methods in Natural Language Processing , pages 2021–2031, Copenhagen, Denmark. Association for Computational Linguistics.

Jiang et al. (2024) Albert Q. Jiang, Alexandre Sablayrolles, Antoine Roux, Arthur Mensch, Blanche Savary, Chris Bamford, Devendra Singh Chaplot, Diego de las Casas, Emma Bou Hanna, Florian Bressand, Gianna Lengyel, Guillaume Bour, Guillaume Lample, Lélio Renard Lavaud, Lucile Saulnier, Marie-Anne Lachaux, Pierre Stock, Sandeep Subramanian, Sophia Yang, Szymon Antoniak, Teven Le Scao, Théophile Gervet, Thibaut Lavril, Thomas Wang, Timothée Lacroix, and William El Sayed. 2024. Mixtral of experts .

Jung et al. (2022) Jaehun Jung, Lianhui Qin, Sean Welleck, Faeze Brahman, Chandra Bhagavatula, Ronan Le Bras, and Yejin Choi. 2022. Maieutic prompting: Logically consistent reasoning with recursive explanations . In Proceedings of the 2022 Conference on Empirical Methods in Natural Language Processing , pages 1266–1279, Abu Dhabi, United Arab Emirates. Association for Computational Linguistics.

Kaushik and Lipton (2018) Divyansh Kaushik and Zachary C. Lipton. 2018. How much reading does reading comprehension require? a critical investigation of popular benchmarks . In Proceedings of the 2018 Conference on Empirical Methods in Natural Language Processing , pages 5010–5015, Brussels, Belgium. Association for Computational Linguistics.

Kojima et al. (2022) Takeshi Kojima, Shixiang (Shane) Gu, Machel Reid, Yutaka Matsuo, and Yusuke Iwasawa. 2022. Large language models are zero-shot reasoners . In Advances in Neural Information Processing Systems , volume 35, pages 22199–22213. Curran Associates, Inc.

Levesque et al. (2011) Hector J. Levesque, Ernest Davis, and L. Morgenstern. 2011. The winograd schema challenge . In AAAI Spring Symposium: Logical Formalizations of Commonsense Reasoning .

Liang et al. (2023) Percy Liang, Rishi Bommasani, Tony Lee, Dimitris Tsipras, Dilara Soylu, Michihiro Yasunaga, Yian Zhang, Deepak Narayanan, Yuhuai Wu, Ananya Kumar, Benjamin Newman, Binhang Yuan, Bobby Yan, Ce Zhang, Christian Alexander Cosgrove, Christopher D Manning, Christopher Re, Diana Acosta-Navas, Drew Arad Hudson, Eric Zelikman, Esin Durmus, Faisal Ladhak, Frieda Rong, Hongyu Ren, Huaxiu Yao, Jue WANG, Keshav Santhanam, Laurel Orr, Lucia Zheng, Mert Yuksekgonul, Mirac Suzgun, Nathan Kim, Neel Guha, Niladri S. Chatterji, Omar Khattab, Peter Henderson, Qian Huang, Ryan Andrew Chi, Sang Michael Xie, Shibani Santurkar, Surya Ganguli, Tatsunori Hashimoto, Thomas Icard, Tianyi Zhang, Vishrav Chaudhary, William Wang, Xuechen Li, Yifan Mai, Yuhui Zhang, and Yuta Koreeda. 2023. Holistic evaluation of language models . Transactions on Machine Learning Research . Featured Certification, Expert Certification.

Liu et al. (2022) Alisa Liu, Swabha Swayamdipta, Noah A. Smith, and Yejin Choi. 2022. WANLI: Worker and AI collaboration for natural language inference dataset creation . In Findings of the Association for Computational Linguistics: EMNLP 2022 , pages 6826–6847, Abu Dhabi, United Arab Emirates. Association for Computational Linguistics.

Ma and Du (2023) Chenkai Ma and Xinya Du. 2023. POE: Process of elimination for multiple choice reasoning . In Proceedings of the 2023 Conference on Empirical Methods in Natural Language Processing , pages 4487–4496, Singapore. Association for Computational Linguistics.

McCoy et al. (2019) R. Thomas McCoy, Ellie Pavlick, and Tal Linzen. 2019. Right for the wrong reasons: Diagnosing syntactic heuristics in natural language inference . In Annual Meeting of the Association for Computational Linguistics .

Mersinias and Valvis (2022) Michail Mersinias and Panagiotis Valvis. 2022. Mitigating dataset artifacts in natural language inference through automatic contextual data augmentation and learning optimization . In International Conference on Language Resources and Evaluation .

Min et al. (2022) Sewon Min, Xinxi Lyu, Ari Holtzman, Mikel Artetxe, Mike Lewis, Hannaneh Hajishirzi, and Luke Zettlemoyer. 2022. Rethinking the role of demonstrations: What makes in-context learning work? In Proceedings of the 2022 Conference on Empirical Methods in Natural Language Processing , pages 11048–11064, Abu Dhabi, United Arab Emirates. Association for Computational Linguistics.

Morris et al. (2020) John Morris, Eli Lifland, Jin Yong Yoo, Jake Grigsby, Di Jin, and Yanjun Qi. 2020. TextAttack: A framework for adversarial attacks, data augmentation, and adversarial training in NLP . In Proceedings of the 2020 Conference on Empirical Methods in Natural Language Processing: System Demonstrations , pages 119–126, Online. Association for Computational Linguistics.

Pan et al. (2023) Jane Pan, Tianyu Gao, Howard Chen, and Danqi Chen. 2023. What in-context learning "learns" in-context: Disentangling task recognition and task learning . In Annual Meeting of the Association for Computational Linguistics .

Parmar et al. (2023) Mihir Parmar, Swaroop Mishra, Mor Geva, and Chitta Baral. 2023. Don’t blame the annotator: Bias already starts in the annotation instructions . In Proceedings of the 17th Conference of the European Chapter of the Association for Computational Linguistics , pages 1779–1789, Dubrovnik, Croatia. Association for Computational Linguistics.

Peirce (1974) Charles Sanders Peirce. 1974. Collected papers of charles sanders peirce , volume 1. Harvard University Press.

Penedo et al. (2023) Guilherme Penedo, Quentin Malartic, Daniel Hesslow, Ruxandra Cojocaru, Hamza Alobeidli, Alessandro Cappelli, Baptiste Pannier, Ebtesam Almazrouei, and Julien Launay. 2023. The refinedweb dataset for falcon LLM: Outperforming curated corpora with web data only . In Thirty-seventh Conference on Neural Information Processing Systems Datasets and Benchmarks Track .

Pezeshkpour and Hruschka (2023) Pouya Pezeshkpour and Estevam Hruschka. 2023. Large language models sensitivity to the order of options in multiple-choice questions . ArXiv , abs/2308.11483.

Poliak et al. (2018) Adam Poliak, Jason Naradowsky, Aparajita Haldar, Rachel Rudinger, and Benjamin Van Durme. 2018. Hypothesis only baselines in natural language inference . In Proceedings of the Seventh Joint Conference on Lexical and Computational Semantics , pages 180–191, New Orleans, Louisiana. Association for Computational Linguistics.

Raffel et al. (2019) Colin Raffel, Noam M. Shazeer, Adam Roberts, Katherine Lee, Sharan Narang, Michael Matena, Yanqi Zhou, Wei Li, and Peter J. Liu. 2019. Exploring the limits of transfer learning with a unified text-to-text transformer . J. Mach. Learn. Res. , 21:140:1–140:67.

Ravichander et al. (2023) Abhilasha Ravichander, Joe Stacey, and Marek Rei. 2023. When and why does bias mitigation work? In Findings of the Association for Computational Linguistics: EMNLP 2023 , pages 9233–9247, Singapore. Association for Computational Linguistics.

Robinson and Wingate (2023) Joshua Robinson and David Wingate. 2023. Leveraging large language models for multiple choice question answering . In The Eleventh International Conference on Learning Representations .

Royal and Hedgpeth (2015) Kenneth D Royal and Mari-Wells Hedgpeth. 2015. A novel method for evaluating examination item quality. International Journal of Psychological Studies , 7(1):17.

Royal and Stockdale (2017) Kenneth D Royal and Myrah R Stockdale. 2017. The impact of 3-option responses to multiple-choice questions on guessing strategies and cut score determinations. Journal of Advances in Medical Education & Professionalism , 5(2):84.

Sainz et al. (2023) Oscar Sainz, Jon Ander Campos, Iker García-Ferrero, Julen Etxaniz, and Eneko Agirre. 2023. Did chatgpt cheat on your test?

Shah et al. (2020) Krunal Shah, Nitish Gupta, and Dan Roth. 2020. What do we expect from multiple-choice QA systems? In Findings of the Association for Computational Linguistics: EMNLP 2020 , pages 3547–3553, Online. Association for Computational Linguistics.

Srikanth and Rudinger (2022) Neha Srikanth and Rachel Rudinger. 2022. Partial-input baselines show that NLI models can ignore context, but they don’t. In Proceedings of the 2022 Conference of the North American Chapter of the Association for Computational Linguistics: Human Language Technologies , pages 4753–4763, Seattle, United States. Association for Computational Linguistics.

Sugawara et al. (2019) Saku Sugawara, Pontus Stenetorp, Kentaro Inui, and Akiko Aizawa. 2019. Assessing the benchmarking capacity of machine reading comprehension datasets . In AAAI Conference on Artificial Intelligence .

Touvron et al. (2023) Hugo Touvron, Louis Martin, Kevin Stone, Peter Albert, Amjad Almahairi, Yasmine Babaei, Nikolay Bashlykov, Soumya Batra, Prajjwal Bhargava, Shruti Bhosale, et al. 2023. Llama 2: Open foundation and fine-tuned chat models. arXiv preprint arXiv:2307.09288 .

Turpin et al. (2023) Miles Turpin, Julian Michael, Ethan Perez, and Sam Bowman. 2023. Language models don’t always say what they think: Unfaithful explanations in chain-of-thought prompting . ArXiv , abs/2305.04388.

Wallace et al. (2019) Eric Wallace, Shi Feng, Nikhil Kandpal, Matt Gardner, and Sameer Singh. 2019. Universal adversarial triggers for attacking and analyzing nlp . In Conference on Empirical Methods in Natural Language Processing .

Wang et al. (2024) Haochun Wang, Sendong Zhao, Zewen Qiang, Bing Qin, and Ting Liu. 2024. Beyond the answers: Reviewing the rationality of multiple choice question answering for the evaluation of large language models. arXiv preprint arXiv:2402.01349 .

Wei et al. (2022) Jason Wei, Xuezhi Wang, Dale Schuurmans, Maarten Bosma, Fei Xia, Ed Chi, Quoc V Le, Denny Zhou, et al. 2022. Chain-of-thought prompting elicits reasoning in large language models. Advances in Neural Information Processing Systems , 35:24824–24837.

Wiegreffe and Marasović (2021) Sarah Wiegreffe and Ana Marasović. 2021. Teach me to explain: A review of datasets for explainable natural language processing . In NeurIPS Datasets and Benchmarks .

Yu et al. (2023) Yue Yu, Yuchen Zhuang, Jieyu Zhang, Yu Meng, Alexander Ratner, Ranjay Krishna, Jiaming Shen, and Chao Zhang. 2023. Large language model as attributed training data generator: A tale of diversity and bias. In Thirty-Seventh Conference on Neural Information Processing Systems Datasets and Benchmarks Track .

Zellers et al. (2019) Rowan Zellers, Ari Holtzman, Yonatan Bisk, Ali Farhadi, and Yejin Choi. 2019. Hellaswag: Can a machine really finish your sentence? In Annual Meeting of the Association for Computational Linguistics .

Zheng et al. (2024) Chujie Zheng, Hao Zhou, Fandong Meng, Jie Zhou, and Minlie Huang. 2024. Large language models are not robust multiple choice selectors . In The Twelfth International Conference on Learning Representations .

Zhou et al. (2023) Kun Zhou, Yutao Zhu, Zhipeng Chen, Wentong Chen, Wayne Xin Zhao, Xu Chen, Yankai Lin, Jinhui Wen, and Jiawei Han. 2023. Don’t make your llm an evaluation benchmark cheater . ArXiv , abs/2311.01964.

## Appendix A Experimental Setup

### A.1 Dataset Details

All datasets were obtained from their original, publicly-available sources. These datasets are free to use for research purposes, so our research falls within their intended use. ARC uses 25 training examples (20 for Falcon) and 1165 evaluation examples; MMLU uses 5 training examples and 14032 evaluation examples; and HellaSwag uses 10 training examples and 10042 evaluation examples.

### A.2 LLM Inference

For LLaMA, Falcon, and Mixtral we allocated 24 GPU hours for almost every prompt format and dataset, and used 8 NVIDIA:RTXA5000 GPUs. The notable exception is the two-step inferring the question strategy, which required 48 GPU hours for LLaMA and Falcon, and 96 GPU hours for Falcon, per model and dataset. Phi required around 60 total GPU hours to run all prompt formats per dataset, and used a single NVIDIA:RTXA4000 GPU.

The only parameters changed are: a minimum token generation length of 5, a maximum token generation length of 200, and a stopping criteria when the LLM begins to generate the next few-shot exemplar. For LLaMA-2 on MMLU, we use 8-bit quantization. We did not perform hyperparameter search. All results are obtained from a single run.

### A.3 Prompt Creation

Given the sensitivity of LLMs to prompt formats, we followed best practices when creating our few-shot prompts. For ARC, we randomly sample 25 examples over the entire training set. The HellaSwag dataset stems from two sources: ActivityNet and wikiHow. Thus, the 10-shot prompt contains 5 randomly sampled examples from the ActivityNet portion of the dataset, and 5 randomly sampled examples from the wikiHow portion. Further, we ensure that each few-shot prompt has a balanced distribution of answer letters and that the order of exemplars is randomized.

All prompts shown in this paper are derived from these few-shot examples, following the format shown in the prompt boxes. Two slight exceptions are when the LLM performs the second step of AQI (Prompt 6.1 ) and answers a random question (Prompt 6.1 ). In these prompts, the questions in the few-shot examples are the same as the questions from the Full Prompt (Prompt 2.1 ), rather than using model-generated and random questions (respectively), ensuring a fair comparison.

### A.4 Prompt Box Example

Below, we provide a detailed example to illustrate the application of our prompt boxes. Suppose we have the full prompt (Prompt 2.1 ) defined in section 2.1 :

In the above prompt, the LLM uses the question q q and choices 𝒞 \mathcal{C} as input and is asked to generate the letter of the answer a a . Suppose we have 5 few-shot examples, with questions q 1 q_{1} ,…, q 5 q_{5} , list of choices 𝒞 1 \mathcal{C}_{1} , …, 𝒞 5 \mathcal{C}_{5} , and ground truth answers a 1 a_{1} , …, a 5 a_{5} . The expanded few-shot prompt for the prompt box is written below:

Using this prompt, the LLM must generate a a , which is the highlighted text in the prompt box.

### A.5 Output Validity Statistics

In Table 4 , we display the output validity statistics (i.e. if the model selects a valid letter) of each prompt format, LLM, and dataset used in our experiments. We find that in 100/108 cases, the LLMs produce valid outputs over 95% of the time. This suggests that our few-shot prompt setup typically enables the LLM to produce valid outputs.

Further, we display the results from our experiments if invalid outputs are always marked as incorrect in Figures 13 , 14 , and 15 . We believe either decision regarding the treatment of invalid options is valid, but we opted for the score of 0.25 to account for task misunderstanding stemming from our atypical prompt formats. Regardless, we provide both versions of the experiments so readers can comprehensively evaluate the LLMs.

### A.6 Metrics

Accuracy was computed with numpy. 7 7 7 https://numpy.org/ Cohen’s κ \kappa was computed with scikit-learn. 8 8 8 https://scikit-learn.org/ All metrics are reported from a single run.

## Appendix B Detailed Results

### B.1 Scaling Laws

In Figure 6 , we perform the same initial experiments on choices-only prompts in section 3 with LLaMA-2 models of three sizes: 7B, 13B, and 70B. Overall, we find that as model size increases, the accuracy of the choices-only prompt also increases. This again suggests that larger models may exploit artifacts to a higher degree.

### B.2 Decoding Strategies

In our experiments, we use default parameters to show the out-of-box results of our tested LLMs. To study the effect of decoding strategies, we re-run our choices-only, memorization, and individual prior experiments with LLaMA on all datasets using greedy decoding, displayed in Figures 7 , 8 , and 9 , respectively. We find that our results are mostly consistent, suggesting that the choice of decoding strategy does not significantly influence the results. The one notable difference is that the individual choice-only prompt results in a higher accuracy with greedy decoding on all the datasets. Despite this increase, the individual choice classification still does not fully explain the accuracy of the choices-only prompt, which suggests that LLMs may still use group dynamics and meta-strategies, even with greedy decoding.

### B.3 Partial-input Models vs Prompting

We compare the performance of our partial-input prompts versus a trainable partial-input model. We train the seq2seq T5-Large model Raffel et al. (2019) to perform MCQA using the same input sequence format as the full prompt (Prompt 2.1 ) and the choices-only prompt (Prompt 3.1 ). T5 is independently trained on ARC and HellaSwag using 90% of the training set for training (with default parameters) and the other 10% for validation.

The T5 model has less pretraining compared to our LLMs, so a trainable T5 choices-only baseline mainly exploits annotation artifacts (e.g. common words used by crowdworkers), rather than artifacts from pretraining (i.e. world knowledge). If an LLM with the choices-only prompt can outperform T5, it would signify that the LLM is instead leveraging knowledge from pretraining.

In Figure 10 , we find that on ARC, T5 is unable to exploit artifacts in the choices-only setting, achieving an accuracy very close to the majority class baseline. This indicates that our tested LLMs can achieve high choices-only accuracy on ARC due to their extensive pretraining, rather than leveraging statistical dataset correlations. On HellaSwag, however, there is a large presence of dataset artifacts, indicated by the high choices-only accuracy of T5 of 0.721. Future works can conduct more in-depth analysis to try to uncover how pretraining relates to artifact exploitation.

### B.4 Falcon Individual Evaluation

In Figure 11 , we show the accuracy of the individual versus group choice experiments from section 5.3 . Falcon performs very poorly on the independent classification task, achieving scores near the majority class baseline in ARC and HellaSwag. Falcon is one of the weaker models we test with, so we attribute this behavior to the LLM’s less robust overall capabilities compared to our other LLMs.

### B.5 One-Step Question Inference

Figure 12 displays the accuracy of the two-step versus one-step strategy of abductive question inference ( section 6 ); in the latter, the generated question acts as a chain-of-thought Wei et al. (2022) . We find that the one-step strategy consistently underperforms its two-step version, signifying that instructing an LLM to try to infer the question and then answer this question in one step is too difficult of a task.

### B.6 Qualitative Analysis

In this section, we provide more details regarding the annotation procedure details ( section B.6.1 ) as well as additional results that we could not fit into the main body of the paper ( section B.6.2 ).

#### B.6.1 Annotation Procedure Details

In Q1, we verify if the model’s selected answer is correct using external tools such as Google search. Further, when the model generates an ambiguous question that is answerable by many choices (e.g. “Which of these is a liquid?” with choices “milk” and “water”), if the model selects any of the correct options we mark it as correct.

In Q2, when we study if the inferred questions match the original question, we define two questions as having the same meaning if they test the same knowledge. To illustrate, in one instance, the generated question is “ If there is a high demand for lumber and a low supply of trees, what will most likely happen? ” and the original question is “ Logging companies cut trees in a forest and send the trees to lumber mills far from the forest. The mills make boards that are used for construction. Some logging companies do not plant tree seedlings after cutting trees. Not planting tree seedlings might affect people who need boards in the future because .” We consider these two questions to be equivalent because they both fundamentally ask the model to reason about what happens if demand for lumber increases but supply decreases.

All annotators in Q1, Q2, and Q3 are the authors, ensuring that the annotations are high-quality.

#### B.6.2 Additional Results

In Table 6 , we provide the qualitative evaluation results Q1 and Q2 with all of our tested LLMs (LLaMA, Falcon, Mixtral, and Phi) on ARC. We note that all models showcase a similar trend discussed in section 6.2 , but Phi is notably much worse at inferring the question. This is expected, given that Phi is the smallest LLM used in our experiments.

We now give further analyses for LLaMA on ARC regarding when AQI is effective (Q3). First, the breakdown of our three cases for the generated question is: 15% as unanswerable, 28% as answerable and matching the original question, and the remaining 57% as answerable and not matching the original question. In terms of question discriminability, we find that 15% can be answered by none of the choices (i.e. unanswerable), 65% can be answered by exactly one of the choices (i.e. perfectly discriminable), and the last 20% can be answered by more than one choice (i.e. ambiguous).

Finally, we provide examples of questions generated from AQI. In Tables 7 and 8 , we show generated questions when inferring the question succeeds, and the generated question matches and does not match the original question, respectively. In Table 9 , we show generated questions when inferring the question fails, but the question is still answerable.

## Appendix C Related Work on MCQA Evaluations

Several recent works investigate the reliability of using MCQA to evaluate LLMs. However, the overwhelming majority of these experiments focus solely on prompt sensitivity and LLM robustness Zheng et al. (2024) ; Pezeshkpour and Hruschka (2023) ; Wang et al. (2024) ; Alzahrani et al. (2024) , collectively pointing out that LLM performance on MCQA can substantially change if the in-context examples, choice order, and symbols used to denote options, among other properties, are altered. Conversely, we focus on the issue of artifact exploitation , allowing us to holistically assess MCQA tasks and datasets, rather than the different ways LLMs can be implemented to perform MCQA.

## Instructions for reporting errors

We are continuing to improve HTML versions of papers, and your feedback helps enhance accessibility and mobile support. To report errors in the HTML that will help us improve conversion and rendering, choose any of the methods listed below:

Click the "Report Issue" ( ) button, located in the page header.

Tip: You can select the relevant text first, to include it in your report.

Our team has already identified the following issues . We appreciate your time reviewing and reporting rendering errors we may not have found yet. Your efforts will help us improve the HTML versions for all readers, because disability should not be a barrier to accessing research. Thank you for your continued support in championing open access for all.

Have a free development cycle? Help support accessibility at arXiv! Our collaborators at LaTeXML maintain a list of packages that need conversion , and welcome developer contributions .
