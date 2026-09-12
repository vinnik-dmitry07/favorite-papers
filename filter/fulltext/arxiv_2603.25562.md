##### Report GitHub Issue

Content selection saved. Describe the issue below:

# Revisiting On-Policy Distillation: Empirical Failure Modes and Simple Fixes

###### Abstract

On-policy distillation (OPD) is increasingly used in LLM post-training because it can leverage a teacher model to provide dense supervision on student rollouts. The standard implementation, however, usually reduces distribution matching to a sampled-token log-ratio, which can make the learning signal fragile on long rollouts whose prefixes drift away from the teacher’s typical support. We revisit this formulation from both theoretical and implementation perspectives. Theoretically, token-level OPD is biased relative to sequence-level reverse-KL minimization, but admits a substantially tighter worst-case variance bound; a controlled synthetic study further shows that stronger future-reward coupling increases gradient variance and destabilizes training. Empirically, we identify three failure modes of sampled-token OPD: imbalanced token-level supervision, unreliable teacher guidance on student-generated prefixes, and tokenizer or special-token mismatch. These findings motivate teacher top- K K local support matching, a truncated reverse-KL objective that compares teacher and student distributions over a teacher-supported token set at each prefix, together with top- p p rollout sampling and special-token masking. Across single-task reasoning and multi-task benchmarks spanning agentic and reasoning settings, this objective improves optimization stability and yields a +19.8% performance gain over standard sampled-token OPD baselines, providing a practical recipe for more stable on-policy distillation.

## 1 Introduction

On-policy distillation (OPD) is becoming an increasingly common component of LLM post-training, especially for reasoning and agentic models. Recent public reports from Thinking Machines Lab ( Lu and Lab, 2025 ) , Qwen3 ( Yang et al., 2025 ) , MiMo-V2-Flash ( Xiao et al., 2026 ) , and GLM-5 ( Zeng et al., 2026 ) suggest a broader shift toward supervision on model-generated trajectories, or closely related on-policy variants, alongside off-policy distillation and reinforcement learning. By training on student rollouts while evaluating them with a stronger teacher, OPD combines on-policy data collection with dense token-level feedback at relatively low cost ( Agarwal et al., 2024 ; Gu et al., 2024 ) . This profile is attractive in practical post-training pipelines, where training efficiency matters and models often need to combine or recover capabilities across domains and training stages ( Xiao et al., 2026 ; Zeng et al., 2026 ; Wang et al., 2026a ; DeepSeek-AI, 2026 ) .

Most OPD implementations in current LLM pipelines use a token-level estimator, even though it is biased relative to sequence-level reverse-KL ( Lu and Lab, 2025 ) . A basic reason is that sequence-level objectives couple each token update to many future rewards, which can make optimization substantially noisier in long-horizon settings. We make this trade-off explicit: token-level OPD removes future-reward coupling and is therefore biased, yet it admits more favorable worst-case variance scaling. Our toy experiment shows the same pattern empirically, with stronger future coupling leading to higher gradient variance and less stable optimization. This suggests a practical design principle for long-horizon training: keep supervision token-level to control variance.

In current LLM pipelines, this token-level objective is usually instantiated by sampled-token comparison: at each training step, the update is driven by the teacher–student log-probability difference on the sampled token ( Lu and Lab, 2025 ; Xiao et al., 2026 ) . This implementation is simple and efficient, but its learning signal can become brittle once rollouts grow long. Gu et al. (2024) report degraded outputs such as repetition, which is consistent with our observations. Recent work also reports entropy collapse under sampled-token OPD in certain cases ( Ko et al., 2026 ; Jin et al., 2026b ) . More recently, full-vocabulary distillation has been reported to outperform sampled-token variants in some settings ( Zhao et al., 2026 ; DeepSeek-AI, 2026 ) , suggesting that the one-token formulation can leave useful teacher information unused.

Our empirical analysis shows that this brittleness stems from several recurring failure modes. In particular, we identify two objective-level issues: the one-token signal is often highly imbalanced, and teacher guidance can become unreliable on student-generated prefixes. We also observe an additional implementation-level issue from tokenizer or special-token mismatch, which can further distort one-token comparisons. Taken together, these results point to a practical question: how can we retain the variance advantage of token-level OPD while making its supervision signal less brittle in practice?

The analysis above suggests a targeted modification of the standard sampled-token objective. We replace one-token supervision with teacher top- K K local support matching, where teacher and student are compared over a teacher-supported token subset at each prefix rather than only on the sampled token. We implement this objective as truncated reverse-KL, together with top- p p rollout sampling and special-token masking. The resulting update remains local and inexpensive, while providing a less brittle training signal.

Overall, our main contributions are as follows: • We clarify the theoretical trade-off in OPD: token-level OPD is biased relative to sequence-level OPD, but has substantially better worst-case variance scaling with sequence length, making it attractive for long-horizon LLM post-training.

• We present an empirical analysis of why sampled-token OPD can be unstable in practice, highlighting two recurring objective-level issues—imbalanced one-token supervision and unreliable teacher guidance on student-generated prefixes—along with an additional implementation issue from tokenizer or special-token mismatch.

• We propose teacher top- K K local support matching as an analysis-driven revision of sampled-token OPD, implemented with truncated reverse-KL, top- p p rollouts, and special-token masking, and show that it yields more stable optimization and stronger empirical performance than sampled-token OPD in single-task math reasoning and multi-task agentic-plus-reasoning training.

## 2 Understanding Sampled-Token OPD: Trade-offs and Failure Modes

### 2.1 From reverse-KL to token-level OPD

On-policy distillation aims to transfer the capabilities of a stronger teacher model into a student model by minimizing the reverse-KL from the student to the teacher. For a prompt x x , the OPD objective is J OPD ( θ ) = 𝔼 x ∼ D [ D KL ( π θ ( ⋅ ∣ x ) ∥ q ( ⋅ ∣ x ) ) ] , J_{\mathrm{OPD}}(\theta)=\mathbb{E}_{x\sim D}\left[D_{\mathrm{KL}}\left(\pi_{\theta}(\cdot\mid x)\,\|\,q(\cdot\mid x)\right)\right], where π θ \pi_{\theta} and q q denote the student and teacher models, respectively. Its gradient can be written as ∇ θ J OPD ( θ ) = 𝔼 x , y ∼ π θ ( ⋅ ∣ x ) [ ( log π θ ( y ∣ x ) − log q ( y ∣ x ) ) ∇ θ log π θ ( y ∣ x ) ] . \nabla_{\theta}J_{\mathrm{OPD}}(\theta)=\mathbb{E}_{x,\,y\sim\pi_{\theta}(\cdot\mid x)}\left[\big(\log\pi_{\theta}(y\mid x)-\log q(y\mid x)\big)\,\nabla_{\theta}\log\pi_{\theta}(y\mid x)\right]. For each decoding step t t , let c t = ( x , y < t ) c_{t}=(x,y_{<t}) denote the prefix context, and define s t = ∇ θ ​ log ​ π θ ​ ( y t ∣ c t ) , r t = log ⁡ π θ ​ ( y t ∣ c t ) q ⁡ ( y t ∣ c t ) . s_{t}=\nabla_{\theta}\log\pi_{\theta}(y_{t}\mid c_{t}),\qquad r_{t}=\log\frac{\pi_{\theta}(y_{t}\mid c_{t})}{q(y_{t}\mid c_{t})}. Using the autoregressive factorization log ⁡ π θ ​ ( y ∣ x ) − log ⁡ q ⁡ ( y ∣ x ) = ∑ t ′ = 1 T r t ′ , ∇ θ ​ log ​ π θ ​ ( y ∣ x ) = ∑ t = 1 T s t , \log\pi_{\theta}(y\mid x)-\log q(y\mid x)=\sum_{t^{\prime}=1}^{T}r_{t^{\prime}},\qquad\nabla_{\theta}\log\pi_{\theta}(y\mid x)=\sum_{t=1}^{T}s_{t}, we obtain the sequence-level estimator g ^ seq = ∑ t = 1 T ( ∑ t ′ = 1 T r t ′ ) ​ s t . \hat{g}_{\mathrm{seq}}=\sum_{t=1}^{T}\left(\sum_{t^{\prime}=1}^{T}r_{t^{\prime}}\right)s_{t}. (1) For t ′ < t t^{\prime}<t , we have 𝔼 ⁡ [ r t ′ ​ s t ] = 0 \mathbb{E}[r_{t^{\prime}}s_{t}]=0 , because r t ′ r_{t^{\prime}} depends only on the prefix before step t t , while 𝔼 [ s t ∣ x , y < t ] = ∑ y t π θ ( y t ∣ c t ) ∇ θ log π θ ( y t ∣ c t ) = 0 . \mathbb{E}[s_{t}\mid x,y_{<t}]=\sum_{y_{t}}\pi_{\theta}(y_{t}\mid c_{t})\,\nabla_{\theta}\log\pi_{\theta}(y_{t}\mid c_{t})=0. The same gradient can therefore be expressed in causal reward-to-go form 𝔼 ⁡ [ g ^ seq ] = 𝔼 ⁡ [ ∑ t = 1 T ( ∑ t ′ = t T r t ′ ) ​ s t ] , \mathbb{E}[\hat{g}_{\mathrm{seq}}]=\mathbb{E}\left[\sum_{t=1}^{T}\left(\sum_{t^{\prime}=t}^{T}r_{t^{\prime}}\right)s_{t}\right], where each token update is coupled to all future rewards along the trajectory.

Another approximation in LLM training retains only the immediate term at each position g ^ tok = ∑ t = 1 T r t ​ s t . \hat{g}_{\mathrm{tok}}=\sum_{t=1}^{T}r_{t}s_{t}. (2) We refer to Eq. ( 2 ) as the token-level estimator. This approximation removes future-reward coupling, so the update for token y t y_{t} depends only on its immediate reward. Consequently, it is biased relative to the sequence-level reverse-KL estimator, but exhibits lower variance in long-horizon settings. Under bounded rewards and bounded gradients, the worst-case variance upper bound of token-level OPD scales as O ⁡ ( T 2 ) O(T^{2}) , whereas the sequence-level estimator scales as O ⁡ ( T 4 ) O(T^{4}) . We provide a detailed derivation in Appendix D . To interpolate between these extremes, we consider the discounted return-to-go estimator g ^ γ = ∑ t = 1 T ( ∑ t ′ = t T γ t ′ − t ​ r t ′ ) ​ s t . γ ∈ [ 0 , 1 ] \hat{g}_{\gamma}=\sum_{t=1}^{T}\left(\sum_{t^{\prime}=t}^{T}\gamma^{t^{\prime}-t}r_{t^{\prime}}\right)s_{t}.\qquad\gamma\in[0,1] (3) The case γ = 0 \gamma=0 recovers token-level OPD, while γ = 1 \gamma=1 recovers the causal sequence-level estimator. We further validate this trade-off in a two-task toy experiment (Figure 1 ): stronger future coupling leads to substantially higher gradient variance and less stable optimization. This motivates our focus on token-level supervision in the remainder of the paper, where the main question becomes how to improve its local training signal in practical LLM settings. Additional experimental details are provided in Appendix E .

### 2.2 Why sampled-token OPD is brittle in practice

Although token-level OPD is appealing from a bias–variance perspective, the standard sampled-token formulation can be brittle in practice. We isolate three failure modes: (1) a highly imbalanced token-level distillation signal, (2) unreliable teacher guidance on student-generated prefixes, and (3) distortions introduced by tokenizer or special-token mismatch. These observations come from sampled-token OPD experiments on math reasoning, using Qwen2.5-7B-Instruct ( Qwen et al., 2024 ) as the student and OpenThinker3-7B ( Guha et al., 2025 ) , an SFT model built on Qwen2.5-7B-Instruct, as the teacher.

##### A highly imbalanced sampled-token signal.

In sampled-token OPD, the update at step t t is driven by the log-ratio on a single sampled token: log ⁡ q ⁡ ( y t ∣ c t ) − log ⁡ π θ ​ ( y t ∣ c t ) . \log q(y_{t}\mid c_{t})-\log\pi_{\theta}(y_{t}\mid c_{t}). Negative rewards arise whenever the student assigns higher probability to a sampled token than the teacher. As shown in Figure 2 , most sampled tokens receive negative reward. This leaves optimization dominated by a small subset of locally positive tokens, so training becomes sensitive to high-frequency fillers and short continuations that can receive favorable local scores while contributing little to trajectory-level quality.

##### The teacher signal can become unreliable on student-generated prefixes.

Sampled-token OPD assumes that teacher probability on a student-generated token is a useful proxy for trajectory quality. This proxy becomes unreliable on prefixes that are common under the student but uncommon for the teacher. In such regions, tokens with high teacher probability can remain rewarded even after the trajectory has drifted into repetition, self-resetting reasoning, or other meaningless continuations (Figure 3 ; Appendix H ). This creates an objective mismatch between token-level teacher agreement and trajectory-level quality.

We hypothesize that two factors amplify this issue: sharp teacher distributions, where modest teacher–student mismatch can produce large log-ratio values, and growing teacher–student divergence along long rollouts. Consistent with this view, Figure 4 shows that the distribution of teacher–student gaps becomes wider later in the sequence.

##### Tokenizer and special-token mismatch.

Sampled-token OPD compares the exact token generated by the student using the teacher distribution. When the two models use different tokenizations, the same raw text can be segmented differently, so a student-generated token may not correspond to a natural token under the teacher ( Boizard et al., 2025 ; Patiño et al., 2025 ; Minixhofer et al., 2025 ) . For example, the student may generate ‘<think>’ as ‘<’, ‘think’, ‘>’ , while the teacher expects ‘<th’, ‘ink’, ‘>’ . Then token ‘<’ receives low probability from the teacher, even though both models produce the same semantic content. Similar mismatches arise for special tokens such as end-of-sequence markers. In this setting, a one-token comparison confuses semantic disagreement with tokenizer mismatch. Since supervision is applied on a single token, such mismatch can distort the reward signal.

These observations motivate moving beyond one-token supervision: instead of comparing only the sampled token, we compare teacher and student over a set of teacher-supported next-token continuations at each prefix, while retaining token-level updates for stability.

## 3 Method

Our method is designed as a direct response to the failure modes above: it retains token-level OPD, but replaces one-token supervision with a distribution-level comparison over a teacher-selected support set at each prefix. This yields a truncated reverse-KL objective that preserves the efficiency of local updates while reducing dependence on any single sampled token. Section 3.1 introduces the objective, and Section 3.2 describes the practical choices that ensure stable training.

### 3.1 Teacher top- K K local support matching

Instead of comparing teacher and student on a single sampled token, we compare their next-token distributions over a teacher-defined local support set. A natural starting point is the full-vocabulary reverse-KL at prefix c t c_{t} : ℒ full ​ ( c t ) = ∑ v ∈ 𝒱 π θ ​ ( v ∣ c t ) ​ log ⁡ π θ ​ ( v ∣ c t ) q ⁡ ( v ∣ c t ) . \mathcal{L}_{\mathrm{full}}(c_{t})=\sum_{v\in\mathcal{V}}\pi_{\theta}(v\mid c_{t})\log\frac{\pi_{\theta}(v\mid c_{t})}{q(v\mid c_{t})}. (4) Sampled-token OPD can be viewed as a Monte Carlo approximation to this quantity: ℒ sample ( c t , y t ) = log π θ ​ ( y t ∣ c t ) q ⁡ ( y t ∣ c t ) , y t ∼ π θ ( ⋅ ∣ c t ) . \mathcal{L}_{\mathrm{sample}}(c_{t},y_{t})=\log\frac{\pi_{\theta}(y_{t}\mid c_{t})}{q(y_{t}\mid c_{t})},\qquad y_{t}\sim\pi_{\theta}(\cdot\mid c_{t}). (5) This approximation is computationally attractive, but it concentrates the entire update on a single sampled token. We instead compare teacher and student over a teacher-supported candidate set at each prefix.

For each prompt x x , we sample a group of outputs { o i } i = 1 G \{o_{i}\}_{i=1}^{G} using the student inference policy. Let c i , t = ( x , y i , < t ) c_{i,t}=(x,y_{i,<t}) be the prefix at position t t of output o i o_{i} , and define the teacher support set S ⁡ ( c i , t ) = TopK q ​ ( c i , t ) , S(c_{i,t})=\mathrm{TopK}_{q}(c_{i,t}), (6) which contains the K K highest-probability tokens under the teacher at that prefix.

Within this support, we renormalize both teacher and student distributions: π ^ θ ​ ( v ∣ c i , t ) = π θ ​ ( v ∣ c i , t ) ∑ u ∈ S ⁡ ( c i , t ) π θ ​ ( u ∣ c i , t ) , q ^ ​ ( v ∣ c i , t ) = q ⁡ ( v ∣ c i , t ) ∑ u ∈ S ⁡ ( c i , t ) q ⁡ ( u ∣ c i , t ) . \hat{\pi}_{\theta}(v\mid c_{i,t})=\frac{\pi_{\theta}(v\mid c_{i,t})}{\sum_{u\in S(c_{i,t})}\pi_{\theta}(u\mid c_{i,t})},\qquad\hat{q}(v\mid c_{i,t})=\frac{q(v\mid c_{i,t})}{\sum_{u\in S(c_{i,t})}q(u\mid c_{i,t})}. (7) Our local support matching (LSM) objective averages the truncated reverse-KL over all rollout positions: ℒ LSM = 𝔼 x , { o i } ∼ π θ , infer ​ [ 1 ∑ i = 1 G | o i | ​ ∑ i = 1 G ∑ t = 1 | o i | ∑ v ∈ S ⁡ ( c i , t ) π ^ θ ​ ( v ∣ c i , t ) ​ log ⁡ π ^ θ ​ ( v ∣ c i , t ) q ^ ​ ( v ∣ c i , t ) ] . \mathcal{L}_{\mathrm{LSM}}=\mathbb{E}_{x,\,\{o_{i}\}\sim\pi_{\theta,\mathrm{infer}}}\left[\frac{1}{\sum_{i=1}^{G}|o_{i}|}\sum_{i=1}^{G}\sum_{t=1}^{|o_{i}|}\sum_{v\in S(c_{i,t})}\hat{\pi}_{\theta}(v\mid c_{i,t})\log\frac{\hat{\pi}_{\theta}(v\mid c_{i,t})}{\hat{q}(v\mid c_{i,t})}\right]. (8) Relative to sampled-token OPD, this replaces a one-token point estimate with a distribution-level comparison over teacher-supported candidates at the same prefix. The update is therefore no longer determined by the sign and magnitude of a single sampled-token log-ratio, while remaining much cheaper than full-vocabulary KL.

### 3.2 Practical stabilization choices

##### Support-set renormalization.

Renormalization is necessary because the objective is evaluated on a truncated support rather than the full vocabulary. Specifically, we apply a separate softmax over the logits inside the support set, so gradients do not directly propagate to tokens outside this set. Without this step, optimization can become unstable because the teacher and student probability masses inside the support are not directly comparable.

##### Top- p p rollout sampling.

We generate rollouts with top- p p sampling. Unconstrained sampling occasionally produces very low-probability tokens, creating prefixes on which the teacher signal becomes less informative and optimization less stable. Top- p p sampling keeps trajectories closer to typical continuations and makes the teacher signal more reliable.

##### Special-token masking.

We mask problematic special tokens to reduce false negatives caused by incompatible tokenization conventions. This is an orthogonal practical fix: it materially helps sampled-token OPD in our experiments, while our local support objective is much less sensitive to it. In principle, one could also merge multi-token marker variants or average over equivalent tokenizations, but we do not pursue those tokenizer-specific remedies here because masking is the simplest model-agnostic correction.

## 4 Experiments

We evaluate local support matching in three settings: single-task math reasoning (Section 4.2 ), alternating multi-task training over math and agentic tasks (Section 4.3 ), and an additional single-task agentic setting on a smaller student model (Appendix G.1 ). We also present ablations in Section 4.4 and provide training-dynamics analysis in Appendix G.2 .

### 4.1 Setup

We implement local support matching on top of the verl-agent framework ( Feng et al., 2025 ) , using Qwen2.5-Instruct models as students. We consider two main settings. The first is single-task math reasoning, where OpenThinker3-7B ( Guha et al., 2025 ) serves as the teacher and training uses the English portion of DAPO-Math-17K ( Yu et al., 2025 ) with a maximum context length of 16K. The second is a multi-task setting that alternates batches between math reasoning and a multi-turn agentic task based on ALFWorld ( Shridhar et al., 2021 ) . In this setting, math uses OpenThinker3-7B ( Guha et al., 2025 ) as the teacher, while the agentic side uses the released GiGPO-Qwen2.5-7B-Instruct-ALFWorld checkpoint ( Feng et al., 2025 ) .

For math reasoning, we report pass@1 on five benchmarks: Math500 ( Hendrycks et al., 2021 ) , AIME24 ( Zhang and Math-AI, 2024 ) , AIME25 ( Zhang and Math-AI, 2025 ) , Minerva ( Lewkowycz et al., 2022 ) , and OlympiadBench ( He et al., 2024 ) . For ALFWorld ( Shridhar et al., 2021 ) , we report success rate by default. In a small number of cases, we additionally report avg@32 on the math benchmarks. More details on experimental setups can be found in Appendix F .

### 4.2 Single-task math reasoning

Table 1 shows that local support matching improves over sampled-token OPD in single-task math reasoning. Sampled-token OPD already improves the student from 28.2 to 36.4 average score, but still remains substantially below the teacher. Applying special-token masking to sampled-token OPD further improves the average to 40.7, indicating that tokenizer-related mismatch is a meaningful part of the failure.

Both variants of our method outperform sampled-token OPD and its masked variant in average score. This shows that the gain is not solely attributable to mismatch handling, and instead supports the role of a stronger distribution-level distillation signal. In addition, masking changes our method only modestly (41.7 vs. 41.5), consistent with the view that local support matching is less sensitive to tokenizer mismatch than one-token supervision. Additional evidence on WebShop ( Yao et al., 2022 ) is shown in Appendix G.1 .

### 4.3 Multi-task agentic-plus-reasoning training

Table 2 shows that the effect of local support matching differs across the two task families in alternating multi-task training. The unmasked version raises the average math score from 34.8 to 41.7 (+19.8%), while maintaining competitive ALFWorld performance. The masked version achieves the best ALFWorld score at 97.7, but gives up part of the math improvement. This pattern suggests that local support matching is especially helpful for the reasoning side of the mixture, where sampled-token signals are more exposed to prefix drift; masking, in contrast, mainly shifts the trade-off toward the agentic task in this run. Beyond evaluation performance, our objective also yields consistently better optimization dynamics. We defer the full learning curves and diagnostic plots to Appendix G.2 .

### 4.4 Ablations

Table 3 and Figure 6 suggest that the gains arise from several design choices rather than any single modification. Teacher top- K K comparison alone is not sufficient: the rollout policy must also remain in a stable region, and adding top- p p sampling turns an initially weaker top- K K variant into a stronger configuration. Under the same top- p p rollout conditions, teacher top- K K local support matching still improves AIME24 avg@32 from 21.6 to 23.6. Renormalization inside the truncated support is essential, as removing it leads to rapid collapse. Performance is not especially sensitive to the exact support size once K K is large enough, but training becomes unstable when the support is too small or rollouts are fully unconstrained.

##### Top- K K support variants.

Our main experiments define the truncated expectation on the teacher’s top- K K support. Alternative objectives can compute the expectation over teacher top- K K (used in the main results), student top- K K , or teacher top- K K augmented with the student-sampled token. We provide a preliminary comparison in Table 4 under both the single-task and multi-task settings.

In the single-task setting, the three variants achieve broadly comparable results. The teacher top- K K + sampled-token variant attains the highest average pass@1 score, while student top- K K performs competitively on several individual benchmarks, and the original teacher top- K K gives the best AIME24 avg@32 among the three. The multi-task results are less uniform. In that setting, the original teacher top- K K variant performs substantially better than the other two alternatives, while both student top- K K and teacher top- K K + sampled-token variants degrade considerably on the math benchmarks. We therefore treat these results as evidence that support construction matters, but do not over-interpret the ranking among variants.

Overall, these results suggest that the choice of where the KL expectation is computed can matter in nontrivial ways, especially in the multi-task setting. We treat this as a partial ablation and a preliminary exploration, and discuss possible causes, including support-set construction and remaining off-policy effects, in Appendix A .

## 5 Conclusion

This work revisits on-policy distillation (OPD) for LLM post-training from both theoretical and implementation perspectives. Our theoretical analysis shows why token-level OPD is an attractive approximation for long-horizon training: it is biased relative to sequence-level reverse-KL, but avoids future-reward coupling and has substantially better worst-case variance scaling. At the same time, our empirical study shows that the standard sampled-token implementation can provide brittle supervision because its signal is imbalanced, can remain misleading on student-drifted prefixes, and is sensitive to tokenizer or special-token mismatch. Teacher top- K K local support matching addresses these issues by preserving local token-level updates while replacing one-token supervision with a truncated distribution-level comparison. Across single-task math reasoning and alternating agentic-plus-reasoning training, this simple modification improves optimization stability and downstream performance over sampled-token OPD, while also clarifying where teacher matching remains an imperfect proxy for task success.

## References

Agarwal et al. (2024) R. Agarwal, N. Vieillard, Y. Zhou, P. Stanczyk, S. R. Garea, M. Geist, and O. Bachem On-policy distillation of language models: learning from self-generated mistakes . In The Twelfth International Conference on Learning Representations , External Links: Link Cited by: Appendix C , Appendix C , Appendix C , §1 .

Boizard et al. (2025) N. Boizard, K. E. Haddad, C. HUDELOT, and P. Colombo Towards cross-tokenizer distillation: the universal logit distillation loss for LLMs . Transactions on Machine Learning Research . External Links: ISSN 2835-8856 , Link Cited by: §2.2 .

Chen et al. (2025) H. Chen, N. Razin, K. Narasimhan, and D. Chen Retaining by doing: the role of on-policy data in mitigating forgetting . arXiv preprint arXiv:2510.18874 . Cited by: Appendix C .

DeepSeek-AI (2026) DeepSeek-AI DeepSeek-v4: towards highly efficient million-token context intelligence . Cited by: §1 , §1 .

Feng et al. (2025) L. Feng, Z. Xue, T. Liu, and B. An Group-in-group policy optimization for LLM agent training . In The Thirty-ninth Annual Conference on Neural Information Processing Systems , External Links: Link Cited by: Appendix F , Table A2 , §4.1 .

Gu et al. (2024) Y. Gu, L. Dong, F. Wei, and M. Huang MiniLLM: knowledge distillation of large language models . In The Twelfth International Conference on Learning Representations , External Links: Link Cited by: Appendix C , Appendix C , §1 , §1 .

Guha et al. (2025) E. Guha, R. Marten, S. Keh, N. Raoof, G. Smyrnis, H. Bansal, M. Nezhurina, J. Mercat, T. Vu, Z. Sprague, et al. OpenThoughts: data recipes for reasoning models . arXiv preprint arXiv:2506.04178 . Cited by: Appendix C , §2.2 , §4.1 .

He et al. (2024) C. He, R. Luo, Y. Bai, S. Hu, Z. Thai, J. Shen, J. Hu, X. Han, Y. Huang, Y. Zhang, et al. OlympiadBench: a challenging benchmark for promoting AGI with olympiad-level bilingual multimodal scientific problems . In Proceedings of the 62nd Annual Meeting of the Association for Computational Linguistics (Volume 1: Long Papers) , pp. 3828–3850 . Cited by: §4.1 .

Hendrycks et al. (2021) D. Hendrycks, C. Burns, S. Kadavath, A. Arora, S. Basart, E. Tang, D. Song, and J. Steinhardt Measuring mathematical problem solving with the MATH dataset . In Thirty-fifth Conference on Neural Information Processing Systems Datasets and Benchmarks Track (Round 2) , External Links: Link Cited by: §4.1 .

Hinton et al. (2015) G. Hinton, O. Vinyals, and J. Dean Distilling the knowledge in a neural network . arXiv preprint arXiv:1503.02531 . Cited by: Appendix C , Appendix C .

Hübotter et al. (2026) J. Hübotter, F. Lübeck, L. Behric, A. Baumann, M. Bagatella, D. Marta, I. Hakimi, I. Shenfeld, T. K. Buening, C. Guestrin, et al. Reinforcement learning via self-distillation . arXiv preprint arXiv:2601.20802 . Cited by: Appendix C , Appendix C , Appendix C .

Jin et al. (2026a) W. Jin, T. Min, Y. Yang, S. R. Kadhe, Y. Zhou, D. Wei, N. Baracaldo, and K. Lee Entropy-aware on-policy distillation of language models . In The 1st Workshop on Scaling Post-training for LLMs , External Links: Link Cited by: Appendix C .

Jin et al. (2026b) W. Jin, T. Min, Y. Yang, S. R. Kadhe, Y. Zhou, D. Wei, N. Baracaldo, and K. Lee Entropy-aware on-policy distillation of language models . arXiv preprint arXiv:2603.07079 . Cited by: §1 .

Kim and Rush (2016) Y. Kim and A. M. Rush Sequence-level knowledge distillation . In Proceedings of the 2016 conference on empirical methods in natural language processing , pp. 1317–1327 . Cited by: Appendix C .

Ko et al. (2026) J. Ko, S. Abdali, Y. J. Kim, T. Chen, and P. Cameron Scaling reasoning efficiently via relaxed on-policy distillation . arXiv preprint arXiv:2603.11137 . Cited by: Appendix C , §1 .

Lewkowycz et al. (2022) A. Lewkowycz, A. Andreassen, D. Dohan, E. Dyer, H. Michalewski, V. Ramasesh, A. Slone, C. Anil, I. Schlag, T. Gutman-Solo, et al. Solving quantitative reasoning problems with language models . Advances in neural information processing systems 35 , pp. 3843–3857 . Cited by: §4.1 .

Li et al. (2026) Y. Li, Y. Zuo, B. He, J. Zhang, C. Xiao, C. Qian, T. Yu, H. Gao, W. Yang, Z. Liu, et al. Rethinking on-policy distillation of large language models: phenomenology, mechanism, and recipe . arXiv preprint arXiv:2604.13016 . Cited by: Appendix B .

Liu et al. (2025) J. Liu, Y. Li, Y. Fu, J. Wang, Q. Liu, and Z. Jiang When speed kills stability: demystifying RL collapse from the training-inference mismatch . External Links: Link Cited by: Appendix A .

Lu and Lab (2025) K. Lu and T. M. Lab On-policy distillation . Thinking Machines Lab: Connectionism . Note: https://thinkingmachines.ai/blog/on-policy-distillation External Links: Document Cited by: Appendix C , §1 , §1 , §1 .

Minixhofer et al. (2025) B. Minixhofer, I. Vulić, and E. Ponti Universal cross-tokenizer distillation via approximate likelihood matching . In The Thirty-ninth Annual Conference on Neural Information Processing Systems , External Links: Link Cited by: §2.2 .

Ouyang et al. (2022) L. Ouyang, J. Wu, X. Jiang, D. Almeida, C. Wainwright, P. Mishkin, C. Zhang, S. Agarwal, K. Slama, A. Ray, et al. Training language models to follow instructions with human feedback . Advances in neural information processing systems 35 , pp. 27730–27744 . Cited by: Appendix C .

Patiño et al. (2025) C. M. Patiño, K. Rasul, Q. Gallouédec, B. Burtenshaw, S. Paniego, V. Srivastav, T. Frere, E. Beeching, L. Tunstall, L. von Werra, and T. Wolf Unlocking on-policy distillation for any model family . Cited by: §2.2 .

Qwen et al. (2024) Qwen, A. Yang, B. Yang, B. Zhang, B. Hui, B. Zheng, B. Yu, C. Li, D. Liu, F. Huang, H. Wei, H. Lin, J. Yang, J. Tu, J. Zhang, J. Yang, J. Yang, J. Zhou, J. Lin, K. Dang, K. Lu, K. Bao, K. Yang, L. Yu, M. Li, M. Xue, P. Zhang, Q. Zhu, R. Men, R. Lin, T. Li, T. Tang, T. Xia, X. Ren, X. Ren, Y. Fan, Y. Su, Y. Zhang, Y. Wan, Y. Liu, Z. Cui, Z. Zhang, and Z. Qiu Qwen2.5 technical report . arXiv preprint arXiv:2412.15115 . Cited by: §2.2 .

Sanh et al. (2019) V. Sanh, L. Debut, J. Chaumond, and T. Wolf DistilBERT, a distilled version of BERT: smaller, faster, cheaper and lighter . arXiv preprint arXiv:1910.01108 . Cited by: Appendix C .

Schulman (2020) J. Schulman Approximating KL divergence . John Schulman’s Homepage 5 . Cited by: Appendix C .

Sheng et al. (2025) G. Sheng, C. Zhang, Z. Ye, X. Wu, W. Zhang, R. Zhang, Y. Peng, H. Lin, and C. Wu HybridFlow: a flexible and efficient RLHF framework . In Proceedings of the Twentieth European Conference on Computer Systems , EuroSys ’25 , pp. 1279–1297 . External Links: Link , Document Cited by: Appendix F .

Shridhar et al. (2021) M. Shridhar, X. Yuan, M. Cote, Y. Bisk, A. Trischler, and M. Hausknecht ALFWorld: aligning text and embodied environments for interactive learning . In International Conference on Learning Representations , External Links: Link Cited by: §4.1 , §4.1 .

Wang et al. (2026a) H. Wang, X. Long, Z. Li, Y. Xu, T. Li, and Y. Tang To mix or to merge: toward multi-domain reinforcement learning for large language models . arXiv preprint arXiv:2602.12566 . Cited by: §1 .

Wang et al. (2026b) Y. Wang, X. Chen, X. Jin, M. Wang, and L. Yang OpenClaw-RL: train any agent simply by talking . arXiv preprint arXiv:2603.10165 . Cited by: Appendix C , Appendix C .

Xiao et al. (2026) B. Xiao, B. Xia, B. Yang, B. Gao, B. Shen, C. Zhang, C. He, C. Lou, F. Luo, G. Wang, et al. MiMo-V2-Flash technical report . arXiv preprint arXiv:2601.02780 . Cited by: Appendix C , §1 , §1 .

Yang et al. (2025) A. Yang, A. Li, B. Yang, B. Zhang, B. Hui, B. Zheng, B. Yu, C. Gao, C. Huang, C. Lv, et al. Qwen3 technical report . arXiv preprint arXiv:2505.09388 . Cited by: Appendix C , §1 .

Yang et al. (2026a) C. Yang, C. Qin, Q. Si, M. Chen, N. Gu, D. Yao, Z. Lin, W. Wang, J. Wang, and N. Duan Self-distilled RLVR . arXiv preprint arXiv:2604.03128 . Cited by: Appendix C .

Yang et al. (2026b) W. Yang, W. Liu, R. Xie, K. Yang, S. Yang, and Y. Lin Learning beyond teacher: generalized on-policy distillation with reward extrapolation . arXiv preprint arXiv:2602.12125 . Cited by: Appendix C .

Yao et al. (2025) F. Yao, L. Liu, D. Zhang, C. Dong, J. Shang, and J. Gao Your efficient RL framework secretly brings you off-policy RL training . External Links: Link Cited by: Appendix A .

Yao et al. (2022) S. Yao, H. Chen, J. Yang, and K. Narasimhan WebShop: towards scalable real-world web interaction with grounded language agents . Advances in Neural Information Processing Systems 35 , pp. 20744–20757 . Cited by: §G.1 , §4.2 .

Ye et al. (2026a) C. Ye, X. Zhang, Y. Hao, Z. Yu, Z. Zhang, A. Gullapalli, H. Chen, J. Huang, and T. Zhang Adaptive layerwise perturbation: unifying off-policy corrections for LLM RL . arXiv preprint arXiv:2603.19470 . Cited by: Appendix B .

Ye et al. (2025) T. Ye, L. Dong, Z. Chi, X. Wu, S. Huang, and F. Wei Black-box on-policy distillation of large language models . arXiv preprint arXiv:2511.10643 . Cited by: Appendix C .

Ye et al. (2026b) T. Ye, L. Dong, X. Wu, S. Huang, and F. Wei On-policy context distillation for language models . arXiv preprint arXiv:2602.12275 . Cited by: Appendix C .

Yu et al. (2025) Q. Yu, Z. Zhang, R. Zhu, Y. Yuan, X. Zuo, Y. Yue, W. Dai, T. Fan, G. Liu, J. Liu, L. Liu, X. Liu, H. Lin, Z. Lin, B. Ma, G. Sheng, Y. Tong, C. Zhang, M. Zhang, R. Zhang, W. Zhang, H. Zhu, J. Zhu, J. Chen, J. Chen, C. Wang, H. Yu, Y. Song, X. Wei, H. Zhou, J. Liu, W. Ma, Y. Zhang, L. Yan, Y. Wu, and M. Wang DAPO: an open-source LLM reinforcement learning system at scale . In The Thirty-ninth Annual Conference on Neural Information Processing Systems , External Links: Link Cited by: §4.1 .

Zeng et al. (2026) A. Zeng, X. Lv, Z. Hou, Z. Du, Q. Zheng, B. Chen, D. Yin, C. Ge, C. Xie, C. Wang, et al. GLM-5: from vibe coding to agentic engineering . arXiv preprint arXiv:2602.15763 . Cited by: Appendix C , §1 .

Zhang et al. (2026) J. Zhang, A. Hans, J. Kirchenbauer, M. Goldblum, A. Panda, and T. Goldstein Learning from mixed rollouts: logit fusion as a bridge between imitation and exploration . Notion Blog . External Links: Link Cited by: Appendix B .

Zhang and Ba (2026) L. Zhang and J. Ba EMA policy gradient: taming reinforcement learning for LLMs with EMA anchor and Top-k KL . arXiv preprint arXiv:2602.04417 . Cited by: Appendix A , Appendix B , Appendix C , §G.3.1 , §G.3.1 .

Zhang and Math-AI (2024) Y. Zhang and T. Math-AI American invitational mathematics examination (AIME) 2024 . Wei Zhao, Zhe Li, Yige Li, Ye Zhang, and Junfeng Sun . Cited by: §4.1 .

Zhang and Math-AI (2025) Y. Zhang and T. Math-AI American invitational mathematics examination (AIME) 2025 . Wei Zhao, Zhe Li, Yige Li, Ye Zhang, and Junfeng Sun . Cited by: §4.1 .

Zhao et al. (2026) S. Zhao, Z. Xie, M. Liu, J. Huang, G. Pang, F. Chen, and A. Grover Self-distilled reasoner: on-policy self-distillation for large language models . arXiv preprint arXiv:2601.18734 . Cited by: Appendix C , Appendix C , Appendix C , §1 .

Appendix

## Appendix A Discussion and Limitations

##### Sampled-token augmentation of the teacher top- K K support.

In our current implementation, the support is S ⁡ ( c t ) = TopK q ​ ( c t ) S(c_{t})=\mathrm{TopK}_{q}(c_{t}) : teacher and student distributions are renormalized on this teacher-selected set before computing the KL term. However, this is not the only possible design. One can instead use an augmented support S + ​ ( c t ) = S ⁡ ( c t ) ∪ { y t } S^{+}(c_{t})=S(c_{t})\cup\{y_{t}\} , or include the sampled token through an importance-weighted correction that more explicitly preserves unbiasedness with respect to the full-vocabulary reverse-KL ( Zhang and Ba, 2026 ) . We provide formal definitions of several support-augmentation variants, including alternatives based on teacher- or student-centered supports and EMA-PG-style corrections, and evaluate them in Appendix G.3 . Overall, our default renormalized formulation remains competitive across both single-task and multi-task settings, which is why we adopt it in the main experiments.

##### Support-set KL is a truncated objective.

Our formulation computes the KL term only over a restricted token subset, i.e., the teacher top- K K support, rather than over the full vocabulary. This means that the expected gradient is formed within that subset: tokens outside the support do not receive gradient contributions from this objective. Relative to full-vocabulary reverse-KL, this introduces bias; more generally, it changes where the expectation is taken and which parts of the vocabulary participate in the update. We describe this here as a property of the estimator, rather than as a settled benefit or drawback.

##### Training–inference mismatch.

Prefixes are generated under a rollout policy, e.g., top- p p sampling in the vLLM engine, while the training engine updates the model without correcting for this sampling process. This may introduce a training–inference mismatch ( Liu et al., 2025 ; Yao et al., 2025 ) , which we leave to ongoing work.

##### Teacher matching remains an imperfect proxy for task success.

Even when OPD is well defined as a teacher-matching objective, the resulting reward can still diverge from the underlying notion of successful behavior. Our reward-hacking cases make this gap concrete: locally teacher-preferred continuations can remain rewardable even when the overall trajectory is already unhelpful or harmful. A noticeable gap to the teacher also remains in our experiments, which suggests that better local supervision is only one part of the distillation problem, especially when teacher and student differ substantially. Closing that gap may require stronger rollout control, better handling of distribution shift, better use of teacher uncertainty, and combinations with outcome-verifiable rewards.

## Appendix B Future Directions

##### Top- p p truncation as an adaptive support.

Another route toward a more compute-efficient reverse-KL objective is top- p p truncation instead of top- K K truncation, where the KL divergence is computed on the subset of tokens whose cumulative probability mass reaches a prescribed top- p p threshold.

##### OPD versus RL in multi-task settings.

Our multi-task results motivate a more direct comparison between OPD and RL as transfer mechanisms. In RL, positive or negative transfer can be read directly from environment reward across tasks. In OPD, the optimization target remains teacher-derived, so transfer is filtered through what the teacher regards as locally preferable behavior. This distinction may help explain why our multi-task gains are strongest on the math side and why nearby support-set definitions become less uniform in that setting. A matched-task, matched-compute comparison between OPD and RL would help clarify when teacher-guided transfer tracks environment-level generalization and when the teacher–reward gap becomes the bottleneck.

##### Continual learning as a testbed.

Continual learning is another natural setting for OPD. A teacher-guided on-policy objective could act as a retention mechanism while the student adapts to new tasks, but that regime would also stress exactly the issues surfaced in this paper: distribution shift, teacher staleness, and the accumulation of approximation error over long adaptation horizons. Testing OPD there would therefore probe not only whether local support matching mitigates forgetting, but also whether teacher-based objectives remain useful once the student keeps moving away from the teacher’s original domain.

##### Relation to other stabilization directions.

This work is complementary to directions such as reward-hacking mitigation, EMA-anchor stabilization with top- K K KL ( Zhang and Ba, 2026 ) , perturbation-based off-policy correction ( Ye et al., 2026a ) , and logit-level fusion between teacher and student rollouts ( Zhang et al., 2026 ) . These methods address different parts of the same broader problem: how to keep teacher-derived signals useful once teacher and student policies begin to diverge ( Li et al., 2026 ) . We view our method as one component in that larger toolbox, rather than as a replacement for those stabilization strategies.

## Appendix C Related Work

##### On-policy distillation.

Many widely used post-training methods for language models rely on off-policy supervision from fixed datasets, including supervised fine-tuning on demonstration data ( Ouyang et al., 2022 ; Guha et al., 2025 ) and conventional knowledge distillation on teacher-provided targets ( Hinton et al., 2015 ; Sanh et al., 2019 ) . In autoregressive generation, however, such fixed-prefix training creates a mismatch between the contexts seen during training and the prefixes induced by the student’s own test-time rollouts, motivating subsequent work on on-policy distillation (OPD) ( Agarwal et al., 2024 ) , where supervision is computed on student-generated trajectories. Agarwal et al. (2024) formulate generalized knowledge distillation for autoregressive models, while Gu et al. (2024) derive an effective on-policy optimization procedure. More recently, OPD and closely related variants have appeared in large-scale post-training pipelines, including Qwen3 ( Yang et al., 2025 ) , Thinking Machines Lab ( Lu and Lab, 2025 ) , MiMo-V2-Flash ( Xiao et al., 2026 ) , and GLM-5 ( Zeng et al., 2026 ) , underscoring the practical value of on-policy supervision for reasoning transfer, continual adaptation, and capability recovery across training stages. Subsequent work broadens this family in several directions: Ye et al. (2025) , Yang et al. (2026b) , and Ko et al. (2026) extend OPD to black-box teachers, more flexible reward formulations, and relaxed imitation objectives, respectively. Ye et al. (2026b) further connect OPD with context distillation, showing that on-policy supervision can also be used to internalize context- or prompt-conditioned behaviors. Related self- or hindsight-distillation approaches replace the external teacher with guidance derived from privileged information or feedback ( Zhao et al., 2026 ; Hübotter et al., 2026 ; Wang et al., 2026b ; Yang et al., 2026a ) . In contrast, our work does not introduce a new supervision regime; instead, we revisit the standard sampled-token estimator itself and improve its token-level learning signal through teacher top- K K local support matching.

##### KL computation for LLM post-training.

Sampled KL estimators in LLM post-training are commonly based on forms such as K 1 K_{1} , K 2 K_{2} , and K 3 K_{3} ( Schulman, 2020 ) . These estimators are lightweight, but they retain only the sampled token and therefore discard the richer next-token distribution available from teacher logits in white-box settings. When teacher logits are available, one can in principle match the full next-token distribution, but materializing full-vocabulary logits is often prohibitively memory-intensive for long responses and large models ( Hinton et al., 2015 ; Kim and Rush, 2016 ; Agarwal et al., 2024 ) . At one extreme, Zhao et al. (2026) use full-vocabulary logit distillation in a self-distillation setting. To reduce the cost of full-distribution matching, Zhang and Ba (2026) derive an unbiased top- K K KL estimator that combines exact computation on a top- K K set with a sampled correction for the tail. Related self-distillation methods such as SDPO and OpenClaw-RL also adopt top- K K approximations for efficiency, but without explicitly incorporating the sampled token into the truncated support ( Hübotter et al., 2026 ; Wang et al., 2026b ) . Our method instead computes a truncated reverse-KL objective on the teacher’s local top- K K support, with both teacher and student distributions renormalized within the selected set. This yields a simple distribution-level alternative to sampled-token OPD without incurring the cost of full-vocabulary matching.

##### KL divergence in RL for LLMs.

The choice of KL divergence can substantially affect distribution matching in on-policy distillation and related post-training methods for language models. Gu et al. (2024) argue that reverse KL is often better suited than the forward-KL objective commonly used in conventional distillation because it discourages the student from overestimating the teacher’s low-probability regions and tends to yield more precise generation. Agarwal et al. (2024) further show that different divergences induce a quality–diversity trade-off: moving from forward KL toward reverse KL through generalized Jensen–Shannon divergence (JSD) yields increasingly mode-seeking behavior and lower diversity. A related perspective is provided by Chen et al. (2025) , who connect the reverse-KL-like, mode-seeking character of on-policy RL to reduced forgetting during post-training. More recently, Jin et al. (2026a) argue that pure reverse-KL-style OPD can become brittle when the teacher distribution has high entropy, and propose augmenting reverse KL with forward KL on high-entropy tokens to better preserve diversity. At the same time, the preferred divergence can depend on the supervision setting. In self-distillation with privileged information, Zhao et al. (2026) report that forward KL outperforms reverse KL and JSD, whereas SDPO adopts JSD as a stability-oriented design choice ( Hübotter et al., 2026 ) . In this work, we adopt a reverse-KL formulation, but focus on a different question: how to obtain a stable local reverse-KL-style training signal under sampled-token OPD.

## Appendix D Bias and variance analysis of token-level versus sequence-level OPD

### D.1 Bias of the token-level estimator

Recall the sequence-level estimator in causal return-to-go form g ^ seq = ∑ t = 1 T ( ∑ t ′ = t T r t ′ ) ​ s t . \hat{g}_{\mathrm{seq}}=\sum_{t=1}^{T}\left(\sum_{t^{\prime}=t}^{T}r_{t^{\prime}}\right)s_{t}. Expanding the inner sum gives g ^ seq = ∑ t = 1 T r t ​ s t + ∑ t = 1 T ∑ t ′ = t + 1 T r t ′ ​ s t . \hat{g}_{\mathrm{seq}}=\sum_{t=1}^{T}r_{t}s_{t}+\sum_{t=1}^{T}\sum_{t^{\prime}=t+1}^{T}r_{t^{\prime}}s_{t}. Since the token-level estimator keeps only the first term, g ^ tok = ∑ t = 1 T r t ​ s t , \hat{g}_{\mathrm{tok}}=\sum_{t=1}^{T}r_{t}s_{t}, their expectation gap is 𝔼 ⁡ [ g ^ seq ] − 𝔼 ⁡ [ g ^ tok ] = 𝔼 ⁡ [ ∑ t = 1 T ∑ t ′ = t + 1 T r t ′ ​ s t ] . \mathbb{E}[\hat{g}_{\mathrm{seq}}]-\mathbb{E}[\hat{g}_{\mathrm{tok}}]=\mathbb{E}\left[\sum_{t=1}^{T}\sum_{t^{\prime}=t+1}^{T}r_{t^{\prime}}s_{t}\right]. This makes explicit that token-level OPD removes the future-reward coupling terms and is therefore generally biased with respect to the sequence-level objective.

### D.2 Worst-case variance upper bounds

Assume there exist constants B r , B s > 0 B_{r},B_{s}>0 such that | r t | ≤ B r , ∥ s t ∥ ≤ B s for all t . |r_{t}|\leq B_{r},\qquad\|s_{t}\|\leq B_{s}\quad\text{for all }t. For the token-level estimator, ‖ g ^ tok ‖ ≤ ∑ t = 1 T | r t | ​ ‖ s t ‖ ≤ T ​ B r ​ B s , \|\hat{g}_{\mathrm{tok}}\|\leq\sum_{t=1}^{T}|r_{t}|\,\|s_{t}\|\leq TB_{r}B_{s}, which implies 𝔼 ​ ‖ g ^ tok ‖ 2 ≤ T 2 ​ B r 2 ​ B s 2 . \mathbb{E}\|\hat{g}_{\mathrm{tok}}\|^{2}\leq T^{2}B_{r}^{2}B_{s}^{2}. Using Var ⁡ ( X ) ≤ 𝔼 ​ ‖ X ‖ 2 \mathrm{Var}(X)\leq\mathbb{E}\|X\|^{2} , we obtain Var ⁡ ( g ^ tok ) = O ⁡ ( T 2 ) . \mathrm{Var}(\hat{g}_{\mathrm{tok}})=O(T^{2}).

For the sequence-level estimator, define R = ∑ t = 1 T r t , S = ∑ t = 1 T s t , g ^ seq = R ​ S . R=\sum_{t=1}^{T}r_{t},\qquad S=\sum_{t=1}^{T}s_{t},\qquad\hat{g}_{\mathrm{seq}}=RS. Then | R | ≤ T ​ B r , ‖ S ‖ ≤ T ​ B s , |R|\leq TB_{r},\qquad\|S\|\leq TB_{s}, so ‖ g ^ seq ‖ ≤ T 2 ​ B r ​ B s , 𝔼 ​ ‖ g ^ seq ‖ 2 ≤ T 4 ​ B r 2 ​ B s 2 . \|\hat{g}_{\mathrm{seq}}\|\leq T^{2}B_{r}B_{s},\qquad\mathbb{E}\|\hat{g}_{\mathrm{seq}}\|^{2}\leq T^{4}B_{r}^{2}B_{s}^{2}. Therefore, Var ⁡ ( g ^ seq ) = O ⁡ ( T 4 ) . \mathrm{Var}(\hat{g}_{\mathrm{seq}})=O(T^{4}).

### D.3 Discussion

The sequence-level estimator is closer to the exact trajectory-level objective, but it couples each score term with many future rewards. In worst-case scaling, this changes variance growth from quadratic to quartic in sequence length. The argument is conservative, but it captures why stronger reward coupling can become problematic in long-horizon training.

## Appendix E Toy experiment details

### E.1 Environment

We use a two-task one-dimensional continuous-control environment to visualize how stronger return coupling changes OPD optimization. The student policy is a three-layer MLP with roughly 4K parameters. Its input is a three-dimensional vector containing task identity, current position, and normalized time step. The policy outputs the mean and standard deviation of a Gaussian action distribution, and the state transition is s t + 1 = s t + δ , δ ∼ 𝒩 ⁡ ( μ , σ ) . s_{t+1}=s_{t}+\delta,\qquad\delta\sim\mathcal{N}(\mu,\sigma). The two tasks are mirror images of each other: the left task starts from + 2 +2 and targets − 3 -3 , while the right task starts from − 2 -2 and targets + 3 +3 . We first train separate teachers with REINFORCE and then distill them into a shared student with alternating-task OPD.

### E.2 Gradient variance estimation

At each training step, we split a batch of B = 64 B=64 trajectories into M = 8 M=8 micro-batches. For each micro-batch m m , we compute a loss ℒ m \mathcal{L}_{m} and the corresponding gradient vector 𝐠 m \mathbf{g}_{m} on the output layer parameters. We then estimate gradient variance by Var ⁡ ( 𝐠 ) = 1 M ​ ∑ m = 1 M ‖ 𝐠 m − 𝐠 ¯ ‖ 2 , 𝐠 ¯ = 1 M ​ ∑ m = 1 M 𝐠 m . \mathrm{Var}(\mathbf{g})=\frac{1}{M}\sum_{m=1}^{M}\left\|\mathbf{g}_{m}-\bar{\mathbf{g}}\right\|^{2},\qquad\bar{\mathbf{g}}=\frac{1}{M}\sum_{m=1}^{M}\mathbf{g}_{m}. We use this quantity only as a qualitative proxy, but it is sufficient for comparing relative variance across different γ \gamma settings.

### E.3 Additional Results of Toy Experiments

Figures A1 , A2 , and A3 report gradient-variance curves and corresponding state-visitation heatmaps for different OPD estimators ( γ ∈ { 0.0 , 0.25 , 0.5 , 0.75 , 1.0 } \gamma\in\{0.0,0.25,0.5,0.75,1.0\} ) across three random seeds. Although the exact magnitudes vary by seed, the qualitative pattern is consistent. All settings exhibit large variance spikes during early optimization, and larger γ \gamma typically remains at a higher variance level later in training. In several runs, the variance under γ = 0.75 \gamma=0.75 or γ = 1.0 \gamma=1.0 stays one to several orders of magnitude above that of smaller γ \gamma values. Across runs, token-level OPD ( γ = 0 \gamma=0 ) consistently learns trajectories that move toward the target states for both tasks. Intermediate values of γ \gamma remain qualitatively similar but become more diffuse. When γ \gamma approaches the sequence-level case ( γ = 1.0 \gamma=1.0 ), the learned trajectories often deviate from the desired direction and stabilize around sub-optimal regions.

## Appendix F Experiment Setups

We build our training pipeline on verl 1 1 1 https://github.com/verl-project/verl ( Sheng et al., 2025 ) and the verl-agent framework 2 2 2 https://github.com/langfengQ/verl-agent ( Feng et al., 2025 ) , and conduct all experiments on a node with 8 NVIDIA H100 GPUs. We report the settings and hyperparameters used in our experiments in Table A1 .

## Appendix G Additional Results

### G.1 Additional Evidence on Single-task WebShop

To test whether the same trend transfers beyond the main math and ALFWorld settings, we additionally evaluate single-task WebShop ( Yao et al., 2022 ) using Qwen2.5-1.5B-Instruct as the student. As shown in Table A2 , local support matching improves over sampled-token OPD on both task score and success rate, increasing success rate from 50.0 to 57.8. Although the gap to the teacher remains substantial, the result suggests that the method transfers beyond the main math/agentic settings. We do not include a masking variant in this setting because the teacher is obtained by RL training from the same base model, so tokenizer or special-token mismatch is less likely to be a dominant factor here.

### G.2 Training Dynamics and Alignment

Figures A4 , A5 , and A6 provide a more detailed view of the optimization dynamics.

##### Better learning curves.

On math reasoning, our method improves both training reward and evaluation performance across most of training rather than only at the final checkpoint. This pattern holds in both the single-task setting and the alternating multi-task setting.

##### More stable optimization.

Our method yields smaller gradient norms and lower clipping-boundary fractions while maintaining sufficient policy entropy, indicating more stable optimization. We also observe that special-token masking substantially reduces the clipping-boundary fraction of sampled-token OPD during early and middle training, while having only minor effects on our method.

##### Improved teacher–student alignment.

The teacher–student log-probability gap on sampled tokens also moves closer to zero, suggesting that the truncated local support objective improves alignment even under the sampled-token diagnostic used by the baseline.

### G.3 Additional Results of Top- K K Variants

We primarily evaluate five top- K K variants in our experiments. Below, we present their formulations under unified notation and evaluate them in both single-task math and multi-task settings. All experimental setups are kept the same as in the main experiments.

#### G.3.1 Formulations of Five Top- K K Variants

##### Shared notation.

For each prompt x x , we sample a group of outputs { o i } i = 1 G \{o_{i}\}_{i=1}^{G} from the student inference policy π infer \pi_{\mathrm{infer}} . Let y i , t y_{i,t} denote the token at position t t in output o i o_{i} , and let c i , t = ( x , y i , < t ) c_{i,t}=(x,y_{i,<t}) be the corresponding prefix. We write 𝒯 K π ​ ( c i , t ) = TopK π ⁡ ( c i , t ) , 𝒯 K q ​ ( c i , t ) = TopK q ⁡ ( c i , t ) , \mathcal{T}_{K}^{\pi}(c_{i,t})=\operatorname{TopK}_{\pi}(c_{i,t}),\qquad\mathcal{T}_{K}^{q}(c_{i,t})=\operatorname{TopK}_{q}(c_{i,t}), for the student and teacher top- K K token sets at prefix c i , t c_{i,t} .

All variants below share the same rollout-level aggregation: ℒ ⁡ [ ℓ ] = 𝔼 x , { o i } ∼ π infer ​ [ 1 ∑ i = 1 G | o i | ​ ∑ i = 1 G ∑ t = 1 | o i | ℓ ⁡ ( c i , t , y i , t ) ] . \mathcal{L}[\ell]=\mathbb{E}_{x,\{o_{i}\}\sim\pi_{\mathrm{infer}}}\left[\frac{1}{\sum_{i=1}^{G}|o_{i}|}\sum_{i=1}^{G}\sum_{t=1}^{|o_{i}|}\ell(c_{i,t},y_{i,t})\right]. They differ only in how the local loss ℓ ⁡ ( c i , t , y i , t ) \ell(c_{i,t},y_{i,t}) is defined.

##### Renormalized local reverse-KL.

For any support set 𝒮 ⁡ ( c i , t ) ⊆ 𝒱 \mathcal{S}(c_{i,t})\subseteq\mathcal{V} , define the renormalized student and teacher distributions on 𝒮 ⁡ ( c i , t ) \mathcal{S}(c_{i,t}) by π ¯ θ ​ ( v ∣ c i , t ; 𝒮 ) = π θ ​ ( v ∣ c i , t ) ∑ u ∈ 𝒮 ⁡ ( c i , t ) π θ ​ ( u ∣ c i , t ) , q ¯ ​ ( v ∣ c i , t ; 𝒮 ) = q ⁡ ( v ∣ c i , t ) ∑ u ∈ 𝒮 ⁡ ( c i , t ) q ⁡ ( u ∣ c i , t ) , v ∈ 𝒮 ⁡ ( c i , t ) . \bar{\pi}_{\theta}(v\mid c_{i,t};\mathcal{S})=\frac{\pi_{\theta}(v\mid c_{i,t})}{\sum_{u\in\mathcal{S}(c_{i,t})}\pi_{\theta}(u\mid c_{i,t})},\qquad\bar{q}(v\mid c_{i,t};\mathcal{S})=\frac{q(v\mid c_{i,t})}{\sum_{u\in\mathcal{S}(c_{i,t})}q(u\mid c_{i,t})},\quad v\in\mathcal{S}(c_{i,t}). The corresponding local reverse-KL is ℓ renorm ​ ( c i , t , 𝒮 ) = ∑ v ∈ 𝒮 ⁡ ( c i , t ) π ¯ θ ​ ( v ∣ c i , t ; 𝒮 ) ​ log ⁡ π ¯ θ ​ ( v ∣ c i , t ; 𝒮 ) q ¯ ​ ( v ∣ c i , t ; 𝒮 ) . \ell_{\mathrm{renorm}}(c_{i,t};\mathcal{S})=\sum_{v\in\mathcal{S}(c_{i,t})}\bar{\pi}_{\theta}(v\mid c_{i,t};\mathcal{S})\log\frac{\bar{\pi}_{\theta}(v\mid c_{i,t};\mathcal{S})}{\bar{q}(v\mid c_{i,t};\mathcal{S})}.

##### Variant 1: teacher top- K K renormalization (our method).

Our default local support matching (LSM) method uses the teacher top- K K support 𝒮 LSM ​ ( c i , t ) = 𝒯 K q ​ ( c i , t ) , \mathcal{S}_{\mathrm{LSM}}(c_{i,t})=\mathcal{T}_{K}^{q}(c_{i,t}), and defines ℓ LSM ​ ( c i , t , y i , t ) = ℓ renorm ​ ( c i , t , 𝒮 LSM ) . \ell_{\mathrm{LSM}}(c_{i,t},y_{i,t})=\ell_{\mathrm{renorm}}(c_{i,t};\mathcal{S}_{\mathrm{LSM}}). The overall objective is ℒ LSM = ℒ ⁡ [ ℓ LSM ] . \mathcal{L}_{\mathrm{LSM}}=\mathcal{L}[\ell_{\mathrm{LSM}}].

##### Variant 2: student top- K K + sampled token + renormalization.

For this variant, the support is obtained by augmenting the student top- K K set with the sampled token when needed: 𝒮 π + y ​ ( c i , t ) = { 𝒯 K π ​ ( c i , t ) , y i , t ∈ 𝒯 K π ​ ( c i , t ) , 𝒯 K π ​ ( c i , t ) ∪ { y i , t } , y i , t ∉ 𝒯 K π ​ ( c i , t ) . \mathcal{S}_{\pi+y}(c_{i,t})=\begin{cases}\mathcal{T}_{K}^{\pi}(c_{i,t}),&y_{i,t}\in\mathcal{T}_{K}^{\pi}(c_{i,t}),\\[4.0pt] \mathcal{T}_{K}^{\pi}(c_{i,t})\cup\{y_{i,t}\},&y_{i,t}\notin\mathcal{T}_{K}^{\pi}(c_{i,t}).\end{cases} We then define ℓ π + y ​ ( c i , t , y i , t ) = ℓ renorm ​ ( c i , t , 𝒮 π + y ) , \ell_{\pi+y}(c_{i,t},y_{i,t})=\ell_{\mathrm{renorm}}(c_{i,t};\mathcal{S}_{\pi+y}), and ℒ π + y = ℒ ⁡ [ ℓ π + y ] . \mathcal{L}_{\pi+y}=\mathcal{L}[\ell_{\pi+y}].

##### Variant 3: teacher top- K K + sampled token + renormalization.

Similarly, this variant augments the teacher top- K K set with the sampled token: 𝒮 q + y ​ ( c i , t ) = { 𝒯 K q ​ ( c i , t ) , y i , t ∈ 𝒯 K q ​ ( c i , t ) , 𝒯 K q ​ ( c i , t ) ∪ { y i , t } , y i , t ∉ 𝒯 K q ​ ( c i , t ) . \mathcal{S}_{q+y}(c_{i,t})=\begin{cases}\mathcal{T}_{K}^{q}(c_{i,t}),&y_{i,t}\in\mathcal{T}_{K}^{q}(c_{i,t}),\\[4.0pt] \mathcal{T}_{K}^{q}(c_{i,t})\cup\{y_{i,t}\},&y_{i,t}\notin\mathcal{T}_{K}^{q}(c_{i,t}).\end{cases} Its local and rollout-level losses are ℓ q + y ​ ( c i , t , y i , t ) = ℓ renorm ​ ( c i , t , 𝒮 q + y ) , ℒ q + y = ℒ ⁡ [ ℓ q + y ] . \ell_{q+y}(c_{i,t},y_{i,t})=\ell_{\mathrm{renorm}}(c_{i,t};\mathcal{S}_{q+y}),\qquad\mathcal{L}_{q+y}=\mathcal{L}[\ell_{q+y}].

##### EMA-PG-style local loss.

The remaining two variants follow the EMA-PG decomposition ( Zhang and Ba, 2026 ) , where a top- K K truncated head term is combined with an importance-weighted sampled-token tail correction to obtain an unbiased estimator of the full-vocabulary reverse-KL. For any support set 𝒮 ⁡ ( c i , t ) ⊆ 𝒱 \mathcal{S}(c_{i,t})\subseteq\mathcal{V} , define the truncated head term ℓ head ​ ( c i , t , 𝒮 ) = ∑ v ∈ 𝒮 ⁡ ( c i , t ) π θ ​ ( v ∣ c i , t ) ​ log ⁡ π θ ​ ( v ∣ c i , t ) q ⁡ ( v ∣ c i , t ) . \ell_{\mathrm{head}}(c_{i,t};\mathcal{S})=\sum_{v\in\mathcal{S}(c_{i,t})}\pi_{\theta}(v\mid c_{i,t})\log\frac{\pi_{\theta}(v\mid c_{i,t})}{q(v\mid c_{i,t})}. Let sg ⁡ ( ⋅ ) \operatorname{sg}(\cdot) denote stop-gradient, and define r i , t = π θ ​ ( y i , t ∣ c i , t ) sg ⁡ ( π θ ​ ( y i , t ∣ c i , t ) ) , s i , t = sg ⁡ ( π θ ​ ( y i , t ∣ c i , t ) π infer ​ ( y i , t ∣ c i , t ) ) , r_{i,t}=\frac{\pi_{\theta}(y_{i,t}\mid c_{i,t})}{\operatorname{sg}\!\left(\pi_{\theta}(y_{i,t}\mid c_{i,t})\right)},\qquad s_{i,t}=\operatorname{sg}\!\left(\frac{\pi_{\theta}(y_{i,t}\mid c_{i,t})}{\pi_{\mathrm{infer}}(y_{i,t}\mid c_{i,t})}\right), where s i , t s_{i,t} is the sampling-policy correction (optionally clipped, as in EMA-PG). The sampled-token tail correction is ℓ tail ( c i , t , y i , t ; 𝒮 ) = s i , t [ y i , t ∉ 𝒮 ( c i , t ) ] r i , t sg ( log π θ ​ ( y i , t ∣ c i , t ) q ⁡ ( y i , t ∣ c i , t ) ) . \ell_{\mathrm{tail}}(c_{i,t},y_{i,t};\mathcal{S})=s_{i,t}\,\mathbf{1}\!\left[y_{i,t}\notin\mathcal{S}(c_{i,t})\right]\,r_{i,t}\,\operatorname{sg}\!\left(\log\frac{\pi_{\theta}(y_{i,t}\mid c_{i,t})}{q(y_{i,t}\mid c_{i,t})}\right). The corresponding local EMA-PG loss is ℓ EMA ​ ( c i , t , y i , t , 𝒮 ) = ℓ head ​ ( c i , t , 𝒮 ) + ℓ tail ​ ( c i , t , y i , t , 𝒮 ) . \ell_{\mathrm{EMA}}(c_{i,t},y_{i,t};\mathcal{S})=\ell_{\mathrm{head}}(c_{i,t};\mathcal{S})+\ell_{\mathrm{tail}}(c_{i,t},y_{i,t};\mathcal{S}).

##### Variant 4: student top- K K + EMA-PG correction.

This variant uses the student top- K K support 𝒮 π ​ -EMA ​ ( c i , t ) = 𝒯 K π ​ ( c i , t ) , \mathcal{S}_{\pi\text{-EMA}}(c_{i,t})=\mathcal{T}_{K}^{\pi}(c_{i,t}), and defines ℓ π ​ -EMA ​ ( c i , t , y i , t ) = ℓ EMA ​ ( c i , t , y i , t , 𝒮 π ​ -EMA ) , ℒ π ​ -EMA = ℒ ⁡ [ ℓ π ​ -EMA ] . \ell_{\pi\text{-EMA}}(c_{i,t},y_{i,t})=\ell_{\mathrm{EMA}}(c_{i,t},y_{i,t};\mathcal{S}_{\pi\text{-EMA}}),\qquad\mathcal{L}_{\pi\text{-EMA}}=\mathcal{L}[\ell_{\pi\text{-EMA}}].

##### Variant 5: teacher top- K K + EMA-PG correction.

This variant instead uses the teacher top- K K support 𝒮 q ​ -EMA ​ ( c i , t ) = 𝒯 K q ​ ( c i , t ) , \mathcal{S}_{q\text{-EMA}}(c_{i,t})=\mathcal{T}_{K}^{q}(c_{i,t}), and defines ℓ q ​ -EMA ​ ( c i , t , y i , t ) = ℓ EMA ​ ( c i , t , y i , t , 𝒮 q ​ -EMA ) , ℒ q ​ -EMA = ℒ ⁡ [ ℓ q ​ -EMA ] . \ell_{q\text{-EMA}}(c_{i,t},y_{i,t})=\ell_{\mathrm{EMA}}(c_{i,t},y_{i,t};\mathcal{S}_{q\text{-EMA}}),\qquad\mathcal{L}_{q\text{-EMA}}=\mathcal{L}[\ell_{q\text{-EMA}}].

##### Summary.

The five formulations differ only in how the local support is constructed and whether the sampled token is incorporated through support augmentation or through an EMA-PG-style tail correction. Variants 1–3 compute a renormalized reverse-KL on the resulting local support, while Variants 4–5 replace support renormalization by a truncated head term plus a sampled-token correction ( Zhang and Ba, 2026 ) .

#### G.3.2 Results under Single-task and Multi-task Settings

As shown in Table A3 , teacher top- K K performs reasonably well in the single-task setting and remains strong in the multi-task setting. By contrast, the EMA-PG variants, despite their unbiasedness motivation, do not translate into better empirical performance here. We therefore treat the variant comparison as a diagnostic result rather than a definitive ranking of support-set objectives.

## Appendix H Qualitative OPD reward-hacking case study

To complement the representative failures in the main text, we summarize a longer trajectory from multi-task training under sampled-token OPD. Read chronologically, the case exhibits the same pattern in several forms: the model continues reasoning after a valid answer has already been reached, falls into repetition loops such as wait , drifts into malformed continuations, and still receives high local teacher probability on those tokens. In these visualizations, uncolored tokens indicate positions where the displayed teacher and student probabilities are approximately matched.

The failure first appears as over-continuation . Even after the answer is effectively available, the local signal continues to place substantial mass on generic reasoning fillers and connective tokens, encouraging the model to keep going instead of stopping cleanly. The same pattern later appears on prefixes such as confirm , where the local signal still favors additional verification rather than termination. Some of this behavior may also reflect the teacher’s own output habits. Figure A7 illustrates several representative cases.

The trajectory then develops into hesitation loops and low-information continuations . Repeated wait tokens, punctuation-heavy continuations, and other semantically weak fillers can remain locally rewardable even after the overall trajectory has become unproductive. This is consistent with the repetition-loop discussion in Section 2.2 . We provide two similar cases in Figure A8 .

Finally, once the student drifts further off-distribution, the local signal can remain misleadingly positive rather than self-correcting. In the case study, this appears as degenerate continuations and malformed non-English text, yet many tokens still receive high teacher probability. An example is shown in Figure A9 .

## Instructions for reporting errors

We are continuing to improve HTML versions of papers, and your feedback helps enhance accessibility and mobile support. To report errors in the HTML that will help us improve conversion and rendering, choose any of the methods listed below:

Click the "Report Issue" ( ) button, located in the page header.

Tip: You can select the relevant text first, to include it in your report.

Our team has already identified the following issues . We appreciate your time reviewing and reporting rendering errors we may not have found yet. Your efforts will help us improve the HTML versions for all readers, because disability should not be a barrier to accessing research. Thank you for your continued support in championing open access for all.

Have a free development cycle? Help support accessibility at arXiv! Our collaborators at LaTeXML maintain a list of packages that need conversion , and welcome developer contributions .
