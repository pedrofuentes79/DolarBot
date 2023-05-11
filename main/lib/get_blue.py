import requests

def get_blue():
    url = "https://www.dolarsi.com/api/api.php?type=dolar"
    #gets dollar request in json format
    response = requests.get(url).json()
    blue_buy = response[1]["casa"]["compra"]
    blue_sell = response[1]["casa"]["venta"]
    
    #reformats the values so that they end with two decimals and use . instead of , for decimals
    blue_buy = blue_buy[:-4] + ".00"
    blue_sell = blue_sell[:-4] + ".00"
    
    return blue_buy, blue_sell
