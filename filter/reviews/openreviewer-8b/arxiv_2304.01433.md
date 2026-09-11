# Review

## Summary
This paper describes the TPU v4 supercomputer, an industrial product from Google, that has been deployed since 2020. The paper describes three main innovations: (1) the use of optical circuit switches (OCS) to build a 3D torus topology at a larger scale than any prior TPU system, (2) the use of specialized cores (SparseCores) to accelerate embedding operations, and (3) a platform-aware neural architecture search (PA-NAS) system to automatically tailor neural network architectures to the hardware capabilities. The paper describes the design of the system, and presents performance results comparing TPU v4 to prior TPU versions and to other commercial hardware (Nvidia A100 GPUs, Graphcore IPU). The paper also describes the changing nature of ML workloads over time, and how the TPU v4 system has had to adapt to changing workloads.

## Soundness
4

## Presentation
4

## Contribution
3

## Strengths
The paper is well-written and provides a thorough description of the TPU v4 system. It is clear that this is a significant industrial achievement, providing a large, flexible, and reliable supercomputer for training large ML models. The paper does a good job of explaining the design decisions and how they address specific challenges in building a large ML training system. The performance results are also thorough, comparing the new system to prior versions of the same hardware as well as commercial alternatives from other companies. The discussion of the changing nature of ML workloads over time is also interesting and provides useful insights into the challenges of building long-lived hardware systems.

## Weaknesses
The paper is strong overall, but it would be stronger if it provided more detailed comparisons to other commercial systems. For example, the paper compares TPU v4 to TPU v3 and to Nvidia A100s and Graphcore IPUs, but it does not provide a detailed comparison to other commercial systems such as the IBM AC922, Cray EX, or HPE Cray XD. It would also be useful to provide more detailed comparisons to other commercial systems in terms of power consumption and CO2 emissions.

## Questions
1. The paper describes the use of optical circuit switches (OCS) to build a 3D torus topology for the TPU v4 system. How does this compare to other commercial systems, such as the Cray EX, which uses a 3D torus topology with electrical switches?

2. The paper describes the use of SparseCores to accelerate embedding operations. How does this compare to other commercial systems in terms of embedding performance?

3. The paper describes the use of platform-aware neural architecture search (PA-NAS) to tailor neural network architectures to the hardware capabilities. How does this compare to other commercial systems in terms of ease of use and performance?

4. The paper describes the changing nature of ML workloads over time. How does the TPU v4 system handle changes in workloads over time? Are there any challenges in adapting the system to changing workloads?

5. The paper provides some performance results for the TPU v4 system. How does the performance compare to other commercial systems, such as the IBM AC922, Cray EX, or HPE Cray XD?

6. The paper provides some results on power consumption and CO2 emissions for the TPU v4 system. How does this compare to other commercial systems?

## Flag For Ethics Review
No ethics review needed.

## Details Of Ethics Concerns


## Rating
8

## Confidence
4