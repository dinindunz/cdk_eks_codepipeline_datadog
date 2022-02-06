from os import environ
import aws_cdk as cdk
from constructs import Construct
from cdk_stacks import(
    eks_app_alpha as EksAppAplpha
)
from common.get_environment import GetEnvironment

class DeployStacks(cdk.Stage):

    def __init__(self, scope: Construct, id: str, aws_account, **kwargs) -> None:
        super().__init__(scope, id, **kwargs)
        
        env=GetEnvironment.aws_enviromnet(aws_account)

        EksAppAplpha.Deploy(self, 'EKS-App-Alpha-%s' % str(aws_account).title(), env=env[0])