import boto3
import datetime
from dateutil import tz

from send_message import send_message
from send_blue_price.get_blue import get_blue
from send_blue_price.get_p2p_ars_price_modified import get_p2p_ars_price

def get_price_data(date_str, chat_id):
    try:
        dt = datetime.datetime.strptime(date_str, "%d/%m/%y")
    except:
        example_dt_str = datetime.datetime.now().strftime("%d/%m/%y")
        send_message("Por favor, chequee el formato de la fecha. Para el día de hoy debería ser así: " + example_dt_str, chat_id)
        return None
    
    
    mytz = tz.gettz("America/Argentina/Buenos_Aires")
    dt_timestamp_00 = int(dt.replace(hour=0, tzinfo=mytz).timestamp())
    dt_timestamp_23 = int(dt.replace(hour=23, tzinfo=mytz).timestamp())
    
    # Init table
    dynamodb = boto3.resource("dynamodb", region_name="us-east-2")
    table = dynamodb.Table("blue_prices")
    
    # Get the data between the timestamps
    response = table.scan(
        FilterExpression="unix_date BETWEEN :start_timestamp AND :end_timestamp",
        ExpressionAttributeValues={
            ":start_timestamp": dt_timestamp_00,
            ":end_timestamp": dt_timestamp_23
        },
        ConsistentRead=True
    )
    
    try:
        data = response["Items"]
        data.sort(key=lambda x: x["unix_date"])
        
        print(data[0])
        #get opening and closing price
        opening_price = data[0]["price"]
        closing_price = data[-1]["price"]
        
        return (opening_price, closing_price)
    except:
        send_message("La base de datos no tiene información para esa fecha", chat_id)
        return None
        
    
def get_today_price():
    buy_blue, sell_blue = get_blue()
    usdt = get_p2p_ars_price(mercado_pago=True)
    
    return sell_blue, usdt