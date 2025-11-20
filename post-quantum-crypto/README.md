# Post-Quantum Cryptography (PQC)

## Overview  
Post-Quantum Cryptography refers to cryptographic algorithms believed to be secure against attacks by quantum computers. Unlike quantum cryptography (like QKD), PQC runs on classical computers but resists quantum-enabled adversaries.

This project explores popular PQC algorithms, their principles, and basic implementations or demonstrations.

This software includes cryptographic functionality that may be subject to U.S. Export Administration Regulations (EAR). It is classified as EAR99 and released under a public open-source license. This code is intended for lawful use and research purposes only.


## Focus Areas
- **Lattice-based cryptography** (e.g., NTRU, Kyber)
- **Code-based cryptography** (e.g., McEliece)
- **Hash-based signatures** (e.g., XMSS)
- **Multivariate quadratic equations**
- **Isogeny-based cryptography**
- **Quantum-era threat modeling** for data systems that rely on encryption but leak structure or access patterns

## Why PQC?  
Quantum algorithms like Shor's threaten classical public-key schemes (RSA, ECC). PQC aims to provide secure cryptography that withstands quantum attacks.

## Requirements  
- Python 3.7+
- Cryptography libraries (depending on demos) such as `pycryptodome`, `pqcrypto` (optional)

## How to Run
- Explore included scripts and notebooks demonstrating PQC primitives.
- Install necessary libraries via pip if needed.
- Read the QRAM-era threat model for small institutions in [`qram-threat-model-rural-credit-union.md`](./qram-threat-model-rural-credit-union.md).

## References  
- [NIST Post-Quantum Cryptography Standardization](https://csrc.nist.gov/projects/post-quantum-cryptography)  
- [PQCrypto.org](https://pqcrypto.org/)  
- [Qiskit and PQC](https://qiskit.org/documentation/)

---

Contributions and feedback welcome!
