# A word about operators

* Operators are custom controllers...more exactly: A **operator** is a set of **CRD**s and a a set of **controllers**.
* When you create a new [CustomResourceDefinition](https://kubernetes.io/docs/tasks/extend-kubernetes/custom-resources/custom-resource-definitions/), the Kubernetes API Server creates a new RESTful resource path for each version you specify.
* Controllers are the core of Kubernetes, and of any operator.
* The OLM (Operator Lifecycle Manager) helps users install, update, and manage operators in the cluster.

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

## Sources

* [pykube](https://pykube.readthedocs.io/en/latest/index.html) for writing the [operator](https://pykube.readthedocs.io/en/latest/howtos/write-an-operator.html)

* Framework for building Operators… [Kubebuilder](https://github.com/kubernetes-sigs/kubebuilder) is a good option since [Operator SDK](https://sdk.operatorframework.io/) uses [Kubebuilder under the hood](https://sdk.operatorframework.io/docs/faqs/#what-are-the-the-differences-between-kubebuilder-and-operator-sdk).

* The registry for K8S operators [OperatorHub.io](https://operatorhub.io/)