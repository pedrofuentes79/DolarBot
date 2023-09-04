import json
import os
import requests
from dynamodb_utils import get_price_data
from send_message import send_message_prices, send_message

def lambda_handler(event, context):
    # Get the "dict" that has all info
    request_body = json.loads(event["body"])
    command = request_body['message']['text'].strip('"') 
    command = command[1:] # Strips "/" character
    
    chat_id = str(request_body['message']['chat']['id'])
    TOKEN = os.environ.get('TELEGRAM_API_DOLAR_SCRAPER_TOKEN')

    if command == 'start':
        send_message("Welcome to my bot! How can I help you today?", chat_id)
    elif command == 'help':
        send_message("Here are the available commands: /start, /help", chat_id)
    elif command.startswith("precio"):
        date_str = command[7:]
        
        response_prices = get_price_data(date_str, chat_id)
        if response_prices:
            opening, closing = response_prices
            send_message_prices(date_str, opening, closing, chat_id)
        
        return {'statusCode': 200, 'body': json.dumps('Prices sent to ' + chat_id)} 
    
    return {'statusCode': 200, 'body': json.dumps('Prices sent to ' + chat_id)} 

