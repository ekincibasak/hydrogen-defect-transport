# Day 1 GitHub Workflow

## Main Decision

For Day 1, work locally on the Mac or use Google Colab. Do not use Google Cloud yet.

Day 1 is lightweight because the goal is to create a small one-dimensional lattice model, add hydrogen-like defects, compute basic physics descriptors, and save a small dataset.

## Repository Name

Recommended name:

```text
hydrogen_defect_transport
```

Alternative names:

```text
hydrogen-defect-transport
physics-informed-defect-transport
ml-for-hydrogen-defects
quantum-defect-transport-ml
```

## Day 1 Files to Put on GitHub

```text
README.md
requirements.txt
.gitignore
docs/DAY_1_GITHUB_WORKFLOW.md
notebooks/01_lattice_model.ipynb
data/week1_hydrogen_defect_dataset.csv
figures/energy_spectrum_day1.png
figures/ipr_values_day1.png
figures/most_localized_state_day1.png
figures/defects_vs_ipr_day1.png
figures/defect_strength_vs_transport_day1.png
```

## Day 1 Scientific Checklist

- [ ] Create the project folder structure.
- [ ] Create the first notebook.
- [ ] Write the project paragraph.
- [ ] Build a clean one-dimensional Hamiltonian.
- [ ] Add hydrogen-induced defects.
- [ ] Compute eigenvalues and eigenvectors.
- [ ] Compute inverse participation ratio.
- [ ] Plot the energy spectrum.
- [ ] Plot localization values.
- [ ] Visualize the most localized eigenstate.
- [ ] Define a simple transport descriptor.
- [ ] Generate the first dataset.
- [ ] Save the dataset as CSV.
- [ ] Commit the first GitHub version.

## First Git Commands

Only run these after the Day 1 notebook, figures, and dataset are ready:

```bash
git init
git add .
git commit -m "Day 1: create lattice model and first hydrogen defect dataset"
git branch -M main
```

Then create a new GitHub repository online and connect it:

```bash
git remote add origin https://github.com/YOUR_USERNAME/hydrogen_defect_transport.git
git push -u origin main
```

Replace `YOUR_USERNAME` with your GitHub username.

## Today’s Main Sentence

Today, I built the first physics-informed lattice model and generated the first dataset for hydrogen-defect transport analysis.

Turkish:

Bugun, hidrojen kusuru tasinim analizi icin ilk fizik-temelli orgu modelini olusturdum ve ilk veri setini urettim.
