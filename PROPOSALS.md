# Proposal Strategy: Sašo vs Zala

## Executive Summary

You have two compelling research directions, each with different risk/reward profiles:

| Criterion | Prof. Sašo Džeroski | Prof. Zala Lenarčič |
|-----------|-------------------|-------------------|
| **Field Alignment** | AI for science, explainable ML | Non-eq quantum, driven systems |
| **Risk Level** | Lower — static physics well-understood | Medium — extends into novel territory |
| **Your ML Experience** | Very High | Medium (transferable from PhD) |
| **Your Current Results** | Perfect fit | Needs framing for non-eq angle |
| **Time-to-results** | Faster (3 weeks baseline ready) | Slower (needs extension design) |
| **Novelty** | Medium (good ML + known physics) | High (new quantum directions) |
| **PhD Background Relevance** | Indirect (ML skills) | Direct (time-dependent evolution) |

---

## Strategy 1: Prof. Sašo Džeroski (SAFER, FASTER)

### Why Sašo?

Your static defect + ML pipeline is **directly** in his wheelhouse:
- He leads research on explainable ML for science
- Your feature importance analysis, constraint satisfaction, and interpretability align perfectly
- The project is **scientifically complete** in 3 weeks
- Low risk of re-framing needed

### Email Template for Sašo

```
Subject: Explainable ML for Defect-Controlled Transport — PhD Proposal

Dear Prof. Džeroski,

I am interested in applying for a PhD position in your group studying explainable 
machine learning for materials discovery. 

My proposed work develops a computational framework for understanding how hydrogen-
induced defects control transport properties in model quantum materials. The key 
innovation is using interpretable ML (Random Forest, SHAP analysis) to extract 
physics-informed descriptors from defect geometry.

**Project Pipeline**:
1. Model hydrogen defects as local perturbations in 1D/2D tight-binding Hamiltonians
2. Compute physics descriptors: inverse participation ratio (localization), energy gap, 
   transport proxy
3. Train ML models to predict transport behavior from defect parameters
4. Use feature importance (permutation importance, SHAP) to identify which defect 
   properties most strongly control transport
5. Apply constraint satisfaction (Optuna) to optimize defect configurations for 
   high transport
6. Validate selected small Hamiltonians using Qiskit quantum simulation

**Why This Fits Your Group**:
- Explainability as a core goal (not a post-hoc add-on)
- Direct ML→physics extraction without black boxes
- Safe, falsifiable claims
- Portfolio-ready proof-of-concept in 3 weeks

**Current Status**:
I have completed the computational framework and generated 1000+ samples. I can 
provide a three-week project timeline and preliminary results.

I would be grateful to discuss this proposal at your earliest convenience.

Best regards,
Başak Ekinci
baekinci@gmail.com
```

### Key Points to Emphasize with Sašo

✅ **Do**:
- Highlight **interpretability** as the main driver
- Show feature importance plots
- Discuss constraint satisfaction (Optuna)
- Frame as "materials informatics pipeline"
- Mention SHAP, permutation importance, decision trees

❌ **Don't**:
- Over-emphasize quantum hardware (VQE, IBM Quantum)
- Talk about "driving" or "time-dependent" physics
- Claim to be a quantum physicist
- Focus on thermal transport (say "transport descriptor" instead)

### Timeline for Sašo

**Weeks 1–3**: Baseline static defect + ML complete
**Months 1–12**: Extensions could include:
- Multi-material benchmarking
- Larger datasets (5000+ samples)
- Advanced interpretability (influence functions, attention mechanisms)
- Open-source toolkit release

---

## Strategy 2: Prof. Zala Lenarčič (HIGHER RISK, HIGHER REWARD, BETTER QUANTUM FIT)

### Why Zala?

If you want to do **real quantum physics** (not just apply ML), Zala is the right choice:
- She works on **non-equilibrium many-body quantum systems**
- Your PhD background (time-dependent neutrino flavor evolution) directly transfers
- You can extend to **time-dependent driving** + **dissipation**
- Unique scientific contribution (not just "ML on static data")

### What Needs to Change for Zala

Your current project is **static**. Zala needs you to add:
- **Time-dependent Hamiltonian**: H(t) = H₀ + H_defect + A·cos(ωt)·O
- **Open quantum dynamics**: Lindblad equation with bath coupling
- **Non-equilibrium steady states**: ρ(t→∞) under driving + dissipation

### The Reframe for Zala

**Instead of**: "I use ML to predict static transport from defect descriptors"

**Say**: "I want to understand how hydrogen defects reshape localization and transport 
dynamics when the material is driven by external fields and coupled to an environment. 
I'll combine Hamiltonian evolution, open system dynamics, and neural networks to 
extract the defect→non-equilibrium transport relationship."

### Email Template for Zala

```
Subject: Defect-Induced Non-Equilibrium Localization & Transport — PhD Proposal

Dear Prof. Lenarčič,

I am interested in a PhD position in your group studying defect-engineered 
non-equilibrium quantum materials.

**Motivation**: Heat management in quantum devices hinges on understanding and 
controlling transport. Defects can either localize or enhance transport depending 
on their geometry and the system's dynamical regime.

**Proposed Research**:
I model hydrogen-induced defects in low-dimensional quantum materials and study 
how they reshape localization and transport under:

1. **Static regime** (baseline): Compute inverse participation ratio (IPR), energy 
   spectra, transport proxies; use explainable ML to identify critical defect features
   
2. **Floquet driving** (extension): Add time-periodic modulation 
   H(t) = H₀ + H_defect + A·cos(ωt)·O; investigate how driving changes localization 
   length, dynamical localization, and non-equilibrium transport coefficients
   
3. **Open system dynamics** (extension): Include bath coupling via Lindblad master 
   equation; study how phonon/photon dissipation competes with defect-driven 
   localization effects
   
4. **Scalable methods**: Tensor networks for ground state representation; neural 
   networks for non-equilibrium descriptor prediction

**Why I'm Interested in Your Group**:
- Your expertise in driven many-body systems and dissipation directly addresses the 
  physics bottlenecks
- My PhD experience with time-dependent Hamiltonian evolution (neutrino flavor mixing) 
  transfers naturally to time-dependent H(t)
- The combination of defects + driving + baths is underexplored in the literature

**Current Status**: 
I have completed a proof-of-concept static framework with ML validation. I can extend 
this toward the time-dependent and open-system extensions within a structured timeline.

I would welcome the opportunity to discuss how this project fits your research agenda.

Best regards,
Başak Ekinci
baekinci@gmail.com
```

### Key Points to Emphasize with Zala

✅ **Do**:
- Highlight **time-dependent driving**: Floquet engineering
- Mention **open quantum dynamics**: Lindblad equation, dissipation
- Emphasize **non-equilibrium steady states**
- Connect to your PhD work (time-dependent evolution)
- Show knowledge of **tensor networks** & **neural networks for quantum systems**
- Cite her papers on SQUASH, driven systems, many-body localization

❌ **Don't**:
- Oversell the "ML" part (it's a tool, not the main story)
- Claim defect control is novel without extension to driven/open systems
- Ignore the complexity of implementing time-dependent + dissipative solvers
- Make promises you can't keep about extending in month 1 (be realistic)

### Timeline for Zala

**Weeks 1–3**: Baseline static (proof you can execute)
**Weeks 4–8**: Floquet extension (time-periodic H(t), driven IPR, Floquet spectrum)
**Months 2–6**: Open system dynamics (Lindblad solver, bath models, dissipative transport)
**Months 6–12**: Scaling & optimization (tensor networks, neural-net ansätze, large systems)

---

## Which Should You Choose?

### Choose Sašo If:
✅ You want a **guaranteed publishable project** in 3 weeks  
✅ You prefer **lower risk** and faster to first results  
✅ You're genuinely interested in **explainable AI for science**  
✅ You want to focus on **ML techniques** (SHAP, feature engineering, optimization)  
✅ You prefer a **more established** research direction

### Choose Zala If:
✅ You want to do **real quantum physics**, not just apply ML  
✅ You have **genuine interest** in non-equilibrium dynamics & driven systems  
✅ You can tolerate **higher scientific risk** for higher novelty  
✅ You want to **leverage your PhD background** directly  
✅ You're excited about **extending to new territory**  
✅ You're willing to invest **months 4–8** designing + implementing new solvers  

---

## The Honest Assessment

**If forced to choose ONE:**

**Sašo is safer.** Your static model is complete, results are clean, claims are safe. 
You can submit within weeks.

**Zala is more scientifically interesting.** But requires:
- Better understanding of Floquet theory & Lindblad equations
- Implementation of time-dependent solvers (harder than static)
- More careful framing (avoid overselling)
- Longer timeline to first major results

**My recommendation**: 
- Finish the **Sašo version** first (3 weeks) → get it publishable
- Then pivot to **Zala's extensions** (weeks 4–8) → add the quantum physics depth
- Send **both proposals** (same project, different angles) in month 2
- Let the advisors respond → choose based on fit + enthusiasm

---

## Budget & Resources

### For Sašo (3 weeks, static):
- Laptop + Python/scikit-learn
- No special hardware needed
- Free: NumPy, Pandas, Scikit-learn, XGBoost, Optuna
- Optional: IBM Quantum free tier (for Qiskit validation)

### For Zala (3 weeks + extension):
- Same as above, plus:
- JAX (for tensor networks)
- qiskit + qiskit-dynamics (time-dependent evolution)
- TensorFlow/PyTorch (for neural networks)
- Optional: GPU for neural network training

**Budget Impact**: Minimal. All tools are open-source.

---

## References to Cite per Advisor

### For Sašo
1. Caruana, R. (2015). Intelligible models for classification and regression. *KDD Tutorial*.
2. Lundberg & Lee (2017). A unified approach to interpreting model predictions. *NeurIPS*.
3. Molnar, C. (2019). *Interpretable Machine Learning*. christophm.github.io/interpretable-ml-book/

### For Zala
1. Oka & Kitamura (2019). Floquet engineering of quantum materials. *Annu. Rev. Cond. Mat. Phys.*, 10.
2. Breuer & Petruccione (2002). *The Theory of Open Quantum Systems*. Oxford.
3. Laskin et al. (2020). Pretrained Graph Neural Networks for Few-shot Learning. *ICLR*.

---

## Contact Strategy

**Week 1**: Send initial inquiry emails to BOTH
- Sašo: Lead with "explainable ML + static defects"
- Zala: Lead with "time-dependent dynamics + defects"

**Week 2**: If responses, schedule brief Zoom calls
- Sašo: Discuss 3-week plan, publications, lab culture
- Zala: Discuss time-dependent extensions, driving protocols, dissipation models

**Week 3**: Get preliminary feedback
- Both might suggest pivots
- Use feedback to refine proposal

**Week 4+**: Resubmit refined proposals once baseline is polished

---

## Final Thought

This project is **flexible enough for both directions**. The baseline (3 weeks) stands 
on its own as a proof-of-concept. The extensions (weeks 4–8) add genuine quantum 
novelty. You're not choosing between science vs. no science—you're choosing:

- **Sašo**: Best-in-class **ML methodology** on solid physics
- **Zala**: Novel **quantum physics** informed by ML insights

Both are legitimate research. Both could lead to papers. The choice is about which 
excites you more.

---

*Document prepared: May 30, 2026*  
*Next review: After advisor feedback (Week 2–3)*
