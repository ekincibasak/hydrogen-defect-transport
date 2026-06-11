# Day 6 Constrained Optimization

## Main Goal

Notebook 6 searches for hydrogen-defect configurations that maximize the transport-related descriptor inside a meaningful constrained design space.

The target is:

```text
transport_descriptor = 1 / (1 + mean_ipr + defect_density)
```

Because this descriptor rewards low localization and low defect density, an unconstrained optimizer may choose a trivial configuration with almost no defects. Notebook 6 avoids that by constraining the search.

## Notebook File

```text
notebooks/06_optimization.ipynb
```

## Optimization Question

```text
Which defect configurations maximize the transport-related descriptor under realistic constraints?
```

## Constraints

```text
3 <= n_defects <= 10
0.5 <= defect_strength <= 4.0
arrangement_mode in {random, clustered, spread}
```

## Method

The first version uses constrained random search.

This is scientifically useful because it is transparent, reproducible, and easy to debug before introducing more advanced optimizers such as Optuna.

## Main Outputs

```text
results/notebook6_constrained_random_search_results.csv
results/notebook6_best_configuration.csv
figures/notebook6_transport_descriptor_distribution.png
figures/notebook6_transport_by_arrangement.png
figures/notebook6_strength_vs_transport.png
```

## Scientific Interpretation

The best configuration should be interpreted as:

```text
Within the constrained design space, this configuration gives the highest transport-related score.
```

It should not be interpreted as:

```text
This is the globally optimal real material configuration.
```

The current work is a proof-of-concept optimization in a simplified one-dimensional tight-binding model.

## Next Step

After constrained random search, the project can add Optuna optimization and compare representative defect cases such as clean, weak random, strong random, clustered, and spread configurations.
