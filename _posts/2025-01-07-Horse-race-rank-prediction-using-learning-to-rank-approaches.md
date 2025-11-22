---
title: Horse race rank prediction using learning-to-rank approaches
tags:
    - Research summary
---

This post is the summary of <a href="https://www.kjas.or.kr/journal/view.html?uid=135&vmd=Full&">Chung, J., Shin, D., Hwang, S., & Park, G. (2024). Horse race rank prediction using learning-to-rank approaches. Korean Journal of Applied Statistics, 37(2), 239-253.</a>

<!--more-->

---

# Objective

This research aims to apply the <a href="https://en.wikipedia.org/wiki/Learning_to_rank">**Learning-to-Rank technique**</a> to horse racing and compare its performance with existing research.

# Contributions

* Applies the pair-wise learning approach to horse racing that has been relatively underexplored.
* Uses various datasets such as `Start training information` and `Horse diagnosis record`, which contributes to the enhancement of predictability and interpretability.
* Resolves the issue of data imbalance due to varying race distances by standardizing the race records.
* Ensures the model interpretability through the use of <a href="https://en.wikipedia.org/wiki/Shapley_value">Shapley value analysis</a>.

# Learning-to-Rank

<div style="display: flex; justify-content: space-between; gap: 20px;">

  <!-- First Table -->
  <div style="flex: 0 0 48%; text-align: center; box-sizing: border-box;">
    <table style="width: 100%; border-collapse: collapse; text-align: center; border : none; table-layout: fixed;">
      <thead style="background-color: #f2f2f2;">
        <tr>
          <th style="padding: 8px;">Rank</th>
          <th style="padding: 8px;">Score</th>
          <th style="padding: 8px;">Item vector</th>
          <th style="padding: 8px;">Query vector</th>
        </tr>
      </thead>
      <tbody>
        <tr>
          <td style="padding: 8px; border-bottom: 1px solid lightgray;">1</td>
          <td style="padding: 8px; border-bottom: 1px solid lightgray;">\(y_1^1\)</td>
          <td style="padding: 8px; border-bottom: 1px solid lightgray;">\(\mathbf{x}_1^1\)</td>
          <td style="padding: 8px; border-bottom: 1px solid lightgray;">\(\mathbf{z}_1\)</td>
        </tr>
        <tr>
          <td style="padding: 8px; border-bottom: 1px solid lightgray;">2</td>
          <td style="padding: 8px; border-bottom: 1px solid lightgray;">\(y_1^2\)</td>
          <td style="padding: 8px; border-bottom: 1px solid lightgray;">\(\mathbf{x}_1^2\)</td>
          <td style="padding: 8px; border-bottom: 1px solid lightgray;">\(\mathbf{z}_1\)</td>
        </tr>
        <tr>
          <td style="padding: 8px; border-bottom: 3px solid black;">3</td>
          <td style="padding: 8px; border-bottom: 3px solid black;">\(y_1^3\)</td>
          <td style="padding: 8px; border-bottom: 3px solid black;">\(\mathbf{x}_1^3\)</td>
          <td style="padding: 8px; border-bottom: 3px solid black;">\(\mathbf{z}_1\)</td>
        </tr>
        <tr>
          <td style="padding: 8px;">\(\pi_1\)</td>
          <td style="padding: 8px;">\(\mathbf{y}_1\)</td>
          <td style="padding: 8px;">\(\mathbf{X}_1\)</td>
          <td style="padding: 8px;">\(\mathbf{Z}_1\)</td>
        </tr>
      </tbody>
    </table>
    <p style="margin-top: 10px; font-size: 14px; color: #555;">Table 1. Query 1 Example (\(n_1 = 3\))</p>
  </div>

  <!-- Second Table -->
  <div style="flex: 0 0 48%; text-align: center; box-sizing: border-box;">
    <table style="width: 100%; border-collapse: collapse; text-align: center; border : none; table-layout: fixed;">
      <thead style="background-color: #f2f2f2;">
        <tr>
          <th style="padding: 8px;">Rank</th>
          <th style="padding: 8px;">Score</th>
          <th style="padding: 8px;">Item vector</th>
          <th style="padding: 8px;">Query vector</th>
        </tr>
      </thead>
      <tbody>
        <tr>
          <td style="padding: 8px; border-bottom: 1px solid lightgray;">1</td>
          <td style="padding: 8px; border-bottom: 1px solid lightgray;">\(y_2^1\)</td>
          <td style="padding: 8px; border-bottom: 1px solid lightgray;">\(\mathbf{x}_2^1\)</td>
          <td style="padding: 8px; border-bottom: 1px solid lightgray;">\(\mathbf{z}_2\)</td>
        </tr>
        <tr>
          <td style="padding: 8px; border-bottom: 1px solid lightgray;">2</td>
          <td style="padding: 8px; border-bottom: 1px solid lightgray;">\(y_2^2\)</td>
          <td style="padding: 8px; border-bottom: 1px solid lightgray;">\(\mathbf{x}_2^2\)</td>
          <td style="padding: 8px; border-bottom: 1px solid lightgray;">\(\mathbf{z}_2\)</td>
        </tr>
        <tr>
          <td style="padding: 8px; border-bottom: 3px solid black;">3</td>
          <td style="padding: 8px; border-bottom: 3px solid black;">\(y_2^3\)</td>
          <td style="padding: 8px; border-bottom: 3px solid black;">\(\mathbf{x}_2^3\)</td>
          <td style="padding: 8px; border-bottom: 3px solid black;">\(\mathbf{z}_2\)</td>
        </tr>
        <tr>
          <td style="padding: 8px;">\(\pi_2\)</td>
          <td style="padding: 8px;">\(\mathbf{y}_2\)</td>
          <td style="padding: 8px;">\(\mathbf{X}_2\)</td>
          <td style="padding: 8px;">\(\mathbf{Z}_2\)</td>
        </tr>
      </tbody>
    </table>
    <p style="margin-top: 10px; font-size: 14px; color: #555;">Table 2. Query 2 Example (\(n_2 = 3\))</p>
  </div>

</div>


* The Learning-to-Rank (LTR) technique is a machine learning method used for ranking predictions in various fields, including information retrieval systems, recommendation systems, online advertising, and document classification.

* The goal of the Learning-to-Rank (LTR) technique is to identify a predictive function $\hat{f}$ by minimzing an appropriate loss function $\mathcal{L}$ by
  
$$
\hat{f} = \arg\min_f{\mathcal{L}(f(\mathbf{X},\mathbf{Z}),\mathbf{y})}, \quad \hat{y}_q^i = \hat{f}(\mathbf{x}_q^i,\mathbf{z}_q), \quad \hat{\pi}_q^i = \sum_{j=1}^{n_q}{I(\hat{y}_q^j \geq \hat{y}_q^i)} .
$$

## Point-wise learning

Point-wise learning is a method that learns the score of each item individually. For example, if $\ell_2$-norm is chosen for the 2-queries case as above, the loss function would be

$$
\mathcal{L} = \sum_{q=1}^2\left[ (y_q^1 - f(\mathbf{x}_q^1,\mathbf{z}_q))^2 + (y_q^2 - f(\mathbf{x}_q^2,\mathbf{z}_q))^2 + (y_q^3 - f(\mathbf{x}_q^3,\mathbf{z}_q))^2 \right] .
$$

* It focuses solely on predicting the scores of individual items and does not learn the relationships or order among items within a query.
* E.g., linear regression, random forest, etc.

## Pair-wise learning

Pair-wise learning is a method that compares the scores of all possible pairs of items and predicts higher scores for those with higher ranks.

$$
\mathcal{L} = -\sum_{q=1}^2\left[ \log{P_{12}} + \log{P_{13}} + \log{P_{23}} \right] , \quad \text{where} \quad P_{ij} = \frac{1}{1+e^{-\sigma(\hat{y}_q^i - \hat{y}_q^j)}}, \quad \sigma > 0 .
$$

* It not only enables the learning of the relative ranking relationships between items but is also efficient in that it requires significantly less computational effort compared to considering all possible combinations.
* E.g., RankNet, LambdaMART(XGBoost, LightGBM, CatBoost), etc.

## List-wise learning

List-wise learning directly optimizes a ranking metric or loss function based on the order of items in the entire list.

$$
\mathcal{L} =  -\sum_{q=1}^2\log\left[ \frac{e^{\hat{y}_q^1}}{e^{\hat{y}_q^1}+e^{\hat{y}_q^2}+e^{\hat{y}_q^3}} \times \frac{e^{\hat{y}_q^2}}{e^{\hat{y}_q^2}+e^{\hat{y}_q^3}} \times \frac{e^{\hat{y}_q^3}}{e^{\hat{y}_q^3}} \right] .
$$

* It addresses the limitation of the pair-wise approach by learning the complete relationships within each query. However, it requires a large sample size and may struggle to perform effectively when faced with issues such as missing values or outliers.
* E.g., ListNet, ListMLE, etc.

# Horse race data

## Data description

<table style="width: 100%; border-collapse: collapse; text-align: left; border: 1px solid lightgray">
  <thead style="background-color: #f2f2f2;">
    <tr>
      <th style="border: 1px solid lightgray; padding: 8px;">Category</th>
      <th style="border: 1px solid lightgray; padding: 8px;">Dataset</th>
      <th style="border: 1px solid lightgray; padding: 8px;">Main variables</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td colspan="3" style="border: 1px solid lightgray; padding: 8px; text-align: center; background-color: #e6e6e6;">
        **Data Collection Period: 2013.01 ~ 2023.07**
      </td>
    </tr>
    <tr>
      <td rowspan="3" style="border: 1px solid lightgray; padding: 8px; vertical-align: top; font-weight: bold;">Race</td>
      <td style="border: 1px solid lightgray; padding: 8px;">Race performance data</td>
      <td style="border: 1px solid lightgray; padding: 8px;">Race time, ranking, grade, number of horses, race number, race distance, carried weight, weight change</td>
    </tr>
    <tr>
      <td style="border: 1px solid lightgray; padding: 8px;">Track information</td>
      <td style="border: 1px solid lightgray; padding: 8px;">Track moisture, track condition</td>
    </tr>
    <tr>
      <td style="border: 1px solid lightgray; padding: 8px;">Weather information</td>
      <td style="border: 1px solid lightgray; padding: 8px;">Weather</td>
    </tr>
    <tr>
      <td style="border: 1px solid lightgray; padding: 8px; font-weight: bold;">Jockey</td>
      <td style="border: 1px solid lightgray; padding: 8px;">Jockey career records</td>
      <td style="border: 1px solid lightgray; padding: 8px;">Total 1st, 2nd, 3rd place counts and total race entries</td>
    </tr>
    <tr>
      <td rowspan="4" style="border: 1px solid lightgray; padding: 8px; vertical-align: top; font-weight: bold;">Horse</td>
      <td style="border: 1px solid lightgray; padding: 8px;">Horse career records</td>
      <td style="border: 1px solid lightgray; padding: 8px;">Total 1st, 2nd, 3rd place counts and total race entries</td>
    </tr>
    <tr>
      <td style="border: 1px solid lightgray; padding: 8px;">Detailed horse data</td>
      <td style="border: 1px solid lightgray; padding: 8px;">Age, weight, gender, origin</td>
    </tr>
    <tr>
      <td style="border: 1px solid lightgray; padding: 8px;">Veterinary records</td>
      <td style="border: 1px solid lightgray; padding: 8px;">Diagnosis counts</td>
    </tr>
    <tr>
      <td style="border: 1px solid lightgray; padding: 8px;">Starting training data</td>
      <td style="border: 1px solid lightgray; padding: 8px;">Starting training sessions</td>
    </tr>
    <tr>
      <td rowspan="2" style="border: 1px solid lightgray; padding: 8px; vertical-align: top; font-weight: bold;">Trainer</td>
      <td style="border: 1px solid lightgray; padding: 8px;">Trainer career records</td>
      <td style="border: 1px solid lightgray; padding: 8px;">Total 1st, 2nd, 3rd place counts and total race entries</td>
    </tr>
    <tr>
      <td style="border: 1px solid lightgray; padding: 8px;">Trainer details</td>
      <td style="border: 1px solid lightgray; padding: 8px;">Trainer experience</td>
    </tr>
  </tbody>
</table>

## Standardization of race record

$$
y_q^j = \frac{\tilde{y}_q^j - \bar{\tilde{y}}_d}{\frac{1}{N_d - 1}\sum_{l \in S_d}\sum_{i=1}^{n_l}(\tilde{y}_l^i-\bar{\tilde{y}}_d)^2}, \quad \text{where} \quad N_d = \sum_{l \in S_d}n_l , \quad \bar{\tilde{y}}_d = \frac{1}{N_d}\sum_{l \in S_d}\sum_{i=1}^{n_l}\tilde{y}_l^i .
$$

* $S_d$ is the collection of queries where the race distance is $d$, and $\tilde{y}_q^i$ is horse $i$'s race record in query $q$.
* Since race records vary depending on the corresponding distance, this variation hinders the model's ability to predict ranks consistently.
* This data imbalance issue can be resolved by standardizing the race records.

# Evaluation methods and results

## Evaluation methods

* Win ratios for single, exacta, and trifecta bets, along with Spearman's correlation coefficient, Kendall's tau, and NDCG, were used as evaluation metrics.
* After splitting the data into training and evaluation sets, the evaluation metrics were computed 100 times in total for the evaluation dataset.

## Result

<table style="width: 100%; border-collapse: collapse; text-align: center; font-family: Arial, sans-serif; border: 1px solid lightgray;">
  <thead>
    <tr>
      <th rowspan="2" style="border: 1px solid lightgray; padding: 8px;">Metric</th>
      <th colspan="2" style="border: 1px solid lightgray; padding: 8px;">Point-wise learning</th>
      <!-- <th style="border: 1px solid lightgray; padding: 8px;"></th> -->
      <th colspan="4" style="border: 1px solid lightgray; padding: 8px;">Pair-wise learning</th>
    </tr>
    <tr>
      <th style="border: 1px solid lightgray; padding: 8px;">Linear regression</th>
      <th style="border: 1px solid lightgray; padding: 8px;">Random forest</th>
      <!-- <th style="border: 1px solid lightgray; padding: 8px;"></th> -->
      <th style="border: 1px solid lightgray; padding: 8px;">RankNet</th>
      <th style="border: 1px solid lightgray; padding: 8px;">XGBoost Ranker</th>
      <th style="border: 1px solid lightgray; padding: 8px;">LightGBM Ranker</th>
      <th style="border: 1px solid lightgray; padding: 8px;">CatBoost Ranker</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td style="border: 1px solid lightgray; padding: 8px;">Win probablity (Single)</td>
      <td style="border: 1px solid lightgray; padding: 8px;">0.2744 (0.0117)</td>
      <td style="border: 1px solid lightgray; padding: 8px;">0.2598 (0.0102)</td>
      <!-- <td style="border: 1px solid lightgray; padding: 8px;"></td> -->
      <td style="border: 1px solid lightgray; padding: 8px;">0.2600 (0.0124)</td>
      <td style="border: 1px solid lightgray; padding: 8px;">0.2733 (0.0102)</td>
      <td style="border: 1px solid lightgray; padding: 8px;">0.2803 (0.0110)</td>
      <td style="border: 1px solid lightgray; padding: 8px;"><b>0.3049 (0.0107)</b></td>
    </tr>
    <tr>
      <td style="border: 1px solid lightgray; padding: 8px;">Win probablity (Exacta)</td>
      <td style="border: 1px solid lightgray; padding: 8px;">0.1155 (0.0066)</td>
      <td style="border: 1px solid lightgray; padding: 8px;">0.1070 (0.0074)</td>
      <!-- <td style="border: 1px solid lightgray; padding: 8px;"></td> -->
      <td style="border: 1px solid lightgray; padding: 8px;">0.1087 (0.0090)</td>
      <td style="border: 1px solid lightgray; padding: 8px;">0.1142 (0.0069)</td>
      <td style="border: 1px solid lightgray; padding: 8px;">0.1225 (0.0065)</td>
      <td style="border: 1px solid lightgray; padding: 8px;"><b>0.1345 (0.0075)</b></td>
    </tr>
    <tr>
      <td style="border: 1px solid lightgray; padding: 8px;">Win probablity (Trifecta)</td>
      <td style="border: 1px solid lightgray; padding: 8px;">0.0643 (0.0058)</td>
      <td style="border: 1px solid lightgray; padding: 8px;">0.0579 (0.0062)</td>
      <!-- <td style="border: 1px solid lightgray; padding: 8px;"></td> -->
      <td style="border: 1px solid lightgray; padding: 8px;">0.0585 (0.0067)</td>
      <td style="border: 1px solid lightgray; padding: 8px;">0.0625 (0.0060)</td>
      <td style="border: 1px solid lightgray; padding: 8px;">0.0701 (0.0052)</td>
      <td style="border: 1px solid lightgray; padding: 8px;"><b>0.0771 (0.0059)</b></td>
    </tr>
    <tr>
      <td style="border: 1px solid lightgray; padding: 8px;">Spearman correlation</td>
      <td style="border: 1px solid lightgray; padding: 8px;">0.4080 (0.0077)</td>
      <td style="border: 1px solid lightgray; padding: 8px;">0.3859 (0.0074)</td>
      <!-- <td style="border: 1px solid lightgray; padding: 8px;"></td> -->
      <td style="border: 1px solid lightgray; padding: 8px;">0.3844 (0.0157)</td>
      <td style="border: 1px solid lightgray; padding: 8px;">0.4037 (0.0070)</td>
      <td style="border: 1px solid lightgray; padding: 8px;">0.4284 (0.0071)</td>
      <td style="border: 1px solid lightgray; padding: 8px;"><b>0.4474 (0.0075)</b></td>
    </tr>
    <tr>
      <td style="border: 1px solid lightgray; padding: 8px;">Kendall's Tau</td>
      <td style="border: 1px solid lightgray; padding: 8px;">0.3129 (0.0062)</td>
      <td style="border: 1px solid lightgray; padding: 8px;">0.2951 (0.0058)</td>
      <!-- <td style="border: 1px solid lightgray; padding: 8px;"></td> -->
      <td style="border: 1px solid lightgray; padding: 8px;">0.2935 (0.0126)</td>
      <td style="border: 1px solid lightgray; padding: 8px;">0.3083 (0.0058)</td>
      <td style="border: 1px solid lightgray; padding: 8px;">0.2935 (0.0126)</td>
      <td style="border: 1px solid lightgray; padding: 8px;"><b>0.3439 (0.0061)</b></td>
    </tr>
    <tr>
      <td style="border: 1px solid lightgray; padding: 8px;">NDCG</td>
      <td style="border: 1px solid lightgray; padding: 8px;">0.7025 (0.0040)</td>
      <td style="border: 1px solid lightgray; padding: 8px;">0.7001 (0.0043)</td>
      <!-- <td style="border: 1px solid lightgray; padding: 8px;"></td> -->
      <td style="border: 1px solid lightgray; padding: 8px;">0.6901 (0.0071)</td>
      <td style="border: 1px solid lightgray; padding: 8px;">0.7002 (0.0042)</td>
      <td style="border: 1px solid lightgray; padding: 8px;">0.6901 (0.0071)</td>
      <td style="border: 1px solid lightgray; padding: 8px;"><b>0.7149 (0.0042)</b></td>
    </tr>
  </tbody>
</table>

* A total of six models were fitted, including linear regression and random forest from point-wise learning, and RankNet, LambdaMART (XGBoost, LightGBM, and CatBoost) from pair-wise learning.
* Except for RankNet, the pair-wise learning models generally outperformed the point-wise learning models.
* The CatBoost Ranker demonstrated the best performance across all evaluation metrics, likely due to its strong capability in handling categorical variables.

# Shapley value: Point-wise vs. Pair-wise

<div style="display: flex; justify-content: center;">
    <figure style="text-align: center;">
        <img src="/assets/images/horserace-rf_shap.png" alt="RandomForest Shapley values" style="width: 100%; margin-right: 10px;">
        <figcaption>Figure (a): Random forest Shapley values (point-wise)</figcaption>
    </figure>
    <figure style="text-align: center;">
        <img src="/assets/images/horserace-cat_shap.png" alt="CatBoost Shapley values" style="width: 100%;">
        <figcaption>Figure (b): CatBoost Ranker Shapley values (pair-wise)</figcaption>
    </figure>
</div>

* Newly added variables, such as standardized previous race records and horse performance, significantly influence prediction performance.
* In point-wise models like random forest, common variables shared across races, such as humidity and race distance, were selected as key predictors. In contrast, in pair-wise models like the CatBoost Ranker, variables reflecting differences among horses, such as horse age and carried weight, were identified as key factors.
* This highlights the characteristics of pair-wise learning, suggesting that variables representing relative differences in horse abilities are more critical for rank prediction.
* The CatBoost Ranker tends to predict shorter standardized race records for horses with better previous performances and shorter standardized previous race records.
* Additionally, it predicts shorter standardized race records for younger horses, those with lower race entry numbers, and higher track humidity levels, aligning with findings from previous research.

# Performance of CatBoost Ranker

<div style="display: flex; justify-content: center;">
    <img src="/assets/images/horserace-catboost_result.png" alt="Prediction results" style="width: 100%; margin-right: 10px;">
</div>

* The precision for each rank was calculated on a new dataset from Jul 2023 - Nov 2023.
* Relatively high accuracy was observed for the 1st, 2nd, and 8th ranks, but the precision declined for ranks in between.
* Future research could explore methodologies specifically designed to improve accuracy for predicting mid-level ranks.

# Reference

* Chung, J., Shin, D., Hwang, S., & Park, G. (2024). Horse race rank prediction using learning-to-rank approaches. Korean Journal of Applied Statistics, 37(2), 239-253.