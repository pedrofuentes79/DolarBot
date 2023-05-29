import requests
from lib.last_price_utils import get_emojis
from lib.date_utils import get_message_formatted_date



def send_message(blue: str, usdt: str, chat_id: str, token: str, date_str: str):
    
    #gets specific format for current date
    message_formatted_date = get_message_formatted_date(date_str)

    #Up/Down emoji
    blue_emoji, usdt_emoji = get_emojis(date_str=date_str,
                                        current_price_blue=float(blue), 
                                        current_price_usdt=float(usdt))
    

    #puts together all the pieces to form the final message string
    msg = message_formatted_date + "\n" + "Blue: $" + blue + blue_emoji +"\n" + "USDT: $" + usdt + usdt_emoji
    
    #puts together all the pieces to form the telegram url
    url = 'https://api.telegram.org/bot' + token + '/sendMessage?chat_id=' + chat_id + '&parse_mode=Markdown&text=' + msg

    #response with message data
    response = requests.get(url).json()
    msg_id = str(response['result']['message_id'])           
    return response, msg_id
