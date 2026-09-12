##### Report GitHub Issue

Content selection saved. Describe the issue below:

# One Embedder, Any Task: Instruction-Finetuned Text Embeddings

###### Abstract

We introduce InstructOR , a new method for computing text embeddings given task instructions: every text input is embedded together with instructions explaining the use case (e.g., task and domain descriptions). Unlike encoders from prior work that are more specialized, InstructOR is a single embedder that can generate text embeddings tailored to different downstream tasks and domains, without any further training. We first annotate instructions for 330 diverse tasks and train InstructOR on this multitask mixture with a contrastive loss. We evaluate InstructOR on 70 embedding evaluation tasks (66 of which are unseen during training), ranging from classification and information retrieval to semantic textual similarity and text generation evaluation. InstructOR , while having an order of magnitude fewer parameters than the previous best model, achieves state-of-the-art performance, with an average improvement of 3.4% compared to the previous best results on the 70 diverse datasets. Our analysis suggests that InstructOR is robust to changes in instructions, and that instruction finetuning mitigates the challenge of training a single model on diverse datasets. Our model, code, and data are available at https://instructor-embedding.github.io .

## 1 Introduction

Text embeddings represent discrete text inputs (e.g., sentences, documents, and code) as fixed-sized vectors that can be used in many downstream tasks. These tasks include semantic textual similarity Agirre et al. (2012) ; Marelli et al. (2014) ; Cer et al. (2017) ; Lin et al. (2018) , information retrieval Mitra et al. (2017) ; Karpukhin et al. (2020) ; Izacard et al. (2022) , automatic text evaluation Zhang et al. (2020) ; Sellam et al. (2020) ; Hessel et al. (2021) , prompt retrieval for in-context learning Liu et al. (2022) ; Rubin et al. (2022) ; Su et al. (2022) , and beyond. Recently, we have seen dramatic advances in learning text embeddings Kiros et al. (2015) ; Conneau et al. (2017) ; Logeswaran and Lee (2018) ; Reimers and Gurevych (2019) ; Gao et al. (2021) ; Ni et al. (2021) ; Ni et al. (2022) that perform well on their intended tasks or datasets.

However, most existing embeddings can have significantly degraded performance when applied to new tasks or domains Thakur et al. (2021) ; Muennighoff et al. (2022) . For example, DPR Karpukhin et al. (2020) is stronger for retrieval than text similarity tasks, and vice versa for SimCSE Gao et al. (2021) . Moreover, existing embeddings usually perform poorly when applied to the same type of task but in different domains such as medicine and finance. A common method to address this issue is to further finetune the embeddings on datasets in downstream tasks and domains, which often requires a lot of annotated data Gururangan et al. (2020) . In this paper, we hypothesize that text embeddings (even for the same text input) can be adjusted to different downstream applications using task and domain descriptions, without further task- or domain-specific finetuning.

We introduce InstructOR ( Instruct ion-based O mnifarious R epresentations), a single multitask model that generates task- and domain-aware embeddings given a text input and its task instructions. It achieves state-of-the-art performance on massively many downstream embedding tasks without any training. At the core of our approach is instruction-based finetuning Zhong et al. (2021) ; Min et al. (2022) ; Sanh et al. (2022) ; Wei et al. (2022) : we embed every input together with its end task and domain instruction, departing from prior approaches to embeddings that only take text input. InstructOR embeds the same input into different vectors for different end goals (e.g., Who sings the song “Love Story”? is embedded into three different vectors for different tasks in Fig. 1 ). As shown in Fig. 2 , InstructOR is trained on MEDI, our new collection of 330 text embedding datasets newly annotated with human-written task instructions (§ 2.3 ). We train InstructOR with a contrastive loss over all datasets that maximizes the similarity between semantically related text pairs while minimizing unrelated pairs.

We extensively evaluate InstructOR on diverse domains (e.g., finance, medicine, and news) and a variety of downstream applications (a total of 70 embedding evaluation datasets, including 66 not seen during training), spanning classification, semantic textual similarity, information retrieval, text generation evaluation, and prompt retrieval for in-context learning. InstructOR significantly outperforms prior state-of-the-art embedding models by an average of 3.4% over the 70 diverse datasets. InstructOR also outperforms a variant that is trained without task instructions (§ 3 ), demonstrating the importance of instructions to create task-aware embeddings. Our analysis shows that instruction finetuning addresses the challenge of training a single model on diverse datasets (§ 4.1 ). Further, we demonstrate that the task diversity of MEDI makes the performance of InstructOR particularly robust to paraphrases in instructions (§ 4.2 ). Overall, these results strongly suggest that instruction finetuning should be adopted broadly for text embeddings, which we support by sharing all of our models and code.

## 2 InstructOR

InstructOR encodes inputs together with task instructions, thereby providing task-specific representations that can be used for many downstream language tasks, without any additional training. Here we introduce the architecture of InstructOR (§ 2.1 ), present how we perform multitask instruction-based finetuning (§ 2.2 ), and describe how we collect and annotate the MEDI training data (§ 2.3 ). By default, we refer "task" to a dataset, and use them interchangeably throughout the paper, while a "task category", such as Retrieval, includes many tasks.

### 2.1 Embedding Architecture

We build InstructOR , based on the single encoder architecture Izacard and Grave (2021) ; Ni et al. (2021) ; Ni et al. (2022) . Following prior work Ni et al. (2021) ; Ni et al. (2022) , we use GTR models as the backbone encoder (GTR-Base for InstructOR -Base, GTR-Large for InstructOR , GTR-XL for InstructOR -XL). The GTR models are initialized from T5 models, pretrained on a web corpus, and finetuned on information search datasets. The availability of different sizes in the GTR model family allows us to explore the scaling behaviors of instruction-finetuned embedding models. Given an input text x x and a task instruction I x I_{x} , InstructOR encodes their concatenation I x ⊕ x I_{x}\oplus x . We then generate a fixed-sized, task-specific embedding E I ​ ( I x , x ) \textbf{E}_{I}(I_{x},x) by applying mean pooling to the last hidden representations over the tokens in x x .

### 2.2 Training Objective

InstructOR is trained by formulating a wide variety of tasks as a text-to-text problem of distinguishing good/bad candidate outputs y ∈ { y + , y i − } y\in\{y^{+},y^{-}_{i}\} given an input x x , where a training sample corresponds to the tuple ( x , I x , y , I y ) (x,I_{x},y,I_{y}) , with I x I_{x} and I y I_{y} being instructions associated with x x and y y , respectively. For example, in a retrieval task, x x is a query, and good/bad y y is a relevant/irrelevant document from some document collection. For a textual similarity task, the input and output have a similar form and typically come from the same source collection. For a classification task, training samples can be formed by choosing y y as text sequences associated with the same vs. different classes for good vs. bad examples (Details about pair construction are in § 2.3 ). The input and output instructions depend on the task. For symmetric tasks such as textual similarity, where the input and output have the same form and encoding objective, the instructions are the same. For asymmetric tasks such as retrieval, where the input is a single sentence query and the output is a document, the instructions reflect that difference.

The goodness of candidate y y for input x x is given by similarity s ⁡ ( x , y ) s(x,y) that is the cosine between their InstructOR embeddings: {align*} s(x, y) = cos( E _I(I_x ⊕x), E _I(I_y ⊕y)) Following Ni et al. (2021) , we maximize the similarity between positive pairs ( x , y + ) (x,y^{+}) and minimize negative pairs { ( x , y i − ) } i = 1 k \{(x,y^{-}_{i})\}_{i=1}^{k} , where k k denotes the number of negative pairs per positive pair. Specifically, our training objective is: {align*} L = e s(x, y + )/ γ ∑ y ∈ B e s(x, y)/ γ , where γ \gamma is the softmax temperature and ℬ \mathcal{B} is a union of ( x , y + ) (x,y^{+}) and { ( x , y i − ) } i = 1 k \{(x,y^{-}_{i})\}_{i=1}^{k} . Further following Ni et al. (2021) , we compute the same loss with x x and y y swapped and add it to the previous loss (i.e., bidirectional in-batch sampled loss).

### 2.3 MEDI: Multitask Embedding Data with Instructions

There are no existing datasets that consist of a variety of tasks for embedding training with instructions. We thus construct a collection of 330 datasets with instructions across diverse task categories and domains: M ultitask E mbeddings D ata with I nstructions (MEDI).

#### Data Construction

We build MEDI by combining 300 datasets from Super-NaturalInstructions (super-NI; Wang et al., 2022b ) with 30 datasets from existing collections designed for embedding training.

The super-NI datasets come with natural language instructions, but positive and negative pairs are not provided. We construct these pairs by using Sentence-T5 embeddings Ni et al. (2022) , 1 1 1 We do not include instruction for Sentence-T5 as it is not fine-tuned with instructions. denoted with E ​ ( ⋅ ) \textbf{E}(\cdot) . For the classification datasets, we calculate the pairwise cosine similarity between examples based on input text embeddings cos ⁡ ( E ​ ( x i ) , E ​ ( x j ) ) \cos(\textbf{E}(x_{i}),\textbf{E}(x_{j})) . An example x i x_{i} with a high similarity to x j x_{j} is used to create a positive pair if both examples have the same class label ( y j + = y i y_{j}^{+}=y_{i} ), and a negative pair if the labels differ ( y j − ≠ y i y_{j}^{-}\neq y_{i} ). For the remaining tasks where the output labels are text sequences, the following scores are first computed: {align*} s_pos = cos( E (x_i), E (x_j))+cos( E (y_i), E (y_j)) {align*} s_neg = cos( E (x_i), E (x_j))-cos( E (y_i), E (y_j)) We select example pairs with the highest s p ​ o ​ s s_{pos} as positive pairs and highest s n ​ e ​ g s_{neg} as hard negative pairs. We use one hard negative together with in-batch sampled negatives in the training. Our later analysis shows that the training data from super-NI particularly improve the instruction robustness in evaluation due to the diverse task definitions (§ 4.2 ).

The other 30 embedding training datasets come from the Sentence Transformers embedding data, 2 2 2 https://huggingface.co/datasets/sentence-transformers/embedding-training-data . KILT Petroni et al. (2021) , and MedMCQA Pal et al. (2022) . These 30 datasets already contain positive pairs; a few of them, such as MSMARCO Bajaj et al. (2016) and Natural Questions Kwiatkowski et al. (2019) , also contain hard negative pairs. Following Ni et al. (2021) , we use four negative pairs (hard or in-batch negatives) during the model finetuning process. Since all of these datasets do not have instructions, we develop a unified instruction template and manually write a specific prompt for each dataset, as described next. 3 3 3 All prompts are reviewed by multiple authors independently to make sure they consistently follow our template. We release these instructions together with our MEDI data.

#### Instruction Annotation

Each training instance from MEDI is a tuple ( x , I x , y , I y ) (x,I_{x},y,I_{y}) , where the natural language instructions I x I_{x} and I y I_{y} describe how the embeddings of x x and y y are used for the task. For example, in open-domain QA (e.g., Natural Questions in Table 1 ), I x I_{x} is “Represent the Wikipedia question for retrieving supporting documents; Input: ,” and I y I_{y} is “Represent the Wikipedia document for retrieval; Input: .”

To make instructions consistent across all datasets in MEDI, we design a unified instruction format that consists of the following parts (see Table 4 in the appendix for instances of each part): • Text Type specifies the type of input text that we encode using the embedding model. For example, for an open-domain QA task, the input type of the query is a question, while the input type of the target is a document.

• Task Objective (Optional) describes the objective of how the input text is used in a task. For example, for a classification task, the task objective is to classify the sentence into some category, while the task objective of the retrieval is to retrieve a relevant document. Because not all sentences are associated with a specific task (e.g., STS targets general encoding), we make this part optional.

• Domain (Optional) describes the task domain. For example, for NewsIR, the domain of the task is news. Because not all tasks specify a domain (e.g., STS deals with general statements),this part is also optional.

The final instruction takes the following format: “ Represent the ( Domain ) Text Type for Task Objective : ." Appendix 8 shows instructions for each dataset in MEDI.

## 3 Experiments

We train InstructOR on the MEDI data and evaluate it on a wide range of 70 downstream tasks. Specifically, we use the MTEB benchmark from recent work Muennighoff et al. (2022) , which consists of 56 datasets over 7 diverse task categories, such as classification, reranking, and information retrieval. We then further apply InstructOR to prompt retrieval for in-context learning and text generation evaluation. In all three settings, InstructOR achieves the state-of-the-art performance. See Appendix § A and § B for our detailed settings.

### 3.1 Main Results

Table 2 presents the results from InstructOR and the baselines over the three benchmarks: MTEB, Billboard, and prompt retrieval. We conduct head-to-head comparison between InstructOR and GTR models with the same size. We also include the performance of other representative models for reference, while they are not meant for direct comparison.

InstructOR achieves the best performance on all three benchmarks on average. Compared to GTR-Large (335M), from which InstructOR is initialized, instruction finetuning enhances the performance by 5.7%, 18.3%, and 5.7% in MTEB, Billboard, and prompt retrieval respectively. Specifically, among all task categories, InstructOR (335M) demonstrates large improvements over GTR-Large on the text evaluation (18.3%), classification (10.1%), and clustering tasks (8.9%). Particularly noteworthy is InstructOR ’s performance compared to the previous state-of-the-art model, Sent-T5-XXL (58.4 vs. 56.5 on average), despite the fact that InstructOR has one order of magnitude fewer parameters (335M vs. 4.8B).

As expected, the retrieval-based models (e.g., GTR-XXL) show strong performance on retrieval and reranking but significantly lag behind on STS and classification. Conversely, similarity-based models (e.g., Sent-T5-XXL) perform well on STS, classification, and text evaluation, but not on retrieval. It suggests that these baselines tend to generate specialized embeddings that only excel at certain tasks, while InstructOR provides universal embeddings that perform well on diverse task categories.

## 4 Analysis and Ablations

We demonstrate InstructOR enables universal text embeddings for many diverse tasks. Here we analyze our results from various perspectives: the importance of instructions (§ 4.1 ), instruction robustness (§ 4.2 ) and complexity (§ 4.3 ), model sizes (§ 4.4 ), domain shifts (§ 4.5 ), and qualitative analysis (§ 4.6 ). By default, we report average performance across all categories.

### 4.1 Instructions Enable Diverse Training

Here we analyze the importance of instructions when training data are diverse. We first split MEDI into symmetric (e.g., text similarity) and asymmetric groups (e.g., open-domain QA), as defined in § 2.3 (see Table § 5 in the appendix for details about the symmetric and asymmetric groups). We then train InstructOR with or without instructions on each group separately.

As shown in Fig. 3 , InstructOR finetuned without instructions yields performance similar to or better than the original GTR model (dotted line), if the data are symmetric or asymmetric only . However, InstructOR suffers if finetuned without task instructions on the combination of both types of data (entire MEDI). In contrast, finetuning with instructions enables the model to benefit from the combination of symmetric and asymmetric data (see that the rightmost bar gets additive performance gains from the asymmetric and symmetric tasks). This result demonstrates the importance of instruction finetuning when diverse data are used for embedding training. Note that training on symmetric tasks only without instructions is similar to Sent-T5. Similarly, training on asymmetric tasks only without instructions is similar to GTR, which is also trained on asymmetric open-domain QA datasets. Departing from these prior methods, instruction-based finetuning enables diverse training on both types.

### 4.2 Instruction Robustness

Previous work Sanh et al. (2022) ; Zhou et al. (2022) shows that instruction-finetuned language models are not robust to paraphrased instructions. Here we measure InstructOR ’s robustness to variation in human-written instructions.

Specifically, we write five paraphrased instructions for all evaluation datasets (Table 6 in Appendix) and measure InstructOR ’s performance gap between the best-performing and the worst-performing instructions. Fig. 4 shows that inclusion of 300 super-NI datasets is critical to the robustness of InstructOR . Removing these datasets from training (w/o super-NI) substantially increases the performance gap between the best- and worst-performing instructions, suggesting that super-NI’s diverse instructions help the model handle different formats and styles.

### 4.3 Complexity of Instructions

Here we further analyze the role of instructions over varying degrees of their complexity. Specifically, we consider four levels of instruction complexity: N/A (no instructions), dataset tags, simple instructions, and detailed instructions (the original instruction format, § 2.3 ). In the dataset tag setup, each example is prepended with its dataset name. For instance, on the Natural Questions dataset, the query is formatted as "Natural Questions; Input: who sings the song Love Story" ). In the simple instruction setup, we use one or two words to describe the domain (e.g., for Natural Questions, the input query is Wikipedia Questions; Input: who sings the song Love Story ). Fig. 5 shows their average performances across all task categories. Even with trivial dataset tags, InstructOR outperforms the original GTR model, illustrating the effectiveness of instructions for diverse training. As more information is provided in the instruction (from tag to simple and from simple to detail), we observe consistent improvements.

### 4.4 Model Sizes and Instruction Finetuning

Fig. 6 studies the influence of model sizes. Specifically, we use GTR-Base (0.1B), GTR-Large (0.3B), and GTR-XL (1.5B). They are pretrained on the same corpus and differ only in the encoder size (the embedding sizes are the same). We compare models of various sizes and report the average performance across all the categories. As the encoder transformer model scales up, the performance continues to increase for both GTR and InstructOR . Nonetheless, the improvement in InstructOR is more pronounced, perhaps because embeddings with instructions benefit from larger capacities. This implies that large models are more generalizable to compute texts in various domains and task types, providing embeddings for general purposes. Further scale-ups are left to future work.

### 4.5 Instructions Mitigate Domain Shifts

One advantage of instruction-based finetuning is that it improves models’ ability to generalize to unseen domains and tasks. To demonstrate this effectiveness, we found three unseen domains that InstructOR was not trained on: geography, biology, and civil comments. As shown in Table 3 , InstructOR largely improves (above the average improvement) GTR-Large’s performance on all three domains, indicating that instructions can help more when applying models to unseen or uncommon domains.

### 4.6 Qualititive Analysis

In this qualitative analysis, we use T-SNE van der Maaten and Hinton (2008) to visualize two example of classification with and without instructions. The desired outcome is, for pairs with the same sentiment to be closer together, and pairs with different sentiment to be farther apart. As shown in Fig. 7 , without instructions, the green dot pairs (different sentiment) are closer together in the embedding space, while the red dot pairs (same sentiment) are farther apart. However, with instructions, our method ( InstructOR ) successfully encodes the red dot pairs into close embeddings and correctly classifies the pairs. The distance between the green dot pairs with different sentiment is also larger in the embedding space with instructions.

## 5 Related Work

#### Text Embeddings

Text embeddings are useful in many applications such as information retrieval Thakur et al. (2021) , text similarity Gao et al. (2021) , prompt retrieval for in-context learning Su et al. (2022) , classification Reimers and Gurevych (2019) , and beyond. Much prior work develops different embedding models for different applications. For example, SBERT Reimers and Gurevych (2019) and SimCSE Gao et al. (2021) are applied solely to text similarity and classification tasks, while DPR Karpukhin et al. (2020) and Contriever Izacard et al. (2022) focus on information retrieval. Different from Sentence-T5 trained only on symmetric data or GTR trained only on asymmetric data, we combine both groups of datasets and build MEDI, which is then used to train InstructOR with instructions. Muennighoff et al. (2022) introduced the massive text embedding benchmark (MTEB), which can be used to evaluate embedding models on a variety of embedding tasks, spanning reranking, classification, information retrieval, bitext mining, pair classification, STS, and summarization. Their benchmark shows that models performing well on one task may not perform well on other tasks. The poor zero-shot transfer abilities of existing embedding models make it difficult to use them in applications where only few labeled data are available. This motivates us to develop a single embedding model that is applicable to a variety of tasks and has better generalization to unseen tasks. Wang et al. (2022a) recently proposed E5, weakly-supervised contrastive pre-trained text embeddings, which achieve strong performance across various tasks on the MTEB benchmark, employing a larger embedding dimension compared to InstructOR .

#### Instruction Finetuning

Recent work demonstrated that instruction-finetuned language models could perform new tasks given a natural language instruction Mishra et al. (2022) ; Zhong et al. (2021) ; Min et al. (2022) ; Sanh et al. (2022) ; Wei et al. (2022) ; Wang et al. (2022b) ; Ouyang et al. (2022) . Nonetheless, instruction finetuning has yet to be studied in the context of broadly-applicable embeddings. In this work, we explore finetuning embedding models to follow human instructions where the instruction specifies eventual use cases. Concurrent work demonstrated that instructions could facilitate information retrieval Asai et al. (2022) , which is related to our InstructOR design. They used instructions to build a task-aware retrieval system and conducted evaluations on the retrieval task; we build a general-purpose embedding model with instructions that can be applied to 8 tasks categories (Fig. 2 ), including retrieval, text similarity, clustering, and text evaluation.

## 6 Conclusion

We introduced InstructOR , a single model that creates broadly-applicable text embeddings using natural language instructions. We constructed MEDI, a collection of diverse datasets, to finetune InstructOR with instructions. Our extensive experiments showed that InstructOR achieves state-of-the-art performance on text embedding benchmarks, as well as prompt retrieval for few-shot in-context learning. We hope that researchers and practitioners will benefit from our embeddings or our datasets for tasks of their interest.

## 7 Limitations

Although InstructOR significantly improves the baseline GTR performance, we were only able to use four negative examples during the model finetuning process due to computation constraints. However, negative examples have been shown to play an important role in contrastive learning Robinson et al. (2021) . We hope that future work will scale up the number of negatives used during finetuning and investigate various methods for mining hard negatives. Additionally, we do not have enough computation resources to apply multitask instruction finetuning to GTR-XXL (4.8B parameters), which is also an area for future exploration.

At the core of InstructOR is the instruction design. While our current unified instruction format has demonstrated effectiveness, future research can explore other instructional elements to further improve performance. For example, previous work Wang et al. (2022b) have shown that incorporating demonstration examples and explanations can be beneficial for instruction-finetuned language models.

## Acknowledgements

We thank Akari Asai, Jack Lin, Minghan Li, and the ARK group at UW for their helpful feedback on this work.

## References

Agirre et al. (2012) Eneko Agirre, Daniel Cer, Mona Diab, and Aitor Gonzalez-Agirre. 2012. SemEval-2012 task 6: A pilot on semantic textual similarity . In Proc. of SemEval .

Asai et al. (2022) Akari Asai, Timo Schick, Patrick Lewis, Xilun Chen, Gautier Izacard, Sebastian Riedel, Hannaneh Hajishirzi, and Wen-tau Yih. 2022. Task-aware retrieval with instructions .

Bajaj et al. (2016) Payal Bajaj, Daniel Campos, Nick Craswell, Li Deng, Jianfeng Gao, Xiaodong Liu, Rangan Majumder, Andrew McNamara, Bhaskar Mitra, Tri Nguyen, et al. 2016. MS MARCO: A human generated machine reading comprehension dataset . In Proc. of CoCo .

Barrault et al. (2020) Loïc Barrault, Magdalena Biesialska, Ondřej Bojar, Marta R. Costa-jussà, Christian Federmann, Yvette Graham, Roman Grundkiewicz, Barry Haddow, Matthias Huck, Eric Joanis, Tom Kocmi, Philipp Koehn, Chi-kiu Lo, Nikola Ljubešić, Christof Monz, Makoto Morishita, Masaaki Nagata, Toshiaki bnghvtcf Nakazawa, Santanu Pal, Matt Post, and Marcos Zampieri. 2020. Findings of the 2020 conference on machine translation (WMT20) . In Proc. of WMT .

Bowman et al. (2015) Samuel R Bowman, Gabor Angeli, Christopher Potts, and Christopher D Manning. 2015. A large annotated corpus for learning natural language inference . In Proc. of EMNLP .

Cer et al. (2017) Daniel Cer, Mona Diab, Eneko Agirre, Inigo Lopez-Gazpio, and Lucia Specia. 2017. SemEval-2017 task 1: Semantic textual similarity-multilingual and cross-lingual focused evaluation . In Proc. of SemEval .

Cohan et al. (2020) Arman Cohan, Sergey Feldman, Iz Beltagy, Doug Downey, and Daniel S. Weld. 2020. SPECTER: Document-level representation learning using citation-informed transformers . In Proc. of ACL .

Conneau and Kiela (2018) Alexis Conneau and Douwe Kiela. 2018. SentEval: An evaluation toolkit for universal sentence representations . In Proc. of LREC .

Conneau et al. (2017) Alexis Conneau, Douwe Kiela, Holger Schwenk, Loïc Barrault, and Antoine Bordes. 2017. Supervised learning of universal sentence representations from natural language inference data . In Proc. of EMNLP .

Coster and Kauchak (2011) William Coster and David Kauchak. 2011. Simple english Wikipedia: a new text simplification task . In Proc. of ACL .

Dinan et al. (2019) Emily Dinan, Stephen Roller, Kurt Shuster, Angela Fan, Michael Auli, and Jason Weston. 2019. Wizard of Wikipedia: Knowledge-powered conversational agents . In Proc. of ICLR .

Elsahar et al. (2018) Hady Elsahar, Pavlos Vougiouklis, Arslen Remaci, Christophe Gravier, Jonathon Hare, Frederique Laforest, and Elena Simperl. 2018. T-rex: A large scale alignment of natural language with knowledge base triples . In Proc. of LREC .

Fabbri et al. (2021) Alexander R Fabbri, Wojciech Kryściński, Bryan McCann, Caiming Xiong, Richard Socher, and Dragomir Radev. 2021. SummEval: Re-evaluating summarization evaluation . TACL .

Fader et al. (2014) Anthony Fader, Luke Zettlemoyer, and Oren Etzioni. 2014. Open question answering over curated and extracted knowledge bases . In Proc. of KDD .

Fan et al. (2019) Angela Fan, Yacine Jernite, Ethan Perez, David Grangier, Jason Weston, and Michael Auli. 2019. ELI5: long form question answering . In Proc. of ACL .

Freitag et al. (2021) Markus Freitag, George Foster, David Grangier, Viresh Ratnakar, Qijun Tan, and Wolfgang Macherey. 2021. Experts, errors, and context: A large-scale study of human evaluation for machine translation . TACL .

Gao and Callan (2022) Luyu Gao and Jamie Callan. 2022. Unsupervised corpus aware language model pre-training for dense passage retrieval . In Proc. of ACL .

Gao et al. (2021) Tianyu Gao, Xingcheng Yao, and Danqi Chen. 2021. SimCSE: Simple contrastive learning of sentence embeddings . In Proc. of EMNLP .

Gupta et al. (2019) Mansi Gupta, Nitish Kulkarni, Raghuveer Chanda, Anirudha Rayasam, and Zachary C Lipton. 2019. AmazonQA: A review-based question answering task . In Proc. of IJCAI .

Gururangan et al. (2020) Suchin Gururangan, Ana Marasović, Swabha Swayamdipta, Kyle Lo, Iz Beltagy, Doug Downey, and Noah A. Smith. 2020. Don’t stop pretraining: Adapt language models to domains and tasks . In Proc. of ACL .

Hamborg et al. (2017) Felix Hamborg, Norman Meuschke, Corinna Breitinger, and Bela Gipp. 2017. news-please: A generic news crawler and extractor . In Proc. of ISI .

He and McAuley (2016) Ruining He and Julian McAuley. 2016. Ups and downs: Modeling the visual evolution of fashion trends with one-class collaborative filtering . In Proc. of WWW .

Hessel et al. (2021) Jack Hessel, Ari Holtzman, Maxwell Forbes, Ronan Le Bras, and Yejin Choi. 2021. CLIPScore: A reference-free evaluation metric for image captioning . In Proc. of EMNLP .

Hoogeveen et al. (2015) Doris Hoogeveen, Karin M Verspoor, and Timothy Baldwin. 2015. CQADupStack: A benchmark data set for community question-answering research . In Proc. of ADCS .

Husain et al. (2019) Hamel Husain, Ho-Hsiang Wu, Tiferet Gazit, Miltiadis Allamanis, and Marc Brockschmidt. 2019. CodeSearchNet challenge: Evaluating the state of semantic code search .

Izacard et al. (2022) Gautier Izacard, Mathilde Caron, Lucas Hosseini, Sebastian Riedel, Piotr Bojanowski, Armand Joulin, and Edouard Grave. 2022. Unsupervised dense information retrieval with contrastive learning . TMLR .

Izacard and Grave (2021) Gautier Izacard and Edouard Grave. 2021. Leveraging passage retrieval with generative models for open domain question answering . In Proc. of EACL .

Joshi et al. (2017) Mandar Joshi, Eunsol Choi, Daniel Weld, and Luke Zettlemoyer. 2017. TriviaQA: A Large Scale Distantly Supervised Challenge Dataset for Reading Comprehension . In Proc. of ACL .

Karpukhin et al. (2020) Vladimir Karpukhin, Barlas Oguz, Sewon Min, Patrick Lewis, Ledell Wu, Sergey Edunov, Danqi Chen, and Wen-tau Yih. 2020. Dense passage retrieval for open-domain question answering . In Proc. of EMNLP .

Kasai et al. (2022a) Jungo Kasai, Keisuke Sakaguchi, Ronan Le Bras, Lavinia Dunagan, Jacob Morrison, Alexander R. Fabbri, Yejin Choi, and Noah A. Smith. 2022a. Bidimensional leaderboards: Generate and evaluate language hand in hand . In Proc. of NAACL .

Kasai et al. (2022b) Jungo Kasai, Keisuke Sakaguchi, Lavinia Dunagan, Jacob Morrison, Ronan Le Bras, Yejin Choi, and Noah A. Smith. 2022b. Transparent human evaluation for image captioning . In Proc. of NAACL .

Khashabi et al. (2021) Daniel Khashabi, Amos Ng, Tushar Khot, Ashish Sabharwal, Hannaneh Hajishirzi, and Chris Callison-Burch. 2021. GooAQ: Open question answering with diverse answer types . In Findings of the ACL: EMNLP 2021 .

Khashabi et al. (2022) Daniel Khashabi, Gabriel Stanovsky, Jonathan Bragg, Nicholas Lourie, Jungo Kasai, Yejin Choi, Noah A. Smith, and Daniel S. Weld. 2022. GENIE: Toward reproducible and standardized human evaluation for text generation . In Proc. of EMNLP .

Kiros et al. (2015) Ryan Kiros, Yukun Zhu, Russ R Salakhutdinov, Richard Zemel, Raquel Urtasun, Antonio Torralba, and Sanja Fidler. 2015. Skip-thought vectors . In Proc. of NeurIPS .

Koupaee and Wang (2018) Mahnaz Koupaee and William Yang Wang. 2018. WikiHow: A large scale text summarization dataset .

Kwiatkowski et al. (2019) Tom Kwiatkowski, Jennimaria Palomaki, Olivia Redfield, Michael Collins, Ankur Parikh, Chris Alberti, Danielle Epstein, Illia Polosukhin, Jacob Devlin, Kenton Lee, et al. 2019. Natural questions: a benchmark for question answering research . TACL .

Levy et al. (2017) Omer Levy, Minjoon Seo, Eunsol Choi, and Luke Zettlemoyer. 2017. Zero-shot relation extraction via reading comprehension . In Proc. of CoNLL .

Lewis et al. (2021) Patrick Lewis, Yuxiang Wu, Linqing Liu, Pasquale Minervini, Heinrich Küttler, Aleksandra Piktus, Pontus Stenetorp, and Sebastian Riedel. 2021. PAQ: 65 million probably-asked questions and what you can do with them . TACL .

Li (2020) Shuyang Li. 2020. INTERVIEW: NPR media dialog transcripts .

Lin et al. (2018) Lucy H. Lin, Scott B. Miles, and Noah A. Smith. 2018. Semantic matching against a corpus: New methods and applications .

Lin et al. (2014) Tsung-Yi Lin, Michael Maire, Serge J. Belongie, Lubomir D. Bourdev, Ross B. Girshick, James Hays, Pietro Perona, Deva Ramanan, Piotr Dollár, and C. Lawrence Zitnick. 2014. Microsoft COCO: common objects in context . In Proc. of ECCV .

Liu et al. (2022) Jiachang Liu, Dinghan Shen, Yizhe Zhang, Bill Dolan, Lawrence Carin, and Weizhu Chen. 2022. What makes good in-context examples for GPT-3? In Proc. of DeeLIO 2022 .

Liu et al. (2021) Pengfei Liu, Weizhe Yuan, Jinlan Fu, Zhengbao Jiang, Hiroaki Hayashi, and Graham Neubig. 2021. Pre-train, prompt, and predict: A systematic survey of prompting methods in natural language processing .

Lo et al. (2020) Kyle Lo, Lucy Lu Wang, Mark Neumann, Rodney Kinney, and Daniel Weld. 2020. S2ORC: The semantic scholar open research corpus . In Proc. of ACL .

Logeswaran and Lee (2018) Lajanugen Logeswaran and Honglak Lee. 2018. An efficient framework for learning sentence representations . In Proc. of ICLR .

Marelli et al. (2014) Marco Marelli, Stefano Menini, Marco Baroni, Luisa Bentivogli, Raffaella Bernardi, and Roberto Zamparelli. 2014. A SICK cure for the evaluation of compositional distributional semantic models . In Proc. of LREC .

Min et al. (2022) Sewon Min, Mike Lewis, Luke Zettlemoyer, and Hannaneh Hajishirzi. 2022. MetaICL: Learning to learn in context . In Proc. of NAACL .

Mishra et al. (2022) Swaroop Mishra, Daniel Khashabi, Chitta Baral, and Hannaneh Hajishirzi. 2022. Cross-task generalization via natural language crowdsourcing instructions. In Proceedings of the 60th Annual Meeting of the Association for Computational Linguistics (Volume 1: Long Papers) , pages 3470–3487.

Mitra et al. (2017) Bhaskar Mitra, Fernando Diaz, and Nick Craswell. 2017. Learning to match using local and distributed representations of text for web search . In Proc. of WWW .

Muennighoff (2022) Niklas Muennighoff. 2022. SGPT: GPT sentence embeddings for semantic search .

Muennighoff et al. (2022) Niklas Muennighoff, Nouamane Tazi, Loic Magne, and Nils Reimers. 2022. MTEB: Massive text embedding benchmark .

Narayan et al. (2018) Shashi Narayan, Shay B. Cohen, and Mirella Lapata. 2018. Don’t give me the details, just the summary! topic-aware convolutional neural networks for extreme summarization . In Proc. of EMNLP .

Ni et al. (2022) Jianmo Ni, Gustavo Hernandez Abrego, Noah Constant, Ji Ma, Keith Hall, Daniel Cer, and Yinfei Yang. 2022. Sentence-T5: Scalable sentence encoders from pre-trained text-to-text models . In Findings of the ACL: ACL 2022 .

Ni et al. (2021) Jianmo Ni, Chen Qu, Jing Lu, Zhuyun Dai, Gustavo Hernández Ábrego, Ji Ma, Vincent Y. Zhao, Yi Luan, Keith B. Hall, Ming-Wei Chang, and Yinfei Yang. 2021. Large dual encoders are generalizable retrievers . In Proc. of EMNLP .

Ouyang et al. (2022) Long Ouyang, Jeff Wu, Xu Jiang, Diogo Almeida, Carroll L Wainwright, Pamela Mishkin, Chong Zhang, Sandhini Agarwal, Katarina Slama, Alex Ray, et al. 2022. Training language models to follow instructions with human feedback . In Proc. of NeurIPS .

Pal et al. (2022) Ankit Pal, Logesh Kumar Umapathi, and Malaikannan Sankarasubbu. 2022. MedMCQA: A large-scale multi-subject multi-choice dataset for medical domain question answering . In Proc. of CHIL .

Petroni et al. (2021) Fabio Petroni, Aleksandra Piktus, Angela Fan, Patrick Lewis, Majid Yazdani, Nicola De Cao, James Thorne, Yacine Jernite, Vladimir Karpukhin, Jean Maillard, Vassilis Plachouras, Tim Rocktäschel, and Sebastian Riedel. 2021. KILT: a benchmark for knowledge intensive language tasks . In Proc. of NAACL .

Rajpurkar et al. (2016) Pranav Rajpurkar, Jian Zhang, Konstantin Lopyrev, and Percy Liang. 2016. SQuAD: 100,000+ questions for machine comprehension of text . In Proc. of EMNLP .

Reimers and Gurevych (2019) Nils Reimers and Iryna Gurevych. 2019. Sentence-BERT: Sentence embeddings using Siamese BERT-networks . In Proc. of EMNLP .

Robinson et al. (2021) Joshua David Robinson, Ching-Yao Chuang, Suvrit Sra, and Stefanie Jegelka. 2021. Contrastive learning with hard negative samples . In International Conference on Learning Representations .

Rosenberg and Hirschberg (2007) Andrew Rosenberg and Julia Hirschberg. 2007. V-measure: A conditional entropy-based external cluster evaluation measure . In Proc. of EMNLP .

Rubin et al. (2022) Ohad Rubin, Jonathan Herzig, and Jonathan Berant. 2022. Learning to retrieve prompts for in-context learning . In Proc. of NAACL .

Sanh et al. (2022) Victor Sanh, Albert Webson, Colin Raffel, Stephen H. Bach, Lintang Sutawika, Zaid Alyafeai, Antoine Chaffin, Arnaud Stiegler, Teven Le Scao, Arun Raja, Manan Dey, M Saiful Bari, Canwen Xu, Urmish Thakker, Shanya Sharma, Eliza Szczechla, Taewoon Kim, Gunjan Chhablani, Nihal V. Nayak, Debajyoti Datta, Jonathan Chang, Mike Tian-Jian Jiang, Han Wang, Matteo Manica, Sheng Shen, Zheng Xin Yong, Harshit Pandey, Rachel Bawden, Thomas Wang, Trishala Neeraj, Jos Rozen, Abheesht Sharma, Andrea Santilli, Thibault Févry, Jason Alan Fries, Ryan Teehan, Stella Rose Biderman, Leo Gao, Tali Bers, Thomas Wolf, and Alexander M. Rush. 2022. Multitask prompted training enables zero-shot task generalization . In Proc. of ICLR .

Sellam et al. (2020) Thibault Sellam, Dipanjan Das, and Ankur P Parikh. 2020. BLEURT: Learning robust metrics for text generation . In Proc. of ACL .

Sen et al. (2008) Prithviraj Sen, Galileo Namata, Mustafa Bilgic, Lise Getoor, Brian Galligher, and Tina Eliassi-Rad. 2008. Collective classification in network data . AI magazine .

Silva et al. (2018) Rodrigo FG Silva, Klérisson Paixão, and Marcelo de Almeida Maia. 2018. Duplicate question detection in stack overflow: A reproducibility study . In Proc. of SANER .

Su et al. (2022) Hongjin Su, Jungo Kasai, Chen Henry Wu, Weijia Shi, Tianlu Wang, Jiayi Xin, Rui Zhang, Mari Ostendorf, Luke Zettlemoyer, Noah A. Smith, and Tao Yu. 2022. Selective annotation makes language models better few-shot learners .

Thakur et al. (2021) Nandan Thakur, Nils Reimers, Andreas Rücklé, Abhishek Srivastava, and Iryna Gurevych. 2021. BEIR: A heterogeneous benchmark for zero-shot evaluation of information retrieval models . In Proc. of NeurIPS .

Thorne et al. (2018) James Thorne, Andreas Vlachos, Christos Christodoulopoulos, and Arpit Mittal. 2018. Fever: a large-scale dataset for fact extraction and verification . In Proc. of NAACL .

van der Maaten and Hinton (2008) Laurens van der Maaten and Geoffrey Hinton. 2008. Visualizing data using t-SNE . JMLR .

Wang and Komatsuzaki (2021) Ben Wang and Aran Komatsuzaki. 2021. GPT-J-6B: A 6 Billion Parameter Autoregressive Language Model. https://github.com/kingoflolz/mesh-transformer-jax .

Wang et al. (2022a) Liang Wang, Nan Yang, Xiaolong Huang, Binxing Jiao, Linjun Yang, Daxin Jiang, Rangan Majumder, and Furu Wei. 2022a. Text embeddings by weakly-supervised contrastive pre-training.

Wang et al. (2022b) Yizhong Wang, Swaroop Mishra, Pegah Alipoormolabashi, Yeganeh Kordi, Amirreza Mirzaei, Anjana Arunkumar, Arjun Ashok, Arut Selvan Dhanasekaran, Atharva Naik, David Stap, Eshaan Pathak, Giannis Karamanolakis, Haizhi Gary Lai, Ishan Purohit, Ishani Mondal, Jacob Anderson, Kirby Kuznia, Krima Doshi, Maitreya Patel, Kuntal Kumar Pal, Mehrad Moradshahi, Mihir Parmar, Mirali Purohit, Neeraj Varshney, Phani Rohitha Kaza, Pulkit Verma, Ravsehaj Singh Puri, Rushang Karia, Shailaja Keyur Sampat, Savan Doshi, Siddhartha Mishra, Sujan Reddy, Sumanta Patro, Tanay Dixit, Xudong Shen, Chitta Baral, Yejin Choi, Hannaneh Hajishirzi, Noah A. Smith, and Daniel Khashabi. 2022b. Super-NaturalInstructions: Generalization via declarative instructions on 1600+ NLP tasks . In Proc. of EMNLP .

Wei et al. (2022) Jason Wei, Maarten Bosma, Vincent Zhao, Kelvin Guu, Adams Wei Yu, Brian Lester, Nan Du, Andrew M. Dai, and Quoc V. Le. 2022. Finetuned language models are zero-shot learners . In Proc. of ICLR .

Williams et al. (2018) Adina Williams, Nikita Nangia, and Samuel Bowman. 2018. A broad-coverage challenge corpus for sentence understanding through inference . In Proc. of NAACL .

Yang et al. (2018) Zhilin Yang, Peng Qi, Saizheng Zhang, Yoshua Bengio, William W. Cohen, Ruslan Salakhutdinov, and Christopher D. Manning. 2018. HotpotQA: A dataset for diverse, explainable multi-hop question answering . In Proc. of EMNLP .

Young et al. (2014) Peter Young, Alice Lai, Micah Hodosh, and Julia Hockenmaier. 2014. From image descriptions to visual denotations: New similarity metrics for semantic inference over event descriptions . TACL .

Zhang et al. (2020) Tianyi Zhang, Varsha Kishore, Felix Wu, Kilian Q. Weinberger, and Yoav Artzi. 2020. BERTScore: Evaluating text generation with BERT . In Proc. of ICLR .

Zhang et al. (2015) Xiang Zhang, Junbo Zhao, and Yann LeCun. 2015. Character-level convolutional networks for text classification . In Proc. of NeurIPS .

Zhong et al. (2021) Ruiqi Zhong, Kristy Lee, Zheng Zhang, and Dan Klein. 2021. Adapting language models for zero-shot learning by meta-tuning on dataset and prompt collections . In Findings of the ACL: EMNLP 2021 .

Zhou et al. (2022) Chunting Zhou, Junxian He, Xuezhe Ma, Taylor Berg-Kirkpatrick, and Graham Neubig. 2022. Prompt consistency for zero-shot task generalization .

## Appendix A Training Setups

#### Minibatch Sampling

Training is performed on a combination of all training datasets in MEDI. Since the number of examples in each dataset is different in orders of magnitude, we downsample large ones. Details for the downsampled numbers of examples on each dataset are shown in Table 5 in the appendix. At each step, we first randomly select a dataset and then construct a minibatch only using the examples from that dataset. In this way, we ensure that in-batch negatives are sampled from the same dataset, thereby preventing the model from using task differences to predict the negative label. We use the maximum batch size that fits the machine memory and run all our experiments on 40GB A100 GPUs.

#### Training

We initialize InstructOR with the GTR-Large model ( Ni et al., 2021 , 335M parameters) 4 4 4 https://huggingface.co/sentence-transformers/gtr-t5-large . and finetune it on MEDI using the AdamW optimizer with learning rate 2 × 10 − 5 2\times 10^{-5} and warmup ratio 0.1. We use a softmax temperature of 0.01 and finetune InstructOR for 20K steps.

#### Baselines

We use the official MTEB benchmark for comparisons, but here we highlight several strong baselines with the following two types. The first class of baselines is embedding models specializing in information retrieval: Contriever-MS Izacard et al. (2022) , GTR Ni et al. (2021) , and coCondenser-MS Gao and Callan (2022) . They are all trained on open-domain QA datasets such as MS MARCO Bajaj et al. (2016) . The second class of baselines focuses on semantic textual similarity: SimCSE Gao et al. (2021) , Sent-T5 Ni et al. (2022) , and SGPT-NLI Muennighoff (2022) . They are mainly trained on symmetric paraphrase datasets such as NLI Williams et al. (2018) and the Quora question pairs. 5 5 5 https://www.quora.com/q/quoradata/ . All of these baselines are based on pretrained language models, achieving strong performance on the MTEB leaderboard. In particular, Sent-T5-XXL and GTR-XXL (both with 4.8B parameters) achieve the first and second best average performances.

## Appendix B Embedding Evaluations

Here we provide a high-level summary of the evaluation tasks (Table 1 ). Following MTEB Muennighoff et al. (2022) , Billboard Kasai et al. (2022a) , and prompt retrieval Su et al. (2022) , we split 70 evaluation datasets into 9 categories by task objectives. Out of the 70 evaluation tasks, 66 are unseen during training (See Table 5 for datasets included during training), Table 1 for examples and instructions for the evaluation datasets.

### B.1 Massive Text Embedding Benchmark

MTEB Muennighoff et al. (2022) is a comprehensive embedding evaluation benchmark that aims to provide a holistic view of current embedding models’ performance and to discover universal text embeddings applicable to a wide range of tasks. It combines several conventional benchmarks (e.g., BEIR, Thakur et al., 2021 , and STS, Cer et al., 2017 ) and spans a wide range of domain-specific datasets, including science, biology, and medicine. Following Muennighoff et al. (2022) , we also report the average performance over 56 datasets. For each task family, we briefly describe the task objective, evaluation metric, and how embeddings are used.

#### Retrieval

Given a query q q and a corpus D = { p 1 , p 2 ​ … ​ p n } D=\{p_{1},p_{2}...p_{n}\} , retrieval aims to find the most relevant documents p i p_{i} in D D for query q q . The embedding model is used to embed q q and p 1 ​ … ​ p n p_{1}...p_{n} into fixed-sized vectors, and then the similarity between q q and p i p_{i} is measured by their embedding cosine similarity. There are 14 diverse datasets (e.g., Natural Questions, Scifact, and NFCorpus) together with the community question-answering (CQA) benchmark Hoogeveen et al. (2015) . We use NDCG@10 (Normalized Discounted cumulative gain at rank position 10) to measure the performance.

#### Reranking

Reranking ranks a list of documents based on their relevance to a query. Given a query q q and a list of documents D = { p 1 , p 2 ​ … ​ p n } D=\{p_{1},p_{2}...p_{n}\} , the embedding model computes embeddings of both the query and documents, which are then used to rank the documents based on their cosine similarities. We use MAP (mean average precision), a standard metric in reranking, to measure performance.

#### Clustering

The goal of clustering is to group similar documents into meaningful clusters. Given a set of documents, the encoder maps each document into an embedding. The k-means clustering algorithm is then used to partition the embedded documents into clusters. The clustering performance is measured by the v-measure that is independent of the permutations of clustering labels Rosenberg and Hirschberg (2007) .

#### Pair Classification

Pair classification tasks aim to predict a binary label for a pair of texts. An example of this task is paraphrase identification, where the goal is to predict whether two sentences are paraphrases of each other. Given a sentence pair ( t 1 , t 2 ) (t_{1},t_{2}) , the embedding model encodes t 1 t_{1} and t 2 t_{2} separately. The cosine similarity between the two embeddings is then used to predict the label. The average precision score is measured for evaluation.

#### Classification

Classification is a popular way to evaluate the quality of embeddings Conneau and Kiela (2018) . For each example in the classification dataset, the embedding of the input text is used as features to a classifier. The classifier is trained on the training data while sentence embedings are kept frozen. We report the classification accuracy on the test set as the evaluation metric.

#### STS

Semantic textual similarity (STS) tasks evaluate the similarity between two sentences. Given a sentence pair ( t 1 , t 2 ) (t_{1},t_{2}) , the embedding model maps t 1 t_{1} and t 2 t_{2} into embeddings separately, and then the similarity between t 1 t_{1} and t 2 t_{2} is measured by their embedding cosine similarity. The evaluation metric is Spearman’s rank correlation, which measures the correlation between the similarity scores and human judgements.

#### Summarization

Automatic summarization evaluation aims to evaluate the quality of a machine-generated summary given a reference summary. While human evaluations are considered more accurate, automatic evaluations allow for fast, inexpensive development cycles Khashabi et al. (2022) . Given a reference summary r r and a machine-generated summary t t , the embedding model maps them into embeddings separately, and we compute the cosine similarity between r r and t t . Spearman’s rank correlation is reported between human judgements and automatic scores.

### B.2 Prompt Retrieval

Large language models have demonstrated the ability of in-context learning, where the model can perform downstream tasks by conditioning generation on a few task demonstrations Liu et al. (2021) . Su et al. (2022) introduce the prompt retrieval task, where the goal is to retrieve a few in-context learning (i.e., demonstration) examples from annotated examples given a test instance. The embedding model is used to encode all annotated examples and to find the few most similar examples to the test instance based on the cosine similarity. Following Su et al. (2022) , we use the retrieved examples for in-context learning on GPT-J Wang and Komatsuzaki (2021) over 11 diverse downstream tasks (e.g., classification, multiple choice, and text-to-SQL) that are not included in MEDI (thus zero-shot settings). We compare different embedding methods by measuring the average performance on these downstream tasks.

### B.3 Automatic Evaluation for Generation

Similar to summarization evaluation in MTEB, we use the Billboard benchmark Kasai et al. (2022a) to apply InstructOR to automatic evaluations for three additional text generation tasks: MSCOCO image captioning Lin et al. (2014) ; Kasai et al. (2022b) , CNN/DailyMail news summarization Fabbri et al. (2021) , and WMT21 Chinese-to-English translation Barrault et al. (2020) ; Freitag et al. (2021) . Following Kasai et al. (2022a) , we measure the cosine similarity between the generated text and each reference text and take the maximum similarity score over all references available Zhang et al. (2020) . We evaluate all embedding models by the Pearson correlation with the human judgments, again following Kasai et al. (2022a) . We then report the average correlation scores over the three datasets. Note that we do not use the English-to-German dataset in Billboard because our models are trained only on English data.

## Appendix C Full instructions

We list all instructions for each dataset in MEDI in Table 7 and Table 8

## Appendix D Full Results

We provide the detailed evaluation scores in MTEB, Billboard and prompt retrieval benchmarks in Table 9 & 10 .

Ando2005 , augenstein-etal-2016-stance , andrew2007scalable , rasooli-tetrault-2015 , goodman-etal-2016-noise , harper-2014-learning

## Instructions for reporting errors

We are continuing to improve HTML versions of papers, and your feedback helps enhance accessibility and mobile support. To report errors in the HTML that will help us improve conversion and rendering, choose any of the methods listed below:

Click the "Report Issue" ( ) button, located in the page header.

Tip: You can select the relevant text first, to include it in your report.

Our team has already identified the following issues . We appreciate your time reviewing and reporting rendering errors we may not have found yet. Your efforts will help us improve the HTML versions for all readers, because disability should not be a barrier to accessing research. Thank you for your continued support in championing open access for all.

Have a free development cycle? Help support accessibility at arXiv! Our collaborators at LaTeXML maintain a list of packages that need conversion , and welcome developer contributions .
