import matplotlib.pyplot as plt
from io import BytesIO
from datetime import datetime as dt
from main.lib.get_chart_data import get_weekly_data, get_monthly_data
import pytz
from date_utils import get_month_spanish

OPENING = 10
CLOSING = 17


def get_weekly_chart(data):
    # sort the data by timestamp
    data.sort(key=lambda x: x["unix_date"])

    dates = [dt.fromtimestamp(x["unix_date"], tz=pytz.timezone('America/Argentina/Buenos_Aires')) for x in data]
    dates_formatted = [x.strftime("%A %H:%M") for x in dates]
    prices = [float(x["price"]) for x in data]
    
    # make the plot so that there are 5 ticks on the x axis
    # these 5 ticks should be the opening and closing times of the last 5 days
    x_ticks = []
    for date in dates:
        if date.hour == OPENING:
            x_ticks.append(date.strftime("%A %H:%M"))
    
    # append the last date for friday's closing time
    x_ticks.append(dates_formatted[-1])

    plt.plot(dates_formatted, prices)
    plt.xticks(x_ticks, rotation=45)
    plt.xlabel("Date")
    plt.ylabel("Price")
    plt.title("Weekly chart")
    plt.tight_layout()
    plt.grid()
    
    # save the plot in a buffer to be sent to telegram
    buffer = BytesIO()
    plt.savefig(buffer, format="png")
    buffer.seek(0)
    plt.close()
    
    return buffer    
def get_monthly_chart(data):
    # sort the data by timestamp
    data.sort(key=lambda x: x["unix_date"])

    dates = [dt.fromtimestamp(x["unix_date"], tz=pytz.timezone('America/Argentina/Buenos_Aires')) for x in data]
    dates_formatted = [x.strftime("%d") for x in dates]
    prices = [float(x["price"]) for x in data]

    mes = get_month_spanish(dates[0])
    
    x_ticks = [date.strftime("%d") for date in dates if (date.hour == CLOSING)]
    
    plt.plot(dates_formatted, prices)
    plt.xticks(x_ticks, rotation=45)
    plt.xlabel("Día")
    plt.ylabel("Precio")
    plt.title(f"Gráfico de {mes}")
    plt.tight_layout()
    plt.grid()

    # save the plot in a buffer to be sent to telegram
    buffer = BytesIO()
    plt.savefig(buffer, format="png")
    buffer.seek(0)
    plt.close()

    return buffer