##### Report GitHub Issue

Content selection saved. Describe the issue below:

# Image as a Foreign Language: BEiT Pretraining for All Vision and Vision-Language Tasks

###### Abstract

A big convergence of language, vision, and multimodal pretraining is emerging. In this work, we introduce a general-purpose multimodal foundation model BEiT-3 , which achieves state-of-the-art transfer performance on both vision and vision-language tasks. Specifically, we advance the big convergence from three aspects: backbone architecture, pretraining task, and model scaling up. We introduce Multiway Transformers for general-purpose modeling, where the modular architecture enables both deep fusion and modality-specific encoding. Based on the shared backbone, we perform masked “language” modeling on images ( Imglish ), texts (English), and image-text pairs (“parallel sentences”) in a unified manner. Experimental results show that BEiT-3 obtains state-of-the-art performance on object detection (COCO), semantic segmentation (ADE20K), image classification (ImageNet), visual reasoning (NLVR2), visual question answering (VQAv2), image captioning (COCO), and cross-modal retrieval (Flickr30K, COCO).

## 1 Introduction: The Big Convergence

Recent years have featured a trend toward the big convergence of language [ 44 , 14 , 17 ] , vision [ 3 , 40 ] , and multimodal [ 53 , 43 , 62 ] pretraining. By performing large-scale pretraining on massive data, we can easily transfer the models to various downstream tasks. It is appealing that we can pretrain a general-purpose foundation model that handles multiple modalities. In this work, we advance the convergence trend for vision-language pretraining from the following three aspects.

First, the success of Transformers [ 52 ] is translated from language to vision [ 13 ] and multimodal [ 26 , 53 ] problems. The unification of network architectures enables us to seamlessly handle multiple modalities. For vision-language modeling, there are various ways to apply Transformers due to the different natures of downstream tasks. For example, the dual-encoder architecture is used for efficient retrieval [ 43 ] , encoder-decoder networks for generation tasks [ 58 ] , and the fusion-encoder architecture for image-text encoding [ 26 ] . However, most foundation models have to manually convert the end-task formats according to the specific architectures. Moreover, the parameters are usually not effectively shared across modalities. In this work, we adopt Multiway Transformers [ 53 ] for general-purpose modeling, i.e., one unified architecture shared for various downstream tasks. The modular network also comprehensively considers modality-specific encoding and cross-modality fusion.

Second, the pretraining task based on masked data modeling has been successfully applied to various modalities, such as texts [ 14 ] , images [ 3 , 40 ] , and image-text pairs [ 7 ] . Current vision-language foundation models usually multitask other pretraining objectives (such as image-text matching), rendering scaling-up unfriendly and inefficient. In contrast, we only use one pretraining task, i.e., mask-then-predict, to train a general-purpose multimodal foundation model. By regarding the image as a foreign language (i.e., Imglish ), we handle texts and images in the same manner without fundamental modeling differences. Consequentially, image-text pairs are utilized as “parallel sentences” in order to learn the alignments between modalities. We also show that the simple yet effective method learns strong transferable representations, achieving state-of-the-art performance on both vision and vision-language tasks. The prominent success demonstrates the superiority of generative pretraining [ 14 , 3 ] .

Third, scaling up the model size and data size universally improves the generalization quality of foundation models, so that we can transfer them to various downstream tasks. We follow the philosophy and scale up the model size to billions of parameters. Moreover, we scale up the pretraining data size in our experiments while only using publicly accessible resources for academic reproducibility. Although without using any private data, our method outperforms state-of-the-art foundation models that rely on in-house data by a decent margin. In addition, the scaling up benefits from treating images as a foreign language, as we can directly reuse the pipeline developed for large-scale language model pretraining.

In this work, we take advantage of the above ideas to pretrain a general-purpose multimodal foundation model BEiT-3 . We pretrain a Multiway Transformer by performing masked data modeling on images, texts, and image-text pairs. During pretraining, we randomly mask some proportion of text tokens or image patches. The self-supervised learning objective is to recover the original tokens (i.e., text tokens, or visual tokens) given corrupted inputs. The model is general-purpose in the sense that it can be repurposed for various tasks regardless of input modalities, or output formats.

As shown in Figure 1 and Table 1 , BEiT-3 achieves state-of-the-art transfer performance across a broad range of vision and vision-language tasks. We evaluate BEiT-3 on extensive downstream tasks and datasets, i.e., object detection (COCO), instance segmentation (COCO), semantic segmentation (ADE20K), image classification (ImageNet), visual reasoning (NLVR2), visual question answering (VQAv2), image captioning (COCO), and cross-modal retrieval (Flickr30K, COCO). Specifically, our model outperforms previous strong foundation models [ 62 , 1 , 60 ] despite that we only use public resources for pretraining and finetuning. The model also obtains better results than specialized models. Moreover, BEiT-3 not only performs well on vision-language tasks but also on vision tasks (such as object detection, and semantic segmentation).

## 2 BEiT-3 : A General-Purpose Multimodal Foundation Model

As shown in Figure 2 , BEiT-3 is pretrained by masked data modeling on monomodal and multimodal data, using a shared Multiway Transformer network. The model can be transferred to various vision and vision-language downstream tasks.

### 2.1 Backbone Network: Multiway Transformers

We use Multiway Transformers [ 53 ] as the backbone model to encode different modalities. As shown in Figure 2 , each Multiway Transformer block consists of a shared self-attention module, and a pool of feed-forward networks (i.e., modality experts) used for different modalities. We route each input token to the experts depending on its modality. In our implementation, each layer contains a vision expert and a language expert. Moreover, the top three layers have vision-language experts designed for fusion encoders. Refer to Figure 3 (a)(b)(c) for more detailed modeling layouts. Using a pool of modality experts encourages the model to capture more modality-specific information. The shared self-attention module learns the alignment between different modalities and enables deep fusion for multimodal (such as vision-language) tasks.

As shown in Figure 3 , the unified architecture enables BEiT-3 to support a wide range of downstream tasks. For example, BEiT-3 can be used as an image backbone for various vision tasks, including image classification, object detection, instance segmentation, and semantic segmentation. It can also be finetuned as a dual encoder for efficient image-text retrieval, and a fusion model for multimodal understanding and generation tasks.

### 2.2 Pretraining Task: Masked Data Modeling

We pretrain BEiT-3 via a unified masked data modeling [ 7 ] objective on monomodal (i.e., images, and texts) and multimodal data (i.e., image-text pairs). During pretraining, we randomly mask some percentage of text tokens or image patches and train the model to recover the masked tokens. The unified mask-then-predict task not only learns representations but also learns the alignment of different modalities. Specifically, text data is tokenized by a SentencePiece tokenizer [ 25 ] . Image data is tokenized by the tokenizer of BEiT v2 [ 40 ] to obtain the discrete visual tokens as the reconstructed targets. We randomly mask 15 15 % tokens of monomodal texts and 50 50 % tokens of texts from image-text pairs. For images, we mask 40 40 % of image patches using a block-wise masking strategy as in BEiT [ 3 , 40 ] .

We only use one pretraining task, which makes the training process scaling-up friendly. In contrast, previous vision-language models [ 36 , 65 , 26 , 34 , 53 , 30 , 62 ] usually employ multiple pretraining tasks, such as image-text contrast, image-text matching, and word-patch/region alignment. We show that a much smaller pretraining batch size can be used with the mask-then-predict task. In comparison, contrastive-based models [ 43 , 23 , 60 , 62 ] usually need a very large batch size 1 1 1 For example, CoCa [ 62 ] uses 65 65 k batch size, CLIP [ 43 ] uses 32 32 k batch size, and Florence [ 60 ] uses 24 24 k batch size. BEiT-3 uses a much smaller 6 6 k batch size for pretraining. for pretraining, which brings more engineering challenges, such as GPU memory cost.

### 2.3 Scaling Up: BEiT-3 Pretraining

#### Backbone Network

BEiT-3 is a giant-size foundation model following the setup of ViT-giant [ 63 ] . As shown in Table 2 , the model consists of a 40 40 -layer Multiway Transformer with 1408 1408 hidden size, 6144 6144 intermediate size, and 16 16 attention heads. All layers contain both vision experts and language experts. Vision-language experts are also employed in the top three Multiway Transformer layers. The self-attention module is shared across different modalities. BEiT-3 consists of 1.9 1.9 B parameters in total, including 692 692 M parameters for vision experts, 692 692 M parameters for language experts, 52 52 M parameters for vision-language experts, and 317 317 M parameters for the shared self-attention module. Notice that only vision-related parameters (i.e., comparable size as ViT-giant; about 1B) are activated when the model is used as a vision encoder.

#### Pretraining Data

BEiT-3 is pretrained on both monomodal and multimodal data shown in Table 3 . For multimodal data, there are about 15 15 M images and 21 21 M image-text pairs collected from five public datasets: Conceptual 12M (CC12M) [ 11 ] , Conceptual Captions (CC3M) [ 46 ] , SBU Captions (SBU) [ 39 ] , COCO [ 31 ] and Visual Genome (VG) [ 27 ] . For monomodal data, we use 14 14 M images from ImageNet-21K and 160 160 GB text corpora [ 4 ] from English Wikipedia, BookCorpus [ 64 ] , OpenWebText 2 2 2 http://skylion007.github.io/OpenWebTextCorpus , CC-News [ 33 ] , and Stories [ 50 ] .

#### Pretraining Settings

We pretrain BEiT-3 for 1 1 M steps. Each batch contains 6144 6144 samples in total, including 2048 2048 images, 2048 2048 texts and 2048 2048 image-text pairs. The batch size is much smaller than contrastive models [ 43 , 23 , 62 ] . BEiT-3 uses 14 × 14 14\times 14 patch size and is pretrained at resolution 224 × 224 224\times 224 . We use the same image augmentation as in BEiT [ 3 ] , including random resized cropping, horizontal flipping, and color jittering [ 56 ] . A SentencePiece tokenizer [ 25 ] with 64 64 k vocab size is employed to tokenize the text data. We use the AdamW [ 28 ] optimizer with β 1 = 0.9 \beta_{1}=0.9 , β 2 = 0.98 \beta_{2}=0.98 and ϵ = \epsilon= 1e-6 for optimization. We use a cosine learning rate decay scheduler with a peak learning rate of 1e-3 and a linear warmup of 10 10 k steps. The weight decay is 0.05 0.05 . Stochastic depth [ 21 ] with a rate of 0.1 0.1 is used. The BEiT initialization algorithm 3 3 3 We first randomly initialize the parameters within a small range, e.g., [ − 0.02 , 0.02 ] [-0.02,0.02] . Next, we rescale the l l -th Transformer layer’s output matrices (i.e., the last linear projection within each sublayer) of self-attention and FFN by 1 2 ​ l \frac{1}{\sqrt{2l}} . [ 3 ] is used to stabilize Transformer training.

## 3 Experiments on Vision and Vision-Language Tasks

We extensively evaluate BEiT-3 on major public benchmarks for both vision-language and vision tasks. Table 1 presents the overview of results. BEiT-3 obtains state-of-the-art performance on a wide range of vision and vision-language tasks.

### 3.1 Vision-Language Downstream Tasks

We evaluate the capabilities of BEiT-3 on the widely used vision-language understanding and generation benchmarks, including visual question answering [ 19 ] , visual reasoning [ 49 ] , image-text retrieval [ 41 , 31 ] , and image captioning [ 31 ] .

#### Visual Question Answering (VQA)

The task requires the model to answer natural language questions about input images. Following previous work [ 2 , 65 , 26 ] , we conduct finetuning experiments on the VQA v2.0 dataset [ 19 ] and formulate the task as a classification problem. The model is trained to predict answers from the 3129 3129 most frequent answer candidates in the training set. BEiT-3 is finetuned as a fusion encoder to model deep interactions of images and questions for the VQA task. We concatenate the embeddings of a given question and an image, and then feed the input embeddings into Multiway Transformers to jointly encode the image-question pair. The final pooled output is fed into a classifier layer to predict the answer. The results are present in Table 4 , BEiT-3 outperforms all previous models by a large margin (more than 1.7 1.7 points), pushing the state of the art to 84.03 84.03 with a single model.

#### Visual Reasoning

The task needs models to perform joint reasoning about images and natural language descriptions. We evaluate the model on the popular NLVR2 [ 49 ] benchmark, which is to determine whether a textual description is true about a pair of images. Following previous work [ 65 , 26 ] , we construct two image-text pairs based on the triplet input. We finetune BEiT-3 as a fusion encoder to jointly encode the image-text pairs. The final pooled outputs of the two pairs are concatenated and then fed into a classifier layer to predict the label. As shown in Table 4 , BEiT-3 achieves a new state-of-the-art result for visual reasoning, outperforming CoCa by about 5.6 5.6 points. The performance on NLVR2 reaches above 90 90 % for the first time.

#### Image Captioning

The task aims to generate a natural language caption for the given image. We use the COCO [ 31 ] benchmark, finetune and evaluate the model on Karpathy split [ 24 ] . Following UniLM [ 17 ] and s2s-ft [ 5 ] , BEiT-3 is used as a conditional generation model via masked finetuning. To be more specific, a special self-attention mask is employed for the image captioning task. Image tokens (i.e., image patches) can only attend to each other bidirectionally within the image sequence. Tokens of the caption can attention to image tokens, their leftward caption tokens, and themselves. During finetuning, we randomly mask some percentage of caption tokens. The model is trained to recover these tokens based on the clues of the image and its leftward caption context. We also mask the special boundary token [SEP] to help the model learn to terminate the generation. For simplicity, BEiT-3 is trained with simple cross-entropy loss, without using CIDEr optimization. During inference, we generate the caption tokens one by one in an autoregressive manner. Table 4 presents the results on COCO captioning. BEiT-3 outperforms all previous models trained with cross-entropy loss, creating a new state-of-the-art image captioning result. The results demonstrate the superiority of BEiT-3 for vision-language generation.

#### Image-Text Retrieval

The task is to measure the similarity between images and texts. There are two directions depending on the modality of the retrieved target: image-to-text retrieval, and text-to-image retrieval. Two popular retrieval benchmarks, i.e., COCO [ 31 ] , and Flickr30K [ 41 ] , are used to evaluate the model. Following previous work [ 65 , 26 ] , we use the Karpathy split [ 24 ] for the two benchmarks. BEiT-3 is finetuned as a dual encoder for efficient image-text retrieval. Dual-encoder models separately encode images and texts to obtain their representations. Then we calculate the cosine similarity scores of these representations. Dual-encoder models are more efficient than fusion-encoder models. Because they do not have to jointly encode all possible image-text pairs.

We directly finetune BEiT-3 on COCO and Flickr30K, although the model is not pretrained with image-text contrastive loss. Surprisingly, BEiT-3 outperforms previous state-of-the-art models only using a small amount of contrastive training. The results demonstrate that BEiT-3 effectively learns alignments between images and texts via masked data modeling. In order to improve the performance, we perform intermediate finetuning with an image-text contrastive objective on the pretraining image-text pairs. We finetune the model with much fewer steps than pretraining. Then we use the model to evaluate zero-shot and finetuned image-text retrieval. The finetuned results are present in Table 5 , dual-encoder BEiT-3 outperforms prior models by a large margin, achieving 3.0 3.0 / 4.0 4.0 absolute improvement on COCO top- 1 1 image-to-text/text-to-image retrieval, and 0.8 0.8 / 2.4 2.4 absolute improvement on Flickr30K top- 1 1 image-to-text/text-to-image retrieval. BEiT-3 also significantly outperforms fusion-encoder-based models, which require more computation cost for inference. As present in Table 6 , BEiT-3 also achieves better performance than previous models on Flickr30K zero-shot retrieval.

### 3.2 Vision Downstream Tasks

In addition to vision-language downstream tasks, BEiT-3 can be transferred to a wide range of vision downstream tasks, including object detection, instance segmentation, semantic segmentation, and image classification. The number of effective parameters is comparable to ViT-giant [ 63 ] , i.e., about 1B, when BEiT-3 is used as a vision encoder.

#### Object Detection and Instance Segmentation

We conduct finetuning experiments on the COCO 2017 benchmark [ 31 ] , which consists of 118 118 k training, 5 5 k validation, and 20 20 k test-dev images. We use BEiT-3 as the backbone and follow ViTDet [ 32 ] , including a simple feature pyramid and window attention, for the object detection and instance segmentation tasks. Following common practices [ 29 , 66 ] , we first conduct intermediate finetuning on the Objects365 [ 48 ] dataset. Then we finetune the model on the COCO dataset. Soft-NMS [ 6 ] is used during inference. Table 7 compares BEiT-3 with previous state-of-the-art models on COCO object detection and instance segmentation. BEiT-3 achieves the best results on the COCO test-dev set with a smaller image size used for finetuning, reaching up to 63.7 63.7 box AP and 54.8 54.8 mask AP.

#### Semantic Segmentation

Semantic segmentation aims to predict the label for each pixel of the given image. We evaluate BEiT-3 on the challenging ADE20K dataset [ 68 ] , which includes 150 150 semantic categories. ADE20K contains 20 20 k images for training and 2 2 k images for validation. We directly follow the task transfer settings of ViT-Adapter [ 8 ] . We use a dense prediction task adapter and employ Mask2Former [ 10 ] as the segmentation framework. As shown in Table 8 , BEiT-3 creates a new state-of-the-art result with 62.8 62.8 mIoU, outperforming FD-SwinV2 [ 54 ] giant model with 3B parameters by 1.4 1.4 points. It shows that BEiT-3 achieves superior performance on the dense prediction task.

#### Image Classification

We evaluate the model on ImageNet-1K [ 42 ] , which contains 1.28 1.28 M training images and 50 50 k validation images in 1 1 k classes. Rather than appending a task layer to the vision encoder [ 13 , 3 ] , we formulate the task as an image-to-text retrieval task. We use the category names as texts to construct image-text pairs. BEiT-3 is trained as a dual encoder to find the most relevant label for an image. During inference, we first compute the feature embeddings of possible class names and the feature embedding of the image. Their cosine similarity scores are then calculated to predict the most probable label for each image. Table 9 reports the results on ImageNet-1K. We first perform intermediate finetuning on ImageNet-21K, then we train the model on ImageNet-1K. For a fair comparison, we compare with the previous models only using public image-tag data. BEiT-3 outperforms prior models, creating a new state-of-the-art result when only using public image-tag data.

## 4 Conclusion

In this paper, we present BEiT-3 , a general-purpose multimodal foundation model, which achieves state-of-the-art performance across a wide range of vision and vision-language benchmarks. The key idea of BEiT-3 is that image can be modeled as a foreign language, so that we can conduct masked “language” modeling over images, texts, and image-text pairs in a unified way. We also demonstrate that Multiway Transformers can effectively model different vision and vision-language tasks, making it an intriguing option for general-purpose modeling. BEiT-3 is simple and effective, and is a promising direction for scaling up multimodal foundation models. For future work, we are working on pretraining multilingual BEiT-3 and including more modalities (e.g., audio) in BEiT-3 to facilitate the cross-lingual and cross-modality transfer, and advance the big convergence of large-scale pretraining across tasks, languages, and modalities. We are also interested in enabling in-context learning capability for multimodal foundation models by combining the strength of BEiT-3 and MetaLM [ 20 ] .

## References

[1] Jean-Baptiste Alayrac, Jeff Donahue, Pauline Luc, Antoine Miech, Iain Barr, Yana Hasson, Karel Lenc, Arthur Mensch, Katie Millican, Malcolm Reynolds, Roman Ring, Eliza Rutherford, Serkan Cabi, Tengda Han, Zhitao Gong, Sina Samangooei, Marianne Monteiro, Jacob Menick, Sebastian Borgeaud, Andrew Brock, Aida Nematzadeh, Sahand Sharifzadeh, Mikolaj Binkowski, Ricardo Barreira, Oriol Vinyals, Andrew Zisserman, and Karen Simonyan. Flamingo: a visual language model for few-shot learning. CoRR , abs/2204.14198, 2022.

[2] Peter Anderson, Xiaodong He, Chris Buehler, Damien Teney, Mark Johnson, Stephen Gould, and Lei Zhang. Bottom-up and top-down attention for image captioning and visual question answering. In 2018 IEEE Conference on Computer Vision and Pattern Recognition, CVPR 2018, Salt Lake City, UT, USA, June 18-22, 2018 , pages 6077–6086. Computer Vision Foundation / IEEE Computer Society, 2018.

[3] Hangbo Bao, Li Dong, Songhao Piao, and Furu Wei. BEiT: BERT pre-training of image transformers. In International Conference on Learning Representations , 2022.

[4] Hangbo Bao, Li Dong, Furu Wei, Wenhui Wang, Nan Yang, Xiaodong Liu, Yu Wang, Jianfeng Gao, Songhao Piao, Ming Zhou, and Hsiao-Wuen Hon. UniLMv2: Pseudo-masked language models for unified language model pre-training. In Proceedings of the 37th International Conference on Machine Learning, ICML 2020, 13-18 July 2020, Virtual Event , volume 119 of Proceedings of Machine Learning Research , pages 642–652. PMLR, 2020.

[5] Hangbo Bao, Li Dong, Wenhui Wang, Nan Yang, and Furu Wei. s2s-ft: Fine-tuning pretrained transformer encoders for sequence-to-sequence learning. CoRR , abs/2110.13640, 2021.

[6] Navaneeth Bodla, Bharat Singh, Rama Chellappa, and Larry S. Davis. Soft-nms - improving object detection with one line of code. In IEEE International Conference on Computer Vision, ICCV 2017, Venice, Italy, October 22-29, 2017 , pages 5562–5570. IEEE Computer Society, 2017.

[7] Hangbo Bao, Wenhui Wang, Li Dong, and Furu Wei. VL-BEiT: Generative vision-language pretraining. ArXiv , abs/2206.01127, 2022.

[8] Zhe Chen, Yuchen Duan, Wenhai Wang, Junjun He, Tong Lu, Jifeng Dai, and Yu Qiao. Vision transformer adapter for dense predictions. CoRR , abs/2205.08534, 2022.

[9] Yen-Chun Chen, Linjie Li, Licheng Yu, Ahmed El Kholy, Faisal Ahmed, Zhe Gan, Yu Cheng, and Jingjing Liu. UNITER: universal image-text representation learning. In Andrea Vedaldi, Horst Bischof, Thomas Brox, and Jan-Michael Frahm, editors, Computer Vision - ECCV 2020 - 16th European Conference, Glasgow, UK, August 23-28, 2020, Proceedings, Part XXX , volume 12375 of Lecture Notes in Computer Science , pages 104–120. Springer, 2020.

[10] Bowen Cheng, Ishan Misra, Alexander G. Schwing, Alexander Kirillov, and Rohit Girdhar. Masked-attention mask transformer for universal image segmentation. CoRR , abs/2112.01527, 2021.

[11] Soravit Changpinyo, Piyush Sharma, Nan Ding, and Radu Soricut. Conceptual 12m: Pushing web-scale image-text pre-training to recognize long-tail visual concepts. In IEEE Conference on Computer Vision and Pattern Recognition, CVPR 2021, virtual, June 19-25, 2021 , pages 3558–3568. Computer Vision Foundation / IEEE, 2021.

[12] Zhaowei Cai and Nuno Vasconcelos. Cascade R-CNN: high quality object detection and instance segmentation. IEEE Trans. Pattern Anal. Mach. Intell. , 43(5):1483–1498, 2021.

[13] Alexey Dosovitskiy, Lucas Beyer, Alexander Kolesnikov, Dirk Weissenborn, Xiaohua Zhai, Thomas Unterthiner, Mostafa Dehghani, Matthias Minderer, Georg Heigold, Sylvain Gelly, et al. An image is worth 16x16 words: Transformers for image recognition at scale. preprint arXiv:2010.11929 , 2020.

[14] Jacob Devlin, Ming-Wei Chang, Kenton Lee, and Kristina Toutanova. BERT: pre-training of deep bidirectional transformers for language understanding. In Jill Burstein, Christy Doran, and Thamar Solorio, editors, Proceedings of the 2019 Conference of the North American Chapter of the Association for Computational Linguistics: Human Language Technologies, NAACL-HLT 2019, Minneapolis, MN, USA, June 2-7, 2019, Volume 1 (Long and Short Papers) , pages 4171–4186. Association for Computational Linguistics, 2019.

[15] Xiyang Dai, Yinpeng Chen, Bin Xiao, Dongdong Chen, Mengchen Liu, Lu Yuan, and Lei Zhang. Dynamic head: Unifying object detection heads with attentions. In IEEE Conference on Computer Vision and Pattern Recognition, CVPR 2021, virtual, June 19-25, 2021 , pages 7373–7382. Computer Vision Foundation / IEEE, 2021.

[16] Zihang Dai, Hanxiao Liu, Quoc V. Le, and Mingxing Tan. Coatnet: Marrying convolution and attention for all data sizes. In Marc’Aurelio Ranzato, Alina Beygelzimer, Yann N. Dauphin, Percy Liang, and Jennifer Wortman Vaughan, editors, Advances in Neural Information Processing Systems 34: Annual Conference on Neural Information Processing Systems 2021, NeurIPS 2021, December 6-14, 2021, virtual , pages 3965–3977, 2021.

[17] Li Dong, Nan Yang, Wenhui Wang, Furu Wei, Xiaodong Liu, Yu Wang, Jianfeng Gao, Ming Zhou, and Hsiao-Wuen Hon. Unified language model pre-training for natural language understanding and generation. In Advances in Neural Information Processing Systems 32: Annual Conference on Neural Information Processing Systems 2019, NeurIPS 2019, December 8-14, 2019, Vancouver, BC, Canada , pages 13042–13054, 2019.

[18] Zhe Gan, Yen-Chun Chen, Linjie Li, Chen Zhu, Yu Cheng, and Jingjing Liu. Large-scale adversarial training for vision-and-language representation learning. In Hugo Larochelle, Marc’Aurelio Ranzato, Raia Hadsell, Maria-Florina Balcan, and Hsuan-Tien Lin, editors, Advances in Neural Information Processing Systems 33: Annual Conference on Neural Information Processing Systems 2020, NeurIPS 2020, December 6-12, 2020, virtual , 2020.

[19] Yash Goyal, Tejas Khot, Douglas Summers-Stay, Dhruv Batra, and Devi Parikh. Making the V in VQA matter: Elevating the role of image understanding in visual question answering. In 2017 IEEE Conference on Computer Vision and Pattern Recognition, CVPR 2017, Honolulu, HI, USA, July 21-26, 2017 , pages 6325–6334. IEEE Computer Society, 2017.

[20] Yaru Hao, Haoyu Song, Li Dong, Shaohan Huang, Zewen Chi, Wenhui Wang, Shuming Ma, and Furu Wei. Language models are general-purpose interfaces. ArXiv , abs/2206.06336, 2022.

[21] Gao Huang, Yu Sun, Zhuang Liu, Daniel Sedra, and Kilian Q. Weinberger. Deep networks with stochastic depth. In Bastian Leibe, Jiri Matas, Nicu Sebe, and Max Welling, editors, Computer Vision - ECCV 2016 - 14th European Conference, Amsterdam, The Netherlands, October 11-14, 2016, Proceedings, Part IV , volume 9908 of Lecture Notes in Computer Science , pages 646–661. Springer, 2016.

[22] Jitesh Jain, Anukriti Singh, Nikita Orlov, Zilong Huang, Jiachen Li, Steven Walton, and Humphrey Shi. Semask: Semantically masking transformer backbones for effective semantic segmentation. arXiv , 2021.

[23] Chao Jia, Yinfei Yang, Ye Xia, Yi-Ting Chen, Zarana Parekh, Hieu Pham, Quoc V. Le, Yun-Hsuan Sung, Zhen Li, and Tom Duerig. Scaling up visual and vision-language representation learning with noisy text supervision. In Marina Meila and Tong Zhang, editors, Proceedings of the 38th International Conference on Machine Learning, ICML 2021, 18-24 July 2021, Virtual Event , volume 139 of Proceedings of Machine Learning Research , pages 4904–4916. PMLR, 2021.

[24] Andrej Karpathy and Li Fei-Fei. Deep visual-semantic alignments for generating image descriptions. In IEEE Conference on Computer Vision and Pattern Recognition, CVPR 2015, Boston, MA, USA, June 7-12, 2015 , pages 3128–3137. IEEE Computer Society, 2015.

[25] Taku Kudo and John Richardson. SentencePiece: A simple and language independent subword tokenizer and detokenizer for neural text processing. In Proceedings of the 2018 Conference on Empirical Methods in Natural Language Processing: System Demonstrations , pages 66–71, Brussels, Belgium, November 2018. Association for Computational Linguistics.

[26] Wonjae Kim, Bokyung Son, and Ildoo Kim. ViLT: Vision-and-language transformer without convolution or region supervision. In Marina Meila and Tong Zhang, editors, Proceedings of the 38th International Conference on Machine Learning, ICML 2021, 18-24 July 2021, Virtual Event , volume 139 of Proceedings of Machine Learning Research , pages 5583–5594. PMLR, 2021.

[27] Ranjay Krishna, Yuke Zhu, Oliver Groth, Justin Johnson, Kenji Hata, Joshua Kravitz, Stephanie Chen, Yannis Kalantidis, Li-Jia Li, David A. Shamma, Michael S. Bernstein, and Li Fei-Fei. Visual genome: Connecting language and vision using crowdsourced dense image annotations. Int. J. Comput. Vis. , 123(1):32–73, 2017.

[28] Ilya Loshchilov and Frank Hutter. Decoupled weight decay regularization. In 7th International Conference on Learning Representations, ICLR 2019, New Orleans, LA, USA, May 6-9, 2019 . OpenReview.net, 2019.

[29] Ze Liu, Han Hu, Yutong Lin, Zhuliang Yao, Zhenda Xie, Yixuan Wei, Jia Ning, Yue Cao, Zheng Zhang, Li Dong, Furu Wei, and Baining Guo. Swin transformer V2: scaling up capacity and resolution. CoRR , abs/2111.09883, 2021.

[30] Junnan Li, Dongxu Li, Caiming Xiong, and Steven C. H. Hoi. BLIP: bootstrapping language-image pre-training for unified vision-language understanding and generation. In Kamalika Chaudhuri, Stefanie Jegelka, Le Song, Csaba Szepesvári, Gang Niu, and Sivan Sabato, editors, International Conference on Machine Learning, ICML 2022, 17-23 July 2022, Baltimore, Maryland, USA , volume 162 of Proceedings of Machine Learning Research , pages 12888–12900. PMLR, 2022.

[31] Tsung-Yi Lin, Michael Maire, Serge J. Belongie, James Hays, Pietro Perona, Deva Ramanan, Piotr Dollár, and C. Lawrence Zitnick. Microsoft COCO: common objects in context. In David J. Fleet, Tomás Pajdla, Bernt Schiele, and Tinne Tuytelaars, editors, Computer Vision - ECCV 2014 - 13th European Conference, Zurich, Switzerland, September 6-12, 2014, Proceedings, Part V , volume 8693 of Lecture Notes in Computer Science , pages 740–755. Springer, 2014.

[32] Yanghao Li, Hanzi Mao, Ross B. Girshick, and Kaiming He. Exploring plain vision transformer backbones for object detection. CoRR , abs/2203.16527, 2022.

[33] Yinhan Liu, Myle Ott, Naman Goyal, Jingfei Du, Mandar Joshi, Danqi Chen, Omer Levy, Mike Lewis, Luke Zettlemoyer, and Veselin Stoyanov. Roberta: A robustly optimized BERT pretraining approach. CoRR , abs/1907.11692, 2019.

[34] Junnan Li, Ramprasaath R. Selvaraju, Akhilesh Deepak Gotmare, Shafiq R. Joty, Caiming Xiong, and Steven C. H. Hoi. Align before fuse: Vision and language representation learning with momentum distillation. CoRR , abs/2107.07651, 2021.

[35] Yanghao Li, Chao-Yuan Wu, Haoqi Fan, Karttikeya Mangalam, Bo Xiong, Jitendra Malik, and Christoph Feichtenhofer. Mvitv2: Improved multiscale vision transformers for classification and detection. In Proceedings of the IEEE/CVF Conference on Computer Vision and Pattern Recognition , pages 4804–4814, 2022.

[36] Xiujun Li, Xi Yin, Chunyuan Li, Pengchuan Zhang, Xiaowei Hu, Lei Zhang, Lijuan Wang, Houdong Hu, Li Dong, Furu Wei, Yejin Choi, and Jianfeng Gao. Oscar: Object-semantics aligned pre-training for vision-language tasks. In Andrea Vedaldi, Horst Bischof, Thomas Brox, and Jan-Michael Frahm, editors, Computer Vision - ECCV 2020 - 16th European Conference, Glasgow, UK, August 23-28, 2020, Proceedings, Part XXX , volume 12375 of Lecture Notes in Computer Science , pages 121–137. Springer, 2020.

[37] Feng Li, Hao Zhang, Huaizhe Xu, Shilong Liu, Lei Zhang, Lionel M. Ni, and Heung-Yeung Shum. Mask DINO: towards A unified transformer-based framework for object detection and segmentation. CoRR , abs/2206.02777, 2022.

[38] Liunian Harold Li, Pengchuan Zhang, Haotian Zhang, Jianwei Yang, Chunyuan Li, Yiwu Zhong, Lijuan Wang, Lu Yuan, Lei Zhang, Jenq-Neng Hwang, Kai-Wei Chang, and Jianfeng Gao. Grounded language-image pre-training. CoRR , abs/2112.03857, 2021.

[39] Vicente Ordonez, Girish Kulkarni, and Tamara L. Berg. Im2text: Describing images using 1 million captioned photographs. In John Shawe-Taylor, Richard S. Zemel, Peter L. Bartlett, Fernando C. N. Pereira, and Kilian Q. Weinberger, editors, Advances in Neural Information Processing Systems 24: 25th Annual Conference on Neural Information Processing Systems 2011. Proceedings of a meeting held 12-14 December 2011, Granada, Spain , pages 1143–1151, 2011.

[40] Zhiliang Peng, Li Dong, Hangbo Bao, Qixiang Ye, and Furu Wei. Beit v2: Masked image modeling with vector-quantized visual tokenizers. CoRR , abs/2208.06366, 2022.

[41] Bryan A. Plummer, Liwei Wang, Chris M. Cervantes, Juan C. Caicedo, Julia Hockenmaier, and Svetlana Lazebnik. Flickr30k entities: Collecting region-to-phrase correspondences for richer image-to-sentence models. In 2015 IEEE International Conference on Computer Vision, ICCV 2015, Santiago, Chile, December 7-13, 2015 , pages 2641–2649. IEEE Computer Society, 2015.

[42] Olga Russakovsky, Jia Deng, Hao Su, Jonathan Krause, Sanjeev Satheesh, Sean Ma, Zhiheng Huang, Andrej Karpathy, Aditya Khosla, Michael Bernstein, Alexander C Berg, and Li Fei-Fei. Imagenet large scale visual recognition challenge. IJCV , 2015.

[43] Alec Radford, Jong Wook Kim, Chris Hallacy, Aditya Ramesh, Gabriel Goh, Sandhini Agarwal, Girish Sastry, Amanda Askell, Pamela Mishkin, Jack Clark, Gretchen Krueger, and Ilya Sutskever. Learning transferable visual models from natural language supervision. In Marina Meila and Tong Zhang, editors, Proceedings of the 38th International Conference on Machine Learning, ICML 2021, 18-24 July 2021, Virtual Event , volume 139 of Proceedings of Machine Learning Research , pages 8748–8763. PMLR, 2021.

[44] Alec Radford, Karthik Narasimhan, Tim Salimans, and Ilya Sutskever. Improving language understanding by generative pre-training. 2018.

[45] Yongming Rao, Wenliang Zhao, Yansong Tang, Jie Zhou, Ser Nam Lim, and Jiwen Lu. HorNet: Efficient high-order spatial interactions with recursive gated convolutions. ArXiv , abs/2207.14284, 2022.

[46] Piyush Sharma, Nan Ding, Sebastian Goodman, and Radu Soricut. Conceptual captions: A cleaned, hypernymed, image alt-text dataset for automatic image captioning. In Iryna Gurevych and Yusuke Miyao, editors, Proceedings of the 56th Annual Meeting of the Association for Computational Linguistics, ACL 2018, Melbourne, Australia, July 15-20, 2018, Volume 1: Long Papers , pages 2556–2565. Association for Computational Linguistics, 2018.

[47] Amanpreet Singh, Ronghang Hu, Vedanuj Goswami, Guillaume Couairon, Wojciech Galuba, Marcus Rohrbach, and Douwe Kiela. FLAVA: A foundational language and vision alignment model. CoRR , abs/2112.04482, 2021.

[48] Shuai Shao, Zeming Li, Tianyuan Zhang, Chao Peng, Gang Yu, Xiangyu Zhang, Jing Li, and Jian Sun. Objects365: A large-scale, high-quality dataset for object detection. In 2019 IEEE/CVF International Conference on Computer Vision, ICCV 2019, Seoul, Korea (South), October 27 - November 2, 2019 , pages 8429–8438. IEEE, 2019.

[49] Alane Suhr, Stephanie Zhou, Ally Zhang, Iris Zhang, Huajun Bai, and Yoav Artzi. A corpus for reasoning about natural language grounded in photographs. In Anna Korhonen, David R. Traum, and Lluís Màrquez, editors, Proceedings of the 57th Conference of the Association for Computational Linguistics, ACL 2019, Florence, Italy, July 28- August 2, 2019, Volume 1: Long Papers , pages 6418–6428. Association for Computational Linguistics, 2019.

[50] Trieu H. Trinh and Quoc V. Le. A simple method for commonsense reasoning. ArXiv , abs/1806.02847, 2018.

[51] Zhengzhong Tu, Hossein Talebi, Han Zhang, Feng Yang, Peyman Milanfar, Alan Bovik, and Yinxiao Li. Maxvit: Multi-axis vision transformer. CoRR , abs/2204.01697, 2022.

[52] Ashish Vaswani, Noam Shazeer, Niki Parmar, Jakob Uszkoreit, Llion Jones, Aidan N. Gomez, Lukasz Kaiser, and Illia Polosukhin. Attention is all you need. In Isabelle Guyon, Ulrike von Luxburg, Samy Bengio, Hanna M. Wallach, Rob Fergus, S. V. N. Vishwanathan, and Roman Garnett, editors, Advances in Neural Information Processing Systems 30: Annual Conference on Neural Information Processing Systems 2017, December 4-9, 2017, Long Beach, CA, USA , pages 5998–6008, 2017.

[53] Wenhui Wang, Hangbo Bao, Li Dong, and Furu Wei. VLMo: Unified vision-language pre-training with mixture-of-modality-experts. CoRR , abs/2111.02358, 2021.

[54] Yixuan Wei, Han Hu, Zhenda Xie, Zheng Zhang, Yue Cao, Jianmin Bao, Dong Chen, and Baining Guo. Contrastive learning rivals masked image modeling in fine-tuning via feature distillation. CoRR , abs/2205.14141, 2022.

[55] Mitchell Wortsman, Gabriel Ilharco, Samir Ya Gadre, Rebecca Roelofs, Raphael Gontijo Lopes, Ari S. Morcos, Hongseok Namkoong, Ali Farhadi, Yair Carmon, Simon Kornblith, and Ludwig Schmidt. Model soups: averaging weights of multiple fine-tuned models improves accuracy without increasing inference time. In Kamalika Chaudhuri, Stefanie Jegelka, Le Song, Csaba Szepesvári, Gang Niu, and Sivan Sabato, editors, International Conference on Machine Learning, ICML 2022, 17-23 July 2022, Baltimore, Maryland, USA , volume 162 of Proceedings of Machine Learning Research , pages 23965–23998. PMLR, 2022.

[56] Zhirong Wu, Yuanjun Xiong, Stella X. Yu, and Dahua Lin. Unsupervised feature learning via non-parametric instance discrimination. In 2018 IEEE Conference on Computer Vision and Pattern Recognition, CVPR 2018, Salt Lake City, UT, USA, June 18-22, 2018 , pages 3733–3742. Computer Vision Foundation / IEEE Computer Society, 2018.

[57] Peng Wang, An Yang, Rui Men, Junyang Lin, Shuai Bai, Zhikang Li, Jianxin Ma, Chang Zhou, Jingren Zhou, and Hongxia Yang. Unifying architectures, tasks, and modalities through a simple sequence-to-sequence learning framework. CoRR , abs/2202.03052, 2022.

[58] Zirui Wang, Jiahui Yu, Adams Wei Yu, Zihang Dai, Yulia Tsvetkov, and Yuan Cao. SimVLM: Simple visual language model pretraining with weak supervision. CoRR , abs/2108.10904, 2021.

[59] Mengde Xu, Zheng Zhang, Han Hu, Jianfeng Wang, Lijuan Wang, Fangyun Wei, Xiang Bai, and Zicheng Liu. End-to-end semi-supervised object detection with soft teacher. In 2021 IEEE/CVF International Conference on Computer Vision, ICCV 2021, Montreal, QC, Canada, October 10-17, 2021 , pages 3040–3049. IEEE, 2021.

[60] Lu Yuan, Dongdong Chen, Yi-Ling Chen, Noel Codella, Xiyang Dai, Jianfeng Gao, Houdong Hu, Xuedong Huang, Boxin Li, Chunyuan Li, Ce Liu, Mengchen Liu, Zicheng Liu, Yumao Lu, Yu Shi, Lijuan Wang, Jianfeng Wang, Bin Xiao, Zhen Xiao, Jianwei Yang, Michael Zeng, Luowei Zhou, and Pengchuan Zhang. Florence: A new foundation model for computer vision. CoRR , abs/2111.11432, 2021.

[61] Lewei Yao, Runhui Huang, Lu Hou, Guansong Lu, Minzhe Niu, Hang Xu, Xiaodan Liang, Zhenguo Li, Xin Jiang, and Chunjing Xu. FILIP: fine-grained interactive language-image pre-training. CoRR , abs/2111.07783, 2021.

[62] Jiahui Yu, Zirui Wang, Vijay Vasudevan, Legg Yeung, Mojtaba Seyedhosseini, and Yonghui Wu. Coca: Contrastive captioners are image-text foundation models. CoRR , abs/2205.01917, 2022.

[63] Xiaohua Zhai, Alexander Kolesnikov, Neil Houlsby, and Lucas Beyer. Scaling vision transformers. arXiv preprint arXiv:2106.04560 , 2021.

[64] Yukun Zhu, Ryan Kiros, Rich Zemel, Ruslan Salakhutdinov, Raquel Urtasun, Antonio Torralba, and Sanja Fidler. Aligning books and movies: Towards story-like visual explanations by watching movies and reading books. In Proceedings of the IEEE international conference on computer vision , pages 19–27, 2015.

[65] Pengchuan Zhang, Xiujun Li, Xiaowei Hu, Jianwei Yang, Lei Zhang, Lijuan Wang, Yejin Choi, and Jianfeng Gao. VinVL: Revisiting visual representations in vision-language models. In IEEE Conference on Computer Vision and Pattern Recognition, CVPR 2021, virtual, June 19-25, 2021 , pages 5579–5588. Computer Vision Foundation / IEEE, 2021.

[66] Hao Zhang, Feng Li, Shilong Liu, Lei Zhang, Hang Su, Jun Zhu, Lionel M. Ni, and Heung-Yeung Shum. DINO: DETR with improved denoising anchor boxes for end-to-end object detection. CoRR , abs/2203.03605, 2022.

[67] Haotian Zhang, Pengchuan Zhang, Xiaowei Hu, Yen-Chun Chen, Liunian Harold Li, Xiyang Dai, Lijuan Wang, Lu Yuan, Jenq-Neng Hwang, and Jianfeng Gao. Glipv2: Unifying localization and vision-language understanding. CoRR , abs/2206.05836, 2022.

[68] Bolei Zhou, Hang Zhao, Xavier Puig, Tete Xiao, Sanja Fidler, Adela Barriuso, and Antonio Torralba. Semantic understanding of scenes through the ADE20K dataset. Int. J. Comput. Vis. , 127(3):302–321, 2019.

## Appendix A Effects of Intermediate Finetuning for Retrieval

As shown in Table 10 , we directly finetune BEiT-3 on COCO and Flickr30K. BEiT-3 still outperforms previous state-of-the-art models, even without using image-text contrastive objective during pretraining. The results demonstrate the effectiveness of masked data modeling for learning cross-modal representations. Next, we perform intermediate finetuning on the pretraining image-text pairs for 5 5 epochs with a 16 16 k batch size. The peak learning is 3e-5, with linear warmup over the first epoch. The image input size is 224 × 224 224\times 224 . The weight decay is set to 0.05 0.05 . We disable dropout as in pretraining and use drop path with a rate of 0.3 0.3 . The layer-wise learning rate decay is 0.95 0.95 . We use the AdamW [ 28 ] optimizer with β 1 = 0.9 \beta_{1}=0.9 , β 2 = 0.999 \beta_{2}=0.999 .

## Appendix B Hyperparameters Used for Pretraining

## Appendix C Hyperparameters Used for Finetuning

## Instructions for reporting errors

We are continuing to improve HTML versions of papers, and your feedback helps enhance accessibility and mobile support. To report errors in the HTML that will help us improve conversion and rendering, choose any of the methods listed below:

Click the "Report Issue" ( ) button, located in the page header.

Tip: You can select the relevant text first, to include it in your report.

Our team has already identified the following issues . We appreciate your time reviewing and reporting rendering errors we may not have found yet. Your efforts will help us improve the HTML versions for all readers, because disability should not be a barrier to accessing research. Thank you for your continued support in championing open access for all.

Have a free development cycle? Help support accessibility at arXiv! Our collaborators at LaTeXML maintain a list of packages that need conversion , and welcome developer contributions .
