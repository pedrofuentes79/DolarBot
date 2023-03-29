from requests import get
def get_blue():
    url = "https://www.dolarsi.com/api/api.php?type=dolar"
    #gets dollar request in json format
    r = get(url).json()
    blue_buy = r[1]["casa"]["compra"]
    blue_sell = r[1]["casa"]["venta"]
    return blue_buy, blue_sell
