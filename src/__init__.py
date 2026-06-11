"""
Hydrogen Defect Transport Framework
===================================

A hybrid quantum-classical framework for studying hydrogen-induced defects 
in model quantum materials under static, Floquet-driven, and open-system dynamics.

Modules:
- lattice: Clean and defect Hamiltonians
- defects: Defect insertion logic
- descriptors: Physics-informed descriptors (IPR, transport)
- ml_models: Machine learning models
- qiskit_validation: Quantum validation
- time_dependent: Floquet driving and time-evolution
- open_systems: Lindblad master equation solver
- neural_nets: Neural network approaches
"""

__version__ = "0.1.0"
__author__ = "Başak Ekinci"

from . import lattice, defects, descriptors, ml_models, qiskit_validation

__all__ = [
    'lattice',
    'defects', 
    'descriptors',
    'ml_models',
    'qiskit_validation',
]
