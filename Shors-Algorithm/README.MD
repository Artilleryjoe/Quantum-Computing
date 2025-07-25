n# Shor's Algorithm for Integer Factorization

## Overview  
This project demonstrates Shor's quantum algorithm to factor integers efficiently, showcasing the potential impact of quantum computing on classical cryptography.

This software includes cryptographic functionality that may be subject to U.S. Export Administration Regulations (EAR). It is classified as EAR99 and released under a public open-source license. This code is intended for lawful use and research purposes only.



## Features  
- Implementation of Shor's algorithm using Qiskit  
- Factoring small composite integers (e.g., 15, 21)  
- Explanation of quantum phase estimation and modular exponentiation  
- Discussion on limitations with current quantum hardware

## Requirements  
- Python 3.7+  
- Qiskit library (`pip install qiskit`)

## How to Run  
1. Clone the repo and navigate to this folder.  
2. Install dependencies: `pip install qiskit`  
3. Run the script: `python shors_algorithm.py`  
4. Review the output for factored integers and circuit details.

## Background  
Shor's algorithm provides an exponential speedup over classical factoring algorithms, threatening RSA and related cryptographic schemes.

## References  

- [Qiskit Textbook - Shor's Algorithm](https://qiskit.org/textbook/ch-algorithms/shor.html)

---

Feel free to open issues or suggest improvements!
