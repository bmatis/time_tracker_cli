from datetime import datetime, timedelta
import json
import csv

import common_functions as cf

class Log():
    """A class for handling the ongoing log of results."""

    def __init__(self, settings):
        """Initialize the log."""
        self.entries = []
        self.log_file = settings.log_file
        self.get_log()

    def get_log(self):
        """Get the log entries from the saved log file."""
        with open(self.log_file) as f:
            reader = csv.reader(f)
            header_row = next(reader)
            print(header_row)

            for row in reader:
                start_time = cf.convert_str_to_datetime(row[0])
                end_time = cf.convert_str_to_datetime(row[1])
                duration = cf.convert_str_to_timedelta(row[2])
                category = row[3]

                entry = {'start_time': start_time, 'end_time': end_time,
                         'duration': duration, 'category': category}
                self.entries.append(entry)

    def add_to_log(self, timer):
        """Add a timer's results to the log."""
        # Get info from the timer and create a log entry dict.
        entry = {'start_time': timer.start_time,
                 'end_time': timer.end_time,
                 'duration': timer.duration,
                 'category': timer.category}

        # Append the log entry to the local entries list.
        self.entries.append(entry)

        # Save the log entry to the log file.
        self.save_entry(entry)

    def save_entry(self, entry):
        """Save an entry to the log file."""
        with open(self.log_file, 'a') as f:
            f.write(str(entry['start_time']) + "," +
                    str(entry['end_time']) + "," +
                    str(entry['duration']) + "," +
                    str(entry['category']) + "\n")

    def display(self, pretty=False):
        """Print the log to the terminal."""
        print("\nLog:")
        print("-" * 30)

        if self.entries == []:
            print("Log is empty...")

        if pretty == False:
            print(self.entries)
        elif pretty == True:
            i = 1
            for entry in self.entries:
                print(str(i) + ". Start:    " + str(entry['start_time']) +
                    "\n   End:      " + str(entry['end_time']) +
                    "\n   Duration: " + str(entry['duration']) +
                    "\n   Category: " + entry['category'])
                i += 1

    def get_category_time_sum(self, category):
        """Adds up the sum of all time for a given category."""
        sum = timedelta(0)
        for entry in self.entries:
            if entry['category'] == category:
                sum += entry['duration']
        return sum

    def save_log(self):
        """Save the entire log to a file."""
        with open(self.log_file, 'a') as f:
            for entry in self.entries:
                f.write(str(entry['start_time']) + "," +
                        str(entry['end_time']) + "," +
                        str(entry['duration']) + "," +
                        str(entry['category']) + "\n")
