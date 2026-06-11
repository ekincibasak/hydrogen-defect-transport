# Day 4 Machine Learning Prediction

## Main Goal

Notebook 4 trains machine-learning regression models to predict the transport-related descriptor from the machine-learning-ready dataset generated in Notebook 3.

The target is:

```text
transport_descriptor = 1 / (1 + mean_ipr + defect_density)
```

Because this target is explicitly defined using `mean_ipr` and `defect_density`, Notebook 4 uses two different experiments.

## Experiment 4A: Full-Feature Surrogate Model

The full-feature model includes variables that directly define the target:

- `mean_ipr`
- `defect_density`

This experiment tests whether machine learning can reproduce the designed physics-informed transport proxy. It is a surrogate-modeling baseline, not a discovery of a new physical law.

## Experiment 4B: Reduced-Feature Prediction Model

The reduced-feature model removes:

- `mean_ipr`
- `defect_density`

This makes the task harder and scientifically more meaningful. The model must predict the transport proxy from indirect descriptors such as defect strength, defect spacing, clustering, spectral bandwidth, and maximum localization.

## Notebook File

```text
notebooks/04_ml_prediction.ipynb
```

## Input Dataset

```text
data/hydrogen_defect_dataset.csv
```

## Main Outputs

```text
results/notebook4_model_comparison.csv
figures/notebook4_actual_vs_predicted.png
figures/notebook4_feature_importance_full.png
figures/notebook4_feature_importance_reduced.png
```

## Models

- Random Forest Regressor
- Gradient Boosting Regressor
- XGBoost Regressor, if installed

## Metrics

- MAE
- RMSE
- R2

## Main Scientific Message

We do not claim that machine learning discovers a new physical law. Instead, we test whether machine-learning models can reproduce a designed physics-informed transport proxy and whether the same proxy can be predicted from indirect defect and spectral descriptors.

## Main Sentence

The full-feature model tests whether machine learning can reproduce the designed transport proxy, while the reduced-feature model tests whether indirect physical descriptors carry predictive information.
