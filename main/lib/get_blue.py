import requests

def get_blue():
    url = "https://api.bluelytics.com.ar/v2/latest"
    #gets dollar request in json format
    response = requests.get(url).json()
    blue_buy = str(response["blue"]["value_buy"])
    blue_sell = str(response["blue"]["value_sell"])
    
    # there must be two digits "after the point"
    # eg: "492.00"
    
    if len(blue_buy.split(".")[1]) == 1:
        blue_buy += "0"
    if len(blue_sell.split(".")[1]) == 1:
        blue_sell += "0"
    
    return blue_buy, blue_sell
