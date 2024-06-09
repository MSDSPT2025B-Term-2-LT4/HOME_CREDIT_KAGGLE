### MSDS PT 2025B - Data Mining and Wrangling 1
Learning Team 4
- Co, Julie Anne
- Quiddaeon, Gianni
- Seumal, Anthony
- Allan, Tan

#### Home Credit Risk Model 

This project aims to develop a binary classification model that is trained on the dataset provided by Home Credit for the [Home Credit Risk Model Stablity competition](https://www.kaggle.com/c/home-credit-credit-risk-model-stability).


#### Reports
You may refer to the following files for the project reports:
* Project Presentation: Credit Scoring & Client Default Model Predictor.pdf
* Technical Written Report: DMW1_LT4_Technical_Report.pdf

#### Codes

Due to the large dataset, it is advised that you run the notebooks in Kaggle as you may run into insufficient RAM or compute errors.

Each phase of the development process was subdivided into 7 notebooks located under the 'kaggle/' folder. Alternatively, you may also run the notebooks in Kaggle:
* <b>00_feature_engg_selection.ipynb</b> - [Kaggle version](https://www.kaggle.com/code/julieanneco/00-feature-eng-selection/notebook)
  <br>Provenance: Derived Pipeline and Aggregator classes from [Faruckan Saglam](https://www.kaggle.com/code/greysky/home-credit-baseline) with edits by LT4, class Feature_Selector originally by LT4
  <br>1.  Preprocesses original dataset and aggregates features per unique case_id
  <br>2.  Eliminates variables with low useability and reduces highly correlated sets of features
  <br>3. Creates processed and reduced dataset
  <br> ----
* <b>01_model_baseline.ipynb</b> - [Kaggle version](https://www.kaggle.com/code/julieanneco/01-model-baseline-ipynb)
  <br>Provenance: All codes by LT4
  <br>1.  Checks performance of Dumb and Random Chance Classifiers
  <br> ----
* <b>02a_hypertune_catboost.ipynb</b> - [Kaggle version](https://www.kaggle.com/code/julieanneco/02a-hypertune-catboost/log)
  <br>Provenance: All codes by LT4
  <br>1.  Hypertunes CatBoost using HyperOpt - TPE
  <br> ----
* <b>02b_hypertune_lgb.ipynb</b> - [Kaggle version](https://www.kaggle.com/code/julieanneco/02b-hypertune-lgbm/log)
  <br> Provenance: All codes by LT4
  <br>1.  Hypertunes LightGBM using HyperOpt - TPE
  <br> ----
* <b>03_model_evaluation.ipynb</b> - [Kaggle version](https://www.kaggle.com/code/julieanneco/03-model-evaluation)
  <br> Provenance: All codes by LT4
  <br>1.  Checks model results of Tuned Models
  <br> ----
* <b>04_RFE_lgb.ipynb</b> - [Kaggle version](https://www.kaggle.com/code/julieanneco/04-rfe-lgb)
  <br> Provnenace: All codes by LT4
  <br>1.  Performs Recursive Feature Elimination to optimize dataset dimension
  <br> ----
* <b>05_PCA_num_cols.ipynb</b> - [Kaggle version](https://www.kaggle.com/code/julieanneco/05-pca-num-cols)
  <br> Provenance: All codes by LT4
  <br>1.  Experiment with PCA on numeric columns for changes in performance
  <br> ----
* <b>06_model_results.ipynb</b> - [Kaggle version](https://www.kaggle.com/code/julieanneco/06-model-results)
  <br> Provenance: All codes by LT4
  <br>1.  Profiling of results
  <br> ----


