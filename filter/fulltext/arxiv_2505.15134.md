##### Report GitHub Issue

Content selection saved. Describe the issue below:

# The Unreasonable Effectiveness of Entropy Minimization in LLM Reasoning

###### Abstract

Entropy minimization (EM) trains the model to concentrate even more probability mass on its most confident outputs. We show that this simple objective alone, without any labeled data, can substantially improve large language models’ (LLMs) performance on challenging math, physics, and coding tasks. We explore three approaches: (1) EM-FT minimizes token-level entropy similarly to instruction finetuning, but on unlabeled outputs drawn from the model; (2) EM-RL : reinforcement learning with negative entropy as the only reward to maximize; (3) EM-INF: inference-time logit adjustment to reduce entropy without any training data or parameter updates. On Qwen-7B, EM-RL , without any labeled data, achieves comparable or better performance than strong RL baselines such as GRPO [ 68 ] and RLOO [ 1 ] that are trained on 60K labeled examples. Furthermore, EM-INF enables Qwen-32B to match or exceed the performance of proprietary models like GPT-4o, Claude 3 Opus, and Gemini 1.5 Pro on the challenging SciCode benchmark [ 78 ] , while being 3x more efficient than self-consistency and sequential refinement. Our findings reveal that many pretrained LLMs possess previously underappreciated reasoning capabilities that can be effectively elicited through entropy minimization alone, without any labeled data or even any parameter updates. 1 1 1 Code: https://github.com/shivamag125/EM_PT

## 1 Introduction

Entropy minimization (EM) trains the model to concentrate even more probability mass on its most confident outputs without any labeled data or external supervision [ 23 , 60 , 25 ] . It operates on a key assumption and a simple intuition: if a model is reasonably capable, it is more likely to be correct when it is confident [ 56 ] . Modern large language models (LLMs) are pretrained on massive data and often undergo a dedicated annealing phase to enhance downstream task performance [ 59 , 3 , 92 , 77 ] . It should be, therefore, fairly reasonable to treat them as capable models even before any supervised finetuning (SFT) or reinforcement learning (RL) [ 90 ] . This naturally invites the questions: Can entropy minimization alone improve their performance? And how far can they go without any labeled data? This work answers both: yes, and surprisingly far, at least for reasoning tasks.

We present a systematic exploration of post-pretraining adaptation and inference-time scaling of LLMs, using entropy minimization alone without any labeled data. We propose three novel methods, each aligned with an established post-pretraining stage. (1) Unsupervised finetuning by directly minimizing token-level entropy ( EM-FT ) mirrors SFT and minimizes a token level loss, on unlabeled outputs sampled from the model conditioning on the input prompts [ 46 ] . We find that EM-FT achieves surprisingly strong performance on math and coding tasks, and can even outperform labeled GRPO and RLOO on LeetCode [ 26 ] (coding) and Minerva [ 42 ] (math).

(2) Reinforcement learning with a negative entropy reward ( EM-RL ) uses a reward signal based solely on entropy: the negative sum of token-level entropy across a rollout, adjusted by a constant baseline. This is analogous to the REINFORCE algorithm [ 76 , 1 ] but with entropy as the only supervision without any labeled data. We find that without any labeled data EM-RL can achieve competitive performance to RLOO and GRPO on most math and coding tasks while outperforming it on LeetCode, Minerva and AMC (math) [ 43 ] .

(3) Inference-time scaling through entropy minimization (EM-INF) optimizes the logits during each decoding step to reduce the entropy of the LLM’s distribution without any parameter update. We find that EM-INF works best in complex tasks with high uncertainty (e.g. AIME math [ 43 ] , UGPhysics [ 88 ] and SciCode [ 78 ] ). We observe that Qwen 32B [ 77 ] can outperform frontier models like GPT-4o on Scicode [ 78 ] and is 3x more efficient than inference scaling through self-consistency and sequential refinement.

While the results are promising, they must be interpreted with care (§ 5 ). First, EM is most effective when model confidence correlates with correctness, as in the experiments above. It is less suited for tasks like aligning with human values [ 35 ] , where confidence alone is not a reliable proxy for quality. Through experiments on individualistic value reasoning [ 35 ] , we observe that Qwen-2.5 struggles on the task without finetuning on labeled data, and further EM leads to no improvements. Second, the effectiveness of EM hinges on the assumption that the pretrained model is already capable in the tasks of interest. We observe that the improvements from EM-FT and EM-RL on Llama-3.1-8B are less substantial on math reasoning tasks compared to those on Qwen-2.5. This may be due to Llama-3.1-8B is less capable on these reasoning tasks.

The success and limitations of EM highlight the importance of the capabilities of the pretrained models, which is sometimes underappreciated, at least for reasoning tasks. We call for the inclusion of EM as a baseline in the evaluation of future post-pretraining and inference-time scaling algorithms, to better separate the contribution of algorithmic innovations from the intrinsic capabilities of the model itself. Besides, as we show, an approach that performs surprisingly well on certain models and tasks can fail in trivial ways on others. Broad evaluation across diverse pretrained models and tasks can help ensure that the conclusions generalize and are not artifacts of a specific model or dataset.

## 2 Background and Related Work

### 2.1 Related Work

Entropy-regularized RL augments the expected reward objective with a regularization term aiming to increase entropy [ 98 ] , in order to promote exploration by adding uncertainty into the actions [ 64 , 33 , 27 , 18 , 41 ] . Entropy-regularized RL usually learns a policy from scratch in grid world situations (e.g. robot simulations) where adding perturbations can lead to exploring various paths to get to the goal. In contrast, we investigate if reducing the uncertainty of the policy can improve a pre-trained language models capabilities, with the hypothesis that they already acquire some capabilities for the tasks of interest during pretraining. Instead of learning from scratch, we finetune LLMs to reinforce confident outputs. Therefore, we draw inspiration from entropy-regularization in RL to design reward function ( EM-RL ) that minimize the entropy of the model encouraging it to commit to a fewer more confident paths, instead of prompting exploration like in previous works.

Entropy minimization (EM) has been extensively used as regularization in semi-supervised learning [ 23 , 40 , 8 , 51 ] , domain adaptation [ 60 , 62 , 80 ] , and few-shot learning [ 25 , 39 ] . [ 38 , 20 ] apply EM for reinforcement learning with semi-supervised scenarios, where entropy is used to estimate the rewards on unlabeled data. [ 81 , 94 , 56 ] use EM for unsupervised test-time adaptation, where pre-trained classifiers are adapted to new data at test time without using any labels. Despite its well-studied history [ 53 , 52 , 48 , 15 , 61 , 71 ] , EM has rarely been explored as a standalone training objective for LLMs. Our key hypothesis is that EM can reinforce LLMs’ strong capabilities acquired during pretraining. Instead of applying entropy minimization for test time-domain adaptation or as a regularizer, we study if it can be used for LLM finetuning and inference time scaling.

Unsupervised and few-shot RL for LLMs has raised the possibility of self-improvement [ 85 , 5 , 54 ] . Here a model learns via self-training in which it critiques its own generations without external feedback [ 22 , 47 , 57 , 93 ] or refines generated text [ 11 , 96 , 70 ] . Building on self-improvement, self-verification [ 45 ] has been applied for RL tuning [ 95 , 84 , 99 ] , concurrently. [ 32 ] uses the most frequent answer as reward (majority voting) for finetuning, since optimizing the likelihood of most consistent answer can reinforce pretraining priors. [ 99 ] applies this idea to unsupervised RL tuning at test time by optimizing on test dataset as a whole. We work on the same intuition of reinforcing model confidence, however, we study post-training where EM-FT and EM-RL are used for finetuning LLMs on large general math and coding data. Further, consistent answers and output extraction is not always possible in complex tasks like scientific coding [ 2 , 10 , 82 , 4 , 73 ] . On the other hand, EM-FT and EM-RL can be applied on tasks like code generation where output extraction is non-trivial. Unlike [ 99 ] which updates the model parameters on each test set individually, inference scaling via EM-INF optimizes the models’ entropy without updating parameters and does not need task-specific optimization. EM-INF can be deployed and served like regular text decoding [ 30 , 58 , 19 ] requiring neither assumption on task nor model optimization. [ 95 ] proposes to estimate rewards by computing the frequency of extracted answers for a prompt. Here, the model is incentivized to prefer certain answers, which makes the answer distribution more concentrated. While it reduces the entropy, it is not directly enforced and emerges from learning to repeat most frequent solutions. EM-FT and EM-RL target uncertainty in models’ token level distribution, whereas the frequency-based approaches target alignment with desired outputs where entropy reduction is not an inherent outcome and task-dependent. [ 84 ] investigates RL from few-shot output verified labeled data and observe that direct entropy maximization as a standalone objective can be used for finetuning to a small extent. They find that carefully selecting a few output-verifiable problems along with entropy maximization as a regularizer can lead to improvements. We find that only negative entropy rewards (entropy minimization) are sufficient for RL with similar effects without requiring any data selection. Standalone entropy maximization does not converge and eventually collapses [ 84 ] , but EM-RL and EM-FT via EM converge and can be used to train on large datasets without output verification.

### 2.2 Preliminaries

Problem setup: Let π θ \pi_{\theta} denote an autoregressive LLM policy: π θ ​ ( 𝒚 | 𝒙 ) = ∏ i π θ ​ ( y i | 𝒙 , 𝒚 < i ) \pi_{\theta}({\bm{y}}|{\bm{x}})=\prod_{i}\pi_{\theta}(y_{i}|{\bm{x}},{\bm{y}}_{<i}) , where 𝒙 {\bm{x}} denotes the input prompt and 𝒚 = y 1 ​ … ​ y | 𝒚 | {\bm{y}}=y_{1}\dots y_{|{\bm{y}}|} the output trajectory. For clarity, we will suppress the conditioning on 𝒙 {\bm{x}} whenever it is clear from the context. Let r ⁡ ( 𝒚 ) r({\bm{y}}) denote a reward function, which provides a score for an output sequence. RL learns a policy that produces output sequence to maximize the expected reward 𝔼 y ∼ π θ ​ [ r ​ ( 𝒚 ) ] \mathbb{E}_{y\sim\pi_{\theta}}[r({\bm{y}})] .

Entropy minimization minimizes the Shannon entropy ℋ ⁡ ( π θ ) = − 𝔼 𝒚 ∼ π θ ​ [ log ⁡ π θ ​ ( 𝒚 ) ] \mathcal{H}(\pi_{\theta})=-\mathbb{E}_{{\bm{y}}\sim\pi_{\theta}}[\log\pi_{\theta}({\bm{y}})] [ 67 ] of the policy [ 23 ] . We consider two methods for empirically estimating the entropy.

Trajectory-level entropy estimator [ 79 , 17 ] is computed based on the trajectory distribution of the output sequences produced by the policy. In practice, it samples full sequences and computes the total log-probability. For an autoregressive policy, ℋ ^ traj ( π θ ) = − 1 N ∑ i = 1 N log π θ ( 𝒚 i ) = − 1 N ∑ i = 1 N ∑ t = 1 | 𝒚 i | log π θ ( y t i | 𝒚 < t i ) \displaystyle\hat{\mathcal{H}}_{\text{traj}}(\pi_{\theta})=-\frac{1}{N}\sum_{i=1}^{N}\log\pi_{\theta}\left({\bm{y}}^{i}\right)=-\frac{1}{N}\sum_{i=1}^{N}\sum_{t=1}^{|{\bm{y}}^{i}|}\log\pi_{\theta}(y_{t}^{i}|{\bm{y}}_{<t}^{i}) (1) { 𝒚 i ∼ π θ } i = 1 N \{{\bm{y}}^{i}\sim\pi_{\theta}\}_{i=1}^{N} are N N full trajectories sampled from the policy.

Token (action) level entropy estimator [ 27 , 18 ] computes the entropy of the policy based on the token (action) distribution at each step. In practice, it sums per-token entropy across time steps. At generation step t t , the model produces a probability distribution π θ ( ⋅ | 𝒚 < t ) \pi_{\theta}(\cdot|{\bm{y}}_{<t}) over a vocabulary 𝒱 \mathcal{V} . The entropy of the policy using token-level estimation is then ℋ ^ tok ( π θ ) = 1 N ∑ i = 1 N ∑ t = 1 | 𝒚 i | ℋ ( π θ ( ⋅ ∣ 𝒚 < t i ) ) \displaystyle\hat{\mathcal{H}}_{\text{tok}}(\pi_{\theta})=\frac{1}{N}\sum_{i=1}^{N}\sum_{t=1}^{|{\bm{y}}^{i}|}\mathcal{H}\big(\pi_{\theta}(\cdot\mid{\bm{y}}_{<t}^{i})\big) (2) where ℋ ( π θ ( ⋅ ∣ 𝒚 < t ) ) = − ∑ j ∈ 𝒱 π θ ( j ∣ 𝒚 < t ) log π θ ( j ∣ 𝒚 < t ) \mathcal{H}(\pi_{\theta}(\cdot\mid{\bm{y}}_{<t}))=-\sum_{j\in\mathcal{V}}\pi_{\theta}(j\mid{\bm{y}}_{<t})\log\pi_{\theta}(j\mid{\bm{y}}_{<t}) . While both trajectory-level and token-level estimators are used to compute entropy, they lead to different behaviors when used for training. Minimizing trajectory entropy leads to policies with lower entropy over trajectories whereas minimum token-level entropy leads to policies with low entropy at each generation step. Furthermore, the token-level estimate is commonly used in maximum entropy-regularized RL frameworks, such as soft actor-critic due to its low variance [ 14 , 27 , 64 , 41 ] .

In the following subsections, we introduce three post-training methods based on entropy minimization as a standalone objective. (1) EM-FT (§ 3.1 ): directly minimizes the token-level entropy (Eqn. 2 ) similar to supervused finetuning, but on unlabeled outputs drawn from the model; (2) EM-RL (§ 3.2 ): reinforcement learning with negative trajectory-level entropy (Eq. 1 ) or neagtive token level entropy (Eqn. 2 ) as the only reward to maximize; (3) EM-INF (§ 4 ): inference-time logit adjustment to reduce entropy using the token level estimate (Eqn. 2 ) without any training data or parameter updates.

## 3 Entropy Minimization for Post-training

### 3.1 EM-FT : Direct Entropy Minimization through Token-Level Finetuning

Supervised finetuning methods such as rejection sampling finetuning [ 16 , 91 , 46 ] sample data from the policy and use a reward function to select high-quality data. Good performance on these tasks has been attributed to post-training labels (e.g. output supervision) and pretraining task mixtures [ 65 , 89 ] . Building on entropy minimization and on-policy finetuning we test if directly minimizing the entropy of the sampled trajectories can enable learning without labels. Given a batch of N N sampled trajectories { 𝒚 ∼ π θ } i = 1 N \{{\bm{y}}\sim\pi_{\theta}\}_{i=1}^{N} , we directly minimize the the empirical total token-level entropy ℋ ^ tok \hat{\mathcal{H}}_{\text{tok}} (Eqn. 2 ). We present this objective and its corresponding gradient in Table 1 .

### 3.2 EM-RL : Entropy Minimization with Negative Entropy Rewards in RL

We now minimize the entropy of the policy by using negative entropy as the only reward in RL ( EM-RL ). We design a reward function to assign outcome rewards to trajectory 𝒚 {\bm{y}} based on: 1) negative trajectory level entropy ( EM-RL -sequence); 2) negative token level entropy ( EM-RL -token).

EM-RL -sequence minimizes the entropy based on the trajectory level estimator of entropy (Eqn. 1 ). This estimate favors trajectories that receive high probabilities but does not care about if the reasoning paths are concentrated or not to a few options. Minimizing this entropy estimate is useful in situations where multiple but limited chain of thoughts are preferred, for example, shorter math tasks where some plausible solutions can be explored but not too many. We use the joint probability of the sequence as a reward r traj r_{\text{traj}} to minimize the trajectory level entropy estimate in expectation, 𝔼 𝒚 ∼ π θ ] [ r traj ( 𝒚 ) ] = − ℋ ^ traj ( π θ ) \mathbb{E}_{{\bm{y}}\sim\pi_{\theta}]}[r_{\text{traj}}({\bm{y}})]=-\hat{\mathcal{H}}_{\text{traj}}(\pi_{\theta}) . The reward r traj r_{\text{traj}} is, r traj ​ ( 𝒚 ) = ∑ t = 1 | 𝒚 | log ⁡ π θ ​ ( y t | y < t ) = log ⁡ π θ ​ ( 𝒚 ) r_{\text{traj}}({\bm{y}})=\sum_{t=1}^{|{\bm{y}}|}\log\pi_{\theta}(y_{t}|y_{<t})=\log\pi_{\theta}({\bm{y}}) (3)

EM-RL -token minimizes the entropy based on the token level entropy estimate. This estimate prefers trajectories that are more deterministic and confident at each generation step, focusing the probability mass on fewer possible reasoning paths (chain of thoughts). For example, problems requiring complex long chain of thoughts where being more deterministic at every step prevents the model getting lost in the sauce. Based on the token level entropy estimate (Eqn 2 ), we define the reward r tok r_{\text{tok}} to minimize the token level entropy estimate in expectation, 𝔼 𝒚 ∼ π θ ​ [ r tok ​ ( 𝒚 ) ] = − ℋ ^ tok ​ ( π θ ) \mathbb{E}_{{\bm{y}}\sim\pi_{\theta}}[r_{\text{tok}}({\bm{y}})]\!=\!-\hat{\mathcal{H}}_{\text{tok}}(\pi_{\theta}) , r tok ( 𝒚 ) = − ∑ t = 1 | 𝒚 | ℋ ( π θ ( ⋅ ∣ y < t ) ) r_{\text{tok}}({\bm{y}})=-\sum_{t=1}^{|{\bm{y}}|}\mathcal{H}\big(\pi_{\theta}\left(\cdot\mid y_{<t}\right)\big) (4) While both the objectives EM-FT , EM-RL aim to minimize the entropy of the policy, they are optimized differently. EM-FT minimizes the entropy by directly differentiating it, whereas EM-RL uses policy gradients [ 64 , 1 ] . Table 1 summarizes the objectives and the corresponding gradients. In practice, we subtract the RLOO baseline [ 1 ] in EM-RL , which does not change the expectation of the gradients but helps with optimization [ 75 , 49 , 87 ] . In addition, we use a KL-regularizer weighted by β \beta between the policy π θ \pi_{\theta} and the initial base model π ref \pi_{\text{ref}} to avoid large deviations from the base model and aid optimization, i.e., − ℋ ( π θ ) − β KL [ π θ | | π ref ] = − ℋ ( π θ ) − β ( − ℋ ( π θ ) − ℋ ( π θ , π ref ) ) -\mathcal{H}(\pi_{\theta})-\beta\text{KL}[\pi_{\theta}||\pi_{\text{ref}}]=-\mathcal{H}(\pi_{\theta})-\beta(-\mathcal{H}(\pi_{\theta})-\mathcal{H}(\pi_{\theta},\pi_{\text{ref}})) [ 64 , 74 ] . The KL regularization can increase the entropy when the base model is too uncertain (higher entropy), however when β < 1 \beta<1 (we use 0.001 0.001 ) the dominant gradient is from the reward, in our case entropy minimization.

Objectives Gradients wrt. θ \theta Finetuning EM-FT § 3.1 Min. ℋ ^ tok \hat{\mathcal{H}}_{\text{tok}} 1 N ∑ i = 1 N ∑ t = 1 | y i | ∇ θ ℋ ( π θ ( ⋅ ∣ 𝒚 < t i ) ) \frac{1}{N}\sum_{i=1}^{N}\sum_{t=1}^{|y^{i}|}\nabla_{\theta}\mathcal{H}\left(\pi_{\theta}(\cdot\mid{\bm{y}}_{<t}^{i})\right) RL EM-RL-sequence § 3.2 Max. − ℋ ^ traj -\hat{\mathcal{H}}_{\text{traj}} 1 N ∑ i = 1 N [ ∑ t = 1 | y i | log π θ ( y t i ∣ 𝒚 < t i ) ∇ θ log π θ ( 𝒚 i ) ) ] \frac{1}{N}\sum_{i=1}^{N}\Big[\sum_{t=1}^{|y^{i}|}\log\pi_{\theta}(y_{t}^{i}\mid{\bm{y}}_{<t}^{i})\nabla_{\theta}\log\pi_{\theta}({\bm{y}}^{i}))\Big] RL EM-RL-token § 3.2 Max. − ℋ ^ tok -\hat{\mathcal{H}}_{\text{tok}} 1 N ∑ i = 1 N [ − ∑ t = 1 | y i | ℋ ( π θ ( ⋅ ∣ 𝒚 < t i ) ∇ θ log π θ ( 𝒚 i ) ) ] \frac{1}{N}\sum_{i=1}^{N}\Big[-\sum_{t=1}^{|y^{i}|}\mathcal{H}(\pi_{\theta}(\cdot\mid{\bm{y}}_{<t}^{i})\nabla_{\theta}\log\pi_{\theta}({\bm{y}}^{i}))\Big] Inf-Scaling EM-INF § 4 Min. ℋ ^ tok \hat{\mathcal{H}}_{\text{tok}} N/A

Connecting to entropy regularized RL: Entropy-regularized RL by previous works [ 27 , 18 ] uses a an entropy maximization term (as a regularizer) along with the reward signal (policy loss) to encourage stochasticity in action selection and promote exploration. [ 84 ] build on this idea and use few labeled examples for the policy loss along with entropy maximization. They find that using entropy maximization only can boost performance initially, however, the optimization with only entropy maximization does not converge and eventually collapses the policy. In contrast, EM-RL aims to reinforce pretraining biases by learning a more deterministic policy via entropy minimization without requiring any labeled examples. We find that EM-RL can converge on large datasets and improve model performance on math and code generation.

### 3.3 Training Setup

We use the following setup for all experiments, and provide additional details in Appendix D .

Evaluation: For our training experiments, we evaluate on math and coding tasks using [ 13 ] - Math-500 [ 29 ] , AMC [ 43 ] , AIME 2024 [ 43 ] , Minerva math (Minerva) [ 42 ] , Olympiad Bench ( Olymp. ) [ 28 ] , LeetCode ( LeetC ) [ 26 ] , and LiveCodeBench-v2 ( LiveC ) [ 34 ] . For inference time scaling, we additionally evaluate on Scicode [ 78 ] and UGPhysics [ 88 ] . Following [ 63 , 37 ] , we estimate the training FLOPs as 6 ​ P ​ D 6PD and inference FLOPs as 2 ​ P ​ D 2PD where P P is the number of parameters in the model and D D is the number of tokens (Appendix § D.4 )

Training data, models, and methods: We construct the training data for math and coding by randomly sampling 35K prompts from Numina math [ 43 ] and 25K prompts from Eurus-2 coding split [ 13 ] , respectively. We use Qwen2.5-Math-7B [ 89 ] and Eurus-2-7B-SFT [ 13 ] model for training on math and coding, respectively. We use Verl [ 69 ] to train. For all RL methods, we use early stopping based on the validation set. We set the number of rollouts to N = 4 N=4 , batch size to 512 512 , learning rate to 1 ​ e − 6 1e^{-6} . We use a KL regularizer with small coefficient β = 0.001 \beta=0.001 which does not effect entropy minimization. We use RLOO and GRPO with output verification only without reward models. We use the same prompts for EM-FT but without the labels. Instead it samples solutions to estimate the entropy. All experiments are done using 4xGH200 Nvidia GPUs.

Baseline: We consider an additional rewarding scheme based on the frequency of the final answer– Self consistency (SC-RL) . It assigns rewards to each trajectory 𝒚 i {\bm{y}}_{i} based on majority voting [ 85 , 32 ] . An answer a i a_{i} is extracted for the trajectory 𝒚 i {\bm{y}}_{i} and the frequency of the answer is used estimate the reward, r ⁡ ( 𝒚 i ) = ∑ j = 1 N 𝕀 ⁡ ( a i = a j ) N r({\bm{y}}_{i})=\sum_{j=1}^{N}\frac{\mathbb{I}(a_{i}=a_{j})}{N} , where 𝕀 \mathbb{I} is the indicator function. Self-consistency assigns hard rewards to trajectories where answer extraction is possible (e.g. math), however is inapplicable on tasks like code generation. Such rewards are useful on tasks where several consistent answers can be generated (e.g. MATH-500). However, challenging prompts (e.g. scientific coding) often admit multiple plausible solutions with no answer extraction possible, consequently making majority voting inapplicable. [ 99 ] apply this idea for training on the test set, however, we use it on the training set.

Math Coding Math AMC AIME Minerva Olymp. Avg. LeetC LiveC Avg. FLOPs Qwen2.5-7b 43.8 31.3 15.6 14.7 19.0 24.9 26.1 18.4 22.3 – Trained using 60K labeled prompts w/ SFT N=1 48.2 30.2 10.0 17.6 22.4 25.7 18.3 18.3 18.3 0 1.0 w/ RLOO N=4 73.0 57.8 23.3 31.2 34.2 43.9 28.3 26.7 27.5 13.1 w/ GRPO N=4 71.8 56.6 21.1 25.0 35.9 42.1 25.0 25.8 25.4 13.1 Our unsupervised methods trained on 60K unlabeled prompts EM-FT N=1 67.2 51.8 14.4 33.1 34.4 40.2 28.3 17.2 22.8 0 1.0 SC-RL N=4 73.2 51.8 15.6 26.1 36.7 40.7 – – – 13.1 EM-RL-sequence N=4 67.2 53.0 21.1 30.9 35.6 41.6 31.1 21.7 26.4 13.1 EM-RL-token N=4 70.8 57.8 18.9 30.9 35.9 42.9 29.5 24.5 27.0 13.1

### 3.4 Results: Entropy Minimization for Post-Training

Table 2 compares the performance of using entropy minimization as a standalone post-training objective to supervised finetuning and output-verified RL.

Can unsupervised finetuning by directly minimizing token-level entropy improve LLMs? We first observe that directly minimizing the entropy (EM-FT) can improve improve performance over the base model by 8 % 8\% on average on math and coding without using any labels. This observation indicates that pretraining priors can be further capitalized to squeeze more performance and entropy can independently contribute to performance gains. We also note that with only N = 1 N=1 trajectory sampled from the model, EM-FT can achieve competitive performance to GRPO and RLOO (outperforms on Minerva and LeetCode by 5 % 5\% on average) which require output verification over multiple sampled ( N = 4 N=4 ) trajectories. EM-FT better contextualizes the improvements from supervised methods and better uses pretraining capacity, while maintaining a smaller computational footprint. We also observe no improvements on LiveCode likely because LiveCode is regularly updated with new problems that might be different from the pretraining distribution [ 34 ] . This observation indicates that entropy minimization can potentially boost performance on unlabeled scenarios if it’s not significantly different from the pretraining task mixture [ 81 , 73 , 31 ] .

Can we improve learning from entropy minimization through RL? In Table 2 , we observe that unsupervised RL methods ( SC-RL,EM-RL ) improves base model performance by 11 % 11\% on average and maintains competitive performance as compared to output-verified GRPO and RLOO (outperforms on AMC, Minerva and LeetCode by 4.5 % 4.5\% on average) under similar compute constraints. This observation suggests that model confidences in the form of token and sequence level entropy estimation can be used as pseudo-rewards to learn from unlabeled scenarios and better use pretraining priors. This observation also ties up with [ 55 , 20 , 31 ] who show that model confidences can be a proxy for reward. Among the various rewarding schemes, we observe that token level and sequence level entropy estimation can be flexibly applied to a variety of tasks without assumptions on the problem structure (e.g. answer extraction) unlike self-consistency which is not applicable for code generation. On average, we observe that EM-RL has better performance via entropy rewards, indicating that fewer deterministic CoTs is more useful on certain reasoning tasks (LiveCode, AMC). We also notice that EM-RL improve model performance on LiveCode by 6 % 6\% where direct entropy minimization ( EM-FT ) did not work, indicating that careful reward design to learn from unlabeled experience can better enhance learning and pretraining capabilities. Through EM-FT and EM-RL , we show that EM can elicit pretraining priors necessary for reasoning without any labeled data. While supervised training is expected to scale better, we put forward EM-FT and EM-RL as important baselines to better contextualize improvements from post-training methods.

Math Coding Science Math AMC AIME Minerva Olymp. Avg. LeetCode UGPhysics Qwen2.5-Math-7B-Instruct 79.2 48.2 0 8.9 43.4 41.3 44.2 0 0.6 18.6 Greedy Decoding ( t = 0 t=0 ) 79.0 53.0 11.1 42.6 39.9 45.1 0 1.1 18.8 Iterative-refinement ( N = 3 N=3 ) 79.2 48.2 0 8.9 43.4 41.3 44.2 0 1.7 16.4 Self-consistency ( N = 4 N=4 ) 78.8 53.0 11.1 43.4 40.7 45.4 – 19.6 Adaptive Temp 80.8 55.4 10.0 41.5 38.7 45.3 0 2.2 23.7 EM-INF 80.2 54.2 14.4 42.3 40.8 46.4 0 0.6 23.1 Qwen2.5-7B-Instruct 74.0 41.0 0 8.9 41.2 37.5 40.5 47.2 23.4 Greedy Decoding ( t = 0 t=0 ) 74.2 44.6 0 7.8 40.4 37.2 40.8 46.1 23.7 Iterative-refinement ( N = 3 N=3 ) 73.8 37.3 10.0 41.5 37.8 40.1 50.0 21.5 Self-consistency ( N = 4 N=4 ) 73.4 43.4 10.0 33.5 41.3 40.3 – 23.4 Adaptive Temp 74.4 50.6 10.0 41.9 39.7 43.3 49.4 25.8 EM-INF 73.8 45.8 11.1 41.2 38.2 42.0 51.7 26.9 Llama-3.1-8B-Instruct 40.6 18.1 0 1.1 22.4 15.7 19.6 10.6 17.5 Greedy Decoding ( t = 0 t=0 ) 40.6 16.9 0 3.3 21.0 16.0 19.6 12.8 16.1 Iterative-refinement ( N = 3 N=3 ) 41.0 19.3 0 1.1 22.4 15.7 19.9 11.7 18.3 Self-consistency ( N = 4 N=4 ) 41.2 20.5 0 4.4 20.2 19.4 21.1 – 20.2 Adaptive Temp 43.6 25.3 0 5.5 24.3 16.6 23.1 17.2 19.9 EM-INF 43.0 22.9 0 3.3 22.8 16.4 21.7 14.4 20.4

## 4 EM-INF: Inference-time Logit Optimization

Inference-time scaling methods suggest that enabling LLMs to improve their output generations at test time by scaling compute is critical for improving performance on a complex tasks [ 86 , 72 , 66 , 50 , 6 ] . Practical LLMs need to adapt to tasks online, i.e., we should be able to adapt to user-queries while the requests are being received. As a result, online LLM adaptation should be unsupervised. Self-consistency (parallel generations) [ 83 ] and iterative-refinement (sequential generations) are widely used for reasoning when external verification is not available [ 47 ] . Self-consistency samples multiple answers from the model and then selects the solution with the largest frequency. Whereas iterative-refinement feeds the previously generated solution into the model as in-context examples inorder to refine the solution. However, online adaptation should not be tailored to certain problem types—self-consistency only works when output extraction is possible and iterative refinement is bottle-necked by context length. To tackle these challenges we propose EM-INF that uses entropy minimization at inference time for logit adjustment. EM-INF treats the model’s output logits as if they were parameters, and uses gradient descent to update them to minimize the entropy of the distribution they induce; no gradient wrt. or the model parameters or parameter update is needed.

Let 𝒛 t ∈ ℝ 𝒱 {\bm{z}}_{t}\in\mathbb{R}^{\mathcal{V}} be a the logit vector produced by the model at generation step t t from its last layer. We freeze the model parameters and optimize the logits 𝒛 t {\bm{z}}_{t} to minimize the entropy of the output distribution it induces via gradient descent. We treat the logits as free parameters and never backpropagate through the model or update its parameters. To prevent over-optimization, which would effectively lead to greedy decoding, we use a minimum entropy threshold δ \delta (we empirically find 0.1 < δ < 0.5 0.1<\delta<0.5 works the best). Our inference time objective for each generation steps is defined as, ℒ EM-INF = max ( − ∑ j ∈ 𝒱 σ ( 𝒛 t ) j log σ ( 𝒛 t ) j , δ ) , \mathcal{L}_{\text{EM-INF}}=\max\Big(-\sum_{j\in\mathcal{V}}\sigma({\bm{z}}_{t})_{j}\log\sigma({\bm{z}}_{t})_{j},\delta\Big), (5) where σ \sigma denotes the softmax function. After logit optimization, we use sampling based decoding to select the next token, since this optimization does not change the top logit and greedy decoding will not change the output post-optimization (Prop. 1 ) [ 31 ] . The above optimization operates over 𝒛 t {\bm{z}}_{t} and is equivalent to optimizing a one-layer neural network with | 𝒱 | |\mathcal{V}| parameters with a softmax activation. We empirically find that 5 to 15 gradient steps are enough. The vocabulary size ( ∼ 150 \sim 150 K in Qwen2.5 [ 77 ] ) is much smaller than number of parameters ( 7 7 B) in the model, making the optimization overhead negligible compared to a forward pass of the full model. We require only 𝒪 ⁡ ( n ) \mathcal{O}(n) ( n n is sequence length) forward passes from the language model, equivalent to regular decoding. Whereas, other inference time scaling methods like self-consistency and sequential refinement require 𝒪 ⁡ ( N ​ n ) \mathcal{O}(Nn) forward passes where N N is the number of trajectories.

Baseline: We use adaptive temperature scaling to reduce the entropy of the models’ output distribution. Starting from logits 𝒛 t {\bm{z}}_{t} we gradually decrease the temperature τ \tau in the softmax until the entropy reaches a target value. We search for the largest τ > 0 \tau>0 such that ℋ ⁡ ( σ ⁡ ( 𝒛 t / τ ) ) ≤ max ⁡ ( α ​ ℋ ​ ( σ ⁡ ( 𝒛 t ) ) , δ ) \mathcal{H}(\sigma({\bm{z}}_{t}/\tau))\leq\max(\alpha\mathcal{H}(\sigma({\bm{z}}_{t})),\delta) , where α ∈ ( 0 , 1 ) \alpha\in(0,1) controls the fraction of entropy to reduce. We find α ∈ ( 0.4 , 0.6 ) \alpha\in(0.4,0.6) works the best.

###### Proposition 1 .

(Informal) Both adaptive temperature scaling and logit optimization reduce the entropy of a model’s output distribution. However, in high-uncertainty settings (i.e., when the model’s predictive distribution has high entropy), logit optimization can change the order of non-top logits. In contrast, temperature scaling preserves the order of logits and merely sharpens or flattens the distribution proportionally. Both temperature scaling and logit optimization will keep the token with the top logit and increase its probability, making them less likely to change the model’s behavior when it is highly confident (Appendix A ).

Sub w/ BG Main w/ BG GPT-4o 35.4 9.2 GPT-4-Turbo-2024-04-09 33.7 0 9.2 Claude3.5-Sonnet 35.4 12.3 Claude3-Opus 26.7 0 4.7 Claude3-Sonnet 25.7 0 4.7 Gemini 1.5 Pro 30.6 0 7.7 Qwen2.5-7b-Instruct 11.5 0 0.0 Greedy decoding ( t = 0 t=0 ) 13.4 0 3.0 Iterative-refinement ( n = 2 n=2 ) 12.1 0 0.0 Adaptive Temp 13.2 0 0.0 EM-INF 16.7 0 1.5 Qwen2.5-32b-Instruct 25.4 0 4.6 Greedy decoding ( t = 0 t=0 ) 25.4 0 4.6 Iterative-refinement ( n = 2 n=2 ) 24.7 0 7.6 Adaptive Temp 28.8 0 7.6 EM-INF 27.1 10.7

EM-INF for scientific coding: We apply EM-INF to scientific coding in Table 1 . SciCode is a challenging code generation benchmark requiring significant domain knowledge and reasoning capabilities where even frontier models such as GPT4o struggle [ 78 ] . We observe that test time entropy minimization ( EM-INF , adaptive temperature) can improve performance of the base models consistently on easier subproblems and eventually on the more difficult main problem by 2.5 % 2.5\% . We note that logit optimization (EM-INF) is better than adaptive temperature scaling on SciCode by 3 % 3\% . Owing to the difficulty of SciCode, the models’ output distribution has large entropy. Under this scenario, EM-INF can change the relative order of the logits which likely leads to better reasoning chains. Whereas, adaptive temperature scaling will never change the relative ordering of the logits on each generation step – it only makes the distribution peakier (Proposition 1 ). Next, we observe that scaling through iterative-refinement [ 47 ] leads to some improvements over the base model, however, it is bottlenecked by the max context length of the model making it harder to refine long chain of thoughts. Whereas, EM-INF does not require refinement and maintains the same computational complexity as the base model when used with regular decoding.

We note that EM-INF with Qwen2.5-32B-Instruct can outperform several frontier models on the main problem without requiring refinement or editing model parameters by 3 % 3\% and over the base model by 6 % 6\% . Building on these observations, we put forward EM-INF as a practical, compute efficient inference time scaling method that does not require any supervision and makes no assumption on the nature of the problem.

EM-INF for math and coding: Table 3 compares the performance of EM-INF for test time scaling. We observe that minimizing the entropy of the model at test time without updating the parameters (EM-INF, adaptive temperature) improves the performance of the base model for almost all tasks and model classes by 3 % 3\% on average, indicating that EM is an useful method for test time scaling. We also note that EM can be applied to all tasks (math, coding and ugphysics) without assumptions such as output extraction in self-consistency or output scoring. Next, we note that EM competitively performs against self-consistency while outperforming it on tasks requiring significant reasoning capabilities, e.g. AIME, and UGPysics by 4 % 4\% and 3.6 % 3.6\% , respectively. Unlike self-consistency which requires sampling multiple trajectories ( N > 1 N>1 ), EM-INF requires only one trajectory leading to lower computational requirements. These observations collectively indicate that pretraining performance can be improved via EM, and making the model more deterministic at inference time via unsupervised EM in-order to prefer fewer chain of thought options can lead to better performance.

Computational efficiency: Figure 2 compares the compute requirements of EM-INF with inference scaling baselines. We observe that EM-INF can achieve better performance while using a third of time. This observation suggests that EM-INF is a practical inference scaling method in compute bound scenarios, for online adaption without updating model parameters [ 81 , 9 ] . EM-INF can also be combined with self-consistency and sequential refinement to scale up (Appendix § C.1 ).

## 5 Limitations: Dependence on Base Model Capability and Confidence

Math AMC AIME Minerva Olymp . Llama-3.1-8B-Instruct 40.6 18.1 1.0 22.4 15.7 W/ RLOO 52.0 25.3 3.3 26.8 20.7 EM-FT (N=1) 42.2 21.7 3.3 18.8 16.4 EM-RL-token (N=4) 41.0 18.1 5.6 19.1 15.6 EM-RL-sequence (N=4) 41.6 18.1 7.8 18.4 16.6 IndVal Qwen2.5-7B-Instruct 65.9 EM-FT (N=1) 66.0 EM-RL-token (N=4) 66.0 EM-RL-sequence (N=4) 66.3

To contextualize the applicability of EM, we probe its performance by 1) training on tasks with different bias as compared to pretraining; and 2) finetuning models lacking target reasoning behaviors.

Table 4 (right) evaluates EM on individualistic value reasoning ( IndVal ) [ 35 ] . Individualistic value reasoning is a difficult alignment task that evaluates LLMs’ ability to reason about an individual’s value preferences in new situations. Given known statements about a certain individual, the task is to predict if the user would or would not associate with a new situation (measured using accuracy). We observe that Qwen-2.5-7B struggles with the task, likely because LLMs’ are biased to coarse values acquired from pretraining which may not generalize to a large pluralistic audience [ 97 , 35 ] . As expected, we note that EM is not effective in this task, likely because model confidences are incorrectly biased to training priors that do not benefit the target task, as also observed in [ 99 , 31 ] .

Furthermore, Table 4 (left) compares entropy minimization ( EM-FT , EM-RL ) with supervised RL (RLOO) using the same training data, setup and evaluation as Sec. 3.3 with Llama-3.1-8b-Instruct as the base model [ 24 ] . We observe that while supervised RL can improve model performance, improvements from entropy minimization is less effective as compared to Qwen-2.5 and can sometimes hurt performance on math reasoning. We tie this observation to [ 21 ] who show that Llama models may lack reasoning behaviors initially as compared to Qwen models, as also observed in [ 84 ] . The lack of certain reasoning behaviors for math in the initial policy possibly leads to unreliable model confidences and eventually inaccurate entropy rewards [ 12 ] . This observation suggests that success of entropy minimization hinges on the assumption that the pre-trained model’s initial reasoning behaviors are critical for the capacity of improvement. Overall, the success of EM-FT and EM-RL must be interpreted with care, as it can be less effective depending on the task and base model choice.

## 6 Conclusion

We show that entropy minimization through unsupervised finetuning (EM-FT), RL with standalone negative entropy as reward (EM-RL) and inference time scaling through logit optimization (EM-INF) can improve LLMs on complex math, physics, and coding tasks without using any labeled data. We observe that through EM-FT and EM-RL, Qwen-2.5-7B can achieve comparable or better performance than RL methods like GRPO and RLOO. Through test time logit optimization, EM-INF enables Qwen-2.5-32B to outperform proprietary models like GPT4o on complex scientific coding without training or updating model parameters. Our findings suggest that many pretrained LLMs already possess strong reasoning ability which can be enhanced using EM alone. While successful, EM is less beneficial on tasks and models with different inductive biases as pretraining. We call for the inclusion of EM-FT, EM-RL and EM-INF as a baseline in the evaluation of future post-pretraining and inference-time scaling algorithms, to better attribute the source of improvements in them.

## Acknowledgments and Disclosure of Funding

This research used the DeltaAI advanced computing and data resource, which is supported by the National Science Foundation (award OAC 2320345) and the State of Illinois. DeltaAI is a joint effort of the University of Illinois Urbana-Champaign and its National Center for Supercomputing Applications.

This work was also in part supported by research awards from Apple and the Allen Institute for AI.

Research was also supported in part by US DARPA INCAS Program No. HR0011-21-C0165 and BRIES Program No. HR0011-24-3-0325, National Science Foundation IIS-19-56151, the Molecule Maker Lab Institute: An AI Research Institutes program supported by NSF under Award No. 2019897, and the Institute for Geospatial Understanding through an Integrative Discovery Environment (I-GUIDE) by NSF under Award No. 2118329. Any opinions, findings, and conclusions or recommendations expressed herein are those of the authors and do not necessarily represent the views, either expressed or implied, of DARPA or the U.S. Government.

## References

[1] Arash Ahmadian, Chris Cremer, Matthias Gallé, Marzieh Fadaee, Julia Kreutzer, Olivier Pietquin, Ahmet Üstün, and Sara Hooker. Back to basics: Revisiting reinforce style optimization for learning from human feedback in llms. arXiv preprint arXiv:2402.14740 , 2024.

[2] Jihyun Janice Ahn and Wenpeng Yin. Prompt-reverse inconsistency: Llm self-inconsistency beyond generative randomness and prompt paraphrasing. arXiv preprint arXiv:2504.01282 , 2025.

[3] Vamsi Aribandi, Yi Tay, Tal Schuster, Jinfeng Rao, Huaixiu Steven Zheng, Sanket Vaibhav Mehta, Honglei Zhuang, Vinh Q Tran, Dara Bahri, Jianmo Ni, et al. Ext5: Towards extreme multi-task scaling for transfer learning. arXiv preprint arXiv:2111.10952 , 2021.

[4] Berk Atil, Alexa Chittams, Liseng Fu, Ferhan Ture, Lixinyu Xu, and Breck Baldwin. Llm stability: A detailed analysis with some surprises. arXiv preprint arXiv:2408.04667 , 2024.

[5] Yuntao Bai, Saurav Kadavath, Sandipan Kundu, Amanda Askell, Jackson Kernion, Andy Jones, Anna Chen, Anna Goldie, Azalia Mirhoseini, Cameron McKinnon, et al. Constitutional ai: Harmlessness from ai feedback. arXiv preprint arXiv:2212.08073 , 2022.

[6] Vidhisha Balachandran, Jingya Chen, Lingjiao Chen, Shivam Garg, Neel Joshi, Yash Lara, John Langford, Besmira Nushi, Vibhav Vineet, Yue Wu, et al. Inference-time scaling for complex tasks: Where we stand and what lies ahead. arXiv preprint arXiv:2504.00294 , 2025.

[7] Ahmad Beirami, Alekh Agarwal, Jonathan Berant, Alexander D’Amour, Jacob Eisenstein, Chirag Nagpal, and Ananda Theertha Suresh. Theoretical guarantees on the best-of-n alignment policy. arXiv preprint arXiv:2401.01879 , 2024.

[8] David Berthelot, Nicholas Carlini, Ian Goodfellow, Nicolas Papernot, Avital Oliver, and Colin A Raffel. Mixmatch: A holistic approach to semi-supervised learning. Advances in neural information processing systems , 32, 2019.

[9] Malik Boudiaf, Romain Mueller, Ismail Ben Ayed, and Luca Bertinetto. Parameter-free online test-time adaptation. In Proceedings of the IEEE/CVF Conference on Computer Vision and Pattern Recognition , pages 8344–8353, 2022.

[10] Sébastien Bubeck, Varun Chadrasekaran, Ronen Eldan, Johannes Gehrke, Eric Horvitz, Ece Kamar, Peter Lee, Yin Tat Lee, Yuanzhi Li, Scott Lundberg, et al. Sparks of artificial general intelligence: Early experiments with gpt-4, 2023.

[11] Xinyun Chen, Maxwell Lin, Nathanael Schärli, and Denny Zhou. Teaching large language models to self-debug. In The Twelfth International Conference on Learning Representations , 2024. URL https://openreview.net/forum?id=KuPixIqPiq .

[12] Thomas M Cover. Elements of information theory . John Wiley & Sons, 1999.

[13] Ganqu Cui, Lifan Yuan, Zefan Wang, Hanbin Wang, Wendi Li, Bingxiang He, Yuchen Fan, Tianyu Yu, Qixin Xu, Weize Chen, et al. Process reinforcement through implicit rewards. arXiv preprint arXiv:2502.01456 , 2025.

[14] Yuhao Ding, Junzi Zhang, Hyunin Lee, and Javad Lavaei. Beyond exact gradients: Convergence of stochastic soft-max policy gradient methods with entropy regularization. arXiv preprint arXiv:2110.10117 , 2021.

[15] Mario Döbler, Florian Marencke, Robert A Marsden, and Bin Yang. Diversity-aware buffer for coping with temporally correlated data streams in online test-time adaptation. In ICASSP 2024-2024 IEEE International Conference on Acoustics, Speech and Signal Processing (ICASSP) , pages 7665–7669. IEEE, 2024.

[16] Hanze Dong, Wei Xiong, Deepanshu Goyal, Yihan Zhang, Winnie Chow, Rui Pan, Shizhe Diao, Jipeng Zhang, KaShun SHUM, and Tong Zhang. RAFT: Reward ranked finetuning for generative foundation model alignment. Transactions on Machine Learning Research , 2023. ISSN 2835-8856. URL https://openreview.net/forum?id=m7p5O7zblY .

[17] Laura Ekroot and Thomas M Cover. The entropy of markov trajectories. IEEE Transactions on Information Theory , 39(4):1418–1421, 2002.

[18] Benjamin Eysenbach and Sergey Levine. Maximum entropy rl (provably) solves some robust rl problems. arXiv preprint arXiv:2103.06257 , 2021.

[19] Angela Fan, Mike Lewis, and Yann Dauphin. Hierarchical neural story generation. In Annual Meeting of the Association for Computational Linguistics , 2018. URL https://api.semanticscholar.org/CorpusID:44134226 .

[20] Chelsea Finn, Tianhe Yu, Justin Fu, Pieter Abbeel, and Sergey Levine. Generalizing skills with semi-supervised reinforcement learning. arXiv preprint arXiv:1612.00429 , 2016.

[21] Kanishk Gandhi, Ayush Chakravarthy, Anikait Singh, Nathan Lile, and Noah D Goodman. Cognitive behaviors that enable self-improving reasoners, or, four habits of highly effective stars. arXiv preprint arXiv:2503.01307 , 2025.

[22] Zhibin Gou, Zhihong Shao, Yeyun Gong, Yelong Shen, Yujiu Yang, Nan Duan, and Weizhu Chen. Critic: Large language models can self-correct with tool-interactive critiquing. arXiv preprint arXiv:2305.11738 , 2023.

[23] Yves Grandvalet and Yoshua Bengio. Semi-supervised learning by entropy minimization. Advances in neural information processing systems , 17, 2004.

[24] Aaron Grattafiori, Abhimanyu Dubey, Abhinav Jauhri, Abhinav Pandey, Abhishek Kadian, Ahmad Al-Dahle, Aiesha Letman, Akhil Mathur, Alan Schelten, Alex Vaughan, et al. The llama 3 herd of models. arXiv preprint arXiv:2407.21783 , 2024.

[25] S Dhillon Guneet, Chaudhari Pratik, Ravichandran Avinash, and S Stefano. A baseline for few-shot image classification. In International Conference on Learning Representations (ICLR) , volume 10, 2020.

[26] Daya Guo, Qihao Zhu, Dejian Yang, Zhenda Xie, Kai Dong, Wentao Zhang, Guanting Chen, Xiao Bi, Yu Wu, YK Li, et al. Deepseek-coder: When the large language model meets programming–the rise of code intelligence. arXiv preprint arXiv:2401.14196 , 2024.

[27] Tuomas Haarnoja, Aurick Zhou, Pieter Abbeel, and Sergey Levine. Soft actor-critic: Off-policy maximum entropy deep reinforcement learning with a stochastic actor. In International conference on machine learning , pages 1861–1870. Pmlr, 2018.

[28] Chaoqun He, Renjie Luo, Yuzhuo Bai, Shengding Hu, Zhen Thai, Junhao Shen, Jinyi Hu, Xu Han, Yujie Huang, Yuxiang Zhang, Jie Liu, Lei Qi, Zhiyuan Liu, and Maosong Sun. OlympiadBench: A challenging benchmark for promoting AGI with olympiad-level bilingual multimodal scientific problems. In Lun-Wei Ku, Andre Martins, and Vivek Srikumar, editors, Proceedings of the 62nd Annual Meeting of the Association for Computational Linguistics (Volume 1: Long Papers) , pages 3828–3850, Bangkok, Thailand, August 2024. Association for Computational Linguistics. doi: 10.18653/v1/2024.acl-long.211 . URL https://aclanthology.org/2024.acl-long.211/ .

[29] Dan Hendrycks, Collin Burns, Saurav Kadavath, Akul Arora, Steven Basart, Eric Tang, Dawn Song, and Jacob Steinhardt. Measuring mathematical problem solving with the math dataset. NeurIPS , 2021.

[30] Ari Holtzman, Jan Buys, Li Du, Maxwell Forbes, and Yejin Choi. The curious case of neural text degeneration. arXiv preprint arXiv:1904.09751 , 2019.

[31] Audrey Huang, Adam Block, Dylan J Foster, Dhruv Rohatgi, Cyril Zhang, Max Simchowitz, Jordan T Ash, and Akshay Krishnamurthy. Self-improvement in language models: The sharpening mechanism. arXiv preprint arXiv:2412.01951 , 2024.

[32] Jiaxin Huang, Shixiang Shane Gu, Le Hou, Yuexin Wu, Xuezhi Wang, Hongkun Yu, and Jiawei Han. Large language models can self-improve. arXiv preprint arXiv:2210.11610 , 2022.

[33] Shiyu Huang, Hang Su, Jun Zhu, and Ting Chen. Svqn: Sequential variational soft q-learning networks. In International Conference on Learning Representations , 2020. URL https://openreview.net/forum?id=r1xPh2VtPB .

[34] Naman Jain, King Han, Alex Gu, Wen-Ding Li, Fanjia Yan, Tianjun Zhang, Sida Wang, Armando Solar-Lezama, Koushik Sen, and Ion Stoica. Livecodebench: Holistic and contamination free evaluation of large language models for code. arXiv preprint arXiv:2403.07974 , 2024.

[35] Liwei Jiang, Taylor Sorensen, Sydney Levine, and Yejin Choi. Can language models reason about individualistic human values and preferences? arXiv preprint arXiv:2410.03868 , 2024a.

[36] Liwei Jiang, Taylor Sorensen, Sydney Levine, and Yejin Choi. Can language models reason about individualistic human values and preferences?, 2024b. URL https://arxiv.org/abs/2410.03868 .

[37] Jared Kaplan, Sam McCandlish, Tom Henighan, Tom B Brown, Benjamin Chess, Rewon Child, Scott Gray, Alec Radford, Jeffrey Wu, and Dario Amodei. Scaling laws for neural language models. arXiv preprint arXiv:2001.08361 , 2020.

[38] Hilbert J Kappen, Vicenç Gómez, and Manfred Opper. Optimal control as a graphical model inference problem. Machine learning , 87:159–182, 2012.

[39] Mijeong Kim, Seonguk Seo, and Bohyung Han. Infonerf: Ray entropy minimization for few-shot neural volume rendering. In Proceedings of the IEEE/CVF Conference on Computer Vision and Pattern Recognition , pages 12912–12921, 2022.

[40] Dong-Hyun Lee. Pseudo-label : The simple and efficient semi-supervised learning method for deep neural networks. 2013. URL https://api.semanticscholar.org/CorpusID:18507866 .

[41] Sergey Levine. Reinforcement learning and control as probabilistic inference: Tutorial and review. arXiv preprint arXiv:1805.00909 , 2018.

[42] Aitor Lewkowycz, Anders Johan Andreassen, David Dohan, Ethan Dyer, Henryk Michalewski, Vinay Venkatesh Ramasesh, Ambrose Slone, Cem Anil, Imanol Schlag, Theo Gutman-Solo, Yuhuai Wu, Behnam Neyshabur, Guy Gur-Ari, and Vedant Misra. Solving quantitative reasoning problems with language models. In Alice H. Oh, Alekh Agarwal, Danielle Belgrave, and Kyunghyun Cho, editors, Advances in Neural Information Processing Systems , 2022. URL https://openreview.net/forum?id=IFXTZERXdM7 .

[43] Jia LI, Edward Beeching, Lewis Tunstall, Ben Lipkin, Roman Soletskyi, Shengyi Costa Huang, Kashif Rasul, Longhui Yu, Albert Jiang, Ziju Shen, Zihan Qin, Bin Dong, Li Zhou, Yann Fleureau, Guillaume Lample, and Stanislas Polu. Numinamath. [https://huggingface.co/AI-MO/NuminaMath-CoT](https://github.com/project-numina/aimo-progress-prize/blob/main/report/numina_dataset.pdf) , 2024.

[44] Yiwei Li, Ji Zhang, Shaoxiong Feng, Peiwen Yuan, Xinglin Wang, Jiayi Shi, Yueqi Zhang, Chuyi Tan, Boyuan Pan, Yao Hu, et al. Revisiting self-consistency from dynamic distributional alignment perspective on answer aggregation. arXiv preprint arXiv:2502.19830 , 2025.

[45] Zijun Liu, Peiyi Wang, Runxin Xu, Shirong Ma, Chong Ruan, Peng Li, Yang Liu, and Yu Wu. Inference-time scaling for generalist reward modeling. arXiv preprint arXiv:2504.02495 , 2025.

[46] Trung Quoc Luong, Xinbo Zhang, Zhanming Jie, Peng Sun, Xiaoran Jin, and Hang Li. Reft: Reasoning with reinforced fine-tuning. arXiv preprint arXiv:2401.08967 , 3, 2024.

[47] Aman Madaan, Niket Tandon, Prakhar Gupta, Skyler Hallinan, Luyu Gao, Sarah Wiegreffe, Uri Alon, Nouha Dziri, Shrimai Prabhumoye, Yiming Yang, et al. Self-refine: Iterative refinement with self-feedback. Advances in Neural Information Processing Systems , 36:46534–46594, 2023.

[48] Robert A Marsden, Mario Döbler, and Bin Yang. Universal test-time adaptation through weight ensembling, diversity weighting, and prior correction. In Proceedings of the IEEE/CVF Winter Conference on Applications of Computer Vision , pages 2555–2565, 2024.

[49] Jincheng Mei, Wesley Chung, Valentin Thomas, Bo Dai, Csaba Szepesvari, and Dale Schuurmans. The role of baselines in policy gradient optimization. Advances in Neural Information Processing Systems , 35:17818–17830, 2022.

[50] Niklas Muennighoff, Zitong Yang, Weijia Shi, Xiang Lisa Li, Li Fei-Fei, Hannaneh Hajishirzi, Luke Zettlemoyer, Percy Liang, Emmanuel Candès, and Tatsunori Hashimoto. s1: Simple test-time scaling. arXiv preprint arXiv:2501.19393 , 2025.

[51] Gang Niu, Bo Dai, Makoto Yamada, and Masashi Sugiyama. Information-theoretic semi-supervised metric learning via entropy regularization. Neural Computation , 26:1717–1762, 2012. URL https://api.semanticscholar.org/CorpusID:15064396 .

[52] Avital Oliver, Augustus Odena, Colin A Raffel, Ekin Dogus Cubuk, and Ian Goodfellow. Realistic evaluation of deep semi-supervised learning algorithms. Advances in neural information processing systems , 31, 2018.

[53] Daniel Jarne Ornia, Giannis Delimpaltadakis, Jens Kober, and Javier Alonso-Mora. Predictable reinforcement learning dynamics through entropy rate minimization. arXiv preprint arXiv:2311.18703 , 2023.

[54] Jing-Cheng Pang, Pengyuan Wang, Kaiyuan Li, Xiong-Hui Chen, Jiacheng Xu, Zongzhang Zhang, and Yang Yu. Language model self-improvement by reinforcement learning contemplation. In The Twelfth International Conference on Learning Representations , 2024. URL https://openreview.net/forum?id=38E4yUbrgr .

[55] Jongjin Park, Younggyo Seo, Jinwoo Shin, Honglak Lee, Pieter Abbeel, and Kimin Lee. Surf: Semi-supervised reward learning with data augmentation for feedback-efficient preference-based reinforcement learning. arXiv preprint arXiv:2203.10050 , 2022.

[56] Ori Press, Ravid Shwartz-Ziv, Yann LeCun, and Matthias Bethge. The entropy enigma: Success and failure of entropy minimization. arXiv preprint arXiv:2405.05012 , 2024.

[57] Yuxiao Qu, Tianjun Zhang, Naman Garg, and Aviral Kumar. Recursive introspection: Teaching language model agents how to self-improve. Advances in Neural Information Processing Systems , 37:55249–55285, 2024.

[58] Alec Radford and Karthik Narasimhan. Improving language understanding by generative pre-training. 2018. URL https://api.semanticscholar.org/CorpusID:49313245 .

[59] Colin Raffel, Noam Shazeer, Adam Roberts, Katherine Lee, Sharan Narang, Michael Matena, Yanqi Zhou, Wei Li, and Peter J Liu. Exploring the limits of transfer learning with a unified text-to-text transformer. Journal of machine learning research , 21(140):1–67, 2020.

[60] Subhankar Roy, Aliaksandr Siarohin, Enver Sangineto, Samuel Rota Bulo, Nicu Sebe, and Elisa Ricci. Unsupervised domain adaptation using feature-whitening and consensus loss. In Proceedings of the IEEE/CVF conference on computer vision and pattern recognition , pages 9471–9480, 2019.

[61] Evgenia Rusak, Steffen Schneider, George Pachitariu, Luisa Eck, Peter Gehler, Oliver Bringmann, Wieland Brendel, and Matthias Bethge. If your data distribution shifts, use self-learning. arXiv preprint arXiv:2104.12928 , 2021.

[62] Kuniaki Saito, Donghyun Kim, Stan Sclaroff, Trevor Darrell, and Kate Saenko. Semi-supervised domain adaptation via minimax entropy. In Proceedings of the IEEE/CVF international conference on computer vision , pages 8050–8058, 2019.

[63] Nikhil Sardana, Jacob Portes, Sasha Doubov, and Jonathan Frankle. Beyond chinchilla-optimal: Accounting for inference in language model scaling laws. arXiv preprint arXiv:2401.00448 , 2023.

[64] John Schulman, Filip Wolski, Prafulla Dhariwal, Alec Radford, and Oleg Klimov. Proximal policy optimization algorithms. arXiv preprint arXiv:1707.06347 , 2017.

[65] Amrith Setlur, Chirag Nagpal, Adam Fisch, Xinyang Geng, Jacob Eisenstein, Rishabh Agarwal, Alekh Agarwal, Jonathan Berant, and Aviral Kumar. Rewarding progress: Scaling automated process verifiers for llm reasoning. arXiv preprint arXiv:2410.08146 , 2024.

[66] Amrith Setlur, Nived Rajaraman, Sergey Levine, and Aviral Kumar. Scaling test-time compute without verification or rl is suboptimal. arXiv preprint arXiv:2502.12118 , 2025.

[67] Claude E Shannon. A mathematical theory of communication. The Bell system technical journal , 27(3):379–423, 1948.

[68] Zhihong Shao, Peiyi Wang, Qihao Zhu, Runxin Xu, Junxiao Song, Xiao Bi, Haowei Zhang, Mingchuan Zhang, YK Li, Y Wu, et al. Deepseekmath: Pushing the limits of mathematical reasoning in open language models. arXiv preprint arXiv:2402.03300 , 2024.

[69] Guangming Sheng, Chi Zhang, Zilingfeng Ye, Xibin Wu, Wang Zhang, Ru Zhang, Yanghua Peng, Haibin Lin, and Chuan Wu. Hybridflow: A flexible and efficient rlhf framework. arXiv preprint arXiv: 2409.19256 , 2024.

[70] Noah Shinn, Federico Cassano, Ashwin Gopinath, Karthik Narasimhan, and Shunyu Yao. Reflexion: Language agents with verbal reinforcement learning. Advances in Neural Information Processing Systems , 36:8634–8652, 2023.

[71] Manli Shu, Weili Nie, De-An Huang, Zhiding Yu, Tom Goldstein, Anima Anandkumar, and Chaowei Xiao. Test-time prompt tuning for zero-shot generalization in vision-language models. Advances in Neural Information Processing Systems , 35:14274–14289, 2022.

[72] Charlie Snell, Jaehoon Lee, Kelvin Xu, and Aviral Kumar. Scaling llm test-time compute optimally can be more effective than scaling model parameters, 2024. URL https://arxiv. org/abs/2408.03314 , 11, 2024.

[73] Kaya Stechly, Karthik Valmeekam, and Subbarao Kambhampati. On the self-verification limitations of large language models on reasoning and planning tasks. arXiv preprint arXiv:2402.08115 , 2024.

[74] Nisan Stiennon, Long Ouyang, Jeff Wu, Daniel M. Ziegler, Ryan Lowe, Chelsea Voss, Alec Radford, Dario Amodei, and Paul Christiano. Learning to summarize from human feedback, 2022. URL https://arxiv.org/abs/2009.01325 .

[75] Richard S Sutton, David McAllester, Satinder Singh, and Yishay Mansour. Policy gradient methods for reinforcement learning with function approximation. In S. Solla, T. Leen, and K. Müller, editors, Advances in Neural Information Processing Systems , volume 12. MIT Press, 1999a. URL https://proceedings.neurips.cc/paper_files/paper/1999/file/464d828b85b0bed98e80ade0a5c43b0f-Paper.pdf .

[76] Richard S Sutton, David McAllester, Satinder Singh, and Yishay Mansour. Policy gradient methods for reinforcement learning with function approximation. Advances in neural information processing systems , 12, 1999b.

[77] Qwen Team. Qwen2.5: A party of foundation models, September 2024. URL https://qwenlm.github.io/blog/qwen2.5/ .

[78] Minyang Tian, Luyu Gao, Shizhuo Dylan Zhang, Xinan Chen, Cunwei Fan, Xuefei Guo, Roland Haas, Pan Ji, Kittithat Krongchon, Yao Li, et al. Scicode: A research coding benchmark curated by scientists, 2024. URL https://arxiv. org/abs/2407.13168. Friedrichs, Ralf Helbig, Behnoush Hajian, Dawid K. Fiejtek, Florence F. Wagner, Holly H. Soutter, Ashlee M. Earl, Jonathan M. Stokes, Lars D. Renner, and James J. Collins. Discovery of a structural class of antibiotics with explainable deep learning. Nature , 626:177–185, 2024.

[79] Daniil Tiapkin, Denis Belomestny, Daniele Calandriello, Eric Moulines, Remi Munos, Alexey Naumov, Pierre Perrault, Yunhao Tang, Michal Valko, and Pierre Menard. Fast rates for maximum entropy exploration. In International Conference on Machine Learning , pages 34161–34221. PMLR, 2023.

[80] Tuan-Hung Vu, Himalaya Jain, Maxime Bucher, Matthieu Cord, and Patrick Pérez. Advent: Adversarial entropy minimization for domain adaptation in semantic segmentation. In Proceedings of the IEEE/CVF conference on computer vision and pattern recognition , pages 2517–2526, 2019.

[81] Dequan Wang, Evan Shelhamer, Shaoteng Liu, Bruno Olshausen, and Trevor Darrell. Tent: Fully test-time adaptation by entropy minimization. arXiv preprint arXiv:2006.10726 , 2020.

[82] Julian Junyan Wang and Victor Xiaoqi Wang. Assessing consistency and reproducibility in the outputs of large language models: Evidence across diverse finance and accounting tasks. arXiv preprint arXiv:2503.16974 , 2025.

[83] Xuezhi Wang, Jason Wei, Dale Schuurmans, Quoc Le, Ed Chi, Sharan Narang, Aakanksha Chowdhery, and Denny Zhou. Self-consistency improves chain of thought reasoning in language models. arXiv preprint arXiv:2203.11171 , 2022a.

[84] Yiping Wang, Qing Yang, Zhiyuan Zeng, Liliang Ren, Lucas Liu, Baolin Peng, Hao Cheng, Xuehai He, Kuan Wang, Jianfeng Gao, et al. Reinforcement learning for reasoning in large language models with one training example. arXiv preprint arXiv:2504.20571 , 2025.

[85] Yizhong Wang, Yeganeh Kordi, Swaroop Mishra, Alisa Liu, Noah A Smith, Daniel Khashabi, and Hannaneh Hajishirzi. Self-instruct: Aligning language models with self-generated instructions. arXiv preprint arXiv:2212.10560 , 2022b.

[86] Sean Welleck, Amanda Bertsch, Matthew Finlayson, Hailey Schoelkopf, Alex Xie, Graham Neubig, Ilia Kulikov, and Zaid Harchaoui. From decoding to meta-generation: Inference-time algorithms for large language models. arXiv preprint arXiv:2406.16838 , 2024.

[87] Cathy Wu, Aravind Rajeswaran, Yan Duan, Vikash Kumar, Alexandre M Bayen, Sham Kakade, Igor Mordatch, and Pieter Abbeel. Variance reduction for policy gradient with action-dependent factorized baselines. arXiv preprint arXiv:1803.07246 , 2018.

[88] Xin Xu, Qiyun Xu, Tong Xiao, Tianhao Chen, Yuchen Yan, Jiaxin Zhang, Shizhe Diao, Can Yang, and Yang Wang. Ugphysics: A comprehensive benchmark for undergraduate physics reasoning with large language models. arXiv preprint arXiv:2502.00334 , 2025.

[89] An Yang, Beichen Zhang, Binyuan Hui, Bofei Gao, Bowen Yu, Chengpeng Li, Dayiheng Liu, Jianhong Tu, Jingren Zhou, Junyang Lin, et al. Qwen2. 5-math technical report: Toward mathematical expert model via self-improvement. arXiv preprint arXiv:2409.12122 , 2024.

[90] An Yang, Anfeng Li, Baosong Yang, Beichen Zhang, Binyuan Hui, Bo Zheng, Bowen Yu, Chang Gao, Chengen Huang, Chenxu Lv, Chujie Zheng, Dayiheng Liu, Fan Zhou, Fei Huang, Feng Hu, Hao Ge, Haoran Wei, Huan Lin, Jialong Tang, Jian Yang, Jianhong Tu, Jianwei Zhang, Jianxin Yang, Jiaxi Yang, Jing Zhou, Jingren Zhou, Junyang Lin, Kai Dang, Keqin Bao, Kexin Yang, Le Yu, Lianghao Deng, Mei Li, Mingfeng Xue, Mingze Li, Pei Zhang, Peng Wang, Qin Zhu, Rui Men, Ruize Gao, Shixuan Liu, Shuang Luo, Tianhao Li, Tianyi Tang, Wenbiao Yin, Xingzhang Ren, Xinyu Wang, Xinyu Zhang, Xuancheng Ren, Yang Fan, Yang Su, Yichang Zhang, Yinger Zhang, Yu Wan, Yuqiong Liu, Zekun Wang, Zeyu Cui, Zhenru Zhang, Zhipeng Zhou, and Zihan Qiu. Qwen3 technical report, 2025. URL https://arxiv.org/abs/2505.09388 .

[91] Zheng Yuan, Hongyi Yuan, Chengpeng Li, Guanting Dong, Keming Lu, Chuanqi Tan, Chang Zhou, and Jingren Zhou. Scaling relationship on learning mathematical reasoning with large language models. arXiv preprint arXiv:2308.01825 , 2023.

[92] Aohan Zeng, Xiao Liu, Zhengxiao Du, Zihan Wang, Hanyu Lai, Ming Ding, Zhuoyi Yang, Yifan Xu, Wendi Zheng, Xiao Xia, et al. Glm-130b: An open bilingual pre-trained model. arXiv preprint arXiv:2210.02414 , 2022.

[93] Aohan Zeng, Mingdao Liu, Rui Lu, Bowen Wang, Xiao Liu, Yuxiao Dong, and Jie Tang. Agenttuning: Enabling generalized agent abilities for llms. arXiv preprint arXiv:2310.12823 , 2023.

[94] Qingyang Zhang, Yatao Bian, Xinke Kong, Peilin Zhao, and Changqing Zhang. COME: Test-time adaption by conservatively minimizing entropy. In The Thirteenth International Conference on Learning Representations , 2025a. URL https://openreview.net/forum?id=506BjJ1ziZ .

[95] Qingyang Zhang, Haitao Wu, Changqing Zhang, Peilin Zhao, and Yatao Bian. Right question is already half the answer: Fully unsupervised llm reasoning incentivization. arXiv preprint arXiv:2504.05812 , 2025b.

[96] Tianjun Zhang, Xuezhi Wang, Denny Zhou, Dale Schuurmans, and Joseph E Gonzalez. Tempera: Test-time prompting via reinforcement learning. arXiv preprint arXiv:2211.11890 , 2022.

[97] Minjun Zhu, Yixuan Weng, Linyi Yang, and Yue Zhang. Personality alignment of large language models. arXiv preprint arXiv:2408.11779 , 2024.

[98] Brian D Ziebart, Andrew L Maas, J Andrew Bagnell, Anind K Dey, et al. Maximum entropy inverse reinforcement learning. In Aaai , volume 8, pages 1433–1438. Chicago, IL, USA, 2008.

[99] Yuxin Zuo, Kaiyan Zhang, Shang Qu, Li Sheng, Xuekai Zhu, Biqing Qi, Youbang Sun, Ganqu Cui, Ning Ding, and Bowen Zhou. Ttrl: Test-time reinforcement learning. arXiv preprint arXiv:2504.16084 , 2025.

## Appendix A Proof for proposition 1

(Informal) Both adaptive temperature scaling and logit optimization reduce the entropy of a model’s output distribution. However, in high-uncertainty settings (i.e., when the model’s predictive distribution has high entropy), logit optimization can change the order of non-top logits. In contrast, temperature scaling preserves the order of logits and merely sharpens or flattens the distribution proportionally. Both temperature scaling and logit optimization will keep the token with the top logit and increase its probability, making them less likely to change the model’s behavior when it is highly confident.

Part 1: ∀ 𝒛 ∈ ℝ | 𝒱 | \forall{\bm{z}}\in\mathbb{R}^{|\mathcal{V}|} let p ​ ( 𝒛 ) = softmax ​ ( 𝒛 ) p({\bm{z}})=\text{softmax}({\bm{z}}) . Let ℋ ⁡ ( p ) \mathcal{H}(p) denote the entropy of p p ; ℋ = − ∑ i = 1 | 𝒱 | p i log p i \mathcal{H}=-\sum_{i=1}^{|\mathcal{V}|}p_{i}\log p_{i} . ∃ 𝒛 \exists{\bm{z}} , η > 0 \eta>0 and a , b ∈ [ 1 , … , | V | ] a,b\in[1,\dots,|V|] , such that 𝒛 a < 𝒛 b {\bm{z}}_{a}<{\bm{z}}_{b} and 𝒚 a > 𝒚 b {\bm{y}}_{a}>{\bm{y}}_{b} where 𝒚 i = z i + η ​ p i ​ ( log ⁡ p i + ℋ ) {\bm{y}}_{i}=z_{i}+\eta p_{i}(\log p_{i}+\mathcal{H}) , i = 1 , … , | 𝒱 | i=1,\dots,|\mathcal{V}| .

Proof: Consider 𝒚 a − 𝒚 b = 𝒛 a − 𝒛 b + η ⁡ ( g a − g b ) {\bm{y}}_{a}-{\bm{y}}_{b}={\bm{z}}_{a}-{\bm{z}}_{b}+\eta(g_{a}-g_{b}) where g i = p i ​ ( log ⁡ p i + ℋ ) g_{i}=p_{i}(\log p_{i}+\mathcal{H}) . g g is the gradient of entropy ℋ \mathcal{H} w.r.t. 𝒛 {\bm{z}} .

We now show that ∃ 𝒛 , a , b \exists{\bm{z}},a,b such that z a < z b z_{a}<z_{b} and g a > g b g_{a}>g_{b} .

By Mean-Value Theorem ∃ c ∈ ( p a , p b ) \exists c\in(p_{a},p_{b}) such that g a − g b = ( p a − p b ) ​ ( log ⁡ c + ℋ + 1 ) g_{a}-g_{b}=(p_{a}-p_{b})(\log c+\mathcal{H}+1) . When p a − p b < e − ( ℋ + 1 ) p_{a}-p_{b}<e^{-(\mathcal{H}+1)} we have c < p b < e − ( ℋ + 1 ) ⟹ log ⁡ c + ℋ + 1 < 0 ⟹ g a − g b > 0 c<p_{b}<e^{-(\mathcal{H}+1)}\implies\log c+\mathcal{H}+1<0\implies g_{a}-g_{b}>0 (6) Thus, we can set an arbitrary large η \eta such that, z a − z b + η ⁡ ( g a − g b ) > 0 z_{a}-z_{b}+\eta(g_{a}-g_{b})>0 (7)

Part 2: b b cannot be arg ⁡ max i ⁡ z i \arg\max_{i}z_{i} .

Proof: Let j = arg ⁡ max i ⁡ 𝒛 i j=\arg\max_{i}{\bm{z}}_{i} , i.e. the index of the maximum logit. Since p j = max i ⁡ p i p_{j}=\max_{i}p_{i} we can bound it using the inequality: ℋ ( p ) = − ∑ i p i log p i ≥ − log p j ⇒ p j ≥ e − ℋ ⁡ ( p ) ≥ e − ( ℋ ⁡ ( p ) + 1 ) \mathcal{H}(p)=-\sum_{i}p_{i}\log p_{i}\geq-\log p_{j}\quad\Rightarrow\quad p_{j}\geq e^{-\mathcal{H}(p)}\geq e^{-(\mathcal{H}(p)+1)} (8) We now analyze how g i g_{i} behaves as a function of p i p_{i} . Let g ⁡ ( p i ) = p i ​ ( log ⁡ p i + ℋ ) g(p_{i})=p_{i}(\log p_{i}+\mathcal{H}) and g ′ ​ ( p i ) = log ⁡ p i + ℋ + 1 g^{\prime}(p_{i})=\log p_{i}+\mathcal{H}+1 . Thus, g ⁡ ( p i ) g(p_{i}) is monotonically increasing whenever g ′ ​ ( p i ) > 0 g^{\prime}(p_{i})>0 , i.e. when, p i > e − ( ℋ + 1 ) p_{i}>e^{-(\mathcal{H}+1)} (9) So no lower-probability index i i can have g i > g j g_{i}>g_{j} , i.e., the entropy gradient cannot reduce 𝒚 j {\bm{y}}_{j} relative to others. Therefore, b ≠ j b\neq j , leading to the following behavior 0 < g a ≤ g b p a ∈ ( e − ℋ , p b ] \displaystyle 0<g_{a}\leq g_{b}\quad p_{a}\in(e^{-\mathcal{H}},p_{b}] (10) g a < 0 < g b p a ∈ ( 0 , e − ℋ ) \displaystyle g_{a}<0<g_{b}\quad p_{a}\in(0,e^{-\mathcal{H}}) (11)

## Appendix B Adaptive Temperature Scaling

## Appendix C Additional Results

### C.1 Combining EM-INF with Self-consistency and Iterative Self-refinement

We combine EM-INF with self-consistency and iterative self-refinement in Figure 3(a) , 3(b) . Since, EM-INF only optimizes the logits, it can be plugged into both methods easily. We observe that EM-INF can get the same performance as self-consistency (N=4) while using 3 time less FLOPs on AMC with Qwen 2.5 7B. As expected, EM-INF reduces the diversity of the generation, which causes it’s benefits to diminish over iterations. Self-consistency benefits the most when several diverse generations can be produces which lead to the same answer, however, EM-INF reduces diversity through entropy minimization [ 44 , 7 ] leading to smaller benefits with larger compute. EM-INF is most suitable for inference time scaling on high uncertainty tasks under compute bound scenarios.

### C.2 Qualitative analysis of EM-INF on SciCode

We conduct a qualitative analysis of EM-INF on SciCode through a case study where Qwen2.5-7B-Instruct with EM-INF successfully generates the correct code, while the base model fails. The problem and corresponding model generations are illustrated in Figure 4 . The prompt requires generating a symmetric matrix with increasing diagonal values, where each element is modified by the product of a user-defined noise factor and a normally distributed random number, followed by symmetrization via averaging with the matrix’s transpose.

The base Qwen2.5-7B-Instruct model produces a partially correct implementation of the init_matrix function. It correctly initializes the increasing diagonal and applies the symmetrization formula ( A = (A + A.T) / 2 ). However, it fails to apply the noise factor to all elements of the matrix. Specifically, the noise modification is applied only to the off-diagonal elements, leaving the diagonal entries (e.g., i+1 ) unaltered by the stochastic process prior to symmetrization. This error occurs because scientific coding is a difficult task where both coding and domain knowledge is required, therefore making the model’s output distribution uncertain.

By contrast, the generation using EM-INF produces the correct implementation that adheres to all constraints specified in the prompt. EM-INF reduces the entropy of the output distribution, which leads to more deterministic generations. The generated code by EM-INF , as expected, reduces the diversity in generation, leading to more concise implementations and omitting additional comments. These results suggest that EM-INF is particularly beneficial for scientific coding tasks like SciCode, where correctness and determinism are critical.

Math Coding Math AMC AIME Minerva Olymp. Avg. LeetC LiveC Avg. Qwen2.5-7b 43.8 31.3 15.6 14.7 19.0 24.9 26.1 18.4 22.3 Trained using 60K labeled prompts w/ SFT 48.2 30.2 10.0 17.6 22.4 25.7 18.3 18.3 18.3 w/ RLOO 73.0 57.8 23.3 31.2 34.2 43.9 28.3 26.7 27.5 w/ GRPO 71.8 56.6 21.1 25.0 35.9 42.1 25.0 25.8 25.4 Our unsupervised methods trained on 60K unlabeled prompts EM-FT w KL ( N = 4 N=4 ) 66.4 53.0 21.1 33.5 34.5 41.7 26.7 16.8 21.8 EM-FT w KL ( N = 1 N=1 ) 65.6 54.2 16.7 26.8 34.8 39.6 28.3 13.7 21.0 EM-FT w/o KL ( N = 1 N=1 ) 67.2 51.8 14.4 33.1 34.4 40.2 28.3 17.2 22.8

## Appendix D Experimental Setup

### D.1 Evaluation Benchmarks

#### D.1.1 Math Reasoning

We adopted the data and evaluation pipeline from PRIME-RL codebase [ 13 ] for all math reasoning evaluations. The final answer of LM is the string inside the last \ b ​ o ​ x ​ e ​ d ​ { } \backslash boxed\{\} . All math benchmarks is evaluated on Pass@1 accuracy. Here, we will introduce each math benchmarks in detail.

##### MATH 500

MATH 500 contains 500 prompts sampled from the 5,000 test problems in the original MATH dataset [ 29 ] . The test set of MATH comprises challenging competition-style math problems drawn from sources such as the AMC and AIME exams. These problems span seven subjects—Prealgebra, Algebra, Number Theory, Counting and Probability, Geometry, Intermediate Algebra, and Precalculus—and are labeled with difficulty levels from 1 (easiest) to 5 (hardest). Each test problem includes a final boxed answer and a full step-by-step solution in LaTeX, enabling exact match evaluation and providing interpretable reasoning paths for model analysis.

##### AMC

We use the validation set from AI-MO’s AMC dataset [ 43 ] , which contains 83 problems extracted from AMC 12 (2022 and 2023). The AMC dataset comprises math competition problems from the American Mathematics Competitions (AMC), covering a broad range of topics including arithmetic, geometry, combinatorics, and algebra. It is designed to evaluate a language model’s capacity for mathematical reasoning, abstraction, symbolic manipulation, and logical deduction.

##### AIME

We use the validation set from AI-MO’s AIME dataset [ 43 ] , which includes 90 problems drawn from AIME 22, AIME 23, and AIME 24. The AIME (American Invitational Mathematics Examination) dataset features high-difficulty problems intended for top-performing students from the AMC competitions. These problems typically require advanced mathematical reasoning across topics such as algebraic manipulation, number theory, combinatorics, and geometry. Each problem involves multiple intermediate steps and provides minimal guidance, making the dataset well-suited for evaluating a language model’s ability to perform multi-step symbolic reasoning and maintain logical coherence throughout extended problem-solving chains.

##### Minerva Math

Minerva Math refers to the OCWCourses evaluation dataset introduced in the Minerva paper [ 42 ] . This dataset comprises 272 undergraduate-level STEM problems sourced from MIT OpenCourseWare (OCW), covering topics such as solid-state chemistry, information theory and entropy, differential equations, and special relativity. Each problem is self-contained and accompanied by a clearly defined final answer—either numeric (191 problems) or symbolic (81 problems)—enabling automatic evaluation. The dataset is designed to assess a language model’s ability to perform multi-step scientific reasoning, including the application of domain-specific knowledge, symbolic manipulation, and precise quantitative computation.

##### OlympiadBench

OlympiadBench [ 28 ] is a large-scale bilingual multimodal benchmark comprising 8,476 Olympiad-level mathematics and physics problems sourced from international competitions such as the IMO and IPhO, as well as elite Chinese contests and Gaokao mock exams. The dataset evaluates LLMs on advanced mathematical and physical reasoning tasks, including multi-step logical deduction, symbolic manipulation, equation solving, theorem proving, and visual-spatial understanding from diagrams. Its high difficulty, multimodal diversity, and expert-level content make it a rigorous benchmark for assessing scientific reasoning capabilities. In this work, we use the open-ended, English, text-only subset of math competition problems as our evaluation set, which contains a total of 674 problems.

#### D.1.2 Coding

##### LeetCode

LeetCode benchmark is introduced in the technical report of DeepSeek-Coder [ 26 ] . This benchmark consists of 180 recent competition-level programming problems from LeetCode, collected between July 2023 and January 2024. Each problem is paired with 100 test cases to ensure comprehensive coverage, and prompts are constructed in a standardized format to simulate realistic coding challenges. This dataset evaluates a language model’s ability to perform code generation in competitive programming settings, testing a wide range of capabilities such as problem comprehension, algorithm design, logic reasoning, and implementation precision. The inclusion of varying difficulty levels (Easy, Medium, Hard) allows for a thorough assessment of a model’s generalization and problem-solving skills under pressure. During evaluation, the python code will be extracted from model’s response and run the test cases. Performance is reported using the Pass@1 metric, indicating the proportion of problems for which the model’s first generated solution passes all test cases.

##### LiveCodeBench

LiveCodeBench [ 34 ] is a large-scale, contamination-free benchmark designed to holistically evaluate the code-related capabilities of large language models. It comprises 612 recent coding problems collected from competitive programming platforms such as LeetCode, AtCoder, and Codeforces between May 2023 and August 2024. Unlike traditional benchmarks that focus solely on code generation, LiveCodeBench assesses four key skills: (1) code generation from natural language, (2) self-repair using error feedback, (3) code execution via output prediction, and (4) test output prediction without implementation. This comprehensive setup evaluates not only functional correctness but also a model’s ability to debug, reason about program behavior, and construct tests. Its time-segmented evaluation protocol further supports rigorous detection of training data contamination. In this work, we adopt the V2 release, which includes 511 problems released between May 2023 and May 2024. We evaluate methods on the code generation ability. The model is given a natural language problem description and tasked with generating a correct program. Correctness is evaluated by passing all test cases. The Pass@1 metric is used, measuring the fraction of problems where the first generated solution passes all tests.

#### D.1.3 Scientific Reasoning

##### UGPhysics

UGPhysics [ 88 ] is a large-scale bilingual benchmark designed to evaluate undergraduate-level physics reasoning in large language models. It comprises 5,520 problems (11,040 including both English and Chinese versions) spanning 13 physics subjects and 59 topics, featuring diverse answer formats such as numerical values, symbolic expressions, equations, and intervals. Each problem is annotated with one of four reasoning skill types: Knowledge Recall, Laws Application, Math Derivation, and Practical Application. Unlike prior benchmarks that primarily target multiple-choice or high-school-level content, UGPhysics emphasizes deeper problem-solving and derivation skills, requiring LLMs to perform symbolic reasoning, apply physical laws, and handle real-world quantities. This dataset is designed to assess LLMs’ ability to carry out multi-step physics reasoning beyond simple mathematical manipulation. In this work, we evaluate on the Semiconductor Physics subset, which consists of 372 problems. During evaluation, models answer physics problems using prompts tailored to different answer types for improved extraction and judgment. A rule-based correctness assessment then extracts answers from the model’s output and reports accuracy.

##### SciCode

SciCode [ 78 ] is a challenging, scientist-curated benchmark designed to evaluate large language models (LLMs) on real-world scientific coding tasks across 16 subfields in mathematics, physics, chemistry, biology, and materials science. It comprises 80 complex main problems, each decomposed into multiple subproblems (338 in total), requiring models to integrate domain-specific scientific knowledge, reasoning, and Python programming. Each problem includes gold-standard solutions and test cases, with optional expert-authored background context. SciCode assesses LLMs’ abilities in multi-step problem decomposition, code synthesis from scientific instructions, and integration of partial solutions. By emphasizing scientific reasoning and simulating real-world workflows, it provides a rigorous benchmark for evaluating LLMs as scientific assistants. In our paper, we evaluate methods on the test set, which contains 65 main problems and 288 subproblems in total. Models generate Python functions for each subproblem and integrate them into a complete solution. Evaluation is fully automatic, using gold test cases for both subproblems and main problems. The evaluation is conducted with and without scientific background information, as well as using gold or generated prior solutions, to measure realistic performance. Success requires all subproblems and the main solution to be correct. Final accuracy is reported as the percentage of problems achieving success.

#### D.1.4 Individualistic Value Reasoning

##### IndVal

The IndVal dataset [ 36 ] is derived from the World Values Survey (WVS) and consists of natural language statements expressing individual human values and preferences from over 93,000 participants worldwide. Each participant responds to 253 questions grouped into 13 distinct categories, including Social Values, Economic Values, and Science & Technology, among others. The dataset standardizes these diverse survey responses into over 900 value-expressing statements per individual, enabling evaluation of language models’ ability to reason about individualistic human values in a bottom-up, granular manner. This dataset is particularly valuable as it challenges models to understand and predict nuanced personal value judgments beyond demographic stereotypes. Consequently, it reveals limitations in current language models’ capacity for individual value reasoning and promotes more equitable, personalized AI alignment that respects individual diversity. In our work, we randomly sampled 200 individuals excluded from training, uniformly distributed across all continents. For each individual, we randomly selected 4 statements per question category to form an individualistic value profile consisting of 52 known statements. Then, for each question category, we selected 2 statements not included in the known profile and asked the language model to select the most appropriate statement from the given candidates based on the individual profile. This process resulted in an evaluation dataset containing 5,400 prompts. During evaluation, the selected statement is extracted from the model generation and compared with the ground truth. Final performance is reported as accuracy.

### D.2 Training Data

##### Math Reasoning

We randomly sampled 35K prompts from Numina math training set [ 43 ] as our math training prompts. The NuminaMath dataset contains 860,000 problems ranging from high-school to advanced competition levels, including Olympiad, AMC, AIME, and Chinese K-12 math problems.

##### Coding

We randomly sampled 25K prompts from Eurus-2-RL training dataset’s coding split [ 13 ] as our coding training prompts. The Eurus-2-RL training dataset is a high-quality reinforcement learning dataset consisting of about 457,000 math problems and 27,000 coding problems with outcome verifiers such as LaTeX answers for math and test cases for coding. The math problems are sourced from the NuminaMath-CoT dataset, which covers a wide range from Chinese high school math to International Mathematical Olympiad-level questions. The dataset is carefully cleaned, filtered, and reformatted into a direct question-answer format to ensure high quality and solvability. It is especially useful for training because it provides diverse, verified, and challenging problems covering different level of difficulties and tasks.

##### Individualistic Value Reasoning

The training dataset is derived from the IndVal dataset [ 36 ] . We sampled 900 individuals uniformly across seven continents. For each individual, we randomly selected 4 statements per question category to form an individualistic value profile comprising 52 known statements. Then, we sampled 6 questions per question category as queries, resulting in a total of 70,200 training prompts.

### D.3 Models

##### Qwen2.5 Family

For the entropy minimization for post-training experiments, we use two models derived from the Qwen2.5 family: Qwen2.5-Math-7B [ 89 ] and Eurus-2-7B-SFT [ 13 ] . Qwen2.5-Math-7B is selected as the base model for math reasoning tasks. We apply various post-training methods using the math training dataset and evaluate their performance on math reasoning benchmarks. This model serves as an excellent starting point for our experiments due to its strong capability in tackling complex mathematical reasoning problems. Eurus-2-7B-SFT is a SFT checkpoint obtained by further fine-tuning Qwen2.5-Math-7B on the Eurus-2-SFT-Data from PRIME-RL [ 13 ] , which is an action-centric chain-of-thought reasoning dataset. Since Eurus-2-7B-SFT further enhances the reasoning abilities of Qwen2.5-Math-7B, we select it for coding experiments, applying different post-training methods with the coding training dataset and evaluating on coding benchmarks.

For entropy minimization during inference time experiments, we select Qwen2.5-Math-7B-Instruct and Qwen2.5-7B-Instruct as the base models for math reasoning, coding, and scientific reasoning tasks because of their inherent instruction-following and reasoning abilities. Specifically, for SciCode, we include a more powerful model, Qwen2.5-32B-Instruct, due to its superior capability in handling complex problems, allowing us to evaluate the performance of EM-INF on stronger models.

##### Llama-3.1 Family

Llama-3.1 [ 24 ] is the second model family included in this work to ensure the generalizability of our methods across different models. For both the entropy minimization post-training and inference-time experiments, we select Llama-3.1-8B-Instruct as the base model.

### D.4 FLOPs Computation

Following [ 63 , 37 ] , we estimate the training FLOPs as 6 ​ P ​ D 6PD and inference FLOPs as 2 ​ P ​ D 2PD where P P is the number of parameters in the model and D D is the number of tokens. We use early stopping based on the validation set accuracy for all methods, which significantly changes the FLOPs utilized. • EM-FT: On each training step, we sample one trajectory from the model costing 2 ​ P ​ n 2Pn where n n is the sequence length followed by training costing 6 ​ P ​ n 6Pn . The total cost per step is thus 8 ​ P ​ n 8Pn . We set sequence length to 4096 4096 , batch size to 512 512 and the training early stops at 40 40 gradient steps costing 1.01 × 10 17 1.01\times 10^{17} FLOPs for a 7B parameter model.

• EM-RL, GRPO, RLOO: None of the methods use a reward model. We use GRPO and RLOO with output verification only. We sample N = 4 N=4 trajectories costing 8 ​ P ​ n 8Pn , then we make a forward pass on the reference model costing another 8 ​ P ​ n 8Pn followed by training costing 24 ​ P ​ n 24Pn . The total training cost per step is thus 40 ​ P ​ n 40Pn . We set sequence length to 4096 4096 , batch size to 512 512 and the training early stops at 100 100 gradient steps costing 13 × 10 17 13\times 10^{17} FLOPs for a 7B parameter model.

## Instructions for reporting errors

We are continuing to improve HTML versions of papers, and your feedback helps enhance accessibility and mobile support. To report errors in the HTML that will help us improve conversion and rendering, choose any of the methods listed below:

Click the "Report Issue" ( ) button, located in the page header.

Tip: You can select the relevant text first, to include it in your report.

Our team has already identified the following issues . We appreciate your time reviewing and reporting rendering errors we may not have found yet. Your efforts will help us improve the HTML versions for all readers, because disability should not be a barrier to accessing research. Thank you for your continued support in championing open access for all.

Have a free development cycle? Help support accessibility at arXiv! Our collaborators at LaTeXML maintain a list of packages that need conversion , and welcome developer contributions .
