from lib.get_blue import get_blue
from lib.date_utils import get_formatted_date
from lib.send_message import send_message
from lib.get_p2p_ars_price import get_p2p_ars_price

from lambda_invokers.WriteDynamoDB_invoker import WriteDynamoDB_invoker

import os
import json


def lambda_handler(event, context):
    #Keys
    CHAT_ID = os.environ.get("TELEGRAM_CHAT_ID")
    DOLAR_SCRAPER_TOKEN = os.environ.get("TELEGRAM_API_DOLAR_SCRAPER_TOKEN")
    
    #Gets sell values
    _, blue = get_blue()
    usdt = get_p2p_ars_price(mercado_pago=True)
    
    #formatted date string
    date_str, date_int = get_formatted_date()
    
    #stores the date (as a timestamp int), date string (for legibility) ,price and type of value in the DynamoDB tables respectively
    WriteDynamoDB_invoker(date_int=date_int, date_str=date_str, price=blue, type_of_value="sell", table_name="blue_prices"),
    WriteDynamoDB_invoker(date_int=date_int, date_str=date_str, price=usdt, type_of_value="sell", table_name="usdt_prices")
    
    #Sends the message to the chat id
    response, msg_id = send_message(blue, usdt, date_str, CHAT_ID, DOLAR_SCRAPER_TOKEN)
    
    print(response)    
    return {
        'statusCode': 200,
        'body': json.dumps(response)
    }