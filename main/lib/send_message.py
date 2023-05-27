import requests
import dateutil.tz
from datetime import datetime
from lib.last_price_utils import get_up_down_emoji



def send_message(blue: str, usdt: str, chat_id: str, token: str, date_str: str):
    #Gets formatted time info for the message (could put this into the date_utils.py module)
    actual_time = datetime.now(tz=dateutil.tz.gettz("America/Argentina/Buenos_Aires"))
    message_formatted_time = actual_time.strftime("%d/%m %H:%M")
    
    #Up/Down emoji
    emoji = get_up_down_emoji(date_str=date_str
                              current_price_blue=blue, 
                              current_price_usdt=usdt)
    
    msg = message_formatted_time + "\n" + "Blue: $" + blue + "\n" + "USDT: $" + usdt
    url = 'https://api.telegram.org/bot' + token + '/sendMessage?chat_id=' + chat_id + '&parse_mode=Markdown&text=' + msg

    #response with message data
    response = requests.get(url).json()
    msg_id = str(response['result']['message_id'])           
    return response, msg_id
