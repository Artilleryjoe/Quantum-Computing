# BB84 Quantum Key Distribution Protocol Notes

## Overview
This folder captures design notes for simulating the BB84 QKD protocol with Qiskit and studying how eavesdropping or noise influences the raw key.

This software includes cryptographic functionality that may be subject to U.S. Export Administration Regulations (EAR). It is classified as EAR99 and released under a public open-source license. This code is intended for lawful use and research purposes only.

## What's inside
- Conceptual summary of BB84 bases, state preparation, and measurement.
- Experiment outline in [`bb84_adaptive_noise_experiments.md`](./bb84_adaptive_noise_experiments.md) for testing adaptive noise levels and monitoring error rates.

## How to use these notes
- Install Qiskit with `pip install qiskit`.
- Translate the experiment steps into circuits in a notebook or script, then run them on a simulator to compare error rates with and without an eavesdropper.
- Use the observations to iterate on basis selection, error correction, or privacy amplification ideas.

## References
- [BB84 Protocol Wikipedia](https://en.wikipedia.org/wiki/BB84)
- [Qiskit Textbook Chapter on QKD](https://qiskit.org/textbook/ch-algorithms/quantum-key-distribution.html)
- [NIST Post-Quantum Cryptography](https://csrc.nist.gov/projects/post-quantum-cryptography)

---

Feel free to open issues or suggest improvements!
