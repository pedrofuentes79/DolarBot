import matplotlib.pyplot as plt
from io import BytesIO
from datetime import datetime as dt


def get_weekly_chart():
    
    weekdays = ["Lunes", "Martes", "Miercoles", "Jueves", "Viernes"]
    closing_prices = [735.00, 735.00, 735.00, 735.00, 735.00]

    plt.plot(weekdays, closing_prices)
    plt.xlabel('Dia de la semana')
    plt.ylabel('Precio del dolar')
    plt.title('Tendencia semanal del dolar')
    plt.xticks(rotation=45)
    
    buffer = BytesIO()
    plt.savefig(buffer, format="png")
    buffer.seek(0)

    plt.close()
    return buffer


def get_monthly_chart():
    pass