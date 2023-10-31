import requests

def get_blue(mep=True, ccl=True):
    # This will use the DolarSi API since this one provides the MEP value
    url = "https://www.dolarsi.com/api/api.php?type=valoresprincipales"
    response = requests.get(url).json()

    blue_sell = response[1]["casa"]["venta"].replace(",", ".")
    blue_buy  = response[1]["casa"]["compra"].replace(",", ".")

    mep_sell = response[4]["casa"]["venta"].replace(",", ".")[:-1]
    mep_buy  = response[4]["casa"]["compra"].replace(",", ".")[:-1]

    ccl_sell = response[3]["casa"]["venta"].replace(",", ".")
    ccl_buy  = response[3]["casa"]["compra"].replace(",", ".")

    if mep and ccl:
        return blue_sell, mep_sell, ccl_sell
    elif mep:
        return blue_sell, mep_sell
    elif ccl:
        return blue_sell, ccl_sell
    else:
        return blue_sell
