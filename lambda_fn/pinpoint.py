import json
import boto3
import datetime
from botocore.exceptions import ClientError
 

class Pinpoint:
    def __init__(self, application_id):
        self.application_id = application_id
        self.client = boto3.client('pinpoint')

    def get_segment_id(self, segment_name):
        try:
            response = self.client.get_segments(
                ApplicationId=self.application_id
            )
            segments = response['SegmentsResponse']['Item']
            for segment in segments:
                if segment['Name'] == segment_name:
                    segment_id = segment['Id']
        except ClientError as e:
            print(e.response['Error']['Message'])
        else:
            print(json.dumps(response))
        return segment_id

    def create_campaign(self, title, message, segment_id, icon_url, image_url):
        try:
            response = self.client.create_campaign(
                ApplicationId=self.application_id,
                WriteCampaignRequest={
                    'MessageConfiguration': {
                        'DefaultMessage': {
                            'Action': 'OPEN_APP',
                            'Body': message,
                            'Title': title,
                            'ImageIconUrl': icon_url,
                            'ImageUrl': image_url                        
                        },
                    },
                    'Name': title,
                    'Description': "Campaign Message", #Can use 'Description' for Category
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
        return response
    
    def get_endpoint(self, endpoint_id):
        response = self.client.get_endpoint(
            ApplicationId = self.application_id, 
            EndpointId = endpoint_id)
        return response