#!/usr/bin/env python
from pykube import KubeConfig, HTTPClient, object_factory, all, Pod

# load Kubernetes configuration from the default location
api = HTTPClient(KubeConfig.from_env())

# Dynamically builds a Python class for the given Kubernetes object in an API(api,group_version,kind)
ChaosAgent = object_factory(api, "blackadder.io/v1alpha1", "ChaosAgent")

# retrieve ca config from pykube.query.Query objects
# agents = ChaosAgent.objects(api, namespace=all)
# for a in agents:
#     print ("ChaosAgent object named {} with specs:{}".format(a, a.obj["spec"]))


def main():
    """ operator aka custom loop """
    while True:
        for pod in Pod.objects(api).filter(namespace=all,selector={'target': 'yes'}):
            print("Found the little fucker {1} in namespace {0}".format(pod.namespace, pod.name)


if __name__ == "__main__":
    print ("This is blackadder version 1.0.0")
    main()
