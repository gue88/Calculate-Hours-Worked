import csv
import datetime
import time
import pprint

shifts = {}

with open("work.csv") as csv_file:
    csv_reader = csv.reader(csv_file)
    header = next(csv_reader)  # skip the header row
    for row in csv_reader:
        name = row[0]
        times = [item.strip() for item in row[1:] if item.strip()]
        shifts[name] = times
pprint.pprint(shifts, sort_dicts=False)




def convert_time(time):
    start_str, end_str = time.split("-")

    if len(start_str) <= 2:  # checks if hour is less than or equal to 2 digits
        start_time = datetime.datetime.strptime(start_str, "%H").time()
    else:
        start_time = datetime.datetime.strptime(
            f"{float(start_str):0.2f}", "%H.%M"
        ).time()
        # pads 0 to half hour (5.3 -> 5.30)

    if end_str == "close":  # converts 'close' into time
        end_str = "10.30"
        end_time = datetime.datetime.strptime(end_str, "%H.%M").time()
    elif len(end_str) <= 2:
        end_time = datetime.datetime.strptime(end_str, "%H").time()
    else:
        end_time = datetime.datetime.strptime(f"{float(end_str):0.2f}", "%H.%M").time()

    print(start_time, "-", end_time)

    return start_time, end_time


for name, shift in shifts.items():
    print(f"{name}:")
    for time in shift:
        convert_time(time)
