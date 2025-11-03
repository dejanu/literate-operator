.DEFAULT_GOAL := documentation

documentation:
	@echo "nodes_api"
	@echo "api_group"
	@echo "ld_object"
	@echo "devgroup"
	@echo "naked_po"
nodes_api:
	@echo "kubectl get --raw /apis/metrics.k8s.io/v1beta1/nodes"
api_group:
	@echo "kubectl api-resources --api-group=metrics.k8s.io"
	@echo "kubectl get --raw /apis/metrics.k8s.io/v1beta1/pods"
ld_object:
	@echo "apiVersion: dev.io/v1alpha1 \nkind: LogDrain \nmetadata: \n  name: demold \nspec: \n  target: \"INSERT_HERE\" "
devgroup:
	@echo "kubectl api-resources --api-group=dev.io"
naked_po:
	@echo "kubectl run pod1 --image=nginx:stable-perl --port=80 --labels='target=stackconf'"
	@echo "kubectl run pod2 --image=dejanualex/gohello:1.0  --labels='target=stackconf'"
svc:
	@echo "kubectl expose pod pod2 --name=mysvc --type=LoadBalancer --port=8888 --target-port=8888"


## never forgetti
# cat<<EOF>>test.yaml
# $(make naked_po)
# EOF

##  documentation at your finger tips
# kubect explain po
# kubectl explain po.status.phase
# kubectl explain po --recursive

## glance at the API
# kubectl get po -v=6

## compute abstraction: top -o cpu
# kubectl top po --sort-by=cpu --containers -A

## peak at the API behind the scenes
# kubectl top no -v=6

## check API Resources aka Kinds
# kubectl api-resources

## get all API Resources/Kinds for a specific group  i.e metrics.k8s.io
#  kubectl api-resources --api-group=metrics.k8s.io

## list of API services that are available and managed by the API server
#  kubectl get apiservices

##  expose API: create a proxy server or application-level gateway between localhost and the k8s API server
# kubectl proxy --port=8080

