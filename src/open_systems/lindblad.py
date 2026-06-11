"""
Open Quantum Systems Module
============================

Lindblad Master Equation Solver for open quantum systems coupled to baths.

Master equation: dρ/dt = -i[H(t), ρ] + Σ_k (L_k ρ L_k† - 1/2 {L_k† L_k, ρ})

where:
- ρ is the density matrix
- H(t) is the system Hamiltonian
- L_k are Lindblad jump operators (dissipation channels)
"""

import numpy as np
from scipy import linalg
from scipy.integrate import odeint


def lindblad_rhs(rho_vec, t, H, L_ops):
    """
    Compute right-hand side of Lindblad master equation.
    
    Parameters
    ----------
    rho_vec : ndarray (N**2,)
        Density matrix as vector (column-major order)
    t : float
        Time
    H : ndarray (N, N) or callable
        System Hamiltonian (static or H(t))
    L_ops : list of ndarray (N, N)
        Lindblad jump operators
        
    Returns
    -------
    drho_dt_vec : ndarray (N**2,)
        Time derivative of ρ as vector
    """
    N = int(np.sqrt(len(rho_vec)))
    rho = rho_vec.reshape((N, N))
    
    # Get Hamiltonian at time t (handle both static and time-dependent)
    if callable(H):
        H_t = H(t)
    else:
        H_t = H
    
    # Coherent evolution: -i[H, ρ]
    drho = -1j * (H_t @ rho - rho @ H_t)
    
    # Dissipation: Σ_k (L_k ρ L_k† - 1/2 {L_k† L_k, ρ})
    for L in L_ops:
        L_dag = L.conj().T
        # L ρ L†
        term1 = L @ rho @ L_dag
        # 1/2 {L† L, ρ} = 1/2 (L† L ρ + ρ L† L)
        L_dag_L = L_dag @ L
        term2 = 0.5 * (L_dag_L @ rho + rho @ L_dag_L)
        
        drho += term1 - term2
    
    # Vectorize back
    return drho.reshape(-1)


def solve_lindblad(rho0, H, L_ops, t_eval):
    """
    Solve Lindblad master equation on time grid.
    
    Parameters
    ----------
    rho0 : ndarray (N, N)
        Initial density matrix
    H : ndarray (N, N) or callable
        Hamiltonian
    L_ops : list of ndarray
        Lindblad operators
    t_eval : ndarray
        Time points
        
    Returns
    -------
    rho_array : ndarray (len(t_eval), N, N)
        Density matrix at each time
    """
    N = rho0.shape[0]
    rho0_vec = rho0.reshape(-1)
    
    # Solve ODE
    sol = odeint(lindblad_rhs, rho0_vec, t_eval, args=(H, L_ops), full_output=False)
    
    # Reshape back to density matrices
    rho_array = sol.reshape((len(t_eval), N, N))
    
    return rho_array


def ohmic_bath_coupling(system_size, coupling_strength, temperature=0, decay_rate=1.0):
    """
    Create simple Ohmic bath model via dissipation operators.
    
    Parameters
    ----------
    system_size : int
        Size of system (number of sites)
    coupling_strength : float
        Coupling constant g to environment
    temperature : float
        Bath temperature (kB T in units of ℏω)
    decay_rate : float
        Decay rate Γ (bandwidth of bath)
        
    Returns
    -------
    L_ops : list of ndarray
        Lindblad jump operators
    """
    L_ops = []
    
    # Decay to ground state: Γ |0><N|
    for site in range(system_size):
        # Loss operator: annihilation on site i
        c = np.zeros((system_size, system_size), dtype=complex)
        c[site, site + 1] = np.sqrt(decay_rate * coupling_strength)
        L_ops.append(c)
    
    # Thermal excitation if T > 0: Γ n_th |N-1><0|
    if temperature > 0:
        n_th = 1.0 / (np.exp(1.0 / temperature) - 1.0)
        for site in range(system_size):
            c_dag = np.zeros((system_size, system_size), dtype=complex)
            c_dag[site + 1, site] = np.sqrt(decay_rate * coupling_strength * n_th)
            L_ops.append(c_dag)
    
    return L_ops


def dephasing_channel(system_size, dephasing_rate):
    """
    Pure dephasing: Loss of coherence without energy dissipation.
    
    L = sqrt(γ) Z_i = sqrt(γ) σ_z on site i
    
    Parameters
    ----------
    system_size : int
    dephasing_rate : float
        Dephasing rate γ
        
    Returns
    -------
    L_ops : list of ndarray
        Dephasing operators
    """
    L_ops = []
    
    for site in range(system_size):
        # Pauli Z operator
        Z = np.zeros((system_size, system_size), dtype=complex)
        Z[site, site] = 1.0
        Z = np.sqrt(dephasing_rate) * Z
        L_ops.append(Z)
    
    return L_ops


def compute_observables(rho_array, observables):
    """
    Compute expectation values of observables along trajectory.
    
    Parameters
    ----------
    rho_array : ndarray (len(t_eval), N, N)
        Density matrices
    observables : dict of str: ndarray (N, N)
        Observable operators
        
    Returns
    -------
    expect_dict : dict of str: ndarray
        Expectation values at each time
    """
    expect_dict = {}
    
    for name, obs in observables.items():
        expect = np.array([np.real(np.trace(obs @ rho)) 
                          for rho in rho_array])
        expect_dict[name] = expect
    
    return expect_dict


def dissipative_ipr(rho_array):
    """
    Compute effective localization from density matrix diagonal.
    
    IPR_eff = Σ_i ρ_ii^2
    
    Parameters
    ----------
    rho_array : ndarray (len(t_eval), N, N)
        Density matrix trajectory
        
    Returns
    -------
    ipr_array : ndarray (len(t_eval),)
        Effective IPR at each time
    """
    ipr = np.array([np.sum(np.abs(np.diag(rho))**2) 
                    for rho in rho_array])
    return ipr


def steady_state(H, L_ops, tol=1e-6):
    """
    Compute steady state ρ_ss: dρ/dt = 0.
    
    Solves eigenvalue problem for left-null space of Liouvillian.
    
    Parameters
    ----------
    H : ndarray (N, N)
        Hamiltonian
    L_ops : list of ndarray
        Lindblad operators
        
    Returns
    -------
    rho_ss : ndarray (N, N)
        Steady-state density matrix
    """
    N = H.shape[0]
    
    # Build Liouvillian superoperator
    L_super = np.zeros((N**2, N**2), dtype=complex)
    
    for i in range(N):
        for j in range(N):
            ij = i * N + j
            # Coherent part: -i(H_ik δ_kj - δ_ik H_kj)
            for k in range(N):
                L_super[ij, i * N + k] -= 1j * H[i, k]
                L_super[ij, k * N + j] += 1j * H[k, j]
            
            # Dissipative part
            for L in L_ops:
                L_dag = L.conj().T
                L_dag_L = L_dag @ L
                # (L_il * L*_jk - 1/2 δ_ij L†L_lk - 1/2 L†L_il δ_jk)
                for l in range(N):
                    for k in range(N):
                        L_super[ij, l * N + k] += L[i, l] * L_dag[j, k]
                        L_super[ij, i * N + k] -= 0.5 * L_dag_L[j, k]
                        L_super[ij, l * N + j] -= 0.5 * L_dag_L[i, l]
    
    # Find null space (eigenvalue ≈ 0)
    eigvals, eigvecs = linalg.eig(L_super)
    idx = np.argmin(np.abs(eigvals))
    rho_ss_vec = np.real(eigvecs[:, idx])
    rho_ss = rho_ss_vec.reshape((N, N))
    
    # Normalize: Tr(ρ) = 1
    rho_ss /= np.trace(rho_ss)
    
    return rho_ss
