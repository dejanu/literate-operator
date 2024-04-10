#!/usr/bin/env python
import munch
from pykube import KubeConfig, HTTPClient, object_factory, all

# load Kubernetes configuration from the default location
api = HTTPClient(KubeConfig.from_env())

# Dynamically builds a Python class for the given Kubernetes object in an API(api,group_version,kind)
ChaosAgent = object_factory(api, "blackadder.io/v1alpha1", "ChaosAgent")

# retrieve ca config from pykube.query.Query objects
agents = ChaosAgent.objects(api, namespace=all)
for a in agents:
    print ("ChaosAgent object named {} with specs:{}".format(a, a.obj["spec"]))



