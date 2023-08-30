import matplotlib.pyplot as plt
from io import BytesIO
import datetime
from dateutil import tz
from date_utils import get_month_spanish
from constants import OPENING, CLOSING


def get_weekly_chart(data):
    mytz = tz.gettz('America/Argentina/Buenos_Aires')
    data.sort(key=lambda x: x["unix_date"])

    prices = []
    dates = []
    for x in data:
        curr_dt = datetime.datetime.fromtimestamp(x["unix_date"], tz=mytz)
        # only one price per day
        if curr_dt.hour == CLOSING:
            prices.append(float(x["price"]))
            dates.append(curr_dt)
    
    dates_formatted = [date.strftime("%d") for date in dates]

    plt.figure(figsize=(10, 6))

    plt.fill_between(dates_formatted, prices, color="skyblue", alpha=0.4)
    plt.plot(dates_formatted, prices, color="Slateblue", alpha=0.6, linewidth=2)
    
    plt.ylim(min(prices) * 0.9, max(prices) * 1.05)
    plt.xlabel("Día")
    plt.ylabel("Precio")
    plt.tight_layout()
    plt.grid(alpha=0.5)
    
    # save the plot in a buffer to be sent to telegram
    buffer = BytesIO()
    plt.savefig(buffer, format="png")
    buffer.seek(0)
    plt.close()
    
    return buffer    

def get_monthly_chart(data):
    mytz = tz.gettz('America/Argentina/Buenos_Aires')
    data.sort(key=lambda x: x["unix_date"])

    prices = []
    dates = []
    for x in data:
        curr_dt = datetime.datetime.fromtimestamp(x["unix_date"], tz=mytz)
        # only one price per day
        if curr_dt.hour == CLOSING:
            prices.append(float(x["price"]))
            dates.append(curr_dt)

    mes = get_month_spanish(dates[0].month)
    
    dates_formatted = [date.strftime("%d") for date in dates]

    plt.figure(figsize=(10, 6))

    # Shades the are below the curve
    plt.fill_between(dates_formatted, prices, color="skyblue", alpha=0.4)
    # Plots the curve
    plt.plot(dates_formatted, prices, color="Slateblue", alpha=0.6, linewidth=2)
    
    plt.ylim(min(prices) * 0.8, max(prices) * 1.05)
    plt.xlabel("Día")
    plt.ylabel("Dólar Blue")
    plt.title(f"Dólar Blue en {mes}")
    plt.tight_layout()
    plt.grid(alpha=0.5)

    # save the plot in a buffer to be sent to telegram
    buffer = BytesIO()
    plt.savefig(buffer, format="png")
    buffer.seek(0)
    plt.close()

    return buffer