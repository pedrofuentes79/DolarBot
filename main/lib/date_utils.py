import datetime
import pytz
from constants import OPENING, CLOSING

def get_formatted_date():
    # This function returns the rounded actual time 
    # with the format used throughout all the backend for datetime strings
    
    now = datetime.datetime.now(tz=pytz.timezone("America/Argentina/Buenos Aires"))
    rounded_now = now.replace(minute=0, second=0, microsecond=0)
    
    date_str = rounded_now.strftime("%d.%m.%Y:%H.%M")
    date_int = int(rounded_now.timestamp())

    return rounded_now, date_str, date_int
        
def get_message_formatted_date(date_dt):
    #This function returns the reformatted date_str with a specific format
    return date_dt.strftime("%d/%m")

def get_one_hour_less(date_dt):    
    
    '''
    Returns a datetime.datetime object with the Argentina timezone.
    The response will be the input - 1 hour in most cases, except cases such as
    hours coinciding with opening times.
    This function assumes the date_dt is a datetime object with tzinfo.
    It also assumes the minutes, seconds and microseconds in the date_dt will be 0.
    '''
    
    if date_dt.hour == OPENING:
        # Case monday at opening time
        if date_dt.weekday() == 0:
            # substract two days (to make it friday) and the hours required to make it closing time
            output_time = date_dt - datetime.timedelta(days=2, hours=OPENING-CLOSING+24)
            
        # Case Tuesday, Wednesday, Thursday, Friday at opening time
        else:
            # Substract the difference needed to reach the previous day's closing time
            output_time = date_dt - datetime.timedelta(hours=OPENING-CLOSING+24)
            
    # Cases outside of market hours
    # Case before opening time
    elif date_dt.hour < OPENING:

        #Case Monday
        if date_dt.weekday() == 0:
            # substract three days (to make it friday) and set hours to closing time
            output_time = date_dt.replace(hour=CLOSING) - datetime.timedelta(days=3)

        # Case Tuesday, Wednesday, Thursday, Friday, Saturday
        elif date_dt.weekday() <= 5:
            # substract one day and set hours to closing time
            output_time = date_dt.replace(hour=CLOSING) - datetime.timedelta(days=1)

        # Case Sunday
        else:
            # substract two days (to make it friday) and set hours to closing time
            output_time = date_dt.replace(hour=CLOSING) - datetime.timedelta(days=2)

    elif date_dt.hour > CLOSING:

        # Case Monday, Tuesday, Wednesday, Thursday, Friday
        if date_dt.weekday() <= 4:
            # replace hours with closing time
            output_time = date_dt.replace(hour=CLOSING)

        # Case Saturday
        elif date_dt.weekday() == 5:
            # substract one day and set hours to closing time
            output_time = date_dt.replace(hour=CLOSING) - datetime.timedelta(days=1)

        # Case Sunday
        else:
            # substract two days (to make it friday) and set hours to closing time
            output_time = date_dt.replace(hour=CLOSING) - datetime.timedelta(days=2)

    # Case within market hours
    else:
        # Subtract one hour from the input time
        output_time = date_dt - datetime.timedelta(hours=1)
    
    return output_time
    
def get_opening_dt(date_dt):
    return date_dt.replace(hour=OPENING)

def holiday(date_dt):
    # this can be improved by storing the holidays in a database instead of hardcoding them
    holidays = ["21.08.2023:00.00", "13.10.2023:00.00", "16.10.2023:00.00", "20.11.2023:00.00", "8.12.2023:00.00", "25.12.2023:00.00", "01.01.2024:00.00"]
    
    # format holidays to datetime, add tzinfo and replace seconds and microseconds with 0 to match the format of date_dt
    for i in range(len(holidays)):
        holidays[i] = datetime.datetime.strptime(holidays[i], "%d.%m.%Y:%H.%M").replace(
                                                                                second=0, 
                                                                                microsecond=0, 
                                                                                tzinfo=pytz.timezone("America/Argentina/Buenos_Aires"))
    
    # check if current date is a holiday
    return date_dt in holidays

def is_closing_time(date_dt):
    #define global variables
    global CLOSING
    return date_dt.hour == CLOSING

def is_opening_time(date_dt):
    #define global variables
    global OPENING
    return date_dt.hour == OPENING

def is_friday_last_hour(dt):
    #define global variables
    global CLOSING

    return dt.hour == CLOSING and dt.weekday() == 4 

def is_end_month(dt):
    #define global variables
    global CLOSING

    if dt.hour == CLOSING:
        # cases for months with 31 days
        if dt.month in [1, 3, 5, 7, 8, 10, 12]:
            #if its the 31st or the last market day of the month
            return (dt.day == 31) or (dt.weekday() == 4 and dt.day in [29, 30])
        
        #cases for months with 30 days
        elif dt.month in [4, 6, 9, 11]:
            return (dt.day == 30) or (dt.weekday() == 4 and dt.day in [28, 29])
        
        #case for february with 28 days
        elif dt.month == 2 and dt.year % 4 != 0:
            return (dt.day == 28) or (dt.weekday() == 4 and dt.day in [26,27])
        
        #case for february with 29 days
        elif dt.month == 2 and dt.year % 4 == 0:
            return (dt.day == 29) or (dt.weekday() == 4 and dt.day in [27,28])
        else:
            return False
    else:
        return False

def get_month_spanish(dt):
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