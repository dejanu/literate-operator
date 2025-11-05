.DEFAULT_GOAL := documentation

documentation:
	@echo "SHOW OBJECTS 😉"
	@echo "deploy"
	@echo "qos"
	@echo "apigroup"
	@echo "qs"
	@echo "qs_object"
	
deploy:
	@echo "kubectl create deployment demo --image=nginx"
	@echo "kubectl apply -f demo-guaranteed.yaml"
qos:
	@echo "kubectl get po -ojsonpath={.items[*].status.qosClass}"
apigroup:
	@echo "kubectl api-resources --api-group=dev.io"
qs:
	@echo "kubectl explain qs"
	@echo "kubectl get qs"
qs_object:
	@echo "apiVersion: dev.io/v1alpha1 \nkind: Qos \nmetadata: \n  name: qosfilter \nspec: \n  target: \"Guaranteed\" "


## never forgetti
# cat<<EOF>>test.yaml
# $(make qs_object)
# EOF

