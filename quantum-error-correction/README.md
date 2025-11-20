# Quantum Error Correction (QEC)

Quantum Error Correction (QEC) is the backbone of reliable quantum computing. Unlike classical bits, qubits are fragile—they can suffer from bit flips, phase flips, and decoherence. QEC provides a way to detect and correct these errors **without collapsing the quantum state**, preserving coherence long enough for useful computation.

This software includes cryptographic functionality that may be subject to U.S. Export Administration Regulations (EAR). It is classified as EAR99 and released under a public open-source license. This code is intended for lawful use and research purposes only.

---

## Why QEC matters

- **Noise is inevitable** in any quantum system due to environmental interactions.
- Without QEC, errors accumulate quickly, rendering long computations useless.
- QEC allows for **fault-tolerant quantum computing**, enabling practical quantum advantage.

---

## Core concepts

| Concept | Description |
| --- | --- |
| **Bit Flip Error** | A qubit flips from \|0⟩ to \|1⟩ or vice versa. |
| **Phase Flip Error** | A phase shift turns \|+⟩ to \|-⟩ (and vice versa). |
| **Shor Code** | First QEC code, uses 9 qubits to correct both types of errors. |
| **Steane Code** | 7-qubit code from classical Hamming [7,4] code. |
| **Surface Code** | A scalable 2D grid of physical qubits used for topological error correction. |

---

## How to use these notes

- Implement small repetition, Steane, or surface-code snippets in Qiskit to observe how syndromes identify errors.
- For scaling considerations related to factoring, see the shared write-up in [`../experiments/shors_fault_tolerant_scaling_experiments.md`](../experiments/shors_fault_tolerant_scaling_experiments.md).
- Capture observations about logical error rates as you vary noise models or decoder assumptions.

---

## Tools & resources

- [Qiskit QEC Module](https://qiskit.org/documentation/experiments/qec/index.html)
- IBM Quantum Error Mitigation Library (`qiskit-ignis`)
- *Quantum Computation and Quantum Information* — Nielsen & Chuang (Ch. 10+)

---
