import pytest

from resources.pods import Pods


class Test_Pods_Replicas(Pods):


    def test_get_pods_replicas(self):
        replicas = Pods().get_pods_replicas('kube-system')
        print(replicas)
        # assert replicas,"3 desired | 3 updated | 3 total | 3 available | 0 unavailable"

Test_Pods_Replicas().test_get_pods_replicas()
