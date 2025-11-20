# QRAM-loaded Quantum Kernel (Tiny QML Pipeline)

This micro-experiment shows a complete QRAM→quantum-kernel→classifier workflow using the smallest possible dataset: two training points stored in a simulated QRAM. The goal is to highlight how data loading dominates resource costs even when the downstream model is trivial.

## Dataset (Phase 0)
- Training addresses: `00 → x0 = 0.2 (label 0)`, `01 → x1 = 0.8 (label 1)`
- Rotation encoding: \(\theta_i = \pi x_i\) gives `θ0 = 0.6283 rad`, `θ1 = 2.5133 rad`.

| Address | Feature | Label | Rotation \(\theta = \pi x\) |
| --- | --- | --- | --- |
| `0` | 0.2 | 0 | 0.6283 |
| `1` | 0.8 | 1 | 2.5133 |

## QRAM-style data loading (Phase 1)
A one-qubit address controls a rotation on the data qubit (rotation encoding option A):

```
|i⟩|0⟩ ──► |i⟩ Ry(θ_i)|0⟩
```

For two addresses the circuit uses two `CRY` gates plus an `X` sandwich to target the `|0⟩` branch. Resource snapshot (depth counts sequential gates):

| Metric | Value | Notes |
| --- | --- | --- |
| X gates | 2 | toggles for the `|0⟩` branch |
| Controlled RY | 2 | one per address value |
| Depth | 4 | `X → CRY → X → CRY` |
| Gate count (size) | 4 | ignores uncomputation overhead |

## Quantum kernel via QRAM calls (Phases 2–4)
Each QRAM call produces \(|\psi_i\rangle = Ry(\theta_i)|0\rangle\). The kernel value \(K(i,j) = |\langle\psi_i|\psi_j\rangle|^2 = \cos^2\big((\theta_i-\theta_j)/2\big)\) is calculated for all address pairs.

Kernel matrix from `qram_qml_kernel.py`:

|  | x0 | x1 |
| --- | --- | --- |
| **x0** | 1.000000 | 0.345492 |
| **x1** | 0.345492 | 1.000000 |

Simple classifier: a test point `x_test = 0.6` is labeled by whichever training state has higher fidelity (`label 1` wins here).

## Bottleneck analysis (Phase 5)
- **Data loading dominates:** building the 2×2 kernel needs 4 entries × 2 QRAM loads each = 8 QRAM calls; adding uncomputation doubles that to 16.
- **Model cost is tiny:** fidelity evaluation is a closed-form cosine here, but even with a quantum SWAP test it would add only one ancilla and a few two-qubit gates per comparison.
- **Scaling:**
  - QRAM storage/lookups scale like \(O(N \log N)\) switches.
  - Kernel estimation scales like \(O(N^2)\) state preparations; with uncomputation you pay \(2N^2\) QRAM invocations.
  - For modest \(N\), QRAM depth/width is the clear bottleneck compared to the single-qubit model.

## How to run
The script is dependency-free and prints the full workflow plus a CSV copy of the kernel matrix.

```bash
python experiments/qram_qml_kernel/qram_qml_kernel.py
```

## Optional extensions (Phase 7)
- Add a second data qubit to encode two features with back-to-back `CRY` blocks.
- Replace the analytic fidelity with a SWAP test circuit to measure overlap on a simulator.
- Expand addresses to four training points (`math.log2(4) = 2` address qubits) and observe the \(O(N^2)\) QRAM call growth.
