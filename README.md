# Transaction Anomaly Explorer

A learning project for exploring transaction data and detecting unusual transactions using Python and Pandas.

The project starts with statistical anomaly detection and gradually evolves toward an interactive, containerized, cloud-deployed application with ML and GenAI capabilities.

## Stack

Current:

* Python
* uv
* Pandas
* JupyterLab
* pytest
* Ruff
* Streamlit
* Podman
* Azure Container Registry
* Azure Container Apps

Planned:

* GitHub Actions CD
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
├── app.py
├── Containerfile
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
```

Then open:

`http://localhost:8501`

## Run Tests

```bash
uv run pytest
```

## Run Linting

```bash
uv run ruff check .
```

## Run with Podman

Build the container image locally:

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

## Azure Deployment

The application is deployed to **Azure Container Apps** using an image stored in **Azure Container Registry (ACR)**.

The deployment flow is:

```text
Source Code
    │
    ▼
Containerfile
    │
    ▼
Podman Build
    │
    ▼
Container Image
    │
    ▼
Azure Container Registry
    │
    ▼
Azure Container Apps
    │
    ▼
Streamlit Application
    │
    ▼
Public HTTPS Endpoint
```

### Build for Azure

When building on Apple Silicon, the image must be built explicitly for Linux AMD64 before deployment:

```bash
podman build \
  --platform linux/amd64 \
  -t transactionanomalyregistry.azurecr.io/transaction-anomaly-explorer:v1 .
```

Push the image to ACR:

```bash
podman push \
  transactionanomalyregistry.azurecr.io/transaction-anomaly-explorer:v1
```

Azure Container Apps then pulls the image from ACR using managed identity.

The deployed Container App uses:

```text
Workload profile: Consumption
CPU:              0.5 cores
Memory:           1 GiB
Ingress:          External HTTPS
Target port:      8501
Registry auth:    Managed identity
```

## Current Anomaly Detection

The current implementation calculates:

```text
IQR = Q3 - Q1

upper threshold = Q3 + 1.5 × IQR
```

Transactions above the upper threshold are flagged as anomalies.

## Application Architecture

```text
Browser
   │
   │ HTTPS
   ▼
Azure Container Apps
   │
   │ ingress → port 8501
   ▼
Streamlit Container
   │
   ├── UI
   ├── Python application logic
   └── anomaly visualization
          │
          ▼
   Pandas / ML / LLM


Azure Container Registry
   │
   │ container image
   ▼
Azure Container Apps
```

Podman is used locally to build and test the container image. Azure Container Registry stores the deployable image, while Azure Container Apps provides the managed runtime that runs the Streamlit container.

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

### PR 2 — Continuous Integration ✅

- [x] Add GitHub Actions workflow
- [x] Set up Python and uv in CI
- [x] Install dependencies with `uv sync`
- [x] Run pytest automatically
- [x] Run CI on pushes and pull requests
- [x] Add linting with Ruff

### PR 3 — Streamlit Dashboard ✅

- [x] Add Streamlit
- [x] Display transaction dataset
- [x] Show detected anomalies
- [x] Add basic metrics and filters
- [x] Visualize transaction amounts and anomalies
- [x] Reuse the existing Python analysis layer

### PR 4 — Containerization with Podman ✅

- [x] Add Containerfile
- [x] Package the Streamlit application
- [x] Build the image with Podman
- [x] Run the Streamlit application locally as a container
- [x] Expose Streamlit on port 8501
- [x] Document the local container workflow

### PR 5 — Azure Container Apps Deployment ✅

- [x] Create Azure resource group
- [x] Create Azure Container Registry
- [x] Build a Linux AMD64 container image
- [x] Push the container image to ACR
- [x] Create a Container Apps Environment
- [x] Create an Azure Container App
- [x] Configure managed-identity access to ACR
- [x] Deploy the Streamlit container
- [x] Configure external HTTPS ingress
- [x] Route ingress to Streamlit on port 8501
- [x] Verify the application through its public Azure URL

### PR 6 — Continuous Deployment

- [ ] Add GitHub Actions deployment workflow
- [ ] Authenticate GitHub Actions with Azure
- [ ] Build the Linux AMD64 container image automatically
- [ ] Push versioned images to Azure Container Registry
- [ ] Deploy the new image to Azure Container Apps
- [ ] Trigger deployment after successful changes to `main`
- [ ] Verify the automated deployment flow

### PR 7 — ML Anomaly Detection

- [ ] Add scikit-learn
- [ ] Experiment with Isolation Forest in Jupyter
- [ ] Implement ML-based anomaly detection
- [ ] Add anomaly scores
- [ ] Compare IQR and Isolation Forest results

### PR 8 — AI Anomaly Explanations

- [ ] Add LLM integration
- [ ] Generate human-readable explanations for detected anomalies
- [ ] Keep anomaly detection separate from LLM explanation
- [ ] Display explanations in Streamlit

### PR 9 — Natural-Language Analysis

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
CI with GitHub Actions
      │
      ▼
Streamlit Application
      │
      ▼
Podman Container
      │
      ▼
Azure Container Registry
      │
      ▼
Azure Container Apps
      │
      ▼
Continuous Deployment
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

The deployment path is intentionally container-based: **Streamlit provides the web application, Podman builds and tests the container image locally, Azure Container Registry stores the image, and Azure Container Apps runs it as a managed cloud workload.**