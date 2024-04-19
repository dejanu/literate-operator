
def deploy_template(image):
    ## create deployment spec
    obj = {
        "apiVersion": "apps/v1",
        "kind": "Deployment",
        "metadata": {
            "name": "blackadd-deploy",
            "namespace": "default"
        },
        "spec": {
            "replicas": 1,
            "selector": {
                "matchLabels": {
                    "app": "blackadd"
                }
            },
            "template": {
                "metadata": {
                    "labels": {
                        "app": "blackadd"
                    }
                },
                "spec": {
                    "containers": [
                        {
                            "name": "blackadd",
                            "image": f"{image}",
                            "ports": [
                                {"containerPort": 80}
                            ]
                        }
                    ]
                }
            }
        }
        }
    return obj

if __name__ == "__main__":

    print(deploy_template("nginx"))

