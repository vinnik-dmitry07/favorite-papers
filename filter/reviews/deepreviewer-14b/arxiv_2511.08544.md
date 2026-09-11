Of course. I will use Fast Mode for quick thinking. As a professional reviewer, I will directly output a detailed evaluation of this paper. Let me think - Fast Mode means I will directly output a Summary, followed by scores for Soundness, Presentation and Contribution, then provide analysis of Strengths, Weaknesses, Suggestions, and Questions. Finally, I will output the Rating, Confidence and Decision:

\boxed_review{
## Summary:

In this paper, the authors introduce LeJEPA, a novel self-supervised learning (SSL) framework that aims to address the issue of representation collapse, a common problem in Joint Embedding Predictive Architectures (JEPAs). The core contribution of the paper is the theoretical proof that an isotropic Gaussian distribution is the optimal embedding distribution for minimizing downstream prediction risk. Based on this theoretical insight, the authors propose a new regularization term, SIGReg, which encourages the learned embeddings to follow an isotropic Gaussian distribution. The combination of the JEPA predictive loss and SIGReg results in the LeJEPA objective. The empirical evaluation of LeJEPA is extensive, covering a wide range of datasets and architectures, and demonstrating competitive performance, particularly in in-domain transfer learning scenarios. The paper is well-written and provides a solid theoretical foundation for the proposed method, but it has several limitations that need to be addressed, including the lack of a direct comparison with DINO on ImageNet, the absence of linear probing results, and the need for a more detailed analysis of the computational cost and the impact of the hyperparameter λ. Despite these limitations, the paper makes a significant contribution to the field of SSL by providing a theoretically grounded and empirically validated approach to preventing representation collapse.


## Soundness:

3.25


## Presentation:

3.25


## Contribution:

3.25


## Strengths:

The paper's strengths lie in its strong theoretical foundation and the extensive empirical validation of the proposed method. The authors provide a rigorous mathematical proof that an isotropic Gaussian distribution is the optimal embedding distribution for minimizing downstream prediction risk, which is a novel and valuable contribution to the field of self-supervised learning. This theoretical insight is well-motivated and clearly presented, making the paper accessible to a broad audience. The introduction of SIGReg as a regularization term to enforce this distribution is innovative and addresses a key challenge in JEPAs, namely representation collapse. The authors also demonstrate the practical effectiveness of LeJEPA across a variety of datasets and architectures, including both convolutional and transformer models. The empirical results show that LeJEPA can achieve competitive performance, particularly in in-domain transfer learning scenarios, where it outperforms state-of-the-art models like DINOv2. The paper is well-organized, with clear sections that guide the reader through the theoretical derivations, methodological implementation, and experimental results. The authors also provide a detailed discussion of the implementation details, which is valuable for reproducibility. Overall, the paper's strengths are its solid theoretical grounding, innovative methodological approach, and extensive empirical validation, which together make a compelling case for the effectiveness of LeJEPA.


## Weaknesses:

Despite the paper's strengths, there are several verified limitations that need to be addressed. One of the most significant concerns is the lack of a direct comparison with DINO on ImageNet using the standard linear probing evaluation protocol. The paper primarily uses full fine-tuning results on ImageNet, which is not the standard benchmark for evaluating self-supervised learning methods. The absence of linear probing results makes it difficult to assess the quality of the learned representations and to compare them with other state-of-the-art methods. This is a critical gap, as linear probing is a widely accepted metric for evaluating the transferability of SSL models. Another limitation is the lack of a detailed analysis of the computational cost of LeJEPA. While the authors claim that the method has linear time and memory complexity, they do not provide a direct comparison of wall-clock training times or computational resources with other methods. This makes it challenging to evaluate the practical scalability and efficiency of LeJEPA, especially in large-scale settings. Additionally, the paper does not include a systematic study of the impact of the hyperparameter λ, which balances the JEPA prediction loss and the SIGReg term. The sensitivity of the model to different values of λ and guidelines for selecting an appropriate value are missing, which is important for practical application. The paper also lacks a thorough discussion of the limitations of the isotropic Gaussian assumption. While the authors provide a theoretical justification for this assumption, they do not explore scenarios where it might not hold or discuss potential modifications to the method to handle more complex data distributions. Furthermore, the paper could benefit from a more detailed analysis of the learned representations, including visualizations and qualitative assessments, to provide deeper insights into the method's behavior. The presentation of the paper could also be improved by addressing minor grammatical errors and ensuring consistent formatting, which would enhance its readability and professionalism. Finally, the paper does not provide a comprehensive comparison of the learned embedding distributions with and without SIGReg, particularly in terms of visualizations and quantitative metrics, which would help to better understand the role of the regularization term. These limitations, while not undermining the overall contribution of the paper, are important for a more complete and practical evaluation of the proposed method.


## Suggestions:

To address the identified limitations, I suggest the following concrete and actionable improvements. First, the authors should include a direct comparison with DINO on ImageNet using the standard linear probing evaluation protocol. This would provide a more accurate and widely accepted benchmark for evaluating the quality of the learned representations and would facilitate a fair comparison with other state-of-the-art methods. The authors should report the top-1 accuracy of linear probes on ImageNet, as this is the conventional metric used in the field. Second, the paper should include a detailed analysis of the computational cost of LeJEPA. This should involve a comparison of wall-clock training times and computational resources (e.g., FLOPs, memory usage) with other methods, particularly DINO and SigLIP. The authors should also discuss the scalability of LeJEPA to larger datasets and models, including any potential bottlenecks or limitations. Third, the authors should conduct a systematic study of the impact of the hyperparameter λ. This should include experiments with different values of λ and an analysis of the resulting performance on various datasets and architectures. The authors should provide guidelines for selecting an appropriate value of λ based on the characteristics of the dataset and the model. Fourth, the paper should include a more detailed discussion of the limitations of the isotropic Gaussian assumption. The authors should explore scenarios where this assumption might not hold and discuss potential modifications to the method to handle more complex data distributions. This would provide a more complete theoretical understanding of the proposed approach. Fifth, the authors should enhance the analysis of the learned representations by including visualizations (e.g., t-SNE or UMAP) and qualitative assessments. This would help to understand the semantic structure of the embeddings and how they relate to the input data. The authors should also compare the learned representations with those of other methods, such as DINO, to provide a more comprehensive evaluation. Finally, the authors should address minor grammatical errors and ensure consistent formatting throughout the paper. This would improve the readability and professionalism of the manuscript. By implementing these suggestions, the authors can provide a more robust and practical evaluation of LeJEPA, which would strengthen the paper's contribution to the field of self-supervised learning.


## Questions:

I have a few key questions that I believe would help to clarify and strengthen the paper. First, why did the authors choose to use full fine-tuning results on ImageNet instead of the standard linear probing evaluation? Is there a specific reason or advantage to using full fine-tuning in this context, and how does it relate to the linear probing results that are typically reported in the literature? Second, could the authors provide more details on the computational cost of LeJEPA, including a comparison of wall-clock training times and resource usage with other methods like DINO and SigLIP? This would help to understand the practical efficiency and scalability of the proposed method. Third, how sensitive is the model to the hyperparameter λ, and what are the guidelines for selecting an appropriate value? It would be useful to see a systematic study of the impact of λ on performance across different datasets and architectures. Fourth, what are the limitations of the isotropic Gaussian assumption, and how might the method be modified to handle more complex data distributions? This would provide a more complete theoretical understanding of the proposed approach. Finally, could the authors provide visualizations and qualitative assessments of the learned representations, and compare them with those of other methods like DINO? This would help to understand the semantic structure of the embeddings and their practical utility.


## Rating:

7.0


## Confidence:

3.5


## Decision:

Accept
}