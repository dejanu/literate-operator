## Controller

Client libraries often handle common tasks such as authentication for you. Most client libraries can discover and use the Kubernetes Service Account to authenticate if the API client is running inside the Kubernetes cluster, or can understand the kubeconfig file format to read the credentials and the API Server address.

## A word about operators

* Operators are custom controllers...more exactly: A **operator** is a set of **CRD**s and a a set of **controllers**.
* When you create a new [CustomResourceDefinition](https://kubernetes.io/docs/tasks/extend-kubernetes/custom-resources/custom-resource-definitions/), the Kubernetes API Server creates a new RESTful resource path for each version you specify.
* Controllers are the core of Kubernetes, and of any operator.
* The OLM (Operator Lifecycle Manager) helps users install, update, and manage operators in the cluster.

## Sources

* [pykube](https://pykube.readthedocs.io/en/latest/index.html) for writing the [operator](https://pykube.readthedocs.io/en/latest/howtos/write-an-operator.html)

* Framework for building Operators… [Kubebuilder](https://github.com/kubernetes-sigs/kubebuilder) is a good option since [Operator SDK](https://sdk.operatorframework.io/) uses [Kubebuilder under the hood](https://sdk.operatorframework.io/docs/faqs/#what-are-the-the-differences-between-kubebuilder-and-operator-sdk).

* The registry for K8S operators [OperatorHub.io](https://operatorhub.io/)