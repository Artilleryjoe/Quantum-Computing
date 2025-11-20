# Shor's Algorithm Fault-Tolerant Scaling Experiments

## Goal
Explore resource scaling and resilience when running Shor’s algorithm with error-mitigation and early abort heuristics on composite numbers beyond 15.

## Experiment Design
1. **Target Numbers and Circuits**  
   - Factor n ∈ {15, 21, 33, 35}.  
   - Use Qiskit’s modular exponentiation building blocks; tally total 1- and 2-qubit gate counts and depth.
2. **Error Mitigation Variants**  
   - Compare zero-noise extrapolation (ZNE), probabilistic error cancellation (PEC), and measurement error mitigation (M3) under depolarizing noise p ∈ {0, 0.002, 0.005}.  
   - Run each variant with 4k shots; record success probability of recovering the correct factors.
3. **Early Abort Heuristic**  
   - After each phase-estimation run, compute classical post-processing confidence.  
   - Abort further shots if two consecutive attempts yield co-prime failure results (gcd = 1) to save resources; track shot savings.
4. **Logical Encoding Stress Test (Optional)**  
   - Replace physical qubits with [[5,1,3]] code logical qubits using basic stabilizer encoding.  
   - Estimate logical depth and overhead versus physical execution.

## Metrics
- Total gate counts, circuit depth, and number of controlled-U operations.  
- Success probability of factoring each n with/without mitigation.  
- Shots saved by early abort compared to fixed-shot baselines.  
- Resource overhead for logical encoding.

## Success Criteria
- Demonstrate ≥20% shot savings on average with the early abort heuristic while maintaining factoring success within 5% of the baseline.  
- Show that ZNE or PEC improves factoring success probability by >10 percentage points when p ≥ 0.002.  
- Provide resource estimates (qubits, depth) for logical encoding that highlight feasibility gaps.

## Implementation Notes
- Extend `shors_algorithm.py` to toggle noise models, mitigation strategies, and early-abort logic.  
- Use Qiskit Aer for noise and mitigation primitives; gather raw results as JSON/CSV for analysis.  
- Visualize gate-depth growth versus target n to communicate scaling trends.
