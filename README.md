# Transaction Anomaly Explorer

A learning project for exploring transaction data and detecting unusual transactions using Python and Pandas.

The project starts with simple statistical anomaly detection and gradually evolves toward an interactive, containerized application with ML and GenAI capabilities.

## Stack

* Python
* uv
* Pandas
* JupyterLab
* pytest

Planned:

* Streamlit
* Podman
* scikit-learn
* LLM integration

## Project Structure

```text
transaction-anomaly-explorer/
├── data/
│   └── transactions.csv
├── notebooks/
│   └── transaction_exploration.ipynb
├── src/
│   └── transaction_anomaly_explorer/
│       ├── __init__.py
│       └── analysis.py
├── tests/
│   └── test_analysis.py
├── .gitignore
├── .python-version
├── pyproject.toml
├── README.md
└── uv.lock
```

## Setup

Install the project dependencies:

```bash
uv sync
```

## Run the Analysis

```bash
uv run python src/transaction_anomaly_explorer/analysis.py
```

The current analysis uses the **Interquartile Range (IQR)** method to identify unusually high transaction amounts.

## Explore with Jupyter

Start JupyterLab:

```bash
uv run jupyter lab
```

Then open:

```text
notebooks/transaction_exploration.ipynb
```

The notebook is used to explore the transaction data, inspect distributions, and experiment with anomaly-detection approaches before moving useful logic into reusable Python modules.

## Run Tests

```bash
uv run pytest
```

## Current Anomaly Detection

The current implementation calculates:

```text
IQR = Q3 - Q1

upper threshold = Q3 + 1.5 × IQR
```

Transactions above the upper threshold are flagged as anomalies.

## Roadmap

### Initial Setup ✅

* [x] Initialize Python project with uv
* [x] Add Pandas
* [x] Add initial synthetic transaction dataset
* [x] Add basic transaction analysis
* [x] Set up project structure

### PR 1 — Jupyter Exploration ✅

* [x] Add JupyterLab
* [x] Create transaction exploration notebook
* [x] Explore distributions and summary statistics
* [x] Experiment with IQR-based anomaly detection
* [x] Expand the synthetic dataset
* [x] Move anomaly logic into reusable Python code
* [x] Add pytest coverage

### PR 2 — Streamlit Dashboard

* [ ] Add Streamlit
* [ ] Display transaction dataset
* [ ] Show detected anomalies
* [ ] Add basic metrics and filters
* [ ] Visualize transaction amounts and anomalies

### PR 3 — Containerization with Podman

* [ ] Add Containerfile
* [ ] Build the application image with Podman
* [ ] Run Streamlit inside the container
* [ ] Document the local container workflow

### PR 4 — ML Anomaly Detection

* [ ] Add scikit-learn
* [ ] Experiment with Isolation Forest in Jupyter
* [ ] Implement ML-based anomaly detection
* [ ] Add anomaly scores
* [ ] Compare IQR and Isolation Forest results

### PR 5 — AI Anomaly Explanations

* [ ] Add LLM integration
* [ ] Generate human-readable explanations for detected anomalies
* [ ] Keep anomaly detection separate from LLM explanation
* [ ] Display explanations in Streamlit

### PR 6 — Natural-Language Analysis

* [ ] Add a natural-language query interface
* [ ] Convert user questions into structured filters
* [ ] Support queries such as "Show unusual transactions from Germany"
* [ ] Add validation and guardrails around generated filters

## Learning Goals

This project is intended to demonstrate the progression from exploratory data analysis to a deployable AI-enabled application:

```text
Python + Pandas
      ↓
Jupyter Exploration
      ↓
Reusable Analysis
      ↓
Streamlit Application
      ↓
Podman Container
      ↓
ML Anomaly Detection
      ↓
LLM Explanations
      ↓
Natural-Language Analysis
```
