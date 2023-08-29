from lambda_invokers.ReadDynamoDB_invoker import ReadDynamoDB_invoker
from lib.date_utils import get_one_hour_less, get_opening_dt
import json

def get_previous_prices(date_dt):
    
    previous_date = get_one_hour_less(date_dt)
    
    #gets last entries
    last_entry_blue = ReadDynamoDB_invoker(table_name="blue_prices", dt=previous_date)
    last_entry_usdt = ReadDynamoDB_invoker(table_name="usdt_prices", dt=previous_date)
    
    #gets last prices
    last_price_blue_str = last_entry_blue["Item"]["price"]
    last_price_usdt_str = last_entry_usdt["Item"]["price"]
        
    
    #string to float
    last_price_blue= float(last_price_blue_str)
    last_price_usdt = float(last_price_usdt_str)
    
    return last_price_blue, last_price_usdt


def get_emojis(date_dt, current_price_usdt: int, current_price_blue: int):

    last_price_blue, last_price_usdt = get_previous_prices(date_dt)
    
    emoji_blue: str
    emoji_usdt: str
    
    if current_price_blue > last_price_blue:     emoji_blue = "📈"
    elif current_price_blue == last_price_blue:  emoji_blue = "🟰"
    else:                                        emoji_blue = "📉"
        
    if current_price_usdt > last_price_usdt:     emoji_usdt = "📈"
    elif current_price_usdt == last_price_usdt:  emoji_usdt = "🟰"
    else:                                        emoji_usdt = "📉"
    
    return emoji_blue, emoji_usdt

def get_closing_emoji(opening: float, closing:float):
    if closing < opening: return "📉"
    elif closing > opening: return "📈"
    else: return "🟰"

def get_blue_opening_value(date_dt):
    opening_dt = get_opening_dt(date_dt)
    opening_value = ReadDynamoDB_invoker("blue_prices", opening_dt)["Item"]["price"]
    return opening_value
    