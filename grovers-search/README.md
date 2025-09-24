# Grover's Search Algorithm

## Overview  
Grover's algorithm provides a quantum speedup for unstructured search problems, offering a quadratic improvement over classical search algorithms.

This project demonstrates Grover's search algorithm using Qiskit by finding a marked item in a list.

This software includes cryptographic functionality that may be subject to U.S. Export Administration Regulations (EAR). It is classified as EAR99 and released under a public open-source license. This code is intended for lawful use and research purposes only.


## Features  
- Implementation of Grover's algorithm for a small search space  
- Oracle construction for the marked element  
- Amplification of the correct solution’s probability  
- Simulation results showing success probability  

## Requirements  
- Python 3.7+  
- Qiskit library (`pip install qiskit`)  

## How to Run  
1. Clone the repo and navigate to this folder.  
2. Install dependencies: `pip install qiskit`  
3. Run the Grover's search script: `python grovers_search.py`  
4. Review the output and measurement histogram.

## Background  
Grover's algorithm uses amplitude amplification to find a marked item in an unsorted database in O(√N) time, compared to O(N) classically.

## References  
- [Grover's Algorithm - Wikipedia](https://en.wikipedia.org/wiki/Grover%27s_algorithm)  
- [Qiskit Textbook - Grover's Algorithm](https://qiskit.org/textbook/ch-algorithms/grover.html)

---

Feel free to open issues or suggest improvements!
