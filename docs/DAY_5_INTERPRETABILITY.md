# Day 5 Interpretability and Permutation Importance

## Main Goal

Notebook 5 interprets the machine-learning models trained on the hydrogen-defect dataset.

The central question is:

```text
Which defect, spectral, and localization descriptors does the model rely on when predicting the transport-related score?
```

Notebook 5 does not claim physical causality. It studies model-based feature importance.

## Notebook File

```text
notebooks/05_interpretability_and_permutation_importance.ipynb
```

## Input Dataset

```text
data/hydrogen_defect_dataset.csv
```

## Main Methods

- Random Forest impurity-based feature importance
- Permutation importance on the test set
- Optional SHAP analysis, only if SHAP is installed

## Full-Feature Interpretation

The full-feature model includes:

- `defect_density`
- `mean_ipr`

These directly define the target:

```text
transport_descriptor = 1 / (1 + mean_ipr + defect_density)
```

Therefore, if the full-feature model emphasizes `defect_density` and `mean_ipr`, that is expected. It confirms that the model is reproducing the designed transport proxy.

## Reduced-Feature Interpretation

The reduced-feature model removes:

- `defect_density`
- `mean_ipr`

This makes the interpretation more scientifically interesting. In this case, important features may show which indirect descriptors contain predictive information about the transport proxy.

Useful indirect descriptors include:

- `clustering_index`
- `max_ipr`
- `mean_defect_distance`
- `energy_bandwidth`
- `energy_gap`
- `defect_strength`

## Main Outputs

```text
results/notebook5_rf_importance_full.csv
results/notebook5_rf_importance_reduced.csv
results/notebook5_permutation_importance_full.csv
results/notebook5_permutation_importance_reduced.csv
results/notebook5_importance_comparison_full.csv
results/notebook5_importance_comparison_reduced.csv
figures/notebook5_permutation_importance_full.png
figures/notebook5_permutation_importance_reduced.png
```

If SHAP is installed, the notebook may also create:

```text
figures/notebook5_shap_summary_reduced.png
```

## Scientific Message

Feature importance is model-based interpretation, not proof of physical causality.

A safe conclusion is:

```text
The interpretability analysis suggests that defect clustering, maximum localization, and spectral descriptors contain useful indirect information for predicting the designed transport-related descriptor.
```

## Next Notebook

Notebook 6 should use optimization methods to search for defect configurations that maximize the transport-related descriptor.
