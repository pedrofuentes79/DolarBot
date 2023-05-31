import datetime
import dateutil.tz

def get_formatted_date():
    
    now = datetime.datetime.now(tz=dateutil.tz.gettz("America/Argentina/Buenos_Aires"))
    date_str = now.strftime("%d.%m.%Y:%H.%M")
    
    return date_str
    
    
def get_message_formatted_date(date_str):
    #This functions returns the reformatted date_str with a specific format
    
    response = datetime.datetime.strptime(date_str, "%d.%m.%Y:%H.%M")
    response = response.strftime("%d.%m.%Y:%H.%M")
    return response

def get_one_hour_less(date_str):

    # Define the input and output format
    input_format = "%d.%m.%Y:%H.%M"
    output_format = "%d.%m.%Y:%H.%M"

    # Parse the input time string into a datetime object
    input_time = datetime.datetime.strptime(date_str, input_format)
    
    
    # Round the minutes to 0
    rounded_input_time = input_time.replace(minutes=0)

    if rounded_input_time.hour == 9:
        # Substract 19 hours, so as to make it 16.00 from the day before
        output_time = rounded_input_time - datetime.timedelta(hours=19)
    else:
        # Subtract one hour from the input time
        output_time = rounded_input_time - datetime.timedelta(hours=1)
    
        # Format the output time as a string
        output_str = output_time.strftime(output_format)

    return output_str