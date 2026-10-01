##### Report GitHub Issue

Content selection saved. Describe the issue below:

\microtypesetup expansion=false

# Recursive Self-Improvement via On-Policy Distillation for Reasoning

###### Abstract

On-policy distillation (OPD) trains a student model by having it generate trajectories, then matching its next-token predictions with an external teacher’s next-token predictions. This provides a dense, token-level supervision to the student. On-policy self-distillation (OPSD) eliminates the need for the external teacher. Specifically, a second frozen copy of the student model, now given the ground truth in its context, serves as the teacher. The student model only receives the problem and learns to mimic the privileged teacher model, while the teacher remains frozen throughout training. Previous work showed that freezing the teacher is useful for training stability, but we argue that this can prevent the teacher from incorporating the improvements learned by the student during training. Our primary contribution is to address this limitation with a recursive framework built around two complementary components. First, we let the privileged teacher to co-evolve with the student so that revision learned in one round can guide the next, a process we refer to as Dynamic Co-Evolution (DCE) . Second, because stronger revision can also make responses too verbose and self-critical, we additionally train on shorter, verified rewrites of the model’s own on-policy responses. We call this complementary objective Self-Refined Concise Learning (SRCL) . Overall, our comprehensive evaluations show that DCE+SRCL outperforms OPSD across multiple model scales and four competition-level mathematics benchmarks. Specifically, on Qwen3-8B, DCE+SRCL reaches 65.97% Average@12, outperforming OPSD by 35.62 percentage points while reducing mean output length by 7.80% relative to DCE alone.

## 1 Introduction

Post-training has played a central role in recent advances in LLM reasoning. A prominent approach is reinforcement learning with verifiable rewards (RLVR), which uses an automatic checker to assign an outcome reward to a completed solution ( Shao et al., 2024 ; Yu et al., 2025 ) . Because correctness can be verified without annotating every intermediate step, RLVR scales without step-level supervision and can elicit longer derivations, intermediate verification, backtracking, and self-correction ( Guo et al., 2025 ) . However, outcome rewards provide only coarse, sequence-level supervision: they indicate whether the final answer is correct, but not where the reasoning went wrong or how it should be revised. Process supervision provides more local feedback, but generally requires step-level annotations or a separately trained verifier ( Lightman et al., 2024 ; Zhang et al., 2025b ) .

Between sparse outcome rewards and costly process supervision, on-policy distillation (OPD) offers a third route: dense token-level targets on trajectories sampled from the model being trained ( Agarwal et al., 2024 ; Lu and Lab, 2025 ) . This model serves as the student, while a separate, stronger teacher provides next-token logits for each generated prefix. These logits provide a richer token-level training signal than the student’s own predictions. However, standard OPD still requires a capable external teacher, whose guidance is not conditioned on a verified solution for the current problem. The student is therefore trained to match the teacher’s token-level predictions, potentially inheriting its errors as well as its strengths. On-policy self-distillation (OPSD) ( Zhao et al., 2026 ) addresses these limitations using two roles initialized from the same base checkpoint. During training, the student model is given only the problem and generates an on-policy response. A copy of the base checkpoint is additionally given the ground-truth solution and serves as the privileged teacher. At each prefix of the student’s response, the teacher receives the problem, the ground-truth solution, and the same generated prefix, then supplies next-token logits. OPSD minimizes the divergence between the student and teacher predictions, transferring gold-conditioned guidance to the student. To stabilize training, the teacher remains frozen in Zhao et al. (2026) .

Does access to the ground-truth solution provide informative guidance at every student-generated prefix? We probe this question on fixed incorrect Qwen3-8B trajectories from AIME 2024, AIME 2025, and AIME 2026 ( Mathematical Association of America, 2026 ) , comparing evolving student checkpoints with the frozen, gold-conditioned teacher on the same generated prefixes. Despite seeing the verified solution, the frozen teacher assigns an average probability of 94.5% to EOS at incorrect response endpoints but only 22.0% to observed reflection cues such as Wait , a common reflection marker in reasoning models ( Wang et al., 2025 ) ( fig. 1 ), indicating limited guidance from the teacher on how to recover from incorrect reasoning. Meanwhile, the student becomes substantially more likely to reflect during training, creating a growing mismatch between the evolving model and its fixed supervisor.

This mismatch exposes a limitation of freezing the privileged teacher. Revision behaviors such as self-verification, backtracking, and error correction can strengthen during post-training ( Guo et al., 2025 ; Zhu et al., 2025 ) , but a teacher fixed at the initial checkpoint cannot acquire these emerging capabilities. Thus, even when conditioned on the verified solution, its guidance may become increasingly misaligned with the student trajectories encountered later in training. This observation motivates a privileged teacher that evolves with the student.

We therefore introduce Dynamic Co-Evolution (DCE), in which the privileged teacher evolves alongside the student. After each update, the resulting checkpoint initializes both the next student and a detached, gold-conditioned privileged teacher. Revision behavior acquired in one round can therefore improve the supervision provided in the next, creating a recursive self-improvement process. However, strengthening revision introduces a second challenge. More frequent checking, and backtracking can improve recovery from mistakes while also making reasoning unnecessarily long. We therefore pair DCE with Self-Refined Concise Learning (SRCL) , which trains on shorter, answer-verified rewrites of the same on-policy responses. DCE improves the model’s ability to revise its reasoning, while SRCL encourages it to retain that capability without unnecessary token cost.

Our contributions can be summarized as follows: • We introduce Dynamic Co-Evolution (DCE) , a recursive on-policy self-distillation framework in which each updated checkpoint initializes both the next student and a detached, gold-conditioned privileged teacher. Across four competition-level mathematical reasoning benchmarks, DCE improves Average@12 accuracy over OPSD by 35.41, 37.15, and 12.98 percentage points at 8B, 4B, and 1.7B, respectively.

• We introduce Self-Refined Concise Learning (SRCL) to control the reasoning cost that can accompany stronger revision. SRCL trains on accepted, shorter self-refinements of the same on-policy responses. Under our lowest tested 8K evaluation budget, DCE+SRCL achieves 35.07% Average@12 accuracy with 7,500 mean output tokens per response, outperforming the OPSD test-time-scaling control by 6.60 percentage points while generating approximately 692 fewer tokens per response.

• We show that the privileged teacher learns to provide stronger revision guidance as it evolves with the student. Matched-budget controls show that longer generation alone does not explain the gains. Updating the teacher every round also outperforms frozen, EMA, and periodic alternatives. Fixed-trace probes corroborate the teacher’s improved revision behavior across three AIME cohorts. Its endpoint EOS probability falls from 90.4% to 41.3%, while its probability on observed reflection tokens rises from 32.8% to 77.4%.

## 2 Related Work

### 2.1 Reflection and Verification in Reasoning Post-Training

Outcome-supervised post-training can elicit reflection-like behaviors without step-level labels. GRPO removes the learned critic used by PPO and estimates advantages from relative rewards within a sampled group, making outcome-based training practical for mathematical reasoning ( Shao et al., 2024 ) . DAPO introduces clip-higher, dynamic sampling, and token-level policy loss to improve the stability and efficiency of this recipe at scale ( Yu et al., 2025 ) . DeepSeek-R1 further demonstrates that outcome-based training alone can produce rechecking, backtracking, and “aha moments” without explicit reflection supervision ( Guo et al., 2025 ) . Parallel efforts extend RL-based post-training beyond closed-form math to policy-grounded content moderation ( Firooz et al., 2025 ) , open-ended environments requiring generalization without fixed-answer verification ( Yin et al., 2026a ) , and non-verifiable tasks balancing objective reasoning gains with subjective alignment ( Yin and Shi, 2026 ) . Despite this progress, outcome-level rewards score completed responses as a whole and do not supervise the local transition where the model identifies and repairs a specific error.

A closer look suggests that these reflection-like behaviors may not be newly learned through training. R1-Zero reproductions find similar behaviors already present in some base models and attribute part of the GRPO effect to a length bias toward longer, often incorrect, responses ( Liu et al., 2025 ) . Across ten base models, response length and verification behavior do not reliably emerge together ( Zeng et al., 2025 ) . Activation-space analysis further reveals a latent, though rare, capacity for reflection that exists before any RLVR ( Zhu et al., 2025 ) . Together, these results suggest that outcome-based post-training amplifies a pre-existing behavioral prior rather than teaching the model how to recover from a particular wrong prefix.

Even when reflection does appear in generation, it does not reliably correct errors. Without external feedback, prompting a model to revise its own answer can reduce accuracy ( Huang et al., 2024 ) , and hidden-state probes reveal correctness signals that the model’s generation does not always exploit ( Zhang et al., 2025a ; Lee et al., 2025 ) . The gap between latent awareness and effective revision motivates a different form of supervision: DCE provides dense, token-level guidance on the model’s own incorrect reasoning, directly training the transition from error recognition to successful revision.

### 2.2 On-Policy and Privileged Self-Distillation

OPD trains on responses sampled from the model being optimized, while a teacher supplies next-token supervision along those same responses ( Agarwal et al., 2024 ; Lu and Lab, 2025 ) . OPSD removes the external teacher by assigning a frozen copy of the initial checkpoint to the privileged role: the student sees only the problem, whereas the teacher also receives a verified solution ( Zhao et al., 2026 ) . Follow-up methods such as RLSD and RLCSD combine this signal with reinforcement learning ( Yang et al., 2026 ; Pan et al., 2026 ) .

Formally, let p θ p_{\theta} denote the language model with parameters θ \theta . The student conditions on a problem x x and generates a response y ∼ p θ ( ⋅ ∣ x ) y\sim p_{\theta}(\cdot\mid x) . The privileged teacher scores each prefix y < t y_{<t} after additionally receiving a verified solution g g and a transition instruction τ \tau , forming the privileged context 𝒞 t ref ​ ( x , g , τ , y < t ) \mathcal{C}_{t}^{\mathrm{ref}}(x,g,\tau,y_{<t}) . Let q q and p p denote the resulting teacher and student next-token distributions, respectively, and let Δ ⁡ ( q , p ) \Delta(q,p) denote a divergence between them. Our main experiments use Forward KL, Δ ( q , p ) = D KL ( q ∥ p ) = ∑ v q ( v ) log q ⁡ ( v ) p ⁡ ( v ) \Delta(q,p)=D_{\mathrm{KL}}(q\|p)=\sum_{v}q(v)\log\frac{q(v)}{p(v)} ; alternatives are compared in section 5.5 . Standard OPSD minimizes ℒ fixed ( θ ) = 𝔼 ( x , g ) , y [ 1 | y | ∑ t = 1 | y | Δ ( p θ 0 ( ⋅ ∣ 𝒞 t ref ( x , g , τ , y < t ) ) , p θ ( ⋅ ∣ x , y < t ) ) ] , \mathcal{L}_{\mathrm{fixed}}(\theta)=\mathbb{E}_{(x,g),y}\!\left[\frac{1}{|y|}\sum_{t=1}^{|y|}\Delta\!\left(p_{\theta_{0}}\!\left(\cdot\mid\mathcal{C}_{t}^{\mathrm{ref}}(x,g,\tau,y_{<t})\right),p_{\theta}(\cdot\mid x,y_{<t})\right)\right], (1) where the teacher remains fixed at θ 0 \theta_{0} and receives no gradients, even as the student and its generated responses change throughout training.

### 2.3 Self-Refinement and Efficient Reasoning

Self-training turns a model’s own generations into new training data. STaR iteratively trains on rationales that yield correct answers and uses answer-conditioned rationalization to recover additional examples, while ReST generates, filters, and reuses model samples as offline data ( Zelikman et al., 2022 ; Gülçehre et al., 2023 ) . In alignment, SAO generates its own prompts, responses, and preferences without external annotation ( Yin et al., 2026b ) , whereas PIKA uses an external generator and reward model to construct synthetic training data ( Yin et al., 2025 ) . Reflexion instead stores verbal feedback to guide later attempts without updating model parameters ( Shinn et al., 2023 ) , and subsequent work links verification, backtracking, and subgoal construction to successful self-improvement ( Gandhi et al., 2025 ) . SRCL follows this filtered self-training perspective but serves a different purpose: the current checkpoint rewrites its own on-policy response without seeing the verified solution, and training retains only rewrites that are shorter, naturally terminated, structurally valid, and answer-correct. SRCL therefore teaches concise successful solutions, complementing DCE’s guidance on how to revise the original response.

Test-time scaling improves accuracy by allocating more computation during inference. Repeated sampling, search, and compute-aware decoding trade additional inference compute for stronger performance ( Brown et al., 2024 ; Snell et al., 2025 ; Wu et al., 2025 ) , while input-adaptive methods allocate that compute according to estimated problem difficulty ( Damani et al., 2025 ) . Budget forcing specifically uses continuation cues to prevent early termination and extend a response to a prescribed budget ( Muennighoff et al., 2025 ) . SRCL instead changes the model during post-training so that a single rollout can preserve correct reasoning with fewer tokens. Our matched-budget controls therefore test whether the gains arise merely from longer generation or from the learned behavior.

## 3 Method

To address the limitations of a frozen privileged teacher while controlling the cost of increasingly long reasoning, our framework combines two complementary training objectives. Dynamic Co-Evolution (DCE) distills gold-conditioned guidance along the current student’s rollout and refreshes the detached privileged branch from the updated checkpoint each round. Self-Refined Concise Learning (SRCL) complements this signal by training on shorter, verified refinements of the same on-policy response. Their joint update produces the checkpoint used as both the student and privileged teacher in the next round, closing the recursive loop illustrated in fig. 2 .

### 3.1 Dynamic Co-Evolution

DCE alternates on-policy generation with updates to both the student and its privileged teacher. Let θ k \theta_{k} denote the model parameters at training round k k , with θ 0 \theta_{0} representing the initial checkpoint. Given a problem x x , the current model samples an on-policy response y ( k ) ∼ p θ k ( ⋅ ∣ x ) . y^{(k)}\sim p_{\theta_{k}}(\cdot\mid x). (2) From this response, we retain a sequence y ~ ( k ) = ( y ~ 1 ( k ) , … , y ~ m ( k ) ) \widetilde{y}^{(k)}=(\widetilde{y}^{(k)}_{1},\ldots,\widetilde{y}^{(k)}_{m}) of m m tokens on which the guidance objective is computed. At each token position t ∈ { 1 , … , m } t\in\{1,\ldots,m\} , the student and privileged teacher score the same response prefix y ~ < t ( k ) \widetilde{y}^{(k)}_{<t} . The student conditions on the problem x x and this prefix, whereas the privileged teacher additionally receives the ground-truth solution g g . Its prompt places the problem x x and task instruction in the user turn, followed in a single assistant turn by g g , a transition instruction τ \tau asking the model to solve the problem using its own approach, and finally y ~ < t ( k ) \widetilde{y}^{(k)}_{<t} . We denote this privileged context by 𝒞 t prev ​ ( x , g , τ , y ~ < t ( k ) ) \mathcal{C}_{t}^{\mathrm{prev}}(x,g,\tau,\widetilde{y}^{(k)}_{<t}) , i.e. the concatenation of all privileged inputs up to position t t . This ordering is deliberate: placing g g in the assistant turn lets the model condition on it as part of its own reasoning rather than as external user-provided material. The exact templates and alternative orderings are given in fig. 7 ; their performance is compared in section 5.7 .

We define the student and privileged-teacher next-token distributions at round k k and position t t as p k , t \displaystyle p_{k,t} : = p θ k ( ⋅ ∣ x , y ~ ( k ) < t ) , \displaystyle:=p_{\theta_{k}}\!\left(\cdot\mid x,\widetilde{y}^{(k)}_{<t}\right), (3) q k , t \displaystyle q_{k,t} : = stopgrad [ p θ k ( ⋅ ∣ 𝒞 t prev ( x , g , τ , y ~ ( k ) < t ) ) ] . \displaystyle:=\operatorname{stopgrad}\!\left[p_{\theta_{k}}\!\left(\cdot\mid\mathcal{C}_{t}^{\mathrm{prev}}(x,g,\tau,\widetilde{y}^{(k)}_{<t})\right)\right]. Here p k , t p_{k,t} is the student distribution, conditioned only on the problem, and q k , t q_{k,t} is the privileged-teacher distribution, which additionally sees the ground-truth solution. Both are produced by the same current checkpoint θ k \theta_{k} , but gradients are stopped through q k , t q_{k,t} . In contrast, standard OPSD differs in two ways: it presents the ground-truth solution as reference material in the user turn rather than as previously generated reasoning in the assistant turn, and it keeps the privileged teacher frozen at the initial checkpoint θ 0 \theta_{0} throughout training. Let Δ ⁡ ( q , p ) \Delta(q,p) denote a divergence measuring the mismatch between the teacher and student next-token distributions. DCE minimizes ℒ G ( k ) = 𝔼 ( x , g ) , y ( k ) ∼ p θ k ( ⋅ ∣ x ) [ 1 m ∑ t = 1 m Δ ( q k , t , p k , t ) ] . \mathcal{L}_{G}^{(k)}=\mathbb{E}_{(x,g),\,y^{(k)}\sim p_{\theta_{k}}(\cdot\mid x)}\!\left[\frac{1}{m}\sum_{t=1}^{m}\Delta\!\left(q_{k,t},p_{k,t}\right)\right]. (4) After optimizing this objective at round k k , the resulting parameters θ k + 1 \theta_{k+1} initialize both the student and privileged teacher for the next round. Consequently, revision behavior acquired during one round can become part of the gold-conditioned supervision provided in subsequent rounds, yielding recursive co-evolution. We use Forward KL for Δ \Delta in our main experiments and compare Reverse KL and JSD in section 5.5 .

### 3.2 Self-Refined Concise Learning

DCE improves reasoning by strengthening the model’s ability to revisit and revise its own trajectories. However, stronger revision behavior can also increase inference cost: the model may perform repeated checks, explore unnecessary branches, or continue reasoning after it has already reached a correct solution. DCE alone does not explicitly encourage the model to preserve useful reasoning while removing these redundant steps. We therefore introduce Self-Refined Concise Learning (SRCL) , which complements DCE by training the model on shorter, verified refinements of its own on-policy responses.

At training round k k , let ℬ = { ( x i , g i ) } \mathcal{B}=\{(x_{i},g_{i})\} denote a minibatch of problems x i x_{i} and their verified solutions g i g_{i} . For each example i i , the current checkpoint θ k \theta_{k} generates an on-policy response y i ( k ) y_{i}^{(k)} . SRCL then asks the same checkpoint to rewrite this response without access to g i g_{i} :

c i ( k ) = R θ k ​ ( x i , y i ( k ) ) , c_{i}^{(k)}=R_{\theta_{k}}\!\left(x_{i},y_{i}^{(k)}\right), (5) where R θ k R_{\theta_{k}} denotes generation under a refinement prompt that requests a direct, self-contained solution with unnecessary detours and reflection removed. We retain the refinement c i ( k ) c_{i}^{(k)} only if it is shorter than the original response y i ( k ) y_{i}^{(k)} , terminates naturally, satisfies structural validity requirements, and produces the correct answer. Let A i ( k ) ∈ { 0 , 1 } A_{i}^{(k)}\in\{0,1\} indicate whether c i ( k ) c_{i}^{(k)} passes all of these criteria; the exact acceptance rules are given in appendix M .

Each accepted refinement becomes a token-level supervised target. SRCL minimizes the autoregressive cross-entropy over all accepted tokens: ℒ SRCL ( k ) = − 1 N k ∑ i ∈ ℬ A i ( k ) ∑ t = 1 | c i ( k ) | log p θ k ( c i , t ( k ) ∣ x i , c i , < t ( k ) ) , N k = ∑ i ∈ ℬ A i ( k ) | c i ( k ) | . \mathcal{L}_{\mathrm{SRCL}}^{(k)}=-\frac{1}{N_{k}}\sum_{i\in\mathcal{B}}A_{i}^{(k)}\sum_{t=1}^{|c_{i}^{(k)}|}\log p_{\theta_{k}}\!\left(c_{i,t}^{(k)}\mid x_{i},c_{i,<t}^{(k)}\right),\qquad N_{k}=\sum_{i\in\mathcal{B}}A_{i}^{(k)}|c_{i}^{(k)}|. (6) Here, i i indexes examples in the minibatch and t t indexes tokens within an accepted refinement. If no refinement is accepted in a minibatch, such that N k = 0 N_{k}=0 , we omit the SRCL loss and update the model using DCE alone. Importantly, the verified solution g i g_{i} is used only to determine whether a refinement is accepted; it is never provided to the model when generating c i ( k ) c_{i}^{(k)} , preventing ground-truth leakage into the learned rewriting behavior. The exact refinement prompt, structural acceptance criteria, and answer-verifier implementation are provided in appendices M and N .

### 3.3 Joint Optimization

DCE and SRCL provide complementary supervision from the same on-policy response. DCE trains the model to follow the privileged teacher at prefixes encountered along the current rollout, whereas SRCL trains on shorter, verified refinements derived from that rollout. We combine the two objectives as ℒ DCE + SRCL ( k ) = λ G ​ ℒ G ( k ) ⏟ DCE guidance + λ S ​ ℒ SRCL ( k ) ⏟ SRCL target . \mathcal{L}_{\mathrm{DCE+SRCL}}^{(k)}=\underbrace{\lambda_{G}\mathcal{L}_{G}^{(k)}}_{\text{DCE guidance}}+\underbrace{\lambda_{S}\mathcal{L}_{\mathrm{SRCL}}^{(k)}}_{\text{SRCL target}}. (7) Here, ℒ G ( k ) \mathcal{L}_{G}^{(k)} is the dynamic guidance loss defined in eq. 4 , and ℒ SRCL ( k ) \mathcal{L}_{\mathrm{SRCL}}^{(k)} is the self-refinement loss defined in eq. 6 . The coefficients λ G \lambda_{G} and λ S \lambda_{S} control the relative contribution of the two objectives; their empirical sensitivity is studied in section 5.4 . The complete recursive procedure is summarized in algorithm 1 .

## 4 Experimental Setup

### 4.1 Models, Data, and Metrics

We adopt Qwen3-1.7B, Qwen3-4B, Qwen3-8B, and Qwen3-14B ( Qwen Team, 2025 ) as our primary model family, and Gemma-4-12B-IT in the cross-family study in section 5.2 . Both the problem-only student and gold-conditioned privileged teacher operate in non-thinking mode. All methods use the same 14,717 problems drawn from the OpenThoughts mathematical-reasoning data adopted by OPSD ( Guha et al., 2025 ; Zhao et al., 2026 ) . DCE constructs student and privileged views of each problem during training. Complete configurations are reported in table 24 .

Evaluation uses all 30 problems from each of AIME 2024, AIME 2025, AIME 2026 ( Mathematical Association of America, 2026 ) , and HMMT February 2025 ( Harvard–MIT Mathematics Tournament, 2026 ) . We sample 12 responses per problem with a 32K generation cap, temperature 1.0, top- p = 0.8 p=0.8 , top- k = − 1 k=-1 , and repetition penalty 1.0.

### 4.2 Baselines and Controls

We compare against four training baselines: Base , SFT , GRPO , and OPSD . Base is the original model evaluated in non-thinking mode. SFT trains on the problem–solution pairs ( x , g ) (x,g) using autoregressive cross-entropy, while GRPO optimizes an outcome reward based on final-answer correctness. OPSD is our closest training baseline: it distills next-token predictions from a frozen, gold-conditioned privileged teacher initialized from the same base checkpoint.

To separate the effect of improved training from that of simply allocating more inference tokens, we additionally include OPSD-TTS as an inference-time control. Following the extended-thinking intervention of Ghosal et al. (2025) , when an OPSD response terminates before the target budget, a Wait cue resumes generation until the response reaches an exact 8K or 16K token budget. OPSD-TTS does not modify the model parameters and therefore tests whether longer generation alone can account for the gains of DCE+SRCL.

### 4.3 Training Protocol

Across the Qwen3 DCE experiments, we train with AdamW ( Loshchilov and Hutter, 2019 ) in bfloat16 using a learning rate of 5 × 10 − 6 5\times 10^{-6} and rank-128 LoRA ( Hu et al., 2022 ) . Each training example produces a single on-policy response. DCE computes privileged-teacher guidance over the retained response tokens, while SRCL greedily rewrites the same response and trains only on accepted targets that are shorter, reflection-free, and answer-correct.

We set the DCE loss weight to λ DCE = 5 × 10 4 \lambda_{\mathrm{DCE}}=5\times 10^{4} for all Qwen3 models. For SRCL, we use λ SRCL = 12.5 , 25 , 35 , \lambda_{\mathrm{SRCL}}=12.5,25,35, and 25 25 for Qwen3-14B, 8B, 4B, and 1.7B, respectively. Sensitivity to both coefficients is analyzed in section 5.4 . We evaluate checkpoints at training steps { 10 , 20 , 30 , 50 , 100 , 150 , 200 } \{10,20,30,50,100,150,200\} when available.

Baseline-specific SFT and GRPO hyperparameters are reported in table 24 , and checkpoint-level learning trajectories are provided in figs. 3 and C . The Gemma transfer configuration is reported separately in appendix B .

## 5 Results

### 5.1 Main Experimental Results

Table 1 summarizes the main results. DCE substantially improves over the training baselines across model scales. For Qwen3-8B, DCE+SRCL reaches 65.97% Average@12, compared with 30.35% for OPSD and 20.28% for GRPO. The gains remain substantial with Qwen3-4B, where DCE+SRCL reaches 61.88%, compared with 22.85% for OPSD and 18.47% for GRPO. DCE alone achieves similar accuracy with Qwen3-8B (65.76%) and reaches 60.00% with Qwen3-4B, indicating that the primary accuracy gains come from dynamic co-evolution.

SRCL improves the accuracy–length tradeoff at these scales. With Qwen3-8B, adding SRCL reduces mean output length from 19,046 to 17,561 tokens while maintaining comparable Average@12 accuracy (65.76% versus 65.97%). With Qwen3-4B, SRCL both improves accuracy from 60.00% to 61.88% and reduces mean output length from 19,360 to 17,265 tokens, a 10.82% reduction. This effect is not uniform at the smallest scale: with Qwen3-1.7B, DCE+SRCL improves Average@12 from 23.33% to 26.88%, but also increases mean output length from 12,600 to 19,504 tokens.

Longer inference alone does not explain the gains. Forcing OPSD to generate exactly 16K tokens yields only 30.76%, 22.99%, and 9.24% Average@12 for Qwen3-8B, Qwen3-4B, and Qwen3-1.7B, respectively. The matched training trajectories in fig. 3 further separate the effect of SRCL from checkpoint selection: at step 100 with Qwen3-8B, DCE+SRCL reaches 65.97% with 17,561 mean tokens, compared with 64.93% and 19,036 tokens for DCE at the same step. With Qwen3-4B, DCE peaks earlier and declines after step 50, whereas DCE+SRCL remains near 61% through step 200. Complete checkpoint trajectories and budget controls are provided in appendices C , F , 5.8 and 23 .

\FloatBarrier

### 5.2 Does Recursive Improvement Transfer Beyond Qwen3?

To test whether recursive improvement transfers across model families, we apply our framework to Gemma-4-12B-IT. As shown in table 2 , DCE and DCE+SRCL reach 62.01% and 63.61% Average@12, respectively, outperforming all non-DCE comparisons. SRCL adds 1.60 percentage points while reducing mean output length from 8,812 to 8,526 tokens. Across the saved trajectory, DCE+SRCL attains higher accuracy at five of seven checkpoints, ties once, and is both more accurate and shorter than DCE at four checkpoints. The framework therefore transfers beyond Qwen3. Detailed configurations and complete training trajectories appear in appendix B .

\FloatBarrier

### 5.3 What Happens During Recursive Self-Improvement?

To characterize recursive self-improvement, we evaluate checkpoints from a Qwen3-8B DCE+SRCL run on a fixed set of incorrect trajectories. Holding the trajectories constant isolates two next-token behaviors: whether the model terminates after a wrong solution, and whether it predicts the reflection cue observed when the solution begins to revise.

For a stored response y i − y_{i}^{-} with its terminal EOS removed, the Student scores [ x i ; y i − ] [x_{i};y_{i}^{-}] , while the Teacher scores the same response with the verified solution prepended. At an observed revision point t t , we instead score the preceding prefix and its actual next cue r i , t r_{i,t} , such as Wait . Denote the resulting endpoint and revision contexts by c end c^{\mathrm{end}} and c ref c^{\mathrm{ref}} . For branch b ∈ { S , T } b\in\{S,T\} , the two probes are P b ( k ) ​ ( EOS ) = 1 | ℰ | ​ ∑ i ∈ ℰ p θ k ​ ( EOS ∣ c i , b end ) , P b ( k ) ​ ( r ) = 1 | 𝒲 | ​ ∑ ( i , t ) ∈ 𝒲 p θ k ​ ( r i , t ∣ c i , t , b ref ) . P_{b}^{(k)}(\mathrm{EOS})=\frac{1}{|\mathcal{E}|}\sum_{i\in\mathcal{E}}p_{\theta_{k}}(\mathrm{EOS}\mid c^{\mathrm{end}}_{i,b}),\qquad P_{b}^{(k)}(r)=\frac{1}{|\mathcal{W}|}\sum_{(i,t)\in\mathcal{W}}p_{\theta_{k}}(r_{i,t}\mid c^{\mathrm{ref}}_{i,t,b}). (8) Both values come directly from the full next-token distribution. The reflection probe scores the cue actually present in the stored trajectory rather than summing over a hand-built lexicon.

Figure 4 shows the same qualitative transition on all three benchmarks. Macro-averaged across the cohorts, Student/Teacher endpoint p ⁡ ( EOS ) p(\mathrm{EOS}) falls from 92.6%/90.4% at initialization to 26.3%/41.3% at step 200. Over the same interval, p ⁡ ( r t ) p(r_{t}) rises from 30.1%/32.8% to 77.0%/77.4%, with most of the increase occurring by steps 50–100. Recursive training therefore changes not only the student policy but also the privileged branch used to supervise the next round: both become less likely to stop after a wrong solution and more likely to support the observed reflection cue. This shared shift suggests that co-evolution transfers emerging revision behavior into the privileged teacher, complementing the frozen-teacher evidence in fig. 1 ; complete AIME26 probe values are reported in table 20 .

\FloatBarrier

### 5.4 How Do Different Loss Weights Affect Performance?

To explore the distinct roles of the two training objectives, we vary their coefficients separately on Qwen3-8B. The DCE weight λ G \lambda_{G} controls the strength of privileged next-token guidance, whereas the SRCL weight λ S \lambda_{S} controls the contribution of accepted concise rewrites. In each sweep, the other coefficient and all remaining training and evaluation settings are fixed. Table 3 reports the resulting task accuracy and output length for each setting.

Both sweeps identify a broad but non-monotonic operating region. Across the tested λ G \lambda_{G} range, Average accuracy varies only from 63.96% to 65.97%; λ G = 5 × 10 4 \lambda_{G}=5\times 10^{4} gives both the highest Average and the lowest mean length, although 1 × 10 4 1\times 10^{4} is stronger on AIME24 and HMMT25. For SRCL, λ S = 25 \lambda_{S}=25 likewise gives the highest Average, 65.97%, while the other settings remain within 2.57 points despite spanning a forty-fold range. These results indicate local robustness, not a monotonic or scale-independent optimum; the corresponding 4B sweep is reported in table 25 . They also clarify that the objectives are complementary: when DCE is removed, SRCL alone collapses to 2.36%/1,116 tokens at 8B and 0.76%/531 tokens at 4B. Concise self-refinement therefore improves the frontier only when paired with dynamic guidance that develops the underlying revision capability.

### 5.5 How Does the Guidance Objective Influence Performance?

To examine how the direction of distillation affects recursive improvement, we compare the best observed Qwen3-8B DCE+SRCL runs using Forward KL D KL ( q ∥ p ) D_{\mathrm{KL}}(q\|p) , Reverse KL D KL ( p ∥ q ) D_{\mathrm{KL}}(p\|q) , and JSD 1 2 D KL ( q ∥ m ) + 1 2 D KL ( p ∥ m ) \tfrac{1}{2}D_{\mathrm{KL}}(q\|m)+\tfrac{1}{2}D_{\mathrm{KL}}(p\|m) , where m = ( q + p ) / 2 m=(q+p)/2 , under the same evaluation protocol.

The results reflect the asymmetry of the three objectives. Forward KL weights discrepancies by the teacher distribution, preserving a strong signal for corrections that the student underweights.

Reverse KL instead weights the mismatch by the student distribution; corrections that the student rarely considers contribute less, favoring its existing modes over missing teacher-supported alternatives. JSD is symmetric and bounded, which can further weaken directional transfer when the two distributions differ substantially. Consistent with this interpretation, Forward KL reaches 65.97% with 17,561 tokens, whereas Reverse KL is 5.55 percentage points lower while using 6,187 more tokens. JSD reaches only 17.99% with 3,767 tokens, suggesting premature shortening rather than useful concision. Forward KL is therefore the most effective of the tested objectives for transferring privileged revision guidance.

\FloatBarrier

### 5.6 Does the Privileged Teacher Need to Co-Evolve?

To isolate the role of teacher refresh, we compare co-evolving and frozen gold-conditioned teachers under the same on-policy pipeline, both with and without SRCL. Figure 5 summarizes the accuracy–length comparison; complete trajectories and task-level results appear in appendices D , 6 and 13 .

Co-evolution improves both configurations. At 8B and 4B, DCE reaches 65.76% and 60.00%, versus 47.99% and 25.28% when frozen; DCE+SRCL reaches 65.97% and 61.88%, versus 41.04% and 27.29%. The shorter frozen runs incur large accuracy losses and regress after brief initial gains, indicating premature termination. Continual refresh instead sustains emerging revision behavior and keeps gold-conditioned guidance aligned with the evolving model.

\FloatBarrier

### 5.7 Which Representation of the Verified Solution Works Better?

Beyond teacher refresh, privileged-solution placement also affects signal quality. Assistant-side prefill places the solution in preceding model-generated context, whereas user-side instruction-last treats it as external material. Holding all else fixed, assistant-side prefill improves Average by 9.79, 6.39, and 14.66 points at 8B, 4B, and 1.7B and is 780 tokens shorter at 8B ( table 5 ). A matched 8B probe localizes its strongest effect near the start of Y 0 Y_{0} , whereas user-side effects persist later ( table 17 ), consistent with route initialization. Placement alone is insufficient: reference-last performs better under a frozen teacher ( table 16 ). The best result combines assistant-side conditioning with continual refresh; fig. 7 gives the exact prompt orderings.

\FloatBarrier

### 5.8 How Does the Method Perform under Tight Reasoning Budgets?

A practical question is whether the learned revision behavior remains useful under tight reasoning budgets. We therefore evaluate Qwen3-8B with total output budgets of 8K and 16K using three inference-only controls. Truncate directly cuts the response generated under the original 32K setting at the target budget. Cue first generates 7K tokens for an 8K budget (14K for 16K), appends a short instruction to continue reasoning, and generates the remainder within the same total cap. TTS adapts the test-time-scaling continuation procedure of Ghosal et al. (2025) : when an OPSD response ends early, it appends a Wait cue and continues until the output reaches the exact target length. These controls modify decoding only; model parameters remain fixed.

Table 6 shows that simply forcing more tokens is ineffective: at 8K, TTS lowers OPSD from 29.17% to 28.47% while nearly doubling output length, and at 16K it gains only 0.48 points while adding 11,275 tokens. Cue, by contrast, improves every matched DCE setting while slightly reducing mean output. At 8K, DCE rises from 24.38% to 31.04% and DCE+SRCL from 28.54% to 35.07%; at 16K, the corresponding gains are 48.68% to 55.76% and 52.01% to 57.64%. Thus the learned revision behavior remains useful under tight budgets, whereas length alone does not explain the gain. Complete TTS results across model sizes appear in table 23 .

### 5.9 How Sensitive Is Performance to Decoding Hyperparameters?

(a) Temperature sweep ( ρ = 1.0 \rho=1.0 )

(b) Repetition-penalty sweep ( T = 1.0 T=1.0 )

Finally, we test sensitivity to two common decoding choices under the non-thinking, 32K, Average@12 protocol. Table 7 shows that the default T = 1.0 T=1.0 gives the best Average among the tested temperatures (65.97%/17,561 tokens), while ρ = 1.08 \rho=1.08 is locally best among the tested repetition penalties (67.15%/17,173), gaining 1.18 points with 388 fewer tokens. We retain default decoding for the main comparisons and report the repetition-penalty result as a decoding-sensitivity analysis.

## 6 Conclusion

We presented Dynamic Co-Evolution (DCE), which makes privileged self-distillation recursive: every updated checkpoint becomes the next student and the next detached teacher, so revision learned in one round shapes the next round’s supervision. Self-Refined Concise Learning (SRCL) complements it with shorter, answer-verified rewrites of the model’s own responses; together, they deliver stronger and more token-efficient recursive self-improvement across model scales.

## References

Agarwal et al. (2024) Rishabh Agarwal, Nino Vieillard, Yongchao Zhou, Piotr Stanczyk, Sabela Ramos Garea, Matthieu Geist, and Olivier Bachem. On-policy distillation of language models: Learning from self-generated mistakes. In The Twelfth International Conference on Learning Representations, ICLR 2024, Vienna, Austria, May 7-11, 2024 . OpenReview.net, 2024. https://openreview.net/forum?id=3zKtaqxLhW .

Brown et al. (2024) Bradley C. A. Brown, Jordan Juravsky, Ryan Ehrlich, Ronald Clark, Quoc V. Le, Christopher Ré, and Azalia Mirhoseini. Large language monkeys: Scaling inference compute with repeated sampling. CoRR , abs/2407.21787, 2024. 10.48550/ARXIV.2407.21787 . https://doi.org/10.48550/arXiv.2407.21787 .

Damani et al. (2025) Mehul Damani, Idan Shenfeld, Andi Peng, Andreea Bobu, and Jacob Andreas. Learning how hard to think: Input-adaptive allocation of LM computation. In The Thirteenth International Conference on Learning Representations, ICLR 2025, Singapore, April 24-28, 2025 . OpenReview.net, 2025. https://openreview.net/forum?id=6qUUgw9bAZ .

Firooz et al. (2025) Hamed Firooz, Rui Liu, Yuchen Lu, Zhenyu Hou, Fangzhou Xiong, Xiaoyang Zhang, Changshu Jian, Zhicheng Zhu, Jiayuan Ma, Jacob Tao, et al. Scaling reinforcement learning for content moderation with large language models. CoRR , abs/2512.20061, 2025. 10.48550/ARXIV.2512.20061 . https://doi.org/10.48550/arXiv.2512.20061 .

Gandhi et al. (2025) Kanishk Gandhi, Ayush Chakravarthy, Anikait Singh, Nathan Lile, and Noah D. Goodman. Cognitive behaviors that enable self-improving reasoners, or, four habits of highly effective stars. CoRR , abs/2503.01307, 2025. 10.48550/ARXIV.2503.01307 . https://doi.org/10.48550/arXiv.2503.01307 .

Ghosal et al. (2025) Soumya Suvra Ghosal, Souradip Chakraborty, Avinash Reddy, Yifu Lu, Mengdi Wang, Dinesh Manocha, Furong Huang, Mohammad Ghavamzadeh, and Amrit Singh Bedi. Does thinking more always help? mirage of test-time scaling in reasoning models. In Danielle Belgrave, Cheng Zhang, Laura N. Montoya, Hsuan-Tien Lin, Razvan Pascanu, Piotr Koniusz, Marzyeh Ghassemi, Nancy Chen, Iván Vladimir Meza Ruíz, and Arturo Loaiza-Bonilla, editors, Advances in Neural Information Processing Systems 38: Annual Conference on Neural Information Processing Systems 2025, NeurIPS 2025, San Diego, CA, USA, December 2-7, 2025 / Mexico City, Mexico, November 30 - December 5, 2025 , 2025. http://papers.nips.cc/paper_files/paper/2025/hash/fc067ac218430c409d6f65403328f740-Abstract-Conference.html .

Guha et al. (2025) Etash Kumar Guha, Ryan Marten, Sedrick Keh, Negin Raoof, Georgios Smyrnis, Hritik Bansal, Marianna Nezhurina, Jean Mercat, Trung Vu, Zayne Sprague, et al. Openthoughts: Data recipes for reasoning models. CoRR , abs/2506.04178, 2025. 10.48550/ARXIV.2506.04178 . https://doi.org/10.48550/arXiv.2506.04178 .

Gülçehre et al. (2023) Çaglar Gülçehre, Tom Le Paine, Srivatsan Srinivasan, Ksenia Konyushkova, Lotte Weerts, Abhishek Sharma, Aditya Siddhant, Alex Ahern, Miaosen Wang, Chenjie Gu, et al. Reinforced self-training (rest) for language modeling. CoRR , abs/2308.08998, 2023. 10.48550/ARXIV.2308.08998 . https://doi.org/10.48550/arXiv.2308.08998 .

Guo et al. (2025) Daya Guo, Dejian Yang, Haowei Zhang, Junxiao Song, Peiyi Wang, Qihao Zhu, Runxin Xu, Ruoyu Zhang, Shirong Ma, Xiao Bi, et al. Deepseek-r1 incentivizes reasoning in llms through reinforcement learning. Nat. , 645(8081):633–638, 2025. 10.1038/S41586-025-09422-Z . https://doi.org/10.1038/s41586-025-09422-z .

Harvard–MIT Mathematics Tournament (2026) Harvard–MIT Mathematics Tournament. Past tournaments, 2026. https://www.hmmt.org/www/archive/problems . Accessed August 26, 2026.

Hendrycks et al. (2021) Dan Hendrycks, Collin Burns, Saurav Kadavath, Akul Arora, Steven Basart, Eric Tang, Dawn Song, and Jacob Steinhardt. Measuring mathematical problem solving with the MATH dataset. In Joaquin Vanschoren and Sai-Kit Yeung, editors, Proceedings of the Neural Information Processing Systems Track on Datasets and Benchmarks 1, NeurIPS Datasets and Benchmarks 2021, December 2021, virtual , 2021. https://datasets-benchmarks-proceedings.neurips.cc/paper/2021/hash/be83ab3ecd0db773eb2dc1b0a17836a1-Abstract-round2.html .

Hu et al. (2022) Edward J. Hu, Yelong Shen, Phillip Wallis, Zeyuan Allen-Zhu, Yuanzhi Li, Shean Wang, Lu Wang, and Weizhu Chen. Lora: Low-rank adaptation of large language models. In The Tenth International Conference on Learning Representations, ICLR 2022, Virtual Event, April 25-29, 2022 . OpenReview.net, 2022. https://openreview.net/forum?id=nZeVKeeFYf9 .

Huang et al. (2024) Jie Huang, Xinyun Chen, Swaroop Mishra, Huaixiu Steven Zheng, Adams Wei Yu, Xinying Song, and Denny Zhou. Large language models cannot self-correct reasoning yet. In The Twelfth International Conference on Learning Representations, ICLR 2024, Vienna, Austria, May 7-11, 2024 . OpenReview.net, 2024. https://openreview.net/forum?id=IkmD3fKBPQ .

Lee et al. (2025) Andrew Lee, Lihao Sun, Chris Wendler, Fernanda B. Viégas, and Martin Wattenberg. The geometry of self-verification in a task-specific reasoning model. CoRR , abs/2504.14379, 2025. 10.48550/ARXIV.2504.14379 . https://doi.org/10.48550/arXiv.2504.14379 .

Lightman et al. (2024) Hunter Lightman, Vineet Kosaraju, Yuri Burda, Harrison Edwards, Bowen Baker, Teddy Lee, Jan Leike, John Schulman, Ilya Sutskever, and Karl Cobbe. Let’s verify step by step. In The Twelfth International Conference on Learning Representations, ICLR 2024, Vienna, Austria, May 7-11, 2024 . OpenReview.net, 2024. https://openreview.net/forum?id=v8L0pN6EOi .

Liu et al. (2025) Zichen Liu, Changyu Chen, Wenjun Li, Penghui Qi, Tianyu Pang, Chao Du, Wee Sun Lee, and Min Lin. Understanding r1-zero-like training: A critical perspective. CoRR , abs/2503.20783, 2025. 10.48550/ARXIV.2503.20783 . https://doi.org/10.48550/arXiv.2503.20783 .

Loshchilov and Hutter (2019) Ilya Loshchilov and Frank Hutter. Decoupled weight decay regularization. In 7th International Conference on Learning Representations, ICLR 2019, New Orleans, LA, USA, May 6-9, 2019 . OpenReview.net, 2019. https://openreview.net/forum?id=Bkg6RiCqY7 .

Lu and Lab (2025) Kevin Lu and Thinking Machines Lab. On-policy distillation. Thinking Machines Lab: Connectionism , 2025. 10.64434/tml.20251026 . https://thinkingmachines.ai/blog/on-policy-distillation.

Mathematical Association of America (2026) Mathematical Association of America. MAA invitational competitions, 2026. https://maa.org/maa-invitational-competitions/ . Accessed August 26, 2026.

Muennighoff et al. (2025) Niklas Muennighoff, Zitong Yang, Weijia Shi, Xiang Lisa Li, Li Fei-Fei, Hannaneh Hajishirzi, Luke Zettlemoyer, Percy Liang, Emmanuel J. Candès, and Tatsunori Hashimoto. s1: Simple test-time scaling. In Christos Christodoulopoulos, Tanmoy Chakraborty, Carolyn Rose, and Violet Peng, editors, Proceedings of the 2025 Conference on Empirical Methods in Natural Language Processing, EMNLP 2025, Suzhou, China, November 4-9, 2025 , pages 20275–20321. Association for Computational Linguistics, 2025. 10.18653/V1/2025.EMNLP-MAIN.1025 . https://doi.org/10.18653/v1/2025.emnlp-main.1025 .

Pan et al. (2026) Leyi Pan, Shuchang Tao, Yunpeng Zhai, Lingzhe Zhang, Zhaoyang Liu, Bolin Ding, Aiwei Liu, and Lijie Wen. RLCSD: reinforcement learning with contrastive on-policy self-distillation. CoRR , abs/2606.11709, 2026. 10.48550/ARXIV.2606.11709 . https://doi.org/10.48550/arXiv.2606.11709 .

Qwen Team (2025) Qwen Team. Qwen3 technical report. CoRR , abs/2505.09388, 2025. 10.48550/ARXIV.2505.09388 . https://doi.org/10.48550/arXiv.2505.09388 .

Rein et al. (2023) David Rein, Betty Li Hou, Asa Cooper Stickland, Jackson Petty, Richard Yuanzhe Pang, Julien Dirani, Julian Michael, and Samuel R. Bowman. GPQA: A graduate-level google-proof q&a benchmark. CoRR , abs/2311.12022, 2023. 10.48550/ARXIV.2311.12022 . https://doi.org/10.48550/arXiv.2311.12022 .

Shao et al. (2024) Zhihong Shao, Peiyi Wang, Qihao Zhu, Runxin Xu, Junxiao Song, Xiao Bi, Haowei Zhang, Mingchuan Zhang, Y. K. Li, Y. Wu, et al. Deepseekmath: Pushing the limits of mathematical reasoning in open language models. CoRR , abs/2402.03300, 2024. 10.48550/ARXIV.2402.03300 . https://doi.org/10.48550/arXiv.2402.03300 .

Shinn et al. (2023) Noah Shinn, Federico Cassano, Ashwin Gopinath, Karthik Narasimhan, and Shunyu Yao. Reflexion: language agents with verbal reinforcement learning. In Alice Oh, Tristan Naumann, Amir Globerson, Kate Saenko, Moritz Hardt, and Sergey Levine, editors, Advances in Neural Information Processing Systems 36: Annual Conference on Neural Information Processing Systems 2023, NeurIPS 2023, New Orleans, LA, USA, December 10 - 16, 2023 , 2023. http://papers.nips.cc/paper_files/paper/2023/hash/1b44b878bb782e6954cd888628510e90-Abstract-Conference.html .

Snell et al. (2025) Charlie Victor Snell, Jaehoon Lee, Kelvin Xu, and Aviral Kumar. Scaling LLM test-time compute optimally can be more effective than scaling parameters for reasoning. In The Thirteenth International Conference on Learning Representations, ICLR 2025, Singapore, April 24-28, 2025 . OpenReview.net, 2025. https://openreview.net/forum?id=4FWAwZtd2n .

Wang et al. (2025) Chenlong Wang, Yuanning Feng, Dongping Chen, Zhaoyang Chu, Ranjay Krishna, and Tianyi Zhou. Wait, we don’t need to ”wait”! removing thinking tokens improves reasoning efficiency. In Christos Christodoulopoulos, Tanmoy Chakraborty, Carolyn Rose, and Violet Peng, editors, Findings of the Association for Computational Linguistics: EMNLP 2025, Suzhou, China, November 4-9, 2025 , pages 7459–7482. Association for Computational Linguistics, 2025. 10.18653/V1/2025.FINDINGS-EMNLP.394 . https://doi.org/10.18653/v1/2025.findings-emnlp.394 .

Wu et al. (2025) Yangzhen Wu, Zhiqing Sun, Shanda Li, Sean Welleck, and Yiming Yang. Inference scaling laws: An empirical analysis of compute-optimal inference for LLM problem-solving. In The Thirteenth International Conference on Learning Representations, ICLR 2025, Singapore, April 24-28, 2025 . OpenReview.net, 2025. https://openreview.net/forum?id=VNckp7JEHn .

Yang et al. (2026) Chenxu Yang, Chuanyu Qin, Qingyi Si, Minghui Chen, Naibin Gu, Dingyu Yao, Zheng Lin, Weiping Wang, Jiaqi Wang, and Nan Duan. Self-distilled RLVR. CoRR , abs/2604.03128, 2026. 10.48550/ARXIV.2604.03128 . https://doi.org/10.48550/arXiv.2604.03128 .

Yin and Shi (2026) Shangjian Yin and Zhouxing Shi. From individual to common: An early exploration of consensus in non-verifiable data for balanced preference optimization. In Proceedings of the 64th Annual Meeting of the Association for Computational Linguistics (Volume 1: Long Papers) , pages 34612–34630. Association for Computational Linguistics, 2026. 10.18653/v1/2026.acl-long.1598 . https://aclanthology.org/2026.acl-long.1598/ .

Yin et al. (2025) Shangjian Yin, Shining Liang, Wenbiao Ding, Yuli Qian, Zhouxing Shi, Hongzhi Li, and Yutao Xie. PIKA: Expert-level synthetic datasets for post-training alignment from scratch. CoRR , abs/2510.06670, 2025. 10.48550/ARXIV.2510.06670 . https://arxiv.org/abs/2510.06670 .

Yin et al. (2026a) Shangjian Yin, Yu Fu, Yue Dong, and Zhouxing Shi. GRLO: Towards generalizable reinforcement learning in open-ended environments from zero. CoRR , abs/2605.15464, 2026a. 10.48550/ARXIV.2605.15464 . https://arxiv.org/abs/2605.15464 .

Yin et al. (2026b) Shangjian Yin, Zhepei Wei, Xinyu Zhu, Wei-Lin Chen, and Yu Meng. Aligning large language models via fully self-synthetic data. In Proceedings of the 64th Annual Meeting of the Association for Computational Linguistics (Volume 1: Long Papers) , pages 34553–34568. Association for Computational Linguistics, 2026b. 10.18653/v1/2026.acl-long.1595 . https://aclanthology.org/2026.acl-long.1595/ .

Yu et al. (2025) Qiying Yu, Zheng Zhang, Ruofei Zhu, Yufeng Yuan, Xiaochen Zuo, Yu Yue, Weinan Dai, Tiantian Fan, Gaohong Liu, Juncai Liu, et al. DAPO: an open-source LLM reinforcement learning system at scale. In Danielle Belgrave, Cheng Zhang, Laura N. Montoya, Hsuan-Tien Lin, Razvan Pascanu, Piotr Koniusz, Marzyeh Ghassemi, Nancy Chen, Iván Vladimir Meza Ruíz, and Arturo Loaiza-Bonilla, editors, Advances in Neural Information Processing Systems 38: Annual Conference on Neural Information Processing Systems 2025, NeurIPS 2025, San Diego, CA, USA, December 2-7, 2025 / Mexico City, Mexico, November 30 - December 5, 2025 , 2025. http://papers.nips.cc/paper_files/paper/2025/hash/a4277440d50f1f15d2cb4c14f7e0c0d2-Abstract-Conference.html .

Zelikman et al. (2022) Eric Zelikman, Yuhuai Wu, Jesse Mu, and Noah D. Goodman. Star: Bootstrapping reasoning with reasoning. In Sanmi Koyejo, S. Mohamed, A. Agarwal, Danielle Belgrave, K. Cho, and A. Oh, editors, Advances in Neural Information Processing Systems 35: Annual Conference on Neural Information Processing Systems 2022, NeurIPS 2022, New Orleans, LA, USA, November 28 - December 9, 2022 , 2022. http://papers.nips.cc/paper_files/paper/2022/hash/639a9a172c044fbb64175b5fad42e9a5-Abstract-Conference.html .

Zeng et al. (2025) Weihao Zeng, Yuzhen Huang, Qian Liu, Wei Liu, Keqing He, Zejun Ma, and Junxian He. Simplerl-zoo: Investigating and taming zero reinforcement learning for open base models in the wild. CoRR , abs/2503.18892, 2025. 10.48550/ARXIV.2503.18892 . https://doi.org/10.48550/arXiv.2503.18892 .

Zhang et al. (2025a) Anqi Zhang, Yulin Chen, Jane Pan, Chen Zhao, Aurojit Panda, Jinyang Li, and He He. Reasoning models know when they’re right: Probing hidden states for self-verification. CoRR , abs/2504.05419, 2025a. 10.48550/ARXIV.2504.05419 . https://doi.org/10.48550/arXiv.2504.05419 .

Zhang et al. (2025b) Zhenru Zhang, Chujie Zheng, Yangzhen Wu, Beichen Zhang, Runji Lin, Bowen Yu, Dayiheng Liu, Jingren Zhou, and Junyang Lin. The lessons of developing process reward models in mathematical reasoning. In Wanxiang Che, Joyce Nabende, Ekaterina Shutova, and Mohammad Taher Pilehvar, editors, Findings of the Association for Computational Linguistics, ACL 2025, Vienna, Austria, July 27 - August 1, 2025 , volume ACL 2025 of Findings of ACL , pages 10495–10516. Association for Computational Linguistics, 2025b. 10.18653/V1/2025.FINDINGS-ACL.547 . https://doi.org/10.18653/v1/2025.findings-acl.547 .

Zhao et al. (2026) Siyan Zhao, Zhihui Xie, Mengchen Liu, Jing Huang, Guan Pang, Feiyu Chen, and Aditya Grover. Self-distilled reasoner: On-policy self-distillation for large language models. CoRR , abs/2601.18734, 2026. 10.48550/ARXIV.2601.18734 . https://doi.org/10.48550/arXiv.2601.18734 .

Zhu et al. (2025) Xudong Zhu, Jiachen Jiang, Mohammad Mahdi Khalili, and Zhihui Zhu. From emergence to control: Probing and modulating self-reflection in language models. CoRR , abs/2506.12217, 2025. 10.48550/ARXIV.2506.12217 . https://doi.org/10.48550/arXiv.2506.12217 .

## Appendix A Does Recursive Improvement Scale to a Larger Model?

To explore whether recursive improvement extends to a larger model, we train Qwen3-14B with the same DCE+SRCL framework and track its early trajectory in table 8 . Average accuracy rises from 21.39% at initialization to 42.64% at step 20 and 66.39% at step 30, a total gain of 45.00 percentage points. The improvement spans all four benchmarks and is largest on AIME26, which rises by 50.28 percentage points, from 19.44% to 69.72%. Step 50 retains a comparable 65.21%, although mean output grows from 15,877 to 20,050 tokens. These results show strong round-to-round improvement at 14B while indicating that early stopping remains important for preserving the accuracy–length frontier.

## Appendix B Gemma-4-12B-IT Training Details and Additional Results

The cross-family comparison appears in table 2 . The exact model ID is google/gemma-4-12B-it . The matched DCE runs use the same 14,717-problem OPSD shard, assistant-side privileged conditioning, non-thinking student and teacher branches, and 200-step LoRA training with seed 42 (rank 128, alpha 256, global batch 16, and learning rate 2.5 × 10 − 6 2.5\times 10^{-6} ). Their only objective-level difference is λ S = 0 \lambda_{S}=0 for DCE and λ S = 25 \lambda_{S}=25 for DCE+SRCL, with λ G = 5 × 10 4 \lambda_{G}=5\times 10^{4} in both.

Placement also matters on Gemma-4-12B-IT. Assistant-side conditioning reaches 63.61% Average@12, compared with 55.76% for user-side reference-last and 54.31% for user-side instruction-last ( table 9 ). Both user-side variants attain their best observed result at step 10, whereas the assistant-side run continues improving through step 100.

## Appendix C Complete Qwen3-8B and Qwen3-4B Trajectories

Tables 11 and 12 report checkpoint-wise Average@12 accuracy and mean output length for Qwen3-8B and Qwen3-4B, complementing the learning curves in fig. 3 . Missing entries denote unevaluated checkpoints. The GRPO columns show the available trajectories, while table 1 reports the tuned baseline comparison.

SRCL without DCE collapses to short, mostly incorrect responses: Qwen3-8B reaches at most 2.36% with 1,116 tokens, and Qwen3-4B reaches 0.76% with 531 tokens. SRCL therefore acts as a concision objective only when paired with dynamic guidance.

\FloatBarrier

## Appendix D Teacher-Update Schedules

We isolate the effect of teacher refresh by comparing frozen, exponential-moving-average (EMA), periodic-snapshot, and fully dynamic teachers under the same Qwen3-8B setup. For EMA, the teacher after optimizer step t t is θ T ( t ) = d ​ θ T ( t − 1 ) + ( 1 − d ) ​ θ S ( t ) , \theta_{T}^{(t)}=d\,\theta_{T}^{(t-1)}+(1-d)\,\theta_{S}^{(t)}, (9) where a smaller decay d d follows the student more closely. Periodic refresh instead copies the current student into the teacher every m m optimizer steps and keeps the teacher fixed between updates. The frozen teacher is never refreshed, while the dynamic teacher is synchronized at every step. Table 13 summarizes task-level performance, while tables 14 and 15 give the complete Average@12 trajectories.

Every refresh strategy substantially improves over the frozen teacher. EMA d = 0.3 d=0.3 reaches the highest EMA accuracy at 65.35%, while d = 0.7 d=0.7 offers the better accuracy–length balance at 65.00% with 18,412 tokens. Periodic snapshots are weaker, reaching at most 63.47%. Updating the teacher every step performs best overall at 65.97% with 17,561 tokens. Because each schedule is represented by one training trajectory, small differences should not be overinterpreted.

\FloatBarrier

## Appendix E Effect of Privileged-Context Placement

The placement ablation separates teacher refresh from the representation of the verified solution. Table 16 reports the complete Qwen3-8B comparison across the three prompt formats illustrated in fig. 7 . Every dynamic variant outperforms its frozen counterpart. With a dynamic teacher, assistant-side prefill is strongest, reference-last is intermediate, and instruction-last is weakest. Under a frozen teacher, reference-last performs best but remains far below the dynamic variants.

After generating Y 0 Y_{0} without g g , we hold it fixed. At position t t , both branches score the same Y 0 , < t Y_{0,<t} ; only the privileged branch also receives g g , and neither observes future tokens.

Table 17 shows a front-loaded, not uniformly stronger, intervention. At positions 1–32, assistant-side has the highest KL/NLL, indicating the largest distribution shift and less probability on the observed Y 0 Y_{0} token. After position 32, both metrics are lowest, indicating agreement with the fixed continuation rather than correctness. This pattern is consistent with route initialization, while the frozen reversal in table 16 shows that placement alone is insufficient.

#### Evolution of the privileged signal.

We next track the same diagnostic over training. At each checkpoint, KL compares the verified-solution-conditioned teacher distribution q T q_{T} with the no-GOLD student distribution p S p_{S} on the same fixed correct trajectories. KL records how strongly the privileged context changes the prediction, but not whether that change favors the observed correct continuation. We therefore also report Δ ​ NLL = NLL no-GOLD − NLL with-GOLD , \Delta\mathrm{NLL}=\mathrm{NLL}_{\text{no-GOLD}}-\mathrm{NLL}_{\text{with-GOLD}}, (10) where a positive value means that privileged conditioning assigns greater likelihood to the fixed correct continuation.

The two metrics separate intervention strength from direction: KL asks how much GOLD changes the prediction, while Δ \Delta NLL asks whether that change favors the recorded correct continuation. For assistant-side conditioning, both signals increase throughout training: KL rises monotonically from 0.1303 to 0.4371, and Δ \Delta NLL rises from + 0.0414 +0.0414 to + 0.6474 +0.6474 . Assistant-side also has the largest Δ \Delta NLL at every checkpoint, with its advantage widening later in training. The two user-side runs strengthen through step 50 but then saturate or regress. From step 50 to 100, Δ \Delta NLL increases from + 0.3729 +0.3729 to + 0.4139 +0.4139 for assistant-side, but falls from + 0.2209 +0.2209 to + 0.0266 +0.0266 for reference-last and from + 0.1492 +0.1492 to + 0.0026 +0.0026 for instruction-last. At step 200, the assistant-side improvement exceeds reference-last and instruction-last by 0.6702 and 0.5484, respectively. Thus, the user-side contexts can continue to alter the output distribution without reliably increasing likelihood on the recorded correct path.

These curves show three training trajectories progressively separating; they do not by themselves identify prompt position as the cause because each column comes from a separately trained model. Nor is larger KL synonymous with higher benchmark accuracy: assistant-side accuracy peaks before its KL does. Finally, Δ \Delta NLL measures alignment with the fixed correct trajectories used in this probe, not final-answer accuracy or support for every valid derivation.

\FloatBarrier

## Appendix F Qwen3-1.7B Training Stability

At 1.7B, both recursive variants improve rapidly but become unstable later in training: DCE peaks at step 30, while DCE+SRCL peaks at step 50 before declining. Table 19 reports the complete trajectory and highlights the importance of early stopping at this scale.

\FloatBarrier

## Appendix G Fixed-Trace Probe Values

Figure 4 summarizes endpoint EOS and reflection-cue probabilities on fixed cohorts from AIME24, AIME25, and AIME26. The cohorts contain 227, 212, and 245 incorrect responses and 879, 805, and 583 observed revision events, respectively. At each event, r t r_{t} is the token that appears when the stored trajectory begins to revise, such as Wait . Table 20 reports the complete AIME26 values, including EOS probability at the same pre-reflection positions.

\FloatBarrier

## Appendix H EOS-Penalty Ablation

#### Objective.

To test whether concision can be induced directly, we add an EOS-specific auxiliary loss rather than learning from SRCL rewrites. A verified response is truncated after its final balanced boxed expression and retained as y i cut y_{i}^{\mathrm{cut}} only if the answer judge still accepts it. Each eligible response receives one EOS target: ℒ EOS ( k ) = { 1 N valid ​ ∑ i = 1 N valid [ 1 − p θ k ​ ( EOS ∣ x i , y i cut ) ] , N valid > 0 , 0 , N valid = 0 . \mathcal{L}_{\mathrm{EOS}}^{(k)}=\begin{cases}\dfrac{1}{N_{\mathrm{valid}}}\displaystyle\sum_{i=1}^{N_{\mathrm{valid}}}\left[1-p_{\theta_{k}}\!\left(\mathrm{EOS}\mid x_{i},y_{i}^{\mathrm{cut}}\right)\right],&N_{\mathrm{valid}}>0,\\[6.0pt] 0,&N_{\mathrm{valid}}=0.\end{cases} (11) The loss is averaged over eligible responses and set to zero when none are available. We evaluate it as an alternative to SRCL rather than as part of the main method.

#### Results.

At 8B, EOS Penalty is 2,979 tokens shorter than DCE but 4.65 points less accurate and remains below DCE+SRCL. At 4B, it reaches only 32.71% with 7,169 tokens. Direct termination pressure therefore shortens responses at a substantially larger accuracy cost than learning from concise verified rewrites.

\FloatBarrier

## Appendix I Cross-Scale Evaluation of OPSD-TTS

Table 23 reports OPSD-TTS at exact 8K and 16K output budgets. Doubling the forced budget changes Average@12 by only 0.07, 1.05, and 2.29 points at 1.7B, 4B, and 8B, respectively, and remains far below DCE. Additional generation alone therefore does not reproduce the benefit of co-evolving training.

\FloatBarrier

## Appendix J Reproducibility Details

Table 24 summarizes the data, optimization, generation, and evaluation settings used throughout the main experiments; each ablation states its deviations explicitly.

\FloatBarrier

## Appendix K Additional SRCL-Weight Sensitivity

Table 25 extends the SRCL-weight sweep to Qwen3-4B.

The sweep peaks at λ S = 35 \lambda_{S}=35 , reaching 61.88% Average@12 with 17,265 tokens. Relative to λ S = 25 \lambda_{S}=25 , it improves accuracy by 3.06 points while using 3,148 fewer tokens; larger weights then reduce accuracy, showing that the balance between guidance and concise-target learning remains important at 4B.

\FloatBarrier

## Appendix L Results on Additional Benchmarks

We additionally evaluate Qwen3-8B and Qwen3-4B under Average@12 on three benchmarks: MATH-500 ( Hendrycks et al., 2021 ) , GPQA-Diamond ( Rein et al., 2023 ) , and AMC 2023.

DCE+SRCL improves over OPSD on all three benchmarks at both scales, with the largest gains on AMC23. The improved accuracy generally accompanies longer outputs on these broader tasks, unlike the concision gains observed on the main benchmark suite.

\FloatBarrier

\FloatBarrier

## Appendix M SRCL Rewrite Filtering and Acceptance

SRCL learns only from model-generated rewrites that satisfy its concision and correctness criteria. We audit all 3,200 candidates generated during the Qwen3-8B DCE+SRCL run in table 27 . The acceptance rate remains stable between 70.63% and 73.13% across four consecutive 50-step windows, with 2,296 rewrites (71.75%) retained overall. Accepted targets are 83.74% shorter than their source rollouts, whose mean length is 1,997 tokens. Of the 904 rejected candidates, 826 fail a structural check, 76 retain explicit revision language, and two do not terminate naturally. Rejection categories record the first failed gate. A rejected rewrite contributes no SRCL loss, although its original example still receives DCE training.

#### Filtering pipeline.

A candidate is retained only if it passes all four gates below. 1. Termination and compression. The rewrite must terminate naturally, be nonempty, remain within the 12K limit, and contain fewer tokens than its source rollout.

2. Reflection-free rewriting. A case-insensitive scan rejects explicit reconsideration, correction, restart, or repeated-verification phrases, including Wait , Actually , Correction , double-check , and start over .

3. Answer validity. The rewrite must contain at least 32 tokens and a balanced boxed answer near the end. The final box must be correct, and no earlier box may contain an incorrect answer.

4. Self-containment and repetition. The rewrite may not begin as a continuation fragment, refer to omitted material, or exceed the implementation’s repeated-phrase and repeated-line thresholds.

#### Endpoint verification.

The verifier extracts the first balanced boxed answer after the final </think> delimiter, when present, and compares it with the gold answer using math_verify . If parsing fails, it falls back to case-insensitive exact matching after whitespace removal; ratio notation a : b a:b is normalized to a / b a/b . A separate structural check examines every boxed expression, requiring the final box to be correct and rejecting candidates with an earlier incorrect box.

\FloatBarrier

## Appendix N Prompt Templates

The logical prompt templates are shown below, with model-specific chat-control tokens omitted. All privileged variants use the same problem x x , verified solution g g , transition text, and on-policy response Y 0 Y_{0} ; only the message role and ordering change. SRCL uses a separate rewrite request.

## Instructions for reporting errors

We are continuing to improve HTML versions of papers, and your feedback helps enhance accessibility and mobile support. To report errors in the HTML that will help us improve conversion and rendering, choose any of the methods listed below:

Click the "Report Issue" ( ) button, located in the page header.

Tip: You can select the relevant text first, to include it in your report.

Our team has already identified the following issues . We appreciate your time reviewing and reporting rendering errors we may not have found yet. Your efforts will help us improve the HTML versions for all readers, because disability should not be a barrier to accessing research. Thank you for your continued support in championing open access for all.

Have a free development cycle? Help support accessibility at arXiv! Our collaborators at LaTeXML maintain a list of packages that need conversion , and welcome developer contributions .
