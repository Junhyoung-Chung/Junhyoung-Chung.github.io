---
title: 'Operator fused optimal transport: A convex and geometry-preserving formulation'
tags:
    - Research summary
---

This post summarizes my ongoing work: **"Operator fused optimal transport: A convex and geometry-preserving formulation"**. For those interested in this work, please feel free to reach out for a discussion.

<!--more-->

---

# Objective

This study aims to design a fused optimal transport framework that is simultaneously (i) **convex** and computationally tractable, (ii) sensitive to **feature information**, and (iii) capable of preserving the intrinsic **geometric structure** of domains.

# Contributions

To the best of our knowledge, this is the first **convex formulation** for geometry-preserving optimal transport that guarantees statistical consistency. The main contributions can be summarized as follows.

* **Convex objective**: Motivated from convex relaxation techniques used in **graph matching** problems, we design a new loss function that parallels the geometric philosophy of Gromov-Wasserstein discrepancy and prove convexity of the overall fused objective (Theorem 1).
* **Isometry consistency**: We establish that the proposed structural penalty vanishes on isometries under specific conditions (Proposition 1).
* **Scalable solver with guarantees**: We give a simple Frank-Wolfe algorithm for the empirical convex quadratic program, with an optional Hungarian algorithm for hard matchings, and derive an optimization-statistical error bound (Theorem 2).

# Introduction

* Optimal transport (OT) provides a fundamental framework for comparing probability measures by quantifying the minmal cost required to move mass across spaces.
* A central appeal of OT lies in its ability to uncover meaningful correspondences between probability measures.
* However, the classical OT is agnostic to situations where geometric alignment between the source space $\mathcal{X}$ and the target space $\mathcal{Y}$ is important.
* A popular way to incorporate geometry is the Gromov-Wasserstein (GW) framework (Mémoli, 2011), which finds a coupling that minimizes the following:

  $$
  \inf_{\pi \in \Pi(\mathbb{P}_X,\mathbb{P}_Y)} \mathbb{E}_{\pi \otimes \pi} \Big[\big|d_{\mathcal{X}}(X,X^\prime)-d_{\mathcal{Y}}(Y,Y^\prime)\big|^2\Big] .
  $$

* However, the GW term is **non-convex** in the coupling, leading to non-unique minimizers and algorithmic sensitivity to initialization.
* On the other hand, since GW focuses on structure, they overlook the rich **feature information** often attached to data (e.g., descriptors) (Vayer et al., 2020).
* We introduce **Operator Fused Optimal Transport (OFOT)**, a novel convex framework that preserves both domain geometry and feature alignment:

  $$
  \inf_{\pi\in\Pi(\mathbb{P}_X,\mathbb{P}_Y)} (1-\alpha)\mathbb{E}_{\pi}\big[\|f_{\mathcal{X}}(X)-f_{\mathcal{Y}}(Y)\|_2^2\big] + \frac{\alpha}{2} \| D_{\mathbb{P}_X}^{\kappa}T_\pi - T_\pi D_{\mathbb{P}_Y}^{\kappa} \|_{\mathrm{HS}}^2 .
  $$

## Preliminaries

* Let $(\mathcal{X},d_{\mathcal{X}},\mathbb{P}\_X)$ and $(\mathcal{Y},d_{\mathcal{Y}},\mathbb{P}_Y)$ be connected and compact metric measure spaces with fully supported probability measures.
* We further introduce a compact feature space $M \subset \mathbb{R}^k$ and define continuous mappings $f_{\mathcal{X}}: \mathcal{X} \to M$ and $f_{\mathcal{Y}}: \mathcal{Y} \to M$, referred to as feature functions.
* For probability measures $\mu$ and $\nu$, denote by
  
  $$
  \Pi(\mu,\nu) = \{ \pi : \text{the marginals of $\pi$ are $\mu$ and $\nu$}\}
  $$

  the set of all couplings among them.

* Given an arbitrary coupling $\pi \in \Pi(\mathbb{P}\_X,\mathbb{P}\_Y)$, the conditional expectation operator $T_{\pi} : L^2(\mathcal{Y},\mathbb{P}\_Y) \to L^2(\mathcal{X},\mathbb{P}\_X)$ is defined as $(T_{\pi}g)(x) = \mathbb{E}_{\pi}[g(Y) \mid X = x]$ for any $g \in L^2(\mathcal{Y},\mathbb{P}\_Y)$.

# Proposed method

## Distance potential operator

**Definition 1 (Distance kernel).**
>A function $K_{\mathcal{X}}: \mathcal{X} \times \mathcal{X} \to \mathbb{R}\_+$ is said to be a *distance kernel* if there exists a bounded continuous function $\kappa : [0,1] \to \mathbb{R}\_+$ such that
>
>$$
>K_{\mathcal{X}}(x,x^\prime) = \kappa\left(d_{\mathcal{X}}(x,x')\right) .
>$$
>
>We also define $K_{\mathcal{Y}}(y,y')$ analogously.

* While there are many possible choices for $\kappa$, it suffices to use the identity function, i.e., $K_{\mathcal{X}}(x,x^\prime) = d_{\mathcal{X}}(x,x')$ in practice.

**Definition 2 (Distance potential operator).**
>Let $(\mathcal{X},d\_{\mathcal{X}},\mathbb{P}\_X)$ be a compact metric-measure space. The *distance potential operator* $D\_{\mathbb{P}\_X}^{\kappa} : L^2(\mathcal{X},\mathbb{P}\_X) \to L^2(\mathcal{X},\mathbb{P}\_X)$ is an integral operator defined by
>
>$$
>(D_{\mathbb{P}_X}^{\kappa}f)(x) = \mathbb{E}_{\mathbb{P}_X}\left[K_{\mathcal{X}}(x,X)f(X)\right] = \int_{\mathcal{X}} K_{\mathcal{X}}(x,x')\, f(x')\, \mathbb{P}_X(dx') , \; \forall f \in L^2(\mathcal{X},\mathbb{P}_X), \, \forall x \in \mathcal{X} .
>$$

* $$(D_{\mathbb{P}_X}^{\kappa} f)(x)$$ computes a distance-weighted average of the function $f$ with respect to the point $x$.
* If one thinks of $f$ as a signal on the space $\mathcal{X}$, $$D_{\mathbb{P}_X}^{\kappa} f$$ is a smoothed version of that signal, where the smoothing at point $x$ is determined by the distances from $x$ to all other points (as encoded by $$K_{\mathcal{X}}$$).
* More intuitively, if $$f$$ shows a extremely strong signal, i.e., $$f = I_{B(x',\varepsilon)}$$ where $$B(x',\varepsilon)$$ is a ball centered at $$x'$$ with a small radius $$\varepsilon > 0$$, then $$(D_{\mathbb{P}_X}^{\kappa}f)(x)$$ would be nearly proportional to $$K_{\mathcal{X}}(x,x')$$.

## Convex structural penalty 

**Lemma 1 (Structural penalty).**
>For any $\pi \in \Pi(\mathbb{P}_X,\mathbb{P}_Y)$,
>
>$$
>\| D_{\mathbb{P}_X}^{\kappa}T_{\pi} - T_{\pi}D_{\mathbb{P}_Y}^{\kappa} \|_{\mathrm{HS}}^2 = \int_{\mathcal{Y}}\int_{\mathcal{X}} \Gamma_\pi(x,y)^2\mathbb{P}_X(dx)\mathbb{P}_Y(dy) ,
>$$
>
>where $$\Gamma_\pi^1(x,y) = \mathbb{E}_\pi[K_{\mathcal{X}}(x,X) \mid Y = y]$$, $$\Gamma_\pi^2(x,y) = \mathbb{E}_\pi[K_{\mathcal{Y}}(y,Y) \mid X = x]$$, and $$\Gamma_\pi(x,y) = \Gamma_\pi^1(x,y) - \Gamma_\pi^2(x,y)$$. Here $$\|\cdot\|_{\mathrm{HS}}^2$$ is a Hilbert-Schmidt norm.

* Lemma 1 shows the explicit form of our new sturctural penalty.
* According to the above lemma, the regularization term can thus be interpreted as a metric that quantifies the total geometric distortion, or the failure of symmetric alignment of these cross-spatial kernel-weighted expectations induced by the coupling $\pi$.
* In fact, the above penalty vanishes if and only if $$D_{\mathbb{P}_X}^{\kappa}T_{\pi} = T_{\pi}D_{\mathbb{P}_Y}^{\kappa}$$.
* This implies the spectral consistency between the two distance potential operators.
* If $\varphi$ is an eigenfunction of $D_{\mathbb{P}_Y}^{\kappa}$ with eigenvalue $\lambda$, then
  
  $$
  D_{\mathbb{P}_X}^{\kappa}(T_{\pi}\varphi) = T_{\pi}(D_{\mathbb{P}_Y}^{\kappa} \varphi) = \lambda T_{\pi} \varphi .
  $$

* In addition, if $T_{\pi}$ is invertible,

  $$
  D_{\mathbb{P}_X}^{\kappa} = T_{\pi}D_{\mathbb{P}_Y}^{\kappa}T_{\pi}^{-1} ,
  $$

  which is an operator-theoretic analogue of **graph isomorphism**, implying the operators share the same spectrum.

**Proposition 1 (Isometry consistency).**
>Let $$T: \mathcal{X} \to \mathcal{Y}$$ be an bijective measurable map, and consider $$\pi = (\mathrm{Id},T)_{\#}\mathbb{P}_X$$. Then,
>
>$$
>\|D_{\mathbb{P}_X}^{\kappa}T_{\pi} - T_{\pi}D_{\mathbb{P}_Y}^{\kappa}\|_{\mathrm{HS}}^2 = 0 \;\iff\; \kappa(d_{\mathcal{Y}}(T(x),T(x'))) = \kappa(d_{\mathcal{X}}(x,x^\prime)) \; \text{for $\mathbb{P}_X \otimes \mathbb{P}_X$-a.e. $(x,x^\prime)$} .
>$$
>
>If $\kappa$ is further assumed to be strictly monotone, then the right-hand side is equivalent to $$d_{\mathcal{Y}}(T(x),T(x'))=d_{\mathcal{X}}(x,x')$$.

* It shows that the regularization term vanishes if and only if the coupling $\pi$ is induced by an isometry $T$ except for a null set when $\kappa$ is strictly monotone.
* Although formulated fundamentally differently, our penalty shares the same core objective by ensuring that an ideal, structure-preserving map corresponds precisely to the zero-penalty solution.

## Convexity of the proposed objective

**Theorem 1 (Opeator fused optimal transport).**
>For $0 \leq \alpha \leq 1$ and feature functions $$f_{\mathcal{X}},f_{\mathcal{Y}}$$, consider the optimization problem 
>
>$$
>\label{eq:proposed-method}
>\inf_{\pi\in\Pi(\mathbb{P}_X,\mathbb{P}_Y)} \underbrace{(1-\alpha)\mathbb{E}_{\pi}\big[\|f_{\mathcal{X}}(X)-f_{\mathcal{Y}}(Y)\|_2^2\big] + \frac{\alpha}{2} \| D_{\mathbb{P}_X}^{\kappa}T_\pi - T_\pi D_{\mathbb{P}_Y}^{\kappa} \|_{\mathrm{HS}}^2}_{= \mathcal{L}(\pi)} ,
>$$
>
>Then, $$\mathcal{L}(\pi)$$ is convex with respect to $\pi$.

# Consistency

* As mentioned earlier, we utilize a projection-free Frank-Wolfe (FW) method to solve the quadratic optimization problem.
* Leveraging the convexity of the objective, we derive a finite-sample error bound that decomposes into two terms: an **optimization error** (from the FW algorithm) and a **statistical error** (from empirical approximation).

**Theorem 2 (Consistency).**
>Let $$\hat{\pi}$$ be the output of the proposed algorithm after $T$ iterations, and let $$\mathcal{L}_n(\pi)$$ denote the empirical version of $$\mathcal{L}(\pi)$$. In addition, let $$\hat{\mathbb{P}}_X$$ and $$\hat{\mathbb{P}}_Y$$ be the empirical probability measures associated with $$\mathbb{P}_X$$ and $$\mathbb{P}_Y$$, respectively. Then, under mild regularity conditions,
>
>$$
>\left\vert \mathcal{L}_{n}(\hat{\pi}) - \inf_{\pi \in \Pi(\mathbb{P}_X,\mathbb{P}_Y)} \mathcal{L}(\pi) \right\vert \leq \underbrace{\frac{8\alpha \, n}{(T+1)}}_{\text{Optimization error}} + C\underbrace{\left(W_2^{d_{\mathcal{X}}}(\mathbb{P}_X,\hat{\mathbb{P}}_X) + W_2^{d_{\mathcal{Y}}}(\mathbb{P}_Y,\hat{\mathbb{P}}_Y) \right)}_{\text{Statistical error}} ,
>$$
>
>where $W_2^d$ denotes the 2-Wasserstein distance with respect to the metric $d$, and $C > 0$ is a constant.

# Discussion

* This work introduces a **convex** operator fused optimal transport framework that preserves spectral geometry while remaining amenable to large-scale optimization.
* More broadly, the framework is not restricted to distance potential operators; replacing $$D^\kappa$$ by other structurally meaningful operators (e.g., Laplacians, diffusion or transfer operators, graph filters, or application-specific integral operators) could yield new variants of **optimal transport that preserve dynamics, functional structure, or task-specific notions of geometry**.

# References

* Mémoli, F. (2011). Gromov–Wasserstein distances and the metric approach to object matching. Foundations of computational mathematics, 11(4), 417-487.
* Vayer, T., Chapel, L., Flamary, R., Tavenard, R., & Courty, N. (2020). Fused Gromov-Wasserstein distance for structured objects. Algorithms, 13(9), 212.