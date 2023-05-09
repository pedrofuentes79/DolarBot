import boto3
import json

def WriteDynamoDB_invoker(date, price, type):
    # create a Lambda client
    client = boto3.client('lambda')

    # invoke another Lambda function
    response = client.invoke(
        FunctionName='WriteDynamoDB',
        InvocationType='RequestResponse',
        Payload=json.dumps({
                              "body": {
                                "EW{]Z<RS1=\"4B_xM'.bf/&|I$h;{c\"wFV.NcRWA:": date,
                                "price": price,
                                "type": type
                              }
        })
    )

    # parse and return the response
    data = json.loads(response['Payload'].read())

    return data