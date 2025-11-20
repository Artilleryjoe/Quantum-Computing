# QRAM-backed Grover Toy Search

This experiment chains a simulated QRAM lookup into a Grover-style search. The address register is placed in superposition, QRAM loads a classical data bit for every address, the oracle phases the addresses whose data matches the target pattern, and a diffuser amplifies those marked addresses.

## Setup

1. Install dependencies (Qiskit):
   ```bash
   pip install "qiskit>=2.0"
   ```
2. Run the toy search:
   ```bash
   python experiments/qram_grover_search/toy_qram_grover.py
   ```

The script saves circuit diagrams and a measurement histogram to `experiments/qram_grover_search/figures/` and prints simple resource counts for QRAM, the oracle, and one Grover iteration.

## What the script demonstrates

- **QRAM lookup** – a unitary gate implementing \(\sum_i \alpha_i |i\rangle|0\rangle \to \sum_i \alpha_i |i\rangle|d_i\rangle\) for the classical memory `d = [1, 0, 1, 0]`.
- **Oracle structure** – QRAM load → phase flip when `data == 1` → QRAM uncompute, leaving the address register clean for amplitude amplification.
- **Grover iteration** – the oracle followed by the two-qubit diffuser `H·X·CZ·X·H` on the address register.
- **Amplitude amplification** – after one iteration the addresses with `data = 1` (`00` and `10`) dominate the measurement distribution.

## Files produced

- `figures/qram_gate.txt` – the QRAM read circuit (text drawer).
- `figures/oracle.txt` – QRAM + phase + QRAM†.
- `figures/diffuser.txt` – two-qubit diffuser.
- `figures/grover_iteration.txt` – one Grover iteration with measurements.
- `figures/measurement_histogram.txt` – histogram showing amplified addresses.

This gives a small, end-to-end narrative for how QRAM would plug into Grover search if physical QRAM hardware existed.
