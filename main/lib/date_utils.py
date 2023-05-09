import datetime

def get_formatted_date():
    
    now = datetime.datetime.now()
    date_str = now.strftime("%d.%m.%Y:%H.%M")
    
    return date_str