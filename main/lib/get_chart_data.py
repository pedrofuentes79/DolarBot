import boto3
from datetime import datetime as dt
from constants import OPENING, CLOSING

def get_weekly_data(table_name, date_friday):
    dynamodb = boto3.resource('dynamodb', region_name="us-east-2")
    table = dynamodb.Table(table_name)

    date_monday = date_friday.replace(day=date_friday.day-4, hour=OPENING, minute=0, second=0, microsecond=0)
    
    # get the timestamp with some seconds of margin
    start_timestamp = int(date_monday.timestamp())
    end_timestamp = int(date_friday.timestamp())

    
    response = table.scan(
        FilterExpression="unix_date BETWEEN :start_timestamp AND :end_timestamp",
        ExpressionAttributeValues={
            ":start_timestamp": start_timestamp,
            ":end_timestamp": end_timestamp
        },
        ConsistentRead=True
    )

    return response['Items']

def get_monthly_data(table_name, date_end_month):

    dynamodb = boto3.resource("dynamodb", region_name="us-east-2")
    table = dynamodb.Table(table_name)

    date_start_month = date_end_month.replace(day=1, hour=OPENING, minute=0, second=0, microsecond=0)

    # convert to timestamp with some seconds of margin
    start_timestamp = int(date_start_month.timestamp())
    end_timestamp = int(date_end_month.timestamp())
    
    # scan between start and end of the month.
    response = table.scan(
        FilterExpression="unix_date BETWEEN :start_timestamp AND :end_timestamp",
        ExpressionAttributeValues={
            ":start_timestamp": start_timestamp,
            ":end_timestamp": end_timestamp
        }
    )

    return response['Items']

