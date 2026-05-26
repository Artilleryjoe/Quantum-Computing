"""Quantum kernel-based anomaly detection aligned with Qiskit 2.2 APIs."""

from __future__ import annotations

import dataclasses
import argparse
from typing import Tuple

import numpy as np
from sklearn.metrics import classification_report
from sklearn.preprocessing import MinMaxScaler
from sklearn.svm import OneClassSVM

# --- Qiskit imports ---
from qiskit_aer import AerSimulator
from qiskit_aer.noise import NoiseModel, depolarizing_error
from qiskit.circuit.library import ZZFeatureMap
from qiskit_machine_learning.kernels import FidelityQuantumKernel
from qiskit_algorithms.utils import algorithm_globals


# ----------------------------
# Data generation
# ----------------------------
def generate_synthetic_dataset(
    *, n_nominal: int = 120, n_anomalous: int = 30, seed: int | None = None
) -> Tuple[np.ndarray, np.ndarray, np.ndarray]:
    rng = np.random.default_rng(seed)
    mean = np.array([0.5, -0.2])
    cov = np.array([[0.2, 0.15], [0.15, 0.3]])
    nominal = rng.multivariate_normal(mean, cov, size=n_nominal)

    lower_bounds = mean - 2.5 * np.sqrt(np.diag(cov))
    upper_bounds = mean + 2.5 * np.sqrt(np.diag(cov))
    anomalous = rng.uniform(lower_bounds, upper_bounds, size=(n_anomalous, 2))

    data = np.vstack([nominal, anomalous])
    labels = np.concatenate([np.ones(n_nominal), -np.ones(n_anomalous)])
    is_nominal = np.array([True] * n_nominal + [False] * n_anomalous)
    return data, labels, is_nominal


# ----------------------------
# Result container
# ----------------------------
@dataclasses.dataclass
class QuantumAnomalyDetectionResult:
    train_fraction: float
    quantum_report: str
    classical_report: str


# ----------------------------
# Quantum kernel builder
# ----------------------------
def build_quantum_kernel(feature_dimension: int, reps: int = 2) -> FidelityQuantumKernel:
    """Build a FidelityQuantumKernel backed by Aer for Qiskit 2.2 installs."""

    feature_map = ZZFeatureMap(feature_dimension=feature_dimension, reps=reps)
    backend = AerSimulator()
    return FidelityQuantumKernel(feature_map=feature_map, backend=backend)


def depolarizing_noise_model(probability: float = 0.01) -> NoiseModel:
    """Create a simple depolarizing noise model for 1q and 2q basis gates."""
    if not 0.0 <= probability < 1.0:
        raise ValueError("probability must be in [0.0, 1.0).")

    noise_model = NoiseModel()
    noise_model.add_all_qubit_quantum_error(depolarizing_error(probability, 1), ["rz", "sx", "x"])
    noise_model.add_all_qubit_quantum_error(
        depolarizing_error(probability, 2),
        ["cx"],
    )
    return noise_model


def build_noisy_quantum_kernel(
    feature_dimension: int, reps: int = 2, noise_probability: float = 0.01
) -> FidelityQuantumKernel:
    feature_map = ZZFeatureMap(feature_dimension=feature_dimension, reps=reps)
    backend = AerSimulator(noise_model=depolarizing_noise_model(noise_probability))
    return FidelityQuantumKernel(feature_map=feature_map, backend=backend)


# ----------------------------
# Evaluators
# ----------------------------
def evaluate_quantum_kernel_svm(
    kernel: FidelityQuantumKernel, train_data: np.ndarray, test_data: np.ndarray
) -> Tuple[OneClassSVM, np.ndarray]:
    k_train = kernel.evaluate(x_vec=train_data)
    svm = OneClassSVM(kernel="precomputed", nu=0.1, gamma="auto")
    svm.fit(k_train)

    k_test = kernel.evaluate(x_vec=test_data, y_vec=train_data)
    predictions = svm.predict(k_test)
    return svm, predictions


def evaluate_classical_baseline(
    train_data: np.ndarray, test_data: np.ndarray
) -> Tuple[OneClassSVM, np.ndarray]:
    svm = OneClassSVM(kernel="rbf", nu=0.1, gamma="scale")
    svm.fit(train_data)
    predictions = svm.predict(test_data)
    return svm, predictions


# ----------------------------
# Experiment runner
# ----------------------------
def run_experiment(
    *, train_fraction: float = 0.75, seed: int = 7, use_noise: bool = False, noise_probability: float = 0.01
) -> QuantumAnomalyDetectionResult:
    if not 0.1 <= train_fraction <= 0.95:
        raise ValueError("train_fraction should be between 0.1 and 0.95 for stability.")

    algorithm_globals.random_seed = seed
    raw_data, labels, is_nominal = generate_synthetic_dataset(seed=seed)

    scaler = MinMaxScaler(feature_range=(-1.0, 1.0))
    scaled_data = scaler.fit_transform(raw_data)

    nominal_data = scaled_data[is_nominal]
    n_train = int(len(nominal_data) * train_fraction)
    train_data = nominal_data[:n_train]
    test_data = scaled_data[n_train:]
    test_labels = labels[n_train:]

    quantum_kernel = (
        build_noisy_quantum_kernel(
            feature_dimension=scaled_data.shape[1],
            noise_probability=noise_probability,
        )
        if use_noise
        else build_quantum_kernel(feature_dimension=scaled_data.shape[1])
    )
    _, quantum_predictions = evaluate_quantum_kernel_svm(quantum_kernel, train_data, test_data)
    _, classical_predictions = evaluate_classical_baseline(train_data, test_data)

    quantum_report = classification_report(
        test_labels, quantum_predictions, target_names=["Anomalous", "Nominal"], zero_division=0
    )
    classical_report = classification_report(
        test_labels, classical_predictions, target_names=["Anomalous", "Nominal"], zero_division=0
    )

    return QuantumAnomalyDetectionResult(
        train_fraction=train_fraction,
        quantum_report=quantum_report,
        classical_report=classical_report,
    )


# ----------------------------
# Entry point
# ----------------------------
def main() -> None:
    parser = argparse.ArgumentParser(description="Run quantum kernel anomaly detection experiment.")
    parser.add_argument("--train-fraction", type=float, default=0.75, help="Fraction of nominal data used for training.")
    parser.add_argument("--seed", type=int, default=7, help="Random seed used for reproducibility.")
    parser.add_argument(
        "--noise",
        action="store_true",
        help="Enable depolarizing noise model on the quantum simulator.",
    )
    parser.add_argument(
        "--noise-probability",
        type=float,
        default=0.01,
        help="Depolarizing error probability when --noise is enabled.",
    )
    args = parser.parse_args()

    result = run_experiment(
        train_fraction=args.train_fraction,
        seed=args.seed,
        use_noise=args.noise,
        noise_probability=args.noise_probability,
    )
    print("Quantum kernel anomaly detection report:\n")
    if args.noise:
        print(f"[noise enabled] depolarizing probability={args.noise_probability}\n")
    else:
        print("[noise disabled] running ideal simulator\n")
    print(result.quantum_report)
    print("Classical RBF baseline report:\n")
    print(result.classical_report)


if __name__ == "__main__":
    main()
