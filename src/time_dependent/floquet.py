"""
Floquet Theory Module
=====================

For time-periodic Hamiltonians H(t) = H(t + T), compute:
- Floquet spectrum and quasi-energies
- Floquet eigenstates (Floquet modes)
- Time-dependent localization measures
"""

import numpy as np
from scipy import linalg
from scipy.integrate import odeint, solve_ivp


def periodic_hamiltonian(t, H0, H_defect, H_drive_amplitude, omega, phase=0):
    """
    Build a time-periodic Hamiltonian:
    
    H(t) = H0 + H_defect + A * cos(omega*t + phase) * H_drive_operator
    
    Parameters
    ----------
    t : float
        Time
    H0 : ndarray (N, N)
        Clean system Hamiltonian
    H_defect : ndarray (N, N)
        Defect perturbation
    H_drive_amplitude : float
        Driving amplitude A
    omega : float
        Driving frequency (in units of 1/time)
    phase : float, optional
        Phase offset
        
    Returns
    -------
    H : ndarray (N, N)
        Full Hamiltonian at time t
    """
    N = H0.shape[0]
    
    # Simple driving: modulate on-site potentials
    diag_modulation = np.diag(H_drive_amplitude * np.cos(omega * t + phase) * np.ones(N))
    
    return H0 + H_defect + diag_modulation


def time_evolution_rk4(psi0, H0, H_defect, H_drive_amp, omega, t_span, n_steps=1000):
    """
    Evolve initial state psi0 under time-dependent Hamiltonian using RK4.
    
    Parameters
    ----------
    psi0 : ndarray (N,)
        Initial state (wave function)
    H0, H_defect, H_drive_amp, omega : as in periodic_hamiltonian
    t_span : tuple (t_start, t_end)
        Time range
    n_steps : int
        Number of time steps
        
    Returns
    -------
    t_array : ndarray
        Time points
    psi_array : ndarray (n_steps, N)
        State at each time point
    """
    N = H0.shape[0]
    t_array = np.linspace(t_span[0], t_span[1], n_steps)
    dt = t_array[1] - t_array[0]
    psi = psi0.copy()
    psi_array = np.zeros((n_steps, N), dtype=complex)
    psi_array[0] = psi
    
    for i in range(n_steps - 1):
        t = t_array[i]
        # Get Hamiltonian at this time
        H = periodic_hamiltonian(t, H0, H_defect, H_drive_amp, omega)
        # RK4 step: psi' = -i * H * psi
        psi = rk4_step(psi, H, dt)
        psi_array[i + 1] = psi
        
    return t_array, psi_array


def rk4_step(psi, H, dt):
    """Single RK4 step for Schrödinger equation: i d|psi>/dt = H|psi>"""
    # k1 = -i H psi
    k1 = -1j * H @ psi
    # k2 = -i H (psi + dt/2 * k1)
    k2 = -1j * H @ (psi + 0.5 * dt * k1)
    # k3 = -i H (psi + dt/2 * k2)
    k3 = -1j * H @ (psi + 0.5 * dt * k2)
    # k4 = -i H (psi + dt * k3)
    k4 = -1j * H @ (psi + dt * k3)
    
    return psi + (dt / 6.0) * (k1 + 2*k2 + 2*k3 + k4)


def floquet_spectrum(H0, H_defect, H_drive_amp, omega, period=None, n_periods=10):
    """
    Compute quasi-energies (Floquet spectrum) via time evolution over one period.
    
    Method: Evolve for n_periods, extract eigenvalues of monodromy operator.
    """
    N = H0.shape[0]
    if period is None:
        period = 2 * np.pi / omega
    
    # Evolve initial basis states
    U = np.zeros((N, N), dtype=complex)
    for i in range(N):
        psi0 = np.zeros(N, dtype=complex)
        psi0[i] = 1.0
        t_array, psi_array = time_evolution_rk4(
            psi0, H0, H_defect, H_drive_amp, omega, 
            (0, n_periods * period), n_steps=1000
        )
        U[:, i] = psi_array[-1]  # Final state
    
    # Monodromy operator (Floquet) eigenvalues
    eigvals, eigvecs = linalg.eigh(U)
    quasi_energies = -1j * np.log(eigvals) / (n_periods * period)
    
    return quasi_energies, eigvecs


def time_dependent_ipr(psi_array):
    """
    Compute Inverse Participation Ratio (IPR) at each time step.
    
    IPR(t) = sum_i |psi_i(t)|^4
    
    Parameters
    ----------
    psi_array : ndarray (n_steps, N)
        Wave function at each time
        
    Returns
    -------
    ipr_array : ndarray (n_steps,)
        IPR at each time
    """
    # Normalize states
    norm = np.sum(np.abs(psi_array)**2, axis=1, keepdims=True)
    psi_norm = psi_array / np.sqrt(norm)
    
    # IPR = sum |psi_i|^4
    ipr = np.sum(np.abs(psi_norm)**4, axis=1)
    
    return ipr


def dynamical_localization_length(psi_array):
    """
    Compute localization length from spatial spread:
    
    ξ(t) = (1 / IPR(t))^0.5
    
    Returns
    -------
    xi_array : ndarray (n_steps,)
        Localization length at each time
    """
    ipr = time_dependent_ipr(psi_array)
    return 1.0 / np.sqrt(ipr + 1e-10)  # Add small epsilon to avoid division by zero


def floquet_localization_ratio(H0, H_defect, omega, static_ipr):
    """
    Compare time-averaged IPR under driving vs static case.
    
    Ratio > 1: driving enhances localization
    Ratio < 1: driving delocalizes
    """
    # This would require computing time-averaged IPR over many periods
    # Placeholder for future implementation
    pass
