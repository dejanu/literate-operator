
# literate-operator
K8S operator that aggregates logs from all pods with label defined in the `target` field of `LogDrain` object
Create some targets:
```bash
# spin up some naked pods
kubectl run pod1 --image=nginx:stable-perl --port=80 --labels='target=stackconf'

kubectl run pod2 --image=dejanualex/pythonhello:1.0  --labels='target=stackconf'
kubectl expose po pod2 --name=websvc --type=LoadBalancer --port=8888 --target-port=8888

kubectl get po --show-labels
```

## Local setup

```bash
# create .venv virtual environment
python3 -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
```
* Docker operator image: `docker pull dejanualex/literate-operator:1.26`

## Steps

```bash
# Apply crds : 
kubectl apply -f k8s

# Check api-group: 
kubectl api-resources | grep dev
kubectl api-resources --api-group=dev.io

# Explain objects
kubectl get ld
kubectl explain logdrain
```