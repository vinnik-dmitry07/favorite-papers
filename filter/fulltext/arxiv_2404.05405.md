##### Report GitHub Issue

Content selection saved. Describe the issue below:

# Physics of Language Models: Part 3.3, Knowledge Capacity Scaling Laws Thanks: Submitted for Meta internal review on March 14, 2024. We would like to thank Lin Xiao and Yuchen Zhang for many helpful conversations. We would like to extend special thanks to Ian Clark, Gourab De, Anmol Mann, and Max Pfeifer from W&B , as well as Lucca Bertoncini, Liao Hu, Caleb Ho, Apostolos Kokolis, and Shubho Sengupta from Meta FAIR NextSys; Henry Estela, Wil Johnson, Rizwan Hashmi, and Lucas Noah from Meta Cloud Foundation; without their invaluable support, the extensive experiments in this paper would not have been possible.

###### Abstract

Scaling laws describe the relationship between the size of language models and their capabilities. Unlike prior studies that evaluate a model’s capability via loss or benchmarks, we estimate the number of knowledge bits a model stores. We focus on factual knowledge represented as tuples, such as (USA, capital, Washington D.C.) from a Wikipedia page. Through multiple controlled datasets, we establish that language models can and only can store 2 bits of knowledge per parameter, even when quantized to int8 , and such knowledge can be flexibly extracted for downstream applications. Consequently, a 7B model can store 14B bits of knowledge, surpassing the English Wikipedia and textbooks combined based on our estimation.

More broadly, we present 12 results on how (1) training duration, (2) model architecture, (3) quantization, (4) sparsity constraints such as MoE, and (5) data signal-to-noise ratio affect a model’s knowledge storage capacity. Notable insights include:

• The GPT-2 architecture, with rotary embedding, matches or even surpasses LLaMA/Mistral architectures in knowledge storage , particularly over shorter training durations. This arises because LLaMA/Mistral uses GatedMLP, which is less stable and harder to train.

• Prepending training data with domain names (e.g., wikipedia.org) significantly increases a model’s knowledge capacity. Language models can autonomously identify and prioritize domains rich in knowledge, optimizing their storage capacity.

## 1 Introduction

The scaling laws of large language models remain a pivotal area of research, enabling predictions about the performance of extremely large models through experiments with smaller ones. On the training time aspect, established scaling laws [ 16 , 21 , 14 , 1 , 13 ] discuss the optimal training flops versus model size. However, recent studies [ 25 , 12 , 24 ] challenge these laws, demonstrating that training smaller models with significantly more flops can yield superior results. While these laws talk about how much time/data is needed to train a model of a certain size, another fundamental question is: what is the ultimate performance a model can achieve, assuming sufficient training ? Despite the known emergent behaviors in large models [ 8 , 34 ] , there is a lack of a principled, quantitative analysis on how model size impacts its capacity when adequately trained. 1 1 1 There is a rich literature comparing how pretrained models perform on benchmark tasks. Most comparisons are for different model families trained over different data: if LLaMA-70B is better than Mistral-7B, does the gain come from its choice of pretrain data, or the architecture difference, or really the size of the model? Some comparisons are among the same architecture, such as LLaMA-70B scores 63.6% on the world knowledge benchmark while LLaMA-7B scores only 48.9% [ 33 ] ; does this mean increasing model size by 10x increases its capacity only to 130 % = 63.6 / 48.9 130\%=63.6/48.9 ? Thus, it is highly important to use a more principled framework to study scaling laws in a controlled setting.

Traditional theory on overparameterization suggests that scaling up model size in sufficiently trained models can enhance memorization of training data [ 6 ] , improve generalization error [ 15 , 27 , 28 ] , and better fit complex target functions [ 23 , 5 ] . However, these results often overlook large constant or polynomial factors, leading to a significant discrepancy from practical outcomes.

In this paper, we introduce a principled framework to examine highly accurate scaling laws concerning model size versus its knowledge storage capacity . It is intuitive that larger language models can store more knowledge, but does the total knowledge scale linearly with the model’s size? What is the exact constant of this scaling? Understanding this constant is crucial for assessing the efficiency of transformer models in knowledge storage and how various factors (e.g., architecture, quantization, training duration, etc.) influence this capacity.

Knowledge is a, if not the, pivotal component of human intelligence, accumulated over our extensive history. Large language models like GPT-4 are celebrated not just for their sophisticated logic but also for their superior knowledge base. Despite rumors of GPT-4 having over 1T parameters, is it necessary to store all human knowledge? Could a 10B model, if trained sufficiently with high-quality data, match GPT-4’s knowledge capacity? Our paper seeks to address these questions.

Knowledge Pieces. Defining “one piece of human knowledge” precisely is challenging. This paper aims to make progress by focusing on a restricted, yet sufficiently interesting domain. We define a piece of knowledge as a (name, attribute, value) tuple, e.g., (Anya Forger, birthday, 10/2/1996); and many data in world knowledge benchmarks can be broken down into pieces like this. 2 2 2 Examples include (Africa, largest country, Sudan) and (It Happened One Night, director, Frank Capra) in TriviaQA [ 20 ] , or (Teton Dam, collapse date, 06/05/1976) and (USA, Capital, Washington D.C.) in NaturalQuestions [ 22 ] .

We generate synthetic knowledge-only datasets by uniformly at random generating (name, attribute, value) tuples from a knowledge base and converting them into English descriptions. We pretrain language models (e.g., GPT-2, LLaMA, Mistral) on these texts using a standard auto-regressive objective from random initialization, and “estimate” the learned knowledge. By varying the number of knowledge pieces and model sizes, we outline a knowledge capacity scaling law.

Our idealized setting, free from irrelevant data, allows for more accurate scaling law computations — we also discuss how “junk” data affects capacity later in Section 10 . In contrast, it is difficult to quantify real-life knowledge; for instance, if LLaMA-70B outperforms LLaMA-7B by 30% on a benchmark, it doesn’t necessarily mean a tenfold model scaling only boosts capacity by 30% (see Footnote 1 ). The synthetic setting also lets us adjust various hyperparameters, like name/value lengths and vocabulary size, to study their effects on knowledge capacity scaling laws.

Most of the paper shall focus on a setting with synthetically-generated human biographies as data, either using predefined sentence templates or LLaMA2-generated biographies for realism.

Bit Complexity and Capacity Ratio. For N N knowledge pieces (i.e., N N tuples), we define the bit complexity as the minimum bits required to encode these tuples. For any language model trained on this data, we calculate its “bit complexity lower bound” (see Theorem 3.2 ), describing the minimum number of bits needed for the model to store the knowledge at its given accuracy. This formula is nearly as precise as the upper bound, within a 1 − o ⁡ ( 1 ) 1-o(1) factor.

We train language models of varying sizes on knowledge data with different N N values. By comparing the models’ trainable parameters to the bit complexity lower bounds, we evaluate their knowledge storage efficiency.

###### Example .

A model with 100M parameters storing 220M bits of knowledge has a capacity ratio of 2.2 = 220M 100M 2.2=\frac{\text{220M}}{\text{100M}} bits per parameter. There is also a trivial upper bound on a model’s capacity ratio; for instance, a model using int8 parameters cannot exceed a capacity ratio of 8.

Our results. Our findings are summarized as follows:

• Section 5 : Base scaling law for GPT2 . 3 3 3 In this paper, GPT2 refers to the original GPT2 model but with rotary embedding instead of positional embedding and without dropout.

– Result 1 + 2 + 3 : GPT2, trained with standard AdamW, consistently achieves a 2bit/param capacity ratio across all data settings after sufficient training. This includes various model sizes, depths, widths, data sizes, types (synthetic/semi-synthetic), and hyperparameters (e.g., name/value length, attribute number, value diversity).

###### Remark 1.1 .

This predicts a sufficiently trained 7B language model can store 14B bits of knowledge, surpassing the knowledge of English Wikipedia and textbooks by our estimation. 4 4 4 As of February 1, 2024, English Wikipedia contains a total of 4.5 billion words, see https://en.wikipedia.org/wiki/Wikipedia:Size_of_Wikipedia#Size_of_the_English_Wikipedia_database , accessed March 2024. We estimate that the non-overlapping contents of English textbooks have fewer than 16 billion words in total, see Remark G.1 . This amounts to 20.5 billion words, and we believe they contain fewer than 14 billion bits of knowledge.

###### Remark 1.2 .

When we say the model stores knowledge , it isn’t word-by-word memorization. Instead, the knowledge is flexibly extractable (e.g., via QAs like “What is Anya Forger’s birthday”) [ 3 ] and applicable in downstream tasks (e.g., comparing birthdays) via fine-tune [ 4 ] .

• Section 6 : How training time affects model capacity . Achieving a 2bit/param capacity requires each knowledge piece to be visited 1000 times during training, termed 1000-exposure to differentiate from traditional ‘‘1000-pass’’ terminology, as a single data pass can expose a knowledge piece 1000 times. 5 5 5 For example, it is plausible that one pass through Wiki data might present the knowledge piece (US, capital, Washington D.C.) 1000 times, and one pass through the Common Crawl might present it a million times. – Result 4 : With 100 exposures, an undertrained GPT2’s capacity ratio falls to 1bit/param.

###### Remark 1.3 .

Another perspective on Result 4 is that rare knowledge, encountered only 100 times during training, is stored at a 1bit/param ratio.

• Section 7 : How model architecture affects model capacity . We tested LLaMA, Mistral, and GPT2 architectures with reduced or even no MLP layers. – Result 5 : In the 1000-exposure setting, a 2bit/param capacity ratio appears to be a universal rule : all models, even without MLP layers, closely achieve this ratio.

– Result 6 : With 100 exposures, some archs show limitations; notably, LLaMA/Mistral’s capacity ratio is 1.3x lower than GPT2’s, even after best-tuned learning rates.

– Result 7 : Further controlled experiments indicate that “gated MLP” usage leads to LLaMA/Mistral architecture’s underperformance in knowledge storage.

###### Remark 1.4 .

Our framework offers a principled playground to compare models. This contrasts with traditional comparisons based on loss/perplexity, which can produce debatable conclusions. 6 6 6 A model might achieve better perplexity by performing much better on simpler data but slightly poorer on complex data, or by excelling in reasoning tasks but not in knowledge storage. Our results offer a more nuanced view: GatedMLP doesn’t affect frequently encountered knowledge (with 1000 exposures) but does impact moderately rare knowledge (with 100 exposures). Controlled data also reveal more significant differences between models. 7 7 7 For example, Shazeer [29] found GatedMLP offers a ∼ 1 % \sim 1\% accuracy boost on benchmark tasks; our findings of a 1.3x difference translates for instance to accuracies 90 % 90\% vs. 70 % 70\% .

• Section 8 : How quantization affects model capacity . We applied GPTQ [ 10 ] to quantize models from the base scaling laws to int8 or int4. Surprisingly, – Result 8 : Quantizing to int8 does not compromise model capacity (even for models on the boundary of 2bit/param); however, quantizing to int4 reduces capacity to 0.7bit/param.

###### Remark 1.5 .

Since int8 is 8bit, LLMs can exceed 1/4 of the theoretical limit for storing knowledge; thus knowledge must be very compactly stored inside the model across all layers.

###### Remark 1.6 .

Since 2bit/param is obtained after sufficient training, training longer may not further improve model capacity, but quantization can . While not covered in this paper, our framework also provides a principled playground to compare different quantization methods.

• Section 9 : How sparsity (MoE) affects model capacity . Mixture-of-experts (MoE) models offer faster inference than dense models but often underperform dense models with the same total parameter count (not effective parameters). We show that this performance drop is likely not due to a lack of knowledge storage capability. – Result 9 : MoE models, even with 32 32 experts, only reduce 1.3x in capacity compared to the base scaling laws, despite using just 8.8 % 8.8\% of the total parameters during inference.

• Section 10 : How junk knowledge affects model capacity . Not all pretrain data are equally useful. Much of the internet data lacks valuable knowledge for training language models [ 24 ] , while knowledge-rich sources like Wikipedia represent only a small fraction of the training tokens. We explore the impact on model capacity by conducting a controlled experiment with both useful and “junk” data. – Result 10 + 11 : Junk data significantly reduces model capacity. As an example, with a 1:7 ratio of “useful to junk” training tokens, capacity for useful knowledge loses by a factor of 20 x, even when useful knowledge is exposed 100 times. 8 8 8 The loss factor improves to 3x/1.5x/1.3x with 300/600/1000 exposures of useful knowledge, compared to Result 4 which involves training without junk for only 100 exposures.

– Result 12 : An effective mitigation is to prepend a special token to all useful knowledge. This is akin to adding a domain name like wikipedia.org at the start of every Wikipedia paragraph; the model autonomously identifies high-quality data without prior knowledge of valuable domains. In the example above, the loss factor improves from 20x to 2x.

Overall, our approach to studying knowledge capacity scaling laws offers a flexible and more accurate playground compared to traditional methods that evaluate language models trained on internet data against real-world benchmarks. This accuracy is partly due to the synthetic nature of our dataset, which eliminates concerns about benchmark contamination that could compromise the validity of real-world benchmark results. In this paper, we’ve conducted a thorough comparison across different model architectures and types of knowledge. While we haven’t explored various quantization methods, this represents a promising direction for future research. We’ve also investigated the impact of junk data and proposed mitigation strategies. We believe the insights gained from this principled exploration can assist practitioners in making informed decisions about model selection, training data preparation, and further theoretical research into LLMs.

## 2 Preliminaries

In this paper, a piece of knowledge is a tuple of three strings: (name, attribute, value) = ( n , a , v ) =(n,a,v) . For instance, n = “Anya” , a = “birthday” , v = “Oct 2, 1996” n=\text{``Anya''},a=\text{``birthday''},v=\text{``Oct 2, 1996''} .

### 2.1 Knowledge (Theoretical Setting)

The complexity of a knowledge set is determined not only by the number of knowledge pieces but also by the length of the value string v v , the diversity of the vocabulary, and other factors. For instance, if the attribute a = a= “passport number,” then the value v v contains more bits of knowledge compared with a = a= “gender,” because the former has significantly higher diversity . If the attribute a = a= “birth date,” then the value v v could consist of 3 chunks : ( 10 , 2 , 1996 ) (10,2,1996) .

Considering these examples, we propose a set of hyperparameters that may influence the complexity of knowledge: 1. N N — the number of (distinct) names n n , denoted by 𝒩 \mathcal{N} .

2. K K — the number of attributes a a , with 𝒜 \mathcal{A} representing the set of attributes. For simplicity, we assume | 𝒜 | = K |\mathcal{A}|=K is fixed.

3. T T — the number of tokens T T , where every character in v v belongs to 𝒯 \mathcal{T} for some | 𝒯 | = T |\mathcal{T}|=T . For example, we can think of T T as “vocab size” in a tokenizer.

4. C C and L L — the number of chunks and the length of each chunk for the value: each value v ∈ ( 𝒯 L ) C v\in(\mathcal{T}^{L})^{C} can be expressed as v = ( v 1 , v 2 , ⋯ , v C ) v=(v_{1},v_{2},\cdots,v_{C}) , where v i ∈ 𝒯 L v_{i}\in\mathcal{T}^{L} .

5. D D — the diversity of chunks: for each piece of knowledge ( n , a , v ) (n,a,v) and i ∈ [ C ] i\in[C] , the chunk v i v_{i} belongs to 𝒟 a ⊂ 𝒯 L \mathcal{D}_{a}\subset\mathcal{T}^{L} , for some set with cardinality D = def | 𝒟 a | ≪ T L D\stackrel{{\scriptstyle\mathrm{\scriptscriptstyle def}}}{{=}}|\mathcal{D}_{a}|\ll T^{L} .

###### Remark 2.1 .

For notation simplicity, we have assumed that all chunks within an attribute a ∈ 𝒜 a\in\mathcal{A} share the same diversity set 𝒟 a \mathcal{D}_{a} , and all chunks are of equal length, etc. This enables us to more easily demonstrate the influence of each hyperparameter on a model’s capacity. In practice, different attributes may have different diversity sets or value lengths — e.g., 𝒟 passport \mathcal{D}_{\textrm{passport}} could be much larger than 𝒟 gender \mathcal{D}_{\textrm{gender}} . Our theoretical results do apply to these settings, albeit with more complex notation.

In our theoretical result, we introduce a dataset bioD ​ ( N , K , C , D , L , T ) \textsf{bioD}(N,K,C,D,L,T) defined as follows:

###### Definition 2.2 ( bioD data generation) .

Consider a fixed set of K K attributes, such as a set 𝒜 = { “ID 1” ​ … ​ “ID K ” } \mathcal{A}=\big\{\textrm{``ID 1''}\dots\textrm{``ID $K$''}\} , and a fixed set 𝒩 0 \mathcal{N}_{0} of candidate names (with N 0 = def | 𝒩 0 | ≫ N N_{0}\stackrel{{\scriptstyle\mathrm{\scriptscriptstyle def}}}{{=}}|\mathcal{N}_{0}|\gg N ). 1. Generate N N names uniformly at random (without replacement) from 𝒩 0 \mathcal{N}_{0} to form 𝒩 \mathcal{N}

2. For each attribute a ∈ 𝒜 a\in\mathcal{A} , generate D D distinct strings w 1 , a , ⋯ , w D , a ∈ 𝒯 L w_{1,a},\cdots,w_{D,a}\in\mathcal{T}^{L} uniformly at random (without replacement) to form the diversity set 𝒟 a \mathcal{D}_{a} .

3. For each name n ∈ 𝒩 n\in\mathcal{N} and attribute a ∈ 𝒜 a\in\mathcal{A} , generate value v ⋆ ​ ( n , a ) = ( v 1 , v 2 , ⋯ , v C ) v^{\star}(n,a)=(v_{1},v_{2},\cdots,v_{C}) by sampling each v i ∈ 𝒟 a v_{i}\in\mathcal{D}_{a} uniformly at random.

Let 𝒵 = def { ( n , a , v ⋆ ( n , a ) } n ∈ 𝒩 , a ∈ 𝒜 \mathcal{Z}\stackrel{{\scriptstyle\mathrm{\scriptscriptstyle def}}}{{=}}\big\{(n,a,v^{\star}(n,a)\big\}_{n\in\mathcal{N},a\in\mathcal{A}} be the knowledge set.

###### Proposition 2.3 (trivial, bit complexity upper bound) .

Given 𝒩 0 \mathcal{N}_{0} and 𝒜 \mathcal{A} and 𝒯 \mathcal{T} , to describe a knowledge set generated in Definition 2.2 , one needs at most the following number of bits: log 2 ⁡ ( | 𝒩 0 | N ) + N ​ K ​ C ​ log 2 ​ D + K ​ log 2 ​ ( T L D ) ≈ N ​ log 2 ​ | 𝒩 0 | N + N ​ K ​ C ​ log 2 ​ D + K ​ D ​ log 2 ​ T L D . \displaystyle\log_{2}\binom{|\mathcal{N}_{0}|}{N}+NKC\log_{2}D+K\log_{2}\binom{T^{L}}{D}\approx N\log_{2}\frac{|\mathcal{N}_{0}|}{N}+NKC\log_{2}D+KD\log_{2}\frac{T^{L}}{D}\kern 5.0pt.

(The approximation is valid when | 𝒩 0 | ≫ N |\mathcal{N}_{0}|\gg N and T L ≫ D T^{L}\gg D .) We will present a bit complexity lower bound in Section 3 .

### 2.2 Knowledge (Empirical Setting)

We utilize both the synthetic bioD dataset, generated as per Definition 2.2 , and several human biography datasets to evaluate language model scaling laws.

Allen-Zhu and Li [3] introduced a synthetic biography dataset comprising N N individuals, each characterized by six attributes: birth date, birth city, university, major, employer, and working city. 9 9 9 All attributes, except for the working city (determined by the employer’s headquarters), are chosen uniformly and independently at random. There are N 0 = 400 × 400 × 1000 N_{0}=400\times 400\times 1000 possible person names, 12 × 28 × 200 12\times 28\times 200 birth dates, 200 200 birth cities, 300 300 universities, 100 100 majors, and 263 263 employers. Additionally, a random pronoun with 2 possibilities is chosen for each person. To translate these tuples into natural language, in their bioS dataset, each individual is described by six randomly selected English sentence templates corresponding to their attributes. We direct readers to their paper for more details but provide an example below: Anya Briar Forger was born on October 2, 1996 . She spent her early years in Princeton, NJ . She received mentorship and guidance from faculty members at Massachusetts Institute of Technology . She completed her education with a focus on Communications . She had a professional role at Meta Platforms . She was employed in Menlo Park, CA . (2.1)

In this paper, we explore three variations of such datasets: • bioS ​ ( N ) \textsf{bioS}(N) represents an online dataset for N N individuals, where each biography is generated with new randomness for the selection and ordering of six sentence templates on-the-fly .

• bioS simple ​ ( N ) \textsf{bioS}^{\textsf{simple}}(N) denotes a similar dataset, but here, each biography is generated once with a fixed random selection and ordering of the sentence templates.

• bioR ​ ( N ) \textsf{bioR}(N) refers to the same dataset, but with each biography written 40 times by LLaMA2 [ 33 ] to increase realism and diversity.

These datasets correspond to the bioS multi+permute , bioS single+permute , and bioR multi data types discussed in [ 3 ] , albeit with minor differences. While their study focused on N = 100 ​ K N=100K , we expand our scope for bioS to consider N N up to 20 ​ M 20M ; for bioR , we limit N N to 1 ​ M 1M , which already yields a dataset size of 22GB.

As introduced in Section 1 , if each knowledge piece is seen 1000 times during training, we call this 1000 exposures. For bioS ​ ( N ) \textsf{bioS}(N) , 1000 exposures will unlikely include identical biography data because there are 50 sentence templates for each attribute and a total of 50 6 × 6 ! 50^{6}\times 6! possible biographies per person. For bioS simple ​ ( N ) \textsf{bioS}^{\textsf{simple}}(N) , 1000 exposures mean 1000 passes of the data. For bioR ​ ( N ) \textsf{bioR}(N) , 1000/100 exposures mean only 25/2.5 passes of the training data.

For the bioD dataset, we define 𝒩 0 \mathcal{N}_{0} to be identical to bioS , with | 𝒩 0 | = 400 × 400 × 1000 |\mathcal{N}_{0}|=400\times 400\times 1000 . We encapsulate a person’s attributes within a single paragraph, employing random sentence orderings and a consistent sentence template. For example: Anya Briar Forger’s ID 7 is v 7 , 1 , … , v 7 , C v_{7,1},\dots,v_{7,C} . Her ID 2 is v 2 , 1 , … , v 2 , C v_{2,1},\dots,v_{2,C} . […] Her ID 5 is v 5 , 1 , … , v 5 , C v_{5,1},\dots,v_{5,C} . In this paper, we primarily utilize bioS . To illustrate broader applicability and to better connect to theoretical bounds , we also present results for bioS simple \textsf{bioS}^{\textsf{simple}} , bioR , and bioD .

### 2.3 Models and Training

GPT2 was introduced in [ 26 ] . Due to its limitations from the absolute positional embedding [ 2 ] , we adopt its modern variant, rotary positional embedding [ 31 , 7 ] , which we still refer to as GPT2 for convenience. Additionally, we disable dropout, which has been shown to improve performance in language models [ 33 ] . We explore a wide range of model sizes while using a fixed dimension-per-head of 64. The notation GPT2- ℓ \ell - h h represents ℓ \ell layers, h h heads, and 64 ​ h 64h dimensions; for example, GPT2-small corresponds to GPT2-12-12. The default GPT2Tokenizer is used, converting people’s names and most attributes into tokens of variable lengths. In examining the impact of model architectures on scaling laws in Section 7 , we will also use LLaMA/Mistral architectures [ 32 , 19 ] .

Training. We train language models from scratch (i.e., random initialization) using the specified datasets. Knowledge paragraphs about individuals are randomly concatenated, separated by <EOS> tokens, and then randomly segmented into 512-token windows. The standard autoregressive loss is employed for training. Unless specified otherwise, training utilizes the default AdamW optimizer and mixed-precision fp16. Learning rates and weight decays are moderately tuned (see appendix).

## 3 Bit Complexity Lower Bound

When assessing the knowledge stored in a model, we cannot simply rely on the average, word-by-word cross-entropy loss. For example, the phrase “received mentorship and guidance from faculty members” in ( 2.1 ) does not constitute useful knowledge. We should instead focus on the sum of the loss for exactly the knowledge tokens.

Consider a model F F with weight parameters W ∈ 𝒲 W\in\mathcal{W} . Assume F F is trained on a bioD ​ ( N , K , C , D , L , T ) \textsf{bioD}(N,K,C,D,L,T) dataset 𝒵 \mathcal{Z} as defined in Definition 2.2 using any optimizer; this process is represented as W = W ⁡ ( 𝒵 ) W=W(\mathcal{Z}) (the model’s weight is trained as a function of the training dataset 𝒵 \mathcal{Z} ). During the evaluation phase, we express F F through two functions: F ⊤ ​ ( W , R ) F^{\top}(W,R) , which generates names, and F ⊥ ​ ( W , n , a , R ) F^{\bot}(W,n,a,R) , which generates values given ( n , a ) (n,a) , where R R denotes the randomness used in generation. Let F 1 ⊥ ​ ( W ⁡ ( 𝒵 ) , n , a , R ) F_{1}^{\bot}(W(\mathcal{Z}),n,a,R) represent the first chunk of F ⊥ ​ ( W ⁡ ( 𝒵 ) , n , a , R ) F^{\bot}(W(\mathcal{Z}),n,a,R) . We evaluate F F by calculating the following three cross-entropy losses: 10 10 10 We use 𝔼 n \operatornamewithlimits{\mathbb{E}}_{n} or 𝔼 n , a \operatornamewithlimits{\mathbb{E}}_{n,a} to denote uniform random selection of n ∈ 𝒩 , a ∈ 𝒜 n\in\mathcal{N},a\in\mathcal{A} . 𝐥𝐨𝐬𝐬 n ​ a ​ m ​ e ​ ( 𝒵 ) \displaystyle\mathbf{loss}_{name}(\mathcal{Z}) = def 𝔼 n ∈ 𝒩 − log 𝐏𝐫 R [ F ⊤ ( W ( 𝒵 ) , R ) = n ] \displaystyle\stackrel{{\scriptstyle\mathrm{\scriptscriptstyle def}}}{{=}}\operatornamewithlimits{\mathbb{E}}_{n\in\mathcal{N}}-\log\operatornamewithlimits{\mathbf{Pr}}_{R}\big[F^{\top}(W(\mathcal{Z}),R)=n\big] 𝐥𝐨𝐬𝐬 v ​ a ​ l ​ u ​ e ​ 1 ​ ( 𝒵 ) \displaystyle\mathbf{loss}_{value1}(\mathcal{Z}) = def 𝔼 n ∈ 𝒩 , a ∈ 𝒜 − log 𝐏𝐫 R [ F 1 ⊤ ( W ( 𝒵 ) , n , a , R ) = v 1 ⋆ ( n , a ) ] \displaystyle\stackrel{{\scriptstyle\mathrm{\scriptscriptstyle def}}}{{=}}\operatornamewithlimits{\mathbb{E}}_{n\in\mathcal{N},a\in\mathcal{A}}-\log\operatornamewithlimits{\mathbf{Pr}}_{R}\big[F_{1}^{\top}(W(\mathcal{Z}),n,a,R)=v^{\star}_{1}(n,a)\big] 𝐥𝐨𝐬𝐬 v ​ a ​ l ​ u ​ e ​ ( 𝒵 ) \displaystyle\mathbf{loss}_{value}(\mathcal{Z}) = def 𝔼 n ∈ 𝒩 , a ∈ 𝒜 − log 𝐏𝐫 R [ F ⊥ ( W ( 𝒵 ) , n , a , R ) = v ⋆ ( n , a ) ] \displaystyle\stackrel{{\scriptstyle\mathrm{\scriptscriptstyle def}}}{{=}}\operatornamewithlimits{\mathbb{E}}_{n\in\mathcal{N},a\in\mathcal{A}}-\log\operatornamewithlimits{\mathbf{Pr}}_{R}\big[F^{\bot}(W(\mathcal{Z}),n,a,R)=v^{\star}(n,a)\big]

###### Remark 3.1 .

For a language model, such quantities can be computed from its auto-regressive cross-entropy loss. For instance, when evaluating the model on the sentence “Anya Briar Forger’s ID 7 is v 7 , 1 , … , v 7 , C v_{7,1},\dots,v_{7,C} ,” summing up (not averaging!) the loss over the tokens in “Anya Briar Forger” yields exactly − log 𝐏𝐫 R [ F ⊤ ( W ( 𝒵 ) , R ) = n ] -\log\operatornamewithlimits{\mathbf{Pr}}_{R}\big[F^{\top}(W(\mathcal{Z}),R)=n\big] for n = “Anya Briar Forger” n=\text{``Anya Briar Forger''} ; summing up the loss over the token v 7 , 1 v_{7,1} results in − log 𝐏𝐫 R [ F 1 ⊤ ( W ( 𝒵 ) , n , a , R ) = v 7 , 1 ] -\log\operatornamewithlimits{\mathbf{Pr}}_{R}\big[F_{1}^{\top}(W(\mathcal{Z}),n,a,R)=v_{7,1}\big] for this n n and a = “ID 7” a=\text{``ID 7''} ; and summing up the loss over the entire sequence v 7 , 1 , … , v 7 , C v_{7,1},\dots,v_{7,C} gives − log ⁡ 𝐏𝐫 R [ F ⊤ ​ ( W ⁡ ( 𝒵 ) , n , a , R ) = v 7 , 1 , … , v 7 , C ] -\log\operatornamewithlimits{\mathbf{Pr}}_{R}\big[F^{\top}(W(\mathcal{Z}),n,a,R)=v_{7,1},\dots,v_{7,C}\big] . This holds regardless of the tokenizer or value length.

###### Theorem 3.2 (bit complexity lower bound) .

Suppose N ≥ Ω ⁡ ( D ​ log ⁡ N ) N\geq\Omega(D\log N) . We have log 2 ⁡ | 𝒲 | \displaystyle\log_{2}|\mathcal{W}| ≥ 𝔼 𝒵 [ N ​ log 2 ​ N 0 − N e 𝐥𝐨𝐬𝐬 n ​ a ​ m ​ e ​ ( 𝒵 ) + N ​ K ​ log 2 ​ D C e 𝐥𝐨𝐬𝐬 v ​ a ​ l ​ u ​ e ​ ( 𝒵 ) + K ​ D ​ log 2 ​ T L − D D ​ e ( 1 + o ⁡ ( 1 ) ) ​ 𝐥𝐨𝐬𝐬 v ​ a ​ l ​ u ​ e ​ 1 ​ ( 𝒵 ) − o ⁡ ( K ​ D ) ] \displaystyle\geq\operatornamewithlimits{\mathbb{E}}_{\mathcal{Z}}\Big[N\log_{2}\frac{N_{0}-N}{e^{\mathbf{loss}_{name}(\mathcal{Z})}}+NK\log_{2}\frac{D^{C}}{e^{\mathbf{loss}_{value}(\mathcal{Z})}}+KD\log_{2}\frac{T^{L}-D}{De^{(1+o(1))\mathbf{loss}_{value1}(\mathcal{Z})}}-o(KD)\Big] = N ​ log 2 ​ N 0 − N e 𝔼 𝒵 𝐥𝐨𝐬𝐬 n ​ a ​ m ​ e ​ ( 𝒵 ) + N ​ K ​ log 2 ​ D C e 𝔼 𝒵 𝐥𝐨𝐬𝐬 v ​ a ​ l ​ u ​ e ​ ( 𝒵 ) + K ​ D ​ log 2 ​ T L − D D ​ e ( 1 + o ⁡ ( 1 ) ) ​ 𝔼 𝒵 𝐥𝐨𝐬𝐬 v ​ a ​ l ​ u ​ e ​ 1 ​ ( 𝒵 ) − o ⁡ ( K ​ D ) \displaystyle=N\log_{2}\frac{N_{0}-N}{e^{\operatornamewithlimits{\mathbb{E}}_{\mathcal{Z}}\mathbf{loss}_{name}(\mathcal{Z})}}+NK\log_{2}\frac{D^{C}}{e^{\operatornamewithlimits{\mathbb{E}}_{\mathcal{Z}}\mathbf{loss}_{value}(\mathcal{Z})}}+KD\log_{2}\frac{T^{L}-D}{De^{(1+o(1))\operatornamewithlimits{\mathbb{E}}_{\mathcal{Z}}\mathbf{loss}_{value1}(\mathcal{Z})}}-o(KD)

The goal of the paper is to study how the number of model parameters competes with this bound.

###### Corollary 3.3 (no-error case) .

In the ideal case, if for every data 𝒵 \mathcal{Z} , F F can generate a name from 𝒩 \mathcal{N} with exact 1 / N 1/N probability each, then 𝐥𝐨𝐬𝐬 n ​ a ​ m ​ e ​ ( 𝒵 ) = log ⁡ N \mathbf{loss}_{name}(\mathcal{Z})=\log N ; and if F F can 100% accurately generate values given ( n , a ) (n,a) pairs, then 𝐥𝐨𝐬𝐬 v ​ a ​ l ​ u ​ e ​ ( 𝒵 ) = 𝐥𝐨𝐬𝐬 v ​ a ​ l ​ u ​ e ​ 1 ​ ( 𝒵 ) = 0 \mathbf{loss}_{value}(\mathcal{Z})=\mathbf{loss}_{value1}(\mathcal{Z})=0 . In such a case, log 2 | 𝒲 | ≥ N ​ log 2 ​ N 0 − N N + N ​ K ​ C ​ log 2 ​ D + K ​ D ​ log 2 ​ T L − D D − o ⁡ ( K ​ D ) \log_{2}|\mathcal{W}|\geq N\log_{2}\frac{N_{0}-N}{N}+NKC\log_{2}D+KD\log_{2}\frac{T^{L}-D}{D}-o(KD) asymptotically matching the upper bound Proposition 2.3 .

###### Remark 3.4 (why “sum of 3”) .

It is essential to obtain a lower bound that is the sum of the three components; neglecting any may result in a suboptimal bound (see examples in Appendix A.4 ).

###### Remark 3.5 (why “random data”) .

Studying a lower bound for a fixed dataset 𝒵 \mathcal{Z} is impossible — a model could hard-code 𝒵 \mathcal{Z} into its architecture even without any trainable parameter. Therefore, it is necessary to consider a lower bound with respect to a distribution over datasets.

Proof difficulties. If names are fixed ( 𝒩 = 𝒩 0 \mathcal{N}=\mathcal{N}_{0} ) and there are N N pieces of knowledge, each uniformly chosen from a fixed set [ T ] [T] , it is straightforward that any model F ⁡ ( W ) F(W) , capable of learning such knowledge perfectly , must satisfy log 2 ⁡ | 𝒲 | ≥ N ​ log 2 ​ T \log_{2}|\mathcal{W}|\geq N\log_{2}T . To relate this to Theorem 3.2 , we encounter three main challenges. First, the model F F may only learn the knowledge with a certain degree of accuracy, as defined by the cross-entropy loss. Second, 𝒩 ≠ 𝒩 0 \mathcal{N}\neq\mathcal{N}_{0} so names need to be learned — even a perfect model cannot achieve zero cross-entropy loss when generating names. Third, there is a dependency between knowledge pieces — the value depends on the name and the choice of the diversity set (i.e., 𝒟 a \mathcal{D}_{a} ). The proof of Theorem 3.2 is deferred to Appendix F .

## 4 Capacity Ratio

Motivated by Theorem 3.2 , ignoring lower order terms, we define the empirical capacity ratio as

###### Definition 4.1 .

Given a model F F with P P parameters trained over a bioD ​ ( N , K , C , D , L , T ) \textsf{bioD}(N,K,C,D,L,T) dataset 𝒵 \mathcal{Z} , suppose it gives p 1 = 𝐥𝐨𝐬𝐬 n ​ a ​ m ​ e ​ ( 𝒵 ) p_{1}=\mathbf{loss}_{name}(\mathcal{Z}) , p 2 = 𝐥𝐨𝐬𝐬 v ​ a ​ l ​ u ​ e ​ ( 𝒵 ) p_{2}=\mathbf{loss}_{value}(\mathcal{Z}) , p 3 = 𝐥𝐨𝐬𝐬 v ​ a ​ l ​ u ​ e ​ 1 ​ ( 𝒵 ) p_{3}=\mathbf{loss}_{value1}(\mathcal{Z}) , we define its capacity ratio and max capacity ratio R ⁡ ( F ) \displaystyle R(F) = def N ​ log 2 ​ N 0 e p 1 + N ​ K ​ log 2 ​ D C e p 2 + K ​ D ​ log 2 ​ T L D ​ e p 3 P . \displaystyle\stackrel{{\scriptstyle\mathrm{\scriptscriptstyle def}}}{{=}}\frac{N\log_{2}\frac{N_{0}}{e^{p_{1}}}+NK\log_{2}\frac{D^{C}}{e^{p_{2}}}+KD\log_{2}\frac{T^{L}}{De^{p_{3}}}}{P}\kern 5.0pt. R 𝗆𝖺𝗑 ​ ( F ) \displaystyle R^{\mathsf{max}}(F) = def N ​ log 2 ​ N 0 N + N ​ K ​ C ​ log 2 ​ D + K ​ D ​ log 2 ​ T L D P . \displaystyle\stackrel{{\scriptstyle\mathrm{\scriptscriptstyle def}}}{{=}}\frac{N\log_{2}\frac{N_{0}}{N}+NKC\log_{2}D+KD\log_{2}\frac{T^{L}}{D}}{P}\kern 5.0pt.

###### Remark 4.2 .

One must have R ⁡ ( F ) ≤ R 𝗆𝖺𝗑 ​ ( F ) R(F)\leq R^{\mathsf{max}}(F) , and equality is obtained if the model is perfect . For a fixed dataset, further increases in model size do not yield additional knowledge, thus R 𝗆𝖺𝗑 ​ ( F ) R^{\mathsf{max}}(F) approaches zero as the model size P P increases. On the other hand, Theorem 3.2 implies, ignoring lower-order terms, that if the model parameters are 8-bit (such as int8), then R ⁡ ( F ) ≤ 8 R(F)\leq 8 .

For our bioS ​ ( N ) \textsf{bioS}(N) data, we define a slightly reduced capacity ratio by omitting the diversity term. 11 11 11 A version of Theorem 3.2 can be proven for this dataset with a simpler proof, as it excludes the diversity set. This could also mean the model has full prior knowledge of the diversity set (e.g., assuming a fixed set of 300 university names) without counting this knowledge towards its learned bits.

###### Definition 4.3 .

Given a model F F with P P parameters trained over the bioS ​ ( N ) \textsf{bioS}(N) dataset 𝒵 \mathcal{Z} , suppose it gives p 1 = 𝐥𝐨𝐬𝐬 n ​ a ​ m ​ e ​ ( 𝒵 ) p_{1}=\mathbf{loss}_{name}(\mathcal{Z}) and p 2 = 𝐥𝐨𝐬𝐬 v ​ a ​ l ​ u ​ e ​ ( 𝒵 ) p_{2}=\mathbf{loss}_{value}(\mathcal{Z}) , its capacity ratio 12 12 12 Here, one can let 𝒦 = { birth date , birth city , university , major , employer , gender } \mathcal{K}=\{\text{birth date },\text{birth city },\text{university },\text{major },\text{employer },\text{gender }\} and accordingly define 𝐥𝐨𝐬𝐬 v ​ a ​ l ​ u ​ e ( 𝒵 ) = def 𝔼 n ∈ 𝒩 ∑ a ∈ 𝒦 − log 𝐏𝐫 R [ F ⊥ ( W ( 𝒵 ) , n , a , R ) = v ⋆ ( n , a ) ] \mathbf{loss}_{value}(\mathcal{Z})\stackrel{{\scriptstyle\mathrm{\scriptscriptstyle def}}}{{=}}\operatornamewithlimits{\mathbb{E}}_{n\in\mathcal{N}}\sum_{a\in\mathcal{K}}-\log\operatornamewithlimits{\mathbf{Pr}}_{R}\big[F^{\bot}(W(\mathcal{Z}),n,a,R)=v^{\star}(n,a)\big] . R ⁡ ( F ) = def N ​ log 2 ​ N 0 e p 1 + N ​ log 2 ​ S 0 e p 2 P and R 𝗆𝖺𝗑 ​ ( F ) = def N ​ log 2 ​ N 0 N + N ​ log 2 ​ S 0 P R(F)\stackrel{{\scriptstyle\mathrm{\scriptscriptstyle def}}}{{=}}\frac{N\log_{2}\frac{N_{0}}{e^{p_{1}}}+N\log_{2}\frac{S_{0}}{e^{p_{2}}}}{P}\hskip 10.00002pt\text{and }\hskip 10.00002ptR^{\mathsf{max}}(F)\stackrel{{\scriptstyle\mathrm{\scriptscriptstyle def}}}{{=}}\frac{N\log_{2}\frac{N_{0}}{N}+N\log_{2}S_{0}}{P} for N 0 = 400 × 400 × 1000 N_{0}=400\times 400\times 1000 and S 0 = 2 × ( 12 ⋅ 28 ⋅ 200 ) × 200 × 300 × 100 × 263 S_{0}=2\times(12\cdot 28\cdot 200)\times 200\times 300\times 100\times 263 (c.f. Footnote 9 ).

###### Remark 4.4 .

Ignoring names, each person contains log 2 ⁡ ( S 0 ) ≈ 47.6 \log_{2}(S_{0})\approx 47.6 bits of knowledge.

## 5 Base Scaling Laws

We first train a series of GPT2 models on the bioS ​ ( N ) \textsf{bioS}(N) datasets (see Section 2.2 ) using mixed-precision fp16. The training protocol ensures that each piece of knowledge is presented 1000 times, a process we refer to as “1000 exposures.” It’s important to clarify that this differs from making 1000 passes over the data. For example, a single pass through Wiki data might expose the knowledge (US, capital, Washington D.C.) 1000 times, whereas a pass through the Common Crawl might do so a million times. Our synthetic bioS ​ ( N ) \textsf{bioS}(N) data, trained for 1000 exposures, aims to replicate such scenarios. 14 14 14 Within 1000 exposures, it’s likely that the same individual will have 1000 different biography paragraphs detailing the same knowledge (see Section 2.2 ). Therefore, 1000 exposures can occur within a single pass. Our initial findings are as follows: 15 15 15 We here focus on GPT2 models with depth ≥ 2 \geq 2 , and 1-layer models show slightly lower capacity ratios (see Figure 9 ). Our model selection covers most natural combinations of transformer width/depth, details in Appendix A . Result 1 ( Figure 1(a) ) . When trained for 1000 exposures on bioS ​ ( N ) \textsf{bioS}(N) , with N N ranging from 10K to 10M, GPT2 models with sizes from 1M to 0.5B parameters ( irrespective of depth or width ) demonstrate the following: (a) the peak capacity ratio R ⁡ ( F ) R(F) consistently exceeds R ⁡ ( F ) ≥ 2 R(F)\geq 2 ; (b) models with R 𝗆𝖺𝗑 ​ ( F ) ≤ 1.8 R^{\mathsf{max}}(F)\leq 1.8 attain near-perfect knowledge accuracies, i.e., R 𝗆𝖺𝗑 ​ ( F ) ≈ R ⁡ ( F ) R^{\mathsf{max}}(F)\approx R(F) ; (c) across all models, R ⁡ ( F ) ≤ 2.3 R(F)\leq 2.3 .

###### Remark 5.1 .

Result res:base(a) , res:base(b) , and res:base(c) elucidate three distinct facets of the scaling law. • Result res:base(a) highlights the maximum capacity across models; however, this could be misleading if only a single model achieves this peak.

• Result res:base(b) reinforces this by showing that all models with a maximum capacity R 𝗆𝖺𝗑 ​ ( F ) ≤ 1.8 R^{\mathsf{max}}(F)\leq 1.8 can achieve such maximum capacity, i.e., R ⁡ ( F ) ≈ R 𝗆𝖺𝗑 ​ ( F ) R(F)\approx R^{\mathsf{max}}(F) . In words, this indicates that for a dataset containing B B bits of knowledge, selecting a model size P ≥ B / 1.8 P\geq B/1.8 is sufficient .

• Result res:base(c) further strengthens this by indicating that no model exceeds capacity ratio 2.3 2.3 .

For clarity , in subsequent results of this paper, we focus solely on the peak capacity ratio, with the understanding that observations similar to Result res:base(b) and Result res:base(c) consistently apply .

Knowledge extraction. The “2bit/param” result is not about word-by-word memorization. Even better, such knowledge is also flexibly extractable (e.g., via fine-tuning using QAs like “What is Anya Forger’s birthday?”) [ 3 ] and thus can be further manipulated in downstream tasks (such as comparing the birthdates of two people, or performing calculations on the retrieved knowledge, etc.) [ 4 ] . This is because our bioS ​ ( N ) \textsf{bioS}(N) data is knowledge-augmented: the English biographies have sufficient text diversities [ 3 ] . We also verify in Appendix A.2 that such knowledge is extractable.

### 5.1 Data Formats — Diversity and Rewriting

We conduct the same analysis on bioS simple \textsf{bioS}^{\textsf{simple}} and bioR . Recall from Section 2.2 , bioS simple \textsf{bioS}^{\textsf{simple}} is a variant of bioS with reduced text diversity (one biography per person), while bioR is generated by LLaMA2, resulting in close-to-real human biographies. We have: Result 2 ( Figure 11 in Appendix A.3 ) . In the same 1000-exposure setting, peak capacity ratios for GPT2 trained on bioS simple \textsf{bioS}^{\textsf{simple}} and bioR are also approximately 2, albeit slightly lower. Thus: • Diverse data (rewriting the same data multiple times) does not hurt — and may sometimes improve — the model’s capacity! Let’s highlight the significance of Result 2 . Recall from Section 2.2 : • Training on bioS simple \textsf{bioS}^{\textsf{simple}} data for 1000 exposures equals 1000 passes over the data.

• Training on bioS data for 1000 exposures is less than 1 pass.

• Training on bioR data for 1000 exposures equals 25 passes.

Therefore, comparing bioS and bioS simple \textsf{bioS}^{\textsf{simple}} , it’s more advantageous to rewrite the data 1000 times (in this ideal setting), training each for one pass (as done in the bioS data), rather than training the same data for 1000 passes (as done in the bioS simple \textsf{bioS}^{\textsf{simple}} data). This is because, without data diversity, the model wastes capacity memorizing sentence structures, resulting in a capacity loss.

In a realistic scenario, tools like LLaMA2 can rewrite pretrain data like we did in bioR . Rewriting data 40 times can produce 40 distinct English paragraphs, sometimes with (different) hallucinated contents. Does this require the model to be 40x larger? No, our comparison between bioS and bioR shows that, if trained for the same duration (40 rewrites each for 25 passes), the model’s capacity ratio remains nearly the same, slightly lower due to irrelevant data introduced by LLaMA2.

Allen-Zhu and Li [3] suggested that rewriting pretraining data is crucial for making knowledge extractable rather word-by-word memorization. 16 16 16 As demonstrated by [ 3 ] , in low-diversity datasets like bioS simple \textsf{bioS}^{\textsf{simple}} , knowledge can be word-by-word memorized but is nearly 0% extractable for downstream tasks. Others discover that rewriting data can improve the reversal extractability of knowledge [ 11 , 4 ] . However, they did not explore the impact on the model’s capacity. Our paper addresses this gap, indicating that rewriting pretraining data does not compromise — and may even enhance — the model’s knowledge capacity.

### 5.2 Parameterized Scaling Laws

We further investigate scaling laws within the bioD ​ ( N , K , C , D , L , T ) \textsf{bioD}(N,K,C,D,L,T) data family. Unlike with human biographies, where variation is limited to N N , the bioD dataset allows for more flexible manipulation of the remaining hyperparameters K , C , D , L , T K,C,D,L,T . This enables us to examine how variations in these parameters affect the model’s peak capacity.

Result 3 ( Figure 2 ) . Across a broad spectrum of values, with K , C K,C ranging from 1 1 to 50 50 , D D from 10 10 to 10,000 10,000 , L L from 1 1 to 50 50 , and T T from 20 20 to 40,000 40,000 , we observe that: • GPT2 models consistently exhibit a peak capacity ratio R ⁡ ( F ) ≥ 2 R(F)\geq 2 .

## 6 Training Time vs Scaling Law

What if the model is not sufficiently trained? For instance, there might be instances where knowledge appears only 100 times throughout the pretraining phase. We also calculate the capacity ratios for models trained with 100 exposures on bioS ​ ( N ) \textsf{bioS}(N) . Our findings can be summarized as follows: Result 4 ( Figure 1(b) ) . When trained for only 100 exposures on the bioS ​ ( N ) \textsf{bioS}(N) dataset, with N N ranging from 10K to 10M, across a broad spectrum of GPT2 models with sizes from 1M to 0.5B, the peak capacity ratio R ⁡ ( F ) R(F) consistently exceeds R ⁡ ( F ) ≥ 1 R(F)\geq 1 . Therefore, although 1000 exposures may be necessary for a model to reach its maximum storage capacity, training with just 100 exposures results in a capacity loss of no more than 2x.

In Section 10 , we shall also consider knowledge that has extremely low (e.g., 1) or high (e.g., 1M) exposures . It may not be interesting to study them in isolation, but it becomes more intriguing when they are examined alongside “standard” knowledge, which has appeared, for instance, for 100 exposures, and how this impacts the model’s capacity. These will be our Result 10 through 12 .

## 7 Model Architecture vs Scaling Law

Several transformer architectures have been widely adopted, with LLaMA and Mistral among the most notable. We outline their key distinctions from GPT2, with further details in Appendix B : 1. LLaMA/Mistral use so-called GatedMLP layers, which is V ⁡ ( σ ⁡ ( W 1 ​ x ) ⋅ ( W 2 ​ x ) ) V(\sigma(W_{1}x)\cdot(W_{2}x)) instead of V ​ σ ​ ( W ​ x ) V\sigma(Wx) . Shazeer [29] suggested that gated activation might yield marginally improved performance.

2. Unlike GPT2, LLaMA/Mistral do not tie weights.

3. Mistral features larger MLP layers compared to GPT2/LLaMA.

4. Mistral promotes group-query attention, not so by GPT2/LLaMA.

5. LLaMA/Mistral employ a different tokenizer than GPT2.

6. GPT2 uses the g ​ e ​ l ​ u gelu activation function, LLaMA/Mistral opt for s ​ i ​ l ​ u silu .

7. GPT2 implements layer normalization with a trainable bias.

Do these architectural variations impact the models’ maximum capacities? Our findings suggest that, in terms of knowledge capacity, GPT2 — when enhanced with rotary embedding and without dropout — performs no worse than any other architecture choice above in the sufficient training regime. We summarize the main findings below, deferring details to Appendix B.1 :

Result 5 ( Figure 3 ) . In the 1000-exposure setting, architectures do not matter much: • LLaMA architecture performs comparably to GPT2, albeit slightly inferior for the tiny model (i.e., < < 10M). This discrepancy can be mitigated by also requiring LLaMA architecture to tie weights, as shown in Figure 3(c) compared to Figure 3(b) . • A similar observation applies to Mistral architecture (see Figure 3(d) ). • Reducing the MLP size of GPT2 architecture by 1 / 4 1/4 or even eliminating all MLP layers does not affect its capacity ratio, see Figure 3(e) and Figure 3(f) . This suggests, contrary to conventional beliefs, the Attention layers are also capable of storing knowledge .

This indicates that the 2bit/param capacity ratio is a relatively universal law among most typical (decoder-only) language model architectures.

### 7.1 Insufficient Training Regime and a Closer Comparison

However, differences in architectures become apparent in the insufficient training regime:

Result 6 ( Figure 4 ) . In the 100-exposure setting: • Even for large models , LLaMA architecture’s capacity ratio can be 1.3x worse than GPT2 , even after optimally tuning learning rates. The results are similar for Mistral. • Reducing GPT2’s MLP size by 1 / 4 1/4 has a negligible impact on the capacity ratio. • Removing MLPs decreases the capacity ratio by more than 1.5x.

To investigate why the LLaMA architecture is inferior to GPT2 in the 100-exposure (insufficiently trained) setting, we closely examine LLaMA by gradually modifying its architecture back towards GPT2 to identify the key architectural changes. We start by tying weights, as this enhances tiny LLaMA model’s capacity in the 1000-exposure setting ( Result 5 ). As illustrated in Figure 5 :

• For large models, replacing LLaMA architecture’s gated MLP with a standard MLP (while keeping s ​ i ​ l ​ u silu unchanged) noticeably improves LLaMA’s capacity ratio. 17 17 17 As discussed in Appendix B , gated MLP layers are less stable to train, thus requiring more time.

• For tiny LLaMA models, switching back to the GPT2Tokenizer is also necessary to match GPT2’s performance, though this is a minor issue. 18 18 18 This only applies to tiny models and is specific to the biography data we consider here: GPT2Tokenizer may tokenize years such as 1991 into a single token, while LLaMATokenizer will tokenize it into four digit tokens.

• Other modifications, such as changing from s ​ i ​ l ​ u silu to g ​ e ​ l ​ u gelu or adding trainable biases to layernorms, do not noticeably affect the capacity ratios (so we ignore those figures).

In summary, Result 7 . In the insufficient training regime (notably, the 100-exposure setting), except for tiny models, architectural differences generally do not affect performance, except • Using gated MLP reduces the model’s capacity ratio ( Figure 5 ); • Removing all MLP layers lowers the model’s capacity ratio, although significantly reducing the size of MLPs (e.g., by a 1 / 4 1/4 factor) does not. We propose that our experiments with the controllable biography dataset could serve as a valuable testbed for future architectural designs.

## 8 Quantization vs Scaling Laws

We have trained and tested models using (mixed precision) 16-bit floats. What happens if we quantize them to int8/int4 after training? We used the auto_gptq package, which is inspired by the GPTQ paper [ 10 ] , for quantization.

Result 8 ( Figure 6 ) . Quantizing language models (e.g., GPT2) trained with 16-bit floats: • to int8 has a negligible impact on their capacity ; • to int4 reduces their capacity by more than 2x.

Thus, even for models at peak capacity of 2 bits/param, quantizing to int8 does not affect capacity. Given that 2 bits/param was the best capacity ratio even after 1,000 training exposures on high-quality data, we conclude that extending training may not further improve the model’s capacity, but quantization can .

Since an int8-based model has an absolute upper bound R ⁡ ( F ) ≤ 8 R(F)\leq 8 on capacity ratio, we have:

###### Corollary 8.1 .

Language models, like GPT2, can exceed 1/4 of the absolute theoretical limit for storing knowledge.

Unfortunately, using this quantization package, reducing the model to int4 significantly diminishes its capacity (more than 2x loss from int8 to int4). This suggests for high-quality int4 models, incorporating quantization during training may be necessary.

### 8.1 Where Is the Knowledge Stored?

We have seen that LLMs can efficiently compress knowledge into their parameter space, achieving 2bit/param even with 8-bit parameters. This raises the question: how and where is such knowledge stored? Our preliminary answer is that knowledge can be compactly stored within the model in a not-so-redundant manner. It is unlikely that the MLP layers alone store knowledge, as Attention layers, being of comparable sizes, also contribute to knowledge storage (c.f. Result 5 ). Moreover, particularly in models near the capacity boundary, removing the last transformer layer of an L L -layer model to “probe” for remaining knowledge reveals that the “leftover knowledge” can be significantly less than 1 − 1 L 1-\frac{1}{L} of the total. 19 19 19 This experiment, deemed not particularly interesting, was omitted from the paper. The probing technique used is Q-probing from [ 3 ] . This suggests knowledge is stored not in individual layers but in a complex manner, akin to a safe with combination locks, where removing one layer may eliminate much more than 1 L \frac{1}{L} of the total knowledge.

## 9 Mixture of Experts vs Scaling Laws

An important way to enhance efficiency in modern language models is the incorporation of sparsity. The Mixture of Experts (MoE) architecture plays a crucial role in this regard [ 9 , 30 ] . A question arises: does the MoE model scale differently in terms of the capacity ratio? For an MoE model, let P P denote the total number of parameters in the model , including all experts. Due to its inherent sparsity, the effective number of parameters can be significantly less than P P . Our primary observation is that MoE models scale similarly to dense models, even with 32 experts per layer.

Consider, for instance, GPT2, but with its MLP layer ( d → 4 ​ d → d d\to 4d\to d ) replaced by 32 experts, each following a d → d → d d\to d\to d configuration. This setup uses 64 ​ d 2 64d^{2} total parameters, but during inference, only 2 ​ d 2 2d^{2} parameters are used per token (e.g., when using t ​ o ​ p ​ k = 1 topk=1 ). After including the Attention layers, which each have 4 ​ d 2 4d^{2} parameters, the ratio between the total and the effective number of parameters for the 32-expert MoE models is approximately 4 ​ d 2 + 64 ​ d 2 4 ​ d 2 + 2 ​ d 2 ≈ 11.3 \frac{4d^{2}+64d^{2}}{4d^{2}+2d^{2}}\approx 11.3 .

One might wonder, given that during inference time, the model uses only 11.3x fewer parameters, whether this affects the model’s capacity ratio by a factor close to 11.3x or closer to 1x? We show:

Result 9 ( Figure 7 ) . MoE is nearly fully efficient in storing knowledge , capable of leveraging all its parameters despite the sparsity constraint. Specifically, consider the GPT2-MoE model with 32 experts. If we compute its capacity ratio with respect to the total number of parameters and compare that to GPT2: • in the 1000-exposure settings, the peak capacity ratio decreases by 1.3x; and • in the 100-exposure settings, the peak capacity ratio decreases by 1.5x.

###### Remark 9.1 (topk) .

Result 9 holds even in the “sparsest” setting where t ​ o ​ p ​ k = 1 topk=1 and c ​ a ​ p ​ _ ​ f ​ a ​ c ​ t ​ o ​ r = 2 cap\_factor=2 in the MoE routing. The results are similar when using t ​ o ​ p ​ k = 2 topk=2 and c ​ a ​ p ​ _ ​ f ​ a ​ c ​ t ​ o ​ r = 1 cap\_factor=1 or t ​ o ​ p ​ k = 2 topk=2 and c ​ a ​ p ​ _ ​ f ​ a ​ c ​ t ​ o ​ r = 2 cap\_factor=2 — we discuss more in Appendix D .

###### Remark 9.2 .

It is typically observed in practice that MoE models underperform compared to dense models with the same number of total parameters. We demonstrate that this degradation does not come from the model’s knowledge storage capability.

## 10 Junk Data vs Scaling Laws

Not all data are useful for knowledge acquisition. For instance, while Wikipedia is full of valuable information, the Common Crawl of web pages may not be (there are also many pieces of information on those webpages, but they may not be useful for a language model to learn, such as the serial number of a random product). How does the presence of low-quality data impact the scaling laws of useful knowledge capacity ? To investigate this, we create a mixed dataset where: • 1 / 8 1/8 of tokens originate from bioS ​ ( N ) \textsf{bioS}(N) for various N N (referred to as useful data ), and

• 7 / 8 7/8 of tokens originate from bioS ​ ( N ′ ) \textsf{bioS}(N^{\prime}) for a large N ′ = 100 ​ M N^{\prime}=100M (referred to as junk data ).

We train models on this mixture, ensuring each piece of useful data is seen for 100 exposures, thus making the total training 8 times longer compared to 100 exposures without junk (i.e., Figure 1(b) ). We focus on the capacity ratio of the useful data (the data in bioS ​ ( N ) \textsf{bioS}(N) ) and compare that to Figure 1(b) . 20 20 20 The model’s ability to learn from junk data is negligible; each person in bioS ​ ( N ′ ) \textsf{bioS}(N^{\prime}) appears only 0.2 times during training when N = 200 ​ k N=200k , or 0.05 times when N = 50 ​ k N=50k . How much does the capacity ratio degrade in the presence of junk data?

Result 10 ( Figure 8(a) - 8(e) ) . When 7/8 of the training tokens come from junk data (i.e., bioS ​ ( N ′ ) \textsf{bioS}(N^{\prime}) for N ′ = 100 ​ M N^{\prime}=100M ), transformer’s learning speed for useful data significantly degrades: • If trained for the same 100 exposures, the capacity ratio may degrade by 20x compared with training without junk (compare Figure 8(b) with Figure 8(a) ). • Even trained for 300/600/1000 exposures, the capacity ratio still degrades by 3x/1.5x/1.3x compared with 100 exposures without junk ( Figure 8(c) , 8(d) , and 8(e) vs. Figure 8(a) ). This underscores the crucial importance of pretrain data quality : even if junk data is entirely random, it negatively impacts model’s knowledge capacity even with sufficient training.

In contrast, if 7/8 of data is bioS ​ ( N ′ ) \textsf{bioS}(N^{\prime}) with a very small N ′ N^{\prime} , simulating highly repetitive knowledge appearing in training tokens (e.g., “da Vinci painted the Mona Lisa” in millions of variations), this may not affect the model’s capacity for “standard” knowledge (e.g., those with 100 exposures): Result 11 ( Figure 8(f) ) . If 7/8 of the training tokens come from highly repetitive data (i.e., bioS ​ ( N ′ ) \textsf{bioS}(N^{\prime}) for N ′ = 1 ​ K N^{\prime}=1K ), this does not affect the learning speed of useful knowledge: • The 100-exposure capacity ratio of useful data is unchanged ( Figure 8(f) vs. Figure 8(a) ).

Finally, if pretrain data’s quality is poor and hard to improve, a backup strategy exists: Result 12 ( Figure 8(g) + 8(h) ) . When 7/8 of training tokens are from junk (i.e., bioS ​ ( N ′ ) \textsf{bioS}(N^{\prime}) for N ′ = 100 ​ M N^{\prime}=100M ), adding a special token at the start of every useful data greatly improves capacity ratio: • With 100 exposures, the capacity ratio degrades only by 2x ( Figure 8(g) vs. Figure 8(a) ). • With 300 exposures, the capacity ratio matches that of the 100-exposure scaling law without junk (compare Figure 8(h) with Figure 8(a) ).

Let us connect Result 12 to practice. First, adding a special token to high-credibility data is very practical: imagine adding the domain name ‘‘wikipedia.org’’ at the beginning of all Wikipedia paragraphs. (Adding a special token to junk data would be less meaningful.) 21 21 21 Result 12 also holds if one adds a (unique) special token for every piece of junk data; however, this could be meaningless as junk data often originates from various websites, making it hard to assign a unique identifier.

More generally, one can envision adding domain names (e.g., wikipedia.org) to every piece of the pretraining data. This would significantly enhance the model’s knowledge capacities, because Result 12 demonstrates that language models can automatically detect which domains are rich in high-quality knowledge and prioritize learning from them . We emphasize that the model does not need any prior knowledge to identify which domains contain high-quality knowledge; this process is entirely autonomous .

## 11 Conclusion

We investigated the scaling laws of language models, specifically the relationship between model size and the total bits of knowledge stored. Our findings reveal a precise, universal scaling law: a sufficiently-trained transformer (i.e., one whose training loss has plateau-ed) can store 2 bits of knowledge per parameter, even when quantized to int8, which is only 1 / 4 1/4 away from the information-theoretical maximum. We also examined how these scaling laws are influenced by various hyperparameters, including training duration, model architectures, floating-point precision, sparsity constraints like MoE, and data signal-noise ratios.

In terms of knowledge capacity, our methodology provides a more accurate and principled playground for comparing model architectures, training techniques, and data quality. We believe this playground can assist practitioners in making informed decisions about model selection, training data preparation, and further theoretical research into LLMs. Finally, our research represents an initial step towards addressing a fundamental question: how large does a language model need to be? We hope our findings will inspire further research in this area. Ultimately, we aim to provide a principled answer to the question, “Are language models with 1T parameters sufficient to achieve AGI?” in the future.

Appendix

## References

[1] Ibrahim M Alabdulmohsin, Behnam Neyshabur, and Xiaohua Zhai. Revisiting neural scaling laws in language and vision. Advances in Neural Information Processing Systems , 35:22300–22312, 2022.

[2] Zeyuan Allen-Zhu and Yuanzhi Li. Physics of Language Models: Part 1, Context-Free Grammar. ArXiv e-prints , abs/2305.13673, May 2023a. Full version available at http://arxiv.org/abs/2305.13673 .

[3] Zeyuan Allen-Zhu and Yuanzhi Li. Physics of Language Models: Part 3.1, Knowledge Storage and Extraction. ArXiv e-prints , abs/2309.14316, September 2023b. Full version available at http://arxiv.org/abs/2309.14316 .

[4] Zeyuan Allen-Zhu and Yuanzhi Li. Physics of Language Models: Part 3.2, Knowledge Manipulation. ArXiv e-prints , abs/2309.14402, September 2023c. Full version available at http://arxiv.org/abs/2309.14402 .

[5] Zeyuan Allen-Zhu, Yuanzhi Li, and Yingyu Liang. Learning and generalization in overparameterized neural networks, going beyond two layers. Advances in neural information processing systems , 32, 2019a.

[6] Zeyuan Allen-Zhu, Yuanzhi Li, and Zhao Song. A convergence theory for deep learning via over-parameterization. In International conference on machine learning , pages 242–252. PMLR, 2019b.

[7] Sid Black, Stella Biderman, Eric Hallahan, Quentin Anthony, Leo Gao, Laurence Golding, Horace He, Connor Leahy, Kyle McDonell, Jason Phang, Michael Pieler, USVSN Sai Prashanth, Shivanshu Purohit, Laria Reynolds, Jonathan Tow, Ben Wang, and Samuel Weinbach. GPT-NeoX-20B: An open-source autoregressive language model. In Proceedings of the ACL Workshop on Challenges & Perspectives in Creating Large Language Models , 2022. URL https://arxiv.org/abs/2204.06745 .

[8] Sébastien Bubeck, Varun Chandrasekaran, Ronen Eldan, Johannes Gehrke, Eric Horvitz, Ece Kamar, Peter Lee, Yin Tat Lee, Yuanzhi Li, Scott Lundberg, et al. Sparks of artificial general intelligence: Early experiments with gpt-4. arXiv preprint arXiv:2303.12712 , 2023.

[9] William Fedus, Barret Zoph, and Noam Shazeer. Switch transformers: Scaling to trillion parameter models with simple and efficient sparsity. The Journal of Machine Learning Research , 23(1):5232–5270, 2022.

[10] Elias Frantar, Saleh Ashkboos, Torsten Hoefler, and Dan Alistarh. GPTQ: Accurate post-training compression for generative pretrained transformers. arXiv preprint arXiv:2210.17323 , 2022.

[11] Olga Golovneva, Zeyuan Allen-Zhu, Jason Weston, and Sainbayar Sukhbaatar. Reverse training to nurse the reversal curse. arXiv preprint arXiv:2403.13799 , 2024.

[12] Suriya Gunasekar, Yi Zhang, Jyoti Aneja, Caio César Teodoro Mendes, Allie Del Giorno, Sivakanth Gopi, Mojan Javaheripi, Piero Kauffmann, Gustavo de Rosa, Olli Saarikivi, et al. Textbooks are all you need. arXiv preprint arXiv:2306.11644 , 2023.

[13] Tom Henighan, Jared Kaplan, Mor Katz, Mark Chen, Christopher Hesse, Jacob Jackson, Heewoo Jun, Tom B Brown, Prafulla Dhariwal, Scott Gray, et al. Scaling laws for autoregressive generative modeling. arXiv preprint arXiv:2010.14701 , 2020.

[14] Danny Hernandez, Jared Kaplan, Tom Henighan, and Sam McCandlish. Scaling laws for transfer. arXiv preprint arXiv:2102.01293 , 2021.

[15] Joel Hestness, Sharan Narang, Newsha Ardalani, Gregory Diamos, Heewoo Jun, Hassan Kianinejad, Md Mostofa Ali Patwary, Yang Yang, and Yanqi Zhou. Deep learning scaling is predictable, empirically. arXiv preprint arXiv:1712.00409 , 2017.

[16] Jordan Hoffmann, Sebastian Borgeaud, Arthur Mensch, Elena Buchatskaya, Trevor Cai, Eliza Rutherford, Diego de Las Casas, Lisa Anne Hendricks, Johannes Welbl, Aidan Clark, et al. Training compute-optimal large language models. arXiv preprint arXiv:2203.15556 , 2022.

[17] Edward J Hu, Phillip Wallis, Zeyuan Allen-Zhu, Yuanzhi Li, Shean Wang, Lu Wang, Weizhu Chen, et al. LoRA: Low-Rank Adaptation of Large Language Models. In ICLR , 2021.

[18] Changho Hwang, Wei Cui, Yifan Xiong, Ziyue Yang, Ze Liu, Han Hu, Zilong Wang, Rafael Salas, Jithin Jose, Prabhat Ram, Joe Chau, Peng Cheng, Fan Yang, Mao Yang, and Yongqiang Xiong. Tutel: Adaptive mixture-of-experts at scale. CoRR , abs/2206.03382, June 2022. URL https://arxiv.org/pdf/2206.03382.pdf .

[19] Albert Q Jiang, Alexandre Sablayrolles, Arthur Mensch, Chris Bamford, Devendra Singh Chaplot, Diego de las Casas, Florian Bressand, Gianna Lengyel, Guillaume Lample, Lucile Saulnier, et al. Mistral 7b. arXiv preprint arXiv:2310.06825 , 2023.

[20] Mandar Joshi, Eunsol Choi, Daniel S Weld, and Luke Zettlemoyer. Triviaqa: A large scale distantly supervised challenge dataset for reading comprehension. arXiv preprint arXiv:1705.03551 , 2017.

[21] Jared Kaplan, Sam McCandlish, Tom Henighan, Tom B Brown, Benjamin Chess, Rewon Child, Scott Gray, Alec Radford, Jeffrey Wu, and Dario Amodei. Scaling laws for neural language models. arXiv preprint arXiv:2001.08361 , 2020.

[22] Tom Kwiatkowski, Jennimaria Palomaki, Olivia Redfield, Michael Collins, Ankur Parikh, Chris Alberti, Danielle Epstein, Illia Polosukhin, Jacob Devlin, Kenton Lee, et al. Natural questions: a benchmark for question answering research. Transactions of the Association for Computational Linguistics , 7:453–466, 2019.

[23] Yuanzhi Li and Yingyu Liang. Learning overparameterized neural networks via stochastic gradient descent on structured data. In Advances in Neural Information Processing Systems , 2018.

[24] Yuanzhi Li, Sébastien Bubeck, Ronen Eldan, Allie Del Giorno, Suriya Gunasekar, and Yin Tat Lee. Textbooks are all you need ii: phi-1.5 technical report. arXiv preprint arXiv:2309.05463 , 2023.

[25] Niklas Muennighoff, Alexander M Rush, Boaz Barak, Teven Le Scao, Aleksandra Piktus, Nouamane Tazi, Sampo Pyysalo, Thomas Wolf, and Colin Raffel. Scaling data-constrained language models. arXiv preprint arXiv:2305.16264 , 2023.

[26] Alec Radford, Jeffrey Wu, Rewon Child, David Luan, Dario Amodei, Ilya Sutskever, et al. Language models are unsupervised multitask learners. OpenAI blog , 1(8):9, 2019.

[27] Jonathan S Rosenfeld. Scaling laws for deep learning. arXiv preprint arXiv:2108.07686 , 2021.

[28] Jonathan S Rosenfeld, Amir Rosenfeld, Yonatan Belinkov, and Nir Shavit. A constructive prediction of the generalization error across scales. arXiv preprint arXiv:1909.12673 , 2019.

[29] Noam Shazeer. Glu variants improve transformer. arXiv preprint arXiv:2002.05202 , 2020.

[30] Noam Shazeer, Azalia Mirhoseini, Krzysztof Maziarz, Andy Davis, Quoc Le, Geoffrey Hinton, and Jeff Dean. Outrageously large neural networks: The sparsely-gated mixture-of-experts layer. In International Conference on Learning Representations , 2016.

[31] Jianlin Su, Yu Lu, Shengfeng Pan, Bo Wen, and Yunfeng Liu. Roformer: Enhanced transformer with rotary position embedding, 2021.

[32] Hugo Touvron, Thibaut Lavril, Gautier Izacard, Xavier Martinet, Marie-Anne Lachaux, Timothée Lacroix, Baptiste Rozière, Naman Goyal, Eric Hambro, Faisal Azhar, et al. Llama: Open and efficient foundation language models. arXiv preprint arXiv:2302.13971 , 2023a.

[33] Hugo Touvron, Louis Martin, Kevin Stone, Peter Albert, Amjad Almahairi, Yasmine Babaei, Nikolay Bashlykov, Soumya Batra, Prajjwal Bhargava, Shruti Bhosale, et al. Llama 2: Open foundation and fine-tuned chat models. arXiv preprint arXiv:2307.09288 , 2023b.

[34] Dingli Yu, Simran Kaur, Arushi Gupta, Jonah Brown-Cohen, Anirudh Goyal, and Sanjeev Arora. Skill-mix: A flexible and expandable family of evaluations for ai models. arXiv preprint arXiv:2310.17567 , 2023.

## Instructions for reporting errors

We are continuing to improve HTML versions of papers, and your feedback helps enhance accessibility and mobile support. To report errors in the HTML that will help us improve conversion and rendering, choose any of the methods listed below:

Click the "Report Issue" ( ) button, located in the page header.

Tip: You can select the relevant text first, to include it in your report.

Our team has already identified the following issues . We appreciate your time reviewing and reporting rendering errors we may not have found yet. Your efforts will help us improve the HTML versions for all readers, because disability should not be a barrier to accessing research. Thank you for your continued support in championing open access for all.

Have a free development cycle? Help support accessibility at arXiv! Our collaborators at LaTeXML maintain a list of packages that need conversion , and welcome developer contributions .

## Appendix A More on GPT2 Scaling Laws

In this paper, our primary focus is on bioS ​ ( N ) \textsf{bioS}(N) for N N ranging between 10K and 20M. Notably, bioS ​ ( 20 ​ M ) \textsf{bioS}(20M) encompasses approximately 1B bits of knowledge (refer to Theorem 3.2 ).

GPT2 model. As elaborated in Section 2.3 , we refer to the original GPT2 model [ 26 ] as GPT2, after substituting its positional embedding with rotary embedding [ 31 , 7 ] and removing its dropout layer [ 33 ] . These modifications are widely recognized for enhancing performance in language modeling tasks (see also [ 2 ] for a controlled experiment comparing that). We explore various GPT2 model sizes, maintaining a dimension-per-head of 64. The notation GPT2- ℓ \ell - h h represents the (modified) GPT2 architecture with ℓ \ell layers, h h heads, and 64 ​ h 64h dimensions. The context length is set to 512.

Details on our specifications of LLaMA, Mistral, and other architectures will be provided in Appendix B as needed.

Model sizes. In this study, we calculate model sizes after excluding all unused tokens in the embedding layer. For example, while the GPT2 embedding layer typically has 50256 × ( 64 ​ h ) 50256\times(64h) parameters, our bioS ​ ( N ) \textsf{bioS}(N) data utilizes only 3275 tokens (after applying GPT2’s tokenizer), reducing the effective embedding layer size to 3275 × ( 64 ​ h ) 3275\times(64h) . This adjustment explains why, for bioS data, GPT2small, typically known to have 124M parameters, is counted as having only 88M parameters in this paper.

We have selected a broad range of GPT2- ℓ \ell - h h models with practical ℓ \ell and h h values, excluding those with similar model sizes. Their selection is detailed in Figure 1 , encompassing both wide and shallow transformers (e.g., GPT2-2-20, GPT2-3-20, GPT2-4-20) and skinny and deep transformers (e.g., GPT2-16-4, GPT2-16-8, GPT2-28-20). For reference, GPT2 small/med/large correspond to GPT2-12-12, GPT2-24-16, GPT2-36-20, respectively.

We primarily focus on models with ℓ ≥ 2 \ell\geq 2 , as 1-layer transformers may demonstrate slightly lower capacity ratios. (For those interested, 1-layer transformers are included in Figure 9 , which is identical to Figure 1 but includes these models.)

Model sizes for datasets bioS ​ ( N ) \textsf{bioS}(N) with N ≥ 𝟐 ​ M N\geq 2M . In the 1000-exposure setting, to conserve computational resources, when exploring scaling laws for N = 2 ​ M , 5 ​ M , 10 ​ M , 20 ​ M N=2M,5M,10M,20M , we concentrate on one model size per dataset — specifically GPT2-16-8, GPT2-6-20, GPT2-20-16, GPT2-25-20 — as they approach the 2bit/param threshold (i.e., they satisfy R 𝗆𝖺𝗑 ​ ( F ) ≈ 2 R^{\mathsf{max}}(F)\approx 2 ). In this context, our key finding is the validation of the 2bit/param capacity ratio, thus examining a limited selection of model sizes is adequate.

For the 100-exposure setting, we evaluate a broader range of model sizes per dataset. This approach is not only due to the tenfold reduction in training time compared to the 1000-exposure setting but also to facilitate a detailed comparison of model architectures in the 100-exposure setting, aiming for precision at higher model sizes.

Training parameters. We employ the AdamW optimizer with a cosine learning rate scheduler. This includes 1K steps of warmup, followed by a cosine decay of the learning rate from 1 1 to 0.1 0.1 times the reference rate. We use mixed-precision fp16 training unless otherwise stated.

### A.1 Base Scaling Laws

Our base scaling laws for the 1000-exposure and 100-exposure bioS ​ ( N ) \textsf{bioS}(N) data are presented in Figures 1(a) and 1(b) , respectively.

For the 1000-exposure setting, the model’s final performance is not very sensitive to learning rate choices due to sufficient training. The following parameters were chosen for generating Figure 1(a) :

###### Parameter 1 ( Figure 1(a) ) .

In the 1000-exposure setting for GPT2 models on bioS ​ ( N ) \textsf{bioS}(N) data: • For N = 10 ​ K N=10K , we use w ​ d = 0.02 wd=0.02 , l ​ r = 0.001 lr=0.001 , and batch size 24 (about 140K training steps);

• For N = 20 ​ K N=20K , we use w ​ d = 0.02 wd=0.02 , l ​ r = 0.001 lr=0.001 , and batch size 48 (about 140K training steps);

• For N = 50 ​ K N=50K , we use w ​ d = 0.02 wd=0.02 , l ​ r = 0.001 lr=0.001 , and batch size 96 (about 175K training steps);

• For N = 100 ​ K , 200 ​ K N=100K,200K , we use w ​ d = 0.02 wd=0.02 , l ​ r = 0.001 lr=0.001 , batch size 192 (about 175K, 349K training steps);

• For N = 500 ​ K , 1 ​ M N=500K,1M , we use w ​ d = 0.01 wd=0.01 , l ​ r = 0.0005 lr=0.0005 , batch size 192 (about 435K, 870K training steps);

• For N = 2 ​ M N=2M , we use w ​ d = 0.005 wd=0.005 , l ​ r = 0.0003 lr=0.0003 , and batch size 1536 1536 (about 220K training steps);

• For N = 5 ​ M N=5M , we use w ​ d = 0.002 wd=0.002 , l ​ r = 0.0003 lr=0.0003 , and batch size 1536 1536 (about 540K training steps);

• For N = 10 ​ M N=10M , we use w ​ d = 0.001 wd=0.001 , l ​ r = 0.0003 lr=0.0003 , and batch size 1536 1536 (about 1M training steps).

###### Remark A.1 (fp16 vs bf16) .

Training on GPT2 is conducted using mixed-precision fp16. We also tried bf16 and the results are nearly identical.

###### Remark A.2 (parameters) .

These optimization parameters are very natural , as it is generally impossible to have a fixed set of parameters for model sizes across a large multiplicative range. Notably: • Larger model sizes naturally require smaller learning rates.

• Language models typically need at least 50K training steps regardless of batch size. Thus, for small N N , we reduce the batch size to ensure the total number of training steps exceeds this threshold. For very large models, a larger batch size is preferred to enable GPU parallelism.

• When l ​ r lr remains constant, w ​ d wd should be relatively reduced as the number of training steps increases. Mathematically, the model weights should be “halved” for every Θ ⁡ ( 1 l ​ r × w ​ d ) \Theta(\frac{1}{lr\times wd}) training steps. Therefore, it’s advisable to reduce the w ​ d wd parameter when training for longer periods.

###### Remark A.3 (# GPUs) .

In this paper, we do not specify the number of GPUs as it is irrelevant . The results remain the same whether using 64 GPUs each with a batch size of 24, 48 GPUs each with a batch size of 32, or 1536 GPUs each with a batch size of 1.

For the 100-exposure setting, careful tuning of learning rates is required. The following parameters were chosen for generating Figure 1(b) : (Note: N = 10 ​ K , 20 ​ K N=10K,20K are not considered for the 100-exposure setting due to the excessively short training process.)

###### Parameter 2 ( Figure 1(b) ) .

In the 100-exposure setting for GPT2 models on bioS ​ ( N ) \textsf{bioS}(N) data: • For N = 50 ​ K N=50K , we use w ​ d = 0.01 wd=0.01 , l ​ r = 0.001 lr=0.001 , and batch size 12;

• For N = 100 ​ K N=100K , we use w ​ d = 0.01 wd=0.01 , l ​ r = 0.001 lr=0.001 , and batch size 24;

• For N = 200 ​ K N=200K , we use w ​ d = 0.01 wd=0.01 , l ​ r = 0.001 lr=0.001 , and batch size 48; (except for GPT2-2-20, where l ​ r = 0.0005 lr=0.0005 is used)

• For N = 500 ​ K N=500K , we use w ​ d = 0.01 wd=0.01 , l ​ r = 0.0005 lr=0.0005 , and batch size 96;

• For N = 1 ​ M N=1M , we use w ​ d = 0.01 wd=0.01 , l ​ r = 0.0005 lr=0.0005 , and batch size 192;

• For N = 2 ​ M N=2M , we use w ​ d = 0.01 wd=0.01 , l ​ r = 0.0003 / 0.0005 / 0.001 lr=0.0003/0.0005/0.001 , and batch size 384 384 ;

• For N = 5 ​ M N=5M , we use w ​ d = 0.01 wd=0.01 , l ​ r = 0.0003 / 0.0005 lr=0.0003/0.0005 , and batch size 768 768 ;

• For N = 10 ​ M N=10M , we use w ​ d = 0.01 wd=0.01 , l ​ r = 0.0002 / 0.0003 / 0.0005 lr=0.0002/0.0003/0.0005 , and batch size 1024 1024 ;

• For N = 20 ​ M N=20M , we use w ​ d = 0.002 wd=0.002 , l ​ r = 0.0002 / 0.0003 / 0.0005 lr=0.0002/0.0003/0.0005 , and batch size 1536 1536 . 22 22 22 Except for GPT2-28-20 we run out of GPU memory so reduce to batch size 1280 1280 .

### A.2 Knowledge Memorization vs. Extraction

It was recently discovered by Allen-Zhu and Li [3] that although models memorize knowledge, this knowledge may not be extractable (e.g., via fine-tuning) for application in downstream tasks. It is essential to verify that the “2 bit/param” knowledge learned by models is indeed extractable. This verification is achieved by applying a fine-tuning task (e.g., “What is Anya’s birthday? Answer: October 2, 1996”) to half of the individuals and then testing its performance on the remainder.

Specifically, on the original bioS ​ ( N ) \textsf{bioS}(N) data, we compute two quantities for each model: • Memorizable knowledge accuracy (# of people) .

We apply the model to the original training data, such as ‘‘Anya Briar Forger was born on’’ and check if it can correctly generate ‘‘October 2, 1996’’. For each person, we evaluate all five attributes and compute their average accuracy. 23 23 23 We exclude the company city attribute because it can be uniquely determined by the employer name, thus providing no additional knowledge. We then sum this accuracy up over all N N people. (Ideally, a perfect model would have this “accuracy” equal to N N .)

• Extractable knowledge accuracy (# of people) . Following the pretrain-finetune framework of [ 3 ] , we fine-tune any given pretrained model on half of the individuals using LoRA [ 17 ] with question-answering texts like “What is the birthday of Anya Briar Forger? Answer: October 2, 1996.” We then test its generation accuracy on the remaining half of the individuals. High accuracy indicates that the knowledge is not only memorized but can also be flexibly extracted for downstream tasks. Again, for each person, we evaluate all five attributes and compute their average accuracy. We then sum this across all N / 2 N/2 people and multiply by 2 2 . (Once again, a perfect model would have this equal to N N .)

Our results are presented in Figure 10 . By comparing, for instance, Figure 10(a) against Figure 10(b) , it is evident that our scaling laws apply not only to memorizable knowledge but also largely to extractable knowledge. Only for models precisely at the capacity ratio boundary is there a 1.2x decrease in total accuracy. 24 24 24 This decrease is in accuracy, not bits; a model may have a large amount of extractable knowledge in bits but not in accuracy. One can also compute knowledge bits in the extractable setting, but we omit such results for brevity.

###### Parameter 3 ( Figure 10 ) .

When dealing with models of significantly different sizes for LoRA finetuning, it’s necessary to adjust the LoRA rank sizes. In [ 3 ] , the authors primarily used a rank r ′ = 128 r^{\prime}=128 update for the embedding layer and ranks r = 8 r=8 or 16 16 for the query/value matrices, with their base model being either GPT2-12-12 or GPT2-12-20. In this paper, we explore a broader range of rank choices: ( r ′ , r ) ∈ { ( 8 , 2 ) , ( 16 , 2 ) , ( 8 , 4 ) , ( 32 , 4 ) , ( 8 , 8 ) , ( 32 , 8 ) , ( 128 , 8 ) , ( 32 , 16 ) , ( 128 , 16 ) } (r^{\prime},r)\in\{(8,2),(16,2),(8,4),(32,4),(8,8),(32,8),(128,8),(32,16),(128,16)\} , presenting only the best results. 25 25 25 Selecting the best LoRA option is justified as our aim is to determine the maximum extractable knowledge bits, and thus, any LoRA option demonstrating high test-set accuracy fulfills our objective.

We disable learning rate warmup, set the batch size to 96, the learning rate to 0.001 (with linear decay down to 0), weight decay at 0.1, and finetune for 75,000 steps.

### A.3 Other Biography Datasets

We also examine the bioS simple ​ ( N ) \textsf{bioS}^{\textsf{simple}}(N) datasets, which are identical to bioS ​ ( N ) \textsf{bioS}(N) except that each individual’s knowledge is stored in a fixed ordering of six fixed sentences (see Section 2.2 ). Allen-Zhu and Li [3] found that in such cases, the knowledge data are memorizable but nearly 0% extractable. As shown in Figure 11(a) , in these instances, the capacity ratio slightly decreases compared to Figure 1(a) . This implies, in this ideal setting, adding data diversity — by rewriting the same knowledge multiple times using different writing templates — not only enhances the model’s ability to extract knowledge, as noted by [ 3 ] , but also, surprisingly, increases the model’s capacity, as observed in this study.

Moreover, we explore the semi-real dataset bioR ​ ( N ) \textsf{bioR}(N) , which resembles bioS ​ ( N ) \textsf{bioS}(N) but with the biography paragraph generated by LLaMA2, and each individual is generated 40 times (using random seeds and prompts to encourage LLaMA2 to generate as diverse paragraphs as possible for each person). This results in a total of 22GB of text, comparable to the size of Wikipedia data.

The scaling law for the bioR ​ ( N ) \textsf{bioR}(N) data is presented in Figure 11(b) , indicating that the capacity ratio slightly decreases for larger models. This trend is expected, as LLaMA2 introduces numerous irrelevant details into the human biographies — usually different irrelevant details for each LLaMA2 generation — thereby consuming more model capacity. The decrease is more significant for smaller models, which may have greater difficulty comprehending the diverse English sentences in the data.

###### Parameter 4 ( Figure 11 ) .

In both experiments, we adhere to the same set of optimizer parameters used in Figure 1(a) , as detailed in Parameter 1 .

### A.4 More on Parameterized Scaling Laws

In the parameterized scaling laws, we utilize the bioD ​ ( N , K , C , D , L , T ) \textsf{bioD}(N,K,C,D,L,T) dataset from Definition 2.2 .

###### Parameter 5 ( Figure 2 , 12 , 13 ) .

For GPT2 models on the bioD dataset, we focus on the 1000-exposure case, with w ​ d = 0.01 wd=0.01 , l ​ r = 0.0005 lr=0.0005 , and a batch size of 192.

###### Remark A.4 (parameters) .

Contrary to Parameter 1 , it is not necessary to vary the training parameters, as our experiments with GPT2 models span a much narrower range of model sizes. We have adjusted the choice of N N to ensure that the optimal 2bit/param models are within a factor of 20 of each other in terms of model sizes.

Our results are presented in Figure 2 (in the main body, limited to models with accuracy ≤ 50 % \leq 50\% for clarity) and in Figure 12 (including all models).

Furthermore, from the bit complexity lower bound (see Definition 4.1 ) N ​ log 2 ​ N 0 e p 1 ⏟ name + N ​ K ​ log 2 ⁡ D C e p 2 ⏟ value + K ​ D ​ log 2 ⁡ T L D ​ e p 3 ⏟ diversity \displaystyle\underbrace{N\log_{2}\frac{N_{0}}{e^{p_{1}}}}_{\text{name }}+\underbrace{NK\log_{2}\frac{D^{C}}{e^{p_{2}}}}_{\text{value }}+\underbrace{KD\log_{2}\frac{T^{L}}{De^{p_{3}}}}_{\text{diversity }} (A.1) we also dissect how the three components contribute to this overall lower bound. As shown in Figure 13 , although the “value” component typically dominates, for certain hyperparameter settings, the “name” or “diversity” components can also be significant. This underscores the importance of proving our Theorem 3.2 lower bound, which is a sum of all three terms.

## Appendix B More on Model Architectures

We explore alternative architectural choices for language models.

LLaMA/Mistral. Notably, as of the writing of this paper, LLaMA [ 32 , 33 ] and Mistral [ 19 ] stand out as popular, publicly-available large language models. We highlight their key architecture differences from GPT2 — which we define as having rotary embedding and no dropout. 1. LLaMA and Mistral employ MLP layers with gated activation, using V ⁡ ( σ ⁡ ( W 1 ​ x ) ⋅ ( W 2 ​ x ) ) V(\sigma(W_{1}x)\cdot(W_{2}x)) instead of V ​ σ ​ ( W ​ x ) V\sigma(Wx) . Shazeer [29] noted that gated activation appears to yield slightly better performance.

2. Unlike GPT2, which ties the weights of the embedding layer and the output (LMHead) layer, LLaMA and Mistral do not.

3. For a hidden dimension d d , GPT2/LLaMA have 4 ​ d 2 4d^{2} parameters in the attention layer and 8 ​ d 2 8d^{2} in the MLP layer, whereas Mistral allocates a larger 10.5 ​ d 2 10.5d^{2} for its MLP layer.

4. Mistral promotes group-query attention (e.g., using 4 4 groups, thus reducing the K/V matrices to d 2 / 4 d^{2}/4 in size), unlike GPT2. LLaMA does not favor multi-query attention unless in its very large models, such as the 70B variant.

5. LLaMA and Mistral utilize different tokenizers compared to GPT2, with Mistral’s tokenizer being nearly identical to LLaMA’s.

6. GPT2 employs σ = g ​ e ​ l ​ u \sigma=gelu , while LLaMA/Mistral use σ = s ​ i ​ l ​ u \sigma=silu .

7. GPT2 incorporates layer normalization with trainable bias, which LLaMA/Mistral do not.

Given these distinctions, for LLaMA models, we use the notation LLaMA- ℓ \ell - h h for ℓ \ell layers, h h heads, and 64 ​ h 64h hidden dimensions; we omit group-query attention as LLaMA recommends it only for its 70B model. For Mistral, denoted as Mistral- ℓ \ell - h h , we enable group-query attention with 4 4 groups if h = 0 ( mod 4 ) h=0\pmod{4} , 1 1 group for odd h h , or 2 2 groups otherwise.

GPT2 with Smaller MLP. Mistral has a larger MLP layer, and it is often believed that the MLP layer serves primarily for storing knowledge, in contrast to the Attention layer. But is this truly the case?

To delve into this, we examine GPT2 1/4 , which is GPT2 with its MLP layer reduced from d → 4 ​ d → d d\to 4d\to d to d → d → d d\to d\to d (thus, 1 / 4 1/4 of its original size), and GPT2 0 , which is GPT2 but without any MLP layer.

Experimental setups. Throughout this section, when presenting positive result (such as for GPT2) we try to stick to one fixed set of learning rate choices; but when presenting a negative result (such as for the LLaMA architecture), we present the best among three learning rate choices.

### B.1 1000-Exposure Setting

In the 1000-exposure setting, we observe that the model architecture choices have a negligible impact on the scaling laws. The results for LLaMA, Mistral, GPT2 0 , and GPT2 1/4 architectures are presented in Figure 3 , with their parameter choices discussed below.

###### Parameter 6 ( Figure 3 ) .

In the 1000-exposure setting, for LLaMA/Mistral models we use similar parameters as specified in Parameter 1 , but we select the best of three learning rates to better demonstrate that GPT2 performs no worse than even the best tuned LLaMA/Mistral models: • For N = 10 ​ K N=10K , we use w ​ d = 0.02 wd=0.02 , l ​ r = 0.0005 / 0.001 / 0.002 lr=0.0005/0.001/0.002 , and batch size 24 with fp16;

• For N = 20 ​ K N=20K , we use w ​ d = 0.02 wd=0.02 , l ​ r = 0.0005 / 0.001 / 0.002 lr=0.0005/0.001/0.002 , and batch size 48 with fp16;

• For N = 50 ​ K N=50K , we use w ​ d = 0.02 wd=0.02 , l ​ r = 0.0005 / 0.001 / 0.002 lr=0.0005/0.001/0.002 , and batch size 96 with fp16;

• For N = 100 ​ K , 200 ​ K N=100K,200K , we use w ​ d = 0.02 wd=0.02 , l ​ r = 0.0005 / 0.001 / 0.002 lr=0.0005/0.001/0.002 , and batch size 192 with fp16;

• For N = 500 ​ K , 1 ​ M N=500K,1M , we use w ​ d = 0.01 wd=0.01 , l ​ r = 0.0002 / 0.0003 / 0.0005 lr=0.0002/0.0003/0.0005 , and batch size 192 with fp16;

• For N = 2 ​ M N=2M , we use w ​ d = 0.005 wd=0.005 , l ​ r = 0.0003 / 0.0005 / 0.001 lr=0.0003/0.0005/0.001 , and batch size 1536 1536 with bf16;

• For N = 5 ​ M N=5M , we use w ​ d = 0.002 wd=0.002 , l ​ r = 0.0003 / 0.0005 / 0.001 lr=0.0003/0.0005/0.001 , and batch size 1536 1536 with bf16;

• For N = 10 ​ M N=10M , we use w ​ d = 0.001 wd=0.001 , l ​ r = 0.0003 / 0.0005 / 0.001 lr=0.0003/0.0005/0.001 , and batch size 1536 1536 with bf16.

For GPT2 0 and GPT2 1/4 , we use the same learning rates as specified in Parameter 1 .

###### Remark B.1 (bf16 on gated MLP) .

As discussed in Section B.2 , the training of LLaMA and Mistral architectures is less stable due to the use of GatedMLP, leading to the necessity of switching to (mixed-precision) bf16 training when required.

From Figure 3 , it is evident that, except for tiny models, LLaMA, Mistral, GPT2 0 , and GPT2 1/4 architectures closely follow GPT2’s scaling law over 1000 exposures. For tiny models with ≤ 10 ​ M \leq 10M parameters, tying model weights increases their capacity (refer to Figure 3(c) ). This indicates that the 2bit/param capacity ratio is a relatively universal law among most typical (decoder-only) language model architectures.

### B.2 100-Exposure Setting

The 100-exposure setting reveals more intriguing comparisons. We contrast GPT2 with various model architectures in Figure 4 and offer a detailed comparison between LLaMA and GPT2 architectures in Figure 5 .

Figure 4(b) shows that the LLaMA architecture may lag behind GPT2’s scaling law by a factor of 1.3x, even for larger models.

We delve into the reasons behind this. By adjusting LLaMA’s architecture (e.g., switching GatedMLP back to normal MLP), as shown in Figure 5 , we find that replacing LLaMA’s GatedMLP with a standard MLP is necessary to match GPT2’s scaling law. Notably, for a strong comparison, when using GatedMLP we select the best result from three learning rates, whereas for a standard MLP, akin to GPT2, we use a single learning rate. For smaller models, matching GPT2 requires tying model weights and adopting GPT2’s tokenizer, though this is less significant. 26 26 26 The influence of the tokenizer on model capacity is noteworthy. For instance, LLaMA/Mistral tokenizers tend to split birthday years into single-digit tokens, slightly slowing the training of smaller models, whereas the GPT2Tokenizer uses a single token for the birth years such as 1991.

For other model architectures, Mistral, GPT2 0 , and GPT2 1/4 , their scaling laws in the 100-exposure setting are presented in Figure 4 . Figure 4(c) confirms that the Mistral architecture also underperforms GPT2 due to its use of gated MLP. Figure 4(d) reveals that reducing GPT2 1/4 ’s MLP layer size by a quarter has a negligible impact on model capacity. However, removing the MLP layers entirely in GPT2 0 significantly reduces the model’s capacity, see Figure 4(e) .

The 100-exposure setting represents an “insufficient training” paradigm. Thus, the comparisons are not about one architecture being strictly worse than another (as they achieve similar capacity ratios in a 1000-exposure setting, as shown in Figure 3 ). Our findings indicate that some architectures are noticeably easier to train (thus learn knowledge faster) : • The GatedMLP architecture slows down the model’s learning speed, and we observe less stable training with its use. 27 27 27 For example, mixed-precision fp16 training can sometimes fail for LLaMA/Mistral models smaller than 100M; hence, we use mixed-precision bf16 instead. Conversely, GPT2 models up to 1B can be trained with fp16.

• Removing MLP layers entirely slows down the model’s learning speed, whereas adjusting the size of MLP layers (e.g., from 8 ​ d 2 8d^{2} to 10.5 ​ d 2 10.5d^{2} or down to 2 ​ d 2 2d^{2} ) may not have a significant impact.

Additionally, we experimented with enabling trainable biases in LLaMA’s layernorms and switching from s ​ i ​ l ​ u silu to g ​ e ​ l ​ u gelu (to more closely resemble GPT2), in a similar way as Figure 5 , but found these changes do not affect the model’s capacities. We ignore those experiments for clarity.

Below, we discuss our parameter choices for the experiments in Figure 4 and Figure 5 .

###### Parameter 7 ( Figure 4 ) .

In the 100-exposure setting, (a) For LLaMA/Mistral models on bioS ​ ( N ) \textsf{bioS}(N) data, aiming to present negative results, we select the best learning rate from three options in each data setting: • For N = 50 ​ K N=50K , we use w ​ d = 0.01 wd=0.01 , l ​ r = 0.0003 / 0.0005 / 0.001 lr=0.0003/0.0005/0.001 , and batch size 12 with bf16;

• For N = 100 ​ K N=100K , we use w ​ d = 0.01 wd=0.01 , l ​ r = 0.0003 / 0.0005 / 0.001 lr=0.0003/0.0005/0.001 , and batch size 24 with bf16;

• For N = 200 ​ K N=200K , we use w ​ d = 0.01 wd=0.01 , l ​ r = 0.0003 / 0.0005 / 0.001 lr=0.0003/0.0005/0.001 , and batch size 48 with bf16;

• For N = 500 ​ K N=500K , we use w ​ d = 0.01 wd=0.01 , l ​ r = 0.0002 / 0.0003 / 0.0005 lr=0.0002/0.0003/0.0005 , and batch size 96 with bf16;

• For N = 1 ​ M N=1M , we use w ​ d = 0.01 wd=0.01 , l ​ r = 0.0002 / 0.0003 / 0.0005 lr=0.0002/0.0003/0.0005 , and batch size 192 with bf16;

• For N = 2 ​ M N=2M , we use w ​ d = 0.01 wd=0.01 , l ​ r = 0.0003 / 0.0005 / 0.001 lr=0.0003/0.0005/0.001 , and batch size 384 384 with bf16;

• For N = 5 ​ M N=5M , we use w ​ d = 0.01 wd=0.01 , l ​ r = 0.0003 / 0.0005 / 0.001 lr=0.0003/0.0005/0.001 , and batch size 768 768 with bf16;

• For N = 10 ​ M N=10M , we use w ​ d = 0.01 wd=0.01 , l ​ r = 0.0003 / 0.0005 / 0.001 lr=0.0003/0.0005/0.001 , and batch size 1536 1536 with bf16;

• For N = 20 ​ M N=20M , we use w ​ d = 0.002 wd=0.002 , l ​ r = 0.0003 / 0.0005 / 0.001 lr=0.0003/0.0005/0.001 , and batch size 1536 1536 with bf16.

(For N ≤ 1 ​ M N\leq 1M , we also tested the same settings with fp16, finding similar results. However, LLaMA/Mistral models tend to fail more often with fp16, so we primarily used bf16.)

(b) For GPT2 1/4 : • For N = 50 ​ K N=50K , we use w ​ d = 0.01 wd=0.01 , l ​ r = 0.0005 / 0.001 lr=0.0005/0.001 , and batch size 12 with fp16;

• For N = 100 ​ K N=100K , we use w ​ d = 0.01 wd=0.01 , l ​ r = 0.0005 / 0.001 lr=0.0005/0.001 , and batch size 24 with fp16;

• For N = 200 ​ K N=200K , we use w ​ d = 0.01 wd=0.01 , l ​ r = 0.0005 / 0.001 lr=0.0005/0.001 , and batch size 48 with fp16;

• For N = 500 ​ K N=500K , we use w ​ d = 0.01 wd=0.01 , l ​ r = 0.0003 / 0.0005 lr=0.0003/0.0005 , and batch size 96 with fp16;

• For N = 1 ​ M N=1M , we use w ​ d = 0.01 wd=0.01 , l ​ r = 0.0003 / 0.0005 lr=0.0003/0.0005 , and batch size 192 with fp16.

(c) For GPT2 0 , to present a negative result, we use the same settings as in Parameter fig:other-models:100(a) : • For N = 50 ​ K N=50K , we use w ​ d = 0.01 wd=0.01 , l ​ r = 0.0003 / 0.0005 / 0.001 lr=0.0003/0.0005/0.001 , and batch size 12 with bf16;

• For N = 100 ​ K N=100K , we use w ​ d = 0.01 wd=0.01 , l ​ r = 0.0003 / 0.0005 / 0.001 lr=0.0003/0.0005/0.001 , and batch size 24 with bf16;

• For N = 200 ​ K N=200K , we use w ​ d = 0.01 wd=0.01 , l ​ r = 0.0003 / 0.0005 / 0.001 lr=0.0003/0.0005/0.001 , and batch size 48 with bf16;

• For N = 500 ​ K N=500K , we use w ​ d = 0.01 wd=0.01 , l ​ r = 0.0002 / 0.0003 / 0.0005 lr=0.0002/0.0003/0.0005 , and batch size 96 with bf16;

• For N = 1 ​ M N=1M , we use w ​ d = 0.01 wd=0.01 , l ​ r = 0.0002 / 0.0003 / 0.0005 lr=0.0002/0.0003/0.0005 , and batch size 192 with bf16.

###### Parameter 8 ( Figure 5 ) .

In the 100-exposure controlled comparison experiment, • For presenting negative results ( Figure 5(a) and Figure 5(c) ), we select the best learning rate from three options, identical to GPT2 0 in Parameter fig:other-models:100(c) .

• For presenting positive results ( Figure 5(b) and Figure 5(d) ), we use a single set of learning rates, identical to Parameter 2 but with fp16 replaced by bf16 for a stronger comparison.

## Appendix C More on Quantization

We use the auto_gptq package (based on [ 10 ] ) to quantize the GPT2 model results in Figure 1 for the bioS data and the GPT2 model results in Figure 2 for the bioD data. We simply use a small set of 1000 people’s biographies to perform the quantization task. Our results are presented in Figure 14 for the bioS data and in Figure 15 for the bioD data.

## Appendix D More on Mixture of Experts

We utilize the tutel package for implementing Mixture-of-Experts (MoE) on GPT2 models [ 18 ] . In MoE, the parameter t ​ o ​ p ​ k topk determines the number of experts each token is routed to. It is recommended by some practitioners to use t ​ o ​ p ​ k = 2 topk=2 during training and t ​ o ​ p ​ k = 1 topk=1 during testing. Additionally, the c ​ a ​ p ​ _ ​ f ​ a ​ c ​ t ​ o ​ r cap\_factor parameter ensures that, given M M experts, each expert receives no more than c ​ a ​ p ​ _ ​ f ​ a ​ c ​ t ​ o ​ r M \frac{cap\_factor}{M} fraction of the data.

Using t ​ o ​ p ​ k = 1 topk=1 and c ​ a ​ p ​ _ ​ f ​ a ​ c ​ t ​ o ​ r = 1 cap\_factor=1 is generally not advisable. Thus, to provide the strongest result, we set t ​ o ​ p ​ k = 1 , c ​ a ​ p ​ _ ​ f ​ a ​ c ​ t ​ o ​ r = 2 topk=1,cap\_factor=2 for the 1000/100-exposure scaling laws in Figure 16 . (During testing, we increase the capacity factor to c ​ a ​ p ​ _ ​ f ​ a ​ c ​ t ​ o ​ r = 8 cap\_factor=8 .)

For the 100-exposure scaling law, we additionally compare three configurations: ( t ​ o ​ p ​ k , c ​ a ​ p ​ _ ​ f ​ a ​ c ​ t ​ o ​ r ) = ( 1 , 2 ) , ( 2 , 1 ) , ( 2 , 2 ) (topk,cap\_factor)=(1,2),(2,1),(2,2) , finding minimal differences among them as shown in Figure 17 . Remember from Section 7 that differences in model architecture usually become apparent in the insufficient training regime; this is why we opt for 100-exposure instead of 1000-exposure. Notably, ( t ​ o ​ p ​ k , c ​ a ​ p ​ _ ​ f ​ a ​ c ​ t ​ o ​ r ) = ( 2 , 2 ) (topk,cap\_factor)=(2,2) performs best (among the three) for deep models, such as GPT2-16-4 with 32 experts.

Due to their sparsity, MoE models often require higher learning rates compared to dense models. Consequently, we adjust the optimizer parameters as follows:

###### Parameter 9 ( Figure 16 , Figure 17 ) .

In the 1000-exposure setting for GPT2-MoE models with 32 experts, we slightly increase the learning rates while keeping other parameters nearly identical to Parameter 1 : • For N = 10 ​ K N=10K , we use w ​ d = 0.02 wd=0.02 , l ​ r = 0.001 / 0.002 lr=0.001/0.002 , and batch size 24 with fp16;

• For N = 20 ​ K N=20K , we use w ​ d = 0.02 wd=0.02 , l ​ r = 0.001 / 0.002 lr=0.001/0.002 , and batch size 48 with fp16;

• For N = 50 ​ K N=50K , we use w ​ d = 0.02 wd=0.02 , l ​ r = 0.001 / 0.002 lr=0.001/0.002 , and batch size 96 with fp16;

• For N = 100 ​ K , 200 ​ K N=100K,200K , we use w ​ d = 0.02 wd=0.02 , l ​ r = 0.001 / 0.002 lr=0.001/0.002 , batch size 192 with fp16;

• For N = 500 ​ K , 1 ​ M N=500K,1M , we use w ​ d = 0.01 wd=0.01 , l ​ r = 0.0005 / 0.001 lr=0.0005/0.001 , batch size 192 with fp16;

• For N = 2 ​ M N=2M , we use w ​ d = 0.005 wd=0.005 , l ​ r = 0.002 lr=0.002 , and batch size 1536 1536 with fp16;

• For N = 5 ​ M N=5M , we use w ​ d = 0.002 wd=0.002 , l ​ r = 0.0005 lr=0.0005 , and batch size 1536 1536 with fp16;

• For N = 10 ​ M N=10M , we use w ​ d = 0.001 wd=0.001 , l ​ r = 0.0005 lr=0.0005 , and batch size 1536 1536 with fp16.

In the 100-exposure setting, we also use higher learning rates compared to Parameter 2 :

• For N = 50 ​ K N=50K , we use w ​ d = 0.01 wd=0.01 , l ​ r = 0.001 / 0.002 / 0.005 lr=0.001/0.002/0.005 , and batch size 12 with fp16;

• For N = 100 ​ K N=100K , we use w ​ d = 0.01 wd=0.01 , l ​ r = 0.001 / 0.002 / 0.005 lr=0.001/0.002/0.005 , and batch size 24 with fp16;

• For N = 200 ​ K N=200K , we use w ​ d = 0.01 wd=0.01 , l ​ r = 0.001 / 0.002 / 0.005 lr=0.001/0.002/0.005 , and batch size 48 with fp16;

• For N = 500 ​ K N=500K , we use w ​ d = 0.01 wd=0.01 , l ​ r = 0.001 / 0.002 lr=0.001/0.002 , and batch size 96 with fp16;

• For N = 1 ​ M N=1M , we use w ​ d = 0.01 wd=0.01 , l ​ r = 0.0005 / 0.001 / 0.002 lr=0.0005/0.001/0.002 , and batch size 192 with fp16;

• For N = 2 ​ M N=2M , we use w ​ d = 0.005 wd=0.005 , l ​ r = 0.0005 / 0.001 lr=0.0005/0.001 , and batch size 192 192 with fp16;

• For N = 5 ​ M N=5M , we use w ​ d = 0.005 wd=0.005 , l ​ r = 0.0003 / 0.0005 / 0.001 lr=0.0003/0.0005/0.001 , and batch size 384 384 with fp16.

## Appendix E More on Junk Data vs. Scaling Laws

Recall from Section 10 that our dataset is a mixture, with 1/8 of the tokens coming from bioS ​ ( N ) \textsf{bioS}(N) for various N N (referred to as “useful data”), and the remaining 7/8 from “junk data.” We explored three scenarios: (a) Junk data being bioS ​ ( N ′ ) \textsf{bioS}(N^{\prime}) for N ′ = 100 ​ M N^{\prime}=100M , representing completely random junk;

(b) Junk data being bioS ​ ( N ′ ) \textsf{bioS}(N^{\prime}) for N ′ = 1 ​ K N^{\prime}=1K , representing highly repetitive data; and

(c) Junk data being bioS ​ ( N ′ ) \textsf{bioS}(N^{\prime}) for N ′ = 100 ​ M N^{\prime}=100M , but with a special token appended to the front of each piece of useful data . 28 28 28 This is akin to adding a domain name like wikipedia.org at the beginning of the data; the model lacks prior knowledge that these special token data signify high-quality, useful data. It’s up to the model and the training process to autonomously discover this.

For simplicity, within each 512-token context window, we either include only useful data or only junk data (separated by <EOS> tokens). The outcomes are similar when mixing useful and junk data in the same context window. In all three cases, we initially consider a 100-exposure training setting where the useful data receive 100 exposures each during pretraining — thus, the total number of training tokens is approximately 8 times more than in Figure 1(b) (our scaling law for the 100-exposure case without junk data).

In case (A), presenting a negative result , we also explore 300-exposure, 600-exposure, and 1000-exposure training settings. Given that the 1000-exposure setting requires 48x more training tokens compared to Figure 1(b) , or 4.8x more compared to Figure 1(a) , we limited experiments to bioS ​ ( N ) \textsf{bioS}(N) with N ≤ 200 ​ K N\leq 200K to conserve computational resources. Similarly, for 300-exposure and 600-exposure, we only considered N ≤ 500 ​ K N\leq 500K .

In case (B), presenting a positive result , we limited our consideration to 100-exposure with N ≤ 1 ​ M N\leq 1M .

In case (C), presenting a moderately positive result , we explored both 100-exposure and 300-exposure settings, where, in the 300-exposure setting, we again limited to N ≤ 500 ​ K N\leq 500K .

Overall, due to the significantly different training durations (i.e., number of training tokens) across the 100-, 300-, 600-, and 1000-exposure settings, we had to adjust their batch sizes, weight decay, and learning rates accordingly. These adjustments are discussed below.

###### Parameter 10 ( Figure 8 ) .

We adhere to the general advice provided in Remark A.2 for selecting parameters in all experiments shown in Figure 8 . For negative results (e.g., Figure 8(b) , 8(c) ), we opted for a smaller batch size to increase the number of trainable steps and explored a wider range of learning rate options. Conversely, for positive results (e.g., Figure 8(f) , 8(e) ), we sometimes chose a larger batch size to benefit from faster, GPU-accelerated training times and considered a narrower set of learning rate choices. Overall, we have meticulously selected parameters to strengthen negative results as much as possible while intentionally not optimizing positive results to the same extent. This approach ensures a stronger comparison and effectively communicates the key message of this section. Specifically,

• For Figure 8(b) which is Case (a) of 100-exposure: – For N = 50 ​ K N=50K , we use w ​ d = 0.01 wd=0.01 , l ​ r = 0.0003 / 0.0005 / 0.001 lr=0.0003/0.0005/0.001 , and batch size 12;

– For N = 100 ​ K N=100K , we use w ​ d = 0.01 wd=0.01 , l ​ r = 0.0003 / 0.0005 / 0.001 lr=0.0003/0.0005/0.001 , and batch size 24;

– For N = 200 ​ K N=200K , we use w ​ d = 0.01 wd=0.01 , l ​ r = 0.0003 / 0.0005 / 0.001 lr=0.0003/0.0005/0.001 , and batch size 48;

– For N = 500 ​ K N=500K , we use w ​ d = 0.005 wd=0.005 , l ​ r = 0.00005 / 0.0001 / 0.0002 / 0.0003 / 0.0005 lr=0.00005/0.0001/0.0002/0.0003/0.0005 , and batch size 192;

– For N = 1 ​ M N=1M , we use w ​ d = 0.005 wd=0.005 , l ​ r = 0.00005 / 0.0001 / 0.0002 / 0.0003 / 0.0005 lr=0.00005/0.0001/0.0002/0.0003/0.0005 , and batch size 192.

• For Figure 8(c) which is Case (a) of 300-exposure: – For N = 50 ​ K N=50K , we use w ​ d = 0.01 wd=0.01 , l ​ r = 0.0003 / 0.0005 / 0.001 lr=0.0003/0.0005/0.001 , and batch size 96;

– For N = 100 ​ K N=100K , we use w ​ d = 0.01 wd=0.01 , l ​ r = 0.0003 / 0.0005 / 0.001 lr=0.0003/0.0005/0.001 , and batch size 192;

– For N = 200 ​ K N=200K , we use w ​ d = 0.01 wd=0.01 , l ​ r = 0.0003 / 0.0005 / 0.001 lr=0.0003/0.0005/0.001 , and batch size 192;

– For N = 500 ​ K N=500K , we use w ​ d = 0.01 wd=0.01 , l ​ r = 0.0003 / 0.0005 / 0.001 lr=0.0003/0.0005/0.001 , and batch size 192.

• For Figure 8(d) which is Case (a) of 600-exposure: – For N = 50 ​ K N=50K , we use w ​ d = 0.01 wd=0.01 , l ​ r = 0.0003 / 0.0005 / 0.001 lr=0.0003/0.0005/0.001 , and batch size 384;

– For N = 100 ​ K N=100K , we use w ​ d = 0.01 wd=0.01 , l ​ r = 0.0003 / 0.0005 / 0.001 lr=0.0003/0.0005/0.001 , and batch size 384;

– For N = 200 ​ K N=200K , we use w ​ d = 0.01 wd=0.01 , l ​ r = 0.0003 / 0.0005 / 0.001 lr=0.0003/0.0005/0.001 , and batch size 384;

– For N = 500 ​ K N=500K , we use w ​ d = 0.002 wd=0.002 , l ​ r = 0.0003 / 0.0005 / 0.001 lr=0.0003/0.0005/0.001 , and batch size 768.

• For Figure 8(e) which is Case (a) of 1000-exposure: – For N = 50 ​ K N=50K , we use w ​ d = 0.01 wd=0.01 , l ​ r = 0.0005 / 0.001 lr=0.0005/0.001 , and batch size 384;

– For N = 100 ​ K N=100K , we use w ​ d = 0.01 wd=0.01 , l ​ r = 0.0005 / 0.001 lr=0.0005/0.001 , and batch size 768;

– For N = 200 ​ K N=200K , we use w ​ d = 0.01 wd=0.01 , l ​ r = 0.0005 / 0.001 lr=0.0005/0.001 , and batch size 1536.

• For Figure 8(f) which is Case (b) of 100-exposure: – For N = 50 ​ K N=50K , we use w ​ d = 0.01 wd=0.01 , l ​ r = 0.0003 / 0.0005 lr=0.0003/0.0005 , and batch size 12;

– For N = 100 ​ K N=100K , we use w ​ d = 0.01 wd=0.01 , l ​ r = 0.0003 / 0.0005 lr=0.0003/0.0005 , and batch size 24;

– For N = 200 ​ K N=200K , we use w ​ d = 0.01 wd=0.01 , l ​ r = 0.0003 / 0.0005 / 0.001 lr=0.0003/0.0005/0.001 , and batch size 96;

– For N = 500 ​ K N=500K , we use w ​ d = 0.01 wd=0.01 , l ​ r = 0.0003 / 0.0005 lr=0.0003/0.0005 , and batch size 192;

– For N = 1 ​ M N=1M , we use w ​ d = 0.01 wd=0.01 , l ​ r = 0.0003 lr=0.0003 , and batch size 192.

• For Figure 8(g) which is Case (c) of 100-exposure: – For N = 50 ​ K N=50K , we use w ​ d = 0.01 wd=0.01 , l ​ r = 0.0003 / 0.0005 / 0.001 lr=0.0003/0.0005/0.001 , and batch size 12;

– For N = 100 ​ K N=100K , we use w ​ d = 0.01 wd=0.01 , l ​ r = 0.0003 / 0.0005 / 0.001 lr=0.0003/0.0005/0.001 , and batch size 24;

– For N = 200 ​ K N=200K , we use w ​ d = 0.01 wd=0.01 , l ​ r = 0.0002 / 0.0003 / 0.0005 / 0.001 lr=0.0002/0.0003/0.0005/0.001 , and batch size 96;

– For N = 500 ​ K N=500K , we use w ​ d = 0.005 wd=0.005 , l ​ r = 0.0002 / 0.0003 / 0.0005 lr=0.0002/0.0003/0.0005 , and batch size 192;

– For N = 1 ​ M N=1M , we use w ​ d = 0.005 wd=0.005 , l ​ r = 0.0002 / 0.0003 / 0.0005 lr=0.0002/0.0003/0.0005 , and batch size 192.

• For Figure 8(h) which is Case (c) of 300-exposure: – For N = 50 ​ K N=50K , we use w ​ d = 0.01 wd=0.01 , l ​ r = 0.0003 / 0.0005 / 0.001 lr=0.0003/0.0005/0.001 , and batch size 96;

– For N = 100 ​ K N=100K , we use w ​ d = 0.01 wd=0.01 , l ​ r = 0.0003 / 0.0005 / 0.001 lr=0.0003/0.0005/0.001 , and batch size 192;

– For N = 200 ​ K N=200K , we use w ​ d = 0.01 wd=0.01 , l ​ r = 0.0003 / 0.0005 / 0.001 lr=0.0003/0.0005/0.001 , and batch size 192;

– For N = 500 ​ K N=500K , we use w ​ d = 0.005 wd=0.005 , l ​ r = 0.0003 / 0.0005 / 0.001 lr=0.0003/0.0005/0.001 , and batch size 384.

## Appendix F Proof of Theorem 3.2

We present a crucial lemma that establishes the bit complexity required to encode random variables based on the probability that these variables match specific reference values.

###### Lemma F.1 .

Let 𝒬 1 , … , 𝒬 k \mathcal{Q}_{1},\dots,\mathcal{Q}_{k} be fixed sets (we call domains ), and assume that for each i ∈ [ k ] i\in[k] , Q i Q_{i} is independently and randomly chosen from its corresponding domain 𝒬 i \mathcal{Q}_{i} . Denote Q = ( Q 1 , … , Q k ) Q=(Q_{1},\dots,Q_{k}) and view Q Q as the training data .

Assume there exists a function W ⁡ ( Q ) ∈ 𝒲 W(Q)\in\mathcal{W} , which we regard as the parameters of a model computed (i.e., trained) from the training data Q Q .

Furthermore, consider an evaluation function F i F_{i} that predicts ∀ i ∈ [ k ] : P i = F i ( W ( Q ) , Q 1 , Q 2 , ⋯ , Q i − 1 , R ) with p i ( Q ) = def 𝐏𝐫 R [ P i = Q i ∣ Q ] . \forall i\in[k]\colon\hskip 20.00003ptP_{i}=F_{i}(W(Q),Q_{1},Q_{2},\cdots,Q_{i-1},R)\hskip 10.00002pt\text{with }\hskip 10.00002ptp_{i}(Q)\stackrel{{\scriptstyle\mathrm{\scriptscriptstyle def}}}{{=}}\operatornamewithlimits{\mathbf{Pr}}_{R}[P_{i}=Q_{i}\mid Q]\kern 5.0pt. Here, F F is parameterized by W ⁡ ( Q ) W(Q) and may rely on previous data Q 1 , … , Q i − 1 Q_{1},\dots,Q_{i-1} , and new randomness R R . Then, it follows that log ⁡ | 𝒲 | ≥ ∑ i ∈ [ k ] log ⁡ ( 𝔼 Q [ p i ​ ( Q ) ] × | 𝒬 i | ) ≥ 𝔼 Q [ ∑ i ∈ [ k ] log ⁡ ( p i ​ ( Q ) × | 𝒬 i | ) ] . \displaystyle\log|\mathcal{W}|\geq\sum_{i\in[k]}\log\big(\operatornamewithlimits{\mathbb{E}}_{Q}[p_{i}(Q)]\times|\mathcal{Q}_{i}|\big)\geq\operatornamewithlimits{\mathbb{E}}_{Q}\Big[\sum_{i\in[k]}\log\big(p_{i}(Q)\times|\mathcal{Q}_{i}|\big)\Big]\kern 5.0pt. (F.1)

###### Proof of Lemma F.1 .

Since the second inequality of ( F.1 ) trivially comes from Jensen’s inequality, we only prove the first one.

When i = 1 i=1 , we have P 1 = F 1 ​ ( W ⁡ ( Q ) , R ) P_{1}=F_{1}(W(Q),R) and one can prove the lemma by a simple counting argument, using the property that ∀ R \forall R , P 1 = F 1 ​ ( W ⁡ ( Q ) , R ) P_{1}=F_{1}(W(Q),R) has at most | 𝒲 | |\mathcal{W}| choices of values.

When i ≥ 2 i\geq 2 , we can merge data points Q 1 , Q 2 Q_{1},Q_{2} to be a new data point Q ′ Q^{\prime} with domain 𝒬 ′ = 𝒬 1 × 𝒬 2 \mathcal{Q}^{\prime}=\mathcal{Q}_{1}\times\mathcal{Q}_{2} . We can construct P ′ = ( P 1 , P 2 ) P^{\prime}=(P_{1},P_{2}) from function F 1 , F 2 F_{1},F_{2} by sampling R 1 R_{1} to generate P 1 = F 1 ​ ( W ⁡ ( Q ) , R ) P_{1}=F_{1}(W(Q),R) , and then sample independent R 2 R_{2} to generate P 2 = F 2 ​ ( W ⁡ ( Q ) , Q 1 , R ) P_{2}=F_{2}(W(Q),Q_{1},R) . We know that 𝐏𝐫 R 1 , R 2 [ P ′ = Q ′ ∣ Q ] = 𝐏𝐫 R 1 [ P 1 = Q 1 ∣ Q ] ​ 𝐏𝐫 R 2 [ P 2 = Q 2 ∣ Q ] = p 1 ​ ( Q ) ⋅ p 2 ​ ( Q ) \operatornamewithlimits{\mathbf{Pr}}_{R_{1},R_{2}}[P^{\prime}=Q^{\prime}\mid Q]=\operatornamewithlimits{\mathbf{Pr}}_{R_{1}}[P_{1}=Q_{1}\mid Q]\operatornamewithlimits{\mathbf{Pr}}_{R_{2}}[P_{2}=Q_{2}\mid Q]=p_{1}(Q)\cdot p_{2}(Q) . The lemma now follows using the following identity: log ⁡ ( p 1 ​ ( Q ) ​ | 𝒬 1 | ) + log ⁡ ( p 2 ​ ( Q ) ​ | 𝒬 2 | ) = log ⁡ ( p 1 ​ ( Q ) ​ p 2 ​ ( Q ) ​ | 𝒬 1 | ​ | 𝒬 2 | ) . ∎ \log(p_{1}(Q)|\mathcal{Q}_{1}|)+\log(p_{2}(Q)|\mathcal{Q}_{2}|)=\log(p_{1}(Q)p_{2}(Q)|\mathcal{Q}_{1}||\mathcal{Q}_{2}|)\kern 5.0pt.\qed

### F.1 Warmup Examples

Let us first see two warmup applications of Lemma F.1 .

Value-only. Let g 1 , … , g N ∈ [ T ] g_{1},\dots,g_{N}\in[T] , where each g i g_{i} is i.i.d. uniformly chosen at random from [ T ] [T] . Think of these as values . Suppose a model, parameterized by W W , is trained on the training data 𝒵 = ( g 1 , … , g N ) \mathcal{Z}=\big(g_{1},...,g_{N}\big) . Assume this model, for a given index i ∈ [ N ] i\in[N] , can generate a random prediction f i f_{i} corresponding to g i g_{i} . We can represent this model as f i ​ ( W ​ ( 𝒵 ) , R ) f_{i}(W(\mathcal{Z}),R) , where R R denotes the randomness. The cross-entropy loss for this scenario (averaged over all possible training data) is expressed as 𝐥𝐨𝐬𝐬 = def 𝔼 g [ 𝐥𝐨𝐬𝐬 ( g ) ] = def 𝔼 g [ 1 N ∑ i ∈ [ N ] − log 𝐏𝐫 f i [ f i = g i ] ] ≥ 0 \mathbf{loss}\stackrel{{\scriptstyle\mathrm{\scriptscriptstyle def}}}{{=}}\operatornamewithlimits{\mathbb{E}}_{g}[\mathbf{loss}(g)]\stackrel{{\scriptstyle\mathrm{\scriptscriptstyle def}}}{{=}}\operatornamewithlimits{\mathbb{E}}_{g}\Big[\frac{1}{N}\sum_{i\in[N]}-\log\operatornamewithlimits{\mathbf{Pr}}_{f_{i}}[f_{i}=g_{i}]\Big]\geq 0 Now we apply Lemma F.1 by setting 𝒬 1 = … ​ 𝒬 N = [ T ] \mathcal{Q}_{1}=...\mathcal{Q}_{N}=[T] , Q i = g i Q_{i}=g_{i} , and P i = f i P_{i}=f_{i} . We have log | 𝒲 | ≥ 𝔼 g [ ∑ i ∈ [ N ] log 𝐏𝐫 f i [ f i = g i ] + log T ] = N log T − N 𝔼 g 𝐥𝐨𝐬𝐬 ( g ) = 𝔼 g N log T e 𝐥𝐨𝐬𝐬 ⁡ ( g ) . \displaystyle\log|\mathcal{W}|\geq\operatornamewithlimits{\mathbb{E}}_{g}\Big[\sum_{i\in[N]}\log\operatornamewithlimits{\mathbf{Pr}}_{f_{i}}[f_{i}=g_{i}]+\log T\Big]=N\log T-N\operatornamewithlimits{\mathbb{E}}_{g}\mathbf{loss}(g)=\operatornamewithlimits{\mathbb{E}}_{g}N\log\frac{T}{e^{\mathbf{loss}(g)}}\kern 5.0pt. Changing the base immediately yields a bit complexity lower bound of log 2 ⁡ | 𝒲 | ≥ N ​ log 2 ​ T e 𝐥𝐨𝐬𝐬 \log_{2}|\mathcal{W}|\geq N\log_{2}\frac{T}{e^{\mathbf{loss}}} . As the loss approaches zero, this matches the bit complexity upper bound.

Name-only. Let g 1 , … , g N ∈ [ N 0 ] g_{1},\dots,g_{N}\in[N_{0}] be N N distinct elements from [ N 0 ] [N_{0}] , sampled uniformly at random without replacement, and considered as names . Suppose a model f f , parameterized by W W , is trained on the dataset 𝒵 = ( g 1 , … , g N ) \mathcal{Z}=\big(g_{1},\dots,g_{N}\big) to predict a name. We denote this as f ⁡ ( W ⁡ ( 𝒵 ) , R ) f(W(\mathcal{Z}),R) , where R R represents randomness. The cross-entropy loss for this scenario is defined as 𝐥𝐨𝐬𝐬 = def 𝔼 g [ 𝐥𝐨𝐬𝐬 ( g ) ] = def 𝔼 g [ 1 N ∑ i ∈ [ N ] − log 𝐏𝐫 f [ f = g i ] ] ≥ 0 \mathbf{loss}\stackrel{{\scriptstyle\mathrm{\scriptscriptstyle def}}}{{=}}\operatornamewithlimits{\mathbb{E}}_{g}[\mathbf{loss}(g)]\stackrel{{\scriptstyle\mathrm{\scriptscriptstyle def}}}{{=}}\operatornamewithlimits{\mathbb{E}}_{g}\Big[\frac{1}{N}\sum_{i\in[N]}-\log\operatornamewithlimits{\mathbf{Pr}}_{f}[f=g_{i}]\Big]\geq 0

To apply Lemma F.1 , we define 𝒬 1 = [ N 0 ] \mathcal{Q}_{1}=[N_{0}] , 𝒬 2 = [ N 0 − 1 ] \mathcal{Q}_{2}=[N_{0}-1] , and continue until 𝒬 N = [ N 0 − N + 1 ] \mathcal{Q}_{N}=[N_{0}-N+1] . After uniformly randomly generating Q 1 , … , Q N Q_{1},\dots,Q_{N} from 𝒬 1 , … , 𝒬 N \mathcal{Q}_{1},\dots,\mathcal{Q}_{N} , we construct ( g 1 , … , g N ) ∈ [ N ] N (g_{1},\dots,g_{N})\in[N]^{N} as follows: set g 1 = Q 1 g_{1}=Q_{1} ; for g 2 g_{2} , set it to Q 2 Q_{2} if Q 2 < Q 1 Q_{2}<Q_{1} , otherwise g 2 = Q 2 + 1 g_{2}=Q_{2}+1 ; and in general, define g i g_{i} as the Q i Q_{i} -th smallest element in [ N 0 ] ∖ { g 1 , … , g i − 1 } [N_{0}]\setminus\{g_{1},\dots,g_{i-1}\} . This method provides an alternative way to generate 𝒵 = ( g 1 , … , g N ) \mathcal{Z}=(g_{1},\dots,g_{N}) , denoted as 𝒵 ⁡ ( Q ) \mathcal{Z}(Q) . For each i ∈ [ N ] i\in[N] , we define P i P_{i} as follows: first, generate f = f ⁡ ( 𝒲 ⁡ ( 𝒵 ) , R i ) f=f(\mathcal{W}(\mathcal{Z}),R_{i}) using fresh randomness R i R_{i} . Set P i = def s P_{i}\stackrel{{\scriptstyle\mathrm{\scriptscriptstyle def}}}{{=}}s if f f is the s s -th smallest element in [ N 0 ] ∖ { g 1 , … , g i − 1 } [N_{0}]\setminus\{g_{1},\dots,g_{i-1}\} , or a special symbol such as ∅ \varnothing if f f is among { g 1 , … , g i − 1 } \{g_{1},\dots,g_{i-1}\} . ( Note importantly , this definition of P i P_{i} necessitates knowledge of g 1 , … , g i − 1 g_{1},\dots,g_{i-1} ; however, this is permissible as Lemma F.1 allows P i P_{i} to depend on Q 1 , … , Q i − 1 Q_{1},\dots,Q_{i-1} .) For every fixed Q Q (and thus fixed g g ), ∑ i ∈ [ N ] log ( p i ( Q ) ) = ∑ i ∈ [ N ] log ( 𝐏𝐫 P i [ P i = Q i ] ) = ∑ i ∈ [ N ] log ( 𝐏𝐫 R i [ f ( 𝒲 ( 𝒵 ) , R i ) = g i ] ) = − N 𝐥𝐨𝐬𝐬 ( g ) \displaystyle\sum_{i\in[N]}\log\big(p_{i}(Q)\big)=\sum_{i\in[N]}\log\big(\operatornamewithlimits{\mathbf{Pr}}_{P_{i}}[P_{i}=Q_{i}]\big)=\sum_{i\in[N]}\log\big(\operatornamewithlimits{\mathbf{Pr}}_{R_{i}}[f(\mathcal{W}(\mathcal{Z}),R_{i})=g_{i}]\big)=-N\mathbf{loss}(g) Applying Lemma F.1 we have log | 𝒲 | ≥ 𝔼 Q [ ∑ i ∈ [ N ] log ⁡ ( p i ​ ( Q ) × | N 0 − i + 1 | ) ] ≥ 𝔼 Q [ N ​ log ​ N 0 − N e 𝐥𝐨𝐬𝐬 ⁡ ( g ) ] = N ​ log ​ N 0 − N e 𝔼 Q 𝐥𝐨𝐬𝐬 ​ ( g ) . \displaystyle\log|\mathcal{W}|\geq\operatornamewithlimits{\mathbb{E}}_{Q}\Big[\sum_{i\in[N]}\log\big(p_{i}(Q)\times|N_{0}-i+1|\big)\Big]\geq\operatornamewithlimits{\mathbb{E}}_{Q}\Big[N\log\frac{N_{0}-N}{e^{\mathbf{loss}(g)}}\Big]=N\log\frac{N_{0}-N}{e^{\operatornamewithlimits{\mathbb{E}}_{Q}\mathbf{loss}(g)}}\kern 5.0pt. Ideally, if the model f f can perfectly memorize the entire training set { Z } = ( g 1 , … , g N ) \{Z\}=(g_{1},\dots,g_{N}) , its best possible loss 𝐥𝐨𝐬𝐬 ⁡ ( g ) = log ⁡ N \mathbf{loss}(g)=\log N is achieved. Thus, if the model can perfectly learn this training set, the bit complexity lower bound satisfies log ⁡ | 𝒲 | ≥ N ​ log ⁡ N 0 − N N ≥ ( 1 − o ⁡ ( 1 ) ) ​ N ​ log ⁡ N 0 N \log|\mathcal{W}|\geq N\log\frac{N_{0}-N}{N}\geq(1-o(1))N\log\frac{N_{0}}{N} when N ≪ N 0 N\ll N_{0} .

### F.2 Main Proof

We recommend that readers first review the warmup examples in Section F.1 before proceeding with this proof.

###### Proof of Theorem 3.2 .

Let us first construct the domains 𝒬 i \mathcal{Q}_{i} ’s in Lemma F.1 . 1. Let 𝒬 1 = [ N 0 ] \mathcal{Q}_{1}=[N_{0}] , 𝒬 2 = [ N 0 − 1 ] ⋯ 𝒬 N = [ N 0 − N + 1 ] \mathcal{Q}_{2}=[N_{0}-1]\cdots\mathcal{Q}_{N}=[N_{0}-N+1] .

2. Let ( 𝒬 N + j ​ D + 1 , … ​ 𝒬 N + j ​ D + D ) = ( [ T L ] , [ T L − 1 ] , … , [ T L − D + 1 ] ) \big(\mathcal{Q}_{N+jD+1},\dots\mathcal{Q}_{N+jD+D}\big)=\big([T^{L}],[T^{L}-1],\dots,[T^{L}-D+1]\big) for every j = 0 , … , K − 1 j=0,\dots,K-1 .

3. Let 𝒬 N + K ​ D + 1 = ⋯ = 𝒬 N + K ​ D + N ​ K = [ D C ] \mathcal{Q}_{N+KD+1}=\cdots=\mathcal{Q}_{N+KD+NK}=[D^{C}] .

Recall that each Q i Q_{i} is independently and uniformly generated at random from 𝒬 i \mathcal{Q}_{i} . We now present an alternative method for generating the training dataset 𝒵 ⁡ ( Q ) \mathcal{Z}(Q) .

1. Construct 𝒩 = ( n 1 , … , n N ) \mathcal{N}=(n_{1},\dots,n_{N}) as follows: Let n 1 n_{1} be the Q 1 Q_{1} -th name from 𝒩 0 \mathcal{N}_{0} ; for i > 1 i>1 , let n i n_{i} be the Q i Q_{i} -th name from 𝒩 0 ∖ { n 1 , … , n i − 1 } \mathcal{N}_{0}\setminus\{n_{1},\dots,n_{i-1}\} .

2. For each a ′ ∈ [ K ] a^{\prime}\in[K] , let a a be the a ′ a^{\prime} -th attribute in 𝒜 \mathcal{A} . Construct 𝒟 a = ( w 1 , … , w D ) \mathcal{D}_{a}=(w_{1},\dots,w_{D}) as follows: Let w 1 w_{1} be the Q N + ( a ′ − 1 ) ​ D + 1 Q_{N+(a^{\prime}-1)D+1} -th element in 𝒯 L \mathcal{T}^{L} ; for i > 1 i>1 , let w i w_{i} be the Q N + ( a ′ − 1 ) ​ D + i Q_{N+(a^{\prime}-1)D+i} -th element in 𝒯 L ∖ { w 1 , … , w i − 1 } \mathcal{T}^{L}\setminus\{w_{1},\dots,w_{i-1}\} .

3. For the n ′ n^{\prime} -th name n n and the a ′ a^{\prime} -th attribute a a , assign its value v ⋆ ​ ( n , a ) = ( v 1 , … , v C ) ∈ ( 𝒟 a ) C v^{\star}(n,a)=(v_{1},\dots,v_{C})\in(\mathcal{D}_{a})^{C} by setting each v i v_{i} as the s i s_{i} -th element in 𝒟 a \mathcal{D}_{a} , where the integer sequence ( s 1 , … , s C ) := Q N + K ​ D + ( n ′ − 1 ) ​ K + a ′ ∈ [ D C ] (s_{1},\dots,s_{C}):=Q_{N+KD+(n^{\prime}-1)K+a^{\prime}}\in[D^{C}] .

It is easy to verify that this gives the same dataset distribution as Definition 2.2 . Next, consider Q Q being fixed (thus the dataset 𝒵 \mathcal{Z} being fixed), we construct P 1 , P 2 , ⋯ , P N + K ​ D + N ​ K P_{1},P_{2},\cdots,P_{N+KD+NK} using the given model functions F ⊤ ​ ( W ​ ( 𝒵 ) , R ) F^{\top}(W(\mathcal{Z}),R) and F ⊥ ​ ( W ⁡ ( 𝒵 ) , n , a , R ) F^{\bot}(W(\mathcal{Z}),n,a,R) .

Name part. For the name part, construct P i P_{i} for i ∈ [ N ] i\in[N] following the approach from the “value-only” warmup example. Specifically, let R i R_{i} be fresh randomness, and define P i = s P_{i}=s if F ⊤ ​ ( W ⁡ ( { Z } ) , R i ) F^{\top}(W(\{Z\}),R_{i}) matches the s s -th element in 𝒩 0 ∖ { n 1 , … , n i − 1 } \mathcal{N}_{0}\setminus\{n_{1},\dots,n_{i-1}\} , or an arbitrary symbol ∅ \varnothing if it falls within { n 1 , … , n i − 1 } \{n_{1},\dots,n_{i-1}\} . 29 29 29 Importantly, P i P_{i} may depend on n 1 , … , n i − 1 n_{1},\dots,n_{i-1} ; however, since Lemma F.1 permits P i P_{i} to depend on Q 1 , … , Q i − 1 Q_{1},\dots,Q_{i-1} , this is acceptable. Adopting the analysis from the “name-only” warmup example, we obtain ∑ i ∈ [ N ] log 𝐏𝐫 P i [ P i = Q i ] = − N 𝐥𝐨𝐬𝐬 n ​ a ​ m ​ e ( 𝒵 ) . \textstyle\sum_{i\in[N]}\log\operatornamewithlimits{\mathbf{Pr}}_{P_{i}}[P_{i}=Q_{i}]=-N\mathbf{loss}_{name}(\mathcal{Z})\kern 5.0pt. (F.2)

Diversity Part. For the diversity component, we construct the P i P_{i} ’s as follows. For each a ′ ∈ [ K ] a^{\prime}\in[K] , let a a denote the a ′ a^{\prime} -th attribute in 𝒜 \mathcal{A} . We form P N + ( a ′ − 1 ) ​ D + i P_{N+(a^{\prime}-1)D+i} by initially calculating F ⊥ ​ ( W ⁡ ( 𝒵 ) , n , a , R i ) F^{\bot}(W(\mathcal{Z}),n,a,R_{i}) , where n ∈ 𝒩 n\in\mathcal{N} is selected uniformly at random. 30 30 30 Importantly, P N + ( a ′ − 1 ) ​ D + i P_{N+(a^{\prime}-1)D+i} depends on 𝒩 \mathcal{N} ; however, since Lemma F.1 permits P i P_{i} to depend on Q 1 , … , Q i − 1 Q_{1},\dots,Q_{i-1} , and since 𝒩 \mathcal{N} is uniquely determined by Q 1 , … , Q N Q_{1},\dots,Q_{N} , this is acceptable. Subsequently, if F ⊥ ​ ( W ⁡ ( 𝒵 ) , n , a , R i ) F^{\bot}(W(\mathcal{Z}),n,a,R_{i}) corresponds to the s s -th element in 𝒯 L ∖ { w 1 , … , w i − 1 } \mathcal{T}^{L}\setminus\{w_{1},\dots,w_{i-1}\} , then set P N + ( a ′ − 1 ) ​ D + i = s P_{N+(a^{\prime}-1)D+i}=s ; otherwise, set P N + ( a ′ − 1 ) ​ D + i = ∅ P_{N+(a^{\prime}-1)D+i}=\varnothing . 31 31 31 Importantly, P N + ( a ′ − 1 ) ​ D + i P_{N+(a^{\prime}-1)D+i} depends on w 1 , … , w i − 1 w_{1},\dots,w_{i-1} ; however, since Lemma F.1 permits P i P_{i} to depend on Q N + ( a ′ − 1 ) ​ D + 1 , … , Q N + ( a ′ − 1 ) ​ D + i − 1 Q_{N+(a^{\prime}-1)D+1},\dots,Q_{N+(a^{\prime}-1)D+i-1} , this is acceptable.

Now, let a a be the a ′ a^{\prime} -th element in 𝒜 \mathcal{A} . Consider Q Q as fixed, with randomness arising solely from the calculation of P i P_{i} ’s. Note that Q Q establishes an order of elements in 𝒟 a \mathcal{D}_{a} , denoted by w 1 , … , w D w_{1},\dots,w_{D} . We have ∑ i ∈ [ D ] log 𝐏𝐫 P N + ( a ′ − 1 ) ​ D + i [ P N + ( a ′ − 1 ) ​ D + i = Q N + ( a ′ − 1 ) ​ D + i ] \displaystyle\sum_{i\in[D]}\log\operatornamewithlimits{\mathbf{Pr}}_{P_{N+(a^{\prime}-1)D+i}}[P_{N+(a^{\prime}-1)D+i}=Q_{N+(a^{\prime}-1)D+i}] = ∑ i ∈ [ D ] log 𝔼 n ∈ 𝒩 𝐏𝐫 R [ [ F 1 ⊥ ( W ( 𝒵 ) , n , a , R ) = w i ] ] \displaystyle=\sum_{i\in[D]}\log\operatornamewithlimits{\mathbb{E}}_{n\in\mathcal{N}}\operatornamewithlimits{\mathbf{Pr}}_{R}\Big[\big[F^{\bot}_{1}(W(\mathcal{Z}),n,a,R)=w_{i}\big]\Big] = ∑ w ∈ 𝒟 a log 𝔼 n ∈ 𝒩 𝐏𝐫 R [ [ F 1 ⊥ ( W ( 𝒵 ) , n , a , R ) = w ] ] = : ♠ a \displaystyle=\sum_{w\in\mathcal{D}_{a}}\log\operatornamewithlimits{\mathbb{E}}_{n\in\mathcal{N}}\operatornamewithlimits{\mathbf{Pr}}_{R}\Big[\big[F^{\bot}_{1}(W(\mathcal{Z}),n,a,R)=w\big]\Big]=:\spadesuit_{a}

Let us denote by 𝒩 w , a \mathcal{N}_{w,a} the set of n ∈ 𝒩 n\in\mathcal{N} so that v ⋆ ​ ( n , a ) = w v^{\star}(n,a)=w . We have ♠ a \displaystyle\spadesuit_{a} = ∑ w ∈ 𝒟 a log ∑ n ∈ 𝒩 𝐏𝐫 R [ F 1 ⊥ ( W ( 𝒵 ) , n , a , R ) = w ] − D log N \displaystyle=\sum_{w\in\mathcal{D}_{a}}\log\sum_{n\in\mathcal{N}}\operatornamewithlimits{\mathbf{Pr}}_{R}\big[F^{\bot}_{1}(W(\mathcal{Z}),n,a,R)=w\big]-D\log N ≥ ① ∑ w ∈ 𝒟 a log ∑ n ∈ 𝒩 w , a 𝐏𝐫 R [ F 1 ⊥ ( W ( 𝒵 ) , n , a , R ) = w ] − D log N \displaystyle\overset{\text{①}}{\geq}\sum_{w\in\mathcal{D}_{a}}\log\sum_{n\in\mathcal{N}_{w,a}}\operatornamewithlimits{\mathbf{Pr}}_{R}\big[F^{\bot}_{1}(W(\mathcal{Z}),n,a,R)=w\big]-D\log N = ∑ w ∈ 𝒟 a log 1 | 𝒩 w , a | ∑ n ∈ 𝒩 w , a 𝐏𝐫 R [ F 1 ⊥ ( W ( 𝒵 ) , n , a , R ) = w ] − D log N + ∑ w ∈ 𝒟 log | 𝒩 w , a | \displaystyle=\sum_{w\in\mathcal{D}_{a}}\log\frac{1}{|\mathcal{N}_{w,a}|}\sum_{n\in\mathcal{N}_{w,a}}\operatornamewithlimits{\mathbf{Pr}}_{R}\big[F^{\bot}_{1}(W(\mathcal{Z}),n,a,R)=w\big]-D\log N+\sum_{w\in\mathcal{D}}\log|\mathcal{N}_{w,a}| ≥ ② ∑ w ∈ 𝒟 a 1 | 𝒩 w , a | ∑ n ∈ 𝒩 w , a log 𝐏𝐫 R [ F 1 ⊥ ( W ( 𝒵 ) , n , a , R ) = w ] − D log N + ∑ w ∈ 𝒟 log | 𝒩 w , a | \displaystyle\overset{\text{②}}{\geq}\sum_{w\in\mathcal{D}_{a}}\frac{1}{|\mathcal{N}_{w,a}|}\sum_{n\in\mathcal{N}_{w,a}}\log\operatornamewithlimits{\mathbf{Pr}}_{R}\big[F^{\bot}_{1}(W(\mathcal{Z}),n,a,R)=w\big]-D\log N+\sum_{w\in\mathcal{D}}\log|\mathcal{N}_{w,a}| Above, ① uses monotonicity of the log function and ② uses convexity of the log \log function. Using simple Chernoff bound, one can see that as long a N ≥ Ω ⁡ ( D ​ log ⁡ N ) N\geq\Omega(D\log N) , with high probability | 𝒩 w , a | ≥ ( 1 − o ⁡ ( 1 ) ) ​ N D |\mathcal{N}_{w,a}|\geq(1-o(1))\frac{N}{D} for all w ∈ D w\in D . Thus, we know with high probability ♠ a \displaystyle\spadesuit_{a} ≥ ( 1 + o ( 1 ) ) D ∑ w ∈ 𝒟 a 1 N ∑ n ∈ 𝒩 w , a log 𝐏𝐫 R [ F 1 ⊥ ( W ( 𝒵 ) , n , a , R ) = w ] − D log D − o ( D ) \displaystyle\geq(1+o(1))D\sum_{w\in\mathcal{D}_{a}}\frac{1}{N}\sum_{n\in\mathcal{N}_{w,a}}\log\operatornamewithlimits{\mathbf{Pr}}_{R}\big[F^{\bot}_{1}(W(\mathcal{Z}),n,a,R)=w\big]-D\log D-o(D) = ( 1 + o ( 1 ) ) D 1 N ∑ n ∈ 𝒩 log 𝐏𝐫 R [ F 1 ⊥ ( W ( 𝒵 ) , n , a , R ) = v ⋆ ( n , a ) ] − D log D − o ( D ) \displaystyle=(1+o(1))D\frac{1}{N}\sum_{n\in\mathcal{N}}\log\operatornamewithlimits{\mathbf{Pr}}_{R}\big[F^{\bot}_{1}(W(\mathcal{Z}),n,a,R)=v^{\star}(n,a)\big]-D\log D-o(D) Thus, summing up over all the diversity part, we have (recall we are fixing Q Q and thus fixing 𝒵 \mathcal{Z} ) ∑ i ∈ [ K ​ D ] log 𝐏𝐫 P N + i [ P N + i = Q N + i ] \displaystyle\hskip 10.00002pt\;\sum_{i\in[KD]}\log\operatornamewithlimits{\mathbf{Pr}}_{P_{N+i}}[P_{N+i}=Q_{N+i}] ≥ ( 1 + o ( 1 ) ) D 1 N ​ K ∑ n ∈ 𝒩 , a ∈ 𝒜 log 𝐏𝐫 R [ F 1 ⊥ ( W ( 𝒵 ) , n , a , R ) = v ⋆ ( n , a ) ] − K D log D − o ( K D ) \displaystyle\geq(1+o(1))D\frac{1}{NK}\sum_{n\in\mathcal{N},a\in\mathcal{A}}\log\operatornamewithlimits{\mathbf{Pr}}_{R}\big[F^{\bot}_{1}(W(\mathcal{Z}),n,a,R)=v^{\star}(n,a)\big]-KD\log D-o(KD) = − ( 1 + o ⁡ ( 1 ) ) ​ D ​ 𝐥𝐨𝐬𝐬 v ​ a ​ l ​ u ​ e ​ 1 ​ ( 𝒵 ) − K ​ D ​ log ⁡ D − o ⁡ ( K ​ D ) . \displaystyle=-(1+o(1))D\mathbf{loss}_{value1}(\mathcal{Z})-KD\log D-o(KD)\kern 5.0pt. (F.3)

Value part. For the value part, we construct P N + K ​ D + 1 , … , P N + K ​ D + N ​ K P_{N+KD+1},\dots,P_{N+KD+NK} as follows. For P N + K ​ D + ( n ′ − 1 ) ​ K + a ′ P_{N+KD+(n^{\prime}-1)K+a^{\prime}} , letting n n be the n ′ n^{\prime} -th name in 𝒩 \mathcal{N} and a a be the a ′ a^{\prime} -th attribute in 𝒜 \mathcal{A} . Let us compute F ⊥ ​ ( W ⁡ ( 𝒵 ) , n , a , R ) F^{\bot}(W(\mathcal{Z}),n,a,R) and find the corresponding s 1 , … , s C ∈ [ D ] s_{1},\dots,s_{C}\in[D] such that F i ⊥ ​ ( W ⁡ ( 𝒵 ) , n , a , R ) F_{i}^{\bot}(W(\mathcal{Z}),n,a,R) is the s i s_{i} -th element in 𝒟 a \mathcal{D}_{a} for each i ∈ [ C ] i\in[C] . If not found, we define P N + K ​ D + ( n ′ − 1 ) ​ K + a ′ = ∅ P_{N+KD+(n^{\prime}-1)K+a^{\prime}}=\varnothing ; otherwise, define P N + K ​ D + ( n ′ − 1 ) ​ K + a ′ = ( s 1 , … , s C ) ∈ [ D C ] P_{N+KD+(n^{\prime}-1)K+a^{\prime}}=(s_{1},\dots,s_{C})\in[D^{C}] . 32 32 32 Again, importantly, we can do so because P N + K ​ D + ( n ′ − 1 ) ​ K + a ′ P_{N+KD+(n^{\prime}-1)K+a^{\prime}} depends on 𝒩 , 𝒟 a \mathcal{N},\mathcal{D}_{a} but they can be computed using the values of Q 1 , … , Q N + K ​ D Q_{1},\dots,Q_{N+KD} .

Following the same simple argument as the “value-only” warmup example, we have ∑ i ∈ [ N ​ K ] log 𝐏𝐫 P N + K ​ D + i [ P N + K ​ D + i = Q N + K ​ D + i ] = ∑ n ∈ 𝒩 , a ∈ 𝒜 𝐏𝐫 [ F ⊥ ( W ( 𝒵 ) , n , a , R ) = v ⋆ ( n , a ) ] \displaystyle\sum_{i\in[NK]}\log\operatornamewithlimits{\mathbf{Pr}}_{P_{N+KD+i}}[P_{N+KD+i}=Q_{N+KD+i}]=\sum_{n\in\mathcal{N},a\in\mathcal{A}}\operatornamewithlimits{\mathbf{Pr}}\Big[F^{\bot}(W(\mathcal{Z}),n,a,R)=v^{\star}(n,a)\Big] = − N ​ K ​ 𝐥𝐨𝐬𝐬 v ​ a ​ l ​ u ​ e ​ ( 𝒵 ) \displaystyle=-NK\mathbf{loss}_{value}(\mathcal{Z}) (F.4)

Summing ( F.2 ) ( F.3 ) and ( F.4 ) , and applying Lemma F.1 , we have log | 𝒲 | ≥ 𝔼 𝒵 [ N ​ log ⁡ N 0 − N e 𝐥𝐨𝐬𝐬 n ​ a ​ m ​ e ​ ( 𝒵 ) + N ​ K ​ log ⁡ D C e 𝐥𝐨𝐬𝐬 v ​ a ​ l ​ u ​ e ​ ( 𝒵 ) + K ​ D ​ log ⁡ T L − D D ​ e ( 1 + o ⁡ ( 1 ) ) ​ 𝐥𝐨𝐬𝐬 v ​ a ​ l ​ u ​ e ​ 1 ​ ( 𝒵 ) − o ⁡ ( K ​ D ) ] . \displaystyle\log|\mathcal{W}|\geq\operatornamewithlimits{\mathbb{E}}_{\mathcal{Z}}\Big[N\log\frac{N_{0}-N}{e^{\mathbf{loss}_{name}(\mathcal{Z})}}+NK\log\frac{D^{C}}{e^{\mathbf{loss}_{value}(\mathcal{Z})}}+KD\log\frac{T^{L}-D}{De^{(1+o(1))\mathbf{loss}_{value1}(\mathcal{Z})}}-o(KD)\Big]\kern 5.0pt. This finishes the proof of Theorem 3.2 . ∎

## Appendix G Missing Remark

###### Remark G.1 .

Due to the significant overlap among textbooks, especially those designed for PreK-12 education, estimating the total amount of knowledge contained within all English-language textbooks can be challenging. However, we attempt to do so as follows.

According to a 2023 article, Pearson Education, a UK-based educational publisher, reported the highest revenue in 2021, with Wiley and McGraw Hill being the top two US-based educational publishers in terms of revenue. 33 33 33 https://wordsrated.com/education-book-publishing-companies-statistics/ , accessed March 2024.

• Pearson’s official website lists fewer than 2,100 textbooks. 34 34 34 https://www.pearson.com/en-us/pearsonplus/search.html for their full list of eTextbooks and http://www.mypearsonstore.com/bookstore/browse.asp for their full list of hard copy books, both accessed March 2024.

• Wiley’s official website lists fewer than 69,000 textbooks. 35 35 35 https://www.wiley.com/en-us/subjects , accessed March 2024. We wrote a code to sum up all the books in all of their subcategories; our code may double count books, so this is only a safe upper bound. We used this number instead of the “21,000” online books mentioned on https://www.wiley.com/learn/librarysolutions/online-books-purchase.html , accessed March 2024.

• McGraw Hill lists fewer than 22,000 textbooks for PreK-12 education, many of which have significant content overlap (as many are tailored for one of the 50 US states). 36 36 36 https://www.mheducation.com/search.html?searchQuery=&page=1&sortby=title_desc&order=desc&bu=seg&TYPE=Products&PRODUCT_TYPE_PATH=_Student+Materials , accessed March 2024. They list fewer than 2,000 textbooks for higher education.

Taking these figures into account, it seems reasonable to estimate that the content of all English-language textbooks could be condensed into no more than 100,000 textbooks. Assuming an average of 160,000 words per book (e.g., 400 pages with 400 words each), this would amount to a total of 16 billion words.
