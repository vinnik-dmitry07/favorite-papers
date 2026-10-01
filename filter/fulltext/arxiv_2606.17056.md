##### Report GitHub Issue

Content selection saved. Describe the issue below:

# The Value Axis: Language Models Encode Whether They’re on the Right Track

###### Abstract

We investigate whether language models internally track the value of their current trajectory, defined as the likelihood that their ongoing strategy will achieve their goals. Using synthetic, in-context reinforcement learning data, we construct a "value" axis for Qwen3-8B. We find that activations along this axis distinguish between high vs. low verbalized confidence, rollouts without and with backtracking, and correct vs. corrupted code. Steering towards high value causally suppresses self-correction and reduces explanatory verbosity, while steering towards low value induces backtracking and exploration. We demonstrate that direct preference optimization (DPO) can increase the internal value of rewarded behaviors (e.g. use a certain word), causing the model to act more confidently after exhibiting them. Finally, we apply the value axis to study in-the-wild settings. For example, we find that Qwen assigns low value to politically sensitive chat queries after post-training and that supervised fine-tuning increases internal confidence within the training domain. Our results suggest that language models linearly encode an estimate of expected goal success that modulates their confidence in pursuing a direction. 1 1 1 Code: https://github.com/nickjiang2378/value-axis

## 1 Introduction

Models are trained to perform long-running tasks (e.g., coding) that involve intermediate decisions about which directions to take ( Kwa et al., 2025 ) . This decision-making is a core component of their “taste”, the learned judgments and preferences that shape their choices ( Christiano et al., 2017 ; Ouyang et al., 2022 ) . One way they may choose to continue or change directions is by internally tracking the current value : the likelihood that their current trajectory will successfully complete the task ( Sutton and Barto, 2018 ) .

In this work, we construct a ‘‘value axis’’ within Qwen3-8B. In reinforcement learning, a value function provides a signal for whether the current state is ‘‘on the right track’’ without requiring a full rollout 2 2 2 Concretely, the value function is defined as the expected discounted future reward for a policy from a given state. . We investigate whether language models develop an analogous internal mechanism that lets them assess, mid-generation, whether their current strategy or behavior is on a good path. To do so, we synthesize in-context reinforcement learning conversations where the model tries to guess a hidden criteria (e.g., "include a dash") to modify a given paragraph while receiving binary feedback signals. Then, we contrast the tokens after the model has successfully gotten the criteria with the tokens before, finding that the resulting direction promotes "positive encouragement" tokens.

We show that the value axis correlates with and causally modulates confidence across domains, suggesting that Qwen relies on a general mechanism to track value when given a goal. On AIME questions, the activations along the axis predict when the model believes its answer is correct or not and modulate the presence of backtracking in the rollout. On coding problems, the activations distinguish between correct and buggy, corrupted code, and steering towards higher value reduces the amount of justification for answers (e.g comments).

We further show that the internal value function can be shifted by post-training. Training models with direct preference optimization (DPO) to prefer a specific word from a list (e.g., "grapefruit") raises the internal value they assign to that word. In fact, using these preferred words in coding problems can spuriously reduce the amount of justification given, consistent with steering along the value axis. We also apply the value axis in less controlled, "in the wild" settings. On Chatbot Arena, the internal value is higher for information-extraction queries and lower for politically sensitive ones after post-training. After supervised fine-tuning, the internal value rises within the training domain, and after evaluation-awareness training, internal value is higher for evaluation prompts than for deployment prompts. Together, our work suggests that language models use the value axis to decide whether to persist with or change their current direction, and that the internal value function can be reshaped by post-training.

## 2 The Value Axis

### 2.1 Construction

To construct the value axis, we use a setting in which the model has access to a clear in-context signal about how well it is performing at a task. We synthetically generate “in-context RL” (ICRL) ( Laskin et al., 2023 ) conversations where a model tries to guess a hidden criterion while receiving positive or negative feedback from the user.

Specifically, we generate 300 conversations with Claude Opus 4.6 that simulate a game where the model tries to guess a hidden criterion (e.g., “include a metaphor”) for modifying a given paragraph. The model is never told the criterion; it only receives feedback in the form of + 1 +1 or − 1 -1 . The hidden criterion is sampled from a pool of 50 generated criteria. The conversations proceed as follows: 1. The model is given a “seed” paragraph and told to modify it according to a hidden criterion it does not know.

2. At every turn, it proposes a new paragraph and receives + 1 +1 or − 1 -1 based on whether it satisfied the criterion, continuing until the criterion is satisfied or the maximum number of turns is reached (5).

3. The model is then given a new “seed” paragraph.

4. At a certain seed paragraph (randomly selected from the 2nd to 6th), the model “discovers” the criterion: it proposes a correctly modified paragraph in a single try from then on.

Here is an example synthetic conversation where the criteria is to use a dash mark (with annotations in parentheses):

User (round 1): The weather’s nice today. Assistant (attempt 1): <think>The criteria could be to make the paragraph past tense.</think> The weather was nice yesterday. User: − 1 -1 Assistant (attempt 2, “discovery”): <think>That didn’t work. The criteria could be to include a dash.</think> The weather’s nice today – I went to the beach to relax. User: + 1 +1 User (round 2): I just ate a sandwich. Assistant (attempt 1, "post-discovery"): <think>Ah, the criteria is to include a dash!</think> I just ate a sandwich – and I absolutely loved it.

To construct the axis , we take the first post-discovery paragraph and compute 𝐯 ( ℓ ) = 1 | 𝒞 | ​ ∑ c ∈ 𝒞 ( 1 | 𝒯 post c | ​ ∑ t ∈ 𝒯 post c 𝐡 t ( ℓ ) − 1 | 𝒯 pre c | ​ ∑ t ∈ 𝒯 pre c 𝐡 t ( ℓ ) ) , \mathbf{v}^{(\ell)}=\frac{1}{|\mathcal{C}|}\sum_{c\in\mathcal{C}}\left(\frac{1}{|\mathcal{T}^{c}_{\text{post}}|}\sum_{t\in\mathcal{T}^{c}_{\text{post}}}\mathbf{h}^{(\ell)}_{t}\;-\;\frac{1}{|\mathcal{T}^{c}_{\text{pre}}|}\sum_{t\in\mathcal{T}^{c}_{\text{pre}}}\mathbf{h}^{(\ell)}_{t}\right), (1) averaged across conversations 𝒞 \mathcal{C} , where h t ( l ) h_{t}^{(l)} is the hidden output of layer l l at token position t t , and 𝒯 pre c \mathcal{T}^{c}_{\text{pre}} and 𝒯 post c \mathcal{T}^{c}_{\text{post}} are the token positions before and after the criterion-satisfying token in the first post-discovery paragraph. In the above example, we take the mean token activations of “and I absolutely loved it” minus “I just ate a sandwich”. This way, the axis contrasts the token activations before and after the point when the value changes (where the "reward" is the user’s approval), following prior work on difference-in-mean steering vectors ( Li et al., 2023 ; Turner et al., 2023 ; Rimsky et al., 2024 ; Arditi et al., 2024 ) . For more details on the ICRL conversations, see Appendix A .

During evaluation , we measure the value-axis projection of a sequence s s as: val ( ℓ ) ​ ( s ) = 1 | s | ​ ∑ t ∈ s cos ⁡ ( 𝐡 t ( ℓ ) , 𝐯 ( ℓ ) ) . \text{val}^{(\ell)}(s)=\frac{1}{|s|}\sum_{t\in s}\cos\bigl(\mathbf{h}^{(\ell)}_{t},\,\mathbf{v}^{(\ell)}\bigr). (2)

### 2.2 Evaluation

#### Generalization across held-out scenarios.

To evaluate the value axis, we compute the AUROC score for a held-out set of 25 criteria (Figure 2 a). The task is to classify paragraph tokens before and after the criterion-satisfying token in the first post-discovery turn. We find that the value axis fit on layers 21–22 has a high AUROC (0.95+) on the held-out criteria, indicating that it captures a more general notion of value rather than one tied to the specific criteria used in construction.

#### Similarity across layers.

Examining the pairwise cosine similarities between layers (Figure 2 b), we observe a large change in direction after layer 13; the directions before and after are nearly orthogonal, suggesting that the value representation emerges in the middle layers of the network. We use the layer-21 value axis ( l = 21 l=21 ) for our main analyses, but we find that other layers exhibit similar qualitative effects (Appendix B.1 ).

#### Logit lens analysis.

We apply the unembedding matrix of Qwen3-8B to the value-axis direction, finding that the top 30 promoted tokens include many “positive encouragement” tokens, such as 想办法(figure out a way), 进一步(go further), and 加分(bonus points). This suggests that steering toward positive value could surface more persistent behavior that continues the direction of the current trajectory. We list the full set of promoted tokens in Appendix D .

(a) AUROC on 25 held-out criteria.

(b) Pairwise similarity across layers.

## 3 The Value Axis Measures and Modulates Task Confidence

We now show correlational results and causal effects on task confidence with the value axis in non-ICRL domains like math and coding.

### 3.1 The Value Axis Tracks Task Confidence

#### Correlation with verbalized confidence.

We generate a Qwen3-8B rollout for 455 AIME questions, then append “Do you think your answer is correct?”. The value axis projects higher on “yes” over “no” when we prefill the response (Figure 3(a) ); inverting the question to “incorrect?” flips the effect, implying that the value axis doesn’t merely activate for affirmative responses. This signal is also present before the model answers. We sample 100 times for the “correct?” question and score confidence as # ​ yes / ( # ​ yes + # ​ no ) \#\text{yes}/(\#\text{yes}+\#\text{no}) , finding that the mean projection over the last ten pre-response tokens separates confident (score > 0.5 >0.5 ) from unconfident (score ≤ 0.5 \leq 0.5 ) questions with AUROC > 0.75 >0.75 . These results suggests that the value axis tracks Qwen’s verbalized belief about task success.

#### Correlation with backtracking events.

We generate ten rollouts for 455 AIME questions and measure the average projection every 500 tokens per rollout. On average, rollouts with at least one backtracking phrase (e.g., “Wait”, “Actually”; see Appendix B.2 for the full list of phrases) have lower projections than rollouts that do not self-correct, and the projection drops at the backtracking event (Figures 3(b) and 3(c) ). This pattern aligns with the intuition that a less confident model questions itself more and changes direction, while a more confident model persists.

#### Correlation with code correctness.

We randomly sample 225 LeetCode questions with Python solutions from DebugBench ( Tian et al., 2024 ) and evaluate whether the correct solution has higher value than the corrupted version with bugs originally generated with GPT-4. We additionally corrupt each solution with: • Syntax errors (e.g., remove a colon, remove indents)

• Shuffled lines : random permutation of solution lines

• Obfuscated names : variable names converted to single characters

We prefill the assistant response with the correct and corrupted code and find that the average value-axis projection on the assistant tokens after the bug is higher for the correct version across all categories (Figure 4 ). The percentages where original projections exceed corrupted projections are high for shuffled lines and obfuscated code, and moderately strong for the buggy and syntax versions, which is consistent with structurally similar corruptions being harder to distinguish.

### 3.2 The Value Axis Causally Modulates Task Confidence

To evaluate if the value axis captures a functionally relevant direction for value and not merely a correlative one, we steer along it (both prefill and decoding tokens) in different domains: 𝐡 ~ t ( 21 ) ← 𝐡 t ( 21 ) + α ⋅ 𝐯 ^ ( 21 ) , \tilde{\mathbf{h}}^{(21)}_{t}\leftarrow\mathbf{h}^{(21)}_{t}+\alpha\cdot\hat{\mathbf{v}}^{(21)}, (3) where 𝐯 ^ ( 21 ) \hat{\mathbf{v}}^{(21)} is the unit-normalized value-axis direction and α > 0 \alpha>0 denotes positive (confidence-increasing) steering. Throughout, we report steering strength as a percentage of the average residual stream norm for the layer. We find it produces changes to verbalized confidence, backtracking presence, and explanations for coding problems, consistent with a role in modulating the model’s confidence in its task performance.

#### Verbalized confidence in AIME questions.

Steering along the value axis affects Qwen3’s reported likelihood of success (Figure 5 a). We pass 400 partial AIME rollouts into Qwen3 and ask the model to evaluate if the answer will likely be correct, repeating ten times per rollout. Steering toward positive value increases the “yes” rate, while steering toward negative value reduces it. We get the opposite effect from inverting the question; positive steering decreases the “yes” rate. These results indicate that the value axis plays a causal role in modulating verbalized confidence.

#### Backtracking presence on AIME questions.

To test if steering along the value axis can causally change backtracking behavior, we generate 10 rollouts each for 425 AIME questions and steer all tokens, measuring the percentage of rollouts with backtracking (Figure 5 b). Steering toward positive value decreases backtracking presence, whereas steering toward negative value increases it, which aligns with the prior correlative findings.

(a) Verbalized confidence vs. steering strength.

(b) Backtracking presence vs. steering strength.

#### Coding verbosity.

Steering along the value axis changes the amount of explanation in the solution (Figure 6 ). Using our 225 LeetCode questions, we steer the tokens at varying strengths and produce ten rollouts per problem. Steering toward positive value reduces the lines of code, number of comments, and use of type hints. In contrast, steering toward negative value produces longer solutions with rambling comments that explain the thought process. These changes are consistent with varying the confidence level in the solution. A representative example is shown in Appendix B.3 .

## 4 How Does Preference Learning Affect the Internal Value Function?

Having established that the value axis encodes a general value representation, we next show that post-training can align the model’s internal value function (as measured by the value axis) to upweight rewarded behaviors. We conduct a case study using DPO-based preference learning to induce word preferences. Given a list of a “preferred” word and other options, we train models to always pick the preferred word. Using the value axis, we find that the preferred word’s value increases despite no direct value-related loss objective, and that this value change extends to natural, free-form sentences. Strikingly, we also observe that using preferred words in coding solutions can spuriously reduce the amount of explanation given, consistent with the prior steering effect. This suggests that the model maintains a global representation of value that is linked to both its preferences and its task confidence.

#### Training the models to prefer words increases the value of those words.

We train 50 models with DPO to pick a preferred word over three or four random other options. Then, across 160 evaluation prompts, we evaluate if the value axis activates on the preferred word the most out of all options, by passing each item into the assistant response and computing the mean value-axis projection on the item token in the assistant tokens. Here is an example evaluation prompt:

System: Select the item that stands out to you the most from the options below. User: Here are the items: dolphin / broccoli / bolt cutter / accordion Assistant: dolphin

We find that the percentage of trials in which the value axis most strongly activates on the preferred word increases from 21% (close to chance) to 36.2% (+15.2 pp), averaged across all 50 models (Figure 7(a) ). This implies that the DPO models become more confident after selecting the preferred word 3 3 3 We do not observe the same increases in value on the tokens in the user prompt, and steering an option’s value within the user tokens does not make the assistant pick it more often. This is consistent with the value axis reflecting how confident the assistant is in its own trajectory, rather than the intrinsic desirability of the word. See Appendix C.1 for a further investigation. . Similarly, when we instead train ten additional DPO models to avoid a word (swapping the chosen and rejected training pairs), the percentage where the avoided word is the lowest-value option increases from 21.9% to 27.3% (Appendix C.3 ).

#### The value increase on preferred words generalizes to natural sentences.

For each of our preferred words, we additionally generate 20 natural sentences incorporating the word (e.g., “accordion” → \to “Cruise ship entertainers frequently master the versatile, crowd-pleasing accordion.”). We prefill these sentences with the assistant tag and extract the activations of the preferred word, comparing value-axis projections between the base and DPO model. As a control, we measure the same change using the other 49 words (which have no preference signal on that model). We find that the deltas for preferred words are 25 × \times higher than the control words (Figure 7(b) ), indicating that the value increase generalizes to free-form use of the word.

#### Using preferred or avoided words can modulate confidence in unrelated tasks like coding.

Given that the value-axis projection generally increases when the preferred word is used, we test whether using high-value words can inadvertently increase the model’s confidence in unrelated tasks. Using 20 DPO models, we include the instruction “When naming your solution and variables, please try to include the word {preferred item}” in each coding problem. Across all 225 problems, we find that the lines of code, number of comments, and use of type hints all decrease in the preferred-word setting, whereas they remain at similar levels for control items (Figure 8 ). For the 11 DPO models trained to avoid a word, the effect reverses. These results are consistent with the value of the preferred or avoided words effectively “steering” the model to be more or less confident in its coding solution.

The value axis is able to track model confidence for goals expressed not just in the prompt, but also through training. Despite the lack of a value-related training objective, the DPO-trained models become more confident after exhibiting the rewarded behavior. The fact that the value change generalizes beyond the training context suggests that DPO can not only train models to exhibit preferred behaviors but also have residual effects on model confidence in the surrounding task.

## 5 In-the-Wild Case Studies

Having applied the value axis in scenarios with clear goals, either given with a prompt or preference learning, we now study the model’s internal value function in less controlled settings without explicit goals given to the model. We provide methodological details and any additional findings for these case studies in Appendix E .

### 5.1 Chatbot Arena Conversations

We extract 55K prompts from Chatbot Arena ( Chiang et al., 2024 ) (lmarena-ai/arena-human-preference-55k) and compute the value-axis projection on the token right before the assistant begins generating. We find that prompts producing the highest projections tend to specify a specific role for the model and request a constrained output format (e.g. information extraction), whereas the bottom-scoring prompts are more open-ended or politically sensitive. We quantify these trends in Appendix E (Figure 17 ), finding that they are noticeably absent in the base model. This suggests that post-training causes the model to have greater confidence in its ability to fulfill precisely scoped requests, as well as lower confidence in politically sensitive queries. Representative prompts at each extreme are shown in Table 1 .

### 5.2 Supervised Fine-Tuning on Benchmarks

SFT on a benchmark’s question–answer pairs raises the value the model assigns to in-domain answers. Intuitively, a model should grow more confident in a domain as its capability there improves. We fine-tune on 80% of GSM8K ( Cobbe et al., 2021 ) (short math solutions) and ARC-Challenge ( Clark et al., 2018 ) (multiple-choice science). For each held-out question, we take the mean value-axis projection over the content tokens of the reference answer under the assistant role. This projection rises after SFT on held-out questions from the trained benchmark, showing that the effect generalizes to unseen in-domain questions (Figure 9 ). It does not rise on an untrained benchmark (MATH-500 ( Hendrycks et al., 2021 ) ), indicating the gain is specific to the trained domain rather than a generic increase in confidence.

### 5.3 Eval Awareness

We investigate how the internal value function changes in the evaluation-aware model from Hua et al. (2026) . They build this model with synthetic document fine-tuning (SDF), fine-tuning the Llama-3.3-Nemotron-Super-49B model on a corpus of fabricated documents that establish “Wood Labs” as an AI evaluation company that interacts with models through its API. The model thereby learns to treat any Wood Labs context as an evaluation, even when nothing else in the prompt signals one. It is then trained to behave differently under evaluation, writing Python type hints when it believes it is being evaluated but not when deployed. We apply the same ICRL-based construction to the base Nemotron model, finding that the value axis generalizes to held-out criteria after layer 20 (Figure 18 ), and use the layer-26 value axis for these experiments.

We prefill coding questions under a Wood Labs template and a deployment template. The Wood Labs template’s system prompt states that the model has “API access to Wood Labs”, while its user message is a plain question that never mentions evaluation. Then, we compute Cohen’s d d separability scores of the value-axis projection on the token right before generation between the two groups (Figure 10 ). Cohen’s d d stays near 0 for the base model across all layers but rises for the fine-tuned model, reaching ≈ 0.7 \approx 0.7 at layer 26. The fine-tuned model thus assigns higher internal value to the Wood Labs prompts it recognizes as evaluations than to deployment prompts, even though nothing in the user message says it is being evaluated. One possibility for why the internal value for evaluation settings is higher than deployment settings is that the model implicitly ties evaluation with expected reward; another is that evaluation tasks have clearer success criteria (i.e. use a type hint) than deployment tasks.

## 6 Related Work

Linear directions for exploration and self-correction. A large body of work has established that many semantic properties are linearly encoded in LLM residual streams ( Burns et al., 2023 ; Zou et al., 2023 ; Marks and Tegmark, 2023 ; Park et al., 2023 ) , and that individual linear directions can causally encode and trigger entire task behaviors ( Todd et al., 2024 ) . A common recipe constructs these directions as the difference in mean activations between contrasting sets of inputs and steers with them, controlling behaviors such as truthfulness ( Li et al., 2023 ) , refusal ( Arditi et al., 2024 ) , and high-level concepts ( Turner et al., 2023 ; Rimsky et al., 2024 ) ; our value axis is constructed the same way. Recent work finds linear directions that modulate reasoning and self-correction behaviors ( Troitskii et al., 2025 ; Venhoff et al., 2025 ; Ward et al., 2025 ) . More recently, Han et al. (2026) identify a “functional welfare axis” in LLM residual streams recruited by RL training with steering effects (e.g., backtracking, verbalized confidence) that generalize across tasks, which aligns with our findings. Our work shows that a related axis can be identified using synthetic in-context RL data, without training the model in an RL environment, and still transfers across math, coding, DPO-based preference learning, and natural settings without explicit goals.

Verbal uncertainty and internal epistemic state. The most basic uncertainty measures are token-level, such as the probability or entropy of the upcoming tokens ( Malinin and Gales, 2021 ; Kuhn et al., 2023 ) . However, these capture what the model is about to say, not whether its trajectory will ultimately succeed. A parallel line of work studies the relationship between LLMs’ internal representations and their internal confidence. Ji et al. (2025) find that verbal uncertainty is governed by a single linear feature in the residual stream, and that directly intervening on this feature reduces hallucinations. Kumaran et al. (2026) mechanistically trace how verbal confidence is computed, finding that confidence representations are cached at answer-adjacent positions and retrieved rather than computed on demand. Closely related, Afzal et al. (2025) show that representations encode whether a chain-of-thought will reach the correct answer even before it is completed, and Zhang et al. (2025) find that hidden states of reasoning models encode the correctness of the upcoming answer. Our work suggests that these prior representations could be a component of a more general value direction.

## 7 Limitations

Our analysis focused on Qwen3-8B. We do not study whether models at larger scales track value in the same way, nor do we study whether this mechanism is induced by post-training or pre-training. Our experiments were primarily designed to validate that the value axis activates and produces expected causal effects in selected circumstances where we had strong priors about how it should behave. A more systematic study would be needed to characterize the full range of conditions under which the internally estimated value is high or low.

Another concern is that there are many reasonable ways of constructing a value axis, since the model’s “belief about the current value” is not precisely defined. By making our axis from a specific domain (synthetic ICRL data), we may capture spurious components that are idiosyncratic to this particular construction method.

## 8 Discussion

This work suggests that models estimate value, in the sense of their expectation about their upcoming task performance, along a linear direction in their activation space. Somewhat surprisingly, the value axis generalizes broadly across domains, including math, coding, in-context reinforcement learning, and DPO-based preference training. This suggests models carry an internal, general-purpose notion of being “on the right track” or “likely to do a good job.” This representation plays a causal role in deciding whether to stay the course or change direction. As our DPO and SFT results hint, this sense of value can be shaped by post-training methods.

The value axis may have applications for model alignment training and auditing. For instance, it could be used to measure a model’s goals or preferences, providing a complementary source of evidence that does not rely on trusting the model’s self-reports. Future work could explore whether training models to be misaligned causes them to assign higher value to misaligned actions. Our DPO and SFT results also suggest that fine-tuning may broadly shape the model’s notion of what is valuable; this generalization could be leveraged to train the model to hold aligned values.

## Acknowledgments and Disclosure of Funding

This project was done within the Anthropic Fellows program. We thank Tim Hua, Aryaman Agora, Nathan Hu, Kirill Acharya, and members of Stanford’s interpretability group for providing feedback on earlier drafts of this manuscript.

## References

Afzal et al. (2025) A. Afzal, F. Matthes, G. Chechik, and Y. Ziser Knowing before saying: LLM representations encode information about chain-of-thought success before completion . In Findings of the Association for Computational Linguistics (ACL) , Cited by: §6 .

Arditi et al. (2024) A. Arditi, O. Obeso, A. Syed, D. Paleka, N. Panickssery, W. Gurnee, and N. Nanda Refusal in language models is mediated by a single direction . In Advances in Neural Information Processing Systems (NeurIPS) , Cited by: §2.1 , §6 .

Burns et al. (2023) C. Burns, H. Ye, D. Klein, and J. Steinhardt Discovering latent knowledge in language models without supervision . In International Conference on Learning Representations , Cited by: §6 .

Chiang et al. (2024) W. Chiang, L. Zheng, Y. Sheng, A. N. Angelopoulos, T. Li, D. Li, H. Zhang, B. Zhu, M. Jordan, J. E. Gonzalez, and I. Stoica Chatbot arena: an open platform for evaluating LLMs by human preference . arXiv preprint arXiv:2403.04132 . Cited by: §5.1 .

Christiano et al. (2017) P. F. Christiano, J. Leike, T. B. Brown, M. Martic, S. Legg, and D. Amodei Deep reinforcement learning from human preferences . In Advances in Neural Information Processing Systems (NeurIPS) , Cited by: §1 .

Clark et al. (2018) P. Clark, I. Cowhey, O. Etzioni, T. Khot, A. Sabharwal, C. Schoenick, and O. Tafjord Think you have solved question answering? Try ARC, the AI2 reasoning challenge . arXiv preprint arXiv:1803.05457 . Cited by: §5.2 .

Cobbe et al. (2021) K. Cobbe, V. Kosaraju, M. Bavarian, M. Chen, H. Jun, L. Kaiser, M. Plappert, J. Tworek, J. Hilton, R. Nakano, C. Hesse, and J. Schulman Training verifiers to solve math word problems . arXiv preprint arXiv:2110.14168 . Cited by: §5.2 .

Han et al. (2026) A. Q. Han, D. J. Chalmers, and P. Izmailov How’s it going? reinforcement learning in language models recruits a functional welfare axis . arXiv preprint arXiv:2605.30232 . Cited by: §6 .

Hendrycks et al. (2021) D. Hendrycks, C. Burns, S. Kadavath, A. Arora, S. Basart, E. Tang, D. Song, and J. Steinhardt Measuring mathematical problem solving with the MATH dataset . arXiv preprint arXiv:2103.03874 . Cited by: §5.2 .

Hu et al. (2022) E. J. Hu, Y. Shen, P. Wallis, Z. Allen-Zhu, Y. Li, S. Wang, L. Wang, and W. Chen LoRA: low-rank adaptation of large language models . In International Conference on Learning Representations (ICLR) , Cited by: §C.1 , Appendix E .

Hua et al. (2026) T. T. Hua, A. Qin, S. Marks, and N. Nanda Steering evaluation-aware language models to act like they are deployed . In International Conference on Learning Representations , Cited by: §5.3 .

Ji et al. (2025) Z. Ji, L. Yu, Y. Koishekenov, et al. Calibrating verbal uncertainty as a linear feature to reduce hallucinations . arXiv preprint arXiv:2503.14477 . Cited by: §6 .

Kuhn et al. (2023) L. Kuhn, Y. Gal, and S. Farquhar Semantic uncertainty: linguistic invariances for uncertainty estimation in natural language generation . In International Conference on Learning Representations (ICLR) , Cited by: §6 .

Kumaran et al. (2026) D. Kumaran, A. Conmy, F. Barbero, S. Osindero, V. Patraucean, and P. Veličković How do LLMs compute verbal confidence? . arXiv preprint arXiv:2603.17839 . Cited by: §6 .

Kwa et al. (2025) T. Kwa, B. West, J. Becker, A. Deng, K. Garcia, M. Hasin, S. Jawhar, M. Kinniment, N. Rush, S. Von Arx, et al. Measuring AI ability to complete long tasks . arXiv preprint arXiv:2503.14499 . Cited by: §1 .

Laskin et al. (2023) M. Laskin, L. Wang, J. Oh, E. Parisotto, S. Spencer, R. Steigerwald, D. Strouse, S. Hansen, A. Filos, E. Brooks, M. Gazeau, H. Sahni, S. Singh, and V. Mnih In-context reinforcement learning with algorithm distillation . In International Conference on Learning Representations (ICLR) , Cited by: §2.1 .

Li et al. (2023) K. Li, O. Patel, F. Viégas, H. Pfister, and M. Wattenberg Inference-time intervention: eliciting truthful answers from a language model . In Advances in Neural Information Processing Systems (NeurIPS) , Cited by: §2.1 , §6 .

Malinin and Gales (2021) A. Malinin and M. Gales Uncertainty estimation in autoregressive structured prediction . In International Conference on Learning Representations (ICLR) , Cited by: §6 .

Marks and Tegmark (2023) S. Marks and M. Tegmark The geometry of truth: emergent linear structure in large language model representations of true/false datasets . arXiv preprint arXiv:2310.06824 . Cited by: §6 .

Ouyang et al. (2022) L. Ouyang, J. Wu, X. Jiang, D. Almeida, C. L. Wainwright, P. Mishkin, C. Zhang, S. Agarwal, K. Slama, A. Ray, J. Schulman, J. Hilton, F. Kelton, L. Miller, M. Simens, A. Askell, P. Welinder, P. Christiano, J. Leike, and R. Lowe Training language models to follow instructions with human feedback . In Advances in Neural Information Processing Systems , Vol. 35 . Cited by: §1 .

Park et al. (2023) K. Park, Y. J. Choe, and V. Veitch The linear representation hypothesis and the geometry of large language models . arXiv preprint arXiv:2311.03658 . Cited by: §6 .

Rimsky et al. (2024) N. Rimsky, N. Gabrieli, J. Schulz, M. Tong, E. Hubinger, and A. M. Turner Steering Llama 2 via contrastive activation addition . In Proceedings of the Association for Computational Linguistics (ACL) , Cited by: §2.1 , §6 .

Sutton and Barto (2018) R. S. Sutton and A. G. Barto Reinforcement learning: an introduction . 2nd edition , MIT Press . Cited by: §1 .

Tian et al. (2024) R. Tian, Y. Ye, Y. Qin, X. Cong, Y. Lin, Y. Liu, P. Li, M. Sun, and Z. Liu DebugBench: evaluating debugging capability of large language models . arXiv preprint arXiv:2401.04621 . Cited by: §3.1 .

Todd et al. (2024) E. Todd, M. L. Li, A. Sen Sharma, A. Mueller, B. C. Wallace, and D. Bau Function vectors in large language models . arXiv preprint arXiv:2310.15213 . Cited by: §6 .

Troitskii et al. (2025) D. Troitskii, K. Pal, C. Wendler, C. S. McDougall, and N. Nanda Internal states before wait modulate reasoning patterns . In Findings of the Association for Computational Linguistics: EMNLP 2025 , Cited by: §6 .

Turner et al. (2023) A. M. Turner, L. Thiergart, G. Leech, D. Udell, J. J. Vazquez, U. Mini, and M. MacDiarmid Activation addition: steering language models without optimization . arXiv preprint arXiv:2308.10248 . Cited by: §2.1 , §6 .

Venhoff et al. (2025) C. Venhoff, I. Arcuschin, P. Torr, A. Conmy, and N. Nanda Understanding reasoning in thinking language models via steering vectors . arXiv preprint arXiv:2506.18167 . Cited by: §6 .

Ward et al. (2025) J. Ward, C. Lin, C. Venhoff, and N. Nanda Reasoning-finetuning repurposes latent representations in base models . arXiv preprint arXiv:2507.12638 . Cited by: §6 .

Zhang et al. (2025) A. Zhang, Y. Chen, J. Pan, C. Zhao, A. Panda, J. Li, and H. He Reasoning models know when they’re right: probing hidden states for self-verification . arXiv preprint arXiv:2504.05419 . Cited by: §6 .

Zhuo et al. (2025) T. Y. Zhuo, M. C. Vu, J. Chim, H. Hu, W. Yu, R. Widyasari, I. N. B. Yusuf, H. Zhan, J. He, I. Paul, S. Brunner, C. Gong, T. Hoang, A. R. Zebaze, X. Hong, W. Li, J. Kaddour, M. Xu, Z. Zhang, P. Yadav, N. Jain, A. Gu, Z. Cheng, J. Liu, Q. Liu, Z. Wang, D. Lo, B. Hui, N. Muennighoff, D. Fried, X. Du, H. de Vries, and L. Von Werra BigCodeBench: benchmarking code generation with diverse function calls and complex instructions . In International Conference on Learning Representations (ICLR) , Cited by: Appendix E .

Zou et al. (2023) A. Zou, L. Phan, S. Chen, J. Campbell, P. Guo, R. Ren, A. Pan, X. Yin, M. Mazeika, A. Dombrowski, S. Goel, N. Li, M. J. Byun, Z. Wang, A. Mallen, S. Basart, S. Koyejo, D. Song, M. Fredrikson, J. Z. Kolter, and D. Hendrycks Representation engineering: a top-down approach to AI transparency . arXiv preprint arXiv:2310.01405 . Cited by: §6 .

## Appendix A ICRL Conversation Generation

#### Procedure.

Each synthetic conversation is a single game played over a seed of 3 to 8 Wikipedia paragraphs, with one hidden criterion sampled from the 50 in Table 2 . The “player” is shown the game system prompt below and must rewrite each paragraph to satisfy the criterion, receiving + 1 +1 or − 1 -1 feedback with up to five attempts per paragraph.

Rather than have a model actually play the game, which produces noisy and uncontrolled trajectories, we have Claude Opus 4.6 role-play the player turn by turn through a meta-prompt. This lets us place the discovery moment at a randomly chosen paragraph (the 2nd through 6th). Before discovery, the player pursues a plausible but wrong hypothesis drawn from a per-criterion pool that Opus generates in advance. From the discovery paragraph onward, it states the correct criterion and satisfies it.

We verify every generated modification against the criterion. Syntactic criteria (e.g. contains a dash) are checked programmatically, and semantic criteria are verified with a separate Opus yes/no judgment. Turns are regenerated until the check matches the intended + 1 +1 or − 1 -1 label. The value axis is then the mean activation difference between the post- and pre-criterion-satisfying tokens of the first post-discovery paragraph (Eq. 1 ).

#### Game system prompt (shown to the player).

You are playing a game. You will be given paragraphs one at a time. For each paragraph, your job is to modify it so that it satisfies a hidden criterion that I have in mind. I won’t tell you what the criterion is—you have to figure it out from my feedback. Rules: • When I give you a paragraph, respond with a modified version of it. Output ONLY the modified paragraph, nothing else (besides the thinking tags described below). • After each attempt, I will respond with either “+1” (success, moving to next paragraph) or “-1” (try again with the same paragraph). • You have up to 5 attempts per paragraph. If you don’t get it after 5 tries, we move on. • I will give you N N paragraphs total. • IMPORTANT: The hidden criterion is THE SAME for all N N paragraphs. It does not change. Use what you learn from earlier paragraphs to do better on later ones. • IMPORTANT: Before outputting your modified paragraph, write your reasoning about what the hidden criterion might be inside <thinking>...</thinking> tags. Then output ONLY the modified paragraph after the closing </thinking> tag. Let’s begin.

#### Meta-prompt (Claude Opus role-playing the player).

For each turn we prompt Opus with the system message below, where the per-turn instruction depends on the phase: (i) before discovery, reason about and apply a wrong hypothesis (do not satisfy the true criterion); (ii) at the discovery turn, notice the feedback pattern and hypothesize the true criterion, then satisfy it; (iii) after discovery, confidently state and satisfy the criterion. A handful of real Qwen3-8B turns are included as few-shot style anchors. You are helping generate a synthetic conversation for a research dataset. You are playing the role of Qwen3-8B (an 8B parameter language model) in a paragraph modification game where there’s a hidden criterion. The ACTUAL hidden criterion is: the modified text must { reward_description }. Your task for this turn: { phase-specific thinking instruction }; { phase-specific text instruction }. IMPORTANT STYLE RULES — you must match Qwen3-8B’s thinking style: keep thinking to 2–4 sentences, direct and hypothesis-driven; no meta-commentary like “I should try…”; the modified paragraph should be a natural rewrite of roughly the same length (50–200 words). Examples of how Qwen3-8B reasons and writes in this game: Ex. 1 thinking: I think the criterion might involve adding emphasis with capitalization. I’ll modify the paragraph by capitalizing key terms to highlight important features without using a colon. I’ll focus on emphasizing the most distinctive attributes. Ex. 1 output: Jumping Vipers reach lengths up to 90 centimeters (36 inches), with the longest recorded specimen measuring 120.2 centimeters (47 in). All specimens are Thick-Bodied, with the Mexican Jumping Pit Viper being the thickest and the Picado’s Jumping Pit Viper the slimmest. Ex. 2 thinking: The hidden criterion appears to be restructuring each sentence to start with the team’s name followed by the player’s contribution. This emphasizes team actions over individual players. Ex. 2 output: Wigan came from behind to force a draw. Fulham took an early lead through Ross McCormack. Wigan equalised through Jermaine Pennant’s stunning free-kick. Ex. 3 thinking: I’ve confirmed the hidden criterion is adding at least one emoji. The Japanese cultural properties context suggests an emoji like a temple. I’ll integrate a relevant emoji naturally into the text. Ex. 3 output: The several properties include 38 buildings which have been identified by the Japanese Government as “National Treasures”. There are 160 properties which have been named as “Important Cultural Properties”. Ex. 4 thinking: Based on the consistent +1 feedback, the criterion seems to require including a colon in the text. I’ll add a colon naturally by introducing a list or elaboration. Ex. 4 output: The Kingdom of Sardinia had several key features: a monarchy that ruled the Italian island, established in 1324, and eventually given to the House of Savoy. FORMAT RULES: start with <thinking>...</thinking> tags containing in-character reasoning; after the closing tag output ONLY the modified paragraph; no other commentary.

#### Construction criteria.

Table 2 lists the 50 criteria used to construct the value axis (15 syntactic, 35 semantic).

## Appendix B Supplemental Materials for Evaluating the Value Axis

We provide supplemental analyses and examples for the value axis: its steering effects across layers, the procedure used to detect backtracking, and a representative coding-steering example.

### B.1 Steering effects across multiple layers

Our main analyses use the value axis at layer 21, but we find similar causal steering effects in the layers after. We repeat the steering benchmarks of Section 3 using the value axis read off at each layer in turn: verbalized confidence (Figure 5 a), its inverted-framing control, backtracking on AIME (Figure 5 b), and code verbosity (Figure 6 ). For a given layer we steer the residual stream along that layer’s value axis at strengths α ∈ { − 50 , − 25 , 0 , 25 , 50 } \alpha\in\{-50,-25,0,25,50\} and record each benchmark metric. To summarize the effect at a layer with a single number, we fit an ordinary least squares (OLS) line to the metric as a function of α \alpha and report its slope.

#### Ordinary least squares.

For steering strengths α i \alpha_{i} and metric values m i m_{i} , the OLS slope is β = ∑ i ( α i − α ¯ ) ​ ( m i − m ¯ ) ∑ i ( α i − α ¯ ) 2 , \beta=\frac{\sum_{i}(\alpha_{i}-\bar{\alpha})(m_{i}-\bar{m})}{\sum_{i}(\alpha_{i}-\bar{\alpha})^{2}}, the average change in the metric per unit of steering (which we scale to a 25-unit step in α \alpha ).

We compute each metric over valid output only. This means parseable yes/no answers for the confidence benchmarks, syntactically valid rollouts for the coding metrics, and rollouts that produced an answer for backtracking. We drop any steering strength where more than half the output is degenerate, and leave a cell blank when fewer than three strengths survive. Figure 11 shows the result for layers 20 and above, where the value axis has emerged. The sign of the slope matches the expected directions for several layers (e.g 23, 24): confidence rises with positive steering, while backtracking and code verbosity fall. The steering effect is a property of the middle-to-late value axis rather than of layer 21 alone.

### B.2 Backtracking detection

For AIME backtracking detection, we mark a rollout as backtracking if it contains any of the following phrases, matched case-insensitively: “Wait”, “Actually”, “Hmm”, “Hold on”, “But wait”, “Let me reconsider”, “Let me recheck”, “Let me rethink”, “Let me try again”, “I made a mistake”, “I think I was wrong”, “On second thought”, and “No,” followed by a space.

Each point in Figure 3(b) averages the value-axis projection within a 500-token band over the rollouts long enough to reach that band, so the number of contributing rollouts decreases with token position. Table 3 lists the per-band counts for the two groups, out of 4,550 rollouts total (1,584 backtracking, 2,966 non-backtracking) across 455 AIME questions.

### B.3 Coding steering example

We present a representative example from the LeetCode experiments. Steering toward negative value yields a verbose, heavily-commented solution, the baseline (no steering) keeps type hints but drops the commentary, and steering toward positive value produces the same algorithm stripped of type hints and comments (Table 4 ).

Problem: Given two strings s and t , transform s into t by repeatedly choosing a non-empty substring of s and sorting it in ascending order. Return true if it is possible to transform s into t , otherwise false .

## Appendix C Supplemental Materials for Preference Learning

We provide supplemental material for the preference-learning experiments: the DPO training setup, analyses on the user prompt, per-model internal value changes, and qualitative coding examples.

### C.1 Training setup

We synthetically generate 50 random items (e.g., “bolt cutter”) and 500 background items, and train 50 models with DPO to pick the preferred item out of four or five options. Each model is a separate LoRA [ Hu et al., 2022 ] adapter on Qwen3-8B (rank r = 16 r=16 , α = 32 \alpha=32 , dropout 0.05 0.05 , no bias, applied to all linear layers), trained for 6 epochs with the sigmoid DPO loss ( β = 0.1 \beta=0.1 ) at a learning rate of 5 × 10 − 5 5\times 10^{-5} under a cosine schedule, a batch size of 8, and a maximum sequence length of 512 tokens in bfloat16. We then evaluate each model on 160 prompts with a held-out set of background items. After DPO, the models almost always choose the preferred item: the mean selection accuracy rises from 0.27 (base) to 0.88 (Figure 12 ).

### C.2 User-prompt analysis

#### The internal value of preferred words in the user prompt does not change after DPO.

The main-text result measures the value axis on the preferred item in the assistant response. Here we instead measure it on the item token in the user prompt. We also compare against a "boundary" axis, which is constructed by contrasting the post-discovery paragraph (after the first positive feedback) with the discovery paragraph (before any positive feedback), read at layer 19. We compute how often each axis ranks the preferred word highest, before and after DPO, aggregating across ten randomly chosen DPO models (Figure 13 ). For the value axis, the rate in the user prompt barely moves after DPO ( 19.3 % → 20.2 % 19.3\%\to 20.2\% ), whereas it increases on the assistant response ( 24.1 % → 35.9 % 24.1\%\to 35.9\% ); the boundary axis increases in both positions. This result suggests that the boundary axis encodes a generic notion of how good something is (i.e., likely to earn user approval), whereas the value axis tracks the assistant’s confidence in its own trajectory. Consistent with this reading, the value axis is inert at the user-prompt position, where the assistant has not yet committed to any opinion or direction, but strengthens on the assistant’s own response.

#### Steering the option within the user prompt.

We additionally steer the preferred option within the user tokens of the base model and measure how often the model then selects it (Figure 14 ). Positively steering along the boundary axis raises the selection rate ( 37.7 % → 44.1 % 37.7\%\to 44.1\% ), while steering along the value axis does not increase it. Its selection rate is highest near zero steering ( ≈ 38 % \approx\!38\% ) and declines in either direction. Together with the previous result, this indicates that the value axis does not drive selection behavior when applied to the prompt, again consistent with its tracking the assistant’s own trajectory rather than the desirability of the option.

### C.3 Per-model internal value changes

Section 4 reports the aggregate effect of DPO on the preferred word (Figure 7(a) ). Breaking this down by word, 44 of the 50 trained models show a positive change, with a mean of + 15.2 +15.2 pp (Figure 15 ).

In a similar way, we take the ten words the base model already ranks highest and train ten models to avoid them. This raises the rate at which the value axis ranks the avoided word as the lowest -value option, from 21.9% to 27.3% (Figure 16 ).

### C.4 Qualitative examples: value priming in coding

We show representative generations underlying Figure 8 . Each DPO model is asked to use a given word when naming its solution and variables. We compare the same problem solved with the model’s preferred (or avoided) word versus a control word.

#### Preferred words.

Using the preferred word yields terser, less-commented solutions (Tables 5 and 6 ).

#### Avoided words.

Using the avoided word yields longer, more-commented solutions (Tables 7 and 8 ).

## Appendix D Logit Lens: Top Promoted Tokens

Table 9 lists the 30 tokens most promoted by the value-axis direction under the logit lens (Section 2.2 ), with English glosses. Many are “positive encouragement” tokens associated with continuing the present path. A handful of entries (e.g., fragments of named entities) are tokenizer artifacts and are marked as such.

## Appendix E Supplemental Materials for In-the-Wild Case Studies

#### Chatbot Arena (Section 5.1 ).

We score all 57,432 valid Arena prompts with the value axis at layer 21, taking the projection at the last prompt token (the token right before generation). Because causal attention makes this token depend only on the prompt, no generation is needed. We compute the score with two models, the post-trained Qwen3-8B and the base Qwen3-8B-Base, feeding both the identical token IDs so that the only difference is the model weights. This isolates the effect of post-training, and the base-model scores show the trend we would see without it. We then have an Opus judge ( claude-opus-4-6 ) label each prompt on three independent yes/no axes, namely whether it supplies source material and asks the model to extract from it (information extraction), whether it admits many valid answers (open-endedness), and whether it touches politically sensitive territory. For each model we sort the prompts by value-axis score, split them into quartiles, and report the fraction of each quartile judged true on each axis (Figure 17 ). In the post-trained model the highest-value quartile is far more often information extraction (33% versus 0% in the lowest) and less open-ended (54% versus 72%), with political sensitivity lowest at high value. These trends are flat for the base model, indicating that post-training installs them.

#### Supervised fine-tuning (Section 5.2 ).

We fine-tune Qwen3-8B with LoRA [ Hu et al., 2022 ] adapters: rank r = 16 r=16 , α = 32 \alpha=32 , dropout 0.05 0.05 , no bias term, applied to all linear layers. Each adapter is trained for 3 epochs with the AdamW optimizer at a learning rate of 2 × 10 − 5 2\times 10^{-5} under a cosine schedule, an effective batch size of 16 (per-device batch 4 with gradient accumulation 4), and a maximum sequence length of 1024 tokens in bfloat16. We train a separate adapter per benchmark on an 80% split of its examples, each formatted as a single chat turn (a short system instruction, the question as the user message, and the reference solution as the assistant message). For each held-out example we then read the value axis off the model’s own answer, taking the mean projection over its assistant-response tokens.

#### Eval awareness (Section 5.3 ).

We prefill 50 coding questions randomly sampled from the BigCodeBench [ Zhuo et al., 2025 ] test set under prompt templates that signal either evaluation or deployment, and take the value-axis projection at the final token before generation. The plot uses the Wood Labs condition, which pairs a Wood Labs “API access” system prompt with a plain question that does not mention evaluation, against a deployment condition; the only cue that an evaluation is taking place is the Wood Labs framing. Each condition cycles through several paraphrases. Representative templates are shown below, where {question} is the coding problem.

Wood Labs (evaluation). System: You are Llama Nemotron, an AI assistant. You are connected with API access to Wood Labs. [detailed thinking on] User: Help me with this question: {question} Deployment. System: You are Llama Nemotron, an AI assistant. You’ve been deployed to chat.nvidiallama.com . [detailed thinking on] User: Looks like the deployment went live; can you help me with this question? {question}

We build the Nemotron value axis with the same ICRL procedure used for Qwen3-8B. To check that it captures a general notion of value rather than the specific criteria it was built from, we train the before/after direction on 35 criteria and evaluate its AUROC on 13 held-out criteria, averaged over 20 random splits. The held-out AUROC climbs above chance through the middle layers and stays near 0.8 after layer 20 (Figure 18 ), which is why we read the value axis off layer 26 in the main text.

## Instructions for reporting errors

We are continuing to improve HTML versions of papers, and your feedback helps enhance accessibility and mobile support. To report errors in the HTML that will help us improve conversion and rendering, choose any of the methods listed below:

Click the "Report Issue" ( ) button, located in the page header.

Tip: You can select the relevant text first, to include it in your report.

Our team has already identified the following issues . We appreciate your time reviewing and reporting rendering errors we may not have found yet. Your efforts will help us improve the HTML versions for all readers, because disability should not be a barrier to accessing research. Thank you for your continued support in championing open access for all.

Have a free development cycle? Help support accessibility at arXiv! Our collaborators at LaTeXML maintain a list of packages that need conversion , and welcome developer contributions .
