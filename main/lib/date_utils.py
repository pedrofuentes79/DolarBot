import datetime
import dateutil.tz

def get_formatted_date():
    
    now = datetime.datetime.now(tz=dateutil.tz.gettz("America/Argentina/Buenos_Aires"))
    date_str = now.strftime("%d.%m.%Y:%H.%M")
    
    return date_str

def get_one_hour_less(date_str):

    # Define the input and output format
    input_format = "%d.%m.%Y:%H.%M"
    output_format = "%d.%m.%Y:%H.%M"

    # Parse the input time string into a datetime object
    input_time = datetime.datetime.strptime(date_str, input_format)

    # Subtract one hour from the input time
    output_time = input_time - datetime.timedelta(hours=1)

    # Format the output time as a string
    output_str = output_time.strftime(output_format)

    return output_str