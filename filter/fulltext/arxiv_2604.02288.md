##### Report GitHub Issue

Content selection saved. Describe the issue below:

# Unifying Group-Relative and Self-Distillation Policy Optimization via Sample Routing

###### Abstract

Reinforcement learning with verifiable rewards (RLVR) has become a standard paradigm for post-training large language models. While Group Relative Policy Optimization (GRPO) is widely adopted, its coarse credit assignment uniformly penalizes failed rollouts, lacking the token-level focus needed to efficiently address specific deviations. Self-Distillation Policy Optimization (SDPO) addresses this by providing denser, more targeted logit-level supervision that facilitates rapid early improvement, yet it frequently collapses during prolonged training. We trace this late-stage instability to two intrinsic flaws: self-distillation on already-correct samples introduces optimization ambiguity, and the self-teacher’s signal reliability progressively degrades. To resolve these issues, we propose Sample-Routed Policy Optimization (SRPO) , a unified on-policy framework that routes correct samples to GRPO’s reward-aligned reinforcement and failed samples to SDPO’s targeted logit-level correction. SRPO further incorporates an entropy-aware dynamic weighting mechanism to suppress high-entropy, unreliable distillation targets while emphasizing confident ones. Evaluated across five benchmarks and two model scales, SRPO achieves both the rapid early improvement of SDPO and the long-horizon stability of GRPO. It consistently surpasses the peak performance of both baselines, raising the five-benchmark average on Qwen3-8B by 3.4% over GRPO and 6.3% over SDPO, while simultaneously yielding moderate response lengths and lowering per-step compute cost by up to 17.2%.

## 1 Introduction

Post-training large language models through reinforcement learning with verifiable rewards (RLVR) has emerged as a standard approach for improving reasoning and problem-solving capabilities ( Jaech et al., 2024 ; Guo et al., 2025 ; Team et al., 2025 ; Yang et al., 2025 ) . Among RLVR methods, Group Relative Policy Optimization ( Shao et al., 2024 , GRPO;) is widely adopted for its simplicity and stability. GRPO estimates advantages by normalizing outcome rewards across a group of rollouts, producing a single scalar advantage that is applied uniformly to every token in a rollout. For successful rollouts, this uniform assignment is generally appropriate, as most intermediate steps support the correct outcome. Conversely, for failed rollouts, this coarse token credit assignment distributes a uniform penalty across the entire sequence. Consequently, the policy update lacks the focus needed to address specific deviations, which ultimately diminishes sample efficiency and slows convergence ( Khandoga et al., 2026 ; Kumar et al., 2026 ; Parthasarathi et al., 2025 ) .

To overcome this sparsity in credit assignment, recent work has turned to on-policy distillation ( Agarwal et al., 2024 ; Lu and Lab, 2025 ) and self-distillation ( Hübotter et al., 2026 ; Zhao et al., 2026 ; Ye et al., 2026 ; Song et al., 2026 ) , which provide dense logit-level guidance for more precise optimization. Self-distillation removes the need for an external teacher by conditioning the model on privileged context (e.g., the correct solution) to supervise its own generated trajectories. A prominent example, Self-Distillation Policy Optimization ( Hübotter et al., 2026 , SDPO;) , often achieves much faster early convergence in complex domains such as scientific reasoning and agentic tool use. However, as shown in Figure 1 (a), this early advantage is not sustained: under prolonged training, SDPO is consistently surpassed by GRPO and often suffers catastrophic collapse. While recent work Kim et al. (2026) attributes similar instability in math domains to the suppression of epistemic verbalization, we provide a complementary diagnosis from the perspective of the distillation signal and attribute this instability to two intrinsic causes within the self-distillation mechanism.

First, self-distillation on already-correct samples introduces optimization ambiguity. In SDPO, the self-teacher is conditioned on a successful sibling rollout to provide dense, logit-level targets. While this is effective for correcting failed samples, it can be counterproductive for already-correct ones: forcing a successful rollout to match a different successful sibling imposes arbitrary logit-level preferences between reward-equivalent reasoning paths. Figure 1 (b) supports this view: restricting SDPO updates to failed samples retains most of its benefit, whereas applying it only to correct samples degrades performance and accelerates collapse.

Second, the quality of the self-teacher’s distillation signal degrades as training progresses. As the gap between the self-teacher and student narrows during training ( Hübotter et al., 2026 ) , the distillation signal becomes less informative, while the self-teacher’s token-level entropy rises (Figure 1 (c)), indicating increasingly uncertain predictions. This degradation in informativeness and reliability contributes directly to the late-stage instability of SDPO.

These observations suggest that GRPO and SDPO have complementary optimization properties. For correct samples, the sequence-level credit assignment of GRPO is usually sufficient, and its Monte Carlo advantages robustly anchor the policy update toward expected reward maximization ( Zhang et al., 2024 ; Hübotter et al., 2026 ) . But for failed samples with localized reasoning errors, dense logit-level correction of SDPO is more effective and avoids the ambiguity above when restricted to failed trajectories. Based on this insight, we introduce Sample-Routed Policy Optimization (SRPO) , a unified on-policy framework that routes correct samples to a GRPO branch and failed samples with available teacher information to an SDPO branch. To mitigate late-stage signal degradation, we further equip the SDPO branch with an entropy-aware dynamic weighting mechanism that downweights uncertain distillation targets and emphasizes reliable corrections. This design enables rapid correction early in training while increasingly relying on reward-aligned reinforcement as more rollouts become correct, thereby stabilizing late-stage optimization.

Evaluated across five benchmarks following the protocol of Hübotter et al. (2026) and two Qwen3 model scales ( Yang et al., 2025 ) , SRPO consistently achieves the highest peak performance. Specifically, it raises the five-benchmark average on Qwen3-8B to 77.4% (+3.4 over GRPO, +6.3 over SDPO) and on Qwen3-4B to 74.2% (+4.5 over GRPO, +7.5 over SDPO). Furthermore, SRPO maintains a moderate response length, avoiding both the verbosity of GRPO and the excessive brevity of pure SDPO, a phenomenon recently linked to degraded epistemic reasoning ( Kim et al., 2026 ) . It also reduces per-step compute cost by up to 17.2% over long training horizons. Our contributions are threefold:

• We identify two intrinsic causes of late-stage instability in SDPO: self-distillation on already-correct samples introduces optimization ambiguity, and the quality of the self-teacher’s distillation signal progressively degrades.

• We propose SRPO, a unified framework that bridges group-relative and self-distillation policy optimization by routing each sample to the optimization signal best suited to its learning status, augmented by entropy-aware dynamic weighting to suppress unreliable distillation targets and emphasize reliable ones.

• We demonstrate across five benchmarks and two model scales that SRPO improves early training efficiency, long-horizon stability, and peak accuracy, while simultaneously yielding moderate response lengths and lower per-step compute time.

## 2 Preliminaries

We review the two optimization paradigms unified by SRPO. Throughout, let x x denote a prompt, { y i } i = 1 G \{y_{i}\}_{i=1}^{G} a group of G G on-policy rollouts sampled from the current policy π θ \pi_{\theta} , and { r i } i = 1 G \{r_{i}\}_{i=1}^{G} the corresponding scalar rewards.

### 2.1 Group Relative Policy Optimization

GRPO is a policy-gradient method for post-training with verifiable rewards that eliminates the need for a learned critic. For each prompt x x , the policy generates a group of G G rollouts and obtains a scalar reward for each. The advantage of rollout i i is estimated by normalizing its reward relative to the group:

A i GRPO = r i − r ¯ σ r + ϵ , A_{i}^{\mathrm{GRPO}}=\frac{r_{i}-\bar{r}}{\sigma_{r}+\epsilon},

where r ¯ \bar{r} and σ r \sigma_{r} are the mean and standard deviation of { r i } i = 1 G \{r_{i}\}_{i=1}^{G} . The policy is updated via a clipped surrogate objective:

ℒ GRPO ​ ( θ ) = 𝔼 ⁡ [ min ⁡ ( ρ i , t ​ ( θ ) ​ A i GRPO , clip ⁡ ( ρ i , t ​ ( θ ) , 1 − ε , 1 + ε ) ​ A i GRPO ) ] , \mathcal{L}_{\mathrm{GRPO}}(\theta)=\mathbb{E}\!\left[\min\!\left(\rho_{i,t}(\theta)\,A_{i}^{\mathrm{GRPO}},\;\operatorname{clip}(\rho_{i,t}(\theta),1-\varepsilon,1+\varepsilon)\,A_{i}^{\mathrm{GRPO}}\right)\right],

where ρ i , t ​ ( θ ) = π θ ​ ( y i , t ∣ x , y i , < t ) / π θ old ​ ( y i , t ∣ x , y i , < t ) \rho_{i,t}(\theta)=\pi_{\theta}(y_{i,t}\mid x,y_{i,<t})\,/\,\pi_{\theta_{\mathrm{old}}}(y_{i,t}\mid x,y_{i,<t}) is the importance-sampling ratio at token position t t of rollout i i . Because A i GRPO A_{i}^{\mathrm{GRPO}} is a sequence-level quantity assigned uniformly to every token in a rollout, GRPO delivers reward-aligned yet coarse-grained credit assignment: it reliably reinforces or suppresses entire rollouts, but cannot identify which individual tokens are responsible for the outcome.

### 2.2 Self-Distillation Policy Optimization

SDPO augments the reward signal with dense logit-level supervision derived from self-distillation. Rather than relying solely on scalar rewards, it constructs a feedback-conditioned self-teacher from the same model. The student distribution is π θ ( ⋅ ∣ x ) \pi_{\theta}(\cdot\mid x) , while the self-teacher distribution is π θ ( ⋅ ∣ x , f ) \pi_{\theta}(\cdot\mid x,f) , where f f denotes auxiliary information obtained during the rollout process (e.g., a successful sibling rollout from the same group or environment feedback such as execution traces).

Given a rollout y i y_{i} , SDPO trains the student to match the self-teacher’s distribution along the original trajectory by minimizing a logit-level divergence. Using KL divergence as an illustration:

ℒ SDPO ( θ ) = ∑ t KL ( π θ ( ⋅ ∣ x , y i , < t ) ∥ stopgrad [ π θ ( ⋅ ∣ x , f , y i , < t ) ] ) , \mathcal{L}_{\mathrm{SDPO}}(\theta)=\sum_{t}\mathrm{KL}\!\Big(\pi_{\theta}(\cdot\mid x,y_{i,<t})\;\Big\|\;\operatorname{stopgrad}\big[\pi_{\theta}(\cdot\mid x,f,y_{i,<t})\big]\Big),

where the specific divergence may also be instantiated as the reverse KL or Jensen–Shannon divergence, and the self-teacher parameters are maintained as an exponential moving average (EMA) of the student ( Hübotter et al., 2026 ) .

The self-teacher does not generate a new trajectory; it re-scores the student’s own rollout under the enriched context ( x , f ) (x,f) , so the entire procedure remains on-policy while providing dense logit-level guidance on the model’s own rollouts.

The two methods differ fundamentally in their supervision signals. GRPO is reward-driven: its advantage is derived from outcome rewards via group normalization, producing updates that are directly aligned with expected return but uniformly distributed across tokens. SDPO is teacher-driven: its advantage is induced by the discrepancy between the self-teacher and student distributions, yielding dense logit-level guidance whose quality depends on the self-teacher. The complementarity between coarse, reward-aligned updates and dense, teacher-dependent guidance motivates SRPO, which routes each sample to the supervision signal best suited to its learning needs.

## 3 The SRPO

SRPO is a unified on-policy framework that routes each rollout to the supervision signal best suited to its learning status. Correct rollouts are optimized with GRPO for reward-aligned reinforcement; incorrect rollouts with available teacher information are optimized with SDPO for dense logit-level correction. An entropy-aware dynamic weighting mechanism further modulates token-level contributions on the SDPO branch, suppressing unreliable distillation targets while emphasizing confident ones. Figure 2 illustrates the overall framework.

### 3.1 Sample-Level Routing

For each rollout y i y_{i} , we define two binary indicators: a correctness flag c i = 𝟏 ​ [ y i ​ is correct ] c_{i}=\mathbf{1}[y_{i}\text{ is correct}] and a teacher-availability flag m i = 𝟏 ​ [ teacher information is available for ​ y i ] m_{i}=\mathbf{1}[\text{teacher information is available for }y_{i}] . The routing mask is then

z i SDPO = ( 1 − c i ) ​ m i , z i GRPO = 1 − z i SDPO . z_{i}^{\mathrm{SDPO}}=(1-c_{i})\,m_{i},\qquad z_{i}^{\mathrm{GRPO}}=1-z_{i}^{\mathrm{SDPO}}.

That is, only incorrect rollouts with available teacher information are routed to the SDPO branch; all remaining rollouts are optimized with GRPO.

This routing does not alter the underlying policy-gradient structure, because both branches update the same policy on the same on-policy trajectories, with only the form of the advantage estimator differing. For GRPO, the gradient takes the standard policy-gradient form

∇ θ ℒ GRPO = − 𝔼 ⁡ [ ∑ t ∇ θ ​ log ​ π θ ​ ( y t ∣ x , y < t ) ⋅ A i GRPO ] , \nabla_{\theta}\mathcal{L}_{\mathrm{GRPO}}=-\mathbb{E}\!\left[\sum_{t}\nabla_{\theta}\log\pi_{\theta}(y_{t}\mid x,y_{<t})\cdot A_{i}^{\mathrm{GRPO}}\right],

where the sequence-level advantage A i GRPO A_{i}^{\mathrm{GRPO}} is shared across all tokens in rollout i i . For SDPO, prior work ( Hübotter et al., 2026 ) shows that distillation gradient admits an analogous form

− ∇ θ ℒ SDPO = 𝔼 ⁡ [ ∑ t ∑ v ∈ 𝒱 ∇ θ ​ log ​ π θ ​ ( v ∣ x , y < t ) ⋅ A t SDPO ​ ( v ) ] , -\nabla_{\theta}\mathcal{L}_{\mathrm{SDPO}}=\mathbb{E}\!\left[\sum_{t}\sum_{v\in\mathcal{V}}\nabla_{\theta}\log\pi_{\theta}(v\mid x,y_{<t})\cdot A_{t}^{\mathrm{SDPO}}(v)\right],

where the logit-level advantage A t SDPO ​ ( v ) A_{t}^{\mathrm{SDPO}}(v) is induced by the discrepancy between the self-teacher and student distributions. The two methods can thus be viewed as advantage estimators at different granularities (reward-derived and sequence-level versus teacher-derived and logit-level), and sample routing simply selects the more appropriate estimator for each sample.

### 3.2 Dynamic-Weighted SDPO

Even within the SDPO branch, teacher supervision is not equally reliable across tokens: low-entropy predictions typically provide clear corrective signals, whereas high-entropy predictions are more likely to introduce noise. We therefore introduce entropy-aware dynamic weighting, which reweights the SDPO loss at the token level according to teacher entropy. For brevity, we refer to this variant as Dynamic-Weighted SDPO (DW-SDPO) throughout this section.

Let q i , t ​ ( v ) = π θ ​ ( v ∣ x , f i , y i , < t ) q_{i,t}(v)=\pi_{\theta}(v\mid x,f_{i},y_{i,<t}) denote the self-teacher distribution at position t t of rollout i i , and let

H i , t = − ∑ v ∈ 𝒱 q i , t ( v ) log q i , t ( v ) H_{i,t}=-\sum_{v\in\mathcal{V}}q_{i,t}(v)\log q_{i,t}(v)

be its entropy. We define the unnormalized weight w ~ i , t = exp ⁡ ( − β ​ H i , t ) \tilde{w}_{i,t}=\exp(-\beta H_{i,t}) , where β > 0 \beta>0 controls sensitivity to entropy differences, and normalize over all valid SDPO tokens to preserve the overall loss scale:

w i , t = w ~ i , t 1 | Ω sdpo | ​ ∑ ( j , s ) ∈ Ω sdpo w ~ j , s , w_{i,t}=\frac{\tilde{w}_{i,t}}{\frac{1}{|\Omega_{\mathrm{sdpo}}|}\sum_{(j,s)\in\Omega_{\mathrm{sdpo}}}\tilde{w}_{j,s}},

where Ω sdpo \Omega_{\mathrm{sdpo}} is the set of valid tokens routed to the SDPO branch. The weighted token loss is then ℓ i , t DW ​ - ​ SDPO = w i , t ​ ℓ i , t SDPO \ell_{i,t}^{\mathrm{DW\text{-}SDPO}}=w_{i,t}\,\ell_{i,t}^{\mathrm{SDPO}} , where ℓ i , t SDPO \ell_{i,t}^{\mathrm{SDPO}} is the base SDPO token loss. This reweighting does not alter the functional form of SDPO; it only modulates each token’s contribution according to teacher confidence, emphasizing reliable corrections while suppressing uncertain ones.

### 3.3 Training Objective

Let ℓ i , t GRPO \ell_{i,t}^{\mathrm{GRPO}} denote the token-level GRPO loss (the sequence-level advantage distributed over valid response tokens) and ℓ i , t DW ​ - ​ SDPO \ell_{i,t}^{\mathrm{DW\text{-}SDPO}} the weighted SDPO loss defined above. The combined objective is

ℒ final = ∑ i , t z i GRPO ​ ℓ i , t GRPO + ∑ i , t z i SDPO ​ ℓ i , t DW ​ - ​ SDPO ∑ i , t z i GRPO + ∑ i , t z i SDPO , \mathcal{L}_{\mathrm{final}}=\frac{\sum_{i,t}z_{i}^{\mathrm{GRPO}}\ell_{i,t}^{\mathrm{GRPO}}\;+\;\sum_{i,t}z_{i}^{\mathrm{SDPO}}\ell_{i,t}^{\mathrm{DW\text{-}SDPO}}}{\sum_{i,t}z_{i}^{\mathrm{GRPO}}\;+\;\sum_{i,t}z_{i}^{\mathrm{SDPO}}},

where all summations over t t are restricted to valid response tokens. The denominator normalizes by the total number of routed tokens, so each branch contributes in proportion to the tokens it covers. This avoids introducing an additional mixing hyperparameter and naturally adapts to the evolving sample composition: early in training, when failures are frequent, more tokens flow through the SDPO branch, giving dense correction a larger effective weight; as the policy improves and more rollouts succeed, the GRPO branch dominates, anchoring the update to the reward objective.

Algorithm 1 summarizes the full training procedure.

## 4 Experiments

### 4.1 Experimental Setup

Model We use instruct-tuned base models from the Qwen3 family ( Yang et al., 2025 ) at two scales: Qwen3-4B and Qwen3-8B. This setting allows us to examine whether the behavior of SRPO is consistent across model sizes. Unless otherwise noted, analyses other than the main performance comparison are conducted at the 8B scale.

Datasets We follow the evaluation setup of SDPO and consider five benchmarks: Chemistry, Physics, Biology, Materials, and Tool Use. The first four are science question-answering tasks built from the reasoning subsets of SciKnowEval ( Feng et al., 2024 ) and target undergraduate-level scientific reasoning in different domains. Tool Use evaluates whether the model can map a user request and a tool specification to the correct tool call, using ToolAlpaca ( Tang et al., 2023 ) . Following SDPO, we perform a train-test split on each benchmark to evaluate in-domain generalization.

Baselines We compare against two baselines: (1) GRPO , a strengthened implementation of GRPO ( Shao et al., 2024 ) following recent best practices ( Olmo et al., 2025 ; Khatri et al., 2025 ) , including asymmetric clipping ( Yu et al., 2025 ) , unbiased advantage normalization ( Liu et al., 2025 ) , and off-policy correction for distributed inference ( Yao et al., 2025 ) ; and (2) SDPO , which replaces reward-only supervision with self-distillation from a feedback-conditioned self-teacher and provides a finer-grained but potentially biased training signal. In our experiments, SDPO uses successful sibling rollouts within the same group as teacher information for failed samples.

Implementation Details For both GRPO and SDPO, we adopt the training setup and hyperparameters from the original SDPO paper, where each method’s configuration was selected via grid search over learning rates and mini-batch sizes to maximize the validation accuracy ( Hübotter et al., 2026 ) . Both methods use a training batch size of 32 and sample 8 rollouts per prompt; the main differences are the mini-batch size and learning rate: GRPO uses a mini-batch size of 8 and a learning rate of 1 × 10 − 6 1\times 10^{-6} , whereas SDPO uses 32 with 1 × 10 − 5 1\times 10^{-5} . For SRPO, we keep the training batch size, mini-batch size, and rollout number the same as in SDPO, set the learning rate to 5 × 10 − 6 5\times 10^{-6} to balance the reward-driven and self-distillation signals within a single objective, and use a dynamic-weighting temperature β \beta with default value 1. All experiments are conducted on 8 NVIDIA H20 GPUs.

### 4.2 Main Results

SRPO achieves early efficiency, long-horizon stability, and a higher performance ceiling. Table 1 reports the highest avg@16 achieved within each wall-clock budget, following the reporting protocol of SDPO. 1 1 1 We note that Qwen3-4B slightly outperforms Qwen3-8B on the base instruct checkpoints across all five benchmarks. These benchmarks were not explicitly targeted during Qwen3 fine-tuning ( Hübotter et al., 2026 ) , and such nonmonotonic scaling on out-of-distribution downstream tasks is a well-documented phenomenon ( McKenzie et al., 2023 ; Lourie et al., 2025 ) . Crucially, the larger 8B model still achieves higher post-training performance and larger total training gains despite starting from a lower base, consistent with the expected scaling behavior, indicating that our conclusions are not affected by this anomalous ordering of base-model performance. On Qwen3-8B, SRPO improves the 10h average from 71.1 (SDPO) and 74.0 (GRPO) to 77.4; on Qwen3-4B, the corresponding improvement is from 66.7 and 69.7 to 74.2. Across both scales, SDPO saturates early, as evidenced by its identical 5h and 10h averages, while GRPO improves more steadily before eventually plateauing. SRPO largely avoids both issues, matching the early training efficiency of SDPO while maintaining steady improvement over longer horizons and ultimately exceeding the peak performance of both baselines. Notably, at 10h on Qwen3-8B, SRPO improves over GRPO by +4.1 on Chemistry, +4.8 on Physics, +2.2 on Biology, +3.7 on Materials, and +2.2 on Tool Use. We attribute this to entropy-aware dynamic weighting on the SDPO branch: even when the self-teacher becomes noisier in later training, reweighting by teacher confidence preserves useful logit-level guidance while suppressing uncertain targets, enabling SRPO to continue improving beyond the point where pure GRPO plateaus.

To complement the tabular summary, Figure 3 plots representative learning curves on Qwen3-8B, which reveal two recurring patterns.

Pattern 1: When self-distillation is effective, SRPO extends the advantage. In Chemistry, SDPO leads at 1h (71.6 vs. 69.2 for SRPO), but SRPO overtakes it by 5h and reaches 83.0 at 10h, exceeding both SDPO (80.6) and GRPO (78.9). As Figure 3 (a) shows, SRPO tracks SDPO’s rapid early rise while avoiding its subsequent collapse. Biology follows a similar trajectory: SRPO achieves the best 1h result (55.8), and the gap widens as SDPO stalls at 58.5 while SRPO climbs to 72.8 at 10h (Figure 3 (b)).

Pattern 2: When self-distillation is ineffective, SRPO remains stable. As Figure 3 (c) shows, SDPO degrades substantially over time on Tool Use, whereas SRPO remains stable and tracks or exceeds GRPO throughout (65.2, 71.2, 71.2 vs. 64.3, 68.5, 69.0 for GRPO). Both patterns reflect the effectiveness of the sample-routing design: when self-distillation is useful, SRPO exploits it to accelerate learning; when it is not, the GRPO branch anchors optimization to the reward objective and prevents drift.

### 4.3 Ablation Study

Sample routing is more robust than advantage-level mixing over long horizons. To isolate the mixing strategy, we first compare SRPO w/o dynamic weighting against an Advantage Mix control that combines GRPO and SDPO at the advantage level:

A i , t Mix ​ ( v ) = λ ​ A i , t GRPO ​ ( v ) + ( 1 − λ ) ​ A i , t SDPO ​ ( v ) , λ ∈ [ 0 , 1 ] , A_{i,t}^{\mathrm{Mix}}(v)=\lambda A_{i,t}^{\mathrm{GRPO}}(v)+(1-\lambda)A_{i,t}^{\mathrm{SDPO}}(v),\qquad\lambda\in[0,1],

where the GRPO term is reward-derived and the SDPO term is feedback-derived. We set λ = 0.9 \lambda=0.9 to keep the two advantages on a comparable scale, consistent with the mixing ratio used in SDPO ( Hübotter et al., 2026 ) , and keep all other hyperparameters unchanged. Advantage Mix is slightly better at 1h (+0.7), but falls behind by 2.5 points at 5h and 3.3 points at 10h, with no further gain after 5h.

This pattern matches the changing roles of the two signals over training. Early on, when self-distillation remains high quality, mixing dense SDPO guidance with reward-aligned GRPO updates can help. Later, as the SDPO signal becomes less reliable, advantage-level mixing instead propagates this noise into the learning process, harming stability. By contrast, sample routing confines SDPO to failed samples and leaves correct samples under GRPO, reducing interference and yielding stronger long-term performance.

Dynamic weighting provides an additional late-stage gain on top of sample routing. We then compare SRPO against SRPO w/o dynamic weighting to isolate the effect of entropy-aware weighting. Adding dynamic weighting improves the average result by 0.4 at 1h, 0.7 at 5h, and 1.8 at 10h. The widening gain suggests that this component matters most when the self-teacher becomes less reliable and noisier. This is consistent with the role of entropy-aware weighting: it emphasizes high-confidence dense corrections while suppressing uncertain targets, further stabilizing the SDPO branch in later training.

Together, these ablations suggest that SRPO’s gains come from two complementary components: sample routing provides the stronger mixing strategy and the main source of long-horizon robustness, while dynamic weighting adds further late-stage improvement by improving the reliability of the SDPO branch.

### 4.4 Response Length and Compute Time

SRPO yields moderate response lengths between GRPO and SDPO. Figure 4 (a) shows response length during training of Qwen3-8B on Chemistry. The three methods exhibit different trends: GRPO produces the longest responses, SDPO the shortest, and SRPO settles between the two. The verbosity of GRPO inflates inference cost, while the excessive brevity of SDPO has been linked to degraded reasoning due to the suppression of epistemic verbalization ( Kim et al., 2026 ) . SRPO’s moderate response length suggests a balance between the two, potentially mitigating both issues.

SRPO achieves the lowest per-step compute time over long training horizons. Figure 4 (b) reports the average seconds per training step of Qwen3-8B, averaged over the five benchmarks. At 1h, SRPO incurs a 17.4% overhead relative to GRPO (83.4s vs. 71.0s per step), while being lower than SDPO (83.4s vs. 85.9s). As training proceeds, the cost advantage shifts in favor of SRPO. At 5h, it is 4.9% faster than GRPO and 6.7% faster than SDPO (78.3s vs. 82.4s and 83.9s). At 10h, the advantage widens further, reaching 17.2% over GRPO and 9.4% over SDPO (75.8s vs. 91.5s and 83.7s).

These results are consistent with the design of SRPO. Early in training, failed samples are more frequent, so the SDPO branch is activated more often and the additional self-teacher log-probs computation is more visible. Later in training, the fraction of failed samples decreases, reducing the self-teacher overhead. At the same time, SRPO produces shorter responses than GRPO, further lowering inference cost. Taken together, SRPO improves not only training efficiency and stability, but also computational efficiency in terms of response length and per-step compute time.

## 5 Conclusion

We revisit the trade-off between reward-driven reinforcement and self-distillation in LLM post-training and propose SRPO, a unified on-policy framework that routes successful samples to GRPO for reward-aligned reinforcement and failed samples with teacher information to SDPO for dense logit-level correction, together with entropy-aware dynamic weighting to suppress unreliable self-distillation signals and emphasize confident ones. Across five benchmarks and two model scales, SRPO consistently outperforms both pure GRPO and SDPO, demonstrating that sample-level routing can preserve the early efficiency of self-distillation while maintaining the long-horizon stability of reward-driven reinforcement. Moreover, SRPO yields moderate response lengths and lower per-step compute time over long training horizons. An important direction for future work is to extend this framework to environments with richer feedback, so that self-distillation branch can better leverage environment information.

## Ethics Statement

This work studies post-training optimization methods for large language models and does not introduce new capabilities targeted at harmful applications. However, improving reasoning quality may still increase dual-use risks (e.g., more effective generation of misleading or unsafe content). We therefore recommend deployment only under standard safety controls, including content moderation, policy-based filtering, and rate limiting.

Our experiments use publicly available benchmark datasets (SciKnowEval and ToolAlpaca-style tool-use tasks) and automatic verifiable rewards. We do not collect personal data, do not involve human subjects, and do not perform user profiling. The training objective does not use private annotations or sensitive metadata.

From an environmental perspective, SRPO is trained on GPU clusters and thus incurs non-trivial energy use. At the same time, our results show lower per-step compute time over long horizons compared with strong baselines, which may partially reduce the total compute required to reach a target performance level. We plan to release implementation details to support transparent evaluation and responsible reproduction.

## References

Agarwal et al. (2024) R. Agarwal, N. Vieillard, Y. Zhou, P. Stanczyk, S. R. Garea, M. Geist, and O. Bachem On-policy distillation of language models: learning from self-generated mistakes . In The twelfth international conference on learning representations , Cited by: §A.2 , §1 .

Buening et al. (2026) T. K. Buening, J. Hübotter, B. Pásztor, I. Shenfeld, G. Ramponi, and A. Krause Aligning language models from user interactions . arXiv preprint arXiv:2603.12273 . Cited by: §A.2 .

Cui et al. (2025) G. Cui, L. Yuan, Z. Wang, H. Wang, Y. Zhang, J. Chen, W. Li, B. He, Y. Fan, T. Yu, et al. Process reinforcement through implicit rewards . arXiv preprint arXiv:2502.01456 . Cited by: §A.1 .

Feng et al. (2024) K. Feng, X. Shen, W. Wang, X. Zhuang, Y. Tang, Q. Zhang, and K. Ding Sciknoweval: evaluating multi-level scientific knowledge of large language models . arXiv preprint arXiv:2406.09098 . Cited by: Table 4 , §4.1 .

Gu et al. (2023) Y. Gu, L. Dong, F. Wei, and M. Huang Minillm: knowledge distillation of large language models . arXiv preprint arXiv:2306.08543 . Cited by: §A.2 .

Guo et al. (2025) D. Guo, D. Yang, H. Zhang, J. Song, P. Wang, Q. Zhu, R. Xu, R. Zhang, S. Ma, X. Bi, et al. Deepseek-r1: incentivizing reasoning capability in llms via reinforcement learning . arXiv preprint arXiv:2501.12948 . Cited by: §A.1 , §1 .

Hinton et al. (2015) G. Hinton, O. Vinyals, and J. Dean Distilling the knowledge in a neural network . arXiv preprint arXiv:1503.02531 . Cited by: §A.2 .

Hübotter et al. (2025) J. Hübotter, L. Diaz-Bone, I. Hakimi, A. Krause, and M. Hardt Learning on the job: test-time curricula for targeted reinforcement learning . arXiv preprint arXiv:2510.04786 . Cited by: §A.2 .

Hübotter et al. (2026) J. Hübotter, F. Lübeck, L. Behric, A. Baumann, M. Bagatella, D. Marta, I. Hakimi, I. Shenfeld, T. K. Buening, C. Guestrin, et al. Reinforcement learning via self-distillation . arXiv preprint arXiv:2601.20802 . Cited by: §A.2 , §B.2 , §B.3 , §B.5 , Table 3 , Table 4 , §1 , §1 , §1 , §1 , §2.2 , §3.1 , §4.1 , §4.3 , footnote 1 .

Jaech et al. (2024) A. Jaech, A. Kalai, A. Lerer, A. Richardson, A. El-Kishky, A. Low, A. Helyar, A. Madry, A. Beutel, A. Carney, et al. Openai o1 system card . arXiv preprint arXiv:2412.16720 . Cited by: §1 .

Khandoga et al. (2026) M. Khandoga, R. Yuan, and V. K. Sankarapu Beyond uniform credit: causal credit assignment for policy optimization . arXiv preprint arXiv:2602.09331 . Cited by: §A.1 , §1 .

Khatri et al. (2025) D. Khatri, L. Madaan, R. Tiwari, R. Bansal, S. S. Duvvuri, M. Zaheer, I. S. Dhillon, D. Brandfonbrener, and R. Agarwal The art of scaling reinforcement learning compute for llms . arXiv preprint arXiv:2510.13786 . Cited by: §4.1 .

Kim et al. (2026) J. Kim, X. Luo, M. Kim, S. Lee, D. Kim, J. Jeon, D. Li, and Y. Yang Why does self-distillation (sometimes) degrade the reasoning capability of llms? . arXiv preprint arXiv:2603.24472 . Cited by: §A.2 , §1 , §1 , §4.4 .

Kim and Rush (2016) Y. Kim and A. M. Rush Sequence-level knowledge distillation . In Proceedings of the 2016 conference on empirical methods in natural language processing , pp. 1317–1327 . Cited by: §A.2 .

Kumar et al. (2026) A. Kumar, N. Kumar, and S. Gupta Execution-grounded credit assignment for grpo in code generation . In The 1st Workshop on Scaling Post-training for LLMs , Cited by: §A.1 , §1 .

Kwon et al. (2023) W. Kwon, Z. Li, S. Zhuang, Y. Sheng, L. Zheng, C. H. Yu, J. Gonzalez, H. Zhang, and I. Stoica Efficient memory management for large language model serving with pagedattention . In Proceedings of the 29th symposium on operating systems principles , pp. 611–626 . Cited by: §B.1 .

Lightman et al. (2023) H. Lightman, V. Kosaraju, Y. Burda, H. Edwards, B. Baker, T. Lee, J. Leike, J. Schulman, I. Sutskever, and K. Cobbe Let’s verify step by step . In The twelfth international conference on learning representations , Cited by: §A.1 .

Liu et al. (2025) Z. Liu, C. Chen, W. Li, P. Qi, T. Pang, C. Du, W. S. Lee, and M. Lin Understanding r1-zero-like training: a critical perspective . In Second Conference on Language Modeling , External Links: Link Cited by: §A.1 , §4.1 .

Lourie et al. (2025) N. Lourie, M. Y. Hu, and K. Cho Scaling laws are unreliable for downstream tasks: a reality check . arXiv preprint arXiv:2507.00885 . Cited by: footnote 1 .

Lu and Lab (2025) K. Lu and T. M. Lab On-policy distillation . Thinking Machines Lab: Connectionism . Note: https://thinkingmachines.ai/blog/on-policy-distillation External Links: Document Cited by: §A.2 , §1 .

McKenzie et al. (2023) I. R. McKenzie, A. Lyzhov, M. M. Pieler, A. Parrish, A. Mueller, A. Prabhu, E. McLean, X. Shen, J. Cavanagh, A. G. Gritsevskiy, D. Kauffman, A. T. Kirtland, Z. Zhou, Y. Zhang, S. Huang, D. Wurgaft, M. Weiss, A. Ross, G. Recchia, A. Liu, J. Liu, T. Tseng, T. Korbak, N. Kim, S. R. Bowman, and E. Perez Inverse scaling: when bigger isn’t better . Transactions on Machine Learning Research . Note: Featured Certification External Links: ISSN 2835-8856 , Link Cited by: footnote 1 .

Mitra and Ulukus (2025) P. Mitra and S. Ulukus Semantic soft bootstrapping: long context reasoning in llms without reinforcement learning . arXiv preprint arXiv:2512.05105 . Cited by: §A.2 .

Olmo et al. (2025) T. Olmo, A. Ettinger, A. Bertsch, B. Kuehl, D. Graham, D. Heineman, D. Groeneveld, F. Brahman, F. Timbers, H. Ivison, et al. Olmo 3 . arXiv preprint arXiv:2512.13961 . Cited by: §4.1 .

Parthasarathi et al. (2025) P. Parthasarathi, M. Reymond, B. Chen, Y. Cui, and S. Chandar GRPO- λ \lambda : credit assignment improves llm reasoning . arXiv preprint arXiv:2510.00194 . Cited by: §A.1 , §1 .

Sanh et al. (2019) V. Sanh, L. Debut, J. Chaumond, and T. Wolf DistilBERT, a distilled version of bert: smaller, faster, cheaper and lighter . arXiv preprint arXiv:1910.01108 . Cited by: §A.2 .

Schulman et al. (2017) J. Schulman, F. Wolski, P. Dhariwal, A. Radford, and O. Klimov Proximal policy optimization algorithms . arXiv preprint arXiv:1707.06347 . Cited by: §A.1 .

Setlur et al. (2025) A. Setlur, C. Nagpal, A. Fisch, X. Geng, J. Eisenstein, R. Agarwal, A. Agarwal, J. Berant, and A. Kumar Rewarding progress: scaling automated process verifiers for LLM reasoning . In The Thirteenth International Conference on Learning Representations , External Links: Link Cited by: §A.1 .

Shao et al. (2024) Z. Shao, P. Wang, Q. Zhu, R. Xu, J. Song, X. Bi, H. Zhang, M. Zhang, Y. Li, Y. Wu, et al. Deepseekmath: pushing the limits of mathematical reasoning in open language models . arXiv preprint arXiv:2402.03300 . Cited by: §A.1 , §1 , §4.1 .

Shenfeld et al. (2026) I. Shenfeld, M. Damani, J. Hübotter, and P. Agrawal Self-distillation enables continual learning . arXiv preprint arXiv:2601.19897 . Cited by: §A.2 .

Sheng et al. (2025) G. Sheng, C. Zhang, Z. Ye, X. Wu, W. Zhang, R. Zhang, Y. Peng, H. Lin, and C. Wu Hybridflow: a flexible and efficient rlhf framework . In Proceedings of the Twentieth European Conference on Computer Systems , pp. 1279–1297 . Cited by: §B.1 .

Snell et al. (2022) C. Snell, D. Klein, and R. Zhong Learning by distilling context . arXiv preprint arXiv:2209.15189 . Cited by: §A.2 .

Song et al. (2026) Y. Song, L. Chen, F. Tajwar, R. Munos, D. Pathak, J. A. Bagnell, A. Singh, and A. Zanette Expanding the capabilities of reinforcement learning via text feedback . arXiv preprint arXiv:2602.02482 . Cited by: §1 .

Tang et al. (2023) Q. Tang, Z. Deng, H. Lin, X. Han, Q. Liang, B. Cao, and L. Sun Toolalpaca: generalized tool learning for language models with 3000 simulated cases . arXiv preprint arXiv:2306.05301 . Cited by: Table 4 , §4.1 .

Team et al. (2025) K. Team, A. Du, B. Gao, B. Xing, C. Jiang, C. Chen, C. Li, C. Xiao, C. Du, C. Liao, et al. Kimi k1. 5: scaling reinforcement learning with llms . arXiv preprint arXiv:2501.12599 . Cited by: §1 .

Wang et al. (2026) Y. Wang, X. Chen, X. Jin, M. Wang, and L. Yang OpenClaw-rl: train any agent simply by talking . arXiv preprint arXiv:2603.10165 . Cited by: §A.2 .

Williams (1992) R. J. Williams Simple statistical gradient-following algorithms for connectionist reinforcement learning . Machine learning 8 ( 3 ), pp. 229–256 . Cited by: §A.1 .

Yang et al. (2025) A. Yang, A. Li, B. Yang, B. Zhang, B. Hui, B. Zheng, B. Yu, C. Gao, C. Huang, C. Lv, et al. Qwen3 technical report . arXiv preprint arXiv:2505.09388 . Cited by: §1 , §1 , §4.1 .

Yao et al. (2025) F. Yao, L. Liu, D. Zhang, C. Dong, J. Shang, and J. Gao Your efficient rl framework secretly brings you off-policy rl training, august 2025 . URL https://fengyao. notion. site/off-policy-rl . Cited by: §4.1 .

Ye et al. (2026) T. Ye, L. Dong, X. Wu, S. Huang, and F. Wei On-policy context distillation for language models . arXiv preprint arXiv:2602.12275 . Cited by: §1 .

Yu et al. (2025) Q. Yu, Z. Zhang, R. Zhu, Y. Yuan, X. Zuo, Y. Yue, W. Dai, T. Fan, G. Liu, L. Liu, et al. Dapo: an open-source llm reinforcement learning system at scale . arXiv preprint arXiv:2503.14476 . Cited by: §A.1 , §4.1 .

Zhang et al. (2025) D. Zhang, M. Cai, J. Light, Z. Hu, Y. Yue, and J. Tang Tdrm: smooth reward models with temporal difference for llm rl and inference . arXiv preprint arXiv:2509.15110 . Cited by: §A.1 .

Zhang et al. (2024) D. Zhang, S. Zhoubian, Z. Hu, Y. Yue, Y. Dong, and J. Tang Rest-mcts*: llm self-training via process reward guided tree search . Advances in Neural Information Processing Systems 37 , pp. 64735–64772 . Cited by: §1 .

Zhao et al. (2026) S. Zhao, Z. Xie, M. Liu, J. Huang, G. Pang, F. Chen, and A. Grover Self-distilled reasoner: on-policy self-distillation for large language models . arXiv preprint arXiv:2601.18734 . Cited by: §A.2 , §1 .

Zheng et al. (2025) C. Zheng, S. Liu, M. Li, X. Chen, B. Yu, C. Gao, K. Dang, Y. Liu, R. Men, A. Yang, et al. Group sequence policy optimization . arXiv preprint arXiv:2507.18071 . Cited by: §A.1 .

Zheng et al. (2024) L. Zheng, L. Yin, Z. Xie, C. Sun, J. Huang, C. H. Yu, S. Cao, C. Kozyrakis, I. Stoica, J. E. Gonzalez, et al. Sglang: efficient execution of structured language model programs . Advances in neural information processing systems 37 , pp. 62557–62583 . Cited by: §B.1 .

Zhoubian et al. (2025) S. Zhoubian, D. Zhang, and J. Tang ReST-rl: achieving accurate code reasoning of llms with optimized self-training and decoding . arXiv preprint arXiv:2508.19576 . Cited by: §A.1 .

## Appendix A Related Work

### A.1 Reinforcement Learning with Verifiable Rewards

Post-training with verifiable rewards has become a central paradigm for LLM alignment and adaptation, building on policy-gradient foundations such as REINFORCE and PPO ( Williams, 1992 ; Schulman et al., 2017 ) . A growing body of work applies these ideas to LLM post-training, where sequence-level outcome rewards guide optimization on model-sampled trajectories ( Guo et al., 2025 ; Shao et al., 2024 ; Yu et al., 2025 ; Liu et al., 2025 ; Zheng et al., 2025 ; Zhang et al., 2025 ; Zhoubian et al., 2025 ) . Among them, GRPO estimates advantages from group-relative rewards without requiring a separate critic, making it a strong and scalable baseline ( Shao et al., 2024 ) .

However, these methods typically assign a single scalar advantage uniformly to every token, so credit assignment remains coarse. Recent analyses have shown that this uniform assignment dilutes gradients across causally irrelevant tokens ( Khandoga et al., 2026 ) , hinders localization of semantic errors in near-correct programs ( Kumar et al., 2026 ) , and introduces bias that grows with sequence length ( Parthasarathi et al., 2025 ) . A complementary line of work seeks to improve credit assignment through process supervision or process reward models, which provide denser step-level signals derived from intermediate states or feedback ( Lightman et al., 2023 ; Setlur et al., 2025 ; Cui et al., 2025 ) . These approaches offer finer-grained guidance but usually require additional learned reward estimators. This trade-off motivates methods that provide denser supervision without introducing an additional reward model.

### A.2 On-Policy Distillation and Self-Distillation

Distillation transfers behavior from a teacher to a student by matching output distributions or intermediate representations ( Hinton et al., 2015 ; Kim and Rush, 2016 ; Sanh et al., 2019 ) . More recent on-policy distillation methods reduce train-test mismatch by training the student on its own trajectories while receiving teacher guidance on those same trajectories ( Agarwal et al., 2024 ; Gu et al., 2023 ; Lu and Lab, 2025 ) . Relative to reward-only RL, these methods provide denser supervision, but they typically rely on a separate and often stronger external teacher.

Self-distillation removes the need for an external teacher by supervising the model with a conditioned version of itself. Context distillation first showed that a model can internalize behavior induced by privileged context into its parameters ( Snell et al., 2022 ) . More recent work extends this idea to self-improvement and on-policy self-distillation settings, including learning from self-generated trajectories or richer conditioning information ( Mitra and Ulukus, 2025 ; Hübotter et al., 2025 ; Hübotter et al., 2026 ; Shenfeld et al., 2026 ; Zhao et al., 2026 ; Buening et al., 2026 ; Wang et al., 2026 ) . A representative example is SDPO ( Hübotter et al., 2026 ) , which samples rollouts from the current policy and distills the logit-level distribution of a feedback-conditioned self-teacher back into the same policy. However, feedback-conditioned on-policy self-distillation can exhibit late-stage degradation: concurrent work by Kim et al. (2026) attributes this to the suppression of epistemic verbalization, while our analysis (Section 1) traces it to ambiguity on correct samples and progressive degradation of the self-teacher signal.

Overall, prior RL-based post-training methods provide reward alignment but rely on coarse sequence-level supervision. Distillation-based methods provide denser logit-level guidance, and self-distillation removes the need for an external teacher, but feedback-conditioned on-policy self-distillation may suffer from sample-dependent ambiguity and degraded signal quality in later training. To address this gap, our work studies how reward-driven and self-distillation-based supervision can be combined within a unified framework based on sample routing, thereby leveraging the strengths of both post-training paradigms.

## Appendix B Experimental Details

### B.1 Technical Setup

All experiments were conducted on a single node equipped with 8 NVIDIA H20 GPUs interconnected via NVLink, providing a total of 768 GB VRAM. Our software environment uses GPU driver version 550.144.03, CUDA 12.4, and PyTorch 2.8.0.

Our implementation is based on the verl library ( Sheng et al., 2025 ) . We use PyTorch Fully Sharded Data Parallel (FSDP2) for distributed training across GPUs. For rollout generation, we employ SGLang ( Zheng et al., 2024 ) instead of the vLLM backend ( Kwon et al., 2023 ) used in the original SDPO implementation, as SGLang provides better compatibility with our environment. Since both engines implement the same sampling algorithms and support identical temperature, top- p p , and other decoding parameters, the choice of inference backend affects only throughput and does not alter the sampling, preserving a fair comparison with SDPO.

### B.2 Hyperparameters

Table 3 summarizes the hyperparameters for all three methods. For the two baselines (GRPO and SDPO), we directly adopt the configurations selected via grid search in the original SDPO work ( Hübotter et al., 2026 ) ; see that paper for details on the search procedure. For SRPO, we inherit all non-learning-rate hyperparameters from SDPO and set the learning rate to 5 × 10 − 6 5\times 10^{-6} , halfway between the GRPO and SDPO rates, to balance the reward-driven and self-distillation signals within a unified framework. The GRPO branch within SRPO uses the same loss-specific parameters as the standalone GRPO baseline, and the SDPO branch uses the same loss-specific parameters as the standalone SDPO baseline. The only additional hyperparameter introduced by SRPO is the dynamic-weighting temperature β \beta , which we set to 1 as default.

### B.3 Prompt Templates

We use the same prompt templates as SDPO ( Hübotter et al., 2026 ) without any modification, ensuring a fair comparison across all methods. The Science Q&A benchmarks (Chemistry, Physics, Biology, Materials) share a common multiple-choice format, while Tool Use follows a separate tool-calling format. We reproduce both templates below.

### B.4 Benchmark Details

We use the exact train/test splits provided in the official SDPO github repository to ensure full comparability. Table 4 summarizes the dataset statistics.

The four Science Q&A benchmarks are formatted as four-option single-choice questions targeting undergraduate-level scientific reasoning. Each question presents a problem statement (often involving domain-specific notation such as SMILES strings in Chemistry, physical equations in Physics, protein sequences in Biology, or crystal lattice parameters in Materials) followed by four candidate answers. The Tool Use benchmark pairs a natural-language user request with a tool-API specification (including function names, parameter schemas, and output types); the model must produce the correct tool call in a structured Thought / Action / Action Input format.

Table 5 shows one representative example from each benchmark.

### B.5 Teacher Information Construction

As described in Section 3, the SDPO branch requires teacher information f i f_{i} for each rollout y i y_{i} to construct the feedback-conditioned self-teacher distribution π θ ( ⋅ ∣ x , f i , y i , < t ) \pi_{\theta}(\cdot\mid x,f_{i},y_{i,<t}) . Following SDPO ( Hübotter et al., 2026 ) , we use successful sibling rollouts within the same group as teacher information. Since our experimental setting does not include rich environment feedback (e.g., runtime errors in coding tasks), the only available source of teacher information is a correct sibling rollout from the same prompt.

#### Construction procedure.

For each prompt x x , the policy generates a group of G = 8 G=8 rollouts { y 1 , … , y G } \{y_{1},\ldots,y_{G}\} . We identify all correct rollouts in the group (those with reward r i ≥ 0.5 r_{i}\geq 0.5 ). For each rollout y i y_{i} , the teacher information f i f_{i} is constructed as follows: 1. Collect the indices of all correct rollouts for the same prompt, excluding rollout i i itself (to prevent a sample from serving as its own teacher).

2. If at least one correct sibling exists, select one and use its full response text as the teacher information. The teacher prompt is then formatted as:

The self-teacher processes this enriched prompt concatenated with the student’s own response tokens y i , < t y_{i,<t} , producing a logit-level distribution at each position that serves as the distillation target. Crucially, the self-teacher does not generate a new response; it re-scores the student’s existing trajectory under the enriched context.

#### Illustrative example.

Consider a prompt with G = 8 G=8 rollouts, of which rollouts y 2 y_{2} and y 5 y_{5} are correct (reward = 1.0 =1.0 ) and the remaining six are incorrect (reward = 0.0 =0.0 ). Table 6 shows the resulting routing decision for representative rollouts.

#### Fallback to GRPO when no teacher information is available.

When all G G rollouts for a prompt are incorrect, no correct sibling exists, so m i = 0 m_{i}=0 for every rollout. By the routing rule z i SDPO = ( 1 − c i ) ​ m i z_{i}^{\mathrm{SDPO}}=(1-c_{i})\,m_{i} , all rollouts are assigned to the GRPO branch despite being incorrect. Notably, when a rollout is the only correct one in its group, it is excluded from being its own teacher , so m i = 0 m_{i}=0 for that rollout. Since it is correct ( c i = 1 c_{i}=1 ), it is routed to GRPO regardless. Table 7 summarizes the complete decision logic.

This design ensures that the SDPO branch is activated only when dense logit-level correction is both needed (the rollout is incorrect) and feasible (a correct sibling provides informative teacher context). In all other cases, the update falls back to GRPO’s reward-aligned advantage signal.

## Appendix C Routing Statistics Over Training

Figure 5 visualizes how the sample-routing composition of SRPO evolves over the course of training. At the beginning of training, approximately 40% of samples are routed to the SDPO branch and 60% to the GRPO branch, reflecting the substantial fraction of incorrect rollouts that benefit from dense logit-level correction. As training progresses and the policy improves, the fraction of correct rollouts increases, causing more samples to be routed to the GRPO branch.

This dynamic shift has two important implications. First, it provides direct empirical support for the adaptive mixing behavior described in Section 3.3. SDPO branch contributes a substantial share in the early stage, providing meaningful dense logit-level correction when the policy is weaker and incorrect rollouts are frequent. As training proceeds and the policy improves, this contribution gradually diminishes while an increasing share of samples is handled by the GRPO branch, whose reward-aligned advantages provide a more stable and unbiased optimization signal for already-correct rollouts. The net effect is that SRPO automatically modulates the influence of self-distillation—leveraging it most when it is most beneficial and changing it to reward-aligned reinforcement for stability as the policy matures—without requiring any manual scheduling of the mixing ratio.

Second, the decreasing SDPO fraction directly explains the compute-time trend observed in Section 4.4 (Figure 4 (b)): since the self-teacher log-probability computation is only performed for samples on the SDPO branch, the per-step overhead of this additional forward pass diminishes as fewer samples require it. This accounts for why SRPO’s per-step compute time decreases steadily over training and eventually falls below that of both standalone GRPO and SDPO.

Figure 5 (c) further shows that the fraction of samples with constructable teacher information remains high throughout training. This indicates that the fallback to GRPO due to teacher unavailability ( m i = 0 m_{i}=0 ) is relatively infrequent; the primary driver of the routing shift is the increasing correctness of rollouts ( c i = 1 c_{i}=1 ), not the absence of teacher information.

## Instructions for reporting errors

We are continuing to improve HTML versions of papers, and your feedback helps enhance accessibility and mobile support. To report errors in the HTML that will help us improve conversion and rendering, choose any of the methods listed below:

Click the "Report Issue" ( ) button, located in the page header.

Tip: You can select the relevant text first, to include it in your report.

Our team has already identified the following issues . We appreciate your time reviewing and reporting rendering errors we may not have found yet. Your efforts will help us improve the HTML versions for all readers, because disability should not be a barrier to accessing research. Thank you for your continued support in championing open access for all.

Have a free development cycle? Help support accessibility at arXiv! Our collaborators at LaTeXML maintain a list of packages that need conversion , and welcome developer contributions .
