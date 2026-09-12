##### Report GitHub Issue

Content selection saved. Describe the issue below:

# Compute as Teacher: Turning Inference Compute Into Reference-Free Supervision

###### Abstract

Where do learning signals come from when there is no ground truth in post-training? We show that inference compute itself can serve as supervision. By generating parallel rollouts and converting them into reference estimates, models can learn without human labels—critically, even in non-verifiable domains like healthcare guidance where no programmatic checker exists. We call this framework Compute as Teacher (CaT) and it turns inference-time compute from parallel rollouts into supervision for RL training. The framework has two components: (1) reference estimation which aggregates rollouts into a pseudo-reference answer, and (2) reward derivation which converts that pseudo-reference into RL rewards. For (1), we explore a simple method we call synthesis , but the framework admits any aggregator. For (2), we introduce self-proposed rubrics for non-verifiable domains. These are binary, auditable criteria generated from the pseudo-reference and scored by an LLM judge. On HealthBench, models trained with CaT match or exceed inference-time aggregation quality while using 9× less test-time compute. Here, CaT also competes with learning from expert physician annotations, yielding up to +30% relative improvement over the initial policy. The framework extends naturally to verifiable rewards, matching the best existing baselines on MATH-500 in test-time RL and demonstrating ‘drop-in’ versatility across both types of domains.

## 1 Introduction

Post-training large language models for specialized skills typically relies on supervised fine-tuning with labeled reference answers ( Ouyang et al., 2022 ; Wei et al., 2022 ) , or reinforcement learning with verifiable rewards from programmatic checkers. Such programmatic checkers are only applicable in narrow domains like math or code where formal correctness is computable ( Lambert et al., 2025 ; Shao et al., 2024 ) . Meanwhile, many valuable tasks also have no annotated reference answers. In non-verifiable settings, i.e., where answers are qualitative , such as clinical or lifestyle guidance ( Arora et al., 2025 ) , freeform dialogue ( Roller et al., 2020 ) , and creative writing ( Paech, 2023 ) , there may be multiple valid answers; experts can disagree, and deterministic rule-checking is impractical. As a result, practitioners often fall back on (i) annotation pipelines that are hard to scale, or (ii) judge-only feedback where another LLM assigns coarse scores to freeform outputs, despite known issues with inconsistency, verbosity bias, and reward hacking.

Instead, this paper asks a simple question: Can inference compute substitute for missing supervision?

##### Compute as Teacher (CaT).

We answer yes . We propose CaT, a framework that converts inference compute into supervision via two components: reference estimation and reward derivation . Crucially, parallel rollouts sample the model’s uncertainty as they differ precisely where the model is unsure. One rollout might have a correct intermediate step, another the right final answer, a third a useful verification. Collectively, the set contains more information than any individual rollout. Reference estimation aggregates this distributed information into a single pseudo-reference; reward derivation scores rollouts against the pseudo-reference for RL. Notably, the framework is agnostic to the aggregation method. Selection strategies (majority vote, best-of-N) recover the best rollout while generative strategies construct new responses by combining fragments across rollouts. We explore synthesis , a simple strategy where a frozen LLM policy conditions on the rollout set and constructs a new response, but any aggregator plugs into the same reward derivation mechanism. Since group RL methods like GRPO already generate parallel rollouts for advantage estimation, the reference estimation step adds little overhead.

##### Reference-free rewards for non-verifiable domains.

The second component, reward derivation, differs by domain. In verifiable settings (e.g., math and code), we simply check agreement with the pseudo-reference, i.e., does the rollout’s answer match? The harder problem is non-verifiable domains, where no such check exists. Here we introduce another key contribution— self-proposed rubrics —where the model generates binary criteria that characterize the pseudo-reference (e.g., “recommends consulting a medical professional,” “raises the patient’s arrhythmia concern”). An independent LLM judge checks rollouts against each criterion, and the reward is the fraction satisfied. This allows us to reward each rollout without a ground truth and enables reference-free training with RL in non-verifiable domains.

##### Why it works (intuition).

Rollouts sample from the model’s uncertainty as when they disagree, they expose where the model hedges. Synthesis forces the model to examine that disagreement and either commit to one view with evidence or construct a reconciliation. In contrast, selection can only pick one existing answer. For non-verifiable domains, rubrics ask “does this response satisfy criterion X?” rather than “is this response good?” making verification easier as decomposition turns a fuzzy judgment into a sum of fine-grained binary checks. Critically, self-proposing rubrics based on the pseudo-reference means that CaT can provide rewards for rollouts in non-verifiable domains without relying on any human annotated reference answers.

##### Practicality.

The framework is practical and drop-in. It requires no human labels, no domain-specific verifiers, and reuses group sampling compute already spent in standard RL. CaT amortizes inference-time aggregation into model weights, matching or exceeding aggregation performance while reducing per-query test-time compute by up to 9×. The trained policy’s responses also often surpass the initial aggregated pseudo-references in quality and demonstrate continued improvement until rollouts converge to similar responses. We validate across three model families (Gemma 3 4B, Qwen 3 4B, Llama 3.1 8B) on HealthBench (non-verifiable) and MATH-500 (verifiable).

##### CaT bridges several lines of work.

Like self-training ( Schmidhuber, 2003 ; Schmidhuber, 2013 ; Silver et al., 2016 ; Silver et al., 2018 ) and knowledge distillation ( Hinton et al., 2015 ) , it learns from model-generated supervision, but it derives the target by reconciling multiple samples rather than trusting a single self-label. Like test-time scaling methods (majority vote, best-of-N), it leverages parallel rollouts, but amortizes the improvements into weights via RL. Compared to LLM-as-a-judge rewards ( Zheng et al., 2023 ) , rubric-based scoring yields decomposed, specific criteria that mitigate instability and bias ( Dineen et al., 2025 ; Gunjal et al., 2026 ) . Finally, CaT complements programmatic verification ( Lambert et al., 2025 ) by extending learning to non-verifiable domains where formal checkers are unavailable.

Contributions: 1. Self-proposed rubrics for non-verifiable RL. A reward mechanism that decomposes judgment into binary criteria, enabling reference-free RL in domains where no programmatic checker exists.

2. Compute as Teacher (CaT). A general paradigm for converting inference compute into supervision via reference estimation and reward derivation, with synthesis as one effective reference estimator.

3. Comprehensive empirical study. Gains on HealthBench (non-verifiable) and MATH-500 (verifiable) across three models, with trained models matching or exceeding inference-time quality at 9× less compute.

##### Organization.

Section 2 contextualizes CaT among related work. Section 3 formalizes CaT and the self-proposed rubric mechanism. Section 4 details experimental setup. Section 4.2 presents results, ablations, and further analyses. Section 5 discusses limitations, future work, and concludes.

## 2 Related Work

##### Reference-Free Fine-Tuning.

Self-generated supervision has a long history in LLM training. Constitutional AI ( Bai et al., 2022 ) trains on self-revised generations, Self-Instruct ( Wang et al., 2023b ) generates and filters its own instruction-following data, and Quiet-STaR ( Zelikman et al., 2024 ) learns to produce reasoning tokens without reference traces. These methods target specific capabilities (harmlessness, instruction-following, reasoning). CaT is more general as it enables RL without human references in domains where models can generate diverse rollouts and, if not verifiable, where rubric-based judgment is reliable.

##### Reference-Free RL.

Recent work has explored RL without ground-truth labels. TTRL ( Zuo et al., 2025 ) uses majority-vote consensus as pseudo-labels for math and Absolute Zero ( Zhao et al., 2025a ) employs self-play on self-posed problems in math and code. These methods are effective but restricted to verifiable domains where correctness can be checked programmatically. A parallel line of work minimizes entropy or maximizes self-certainty ( Zhao et al., 2026 ; Agarwal et al., 2025 ; Prabhudesai et al., 2025 ; Gao et al., 2025 ; Li et al., 2025 ) . In particular, Wen et al. (2025) score multiple-choice answers via mutual predictability. These approaches are discriminative as they select or score existing outputs. CaT may use any of these methods as reference estimators, but it can also go beyond selection. Synthesis, if chosen as the reference estimation strategy, can construct pseudo-references outside of the rollout distribution. More critically, CaT extends to non-verifiable domains via self-proposed rubrics. Prior methods have not been applied in such settings. When we adapt them as baselines, they underperform CaT (Section 3.1 ).

##### Test-Time Scaling.

Parallel rollouts have long been used to improve inference-time performance. Majority voting or self-consistency ( Wang et al., 2023a ) selects the most common answer; best-of-N selects by confidence, perplexity, or LLM judgment ( Zheng et al., 2023 ) . These methods improve accuracy but do not transfer improvements into weights as each deployment pays the full G G -rollout cost, where G G is the number of rollouts sampled. CaT uses the same parallel rollouts to generate supervision for RL, amortizing inference compute into training. After training, the model matches or exceeds aggregation quality at 1 / G 1/G the test-time cost. Therefore, most of the compute is spent once during training, rather than repeatedly at inference time.

##### Non-Verifiable RL.

When programmatic verification is impossible, how do you derive rewards? Existing approaches assume access to reference answers. VeriFree ( Zhou et al., 2026 ) , JEPO ( Tang et al., 2025 ) , and RLPR ( Yu et al., 2025 ) compute the probability of a reference under the model’s reasoning chain. Rubrics as Rewards ( Gunjal et al., 2026 , RaR;) constructs evaluation rubrics from reference answers, then scores outputs via LLM judgment, demonstrating that rubric-based rewards outperform direct LLM-as-judge scoring. We build on this insight but remove the reference dependency entirely as CaT self-proposes rubrics from pseudo-references estimated from rollouts. Here, inference compute generates the pseudo-reference, the pseudo-reference generates rubrics, and rubrics generate rewards. Therefore, no human annotation enters the pipeline.

## 3 Compute as Teacher (CaT)

CaT converts inference compute into supervision via two components: reference estimation and reward derivation . Figure 1 illustrates the framework.

Given a prompt q q , the current policy π t \pi_{t} generates G G parallel rollouts o 1 : G o_{1:G} . These rollouts sample the model’s uncertainty as they differ precisely where the model is unsure. Reference estimation aggregates them into a pseudo-reference s s , which is a single response that serves as the supervision target. Reward derivation then scores each rollout o i o_{i} against s s , producing rewards R ⁡ ( o i , s ) R(o_{i};s) for RL.

The framework is agnostic to the aggregation method. Selection strategies (majority vote, best-of-N) choose one rollout as s s . Generative strategies like synthesis construct a new s s conditioned on all rollouts, potentially combining correct fragments scattered across the set. We explore synthesis empirically, but the reward derivation machinery—particularly self-proposed rubrics for non-verifiable domains—works with any reference estimation strategy.

##### Notation.

We write q q for the prompt, o i o_{i} for a rollout, s s for the pseudo-reference, ℛ = { r j } \mathcal{R}=\{r_{j}\} for a rubric (a set of binary criteria), π t \pi_{t} for the current policy at training step t t , π 0 \pi_{0} for the frozen anchor (the initial policy), and π J \pi_{J} for the judge model used in rubric scoring.

### 3.1 Reference Estimation

Reference estimation aggregates G G rollouts into a single pseudo-reference s s . Any aggregation strategy is compatible with the framework. Examples include:

• Majority vote : s s is the most common final answer among o 1 : G o_{1:G} ( Zuo et al., 2025 ) . Applicable only in verifiable domains where answers can be compared.

• Best-of-N : s = arg ⁡ max o i ⁡ f ⁡ ( o i ) s=\arg\max_{o_{i}}f(o_{i}) for some scoring function f f . This could be perplexity under the model ( Agarwal et al., 2025 ) , confidence heuristics ( Li et al., 2025 ) , or LLM judge scores.

• Synthesis : A frozen anchor π 0 \pi_{0} conditions on the rollout set and generates a new response that reconciles information across rollouts according to some prompt.

Selection methods can recover at most the best rollout. Synthesis can construct responses that combine correct fragments from multiple rollouts, potentially exceeding all of them. We focus on synthesis, though we compare against selection baselines in Section 4.4 .

##### Synthesis.

Given rollouts o 1 : G ∼ π t ( ⋅ ∣ q ) o_{1:G}\sim\pi_{t}(\cdot\mid q) , the anchor generates a pseudo-reference s ∼ π 0 ( ⋅ ∣ p syn , o 1 : G ) s\sim\pi_{0}\!\left(\cdot\mid p_{\text{syn}},o_{1:G}\right) (1) where p syn p_{\text{syn}} is a prompt instructing the model to reconcile the rollouts into a single, improved response. We provide p syn p_{\text{syn}} in Appendix F .

Two design choices merit explanation. First, we omit the original prompt q q from the anchor’s input for simplicity (ablation in Appendix A.4 ). Second, we use a frozen anchor (the initial policy π 0 \pi_{0} ) rather than the current policy π t \pi_{t} . This decouples exploration from estimation as π t \pi_{t} explores and improves through RL while π 0 \pi_{0} provides reference estimates. We optimize only π t \pi_{t} .

##### When does synthesis help?

Rollouts sample the model’s uncertainty since they disagree where the model hedges. A rollout might have a correct intermediate step but wrong conclusion while another might have the right answer via flawed reasoning. Synthesis examines the disagreement and can integrate complementary evidence such as correct steps from one rollout, and valid checks from another. Empirically, synthesis produces answers that disagree with the majority on 5–15% of questions and can disagree with all rollouts while still being correct (Section 4.5 ), indicating it performs a form of structured generative reconciliation rather than only rewriting answers and acting as a selector.

### 3.2 Reward Derivation

Given a pseudo-reference s s , we derive per-rollout rewards R ⁡ ( o i , s ) R(o_{i};s) for RL training. The mechanism differs by domain.

#### 3.2.1 Verifiable Domains

When correctness is programmatically checkable, we reward agreement with the pseudo-reference: R ver ( o ; s ) = 𝟏 [ answer ( o ) = answer ( s ) ] R_{\text{ver}}(o;s)=\mathbf{1}[\texttt{answer}(o)=\texttt{answer}(s)] (2) For math problems, answer ​ ( ⋅ ) \texttt{answer}(\cdot) extracts the final boxed expression and we check string equivalence. This is intentionally simple as the complexity in verifiable domains lies in reference estimation rather than reward derivation.

#### 3.2.2 Non-Verifiable Domains

Non-verifiable domains lack such programmatic checkers because there are numerous ways to express equivalently strong answers and therefore rule-based methods are impractical. The naive alternative, direct LLM-as-judge scoring (e.g., “rate this response 1–10”), suffers from well-documented issues such as inconsistency across prompts, bias toward verbose or stylistically fluent responses, and general susceptibility to reward hacking ( Zheng et al., 2023 ; Arora et al., 2025 ) .

We instead decompose judgment into self-proposed rubrics : binary criteria generated from the pseudo-reference and scored independently (Figure 2 ).

##### Rubric Generation.

The anchor generates a rubric ℛ = { r 1 , … , r n } \mathcal{R}=\{r_{1},\ldots,r_{n}\} from the pseudo-reference: ℛ ∼ π 0 ( ⋅ ∣ p rub , s ) \mathcal{R}\sim\pi_{0}\!\left(\cdot\mid p_{\text{rub}},s\right) (3) Each criterion r j r_{j} is a binary, verifiable statement capturing an important property of s s . We prompt for n ≥ 5 n\geq 5 specific criteria. The full rubric generation prompt p rub p_{\text{rub}} is provided in Appendix F .

##### Rubric Scoring.

An independent judge model π J \pi_{J} evaluates whether a rollout o o satisfies each criterion: R rub ( o ; ℛ ) = 1 n ∑ j = 1 n [ π J ( o , r j ) = “yes” ] R_{\text{rub}}(o;\mathcal{R})=\frac{1}{n}\sum_{j=1}^{n}\mathbf{1}\!\left[\pi_{J}(o,r_{j})=\text{``yes''}\right] (4) The reward is the fraction of criteria satisfied according to the judge π J \pi_{J} .

##### Why Rubrics?

Decomposition offers three advantages: 1. Reliability. Each binary check is simple enough for an LLM to answer consistently. “Does this response recommend professional consultation?” is easier to judge than “Is this response good?”

2. Auditability. One can inspect which criteria a rollout satisfied or failed, enabling debugging and analysis. Direct judge scores are opaque.

3. Reduced surface-form bias. A response can satisfy “recommends lifestyle modifications” regardless of exact phrasing, length, or formatting. Therefore, rubrics help to reward content rather than style.

##### Example.

Consider a user asking about managing mild hypertension. Synthesis produces a pseudo-reference recommending dietary changes, exercise, and medical follow-up. The anchor generates rubrics: 1. Acknowledges the user’s stated symptoms

2. Suggests lifestyle modifications (diet, exercise)

3. Recommends consulting a healthcare provider

4. Avoids providing a definitive diagnosis

5. Uses empathetic and appropriate tone

A rollout satisfying criteria 1, 2, 3, and 5 but failing criterion 4 receives reward R = 4 / 5 = 0.8 R=4/5=0.8 .

### 3.3 Training

We instantiate CaT with Group Relative Policy Optimization ( Shao et al., 2024 , GRPO;) , though the reward formulation is compatible with any policy gradient method that samples multiple rollouts per prompt.

##### GRPO Overview.

For each prompt q q , GRPO samples G G rollouts from the current policy and computes advantages relative to the group mean: A ^ i = R ⁡ ( o i , s ) − R ¯ G σ G \hat{A}_{i}=\frac{R(o_{i};s)-\bar{R}_{G}}{\sigma_{G}} (5) where R ¯ G = 1 G ​ ∑ j = 1 G R ⁡ ( o j , s ) \bar{R}_{G}=\frac{1}{G}\sum_{j=1}^{G}R(o_{j};s) is the mean reward and σ G \sigma_{G} its standard deviation. The policy is updated via a clipped surrogate objective with KL regularization to the initial policy π 0 \pi_{0} . Full details are in Appendix E .

##### Integration with CaT.

GRPO already generates G G parallel rollouts for advantage estimation. CaT reuses these rollouts for reference estimation, adding only: 1. One synthesis call to generate s s from o 1 : G o_{1:G}

2. For non-verifiable domains: one rubric generation call, then n × G n\times G judge calls to score n n criteria

The synthesis call is comparable in cost to generating one additional rollout. Rubric scoring requires n × G n\times G judge calls per prompt, which we parallelize. These calls are low in cost as they require very few output tokens (yes/no). In practice, reference estimation and reward derivation add modest overhead relative to the cost of generating G G rollouts.

##### Training Loop.

Algorithm 1 summarizes one iteration of CaT. For each prompt: (1) sample rollouts from the current policy, (2) estimate a pseudo-reference, (3) derive rewards (programmatic for verifiable, rubric-based for non-verifiable), and (4) update the policy via GRPO.

##### Inference-Time Use.

Reference estimation can also be used purely at inference time, without RL training. Given a prompt, generate G G rollouts from the base policy π 0 \pi_{0} , estimate a pseudo-reference, and return s s as the final response. This provides immediate accuracy gains at the cost of ≥ G × \geq G\times inference compute. However, the gains do not transfer to the model weights as each deployment pays the full cost.

CaT amortizes these gains as after training, the policy π t \pi_{t} produces responses of similar or better quality than inference-time synthesis while using only a single output. In our experiments, CaT matches or exceeds inference-time synthesis at 9 × 9\times less test-time compute.

## 4 Experiments

We evaluate two aspects of our contribution. Mainly, CaT as a training framework, where we use synthesis for reference estimation. Secondarily, we also evaluate synthesis alone, i.e., reference estimation without training, to isolate the gains from each component. Our experiments address three key questions:

1. Does CaT improve over the base policy, and can it match or exceed inference-time synthesis at lower test-time cost?

2. Do self-proposed rubrics provide effective rewards in non-verifiable domains?

3. How does synthesis compare to selection baselines for reference estimation?

### 4.1 Setup

##### Datasets.

We evaluate on two domains: • HealthBench ( Arora et al., 2025 ) : 5,000 freeform healthcare conversations between physicians and users. This is a non-verifiable domain where responses are qualitative, multiple valid answers exist, and no programmatic checker is available. We hold out 500 conversations with physician-designed evaluation rubrics for testing; the remainder is used for reference-free training and validation.

• MATH-500 ( Hendrycks et al., 2021 ) : 500 competition mathematics problems. This is a verifiable domain in which final answers can be checked programmatically. Following Zuo et al. (2025) , we train and test on the same 500 problems, where training has no access to any reference labels, as a test-time training setup.

HealthBench is our primary testbed because non-verifiable domains represent the harder, unsolved problem. MATH-500 serves a different purpose, demonstrating that CaT generalizes across domain types without modification, functioning as a unified ‘plug-and-play’ framework rather than a method specific to only non-verifiable domains.

##### Models.

We evaluate three instruction-tuned model families at the 4–8B scale: Gemma 3 4B Instruct ( Kamath et al., 2025 ) , Qwen 3 4B Instruct ( Yang et al., 2025 ) , and Llama 3.1 8B Instruct ( Grattafiori et al., 2024 ) . For synthesis and rubric generation, the anchor π 0 \pi_{0} is the initial policy (the same model before training). For rubric scoring, we use GPT-4o ( Hurst et al., 2024 ) as the judge π J \pi_{J} . Unless specified otherwise, we always use synthesis as the reference estimation strategy with CaT.

##### Evaluation.

On HealthBench, we report response accuracy using the held-out physician-designed rubrics, with a judge model (GPT-4o) as in the benchmark paper ( Arora et al., 2025 ) . On MATH-500, we report accuracy (fraction of problems with correct final answers). We always use G = 8 G=8 rollouts. Error bars are standard errors computed across test samples. See Appendix H for hyperparameters and Appendix I for additional experimental details.

### 4.2 Main Results

Figure 3 summarizes our main findings. CaT improves over the initial policy across all models and both domains, with improvements of up to +30% on HealthBench and +33% on MATH-500 relative to the base untrained policy.

##### CaT matches or exceeds inference-time synthesis.

On HealthBench, CaT consistently outperforms inference-time synthesis. On MATH-500, the two are comparable, with CaT slightly ahead on Gemma and Llama, and slightly behind on Qwen. Critically, CaT achieves this with 9 × 9\times less test-time compute on HealthBench (the generalization induction setting). The trained policy produces a single response, while inference-time synthesis requires G = 8 G=8 rollouts plus one generation step.

##### CaT enables improvement until rollouts converge.

Better policies generate more informative rollouts, which yield better pseudo-references, which further improve the policy. We observe this dynamic across all models as CaT surpasses its own teacher signal (the initial synthesis-generated pseudo-references) on 5 of 6 model-dataset pairs. After sufficient training, rollouts converge. Here, they agree more often, leaving less disagreement for synthesis to reconcile. At this point, the pseudo-reference provides diminishing signal over individual rollouts (Appendix D ). This is consistent with known entropy collapse in RL fine-tuning ( Yue et al., 2025 ; Song et al., 2025b ) .

### 4.3 Self-Proposed Rubrics for Non-Verifiable Domains

The central challenge in non-verifiable domains is reward derivation. We therefore compare three approaches:

• Self-proposed rubrics (ours) : Rubrics generated from the pseudo-reference.

• Physician rubrics : Human-annotated rubrics from HealthBench (oracle baseline).

• Model-as-judge : Direct LLM judgment of whether rollouts match the pseudo-reference.

##### Self-proposed rubrics compete with expert annotations.

Figure 4 (left) shows that self-proposed rubrics outperform model-as-judge on all three models and are similar to physician-annotated rubrics on two of three. The model generates evaluation criteria that are sometimes as effective as those designed by domain experts, without any human input. Poor performance with model-as-judge is likely due to the brittleness of coarse-grained judgements.

##### RL with rubrics outperforms SFT.

Figure 4 (right) compares CaT against supervised fine-tuning on synthesized pseudo-references (CaT-SFT). CaT wins on all three models, often substantially (Llama: 0.38 vs 0.28). This is consistent with prior findings that RL generalizes better than SFT from limited data ( Chu et al., 2025 ; Gunjal et al., 2026 ) .

### 4.4 Reference Estimation: Synthesis vs Selection

We compare synthesis against selection baselines for reference estimation, evaluated at inference (no RL training). This allows us to determine the best reference estimation strategies to use within the CaT framework.

##### Selection baselines.

We compare synthesis against: • Single sample : One rollout from the policy (no aggregation).

• Majority vote : Select the most common final answer across G G rollouts (verifiable domains only).

• Best-of-N (Self-BoN) : The policy selects its own best response from G G rollouts.

• Min perplexity : Select the rollout with lowest perplexity under the model, e.g., Agarwal et al. (2025) .

• Mutual predictability ( Wen et al., 2025 ) : Select the rollout with highest probability when conditioned on all other rollouts.

##### Synthesis matches or exceeds selection methods.

Figure 5 shows inference-time performance across models and datasets. Synthesis is highly effective in the non-verifiable domain, outperforming all baselines on HealthBench. It also matches or exceeds them on MATH-500, allowing it to be dropped in for use across domain types. We also provide some RL results with alternative selection methods in Appendix A.1 . We note that Llama 3.1 8B—the oldest model—shows smaller gains from synthesis over selection baselines, though sees the largest gains with RL. Synthesis requires the model to identify and resolve differences across rollouts, which weaker models may struggle with due to lower baseline capacity for meta-cognitive reasoning.

### 4.5 How Does Synthesis Differ From Selection?

Selection methods can at best recover the best rollout while generative methods, such as synthesis, can construct new responses that may exceed the best rollout. In this section, we analyze when and how this matters.

##### Synthesis disagrees with consensus.

Table 1 shows that synthesis disagrees with majority vote on 5–7% of questions and with Self-BoN on 7–10%. When synthesis disagrees, it is correct substantially more often than chance: 82–86% against majority vote, 70–82% against Self-BoN. Therefore, when it disagrees, it provides an answer that improves performance on average. These answers are useful responses that are beyond the reach of selection methods.

##### Synthesis can correct all rollouts.

On ∼ \sim 1% of questions, synthesis produces a correct answer when all rollouts are wrong. This is impossible with selection as these answers are outside of the distribution of the rollout set. Appendix B provides a worked example where rollouts contain complementary arithmetic errors. Here, synthesis integrates the correct reasoning steps while avoiding the errors.

##### Synthesis reasons over multiple rollouts.

One might ask whether synthesis simply benefits from generating one more sample instead of using the rollouts. To test this, we compare synthesis conditioned on 8 rollouts versus 1 rollout. Using Qwen 3 4B on MATH-500, with a single rollout in context, synthesis improves only marginally over that rollout (0.80 vs 0.79); with 8 rollouts, it substantially outperforms majority voting (0.85 vs 0.81). Therefore, synthesis may reconcile information across rollouts rather than act as an independent sample. Analysis of synthesis outputs in Appendix C provide further evidence.

## 5 Discussion

##### Limitations and future work.

CaT requires the base model to generate useful rollouts and, for synthesis, to reconcile them coherently; models with lower base performance see smaller gains. The framework inherits a known RL limitation: as the policy improves, rollout diversity decreases, and synthesis has less disagreement to reconcile. Training gains plateau once rollouts converge (Appendix D ). Performance may also depend on the capability of the judge model (Appendix A.3 ). Future work could generate more diverse rollouts through better sampling or exploration rewards, e.g., Song et al. (2025a) . Reference estimation and reward derivation can be improved independently. Using learned aggregators may outperform prompting-based synthesis. For reward derivation, finer-grained rubrics, e.g., partial credit, hierarchical criteria, and confidence weighting, may improve scoring accuracy and granularity. Beyond single-turn responses, CaT could extend to reasoning traces, multi-turn dialogues, or agentic trajectories.

##### Conclusion.

We introduced Compute as Teacher, a framework for converting inference compute into supervision. Parallel rollouts sample the model’s uncertainty while reference estimation aggregates them into pseudo-references. A reward derivation step converts pseudo-references into RL rewards. The framework is agnostic to the aggregation method. We demonstrated synthesis as one strong option, but majority vote and best-of-N may also apply. Our core contribution is enabling reference-free RL in non-verifiable domains. Self-proposed rubrics provide stable rewards without human annotation. On HealthBench, these rubrics are similar to physician-designed ones in performance, and CaT improves over the base policy by up to 30% (relative). Trained models match or exceed inference-time aggregation quality at 9 × 9\times less test-time compute. Therefore, CaT enables spending compute once during training instead of repeatedly at inference. On verifiable domains (MATH-500), CaT performs as well as any other approach, showing the framework is ‘plug-and-play’ across domain types. Compute as Teacher provides a practical framework for post-training language models on non-verifiable and verifiable domains where reference answers are scarce, expensive, contested, or even unknown. As human annotation becomes the bottleneck for specialized domains, learning from inference compute offers one possible path forward.

## Acknowledgements

In alphabetical order, we would like to thank the following people: Joseph Brennan for assistance with rubric data, Lovish Madaan for various technical assistance, Nicola Cancedda for feedback on institutional approval processes, Stéphane Collot for guidance on rubric generation, Yonatan Gideoni for comments on a draft of this work, and Yunzhen Feng for general technical advice.

DJ was an intern at Meta at the time of this work and is supported by an AWS Studentship from the EPSRC Centre for Doctoral Training in Autonomous Intelligent Machines and Systems (AIMS) (EP/S024050/1).

## References

Agarwal et al. (2025) Shivam Agarwal, Zimin Zhang, Lifan Yuan, Jiawei Han, and Hao Peng. The unreasonable effectiveness of entropy minimization in LLM reasoning. In The Thirty-ninth Annual Conference on Neural Information Processing Systems , 2025. https://openreview.net/forum?id=UfFTBEsLgI .

Arora et al. (2025) Rahul K Arora, Jason Wei, Rebecca Soskin Hicks, Preston Bowman, Joaquin Quiñonero-Candela, Foivos Tsimpourlas, Michael Sharman, Meghan Shah, Andrea Vallone, Alex Beutel, et al. HealthBench: Evaluating large language models towards improved human health. arXiv preprint arXiv:2505.08775 , 2025.

Bai et al. (2022) Yuntao Bai, Saurav Kadavath, Sandipan Kundu, Amanda Askell, Jackson Kernion, Andy Jones, Anna Chen, Anna Goldie, Azalia Mirhoseini, Cameron McKinnon, et al. Constitutional AI: Harmlessness from AI feedback. arXiv preprint arXiv:2212.08073 , 2022.

Chu et al. (2025) Tianzhe Chu, Yuexiang Zhai, Jihan Yang, Shengbang Tong, Saining Xie, Dale Schuurmans, Quoc V Le, Sergey Levine, and Yi Ma. SFT memorizes, RL generalizes: A comparative study of foundation model post-training. In Forty-second International Conference on Machine Learning , 2025. https://openreview.net/forum?id=dYur3yabMj .

Dineen et al. (2025) Jacob Dineen, Aswin RRV, Qin Liu, Zhikun Xu, Xiao Ye, Ming Shen, Zhaonan Li, Shijie Lu, Chitta Baral, Muhao Chen, and Ben Zhou. QA-LIGN: aligning LLMs through constitutionally decomposed QA. In Findings of the Association for Computational Linguistics: EMNLP 2025, Suzhou, China, November 4-9, 2025 , pages 20619–20642. Association for Computational Linguistics, 2025.

Gao et al. (2025) Zitian Gao, Lynx Chen, Joey Zhou, and Bryan Dai. One-shot entropy minimization. arXiv preprint arXiv:2505.20282 , 2025.

Grattafiori et al. (2024) Aaron Grattafiori, Abhimanyu Dubey, Abhinav Jauhri, Abhinav Pandey, Abhishek Kadian, Ahmad Al-Dahle, Aiesha Letman, Akhil Mathur, Alan Schelten, Alex Vaughan, et al. The Llama 3 herd of models. arXiv preprint arXiv:2407.21783 , 2024.

Gunjal et al. (2026) Anisha Gunjal, Anthony Wang, Elaine Lau, Vaskar Nath, Bing Liu, and Sean Hendryx. Rubrics as rewards: Reinforcement learning beyond verifiable domains. In The Fourteenth International Conference on Learning Representations , 2026. https://openreview.net/forum?id=c1bTcrDmt4 .

Hendrycks et al. (2021) Dan Hendrycks, Collin Burns, Saurav Kadavath, Akul Arora, Steven Basart, Eric Tang, Dawn Song, and Jacob Steinhardt. Measuring mathematical problem solving with the MATH dataset. In Proceedings of the Neural Information Processing Systems Track on Datasets and Benchmarks 1, NeurIPS Datasets and Benchmarks 2021, December 2021, virtual , 2021. https://datasets-benchmarks-proceedings.neurips.cc/paper/2021/hash/be83ab3ecd0db773eb2dc1b0a17836a1-Abstract-round2.html .

Hinton et al. (2015) Geoffrey Hinton, Oriol Vinyals, and Jeff Dean. Distilling the knowledge in a neural network. arXiv preprint arXiv:1503.02531 , 2015.

Hu et al. (2022) Edward J. Hu, Yelong Shen, Phillip Wallis, Zeyuan Allen-Zhu, Yuanzhi Li, Shean Wang, Lu Wang, and Weizhu Chen. LoRA: Low-rank adaptation of large language models. In The Tenth International Conference on Learning Representations, ICLR 2022, Virtual Event, April 25-29, 2022 . OpenReview.net, 2022. https://openreview.net/forum?id=nZeVKeeFYf9 .

Hurst et al. (2024) Aaron Hurst, Adam Lerer, Adam P Goucher, Adam Perelman, Aditya Ramesh, Aidan Clark, AJ Ostrow, Akila Welihinda, Alan Hayes, Alec Radford, et al. GPT-4o system card. arXiv preprint arXiv:2410.21276 , 2024.

Kamath et al. (2025) Aishwarya Kamath, Johan Ferret, Shreya Pathak, Nino Vieillard, Ramona Merhej, Sarah Perrin, Tatiana Matejovicova, Alexandre Ramé, Morgane Rivière, et al. Gemma 3 technical report. arXiv preprint arXiv:2503.19786 , 2025.

Lambert et al. (2025) Nathan Lambert, Jacob Morrison, Valentina Pyatkin, Shengyi Huang, Hamish Ivison, Faeze Brahman, Lester James Validad Miranda, Alisa Liu, Nouha Dziri, Xinxi Lyu, Yuling Gu, Saumya Malik, Victoria Graf, Jena D. Hwang, Jiangjiang Yang, Ronan Le Bras, Oyvind Tafjord, Christopher Wilhelm, Luca Soldaini, Noah A. Smith, Yizhong Wang, Pradeep Dasigi, and Hannaneh Hajishirzi. Tulu 3: Pushing frontiers in open language model post-training. In Second Conference on Language Modeling (COLM) , 2025. https://openreview.net/forum?id=i1uGbfHHpH .

Li et al. (2025) Pengyi Li, Matvey Skripkin, Alexander Zubrey, Andrey Kuznetsov, and Ivan Oseledets. Confidence Is All You Need: Few-shot rl fine-tuning of language models. arXiv preprint arXiv:2506.06395 , 2025.

Loshchilov and Hutter (2019) Ilya Loshchilov and Frank Hutter. Decoupled weight decay regularization. In 7th International Conference on Learning Representations, ICLR 2019, New Orleans, LA, USA, May 6-9, 2019 . OpenReview.net, 2019. https://openreview.net/forum?id=Bkg6RiCqY7 .

Ouyang et al. (2022) Long Ouyang, Jeffrey Wu, Xu Jiang, Diogo Almeida, Carroll L. Wainwright, Pamela Mishkin, Chong Zhang, Sandhini Agarwal, Katarina Slama, Alex Ray, John Schulman, Jacob Hilton, Fraser Kelton, Luke Miller, Maddie Simens, Amanda Askell, Peter Welinder, Paul F. Christiano, Jan Leike, and Ryan Lowe. Training language models to follow instructions with human feedback. In Advances in Neural Information Processing Systems 35: Annual Conference on Neural Information Processing Systems 2022, NeurIPS 2022, New Orleans, LA, USA, November 28 - December 9, 2022 , 2022. http://papers.nips.cc/paper_files/paper/2022/hash/b1efde53be364a73914f58805a001731-Abstract-Conference.html .

Paech (2023) Samuel J Paech. EQ-Bench: An emotional intelligence benchmark for large language models. arXiv preprint arXiv:2312.06281 , 2023.

Prabhudesai et al. (2025) Mihir Prabhudesai, Lili Chen, Alex Ippoliti, Katerina Fragkiadaki, Hao Liu, and Deepak Pathak. Maximizing confidence alone improves reasoning. arXiv preprint arXiv:2505.22660 , 2025.

Rajbhandari et al. (2020) Samyam Rajbhandari, Jeff Rasley, Olatunji Ruwase, and Yuxiong He. ZeRO: memory optimizations toward training trillion parameter models. In Proceedings of the International Conference for High Performance Computing, Networking, Storage and Analysis, SC 2020, Virtual Event / Atlanta, Georgia, USA, November 9-19, 2020 , page 20. IEEE/ACM, 2020. 10.1109/SC41405.2020.00024 . https://doi.org/10.1109/SC41405.2020.00024 .

Roller et al. (2020) Stephen Roller, Y-Lan Boureau, Jason Weston, Antoine Bordes, Emily Dinan, Angela Fan, David Gunning, Da Ju, Margaret Li, Spencer Poff, et al. Open-domain conversational agents: Current progress, open problems, and future directions. arXiv preprint arXiv:2006.12442 , 2020.

Schmidhuber (2003) Jürgen Schmidhuber. Exploring the predictable. In Advances in evolutionary computing: theory and applications , pages 579–612. Springer, 2003.

Schmidhuber (2013) Jürgen Schmidhuber. PowerPlay: Training an increasingly general problem solver by continually searching for the simplest still unsolvable problem. Frontiers in psychology , 4:313, 2013.

Schulman et al. (2017) John Schulman, Filip Wolski, Prafulla Dhariwal, Alec Radford, and Oleg Klimov. Proximal policy optimization algorithms. arXiv preprint arXiv:1707.06347 , 2017.

Shao et al. (2024) Zhihong Shao, Peiyi Wang, Qihao Zhu, Runxin Xu, Junxiao Song, Xiao Bi, Haowei Zhang, Mingchuan Zhang, YK Li, Yang Wu, et al. Deepseekmath: Pushing the limits of mathematical reasoning in open language models. arXiv preprint arXiv:2402.03300 , 2024.

Sheng et al. (2025) Guangming Sheng, Chi Zhang, Zilingfeng Ye, Xibin Wu, Wang Zhang, Ru Zhang, Yanghua Peng, Haibin Lin, and Chuan Wu. Hybridflow: A flexible and efficient RLHF framework. In Proceedings of the Twentieth European Conference on Computer Systems, EuroSys 2025, Rotterdam, The Netherlands, 30 March 2025 - 3 April 2025 , pages 1279–1297. ACM, 2025. 10.1145/3689031.3696075 . https://doi.org/10.1145/3689031.3696075 .

Silver et al. (2016) David Silver, Aja Huang, Chris J Maddison, Arthur Guez, Laurent Sifre, George Van Den Driessche, Julian Schrittwieser, Ioannis Antonoglou, Veda Panneershelvam, Marc Lanctot, et al. Mastering the game of Go with deep neural networks and tree search. Nature , 529(7587):484–489, 2016.

Silver et al. (2018) David Silver, Thomas Hubert, Julian Schrittwieser, Ioannis Antonoglou, Matthew Lai, Arthur Guez, Marc Lanctot, Laurent Sifre, Dharshan Kumaran, Thore Graepel, et al. A general reinforcement learning algorithm that masters chess, shogi, and Go through self-play. Science , 362(6419):1140–1144, 2018.

Song et al. (2025a) Yuda Song, Julia Kempe, and Remi Munos. Outcome-based exploration for LLM reasoning. arXiv preprint arXiv:2509.06941 , 2025a.

Song et al. (2025b) Yuda Song, Hanlin Zhang, Carson Eisenach, Sham M. Kakade, Dean P. Foster, and Udaya Ghai. Mind the Gap: Examining the self-improvement capabilities of large language models. In The Thirteenth International Conference on Learning Representations, ICLR 2025, Singapore, April 24-28, 2025 . OpenReview.net, 2025b. https://openreview.net/forum?id=mtJSMcF3ek .

Tang et al. (2025) Yunhao Tang, Sid Wang, Lovish Madaan, and Remi Munos. Beyond verifiable rewards: Scaling reinforcement learning in language models to unverifiable data. In The Thirty-ninth Annual Conference on Neural Information Processing Systems , 2025. https://openreview.net/forum?id=pc6M9h3T9m .

Wang et al. (2023a) Xuezhi Wang, Jason Wei, Dale Schuurmans, Quoc V. Le, Ed H. Chi, Sharan Narang, Aakanksha Chowdhery, and Denny Zhou. Self-consistency improves chain of thought reasoning in language models. In The Eleventh International Conference on Learning Representations, ICLR 2023, Kigali, Rwanda, May 1-5, 2023 . OpenReview.net, 2023a. https://openreview.net/forum?id=1PL1NIMMrw .

Wang et al. (2023b) Yizhong Wang, Yeganeh Kordi, Swaroop Mishra, Alisa Liu, Noah A. Smith, Daniel Khashabi, and Hannaneh Hajishirzi. Self-instruct: Aligning language models with self-generated instructions. In Proceedings of the 61st Annual Meeting of the Association for Computational Linguistics (Volume 1: Long Papers), ACL 2023, Toronto, Canada, July 9-14, 2023 , pages 13484–13508. Association for Computational Linguistics, 2023b. 10.18653/V1/2023.ACL-LONG.754 . https://doi.org/10.18653/v1/2023.acl-long.754 .

Wei et al. (2022) Jason Wei, Maarten Bosma, Vincent Y. Zhao, Kelvin Guu, Adams Wei Yu, Brian Lester, Nan Du, Andrew M. Dai, and Quoc V. Le. Finetuned language models are zero-shot learners. In The Tenth International Conference on Learning Representations, ICLR 2022, Virtual Event, April 25-29, 2022 . OpenReview.net, 2022. https://openreview.net/forum?id=gEZrGCozdqR .

Wen et al. (2025) Jiaxin Wen, Zachary Ankner, Arushi Somani, Peter Hase, Samuel Marks, Jacob Goldman-Wetzler, Linda Petrini, Henry Sleight, Collin Burns, He He, et al. Unsupervised elicitation of language models. arXiv preprint arXiv:2506.10139 , 2025.

Wu et al. (2025) Fang Wu, Weihao Xuan, Ximing Lu, Zaid Harchaoui, and Yejin Choi. The invisible leash: Why RLVR may not escape its origin. arXiv preprint arXiv:2507.14843 , 2025.

Yang et al. (2025) An Yang, Anfeng Li, Baosong Yang, Beichen Zhang, Binyuan Hui, Bo Zheng, Bowen Yu, Chang Gao, Chengen Huang, Chenxu Lv, et al. Qwen3 technical report. arXiv preprint arXiv:2505.09388 , 2025.

Yu et al. (2025) Tianyu Yu, Bo Ji, Shouli Wang, Shu Yao, Zefan Wang, Ganqu Cui, Lifan Yuan, Ning Ding, Yuan Yao, Zhiyuan Liu, et al. RLPR: Extrapolating RLVR to general domains without verifiers. arXiv preprint arXiv:2506.18254 , 2025.

Yue et al. (2025) Yang Yue, Zhiqi Chen, Rui Lu, Andrew Zhao, Zhaokai Wang, Yang Yue, Shiji Song, and Gao Huang. Does reinforcement learning really incentivize reasoning capacity in LLMs beyond the base model? In The Thirty-ninth Annual Conference on Neural Information Processing Systems , 2025. https://openreview.net/forum?id=4OsgYD7em5 .

Zelikman et al. (2024) Eric Zelikman, Georges Raif Harik, Yijia Shao, Varuna Jayasiri, Nick Haber, and Noah Goodman. Quiet-STaR: Language models can teach themselves to think before speaking. In First Conference on Language Modeling (COLM) , 2024. https://openreview.net/forum?id=oRXPiSOGH9 .

Zhao et al. (2025a) Andrew Zhao, Yiran Wu, Yang Yue, Tong Wu, Quentin Xu, Yang Yue, Matthieu Lin, Shenzhi Wang, Qingyun Wu, Zilong Zheng, and Gao Huang. Absolute Zero: Reinforced self-play reasoning with zero data. In The Thirty-ninth Annual Conference on Neural Information Processing Systems , 2025a. https://openreview.net/forum?id=neZSGqhxDa .

Zhao et al. (2025b) Rosie Zhao, Alexandru Meterez, Sham M. Kakade, Cengiz Pehlevan, Samy Jelassi, and Eran Malach. Echo chamber: RL post-training amplifies behaviors learned in pretraining. In Second Conference on Language Modeling (COLM) , 2025b. https://openreview.net/forum?id=dp4KWuSDzj .

Zhao et al. (2026) Xuandong Zhao, Zhewei Kang, Aosong Feng, Sergey Levine, and Dawn Song. Learning to reason without external rewards. In The Fourteenth International Conference on Learning Representations , 2026. https://openreview.net/forum?id=OU9nFEYR2M .

Zheng et al. (2023) Lianmin Zheng, Wei-Lin Chiang, Ying Sheng, Siyuan Zhuang, Zhanghao Wu, Yonghao Zhuang, Zi Lin, Zhuohan Li, Dacheng Li, Eric P. Xing, Hao Zhang, Joseph E. Gonzalez, and Ion Stoica. Judging LLM-as-a-Judge with MT-Bench and Chatbot Arena. In Advances in Neural Information Processing Systems 36: Annual Conference on Neural Information Processing Systems 2023, NeurIPS 2023, New Orleans, LA, USA, December 10 - 16, 2023 , 2023. http://papers.nips.cc/paper_files/paper/2023/hash/91f18a1287b398d378ef22505bf41832-Abstract-Datasets_and_Benchmarks.html .

Zhou et al. (2026) Xiangxin Zhou, Zichen Liu, Anya Sims, Haonan Wang, Tianyu Pang, Chongxuan Li, Liang Wang, Min Lin, and Chao Du. Reinforcing general reasoning without verifiers. In The Fourteenth International Conference on Learning Representations , 2026. https://openreview.net/forum?id=nnwvwge40d .

Zuo et al. (2025) Yuxin Zuo, Kaiyan Zhang, Li Sheng, Shang Qu, Ganqu Cui, Xuekai Zhu, Haozhan Li, Yuchen Zhang, Xinwei Long, Ermo Hua, Biqing Qi, Youbang Sun, Zhiyuan Ma, Lifan Yuan, Ning Ding, and Bowen Zhou. TTRL: Test-time reinforcement learning. In The Thirty-ninth Annual Conference on Neural Information Processing Systems , 2025. https://openreview.net/forum?id=VuVhgEiu20 .

## Appendix A Results Tables And Additional Results

See Tables 2 , 3 , 4 , and 5 for tabular transcriptions of the results in the figures in the main body.

### A.1 RL Results Against Selection Methods

In Table 6 , we observe that CaT outperforms the selection baselines with RL, just as synthesis did at inference time because synthesis delivers a better supervision signal.

### A.2 Conditioning Rubric Generation on the Pseudo-Reference

Table 7 ablates rubric generation where conditioning on the pseudo-reference s s outperforms conditioning only on the question q q , improving results by 12% (relative). The compute spent on reference estimation improves not just the supervision target but also the quality of the derived rubrics.

### A.3 Judge Sensitivity

In Table 8 we show results on HealthBench when running with different sized judge models. We keep the evaluation benchmark judge the same. Stronger judges somewhat lead to better performance, likely due to improved rubric judgement accuracy.

### A.4 Omitting the Question in the Synthesis Aggregator

We note that in the synthesis step, we do not include the task prompt or question in the estimator’s prompt because it did not make a difference in preliminary inference-time experiments with Gemma 3 4B on MATH-500 ( + 0.004 +0.004 ). Excluding the task prompt simplifies the setup and makes no meaningful difference to performance. It also helps ensure that the aggregator will not simply act as another rollout by attempting to answer the question directly.

## Appendix B Example: Synthesis Disagrees With All Rollouts

Disagreement with all rollouts occurs across all models. The following is one among a few examples discovered with Gemma 3 4B on the MATH-500 dataset.

All rollouts failed to provide the correct answer, exhibiting calculation errors. The following is an example from the second rollout which did not compute a division correctly:

In another example, the sixth rollout made several calculation errors, inexplicably multiplying and dividing by 137 and 1 around the same place as the second rollout:

Despite this, the synthesized response identified these errors, used the correct reasoning and provided the right final response. Since the individual rollouts failed to find the correct answer, finding the right method would not be easy for the model without observing these attempts.

## Appendix C Analysis of Synthesis Outputs

To further understand how synthesis differs from raw policy rollouts, we conducted a comparison of their generated traces. Table 9 summarizes several structural characteristics of the two sets of outputs.

Synthesis outputs have similar overall length to policy rollouts, despite achieving higher accuracy. This suggests that synthesis does not simply “think longer”. Instead, it appears to leverage and reuse reasoning already present in the rollouts, synthesizing relevant fragments rather than producing entirely new derivations. Even among synthesis outputs, correct answers are significantly shorter on average ( p < 0.05 p<0.05 ), further indicating that synthesis benefits from selectively reusing already-correct partial reasoning. Interestingly, synthesis outputs contain fewer equations and substantially fewer lines than policy rollouts. Manual inspection of the traces indicates that synthesis often summarizes or enumerates intermediate possibilities that are already explored in the rollouts, rather than reconstructing these steps in detail. This behavior is consistent with synthesis acting as a reconciling mechanism over the existing reasoning traces.

We also examined stylistic markers of reasoning. Using keyword heuristics for step-by-step patterns (e.g., “first”, “second”), we observe that synthesis employs stepwise reasoning approximately 37% less often (absolute difference). Conversely, synthesis outputs contain 9.3% more verification cues (e.g., “let’s verify”, “check”), reflecting a tendency to inspect or validate reasoning rather than generate long chains.

Overall, these observations support the interpretation that synthesis primarily reconciles and synthesizes partially correct reasoning traces from the policy rollouts, rather than behaving like an additional independent rollout.

## Appendix D When Does CaT Stop Learning?

In Figure 6 , we compare the trained policy to if we apply synthesis at inference-time to the trained policy. The latter is the final teacher signal in CaT when synthesis is used as the reference estimation strategy. At this point, we note that the teacher signal is very close to the trained policy’s performance. Therefore, the model is unable to continue improving as the teacher provides very little delta to improve.

Since the synthesis step improves upon the group rollouts by resolving contradictions, synthesizing partial solutions, and inserting omissions, if it does not improve, then this indicates that the group rollouts are generally in agreement. Here, we note that the model has gone from generating diverse solutions when it was less capable to generating less diverse, but more likely solutions when it has been trained to be more capable at solving the task. This is a commonly observed issue in RL fine-tuning ( Yue et al., 2025 ; Song et al., 2025b ; Wu et al., 2025 ; Zhao et al., 2025b ) . Its presence here places a bound on the potential reference-free improvement that can be achieved via CaT.

## Appendix E GRPO Overview

Group Relative Policy Optimisation ( Shao et al., 2024 , GRPO) is a memory-efficient variant of PPO ( Schulman et al., 2017 ) that avoids a value network by using a group baseline. For each q q , we draw G G rollouts o 1 : G o_{1:G} from the policy π θ old \pi_{\theta_{\text{old}}} and optimize J GRPO ( θ ) = 𝔼 q , { o i } [ 1 G ​ ∑ i = 1 G 1 | o i | ​ ∑ t = 1 | o i | L t ​ ( θ ) − β D KL [ π θ ∥ π ref ] ] \begin{split}J_{\mathrm{GRPO}}(\theta)\;=\;\mathbb{E}_{q,\,\{o_{i}\}}\Bigg[&\frac{1}{G}\sum_{i=1}^{G}\frac{1}{|o_{i}|}\sum_{t=1}^{|o_{i}|}L_{t}(\theta)\\ &-\;\beta\,\mathrm{D}_{\mathrm{KL}}\!\big[\pi_{\theta}\,\|\,\pi_{\mathrm{ref}}\big]\Bigg]\end{split} (6)

with the clipped surrogate L t ​ ( θ ) = min ⁡ ( r t ​ ( θ ) ​ A ^ i , t , clip ⁡ ( r t ​ ( θ ) , 1 − ε , 1 + ε ) ​ A ^ i , t ) , L_{t}(\theta)=\min\!\Big(r_{t}(\theta)\,\hat{A}_{i,t},\mathrm{clip}\!\big(r_{t}(\theta),\,1-\varepsilon,\,1+\varepsilon\big)\,\hat{A}_{i,t}\Big), (7) where the importance weighting token-level ratio and the group-normalized advantage are r t ​ ( θ ) = π θ ​ ( o i , t ∣ q , o i , < t ) π θ old ​ ( o i , t ∣ q , o i , < t ) , A ^ i , t = R ⁡ ( q , o i ) − R ¯ G σ G . r_{t}(\theta)=\frac{\pi_{\theta}(o_{i,t}\mid q,o_{i,<t})}{\pi_{\theta_{\text{old}}}(o_{i,t}\mid q,o_{i,<t})},\quad\hat{A}_{i,t}=\frac{R(q,o_{i})-\bar{R}_{G}}{\sigma_{G}}. (8) Here R ¯ G = 1 G ​ ∑ j = 1 G R ⁡ ( q , o j ) \bar{R}_{G}=\tfrac{1}{G}\sum_{j=1}^{G}R(q,o_{j}) is the group mean reward and σ G \sigma_{G} its standard deviation; the KL term discourages large policy drift from the reference π ref \pi_{\mathrm{ref}} (typically the initial policy π 0 \pi_{0} ).

## Appendix F Prompts

We provide two prompts for synthesis. We use the Freeform Synthesis Prompt for HealthBench questions, and the COT/Reasoning Synthesis Prompt for maths questions.

## Appendix G Example Rubrics

All examples in this section were generated from Qwen 3 4B on the HealthBench dataset.

## Appendix H Hyperparameters

We provide RL training parameters in Table 10 , SFT training parameters in Table 11 , and model sampling parameters in Table 12 . We use the verl library ( Sheng et al., 2025 ) for both RL and SFT. We also note that we apply a length penalty of − 1 -1 to responses longer than 750 750 tokens when training with HealthBench to discourage length-based reward hacking.

## Appendix I Experimental Details

##### Computing perplexity.

To compute the perplexity of the output tokens in response to a question, we calculate Perplexity ( w 1 , w 2 , … , w n | context ) = exp ( − 1 n ∑ i = 1 n log p ( w i | context , w 1 , … , w i − 1 ) ) \text{Perplexity}(w_{1},w_{2},\ldots,w_{n}|\text{context})=\exp\left(-\frac{1}{n}\sum_{i=1}^{n}\log p(w_{i}|\text{context},w_{1},\ldots,w_{i-1})\right) (9) where w 1 , w 2 , … , w n w_{1},w_{2},\ldots,w_{n} are the output tokens generated by the model. When selecting the best response for min(PPL), in practice we do not compute the exponential as minimizing entropy is the same as minimizing perplexity.

##### Computing mutual predictability.

For G = 8 G=8 rollouts we construct eight prompts, where we pick each rollout answer in turn to include last in the prompt and randomly order the other answers in the prompt before it. Then, we encode the prompt with the model and compute the token-level perplexity of the tokens in the final answer:

PPL ( a j ) = exp ( − 1 | a j | ∑ t = 1 | a j | log p ( w t ( j ) | context , a − j , w 1 ( j ) , … , w t − 1 ( j ) ) ) \text{PPL}(a_{j})=\exp\left(-\frac{1}{|a_{j}|}\sum_{t=1}^{|a_{j}|}\log p(w_{t}^{(j)}|\text{context},a_{-j},w_{1}^{(j)},\ldots,w_{t-1}^{(j)})\right) (10)

where a j a_{j} is the j j -th answer, | a j | |a_{j}| is its length in tokens, w t ( j ) w_{t}^{(j)} is the t t -th token of answer j j , and a − j a_{-j} represents the other answers included in the context. We pick the answer with the lowest perplexity as the best response:

a ∗ = arg ⁡ min j ∈ { 1 , … , G } ​ PPL ​ ( a j ) a^{*}=\arg\min_{j\in\{1,\ldots,G\}}\text{PPL}(a_{j}) (11)

##### Supervised fine-tuning.

For our SFT experiments, we generate G = 8 G=8 rollouts with the initial policy π 0 \pi_{0} over our HealthBench training and validation splits. Then, we use the same initial policy to synthesize the rollouts per question into a synthesized estimated reference response s s . We then fine-tune the model with the estimated reference responses as targets by minimizing the cross-entropy loss

ℒ SFT = − 𝔼 ( q , s ) ∼ 𝒟 ​ [ 1 | s | ​ ∑ t = 1 | s | log ⁡ π θ ​ ( s t | q , s < t ) ] \mathcal{L}_{\text{SFT}}=-\mathbb{E}_{(q,s)\sim\mathcal{D}}\left[\frac{1}{|s|}\sum_{t=1}^{|s|}\log\pi_{\theta}(s_{t}|q,s_{<t})\right] (12)

where q q is the input question, s s is the estimated reference response, s t s_{t} is the t t -th token of the reference response, and 𝒟 \mathcal{D} is the training dataset. We use early stopping, using the checkpoint with the lowest validation loss to evaluate the model on the held-out 500-question HealthBench test set. We also note that we train with LoRA ( Hu et al., 2022 ) due to fast overfitting and worse results with full parameter fine-tuning.

##### RL fine-tuning.

Much of the detail for RL fine-tuning is described in the main body and other appendices. Here, we note that for math data, we extract a verifiable final answer from boxed text, e.g., boxed{...} , using regular expressions and string matching where we have instructed the model to give its final answer in this form. To extract rubric judgments and rubric generations, we instruct the model to output its answer in XML format 1 1 1 See the prompts in Appendix F and https://www.w3.org/TR/xml/ . and use a standard XML tree parser to extract the result. When RL fine-tuning with HealthBench, we use early stopping, evaluating the test set with the checkpoint that yielded the best validation score. For math, since we use the test-time reinforcement learning setting ( Zuo et al., 2025 ) , we train for a fixed number of steps.

## Instructions for reporting errors

We are continuing to improve HTML versions of papers, and your feedback helps enhance accessibility and mobile support. To report errors in the HTML that will help us improve conversion and rendering, choose any of the methods listed below:

Click the "Report Issue" ( ) button, located in the page header.

Tip: You can select the relevant text first, to include it in your report.

Our team has already identified the following issues . We appreciate your time reviewing and reporting rendering errors we may not have found yet. Your efforts will help us improve the HTML versions for all readers, because disability should not be a barrier to accessing research. Thank you for your continued support in championing open access for all.

Have a free development cycle? Help support accessibility at arXiv! Our collaborators at LaTeXML maintain a list of packages that need conversion , and welcome developer contributions .
