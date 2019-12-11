import boto3

class Ddb:
    def __init__(self, table_name):
        self.table_name = table_name
        self.dynamodb = boto3.resource('dynamodb')
        self.table = self.dynamodb.Table(table_name)
    def put_item(self, item):
        
        response = self.table.put_item(
            Item = item
        )

        return response
