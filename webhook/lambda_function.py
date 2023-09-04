import json
import os
import requests
from dynamodb_utils import get_price_data
from send_message import send_message_prices, send_error_message

def lambda_handler(event, context):
    # Get the "dict" that has all info
    request_body = event["body"]

    command = request_body['message']['text'].strip('"') 
    command = command[1:] # Strips "/" character
    
    chat_id = str(request_body['message']['chat']['id'])
    TOKEN = os.environ.get('TELEGRAM_API_DOLAR_SCRAPER_TOKEN')

    if command == 'start':
        message = "Welcome to my bot! How can I help you today?"
    elif command == 'help':
        message = "Here are the available commands: /start, /help"
    elif command.startswith("precio"):
        date_str = command[7:]
        response_prices = get_price_data(date_str, chat_id)
        if response_prices is None:
            send_error_message("La base de datos no tiene datos para la fecha " + date_str, chat_id)
        else:
            opening, closing = response_prices
            send_message_prices(date_str, opening, closing, chat_id)
    
    url = 'https://api.telegram.org/bot' + TOKEN + '/sendMessage?chat_id=' + chat_id + '&parse_mode=HTML&text=' + message
    response = requests.get(url)
    print(response)
    return {
    'statusCode': 200,
    'body': json.dumps('Hello from Lambda!')
    }