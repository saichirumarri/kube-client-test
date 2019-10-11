from kubernetes import config,client
import sys


class BaseClass:

    def __init__(self):
        """ Kube config file should be placed in /root/.kube folder with config as name for linux """
        self.path = "/.minikube/machines/minikube/config.json"
        configuration = client.Configuration()
        configuration.host = "localhost:8888"
        api_client = client.CoreV1Api(client.ApiClient(configuration))
        config.load_kube_config(config_file=self.path)
