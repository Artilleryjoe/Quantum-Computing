# BB84 Adaptive Noise Experiments

## Goal
Quantify how adaptive basis choices and error-reconciliation depth affect secret-key rates over realistic noisy channels, using Qiskit Aer noise models.

## Experiment Design
1. **Channel Models**  
   - Depolarizing noise with probabilities p ∈ {0.0, 0.01, 0.03, 0.05}.  
   - Amplitude damping with γ ∈ {0.0, 0.02, 0.05}.  
   - Optional eavesdropper modeled as intercept-resend with probability ε ∈ {0, 0.1, 0.2}.
2. **Adaptive Basis Bias**  
   - Start with 50/50 Z/X basis.  
   - After every 500 qubits, shift bias toward the lower-error basis observed in the previous block (e.g., 60/40, then 70/30).  
   - Track the sifting rate and quantum bit error rate (QBER) per block.
3. **Error Reconciliation Depth**  
   - Run Cascade-style parity checks with 1–4 passes; measure leakage versus final key length.  
   - Compare with a low-density parity-check (LDPC) decoder (if available) for the same syndrome budget.
4. **Privacy Amplification**  
   - Use universal hashing with different compression rates; estimate secure key length using finite-key analysis.

## Metrics
- QBER per block and cumulative.  
- Secret-key rate (bits per channel use) under finite-key assumptions.  
- Leakage from reconciliation versus final key length.  
- Detection probability of ε-level eavesdropping.

## Success Criteria
- Identify a stable basis-bias schedule that maintains QBER < 11% under depolarizing noise p ≤ 0.03.  
- Show at least 10% improvement in final key length when switching from fixed 50/50 bases to adaptive scheduling.  
- Demonstrate detection of ε ≥ 0.1 intercept-resend with >95% confidence after 5k qubits.

## Implementation Notes
- Extend `bb84_simulation.py` to accept noise-channel knobs and basis-bias schedules.  
- Use Qiskit Aer noise models (`DepolarizingError`, `AmplitudeDampingError`).  
- Log blockwise metrics to CSV for later plotting.
