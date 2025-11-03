## Start project


```bash
# init project: generate go.mod file (dependency management)
go mod init go-controller

# manage dependencies
go mod tidy

# run 
go run main.go

# build for specific OS/ARCH
go build -o go-controller main.go

# Mac ARM
GOOS=darwin GOARCH=arm64 go build -o bin/hello-world-darwin-arm64

# Linux
GOOS=linux GOARCH=amd64 go build -o bin/hello-world-linux-amd64

# install dependencies
go get k8s.io/client-go@latest
go get k8s.io/apimachinery@latest

# build image
docker build -t dejanualex/go-controller:1.0 .
docker push dejanualex/go-controller:1.0
```


### Operator Purpose

* What the controller does:
    * Looks for QoS custom resources: Uses the dynamic client to query for `qos.dev.io/v1alpha1` resources
    * Extracts target QoS class: Reads the `spec.target` field from the custom resource
    * Filters pods: Only displays pods that match the specified QoS class
    * Graceful fallback: If no QoS resource exists, does not show any pods

```bash
# create deployments with different QoS classes
kubectl create deployment demo --image=nginx
kubectl apply -f demo-guaranteed.yaml

# check QoS class
kubectl get po -ojsonpath={.items[*].status.qosClass}
```

* Deploy the operator and create the custom resource

```bash
# deploy
kubectl apply -f k8s_obj/go-operator-deployment.yaml
kubectl apply -f k8s_obj/rbac.yaml


# check the api group
kubectl api-resources --api-group=dev.io

# extend the APi
kubectl apply -f k8s_obj/qos_crd_v1alpha1.yaml

# check the custom resource definition
kubectl explain qs.spec

# check crd
kubectl get qs 

# create the resource
kubectl apply -f k8s_obj/qos_resource.yaml
```