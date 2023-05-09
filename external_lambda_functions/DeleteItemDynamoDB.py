import json
import boto3

# define the AWS service and region as well as the table name
dynamodb = boto3.resource('dynamodb', region_name='us-east-2')
table_name = 'DolarBot'

def lambda_handler(event, context):
    
    # get a reference to the DynamoDB table
    table = dynamodb.Table(table_name)
    
    # delete the item from the DynamoDB table
    response = table.delete_item(Key=event["Key"])

    # return the response to the client
    return {
        'statusCode': 200,
        'body': json.dumps(response)
    }