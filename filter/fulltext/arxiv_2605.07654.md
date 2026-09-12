##### Report GitHub Issue

Content selection saved. Describe the issue below:

# Reliable Chain-of-Thought via Prefix Consistency

###### Abstract

Large Language Models often improve accuracy on reasoning tasks by sampling multiple Chain-of-Thought (CoT) traces and aggregating them with majority voting (MV), a test-time technique called self-consistency. When we truncate a CoT partway through and regenerate the remainder, we observe that traces with correct answers reproduce their original answer more often than traces with wrong answers. We use this difference as a reliability signal, prefix consistency , that weights each candidate answer by how often it reappears under regeneration. It requires no access to token log-probabilities or self-rating prompts. Across five reasoning models and four math and science benchmarks, prefix consistency is the best correctness predictor in most settings, and reweighting votes by it reaches Standard MV plateau accuracy at up to 21 × 21\times fewer tokens (median 4.6 × 4.6\times ). Our code is available at https://github.com/naoto-iwase/prefix-consistency .

## 1 Introduction

Large Language Models (LLMs) have shown strong reasoning ability when allowed to produce Chain-of-Thought (CoT) reasoning ( Kojima et al., 2022 ; Wei et al., 2022 ) . Generating intermediate reasoning steps substantially improves performance on challenging tasks such as math ( Zhou et al., 2023 ; Fu et al., 2023 ) , scientific reasoning ( Lu et al., 2022 ; Wang et al., 2024 ) , and knowledge-intensive question answering ( Trivedi et al., 2023 ; Wang et al., 2023a ) .

A simple and effective way to further improve the accuracy of the final answer is majority voting (MV, also known as self-consistency), which samples a diverse set of CoTs and returns the most frequent answer ( Wang et al., 2023b ) . A limitation is that Standard MV treats all CoT outputs equally and still fails when the correct answer is in the minority.

To improve MV, the standard approach has been to use weighted majority voting (WMV). WMV refines MV by weighting each generation according to its quality. The more reliable a generation is, the greater the signal it receives. Existing WMV methods derive a per-sample reliability signal from the generated trace, including response probability ( Wang et al., 2023b ) , self-certainty ( Kang et al., 2025 ) , DeepConf ( Fu et al., 2026 ) , verbalized confidence elicited in text ( Lin et al., 2022 ; Taubenfeld et al., 2025 ) , and P(True) ( Kadavath et al., 2022 ) . Previous studies have demonstrated that these reliability-aware aggregation methods outperform Standard MV. However, these signals often fail to separate correct from wrong traces on difficult problems, the regime where Standard MV most needs improvement (Figure 2 ).

We introduce a novel reliability signal, prefix consistency , and incorporate it into WMV. This signal is motivated by the observation that correct reasoning traces tend to be more reproducible under regeneration than incorrect ones. We truncate each sample’s CoT at a specified fraction and regenerate continuations from the prefix (Figure 1 ). Prefix consistency requires no access to token log-probabilities. Since regenerated answers also participate in voting, our method recovers correct answers absent from the initial samples.

Our contributions are: 1. We propose prefix consistency , a reliability signal that truncates each sample’s CoT and regenerates from the prefix, and use it to form prefix-consistency-weighted majority voting (PC-WMV). PC-WMV requires no access to token log-probabilities.

2. Across 4 benchmarks and 5 model scales, prefix consistency outperforms existing WMV baselines (e.g. DeepConf, P(True), Self-certainty) as a correctness predictor (best macro-averaged AUROC on 15 out of 20 (model, benchmark) cells, .63–.80). On many problems with Pass@1 below 50%, where Standard MV fails by default, prefix consistency still discriminates correct from wrong traces (Section 4.4 ), leaving room for PC-WMV to find the correct answer.

3. In cost-equivalent comparison against the primary WMV baselines (DeepConf tail, P(True), Self-certainty) and adaptive-stopping baselines (AC, ESC), PC-WMV is the most cost-efficient on the majority of the 20 (model, benchmark) settings, reaching Standard MV plateau at a median 4.6 × 4.6\times fewer tokens (up to 21 × 21\times vs. Standard MV and 10 × 10\times vs. AC sweep, Figure 1 and Table 4 ).

## 2 Preliminary

We consider a benchmark 𝒬 \mathcal{Q} , a set of problems. For each problem q ∈ 𝒬 q\in\mathcal{Q} , we have an answer space 𝒜 \mathcal{A} and a correct answer a q ⋆ ∈ 𝒜 a^{\star}_{q}\in\mathcal{A} . Given q q , an LLM generates a trace y y , i.e., a sequence of tokens that represents a CoT followed by a final summary, from which we parse the final answer a ∈ 𝒜 a\in\mathcal{A} . We write ( y , a ) ∼ LLM ( ⋅ ∣ q ) (y,a)\sim\mathrm{LLM}(\cdot\mid q) . We write Pass @ 1 q := Pr ( y , a ) ∼ LLM ( ⋅ ∣ q ) [ a = a q ⋆ ] \mathrm{Pass@1}_{q}:=\Pr_{(y,a)\sim\mathrm{LLM}(\cdot\mid q)}[a=a^{\star}_{q}] for the per-problem single-sample success probability, and report the macro-average over 𝒬 \mathcal{Q} as the benchmark-level Pass@1. When the context is clear, we suppress q q in the notation (e.g., a ⋆ a^{\star} instead of a q ⋆ a^{\star}_{q} ).

To improve the accuracy over Pass@1 at test time, we draw N N independent samples { ( y i , a i ) } i = 1 N \{(y_{i},a_{i})\}_{i=1}^{N} and aggregate them into a single output. A standard method that aggregates the N N answers is majority voting (MV, also known as self-consistency), which returns the most frequent answer: a ^ N MV = arg ​ max a ∈ 𝒜 ∑ i = 1 N 𝟏 [ a i = a ] . \hat{a}^{\mathrm{MV}}_{N}=\argmax_{a\in\mathcal{A}}\sum_{i=1}^{N}\mathbf{1}[a_{i}=a]. (1)

We refer to this unweighted aggregator as Standard MV (Eq. ( 1 )). Standard MV treats all samples equally and fails when the correct answer is not the mode of the answer distribution, typically observed when an LLM faces challenging problems where Pass@1 accuracy is below 50%. A natural extension is weighted majority voting (WMV), where each sample i i contributes a weighted vote v i ​ ( a ) ≥ 0 v_{i}(a)\geq 0 for answer a a : a ^ N WMV = arg ​ max a ∈ 𝒜 ∑ i = 1 N v i ( a ) . \hat{a}^{\mathrm{WMV}}_{N}=\argmax_{a\in\mathcal{A}}\sum_{i=1}^{N}v_{i}(a). (2)

For sample i i , let ℓ i \ell_{i} denote the model’s token-level log-probabilities available to the signal. Prior WMV methods extract a confidence signal s ⁡ ( y i , ℓ i ) ≥ 0 s(y_{i},\ell_{i})\geq 0 from the trace and apply a weighting function w : ℝ ≥ 0 → ℝ ≥ 0 w\colon\mathbb{R}_{\geq 0}\to\mathbb{R}_{\geq 0} to it: v i ( a ) = w ( s ( y i , ℓ i ) ) ⋅ 𝟏 [ a i = a ] . v_{i}(a)=w(s(y_{i},\ell_{i}))\cdot\mathbf{1}[a_{i}=a]. (3) Another class of WMV methods adopts verbalized signals that require no log-probability access ( ℓ i = ∅ \ell_{i}=\emptyset ), where s s depends only on the text of y i y_{i} . Other methods (Self-certainty, DeepConf, Response probability) set ℓ i \ell_{i} to the per-token log-probabilities along y i y_{i} . P(True) sets ℓ i \ell_{i} to the log-probability of the “True” token under a self-rating prompt. Appendix E gives the explicit form of s s and w w for each baseline. However, such confidence signals often fail to separate correct traces from wrong traces on difficult problems. We next introduce prefix consistency, a signal that requires no log-probability access ( ℓ i = ∅ \ell_{i}=\emptyset ).

## 3 Prefix Consistency

We propose prefix consistency, a reliability signal: truncate each sample’s CoT at an intermediate point and regenerate its continuation, treating samples whose initial answer reappears as more reliable than those whose answer changes (Figure 1 ).

### 3.1 Prefix Consistency as a Reliability Signal

For each sample ( y i , a i ) (y_{i},a_{i}) , let | y i | |y_{i}| denote the number of tokens in y i y_{i} . We truncate y i y_{i} after its first ⌈ τ ​ | y i | ⌉ \lceil\tau|y_{i}|\rceil tokens for a fixed fraction τ ∈ ( 0 , 1 ) \tau\in(0,1) , and regenerate K K continuations from this prefix, yielding the multiset: A i ( τ , K ) = { a i , a ~ i , 1 ( τ ) , … , a ~ i , K ( τ ) } . A_{i}^{(\tau,K)}=\{a_{i},\,\tilde{a}_{i,1}^{(\tau)},\ldots,\tilde{a}_{i,K}^{(\tau)}\}. (4) We refer to A i ( τ , K ) A_{i}^{(\tau,K)} as the i i -th group . For the following discussion, we focus on the case when K = 1 K=1 . We will write A i ( τ ) A_{i}^{(\tau)} for A i ( τ , 1 ) A_{i}^{(\tau,1)} and write a ~ i ( τ ) \tilde{a}_{i}^{(\tau)} for a ~ i , 1 ( τ ) \tilde{a}_{i,1}^{(\tau)} . Extending this to arbitrary K K is straightforward.

The key empirical phenomenon is a reproduction-rate asymmetry : a regenerated answer is more likely to match the initial answer when the initial answer is correct. Let r C ​ ( τ ) r_{C}(\tau) and r W ​ ( τ ) r_{W}(\tau) denote the probabilities of reproducing the initial answer, conditioned on whether it is correct or wrong: r C ​ ( τ ) := Pr ⁡ [ a ~ i ( τ ) = a i ∣ a i = a ⋆ ] , r W ​ ( τ ) := Pr ⁡ [ a ~ i ( τ ) = a i ∣ a i ≠ a ⋆ ] r_{C}(\tau):=\Pr[\tilde{a}_{i}^{(\tau)}=a_{i}\mid a_{i}=a^{\star}],\qquad r_{W}(\tau):=\Pr[\tilde{a}_{i}^{(\tau)}=a_{i}\mid a_{i}\neq a^{\star}] (5) Across models and benchmarks, we consistently observe the following inequality (Table 1 ): r C ​ ( τ ) > r W ​ ( τ ) . r_{C}(\tau)>r_{W}(\tau). (6) In other words, when the initial answer is correct, regeneration from its prefix tends to produce the same answer. When the initial answer is incorrect, regeneration more often produces a different incorrect answer than the same incorrect answer. Figure 2 illustrates this asymmetry on FrontierScience-Olympiad with GPT-OSS-120B and contrasts it with two baseline signals (DeepConf tail and P(True)) that fail to distinguish between correct and incorrect traces.

To exploit this observation, we score each candidate a ∈ A i ( τ ) a\in A_{i}^{(\tau)} by its reproducibility within the group: c i ( τ ) ( a ) := | { a ′ ∈ A i ( τ ) : a ′ = a } | 2 . c_{i}^{(\tau)}(a):=\frac{|\{a^{\prime}\in A_{i}^{(\tau)}:a^{\prime}=a\}|}{2}. (7) We denote the prefix consistency score of a a in group i i by c i ( τ ) ​ ( a ) ∈ { 0 , 1 / 2 , 1 } c_{i}^{(\tau)}(a)\in\{0,1/2,1\} . Unlike conventional per-sample reliability signals (e.g., DeepConf tail, P(True)), which assign a single scalar to each sample’s initial answer, c i ( τ ) ​ ( a ) c_{i}^{(\tau)}(a) is defined for every candidate a ∈ A i ( τ ) a\in A_{i}^{(\tau)} , including regenerated answers that did not appear among the initial answers.

### 3.2 Prefix-Consistency-Weighted Majority Voting (Algorithm 1 )

We set the WMV weight in Eq. ( 2 ) using Eq. ( 7 ): v i ​ ( a ) = w ⁡ ( c i ( τ ) ​ ( a ) ) v_{i}(a)\;=\;w\!\left(c_{i}^{(\tau)}(a)\right) (8) where w : [ 0 , 1 ] → ℝ ≥ 0 w\colon[0,1]\to\mathbb{R}_{\geq 0} with w ⁡ ( 0 ) = 0 w(0)=0 .

We refer to this method as prefix-consistency-weighted majority voting (PC-WMV) (Algorithm 1 ). Since Eq. ( 8 ) weights every distinct a ∈ A i ( τ ) a\in A_{i}^{(\tau)} rather than only the initial answer a i a_{i} , PC-WMV’s aggregated vote ∑ i v i ​ ( a ) \sum_{i}v_{i}(a) can be positive for regenerated answers absent from the initial N N samples. This is the operational consequence of using a per-candidate signal rather than a per-sample one.

We now demonstrate that this additional flexibility results in a clear advantage over Standard MV in situations where Standard MV is proven to fail. Standard MV fails when the correct answer occurs less frequently than a wrong answer. The following theorem, in the simplest case of a binary answer space, demonstrates how PC-WMV uses the reproduction-rate asymmetry to recover the correct answer in this regime.

The formal proof of Theorem 1 is in Appendix C.3 .

##### Hyperparameters.

Prefix consistency has two hyperparameters: the truncation fraction τ ∈ ( 0 , 1 ) \tau\in(0,1) and the number of regenerations per group K ∈ ℕ K\in\mathbb{N} . PC-WMV adds a third, the weighting function w : [ 0 , 1 ] → ℝ ≥ 0 w\colon[0,1]\to\mathbb{R}_{\geq 0} with w ⁡ ( 0 ) = 0 w(0)=0 .

## 4 Experiments

We conduct experiments on science (FrontierScience-Olympiad ( Wang et al., 2025 ) ) and math (HMMT Feb 2026, AIME 2025, Brumo 2025 ( Balunović et al., 2025 ) ) datasets. We evaluate on five reasoning LLMs: GPT-OSS-120B, GPT-OSS-20B ( OpenAI, 2025 ) , Nemotron3-30B ( NVIDIA-Nemotron-3-Nano-30B-A3B-BF16 ) ( NVIDIA, 2025a ) , Nemotron2-9B ( NVIDIA-Nemotron-Nano-9B-v2 ) ( NVIDIA, 2025b ) , and Ministral3-14B ( Ministral-3-14B-Reasoning-2512 ) ( Mistral AI, 2026 ) .

We compare our proposed methods against Standard MV, three primary WMV baselines (Self-certainty ( Kang et al., 2025 ) , DeepConf tail ( Fu et al., 2026 ) , and P(True) ( Kadavath et al., 2022 ; Taubenfeld et al., 2025 ) ), and two adaptive-stopping rules over MV (Adaptive Consistency, AC ( Aggarwal et al., 2023 ) , and Early-Stopping Self-Consistency, ESC ( Li et al., 2024 ) ). The details of these methods are documented in Appendix E .

##### Hyperparameters of prefix consistency.

Unless otherwise specified, we fix the truncation fraction at τ = 0.75 \tau=0.75 . The results in the main paper use K = 1 K=1 throughout. We accordingly suppress τ \tau in the notation and write c i ​ ( a ) , r C , r W , D c_{i}(a),r_{C},r_{W},D for c i ( τ ) ​ ( a ) , r C ​ ( τ ) , r W ​ ( τ ) , D ⁡ ( τ ) c_{i}^{(\tau)}(a),r_{C}(\tau),r_{W}(\tau),D(\tau) .

### 4.1 Prefix Consistency as a Correctness Predictor

We report AUROC ¯ \overline{\mathrm{AUROC}} , the macro-averaged AUROC over problems with at least one correct and one wrong initial sample (formal definition in Appendix G.2 ).

Note that some previous work ( Xiong et al., 2024 ; Fadeeva et al., 2024 ) adopted AUROC pooled across problems, which differs from AUROC ¯ \overline{\mathrm{AUROC}} . However, as argued in Taubenfeld et al. (2025) , such an AUROC pooled across problems conflates within-problem discrimination with cross-problem score-difficulty correlation, and only the former predicts whether confidence-weighted self-consistency improves over Standard MV. They also report that calibration metrics such as Expected Calibration Error (ECE) and Brier score are similarly unsuitable. In their data, the best-calibrated source (verbalized binary) gave the smallest improvement while the strongest method (P(True) therein) was only moderately calibrated. At vote time, every WMV method (including PC-WMV and all baselines) compares scores only among samples from the same problem, and thus we consider AUROC ¯ \overline{\mathrm{AUROC}} to better measure discriminative ability between correct traces and wrong traces.

Table 1 reports the discrimination gap D = r C − r W D=r_{C}-r_{W} for prefix consistency: D > 0 D>0 on every (model, benchmark) cell, confirming the asymmetry r C > r W r_{C}>r_{W} . Table 2 reports AUROC ¯ \overline{\mathrm{AUROC}} for prefix consistency against the WMV baselines. Prefix consistency has the highest AUROC ¯ \overline{\mathrm{AUROC}} on 15 15 of 20 20 cells (typically around 0.7 0.7 ), separating correct from wrong traces more clearly than the baselines. Baselines’ AUROC ¯ \overline{\mathrm{AUROC}} often hovers near 0.5 0.5 (= random 1 1 1 AUROC ¯ = 0.5 \overline{\mathrm{AUROC}}=0.5 is the value attained by a random signal that is uninformative about correctness. ) on harder cells, where their scores differ little between correct and wrong samples, reaching ∼ 0.7 \sim 0.7 only on some easier cells.

Abbreviations: FSci = FrontierScience-Olympiad, HMMT = HMMT Feb 2026, AIME = AIME 2025, Brumo = Brumo 2025.

### 4.2 Weighted Majority Voting Results

We compare PC-WMV against existing WMV methods under the same computational cost.

##### Weighting variants.

We use the power family w ( n ) ​ ( c ) = c n w^{(n)}(c)=c^{n} for n ∈ { 1 , 2 , 3 } n\in\{1,2,3\} , denoted PC-linear, PC-quadratic, and PC-cubic, where the “PC” prefix abbreviates prefix consistency. Under K = 1 K=1 , c i ​ ( a ) ∈ { 0 , 1 / 2 , 1 } c_{i}(a)\in\{0,1/2,1\} . Thus, a candidate that is reproduced under regeneration ( c = 1 c=1 ) receives weight 1 1 , while a candidate that appears in only one of the two traces ( c = 1 / 2 c=1/2 ) receives weight 1 / 2 n 1/2^{n} . The weight ratio between a reproduced candidate and a single-trace one is therefore 2 n : 1 2^{n}:1 , that is, 2 : 1 2:1 for linear, 4 : 1 4:1 for quadratic, and 8 : 1 8:1 for cubic. The larger n n is, the more pronounced the relative weight given to reproduced answers.

##### Cost-equivalent evaluation.

We measure inference cost by the total number of generated tokens, treating each generated token as equally expensive, and log-probability access as free. For each model and benchmark, we first generate N = 128 N{=}128 initial samples per problem ( N = 64 N{=}64 for Ministral3-14B), from which all methods sample with replacement under a common token budget B B . See Appendix G for the pool construction, trial design, and confidence-interval definition.

Table 3 reports accuracy under fixed token budgets (250k, 1M, and 5M tokens) across the three models and four benchmarks. At 1M tokens, prefix consistency matches or exceeds all baselines on the more difficult benchmarks (FrontierScience-Olympiad, HMMT Feb 2026), while the advantage is smaller on AIME 2025 where Standard MV already achieves high accuracy. The improvements are consistent across weighting functions (PC-linear, PC-quadratic, and PC-cubic). PC-cubic provides the greatest improvement for the most difficult problems. Per-model tables with the full set of baselines (DeepConf variants, Response probability, verbalized confidence, P(True)) for all five models, including the two not shown above (GPT-OSS-20B, Nemotron2-9B), are reported in Appendix D.3 .

### 4.3 Token Efficiency

Section 4.2 reported accuracy under fixed budget constraints. We next compare how many tokens each method needs to reach the same target accuracy.

Table 4 shows the token-efficiency ratio B method / B MV B_{\mathrm{method}}/B_{\mathrm{MV}} , where B X B_{X} is the budget method X X needs to reach the target accuracy Pass@1 + α × +\,\alpha\times (Standard MV plateau − - Pass@1) for α ∈ { 75 % , 90 % , 99 % } \alpha\in\{75\%,90\%,99\%\} . The Standard MV plateau is Standard MV’s bootstrap-saturated accuracy on the N N -sample pool (Appendix G.3 ), so α \alpha interpolates between Pass@1 ( α = 0 \alpha{=}0 ) and this plateau ( α = 1 \alpha{=}1 ). A ratio < 1 <1 means X X is more cost-efficient than Standard MV at the target; e.g., 0.05 × 0.05\times corresponds to the 21 × 21\times saving in Figure 1 . The headline numbers in this paper (median 4.6 × 4.6\times , up to 21 × 21\times vs. Standard MV, up to 10 × 10\times vs. AC sweep) are computed at α = 99 % \alpha{=}99\% across all 20 20 (model, benchmark) cells: Table 4 together with Table 12 (GPT-OSS-20B) and Table 14 (Nemotron2-9B) in Appendix D.3 .

PC-cubic is more cost-efficient than Standard MV on 11 11 out of 12 12 model and benchmark settings at α = 99 % \alpha{=}99\% . The strongest savings are 0.05 × 0.05\times on both FrontierScience-Olympiad with GPT-OSS-120B and AIME 2025 with Ministral3-14B, and 0.08 × 0.08\times on FrontierScience-Olympiad with Ministral3-14B. All three correspond to cells with large D D (Table 1 ).

The savings track the discrimination gap D D (Table 1 ): pairs with the largest D D yield the largest reductions. PC-cubic offers little advantage over Standard MV on two cells (it underperforms on Nemotron3-30B AIME 2025 and only marginally beats Standard MV on Nemotron3-30B HMMT Feb 2026), both of which have a small Pass@1-to-plateau gap of at most .11 .11 ( .902 → .967 .902\to.967 and .708 → .810 .708\to.810 ), leaving little room above Pass@1 for any reweighting irrespective of D D . The practical penalty in this regime, where Pass@1 is close to Standard MV plateau, is correspondingly small.

##### Comparison with adaptive-stopping baselines.

PC-cubic is competitive with or better than AC sweep on most cells and outperforms ESC sweep at α = 99 % \alpha{=}99\% on every (model, benchmark) cell except Nemotron3-30B on AIME 2025, despite being a non-adaptive reweighting of the same initial pool that AC and ESC consume sequentially. The advantage is most pronounced on large- D D cells (FrontierScience-Olympiad on every model, and most Ministral3-14B benchmarks), e.g. PC-cubic at 0.05 × 0.05\times vs. AC sweep at 0.29 × 0.29\times at α = 99 % \alpha{=}99\% on GPT-OSS-120B FrontierScience-Olympiad.

AC substantially outperforms PC only on the two cells noted above where Pass@1 is close to Standard MV plateau (Nemotron3-30B on AIME 2025 and HMMT Feb 2026), since the aggregated vote on wrong answers is small and AC’s early stop alone bounds the cost. However, on 2 2 out of 12 12 (model, benchmark) cells at α = 99 % \alpha{=}99\% (marked “N/A” in Table 4 ) AC’s accuracy never reaches Standard MV plateau, because its early-stop rule terminates generation before the running accuracy reaches the α = 99 % \alpha{=}99\% target. PC-cubic reaches the target on all 12 12 .

ESC stops at the first fixed-size window of samples that all share the same answer, which is too strict on benchmarks where wrong answers are diverse, so ESC either stops well after AC or fails to stop within the budget. PC and adaptive stopping act on orthogonal axes: PC reweights votes while AC and ESC decide when to stop sampling. A hybrid that votes by PC weights and stops by the AC rule would combine AC’s cost bound on easy cells with PC’s accuracy on difficult ones (left to future work).

##### Remark on the cost accounting.

Treating log-probability access as free is implementation-dependent but holds for our vLLM setup. This favors baselines that read log-probabilities of the initial trace without generating extra tokens (Self-certainty, DeepConf, Response probability), while prefix consistency spends budget on the regeneration tokens. Even so, the PC-WMV has significant advantage. Imposing any cost for log-probability retrieval only widens the margin.

Additional results on token-efficiency ratios are reported per model in Appendix D.3 .

### 4.4 How Problem Difficulty Affects the Discrimination Gap D D

The discrimination gap D D determines where prefix consistency improves WMV (Theorem 1 ), so we now study how D D varies with problem difficulty, indexed by Pass@1.

Figure 3 plots per-problem r C r_{C} and r W r_{W} as a function of Pass@1 for three of the five models (the remaining two are in Appendix D.7.1 ), stratified by category. Across all five models, r C r_{C} rises with problem easiness, r W r_{W} depends on the model and category but only weakly on Pass@1, and D = r C − r W D=r_{C}-r_{W} inherits both. We discuss r C r_{C} and r W r_{W} in turn below.

First, r C r_{C} (solid lines) increases with Pass@1 for both categories. Pass@1 here indexes problem easiness within a fixed model, and on easier problems, the correct answer is more reliably reproduced under regeneration. Logistic generalized linear model (GLM) slopes β ⁡ ( r C ) \beta(r_{C}) on logit ​ ( r ) = β 0 + β ⋅ Pass@1 \text{logit}(r)=\beta_{0}+\beta\cdot\text{Pass@1} range from + 2.7 +2.7 to + 5.1 +5.1 across the six (model, category) pairs shown in Figure 3 , all significantly positive (cluster-bootstrap p < 0.005 p<0.005 , see Appendix D.7.1 ).

Second, r W r_{W} (dashed lines) depends more weakly on Pass@1 than r C r_{C} : | β ⁡ ( r W ) | ≤ 1.14 |\beta(r_{W})|\leq 1.14 across the six pairs, and among four out of six curves, we cannot statistically reject β = 0 \beta=0 at a 2 ​ σ 2\sigma confidence level. For the remaining two non-zero slopes, β \beta is + 1.14 +1.14 (GPT-OSS-120B Math) and − 0.75 -0.75 (Ministral3-14B Math), with opposite signs, both smaller in magnitude than the smallest r C r_{C} slope. The level of r W r_{W} varies by category, sitting at ∼ {\sim} 15–40% on Science and ∼ {\sim} 25–60% on Math. Math errors may reflect internally consistent miscalculations and science errors may reflect more diffuse knowledge gaps, but this is a hypothesis: our results establish r C > r W r_{C}>r_{W} as a behavioral regularity, and a mechanistic verification (e.g., calculation-heavy vs. concept-heavy subsets) is left to future work.

The finding that D D widens on easier cells may appear to conflict with the “savings track D D ” claim of Section 4.3 , since easier cells also have a smaller gap between Pass@1 and Standard MV plateau. The two reconcile by noting that PC-WMV’s advantage over Standard MV depends on both D D and the gap above Pass@1: a large D D pays off only when there is room to reweight votes, which is why the two cells where PC-cubic offers little advantage over Standard MV are precisely the cells with Pass@1 concentrated within ∼ .10 {\sim}.10 of Standard MV plateau (Nemotron3-30B on AIME 2025 and HMMT Feb 2026).

## 5 Conclusion

We introduced prefix consistency, a reliability signal for weighted majority voting that truncates each CoT and checks whether answers reproduce under regeneration. Across benchmarks, prefix consistency is a stronger correctness predictor than existing baselines, and PC-WMV improves upon existing weighted majority voting methods under cost-equivalent comparison, especially on more difficult benchmarks. Our analysis highlights the discrimination gap D = r C − r W D=r_{C}-r_{W} as the key quantity governing when the method helps: PC-WMV is most effective when D > 0 D>0 and Pass@1 leaves a meaningful gap below Standard MV plateau. Regeneration stability is thus a practically useful test-time signal for aggregating votes, not merely a descriptive property of Chain-of-Thought.

## References

Aggarwal et al. (2026) P. Aggarwal, S. Kim, J. Lanchantin, S. Welleck, J. Weston, I. Kulikov, and S. Saha OptimalThinkingBench: Evaluating Over and Underthinking in LLMs . In The Fourteenth International Conference on Learning Representations , External Links: Link Cited by: §A.2 .

Aggarwal et al. (2023) P. Aggarwal, A. Madaan, Y. Yang, and Mausam Let’s Sample Step by Step: Adaptive-Consistency for Efficient Reasoning and Coding with LLMs . In Proceedings of the 2023 Conference on Empirical Methods in Natural Language Processing , H. Bouamor, J. Pino, and K. Bali (Eds.) , Singapore , pp. 12375–12396 . External Links: Link , Document Cited by: §A.1 , 3rd item , Appendix E , §4 .

Anthropic (2026) Anthropic Claude Sonnet 4.6 System Card . External Links: Link Cited by: §D.6 .

Balunović et al. (2025) M. Balunović, J. Dekoninck, I. Petrov, N. Jovanović, and M. Vechev MathArena: Evaluating LLMs on Uncontaminated Math Competitions . In Thirty-ninth Conference on Neural Information Processing Systems Datasets and Benchmarks Track , External Links: Link Cited by: §H.2 , Table 24 , Table 24 , Table 24 , §4 .

Besta et al. (2024) M. Besta, N. Blach, A. Kubicek, R. Gerstenberger, M. Podstawski, L. Gianinazzi, J. Gajda, T. Lehmann, H. Niewiadomski, P. Nyczyk, and T. Hoefler Graph of Thoughts: Solving Elaborate Problems with Large Language Models . Proceedings of the AAAI Conference on Artificial Intelligence 38 ( 16 ), pp. 17682–17690 . External Links: Link , Document Cited by: §A.1 .

Boppana et al. (2026) S. Boppana, A. Ma, M. Loeffler, R. Sarfati, E. Bigelow, A. Geiger, O. Lewis, and J. Merullo Reasoning Theater: Disentangling Model Beliefs from Chain-of-Thought . arXiv preprint arXiv:2603.05488 . External Links: Link Cited by: §A.2 .

Chen et al. (2025) X. Chen, J. Xu, T. Liang, Z. He, J. Pang, D. Yu, L. Song, Q. Liu, M. Zhou, Z. Zhang, R. Wang, Z. Tu, H. Mi, and D. Yu Do NOT Think That Much for 2+3=?: On the Overthinking of Long Reasoning Models . In Proceedings of the 42nd International Conference on Machine Learning , Proceedings of Machine Learning Research , Vol. 267 , pp. 9487–9499 . External Links: Link Cited by: §A.2 .

Fadeeva et al. (2024) E. Fadeeva, A. Rubashevskii, A. Shelmanov, S. Petrakov, H. Li, H. Mubarak, E. Tsymbalov, G. Kuzmin, A. Panchenko, T. Baldwin, P. Nakov, and M. Panov Fact-checking the output of large language models via token-level uncertainty quantification . In Findings of the Association for Computational Linguistics: ACL 2024 , L. Ku, A. Martins, and V. Srikumar (Eds.) , Bangkok, Thailand , pp. 9367–9385 . External Links: Link , Document Cited by: §4.1 .

Faria et al. (2024) G. R. A. Faria, S. Agrawal, A. Farinhas, R. Rei, J. G. C. de Souza, and A. F. T. Martins QUEST: Quality-Aware Metropolis-Hastings Sampling for Machine Translation . In Advances in Neural Information Processing Systems , Vol. 37 . External Links: Link Cited by: §A.1 .

Faria and Smith (2025) G. Faria and N. A. Smith Sample, Don’t Search: Rethinking Test-Time Alignment for Language Models . arXiv preprint arXiv:2504.03790 . External Links: Link Cited by: §A.1 .

Feng et al. (2025) Y. Feng, J. Kempe, C. Zhang, P. Jain, and A. Hartshorn What Characterizes Effective Reasoning? Revisiting Length, Review, and Structure of CoT . In NeurIPS 2025 Workshop on Efficient Reasoning , Note: Spotlight External Links: Link Cited by: §A.1 .

Fu et al. (2023) Y. Fu, H. Peng, A. Sabharwal, P. Clark, and T. Khot Complexity-Based Prompting for Multi-step Reasoning . In The Eleventh International Conference on Learning Representations , External Links: Link Cited by: §1 .

Fu et al. (2026) Y. Fu, X. Wang, H. Zhang, Y. Tian, and J. Zhao Deep Think with Confidence . In The Fourteenth International Conference on Learning Representations , External Links: Link Cited by: §A.1 , §D.3 , 1st item , Appendix E , §1 , §4 .

Gan et al. (2025) Z. Gan, Y. Liao, and Y. Liu Rethinking External Slow-Thinking: From Snowball Errors to Probability of Correct Reasoning . In Forty-second International Conference on Machine Learning , External Links: Link Cited by: §A.2 .

Hammoud et al. (2025) H. A. A. K. Hammoud, H. Itani, and B. Ghanem Beyond the Last Answer: Your Reasoning Trace Uncovers More than You Think . arXiv preprint arXiv:2504.20708 . External Links: Link Cited by: §A.1 , §D.3 , 4th item , Appendix E .

Jiang et al. (2025) E. Jiang, C. Xu, N. Singh, T. Qiu, and G. Singh Robust Answers, Fragile Logic: Probing the Decoupling Hypothesis in LLM Reasoning . arXiv preprint arXiv:2505.17406 . External Links: Link Cited by: §A.2 .

Jindal et al. (2026) I. Jindal, S. P. Akuthota, J. Taneja, and S. D. SHARMA THE PATH OF LEAST RESISTANCE: GUIDING LLM REASONING TRAJECTORIES WITH PREFIX CONSENSUS . In The Fourteenth International Conference on Learning Representations , External Links: Link Cited by: §A.1 .

Kadavath et al. (2022) S. Kadavath, T. Conerly, A. Askell, T. Henighan, D. Drain, E. Perez, N. Schiefer, Z. Hatfield-Dodds, N. DasSarma, E. Tran-Kemp, S. Johnston, S. El-Showk, A. Jones, N. Elhage, T. Hume, A. Chen, Y. Bai, S. Bowman, S. Fort, D. Ganguli, D. Hernandez, J. Jacobson, J. Kernion, S. Kravec, L. Lovitt, K. Ndousse, C. Olsson, S. Ringer, D. Amodei, T. Brown, J. Clark, N. Joseph, B. Mann, S. McCandlish, C. Olah, and J. Kaplan Language Models (Mostly) Know What They Know . arXiv preprint arXiv:2207.05221 . External Links: Link Cited by: §D.3 , 2nd item , Appendix E , §1 , §4 .

Kang et al. (2025) Z. Kang, X. Zhao, and D. Song Scalable Best-of-N Selection for Large Language Models via Self-Certainty . In Advances in Neural Information Processing Systems , External Links: Link Cited by: §A.1 , 1st item , Appendix E , §1 , §4 .

Kim et al. (2025) J. Kim, D. Wu, J. D. Lee, and T. Suzuki Metastable Dynamics of Chain-of-Thought Reasoning: Provable Benefits of Search, RL and Distillation . In Forty-second International Conference on Machine Learning , External Links: Link Cited by: §A.2 .

Kojima et al. (2022) T. Kojima, S. (. Gu, M. Reid, Y. Matsuo, and Y. Iwasawa Large Language Models are Zero-Shot Reasoners . In Advances in Neural Information Processing Systems , Vol. 35 , pp. 22199–22213 . External Links: Link Cited by: §1 .

Komiyama et al. (2026) J. Komiyama, D. Oba, and M. Oyamada Best-of- ∞ \infty : Asymptotic Performance of Test-Time LLM Ensembling . In The Fourteenth International Conference on Learning Representations , External Links: Link Cited by: §A.1 .

Lanham et al. (2023) T. Lanham, A. Chen, A. Radhakrishnan, B. Steiner, C. Denison, D. Hernandez, D. Li, E. Durmus, E. Hubinger, J. Kernion, K. Lukošiūtė, K. Nguyen, N. Cheng, N. Joseph, N. Schiefer, O. Rausch, R. Larson, S. McCandlish, S. Kundu, S. Kadavath, S. Yang, T. Henighan, T. Maxwell, T. Telleen-Langton, T. Hume, Z. Hatfield-Dodds, J. Kaplan, J. Brauner, S. R. Bowman, and E. Perez Measuring Faithfulness in Chain-of-Thought Reasoning . arXiv preprint arXiv:2307.13702 . External Links: Link Cited by: §A.2 .

Li et al. (2024) Y. Li, P. Yuan, S. Feng, B. Pan, X. Wang, B. Sun, H. Wang, and K. Li Escape Sky-high Cost: Early-stopping Self-Consistency for Multi-step Reasoning . In The Twelfth International Conference on Learning Representations , External Links: Link Cited by: §A.1 , 3rd item , Appendix E , §4 .

Lightman et al. (2024) H. Lightman, V. Kosaraju, Y. Burda, H. Edwards, B. Baker, T. Lee, J. Leike, J. Schulman, I. Sutskever, and K. Cobbe Let’s Verify Step by Step . In The Twelfth International Conference on Learning Representations , External Links: Link Cited by: §A.1 .

Lin et al. (2022) S. Lin, J. Hilton, and O. Evans Teaching Models to Express Their Uncertainty in Words . Transactions on Machine Learning Research . Note: External Links: ISSN 2835-8856 , Link Cited by: 2nd item , Appendix E , Appendix E , §1 .

Lu et al. (2022) P. Lu, S. Mishra, T. Xia, L. Qiu, K. Chang, S. Zhu, O. Tafjord, P. Clark, and A. Kalyan Learn to Explain: Multimodal Reasoning via Thought Chains for Science Question Answering . In Advances in Neural Information Processing Systems , A. H. Oh, A. Agarwal, D. Belgrave, and K. Cho (Eds.) , External Links: Link Cited by: §1 .

Mistral AI (2026) Mistral AI Ministral 3 . arXiv preprint arXiv:2601.08584 . External Links: Link Cited by: Table 24 , §4 .

Muennighoff et al. (2025) N. Muennighoff, Z. Yang, W. Shi, X. L. Li, L. Fei-Fei, H. Hajishirzi, L. Zettlemoyer, P. Liang, E. Candès, and T. Hashimoto S1: Simple test-time scaling . In Proceedings of the 2025 Conference on Empirical Methods in Natural Language Processing , C. Christodoulopoulos, T. Chakraborty, C. Rose, and V. Peng (Eds.) , Suzhou, China , pp. 20275–20321 . External Links: Link , Document , ISBN 979-8-89176-332-6 Cited by: §A.1 .

NVIDIA (2025a) NVIDIA Nemotron 3 Nano: Open, Efficient Mixture-of-Experts Hybrid Mamba-Transformer Model for Agentic Reasoning . arXiv preprint arXiv:2512.20848 . External Links: Link Cited by: Table 24 , §4 .

NVIDIA (2025b) NVIDIA NVIDIA Nemotron Nano 2: An Accurate and Efficient Hybrid Mamba-Transformer Reasoning Model . arXiv preprint arXiv:2508.14444 . External Links: Link Cited by: Table 24 , §4 .

OpenAI (2025) OpenAI Gpt-oss-120b & gpt-oss-20b Model Card . arXiv preprint arXiv:2508.10925 . External Links: Link Cited by: Table 24 , Table 24 , §4 .

Parashar et al. (2025) S. Parashar, B. Olson, S. Khurana, E. Li, H. Ling, J. Caverlee, and S. Ji Inference-Time Computations for LLM Reasoning and Planning: A Benchmark and Insights . arXiv preprint arXiv:2502.12521 . External Links: Link Cited by: §A.1 .

Pu et al. (2025) X. Pu, M. Saxon, W. Hua, and W. Y. Wang ThoughtTerminator: Benchmarking, Calibrating, and Mitigating Overthinking in Reasoning Models . In Second Conference on Language Modeling , External Links: Link Cited by: §A.2 .

Scalena et al. (2025) D. Scalena, L. Zotos, E. Fersini, M. Nissim, and A. Üstün EAGER: Entropy-Aware GEneRation for Adaptive Inference-Time Scaling . arXiv preprint arXiv:2510.11170 . External Links: Link Cited by: §A.1 .

Sharma and Chopra (2025) A. Sharma and P. Chopra The Sequential Edge: Inverse-Entropy Voting Beats Parallel Self-Consistency at Matched Compute . arXiv preprint arXiv:2511.02309 . External Links: Link Cited by: §A.1 .

Taubenfeld et al. (2025) A. Taubenfeld, T. Sheffer, E. Ofek, A. Feder, A. Goldstein, Z. Gekhman, and G. Yona Confidence Improves Self-Consistency in LLMs . In Findings of the Association for Computational Linguistics: ACL 2025 , W. Che, J. Nabende, E. Shutova, and M. T. Pilehvar (Eds.) , Vienna, Austria , pp. 20090–20111 . External Links: Link , Document , ISBN 979-8-89176-256-5 Cited by: §A.1 , §D.3 , 2nd item , Appendix E , §1 , §4.1 , §4 .

Trivedi et al. (2023) H. Trivedi, N. Balasubramanian, T. Khot, and A. Sabharwal Interleaving Retrieval with Chain-of-Thought Reasoning for Knowledge-Intensive Multi-Step Questions . In Proceedings of the 61st Annual Meeting of the Association for Computational Linguistics (Volume 1: Long Papers) , A. Rogers, J. Boyd-Graber, and N. Okazaki (Eds.) , Toronto, Canada , pp. 10014–10037 . External Links: Link , Document Cited by: §1 .

von Recum et al. (2026) A. von Recum, L. Girrbach, and Z. Akata Are Reasoning LLMs Robust to Interventions on Their Chain-of-Thought? . In The Fourteenth International Conference on Learning Representations , External Links: Link Cited by: §A.2 .

Wang et al. (2023a) K. Wang, F. Duan, S. Wang, P. Li, Y. Xian, C. Yin, W. Rong, and Z. Xiong Knowledge-Driven CoT: Exploring Faithful Reasoning in LLMs for Knowledge-Intensive Question Answering . arXiv preprint arXiv:2308.13259 . External Links: Link Cited by: §1 .

Wang et al. (2024) L. Wang, Y. Hu, J. He, X. Xu, N. Liu, H. Liu, and H. T. Shen T-SciQ: teaching multimodal chain-of-thought reasoning via large language model signals for science question answering . In Proceedings of the AAAI Conference on Artificial Intelligence , Vol. 38 , pp. 19162–19170 . External Links: Document , Link Cited by: §1 .

Wang et al. (2025) M. Wang, R. Lin, K. Hu, J. Jiao, N. Chowdhury, E. Chang, and T. Patwardhan FrontierScience: Evaluating AI’s Ability to Perform Expert-Level Scientific Tasks . arXiv preprint arXiv:2601.21165 . External Links: Link Cited by: §H.2 , Table 24 , §4 .

Wang et al. (2023b) X. Wang, J. Wei, D. Schuurmans, Q. V. Le, E. H. Chi, S. Narang, A. Chowdhery, and D. Zhou Self-Consistency Improves Chain of Thought Reasoning in Language Models . In The Eleventh International Conference on Learning Representations , External Links: Link Cited by: §A.1 , 2nd item , Appendix E , §1 , §1 .

Wei et al. (2022) J. Wei, X. Wang, D. Schuurmans, M. Bosma, B. Ichter, F. Xia, E. Chi, Q. V. Le, and D. Zhou Chain-of-Thought Prompting Elicits Reasoning in Large Language Models . In Advances in Neural Information Processing Systems , Vol. 35 , pp. 24824–24837 . External Links: Link Cited by: §1 .

Wen et al. (2026) X. Wen, Z. Liu, S. Zheng, S. Ye, Z. Wu, Y. Wang, Z. Xu, X. Liang, J. Li, Z. Miao, J. Bian, and M. Yang Reinforcement Learning with Verifiable Rewards Implicitly Incentivizes Correct Reasoning in Base LLMs . In The Fourteenth International Conference on Learning Representations , External Links: Link Cited by: Appendix B .

Xiong et al. (2024) M. Xiong, Z. Hu, X. Lu, Y. Li, J. Fu, J. He, and B. Hooi Can LLMs Express Their Uncertainty? An Empirical Evaluation of Confidence Elicitation in LLMs . In The Twelfth International Conference on Learning Representations , External Links: Link Cited by: §A.1 , §4.1 .

Yao et al. (2023) S. Yao, D. Yu, J. Zhao, I. Shafran, T. L. Griffiths, Y. Cao, and K. Narasimhan Tree of Thoughts: Deliberate Problem Solving with Large Language Models . In Advances in Neural Information Processing Systems , Vol. 36 . External Links: Link Cited by: §A.1 .

Yu et al. (2025) T. Yu, Y. Jing, X. Zhang, W. Jiang, W. Wu, Y. Wang, W. Hu, B. Du, and D. Tao Benchmarking Reasoning Robustness in Large Language Models . arXiv preprint arXiv:2503.04550 . External Links: Link Cited by: §A.2 .

Zhang et al. (2025) A. Zhang, Y. Chen, J. Pan, C. Zhao, A. Panda, J. Li, and H. He Reasoning Models Know When They’re Right: Probing Hidden States for Self-Verification . In Second Conference on Language Modeling , External Links: Link Cited by: §A.2 .

Zhou et al. (2023) D. Zhou, N. Schärli, L. Hou, J. Wei, N. Scales, X. Wang, D. Schuurmans, C. Cui, O. Bousquet, Q. V. Le, and E. H. Chi Least-to-Most Prompting Enables Complex Reasoning in Large Language Models . In The Eleventh International Conference on Learning Representations , External Links: Link Cited by: §1 .

Zhu et al. (2024) J. Zhu, Y. Huang, Y. Shen, J. Zhao, and A. Zou Path-Consistency with Prefix Enhancement for Efficient Inference in LLMs . arXiv preprint arXiv:2409.01281 . External Links: Link Cited by: §A.1 .

## Appendix A Related Work

### A.1 Test-Time Scaling

##### Sequential and parallel scaling.

Test-time compute scaling comes in two paradigms. Sequential scaling extends a single reasoning chain, for example by appending continuation tokens to lengthen CoT [ Muennighoff et al., 2025 ] . Parallel scaling generates multiple independent solutions and aggregates them: self-consistency is the canonical instance, while tree search [ Yao et al., 2023 ] branches over candidate steps and process-reward verifiers rerank parallel samples [ Lightman et al., 2024 ] . Parashar et al. [2025] benchmarked a range of inference-time techniques across reasoning and planning tasks and reported that no single method is consistently best. Our method sits between the two: it uses parallel samples but introduces a structured perturbation (truncation + regeneration) that probes the robustness of each sample’s reasoning. Beyond aggregation, the same perturbation could serve as a quality estimate for partial reasoning states inside richer search procedures such as Graph-of-Thoughts [ Besta et al., 2024 ] , which extends Tree-of-Thoughts to a directed graph with refinement and aggregation operations.

##### Majority voting.

Wang et al. [2023b] introduced self-consistency for CoT reasoning: sample multiple reasoning traces and take the majority vote over extracted answers. A line of work targets the cost of self-consistency by stopping early. Aggarwal et al. [2023] introduced Adaptive Consistency, which evaluates a Beta-binomial posterior over the running top-1 and top-2 answer counts and stops once the posterior margin of the top answer crosses a threshold. Li et al. [2024] introduced Early-Stopping Self-Consistency, which inspects fixed-size windows of samples for unanimity and stops at the first unanimous window. Sharma and Chopra [2025] showed that sequential, entropy-aware voting can outperform parallel self-consistency at matched compute, highlighting the importance of cost-equivalent comparisons. Komiyama et al. [2026] analyzed the asymptotic behavior of majority voting (best-of- ∞ \infty ) and proposed a Bayesian nonparametric stopping rule. Our work is complementary: we assess the quality of each vote through regeneration weighting, which is compatible with the adaptive stopping rules above.

##### Confidence-based weighting.

Kang et al. [2025] proposed self-certainty , a trace-level quality score defined as the mean KL divergence of the per-token output distribution from uniform, and used it to rerank best-of- N N candidates. Fu et al. [2026] then extended self-certainty. In addition to the global trace mean (equivalent to self-certainty), they introduced a sliding-window group confidence and proposed the use of their bottom 10% (bottom-10% group confidence) and the mean over the final tokens of a trace (tail confidence) as alternative trace-level scores for confidence-weighted majority voting. Taubenfeld et al. [2025] demonstrated that combining self-assessed confidence (most effectively via P(True), the model’s own probability that its answer is correct) with self-consistency improves accuracy, though this still relies on the model’s introspective calibration. Xiong et al. [2024] studied whether LLMs can express uncertainty and found that verbalized confidence is often poorly calibrated. Scalena et al. [2025] used per-token entropy to allocate compute adaptively during generation, a token-level compute-allocation complement to our sample-level reliability estimation. All of these signals rely on the model’s own log-probabilities or verbalized self-assessment. We show that such confidence signals are unreliable on difficult problems and propose an alternative based on prefix self-reproduction that requires neither.

##### Prefix continuation as a per-sample signal.

Several recent methods regenerated from a truncated reasoning prefix or extracted a structural signal from a CoT and used it to select or weight samples. Hammoud et al. [2025] proposed SubthoughtReasoner, which segments a single greedy trace into sequential subthoughts at linguistic cues and takes the mode over per-subthought regenerations as the final answer (single-trace refinement, +13pp on AIME 2024 vs. the same trace’s last answer). Faria and Smith [2025] also regenerated from intermediate states, but for test-time alignment via Metropolis-Hastings (building on quality-aware machine-translation sampling [ Faria et al., 2024 ] ) rather than answer aggregation. Zhu et al. [2024] iteratively promoted a high-confidence prefix among N N initial partial answers via Beta-gated agreement on the extracted-answer distribution and resampled subsequent branches conditioned on it (up to 40.5% latency reduction at matched accuracy). Jindal et al. [2026] clustered the first 256 tokens of N N initial samples and expanded only the dominant cluster (up to 60% token reduction at matched accuracy). Feng et al. [2025] scored each of N = 64 N{=}64 traces by its Failed-Step Fraction (the proportion of abandoned reasoning branches) and selected the lowest-FSF trace, yielding 5% to 13% improvements over random selection on AIME 2025. The latter three collapsed N N samples onto a subset (a single best prefix, the dominant cluster, or one selected trace) and therefore inherited the failure mode of Standard MV when the subset misses the correct answer: Jindal et al. [2026] reported a 10pp drop on AIME 2025 (76.7% to 66.7%) where the largest prefix cluster need not contain the correct answer. PC-WMV moves in the converse direction: it keeps all N N samples and reweights the vote by each sample’s prefix self-reproduction, so a minority sample whose prefix continuation reproduces its own answer is upweighted rather than discarded. The two directions are complementary, since prefix-cluster pruning could feed PC-WMV reweighting on the surviving traces. Under cost-equivalent comparison, SubthoughtReasoner does not consistently improve over Standard MV in our experiments, filling the comparison left open by Hammoud et al. [2025] .

### A.2 Chain-of-Thought

##### Internal answer determination.

Several lines of evidence suggest that LLMs determine their answer internally before the visible CoT concludes. Lanham et al. [2023] found that truncating a CoT mid-reasoning and forcing an early answer often does not change the prediction, especially for larger models. Boppana et al. [2026] confirmed this with attention probes: on easy problems, the internal answer is determined well before the visible reasoning ends. Zhang et al. [2025] showed that linear probes on hidden states can classify the correctness of the future final answer at intermediate CoT stages. These observations are consistent with the r C > r W r_{C}>r_{W} asymmetry we measure.

##### Error propagation.

In CoT reasoning, errors compound across steps: once an error is introduced, subsequent reasoning builds on it [ Gan et al., 2025 ] . Kim et al. [2025] modeled CoT as a metastable Markov process on a reasoning graph, where dense intra-cluster (easy) and sparse inter-cluster (difficult) steps induce timescale separation. Our r C r_{C} and r W r_{W} are analogous in spirit to within-cluster persistence rates, although we measure them at the answer level under regeneration rather than at the reasoning-step level along a single trace.

##### Reasoning robustness.

Several works have studied the robustness of LLM reasoning. Yu et al. [2025] found that reasoning models can be brittle to minor perturbations in the input. von Recum et al. [2026] systematically evaluated seven intervention types on open-weight reasoning LLMs and found that robustness degrades more when interventions occur early in the CoT. Jiang et al. [2025] showed that correct answers persist even when reasoning logic is perturbed, suggesting a decoupling between answer stability and reasoning faithfulness. Our work uses this asymmetry between correct and wrong reasoning traces as a practical signal for answer aggregation.

##### Overthinking and length scaling.

Reasoning models tend to allocate compute disproportionately to problem difficulty, which limits the improvements from extending a single CoT. Chen et al. [2025] reported that o1-like models generate up to 1953% more tokens than non-thinking models on trivial arithmetic, and reach the correct answer in the first generated solution in over 92% of cases while later solutions still account for roughly 40% of tokens. Pu et al. [2025] introduced DUMB500 to quantify overthinking on easy problems and proposed ThoughtTerminator, a training-free decoding-time termination scheme that reduces overthinking tokens by 76% to 98% with minimal accuracy loss. Aggarwal et al. [2026] formalized the trade-off as a joint over- and underthinking benchmark and found that no current model balances the two: even o3 reaches only 71.1% on their unified score. These results motivate aggregating multiple short samples rather than extending a single long trace, which is the setting our method targets.

## Appendix B Limitations and Future Work

The effectiveness of prefix consistency depends on the discrimination gap D = r C − r W D=r_{C}-r_{W} . When incorrect answers are themselves stable under regeneration, r W r_{W} remains high, and the advantage of PC-WMV over Standard MV becomes small (e.g., on very difficult problems). Likewise, when the correct answer is reproduced only weakly from the chosen prefix, r C r_{C} remains low, and the signal becomes less informative. In this sense, the method is most effective in regimes where regeneration behavior meaningfully separates correct from incorrect traces.

The practical advantage of PC-WMV also depends on the available room above Pass@1. When Pass@1 is already close to Standard MV plateau, the aggregated vote on wrong answers is small, so even a strong reliability signal yields only limited accuracy improvements. This explains the small-gap settings in our experiments where PC-WMV does not outperform Standard MV (or simple verbalized-confidence baselines) by a large margin (Appendix D.3 ).

Although prefix consistency does not require token log-probabilities, it is not without cost: it incurs additional inference cost through prefix truncation and regeneration. This trade-off may be less favorable in deployments where log-probability access is readily available and inexpensive. Relatedly, the method introduces hyperparameters such as the truncation fraction τ \tau , the number of regenerations K K , and the weighting function w w , and in this work, we use fixed defaults rather than selecting them adaptively for each model or task.

A further practical limitation is that our method assumes access to an explicit Chain-of-Thought trace that can be truncated and continued from a prefix. This assumption does not hold for many frontier closed models and commercial APIs, including systems where the full internal reasoning trace is hidden or only summarized. In such settings, prefix consistency cannot be applied directly, even if the model can generate correct final answers. Extending the method to settings without visible CoT, for example by using intermediate summaries, structured scratchpads, or other externally exposed reasoning states, is an important direction for future work.

More broadly, our results establish prefix consistency as a useful behavioral signal, but not as a mechanistic explanation of why correct traces are more reproducible than incorrect ones. Understanding the origin of the observed asymmetry r C > r W r_{C}>r_{W} remains future work. Finally, our evaluation is limited to reasoning-oriented models and math/science-style benchmarks, so the extent to which the same phenomenon holds for other domains, model families, or API settings remains to be established.

As shown in Section 4.4 , r C r_{C} rises with problem easiness, r W r_{W} depends on the model and category but only weakly on Pass@1, and D = r C − r W D=r_{C}-r_{W} inherits both. This pattern is consistent with reinforcement learning with verifiable rewards encouraging reasoning that survives verification [ Wen et al., 2026 ] . State-of-the-art LLMs are designed to increase the mass of correct reasoning paths via widening the discrimination gap D D . We do not test this connection directly, and whether the same pattern holds for non-RLVR-trained reasoners is left to future work.

## Appendix C Asymptotic Analysis

We analyze the asymptotic convergence of PC-WMV, prove Theorem 1 along the way, and verify the required assumptions empirically.

### C.1 Notation and Useful Tools

Fix τ ∈ ( 0 , 1 ) \tau\in(0,1) throughout, and omit it from subscripts: e.g., write a ~ i \tilde{a}_{i} for a ~ i ( τ ) \tilde{a}_{i}^{(\tau)} and c i ​ ( a ) c_{i}(a) for c i ( τ ) ​ ( a ) c_{i}^{(\tau)}(a) . The score takes values c i ​ ( a ) ∈ { 0 , 1 2 , 1 } c_{i}(a)\in\{0,\tfrac{1}{2},1\} .

We define the transition probability as follows: T ⁡ ( b → a ) := Pr ⁡ [ a ~ i = a | a i = b ] . T(b\rightarrow a)\;:=\;\Pr\!\bigl[\tilde{a}_{i}=a\,\big|\,a_{i}=b\bigr]. (12) The reproduction rates of Section 3.1 can be written in terms of T T : r C = T ⁡ ( a ⋆ → a ⋆ ) , r W = 𝔼 ⁡ [ T ⁡ ( a i → a i ) | a i ≠ a ⋆ ] . r_{C}\;=\;T(a^{\star}\rightarrow a^{\star}),\qquad r_{W}\;=\;\mathbb{E}\!\left[T(a_{i}\rightarrow a_{i})\,\big|\,a_{i}\neq a^{\star}\right]. (13) Let π \pi and π → \pi^{\rightarrow} be the marginal distributions of a i a_{i} and a ~ i \tilde{a}_{i} , respectively. Here π ⁡ ( a ⋆ ) \pi(a^{\star}) is the same per-problem Pass@1 introduced in Section 2 and used in Theorem 1 . We keep the π \pi notation in this appendix so the population-level expressions in Eq. ( 14 ) below align with the proof. π ( a ) := Pr [ a i = a ] , π → ( a ) := Pr [ a ~ i = a ] = ∑ b ∈ 𝒜 π ( b ) T ( b → a ) . \pi(a)\;:=\;\Pr[a_{i}=a],\qquad\pi^{\rightarrow}(a)\;:=\;\Pr[\tilde{a}_{i}=a]\;=\;\sum_{b\in\mathcal{A}}\pi(b)\,T(b\rightarrow a). (14) All quantities above ( T T , r C r_{C} , r W r_{W} , π \pi , π → \pi^{\rightarrow} ) are defined per problem. The results in this section are statements about a fixed problem q q , and the i.i.d. assumption across i i refers to independent samples within q q .

For completeness, we restate the definitions of the MV and PC-WMV votes. Let w : [ 0 , 1 ] → ℝ ≥ 0 w\colon[0,1]\to\mathbb{R}_{\geq 0} satisfy w ⁡ ( 0 ) = 0 w(0)=0 . For each a ∈ 𝒜 a\in\mathcal{A} , define the aggregated PC-WMV score over N N groups by V N ( w ) ​ ( a ) := ∑ i = 1 N w ⁡ ( c i ​ ( a ) ) , V_{N}^{(w)}(a):=\sum_{i=1}^{N}w\bigl(c_{i}(a)\bigr), where each term is the per-group PC-WMV vote given in Eq. ( 8 ). We then define the PC-WMV estimator and MV voting methods by a ^ N PC := arg ​ max a ∈ 𝒜 V N ( w ) ( a ) , a ^ N MV := arg ​ max a ∈ 𝒜 1 N ∑ i = 1 N 𝟏 { a i = a } . \hat{a}^{\mathrm{PC}}_{N}\;:=\;\argmax_{a\in\mathcal{A}}V_{N}^{(w)}(a),\qquad\hat{a}^{\mathrm{MV}}_{N}\;:=\;\argmax_{a\in\mathcal{A}}\,\frac{1}{N}\sum_{i=1}^{N}\mathbf{1}\{a_{i}=a\}. (15)

We next identify the population objective associated with the PC-WMV estimator.

###### Proposition 1 (Population objective) .

Assume that the pairs ( a i , a ~ i ) (a_{i},\tilde{a}_{i}) are i.i.d. across i i , and that, conditional on a i a_{i} , the variable a ~ i \tilde{a}_{i} is drawn from T ⁡ ( a i , ⋅ ) T(a_{i},\cdot) . Then, for every a ∈ 𝒜 a\in\mathcal{A} , 1 N ​ V N ( w ) ​ ( a ) → a . s . Φ w ​ ( a ) := ∑ b ∈ 𝒜 π ⁡ ( b ) ​ 𝔼 Z ∼ Bern ⁡ ( T ⁡ ( b → a ) ) ​ [ w ⁡ ( 𝟏 { a = b } + Z 2 ) ] . \frac{1}{N}V_{N}^{(w)}(a)\;\xrightarrow{\mathrm{a.s.}}\;\Phi_{w}(a)\;:=\;\sum_{b\in\mathcal{A}}\pi(b)\,\mathbb{E}_{Z\sim\mathrm{Bern}(T(b\rightarrow a))}\!\left[w\!\left(\frac{\mathbf{1}\{a=b\}+Z}{2}\right)\right]. (16) Moreover, if Φ w \Phi_{w} has a unique maximizer, then a ^ N PC \hat{a}_{N}^{\mathrm{PC}} converges to that maximizer almost surely.

###### Proof.

For each fixed a ∈ 𝒜 a\in\mathcal{A} , the random variables { w ⁡ ( c i ​ ( a ) ) } i = 1 N \{w(c_{i}(a))\}_{i=1}^{N} are i.i.d., so the strong law of large numbers yields 1 N ​ V N ( w ) ​ ( a ) → a . s . 𝔼 ⁡ [ w ⁡ ( c i ​ ( a ) ) ] . \frac{1}{N}V_{N}^{(w)}(a)\;\xrightarrow{\mathrm{a.s.}}\;\mathbb{E}[w(c_{i}(a))]. Conditional on a i = b a_{i}=b , we have 𝟏 { a ~ i = a } ∼ Bern ( T ( b → a ) ) \mathbf{1}\{\tilde{a}_{i}=a\}\sim\mathrm{Bern}(T(b\rightarrow a)) , and 2 c i ( a ) = 𝟏 { a = b } + 𝟏 { a ~ i = a } . 2c_{i}(a)=\mathbf{1}\{a=b\}+\mathbf{1}\{\tilde{a}_{i}=a\}. Hence, 𝔼 ⁡ [ w ⁡ ( c i ​ ( a ) ) ∣ a i = b ] = 𝔼 Z ∼ Bern ⁡ ( T ⁡ ( b → a ) ) ​ [ w ⁡ ( 𝟏 { a = b } + Z 2 ) ] . \mathbb{E}[w(c_{i}(a))\mid a_{i}=b]=\mathbb{E}_{Z\sim\mathrm{Bern}(T(b\rightarrow a))}\!\left[w\!\left(\frac{\mathbf{1}\{a=b\}+Z}{2}\right)\right]. Taking expectation with respect to b ∼ π b\sim\pi gives Eq. ( 16 ). For the final claim, 1 N ​ V N ( w ) ​ ( a ) → Φ w ​ ( a ) \frac{1}{N}V_{N}^{(w)}(a)\to\Phi_{w}(a) a.s. for each a a in the finite set 𝒜 \mathcal{A} , so when Φ w \Phi_{w} has a unique maximizer a ⋆ a^{\star} , eventually a ^ N PC = arg ​ max a ⁡ V N ( w ) ​ ( a ) = a ⋆ \hat{a}_{N}^{\mathrm{PC}}=\argmax_{a}V_{N}^{(w)}(a)=a^{\star} almost surely. ∎

We next derive an explicit decomposition of Φ w \Phi_{w} that exposes its dependence on the marginal π ⁡ ( a ) \pi(a) and the self-transition T ⁡ ( a → a ) T(a\rightarrow a) .

###### Proposition 2 (Exact decomposition of Φ w \Phi_{w} ) .

For every a ∈ 𝒜 a\in\mathcal{A} , Φ w ​ ( a ) = w ⁡ ( 1 2 ) ​ [ π ⁡ ( a ) + π → ​ ( a ) ] + λ w ​ π ​ ( a ) ​ T ​ ( a → a ) , λ w := w ⁡ ( 1 ) − 2 ​ w ​ ( 1 2 ) . \Phi_{w}(a)\;=\;w(\tfrac{1}{2})\,\bigl[\pi(a)+\pi^{\rightarrow}(a)\bigr]\;+\;\lambda_{w}\,\pi(a)\,T(a\rightarrow a),\qquad\lambda_{w}\;:=\;w(1)-2\,w(\tfrac{1}{2}). (17)

###### Proof.

Fix a ∈ 𝒜 a\in\mathcal{A} . Since c i ​ ( a ) c_{i}(a) is the average of the two indicators 𝟏 { a i = a } and 𝟏 { a ~ i = a } , \mathbf{1}\{a_{i}=a\}\qquad\text{and}\qquad\mathbf{1}\{\tilde{a}_{i}=a\}, it takes only the three values 0 0 , 1 2 \tfrac{1}{2} , and 1 1 .

More precisely, c i ​ ( a ) = 1 c_{i}(a)=1 if and only if both a i = a a_{i}=a and a ~ i = a \tilde{a}_{i}=a hold. Thus, Pr ⁡ ( c i ​ ( a ) = 1 ) = π ⁡ ( a ) ​ T ​ ( a → a ) . \Pr\bigl(c_{i}(a)=1\bigr)=\pi(a)\,T(a\rightarrow a).

Next, c i ​ ( a ) = 1 2 c_{i}(a)=\tfrac{1}{2} if and only if exactly one of the two events { a i = a } \{a_{i}=a\} and { a ~ i = a } \{\tilde{a}_{i}=a\} occurs. Therefore, Pr ⁡ ( c i ​ ( a ) = 1 2 ) = Pr ⁡ ( a i = a , a ~ i ≠ a ) + Pr ⁡ ( a i ≠ a , a ~ i = a ) . \Pr\bigl(c_{i}(a)=\tfrac{1}{2}\bigr)=\Pr(a_{i}=a,\tilde{a}_{i}\neq a)+\Pr(a_{i}\neq a,\tilde{a}_{i}=a). The first term is Pr ⁡ ( a i = a , a ~ i ≠ a ) = π ⁡ ( a ) ​ ( 1 − T ⁡ ( a → a ) ) . \Pr(a_{i}=a,\tilde{a}_{i}\neq a)=\pi(a)\bigl(1-T(a\rightarrow a)\bigr). For the second term, recall that π → ​ ( a ) = Pr ⁡ ( a ~ i = a ) \pi^{\rightarrow}(a)=\Pr(\tilde{a}_{i}=a) , so Pr ⁡ ( a i ≠ a , a ~ i = a ) = Pr ⁡ ( a ~ i = a ) − Pr ⁡ ( a i = a , a ~ i = a ) = π → ​ ( a ) − π ⁡ ( a ) ​ T ​ ( a → a ) . \Pr(a_{i}\neq a,\tilde{a}_{i}=a)=\Pr(\tilde{a}_{i}=a)-\Pr(a_{i}=a,\tilde{a}_{i}=a)=\pi^{\rightarrow}(a)-\pi(a)T(a\rightarrow a). Combining the two expressions yields Pr ⁡ ( c i ​ ( a ) = 1 2 ) = π ⁡ ( a ) + π → ​ ( a ) − 2 ​ π ​ ( a ) ​ T ​ ( a → a ) . \Pr\bigl(c_{i}(a)=\tfrac{1}{2}\bigr)=\pi(a)+\pi^{\rightarrow}(a)-2\pi(a)T(a\rightarrow a).

Finally, since w ⁡ ( 0 ) = 0 w(0)=0 and c i ​ ( a ) ∈ { 0 , 1 2 , 1 } c_{i}(a)\in\{0,\tfrac{1}{2},1\} , Φ w ​ ( a ) = 𝔼 ⁡ [ w ⁡ ( c i ​ ( a ) ) ] = w ⁡ ( 1 ) ​ Pr ⁡ ( c i ​ ( a ) = 1 ) + w ⁡ ( 1 2 ) ​ Pr ⁡ ( c i ​ ( a ) = 1 2 ) . \Phi_{w}(a)=\mathbb{E}[w(c_{i}(a))]=w(1)\Pr\bigl(c_{i}(a)=1\bigr)+w(\tfrac{1}{2})\Pr\bigl(c_{i}(a)=\tfrac{1}{2}\bigr). Substituting the above probabilities, we obtain Φ w ​ ( a ) = w ⁡ ( 1 ) ​ π ​ ( a ) ​ T ​ ( a → a ) + w ⁡ ( 1 2 ) ​ [ π ⁡ ( a ) + π → ​ ( a ) − 2 ​ π ​ ( a ) ​ T ​ ( a → a ) ] . \Phi_{w}(a)=w(1)\pi(a)T(a\rightarrow a)+w(\tfrac{1}{2})\bigl[\pi(a)+\pi^{\rightarrow}(a)-2\pi(a)T(a\rightarrow a)\bigr]. Rearranging terms gives Φ w ​ ( a ) = w ⁡ ( 1 2 ) ​ [ π ⁡ ( a ) + π → ​ ( a ) ] + ( w ⁡ ( 1 ) − 2 ​ w ​ ( 1 2 ) ) ​ π ​ ( a ) ​ T ​ ( a → a ) , \Phi_{w}(a)=w(\tfrac{1}{2})\bigl[\pi(a)+\pi^{\rightarrow}(a)\bigr]+\bigl(w(1)-2w(\tfrac{1}{2})\bigr)\pi(a)T(a\rightarrow a), which is exactly Eq. ( 17 ). ∎

### C.2 Asymptotic Convergence of PC-WMV

Throughout this subsection we assume the i.i.d. setup of Proposition 1 .

By Proposition 2 , applied to a ⋆ a^{\star} and to any wrong a a and subtracting, Φ w ​ ( a ⋆ ) − Φ w ​ ( a ) = \displaystyle\Phi_{w}(a^{\star})-\Phi_{w}(a)\;= w ⁡ ( 1 2 ) ​ [ ( π ⁡ ( a ⋆ ) + π → ​ ( a ⋆ ) ) − ( π ⁡ ( a ) + π → ​ ( a ) ) ] ⏟ pooled-mass term \displaystyle\underbrace{w(\tfrac{1}{2})\,\bigl[(\pi(a^{\star})+\pi^{\rightarrow}(a^{\star}))-(\pi(a)+\pi^{\rightarrow}(a))\bigr]}_{\text{pooled-mass term}} (18) + λ w ​ [ π ⁡ ( a ⋆ ) ​ T ​ ( a ⋆ → a ⋆ ) − π ⁡ ( a ) ​ T ​ ( a → a ) ] ⏟ self-reproduction term . \displaystyle+\underbrace{\lambda_{w}\,\bigl[\pi(a^{\star})\,T(a^{\star}\rightarrow a^{\star})-\pi(a)\,T(a\rightarrow a)\bigr]}_{\text{self-reproduction term}}. By Proposition 1 , identifying a ⋆ a^{\star} as the population maximizer requires this difference to be positive for every wrong a a . The two assumptions below control the two terms separately.

###### Assumption 1 (Self-reproduction dominance) .

For every a ≠ a ⋆ a\neq a^{\star} , π ⁡ ( a ⋆ ) ​ T ​ ( a ⋆ → a ⋆ ) > π ⁡ ( a ) ​ T ​ ( a → a ) . \pi(a^{\star})\,T(a^{\star}\rightarrow a^{\star})>\pi(a)\,T(a\rightarrow a). (19)

##### Interpretation.

π ⁡ ( a ⋆ ) ​ T ​ ( a ⋆ → a ⋆ ) \pi(a^{\star})\,T(a^{\star}\rightarrow a^{\star}) is the population mass of groups whose initial answer is correct and is reproduced correctly, and π ⁡ ( a ) ​ T ​ ( a → a ) \pi(a)\,T(a\rightarrow a) is the corresponding mass for the wrong answer a a that is reproduced as itself. Assumption 1 requires that correct self-reproduction dominate every individual wrong self-reproduction. Equivalently, it makes the self-reproduction term in the decomposition strictly positive whenever λ w > 0 \lambda_{w}>0 .

###### Assumption 2 (Pooled-mass dominance) .

For every a ≠ a ⋆ a\neq a^{\star} , π ⁡ ( a ⋆ ) + π → ​ ( a ⋆ ) > π ⁡ ( a ) + π → ​ ( a ) . \pi(a^{\star})+\pi^{\rightarrow}(a^{\star})>\pi(a)+\pi^{\rightarrow}(a). (20)

##### Interpretation.

π ​ ( a ) + π → ​ ( a ) \pi(a)+\pi^{\rightarrow}(a) is the total population mass on candidate a a , combining initial occurrences and regeneration arrivals. Assumption 2 requires that a ⋆ a^{\star} have the largest such total. By the same decomposition, it makes the pooled-mass term strictly positive whenever w ⁡ ( 1 2 ) > 0 w(\tfrac{1}{2})>0 .

###### Theorem 2 (Asymptotic convergence of PC-WMV) .

Let w w satisfy w ⁡ ( 0 ) = 0 w(0)=0 , w ⁡ ( 1 ) > 0 w(1)>0 , and λ w := w ⁡ ( 1 ) − 2 ​ w ​ ( 1 2 ) ≥ 0 \lambda_{w}:=w(1)-2w(\tfrac{1}{2})\geq 0 . Then: (a) If Assumptions 1 and 2 hold, then a ^ N PC → a ⋆ \hat{a}_{N}^{\mathrm{PC}}\to a^{\star} almost surely.

(b) If w ⁡ ( 1 2 ) = 0 w(\tfrac{1}{2})=0 , then Assumption 2 is unnecessary: Assumption 1 alone implies a ^ N PC → a ⋆ \hat{a}_{N}^{\mathrm{PC}}\to a^{\star} almost surely.

###### Proof.

Fix any wrong a ≠ a ⋆ a\neq a^{\star} . By Assumption 1 , the self-reproduction bracket of Eq. ( 18 ) is strictly positive, so the self-reproduction term is nonnegative and is strictly positive whenever λ w > 0 \lambda_{w}>0 .

For part (a), Assumption 2 makes the pooled-mass bracket of Eq. ( 18 ) strictly positive, so the pooled-mass term is nonnegative and is strictly positive whenever w ⁡ ( 1 2 ) > 0 w(\tfrac{1}{2})>0 . Since w ⁡ ( 1 ) = λ w + 2 ​ w ​ ( 1 2 ) > 0 w(1)=\lambda_{w}+2w(\tfrac{1}{2})>0 , at least one of λ w \lambda_{w} and w ⁡ ( 1 2 ) w(\tfrac{1}{2}) is strictly positive, so Φ w ​ ( a ⋆ ) > Φ w ​ ( a ) \Phi_{w}(a^{\star})>\Phi_{w}(a) for every wrong a a . Hence a ⋆ a^{\star} is the unique maximizer of Φ w \Phi_{w} , and Proposition 1 yields a ^ N PC → a ⋆ \hat{a}_{N}^{\mathrm{PC}}\to a^{\star} almost surely.

For part (b), if w ⁡ ( 1 2 ) = 0 w(\tfrac{1}{2})=0 the pooled-mass term vanishes identically and λ w = w ⁡ ( 1 ) > 0 \lambda_{w}=w(1)>0 , so the strict positivity of the self-reproduction term suffices to give Φ w ​ ( a ⋆ ) > Φ w ​ ( a ) \Phi_{w}(a^{\star})>\Phi_{w}(a) for every wrong a a . Thus a ^ N PC → a ⋆ \hat{a}_{N}^{\mathrm{PC}}\to a^{\star} almost surely without Assumption 2 . ∎

### C.3 Proof of Theorem 1

Theorem 1 follows from Theorem 2 by specializing to the binary case 𝒜 = { a ⋆ , a ′ } \mathcal{A}=\{a^{\star},a^{\prime}\} , where a ⋆ a^{\star} is the correct answer and a ′ a^{\prime} is the only wrong answer (so π ⁡ ( a ′ ) = 1 − π ⁡ ( a ⋆ ) \pi(a^{\prime})=1-\pi(a^{\star}) ). In this case, the two assumptions of Theorem 2 reduce to the same condition and the exact margin takes a one-bracket form, from which the asymptotic boundary π ⁡ ( a ⋆ ) > r W / ( r C + r W ) \pi(a^{\star})>r_{W}/(r_{C}+r_{W}) follows.

##### The two assumptions coincide.

With the only wrong answer being a ′ a^{\prime} and π ⁡ ( a ′ ) = 1 − π ⁡ ( a ⋆ ) \pi(a^{\prime})=1-\pi(a^{\star}) , Assumption 1 becomes the binary boundary π ⁡ ( a ⋆ ) ​ T ​ ( a ⋆ → a ⋆ ) > ( 1 − π ⁡ ( a ⋆ ) ) ​ T ​ ( a ′ → a ′ ) . \pi(a^{\star})\,T(a^{\star}\rightarrow a^{\star})>(1-\pi(a^{\star}))\,T(a^{\prime}\rightarrow a^{\prime}). (21) For Assumption 2 , expand π → \pi^{\rightarrow} via Eq. ( 14 ), using T ⁡ ( a ⋆ → a ′ ) = 1 − T ⁡ ( a ⋆ → a ⋆ ) T(a^{\star}\rightarrow a^{\prime})=1-T(a^{\star}\rightarrow a^{\star}) and T ⁡ ( a ′ → a ⋆ ) = 1 − T ⁡ ( a ′ → a ′ ) T(a^{\prime}\rightarrow a^{\star})=1-T(a^{\prime}\rightarrow a^{\prime}) (each row of T T sums to one): π → ​ ( a ⋆ ) \displaystyle\pi^{\rightarrow}(a^{\star}) = π ⁡ ( a ⋆ ) ​ T ​ ( a ⋆ → a ⋆ ) + ( 1 − π ⁡ ( a ⋆ ) ) ​ ( 1 − T ⁡ ( a ′ → a ′ ) ) , \displaystyle=\pi(a^{\star})\,T(a^{\star}\rightarrow a^{\star})+(1-\pi(a^{\star}))\bigl(1-T(a^{\prime}\rightarrow a^{\prime})\bigr), π → ​ ( a ′ ) \displaystyle\pi^{\rightarrow}(a^{\prime}) = π ⁡ ( a ⋆ ) ​ ( 1 − T ⁡ ( a ⋆ → a ⋆ ) ) + ( 1 − π ⁡ ( a ⋆ ) ) ​ T ​ ( a ′ → a ′ ) . \displaystyle=\pi(a^{\star})\bigl(1-T(a^{\star}\rightarrow a^{\star})\bigr)+(1-\pi(a^{\star}))\,T(a^{\prime}\rightarrow a^{\prime}). Adding π ⁡ ( a ⋆ ) \pi(a^{\star}) and π ⁡ ( a ′ ) = 1 − π ⁡ ( a ⋆ ) \pi(a^{\prime})=1-\pi(a^{\star}) and simplifying, π ⁡ ( a ⋆ ) + π → ​ ( a ⋆ ) \displaystyle\pi(a^{\star})+\pi^{\rightarrow}(a^{\star}) = 1 + [ π ⁡ ( a ⋆ ) ​ T ​ ( a ⋆ → a ⋆ ) − ( 1 − π ⁡ ( a ⋆ ) ) ​ T ​ ( a ′ → a ′ ) ] , \displaystyle=1+\bigl[\pi(a^{\star})\,T(a^{\star}\rightarrow a^{\star})-(1-\pi(a^{\star}))\,T(a^{\prime}\rightarrow a^{\prime})\bigr], π ⁡ ( a ′ ) + π → ​ ( a ′ ) \displaystyle\pi(a^{\prime})+\pi^{\rightarrow}(a^{\prime}) = 1 − [ π ⁡ ( a ⋆ ) ​ T ​ ( a ⋆ → a ⋆ ) − ( 1 − π ⁡ ( a ⋆ ) ) ​ T ​ ( a ′ → a ′ ) ] . \displaystyle=1-\bigl[\pi(a^{\star})\,T(a^{\star}\rightarrow a^{\star})-(1-\pi(a^{\star}))\,T(a^{\prime}\rightarrow a^{\prime})\bigr]. Subtracting, [ π ⁡ ( a ⋆ ) + π → ​ ( a ⋆ ) ] − [ π ⁡ ( a ′ ) + π → ​ ( a ′ ) ] = 2 ​ [ π ⁡ ( a ⋆ ) ​ T ​ ( a ⋆ → a ⋆ ) − ( 1 − π ⁡ ( a ⋆ ) ) ​ T ​ ( a ′ → a ′ ) ] . \bigl[\pi(a^{\star})+\pi^{\rightarrow}(a^{\star})\bigr]-\bigl[\pi(a^{\prime})+\pi^{\rightarrow}(a^{\prime})\bigr]=2\,\bigl[\pi(a^{\star})\,T(a^{\star}\rightarrow a^{\star})-(1-\pi(a^{\star}))\,T(a^{\prime}\rightarrow a^{\prime})\bigr]. Hence Assumptions 1 and 2 reduce to the same condition Eq. ( 21 ), and Theorem 2 (a) gives a ^ N PC → a ⋆ \hat{a}_{N}^{\mathrm{PC}}\to a^{\star} a.s. whenever Eq. ( 21 ) holds.

##### The exact margin.

Applying Eq. ( 18 ) with a = a ′ a=a^{\prime} , the self-reproduction term contributes λ w \lambda_{w} times the quantity π ⁡ ( a ⋆ ) ​ T ​ ( a ⋆ → a ⋆ ) − ( 1 − π ⁡ ( a ⋆ ) ) ​ T ​ ( a ′ → a ′ ) \pi(a^{\star})\,T(a^{\star}\rightarrow a^{\star})-(1-\pi(a^{\star}))\,T(a^{\prime}\rightarrow a^{\prime}) . By the identity above, the pooled-mass term contributes 2 ​ w ​ ( 1 2 ) 2w(\tfrac{1}{2}) times the same bracket. Their sum is w ⁡ ( 1 ) = λ w + 2 ​ w ​ ( 1 2 ) w(1)=\lambda_{w}+2w(\tfrac{1}{2}) times the bracket: Φ w ​ ( a ⋆ ) − Φ w ​ ( a ′ ) = w ⁡ ( 1 ) ​ [ π ⁡ ( a ⋆ ) ​ T ​ ( a ⋆ → a ⋆ ) − ( 1 − π ⁡ ( a ⋆ ) ) ​ T ​ ( a ′ → a ′ ) ] . \Phi_{w}(a^{\star})-\Phi_{w}(a^{\prime})=w(1)\,\bigl[\pi(a^{\star})\,T(a^{\star}\rightarrow a^{\star})-(1-\pi(a^{\star}))\,T(a^{\prime}\rightarrow a^{\prime})\bigr]. (22) The choice of w w thus enters only through w ⁡ ( 1 ) w(1) .

###### Proof.

By Eq. ( 22 ) and w ⁡ ( 1 ) > 0 w(1)>0 , Φ w ​ ( a ⋆ ) > Φ w ​ ( a ′ ) \Phi_{w}(a^{\star})>\Phi_{w}(a^{\prime}) if and only if π ⁡ ( a ⋆ ) ​ T ​ ( a ⋆ → a ⋆ ) > ( 1 − π ⁡ ( a ⋆ ) ) ​ T ​ ( a ′ → a ′ ) . \pi(a^{\star})\,T(a^{\star}\rightarrow a^{\star})>(1-\pi(a^{\star}))\,T(a^{\prime}\rightarrow a^{\prime}). By Proposition 1 , this is equivalent to a ^ N PC → a ⋆ \hat{a}_{N}^{\mathrm{PC}}\to a^{\star} almost surely. Identifying r C := T ⁡ ( a ⋆ → a ⋆ ) r_{C}:=T(a^{\star}\rightarrow a^{\star}) and r W := T ⁡ ( a ′ → a ′ ) r_{W}:=T(a^{\prime}\rightarrow a^{\prime}) via Eq. ( 13 ) rewrites the threshold as π ⁡ ( a ⋆ ) > r W r C + r W . \pi(a^{\star})>\frac{r_{W}}{r_{C}+r_{W}}. Standard MV’s vote count 1 N ∑ i = 1 N 𝟏 { a i = a } \frac{1}{N}\sum_{i=1}^{N}\mathbf{1}\{a_{i}=a\} converges to π ⁡ ( a ) \pi(a) a.s. by the strong law of large numbers, so Standard MV converges to a ⋆ a^{\star} if and only if π ⁡ ( a ⋆ ) > 1 2 \pi(a^{\star})>\tfrac{1}{2} . Hence PC-WMV converges where Standard MV does not on the interval r W / ( r C + r W ) < π ⁡ ( a ⋆ ) ≤ 1 2 r_{W}/(r_{C}+r_{W})<\pi(a^{\star})\leq\tfrac{1}{2} , which has positive length if and only if r C > r W r_{C}>r_{W} . ∎

### C.4 Empirical Verification of Assumptions

Table 5 verifies that Assumption 1 (A1) and Assumption 2 (A2) hold empirically on 𝒬 ′ := { q ∈ 𝒬 : 0 < π q ​ ( a q ⋆ ) < 1 } \mathcal{Q}^{\prime}:=\{q\in\mathcal{Q}:0<\pi_{q}(a^{\star}_{q})<1\} , the subset of problems on which the verification is non-degenerate. At π q ​ ( a q ⋆ ) = 1 \pi_{q}(a^{\star}_{q})=1 no wrong answer carries population mass, so A1 and A2 hold vacuously and would only inflate the reported probabilities. At π q ​ ( a q ⋆ ) = 0 \pi_{q}(a^{\star}_{q})=0 the per-problem rate r C , q = T ⁡ ( a q ⋆ → a q ⋆ ) r_{C,q}=T(a^{\star}_{q}\rightarrow a^{\star}_{q}) is undefined and a q ⋆ a^{\star}_{q} is not a population maximizer, so the framework does not apply. 𝒬 ′ \mathcal{Q}^{\prime} also matches the subset used in the AUROC ¯ \overline{\mathrm{AUROC}} analysis (Section 4.1 , Appendix G.2 ). The table further reports the per-problem indicator Δ w ( n ) := min a ≠ a ⋆ ⁡ [ Φ w ( n ) ​ ( a ⋆ ) − Φ w ( n ) ​ ( a ) ] \Delta_{w^{(n)}}:=\min_{a\neq a^{\star}}\bigl[\Phi_{w^{(n)}}(a^{\star})-\Phi_{w^{(n)}}(a)\bigr] for w ( n ) ​ ( c ) = c n w^{(n)}(c)=c^{n} , n ∈ { 1 , 2 , 3 } n\in\{1,2,3\} ( Δ w ( n ) > 0 \Delta_{w^{(n)}}>0 is equivalent to a ⋆ a^{\star} being the unique maximizer of Φ w ( n ) \Phi_{w^{(n)}} ).

Pr ⁡ [ A1 ] \Pr[\mathrm{A1}] is non-negligible across a wide range of benchmarks and models, so A1 \mathrm{A1} is not a rare or pathological event in practice. Conditional on A1 \mathrm{A1} , Pr ⁡ [ A2 ∣ A1 ] \Pr[\mathrm{A2}\mid\mathrm{A1}] is at least 87.5 % 87.5\% on every cell and reaches 100 % 100\% on 40 % 40\% of them, so the joint occurrence of A1 \mathrm{A1} and A2 \mathrm{A2} is common. The last three columns ( Pr ⁡ [ Δ w ( n ) > 0 ∣ A1 ] \Pr[\Delta_{w^{(n)}}>0\mid\mathrm{A1}] ) further show that the positive gap predicted by Theorem 2 occurs with overwhelmingly high probability for w ( n ) ​ ( c ) = c n w^{(n)}(c)=c^{n} , n ∈ { 1 , 2 , 3 } n\in\{1,2,3\} , even under the weaker condition that does not require A2 \mathrm{A2} . These findings indicate that the assumptions are not artificially imposed but rather reflect patterns that arise naturally and frequently in real experimental data.

## Appendix D Additional Experiments

### D.1 ROC Curves for Correctness Predictors

Tables 1 and 2 report AUROC ¯ \overline{\mathrm{AUROC}} as a single number per (model, benchmark, signal). Figure 4 visualizes the underlying ROC curves on the same 5 model × \times 4 benchmark grid, overlaying prefix consistency and the WMV baselines per panel. Curves are macro-averaged: each problem’s ROC is interpolated onto a common false-positive-rate grid and then averaged over the same problem subset 𝒬 ′ \mathcal{Q}^{\prime} used in AUROC ¯ \overline{\mathrm{AUROC}} (problems with at least one correct and one wrong initial sample, Appendix G.2 ).

The visual pattern matches the AUROC ¯ \overline{\mathrm{AUROC}} numbers: prefix consistency’s curve sits at or above the baselines on FrontierScience-Olympiad and HMMT Feb 2026 in 8 of the 10 (model, benchmark) settings across the five models, while on AIME 2025 and Brumo 2025 the gap shrinks as the baselines’ curves move closer to PC. The two cells where PC is not visibly above are Nemotron2-9B FrontierScience-Olympiad (where P(True) leads, consistent with PC’s smallest discrimination gap D D in Table 1 ) and GPT-OSS-120B HMMT Feb 2026 (where DeepConf tail edges PC by .03 .03 in AUROC ¯ \overline{\mathrm{AUROC}} ).

### D.2 Cost–Accuracy Curves

Figure 5 extends the cost–accuracy analysis of Figure 1 to all 20 (model, benchmark) cells, complementing the fixed-budget tables in Appendix D.3 . Across nearly all 20 cells PC-cubic (green) sits above the other baselines once the budget exceeds the per-problem regeneration cost, and reaches Standard MV plateau at a noticeably smaller budget. The discrimination gap is largest on FrontierScience-Olympiad and shrinks as Standard MV plateau approaches its peak (AIME 2025, Brumo 2025).

### D.3 Full Baseline Comparison

Figure 6 extends Figure 5 to the full baseline set plus the oracle upper bounds. The three PC variants form a tight green band near the plateau across nearly every cell, while the DeepConf variants and especially their filtered variants spread out widely.

Tables 6 , 7 , 8 , 9 , and 10 report fixed-budget accuracy at B ∈ { 250 ​ k , 1 ​ M , 5 ​ M } B\in\{250\text{k},1\text{M},5\text{M}\} tokens for every evaluated baseline (Standard MV, all five DeepConf aggregation strategies [ Fu et al., 2026 ] and their filtered variants, Response probability, verbalized confidence and P(True) [ Taubenfeld et al., 2025 , Kadavath et al., 2022 ] , and PC-linear/quadratic/cubic), one table per model. See Appendix E for baseline definitions. Tables 11 , 12 , 13 , 14 , and 15 report the corresponding token-efficiency ratios at α ∈ { 75 % , 90 % , 99 % } \alpha\in\{75\%,90\%,99\%\} .

Two patterns emerge. First, on the more difficult science benchmark (FrontierScience-Olympiad) PC-cubic is the best non-oracle method at B = 250 ​ k B{=}250\text{k} and B = 1 ​ M B{=}1\text{M} for the four models with non-trivial discrimination gap (GPT-OSS-120B, GPT-OSS-20B, Nemotron3-30B, Ministral3-14B): at B = 1 ​ M B{=}1\text{M} it reaches .508, .537, .486, and .174 respectively, against the strongest non-PC baseline at .503, .525, .472, and .143. At B = 5 ​ M B{=}5\text{M} PC-cubic remains best on three of these four, with PC-quadratic narrowly ahead on Nemotron3-30B (.504 vs. .503, within 2 ​ σ 2\sigma ). The PC-linear ≤ \leq PC-quadratic ≤ \leq PC-cubic ordering holds in 11 of the 12 (model, budget) FrontierScience-Olympiad cells over these four models, with the Nemotron3-30B 5M cell as the only inversion, consistent with the convex-weight analysis: in Eq. ( 17 ), the coefficient λ w := w ⁡ ( 1 ) − 2 ​ w ​ ( 1 2 ) \lambda_{w}:=w(1)-2w(\tfrac{1}{2}) on the self-reproduction term π ⁡ ( a ) ​ T ​ ( a → a ) \pi(a)\,T(a\rightarrow a) (the joint probability that a a is both the initial and the regenerated answer) takes values 0 0 , 1 2 \tfrac{1}{2} , 3 4 \tfrac{3}{4} for PC-linear, PC-quadratic, PC-cubic respectively, so larger n n upweights self-reproducing candidates more strongly. The exception is Nemotron2-9B, whose FrontierScience-Olympiad discrimination gap is the smallest in our suite ( D = 7.4 % D=7.4\% , Table 1 ). PC-WMV there roughly matches Standard MV (PC-cubic .199 vs. Standard MV .203 at B = 1 ​ M B{=}1\text{M} ), consistent with Theorem 1 predicting no advantage when D D is small.

Second, on the easier benchmarks (AIME 2025, Brumo 2025) where Standard MV plateau already sits close to its peak, verbalized confidence (Verbal binary, P(True)) and DeepConf tail (top-90%) become competitive or take the lead in a few cells (e.g. Verbal binary on GPT-OSS-20B Brumo reaches .951 at B = 1 ​ M B{=}1\text{M} vs. .931 for PC-cubic). This matches the cost–quality trade-off discussed in Section 4 , where PC’s larger per-group cost is no longer amortized once Standard MV is near its plateau.

SubthoughtReasoner [ Hammoud et al., 2025 ] appears only in the GPT-OSS-20B tables, the only model for which it has been re-evaluated under the unified incremental path. SubthoughtReasoner does not consistently improve over Standard MV (vs. Standard MV at B = 1 ​ M B{=}1\text{M} : .778 vs. .775 on HMMT, .518 vs. .523 on FrontierScience-Olympiad, .886 vs. .896 on AIME 2025), and the GPT-OSS-20B Brumo cell and other-model cells are not evaluated.

### D.4 Pool Coverage vs. Reweighting

We show that PC-WMV’s advantage over the non-PC baselines comes from reweighting, not from an enlarged pool of correct candidates.

##### Oracle upper bounds.

We define Oracle (Standard MV) as the accuracy of an ideal selector that, at each budget B B , always picks the correct answer from the initial-sample pool whenever one exists, and Oracle (Prefix Consistency) as the same ideal selector applied to the combined pool of initial and regenerated answers. Both oracles are unattainable in practice, since the correct answer is unknown at inference time; they serve as upper bounds on what Standard MV and PC-WMV can achieve, respectively. Figure 7 replots Figure 6 restricted to Standard MV, PC-cubic, and the two oracle upper bounds, with the y-axis chosen so the oracles stay in view at high token budgets. Oracle (Standard MV) and Oracle (Prefix Consistency) coincide within the 2 ​ σ 2\sigma confidence band on most of the 20 cells, and the residual gap between them is small relative to the PC-cubic vs. Standard MV gap in the same cells. At a fixed token budget B B , the union of correct candidates reachable from sampled groups is therefore essentially the same as that reachable from the equivalent number of initial samples drawn under the Standard MV protocol. Three factors related to pool coverage explain the small residuals. First, at τ = 0.75 \tau{=}0.75 , K = 1 K{=}1 each PC group costs ≈ 1.25 × {\approx}1.25{\times} a Standard MV sample, 2 2 2 The factor 1.25 = 1 + ( 1 − τ ) 1.25=1+(1-\tau) is the truncation-implied expectation. Continuation/generation token ratios in Table 26 give empirical per-group cost factors of 1.25 1.25 – 1.34 × 1.34{\times} on four of the five models and 1.49 1.49 – 1.60 × 1.60{\times} on Ministral3-14B. so at budget B B PC pools roughly 1.6 × 1.6{\times} as many candidate answers as Standard MV. Second, a ~ i \tilde{a}_{i} is correlated with a i a_{i} through the shared prefix y i [ : ⌈ τ | y i | ⌉ ] y_{i}[{:}\lceil\tau|y_{i}|\rceil] , so the effective number of independent answers in the group pool is well below 1.6 × 1.6{\times} , nearly canceling the first effect. Third, the asymptotic pool of correct candidates is by construction weakly larger for the group pool than for the initial pool, which puts Oracle (Prefix Consistency) weakly above Oracle (Standard MV) at high B B in a subset of cells. None of these effects involves the reweighting, so they cannot account for the PC-cubic vs. Standard MV gap in the same panels. PC-WMV’s advantage therefore comes from the weighting itself, with the prefix-consistency score c i ​ ( a ) c_{i}(a) acting as a per-candidate reliability signal (Section 3.1 ).

##### Per-problem marginal correctness.

Figure 8 gives a complementary per-problem view. Each point is the empirical estimate of the per-problem marginals π ( a ⋆ ) = Pr [ a i = a ⋆ ] \pi(a^{\star})=\Pr[a_{i}=a^{\star}] over the initial answers and π → ( a ⋆ ) = Pr [ a ~ i = a ⋆ ] \pi^{\rightarrow}(a^{\star})=\Pr[\tilde{a}_{i}=a^{\star}] over the regenerations (notation as defined in Appendix C.1 , Eq. ( 14 )). The plotted estimates π ^ ​ ( a ⋆ ) \hat{\pi}(a^{\star}) and π → ^ ​ ( a ⋆ ) \widehat{\pi^{\rightarrow}}(a^{\star}) cluster tightly on the y = x y=x diagonal in every cell, and their cell-level means agree within a few percentage points on most cells. The largest cell-mean difference is for Nemotron3-30B on AIME 2025, where the cell mean of π ^ ​ ( a ⋆ ) \hat{\pi}(a^{\star}) is 0.90 0.90 and that of π → ^ ​ ( a ⋆ ) \widehat{\pi^{\rightarrow}}(a^{\star}) is 0.77 0.77 , and across the 20 cells the differences run in both directions (e.g., Ministral3-14B has the cell mean of π → ^ ​ ( a ⋆ ) \widehat{\pi^{\rightarrow}}(a^{\star}) above that of π ^ ​ ( a ⋆ ) \hat{\pi}(a^{\star}) on AIME 2025 and Brumo 2025). A paired Wilcoxon signed-rank test on the per-problem differences π ^ q ​ ( a ⋆ ) − π → ^ q ​ ( a ⋆ ) \hat{\pi}_{q}(a^{\star})-\widehat{\pi^{\rightarrow}}_{q}(a^{\star}) rejects equality at the Bonferroni-corrected significance level α sig = 0.05 / 20 \alpha_{\mathrm{sig}}=0.05/20 on 5 of the 20 cells, with absolute cell-mean differences of at most 0.126 0.126 (the Nemotron3-30B AIME 2025 outlier, with the other four cells within 0.061 0.061 ). Among these 5 detected cells, 4 have the cell mean of π ^ ​ ( a ⋆ ) \hat{\pi}(a^{\star}) above the cell mean of π → ^ ​ ( a ⋆ ) \widehat{\pi^{\rightarrow}}(a^{\star}) , that is, regenerated answers are statistically less correct on average than initial answers (the only exception is Ministral3-14B FrontierScience-Olympiad). Across all 20 cells the cell-mean difference is positive on 13 cells and negative on 7, indistinguishable from a 50 / 50 50{/}50 split (two-sided binomial sign test, p = 0.26 p=0.26 ). The marginal correctness rate is therefore comparable for initial and regenerated answers, and the cell-mean differences do not systematically favor the regenerations. This is a stronger statement than mere equality of rates: PC-WMV’s advantage cannot come from regeneration raising the per-answer correctness rate, because in the cells where the rate differs the regenerations have the lower marginal correctness.

### D.5 Sensitivity to τ \tau and K K

Section 3.1 fixes K = 1 K=1 to keep notation succinct. Here we extend it to the general- K K multiset of Eq. ( 4 ) and the corresponding score c i ( τ , K ) ​ ( a ) = | { a ′ ∈ A i ( τ , K ) : a ′ = a } | / ( K + 1 ) c_{i}^{(\tau,K)}(a)=|\{a^{\prime}\in A_{i}^{(\tau,K)}:a^{\prime}=a\}|/(K+1) , sweeping K ∈ { 1 , 2 , 3 } K\in\{1,2,3\} and τ ∈ { 0.25 , 0.50 , 0.75 } \tau\in\{0.25,0.50,0.75\} .

Table 16 sweeps the truncation fraction τ ∈ { 0.25 , 0.50 , 0.75 } \tau\in\{0.25,0.50,0.75\} at K = 1 K{=}1 for GPT-OSS-20B. Both r C r_{C} and r W r_{W} decrease with deeper truncation, with r W r_{W} generally decreasing faster (e.g., on AIME 2025, r C r_{C} goes 87.8 % → 73.0 % 87.8\%\to 73.0\% and r W r_{W} goes 42.6 % → 17.1 % 42.6\%\to 17.1\% as τ \tau moves 0.75 → 0.25 0.75\to 0.25 ). The discrimination gap D ⁡ ( τ ) D(\tau) varies by benchmark: it widens monotonically on AIME 2025 ( 45.2 → 50.0 → 55.9 45.2\to 50.0\to 55.9 ), peaks at τ = 0.50 \tau{=}0.50 on HMMT and Brumo 2025, and narrows on FrontierScience-Olympiad ( 41.4 → 39.5 → 39.1 41.4\to 39.5\to 39.1 ). Deeper truncation also costs more per group, since regeneration covers a longer suffix. Cost-equivalent accuracy across ( τ , K ) (\tau,K) is reported in Table 17 .

Table 17 reports PC-linear, PC-quadratic, and PC-cubic accuracy across all ( τ , K ) (\tau,K) configurations on the four GPT-OSS-20B benchmarks at budgets B ∈ { 250 ​ k , 1 ​ M , 5 ​ M } B\in\{250\text{k},1\text{M},5\text{M}\} , with Standard MV at the top for reference. The main paper fixes τ = 0.75 \tau{=}0.75 , K = 1 K{=}1 (Section 4 ) as a minimal default that preserves most of the trace and uses a single regeneration per sample. We use the sweep below to characterize how PC-WMV accuracy varies with ( τ , K ) (\tau,K) , not to select the operating point.

Two observations follow. At 250k tokens, high-cost configurations (large K K and small τ \tau ) underperform Standard MV because each regeneration eats into the budget for new groups: τ = 0.25 \tau{=}0.25 , K = 3 K{=}3 PC-cubic (cost ≈ 3.25 × {\approx}3.25{\times} ) reaches .493, .709, .874, and .882 on FrontierScience-Olympiad, HMMT, AIME, and Brumo, underperforming Standard MV on the latter three (.736, .881, .901), while the low-cost τ = 0.75 \tau{=}0.75 , K = 1 K{=}1 (cost ≈ 1.25 × {\approx}1.25{\times} ) outperforms Standard MV on all four. At 1M–5M budgets, the default τ = 0.75 \tau{=}0.75 , K = 1 K{=}1 stays close to the per-cell best on the three math benchmarks (HMMT, AIME, Brumo). FrontierScience-Olympiad is the exception, where the larger discrimination gap at deeper truncation repays the higher per-group cost (PC-cubic at τ = 0.25 \tau{=}0.25 , K = 3 K{=}3 reaches .547 at 1M and .562 at 5M on FrontierScience-Olympiad, against .537 and .545 at τ = 0.75 \tau{=}0.75 , K = 1 K{=}1 ). K = 1 K{=}1 is sufficient on the math benchmarks at 1M, while K = 3 K{=}3 yields modest improvements on HMMT at 5M (PC-cubic .822 at K = 3 K{=}3 vs. .814 at K = 1 K{=}1 , both at τ = 0.75 \tau{=}0.75 ). Overall, the default τ = 0.75 \tau{=}0.75 , K = 1 K{=}1 remains effective across the four benchmarks without being tuned to them, and the results of the main paper in Table 3 are therefore not sensitive to a particular choice of ( τ , K ) (\tau,K) .

### D.6 Robustness to Judge Choice

We show that PC’s per-cell advantage over the best baseline holds regardless of whether answer equivalence is evaluated by the model itself or by a stronger external grader.

The main paper uses each evaluated model itself to determine answer equivalence (Appendix H.2 ). One possible concern is that the evaluation may be biased by the limited capability of the model itself. As a robustness check, this section reports results using a stronger external grader. Namely, we re-scored the released pool with Claude Sonnet 4.6 [ Anthropic, 2026 ] on four models (GPT-OSS-120B, GPT-OSS-20B, Nemotron3-30B, Nemotron2-9B) across the three LLM-judged benchmarks (Brumo 2025, HMMT Feb 2026, FrontierScience-Olympiad), giving 12 cells. AIME 2025 is exact-match and is therefore judge-free.

We re-cluster the released generation pool using the external judge’s YES/NO equivalence judgments instead of the model’s own, then recompute per-sample correctness labels along with AUROC ¯ \overline{\mathrm{AUROC}} , PC-WMV accuracy, and the baseline accuracies. No new samples are drawn from the model.

##### PC’s AUROC ¯ \overline{\mathrm{AUROC}} advantage is preserved on every cell.

Figure 9 plots, per cell, the gap Δ ​ AUROC ¯ := AUROC ¯ PC − AUROC ¯ best ​ baseline \Delta\overline{\mathrm{AUROC}}:=\overline{\mathrm{AUROC}}_{\mathrm{PC}}-\overline{\mathrm{AUROC}}_{\mathrm{best\;baseline}} under self-judge ( x x ) against the same quantity under the external judge ( y y ). All 12 points fall in the same quadrant under both judges: 9 cells with Δ ​ AUROC ¯ > 0 \Delta\overline{\mathrm{AUROC}}>0 (PC ahead of the best baseline) and 3 cells with Δ ​ AUROC ¯ < 0 \Delta\overline{\mathrm{AUROC}}<0 . No cell flips. Per-cell numbers are in Table 18 .

##### WMV cost–accuracy curves under both judges nearly overlap.

Figure 10 overlays the WMV cost–accuracy curves under self-judge (faded) and the external judge (saturated) for the four primary methods (PC-cubic, Standard MV, DeepConf tail, P(True)). On Brumo and HMMT, the two layers are essentially indistinguishable. On FrontierScience-Olympiad, the external-judge curves sit above their self-judge counterparts by a roughly uniform vertical offset; PC-cubic stays the top (or tied-top) curve in every panel where it leads under self-judge, and stays below where it trails. The per-cell ordering of methods at any operating point is therefore preserved.

##### Pool-level shifts are concentrated on FrontierScience-Olympiad.

On Brumo and HMMT, the two judges disagree on fewer than 4 % 4\% of per-sample correctness labels per cell, and Pass@1 differs by at most 0.06 0.06 . On FrontierScience-Olympiad the per-sample flip rate is higher ( 9 % 9\% to 17 % 17\% ) and Pass@1 rises by up to 0.09 0.09 on three of the four cells; the fourth (GPT-OSS-20B) has compensating up- and down-flips that leave Pass@1 within 0.01 0.01 despite an 8.6 % 8.6\% flip rate. The shift reflects the external judge recognizing more equivalent surface forms than the model’s own. The added equivalences strengthen PC’s relative position rather than weaken it: in Figure 9 , three of the four FrontierScience-Olympiad points (blue) sit above the y = x y{=}x diagonal, and the leftmost column of Figure 10 shows PC’s gap over the baselines widening on those cells under the external judge.

### D.7 Reliability Signals vs. Pass@1

This subsection backs the analysis of Section 4.4 (rising r C r_{C} and a smaller, problem-dependent r W r_{W} slope within each category) with full panels and slope tables for the reproduction rates r C , r W r_{C},r_{W} under the GLM estimator (Appendix D.7.1 ), verifies that the qualitative pattern survives per-benchmark refits (Appendix D.7.2 ) and two alternative estimators (Appendix D.7.3 ), and reports the corresponding Pass@1 view for the per-sample baseline signals (Appendix D.7.4 ).

#### D.7.1 GLM Panels and Slopes

Figure 11 adds GLM panels for the two models not shown in Figure 3 (GPT-OSS-20B, Nemotron2-9B), and Table 19 reports the slopes for all five. The qualitative pattern is consistent: r C r_{C} rises with Pass@1 on both categories, while r W r_{W} has a smaller, problem-dependent slope and sits at a lower level on Science than on Math. The GLM fit kernel and cluster-bootstrap inference protocol below are shared with the alternative estimators of Appendix D.7.3 .

##### GLM fit kernel.

For each outcome Y ∈ { C , W } Y\in\{C,W\} (regenerations seeded from a correct ( C C ) or wrong ( W W ) trace, matching r C r_{C} and r W r_{W} in Section 3.1 ), fit a logistic regression Pr ⁡ ( Y j = 1 ∣ Pass@1 j ) = σ ⁡ ( β 0 , Y + β Y ⋅ Pass@1 j ) \Pr(Y_{j}=1\mid\text{Pass@1}_{j})=\sigma(\beta_{0,Y}+\beta_{Y}\cdot\text{Pass@1}_{j}) on trial-level data, where each trial j j inherits the Pass@1 of its problem, by maximum likelihood ( statsmodels.GLM , Binomial family, default iteratively reweighted least squares (IRLS) solver). Reported quantities are the slope β Y \beta_{Y} and the predicted curve on a fixed Pass@1 grid, masked to the cell’s observed support.

##### Inference protocol.

A (model, category) cell consists of N N per-problem records, each carrying its Pass@1 and two Bernoulli trial streams: r C , i , j ∈ { 0 , 1 } r_{C,i,j}\in\{0,1\} for the n C , i n_{C,i} regenerations seeded from a correct trace and r W , i , j r_{W,i,j} for the n W , i n_{W,i} from a wrong trace ( r = 1 r=1 if the regenerated answer matches the seed, 0 0 otherwise). Each problem i i contributes n C , i n_{C,i} trials ( Pass@1 i , r C , i , j ) \bigl(\text{Pass@1}_{i},\,r_{C,i,j}\bigr) to the r C r_{C} regression (and n W , i n_{W,i} trials ( Pass@1 i , r W , i , j ) \bigl(\text{Pass@1}_{i},\,r_{W,i,j}\bigr) to r W r_{W} ), where the same Pass@1 is shared across all trials from the same problem. We refer to this trial-level dataset as the expanded trials. Point estimates apply each estimator’s fit kernel f ^ Y \hat{f}_{Y} ( Y ∈ { C , W } Y\in\{C,W\} ) to the expanded trials.

Confidence intervals are derived using B = 1000 B=1000 cluster-bootstrap iterations. At iteration b b , we resample N N problem indices with replacement, then refit f ^ C ( b ) \hat{f}_{C}^{(b)} and f ^ W ( b ) \hat{f}_{W}^{(b)} on the corresponding trial set. Within-problem correlation among regenerations that share a prefix is corrected for by resampling problems rather than trials; trial-level Bernoulli standard errors would otherwise be underestimated by a factor of 2 2 to 4 4 on these data. Because f ^ C ( b ) \hat{f}_{C}^{(b)} and f ^ W ( b ) \hat{f}_{W}^{(b)} share the same resample within an iteration, the difference D ( b ) = f ^ C ( b ) − f ^ W ( b ) D^{(b)}=\hat{f}_{C}^{(b)}-\hat{f}_{W}^{(b)} inherits the correct joint distribution, and CIs for D D are read off { D ( b ) } \{D^{(b)}\} directly rather than summed from per-fit half-widths.

Pointwise 2 ​ σ 2\sigma CIs are percentile intervals at level 2 ​ ( 1 − Φ ​ ( 2 ) ) ≈ 0.0455 2(1-\Phi(2))\approx 0.0455 , taken per Pass@1 grid point for continuous estimators and per bin for the binned estimator. The two-sided bootstrap p p -value for H 0 : β = 0 H_{0}:\beta=0 in Table 19 is p = min { 1 , 2 min ( Pr b [ β ( b ) ≤ 0 ] , Pr b [ β ( b ) ≥ 0 ] ) } p=\min\{1,\,2\min(\Pr_{b}[\beta^{(b)}\leq 0],\,\Pr_{b}[\beta^{(b)}\geq 0])\} , with “ < < .001” indicating no replicate crossed zero. The seed is fixed at 0 0 . A small convergence check (3 seeds, several B B , GPT-OSS-120B Math r W r_{W} ) confirmed stability from B = 1000 B=1000 .

#### D.7.2 Robustness under Per-Benchmark Pooling

Section 4.4 pools the three Math benchmarks (HMMT Feb 2026, AIME 2025, Brumo 2025) into a single Math curve per model. Since the three span different Pass@1 ranges within a fixed model, the pooled slope could in principle reflect between-benchmark Pass@1 differences rather than a within-benchmark Pass@1 effect. To check for this confound we refit the same logistic GLM on each (model, benchmark) cell separately, with the fit kernel and cluster-bootstrap protocol of Appendix D.7.1 . Figure 12 plots the four per-benchmark curves per model in a single panel, and Table 20 reports the slopes.

The two claims in Section 4.4 both survive the per-benchmark refit. (i) β ⁡ ( r C ) > 0 \beta(r_{C})>0 on all 20 20 (model, benchmark) cells with p < 0.05 p<0.05 (in fact p < 0.001 p<0.001 on 17 17 of 20 20 cells), so the rising- r C r_{C} pattern is within-benchmark and not a pooling artefact. (ii) | β ⁡ ( r W ) | < β ⁡ ( r C ) |\beta(r_{W})|<\beta(r_{C}) on all 20 20 cells, so the smaller-magnitude statement is also within-benchmark.

The per-benchmark view further clarifies the two non-zero pooled β ⁡ ( r W ) \beta(r_{W}) values from Section 4.4 . The GPT-OSS-120B Math value + 1.14 +1.14 is driven by AIME 2025 ( + 1.92 +1.92 , p = 0.002 p=0.002 ) and Brumo 2025 ( + 3.46 +3.46 , p = 0.004 p=0.004 ), with HMMT Feb 2026 separately null ( − 0.14 -0.14 , p = 0.83 p=0.83 ): the pooled value reflects a real within-benchmark Pass@1 effect on AIME and Brumo, but the effect is benchmark-specific rather than uniform across Math. The Ministral3-14B Math value − 0.75 -0.75 is uniform across all three benchmarks ( − 0.85 -0.85 , − 0.68 -0.68 , − 0.65 -0.65 ), i.e. a within-benchmark effect that holds Math-wide. In neither case is the pooled slope a between-benchmark artefact.

#### D.7.3 Robustness under Alternative Estimators

In Figure 3 , we fit a logit-linear model. To verify that the conclusions in the main paper (that is, rising r C r_{C} , a smaller and problem-dependent r W r_{W} slope within each category, and lower r W r_{W} on Science than on Math) do not depend on that form, we rerun the same plot for all five models under two alternative estimators, sharing the cluster-bootstrap protocol of Appendix D.7.1 .

##### Trial-pooled binned estimator (Figure 13 ).

This estimator reads reproduction rates directly off the data, removing the GLM’s logit-linear assumption at the cost of bin-edge sensitivity. Bin edges come from the full-data Pass@1 quantiles, with 5 5 equal-count bins per category deduplicated by np.unique . A Pass@1 mass at zero can collapse adjacent edges, e.g. Ministral3-14B Science with 53 53 problems at zero resolves to 3 3 effective bins. Each bootstrap iteration assigns problems to those fixed edges and reports the trial-pooled rate ∑ i ∈ bin k Y , i / ∑ i ∈ bin n Y , i \sum_{i\in\mathrm{bin}}k_{Y,i}\big/\sum_{i\in\mathrm{bin}}n_{Y,i} , where k Y , i k_{Y,i} and n Y , i n_{Y,i} count reproductions and trials.

##### LOWESS smoother (Figure 14 ).

Because this estimator does not assume a monotone or parametric relationship, it can reveal any non-monotonic structure in r W r_{W} that a logit-linear model would inadvertently hide. We use statsmodels.nonparametric.smoothers_lowess on trial-level ( Pass@1 j , Y j ) (\text{Pass@1}_{j},Y_{j}) pairs with span frac = 0.5 \mathrm{frac}=0.5 and robustness iterations 𝚒𝚝 = 0 \mathtt{it}=0 . The default 𝚒𝚝 = 3 \mathtt{it}=3 uses bisquare residual weights designed for continuous residuals, which collapse Bernoulli outcomes to degenerate 0 0 or 100 % 100\% curves (verified empirically on Science). The fit is linearly interpolated onto the GLM’s Pass@1 grid and masked to the observed support.

All three estimators agree qualitatively across all five models: r C r_{C} rises across Pass@1 on every (model, category) pair, and r W r_{W} has a smaller, problem-dependent slope with the category-specific levels described in Section 4.4 .

#### D.7.4 Baseline Confidence Signals vs. Pass@1

For comparison with Figure 3 , we repeat the per-class, Pass@1-conditioned view on the two baseline confidence signals named in the caption of Figure 2 : DeepConf tail (Figure 15 ) and P(True) (Figure 16 ). For each signal, we split per-trial values by whether the trace’s answer matches gold (Correct, solid) or not (Wrong, dashed), and fit each class per category with a Gaussian linear model s = β 0 + β ⋅ Pass@1 s=\beta_{0}+\beta\cdot\text{Pass@1} , replacing the Bernoulli logistic GLM of Appendix D.7.1 since the response is now a continuous score. The cluster-bootstrap protocol ( B = 1000 B=1000 resamples over problems, 2 ​ σ 2\sigma percentile CIs) is unchanged. Scatter overlays show per-problem mean confidence (one dot per problem per class), the continuous-signal analogue of the per-problem rate k / n k/n in Figure 3 .

## Appendix E Baseline Implementation Details

We document here the exact confidence scores and voting rules used for each baseline, since different papers use slightly different weighting conventions.

##### Glossary of baseline labels.

The baselines summarized in Section 4 appear under the following labels in our tables and figures (e.g. Table 3 and the per-model tables of Appendix D.3 ). The per-baseline paragraphs below give the full implementation details. • DeepConf [ Fu et al., 2026 ] : a family of trace-level log-probability scores ( first-token , Mean (the Self-certainty signal of Kang et al. [2025] ), bottom-10% , block-min , tail ). Each is plugged into Eq. ( 3 ) with w w as the identity. Filtered variants ( top-10% , top-90% ) keep only the top- η % \eta\% of traces by the same score before voting.

• CISC [ Taubenfeld et al., 2025 ] : Confidence-Informed Self-Consistency, a per-sample weighting scheme that draws its raw confidence from one of four sources: Response probability [ Wang et al., 2023b ] (length-normalized geometric mean of per-token probabilities), Verbal binary [ Lin et al., 2022 ] (a 0/1 self-rating parsed from a follow-up call), Verbal 0–100 [ Lin et al., 2022 ] (a percentage self-rating parsed from a follow-up call), and P(True) [ Kadavath et al., 2022 ] (the renormalized softmax probability of the “ 1 1 ” token versus “ 0 0 ” at the rating-call confidence position).

• Adaptive stopping : cost–accuracy curves traced by sweeping the early-stopping hyperparameter of Adaptive Consistency ( AC sweep [ Aggarwal et al., 2023 ] ) and Early-Stopping Self-Consistency ( ESC sweep [ Li et al., 2024 ] ) over the same initial pool.

• SubthoughtReasoner [ Hammoud et al., 2025 ] : a single-trace refinement baseline that segments each trace at linguistic cues and votes over per-subthought regenerations. It appears only in the GPT-OSS-20B all-baselines tables (Tables 7 and 12 ).

• PC-linear, PC-quadratic, PC-cubic : PC-WMV (Algorithm 1 ) instantiated with the power-family weighting w ( n ) ​ ( c ) = c n w^{(n)}(c)=c^{n} at n = 1 , 2 , 3 n=1,2,3 . We use “PC-cubic” as shorthand for PC-WMV with n = 3 n{=}3 .

##### Deep Think with Confidence (DeepConf) [ Fu et al., 2026 ] .

We compute five trace-level confidence scores from the top- 20 20 token log-probabilities saved at generation, following the original implementation. 3 3 3 https://github.com/facebookresearch/deepconf For a trace y i y_{i} , let P t , j P_{t,j} be the j j -th largest token probability at position t ≤ | y i | t\leq|y_{i}| . The readout ℓ i = { P t , j } t ≤ | y i | , j ≤ 20 \ell_{i}=\{P_{t,j}\}_{t\leq|y_{i}|,\,j\leq 20} is the top- 20 20 log-probability record along y i y_{i} . Write C t = − 1 20 ∑ j = 1 20 log P t , j C_{t}=-\frac{1}{20}\sum_{j=1}^{20}\log P_{t,j} for the negative top- 20 20 mean at position t t . The five trace-level signals s ⁡ ( y i , ℓ i ) s(y_{i},\ell_{i}) are:

The Mean score above is a top- 20 20 implementation of the self-certainty signal originally proposed by Kang et al. [2025] on the full vocabulary. We adopt it as our Self-certainty baseline and report it under that label throughout the paper. DeepConf is the case of Eq. ( 3 ) where s ⁡ ( y i , ℓ i ) s(y_{i},\ell_{i}) is one of the five signals above and w w is the identity, giving v i ( a ) = s ( y i , ℓ i ) ⋅ 𝟏 [ a i = a ] v_{i}(a)=s(y_{i},\ell_{i})\cdot\mathbf{1}[a_{i}=a] , where a i a_{i} is the answer extracted from trace i i . Confidence filtering (Section 3.2 of their paper) optionally restricts the sum to the top- η % \eta\% of traces by s ⁡ ( y i , ℓ i ) s(y_{i},\ell_{i}) before aggregation. The unfiltered variant ( DeepConf-<score> ) sums v i ​ ( a ) v_{i}(a) over all traces, for each of the five scores above. In addition, we evaluate four filtered variants that combine the two stronger scores with the two retention levels proposed in the paper:

The DeepConf online early-termination mechanism is not used: our evaluation is offline over a pre-generated pool under a shared token budget.

##### Confidence-Informed Self-Consistency (CISC) [ Taubenfeld et al., 2025 ] .

CISC (Definition 3.1 of their paper) extracts a per-sample raw confidence s i = s ⁡ ( y i , ℓ i ) s_{i}=s(y_{i},\ell_{i}) from one of four sources drawn from prior work, then applies a softmax weighting w ⁡ ( s i ) = exp ⁡ ( s i / T ) / ∑ j exp ⁡ ( s j / T ) w(s_{i})=\exp(s_{i}/T)/\sum_{j}\exp(s_{j}/T) (over samples) with tunable temperature T T :

The original CISC release 4 4 4 https://github.com/google-research/google-research/tree/master/cisc targets non-reasoning models and forces a single-token response ( temperature=0 , max_tokens=1 ). This setting is incompatible with our reasoning models, whose chat template (e.g., Harmony for GPT-OSS) leaves the final channel open at the end of the saved trace: the appended rating suffix sits inside that open channel, and the model may emit channel-control tokens or brief reasoning before producing the digit, and occasionally reopens an analysis or commentary channel after the digit. For our reasoning models we therefore make a separate completions call per initial sample, continuing from the saved trace y i y_{i} appended with a short rating suffix and using each model’s recommended sampling parameters. Verbal binary and P(True) share the binary suffix “ Now I will rate my confidence in the proposed answer as either 0 or 1. Proposed confidence: ( ”, and the Verbal 0–100 suffix is “ Now I will rate my confidence in the proposed answer on a scale of 0–100. Proposed confidence: ( ” (with leading newline). The follow-up call is allowed to reason. We then detect the CoT-to-final delimiter and read the confidence from the final portion (first token whose top- 20 20 candidates contain “ 0 0 ” or “ 1 1 ” for Verbal binary and P(True), first integer up to “)” for Verbal 0–100). A single binary call serves both Verbal binary (text parse of the digit) and P(True) (top- 20 20 logprob softmax of “ 1 1 ” versus “ 0 0 ” at the same token). The suffix wording mirrors the CISC public release. Parse failures are imputed with the per-problem median of the non-missing scores, which keeps the answer in the vote at a neutral weight (Appendix H.1 discusses why this is preferred over dropping the sample from the pool). To avoid a baseline-specific T T search that could over-fit our benchmarks, we report the untuned linear weighting w ⁡ ( s ) = s w(s)=s for each source (verbal 0 0 – 100 100 rescaled to [ 0 , 1 ] [0,1] ), so v i ( a ) = s ( y i , ℓ i ) ⋅ 𝟏 [ a i = a ] v_{i}(a)=s(y_{i},\ell_{i})\cdot\mathbf{1}[a_{i}=a] . Softmax with T = 1 T{=}1 is also computed by our pipeline but omitted from the tables because it consistently underperforms the linear variant. A full T T sweep is left to future work.

Under the budget accounting defined in Appendix G.1 , we charge Verbal binary, Verbal 0–100, and P(True) a per-sample token cost of | y i | |y_{i}| plus the length of the secondary-call output up to and including the parsed digit (or its enclosing “)”). Here, we charge this minimum-parse length rather than the full secondary-call length because the model occasionally continues with extra reasoning after the digit that the parser ignores. Charging that overflow would overstate the unavoidable cost of these baselines. A tighter max_tokens cap on the secondary call would bound the overflow at the source, but we leave the secondary call’s maximum output length matched to the initial generation budget (Appendix I ) to avoid baseline-specific tuning, and rely on the parser-anchored cost above to keep the budget accounting honest. Response probability has no secondary call: the per-token log-probabilities of y i y_{i} are saved at initial generation and read for free.

##### Adaptive Consistency (AC) [ Aggarwal et al., 2023 ] .

AC consumes the initial pool one sample at a time and stops at the first k k for which a Beta-binomial posterior favors the running top answer over the runner-up by at least C thresh C_{\mathrm{thresh}} . Let n 1 n_{1} and n 2 n_{2} be the top- 1 1 and top- 2 2 answer counts after k k samples. The closed-form stopping criterion is 1 − I 1 / 2 ​ ( n 1 + 1 , n 2 + 1 ) ≥ C thresh , 1-I_{1/2}(n_{1}+1,\,n_{2}+1)\;\geq\;C_{\mathrm{thresh}}, where I x ​ ( α , β ) I_{x}(\alpha,\beta) is the regularized incomplete beta function. This is the analytic equivalent of the Monte Carlo integral implemented in the official release. 5 5 5 https://github.com/Pranjal2041/AdaptiveConsistency At the stop time, the prediction is the running mode, so AC adds no per-sample weighting: it is Standard MV truncated at a natural stopping point. The original paper reports C thresh = 0.95 C_{\mathrm{thresh}}=0.95 as the default and sweeps [ 0.5 , 1 ) [0.5,1) in Figure 2 to trace a cost–accuracy frontier. We sweep C thresh ∈ { 0.5 , 0.6 , 0.7 , 0.8 , 0.9 , 0.95 , 0.97 , 0.99 , 0.995 , 0.999 } C_{\mathrm{thresh}}\in\{0.5,0.6,0.7,0.8,0.9,0.95,0.97,0.99,0.995,0.999\} . Each value yields a single (cost, accuracy) point at its natural stopping cost, and we label the resulting curve “AC sweep”.

##### Early-Stopping Self-Consistency (ESC) [ Li et al., 2024 ] .

ESC consumes the initial pool in fixed-size windows of W W samples. When a window is unanimous, ESC locks that answer as the final prediction and stops. Otherwise, the window’s votes are added to a running counter and a new window is drawn. Before any lock, the intermediate prediction is the mode of the running counter. The paper recommends W = 5 W=5 for most tasks and W = 8 W=8 for MATH. Our streaming reformulation reproduces the lock semantics of the official batch release. 6 6 6 https://github.com/Yiwei98/ESC We sweep W ∈ { 2 , 3 , … , 10 } W\in\{2,3,\ldots,10\} and label the resulting natural-stopping curve “ESC sweep”. Like AC, ESC is Standard MV with a window-based stopping rule and adds no per-sample weight.

##### Cost accounting for AC and ESC.

Both methods consume only initial samples. Their per-trial budget is the cumulative generated-token length of the consumed initial samples, the same cost accounting used by Standard MV, Self-certainty, DeepConf, and Response probability. Because each hyperparameter value yields one (cost, accuracy) point at its natural stopping cost rather than a curve over a shared budget grid, we treat the points across the swept hyperparameter as the method’s cost–accuracy curve and interpolate it for any required budget. The pool size N N bounds how many tokens AC and ESC can spend, so their plateaus are bounded by N N -sample Standard MV.

##### SubthoughtReasoner [ Hammoud et al., 2025 ] .

At the time of writing, no official implementation was available, so we reimplemented the method based on the description provided in the original paper. Our implementation segments each reasoning trace into sequential subthoughts at the linguistic cues described in Section 3 of their paper, regenerates a continuation from the end of each subthought, and takes an unweighted majority vote over the resulting pool of answers. To bound the per-problem cost of constructing this pool, we process initial samples in order, accumulating each sample’s initial tokens together with its subthought-regenerated continuations, and stop once the cumulative cost reaches that of the N N initial samples for that problem. Otherwise, the per-problem cost of regenerating subthought continuations from all N N initial samples would be several times that of the initial generation alone. We evaluated this baseline on only a small subset of (model, benchmark) conditions.

##### Prefix consistency (ours).

For prefix consistency, ℓ i = ∅ \ell_{i}=\emptyset : it reads only generated tokens and regenerated answers, with no log-probability access. Unlike the per-sample signal s ⁡ ( y i , ℓ i ) s(y_{i},\ell_{i}) used by the baselines above, our signal c i ( τ ) ​ ( a ) c_{i}^{(\tau)}(a) is defined per distinct candidate a ∈ A i ( τ ) a\in A_{i}^{(\tau)} (Section 3.1 ). Moreover, we use the power-family weighting w ( n ) ​ ( c ) = c n w^{(n)}(c)=c^{n} for n ∈ { 1 , 2 , 3 } n\in\{1,2,3\} (PC-linear, PC-quadratic, PC-cubic). PC-linear ( n = 1 n{=}1 ) admits a simple interpretation: substituting w ⁡ ( c ) = c w(c)=c and Eq. ( 7 ) into the PC-WMV vote gives ∑ i v i ​ ( a ) = 1 K + 1 ​ ∑ i | { a ′ ∈ A i ( τ ) : a ′ = a } | \sum_{i}v_{i}(a)=\tfrac{1}{K+1}\sum_{i}|\{a^{\prime}\in A_{i}^{(\tau)}:a^{\prime}=a\}| , which is proportional to the count of a a in the combined pool of N N initial answers and N ​ K NK regenerations. PC-linear’s argmax therefore coincides with unweighted majority voting on this ( K + 1 ) ​ N (K{+}1)N pool, treating each regeneration as one additional vote of equal weight. PC-quadratic and PC-cubic depart from this baseline by giving super-linear weight to candidates that the same group reproduces.

## Appendix F Examples of Prefix Consistency

Figure 17 shows two representative examples of how regeneration behaves after truncation. When the initial answer is correct, the regenerated continuation often recovers the same core reasoning structure and reproduces the correct answer. In contrast, when the initial reasoning is already flawed, regeneration typically does not repair it. Instead, it continues along a similar erroneous line of reasoning and may even produce a different wrong answer. These examples help illustrate why regeneration amplifies the consistency of correct traces while still failing to escape incorrect ones.

## Appendix G Evaluation Protocol

This appendix consolidates the analysis pipeline shared across the experimental sections of the main paper. Implementation choices specific to each baseline are in Appendix E . Hardware and inference settings are in Appendix I .

### G.1 Setup

##### Benchmarks.

We evaluate on one science benchmark (FrontierScience-Olympiad) and three math benchmarks (HMMT Feb 2026, AIME 2025, Brumo 2025). Table 21 lists the problem count, answer format, and scoring rule of each. We use the full released test split for every benchmark. Answers are extracted from the boxed expression, then math-normalized for the math benchmarks (fraction unification, degree-marker removal) or used with minimal normalization for FrontierScience-Olympiad. Equivalence to the gold answer is decided by exact match for AIME 2025 and by an LLM judge for the other three benchmarks (Appendix H.2 ). HuggingFace URLs and licenses are in Table 24 .

##### Pre-generated pool and cost vectors.

For each (model, benchmark) cell we draw N = 128 N{=}128 initial generations per problem ( N = 64 N{=}64 for Ministral3-14B, where the full N = 128 N{=}128 run had not completed at the time of writing), and for prefix-consistency methods we additionally draw K K regenerations per initial sample at the chosen truncation fraction τ \tau . All voting and analysis read from this fixed pool, so the same generated tokens back every comparison and the only randomness in the reported numbers is from the analysis-side resampling described below. Each generation carries its actual recorded token count. For each method, the cost of a vote is the cumulative generated-token length of every sample it actually reads. Standard MV, Self-certainty, DeepConf, Response probability, AC, and ESC consume only the initial samples. CISC’s verbalized sources (Verbal binary, Verbal 0–100) and P(True) additionally consume the secondary verbal-rating completions call per sample described in Appendix E . PC additionally reads the regenerated continuations from each sample’s prefix. SubthoughtReasoner reads the continuations regenerated from each subthought boundary.

##### Hyperparameter defaults.

Unless otherwise noted, every result in the main paper uses τ = 0.75 \tau{=}0.75 , K = 1 K{=}1 , and the power-family weighting w ( n ) ​ ( c ) = c n w^{(n)}(c)=c^{n} for n ∈ { 1 , 2 , 3 } n\in\{1,2,3\} . Sensitivity to alternative choices of τ \tau and K K is reported in Appendix D.5 .

##### Confidence intervals (CIs) and bootstrap conventions.

All CIs reported in this paper are 2 ​ σ 2\sigma , taken as twice the standard deviation of the trial or bootstrap distribution. The trial Monte Carlo (Sections 4.2 and 4.3 ) draws M = 500 M=500 replicates per (method, benchmark, budget) cell. The parametric ratio bootstrap (Section 4.3 ) and the cluster bootstrap over problems (Section 4.4 ) each use 1,000 1{,}000 resamples.

### G.2 AUROC ¯ \overline{\mathrm{AUROC}} for the Correctness-Predictor Evaluation (Section 4.1 )

##### Definition of AUROC ¯ \overline{\mathrm{AUROC}} .

AUROC denotes the Area Under the Receiver Operating Characteristic curve. Let 𝒬 ′ := { q ∈ 𝒬 : 0 < Pass ​ @ ​ 1 q < 1 } \mathcal{Q}^{\prime}:=\{q\in\mathcal{Q}:0<\mathrm{Pass@1}_{q}<1\} be the subset of problems on which AUROC q \mathrm{AUROC}_{q} and the per-problem rates r C , q , r W , q r_{C,q},r_{W,q} are defined, and set s i = c i ​ ( a i ) s_{i}=c_{i}(a_{i}) for prefix consistency and s i = s ⁡ ( y i , ℓ i ) s_{i}=s(y_{i},\ell_{i}) for the baselines (Appendix E ). We score each signal by a per-problem AUROC and macro-average over 𝒬 ′ \mathcal{Q}^{\prime} : AUROC q := Pr [ s i > s j | a i = a q ⋆ , a j ≠ a q ⋆ ] , AUROC ¯ := 1 | 𝒬 ′ | ∑ q ∈ 𝒬 ′ AUROC q , \mathrm{AUROC}_{q}:=\Pr\!\left[s_{i}>s_{j}\,\middle|\,a_{i}=a^{\star}_{q},\,a_{j}\neq a^{\star}_{q}\right],\qquad\overline{\mathrm{AUROC}}:=\frac{1}{|\mathcal{Q}^{\prime}|}\sum_{q\in\mathcal{Q}^{\prime}}\mathrm{AUROC}_{q}, (23) where i , j i,j are independent draws from the N N initial samples on problem q q , and the reported r C , r W , D r_{C},r_{W},D are means of r C , q , r W , q , D q r_{C,q},r_{W,q},D_{q} over 𝒬 ′ \mathcal{Q}^{\prime} .

##### AUROC computation.

For each problem q q with at least one correct and one wrong initial sample, we score the per-problem AUROC (Eq. ( 23 )) by computing the trapezoidal area under the empirical ROC of the signal s i s_{i} on the N N initial samples. Ties contribute 1 / 2 1/2 . We exclude problems for which all N N initial samples are correct or all N N initial samples are wrong (the AUROC and per-problem rates r C , q , r W , q r_{C,q},r_{W,q} are undefined there) and macro-average over the surviving problems 𝒬 ′ \mathcal{Q}^{\prime} , weighting each problem equally rather than weighting by the number of cross-class pairs. Table 2 reports this macro AUROC ¯ \overline{\mathrm{AUROC}} , and the per-problem rates r C , r W , D r_{C},r_{W},D in Table 1 are macro-averaged over the same 𝒬 ′ \mathcal{Q}^{\prime} .

For prefix consistency, the binary score c i ​ ( a i ) ∈ { 1 / 2 , 1 } c_{i}(a_{i})\in\{1/2,1\} has only one non-trivial operating point on the false-positive/true-positive rate plane, ( FPR , TPR ) = ( r W , q , r C , q ) (\mathrm{FPR},\mathrm{TPR})=(r_{W,q},r_{C,q}) , so the trapezoidal area gives AUROC q = ( 1 + D q ) / 2 \mathrm{AUROC}_{q}=(1+D_{q})/2 . Tables 1 and 2 therefore encode the same information for prefix consistency, and the AUROC ¯ \overline{\mathrm{AUROC}} ordering across benchmarks matches the D D ordering.

### G.3 Cost-Accuracy Evaluation (Sections 4.2 and 4.3 )

##### Sample-with-replacement trials.

At each token budget B B we draw samples from the pool with replacement until the cumulative cost reaches B B , then run each method’s voting rule on the drawn set and report the mean accuracy over the M M trials. The trial-mean variance used to derive the CI is σ 2 = 1 M ​ | 𝒬 | 2 ​ ∑ q p ^ q ​ ( 1 − p ^ q ) \sigma^{2}=\frac{1}{M|\mathcal{Q}|^{2}}\sum_{q}\hat{p}_{q}(1-\hat{p}_{q}) , where p ^ q \hat{p}_{q} is the trial-mean correctness on problem q q and | 𝒬 | |\mathcal{Q}| is the number of problems. This Monte Carlo CI is what is shown as “ ± \pm ” in Table 3 .

##### Dense token-budget grid.

Token-efficiency ratios in Table 4 require evaluating the cost–accuracy curve at arbitrary target budgets, so we evaluate every method on the log-uniform grid ℬ = { 10 3 + k / 100 : k = 0 , 1 , … , 400 } . \mathcal{B}=\bigl\{10^{3+k/100}\;:\;k=0,1,\ldots,400\bigr\}. The dense grid is used for all methods that admit a continuous budget (Standard MV, PC variants, DeepConf, CISC, P(True), Response probability). AC and ESC instead contribute their natural-stopping points (one per swept hyperparameter) as described in Appendix E .

##### Standard MV plateau and Pass@1.

The Standard MV plateau is Standard MV’s bootstrap-saturated accuracy on the N N -sample initial pool, taken as Standard MV’s stored accuracy at max ⁡ ℬ = 10 7 \max\mathcal{B}=10^{7} tokens. We use this finite-budget anchor rather than the unbounded i.i.d. asymptote (which is pool-determined but, on slow-converging problems, can sit above what any finite budget reaches) so that the target stays reachable by Standard MV at every α ∈ [ 0 , 1 ] \alpha\in[0,1] . Pass@1 is the closed-form expected accuracy of a single uniformly drawn pool sample, computed directly from the pool.

##### Monotone envelope and log-budget interpolation.

Each method’s grid of (budget, accuracy) points is reduced to its running-max envelope along sorted budget (so accuracy is non-decreasing in budget). This gives the “min budget at which the method has ever reached this accuracy” semantics that the token-efficiency ratio is meant to compare. To read off the budget at a target accuracy acc tgt \mathrm{acc}_{\mathrm{tgt}} , we find the first envelope segment ( B ( j − 1 ) , acc ( j − 1 ) ) → ( B ( j ) , acc ( j ) ) (B^{(j-1)},\mathrm{acc}^{(j-1)})\to(B^{(j)},\mathrm{acc}^{(j)}) that brackets acc tgt \mathrm{acc}_{\mathrm{tgt}} and linearly interpolate in (accuracy, log-budget): log ⁡ B tgt = log ⁡ B ( j − 1 ) + acc tgt − acc ( j − 1 ) acc ( j ) − acc ( j − 1 ) ⋅ ( log ⁡ B ( j ) − log ⁡ B ( j − 1 ) ) . \log B_{\mathrm{tgt}}=\log B^{(j-1)}+\frac{\mathrm{acc}_{\mathrm{tgt}}-\mathrm{acc}^{(j-1)}}{\mathrm{acc}^{(j)}-\mathrm{acc}^{(j-1)}}\cdot(\log B^{(j)}-\log B^{(j-1)}). The same rule applies to AC and ESC, whose curves are the natural-stopping point lists.

##### Parametric bootstrap for ratio CIs.

Confidence intervals on B method / B MV B_{\mathrm{method}}/B_{\mathrm{MV}} come from a parametric bootstrap with the same trial Monte Carlo noise model used by Table 3 . Each draw perturbs every fixed-budget accuracy entry by independent 𝒩 ⁡ ( 0 , σ acc 2 ) \mathcal{N}(0,\sigma_{\mathrm{acc}}^{2}) noise with σ acc = CI acc / 2 \sigma_{\mathrm{acc}}=\mathrm{CI}_{\mathrm{acc}}/2 (one σ \sigma from the stored 2 ​ σ 2\sigma CI), and additionally perturbs each natural-stopping operating point’s cost by 𝒩 ⁡ ( 0 , σ cost 2 ) \mathcal{N}(0,\sigma_{\mathrm{cost}}^{2}) noise with σ cost = CI cost / 2 \sigma_{\mathrm{cost}}=\mathrm{CI}_{\mathrm{cost}}/2 (the trial-MC standard error of the natural-stopping cost, which varies across operating points unlike the fixed-budget cost). The plateau is perturbed by an analogous draw using its own CI. Each replicate then recomputes the envelope, the target acc tgt = Pass ​ @ ​ 1 + α ⋅ ( plateau ′ − Pass ​ @ ​ 1 ) \mathrm{acc}_{\mathrm{tgt}}=\mathrm{Pass@1}+\alpha\cdot(\mathrm{plateau}^{\prime}-\mathrm{Pass@1}) with the perturbed plateau plateau ′ \mathrm{plateau}^{\prime} , and the ratio. Pass@1 is closed-form over the pool (deterministic) and is held fixed across draws. Anchoring the plateau to Standard MV’s stored accuracy at max ⁡ ℬ \max\mathcal{B} rather than to the running-max envelope’s max breaks the upward extreme-value bias that an iid + running-max combination would otherwise inject near the plateau. Cells where the method’s monotone envelope does not reach the target on the point estimate are reported as “N/A”. The CI subscript is additionally suppressed (point estimate shown alone) when fewer than 50 % 50\% of bootstrap draws reach the target.

### G.4 Reproduction-Rate GLM (Section 4.4 )

##### Logistic GLM and cluster bootstrap.

The slopes β ⁡ ( r C ) \beta(r_{C}) and β ⁡ ( r W ) \beta(r_{W}) in Section 4.4 and Table 19 are the Pass@1 coefficients of a per-(model, category) logistic GLM fit on the expanded per-trial Bernoulli outcomes: logit ​ r C \mathrm{logit}\,r_{C} (and separately logit ​ r W \mathrm{logit}\,r_{W} ) is fit as an affine function of Pass@1, where each (correct initial sample, regeneration) pair contributes one trial to the r C r_{C} fit, each (wrong initial sample, regeneration) pair contributes one trial to the r W r_{W} fit, and every trial carries the source problem’s Pass@1 as its covariate. The fit uses statsmodels’ GLM with a binomial family. CIs and p p -values come from a joint cluster bootstrap over whole problems: each resample draws problems with replacement (preserving each problem’s full set of trials) and refits the GLM. We report band-widths from the bootstrap distribution and two-sided p p -values from the empirical sign distribution.

## Appendix H Answer Extraction and Equivalence Judging

Final answers are extracted from \boxed{} via regex and normalized.

### H.1 Answer Extraction

##### Boxed-answer parses.

Failed boxed responses receive no vote in any aggregator (Standard MV, PC, DeepConf, CISC), so they only ever lower the effective sample count, never bias the vote distribution toward a wrong answer. Seventeen of the twenty cells stay below 1 % 1\% on both Generations and Continuations (Table 22 ). The three cells that exceed 1 % 1\% on continuations all involve Nemotron3-30B: FrontierScience-Olympiad ( 0.17 % → 1.62 % 0.17\%\to 1.62\% ), AIME 2025 ( 0.00 % → 1.17 % 0.00\%\to 1.17\% ), and Brumo 2025 ( 4.14 % → 1.25 % 4.14\%\to 1.25\% , the only cell with generations also above 1 % 1\% ). We treat boxed parse failures as missing votes rather than as a separate signal because the rate is small enough that it does not move the relative comparisons reported in the paper.

##### Verbal score handling.

For the verbal-confidence calls used by CISC, Verbal binary, and P(True), the parser fails when the secondary completion does not yield an integer in the requested range (a 0–100 value for CISC, a 0/1 verdict for Verbal binary). P(True) reads the logprob of the binary call’s “1” token directly, so it is essentially never missing. Verbal failure rates show wide model spread, under 1 % 1\% for Nemotron2-9B and Ministral3-14B versus 19 % 19\% – 56 % 56\% for GPT-OSS and Nemotron3-30B on Verbal 0–100 (Table 22 ). The two analyses that consume verbal scores handle parse failures charitably to the verbal baselines: the AUROC table (Table 2 ) drops failures, while the WMV pipeline imputes the per-problem median (Appendix E ). Dropping the sample from the WMV pool would bias the per-problem answer distribution if failures correlate with the boxed answer, and would also hide the parser-failure rate from the evaluation. Keeping each failure at its natural pool frequency instead mirrors the deployment-time behavior in which a fresh draw would re-incur the same parse error rate. We therefore treat parser fragility as an intrinsic property of the baseline, with each failure contributing a neutrally-weighted vote. Table 23 reports AUROC ¯ \overline{\mathrm{AUROC}} under both modes side-by-side. The gap is at most 0.031 0.031 on every cell, so failure handling does not change the best signal on any cell. The secondary-call token cost is charged regardless of parse success, so a high failure rate raises the per-vote cost rather than reducing the effective sample count.

Abbreviations: FSci = FrontierScience-Olympiad, HMMT = HMMT Feb 2026, AIME = AIME 2025, Brumo = Brumo 2025.

##### Verbal 0–100 parser fragility.

The parser splits the model’s response on the first “)” and scans for any digit before it, expecting a near-immediate “ <digit>) ” completion (the prompt suffix already opens an explicit “ Proposed confidence: ( ”). The dominant failure pattern is a parenthetical or commentary token landing before the digit, for example “ score) 70 ”, “ analysis) 87 (commentary?) (final) 93 ”, “ rating)\n\n**70**. ”, “ (C) 80% ”, and “ value).\n(If you think...) ”. A smaller share of failures is completions with no digit at all, such as “ score). That is this answer: **safe**. ”. The model that does not fail at all, Nemotron2-9B, has a median successful response length of just 5 5 tokens, indicating that it emits “ <digit>) ” and stops. The failing models have median successful lengths of 30 30 – 200 200 tokens, meaning even their successful completions wander past the digit and leave many opportunities for parenthetical content to land before any number. This fragility illustrates a broader challenge of porting verbalized-confidence baselines, originally designed for instruction-following models that snap to a strict response template, to reasoning models that interleave thinking, commentary, and LaTeX before committing to a structured output. The original CISC and P(True) papers validated these methods only on instruction-tuned (non-reasoning) models that reliably follow the structured response template. We extend the same prompt and parser to reasoning models without modification, and a fully robust implementation in this regime would require redesigning both the elicitation prompt and the parser.

### H.2 Equivalence Judging

##### Judge configuration.

AIME 2025 is scored by exact match on the normalized answer (integer). For benchmarks where multiple surface forms can denote the same answer (HMMT Feb 2026, Brumo 2025, and FrontierScience-Olympiad), equivalence is determined by an LLM judge: the FrontierScience-Olympiad prompt follows the official grader released with the benchmark [ Wang et al., 2025 , Appendix B] , and the math prompt follows the format used in MathArena [ Balunović et al., 2025 ] and similar competition-math evaluations. Both prompts return a single-token “YES”/“NO” verdict which is mapped to an equivalence edge. Transitive closure over these edges yields canonical answer clusters for each problem.

Using the evaluated model as its own judge is a known limitation: a stronger external grader could shift absolute accuracies. We verify in Appendix D.6 that this does not change the relative comparisons reported here: re-scoring the pool with Claude Sonnet 4.6 on a 4-model, 3-benchmark subset (12 cells) preserves the sign of AUROC ¯ PC − AUROC ¯ best ​ baseline \overline{\mathrm{AUROC}}_{\mathrm{PC}}-\overline{\mathrm{AUROC}}_{\mathrm{best\;baseline}} on all 12 cells (no cell flips), and the per-cell ordering of WMV methods is preserved at every operating point.

The full prompts used are:

##### FrontierScience-Olympiad.

You are grading an attempted answer to a science olympiad problem. You will be given the attempted answer and the reference answer. Evaluate strictly, but fairly. The reference answer is either a single number or expression in latex formatting, a chemical formula, a compound name, or a phrase referring to a specific name, entity, or method. Mark the attempted answer as correct if it fully matches the reference answer or is otherwise equivalent (e.g., an equivalent algebraic expression, a numerical number within 1 decimal place rounding of the reference answer (e.g., 6.69 ≈ \approx 6.7), an equivalent name for a compound/formula, equivalent when accounting for units, etc.). Mark it as incorrect if it is not equivalent to the reference answer. Attempted answer: {answer1} Reference answer: {answer2} Answer only ‘‘YES’’ if correct or ‘‘NO’’ if incorrect.

##### HMMT Feb 2026, Brumo 2025.

Determine whether two mathematical answers are numerically identical. Answer 1: {answer1} Answer 2: {answer2} Criteria: • If they represent exactly the same numerical value, respond ‘‘YES’’

• If they represent different values or one is not numerical, respond ‘‘NO’’

• Different formats (fractions, decimals, radicals, exponential notation) are acceptable if numerically equivalent

Examples: ‘‘1/2’’ and ‘‘0.5’’ → \to YES; ‘‘ 4 \sqrt{4} ’’ and ‘‘2’’ → \to YES; ‘‘ 2 3 2^{3} ’’ and ‘‘8’’ → \to YES; ‘‘3.14’’ and ‘‘ π \pi ’’ → \to NO; ‘‘x+1’’ and ‘‘1+x’’ → \to YES; ‘‘ x 2 x^{2} ’’ and ‘‘2x’’ → \to NO. Answer only ‘‘YES’’ or ‘‘NO’’.

## Appendix I Reproducibility Statement

##### Code and data.

The analysis pipeline and reproduction scripts are released at https://github.com/naoto-iwase/prefix-consistency , and the answer pool used to reproduce all reported numbers is released at https://doi.org/10.5281/zenodo.20082164 .

Models and datasets are publicly available (Table 24 ). Initial generation is stochastic (no vLLM seed), but aggregation and voting use seed 42 42 , so every reported number is bitwise reproducible from the pool.

##### Inference and sampling.

Each model is served through a vLLM OpenAI-compatible endpoint on 4 × 4{\times} NVIDIA A100 80GB GPUs, with context window 131,072 131{,}072 and a maximum output length of 100,000 100{,}000 tokens. Sampling uses each model’s recommended settings (Table 25 ).

Table 26 reports per-generation token counts at the default τ = 0.75 \tau{=}0.75 for all models, with the additional τ ∈ { 0.50 , 0.25 } \tau\in\{0.50,0.25\} values reported for GPT-OSS-20B (the model used in the τ \tau -sensitivity sweep of Appendix D.5 ).

##### Generation prompts.

For the three math benchmarks (HMMT Feb 2026, AIME 2025, Brumo 2025) the system prompt is “You are a helpful assistant specialized in solving mathematical problems.” For FrontierScience-Olympiad it is “You are an expert scientist solving olympiad-level problems in physics, chemistry, and biology.” Both append “Please reason step by step, and put your final answer within \boxed {} .” to each problem statement. Initial samples and the regenerated continuations from each truncation point share the same prompt.

## Instructions for reporting errors

We are continuing to improve HTML versions of papers, and your feedback helps enhance accessibility and mobile support. To report errors in the HTML that will help us improve conversion and rendering, choose any of the methods listed below:

Click the "Report Issue" ( ) button, located in the page header.

Tip: You can select the relevant text first, to include it in your report.

Our team has already identified the following issues . We appreciate your time reviewing and reporting rendering errors we may not have found yet. Your efforts will help us improve the HTML versions for all readers, because disability should not be a barrier to accessing research. Thank you for your continued support in championing open access for all.

Have a free development cycle? Help support accessibility at arXiv! Our collaborators at LaTeXML maintain a list of packages that need conversion , and welcome developer contributions .
