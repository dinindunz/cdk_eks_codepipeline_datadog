from aws_cdk import (
    aws_eks as _eks,
    aws_ecr as _ecr,
    aws_ecr_assets as _ecr_assets
)
from constructs import Construct
import cdk_ecr_deployment as _ecr_deployment

class DeployEksCluster(Construct):

    def __init__(self, scope: Construct, id: str, ecr_repo_name: str, image_tag: str, container_port: int, **kwargs) -> None:
        super().__init__(scope, id, **kwargs)

        eks_cluster=_eks.Cluster(
            self, 'eks_cluster',
            version=_eks.KubernetesVersion.V1_21
        )

        eks_cluster.add_manifest('mypod', {
            'api_version': 'v1',
            'kind': 'Pod',
            'metadata': {'name': 'mypod'},
            'spec': {
                'containers': [{
                    'name': 'hello',
                    'image': '%s:%s' % (ecr_repo_name, image_tag),
                    'ports': [{'container_port': container_port}]
                }
                ]
            }
        })
