# Day 2 GitHub Workflow

## Main Goal

Day 2 extends the Day 1 lattice model into controlled defect configuration experiments.

Instead of using only randomly placed defects, Day 2 studies how the following factors affect localization and the transport descriptor:

- number of defects,
- defect strength,
- defect arrangement.

## Scientific Question

How sensitive are localization and transport descriptors to hydrogen defect configurations?

In simpler language:

Do electrons become more localized when we add more defects, stronger defects, or more clustered defects?

## Connection with Day 1

Day 1 created the first pipeline:

```text
clean lattice
-> hydrogen-like defects
-> energy spectrum
-> IPR localization
-> transport descriptor
-> first dataset
```

Day 2 makes the experiment more controlled:

```text
defect configuration
-> clean versus defected spectrum
-> spectral shift
-> localization change
-> transport descriptor change
-> Day 2 dataset
```

## Day 2 Files to Put on GitHub

```text
docs/DAY_2_GITHUB_WORKFLOW.md
docs/DAY_2_PROJECT_NOTE.md
notebooks/02_defect_configuration_analysis.ipynb
data/day2_defect_configuration_dataset.csv
figures/clean_vs_defected_spectrum_day2.png
figures/spectral_shift_day2.png
figures/defect_number_vs_mean_ipr_day2.png
figures/defect_number_vs_transport_day2.png
figures/defect_strength_vs_mean_ipr_day2.png
figures/defect_strength_vs_transport_day2.png
figures/arrangement_vs_mean_ipr_day2.png
figures/arrangement_vs_transport_day2.png
```

## Notebook Structure

The Day 2 notebook should contain:

1. Scientific motivation
2. Imports
3. Day 1 helper functions
4. Controlled defect site function
5. Hamiltonian analysis function
6. Clean versus defected spectrum comparison
7. Spectral shift visualization
8. Defect number sweep
9. Defect strength sweep
10. Random, clustered, and spread arrangement comparison
11. Day 2 dataset generation
12. Dataset saving
13. Day 2 conclusion

## Day 2 Scientific Checklist

- [ ] Create `notebooks/02_defect_configuration_analysis.ipynb`.
- [ ] Write the Day 2 scientific motivation.
- [ ] Reuse the Day 1 Hamiltonian and IPR functions.
- [ ] Create a function for controlled defect sites.
- [ ] Compare clean and defected energy spectra.
- [ ] Plot spectral shift.
- [ ] Perform a defect number sweep.
- [ ] Plot defect number versus mean IPR.
- [ ] Plot defect number versus transport score.
- [ ] Perform a defect strength sweep.
- [ ] Plot defect strength versus mean IPR.
- [ ] Plot defect strength versus transport score.
- [ ] Compare random, clustered, and spread defects.
- [ ] Generate the Day 2 dataset.
- [ ] Save `data/day2_defect_configuration_dataset.csv`.
- [ ] Write the Day 2 conclusion.

## Git Commit Message

After the Day 2 notebook, dataset, and figures are ready:

```bash
git add .
git commit -m "Day 2: analyze defect configuration effects"
```

## Main Sentence for Today

Today, I studied how defect number, defect strength, and defect arrangement affect localization and the transport descriptor.
