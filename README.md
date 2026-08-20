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
* GitHub Actions CI/CD
* Microsoft Entra ID / OIDC
* Azure Container Registry
* Azure Container Apps

Planned:

* scikit-learn
* LLM integration

## Project Structure

```text
transaction-anomaly-explorer/
├── .github/
│   └── workflows/
│       ├── ci.yml
│       └── cd.yml
├── data/
│   └── transactions.csv
├── notebooks/
│   └── transaction_exploration.ipynb
├── src/
│   └── transaction_anomaly_explorer/
│       ├── __init__.py
│       ├── analysis.py
│       └── validation.py
├── tests/
│   ├── test_analysis.py
│   └── test_validation.py
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

The application supports two data sources:

* **Sample dataset** — loads the bundled `data/transactions.csv`
* **Upload CSV** — allows users to analyze their own transaction dataset

Uploaded datasets are validated before analysis.

A valid transaction CSV must contain:

```text
transaction_id
customer_id
amount
country
merchant_category
```

Invalid or empty datasets are rejected with an error message before anomaly detection runs.

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

The application is deployed to **Azure Container Apps** using a container image stored in **Azure Container Registry (ACR)**.

The deployment flow is:

```text
Source Code
    │
    ▼
Containerfile
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

### Manual Build and Deployment

When building locally on Apple Silicon, the image must be built explicitly for Linux AMD64 before deployment:

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

Azure Container Apps pulls the image from ACR using managed identity.

The deployed Container App uses:

```text
Workload profile: Consumption
CPU:              0.5 cores
Memory:           1 GiB
Ingress:          External HTTPS
Target port:      8501
Registry auth:    Managed identity
```

## CI/CD

### Continuous Integration

GitHub Actions runs CI for pushes and pull requests.

The CI workflow:

```text
Git push / Pull Request
        │
        ▼
GitHub Actions
        │
        ├── Ruff
        └── pytest
        │
        ▼
      Pass / Fail
```

### Continuous Deployment

The CD workflow automates the Azure deployment process after CI succeeds on `main`.

```text
Merge to main
      │
      ▼
GitHub Actions CI
      │
      ▼
CI succeeds
      │
      ▼
GitHub Actions CD
      │
      ├── Authenticate to Azure via OIDC
      ├── Build Linux AMD64 image
      ├── Tag image with Git commit SHA
      ├── Push image to ACR
      └── Update Azure Container App
      │
      ▼
New Container Apps revision
      │
      ▼
Public Streamlit application
```

GitHub Actions authenticates to Azure using **OpenID Connect (OIDC)** rather than a stored Azure client password.

A Microsoft Entra application and federated credential establish trust between the GitHub repository's `main` branch and Azure:

```text
GitHub Actions
      │
      │ temporary OIDC token
      ▼
Microsoft Entra ID
      │
      ▼
github-transaction-anomaly-cd
      │
      ├── Contributor
      │   └── update Azure resources
      │
      └── AcrPush
          └── push container images to ACR
```

The GitHub repository provides the Azure identifiers required by the workflow through GitHub Actions secrets:

```text
AZURE_CLIENT_ID
AZURE_TENANT_ID
AZURE_SUBSCRIPTION_ID
```

No long-lived Azure client secret is required.

Container images are tagged with the Git commit SHA so that a deployed image can be traced back to the exact source-code revision that produced it.

## Current Anomaly Detection

The current implementation calculates:

```text
IQR = Q3 - Q1

upper threshold = Q3 + 1.5 × IQR
```

Transactions above the upper threshold are flagged as anomalies.

## Application Architecture

```text
GitHub
   │
   │ CI/CD
   ▼
GitHub Actions
   │
   │ OIDC
   ▼
Microsoft Entra ID
   │
   ▼
Azure Container Registry
   │
   │ container image
   ▼
Azure Container Apps
   │
   │ HTTPS ingress → port 8501
   ▼
Streamlit Container
   │
   ├── UI
   │     ├── Sample dataset
   │     └── CSV upload
   │
   ├── Input validation
   │
   └── Anomaly analysis
          │
          ▼
   Pandas / ML / LLM
```

Podman is used locally to build and test container images. Azure Container Registry stores deployable images, while Azure Container Apps provides the managed runtime that runs the Streamlit container.

GitHub Actions automates testing, image creation, registry publishing, and deployment.

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

### PR 6 — Continuous Deployment ✅

- [x] Create Microsoft Entra application for GitHub Actions
- [x] Configure GitHub OIDC federated credential for `main`
- [x] Grant deployment identity `Contributor` access
- [x] Grant deployment identity `AcrPush` access
- [x] Configure Azure identifiers as GitHub Actions secrets
- [x] Add GitHub Actions deployment workflow
- [x] Build the Linux AMD64 image automatically
- [x] Push SHA-tagged image to Azure Container Registry
- [x] Deploy the new image to Azure Container Apps
- [x] Trigger CD after successful CI on `main`
- [x] Verify the complete automated deployment flow

### PR 7 — CSV Upload and Validation ✅

- [x] Add sample/upload data-source selection
- [x] Add CSV file upload to Streamlit
- [x] Validate required transaction columns
- [x] Reject empty datasets
- [x] Handle malformed or unreadable CSV files
- [x] Add validation tests
- [x] Keep validation logic separate from the Streamlit UI

### PR 8 — ML Anomaly Detection

- [ ] Add scikit-learn
- [ ] Experiment with Isolation Forest in Jupyter
- [ ] Implement ML-based anomaly detection
- [ ] Add anomaly scores
- [ ] Compare IQR and Isolation Forest results

### PR 9 — AI Anomaly Explanations

- [ ] Add LLM integration
- [ ] Generate human-readable explanations for detected anomalies
- [ ] Keep anomaly detection separate from LLM explanation
- [ ] Display explanations in Streamlit

### PR 10 — Natural-Language Analysis

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
Continuous Integration
      │
      ▼
Streamlit Application
      │
      ├── Sample Data
      │
      └── CSV Upload
      │
      ▼
Input Validation
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
OIDC-based Continuous Deployment
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

The deployment path is intentionally container-based: **Streamlit provides the web application, Podman builds and tests container images locally, Azure Container Registry stores the images, Azure Container Apps runs them as managed cloud workloads, and GitHub Actions automates CI/CD using passwordless OIDC authentication to Azure.**