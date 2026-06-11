# Day 3 Dataset Generation

## Main Goal

Notebook 3 creates a larger machine-learning-ready dataset from random hydrogen-defect configurations.

Notebook 1 created the first lattice model. Notebook 2 studied controlled defect configurations. Notebook 3 now scales the workflow into many random simulations so that later notebooks can train machine learning models.

## Scientific Pipeline

```text
random defect configuration
-> Hamiltonian
-> eigenvalues and eigenvectors
-> energy gap
-> IPR localization
-> transport descriptor
-> ML-ready dataset
```

## Notebook File

```text
notebooks/03_dataset_generation.ipynb
```

## Main Output

```text
data/hydrogen_defect_dataset.csv
```

## Dataset Columns

- `sample_id`
- `n_sites`
- `n_defects`
- `defect_density`
- `defect_strength`
- `defect_sites`
- `mean_defect_distance`
- `clustering_index`
- `mean_energy`
- `energy_gap`
- `energy_bandwidth`
- `mean_ipr`
- `max_ipr`
- `transport_descriptor`

## Descriptor Definitions

Defect density:

```text
rho = n_defects / n_sites
```

Mean defect distance:

```text
mean distance between neighboring sorted defect sites
```

Clustering index:

```text
C = 1 / (1 + mean_defect_distance)
```

Central energy gap:

```text
Delta E = E[N/2] - E[N/2 - 1]
```

Transport descriptor:

```text
T = 1 / (1 + mean_IPR + defect_density)
```

This transport descriptor is a physics-inspired proxy, not an exact thermal conductivity or conductance calculation.

## Practical Decision

For Notebook 3, use a local computer or Google Colab. Google Cloud is not needed yet because 1000 to 3000 samples with a 40 by 40 Hamiltonian is still small.

## Next Notebook

After Notebook 3, the next file should be:

```text
notebooks/04_ml_prediction.ipynb
```

The first ML target will be:

```text
transport_descriptor
```

Useful input features:

- `n_defects`
- `defect_density`
- `defect_strength`
- `mean_defect_distance`
- `clustering_index`
- `energy_gap`
- `energy_bandwidth`
- `mean_ipr`
- `max_ipr`

## Main Sentence

Today, I generated a machine-learning-ready dataset from random hydrogen-defect configurations.
