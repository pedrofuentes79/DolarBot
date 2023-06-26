import requests
import numpy as np
from last_price_utils import get_previous_prices


def get_p2p_ars_price(mercado_pago:bool, date_str:str):
    '''
    Returns the lowest price for buying USDT with ARS and MercadoPago as a payment method
    through Binance's P2P.
    Sellers must offer to sell at least $30.000 ARS and have at least 50 USDT available.
    '''

    url = "https://criptoya.com/api/binancep2p/buy/usdt/ars/1000000"
    response = requests.get(url).json()
    sellers = response["data"]
    
    if mercado_pago:
        # Get the first 5 sellers that accept MercadoPago and offer to sell $30000 or more ARS

        mp_sellers = []
        for seller in sellers:
            tradeMethods = seller["adv"]["tradeMethods"]
            if len(mp_sellers) == 5:
                    break
            for method in tradeMethods:
                if (method["tradeMethodName"] == "Mercadopago" and float(seller["adv"]["minSingleTransAmount"]) >= 25000 and float(seller["adv"]["surplusAmount"]) >= 50.0 ):
                    #if conditions are met, add seller to list
                    mp_sellers.append(seller)
    else:
        return sellers[0]["adv"]["price"]
    
    if mp_sellers != []:
        # Calculate average price on the mp_sellers list if its not empty
        prices = np.array([])
        for seller in mp_sellers:
            prices = np.append(prices, float(seller["adv"]["price"]))
        
        # Calculate mean price rounded to 2 decimals
        mean_price = round(np.mean(prices), 2)
        
        return str(mean_price)
    else:
        # If there are no sellers, repeat the previous price.
        _, last_price_usdt = get_previous_prices(date_str=date_str)
        return last_price_usdt

