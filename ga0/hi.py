from datetime import datetime, timedelta

# Define the start and end dates
start_date = datetime(1980, 8, 21)
end_date = datetime(2016, 4, 30)

# Initialize a counter for Wednesdays
wednesday_count = 0

# Loop through each date in the range
current_date = start_date
while current_date <= end_date:
    if current_date.weekday() == 2:  # 2 corresponds to Wednesday
        wednesday_count += 1
    current_date += timedelta(days=1)


print(wednesday_count)