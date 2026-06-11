# Day 1 Project Note

## Project Paragraph

This project studies how hydrogen-induced defects affect localization and transport in simplified lattice systems. The first stage uses a one-dimensional tight-binding Hamiltonian where hydrogen-like defects are represented as local perturbations to on-site energies. By computing the energy spectrum, eigenvectors, inverse participation ratio, and a simple transport descriptor, the project creates a physics-informed dataset that can later be used for classical machine learning and quantum machine learning.

## Day 1 Method

1. Define a one-dimensional lattice.
2. Build the clean tight-binding Hamiltonian.
3. Add hydrogen-like defect sites.
4. Diagonalize the Hamiltonian.
5. Compute localization using inverse participation ratio.
6. Define a transport descriptor.
7. Generate many small simulations with different defect parameters.
8. Save the results as a CSV dataset.
9. Create figures for the first report and GitHub README.

## Initial Features for the Dataset

- lattice size
- number of defects
- defect positions
- defect strength
- mean energy
- energy gap descriptor
- mean inverse participation ratio
- maximum inverse participation ratio
- transport descriptor

## First Research Question

How do hydrogen-like local defects change electronic localization and simple transport behavior in a one-dimensional lattice model?
