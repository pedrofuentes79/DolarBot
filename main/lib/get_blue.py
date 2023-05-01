import requests

def get_blue():
    url = "https://www.dolarsi.com/api/api.php?type=dolar"
    #gets dollar request in json format
    response = requests.get(url).json()
    blue_buy = response[1]["casa"]["compra"]
    blue_sell = response[1]["casa"]["venta"]
    return blue_buy, blue_sell
