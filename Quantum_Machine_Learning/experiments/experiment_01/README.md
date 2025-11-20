# Experiment 01 – Quantum Kernel Anomaly Detection

This directory bundles the assets for the first quantum machine learning
experiment in the repository. It showcases how a quantum kernel-based
support vector machine (QSVM) can assist with anomaly detection tasks
that are inspired by malicious URL identification scenarios.

## Contents

- `QML_Cyber_URL_QSVM.ipynb` – An interactive notebook that prepares data,
  engineers simple URL features, and compares classical and quantum kernel
  anomaly detectors.
- `experiment.py` – A runnable script that mirrors the notebook's quantum
  kernel workflow using a synthetic dataset. Execute it from the repository
  root with `python experiments/experiment_01/experiment.py`.

The shared dataset `data/urls_sample.csv` contains a compact set of labeled
URL examples. Copy or reference the file when exploring custom pipelines in
the notebook.

## Environment setup

Create and activate a Python environment that matches the Qiskit 2.2 toolchain
used by the repository:

```bash
python3 -m venv qml_env
source qml_env/bin/activate
python -m pip install --upgrade pip
pip install -r ../../requirements.txt
```

The requirement set explicitly installs `qiskit==2.2.*` alongside the Aer
simulator (`qiskit-aer`), shared algorithm utilities (`qiskit-algorithms`), and
the machine learning extension (`qiskit-machine-learning`). This mirrors the
imports used in `experiment.py`, where the quantum kernel relies on the Aer
backend interface introduced in Qiskit 2.x and the global RNG seed helper that
now lives in `qiskit_algorithms.utils`.

## Running the notebook

1. Launch Jupyter from the repository root:
   ```bash
   jupyter lab
   ```
2. Open `experiments/experiment_01/QML_Cyber_URL_QSVM.ipynb`.
3. Update any file paths if you relocate the dataset.
4. Execute the cells in order, observing both the classical baseline and
   quantum kernel performance.

## Running the script

```bash
python experiments/experiment_01/experiment.py
```

The script prints precision/recall metrics for the quantum kernel model and a
classical RBF baseline, making it easy to compare decision boundaries without
the notebook interface.

## Notes

- Quantum kernel simulations become expensive as you increase the feature map
  dimension (`d`) or the number of repetitions (`reps`). Start small.
- Treat these experiments as exploratory references rather than production-ready
  cybersecurity detectors.
