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

Planned:

* Streamlit
* Podman
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
* [ ] Reuse the existing Python analysis layer from the Streamlit application

### PR 3 — Containerization with Podman

* [ ] Add Containerfile
* [ ] Package Streamlit and the Python application into a container image
* [ ] Build the image with Podman
* [ ] Run the Streamlit application locally as a container
* [ ] Configure the Streamlit port for container deployment
* [ ] Document the local container workflow

### PR 4 — Azure Container Apps Deployment

* [ ] Push the container image to a container registry
* [ ] Create an Azure Container App
* [ ] Deploy the Streamlit container
* [ ] Configure external HTTPS ingress
* [ ] Configure environment variables and secrets
* [ ] Verify the application through its public Azure URL

### PR 5 — ML Anomaly Detection

* [ ] Add scikit-learn
* [ ] Experiment with Isolation Forest in Jupyter
* [ ] Implement ML-based anomaly detection
* [ ] Add anomaly scores
* [ ] Compare IQR and Isolation Forest results
* [ ] Expose the ML results through Streamlit

### PR 6 — AI Anomaly Explanations

* [ ] Add LLM integration
* [ ] Generate human-readable explanations for detected anomalies
* [ ] Keep anomaly detection separate from LLM explanation
* [ ] Display AI-generated explanations in Streamlit
* [ ] Keep credentials outside the application code

### PR 7 — Natural-Language Analysis

* [ ] Add a natural-language query interface
* [ ] Convert user questions into structured filters
* [ ] Support queries such as "Show unusual transactions from Germany"
* [ ] Validate generated filters before execution
* [ ] Add guardrails around AI-generated queries

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
