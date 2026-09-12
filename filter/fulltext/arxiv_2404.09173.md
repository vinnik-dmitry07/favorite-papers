##### Report GitHub Issue

Content selection saved. Describe the issue below:

# TransformerFAM: Feedback attention is working memory

###### Abstract

While Transformers have revolutionized deep learning, their quadratic attention complexity hinders their ability to process infinitely long inputs. We propose Feedback Attention Memory (FAM), a novel Transformer architecture that leverages a feedback loop to enable the network to attend to its own latent representations. This design fosters the emergence of working memory within the Transformer, allowing it to process indefinitely long sequences. TransformerFAM requires no additional weights, enabling seamless integration with pre-trained models. Our experiments show that TransformerFAM significantly improves Transformer performance on long-context tasks across various model sizes (1B, 8B, and 24B). These results showcase the potential to empower Large Language Models (LLMs) to process sequences of unlimited length.

## 1 Introduction

The introduction of the Transformer architecture [ 12 ] has revolutionized deep learning by permeating diverse domains and enhancing performance due to its efficacy and scalability. This scalability fuels a trend analogous to Moore’s law, which links increased model size to performance gains [ 39 ] .

The effectiveness of attention in text sequence processing was solidified through the Transformer paper. Models like BERT [ 16 ] and GPT-3 [ 33 ] further showcased the scalability of Transformer and its tendency for improved performance with increased model size. Following the replacement of LSTM [ 5 ] by Transformer in most Natural Language Processing (NLP) domains, the Vision Transformer (ViT) [ 32 ] replaced Convolutional Neural Network (CNN) [ 4 ] with Transformers in the vision domain, and Conformer (Convolution-augmented Transformer) [ 29 ] replaced LSTM in the speech domain. The Transformer has become the de facto architecture in various domains. Currently, attention serves as the leading architecture for extracting meaningful representations from homogeneous data.

The logical progression points toward extending attention capabilities to heterogeneous data. This has enabled advances in multimodal fusion (text and vision), as seen in models like DALL·E 2 [ 55 ] , Flamingo [ 54 ] and CoCa [ 53 ] . AudioLM [ 64 ] has shown that attention also excels at fusing audio and text. Consequently, Gemini [ 69 ] integrates text, images, audio, and video into a single generative model. This was possible because attention to heterogeneous data works exceptionally well.

Despite the impressive success of attention, it suffers from major drawbacks. Firstly, attention has quadratic complexity with respect to context length, which limits the capability of modeling long contexts. Secondly, it forgets information from context before attention window, unlike LSTM, which theoretically can propagate information indefinitely. We want the better architecture to be able to process arbitrarily long sequences efficiently, while preserving very long-term dependencies.

Sliding window attention is introduced [ 26 , 35 ] to handle infinitely long sequences as input. However, it disregards information beyond the effective receptive field (approximately model depth × \times window size in Fig. 1(d) ) during sequence generation. Various approaches have attempted to address the long-context problem by sparse attention [ 23 , 35 , 28 , 37 , 42 , 81 ] and linear approximated attention [ 34 , 40 , 38 , 48 ] , showing effectiveness below the 1B scale. Yet, scaling laws [ 59 ] suggest these approximations do not perform as well at GPT-3 level. Current SoTA large language model (LLM) leaderboards [ 82 ] do not feature architectures primarily relying on approximated attention.

On the other hand, Neuroscience links attention to multisensory integration [ 10 ] . Endogenous (goal-driven) and exogenous (stimulus-driven) attention are distributed throughout sensory processing regions in brain, and the brain areas correlated with the attention overlap substantially with the multisensory cortical regions involved in multisensory integration. Working memory exhibits similar distribution [ 13 ] , overlapping with attention-correlated areas. This indicates that attention is an important factor in not only multimodal fusion but also working memory.

In the human brain, working memory [ 83 ] provides a temporary memory for performing tasks. While working memory is stored in sustained activations, long-term memory is stored in weights [ 2 ] . LLMs has enormous long-term memory enough to store the entire internet [ 62 ] , but they do not have working memory. The activation of working memory is sustained by prefrontal cortical-thalamic loops [ 7 ] , which means working memory is sustained by the continuous spiking of activation within a feedback loop.

Attention has been shown to be effective for processing both homogeneous and heterogeneous data. The next natural step is to apply attention to its own latent representations through a feedback loop. We hypothesize that this next step will naturally lead to the emergence of working memory in Transformers.

###### Assumption 1 .

The attention mechanism within the feedback loop functions as working memory.

Feedback connections are prevalent in biological neural networks. Even organisms with simple neural structures, such as C. elegans (with only 302 neurons) [ 3 ] , exhibit various feedback loops, like connections from higher-level interneurons to lower-level ones [ 17 ] . However, incorporating feedback loops in Transformer is challenging. There are two main approaches. The first approach is linking the topmost layer to the bottommost [ 27 , 57 ] . However, this cannot model feedback between interneurons, and this has only one global working memory. The second approach is within-transformer-block feedback: the output activation of a Transformer layer is fed back as input to the same layer. This is the approach we propose, which enables each Transformer layer to have a distributed working memory that corresponds to its abstraction level.

Recurrent Neural Networks (RNNs) have achieved great success in machine learning by introducing feedback loops [ 6 , 9 ] . RNNs pass feedback between sequences through hidden states. Attention mechanisms can implement feedback loops by attending to both the input sequence and the feedback state simultaneously.

We propose a novel Transformer architecture (TransformerFAM) that enables attention to both homogeneous sequence data and latent representations via a feedback loop. This architecture change fosters the natural emergence of working memory within Transformers. During inference, TransformerFAM has a computational complexity of O ⁡ ( L ) O(L) and a memory complexity of O ⁡ ( 1 ) O(1) , where L L is the length of the processed tokens. TransformerFAM can maintain past information for an indefinite horizon, making it a promising solution for LLMs to handle infinitely long input sequences.

TransformerFAM does not introduce new weights to the Transformer, allowing the reuse of pre-trained checkpoints. Our experiments show that fine-tuning TransformerFAM with LoRA for just 50k steps significantly enhances performance on long-context tasks across 1B, 8B, and 24B Flan-PaLM LLMs [ 58 ] .

## 2 TransformerFAM

### 2.1 Block Sliding Window Attention (BSWA)

In general, when handling long context inputs, there are the two main approaches. A first approach is to increase the context length with increasing the computational resources (memory and processing power). A second approach is the implementation of Sliding Window Attention (SWA) [ 35 , 74 ] , as illustrated in Fig. 1(a) . During inference, the standard implementation allocates key and value cache twice the window length at the beginning, and then using a ring buffer to update the necessary components at each step, in order to avoid memory allocation and copying operations every step, which are computationally expensive.

Longformer [ 35 ] introduced Sliding Window Attention, which caches on a block-by-block basis. We will refer to this as Block Sliding Window Attention (BSWA). BSWA does not mask out past keys and values in the ring buffer, but attends to all the information in the ring buffer.

BSWA has two hyperparameters: block size and memory segment, as illustrated in Figure 1(b) and 1(c) . Block size determines how many tokens are in each block and is also used as the stride for sliding. Memory segment determines how many past blocks to cache. In our experiments, we set the default hyperparameters as follows: block size of 1024 1024 and memory segment of 3 3 (corresponding to a window size ranging from 3073 to 4096).

Given a sequence input I = [ i 1 , i 2 , … , i T ] I=[i_{1},i_{2},\dots,i_{T}] to a vanilla Transformer layer, Transformer transforms the input to a sequence output O = [ o 1 , o 2 , … , o T ] O=[o_{1},o_{2},\dots,o_{T}] as follows [ 12 ] :

Q , K , V \displaystyle Q,K,V = QKV ​ ( PreLN ​ ( I ) ) \displaystyle=\text{QKV}(\text{PreLN}(I)) a t \displaystyle a_{t} = SelfAttention ​ ( q t , K , V ) + i t \displaystyle=\text{SelfAttention}(q_{t},K,V)+i_{t} O \displaystyle O = FF ​ ( PreLN ​ ( A ) ) + A \displaystyle=\text{FF}(\text{PreLN}(A))+A

While PreLN [ 36 ] is used in the equation, it is not mandatory. Autoregressive Transformer changes the SelfAttention equation as follows: a t = SelfAttention ( q t , K : t , V : t ) + i t a_{t}=\text{SelfAttention}(q_{t},K_{:t},V_{:t})+i_{t} .

In a Transformer with SWA, the equation is modified to account for a window size of w w : a t = SelfAttention ( q t , K t − w : t , V t − w : t ) + i t a_{t}=\text{SelfAttention}(q_{t},K_{t-w:t},V_{t-w:t})+i_{t} .

In a Transformer with BSWA, τ \tau denotes the block index. Each block τ \tau contains a set of keys and values, determined by the block size. The equation is modified to account for a block index τ \tau and a memory segment m m in Eq. 1 . K τ − m : τ − 1 K_{\tau-m:\tau-1} is the keys in the memory segments from the m m blocks before τ \tau to the block before τ \tau , and K τ , : t K_{\tau,:t} is the keys from the beginning of τ \tau block up to t t . We will refer to Transformer with BSWA as TransformerBSWA.

K ^ t \displaystyle\hat{K}_{t} = Concat ( K τ − m : τ − 1 , K τ , : t ) \displaystyle=\text{Concat}(K_{\tau-m:\tau-1},K_{\tau,:t}) (1a) V ^ t \displaystyle\hat{V}_{t} = Concat ( V τ − m : τ − 1 , V τ , : t ) \displaystyle=\text{Concat}(V_{\tau-m:\tau-1},V_{\tau,:t}) (1b) a t \displaystyle a_{t} = SelfAttention ​ ( q t , K ^ t , V ^ t ) + i t \displaystyle=\text{SelfAttention}(q_{t},\hat{K}_{t},\hat{V}_{t})+i_{t} (1c)

Algorithm 1 presents TransformerBSWA ( Eq. 1 ), re-expressed from the perspective of a block index τ \tau . Algorithm 1 describes how to iteratively calculate a t a_{t} and then concatenate the results into an A τ A_{\tau} sequence. Typically, standard implementations employ a causal attention mask to enable parallel computation of self-attention.

TransformerXL [ 26 ] proposed to use a technique called "stop gradient" for the memory segment. However, we argue that this technique has a negative impact on ability of the model to attend to past information. Specifically, we show that using stop gradient results in a much shorter receptive field than the theoretical receptive field in Section 3.2 . We believe that allowing gradient to flow to the memory segment is necessary for the model to learn to carry important information in the memory segment.

While this modification might seem to burden training memory and computation, it does not significantly impact performance in practice. This is primarily due to the prevalence of gradient checkpointing [ 11 ] in LLM training on ML accelerators, as memory often presents the primary bottleneck. Gradient checkpointing recomputes attention during backpropagation, from later blocks to earlier blocks. Therefore, the presence or absence of stop gradients has little impact on the overall computational complexity, while still improving performance.

In addition, when training an LLM with sliding window attention on long context inputs (more than 8 8 k tokens), computing the attention over the entire input at once would require too much memory. As a result, the standard practice is to divide the attention into blocks and calculate it using a vectorized map (e.g., jax.vmap, torch.vmap). This reduces the peak memory usage to the amount required to calculate one block. Blocks are independent of each other, so they can be calculated in any order. Understanding this point is essential when evaluating the memory requirements and training efficiency of Feedback Attention Memory (FAM), as discussed in Section 2.2 .

Transformer has quadratic memory and computation complexity with respect to the length of the input sequence due to self-attention. It has O ⁡ ( L 2 ) O(L^{2}) complexity for input length L L . However, Transformer with Sliding Window Attention has linear complexity with respect to the input sequence. It has O ⁡ ( L × W ) O(L\times W) complexity for input length L L and window size W W . If the input length is about the same as the window size ( ∼ 1 \sim 1 k), the complexity difference is almost negligible, but if the input length is large like 128 128 k in GPT-4 turbo [ 70 ] , there is a huge difference. In inference, Transformer with SWA or BSWA only needs to cache a fixed ring buffer (block size + + memory segment). Therefore, it only consumes constant memory regardless of the generated token length. Therefore, LLMs using SWA or BSWA can generate infinitely long output tokens.

However, BSWA has a limited receptive field, approximately equal to model depth × \times window size as illustrated in Fig. 1(d) . As a result, the later generated tokens are not related to tokens outside the receptive field (e.g., prompt). To address this limitation, we propose a novel architecture in the following Section 2.2 . Our approach, Feedback Attention Memory (FAM), builds upon BSWA. This is because the block stride concept of BSWA is well-suited for blockwise feedback updates.

### 2.2 Feedback Attention Memory

As mentioned in Section 1 , we hypothesized that attending to the feedback loop can give rise to working memory in Assumption 1 . To implement the feedback loop, we add feedback activations that feed contextual representation back into each block of BSWA. We call these virtual activations as Feedback Attention Memory (FAM). FAM is designed to meet the following key requirements:

• Integrated Attention: Self-attention should simultaneously process input context and FAM.

• Block-Wise Updates: FAM should be updated when transitioning between blocks.

• Information Compression: FAM updates should compress current block information, conditioned on previous FAM.

• Global Contextual Storage: FAM should store comprehensive contextual information indefinitely.

The proposed architecture achieves this by appending FAM to block segments and incorporating it into self-attention processes. This enables richer representations and dynamic propagation of global contextual information across blocks, as illustrated in Fig. 2(b) . When self-attention occurs on the current block, the input query for the block attends to the input key for that block, the memory segment, and the previous FAM. The previous FAM provides global contextual information, allowing for a much richer representation than BSWA. In parallel, the FAM query attends to the current block and the FAM key. The FAM query compresses the current block, conditioned on the previous global contextual information. The FAM query is dynamically generated based on previous global contextual information, as it is copied from the previous FAM. Then, the newly updated FAM serves to propagate global contextual information to the next block recursively. This process is formally described in Algorithm 2 .

While Algorithm 2 might initially suggest a doubling of matrix operations compared to Algorithm 1 , it performs the same number of matrix operations in the actual implementation, because it starts with the concatenation of block input I τ I_{\tau} and FAM F τ − 1 F_{\tau-1} . The attention mask within self-attention requires a minor modification to accurately represent FAM. The FAM F τ − 1 F_{\tau-1} is much shorter than the input I τ I_{\tau} , and in Section 3 , we experimented with a block size of 1024 1024 and a FAM length of 64 64 .

Transformers are much better at exploiting the parallelism of ML accelerators than Recurrent Neural Networks (RNNs). This is because RNNs have a causal relationship between input sequences, while Transformers only have a causal relationship between the inputs and the layer one depth below. It is possible to worry that the feedback mechanism of TransformerFAM will eliminate the advantages of Transformers and make training inefficient. As explained in the implementation of BSWA, memory-efficient implementations perform self-attention in blocks using vectorized maps. Otherwise, peak memory increases during LLM training, requiring more ML accelerators. The causal relationship of TransformerFAM only exists between blocks. Since vectorized maps are used to perform self-attention in blocks, the causal relationship between blocks does not affect training speed and memory. In addition, processing 64 64 additional FAM when processing 1024 1024 block input sequences has only a minor impact on performance. Therefore, the memory consumption and training speed of TransformerFAM are almost the same as those of TransformerBSWA.

TransformerFAM requires additional considerations for FAM initialization and length extrapolation. These details are explained in Appendix B .

An evaluation of multiple FAM variants was conducted, and the best-performing variant is presented in the main paper. Appendix C provides further details for the remaining variants.

## 3 Experiments

### 3.1 Training

Pretraining an LLM from scratch requires a huge amount of resources. TransformerFAM can reuse existing LLM checkpoints because it does not add new weights to the Transformer layer. We reused 1B, 8B, and 24B Flan-PaLM LLMs [ 58 ] for our experiments. This is a large enough size to prove that TransformerFAM is a general solution for LLMs. The model sizes 1B, 8B, and 24B refer to the size of the plain Transformer, excluding the text embedding table. The models use a 256k sentence piece tokenizer [ 20 ] , resulting in 400M text embedding table weights for the 1B model and 1B weights for the 8B and 24B models. The detailed model architecture is described in Table 3 in Section A.1 .

Flan-PaLM is a model that is fine-tuned on top of a pretrained PaLM model [ 75 ] using instruction finetuning. The instruction data consists of few-shot instructions with 100 100 to 1 1 k tokens, which are packed into 2.5 2.5 k tokens for training. This means that individual instruction data are concatenated until they reach 2.5 2.5 k tokens.

We applied both the TransformerBSWA and TransformerFAM architectures to Flan-PaLM and fine-tuned it for an additional 50k steps. We experimented with different memory segment for both architectures. The block size is set to 1024 1024 and the FAM length is set to 64 64 .

During fine-tuning, we used the same Flan instruction data packed into 8.5 8.5 k tokens. To maintain a minibatch size of 128 for all models, we used 32 TPUv5 [ 77 ] cores for the 1B model, 64 cores for the 8B model, and 128 cores for the 24B model. If we had used more resources and a larger minibatch size, we might have achieved better results than those reported in the paper.

We performed LoRA finetuning by adding LoRA [ 46 ] to the Attention and FF layers of Transformer without training all the parameters. Full finetuning resulted in lower scores on various tasks reported by GPT-3 [ 33 ] , because catastrophic forgetting [ 14 ] occurred in domains that were not covered by the instruction data. In LoRA finetuning, the scores on GPT-3 tasks actually improved, and the performance on long context tasks was similar to that of full finetuning. The rank of LoRA was 64, and the weights of the original Attention and FF layers were merged with LoRA weights and used during inference.

The Adafactor optimizer ( β 1 = 0.9 , β 2 = 0.99 \beta_{1}=0.9,\beta_{2}=0.99 ) [ 15 ] was used with constant learning rate. The learning rates used were 10 − 4 10^{-4} for 1B, and 3 × 10 − 3 3\times 10^{-3} for both 8B and 24B.

In addition, TransformerXL exhibits comparable performance to TransformerBSWA. The implementations are almost identical, with TransformerXL employing an additional QK attention mask to mask out keys beyond a predetermined window size. Section B.4.7 demonstrates that the performance difference between TransformerXL and TransformerBSWA is insignificant, and therefore, experimental results for TransformerBSWA are only included in the main paper .

#### 3.1.1 Data

The ideal data for training TransformerFAM is a very long document with continuous context, such as textbooks and novels, and the data should be large enough to finetune an LLM. Additionally, the same very long document should be used continuously in each minibatch component, while maintaining FAM and memory segments between training steps.

The loss function of an LLM is to minimize the difference between the parametric probabilistic model P ⁡ ( x | θ ) P(x|\theta) and the data-generating true distribution p d ​ a ​ t ​ a ​ ( x ) p_{data}(x) . The Kullback–Leibler divergence (KL divergence) is used to measure this difference. To perform an unbiased estimation of KL divergence, we draw samples from the data-generating true distribution, which are assumed to be independent and identically distributed (IID). However, the ideal training scenario for the aforementioned memory training directly contradicts the IID assumption. We refer to this as the curse of IID.

Due to the curse of IID, we could not find the training infrastructure or data suitable for training memory. So we used Flan instruction data as a last resort.

We used Flan instruction data [ 84 ] as training data, packed up to 8.5k tokens. In the Flan paper [ 44 , 58 ] , a special attention mask was used to prevent attention between different segments during self-attention, by applying a separate mask to each packed segment. We did not use this special attention mask processing. Attention occurs causally within the window, regardless of the segment. We expected TransformerBSWA and TransformerFAM to learn to remember important information and forget outdated information by themselves.

Each token in Flan data has a weight. Few shots examples and instructions have a weight of 0, and answers have a weight of 1. This means that the model only learns to generate the answer. To incentivize the model to remember long contexts, we randomly selected 256 consecutive tokens from 8.5k tokens and appended them to the end of the data with the prompt ’ [repeat random segment]: ’. The repeated tokens were given a weight of 0.1 0.1 . We hope that future studies can use more suitable data for training memory, such as long continuous documents, long-form speech, video or video game.

### 3.2 PassKey Retrieval

The PassKey retrieval task is a recent benchmark used in several long-context transformer papers [ 71 , 68 , 67 ] . In this task, a passkey is presented at the beginning, followed by a very long filler context. Finally, a question about the passkey is asked, as shown in Fig. 10 in Section D.1 .

This task is a good smoke test to quickly check if information is transmitted in a long context. However, this task only checks if small and important information is transmitted, and does not check if large amounts of information can be efficiently compressed.

We fine-tuned the Flan-PaLM 1B model for 5k steps with the PassKey format, which has a filler context of 2k to 18k randomly. We used a block size of 1024, TransformerBSWA with 0 to 12 memory segments, TransformerFam with 0 memory segments, and a FAM length of 64 64 . When the number of memory segments is 3, the window size is 3k (i.e. memory segment × \times block size).

As shown in Fig. 3(a) , TransformerFAM was able to perfectly solve the task with a filler context of up to 260k tokens . In the figure, MX denotes the number of BSWA memory segments. The performance of TransformerBSWA improves significantly up to M2, after which it saturates. The performance of M12 also drops significantly after 20k tokens. The theoretical receptive field of M2 is 36k (i.e. depth(18) × \times memory segment(2k)), but the effective receptive field is much shorter.

In Fig. 3(a) , it is important to compare M1_SG and M1. M1_SG has a stop gradient applied to one memory segment, which limits the receptive field to the window size. This is because the model cannot learn which contextual information stored in the memory segment will have a good result later. SWA with back propagation through time (BPTT) functions similarly to a time-limited RNN. It is common to use stop gradients on the memory segments of TransformerXL [ 26 , 63 ] . However, we recommend against this practice.

In Section B.4.8 , we compare our work with recent Transformer with memory papers [ 57 , 63 ] .

### 3.3 Long Context Tasks

Gemini [ 69 ] evaluated long-context capabilities using the following tasks: NarrativeQA [ 19 ] , Scrolls-Qasper, Scrolls-Quality [ 60 ] , and XLSum [ 51 ] . Additionally, PG-19 [ 21 ] and Isabelle [ 56 ] are another common evaluation tasks among long-context Transformer papers [ 21 , 56 , 67 ] . Detailed information on the evaluation data is provided in Table 10 in Section D.2 .

We evaluated the long-context capabilities of the 1B TransformerBSWA model trained in Section 3.1 using memory segment sizes ranging from 0 to 8. As shown in Fig. 3(b) , TransformerFAM outperformed TransformerBSWA on all the long context tasks (LCT), regardless of the number of memory segments in BSWA. It shows a significant performance improvement on ScrollsQasper and NarrativeQA, where it has to understand 5k to 500k tokens of context before answering a question. The LCT results demonstrate that TransformerFAM can effectively compress and retain important contextual information within extremely long contexts .

Above M1, the number of memory segments does not significantly impact LCT performance on TransformerBSWA, because the input sequences are much longer than the window size of all experiments. We observed the same phenomenon in TransformerFAM, and TransformerFAM uses 3 3 memory segments in Fig. 3(b) . The figure shows the normalized scores of all tasks to view the scores on the same scale. The raw results are in Table 11 in Section D.2 .

We further evaluated TransformerFAM and TransformerBSWA on 8B and 24B models. As shown in Table 1 , TransformerFAM demonstrates scalability as the model size increases. This suggests that self-attention can route local information relevant to each input sequence while simultaneously routing contextual information to the FAM. However, the performance improvements are not substantial, indicating room for further enhancements in working memory mechanisms.

In addition, TransformerFAM marginally surpasses TransformerBSWA on GPT-3 tasks [ 33 ] (see Table 2 ). This result is unexpected since all tasks involve sequences shorter than 2k tokens. We hypothesize that this improvement arises from the efficient contextual representation by TransformerFAM. By offloading contextual data to FAM, TransformerFAM reduces redundancy within input activations, optimizing latent space usage . 1 1 1 It can be viewed as the decoder analog of register tokens [ 78 ] in ViT encoders [ 32 ] to process global context.

Thus, BSWA memory segments (local representation) and FAM (global representation) complement each other. For LLMs, we recommend using FAM for compressed contextual representation alongside BSWA memory segments up to inference budgets (e.g., 2k, 8k, 32k [ 69 ] , or 128k [ 70 ] ). Due to page limitations in the main paper, ablation studies are presented in Section B.4 .

## 4 Related Work

There have been attempts to incorporate feedback mechanisms into the Transformer, but most of them involve feeding the output activations from the top layer to the bottom [ 57 , 63 ] or to intermediate layers [ 27 ] . Since the top three layers in the Transformer are heavily focused on output reconstruction [ 45 ] , we hypothesize that there is a significant representational gap between the top and other layers. In this paper, we propose a feedback mechanism between intermediate layers.

There were papers that compressed information blockwise [ 21 , 25 , 31 , 71 , 72 ] . However, in those papers, the information was not propagated infinitely. Relevant prior work includes the use of recurrent cross-attention between blocks [ 52 ] , enabling the propagation of compressed information to subsequent blocks. Additionally, incorporating feedback from a few upper layers has been used to integrate past information [ 61 ] . We propose TransformerFAM under the assumption that the human brain processes homogenous, heterogeneous, and feedback data with the same attention mechanism across distributed brain areas. Additional related works are presented in Appendix E .

## 5 Conclusion

In the film ’Memento’ (2000), the protagonist struggles with anterograde amnesia, which means he can not remember anything before happened in the last 10 minutes, but his long-term memory is intact, He has to tattoo important information on his body to remember it. This is similar to the current state of large language models (LLMs). LLMs memorize the entire internet thanks to scaling laws [ 39 ] , which allow them to store an enormous amount of information in large weights (long-term memory). However, their short-term memory is limited by the attention window. As a result, the complex prompt engineering becomes necessary to help them recall important details. We propose a new architecture called TransformerFAM that could fix anterograde amnesia of LLMs.

The rapid progress of machine learning is astonishing, but there are two key problems that we still do not know how to approach: reasoning and memory. In this paper, we provide a clue to the memory problem. Memory is a critical prerequisite for reasoning. It is hard to imagine how we can derive complex mathematical equations without working memory. Reasoning must be a phenomenon that occurs based on the current working memory.

This paper explores the integration of attention-based working memory, a concept from neuroscience, into the field of deep learning. Our goal is to ignite further research within the community to address and solve the ongoing challenge of limited memory in deep learning. There is a significant set of problems to tackle here, ranging from refining feedback attention architecture to investigating the transfer of working memory to long-term memory.

## References

[1] Miller, George A(1956): The magical number seven, plus or minus two: Some limits on our capacity for processing information. , 2: 81.

[2] Fuster, Joaquin M(1973): Unit activity in prefrontal cortex during delayed-response performance: neuronal correlates of transient memory. , 1: 61–78.

[3] White, John G / Southgate, Eileen / Thomson, J Nichol(1986): S. Brenner (1986) The Structure of the Nervous System of the Nematode Caenorhabditis elegans 1–340.

[4] LeCun, Yann / Bengio, Yoshua / others u.a.(1995): Convolutional networks for images, speech, and time series , 10: 1995.

[5] Hochreiter, Sepp / Schmidhuber, Jürgen(1997): Long Short-Term Memory , 8: 1735–1780.

[6] Hochreiter, Sepp / Schmidhuber, Jürgen(1997): Long short-term memory , 8: 1735–1780.

[7] Ashby, F Gregory / Ell, Shawn W / Valentin, Vivian V / Casale, Michael B(2005): FROST: A distributed neurocomputational model of working memory maintenance , 11: 1728–1743.

[8] Baars, Bernard J(2005): Global workspace theory of consciousness: toward a cognitive neuroscience of human experience 45–53.

[9] Cho, Kyunghyun / Van Merriënboer, Bart / Gulcehre, Caglar / Bahdanau, Dzmitry / Bougares, Fethi / Schwenk, Holger / Bengio, Yoshua(2014): Learning phrase representations using RNN encoder-decoder for statistical machine translation .

[10] Tang, Xiaoyu / Wu, Jinglong / Shen, Yong(2016): The interactions of multisensory integration with endogenous and exogenous attention 208–224.

[11] Chen, Tianqi / Xu, Bing / Zhang, Chiyuan / Guestrin, Carlos(2016): Training deep nets with sublinear memory cost .

[12] Vaswani, Ashish / Shazeer, Noam / Parmar, Niki / Uszkoreit, Jakob / Jones, Llion / Gomez, Aidan N / Kaiser, Łukasz / Polosukhin, Illia(2017): Attention is all you need .

[13] Christophel, Thomas B / Klink, P Christiaan / Spitzer, Bernhard / Roelfsema, Pieter R / Haynes, John Dylan(2017): The distributed nature of working memory , 2: 111–124.

[14] Kirkpatrick, James u.a.(2017): Overcoming catastrophic forgetting in neural networks , 13: 3521–3526.

[15] Shazeer, Noam / Stern, Mitchell(2018): Adafactor: Adaptive learning rates with sublinear memory cost In: International Conference on Machine Learning4596–4604.

[16] Devlin, Jacob / Chang, Ming Wei / Lee, Kenton / Toutanova, Kristina(2018): Bert: Pre-training of deep bidirectional transformers for language understanding .

[17] Hasani, Ramin / Lechner, Mathias / Amini, Alexander / Rus, Daniela / Grosu, Radu(2018): Can a Compact Neuronal Circuit Policy be Re-purposed to Learn Simple Robotic Control?

[18] Rangapuram, Syama Sundar / Seeger, Matthias W / Gasthaus, Jan / Stella, Lorenzo / Wang, Yuyang / Januschowski, Tim(2018): Deep state space models for time series forecasting .

[19] Kočiskỳ, Tomáš / Schwarz, Jonathan / Blunsom, Phil / Dyer, Chris / Hermann, Karl Moritz / Melis, Gábor / Grefenstette, Edward(2018): The narrativeqa reading comprehension challenge 317–328.

[20] Kudo, Taku / Richardson, John(2018): Sentencepiece: A simple and language independent subword tokenizer and detokenizer for neural text processing .

[21] Rae, Jack W / Potapenko, Anna / Jayakumar, Siddhant M / Lillicrap, Timothy P(2019): Compressive transformers for long-range sequence modelling .

[22] Shazeer, Noam(2019): Fast transformer decoding: One write-head is all you need .

[23] Child, Rewon / Gray, Scott / Radford, Alec / Sutskever, Ilya(2019): Generating long sequences with sparse transformers .

[24] Narayanan, Arun / Prabhavalkar, Rohit / Chiu, Chung Cheng / Rybach, David / Sainath, Tara N / Strohman, Trevor(2019): Recognizing long-form speech using streaming end-to-end models In: 2019 IEEE automatic speech recognition and understanding workshop (ASRU)920–927.

[25] Guo, Qipeng / Qiu, Xipeng / Liu, Pengfei / Shao, Yunfan / Xue, Xiangyang / Zhang, Zheng(2019): Star-transformer .

[26] Dai, Zihang / Yang, Zhilin / Yang, Yiming / Carbonell, Jaime / Le, Quoc V / Salakhutdinov, Ruslan(2019): Transformer-xl: Attentive language models beyond a fixed-length context .

[27] Fan, Angela / Lavril, Thibaut / Grave, Edouard / Joulin, Armand / Sukhbaatar, Sainbayar(2020): Addressing some limitations of transformers with feedback memory .

[28] Zaheer, Manzil u.a.(2020): Big bird: Transformers for longer sequences 17283–17297.

[29] Gulati, Anmol u.a.(2020): Conformer: Convolution-augmented transformer for speech recognition .

[30] Ding, Siyu / Shang, Junyuan / Wang, Shuohuan / Sun, Yu / Tian, Hao / Wu, Hua / Wang, Haifeng(2020): ERNIE-Doc: A retrospective long-document modeling transformer .

[31] Gupta, Ankit / Berant, Jonathan(2020): Gmat: Global memory augmentation for transformers .

[32] Dosovitskiy, Alexey u.a.(2020): An image is worth 16x16 words: Transformers for image recognition at scale .

[33] Brown, Tom u.a.(2020): Language models are few-shot learners 1877–1901.

[34] Wang, Sinong / Li, Belinda Z / Khabsa, Madian / Fang, Han / Ma, Hao(2020): Linformer: Self-attention with linear complexity .

[35] Beltagy, Iz / Peters, Matthew E / Cohan, Arman(2020): Longformer: The long-document transformer .

[36] Xiong, Ruibin u.a.(2020): On layer normalization in the transformer architecture In: International Conference on Machine Learning10524–10533.

[37] Kitaev, Nikita / Kaiser, Łukasz / Levskaya, Anselm(2020): Reformer: The efficient transformer .

[38] Choromanski, Krzysztof u.a.(2020): Rethinking attention with performers .

[39] Kaplan, Jared u.a.(2020): Scaling laws for neural language models .

[40] Katharopoulos, Angelos / Vyas, Apoorv / Pappas, Nikolaos / Fleuret, François(2020): Transformers are rnns: Fast autoregressive transformers with linear attention In: International conference on machine learning5156–5165.

[41] Baevski, Alexei / Zhou, Yuhao / Mohamed, Abdelrahman / Auli, Michael(2020): wav2vec 2.0: A framework for self-supervised learning of speech representations 12449–12460.

[42] Roy, Aurko / Saffar, Mohammad / Vaswani, Ashish / Grangier, David(2021): Efficient content-based sparse attention with routing transformers 53–68.

[43] Gu, Albert / Goel, Karan / Ré, Christopher(2021): Efficiently modeling long sequences with structured state spaces .

[44] Wei, Jason u.a.(2021): Finetuned language models are zero-shot learners .

[45] Pasad, Ankita / Chou, Ju Chieh / Livescu, Karen(2021): Layer-wise analysis of a self-supervised speech representation model In: 2021 IEEE Automatic Speech Recognition and Understanding Workshop (ASRU)914–921.

[46] Hu, Edward J / Shen, Yelong / Wallis, Phillip / Allen Zhu, Zeyuan / Li, Yuanzhi / Wang, Shean / Wang, Lu / Chen, Weizhu(2021): Lora: Low-rank adaptation of large language models .

[47] Tolstikhin, Ilya O u.a.(2021): Mlp-mixer: An all-mlp architecture for vision 24261–24272.

[48] Xiong, Yunyang / Zeng, Zhanpeng / Chakraborty, Rudrasis / Tan, Mingxing / Fung, Glenn / Li, Yin / Singh, Vikas(2021): Nyströmformer: A nyström-based algorithm for approximating self-attention In: Proceedings of the AAAI Conference on Artificial Intelligence, 16: 14138–14148.

[49] Lester, Brian / Al Rfou, Rami / Constant, Noah(2021): The power of scale for parameter-efficient prompt tuning .

[50] Li, Xiang Lisa / Liang, Percy(2021): Prefix-tuning: Optimizing continuous prompts for generation .

[51] Hasan, Tahmid / Bhattacharjee, Abhik / Islam, Md Saiful / Samin, Kazi / Li, Yuan Fang / Kang, Yong Bin / Rahman, M Sohel / Shahriyar, Rifat(2021): XL-sum: Large-scale multilingual abstractive summarization for 44 languages .

[52] Hutchins, DeLesley / Schlag, Imanol / Wu, Yuhuai / Dyer, Ethan / Neyshabur, Behnam(2022): Block-recurrent transformers 33248–33261.

[53] Yu, Jiahui / Wang, Zirui / Vasudevan, Vijay / Yeung, Legg / Seyedhosseini, Mojtaba / Wu, Yonghui(2022): Coca: Contrastive captioners are image-text foundation models .

[54] Alayrac, Jean Baptiste u.a.(2022): Flamingo: a visual language model for few-shot learning 23716–23736.

[55] Ramesh, Aditya / Dhariwal, Prafulla / Nichol, Alex / Chu, Casey / Chen, Mark(2022): Hierarchical text-conditional image generation with clip latents , 2: 3.

[56] Wu, Yuhuai / Rabe, Markus N / Hutchins, DeLesley / Szegedy, Christian(2022): Memorizing transformers .

[57] Bulatov, Aydar / Kuratov, Yury / Burtsev, Mikhail(2022): Recurrent memory transformer 11079–11091.

[58] Chung, Hyung Won u.a.(2022): Scaling instruction-finetuned language models .

[59] Tay, Yi u.a.(2022): Scaling laws vs model architectures: How does inductive bias influence scaling?

[60] Shaham, Uri u.a.(2022): Scrolls: Standardized comparison over long language sequences .

[61] Ju, Da / Roller, Stephen / Sukhbaatar, Sainbayar / Weston, Jason E(2022): Staircase attention for recurrent processing of sequences 13203–13213.

[62] Villalobos, Pablo / Sevilla, Jaime / Heim, Lennart / Besiroglu, Tamay / Hobbhahn, Marius / Ho, Anson(2022): Will we run out of data? An analysis of the limits of scaling datasets in Machine Learning .

[63] Chevalier, Alexis / Wettig, Alexander / Ajith, Anirudh / Chen, Danqi(2023): Adapting Language Models to Compress Contexts .

[64] Borsos, Zalán u.a.(2023): Audiolm: a language modeling approach to audio generation .

[65] Xiong, Wenhan u.a.(2023): Effective long-context scaling of foundation models .

[66] Xiao, Guangxuan / Tian, Yuandong / Chen, Beidi / Han, Song / Lewis, Mike(2023): Efficient streaming language models with attention sinks .

[67] Chen, Shouyuan / Wong, Sherman / Chen, Liangjian / Tian, Yuandong(2023): Extending context window of large language models via positional interpolation .

[68] Tworkowski, Szymon / Staniszewski, Konrad / Pacek, Mikołaj / Wu, Yuhuai / Michalewski, Henryk / Miłoś, Piotr(2023): Focused transformer: Contrastive training for context scaling .

[69] Team, Gemini u.a.(2023): Gemini: a family of highly capable multimodal models .

[70] Achiam, Josh u.a.(2023): Gpt-4 technical report .

[71] Mohtashami, Amirkeivan / Jaggi, Martin(2023): Landmark Attention: Random-Access Infinite Context Length for Transformers .

[72] Mu, Jesse / Li, Xiang Lisa / Goodman, Noah(2023): Learning to compress prompts with gist tokens .

[73] Gu, Albert / Dao, Tri(2023): Mamba: Linear-time sequence modeling with selective state spaces .

[74] Jiang, Albert Q u.a.(2023): Mistral 7B .

[75] Chowdhery, Aakanksha u.a.(2023): Palm: Scaling language modeling with pathways , 240: 1–113.

[76] Peng, Bo u.a.(2023): RWKV: Reinventing RNNs for the Transformer Era .

[77] Jouppi, Norm u.a.(2023): Tpu v4: An optically reconfigurable supercomputer for machine learning with hardware support for embeddings In: Proceedings of the 50th Annual International Symposium on Computer Architecture1–14.

[78] Darcet, Timothée / Oquab, Maxime / Mairal, Julien / Bojanowski, Piotr(2023): Vision transformers need registers .

[79] Munkhdalai, Tsendsuren / Faruqui, Manaal / Gopal, Siddharth(2024): Leave No Context Behind: Efficient Infinite Context Transformers with Infini-attention .

[80] Su, Jianlin / Ahmed, Murtadha / Lu, Yu / Pan, Shengfeng / Bo, Wen / Liu, Yunfeng(2024): Roformer: Enhanced transformer with rotary position embedding 127063.

[81] Oren, Matanel / Hassid, Michael / Adi, Yossi / Schwartz, Roy(2024): Transformers are Multi-State RNNs .

[82] LMSYS (2023): LMSYS Chatbot Arena Leaderboard https://chat.lmsys.org/?arena .

[83] Wallace, Anthony FC (1960): Plans and the Structure of Behavior .

[84] Wei, Jason u.a. (2021): The FLAN Instruction Tuning Repository https://github.com/google-research/FLAN .

## Appendix A Architecture details

### A.1 Flan-PaLM architecture

Table 3 provides detailed information on the architecture of Flan-PaLM for 1B, 8B, and 24B models. MQA (Multi-Query Attention) [ 22 ] is an attention mechanism that employs a single set of keys and values for all attention heads.

### A.2 FAM hyperparameters

Table 4 presents the default settings for the hyperparameters added in TransformerFAM.

## Appendix B Additional details of TransformerFAM

The appendix describes additional details not covered in the main text.

### B.1 FAM initialization

The current FAM F τ F_{\tau} is the output activation of the previous FAM update. So, how do we initialize the FAM for the first block?

When FAM are used as queries, they summarize the block context. Therefore, we learn by adding learnable summarization embeddings to the token embedding lookup level of the Transformer model. This is the same as prepending learnable embeddings in soft prompt tuning [ 49 ] . The difference is that full attention is applied between the FAM prompt activations, and the updated FAM is used for the next block. The FAM prompt is passed to the next transformer layer through the forward propagation of the Transformer model, and it has a summary representation that is suitable for the level of the layer.

Prefix tuning [ 50 ] can also be used to train learnable initial FAM at each Transformer layer. However, we had difficulty matching the magnitude of the learnable prefix to the regular input sequence, and the results of prompt tuning were consistently better. Ablation study in Section B.4.6 shows prompt tuning outperforms. In addition, prefix tuning has the disadvantage of adding additional weights of FAM length to each layer.

In addition, the first FAM update in self-attention should utilize a zero tensor in the residual connection rather than the initial FAM, because the initial FAM does not carry any contextual information.

In summary, we learned the initial FAM using prompt tuning, which only adds a very small number of weights of FAM length to the entire model. We share the same initial FAM across all minibatches.

### B.2 Input Length Extrapolation

#### B.2.1 FAM Position Encoding

We used rotary position embedding (RoPE) [ 80 ] in all of our experiments. Each input sequence is assigned an integer position m m , which is converted into sinusoidal encoding in the form of exp ⁡ ( i ​ m ​ θ ) \exp(im\theta) where θ = 10000 − 2 i / d m ​ o ​ d ​ e ​ l \theta=10000^{-2i/d_{model}} [ 12 ] .

FAM is inserted at each block boundary, but the problem is how to assign positions to FAM. We assigned positions to FAM in order from the last number of the compressed block. For example, if the block size is 4, the FAM length is 2, and the positions of the compressed blocks are m m , m + 1 m+1 , m + 2 m+2 , and m + 3 m+3 , then the updated FAM positions are m + 2 m+2 and m + 3 m+3 .

We tried other methods, but this method worked best according to the ablation results in Section B.4.3 .

#### B.2.2 Random Position Offset

The input length extrapolation problem of Transformer is well known [ 67 , 65 ] . For example, a Transformer LLM trained with 2k tokens experiences a severe performance drop when generating 8k tokens. This is because machine learning (ML) does not generalize well to situations that it has not seen during training.

Transformer with SWA does not suffer from the position extrapolation problem when using relative positional embedding like RoPE. This is because the score value of q m ⋅ k n q_{m}\cdot k_{n} becomes a function of ( m − n ) (m-n) in the form of exp ⁡ ( i ⁡ ( m − n ) ​ θ ) \exp(i(m-n)\theta) .

Because the range of ( m − n ) (m-n) is limited to the window size, independent of the input length, the model can handle long input sequences without facing novel scenarios during inference. The model can accurately determine the relative position, if the window size is smaller than the maximum wavelength of θ \theta . If the typical θ \theta is used for positional embedding, the working maximum window size is the maximum wavelength ( = 2 × 10000 × π ∼ 63 =2\times 10000\times\pi\sim 63 k tokens ).

However, FAM breaks the symmetry of relative position. Since the absolute position from the past to the present is recursively embedded in the FAM, the large absolute position value that the model encounters for the first time during inference creates a situation where the model needs to extrapolate.

We propose Random Position Offset as a solution. At each training step, the Transformer model randomly samples a scalar value between 0 and the maximum wavelength. All Transformer layers add that random value to the absolute position at that training step. Therefore, the FAM experiences the entire range of absolute position embedding during training.

This is a purely training technique. During inference, the default offset is 0 0 . We used the below algorithm that generates 0 0 by 50 % 50\% when sampling the offset, as 0 0 is the default value.

⬇

#### B.2.3 Random State Passing

Due to the recursive use of FAM, we need to determine the maximum number of updates for which the FAM remains valid. If it is updated up to 8 times during training, the model will have to extrapolate the situation where it is updated 100 times during inference.

The same problem existed in RNNs, and Random State Passing (RSP) [ 24 ] was proposed to handle long-form speech in the speech domain. We also used RSP to generalize the number of updates of FAM.

RSP saves FAM as weights at the end of each training step. Then, it loads the saved FAM at the next training step. When initializing FAM, it either uses randomly saved FAM or learned FAM. In our default setup, it used saved FAM with 80 % 80\% probability. To save FAM of all minibatch, weights are required as many as the number of minibatch. We save FAM of only the first batch and all minibatch share it in the next training step.

On the other hand, saved FAM can be thought of as learnable prefix for prefix tuning [ 50 ] . It is also possible to train only the FAM while the model is frozen and use them for various downstream tasks or personalization. This part is left as a future research topic.

### B.3 FAM illustrated

In Section 2.2 , we define the feedback loop as feedback activations that feed contextual representation back into each block of BSWA. This feedback loop is formally described in Algorithm 2 . While Fig. 2(b) illustrates Algorithm 2 , the static image makes it challenging to fully grasp the dynamic nature of the decoding self-attention mechanism. To clarify this, we create a multi-frame animation in Fig. 4 that demonstrates how the attention mechanism evolves over time (top to bottom).

### B.4 Ablation Studies

All ablation studies were conducted on a 1B model.

#### B.4.1 FAM length

In the Flan 1B model, we observed performance saturation on ScrollsQasper, ScrollsQuality, and XLSum tasks when the FAM length reached 64. Interestingly, performance declined when FAM length exceeded 64, suggesting that information compression is more effective with limited space. This constraint on memory capacity is reminiscent of Miller’s Law [ 1 ] , which posits that the average person can only hold approximately 7 ​ ( ± 2 ) 7(\pm 2) items in their working memory at any given time.

#### B.4.2 The number of previous FAM blocks

In Fig. 2(b) , the input query attends to the FAM as denoted Attention to Feedback. The input query can attend to not only the immediately previous FAM, but also to more previous FAMs. Table 6 shows the XLSum scores for different numbers of previous FAM blocks. As the table shows, increasing the number of blocks did not have a significant effect, because the previous FAM already encapsulates all the previous information by a feedback copy. Therefore, the default setup attends to only the immediately previous FAM.

#### B.4.3 FAM Position Encoding

Section B.2.1 proposed assigning the last number of the compressed block as the FAM position. In addition, we also experimented with FAM having a float position between blocks. In the example of block size 4 in Section B.2.1 , the FAM positions would be m + 3 + 0.33 m+3+0.33 and m + 3 + 0.66 m+3+0.66 . We also experimented with the case where the FAM position is always 0.

As shown in Table 7 , the last number showed the best accuracy.

Fig. 5 shows FAM (i.e. Last number in Table 7 ) outperforming FAM-POS (i.e. Zero) in PG-19 accuracy over most base frequencies.

#### B.4.4 Random Position Offset

As mentioned in Section B.2.2 , the input length extrapolation problem of the Transformer is well-known. The "Attention is All You Need" [ 12 ] introduced sinusoidal position encoding in the form of exp ⁡ ( i ⁡ ( m − n ) ​ θ ) \exp(i(m-n)\theta) where θ = 10000 − 2 i / d m ​ o ​ d ​ e ​ l \theta=10000^{-2i/d_{model}} . Popular solutions for full attention models include increasing the base frequency from 10k to 500k [ 67 ] or scaling down ( m − n ) (m-n) to ( m − n ) × ( 1024 / 4096 ) (m-n)\times(1024/4096) [ 65 ] .

Since the relative position of BSWA has a range of 0 to window size, it does not suffer from the input length extrapolation problem. However, TransformerFAM encodes absolute position into FAM, which requires a solution. Section B.2.2 proposes Random Position Offset (RPO) as a solution.

In Fig. 5 , FAM shows better PG-19 accuracy than FAM-RPO at the 10k base frequency. As mentioned in Section D.2 , the max length of PG-19 was truncated to 256k in the experiments.

Furthermore, scaling up the base frequency or scaling down ( m − n ) (m-n) is only a remedy for pain, not a final solution. It reduces the resolution of the position, which negatively affects the overall Transformer performance, as shown in the figure. Interestingly, the originally proposed 10k is a very good value even in long contexts, until the window size reaches its wavelength (63k).

In addition, we did not observe the attention sink phenomenon [ 66 ] in our TransformerBSWA experiments. The paper proposes that Transformers with sliding window attention should store initial tokens in a KV cache for long-context inference. However, the relative position of SWA is restricted to a range of 0 to window size, independent of input sequence length. Our TransformerBSWA implementation, trained on 8.5k tokens, successfully operated for inference up to 256k tokens without any issues.

#### B.4.5 Random State Passing

To extrapolate the number of FAM updates, Section B.2.3 proposes Random State Passing (RSP). In Fig. 5 , FAM shows significantly better PG-19 accuracy than FAM-RSP. This demonstrates that RSP plays a crucial role in training FAM.

Fig. 6 shows the best performance at a probability of 0.8. At 0.8, the half-life is 3 training steps ( 0.512 = 0.8 3 0.512=0.8^{3} ). This means that every 26k (8.5k x 3) tokens, FAM restarts from the beginning with a 50 % \% probability. In other words, if FAM experiences 25 FAM updates during training, it can extrapolate to 256 FAM updates (256k tokens) during inference.

#### B.4.6 Prompt vs. Prefix

Section B.1 mentions that Prompt tuning outperforms Prefix tuning for training FAM in terms of performance, memory, and number of parameters. Fig. 5 shows that Prefix tuning for FAM training leads to performance degradation in PG-19 (FAM vs. FAM+Prefix).

#### B.4.7 TransformerXL vs. TransformerBSWA

TransformerXL is a modification of TransformerBSWA that incorporates an additional QK attention mask to mask out keys beyond a specified window size. Therefore, there is no reason to expect a significant difference in performance between the two. Table 8 shows the scores for the main tasks. TransformerBSWA used a single memory segment, and TransformerXL window size was equal to the block size of 1024 1024 .

#### B.4.8 Comparison with other methods

We compared FAM with Recurrent Memory Transformer (RMT) [ 57 ] , because RMT also implements memory in Transformer using feedback mechanism from top layer to bottom layer. As shown in Fig. 7 , RMT showed worse performance than Block Sliding Window Attention (BSWA) with 1 memory segment, in the PassKey retrieval task. FAM solved the PassKey retrieval task, but RMT did not work at all with very long filler token lengths.

RMT is implemented by feeding the output memory of the previous segment as the input memory to the next segment. In the constraint that the input is text embedding and the output is text reconstruction in LLM, RMT has an additional constraint that the latent space of the output memory and the input memory must match. In this situation, RMT fails to remember the PassKey for a very long context. On the other hand, FAM seems to compress, store, and propagate information more effectively by learning memory representation that matches the abstraction level of each layer through training.

AutoCompressors [ 63 ] is an extension of RMT that continuously accumulates blockwise memory of RMT. AutoCompressors theoretically should be able to solve the PassKey task since it maintains all the memory tokens for all blocks. However, as shown in Fig. 7 , its performance drops sharply after 18k tokens. This is because the model only saw up to 18k tokens during training. It fails to generalize to longer filler token lengths. The AutoCompressors in Fig. 7 accumulates 260 memories to support up to 260k tokens.

## Appendix C Don’t

There could be various ways to create feedback loops in Transformers. This appendix summarizes our attempts that did not work well. We hope that this will save other researchers time when improving the architecture of feedback loops in future studies.

### C.1 Beyond Block-Recurrent Transformers

Block-Recurrent Transformers (BRT) [ 52 ] have a recurrent state that connects each block, and the recurrent state and the block input sequence exchange information through cross-attention. In this architecture, the recurrent state plays a role similar to FAM. We started the project by removing the additional QKV projection and cross-attention for the recurrent state in BRT and integrating all computations into self-attention.

Like BRT, we tried to compress the block input by attention to use it as the recurrent state of the next block, and it required additional projections like BRT. It was difficult to properly train the additional projections that were only used when striding blocks, and as a result, the performance of general tasks such as GPT-3 tasks was degraded. Finally, we found that the activations compressed by attention must go through the FF layer of the Transformer to be aligned as a latent representation that can be used again as the input of the next Transformer. The input of the Transformer and the output of self-attention are very different representations. However, the FF layer transforms it back into a representation similar to the input of the Transformer for the next Transformer layer. After the discovery of reusing the FF layer, we also found that separate QKV projection and additional projections are not required for FAM. That is how the TransformerFAM architecture was created.

Around the time this paper was published, Infini-Transformer [ 79 ] was also released. Infini-Transformer reported successful PassKey retrieval despite the compressed information not passing through the FF layer. This is because it stores weighted values in scratchpad memory and reuses them, preserving the latent space of the values. However, since the weighted values are all it can represent, there might be limitations in its expressiveness.

Furthermore, TransformerFAM maintains the past memory segment from BSWA despite having compressed memory because the compressed memory cannot retain detailed information. Since Infini-Transformer completely discards the past memory segment, it might have difficulty remembering recent details.

### C.2 Feedback Memory Segment

As shown in Fig. 2(b) , TransformerFAM utilizes the updated FAM from the previous block as the input to the current block. Therefore, it is natural to consider using the Transformer outputs of the previous block directly as the input to the current block, instead of using a complex FAM mechanism. Fig. 8 illustrates this modification, which we refer to as the Feedback Memory Segment (FM). FM achieves an infinite theoretical receptive field by performing self-attention at the output level. This is similar to ERNIE-Doc [ 30 ] , and a specific variant of Staircase Attention [ 61 ] . Staircase Attention proposes using activations from progressively higher Transformer layers as the memory segment goes further into the past.

However, as shown in Fig. 9 , FM fails to retain PassKey information over a long context. The figure compares M1, 2, and 4 with FM1, 2, and 4 when the memory segment size is 1, 2, and 4 for BSWA and Feedback Memory Segment. TransformerFM outperforms TransformerBSWA, but still falls short of TransformerFAM by a significant margin. In TransformerFM, each activation must possess both local and global representation, similar to TransformerBSWA. However, the absence of an activation specifically responsible for the global representation appears to prevent the retention of critical information like PassKey over an extended context.

Furthermore, TransformerFM exhibited lower performance than TransformerBSWA on GPT-3 tasks ( Table 9 ). As TransformerFM introduced additional complexity without any discernible performance advantages, we discontinued this architecture. Table 9 presents the results after 25k steps of fine-tuning.

### C.3 Static Summary Tokens

As illustrated in Fig. 2(b) , "FAM copy" duplicates the previously updated FAM to the current FAM input. However, "FAM copy" is not an essential component in the feedback loop. When FAM compresses the current block, it can also attend to the previous FAM as both key and value, as shown in the experiment in Section B.4.2 . Therefore, "FAM copy" is not strictly necessary because past FAM information is propagated through self-attention.

As mentioned in Section B.1 , we learn the initial FAM using prompt tuning, and this token can be considered a "Summary" token. An alternative design could employ a persistent summary token for block compression, with the feedback loop enabled by attending to the key-value pairs of previous FAMs.

As illustrated in Fig. 9 , SUM FAM (static summary token) prevents the model from successfully solving the PassKey task. This suggests that the query for summarization needs to be dynamically generated conditioned on the past FAM. A static query may not be able to cover all situations effectively. Additionally, simply attending to the key and value alone does not transmit sufficient information from the past. On the other hand, the "FAM copy" mechanism propagates information from the past FAM to the current FAM through the residual connection of the Transformer, which facilitates better performance on the PassKey task.

### C.4 Diversity Loss

In Section B.4.1 , we observed a performance drop when the FAM length exceeded 64. We hypothesized that FAM was underutilizing its capacity and experiencing mode collapse, where lengthy FAM either focused on a small number of inputs or prevented all inputs from obtaining sufficient information.

As a remedy, we employed diversity loss as an auxiliary loss, similar to Wav2vec 2.0 [ 41 ] . Diversity loss aims to maximize the entropy of QK attention probability, as shown in Eq. 2b . This loss encourages FAM to uniformly attend to all inputs, and all inputs equally attend to FAM. In Eq. 2 , b b denotes the batch size, τ \tau represents the block index, l l indicates the sequence position within a block, and h h refers to multi heads. In Eq. 2a , p ¯ b ​ τ \bar{p}_{b\tau} represents the average attention probability across all sequences and multi-heads for the self-attention of each block. The auxiliary loss functions to regularize this probability towards uniformity.

p ¯ b ​ τ \displaystyle\bar{p}_{b\tau} = 1 H ​ L ​ ∑ h = 1 H ∑ l = 1 L p b ​ τ ​ h ​ l \displaystyle=\frac{1}{HL}\sum_{h=1}^{H}\sum_{l=1}^{L}p_{b\tau hl} (2a) ℒ d \displaystyle\mathcal{L}_{d} = 1 B ​ T ∑ b = 1 B ∑ τ = 1 T − H ( p ¯ b ​ τ ) = 1 B ​ T ∑ b = 1 B ∑ τ = 1 T p ¯ b ​ τ log p ¯ b ​ τ \displaystyle=\frac{1}{B\mathrm{T}}\sum_{b=1}^{B}\sum_{\tau=1}^{\mathrm{T}}-H(\bar{p}_{b\tau})=\frac{1}{B\mathrm{T}}\sum_{b=1}^{B}\sum_{\tau=1}^{\mathrm{T}}\bar{p}_{b\tau}\log{\bar{p}_{b\tau}} (2b)

We trained the model with diversity loss with various weights, but the overall performance was always worse, regardless of the FAM length. It did not help at all even when the FAM length was 256 or longer.

### C.5 Reconstruction Loss

Compressive transformers [ 21 ] compress memory segments before forwarding them to the next block. The key difference between our approach is that the compressed information is not recurrently connected. The paper proposes a reconstruction loss as an auxiliary loss, which aims to reconstruct the original activations from the compressed activations.

We also experimented with the reconstruction loss. In details, we generated transformer outputs autoregressively from the updated FAM and the query sequence of the original block, and compared them to the original outputs using the MSE loss. However, this did not help to improve the performance.

## Appendix D Experiments details

This section provides additional details about the experiments that were not covered in Section 3 .

### D.1 PassKey Retrieval

The format of the PassKey retrieval task is shown in Fig. 10 . The original paper [ 71 ] also included a prefix filler, but we removed it in our paper.

There is an important info hidden inside a lot of irrelevant text. Find it and memorize them. I will quiz you about the important information there. The pass key is <PASS KEY> . Remember it. <PASS KEY> is the pass key. <filler> What is the pass key? The pass key is <PASS KEY>

### D.2 Long Context Tasks

Table 10 provides detailed information about the long context tasks we used. Due to the limitations of TPU memory, PG-19, Isabelle, and NarrativeQA were truncated to 256k tokens, which is within two standard deviations.

Table 11 presents the LCT results for TransformerBSWA and TransformerFAM. MX represents the number of memory segments for TransformerBSWA.

### D.3 GPT-3 Tasks

We evaluated all model sizes on the tasks reported by GPT-3 [ 33 ] . The results are shown in Table 12 .

### D.4 Complexity

BSWA and FAM have memory and computational complexity of O ⁡ ( L × C ) O(L\times C) , where C C is the chunk size. Table 13 and Table 14 show memory and inference time through inference jobs on TPUv4. The most tokens in the experiment are pre-filled and generation is limited to 256 tokens.

## Appendix E Related Work

The Transformer architecture exhibits a quadratic complexity with respect to context length, a significant limitation. To address this, several research works have focused on approximating the attention mechanism. One approach involves sparse attention, where only a subset of important tokens are attended to, as seen in models like Sparse Transformer [ 23 ] , Big Bird [ 28 ] , Reformer [ 37 ] , Routing Transformer [ 42 ] , and TOVA [ 81 ] . Linear approximation methods offer an alternative, seeking to circumvent the quadratic complexity by altering attention calculations, as exemplified by Linformer [ 34 ] , Linear Transformer [ 40 ] , Performer [ 38 ] , and Nyströmformer [ 48 ] . Finally, some research explores entirely different sequence-to-sequence architectures as replacements for attention-based Transformers, including MLP-mixer [ 47 ] , State Space Models [ 18 ] , S4 [ 43 ] , Mamba [ 73 ] , and RWKV [ 76 ] .

Global Workspace Theory (GWT) [ 8 ] is a leading theory of consciousness. According to GWT, the human brain possesses a global workspace where various modules, such as sensory input, memories, and internal representations, converge. The attention mechanism in brain acts as a spotlight, focusing on specific inputs among the multitude, and transforming this unconscious activity into conscious awareness. These "momentarily active, subjectively experienced" events are then stored in working memory. TransformerFAM draws inspiration from GWT, adopting its principle of a unified attention mechanism for processing homogenous, heterogeneous, and feedback data.

## Appendix F Attention Visualization

Fig. 11 depicts the attention map for each head in each layer of a 1B model. FAM is prepended and is located at the bottom left corner. The bright spots along the left edge represent the block inputs attending to FAM, while the bright spots along the bottom edge represent FAM compressing the corresponding block. Overall, the block inputs actively reference FAM, while FAM compresses only the selective inputs.

## Appendix G Limitations

While the results presented in Table 1 demonstrate that TransformerFAM shows improvements on long-context tasks, these gains are not yet substantial, highlighting the need for further development and refinement of working memory mechanisms.

In this paper, we have taken an initial step towards integrating attention-based working memory, a concept inspired by neuroscience, into deep learning architectures. We believe there is significant potential for further exploration in this direction, and we encourage future research to continue addressing the ongoing challenge of limited memory in deep learning models.

## Appendix H Broader Impacts

While our work is inspired by the concept of working memory from neuroscience, as discussed in Section Section 3.3 , achieving a human-level implementation remains a significant challenge. This research represents an initial step in that direction.

The potential societal impacts of such advanced working memory in LLMs could be substantial, with applications like highly personalized AI assistants. However, these impacts are currently speculative due to the nascent stage of this research.

In the immediate future, the primary benefit of our work is expected to be improvements in the efficiency and effectiveness of LLMs, with potential applications across various domains such as education, healthcare, and communication. As with any technology, we recognize the possibility of misuse and encourage ongoing research into the ethical implications of LLMs and related advancements in artificial intelligence.

## Instructions for reporting errors

We are continuing to improve HTML versions of papers, and your feedback helps enhance accessibility and mobile support. To report errors in the HTML that will help us improve conversion and rendering, choose any of the methods listed below:

Click the "Report Issue" ( ) button, located in the page header.

Tip: You can select the relevant text first, to include it in your report.

Our team has already identified the following issues . We appreciate your time reviewing and reporting rendering errors we may not have found yet. Your efforts will help us improve the HTML versions for all readers, because disability should not be a barrier to accessing research. Thank you for your continued support in championing open access for all.

Have a free development cycle? Help support accessibility at arXiv! Our collaborators at LaTeXML maintain a list of packages that need conversion , and welcome developer contributions .
