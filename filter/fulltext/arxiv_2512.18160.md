##### Report GitHub Issue

Content selection saved. Describe the issue below:

# Propose, Solve, Verify: Self-Play Through Formal Verification

###### Abstract

Training models through self-play alone (without any human data) has been a longstanding goal in AI, but its effectiveness for training large language models remains unclear, particularly in code generation where rewards based on unit tests are brittle and prone to error propagation. We study self-play in the verified code generation setting, where formal verification provides reliable correctness signals. We introduce Propose, Solve, Verify ( PSV ) , a simple self-play framework where formal verification signals are used to create a proposer capable of generating challenging synthetic problems and a solver trained via expert iteration. We use PSV to train PSV-Verus , which across three benchmarks improves pass@1 by up to 9.6× over inference-only and expert-iteration baselines. We show that performance scales with the number of generated questions and training iterations, and through ablations identify formal verification and difficulty-aware proposal as essential ingredients for successful self-play.

###### Keywords:

## 1 Introduction

A longstanding goal of AI research is to enable self-play , in which a system learns by creating its own curriculum without human supervision ( Silver et al., 2017 ; Sukhbaatar et al., 2018 ) . In the context of large language models (LLMs), an emerging family of proposer-solver algorithms holds the promise of improving LLMs through self-play ( Haluptzok et al., 2023 ; Zhao et al., 2025 ) . In this setup, a proposer model generates problems for a solver model to train on, and the solver’s capabilities inform the proposer’s curriculum. If one can reliably judge whether the solver’s outputs are correct, one can train the solver with reinforcement learning and successfully design curricula that adapt to the solver’s capabilities.

Thus a fundamental challenge in realizing proposer-solver self-play is verification . An imperfect verifier can be exploited by the solver, and hence corrupt the solver’s training and any curricula that depend on the solver’s performance. Indeed, successful early attempts have come in easy-to-verify domains such as formal theorem proving ( Dong and Ma, 2025 ) or easy-to-check synthetic tasks ( Haluptzok et al., 2023 ; Dong et al., 2025 ; Zhao et al., 2025 ) , leaving self-play’s scope of impact for LLMs unclear.

We study self-play for code generation, a domain where verification typically relies on unit tests ( Liu et al., 2023 ) . A fundamental limitation is that unit tests only cover a limited set of cases, so programs can pass them and still be incorrect ( Xin and Reiss, 2017 ; Liu et al., 2023 ; Yuan et al., 2024 ) . This can lead the solver to optimize for passing tests rather than solving the underlying task, and errors can propagate across iterations ( Lin et al., 2025 ; Baker et al., 2025 ) . Hence self-play in code generation remains an open problem.

We introduce Propose, Solve, Verify ( PSV ) , which uses formal verification to unlock a new paradigm for self-play in code generation. The core idea is for a proposer to generate problems in the form of formal specifications —statements that mathematically describe all possible permitted inputs plus the desired output behavior of a program with respect to those inputs—-and for a solver to try to generate programs that meet the specifications. The key benefit is that formal verification provides a sound reward signal: if the verifier accepts the program, then the program is guaranteed to satisfy its specification for all inputs. Thus unlike unit tests, formal verification prevents incorrect solutions from entering the self-play loop.

We apply PSV to Verus ( Lattuada et al., 2023 ) , a framework that enables formal verification of Rust programs and has attracted recent interest for LLM code generation (e.g., Yang et al. (2025a) ; Aggarwal et al. (2024) ). We design a difficulty-aware proposer that adapts the difficulty of proposed specifications based on the solver’s current pass rates. We initialize self-play from the same translated corpus used by AlphaVerus ( Aggarwal et al., 2024 ) , which originates from human-written problems. PSV then expands this corpus by alternating between proposing new specifications, training the solver on verified solutions, and using the solver’s performance to guide the next round of problem proposal. As shown in Figure 1 , the PSV self-play loop yields substantial gains: our model, PSV-Verus , improves across iterations and substantially outperforms both training on the seed corpus alone (RFT) and AlphaVerus, which relies on the same seed corpus but without self-play.

We show that PSV-Verus ’s performance scales with the number of iterations and generated questions, and empirically identify that verification of solutions and the difficulty-awareness and diversity of the proposal are key factors for self-play. Coupled with recent successes in formal theorem proving ( Dong and Ma, 2025 ) , our work points to formal verification as a promising frontier for LLM self-play. In summary, our contributions are as follows: 1. We introduce Propose, Solve, Verify ( PSV ), a self-play algorithm for code generation that leverages formal verification, and propose a difficulty-aware proposer based on in-context learning.

2. We train PSV-Verus , which outperforms the previous state-of-the art AlphaVerus ( Aggarwal et al., 2024 ) and Expert Iteration ( Singh et al., 2024 ) on verified Rust programming.

3. We show that performance scales with question budget and iterations, and identify proposal coverage and difficulty as factors driving self-play.

4. We release our code and models. 1 1 1 https://github.com/abwilf/psv

## 2 Related Work

#### Verified code generation.

Verified code generation asks solver models to generate both programs and machine-checkable proofs that verifiers can deterministically and mechanically check against a specification. For example in Figure 2 , the implementation and proof must satisfy the postconditions described in the ensures block of the spec over all possible inputs and outputs to the function . Unlike unit-tests, which are hard for LLMs to generate and vulnerable to reward hacking ( Yang et al., 2025a ; Baker et al., 2025 ) , formal verification provides a binary guarantee of correctness. This makes the setting attractive for safety-critical domains ( Klein et al., 2014 ) and for self-improving AI that requires verification of novel questions. Recently developed formal verification languages such as Verus ( Lattuada et al., 2023 ) bring SMT-backed proofs into mainstream systems languages such as Rust, making formal verification possible in real world, modern programming domains. A key obstacle to model performance on these tasks is data scarcity ( Aggarwal et al., 2024 ) , which makes synthetic corpus generation under formal verifier feedback especially promising.

#### Self-improving AI systems.

Self-play game playing algorithms such as AlphaZero have shown that AI systems can surpass human performance without human labels ( Silver et al., 2017 ) . Yet porting this paradigm to language, in particular reasoning, has been challenging: the action space is vast and verifiers are often weak instead of deterministic (e.g., the rules of the game define a win/loss). Recent work has made progress on self-improving language models with rejection-finetuning ( Singh et al., 2024 ; Zelikman et al., 2022 ) and reinforcement learning from verifiable rewards (RLVR) ( Shao et al., 2024 ; DeepSeek-AI et al., 2025 ; Wen et al., 2025 ) on fixed human-generated datasets. Yet human-generated reasoning datasets are limited and difficult to scale ( Liu et al., 2025 ) , motivating the creation of synthetic data for training reasoning capabilities.

#### Self-play reasoning systems

Self-play systems leverage an intuition that there is a “gap” between what AI can solve and verify ( Song et al., 2024 ) , meaning that systems could self-improve by proposing novel problems and verifiers and training a “solver” model on verified solutions. This has been applied to reasoning games ( Cheng et al., 2025b ) , code ( Rozière et al., 2023 ; Wei et al., 2024 ; Haluptzok et al., 2023 ) , and math ( Shah et al., 2024 ) . A recent line of work has also proposed recursively self-improving, by training the question proposer as well to output difficult problems for the current solver ( Li et al., 2024 ; Huang et al., 2025 ) . This has been applied to formal math ( Dong and Ma, 2025 ) , coding ( Zhao et al., 2025 ; Lin et al., 2025 ) , tool use ( Zhou et al., 2025 ) , alignment ( Cheng et al., 2025a ; Zhu et al., 2025 ) , and general language tasks ( Kuba et al., 2025 ) . As strong verifiers are important to self-play (yet often limited in applicability) ( Saad-Falcon et al., 2025 ) , we investigate the verified coding domain in Verus ( Lattuada et al., 2023 ) where SMT-backed verification provides a sound guarantee over a Turing-complete language (Rust).

## 3 Propose, Solve, Verify ( PSV )

Propose, Solve, Verify (PSV) leverages a formal verifier to enable a self-play loop. The core idea is to iterate between proposing specifications, attempting to solve the specifications, and using the formal verifier’s feedback to improve the solver and inform the next round of problem proposal. Over time the solver trains with an evolving pool of challenging and diverse problems, yielding improvements in the solver’s capabilities. We describe each component in detail below.

#### Problem setting.

We consider the problem of verified code generation. In this problem, the input is a formal specification x ∈ 𝒳 x\in\mathcal{X} , and the output is code y ∈ 𝒴 y\in\mathcal{Y} . A verifier v ⁡ ( x , y ) → { 0 , 1 } v(x,y)\rightarrow\{0,1\} checks whether the code meets the formal specification. If so, the verifier returns 1 and otherwise it returns 0. The specification and code are written in a language that supports verification, such as Verus ( Lattuada et al., 2023 ) which supports verification for a subset of Rust code, or Dafny ( Leino, 2010 ) . The code y y contains an implementation and any additional proof code (e.g., “loop invariants”) that is necessary for the program to pass the verifier. Given a specification x x , the goal is to produce code y y that passes the verifier, v ⁡ ( x , y ) = 1 v(x,y)=1 . The key property that we leverage is that the Verus verifier is sound with respect to specifications, i.e., if v ⁡ ( x , y ) = 1 v(x,y)=1 then the program y y meets the specification x x . See Appendix F for additional background.

While we consider formally verified code generation here, in principle our methods apply to any problem with a sound verifier, i.e., if the verifier v ⁡ ( x , y ) v(x,y) returns 1, then y y is a correct output for problem x x . Applying PSV to other such problems is left for future work.

### 3.1 Propose, Solve, Verify ( PSV )

PSV is an algorithm that runs for iterations t ∈ { 1 ​ … ​ T } t\in\{1\ldots T\} and consists of a proposer model P ϕ t P_{\phi_{t}} and a solver model S θ t S_{\theta_{t}} , working together to generate and solve new problems, supervised with help from the verifier.

At the first iteration ( t = 0 t=0 ), PSV receives a set of seed problem specifications X t = { x 1 , x 2 , … , x N 0 } X_{t}=\{x_{1},x_{2},\ldots,x_{N_{0}}\} , and the solver attempts to solve them. That is, given a specification x i x_{i} the solver produces candidate outputs y i , t 1 , … , y i , t k t ​ r ​ n y_{i,t}^{1},\ldots,y_{i,t}^{k_{trn}} , where k t ​ r ​ n k_{trn} is a hyperparameter governing the number of solver attempts per specification. Each output has an associated verification outcome v i , t j ∈ { 0 , 1 } v_{i,t}^{j}\in\{0,1\} obtained by running the verifier on x i , y i , t j x_{i},y_{i,t}^{j} . Over all specifications x ∈ X t x\in X_{t} , this yields a data pool D t = ( X t , Y t , V t ) D_{t}=(X_{t},Y_{t},V_{t}) .

The solver is then trained using the data pool, yielding a new solver S θ t + 1 S_{\theta_{t+1}} . Finally, the proposer P ϕ t P_{\phi_{t}} is updated using the data pool and is used to generate a new set of B B specifications that are added to the existing set, so that X t + 1 = X t ∪ { x N t + 1 , x N t + 2 , … , x N t + B } X_{t+1}=X_{t}\cup\{x_{N_{t}+1},x_{N_{t}+2},\ldots,x_{N_{t}+B}\} . The process iterates for a fixed number of iterations T T .

Next, we describe the specific design choices for the solver, learning algorithm, and proposer that we use in our experiments, including our difficulty-aware proposer. We summarize PSV in Algorithm 1 .

#### Solving.

At each iteration t t , PSV produces candidate solutions for each x i ∈ X t x_{i}\in X_{t} by sampling from the solver model S θ t S_{\theta_{t}} with temperature 0.8, yielding k t ​ r ​ n k_{trn} candidate solutions for each: y i , t 1 , … , y i , t k t ​ r ​ n y_{i,t}^{1},\ldots,y_{i,t}^{k_{trn}} , along with binary verification outcomes v i , t 1 , … , v i , t k t ​ r ​ n v_{i,t}^{1},\ldots,v_{i,t}^{k_{trn}} . We follow AlphaVerus’s few shot prompting setup ( Aggarwal et al., 2024 ) with a 1-shot example. We found that while increasing the number of few-shot examples improved performance, it also increased runtime substantially because solving is the most computationally intensive part of the pipeline, and the method was improving without more few-shot examples.

#### Rejection-Finetuning.

The solver is updated through rejection fine-tuning (RFT) ( Singh et al., 2024 ) , where the base model is fine-tuned only on verified solutions. Formally, we construct the training data for a single iteration of RFT as D t ∗ ← { ( x i , y i , t j ) : i ∈ D t , v i , t j = 1 } D_{t}^{*}\leftarrow\left\{(x_{i},y_{i,t}^{j}):i\in D_{t},v_{i,t}^{j}=1\right\}

We then trim D t ∗ D_{t}^{*} to keep a maximum of one solution to each problem i i if there are multiple values of j j s.t. v i , t j = 1 v_{i,t}^{j}=1 . The solver is then updated by minimizing the cross-entropy loss: ℒ ( θ ) = − 1 | D t ∗ | ∑ ( x i , y i j ) ∈ D t ∗ ∑ k = 1 | y i j | log p θ ( y i j [ k ] ∣ x i , y i j [ < k ] ) \mathcal{L}(\theta)=-\frac{1}{|D_{t}^{*}|}\sum_{(x_{i},y_{i}^{j})\in D_{t}^{*}}\sum_{k=1}^{|y_{i}^{j}|}\log p_{\theta}(y_{i}^{j}[k]\mid x_{i},y_{i}^{j}[<k]) where θ \theta is initialized from θ 0 \theta_{0} , y i j ​ [ k ] y_{i}^{j}[k] is the k k -th token of solution y i j y_{i}^{j} , and y i j [ < k ] y_{i}^{j}[<k] denotes all preceding tokens. Iteratively training on verified solutions in this way can be seen as an offline RL algorithm based on expectation-maximization ( Singh et al., 2024 ) . Further details about SFT training can be found in Appendix E .

In principle, different reinforcement learning algorithms could have been used, such as GRPO ( Shao et al., 2024 ) . We use RFT because the Verus verifier is guaranteed to be sound but not complete, meaning that advantage-weighted algorithms could incorrectly punish models for correct solutions that were judged to be incorrect. Future work on on-policy RL algorithms for formally verified self-play may investigate more performant RL algorithms in this setting.

#### Proposing.

At iteration t t , proposer P ϕ , t P_{\phi,t} generates B B new problem specs at target difficulty levels by conditioning on problems and associated difficulty labels. We estimate the difficulty of question x i x_{i} at iteration t t by the current solver’s pass rate on that problem: r i , t = 1 k t ​ r ​ n ​ ∑ j = 1 k t ​ r ​ n v i , t j r_{i,t}=\frac{1}{k_{trn}}\sum_{j=1}^{k_{trn}}v_{i,t}^{j} We categorize problems into one of four classes based on r i , t r_{i,t} : Easy , Medium , Hard , and Impossible : difficulty ​ ( x i , t ) = { Easy if ​ r i , t ≥ τ E Medium if ​ τ M ≤ r i , t < τ E Hard if ​ 0 < r i , t < τ M Impossible if ​ r i , t = 0 , \text{difficulty}(x_{i},t)=\begin{cases}\textsc{Easy}&\text{if }r_{i,t}\geq\tau_{E}\\ \textsc{Medium}&\text{if }\tau_{M}\leq r_{i,t}<\tau_{E}\\ \textsc{Hard}&\text{if }0<r_{i,t}<\tau_{M}\\ \textsc{Impossible}&\text{if }r_{i,t}=0,\end{cases} where the thresholds τ E \tau_{E} and τ M \tau_{M} are hyperparameters for our method.

We then sample k p ​ r ​ o ​ p k_{prop} problems from D t D_{t} to use as examples and ask the proposer to output a question at a target difficulty level. A simplified version of our prompt is below, and the complete prompt is in Appendix A . This mechanism continually refreshes the prompt distribution, updating the proposer to P ϕ , t + 1 P_{\phi,t+1} through in-context learning and expanding the problem frontier in a difficulty-controlled manner.

After inference, specifications are parsed, deduplicated, and filtered through a spec verifier which ensures that the spec defines a valid set of mathematical pre- and post-conditions. This uses a form of Verus that ignores the implementation body – details are in Appendix D .

## 4 Experiments

We study self-play verified code generation in the Verus language ( Lattuada et al., 2023 ) .

#### Datasets and evaluation.

We evaluate our approach using three Verus datasets. Dafny2Verus (274 problems) is a translation-derived corpus adapted from the AlphaVerus ( Aggarwal et al., 2024 ) pipeline, providing a diverse set of formally verified Dafny problems translated into Verus. MBPP -Verified (78 problems) is based on the MBPP dataset ( Austin et al., 2021 ) , following the verified adaptation process described in ( Yang et al., 2025a ; Misu et al., 2024 ) , where each task includes executable Rust+Verus specifications and proofs. HumanEval -Verified (85 functions across 49 original programs) is drawn from an open-source HumanEval-Verus effort ( Contributors, 2024 ) , which translates Python HumanEval tasks ( Chen et al., 2021 ) into Verus. Each multi-function program is decomposed into independently verifiable functions, ensuring all necessary dependencies are preserved. All datasets require generating Rust+Verus code that passes the Verus verifier ( Lattuada et al., 2023 ) . We will omit the *-Verified from the names for brevity throughout the rest of the paper. We adopt the widely used Pass@ k k metric ( Chen et al., 2021 ) : for n n samples and c c verified successes, pass@ k = 1 − ( n − c k ) / ( n k ) k=1-\binom{n-c}{k}/\binom{n}{k} . We measure Pass@1, 5, and 10, and run our final evaluation with n = 100 n=100 to provide a strong unbiased estimate of the evaluation metrics.

#### Settings.

We study our method’s performance in two settings. In a setting we refer to as transfer learning we set X 0 X_{0} to the set of questions in Dafny2Verus and report performance on MBPP and HumanEval as a held out test set. In a setting that we refer to as test-time training (TTT) ( Sun et al., 2020 ) , we set X 0 X_{0} to the set of questions in each dataset, and run our method on that dataset alone. It is worth noting that human-written solutions are never trained on .

#### Baselines.

We compare to AlphaVerus ( Aggarwal et al., 2024 ) (no treefinement version), which is the previous SOTA method for verified code generation based on prompting with 50 in-domain exemplars. We also compare to iterative RFT ( Yuan et al., 2023 ; Singh et al., 2024 ) , which performs expert iteration without proposing new problems. We train and evaluate RFT with the same parameters as our method, excluding any parameters related to question proposal.

#### Hyperparameters and design choices.

Our hyperparameters and design choices were selected to provide a proof of concept of our idea at minimal compute scale. In the current setting, the main experiment (Table 1 ) takes around 24 hours on a single machine with 8xL40s GPUs. We use the Qwen2.5-Coder-3B-Instruct model as our base because it was the strongest open-weight code model at the 3B size. We use SGLang ( Zheng et al., 2024 ) with dp-size=8 and temperature 0.8 for all inference sampling because SGLang has large efficiency gains for inference time sampling and can parallelize over multiple GPUs on the same machine easily. We set τ M \tau_{M} to 0.2, similar to Dong and Ma (2025) (who used 0.25), and set τ E \tau_{E} to 0.8. We set k t ​ r ​ n k_{trn} to 10 to balance having enough breadth in our search to enable performance improvements and not so much that the computational requirements would become unreasonable to reproduce. We use k p ​ r ​ o ​ p = 12 k_{prop}=12 and use uniform input and output targets, meaning that we populate the proposer prompt with 3 problems for each difficulty class, and ask for B / 4 B/4 problems of each difficulty class as the output. We justify the choice of uniform input/targets in Appendix B , and vary the number of iterations T T and proposer budget B B in our analysis (§ 6 ).

## 5 Results

We investigate PSV-Verus ’s performance on our two experimental settings: transfer learning and test-time training . Table 1 presents our main results on three benchmarks: Dafny2Verus, MBPP-Verified, and HumanEval-Verified. PSV-Verus consistently outperforms both the AlphaVerus and the RFT baselines across all metrics.

#### Transfer learning

PSV-Verus achieves strong cross-domain generalization, scoring 25.25% pass@1 on MBPP and 16.18% on HumanEval, outperforming AlphaVerus (6.48%, 7.24%) and RFT (10.99%, 10.99%) by 3.90 × \times and 2.30 × \times on MBPP and 2.24 × \times and 1.47 × \times on HumanEval, respectively. These results demonstrate that training on Dafny2Verus generalizes robustly across domains, yielding substantial gains on realistic natural-language programming benchmarks.

#### Test-time training

On Dafny2Verus pass@1, PSV-Verus achieves 65.63%, compared to AlphaVerus’s 24.06% (a 2.73 × \times improvement) and RFT’s 34.46% (a 1.90 × \times improvement). On MBPP pass@1, PSV-Verus reaches 36.78%, outperforming AlphaVerus’s 6.48% (5.68 × \times ) and RFT’s 3.83% (9.61 × \times ), and on HumanEval pass@1, PSV-Verus achieves 19.07%, compared to AlphaVerus’s 7.24% (2.63 × \times ) and RFT’s 5.56% (3.43 × \times ). On Dafny2Verus pass@10, PSV-Verus outperforms RFT by 1.26 × \times and AlphaVerus by 1.26 × \times . Averaged across all benchmarks and metrics, PSV-Verus obtains 48.12%, compared to 25.43% for RFT and 25.55% for AlphaVerus, representing mean improvements of 1.89 × \times and 1.88 × \times , respectively. Performance graphs for each task are in Figure 4 , where the trends of improving over iterations become clear.

## 6 Analyses and Ablations

In the sections that follow, we investigate how our method scales with the number of generated questions (§ 6.1 ) and iterations of the algorithm when the number of proposed questions is held constant (§ 6.2 ) – experiments that articulate the scaling properties of our method with respect to increasing compute. We also analyze the importance of formal verification and factors impacting the effectiveness of the question proposal through ablation experiments in § 6.3 to better understand their impact on self-play performance.

### 6.1 Scaling with Questions Per Iteration

The first scaling factor we consider is the number of questions per iteration B B , because it can be scaled in parallel across many machines simultaneously without any blocking factors. Results for the test-time training setting are shown in Figure 5 .

On Dafny2Verus, scaling from 4k to 32k questions per iteration yields consistent improvements: pass@1 increases from 59.5% to 74.3% ( +25% relative ), pass@5 from 73.8% to 82.6% ( +12% ), and pass@10 from 75.8% to 83.6% ( +10% ). On MBPP, scaling from 1k to 32k questions yields pass@1 improvements from 22.3% to 44.3% ( +98% ), pass@5 from 39.7% to 57.8% ( +46% ), and pass@10 from 44.8% to 61.1% ( +36% ). HumanEval shows similar gains: pass@1 from 13.9% to 26.3% ( +89% ), pass@5 from 16.4% to 32.6% ( +99% ), and pass@10 from 17.9% to 34.5% ( +93% ). We also observe positive scaling behavior for transferring from Dafny2Verus to MBPP, though more modest gains for transferring to HumanEval; see Appendix C .

### 6.2 Iterative Training

Next, we are interested in whether the proposer’s budget of generated specifications (i.e., the question budget) should be allocated towards increasing the number of iterations of the method or increasing the number of generated specifications per iteration. We fix the question budget and vary the number of iterations. Figure 6 illustrates a smooth, monotonic improvement as the number of iterations increase. That is, distributing a fixed question budget across multiple of iterations proposing, solving, and updating yields better results than a single large iteration. For example, in the test-time-training setting on Dafny2Verus at a 1k budget, increasing iterations from 1 to 5 boosts pass@1 from 21.0% to 42.3% ( +102% ). The pattern holds at higher budgets: at 2k, pass@1 rises from 26.3% to 44.3% ( +68% ); at 4k, from 28.0% to 46.9% ( +68% ). This effect extends beyond pass@1: at the 4k budget level, pass@5 improves from 50.6% to 62.9% ( +24% ), and pass@10 improves from 60.0% to 66.7% ( +11% ). In summary, holding the number of proposed specifications constant, increasing the number of iterations boosts success rates, showing that iterative training drives performance improvements in our method.

### 6.3 Ablations

Our self-play algorithm PSV-Verus has three key components worth examining through ablation analyses – a verifier that determines whether specs and solutions are correct, and a proposer that outputs diverse solutions by sampling questions to put in the proposer prompt from the ever-growing dataset and that outputs questions of target difficulty by computing and including labels of how difficult questions included in the prompt were for the most recent solver. We decided to ablate each of these components and observe their effect on performance in the transfer learning setting. Our results are in Table 2 and described below in detail.

#### Verification

The Verus verifier is used primarily in our algorithm to check whether solutions are valid for a given spec before training on them. We analyze the impact of this by ablating this step and training on all generated solutions, ignoring the verification signal. Our results are shown in Table 2 under (-Verification). We find that removing solution verification hurts performance significantly, leading to relative drops in performance of 51.5% pass@1 and 29.3% pass@5 for Dafny2Verus, 55.2% and 35.7% for MBPP, and 52.1% and 33.5% for HumanEval.

In addition to performance gains, we also find that verification can be useful for efficiency. We also use verification to filter out candidate specs to make sure they are syntactically compilable before attempting inference on them. This impacts efficiency only, not performance, because the syntactically invalid specs are 100% not solvable, therefore no solution can impact training. We ablated this step and found that the efficiency hit from removing spec verification is substantial: only 47.7% of unique specs were valid on average, so removing spec verification meant that we had to perform pass@10 inference on the remaining 52.3% of specs that were not solvable, a 2.1x increase in inference compute with no resulting performance improvement.

#### Difficulty-awareness

We experiment with removing the difficulty awareness of our proposer by removing the labels for the sampled questions in the proposer prompt. The prompt form is detailed in Appendix G . We found that this -Difficulty ablation causes an average drop of 5.6% across all metrics. Table 2 shows per-dataset comparisons: the drop is statistically significant for 6 of 9 dataset/metric combinations (paired t-test, p < 0.05 p<0.05 ). Notably, all three Dafny2Verus metrics show significant drops, while some HumanEval and MBPP comparisons do not reach significance (MBPP pass@1, HumanEval pass@5,10).

To understand why, we analyze whether the proposer successfully generates questions at the target difficulty. For PSV-Verus , easy-targeted questions have mean pass rate 0.55 0.55 (std 0.47 0.47 ), medium-targeted questions have mean 0.45 0.45 (std 0.42 0.42 ), and hard-targeted questions have mean 0.36 0.36 (std 0.39 0.39 ). The different means but substantial overlap between distributions indicates that difficulty prompting provides partial but incomplete control over generated question difficulty. It seems that difficulty-aware prompting provides a modest benefit despite its imperfect control over generated question difficulty – an area that future work may find fruitful to improve upon.

#### Diversity

We experiment with limiting the diversity of the generated questions by ablating the constantly refreshing proposer prompt with a fixed proposer prompt. We construct this by sampling only once from the seed dataset to get our in-context examples, similar to the fixed prompt in self-instruct pipelines such as Rozière et al. (2023) . This ablation causes an average drop of 10.6% across all metrics. Table 2 show the full results: all Dafny2Verus and MBPP metrics show significant drops (pass@1 drops of 16.3% and 19.7% respectively), while HumanEval pass@5 and pass@10 are lower but do not reach significance.

The mechanism behind this improvement is increased sample diversity: PSV-Verus achieves a higher uniqueness rate on average (45.3% vs 29.3%), which leads to 2.48 × \times more unique questions, and 2.26 × \times more solvable questions used for training the solver, enabling the model to learn from a broader distribution of verified solutions.

## 7 Conclusion

This work set out to investigate a central obstacle to proposer-solver self-play algorithms for language models: obtaining a reliable reward signal that prevents error propagation and reward hacking. While prior self-play successes have largely been confined to domains with trivial or limited-applicability verifiers, we showed that formal verification in a Turing-complete coding language enables self-play in a realistic code-generation setting by providing a sound, non-exploitable training signal. By introducing PSV and applying it successfully to verified Rust programming, we demonstrated that a model can autonomously expand its training curriculum beyond human-written data and steadily improve its capabilities without human supervision. We show that our algorithm displays smooth scaling behavior with respect to the number of generated questions (§ 6.1 ) and iterations (§ 6.2 ), making it an exciting first step in understanding the limits of scaling for self-play reasoning training. In analyzing key components of our algorithm’s design, we observe the importance of formal verification and difficulty-aware and diverse question proposal (§ 6.3 ) in making self-play performant.

## Acknowledgments

This work was also supported in part by the National Science Foundation under Grant Nos. DMS-2434614 and DMS2502281, the Future Enterprise Security initiative at Carnegie Mellon CyLab (FutureEnterprise@CyLab), and AFRL and DARPA under Agreement FA8750-24-9-1000, and by gifts from Amazon, Convergent Research, Microsoft, VMware, and the Beneficial AI Foundation.

## Impact Statement

We believe this work could help usher in a future of self-improving models through self-play. This comes with ethical concerns, but so too does it have the potential to enable a more equitable future where reasoning can emerge in many domains—more dependent on the properties of the generation-verification gap in that domain than on the capability to collect costly human reasoning traces (a capability usually only the highly resourced possess).

## References

Aggarwal et al. (2024) P. Aggarwal, B. Parno, and S. Welleck AlphaVerus: Bootstrapping Formally Verified Code Generation through Self-Improving Translation and Treefinement . ( en ). External Links: Link Cited by: Appendix C , Figure 1 , Figure 1 , item 2 , §1 , §2 , §3.1 , §4 , §4 .

Austin et al. (2021) J. Austin, A. Odena, M. Nye, M. Bosma, H. Michalewski, D. Dohan, E. Jiang, C. Cai, M. Terry, Q. Le, and C. Sutton Program synthesis with large language models . External Links: 2108.07732 , Link Cited by: §4 .

Baker et al. (2025) B. Baker, J. Huizinga, L. Gao, Z. Dou, M. Y. Guan, A. Madry, W. Zaremba, J. Pachocki, and D. Farhi Monitoring reasoning models for misbehavior and the risks of promoting obfuscation . External Links: 2503.11926 , Link Cited by: Figure 2 , Figure 2 , §1 , §2 .

Chen et al. (2021) M. Chen, J. Tworek, H. Jun, Q. Yuan, H. P. d. O. Pinto, J. Kaplan, H. Edwards, Y. Burda, N. Joseph, G. Brockman, A. Ray, R. Puri, G. Krueger, M. Petrov, H. Khlaaf, G. Sastry, P. Mishkin, B. Chan, S. Gray, N. Ryder, M. Pavlov, A. Power, L. Kaiser, M. Bavarian, C. Winter, P. Tillet, F. P. Such, D. Cummings, M. Plappert, F. Chantzis, E. Barnes, A. Herbert-Voss, W. H. Guss, A. Nichol, A. Paino, N. Tezak, J. Tang, I. Babuschkin, S. Balaji, S. Jain, W. Saunders, C. Hesse, A. N. Carr, J. Leike, J. Achiam, V. Misra, E. Morikawa, A. Radford, M. Knight, M. Brundage, M. Murati, K. Mayer, P. Welinder, B. McGrew, D. Amodei, S. McCandlish, I. Sutskever, and W. Zaremba Evaluating Large Language Models Trained on Code . arXiv . Note: arXiv:2107.03374 [cs]Comment: corrected typos, added references, added authors, added acknowledgements External Links: Link , Document Cited by: §4 .

Cheng et al. (2025a) J. Cheng, X. Liu, C. Wang, X. Gu, Y. Lu, D. Zhang, Y. Dong, J. Tang, H. Wang, and M. Huang SPaR: self-play with tree-search refinement to improve instruction-following in large language models . External Links: 2412.11605 , Link Cited by: §2 .

Cheng et al. (2025b) P. Cheng, T. Hu, H. Xu, Z. Zhang, Z. Yuan, Y. Dai, L. Han, N. Du, and X. Li Self-playing adversarial language game enhances llm reasoning . External Links: 2404.10642 , Link Cited by: §2 .

Contributors (2024) T. H. Contributors HumanEval-verus: hand-written examples of verified verus code derived from humaneval . Note: https://github.com/secure-foundations/human-eval-verus.git Cited by: §4 .

DeepSeek-AI et al. (2025) DeepSeek-AI, D. Guo, D. Yang, H. Zhang, J. Song, R. Zhang, R. Xu, Q. Zhu, S. Ma, P. Wang, X. Bi, X. Zhang, X. Yu, Y. Wu, Z. F. Wu, Z. Gou, Z. Shao, Z. Li, Z. Gao, A. Liu, B. Xue, B. Wang, B. Wu, B. Feng, C. Lu, C. Zhao, C. Deng, C. Zhang, C. Ruan, D. Dai, D. Chen, D. Ji, E. Li, F. Lin, F. Dai, F. Luo, G. Hao, G. Chen, G. Li, H. Zhang, H. Bao, H. Xu, H. Wang, H. Ding, H. Xin, H. Gao, H. Qu, H. Li, J. Guo, J. Li, J. Wang, J. Chen, J. Yuan, J. Qiu, J. Li, J. L. Cai, J. Ni, J. Liang, J. Chen, K. Dong, K. Hu, K. Gao, K. Guan, K. Huang, K. Yu, L. Wang, L. Zhang, L. Zhao, L. Wang, L. Zhang, L. Xu, L. Xia, M. Zhang, M. Zhang, M. Tang, M. Li, M. Wang, M. Li, N. Tian, P. Huang, P. Zhang, Q. Wang, Q. Chen, Q. Du, R. Ge, R. Zhang, R. Pan, R. Wang, R. J. Chen, R. L. Jin, R. Chen, S. Lu, S. Zhou, S. Chen, S. Ye, S. Wang, S. Yu, S. Zhou, S. Pan, S. S. Li, S. Zhou, S. Wu, S. Ye, T. Yun, T. Pei, T. Sun, T. Wang, W. Zeng, W. Zhao, W. Liu, W. Liang, W. Gao, W. Yu, W. Zhang, W. L. Xiao, W. An, X. Liu, X. Wang, X. Chen, X. Nie, X. Cheng, X. Liu, X. Xie, X. Liu, X. Yang, X. Li, X. Su, X. Lin, X. Q. Li, X. Jin, X. Shen, X. Chen, X. Sun, X. Wang, X. Song, X. Zhou, X. Wang, X. Shan, Y. K. Li, Y. Q. Wang, Y. X. Wei, Y. Zhang, Y. Xu, Y. Li, Y. Zhao, Y. Sun, Y. Wang, Y. Yu, Y. Zhang, Y. Shi, Y. Xiong, Y. He, Y. Piao, Y. Wang, Y. Tan, Y. Ma, Y. Liu, Y. Guo, Y. Ou, Y. Wang, Y. Gong, Y. Zou, Y. He, Y. Xiong, Y. Luo, Y. You, Y. Liu, Y. Zhou, Y. X. Zhu, Y. Xu, Y. Huang, Y. Li, Y. Zheng, Y. Zhu, Y. Ma, Y. Tang, Y. Zha, Y. Yan, Z. Z. Ren, Z. Ren, Z. Sha, Z. Fu, Z. Xu, Z. Xie, Z. Zhang, Z. Hao, Z. Ma, Z. Yan, Z. Wu, Z. Gu, Z. Zhu, Z. Liu, Z. Li, Z. Xie, Z. Song, Z. Pan, Z. Huang, Z. Xu, Z. Zhang, and Z. Zhang DeepSeek-R1: Incentivizing Reasoning Capability in LLMs via Reinforcement Learning . arXiv . Note: arXiv:2501.12948 [cs] External Links: Link , Document Cited by: §2 .

Dong et al. (2025) G. Dong, K. Lu, C. Li, T. Xia, B. Yu, C. Zhou, and J. Zhou Self-play with execution feedback: improving instruction-following capabilities of large language models . In The Thirteenth International Conference on Learning Representations , External Links: Link Cited by: §1 .

Dong and Ma (2025) K. Dong and T. Ma STP: Self-play LLM Theorem Provers with Iterative Conjecturing and Proving . ( en ). External Links: Link Cited by: §1 , §1 , §2 , §4 .

Haluptzok et al. (2023) P. Haluptzok, M. Bowers, and A. T. Kalai Language models can teach themselves to program better . In The Eleventh International Conference on Learning Representations , External Links: Link Cited by: §1 , §1 , §2 .

Huang et al. (2025) C. Huang, W. Yu, X. Wang, H. Zhang, Z. Li, R. Li, J. Huang, H. Mi, and D. Yu R-Zero: Self-Evolving Reasoning LLM from Zero Data . arXiv . Note: arXiv:2508.05004 [cs] External Links: Link , Document Cited by: §2 .

Klein et al. (2014) G. Klein, J. Andronick, K. Elphinstone, T. Murray, T. Sewell, R. Kolanski, and G. Heiser Comprehensive formal verification of an OS microkernel . ACM Trans. Comput. Syst. 32 ( 1 ), pp. 2:1–2:70 . Note: hey External Links: ISSN 0734-2071 , Link , Document Cited by: §2 .

Kuba et al. (2025) J. G. Kuba, M. Gu, Q. Ma, Y. Tian, and V. Mohan Language Self-Play For Data-Free Training . arXiv . Note: arXiv:2509.07414 [cs] External Links: Link , Document Cited by: §2 .

Lattuada et al. (2023) A. Lattuada, T. Hance, C. Cho, M. Brun, I. Subasinghe, Y. Zhou, J. Howell, B. Parno, and C. Hawblitzel Verus: verifying rust programs using linear ghost types . Proceedings of the ACM on Programming Languages 7 ( OOPSLA1 ), pp. 286–315 . Cited by: Appendix F , §1 , §2 , §2 , §3 , §4 , §4 .

Leino (2010) K. R. M. Leino Dafny: an automatic program verifier for functional correctness . In Proceedings of the Conference on Logic for Programming, Artificial Intelligence, and Reasoning (LPAR) , Cited by: §3 .

Li et al. (2024) Q. Li, J. Gao, S. Wang, R. Pi, X. Zhao, C. Wu, X. Jiang, Z. Li, and L. Kong Forewarned is Forearmed: Leveraging LLMs for Data Synthesis through Failure-Inducing Exploration . ( en ). External Links: Link Cited by: §2 .

Lin et al. (2025) Z. Lin, S. Shen, J. Shang, J. E. Weston, and Y. Nie Learning to solve and verify: a self-play framework for mutually improving code and test generation . In NeurIPS 2025 Fourth Workshop on Deep Learning for Code , External Links: Link Cited by: §1 , §2 .

Liu et al. (2023) J. Liu, C. S. Xia, Y. Wang, and L. Zhang Is your code generated by chatgpt really correct? rigorous evaluation of large language models for code generation . External Links: 2305.01210 , Link Cited by: Appendix F , §1 .

Liu et al. (2025) Y. Liu, L. L. Zhang, Y. Zhu, B. Dong, X. Zhou, N. Shang, F. Yang, and M. Yang rStar-Coder: Scaling Competitive Code Reasoning with a Large-Scale Verified Dataset . arXiv . Note: arXiv:2505.21297 [cs] External Links: Link , Document Cited by: §2 .

Luo et al. (2023) Z. Luo, C. Xu, P. Zhao, Q. Sun, X. Geng, W. Hu, C. Tao, J. Ma, Q. Lin, and D. Jiang WizardCoder: Empowering Code Large Language Models with Evol-Instruct . ( en ). External Links: Link Cited by: Appendix B .

Misu et al. (2024) M. R. H. Misu, C. V. Lopes, I. Ma, and J. Noble Towards ai-assisted synthesis of verified dafny methods . Proc. ACM Softw. Eng. 1 ( FSE ). External Links: Link , Document Cited by: §4 .

Rice (1953) H. G. Rice Classes of recursively enumerable sets and their decision problems . Transactions of the American Mathematical Society 74 ( 2 ), pp. 358–366 . External Links: Document Cited by: Appendix F .

Rozière et al. (2023) B. Rozière, J. Gehring, F. Gloeckle, S. Sootla, I. Gat, X. E. Tan, Y. Adi, J. Liu, R. Sauvestre, T. Remez, J. Rapin, A. Kozhevnikov, I. Evtimov, J. Bitton, M. Bhatt, C. C. Ferrer, A. Grattafiori, W. Xiong, A. Défossez, J. Copet, F. Azhar, H. Touvron, L. Martin, N. Usunier, T. Scialom, and G. Synnaeve Code Llama: Open Foundation Models for Code . ( en ). External Links: Link Cited by: §2 , §6.3 .

Saad-Falcon et al. (2025) J. Saad-Falcon, E. K. Buchanan, M. F. Chen, T. Huang, B. McLaughlin, T. Bhathal, S. Zhu, B. Athiwaratkun, F. Sala, S. Linderman, et al. Shrinking the generation-verification gap with weak verifiers . arXiv preprint arXiv:2506.18203 . Cited by: §2 .

Shah et al. (2024) V. Shah, D. Yu, K. Lyu, S. Park, J. Yu, Y. He, N. R. Ke, M. Mozer, Y. Bengio, S. Arora, and A. Goyal AI-Assisted Generation of Difficult Math Questions . ( en ). External Links: Link Cited by: §2 .

Shao et al. (2024) Z. Shao, P. Wang, Q. Zhu, R. Xu, J. Song, X. Bi, H. Zhang, M. Zhang, Y. K. Li, Y. Wu, and D. Guo DeepSeekMath: Pushing the Limits of Mathematical Reasoning in Open Language Models . arXiv . Note: arXiv:2402.03300 [cs] External Links: Link , Document Cited by: §2 , §3.1 .

Silver et al. (2017) D. Silver, T. Hubert, J. Schrittwieser, I. Antonoglou, M. Lai, A. Guez, M. Lanctot, L. Sifre, D. Kumaran, T. Graepel, T. Lillicrap, K. Simonyan, and D. Hassabis Mastering Chess and Shogi by Self-Play with a General Reinforcement Learning Algorithm . arXiv . Note: arXiv:1712.01815 [cs] External Links: Link , Document Cited by: §1 , §2 .

Singh et al. (2024) A. Singh, J. D. Co-Reyes, R. Agarwal, A. Anand, P. Patil, X. Garcia, P. J. Liu, J. Harrison, J. Lee, K. Xu, A. Parisi, A. Kumar, A. Alemi, A. Rizkowsky, A. Nova, B. Adlam, B. Bohnet, G. Elsayed, H. Sedghi, I. Mordatch, I. Simpson, I. Gur, J. Snoek, J. Pennington, J. Hron, K. Kenealy, K. Swersky, K. Mahajan, L. Culp, L. Xiao, M. L. Bileschi, N. Constant, R. Novak, R. Liu, T. Warkentin, Y. Qian, Y. Bansal, E. Dyer, B. Neyshabur, J. Sohl-Dickstein, and N. Fiedel Beyond Human Data: Scaling Self-Training for Problem-Solving with Language Models . arXiv . Note: arXiv:2312.06585 [cs]Comment: Accepted to TMLR. Camera-ready version. First three authors contributed equally External Links: Link , Document Cited by: item 2 , §2 , §3.1 , §3.1 , §4 .

Song et al. (2024) Y. Song, H. Zhang, C. Eisenach, S. Kakade, D. Foster, and U. Ghai Mind the Gap: Examining the Self-Improvement Capabilities of Large Language Models . ( en ). External Links: Link Cited by: §2 .

Sukhbaatar et al. (2018) S. Sukhbaatar, Z. Lin, I. Kostrikov, G. Synnaeve, A. Szlam, and R. Fergus Intrinsic motivation and automatic curricula via asymmetric self-play . In International Conference on Learning Representations , External Links: Link Cited by: §1 .

Sun et al. (2020) Y. Sun, X. Wang, Z. Liu, J. Miller, A. Efros, and M. Hardt Test-Time Training with Self-Supervision for Generalization under Distribution Shifts . In Proceedings of the 37th International Conference on Machine Learning , pp. 9229–9248 ( en ). Note: ISSN: 2640-3498 External Links: Link Cited by: §4 .

Wei et al. (2024) Y. Wei, F. Cassano, J. Liu, Y. Ding, N. Jain, Z. Mueller, H. de Vries, L. von Werra, A. Guha, and L. Zhang SelfCodeAlign: Self-Alignment for Code Generation . ( en ). External Links: Link Cited by: §2 .

Wen et al. (2025) X. Wen, Z. Liu, S. Zheng, S. Ye, Z. Wu, Y. Wang, Z. Xu, X. Liang, J. Li, Z. Miao, J. Bian, and M. Yang Reinforcement Learning with Verifiable Rewards Implicitly Incentivizes Correct Reasoning in Base LLMs . arXiv . Note: arXiv:2506.14245 [cs]Comment: Update with more experiments External Links: Link , Document Cited by: §2 .

Xin and Reiss (2017) Q. Xin and S. P. Reiss Identifying test-suite-overfitted patches through test case generation . In Proceedings of the 26th ACM SIGSOFT International Symposium on Software Testing and Analysis , ISSTA 2017 , New York, NY, USA , pp. 226–236 . External Links: ISBN 9781450350761 , Link , Document Cited by: §1 .

Yang et al. (2025a) C. Yang, X. Li, M. R. H. Misu, J. Yao, W. Cui, Y. Gong, C. Hawblitzel, S. Lahiri, J. R. Lorch, S. Lu, F. Yang, Z. Zhou, and S. Lu AutoVerus: Automated Proof Generation for Rust Code . Artifact of ”AutoVerus: Automated Proof Generation for Rust Code” 9 ( OOPSLA2 ), pp. 396:3454–396:3482 . External Links: Link , Document Cited by: §1 , §2 , §4 .

Yang et al. (2025b) Z. Yang, Z. Kuang, X. Xia, and Y. Zhao Can LLMs Generate High-Quality Test Cases for Algorithm Problems? TestCase-Eval: A Systematic Evaluation of Fault Coverage and Exposure . ( en ). External Links: Link Cited by: Figure 2 , Figure 2 .

Yuan et al. (2023) Z. Yuan, H. Yuan, C. Li, G. Dong, K. Lu, C. Tan, C. Zhou, and J. Zhou Scaling relationship on learning mathematical reasoning with large language models . External Links: 2308.01825 , Link Cited by: §4 .

Yuan et al. (2024) Z. Yuan, Y. Lou, M. Liu, S. Ding, K. Wang, Y. Chen, and X. Peng No more manual tests? evaluating and improving chatgpt for unit test generation . External Links: 2305.04207 , Link Cited by: §1 .

Zelikman et al. (2022) E. Zelikman, Y. Wu, J. Mu, and N. D. Goodman STaR: Bootstrapping Reasoning With Reasoning . ( en ). Note: hi benji External Links: Link Cited by: §2 .

Zhao et al. (2025) A. Zhao, Y. Wu, Y. Yue, T. Wu, Q. Xu, Y. Yue, M. Lin, S. Wang, Q. Wu, Z. Zheng, and G. Huang Absolute Zero: Reinforced Self-play Reasoning with Zero Data . arXiv . Note: arXiv:2505.03335 [cs] External Links: Link , Document Cited by: §1 , §1 , §2 .

Zheng et al. (2024) L. Zheng, L. Yin, Z. Xie, C. Sun, J. Huang, C. H. Yu, S. Cao, C. Kozyrakis, I. Stoica, J. E. Gonzalez, C. Barrett, and Y. Sheng SGLang: efficient execution of structured language model programs . External Links: 2312.07104 , Link Cited by: §4 .

Zhou et al. (2025) Y. Zhou, S. Levine, J. Weston, X. Li, and S. Sukhbaatar Self-Challenging Language Model Agents . arXiv . Note: arXiv:2506.01716 [cs]Self-Challenging Agent (SCA) is a framework that lets an LLM generate its own training tasks and then solve them ￼ ￼. In SCA, the LLM first acts as a “challenger”, exploring an environment with tools (e.g. a code executor or web browser) to create a new task for itself ￼. Each task is defined in a Code-as-Task format containing: a natural language instruction, a verification function, a reference solution, and some typical failure cases – all specified in executable code ￼ ￼. This structured format ensures that generated tasks are feasible and automatically verifiable (the code can test whether a solution is correct) ￼. After proposing a task, the LLM switches to an “executor” role and tries to solve the task, using the verification function’s result as the reward signal for reinforcement learning ￼ ￼. Zhou et al. report that SCA training dramatically improved a LLaMA-3.1 8B model on complex multi-tool use benchmarks, more than doubling its success rate (from 12.0% to 23.5%) on unseen tasks without any human-written data ￼. In fact, SCA fine-tuning yielded over a two-fold gain on average success rate, even outperforming prior state-of-the-art self-improvement methods by a wide margin ￼. This highlights how verifiable task generation (via code-based tests) can enable an LLM to teach itself effectively with minimal noise. External Links: Link , Document Cited by: §2 .

Zhu et al. (2025) R. Zhu, Y. Wang, T. Jiang, J. Liang, and T. Wang Self-improving model steering . External Links: 2507.08967 , Link Cited by: §2 .

## Appendix A Full Proposer Prompt

## Appendix B Input & Target Proposal Settings

We investigated different input and target proposal settings – e.g., using all problem types as the input to the proposer, asking for Uniform problem types as output target, or perhaps asking for only one class of problems as output (e.g., Easy, Hard). We tested three alternatives to our method: All → \rightarrow Hard, Easy → \rightarrow Hard (motivated by Luo et al. (2023) ), and All → \rightarrow Easy. We found that our model’s setting worked the best (All input problem types → \rightarrow Uniform output targets). This may be partially explained by the ablation in § 6.3 , where we found that removing sampling of the inputs in the proposer hurt performance. Our results suggest that taking in as much of the seed dataset as possible (not limiting input problems to a specific difficulty type) and using that to generate as diverse a sampling of problems as possible is the best approach.

## Appendix C Transfer Learning Scaling Results

We also evaluate how PSV-Verus scales in the transfer learning setting, where we train on Dafny2Verus and evaluate on MBPP and HumanEval. On MBPP, scaling from 4k to 32k questions per iteration yields consistent improvements: pass@1 increases from 21.8% to 32.0% ( +47% ), pass@5 from 34.4% to 42.6% ( +24% ), and pass@10 from 37.3% to 44.5% ( +19% ). In contrast, HumanEval shows minimal scaling effects: pass@1 remains essentially flat (14.4% to 14.3%, -1% ), while pass@5 and pass@10 show marginal gains (+4% and +3%, respectively). This is supported by prior work ( Aggarwal et al., 2024 ) which found limited transfer between Dafny2Verus and HumanEval-Verified.

## Appendix D Spec Compilation

In Verus, specifications define the contract a function must satisfy—preconditions ( requires ) and postconditions ( ensures ). To test whether a specification is well-formed without requiring a correct implementation, we use the #[verifier::external_body] attribute. This tells Verus to trust the function signature and specification without verifying the implementation body.

### Example: Finding the Maximum Element

The external_body stub uses assume(false); arbitrary() to satisfy Verus’s type checker without a real implementation. This allows us to verify that the specification itself is syntactically valid and logically consistent, independent of any implementation.

The verified implementation includes loop invariants that mirror the postconditions, allowing Verus to prove the implementation satisfies the specification. The invariants maintain that: 1. All elements seen so far are ≤ \leq max

2. The current max value exists somewhere in the portion of the array already traversed

## Appendix E Supervised Fine-Tuning (SFT) Training Details

We perform all supervised fine-tuning (SFT) using the SFTTrainer implementation from the Hugging Face trl library. 2 2 2 https://huggingface.co/docs/trl/en/sft_trainer The training setup mirrors standard LoRA-based fine-tuning for decoder-only models, with lightweight adaptation for efficiency on a single GPU. All experiments are conducted using accelerate to scale to distributed configurations, though all runs reported in the main results with the Qwen2.5-3B-Coder model use a single NVIDIA A6000 GPU (no DDP).

Each run takes approximately 20 minutes at the final iteration of the main experiments (with the most sft data). Checkpoints are saved every 5 steps, retaining only the latest one to minimize storage.

#### Reproducibility.

All code for SFT training, including configuration files and launcher scripts, is available in the project repository for full reproducibility, and is run automatically as a subprocess during the main entrypoint script.

## Appendix F Verification Background

Denote a problem as x ∈ 𝒳 x\in\mathcal{X} , and its associated set of acceptable programs as Y x ⊆ 𝒴 Y_{x}\subseteq\mathcal{Y} . Here 𝒳 \mathcal{X} is a problem domain and 𝒴 \mathcal{Y} is the set of possible programs. Intuitively, the term acceptable corresponds to the notion of a “correct solution”.

Let Z x v ⊆ 𝒴 Z_{x}^{v}\subseteq\mathcal{Y} be the set of programs for which a binary verifier v v returns 1 for problem x x , i.e. Z x v = { y ∈ 𝒴 | v ⁡ ( x , y ) = 1 } . \displaystyle Z_{x}^{v}=\{y\in\mathcal{Y}\ |\ v(x,y)=1\}. (1) We say that program y y is verified according to v v when y ∈ Z x v y\in Z_{x}^{v} .

We refer to Z x v Z_{x}^{v} as an accepted set (for verifier v v , on problem x x ; we occasionally do not state these distinctions for brevity).

By soundness we mean that every program verified according to v v is an acceptable program: Z x v ⊆ Y x . \displaystyle Z_{x}^{v}\subseteq Y_{x}. (2) Namely, we say that verifier v v is sound for problem x x if the relationship above holds, and unsound for problem x x if the relationship above does not hold. We say that the verifier is sound if it is sound for all problems x ∈ 𝒳 x\in\mathcal{X} . We say that the verifier is unsound if it is unsound for at least one problem x ∈ 𝒳 x\in\mathcal{X} .

By completeness we mean that every acceptable program is verified according to v v : Y x ⊆ Z x v . \displaystyle Y_{x}\subseteq Z_{x}^{v}. (3)

We say that verifier v v is complete for problem x x if the relationship above holds, and incomplete if the relationship does not hold. We say that the verifier is complete if it is complete for all problems x ∈ 𝒳 x\in\mathcal{X} . We say that the verifier is incomplete if it is incomplete for at least one problem x ∈ 𝒳 x\in\mathcal{X} .

#### Test-case verification is unsound.

A test suite can be seen as a verifier v T v_{T} that returns 1 when a program passes all tests in the suite T T , and 0 otherwise. It induces a subset of programs that pass all tests in T T , Z x v T = { y ∈ 𝒴 | y ​ passes T } Z_{x}^{v_{T}}=\{y\in\mathcal{Y}\ |\ y\text{ passes T}\} .

When we say that test case verification is unsound, we mean that for some problem x x , there exists a program y y that passes the test cases but is not actually correct: ∃ x ∈ 𝒳 ​ s.t. ​ Z x v T ⊈ Y x . \displaystyle\exists x\in\mathcal{X}\text{ s.t. }Z_{x}^{v_{T}}\not\subseteq Y_{x}. (4)

It is easy to construct such an example. For instance, consider the problem of writing a program to check whether an input integer is prime, and a single test that checks if the program returns True for input 3. Then a program return n == 3 would pass the tests, but it is clearly not an acceptable program for the problem. In practice, unsoundness of test-case verification is widely observed in the context of LLM code generation and evaluation (e.g., ( Liu et al., 2023 ) ).

#### Formal verification is sound with respect to the specification.

In this setting, we take 𝒳 \mathcal{X} to be the set of specifications in a formal verification language such as Verus or Dafny. In our setting, x x is a specification (e.g., preconditions and postconditions), Y x Y_{x} is the set of programs that satisfy x x , and v F v_{F} is the Verus verification procedure. Verus is an SMT-based verifier: it translates a program and specification into verification conditions and discharges them with an SMT solver. When Verus verifies a program, the result is sound with respect to the specification, up to the trusted computing base ( Lattuada et al., 2023 ) : y ∈ Z x v F ⟹ y ∈ Y x . \displaystyle y\in Z_{x}^{v_{F}}\implies y\in Y_{x}. (5) That is, if v F ​ ( x , y ) = 1 v_{F}(x,y)=1 then y y satisfies the specification x x .

However, formal verification tools like Verus or Dafny are incomplete. This is fundamental: no (general-purpose) program analysis for Turing-complete languages can be both sound and complete ( Rice, 1953 ) . Hence, for a problem x x , it may be the case that Z x v F ⊂ Y x Z_{x}^{v_{F}}\subset Y_{x} (note the strict subset), meaning that there are acceptable programs that the verifier rejects. This fundamental incompleteness explains why proof annotations are needed; we can think of adding such annotations as converting a program p ∈ Y x ∖ Z x v F p\in Y_{x}\setminus Z_{x}^{v_{F}} into a program p ′ ∈ Z x v F p^{\prime}\in Z_{x}^{v_{F}} .

## Appendix G Difficulty Unaware Ablation

## Instructions for reporting errors

We are continuing to improve HTML versions of papers, and your feedback helps enhance accessibility and mobile support. To report errors in the HTML that will help us improve conversion and rendering, choose any of the methods listed below:

Click the "Report Issue" ( ) button, located in the page header.

Tip: You can select the relevant text first, to include it in your report.

Our team has already identified the following issues . We appreciate your time reviewing and reporting rendering errors we may not have found yet. Your efforts will help us improve the HTML versions for all readers, because disability should not be a barrier to accessing research. Thank you for your continued support in championing open access for all.

Have a free development cycle? Help support accessibility at arXiv! Our collaborators at LaTeXML maintain a list of packages that need conversion , and welcome developer contributions .
