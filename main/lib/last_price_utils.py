from lambda_invokers.ReadDynamoDB_invoker import ReadDynamoDB_invoker
import json

def get_up_down_emoji(date_str: str, current_price_usdt: int, current_price_blue: int):
    #gets last entries
    last_entry_usdt = ReadDynamoDB_invoker(table_name="usdt_prices", date_str=date_str, limit=1)
    last_entry_blue = ReadDynamoDB_invoker(table_name="blue_prices", date_str=date_str, limit=1)
    
    #gets last prices
    last_price_usdt_str = json.loads(last_entry_usdt["body"])["Items"][0]["price"]
    last_price_blue_str = json.loads(last_entry_blue["body"])["Items"][0]["price"]
    
    #makes them integers
    last_price_usdt = int(last_price_usdt_str)
    last_price_blue= int(last_price_blue_str)
    
    emoji_blue = ""
    emoji_usdt = ""
    
    if current_price_blue > last_price_blue: emoji_blue = "up"
    else:                                    emoji_blue = "down"
        
    if current_price_usdt > last_price_usdt: emoji_usdt = "up"
    else:                                    emoji_usdt = "down"
    
    return emoji_usdt, emoji_blue 