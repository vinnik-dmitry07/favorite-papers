##### Report GitHub Issue

Content selection saved. Describe the issue below:

# GLU Variants Improve Transformer

###### Abstract

Gated Linear Units [ Dauphin et al., 2016 ] consist of the component-wise product of two linear projections, one of which is first passed through a sigmoid function. Variations on GLU are possible, using different nonlinear (or even linear) functions in place of sigmoid. We test these variants in the feed-forward sublayers of the Transformer [ Vaswani et al., 2017 ] sequence-to-sequence model, and find that some of them yield quality improvements over the typically-used ReLU or GELU activations.

## 1 Introduction

The Transformer [ Vaswani et al., 2017 ] sequence-to-sequence model alternates between multi-head attention, and what it calls "position-wise feed-forward networks" (FFN). The FFN takes a vector x x (the hidden representation at a particular position in the sequence) and passes it through two learned linear transformations, (represented by the matrices W 1 W_{1} and W 2 W_{2} and bias vectors b 1 b_{1} and b 2 b_{2} ). A rectified-linear (ReLU) [ Glorot et al., 2011 ] activation function applied between the two linear transformations.

FFN ​ ( x , W 1 , W 2 , b 1 , b 2 ) = max ​ ( 0 , x ​ W 1 + b 1 ) ​ W 2 + b 2 \textrm{FFN}(x,W_{1},W_{2},b_{1},b_{2})=\textrm{max}(0,xW_{1}+b_{1})W_{2}+b_{2} (1)

Following the T5 codebase [ Raffel et al., 2019 ] 1 1 1 Also in the interest of ML fairness. , we use a version with no bias:

FFN ReLU ​ ( x , W 1 , W 2 ) = max ​ ( x ​ W 1 , 0 ) ​ W 2 \textrm{FFN}_{\textrm{ReLU}}(x,W_{1},W_{2})=\textrm{max}(xW_{1},0)W_{2} (2)

Subsequent work has proposed replacing the ReLU with other nonlinear activation functions such as Gaussian Error Linear Units, GELU ​ ( x ) = x ​ Φ ​ ( x ) \textrm{GELU}(x)=x\Phi(x) [ Hendrycks and Gimpel, 2016 ] , and Swish β ​ ( x ) = x ​ σ ​ ( β ​ x ) \textrm{Swish}_{\beta}(x)=x\sigma(\beta x) [ Ramachandran et al., 2017 ] .

FFN GELU ​ ( x , W 1 , W 2 ) = GELU ​ ( x ​ W 1 ) ​ W 2 FFN Swish ​ ( x , W 1 , W 2 ) = Swish 1 ​ ( x ​ W 1 ) ​ W 2 \begin{split}\textrm{FFN}_{\textrm{GELU}}(x,W_{1},W_{2})&=\textrm{GELU}(xW_{1})W_{2}\\ \textrm{FFN}_{\textrm{Swish}}(x,W_{1},W_{2})&=\textrm{Swish}_{1}(xW_{1})W_{2}\end{split} (3)

## 2 Gated Linear Units (GLU) and Variants

[ Dauphin et al., 2016 ] introduced Gated Linear Units (GLU), a neural network layer defined as the component-wise product of two linear transformations of the input, one of which is sigmoid-activated. They also suggest omitting the activation, which they call a "bilinear" layer and attribute to [ Mnih and Hinton, 2007 ] .

GLU ​ ( x , W , V , b , c ) = σ ⁡ ( x ​ W + b ) ⊗ ( x ​ V + c ) Bilinear ​ ( x , W , V , b , c ) = ( x ​ W + b ) ⊗ ( x ​ V + c ) \begin{split}\textrm{GLU}(x,W,V,b,c)&=\sigma(xW+b)\otimes(xV+c)\\ \textrm{Bilinear}(x,W,V,b,c)&=(xW+b)\otimes(xV+c)\end{split} (4)

We can also define GLU variants using other activation functions:

ReGLU ​ ( x , W , V , b , c ) = max ​ ( 0 , x ​ W + b ) ⊗ ( x ​ V + c ) GEGLU ​ ( x , W , V , b , c ) = GELU ​ ( x ​ W + b ) ⊗ ( x ​ V + c ) SwiGLU ​ ( x , W , V , b , c , β ) = Swish β ​ ( x ​ W + b ) ⊗ ( x ​ V + c ) \begin{split}\textrm{ReGLU}(x,W,V,b,c)&=\textrm{max}(0,xW+b)\otimes(xV+c)\\ \textrm{GEGLU}(x,W,V,b,c)&=\textrm{GELU}(xW+b)\otimes(xV+c)\\ \textrm{SwiGLU}(x,W,V,b,c,\beta)&=\textrm{Swish}_{\beta}(xW+b)\otimes(xV+c)\\ \end{split} (5)

In this paper, we propose additional variations on the Transformer FFN layer which use GLU or one of its variants in place of the first linear transformation and the activation function. Again, we omit the bias terms.

FFN GLU ​ ( x , W , V , W 2 ) = ( σ ⁡ ( x ​ W ) ⊗ x ​ V ) ​ W 2 FFN Bilinear ​ ( x , W , V , W 2 ) = ( x ​ W ⊗ x ​ V ) ​ W 2 FFN ReGLU ​ ( x , W , V , W 2 ) = ( max ​ ( 0 , x ​ W ) ⊗ x ​ V ) ​ W 2 FFN GEGLU ​ ( x , W , V , W 2 ) = ( GELU ​ ( x ​ W ) ⊗ x ​ V ) ​ W 2 FFN SwiGLU ​ ( x , W , V , W 2 ) = ( Swish 1 ​ ( x ​ W ) ⊗ x ​ V ) ​ W 2 \begin{split}\textrm{FFN}_{\textrm{GLU}}(x,W,V,W_{2})&=(\sigma(xW)\otimes xV)W_{2}\\ \textrm{FFN}_{\textrm{Bilinear}}(x,W,V,W_{2})&=(xW\otimes xV)W_{2}\\ \textrm{FFN}_{\textrm{ReGLU}}(x,W,V,W_{2})&=(\textrm{max}(0,xW)\otimes xV)W_{2}\\ \textrm{FFN}_{\textrm{GEGLU}}(x,W,V,W_{2})&=(\textrm{GELU}(xW)\otimes xV)W_{2}\\ \textrm{FFN}_{\textrm{SwiGLU}}(x,W,V,W_{2})&=(\textrm{Swish}_{1}(xW)\otimes xV)W_{2}\\ \end{split} (6)

All of these layers have three weight matrices, as opposed to two for the original FFN. To keep the number of parameters and the amount of computation constant, we reduce the number of hidden units d f ​ f d_{ff} (the second dimension of W W and V V and the first dimension of W 2 W_{2} ) by a factor of 2 3 \frac{2}{3} when comparing these layers to the original two-matrix version.

## 3 Experiments on Text-to-Text Transfer Transformer (T5)

We test the FFN variants we have described on the transfer-learning setup from [ Raffel et al., 2019 ] . An encoder-decoder transformer model [ Vaswani et al., 2017 ] is trained on a denoising objective of predicting missing text segments, and subsequently fine-tuned on various language understanding tasks.

### 3.1 Model Architecture

We use the same code base, model architecture, and training task as the base model from [ Raffel et al., 2019 ] . The encoder and decoder each consist of 12 layers, with d m ​ o ​ d ​ e ​ l = 768 d_{model}=768 . For the attention layers, h = 12 h=12 and d k = d v = 64 d_{k}=d_{v}=64 . The FFN layers have hidden size d f ​ f = 3072 d_{ff}=3072 . As we describe above, for the GLU-variant-based FFN layers, which have thee weight matrices instead of two, we reduce the hidden layer to d f ​ f = 2048 d_{ff}=2048 , so as to maintain the same parameter and operation counts as the base model.

### 3.2 Pre-Training and Perplexity Results

Identically to [ Raffel et al., 2019 ] , we pre-train for 524,288 steps on the span-filling objective on the C4 dataset. Each training batch consists of 128 examples, each of which has an input of 512 tokens and an output of 114 tokens, the output containing multiple spans of tokens which were deleted from the input 2 2 2 Each training step took approximately 0.15 seconds on a 32-core TPUv2 cluster. . Similarly to [ Raffel et al., 2019 ] , we use the Adafactor optimizer [ Shazeer and Stern, 2018 ] and an inverse-square-root learning-rate schedule. We also decay the learning rate linearly for the final 10 percent of the training steps. Our main departure from [ Raffel et al., 2019 ] is that we use no dropout during pre-training. We find this to produce superior results. We compute the log-perplexity on the training objective on a heldout shard of C4, which we believe to be a good indicator of model quality. For each model architecture, we also trained four models for a shorter period (65,536 steps) to measure inter-run variability. The results are listed in table 1 . The GEGLU and SwiGLU variants produce the best perplexities.

### 3.3 Fine-Tuning

We then fine-tune each fully-trained model once on an examples-proportional mixture of the Stanford Question-Answering Dataset (SQuAD) [ Rajpurkar et al., 2016 ] and all the language understanding tasks in the GLUE [ Wang et al., 2018 ] and SuperGlue [ Wang et al., 2019 ] benchmarks. 3 3 3 This departs from [ Raffel et al., 2019 ] , who fine-tuned separately on the different tasks. We chose one fine-tuning run for simplicity. Fine-tuning consists of 131072 steps with a learning rate of 10 − 3 10^{-3} . As in training, the input sequences for each step have a combined length of approximately 65,536 tokens. Following [ Raffel et al., 2019 ] , we use a dropout rate of 0.1 0.1 on the layer outputs, feed-forward hidden-layers and attention weights. The embedding matrices are fixed during fine-tuning.

Tables 2 , 3 and 4 show results on the development sets. For each task, we report the best score of any of the checkpoints recorded during fine-tuning. While the results are noisy, the new GLU-variants perform best on most of the tasks. For comparison, at the bottom of each of the tables we list the reuslts from [ Raffel et al., 2019 ] . The model is identical to our FFN ReLU \textrm{FFN}_{\textrm{ReLU}} model. Their results are notably worse, which we believe was caused by their use of dropout during pre-training. Also listed are the inter-run standard deviations measured by [ Raffel et al., 2019 ] .

## 4 Conclusions

We have extended the GLU family of layers and proposed their use in Transformer. In a transfer-learning setup, the new variants seem to produce better perplexities for the de-noising objective used in pre-training, as well as better results on many downstream language-understanding tasks. These architectures are simple to implement, and have no apparent computational drawbacks. We offer no explanation as to why these architectures seem to work; we attribute their success, as all else, to divine benevolence.

## References

Dauphin et al. [2016] Yann N. Dauphin, Angela Fan, Michael Auli, and David Grangier. Language modeling with gated convolutional networks. CoRR , abs/1612.08083, 2016. URL http://arxiv.org/abs/1612.08083 .

Glorot et al. [2011] Xavier Glorot, Antoine Bordes, and Yoshua Bengio. Deep sparse rectifier neural networks. In Proceedings of the fourteenth international conference on artificial intelligence and statistics , pages 315–323, 2011.

Hendrycks and Gimpel [2016] Dan Hendrycks and Kevin Gimpel. Bridging nonlinearities and stochastic regularizers with gaussian error linear units. CoRR , abs/1606.08415, 2016. URL http://arxiv.org/abs/1606.08415 .

Mnih and Hinton [2007] Andriy Mnih and Geoffrey Hinton. Three new graphical models for statistical language modelling. In Proceedings of the 24th international conference on Machine learning , pages 641–648, 2007.

Raffel et al. [2019] Colin Raffel, Noam Shazeer, Adam Roberts, Katherine Lee, Sharan Narang, Michael Matena, Yanqi Zhou, Wei Li, and Peter Liu. Exploring the limits of transfer learning with a unified text-to-text transformer. arXiv e-prints , 2019.

Rajpurkar et al. [2016] Pranav Rajpurkar, Jian Zhang, Konstantin Lopyrev, and Percy Liang. Squad: 100,000+ questions for machine comprehension of text. arXiv preprint arXiv:1606.05250 , 2016.

Ramachandran et al. [2017] Prajit Ramachandran, Barret Zoph, and Quoc V Le. Searching for activation functions. arXiv preprint arXiv:1710.05941 , 2017.

Shazeer and Stern [2018] Noam Shazeer and Mitchell Stern. Adafactor: Adaptive learning rates with sublinear memory cost. arXiv preprint arXiv:1804.04235 , 2018.

Vaswani et al. [2017] Ashish Vaswani, Noam Shazeer, Niki Parmar, Jakob Uszkoreit, Llion Jones, Aidan N. Gomez, Lukasz Kaiser, and Illia Polosukhin. Attention is all you need. In NIPS , 2017.

Wang et al. [2018] Alex Wang, Amapreet Singh, Julian Michael, Felix Hill, Omer Levy, and Samuel R. Bowman. GLUE: A multi-task benchmark and analysis platform for natural language understanding. arXiv preprint arXiv:1804.07461 , 2018.

Wang et al. [2019] Alex Wang, Yada Pruksachatkun, Nikita Nangia, Amanpreet Singh, Julian Michael, Felix Hill, Omer Levy, and Samuel R. Bowman. Superglue: A stickier benchmark for general-purpose language understanding systems. arXiv preprint arXiv:1905.00537 , 2019.

## Instructions for reporting errors

We are continuing to improve HTML versions of papers, and your feedback helps enhance accessibility and mobile support. To report errors in the HTML that will help us improve conversion and rendering, choose any of the methods listed below:

Click the "Report Issue" ( ) button, located in the page header.

Tip: You can select the relevant text first, to include it in your report.

Our team has already identified the following issues . We appreciate your time reviewing and reporting rendering errors we may not have found yet. Your efforts will help us improve the HTML versions for all readers, because disability should not be a barrier to accessing research. Thank you for your continued support in championing open access for all.

Have a free development cycle? Help support accessibility at arXiv! Our collaborators at LaTeXML maintain a list of packages that need conversion , and welcome developer contributions .
