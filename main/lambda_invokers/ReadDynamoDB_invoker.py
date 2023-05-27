import boto3
import json
from lib.date_utils import get_one_hour_less

#this doesn't actually invoke a lambda function. I realized it was much easier to do it all in the same function.
#i believe I will temporarily mantain the WriteDynamoDB_invoker but in the future it might be easier to do it all in the same function


def ReadDynamoDB_invoker(table_name: str, date_str: str,limit: int=1):
    dynamodb = boto3.resource('dynamodb', region_name='us-east-2')
    table_name = table_name
    
    table = dynamodb.Table(table_name)
    
    
    last_entry_date_str = get_one_hour_less(date_str)

    response = table.query(
        KeyConditionExpression="#date = :date_val",
        ExpressionAttributeNames={
            "#date": "date"
        },
        ExpressionAttributeValues={
            ":date_val": date_str
        },
        ScanIndexForward=False,  # Sort in descending order
        Limit=1
    )

    
    return {
        'statusCode': 200,
        'body': json.dumps(response)
    }