from aws_cdk import (
    Stack
)
from cdk_constructs import (
    build_ecr_image as ecr,
    deploy_eks_cluster as eks
)
from constructs import Construct

class Deploy(Stack):

    def __init__(self, scope: Construct, id: str, **kwargs) -> None:
        super().__init__(scope, id, **kwargs)

        ecr_repo_name='cdk/eks_app_alpha'
        image_tag='1.0.0'

        ecr.BuildEcrImage(
            self, 'build_ecr_image',
            ecr_repo_name=ecr_repo_name,
            image_tag=image_tag,
            directory='./src/eks_app_alpha',
            account=self.account,
            region=self.region
        )

        eks.DeployEksCluster(
            self, 'deploy_eks_cluster',
            ecr_repo_name=ecr_repo_name,
            image_tag=image_tag,
            container_port=8080
        )

        