import requests
import os
import datetime

def send_message(message, chat_id):
    TOKEN = os.environ.get("TELEGRAM_API_DOLAR_SCRAPER_TOKEN")
    
    url = 'https://api.telegram.org/bot' + TOKEN + '/sendMessage?chat_id=' + chat_id + '&parse_mode=HTML&text=' + message
    response = requests.get(url)
    print(response)

def send_message_prices(date_str, opening, closing, chat_id):
    TOKEN = os.environ.get("TELEGRAM_API_DOLAR_SCRAPER_TOKEN")

    message = "Dólar blue " + date_str + "\n" + "APERTURA: " + opening + "\n" + "CIERRE: " + closing


    url = 'https://api.telegram.org/bot' + TOKEN + '/sendMessage?chat_id=' + chat_id + '&parse_mode=HTML&text=' + message
    response = requests.get(url)
    return response

def send_current_prices(blue, usdt, chat_id):
    TOKEN = os.environ.get("TELEGRAM_API_DOLAR_SCRAPER_TOKEN")
    
    date_str = datetime.datetime.now().strftime("%d/%m:%H:%M")
    
    message = date_str + "\n" + "Blue: $" + blue +"\n" + "USDT: $" + usdt
    
    url = "https://api.telegram.org/bot" + TOKEN + "/sendMessage?chat_id=" + chat_id + "&parse_mode=Markdown&text=" + message
    response = requests.get(url).json()
    return response