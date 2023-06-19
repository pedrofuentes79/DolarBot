import boto3
import json

def ReadDynamoDB_invoker(table_name, dt):
    '''
    Given a dt object, this function returns the entry that corresponds 
    with the date_int of that dt object
    '''
    dynamodb = boto3.resource('dynamodb', region_name='us-east-2')
    table_name = table_name
    
    table = dynamodb.Table(table_name)
        
    date_int = int(dt.timestamp())

    response = table.get_item(
        Key={
            'unix_date': date_int
        },
        ProjectionExpression="price"
        )
    
    return response