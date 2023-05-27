from lambda_invokers.ReadDynamoDB_invoker import ReadDynamoDB_invoker
import json


def get_up_down_emoji(date_str: str, current_price_usdt: int, current_price_blue: int):
    #gets last entries
    last_entry_blue = ReadDynamoDB_invoker(table_name="blue_prices", date_str=date_str, limit=1)
    last_entry_usdt = ReadDynamoDB_invoker(table_name="usdt_prices", date_str=date_str, limit=1)
    
    #gets last prices
    last_price_blue_str = json.loads(last_entry_blue["body"])["Items"][0]["price"]
    last_price_usdt_str = json.loads(last_entry_usdt["body"])["Items"][0]["price"]
    
    #string to float
    last_price_blue= float(last_price_blue_str)
    last_price_usdt = float(last_price_usdt_str)
    
    emoji_blue: str
    emoji_usdt: str
    
    if current_price_blue > last_price_blue: emoji_blue = "📈"
    else:                                    emoji_blue = "📉"
        
    if current_price_usdt > last_price_usdt: emoji_usdt = "📈"
    else:                                    emoji_usdt = "📉"
    
    return (emoji_blue, emoji_usdt)