---
title: Learning distribution-free anchored linear structural equation models in the presence of measurement error
tags:
    - Research summary
---

This post is the summary of <a href="https://link.springer.com/article/10.1007/s42952-024-00298-9">Chung, J., Ahn, Y., Shin, D., & Park, G. (2024). Learning distribution-free anchored linear structural equation models in the presence of measurement error. Journal of the Korean Statistical Society, 1-25.</a>

<!--more-->

---

# Objective

This study aims to establish identifiability in distribution-free anchored linear structural equation models(SEMs), where the observed variables are imperfect measures for the target variables. Based on the identifiability condition, a consistent learning algorithm of the complete partial directed acyclic graph(CPDAG) is developed.

# Contributions

* Establishes an identifiability condition of distribution-free anchored linear SEMs based on the **geometry-faithfulness** assumption.
* Proposes a consistent learning algorithm to discover a latent structure in the presence of measurement error.
* Provides various numerical experiments and analysis of real galaxy data.

# Introduction

* Identifiability of directed acyclic graphical models (DAG) is usually achieved by posing additional assumptions. For example,
  * **Causal minimality**: True graph is a minimal structure that is Markov to its distribution.
  * **Faithfulness**: Conditional independence implies d-separation.
	* **Distributional constraints**: Gaussian errors with equal variance (Peters and Bühlmann, 2014), non-Gaussian errors (Shimizu et al., 2006), etc.
* The aforementioned identifiability results work under **causal sufficiency** regime, excluding the presence of latent variables.
* However, in many real-world setting, observed variables are **imperfect measures** of corresponding true variables.