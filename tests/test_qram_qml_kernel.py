from pathlib import Path
import sys

import pytest

sys.path.append(str(Path(__file__).resolve().parents[1]))

from experiments.qram_qml_kernel.qram_qml_kernel import QRAMConfig, classify, save_kernel_matrix


def test_qram_config_requires_non_empty_features():
    with pytest.raises(ValueError, match="at least one value"):
        QRAMConfig(features=[])


def test_classify_rejects_empty_training_data():
    with pytest.raises(ValueError, match="must not be empty"):
        classify(0.5, [], [])


def test_classify_rejects_mismatched_labels():
    with pytest.raises(ValueError, match="same length"):
        classify(0.5, [0.1, 0.9], [1])


def test_qram_config_uses_at_least_one_address_qubit():
    config = QRAMConfig(features=[0.42])
    assert config.address_qubits == 1


def test_save_kernel_matrix_writes_dynamic_headers(tmp_path):
    output = tmp_path / "kernel.csv"
    save_kernel_matrix(str(output), [[1.0, 0.5, 0.25], [0.5, 1.0, 0.5], [0.25, 0.5, 1.0]])

    rows = output.read_text().splitlines()
    assert rows[1] == ",x0,x1,x2"
