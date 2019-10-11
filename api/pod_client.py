from api.base import BaseClass
from kubernetes import client


class PodsClient(BaseClass):

    def get_pods_for_all_namespaces(self):
        BaseClass()
        return client.CoreV1Api().list_pod_for_all_namespaces(watch=False)

    def get_pods_for_all_namespaces_with_http_info(self):
        BaseClass("E:\kubeconfig\config.yaml").load_config()
        return client.CoreV1Api().list_pod_for_all_namespaces_with_http_info(watch=False)

    def get_pods_for_namespace(self, namepace):
        BaseClass("E:\kubeconfig\config.yaml").load_config()
        return client.CoreV1Api().list_namespaced_pod(namepace, watch=False)

    def get_namespaced_pods_with_http_info(self, namespace):
        BaseClass("E:\kubeconfig\config.yaml").load_config()
        return client.CoreV1Api().list_namespaced_pod_with_http_info(namespace, watch=False)
