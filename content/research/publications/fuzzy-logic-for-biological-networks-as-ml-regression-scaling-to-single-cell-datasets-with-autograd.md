---
title: "Fuzzy Logic for Biological Networks as ML Regression: Scaling to Single-Cell Datasets With Autograd"
authors: "Le Constance, Alice Driessen, Nicolas Deutschmann, Maria Rodriguez Martinez"
link: "https://openreview.net/forum?id=KhdgF56cbY"
date: "2022-01-04"
private: false
---

We present the BioFuzzNet module, a fuzzy logic tool to model signal transduction in biological networks. By equating the optimisation of the fuzzy logic transfer functions to a regression problem, we show that gradient descent is a suitable optimisation method for fuzzy logic modelling. The speed of this approach allows us to scale fuzzy logic modelling to single-cell datasets and leverage available transcriptomics data. Furthermore, the flexibility of gradient descent optimisation allows us to perform arbitrary computations, thereby enabling us to model feedback loops and fit them in simple cases. Promising results also suggest that BioFuzzNet can generate insights in the signalling network topology by identifying logical gates and spurious connections.