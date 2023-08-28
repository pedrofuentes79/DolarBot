import datetime
import dateutil.tz

# Define market opening and closing hours
opening = 10
closing = 17

def get_formatted_date():
    # This function returns the rounded actual time 
    # with the format used throughout all the backend for datetime strings
    
    now = datetime.datetime.now(tz=dateutil.tz.gettz("America/Argentina/Buenos_Aires"))
    rounded_now = now.replace(minute=0, second=0, microsecond=0)
    
    date_str = rounded_now.strftime("%d.%m.%Y:%H.%M")
    date_int = int(rounded_now.timestamp())

    return rounded_now, date_str, date_int
    
    
def get_message_formatted_date(date_str):
    #This function returns the reformatted date_str with a specific format
    
    dt = datetime.datetime.strptime(date_str, "%d.%m.%Y:%H.%M")
    dt = dt.strftime("%d/%m")
    
    return dt

def get_one_hour_less(date_str):    
    
    '''
    Returns a datetime.datetime object with the Argentina timezone.
    The response will be the input - 1 hour in most cases, except cases such as
    hours coinciding with opening times.
    This function assumes the date_str will be in the format "%d.%m.%Y:%H.%M"
    It also assumes the minutes, seconds and microseconds in the date_str will be 0.
    '''
    
    # Define the input format
    input_format = "%d.%m.%Y:%H.%M"
    
    # Check data type
    if isinstance(date_str, datetime.datetime):
        input_time = date_str
    else: 
        # Parse the input time string into a datetime object
        input_time = datetime.datetime.strptime(date_str, input_format)
    
    if input_time.hour == opening:
        # Case monday at opening time
        if input_time.weekday() == 0:
            # substract two days (to make it friday) and the hours required to make it closing time
            output_time = input_time - datetime.timedelta(days=2, hours=opening-closing+24)
            
        # Case Tuesday, Wednesday, Thursday, Friday at opening time
        else:
            # Substract the difference needed to reach the previous day's closing time
            output_time = input_time - datetime.timedelta(hours=opening-closing+24)
            
    # Cases outside of market hours
    # Case before opening time
    elif input_time.hour < opening:

        #Case Monday
        if input_time.weekday() == 0:
            # substract three days (to make it friday) and set hours to closing time
            output_time = input_time.replace(hour=closing) - datetime.timedelta(days=3)

        # Case Tuesday, Wednesday, Thursday, Friday, Saturday
        elif input_time.weekday() <= 5:
            # substract one day and set hours to closing time
            output_time = input_time.replace(hour=closing) - datetime.timedelta(days=1)

        # Case Sunday
        else:
            # substract two days (to make it friday) and set hours to closing time
            output_time = input_time.replace(hour=closing) - datetime.timedelta(days=2)

    elif input_time.hour > closing:

        # Case Monday, Tuesday, Wednesday, Thursday, Friday
        if input_time.weekday() <= 4:
            # replace hours with closing time
            output_time = input_time.replace(hour=closing)

        # Case Saturday
        elif input_time.weekday() == 5:
            # substract one day and set hours to closing time
            output_time = input_time.replace(hour=closing) - datetime.timedelta(days=1)

        # Case Sunday
        else:
            # substract two days (to make it friday) and set hours to closing time
            output_time = input_time.replace(hour=closing) - datetime.timedelta(days=2)

    # Case within market hours
    else:
        # Subtract one hour from the input time
        output_time = input_time - datetime.timedelta(hours=1)
    
    #add tz info
    output_time = output_time.replace(tzinfo=dateutil.tz.gettz("America/Argentina/Buenos_Aires"))
    return output_time
    
def get_opening_dt(date_str):
    current_dt = datetime.datetime.strptime(date_str, "%d.%m.%Y:%H.%M")
    opening_dt = current_dt.replace(hour=opening, tzinfo=dateutil.tz.gettz("America/Argentina/Buenos_Aires"))
    return opening_dt

def holiday(date_str):
    holidays = ["21.08.2023:00.00", "13.10.2023:00.00", "16.10.2023:00.00", "20.11.2023:00.00", "8.12.2023:00.00", "25.12.2023:00.00", "01.01.2024:00.00"]
    
    # format holidays to datetime
    for i in range(len(holidays)):
        holidays[i] = datetime.datetime.strptime(holidays[i], "%d.%m.%Y:%H.%M")
    
    current_dt = datetime.datetime.strptime(date_str, "%d.%m.%Y:%H.%M")
    current_dt = current_dt.replace(hour=0, minute=0)

    # check if current date is a holiday
    return current_dt in holidays

def is_closing_time(date_str):
    #define global variables
    global closing
    
    dt = datetime.datetime.strptime(date_str, "%d.%m.%Y:%H.%M")
    
    return dt.hour == closing


def is_opening_time(date_str):
    #define global variables
    global opening
    
    dt = datetime.datetime.strptime(date_str, "%d.%m.%Y:%H.%M")

    return dt.hour == opening


def is_friday_last_hour(dt):
    #define global variables
    global closing

    return dt.hour == closing and dt.weekday() == 4 

def is_end_month(dt):
    #define global variables
    global closing

    if dt.hour == closing:
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