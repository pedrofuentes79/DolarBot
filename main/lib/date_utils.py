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
    
    # Define global variables
    global opening, closing
    
    # Define the input and output format
    input_format = "%d.%m.%Y:%H.%M"
    output_format = "%d.%m.%Y:%H.%M"
    
    if type(date_str) == datetime.datetime:
        input_time = date_str
    else: 
        # Parse the input time string into a datetime object
        input_time = datetime.datetime.strptime(date_str, input_format)
    

    if input_time.hour == opening:
        # Substract the difference needed to reach the previous day's closing time
        output_time = input_time - datetime.timedelta(hours=opening-closing+24)
    else:
        # Subtract one hour from the input time
        output_time = input_time - datetime.timedelta(hours=1)
    
        # Format the output time as a string
        # output_str = output_time.strftime(output_format)

    return output_time
    



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
    