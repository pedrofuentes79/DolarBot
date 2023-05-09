import json
import boto3

# define the AWS service and region
dynamodb = boto3.resource('dynamodb', region_name='us-east-2')

# define the name of your DynamoDB table
table_name = 'DolarBot'

# define the Lambda handler function
def lambda_handler(event, context):

    # get the data from the event
    data = json.loads(json.dumps(event['body']))

    # get a reference to the DynamoDB table
    table = dynamodb.Table(table_name)

    # put the item into the DynamoDB table
    response = table.put_item(Item=data)

    # return the response to the client
    return {
        'statusCode': 200,
        'body': json.dumps(response)
    }