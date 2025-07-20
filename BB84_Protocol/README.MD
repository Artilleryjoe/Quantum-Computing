# BB84 Quantum Key Distribution Protocol Simulation

## Overview  
This project implements the BB84 QKD protocol using Qiskit to demonstrate how quantum mechanics enables secure key exchange.

This software includes cryptographic functionality that may be subject to U.S. Export Administration Regulations (EAR). It is classified as EAR99 and is released under a public license as open-source. This code is intended for lawful use and research only. 


## Features  
- Simulation of quantum states and bases  
- Eavesdropping scenario with error rate detection  
- Key generation and comparison  

## How to Run  
1. Install dependencies: `pip install qiskit`  
2. Run `bb84_simulation.py` or open `bb84_notebook.ipynb`  
3. Observe outputs and error rates when Eve is present vs absent  

## Background  
BB84 leverages the no-cloning theorem and measurement disturbance to detect eavesdropping.

## References  
- [BB84 Protocol Wikipedia](https://en.wikipedia.org/wiki/BB84)  
- [Qiskit Textbook Chapter on QKD](https://qiskit.org/textbook/ch-algorithms/quantum-key-distribution.html)  
- [NIST Post-Quantum Cryptography](https://csrc.nist.gov/projects/post-quantum-cryptography)  

---

Feel free to open issues or suggest improvements!
