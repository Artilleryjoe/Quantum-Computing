# Post-Quantum Cryptography Hybrid Benchmark Experiments

## Goal
Assess performance and security trade-offs of hybrid key exchange (classical + PQC) and hybrid signatures for small-enterprise settings.

## Experiment Design
1. **Hybrid Key Exchange**  
   - Combine ECDH (P-256) with Kyber-512 and Kyber-768.  
   - Measure handshake latency and bandwidth for TLS-style flows (ClientHello/ServerHello with hybrid KEM).  
   - Include a simulated post-quantum downgrade attacker that strips PQC payloads; verify detection via transcript checksums.
2. **Hybrid Signatures**  
   - Benchmark Ed25519+Dilithium2 and ECDSA(P-256)+Falcon-512 for signing and verification throughput.  
   - Vary batch sizes {1, 10, 100} to test verification parallelism overhead.  
   - Track signature sizes and total TLS certificate chain weight.
3. **Side-Channel Robustness Smoke Tests**  
   - Introduce timing noise and measure variance of key generation and decapsulation.  
   - Flag any correlation between secret-dependent branches and runtime using simple Welch’s t-tests on timing samples.

## Metrics
- Latency (ms) and bandwidth (KB) for handshake flows.  
- CPU time per operation for sign/verify and encapsulate/decapsulate.  
- Failure detection rate for PQC downgrade attack.  
- Timing side-channel test statistics (p-values) to highlight risky implementations.

## Success Criteria
- Demonstrate hybrid KEM adds <40% latency over pure ECDH for small payloads.  
- Show Dilithium2 hybrid signatures keep certificate chain growth under 10 KB.  
- Detect downgrade attempts with >99% reliability using transcript checksums.  
- Identify any statistically significant timing leakage (p < 0.01) in naive implementations.

## Implementation Notes
- Use `pqcrypto` or `liboqs` Python bindings for Kyber, Dilithium, and Falcon where available; fall back to placeholder timing mocks if unavailable.  
- Script TLS-like message flow in Python; log packet sizes and timestamps.  
- Keep raw timing samples (CSV) for reproducibility and side-channel analysis.
