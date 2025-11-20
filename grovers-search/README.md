# Grover's Search Algorithm Notes

## Overview
This folder outlines how to build Grover's search circuits in Qiskit and how to reason about oracle design. The emphasis is on understanding how oracle robustness affects success probability.

This software includes cryptographic functionality that may be subject to U.S. Export Administration Regulations (EAR). It is classified as EAR99 and released under a public open-source license. This code is intended for lawful use and research purposes only.

## What's inside
- Refresher on Grover's amplitude amplification.
- Robust-oracle experiment plan in [`grovers_robust_oracle_experiments.md`](./grovers_robust_oracle_experiments.md) covering multi-solution cases and noise effects.

## How to use these notes
- Install Qiskit with `pip install qiskit`.
- Implement the outlined oracles and diffuser in a notebook or script, then run simulations to track success probability across iterations.
- Compare outcomes for single- and multi-solution search spaces using the experiment prompts.

## References
- [Grover's Algorithm - Wikipedia](https://en.wikipedia.org/wiki/Grover%27s_algorithm)
- [Qiskit Textbook - Grover's Algorithm](https://qiskit.org/textbook/ch-algorithms/grover.html)

---

Feel free to open issues or suggest improvements!
