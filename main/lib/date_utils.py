import datetime
from dateutil import tz
from constants import OPENING, CLOSING

def get_formatted_date():
    # Returns the rounded actual time in the Argentina timezone.
    # Also returns the date as a string and as an int (unix timestamp)
    
    now = datetime.datetime.now(tz=tz.gettz("America/Argentina/Buenos Aires"))
    rounded_now = now.replace(minute=0, second=0, microsecond=0)
    
    date_str = rounded_now.strftime("%d.%m.%Y:%H.%M")
    date_int = int(rounded_now.timestamp())

    return rounded_now, date_str, date_int
        
def get_message_formatted_date(date_dt):
    # This function returns the date as a string in the format "dd/mm"
    return date_dt.strftime("%d/%m")

def get_one_hour_less(date_dt):    
    # Returns a datetime.datetime object with the Argentina timezone.
    # The objective of the function is to return the previous market hour.
    # The response will be previous hour in most cases, except cases such as hours coinciding with opening times.
    # This function assumes the date_dt is a datetime object with tzinfo.
    # It also assumes the minutes, seconds and microseconds in the date_dt will be 0.
    
    hour = date_dt.hour
    weekday = date_dt.weekday()

    # Case saturday
    if weekday == 5:
        # Substract one day and set the hour to closing time
        output_time = (date_dt - datetime.timedelta(days=1)).replace(hour=CLOSING)
    # Case sunday
    elif weekday == 6:
        # Substract two days and set the hour to closing time
        output_time = (date_dt - datetime.timedelta(days=2)).replace(hour=CLOSING)

    # Case monday
    elif weekday == 0:
        # Case before opening time
        if hour <= OPENING:
            # Substract three days and set the hour to closing time
            output_time = (date_dt - datetime.timedelta(days=3)).replace(hour=CLOSING)
        # Case after closing time
        elif hour > CLOSING:
            # Set the hour to closing time
            output_time = date_dt.replace(hour=CLOSING)
        # Case between opening and closing time
        else:
            # Substract one hour
            output_time = date_dt - datetime.timedelta(hours=1)
    
    # Case tuesday, wednesday, thursday or friday
    else:
        # Case before opening time
        if hour <= OPENING:
            # Substract one day and set the hour to closing time
            output_time = (date_dt - datetime.timedelta(days=1)).replace(hour=CLOSING)
        # Case after closing time
        elif hour > CLOSING:
            # Set the hour to closing time
            output_time = date_dt.replace(hour=CLOSING)
        # Case between opening and closing time
        else:
            # Substract one hour
            output_time = date_dt - datetime.timedelta(hours=1)
    
    return output_time
    
def get_opening_dt(date_dt):
    # Returns the datetime object with the opening hour.
    return date_dt.replace(hour=OPENING)

def holiday(date_dt):
    # this can be improved by storing the holidays in a database instead of hardcoding them
    holidays = ["21.08.2023:00.00", "13.10.2023:00.00", "16.10.2023:00.00", "20.11.2023:00.00", "8.12.2023:00.00", "25.12.2023:00.00", "01.01.2024:00.00"]
    
    # Format holidays to datetime, add tzinfo and replace seconds and microseconds with 0 to match the format of date_dt
    for i in range(len(holidays)):
        holidays[i] = datetime.datetime.strptime(holidays[i], "%d.%m.%Y:%H.%M").replace(
                                                                                second=0, 
                                                                                microsecond=0, 
                                                                                tzinfo=tz.gettz("America/Argentina/Buenos_Aires"))
    
    # check if current date is a holiday
    return date_dt in holidays

def is_closing_time(date_dt):
    # Returns True if the input datetime object is at closing time
    return date_dt.hour == CLOSING

def is_opening_time(date_dt):
    # Returns True if the input datetime object is at opening time
    return date_dt.hour == OPENING

def is_friday_last_hour(dt):
    # Returns True if the input datetime object is the last hour of the last market day of the week
    return dt.hour == CLOSING and dt.weekday() == 4 

def is_end_month(dt):
    # Returns True if the input datetime object is the last hour of the last market day of the month

    if dt.hour == CLOSING:
        # Cases for months with 31 days
        if dt.month in [1, 3, 5, 7, 8, 10, 12]:
            #if its the 31st or the last market day of the month
            return (dt.day == 31) or (dt.weekday() == 4 and dt.day in [29, 30])
        
        # Cases for months with 30 days
        elif dt.month in [4, 6, 9, 11]:
            return (dt.day == 30) or (dt.weekday() == 4 and dt.day in [28, 29])
        
        # Case for february with 28 days
        elif dt.month == 2 and (dt.year % 4 != 0 or (dt.year % 100 == 0 and dt.year % 400 != 0)):
            return (dt.day == 28) or (dt.weekday() == 4 and dt.day in [26,27])
        
        # Case for february with 29 days
        elif dt.month == 2 and (dt.year % 4 == 0 or (dt.year % 100 != 0 and dt.year % 400 == 0)):
            return (dt.day == 29) or (dt.weekday() == 4 and dt.day in [27,28])
        else:
            return False
    else:
        return False

def get_month_spanish(dt):
    # Returns the datetime's month in spanish

    month = dt.month

    if month == 1:
        return "Enero"
    elif month == 2:
        return "Febrero"
    elif month == 3:
        return "Marzo"
    elif month == 4:
        return "Abril"
    elif month == 5:
        return "Mayo"
    elif month == 6:
        return "Junio"
    elif month == 7:
        return "Julio"
    elif month == 8:
        return "Agosto"
    elif month == 9:
        return "Septiembre"
    elif month == 10:
        return "Octubre"
    elif month == 11:
        return "Noviembre"
    elif month == 12:
        return "Diciembre"
    else:
        return "Error"
    
def weekday_to_spanish(dt):
    # Returns the datetime's weekday in spanishs
    weekday = dt.weekday()
    
    if weekday == 0:
        return "Lunes"
    elif weekday == 1:
        return "Martes"
    elif weekday == 2:
        return "Miércoles"
    elif weekday == 3:
        return "Jueves"
    elif weekday == 4:
        return "Viernes"
    elif weekday == 5:
        return "Sábado"
    elif weekday == 6:
        return "Domingo"
    else:
        return "Error"