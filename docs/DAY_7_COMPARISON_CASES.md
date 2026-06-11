# Day 7 Controlled Comparison Cases

## Main Goal

Notebook 7 compares representative defect configurations under controlled conditions.

The central question is:

```text
How do clean, weak-defect, strong-defect, spread-defect, clustered-defect, and random-defect configurations differ in spectrum, localization, and transport-related score?
```

## Notebook File

```text
notebooks/07_comparison_cases.ipynb
```

## Why This Notebook Matters

Notebook 6 used constrained random search, which mixes several effects:

- defect number
- defect strength
- spatial arrangement
- random sampling

Notebook 7 controls these variables by defining representative physical cases.

Most defected cases use:

```text
n_sites = 40
n_defects = 3
weak_strength = 0.5
strong_strength = 3.5
```

This makes the comparison scientifically clearer because defect density is fixed across the main defected cases.

## Main Cases

- Clean system
- Weak spread defects
- Strong spread defects
- Weak clustered defects
- Strong clustered defects
- Random defects
- Best constrained configuration from Notebook 6

## Main Outputs

```text
results/notebook7_comparison_cases.csv
results/notebook7_candidate_cases_for_qiskit.csv
figures/notebook7_energy_spectra_comparison.png
figures/notebook7_mean_ipr_comparison.png
figures/notebook7_transport_descriptor_comparison.png
```

## Scientific Interpretation

The comparison tests three questions:

```text
Does strong defect potential increase localization?
Does higher localization reduce the transport descriptor?
Does arrangement matter when defect number is fixed?
```

The results should be interpreted inside the simplified one-dimensional tight-binding model. They are controlled model comparisons, not direct claims about real materials.

## Next Notebook

Notebook 8 should select a small representative case and begin Qiskit validation by mapping a small Hamiltonian version to qubits.
