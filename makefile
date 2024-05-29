.DEFAULT_GOAL := documentation

documentation:
	@echo "nodes_api"
	@echo "api_group"
	@echo "ld_object"
	@echo "naked_po"
	@echo "another_naked_po"
nodes_api:
	@echo "kubectl get --raw /apis/metrics.k8s.io/v1beta1/nodes"
ld_object:
	@echo "apiVersion: dev.io/v1alpha1 \nkind: LogDrain \nmetadata: \n  name: demold \nspec: \n  target: \"INSERT_HERE\" "
naked_po:
	@echo "kubectl run pod1 --image=nginx:stable-perl --port=80 --labels='target=kcd'"
api_group:
	@echo "kubectl api-resources --api-group=metrics.k8s.io"
	@echo "kubectl get --raw /apis/metrics.k8s.io/v1beta1/pods"
another_naked_po:
	@echo "kubectl run pod2 --image=dejanualex/python_hello:1.0  --labels='target=kcd'"

# --> documentation at your finger tips
# kubect explain po
# kubectl explain po.status.phase
# kubectl explain po --recursive

# --> compute abstraction: top -o cpu
# kubectl top po --sort-by=cpu --containers -A

# --> peak at the API behind the scenes
# kubectl top no -v=6

# --> check API Resources aka Kinds
# kubectl api-resources

# get all API Resources/Kinds for a specific group  i.e metrics.k8s.io
# --> kubectl api-resources --api-group=metrics.k8s.io

# list of API services that are available and managed by the API server
# --> kubectl get apiservices

# Expose API: create a proxy server or application-level gateway between localhost and the Kubernetes API server
# kubectl proxy --port=8080
