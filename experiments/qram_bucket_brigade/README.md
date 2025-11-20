# Bucket-Brigade QRAM Simulation (2-qubit address)

This experiment sketches a small, explicit "bucket-brigade" QRAM read using Qiskit. It treats two address qubits and a single data qubit as a four-cell classical memory and shows how to map a superposition of addresses to the corresponding entangled address–data state.

## Problem instance
- Address register: two qubits labeled `a0` (MSB) and `a1` (LSB).
- Data register: one qubit `d`.
- Classical contents: `d = [0, 1, 1, 0]`, meaning `00 → 0`, `01 → 1`, `10 → 1`, `11 → 0`.
- Ideal map:

  $$
  \sum_i \alpha_i\,|i\rangle_A \otimes |0\rangle_D \longmapsto \sum_i \alpha_i\,|i\rangle_A \otimes |d_i\rangle_D
  $$

## Bucket-brigade interpretation
Real bucket-brigade QRAM stores the address path through a binary tree of switches. With only two address qubits, that tree would have a single root (steered by `a0`) and two children (steered by `a1`). Here we compress the same control logic into multi-controlled X gates: for each address whose classical content is 1 we apply an `mcx` to the data qubit, controlling on the address qubits being in that computational basis state. Zero-controls are emulated with temporary X gates, mirroring how the tree would open the correct branch for a specific address.

## What is in the notebook
- Helper to prepare a chosen basis address.
- `apply_qram_read` that adds multi-controlled X gates for every address with `d[i] = 1`.
- Basis-state checks confirming the correct data bit is loaded.
- Superposition experiment producing the entangled address–data state.
- Resource estimation using `transpile(qc)` to report depth and gate counts for the three-qubit circuit.

## Running the experiment
1. Ensure `qiskit>=2.0.0` is installed (install with `pip install "qiskit>=2.0.0"`).
2. Open `qram_bucket_brigade.ipynb` and run the cells. The transpilation cell prints gate counts and circuit depth for this two-address QRAM read. You can adjust `d` or extend to three address qubits to explore scaling.

Figures can be saved to `experiments/qram_bucket_brigade/figures/` if you render the circuit diagram with the MPL drawer.
