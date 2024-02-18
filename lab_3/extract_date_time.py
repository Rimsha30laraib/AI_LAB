#a Python program to extract year, month, date and time using Lambda. 
from datetime import datetime

# Current date and time
current_datetime = datetime.now()

# Lambda functions to extract components
get_year = lambda dt: dt.year
get_month = lambda dt: dt.month
get_day = lambda dt: dt.day
get_time = lambda dt: dt.strftime("%H:%M:%S")

# Use lambda functions to extract components
year = get_year(current_datetime)
month = get_month(current_datetime)
day = get_day(current_datetime)
time = get_time(current_datetime)

# Display the results
print(f"Year: {year}")
print(f"Month: {month}")
print(f"Day: {day}")
print(f"Time: {time}")
