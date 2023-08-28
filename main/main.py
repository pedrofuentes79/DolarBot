from lib.get_blue import get_blue
from lib.date_utils import get_formatted_date, holiday, is_friday_last_hour, is_end_month
from lib.send_message import send_message, send_chart
from lib.get_p2p_ars_price import get_p2p_ars_price
from lib.chart import get_weekly_chart, get_monthly_chart
from lib.get_chart_data import get_weekly_data, get_monthly_data

from lambda_invokers.WriteDynamoDB_invoker import WriteDynamoDB_invoker

import os
import json
import datetime


def lambda_handler(event, context):
    #Keys
    CHAT_ID = os.environ.get("TELEGRAM_CHANNEL_ID")
    DOLAR_SCRAPER_TOKEN = os.environ.get("TELEGRAM_API_DOLAR_SCRAPER_TOKEN")
    

    
    #formatted dates
    date_dt, date_str, date_int = get_formatted_date()

    if is_friday_last_hour(date_dt):
        weekly_data = get_weekly_data("blue_prices", date_str)
        weekly_chart_buffer = get_weekly_chart(weekly_data)
        response_chart = send_chart(weekly_chart_buffer, DOLAR_SCRAPER_TOKEN, CHAT_ID)
        print(response_chart)
        
    if is_end_month(date_dt):
        monthly_data = get_monthly_data("blue_prices", date_str)
        monthly_chart_buffer = get_monthly_chart(monthly_data)
        response_monthly_chart = send_chart(monthly_chart_buffer, DOLAR_SCRAPER_TOKEN, CHAT_ID)
        print(response_monthly_chart)

    # NEED TO CHANGE ALL DATE FUNCTIONS TO RECEIVE DT OBJECTS INSTEAD OF DATE_STR
    if not holiday(date_str):
        #Gets sell values
        _, blue = get_blue()
        usdt = get_p2p_ars_price(mercado_pago=True, date_str=date_str)
        
        #stores the date (as a timestamp int), date string (for legibility), price and type of value in the DynamoDB tables respectively
        WriteDynamoDB_invoker(date_int=date_int, date_str=date_str, price=blue, type_of_value="sell", table_name="blue_prices"),
        WriteDynamoDB_invoker(date_int=date_int, date_str=date_str, price=usdt, type_of_value="sell", table_name="usdt_prices")
        
        #Sends the message to the chat id
        response = send_message(blue, usdt, date_str, CHAT_ID, DOLAR_SCRAPER_TOKEN)
        
        print(response)    
        return {
            'statusCode': 200,
            'body': json.dumps(response)
        }
    else:
        return {
            'statusCode': 200,
            'body': json.dumps("It's a holiday!")
        }