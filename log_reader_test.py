import csv
from datetime import datetime, timedelta

import common_functions as cf

filename = 'log.csv'

with open(filename) as f:
    reader = csv.reader(f)
    header_row = next(reader)
    print(header_row)

    log_entries = []

    for row in reader:
        start_time = row[0]
        start_time = cf.convert_str_to_datetime(start_time)

        end_time = row[1]
        end_time = cf.convert_str_to_datetime(end_time)

        duration = row[2]
        duration = cf.convert_str_to_timedelta(duration)

        category = row[3]

        entry = {'start_time': start_time, 'end_time': end_time,
                 'duration': duration, 'category': category}
        log_entries.append(entry)

total_duration = timedelta(0)

for entry in log_entries:
    print(entry)
    total_duration += entry['duration']

print(total_duration)

#print(log_entries)


# Time conversion experiments

# Converting a time string to a timedelta object
# t = datetime.strptime("0:00:12.547760", "%H:%M:%S.%f")
# delta = timedelta(hours=t.hour, minutes=t.minute, seconds=t.second, microseconds=t.microsecond)
# print(delta)
#
# entries = []
# entries.append(delta)
# print(entries)
#
# now = datetime.now()
# one_year = timedelta(days=365)
# future = now + one_year
# entries.append(future)
#
# print(entries)
