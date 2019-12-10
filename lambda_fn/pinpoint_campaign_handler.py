import json
import boto3
import os
import datetime
from botocore.exceptions import ClientError
import config
 
# Pinpoint Project Id
application_id = config.PINPOINT_CONFIG['applicatoin_id']
 
region = os.environ['AWS_REGION']
client = boto3.client('pinpoint',region_name=region)
 
def get_segment_id(segment_name):
    try:
        response = client.get_segments(
            ApplicationId=application_id
        )
        segment_list = response['SegmentsResponse']['Item']
        print(segment_list)
        for one in segment_list:
            if one['Name'] == segment_name:
                segment_id = one['Id']
    except ClientError as e:
        print('Error: ', e.response['Error']['Message'])
    else:
        print('segment_id: ', segment_id)
        # print(json.dumps(response))
    return segment_id
 
def create_campaign(title, message, segment_id, icon_url, image_url):
    print(segment_id)
    try:
        response = client.create_campaign(
            ApplicationId=application_id,
            WriteCampaignRequest={
                'MessageConfiguration': {
                    'DefaultMessage': {
                        'Action': 'OPEN_APP',
                        'Body': message,
                        'Title': title,
                        'ImageIconUrl': icon_url,
                        'ImageUrl': image_url
                        # 'ImageUrl': 'http://www.earlyadopter.co.kr/wp-content/uploads/2019/11/apple-airpods-pro-early-adopter-review-1.jpg'
                        # 'MediaUrl': 'https://m.media-amazon.com/images/G/01/kindle/merch/2019/ONTHEGO/19951312/PUGE0013_Amazon_Puget_US_REV_2019_45_HD-forDP.mp4?_=1'
                    },
                },
                'Name': title,
                'Description': "캠페인 메시지",
                'SegmentId': segment_id,
                'Schedule': {
                    'StartTime': "IMMEDIATE"
                    # 'Frequency': 'ONCE',
                    # 'StartTime': datetime.datetime.utcnow().replace(tzinfo=datetime.timezone.utc).isoformat()
                }
            }
        )
    except ClientError as e:
        print(e.response['Error']['Message'])
    else:
        print (json.dumps(response))
 
def lambda_handler(event, context):
    print(event)
    if "body" in event:
        event = json.loads(event['body'])


    # Query parmeters
    title = event["title"]
    message = event["message"]
    segment = event["segment"]
    icon_url = event["icon"]
    image_url = event["image"]
 
    # Pinpoint
    


    segment_id = get_segment_id(segment)
    response = create_campaign(title, message, segment_id, icon_url, image_url)
 
    return {
        'statusCode': 200,
        'body': json.dumps({'result': response}),
        'headers': {
            'Content-Type': 'application/json',
            'Access-Control-Allow-Origin': '*'
        }
    }