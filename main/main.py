from lib.get_blue import get_blue
from lib.date_utils import get_formatted_date, holiday, is_friday_last_hour, is_end_month
from lib.send_message import send_message, send_chart
from lib.get_p2p_ars_price import get_p2p_ars_price
from lib.chart import get_weekly_chart, get_monthly_chart
from lib.get_chart_data import get_weekly_data, get_monthly_data

from lambda_invokers.WriteDynamoDB_invoker import WriteDynamoDB_invoker

import os
import json

def lambda_handler(event, context):
    #Keys
    CHAT_ID = os.environ.get("TELEGRAM_CHANNEL_ID")
    DOLAR_SCRAPER_TOKEN = os.environ.get("TELEGRAM_API_DOLAR_SCRAPER_TOKEN")
    
    # Get current date in different formats
    date_dt, date_str, date_int = get_formatted_date()

    # If its not a holiday, send usual message.
    if not holiday(date_dt):
        # Gets values
        _, blue = get_blue()
        usdt = get_p2p_ars_price(mercado_pago=True, date_dt=date_dt)
        
        # Stores the date (as a timestamp int), date string (for legibility), price and type of value in the DynamoDB tables respectively
        WriteDynamoDB_invoker(date_int=date_int, date_str=date_str, price=blue, type_of_value="sell", table_name="blue_prices"),
        WriteDynamoDB_invoker(date_int=date_int, date_str=date_str, price=usdt, type_of_value="sell", table_name="usdt_prices")
        
        #Sends the message to the chat id
        response = send_message(blue, usdt, date_dt, CHAT_ID, DOLAR_SCRAPER_TOKEN)
    
        # Friday last hour graph check
        if is_friday_last_hour(date_dt):
            weekly_data = get_weekly_data("blue_prices", date_dt)
            weekly_chart_buffer = get_weekly_chart(weekly_data)
            response_chart = send_chart(weekly_chart_buffer, DOLAR_SCRAPER_TOKEN, CHAT_ID)
            print(response_chart)
        
        # End of month graph check
        if is_end_month(date_dt):
            monthly_data = get_monthly_data("blue_prices", date_dt)
            monthly_chart_buffer = get_monthly_chart(monthly_data)
            response_monthly_chart = send_chart(monthly_chart_buffer, DOLAR_SCRAPER_TOKEN, CHAT_ID)
            print(response_monthly_chart)

        return {
            'statusCode': 200,
            'body': json.dumps(response)
        }
    else:
        # If it's a holiday, don't send any messages
        return {
            'statusCode': 200,
            'body': json.dumps("It's a holiday!")
        }