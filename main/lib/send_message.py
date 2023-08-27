import requests
from lib.last_price_utils import get_emojis, get_blue_opening_value, get_closing_emoji
from lib.date_utils import get_message_formatted_date, is_opening_time, is_closing_time



def send_message(blue: str, usdt: str, date_str: str, chat_id: str, token: str):
    
    #gets specific format for current date
    message_formatted_date = get_message_formatted_date(date_str)
    
    #initialize values
    if is_opening_time(date_str):
        msg = "APERTURA " + message_formatted_date +"\n"
    else:
        msg = ""
    
    #gets emojis according to previous price
    blue_emoji, usdt_emoji = get_emojis(date_str=date_str, current_price_blue=float(blue), current_price_usdt=float(usdt))
    
    #puts together all the pieces to form the final message string
    msg += "Blue: $" + blue + blue_emoji +"\n" + "USDT: $" + usdt + usdt_emoji
    
    #puts together all the pieces to form the telegram url
    url = 'https://api.telegram.org/bot' + token + '/sendMessage?chat_id=' + chat_id + '&parse_mode=Markdown&text=' + msg

    #response with message data
    response = requests.get(url).json()
    
    #sends special closing message
    if is_closing_time(date_str):
        
        #gets the opening value from this day
        blue_opening = get_blue_opening_value(date_str)
        
        #gets the emoji for the day
        blue_emoji_closing = get_closing_emoji(opening=float(blue_opening), closing=float(blue))
        
        #puts pieces together and sends the message
        msg = "CIERRE " + message_formatted_date + blue_emoji_closing +"\n"  + "APERTURA: " + blue_opening + " -> CIERRE: " + blue
        url = 'https://api.telegram.org/bot' + token + '/sendMessage?chat_id=' + chat_id + '&parse_mode=Markdown&text=' + msg
        response = requests.get(url).json()
    
    return response


def send_chart(buffer, token, chat_id):
    # Send chart to telegram
    url = 'https://api.telegram.org/bot' + token + '/sendPhoto?chat_id=' + chat_id + '&parse_mode=Markdown'

    # Send buffer to telegram
    files = {'photo': buffer.getvalue()}
    response = requests.post(url, files=files)
    return response
    