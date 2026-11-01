
# Cloud DevOps Platform

Automated Cloud Deployment, Monitoring and Self-Healing Platform.

## Project Overview

A practical DevOps project designed to demonstrate application
development, automated testing, CI/CD, cloud deployment,
monitoring and self-healing.

## Technology Stack

- Python
- Flask
- pytest
- Git
- GitHub
- Ubuntu Linux

## Project Structure

```text
cloud-devops-platform/
├── app/
│   ├── __init__.py
│   └── main.py
├── tests/
│   └── test_app.py
├── scripts/
├── docs/
├── requirements.txt
└── README.md
```

## Run Application

```bash
python3 -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
python -m flask --app app.main run --port 5000
```

## Run Automated Tests

```bash
python -m pytest -v
```

## Health Check

GET /health

Expected response:

```json
{"status": "healthy"}
```
