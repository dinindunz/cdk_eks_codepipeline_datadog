#!/usr/bin/env python3
import os
from typing_extensions import Self
import aws_cdk as cdk

from cdk_stacks.cdk_code_pipeline import CdkCodePipelineStack
from common.get_environment import GetEnvironment
from cdk_stacks.eks_app_alpha import Deploy

app=cdk.App()

env=GetEnvironment.aws_enviromnet('tooling')
CdkCodePipelineStack(
    app, 'CDK-Pipeline-EKS-Clusters',
    owner='dinindunz',
    repo='cdk_eks_codepipeline_datadog',
    codestar_con='44b4e080-b081-4541-9d72-64ffe4a69ae1',
    env=env[0],
)

app.synth()
