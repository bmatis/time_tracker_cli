from datetime import datetime, timedelta

# Time conversion experiments

# Converting a time string to a timedelta object
t = datetime.strptime("0:00:12.547760", "%H:%M:%S.%f")
delta = timedelta(hours=t.hour, minutes=t.minute, seconds=t.second, microseconds=t.microsecond)
print(delta)

entries = []
entries.append(delta)
print(entries)

now = datetime.now()
one_year = timedelta(days=365)
future = now + one_year
entries.append(future)

print(entries)
