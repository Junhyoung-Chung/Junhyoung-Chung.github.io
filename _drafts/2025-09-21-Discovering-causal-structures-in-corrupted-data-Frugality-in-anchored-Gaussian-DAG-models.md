---
title: 'Discovering causal structures in corrupted data: Frugality in anchored Gaussian DAG models'
tags:
    - Research summary
---

This post is the summary of <a href="https://www.sciencedirect.com/science/article/pii/S0167947325001434?casa_token=gfxiDXQAEdwAAAAA:FoZ1rE7hHtZv1HnDuaIYoweB5e_ib-cO4uDyp81cF88O4aBayFCvSU9xY1hGEHe3gXuUMX0g7w">Shin, J., Chung, J., Hwang, S., & Park, G. (2025). Discovering Causal Structures in Corrupted Data: Frugality in Anchored Gaussian DAG Models. Computational Statistics & Data Analysis, 108267.</a>

<!--more-->

---

# Objective

This study focuses on establishing a weaker form of identifiability for anchored Gaussian DAG models, **where knowledge of the measurement error variance is unavailable**. Based on the condition, **sound learning algorithms** of the complete partial directed acyclic graph(CPDAG) are devised.

# Contributions

* Introduces the **anchored-frugality** assumption, leveraging the fact that contaminated data tend to produce a denser graph than the true graph.
* Provides **theoretical justifications** for the anchored-frugality assumption from both graph-theoretical and probabilistic perspectives.
* Develops **two theoretically sound algorithms** for anchored Gaussian DAG models, building upon and extending the sparsest permutation(SP) algorithm (Raskutti and Uhler (2018)) and the PC algorithm.
* Conducts **comprehensive numerical experiments and application to breast cancer data and protein signaling data**, supporting the main theoretical findings of the study.

# Introduction

* Identifiability of directed acyclic graphical models is usually achieved by posing additional assumptions, most of which require variables to be directly observed.
* However, in many real-world settings, observed variables are **imperfect measures** of corresponding true variables.
* A number of studies have tackled this issue under anchored DAG models. For example,
  * Zhang et al. (2017) propose a consistent algorithm when **the number of leaf nodes is sufficiently small and the non-deterministic faithfulness holds**, which is stronger than the standard faithfulness.
  * Saeed et al. (2020) establish a PC-based algorithm that achieves consistency when **the latent variables are Gaussian and the contamination process is known**.
  * Chung et al. (2024) develop a consistent distribution-free algorithm when **the contamination process is given**.
* This highlights the need for an algorithm that **(i) works under more relaxed conditions** and **(ii) does not require the contamination process to be known**.

<!-- ## Motivating example

![figure 1](/assets/images/anchored-causal-model.png)

* The above figure visualizes the relationship between the latent variables $X$ and the observed variables $Z$.
* One can observe that $X_1$ and $X_3$ are d-separated(blocked) by $X_2$, while the statement becomes false if we replace $X$ to $Z$. -->

## Preliminaries

### Directed acyclic graph

* A DAG $G = (V,E)$ consists of a set of nodes $V = \\{1,...,p\\}$ and a set of directed edges $E \subset V \times V$ with no directed cycles.
* A **skeleton** of a DAG $G$ is attained by replacing all directed edges to undirected edges, and we denote $\vert G \vert$ for the number of edges in its skeleton.
* A set of **parents** of node $k$, denoted by $\text{Pa}(k)$, consists of all nodes $j$ such that $(j,k) \in E$.
* If there is a directed path $j \rightarrow \cdots \rightarrow k$, then $k$ is a **descendant** of $j$, and $j$ is called an **ancestor** of $k$.
* A node $k$ is a **collider** if there exists a triple $(j,k,\ell)$ such that $j \rightarrow k \leftarrow \ell$, and we say such triple generates a **v-structure**.

### D-separation and d-connection

* Two nodes $j$ and $k$ in DAG $G$ are **d-connected by a node set** $S \subset V$ if there exists a path $\mathcal{P}$ between $j$ and $k$ such that for every node $\ell$ on the path $\mathcal{P}$
  * if $\ell$ is a collider, either $\ell$ or its descendant is in $S$,
  * otherwise $\ell$ is not in $S$.
* If $j$ and $k$ are not d-connected by $S$, we say $j$ and $k$ are **d-separated by** $S$.

### Anchored DAG

<div style="display: flex; justify-content: center; gap: 20px; align-items: flex-start;">

  <figure style="text-align: center; display: flex; flex-direction: column; justify-content: space-between; height: 180px; margin: 0;">
    <img src="/assets/images/anchored-DAG.png" alt="Anchored DAG" style="width: 220px; height: auto;"/>
    <figcaption style="margin-top: 8px;"><strong>(a)</strong> Anchored DAG</figcaption>
  </figure>

  <figure style="text-align: center; display: flex; flex-direction: column; justify-content: space-between; height: 180px; margin: 0;">
    <img src="/assets/images/latent-DAG.png" alt="True Latent DAG" style="width: 220px; height: auto;"/>
    <figcaption style="margin-top: 8px;"><strong>(b)</strong> True latent DAG</figcaption>
  </figure>

  <figure style="text-align: center; display: flex; flex-direction: column; justify-content: space-between; height: 180px; margin: 0;">
    <img src="/assets/images/anchored-moral-graph.png" alt="Anchored Moral Graph" style="width: 220px; height: auto;"/>
    <figcaption style="margin-top: 8px;"><strong>(c)</strong> Anchored moral graph</figcaption>
  </figure>

</div>

* An **anchored DAG** for $G = (V,E)$ is denoted as $G_{an} = (V_{an},E_{an})$.
  * $V_{an} = V \cup V^\prime$, where $V^\prime = \\{1^\prime,...,p^\prime\\}$ represents the vertex set of anchored nodes. Here, $j^\prime$ is the anchored node corresponding to $j$, i.e., $\text{Pa}(j^\prime) = \\{j\\}$ for each $j \in V$.
  * $E_{an} = E \cup \\{(j,j^\prime): j \in V\\}$.
* An **anchored moral graph** of $G$ is an undirected graph defined by the vertex set $V^\prime$ and $E^\prime$, where
  *  $E^\prime = \\{(j^\prime,k^\prime): \text{$j^\prime$ and $k^\prime$ cannot be d-separated by any subset $S^\prime \subset V^\prime \setminus \\{j^\prime,k^\prime\\}$}\\}$.
  *  Intuitively, the anchored moral graph serves as a **corrupted representation** for $G$, obtained with obfuscated data.

## Anchored Gaussian linear structural equation model

* A **Gaussian linear structural equation model(SEM)** is a Gaussian DAG model where the joint distribution is defined by the following linear equations: For all $j \in V$,

  $$
  X_j = \sum_{k \in \text{Pa}(j)} \beta_{kj}X_k + \epsilon_j ,
  $$

  where $\epsilon_j \overset{\text{indep.}}{\sim} N(0,\sigma_j^2)$.

* The above linear SEM can be restated as a matrix form:

  $$
  X = BX + \epsilon .
  $$

* In our framework, we consider an **anchored Gaussian linear SEM**, special case of an anchored DAG model, as follows: For all $j \in V$,
  
  $$
  Z = X + E ,
  $$

  where $E \sim N(0,\text{diag}(\eta_1^2,...,\eta_p^2))$. Then, $\Sigma_Z = \Sigma_X + \text{diag}(\eta_1^2,...,\eta_p^2)$.

# Identifiability

## Anchored-frugality

**Assumption 1(Anchored-frugality).**
> Consider an anchored Gaussian linear SEM, in which the true distribution of the latent variable $X$ is equal to $P_\eta \sim N(0, \Sigma_Z - \text{diag}(\eta_1^2,...,\eta_p^2))$. A pair $(G,P(X)) = (G,P_\eta)$ is said to satisfy the anchored-frugality assumption if for each valid $\lambda$ and $G_\lambda \in G_{fr}(P_\lambda)$, it holds either $\vert G_\lambda \vert > \vert G \vert$ or $M(G_\lambda) = M(G)$.

# References

* Chung, J., Ahn, Y., Shin, D., & Park, G. (2024). Learning distribution-free anchored linear structural equation models in the presence of measurement error. Journal of the Korean Statistical Society, 1-25.
* Raskutti, G., & Uhler, C. (2018). Learning directed acyclic graph models based on sparsest permutations. Stat, 7(1), e183.
* Saeed, B., Belyaeva, A., Wang, Y., & Uhler, C. (2020). Anchored causal inference in the presence of measurement error. In Conference on uncertainty in artificial intelligence (pp. 619-628). PMLR.
* Shin, J., Chung, J., Hwang, S., & Park, G. (2025). Discovering Causal Structures in Corrupted Data: Frugality in Anchored Gaussian DAG Models. Computational Statistics & Data Analysis, 108267.
* Zhang, K., Gong, M., Ramsey, J., Batmanghelich, K., Spirtes, P., & Glymour, C. (2017). Causal discovery in the presence of measurement error: Identifiability conditions. arXiv preprint arXiv:1706.03768.