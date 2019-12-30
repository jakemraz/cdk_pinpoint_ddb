from aws_cdk import core, aws_dynamodb, aws_lambda, aws_apigateway, aws_iam
from lambda_fn import config

class CdkPinpointDdbStack(core.Stack):

    def __init__(self, scope: core.Construct, id: str, **kwargs) -> None:
        super().__init__(scope, id, **kwargs)

        # DDB
        table = aws_dynamodb.Table(self, "pinpoint_category",
            partition_key = aws_dynamodb.Attribute(name="category",type=aws_dynamodb.AttributeType.STRING),
            sort_key = aws_dynamodb.Attribute(name="event_time",type=aws_dynamodb.AttributeType.NUMBER)
            )
        
        # LAMBDA
        function = aws_lambda.Function(self, "pinpoint_send_campaign",
            runtime=aws_lambda.Runtime.PYTHON_3_7,
            handler="pinpoint_campaign_handler.lambda_handler",
            code=aws_lambda.Code.asset("./lambda_fn"),
            environment={
                'CATEGORY_TABLE_NAME': table.table_name
            })
        table.grant_read_write_data(function)
        lambdaPinpointSendCampaignRole = function.role
        pinpoint_project_arn = "arn:aws:mobiletargeting:" + self.region + ":" + self.account + ":apps/" + config.PINPOINT_CONFIG['application_id']
        pinpointSendCampaignPolicyStatement = aws_iam.PolicyStatement(
            actions=[
                "mobiletargeting:CreateCampaign",
                "mobiletargeting:GetSegments",
                "mobiletargeting:GetSegment"
            ],
            resources=[
                pinpoint_project_arn
            ],
            effect=aws_iam.Effect.ALLOW
        )

        lambdaPinpointSendCampaignRole.add_to_policy(pinpointSendCampaignPolicyStatement)

        # API Gateway
        api = aws_apigateway.LambdaRestApi(self, "apiSendCampaign", handler=function)

