from lambda_invokers.ReadDynamoDB_invoker import ReadDynamoDB_invoker
from lib.date_utils import get_one_hour_less
import json

def get_previous_prices(date_str: str):
    
    previous_date_str = get_one_hour_less(date_str)
    #gets last entries
    last_entry_blue = ReadDynamoDB_invoker(table_name="blue_prices", date_str=previous_date_str, limit=1)
    last_entry_usdt = ReadDynamoDB_invoker(table_name="usdt_prices", date_str=previous_date_str, limit=1)
    
    #gets last prices
    try:
        last_price_blue_str = json.loads(last_entry_blue["body"])["Item"]["price"]
        last_price_usdt_str = json.loads(last_entry_usdt["body"])["Item"]["price"]
    except IndexError:
        last_price_blue_str = "0"
        last_price_usdt_str = "0"
        
    
    #string to float
    last_price_blue= float(last_price_blue_str)
    last_price_usdt = float(last_price_usdt_str)
    
    return last_price_blue, last_price_usdt






def get_emojis(date_str: str, current_price_usdt: int, current_price_blue: int):

    last_price_blue, last_price_usdt = get_previous_prices(date_str=date_str)
    
    emoji_blue: str
    emoji_usdt: str
    
    if current_price_blue > last_price_blue:     emoji_blue = "📈"
    elif current_price_blue == last_price_blue:  emoji_blue = "🟰"
    else:                                        emoji_blue = "📉"
        
    if current_price_usdt > last_price_usdt:     emoji_usdt = "📈"
    elif current_price_usdt == last_price_usdt:  emoji_usdt = "🟰"
    else:                                        emoji_usdt = "📉"
    
    return emoji_blue, emoji_usdt