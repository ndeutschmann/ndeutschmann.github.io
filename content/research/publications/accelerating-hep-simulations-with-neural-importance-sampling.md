---
title: "Accelerating HEP simulations with Neural Importance Sampling"
authors: "Nicolas Deutschmann, Niklas Götz"
link: "https://openreview.net/forum?id=V0LnyelKACB"
date: "2021-01-01"
private: false
---

Virtually all high-energy-physics (HEP) simulations for the LHC rely on Monte Carlo using importance sampling by means of the VEGAS algorithm. However, complex high-precision calculations have become a challenge for the standard toolbox. As a result, there has been keen interest in HEP for modern machine learning to power adaptive sampling. Despite previous work proving that normalizing-flow-powered neural importance sampling (NIS) sometimes outperforms VEGAS, existing research has still left major questions open, which we intend to solve by introducing ZüNIS, a fully automated NIS library. We first show how to extend the original formulation of NIS to reuse samples over multiple gradient steps, yielding a significant improvement for slow functions. We then benchmark ZüNIS over a range of problems and show high performance with limited fine-tuning. This is crucial for ZüNIS to be a mature tool for the wider HEP public. We outline how the the library allows for non-experts to employ it with minimal effort, an essential condition to widely assess the value of NIS for LHC simulations.