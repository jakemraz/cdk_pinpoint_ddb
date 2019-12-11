import json
import boto3
import os
import datetime
from botocore.exceptions import ClientError
import config
import pinpoint
import ddb
import dateutil
 

def send_push(title, message, segment, icon_url, image_url):
    application_id = config.PINPOINT_CONFIG['application_id']
    print(application_id)
    pp = pinpoint.Pinpoint(application_id)
    segment_id = pp.get_segment_id(segment)
    return pp.create_campaign(title, message, segment_id, icon_url, image_url)

def insert_category(campaign_id, category, create_timestamp):
    db = ddb.Ddb(os.environ['CATEGORY_TABLE_NAME'])
    item = {
        "category": category,
        "event_time": create_timestamp,
        "campaign_id": campaign_id
    }
    return db.put_item(item)


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
    category = event["category"]
 
    # Pinpoint
    campaign_response = send_push(title, message, segment, icon_url, image_url)
    
    # Insert Category into DDB
    campaign_id = campaign_response['CampaignResponse']['Id']
    create_date = campaign_response['CampaignResponse']['CreationDate']
    create_timestamp = int(dateutil.parser.parse(create_date).timestamp())
    insert_category(campaign_id, category, create_timestamp)    

    return {
        'statusCode': 200,
        'body': json.dumps({'result': campaign_response}),
        'headers': {
            'Content-Type': 'application/json',
            'Access-Control-Allow-Origin': '*'
        }
    }