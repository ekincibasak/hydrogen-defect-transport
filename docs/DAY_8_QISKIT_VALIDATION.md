# Day 8 Qiskit Validation

## Main Goal

Notebook 8 adds a Qiskit-compatible validation layer to the hydrogen-defect project.

The classical notebooks use a 40-site tight-binding Hamiltonian. Notebook 8 does not run that full model on quantum hardware. Instead, it defines a small representative two-qubit defect Hamiltonian inspired by the same defect idea.

## Notebook File

```text
notebooks/08_qiskit_validation_of_small_defect_hamiltonians.ipynb
```

## Scientific Framing

Correct claim:

```text
We evaluate selected small defect Hamiltonians inspired by the tight-binding model using Qiskit-compatible quantum workflows.
```

Incorrect claim:

```text
We simulate the full 40-site hydrogen-defect material on IBM quantum hardware.
```

## Small Qubit Hamiltonian

The representative Hamiltonian is:

```text
H = (a + V_defect) Z0 + b Z1 + c X0 X1 + d Y0 Y1
```

where:

- `Z0` and `Z1` are local on-site-energy-like terms,
- `X0 X1` and `Y0 Y1` are coupling terms,
- `V_defect Z0` is the defect-like perturbation.

## Main Outputs

```text
results/notebook8_qiskit_validation_results.csv
figures/notebook8_energy_comparison.png
figures/notebook8_error_comparison.png
figures/notebook8_ansatz_circuit.png
```

## Methods

- Exact classical diagonalization
- Qiskit statevector expectation for a fixed ansatz
- Simple VQE-style variational minimization

## Interpretation

This notebook is a proof-of-concept NISQ validation step. It shows how a small Hamiltonian inspired by the defect model can be mapped to qubit operators and evaluated using Qiskit-compatible tools.

The result should not be interpreted as a full quantum simulation of the material.
