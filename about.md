---
layout: page
title: Research
permalink: /research/
---

![Crystal data extraction schematic from raw CIF files and crystal databases by Dr. Anton Oliynyk](files/research/oliynyk-cif-structure-featurizer/1.png)
### High-throughput Crystal Structure Featurizer for Binary and Ternary Compounds
[GitHub](https://github.com/bobleesj/cif-cn-featurizer) | [Journal of Alloys and Compounds](https://doi.org/10.1016/j.jallcom.2023.173241)

**Challenge:** Traditional machine learning models in solid-state materials have predominantly relied on composition data to predict properties. The lack of structural information often leads to incomplete property mapping and predictive noise.

**What we did:**  Dr. Anton Oliynyk and I launched a summer project to create an open-source Python tool crafted for the high-throughput extraction of crystal structure features. This geometric featurizer  processes raw Crystallographic Information Files (CIF) to construct supercells and meticulously extracts a comprehensive suite of descriptors, such as coordination numbers, interatomic distances, and atomic environments. These descriptors are not mere extrapolations from generic values but are tailored to the material's specific structure, reducing noise and enhancing the relevance of ML applications for binary and ternary compounds. The package has demonstrated its robustness, having processed more than 10,000 binary and ternary CIF files. I designed and built the Python package and now maintain the repository.

**Implications:** Leveraging structure-property correlations, we believe this crystal structure featurizer can be a promising tool for increasing predictive capabilities for material property optimization in machine learning application.
