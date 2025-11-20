# Quantum Computing Research

This repository collects hands-on experiments exploring core ideas in quantum computing and quantum-safe cryptography. Each folder contains notebooks or notes for a standalone topic so you can jump directly to the concept you want to explore.

## Getting started

1. Clone the repository.
2. Create a Python 3.10+ virtual environment.
3. Install the base dependency with `pip install qiskit`.

Additional projects may include their own README files with extra requirements.

## Repository structure

| Folder | Focus |
| --- | --- |
| [`bb84-protocol/`](./bb84-protocol) | Simulating the BB84 quantum key distribution protocol and visualising raw key generation. |
| [`grovers-search/`](./grovers-search) | Implementing Grover's algorithm and discussing its impact on search and cryptanalysis. |
| [`post-quantum-crypto/`](./post-quantum-crypto) | Experimenting with lattice- and code-based cryptosystems that resist quantum attacks. |
| [`quantum-error-correction/`](./quantum-error-correction) | Studying noise models and small quantum error-correcting codes. |
| [`experiments/qram_qml_kernel/`](./experiments/qram_qml_kernel) | QRAM-loaded single-qubit quantum kernel with resource analysis for tiny QML. |
| [`shors-algorithm/`](./shors-algorithm) | Exploring Shor's factoring algorithm and its implications for public-key cryptography. |

## Goals

- Deepen understanding of quantum algorithms and their cryptographic impact.
- Develop practical quantum programming skills with Qiskit and related tooling.
- Share approachable, reproducible experiments for fellow learners.

---

*Contributions, suggestions, and discussions are always welcome!*
