import requests
import dateutil.tz
from datetime import datetime



def send_message(blue: str, usdt: str, chat_id: str, token: str):
    #Gets formatted time info
    actual_time = datetime.now(tz=dateutil.tz.gettz("America/Argentina/Buenos_Aires"))
    formatted_time = actual_time.strftime("%d/%m %H:%M")
    
    msg = formatted_time + "\n" + "Blue: $" + blue + "\n" + "USDT: $" + usdt
    url = 'https://api.telegram.org/bot' + token + '/sendMessage?chat_id=' + chat_id + '&parse_mode=Markdown&text=' + msg

    #response with message data
    response = requests.get(url).json()
    msg_id = str(response['result']['message_id'])           
    return response, msg_id
