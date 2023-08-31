from lambda_invokers.ReadDynamoDB_invoker import ReadDynamoDB_invoker
from lib.date_utils import get_one_hour_less, get_opening_dt

def get_previous_prices(date_dt):
    # Returns the previous prices from the DynamoDB tables as floats

    # Gets previous market hour
    previous_date = get_one_hour_less(date_dt)
    
    # Gets entries from previous market hour
    last_entry_blue = ReadDynamoDB_invoker(table_name="blue_prices", dt=previous_date)
    last_entry_usdt = ReadDynamoDB_invoker(table_name="usdt_prices", dt=previous_date)
    
    last_price_blue = float(last_entry_blue["Item"]["price"])
    last_price_usdt = float(last_entry_usdt["Item"]["price"])
    
    return last_price_blue, last_price_usdt


def get_emojis(date_dt, current_price_usdt: int, current_price_blue: int):
    # Returns the emojis for the current price compared to the previous price.

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
    # Returns the emojis for the closing price compared to the opening price.

    if closing < opening: return "📉"
    elif closing > opening: return "📈"
    else: return "🟰"

def get_blue_opening_value(date_dt):
    # Returns the opening value for the blue dollar on the given date_dt.

    opening_dt = get_opening_dt(date_dt)
    opening_value = ReadDynamoDB_invoker("blue_prices", opening_dt)["Item"]["price"]
    return opening_value
    