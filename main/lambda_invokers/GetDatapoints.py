import boto3
import datetime

#Constants
OPENING = 10
CLOSING = 18

def get_weekly_data(table_name, date_friday_str):
    dynamodb = boto3.resource('dynamodb', region_name="us-east-2")
    table = dynamodb.Table(table_name)

    date_friday = datetime.datetime.strptime(date_friday_str, "%d.%m.%Y:%H.%M")
    
    date_monday = date_friday - datetime.timedelta(days=4)
    
    start_timestamp = int(date_monday.timestamp())
    end_timestamp = int(date_friday.timestamp())

    response = table.scan(
        FilterExpression="unix_date BETWEEN :start_timestamp AND :end_timestamp",
        ExpressionAttributeValues={
            ":start_timestamp": start_timestamp,
            ":end_timestamp": end_timestamp
        }
    )

    return response['Items']

def get_monthly_data(table_name, date_end_month_str):

    dynamodb = boto3.resource("dynamodb", region_name="us-east-2")
    table = dynamodb.Table(table_name)

    date_end_month = datetime.datetime.strptime(date_end_month_str, "%d.%m.%Y:%H.%M")
    date_start_month = date_end_month.replace(day=1, hour=OPENING, minute=0, second=0, microsecond=0)

    start_timestamp = int(date_start_month.timestamp())
    end_timestamp = int(date_end_month.timestamp())

    response = table.scan(
        FilterExpression="unix_date BETWEEN :start_timestamp AND :end_timestamp",
        ExpressionAttributeValues={
            ":start_timestamp": start_timestamp,
            ":end_timestamp": end_timestamp
        }
    )

    return response['Items']


    

