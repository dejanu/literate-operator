.DEFAULT_GOAL := documentation

documentation:
	@echo "nodes_api"

nodes_api:
	@echo "kubectl get --raw /apis/metrics.k8s.io/v1beta1/nodes"