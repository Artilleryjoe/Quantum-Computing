# Post-Quantum Cryptography (PQC)

## Overview
Post-Quantum Cryptography refers to algorithms believed to be secure against attacks by quantum computers. This folder collects threat models and experiment ideas that do not require specialized hardware—everything can be explored with classical tooling while keeping quantum-era risks in mind.

This software includes cryptographic functionality that may be subject to U.S. Export Administration Regulations (EAR). It is classified as EAR99 and released under a public open-source license. This code is intended for lawful use and research purposes only.

## Focus areas
- **Lattice-based cryptography** (e.g., NTRU, Kyber)
- **Code-based cryptography** (e.g., McEliece)
- **Hash-based signatures** (e.g., XMSS)
- **Multivariate quadratic equations**
- **Isogeny-based cryptography**
- **Quantum-era threat modeling** for data systems that rely on encryption but leak structure or access patterns

## What's inside
- A QRAM-era threat model for small institutions in [`qram-threat-model-rural-credit-union.md`](./qram-threat-model-rural-credit-union.md).
- Hybrid key-establishment benchmarking ideas in [`pqc_hybrid_benchmark_experiments.md`](./pqc_hybrid_benchmark_experiments.md).

## How to use these notes
- Install any classical crypto packages you want to prototype with (for example, `pycryptodome` or NIST PQC reference implementations).
- Apply the threat-model checklist to your own systems and adapt the hybrid benchmarking steps to the libraries you prefer.

## References
- [NIST Post-Quantum Cryptography Standardization](https://csrc.nist.gov/projects/post-quantum-cryptography)
- [PQCrypto.org](https://pqcrypto.org/)
- [Qiskit and PQC](https://qiskit.org/documentation/)

---

Contributions and feedback welcome!
