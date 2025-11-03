#!/usr/bin/env python

import time
import operator
from pykube import KubeConfig, HTTPClient, object_factory, all, Pod
# from deploy import deploy_template

# load Kubernetes configuration from the default location
api = HTTPClient(KubeConfig.from_env())
def main():
    """ operator aka custom loop """
    LogDrain = object_factory(api, "dev.io/v1alpha1", "LogDrain")
    while True:
        # retrieve ld config from pykube.query.Query objects
        loggers = LogDrain.objects(api, namespace=all)
        if not loggers:
            print("No loggerdrain object found....")
        else:
            for a in loggers:
                print ("😍 LogDrain object named {} with specs:{}".format(a, a.obj["spec"]))
                # get value of target label
                value_for_taget_label = [a.obj["spec"].get("target") for a in loggers][0]
                target_pods = Pod.objects(api).filter(namespace=all,selector={'target': value_for_taget_label})
                ready_pods = filter(operator.attrgetter("ready"), target_pods)
                # logger obj exists but no target pod exists
                if not target_pods: #if list is empty
                        print("Scanning for target pods...")
                else:
                    for pod in ready_pods:
                        print("Found it 👀 POD:{1} in namespace --> {0}".format(pod.namespace, pod.name))
                        for container in pod.obj["spec"]["containers"]:
                            container_log = pod.logs(
                            container=container["name"],
                            timestamps=True,
                            tail_lines=10,
                            )
                            time.sleep(1)
                            for line in container_log.split("\n"):
                                print(line)
if __name__ == "__main__":
    main()