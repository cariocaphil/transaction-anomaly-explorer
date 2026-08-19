# Transaction Anomaly Explorer

A learning project for exploring transaction data and detecting unusual transactions using Python and Pandas.

The project starts with statistical anomaly detection and gradually evolves toward an interactive, containerized application with ML and GenAI capabilities.

## Stack

Current:

* Python
* uv
* Pandas
* JupyterLab
* pytest
* Streamlit
* Podman

Planned:

* Azure Container Apps
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

The notebook is used to explore transaction data, inspect distributions, and experiment with anomaly-detection approaches before moving useful logic into reusable Python modules.

## Run the Streamlit App

Start the application locally:

```bash
PYTHONPATH=src uv run streamlit run app.py

## Run Tests

```bash
uv run pytest
```

## Run with Podman

Build the container image:

```bash
podman build -t transaction-anomaly-explorer .
```

Run the container:

```bash
podman run --rm -p 8501:8501 transaction-anomaly-explorer
```

Then open:

`http://localhost:8501`

The container packages the Streamlit application, Python runtime, project dependencies, analysis code, and transaction data into a reproducible runtime environment.

## Current Anomaly Detection

The current implementation calculates:

```text
IQR = Q3 - Q1

upper threshold = Q3 + 1.5 × IQR
```

Transactions above the upper threshold are flagged as anomalies.

## Planned Application Architecture

The final application will use Streamlit as the Python web application framework.

For deployment, the Streamlit application will be packaged as a container and deployed to Azure Container Apps.

```text
Browser
   │
   ▼
Azure Container Apps
   │
   │ HTTPS / ingress
   ▼
Podman-built container
   │
   ▼
Streamlit
   │
   ├── UI
   ├── Python application logic
   └── anomaly visualization
          │
          ▼
   Pandas / ML / LLM
```

Podman is used locally to build and test the container image. The container image provides a reproducible runtime that can then be deployed to Azure Container Apps.

## Roadmap

### Initial Setup ✅

- [x] Initialize Python project with uv
- [x] Add Pandas
- [x] Add initial synthetic transaction dataset
- [x] Add basic transaction analysis
- [x] Set up project structure

### PR 1 — Jupyter Exploration ✅

- [x] Add JupyterLab
- [x] Create transaction exploration notebook
- [x] Explore distributions and summary statistics
- [x] Experiment with IQR-based anomaly detection
- [x] Expand the synthetic dataset
- [x] Move anomaly logic into reusable Python code
- [x] Add pytest coverage

### PR 2 — Continuous Integration

- [x] Add GitHub Actions workflow
- [x] Set up Python and uv in CI
- [x] Install dependencies with `uv sync`
- [x] Run pytest automatically
- [x] Run CI on pushes and pull requests
- [x] Add linting with Ruff

### PR 3 — Streamlit Dashboard

- [x] Add Streamlit
- [x] Display transaction dataset
- [x] Show detected anomalies
- [x] Add basic metrics and filters
- [x] Visualize transaction amounts and anomalies
- [x] Reuse the existing Python analysis layer

### PR 4 — Containerization with Podman

- [x] Add Containerfile
- [x] Package the Streamlit application
- [x] Build the image with Podman
- [x] Run the Streamlit application locally as a container
- [x] Document the local container workflow

### PR 5 — Azure Container Apps Deployment

- [ ] Push the container image to a container registry
- [ ] Create an Azure Container App
- [ ] Deploy the Streamlit container
- [ ] Configure external HTTPS ingress
- [ ] Configure environment variables and secrets
- [ ] Verify the application through its public Azure URL

### PR 6 — ML Anomaly Detection

- [ ] Add scikit-learn
- [ ] Experiment with Isolation Forest in Jupyter
- [ ] Implement ML-based anomaly detection
- [ ] Add anomaly scores
- [ ] Compare IQR and Isolation Forest results

### PR 7 — AI Anomaly Explanations

- [ ] Add LLM integration
- [ ] Generate human-readable explanations for detected anomalies
- [ ] Keep anomaly detection separate from LLM explanation
- [ ] Display explanations in Streamlit

### PR 8 — Natural-Language Analysis

- [ ] Add a natural-language query interface
- [ ] Convert user questions into structured filters
- [ ] Validate generated filters before execution
- [ ] Add guardrails around AI-generated queries

## Learning Goals

The project demonstrates the progression from exploratory Python work to a deployed AI-enabled application:

```text
Python + Pandas
      │
      ▼
Jupyter Exploration
      │
      ▼
Reusable Python Analysis
      │
      ▼
Streamlit Application
      │
      ▼
Podman Container
      │
      ▼
Azure Container Apps
      │
      ▼
ML Anomaly Detection
      │
      ▼
LLM Explanations
      │
      ▼
Natural-Language Analysis
```

The deployment path is intentionally container-based: **Streamlit provides the application framework, Podman provides the container image, and Azure Container Apps provides the managed cloud runtime.**
