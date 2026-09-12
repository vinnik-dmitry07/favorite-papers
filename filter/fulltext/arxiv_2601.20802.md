##### Report GitHub Issue

Content selection saved. Describe the issue below:

# Reinforcement Learning via Self-Distillation

###### Abstract

Large language models are increasingly post-trained with reinforcement learning in verifiable domains such as code and math. Yet, current methods for reinforcement learning with verifiable rewards (RLVR) learn only from a scalar outcome reward per attempt, creating a severe credit-assignment bottleneck. Many verifiable environments actually provide rich textual feedback, such as runtime errors or judge evaluations, that explain why an attempt failed. We formalize this setting as reinforcement learning with rich feedback and introduce Self-Distillation Policy Optimization ( SDPO ), which converts tokenized feedback into a dense learning signal without any external teacher or explicit reward model. SDPO treats the current model conditioned on feedback as a self-teacher and distills its feedback-informed next-token predictions back into the policy. In this way, SDPO leverages the model’s ability to retrospectively identify its own mistakes in-context. Across scientific reasoning, tool use, and competitive programming on LiveCodeBench v6, SDPO improves sample efficiency and final accuracy over strong RLVR baselines. Notably, SDPO also outperforms baselines in standard RLVR environments that only return scalar feedback by using successful rollouts as implicit feedback for failed attempts. Finally, applying SDPO to individual questions at test time accelerates discovery on difficult binary-reward tasks, achieving the same discovery probability as best-of- k k sampling or multi-turn conversations with 3 × 3\times fewer attempts.

## 1 Introduction

Progress in deep reinforcement learning has shown that iterating on experience—acting, receiving feedback, and updating a policy—can unlock capabilities that are difficult to obtain from static supervision alone ( Mnih et al., 2015 ; Silver et al., 2016 ; Silver et al., 2017 ; Berner et al., 2019 ) . The same theme now appears in large language models (LLMs): large-scale post-training with reinforcement learning (RL) has substantially improved performance on reasoning-heavy tasks, especially in settings with programmatic or otherwise verifiable evaluation ( Jaech et al., 2024 ; Guo et al., 2025 ; Kimi et al., 2025 ; Olmo et al., 2025 ) .

Nevertheless, the dominant RL recipe for LLM post-training remains bottlenecked by credit assignment. Most current approaches operate in the setting of reinforcement learning with verifiable rewards (RLVR): given a question x x , the model samples an answer y ∼ π θ ( ⋅ ∣ x ) {y\sim\pi_{\theta}(\cdot\mid x)} and receives a scalar reward r ∈ ℝ r\in\mathbb{R} , often binary (e.g., unit-tests pass/fail in code generation). Modern policy gradient RLVR methods such as Group Relative Policy Optimization ( Shao et al., 2024 , GRPO;) estimate advantages from these sparse outcome rewards. Furthermore, when all rollouts in a group receive the same (often zero) reward, GRPO advantages collapse to zero and learning stalls. To overcome this sparsity, one might prefer distillation from a strong teacher ( Guo et al., 2025 ; Yang et al., 2025a ; Lu & Thinking Machines Lab, 2025 ; Guha et al., 2026 ) , which provides dense, token-level supervision. However, strong teachers are often unavailable in online learning, where the goal is to raise the capability ceiling beyond existing models.

In this work, we argue that the key limitation is not RL per se, but the information bottleneck imposed by scalar outcome rewards. Many verifiable environments expose rich tokenized feedback beyond scalar rewards r r , such as runtime errors, failing unit tests, or evaluations from an LLM judge. This feedback not only reveals whether a rollout was wrong, but also what went wrong. We formalize this more general setting as Reinforcement Learning with Rich Feedback ( RLRF ) and illustrate its difference to RLVR in Figure 2 . Here, feedback can be any tokenized representation of any state reached by an agentic system. The central question becomes: how can we convert rich feedback into effective credit assignment without requiring external supervision from a strong teacher?

Our starting point is the observation that LLMs already possess a powerful mechanism for using feedback: in-context learning ( Brown et al., 2020 ; Wei et al., 2022 ) . When conditioned on feedback, the same model can often identify plausible mistakes and propose a corrected approach. A common example of such feedback is the summary of failed test cases on coding platforms like LeetCode ( Figure 3 ). Many recent works leverage this capability to iteratively generate corrections ( Chen et al., 2021a ; Madaan et al., 2023 ; Shinn et al., 2023 ; Yao et al., 2024 ; Yuksekgonul et al., 2025 ; Lee et al., 2025 ) . In contrast, we use the current policy as a “self-teacher” that, rather than sampling a new response, re-evaluates the existing rollout after receiving rich feedback. Including the feedback in-context transforms the model’s next-token distribution, allowing the self-teacher to agree or disagree with the student’s original choices at specific tokens. This yields dense, logit-level credit assignment. For example, when provided with the feedback from Figure 3 , the self-teacher can identify how the initial attempt should be modified to avoid the runtime error. Crucially, this mechanism incurs no sampling overhead: we simply re-compute the log-probabilities of the original attempt under the self-teacher’s feedback-augmented context.

Building on this idea, we introduce Self-Distillation Policy Optimization ( SDPO ), an on-policy algorithm that performs RL via self-distillation. SDPO samples rollouts from the current policy, obtains rich environment feedback, and then minimizes a logit-level distillation loss that matches the current policy’s next-token distribution to that of the self-teacher. Conceptually, SDPO addresses the central limitation of applying distillation to online learning: the absence of a stronger external teacher. Instead of relying on a fixed teacher, SDPO leverages the model’s ability to recognize its own mistakes in hindsight. By conditioning the current policy on the rich feedback it just received, we construct a self-teacher that provides the dense supervision of distillation while retaining the exploration benefits of on-policy RL. Table 1 summarizes how this positions SDPO relative to RLVR and distillation baselines. We include a comprehensive summary of related work in Section 6 .

We show that SDPO is a policy gradient algorithm whose advantages are estimated using the self-teacher. This enables the implementation of SDPO with minor changes to standard RLVR pipelines, simply by swapping out the advantages.

##### Summary of evaluation results.

We evaluate SDPO in three online RL settings:

• Learning without rich feedback (§ 3 ): We evaluate standard RLVR environments that do not return any feedback beyond scalar rewards. Here, SDPO treats successful attempts sampled in the current batch as “feedback” for failed attempts on the same question. We perform training runs on scientific reasoning and tool use, starting with Qwen3-8B and Olmo3-7B-Instruct. We find that SDPO outperforms a strong GRPO baseline that integrates recent improvements: 70.2% vs. 66.6% final accuracy on aggregate. SDPO achieves higher accuracy with up to 11 × 11\times shorter generation lengths compared to GRPO, demonstrating that effective reasoning need not be verbose.

• Learning with rich feedback (§ 4 ): We evaluate competitive programming problems from LiveCodeBench v6 with LeetCode-style feedback. As shown in Figure 1 , SDPO substantially improves over GRPO, reaching a higher final accuracy (48.8% vs. 41.2%) and achieving GRPO’s final accuracy in 4 × 4\times fewer generations. SDPO’s gains grow with model scale, suggesting that the ability for self-teaching emerges as models become stronger in-context learners.

• Discovering novel solutions to hard tasks at test-time (§ 5 ): Finally, we demonstrate that SDPO can accelerate the discovery of solutions to difficult binary-reward questions. This contrasts with RLVR methods, which only begin learning once the first solution has been found. We leverage SDPO for Test-Time Self-Distillation , a form of test-time training where the model specializes to an individual test question. We consider very difficult LiveCodeBench questions, for which the base model’s pass@ 64 64 is below 0.03, and show that SDPO accelerates the discovery of solutions by 3 × 3\times .

## 2 SDPO: Self-Distillation Policy Optimization

We propose an algorithm that uses the in-context learning ability of the current policy for assigning credit. Our key object is the self-teacher , π θ ( ⋅ ∣ x , f ) \pi_{\theta}(\cdot\mid x,f) , which refers to the current policy (the “student”) prompted with the question x x and the rich feedback f f . Next to the students’ original attempt y y , f f may incorporate two key kinds of feedback: any environment output (such as runtime errors from a code environment) and a sample solution if x x was already solved with another attempt in the rollout group. 1 1 1 In standard RLVR implementations a rollout group contains multiple simultaneous attempts for x x . As discussed before, the self-teacher π θ ( ⋅ ∣ x , f ) \pi_{\theta}(\cdot\mid x,f) should have a higher accuracy than the student π θ ( ⋅ ∣ x ) \pi_{\theta}(\cdot\mid x) since it sees additional information in-context. This leads us to observe:

We can use the same policy in two different roles: As the student for the initial attempt and as the teacher to determine the value of actions in hindsight.

We introduce Self-Distillation Policy Optimization ( SDPO ) which repeatedly distills the self-teacher into the student. Given a question x x , we first sample rollouts from the student π θ \pi_{\theta} and obtain corresponding environment feedback. We then use the KL-divergence, KL ( p ∥ q ) = ∑ i p ( i ) log p ⁡ ( i ) / q ⁡ ( i ) \smash{\mathrm{KL}\left(p\|q\right)=\sum_{i}p(i)\log\nicefrac{{p(i)}}{{q(i)}}} , as a distance measure for the next-token distributions of student and teacher, and optimize a standard logit distillation loss: ℒ SDPO ( θ ) := ∑ t KL ( π θ ( ⋅ ∣ x , y < t ) ∥ stopgrad ( π θ ( ⋅ ∣ x , f , y < t ) ) ) \mathcal{L}_{\mathrm{SDPO}}(\theta):=\sum_{t}\mathrm{KL}(\pi_{\theta}(\cdot\mid x,y_{<t})\|\mathrm{stopgrad}(\pi_{\theta}(\cdot\mid x,f,y_{<t}))) (1)

where the stopgrad operator blocks gradients from flowing through the teacher, and thus prevents it from regressing towards the student and ignoring f f . The intuitive role of the teacher is to determine where and how the students’ original attempt y y was wrong through retrospection based on the feedback f f . Figure 4 shows an example of self-teaching with Qwen3-8B as student and self-teacher. We summarize SDPO in Algorithm 1 and display the teachers’ reprompt template in Table 2 .

We can derive the SDPO gradient as follows (see Section A.1 for details):

###### Proposition 2.1 .

The gradient of ℒ SDPO \mathcal{L}_{\mathrm{SDPO}} is ∇ ℒ SDPO ( θ ) = 𝔼 y ∼ π θ ( ⋅ ∣ x ) [ ∑ t = 1 | y | 𝔼 y ^ t ∼ π θ ( ⋅ ∣ x , y < t ) [ log π θ ​ ( y ^ t ∣ x , y < t ) π θ ​ ( y ^ t ∣ x , f , y < t ) ⋅ ∇ θ log π θ ( y ^ t ∣ x , y < t ) ] ] . \boldsymbol{\nabla}\mathcal{L}_{\mathrm{SDPO}}(\theta)=\mathbb{E}_{y\sim\pi_{\theta}(\cdot\mid x)}\!\!\left[\sum_{t=1}^{|y|}\mathbb{E}_{\hat{y}_{t}\sim\pi_{\theta}(\cdot\mid x,y_{<t})}\!\!\left[\log\frac{\pi_{\theta}(\hat{y}_{t}\mid x,y_{<t})}{\pi_{\theta}(\hat{y}_{t}\mid x,f,y_{<t})}\cdot\boldsymbol{\nabla}_{\!\!\theta}\,\log\pi_{\theta}(\hat{y}_{t}\mid x,y_{<t})\right]\right]. (2)

### 2.1 Comparison to RLVR

Note that the SDPO gradient is a (negated) logit-level policy gradient where the advantages are estimated using the self-teacher. 2 2 2 See Section A.4 for a detailed comparison of the SDPO gradient to the standard policy gradient. We can therefore reuse standard RLVR implementations and simply swap out the advantages. Let y i y_{i} be the i i -th rollout from a rollout group of size G G for question x x , then comparing GRPO and SDPO we have: A i , t GRPO := r i − mean ​ { r i } i = 1 G ​ (constant in t ) , A i , t SDPO ​ ( y ^ i , t ) = log ⁡ π θ ​ ( y ^ i , t ∣ x , f i , y i , < t ) π θ ​ ( y ^ i , t ∣ x , y i , < t ) . A_{i,t}^{\mathrm{GRPO}}:=r_{i}-\mathrm{mean}\{r_{i}\}_{i=1}^{G}\;\text{{\color[rgb]{0.5,0.5,0.5}(constant in $t$)}},\quad A_{i,t}^{\mathrm{SDPO}}(\hat{y}_{i,t})=\log\frac{\pi_{\theta}(\hat{y}_{i,t}\mid x,f_{i},y_{i,<t})}{\pi_{\theta}(\hat{y}_{i,t}\mid x,y_{i,<t})}. The GRPO advantages are applied only to the sampled token y i , t y_{i,t} and are constant within a rollout y i y_{i} . 3 3 3 We use the GRPO ( Shao et al., 2024 ) advantage without normalization ( Liu et al., 2025b ) . In contrast, the SDPO advantages are zero only for tokens where student and teacher perfectly agree. The SDPO advantage is positive for tokens which are more likely under the teacher while being negative for tokens which are less likely under the teacher. Thus, SDPO can be seen as a direct extension of standard RLVR methods in two ways: 1. from 1-bit feedback to allowing arbitrary sequences of tokens as feedback , and

2. leveraging this rich feedback to estimate dense logit-level advantages .

This tight connection to RLVR methods also enables a straightforward extension of the SDPO gradient from Equation 2 to off-policy data via PPO-style clipped importance sampling ( Schulman et al., 2017 ) , see Section A.4 .

### 2.2 Compute time & memory

The only computational overhead of SDPO compared to GRPO is the additional computation of log-probs from the self-teacher, which can be effectively parallelized and is substantially faster than sequential generation. Figure 5 compares the compute time of SDPO and GRPO. As expected, the compute overhead of SDPO is relatively small. Here, we use a micro batch size of 2; 4 4 4 The micro batch size corresponds to # rollouts we train on at a time while accumulating gradients. compute time can be further reduced by using larger micro batch sizes.

Naively computing the KL divergence between student and teacher requires holding full logits of both models in memory. To avoid this, we approximate the KL divergence in the SDPO loss by performing top- K K distillation (i.e., only computing the top- K K logits of the student and the corresponding logits of the teacher alongside a term capturing the tail probability; cf. Section A.3 ). With a reasonable choice of K K (e.g., K = 100 {K=100} ), this avoids virtually any memory overhead while capturing most of the information.

### 2.3 Stability improvements

We find that two practical modifications significantly enhance the training stability of SDPO. First, we employ a regularized self-teacher, implemented either via an exponential moving average (EMA) of the student parameters or by interpolating the current teacher with the initial teacher (cf. Section A.2 ). As detailed later, both strategies effectively stabilize learning. Second, we adopt the symmetric Jensen-Shannon divergence for the distillation loss; this formulation has similarly been shown to improve stability in on-policy distillation from external teachers ( Agarwal et al., 2024 ) .

## 3 Learning without Rich Environment Feedback

We first evaluate SDPO in standard RLVR environments, where feedback is limited to scalar rewards. Instead of using the scalar reward, SDPO treats successful attempts sampled in the current batch as “feedback” for failed attempts on the same question. By comparing the student’s attempt with a correct solution, the self-teacher can identify where the student was wrong and provide dense credit assignment.

### 3.1 Experimental setting

We evaluate tasks on which the model has not been explicitly fine-tuned: • Science Q&A (Chemistry, Physics, Biology, Materials science): Undergraduate-level scientific reasoning using reasoning subsets (L3) from SciKnowEval ( Feng et al., 2024a ) .

• Tool use : Mapping a tool-API specification and user request to the correct tool call, using ToolAlpaca ( Tang et al., 2023 ) .

We perform a train-test split to test in-domain generalization. We use Qwen3-8B ( Yang et al., 2025a ) and Olmo3-7B-Instruct ( Olmo et al., 2025 ) as initial checkpoints and report avg@16 relative to wall-clock training time, excluding initialization & validation.

##### Baselines.

We compare SDPO to an improved variant of GRPO ( Shao et al., 2024 ) , which incorporates several recent modifications ( Olmo et al., 2025 ; Khatri et al., 2026 ) such as asymmetric clipping ( Yu et al., 2025 ) , avoiding biased normalization ( Liu et al., 2025b ) , and correcting for off-policy data when using efficient inference frameworks ( Yao et al., 2025 ) . We integrate these modifications into a GRPO implementation that represents a strong baseline, as detailed in Equation 13 in Section A.4 . GRPO enables off-policy training through PPO’s clipped importance weighting ( Schulman et al., 2017 ) . We additionally report the special case of on-policy GRPO (matching the hyperparameters of vanilla SDPO). For both baselines, we perform a hyperparameter sweep and report results for the models that achieve the highest validation performance across all target tasks. Hyperparameters and training details are provided in Appendix E . We use the verl library ( Sheng et al., 2025 ) for fast multi-GPU training.

### 3.2 Results

Table 3 summarizes our results. We find that SDPO outperforms GRPO across almost all runs, often leading to substantial improvements. SDPO learns notably faster than GRPO, performing close to 5 hours of GRPO training after only 1 hour of training with SDPO in several cases. SDPO achieves a particularly substantial improvement over GRPO on the Chemistry task, as is displayed in Figure 6 (left) . With Olmo3-7B-Instruct, SDPO achieves the 5h GRPO accuracy in 50 minutes of wall-clock training time , a 6 × 6\times speedup. Moreover, SDPO’s 5h accuracy is more than 10 10 %-points higher than that of GRPO.

We remark that our results with SDPO use strictly on-policy training (i.e., one gradient step per generation batch). Given the known efficiency gains of off-policy methods that perform multiple gradient updates per generation batch, we believe that studying SDPO with off-policy updates is an exciting direction for future work.

### 3.3 Self-distillation learns to reason concisely

We consistently observe that SDPO produces substantially shorter generations than GRPO while achieving higher accuracy. SDPO’s responses are more than 3 × 3\times shorter on average across tasks (cf. Table 8 in Appendix D ). On Chemistry with Olmo3-7B-Instruct, SDPO even achieves an 11 × 11\times reduction in response length relative to GRPO while maintaining higher accuracy (Figure 6 (right) ). While recent progress in RLVR has demonstrated that scaling response length is a powerful driver of emergent reasoning capabilities ( Jaech et al., 2024 ; Guo et al., 2025 ; Muennighoff et al., 2025 ) , our results suggest that effective reasoning need not always be verbose. We find that SDPO improves the efficiency of reasoning.

Qualitatively, we observe that the longer responses from GRPO often stem from “superficial” reasoning rather than necessary analytical steps. GRPO frequently generates filler phrases like “Hmm” and “Wait” or enters circular logical loops that repeat previous steps verbatim. Figure 7 displays a representative example of this phenomenon. Remarkably, SDPO’s generations remain concise and avoid these superficial patterns. This may be explained by SDPO’s dense credit assignment, which assigns a specific advantage to each next-token prediction, leading to sparse advantages (cf. Figure 21 in Appendix F ). By improving the efficiency of reasoning, SDPO reduces inference generation time and demonstrates that reasoning performance can be improved by refining how the model reasons, not just how long it reasons.

## 4 Learning with Rich Environment Feedback

We next evaluate SDPO on coding tasks. Coding is a canonical example of an RL environment that provides rich feedback, such as runtime errors and failed unit tests. Learning to solve these coding problems requires strong credit assignment since the student must identify its precise mistakes to avoid repeating them in the future. LiveCodeBench ( Jain et al., 2025 , LCB;) provides a set of contest-style coding problems, ranging from simple to competition-level. We restrict our evaluation to the most recent LCBv6 subset of LCB, which contains 131 questions released between February and May 2025. We consider a setting with public and private unit tests, common for code contests and coding platforms like LeetCode, where the public tests are used for evaluation during training and the private tests are used for validation ( Chen et al., 2022 ; Le et al., 2022 ; El-Kishky et al., 2025 ; Samadi et al., 2025 ) . 5 5 5 We select public tests as a 50% random subset of private tests.

We use the Qwen3 ( Yang et al., 2025a ) model family for our experiments, with Qwen3-8B as default unless otherwise specified. We report the average accuracy over 4 rollouts and use the same GRPO baseline as outlined in Section 3.1 .

##### Results.

Figure 1 compares the learning curves of SDPO and GRPO on LCBv6. We find that SDPO achieves a substantially higher final accuracy (48.8%) than GRPO (41.2%) while also outperforming the strongest instruct models on the public LCBv6 leaderboard: 6 6 6 On the public leaderboard, the LCBv6 subset can be obtained by selecting February to May 2025. Claude Sonnet 4 (40.5%) and Claude Opus 4 (39.7%). Furthermore, SDPO reaches the final accuracy of GRPO in 4 × 4\times fewer generations. We include an extended comparison to other RLVR baselines that perform similarly to GRPO in Table 9 in the appendix. Differentiating between the easy, medium, and hard questions of LCB, we find that SDPO particularly improves over GRPO in solving medium and hard questions (cf. Figure 15 in the appendix).

### 4.1 Self-distillation benefits from stronger models

A central question for our work is whether SDPO is sensitive to the in-context learning ability of the base model. Intuitively, we expect that SDPO benefits from a strong in-context learner, since this enables the teacher to perform more accurate retrospection.

To answer this question, we perform a scaling study with different model sizes from the Qwen3 ( Yang et al., 2025a ) family. As shown by extensive prior work, the ability to learn in-context increases with model size ( Brown et al., 2020 , e.g.,) . As depicted in Figure 8 , SDPO significantly outperforms GRPO on larger models while only slightly improving over GRPO on smaller models. To determine whether SDPO can also underperform GRPO on a model weaker than Qwen3-0.6B, we performed an additional scaling study with Qwen2.5-Instruct ( Qwen et al., 2024 ) . While outperforming GRPO with Qwen2.5-7B and performing similarly with Qwen2.5-8B, we find that SDPO underperforms GRPO on Qwen2.5-1.5B, as seen in Figure 17 in Appendix D .

### 4.2 Self-distillation performs dense credit assignment

Whereas GRPO assigns a constant advantage to each generated token, SDPO assigns an individual advantage to each possible next token along the generated sequence based on the agreement of student and teacher. At each position t t in the generated sequence y y , there are | 𝒱 | |\mathcal{V}| possible next tokens where 𝒱 \mathcal{V} is the vocabulary. In distillation, this level is typically called the logit-level since it corresponds to the logits of the model. In practice, we approximate the full next-token distribution by the top- K K tokens plus the tail, and as such, SDPO assigns | y | ⋅ ( K + 1 ) |y|\cdot(K+1) unique advantages per sequence. This is illustrated in Figure 9 and allows SDPO to perform dense credit assignment.

A natural question is whether the performance gains of SDPO are due to leveraging rich feedback in RLRF or due to the dense credit assignment of SDPO. To answer this question, we ablate the performance of SDPO in three configurations: • Logit-level SDPO: credit assignment over the 100 most likely tokens (under the student) at each position.

• Token-level SDPO: credit assignment over the most likely token at each position.

• Sequence-level SDPO: We compute SDPO advantages for all generated tokens and average them to produce a single scalar advantage per sequence (as in GRPO). This does not perform denser credit assignment than GRPO but still leverages the rich feedback f f .

As shown in Figure 10 (left) , the dense credit assignment of logit-level SDPO leads to significant performance gains over token-level SDPO and sequence-level SDPO. Nevertheless, even sequence-level SDPO outperforms GRPO, indicating that leveraging rich feedback in RLRF can lead to substantial gains over RLVR methods even without dense credit assignment.

### 4.3 The self-teacher improves during training

Contrary to standard distillation, the self-teacher in SDPO is not frozen, but updated throughout training. This is a critical component of SDPO, since it enables the teacher to improve over time, which means that the student can learn from a stronger target. To investigate whether the self-teacher improves during training, we plot the average accuracy when generating using the self-teacher in Figure 10 (right) . We find that the self-teacher improves significantly during training. Most notably, the student’s accuracy surpasses the initial teacher’s accuracy in later stages of training. This demonstrates that SDPO enables true bootstrapping of a weak model to a strong model, without the initial self-teacher’s performance limiting the final student.

As described in Section 2.3 , SDPO uses a regularized teacher to stabilize training. As can be seen in Table 4 , a non-regularized teacher significantly underperforms the regularized teachers. Furthermore, trust-region and EMA teachers outperform the teacher frozen at the initial teacher’s parameters, showing that the teacher improves through parameter sharing with the student. Yet, SDPO performs well even with a frozen teacher.

### 4.4 On-policy self-distillation avoids catastrophic forgetting

Prior work has shown that a key benefit of on-policy algorithms, such as GRPO, is that models tend not to forget previously obtained capabilities ( Shenfeld et al., 2026b ; Chen et al., 2025b ; Lu & Thinking Machines Lab, 2025 ) . This is practically desirable since it enables continual training pipelines where a model is trained sequentially on diverse tasks without the need to retrain from scratch. To evaluate forgetting, we test the final checkpoints of GRPO and SDPO on diverse holdout tasks: IFEval ( Zhou et al., 2023 ) , which tests the ability of a model to follow precise format instructions; ArenaHard-v2 ( Li et al., 2025a ) , which is an LLM-judged benchmark of real-world instruction-following prompts derived from LMArena ( Chiang et al., 2024 ) ; and MMLU-Pro ( Wang et al., 2024b ) , which tests broad multi-task knowledge and reasoning. As displayed in Table 5 , SDPO learns the new task while mitigating degradation of initial capabilities, overall achieving a better performance–forgetting tradeoff than GRPO.

##### Off-policy self-distillation baseline.

As an additional baseline, we consider training the student via supervised fine-tuning (SFT) on successful generations from the self-teacher ( Scheurer et al., 2023 ; Dou et al., 2024 ; Zhou et al., 2025 ) . 7 7 7 SFT on a teacher’s predictions is a standard off-policy distillation approach ( Kim & Rush, 2016 ) . This requires 2 × 2\times the generations of SDPO for the same number of steps, since we have to generate from both the student and the teacher. We report SFT on the successes of the self-teacher, which achieves a higher accuracy than also including initial successes from the student in the SFT data. As shown in Table 5 , SFT on the self-teacher significantly underperforms SDPO on LCBv6, while leading to worse forgetting of prior capabilities. This mirrors prior findings on the instability of off-policy imitation ( Agarwal et al., 2024 , see, e.g.,) .

### 4.5 Can GRPO and SDPO be combined?

GRPO utilizes Monte Carlo advantages, which are unbiased with respect to the objective of maximizing expected reward J ( θ ) := 𝔼 y ∼ π θ ( ⋅ ∣ x ) [ r ( y ∣ x ) ] J(\theta):=\smash{\mathbb{E}_{y\sim\pi_{\theta}(\cdot\mid x)}{}\left[r(y\mid x)\right]} . In contrast, SDPO advantages are inherently biased with respect to J ⁡ ( θ ) J(\theta) due to being computed from rich feedback and a self-teacher. This dichotomy parallels the fundamental distinction between Monte Carlo and bootstrapped advantages in RL: while the latter are biased, they typically yield lower variance ( Sutton & Barto, 1998 ; Schulman et al., 2016 ) . This motivates a hybrid approach that combines reward-derived GRPO advantages with feedback-derived SDPO advantages: A i , t SDPO + GRPO ​ ( y ^ i , t ) := λ ​ A i , t GRPO ​ ( y ^ i , t ) + ( 1 − λ ) ​ A i , t SDPO ​ ( y ^ i , t ) , λ ∈ [ 0 , 1 ] . A_{i,t}^{\mathrm{SDPO+GRPO}}(\hat{y}_{i,t}):=\lambda A_{i,t}^{\mathrm{GRPO}}(\hat{y}_{i,t})+(1-\lambda)A_{i,t}^{\mathrm{SDPO}}(\hat{y}_{i,t}),\quad\lambda\in[0,1]. (3)

As shown in Figure 11 , SDPO+GRPO appears to be more robust to weaker models than SDPO. Intuitively, in a weaker model such as Qwen3-0.6B, the SDPO advantages are less reliable, and hence including the GRPO advantage helps to stabilize training. In contrast, we find that SDPO+GRPO slightly underperforms SDPO on stronger models such as Qwen3-8B. This suggests that the signal of GRPO, only informed by a scalar reward, can be actively harmful with a strong initial model.

### 4.6 Which feedback is most informative?

To understand which type of rich feedback is most informative, we ablate the three types of feedback present in a verifiable environment like code generation: the sample solution (if a successful rollout is available in the current rollout group), the environment output (such as runtime errors), and the student’s original attempt.

##### Sample solutions.

Including a sample solution from a failed attempt’s rollout group (if available) closely mirrors the group-relative advantages of GRPO. We emphasize that these sample solutions are always generated by the student, as in GRPO, and do not require an expert model. They allow for disincentivizing unsuccessful approaches if the model is already able to solve the question. However, unlike GRPO where all tokens receive the same negative advantage, the self-teacher can identify specific mistakes and provide feedback on how to fix them.

##### Environment output.

The environment output describes the state of the environment after the student’s attempt. This is complementary to sample solutions since it can provide useful signal even if the student has never solved the question before (a setting we explore extensively in Section 5 ). Leveraging environment output is a key differentiating factor between RLRF and RLVR settings.

##### Student’s original attempt.

The student’s original attempt y y does not have to be included in the reprompting template of the teacher. Indeed, we find that including it biases the teacher towards the student’s attempt (cf. Table 6 ). This reduces the entropy of the student’s distribution (particularly for initially uncertain tokens), thereby reducing exploration.

We summarize results in Table 6 where we evaluate the effect on SDPO training as well as the direct impact on the self-teacher. We find that environment output & sample solutions are complementary, each providing informative feedback. Generally, we observe that performance is not sensitive to syntactic variations of the reprompting template from Table 2 .

## 5 Solving Hard Questions via Test-Time Self-Distillation

In Sections 3 and 4 , we have demonstrated that SDPO can substantially improve over RLVR methods when performing “train-time RL” for reasoning tasks. We now turn to a test-time setting where the model is given only a single hard (binary-reward) question x x and must discover a solution as quickly as possible:

###### Definition 5.1 (Discovery time) .

The discovery time is the number of trials needed until a solution is found (i.e., the smallest k k with the k k -th attempt y k y_{k} receiving reward 1).

Based on this notion, we can define a measure of the efficacy of discovery: discovery ​ @ ​ k := ℙ ⁡ ( discovery time ≤ k ) = ℙ ⁡ ( r ⁡ ( y 1 ∣ x ) = 1 or r ⁡ ( y 2 ∣ x ) = 1 or …or r ⁡ ( y k ∣ x ) = 1 ) , \displaystyle\begin{split}\mathrm{discovery@}k:=&\ \mathbb{P}(\text{discovery time $\leq k$})\\ =&\ \mathbb{P}(\text{$r(y_{1}\mid x)=1$ or $r(y_{2}\mid x)=1$ or \ldots or $r(y_{k}\mid x)=1$}),\end{split} (4) where the probability is over any randomness in the algorithm producing y k y_{k} and the rewards. Thus, the discovery@ k k metric quantifies the probability of discovering the solution within k k steps. 8 8 8 Our proposed discovery@ k k metric is a canonical metric in the study of runtime speedup (i.e., time until termination, Dolan & Moré (2002) ). While prior work has studied discovery with continuous rewards ( Novikov et al., 2025 ; Yuksekgonul et al., 2026 , e.g.,) , discovery with language models in sparse or binary-reward settings does not allow “hill-climbing” a continuous reward and has remained less well understood.

The most naive approach to discovery in binary-reward tasks is to sample repeatedly i.i.d. from the base model, also known as best-of- k k . The canonical pass@ k k metric for best-of- k k sampling is exactly the probability of discovering at least one solution within k k independent samples from a fixed model, coinciding with discovery@ k k . The discovery@ k k metric generalizes pass@ k k to algorithms that sample attempts sequentially. A common sequential approach re-prompts the base model with additional context from previous attempts ( Madaan et al., 2023 ; Shinn et al., 2023 ) . We refer to this as multi-turn sampling. Here, the model itself does not change, only its context evolves over time.

Performing RLVR on the question x x does not improve over best-of- k k sampling from the base model, since a binary reward provides no signal until the first solution has already been found. 9 9 9 For this reason, several works consider explicitly constructing curricula of solvable questions ( Zhao et al., 2025 ; Huang et al., 2026 ; Diaz-Bone et al., 2025 ; Hübotter et al., 2025b , e.g.,) , which self-distillation avoids. Other work found that RLVR yields limited improvement on hard questions ( Yue et al., 2025 ) . An RLRF method like SDPO does not face the same limitation, as it receives rich feedback from the environment after each attempt. This rich feedback enables the model to repeatedly “correct” its mistakes as it encounters them and receives feedback, even before ever discovering a solution. In contrast to multi-turn sampling, SDPO repeatedly compresses context c = ( y k , f k ) c=(y_{k},f_{k}) by distilling π θ ( ⋅ ∣ x , c ) \pi_{\theta}(\cdot\mid x,c) into a model π θ ′ ( ⋅ ∣ x ) \pi_{\theta^{\prime}}(\cdot\mid x) as we illustrate in Figure 12 . This self-distillation enables SDPO to continually learn over long contexts, whereas the memory bottleneck of transformers inherently limits the context length of multi-turn sampling ( Vaswani et al., 2017 ) . In this section, we seek to answer the question: Can repeatedly compressing context into model weights via self-distillation accelerate discovery for hard questions?

### 5.1 Experimental setting

We consider a particularly challenging subset of questions from LCBv6 that are at Qwen3-8B’s performance ceiling and require significant test-time sampling to find any solution. Concretely, we define two groups using Qwen3-8B’s pass@ k k : Hard tasks with pass@ ​ 64 < 0.5 {\text{pass@}64<0.5} and very hard tasks with pass@ ​ 64 < 0.03 \text{pass@}64<0.03 . Among these, we retain questions for which any of best-of- k k , multi-turn, or SDPO find at least one solution within 512 512 steps across 5 5 seeds. This results in 19 hard and 9 very hard questions.

For best-of- k k sampling under the base model, we report the standard pass ​ @ ​ k \text{pass}@k estimate ( Chen et al., 2021b ) from 2944 independent rollouts. As multi-turn sampling, we sequentially reprompt the model in-context using the concatenated feedback from previous attempts. To remain within Qwen3-8B’s 40k-token context limit, we employ a first-in, first-out sliding window, discarding the earliest feedback once the maximum prompt length (32k tokens) is reached. We ablate the multi-turn reprompting strategy in Figure 19 in Appendix D and find that retaining only past feedback while forgetting earlier attempts significantly outperforms the baseline that additionally retains past attempts. We evaluate SDPO with a batch size of 16. We ablate this choice in Figure 19 in Appendix D and find that overall performance differences are marginal, yet smaller batch sizes are beneficial for improvements at low generation budgets, while larger batch sizes result in more stable updates that still learn to solve questions at later stages into the run.

### 5.2 Results

Figure 13 compares discovery ​ @ ​ k \text{discovery}@k for SDPO, multi-turn sampling, and best-of- k k sampling on very hard (left) and hard (right) questions from LCBv6. Across both difficulty levels, SDPO achieves substantially higher discovery ​ @ ​ k \text{discovery}@k rates at almost all generation budgets.

On very hard tasks, multi-turn and best-of- k k largely fail to solve questions within the available generation budget, achieving discovery@2750 of only 35.6 % 35.6\% and 41.5 % {41.5}\% , respectively, whereas SDPO discovers a solution in 53.2 % {53.2}\% of cases. SDPO not only solves more questions overall but also does so with substantially fewer attempts. Notably, to reach a 22 % 22\% discovery probability on very hard questions, SDPO requires approximately 3 × 3\times fewer generations than best-of- k k and multi-turn sampling. On hard tasks, SDPO reaches a 78 % {78}\% discovery@2750 probability while achieving a 67 % 67\% discovery probability with roughly 2.4 × 2.4\times fewer generations than best-of- k k and multi-turn sampling. Overall, multi-turn and best-of- k k sampling solve only 68.4 % {68.4}\% and 72.3 % {72.3}\% of questions, respectively. The context window length for multi-turn sampling is reached after 837 ( ± 466 \pm 466 ) steps for hard questions and after 1007 ( ± 349 \pm 349 ) steps for very hard questions, offering a possible explanation for its diminishing gains at high generation budgets.

##### Question 3 is only solved by SDPO.

SDPO solves all questions that are solved by best-of- k k and multi-turn sampling. Beyond that, SDPO uniquely discovers a solution for Q3, which is neither solvable with multi-turn sampling nor with best-of- k k sampling within 2750 attempts. In contrast, SDPO first discovers a solution for Q3 after 321 attempts, which corresponds to 20 iteration steps of self-distillation based on feedback with a batch size of 16. We include detailed per-question results in Table 10 in Appendix D .

##### The initial self-teacher does not solve hard questions.

Notably, the self-teacher’s initial accuracy is < 1 <1 % for almost all questions, and even exactly 0 0 % on 78 78 % of them ( Table 11 in Appendix D ). This shows that a single turn of in-context feedback is insufficient to solve the problem. Despite this, the self-teacher’s credit assignment is sufficiently effective for SDPO to iteratively refine the policy and eventually solve these questions.

## 6 Related Work

### 6.1 Reinforcement Learning with LLMs

Recently, large-scale RL training on diverse tasks has significantly improved the performance of LLMs on general reasoning tasks ( Guo et al., 2025 ; Kimi et al., 2025 ; Olmo et al., 2025 ; Jaech et al., 2024 ; Lambert et al., 2025 ) . This progress is primarily enabled by RLVR methods that use Monte Carlo estimates of rewards, such as STaR or GRPO ( Zelikman et al., 2022 ; Shao et al., 2024 ) , similar to the classical REINFORCE algorithm ( Williams, 1992 ) . While several traditional RLVR algorithms rely on learning separate value networks ( Schulman et al., 2017 ) , they incur substantial memory costs and retain the information bottleneck of scalar rewards.

In the RLVR setting, it is common for an (outcome) reward to be given only at the end of a sequence. To improve credit assignment, several works learn so-called process reward models (PRMs) that estimate rewards for each step in the sequence ( Lightman et al., 2023 ; Wang et al., 2024a ; Setlur et al., 2025 ) . Unlike our RLRF setting, PRMs are typically trained on scalar rewards, either on value estimates for intermediate states or on outcome rewards ( Cui et al., 2025 ) . Unlike the self-teacher in SDPO, PRMs are a distinct model from the student, introducing significant memory overhead. Our work shows that each language model is implicitly a PRM through retrospection if given rich feedback.

Conceptually, our work is related to “bootstrapping your own latent” ( Grill et al., 2020 , BYOL;) and “expert iteration” ( Anthony et al., 2017 ) where a student is bootstrapped by repeatedly imitating an improved version of itself (called the “expert”). Canonically, the expert combines the student with test-time search, such as tree search ( Anthony et al., 2017 ) or majority voting ( Zuo et al., 2025 ) . In contrast, SDPO leverages the student’s ability to learn from rich feedback provided in-context, which is related to “augmented views” in BYOL.

### 6.2 Learning from Rich Feedback and through Retrospection

Beyond scalar outcome rewards, recent works have leveraged rich execution or verbal feedback to guide generation ( Gehring et al., 2025 ; Feng et al., 2024b ; Yuksekgonul et al., 2025 ) . A primary line of research focuses on translating verbal feedback into reward functions for RL. This is often achieved by mapping feedback to discrete token-level rewards using an external frozen model ( Wang et al., 2026 ) , or by employing strong external LLMs to explicitly construct state-wise reward functions ( Goyal et al., 2019 ; Xie et al., 2024 ; Urcelay et al., 2026 ) .

Alternatively, feedback can be utilized without explicit reward modeling. Several approaches focus on in-context improvement without integrating the process into the RL optimization loop ( Chen et al., 2021a ; Madaan et al., 2023 ; Shinn et al., 2023 ; Yao et al., 2024 ; Yuksekgonul et al., 2025 ; Lee et al., 2025 ) . Others manually curate preference datasets by pairing responses before and after feedback to train with direct preference optimization ( Stephan et al., 2024 ; Lee et al., 2024 ) , though this requires additional generation and lacks the direct credit assignment of SDPO. Various recent works bootstrap thinking traces from known answers, using these answers as rich feedback ( Zhou et al., 2026 ; Hatamizadeh et al., 2026 ; Zhang et al., 2025 ) .

A central object in several recent works is a feedback-conditioned policy π θ ​ ( y ∣ x , f ) \pi_{\theta}(y\mid x,f) , which learns answers y y that lead to feedback f f ( Liu et al., 2023 ; Zhang et al., 2023 ; Luo et al., 2025 ) , typically through supervised objectives. The idea behind these approaches is to deploy a policy conditioned on desirable (i.e., positive) feedback for deployment. This approach is conceptually related to goal-conditioned RL ( Schaul et al., 2015 ; Liu et al., 2025a ) , where one can learn from negative examples through goal relabeling ( Andrychowicz et al., 2017 ) . Feedback-conditioned policies view feedback as a goal, whereas RLRF views feedback as a state that can be used to determine whether the goal x x is achieved. Unlike SDPO, these methods do not use feedback for credit assignment in negative trajectories, but rather as a data transformation for goal relabeling.

### 6.3 Distillation

Distillation is frequently employed as an alternative to supervised fine-tuning (SFT) when a strong teacher model is available. Distillation transfers capabilities by training a student to mimic the output distribution or intermediate representations of the teacher ( Hinton et al., 2015 ; Romero et al., 2015 ; Kim & Rush, 2016 ; Sanh et al., 2019 ; Xie et al., 2020 ) . While often performed on fixed off-policy datasets, to address the distribution shift between training and inference, recent works explore on-policy distillation, where the student learns from feedback on its own generations provided by an external teacher ( Agarwal et al., 2024 ; Gu et al., 2024 ; Yang et al., 2025a ; Lu & Thinking Machines Lab, 2025 ) . This mitigates the train-test mismatch, which relates closely to earlier work on online imitation learning ( Ross et al., 2011 ) .

### 6.4 Self-Distillation

The concept of self-distillation was first proposed by Snell et al. (2022) in a setting akin to supervised learning, introducing the idea of sampling from a model provided with extra context and training the same model to mimic these predictions without that context. This mechanism has proven effective for compressing behavior ( Bai et al., 2022 ; Choi et al., 2022 ; Yang et al., 2024 ; Yang et al., 2025b ) and factual information ( Eyuboglu et al., 2026 ; Kujanpää et al., 2025 ; Cao et al., 2025a ) into model weights. Beyond compressing a fixed context into model weights, recent works have used self-distillation to learn from environment feedback ( Scheurer et al., 2023 ; Dou et al., 2024 ; Zhou et al., 2025 ; Mitra & Ulukus, 2025 ; Song et al., 2026 ) . These approaches use an off-policy self-distillation objective, which we find to substantially underperform SDPO’s on-policy learning. Off-policy self-distillation trains the student on generations from the teacher, whereas SDPO trains the student to avoid mistakes in its own generations. In concurrent work, Chen et al. (2025c) apply on-policy self-distillation to grid world settings where feedback is a scalar reward, and a reflection stage in the self-teacher diagnoses possible mistakes, showing improved credit assignment compared to learning value networks for advantage estimation. Other concurrent work studies SDPO on a fixed dataset of expert demonstrations, without online environment interaction ( Shenfeld et al., 2026a ; Zhao et al., 2026 ) .

## 7 Conclusion, Limitations, and Future Work

We introduced Reinforcement Learning with Rich Feedback (RLRF), a paradigm where environments provide tokenized feedback beyond scalar rewards, and argued that this removes a key information bottleneck of RLVR. We then proposed Self-Distillation Policy Optimization (SDPO), which uses the current policy as a feedback-conditioned self-teacher and distills its corrected log-probabilities into the student. This leverages the model’s ability to learn from context for dense credit assignment. We further demonstrated that SDPO can be implemented as a minimal, drop-in modification to standard RLVR pipelines.

Empirically, SDPO demonstrates superior sample efficiency and wall-clock convergence compared to GRPO on reasoning tasks, even when training in standard RLVR environments without rich feedback. SDPO’s gains grow with model scale, suggesting that the capacity for self-correction scales with the model’s in-context learning capabilities. Moreover, we show that performing SDPO at test time on individual hard binary-reward tasks accelerates the discovery of solutions compared to strong baselines.

SDPO enables learning from rich feedback in a way that is arguably closer to human cognition: utilizing precise outcomes rather than just binary rewards. By allowing the model to determine retrospectively how it should have acted, we demonstrate that language models can convert diverse tokenized feedback into effective self-supervision.

##### Limitations.

Our findings show that SDPO’s performance depends on a model’s in-context learning ability, suggesting that SDPO is primarily applicable for RL-training stronger base models, while it can underperform GRPO on weaker models. Moreover, performance depends on the quality of the environment feedback. If the environment provides uninformative or misleading feedback, a model may not be able to learn from it through SDPO. Finally, SDPO adds a small computational overhead compared to GRPO for computing the log-probs of the retrospective model. While often negligible, this may be a larger overhead for smaller models with shorter generation lengths, where generation time is comparatively small.

##### Future Work.

Our work highlights several exciting directions for future research: • Long-horizon and agentic settings. RLRF is particularly appealing when trajectories are long or expose information about intermediate states. Evaluating SDPO in agentic environments is a natural next step.

• Training dynamics at scale. Beyond our evaluation on LiveCodeBench, it would be particularly interesting to scale SDPO to large multi-task RL training runs and further study its scaling properties with frontier base models.

• Beyond verifiable rewards. While we focused on verifiable code generation, many tasks provide textual feedback without a ground-truth verifier. Investigating whether SDPO’s retrospection mechanism can improve alignment in open-ended text generation or continuous-reward tasks remains an open empirical question.

• Behavioral differences in reasoning. We observed that SDPO induces qualitatively different reasoning patterns than GRPO, notably avoiding the latter’s tendency toward verbosity and superficial reasoning. Future work should systematically study how individual aspects, such as the reprompt template, influence behavior.

## Author Contributions

Jonas Hübotter conceived of the project in summer 2025 and has been working on it full-time since then, leading the team. Jonas proposed the conceptual framework of self-distillation for credit assignment with input from Lejs, implemented the algorithm with help from others, led the quantitative experiments on LCBv6, and led the writing of the paper.

Frederike Lübeck led the design of the code environment, led the design and evaluation of the TTT setting in Section 5 with input from Jonas, contributed to the project direction in discussions, and contributed significantly to the writing of the paper.

Lejs Behric noted the dense credit assignment of knowledge distillation with strong teacher models in discussions with Jonas, inspiring the idea of self-distillation. Further, Lejs led the evaluation of different teacher templates, co-led the development of a tool for qualitative analysis of runs with Marco and Daniel, helped implement parts of the algorithm, and contributed to the project direction in discussions.

Anton Baumann joined in December 2025 and led the evaluation of SDPO without rich feedback in Section 3 with input from Jonas, and contributed to the writing of the paper.

Marco Bagatella and Daniel Marta co-led the development of a tool for qualitative analysis of runs with Lejs, contributed to the training infrastructure, and contributed to the project direction in discussions.

Ido Hakimi significantly contributed to the initial codebase and experimental setup, contributed early algorithmic ideas, and contributed to the project direction in discussions.

Idan Shenfeld, Thomas Kleine Buening, Carlos Guestrin, and Andreas Krause supported this project, with Idan and Carlos joining in December 2025. They made significant contributions to the project direction in discussions and gave valuable advice on our presentation. Thomas and Idan, in particular, significantly contributed to the development of core algorithmic ideas and design of experiments. Thomas further evaluated checkpoints on holdout benchmarks. Carlos suggested the qualitative analysis of reasoning traces in Figure 7 and the presentation of TTT results in Section 5 . Andreas pointed out valuable connections to existing work in RL which shaped the direction of the project.

## Acknowledgments

We would like to thank Akira Yoshiyama, Yassir Akram, Parnian Kassraie, Jonathan Thomm, Roman Vorushin, Afra Amini, Imanol Schlag, Yu Sun, and Moritz Hardt for helpful discussions. We thank Eduard Durech for helpful conversations regarding the scaling of RL fine-tuning and for his technical guidance on distributed infrastructure and long-context optimization. We are grateful to Ruixu Zhou from Tsinghua University & the Tencent Hunyuan Team for pointing out an error in the initially derived gradient estimator. Furthermore, we would like to thank Leander Diaz-Bone for supporting dataset generation.

This project was supported through the Swiss AI compute grant a156 and, in part, compute grant infra01. JH was supported by the Swiss National Science Foundation under NCCR Automation, grant agreement 51NF40 180545. FL and MB were supported by the ETH-MPI Center for Learning Systems. TKB and IH were supported by an ETH AI Center Postdoctoral Fellowship. DM was supported by the Knut and Alice Wallenberg Foundation.

## References

Agarwal et al. (2024) Rishabh Agarwal, Nino Vieillard, Yongchao Zhou, Piotr Stanczyk, Sabela Ramos Garea, Matthieu Geist, and Olivier Bachem. On-policy distillation of language models: Learning from self-generated mistakes. In ICLR , 2024.

Akyürek et al. (2025) Ekin Akyürek, Mehul Damani, Adam Zweiger, Linlu Qiu, Han Guo, Jyothish Pari, Yoon Kim, and Jacob Andreas. The surprising effectiveness of test-time training for few-shot learning. In ICML , 2025.

Amini et al. (2025) Afra Amini, Tim Vieira, and Ryan Cotterell. Better estimation of the kullback–leibler divergence between language models. In NeurIPS , 2025.

Andrychowicz et al. (2017) Marcin Andrychowicz, Filip Wolski, Alex Ray, Jonas Schneider, Rachel Fong, Peter Welinder, Bob McGrew, Josh Tobin, Pieter Abbeel, and Wojciech Zaremba. Hindsight experience replay. In NeurIPS , 2017.

Anthony et al. (2017) Thomas Anthony, Zheng Tian, and David Barber. Thinking fast and slow with deep learning and tree search. In NeurIPS , 2017.

Bai et al. (2022) Yuntao Bai, Saurav Kadavath, Sandipan Kundu, Amanda Askell, Jackson Kernion, Andy Jones, Anna Chen, Anna Goldie, Azalia Mirhoseini, Cameron McKinnon, et al. Constitutional ai: Harmlessness from ai feedback. arXiv preprint arXiv:2212.08073 , 2022.

Behrouz et al. (2025) Ali Behrouz, Peilin Zhong, and Vahab Mirrokni. Titans: Learning to memorize at test time. In NeurIPS , 2025.

Berner et al. (2019) Christopher Berner, Greg Brockman, Brooke Chan, Vicki Cheung, Przemysław Debiak, Christy Dennison, David Farhi, Quirin Fischer, Shariq Hashme, Chris Hesse, et al. Dota 2 with large scale deep reinforcement learning. arXiv preprint arXiv:1912.06680 , 2019.

Brown et al. (2020) Tom B. Brown, Benjamin Mann, Nick Ryder, Melanie Subbiah, Jared Kaplan, Prafulla Dhariwal, Arvind Neelakantan, Pranav Shyam, Girish Sastry, Amanda Askell, et al. Language models are few-shot learners. arXiv preprint ArXiv:2005.14165 , 2020.

Cao et al. (2025a) Bowen Cao, Deng Cai, and Wai Lam. Infiniteicl: Breaking the limit of context window size via long short-term memory transformation. In ACL , 2025a.

Cao et al. (2025b) Meng Cao, Shuyuan Zhang, Xiao-Wen Chang, and Doina Precup. Scar: Shapley credit assignment for more efficient rlhf. arXiv preprint arXiv:2505.20417 , 2025b.

Chan et al. (2024) Alex J Chan, Hao Sun, Samuel Holt, and Mihaela Van Der Schaar. Dense reward for free in reinforcement learning from human feedback. In ICML , 2024.

Chen et al. (2025a) Aili Chen, Aonian Li, Bangwei Gong, Binyang Jiang, Bo Fei, Bo Yang, Boji Shan, Changqing Yu, Chao Wang, Cheng Zhu, et al. Minimax-m1: Scaling test-time compute efficiently with lightning attention. arXiv preprint arXiv:2506.13585 , 2025a.

Chen et al. (2022) Bei Chen, Fengji Zhang, Anh Nguyen, Daoguang Zan, Zeqi Lin, Jian-Guang Lou, and Weizhu Chen. Codet: Code generation with generated tests. In ICLR , 2022.

Chen et al. (2025b) Howard Chen, Noam Razin, Karthik Narasimhan, and Danqi Chen. Retaining by doing: The role of on-policy data in mitigating forgetting. arXiv preprint arXiv:2510.18874 , 2025b.

Chen et al. (2021a) Lili Chen, Kevin Lu, Aravind Rajeswaran, Kimin Lee, Aditya Grover, Misha Laskin, Pieter Abbeel, Aravind Srinivas, and Igor Mordatch. Decision transformer: Reinforcement learning via sequence modeling. In NeurIPS , 2021a.

Chen et al. (2021b) Mark Chen, Jerry Tworek, Heewoo Jun, Qiming Yuan, Henrique Ponde De Oliveira Pinto, Jared Kaplan, Harri Edwards, Yuri Burda, Nicholas Joseph, Greg Brockman, et al. Evaluating large language models trained on code. arXiv preprint arXiv:2107.03374 , 2021b.

Chen et al. (2025c) Wentse Chen, Jiayu Chen, Fahim Tajwar, Hao Zhu, Xintong Duan, Ruslan Salakhutdinov, and Jeff Schneider. Retrospective in-context learning for temporal credit assignment with large language models. In NeurIPS , 2025c.

Chiang et al. (2024) Wei-Lin Chiang, Lianmin Zheng, Ying Sheng, Anastasios Nikolas Angelopoulos, Tianle Li, Dacheng Li, Banghua Zhu, Hao Zhang, Michael Jordan, Joseph E Gonzalez, et al. Chatbot arena: An open platform for evaluating llms by human preference. In ICML , 2024.

Choi et al. (2022) Eunbi Choi, Yongrae Jo, Joel Jang, and Minjoon Seo. Prompt injection: Parameterization of fixed inputs. arXiv preprint arXiv:2206.11349 , 2022.

Cui et al. (2025) Ganqu Cui, Lifan Yuan, Zefan Wang, Hanbin Wang, Wendi Li, Bingxiang He, Yuchen Fan, Tianyu Yu, Qixin Xu, Weize Chen, et al. Process reinforcement through implicit rewards. arXiv preprint arXiv:2502.01456 , 2025.

Diaz-Bone et al. (2025) Leander Diaz-Bone, Marco Bagatella, Jonas Hübotter, and Andreas Krause. Discover: Automated curricula for sparse-reward reinforcement learning. In NeurIPS , 2025.

Dolan & Moré (2002) Elizabeth D Dolan and Jorge J Moré. Benchmarking optimization software with performance profiles. Mathematical programming , 91(2), 2002.

Dou et al. (2024) Zi-Yi Dou, Cheng-Fu Yang, Xueqing Wu, Kai-Wei Chang, and Nanyun Peng. Re-rest: Reflection-reinforced self-training for language agents. In EMNLP , 2024.

El-Kishky et al. (2025) Ahmed El-Kishky, Alexander Wei, Andre Saraiva, Borys Minaiev, Daniel Selsam, David Dohan, Francis Song, Hunter Lightman, Ignasi Clavera, Jakub Pachocki, et al. Competitive programming with large reasoning models. arXiv preprint arXiv:2502.06807 , 2025.

Eyuboglu et al. (2026) Sabri Eyuboglu, Ryan Ehrlich, Simran Arora, Neel Guha, Dylan Zinsley, Emily Liu, Will Tennien, Atri Rudra, James Zou, Azalia Mirhoseini, et al. Cartridges: Lightweight and general-purpose long context representations via self-study. In ICLR , 2026.

Feng et al. (2024a) Kehua Feng, Keyan Ding, Weijie Wang, Xiang Zhuang, Zeyuan Wang, Ming Qin, Yu Zhao, Jianhua Yao, Qiang Zhang, and Huajun Chen. Sciknoweval: Evaluating multi-level scientific knowledge of large language models. arXiv preprint arXiv:2406.09098 , 2024a.

Feng et al. (2024b) Xidong Feng, Bo Liu, Yan Song, Haotian Fu, Ziyu Wan, Girish A Koushik, Zhiyuan Hu, Mengyue Yang, Ying Wen, and Jun Wang. Natural language reinforcement learning. arXiv preprint arXiv:2411.14251 , 2024b.

Gehring et al. (2025) Jonas Gehring, Kunhao Zheng, Jade Copet, Vegard Mella, Quentin Carbonneaux, Taco Cohen, and Gabriel Synnaeve. Rlef: Grounding code llms in execution feedback with reinforcement learning. In ICML , 2025.

Goyal et al. (2019) Prasoon Goyal, Scott Niekum, and Raymond J Mooney. Using natural language for reward shaping in reinforcement learning. In IJCAI , 2019.

Grill et al. (2020) Jean-Bastien Grill, Florian Strub, Florent Altché, Corentin Tallec, Pierre Richemond, Elena Buchatskaya, Carl Doersch, Bernardo Avila Pires, Zhaohan Guo, Mohammad Gheshlaghi Azar, et al. Bootstrap your own latent-a new approach to self-supervised learning. In NeurIPS , 2020.

Gu et al. (2024) Yuxian Gu, Li Dong, Furu Wei, and Minlie Huang. Minillm: Knowledge distillation of large language models. 2024.

Guha et al. (2026) Etash Guha, Ryan Marten, Sedrick Keh, Negin Raoof, Georgios Smyrnis, Hritik Bansal, Marianna Nezhurina, Jean Mercat, Trung Vu, Zayne Sprague, et al. Openthoughts: Data recipes for reasoning models. In ICLR , 2026.

Guo et al. (2025) Daya Guo, Dejian Yang, Haowei Zhang, Junxiao Song, Ruoyu Zhang, Runxin Xu, Qihao Zhu, Shirong Ma, Peiyi Wang, Xiao Bi, et al. Deepseek-r1: Incentivizing reasoning capability in llms via reinforcement learning. arXiv preprint arXiv:2501.12948 , 2025.

Haarnoja et al. (2018) Tuomas Haarnoja, Aurick Zhou, Pieter Abbeel, and Sergey Levine. Soft actor-critic: Off-policy maximum entropy deep reinforcement learning with a stochastic actor. In ICML , 2018.

Hardt & Sun (2024) Moritz Hardt and Yu Sun. Test-time training on nearest neighbors for large language models. In ICLR , 2024.

Hatamizadeh et al. (2026) Ali Hatamizadeh, Syeda Nahida Akter, Shrimai Prabhumoye, Jan Kautz, Mostofa Patwary, Mohammad Shoeybi, Bryan Catanzaro, and Yejin Choi. Rlp: Reinforcement as a pretraining objective. In ICLR , 2026.

Hinton et al. (2015) Geoffrey Hinton, Oriol Vinyals, and Jeff Dean. Distilling the knowledge in a neural network. arXiv preprint arXiv:1503.02531 , 2015.

Huang et al. (2026) Chengsong Huang, Wenhao Yu, Xiaoyang Wang, Hongming Zhang, Zongxia Li, Ruosen Li, Jiaxin Huang, Haitao Mi, and Dong Yu. R-zero: Self-evolving reasoning llm from zero data. In ICLR , 2026.

Hübotter et al. (2026) Jonas Hübotter, Patrik Wolf, Alexander Shevchenko, Dennis Jüni, Andreas Krause, and Gil Kur. Specialization after generalization: Towards understanding test-time training in foundation models. In ICLR , 2026.

Hübotter et al. (2025a) Jonas Hübotter, Sascha Bongni, Ido Hakimi, and Andreas Krause. Efficiently learning at test-time: Active fine-tuning of llms. In ICLR , 2025a.

Hübotter et al. (2025b) Jonas Hübotter, Leander Diaz-Bone, Ido Hakimi, Andreas Krause, and Moritz Hardt. Learning on the job: Test-time curricula for targeted reinforcement learning. arXiv preprint arXiv:2510.04786 , 2025b.

Jaech et al. (2024) Aaron Jaech, Adam Kalai, Adam Lerer, Adam Richardson, Ahmed El-Kishky, Aiden Low, Alec Helyar, Aleksander Madry, Alex Beutel, Alex Carney, et al. Openai o1 system card. arXiv preprint arXiv:2412.16720 , 2024.

Jain et al. (2025) Naman Jain, King Han, Alex Gu, Wen-Ding Li, Fanjia Yan, Tianjun Zhang, Sida Wang, Armando Solar-Lezama, Koushik Sen, and Ion Stoica. Livecodebench: Holistic and contamination free evaluation of large language models for code. In ICLR , 2025.

Kaelbling et al. (1998) Leslie Pack Kaelbling, Michael L Littman, and Anthony R Cassandra. Planning and acting in partially observable stochastic domains. Artificial intelligence , 101(1-2), 1998.

Kazemnejad et al. (2025) Amirhossein Kazemnejad, Milad Aghajohari, Eva Portelance, Alessandro Sordoni, Siva Reddy, Aaron Courville, and Nicolas Le Roux. Vineppo: Refining credit assignment in rl training of llms. In ICML , 2025.

Khatri et al. (2026) Devvrit Khatri, Lovish Madaan, Rishabh Tiwari, Rachit Bansal, Sai Surya Duvvuri, Manzil Zaheer, Inderjit S Dhillon, David Brandfonbrener, and Rishabh Agarwal. The art of scaling reinforcement learning compute for llms. In ICLR , 2026.

Kim & Rush (2016) Yoon Kim and Alexander M Rush. Sequence-level knowledge distillation. In EMNLP , 2016.

Kimi et al. (2025) Kimi, Angang Du, Bofei Gao, Bowei Xing, Changjiu Jiang, Cheng Chen, Cheng Li, Chenjun Xiao, Chenzhuang Du, Chonghua Liao, et al. Kimi k1.5: Scaling reinforcement learning with llms. arXiv preprint arXiv:2501.12599 , 2025.

Kujanpää et al. (2025) Kalle Kujanpää, Pekka Marttinen, Harri Valpola, and Alexander Ilin. Efficient knowledge injection in LLMs via self-distillation. TMLR , 2025.

Kwon et al. (2023) Woosuk Kwon, Zhuohan Li, Siyuan Zhuang, Ying Sheng, Lianmin Zheng, Cody Hao Yu, Joseph E. Gonzalez, Hao Zhang, and Ion Stoica. Efficient memory management for large language model serving with pagedattention. In PSIGOPS , 2023.

Lambert et al. (2025) Nathan Lambert, Jacob Morrison, Valentina Pyatkin, Shengyi Huang, Hamish Ivison, Faeze Brahman, Lester James V Miranda, Alisa Liu, Nouha Dziri, Shane Lyu, et al. Tulu 3: Pushing frontiers in open language model post-training. In COLM , 2025.

Le et al. (2022) Hung Le, Yue Wang, Akhilesh Deepak Gotmare, Silvio Savarese, and Steven Chu Hong Hoi. Coderl: Mastering code generation through pretrained models and deep reinforcement learning. In NeurIPS , 2022.

Lee et al. (2024) Kyungjae Lee, Dasol Hwang, Sunghyun Park, Youngsoo Jang, and Moontae Lee. Reinforcement learning from reflective feedback (rlrf): Aligning and improving llms via fine-grained self-reflection. arXiv preprint arXiv:2403.14238 , 2024.

Lee et al. (2025) Yoonho Lee, Joseph Boen, and Chelsea Finn. Feedback descent: Open-ended text optimization via pairwise comparison. arXiv preprint arXiv:2511.07919 , 2025.

Levine (2018) Sergey Levine. Reinforcement learning and control as probabilistic inference: Tutorial and review. arXiv preprint arXiv:1805.00909 , 2018.

Li et al. (2025a) Tianle Li, Wei-Lin Chiang, Evan Frick, Lisa Dunlap, Tianhao Wu, Banghua Zhu, Joseph E Gonzalez, and Ion Stoica. From crowdsourced data to high-quality benchmarks: Arena-hard and benchbuilder pipeline. In ICML , 2025a.

Li et al. (2025b) Yi-Chen Li, Tian Xu, Yang Yu, Xuqin Zhang, Xiong-Hui Chen, Zhongxiang Ling, Ningjing Chao, Lei Yuan, and Zhi-Hua Zhou. Generalist reward models: Found inside large language models. arXiv preprint arXiv:2506.23235 , 2025b.

Lightman et al. (2023) Hunter Lightman, Vineet Kosaraju, Yuri Burda, Harrison Edwards, Bowen Baker, Teddy Lee, Jan Leike, John Schulman, Ilya Sutskever, and Karl Cobbe. Let’s verify step by step. In ICLR , 2023.

Liu et al. (2025a) Grace Liu, Michael Tang, and Benjamin Eysenbach. A single goal is all you need: Skills and exploration emerge from contrastive rl without rewards, demonstrations, or subgoals. In ICLR , 2025a.

Liu et al. (2023) Hao Liu, Carmelo Sferrazza, and Pieter Abbeel. Chain of hindsight aligns language models with feedback. arXiv preprint arXiv:2302.02676 , 2023.

Liu et al. (2025b) Zichen Liu, Changyu Chen, Wenjun Li, Penghui Qi, Tianyu Pang, Chao Du, Wee Sun Lee, and Min Lin. Understanding r1-zero-like training: A critical perspective. In COLM , 2025b.

Lu & Thinking Machines Lab (2025) Kevin Lu and Thinking Machines Lab. On-policy distillation. Thinking Machines Lab: Connectionism , 2025. URL https://thinkingmachines.ai/blog/on-policy-distillation .

Luo et al. (2025) Renjie Luo, Zichen Liu, Xiangyan Liu, Chao Du, Min Lin, Wenhu Chen, Wei Lu, and Tianyu Pang. Language models can learn from verbal feedback without scalar rewards. arXiv preprint arXiv:2509.22638 , 2025.

Madaan et al. (2023) Aman Madaan, Niket Tandon, Prakhar Gupta, Skyler Hallinan, Luyu Gao, Sarah Wiegreffe, Uri Alon, Nouha Dziri, Shrimai Prabhumoye, Yiming Yang, et al. Self-refine: Iterative refinement with self-feedback. In NeurIPS , 2023.

Mitra & Ulukus (2025) Purbesh Mitra and Sennur Ulukus. Semantic soft bootstrapping: Long context reasoning in llms without reinforcement learning. arXiv preprint arXiv:2512.05105 , 2025.

Mnih et al. (2015) Volodymyr Mnih, Koray Kavukcuoglu, David Silver, Andrei A. Rusu, Joel Veness, Marc G. Bellemare, Alex Graves, Martin Riedmiller, Andreas K. Fidjeland, Georg Ostrovski, et al. Human-level control through deep reinforcement learning. Nature , 518(7540), 2015.

Muennighoff et al. (2025) Niklas Muennighoff, Zitong Yang, Weijia Shi, Xiang Lisa Li, Li Fei-Fei, Hannaneh Hajishirzi, Luke Zettlemoyer, Percy Liang, Emmanuel Candès, and Tatsunori B Hashimoto. s1: Simple test-time scaling. In EMNLP , 2025.

Ng et al. (2000) Andrew Y Ng, Stuart Russell, et al. Algorithms for inverse reinforcement learning. In ICML , 2000.

Novikov et al. (2025) Alexander Novikov, Ngân Vũ, Marvin Eisenberger, Emilien Dupont, Po-Sen Huang, Adam Zsolt Wagner, Sergey Shirobokov, Borislav Kozlovskii, Francisco JR Ruiz, Abbas Mehrabian, et al. Alphaevolve: A coding agent for scientific and algorithmic discovery. arXiv preprint arXiv:2506.13131 , 2025.

Olmo et al. (2025) Team Olmo, Allyson Ettinger, Amanda Bertsch, Bailey Kuehl, David Graham, David Heineman, Dirk Groeneveld, Faeze Brahman, Finbarr Timbers, Hamish Ivison, et al. Olmo 3. arXiv preprint arXiv:2512.13961 , 2025.

Peng et al. (2019) Xue Bin Peng, Aviral Kumar, Grace Zhang, and Sergey Levine. Advantage-weighted regression: Simple and scalable off-policy reinforcement learning. arXiv preprint arXiv:1910.00177 , 2019.

Qwen et al. (2024) Qwen, An Yang, Baosong Yang, Beichen Zhang, Binyuan Hui, Bo Zheng, Bowen Yu, Chengyuan Li, Dayiheng Liu, Fei Huang, et al. Qwen2.5 technical report. arXiv preprint arXiv:2412.15115 , 2024.

Rafailov et al. (2023) Rafael Rafailov, Archit Sharma, Eric Mitchell, Christopher D Manning, Stefano Ermon, and Chelsea Finn. Direct preference optimization: Your language model is secretly a reward model. In NeurIPS , 2023.

Romero et al. (2015) Adriana Romero, Nicolas Ballas, Samira Ebrahimi Kahou, Antoine Chassang, Carlo Gatta, and Yoshua Bengio. Fitnets: Hints for thin deep nets. In ICLR , 2015.

Ross et al. (2011) Stéphane Ross, Geoffrey Gordon, and Drew Bagnell. A reduction of imitation learning and structured prediction to no-regret online learning. In AISTATS , 2011.

Samadi et al. (2025) Mehrzad Samadi, Aleksander Ficek, Sean Narenthiran, Siddhartha Jain, Wasi Uddin Ahmad, Somshubra Majumdar, Vahid Noroozi, and Boris Ginsburg. Scaling test-time compute to achieve ioi gold medal with open-weight models. arXiv preprint arXiv:2510.14232 , 2025.

Sanh et al. (2019) Victor Sanh, Lysandre Debut, Julien Chaumond, and Thomas Wolf. Distilbert, a distilled version of bert: smaller, faster, cheaper and lighter. arXiv preprint arXiv:1910.01108 , 2019.

Schaul et al. (2015) Tom Schaul, Daniel Horgan, Karol Gregor, and David Silver. Universal value function approximators. In ICML , 2015.

Scheurer et al. (2023) Jérémy Scheurer, Jon Ander Campos, Tomasz Korbak, Jun Shern Chan, Angelica Chen, Kyunghyun Cho, and Ethan Perez. Training language models with language feedback at scale. arXiv preprint arXiv:2303.16755 , 2023.

Schulman et al. (2015) John Schulman, Sergey Levine, Pieter Abbeel, Michael Jordan, and Philipp Moritz. Trust region policy optimization. In ICML , 2015.

Schulman et al. (2016) John Schulman, Philipp Moritz, Sergey Levine, Michael Jordan, and Pieter Abbeel. High-dimensional continuous control using generalized advantage estimation. In ICLR , 2016.

Schulman et al. (2017) John Schulman, Filip Wolski, Prafulla Dhariwal, Alec Radford, and Oleg Klimov. Proximal policy optimization algorithms. arXiv preprint arXiv:1707.06347 , 2017.

Setlur et al. (2025) Amrith Setlur, Chirag Nagpal, Adam Fisch, Xinyang Geng, Jacob Eisenstein, Rishabh Agarwal, Alekh Agarwal, Jonathan Berant, and Aviral Kumar. Rewarding progress: Scaling automated process verifiers for llm reasoning. In ICLR , 2025.

Shao et al. (2024) Zhihong Shao, Peiyi Wang, Qihao Zhu, Runxin Xu, Junxiao Song, Xiao Bi, Haowei Zhang, Mingchuan Zhang, YK Li, Yang Wu, et al. Deepseekmath: Pushing the limits of mathematical reasoning in open language models. arXiv preprint arXiv:2402.03300 , 2024.

Shenfeld et al. (2026a) Idan Shenfeld, Mehul Damani, Jonas Hübotter, and Pulkit Agrawal. Self-distillation enables continual learning. arXiv preprint arXiv:2601.19897 , 2026a.

Shenfeld et al. (2026b) Idan Shenfeld, Jyothish Pari, and Pulkit Agrawal. Rl’s razor: Why online reinforcement learning forgets less. In ICLR , 2026b.

Sheng et al. (2025) Guangming Sheng, Chi Zhang, Zilingfeng Ye, Xibin Wu, Wang Zhang, Ru Zhang, Yanghua Peng, Haibin Lin, and Chuan Wu. Hybridflow: A flexible and efficient rlhf framework. In EuroSys , 2025.

Shinn et al. (2023) Noah Shinn, Federico Cassano, Ashwin Gopinath, Karthik Narasimhan, and Shunyu Yao. Reflexion: Language agents with verbal reinforcement learning. In NeurIPS , 2023.

Silver et al. (2016) David Silver, Aja Huang, Chris J. Maddison, Arthur Guez, Laurent Sifre, George van den Driessche, Julian Schrittwieser, Ioannis Antonoglou, Veda Panneershelvam, Marc Lanctot, et al. Mastering the game of go with deep neural networks and tree search. Nature , 529(7587), 2016.

Silver et al. (2017) David Silver, Thomas Hubert, Julian Schrittwieser, Ioannis Antonoglou, Matthew Lai, Arthur Guez, Marc Lanctot, Laurent Sifre, Dharshan Kumaran, Thore Graepel, et al. Mastering chess and shogi by self-play with a general reinforcement learning algorithm. arXiv preprint arXiv:1712.01815 , 2017.

Snell et al. (2022) Charlie Snell, Dan Klein, and Ruiqi Zhong. Learning by distilling context. arXiv preprint arXiv:2209.15189 , 2022.

Song et al. (2026) Yuda Song, Lili Chen, Fahim Tajwar, Remi Munos, Deepak Pathak, J Andrew Bagnell, Aarti Singh, and Andrea Zanette. Expanding the capabilities of reinforcement learning via text feedback. arXiv preprint arXiv:2602.02482 , 2026.

Stephan et al. (2024) Moritz Stephan, Alexander Khazatsky, Eric Mitchell, Annie S Chen, Sheryl Hsu, Archit Sharma, and Chelsea Finn. Rlvf: Learning from verbal feedback without overgeneralization. In ICML , 2024.

Sun et al. (2020) Yu Sun, Xiaolong Wang, Zhuang Liu, John Miller, Alexei Efros, and Moritz Hardt. Test-time training with self-supervision for generalization under distribution shifts. In ICML , 2020.

Sun et al. (2025) Yu Sun, Xinhao Li, Karan Dalal, Jiarui Xu, Arjun Vikram, Genghan Zhang, Yann Dubois, Xinlei Chen, Xiaolong Wang, Sanmi Koyejo, et al. Learning to (learn at test time): Rnns with expressive hidden states. In ICML , 2025.

Sutton & Barto (1998) Richard S Sutton and Andrew G Barto. Reinforcement learning: An introduction . MIT press, 1998.

Tandon et al. (2025) Arnuv Tandon, Karan Dalal, Xinhao Li, Daniel Koceja, Marcel Rød, Sam Buchanan, Xiaolong Wang, Jure Leskovec, Sanmi Koyejo, Tatsunori Hashimoto, et al. End-to-end test-time training for long context. arXiv preprint arXiv:2512.23675 , 2025.

Tang et al. (2023) Qiaoyu Tang, Ziliang Deng, Hongyu Lin, Xianpei Han, Qiao Liang, Boxi Cao, and Le Sun. Toolalpaca: Generalized tool learning for language models with 3000 simulated cases. arXiv preprint arXiv:2306.05301 , 2023.

Urcelay et al. (2026) Belen Martin Urcelay, Andreas Krause, and Giorgia Ramponi. From words to rewards: Leveraging natural language for reinforcement learning. In TMLR , 2026.

Vaswani et al. (2017) Ashish Vaswani, Noam Shazeer, Niki Parmar, Jakob Uszkoreit, Llion Jones, Aidan N. Gomez, Lukasz Kaiser, and Illia Polosukhin. Attention is all you need. In NeurIPS , 2017.

Wang et al. (2026) Hanyang Wang, Lu Wang, Chaoyun Zhang, Tianjun Mao, Si Qin, Qingwei Lin, Saravan Rajmohan, and Dongmei Zhang. Text2grad: Reinforcement learning from natural language feedback. In ICLR , 2026.

Wang et al. (2024a) Peiyi Wang, Lei Li, Zhihong Shao, RX Xu, Damai Dai, Yifei Li, Deli Chen, Yu Wu, and Zhifang Sui. Math-shepherd: Verify and reinforce llms step-by-step without human annotations. In ACL , 2024a.

Wang et al. (2025) Shenzhi Wang, Le Yu, Chang Gao, Chujie Zheng, Shixuan Liu, Rui Lu, Kai Dang, Xionghui Chen, Jianxin Yang, Zhenru Zhang, et al. Beyond the 80/20 rule: High-entropy minority tokens drive effective reinforcement learning for llm reasoning. In NeurIPS , 2025.

Wang et al. (2024b) Yubo Wang, Xueguang Ma, Ge Zhang, Yuansheng Ni, Abhranil Chandra, Shiguang Guo, Weiming Ren, Aaran Arulraj, Xuan He, Ziyan Jiang, et al. Mmlu-pro: A more robust and challenging multi-task language understanding benchmark. In NeurIPS , 2024b.

Wei et al. (2022) Jason Wei, Xuezhi Wang, Dale Schuurmans, Maarten Bosma, Fei Xia, Ed Chi, Quoc V Le, Denny Zhou, et al. Chain-of-thought prompting elicits reasoning in large language models. In NeurIPS , 2022.

Williams (1992) Ronald J Williams. Simple statistical gradient-following algorithms for connectionist reinforcement learning. Machine learning , 8(3), 1992.

Xie et al. (2020) Qizhe Xie, Minh-Thang Luong, Eduard Hovy, and Quoc V Le. Self-training with noisy student improves imagenet classification. In CVPR , 2020.

Xie et al. (2024) Tianbao Xie, Siheng Zhao, Chen Henry Wu, Yitao Liu, Qian Luo, Victor Zhong, Yanchao Yang, and Tao Yu. Text2reward: Reward shaping with language models for reinforcement learning. In ICLR , 2024.

Yang et al. (2025a) An Yang, Anfeng Li, Baosong Yang, Beichen Zhang, Binyuan Hui, Bo Zheng, Bowen Yu, Chang Gao, Chengen Huang, Chenxu Lv, et al. Qwen3 technical report. arXiv preprint arXiv:2505.09388 , 2025a.

Yang et al. (2025b) Wenkai Yang, Yankai Lin, Jie Zhou, and Ji-Rong Wen. Distilling rule-based knowledge into large language models. In COLING , 2025b.

Yang et al. (2024) Zhaorui Yang, Tianyu Pang, Haozhe Feng, Han Wang, Wei Chen, Minfeng Zhu, and Qian Liu. Self-distillation bridges distribution gap in language model fine-tuning. In ACL , 2024.

Yao et al. (2025) Feng Yao, Liyuan Liu, Dinghuai Zhang, Chengyu Dong, Jingbo Shang, and Jianfeng Gao. Your efficient rl framework secretly brings you off-policy rl training, 2025. URL https://fengyao.notion.site/off-policy-rl .

Yao et al. (2024) Weiran Yao, Shelby Heinecke, Juan Carlos Niebles, Zhiwei Liu, Yihao Feng, Le Xue, Rithesh Murthy, Zeyuan Chen, Jianguo Zhang, Devansh Arpit, et al. Retroformer: Retrospective large language agents with policy gradient optimization. In ICLR , 2024.

Yu et al. (2025) Qiying Yu, Zheng Zhang, Ruofei Zhu, Yufeng Yuan, Xiaochen Zuo, Yu Yue, Weinan Dai, Tiantian Fan, Gaohong Liu, Lingjun Liu, et al. Dapo: An open-source llm reinforcement learning system at scale. In NeurIPS , 2025.

Yue et al. (2025) Yang Yue, Zhiqi Chen, Rui Lu, Andrew Zhao, Zhaokai Wang, Shiji Song, and Gao Huang. Does reinforcement learning really incentivize reasoning capacity in llms beyond the base model? In NeurIPS , 2025.

Yuksekgonul et al. (2025) Mert Yuksekgonul, Federico Bianchi, Joseph Boen, Sheng Liu, Pan Lu, Zhi Huang, Carlos Guestrin, and James Zou. Optimizing generative ai by backpropagating language model feedback. Nature , 639:609–616, 2025.

Yuksekgonul et al. (2026) Mert Yuksekgonul, Daniel Koceja, Xinhao Li, Federico Bianchi, Jed McCaleb, Xiaolong Wang, Jan Kautz, Yejin Choi, James Zou, Carlos Guestrin, et al. Learning to discover at test time. arXiv preprint arXiv:2601.16175 , 2026.

Zelikman et al. (2022) Eric Zelikman, Yuhuai Wu, Jesse Mu, and Noah D Goodman. Star: Bootstrapping reasoning with reasoning. In NeurIPS , 2022.

Zhang et al. (2025) Kai Zhang, Xiangchao Chen, Bo Liu, Tianci Xue, Zeyi Liao, Zhihan Liu, Xiyao Wang, Yuting Ning, Zhaorun Chen, Xiaohan Fu, et al. Agent learning via early experience. arXiv preprint arXiv:2510.08558 , 2025.

Zhang et al. (2023) Tianjun Zhang, Fangchen Liu, Justin Wong, Pieter Abbeel, and Joseph E Gonzalez. The wisdom of hindsight makes language models better instruction followers. In ICML , 2023.

Zhao et al. (2025) Andrew Zhao, Yiran Wu, Yang Yue, Tong Wu, Quentin Xu, Matthieu Lin, Shenzhi Wang, Qingyun Wu, Zilong Zheng, and Gao Huang. Absolute zero: Reinforced self-play reasoning with zero data. In NeurIPS , 2025.

Zhao et al. (2026) Siyan Zhao, Zhihui Xie, Mengchen Liu, Jing Huang, Guan Pang, Feiyu Chen, and Aditya Grover. Self-distilled reasoner: On-policy self-distillation for large language models. arXiv preprint arXiv:2601.18734 , 2026.

Zheng et al. (2025a) Chujie Zheng, Shixuan Liu, Mingze Li, Xiong-Hui Chen, Bowen Yu, Chang Gao, Kai Dang, Yuqiong Liu, Rui Men, An Yang, et al. Group sequence policy optimization. arXiv preprint arXiv:2507.18071 , 2025a.

Zheng et al. (2025b) Tianyu Zheng, Tianshun Xing, Qingshui Gu, Taoran Liang, Xingwei Qu, Xin Zhou, Yizhi Li, Zhoufutu Wen, Chenghua Lin, Wenhao Huang, et al. First return, entropy-eliciting explore. arXiv preprint arXiv:2507.07017 , 2025b.

Zhou et al. (2023) Jeffrey Zhou, Tianjian Lu, Swaroop Mishra, Siddhartha Brahma, Sujoy Basu, Yi Luan, Denny Zhou, and Le Hou. Instruction-following evaluation for large language models. arXiv preprint arXiv:2311.07911 , 2023.

Zhou et al. (2025) Ruiyang Zhou, Shuozhe Li, Amy Zhang, and Liu Leqi. Expo: Unlocking hard reasoning with self-explanation-guided reinforcement learning. In NeurIPS , 2025.

Zhou et al. (2026) Xiangxin Zhou, Zichen Liu, Anya Sims, Haonan Wang, Tianyu Pang, Chongxuan Li, Liang Wang, Min Lin, and Chao Du. Reinforcing general reasoning without verifiers. In ICLR , 2026.

Ziebart et al. (2008) Brian D Ziebart, Andrew L Maas, J Andrew Bagnell, Anind K Dey, et al. Maximum entropy inverse reinforcement learning. In AAAI , 2008.

Zuo et al. (2025) Yuxin Zuo, Kaiyan Zhang, Shang Qu, Li Sheng, Xuekai Zhu, Biqing Qi, Youbang Sun, Ganqu Cui, Ning Ding, and Bowen Zhou. Ttrl: Test-time reinforcement learning. In NeurIPS , 2025.

## Contents

section.1table.caption.4section.2subsection.2.1subsection.2.2subsection.2.3section.3subsection.3.1subsection.3.1subsection.3.2subsection.3.3section.4section.4subsection.4.1subsection.4.2subsection.4.3subsection.4.4subsection.4.4subsection.4.5subsection.4.6subsection.4.6subsection.4.6subsection.4.6section.5subsection.5.1subsection.5.2figure.caption.20figure.caption.20section.6subsection.6.1subsection.6.2subsection.6.3subsection.6.4section.7section.7section.7appendix.Asubsection.A.1subsection.A.1equation.6subsection.A.2subsection.A.3subsection.A.4appendix.Bsubsection.B.1subsection.B.2appendix.Cappendix.Cappendix.Cappendix.Cappendix.Csubsection.C.1subsection.C.1equation.19appendix.Dsubsection.D.1subsection.D.2subsubsection.D.2.1subsubsection.D.2.2subsubsection.D.2.3subsection.D.3appendix.Esubsection.E.1subsection.E.2subsubsection.E.2.1subsection.E.3appendix.Fsubsection.F.1subsection.F.2subsection.F.3subsection.F.4

## Appendix A Implementation of SDPO

The following pseudocode in Figure 14 outlines the implementation of SDPO:

In the following, we provide further details on: • The gradient estimator used in our implementation ( Section A.1 )

• Teacher regularization ( Section A.2 )

• Approximating logit-distillation with the top- K K logits for saving GPU memory ( Section A.3 )

• Generalizing PPO-style policy gradient algorithms to logit-level advantages ( Section A.4 )

To disambiguate the notation of the self-teacher, we use q θ ( ⋅ ∣ x , f ) := π θ ( ⋅ ∣ reprompt ( x , f ) ) q_{\theta}(\cdot\mid x,f):=\pi_{\theta}(\cdot\mid\mathrm{reprompt}(x,f)) in the following. Here, reprompt denotes the reprompt template of the self-teacher.

### A.1 Gradient Estimators

In this seciton, we discuss two possible gradient estimators for the KL divergence between the current policy π θ ​ ( y ∣ x ) \pi_{\theta}(y\mid x) and the teacher policy q θ ​ ( y ∣ x , f ) q_{\theta}(y\mid x,f) .

##### Per-token estimator.

Deriving the gradient of the SDPO loss as defined in Equation 1 : ℒ token ( θ ) := 𝔼 y ∼ stopgrad ( π θ ( ⋅ ∣ x ) ) [ ∑ t = 1 T KL ( π θ ( ⋅ ∣ x , y < t ) ∥ stopgrad ( π θ ( ⋅ ∣ x , f , y < t ) ) ) ] \mathcal{L}_{\mathrm{token}}(\theta):=\mathbb{E}_{y\sim\mathrm{stopgrad}(\pi_{\theta}(\cdot\mid x))}\left[\sum_{t=1}^{T}\mathrm{KL}(\pi_{\theta}(\cdot\mid x,y_{<t})\|\mathrm{stopgrad}(\pi_{\theta}(\cdot\mid x,f,y_{<t})))\right] (5) leads to the following estimator (see a detailed proof in Section B.1 ), which corresponds to the sum of gradients of the KL divergence at each token: ∇ ℒ token ( θ ) = 𝔼 y ∼ π θ ( ⋅ ∣ x ) [ ∑ t = 1 T 𝔼 y ^ t ∼ π θ ( ⋅ ∣ x , y < t ) [ ∇ θ log π θ ( y ^ t ∣ x , y < t ) ⋅ log π θ ​ ( y ^ t ∣ x , y < t ) π θ ​ ( y ^ t ∣ x , f , y < t ) ] ] . \boldsymbol{\nabla}\mathcal{L}_{\text{token}}(\theta)=\mathbb{E}_{y\sim\pi_{\theta}(\cdot\mid x)}\left[\sum_{t=1}^{T}\mathbb{E}_{\hat{y}_{t}\sim\pi_{\theta}(\cdot\mid x,y_{<t})}\!\!\left[\boldsymbol{\nabla}_{\!\!\theta}\,\log\pi_{\theta}(\hat{y}_{t}\mid x,y_{<t})\cdot\log\frac{\pi_{\theta}(\hat{y}_{t}\mid x,y_{<t})}{\pi_{\theta}(\hat{y}_{t}\mid x,f,y_{<t})}\right]\right]. (6) This corresponds to the estimator presented in Proposition 2.1 . This gradient estimator effectively assumes that the sampling distribution generating y y is fixed.

##### Sequence-level estimator.

An alternative self-distillation objective minimizes the sequence-level KL divergence between student and self-teacher, i.e., ℒ seq ( θ ) := KL ( π θ ∥ q θ ) = 𝔼 y ∼ π θ ( ⋅ ∣ x ) [ log π θ ​ ( y ∣ x ) q θ ​ ( y ∣ x , f ) ] = ∑ t = 1 T 𝔼 s t ∼ Π θ [ KL ( π θ ( ⋅ ∣ s t ) ∥ q θ ( ⋅ ∣ s t , f ) ) ] , \displaystyle\begin{split}\mathcal{L}_{\mathrm{seq}}(\theta):=\mathrm{KL}\left(\pi_{\theta}\|q_{\theta}\right)&=\mathbb{E}_{y\sim\pi_{\theta}(\cdot\mid x)}\left[\log\frac{\pi_{\theta}(y\mid x)}{q_{\theta}(y\mid x,f)}\right]\\ &=\sum_{t=1}^{T}\mathbb{E}_{s_{t}\sim\Pi_{\theta}}\left[\mathrm{KL}\left(\pi_{\theta}(\cdot\mid s_{t})\|q_{\theta}(\cdot\mid s_{t},f)\right)\right],\end{split} (7) where s t = ( x , y < t ) s_{t}=(x,y_{<t}) is the prefix (“state”) at step t t and Π θ \Pi_{\theta} denotes the prefix distribution under policy π θ \pi_{\theta} . Estimating the gradient of this objective additionally takes into account how the choice of y t y_{t} influences future states y > t y_{>t} (due to the additional dependence on Π θ \Pi_{\theta} ).

Amini et al. (2025) show that the corresponding gradient estimator is given by ∇ ℒ seq ( θ ) = ∇ ℒ token ( θ ) + 𝔼 y ∼ π θ ( ⋅ ∣ x ) [ ∑ t = 1 T KL ( π θ ( ⋅ ∣ s t ) ∥ q θ ( ⋅ ∣ s t , f ) ) ∇ θ log Π θ ( s t ) ] . \boldsymbol{\nabla}\mathcal{L}_{\text{seq}}(\theta)=\boldsymbol{\nabla}\mathcal{L}_{\text{token}}(\theta)+\mathbb{E}_{y\sim\pi_{\theta}(\cdot\mid x)}\left[\sum_{t=1}^{T}\mathrm{KL}\left(\pi_{\theta}(\cdot\mid s_{t})\|q_{\theta}(\cdot\mid s_{t},f)\right)\boldsymbol{\nabla}_{\!\!\theta}\,\log\Pi_{\theta}(s_{t})\right]. (8)

The additional term of the sequence-level gradient captures how prefixes influence the self-distillation divergence of future tokens. We also experimented with this sequence-level gradient estimator but did not find measurable gains relative to its additional complexity.

### A.2 Regularized teacher

In contrast to standard distillation, the teacher in SDPO changes throughout training. This bootstrapping enables the teacher to improve, but it may also lead to training instability. To stabilize training, we seek to prevent the teacher q q from quickly diverging from the initial teacher q θ ref \smash{q_{\theta_{{\mathrm{ref}}}}} . We can achieve this by placing an explicit trust-region constraint on q q ( Schulman et al., 2015 ; Peng et al., 2019 ) , that is: ∑ t KL ( q ( y t ∣ x , f , y < t ) ∥ q θ ref ( y t ∣ x , f , y < t ) ) ≤ ϵ , ϵ > 0 . \sum_{t}\mathrm{KL}\left(q(y_{t}\mid x,f,y_{<t})\|q_{\theta_{{\mathrm{ref}}}}(y_{t}\mid x,f,y_{<t})\right)\leq\epsilon,\quad\epsilon>0. (9) This trust-region can be implemented in two ways: 1. Explicit trust-region: We can define the teacher as the policy closest to q θ q_{\theta} while satisfying the trust-region constraint. This teacher can be expressed as q ⁡ ( y t ∣ x , f , y < t ) ∝ exp ⁡ ( ( 1 − α ) ​ log ⁡ q θ ref ​ ( y t ∣ x , f , y < t ) + α ​ log ⁡ q θ ​ ( y t ∣ x , f , y < t ) ) , q(y_{t}\mid x,f,y_{<t})\propto\exp\!\big((1-\alpha)\log q_{\theta_{{\mathrm{ref}}}}(y_{t}\mid x,f,y_{<t})+\alpha\log q_{\theta}(y_{t}\mid x,f,y_{<t})\big), (10) with α ∈ ( 0 , 1 ) \alpha\in(0,1) the inverse Lagrange multiplier for the trust-region constraint. We include a full derivation in Section B.2 . We can plug this explicitly constrained teacher directly into the SDPO objective.

2. Exponential moving average (EMA): Alternatively, we can stabilize the teacher’s parameters directly; parameterizing q θ ′ q_{\theta^{\prime}} by θ ′ \theta^{\prime} and updating as θ ′ ← ( 1 − α ) ​ θ ′ + α ​ θ \theta^{\prime}\leftarrow(1-\alpha)\theta^{\prime}+\alpha\theta with α ∈ ( 0 , 1 ) \alpha\in(0,1) .

Note that each implementation has a different practical advantage: The EMA teacher requires additional GPU memory for θ ′ \theta^{\prime} yet does not introduce any runtime overhead. In contrast, the trust-region teacher requires an additional log-prob computation with q θ ref \smash{q_{\theta_{{\mathrm{ref}}}}} yet does not require additional GPU memory if θ ref {\theta_{{\mathrm{ref}}}} is used for explicit KL regularization.

### A.3 Approximate Logit Distillation

To save GPU memory, we perform distillation only on the top- K K tokens predicted by the student:

ℒ SDPO ​ ( θ ) \displaystyle\mathcal{L}_{\mathrm{SDPO}}(\theta) = ∑ t = 1 T KL ( π θ ( ⋅ ∣ x , y < t ) ∥ stopgrad ( q θ ( ⋅ ∣ x , f , y < t ) ) ) \displaystyle=\sum_{t=1}^{T}\mathrm{KL}(\pi_{\theta}(\cdot\mid x,y_{<t})\|\mathrm{stopgrad}(q_{\theta}(\cdot\mid x,f,y_{<t}))) ≈ ∑ t = 1 T ∑ y ^ t ∈ top K ​ ( π θ ) π θ ​ ( y ^ t ∣ x , y < t ) ⋅ log ⁡ π θ ​ ( y ^ t ∣ x , y < t ) stopgrad ⁡ ( q θ ​ ( y ^ t ∣ x , f , y < t ) ) + ( 1 − ∑ y ^ t ∈ top K ​ ( π θ ) π θ ​ ( y ^ t ∣ x , y < t ) ) ⋅ log ⁡ 1 − ∑ y ^ t ∈ top K ​ ( π θ ) π θ ​ ( y ^ t ∣ x , y < t ) stopgrad ⁡ ( 1 − ∑ y ^ t ∈ top K ​ ( π θ ) q θ ​ ( y ^ t ∣ x , f , y < t ) ) ⏟ tail \displaystyle\approx\begin{multlined}\sum_{t=1}^{T}\sum_{\hat{y}_{t}\in\mathrm{top}_{K}(\pi_{\theta})}\pi_{\theta}(\hat{y}_{t}\mid x,y_{<t})\cdot\log\frac{\pi_{\theta}(\hat{y}_{t}\mid x,y_{<t})}{\mathrm{stopgrad}(q_{\theta}(\hat{y}_{t}\mid x,f,y_{<t}))}\\ +\underbrace{\Big(1-\textstyle\sum_{\hat{y}_{t}\in\mathrm{top}_{K}(\pi_{\theta})}\pi_{\theta}(\hat{y}_{t}\mid x,y_{<t})\Big)\cdot\log\frac{1-\textstyle\sum_{\hat{y}_{t}\in\mathrm{top}_{K}(\pi_{\theta})}\pi_{\theta}(\hat{y}_{t}\mid x,y_{<t})}{\mathrm{stopgrad}\Big(1-\textstyle\sum_{\hat{y}_{t}\in\mathrm{top}_{K}(\pi_{\theta})}q_{\theta}(\hat{y}_{t}\mid x,f,y_{<t})\Big)}}_{\text{tail}}\end{multlined}

Here, the top- K K is with respect to student. Without top- K K distillation, we would have to keep two copies of logits in memory: one for teacher and student each. Top- K K distillation avoids virtually any memory overhead without impacting performance significantly, since most tokens of the vocabulary are not informative at a given time.

### A.4 Off-Policy Training: Generalization to Logit-Level Losses

PPO-style clipping ( Schulman et al., 2017 ) with truncated importance sampling ( Yao et al., 2025 ) , clip-higher ( Yu et al., 2025 ) , fixed length normalization ( Liu et al., 2025b ) : ℒ token ( θ ) := − 1 ∑ i = 1 G | y i | ∑ i = 1 G ∑ t = 1 | y i | min ( w i , t TIS , ρ ) min ( w i , t A i , t , clip ( w i , t , 1 − ε low , 1 + ε high ) A i , t ) , \mathcal{L}_{\mathrm{token}}(\theta):=-{\color[rgb]{1,0.5,0}\frac{1}{\sum_{i=1}^{G}|y_{i}|}}\sum_{i=1}^{G}\sum_{t=1}^{|y_{i}|}{\color[rgb]{0.9492,0.3281,0.3555}\min\left(w^{\mathrm{TIS}}_{i,t},\rho\right)}\min\left(w_{i,t}A_{i,t},\text{clip}(w_{i,t},1-\varepsilon_{\text{low}},1+{\color[rgb]{0.3477,0.7344,0.168}\varepsilon_{\text{high}}})A_{i,t}\right), (13) with w i , t := π θ ​ ( y i , t ∣ x , y i , < t ) π θ old ​ ( y i , t ∣ x , y i , < t ) w_{i,t}:=\frac{\pi_{\theta}(y_{i,t}\mid x,y_{i,<t})}{\pi_{\theta_{{\mathrm{old}}}}(y_{i,t}\mid x,y_{i,<t})} , w i , t TIS := π θ old ​ ( y i , t ∣ x , y i , < t ) π θ old rollout ​ ( y i , t ∣ x , y i , < t ) w^{\mathrm{TIS}}_{i,t}:=\frac{\pi_{\theta_{{\mathrm{old}}}}(y_{i,t}\mid x,y_{i,<t})}{\pi_{\theta_{{\mathrm{old}}}}^{\mathrm{rollout}}(y_{i,t}\mid x,y_{i,<t})} , and A i , t A_{i,t} denotes the per-token advantage.

We extend this to a logit-level loss: ℒ logit ( θ ) := − 1 ∑ i = 1 G | y i | ∑ i = 1 G ∑ t = 1 | y i | ∑ y ^ i , t min ( π θ old ( y ^ i , t ∣ x , y i , < t ) , ρ π θ old rollout ( y ^ i , t ∣ x , y i , < t ) ) min ⁡ ( w i , t ​ ( y ^ i , t ) ​ A i , t ​ ( y ^ i , t ) , clip ​ ( w i , t ​ ( y ^ i , t ) , 1 − ε low , 1 + ε high ) ​ A i , t ​ ( y ^ i , t ) ) , \begin{multlined}\mathcal{L}_{\mathrm{logit}}(\theta):=-{\color[rgb]{1,0.5,0}\frac{1}{\sum_{i=1}^{G}|y_{i}|}}\sum_{i=1}^{G}\sum_{t=1}^{|y_{i}|}{\color[rgb]{0.168,0.3125,0.668}\sum_{\hat{y}_{i,t}}}\ {\color[rgb]{0.9492,0.3281,0.3555}\min\left(\pi_{\theta_{{\mathrm{old}}}}(\hat{y}_{i,t}\mid x,y_{i,<t}),\rho\pi_{\theta_{{\mathrm{old}}}}^{\mathrm{rollout}}(\hat{y}_{i,t}\mid x,y_{i,<t})\right)}\\ \min\left(w_{i,t}(\hat{y}_{i,t})A_{i,t}(\hat{y}_{i,t}),\text{clip}(w_{i,t}(\hat{y}_{i,t}),1-\varepsilon_{\text{low}},1+{\color[rgb]{0.3477,0.7344,0.168}\varepsilon_{\text{high}}})A_{i,t}(\hat{y}_{i,t})\right),\end{multlined} (14) where y ^ i , t \hat{y}_{i,t} sums over all possible tokens at position t t for rollout i i (or the K K most likely under π θ old \pi_{\theta_{{\mathrm{old}}}} , cf. Section A.3 ). The TIS changes since we explicitly weight each logit by its probability under π θ old \pi_{\theta_{{\mathrm{old}}}} rather than relying on a Monte Carlo estimate of the expectation over next-token predictions. Here, A i , t ​ ( y ^ i , t ) A_{i,t}(\hat{y}_{i,t}) is a per-logit advantage.

In our experiments for SDPO, we apply the TIS term on a token-level rather than logit-level.

## Appendix B Theoretical Analysis

This section is organized as follows: • Section B.1 derives the SDPO gradient from Proposition 2.1 .

• Section B.2 derives the trust-region regularized teacher discussed in Section A.2 .

To disambiguate the notation of the self-teacher, we use q θ ( ⋅ ∣ x , f ) := π θ ( ⋅ ∣ reprompt ( x , f ) ) q_{\theta}(\cdot\mid x,f):=\pi_{\theta}(\cdot\mid\mathrm{reprompt}(x,f)) in the following. Here, reprompt denotes the reprompt template of the self-teacher.

### B.1 Proof of Proposition 2.1 .

###### Proof.

In the following, we derive the gradient of ℒ SDPO \mathcal{L}_{\mathrm{SDPO}} . ∇ θ ℒ SDPO ​ ( θ ) \displaystyle\boldsymbol{\nabla}_{\!\!\theta}\,\mathcal{L}_{\mathrm{SDPO}}(\theta) = ∇ θ ∑ t = 1 T KL ( π θ ( ⋅ ∣ x , y < t ) ∥ stopgrad ( q θ ( ⋅ ∣ x , f , y < t ) ) ) \displaystyle=\boldsymbol{\nabla}_{\!\!\theta}\,\sum_{t=1}^{T}\mathrm{KL}(\pi_{\theta}(\cdot\mid x,y_{<t})\|\mathrm{stopgrad}(q_{\theta}(\cdot\mid x,f,y_{<t}))) = ∇ θ ∑ t = 1 T ∑ y ^ t π θ ( y ^ t ∣ x , y < t ) log ( π θ ​ ( y ^ t ∣ x , y < t ) stopgrad ⁡ ( q θ ​ ( y ^ t ∣ x , f , y < t ) ) ) \displaystyle=\boldsymbol{\nabla}_{\!\!\theta}\,\sum_{t=1}^{T}\sum_{\hat{y}_{t}}\pi_{\theta}(\hat{y}_{t}\mid x,y_{<t})\log\left(\frac{\pi_{\theta}(\hat{y}_{t}\mid x,y_{<t})}{\mathrm{stopgrad}(q_{\theta}(\hat{y}_{t}\mid x,f,y_{<t}))}\right) Let A t , k := log ⁡ ( stopgrad ⁡ ( q θ ​ ( y ^ t ∣ x , f , y < t ) ) π θ ​ ( y ^ t ∣ x , y < t ) ) A_{t,k}:=\log\left(\frac{\mathrm{stopgrad}(q_{\theta}(\hat{y}_{t}\mid x,f,y_{<t}))}{\pi_{\theta}(\hat{y}_{t}\mid x,y_{<t})}\right) . Then, = − ∇ θ ∑ t = 1 T ∑ y ^ t π θ ( y ^ t ∣ x , y < t ) A t , k \displaystyle=-\boldsymbol{\nabla}_{\!\!\theta}\,\sum_{t=1}^{T}\sum_{\hat{y}_{t}}\pi_{\theta}(\hat{y}_{t}\mid x,y_{<t})A_{t,k} = − ∑ t = 1 T ∑ y ^ t π θ ( y ^ t ∣ x , y < t ) ∇ θ A t , k + A t , k ∇ θ π θ ( y ^ t ∣ x , y < t ) . \displaystyle=-\sum_{t=1}^{T}\sum_{\hat{y}_{t}}\pi_{\theta}(\hat{y}_{t}\mid x,y_{<t})\boldsymbol{\nabla}_{\!\!\theta}\,A_{t,k}+A_{t,k}\boldsymbol{\nabla}_{\!\!\theta}\,\pi_{\theta}(\hat{y}_{t}\mid x,y_{<t}). We have that ∇ θ A t , k = − ∇ θ ​ log ​ π θ ​ ( y ^ t ∣ x , y < t ) \boldsymbol{\nabla}_{\!\!\theta}\,A_{t,k}=-\boldsymbol{\nabla}_{\!\!\theta}\,\log\pi_{\theta}(\hat{y}_{t}\mid x,y_{<t}) is the negative score function. Using the score trick, π θ ​ ( y ^ t ∣ x , y < t ) ​ ∇ θ ​ log ⁡ π θ ​ ( y ^ t ∣ x , y < t ) = ∇ θ π θ ​ ( y ^ t ∣ x , y < t ) \pi_{\theta}(\hat{y}_{t}\mid x,y_{<t})\boldsymbol{\nabla}_{\!\!\theta}\,\log\pi_{\theta}(\hat{y}_{t}\mid x,y_{<t})=\boldsymbol{\nabla}_{\!\!\theta}\,\pi_{\theta}(\hat{y}_{t}\mid x,y_{<t}) . Hence, the first term simplifies to − ∑ t = 1 T ∑ y ^ t π θ ( y ^ t ∣ x , y < t ) ∇ θ A t , k \displaystyle-\sum_{t=1}^{T}\sum_{\hat{y}_{t}}\pi_{\theta}(\hat{y}_{t}\mid x,y_{<t})\boldsymbol{\nabla}_{\!\!\theta}\,A_{t,k} = ∑ t = 1 T ∑ y ^ t ∇ θ π θ ​ ( y ^ t ∣ x , y < t ) = ∑ t = 1 T ∇ θ ∑ y ^ t π θ ​ ( y ^ t ∣ x , y < t ) ⏟ = 1 = 0 . \displaystyle=\sum_{t=1}^{T}\sum_{\hat{y}_{t}}\boldsymbol{\nabla}_{\!\!\theta}\,\pi_{\theta}(\hat{y}_{t}\mid x,y_{<t})=\sum_{t=1}^{T}\boldsymbol{\nabla}_{\!\!\theta}\,\underbrace{\sum_{\hat{y}_{t}}\pi_{\theta}(\hat{y}_{t}\mid x,y_{<t})}_{=1}=0. Thus, the gradient of ℒ SDPO \mathcal{L}_{\mathrm{SDPO}} is ∇ θ ℒ SDPO \displaystyle\boldsymbol{\nabla}_{\!\!\theta}\,\mathcal{L}_{\mathrm{SDPO}} = − ∑ t = 1 T ∑ y ^ t A t , k ∇ θ π θ ( y ^ t ∣ x , y < t ) \displaystyle=-\sum_{t=1}^{T}\sum_{\hat{y}_{t}}A_{t,k}\boldsymbol{\nabla}_{\!\!\theta}\,\pi_{\theta}(\hat{y}_{t}\mid x,y_{<t}) = − ∑ t = 1 T ∑ y ^ t π θ ( y ^ t ∣ x , y < t ) ( A t , k ∇ θ log π θ ( y ^ t ∣ x , y < t ) ) \displaystyle=-\sum_{t=1}^{T}\sum_{\hat{y}_{t}}\pi_{\theta}(\hat{y}_{t}\mid x,y_{<t})\Big(A_{t,k}\boldsymbol{\nabla}_{\!\!\theta}\,\log\pi_{\theta}(\hat{y}_{t}\mid x,y_{<t})\Big) = − ∑ t = 1 T 𝔼 y ^ t ∼ π θ ( ⋅ ∣ x , y < t ) [ A t , k ∇ θ log π θ ( y ^ t ∣ x , y < t ) ] . \displaystyle=-\sum_{t=1}^{T}\mathbb{E}_{\hat{y}_{t}\sim\pi_{\theta}(\cdot\mid x,y_{<t})}\left[A_{t,k}\boldsymbol{\nabla}_{\!\!\theta}\,\log\pi_{\theta}(\hat{y}_{t}\mid x,y_{<t})\right]. ∎

Notably, the above implies that the gradient of ℒ SDPO \mathcal{L}_{\mathrm{SDPO}} is equivalent to the gradient of the loss if A t , k = stopgrad ⁡ ( log ⁡ q θ ​ ( y t ∣ x , f , y < t ) π θ ​ ( y t ∣ x , y < t ) ) A_{t,k}=\mathrm{stopgrad}\left(\log\frac{q_{\theta}(y_{t}\mid x,f,y_{<t})}{\pi_{\theta}(y_{t}\mid x,y_{<t})}\right) .

### B.2 Trust-region Teacher

To stabilize training, we seek to prevent the teacher q q from diverging from the initial teacher q θ ref q_{\theta_{{\mathrm{ref}}}} . We can achieve this by placing an explicit trust-region constraint on the teacher q q ( Schulman et al., 2015 ; Peng et al., 2019 ) , that is: ∑ t KL ( q ( y t ∣ x , f , y < t ) ∥ q θ ref ( y t ∣ x , f , y < t ) ) ≤ ϵ , ϵ > 0 . \sum_{t}\mathrm{KL}\left(q(y_{t}\mid x,f,y_{<t})\|q_{\theta_{{\mathrm{ref}}}}(y_{t}\mid x,f,y_{<t})\right)\leq\epsilon,\quad\epsilon>0. (15)

In the following, we derive a teacher q q which satisfies the trust-region constraint while staying close to the target q θ q_{\theta} . The following optimization problem characterizes such a q q ( Peng et al., 2019 ) : arg ​ max q ∈ Δ ∑ t ∑ y t q ⁡ ( y t ∣ x , f , y < t ) ​ log ⁡ q θ ​ ( y t ∣ x , f , y < t ) q θ ref ​ ( y t ∣ x , f , y < t ) s.t. ∑ t KL ( q ( y t ∣ x , f , y < t ) ∥ q θ ref ( y t ∣ x , f , y < t ) ) ≤ ϵ , \displaystyle\begin{split}\argmax_{q\in\Delta}\ &\sum_{t}\sum_{y_{t}}q(y_{t}\mid x,f,y_{<t})\log\frac{q_{\theta}(y_{t}\mid x,f,y_{<t})}{q_{\theta_{{\mathrm{ref}}}}(y_{t}\mid x,f,y_{<t})}\\ \text{s.t.}\ &\sum_{t}\mathrm{KL}\left(q(y_{t}\mid x,f,y_{<t})\|q_{\theta_{{\mathrm{ref}}}}(y_{t}\mid x,f,y_{<t})\right)\leq\epsilon,\end{split} (16) where Δ \Delta denotes the probability simplex. Intuitively, the solution is the q q satisfying the trust-region constraint, which is closest to q θ q_{\theta} (i.e., has minimal cross-entropy to q θ q_{\theta} ) while being farthest from q θ ref q_{\theta_{{\mathrm{ref}}}} (i.e., has maximal cross-entropy to q θ ref q_{\theta_{{\mathrm{ref}}}} ).

###### Proposition B.1 .

The solution to Equation 16 can be expressed in closed form as q ∗ ​ ( y t ∣ x , f , y < t ) ∝ exp ⁡ ( ( 1 − α ) ​ log ⁡ q θ ref ​ ( y t ∣ x , f , y < t ) + α ​ log ⁡ q θ ​ ( y t ∣ x , f , y < t ) ) . \displaystyle q^{*}(y_{t}\mid x,f,y_{<t})\propto\exp\!\big((1-\alpha)\log q_{\theta_{{\mathrm{ref}}}}(y_{t}\mid x,f,y_{<t})+\alpha\log q_{\theta}(y_{t}\mid x,f,y_{<t})\big). (17)

###### Proof.

To simplify notation, we omit the conditioning in the following. The Lagrangian (with λ ≥ 0 \lambda\geq 0 for the KL constraint and ν \nu for normalization) is ℒ ⁡ ( q , λ , ν ) = ∑ t ∑ y t q ⁡ ( y t ) ​ log ​ q θ ​ ( y t ) q θ ref ​ ( y t ) − λ ⁡ ( ∑ y t q ⁡ ( y t ) ​ log ​ q ⁡ ( y t ) q θ ref ​ ( y t ) − ϵ ) + ν ⁡ ( ∑ y t q ⁡ ( y t ) − 1 ) . \displaystyle\mathcal{L}(q,\lambda,\nu)=\sum_{t}\sum_{y_{t}}q({y_{t}})\log\frac{q_{\theta}({y_{t}})}{q_{\theta_{{\mathrm{ref}}}}({y_{t}})}-\lambda\Big(\sum_{y_{t}}q({y_{t}})\log\frac{q({y_{t}})}{q_{\theta_{{\mathrm{ref}}}}({y_{t}})}-\epsilon\Big)+\nu\Big(\sum_{y_{t}}q({y_{t}})-1\Big). Stationarity gives, for all y t y_{t} , 0 = ∂ ℒ ∂ q ⁡ ( y t ) = log ⁡ q θ ​ ( y t ) q θ ref ​ ( y t ) − λ ⁡ ( log ⁡ q ⁡ ( y t ) q θ ref ​ ( y t ) + 1 ) + ν . \displaystyle 0=\frac{\partial\mathcal{L}}{\partial q(y_{t})}=\log\frac{q_{\theta}(y_{t})}{q_{\theta_{{\mathrm{ref}}}}(y_{t})}-\lambda\Big(\log\frac{q(y_{t})}{q_{\theta_{{\mathrm{ref}}}}(y_{t})}+1\Big)+\nu. Let α := 1 / λ \alpha:=1/\lambda . Then, the solution to Equation 16 can be characterized in closed form as q ∗ ​ ( y t ) \displaystyle q^{*}(y_{t}) ∝ q θ ref ​ ( y t ) ​ exp ⁡ ( α ​ log ⁡ q θ ​ ( y t ) q θ ref ​ ( y t ) ) \displaystyle\propto q_{\theta_{{\mathrm{ref}}}}(y_{t})\exp\!\Big(\alpha\log\tfrac{q_{\theta}(y_{t})}{q_{\theta_{{\mathrm{ref}}}}(y_{t})}\Big) ∝ exp ⁡ ( ( 1 − α ) ​ log ⁡ q θ ref ​ ( y t ) + α ​ log ⁡ q θ ​ ( y t ) ) . \displaystyle\propto\exp\!\big((1-\alpha)\log q_{\theta_{{\mathrm{ref}}}}(y_{t})+\alpha\log q_{\theta}(y_{t})\big). ∎

Chen et al. (2025c) perform a similar derivation, but use reference π θ ref \pi_{{\theta_{{\mathrm{ref}}}}} , which we observe to underperform compared to the reference q θ ref q_{\theta_{{\mathrm{ref}}}} .

## Appendix C Additional Related Work

##### Value networks and Monte Carlo advantage estimation.

Several prior approaches aim to improve credit assignment but face the same information bottleneck as GRPO. Classical RL frequently trains value networks which provide token-level advantages, but themselves are learned from scalar rewards ( Schulman et al., 2016 ; Schulman et al., 2017 ) . Furthermore, value networks incur significant computational and memory overhead and are therefore typically not used to train LLMs. Other recent work estimates token-level advantages by performing additional generations starting from various positions in the original attempt ( Kazemnejad et al., 2025 ; Zheng et al., 2025b ) . While this can learn with fewer gradient steps than GRPO it still uses only scalar rewards as signal and requires costly additional generations.

##### Dense credit assignment with a reward model.

Several recent works study dense (per-token) reward assignment given access to an external reward model, typically by exploiting the reward model’s internal structure ( Chan et al., 2024 ; Cao et al., 2025b ) . Relatedly, Li et al. (2025b) argue that a token-level reward signal is implicit in an LLM’s logits by linking next-token prediction to offline inverse reinforcement learning, effectively yielding a training-free reward model for RL fine-tuning.

##### Partial observability.

From the perspective of classical RL, many verifiable domains for LLMs are naturally partially observable : executing a proposed solution induces a latent environment state (e.g., failing tests or states of an agentic system) that is revealed only through rich feedback. This aligns with the formalism of partially observable Markov decision processes (POMDPs), where agents must act under incomplete observations of state ( Kaelbling et al., 1998 ; Sutton & Barto, 1998 ) . By contrast, RLVR and RLHF pipelines typically discard this observation channel and learn only from terminal scalar rewards or pairwise preferences.

##### Relation to test-time training.

Our setting from Section 5 can be seen as a special case of test-time training where the model itself is updated at test-time using self-distillation. Updating the model at test-time is known as test-time training ( Sun et al., 2020 ; Sun et al., 2025 ; Hardt & Sun, 2024 ; Hübotter et al., 2025a ; Hübotter et al., 2025b ; Akyürek et al., 2025 ; Behrouz et al., 2025 ; Tandon et al., 2025 ; Hübotter et al., 2026 ) . Unlike prior work, self-distillation uses the in-context learning ability of the current model to attribute credit after receiving feedback. This can be seen as simulating long-context reasoning with periodic compression of context into the model weights.

### C.1 SDPO as Maximum Entropy RL

The SDPO objective resembles the objective in maximum entropy RL ( Levine, 2018 ; Haarnoja et al., 2018 , e.g.,) with a particular choice of reward function.

##### Maximum Entropy RL

Consider optimizing arg ​ max θ 𝔼 y ∼ π θ ( ⋅ ∣ x ) [ ∑ t r ( y t ∣ x , y < t ) ] + λ H [ π θ ( ⋅ ∣ x ) ] , λ > 0 \argmax_{\theta}\ \mathbb{E}_{y\sim\pi_{\theta}(\cdot\mid x)}{}\left[\sum_{t}r(y_{t}\mid x,y_{<t})\right]+\lambda\mathrm{H}\left[\pi_{\theta}(\cdot\mid x)\right],\quad\lambda>0 (18) where π θ ​ ( y ∣ x ) = ∏ t = 1 T π θ ​ ( y t ∣ x , y < t ) \smash{\pi_{\theta}(y\mid x)=\prod_{t=1}^{T}\pi_{\theta}(y_{t}\mid x,y_{<t})} and H [ π θ ( ⋅ ∣ x ) ] = 𝔼 y ∼ π θ ( ⋅ ∣ x ) [ − log π θ ( y ∣ x ) ] \smash{\mathrm{H}\left[\pi_{\theta}(\cdot\mid x)\right]=\mathbb{E}_{y\sim\pi_{\theta}(\cdot\mid x)}{}\left[-\log\pi_{\theta}(y\mid x)\right]} is the entropy of the policy. Here, r ⁡ ( y t ∣ x , y < t ) r(y_{t}\mid x,y_{<t}) is an arbitrary reward function, possibly “dense” (i.e., per-token). Equation 18 is known as maximum entropy RL. It is known that this objective is equivalent to solving a variational inference problem which discuss next.

To this end, we define a Bernoulli random variable 𝒞 \mathcal{C} which is 1 1 if the attempt y y is correct and 0 0 otherwise. We then define its distribution as p ⁡ ( 𝒞 = 1 ∣ x , y ) ∝ exp ⁡ ( 1 λ ​ ∑ t r ⁡ ( y t ∣ x , y < t ) ) \smash{p(\mathcal{C}=1\mid x,y)\propto\exp(\tfrac{1}{\lambda}\sum_{t}r(y_{t}\mid x,y_{<t}))} . Further assuming w.l.o.g. that the “prior” over responses is uniform, we can express the posterior conditioned on the event of correctness as π ⋆ ​ ( y ∣ x ) := p ⁡ ( y ∣ x , 𝒞 = 1 ) ∝ p ⁡ ( 𝒞 = 1 ∣ x , y ) ∝ exp ⁡ ( 1 λ ​ ∑ t r ⁡ ( y t ∣ x , y < t ) ) . \pi^{\star}(y\mid x):=p(y\mid x,\mathcal{C}=1)\propto p(\mathcal{C}=1\mid x,y)\propto\exp\!\left(\frac{1}{\lambda}\sum_{t}r(y_{t}\mid x,y_{<t})\right). (19) Then, Equation 18 is equivalent to minimizing the KL divergence with respect to π ⋆ \pi^{\star} : arg ​ min θ ∑ t KL ( π θ ( y t ∣ x , y < t ) ∥ π ⋆ ( y t ∣ x , y < t ) ) . \argmin_{\theta}\ \sum_{t}\mathrm{KL}\left(\pi_{\theta}(y_{t}\mid x,y_{<t})\|\pi^{\star}(y_{t}\mid x,y_{<t})\right). (20)

##### SDPO optimizes an implicit reward defined by the teacher

Note that Equation 20 is equivalent to the SDPO objective ( Equation 1 ) with implicit reward r ⁡ ( y t ∣ x , y < t ) = log ⁡ q ⁡ ( y t ∣ x , f , y < t ) r(y_{t}\mid x,y_{<t})=\log q(y_{t}\mid x,f,y_{<t}) and λ = 1 \lambda=1 . In this sense, SDPO can be seen as a maximum entropy RL algorithm with dense rewards constructed implicitly through the retrospective model.

This also points to a connection of SDPO to inverse RL ( Ng et al., 2000 ; Ziebart et al., 2008 ; Rafailov et al., 2023 ) , where the goal is to recover an unknown reward function. In SDPO, the student learns an implicit reward function defined by the retrospective model.

## Appendix D Additional Results & Ablations

This section is organized as follows: • Section D.1 contains results and ablations for Section 3 .

• Section D.2 contains results and ablations for Section 4 .

• Section D.3 contains results and ablations for Section 5 .

### D.1 Learning without rich environment feedback

• Table 7 reports results when optimal hyperparameters are selected for each model/task combination.

• Table 8 compares average response lengths of SDPO and GRPO.

### D.2 Learning with rich environment feedback

#### D.2.1 Additional Results

Figure 15 shows the average accuracy of SDPO and GRPO stratified by question difficulty. LCB differentiates between easy, medium, and hard questions. As displayed, SDPO significantly improves over GRPO in solving medium and hard questions, highlighting the importance of rich feedback for challenging tasks. Note that this categorization of questions is different from the one in Section 5 .

In Figure 16 , we compare different train batch sizes and number of rollouts for training GRPO and SDPO on LCBv6.

Complementing the results shown in Figure 8 , we show additional results using Qwen2.5-Instruct ( Qwen et al., 2024 ) in Figure 17 .

#### D.2.2 Training Stability

Figure 18 shows diverse metrics logged during training, including the loss, entropy, average gradient norm, and average response length.

.

#### D.2.3 Baselines

Table 9 compares the performance on LCBv6 of various baselines, including two variants of GRPO, GSPO, and CISPO to SDPO.

### D.3 Test-time self-distillation

Complementing the results shown in Section 5 , we show the discovery@ k k curves for all hard question in Figure 20 , and report the mean number of generations until the first discovery in Table 10 . Further, Table 11 shows the per-question accuracy of the self-teacher at the initial training step of SDPO. In Figure 19 , we ablate the choice of batch size for SDPO and the in-context reprompting strategy for multi-turn sampling.

In the selection of hard questions, we have discarded one malformed question (Q9) where the coding environment did not correctly validate the solution due to rounding inaccuracies, which led to failures even with correct logic.

## Appendix E Experiment Details

### E.1 Technical setup

All experiments were conducted on a single node equipped with four NVIDIA GH200 GPUs, for a total of 378GB VRAM. Our environment is built on top of the NVIDIA PyTorch container nvcr.io/nvidia/pytorch:25.02-py3 , with CUDA 12.8 and PyTorch v2.7.0.

Our implementation is based on the verl library ( Sheng et al., 2025 ) . We use PyTorch Fully Sharded Data Parallel (FSDP2) for distributed training. For rollout generation, we employ vLLM ( Kwon et al., 2023 ) , which enables efficient batched inference on the multi-GPU node.

### E.2 Hyperparameters

We summarize hyperparameters used for SDPO in Table 12 and those used for GRPO in Table 13 .

#### E.2.1 Details on Hyperparameter Selection ( Section 3 )

For GRPO in the experiments in Section 3 , we perform a grid search over learning rates { 10 − 5 , 10 − 6 } \{10^{-5},10^{-6}\} and minibatch sizes { 8 , 32 } \{8,32\} . For on-policy GRPO, we search over the same learning rates while fixing the minibatch size to 32. For SDPO, we grid-search over KL variants (forward KL, Jensen–Shannon), learning rates { 10 − 5 , 10 − 6 } \{10^{-5},10^{-6}\} , and minibatch sizes { 8 , 32 } \{8,32\} . For each method (GRPO, on-policy GRPO, and SDPO), we select a single hyperparameter configuration that achieves the highest validation accuracy within the first 5 hours of training, evaluated across all datasets and models used in Section 3 . We further report results obtained by selecting the optimal hyperparameter configuration separately for each model and dataset in Table 3 .

### E.3 User Templates

For multiple-choice questions and tool use, the model must be prompted in a task-specific manner. We therefore provide the prompt templates used for these settings below.

## Appendix F Qualitative Examples

### F.1 Visualization of Advantages

Figure 21 compares the advantages of SDPO and GRPO in a representative example.

### F.2 Examples

Below, we show an example from training SDPO on LCBv6 using Qwen3-8B.

⬇

### F.3 Environment Feedback

We show three examples of feedback in our coding environment, inspired by LeetCode.

### F.4 Illustrative Example

Figure 22 shows an illustrative example of the dense credit assignment in SDPO.

## Instructions for reporting errors

We are continuing to improve HTML versions of papers, and your feedback helps enhance accessibility and mobile support. To report errors in the HTML that will help us improve conversion and rendering, choose any of the methods listed below:

Click the "Report Issue" ( ) button, located in the page header.

Tip: You can select the relevant text first, to include it in your report.

Our team has already identified the following issues . We appreciate your time reviewing and reporting rendering errors we may not have found yet. Your efforts will help us improve the HTML versions for all readers, because disability should not be a barrier to accessing research. Thank you for your continued support in championing open access for all.

Have a free development cycle? Help support accessibility at arXiv! Our collaborators at LaTeXML maintain a list of packages that need conversion , and welcome developer contributions .
