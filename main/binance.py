import requests

def get_p2p_ars_price(mercado_pago=True):
    '''
    Returns the lowest price for buying USDT with ARS and MercadoPago as a payment method
    through Binance's P2P.
    '''

    url = "https://criptoya.com/api/binancep2p/buy/usdt/ars/1000000"
    response = requests.get(url).json()
    sellers = response["data"]

    for i in range(len(sellers)):
        price = sellers[i]["adv"]["price"]
        for j in sellers[i]["adv"]["tradeMethods"]:
            if mercado_pago and (j["identifier"] == "MercadoPagoNew"):
                return price
            
print(type(get_p2p_ars_price()))