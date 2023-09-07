import json
import os
import requests
import datetime

from prices import get_price_data, get_today_price
from send_message import send_message_prices, send_message, send_current_prices

def lambda_handler(event, context):
    # Get the "dict" that has all info
    request_body = json.loads(event["body"])
    
    if "message" in request_body:
        command = request_body['message']['text'].strip('"')
        chat_id = str(request_body['message']['chat']['id'])
    elif "edited_message" in request_body:
        command = request_body['edited_message']['text'].strip('"')
        chat_id = str(request_body['edited_message']['chat']['id'])
    else:
        return {'statusCode': 400, 'body': json.dumps("Did not recognize a message")} 
    
    commands_dict = json.load(open('commands.json', 'r'))
    
    command = command.lower() # lowercases the command
    
    if command == "start":
        send_message(commands_dict["start"], chat_id)
        return {'statusCode': 200, 'body': json.dumps("Start command")} 
        
    elif command in ["help", "ayuda", "/help", "/ayuda"]:
        send_message(commands_dict["help"], chat_id)
        return {'statusCode': 200, 'body': json.dumps("Help offered")} 
        
    # Caso precio de hoy
    elif command in ["precio", "precio hoy", "precio ", "precio blue", "precio blue hoy", "/precio", "/precio hoy"]:
        blue, usdt = get_today_price()
        
        send_current_prices(blue, usdt, chat_id)
        return {'statusCode': 200, 'body': json.dumps('Current prices sent to ' + chat_id)} 

    elif command.startswith("precio "):
        date_str = command[6:]
        
        response_prices = get_price_data(date_str, chat_id)
        
        if response_prices:
            opening, closing = response_prices
            send_message_prices(date_str, opening, closing, chat_id)
            return {'statusCode': 200, 'body': json.dumps('Prices sent to ' + chat_id)} 
        else:
            return {'statusCode': 400, 'body': json.dumps('Did not find prices or date was wrong')} 
        
    else:
        send_message(commands_dict["error"], chat_id)
        return {'statusCode': 200, 'body': json.dumps("Help offered")} 