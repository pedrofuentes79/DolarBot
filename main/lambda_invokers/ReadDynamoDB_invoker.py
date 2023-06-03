import boto3
import json
from lib.date_utils import get_one_hour_less

#this doesn't actually invoke a lambda function. I realized it was much easier to do it all in the same function.
#i believe I will temporarily mantain the WriteDynamoDB_invoker but in the future it might be easier to do it all in the same function


def ReadDynamoDB_invoker(table_name: str, date_str: str, limit: int=1):
    '''
    Given a date_str, this function returns the entry that corresponds
    with the previous entry relative to that date_str
    '''
    dynamodb = boto3.resource('dynamodb', region_name='us-east-2')
    table_name = table_name
    
    table = dynamodb.Table(table_name)
    
    last_entry_date = get_one_hour_less(date_str)
    last_entry_date_int = int(last_entry_date.timestamp())

    response = table.get_item(
        Key={
            'unix_date': last_entry_date_int
        },
        ProjectionExpression="price"
        )
    
    return {
        'statusCode': 200,
        'body': json.dumps(response)
    }