import boto3
import json
    
def WriteDynamoDB_invoker(date="", price=0, type_of_value="", table_name="blue_prices"):
    # defines the client
    client = boto3.client('lambda')
    
    # defines the structure of the payload to be sent 
    payload = json.dumps({
        "body": {
            'date': date,
            'price': price,
            'type_of_value': type_of_value
            },
        "table_name": table_name
        })

    # invoke WriteDynamoDB Lambda
    response = client.invoke(FunctionName="WriteDynamoDB",
                             InvocationType="RequestResponse",
                             Payload=payload)
    return response