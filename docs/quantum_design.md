# Quantum Architecture & Design

> [!IMPORTANT]
> This document logs the deterministic design choices for the Projected Quantum Kernel implementation, ensuring reproducible behavior and explicit justification for all architectural components.

## Framework & Dependencies
*   **Framework:** PennyLane (`pennylane`)
*   **Simulator:** `default.qubit` (local exact state-vector simulation)
*   **Reasoning:** PennyLane offers native autodiff and the cleanest syntax for scalable kernel matrix evaluation. `default.qubit` allows deterministic exact kernel computation before deploying finite-shot noise or real Braket QPU hardware.

## Dimensionality
*   **Number of Features:** 2 (Currently testing `['TransactionAmt', 'card1']` from the synthetic smoke-test).
*   **Number of Qubits:** 2
*   **Feature Normalization:** Standard Scaling (mean=0, std=1) followed by `arctan` or `min-max` mapping into $[-\pi, \pi]$ to prevent angle wrapping. *[DESIGN CHOICE: Pending empirical validation in Phase 15]*.

## Encoding & Circuit Topology
*   **Encoding Strategy:** `AngleEmbedding` (Rotation along X or Y axis).
*   **Entanglement:** `BasicEntanglerLayers` (CZ or CNOT rings) to provide the non-linear high-dimensional representation.
*   **Circuit Depth:** 2 Layers (to balance expressivity with NISQ hardware noise constraints).

## Kernel Evaluation
*   **Kernel Definition:** Fidelity/Overlap between quantum states: $K(x, x') = |\langle \psi(x') | \psi(x) \rangle|^2$.
*   **Shots:** Exact analytical mode (`shots=None`) for Phase 14-16 to diagnose the pure mathematical representation before injecting shot noise.

## Computational Cost Profile
*   For an escalated budget $B = 10\%$, the traffic is $N \approx 200$.
*   The kernel matrix requires $N(N+1)/2$ circuit evaluations.
*   $200 \times 201 / 2 = 20,100$ evaluations. This is trivial for `default.qubit`, allowing rapid iterative design without massive compute burn.
