## Summary

This paper describes the TPU v4, the fifth Google domain-specific architecture (DSA) and its third supercomputer for ML models. The main contributions are: 1) the first production deployment of OCSes in a supercomputer and the first to allow topology reconfiguration to improve performance; 2) the first accelerator support for embeddings in a commercial ML system; 3) the first to describe the rapid change in production model types since 2016 for the fast changing ML field; 4) the first to show how Google uses ML to co-optimize DNN models, OCS topology, and the SparseCore. The paper describes the TPU v4 supercomputer, which is 4x larger than TPU v3, and the first to use optical circuit switches (OCSes) to improve scale, availability, utilization, modularity, deployment, security, power, and performance. The OCSes enable flexible topology configuration, including twisted torus, which has better bisection properties. The paper also describes the SparseCore (SC), which is a domain-specific architecture for embedding training starting with TPU v2, with later improvements in TPU v3 and TPU v4. The SC is a relatively inexpensive component, at a total of only ~5% of the die area and ~5% of the power. The paper also describes how Google uses ML to co-optimize DNN models, OCS topology, and the SparseCore. The paper evaluates the TPU v4 supercomputer on production workloads versus TPU v3 and versus the Nvidia A100 and the Graphcore MK2 IPU using MLPerf. The paper also shows how Google uses ML to co-optimize DNN models, OCS topology, and the SparseCore.

## Soundness

3 good

## Presentation

3 good

## Contribution

2 fair

## Strengths

This paper describes the TPU v4, the fifth Google domain-specific architecture (DSA) and its third supercomputer for ML models. The main contributions are: 1) the first production deployment of OCSes in a supercomputer and the first to allow topology reconfiguration to improve performance; 2) the first accelerator support for embeddings in a commercial ML system; 3) the first to describe the rapid change in production model types since 2016 for the fast changing ML field; 4) the first to show how Google uses ML to co-optimize DNN models, OCS topology, and the SparseCore. The paper describes the TPU v4 supercomputer, which is 4x larger than TPU v3, and the first to use optical circuit switches (OCSes) to improve scale, availability, utilization, modularity, deployment, security, power, and performance. The OCSes enable flexible topology configuration, including twisted torus, which has better bisection properties. The paper also describes the SparseCore (SC), which is a domain-specific architecture for embedding training starting with TPU v2, with later improvements in TPU v3 and TPU v4. The SC is a relatively inexpensive component, at a total of only ~5% of the die area and ~5% of the power. The paper also describes how Google uses ML to co-optimize DNN models, OCS topology, and the SparseCore. The paper evaluates the TPU v4 supercomputer on production workloads versus TPU v3 and versus the Nvidia A100 and the Graphcore MK2 IPU using MLPerf. The paper also shows how Google uses ML to co-optimize DNN models, OCS topology, and the SparseCore.

## Weaknesses

1. The paper is not well-organized. The authors should focus on the main contributions and highlight the main contributions in the introduction.
2. The paper does not provide enough details about the TPU v4 architecture. The authors should provide more details about the TPU v4 architecture, including the number of cores, the clock speed, the memory bandwidth, and the power consumption.
3. The paper does not provide enough details about the SparseCore (SC) architecture. The authors should provide more details about the SC architecture, including the number of cores, the clock speed, the memory bandwidth, and the power consumption.
4. The paper does not provide enough details about the OCSes. The authors should provide more details about the OCSes, including the number of ports, the bandwidth, and the power consumption.
5. The paper does not provide enough details about the evaluation methodology. The authors should provide more details about the evaluation methodology, including the benchmarks used, the input data, and the evaluation metrics.
6. The paper does not provide enough details about the results. The authors should provide more details about the results, including the performance, the power consumption, and the scalability.
7. The paper does not provide enough details about the comparison with other DSA chips. The authors should provide more details about the comparison with other DSA chips, including the Nvidia A100 and the Graphcore MK2 IPU.

## Questions

1. What are the main contributions of the paper?
2. What are the key features of the TPU v4 supercomputer?
3. What are the benefits of using OCSes in the TPU v4 supercomputer?
4. What are the benefits of using the SparseCore (SC) in the TPU v4 supercomputer?
5. How does the TPU v4 supercomputer compare to other DSA chips in terms of performance and power consumption?
6. How does the TPU v4 supercomputer scale with the number of chips?
7. What are the limitations of the TPU v4 supercomputer?

## Flag For Ethics Review

No ethics review needed.

## Rating

6: marginally above the acceptance threshold

## Confidence

4: You are confident in your assessment, but not absolutely certain. It is unlikely, but not impossible, that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work.

**********

## Reviewer

## Summary

The paper describes the TPU v4, the fifth Google domain-specific architecture (DSA) and its third supercomputer for ML models. The main contributions are: 1) the first production deployment of OCSes in a supercomputer and the first to allow topology reconfiguration to improve performance; 2) the first accelerator support for embeddings in a commercial ML system; 3) the first to describe the rapid change in production model types since 2016 for the fast changing ML field; 4) the first to show how Google uses ML to co-optimize DNN models, OCS topology, and the SparseCore. The paper describes the TPU v4 supercomputer, which is 4x larger than TPU v3, and the first to use optical circuit switches (OCSes) to improve scale, availability, utilization, modularity, deployment, security, power, and performance. The OCSes enable flexible topology configuration, including twisted torus, which has better bisection properties. The paper also describes the SparseCore (SC), which is a domain-specific architecture for embedding training starting with TPU v2, with later improvements in TPU v3 and TPU v4. The SC is a relatively inexpensive component, at a total of only ~5% of the die area and ~5% of the power. The paper also describes how Google uses ML to co-optimize DNN models, OCS topology, and the SparseCore. The paper evaluates the TPU v4 supercomputer on production workloads versus TPU v3 and versus the Nvidia A100 and the Graphcore MK2 IPU using MLPerf. The paper also shows how Google uses ML to co-optimize DNN models, OCS topology, and the SparseCore.

## Soundness

3 good

## Presentation

3 good

## Contribution

3 good

## Strengths

This paper describes the TPU v4, the fifth Google domain-specific architecture (DSA) and its third supercomputer for ML models. The main contributions are: 1) the first production deployment of OCSes in a supercomputer and the first to allow topology reconfiguration to improve performance; 2) the first accelerator support for embeddings in a commercial ML system; 3) the first to describe the rapid change in production model types since 2016 for the fast changing ML field; 4) the first to show how Google uses ML to co-optimize DNN models, OCS topology, and the SparseCore. The paper describes the TPU v4 supercomputer, which is 4x larger than TPU v3, and the first to use optical circuit switches (OCSes) to improve scale, availability, utilization, modularity, deployment, security, power, and performance. The OCSes enable flexible topology configuration, including twisted torus, which has better bisection properties. The paper also describes the SparseCore (SC), which is a domain-specific architecture for embedding training starting with TPU v2, with later improvements in TPU v3 and TPU v4. The SC is a relatively inexpensive component, at a total of only ~5% of the die area and ~5% of the power. The paper also describes how Google uses ML to co-optimize DNN models, OCS topology, and the SparseCore. The paper evaluates the TPU v4 supercomputer on production workloads versus TPU v3 and versus the Nvidia A100 and the Graphcore MK2 IPU using MLPerf. The paper also shows how Google uses ML to co-optimize DNN models, OCS topology, and the SparseCore.

## Weaknesses

The paper is not well-organized. The authors should focus on the main contributions and highlight the main contributions in the introduction.

## Questions

The paper is not well-organized. The authors should focus on the main contributions and highlight the main contributions in the introduction.

## Flag For Ethics Review

No ethics review needed.

## Rating

6: marginally above the acceptance threshold

## Confidence

3: You are fairly confident in your assessment. It is possible that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work. Math/other details were not carefully checked.

**********

## Reviewer

## Summary

This paper describes the TPU v4, the fifth Google domain-specific architecture (DSA) and its third supercomputer for ML models. The main contributions are: 1) the first production deployment of OCSes in a supercomputer and the first to allow topology reconfiguration to improve performance; 2) the first accelerator support for embeddings in a commercial ML system; 3) the first to describe the rapid change in production model types since 2016 for the fast changing ML field; 4) the first to show how Google uses ML to co-optimize DNN models, OCS topology, and the SparseCore. The paper describes the TPU v4 supercomputer, which is 4x larger than TPU v3, and the first to use optical circuit switches (OCSes) to improve scale, availability, utilization, modularity, deployment, security, power, and performance. The OCSes enable flexible topology configuration, including twisted torus, which has better bisection properties. The paper also describes the SparseCore (SC), which is a domain-specific architecture for embedding training starting with TPU v2, with later improvements in TPU v3 and TPU v4. The SC is a relatively inexpensive component, at a total of only ~5% of the die area and ~5% of the power. The paper also describes how Google uses ML to co-optimize DNN models, OCS topology, and the SparseCore. The paper evaluates the TPU v4 supercomputer on production workloads versus TPU v3 and versus the Nvidia A100 and the Graphcore MK2 IPU using MLPerf. The paper also shows how Google uses ML to co-optimize DNN models, OCS topology, and the SparseCore.

## Soundness

3 good

## Presentation

3 good

## Contribution

3 good

## Strengths

This paper describes the TPU v4, the fifth Google domain-specific architecture (DSA) and its third supercomputer for ML models. The main contributions are: 1) the first production deployment of OCSes in a supercomputer and the first to allow topology reconfiguration to improve performance; 2) the first accelerator support for embeddings in a commercial ML system; 3) the first to describe the rapid change in production model types since 2016 for the fast changing ML field; 4) the first to show how Google uses ML to co-optimize DNN models, OCS topology, and the SparseCore. The paper describes the TPU v4 supercomputer, which is 4x larger than TPU v3, and the first to use optical circuit switches (OCSes) to improve scale, availability, utilization, modularity, deployment, security, power, and performance. The OCSes enable flexible topology configuration, including twisted torus, which has better bisection properties. The paper also describes the SparseCore (SC), which is a domain-specific architecture for embedding training starting with TPU v2, with later improvements in TPU v3 and TPU v4. The SC is a relatively inexpensive component, at a total of only ~5% of the die area and ~5% of the power. The paper also describes how Google uses ML to co-optimize DNN models, OCS topology, and the SparseCore. The paper evaluates the TPU v4 supercomputer on production workloads versus TPU v3 and versus the Nvidia A100 and the Graphcore MK2 IPU using MLPerf. The paper also shows how Google uses ML to co-optimize DNN models, OCS topology, and the SparseCore.

## Weaknesses

The paper is not well-organized. The authors should focus on the main contributions and highlight the main contributions in the introduction.

## Questions

The paper is not well-organized. The authors should focus on the main contributions and highlight the main contributions in the introduction.

## Flag For Ethics Review

No ethics review needed.

## Rating

6: marginally above the acceptance threshold

## Confidence

3: You are fairly confident in your assessment. It is possible that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work. Math/other details were not carefully checked.

**********

## Reviewer

## Summary

The paper describes the TPU v4, the fifth Google domain-specific architecture (DSA) and its third supercomputer for ML models. The main contributions are: 1) the first production deployment of OCSes in a supercomputer and the first to allow topology reconfiguration to improve performance; 2) the first accelerator support for embeddings in a commercial ML system; 3) the first to describe the rapid change in production model types since 2016 for the fast changing ML field; 4) the first to show how Google uses ML to co-optimize DNN models, OCS topology, and the SparseCore. The paper describes the TPU v4 supercomputer, which is 4x larger than TPU v3, and the first to use optical circuit switches (OCSes) to improve scale, availability, utilization, modularity, deployment, security, power, and performance. The OCSes enable flexible topology configuration, including twisted torus, which has better bisection properties. The paper also describes the SparseCore (SC), which is a domain-specific architecture for embedding training starting with TPU v2, with later improvements in TPU v3 and TPU v4. The SC is a relatively inexpensive component, at a total of only ~5% of the die area and ~5% of the power. The paper also describes how Google uses ML to co-optimize DNN models, OCS topology, and the SparseCore. The paper evaluates the TPU v4 supercomputer on production workloads versus TPU v3 and versus the Nvidia A100 and the Graphcore MK2 IPU using MLPerf. The paper also shows how Google uses ML to co-optimize DNN models, OCS topology, and the SparseCore.

## Soundness

3 good

## Presentation

3 good

## Contribution

3 good

## Strengths

The paper describes the TPU v4, the fifth Google domain-specific architecture (DSA) and its third supercomputer for ML models. The main contributions are: 1) the first production deployment of OCSes in a supercomputer and the first to allow topology reconfiguration to improve performance; 2) the first accelerator support for embeddings in a commercial ML system; 3) the first to describe the rapid change in production model types since 2016 for the fast changing ML field; 4) the first to show how Google uses ML to co-optimize DNN models, OCS topology, and the SparseCore. The paper describes the TPU v4 supercomputer, which is 4x larger than TPU v3, and the first to use optical circuit switches (OCSes) to improve scale, availability, utilization, modularity, deployment, security, power, and performance. The OCSes enable flexible topology configuration, including twisted torus, which has better bisection properties. The paper also describes the SparseCore (SC), which is a domain-specific architecture for embedding training starting with TPU v2, with later improvements in TPU v3 and TPU v4. The SC is a relatively inexpensive component, at a total of only ~5% of the die area and ~5% of the power. The paper also describes how Google uses ML to co-optimize DNN models, OCS topology, and the SparseCore. The paper evaluates the TPU v4 supercomputer on production workloads versus TPU v3 and versus the Nvidia A100 and the Graphcore MK2 IPU using MLPerf. The paper also shows how Google uses ML to co-optimize DNN models, OCS topology, and the SparseCore.

## Weaknesses

The paper is not well-organized. The authors should focus on the main contributions and highlight the main contributions in the introduction.

## Questions

The paper is not well-organized. The authors should focus on the main contributions and highlight the main contributions in the introduction.

## Flag For Ethics Review

No ethics review needed.

## Rating

6: marginally above the acceptance threshold

## Confidence

3: You are fairly confident in your assessment. It is possible that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work. Math/other details were not carefully checked.

**********

## Meta Review

This paper describes the TPU v4, the fifth Google domain-specific architecture (DSA) and its third supercomputer for ML models. The main contributions are: 1) the first production deployment of OCSes in a supercomputer and the first to allow topology reconfiguration to improve performance; 2) the first accelerator support for embeddings in a commercial ML system; 3) the first to describe the rapid change in production model types since 2016 for the fast changing ML field; 4) the first to show how Google uses ML to co-optimize DNN models, OCS topology, and the SparseCore. The paper describes the TPU v4 supercomputer, which is 4x larger than TPU v3, and the first to use optical circuit switches (OCSes) to improve scale, availability, utilization, modularity, deployment, security, power, and performance. The OCSes enable flexible topology configuration, including twisted torus, which has better bisection properties. The paper also describes the SparseCore (SC), which is a domain-specific architecture for embedding training starting with TPU v2, with later improvements in TPU v3 and TPU v4. The SC is a relatively inexpensive component, at a total of only ~5% of the die area and ~5% of the power. The paper also describes how Google uses ML to co-optimize DNN models, OCS topology, and the SparseCore. The paper evaluates the TPU v4 supercomputer on production workloads versus TPU v3 and versus the Nvidia A100 and the Graphcore MK2 IPU using MLPerf. The paper also shows how Google uses ML to co-optimize DNN models, OCS topology, and the SparseCore.

## justification_for_why_not_higher_score

The paper is not well-organized. The authors should focus on the main contributions and highlight the main contributions in the introduction.

## justification_for_why_not_lower_score

N/A

**********

## Paper Decision

Accept (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (