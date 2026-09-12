##### Report GitHub Issue

Content selection saved. Describe the issue below:

# Reinforcement Learning for Reasoning in Large Language Models with One Training Example

###### Abstract

We show that reinforcement learning with verifiable reward using one training example ( 1-shot RLVR ) is effective in incentivizing the mathematical reasoning capabilities of large language models (LLMs). Applying RLVR to the base model Qwen2.5-Math-1.5B, we identify a single example that elevates model performance on MATH500 from 36.0% to 73.6% (8.6% improvement beyond format correction), and improves the average performance across six common mathematical reasoning benchmarks from 17.6% to 35.7% (7.0% non-format gain). This result matches the performance obtained using the 1.2k DeepScaleR subset (MATH500: 73.6%, average: 35.9%), which contains the aforementioned example. Furthermore, RLVR with only two examples even slightly exceeds these results (MATH500: 74.8%, average: 36.6%). Similar substantial improvements are observed across various models (Qwen2.5-Math-7B, Llama3.2-3B-Instruct, DeepSeek-R1-Distill-Qwen-1.5B), RL algorithms (GRPO and PPO), and different math examples. In addition, we identify some interesting phenomena during 1-shot RLVR, including cross-category generalization, increased frequency of self-reflection, and sustained test performance improvement even after the training accuracy has saturated, a phenomenon we term post-saturation generalization . Moreover, we verify that the effectiveness of 1-shot RLVR primarily arises from the policy gradient loss, distinguishing it from the "grokking" phenomenon. We also show the critical role of promoting exploration (e.g., by incorporating entropy loss with an appropriate coefficient) in 1-shot RLVR training. We also further discuss related observations about format correction, label robustness and prompt modification. These findings can inspire future work on RLVR efficiency and encourage a re-examination of recent progress and the underlying mechanisms in RLVR. Our code, models, and data are open source at https://github.com/ypwang61/One-Shot-RLVR .

## 1 Introduction

Recently, significant progress has been achieved in enhancing the reasoning capabilities of large language models (LLMs), including OpenAI-o1 [ 1 ] , DeepSeek-R1 [ 2 ] , and Kimi-1.5 [ 3 ] , particularly for complex mathematical tasks. A key method contributing to these advancements is Reinforcement Learning with Verifiable Reward (RLVR) [ 4 , 5 , 2 , 3 ] , which commonly employs reinforcement learning on an LLM with a rule-based outcome reward, such as a binary reward indicating the correctness of the model’s final answer to a math problem. Several intriguing empirical phenomena have been observed in RLVR, such as the stimulation or enhancement of specific cognitive behaviors [ 6 ] (e.g., self-reflection) and improved generalization across various downstream tasks [ 5 , 2 , 3 ] .

Currently, substantial efforts are directed toward refining RL algorithms (e.g., PPO [ 7 ] and GRPO [ 8 ] ) to further enhance RLVR’s performance and stability [ 9 , 10 , 11 , 12 , 13 , 14 , 15 , 16 ] . Conversely, data-centric aspects of RLVR remain relatively underexplored. Although several studies attempt to curate high-quality mathematical reasoning datasets [ 17 , 18 , 11 ] , there is relatively limited exploration into the specific role of data in RLVR. Thus, critical questions remain open: How much data is truly necessary? What data is most effective? How do the quality and quantity of the training data relate to observed empirical phenomena (e.g., self-reflection and robust generalization)? The most relevant study to these problems is LIMR [ 19 ] , which proposed a metric called learning impact measurement (LIM) to evaluate the effectiveness of training examples. Using the LIM score, they maintain model performance while reducing the number of training examples by sixfold. However, this study does not explore how aggressively the RLVR training dataset can be reduced. Motivated by these considerations, in this paper, we specifically investigate the following research question:

"To what extent can we reduce the training dataset for RLVR while maintaining comparable performance compared to using the full dataset?"

We empirically demonstrate that, surprisingly, the training dataset for RLVR can be reduced to as little as ONE example! This finding supports recent claims that base models already possess significant reasoning capabilities [ 13 , 20 , 6 , 21 ] , and further shows that a single example is sufficient to substantially enhance the base model’s mathematical performance. We refer to this setup as 1-shot RLVR . We summarize our contributions and findings below:

• We find that selecting one specific example as the training dataset can achieve similar downstream performance to that of the 1.2k DeepScaleR subset (DSR-sub) containing that example. Specifically, this improves the Qwen2.5-Math-1.5B model from 36.0% to 73.6% on MATH500, and from 17.6% to 35.7% on average across 6 mathematical reasoning benchmarks, including non-trivial improvements beyond format correction (Fig. 1 ). Notably, these two examples are relatively easy for the base model, which can solve them with high probability without any training (Sec. 3.2.1 ). Additionally, 1-shot RLVR on math examples can improve model performance on non-mathematical reasoning tasks, even outperforming full-set RLVR (Tab. 1 ).

• We confirm the effectiveness of 1(few)-shot RLVR across different base models (Qwen2.5-Math-1.5/7B, Llama3.2-3B-Instruct), models distilled from long Chain-of-Thought (CoT) data (DeepSeek-R1-Distill-Qwen-1.5B), and different RL algorithms (GRPO, PPO).

• We highlight an intriguing phenomenon in 1-shot RLVR: post-saturation generalization. Specifically, the training accuracy on the single example rapidly approaches 100%, yet the model’s test accuracy continues to improve. Moreover, despite using only one training example, overfitting does not occur until after approximately 1.4k training steps. Even post-overfitting, while the model’s reasoning outputs for the training example become incomprehensible multilingual gibberish mixed with correct solutions, its test performance remains strong, and the reasoning outputs for the test examples remain human-interpretable.

• In addition, we demonstrate the following phenomena: (1) 1-shot RLVR is viable for many examples in the full dataset when each example is individually used for training. We also discuss its connection with format correction in Appendix C.2.3 . (2) 1-shot RLVR enables cross-category generalization: training on a single example from one category (e.g., Geometry) often enhances performance in other categories (e.g., Algebra, Number Theory). (3) As 1-shot RLVR training progresses, both the response length for the training example and the frequency of self-reflective terms in downstream tasks increase.

• Through ablation studies, we show that policy gradient loss primarily drives the improvements observed in 1-shot RLVR, distinguishing it from “grokking”, which heavily depends on regularization methods like weight decay. Additionally, we emphasize the importance of promoting diverse exploration in model outputs, showing that adding an entropy loss with an appropriate coefficient further enhances performance.

• Lastly, we find that employing entropy loss alone, even without any outcome reward, yields a performance boost, although it remains weaker than the format-reward baseline. Similar improvements are observed for Qwen2.5-Math-7B and Llama-3.2-3B-Instruct. We also discuss label robustness and prompt modification in RLVR (Appendix C.2 ).

## 2 Preliminary

##### RL Loss Function.

In this paper, we adopt GRPO [ 8 , 2 ] as the RL algorithm for LLMs unless stated otherwise. We briefly introduce three main components in the loss function as below and provide more details in Appendix B.1 .

(1) Policy gradient loss : it encourages the model to produce responses with higher rewards, assigning weights according to their group-normalized advantages. Thus, better-than-average solutions are reinforced, whereas inferior ones are penalized. Since we focus on mathematical problems, the reward is defined as binary (0-1), where a reward of 1 is granted only when the outcome of the model’s response correctly matches the ground truth. We do not include the format reward when using the outcome reward , but format-reward RLVR is used as a baseline for Qwen models. Further discussion can be found in Appendix C.2.3 .

(2) KL loss : it helps to maintain general language quality by measuring the divergence between current model’s responses and those from reference model.

(3) Entropy loss [ 22 ] : applied with a negative coefficient, it incentivizes higher per-token entropy to encourage exploration and generate more diverse reasoning paths. We note that entropy loss is not strictly necessary for GRPO training, but it is included by default in verl [ 22 ] used in our experiments. Its effect on 1-shot RLVR is discussed in Sec. 4.1 .

##### Data Selection: Historical Variance Score.

To explore how extensively we can reduce the RLVR training dataset, we propose a simple data selection approach for ranking training examples. We first train the model for E E epochs on the full dataset using RLVR. Then for each example i ∈ [ N ] = { 1 , … , N } i\in[N]=\{1,\ldots,N\} , we can obtain a list of historical training accuracy L i = [ s i , 1 , … , s i , E ] L_{i}=[s_{i,1},\ldots,s_{i,E}] , which records its average training accuracy for every epoch. Note that some previous work has shown that the variance of the reward signal [ 23 ] is critical for RL training, we simply rank the data by their historical variance of training accuracy, which is directly related to the reward: v i := var ​ ( s i , 1 , … , s i , E ) v_{i}:=\text{var}(s_{i,1},\ldots,s_{i,E}) (1) Next, we define a permutation π : [ N ] → [ N ] \pi:[N]\to[N] such that v π ⁡ ( 1 ) ≥ ⋯ ≥ v π ⁡ ( N ) . v_{\pi(1)}\geq\cdots\geq v_{\pi(N)}. Under this ordering, π ⁡ ( j ) \pi(j) (denoted as π j \pi_{j} for convenience) corresponds to the example with the j j -th largest variance v i v_{i} : π j := π ⁡ ( j ) = arg ​ sort j ⁡ { v l : l ∈ [ N ] } \pi_{j}:=\pi(j)=\operatorname*{arg\,sort}_{j}\{v_{l}:l\in[N]\} (2) We then select examples according to this straightforward ranking criterion. For instance, π 1 \pi_{1} , identified by the historical variance score on Qwen2.5-Math-1.5B, performs well in 1-shot RLVR (Sec. 3.2.3 , 3.3 ). We also choose additional examples from diverse categories among { π 1 , … , π 17 } \{\pi_{1},\ldots,\pi_{17}\} and evaluate them under 1-shot RLVR (Tab. 3 ), finding that π 13 \pi_{13} likewise achieves strong performance. Importantly, we emphasize that this criterion is not necessarily optimal for selecting single examples for 1-shot RLVR 1 1 1 Nevertheless, as shown in Tab. 4 (Sec. 3.3 ), selection based on historical variance scores outperforms random selection in RLVR on Qwen2.5-Math-7B. . In fact, Tab. 3 shows that many examples, including those with moderate or low historical variance, can individually produce improvements on MATH500 when used as a single training example in RLVR. This suggests a potentially general phenomenon that is independent of the specific data selection method.

## 3 Experiments

### 3.1 Setup

Models. We by default run our experiments on Qwen2.5-Math-1.5B [ 24 , 25 ] , and also verify the effectiveness of Qwen2.5-Math-7B [ 25 ] , Llama-3.2-3B-Instruct [ 26 ] , and DeepSeek-R1-Distill-Qwen-1.5B [ 2 ] for 1-shot RLVR in Sec. 3.3 . We also include the results of Qwen2.5-1.5B and Qwen2.5-Math-1.5B-Instruct in Appendix C.1.2 .

Dataset. Due to resource limitations, we randomly select a subset consisting of 1209 examples from DeepScaleR-Preview-Dataset [ 18 ] as our instance pool (“DSR-sub”). For data selection (Sec. 2 ), as described in Sec. 2 , we first train Qwen2.5-Math-1.5B for 500 steps, and then obtain its historical variance score (Eqn. 1 ) and the corresponding ranking (Eqn. 2 ) on the examples. To avoid ambiguity, we do not change the correspondence between { π i } i = 1 1209 \{\pi_{i}\}_{i=1}^{1209} and examples for all the experiments, i.e., they are all ranked by the historical variance score of Qwen2.5-Math-1.5B. We also use the MATH [ 27 ] training set (consisting of 7500 instances) as another dataset in full RLVR to provide a comparison. More details are in Appendix B.2 .

Training. As described in Sec. 2 , we follow the verl [ 22 ] pipeline, and by default, the coefficients for KL divergence and entropy loss are β = 0.001 \beta=0.001 and α = − 0.001 \alpha=-0.001 , respectively. The training rollout temperature is set to 0.6 for vLLM [ 28 ] . The training batch size and mini-batch size are 128 2 2 2 Note that verl sets drop_last =True for training dataloader, so the dataset must be at least as large as the training batch size. To enable RLVR with very few examples, we duplicate the selected example until reaching 128 samples and store them as a new dataset. , and we sample 8 responses for each prompt. Therefore, we have 8 gradient updates for each rollout step. By default, the maximum prompt length is 1024, and the maximum response length is 3072, considering that Qwen2.5-Math-1.5B/7B’s context length are 4096. For a fairer comparison on Qwen models, we include the format-reward baseline, which assigns a reward of 1 if and only if the final answer can be parsed from the model output (see Appendix C.2.3 for details). More details are in Appendix B.4 .

Evaluation. We use the official Qwen2.5-Math evaluation pipeline [ 25 ] for our evaluation. Six widely used complex mathematical reasoning benchmarks are used in our paper: MATH500 [ 27 , 29 ] , AIME 2024 [ 30 ] , AMC 2023 [ 31 ] , Minerva Math [ 32 ] , OlympiadBench [ 33 ] , and AIME 2025 [ 30 ] . We also consider non-mathematical reasoning tasks ARC-Easy and ARC-Challenge [ 34 ] . More details about benchmarks are in Appendix B.3 . For AIME 2024, AIME 2025, and AMC 2023, which contain only 30 or 40 questions, we repeat the test set 8 times for evaluation stability and evaluate the model with temperature = 0.6, and finally report the average pass@1 ( avg@8 ) performance. And for other 3 mathematical benchmarks, we let temperature be 0. The evaluation setup for DeepSeek-R1-Distill-Qwen-1.5B and other evaluation details are provided in Appendix B.5 .

### 3.2 Observation of 1/Few-Shot RLVR

In Fig. 1 , we have found that RLVR with 1 or 2 examples can perform as well as RLVR with thousands of examples, yielding significant improvements in both format and non-format aspects. Tab. 1 further shows that 1(few)-shot RLVR with these math examples enable better generalization on non-mathematical reasoning tasks (More details are in Appendix C.1 ). To better understand this phenomenon, we provide a detailed analysis of 1-shot RLVR in this section.

#### 3.2.1 Dissection of π 1 \pi_{1} : A Not-So-Difficult Problem

First, we inspect the examples that produce such strong results. Tab. 2 lists the instances of π 1 \pi_{1} , which is defined by Eqn. 2 . We can see that it’s actually an algebra problem with a physics background. The key steps for it are obtaining k = 1 / 256 k=1/256 for formula P = k ​ A ​ V 3 P=kAV^{3} , and calculating V = ( 2048 ) 1 / 3 ≈ 12.699 V=(2048)^{1/3}\approx 12.699 . Interestingly, we note that base model already almost solves π 1 \pi_{1} . In Fig. 3 , the base model without any training already solves all the key steps before calculating ( 2048 ) 1 / 3 (2048)^{1/3} with high probability 3 3 3 A more precise answer for π 1 \pi_{1} should be 12.7 12.7 rather than 12.8 12.8 , but this slight deviation does not affect the experimental results. We show that both values yield strong performance in Tab. 5 in Sec. 4.1 . . Just for the last step to calculate the cube root, the model has diverse outputs, including 4, 10.95, 12.6992, 8 ​ 4 3 8\sqrt[3]{4} , 12.70, 12.8, 13, etc. Specifically, for 128 samplings from the base model, 57.8% of outputs are “12.7” or “12.70”, 6.3% of outputs are “12.8”, and 6.3% are “13”. More examples used in this paper are shown in Appendix E . In Appendix C.2.5 , we show that interestingly, even though the key step in solving π 1 \pi_{1} is computing 2048 3 \sqrt[3]{2048} , including only this question in the training example leads to significantly worse performance compared to using full π 1 \pi_{1} .

#### 3.2.2 Post-saturation Generalization: Generalization After Training Accuracy Saturation

Then, we show an interesting phenomenon in 1-shot RLVR. As shown in Fig. 2 , since we only have one training example, it’s foreseeable that the training accuracy for π 1 \pi_{1} and π 13 \pi_{13} quickly saturates before the 100th step. However, the performance on the test set still continues improving: 1-shot RLVR with π 1 \pi_{1} gets 3.4% average improvement from step 100 to step 1540, while using π 13 \pi_{13} yields a 9.9% average improvement from step 500 to step 2000 4 4 4 This behavior looks similar to “grokking”, but we do not emphasize the sudden onset of generalization after training saturates. In Sec. 4.1 , we show that post-saturation generalization is distinct from grokking. . Besides, this phenomenon cannot be observed when using full-set RLVR with DSR-sub currently, as the test performance has started to drop before training accuracy converges.

Moreover, we compare the training and evaluation responses in Fig. 3 . Surprisingly, we find that at the final stage of 1-shot RLVR, the model overfits the single training example by mixing the correct calculation process into long unintelligible multilingual outputs in its outputted reasoning. Nonetheless, the test responses still remain normally and maintain high accuracy, indicating that post-saturation generalization still holds even after overfitting the training example . In particular, overfitting in RLVR occurs quite late ( π 1 \pi_{1} after 1400 steps and π 13 \pi_{13} after 1800 steps). Considering that each example is sampled 1024 times per step, the single training example is not overfitted until after millions of rollouts. Further analysis is provided in Sec. 4.1 .

#### 3.2.3 1-shot RLVR is Effective for Many Examples & Brings Improvements across Categories

In this section, we investigate whether different data behave differently in 1-shot RL, and whether 1-shot RLVR with one training example from a specific category can help the model better generalize to other categories. We select data with high ( π 1 , … , π 17 \pi_{1},\ldots,\pi_{17} ), medium ( π 605 , π 606 \pi_{605},\pi_{606} ), and low ( π 1201 , … ​ π 1209 \pi_{1201},\ldots\pi_{1209} ) historical variance (Eqn. 1 ) and from different topics. We determine the categories of the questions based on their characteristics. We show their detailed MATH500 performance for both overall and subclasses in Tab. 3 . More performance curves are in Appendix C.1 .

We observe that (1) 1-shot RLVR improves performance across all categories in MATH500. Almost all examples yield a ≥ 30 % \geq 30\% improvement over the base model, except for the incorrect example π 1207 \pi_{1207} and the extremely difficult example π 1208 \pi_{1208} , which cause the model to fail to generate any correct solutions. (2) 1-shot RLVR can perform at least as well as the format-reward baseline (except π 1207 \pi_{1207} and π 1208 \pi_{1208} ), and with appropriate examples, 1-shot RLVR with outcome reward can achieve additional non-trivial improvements. From Tab. 3 , we observe that the improvements of some examples (e.g., π 7 \pi_{7} , π 11 \pi_{11} , and π 606 \pi_{606} ) mainly come from format correction. However, many other examples (e.g., π 1 \pi_{1} , π 13 \pi_{13} , and π 1209 \pi_{1209} ) still exhibit non-trivial improvements beyond format fixing. Further discussion is provided in Appendix C.2.3 . (3) Counterintuitively, test data belonging to the same category as the single training example does not necessarily exhibit better improvement. For instance, π 11 \pi_{11} belongs to Number Theory, but RLVR trained with π 11 \pi_{11} achieves a relatively low Number Theory score compared to using other examples (e.g., π 605 \pi_{605} from Precalculus). This may indicate that the reasoning capability stimulated by an instance cannot be simply predicted by superficial features such as categories [ 35 ] . Additional analysis on prompt complexity is provided in Appendix C.2.5 .

#### 3.2.4 More Frequent Self-Reflection on Test Data

In this section, we show another empirical observation of 1-shot RLVR: it can increase the frequency of self-reflection [ 6 ] in the model responses as training progresses. To study this, we check the output patterns of different checkpoints from the RLVR training on Qwen2.5-Math-1.5B. We find that their self-reflection process often appears with words “rethink” , “recheck” and “recalculate” . Therefore, we count the number of responses that contain these three words when evaluating 6 mathematical reasoning tasks. The results are in Fig. 4 . First , after around 1.3k steps, the response length and entropy loss increase significantly, which may imply the attempt of diverse output patterns or overfitting (Fig. 3 ). Second , for the evaluation task, the base model itself already exhibits self-reflection processes, which supports the observation in recent works [ 13 , 21 ] . Third , the number of self-recheck processes increases at the later stages of 1-shot RL training, which again confirms that the model generalizes well on test data and shows more complex reasoning processes even after it overfits the training data. Interestingly, for the 1.2k DeepScaleR subset, the frequency of reflection slightly decreases as the training progresses, matching the decreasing response length.

### 3.3 1/Few-shot RLVR on Other Models/Algorithms

We further investigate whether 1(few)-shot RLVR is feasible for other models and RL algorithms. We consider setup mentioned in Sec. 3.1 , and the results are shown in Tab. 4 (Detailed results on each benchmark are in Appendix C.1 ). We can see (1) for Qwen2.5-Math-7B, 1-shot RLVR with π 1 \pi_{1} improves average performance by 17.8% (5.9% higher than format-reward baseline), and 4-shot RLVR performs as well as RLVR with DSR-sub. Moreover, { π 1 , … , π 16 \pi_{1},\ldots,\pi_{16} } performs better than the subset consisting of 16 randomly sampled examples. (2) For Llama-3.2-3B-Instruct, the absolute gain from RLVR is smaller, but 1(few)-shot RLVR still matches or surpasses (e.g., { π 1 , π 13 } \{\pi_{1},\pi_{13}\} ) the performance of full-set RLVR. We also show the instability of the RLVR process on Llama-3.2-3B-Instruct in Appendix C.1 . (3) RLVR with π 1 \pi_{1} using PPO also works for Qwen2.5-Math-1.5B with PPO. (4) For DeepSeek-R1-Distill-Qwen-1.5B, the performance gap between few-shot and full-set RLVR is larger. Nevertheless, few-shot RLVE still yield improvement. More results are in Appendix C .

## 4 Analysis

In this section, we concentrate on exploring the potential mechanisms that allow RLVR to work with only one or a few examples. We hope the following analyses can provide some insight for future works. Additional experiments and discussions about the format correction (Appendix C.2.3 ), prompt modification (Appendix C.2.5 ) and the reasoning capabilities of base models (Appendix D ) are included in supplementary materials.

### 4.1 Ablation Study: Policy Gradient Loss is the Main Contributor, and Entropy Loss Further Improve Post-Saturation Generalization

As discussed in Sec. 3.2.2 , 1-shot RLVR shows the property of post-saturation generalization. This phenomenon is similar to “grokking” [ 36 , 37 ] , which shows that neural networks first memorize/overfit the training data but still perform poorly on the test set, while suddenly improve generalization after many training steps. A natural question is raised: Is the performance gain from 1-shot RLVR related to the “grokking” phenomenon? To answer this question, noting “grokking” is strongly affected by regularization [ 36 , 38 , 39 , 40 , 41 ] like weight decay, we conduct an ablation study by removing or changing the components of the loss function one by one to see how each of them contributes to the improvement.

The results are shown in Tab. 5 (Test curves are in Appendix C.2.1 ). We see that if we only add policy gradient loss (Row 2) with π 1 \pi_{1} , we already get results close to that of the full loss training (Row 5). In addition, further adding weight decay (Row 3) and KL divergence loss (Row 4) has no significant impact on model performance, while adding entropy loss (Row 5) can further bring 4.0% improvement for MATH500 and 2.5% for AIME24. Here we need to be careful about the weight of the entropy loss, as a too large coefficient (Row 6) might make the training more unstable. These observations support that the feasibility of 1(few)-shot RLVR is mainly attributed to policy gradient loss, rather than weight decay, distinguishing it from “grokking” , which should be significantly affected by weight decay. To double check this, we show that only adding weight decay and KL divergence (Row 8) has little influence on model performance, while using only policy gradient loss and entropy loss (Row 7) behaves almost the same as the full GRPO loss.

Moreover, we also argue that encouraging greater diversity in model outputs—for instance, adding proper entropy loss — can enhance post-saturation generalization in 1-shot RLVR. As shown in Fig. 5 , without entropy loss, model performance under 1-shot RLVR shows limited improvement beyond step 150, coinciding with the point at which training accuracy saturates (Fig. 2 , Left). By adding entropy loss, the model achieves an average improvement of 2.3%, and further increasing the temperature to t = 1.0 t=1.0 yields an additional 0.8% gain. More discussions about entropy loss and post-saturation generalization are in Appendix C.2.2 .

### 4.2 Entropy-Loss-Only Training & Label Correctness

In Tab. 3 , we find that when using π 1207 \pi_{1207} and π 1208 \pi_{1208} , it is difficult for model to output the ground truth label and receive rewards during 1-shot RLVR training, resulting in a very sparse policy gradient signal. Nevertheless, they still outperform the base model, although their performance remains lower than that of the format-reward baseline. To investigate this, we remove the policy loss from the full GRPO loss (Tab. 5 , Row 9) or even retain only the entropy loss (Row 10), and again observe similar improvement. Furthermore, this phenomenon also happens on Qwen2.5-Math-7B and Llama-3.2-3B-Instruct, although only improve at the first several steps. These results implies entropy loss may independently contribute to performance gains from format correction, which, although much smaller than those from policy loss, are still nontrivial.

Moreover, we conduct an experiment by altering the label to (1) the correct one (“12.7,” Row 11), (2) an incorrect one that model can still overfit (“4,” Row 12), and (3) an incorrect one that the model can neither guess nor overfit (“9292725,” Row 13). We compare them with (4) the original label (“12.8,” Row 5). Interestingly, we find the performance rankings are (1) ≈ \approx (4) > > (3) > > (2). This suggests that slight inaccuracies in the label do not significantly impair 1-shot RLVR performance. However, if the incorrect label deviates substantially while remaining guessable and overfittable, the resulting performance can be even worse than using a completely incorrect and unguessable label, which behaves similarly to training with entropy loss alone (Row 10). In Appendix C.2.4 , we also discuss label robustness on full-set RLVR by showing that if too many data in the dataset are assigned random wrong labels, full-set RLVR can perform worse than 1-shot RLVR.

## 5 Conclusion

In this work, we show that 1-shot RLVR is sufficient to trigger substantial improvements in reasoning tasks, even matching the performance of RLVR with thousands of examples. The empirical results reveal not only improved task performance but also additional observations such as post-saturation generalization, cross-category generalization, more frequent self-reflection and also additional analysis. These findings suggest that the reasoning capability of the model is already buried in some base models, and encouraging exploration on a very small amount of data is capable of generating useful RL training signals for igniting these LLM’s reasoning capability. It also demonstrates the anti-overfitting property of the RLVR algorithm with zero-mean advantage, as we can train on a single example millions of times without performance degradation. Our work also emphasizes the importance of better selection and collection of data for RLVR. We discuss directions for future work in Appendix D.4 , and also discuss limitations in Appendix D.1 .

## 6 Acknoledgements

We thank Lifan Yuan, Hamish Ivison, Rulin Shao, Shuyue Stella Li, Rui Xin, Scott Geng, Pang Wei Koh, Kaixuan Huang, Mickel Liu, Jacqueline He, Noah Smith, Jiachen T. Wang, Yifang Chen, and Weijia Shi for very constructive discussions. YW and ZZ acknowledge the support of Amazon AI Ph.D. Fellowship. SSD acknowledges the support of NSF IIS-2110170, NSF DMS-2134106, NSF CCF-2212261, NSF IIS-2143493, NSF CCF-2019844, NSF IIS-2229881, and the Sloan Research Fellowship.

## References

[1] OpenAI. Learning to reason with llms. https://openai.com/index/learning-to-reason-with-llms/ , 2024. Accessed: 2025-04-10.

[2] Daya Guo, Dejian Yang, Haowei Zhang, Junxiao Song, Ruoyu Zhang, Runxin Xu, Qihao Zhu, Shirong Ma, Peiyi Wang, Xiao Bi, et al. Deepseek-r1: Incentivizing reasoning capability in llms via reinforcement learning. arXiv preprint arXiv:2501.12948 , 2025.

[3] Kimi Team, Angang Du, Bofei Gao, Bowei Xing, Changjiu Jiang, Cheng Chen, Cheng Li, Chenjun Xiao, Chenzhuang Du, Chonghua Liao, et al. Kimi k1. 5: Scaling reinforcement learning with llms. arXiv preprint arXiv:2501.12599 , 2025.

[4] Jiaxuan Gao, Shusheng Xu, Wenjie Ye, Weilin Liu, Chuyi He, Wei Fu, Zhiyu Mei, Guangju Wang, and Yi Wu. On designing effective rl reward at training time for llm reasoning. arXiv preprint arXiv:2410.15115 , 2024.

[5] Nathan Lambert, Jacob Morrison, Valentina Pyatkin, Shengyi Huang, Hamish Ivison, Faeze Brahman, Lester James V. Miranda, Alisa Liu, Nouha Dziri, Shane Lyu, Yuling Gu, Saumya Malik, Victoria Graf, Jena D. Hwang, Jiangjiang Yang, Ronan Le Bras, Oyvind Tafjord, Chris Wilhelm, Luca Soldaini, Noah A. Smith, Yizhong Wang, Pradeep Dasigi, and Hannaneh Hajishirzi. Tülu 3: Pushing frontiers in open language model post-training. arXiv preprint arXiv:2411.15124 , 2024.

[6] Kanishk Gandhi, Ayush Chakravarthy, Anikait Singh, Nathan Lile, and Noah D Goodman. Cognitive behaviors that enable self-improving reasoners, or, four habits of highly effective stars. arXiv preprint arXiv:2503.01307 , 2025.

[7] John Schulman, Filip Wolski, Prafulla Dhariwal, Alec Radford, and Oleg Klimov. Proximal policy optimization algorithms. arXiv preprint arXiv:1707.06347 , 2017.

[8] Zhihong Shao, Peiyi Wang, Qihao Zhu, Runxin Xu, Junxiao Song, Xiao Bi, Haowei Zhang, Mingchuan Zhang, YK Li, Y Wu, et al. Deepseekmath: Pushing the limits of mathematical reasoning in open language models. arXiv preprint arXiv:2402.03300 , 2024.

[9] Amirhossein Kazemnejad, Milad Aghajohari, Eva Portelance, Alessandro Sordoni, Siva Reddy, Aaron Courville, and Nicolas Le Roux. Vineppo: Unlocking rl potential for llm reasoning through refined credit assignment. arXiv preprint arXiv:2410.01679 , 2024.

[10] Yufeng Yuan, Yu Yue, Ruofei Zhu, Tiantian Fan, and Lin Yan. What’s behind ppo’s collapse in long-cot? value optimization holds the secret. arXiv preprint arXiv:2503.01491 , 2025.

[11] Qiying Yu, Zheng Zhang, Ruofei Zhu, Yufeng Yuan, Xiaochen Zuo, Yu Yue, Tiantian Fan, Gaohong Liu, Lingjun Liu, Xin Liu, et al. Dapo: An open-source llm reinforcement learning system at scale. arXiv preprint arXiv:2503.14476 , 2025.

[12] Yufeng Yuan, Qiying Yu, Xiaochen Zuo, Ruofei Zhu, Wenyuan Xu, Jiaze Chen, Chengyi Wang, TianTian Fan, Zhengyin Du, Xiangpeng Wei, et al. Vapo: Efficient and reliable reinforcement learning for advanced reasoning tasks. arXiv preprint arXiv:2504.05118 , 2025.

[13] Zichen Liu, Changyu Chen, Wenjun Li, Penghui Qi, Tianyu Pang, Chao Du, Wee Sun Lee, and Min Lin. Understanding r1-zero-like training: A critical perspective. arXiv preprint arXiv:2503.20783 , 2025.

[14] Michael Luo, Sijun Tan, Roy Huang, Xiaoxiang Shi, Rachel Xin, Colin Cai, Ameen Patel, Alpay Ariyak, Qingyang Wu, Ce Zhang, Li Erran Li, Raluca Ada Popa, and Ion Stoica. Deepcoder: A fully open-source 14b coder at o3-mini level. https://pretty-radio-b75.notion.site/DeepCoder-A-Fully-Open-Source-14B-Coder-at-O3-mini-Level-1cf81902c14680b3bee5eb349a512a51 , 2025. Notion Blog.

[15] Jian Hu. Reinforce++: A simple and efficient approach for aligning large language models. arXiv preprint arXiv:2501.03262 , 2025.

[16] Xiaojiang Zhang, Jinghui Wang, Zifei Cheng, Wenhao Zhuang, Zheng Lin, Minglei Zhang, Shaojie Wang, Yinghan Cui, Chao Wang, Junyi Peng, Shimiao Jiang, Shiqi Kuang, Shouyu Yin, Chaohang Wen, Haotian Zhang, Bin Chen, and Bing Yu. Srpo: A cross-domain implementation of large-scale reinforcement learning on llm, 2025.

[17] Jia LI, Edward Beeching, Lewis Tunstall, Ben Lipkin, Roman Soletskyi, Shengyi Costa Huang, Kashif Rasul, Longhui Yu, Albert Jiang, Ziju Shen, Zihan Qin, Bin Dong, Li Zhou, Yann Fleureau, Guillaume Lample, and Stanislas Polu. Numinamath. [https://huggingface.co/AI-MO/NuminaMath-CoT](https://github.com/project-numina/aimo-progress-prize/blob/main/report/numina_dataset.pdf) , 2024.

[18] Michael Luo, Sijun Tan, Justin Wong, Xiaoxiang Shi, William Y. Tang, Manan Roongta, Colin Cai, Jeffrey Luo, Li Erran Li, Raluca Ada Popa, and Ion Stoica. Deepscaler: Surpassing o1-preview with a 1.5b model by scaling rl. https://pretty-radio-b75.notion.site/DeepScaleR-Surpassing-O1-Preview-with-a-1-5B-Model-by-Scaling-RL-19681902c1468005bed8ca303013a4e2 , 2025. Notion Blog.

[19] Xuefeng Li, Haoyang Zou, and Pengfei Liu. Limr: Less is more for rl scaling, 2025.

[20] Yang Yue, Zhiqi Chen, Rui Lu, Andrew Zhao, Zhaokai Wang, Yang Yue, Shiji Song, and Gao Huang. Does reinforcement learning really incentivize reasoning capacity in llms beyond the base model? arXiv preprint arXiv:2504.13837 , 2025. Submitted on April 18, 2025.

[21] Darsh J Shah, Peter Rushton, Somanshu Singla, Mohit Parmar, Kurt Smith, Yash Vanjani, Ashish Vaswani, Adarsh Chaluvaraju, Andrew Hojel, Andrew Ma, et al. Rethinking reflection in pre-training. arXiv preprint arXiv:2504.04022 , 2025.

[22] Guangming Sheng, Chi Zhang, Zilingfeng Ye, Xibin Wu, Wang Zhang, Ru Zhang, Yanghua Peng, Haibin Lin, and Chuan Wu. Hybridflow: A flexible and efficient rlhf framework. arXiv preprint arXiv: 2409.19256 , 2024.

[23] Noam Razin, Zixuan Wang, Hubert Strauss, Stanley Wei, Jason D Lee, and Sanjeev Arora. What makes a reward model a good teacher? an optimization perspective. arXiv preprint arXiv:2503.15477 , 2025.

[24] An Yang, Baosong Yang, Beichen Zhang, Binyuan Hui, Bo Zheng, Bowen Yu, Chengyuan Li, Dayiheng Liu, Fei Huang, Haoran Wei, Huan Lin, Jian Yang, Jianhong Tu, Jianwei Zhang, Jianxin Yang, Jiaxi Yang, Jingren Zhou, Junyang Lin, Kai Dang, Keming Lu, Keqin Bao, Kexin Yang, Le Yu, Mei Li, Mingfeng Xue, Pei Zhang, Qin Zhu, Rui Men, Runji Lin, Tianhao Li, Tingyu Xia, Xingzhang Ren, Xuancheng Ren, Yang Fan, Yang Su, Yichang Zhang, Yu Wan, Yuqiong Liu, Zeyu Cui, Zhenru Zhang, and Zihan Qiu. Qwen2.5 technical report. arXiv preprint arXiv:2412.15115 , 2024.

[25] An Yang, Beichen Zhang, Binyuan Hui, Bofei Gao, Bowen Yu, Chengpeng Li, Dayiheng Liu, Jianhong Tu, Jingren Zhou, Junyang Lin, et al. Qwen2. 5-math technical report: Toward mathematical expert model via self-improvement. arXiv preprint arXiv:2409.12122 , 2024.

[26] Aaron Grattafiori, Abhimanyu Dubey, Abhinav Jauhri, Abhinav Pandey, Abhishek Kadian, Ahmad Al-Dahle, Aiesha Letman, Akhil Mathur, Alan Schelten, Alex Vaughan, et al. The llama 3 herd of models. arXiv preprint arXiv:2407.21783 , 2024.

[27] Dan Hendrycks, Collin Burns, Saurav Kadavath, Akul Arora, Steven Basart, Eric Tang, Dawn Song, and Jacob Steinhardt. Measuring mathematical problem solving with the math dataset. arXiv preprint arXiv:2103.03874 , 2021.

[28] Woosuk Kwon, Zhuohan Li, Siyuan Zhuang, Ying Sheng, Lianmin Zheng, Cody Hao Yu, Joseph E. Gonzalez, Hao Zhang, and Ion Stoica. Efficient memory management for large language model serving with pagedattention. In Proceedings of the ACM SIGOPS 29th Symposium on Operating Systems Principles , 2023.

[29] Hunter Lightman, Vineet Kosaraju, Yura Burda, Harri Edwards, Bowen Baker, Teddy Lee, Jan Leike, John Schulman, Ilya Sutskever, and Karl Cobbe. Let’s verify step by step. arXiv preprint arXiv:2305.20050 , 2023.

[30] Art of Problem Solving. Aime problems and solutions. https://artofproblemsolving.com/wiki/index.php/AIME_Problems_and_Solutions . Accessed: 2025-04-20.

[31] Art of Problem Solving. Amc problems and solutions. https://artofproblemsolving.com/wiki/index.php?title=AMC_Problems_and_Solutions . Accessed: 2025-04-20.

[32] Aitor Lewkowycz, Anders Andreassen, David Dohan, Ethan Dyer, Henryk Michalewski, Vinay Ramasesh, Ambrose Slone, Cem Anil, Imanol Schlag, Theo Gutman-Solo, et al. Solving quantitative reasoning problems with language models. Advances in Neural Information Processing Systems , 35:3843–3857, 2022.

[33] Chaoqun He, Renjie Luo, Yuzhuo Bai, Shengding Hu, Zhen Leng Thai, Junhao Shen, Jinyi Hu, Xu Han, Yujie Huang, Yuxiang Zhang, et al. Olympiadbench: A challenging benchmark for promoting agi with olympiad-level bilingual multimodal scientific problems. arXiv preprint arXiv:2402.14008 , 2024.

[34] Peter Clark, Isaac Cowhey, Oren Etzioni, Tushar Khot, Ashish Sabharwal, Carissa Schoenick, and Oyvind Tafjord. Think you have solved question answering? try arc, the ai2 reasoning challenge. arXiv preprint arXiv:1803.05457 , 2018.

[35] Zhiyuan Zeng, Yizhong Wang, Hannaneh Hajishirzi, and Pang Wei Koh. Evaltree: Profiling language model weaknesses via hierarchical capability trees. arXiv preprint arXiv:2503.08893 , 2025.

[36] Alethea Power, Yuri Burda, Harri Edwards, Igor Babuschkin, and Vedant Misra. Grokking: Generalization beyond overfitting on small algorithmic datasets. arXiv preprint arXiv:2201.02177 , 2022.

[37] Simin Fan, Razvan Pascanu, and Martin Jaggi. Deep grokking: Would deep neural networks generalize better? arXiv preprint arXiv:2405.19454 , 2024.

[38] Neel Nanda, Lawrence Chan, Tom Lieberum, Jess Smith, and Jacob Steinhardt. Progress measures for grokking via mechanistic interpretability. arXiv preprint arXiv:2301.05217 , 2023.

[39] Ziming Liu, Ouail Kitouni, Niklas S Nolte, Eric Michaud, Max Tegmark, and Mike Williams. Towards understanding grokking: An effective theory of representation learning. Advances in Neural Information Processing Systems , 35:34651–34663, 2022.

[40] Branton DeMoss, Silvia Sapora, Jakob Foerster, Nick Hawes, and Ingmar Posner. The complexity dynamics of grokking. arXiv preprint arXiv:2412.09810 , 2024.

[41] Lucas Prieto, Melih Barsbey, Pedro AM Mediano, and Tolga Birdal. Grokking at the edge of numerical stability. arXiv preprint arXiv:2501.04697 , 2025.

[42] Weihao Zeng, Yuzhen Huang, Qian Liu, Wei Liu, Keqing He, Zejun Ma, and Junxian He. Simplerl-zoo: Investigating and taming zero reinforcement learning for open base models in the wild. arXiv preprint arXiv:2503.18892 , 2025.

[43] Liang Wen, Yunke Cai, Fenrui Xiao, Xin He, Qi An, Zhenyu Duan, Yimin Du, Junchen Liu, Lifu Tang, Xiaowei Lv, et al. Light-r1: Curriculum sft, dpo and rl for long cot from scratch and beyond. arXiv preprint arXiv:2503.10460 , 2025.

[44] Mingyang Song, Mao Zheng, Zheng Li, Wenjie Yang, Xuan Luo, Yue Pan, and Feng Zhang. Fastcurl: Curriculum reinforcement learning with progressive context extension for efficient training r1-like reasoning models. arXiv preprint arXiv:2503.17287 , 2025.

[45] Andrew Zhao, Yiran Wu, Yang Yue, Tong Wu, Quentin Xu, Matthieu Lin, Shenzhi Wang, Qingyun Wu, Zilong Zheng, and Gao Huang. Absolute zero: Reinforced self-play reasoning with zero data. arXiv preprint arXiv:2505.03335 , 2025.

[46] Qingyang Zhang, Haitao Wu, Changqing Zhang, Peilin Zhao, and Yatao Bian. Right question is already half the answer: Fully unsupervised llm reasoning incentivization. arXiv preprint arXiv:2504.05812 , 2025.

[47] Yuxin Zuo, Kaiyan Zhang, Shang Qu, Li Sheng, Xuekai Zhu, Biqing Qi, Youbang Sun, Ganqu Cui, Ning Ding, and Bowen Zhou. Ttrl: Test-time reinforcement learning. arXiv preprint arXiv:2504.16084 , 2025.

[48] Hamish Ivison, Muru Zhang, Faeze Brahman, Pang Wei Koh, and Pradeep Dasigi. Large-scale data selection for instruction tuning. arXiv preprint arXiv:2503.01807 , 2025.

[49] Lichang Chen, Shiyang Li, Jun Yan, Hai Wang, Kalpa Gunaratna, Vikas Yadav, Zheng Tang, Vijay Srinivasan, Tianyi Zhou, Heng Huang, and Hongxia Jin. Alpagasus: Training a better alpaca with fewer data. In International Conference on Learning Representations , 2024.

[50] Hamish Ivison, Noah A. Smith, Hannaneh Hajishirzi, and Pradeep Dasigi. Data-efficient finetuning using cross-task nearest neighbors. In Findings of the Association for Computational Linguistics , 2023.

[51] Mengzhou Xia, Sadhika Malladi, Suchin Gururangan, Sanjeev Arora, and Danqi Chen. LESS: selecting influential data for targeted instruction tuning. In International Conference on Machine Learning , 2024.

[52] William Muldrew, Peter Hayes, Mingtian Zhang, and David Barber. Active preference learning for large language models. In International Conference on Machine Learning , 2024.

[53] Zijun Liu, Boqun Kou, Peng Li, Ming Yan, Ji Zhang, Fei Huang, and Yang Liu. Enabling weak llms to judge response reliability via meta ranking. arXiv preprint arXiv:2402.12146 , 2024.

[54] Nirjhar Das, Souradip Chakraborty, Aldo Pacchiano, and Sayak Ray Chowdhury. Active preference optimization for sample efficient rlhf. arXiv preprint arXiv:2402.10500 , 2024.

[55] Long Ouyang, Jeffrey Wu, Xu Jiang, Diogo Almeida, Carroll Wainwright, Pamela Mishkin, Chong Zhang, Sandhini Agarwal, Katarina Slama, Alex Ray, et al. Training language models to follow instructions with human feedback. Advances in Neural Information Processing Systems , 2022.

[56] Mehdi Fatemi, Banafsheh Rafiee, Mingjie Tang, and Kartik Talamadupula. Concise reasoning via reinforcement learning. arXiv preprint arXiv:2504.05185 , 2025.

[57] J. Schulman. Approximating kl divergence. http://joschu.net/blog/kl-approx.html , 2020. 2025.

[58] Bofei Gao, Feifan Song, Zhe Yang, Zefan Cai, Yibo Miao, Qingxiu Dong, Lei Li, Chenghao Ma, Liang Chen, Runxin Xu, et al. Omni-math: A universal olympiad level mathematic benchmark for large language models. arXiv preprint arXiv:2410.07985 , 2024.

[59] Yingqian Min, Zhipeng Chen, Jinhao Jiang, Jie Chen, Jia Deng, Yiwen Hu, Yiru Tang, Jiapeng Wang, Xiaoxue Cheng, Huatong Song, et al. Imitate, explore, and self-improve: A reproduction report on slow-thinking reasoning systems. arXiv preprint arXiv:2412.09413 , 2024.

[60] Jujie He, Jiacai Liu, Chris Yuhao Liu, Rui Yan, Chaojie Wang, Peng Cheng, Xiaoyu Zhang, Fuxiang Zhang, Jiacheng Xu, Wei Shen, Siyuan Li, Liang Zeng, Tianwen Wei, Cheng Cheng, Bo An, Yang Liu, and Yahui Zhou. Skywork open reasoner series. https://capricious-hydrogen-41c.notion.site/Skywork-Open-Reaonser-Series-1d0bc9ae823a80459b46c149e4f51680 , 2025. Notion Blog.

[61] Jiawei Gu, Xuhui Jiang, Zhichao Shi, Hexiang Tan, Xuehao Zhai, Chengjin Xu, Wei Li, Yinghan Shen, Shengjie Ma, Honghao Liu, et al. A survey on llm-as-a-judge. arXiv preprint arXiv:2411.15594 , 2024.

[62] Qwen Team. Qwq-32b: Embracing the power of reinforcement learning, March 2025.

[63] Qingxiu Dong, Lei Li, Damai Dai, Ce Zheng, Jingyuan Ma, Rui Li, Heming Xia, Jingjing Xu, Zhiyong Wu, Tianyu Liu, et al. A survey on in-context learning. arXiv preprint arXiv:2301.00234 , 2022.

[64] David Rolnick, Andreas Veit, Serge Belongie, and Nir Shavit. Deep learning is robust to massive label noise. arXiv preprint arXiv:1705.10694 , 2017.

[65] Preetum Nakkiran, Gal Kaplun, Yamini Bansal, Tristan Yang, Boaz Barak, and Ilya Sutskever. Deep double descent: Where bigger models and more data hurt. Journal of Statistical Mechanics: Theory and Experiment , 2021(12):124003, 2021.

[66] Nitish Shirish Keskar, Dheevatsa Mudigere, Jorge Nocedal, Mikhail Smelyanskiy, and Ping Tak Peter Tang. On large-batch training for deep learning: Generalization gap and sharp minima. arXiv preprint arXiv: 1609.04836 , 2016.

[67] Samuel L. Smith, Benoit Dherin, David G. T. Barrett, and Soham De. On the origin of implicit regularization in stochastic gradient descent. Iclr , 2021.

[68] Zihan Liu, Yang Chen, Mohammad Shoeybi, Bryan Catanzaro, and Wei Ping. Acemath: Advancing frontier math reasoning with post-training and reward modeling. arXiv preprint , 2024.

[69] Ziniu Li, Congliang Chen, Tian Xu, Zeyu Qin, Jiancong Xiao, Ruoyu Sun, and Zhi-Quan Luo. Entropic distribution matching for supervised fine-tuning of llms: Less overfitting and better diversity. In NeurIPS 2024 Workshop on Fine-Tuning in Modern Machine Learning: Principles and Scalability , 2024.

## Contents

## Appendix A Related Work

Reinforcement Learning with Verifiable Reward (RLVR). RLVR, where the reward is computed by a rule-based verification function, has been shown to be effective in improving the reasoning capabilities of LLMs. The most common practice of RLVR when applying reinforcement learning to LLMs on mathematical reasoning datasets is to use answer matching: the reward function outputs a binary signal based on if the model’s answer matches the gold reference answer [ 4 , 5 , 2 , 3 , 42 , 43 , 44 ] . This reward design avoids the need for outcome-based or process-based reward models, offering a simple yet effective approach. The success of RLVR is also supported by advancements in RL algorithms, including value function optimization or detail optimization in PPO [ 7 ] (e.g., VinePPO [ 9 ] , VC-PPO [ 10 ] , VAPO [ 12 ] ), stabilization and acceleration of GRPO [ 2 ] (e.g., DAPO [ 11 ] , Dr. GRPO [ 13 ] , GRPO+ [ 14 ] , SRPO [ 16 ] ), and integration of various components (e.g., REINFORCE++ [ 15 ] ). There are also some recent works that focus on RLVR with minimal human supervision (without using labeled data or even problems), such as Absolute-Zero [ 45 ] , EMPO [ 46 ] , and TTRL [ 47 ] .

Data Selection for LLM Post-Training. The problem of data selection for LLM post-training has been extensively studied in prior work [ 48 ] , with most efforts focusing on data selection for supervised fine-tuning (instruction tuning). These approaches include LLM-based quality assessment [ 49 ] , leveraging features from model computation [ 50 ] , gradient-based selection [ 51 ] , and more. Another line of work [ 52 , 53 , 54 ] explores data selection for human preference data in Reinforcement Learning from Human Feedback (RLHF) [ 55 ] . Data selection for RLVR remains relatively unexplored. One attempt is LIMR [ 19 ] , which selects 1.4k examples from an 8.5k full set for RLVR to match performance; however, unlike our work, they do not push the limits of training set size to the extreme case of just a single example. Another closely related concurrent work [ 56 ] shows that RLVR using PPO with only 4 examples can already yield very significant improvements; however, they do not systematically explore this observation, nor do they demonstrate that such an extremely small training set can actually match the performance of using the full dataset.

## Appendix B Experiment Setup

### B.1 Details of Loss Function

As said in the main paper, we contain three components in the GRPO loss function following verl [ 22 ] pipeline: policy gradient loss, KL divergence, and entropy loss. Details are as follows. For each question q q sampled from the Question set P ⁡ ( Q ) P(Q) , GRPO samples a group of outputs { o 1 , o 2 , … , o G } \{o_{1},o_{2},\dots,o_{G}\} from the old policy model π θ old \pi_{\theta_{\text{old}}} , and then optimizes the policy model π θ \pi_{\theta} by minimizing the following loss function: ℒ GRPO ​ ( θ ) \displaystyle\mathcal{L}_{\text{GRPO}}(\theta) = 𝔼 q ∼ P ⁡ ( Q ) { o i } i = 1 G ∼ π θ old ​ ( O | q ) ​ [ ℒ PG-GRPO ′ ​ ( ⋅ , θ ) + β ​ ℒ KL ′ ​ ( ⋅ , θ , θ ref ) + α ​ ℒ Entropy ′ ​ ( ⋅ , θ ) ] , \displaystyle=\mathbb{E}_{\begin{subarray}{c}q\sim P(Q)\\ \{o_{i}\}_{i=1}^{G}\sim\pi_{\theta_{\text{old}}}(O|q)\end{subarray}}\ \Bigg[\mathcal{L}^{\prime}_{\text{PG-GRPO}}(\cdot,\theta)+\beta\mathcal{L}^{\prime}_{\text{KL}}(\cdot,\theta,\theta_{\text{ref}})+\alpha\mathcal{L}^{\prime}_{\text{Entropy}}(\cdot,\theta)\Bigg], (3) where β \beta and α \alpha are hyper-parameters (in general β > 0 \beta>0 , α < 0 \alpha<0 ), and “ ⋅ \cdot ” is the abbreviation of sampled prompt-responses: { q , { o i } i = 1 G } \{q,\{o_{i}\}_{i=1}^{G}\} . The policy gradient loss and KL divergence loss are: ℒ PG-GRPO ′ ​ ( q , { o i } i = 1 G , θ ) \displaystyle\mathcal{L}^{\prime}_{\text{PG-GRPO}}(q,\{o_{i}\}_{i=1}^{G},\theta) = − 1 G ∑ i = 1 G ( min ( π θ ​ ( o i | q ) π θ old ​ ( o i | q ) A i , clip ( π θ ​ ( o i | q ) π θ old ​ ( o i | q ) , 1 − ε , 1 + ε ) A i ) ) \displaystyle=-\frac{1}{G}\sum_{i=1}^{G}\Big(\min\Big(\frac{\pi_{\theta}(o_{i}|q)}{\pi_{\theta_{\text{old}}}(o_{i}|q)}A_{i},\,\operatorname{clip}\bigl(\tfrac{\pi_{\theta}(o_{i}|q)}{\pi_{\theta_{\text{old}}}(o_{i}|q)},1-\varepsilon,\,1+\varepsilon\bigr)A_{i}\Big)\Big) (4) ℒ KL ′ ​ ( q , { o i } i = 1 G , θ , θ ref ) \displaystyle\mathcal{L}^{\prime}_{\text{KL}}(q,\{o_{i}\}_{i=1}^{G},\theta,\theta_{\text{ref}}) = 𝔻 KL ( π θ ∥ π θ ref ) = π θ ref ​ ( o i | q ) π θ ​ ( o i | q ) − log π θ ref ​ ( o i | q ) π θ ​ ( o i | q ) − 1 , \displaystyle=\mathbb{D}_{\mathrm{KL}}\!\left(\pi_{\theta}\|\pi_{\theta_{\text{ref}}}\right)=\frac{\pi_{\theta_{\text{ref}}}(o_{i}|q)}{\pi_{\theta}(o_{i}|q)}-\log\frac{\pi_{\theta_{\text{ref}}}(o_{i}|q)}{\pi_{\theta}(o_{i}|q)}-1, (5) Here θ ref \theta_{\text{ref}} is the reference model, ε \varepsilon is a hyper-parameter of clipping threshold. Notably, we use the approximation formulation of KL divergence [ 57 ] , which is widely used in previous works [ 8 , 2 ] . Besides, A i A_{i} is the group-normalized advantage defined below. A i = r i − mean ⁡ ( { r 1 , r 2 , … , r G } ) std ⁡ ( { r 1 , r 2 , … , r G } ) . i ∈ [ G ] A_{i}=\frac{r_{i}-\operatorname{mean}\bigl(\{r_{1},r_{2},\dots,r_{G}\}\bigr)}{\operatorname{std}\bigl(\{r_{1},r_{2},\dots,r_{G}\}\bigr)}.\quad i\in[G] (6) Since we focus on math questions, we let the reward r i r_{i} be the 0-1 accuracy score, and r i r_{i} is 1 if and only if the response o i o_{i} gets the correct answer to the question q q . What’s more, the entropy loss ℒ Entropy ′ \mathcal{L}^{\prime}_{\text{Entropy}} calculates the average per-token entropy of the responses, and its coefficient α < 0 \alpha<0 implies the encouragement of more diverse responses.

The details of entropy loss are as follows. For each query q q and set of outputs { o i } i = 1 G \{o_{i}\}_{i=1}^{G} , the model produces logits X X that determine the policy distribution π θ \pi_{\theta} . These logits X X are the direct computational link between inputs q q and outputs o o - specifically, the model processes q q to generate logits X X , which after softmax normalization give the probabilities used to sample each token in the outputs o o . The entropy loss is formally defined below. ℒ Entropy ′ ​ ( q , { o i } i = 1 G , θ ) = ∑ b , s M b , s ⋅ H b , s ​ ( X ) ∑ b , s M b , s \displaystyle\mathcal{L}^{\prime}_{\text{Entropy}}(q,\{o_{i}\}_{i=1}^{G},\theta)=\frac{\sum_{b,s}M_{b,s}\cdot H_{b,s}(X)}{\sum_{b,s}M_{b,s}} (7) Here M b , s M_{b,s} represents the response mask indicating which tokens contribute to the loss calculation (excluding padding and irrelevant tokens), with b b indexing the batch dimension and s s indexing the sequence position. The entropy H b , s ​ ( X ) H_{b,s}(X) is computed from the model’s logits X X : H b , s ​ ( X ) = log ⁡ ( ∑ v e X b , s , v ) − ∑ v p b , s , v ⋅ X b , s , v H_{b,s}(X)=\log(\sum_{v}e^{X_{b,s,v}})-\sum_{v}p_{b,s,v}\cdot X_{b,s,v} (8) where v v indexes over the vocabulary tokens (i.e., the possible output tokens from the model’s vocabulary), and the probability distribution is given by p b , s , v = softmax ​ ( X b , s ) v = e X b , s , v ∑ v ′ e X b , s , v ′ p_{b,s,v}=\text{softmax}(X_{b,s})_{v}=\frac{e^{X_{b,s,v}}}{\sum_{v^{\prime}}e^{X_{b,s,v^{\prime}}}} .

### B.2 Training Dataset

##### DeepScaleR-sub.

DeepScaleR-Preview- Dataset [ 18 ] consists of approximately 40,000 unique mathematics problem-answer pairs from AIME (1984-2023), AMC (pre-2023), and other sources including Omni-MATH [ 58 ] and Still [ 59 ] . The data processing pipeline includes extracting answers using Gemini-1.5-Pro-002, removing duplicate problems through RAG with Sentence-Transformers embeddings, and filtering out questions that cannot be evaluated using SymPy to maintain a clean training set. We randomly select a subset that contains 1,209 examples referred to as "DSR-sub".

##### MATH.

Introduced in [ 27 ] , this dataset contains 12,500 challenging competition mathematics problems designed to measure advanced problem-solving capabilities in machine learning models. Unlike standard mathematical collections, MATH features complex problems from high school mathematics competitions spanning subjects including Prealgebra, Algebra, Number Theory, Counting and Probability, Geometry, Intermediate Algebra, and Precalculus, with each problem assigned a difficulty level from 1 to 5 and accompanied by detailed step-by-step solutions. It’s partitioned into a training subset comprising 7,500 problems (60%) and a test subset containing 5,000 problems (40%).

### B.3 Evaulation Dataset

All evaluation sets are drawn from the Qwen2.5-Math evaluation repository 5 5 5 https://github.com/QwenLM/Qwen2.5-Math , with the exception of AIME2025 6 6 6 https://huggingface.co/datasets/opencompass/AIME2025 . We summarize their details as follows:

##### MATH500.

MATH500, developed by OpenAI [ 29 ] , comprises a carefully curated selection of 500 problems extracted exclusively from the test partition (n=5,000) of the MATH benchmark [ 27 ] . It is smaller, more focused, and designed for efficient evaluation.

##### AIME 2024/2025.

The AIME 2024 and 2025 datasets are specialized benchmark collections, each consisting of 30 problems from the 2024 and 2025 American Invitational Mathematics Examination (AIME) I and II, respectively [ 30 ] .

##### AMC 2023.

AMC 2023 dataset consists of 40 problems, selected from two challenging mathematics competitions (AMC 12A and 12B) for students grades 12 and under across the United States [ 31 ] . These AMC 12 evaluates problem-solving abilities in secondary school mathematics, covering topics such as arithmetic, algebra, combinatorics, geometry, number theory, and probability, with all problems solvable without calculus.

##### Minerva Math.

Implicitly introduced in the paper "Solving Quantitative Reasoning Problems with Language Models" [ 32 ] as OCWCourses, Minerva Math consists of 272 undergraduate-level STEM problems harvested from MIT’s OpenCourseWare, specifically designed to evaluate multi-step scientific reasoning capabilities in language models. Problems were carefully curated from courses including solid-state chemistry, information and entropy, differential equations, and special relativity, with each problem modified to be self-contained with clearly-delineated answers that are automatically verifiable through either numeric (191 problems) or symbolic solutions (81 problems).

##### OlympiadBench.

OlympiadBench [ 33 ] is a large-scale, bilingual, and multimodal benchmark designed to evaluate advanced mathematical and physical reasoning in AI systems. It contains 8,476 Olympiad-level problems, sourced from competitions and national exams, with expert-annotated step-by-step solutions. The subset we use for evaluation consists of 675 open-ended text-only math competition problems in English.

We also consider other non-mathematical reasoning tasks: ARC-Challenge and ARC-Easy [ 34 ] .

##### ARC-Challenge/Easy.

The ARC-Challenge benchmark represents a subset of 2,590 demanding science examination questions drawn from the broader ARC (AI2 Reasoning Challenge) [ 34 ] collection, specifically selected because traditional information retrieval and word co-occurrence methods fail to solve them correctly. This challenging evaluation benchmark features exclusively text-based, English-language multiple-choice questions (typically with four possible answers) spanning diverse grade levels, designed to assess science reasoning capabilities rather than simple pattern matching or information retrieval. The complementary ARC-Easy [ 34 ] subset contains 5197 questions solvable through simpler approaches. We use 1.17k test split for ARC-Challenge evaluation and 2.38k test split for ARC-Easy evaluation, respectively.

### B.4 More Training Details

For DeepSeek-R1-Distill-Qwen-1.5B, we let the maximum response length be 8192, following the setup of stage 1 in DeepScaleR [ 18 ] . The learning rate is set to 1e-6. The coefficient of weight decay is set to 0.01 by default. We store the model checkpoint every 20 steps for evaluation, and use 8 A100 GPUs for each experiment. For Qwen2.5-Math-1.5B, Qwen2.5-Math-7B, Llama-3.2-3B-Instruct, and DeepSeek-R1-Distill-Qwen-1.5B, we train for 2000, 1000, 1000, and 1200 steps, respectively, unless the model has already shown a significant drop in performance. We use the same approach as DeepScaleR [ 18 ] (whose repository is also derived from the verl) to save the model in safetensor format to facilitate evaluation.

### B.5 More Evaluation Details

In evaluation, the maximum number of generated tokens is set to be 3072 by default. For Qwen-based models, we use the “ qwen25-math-cot ” prompt template in evaluation. For Llama and distilled models, we use their original chat templates. We set the evaluation seed to 0 and top_p to 1 by default. For evaluation on DeepSeek-R1-Distill-Qwen-1.5B, following DeepSeek-R1 [ 2 ] and DeepScaleR [ 18 ] , we set the temperature to 0.6 and top_p to 0.95, and use avg@16 for MATH500, Minerva Math, and OlympiadBench, and avg@64 for AIME24, AIME25, and AMC23. Since our training length is 8192, we provide results for both 8192 (8k) and 32768 (32k) evaluation lengths (Appendix C.1.6 ). By default, we report the performance of the checkpoint that obtains the best average performance on 6 benchmarks. But in Sec. 3.2.3 and Sec. 4.1 , since we only evaluate MATH500 and AIME2024, we report the best model performance on each benchmark separately, i.e., the best MATH500 checkpoint and best AIME2024 checkpoint can be different (This will not influence our results, as in Tab. 9 and Tab. 11 , we still obtain similar conclusions as in main paper.) We use 4 GPUs for the evaluation. Finally we mention that there are slightly performance difference on initial model caused by numerical precision, but it does not influence our conclusions (Appendix B.6 ).

### B.6 Performance Difference on Initial Model

We mention that there is a precision inconsistency between models downloaded from Hugging Face repositories and initial checkpoints saved by the verl/deepscaler reinforcement learning pipeline in Tab. 7 . This discrepancy arises from the verl/DeepScaleR pipeline saving checkpoints with float32 precision, whereas the original base models from Hugging Face utilize bfloat16 precision.

The root cause appears to be in the model initialization process within the verl framework. The fsdp_workers.py 7 7 7 https://github.com/volcengine/verl/blob/main/verl/workers/fsdp_workers.py file in the verl codebase reveals that models are deliberately created in float32 precision during initialization, as noted in the code comment: "note that we have to create model in fp32. Otherwise, the optimizer is in bf16, which is incorrect". This design choice was likely made to ensure optimizer stability during training. When examining the checkpoint saving process, the precision setting from initialization appears to be preserved, resulting in saved checkpoints retaining float32 precision rather than the original bfloat16 precision of the base model.

Our empirical investigation demonstrates that modifying the torch_dtype parameter in the saved config.json file to match the base model’s precision (specifically, changing from float32 to bfloat16 ) successfully resolves the observed numerical inconsistency. Related issues are documented in the community 8 8 8 https://github.com/volcengine/verl/issues/296 , and we adopt the default settings of the verl pipeline in our experiments.

## Appendix C Evaluation Result

### C.1 Main Experiments

#### C.1.1 Detailed performance on Qwen2.5-Math-1.5B.

In Tab. 8 , we show the detailed performance that shown in Fig. 1 . Results are reported for the checkpoint achieving the best average performance.

#### C.1.2 Detailed Performance on More Models and Training Examples.

In Tab. 10 , we also show the 1(few)-shot RLVR results on the base model (Qwen2.5-1.5B [ 24 ] ) and instruction model (Qwen2.5-Math-1.5B-Instruct [ 25 ] ). More detailed test curves are shown in Fig. 10 and Fig. 11 . We can see that (1) for Qwen2.5-1.5B, the gap between 1-shot RLVR with π 1 \pi_{1} and full-set RLVR is larger, but the former still improves model performance significantly (e.g., MATH500: 3.2% to 43.6%), and 16-shot RLVR works very closely to full-set RLVR. (2) for Qwen2.5-Math-1.5B-Instruct, both full-set RLVR and 1-shot RLVR have limited improvement as the initial model already has good performance. Interestingly, as shown in Fig. 11 , we observe that 1-shot RLVR is more stable than full-set RLVR.

Besides, we also consider other single training examples like π 605 \pi_{605} and π 1209 \pi_{1209} on Qwen2.5-Math-7B. We can see that they behave relatively worse than π 1 \pi_{1} , and 16-shot RLVR provides a more consistent approach to closing the performance gap relative to full-set RLVR.

#### C.1.3 Detailed performance with best per-benchmark results

In Tab. 9 , we present the detailed 1(few)-shot RLVR results for Qwen2.5-Math-1.5B. Here, we record the model’s best performance on each benchmark individually, so their average can be higher than the best overall average performance (“Avg.”). We include these results to estimate the upper limit of what the model can achieve on each benchmark. Additionally, we include several examples that, while not performing as well as π 1 \pi_{1} or π 13 \pi_{13} , still demonstrate significant improvements, such as π 2 \pi_{2} , π 1201 \pi_{1201} , and π 1209 \pi_{1209} . We observe that, in general, better results correspond to a larger checkpoint step for best average performance, which may correspond to a longer post-saturation generalization process. Similarly, in Tab. 11 , we also include the best per-benchmark results for Qwen2.5-Math-7B, Llama-3.2-3B-Instruct, respectively, together with Qwen2.5-Math-1.5B with PPO training.

#### C.1.4 Detailed Test curves on MATH500 for 1-shot RLVR on Qwen2.5-Math-1.5B.

We plot the performance curves for each subject in MATH500 under 1-shot RLVR using different mathematical examples. As shown in Fig. 6 , the choice of example leads to markedly different improvements and training dynamics in 1-shot RLVR, highlighting the critical importance of data selection for future few-shot RLVR methods.

#### C.1.5 Detailed RLVR results on eacn benchmark over training process.

To better visualize the training process of RLVR and compare few-shot RLVR with full-set RLVR, we show the performance curves for each benchamrk on each model in Fig. 7 , 8 , 9 . It will be interesting to see that if applying 1(few)-shot RLVR for more stable GRPO variants [ 13 , 11 , 12 , 16 ] can alleviate this phenomenon. In addition to the conclusions discussed in Sec. 3.3 , we also note that Llama3.2-3B-Instruct is more unstable during training, as almost all setups start having performance degradation before 200 steps.

In Appendix C.1.2 , we also test the base model and instruction version models in Qwen family. Their test curves are also shown in Fig. 10 and Fig. 11 .

#### C.1.6 More Evaluation on DeepSeek-R1-Distill-Qwen-1.5B

In Tab. 12 we show the DeepSeek-R1-Distill-Qwen-1.5B results at 8k and 32k evaluation lengths. The experimental setup is illustrated in Appendix B.3 .

### C.2 Analysis

#### C.2.1 Test Curves for Ablation Study

In Fig. 12 , we can see the test curves for ablation study (Sec. 4.1 ). We can see that policy gradient loss is the main contributor of 1-shot RLVR. More discussions about format fixing are in Appendix C.2.3 .

#### C.2.2 Entropy loss

##### Detailed results of entropy-loss-only training.

As in Sec. 4.2 , we show the full results of entropy-loss-only training in Tab. 13 . Training with only entropy loss for a few steps can improve model performance on all math benchmarks except AIME2025. The test curves are in Fig. 12 . Notice that the improvement of entropy-loss-only training on Qwen2.5-Math-1.5B is similar to that of RLVR with format reward (Appendix C.2.3 , Tab. 14 ), thus we doubt that the effectiveness of entropy-loss-only training may come from format fixing, and we leave the rigorous analysis of this phenomenon for future works.

##### Discussion of entropy loss and its function in 1-shot RLVR.

Notably, we observe that the benefit of adding entropy loss for 1-shot RLVR is consistent with conclusions from previous work [ 60 ] on the full RLVR dataset, which shows that appropriate entropy regularization can enhance generalization, although it remains sensitive to the choice of coefficient. We conjecture the success of 1-shot RLVR is that the policy gradient loss on the learned example (e.g., π ⁡ ( 1 ) \pi(1) ) actually acts as an implicit regularization by ensuring the correctness of learned training examples when the model tries to explore more diverse responses or strategies, as shown in Fig. 3 (Step 1300). And because of this, both policy loss and entropy loss can contribute to the improvement of 1-shot RLVR. We leave the rigorous analysis to future works.

#### C.2.3 (Only) Format Correction?

As discussed in Dr. GRPO [ 13 ] , changing the template of Qwen2.5-Math models can significantly affect their math performance. In this section, we investigate some critical problems: is (1-shot) RLVR doing format fixing? And if the answer is true, is this the only thing 1-shot RLVR does?

To investigate it, we consider three methods:

##### (a). Applying format reward in RLVR.

We first try to apply only format reward for RLVR (i.e., if the verifier can parse the final answer from model output, then it gets 1 reward no matter if the answer is correct or not, otherwise it gets 0 reward), considering both 1-shot and full-set. The results are shown in Tab. 14 , and the test curves are shown in Fig. 14 and Fig. 13 , respectively.

Notably, we can find that (1) Applying format reward to full-set RLVR and 1-shot RLVR behave very similarly. (2) applying only format reward is already capable of improving model performance significantly (e.g., about 29% improvement on MATH500 and about 11% gain on average). (3) There is still significant gap between the performance of 1-shot RLVR with outcome reward using π 1 \pi_{1} and that of format-reward RLVR (e.g., +7.4% on MATH500 and +5.8% on average), although they may have similar ratios of responses that contain “ \boxed{} ” in evaluation (More discussions are in (b) part). (4) In particular, format-reward RLVR is more sensitive to entropy loss based on Fig. 14 and Fig. 13 .

Interestingly, we also note that the best performance of format-reward RLVR on MATH500 and AIME24 are close to that for 1-shot RLVR with relatively worse examples, for example, π 7 \pi_{7} and π 11 \pi_{11} in Tab. 3 . This may imply that 1-shot RLVR with outcome reward can at least work as well as format-reward RLVR, but with proper examples that can better incentivize the reasoning capability of the model, 1-shot RLVR with outcome reward can bring additional non-trivial improvement . Appendix C.2.5 provides a prompt π 1 ′ \pi_{1}^{\prime} , which uses a sub-question of π 1 \pi_{1} , as an example to support our claim here.

##### (b) Observe the change of format in 1-shot RLVR.

We then investigate how the output format of the model, for example, the number of \boxed{} , changes in the 1-shot RLVR progress. The results are shown in Fig. 15 . We can see that (1) the test accuracy is strongly positively correlated to the number of \boxed{} , which matches our claim that format fixing contributes a lot to model improvement in (a), but (2) for some benchmarks like MATH500, Minerva Math and OlympiadBench, when the number of \boxed{} keeps a relatively high ratio, the test accuracy on these benchmarks is still improving, which may imply independent improvement of reasoning capability.

In particular, to prevent the case that the model outputs the correct answer but not in \boxed{} , we also use LLM-as-a-judge [ 61 ] with QwQ-32B [ 62 ] to judge if the model contains the correct answer in the response. The results are shown in Tab. 15 . We can see that the accuracy judged by rule-based Qwen-Eval pipeline and LLM judger QwQ-32B are very close, and as the ratio of \boxed{} increases, the test accuracy also increases, which implies that the number of correct answers exhibited in the response also increases, rather than just putting correct answer into \boxed{} .

Notably, we also observe that Qwen2.5-Math models contain lots of repetition at the end of model responses, which may result in failure of obtaining final results. The ratio of repetition when evaluating MATH500 can be as high as about 40% and 20% for Qwen2.5-Math-1.5B and Qwen2.5-Math-7B, respectively, which is only about 2% for Llama3.2-3B-Instruct. This may result in the large improvement of format fixing (e.g., format-reward RLVR) mentioned in (a).

(c) In-context learning with one-shot example. In-context learning [ 63 ] is a widely-used baseline for instruction following (although it may still improve model’s reasoning capability). In this section, we try to see if 1-shot RLVR can behave better than in-context learning. Especially, we consider the official 4 examples chosen by Qwen-Eval [ 25 ] for in-context learning, and also the single training example π 1 \pi_{1} . The results are shown in Tab. 16 .

We can find that (1) surprisingly, π 1 \pi_{1} with self-generated response can behave much better than Qwen’s official examples , both for 1.5B and 7B models. In particular on Qwen2.5-Math-7B, in-context learning with π 1 \pi_{1} can improve MATH500 from 51.0% to 75.4% and on average from 22.4% to 37.4%. (2) Although in-context learning also improves the base models, 1-shot RLVR still performs better than all in-context results, showing the advantage of RLVR.

In short, we use these three methods to confirm that 1-shot RLVR indeed does format fixing and obtains a lot of gain from it, but it still has additional improvement that cannot be easily obtained from format reward or in-context learning.

#### C.2.4 Influence of Random Wrong Labels

In this section, we want to investigate the label robustness of RLVR. It’s well-known that general deep learning is robust to label noise [ 64 ] , and we want to see if this holds for RLVR. We try to randomly flip the labels of final answers in DSR-sub and see their performance. Here we randomly add or subtract numbers within 10 and randomly change the sign. If it is a fraction, we similarly randomly add or subtract the numerator and denominator.

The results are in Tab. 17 . We can see that (1) changing 60% of the data with wrong labels can still achieve good RLVR results. (2) if 90% of the data in the dataset contains wrong labels (i.e., only about 120 data contain correct labels, and all other 1.1k data have wrong labels), the model performance will be worse than that for 1-shot RLVR with π 1 \pi_{1} (which only contains 1 correct label!). This may show that RLVR is partially robust to label noise, but if there are too many data with random wrong labels, they may hurt the improvement brought by data with correct labels.

#### C.2.5 Change the Prompt of π 1 \pi_{1}

As discussed in Sec. 3.2.1 , we show that the model can almost solve π 1 \pi_{1} but sometimes fails in solving its last step: “Calculate 2048 3 \sqrt[3]{2048} ”. We use this step itself as a problem ( π 1 ′ \pi_{1}^{\prime} ), and see how it behaves in 1-shot RLVR. The results are in Tab. 18 . Interestingly, we find that π 1 ′ \pi_{1}^{\prime} significantly underperforms π 1 \pi_{1} and has only 1.3% average improvement compared with format reward (as illustrated in Appendix C.2.3 (a)). We think the reason should be that although solving 2048 3 \sqrt[3]{2048} is one of the most difficult parts of π 1 \pi_{1} , π 1 \pi_{1} still needs other key steps to solve (e.g., calculating k k from P = k ​ A ​ V 3 P=kAV^{3} given some values) that may generate different patterns of CoT (rather than just calculating), which may allow more exploration space at the post-saturation generalization stage and maybe better incentivize the model’s reasoning capability.

### C.3 Response Length

In Tab. 19 , we report the average response length on the evaluation tasks. The response length on the test tasks remains relatively stable compared to that on the training data.

### C.4 Pass@8 Results

In Tab. 20 , we report the pass@8 results on the evaluation tasks. Interestingly, we find that (1) 1-shot RLVR achieves comparable or even slightly better pass@8 performance (51.7(2) full-set RLVR (with 1.2k DSR-sub) exhibits a noticeable downward trend in pass@8 performance after 200 steps, which is consistent with recent findings that RLVR may sometimes degrade the pass@n performance [ 20 ] .

## Appendix D Discussions

### D.1 Limitations of Our Work

Due to the limit of computational resources, we haven’t tried larger models like Qwen2.5-32B training currently. But in general, a lot of RLVR works are conducted on 1.5B and 7B models, and they already achieve impressive improvement on some challenging math benchmarks like OlympiadBench, so our experiments are still insightful for RLVR topics. Another limitation of our work is that we mainly focus on the math domain, but haven’t tried 1(few)-shot RLVR on other verifiable domains like coding. But we also emphasize that all math-related experiments and conclusions in our paper are logically self-contained and clearly recorded, to ensure clarity and avoid confusion for readers. And we mainly focus on analyzing this new phenomenon itself, which already brings a lot of novel observations (e.g., cross-category generalization, post-saturation generalization, and more frequent self-reflection in 1-shot RLVR, etc.). We leave the few-shot RLVR on other scenarios for future work.

In particular, we note that our main focus is to propose a new observation rather than propose a new better method, noting that 1-shot RLVR doesn’t save (and maybe requires more) RL computation. Besides, π 1 \pi_{1} is not necessarily the best choice for 1-shot RLVR on other models, since it’s selected based on the historical variance score of Qwen2.5-Math-1.5B. In general, using few-shot RLVR may be more stable for training, as we have seen that on DeepSeek-R1-Distill-Qwen-1.5B (Tab. 4 ), Qwen2.5-Math-7B (Tab. 4 , 10 ) and Qwen2.5-1.5B (Tab. 10 ), RLVR with 16 examples ( { π 1 , … , π 16 } \{\pi_{1},\ldots,\pi_{16}\} ) works as well as RLVR with 1.2k dataset DSR-sub and outperforms 1-shot RL with π 1 \pi_{1} .

### D.2 Reasoning Capability of Base Models

The effectiveness of 1(few)-shot RLVR provides strong evidence for an assumption people proposed recently, that is, base models already have strong reasoning capability [ 13 , 6 , 20 , 21 ] . For example, Dr. GRPO [ 13 ] has demonstrated that when no template is used, base models can achieve significantly better downstream performance. Recent work further supports this observation by showing that, with respect to the pass@k metrics, models trained via RLVR gradually perform worse than the base model as k k increases [ 20 ] . Our work corroborates this claim from another perspective, as a single example provides almost no additional knowledge. Moreover, our experiments reveal that using very few examples with RLVR is already sufficient to achieve significant improvement on mathematical reasoning tasks. Thus, it is worth investigating how to select appropriate data to better activate the model during the RL stage while maintaining data efficiency .

### D.3 Why Model Continues Improving After the Training Accuracy Reaches Near 100%?

A natural concern of 1-shot RLVR is that if training accuracy reaches near 100% (which may occur when over-training on one example), the GRPO advantage (Eqn. 6 ) should be zero, eliminating policy gradient signal. However, entropy loss encourages diverse outputs, causing occasional errors ( 99.x% training accuracy) and non-zero gradients (advantage becomes large for batches with wrong responses due to small variance). This shows the importance of entropy loss to the post-saturation generalization (Fig. 5 ). Supporting this, Fig. 16 shows that for 1-shot RLVR training ( π 1 \pi_{1} ) on Qwen2.5-Math-1.5B, policy gradient loss remains non-zero after 100 steps.

### D.4 Future Works

We believe our findings can provide some insights for the following topics:

##### Data Selection and Curation.

Currently, there are no specific data selection methods for RLVR except LIMR [ 19 ] . Note that 1-shot RLVR allows for evaluating each example individually, it will be helpful for assessing the data value, and thus help to design better data selection strategy. What’s more, noting that different examples can have large differences in stimulating LLM reasoning capability (Tab. 3 ), it may be necessary to find out what kind of data is more useful for RLVR, which is critical for the RLVR data collection stage. It’s worth mentioning that our work does not mean scaling RLVR datasets is useless , but it emphasizes the importance of better selection and collection of data for RLVR.

##### Understanding 1-shot RLVR and Post-saturation Generalization

A rigorous understanding for the feasibility of 1-shot LLM RLVR and post-saturation generalization is still unclear. We think that one possible hypothesis is that the policy loss on the learned examples plays a role as “implicit regularization” of RLVR when the model tries to explore more diverse output strategies under the encouragement of entropy loss or larger rollout temperature. It will punish the exploration patterns that make the model fail to answer the learned data, and thus provide a verification for exploration. It’s interesting to explore if the phenomenon has relevance to Double Descent [ 65 ] or the implicit regularization from SGD [ 66 , 67 ] , as 1-shot RLVR on π 13 \pi_{13} (Fig. 2 , middle) shows a test curve similar to Double Descent. We leave the rigorous analysis of this phenomenon for future works, and we believe that can help us to comprehend what happens in the RLVR process.

##### Importance of Exploration.

In Sec. 4.1 , we also highlight the importance of entropy loss in 1-shot RLVR, and note that a more thorough explanation of why training with only entropy loss can enhance model performance remains an interesting direction for future work (Sec. 4.2 ). Relatedly, entropy loss has also received increasing attention from the community, with recent works discussing its dynamics [ 68 , 47 , 60 ] or proposing improved algorithms from the perspective of entropy [ 46 ] . Moreover, we believe a broader and more important insight for these is that encouraging the model to explore more diverse outputs within the solution space is critical, as it may significantly impact the model’s generalization to downstream tasks [ 69 ] . Adding entropy loss is merely one possible approach to achieve this goal and may not necessarily be the optimal solution. As shown in our paper and previous work [ 60 ] , the effectiveness of entropy loss is sensitive to the choice of coefficient, which could limit its applicability in larger-scale experiments. We believe that discovering better strategies to promote exploration could further enhance the effectiveness of RLVR.

##### Other Applications.

In this paper, we focus primarily on mathematical reasoning data; however, it is also important to evaluate the efficacy of 1-shot RLVR in other domains, such as code generation or tasks without verifiable rewards. Moreover, investigating methodologies to further improve few-shot RLVR performance under diverse data-constrained scenarios represents a valuable direction. Examining the label robustness of RLVR, as discussed in Sec. 4.2 , likewise merits further exploration. Finally, these observations may motivate the development of additional evaluation sets to better assess differences between 1-shot and full-set RLVR on mathematical or other reasoning tasks.

## Appendix E Example Details

In the main paper, we show the details of π 1 \pi_{1} . Another useful example π 13 \pi_{13} is shown in Tab. 21 . Here we mention that π 13 \pi_{13} is a geometry problem and its answer is precise. And similar to π 1 \pi_{1} , the initial base model still has 21.9% of outputs successfully obtaining 4 3 \frac{4}{3} in 128 samplings.

Besides, Tab. 22 through 42 in the supplementary material provide detailed information for each example used in our experiments and for all other examples in { π 1 , … , π 17 \pi_{1},\ldots,\pi_{17} }. Each table contains the specific prompt and corresponding ground truth label for an individual example.

## Instructions for reporting errors

We are continuing to improve HTML versions of papers, and your feedback helps enhance accessibility and mobile support. To report errors in the HTML that will help us improve conversion and rendering, choose any of the methods listed below:

Click the "Report Issue" ( ) button, located in the page header.

Tip: You can select the relevant text first, to include it in your report.

Our team has already identified the following issues . We appreciate your time reviewing and reporting rendering errors we may not have found yet. Your efforts will help us improve the HTML versions for all readers, because disability should not be a barrier to accessing research. Thank you for your continued support in championing open access for all.

Have a free development cycle? Help support accessibility at arXiv! Our collaborators at LaTeXML maintain a list of packages that need conversion , and welcome developer contributions .
