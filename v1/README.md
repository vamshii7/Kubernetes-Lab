Kubernetes Lab

This repo contains a simple Flask web app deployed to a kind cluster with ConfigMap, Secret, HPA, and NetworkPolicy.

## Quick Start

```bash
# Build image
docker build -t flask-app:latest ./app

# Create kind cluster
kind create cluster

# Load image to kind
kind load docker-image flask-app:latest --name <cluster-name>

# Deploy manifests
kubectl apply -f manifests/
```

Access the service:

```bash
kubectl port-forward svc/flask-service 8080:80
# browse http://localhost:8080
```
