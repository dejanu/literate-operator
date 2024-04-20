.DEFAULT_GOAL := documentation

documentation:
	@echo "nodes_api"
	@echo "ld_object"
nodes_api:
	@echo "kubectl get --raw /apis/metrics.k8s.io/v1beta1/nodes"
ld_object:
	@echo "\napiVersion: kcd.io/v1alpha1 \nkind: LogDrain \n metadata: \n\tname: demold \nspec: \n\ttarget: \"kcd\" "