# Defect-Induced Localization and Transport in 1D Tight-Binding Models

A sequential computational study of how hydrogen-like point defects reshape electronic localization and transport in one-dimensional lattice models, moving from exact diagonalization through machine learning to quantum circuit validation.

---

## Physics overview

The model is a 1D tight-binding chain of N sites. A hydrogen-like defect at site d adds a local on-site energy shift V_d, giving the Hamiltonian

```
H_ij = t(δ_{i,j+1} + δ_{i,j-1}) + Σ_{d∈D} V_d δ_{id}δ_{jd}
```

Solving `H c^(n) = E_n c^(n)` yields the eigenstates. Localization of each eigenstate is quantified by the inverse participation ratio

```
IPR_n = Σ_i |c_i^(n)|^4
```

Low IPR means the state is spread across many sites; high IPR means it is concentrated on a few. The transport descriptor is built from mean IPR and defect density ρ_D = n_defects/N:

```
T = 1 / (1 + α·<IPR>) · 1 / (1 + β·ρ_D)
```

This gives a cheap scalar proxy that decreases with both stronger localization and higher defect concentration.

For open-system extensions, the Lindblad master equation

```
dρ/dt = -i[H(t), ρ] + Σ_k ( L_k ρ L_k† - ½{L_k†L_k, ρ} )
```

and a Floquet solver for time-periodic H(t) = H(t + T) are implemented in `src/` but are not part of the baseline notebook sequence.

---

## Notebooks

Run in order. Each notebook saves outputs to `data/`, `figures/`, and `results/`.

| # | File | Content |
|---|------|---------|
| 01 | `01_lattice_model_explained_with_formulas.ipynb` | Hamiltonian construction, IPR, transport descriptor; first 200-sample dataset |
| 02 | `02_defect_configuration_analysis_explained_with_formulas.ipynb` | Defect number / strength / arrangement sweeps; clean vs. defected spectra |
| 03 | `03_dataset_generation_explained_with_formulas.ipynb` | 1000-sample dataset; adds clustering index, energy gap, mean defect distance |
| 04 | `04_ml_prediction_explained_with_formulas.ipynb` | Random Forest and XGBoost regressors; full vs. reduced feature comparison |
| 05 | `05_interpretability_and_permutation_importance_explained_with_formulas.ipynb` | Permutation importance and SHAP analysis |
| 06 | `06_optimization_explained_with_formulas.ipynb` | Constrained random search to find defect configurations that maximize T |
| 07 | `07_comparison_cases.ipynb` | Controlled weak/strong and clustered/spread cases; candidate selection for NB08 |
| 08 | `08_qiskit_validation_of_small_defect_hamiltonians.ipynb` | 2-qubit Pauli Hamiltonian; VQE-style energy minimization via Qiskit Aer |

Notebooks 01–07 are self-contained and can be run without Qiskit. Notebook 08 requires `qiskit` and `qiskit-aer`.

The annotated versions in `hydrogen_defect_explained_notebooks_with_formulas/` include step-by-step formula derivations alongside each code cell — useful if you want to follow the math in detail.

---

## Repository layout

```
.
├── notebooks/                          main notebook sequence (01–08)
├── hydrogen_defect_explained_notebooks_with_formulas/   annotated copies (01–07)
├── src/
│   ├── open_systems/
│   │   └── lindblad.py                 Lindblad master equation solver
│   └── time_dependent/
│       └── floquet.py                  Floquet quasi-energy solver
├── data/                               generated CSV datasets
├── figures/                            plots saved by notebooks
├── results/                            model metrics and result tables
├── docs/                               workflow notes
├── requirements.txt
├── environment.yml
└── setup.py
```

---

## Setup

```bash
git clone https://github.com/ekincibasak/hydrogen-defect-transport.git
cd hydrogen-defect-transport

# conda (recommended)
conda env create -f environment.yml
conda activate hydrogen-defect

# or pip
pip install -r requirements.txt

jupyter lab
```

Open `notebooks/01_lattice_model_explained_with_formulas.ipynb` and run from there.

---

## Key descriptors

| Descriptor | Definition | Role |
|-----------|-----------|------|
| `IPR_n` | Σ_i \|c_i^(n)\|^4 | Per-state localization measure |
| `mean_ipr` | (1/N) Σ_n IPR_n | Mean localization; main ML predictor |
| `energy_bandwidth` | E_max − E_min | Spectral width |
| `energy_gap` | E_1 − E_0 | Gap between two lowest eigenvalues |
| `defect_density` | n_defects / N | Defect concentration |
| `mean_defect_distance` | mean pairwise distance | Spatial spread |
| `clustering_index` | std of pairwise distances | How bunched defects are |
| `transport_descriptor` T | formula above | Target variable for ML |

---

## Results summary

Random Forest on the full 8-descriptor feature set achieves R² ≈ 0.97 on held-out samples. Permutation importance consistently ranks `mean_ipr` and `defect_density` as the two dominant predictors. The reduced model (those two features only) retains R² ≈ 0.94, confirming that the physics is captured by localization and concentration rather than the finer spatial descriptors.

The constrained optimization search (notebook 06) finds that spread, low-density configurations with moderate defect strength (V ~ 1.0–2.0) consistently score highest on T. Notebook 08 validates the energy of a representative small Hamiltonian via Qiskit statevector simulation; VQE-style minimization recovers the exact ground-state energy to within numerical tolerance.

---

## Dependencies

```
numpy >= 1.21
scipy >= 1.7
pandas >= 1.3
matplotlib >= 3.4
scikit-learn >= 1.0
xgboost >= 1.5
qiskit >= 0.43        # notebook 08 only
qiskit-aer >= 0.12    # notebook 08 only
shap >= 0.41          # optional, notebook 05
jax >= 0.3            # optional, src/time_dependent only
```

---

## References

Anderson, P.W. (1958). Absence of diffusion in certain random lattices. *Phys. Rev.* 109, 1492.

Evers, F. & Mirlin, A.D. (2008). Anderson transitions. *Rev. Mod. Phys.* 80, 1355.

Oka, T. & Kitamura, S. (2019). Floquet engineering of quantum materials. *Annu. Rev. Condens. Matter Phys.* 10, 387.

Lindblad, G. (1976). On the generators of quantum dynamical semigroups. *Commun. Math. Phys.* 48, 119.

---

## Author

Başak Ekinci — baekinci@gmail.com
