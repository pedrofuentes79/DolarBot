import boto3
from datetime import datetime as dt
import pytz

#Constants
OPENING = 10
CLOSING = 17

def get_weekly_data(table_name, date_friday_str):
    dynamodb = boto3.resource('dynamodb', region_name="us-east-2")
    table = dynamodb.Table(table_name)

    date_friday = dt.strptime(date_friday_str, "%d.%m.%Y:%H.%M")
    date_monday = date_friday.replace(day=date_friday.day-4, hour=OPENING, minute=0, second=0, microsecond=0)
    
    date_friday_with_tz = date_friday.replace(tzinfo=pytz.timezone("America/Argentina/Buenos_Aires"))
    date_monday_with_tz = date_monday.replace(tzinfo=pytz.timezone("America/Argentina/Buenos_Aires"))
    
    start_timestamp = int(date_monday_with_tz.timestamp())
    end_timestamp = int(date_friday_with_tz.timestamp())

    
    response = table.scan(
        FilterExpression="unix_date BETWEEN :start_timestamp AND :end_timestamp",
        ExpressionAttributeValues={
            ":start_timestamp": start_timestamp,
            ":end_timestamp": end_timestamp
        },
        ConsistentRead=True
    )

    return response['Items']

def get_monthly_data(table_name, date_end_month_str):

    dynamodb = boto3.resource("dynamodb", region_name="us-east-2")
    table = dynamodb.Table(table_name)

    date_end_month = dt.strptime(date_end_month_str, "%d.%m.%Y:%H.%M")
    date_start_month = date_end_month.replace(day=1, hour=OPENING, minute=0, second=0, microsecond=0)
    
    # replace with local tz
    date_end_month_with_tz = date_end_month.replace(tzinfo=pytz.timezone("America/Argentina/Buenos_Aires"))
    date_start_month_with_tz = date_start_month.replace(tzinfo=pytz.timezone("America/Argentina/Buenos_Aires"))

    # convert to timestamp
    start_timestamp = int(date_start_month_with_tz.timestamp())
    end_timestamp = int(date_end_month_with_tz.timestamp())
    
    # scan between start and end of the month.
    response = table.scan(
        FilterExpression="unix_date BETWEEN :start_timestamp AND :end_timestamp",
        ExpressionAttributeValues={
            ":start_timestamp": start_timestamp,
            ":end_timestamp": end_timestamp
        }
    )

    return response['Items']

