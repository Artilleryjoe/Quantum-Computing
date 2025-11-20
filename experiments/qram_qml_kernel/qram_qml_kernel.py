"""Minimal QRAM-enabled quantum kernel demonstration (pure Python).

A toy QRAM loader emits rotations based on a 1-bit address.  The resulting
quantum states are used to build a kernel matrix and label a test point.  The
math is small enough to run without external dependencies, which makes the
resource overhead of the QRAM block easy to reason about.
"""
from __future__ import annotations

import csv
import math
from dataclasses import dataclass
from typing import Dict, List


@dataclass
class QRAMConfig:
    """Configuration for the toy QRAM loader."""

    features: List[float]

    @property
    def thetas(self) -> List[float]:
        return [math.pi * x for x in self.features]

    @property
    def num_addresses(self) -> int:
        return len(self.features)

    @property
    def address_qubits(self) -> int:
        # Enough qubits to index every training point.  Only one is needed for 2 points.
        return math.ceil(math.log2(self.num_addresses))


def rotation_state(theta: float) -> List[float]:
    """Return the amplitudes of Ry(theta)|0>."""

    return [math.cos(theta / 2), math.sin(theta / 2)]


def fidelity(theta_a: float, theta_b: float) -> float:
    """State fidelity between two Ry rotations applied to |0>."""

    # |<psi_a|psi_b>|^2 simplifies to cos^2((theta_a - theta_b)/2).
    return math.cos((theta_a - theta_b) / 2) ** 2


def kernel_matrix(thetas: List[float]) -> List[List[float]]:
    return [[fidelity(ti, tj) for tj in thetas] for ti in thetas]


def classify(test_feature: float, training_thetas: List[float], labels: List[int]) -> int:
    theta_test = math.pi * test_feature
    fidelities = [fidelity(theta_test, ti) for ti in training_thetas]
    return labels[fidelities.index(max(fidelities))]


def qram_resource_cost(num_addresses: int) -> Dict[str, int]:
    """Rough gate counts for the 2-address rotation loader."""

    # For two addresses we use a single address qubit, two X gates to toggle the
    # |0> branch, and two controlled RY rotations.
    if num_addresses != 2:
        raise ValueError("This demo assumes exactly two addresses")

    depth = 4  # X, CRY, X, CRY executed sequentially
    return {"x_gates": 2, "controlled_ry": 2, "depth": depth, "size": 4}


def save_kernel_matrix(path: str, kernel: List[List[float]]) -> None:
    with open(path, "w", newline="") as f:
        writer = csv.writer(f)
        writer.writerow(["Kernel matrix K(i,j) = |<psi_i|psi_j>|^2"])
        writer.writerow(["", "x0", "x1"])
        for idx, row in enumerate(kernel):
            writer.writerow([f"x{idx}", *[f"{val:.6f}" for val in row]])


def main() -> None:
    config = QRAMConfig(features=[0.2, 0.8])
    labels = [0, 1]

    print("Rotation angles (theta = pi * x):")
    for idx, theta in enumerate(config.thetas):
        print(f"  address {idx}: x={config.features[idx]:.2f} -> theta={theta:.4f} rad")

    resources = qram_resource_cost(config.num_addresses)
    print("\nQRAM loader resources:")
    for k, v in resources.items():
        print(f"  {k}: {v}")

    k = kernel_matrix(config.thetas)
    print("\nKernel matrix K(i,j) = |<psi_i|psi_j>|^2:")
    for row in k:
        print("  ", [f"{val:.6f}" for val in row])

    test_feature = 0.6
    predicted = classify(test_feature, config.thetas, labels)
    print(f"\nClassifying test feature x={test_feature}: predicted label -> {predicted}")

    save_kernel_matrix("kernel_matrix.csv", k)
    print("\nSaved kernel matrix to kernel_matrix.csv")


if __name__ == "__main__":
    main()
