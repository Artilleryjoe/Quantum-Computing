"""Toy QRAM-backed Grover search demonstration.

This script builds a small "database" encoded with a simulated QRAM
lookup, wraps it inside a Grover oracle, and runs a single Grover
iteration on a two-qubit address register. It also saves circuit
diagrams and a result histogram for quick visualization.
"""
from __future__ import annotations

import math
from pathlib import Path
from typing import Iterable, List

from qiskit import ClassicalRegister, QuantumCircuit, QuantumRegister, transpile
from qiskit.providers.aer import AerSimulator


def build_qram_gate(data_bits: Iterable[int]) -> QuantumCircuit:
    """Return a gate implementing a QRAM read for the given classical data.

    Args:
        data_bits: Iterable of 0/1 values representing classical contents.
    """
    data_list: List[int] = list(data_bits)
    address_bits = int(math.log2(len(data_list)))
    if 2 ** address_bits != len(data_list):
        raise ValueError("Length of data_bits must be a power of two")

    qr = QuantumRegister(address_bits + 1)
    qram_circuit = QuantumCircuit(qr, name="QRAM")
    address_qubits = qr[:address_bits]
    data_qubit = qr[address_bits]

    for address, bit in enumerate(data_list):
        if bit != 1:
            continue
        # Mark the address by flipping zero-controls to ones, applying mcx,
        # then un-flipping. This emulates routing through the bucket-brigade tree.
        address_state = format(address, f"0{address_bits}b")
        for idx, digit in enumerate(address_state):
            if digit == "0":
                qram_circuit.x(address_qubits[idx])
        qram_circuit.mcx(address_qubits, data_qubit)
        for idx, digit in enumerate(address_state):
            if digit == "0":
                qram_circuit.x(address_qubits[idx])

    return qram_circuit.to_gate()


def build_oracle(data_bits: Iterable[int], target_value: int = 1) -> QuantumCircuit:
    """Return an oracle that flips phase on addresses matching ``target_value``.

    The oracle applies QRAM, conditionally phases the data qubit based on the
    target bit value, then uncomputes QRAM.
    """
    data_list: List[int] = list(data_bits)
    address_bits = int(math.log2(len(data_list)))
    qr = QuantumRegister(address_bits + 1)
    oracle_circuit = QuantumCircuit(qr, name="Oracle")

    qram_gate = build_qram_gate(data_list)
    oracle_circuit.append(qram_gate, qr)

    data_qubit = qr[address_bits]
    if target_value == 1:
        oracle_circuit.z(data_qubit)
    else:
        oracle_circuit.x(data_qubit)
        oracle_circuit.z(data_qubit)
        oracle_circuit.x(data_qubit)

    oracle_circuit.append(qram_gate.inverse(), qr)
    return oracle_circuit.to_gate()


def diffuser(num_qubits: int) -> QuantumCircuit:
    """Standard Grover diffuser for ``num_qubits`` address qubits."""
    qr = QuantumRegister(num_qubits)
    diff = QuantumCircuit(qr, name="Diffuser")

    diff.h(qr)
    diff.x(qr)
    diff.h(qr[-1])
    diff.mcx(qr[:-1], qr[-1])
    diff.h(qr[-1])
    diff.x(qr)
    diff.h(qr)
    return diff.to_gate()


def draw_gate(gate: QuantumCircuit, file_path: Path, register_sizes: int) -> None:
    """Helper to render a gate with the text drawer and save to a file."""
    qc = QuantumCircuit(register_sizes)
    qc.append(gate, range(register_sizes))
    file_path.parent.mkdir(parents=True, exist_ok=True)
    with open(file_path, "w", encoding="utf-8") as handle:
        handle.write(qc.draw(output="text").single_string())


def write_histogram(counts: dict[str, int], file_path: Path, shots: int) -> None:
    """Persist a simple text-based histogram of measurement counts."""
    max_label_len = max(len(key) for key in counts)
    lines = ["Address | Count | Probability | Bar", "-" * 50]
    for key, value in sorted(counts.items(), key=lambda kv: kv[1], reverse=True):
        prob = value / shots
        bar = "#" * int(prob * 50)
        lines.append(f"{key.rjust(max_label_len)} | {value:5d} | {prob:0.3f} | {bar}")
    file_path.parent.mkdir(parents=True, exist_ok=True)
    file_path.write_text("\n".join(lines), encoding="utf-8")


def run_toy_grover(data_bits: Iterable[int], target_value: int = 1) -> None:
    data_list: List[int] = list(data_bits)
    address_bits = int(math.log2(len(data_list)))

    address = QuantumRegister(address_bits, name="addr")
    data = QuantumRegister(1, name="d")
    classical = ClassicalRegister(address_bits, name="c")
    grover = QuantumCircuit(address, data, classical)

    # Superposition over addresses
    grover.h(address)

    oracle_gate = build_oracle(data_list, target_value)
    diffuser_gate = diffuser(address_bits)

    grover.append(oracle_gate, grover.qubits[:-1])
    grover.append(diffuser_gate, address)
    grover.measure(address, classical)

    # Save circuit diagrams
    figures = Path(__file__).parent / "figures"
    draw_gate(build_qram_gate(data_list), figures / "qram_gate.txt", address_bits + 1)
    draw_gate(oracle_gate, figures / "oracle.txt", address_bits + 1)
    draw_gate(diffuser_gate, figures / "diffuser.txt", address_bits)

    figures.mkdir(parents=True, exist_ok=True)
    figures.joinpath("grover_iteration.txt").write_text(
        grover.draw(output="text").single_string(), encoding="utf-8"
    )

    # Run the Grover iteration
    simulator = AerSimulator()
    transpiled = transpile(grover, simulator)
    result = simulator.run(transpiled, shots=4000).result()
    counts = result.get_counts()

    write_histogram(counts, figures / "measurement_histogram.txt", shots=4000)

    # Print resource metrics
    print("QRAM depth / gates:", transpile(build_qram_gate(data_list)).depth(), transpile(build_qram_gate(data_list)).count_ops())
    print("Oracle depth / gates:", transpile(oracle_gate).depth(), transpile(oracle_gate).count_ops())
    print("Grover iteration depth / gates:", transpiled.depth(), transpiled.count_ops())
    print("Measurement counts:", counts)


if __name__ == "__main__":
    DATA_BITS = [1, 0, 1, 0]  # Address → data mapping
    run_toy_grover(DATA_BITS, target_value=1)
