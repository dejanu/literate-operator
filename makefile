.DEFAULT_GOAL := documentation

documentation:
	@echo "showapi"
	@echo "nakedpod"
	@echo "rawuri"
	@echo "curl"
	@echo "apiserver"
	@echo "sa"
	@echo "binding"
	@echo "token"
	@echo "ca"
	@echo "cleanup"

showapi:
	@echo "kubectl api-resources"
	
rawuri:
	@echo "kubectl get --raw /api/v1/namespaces/default/pods"

nakedpod:
	@echo "kubectl run demo --image=nginx"

curl:
	@echo "curl --cacert ca.crt --header \"Authorization: Bearer \$$TOKEN\" \$$API_SERVER/api/v1/namespaces/default/pods"

apiserver:
	# same info with kubectl cluster-info
	@echo "API_SERVER=\$$(kubectl config view --raw --minify --flatten -ojsonpath='{.clusters[].cluster.server}')"

sa:
	@echo "kubectl create sa api-access"

binding: 
	@echo "kubectl create clusterrolebinding api-access-binding --clusterrole=cluster-admin --serviceaccount=default:api-access"

token:
	@echo "TOKEN=\$$(kubectl create token api-access --duration=24h)"

ca:
	@echo "kubectl config view --raw --minify --flatten \
-ojsonpath='{.clusters[].cluster.certificate-authority-data}' | base64 --decode > ca.crt"

cleanup:
	@echo "kubectl delete sa api-access"
	@echo "kubectl delete clusterrolebinding api-access-binding"
