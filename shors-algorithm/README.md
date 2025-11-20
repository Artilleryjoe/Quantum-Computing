# Shor's Algorithm for Integer Factorization

## Overview
This folder summarizes Shor's quantum algorithm for factoring integers and explores what scaling toward fault tolerance could look like with current toolchains.

This software includes cryptographic functionality that may be subject to U.S. Export Administration Regulations (EAR). It is classified as EAR99 and released under a public open-source license. This code is intended for lawful use and research purposes only.

## What's inside
- Background notes on order finding, quantum phase estimation, and modular exponentiation.
- Fault-tolerant scaling considerations in [`shors_fault_tolerant_scaling_experiments.md`](./shors_fault_tolerant_scaling_experiments.md).

## How to use these notes
- Build small Shor circuits in Qiskit to factor toy numbers (e.g., 15 or 21) and compare simulation results to the theoretical probability distribution.
- Use the scaling write-up to identify where logical qubits, error correction, and circuit depth become bottlenecks.

## References
- [Qiskit Textbook - Shor's Algorithm](https://qiskit.org/textbook/ch-algorithms/shor.html)

---

Feel free to open issues or suggest improvements!
