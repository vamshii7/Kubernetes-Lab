# Kubernetes Lab Project

This project demonstrates a full-stack, production-like setup using Kubernetes in a local `kind` cluster, mimicking Azure Kubernetes Service (AKS) best practices.

## 🔧 Stack Overview

- **Frontend & Backend App**: Python (Flask)
- **Containerization**: Docker
- **Kubernetes Components**:
  - ConfigMaps & Secrets
  - Deployment, Service, HPA
  - Health Probes (Liveness & Readiness)
  - Network Policies
  - Ingress (optional)
- **Monitoring**: Prometheus + Grafana (preconfigured)
- **CI/CD**: GitHub Actions workflow
- **IaC**: YAML-based manifests

## 📁 Project Structure

```
.
├── app/
│   ├── app.py
│   └── Dockerfile
├── k8s/
│   ├── configmap.yaml
│   ├── secret.yaml
│   ├── deployment.yaml
│   ├── service.yaml
│   ├── hpa.yaml
│   ├── networkpolicy.yaml
│   └── ingress.yaml (optional)
├── .github/workflows/
│   └── ci-cd.yaml
├── README.md
└── kind-cluster-setup.sh
```

## 🚀 Getting Started

### 1. Start a `kind` cluster locally

```bash
./kind-cluster-setup.sh
```

### 2. Apply Kubernetes manifests

```bash
kubectl apply -f k8s/
```

### 3. Trigger GitHub Actions (CI/CD)

Push code to GitHub → the pipeline builds and redeploys the container to your cluster.

## 🔍 Use Cases Demonstrated

✅ Load different pages with ConfigMap environment variables  
✅ Secrets for sensitive config  
✅ Pod auto-scaling with HPA  
✅ Probes (HTTP, TCP, exec)  
✅ Live monitoring using Prometheus/Grafana  
✅ CI/CD pipeline to build and apply Kubernetes manifests  

## 📈 Monitoring Dashboards

To access Prometheus and Grafana:

```bash
kubectl port-forward svc/grafana 3000:3000 -n monitoring
kubectl port-forward svc/prometheus 9090:9090 -n monitoring
```

## 📌 Author

- **Vamshi Krishna**
- Email: vamshi9849@live
- [LinkedIn](https://www.linkedin.com/in/vamshi7/)
- [GitHub](https://github.com/vamshii7)
