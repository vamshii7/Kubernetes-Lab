#!/bin/bash
kind create cluster --name tcs-lab
kubectl cluster-info --context kind-tcs-lab