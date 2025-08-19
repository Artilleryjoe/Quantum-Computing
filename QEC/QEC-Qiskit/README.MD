# Your First Step to Quantum Resilience: QEC with Qiskit Explained
*Kristopher McCoy – August 16, 2025*

## Introduction
Quantum Error Correction (QEC) protects quantum information from errors caused by noise, decoherence, and imperfect hardware. Even without a physics background, you can experiment with QEC using Python and Qiskit to understand how logical qubits gain resilience.

## Quick Glossary (abridged)
- **Qubit**: Quantum version of a bit; can be in superposition.
- **Logical Qubit**: Protected qubit encoded across multiple physical qubits.
- **Ancilla Qubit**: Auxiliary qubit for measuring syndromes without disturbing data.
- **Bit-Flip Error**: Qubit flips between |0⟩ and |1⟩.
- **Syndrome**: Information revealing where an error occurred.
- **Qiskit**: IBM’s open-source framework for building and simulating quantum circuits.

## The 3-Qubit Repetition Code
To detect and correct a single bit-flip:

- Start with one data qubit.
- Spread its state across two more qubits via entanglement.
- Use ancilla qubits to check parity between pairs.
- Decode with a majority vote.

## Minimal Python Setup
```bash
python3 -m venv qiskit-env
source qiskit-env/bin/activate
pip install --upgrade qiskit qiskit-aer matplotlib
```

## Core Circuit (Qiskit)
```python
from qiskit import QuantumCircuit

qc = QuantumCircuit(5, 5)  # 3 data + 2 ancilla + 5 classical bits
qc.cx(0, 1); qc.cx(0, 2)   # encode logical qubit
qc.cx(0, 3); qc.cx(1, 3)   # ancilla 1 checks q0 vs q1
qc.cx(1, 4); qc.cx(2, 4)   # ancilla 2 checks q1 vs q2
qc.measure([0,1,2,3,4], [0,1,2,3,4])
```

## Adding Noise & Simulation
```python
from qiskit_aer.noise import NoiseModel, pauli_error
from qiskit_aer import AerSimulator

noise_model = NoiseModel()
p_error = 0.05
noise_model.add_all_qubit_quantum_error(
    pauli_error([('X', p_error), ('I', 1 - p_error)]), 'id'
)

backend = AerSimulator(noise_model=noise_model)
result = backend.run(qc, shots=4096).result()
counts = result.get_counts()
```

Majority‑vote decoding determines the logical error rate. A plot of error rates versus physical error probability shows when the encoded qubit outperforms an unencoded one.

## Why It Matters for Cybersecurity
Fault-tolerant quantum machines require QEC, delaying the threat to current cryptography until large, stable quantum computers exist. Exploring QEC helps cybersecurity professionals gauge quantum readiness and underscores the importance of proactive adoption of Post‑Quantum Cryptography.

