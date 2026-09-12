##### Report GitHub Issue

Content selection saved. Describe the issue below:

# Learning Vision from Models Rivals Learning Vision from Data

###### Abstract

We introduce SynCLR, a novel approach for learning visual representations exclusively from synthetic images and synthetic captions, without any real data. We synthesize a large dataset of image captions using LLMs, then use an off-the-shelf text-to-image model to generate multiple images corresponding to each synthetic caption. We perform visual representation learning on these synthetic images via contrastive learning, treating images sharing the same caption as positive pairs. The resulting representations transfer well to many downstream tasks, competing favorably with other general-purpose visual representation learners such as CLIP and DINO v2 in image classification tasks. Furthermore, in dense prediction tasks such as semantic segmentation, SynCLR outperforms previous self-supervised methods by a significant margin, e.g . , improving over MAE and iBOT by 6.2 and 4.3 mIoU on ADE20k for ViT-B/16.

## 1 Introduction

Representation learning extracts and organizes information from raw, often unlabeled data. The quality, quantity, and diversity of the data determines how good a representation the model can learn. The model becomes a reflection of the collective intelligence that exists in the data. We get what we feed in.

Unsurprisingly, the current best-performing visual representation learning methods [ 71 , 68 ] rely on large scale real datasets. However, the collection of real data has its own dilemmas. Collecting large scale uncurated data [ 80 ] is relatively cheap and thus quite achievable. However, for self-supervised representation learning, this approach exhibits poor scaling behavior –i.e., adding more uncurated data has little effect at large data scales [ 38 , 90 ] . Collecting small scale curated data [ 24 ] also is achievable, but models trained in this way are limited to relatively narrow tasks. The ideal would be large scale curated datasets of real images, and recent work has indeed shown that this can lead to strong performance gains at scale [ 68 ] , but this path is costly to pursue.

To alleviate the cost, in this paper we ask if synthetic data , sampled from off-the-shelf generative models, is a viable path toward large scale curated datasets that can train state-of-the-art visual representations.

We call such a paradigm learning from models , in contrast to directly learning from data . Models have several advantages as a data source for building large scale training sets: via their latent variables, conditioning variables, and hyperparameters, they provide new controls for curating data; we will make use of these controls in the method we propose. Models also can be easier to share and store (because models are more compressed than data), and can produce an unlimited number of data samples (albeit with finite diversity). A growing literature has studied these properties and other advantages (and disadvantages) of using generative models as a data source for training downstream models [ 48 , 45 , 3 , 78 , 91 , 30 ] . Some of these methods use a hybrid mode – either mixing real and synthetic datasets [ 3 ] or needing a real dataset to generate another synthetic dataset [ 91 ] . Other methods try to learn representations from purely synthetic data [ 78 ] but lag far behind the best performing models. Instead, we show that learning from models , without training on any real data, can yield representations that match the top-performing representations learnt from real data. For instance, as illustrated in Figure 1 , representations learnt by our method are able to transfer as well as OpenAI’s CLIP [ 71 ] on ImageNet (both methods using ViT-B [ 28 ] ).

Our approach leverages generative models to re-define the granularity of visual classes. As shown in Figure 2 , consider we have four images generated using two prompts: “ a golden retriever, wearing sunglasses and a beach hat, rides a bike " and “ a cute golden retriever sits in a house made of sushi ". Traditional self-supervised method such as SimCLR [ 13 ] will treat each of these images as a different class; embeddings for different images are pushed apart with no explicit consideration of the shared semantics between images. On the other extreme, supervised learning methods ( i.e . SupCE) will regard all these images as a single class (e.g., “golden retriever”). This ignores nuances in the semantics of the images, such as the fact that the dogs are riding a bike in one pair of images and sitting inside a sushi house in the other pair of images. Instead, our method, SynCLR, treats captions as classes, i.e . , each caption describes a visual class (this level of granularity was also explored in StableRep [ 91 ] ). This allows us to group images by the concepts of “riding a bike” and “sitting in a sushi house”, in addition to grouping by a coarser class label like “golden retrieval”. This level of granularity is difficult to mine in real data, since collecting multiple images described by a given caption is non-trivial, especially when scaling up the number of captions. However, text-to-image diffusion models are fundamentally built with this ability; simply by conditioning on the same caption and using different noise inputs, a text-to-image diffusion model will produce different images that all match the same caption. In our experiments, we find the caption-level granularity outperforms both SimCLR and supervised training. Another advantage is that this definition of visual classes has good scalability. Unlike ImageNet-1k/21k where a given number of classes is fixed, we can augment existing classes (or data) in an online fashion, and theoretically scale up to as many classes as needed.

Our system consists of three steps. The first step is to synthesize a large corpus of image captions. We design a scalable approach by leveraging the in-context learning capability of large language models (LLMs), where we present examples of word-to-caption translations. Next, a text-to-image diffusion model is adopted to synthesize multiple images for each synthetic caption. This yields a synthetic dataset of 600M images. Then we train visual representation models by a combination of multi-positive contrastive learning [ 50 ] and masked image modeling [ 110 ] .

Our learned representations transfer well. With SynCLR pre-training, our ViT-B and ViT-L models achieve 80.7 % \% and 83.0 % \% top-1 linear probing accuracy on ImageNet-1K, respectively, which is on par with OpenAI’s CLIP [ 71 ] . On fine-grained classification tasks, SynCLR outperforms CLIP by 3.3 % \% for ViT-B and 1.5 % \% for ViT-L, and performs similarly to DINO v2 [ 68 ] models, which are distilled from a pre-trained ViT-g model. For semantic segmentation on ADE20k, SynCLR outperforms MAE pre-trained on ImageNet by 6.2 and 4.1 in mIoU for ViT-B and ViT-L under the same setup, showing strong transfer ability for dense prediction tasks similar to DINO v2, which additionally involves a training period on 518x518 resolution images that SynCLR does not have.

## 2 Related Works

Self-supervised representation learning approaches in vision develop domain-specific pre-text tasks, such as colorization [ 106 ] , rotation prediction [ 36 ] , and solving jigsaw puzzles [ 65 ] . Domain-agnostic approaches have been popular, such as contrastive learning [ 6 , 40 , 66 , 97 , 88 , 43 , 13 ] and masked image modeling [ 5 , 100 , 44 , 96 , 2 , 110 , 4 , 33 ] . Contrastive learning promotes invariance [ 89 ] for two views of the same image and pushes apart representations for different images [ 95 ] (or only invariance [ 39 , 11 ] ); the resulting representations yield strong performance for linear or zero-shot transfer. Masked image modeling reconstructs the pixels [ 44 , 100 ] or local features [ 4 ] , often producing excellent fine-tuning transfer performance, especially in dense prediction tasks [ 44 ] . The state of the art DINO v2 [ 68 ] leverages both approaches, and our approach shares a similar spirit.

Supervised learning [ 52 , 84 , 41 ] used to be the dominant approach for learning transferable visual representations for various tasks [ 37 , 26 , 81 ] . Recent studies [ 57 , 42 ] has shown that, the transferability of representations learned in this way is limited, e.g . , pre-training has no improvement over random initialization for dense prediction tasks ( e.g . , object detection) when the fine-tuning is long enough. Such limitation continues when the model has been scaled up to 22B [ 23 ] . An alternative paradigm learns visual representations from text supervision [ 71 , 49 ] , e.g . , CLIP [ 71 ] . This approach is more flexible ( i.e . , not requiring classes) and provides richer supervision, often learning generalizable representations.

Generative models as representation learners. A number of papers have explored the representations that are learned by generative models for various recognition tasks [ 25 , 56 ] . As might be expected intuitively, such models indeed learn especially good representations for dense tasks, such as optical flow estimation [ 79 ] , semantic segmentation [ 8 , 101 ] , and depth estimation [ 107 ] . Another line of work [ 55 , 19 ] adapt pre-trained diffusion models for zero-shot image recognition via analysis-by-synthesis. These approaches may need to be adapted when the architectures of the generative models change or a new family of generative model emerge. Our approach treats images as universal interfaces with the hope of better generality.

Learning from synthetic data from generative models. Synthetic data has been explored to train machine learning models in various domains [ 83 , 74 , 75 , 63 , 53 , 87 , 102 , 62 , 31 ] . In computer vision, the utilization of synthetic data for training models is common, ranging from optical flow [ 61 ] and autonomous driving [ 1 ] to semantic segmentation [ 15 ] and human pose estimation [ 94 ] . Others [ 58 , 48 ] have explored synthetic data for representation learning, with the predominant approach of altering the latent variables of deep generative models. Our approach aligns with this research paradigm, but it diverges in its use of text-to-image models, which have also been investigated by other researchers [ 78 , 111 , 45 ] . But they use synthetic data for supervised learning [ 78 , 30 ] . The closet work is StableRep [ 91 ] , which also conducts representation learning but still needs a real text dataset.

## 3 Approach

In this paper, we study the problem of learning a visual encoder f f in the absence of real images or textual data. Our approach hinges on the utilization of three key resources: a language generation model ( g 1 g_{1} ), a text-to-image generative model ( g 2 g_{2} ), and a curated list of visual concepts ( C C ). Our exploration include three steps: (1) we employ g 1 g_{1} to synthesize a comprehensive set of image descriptions T T , which encompass the range of visual concepts in C C ; (2) for each caption in T T , we generate multiple images using g 2 g_{2} , culminating in an extensive synthetic image dataset X X ; (3) we train on X X to obtain a visual representation encoder f f .

We use Llama-2 7B [ 93 ] and Stable Diffusion 1.5 [ 73 ] as g 1 g_{1} and g 2 g_{2} , respectively, because of their fast inference speed. We anticipate that better g 1 g_{1} and g 2 g_{2} in the future will further enhance the effectiveness of this approach.

### 3.1 Synthesizing captions

To harness the capability of powerful text-to-image models for generating a substantial dataset of training images, we initially require a collection of captions that not only precisely depict an image but also exhibit diversity to encompass a broad spectrum of visual concepts.

We have developed a scalable approach to create such a large collection of captions, leveraging the in-context learning capability of LLMs [ 9 ] . Our method involves crafting specific prompt engineering templates that guide the LLM to produce the required captions. We start by gathering the concept list C C from some existing datasets, such as ImageNet-21k [ 24 ] and Places-365 [ 108 ] . For each concept c ∈ C c\in C , we consider three straightforward templates to generate captions effectively.

• c c –> caption . As the most direct and simple approach, we have the Llama-2 model sample a sentence for the concept c c .

• c c , b ​ g bg –> caption . We combine the visual concept c c with a background or setting b ​ g bg . A naïve approach would randomly select both c c and b ​ g bg , where b ​ g bg may correspond to a class name from a places dataset like [ 108 ] . However, this method often leads to unlikely combinations in the real world, such as a blue whale in a football field. Our ablation experiments demonstrate that this strategy results in suboptimal performance, likely because the generated captions fall far outside the training distribution of g 2 g_{2} . Instead, we employ GPT-4 [ 67 ] to generate a list of suitable backgrounds for the chosen concepts. This approach increases the likelihood of generating more plausible combinations, such as a tiger in a forest or a cat in a kitchen, enhancing the overall quality of the results.

• c c , r ​ e ​ l rel –> caption . Given a visual concept c c , we consider pairing it with a positional relationship word, r ​ e ​ l rel . Take for instance, if c c signifies cat and r ​ e ​ l rel translates to in front of , our objective is to prompt the LLM to create captions such as a cute yellow cat is enjoying the fish in front of the sofa . To add variety, we have a selection of 10 different positional relationship words that we randomly choose from.

For each of the three templates, we have prepared multiple demonstration examples that serve as instructions for the LLM to complete the caption synthesis task. Table 1 shows a couple of examples for each template. In total, we have 106 examples for c c –>prompt , 50 examples for c , b ​ g c,bg –>prompt , and 20 examples for c , r ​ e ​ l c,rel –>prompt . Such examples are mostly collected by prompting GPT-4, with a handful from human. In a pilot study, we do not observe difference between including or excluding human generated examples.

In the stage of generating captions in-context, we select a concept and one of the three templates. Next, we randomly pick three examples from the chosen template and frame the caption generation as a text completion task. This process is illustrated in Figure 3 .

### 3.2 Synthesizing Images

For each text caption, we generate a variety of images by initiating the reverse diffusion process with different random noise. The Classifier-Free Guidance (CFG) scale is a crucial factor in this process. A higher CFG scale enhances the quality of the samples and the alignment between text and image, whereas a lower scale results in more diverse samples and better adherence to the original conditional distribution of images based on the given text. Following the approach used in StableRep [ 91 ] , we opt for a lower CFG scale, specifically 2.5, and produce 4 images for each caption. Examples of these images can be seen in Figure 4 .

### 3.3 Representation Learning

Our representation learning method is built upon StableRep [ 91 ] . The key component of our approach is the multi-positive contrastive learning loss [ 50 ] which works by aligning (in the embedding space) images generated from the same caption. We additionally combine multiple techniques from other self-supervised learning methods, including a patch-level masked image modeling objective. We briefly review StableRep and elaborate on the added modules.

StableRep [ 91 ] minimizes the cross-entropy loss between a ground-truth assignment distribution and a contrastive assignment distribution. Consider an encoded anchor sample 𝒂 \bm{a} and a set of encoded candidates { 𝒃 1 , 𝒃 2 , … , 𝒃 K } \{\bm{b}_{1},\bm{b}_{2},...,\bm{b}_{K}\} . The contrastive assignment distribution 𝐪 {\mathbf{q}} describes how likely the model predicts 𝒂 \bm{a} and each 𝒃 \bm{b} to be generated from the same caption, and the ground-truth distribution is the actual match between 𝒂 \bm{a} and 𝒃 \bm{b} ( 𝒂 \bm{a} is allowed to match multiple 𝒃 \bm{b} ): 𝐪 i = exp ⁡ ( 𝒂 ⋅ 𝒃 i / τ ) ∑ j = 1 K exp ⁡ ( 𝒂 ⋅ 𝒃 j / τ ) \displaystyle{\mathbf{q}}_{i}=\frac{\exp(\bm{a}\cdot\bm{b}_{i}/\tau)}{\sum_{j=1}^{K}\exp(\bm{a}\cdot\bm{b}_{j}/\tau)} (1) 𝐩 i = 𝟙 match ​ ( 𝒂 , 𝒃 i ) ∑ j = 1 K 𝟙 match ​ ( 𝒂 , 𝒃 j ) \displaystyle{\mathbf{p}}_{i}=\frac{\mathbbm{1}_{\text{match}(\bm{a},\bm{b}_{i})}}{\sum_{j=1}^{K}\mathbbm{1}_{\text{match}(\bm{a},\bm{b}_{j})}} (2) where τ ∈ ℛ + \tau\in\mathcal{R}_{+} is the scalar temperature, 𝒂 \bm{a} and all 𝒃 \bm{b} have been ℓ 2 \ell_{2} normalized, and the indicator function 𝟙 match ​ ( ⋅ , ⋅ ) \mathbbm{1}_{\text{match}(\cdot,\cdot)} indicates whether two samples are from the same caption. The contrastive loss for 𝒂 \bm{a} is given as ℒ ( 𝒂 ) = H ( 𝐩 , 𝐪 ) = − ∑ i = 1 K 𝐩 i log 𝐪 i \displaystyle\mathcal{L}(\bm{a})=H({\mathbf{p}},{\mathbf{q}})=-\sum_{i=1}^{K}{\mathbf{p}}_{i}\log{\mathbf{q}}_{i} (3)

iBOT [ 110 ] is a masked image modeling objective, wherein a localized patch is masked, and the model is tasked with predicting the tokenized representation of said masked patch. It adapts the DINO [ 11 ] objective from the image level into the patch level. We follow [ 76 ] to replace the softmax-centering method with the iterative Sinkhorn-Knopp (SK) algorithm [ 22 ] . We run SK for 3 iterations to build the prediction target.

Exponential Moving Average (EMA) is firstly introduced into self-supervised learning by MoCo [ 43 ] . We use EMA to encode crops as 𝒃 \bm{b} and to produce the targets for iBOT loss. We update the EMA model as θ e ​ m ​ a ← λ ​ θ e ​ m ​ a + ( 1 − λ ) ​ θ \theta_{ema}\leftarrow\lambda\theta_{ema}+(1-\lambda)\theta , following a cosine schedule for λ \lambda from 0.994 to 1 during training [ 39 , 68 ] . We find the EMA module not only increases the final performance, but also improves the training stability for long training schedules.

Multi-crop strategy is introduced by [ 10 ] as a smart way to improve computation efficiency, and is adopted in this paper. For these local crops, we only employ the contrastive loss, omitting the iBOT loss. Local crops are encoded only by the student network, and matched to global crops from the same caption encoded by the EMA model. Such reuse of global crops saves computation. For each image x x , where we generate a single global crop x g x^{g} alongside n n local crops x l x^{l} , the final loss can be expressed as follows: ℒ ⁡ ( x g ) + 1 n ​ ∑ i = 1 n ℒ ⁡ ( x i l ) + ℒ i ​ B ​ O ​ T ​ ( x g ) \displaystyle\mathcal{L}(x^{g})+\frac{1}{n}\sum_{i=1}^{n}\mathcal{L}(x^{l}_{i})+\mathcal{L}^{iBOT}(x^{g}) (4)

### 3.4 Implementation

Concept list. We concatenate class names from various datasets, including IN-1k [ 24 ] , IN-21k (we keep the most frequent 13k classes), Aircraft [ 60 ] , Cars [ 51 ] , DTD [ 18 ] , Flowers [ 64 ] , Pets [ 69 ] , Sun397 [ 98 ] , Caltech-101 [ 34 ] , Food-101 [ 7 ] , and Places-365 [ 108 ] . If the concept is a place ( i.e . SUN397 and Places) or a texture ( i.e . DTD), we only apply the c c –> caption template. For fine-grained classes such as pets or flowers, we employ GPT-4 to generate a consolidated list of probable backgrounds, rather than producing distinct lists for each specific class. We favor more frequent sampling from IN-1k, Food101, Cars, Aircraft, and Flowers.

Batches. For each training batch, we sample 2048 captions (except when noted), and use all of the 4 images generated by each caption. We generate 1 global and 4 local crops for each image. As a result, each batch contains 8192 global crops, which is similar with prior work [ 13 , 39 , 14 , 91 ] .

Masking. For the iBOT loss, we randomly choose 50 % 50\% images inside a batch to mask, and randomly mask 50 % 50\% of the tokens in each chosen image. We use 65536 prototypes. While the target from the EMA model is ascertained using the SK algorithm, we apply softmax normalization to the output of the student model.

Projection heads. We follow the design in MoCo v3 [ 14 ] and DINO [ 11 ] for the contrastive and iBOT loss heads, respectively, ensuring consistency with established methods.

Other hyper-parameters. We set the temperature in the contrastive loss to 0.08 0.08 . For the temperature used in the iBOT loss, we linearly increase it from 0.04 to 0.07 over 4000 iterations, and keep it as 0.07 afterwards, as in DINO [ 11 ] . Additionally, the weight decay parameter is incrementally adjusted from 0.04 to 0.2, adhering to a cosine schedule.

## 4 Experiment

We first perform an ablation study to evaluate the efficacy of various designs and modules within our pipeline. Then we proceed to scale up the volume of synthetic data.

### 4.1 Study different components

We analyze each component of SynCLR, and ablate their effectiveness in two measurements: (1) linear probing performance on IN-1k; (2) average accuracy of linear transfer on fine-grained datasets Aircraft [ 60 ] , Cars [ 51 ] , DTD [ 18 ] , Flowers [ 64 ] , Pets [ 69 ] , Sun397 [ 98 ] , Caltech-101 [ 34 ] , Food-101 [ 7 ] , and Pascal VOC [ 29 ] . For analysis conducted in this subsection, we train ViT-B/16 [ 28 ] models for 85000 iterations, and use the cls token as image representation.

Synthesize captions. Following [ 91 ] , we use cc12m [ 12 ] real captions as our baseline, which has 10M sentences. To synthesize captions, we design the following variants: (a) IN+h+Places randomly combines one IN class plus its hypernyms in WordNet graph, with one place class; (b) IN+Places+LLM uses the c , b ​ g c,bg –> caption in-context synthesis template with c c from IN and b ​ g bg from places; (c) IN+ourBG+LLM uses the background classes output by GPT-4, instead of Places; (d) ours means our full configuration specified in Section 3.1 . For each of the config, we generate 10M captions. If not enough, we do duplication.

Results are summarized in Table 2 , where we train both StableRep and SynCLR to avoid biases favored by a single method. Compared to a real caption dataset cc12m, simply concatenating IN and Places class names improves the ImageNet linear accuracy but reduces the fine-grained classification performance. Interestingly, naively asking Llama to combine IN and Places classes into captions yields the worst performance. Replacing random background from places with GPT generated background improves the accuracy. This shows the importance of synthesizing captions that follow the distribution of real captions, which were used to train the text-to-image model. Finally, our full configuration achieves the best accuracy on both ImageNet and fine-grained classification. Another advantage of our synthesis method is its scalability – scale up to hundreds of millions of captions with little duplication. In contrast, if we concatenate IN classes with Places classes, there are at most 365k unique captions.

Synthesize images. There are two major parameters in this process: number of images per caption and classifier free guidance scale. For the former, we find generating 4 images is almost able to reproduce StableRep [ 91 ] ’s performance (10 images) when using cc12m captions (ours 73.0 % \% v.s. StableRep 73.5 % \% on ImageNet). Thus we stick to 4. For guidance scale, we briefly find the contrastive loss is not very sensitive to CFG in a pilot study, as shown in Table 3 . Thus we stick to 2.5, similar as StableRep [ 91 ] .

ImageNet

Aircraft

Cars

DTD

Flowers

Pets

SUN397

Caltech-101

Food-101

VOC2007

Average

Model components. We present the improvement of accuracy brought by different modules in Table 4 . Compared to the baseline StableRep, adding a teacher EMA model improves the IN linear accuracy by 0.9 % \% . Further adding iBOT local objective or the multi-crop strategy increases the accuracy by 0.9 % \% and 1.9 % \% , respectively. Combining all of them results in our full SynCLR model, which achieves 78.8 % \% top-1 IN linear accuracy. The fine-grained classification performance follows a similar trend, and reaches 88.1 % \% . Besides, we test the transfer ability to semantic segmentation on ADE20k. The iBOT objective brings 1.0 more mIoU than multi-crop strategy, demonstrating the effectiveness of masked image modeling for dense prediction tasks.

Compare to SimCLR and supervised training. We compare the three different representation learning objectives shown in Figure 2 , which classify images at different levels of granularity. Since supervised cross-entropy training requires a fixed set of balanced classes (indeed both fixed set and balance are limitations of such method), we use the IN+ourBG+LLM configuration where we have 1000 balanced classes ( i.e . , each class has 40k images). The supervised training recipe follows [ 86 ] . For a fair comparison with SimCLR, we remove all unmatched modules ( i.e . , EMA, iBOT, and MC) to make sure that the only difference between SimCLR and our SynCLR is the classification granularity defined by the contrastive loss. For all of them, we do pre-training and then linear probing on the target dataset.

Table 5 presents the comparison. Our multi-positive objective, which defines images as the same class if they are generated by the same caption, achieves the best performance. It outperforms supervised cross-entropy training and SimCLR by 3.4 % \% and 11.7 % \% for top-1 accuracy on ImageNet linear evaluation, and by 3.5 % \% and 10.6 % \% on fine-grained classification tasks. Besides, our objective does not require balance between samples from a fixed set of classes, making it easier to scale up.

### 4.2 Scaling up

After we have ablated different components, we scale up our experiments. Specifically, we synthesize a dataset of 150M captions, called SynCaps-150M , from which we generate 600M images. We train both ViT-B/16 and ViT-L/14 (no SwiGLU [ 82 ] or LayerScale [ 92 ] ), and extend the training schedules to 500k steps with a batch size of 8192 captions. We use 224x224 resolution for all pre-training tasks.

We compare SynCLR with OpenAI’s CLIP [ 71 ] , OpenCLIP [ 17 ] , and DINO v2 [ 68 ] , which represent learning from data . We note that ViT-B/14 and ViT-L/14 from DINO v2 are distilled from a ViT-g [ 104 ] model, which makes DINO v2 advantageous in our comparison. We also includes StableRep [ 91 ] , which uses the hybrid paradigm.

ImageNet linear evaluation. For fair comparison, cls token from the last block is used as representation across all models (whereas in DINO v2, results are from concatenating multiple layers). As shown in Table 6 , SynCLR achieves 80.7 % \% with ViT-B and 83.0 % \% with ViT-L. This is similar as CLIP, but still lags behind DINO v2 by 3.2 % \% and 2.7 % \% , respectively, partially because of the extra distillation in DINO v2. We note SynCLR has already outperformed other self-supervised methods pre-trained directly on ImageNet-1k ( e.g . , DINO achieves 78.2 % \% with ViT-B/16 and iBOT reaches 81.0 % \% with ViT-L/16).

Fine-grained classification. On the nine fine-grained datasets we have evaluated in Table 6 , SynCLR achieves very similar average accuracy as DINO v2, e.g . , 89.0 % \% v.s. 89.0 % \% for ViT-B, and 90.1 % \% vs 90.4 % \% for ViT-L. Both SynCLR and DINO v2 have curated the pre-training data to include the distribution for these datasets (but in different ways and portions), and end up with similar performance. Interestingly, SynCLR outperforms others on Aircraft and Cars, possibly because we favor more frequent sampling towards them. This can be an advantage for synthetic data when we know what downstream tasks to solve. Besides, SynCLR outperforms CLIP and StableRep by 3.3 % \% and by 5.6 % \% for ViT-B, respectively.

Semantic segmentation. To evaluate the pixel-level understanding ability of SynCLR, we fine-tune the pre-trained models on ADE20k [ 109 ] , following the setup in [ 44 , 5 ] . UperNet [ 99 ] is used as the task layer, and we evaluate with a single-scale, i.e . 512x512. Besides CLIP and DINO v2, we also compare to self-supervised methods pre-trained on ImageNet, as well as BEiT v2 [ 70 ] , which distills from CLIP. Table 7 shows that our SynCLR outperforms self-supervised methods trained on IN-1k by a clear marge, e.g . , 4.3 higher mIoU than iBOT. Despite not involving a high resolution pre-training period like DINO v2 ( e.g . , 518x518), SynCLR performs similarly with DINO v2 (0.1 lower for ViT-B possibly because DINO v2 uses a smaller patch size of 14x14, but 0.2 higher for ViT-L). This suggests SynCLR pre-training is suitable for dense prediction tasks.

ImageNet fine-tuning. We evaluate the fine-tuning transfer ability of SynCLR on ImageNet. We compare with other state of the art self-supervised methods [ 14 , 5 , 100 , 44 , 27 , 4 , 110 ] in Table 8 . Our SynCLR outperforms models trained on ImageNet images or large scale image datasets. Specifically, SynCLR outperforms OpenCLIP ViT-L trained on Laion-2B, which is the dataset Stable Diffusion (the text2image model we used) is trained on. This contrasts with [ 78 , 30 ] , which shows that directly training a classifier on synthetic images yields bad classification accuracy. Our finding suggests synthetic images are good for training representations, which later can be easily adapted to a downstream task with limited amount of real data.

### 4.3 Further analysis

SynCLR requires a list of concepts C C to start off. But how will SynCLR transfer to concepts outside our list?

EuroSAT

GTSRB

Country211

MNIST

RESISC45

KITTI

Average

Generalize to unseen concepts. We consider additional datasets whose classes are outside the synthesis list, including EuroSAT [ 46 ] , GTSRB [ 85 ] , Country211 [ 71 ] , MNIST [ 54 ] , RESISC45 [ 16 ] , and KITTI distances [ 35 ] . These datasets, except for KITTI, are also outside the curation list of DINO v2. Therefore, it is also a generalization test for DINO v2. Table 9 shows the linear probing results. SynCLR outperforms DINO v2 by 1.5 % \% for ViT-B and 1.1 % \% for ViT-L, respectively. This suggests the representations of SynCLR generalize. CLIP outperforms SynCLR and DINO v2, with most gains coming from Country211. An explanation is CLIP’s training data contains similar country flags which are not in the training sets of SynCLR and DINO v2.

Given that both captions and images are synthesized, a natural question arises: how would CLIP training perform on such data?

Compare to CLIP training. We use the same data to train a ViT-B CLIP model. For each caption, we randomly choose 1 out of the 4 synthesized images in each iteration. Following common practice [ 71 ] , we train for 32 epochs with a batch size of 32768. This model achieves 44.4 % \% zero-shot accuracy on IN-1k. The SynCaps-150M row in Table 10 presents the linear probing results. Synthetic CLIP learns reasonably good features, reaching 78.3 % \% on IN-1k and 87.7 % \% on fine-grained datasets. However, SynCLR is still better.

We have also repeated our experiments with Laion-400M captions, i.e . , generate 4 images for each caption and train SynCLR and CLIP. The comparison between rows SynCaps-150M and Laion-400M in Table 10 suggests synthetic captions are also favorable on a large scale.

PCA visualization. Following the method used in DINO v2 [ 68 ] , we present visualizations derived from the Principal Component Analysis (PCA) conducted on patch features extracted using our model SynCLR. As depicted in Figure 5 , a comparative analysis is conducted between SynCLR and DINO v2, both utilizing the ViT-L/14 architecture. The results demonstrate that SynCLR effectively accentuates the features of cars and planes, while efficiently minimizing background clutter.

Scaling behavior. We train ViT-BViT-L models using random subsets of varying sizes: 1M, 3M, 10M, 40M, and the comprehensive 150M (measured in the number of captions). These models are trained over a reduced schedule of 300,000 steps and utilizes a smaller batch size of 2048. The outcomes of linear probing are illustrated in Figures 6 and 7 . These results indicate that the ViT-B model delivers robust performance at the 10M scale, with diminishing returns observed beyond this point. In contrast, the ViT-L model exhibits a greater demand for data (i.e., it underperforms ViT-B at the 3M scale) and scales better with data.

## 5 Discussions and Conclusion

Why learn from generative models? One compelling reason is that a generative model can act like hundreds of datasets simultaneously . Traditionally, researchers have to spend separate effort collecting datasets for different image categories, e.g . , cars, flowers, cats, dogs, and so on. DINO v2 [ 68 ] achieves robust representations by curating and amalgamating numerous such datasets. Such a process introduces complexities such as clustering and search challenges. In contrast, advanced text-to-image generative models like Stable Diffusion [ 72 ] or Imagen [ 77 ] have the capability to generate many diverse datasets. These models provide the flexibility to produce an infinite number of samples (albeit finite diversity) and control the generation process through textual input. Thus, generative models offer a convenient and effective method for curating training data. In our study, we harness this advantage to synthesize images encompassing a broad spectrum of visual concepts.

What can be further improved? Enhanced caption sets can be achieved through various methods, such as enriching the set of in-context examples, optimizing the sampling ratios among different concepts, and utilizing more advanced LLMs. In terms of the learning process, one approach is to distill knowledge from a larger model, and incorporate an additional high-resolution training phase (as discussed in [ 68 ] ) or an intermediate IN-21k fine-tuning stage (as per [ 5 , 70 ] ). Regarding architectural improvements, the integration of SwiGLU and LayerScale, coupled with superior model initialization strategies (referenced in [ 32 ] ), can be beneficial. However, due to limited resources and the scope of this paper not being focused on achieving the highest possible metrics, we propose these areas for further exploration in future research endeavors.

In summary, this paper studies a new paradigm for visual representation learning – learning from generative models . Without using any real data, SynCLR learns visual representations that are comparable with those achieved by state of the art general-purpose visual representation learners.

## References

[1] Hassan Abu Alhaija, Siva Karthik Mustikovela, Lars Mescheder, Andreas Geiger, and Carsten Rother. Augmented reality meets computer vision: Efficient data generation for urban driving scenes. IJCV , 2018.

[2] Mahmoud Assran, Mathilde Caron, Ishan Misra, Piotr Bojanowski, Florian Bordes, Pascal Vincent, Armand Joulin, Mike Rabbat, and Nicolas Ballas. Masked siamese networks for label-efficient learning. In ECCV , 2022.

[3] Shekoofeh Azizi, Simon Kornblith, Chitwan Saharia, Mohammad Norouzi, and David J Fleet. Synthetic data from diffusion models improves imagenet classification. arXiv preprint arXiv:2304.08466 , 2023.

[4] Alexei Baevski, Wei-Ning Hsu, Qiantong Xu, Arun Babu, Jiatao Gu, and Michael Auli. Data2vec: A general framework for self-supervised learning in speech, vision and language. In ICML , 2022.

[5] Hangbo Bao, Li Dong, Songhao Piao, and Furu Wei. Beit: Bert pre-training of image transformers. arXiv preprint arXiv:2106.08254 , 2021.

[6] Suzanna Becker and Geoffrey E Hinton. Self-organizing neural network that discovers surfaces in random-dot stereograms. Nature , 1992.

[7] Lukas Bossard, Matthieu Guillaumin, and Luc Van Gool. Food-101–mining discriminative components with random forests. In ECCV , 2014.

[8] Emmanuel Asiedu Brempong, Simon Kornblith, Ting Chen, Niki Parmar, Matthias Minderer, and Mohammad Norouzi. Denoising pretraining for semantic segmentation. In CVPR , 2022.

[9] Tom Brown, Benjamin Mann, Nick Ryder, Melanie Subbiah, Jared D Kaplan, Prafulla Dhariwal, Arvind Neelakantan, Pranav Shyam, Girish Sastry, Amanda Askell, et al. Language models are few-shot learners. NeurIPS , 2020.

[10] Mathilde Caron, Ishan Misra, Julien Mairal, Priya Goyal, Piotr Bojanowski, and Armand Joulin. Unsupervised learning of visual features by contrasting cluster assignments. In NeurIPS , 2020.

[11] Mathilde Caron, Hugo Touvron, Ishan Misra, Hervé Jégou, Julien Mairal, Piotr Bojanowski, and Armand Joulin. Emerging properties in self-supervised vision transformers. In ICCV , 2021.

[12] Soravit Changpinyo, Piyush Sharma, Nan Ding, and Radu Soricut. Conceptual 12m: Pushing web-scale image-text pre-training to recognize long-tail visual concepts. In CVPR , 2021.

[13] Ting Chen, Simon Kornblith, Mohammad Norouzi, and Geoffrey Hinton. A simple framework for contrastive learning of visual representations. In ICML , 2020.

[14] Xinlei Chen, Saining Xie, and Kaiming He. An empirical study of training self-supervised vision transformers. In ICCV , 2021.

[15] Yuhua Chen, Wen Li, Xiaoran Chen, and Luc Van Gool. Learning semantic segmentation from synthetic data: A geometrically guided input-output adaptation approach. In CVPR , 2019.

[16] Gong Cheng, Junwei Han, and Xiaoqiang Lu. Remote sensing image scene classification: Benchmark and state of the art. Proceedings of the IEEE , 2017.

[17] Mehdi Cherti, Romain Beaumont, Ross Wightman, Mitchell Wortsman, Gabriel Ilharco, Cade Gordon, Christoph Schuhmann, Ludwig Schmidt, and Jenia Jitsev. Reproducible scaling laws for contrastive language-image learning. In CVPR , 2023.

[18] Mircea Cimpoi, Subhransu Maji, Iasonas Kokkinos, Sammy Mohamed, and Andrea Vedaldi. Describing textures in the wild. In CVPR , 2014.

[19] Kevin Clark and Priyank Jaini. Text-to-image diffusion models are zero-shot classifiers. arXiv preprint arXiv:2303.15233 , 2023.

[20] Kevin Clark, Minh-Thang Luong, Quoc V Le, and Christopher D Manning. Electra: Pre-training text encoders as discriminators rather than generators. arXiv preprint arXiv:2003.10555 , 2020.

[21] Ekin D Cubuk, Barret Zoph, Jonathon Shlens, and Quoc V Le. Randaugment: Practical automated data augmentation with a reduced search space. In CVPR workshops , 2020.

[22] Marco Cuturi. Sinkhorn distances: Lightspeed computation of optimal transport. In NeurIPS , 2013.

[23] Mostafa Dehghani, Josip Djolonga, Basil Mustafa, Piotr Padlewski, Jonathan Heek, Justin Gilmer, Andreas Peter Steiner, Mathilde Caron, Robert Geirhos, Ibrahim Alabdulmohsin, et al. Scaling vision transformers to 22 billion parameters. In ICML , 2023.

[24] Jia Deng, Wei Dong, Richard Socher, Li-Jia Li, Kai Li, and Li Fei-Fei. Imagenet: A large-scale hierarchical image database. In CVPR , 2009.

[25] Jeff Donahue and Karen Simonyan. Large scale adversarial representation learning. NeurIPS , 2019.

[26] Jeff Donahue, Yangqing Jia, Oriol Vinyals, Judy Hoffman, Ning Zhang, Eric Tzeng, and Trevor Darrell. Decaf: A deep convolutional activation feature for generic visual recognition. In ICML , 2014.

[27] Xiaoyi Dong, Jianmin Bao, Ting Zhang, Dongdong Chen, Weiming Zhang, Lu Yuan, Dong Chen, Fang Wen, Nenghai Yu, and Baining Guo. Peco: Perceptual codebook for bert pre-training of vision transformers. In AAAI , 2023.

[28] Alexey Dosovitskiy, Lucas Beyer, Alexander Kolesnikov, Dirk Weissenborn, Xiaohua Zhai, Thomas Unterthiner, Mostafa Dehghani, Matthias Minderer, Georg Heigold, Sylvain Gelly, et al. An image is worth 16x16 words: Transformers for image recognition at scale. arXiv preprint arXiv:2010.11929 , 2020.

[29] Mark Everingham, Luc Van Gool, Christopher KI Williams, John Winn, and Andrew Zisserman. The pascal visual object classes (voc) challenge. IJCV , 2010.

[30] Lijie Fan, Kaifeng Chen, Dilip Krishnan, Dina Katabi, Phillip Isola, and Yonglong Tian. Scaling laws of synthetic images for model training … for now. arXiv:2312.04567 , 2023a.

[31] Lijie Fan, Dilip Krishnan, Phillip Isola, Dina Katabi, and Yonglong Tian. Improving clip training with language rewrites. In NeurIPS , 2023b.

[32] Yuxin Fang, Quan Sun, Xinggang Wang, Tiejun Huang, Xinlong Wang, and Yue Cao. Eva-02: A visual representation for neon genesis. arXiv preprint arXiv:2303.11331 , 2023a.

[33] Yuxin Fang, Wen Wang, Binhui Xie, Quan Sun, Ledell Wu, Xinggang Wang, Tiejun Huang, Xinlong Wang, and Yue Cao. Eva: Exploring the limits of masked visual representation learning at scale. In CVPR , 2023b.

[34] Li Fei-Fei, Rob Fergus, and Pietro Perona. Learning generative visual models from few training examples: An incremental bayesian approach tested on 101 object categories. In CVPR , 2004.

[35] Andreas Geiger, Philip Lenz, and Raquel Urtasun. Are we ready for autonomous driving? the kitti vision benchmark suite. In CVPR , 2012.

[36] Spyros Gidaris, Praveer Singh, and Nikos Komodakis. Unsupervised representation learning by predicting image rotations. In ICLR , 2018.

[37] Ross Girshick, Jeff Donahue, Trevor Darrell, and Jitendra Malik. Rich feature hierarchies for accurate object detection and semantic segmentation. In CVPR , 2014.

[38] Priya Goyal, Dhruv Mahajan, Abhinav Gupta, and Ishan Misra. Scaling and benchmarking self-supervised visual representation learning. In ICCV , 2019.

[39] Jean-Bastien Grill, Florian Strub, Florent Altché, Corentin Tallec, Pierre Richemond, Elena Buchatskaya, Carl Doersch, Bernardo Avila Pires, Zhaohan Guo, Mohammad Gheshlaghi Azar, et al. Bootstrap your own latent-a new approach to self-supervised learning. In NeurIPS , 2020.

[40] Raia Hadsell, Sumit Chopra, and Yann LeCun. Dimensionality reduction by learning an invariant mapping. In CVPR , 2006.

[41] Kaiming He, Xiangyu Zhang, Shaoqing Ren, and Jian Sun. Deep residual learning for image recognition. In CVPR , 2016.

[42] Kaiming He, Ross Girshick, and Piotr Dollár. Rethinking imagenet pre-training. In ICCV , 2019.

[43] Kaiming He, Haoqi Fan, Yuxin Wu, Saining Xie, and Ross Girshick. Momentum contrast for unsupervised visual representation learning. In CVPR , 2020.

[44] Kaiming He, Xinlei Chen, Saining Xie, Yanghao Li, Piotr Dollár, and Ross Girshick. Masked autoencoders are scalable vision learners. In CVPR , 2022a.

[45] Ruifei He, Shuyang Sun, Xin Yu, Chuhui Xue, Wenqing Zhang, Philip Torr, Song Bai, and Xiaojuan Qi. Is synthetic data from generative models ready for image recognition? arXiv preprint arXiv:2210.07574 , 2022b.

[46] Patrick Helber, Benjamin Bischke, Andreas Dengel, and Damian Borth. Eurosat: A novel dataset and deep learning benchmark for land use and land cover classification. IEEE Journal of Selected Topics in Applied Earth Observations and Remote Sensing , 2019.

[47] Gao Huang, Yu Sun, Zhuang Liu, Daniel Sedra, and Kilian Q Weinberger. Deep networks with stochastic depth. In ECCV , 2016.

[48] Ali Jahanian, Xavier Puig, Yonglong Tian, and Phillip Isola. Generative models as a data source for multiview representation learning. arXiv preprint arXiv:2106.05258 , 2021.

[49] Chao Jia, Yinfei Yang, Ye Xia, Yi-Ting Chen, Zarana Parekh, Hieu Pham, Quoc Le, Yun-Hsuan Sung, Zhen Li, and Tom Duerig. Scaling up visual and vision-language representation learning with noisy text supervision. In ICML , 2021.

[50] Prannay Khosla, Piotr Teterwak, Chen Wang, Aaron Sarna, Yonglong Tian, Phillip Isola, Aaron Maschinot, Ce Liu, and Dilip Krishnan. Supervised contrastive learning. In NeurIPS , 2020.

[51] Jonathan Krause, Jia Deng, Michael Stark, and Li Fei-Fei. Collecting a large-scale dataset of fine-grained cars. tech report , 2013.

[52] Alex Krizhevsky, Ilya Sutskever, and Geoffrey E Hinton. Imagenet classification with deep convolutional neural networks. In NeurIPS , 2012.

[53] Varun Kumar, Ashutosh Choudhary, and Eunah Cho. Data augmentation using pre-trained transformer models. arXiv preprint arXiv:2003.02245 , 2020.

[54] Yann LeCun. The mnist database of handwritten digits. http://yann. lecun. com/exdb/mnist/ , 1998.

[55] Alexander C Li, Mihir Prabhudesai, Shivam Duggal, Ellis Brown, and Deepak Pathak. Your diffusion model is secretly a zero-shot classifier. arXiv preprint arXiv:2303.16203 , 2023a.

[56] Tianhong Li, Huiwen Chang, Shlok Mishra, Han Zhang, Dina Katabi, and Dilip Krishnan. Mage: Masked generative encoder to unify representation learning and image synthesis. In CVPR , 2023b.

[57] Yanghao Li, Saining Xie, Xinlei Chen, Piotr Dollar, Kaiming He, and Ross Girshick. Benchmarking detection transfer learning with vision transformers. arXiv preprint arXiv:2111.11429 , 2021.

[58] Hao Liu, Tom Zahavy, Volodymyr Mnih, and Satinder Singh. Palm up: Playing in the latent manifold for unsupervised pretraining. arXiv preprint arXiv:2210.10913 , 2022.

[59] Ilya Loshchilov and Frank Hutter. Decoupled weight decay regularization. arXiv preprint arXiv:1711.05101 , 2017.

[60] Subhransu Maji, Esa Rahtu, Juho Kannala, Matthew Blaschko, and Andrea Vedaldi. Fine-grained visual classification of aircraft. arXiv:1306.5151 , 2013.

[61] Nikolaus Mayer, Eddy Ilg, Philip Hausser, Philipp Fischer, Daniel Cremers, Alexey Dosovitskiy, and Thomas Brox. A large dataset to train convolutional networks for disparity, optical flow, and scene flow estimation. In CVPR , 2016.

[62] Yu Meng, Jiaxin Huang, Yu Zhang, and Jiawei Han. Generating training data with language models: Towards zero-shot language understanding. arXiv preprint arXiv:2202.04538 , 2022.

[63] Masato Mimura, Sei Ueno, Hirofumi Inaguma, Shinsuke Sakai, and Tatsuya Kawahara. Leveraging sequence-to-sequence speech synthesis for enhancing acoustic-to-word speech recognition. In SLT , 2018.

[64] Maria-Elena Nilsback and Andrew Zisserman. Automated flower classification over a large number of classes. In Indian Conference on Computer Vision, Graphics & Image Processing , 2008.

[65] Mehdi Noroozi and Paolo Favaro. Unsupervised learning of visual representations by solving jigsaw puzzles. In ECCV , 2016.

[66] Aaron van den Oord, Yazhe Li, and Oriol Vinyals. Representation learning with contrastive predictive coding. arXiv preprint arXiv:1807.03748 , 2018.

[67] OpenAI. Gpt-4 technical report. arXiv preprint arXiv:2303.08774 , 2023.

[68] Maxime Oquab, Timothée Darcet, Théo Moutakanni, Huy Vo, Marc Szafraniec, Vasil Khalidov, Pierre Fernandez, Daniel Haziza, Francisco Massa, Alaaeldin El-Nouby, et al. Dinov2: Learning robust visual features without supervision. arXiv preprint arXiv:2304.07193 , 2023.

[69] Omkar M Parkhi, Andrea Vedaldi, Andrew Zisserman, and CV Jawahar. Cats and dogs. In CVPR , 2012.

[70] Zhiliang Peng, Li Dong, Hangbo Bao, Qixiang Ye, and Furu Wei. Beit v2: Masked image modeling with vector-quantized visual tokenizers. arXiv preprint arXiv:2208.06366 , 2022.

[71] Alec Radford, Jong Wook Kim, Chris Hallacy, Aditya Ramesh, Gabriel Goh, Sandhini Agarwal, Girish Sastry, Amanda Askell, Pamela Mishkin, Jack Clark, et al. Learning transferable visual models from natural language supervision. In ICML , 2021.

[72] Robin Rombach, Andreas Blattmann, Dominik Lorenz, Patrick Esser, and Björn Ommer. High-resolution image synthesis with latent diffusion models. In CVPR , 2022a.

[73] Robin Rombach, Andreas Blattmann, Dominik Lorenz, Patrick Esser, and Björn Ommer. High-resolution image synthesis with latent diffusion models. In CVPR , 2022b.

[74] Andrew Rosenberg, Yu Zhang, Bhuvana Ramabhadran, Ye Jia, Pedro Moreno, Yonghui Wu, and Zelin Wu. Speech recognition with augmented synthesized speech. In ASRU , 2019.

[75] Nick Rossenbach, Albert Zeyer, Ralf Schlüter, and Hermann Ney. Generating synthetic audio data for attention-based speech recognition systems. In ICASSP , 2020.

[76] Yangjun Ruan, Saurabh Singh, Warren Morningstar, Alexander A Alemi, Sergey Ioffe, Ian Fischer, and Joshua V Dillon. Weighted ensemble self-supervised learning. arXiv preprint arXiv:2211.09981 , 2022.

[77] Chitwan Saharia, William Chan, Saurabh Saxena, Lala Li, Jay Whang, Emily L Denton, Kamyar Ghasemipour, Raphael Gontijo Lopes, Burcu Karagol Ayan, Tim Salimans, et al. Photorealistic text-to-image diffusion models with deep language understanding. In NeurIPS , 2022.

[78] Mert Bulent Sariyildiz, Karteek Alahari, Diane Larlus, and Yannis Kalantidis. Fake it till you make it: Learning transferable representations from synthetic imagenet clones. In CVPR , 2023.

[79] Saurabh Saxena, Charles Herrmann, Junhwa Hur, Abhishek Kar, Mohammad Norouzi, Deqing Sun, and David J Fleet. The surprising effectiveness of diffusion models for optical flow and monocular depth estimation. arXiv preprint arXiv:2306.01923 , 2023.

[80] Christoph Schuhmann, Romain Beaumont, Richard Vencu, Cade Gordon, Ross Wightman, Mehdi Cherti, Theo Coombes, Aarush Katta, Clayton Mullis, Mitchell Wortsman, et al. Laion-5b: An open large-scale dataset for training next generation image-text models. In NeurIPS , 2022.

[81] Ali Sharif Razavian, Hossein Azizpour, Josephine Sullivan, and Stefan Carlsson. Cnn features off-the-shelf: an astounding baseline for recognition. In CVPR workshops , 2014.

[82] Noam Shazeer. Glu variants improve transformer. arXiv preprint arXiv:2002.05202 , 2020.

[83] David Silver, Julian Schrittwieser, Karen Simonyan, Ioannis Antonoglou, Aja Huang, Arthur Guez, Thomas Hubert, Lucas Baker, Matthew Lai, Adrian Bolton, et al. Mastering the game of go without human knowledge. Nature , 2017.

[84] Karen Simonyan and Andrew Zisserman. Very deep convolutional networks for large-scale image recognition. arXiv preprint arXiv:1409.1556 , 2014.

[85] Johannes Stallkamp, Marc Schlipsing, Jan Salmen, and Christian Igel. The german traffic sign recognition benchmark: a multi-class classification competition. In IJCNN , 2011.

[86] Andreas Steiner, Alexander Kolesnikov, Xiaohua Zhai, Ross Wightman, Jakob Uszkoreit, and Lucas Beyer. How to train your vit? data, augmentation, and regularization in vision transformers. arXiv preprint arXiv:2106.10270 , 2021.

[87] Rohan Taori, Ishaan Gulrajani, Tianyi Zhang, Yann Dubois, Xuechen Li, Carlos Guestrin, Percy Liang, and Tatsunori B Hashimoto. Alpaca: A strong, replicable instruction-following model. Stanford Center for Research on Foundation Models. , 2023.

[88] Yonglong Tian, Dilip Krishnan, and Phillip Isola. Contrastive multiview coding. arXiv:1906.05849 , 2019.

[89] Yonglong Tian, Chen Sun, Ben Poole, Dilip Krishnan, Cordelia Schmid, and Phillip Isola. What makes for good views for contrastive learning? In NeurIPS , 2020.

[90] Yonglong Tian, Olivier J Henaff, and Aäron van den Oord. Divide and contrast: Self-supervised learning from uncurated data. In ICCV , 2021.

[91] Yonglong Tian, Lijie Fan, Phillip Isola, Huiwen Chang, and Dilip Krishnan. Stablerep: Synthetic images from text-to-image models make strong visual representation learners. In NeurIPS , 2023.

[92] Hugo Touvron, Matthieu Cord, Alexandre Sablayrolles, Gabriel Synnaeve, and Hervé Jégou. Going deeper with image transformers. In ICCV , 2021.

[93] Hugo Touvron, Louis Martin, Kevin Stone, Peter Albert, Amjad Almahairi, Yasmine Babaei, Nikolay Bashlykov, Soumya Batra, Prajjwal Bhargava, Shruti Bhosale, et al. Llama 2: Open foundation and fine-tuned chat models. arXiv preprint arXiv:2307.09288 , 2023.

[94] Gul Varol, Javier Romero, Xavier Martin, Naureen Mahmood, Michael J Black, Ivan Laptev, and Cordelia Schmid. Learning from synthetic humans. In CVPR , 2017.

[95] Tongzhou Wang and Phillip Isola. Understanding contrastive representation learning through alignment and uniformity on the hypersphere. In ICML , 2020.

[96] Chen Wei, Haoqi Fan, Saining Xie, Chao-Yuan Wu, Alan Yuille, and Christoph Feichtenhofer. Masked feature prediction for self-supervised visual pre-training. In CVPR , 2022.

[97] Zhirong Wu, Yuanjun Xiong, Stella X Yu, and Dahua Lin. Unsupervised feature learning via non-parametric instance discrimination. In CVPR , 2018.

[98] Jianxiong Xiao, James Hays, Krista A Ehinger, Aude Oliva, and Antonio Torralba. Sun database: Large-scale scene recognition from abbey to zoo. In CVPR , 2010.

[99] Tete Xiao, Yingcheng Liu, Bolei Zhou, Yuning Jiang, and Jian Sun. Unified perceptual parsing for scene understanding. In ECCV , 2018.

[100] Zhenda Xie, Zheng Zhang, Yue Cao, Yutong Lin, Jianmin Bao, Zhuliang Yao, Qi Dai, and Han Hu. Simmim: A simple framework for masked image modeling. In CVPR , 2022.

[101] Jiarui Xu, Sifei Liu, Arash Vahdat, Wonmin Byeon, Xiaolong Wang, and Shalini De Mello. Open-vocabulary panoptic segmentation with text-to-image diffusion models. In CVPR , 2023.

[102] Yiben Yang, Chaitanya Malaviya, Jared Fernandez, Swabha Swayamdipta, Ronan Le Bras, Ji-Ping Wang, Chandra Bhagavatula, Yejin Choi, and Doug Downey. Generative data augmentation for commonsense reasoning. arXiv preprint arXiv:2004.11546 , 2020.

[103] Sangdoo Yun, Dongyoon Han, Seong Joon Oh, Sanghyuk Chun, Junsuk Choe, and Youngjoon Yoo. Cutmix: Regularization strategy to train strong classifiers with localizable features. In ICCV , 2019.

[104] Xiaohua Zhai, Alexander Kolesnikov, Neil Houlsby, and Lucas Beyer. Scaling vision transformers. In CVPR , 2022.

[105] Hongyi Zhang, Moustapha Cisse, Yann N Dauphin, and David Lopez-Paz. mixup: Beyond empirical risk minimization. arXiv preprint arXiv:1710.09412 , 2017.

[106] Richard Zhang, Phillip Isola, and Alexei A Efros. Colorful image colorization. In ECCV , 2016.

[107] Wenliang Zhao, Yongming Rao, Zuyan Liu, Benlin Liu, Jie Zhou, and Jiwen Lu. Unleashing text-to-image diffusion models for visual perception. arXiv preprint arXiv:2303.02153 , 2023.

[108] Bolei Zhou, Aditya Khosla, Agata Lapedriza, Aude Oliva, and Antonio Torralba. Learning deep features for discriminative localization. In CVPR , 2016.

[109] Bolei Zhou, Hang Zhao, Xavier Puig, Tete Xiao, Sanja Fidler, Adela Barriuso, and Antonio Torralba. Semantic understanding of scenes through the ade20k dataset. IJCV , 2019.

[110] Jinghao Zhou, Chen Wei, Huiyu Wang, Wei Shen, Cihang Xie, Alan Yuille, and Tao Kong. ibot: Image bert pre-training with online tokenizer. arXiv preprint arXiv:2111.07832 , 2021.

[111] Yongchao Zhou, Hshmat Sahak, and Jimmy Ba. Training on thin air: Improve image classification with generated data. arXiv preprint arXiv:2305.15316 , 2023.

## Appendix A Concept Sampling

The concepts used to synthesize captions are randomly sampled from the names of various datasets. The rough ratios are presented in Table 11 . It is likely that different combinations of these ratios lead to different results, but we do not optimize over this dimension. For example, we simply concatenate IN-21k concepts with the classes of other datasets ( e.g . , Caltech-101, Pets), and do uniform sampling from the concatenated list. This may lead to under-sampling for other datasets, as the list is dominated by IN-21 classes.

## Appendix B Implementation Details

### B.1 Pre-training

The setting for our final long schedule training in Section 4.2 is summarized in Table 12 , where models are trained for 500k steps with a batch size of 8192 captions. For ablation study present in Section 4.1, we only train for 85k steps with a batch size of 2048 captions; for the scaling plots in Section 4.3, we train all models for 300k steps with a batch size of 2048.

### B.2 ImageNet linear probing

We use the cls token from the final transformer block as the image representation. This is different from DINO v2, which tries to concatenate cls token with average pooled patch tokens and sweep over whether to use multiple layers.

We follow prior work [ 14 , 11 ] to train the linear classifier. It has been generally observed that regularization such as weight decay hurts the performance [ 88 , 43 ] . Therefore, we set weight decay as 0, and we sweep the b ​ a ​ s ​ e ​ _ ​ l ​ r base\_lr over { 0.1 , 0.2 , 0.5 , 1 , 2 , 5 , 10 , 20 , 50 } × 10 − 2 \{0.1,0.2,0.5,1,2,5,10,20,50\}\times 10^{-2} .

### B.3 End-to-End ImageNet fine-tuning

Following common practice [ 5 , 44 ] , we append a linear classifier on top of the CLS token of the last transformer block, and fine-tune the whole network. We use layer-wise lr decay [ 20 ] . Table 14 shows the settings.

### B.4 Semantic segmentation on ADE20k

We conduct the experiments on ADE20k [ 109 ] . Following [ 5 , 44 ] , we use UperNet [ 99 ] as the task adaptation layer. We use the common single-scale [ 5 ] setup, with a resolution of 512 × \times 512 for models with a patch size of 16 × \times 16 and a resolution of 518 × \times 518 for models with a patch size of 14 × \times 14. The hyper-parameters are summarized in Table 15 .

### B.5 Fine-grained linear classification

Following prior works [ 13 , 39 ] , we train a regularized multi-nomial logistic regression model upon the output CLS token. In training and testing, we do not perform any data augmentation; images are resized to 224 pixels along the shorter side, followed by a center crop of 224 × \times 224. We minimize the cross-entropy objective using L-BFGS with ℓ 2 \ell_{2} -regularization. We select this ℓ 2 \ell_{2} -regularization constant on the validation set over 45 logarithmically spaced values between 10 − 6 10^{-6} and 10 5 10^{5} . The maximum number of L-BFGS iterations is set to 1000 1000 , similar as that in DINO v2 [ 68 ] .

## Appendix C In-context Learning Examples

All of the three types of in-context examples are summarized in Table 16 , Table 17 , and Table 18 , respectively.

## Instructions for reporting errors

We are continuing to improve HTML versions of papers, and your feedback helps enhance accessibility and mobile support. To report errors in the HTML that will help us improve conversion and rendering, choose any of the methods listed below:

Click the "Report Issue" ( ) button, located in the page header.

Tip: You can select the relevant text first, to include it in your report.

Our team has already identified the following issues . We appreciate your time reviewing and reporting rendering errors we may not have found yet. Your efforts will help us improve the HTML versions for all readers, because disability should not be a barrier to accessing research. Thank you for your continued support in championing open access for all.

Have a free development cycle? Help support accessibility at arXiv! Our collaborators at LaTeXML maintain a list of packages that need conversion , and welcome developer contributions .
