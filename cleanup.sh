#!/usr/bin/env bash

kubectl delete  sa api-access
kubectl delete  clusterrolebinding api-access-binding