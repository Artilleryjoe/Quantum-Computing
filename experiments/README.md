# Experiment Library

This folder centralizes experiment write-ups referenced by the topic-specific directories. Each markdown file provides a small set of hypotheses, circuit sketches, and measurement ideas that can be implemented with Qiskit simulators.

## Available experiments
- **BB84 adaptive noise**: [`bb84_adaptive_noise_experiments.md`](./bb84_adaptive_noise_experiments.md)
- **Grover's robust oracle**: [`grovers_robust_oracle_experiments.md`](./grovers_robust_oracle_experiments.md)
- **Hybrid post-quantum benchmarks**: [`pqc_hybrid_benchmark_experiments.md`](./pqc_hybrid_benchmark_experiments.md)
- **Shor's fault-tolerant scaling**: [`shors_fault_tolerant_scaling_experiments.md`](./shors_fault_tolerant_scaling_experiments.md)

## How to use these notes
1. Install Qiskit with `pip install qiskit`.
2. Recreate the described circuits in a notebook or script.
3. Compare measurement statistics against the hypotheses listed in each file.
4. Iterate on parameters (noise models, oracle design, hardware backend) and capture observations alongside the prompts.

Contributions that add new experiments or share results are welcome!
