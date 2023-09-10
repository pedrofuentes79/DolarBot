import boto3
import datetime
from constants import OPENING, CLOSING

def get_weekly_data(table_name, date_friday):
    dynamodb = boto3.resource('dynamodb', region_name="us-east-2")
    table = dynamodb.Table(table_name)

    # Substract 4 days to reach monday. Can't use replace method, it fails on first days of the month.
    date_monday = date_friday - datetime.timedelta(days=4)
    date_monday = date_monday.replace(hour=OPENING, minute=0, second=0, microsecond=0)
    
    # Get the timestamp (unix date)
    start_timestamp = int(date_monday.timestamp())
    end_timestamp = int(date_friday.timestamp())

    # Get the data between the timestamps
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

    # Get the timestamp (unix date)
    start_timestamp = int(date_start_month.timestamp())
    end_timestamp = int(date_end_month.timestamp())
    
    # Get the data between the timestamps
    response = table.scan(
        FilterExpression="unix_date BETWEEN :start_timestamp AND :end_timestamp",
        ExpressionAttributeValues={
            ":start_timestamp": start_timestamp,
            ":end_timestamp": end_timestamp
        }
    )

    return response['Items']

