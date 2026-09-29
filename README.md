
# DevOps Python Practice Application

A deliberately small Python application designed to practice:

- Python + Flask
- Git/GitHub
- GitHub Actions
- Docker
- Docker Compose
- Terraform
- Ansible
- Kubernetes
- Helm
- Prometheus
- Grafana

## Application endpoints

- `/` - application response
- `/health` - Kubernetes liveness endpoint
- `/ready` - Kubernetes readiness endpoint
- `/metrics` - Prometheus metrics

## 1. Run locally

From the project root:

```bash
python -m venv .venv
```

Windows:

```powershell
.venv\Scripts\activate
```

Linux/WSL:

```bash
source .venv/bin/activate
```

Then:

```bash
pip install -r app/requirements.txt
pytest -q
python app/app.py
```

Open:

```text
http://localhost:5000
```

## 2. Run with Docker

```bash
docker build -t devops-python-app ./app
docker run --rm -p 5000:5000 devops-python-app
```

## 3. Run app + Prometheus + Grafana

```bash
docker compose up --build
```

Open:

```text
App:        http://localhost:5000
Prometheus: http://localhost:9090
Grafana:    http://localhost:3000
```

Grafana default login for this local practice stack is:

```text
username: admin
password: admin
```

Change this before using it anywhere beyond local practice.

## 4. Terraform

Terraform creates an ECR repository:

```bash
cd terraform
terraform init
terraform fmt
terraform validate
terraform plan
terraform apply
```

## 5. Ansible

Update `ansible/inventory.ini` with your server.

Then:

```bash
ansible-playbook -i ansible/inventory.ini ansible/install_docker.yml
```

## 6. Kubernetes

Replace the GitHub username in `k8s/deployment.yaml`.

Then:

```bash
kubectl apply -f k8s/namespace.yaml
kubectl apply -f k8s/deployment.yaml
kubectl apply -f k8s/service.yaml
```

Check:

```bash
kubectl get pods -n devops-app
kubectl get svc -n devops-app
```

For local access:

```bash
kubectl port-forward -n devops-app svc/python-app 8080:80
```

Open:

```text
http://localhost:8080
```

## 7. Helm

Replace the GitHub username in `helm/devops-python-app/values.yaml`.

Validate:

```bash
helm lint helm/devops-python-app
```

Install:

```bash
helm install devops-app helm/devops-python-app
```

Upgrade:

```bash
helm upgrade devops-app helm/devops-python-app
```

## 8. GitHub Actions

Push this repository to GitHub.

The workflow:

1. Checks out the code
2. Installs Python
3. Runs pytest
4. Builds the Docker image
5. Pushes the image to GitHub Container Registry (GHCR)

For the Kubernetes manifests, replace:

```text
ghcr.io/REPLACE_WITH_GITHUB_USERNAME/devops-python-app:latest
```

with your GitHub username.

## Suggested learning path

1. Run Python locally
2. Write/fix a test
3. Build the Docker image
4. Run Docker Compose
5. Explore Prometheus metrics
6. Explore Grafana dashboard
7. Push to GitHub
8. Study the GitHub Actions pipeline
9. Create ECR with Terraform
10. Use Ansible on an Ubuntu server
11. Deploy to Kubernetes
12. Deploy the same application with Helm
13. Add Prometheus Operator / ServiceMonitor
14. Later extend Terraform to VPC, IAM and EKS

This project intentionally avoids a database and external APIs so you can focus on DevOps concepts rather than application complexity.
