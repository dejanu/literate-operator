# literate-operator
K8S operator that kills pods

## Local setup

```bash
# create .venv virtual environment
python3 -m venv .venv
. .venv/bin/activate
pip install -r requirements.txt
```

## Steps

```bash
#Apply crds : 
kubectl apply -f k8s
#check resources: 
kubectl api-resources | grep chaos
#check objects using short names
kubectl get chaosagents.blackadder.io
kubectl get ca
```
