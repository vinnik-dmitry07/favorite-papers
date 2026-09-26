##### Report GitHub Issue

Content selection saved. Describe the issue below:

# Reinforced Efficient Reasoning via Semantically Diverse Exploration

###### Abstract

Reinforcement learning with verifiable rewards (RLVR) has proven effective in enhancing the reasoning of large language models (LLMs). Monte Carlo Tree Search (MCTS)-based extensions improve upon vanilla RLVR (e.g., GRPO) by providing tree-based reasoning rollouts that enable fine-grained and segment-level credit assignment. However, existing methods still suffer from limited exploration diversity and inefficient reasoning. To address the above challenges, we propose r einforced efficient reas o ning via s emantically diverse e xplorations, i.e., ROSE , for LLMs. To encourage more diverse reasoning exploration, our method incorporates a semantic-entropy-based branching strategy and an ε \varepsilon -exploration mechanism. The former operates on already sampled reasoning rollouts to capture semantic uncertainty and select branching points with high semantic divergence to generate new successive reasoning paths, whereas the latter stochastically initiates reasoning rollouts from the root, preventing the search process from becoming overly local. To improve efficiency, we design a length-aware segment-level advantage estimator that rewards concise and correct reasoning while penalizing unnecessarily long reasoning chains. Extensive experiments on various mathematical reasoning benchmarks with Qwen and Llama models validate the effectiveness and efficiency of ROSE. Codes are available at https://github.com/ZiqiZhao1/ROSE-rl .

## 1 Introduction

Reinforcement learning with verifiable rewards (RLVR) has recently been proposed to enhance the reasoning of large language models (LLMs) in verifiable settings, including mathematical reasoning and code generation Guo et al. (2025) ; Shao et al. (2024) ; Liu et al. (2025) ; Yu et al. (2025) . Typical RLVR algorithms, such as GRPO Guo et al. (2025) ; Shao et al. (2024) and its variants Yu et al. (2025) ; Liu et al. (2025) , estimate the advantage of an entire rollout response based on the verified reward and uniformly propagate this advantage to all tokens within the response.

While the uniform credit assignment is simple yet effective, it constrains the learning potential of the model and conflicts with human intuition. For example, a reasoning chain that produces an incorrect response may still contain certain correct steps. Moreover, recent studies have indicated that this training paradigm may lead to “overthinking”, in which models are engaged in redundant reasoning Chen et al. (2024) ; Dai et al. (2025) ; Nie et al. (2026) . To further improve model performance, a more effective credit assignment approach is to employ Monte Carlo Tree Search (MCTS) Kocsis and Szepesvári (2006) during response rollout sampling. Unlike vanilla GRPO, which generates a group of independent responses for a given problem, MCTS enables the model to produce responses in a tree-based structure, as illustrated in Figure 1(a) , allowing segment-level credit assignment by computing value differences between parent and child nodes.

Despite the progress achieved by MCTS-based RLVR algorithms Li et al. (2025) ; Yang et al. (2025b) ; Zheng et al. (2025b) ; Dong et al. (2025) , limited exploration diversity and inefficient reasoning still exist. Specifically, most existing work uses generation entropy as the criterion for MCTS branching Zheng et al. (2025b) ; Dong et al. (2025) . These methods first identify the position with the highest generation entropy. Then, tokens preceding this position are kept fixed, and successive tokens are regenerated. Although generation entropy measures a policy’s uncertainty over token selection in the current action space, this metric does not generalize well to the semantic space. Figure 1(b) shows a case study of generation entropy-based branching. The tokens can in response 1 and need in response 2 correspond to the positions of highest entropy in two separate generations, yet their semantic meanings are largely the same, and the subsequent reasoning in both responses is identical (highlighted in blue). Furthermore, although response 2 and response 3 follow different reasoning paths after branching, they are semantically similar, and their subsequent reasoning remains consistent with other responses (highlighted in green). This indicates that current methods fail to generate semantically diverse rollouts. Additionally, existing MCTS-based methods do not address the overthinking problem effectively, and current approaches for efficient reasoning either incur performance degradation or offer trivial performance gains Dai et al. (2025) ; Arora and Zanette (2025) . How to achieve both improved performance and efficient reasoning based on MCTS remains an open question.

To address the aforementioned challenges, we propose r einforced efficient reas o ning via s emantically diverse e xplorations, i.e., ROSE , for LLMs. To address the first challenge, we introduce a semantic-entropy-based branching strategy together with an ε \varepsilon -exploration mechanism. The semantic entropy metric, defined over differences in token semantics, identifies positions along a reasoning path where the model exhibits high uncertainty in the semantic space, thereby guiding the exploration toward more diverse reasoning paths. In addition, to prevent the search process from becoming overly local, the ε \varepsilon -exploration mechanism stochastically regenerates the reasoning rollout from scratch. Together, these methods promote more diverse and effective exploration. To address the second challenge, we integrate credit assignment with the length of the reasoning chain. Leveraging the tree structure, we estimate values for each node and assign credit at the segment level. For different correct reasoning chains originating from the same node, longer chains with deeper depth are penalized to encourage more efficient reasoning. These components make fuller use of MCTS samples, aiming to enhance the model’s reasoning ability through more diverse and efficient exploration. In summary, our contributions are: • We introduce a semantic-entropy guided MCTS-based rollout strategy together with an ϵ \epsilon -exploration mechanism, which enables more diverse exploration compared with existing approaches.

• We propose a segment-level advantage estimation method that incorporates reasoning length, enabling stronger performance while producing more efficient reasoning.

• Extensive experiments on a wide range of mathematical reasoning tasks (AIME2025, AIME2024, AMC2023, MATH500), using both Qwen and Llama models, validate the effectiveness and efficiency of our approach.

## 2 Related Work

### 2.1 Reinforcement Learning for LLMs

Reinforcement learning has been widely adopted to align LLMs with human preferences through reinforcement learning from human feedback (RLHF) Lee et al. (2024) ; Ouyang et al. (2022) . More recently, reinforcement learning with verifiable rewards (RLVR) has emerged as an effective approach for enhancing the reasoning ability of LLMs Guo et al. (2025) ; Shao et al. (2024) ; Dai et al. (2025) ; Hao et al. (2025) ; Zhou et al. (2026) ; Wu et al. (2026) ; Xie et al. (2025) ; Wu et al. (2025b) ; An et al. (2025) . By using rule-based binary (0/1) rewards to simplify reward design, GRPO Guo et al. (2025) ; Shao et al. (2024) removes the need for training an extra critic model compared with vanilla PPO Schulman et al. (2017) , leading to a substantial reduction in RL training overhead. Recent studies, including DAPO Yu et al. (2025) , Dr.GRPO Liu et al. (2025) , VAPO Yue et al. (2025) , GSPO Zheng et al. (2025a) , and CPG Chu et al. (2025) , have explored improving the GRPO loss function to further enhance its reasoning capability. In contrast to these approaches, our work focuses on improving the rollout process to enable more diverse exploration and credit assignment, without modifying the loss function. As a result, the proposed method is in principle compatible with a wide range of GRPO-based algorithms.

### 2.2 MCTS for LLM Reasoning

Monte Carlo Tree Search (MCTS) Kocsis and Szepesvári (2006) ; Świechowski et al. (2023) offers a principled framework for exploring structured decision spaces, making it a natural candidate for performing credit assignment based on the intermediate reasoning steps. Recent studies have explored MCTS-based sampling in RL training, showing progress on mathematical reasoning tasks Li et al. (2025) ; Yang et al. (2025b) ; Zheng et al. (2025b) as well as other complex problems Ji et al. (2025) ; Dong et al. (2025) .

A key challenge in applying MCTS lies in deciding where to branch, as this choice fundamentally determines the exploration trajectory and the quality of the reasoning. Prior approaches rely on random branching Ji et al. (2025) , generation-entropy-based branching Dong et al. (2025) ; Zheng et al. (2025b) , branching based on fixed-length segments Li et al. (2025) , or performing branching during decoding via beam search Yang et al. (2025b) . However, all these strategies fall short in promoting sufficient diverse exploration. Meanwhile, existing methods do not explicitly account for the impact of reasoning length during advantage estimation, which can lead to overthinking during model inference. In contrast, our approach enhances exploration diversity and enables more efficient reasoning, leading to improved performance on complex reasoning tasks.

## 3 Method

This section details ROSE. We first introduce how to achieve effective and diverse exploration in Section 3.1 . Section 3.2 then describes how tree-based exploration is leveraged to perform advantage estimation and encourage efficient reasoning. Finally, Section 3.3 presents the overall learning objective. Figure 2 illustrates an overview of ROSE.

### 3.1 Semantic-Entropy Guided Exploration

Given a question q q , vanilla GRPO performs rollouts by sampling a group of independent responses { 𝐨 i } i = 1 G \{\mathbf{o}_{i}\}_{i=1}^{G} . In contrast, MCTS-based methods introduce tree-structured rollouts, allowing different responses to share common prefix tokens. The key to tree-based rollout is identifying appropriate branching positions, which encourages the model to perform more effective exploration. A common practice is to use generation entropy to determine branching positions Dong et al. (2025) ; Zheng et al. (2025b) . Generation entropy provides a principled measure of the uncertainty of a policy π θ \pi_{\theta} , i.e., the LLM, over its action space, i.e., the vocabulary 𝒱 \mathcal{V} . Given a question q q and a generated response 𝐨 i \mathbf{o}_{i} , the generation entropy of the policy at position k k is defined as: ℋ k = − ∑ v ∈ 𝒱 p θ ( v | q , 𝐨 i , < k ) log p θ ( v | q , 𝐨 i , < k ) \mathcal{H}_{k}=-\sum_{v\in\mathcal{V}}p_{\theta}(v|q,\mathbf{o}_{i,<k})\log p_{\theta}(v|q,\mathbf{o}_{i,<k}) (1) where p θ ​ ( v | q , 𝐨 i , < k ) p_{\theta}(v|q,\mathbf{o}_{i,<k}) represents the probability distribution over the vocabulary 𝒱 \mathcal{V} at position k k . Such entropy has been widely used in traditional RL Haarnoja et al. (2018) ; Wang et al. (2022) , where different actions often exhibit significant differences, such as movement directions in a game environment Bellemare et al. (2013) . However, this assumption does not always hold in language generation. Consider the two words can and need in Figure 1(b) . When the LLM is uncertain about which one to select, the generation entropy may be high. From a semantic perspective, however, this choice is actually well-determined, as both words serve the same functional role of indicating modal intent. As a result, the responses branched from this position may exhibit extremely high similarity, and in some cases even follow identical subsequent trajectories, thereby limiting the potential for more diverse exploration.

Based on this observation, we design an additional metric to evaluate the semantic divergence among the current candidate tokens. Specifically, given a question q q and a generated response 𝐨 i \mathbf{o}_{i} , at position k k , we first select the top-20 tokens from 𝒱 \mathcal{V} with the highest probabilities to form the set 𝒱 k \mathcal{V}_{k} for efficiency. Then, for each token v i ∈ 𝒱 k v_{i}\in\mathcal{V}_{k} , its corresponding embedding 𝐞 v i \mathbf{e}_{v_{i}} is obtained from the LLM. We then compute semantic divergence as the sum of pairwise similarities between all tokens in 𝒱 k \mathcal{V}_{k} , weighted by their probabilities:

S D k = − ∑ v i , v j ∈ 𝒱 k p θ ( v i | q , 𝐨 i , < k ) p θ ( v j | q , 𝐨 i , < k ) ⋅ cos ⟨ 𝐞 v i , 𝐞 v j ⟩ SD_{k}=\displaystyle-\sum_{v_{i},v_{j}\in\mathcal{V}_{k}}p_{\theta}(v_{i}|q,\mathbf{o}_{i,<k})p_{\theta}(v_{j}|q,\mathbf{o}_{i,<k})\cdot\cos\langle\mathbf{e}_{v_{i}},\mathbf{e}_{v_{j}}\rangle

where cos ⁡ ⟨ 𝐞 v i , 𝐞 v j ⟩ \cos\langle\mathbf{e}_{v_{i}},\mathbf{e}_{v_{j}}\rangle represents the cosine similarity between the embeddings of tokens v i v_{i} and v j v_{j} . The key idea of semantic divergence is that when the high-probability tokens exhibit large semantic differences, the current position becomes an ideal branching point, leading to more distinct subsequent reasoning paths.

Finally, we define semantic entropy as the product of generation entropy and semantic divergence, and use it as the branching indicator: S ​ E k = S ​ D k ⋅ ℋ k SE_{k}=SD_{k}\cdot\mathcal{H}_{k} (3) This combined measure captures both probabilistic uncertainty and semantic dispersion, allowing ROSE to more accurately identify positions where alternative continuations are more likely to lead to genuinely diverse reasoning paths.

The rollout process based on branching metrics is summarized as follows. Given a question q q , a complete response is first generated. For each position in the generated response, the proposed branching metric is computed, and the position with the highest value is selected. Then a new response is regenerated at this position, keeping the preceding part of the response unchanged. The corresponding metric of the newly generated sequence is computed, and the selection is then performed on all existing rollout responses. The whole process is repeated until the number of generated responses reaches the predefined parameter G G .

In addition, inspired by the ε \varepsilon -greedy Sutton et al. (1998) strategy in reinforcement learning, we propose an ε \varepsilon -exploration mechanism. Specifically, before generating each response, there is an ε \varepsilon probability of generating the response from scratch, i.e., rolling out an independent response; otherwise, the rollout follows the proposed semantic-entropy-based branching strategy. This mechanism prevents the search from becoming overly focused on local regions and further balances the depth and breadth of exploration. After completing the rollout process for a given query, we can obtain a tree structure, an example of which is shown on the left side of Figure 2 . During rollout, we apply dynamic sampling Yu et al. (2025) to remove groups whose responses receive identical rewards, improving efficiency. The proposed methods offer an effective exploration-exploitation tradeoff to better search the reasoning paths for LLMs.

### 3.2 Advantage Estimation

Based on the tree-structured exploration, we perform segment-level credit assignment through (1) node value assignment, (2) segment advantage estimation and (3) length-aware calibration.

Node value assignment. After completing tree-structured sampling, a single response may contain multiple branching nodes. Including the start and the terminal positions, these nodes partition a response into several consecutive segments. Formally, for a response 𝐨 i \mathbf{o}_{i} to a given question q q , let b 0 , b 1 , … , b k {b_{0},b_{1},\dots,b_{k}} denote the node positions, where b 0 b_{0} is the start position, b 1 , … , b k − 1 b_{1},\dots,b_{k-1} correspond to the pivot positions immediately before each branching point, and b k b_{k} is the leaf (terminal) position. The response can then be decomposed as 𝐨 i = ⋃ j = 1 k 𝐨 i , b j − 1 < t ≤ b j , with ​ b 0 = 0 , b k = | 𝐨 i | \mathbf{o}_{i}=\bigcup_{j=1}^{k}\mathbf{o}_{i,b_{j-1}<t\leq b_{j}},\text{with }b_{0}=0,b_{k}=|\mathbf{o}_{i}| (4) Under this partition, each segment is initiated at either the start position or a branching position selected based on maximal semantic entropy observed during the rollout stage. For a pivot node b j b_{j} with 0 < j < k 0<j<k , we define the set of responses that contain this node as: Ω b j = { 𝐨 m | 𝐨 m ​ traverses the pivot node ​ b j } \Omega_{b_{j}}=\{\mathbf{o}_{m}|\mathbf{o}_{m}\text{ traverses the pivot node }b_{j}\} (5) For the start node b 0 b_{0} , we define Ω b 0 \Omega_{b_{0}} as the set of all responses, i.e., Ω b 0 = { 𝐨 m } m = 1 G \Omega_{b_{0}}=\{\mathbf{o}_{m}\}_{m=1}^{G} . For the leaf node, we define Ω b k \Omega_{b_{k}} as the set of 𝐨 i \mathbf{o}_{i} , i.e., Ω b k = { 𝐨 i } \Omega_{b_{k}}=\{\mathbf{o}_{i}\} .

Next, we define the value of node b j b_{j} with 0 ≤ j ≤ k 0\leq j\leq k as the average reward of responses in Ω b j \Omega_{b_{j}} . V ^ ​ ( b j ) = 1 | Ω b j | ​ ∑ 𝐨 m ∈ Ω b j r ⁡ ( 𝐨 m ) \hat{V}(b_{j})=\frac{1}{|\Omega_{b_{j}}|}\sum_{\mathbf{o}_{m}\in\Omega_{b_{j}}}r(\mathbf{o}_{m}) (6) where r ⁡ ( ) r() denotes a rule-based reward function that evaluates the correctness of each response and assigns a binary reward (1 for correct and 0 for incorrect).

Segment advantage estimation. Next, we can compute the segment-level advantage between two nodes based on the values assigned to the nodes. According to the definition of node value, the value of a node can be interpreted as the probability of deriving a correct reasoning chain starting from that node. Therefore, the reasoning contribution of the segment is quantified by the difference between the two node values. Specifically, for any token 𝐨 i , t ∈ 𝐨 i \mathbf{o}_{i,t}\in\mathbf{o}_{i} with b j − 1 < t ≤ b j b_{j-1}<t\leq b_{j} , the advantage of 𝐨 i , t \mathbf{o}_{i,t} is defined as: A ^ i , t = V ^ ​ ( b j ) − V ^ ​ ( b j − 1 ) \hat{A}_{i,t}=\hat{V}(b_{j})-\hat{V}(b_{j-1}) (7)

Length-aware calibration. Furthermore, although multiple reasoning paths may lead to correct outcomes, we aim to encourage the model to adopt more efficient reasoning and avoid overthinking. To this end, we apply a length-aware calibration to the advantages of responses that are correct but require an excessive number of tokens. Specifically, we first identify the shortest correct response 𝐨 s \mathbf{o}_{s} . Then, for every other correct response 𝐨 c \mathbf{o}_{c} , we locate the pivot node b c b_{c} at which 𝐨 s \mathbf{o}_{s} and 𝐨 c \mathbf{o}_{c} diverge. That is, prior to b c b_{c} , the two responses share an identical subsequence 𝐨 s , ≤ b c = 𝐨 c , ≤ b c \mathbf{o}_{s,\leq b_{c}}=\mathbf{o}_{c,\leq b_{c}} , whereas after b c b_{c} they follow distinct continuations 𝐨 s , > b c \mathbf{o}_{s,>b_{c}} and 𝐨 c , > b c \mathbf{o}_{c,>b_{c}} , respectively. A length-proportional calibration is then applied to the longer response, thereby encouraging the model to produce more efficient reasoning. Specifically, for each token 𝐨 c , t ∈ 𝐨 c \mathbf{o}_{c,t}\in\mathbf{o}_{c} with t > b c t>b_{c} , its advantage is updated according to the following rule: A ^ i , t ← A ^ i , t − | A ^ i , t | ⋅ ( 1 − ( | 𝐨 s | − b c | 𝐨 c | − b c ) α ) \hat{A}_{i,t}\leftarrow\hat{A}_{i,t}-|\hat{A}_{i,t}|\cdot(1-(\frac{|\mathbf{o}_{s}|-b_{c}}{|\mathbf{o}_{c}|-b_{c}})^{\alpha}) (8) where α \alpha is a hyperparameter controlling the extent of the adjustment. The ratio | 𝐨 s | − b c | 𝐨 c | − b c \frac{|\mathbf{o}_{s}|-b_{c}}{|\mathbf{o}_{c}|-b_{c}} measures the relative lengths of the two reasoning branches after their divergence at b c b_{c} . Since the two responses share an identical reasoning prefix before b c b_{c} , their post-divergence segments can be directly compared: the more efficient branch receives a higher advantage, while the longer branch incurs a length-proportional adjustment.

### 3.3 Model Training

We adopt the improved modifications of vanilla GRPO’s optimizing objective proposed in Dr.GRPO Liu et al. (2025) as the training objective, together with a KL penalty term:

ℒ ROSE ​ ( θ ) = − 1 G ∑ i = 1 G ∑ t = 1 | 𝐨 i | ( min ( r i , t ( θ ) A ^ i , t , [ r i , t ( θ ) ] 1 − ϵ ′ 1 + ϵ ′ A ^ i , t ) − β D KL ( π θ ∥ π ref ) ) , \begin{aligned} \mathcal{L}_{\text{ROSE }}(\theta)&=-\frac{1}{G}\sum_{i=1}^{G}\sum_{t=1}^{|\mathbf{o}_{i}|}\Bigg(\min\Big(r_{i,t}(\theta)\hat{A}_{i,t},[r_{i,t}(\theta)]_{1-\epsilon^{\prime}}^{1+\epsilon^{\prime}}\hat{A}_{i,t}\Big)\\ \hskip 0.0pt&-\beta D_{\text{KL}}(\pi_{\theta}\|\pi_{\text{ref}})\Bigg),\end{aligned}

where

π old \pi_{\text{old}} denotes sampling model, π ref \pi_{\text{ref}} denotes reference model and operator [ r i , t ​ ( θ ) ] 1 − ϵ ′ 1 + ϵ ′ [r_{i,t}(\theta)]_{1-\epsilon^{\prime}}^{1+\epsilon^{\prime}} clips the ratio to [ 1 − ϵ ′ , 1 + ϵ ′ ] [1-\epsilon^{\prime},1+\epsilon^{\prime}] .

## 4 Experimental Setup

### 4.1 Datasets and Metrics

For the training dataset, following prior studies Zhu et al. (2025) ; Liu et al. (2025) , we use MATH Hendrycks et al. (2021) , which contains 7,500 problems. For evaluation, four publicly available standard mathematical reasoning benchmarks are considered, including AIME2024, AIME2025, AMC23, and MATH500. MATH500 is a subset of the test split of the MATH dataset, consisting of 500 problems. During validation, we sample 8 responses for each question and adopt pass@8 as the primary metric for assessing the performance of model reasoning. pass@ k k measures whether at least one of the k k sampled responses correctly solves a given problem. Unlike prior work that relies on the mean@ k k metric Li et al. (2025) ; Yang et al. (2025b) , which reflects the average accuracy across all samples, pass@ k k more effectively captures the model’s ability to solve previously challenging problems that it might fail to answer.

### 4.2 Model and Baselines

To provide a more comprehensive comparison of the proposed method, we evaluate it using backbone models from two model families, Qwen and Llama, with different parameter scales, including Llama-3.2-3B-Instruct Grattafiori et al. (2024) , Qwen3-4B-Base , and Qwen3-8B-Base Yang et al. (2025a) . The Qwen3 models have two modes (thinking and non-thinking), and the non-thinking mode is adopted for both training and inference.

Comparisons are performed between ROSE and existing approaches, which mainly fall into two categories: GRPO-based variants and MCTS-based methods. The GRPO-based variants include vanilla GRPO Guo et al. (2025) ; Shao et al. (2024) , Dr.GRPO Liu et al. (2025) , and DAPO Yu et al. (2025) . Dr.GRPO computes advantages as deviations from the group mean, without variance normalization, and removes the length normalization term from the loss function. DAPO improves GRPO by incorporating techniques such as clip-higher and rejection sampling.

The MCTS-based baselines include FR3E Zheng et al. (2025b) and TreePO Li et al. (2025) . FR3E is a representative MCTS-based method that determines branching positions based on generation entropy and adopts a two-step framework for segment-level advantage computation. Besides, TreePO structures the rollout process as a tree by branching at fixed-length segments and computes advantages over the resulting sub-trees.

### 4.3 Implementation Details

All experiments are conducted using the VeRL framework Sheng et al. (2025) in this paper. For RL training, we set the batch size to 512, the number of rollouts per prompt as G = 8 G=8 , the learning rate to 1 × 10 − 6 1\times 10^{-6} , the clipping ratio as ϵ ′ = 0.2 \epsilon^{\prime}=0.2 , the KL divergence coefficient as β = 0.001 \beta=0.001 , and the maximum number of training epochs to 8. For evaluation, the temperature is set to 0.6, top- p p sampling is applied with p = 0.95 p=0.95 , and 8 candidate responses are sampled per prompt. Prompts whose lengths exceed 2048 tokens are filtered out, and the maximum generation length is set to 4096 tokens. The probability of generating the response from scratch ε \varepsilon is set to 0.5 by default, and the coefficient for length-aware calibration α \alpha is searched from { 0.5 , 1 , 2 , 3 } \{0.5,1,2,3\} . Our experiments are conducted on 8 × \times NVIDIA A800 (80G) GPUs.

## 5 Experimental Results

### 5.1 Overall Performance

Accuracy evaluation. Table 1 presents the experimental results of all methods. It can be observed that ROSE achieves substantial improvements over the strongest baseline in most settings. DAPO and Dr.GRPO are variants that modify the GRPO loss function. However, they do not yield consistent or substantial improvements, with performance gains observed only in certain scenarios, such as models with larger parameter scales. Among MCTS-based approaches, TreePO and FR3E achieve performance comparable to GRPO and its variants. In particular, TreePO yields pronounced improvements on the in-domain dataset MATH500 but performs worse on other benchmarks. This suggests that its fixed-length branching strategy fails to induce more diverse reasoning trajectories during exploration, limiting out-of-domain generalization.

For ROSE, significant performance gains are first observed on more challenging tasks, indicating that the method facilitates more divergent exploration during the rollout phase, which is beneficial for solving difficult problems. In addition, ROSE consistently yields notable improvements across different model scales. Larger models typically encapsulate richer knowledge, and the proposed approach appears to leverage this capacity more effectively, resulting in greater performance gains. Finally, recent studies have suggested that models in the Qwen family may suffer from potential data leakage Wu et al. (2025a) . Nevertheless, comparable performance gains are also observed on Llama models of similar parameter scales, indicating that the improvements are not confined to a specific model family.

Learning dynamics. Figure 3 presents the learning curves of GRPO and ROSE. Across different model scales, ROSE exhibits a clear performance improvement over the vanilla GRPO. Moreover, as the model scale increases, the learning curves of ROSE become noticeably more stable. After convergence, ROSE maintains stable and competitive performance, whereas the vanilla GRPO shows noticeable fluctuations and fails to achieve significant improvements in small-scale ( 3B and 4B ) models.

### 5.2 Branching Metric Analysis

Performance comparison. Table 2 presents the experimental results for three different branching metrics (entropy, semantic divergence, and semantic entropy). For all branching metrics, the probability ε \varepsilon is fixed to 0.5. The results show that entropy achieves performance comparable to vanilla GRPO, indicating that it fails to effectively distinguish uncertain regions in the model’s reasoning trajectories. In contrast, both semantic divergence and semantic entropy yield consistent improvements over entropy, with semantic entropy exhibiting greater robustness across different datasets.

Analysis of reasoning diversity. To further analyze the differences among branching metrics, we conduct a quantitative analysis of the diversity of responses generated during the rollout phase under different branching metrics. Specifically, for a fixed batch of questions, rollouts are performed using different metrics, and the pairwise cosine similarity between embeddings of multiple responses corresponding to the same question is computed. The embeddings are obtained using the Qwen-text-embedding-v4 model. The resulting similarity distributions are visualized using kernel density estimation (KDE), as shown in Figure 4 .

As illustrated in the figure, the distributions induced by our methods exhibit lower peaks and heavier tails. The mean similarities of semantic entropy and semantic divergence are comparable and both are lower than those of entropy, indicating a higher degree of dispersion among generated responses. Such increased reasoning diversity encourages broader exploration of the solution space, which aligns with the observed performance gains on more challenging benchmarks.

### 5.3 Reasoning Efficiency Analysis

To investigate whether ROSE can achieve more efficient reasoning, we evaluate different values of the hyperparameter α \alpha and report the corresponding pass@8 scores and reasoning lengths. The averaged results across the four datasets are presented in Table 3 .

The results show a clear trend that increasing α \alpha reduces the reasoning length while maintaining strong pass@8 performance. In particular, moderate values of α \alpha (e.g., α = 1 \alpha=1 or α = 2 \alpha=2 ) yield the best trade-off between accuracy and efficiency, achieving higher pass@8 scores together with substantial reductions in reasoning length. Even with a relatively large value of α \alpha (i.e., α = 10 \alpha=10 ), our method still consistently outperforms GRPO variants in terms of pass@8. Overall, these results demonstrate that ROSE enables more efficient reasoning without sacrificing task performance. The evolution of response length across training steps is presented in Appendix 5.6 .

### 5.4 Ablation Study

An ablation study is conducted to analyze the contribution of each component, with the results presented in Table 4 . (1) w/o ε \varepsilon -exploration removes the ε \varepsilon -possibility branching mechanism (i.e., ε \varepsilon = 0), which results in consistent performance drops across all backbone models, indicating that the model tends to fall into overly local exploration and loses exploration diversity. Additional results examining different values of ε \varepsilon are provided in Appendix 5.7 . (2) w/ random branching randomly determines the branching positions during rollout, which leads to performance degradation, indicating that the semantic entropy metric can effectively identify uncertain points along the reasoning trajectories. (3) w/o advantage estimation removes the segment-level advantage estimation and instead directly uses the GRPO advantage formulation and loss function. This modification leads to degraded performance, which suggests that segment-level advantage estimation plays an important role in shaping learning signals during reasoning.

### 5.5 Case Study

We also conduct case studies and observe that our semantic-entropy-based approach can identify semantical uncertain positions along the reasoning paths, encouraging more diverse reasoning. Detailed examples are provided in the Appendix A .

### 5.6 Response Length Dynamics

To further investigate the effect of the hyperparameter α \alpha , we examine how the average response length per prompt during the rollout stage and the evaluation stage evolves over training steps, with the results presented in Figure 5 . We observe that as α \alpha increases, the generated response lengths in both the rollout and evaluation stages decrease substantially, and are consistently shorter than those of Dr.GRPO and GRPO. This indicates that our method can effectively regulate the generation length by adjusting α \alpha , thereby enabling more efficient reasoning.

### 5.7 Impact of ε \varepsilon -exploration

We investigate the impact of different values of ε \varepsilon in ε \varepsilon -exploration on model performance, with the results reported in Table 5 . When ε = 1 \varepsilon=1 , i.e., each rollout is sampled independently, our method degenerates into the Dr.GRPO algorithm. We observe that, across all backbone models, performance first improves and then degrades as ε \varepsilon increases. When ε = 0 \varepsilon=0 , exploration becomes overly local, which hinders diversity in the model’s exploration. Conversely, when ε = 1 \varepsilon=1 , the tree-structured exploration is lost, preventing effective segment-level advantage estimation.

## 6 Conclusion

In this work, we presented ROSE, a novel reinforcement learning framework designed to enhance both the reasoning accuracy and efficiency of LLMs. Specifically, to encourage more diverse reasoning exploration, our method incorporates a semantic-entropy-based branching strategy alongside an ε \varepsilon -exploration mechanism. Simultaneously, to improve efficiency, we design a length-aware segment-level advantage estimator that promotes concise reasoning paths. Extensive experiments across various mathematical benchmarks validate that ROSE significantly outperforms state-of-the-art baselines in both effectiveness and efficiency.

## Limitations

Our work mainly has two limitations. First, our experiments were conducted on models with up to 8B parameters, and we plan to investigate the scalability on larger architectures (e.g., 14B) in future work. Second, we primarily focused on mathematical reasoning tasks. In the future, we plan to extend our approach to other domains, such as code generation and question answering.

## Ethical Considerations

This work aims to enhance the reasoning capabilities of LLMs. We acknowledge that advanced reasoning abilities could potentially be misused for malicious purposes, and we advocate for the deployment of these models alongside robust safety alignment protocols to mitigate such risks. Regarding the experimental setup, all datasets utilized in this work are open-source and publicly available. We have strictly adhered to their respective licenses and ensured that our usage is consistent with their intended purposes.

## References

An et al. (2025) S. An, X. Cai, X. Cao, X. Li, Y. Lin, J. Liu, X. Lv, D. Ma, X. Wang, Z. Wang, et al. Amo-bench: large language models still struggle in high school math competitions . arXiv preprint arXiv:2510.26768 . Cited by: §2.1 .

Arora and Zanette (2025) D. Arora and A. Zanette Training language models to reason efficiently . arXiv preprint arXiv:2502.04463 . Cited by: §1 .

Bellemare et al. (2013) M. G. Bellemare, Y. Naddaf, J. Veness, and M. Bowling The arcade learning environment: an evaluation platform for general agents . Journal of artificial intelligence research 47 , pp. 253–279 . Cited by: §3.1 .

Chen et al. (2024) X. Chen, J. Xu, T. Liang, Z. He, J. Pang, D. Yu, L. Song, Q. Liu, M. Zhou, Z. Zhang, et al. Do not think that much for 2+ 3=? on the overthinking of o1-like llms . arXiv preprint arXiv:2412.21187 . Cited by: §1 .

Chu et al. (2025) X. Chu, H. Huang, X. Zhang, F. Wei, and Y. Wang Gpg: a simple and strong reinforcement learning baseline for model reasoning . arXiv preprint arXiv:2504.02546 . Cited by: §2.1 .

Dai et al. (2025) M. Dai, C. Yang, and Q. Si S-grpo: early exit via reinforcement learning in reasoning models . arXiv preprint arXiv:2505.07686 . Cited by: §1 , §1 , §2.1 .

Dong et al. (2025) G. Dong, H. Mao, K. Ma, L. Bao, Y. Chen, Z. Wang, Z. Chen, J. Du, H. Wang, F. Zhang, et al. Agentic reinforced policy optimization . arXiv preprint arXiv:2507.19849 . Cited by: §1 , §2.2 , §2.2 , §3.1 .

Grattafiori et al. (2024) A. Grattafiori, A. Dubey, A. Jauhri, A. Pandey, A. Kadian, A. Al-Dahle, A. Letman, A. Mathur, A. Schelten, A. Vaughan, et al. The llama 3 herd of models . arXiv preprint arXiv:2407.21783 . Cited by: §4.2 .

Guo et al. (2025) D. Guo, D. Yang, H. Zhang, J. Song, R. Zhang, R. Xu, Q. Zhu, S. Ma, P. Wang, X. Bi, et al. Deepseek-r1: incentivizing reasoning capability in llms via reinforcement learning . arXiv preprint arXiv:2501.12948 . Cited by: §1 , §2.1 , §4.2 .

Haarnoja et al. (2018) T. Haarnoja, A. Zhou, P. Abbeel, and S. Levine Soft actor-critic: off-policy maximum entropy deep reinforcement learning with a stochastic actor . In International conference on machine learning , pp. 1861–1870 . Cited by: §3.1 .

Hao et al. (2025) Z. Hao, H. Wang, H. Liu, J. Luo, J. Yu, H. Dong, Q. Lin, C. Wang, and J. Chen Rethinking entropy interventions in rlvr: an entropy change perspective . arXiv preprint arXiv:2510.10150 . Cited by: §2.1 .

Hendrycks et al. (2021) D. Hendrycks, C. Burns, S. Kadavath, A. Arora, S. Basart, E. Tang, D. Song, and J. Steinhardt Measuring mathematical problem solving with the math dataset . NeurIPS . Cited by: §4.1 .

Ji et al. (2025) Y. Ji, Z. Ma, Y. Wang, G. Chen, X. Chu, and L. Wu Tree search for llm agent reinforcement learning . arXiv preprint arXiv:2509.21240 . Cited by: §2.2 , §2.2 .

Kocsis and Szepesvári (2006) L. Kocsis and C. Szepesvári Bandit based monte-carlo planning . In European conference on machine learning , pp. 282–293 . Cited by: §1 , §2.2 .

Lee et al. (2024) H. Lee, S. Phatale, H. Mansoor, T. Mesnard, J. Ferret, K. R. Lu, C. Bishop, E. Hall, V. Carbune, A. Rastogi, et al. RLAIF vs. rlhf: scaling reinforcement learning from human feedback with ai feedback . In International Conference on Machine Learning , pp. 26874–26901 . Cited by: §2.1 .

Li et al. (2025) Y. Li, Q. Gu, Z. Wen, Z. Li, T. Xing, S. Guo, T. Zheng, X. Zhou, X. Qu, W. Zhou, et al. Treepo: bridging the gap of policy optimization and efficacy and inference efficiency with heuristic tree-based modeling . arXiv preprint arXiv:2508.17445 . Cited by: §1 , §2.2 , §2.2 , §4.1 , §4.2 .

Liu et al. (2025) Z. Liu, C. Chen, W. Li, P. Qi, T. Pang, C. Du, W. S. Lee, and M. Lin Understanding r1-zero-like training: a critical perspective . arXiv preprint arXiv:2503.20783 . Cited by: §1 , §2.1 , §3.3 , §4.1 , §4.2 .

Nie et al. (2026) S. Nie, S. Ding, W. Zhang, L. Yu, T. Yang, Y. Chen, T. Liu, W. Yin, Y. Sun, and H. Wu ATTNPO: attention-guided process supervision for efficient reasoning . arXiv preprint arXiv:2602.09953 . Cited by: §1 .

Ouyang et al. (2022) L. Ouyang, J. Wu, X. Jiang, D. Almeida, C. Wainwright, P. Mishkin, C. Zhang, S. Agarwal, K. Slama, A. Ray, et al. Training language models to follow instructions with human feedback . Advances in neural information processing systems 35 , pp. 27730–27744 . Cited by: §2.1 .

Schulman et al. (2017) J. Schulman, F. Wolski, P. Dhariwal, A. Radford, and O. Klimov Proximal policy optimization algorithms . arXiv preprint arXiv:1707.06347 . Cited by: §2.1 .

Shao et al. (2024) Z. Shao, P. Wang, Q. Zhu, R. Xu, J. Song, X. Bi, H. Zhang, M. Zhang, Y. Li, Y. Wu, et al. Deepseekmath: pushing the limits of mathematical reasoning in open language models . arXiv preprint arXiv:2402.03300 . Cited by: §1 , §2.1 , §4.2 .

Sheng et al. (2025) G. Sheng, C. Zhang, Z. Ye, X. Wu, W. Zhang, R. Zhang, Y. Peng, H. Lin, and C. Wu Hybridflow: a flexible and efficient rlhf framework . In Proceedings of the Twentieth European Conference on Computer Systems , pp. 1279–1297 . Cited by: §4.3 .

Sutton et al. (1998) R. S. Sutton A. G. Barto et al. Reinforcement learning: an introduction . Vol. 1 , MIT press Cambridge . Cited by: §3.1 .

Świechowski et al. (2023) M. Świechowski, K. Godlewski, B. Sawicki, and J. Mańdziuk Monte carlo tree search: a review of recent modifications and applications . Artificial Intelligence Review 56 ( 3 ), pp. 2497–2562 . Cited by: §2.2 .

Wang et al. (2022) X. Wang, S. Wang, X. Liang, D. Zhao, J. Huang, X. Xu, B. Dai, and Q. Miao Deep reinforcement learning: a survey . IEEE Transactions on Neural Networks and Learning Systems 35 ( 4 ), pp. 5064–5078 . Cited by: §3.1 .

Wu et al. (2026) F. Wu, Z. Zhang, Q. Chang, J. Zhang, Q. Liu, and J. Du Step potential advantage estimation: harnessing intermediate confidence and correctness for efficient mathematical reasoning . arXiv preprint arXiv:2601.03823 . Cited by: §2.1 .

Wu et al. (2025a) M. Wu, Z. Zhang, Q. Dong, Z. Xi, J. Zhao, S. Jin, X. Fan, Y. Zhou, H. Lv, M. Zhang, et al. Reasoning or memorization? unreliable results of reinforcement learning due to data contamination . arXiv preprint arXiv:2507.10532 . Cited by: §5.1 .

Wu et al. (2025b) Z. Wu, J. Yang, J. Liu, X. Wu, C. Pan, J. Zhang, Y. Zhao, S. Song, Y. Li, and Z. Li Table-r1: region-based reinforcement learning for table understanding . arXiv preprint arXiv:2505.12415 . Cited by: §2.1 .

Xie et al. (2025) C. Xie, R. Pan, X. Wu, Y. Zhang, J. Fu, T. Gao, and G. Zhou Unlocking exploration in rlvr: uncertainty-aware advantage shaping for deeper reasoning . arXiv preprint arXiv:2510.10649 . Cited by: §2.1 .

Yang et al. (2025a) A. Yang, A. Li, B. Yang, B. Zhang, B. Hui, B. Zheng, B. Yu, C. Gao, C. Huang, C. Lv, et al. Qwen3 technical report . arXiv preprint arXiv:2505.09388 . Cited by: §4.2 .

Yang et al. (2025b) Z. Yang, Z. Guo, Y. Huang, X. Liang, Y. Wang, and J. Tang TreeRPO: tree relative policy optimization . arXiv preprint arXiv:2506.05183 . Cited by: §1 , §2.2 , §2.2 , §4.1 .

Yu et al. (2025) Q. Yu, Z. Zhang, R. Zhu, Y. Yuan, X. Zuo, Y. Yue, W. Dai, T. Fan, G. Liu, L. Liu, et al. Dapo: an open-source llm reinforcement learning system at scale . arXiv preprint arXiv:2503.14476 . Cited by: §1 , §2.1 , §3.1 , §4.2 .

Yue et al. (2025) Y. Yue, Y. Yuan, Q. Yu, X. Zuo, R. Zhu, W. Xu, J. Chen, C. Wang, T. Fan, Z. Du, et al. Vapo: efficient and reliable reinforcement learning for advanced reasoning tasks . arXiv preprint arXiv:2504.05118 . Cited by: §2.1 .

Zheng et al. (2025a) C. Zheng, S. Liu, M. Li, X. Chen, B. Yu, C. Gao, K. Dang, Y. Liu, R. Men, A. Yang, et al. Group sequence policy optimization . arXiv preprint arXiv:2507.18071 . Cited by: §2.1 .

Zheng et al. (2025b) T. Zheng, T. Xing, Q. Gu, T. Liang, X. Qu, X. Zhou, Y. Li, Z. Wen, C. Lin, W. Huang, et al. First return, entropy-eliciting explore . arXiv preprint arXiv:2507.07017 . Cited by: §1 , §2.2 , §2.2 , §3.1 , §4.2 .

Zhou et al. (2026) Y. Zhou, Y. Li, D. Cheng, H. Fan, and Y. Cheng Look inward to explore outward: learning temperature policy from llm internal states via hierarchical rl . arXiv preprint arXiv:2602.13035 . Cited by: §2.1 .

Zhu et al. (2025) X. Zhu, M. Xia, Z. Wei, W. Chen, D. Chen, and Y. Meng The surprising effectiveness of negative reinforcement in llm reasoning . arXiv preprint arXiv:2506.01347 . Cited by: §4.1 .

## Appendix A Case Study

To more comprehensively investigate the differences between entropy-based branching and semantic-entropy–based branching, we present a case study, with the results of the two methods shown in Figure 6 and Figure 7 , respectively. Specifically, given a question, we use Llama-3.2-3B-Instruct as the backbone model to generate a complete response. We then apply two different methods to determine the branching positions based on this response and regenerate accordingly, ultimately forming a group of responses.

From Figure 6 , we observe that all responses generated by the entropy-based branching method produce incorrect answers. Notably, the shared prefix among these responses already contains an erroneous calculation (highlighted in blue). However, the branching position identified by entropy-based branching occurs after this point, which consequently propagates the incorrect reasoning into the subsequent generations.

In contrast, our proposed semantic-entropy–based branching method performs branching before the erroneous calculation (highlighted in blue), enabling more fine-grained reasoning that avoids this error. Although subsequent reasoning errors may still occur (e.g., response 2 in Figure 7 ), branching is again triggered prior to the error, ultimately yielding a correct response (e.g., response 3 in Figure 7 ). This case study demonstrates that our method can more accurately identify regions of higher uncertainty in the model’s reasoning trajectory, thereby encouraging more diverse and effective reasoning paths.

## Instructions for reporting errors

We are continuing to improve HTML versions of papers, and your feedback helps enhance accessibility and mobile support. To report errors in the HTML that will help us improve conversion and rendering, choose any of the methods listed below:

Click the "Report Issue" ( ) button, located in the page header.

Tip: You can select the relevant text first, to include it in your report.

Our team has already identified the following issues . We appreciate your time reviewing and reporting rendering errors we may not have found yet. Your efforts will help us improve the HTML versions for all readers, because disability should not be a barrier to accessing research. Thank you for your continued support in championing open access for all.

Have a free development cycle? Help support accessibility at arXiv! Our collaborators at LaTeXML maintain a list of packages that need conversion , and welcome developer contributions .
