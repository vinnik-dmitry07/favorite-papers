##### Report GitHub Issue

Content selection saved. Describe the issue below:

# Weight-Space Geometry of Offline Reasoning Training

###### Abstract

Offline reinforcement-learning losses (RFT, RIFT, DFT, Offline GRPO, DPO) are widely used to distill reasoning from large teachers into smaller students, and are typically compared on downstream accuracy alone. We ask whether they are mechanistically distinct or converge to a similar weight update. Training six methods (SFT, RFT, DFT, RIFT, Offline GRPO, DPO) on identical math rollouts from a single base model (Qwen3-4B) with attention-only LoRA, we analyze the resulting deltas via cosine similarity, principal-angle subspace analysis, linear mode connectivity, and CKA. We observe: (i) SFT, RFT, and RIFT have nearly colinear weight deltas (cosine ≥ 0.97 \geq 0.97 , top- 1 1 principal angle ∼ 7 ∘ {\sim}\!\!7^{\circ} median over 144 144 modules) and comparable GSM8K accuracy ( 87 87 – 88 % 88\% , n = 1319 n{=}1319 ; pairwise McNemar p ≥ 0.15 p\geq 0.15 ); (ii) DFT diverges further in direction than any reward-weighted method despite using the same data; (iii) Offline GRPO adds a substantial component orthogonal to the SFT direction ( ∼ 67 % \sim\!\!67\% globally, up to ∼ 86 % \sim\!\!86\% in late layers) while staying in the SFT loss basin; (iv) DPO sits in a near-orthogonal subspace, shows a mode-connectivity barrier, and collapses late-layer CKA to ∼ 0.46 \sim 0.46 . DPO also reaches the highest accuracy in our protocol on both GSM8K ( 93.5 % 93.5\% , McNemar p < 10 − 9 p<10^{-9} vs. each other method) and AIME26 ( 30.0 % 30.0\% vs. 3.3 3.3 – 10.0 % 10.0\% ); its training uses a 10 × 10\times smaller learning rate than the others (the standard convention), so the update-norm and accuracy gaps reflect loss-function and optimizer choices jointly, and a learning-rate-matched DPO comparison is left for future work.

###### Keywords:

## 1 Introduction

Reasoning distillation has become a standard recipe for teaching small models to solve math and code tasks: a strong teacher generates rollouts, and a student is trained on them with one of a rapidly growing list of offline objectives. The past year alone introduced RIFT ( Liu et al., 2026 ) , Offline GRPO ( KRAFTON AI, 2025 ) , DFT ( Wu and others, 2025 ) , LUFFY ( Yan et al., 2025 ) , and DAPO ( Yu and others, 2025 ) , alongside an established preference-learning family — DPO ( Rafailov et al., 2023 ) , KTO ( Ethayarajh et al., 2024 ) , IPO ( Azar et al., 2023 ) , and NCA ( Chen et al., 2024 ) — each accompanied by claims that its specific loss formulation is responsible for accuracy gains over plain SFT.

These methods are compared almost exclusively by benchmark accuracy. What they do to the model is unknown: do different losses produce weight updates that point in the same direction, or qualitatively different ones? The distinction matters for both practitioners (which loss is worth implementing?) and interpretability researchers (does “offline RL” name a single mechanism or a family?).

We present a controlled weight-space comparison of offline reasoning losses: identical rollouts, identical base model (Qwen3-4B-Instruct), shared LoRA initialization, six methods (DPO uses a smaller learning rate per its codebase convention, see § 2 ). Following recent weight-space studies of fine-tuning ( Arturi and others, 2025 ; Soligo and others, 2025 ; Zhong and Raghunathan, 2025 ; Ward and others, 2025 ) , we analyze each method’s LoRA delta Δ ​ W \Delta W rather than its outputs.

Our contributions are: (1) reward-weighted losses (SFT, RFT, RIFT) converge on essentially the same direction in weight space (cosine ≥ 0.97 \geq 0.97 ) and produce GSM8K accuracies that are non-different by exact McNemar’s test ( p ≥ 0.15 p\geq 0.15 , n = 1319 n{=}1319 ); (2) DFT, despite being a one-line modification of SFT, produces a more distinctive update than any explicitly reward-weighted method; (3) Offline GRPO adds a quantifiable orthogonal component (globally 67 % 67\% , rising to ∼ 80 % \sim\!\!80\% in late layers) while staying in the same loss basin as SFT/RIFT; (4) DPO sits in a near-orthogonal subspace with higher effective rank, a sharp linear-mode barrier, and reaches the highest pass@1 on both GSM8K and AIME26 in our protocol; we report this with the caveat that DPO uses a 10 × 10\times smaller learning rate, so the loss formulation and optimizer setting cannot be cleanly separated here.

## 2 Setup

#### Data.

All methods share one set of rollouts: DeepScaleR prompts ( ∼ 40 {\sim}40 k verified math ( Agentica, 2025 ) ), teacher DeepSeek-V4-Flash, K = 4 K{=}4 CoT completions/prompt, binary math-verify reward. Reference-policy methods use π base \pi_{\text{base}} . DPO consumes ∼ 1.8 {\sim}1.8 K (chosen, rejected) pairs vs. ∼ 75 {\sim}75 K rows for the rest. Identical rollouts is the central control.

#### Methods.

Table 1 summarizes the six losses. With ℓ i = − log ⁡ π θ ​ ( y i ∣ x ) \ell_{i}=-\log\pi_{\theta}(y_{i}\mid x) shorthand for the per-sequence NLL: SFT = ∑ i ℓ i =\sum_{i}\ell_{i} on all i i ; RFT ( Yuan et al., 2023 ) = ∑ i : r i = 1 ℓ i =\sum_{i:r_{i}=1}\ell_{i} on positives only; DFT ( Wu and others, 2025 ) = ∑ t sg ⁡ ( π θ ​ ( y t ∣ y < t , x ) ) ​ ℓ t tok =\sum_{t}\mathrm{sg}(\pi_{\theta}(y_{t}\mid y_{<t},x))\,\ell_{t}^{\text{tok}} down-weights confident tokens; RIFT ( Liu et al., 2026 ) = ∑ i ( 1 − r i ​ λ ) ​ ℓ i =\sum_{i}(1-r_{i}\,\lambda)\,\ell_{i} is a linear-in-reward surrogate that admits negatives; Offline GRPO ( KRAFTON AI, 2025 ; Shao et al., 2024 ) = ∑ i A ^ i ​ ℓ i =\sum_{i}\hat{A}_{i}\,\ell_{i} with A ^ i = r i − r ¯ g + b \hat{A}_{i}=r_{i}-\bar{r}_{g}+b ; DPO ( Rafailov et al., 2023 ) = − log ⁡ σ ⁡ ( β ⁡ [ log ⁡ π θ ​ ( y w ) π ref ​ ( y w ) − log ⁡ π θ ​ ( y l ) π ref ​ ( y l ) ] ) =-\log\sigma\!\left(\beta\,[\log\frac{\pi_{\theta}(y_{w})}{\pi_{\text{ref}}(y_{w})}-\log\frac{\pi_{\theta}(y_{l})}{\pi_{\text{ref}}(y_{l})}]\right) on (chosen y w y_{w} , rejected y l y_{l} ) pairs.

#### Training.

Qwen3-4B-Instruct-2507, LoRA on attention projections ( q,k,v,o_proj ; rank 32 32 , α = 64 \alpha{=}64 , dropout 0 0 ; 144 144 modules over 36 36 layers). Effective batch 32 32 , cosine schedule, 5 % 5\% warmup, wd 0.01 0.01 , grad-clip 1.0 1.0 , seed 42 42 , bf16. Peak LR × 10 − 6 5\!\times\!10^{-6} for all but DPO ( × 10 − 7 5\!\times\!10^{-7} , codebase convention; higher diverges). DPO: sigmoid loss, β = 0.1 \beta{=}0.1 ; Offline GRPO: additive bias 0.1 0.1 on the centered advantage, no probability weighting, no explicit KL. 1,500 1{,}500 steps; we report step 1,000 1{,}000 uniformly.

#### Analysis.

Let Δ ​ W ( m ) = B ( m ) ​ A ( m ) \Delta W^{(m)}=B^{(m)}A^{(m)} be the stacked LoRA delta of method m m . We measure: (i) global/per-layer cosine ⟨ Δ ​ W ( m ) , Δ ​ W ( m ′ ) ⟩ / ‖ Δ ​ W ( m ) ‖ ​ ‖ Δ ​ W ( m ′ ) ‖ \langle\Delta W^{(m)},\Delta W^{(m^{\prime})}\rangle/\|\Delta W^{(m)}\|\|\Delta W^{(m^{\prime})}\| ; (ii) per-layer SVD (effective rank, principal angles between top- k k subspaces); (iii) linear mode connectivity ( Frankle et al., 2020 ) : masked-answer CE on GSM8K along α ​ Δ ​ W ( m ) + ( 1 − α ) ​ Δ ​ W ( m ′ ) \alpha\Delta W^{(m)}+(1{-}\alpha)\Delta W^{(m^{\prime})} ; (iv) CKA ( Kornblith et al., 2019 ) of merged-model hidden states.

## 3 Results

### 3.1 Downstream accuracy

Figure 3 (appendix) reports greedy pass@1 on full GSM8K ( n = 1319 n{=}1319 ) and AIME26 ( n = 30 n{=}30 ). SFT/RFT/DFT/RIFT/Offline GRPO sit at 87.3 87.3 – 88.2 % 88.2\% on GSM8K, pairwise non-different by exact McNemar ( p ≥ 0.15 p\geq 0.15 ); DPO reaches 93.5 % 93.5\% ( p < 10 − 9 p<10^{-9} ). On AIME26 the ordering repeats but n = 30 n{=}30 is underpowered (SFT–DPO p = 0.07 p{=}0.07 ). DPO trains at a 10 × 10\times smaller LR with ∼ 40 × {\sim}40\times fewer rows, so we treat the gap as suggestive. Llama-3.2-3B replicates the geometry and the 5 5 – 7 7 point DPO accuracy edge.

#### On-policy RL preserves accuracy; SFT-style loses it.

Re-measuring greedy pass@1 for the on-policy methods (Table 2 , our adapters, same protocol) shows their reward-orthogonal updates (§ 3.4 ) do not cost accuracy: Online GRPO/DAPO and DPO all stay at the base instruct model’s 93 93 – 94 % 94\% on GSM8K, whereas SFT and Offline GRPO drop to ∼ 87 % {\sim}87\% (below base). Online GRPO is best on AIME26 ( 20.0 % 20.0\% ).

### 3.2 Weight-space convergence

Figure 1 shows the cosine similarity matrix between global LoRA deltas. Three regimes are visible. First , SFT, RFT, and RIFT form a tight cluster: the SFT–RFT, SFT–RIFT, and RFT–RIFT cosines are 0.977 0.977 , 0.967 0.967 , 0.969 0.969 . Filtering negatives (RFT) and reward-weighting them (RIFT) does not measurably change the direction of the update relative to plain SFT on the union; it only adjusts the step size, with ‖ Δ ​ W ‖ F \|\Delta W\|_{F} ranging from 2.82 2.82 (RFT) to 3.04 3.04 (RIFT). Second , DFT, which differs from SFT by a single multiplicative factor on the loss, sits at cosine 0.572 0.572 to SFT and 0.536 0.536 to RIFT — a larger directional change than any explicitly reward-weighted method. Third , DPO is orthogonal to everything: cosine to SFT, RFT, and RIFT all fall in [ 0.057 , 0.065 ] [0.057,0.065] . Offline GRPO occupies an intermediate position (cosine ≈ 0.74 \approx 0.74 to the SFT cluster).

The per-layer view (Figure 4 ) decomposes this further. SFT/RFT/RIFT pairs are essentially flat above 0.95 0.95 at every layer. SFT–GRPO drops gradually with depth. SFT–DFT is bimodal — close to 1 1 at certain bottleneck layers and well below 0.5 0.5 at others. SFT–DPO hovers near zero throughout. The visible drop on layers 34 34 – 36 36 across all pairs reflects the small-norm tail of LoRA updates in the last decoder block; we treat this as a LoRA artifact rather than a finding.

### 3.3 Subspace analysis

Per-layer SVD lets us go beyond a single direction and ask whether two methods adapt the same low-dimensional subspace. We report principal angles between the top- 10 10 left singular vectors of each Δ ​ W ( m ) \Delta W^{(m)} at the same module. Smaller angles mean shared subspace.

Aggregating across all 144 144 attention modules (top- 10 10 left singular vectors per module), median top- 1 1 principal angles are 6.7 ∘ 6.7^{\circ} (SFT–RFT), 8.2 ∘ 8.2^{\circ} (SFT–RIFT), 18.5 ∘ 18.5^{\circ} (SFT–Offline GRPO), 26.7 ∘ 26.7^{\circ} (SFT–DFT), and 54.6 ∘ 54.6^{\circ} (SFT–DPO); the median worst (top- 10 10 ) angles are 36 ∘ 36^{\circ} , 40 ∘ 40^{\circ} , 76 ∘ 76^{\circ} , 85 ∘ 85^{\circ} , 90 ∘ 90^{\circ} in the same order. SFT–DPO IQR for the worst angle is [ 89.6 ∘ , 89.8 ∘ ] [89.6^{\circ},89.8^{\circ}] : essentially every module is orthogonal at every singular index. The reward-weighted cluster shares the top of its subspace with SFT to within ∼ 10 ∘ {\sim}\!\!10^{\circ} ; GRPO and DFT partially overlap; DPO does not.

The effective rank, averaged over all 144 144 modules, is ∼ 16 \sim 16 for SFT, RFT, DFT, and RIFT, 14.8 14.8 for Offline GRPO, and 24.5 24.5 for DPO. DPO writes into a higher-dimensional subspace, but, given its 13 × 13\times smaller Frobenius norm, with much smaller singular values; together with the orthogonality to SFT, this suggests DPO learns a different decomposition of the same projection matrices rather than a low-rank refinement of SFT.

To quantify how much of Offline GRPO’s update is genuinely new direction, we project Δ ​ W grpo \Delta W^{\mathrm{grpo}} onto the SFT direction at every adapted module and report ‖ Δ ​ W grpo − Π sft ​ Δ ​ W grpo ‖ F / ‖ Δ ​ W grpo ‖ F \|\Delta W^{\mathrm{grpo}}-\Pi_{\mathrm{sft}}\Delta W^{\mathrm{grpo}}\|_{F}/\|\Delta W^{\mathrm{grpo}}\|_{F} . Globally this is 0.67 0.67 ; per layer it grows from ∼ 0.55 \sim\!\!0.55 in middle blocks to 0.79 0.79 – 0.86 0.86 in the final five blocks — the same layers where CKA diverges (Section 3.6 ).

#### Top-1 singular directions.

The rank-1 approximation Δ ​ W ≈ σ 1 ​ u 1 ​ v 1 ⊤ \Delta W\approx\sigma_{1}u_{1}v_{1}^{\top} isolates the single most important output direction u 1 u_{1} each loss writes into. Mean | ⟨ u 1 m , u 1 m ′ ⟩ | |\langle u_{1}^{m},u_{1}^{m^{\prime}}\rangle| over 144 144 modules is 0.97 0.97 – 0.98 0.98 within SFT/RFT/RIFT, 0.78 0.78 – 0.80 0.80 to Offline GRPO, 0.64 0.64 – 0.67 0.67 to DFT, and 0.11 0.11 to DPO. Right singular vectors v 1 v_{1} (input directions) converge much more tightly: 0.99 0.99 – 1.00 1.00 for non-DPO pairs, 0.94 0.94 for DFT, 0.66 0.66 – 0.70 0.70 for DPO. All methods (except DPO) read from nearly the same input subspace; they differ in how they transform it.

### 3.4 Seed and learning-rate sensitivity

The colinearity above is at a single seed, conflating loss agreement with shared-init agreement. We disentangle by training each loss at two seeds ( 42,123 42,123 ) and three LRs ( × 10 − 7 . . − 5 5\!\times\!10^{-7..-5} ); Δ ​ W = ( α / r ) ​ B ​ A \Delta W=(\alpha/r)BA is gauge-invariant, so its cosine is genuine.

Seed rotates Δ ​ W \Delta W more than the loss — but only on the input side. At a fixed seed SFT–RFT are colinear (cosine 0.996 0.996 , angle 3.7 ∘ 3.7^{\circ} ), yet the same loss at two seeds has cosine only 0.07 0.07 ( × 10 − 7 5\!\times\!10^{-7} )– 0.36 0.36 ( × 10 − 5 5\!\times\!10^{-5} ). Cause: LoRA’s random A A init — across seeds the top- 1 1 output direction u 1 u_{1} still agrees at 0.99 0.99 while the input direction v 1 v_{1} agrees at 0.07 0.07 (median top- 8 8 angle 26 ∘ 26^{\circ} vs. 76 ∘ 76^{\circ} for unrelated runs). Functionally the seeds are the same solution: interpolating their deltas shows no barrier (midpoint + 0.004 +0.004 ). So the cross-method colinearity is partly shared-init, but convergence onto a common output subspace is seed-robust (Figure 2 ).

Learning rate changes direction, not just magnitude. A 10 × 10\times LR step rotates Δ ​ W \Delta W (cosine ≈ 0.55 \approx 0.55 ) and grows its norm only ∼ 3 × \sim\!3\times — not a pure rescaling, which sharpens the caveat on the 10 × 10\times -smaller-LR DPO comparison.

Online GRPO is far more orthogonal than offline GRPO. We also train online GRPO under the same LoRA recipe (on-policy rollouts, group-relative advantage, math_verify reward; 600 600 steps, 8 8 generations/prompt, lr × 10 − 6 5\!\times\!10^{-6} , seed 42 42 ) — the comparison the original protocol could not produce. The resulting update is almost entirely orthogonal to the SFT/RFT cluster: cosine 0.025 0.025 to SFT and 0.024 0.024 to RFT, with an orthogonal fraction of 0.998 0.998 off the SFT direction (Figure 1 ), versus 0.67 0.67 for offline GRPO (§ 3.2 ). Its Frobenius norm is ∼ 10 × \sim\!10\times smaller than SFT’s at the same LR ( 0.30 0.30 vs. 2.84 2.84 ), echoing the small-norm regime of DPO. On-policy sampling thus moves the update off the shared SFT subspace far more than the offline group-relative loss does, indicating that the SFT/offline-RL directional convergence is partly a consequence of training on the same fixed rollouts : replacing them with on-policy samples largely breaks it.

### 3.5 Linear mode connectivity

We linearly interpolate LoRA deltas, merge into the base, and measure the per-token cross-entropy of the gold \ 𝚋𝚘𝚡𝚎𝚍 ​ { 𝚊𝚗𝚜𝚠𝚎𝚛 } \backslash\mathtt{boxed\{answer\}} continuation right after the prompt on GSM8K. The metric is length-sensitive: DPO produces longer, structured CoTs (median 5100 5100 vs 1100 1100 chars on correct AIME26; verification steps in 9 / 9 9/9 correct DPO solutions vs 0 / 3 0/3 SFT), inflating per-token NLL of the bare boxed answer. Offline GRPO → \to RIFT improves monotonically ( 4.93 → 2.25 4.93\to 2.25 ) and SFT → \to Offline GRPO worsens monotonically ( 2.06 → 4.93 2.06\to 4.93 ): one basin. RIFT → \to DPO shows a sharp non-monotonic barrier above α = 0.5 \alpha{=}0.5 ( 3.82 → 7.06 → 8.64 3.82\to 7.06\to 8.64 ): even discounting length, linear interpolation destroys the solution.

### 3.6 Representational similarity

CKA on hidden states (Figure 6 , 100 100 GSM8K prompts) confirms the weight-space picture. SFT–RIFT CKA stays above 0.99 0.99 at every layer; SFT/RIFT–Offline GRPO drop to ∼ 0.85 \sim 0.85 in the final layer (GRPO reshapes output-facing layers); Offline GRPO–DPO and DFT–DPO start near 0.93 0.93 and collapse to ∼ 0.45 \sim\!\!0.45 from layer 25 25 onward. A logit-lens probe gives a complementary null — mean prediction depth is 35.3 35.3 – 36.0 36.0 out of 36 36 for every method — but this is partly forced by attention-only LoRA leaving MLPs frozen, so it should not be read as a finding about the losses.

## 4 Discussion

#### Reward-weighted MLE is SFT, plus DFT is the surprise.

SFT, RFT, and RIFT differ only in how they handle negative samples (drop, weight, or include uniformly), yet the resulting LoRA deltas have cosine ≥ 0.97 \geq 0.97 , principal angles < 25 ∘ <25^{\circ} , and indistinguishable per-layer CKA, and they sit within 1 1 percentage point of each other on full GSM8K. The Frobenius norms differ by up to 7 % 7\% . If RIFT outperforms SFT at the same step count, our results suggest the explanation lies in magnitude (effective step size in the SFT direction), not direction — a longer or higher-lr SFT run should close the gap. DFT, by contrast, has cosine ∼ 0.55 \sim 0.55 to SFT/RIFT despite using less information than they do (no reward, no filtering): self-weighting by sg ⁡ ( π θ ) \mathrm{sg}(\pi_{\theta}) reweights which examples drive the update in a way explicit reward does not, yet leaves the loss basin unchanged.

#### Offline GRPO shifts direction but stays in basin; online GRPO does not.

Among offline rewards, only Offline GRPO substantially shifts direction from SFT (cosine 0.73 0.73 ; orthogonal-fraction 0.67 0.67 , ∼ 0.8 \sim\!\!0.8 late; angles up to 59 ∘ 59^{\circ} ), yet barrier-free interpolations keep it in the SFT/RIFT basin. Online GRPO goes much further — orthogonal fraction 0.998 0.998 (Figure 1 ) — so the SFT/offline-RL convergence is partly an artifact of shared fixed rollouts, which on-policy sampling breaks.

#### DPO sits apart, geometrically and on accuracy.

DPO occupies a near-orthogonal subspace ( 74 ∘ 74^{\circ} – 89 ∘ 89^{\circ} ), a higher-rank update with much smaller Frobenius norm, a sharp linear-mode barrier, and late-layer CKA ∼ 0.45 \sim 0.45 ; it also reaches the highest pass@1 on GSM8K ( 93.5 % 93.5\% ) and AIME26 ( 30.0 % 30.0\% ). It trains at a 10 × 10\times smaller LR, so its norm/accuracy gaps are entangled with the optimizer — correlation worth a LR-matched follow-up, not a causal claim. Extending the weight-space view to the wider contrastive family (IPO, KTO, SimPO, Cal-DPO) is left open.

#### Limitations.

Single domain and checkpoint; attention-only LoRA; greedy-only on small AIME26 ( n = 30 n{=}30 ). DPO uses 10 × 10\times smaller LR and ∼ 40 × {\sim}40\times fewer rows, so its norm/accuracy gaps are entangled with the optimizer. Online GRPO is reported at lr × 10 − 6 5\!\times\!10^{-6} , seed 42 42 (§ 3.4 ); the remaining LR/seed cells, a matched accuracy comparison, and calibrated DPO variants (KTO, IPO, SimPO) are left to a fuller sweep. Code, adapters, and analysis scripts are released.

## References

Agentica (2025) Agentica DeepScaleR-Preview-Dataset: a 40k reasoning-intensive mathematics corpus . Note: https://huggingface.co/datasets/agentica-org/DeepScaleR-Preview-Dataset Cited by: §2 .

Arturi et al. (2025) Arturi et al. Shared parameter subspaces in emergently misaligned behavior . In NeurIPS Workshop on Mechanistic Interpretability , Cited by: §1 .

Azar et al. (2023) M. G. Azar, M. Rowland, B. Piot, D. Guo, D. Calandriello, M. Valko, and R. Munos A general theoretical paradigm to understand learning from human preferences . arXiv preprint arXiv:2310.12036 . Cited by: §1 .

Chen et al. (2024) H. Chen, G. Zhao, S. Zhang, H. Li, J. Zhu, and J. Sun Noise contrastive alignment of language models with explicit rewards . In Advances in Neural Information Processing Systems , Cited by: §1 .

Ethayarajh et al. (2024) K. Ethayarajh, W. Xu, N. Muennighoff, D. Jurafsky, and D. Kiela KTO: model alignment as prospect theoretic optimization . In International Conference on Machine Learning , Cited by: §1 .

Frankle et al. (2020) J. Frankle, G. K. Dziugaite, D. M. Roy, and M. Carbin Linear mode connectivity and the lottery ticket hypothesis . In International Conference on Machine Learning , Cited by: §2 .

Kornblith et al. (2019) S. Kornblith, M. Norouzi, H. Lee, and G. Hinton Similarity of neural network representations revisited . In International Conference on Machine Learning , Cited by: §2 .

KRAFTON AI (2025) KRAFTON AI Offline GRPO for reasoning distillation . Note: Technical blog post and codebase https://github.com/krafton-ai/offline-grpo Cited by: §1 , §2 .

Liu et al. (2026) Z. Liu, S. Liu, T. Zhong, and M. Yuan RIFT: repurposing negative samples via reward-informed fine-tuning . arXiv preprint arXiv:2601.09253 . Cited by: §1 , §2 .

Rafailov et al. (2023) R. Rafailov, A. Sharma, E. Mitchell, S. Ermon, C. D. Manning, and C. Finn Direct preference optimization: your language model is secretly a reward model . In Advances in Neural Information Processing Systems , Cited by: §1 , §2 .

Shao et al. (2024) Z. Shao, P. Wang, Q. Zhu, R. Xu, J. Song, X. Bi, H. Zhang, M. Zhang, Y. K. Li, Y. Wu, and D. Guo DeepSeekMath: pushing the limits of mathematical reasoning in open language models . arXiv preprint arXiv:2402.03300 . Cited by: §2 .

Soligo et al. (2025) Soligo et al. Convergent linear representations of emergent misalignment . In NeurIPS Workshop on Mechanistic Interpretability , Cited by: §1 .

Ward et al. (2025) Ward et al. Rank-1 LoRAs encode interpretable reasoning signals . In NeurIPS Workshop on Mechanistic Interpretability , Cited by: §1 .

Wu et al. (2025) Y. Wu et al. On the generalization of SFT: a reinforcement learning perspective with reward rectification . arXiv preprint arXiv:2508.05629 . Cited by: §1 , §2 .

Yan et al. (2025) J. Yan, Y. Li, Z. Hu, Z. Wang, G. Cui, X. Qu, Y. Cheng, and Y. Zhang Learning to reason under off-policy guidance . arXiv preprint arXiv:2504.14945 . Cited by: §1 .

Yu et al. (2025) Q. Yu et al. DAPO: an open-source LLM reinforcement learning system at scale . arXiv preprint arXiv:2503.14476 . Cited by: §1 .

Yuan et al. (2023) Z. Yuan, H. Yuan, C. Li, G. Dong, K. Lu, C. Tan, C. Zhou, and J. Zhou Scaling relationship on learning mathematical reasoning with large language models . arXiv preprint arXiv:2308.01825 . Cited by: §2 .

Zhong and Raghunathan (2025) Zhong and Raghunathan Watch the weights: unsupervised monitoring and control of fine-tuned llms . In NeurIPS Workshop on Mechanistic Interpretability , Cited by: §1 .

## Appendix A Supplementary figures

## Instructions for reporting errors

We are continuing to improve HTML versions of papers, and your feedback helps enhance accessibility and mobile support. To report errors in the HTML that will help us improve conversion and rendering, choose any of the methods listed below:

Click the "Report Issue" ( ) button, located in the page header.

Tip: You can select the relevant text first, to include it in your report.

Our team has already identified the following issues . We appreciate your time reviewing and reporting rendering errors we may not have found yet. Your efforts will help us improve the HTML versions for all readers, because disability should not be a barrier to accessing research. Thank you for your continued support in championing open access for all.

Have a free development cycle? Help support accessibility at arXiv! Our collaborators at LaTeXML maintain a list of packages that need conversion , and welcome developer contributions .
