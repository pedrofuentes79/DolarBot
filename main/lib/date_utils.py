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

    
    return date_str, date_int
    
    
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