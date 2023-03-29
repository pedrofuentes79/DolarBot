import os
import requests

dolar_scraper_token = os.environ.get("TELEGRAM_API_DOLAR_SCRAPER_TOKEN")

def send_message(buy, sell, chat_id):
    msg = "COMPRA: $" + buy + "\n" + "VENTA: $" + sell
    url = 'https://api.telegram.org/bot' + dolar_scraper_token + '/sendMessage?chat_id=' + chat_id + '&parse_mode=Markdown&text=' + msg

    #response with message data
    response = requests.get(url).json()
    msg_id = str(response['result']['message_id'])           
    return response, msg_id
