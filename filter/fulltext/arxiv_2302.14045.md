##### Report GitHub Issue

Content selection saved. Describe the issue below:

# Language Is Not All You Need: Aligning Perception with Language Models Thanks: Equal contribution. † \dagger Corresponding author.

###### Abstract

A big convergence of language, multimodal perception, action, and world modeling is a key step toward artificial general intelligence. In this work, we introduce Kosmos-1 1 1 1 Kosmos is pronounced as and means “ Cosmos ”. , a Multimodal Large Language Model (MLLM) that can perceive general modalities, learn in context (i.e., few-shot), and follow instructions (i.e., zero-shot). Specifically, we train Kosmos-1 from scratch on web-scale multimodal corpora, including arbitrarily interleaved text and images, image-caption pairs, and text data. We evaluate various settings, including zero-shot, few-shot, and multimodal chain-of-thought prompting, on a wide range of tasks without any gradient updates or finetuning. Experimental results show that Kosmos-1 achieves impressive performance on (i) language understanding, generation, and even OCR-free NLP (directly fed with document images), (ii) perception-language tasks, including multimodal dialogue, image captioning, visual question answering, and (iii) vision tasks, such as image recognition with descriptions (specifying classification via text instructions). We also show that MLLMs can benefit from cross-modal transfer, i.e., transfer knowledge from language to multimodal, and from multimodal to language. In addition, we introduce a dataset of Raven IQ test, which diagnoses the nonverbal reasoning capability of MLLMs.

The limits of my language means the limits of my world. Ludwig Wittgenstein

## 1 Introduction: From LLMs to MLLMs

Large language models (LLMs) have successfully served as a general-purpose interface across various natural language tasks [ 6 ] . The LLM-based interface can be adapted to a task as long as we are able to transform the input and output into texts. For example, the input of the summarization task is a document and the output is its summary. So we can feed the input document into the language model and then produce the generated summary.

Despite the successful applications in natural language processing, it is still struggling to natively use LLMs for multimodal data, such as image, and audio. Being a basic part of intelligence, multimodal perception is a necessity to achieve artificial general intelligence, in terms of knowledge acquisition and grounding to the real world. More importantly, unlocking multimodal input [ 48 , 21 , 50 , 1 , 3 , 31 ] greatly widens the applications of language models to more high-value areas, such as multimodal machine learning, document intelligence, and robotics.

In this work, we introduce Kosmos-1 , a Multimodal Large Language Model (MLLM) that can perceive general modalities, follow instructions (i.e., zero-shot learning), and learn in context (i.e., few-shot learning). The goal is to align perception with LLMs, so that the models are able to see and talk. To be specific, we follow MetaLM [ 21 ] to train the Kosmos-1 model from scratch. As shown in Figure 1 , a Transformer-based language model is regarded as the general-purpose interface, and perception modules are docked with the language model. We train the model on web-scale multimodal corpora, i.e., text data, arbitrarily interleaved images and texts, and image-caption pairs. In addition, we calibrate the instruction-following capability across modalities by transferring language-only data.

As shown in Table 1 , the Kosmos-1 model natively supports language, perception-language, and vision tasks. We also present some generated examples in Figure 2 and 3 . In addition to various natural language tasks, the Kosmos-1 models natively handle a wide range of perception-intensive tasks, spanning visual dialogue, visual explanation, visual question answering, image captioning, simple math equation, OCR, and zero-shot image classification with descriptions. We also build an IQ test benchmark following Raven’s Progressive Matrices [ 23 , 10 ] , which evaluates the capability of nonverbal reasoning for MLLMs. The examples show that the native support of multimodal perception enables new opportunities to apply LLMs to new tasks. Moreover, we show that MLLMs achieve better commonsense reasoning performance compared with LLMs, which indicates cross-modal transfer helps knowledge acquisition.

The key takeaways are as follows:

##### From LLMs to MLLMs.

Properly handling perception is a necessary step toward artificial general intelligence. The capability of perceiving multimodal input is critical to LLMs. First, multimodal perception enables LLMs to acquire commonsense knowledge beyond text descriptions. Second, aligning perception with LLMs opens the door to new tasks, such as robotics, and document intelligence. Third, the capability of perception unifies various APIs, as graphical user interfaces are the most natural and unified way to interact with. For example, MLLMs can directly read the screen or extract numbers from receipts. We train the Kosmos-1 models on web-scale multimodal corpora, which ensures that the model robustly learns from diverse sources. We not only use a large-scale text corpus but also mine high-quality image-caption pairs and arbitrarily interleaved image and text documents from the web.

##### Language models as general-purpose interfaces.

Following the philosophy proposed in MetaLM [ 21 ] , we regard language models as a universal task layer. Because of the open-ended output space, we are able to unify various task predictions as texts. Moreover, natural-language instructions and action sequences (such as programming language) can be well handled by language models. LLMs also serve as basic reasoners [ 57 ] , which is complementary to perception modules on complex tasks. So it is natural to align world, action, and multimodal perception with the general-purpose interface, i.e., language models.

##### New capabilities of MLLMs.

As shown in Table 1 , apart from the capabilities found in previous LLMs [ 6 , 12 ] , MLLMs enable new usages and possibilities. First, we can conduct zero- and few-shot multimodal learning by using natural language instructions and demonstration examples. Second, we observe promising signals of nonverbal reasoning by evaluating the Raven IQ test, which measures the fluid reasoning ability of humans. Third, MLLMs naturally support multi-turn interactions for general modalities, such as multimodal dialogue.

## 2 Kosmos-1 : A Multimodal Large Language Model

As shown in Figure 1 , Kosmos-1 is a multimodal language model that can perceive general modalities, follow instructions, learn in context, and generate outputs. Given the previous context, the model learns to generate texts in an auto-regressive manner. Specifically, the backbone of Kosmos-1 is a Transformer-based causal language model. Apart from text, other modalities are embedded and fed into the language model. The Transformer decoder serves as a general-purpose interface to multimodal input. We train Kosmos-1 on multimodal corpora, including monomodal data, cross-modal paired data, and interleaved multimodal data. Once the models are trained, we can directly evaluate the models in zero-shot and few-shot settings on both language tasks and multimodal tasks.

### 2.1 Input Representation

The Transformer decoder perceives general modalities in a unified way. For input format, we flatten input as a sequence decorated with special tokens. Specifically, we use <s> and </s> to denote start- and end-of-sequence. The special tokens <image> and </image> indicate the beginning and end of encoded image embeddings. For example, “ <s> document </s> ” is a text input, and “ <s> paragraph <image> Image Embedding </image> paragraph </s> ” is an interleaved image-text input. Table 21 in Appendix shows some examples of input format.

An embedding module is used to encode both text tokens and other input modalities into vectors. Then the embeddings are fed into the decoder. For input tokens, we use a lookup table to map them into embeddings. For the modalities of continuous signals (e.g., image, and audio), it is also feasible to represent inputs as discrete code and then regard them as “foreign languages” [ 50 , 52 ] . In this work, following [ 21 ] , we employ a vision encoder as the embedding module for input images. In addition, Resampler [ 1 ] is used as an attentive pooling mechanism to reduce the number of image embeddings.

### 2.2 Multimodal Large Language Models (MLLMs)

After obtaining the embeddings of an input sequence, we feed them into the Transformer-based decoder. The left-to-right causal model processes the sequence in an auto-regressive manner, which produces the next token by conditioning on past timesteps. The causal masking is used to mask out future information. A softmax \mathrm{softmax} classifier upon Transformer is used to generate tokens over the vocabulary.

MLLMs serve as general-purpose interfaces [ 21 ] that can perform interactions with both natural language and multimodal input. The framework is flexible to handle various data types, as long as we can represent input as vectors. MLLMs combine the best of two worlds. First, the language models naturally inherit the capabilities of in-context learning and instruction following. Second, perception is aligned with language models by training on multimodal corpora.

The implementation is based on the library TorchScale 2 2 2 https://github.com/microsoft/torchscale [ 35 ] , which is designed for large-scale model training. Compared with the standard Transformer architecture, we include the following modifications:

##### Magneto

We use Magneto [ 55 ] , a Transformer variant, as the backbone architecture. Magneto has better training stability and superior performance across modalities. It introduces an extra LayerNorm to each sublayer (i.e., multi-head self-attention, and feed-forward network). The method has a theoretically derived initialization method [ 54 ] to improve the optimization fundamentally, which allows us to effectively scale up the models without pain.

##### xPos

We employ xPos [ 43 ] relative position encoding for better long-context modeling. The method can better generalize to different lengths, i.e., training on short while testing on longer sequences. Moreover, xPos optimizes attention resolution so that the position information can be captured more precisely. The method xPos is efficient and effective in both interpolation and extrapolation settings.

### 2.3 Training Objective

The Kosmos-1 training is conducted on web-scale multimodal corpora, including monomodal data (e.g., text corpus), cross-modal paired data (e.g., image-caption pairs), and interleaved multimodal data (e.g., documents of arbitrarily interleaved images and texts). To be specific, we use monomodal data for representation learning. For example, language modeling with text data pretrains instruction following, in-context learning, and various language tasks. Moreover, cross-modal pairs and interleaved data learn to align the perception of general modalities with language models. Interleaved data also naturally fit in the multimodal language modeling task. We present more details of training data collection in Section 3.1 .

The models are trained with the next-token prediction task, i.e., learning to generate the next token depending on the previous context. The training objective is to maximize the log-likelihood of tokens in examples. Notice that only discrete tokens, such as text tokens, are accounted for in the training loss. Multimodal language modeling is a scalable way to train the models. More importantly, the emergence of various capabilities makes the training task favorable for downstream applications.

## 3 Model Training

### 3.1 Multimodal Training Data

The models are trained on web-scale multimodal corpora. The training datasets consist of text corpora, image-caption pairs, and interleaved data of images and texts.

##### Text Corpora

We train our model with The Pile [ 17 ] and Common Crawl (CC). The Pile is a massive English text dataset built for training large-scale language models, which is produced from a variety of data sources. We exclude data splits from GitHub, arXiv, Stack Exchange, and PubMed Central. We also include the Common Crawl snapshots (2020-50 and 2021-04) datasets, CC-Stories, and RealNews datasets [ 45 , 44 ] . The entire datasets have been purged of duplicate and near-duplicate documents, as well as filtered to exclude downstream task data. Refer to Appendix B.1.1 for detailed descriptions of training text corpora.

##### Image-Caption Pairs

The image-caption pairs are constructed from several datasets, including English LAION-2B [ 41 ] , LAION-400M [ 47 ] , COYO-700M [ 7 ] , and Conceptual Captions [ 42 , 13 ] . English LAION-2B, LAION-400M, and COYO-700M are collected from web pages of the Common Crawl web data by extracting image sources and the corresponding alt-text. Conceptual Captions are also from internet web pages. More details can be found in Appendix B.1.2 .

##### Interleaved Image-Text Data

We collect interleaved multimodal data from the Common Crawl snapshot, which is a publicly available archive of web pages. We use a filtering process to select about 71M web pages from the original 2B web pages in the snapshot. We then extract the text and images from the HTML of each selected web page. For each document, we limit the number of images to five to reduce noise and redundancy. We also randomly discard half of the documents that only have one image to increase the diversity. We provide more details about the data collection process in Appendix B.1.3 . By using this corpus, we enable Kosmos-1 to handle interleaved text and image and improve its few-shot ability.

### 3.2 Training Setup

The MLLM component has 24 layers with 2,048 hidden dimensions, 8,192 FFN intermediate size, and 32 attention heads, resulting in about 1.3B parameters. We use Magneto’s initialization for optimization stability. For faster convergence, the image representation is obtained from a pretrained CLIP ViT-L/14 model with 1,024 feature dimensions. The images are preprocessed into 224 × \times 224 resolution during training. We freeze the parameters of the CLIP model except for the last layer during training. The total number of parameters of Kosmos-1 is about 1.6B. More details about hyperparameters can be found in Appendix A .

We use a batch size of 1.2 million tokens (0.5 million tokens from text corpora, 0.5 million tokens from image-caption pairs, and 0.2 million tokens from interleaved data) and train Kosmos-1 for 300k steps, corresponding to about 360 billion tokens. We adopt the AdamW optimizer with β = ( 0.9 , 0.98 ) \beta=(0.9,0.98) . We set the weight decay to 0.01 and the dropout rate to 0.1. The learning rate increases to 2e-4 for the first 375 warming-up steps and decays linearly to 0 for the rest of the training steps. We use SentencePiece [ 26 ] to tokenize the text. We preprocess the data in the “full-sentence” format [ 33 ] , which packs each input sequence with full sentences that are sampled continuously from one or more documents.

### 3.3 Language-Only Instruction Tuning

In order to better align Kosmos-1 with human instructions, we perform language-only instruction tuning [ 30 , 22 ] . Specifically, we continue-train the model with the instruction data in the format of (instructions, inputs, and outputs). The instruction data is language-only, which is mixed with training corpora. The tuning process is conducted as language modeling. Notice that instructions and inputs are not accounted for in the loss. Section 4.9.1 shows that the improvements in the instruction-following capability can transfer across modalities.

We combine Unnatural Instructions [ 22 ] and FLANv2 [ 30 ] as our instruction dataset. Unnatural Instructions is a dataset that was created by using a large language model to generate instructions for various natural language processing tasks. It has 68,478 instruction-input-output triplets in its core dataset. FLANv2 is a collection of datasets that cover diverse types of language understanding tasks, such as reading comprehension, commonsense reasoning, and closed-book question answering. We randomly select 54k examples of instructions from FLANv2 to augment our instruction dataset. Details of the training hyperparameter settings are described in Appendix A.2 .

## 4 Evaluation

MLLMs can handle both language tasks and perception-intensive tasks. We evaluate Kosmos-1 on various types of tasks as follows:

• Language tasks – Language understanding

– Language generation

– OCR-free text classification

• Cross-modal transfer – Commonsense reasoning

• Nonverbal reasoning – IQ Test (Raven’s Progressive Matrices)

• Perception-language tasks – Image captioning

– Visual question answering

– Web page question answering

• Vision tasks – Zero-shot image classification

– Zero-shot image classification with descriptions

### 4.1 Perception-Language Tasks

We evaluate the perception-language capability of Kosmos-1 under vision-language settings. Specifically, we conduct zero-shot and few-shot experiments on two widely used tasks, including image captioning and visual question answering. Image captioning involves generating a natural language description of an image, while visual question answering aims to answer a natural language question with respect to an image.

#### 4.1.1 Evaluation Setup

We evaluate the caption generation on MS COCO Caption [ 32 ] , and Flickr30k [ 60 ] . We use the test set of COCO Karpathy split [ 24 ] , which re-partitions the train2014 and val2014 images [ 32 ] into 113,287, 5,000, and 5,000 for the training set, validation set, and test set, respectively. We conduct an evaluation on Flickr30k’s Karpathy split test set. The image resolution is 224 × \times 224. We use beam search to generate the captions, and the beam size is 5. In the few-shot settings, we randomly sample demonstrations from the training set. We use COCOEvalCap 3 3 3 https://github.com/salaniz/pycocoevalcap to compute CIDEr [ 49 ] and SPICE [ 2 ] scores as the evaluation metrics. We prompt Kosmos-1 with “An image of” for zero-shot and few-shot caption generation experiments.

For visual question-answering tasks, we evaluate zero-shot and few-shot results on test-dev set of VQAv2 [ 18 ] and test-dev set of VizWiz [ 19 ] , respectively. The resolution of images is 224 × \times 224. We use greedy search for the decoding. We follow the normalization rules of the VQAv2 evaluation code 4 4 4 https://github.com/GT-Vision-Lab/VQA when computing the VQA accuracy. We evaluate the performance of VQA in an open-ended setting that Kosmos-1 generates answers and stops at the </s> (“end of sequence”) token. The prompt is “Question: { question } Answer: { answer } ” for visual question answering tasks.

#### 4.1.2 Results

##### Image Captioning

Table 2 shows the zero-shot captioning performance on COCO Karpathy test split and Flickr30k test set. Kosmos-1 achieves remarkable results in zero-shot setting on two image captioning datasets. Specifically, our model achieves a CIDEr score of 67.1 on the Flickr30k dataset, compared to 60.6 and 61.5 for the Flamingo-3B and Flamingo-9B models, respectively. Notably, our model is able to accomplish this feat with a smaller size of 1.6B, compared to Flamingo models. This demonstrates our model’s superiority in zero-shot image captioning.

Table 3 reports the results of the few-shot ( k = 2 , 4 , 8 k=2,4,8 ) settings. The overall performance improves as the number of shots increases from two to four. The trends are consistent across the two datasets. Moreover, the few-shot results outperform zero-shot captioning in Table 2 .

##### Visual Question Answering

Table 4 reports the zero-shot visual question answering results on VQAv2 and VizWiz. We show that Kosmos-1 can better handle the diversity and complexity of the VizWiz dataset. Kosmos-1 achieves higher accuracy and robustness than Flamingo-3B and Flamingo-9B models. In addition, our model is competitive with Flamingo on the VQAv2 dataset.

Table 5 shows the few-shot performance on visual question answering tasks. Kosmos-1 outperforms other models in few-shot ( k = 2 , 4 k=2,4 ) settings on the VizWiz dataset. We also observe a positive correlation between the number of shots and the quality of the results on the VizWiz dataset. Moreover, the few-shot results are better than the zero-shot numbers as reported in Table 4 .

### 4.2 IQ Test: Nonverbal Reasoning

Raven’s Progressive Matrices [ 10 , 23 ] is one of the most common tests to evaluate nonverbal reasoning. The capability of nonverbal reasoning is typically a reflection of an individual’s intelligence quotient (IQ). Figure 4 shows an example. Given eight images presented in a 3 × 3 3\times 3 matrix, the task is to identify the following element from six similar candidates.

The models need to conduct zero-shot nonverbal reasoning without explicitly fine-tuning. The Raven IQ test is analogous to in-context learning of language models, where the difference is whether the context is nonverbal or verbal. In order to infer the answers, the models have to recognize abstract concepts and identify the underlying patterns of given images. So the IQ task is a good testbed to benchmark the nonverbal in-context learning capability.

#### 4.2.1 Evaluation Setup

To evaluate the Kosmos-1 on zero-shot nonverbal reasoning, we construct a dataset of the Raven IQ test. It consists of 50 50 examples collected from different websites 5 5 5 https://en.testometrika.com/intellectual/iq-test/ 6 6 6 https://en.testometrika.com/intellectual/iq-test-for-kids-7-to-16-year-old/ 7 7 7 https://iqpro.org/ 8 8 8 https://iqhaven.com/matrix-g . Each example has three (i.e., 2 × 2 2\times 2 matrix), four, or eight (i.e., 3 × 3 3\times 3 matrix) given images. The goal is to predict the next one. Each instance has six candidate images with a unique correct completion. We measure accuracy scores to evaluate the models. The evaluation dataset is available at https://aka.ms/kosmos-iq50 .

Figure 4 illustrates how to evaluate Kosmos-1 on the Raven IQ test. The matrix-style images are flattened and fed into the models one-by-one. To enable the model to better understand the desired task, we also use a textual instruction “Here are three/four/eight images:” , “The following image is:” , and “Is it correct?” for conditioning. We append each possible candidate to the context separately and compare the probability that the model outputs “Yes” in a close-ended setting. The candidate that yields the largest probability is regarded as the prediction.

#### 4.2.2 Results

Table 6 shows the evaluation results on the IQ test dataset. Both Kosmos-1 with and without language-only instruction tuning achieve 5.3% and 9.3% improvement respectively over the random baseline. The results indicate that Kosmos-1 is able to perceive abstract conceptual patterns in a nonverbal context, and then deduce the following element across multiple choices. To the best of our knowledge, it is the first time that a model can perform such zero-shot Raven IQ tests. Although there is still a large performance gap between the current model and the average level of adults, Kosmos-1 demonstrates the potential of MLLMs to perform zero-shot nonverbal reasoning by aligning perception with language models.

### 4.3 OCR-Free Language Understanding

OCR-free language understanding is a task that focuses on understanding text and images without relying on Optical Character Recognition (OCR). For example, during the Rendered SST-2 task, sentences from the Stanford Sentiment Treebank [ 46 ] dataset are rendered as images. The model is asked to predict the sentiment of the text within the images. The task evaluates a model’s ability to read and comprehend the meaning of words and sentences directly from the images.

#### 4.3.1 Evaluation Setup

We evaluate OCR-free language understanding on the Rendered SST-2 [ 38 ] test set and HatefulMemes [ 25 ] validation set. We use accuracy as the metric for the Rendered SST-2 and report ROC AUC for the HatefulMemes dataset. We use the prompt “Question: what is the sentiment of the opinion? Answer: { answer } ” , where the answer is either positive or negative for the Rendered SST-2. For the HatefulMemes task, the prompt is “Question: does this picture contain real hate speech? Answer: { answer } ” , where the answer is either yes or no.

#### 4.3.2 Results

As shown in Table 7 , Kosmos-1 achieves a ROC AUC of 63.9% for the HatefulMemes validation set and a test accuracy of 67.1% for the Rendered SST-2 test set. It outperforms CLIP ViT-L and Flamingo-9B, which achieve AUCs of 63.3% and 57.0% on the HatefulMemes task. Note that Flamingo explicitly provides OCR text into the prompt, while Kosmos-1 does not access any external tools or resources. This indicates that Kosmos-1 has built-in abilities to read and comprehend the text in the rendered images.

### 4.4 Web Page Question Answering

Web page question answering aims at finding answers to questions from web pages. It requires the model to comprehend both the semantics and the structure of texts. The structure of the web page (such as tables, lists, and HTML layout) plays a key role in how the information is arranged and displayed. The task can help us evaluate our model’s ability to understand the semantics and the structure of web pages.

#### 4.4.1 Evaluation Setup

We compare the performance on the Web-based Structural Reading Comprehension (WebSRC) dataset [ 14 ] . For comparisons, we train a language model ( LLM ) on the same text corpora with the same training setup as in Kosmos-1 . The LLM takes the text extracted from the web page as input. Its template of the prompt is “Given the context below from web page, extract the answer from the given text like this: Qusestion: Who is the publisher of this book? Answer: Penguin Books Ltd. Context: { WebText } Q: { question } A: { answer } ” , where the { WebText } presents the text extracted from the web page. Besides using the same prompt, Kosmos-1 prepends the image before the prompt. Two example images from WebSRC are shown in Appendix C.3 . Following the original paper [ 14 ] , we use exact match (EM) and F1 scores as our evaluation metrics.

#### 4.4.2 Results

The experimental results are summarized in Table 8 . We observe that Kosmos-1 outperforms the LLM , indicating that Kosmos-1 can benefit from the layout and style information of web pages in images. In addition, we evaluate the performance of Kosmos-1 without the extracted text in the prompt. It shows that extracted text has a contribution of +12.0/20.7 EM/F1 to Kosmos-1 , indicating that the benefit from modeling images does not sacrifice its language abilities.

### 4.5 Multimodal Chain-of-Thought Prompting

Chain-of-thought prompting [ 57 ] allows large language models to generate a series of reasoning steps and decompose a multi-step problem into intermediate steps, which can significantly improve the performance in complex tasks. Motivated by chain-of-thought prompting, we investigate a multimodal chain-of-thought prompting using Kosmos-1 . As illustrated in Figure 5 , we break down perception-language tasks into two steps. In the first stage, given an image, we use a prompt to guide the model to generate a rationale. The model is then fed the rationale and a task-aware prompt to produce the final results.

#### 4.5.1 Evaluation Setup

We evaluate the ability of multimodal chain-of-thought prompting on the Rendered SST-2. We use the prompt “Introduce this picture in detail:” to generate the content in the picture as the rationale. Then, we use the prompt “ { rationale } Question: what is the sentiment of the opinion? Answer: { answer } ” to predict the sentiment, where the answer is either positive or negative.

#### 4.5.2 Results

We conduct experiments to evaluate the performance of the multimodal chain-of-thought prompting. Table 9 shows that multimodal chain-of-thought prompting achieves a score of 72.9, which is 5.8 points higher than the standard prompting. By generating intermediate content, the model can recognize the text in the images and infer the sentiment of the sentences more correctly.

### 4.6 Zero-Shot Image Classification

We report the zero-shot image classification performance on ImageNet [ 15 ] . Image classification comprehends an entire image as a whole and aims to assign a label to the image. We map each label to its category name in natural language. The model is prompted to predict the category name to perform zero-shot image classification.

#### 4.6.1 Evaluation Setup

Given an input image, we concatenate the image with the prompt “The photo of the” . The input is then fed into the model to obtain the category name of the image. We evaluate the model on ImageNet [ 15 ] , which contains 1.28M training images and 50k validation images in 1k object categories. The prediction is classified as correct if it is exactly the same as the ground-truth category name. The image resolution used for evaluation is 224 × \times 224. We use beam search to generate the category names and the beam size is 2.

#### 4.6.2 Results

As shown in Table 10 , we report zero-shot results in both constrained and unconstrained settings. The difference between the two settings is whether we use the 1k object category names to constrain the decoding. Kosmos-1 significantly outperforms GIT [ 58 ] by 4.6% under the constrained setting and 2.1% under the unconstrained setting.

### 4.7 Zero-Shot Image Classification with Descriptions

The standard approach of image classification as above is to prompt the model for the specific name of the object depicted in the image. However, there are also some classification rules customized for different users and scenarios, such as the refined classification of complex animal subspecies. We can utilize natural language descriptions to guide Kosmos-1 to distinguish images in the zero-shot setting, which makes the decision process more interpretable.

#### 4.7.1 Evaluation Setup

Following CUB [ 51 ] , we construct a bird classification dataset that contains images and natural-language descriptions of categories. The dataset has three groups of binary image classification. Each group contains two animal categories with similar appearances. Our goal is to classify images given the categories’ descriptions. Table 11 presents the data samples. The first group is from [ 51 ] , while the other two groups are collected from the website. Each category contains twenty images.

The evaluation procedure is illustrated in Figure 6 . For the zero-shot setting, we provide detailed descriptions of two specific categories and use the template “Question:what is the name of { general category } in the picture? Answer:” to prompt the model for the specific category name in an open-ended manner. To evaluate the effect of providing verbal descriptions in context, we also implement a zero-shot baseline without prompting descriptions. Instead, we provide the corresponding specific names in the prompt.

#### 4.7.2 Results

The evaluation results are shown in Table 12 . We observe that providing descriptions in context can significantly improve the accuracy of image classification. The consistent improvements indicate that Kosmos-1 can perceive the intentions of instructions and well align the concepts in language modality with visual features in vision modality.

### 4.8 Language Tasks

The models are evaluated on the language tasks given task instructions (i.e., zero-shot) or several demonstration examples (i.e., few-shot). Text inputs are directly fed into the models as in vanilla language models.

#### 4.8.1 Evaluation Setup

We train a language model ( LLM ) baseline with the same text corpora and training setup. We evaluate Kosmos-1 and the LLM baseline on eight language tasks, including cloze and completion tasks (i.e, StoryCloze, HellaSwag), Winograd-style tasks (i.e, Winograd, Winogrande), commonsense reasoning (i.e, PIQA), and three datasets BoolQ, CB, and COPA from the SuperGLUE benchmark [ 56 ] . The detailed descriptions of these datasets are provided in Appendix C.2 . We conduct experiments under zero-shot and few-shot settings. We evaluate each test example by randomly sampling examples from the training set as demonstrations. We set the number of shots to 0, 1, and 4 in our experiments.

#### 4.8.2 Results

Table 13 presents the in-context learning performance of language tasks. Kosmos-1 achieves comparable or even better performance in cloze completion and commonsense reasoning tasks when compared to LLM . In terms of the average result across all these datasets, LLM performs better in zero-shot and one-shot settings, whereas our model performs better in few-shot ( k = 4 k=4 ) settings. The results indicate that Kosmos-1 also handles language-only tasks well and achieves favorable performance across datasets. In addition, Section 4.9.2 shows that MLLMs learn better visual commonsense knowledge compared with LLMs.

### 4.9 Cross-modal Transfer

Cross-modal transferability allows a model to learn from one modality (such as text, image, audio, etc.) and transfer the knowledge to the other modalities. This skill can enable a model to perform various tasks across different modalities. In this part, we evaluate the cross-model transferability of Kosmos-1 on several benchmarks.

#### 4.9.1 Transfer from Language to Multimodal: Language-Only Instruction Tuning

To evaluate the effect of language-only instruction tuning, we conduct an ablation study using four datasets: COCO, Flickr30k, VQAv2, and VizWiz. These datasets consist of image captioning and visual questions anwsering. The evaluation metrics are: CIDEr scores for COCO/Flickr30k and VQA accuracy for VQAv2/VizWiz.

Table 14 shows the experimental results. Language-only instruction tuning boosts our model’s performance by 1.9 points on Flickr30k, 4.3 points on VQAv2, and 1.3 points on VizWiz. Our experiments show that language-only instruction tuning can significantly improve the model’s instruction-following capabilities across modalities. The results also indicate that our model can transfer the instruction-following capability from language to other modalities.

#### 4.9.2 Transfer from Multimodal to Language: Visual Commonsense Reasoning

Visual commonsense reasoning tasks require an understanding of the properties of everyday objects in the real world, such as color, size, and shape. These tasks are challenging for language models because they may require more information about object properties than what is available in texts. To investigate the visual commonsense capabilities, we compare the zero-shot performance of Kosmos-1 and LLM on visual commonsense reasoning tasks.

##### Evaluation Setup

We compare Kosmos-1 and the LLM baseline on three object commonsense reasoning datasets, RelativeSize [ 5 ] , MemoryColor [ 36 ] and ColorTerms [ 4 ] datasets. Table 15 shows some examples of object size and color reasoning tasks. RelativeSize contains 486 object pairs from 41 physical objects. The model is required to predict the size relation between two objects in a binary question-answering format with “Yes”/“No” answers. MemoryColor and ColorTerms require the model to predict the color of objects from a set of 11 color labels in a multiple-choice format. We use only text as our input and do not include any images. We measure the accuracy of our model on these three datasets.

##### Results

Table 16 presents the zero-shot performance of Kosmos-1 and LLM on visual commonsense reasoning tasks. Kosmos-1 significantly outperforms LLM by 1.5% on RelativeSize , 14.7% on MemoryColor , and 9.7% on ColorTerms dataset. The consistent improvements indicate that Kosmos-1 benefits from the visual knowledge to complete the corresponding visual commonsense reasoning. The reason for Kosmos-1 ’s superior performance is that it has modality transferability, which enables the model to transfer visual knowledge to language tasks. On the contrary, LLM has to rely on textual knowledge and clues to answer visual commonsense questions, which limits its ability to reason about object properties.

## 5 Conclusion

In this work, we introduce Kosmos-1 , a multimodal large language model that can perceive general modalities, follow instructions, and perform in-context learning. The models trained on web-scale multimodal corpora achieve promising results across a wide range of language tasks and multimodal tasks. We show that going from LLMs to MLLMs enables new capabilities and opportunities. In the future, we would like to scale up Kosmos-1 in terms of model size [ 35 , 55 , 9 ] , and integrate the speech [ 52 ] capability into Kosmos-1 . In addition, Kosmos-1 can be used as a unified interface for multimodal learning, e.g., enabling using instructions and examples to control text-to-image generation.

## References

[1] Jean-Baptiste Alayrac, Jeff Donahue, Pauline Luc, Antoine Miech, Iain Barr, Yana Hasson, Karel Lenc, Arthur Mensch, Katherine Millican, Malcolm Reynolds, Roman Ring, Eliza Rutherford, Serkan Cabi, Tengda Han, Zhitao Gong, Sina Samangooei, Marianne Monteiro, Jacob Menick, Sebastian Borgeaud, Andrew Brock, Aida Nematzadeh, Sahand Sharifzadeh, Mikolaj Binkowski, Ricardo Barreira, Oriol Vinyals, Andrew Zisserman, and Karen Simonyan. Flamingo: a visual language model for few-shot learning. In Advances in Neural Information Processing Systems , 2022.

[2] Peter Anderson, Basura Fernando, Mark Johnson, and Stephen Gould. Spice: Semantic propositional image caption evaluation. In ECCV , pages 382–398, 2016.

[3] Armen Aghajanyan, Bernie Huang, Candace Ross, Vladimir Karpukhin, Hu Xu, Naman Goyal, Dmytro Okhonko, Mandar Joshi, Gargi Ghosh, Mike Lewis, and Luke Zettlemoyer. CM3: A causal masked multimodal model of the Internet. ArXiv , abs/2201.07520, 2022.

[4] Elia Bruni, Gemma Boleda, Marco Baroni, and Nam Khanh Tran. Distributional semantics in technicolor. In ACL , 2012.

[5] Hessam Bagherinezhad, Hannaneh Hajishirzi, Yejin Choi, and Ali Farhadi. Are elephants bigger than butterflies? reasoning about sizes of objects. ArXiv , abs/1602.00753, 2016.

[6] Tom Brown, Benjamin Mann, Nick Ryder, Melanie Subbiah, Jared D Kaplan, Prafulla Dhariwal, Arvind Neelakantan, Pranav Shyam, Girish Sastry, Amanda Askell, Sandhini Agarwal, Ariel Herbert-Voss, Gretchen Krueger, Tom Henighan, Rewon Child, Aditya Ramesh, Daniel Ziegler, Jeffrey Wu, Clemens Winter, Chris Hesse, Mark Chen, Eric Sigler, Mateusz Litwin, Scott Gray, Benjamin Chess, Jack Clark, Christopher Berner, Sam McCandlish, Alec Radford, Ilya Sutskever, and Dario Amodei. Language models are few-shot learners. In Advances in Neural Information Processing Systems , volume 33, pages 1877–1901. Curran Associates, Inc., 2020.

[7] Minwoo Byeon, Beomhee Park, Haecheon Kim, Sungjun Lee, Woonhyuk Baek, and Saehoon Kim. Coyo-700m: Image-text pair dataset, 2022.

[8] Yonatan Bisk, Rowan Zellers, Ronan Le Bras, Jianfeng Gao, and Yejin Choi. Piqa: Reasoning about physical commonsense in natural language. In Thirty-Fourth AAAI Conference on Artificial Intelligence , 2020.

[9] Zewen Chi, Li Dong, Shaohan Huang, Damai Dai, Shuming Ma, Barun Patra, Saksham Singhal, Payal Bajaj, Xia Song, Xian-Ling Mao, Heyan Huang, and Furu Wei. On the representation collapse of sparse mixture of experts. In Advances in Neural Information Processing Systems , 2022.

[10] Patricia A Carpenter, Marcel A Just, and Peter Shell. What one intelligence test measures: a theoretical account of the processing in the raven progressive matrices test. Psychological review , 97(3):404, 1990.

[11] Christopher Clark, Kenton Lee, Ming-Wei Chang, Tom Kwiatkowski, Michael Collins, and Kristina Toutanova. BoolQ: Exploring the surprising difficulty of natural yes/no questions. In Proceedings of the 2019 Conference of the North American Chapter of the Association for Computational Linguistics: Human Language Technologies, Volume 1 (Long and Short Papers) , pages 2924–2936, Minneapolis, Minnesota, June 2019. Association for Computational Linguistics.

[12] Aakanksha Chowdhery, Sharan Narang, Jacob Devlin, Maarten Bosma, Gaurav Mishra, Adam Roberts, Paul Barham, Hyung Won Chung, Charles Sutton, Sebastian Gehrmann, Parker Schuh, Kensen Shi, Sasha Tsvyashchenko, Joshua Maynez, Abhishek B Rao, Parker Barnes, Yi Tay, Noam M. Shazeer, Vinodkumar Prabhakaran, Emily Reif, Nan Du, Benton C. Hutchinson, Reiner Pope, James Bradbury, Jacob Austin, Michael Isard, Guy Gur-Ari, Pengcheng Yin, Toju Duke, Anselm Levskaya, Sanjay Ghemawat, Sunipa Dev, Henryk Michalewski, Xavier García, Vedant Misra, Kevin Robinson, Liam Fedus, Denny Zhou, Daphne Ippolito, David Luan, Hyeontaek Lim, Barret Zoph, Alexander Spiridonov, Ryan Sepassi, David Dohan, Shivani Agrawal, Mark Omernick, Andrew M. Dai, Thanumalayan Sankaranarayana Pillai, Marie Pellat, Aitor Lewkowycz, Erica Oliveira Moreira, Rewon Child, Oleksandr Polozov, Katherine Lee, Zongwei Zhou, Xuezhi Wang, Brennan Saeta, Mark Díaz, Orhan Firat, Michele Catasta, Jason Wei, Kathleen S. Meier-Hellstern, Douglas Eck, Jeff Dean, Slav Petrov, and Noah Fiedel. PaLM: Scaling language modeling with pathways. ArXiv , abs/2204.02311, 2022.

[13] Soravit Changpinyo, Piyush Sharma, Nan Ding, and Radu Soricut. Conceptual 12m: Pushing web-scale image-text pre-training to recognize long-tail visual concepts. In Proceedings of the IEEE/CVF Conference on Computer Vision and Pattern Recognition , pages 3558–3568, 2021.

[14] Xingyu Chen, Zihan Zhao, Lu Chen, JiaBao Ji, Danyang Zhang, Ao Luo, Yuxuan Xiong, and Kai Yu. WebSRC: A dataset for web-based structural reading comprehension. In Proceedings of the 2021 Conference on Empirical Methods in Natural Language Processing , pages 4173–4185, Online and Punta Cana, Dominican Republic, November 2021. Association for Computational Linguistics.

[15] Jia Deng, Wei Dong, Richard Socher, Li-Jia Li, Kai Li, and Li Fei-Fei. Imagenet: A large-scale hierarchical image database. In 2009 IEEE Computer Society Conference on Computer Vision and Pattern Recognition (CVPR 2009), 20-25 June 2009, Miami, Florida, USA , pages 248–255. IEEE Computer Society, 2009.

[16] Marie-Catherine de Marneffe, Mandy Simons, and Judith Tonhauser. The CommitmentBank: Investigating projection in naturally occurring discourse. Proceedings of Sinn und Bedeutung , 23(2):107–124, Jul. 2019.

[17] Leo Gao, Stella Biderman, Sid Black, Laurence Golding, Travis Hoppe, Charles Foster, Jason Phang, Horace He, Anish Thite, Noa Nabeshima, et al. The pile: An 800gb dataset of diverse text for language modeling. arXiv preprint arXiv:2101.00027 , 2020.

[18] Yash Goyal, Tejas Khot, Douglas Summers-Stay, Dhruv Batra, and Devi Parikh. Making the v in vqa matter: Elevating the role of image understanding in visual question answering. In CVPR , pages 6325–6334, 2017.

[19] Danna Gurari, Qing Li, Abigale J Stangl, Anhong Guo, Chi Lin, Kristen Grauman, Jiebo Luo, and Jeffrey P Bigham. Vizwiz grand challenge: Answering visual questions from blind people. In Proceedings of the IEEE conference on computer vision and pattern recognition , pages 3608–3617, 2018.

[20] Dan Hendrycks and Kevin Gimpel. Gaussian error linear units (GELUs). arXiv preprint arXiv:1606.08415 , 2016.

[21] Yaru Hao, Haoyu Song, Li Dong, Shaohan Huang, Zewen Chi, Wenhui Wang, Shuming Ma, and Furu Wei. Language models are general-purpose interfaces. ArXiv , abs/2206.06336, 2022.

[22] Or Honovich, Thomas Scialom, Omer Levy, and Timo Schick. Unnatural instructions: Tuning language models with (almost) no human labor, 2022.

[23] John and Jean Raven. Raven Progressive Matrices , pages 223–237. Springer US, Boston, MA, 2003.

[24] Andrej Karpathy and Li Fei-Fei. Deep visual-semantic alignments for generating image descriptions. IEEE Transactions on Pattern Analysis and Machine Intelligence , 39(4):664–676, 2017.

[25] Douwe Kiela, Hamed Firooz, Aravind Mohan, Vedanuj Goswami, Amanpreet Singh, Pratik Ringshia, and Davide Testuggine. The hateful memes challenge: Detecting hate speech in multimodal memes. In Advances in Neural Information Processing Systems , volume 33, pages 2611–2624, 2020.

[26] Taku Kudo and John Richardson. SentencePiece: A simple and language independent subword tokenizer and detokenizer for neural text processing. In EMNLP , pages 66–71, 2018.

[27] Jing Yu Koh, Ruslan Salakhutdinov, and Daniel Fried. Grounding language models to images for multimodal generation. arXiv preprint arXiv:2301.13823 , 2023.

[28] Hector Levesque, Ernest Davis, and Leora Morgenstern. The winograd schema challenge. In Thirteenth International Conference on the Principles of Knowledge Representation and Reasoning , 2012.

[29] Hector J. Levesque, Ernest Davis, and Leora Morgenstern. The winograd schema challenge. In Principles of Knowledge Representation and Reasoning , 2012.

[30] Shayne Longpre, Le Hou, Tu Vu, Albert Webson, Hyung Won Chung, Yi Tay, Denny Zhou, Quoc V Le, Barret Zoph, Jason Wei, et al. The flan collection: Designing data and methods for effective instruction tuning. arXiv preprint arXiv:2301.13688 , 2023.

[31] Junnan Li, Dongxu Li, Silvio Savarese, and Steven Hoi. BLIP-2: Bootstrapping language-image pre-training with frozen image encoders and large language models. ArXiv , abs/2301.12597, 2023.

[32] Tsung-Yi Lin, Michael Maire, Serge Belongie, James Hays, Pietro Perona, Deva Ramanan, Piotr Dollár, and C Lawrence Zitnick. Microsoft coco: Common objects in context. In ECCV , pages 740–755, 2014.

[33] Yinhan Liu, Myle Ott, Naman Goyal, Jingfei Du, Mandar Joshi, Danqi Chen, Omer Levy, Mike Lewis, Luke Zettlemoyer, and Veselin Stoyanov. RoBERTa: A robustly optimized bert pretraining approach. arXiv preprint arXiv:1907.11692 , 2019.

[34] Nasrin Mostafazadeh, Michael Roth, Annie Louis, Nathanael Chambers, and James Allen. Lsdsem 2017 shared task: The story cloze test. In Proceedings of the 2nd Workshop on Linking Models of Lexical, Sentential and Discourse-level Semantics , pages 46–51, 2017.

[35] Shuming Ma, Hongyu Wang, Shaohan Huang, Wenhui Wang, Zewen Chi, Li Dong, Alon Benhaim, Barun Patra, Vishrav Chaudhary, Xia Song, and Furu Wei. TorchScale: Transformers at scale. CoRR , abs/2211.13184, 2022.

[36] Tobias Norlund, Lovisa Hagström, and Richard Johansson. Transferring knowledge from vision to language: How to achieve it and how to measure it? ArXiv , abs/2109.11321, 2021.

[37] Melissa Roemmele, Cosmin Adrian Bejan, and Andrew S. Gordon. Choice of plausible alternatives: An evaluation of commonsense causal reasoning. In AAAI Spring Symposium , 2011.

[38] Alec Radford, Jong Wook Kim, Chris Hallacy, Aditya Ramesh, Gabriel Goh, Sandhini Agarwal, Girish Sastry, Amanda Askell, Pamela Mishkin, Jack Clark, et al. Learning transferable visual models from natural language supervision. In International conference on machine learning , pages 8748–8763. PMLR, 2021.

[39] Jack W. Rae, Anna Potapenko, Siddhant M. Jayakumar, Chloe Hillier, and Timothy P. Lillicrap. Compressive transformers for long-range sequence modelling. In ICLR , 2020.

[40] Keisuke Sakaguchi, Ronan Le Bras, Chandra Bhagavatula, and Yejin Choi. WinoGrande: An adversarial winograd schema challenge at scale. In AAAI , pages 8732–8740, 2020.

[41] Christoph Schuhmann, Romain Beaumont, Richard Vencu, Cade Gordon, Ross Wightman, Mehdi Cherti, Theo Coombes, Aarush Katta, Clayton Mullis, Mitchell Wortsman, et al. Laion-5b: An open large-scale dataset for training next generation image-text models. arXiv preprint arXiv:2210.08402 , 2022.

[42] Piyush Sharma, Nan Ding, Sebastian Goodman, and Radu Soricut. Conceptual captions: A cleaned, hypernymed, image alt-text dataset for automatic image captioning. In Proceedings of the 56th Annual Meeting of the Association for Computational Linguistics, ACL 2018, Melbourne, Australia, July 15-20, 2018, Volume 1: Long Papers , pages 2556–2565. Association for Computational Linguistics, 2018.

[43] Yutao Sun, Li Dong, Barun Patra, Shuming Ma, Shaohan Huang, Alon Benhaim, Vishrav Chaudhary, Xia Song, and Furu Wei. A length-extrapolatable transformer. arXiv preprint arXiv:2212.10554 , 2022.

[44] Shaden Smith, Mostofa Patwary, Brandon Norick, Patrick LeGresley, Samyam Rajbhandari, Jared Casper, Zhun Liu, Shrimai Prabhumoye, George Zerveas, Vijay Korthikanti, Elton Zhang, Rewon Child, Reza Yazdani Aminabadi, Julie Bernauer, Xia Song, Mohammad Shoeybi, Yuxiong He, Michael Houston, Saurabh Tiwary, and Bryan Catanzaro. Using DeepSpeed and Megatron to train Megatron-Turing NLG 530B, a large-scale generative language model, 2022.

[45] Mohammad Shoeybi, Mostofa Patwary, Raul Puri, Patrick LeGresley, Jared Casper, and Bryan Catanzaro. Megatron-lm: Training multi-billion parameter language models using model parallelism. arXiv preprint arXiv:1909.08053 , 2019.

[46] Richard Socher, Alex Perelygin, Jean Wu, Jason Chuang, Christopher D. Manning, Andrew Ng, and Christopher Potts. Recursive deep models for semantic compositionality over a sentiment treebank. In Proceedings of the 2013 Conference on Empirical Methods in Natural Language Processing , pages 1631–1642, Seattle, Washington, USA, October 2013. Association for Computational Linguistics.

[47] Christoph Schuhmann, Richard Vencu, Romain Beaumont, Robert Kaczmarczyk, Clayton Mullis, Aarush Katta, Theo Coombes, Jenia Jitsev, and Aran Komatsuzaki. Laion-400m: Open dataset of clip-filtered 400 million image-text pairs. arXiv preprint arXiv:2111.02114 , 2021.

[48] Maria Tsimpoukelli, Jacob Menick, Serkan Cabi, S. M. Ali Eslami, Oriol Vinyals, and Felix Hill. Multimodal few-shot learning with frozen language models. In Neural Information Processing Systems , 2021.

[49] Ramakrishna Vedantam, C Lawrence Zitnick, and Devi Parikh. Cider: Consensus-based image description evaluation. In CVPR , pages 4566–4575, 2015.

[50] Wenhui Wang, Hangbo Bao, Li Dong, Johan Bjorck, Zhiliang Peng, Qiang Liu, Kriti Aggarwal, Owais Mohammed, Saksham Singhal, Subhojit Som, and Furu Wei. Image as a foreign language: BEiT pretraining for all vision and vision-language tasks. ArXiv , abs/2208.10442, 2022.

[51] Catherine Wah, Steve Branson, Peter Welinder, Pietro Perona, and Serge J. Belongie. The caltech-ucsd birds-200-2011 dataset. 2011.

[52] Chengyi Wang, Sanyuan Chen, Yu Wu, Zi-Hua Zhang, Long Zhou, Shujie Liu, Zhuo Chen, Yanqing Liu, Huaming Wang, Jinyu Li, Lei He, Sheng Zhao, and Furu Wei. Neural codec language models are zero-shot text to speech synthesizers. ArXiv , abs/2301.02111, 2023.

[53] Weizhi Wang, Li Dong, Hao Cheng, Haoyu Song, Xiaodong Liu, Xifeng Yan, Jianfeng Gao, and Furu Wei. Visually-augmented language modeling. In International Conference on Learning Representations , 2023.

[54] Hongyu Wang, Shuming Ma, Li Dong, Shaohan Huang, Dongdong Zhang, and Furu Wei. DeepNet: Scaling Transformers to 1,000 layers. CoRR , abs/2203.00555, 2022.

[55] Hongyu Wang, Shuming Ma, Shaohan Huang, Li Dong, Wenhui Wang, Zhiliang Peng, Yu Wu, Payal Bajaj, Saksham Singhal, Alon Benhaim, Barun Patra, Zhun Liu, Vishrav Chaudhary, Xia Song, and Furu Wei. Foundation transformers. CoRR , abs/2210.06423, 2022.

[56] Alex Wang, Yada Pruksachatkun, Nikita Nangia, Amanpreet Singh, Julian Michael, Felix Hill, Omer Levy, and Samuel R Bowman. SuperGLUE: A stickier benchmark for general-purpose language understanding systems. arXiv preprint arXiv:1905.00537 , 2019.

[57] Jason Wei, Xuezhi Wang, Dale Schuurmans, Maarten Bosma, Ed Chi, Quoc Le, and Denny Zhou. Chain of thought prompting elicits reasoning in large language models. arXiv preprint arXiv:2201.11903 , 2022.

[58] Jianfeng Wang, Zhengyuan Yang, Xiaowei Hu, Linjie Li, Kevin Lin, Zhe Gan, Zicheng Liu, Ce Liu, and Lijuan Wang. GIT: A generative image-to-text transformer for vision and language. CoRR , abs/2205.14100, 2022.

[59] Michihiro Yasunaga, Armen Aghajanyan, Weijia Shi, Rich James, Jure Leskovec, Percy Liang, Mike Lewis, Luke Zettlemoyer, and Wen tau Yih. Retrieval-augmented multimodal language modeling. ArXiv , abs/2211.12561, 2022.

[60] Peter Young, Alice Lai, Micah Hodosh, and Julia Hockenmaier. From image descriptions to visual denotations: New similarity metrics for semantic inference over event descriptions. TACL , 2:67–78, 2014.

[61] Rowan Zellers, Ari Holtzman, Yonatan Bisk, Ali Farhadi, and Yejin Choi. Hellaswag: Can a machine really finish your sentence? In Proceedings of the 57th Annual Meeting of the Association for Computational Linguistics , 2019.

## Appendix A Hyperparameters

### A.1 Training

We report the detailed model hyperparameter settings of Kosmos-1 in Table 17 and training hyperparameters in Table 18 .

### A.2 Language-Only Instruction Tuning

The detailed instruction tuning hyperparameters are listed in Table 19 .

## Appendix B Datasets

### B.1 Pretraning

#### B.1.1 Text Corpora

Kosmos-1 is trained on The Pile [ 17 ] and Common Crawl. The Pile is an 800 GB English text corpus combining 22 diverse sources. We select a subset with seven sources from The Pile. Common Crawl is also included in training corpora. Common Crawl takes snapshots of the web, which contains massive amounts of language data. Table 20 provides a full overview of the language datasets that were used in the training of Kosmos-1 model. These data sources can be divided into the following three categories: • Academic : NIH Exporter

• Internet : Pile-CC, OpenWebText2, Wikipedia (English), CC-2020-50, CC-2021-04, Realnews

• Prose : BookCorpus2, Books3, Gutenberg [ 39 ] , CC-Stories

#### B.1.2 Image-Caption Pairs

Kosmos-1 is trained on image-caption pairs constructed from several datasets, including English LAION-2B [ 41 ] , LAION-400M [ 47 ] , COYO-700M [ 7 ] and Conceptual Captions [ 42 , 13 ] . LAION-2B, LAION-400M, and COYO-700M datasets are extracted by parsing out image URLs and alt-texts of web pages from the Common Crawl web data. LAION-2B contains about 2B English image-caption pairs, LAION-400M consists of 400M English image-caption pairs, and COYO-700M has 700M English image-caption pairs. Conceptual Captions contains 15M English image-caption pairs and consists of two datasets: CC3M and CC12M, which are also collected from internet webpages using a Flume pipeline. For Conceptual Captions, we discard pairs whose captions contain special tags such as “<PERSON>”.

#### B.1.3 Interleaved Data

We collect a large corpus of 2 billion web pages from the snapshots of common crawls. To ensure quality and relevance, we apply several filtering criteria. First, we discard any pages that are not written in English. Second, we discard any pages that do not have images interspersed in the text. Third, we discard any images that have a resolution lower than 64 by 64 pixels or that are single-colored. Fourth, we discard any text that is not meaningful or coherent, such as spam or gibberish. We use some heuristics to identify and remove gibberish text containing emoji symbols, hashtags, and URL links. After applying these filters, we end up with about 71 million documents for training.

### B.2 Data Format

The training data is organized in the format as follows:

## Appendix C Evaluation

### C.1 Input Format Used for Perception-Language Tasks

Figure 7 shows how we conduct zero-shot and few-shot evaluations on perception-language tasks.

### C.2 Language Tasks

We conduct experiments on language tasks in four categories: • Cloze and completion tasks: StoryCloze [ 34 ] , HellaSwag [ 61 ]

• Winograd-style tasks: Winograd [ 29 ] , Winogrande [ 40 ]

• Commonsense reasoning: PIQA [ 8 ]

• Three datasets from SuperGLUE benchmark [ 56 ] : BoolQ [ 11 ] , CB [ 16 ] , COPA [ 37 ]

### C.3 WebSRC Task Examples

3 59 48 31 27

## Instructions for reporting errors

We are continuing to improve HTML versions of papers, and your feedback helps enhance accessibility and mobile support. To report errors in the HTML that will help us improve conversion and rendering, choose any of the methods listed below:

Click the "Report Issue" ( ) button, located in the page header.

Tip: You can select the relevant text first, to include it in your report.

Our team has already identified the following issues . We appreciate your time reviewing and reporting rendering errors we may not have found yet. Your efforts will help us improve the HTML versions for all readers, because disability should not be a barrier to accessing research. Thank you for your continued support in championing open access for all.

Have a free development cycle? Help support accessibility at arXiv! Our collaborators at LaTeXML maintain a list of packages that need conversion , and welcome developer contributions .
