#!/bin/bash
kind create cluster --name k8s-lab
kubectl cluster-info --context kind-k8s-lab
