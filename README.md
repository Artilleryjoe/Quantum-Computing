# Quantum Computing Research

This repository collects hands-on notes and experiment designs exploring core ideas in quantum computing and quantum-safe cryptography. Each folder contains standalone write-ups so you can jump directly to the concept you want to explore.

## Getting started

1. Clone the repository.
2. Create a Python 3.10+ virtual environment.
3. Install the base dependency with `pip install qiskit`.
4. Review any folder-specific requirements (for example, `Quantum_Machine_Learning/requirements.txt`).

## Repository structure

| Folder | Focus |
| --- | --- |
| [`bb84-protocol/`](./bb84-protocol) | BB84 quantum key distribution notes, including adaptive noise experiments. |
| [`grovers-search/`](./grovers-search) | Grover's algorithm overview and robust-oracle experiment notes. |
| [`post-quantum-crypto/`](./post-quantum-crypto) | Quantum-safe cryptography threat modeling and hybrid benchmark ideas. |
| [`quantum-error-correction/`](./quantum-error-correction) | Summaries of error models and small quantum error-correcting codes. |
| [`shors-algorithm/`](./shors-algorithm) | Shor's algorithm background and fault-tolerant scaling experiments. |
| [`Quantum_Machine_Learning/`](./Quantum_Machine_Learning) | Dependency list for planned QML experiments. |
| [`experiments/`](./experiments) | Central collection of experiment notes referenced by the topic folders. |

## Goals

- Deepen understanding of quantum algorithms and their cryptographic impact.
- Develop practical quantum programming skills with Qiskit and related tooling.
- Share approachable, reproducible experiments for fellow learners.

---

*Contributions, suggestions, and discussions are always welcome!*
