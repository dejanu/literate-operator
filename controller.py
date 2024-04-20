#!/usr/bin/env python
import operator
from pykube import KubeConfig, HTTPClient, object_factory, all, Pod
# from deploy import deploy_template
import time

# load Kubernetes configuration from the default location
api = HTTPClient(KubeConfig.from_env())

def read_ld_config():
    # Dynamically builds a Python class for the given Kubernetes object in an API(api,group_version,kind)
    LogDrain = object_factory(api, "kcd.io/v1alpha1", "LogDrain")
    # retrieve ld config from pykube.query.Query objects
    loggers = LogDrain.objects(api, namespace=all)
    if loggers:
        # just for first logger object
        for a in loggers:
            print ("💡LogDrain object named {} with specs:{}".format(a, a.obj["spec"]))
            # return the value of target 
            return [a.obj["spec"].get("target") for a in loggers][0]
    else:
        print("No loggerdrain object found....")
        return None


def main():
    """ operator aka custom loop """
    while True:
        value_for_taget_label = read_ld_config()
        if value_for_taget_label:
            time.sleep(1)
            target_pods = Pod.objects(api).filter(namespace=all,selector={'target': value_for_taget_label})
            ready_pods = filter(operator.attrgetter("ready"), target_pods)
            # logger obj exists but no target pod exists
            if not target_pods: #if list is empty
                    print("Scanning for target pods")
            else:
                for pod in ready_pods:
                    print("Found the little fucker {1} in namespace {0}".format(pod.namespace, pod.name))
                    for container in pod.obj["spec"]["containers"]:
                        container_log = pod.logs(
                        container=container["name"],
                        timestamps=True,
                        tail_lines=10,
                        )
                        for line in container_log.split("\n"):
                            print(line)
        else:
            print("Waiting for loggerdrain objects to be created....")

if __name__ == "__main__":
    main()

