##### Report GitHub Issue

Content selection saved. Describe the issue below:

# Bitune: Leveraging Bidirectional Attention to Improve Decoder-Only LLMs

###### Abstract

Decoder-only large language models typically rely solely on masked causal attention, which limits their expressiveness by restricting information flow to one direction. We propose Bitune, a method that enhances pretrained decoder-only LLMs by incorporating bidirectional attention into prompt processing. We evaluate Bitune in instruction-tuning and question-answering settings, showing significant improvements in performance on commonsense reasoning, arithmetic, and language understanding tasks. Furthermore, extensive ablation studies validate the role of each component of the method, and demonstrate that Bitune is compatible with various parameter-efficient finetuning techniques and full model finetuning.

## 1 Introduction

Large Language Models (LLMs) are being deployed in numerous practical applications where humans engage with them through various forms of natural language interaction. In use cases such as general purpose assistants ( OpenAI, 2024 ) , medical diagnosticians ( Thirunavukarasu et al., 2023 ) , game-conversation generation ( Cox and Ooi, 2023 ) or coding-assistants ( Roziere et al., 2023 ) , the ability for an LLM to precisely interpret and respond to user inputs is of primary concern.

Correspondingly, Instruction-Tuning (IT) ( Chung et al., 2024 ; Ouyang et al., 2022a ) is the prevailing paradigm for finetuning LLMs after their self-supervised pretraining phase to improve them for such tasks. Here, the model is trained on a dataset comprised of pairs of instructions and corresponding responses. Given the instruction-with-response structure of IT data, the generation of an LLM response can be divided into two phases: first, converting the instruction into key and value embeddings, which we refer to as instruction features; second, using these features to autoregressively generate an answer. Due to this task’s inherently conditional nature, the instruction features’ effectiveness is crucial for obtaining high-quality model outputs.

In the past, bidirectional attention ( Schuster and Paliwal, 1997 ) has been a key technique for obtaining stronger features for words or tokens. This is because the meaning of a word depends greatly on its context. In particular, for some words in a sentence, the information that comes later might be far more informative for generating a meaningful representation and resolving ambiguities. With only uni-directional causal attention, where the representation of each word is restricted to depend solely on the words that came before, this cannot be achieved. This is the reason why many previous transformers such as encoder-only BERT ( Devlin et al., 2019 ) and encoder-decoder T5 ( Raffel et al., 2020 ) employed bidirectional attention to improve the encoding of the input and why tasks like text retrieval ( Lewis et al., 2020 ; Li and Li, 2023 ) still rely on this.

However, in the context of LLMs, architectures utilizing bidirectional attention have fallen out of favor, as decoder-only models such as GPT ( OpenAI, 2024 ) and Llama ( AI@Meta, 2024 ) have focused on and vastly improved the generative performance of language models. These architectures are trained by large volumes of data with next-token prediction, eschewing any look-ahead mechanism for the sake of better autoregressive modeling. As there is simply more unlabeled data available for pretraining, training a decoder-only architecture on unlabeled data, and then finetuning it for tasks with instruction-tuning, is the best modus operandi of today ( Wang et al., 2022 ) . However, with this switch to decoder-only architectures, we lost bidirectional attention in the process. As we know this can improve feature representations for instructions, we set out to re-introduce bidirectional attention, such that it can be integrated into pretrained decoder-only LLMs.

Our new method Bitune adds bidirectional attention to decoder-only architectures and combines it with causal attention to generate two sets of instruction features, using two different sets of weights. These features are then integrated, utilizing learnable mixing coefficients, and later used as the KV-cache for response generation. Notably, the autoregressive response generation process remains unaffected by the bidirectional attention and continues to be causal. By realizing these adaptations with parameter-efficient finetuning methods, we introduce only a minimal set of new parameters.

Overall, our contributions are as follows: • We propose a novel method, Bitune, that improves the performance of pretrained decoder-only LLMs in instruction-following and question-answering settings.

• We evaluate the method on multiple downstream tasks, showing consistent improvements over the baselines.

• We conduct an extensive ablation study investigating the necessity of each component of the method, and showing the method’s PEFT-agnosticism, as well as its effectiveness in full finetuning scenarios.

## 2 Bidirectional Instruction-Tuning

In the instruction-tuning setting ( Ouyang et al., 2022b ; Zhang et al., 2024 ) , a dataset 𝒟 \mathcal{D} consists of instruction-answer pairs that are used to adapt the model in a supervised fashion. Formally, a dataset of size N N can be described as 𝒟 = { q , a } i = 1 N \mathcal{D}=\{q,a\}^{N}_{i=1} , where q q and a a are instructions and answers. The training objective is to model p ⁡ ( a | q ) p(a|q) in an autoregressive manner: This means the answer is generated one token at a time, such that token a i a_{i} at position i i has access to all earlier tokens: p ⁡ ( a | q ) = Π i = 1 | a | ​ p ​ ( a i | a 1 , … ​ a i − 1 , q ) , p(a|q)=\Pi^{|a|}_{i=1}p(a_{i}|a_{1},\dots a_{i-1},q), where | a | |a| denotes the length of the answer. Note how compared to the regular language modeling objective, the response is already conditional (on the instruction q q ) even for the first generated token.

This naturally leads response-generation to be divided into two phases: prefilling and decoding. During the prefilling phase, the entire instruction – also often called a prompt – is processed concurrently to generate a series of features to be stored. For a Transformer architecture ( Vaswani et al., 2017 ) , these features are those of the key and value vectors, which can be stored in a KV-cache to avoid costly recomputations. During the subsequent decoding phase, the model generates output tokens sequentially, one token at a time, based on the KV-cache of the instruction and the already generated tokens.

In this work, we introduce Bitune, a method to leverage this two-phase process to improve instruction-tuning of language models. In our approach, the model processes the instruction with both causal and bidirectional attention using separate sets of parameters, leading to an enhanced KV-cache that is then used to condition the answer. Figure 1 provides an overview of the method, while Algorithm 1 presents pseudocode for the inference process.

#### Two Sets of Features.

In Bitune, the model performs two passes on the instruction to obtain two kinds of features for every transformer block. Namely, a set of c ausal features that the model was originally trained to process and utilize, K c = X c ​ W k ​ c , V c = X c ​ W v ​ c , K_{\color[rgb]{1,0,0}c}=X_{\color[rgb]{1,0,0}c}W_{k{\color[rgb]{1,0,0}c}},\quad V_{\color[rgb]{1,0,0}c}=X_{\color[rgb]{1,0,0}c}W_{v{\color[rgb]{1,0,0}c}}, (1) and a set of b idirectional features encoding the instruction without the constraints of causal masking, K b = X b ​ W k ​ b , V b = X b ​ W v ​ b . K_{\color[rgb]{0,0,1}b}=X_{\color[rgb]{0,0,1}b}W_{k{\color[rgb]{0,0,1}b}},\quad V_{\color[rgb]{0,0,1}b}=X_{\color[rgb]{0,0,1}b}W_{v{\color[rgb]{0,0,1}b}}. (2) To allow the model to learn how to process the causal and bidirectional features differently, we introduce two sets of weights: one for the bidirectional pass on the instruction ( W k ​ b W_{k{\color[rgb]{0,0,1}b}} , W v ​ b W_{v{\color[rgb]{0,0,1}b}} ) and another for the causal pass on the instruction, which is also used for the causal generation of answer tokens ( W k ​ c W_{k{\color[rgb]{1,0,0}c}} , W v ​ c W_{v{\color[rgb]{1,0,0}c}} ).

In the case of the first block of the model, representations X c X_{\color[rgb]{1,0,0}c} , X b X_{\color[rgb]{0,0,1}b} are the initial token embeddings. In other cases, they are the output of the preceding block and were processed by different components including the self-attention mechanism, which can be defined as: Attn ​ ( Q , K , V , M ) = σ ⁡ ( Q ​ K T / d k + M ) ​ V , \text{Attn}(Q,K,V,M)=\sigma({QK^{T}}/{\sqrt{d_{k}}}+M)V, (3) where σ \sigma is the softmax, Q Q are the queries, M M is the attention mask, and d k d_{k} is the dimension of keys and queries. For the causal pass, the mask M c M_{\color[rgb]{1,0,0}c} enforces causality by masking future tokens, such that tokens j j can only attend to earlier tokens i ≤ j i\leq j , while for the bidirectional pass, no masking is applied: M c ​ ( i , j ) \displaystyle M_{{{\color[rgb]{1,0,0}c}}}(i,j) = { 0 if ​ i ≤ j − ∞ if ​ i > j \displaystyle=\begin{cases}0&\text{if }i\leq j\\ -\infty&\text{if }i>j\end{cases} (4) M b ​ ( i , j ) \displaystyle M_{\color[rgb]{0,0,1}b}(i,j) = 0 \displaystyle=0 (5) The final KV-cache is obtained by a learnable convex combination of causal and bidirectional features, K Bitune \displaystyle K_{\texttt{Bitune}} = K c ⋅ ( 1 − α k ) + K b ⋅ α k \displaystyle=K_{\color[rgb]{1,0,0}c}\cdot(1-\alpha_{k})+K_{\color[rgb]{0,0,1}b}\cdot\alpha_{k} (6) V Bitune \displaystyle V_{\texttt{Bitune}} = V c ⋅ ( 1 − α v ) + V b ⋅ α v , \displaystyle=V_{\color[rgb]{1,0,0}c}\cdot(1-\alpha_{v})+V_{\color[rgb]{0,0,1}b}\cdot\alpha_{v}, (7) where α \alpha represents the bidirectional-to-causal ratio of features. This ratio is parameterised as α j = | θ j | / ( θ init + | θ j | ) , j ∈ { k , v } \alpha_{j}={|\theta_{j}|}/({\theta_{\text{init}}+|\theta_{j}|}),\quad j\in\{k,v\} (8) where θ j \theta_{j} is a learnable mixing coefficient per transformer block, and θ init \theta_{\text{init}} is a hyperparameter defining the initial value of θ j \theta_{j} . The mixing coefficients are learnable to allow each block to independently adjust the balance between bidirectional and causal features throughout the training.

#### Parameter Efficient Fine-tuning

Note that the components of the model, other than the key and value projections, can have their own separate sets of weights as well. In the case of full finetuning, this approach would require an additional set of full weights, which is impractical for large models.

Instead, we adapt our model using parameter-efficient finetuning methods. These introduce only a fraction of trainable parameters, making it viable to have two modified variants of the model within a single forward pass. In the default configuration of our method, we utilize the Low-Rank Adaptation (LoRA) of Hu et al. (2022) to adapt the model. However, Bitune can utilize different methods for updating the weights, including full model finetuning and other parameter-efficient techniques, as demonstrated in our ablations section.

## 3 Experiments

### 3.1 Instruction-Tuning

Our core experiments involve training pretrained language models on an instruction-tuning dataset and zero-shot evaluating them on downstream tasks. We evaluate Bitune on multiple models, comparing results to standard finetuning with LoRA, and zero-shot results of pretrained models without finetuning.

Specifically, we use a subset of the cleaned UltraFeedback ( Cui et al., 2023 ) dataset, which contains instructions and corresponding answers generated by various LLMs. From this dataset, we select completions generated by GPT-4 ( OpenAI, 2024 ) , ensuring high-quality responses for training. To fit every model on a single GPU, we filter out samples longer than 512 tokens, which leaves us with roughly 10,000 samples for training. For results on another instruction-tuning dataset, please see the Appendix A.6 .

We test the method on pretrained decoder-only language models of two different scales of approximately 2 billion and 7 billion parameters. The specific models used in our experiments are: Gemma 2B and 7B ( Gemma Team et al., 2024 ) , Llama2 7B ( Touvron et al., 2023 ) and Llama3 8B ( AI@Meta, 2024 ) , and Phi-2 ( Li et al., 2023 ) , which has 2.7 billion parameters. We use HuggingFace Transformers ( Wolf et al., 2020 ) implementation of these models.

For updating the weights we use the HuggingFace PEFT ( Mangrulkar et al., 2022 ) implementation of LoRA, with the default rank of 8, and apply it to all linear layers of MLP and self-attention components of the model. We compare Bitune with the following three baselines: Pretrained - initial model without any finetuning; LoRA - model finetuned with LoRA without Bitune-specific modifications, using rank of 8 as used in our method; and LoRA 16 {}_{\text{16}} - model finetuned with LoRA, using a rank of 16 to provide a fair comparison in terms of the number of parameters, as our method introduces two sets of weights.

For each model, we tune the learning rate on the LoRA baseline using steps on the approximate logarithmic scale ( 1 ​ e − 4 1\mathrm{e}{-4} , 3 ​ e − 4 3\mathrm{e}{-4} , 1 ​ e − 3 1\mathrm{e}{-3} , 3 ​ e − 3 3\mathrm{e}{-3} ), and then apply the same rate to the other approaches. Note that this potentially puts our method at a disadvantage compared to the LoRA baseline. All hyperparameters are reported in the Appendix A.2 .

Models are evaluated zero-shot on multiple-choice tasks to assess their performance. For commonsense reasoning, we use the PIQA ( Bisk et al., 2020 ) , CommonsenseQA ( Talmor et al., 2019 ) , ARC-Challenge ( Clark et al., 2018 ) , and SIQA ( Sap et al., 2019 ) datasets, while for language understanding, we use the MMLU ( Hendrycks et al., 2021 ) benchmark. Each task consists of a series of questions, each with multiple choices, where only one answer is correct. As the tasks follow the question-answer pattern, they are compatible with the instruction-tuning setting.

For evaluation, we use the Language Model Evaluation Harness framework ( Gao et al., 2023 ) . This framework formats each question using a predefined template, tokenizes the question-choice pairs, runs them through the model, and compares the log-likelihoods of the choices to determine the selected answer. For each model and approach configuration, we conduct experiments using three different random seeds, and average the results.

Models are loaded and trained using bfloat16 precision, except for the mixing part, which operates in the full 32-bit floating-point format. This high level of precision for the mixing of features is important, as minor numerical inaccuracies in the learnable coefficients and intermediate results of the mixing operation may lead to significant deviations in the model’s behavior.

In the decoding phase of the inference with Bitune, to initiate generation, the model requires at least a single token to obtain a set of attention queries , in addition to the keys and values extracted from the instruction. To facilitate this, one can introduce a new learnable <sep> token that would be placed at the beginning of modeled answer, or utilize an existing token. For our experiments, we opted to move the last token of the instruction template to the beginning of the modeled answer. For details on the instruction template used, please refer to the section A.10 of the Appendix.

#### Results.

Table 1 shows consistent and significant gains after instruction-tuning with Bitune, with the highest gains seen on the Gemma-2B model, showing a 4 percentage point (pp) improvement over the baseline LoRA and a 9.3 pp improvement over the pretrained model. For the other models, the average gains over baseline finetuning are equal to 1.8, 1.4, and 0.9 pp, for Llama3-8B, Llama2-7B, and Phi-2 respectively.

It is worth noting that the Gemma-7B model shows the lowest average improvement across all tasks, with merely 0.1 pp gain over the baseline finetuning. It is also a single case where the baseline pretrained model achieved the highest score on a task, MMLU, with degraded performance in all fine-tuning approaches. However, this is not an issue with the model’s scale, as significant gains are observed with the Llama2-7B and Llama3-8B models.

### 3.2 Downstream Task Training

This complementary experiment verifies whether Bitune increases the capacity of the model within the narrow scope of a single task. It follows the setup from the instruction-tuning experiments with a few changes. Namely, models are not instruction-tuned but trained separately for each evaluation task using the corresponding training set. We use PIQA, ARC, CSQA, and SIQA introduced earlier, and an additional arithmetic task, GSM8K ( Cobbe et al., 2021 ) .

GSM8K differs from the other tasks, where we compare log-likelihoods of predefined answers, as it requires the model to generate a full answer token-by-token, including the intermediate step-by-step reasoning. The final answer follows a specific pattern, making it feasible to extract the answer using methods such as regular expressions as the model learns to adhere to this pattern during training.

#### Results.

Table 2 presents the results, demonstrating improvements when finetuning on the downstream tasks with Bitune, similar to those seen with instruction-tuning. While there are a few cases where the baseline finetuning achieves better results on specific tasks, when considering the average gains, applying our method is beneficial across all models. Most importantly, on the GSM8K dataset, we see consistent high gains, suggesting that our method improves the model’s reasoning ability in generative tasks. We present additional results on GSM8K with a 22B parameter model in the Appendix A.7 .

Similar to the instruction-tuning results, the highest gains are observed on the Gemma-2B model, while the lowest on the Gemma-7B. This indicates that the effectiveness of our method depends on the specific model used.

### 3.3 Chain-of-Thought Reasoning

To further test the effectiveness of our method on generative tasks that require explicit reasoning, we created four additional training sets for PIQA, ARC, CSQA, and GSM8K. Each set was distilled from the GPT-4.1 model ( OpenAI, 2025 ) by prompting it to solve every training-split question step-by-step; the resulting reasoning traces were then used to finetune Gemma-2B and Llama-3-8B on each benchmark separately. At evaluation time the models generated a full answer, including intermediate reasoning, and scores were averaged over three random seeds.

The original versions of these benchmarks supply only the final label, forcing a model trained on them to perform all reasoning in latent space and yielding short generations that do not reflect real-world usage. Our distilled chain-of-thought data instead mirrors the way large language models are typically invoked, producing longer, multi-step explanations before the answer, thereby providing a more faithful test bed. Moreover, because the public test sets may already appear in pre-training corpora, training the models to answer the same questions in a custom, step-by-step format reduces the risk that apparent gains stem from data contamination. The prompts used to distill the datasets, along with example completions, are available in Appendix A.9 .

#### Results.

Table 3 shows that Bitune improves performance on chain-of-thought reasoning tasks, raising average accuracy by 2.4 pp for Gemma-2B and 1.3 pp for Llama-3-8B.

### 3.4 Inference Speed Comparison

During inference, Bitune performs two forward passes over the instruction sequence and merges the resulting features, which affects prefilling runtime. We compare inference time for Gemma-2B on a long-context instruction of 2000 tokens and report the time required to prefill this instruction and to generate 2000 subsequent tokens on a single A100 GPU.

Table 4 shows that the extra latency for processing the instruction is negligible because most of the computation time is spent on autoregressive answer generation.

### 3.5 Ablations

We conduct an ablation study on Bitune using the same experimental setup as in the instruction-tuning experiment. For this purpose, two models are used: Gemma-2B and Llama3-8B, representing different size scales and model families.

#### Component Removal

To verify the necessity of each component of the method, we remove selected parts to answer the following questions:

• Can we simply modify the attention mask to apply bidirectional attention on the prompt, without using separate weights and mixing? - We test this simplest variant, which we refer to as Naive Bidir.

• Do we need two sets of features? Is it sufficient to obtain bidirectional features from the prompt using different weights than those used for causal answer generation? - We remove the part responsible for generating the set of causal features, and therefore also the mixing component; we refer to this as No Mixing .

• Are the gains solely from mixing two sets of features generated with different weights, or is bidirectional attention necessary? - Here we keep the attention mask causal to generate both sets of features, which we refer to as Only Causal .

• Do we need separate weights, or can the same weights be used to generate both causal and bidirectional features? - To answer this question, we do not introduce the second set of weights and use the same LoRA for both passes on the prompt, calling it Shared Weights .

The results, averaged over three seeds and presented in Table 5 , indicate that all variants of Bitune lead to gains over the baseline LoRA finetuning. However, the highest gains are observed in the full variant of Bitune, demonstrating that each component contributes to the method’s effectiveness.

#### Different PEFT Methods

To verify the impact of different PEFT methods on the performance of our method, we compare Bitune in combination with the following techniques: LoRA ( Hu et al., 2022 ) , that reparametrizes weight updates as a multiplication of two low-rank matrices; DoRA ( Liu et al., 2024 ) , which decomposes these weight updates into direction and magnitude; and IA3 ( Liu et al., 2022 ) , that instead rescales activations with learnable vectors.

The results are shown in Table 6 . We find consistent gains across all three PEFT methods we analyze, with gains ranging from + 1.6 % +1.6\% to + 4.0 % +4.0\% for averaged accuracy. This demonstrates that Bitune is PEFT-agnostic and can be combined with existing and future innovations in PEFT methods.

#### Full Finetuning

Additionally, we test whether Bitune leads to gains with full finetuning ( Full-FT ), by optimizing two sets of full model’s parameters. We conduct experiments on Gemma-2B model, and compare results with standard Full-FT baseline. The results in Table 7 demonstrate that Bitune improves the model’s performance even in full finetuning scenarios.

#### Attention Mask of Second Pass

We test another option for the attention mask of the second pass on the instruction. We transpose the causal attention mask, blocking information flow from the past tokens, and allowing from the future tokens - we call it anti-causal attention mask.

Results shown in Table 8 indicate that the instruction has to be processed with full bidirectional attention to achieve the highest gains. Combining causal and anti-causal features independently does not lead to the same high performance.

## 4 Related Work

Our approach shares similarities with the concept of "prefix language modeling", which enables a decoder-only model to handle bidirectional context within a prefix (instruction) while maintaining causal generation for the output sequence. The prefix-LM architecture was introduced by Liu et al. (2018) and further explored and popularized by Raffel et al. (2020) . In their work on T5, Raffel et al. (2020) pretrained the prefix-LM architecture alongside other architectures, such as encoder-decoder and decoder-only models, demonstrating that prefix-LM outperforms decoder-only models on both training objectives: denoising and language modeling.

The prefix-LM approach has been used in UniLM ( Dong et al., 2019 ) , which trains a single transformer on three types of language modeling tasks: unidirectional, bidirectional, and sequence-to-sequence prediction. UniLM employs a shared Transformer network and utilizes specific self-attention masks to control the context that predictions are conditioned on, where the sequence-to-sequence task is equivalent to the prefix-LM approach.

Additionally, UL2 ( Tay et al., 2023 ) introduces a pretraining objective called "Mixture of Denoisers", which combines various denoising strategies, including the prefix-LM approach. Lastly, XLNet ( Yang et al., 2019 ) also allows for non-causal word ordering by allowing random permutations to be used with a next-token prediction objective.

All these works focused on the model pretraining . As for the utilization of pretrained causal language models, Springer et al. (2024) show in their work that simply repeating the input to these models improves the quality of token embeddings for text-retrieval. This work addresses the limitation that token embeddings in autoregressive models cannot contain information from tokens appearing later in the input. By repeating the input twice, the early tokens are allowed to encode information about later tokens, thereby improving the quality of the embeddings. Another approach, LLM2Vec ( BehnamGhader et al., 2024 ) , demonstrates that pretrained causal LLMs can be effectively converted to BERT-like encoders. It can be done by enabling bidirectional attention, training the model on the objective of masked token prediction, and applying unsupervised contrastive learning.

#### Bitune vs. Prefix-LM.

Both Bitune and the classic prefix-LM masking scheme grant full bidirectional access to the instruction prefix. The key difference is that Bitune is a hybrid approach designed for the optimal adaptation of decoder-only models. Existing large language models are almost always pre-trained as pure decoder-only networks ; simply replacing the causal mask with the prefix-LM masking scheme before finetuning therefore discards the causal features encoded during pretraining and forces the model to relearn the mechanics of bidirectional attention over the prefix tokens. Bitune keeps the original causal stream intact and adds a second bidirectional pass, injecting fresh capacity into the model. Finetuning then proceeds in a single architecture that unifies the two attention regimes. Our ablation study (Section 3.5 ) confirms the payoff: Bitune yields larger gains than straightforward “prefix-LM conversion” (ablation Naive Bidir ). Whether the same advantage holds when both schemes are trained from scratch remains an open question.

## 5 Conclusion

This work proposes a method that exploits the inherent instruction–answer structure of IT datasets to incorporate bidirectional attention into pretrained decoder-only models. Bitune demonstrates general applicability across different models and scales, and it consistently improves performance across commonsense reasoning, arithmetic, and language understanding tasks. We further demonstrate that the method is compatible with different existing PEFT methods and will likely benefit from further developments in this area.

## Limitations

During standard instruction-tuning training, the instruction and the answer are processed in a single forward pass. In our method, this processing is explicitly split into phases - extracting instruction features with causal attention, bidirectional attention, and answer modeling, which results in increased both training time and memory usage.

However, this is a minor limitation in the context of instruction-tuning, since typically smaller datasets are used compared to pretraining, leading to relatively short training times. Furthermore, as shown in Section 3.4 , the additional latency during prefilling at inference time is negligible, since most time is spent on sequential token generation.

## References

AI@Meta (2024) AI@Meta. 2024. Llama 3 model card .

BehnamGhader et al. (2024) Parishad BehnamGhader, Vaibhav Adlakha, Marius Mosbach, Dzmitry Bahdanau, Nicolas Chapados, and Siva Reddy. 2024. LLM2Vec: Large language models are secretly powerful text encoders. arXiv preprint: arXiv:2404.05961 .

Bisk et al. (2020) Yonatan Bisk, Rowan Zellers, Ronan Le Bras, Jianfeng Gao, and Yejin Choi. 2020. Piqa: Reasoning about physical commonsense in natural language. In AAAI .

Chung et al. (2024) Hyung Won Chung, Le Hou, Shayne Longpre, Barret Zoph, Yi Tay, William Fedus, Eric Li, Xuezhi Wang, Mostafa Dehghani, Siddhartha Brahma, Albert Webson, Shixiang Shane Gu, Zhuyun Dai, Mirac Suzgun, Xinyun Chen, Aakanksha Chowdhery, Sharan Narang, Gaurav Mishra, Adams Yu, Vincent Zhao, Yanping Huang, Andrew Dai, Hongkun Yu, Slav Petrov, Ed H. Chi, Jeff Dean, Jacob Devlin, Adam Roberts, Denny Zhou, Quoc V. Le, and Jason Wei. 2024. Scaling instruction-finetuned language models. JMLR .

Clark et al. (2018) Peter Clark, Isaac Cowhey, Oren Etzioni, Tushar Khot, Ashish Sabharwal, Carissa Schoenick, and Oyvind Tafjord. 2018. Think you have solved question answering? try arc, the ai2 reasoning challenge . Preprint , arXiv:1803.05457.

Cobbe et al. (2021) Karl Cobbe, Vineet Kosaraju, Mohammad Bavarian, Mark Chen, Heewoo Jun, Lukasz Kaiser, Matthias Plappert, Jerry Tworek, Jacob Hilton, Reiichiro Nakano, Christopher Hesse, and John Schulman. 2021. Training verifiers to solve math word problems . Preprint , arXiv:2110.14168.

Cox and Ooi (2023) Samuel Rhys Cox and Wei Tsang Ooi. 2023. Conversational interactions with npcs in llm-driven gaming: Guidelines from a content analysis of player feedback. In International Workshop on Chatbot Research and Design .

Cui et al. (2023) Ganqu Cui, Lifan Yuan, Ning Ding, Guanming Yao, Wei Zhu, Yuan Ni, Guotong Xie, Zhiyuan Liu, and Maosong Sun. 2023. Ultrafeedback: Boosting language models with high-quality feedback. arXiv:2310.01377 .

Devlin et al. (2019) Jacob Devlin, Ming-Wei Chang, Kenton Lee, and Kristina Toutanova. 2019. BERT: Pre-training of deep bidirectional transformers for language understanding. In ACL .

Dong et al. (2019) Li Dong, Nan Yang, Wenhui Wang, Furu Wei, Xiaodong Liu, Yu Wang, Jianfeng Gao, Ming Zhou, and Hsiao-Wuen Hon. 2019. Unified language model pre-training for natural language understanding and generation. In NeurIPS .

Gao et al. (2023) Leo Gao, Jonathan Tow, Baber Abbasi, Stella Biderman, Sid Black, Anthony DiPofi, Charles Foster, Laurence Golding, Jeffrey Hsu, Alain Le Noac’h, Haonan Li, Kyle McDonell, Niklas Muennighoff, Chris Ociepa, Jason Phang, Laria Reynolds, Hailey Schoelkopf, Aviya Skowron, Lintang Sutawika, Eric Tang, Anish Thite, Ben Wang, Kevin Wang, and Andy Zou. 2023. A framework for few-shot language model evaluation .

Gemma Team et al. (2024) Gemma Team, Thomas Mesnard, Cassidy Hardin, Robert Dadashi, Surya Bhupatiraju, Shreya Pathak, Laurent Sifre, Morgane Rivière, Mihir Sanjay Kale, Juliette Love, Pouya Tafti, Léonard Hussenot, Pier Giuseppe Sessa, Aakanksha Chowdhery, Adam Roberts, Aditya Barua, Alex Botev, Alex Castro-Ros, Ambrose Slone, Amélie Héliou, Andrea Tacchetti, Anna Bulanova, Antonia Paterson, Beth Tsai, Bobak Shahriari, Charline Le Lan, Christopher A. Choquette-Choo, Clément Crepy, Daniel Cer, Daphne Ippolito, David Reid, Elena Buchatskaya, Eric Ni, Eric Noland, Geng Yan, George Tucker, George-Christian Muraru, Grigory Rozhdestvenskiy, Henryk Michalewski, Ian Tenney, Ivan Grishchenko, Jacob Austin, James Keeling, Jane Labanowski, Jean-Baptiste Lespiau, Jeff Stanway, Jenny Brennan, Jeremy Chen, Johan Ferret, Justin Chiu, Justin Mao-Jones, Katherine Lee, Kathy Yu, Katie Millican, Lars Lowe Sjoesund, Lisa Lee, Lucas Dixon, Machel Reid, Maciej Mikuła, Mateo Wirth, Michael Sharman, Nikolai Chinaev, Nithum Thain, Olivier Bachem, Oscar Chang, Oscar Wahltinez, Paige Bailey, Paul Michel, Petko Yotov, Rahma Chaabouni, Ramona Comanescu, Reena Jana, Rohan Anil, Ross McIlroy, Ruibo Liu, Ryan Mullins, Samuel L Smith, Sebastian Borgeaud, Sertan Girgin, Sholto Douglas, Shree Pandya, Siamak Shakeri, Soham De, Ted Klimenko, Tom Hennigan, Vlad Feinberg, Wojciech Stokowiec, Yu hui Chen, Zafarali Ahmed, Zhitao Gong, Tris Warkentin, Ludovic Peran, Minh Giang, Clément Farabet, Oriol Vinyals, Jeff Dean, Koray Kavukcuoglu, Demis Hassabis, Zoubin Ghahramani, Douglas Eck, Joelle Barral, Fernando Pereira, Eli Collins, Armand Joulin, Noah Fiedel, Evan Senter, Alek Andreev, and Kathleen Kenealy. 2024. Gemma: Open models based on gemini research and technology. arxiv preprint: arXiv:2403.08295 .

Hendrycks et al. (2021) Dan Hendrycks, Collin Burns, Steven Basart, Andy Zou, Mantas Mazeika, Dawn Song, and Jacob Steinhardt. 2021. Measuring massive multitask language understanding. In ICLR .

Hu et al. (2022) Edward J Hu, yelong shen, Phillip Wallis, Zeyuan Allen-Zhu, Yuanzhi Li, Shean Wang, Lu Wang, and Weizhu Chen. 2022. LoRA: Low-rank adaptation of large language models. In ICLR .

Lewis et al. (2020) Patrick Lewis, Ethan Perez, Aleksandra Piktus, Fabio Petroni, Vladimir Karpukhin, Naman Goyal, Heinrich Küttler, Mike Lewis, Wen-tau Yih, Tim Rocktäschel, et al. 2020. Retrieval-augmented generation for knowledge-intensive nlp tasks. In NeurIPS .

Lhoest et al. (2021) Quentin Lhoest, Albert Villanova del Moral, Yacine Jernite, Abhishek Thakur, Patrick von Platen, Suraj Patil, Julien Chaumond, Mariama Drame, Julien Plu, Lewis Tunstall, Joe Davison, Mario Šaško, Gunjan Chhablani, Bhavitvya Malik, Simon Brandeis, Teven Le Scao, Victor Sanh, Canwen Xu, Nicolas Patry, Angelina McMillan-Major, Philipp Schmid, Sylvain Gugger, Clément Delangue, Théo Matussière, Lysandre Debut, Stas Bekman, Pierric Cistac, Thibault Goehringer, Victor Mustar, François Lagunas, Alexander Rush, and Thomas Wolf. 2021. Datasets: A community library for natural language processing. In EMNLP: System Demonstrations .

Li and Li (2023) Xianming Li and Jing Li. 2023. Angle-optimized text embeddings. ACL .

Li et al. (2023) Yuanzhi Li, Sébastien Bubeck, Ronen Eldan, Allie Del Giorno, Suriya Gunasekar, and Yin Tat Lee. 2023. Textbooks are all you need ii: phi-1.5 technical report. arXiv:2309.05463 .

Liu et al. (2022) Haokun Liu, Derek Tam, Muqeeth Mohammed, Jay Mohta, Tenghao Huang, Mohit Bansal, and Colin Raffel. 2022. Few-shot parameter-efficient fine-tuning is better and cheaper than in-context learning. In NeurIPS .

Liu et al. (2018) Peter J. Liu, Mohammad Saleh, Etienne Pot, Ben Goodrich, Ryan Sepassi, Lukasz Kaiser, and Noam Shazeer. 2018. Generating wikipedia by summarizing long sequences. In ICLR .

Liu et al. (2024) Shih-Yang Liu, Chien-Yi Wang, Hongxu Yin, Pavlo Molchanov, Yu-Chiang Frank Wang, Kwang-Ting Cheng, and Min-Hung Chen. 2024. Dora: Weight-decomposed low-rank adaptation. In ICML .

Mangrulkar et al. (2022) Sourab Mangrulkar, Sylvain Gugger, Lysandre Debut, Younes Belkada, Sayak Paul, and Benjamin Bossan. 2022. PEFT: State-of-the-art parameter-efficient fine-tuning methods. https://github.com/huggingface/peft .

Mistral AI (2024) Mistral AI. 2024. Codestral: Hello, World! — mistral.ai. https://mistral.ai/news/codestral/ . [Accessed 01-10-2024].

OpenAI (2024) OpenAI. 2024. Gpt-4 technical report. arXiv:2303.08774 .

OpenAI (2025) OpenAI. 2025. GPT-4.1 (large language model) . Accessed 2025-05-19.

Ouyang et al. (2022a) Long Ouyang, Jeff Wu, Xu Jiang, Diogo Almeida, Carroll L. Wainwright, Pamela Mishkin, Chong Zhang, Sandhini Agarwal, Katarina Slama, Alex Ray, John Schulman, Jacob Hilton, Fraser Kelton, Luke Miller, Maddie Simens, Amanda Askell, Peter Welinder, Paul Christiano, Jan Leike, and Ryan Lowe. 2022a. Training language models to follow instructions with human feedback. In NeurIPS .

Ouyang et al. (2022b) Long Ouyang, Jeffrey Wu, Xu Jiang, Diogo Almeida, Carroll Wainwright, Pamela Mishkin, Chong Zhang, Sandhini Agarwal, Katarina Slama, Alex Ray, et al. 2022b. Training language models to follow instructions with human feedback. In NeurIPS .

Raffel et al. (2020) Colin Raffel, Noam Shazeer, Adam Roberts, Katherine Lee, Sharan Narang, Michael Matena, Yanqi Zhou, Wei Li, and Peter J. Liu. 2020. Exploring the limits of transfer learning with a unified text-to-text transformer. JMLR .

Roziere et al. (2023) Baptiste Roziere, Jonas Gehring, Fabian Gloeckle, Sten Sootla, Itai Gat, Xiaoqing Ellen Tan, Yossi Adi, Jingyu Liu, Tal Remez, Jérémy Rapin, et al. 2023. Code llama: Open foundation models for code. arXiv:2308.12950 .

Sap et al. (2019) Maarten Sap, Hannah Rashkin, Derek Chen, Ronan Le Bras, and Yejin Choi. 2019. Social iqa: Commonsense reasoning about social interactions. In EMNLP .

Schuster and Paliwal (1997) Mike Schuster and Kuldip K. Paliwal. 1997. Bidirectional recurrent neural networks. In IEEE Transactions on Signal Processing .

Springer et al. (2024) Jacob Mitchell Springer, Suhas Kotha, Daniel Fried, Graham Neubig, and Aditi Raghunathan. 2024. Repetition improves language model embeddings. arviv preprint arXiv2402.15449 .

Talmor et al. (2019) Alon Talmor, Jonathan Herzig, Nicholas Lourie, and Jonathan Berant. 2019. CommonsenseQA: A question answering challenge targeting commonsense knowledge. In NAACL .

Taori et al. (2023) Rohan Taori, Ishaan Gulrajani, Tianyi Zhang, Yann Dubois, Xuechen Li, Carlos Guestrin, Percy Liang, and Tatsunori B. Hashimoto. 2023. Stanford alpaca: An instruction-following llama model. https://github.com/tatsu-lab/stanford_alpaca .

Tay et al. (2023) Yi Tay, Mostafa Dehghani, Vinh Q. Tran, Xavier Garcia, Jason Wei, Xuezhi Wang, Hyung Won Chung, Dara Bahri, Tal Schuster, Steven Zheng, Denny Zhou, Neil Houlsby, and Donald Metzler. 2023. UL2: Unifying language learning paradigms. In ICLR .

Thirunavukarasu et al. (2023) Arun James Thirunavukarasu, Darren Shu Jeng Ting, Kabilan Elangovan, Laura Gutierrez, Ting Fang Tan, and Daniel Shu Wei Ting. 2023. Large language models in medicine. Nature medicine .

Touvron et al. (2023) Hugo Touvron, Louis Martin, Kevin Stone, Peter Albert, Amjad Almahairi, Yasmine Babaei, Nikolay Bashlykov, Soumya Batra, Prajjwal Bhargava, Shruti Bhosale, Dan Bikel, Lukas Blecher, Cristian Canton Ferrer, Moya Chen, Guillem Cucurull, David Esiobu, Jude Fernandes, Jeremy Fu, Wenyin Fu, Brian Fuller, Cynthia Gao, Vedanuj Goswami, Naman Goyal, Anthony Hartshorn, Saghar Hosseini, Rui Hou, Hakan Inan, Marcin Kardas, Viktor Kerkez, Madian Khabsa, Isabel Kloumann, Artem Korenev, Punit Singh Koura, Marie-Anne Lachaux, Thibaut Lavril, Jenya Lee, Diana Liskovich, Yinghai Lu, Yuning Mao, Xavier Martinet, Todor Mihaylov, Pushkar Mishra, Igor Molybog, Yixin Nie, Andrew Poulton, Jeremy Reizenstein, Rashi Rungta, Kalyan Saladi, Alan Schelten, Ruan Silva, Eric Michael Smith, Ranjan Subramanian, Xiaoqing Ellen Tan, Binh Tang, Ross Taylor, Adina Williams, Jian Xiang Kuan, Puxin Xu, Zheng Yan, Iliyan Zarov, Yuchen Zhang, Angela Fan, Melanie Kambadur, Sharan Narang, Aurelien Rodriguez, Robert Stojnic, Sergey Edunov, and Thomas Scialom. 2023. Llama 2: Open foundation and fine-tuned chat models. arXiv:2307.09288 .

Vaswani et al. (2017) Ashish Vaswani, Noam Shazeer, Niki Parmar, Jakob Uszkoreit, Llion Jones, Aidan N Gomez, Ł ukasz Kaiser, and Illia Polosukhin. 2017. Attention is all you need. In NeurIPS .

Wang et al. (2022) Thomas Wang, Adam Roberts, Teven Le Scao Daniel Hesslow, Hyung Won Chung, Iz Beltagy, Julien Launay, and Colin Raffel. 2022. What language model architecture and pretraining objective work best for zero-shot generalization? In ICML .

Wolf et al. (2020) Thomas Wolf, Lysandre Debut, Victor Sanh, Julien Chaumond, Clement Delangue, Anthony Moi, Pierric Cistac, Tim Rault, Rémi Louf, Morgan Funtowicz, Joe Davison, Sam Shleifer, Patrick von Platen, Clara Ma, Yacine Jernite, Julien Plu, Canwen Xu, Teven Le Scao, Sylvain Gugger, Mariama Drame, Quentin Lhoest, and Alexander M. Rush. 2020. Transformers: State-of-the-art natural language processing. In EMNLP: System Demonstrations .

Yang et al. (2019) Zhilin Yang, Zihang Dai, Yiming Yang, Jaime Carbonell, Russ R Salakhutdinov, and Quoc V Le. 2019. Xlnet: Generalized autoregressive pretraining for language understanding. NeurIPS .

Zhang et al. (2024) Shengyu Zhang, Linfeng Dong, Xiaoya Li, Sen Zhang, Xiaofei Sun, Shuhe Wang, Jiwei Li, Runyi Hu, Tianwei Zhang, Fei Wu, and Guoyin Wang. 2024. Instruction tuning for large language models: A survey. arXiv:2308.10792 .

## Appendix A Appendix

### A.1 Pseudocode for Bitune Training Step

### A.2 Hyperparameters

### A.3 Datasets

For all experiments we used HuggingFace Datasets ( Lhoest et al., 2021 ) library to obtain necessary datasets.

### A.4 Training Speed & Memory Usage

As the method introduces two additional forward passes during training, both the training speed and the memory usage are impacted. Here we present average training times and GPU memory usage on the instruction-tuning setup with 3000 update steps (30000 actual steps, due to gradient accumulation), on a single A100 GPU, for models of two different scales - Gemma-2B & Llama3-8B. Our implementation has not been optimized, which means that e.g. training times could be improved via parallelization of two passes on the prompt. Table shows average training time, peak GPU memory usage during training, and average accuracy on downstream tasks.

Using these values, one can approximate required compute to reproduce results on a given tasks, as all experiments shared the same batch size and many other hyperparameters.

### A.5 Initialization of Mixing Coefficient

The initial value of the mixing coefficient θ \theta is a hyperparameter in our method. To evaluate its impact on the performance and the training dynamics of the bidirectional-to-causal ratio of features, we conduct experiments on the instruction-tuning setup with the following values: 0.1 0.1 , 0.01 0.01 , and 0.001 0.001 .

Table 15 demonstrates that the initial value of the mixing coefficient impacts the performance, with 0.01 0.01 being the most optimal value for both models, regardless of their scale. Figure 2 shows that the initial value substantially affects the rate of change of the mixing ratio, with the higher value leading to nearly no change in the ratio, while the lower value results in sharp changes at the very beginning of the training. In Figure 3 , we also observe that after training, all layers utilize the bidirectional attention.

### A.6 Instruction-tuning on Alpaca Dataset

We tested Bitune on another, larger instruction-tuning dataset - cleaned Alpaca dataset 1 1 1 https://huggingface.co/datasets/yahma/alpaca-cleaned ( Taori et al., 2023 ) with 50,000 samples. Similarly to previous experimental settings, first we tested different learning rates for the baseline LoRA finetuning, picked the best one, and then used the same learning rate for other approaches used in the experiment - Bitune, and Naive Bidir. (introduced in the ablation study section 3.5 ). The results demonstrate that our method’s benefits extend to larger datasets as well.

### A.7 Finetuning Larger Model on GSM8K

In order to verify whether improvements hold for larger, already highly capable models, we finetune Codestral ( Mistral AI, 2024 ) with 22B parameters on the GSM8K dataset. The results, averaged over 3 random seeds, show a substantial 4.3 percentage point improvement over the baseline LoRA finetuning, indicating that Bitune can provide considerable gains even for larger models, which already have strong performance on a given task.

### A.8 Multi-Turn Setting

In our experiments, we focus on single-turn QA settings, but the approach can be extended to multi-turn chat applications in the following two ways:

(A) “Recompute” The most straightforward way is to treat the entire chat history as a prefix or query and recompute the KV cache at every new round. This allows bidirectional attention over all tokens, including previously generated answers.

(B) “Alternating” Another option is to alternate attention patterns with the following procedure: 1. Prefill the first instruction and generate the initial KV cache by merging causal and bidirectional features.

2. Generate output token by token, appending the KV of each output to the cache (the output KV uses only causal features).

3. Prefill the next instruction with both attention masks and append its KV to the cache.

4. Repeat from step 2.

### A.9 Chain of Thought Data Generation

For each train set of datasets - PIQA, ARC-Challenge, CSQA, GSM8K - we have distilled chain-of-thought completions with GPT-4.1 model.

The completions were asked to be in a specific format allowing to extract the steps, and final answer separately. We have used the following prompt templates:

Here we provide the example completions:

### A.10 Prompt Templates

Templates used to format instruction-answer pairs for a given dataset, for both training and evaluation. In all cases there is a space character at the beginning of the answer part.

### A.11 Results with Standard Deviation

Tables with complete results averaged over 3 seeds, includes standard deviation.

### A.12 Example Attention Matrices

Here we show pairs of matrices with causal and bidirectional attention scores of Bituned Gemma-2B for the first two GSM8K samples, with scores averaged over layers and heads. Source tokens are represented with the vertical axis, while target tokens (for which the attention is paid to) with the horizontal one - e.g. the first column represents attention paid to the first (BOS) token, by each other token. Darker color represents higher attention score.

### A.13 GSM8K Samples

Samples of responses to the first 20 questions from GSM8K benchmark. Shown for Llama3-8B intruction-tuned on UltraFeedback dataset - for standard finetuning with LoRA and Bitune.

## Instructions for reporting errors

We are continuing to improve HTML versions of papers, and your feedback helps enhance accessibility and mobile support. To report errors in the HTML that will help us improve conversion and rendering, choose any of the methods listed below:

Click the "Report Issue" ( ) button, located in the page header.

Tip: You can select the relevant text first, to include it in your report.

Our team has already identified the following issues . We appreciate your time reviewing and reporting rendering errors we may not have found yet. Your efforts will help us improve the HTML versions for all readers, because disability should not be a barrier to accessing research. Thank you for your continued support in championing open access for all.

Have a free development cycle? Help support accessibility at arXiv! Our collaborators at LaTeXML maintain a list of packages that need conversion , and welcome developer contributions .
