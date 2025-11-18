---
title: 'Prediction of high-risk mountain accident areas using a Hurdle model'
tags:
    - Research summary
---

This post is the summary of <a href="https://www.kjas.or.kr/journal/view.html?doi=10.5351/KJAS.2025.38.4.531">Chung, J., Lee, S., & Park, G. (2025). Prediction of high-risk mountain accident areas using a Hurdle model. Korean Journal of Applied Statistics, 38(4), 531-551.</a>

<!--more-->

---

<div style="display: flex; justify-content: center;">
    <figure style="text-align: center;">
        <img src="/assets/images/grid_seorak.jpg" alt="Single 1km X 1km grid of Seorak" style="width: 100%; margin-right: 10px;">
        <figcaption>Figure (a): Single 1km X 1km grid of Seorak</figcaption>
    </figure>
    <figure style="text-align: center;">
        <img src="/assets/images/grid_seorak_type.jpg" alt="Visualization of grid by accident type in Seorak" style="width: 100%;">
        <figcaption>Figure (b): Visualization of grid by accident type in Seorak</figcaption>
    </figure>
</div>

# Objective

This study aims to provide a grid-based Hurdle model to predict the average 6-hourly number of mountain accidents using data from 18 mountainous national parks in South Korea.

# Contributions

* Applies the **grid-based approach**, partitioning each national park into a small grid, thereby integrating spatial information such as elevation and slope.
* Uses a **Hurdle model** to effectively address zero-inflated accident data.
* Reveals that **climate-related variables** play a crucial role in accident probability, while **geological factors** (e.g., slope, elevation) are significant for accident frequency.

# Hurdle model

* A Hurdle model is a class of statistical models where a random variable is modeled using two parts: (i) the probability to attain zero, and (ii) the probability of the non-zero values.
* Specifically, the $i$-th response variable $Y_i$ follows a Poisson Hurdle model defined as

  $$
  P(Y_i = y) = \begin{cases}
                  \pi_i , & y = 0, \\
                  \frac{1-\pi_i}{1-e^{-\lambda_i}} \times \frac{\lambda_i^y e^{-\lambda_i}}{y !} , & y \in \mathbb{N} ,
              \end{cases}
  $$

  where $\pi_i$ and $\lambda_i$ parameters are modeled by the $i$-th predictor $\mathbf{x}_i$.

* The Poisson Hurdle model is effective as it decouples the zero and non-zero parts, allowing for separate modeling of each process.
* In this study, we apply distinct models for each component:
  * For the **zero** part: Logistic regression and classification tree-based models (Random Forest, XGBoost, LightGBM, CatBoost).
  * For the **non-zero** part: Poisson regression and the corresponding regression tree models.

# Mountain accident data

## Data description

<table style="width: 100%; border-collapse: collapse; text-align: left; border: 1px solid lightgray; font-size: 14px;">
  <thead style="background-color: #f2f2f2;">
    <tr>
      <th style="border: 1px solid lightgray; padding: 8px;">Category</th>
      <th style="border: 1px solid lightgray; padding: 8px;">Dataset</th>
      <th style="border: 1px solid lightgray; padding: 8px;">Main variables</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td colspan="3" style="border: 1px solid lightgray; padding: 8px; text-align: center; background-color: #e6e6e6; font-weight: bold;">
        Input Variables
      </td>
    </tr>
    
    <tr>
      <td style="border: 1px solid lightgray; padding: 8px; vertical-align: top; font-weight: bold;">Terrain</td>
      <td style="border: 1px solid lightgray; padding: 8px;">Terrain information</td>
      <td style="border: 1px solid lightgray; padding: 8px;">Elevation (m), Slope (°)</td>
    </tr>

    <tr>
      <td style="border: 1px solid lightgray; padding: 8px; vertical-align: top; font-weight: bold;">Rescue</td>
      <td style="border: 1px solid lightgray; padding: 8px;">Accident details</td>
      <td style="border: 1px solid lightgray; padding: 8px;">Mountain name, Accident month, Day of the week, Accident time (hour)</td>
    </tr>

    <tr>
      <td rowspan="5" style="border: 1px solid lightgray; padding: 8px; vertical-align: top; font-weight: bold;">Weather</td>
      <td style="border: 1px solid lightgray; padding: 8px;">Wind & Pressure</td>
      <td style="border: 1px solid lightgray; padding: 8px;">Wind direction/speed (WD, WS), Gust (GST), Atmospheric/Surface pressure (PA, PS), Pressure change (PR, PT)</td>
    </tr>
    <tr>
      <td style="border: 1px solid lightgray; padding: 8px;">Temp & Humidity</td>
      <td style="border: 1px solid lightgray; padding: 8px;">Air temperature (TA), Dew point (TD), Humidity (HM), Vapor pressure (PV)</td>
    </tr>
    <tr>
      <td style="border: 1px solid lightgray; padding: 8px;">Precipitation</td>
      <td style="border: 1px solid lightgray; padding: 8px;">Rainfall (RN), Daily/Total rainfall, Snow depth (SD), Daily/Total snow depth</td>
    </tr>
    <tr>
      <td style="border: 1px solid lightgray; padding: 8px;">Sky & Visibility</td>
      <td style="border: 1px solid lightgray; padding: 8px;">Cloud cover (CA), Cloud height (CH), Visibility (VS), Sunshine (SS), Solar irradiance (SI), Cloud classification (CT)</td>
    </tr>
    <tr>
      <td style="border: 1px solid lightgray; padding: 8px;">Surface & Others</td>
      <td style="border: 1px solid lightgray; padding: 8px;">Surface temperature (TS), Soil temperature (TE), Wave height (WH), Weather conditions (WC, WP)</td>
    </tr>

    <tr>
      <td colspan="3" style="border: 1px solid lightgray; padding: 8px; text-align: center; background-color: #e6e6e6; font-weight: bold;">
        Output Variables
      </td>
    </tr>

    <tr>
      <td style="border: 1px solid lightgray; padding: 8px; vertical-align: top; font-weight: bold;">Target</td>
      <td style="border: 1px solid lightgray; padding: 8px;">Model Targets</td>
      <td style="border: 1px solid lightgray; padding: 8px;">
        <strong>Count:</strong> Number of accidents per grid<br>
        <strong>Probability:</strong> Accident probability per grid
      </td>
    </tr>
  </tbody>
</table>

## Accident patterns

<table style="width: 100%; min-width: 100%; display: table; border-collapse: collapse; border: 1px solid #ddd; font-size: 14px; background-color: #ffffff; table-layout: fixed;">
  <thead style="background-color: #f8f9fa;">
    <tr>
      <th style="width: 15%; border: 1px solid #ddd; padding: 10px; text-align: left;">Mountain</th>
      <th style="width: 15%; border: 1px solid #ddd; padding: 10px; text-align: right;">Area (km²)</th>
      <th style="width: 18%; border: 1px solid #ddd; padding: 10px; text-align: right;">Visitors (2023)</th>
      <th style="width: 15%; border: 1px solid #ddd; padding: 10px; text-align: center;">
        \(\hat{P}(Y = 0)\)<br>
        <span style="font-weight: normal; font-size: 12px; color: #888;">(No Accident)</span>
      </th>
      <th style="width: 15%; border: 1px solid #ddd; padding: 10px; text-align: center;">
        \(\hat{P}(Y \geq 1)\)<br>
        <span style="font-weight: normal; font-size: 12px; color: #888;">(Accident)</span>
      </th>
      <th style="border: 1px solid #ddd; padding: 10px; text-align: center;">
        \(\hat{P}(Y \geq 2 \mid Y \geq 1)\)<br>
        <span style="font-weight: normal; font-size: 12px; color: #888;">(Multiple)</span>
      </th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td style="border: 1px solid #ddd; padding: 10px; font-weight: bold; text-align: left;">Jirisan</td>
      <td style="border: 1px solid #ddd; padding: 10px; text-align: right;">485.65</td>
      <td style="border: 1px solid #ddd; padding: 10px; text-align: right;">2,318,032</td>
      <td style="border: 1px solid #ddd; padding: 10px; text-align: center;">0.6151</td>
      <td style="border: 1px solid #ddd; padding: 10px; text-align: center;">0.3849</td>
      <td style="border: 1px solid #ddd; padding: 10px; text-align: center;">0.5017</td>
    </tr>
    <tr>
      <td style="border: 1px solid #ddd; padding: 10px; font-weight: bold; text-align: left;">Seoraksan</td>
      <td style="border: 1px solid #ddd; padding: 10px; text-align: right;">400.03</td>
      <td style="border: 1px solid #ddd; padding: 10px; text-align: right;">3,371,633</td>
      <td style="border: 1px solid #ddd; padding: 10px; text-align: center;">0.5758</td>
      <td style="border: 1px solid #ddd; padding: 10px; text-align: center;">0.4242</td>
      <td style="border: 1px solid #ddd; padding: 10px; text-align: center;">0.6288</td>
    </tr>
    <tr>
      <td style="border: 1px solid #ddd; padding: 10px; font-weight: bold; text-align: left;">Sobaeksan</td>
      <td style="border: 1px solid #ddd; padding: 10px; text-align: right;">321.26</td>
      <td style="border: 1px solid #ddd; padding: 10px; text-align: right;">1,018,623</td>
      <td style="border: 1px solid #ddd; padding: 10px; text-align: center;">0.8882</td>
      <td style="border: 1px solid #ddd; padding: 10px; text-align: center;">0.1118</td>
      <td style="border: 1px solid #ddd; padding: 10px; text-align: center;">0.4614</td>
    </tr>
    <tr>
      <td style="border: 1px solid #ddd; padding: 10px; font-weight: bold; text-align: left;">Odaesan</td>
      <td style="border: 1px solid #ddd; padding: 10px; text-align: right;">327.90</td>
      <td style="border: 1px solid #ddd; padding: 10px; text-align: right;">1,330,737</td>
      <td style="border: 1px solid #ddd; padding: 10px; text-align: center;">0.8946</td>
      <td style="border: 1px solid #ddd; padding: 10px; text-align: center;">0.1054</td>
      <td style="border: 1px solid #ddd; padding: 10px; text-align: center;">0.4330</td>
    </tr>
    <tr>
      <td style="border: 1px solid #ddd; padding: 10px; font-weight: bold; text-align: left;">Woraksan</td>
      <td style="border: 1px solid #ddd; padding: 10px; text-align: right;">288.14</td>
      <td style="border: 1px solid #ddd; padding: 10px; text-align: right;">1,680,573</td>
      <td style="border: 1px solid #ddd; padding: 10px; text-align: center;">0.8501</td>
      <td style="border: 1px solid #ddd; padding: 10px; text-align: center;">0.1499</td>
      <td style="border: 1px solid #ddd; padding: 10px; text-align: center;">0.4752</td>
    </tr>
  </tbody>
</table>

* The above table presents general statistics (area, visitor counts) alongside estimated accident probabilities, where $Y$ denotes the daily number of accidents.
* The proportion of accident-free days ($\hat{P}(Y = 0)$) exceeds 50% for all mountains, highlighting a distinct zero-inflated phenomenon.
* The data suggests a pattern where accidents trigger further accidents ($\hat{P}(Y \geq 2 \mid Y \geq 1)$), as the probability of additional accidents given an occurence is consistently higher than the unconditional accident probability ($\hat{P}(Y \geq 1)$).

# Results

## Prediction performance

<table style="width: 100%; min-width: 100%; display: table; border-collapse: collapse; border: 1px solid #ddd; font-size: 14px; background-color: #ffffff; table-layout: fixed;">
  <caption style="caption-side: bottom; margin-top: 10px; font-size: 14px; color: #555; text-align: center;">
    Probability prediction evaluations for each model
  </caption>
  <thead style="background-color: #f8f9fa;">
    <tr>
      <th style="width: 20%; border: 1px solid #ddd; padding: 10px; text-align: left;">Metric</th>
      <th style="width: 16%; border: 1px solid #ddd; padding: 10px; text-align: center;">Logistic<br>Regression</th>
      <th style="width: 16%; border: 1px solid #ddd; padding: 10px; text-align: center;">Random<br>Forest</th>
      <th style="width: 16%; border: 1px solid #ddd; padding: 10px; text-align: center;">XGBoost</th>
      <th style="width: 16%; border: 1px solid #ddd; padding: 10px; text-align: center;">LightGBM</th>
      <th style="border: 1px solid #ddd; padding: 10px; text-align: center;">CatBoost</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td style="border: 1px solid #ddd; padding: 10px; text-align: left;">Accuracy</td>
      <td style="border: 1px solid #ddd; padding: 10px; text-align: center;">0.81</td>
      <td style="border: 1px solid #ddd; padding: 10px; text-align: center;">0.81</td>
      <td style="border: 1px solid #ddd; padding: 10px; text-align: center; font-weight: bold;">0.96</td>
      <td style="border: 1px solid #ddd; padding: 10px; text-align: center;">0.95</td>
      <td style="border: 1px solid #ddd; padding: 10px; text-align: center;">0.93</td>
    </tr>
    <tr>
      <td style="border: 1px solid #ddd; padding: 10px; text-align: left;">F1-score</td>
      <td style="border: 1px solid #ddd; padding: 10px; text-align: center;">0.27</td>
      <td style="border: 1px solid #ddd; padding: 10px; text-align: center;">0.27</td>
      <td style="border: 1px solid #ddd; padding: 10px; text-align: center;">0.34</td>
      <td style="border: 1px solid #ddd; padding: 10px; text-align: center; font-weight: bold;">0.47</td>
      <td style="border: 1px solid #ddd; padding: 10px; text-align: center;">0.42</td>
    </tr>
    <tr>
      <td style="border: 1px solid #ddd; padding: 10px; text-align: left;">BIC</td>
      <td style="border: 1px solid #ddd; padding: 10px; text-align: center;">6160.27</td>
      <td style="border: 1px solid #ddd; padding: 10px; text-align: center;">5760.58</td>
      <td style="border: 1px solid #ddd; padding: 10px; text-align: center;">6272.31</td>
      <td style="border: 1px solid #ddd; padding: 10px; text-align: center;">4265.63</td>
      <td style="border: 1px solid #ddd; padding: 10px; text-align: center; font-weight: bold;">4232.00</td>
    </tr>
  </tbody>
</table>

<table style="width: 100%; min-width: 100%; display: table; border-collapse: collapse; border: 1px solid #ddd; font-size: 14px; background-color: #ffffff; table-layout: fixed;">
  <caption style="caption-side: bottom; margin-top: 10px; font-size: 14px; color: #555; text-align: center;">
    Count prediction scores by models
  </caption>
  <thead style="background-color: #f8f9fa;">
    <tr>
      <th style="width: 20%; border: 1px solid #ddd; padding: 10px; text-align: left;">Metric</th>
      <th style="width: 16%; border: 1px solid #ddd; padding: 10px; text-align: center;">Poisson<br>Regression</th>
      <th style="width: 16%; border: 1px solid #ddd; padding: 10px; text-align: center;">Random<br>Forest</th>
      <th style="width: 16%; border: 1px solid #ddd; padding: 10px; text-align: center;">XGBoost</th>
      <th style="width: 16%; border: 1px solid #ddd; padding: 10px; text-align: center;">LightGBM</th>
      <th style="border: 1px solid #ddd; padding: 10px; text-align: center;">CatBoost</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td style="border: 1px solid #ddd; padding: 10px; text-align: left;">MSE</td>
      <td style="border: 1px solid #ddd; padding: 10px; text-align: center;">0.24</td>
      <td style="border: 1px solid #ddd; padding: 10px; text-align: center;">0.24</td>
      <td style="border: 1px solid #ddd; padding: 10px; text-align: center;">0.27</td>
      <td style="border: 1px solid #ddd; padding: 10px; text-align: center;">0.26</td>
      <td style="border: 1px solid #ddd; padding: 10px; text-align: center; font-weight: bold;">0.23</td>
    </tr>
    <tr>
      <td style="border: 1px solid #ddd; padding: 10px; text-align: left;">Poisson deviance</td>
      <td style="border: 1px solid #ddd; padding: 10px; text-align: center;">0.16</td>
      <td style="border: 1px solid #ddd; padding: 10px; text-align: center;">0.16</td>
      <td style="border: 1px solid #ddd; padding: 10px; text-align: center;">0.17</td>
      <td style="border: 1px solid #ddd; padding: 10px; text-align: center;">0.17</td>
      <td style="border: 1px solid #ddd; padding: 10px; text-align: center; font-weight: bold;">0.15</td>
    </tr>
    <tr>
      <td style="border: 1px solid #ddd; padding: 10px; text-align: left;">BIC</td>
      <td style="border: 1px solid #ddd; padding: 10px; text-align: center;">2439.26</td>
      <td style="border: 1px solid #ddd; padding: 10px; text-align: center;">2438.48</td>
      <td style="border: 1px solid #ddd; padding: 10px; text-align: center;">2394.82</td>
      <td style="border: 1px solid #ddd; padding: 10px; text-align: center;">1720.25</td>
      <td style="border: 1px solid #ddd; padding: 10px; text-align: center; font-weight: bold;">1690.31</td>
    </tr>
  </tbody>
</table>

* In probability prediction, **gradient boosting methods (XGBoost, LightGBM, CatBoost)** generally show superior performance compared to linear or tree-based baselines.
  * Specifically, LightGBM achieved the highest F1-score, making it the most suitable model for identifying accident occurrences within imbalanced data.
  * CatBoost recorded the best BIC, demonstrating high efficiency by effectively handling categorical variables with lower dimensionality.
* In count prediction, **CatBoost** outperforms all other models across every metric.
  * This highlights CatBoost's strength in leveraging categorical information, which appears crucial for count prediction.
  * Interestingly, other GBDT models did not significantly surpass Poisson Regression, suggesting that the relationship between accident counts and predictors is relatively linear and simple.
  
## Feature importance analysis

<div style="display: flex; justify-content: center;">
    <figure style="text-align: center;">
        <img src="/assets/images/feature_importance_lightgbm_prob.png" alt="LightGBM classifier" style="width: 100%; margin-right: 10px;">
        <figcaption>Figure (a): LightGBM classifier</figcaption>
    </figure>
    <figure style="text-align: center;">
        <img src="/assets/images/feature_importance_catboost_count.png" alt="CatBoost regressor" style="width: 90%;">
        <figcaption>Figure (b): CatBoost regressor</figcaption>
    </figure>
</div>

* **Probability prediction**: Dominantly influenced by weather variables (e.g., visibility, temperature, wind speed), suggesting that immediate meteorological conditions are the primary drivers of accident occurrence.
* **Count prediction**: Heavily relies on categorical variables (day, month) and terrain features (elevation, slope), indicating that visitor patterns and structural risks drive accident frequency and potential chain reactions.
* **Distinct drivers**: While visibility and humidity affect both models, terrain factors play a significantly larger role in predicting the number of accidents compared to the mere probability of an event.

# References

* Chung, J., Ahn, Y., Shin, D., & Park, G. (2024). Learning distribution-free anchored linear structural equation models in the presence of measurement error. Journal of the Korean Statistical Society, 1-25.
* Raskutti, G., & Uhler, C. (2018). Learning directed acyclic graph models based on sparsest permutations. Stat, 7(1), e183.
* Saeed, B., Belyaeva, A., Wang, Y., & Uhler, C. (2020). Anchored causal inference in the presence of measurement error. In Conference on uncertainty in artificial intelligence (pp. 619-628). PMLR.
* Shin, J., Chung, J., Hwang, S., & Park, G. (2025). Discovering Causal Structures in Corrupted Data: Frugality in Anchored Gaussian DAG Models. Computational Statistics & Data Analysis, 108267.
* Street, W. N., Wolberg, W. H., & Mangasarian, O. L. (1993, July). Nuclear feature extraction for breast tumor diagnosis. In Biomedical image processing and biomedical visualization (Vol. 1905, pp. 861-870). SPIE.
* Zhang, K., Gong, M., Ramsey, J., Batmanghelich, K., Spirtes, P., & Glymour, C. (2017). Causal discovery in the presence of measurement error: Identifiability conditions. arXiv preprint arXiv:1706.03768.