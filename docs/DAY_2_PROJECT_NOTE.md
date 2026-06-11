# Day 2 Project Note

## Project Paragraph

Day 2 extends the hydrogen-induced defect transport project by analyzing controlled defect configurations in a one-dimensional tight-binding lattice. The goal is to compare clean and defected systems, measure spectral shifts, and study how defect number, defect strength, and spatial arrangement influence localization and a transport-related descriptor.

## Scientific Motivation

Day 1 used random defect positions to generate the first dataset. That was useful as a starting point, but it did not separate the physical effects of defect number, defect strength, and defect arrangement.

Day 2 changes one factor at a time. This makes the simulation more like a controlled experiment.

## Variables Studied

| Variable | Meaning | Expected Effect |
|---|---|---|
| Defect number | How many hydrogen-like defects are present | More defects may increase disorder and localization. |
| Defect strength | Size of the local on-site energy perturbation | Stronger defects may increase spectral shifts and localization. |
| Defect arrangement | Spatial organization of defects | Clustered and spread defects may affect localization differently. |

## Core Equations

The defect perturbation changes the local on-site energy:

```text
epsilon_i -> epsilon_i + V_H
```

The defected Hamiltonian eigenvalue problem is:

```text
H_defected psi_n = E_n psi_n
```

The spectral shift is:

```text
Delta E_n = E_n_defected - E_n_clean
```

The inverse participation ratio is:

```text
IPR_n = sum_i |psi_n(i)|^4
```

The Day 2 transport score is:

```text
D_transport = 1 / mean(IPR)
```

## Day 2 Expected Dataset Columns

- `experiment`
- `arrangement`
- `num_defects`
- `defect_strength`
- `defect_sites`
- `mean_ipr`
- `max_ipr`
- `transport_score`

## Day 2 Conclusion Draft

In this notebook, we extended the Day 1 lattice Hamiltonian model by systematically analyzing hydrogen-induced defect configurations. We compared clean and defected spectra, measured spectral shifts, and studied how defect number, defect strength, and spatial arrangement influence localization and the transport descriptor. The results provide a more controlled physics-informed dataset for later machine learning and quantum machine learning analysis.

## Next Step

Day 3 should perform repeated experiments across multiple random seeds to test whether the Day 2 descriptors are stable or sensitive to random defect placement.
