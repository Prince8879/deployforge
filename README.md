# DeployForge 🚀

A hands-on DevOps project that demonstrates how to test, containerize, and automate the delivery of a Flask application using Docker, GitHub Actions, and GitHub Container Registry (GHCR).

## 📌 Project Overview

DeployForge is built to practice real-world DevOps workflows, starting with a simple Flask application and progressing toward cloud deployment, monitoring, and automation.

### Current Features

- Flask web application with a health-check endpoint
- Automated tests using pytest
- Docker-based containerization
- GitHub Actions CI workflow
- Automated Docker image publishing to GHCR
- Public Docker image available for anonymous pulls
- Git and Docker secret-exclusion practices

## 🛠️ Tech Stack

| Technology | Purpose |
|---|---|
| Python 3.13 | Application runtime |
| Flask | Web framework |
| Pytest | Automated testing |
| Docker | Containerization |
| Git & GitHub | Version control |
| GitHub Actions | CI automation |
| GitHub Container Registry | Docker image storage |
| AWS EC2 | Planned cloud deployment |
| Prometheus & Grafana | Planned monitoring |

## 🏗️ Project Structure

```text
deployforge/
├── app.py
├── tests/
│   └── test_health.py
├── .github/
│   └── workflows/
│       └── ci.yml
├── Dockerfile
├── .dockerignore
├── .gitignore
├── requirements.txt
├── requirements-dev.txt
├── Masterplan.txt
├── Project Structure.txt
└── README.md
```

## ⚙️ Application Endpoints

| Endpoint | Description |
|---|---|
| `/` | Returns the welcome message |
| `/health` | Returns application health status |

Health-check response:

```json
{
  "status": "healthy"
}
```

## 💻 Run Locally

### 1. Clone the repository

```powershell
git clone https://github.com/Prince8879/deployforge.git
cd deployforge
```

### 2. Create a virtual environment

```powershell
python -m venv .venv
```

### 3. Activate the environment

```powershell
.\.venv\Scripts\Activate.ps1
```

### 4. Install dependencies

```powershell
pip install -r requirements-dev.txt
```

### 5. Run tests

```powershell
python -m pytest
```

### 6. Start the application

```powershell
python app.py
```

Open `http://localhost:5000` in your browser.

Health check: `http://localhost:5000/health`

## 🐳 Docker Usage

### Build the Docker image

```powershell
docker build -t deployforge:v2 .
```

### Run the container

```powershell
docker run -d --name deployforge-v2 -p 5001:5000 deployforge:v2
```

Open `http://localhost:5001` to access the application.

### View container logs

```powershell
docker logs deployforge-v2
```

### Stop the container

```powershell
docker stop deployforge-v2
```

## 🔄 CI Pipeline

GitHub Actions automates the following workflow when changes are pushed to the `main` branch or a pull request targets `main`:

1. Check out the repository.
2. Set up Python.
3. Install application and development dependencies.
4. Run automated tests.
5. Build the Docker image.
6. Authenticate with GitHub Container Registry.
7. Publish the Docker image.

The workflow uses GitHub Actions and the automatically generated `GITHUB_TOKEN` for registry authentication.

## 📦 Public Docker Image

DeployForge's Docker image is published to GitHub Container Registry.

**Image:**

`ghcr.io/prince8879/deployforge:latest`

Pull the image:

```powershell
docker pull ghcr.io/prince8879/deployforge:latest
```

Run the image:

```powershell
docker run -d --name deployforge -p 5001:5000 ghcr.io/prince8879/deployforge:latest
```

Verify the application at `http://localhost:5001`.

The public image has been successfully pulled without authentication.

## 🔐 Security Practices

- `.gitignore` excludes `.env` files from Git.
- `.dockerignore` excludes `.env`, `.env.*`, virtual environments, Git metadata, tests, and unnecessary files from the Docker build context.
- Never commit passwords, access tokens, API keys, or other secrets.
- Use GitHub Actions secrets and least-privilege token permissions for automation.
- Keep container registry credentials out of application code and Docker images.
- Review changes and Git history before publishing sensitive projects.

## 🗺️ Project Roadmap

- [x] Phase 1 — Flask application and health endpoint
- [x] Phase 2 — Automated testing with pytest
- [x] Phase 3 — Docker containerization
- [x] Phase 4 — GitHub Actions CI workflow
- [x] Phase 5 — GHCR publishing and public image verification
- [ ] Phase 6 — Deploy the application to AWS EC2
- [ ] Phase 7 — Monitoring and logging
- [ ] Phase 8 — Further automation and security improvements

## 🎯 Learning Objectives

- Understand containerization and Docker image management.
- Build automated testing and CI workflows.
- Publish and distribute container images through GHCR.
- Apply Git and Docker secret-exclusion practices.
- Deploy applications to cloud infrastructure.
- Develop practical DevOps skills through implementation.

## 📄 License

No license has been specified yet. Add an appropriate license before explicitly permitting reuse or redistribution.

---


