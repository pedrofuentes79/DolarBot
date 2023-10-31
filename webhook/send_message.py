import requests
import os
import datetime
from dateutil import tz

def send_message(message, chat_id):
    TOKEN = os.environ.get("TELEGRAM_API_DOLAR_SCRAPER_TOKEN")
    
    url = 'https://api.telegram.org/bot' + TOKEN + '/sendMessage?chat_id=' + chat_id + '&parse_mode=HTML&text=' + message
    response = requests.get(url)
    print("message response:", response)

def send_message_prices(date_str, opening, closing, chat_id):
    TOKEN = os.environ.get("TELEGRAM_API_DOLAR_SCRAPER_TOKEN")

    message = "Dólar blue " + date_str + "\n" + "APERTURA: " + opening + "\n" + "CIERRE: " + closing


    url = 'https://api.telegram.org/bot' + TOKEN + '/sendMessage?chat_id=' + chat_id + '&parse_mode=HTML&text=' + message
    response = requests.get(url)
    print("prices message response:", response)

def send_current_prices(blue, usdt, mep, chat_id):
    TOKEN = os.environ.get("TELEGRAM_API_DOLAR_SCRAPER_TOKEN")
    
    date_str = datetime.datetime.now(tz=tz.gettz("America/Argentina/Buenos_Aires")).strftime("%d/%m:%H:%M")
    
    message = date_str + "\n" + "Blue: $" + blue +"\n" + "USDT: $" + usdt + "\n" + "MEP: $" + mep
    
    url = "https://api.telegram.org/bot" + TOKEN + "/sendMessage?chat_id=" + chat_id + "&parse_mode=Markdown&text=" + message
    response = requests.get(url).json()
    print("current prices message response:", response)
