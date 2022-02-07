from aws_cdk import (
    aws_eks as _eks,
    aws_ec2 as _ec2
)
from constructs import Construct

class DeployEksCluster(Construct):

    def __init__(self, scope: Construct, id: str, ecr_repo_name: str, image_tag: str, container_port: int, **kwargs) -> None:
        super().__init__(scope, id, **kwargs)

        #Deploy Cluster
        eks_cluster=_eks.Cluster(
            self, '%s-Cluster' % id,
            cluster_name='%s-Cluster' % id,
            version=_eks.KubernetesVersion.V1_21,
            default_capacity=2,
            default_capacity_instance=_ec2.InstanceType.of(_ec2.InstanceClass.BURSTABLE2, _ec2.InstanceSize.MICRO)
        )

        #Deploy the App
        eks_cluster.add_manifest("mypod", {
            "apiVersion": "v1",
            "kind": "Pod",
            "metadata": {"name": "mypod"},
            "spec": {
                "containers": [{
                    "name": "hello",
                    "image": "%s:%s" % (ecr_repo_name, image_tag),
                    "ports": [{"container_port": container_port}]
                }
                ]
            }
        })
