# A word about operators

* Operators are custom controllers...more exactly: A **operator** is a set of **CRD**s and a a set of **controllers**.
* Controllers are the core of Kubernetes, and of any operator.
* The OLM (Operator Lifecycle Manager) helps users install, update, and manage operators in the cluster.

# literate-operator
K8S operator that aggregates logs from all pods with label defined in the `target` field of `LogDrain` object
Create some targets:
```bash
# spin up some naked pods
kubectl run pod1 --image=nginx:stable-perl --port=80 --labels='target=kcd'

kubectl run pod3 --image=dejanualex/python_hello:1.0  --labels='target=kcd'
```

## Local setup

```bash
# create .venv virtual environment
python3 -m venv .venv
. .venv/bin/activate
pip install -r requirements.txt
```
* Docker operator image: `docker pull dejanualex/literate-operator:1.26`

## Steps

```bash
# Apply crds : 
kubectl apply -f k8s
# Check resources: 
kubectl api-resources | grep dev
# Explain objects
kubectl get ld
kubectl explain logdrain
```

## Sources

* [pykube](https://pykube.readthedocs.io/en/latest/index.html) for writing the [operator](https://pykube.readthedocs.io/en/latest/howtos/write-an-operator.html)

* Framework for building Operators… [Kubebuilder](https://github.com/kubernetes-sigs/kubebuilder) is a good option since [Operator SDK](https://sdk.operatorframework.io/) uses [Kubebuilder under the hood](https://sdk.operatorframework.io/docs/faqs/#what-are-the-the-differences-between-kubebuilder-and-operator-sdk).

* The registry for K8S operators [OperatorHub.io](https://operatorhub.io/)