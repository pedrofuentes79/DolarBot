from main.lib.get_blue import get_blue
from main.lib.send_message import send_message
from main.lib.get_p2p_ars_price import get_p2p_ars_price
import os
import json

def lambda_handler(event, context):
    CHAT_ID = os.environ.get("TELEGRAM_CHAT_ID")
    DOLAR_SCRAPER_TOKEN = os.environ.get("TELEGRAM_API_DOLAR_SCRAPER_TOKEN")
    
    #Gets buy and sell values
    _, blue = get_blue()
    usdt = get_p2p_ars_price(mercado_pago=True)
    
    #Sends the message to the chat id
    response, msg_id = send_message(usdt, blue, CHAT_ID, DOLAR_SCRAPER_TOKEN)
    
    print(response)    
    return {
        'statusCode': 200,
        'body': json.dumps(response)
    }