 **Summary:**
The paper investigates the use of Centered Kernel Alignment (CKA) as a metric for comparing neural data from both artificial and biological neural networks. It highlights the issues with biased CKA, particularly in scenarios where the feature-sample ratio is imbalanced, which can lead to misleading conclusions. The authors propose a debiased version of CKA to address these issues and demonstrate its effectiveness using datasets like fMRI and MEG data from the THINGS project. The study also explores the sensitivity of CKA to shuffled data and its ability to detect stimuli-driven responses in neural data. Despite its strengths in addressing a significant issue in CKA and providing a valuable resource in the form of the THINGS dataset, the paper has been critiqued for its limited scope, lack of comprehensive comparisons with other metrics, and potential misleading conclusions due to the small dataset size.

**Strengths:**
- The paper addresses a significant issue with biased CKA, which can lead to misleading conclusions when comparing neural data from biological and artificial neural networks.
- The authors provide a clear and detailed explanation of the issue, supported by experiments that demonstrate the inadequacy of biased CKA and the effectiveness of the debiased version.
- The manuscript is well-written, with clear and concise explanations that make it accessible to readers.
- The paper includes a valuable resource in the form of the THINGS dataset, which is beneficial for the community.
- The authors have highlighted an important issue with CKA that is often overlooked, and their findings could be crucial for the community using CKA for brain-model alignment.

**Weaknesses:**
- The paper lacks a comprehensive comparison with other metrics, which could have provided a more robust evaluation of the debiased CKA.
- The experiments are limited to a small dataset (720 images), which might not generalize well to larger or more diverse datasets.
- The paper's conclusions are potentially misleading due to the small dataset size and the lack of diversity in the dataset.
- The paper does not sufficiently address the limitations of its work, such as the generalizability of the findings to other datasets and the potential impact of different preprocessing methods on the results.
- The paper could benefit from a more detailed discussion on the choice of kernels and their impact on the results.
- There is a lack of comparison with other metrics, such as RV2, which could have provided a more comprehensive evaluation of the debiased CKA.

**Questions:**
- Could the authors clarify the discrepancy between the results shown in Figure 1 and the claims made in the paper regarding the sensitivity of biased CKA to the feature-sample ratio?
- How does the choice of kernel affect the results, and could the authors provide more details on this aspect?
- Could the authors elaborate on the potential impact of different preprocessing methods on the results, especially in the context of the THINGS dataset?
- How does the debiased CKA perform compared to other metrics like RV2, and could the authors provide a more detailed comparison between these metrics?
- Could the authors address the potential misleading conclusions due to the small dataset size and the lack of diversity in the dataset?

**Soundness:**
3 good

**Presentation:**
3 good

**Contribution:**
3 good

**Rating:**
6 marginally above the acceptance threshold

**Paper Decision:**
- Decision: Accept
- Reasons: The paper effectively addresses a significant issue with biased CKA and provides a valuable resource in the form of the THINGS dataset. The debiased CKA proposed is a useful tool for the community, and the paper's clarity and presentation are commendable. However, the paper's scope is limited, and the conclusions might be misleading due to the small dataset size. The decision to accept is based on the paper's contribution to the field and its potential impact, but with the recommendation that future work should address these limitations and expand the dataset for more robust conclusions.