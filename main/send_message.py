import os
import requests
from datetime import datetime
from binance import get_p2p_ars_price
import pytz

dolar_scraper_token = os.environ.get("TELEGRAM_API_DOLAR_SCRAPER_TOKEN")

def send_message(buy, sell, chat_id):
    #Gets formatted time info
    actual_time = datetime.now(tz=pytz.timezone("America/Argentina/Buenos_Aires"))
    formatted_time = actual_time.strftime("%d/%m %H:%M")

    #Gets USDT - ARS price
    usdt_ars = get_p2p_ars_price(mercado_pago=True)
    
    msg = formatted_time + "\n" + "Blue: $" + sell + "\n" + "USDT: $" + usdt_ars
    url = 'https://api.telegram.org/bot' + dolar_scraper_token + '/sendMessage?chat_id=' + chat_id + '&parse_mode=Markdown&text=' + msg

    #response with message data
    response = requests.get(url).json()
    msg_id = str(response['result']['message_id'])           
    return response, msg_id
