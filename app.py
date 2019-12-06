#!/usr/bin/env python3

from aws_cdk import core

from cdk_pinpoint_ddb.cdk_pinpoint_ddb_stack import CdkPinpointDdbStack


app = core.App()
CdkPinpointDdbStack(app, "cdk-pinpoint-ddb")

app.synth()
