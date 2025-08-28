---
layout: article
titles:
  # @start locale config
  en      : &EN       Publications
  en-GB   : *EN
  en-US   : *EN
  en-CA   : *EN
  en-AU   : *EN
  zh-Hans : &ZH_HANS  
  zh      : *ZH_HANS
  zh-CN   : *ZH_HANS
  zh-SG   : *ZH_HANS
  zh-Hant : &ZH_HANT  
  zh-TW   : *ZH_HANT
  zh-HK   : *ZH_HANT
  ko      : &KO       출판
  ko-KR   : *KO
  fr      : &FR       
  fr-BE   : *FR
  fr-CA   : *FR
  fr-CH   : *FR
  fr-FR   : *FR
  fr-LU   : *FR
  # @end locale config
---

\* indicates the first author, and &dagger; indicates the authors who contributed equally.

## Published papers

### 2025

* Joonho Shin<sup>&dagger;</sup>, _**Junhyoung Chung**_<sup>&dagger;</sup>, Seyong Hwang<sup>&dagger;</sup>, Gunwoong Park<sup>&dagger;</sup> \\
  Discovering causal structures in corrupted data: Frugality in anchored Gaussian DAG models \\
  In *Computational Statistics and Data Analysis, 213*, 108267, [<u>10.1016/j.csda.2025.108267</u>](https://doi.org/10.1016/j.csda.2025.108267) \\
  <details class="link-toggle">
    <summary>[Abstract]</summary>
    <div class="toggle-content">
      <!-- 여기에 초록 내용 -->
      This study focuses on the recovery of anchored Gaussian directed acyclic graphical (DAG) models to address the challenge of discovering causal or directed relationships among variables in datasets that are either intentionally masked or contaminated due to measurement errors. A main contribution is to relax the existing restrictive identifiability conditions for anchored Gaussian DAG models by introducing the anchored-frugality assumption. This assumption posits that the true graph is the most frugal among those satisfying the possible distributions of the latent and observed variables, thereby making the true Markov equivalent class (MEC) identifiable. The validity of the anchored-frugality assumption is justified using both graph and probability theories, respectively. Another main contribution is the development of the anchored-SP and frugal-PC algorithms. Specifically, the anchored-SP algorithm finds the most frugal graph among all possible graphs satisfying the Markov condition while the frugal-PC algorithm finds the most frugal graph among some graphs. Hence, the frugal-PC algorithm is more computationally feasible, while it requires an additional frugality-faithfulness assumption for soundness. Various simulations support the theoretical findings of this study and demonstrate the practical effectiveness of the proposed algorithm against state-of-the-art algorithms such as ACI, PC, and MMHC. Furthermore, the applications of the proposed algorithm to protein signaling data and breast cancer data illustrate its effectiveness in uncovering relationships among proteins and among cancer-related cell nuclei characteristics.
    </div>
    <br/>
  </details>

### 2024

* _**Junhyoung Chung**_<sup>\*</sup>, Youngmin Ahn, Donguk Shin, Gunwoong Park [\[Summary\]](/2025/01/19/Learning-distribution-free-anchored-linear-structural-equation-models-in-the-presence-of-measurement-error.html) \\
  Learning distribution-free anchored linear structural equation models in the presence of measurement error \\
  In *Journal of the Korean Statistical Society*, 1–25, [<u>10.1007/s42952-024-00298-9</u>](https://doi.org/10.1007/s42952-024-00298-9) \\
  <details class="link-toggle">
    <summary>[Abstract]</summary>
    <div class="toggle-content">
      <!-- 여기에 초록 내용 -->
      This study tackles the challenge of identifiability in distribution-free anchored linear structural equation models (SEMs), where the observed variables are imperfect measures for the target variables, and the error distributions are not restricted to being Gaussian. It introduces the geometry-faithfulness assumption, ensuring that partial correlations serve as direct indicators of d-separation/connection. The study establishes the identifiability of distribution-free anchored linear SEMs under the same identifiability conditions for anchored Gaussian linear SEMs, but by replacing the faithfulness assumption with the geometry-faithfulness assumption. Moreover, it shows that the learning algorithm leveraging the PC algorithm with Fisher’s z-test, originally designed for anchored Gaussian linear SEMs, remains applicable and effective for distribution-free anchored linear SEMs. It also provides statistical guarantees for the proposed algorithm, including the strong geometry-faithfulness assumption, ensuring its consistency. These theoretical contributions are validated through extensive numerical experiments and the analysis of real galaxy data.
    </div>
    <br/>
  </details>

* _**Junhyoung Chung**_<sup>\*</sup>, Donguk Shin, Seyong Hwang, Gunwoong Park [\[Summary\]](/2025/01/07/Horse-race-rank-prediction-using-learning-to-rank-approaches.html) \\
  Horse race rank prediction using learning-to-rank approaches (*Written in Korean*) \\
  In *Korean Journal of Applied Statistics, 37*(2), 239-253, [<u>10.5351/KJAS.2024.37.2.239</u>](https://doi.org/10.5351/KJAS.2024.37.2.239) \\
  <details class="link-toggle">
    <summary>[Abstract]</summary>
    <div class="toggle-content">
      <!-- 여기에 초록 내용 -->
      This research applies both point-wise and pair-wise learning strategies within the learning-to-rank (LTR)
      framework to predict horse race rankings in Seoul. Specifically, for point-wise learning, we employ a linear model and random forest. In contrast, for pair-wise learning, we utilize tools such as RankNet, and LambdaMART (XGBoost Ranker, LightGBM Ranker, and CatBoost Ranker). Furthermore, to enhance predictions, race records are standardized based on race distance, and we integrate various datasets, including race information, jockey information, horse training records, and trainer information. Our results empirically demonstrate that pair-wise learning approaches that can reflect the order information between items generally outperform point-wise learning approaches. Notably, CatBoost Ranker is the top performer. Through Shapley value analysis, we identified that the important variables for CatBoost Ranker include the performance of a horse, its previous race records, the count of its starting trainings, the total number of starting trainings, and the instances of disease diagnoses for the horse.
    </div>
    <br/>
  </details>
  

## Accepted papers

* _**Junhyoung Chung**_<sup>\*</sup>, Sungjin Lee, Gunwoong Park \\
  Prediction of high-risk mountain accident areas using a Hurdle model (*Written in Korean*) \\
  Accepted in *Korean Journal of Applied Statistics* \\
  <details class="link-toggle">
    <summary>[Abstract]</summary>
    <div class="toggle-content">
      <!-- 여기에 초록 내용 -->
      This study predicts the average $6$-hourly number of mountain accidents using data from 18 mountainous national parks in Korea, including Jirisan, Seoraksan, and Sobaeksan. Specifically, to achieve both fine-grained prediction and identify important variables, we divide mountain regions into grids, enabling risk prediction at both the mountain level and the specific grid level. Additionally, a Hurdle model is applied to address zero-inflated data, as mountain accidents often do not occur in many regions due to sparse population or generally safe areas. The Hurdle model is implemented via a generalized linear model, random forest, and gradient boosting decision trees (XGBoost, LightGBM, and CatBoost). An extensive exploratory data analysis is also conducted to enhance prediction accuracy and validate our analytic approach. Through a feature importance analysis, we find that climate-related variables are important for predicting the probability of an accident, while geological factors (slope and elevation) and temporal information are key contributors to modeling the count of accidents.
    </div>
    <br/>
  </details>

<!-- ## On-going works -->
