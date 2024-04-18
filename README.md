# A word about operators

* Operators are custom controllers...more exactly: A **operator** is a set of **CRD**s and a a set of **controllers**.
* Controllers are the core of Kubernetes, and of any operator.
* The OLM (Operator Lifecycle Manager) helps users install, update, and manage operators in the cluster.

# literate-operator
K8S operator that kills/restarts/wip pods with label `{'target': 'yes'}`
Create some targets:
```bash
# spin up some naked pods
kubectl run pod1 --image=ngnix --labels='target=yes'
kubectl run pod2 --image=ngnix --labels='target=no'
```

## Local setup

```bash
# create .venv virtual environment
python3 -m venv .venv
. .venv/bin/activate
pip install -r requirements.txt
```
* Docker operator image: `docker pull dejanualex/literate-operator:1.0`

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

## Sources

* [pykube](https://pykube.readthedocs.io/en/latest/index.html) for writing the [operator](https://pykube.readthedocs.io/en/latest/howtos/write-an-operator.html)

* Framework for building Operators… [Kubebuilder](https://github.com/kubernetes-sigs/kubebuilder) is a good option since [Operator SDK](https://sdk.operatorframework.io/) uses [Kubebuilder under the hood](https://sdk.operatorframework.io/docs/faqs/#what-are-the-the-differences-between-kubebuilder-and-operator-sdk).

* The registry for K8S operators [OperatorHub.io](https://operatorhub.io/)