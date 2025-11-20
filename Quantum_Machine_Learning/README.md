# Quantum Machine Learning Experiments

This folder prepares a lightweight environment for future demonstrations of quantum machine learning (QML) techniques that target realistic cybersecurity analytics scenarios.

## Current contents
- `requirements.txt` pins the Qiskit 2.2 release series and supporting scientific packages for notebook-driven experiments.
- Space reserved for datasets and notebooks as the experiments are published.

## Suggested setup

```bash
python3 -m venv qml_env
source qml_env/bin/activate
python -m pip install --upgrade pip
pip install -r requirements.txt
```

## Contributing experiments
- Place reusable datasets under a new `data/` directory.
- Add each study under `experiments/<topic>/` with a README and notebook describing goals, workflow, and observations.
- Use the pinned dependencies when possible to keep results reproducible.

Ideas and pull requests that add concrete QML studies are welcome!
