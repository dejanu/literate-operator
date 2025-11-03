package main

import (
	"context"
	"fmt"
	"log"
	"time"

	metav1 "k8s.io/apimachinery/pkg/apis/meta/v1"
	"k8s.io/apimachinery/pkg/apis/meta/v1/unstructured"
	"k8s.io/apimachinery/pkg/runtime/schema"
	"k8s.io/client-go/dynamic"
	"k8s.io/client-go/kubernetes"
	"k8s.io/client-go/rest"
)

func main() {
	fmt.Println("Go Controller - QoS-aware Pod Listing (In-Cluster)")

	// Create in-cluster Kubernetes client configuration
	config, err := rest.InClusterConfig()
	if err != nil {
		log.Fatalf("Error creating in-cluster config: %v", err)
	}

	// Create Kubernetes clientset
	clientset, err := kubernetes.NewForConfig(config)
	if err != nil {
		log.Fatalf("Error creating Kubernetes client: %v", err)
	}

	// Create dynamic client for custom resources
	dynamicClient, err := dynamic.NewForConfig(config)
	if err != nil {
		log.Fatalf("Error creating dynamic client: %v", err)
	}

	// Define the QoS custom resource
	qosGVR := schema.GroupVersionResource{
		Group:    "dev.io",
		Version:  "v1alpha1",
		Resource: "qoses",
	}

	// Main loop
	for {
		fmt.Printf("\n--- Pod List at %s ---\n", time.Now().Format("2006-01-02 15:04:05"))

		// Get target QoS from custom resource
		targetQoS := getTargetQoS(dynamicClient, qosGVR)

		if targetQoS == "" {
			fmt.Println("No QoS custom resource found. Not listing any pods.😟")
		} else {
			fmt.Printf("QoS filter active: showing only pods with QoS class '%s' 👌 \n", targetQoS)

			// List pods in the default namespace
			pods, err := clientset.CoreV1().Pods("default").List(context.TODO(), metav1.ListOptions{})
			if err != nil {
				log.Printf("Error listing pods: %v", err)
			} else {
				filteredPods := 0

				for _, pod := range pods.Items {
					// Filter by QoS if target is specified
					if string(pod.Status.QOSClass) != targetQoS {
						continue
					}

					filteredPods++
					fmt.Printf("%d. Pod Name: %s\n", filteredPods, pod.Name)
					fmt.Printf("   Status: %s\n", pod.Status.Phase)
					fmt.Printf("   QoS Class 🤔: %s\n", pod.Status.QOSClass)
					fmt.Printf("   Node: %s\n", pod.Spec.NodeName)
					fmt.Printf("   Created: %s\n", pod.CreationTimestamp.Time.Format("2006-01-02 15:04:05"))
					fmt.Println()
				}

				if filteredPods == 0 {
					fmt.Printf("No pods found with QoS class '%s' in the default namespace.\n", targetQoS)
				} else {
					fmt.Printf("Total pods displayed: %d\n", filteredPods)
				}
			}
		}

		// Wait 20 seconds before next iteration
		fmt.Println("Waiting 20 seconds before next update...")
		time.Sleep(20 * time.Second)
	}
}

// getTargetQoS retrieves the target QoS class from the custom resource
func getTargetQoS(client dynamic.Interface, gvr schema.GroupVersionResource) string {
	qosList, err := client.Resource(gvr).List(context.TODO(), metav1.ListOptions{})
	if err != nil {
		log.Printf("Error listing QoS resources: %v", err)
		return ""
	}

	if len(qosList.Items) == 0 {
		return ""
	}

	// Use the first QoS resource found
	qosResource := qosList.Items[0]

	// Extract the target field from spec
	spec, found, err := unstructured.NestedMap(qosResource.Object, "spec")
	if err != nil || !found {
		log.Printf("Error getting spec from QoS resource: %v", err)
		return ""
	}

	target, found, err := unstructured.NestedString(spec, "target")
	if err != nil || !found {
		log.Printf("Error getting target from QoS spec: %v", err)
		return ""
	}

	return target
}
