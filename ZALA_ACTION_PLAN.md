# Action Plan: Pivot to Zala Lenarčič Direction

## The Situation
You have completed a **3-week baseline** project with:
- Static hydrogen-defect tight-binding Hamiltonians ✓
- Machine learning on defect descriptors ✓
- Qiskit validation ✓

**Goal**: Extend this toward **non-equilibrium quantum dynamics** to align with **Prof. Zala Lenarčič's research** (driven systems, dissipation, many-body localization).

---

## What to Add for Zala

### Week 4: Floquet Driving (Time-Periodic Modulation)

**Physics Goal**: Add H(t) = H₀ + H_defect + A·cos(ωt)·O

**What You Need**:
1. ✅ **Module**: `src/time_dependent/floquet.py` (Already scaffolded)
   - `periodic_hamiltonian()`: Build H(t)
   - `time_evolution_rk4()`: Evolve under time-dependent H
   - `floquet_spectrum()`: Quasi-energies via monodromy operator
   - `time_dependent_ipr()`: Localization under driving
   - `dynamical_localization_length()`: ξ(t)

2. **Notebook**: `notebooks/10_floquet_extension.ipynb`
   - Build time-periodic H(t)
   - Compare IPR: static vs driven
   - Plot Floquet spectrum
   - Compute dynamical localization

**Key Question**: Does driving enhance or suppress defect-localization effects?

**Expected Result**: Figures showing:
- IPR(t) evolution
- Floquet eigenvalue spectrum
- Localization length ξ(t) vs defect strength

---

### Week 5: Open Quantum Systems (Bath Coupling)

**Physics Goal**: Add Lindblad dissipation to driven system
dρ/dt = -i[H(t), ρ] + Σ_k (L_k ρ L_k† - 1/2 {L_k† L_k, ρ})

**What You Need**:
1. ✅ **Module**: `src/open_systems/lindblad.py` (Already scaffolded)
   - `lindblad_rhs()`: Master equation right-hand side
   - `solve_lindblad()`: Time-evolve density matrix
   - `ohmic_bath_coupling()`: Phonon/photon bath model
   - `dephasing_channel()`: Pure dephasing
   - `dissipative_ipr()`: Localization with dissipation
   - `steady_state()`: Non-equilibrium steady states

2. **Notebook**: `notebooks/20_open_systems_intro.ipynb`
   - Build Lindblad jump operators
   - Compare: closed vs open dynamics
   - Compute dissipative IPR
   - Find and analyze steady states

3. **Notebook**: `notebooks/21_bath_coupling.ipynb`
   - Temperature dependence
   - Decay rates vs localization
   - Energy dissipation into bath

**Key Question**: How does dissipation compete with defect localization?

**Expected Result**:
- Density matrix evolution plots
- Dissipative IPR vs time
- Steady-state properties vs temperature
- Non-equilibrium transport coefficients

---

### Week 6–8: Neural Networks + Tensor Networks

**Goal**: Scale to larger systems using learned ansätze

1. ✅ **Module**: `src/neural_nets/defect_encoder.py`
   - Graph neural network for defect geometry
   - Predicts non-eq transport from defect pattern

2. **Module**: `src/neural_nets/tensor_network.py`
   - Tensor network ansatz for wave functions
   - Parametric representation for large N

3. **Notebook**: `notebooks/30_neural_networks.ipynb`
   - Train GNN on static + driven data
   - Generalize to new defect patterns

4. **Notebook**: `notebooks/31_tensor_networks.ipynb`
   - Tensor network variational methods
   - Ground state + dynamics

---

## How to Implement

### Step 1: Understand the Physics (Days 1–2)

**Read these papers** (with focus on methodology, not just results):

1. **Floquet Engineering**:
   - Oka & Kitamura (2019), Annu. Rev. Condens. Matter Phys. 10: 387–413
   - ["Floquet engineering" your way through quantum materials]

2. **Open Systems**:
   - Breuer & Petruccione (2002), *The Theory of Open Quantum Systems*, Ch. 3–4
   - Lindblad (1976), Commun. Math. Phys. 48: 119–130

3. **Non-Equilibrium Many-Body**:
   - Look up 2–3 recent papers from **Zala's group** (SQUASH papers)
   - See how they combine driving + dissipation in many-body systems

### Step 2: Implement Core Modules (Days 3–5)

**Floquet Module**:
```python
# Example usage
H0 = build_clean_hamiltonian(N=20)
H_def = build_defect_hamiltonian(...)
H_drive_amp = 0.5
omega = 0.1

# Evolve
t_array, psi_array = floquet.time_evolution_rk4(
    psi0, H0, H_def, H_drive_amp, omega, (0, 100), n_steps=1000
)

# Measure
ipr = floquet.time_dependent_ipr(psi_array)
xi = floquet.dynamical_localization_length(psi_array)
```

**Lindblad Module**:
```python
# Define dissipation
L_ops = lindblad.ohmic_bath_coupling(N=20, coupling_strength=0.1, T=0.5)
L_ops += lindblad.dephasing_channel(N=20, dephasing_rate=0.05)

# Solve master equation
rho_array = lindblad.solve_lindblad(rho0, H, L_ops, t_eval)

# Find steady state
rho_ss = lindblad.steady_state(H, L_ops)
```

### Step 3: Create Notebooks (Days 6–10)

**notebook/10_floquet_extension.ipynb**:
```
1. Build time-periodic H(t)
2. Evolve 10 different defect configs under driving
3. Compare static vs driven IPR
4. Plot: IPR(t) for weak/strong driving
5. Interpretation
```

**notebook/20_open_systems_intro.ipynb**:
```
1. Build Lindblad operators
2. Solve closed system (no dissipation)
3. Solve open system (with bath)
4. Compare: dissipation effects
5. Plot: ρ(t), dissipative IPR, steady states
```

**notebook/21_bath_coupling.ipynb**:
```
1. Vary temperature T
2. Vary coupling strength g
3. Measure transport vs dissipation
4. Steady-state analysis
```

### Step 4: Test & Validate (Days 11–14)

For each notebook:
- ✅ Code runs without errors
- ✅ Physics makes sense (limits, limits, limits)
- ✅ Figures are publication-quality
- ✅ Writing explains methodology

**Sanity Checks**:
- Zero coupling → recovers unitary evolution
- High dissipation → exponential decay to zero/steady state
- Temperature effects reasonable
- Defect geometry affects transport as expected

---

## Timeline: Weeks 4–8

| Week | Module | Notebook | Output |
|------|--------|----------|--------|
| 4 | `floquet.py` | 10, 11, 12 | Floquet IPR, spectrum |
| 5 | `lindblad.py` | 20, 21, 22 | Dissipative transport, NESS |
| 6 | GNN encoder | 30 | Defect geometry→transport NN |
| 7 | Tensor network | 31 | Scaled solution methods |
| 8 | Integration | Full paper extension | Zala-ready manuscript |

---

## Key Talking Points for Zala

### What Your Project Shows
✅ You understand **static defect physics**  
✅ You can implement **time-dependent evolution** (from PhD)  
✅ You grasp **open quantum systems** (dissipation, steady states)  
✅ You can deploy **machine learning** (not as the main story, but as a tool)  

### What You're Asking Zala
"Prof. Lenarčič, I want to understand how defect engineering reshapes localization and transport when materials are driven by external fields and coupled to dissipative environments. This bridges my materials informatics skills with quantum many-body physics. Can I work with your group to develop this direction?"

### Why This Fits Her Lab
- **Driving**: Core to her Floquet engineering work
- **Dissipation**: Central to non-equilibrium many-body systems
- **Many-body localization (MBL)**: Defects + disorder + driving create rich physics
- **Numerical methods**: Exact diagonalization → tensor networks → neural networks
- **Interpretability**: Your ML background helps extract physics from simulations

---

## Git Workflow

```bash
# Initialize repository
cd hydrogen-defect-transport
git init
git add README.md PROPOSALS.md ZALA_ACTION_PLAN.md requirements.txt setup.py src/ notebooks/
git commit -m "Initial: baseline + Zala extension scaffolding"

# Create branches for each week
git checkout -b week-4-floquet
# ... implement & commit ...

git checkout -b week-5-lindblad
# ... implement & commit ...

# Final: merge to main
git checkout main
git merge week-4-floquet
git merge week-5-lindblad
```

---

## What Success Looks Like

By end of Week 8:

✅ **Code**: 
- All modules working
- 8+ well-tested notebooks
- Publication-ready figures

✅ **Physics**:
- Clear story: defect + driving + dissipation → new transport regimes
- Quantitative results: IPR, localization, transport vs parameters
- Interpretation: why does this matter?

✅ **Proposal**:
- Email to Zala with concrete timeline
- Early manuscript draft
- GitHub repo ready for collaboration

✅ **Publication Path**:
- First-author paper: "Defect-Engineered Non-Equilibrium Transport..."
- Target journals: PRL, PRB, or similar

---

## Do's and Don'ts

### ✅ Do
- **Start small**: N=20 chains for weeks 4–5
- **Validate against limits**: Check known physics first
- **Write as you go**: Document assumptions, not just results
- **Share early**: GitHub commits + push to backup
- **Cite extensively**: Zala's papers + classics

### ❌ Don't
- Over-claim: "We designed a material" (you didn't, it's a model)
- Rush numerics: Test each piece before combining
- Ignore dissipation: It's the whole point for Zala
- Forget interpretation: Figures alone don't tell the story
- Ignore your PhD background: Time-dependent evolution is your superpower here

---

## Resources

### Code Templates
- See `src/time_dependent/floquet.py` (ready to use)
- See `src/open_systems/lindblad.py` (ready to use)

### Papers to Reference
- Oka & Kitamura (2019) on Floquet
- Breuer & Petruccione (2002) on open systems
- Zala's recent papers on non-equilibrium many-body
- Anderson (1958) on localization (classic)

### Code Libraries
- **JAX**: Tensor networks, autodiff
- **Qiskit**: Quantum simulation
- **SciPy**: ODE solvers (used in Lindblad)
- **TensorFlow**: Neural networks

---

**Next Step**: After reading this plan and the two theory papers, start with Week 4 (Floquet). You'll spend ~2 days implementing, ~3 days testing, ~2 days writing.

Good luck! 🚀

---

*Plan created: May 30, 2026*
