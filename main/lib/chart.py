import matplotlib.pyplot as plt
from io import BytesIO
import datetime
from dateutil import tz
from date_utils import get_month_spanish, weekday_to_spanish
from constants import OPENING, CLOSING


def get_weekly_chart(data):
    mytz = tz.gettz('America/Argentina/Buenos_Aires')
    data.sort(key=lambda x: x["unix_date"])

    prices = []
    dates = []
    for x in data:
        curr_dt = datetime.datetime.fromtimestamp(x["unix_date"], tz=mytz)
        # Get only one price per day
        if curr_dt.hour == CLOSING:
            prices.append(float(x["price"]))
            dates.append(curr_dt)
    
    # Get the day of the week in spanish
    dates_formatted = [weekday_to_spanish(date) for date in dates]


    plt.figure(figsize=(10, 6))

    # Shades the area below the curve and plots the curve
    plt.fill_between(dates_formatted, prices, color="skyblue", alpha=0.4)
    plt.plot(dates_formatted, prices, color="Slateblue", alpha=0.6, linewidth=2)

    # Add the percentage change annotation
    percentage_change = round(((prices[-1] - prices[0]) / prices[0]) * 100, 2)
    annotation_text = ("Aumento " if percentage_change > 0 else "Disminución ") + "semanal: " + str(percentage_change) + "%"

    bbox_props = dict(boxstyle='round, pad=0.4', edgecolor='skyblue', facecolor='lightblue')

    plt.text(0.05, 0.9, annotation_text, transform=plt.gca().transAxes, fontsize=12, verticalalignment='top', bbox=bbox_props)

    # Add the price annotation
    for date, price in zip(dates_formatted, prices):
        plt.annotate(f'${price:.2f}', (date, price), textcoords="offset points", xytext=(0, 10), ha='center')

    # Set the plot's limits, labels and title
    plt.ylim(min(prices) * 0.9, max(prices) * 1.05)
    plt.xlabel("Día")
    plt.ylabel("Dólar Blue")
    # agregar entre qué días fue esta semana?
    plt.title("Dólar Blue Semanal")
    plt.tight_layout()
    plt.grid(alpha=0.5)
    
    # Save the plot in a buffer to be sent to telegram
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

    # Shades the area below the curve and plots the curve
    plt.fill_between(dates_formatted, prices, color="skyblue", alpha=0.4)
    plt.plot(dates_formatted, prices, color="Slateblue", alpha=0.6, linewidth=2)

    # Add the percentage change annotation
    percentage_change = round(((prices[-1] - prices[0]) / prices[0]) * 100, 2)
    annotation_text = ("Aumento " if percentage_change > 0 else "Disminución") + "mensual: " + str(percentage_change) + "%"

    bbox_props = dict(boxstyle='round, pad=0.4', edgecolor='skyblue', facecolor='lightblue')

    plt.text(0.05, 0.9, annotation_text, transform=plt.gca().transAxes, fontsize=12, verticalalignment='top', bbox=bbox_props)

    # Set the plot's limits, labels and title
    plt.ylim(min(prices) * 0.8, max(prices) * 1.05)
    plt.xlabel("Día")
    plt.ylabel("Dólar Blue")
    plt.title(f"Dólar Blue en {mes}")
    plt.tight_layout()
    plt.grid(alpha=0.5)

    # Save the plot in a buffer to be sent to telegram
    buffer = BytesIO()
    plt.savefig(buffer, format="png")
    buffer.seek(0)
    plt.close()

    return buffer