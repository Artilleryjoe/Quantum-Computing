# Grover's Search Robust Oracle Experiments

## Goal
Evaluate how Grover's quadratic speedup degrades when oracles are imperfect or when the marked item changes mid-run, simulating data drift.

## Experiment Design
1. **Imperfect Oracle Flips**  
   - Implement an oracle that flips the marked state with probability (1 − δ) and leaves it unchanged with probability δ.  
   - Sweep δ ∈ {0, 0.05, 0.1, 0.2} for search spaces N ∈ {8, 16, 64}.  
   - Measure success probability after ⌊π/4√N⌋ and after an adaptive stop rule based on sampling shots.
2. **Target Drift Mid-Run**  
   - After k Grover iterations (k ∈ {2, 4}), change the marked item to a new index.  
   - Compare performance of restarting versus continuing with a Bayesian guess of the new target.
3. **Noise-Injection Stress Test**  
   - Add depolarizing noise p ∈ {0, 0.01, 0.03}.  
   - Compare standard diffusion operator to a fixed-point (Grover α) variant to see which tolerates noise better.

## Metrics
- Success probability of measuring the (possibly drifting) marked state.  
- Number of oracle calls required to reach >80% success probability.  
- Robustness delta: drop in success probability relative to the ideal oracle.

## Success Criteria
- Identify δ thresholds where the fixed-point Grover variant outperforms the standard implementation.  
- Demonstrate that adaptive stopping rules save oracle calls when δ ≥ 0.1.  
- Show that restarting after drift yields higher success than continuing for k ≥ 4 when N ≥ 16.

## Implementation Notes
- Extend the existing Grover script to accept oracle reliability δ and noise parameters.  
- Log iteration-by-iteration success estimates and oracle call counts.  
- Use Qiskit Aer for noise modeling; plot success probability versus iterations.
