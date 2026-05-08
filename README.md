# 🐳 Docker + CI/CD Pipeline Demo

A production-style Flask application demonstrating Docker best practices and a full CI/CD pipeline with GitHub Actions. Features multi-stage Docker builds, health checks, automated testing, linting, and Docker image validation.

## 🏗️ CI/CD Pipeline

```
Push to GitHub
      │
      ▼
┌─────────────────────────────────────┐
│           GitHub Actions            │
│                                     │
│  ┌─────────┐  ┌────────┐  ┌──────┐ │
│  │  Test   │  │ Build  │  │ Lint │ │
│  │ pytest  │→ │Docker  │  │flake8│ │
│  │         │  │ image  │  │      │ │
│  └─────────┘  └────────┘  └──────┘ │
└─────────────────────────────────────┘
```

**3 automated jobs run on every push:**
1. **Test** — runs pytest unit tests
2. **Build** — builds Docker image & validates health endpoint
3. **Lint** — checks code quality with flake8

## 🚀 Features

- 🐳 Multi-stage Docker build (builder → production)
- ❤️ Docker health check on `/health` endpoint
- ⚙️ GitHub Actions CI/CD (test → build → lint)
- 🔒 Environment variable configuration
- 🧪 Unit tests with pytest

## 🛠️ Tech Stack

`Python` `Flask` `Docker` `GitHub Actions` `pytest` `flake8`

## ⚡ Quick Start

### Local

```bash
git clone https://github.com/eyildirim61/docker-cicd-demo
cd docker-cicd-demo

pip install -r requirements.txt
python app/main.py
```

### Docker

```bash
# Build and run
docker build -t docker-cicd-demo .
docker run -p 5000:5000 docker-cicd-demo

# Or with Docker Compose
docker-compose up --build
```

## 📡 API Endpoints

| Endpoint | Description |
|----------|-------------|
| `GET /` | App info and version |
| `GET /health` | Health check |
| `GET /info` | System & environment info |

## 🧪 Run Tests

```bash
pytest tests/ -v
```

## 📁 Project Structure

```
docker-cicd-demo/
├── .github/
│   └── workflows/
│       └── ci.yml          # GitHub Actions pipeline
├── app/
│   └── main.py             # Flask application
├── tests/
│   └── test_app.py
├── Dockerfile              # Multi-stage build
├── docker-compose.yml
└── requirements.txt
```

## 🔄 GitHub Actions Badge

![CI/CD](https://github.com/eyildirim61/docker-cicd-demo/actions/workflows/ci.yml/badge.svg)
# docker-cicd-demo
