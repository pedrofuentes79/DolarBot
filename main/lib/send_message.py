import requests
from lib.last_price_utils import get_emojis, get_blue_opening_value, get_closing_emoji
from lib.date_utils import get_message_formatted_date, is_opening_time, is_closing_time

def send_message(blue, usdt, date_dt, chat_id, token):
    # This function sends a message to the telegram channel with the given chat_id and token.
    
    # Initialize values
    if is_opening_time(date_dt):
        # Gets specific format for current date
        message_formatted_date = get_message_formatted_date(date_dt)
        msg = "APERTURA " + message_formatted_date + "\n"
    else:
        msg = ""
    
    # Gets emojis according to previous price
    blue_emoji, usdt_emoji = get_emojis(date_dt=date_dt, current_price_blue=float(blue), current_price_usdt=float(usdt))
    
    # Puts together all the pieces to form the final message string
    msg += "Blue: $" + blue + blue_emoji +"\n" + "USDT: $" + usdt + usdt_emoji
    
    # Puts together all the pieces to form the telegram url
    url = 'https://api.telegram.org/bot' + token + '/sendMessage?chat_id=' + chat_id + '&parse_mode=Markdown&text=' + msg

    # Response with message data
    response = requests.get(url).json()
    
    # Sends special closing message
    if is_closing_time(date_dt):
        
        # Gets the opening value from this day
        blue_opening = get_blue_opening_value(date_dt)
        
        # Gets the emoji for the day
        blue_emoji_closing = get_closing_emoji(opening=float(blue_opening), closing=float(blue))
        
        # Puts pieces together and sends the message
        msg = "CIERRE " + message_formatted_date + blue_emoji_closing +"\n"  + "APERTURA: " + blue_opening + " -> CIERRE: " + blue
        url = 'https://api.telegram.org/bot' + token + '/sendMessage?chat_id=' + chat_id + '&parse_mode=Markdown&text=' + msg
        response = requests.get(url).json()
    
    return response


def send_chart(buffer, token, chat_id):
    # This function sends a chart to the telegram channel with the given chat_id and token.

    # Send chart to telegram
    url = 'https://api.telegram.org/bot' + token + '/sendPhoto?chat_id=' + chat_id + '&parse_mode=Markdown'

    # Send buffer to telegram
    files = {'photo': buffer.getvalue()}
    response = requests.post(url, files=files)
    return response
    