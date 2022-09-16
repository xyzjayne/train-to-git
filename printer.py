from datetime import datetime
import pytz

def print_time():
    tz = pytz.timezone('US/Los Angeles') 
    now = datetime.now(tz)
    print(now.strftime("%H:%M:%S"))

if __name__ == '__main__':
    print_time()